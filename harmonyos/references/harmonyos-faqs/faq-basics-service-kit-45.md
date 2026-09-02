---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-45
title: 如何判断当前设备类型为平板或手机，并配置锁定横屏或竖屏
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 如何判断当前设备类型为平板或手机，并配置锁定横屏或竖屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c9bda30ea9a4ddd4b2d538da2a11cd29f6d3dd73df087bfb1c857be030acd0f9
---

## 问题现象

如何根据获取的设备类型判断是平板还是手机？如果是平板强制屏幕横屏展示不跟随系统进行竖屏切换，如果是手机强制屏幕竖屏展示不跟随系统进行横屏切换。

## 背景知识

* [@ohos.deviceInfo (设备信息)](../harmonyos-references/js-apis-device-info.md)用于获取deviceType设备类型，详细参考[deviceTypes标签](../harmonyos-guides/module-configuration-file.md#devicetypes标签)。
* [setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)来设置主窗口的显示方向属性，参数[Orientation](../harmonyos-references/arkts-apis-window-e.md#orientation9)为窗口显示方向类型枚举。

## 解决方案

可以通过@ohos.deviceInfo接口的deviceType属性来获取设备类型，具体请参考[设备类型枚举](../harmonyos-references/js-apis-device-info.md#devicetypes20)。再通过setPreferredOrientation来设置主窗口的显示方向属性，其中参数Orientation为窗口显示方向类型枚举。

```ts
import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { deviceInfo } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(): void {
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
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        hilog.error(DOMAIN, 'testTag', 'Failed to obtain the main window. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      windowClass = data;
      // 获取设备类型
      let deviceTypeInfo: string = deviceInfo.deviceType;
      hilog.info(DOMAIN, 'testTag', 'the value of the deviceType is:', JSON.stringify(deviceTypeInfo));
      let orientation = window.Orientation.AUTO_ROTATION;
      // 判断设备是手机or平板，来设置窗口显示方向
      if (deviceTypeInfo == 'phone') {
        orientation = window.Orientation.PORTRAIT;
      } else if (deviceTypeInfo == 'tablet') {
        orientation = window.Orientation.LANDSCAPE;
      }
      try {
        windowClass.setPreferredOrientation(orientation, (err: BusinessError) => {
          const errCode: number = err.code;
          if (errCode) {
            hilog.error(DOMAIN, 'testTag', 'Failed to set window orientation. Cause: %{public}s', JSON.stringify(err));

            return;
          }
          hilog.info(DOMAIN, 'testTag', 'Succeeded in setting window orientation.');
        });
      } catch (exception) {
        hilog.error(DOMAIN, 'testTag', 'Failed to set window orientation. Cause: %{public}s', JSON.stringify(err));
      }
    });

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

## 常见FAQ

Q：如何设置应用在启动后就默认横屏显示？

A：可以配置module.json5中abilities标签的Orientation字段，例如LANDSCAPE（仅支持横屏）或AUTO\_ROTATION\_LANDSCAPE（支持在横屏和反向横屏中切换）。

Q：在平板设备上设置"orientation": "portrait"无效的原因是什么？

A：由于平板设备启用了强制横屏模式，因此"orientation": "portrait"的设置无法生效。
