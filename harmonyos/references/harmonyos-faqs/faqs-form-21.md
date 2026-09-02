---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-21
title: 卡片跳转到应用页面
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 卡片跳转到应用页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:64c24808c7c0fd9d64584042b37ecd61683da3371ab1696524caf3caf7579cc7
---

## 问题现象

为了实现服务直达的便捷体验效果，如何通过桌面卡片跳转到应用页面？

## 背景知识

* [页面路由](../harmonyos-guides/arkts-routing.md)指在应用程序中实现不同页面之间的跳转和数据传递。Router模块通过不同的url地址，可以方便地进行页面路由，轻松地访问不同的页面。
* [组件导航](../harmonyos-guides/arkts-navigation-navigation.md)主要用于实现Navigation页面（NavDestination）间的跳转，支持在不同Navigation页面间传递参数，提供灵活的跳转栈操作，从而更便捷地实现对不同页面的访问和复用。
* 在动态卡片中使用[postCardAction接口的router能力](../harmonyos-guides/arkts-ui-widget-event-router.md)，能够快速拉起动态卡片提供方应用的指定UIAbility(页面)，因此UIAbility较多的应用往往会通过卡片提供不同的跳转按钮，实现一键直达的效果。

## 解决方案

主应用中的路由导航有多种方式，常见的场景包括：一、使用Router页面路由；二、使用Navigation组件导航；三、混合使用Router页面路由和Navigation组件导航。针对不同场景，卡片跳转到应用页面的处理方式不同。

| 场景 | 解决方案 |
| --- | --- |
| 使用Router页面路由 | 在EntryAbility的onCreate及onNewWant回调中直接跳转对应页面 |
| 使用Navigation组件导航 | 在EntryAbility的onCreate及onNewWant回调中保存跳转目标页面，在首页跳转 |
| 混合使用Router页面路由和Navigation组件导航 | 在EntryAbility的onCreate及onNewWant回调中保存跳转目标页面，在首页或者其他Router页面跳转 |

* **场景一：使用Router页面路由。**

  参考[示例](../harmonyos-guides/arkts-ui-widget-event-router.md)完成卡片跳转到应用页面。
