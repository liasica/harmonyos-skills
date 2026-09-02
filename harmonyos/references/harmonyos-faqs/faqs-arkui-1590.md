---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1590
title: 如何在页面间进行数据共享和UI同步更新
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何在页面间进行数据共享和UI同步更新
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c162c6a46f30644282da5943efe3bbe097c3e94b3fcc3424281c64e76902e286
---

## 问题现象

父子组件间数据双向同步时，可以将需要共享的数据作为子组件的入参传入，子组件通过[@Link](../harmonyos-guides/arkts-link.md)/[@ObjectLink](../harmonyos-guides/arkts-observed-and-objectlink.md)/[@Param](../harmonyos-guides/arkts-new-param.md)等装饰器接收，从而实现数据的传递与共享。如果需要进行页面间的数据共享和UI的同步更新，该如何实现呢？

## 背景知识

* [LocalStorage](../harmonyos-guides/arkts-localstorage.md)是页面级的UI状态存储，通过@Entry装饰器接收的参数可以在页面内共享同一个LocalStorage实例。
* [AppStorage](../harmonyos-guides/arkts-appstorage.md)是与应用进程绑定的全局UI状态存储中心，由UI框架在应用启动时创建，将UI状态数据存储于运行内存，实现应用级全局状态共享。
* [AppStorageV2](../harmonyos-guides/arkts-new-appstoragev2.md)提供应用级全局共享状态变量的能力，开发者可以通过connect绑定同一个key，进行跨ability的数据共享。

## 解决方案

* **方案一**：创建可观测的全局单例对象，将数据初始化保存在单例中，在需要使用数据的地方引入，实现一处修改，所有使用数据的地方同步刷新UI。以简易通讯录为例：
  1. 创建单例。

     ```ts
     @ObservedV2
     export class OptionTwoDetail {
       @Trace name: string = 'name';
       @Trace callNumber: string = '123456';

       constructor(name: string, callNumber: string) {
         this.name = name;
         this.callNumber = callNumber;
       }
     }

     @ObservedV2
     export class OptionTwoUsers {
       @Trace userArr: OptionTwoDetail[] = [];

       constructor() {
         this.userArr.push(new OptionTwoDetail('张一', '111111'));
         this.userArr.push(new OptionTwoDetail('李四', '222222'));
       }
     }

     export class OptionTwoCommonModel {
       static instance: OptionTwoCommonModel;
       private users: OptionTwoUsers = new OptionTwoUsers();

       public static getInstance() {
         if (!OptionTwoCommonModel.instance) {
           OptionTwoCommonModel.instance = new OptionTwoCommonModel();
         }
         return OptionTwoCommonModel.instance;
       }

       // 替换通讯录
       init(users: OptionTwoUsers) {
         this.users.userArr = users.userArr;
       }

       // 增加联系人
       add(detail: OptionTwoDetail) {
         this.users.userArr.push(detail);
       }

       // 返回通讯录单例
       getUser() {
         return this.users;
       }

       private constructor() {
       }
     }
     ```
  2. 创建主页面。

     ```ts
     import { OptionTwoCommonModel, OptionTwoUsers, OptionTwoDetail } from './OptionTwoSingleViewModel';

     @Entry
     @ComponentV2
     struct OptionTwoPageA {
       @Local user: OptionTwoUsers = OptionTwoCommonModel.getInstance().getUser();

       build() {
         Column() {
           Text('通讯录')
             .fontSize(40);
           List() {
             ForEach(this.user.userArr, (item: OptionTwoDetail, index: number) => {
               ListItem() {
                 Column() {
                   Text(`姓名：${item.name}`)
                     .margin({ left: 20 });
                   Text(`电话：${item.callNumber}`)
                     .margin({ left: 20 });
                 }
                 .width('100%')
                 .alignItems(HorizontalAlign.Start)
                 .onClick(() => {
                   this.getUIContext().getRouter().pushUrl({
                     url: 'pages/OptionTwo/OptionTwoPageB',
                     params: { index: index }
                   });
                 });
               }
               .width('100%')
               .backgroundColor('#ffdedede')
               .borderRadius(15)
               .margin({
                 top: 10,
                 bottom: 10
               });
             });
           }
           .height('100%')
           .width('90%');
         }
         .justifyContent(FlexAlign.Center)
         .width('100%');
       }
     }
     ```
  3. 创建详情页面，获取单例对象并实现数据修改。

     ```ts
     import { OptionTwoCommonModel, OptionTwoUsers } from './OptionTwoSingleViewModel';

     @Entry
     @ComponentV2
     struct OptionTwoPageB {
       @Local user: OptionTwoUsers = OptionTwoCommonModel.instance.getUser(); // 获取单例User
       @Local userIndex: number = 0;

       aboutToAppear(): void {
         let param = this.getUIContext().getRouter().getParams() as Param;
         this.userIndex = param.index; // 获取点击跳转item的索引位置
       }

       build() {
         Column() {
           Text('用户详情修改')
             .fontSize(40)
             .margin({
               bottom: 50
             });
           Text('姓名');
           TextInput({ text: this.user.userArr[this.userIndex].name!!, placeholder: '请输入姓名' })
             .width('90%');
           Text('电话').margin({ top: 10 });
           TextInput({
             text: this.user.userArr[this.userIndex].callNumber!!,
             placeholder: '请输入电话号码'
           })
             .width('90%'); // 未限制只能输入数字，可自行添加限制
           Button('修改完成点击返回')
             .margin({ top: 20 })
             .onClick(() => {
               this.getUIContext().getRouter().back();
             });
         }
         .height('100%')
         .width('100%');
       }
     }

     class Param {
       index: number = 0;
     }
     ```
  4. 在项目的“entry/src/main/resources/base/profile/main\_pages.json”中配置路由。

     ```json
     {
       "src": [
         "pages/OptionTwo/OptionTwoPageA",
         "pages/OptionTwo/OptionTwoPageB",
         "pages/OptionThree/OptionThreePageA",
         "pages/OptionThree/OptionThreePageB"
       ]
     }
     ```

