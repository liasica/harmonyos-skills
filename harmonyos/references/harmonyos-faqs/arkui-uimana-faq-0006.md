---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0006
title: ArkUI状态管理与组件通信常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > ArkUI状态管理与组件通信常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:10+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:683825beec8b8aee05d7350f48e61ed5cd867868d997fb6d8d88de25d1bf2061
---

**Q：PersistentStorage本身不支持对象或者数组类型的存储，如何处理数据才能满足存储的条件，实现对象和数组类型的存储？**

**A**：处理方式如下：

* 场景一：储存没有方法的对象数组。对于没有方法的类，把数组数据通过JSON.stringify()转换为字符串，然后再进行存储。读取的时候，直接用JSON.parse()解析后进行使用即可，参考示例代码如下：

  ```ts
  class SceneOneStudent {
    name: string;
    age: number;

    constructor(name: string, age: number) {
      this.name = name;
      this.age = age;
    }
  }

  PersistentStorage.persistProp('studentArr',
    JSON.stringify([new SceneOneStudent('Tom', 16), new SceneOneStudent('Gina', 18)]));

  @Entry
  @Component
  struct SceneOne {
    @State studentArr: Array<SceneOneStudent> = [];
    @StorageLink('studentArr') @Watch('onStrChange') studentArrStr: string = ' '; // 获取对象数组序列化字符串

    onStrChange() {
      this.studentArr = JSON.parse(this.studentArrStr);
    }

    aboutToAppear(): void {
      // 组件初始化时不会触发Watch事件，通过aboutToAppear事件来初始化数组
      this.studentArr = JSON.parse(this.studentArrStr);
    }

    build() {
      Column({ space: 8 }) {
        ForEach(this.studentArr, (item: SceneOneStudent) => {
          Column() {
            Text(`Student Name: ${item.name}`)
              .width('100%');
            Text(`Student Age: ${item.age}`)
              .width('100%');
          }
          .borderRadius(12)
          .width('100%')
          .backgroundColor(Color.White)
          .padding(16);
        }, (item: SceneOneStudent) => JSON.stringify(item));
      }
      .width('100%')
      .height('100%')
      .backgroundColor('# f1f3f5')
      .padding(12);
    }
  }
  ```
