---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/brightness-control
title: 控制亮度与常亮 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 其他开发场景 > 控制亮度与常亮 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:56928f5503fcd713b5ffab1fe159f6a5ca73119e6a4d8e42dc9002a66fde97dc
---

## 场景介绍

亮度控制用于调节应用窗口或设备屏幕的显示明暗程度，开发者可根据页面内容特征、使用场景和显示需求，对亮度进行动态调整，以提升页面可读性和内容辨识度。亮度主要包含[窗口亮度与屏幕亮度](brightness-control.md#窗口亮度与屏幕亮度)。

常亮控制用于决定屏幕在一段时间内是否保持点亮状态，适用于需要持续展示内容或长时间保持交互可见性的场景，可避免因系统自动熄屏影响业务流程。

## 窗口亮度与屏幕亮度

* **窗口亮度**：指当前应用窗口的显示亮度，仅作用于主窗口，不直接修改设备全局亮度。

  开发者可根据当前页面的展示需求，对窗口亮度单独进行调节，以优化当前应用内的显示效果。可以通过调用[setWindowBrightness()](../harmonyos-references/arkts-apis-window-window.md#setwindowbrightness9-1)接口设置主窗口的窗口亮度。

  **说明** 

  当使用[setWindowBrightness()](../harmonyos-references/arkts-apis-window-window.md#setwindowbrightness9-1)接口设置主窗口的窗口亮度时：

  + 当主窗口处于前台且获焦时，窗口亮度生效（即设置的亮度值会成为当前窗口实际显示亮度），且只会影响当前设备屏幕亮度，无法修改虚拟屏（如投屏所在的屏幕）的屏幕亮度。
  + 当窗口退至后台时，窗口亮度失效，可以通过控制中心或快捷键调整。不建议连续调用或窗口退至后台时调用此接口，否则可能产生时序问题。
* **屏幕亮度**：指设备屏幕的全局显示亮度，作用范围覆盖整个屏幕，会影响系统界面以及所有应用窗口的显示效果。

  屏幕亮度可通过**控制中心**或者**设置 > 显示和亮度**进行调整。目前没有直接设置系统屏幕亮度的接口，但当[setWindowBrightness()](../harmonyos-references/arkts-apis-window-window.md#setwindowbrightness9-1)传入-1时，窗口亮度恢复为系统屏幕亮度。

## 控制屏幕常亮

控制屏幕常亮指通过调用[setWindowKeepScreenOn()](../harmonyos-references/arkts-apis-window-window.md#setwindowkeepscreenon9-1)接口设置当前窗口位于前台时设备的屏幕是否为常亮状态。当前台存在已设置为常亮的窗口时，设备的超时自动熄屏能力将被禁用。在异源虚拟屏上不生效。

建议在明确且有必要保持屏幕常亮的场景下使用，例如导航、视频播放、绘画、游戏等。在无屏幕交互、纯音频播放或其他无需持续点亮屏幕的场景下，不建议设置屏幕常亮。

当窗口退到后台时，系统会自动释放该窗口持有的常亮锁。对于视频播放类应用，当音频流或视频流中断一段时间后，例如暂停、网络卡顿等场景，系统也会自动释放常亮锁。

**说明** 

此类场景下长时间保持屏幕常亮，可能增加设备功耗并影响续航。建议结合业务需要合理控制常亮时长，以保障用户体验。

示例代码如下：

```typescript
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;

@Entry
@Component
struct Index {
  @State brightnessValue: number = 0.5;
  @State keepScreenOn: boolean = false;
  @State statusText: string = 'Adjust window brightness or keep-screen-on.';

  private currentWindow?: window.Window = undefined;

  aboutToAppear(): void {
    void this.initWindow();
  }

  // 获取当前应用窗口，后续通过 Window 对象设置窗口亮度和常亮状态。
  private async initWindow(): Promise<void> {
    try {
      const hostContext = this.getUIContext().getHostContext();
      if (!hostContext) {
        throw new Error('Host context is unavailable.');
      }

      const context = hostContext as common.UIAbilityContext;
      this.currentWindow = await window.getLastWindow(context);

      const windowId = this.currentWindow.getWindowProperties().id;
      this.statusText = `window ready, id=${windowId}`;
      hilog.info(DOMAIN, 'windowBrightness', this.statusText);
    } catch (err) {
      this.statusText = `initWindow failed: ${JSON.stringify(err)}`;
      hilog.error(DOMAIN, 'windowBrightness', this.statusText);
    }
  }

  // 调用接口前确认窗口对象已初始化。
  private async ensureWindow(): Promise<boolean> {
    if (!this.currentWindow) {
      await this.initWindow();
    }

    if (!this.currentWindow) {
      this.statusText = 'current window is unavailable.';
      return false;
    }

    return true;
  }

  // 设置当前窗口亮度，取值范围为 0 到 1；传入 -1 可恢复为系统屏幕亮度。
  private async applyBrightness(): Promise<void> {
    if (!await this.ensureWindow()) {
      return;
    }

    try {
      await this.currentWindow!.setWindowBrightness(this.brightnessValue);
      this.statusText = `setWindowBrightness(${this.brightnessValue.toFixed(2)}) success`;
      hilog.info(DOMAIN, 'windowBrightness', this.statusText);
    } catch (err) {
      this.statusText = `setWindowBrightness failed: ${JSON.stringify(err)}`;
      hilog.error(DOMAIN, 'windowBrightness', this.statusText);
    }
  }

  // 设置当前窗口在前台时是否保持屏幕常亮。
  private async applyKeepScreenOn(value: boolean): Promise<void> {
    if (!await this.ensureWindow()) {
      return;
    }

    try {
      this.keepScreenOn = value;
      await this.currentWindow!.setWindowKeepScreenOn(value);
      this.statusText = `setWindowKeepScreenOn(${value}) success`;
      hilog.info(DOMAIN, 'windowBrightness', this.statusText);
    } catch (err) {
      this.statusText = `setWindowKeepScreenOn failed: ${JSON.stringify(err)}`;
      hilog.error(DOMAIN, 'windowBrightness', this.statusText);
    }
  }

  build() {
    Column({ space: 16 }) {
      Text('Brightness and Keep Screen On')
        .fontSize(24)
        .fontWeight(FontWeight.Bold)
        .width('100%')
        .textAlign(TextAlign.Start)

      Text(`Brightness: ${this.brightnessValue.toFixed(2)}`)
        .width('100%')
        .fontSize(16)
        .textAlign(TextAlign.Start)

      Slider({
        value: this.brightnessValue,
        min: 0,
        max: 1,
        step: 0.01
      })
        .width('100%')
        .showTips(true)
        .onChange((value: number) => {
          this.brightnessValue = value;
        })

      Button('Apply Brightness')
        .width('100%')
        .onClick(() => {
          void this.applyBrightness();
        })

      Row() {
        Text(`Keep screen on: ${this.keepScreenOn}`)
          .layoutWeight(1)
          .fontSize(16)

        Toggle({ type: ToggleType.Switch, isOn: this.keepScreenOn })
          .onChange((value: boolean) => {
            void this.applyKeepScreenOn(value);
          })
      }
      .width('100%')

      Text(this.statusText)
        .width('100%')
        .fontSize(14)
        .textAlign(TextAlign.Start)
    }
    .width('100%')
    .height('100%')
    .padding(20)
    .alignItems(HorizontalAlign.Start)
  }
}
```
