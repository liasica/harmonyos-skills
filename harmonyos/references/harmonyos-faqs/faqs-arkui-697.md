---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-697
title: PC端启动应用默认全屏模式显示，非悬浮窗模式
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > PC端启动应用默认全屏模式显示，非悬浮窗模式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d0c6d6b33cd945e93a60ca9d547979f1492c13b603f1153c9b0697a9aa781a5e
---

## 问题现象

启动应用时默认全屏模式显示，期望在PC端启动时为悬浮窗模式。

## 背景知识

* supportWindowMode：应用配置文件[module.json5](../harmonyos-guides/module-configuration-file.md)的[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)中有属性supportWindowMode，用于标识当前UIAbility组件所支持的窗口模式，但不支持根据设备设置窗口模式。
* [setSupportedWindowModes](../harmonyos-references/arkts-apis-window-windowstage.md#setsupportedwindowmodes15)：针对平板或2in1设备，windowStage.setSupportedWindowModes可以用于设置主窗的窗口支持模式。
* [deviceType](../harmonyos-references/js-apis-device-info.md#常量)：deviceInfo.deviceType可以获取当前设备的类型。
* [recover](../harmonyos-references/arkts-apis-window-window.md#recover11)：在平板或2in1设备，调用windowClass.recover可以将主窗口从全屏、最大化、分屏模式下还原为悬浮窗口，并恢复到进入该模式之前的大小和位置。

## 问题定位

1. 确认配置文件module.json5中是否配置supportWindowMode为fullscreen。
2. 确认是否有使用setSupportedWindowModes设置主窗的窗口支持模式SupportWindowMode.FLOATING。
3. 确认是否有调用windowClass.recover将主窗口切换为悬浮窗口。

## 分析结论

由于配置文件module.json5中配置的supportWindowMode不支持根据设备设置窗口模式，未使用setSupportedWindowModes设置主窗的窗口支持模式SupportWindowMode.FLOATING，且未调用windowClass.recover，故在PC上无法设置为悬浮窗模式。

## 修改建议

可以在onWindowStageCreate生命周期接口中，判断设备类型为2in1时使用setSupportedWindowModes设置其主窗支持悬浮窗模式，并调用windowClass.recover将主窗口切换为悬浮窗口。示例代码如下：

```ts
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError, deviceInfo } from '@kit.BasicServicesKit';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    hilog.info(DOMAIN, 'testTag', `onCreate, want: ${want.abilityName}, the launchReason is ${launchParam.launchReason}`);
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    // 获取设备类型
    let deviceType = deviceInfo.deviceType;
    // setSupportedWindowModes的系统能力为SystemCapability.Window.SessionManager，调用canIUse确认当前支持该系统能力
    let isLocationAvailable = canIUse('SystemCapability.Window.SessionManager');
    if (isLocationAvailable && deviceType === '2in1') {
      try {
        // 设置主窗口支持悬浮窗模式和全屏模式
        let promise = windowStage.setSupportedWindowModes([
          bundleManager.SupportWindowMode.FLOATING,
          bundleManager.SupportWindowMode.FULL_SCREEN
        ]);
        promise.then(() => {
          console.info('Succeeded in setting window support modes');
        }).catch((err: BusinessError) => {
          console.error(`Failed to set window support modes. Cause code: ${err.code}, message: ${err.message}`);
        });
      } catch (exception) {
        console.error(`Failed to set window support modes. Cause code: ${exception.code}, message: ${exception.message}`);
      }
      windowStage.getMainWindow().then((data: window.Window) => {
        // 调用recover接口，将主窗口切换为悬浮窗模式
        data.recover().then(() => {
          console.info('recover success.');
        }).catch((err: BusinessError) => {
          console.info(`recover failed. Error code: ${err.code}`);
        });
      });
    }

    windowStage.loadContent('pages/Index', (err) => {
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
