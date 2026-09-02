---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-155
title: 应用被拉起时如何获取外部传入参数
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 应用被拉起时如何获取外部传入参数
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:88c558ae14607b7fe09ce8e00010d8ad5cbe0dc185f5c35e888138c9a4bf474b
---

## 问题现象

外部启动应用，如何在应用中接收到外部传入的参数？如何把参数传到启动页面？例如首页根据参数显示不同的样式。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/JD-OsmgCQAGHCDA3Enf8gg/zh-cn_image_0000002658868627.png "点击放大")

## 背景知识

* [startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)：启动一个UIAbility。
* [Want](../harmonyos-guides/want-overview.md#want的定义与用途)是一种对象，用于在应用组件之间传递信息。
* [onNewWant()](../harmonyos-guides/uiability-lifecycle.md#onnewwant)：当应用的UIAbility实例已创建，再次调用方法启动该UIAbility实例时，系统触发该UIAbility的onNewWant()回调。
* [onCreate()](../harmonyos-guides/uiability-lifecycle.md#oncreate)：在首次创建UIAbility实例时，系统触发onCreate()回调。
* [getSharedLocalStorage()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getsharedlocalstorage12)：获取当前stage共享的LocalStorage实例。
* 为了能够支持被其他应用访问，目标应用需要在module.json5配置文件中配置skills标签。本示例使用[Deep Linking实现应用间跳转](../harmonyos-guides/deep-linking-startup.md)。

## 解决方案

实现思路：

1. 在拉起方应用TestA中设置参数Want，调用startAbility()触发应用跳转。

   src/main/ets/pages/Index.ets：

   ```ts
   import { common, Want } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct Index {
     message: string = 'Hello TestA';

     build() {
       Column() {
         Text(this.message)
           .id('HelloWorld')
           .fontSize($r('app.float.page_text_font_size'))
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           });

         // 跳转到TestB应用并携带msg参数
         Button('to TestB')
           .onClick(() => {
             let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
             let want: Want = {
               uri: 'link://www.testb.com',
               parameters: {
                 msg: 'Hello TestB, I am TestA.'
               }
             };
             try {
               context.startAbility(want).then(() => {
                 console.info('start ability success.');
               }).catch((err: BusinessError) => {
                 console.error(`start ability failed. Code is ${err.code}, message is ${err.message}`);
               });
             } catch (paramError) {
               console.error(`Failed to start ability. Code is ${paramError.code}, message is ${paramError.message}`);
             }
           });
       }
       .justifyContent(FlexAlign.Center)
       .height('100%')
       .width('100%');
     }
   }
   ```
2. 在目标应用TestB的module.json5配置文件中的skills标签下新增以下skill对象，用于被其他应用访问。

   src/main/module.json5：

   ```json
   {
     "actions": [
       // actions不能为空，actions为空会造成目标方匹配失败。
       "ohos.want.action.viewData"
     ],
     "uris": [
       {
         // scheme必选，可以自定义，以link为例，需要替换为实际的scheme
         "scheme": "link",
         // host必选，配置待匹配的域名
         "host": "www.testb.com"
       }
     ]
   }
   ```
3. 目标应用TestB是冷启动则在onCreate()中接收外部传入的参数Want，是热启动则在onNewWant()中接收外部传入的参数Want。
4. 目标应用TestB将接收到的Want参数存入LocalStorage实例中。

   src/main/ets/entryability/EntryAbility.ets：

   ```ts
   import { ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';

   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {
     onCreate(want: Want): void {
       try {
         this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
       } catch (err) {
         hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
       }
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
       // 应用冷启动，调用getAndSetParameter方法获取外部参数并存入
       this.getAndSetParameter(want);
     }

     onDestroy(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       // Main window is created, set main page for this ability
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

       windowStage.loadContent('pages/Index', this.storage, (err) => {
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

     onNewWant(want: Want) {
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onNewWant');
       // 应用热启动，调用getAndSetParameter方法获取外部参数并存入
       this.getAndSetParameter(want);
     }

     // 获取LocalStorage实例
     storage: LocalStorage = new LocalStorage();

     // 获取外部参数并存入LocalStorage实例中
     getAndSetParameter(want: Want): void {
       let parameters = want.parameters;
       if (parameters === null || parameters === undefined) {
         console.error('获取外部参数失败');
         return;
       }
       let msg = want.parameters?.msg;
       this.storage.setOrCreate('msg', msg);
     }
   };
   ```
5. 目标应用TestB在页面中通过getSharedLocalStorage()获取LocalStorage实例。
6. 目标应用TestB获取LocalStorage实例中的Want参数并使用。

   src/main/ets/pages/Index.ets：

   ```ts
   @Entry
   @Component
   struct Index {
     localStorage = this.getUIContext().getSharedLocalStorage();

     message: string = 'Hello TestB';
     @State msg: string = 'I am TestB';

     onPageShow(): void {
       let val: string = this.localStorage?.get('msg') as string;
       if (val === null || val === undefined) {
         return;
       }
       this.msg = val;
     }

     build() {
       Column() {
         Text(this.message)
           .fontSize($r('app.float.page_text_font_size'))
           .fontWeight(FontWeight.Bold);
         Text(this.msg)
           .fontSize(25)
           .fontWeight(FontWeight.Bold);
       }
       .justifyContent(FlexAlign.Center)
       .height('100%')
       .width('100%');
     }
   }
   ```