* **场景二：使用Navigation组件导航。**

  本示例主要介绍静态卡片的事件开发。对于需要点击跳转到对应NavDestination页面的卡片服务，可将卡片传递的参数使用AppStorage存储，在加载Navigation页面的时候获取AppStorage存储的参数，通过在onPageShow生命周期中实现跳转。详细的开发步骤为：

  1. 创建静态服务卡片，并为FormLink设置对应的params参数。卡片页面为：

     ```ts
     @Entry
     @Component
     struct PushHavDeCardCard {
       build() {
         Column() {
           Text('跳转页面');
           Row() {
             Column() {
               FormLink({
                 action: 'router',
                 abilityName: 'EntryAbility',
                 params: { targetPage: 'pageA' }
               }) {
                 Button() {
                   Text('跳转页面A')
                     .fontColor('#45A6F4')
                     .fontSize(12);
                 }
                 .width(120)
                 .height(32)
                 .margin({ top: '20%' })
                 .backgroundColor('#FFFFFF')
                 .borderRadius(16);
               };

               FormLink({
                 action: 'router',
                 abilityName: 'EntryAbility',
                 params: { targetPage: 'pageB' }
               }) {
                 Button() {
                   Text('跳转页面B')
                     .fontColor('#45A6F4')
                     .fontSize(12);
                 }
                 .width(120)
                 .height(32)
                 .margin({ top: '8%', bottom: '15vp' })
                 .backgroundColor('#FFFFFF')
                 .borderRadius(16);
               };
             };
           }.width('100%').height('80%')
           .justifyContent(FlexAlign.Center);
         }
         .padding(16)
         .width('100%')
         .height('100%')
         .alignItems(HorizontalAlign.Start)
         .backgroundImageSize(ImageSize.Cover);
       }
     }
     ```
  2. 在onCreate和onNewWant回调函数中接收FormLink的参数，并使用AppStorage存储参数。

     EntryAbility.ets：

     ```ts
     import { UIAbility, Want } from '@kit.AbilityKit';
     import { hilog } from '@kit.PerformanceAnalysisKit';
     import { window } from '@kit.ArkUI';

     const DOMAIN = 0x0000;

     export default class EntryAbility extends UIAbility {
       onCreate(want: Want): void {
         // 获取router事件中传递的targetPage参数
         if (want?.parameters?.params) {
           // want.parameters.params对应FormLink()中targetPage内容
           let params: Record<string, Object> = JSON.parse(want.parameters.params as string);
           // 把参数存入AppStorage
           AppStorage.setOrCreate('param', params.targetPage as string);
         }
       }

       // 如果UIAbility已在后台运行，在收到router事件后会触发onNewWant生命周期回调
       onNewWant(want: Want): void {
         if (want?.parameters?.params) {
           // want.parameters.params对应FormLink()中params内容
           let params: Record<string, Object> = JSON.parse(want.parameters.params as string);
           AppStorage.setOrCreate('param', params.targetPage as string);
         }
       }

       onWindowStageCreate(windowStage: window.WindowStage): void {
         // Main window is created, set main page for this ability
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

         windowStage.loadContent('pages/Index', (err) => {
           if (err.code) {
             hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
             return;
           }
           hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
         });
       }
     };
     ```
  3. 创建NavDestination页面、router\_map.json配置文件，并在module.json5中引入routerMap。

     PageA.ets：

     ```ts
     @Builder
     export function PageABuilder() {
       PageA();
     }

     @Component
     struct PageA {
       pageInfos: NavPathStack = new NavPathStack();

       build() {
         NavDestination() {
           Column() {
             Text('this is PageA');
           }
         }.title('PageA')
         .onReady((context: NavDestinationContext) => {
           this.pageInfos = context.pathStack;
         })
       }
     }
     ```

     PageB.ets：

     ```ts
     @Builder
     export function PageBBuilder() {
       PageB();
     }

     @Component
     struct PageB {
       pageInfos: NavPathStack = new NavPathStack();

       build() {
         NavDestination() {
           Column() {
             Text('this is PageB');
           }
         }.title('PageB')
         .onReady((context: NavDestinationContext) => {
           this.pageInfos = context.pathStack;
         })
       }
     }
     ```

     router\_map.json：

     ```json
     {
       "routerMap": [
         {
           "name": "pageA",
           "pageSourceFile": "src/main/ets/pages/PageA.ets",
           "buildFunction": "PageABuilder"
         },
         {
           "name": "pageB",
           "pageSourceFile": "src/main/ets/pages/PageB.ets",
           "buildFunction": "PageBBuilder"
         }
       ]
     }
     ```
  4. 在Navigation页面通过StorageLink获取AppStorage设置的参数，在onPageShow生命周期中跳转到对应的NavDestination页面。

     ```ts
     @Entry
     @Component
     struct Index {
       pageInfos: NavPathStack = new NavPathStack();
       @StorageLink('param') pageParam: string = '';

       onPageShow(): void {
         console.info('this is pageshow Navigation pageParam :' + this.pageParam);
         if (this.pageParam != '') {
           // 如果需要跳转的页面在最上层，则不用再跳转了
           let stackIndexArray = this.pageInfos.getAllPathName();
           if (stackIndexArray.length > 0 && stackIndexArray[stackIndexArray.length - 1] === this.pageParam) {
             this.pageInfos.replacePathByName(this.pageParam, null);
           } else {
             this.pageInfos.pushPathByName(this.pageParam, null, false);
           }
           // 置空参数，防止进入onPageShow后有参数直接跳转到其他页面
           AppStorage.set('param', '');
           console.info('this is pageshow Navigation pageParam setnull:' + this.pageParam);
         }
       }

       build() {
         Navigation(this.pageInfos) {
           Text('这是Navigation页面');
         }
         .title('NavIndex');
       }
     }
     ```