* 场景二：储存自带方法的对象数组。

  对于有方法函数的类，需要先把字符串转成数据数组，然后调用类的构造函数利用每个数据创建出一个对象，这样创建的对象才有原型链，才能调用对应的方法，参考代码如下所示：

  ```ts
  class SceneTwoStudent {
    name: string;
    age: number;

    constructor(name: string, age: number) {
      this.name = name;
      this.age = age;
    }

    selfIntroduction() {
      console.info(`My name is ${this.name} and I'm ${this.age} years old.`);
    }
  }

  PersistentStorage.persistProp('studentArr',
    JSON.stringify([new SceneTwoStudent('Tom', 16), new SceneTwoStudent('Gina', 18)]));

  @Entry
  @Component
  struct SceneTwo {
    @State studentArr: Array<SceneTwoStudent> = [];
    @StorageLink('studentArr') @Watch('onStrChange') studentArrStr: string = ' '; // 获取对象数组序列化的字符串

    onStrChange() {
      const dataArr: Array<SceneTwoStudent> = JSON.parse(this.studentArrStr); // 转化为对象数组
      this.studentArr = dataArr.map((item: SceneTwoStudent) => new SceneTwoStudent(item.name, item.age)); // 重新构造对象数组
    }

    aboutToAppear(): void {
      // 组件初始化时不会触发Watch事件，通过aboutToAppear事件来初始化数组
      const dataArr: Array<SceneTwoStudent> = JSON.parse(this.studentArrStr); // 转化为对象数组
      this.studentArr = dataArr.map((item: SceneTwoStudent) => new SceneTwoStudent(item.name, item.age)); // 重新构造对象数组
    }

    build() {
      Column({ space: 8 }) {
        ForEach(this.studentArr, (item: SceneTwoStudent) => {
          Column() {
            Text(`Student Name: ${item.name}`)
              .width('100%');
            Text(`Student Age: ${item.age}`)
              .width('100%');
            Button('Get Self-introduction')
              .onClick(() => {
                item.selfIntroduction();
              });
          }
          .borderRadius(12)
          .width('100%')
          .backgroundColor(Color.White)
          .padding(16);
        }, (item: SceneTwoStudent) => JSON.stringify(item));
      }
      .width('100%')
      .height('100%')
      .backgroundColor('# f1f3f5')
      .padding(12);
    }
  }
  ```

**Q：在ArkTS并发开发过程中，子线程需要用到AppStorage这类UI资源时，子线程中无法直接访问，有无其他替换方案？（以taskpool中使用AppStorage为例说明）**

**A**：由上面的背景知识可知，AppStorage一般存放应用全局的UI状态，供UI主线程使用，taskpool子线程中无法直接使用，如果想要实现taskpool子线程访问全局UI状态，有以下三种方案：

方案一：借助taskpool参数传递：

1. 将需要在子线程中使用的数据从AppStorage中抽取出来，封装成类；
2. 在UI主线程新建taskpool时，通过初始化参数直接将AppStorage指定的值传递给taskpool子线程；
3. 如果taskpool子线程需要修改AppStorage值且通知UI主线程，可以通过taskpool.Task.sendData发送，UI主线程接收再处理UI刷新。

   ```ts
   import { taskpool } from '@kit.ArkTS';

   @Concurrent
   async function taskpoolFunc2(vaTmp: AppstorageTmpValues): Promise<AppstorageTmpValues> {
     // 在taskpool子线程中直接读AppStorage里面的值,会报错ReferenceError: AppStorage is not defined
     console.info('taskpool backupId:' + vaTmp.backupId); // 输出22222
     console.info('taskpool isLightMode:' + vaTmp.isLightMode); // 输出true
     taskpool.Task.sendData(vaTmp);
     vaTmp.backupId = '33333';
     vaTmp.isLightMode = false;
     taskpool.Task.sendData(vaTmp);
     return vaTmp;
   }

   async function mainFunc(): Promise<void> {
     AppStorage.setOrCreate('backupId', '22222');
     let appStateTmp: AppstorageTmpValues = {
       isLightMode: AppStorage.get('isLightMode') as boolean,
       backupId: AppStorage.get('backupId') as string
     };
     // 直接将AppStorage指定值作为参数传递给taskpool子线程
     let task2: taskpool.Task = new taskpool.Task(taskpoolFunc2, appStateTmp);
     // 设置notice方法接收子线程发送的消息
     task2.onReceiveData(notice);
     let res2: AppstorageTmpValues = await taskpool.execute(task2) as AppstorageTmpValues;
     console.info("ui main get backupId: " + res2.backupId); // 输出33333
     console.info("ui main get isLightMode: " + res2.isLightMode); // 输出false
   }

   function notice(data: AppstorageTmpValues): void {
     console.info("接收并解析子线程发出的消息");
     console.info('backupId:' + data.backupId);
     console.info('isLightMode:' + data.isLightMode);
     AppStorage.setOrCreate('backupId', data.backupId);
     AppStorage.setOrCreate('isLightMode', data.isLightMode);
   }

   @Entry
   @Component
   struct WayOne {
     @StorageLink('isLightMode') isLightMode: boolean = true;
     @StorageLink('backupId') backupId: string = '11111';

     aboutToAppear(): void {
       AppStorage.setOrCreate('isLightMode', true);
       AppStorage.setOrCreate('backupId', '11111');
     }

     build() {
       Row() {
         Column({ space: 10 }) {
           Text(`isLightMode:${this.isLightMode}`);
           Text(`backupId:${this.backupId}`);
           Button('taskpoolEmitterTest')
             .onClick(async () => {
               mainFunc();
             });
         }
         .width('100%')
         .height('100%');
       };
     }
   }

   export interface AppstorageTmpValues {
     isLightMode?: boolean;
     backupId?: string;
   }
   ```

方案二：借助进程不同线程间Emitter事件处理机制：

这里以主线程通知子线程，在子线程中访问AppStorage为例说明：

1. 在主线程中将AppStorage中的数据读取到emitter.EventData，创建emitter事件；
2. 在主线程中将事件数据发送给子线程；
3. 在子线程中读取事件数据，进行使用。

   ```ts
   import { emitter } from '@kit.BasicServicesKit';
   import { taskpool } from '@kit.ArkTS';

   @Concurrent
   async function taskpoolFunc(isLightModeTmp: boolean): Promise<string> {
     console.info('UI主线程过来数据isLightMode:' + isLightModeTmp);
     let backupIdTmp: string = '';
     // 在taskpool子线程中直接读AppStorage里面的值,会报错ReferenceError: AppStorage is not defined
     emitter.on("eventIdTmp", (eventData: emitter.EventData) => {
       let data = eventData?.data;
       if (data) {
         const isLightMode: boolean = data.isLightMode as boolean;
         backupIdTmp = data.backupId as string;
         console.info('通过emitter接收UI主线程的isLightMode:' + isLightMode);
         console.info('通过emitter接收UI主线程的backupId:' + backupIdTmp);
       }
     });
     return backupIdTmp;
   }

   async function mainFunc(): Promise<void> {
     // 直接将AppStorage值作为参数传递给taskpool子线程
     let task1: taskpool.Task = new taskpool.Task(taskpoolFunc, AppStorage.get('isLightMode') as boolean);
     let res1: string = await taskpool.execute(task1) as string;
     // 调整AppStorage里面的值
     AppStorage.setOrCreate('backupId', '8111122555');
     let eventData: emitter.EventData = {
       data: {
         "isLightMode": AppStorage.get('isLightMode'),
         "backupId": AppStorage.get('backupId'),
       }
     };
     // 通过emitter将UI主线程的AppStorage作为消息发送给taskpool子线程
     emitter.emit("eventIdTmp", eventData);
     console.info("taskpool: task res1 is: " + res1);
   }

   @Entry
   @Component
   struct WayTwo {
     aboutToAppear(): void {
       AppStorage.setOrCreate('isLightMode', true);
       AppStorage.setOrCreate('backupId', '8976756778');
     }

     build() {
       Row() {
         Column() {
           Button('taskpoolEmitterTest')
             .onClick(async () => {
               mainFunc();
             });
         }
         .width('100%')
         .height('100%');
       };
     }
   }
   ```

方案三：借助持久化方案sendablePreferences共享用户首选项：

1. 将子线程需要使用的值，直接存储到sendablePreferences中；
2. 使用taskpool将sendablePreferences发送给子线程；
3. 在子线程中直接对sendablePreferences进行读取、访问数据。

   ```ts
   import { sendablePreferences } from '@kit.ArkData';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { lang, taskpool } from '@kit.ArkTS';

   let preferences: sendablePreferences.Preferences;

   @Concurrent
   async function taskpoolFunc(preferences: sendablePreferences.Preferences): Promise<void> {
     // taskpool子线程从共享用户首选项获取backupId配置值，默认取不到返回空
     let backupIdTmp: string = '';
     let backupIdPromise = preferences.get('backupId', '');
     backupIdPromise.then((data: lang.ISendable) => {
       backupIdTmp = data as string;
       console.info('taskpoolFunc backupIdTmp:' + backupIdTmp);
     }).catch((err: BusinessError) => {
       console.error(`Failed to get value of 'backupId'. code: ${err.code}, message: ${err.message}`);
     });
   }

   async function mainFunc(): Promise<void> {
     // UI主线程中从共享用户首选项获取isLightMode配置值，默认取不到返回false
     let isLightModeTmp = false;
     let isLightModePromise = preferences.get('isLightMode', false);
     isLightModePromise.then((data: lang.ISendable) => {
       isLightModeTmp = data as boolean;
       console.info('mainFunc isLightModeTmp:' + isLightModeTmp);
     }).catch((err: BusinessError) => {
       console.error(`Failed to get value of 'isLightMode'. code: ${err.code}, message: ${err.message}`);
     });

     // UI主线程中从共享用户首选项获取backupId配置值，默认取不到返回空
     let backupIdTmp = '';
     let backupIdPromise = preferences.get('backupId', '');
     backupIdPromise.then((data: lang.ISendable) => {
       backupIdTmp = data as string;
       console.info('mainFunc backupIdTmp:' + backupIdTmp);
     }).catch((err: BusinessError) => {
       console.error(`Failed to get value of 'backupId'. code: ${err.code}, message: ${err.message}`);
     });

     // 将共享首选项的preferences（继承自ISendable）引用传递给taskpool子线程
     let task: taskpool.Task = new taskpool.Task(taskpoolFunc, preferences);
     await taskpool.execute(task);
   }

   @Entry
   @Component
   struct WayThree {
     aboutToAppear(): void {
       // 创建AppStorage
       AppStorage.setOrCreate('isLightMode', true);
       AppStorage.setOrCreate('backupId', '8976756778');
       // 添加sendablePreferences相关项
       let options: sendablePreferences.Options = { name: 'myStore' };
       let context = this.getUIContext().getHostContext()!;
       let promise = sendablePreferences.getPreferences(context, options);
       promise.then((object: sendablePreferences.Preferences) => {
         preferences = object;
         // 写入sendablePreferences首选项键值
         preferences.put('isLightMode', AppStorage.get('isLightMode') as boolean);
         preferences.put('backupId', AppStorage.get('backupId') as string);
         console.info("Succeeded in getting preferences.");
       }).catch((err: BusinessError) => {
         console.error(`Failed to get preferences. code: ${err.code}, message: ${err.message}`);
       });
     }

     build() {
       Row() {
         Column() {
           Button('taskpoolSendablePreferenceTest')
             .onClick(async () => {
               mainFunc();
             });
         }
         .width('100%')
         .height('100%');
       };
     }
   }
   ```

**Q：使用Emitter方案，Uint8Array类型的成员变量，或者对象数组传递时会丢失吗？**

**A**：发送事件时传递的数据，支持数据类型包括Array、ArrayBuffer、Boolean、DataView、Date、Error、Map、Number、Object、Primitive（除了symbol）、RegExp、Set、String、TypedArray，数据大小要求最大为16M。Uint8Array类型和对象数组支持传递。

需注意发送接收是同一个事件id，同时确认支持传输的数据大小是否符合要求。

**Q：taskpool.execute没有并行执行，系统卡住没反应？**

**A**：属于taskpool基础语法问题，需要检查下待执行的并行方法有没有使用@Concurrent装饰器装饰。

**Q：使用Emitter方案，如何立即触发emitter.once？**

**A**：将[emitter.emit](../harmonyos-references/js-apis-emitter.md#emitteremit12-1)接口的Options参数，设置为IMMEDIATE，表示事件被立即投递。

**Q：父子组件间数据双向同步时，可以将需要共享的数据作为子组件的入参传入，子组件通过[@Link](../harmonyos-guides/arkts-link.md)/[@ObjectLink](../harmonyos-guides/arkts-observed-and-objectlink.md)/[@Param](../harmonyos-guides/arkts-new-param.md)等装饰器接收，从而实现数据的传递与共享。如果需要进行页面间的数据共享和UI的同步更新，该如何实现呢？**

**A**：方案一：创建可观测的全局单例对象，将数据初始化保存在单例中，在需要使用数据的地方引入，实现一处修改，所有使用数据的地方同步刷新UI。以简易通讯录为例：

1. 创建单例：

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
2. 创建主页面：

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
3. 创建详情页面，获取单例对象并实现数据修改：

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
4. 在项目的“entry/src/main/resources/base/profile/main\_pages.json”中配置路由：

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

方案二：状态管理V1可以使用LocalStorage和AppStorage实现页面间的数据共享，案例可以参考官网示例：[将LocalStorage实例从UIAbility共享到一个或多个页面](../harmonyos-guides/arkts-localstorage.md#将localstorage实例从uiability共享到一个或多个页面)。状态管理V2可以配合[@ObservedV2和@Trace](../harmonyos-guides/arkts-new-observedv2-and-trace.md)实现深层嵌套数据的同步和UI刷新。以简易通讯录为例：

1. 使用@ObservedV2和@Trace实现深度观测：

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
2. 创建主页面，通过AppStorageV2.connect储存通讯录数据并实现双向绑定：

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
3. 创建详情页面，同样通过AppStorageV2.connect实现双向绑定，实现数据修改时同步到主页面：

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
4. 在项目的“entry/src/main/resources/base/profile/main\_pages.json”中配置路由：

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/WHCUnJSAQ6WObWlVFU4DFQ/zh-cn_image_0000002795290405.gif "点击放大")

**Q：除了状态管理是否还有其它实现页面间数据共享的方式？**

**A**：可以使用[Emitter](../harmonyos-references/js-apis-emitter.md)的能力。在所有需要数据共享的页面使用emitter.on订阅同步数据，在其他界面中通过emitter.emit发布数据变动的事件，实现各界面更新数据。但是该方式操作不当容易造成内存泄漏。

**Q：AppStorageV2是否适配ArkUI-X？**

**A**：AppStorageV2暂未适配ArkUI-X。

**Q：在组件的继承关系中，子组件时常会继承父组件的属性和方法并调用，是否有方案能实现父组件调用子组件中的方法？****A**：方案一：父子组件间的数据同步与共享。

1. 定义一个空函数的Controller类，在父组件创建该类的Controller实例并传递给子组件。
2. 在子组件中定义实际方法，并赋值给该Controller实例，将其内部方法重载。
3. 父组件再次调用该实例内的方法时，可以实现调用子组件重载后的新方法。

父子组件间的数据同步与共享可参考官网常见问题：[如何实现组件数据双向同步](../architecture-guides/architecture-v1-3_2-ts_12-0000002337739080.md)，以@Link为例（状态管理V2版本使用[@Param](../harmonyos-guides/arkts-new-param.md)代替@Link），示例代码如下：

```ts
@Entry
@Component
struct ParentComponent {
  @State childController: ChildController = new ChildController(this.getUIContext());

