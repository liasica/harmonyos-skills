---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-369
title: 如何同时获取屏幕方向orientation和系统规避区avoidAreaChange信息
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何同时获取屏幕方向orientation和系统规避区avoidAreaChange信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f2cc9ff0f9b633a4b0b9dfcac0e3ad30b3be852bfeb307133b61d982450da45d
---

以折叠屏形态变化时触发为示例，可以在EntryAbility.ets文件中通过[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)接口监听窗口系统规避区的变化，在callback中获取avoidAreaChange信息，并通过Display实例获取屏幕方向orientation等信息。

```ts
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { display, window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
    });

    let windowClass: window.Window | undefined = undefined;
    try {
      window.getLastWindow(this.context, (err: BusinessError, data) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        windowClass = data;
        console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
        if (windowClass) {
          // Please ensure that the relevant Window instance, namely windowClass, has been obtained
          windowClass.on('avoidAreaChange', async (data) => {
            console.info('Succeeded in enabling the listener for avoid area changes. Type: ' +
            JSON.stringify(data.type) + ', area ' + JSON.stringify(data.area));
            try {
              let defaultDisplay: display.Display = display.getDefaultDisplaySync();
              console.info('---Orientation: ' + defaultDisplay.orientation);
            } catch (error) {
              let err = error as BusinessError;
              hilog.error(0x0000, 'EntryAbility', `error code:${err.code},message:${err.message}`);
            }
          });
        }
      });
    } catch (exception) {
      console.error(`Failed to obtain the top window. Cause code: ${exception.code}, message: ${exception.message}`);
    }
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
  }
}
```

**参考链接**

[开启当前窗口系统规避区变化的监听](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9) [显示设备当前显示的方向枚举](../harmonyos-references/js-apis-display.md#orientation10)