* **场景三：混合使用Router页面路由和Navigation组件导航。**

  本示例主要介绍动态卡片的事件开发。首先，在动态卡片中使用postCardAction接口，接口携带不同的跳转参数。接着，在主应用EntryAbility的onCreate及onNewWant回调函数解析参数并保存，以获取卡片端期望跳转的页面。最后，在Navigation页面的onPageShow回调函数中读取跳转参数，选择停留在本页面还是跳转其他页面。详细的开发步骤为：

  1. 创建[动态卡片](../harmonyos-guides/arkts-ui-widget-creation.md)，在工程的entry模块中，新建名为WidgetCard，大小为4\*4的ArkTS卡片。
  2. 在主应用pages目录下，定义Index和MyHome作为Router页面，定义IndexPA和MyHomePA分别作为NavDestination页面。在module.json5中引入routerMap。

     main\_pages.json：

     ```json
     {
       "src": [
         "pages/Index",
         "pages/MyHome"
       ]
     }
     ```

     router\_map.json：

     ```json
     {
       "routerMap": [
         {
           "name": "IndexPA",
           "pageSourceFile": "src/main/ets/pages/IndexPA.ets",
           "buildFunction": "IndexPABuilder"
         },
         {
           "name": "MyHomePA",
           "pageSourceFile": "src/main/ets/pages/MyHomePA.ets",
           "buildFunction": "MyHomePABuilder"
         }
       ]
     }
     ```
  3. 在卡片页面中定义4个按钮，在按钮的点击事件中引用postCardAction接口，分别定义跳转router页面以及NavDestination页面。

     WidgetCard.ets：

     ```ts
     @Entry
     @Component
     struct WidgetCard {
       build() {
         Column({ space: 20 }) {
           Row({ space: 20 }) {
             Button('Index').onClick(() => {
               postCardAction(this, {
                 action: 'router',
                 abilityName: 'EntryAbility',
                 params: {
                   routerPage: 'pages/Index',
                   subPage: ''
                 }
               });
             });
             Button('IndexPA').onClick(() => {
               postCardAction(this, {
                 action: 'router',
                 abilityName: 'EntryAbility',
                 params: {
                   routerPage: 'pages/Index',
                   subPage: 'IndexPA'
                 }
               });
             });
           }
           .justifyContent(FlexAlign.SpaceBetween)
           .width('100%')
           .height(100);

           Row({ space: 20 }) {
             Button('Home').onClick(() => {
               postCardAction(this, {
                 action: 'router',
                 abilityName: 'EntryAbility',
                 params: {
                   routerPage: 'pages/MyHome',
                   subPage: ''
                 }
               });
             });
             Button('HomePA').onClick(() => {
               postCardAction(this, {
                 action: 'router',
                 abilityName: 'EntryAbility',
                 params: {
                   routerPage: 'pages/MyHome',
                   subPage: 'MyHomePA'
                 }
               });
             });
           }
           .justifyContent(FlexAlign.SpaceBetween)
           .width('100%')
           .height(100);
         }
         .padding(16)
         .width('100%')
         .height('100%');

       }
     }
     ```
  4. 在EntryAbility的onCreate和onNewWant方法中，解析通过卡片传递的参数，并在saveRouterPage方法中保存参数。

     entities/CardParam.ets：

     ```ts
     export interface CardParam {
       routerPage: string,
       subPage: string
     }
     ```

     common/Constant.ets：

     ```ts
     export class Constants {
       static readonly IndexRouterPage = 'pages/Index';
       static readonly MyHomeRouterPage = 'pages/MyHome';
       static readonly selectPageAppKey = 'selectPage';
       static readonly subPageAppKey = 'subPage';
     }
     ```

     EntryAbility.ets：

     ```ts
     import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
     import { hilog } from '@kit.PerformanceAnalysisKit';
     import { window } from '@kit.ArkUI';
     import { CardParam } from '../entities/CardParam';
     import { Constants } from '../common/Constant';

     const DOMAIN = 0x0000;

     export default class EntryAbility extends UIAbility {
       private selectPage: string = Constants.IndexRouterPage;

       onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
         try {
           this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
         } catch (err) {
           hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
         }

         if (want?.parameters?.params) {
           // want.parameters.params对应postCardAction()中params内容
           let cardParam: CardParam = JSON.parse(want.parameters.params as string);
           this.saveRouterPage(cardParam);
         }

         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
         hilog.info(DOMAIN, 'testTag', '%{public}s', launchParam.launchReason);

       }

       // 保存参数信息
       saveRouterPage(cardParam: CardParam) {
         // 将从卡片传递的参数使用AppStorage保存
         this.selectPage = cardParam.routerPage as string;
         if (this.selectPage && this.selectPage.length > 0) {
           AppStorage.setOrCreate(Constants.selectPageAppKey, this.selectPage);
         }
         let subPage = cardParam.subPage as string;
         if (subPage && subPage.length > 0) {
           AppStorage.setOrCreate(Constants.subPageAppKey, subPage);
         }
         hilog.info(DOMAIN, 'testTag', `onCreate selectPage: ${this.selectPage}`);
       }

       // 如果UIAbility已在后台运行，在收到router事件后会触发onNewWant生命周期回调
       onNewWant(want: Want): void {
         hilog.info(DOMAIN, 'testTag', `onNewWant Want: ${want.bundleName}`);
         if (want?.parameters?.params) {
           // want.parameters.params对应postCardAction()中params内容
           let cardParam: CardParam = JSON.parse(want.parameters.params as string);
           this.saveRouterPage(cardParam);
         }
       }

       onDestroy(): void {
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
       }

       onWindowStageCreate(windowStage: window.WindowStage): void {
         // Main window is created, set main page for this ability
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
         windowStage.loadContent(this.selectPage, (err) => {
           if (err.code) {
             hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
             return;
           }
           hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
         });
       }

       onWindowStageDestroy(): void {
         // Main window is destroyed, release UI related resources
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
       }

       onForeground(): void {
         // Ability has brought to foreground
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
       }

       onBackground(): void {
         // Ability has back to background
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
       }
     };
     ```
  5. 在Index和MyHome页面使用Navigation组件，在onPageShow方法中拦截卡片的参数，判断是否在当前页面停留。判断逻辑如下：若跳转目标页面不是当前Navigation页面，则通过Router的pushUrl跳转；若是当前页面，则判断是否需要跳转NavDestination页面。需要的话，再继续判断NavDestination页面是否在路由栈顶，如果是则使用replacePathByName方法，否则使用pushPathByName跳转。

     common/CommonFilter.ets：

     ```ts
     import { Constants } from './Constant';
     import { Router } from '@kit.ArkUI';

     export function commonFilter(pagePathStack: NavPathStack, curPage: string, myRouter: Router) {
       let selectPage = AppStorage.get(Constants.selectPageAppKey) as string;
       let subPage = AppStorage.get(Constants.subPageAppKey) as string;
       // selectPage有值
       if (selectPage && selectPage.length > 0) {
         if (selectPage == curPage) {
           // 跳转的根页面是本页面
           // 清空值，避免后续造成影响
           AppStorage.delete(Constants.selectPageAppKey);
           AppStorage.delete(Constants.subPageAppKey);

           // 有子页面，跳转子页面
           if (subPage && subPage.length > 0) {
             // 如果需要跳转的页面在最上层，则不用再跳转了
             let stackIndexArray = pagePathStack.getAllPathName();
             if (stackIndexArray.length > 0 && stackIndexArray[stackIndexArray.length - 1] === subPage) {
               pagePathStack.replacePathByName(subPage, null);
             } else {
               pagePathStack.pushPathByName(subPage, null, false);
             }
           } else {
             // 回到主页面
             pagePathStack.clear();
           }
         } else {
           // 需要跳转其他的router页面
           myRouter.pushUrl({
             url: selectPage
           });
         }
       }
     }
     ```

     pages/Index.ets：

     ```ts
     import { Constants } from '../common/Constant';
     import { commonFilter } from '../common/CommonFilter';

     @Entry
     @Component
     struct Index {
       pageInfos: NavPathStack = new NavPathStack();

       onPageShow(): void {
         console.info('Index  onPageShow');
         commonFilter(this.pageInfos, Constants.IndexRouterPage, this.getUIContext().getRouter());
       }

       build() {
         Navigation(this.pageInfos) {
           Column({ space: 10 }) {
             Text('这里是Index页面');
             Button('跳转Index - PA子页面').onClick(() => {
               this.pageInfos.pushPathByName('IndexPA', null);
             });

             Button('跳转MyHome页面').onClick(() => {
               this.getUIContext().getRouter().pushUrl({
                 url: 'pages/MyHome'
               });
             });
           }
           .height('100%')
           .width('100%');
         };
       }
     }
     ```

     pages/IndexPA.ets：

     ```ts
     @Builder
     export function IndexPABuilder() {
       IndexPA();
     }

     @Component
     struct IndexPA {
       pageInfos: NavPathStack = new NavPathStack();

       build() {
         NavDestination() {
           Column() {
             Text('this is IndexPA');
           };
         }.title('IndexPA')
         .onReady((context: NavDestinationContext) => {
           this.pageInfos = context.pathStack;
         });
       }
     }
     ```

     pages/MyHome.ets：

     ```ts
     import { Constants } from '../common/Constant';
     import { commonFilter } from '../common/CommonFilter';

     @Entry
     @Component
     struct MyHome {
       pageInfos: NavPathStack = new NavPathStack();

       onPageShow(): void {
         console.info('MyHome  onPageShow');
         commonFilter(this.pageInfos, Constants.MyHomeRouterPage, this.getUIContext().getRouter());
       }

       build() {
         Navigation(this.pageInfos) {
           Column({ space: 10 }) {
             Text('这里是MyHome页面');
             Button('跳转MyHome - A子页面').onClick(() => {
               this.pageInfos.pushPathByName('MyHomePA', null);
             });
           }
           .height('100%')
           .width('100%');
         };
       }
     }
     ```

     pages/MyHomePA.ets：

     ```ts
     @Builder
     export function MyHomePABuilder() {
       MyHomePA();
     }

     @Component
     struct MyHomePA {
       pageInfos: NavPathStack = new NavPathStack();

       build() {
         NavDestination() {
           Column() {
             Text('this is MyHomePA');
           };
         }.title('MyHomePA')
         .onReady((context: NavDestinationContext) => {
           this.pageInfos = context.pathStack;
         });
       }
     }
     ```

## 常见FAQ

Q：多次点击服务卡片拉起应用指定页面后，该页面在路由栈内存在多个，导致返回上一面需要多次返回操作。如何解决该问题？

A：应用在接收到对应的router跳转事件后，处理跳转的时候需要判断跳转的页面是否已经在路由栈的栈顶，如果在的话需要替换当前的页面，如果不在的话，重新push这个页面到栈。