  build() {
    Column() {
      ChildComponent({ controller: this.childController }); // 父组件引用传递单例给子组件
      Button('调用子组件方法')
        .onClick(() => {
          this.childController.changeText();
        });
    }
    .height('100%')
    .width('100%');
  }
}

class ChildController {
  uiContext?: UIContext;
  changeText = () => {
  };

  constructor(uiContext: UIContext) {
    this.uiContext = uiContext;
  }
}

@Component
struct ChildComponent {
  @Link controller: ChildController;
  uiContext: UIContext = this.getUIContext();
  message: string = '';

  aboutToAppear() {
    if (this.controller) {
      this.controller.changeText = this.onShowToast;
    }
  }

  onShowToast() {
    this.message = '子组件被调用';
    console.info(this.message);
    if (this.message) {
      this.uiContext.getPromptAction().showToast({ message: this.message });
    } else {
      this.uiContext.getPromptAction().showToast({ message: 'this.hi is Null' });
    }
  }

  build() {
    Column() {
      Text('Hello World')
        .id('PageHelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold);
    };
  }
}
```

实现效果如下：点击父组件中的Button时，触发了子组件的弹窗效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/WSvt4tmaSti-7BiKJL7VWw/zh-cn_image_0000002795289405.png "点击放大")

方案二：父组件通知子组件调用子组件函数。

参考[@Watch和自定义组件更新](../harmonyos-guides/arkts-watch.md#watch和自定义组件更新)，子组件通过观察父组件传递的状态变量的变化，来判断是否调用自身的函数。状态管理V2版本可以通过[@Monitor](../harmonyos-guides/arkts-new-monitor.md)代替@Watch。

方案三：使用通过Emitter或EventHub在子组件中设置事件监视器，在父组件中触发事件以此来实现父组件调用子组件中的方法。

* 使用Emitter:

  ```ts
  import { emitter } from '@kit.BasicServicesKit';

