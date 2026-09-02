---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-intra-device-interaction
title: 启动应用内的UIAbility组件
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > 应用模型 > 应用组件 > UIAbility组件 > 启动应用内的UIAbility组件
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:308d5e04c9550f1cd2adb1fa3fc0ef09b48a7d818c6e09be8d4326d24d35e3e7
---

[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)是系统调度的最小单元。在设备内的功能模块之间跳转时，会涉及到启动特定的UIAbility，包括应用内的其他UIAbility、或者其他应用的UIAbility（例如启动三方支付UIAbility）。

本文主要介绍启动应用内的UIAbility组件的方式。应用间的组件跳转详见[应用间跳转](link-between-apps-overview.md)。

* [启动应用内的UIAbility](uiability-intra-device-interaction.md#启动应用内的uiability)
* [启动应用内的UIAbility并获取返回结果](uiability-intra-device-interaction.md#启动应用内的uiability并获取返回结果)
* [启动UIAbility的指定页面](uiability-intra-device-interaction.md#启动uiability的指定页面)

## 启动应用内的UIAbility

当一个应用内包含多个[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)时，存在应用内启动UIAbility的场景。例如在支付应用中从入口UIAbility启动收付款UIAbility。

假设应用中有两个UIAbility：EntryAbility和FuncAbility（可以在同一个Module中，也可以在不同的Module中），需要从EntryAbility的页面中启动FuncAbility。

1. 在EntryAbility中，通过调用[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)方法启动UIAbility，[want](../harmonyos-references/js-apis-app-ability-want.md)为UIAbility实例启动的入口参数，其中bundleName为待启动应用的Bundle名称，abilityName为待启动的Ability名称，moduleName在待启动的UIAbility属于不同的Module时添加，parameters为自定义信息参数。示例中的context的获取方式请参见[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

   ```typescript
   import { common, Want } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   const TAG: string = '[MainPage]';
   const DOMAIN_NUMBER: number = 0xFF00;

   @Entry
   @Component
   struct MainPage {
     private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

     build() {
       Column() {
         List({ initialIndex: 0, space: 8 }) {

           ListItem() {
             Row() {
               // ...
             }
             .onClick(() => {
               // context为Ability对象的成员，在非Ability对象内部调用需要
               // 将Context对象传递过去
               let wantInfo: Want = {
                 deviceId: '', // deviceId为空表示本设备
                 bundleName: 'com.samples.uiabilityinteraction',
                 moduleName: 'entry', // moduleName非必选
                 abilityName: 'FuncAbilityA',
                 parameters: {
                   // 自定义信息
                   // 请将$r('app.string.main_page_return_info')替换为实际资源文件，在本示例中该资源文件的value值为"来自EntryAbility MainPage页面"
                   info: $r('app.string.main_page_return_info')
                 },
               };
               // context为调用方UIAbility的UIAbilityContext
               this.context.startAbility(wantInfo).then(() => {
                 hilog.info(DOMAIN_NUMBER, TAG, 'startAbility success.');
               }).catch((error: BusinessError) => {
                 hilog.error(DOMAIN_NUMBER, TAG, 'startAbility failed.');
               });
             })
           }

           // ...
         }
         // ...
       }
       // ...
     }
   }
   ```
2. 在FuncAbility的[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)或者[onNewWant()](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)生命周期回调文件中接收EntryAbility传递过来的参数。

   ```typescript
   import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   // ···

   export default class FuncAbilityA extends UIAbility {
     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       // 接收调用方UIAbility传过来的参数
       let funcAbilityWant = want;
       let info = funcAbilityWant?.parameters?.info;
       // ···
     }

   // ···
   }
   ```

   **说明** 

   在被拉起的FuncAbility中，可以通过获取传递过来的[want](../harmonyos-references/js-apis-app-ability-want.md)参数的parameters来获取拉起方[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)的PID、Bundle Name等信息。
3. 在FuncAbility业务完成之后，如需要停止当前[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)实例，在FuncAbility中通过调用[terminateSelf()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateself)方法实现。

   ```typescript
   import { common } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const TAG: string = '[FuncAbilityAPage]';
   const DOMAIN_NUMBER: number = 0xFF00;

   @Entry
   @Component
   struct FuncAbilityAPage {

     build() {
       Column() {
         // 请将$r('app.string.Stop_AbilityA')替换为实际资源文件，在本示例中该资源文件的value值为"StopFuncAbilityA"
         Button($r('app.string.Stop_AbilityA'))
           .onClick(() => {
             let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
             // context为需要停止的UIAbility实例的AbilityContext
             context.terminateSelf((err) => {
               if (err.code) {
                 hilog.error(DOMAIN_NUMBER, TAG, `Failed to terminate self. Code is ${err.code}, message is ${err.message}`);
                 return;
               }
             });
           })
           // ...
       }
       // ...
     }
   }
   ```

   **说明** 

   调用terminateSelf()方法停止当前UIAbility实例时，默认会保留该实例的快照（Snapshot），即在最近任务列表中仍然能查看到该实例对应的任务。如不需要保留该实例的快照，可以在其对应UIAbility的[module.json5配置文件](module-configuration-file.md)中，将[abilities标签](module-configuration-file.md#abilities标签)的removeMissionAfterTerminate字段配置为true。
4. 如需要关闭应用所有的[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)实例，可以调用[ApplicationContext](../harmonyos-references/js-apis-inner-application-applicationcontext.md)的[killAllProcesses()](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextkillallprocesses)方法实现关闭应用所有的进程。

## 启动应用内的UIAbility并获取返回结果

在一个EntryAbility启动另外一个FuncAbility时，希望在被启动的FuncAbility完成相关业务后，能将结果返回给调用方。例如在应用中将入口功能和账号登录功能分别设计为两个独立的[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)，在账号登录UIAbility中完成登录操作后，需要将登录的结果返回给入口UIAbility。

1. 在EntryAbility中，调用[startAbilityForResult()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startabilityforresult-2)接口启动FuncAbility，异步回调中的data用于接收FuncAbility停止自身后返回给EntryAbility的信息。示例中的context的获取方式请参见[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

   ```typescript
   import { common, Want } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   const TAG: string = '[MainPage]';
   const DOMAIN_NUMBER: number = 0xFF00;

   @Entry
   @Component
   struct MainPage {
     private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

     build() {
       Column() {
         List({ initialIndex: 0, space: 8 }) {

           // ...

           ListItem() {
             Row() {
               // ...
             }
             .onClick(() => {
               let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
               const RESULT_CODE: number = 1001;
               let want: Want = {
                 deviceId: '', // deviceId为空表示本设备
                 bundleName: 'com.samples.uiabilityinteraction',
                 moduleName: 'entry', // moduleName非必选
                 abilityName: 'FuncAbilityA',
                 parameters: {
                   // 自定义信息
                   // 请将$r('app.string.main_page_return_info')替换为实际资源文件，在本示例中该资源文件的value值为"来自EntryAbility MainPage页面"
                   info: $r('app.string.main_page_return_info')
                 }
               };
               context.startAbilityForResult(want).then((data) => {
                 if (data?.resultCode === RESULT_CODE) {
                   // 解析被调用方UIAbility返回的信息
                   let info = data.want?.parameters?.info;
                   hilog.info(DOMAIN_NUMBER, TAG, JSON.stringify(info) ?? '');
                   if (info !== null) {
                     this.getUIContext().getPromptAction().showToast({
                       message: JSON.stringify(info)
                     });
                   }
                 }
                 hilog.info(DOMAIN_NUMBER, TAG, JSON.stringify(data.resultCode) ?? '');
               }).catch((err: BusinessError) => {
                 hilog.error(DOMAIN_NUMBER, TAG, `Failed to start ability for result. Code is ${err.code}, message is ${err.message}`);
               });
             })
           }

           // ...
         }
         // ...
       }
       // ...
     }
   }
   ```
2. 在FuncAbility停止自身时，需要调用[terminateSelfWithResult()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)方法，入参[abilityResult](../harmonyos-references/js-apis-inner-ability-abilityresult.md)为FuncAbility需要返回给EntryAbility的信息。

   ```typescript
   import { common } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const TAG: string = '[FuncAbilityAPage]';
   const DOMAIN_NUMBER: number = 0xFF00;

   @Entry
   @Component
   struct FuncAbilityAPage {

     build() {
       Column() {
         // ...

         List({ initialIndex: 0 }) {
           ListItem() {
             Row() {
               // ...
             }
             .onClick(() => {
               let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
               const RESULT_CODE: number = 1001; // FuncAbilityA返回的结果
               let abilityResult: common.AbilityResult = {
                 resultCode: RESULT_CODE,
                 want: {
                   bundleName: 'com.samples.uiabilityinteraction',
                   moduleName: 'entry', // moduleName非必选
                   abilityName: 'FuncAbilityA',
                   parameters: {
                     // 请将$r('app.string.ability_return_info')替换为实际资源文件，在本示例中该资源文件的value值为"来自FuncAbility Index页面"
                     info: context.resourceManager.getStringSync($r('app.string.ability_return_info').id)
                   },
                 },
               };
               context.terminateSelfWithResult(abilityResult, (err) => {
                 if (err.code) {
                   hilog.error(DOMAIN_NUMBER, TAG, `Failed to terminate self with result. Code is ${err.code}, message is ${err.message}`);
                   return;
                 }
               });
             })
           }
         }
         // ...
       }
       // ...
     }
   }
   ```
3. FuncAbility停止自身后，EntryAbility通过[startAbilityForResult()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startabilityforresult-2)方法回调接收被FuncAbility返回的信息，RESULT\_CODE需要与前面的数值保持一致。

   ```typescript
   import { common, Want } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   const TAG: string = '[MainPage]';
   const DOMAIN_NUMBER: number = 0xFF00;

   @Entry
   @Component
   struct MainPage {
     private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

     build() {
       Column() {
         List({ initialIndex: 0, space: 8 }) {

           // ...

           ListItem() {
             Row() {
               // ...
             }
             .onClick(() => {
               let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
               const RESULT_CODE: number = 1001;
               let want: Want = {
                 deviceId: '', // deviceId为空表示本设备
                 bundleName: 'com.samples.uiabilityinteraction',
                 moduleName: 'entry', // moduleName非必选
                 abilityName: 'FuncAbilityA',
                 parameters: {
                   // 自定义信息
                   // 请将$r('app.string.main_page_return_info')替换为实际资源文件，在本示例中该资源文件的value值为"来自EntryAbility MainPage页面"
                   info: $r('app.string.main_page_return_info')
                 }
               };
               context.startAbilityForResult(want).then((data) => {
                 if (data?.resultCode === RESULT_CODE) {
                   // 解析被调用方UIAbility返回的信息
                   let info = data.want?.parameters?.info;
                   hilog.info(DOMAIN_NUMBER, TAG, JSON.stringify(info) ?? '');
                   if (info !== null) {
                     this.getUIContext().getPromptAction().showToast({
                       message: JSON.stringify(info)
                     });
                   }
                 }
                 hilog.info(DOMAIN_NUMBER, TAG, JSON.stringify(data.resultCode) ?? '');
               }).catch((err: BusinessError) => {
                 hilog.error(DOMAIN_NUMBER, TAG, `Failed to start ability for result. Code is ${err.code}, message is ${err.message}`);
               });
             })
           }

           // ...
         }
         // ...
       }
       // ...
     }
   }
   ```

## 启动UIAbility的指定页面

### 概述

一个[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)可以对应多个页面，在不同的场景下启动该UIAbility时需要展示不同的页面，例如从一个UIAbility的页面中跳转到另外一个UIAbility时，希望启动目标UIAbility的指定页面。

UIAbility的启动分为两种情况：UIAbility冷启动和UIAbility热启动。

* UIAbility冷启动：指的是UIAbility实例处于完全关闭状态下被启动，这需要完整地加载和初始化UIAbility实例的代码、资源等。
* UIAbility热启动：指的是UIAbility实例已经启动并在前台运行过，由于某些原因切换到后台，再次启动该UIAbility实例，这种情况下可以快速恢复UIAbility实例的状态。

本文主要讲解[目标UIAbility冷启动](uiability-intra-device-interaction.md#目标uiability冷启动)和[目标UIAbility热启动](uiability-intra-device-interaction.md#目标uiability热启动)两种启动指定页面的场景，以及在讲解启动指定页面之前会讲解到在调用方如何指定启动页面。

### 调用方UIAbility指定启动页面

调用方[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)启动另外一个UIAbility时，通常需要跳转到指定的页面。例如FuncAbility包含两个页面（Index对应首页，Second对应功能A页面），此时需要在传入的[want](../harmonyos-references/js-apis-app-ability-want.md)参数中配置指定的页面路径信息，可以通过Want中的parameters参数增加一个自定义参数传递页面跳转信息。示例中的context的获取方式请参见[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

```typescript
import { common, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '[MainPage]';
const DOMAIN_NUMBER: number = 0xFF00;

@Entry
@Component
struct MainPage {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    Column() {
      List({ initialIndex: 0, space: 8 }) {

        // ...

        ListItem() {
          Row() {
            // ...
          }
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
            let want: Want = {
              deviceId: '', // deviceId为空表示本设备
              bundleName: 'com.samples.uiabilityinteraction',
              moduleName: 'entry', // moduleName非必选
              abilityName: 'ColdStartAbility',
              parameters: { // 自定义参数传递页面信息
                router: 'funcA'
              }
            };
            // context为调用方UIAbility的UIAbilityContext
            context.startAbility(want).then(() => {
              hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in starting ability.');
            }).catch((err: BusinessError) => {
              hilog.error(DOMAIN_NUMBER, TAG, `Failed to start ability. Code is ${err.code}, message is ${err.message}`);
            });
          })
        }

        // ...
      }
      // ...
    }
    // ...
  }
}
```

### 目标UIAbility冷启动

目标[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)冷启动时，在目标UIAbility的[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)生命周期回调中，接收调用方传过来的参数。然后在目标UIAbility的[onWindowStageCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)生命周期回调中，解析调用方传递过来的[want](../harmonyos-references/js-apis-app-ability-want.md)参数，获取到需要加载的页面信息url，传入[windowStage.loadContent()](../harmonyos-references/arkts-apis-window-windowstage.md#loadcontent9)方法。

```typescript
import { AbilityConstant, Want, UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window, UIContext } from '@kit.ArkUI';

const DOMAIN_NUMBER: number = 0xFF00;
const TAG: string = '[ColdStartAbility]';

export default class ColdStartAbility extends UIAbility {
  private funcAbilityWant: Want | undefined = undefined;
  private uiContext: UIContext | undefined = undefined;

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    // 接收调用方UIAbility传过来的参数
    this.funcAbilityWant = want;
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'Ability onWindowStageCreate');
    // Main window is created, set main page for this ability
    let url = 'pages/Index';
    if (this.funcAbilityWant?.parameters?.router && this.funcAbilityWant.parameters.router === 'funcA') {
      url = 'pages/ColdPage';
    }
    windowStage.loadContent(url, (err, data) => {
    // ···
    });
  }
}
```

### 目标UIAbility热启动

在应用开发中，会遇到目标[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)实例之前已经启动过的场景，这时再次启动目标UIAbility时，不会重新走初始化逻辑，只会直接触发[onNewWant()](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)生命周期方法。为了实现跳转到指定页面，需要在onNewWant()中解析参数进行处理。

例如短信应用和联系人应用配合使用的场景。

1. 用户先打开短信应用，短信应用的UIAbility实例启动，显示短信应用的主页。
2. 用户将设备回到桌面界面，短信应用进入后台运行状态。
3. 用户打开联系人应用，找到联系人张三。
4. 用户点击联系人张三的短信按钮，会再次启动短信应用的UIAbility实例。
5. 由于短信应用的UIAbility实例已经启动过了，此时会触发该UIAbility的onNewWant()回调，而不会再走[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)和[onWindowStageCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)等初始化逻辑。

图1 目标UIAbility热启动

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/Llj6UFnCRT6gpiW8A4LUXA/zh-cn_image_0000002736312119.png)

开发步骤如下所示。

1. 冷启动短信应用的UIAbility实例时，在[onWindowStageCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)生命周期回调中，通过调用[getUIContext()](../harmonyos-references/arkts-apis-window-window.md#getuicontext10)接口获取UI上下文实例[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)对象。

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { Want, UIAbility, AbilityConstant } from '@kit.AbilityKit';
   import { window, UIContext } from '@kit.ArkUI';
   const DOMAIN_NUMBER: number = 0xFF00;
   const TAG: string = '[HotStartAbility]';

   export default class HotStartAbility extends UIAbility {
     private funcAbilityWant: Want | undefined = undefined;
     private uiContext: UIContext | undefined = undefined;
    // ···
    
     onWindowStageCreate(windowStage: window.WindowStage): void {
       // Main window is created, set main page for this ability
       hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'Ability onWindowStageCreate');
       let url = 'pages/Index';
       windowStage.loadContent(url, (err, data) => {
         if (err.code) {
           return;
         }

         let windowClass: window.Window;
         windowStage.getMainWindow((err, data) => {
           if (err.code) {
             hilog.error(DOMAIN_NUMBER, TAG, `Failed to obtain the main window. Code is ${err.code}, message is ${err.message}`);
             return;
           }
           windowClass = data;
           this.uiContext = windowClass.getUIContext();
         });
         hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
       });
     }

   // ···
   }
   ```
2. 在短信应用UIAbility的[onNewWant()](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)回调中通过AppStorage设置全局变量nameForNavi的值，并进行指定页面的跳转。此时再次启动该短信应用的UIAbility实例时，即可跳转到该短信应用的UIAbility实例的指定页面。

   1. 导入相关模块，并在onNewWant()生命周期回调中设置全局变量nameForNavi的值。

      ```typescript
      import { hilog } from '@kit.PerformanceAnalysisKit';
      import { Want, UIAbility, AbilityConstant } from '@kit.AbilityKit';
      // ···
      const DOMAIN_NUMBER: number = 0xFF00;
      const TAG: string = '[HotStartAbility]';

      export default class HotStartAbility extends UIAbility {
      // ···

        onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
          hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'onNewWant');
          AppStorage.setOrCreate<string>('nameForNavi', 'pageOne');
        }
      }
      ```
   2. 在Index页面显示时触发onPageShow回调，获取全局变量nameForNavi的值，并进行执行页面的跳转。

      ```typescript
      @Entry
      @Component
      struct Index {
        @State message: string = 'Index';
        pathStack: NavPathStack = new NavPathStack();

        onPageShow(): void {
          let somePage = AppStorage.get<string>('nameForNavi')
          if (somePage) {
            this.pathStack.pushPath({ name: somePage }, false);
            AppStorage.delete('nameForNavi');
          }
        }

        build() {
          Navigation(this.pathStack) {
            Text(this.message)
              .id('Index')
              // 请将$r('app.float.page_text_font_size')替换为实际资源文件，在本示例中该资源文件的value值为"50fp"
              .fontSize($r('app.float.page_text_font_size'))
              .fontWeight(FontWeight.Bold)
              .alignRules({
                center: { anchor: '__container__', align: VerticalAlign.Center },
                middle: { anchor: '__container__', align: HorizontalAlign.Center }
              })
          }
          .mode(NavigationMode.Stack)
          .height('100%')
          .width('100%')
          .margin({top:250})
        }
      }
      ```
   3. 实现Navigation子页面。

      ```typescript
      @Builder
      export function PageOneBuilder() {
        PageOne();
      }

      @Component
      export struct PageOne {
        @State message: string = 'PageOne';
        pathStack: NavPathStack = new NavPathStack();

        build() {
          NavDestination() {
            Text(this.message)
              .id('PageOne')
              // 请将$r('app.float.page_text_font_size')替换为实际资源文件，在本示例中该资源文件的value值为"50fp"
              .fontSize($r('app.float.page_text_font_size'))
              .fontWeight(FontWeight.Bold)
              .alignRules({
                center: { anchor: '__container__', align: VerticalAlign.Center },
                middle: { anchor: '__container__', align: HorizontalAlign.Center }
              })
          }
          .onReady((context: NavDestinationContext) => {
            this.pathStack = context.pathStack;
          })
          .height('100%')
          .width('100%')
          .margin({top:250})
        }
      }
      ```
   4. 在系统配置文件route\_map.json中配置子页信息（参考[系统路由表](arkts-navigation-cross-package.md#系统路由表)）。

      ```ts
      // route_map.json
      {
        "routerMap": [
          {
            "name": "pageOne",
            "pageSourceFile": "src/main/ets/pages/PageOne.ets",
            "buildFunction": "PageOneBuilder",
            "data": {
              "description": "this is pageOne"
            }
          }
        ]
      }
      ```
   5. 在[module.json5配置文件](module-configuration-file.md#routermap标签)中配置routerMap路由映射。

      ```json5
      {
        "module": {
          // ···
          "routerMap": "$profile:router_map",
          // ···
        }
      }
      ```

**说明** 

当被调用方[UIAbility组件启动模式](uiability-launch-type.md)设置为multiton启动模式时，每次启动都会创建一个新的实例，那么onNewWant()回调就不会被用到。
