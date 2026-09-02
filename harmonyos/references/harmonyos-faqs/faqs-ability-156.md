---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-156
title: HarmonyOS应用中如何关闭深色模式
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > HarmonyOS应用中如何关闭深色模式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:26f731cf04faf502a6b08efd52c97c6d1c2969ebfa01e35b52cf2f44ba2d7980
---

## 问题现象

HarmonyOS深色模式支持关闭吗？是否可以在APP中不使用深色模式？

## 背景知识

* [ApplicationContext.setColorMode](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextsetcolormode11)方法可以自定义应用的颜色模式，官网案例参考：[深色模式适配](../best-practices/bpta-dark-mode-adaptation.md)。该案例内有详细说明如何实现深浅色模式适配以及如何取消或跟随系统的深浅色切换。
* [setColorMode](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#setcolormode18)方法可以将[ColorMode](../harmonyos-references/js-apis-app-ability-configurationconstant.md#colormode)设置不同的枚举，开发者可以使用这些预置枚举设置或获取系统/应用的深浅色模式。

  | 名称 | 值 | 说明 |
  | --- | --- | --- |
  | COLOR\_MODE\_NOT\_SET | -1 | 表示未设置颜色模式。 |
  | COLOR\_MODE\_DARK | 0 | 表示深色模式。 |
  | COLOR\_MODE\_LIGHT | 1 | 表示浅色模式。 |

## 解决方案

1. 应用主动设置深浅色模式的场景。

   如果应用调用[setColorMode](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#setcolormode18)接口主动设置了深浅色，则以接口效果优先。

   EntryAbility.ets文件示例参考如下：

   ```ts
   import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';

   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {
     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       try {
         this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
       } catch (err) {
         hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
       }
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
       console.info(`${want} + ${launchParam}`);
     }

     onDestroy(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
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

       let applicationContext = this.context.getApplicationContext();
       applicationContext.setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT); //主动设置深浅色模式
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

   }
   ```
2. 应用未主动设置深浅色模式的场景。
   * 如果应用工程dark目录下有深色资源，则系统内置组件在深色模式下会自动切换成为深色。
   * 如果应用工程dark目录下没有任何深色资源，则系统内置组件在深色模式下仍会保持浅色体验。

## 常见FAQ

Q：在没有调用[setColorMode](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#setcolormode18)接口的情况下，如何修改状态栏的颜色？

A：可以在EntryAbility.ets中修改状态栏的颜色。

```ts
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
    }
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
    console.info(`${want} + ${launchParam}`);
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  async onWindowStageCreate(windowStage: window.WindowStage): Promise<void> {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });

    (await windowStage.getMainWindow()).setWindowSystemBarProperties({
      // 设置状态栏颜色为其他颜色
      statusBarColor: '#ffa28d8f',
      // 设置状态栏文本颜色为白色
      statusBarContentColor: '#ffe30520'
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

}
```