  @Component
  struct EmitterChildComponent {
    // 组件加载时设置事件监听器
    aboutToAppear(): void {
      // 监听指定ID为1的事件
      emitter.on({ eventId: 1 }, (event) => {
        // 如果事件携带数据，则调用子组件方法处理数据
        if (event.data && event.data.data) {
          this.handleChildMethod(event.data.data as number);
        }
      });
    }

    // 组件销毁时，关闭事件监听
    aboutToDisappear(): void {
      emitter.off(1);
    }

    // 子组件处理方法
    handleChildMethod(value: number) {
      // 输出日志，表明子组件方法已由父组件传递的值触发
      console.info('我是子组件方法', `父组件传递的值为：${value}`);
    }

    build() {
    }
  }

  @Entry
  @Component
  struct EmitterParentComponent {
    build() {
      Column() {
        Button('调用子组件方法').onClick(() => {
          // 触发ID为1的事件，设置优先级为IMMEDIATE
          emitter.emit(
            { eventId: 1, priority: emitter.EventPriority.IMMEDIATE },
            { data: { 'data': 33 } }
          );
        });
        EmitterChildComponent();
      }
      .width('100%');
    }
  }
  ```
* 使用EventHub:

  ```ts
  @Component
  struct EventHubChildComponent {
    // 组件加载时设置事件监听器
    aboutToAppear(): void {
      this.getUIContext().getHostContext()!.eventHub.on('1', (data: number) => {
        this.handleChildMethod(data as number);
      });
    }

