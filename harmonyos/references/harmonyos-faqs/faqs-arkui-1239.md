---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1239
title: 实现热启动跳转至指定Navigation组件页面
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现热启动跳转至指定Navigation组件页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7d1d309fac229d29d22a429a1e683651eb51d166f6b28a6fba6644bf41e84d5c
---

## 问题现象

通过卡片热启动应用，如何跳转至指定的Navigation路由栈中的页面。

## 背景知识

* [组件导航（Navigation）](../harmonyos-guides/arkts-navigation-navigation.md)：主要用于实现页面间以及组件内部的页面跳转，支持在不同组件间传递跳转参数，提供灵活的跳转栈操作。
* [@ohos.events.emitter模块](../harmonyos-references/js-apis-emitter.md)：提供事件发送和处理的能力，包括持续订阅、单次订阅、取消订阅和发送事件到事件队列。
* [onNewWant](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)：当已经启动的UIAbility实例再次被拉起时，系统会触发该回调。可在onNewWant内获取到对应want参数信息，得知将要跳转的页面。
* [getAllPathName](../harmonyos-references/ts-basic-components-navigation.md#getallpathname10)：获取栈中所有NavDestination页面的名称。可用来判断将要跳转的页面，是否已在栈内，从而进行入栈出栈操作。

## 解决方案

* **方案一**：作为Navigation的根页面，首页不会被销毁，且页面上含有NavPathStack变量，可以进行页面跳转操作。通过在页面生命周期函数中发布事件通知首页，进行页面跳转操作。热启动的示例代码如下：
  1. 热启动：在被拉起方UIAbility的[onNewWant](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)方法中（若UIAbility文件无此方法，则自行增加即可），通过[EventHub.emit](../harmonyos-references/js-apis-inner-application-eventhub.md#eventhubemit)触发事件

     ```ts
     this.context.eventHub.emit('navigation', want.parameters?.path?.toString());
     ```
  2. 在Navigation的根页面通过[EventHub.on](../harmonyos-references/js-apis-inner-application-eventhub.md#eventhubon)订阅事件，跳转指定页面。

     ```ts
     aboutToAppear(): void {
       this.getUIContext().getHostContext()?.eventHub.on('navigation', (path: string) => {
         let paths = this.navPathStack.getAllPathName();
         if (paths.slice().pop() === path) {
           return;
         }
         this.navPathStack.pushPath({ name: path }, false);
       });
     }
     ```

* **方案二**：封装NavPathStack，在onNewWant生命周期中通过getAllPathName获取栈中所有NavDestination页面的名称，判断当前页面是否为目标页面，再决定是否用NavPathStack将目标页面push至栈顶。
  1. 封装全局的NavPathStack变量。RouterModule.ets文件。

     ```ts
     export class RouterModule {
       private static pathStack: NavPathStack = new NavPathStack();

       static setRouterStack(pathStack: NavPathStack) {
         RouterModule.pathStack = pathStack;
       }

       static getRouterStatic() {
         return RouterModule.pathStack;
       }
     }
     ```
  2. 在被拉起方UIAbility的[onNewWant](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)方法中（若UIAbility文件无此方法，则自行增加即可），执行判断和跳转操作。

     ```ts
     const pathStack = RouterModule.getRouterStatic();
     let param = want.parameters as Record<string, Object>;
     let backPage = param.message as string;
     if (pathStack.getAllPathName().slice().pop() === backPage) {
       return;
     }
     const pathInfo = new NavPathInfo(backPage, null);
     pathStack.pushPath(pathInfo);
     ```

完整示例如下：

新增工程项目后，此时存在一个entry类型的HAP包（作为拉起方），再新增一个feature类型的HAP（被拉起方）。参考不同类型[HAP](../harmonyos-guides/hap-package.md)的说明。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/7ndlKcceTkC8OSr-vNdqcg/zh-cn_image_0000002628755346.png)

1. 拉起方（entry模块）的示例代码如下，请根据实际的HAP信息更新want参数：

   ```ts
   import { common } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   const BUNDLE_NAME: string = 'com.example.NewWantDemo'; // 在应用app.json5文件中'bundleName'节点获得
   const ABILITY_NAME: string = 'TargetAbility'; // 在HAP包的对应Ability文件中获得

   @Entry
   @Component
   struct HAPRouterDemo {
     private context?: common.UIAbilityContext; // 创建context实例

     aboutToAppear(): void {
       this.context = this.getUIContext().getHostContext() as common.UIAbilityContext; // 获取当前页面关联的UIAbilityContext
     }

     jumpHap() {
       if (this.context) {
         // 启动Ability，拉起HAP模块的UIAbility实例
         this.context.startAbility({
           bundleName: BUNDLE_NAME,
           abilityName: ABILITY_NAME,
           parameters: {
             'path': 'NavDesPage'
           }
         }).then(() => {
           console.info('start audio ability success');
         }).catch((error: BusinessError) => {
           console.error(`start audio ability failed, error: ${error}`);
         });
       }
     }

     build() {
       Column() {
         Button('startAbility跳转HAP')
           .onClick(() => {
             this.jumpHap();
           });
       }
       .justifyContent(FlexAlign.Center)
       .height('100%')
       .width('100%');
     }
   }
   ```
2. 被拉起方（target模块）的示例代码如下：

   ```ts
   import { RouterModule } from './RouterModule';

   @Entry
   @Component
   struct Solution1 {
     navPathStack: NavPathStack = RouterModule.getRouterStatic();

     aboutToAppear(): void {
       this.getUIContext().getHostContext()?.eventHub.on('navigation', (path: string) => {
         let paths = this.navPathStack.getAllPathName();
         if (paths.slice().pop() === path) {
           return;
         }
         this.navPathStack.pushPath({ name: path }, false);
       });
     }

     @Builder
     pageMap(name: string) {
       if (name === 'NavDesPage') {
         NavDesPage();
       }
     }

     build() {
       Navigation(this.navPathStack) {
         Column() {
           Button('跳转NavDestination')
             .onClick(() => {
               this.navPathStack.pushPathByName('NavDesPage', null, false);
             });
         }.height('100%').width('100%').justifyContent(FlexAlign.Center);
       }.navDestination(this.pageMap)
       .height('100%').width('100%');
     }
   }

   @Component
   struct NavDesPage {
     navPathStack: NavPathStack = new NavPathStack();

     build() {
       NavDestination() {
         Text('NavDesPage')
           .fontSize($r('app.float.page_text_font_size'))
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           });
       }
       .onReady((ctx: NavDestinationContext) => {
         this.navPathStack = ctx.pathStack;
       })
       .height('100%')
       .width('100%');
     }
   }
   ```
3. 按照方案的描述修改被拉起方的UIAbility文件（示例中为TargetAbility.ets）的onNewWant方法（若UIAbility文件无此方法，则参照背景知识中介绍自行增加onNewWant即可）。
4. 分别编译target模块和entry模块，再运行entry模块即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/OZI4r7oaTAykKC3RFz4Czw/zh-cn_image_0000002658954667.png)

## 常见FAQ

Q：热启动，如何每次启动都重新打开目标页面？

A：可通过上述两种方案getAllPathName获取到栈中所有NavDestination页面的名称，判断目标页面是否在栈内，如在栈内则通过[removeByName](../harmonyos-references/ts-basic-components-navigation.md#removebyname11)将目标页面从页面栈内删除，再通过pushPath入栈，达到重新打开的效果。示例代码如下：结合上述方案二，在UIAbility文件的[onNewWant](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)方法中增加以下代码（若UIAbility文件无此方法，则自行增加即可）。

```ts
const pathStack = RouterModule.getRouterStatic();
let param = want.parameters as Record<string, Object>;
let targetPage = param.message as string;
const isPageBInStack = pathStack.getAllPathName().indexOf(targetPage) !== -1;
if (isPageBInStack) {
  pathStack.removeByName(targetPage);
  const pathInfo = new NavPathInfo(targetPage, null);
  pathStack.pushPath(pathInfo);
} else {
  const pathInfo = new NavPathInfo(targetPage, null);
  pathStack.pushPath(pathInfo);
}
```
