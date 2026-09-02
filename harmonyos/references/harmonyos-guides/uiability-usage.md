---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage
title: UIAbility组件基本用法
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > 应用模型 > 应用组件 > UIAbility组件 > UIAbility组件基本用法
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f9d330144fceeffb3e7aeb120bb65ffe397869a98c6d6d3685f52059601f6563
---

本文主要介绍[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)组件的基本用法，包括：

* 指定UIAbility的启动页面。
* 获取UIAbility的上下文[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)。
* 获取UIAbility拉起方的信息。

## 指定UIAbility的启动页面

应用中的[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)在启动过程中，需要指定启动页面，否则应用启动后会因为没有默认加载页面而导致白屏。可以在UIAbility的[onWindowStageCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)生命周期回调中，通过[WindowStage](../harmonyos-references/arkts-apis-window-windowstage.md)对象的[loadContent()](../harmonyos-references/arkts-apis-window-windowstage.md#loadcontent9)方法设置启动页面。

```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
// ···

export default class EntryAbility extends UIAbility {
// ···

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    windowStage.loadContent('pages/Index', (err) => {
      // ···
    });
  }

// ···
}
```

**说明** 

在DevEco Studio中创建的UIAbility中，该UIAbility实例默认会加载Index页面，根据需要将Index页面路径替换为需要的页面路径即可。

## 获取UIAbility的上下文信息

[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)类拥有自身的上下文信息，该信息为[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)类的实例，[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)类拥有abilityInfo、currentHapModuleInfo等属性。通过UIAbilityContext可以获取UIAbility的相关配置信息，如包代码路径、Bundle名称、Ability名称和应用程序需要的环境状态等属性信息，以及可以获取操作UIAbility实例的方法（如[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)、[connectServiceExtensionAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#connectserviceextensionability)、[terminateSelf()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateself)等）。

如果需要在页面中获得当前Ability的Context，需要通过调用组件的[getUIContext()](../harmonyos-references/ts-custom-component-api.md#getuicontext)方法获取[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)对象，再调用UIContext对象的[getHostContext()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#gethostcontext12)方法获取当前页面关联的UIAbilityContext或[ExtensionContext](../harmonyos-references/js-apis-inner-application-extensioncontext.md)。

* 在UIAbility中可以通过this.context获取UIAbility实例的上下文信息。

  ```typescript
  import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
  // ···

  export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
      // 获取UIAbility实例的上下文
      let context = this.context;
    }
  // ···
  }
  ```
* 在页面中获取UIAbility实例的上下文信息，包括导入依赖资源context模块和在组件中定义一个context变量两个部分。

  ```typescript
  import { common, Want } from '@kit.AbilityKit';

  @Entry
  @Component
  struct EventHubPage {
    private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

    startAbilityTest(): void {
      let want: Want = {
        // Want参数信息
        // ...
      };
      this.context.startAbility(want);
    }

    // 页面展示
    build() {
      // ...
    }
  }
  ```

  也可以在导入依赖资源context模块后，在具体使用[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)前进行变量定义。

  ```typescript
  import { common, Want } from '@kit.AbilityKit';
  // ...

  @Entry
  @Component
  struct BasicUsage {
    startAbilityTest(): void {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let want: Want = {
        // Want参数信息
        // ...
      };
      context.startAbility(want);
    }

    // 页面展示
    build() {
      // ...
    }
  }
  ```
* 当业务完成后，开发者如果想要终止当前[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)实例，可以通过调用[terminateSelf()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateself)方法实现。

  ```typescript
  import { common, Want } from '@kit.AbilityKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';

  const DOMAIN = 0x0000;

  @Entry
  @Component
  struct BasicUsage {
    // ...

    // 页面展示
    build() {
      Column() {
        // ...

        Button('FuncAbilityB')
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            try {
              context.terminateSelf((err: BusinessError) => {
                if (err.code) {
                  // 处理业务逻辑错误
                  hilog.error(DOMAIN, 'terminateSelf', `terminateSelf failed, code is ${err.code}, message is ${err.message}.`);
                  return;
                }
                // 执行正常业务
                hilog.info(DOMAIN, 'terminateSelf', `terminateSelf succeed.`);
              });
            } catch (err) {
              // 捕获同步的参数错误
              let code = (err as BusinessError).code;
              let message = (err as BusinessError).message;
              hilog.error(DOMAIN, 'terminateSelf', `terminateSelf failed, code is ${code}, message is ${message}.`);
            }
          })
          // ...
      }
      // ...
    }
  }
  ```

## 获取UIAbility拉起方的信息

拉起方（UIAbilityA）通过startAbility启动目标方（UIAbilityB）时，UIAbilityB可以通过[@ohos.app.ability.Want](../harmonyos-references/js-apis-app-ability-want.md)中parameters参数获取UIAbilityA的Pid、BundleName和AbilityName等信息。

1. 通过点击UIAbilityA中的"拉起UIAbilityB"按钮，拉起UIAbilityB。

   ```typescript
   import { common, Want } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct Index {
     @State context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

     build() {
       List({ space: 4 }) {
         ListItem() {
           Button('terminateSelf').onClick(() => {
             this.context.terminateSelf()
           })
             .width('100%')

         }

         ListItem() {
           // 请将$r('app.string.Start_UIAbilityB')替换为实际资源文件，在本示例中该资源文件的value值为"拉起UIAbilityB"
           Button($r('app.string.Start_UIAbilityB'))
             .onClick((event: ClickEvent) => {
               let want: Want = {
                 bundleName: this.context.abilityInfo.bundleName,
                 abilityName: 'UIAbilityB',
               };

               this.context.startAbility(want, (err: BusinessError) => {
                 if (err.code) {
                   console.error(`Failed to startAbility. Code: ${err.code}, message: ${err.message}.`);
                 }
               });
           })
             .width('100%')
         }
       }
       .listDirection(Axis.Vertical)
       .backgroundColor(0xDCDCDC).padding(20)
       .margin({top:250})
     }
   }
   ```
2. 在UIAbilityB的[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)生命周期中，获取UIAbilityA的Pid、BundleName和AbilityName，并通过日志输出。

   ```typescript
   import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   import { window } from '@kit.ArkUI';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const DOMAIN = 0x0000;

   export default class UIAbilityB extends UIAbility {
     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       // 调用方无需手动传递parameters参数，系统会自动向Want对象中传递调用方信息。
       hilog.info(DOMAIN, 'UIAbilityB', `onCreate, callerPid: ${want.parameters?.['ohos.aafwk.param.callerPid']}.`);
       hilog.info(DOMAIN, 'UIAbilityB', `onCreate, callerBundleName: ${want.parameters?.['ohos.aafwk.param.callerBundleName']}.`);
       hilog.info(DOMAIN, 'UIAbilityB', `onCreate, callerAbilityName: ${want.parameters?.['ohos.aafwk.param.callerAbilityName']}.`);
     }

     onDestroy(): void {
       hilog.info(DOMAIN, 'UIAbilityB', `UIAbilityB onDestroy.`);
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       hilog.info(DOMAIN, 'UIAbilityB', `Ability onWindowStageCreate.`);

       windowStage.loadContent('context/BasicUsage', (err) => {
         if (err.code) {
           hilog.error(DOMAIN, 'UIAbilityB', `Failed to load the content, error code: ${err.code}, error msg: ${err.message}.`);
           return;
         }
         hilog.info(DOMAIN, 'UIAbilityB', `Succeeded in loading the content.`);
       });
     }
   }
   ```