    // 组件销毁时，关闭事件监听
    aboutToDisappear(): void {
      this.getUIContext().getHostContext()!.eventHub.off('1');
    }

    // 子组件处理方法
    handleChildMethod(value: number) {
      // 输出日志，表明子组件方法已由父组件传递的值触发
      console.info('我是子组件方法', `父组件传递的值为：${value}`);
    }

    build() {
    }
  }

  @Entry
  @Component
  struct EventHubParentComponent {
    build() {
      Column() {
        Button('调用子组件方法').onClick(() => {
          this.getUIContext().getHostContext()!.eventHub.emit('1', 33);
        });
        EventHubChildComponent();
      }
      .width('100%');
    }
  }
  ```

**Q：在子组件中如何调用父组件的方法？**

**A**：参考方案一中常见问题“如何实现组件数据双向同步”的官网链接。

**Q：有个子组件选择颜色的弹窗，在子组件选择颜色后，点击弹窗的确认按钮后，如何把已选的颜色传递到父组件进行展示？**

**A**：父组件Index默认颜色白色，点击“打开弹窗”，点击“选择颜色-红色”，通过selectColorFunc方法把SelectColorComponent组件选择的颜色传递到父组件Index中并展示，代码示例如下：

```ts
@Entry
@Component
struct SelectColorPage {
  @State selectColor: string = '白色';