* **方案二**：状态管理V1可以使用LocalStorage和AppStorage实现页面间的数据共享，案例可以参考官网示例：[将LocalStorage实例从UIAbility共享到一个或多个页面](../harmonyos-guides/arkts-localstorage.md#将localstorage实例从uiability共享到一个或多个页面)。状态管理V2可以配合[@ObservedV2和@Trace](../harmonyos-guides/arkts-new-observedv2-and-trace.md)实现深层嵌套数据的同步和UI刷新。以简易通讯录为例：
  1. 使用@ObservedV2和@Trace实现深度观测。

     ```ts
     @ObservedV2
     export class OptionThreeDetail {
       @Trace name: string = 'name';
       @Trace callNumber: string = '123456';

       constructor(name: string, callNumber: string) {
         this.name = name;
         this.callNumber = callNumber;
       }
     }

     @ObservedV2
     export class OptionThreeUser {
       @Trace userArr: OptionThreeDetail[] = [];

       constructor() {
         this.userArr.push(new OptionThreeDetail('张一', '111111'));
         this.userArr.push(new OptionThreeDetail('李四', '222222'));
       }
     }
     ```
  2. 创建主页面，通过AppStorageV2.connect储存通讯录数据并实现双向绑定。

     ```ts
     import { OptionThreeUser, OptionThreeDetail } from './OptionThreeViewModel';
     import { AppStorageV2 } from '@kit.ArkUI';

     @Entry
     @ComponentV2
     struct OptionThreePageA {
       @Local user: OptionThreeUser = AppStorageV2.connect(OptionThreeUser, 'OptionThreeUser', () => new OptionThreeUser())!;

       build() {
         Column() {
           Text('通讯录')
             .fontSize(40);
           List() {
             ForEach(this.user.userArr, (item: OptionThreeDetail, index: number) => {
               ListItem() {
                 Column() {
                   Text(`姓名：${item.name}`)
                     .margin({ left: 20 });
                   Text(`电话：${item.callNumber}`)
                     .margin({ left: 20 });
                 }
                 .width('100%')
                 .alignItems(HorizontalAlign.Start)
                 .onClick(() => {
                   this.getUIContext().getRouter().pushUrl({
                     url: 'pages/OptionThree/OptionThreePageB',
                     params: { index: index }
                   });
                 });
               }
               .width('100%')
               .backgroundColor('#ffdedede')
               .borderRadius(15)
               .margin({
                 top: 10,
                 bottom: 10
               });
             });
           }
           .height('100%')
           .width('90%');
         }
         .justifyContent(FlexAlign.Center)
         .width('100%');
       }
     }
     ```
  3. 创建详情页面，同样通过AppStorageV2.connect实现双向绑定，实现数据修改时同步到主页面。

     ```ts
     import { OptionThreeUser } from './OptionThreeViewModel';
     import { AppStorageV2 } from '@kit.ArkUI';

     @Entry
     @ComponentV2
     struct OptionThreePageB {
       @Local user: OptionThreeUser = AppStorageV2.connect(OptionThreeUser, 'OptionThreeUser', () => new OptionThreeUser())!;
       @Local userIndex: number = 0;

       aboutToAppear(): void {
         let param = this.getUIContext().getRouter().getParams() as Param;
         this.userIndex = param.index; // 获取点击跳转item的索引位置
       }

       build() {
         Column() {
           Text('用户详情修改')
             .fontSize(40)
             .margin({
               bottom: 50
             });
           Text('姓名');
           TextInput({ text: this.user.userArr[this.userIndex].name!!, placeholder: '请输入姓名' })
             .width('90%');
           Text('电话').margin({ top: 10 });
           TextInput({
             text: this.user.userArr[this.userIndex].callNumber!!,
             placeholder: '请输入电话号码'
           })
             .width('90%'); // 未限制只能输入数字，可自行添加限制
           Button('修改完成点击返回')
             .margin({ top: 20 })
             .onClick(() => {
               this.getUIContext().getRouter().back();
             });
         }
         .height('100%')
         .width('100%');
       }
     }

     class Param {
       index: number = 0;
     }
     ```
  4. 在项目的“entry/src/main/resources/base/profile/main\_pages.json”中配置路由。

     ```json
     {
       "src": [
         "pages/OptionTwo/OptionTwoPageA",
         "pages/OptionTwo/OptionTwoPageB",
         "pages/OptionThree/OptionThreePageA",
         "pages/OptionThree/OptionThreePageB"
       ]
     }
     ```

方案一和方案二实现效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/_lxPs6JISn6UWNxuYI6Ltg/zh-cn_image_0000002628610308.gif "点击放大")

## 常见FAQ

Q：除了状态管理是否还有其它实现页面间数据共享的方式？

A：可以使用[Emitter](../harmonyos-references/js-apis-emitter.md)的能力。在所有需要数据共享的页面使用emitter.on订阅同步数据，在其他界面中通过emitter.emit发布数据变动的事件，实现各界面更新数据。但是该方式操作不当容易造成内存泄漏。

Q：AppStorageV2是否适配ArkUI-X？

A：AppStorageV2暂未适配ArkUI-X。
