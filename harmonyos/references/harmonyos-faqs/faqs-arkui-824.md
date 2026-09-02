---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-824
title: 如何解决获取导航栏高度失败的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何解决获取导航栏高度失败的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5653cce6b2ef196d5eeafe1a42957b953c547116bfa031982e48a26a0c0b78d7
---

## 问题现象

如何解决使用getWindowAvoidArea方法无法获取到导航栏高度的问题？

问题代码如下：

```ts
onWindowStageCreate(windowStage: window.WindowStage): void {
  // Main window is created,set main page for this ability
  hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

  windowStage.loadContent('pages/Index', (err) => {
    if (err.code) {
      hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
      return;
    }
    hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
  });

  windowStage.getMainWindow((err, data) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(`Failed to obtain the main window. Cause code: ${errCode}, message: ${err.message}`);
      return;
    }
    let windowClass: window.Window;
    // 获取应用主窗口
    windowClass = data;
    // 获取底部导航栏高度，此时的高度单位是px
    let navigationHeight = windowClass.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM).bottomRect.height;
    let navHeightVp = windowClass.getUIContext().px2vp(navigationHeight);
    console.info(`获取导航栏高度：${navigationHeight}px--${navHeightVp}vp`);
  });

}
```

输出日志如下：

```log
获取导航栏高度：0px--0vp
```

## 背景知识

[getWindowAvoidArea](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)可以获取窗口避让区，入参为需要获取的避让区类型，返回值为避让区的相关信息。

## 问题定位

window.AvoidAreaType.TYPE\_SYSTEM表示系统默认区域，并不包括底部导航栏，其中getWindowAvoidArea(window.AvoidAreaType.TYPE\_SYSTEM).topRect表示顶部状态栏，但getWindowAvoidArea(window.AvoidAreaType.TYPE\_SYSTEM)其底部并不包含底部导航栏，所以其bottomRect.height为0。

## 分析结论

入参[AvoidAreaType](../harmonyos-references/arkts-apis-window-e.md#avoidareatype7)的枚举类型中，TYPE\_NAVIGATION\_INDICATOR表示底部导航区域。

## 修改建议

综上所述，需要获取底部导航区域高度时，其值应该为windowClass.getWindowAvoidArea(window.AvoidAreaType.TYPE\_NAVIGATION\_INDICATOR).bottomRect.height。

完整代码如下：

```ts
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    console.info(`want: ${want}`);
    console.info(`launchParam: ${launchParam}`);
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
    }
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
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

    windowStage.getMainWindow((err, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${errCode}, message: ${err.message}`);
        return;
      }
      let windowClass: window.Window;
      // 获取应用主窗口
      windowClass = data;
      // 获取底部导航栏高度，此时的高度单位是px
      let navigationHeight =
        windowClass.getWindowAvoidArea(window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR).bottomRect.height;
      let navHeightVp = windowClass.getUIContext().px2vp(navigationHeight);
      console.info(`获取导航栏高度：${navigationHeight}px--${navHeightVp}vp`);
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

输出日志为：

```log
获取导航栏高度：98px--28vp
```