  build() {
    Column() {
      Text(this.selectColor)
        .fontSize(30)
      SelectColorComponent({
        // 父组件接收结果
        selectColorFunc: (res: string) => {
          // 获取子组件结果
          this.selectColor = res;
        }
      })
    }
    .backgroundColor(this.selectColor == '红色' ? Color.Red : Color.White)
    .justifyContent(FlexAlign.SpaceAround)
    .height('100%')
    .width('100%')
  }
}

@Component
export struct SelectColorComponent {
  dialogID: number = -1;
  selectColorRed: string = '';
  // 子组件里声明方法
  selectColorFunc = (res: string) => {
    console.info(`selectColor:${res}`);
  };

  build() {
    Column() {
      Button('打开弹窗').onClick(() => {
        // 打开弹窗
        this.selectColor();
      })
    }
  }

  @Builder
  ColorPicker() {
    Column() {
      Button('选择颜色-红色').onClick(() => {
        this.selectColorRed = '红色';
      })
      Row() {
        Button('确定')
          .onClick(() => {
            // 获取结果传递给父组件
            this.selectColorFunc(this.selectColorRed);
            // 关闭弹窗。
            this.getUIContext().getPromptAction().closeCustomDialog(this.dialogID);
          })
        Button('取消')
          .onClick(() => {
            // 关闭弹窗。
            this.getUIContext().getPromptAction().closeCustomDialog(this.dialogID);
          })
      }
      .padding(8)
    }
  }

  // 定义弹窗打开的方法。
  selectColor() {
    this.getUIContext().getPromptAction().openCustomDialog({
      builder: () => {
        this.ColorPicker();
      }
    }).then((dialogID) => {
      this.dialogID = Number(dialogID);
    });
  };
}
```

**Q：进入页面时，自定义组件中设置的onPageShow回调没有生效。问题代码如下：**

SplashPage页面：

```ts
@Component
export struct SplashPage {
  onPageShow() {
    console.info(`onPageShow`);
  }

  build() {
    Text('SplashPage')
      .fontSize(50)
      .textAlign(TextAlign.Center)
      .width('100%')
      .height('100%');
  }
}
```

Index页面：

```ts
import { SplashPage } from './SplashPage'

@Entry
@Component
struct Index {
  build() {
    Column() {
      SplashPage()
    }
  }
}
```

A：由背景知识可知，onPageShow回调需要在router路由页面（即@Entry装饰的自定义组件）每次显示时的场景下才会触发，而在问题代码中，并未涉及路由跳转等场景，而且直接调用子组件进行显示，因此onPageShow回调不生效。建议使用aboutToAppear回调，修正代码如下：

SplashPage页面：

```ts
@Component
export struct SplashPage {

  aboutToAppear(): void {
    console.info(`aboutToAppear`);
  }

  build() {
    Text('SplashPage')
      .fontSize(50)
      .textAlign(TextAlign.Center)
      .width('100%')
      .height('100%');
  }
}
```

Index页面：

```ts
import { SplashPage } from './SplashPage';

@Entry
@Component
struct Index {
  build() {
    Column() {
      SplashPage();
    };
  }
}
```

**Q：如果从后面一个界面使用router.back(1, { info: '来自Home页'})携带参数返回，那么不在子组件中使用onPageShow时应该如何获取参数？**

**A**：可以在父组件的onPageShow获取参数，然后使用[@Provide和@Consume](../harmonyos-guides/arkts-provide-and-consume.md)传递给子组件。

**Q：在启动页中，onPageShow回调会执行两次是什么原因？**

**A**：启动页中onPageShow执行两次有以下几种情况导致：

1. Navigation组件生命周期冲突：若应用启动时存在多个共享NavPathStack的Navigation组件（例如闪屏页和首页），可能导致生命周期回调重复触发。
2. Web组件重复加载：若启动页中包含Web组件，并在[onPageBegin](../harmonyos-references/arkts-basic-components-web-events.md#onpagebegin)回调中调用了[setCustomUserAgent](../harmonyos-references/ohos-atomicservice-atomicserviceweb.md#setcustomuseragent)等触发页面重载的操作，会导致Web生命周期重复执行。此时需将设置逻辑提前到[onControllerAttached](../harmonyos-references/arkts-basic-components-web-events.md#oncontrollerattached10)中，并确保在[loadUrl](../harmonyos-references/ohos-atomicservice-atomicserviceweb.md#loadurl)前完成配置。
3. 页面装饰器与路由机制冲突：@Entry装饰器误用：只有被@Entry装饰的组件才能触发onPageShow，但若页面通过NavDestination定义且已包含路由机制，则需使用[onShown](../harmonyos-references/ts-basic-components-navdestination.md#onshown10)替代onPageShow。此时若错误添加@Entry可能导致生命周期混乱。

**Q：页面A使用router路由跳转页面并传参给页面B，为什么页面B在onPageShow方法中无法接收到参数导致组件数据渲染失败？**

**A**：onPageShow回调是在自定义组件的build()函数执行之后触发的。相比之下，aboutToAppear函数则是在创建自定义组件的新实例后，在执行其build()函数之前执行。如果需要在组件显示前进行一些设置或初始化操作，应该在aboutToAppear中实现。

**Q：如何实现打开新页面不关闭模态转场页面，从新页面返回时保持原样？**

**A**：使用if条件渲染+控制器拦截返回，其次通过@State控制模态显示隐藏，然后子组件通过Controller向父页面注册返回拦截，最后父页面onBackPress调用子组件拦截方法实现效果。

步骤如下：

1. 定义子组件控制器（关键通信桥梁）。

   ```ts
   // 1. 定义子组件控制器（核心通信桥梁）
   class ChildController {
     // 子组件注册的返回拦截回调
     onBackPress: () => boolean = () => false;
   }
   ```
2. 子组件声明模态显示隐藏状态&绑定控制器。

   ```ts
   // 2. 子组件（包含模态层）
   @Component
   struct ModalTransitionWithIf {
     // 控制模态层显隐
     @State isShowShare: boolean = false;
     // 接收父页面传入的控制器
     private controller: ChildController = new ChildController();

     aboutToAppear(): void {
       // 向控制器注册子组件的返回拦截逻辑
       this.controller.onBackPress = (): boolean => {
         return this.handleChildBackPress();
       };
     }

     // 子组件返回事件处理（核心拦截逻辑）
     private handleChildBackPress(): boolean {
       if (this.isShowShare) {
         console.info('拦截返回：关闭模态层');
         this.isShowShare = false;
         return true; // 拦截系统返回
       }
       return false; // 不拦截
     }

     // 跳转到新页面（不关闭模态层）
     private jumpToNewPage() {
       this.getUIContext().getRouter().pushUrl({ url: 'pages/SecondPage' });
     }

     build() {
       Stack() {
         Column() {
           Button('打开模态层')
             .onClick(() => this.isShowShare = true)
             .margin(20);
         }
         .width('100%')
         .height('100%')
         .justifyContent(FlexAlign.Start);

         // 条件渲染的模态层（关键实现）
         if (this.isShowShare) {
           Column() {
             Column() {
               Text('模态层内容').fontSize(20).margin(20);
               Button('跳转新页面')
                 .onClick(() => this.jumpToNewPage());
             }
             .width('100%')
             .height('50%')
             .borderRadius(20)
             .backgroundColor('#FFF')
             .shadow(ShadowStyle.OUTER_DEFAULT_XS)
             .position({ x: 0, y: '60%' });
           }
           .width('100%')
           .height('100%')
           .backgroundColor(this.isShowShare ? '#99000000' : '')
           .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP]);
         }
       }
       .width('100%')
       .height('100%');
     }
   }
   ```
3. 父页面（@Entry）集成子组件&全局返回拦截。

   ```ts
   // 3. 父页面（入口组件）
   @Entry
   @Component
   struct MainPage {
     // 创建控制器实例（父子通信枢纽）
     private childController: ChildController = new ChildController();

     // 全局返回拦截（核心）
     onBackPress(): boolean {
       console.info('父页面收到返回事件');
       return this.childController.onBackPress();
     }

     build() {
       Column() {
         // 传递控制器给子组件
         ModalTransitionWithIf({ controller: this.childController });
       }
       .width('100%')
       .height('100%');
     }
   }
   ```

完整示例代码如下：

主页面代码（@Entry入口页面）：

```ts
// 1. 定义子组件控制器（核心通信桥梁）
class ChildController {
  // 子组件注册的返回拦截回调
  onBackPress: () => boolean = () => false;
}

// 2. 子组件（包含模态层）
@Component
struct ModalTransitionWithIf {
  // 控制模态层显隐
  @State isShowShare: boolean = false;
  // 接收父页面传入的控制器
  private controller: ChildController = new ChildController();

  aboutToAppear(): void {
    // 向控制器注册子组件的返回拦截逻辑
    this.controller.onBackPress = (): boolean => {
      return this.handleChildBackPress();
    };
  }

  // 子组件返回事件处理（核心拦截逻辑）
  private handleChildBackPress(): boolean {
    if (this.isShowShare) {
      console.info('拦截返回：关闭模态层');
      this.isShowShare = false;
      return true; // 拦截系统返回
    }
    return false; // 不拦截
  }

  // 跳转到新页面（不关闭模态层）
  private jumpToNewPage() {
    this.getUIContext().getRouter().pushUrl({ url: 'pages/SecondPage' });
  }

  build() {
    Stack() {
      Column() {
        Button('打开模态层')
          .onClick(() => this.isShowShare = true)
          .margin(20);
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Start);

      // 条件渲染的模态层（关键实现）
      if (this.isShowShare) {
        Column() {
          Column() {
            Text('模态层内容').fontSize(20).margin(20);
            Button('跳转新页面')
              .onClick(() => this.jumpToNewPage());
          }
          .width('100%')
          .height('50%')
          .borderRadius(20)
          .backgroundColor('#FFF')
          .shadow(ShadowStyle.OUTER_DEFAULT_XS)
          .position({ x: 0, y: '60%' });
        }
        .width('100%')
        .height('100%')
        .backgroundColor(this.isShowShare ? '#99000000' : '')
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP]);
      }
    }
    .width('100%')
    .height('100%');
  }
}

// 3. 父页面（入口组件）
@Entry
@Component
struct MainPage {
  // 创建控制器实例（父子通信枢纽）
  private childController: ChildController = new ChildController();

  // 全局返回拦截（核心）
  onBackPress(): boolean {
    console.info('父页面收到返回事件');
    return this.childController.onBackPress();
  }

  build() {
    Column() {
      // 传递控制器给子组件
      ModalTransitionWithIf({ controller: this.childController });
    }
    .width('100%')
    .height('100%');
  }
}
```

模态跳转新页面代码（SecondPage页面）：

```ts
//SecondPage页面
@Entry
@Component
struct SecondPage {
  build() {
    Column() {
      Text('新页面内容').fontSize(25).margin(30);
      Button('返回模态层')
        .onClick(() => this.getUIContext().getRouter().back());
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/hxuEaiozRCWMuJx1LeABXA/zh-cn_image_0000002766052340.png "点击放大")
