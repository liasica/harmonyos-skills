---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-987
title: 智能表结合ArcSlider实现调节屏幕亮度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 智能表结合ArcSlider实现调节屏幕亮度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9a17f5bcc949210bb1002a23d8f9632c53d4de2e6f45fed9d6ebe984c7d87957
---

## 问题现象

智能表为圆形屏幕的穿戴设备，如何在页面显示弧形滑动条，并通过滑动条调节屏幕亮度？

## 背景知识

* [ArcSlider](../harmonyos-references/ohos-arkui-advanced-arcslider.md)：弧形滑动条组件，通常用于在圆形屏幕的穿戴设备中快速调节设置值，如音量调节、亮度调节等应用场景。
* [setWindowBrightness](../harmonyos-references/arkts-apis-window-window.md#setwindowbrightness9)：允许应用主窗口设置屏幕亮度值，使用callback异步回调，智能表应用也支持使用。

## 解决方案

1. 添加ArcSlider组件实现弧形滑动条，[ArcSliderOptionsConstructorOptions](../harmonyos-references/ohos-arkui-advanced-arcslider.md#arcslideroptionsconstructoroptions)的onChange事件中把ArcSlider当前的进度值设置为屏幕亮度值。
2. 通过window实例提供的setWindowBrightness方法设置屏幕亮度。

完整示例参考如下：

```ts
import {
  ArcSlider,
  ArcSliderOptions,
  ArcSliderValueOptions,
  ArcSliderLayoutOptions,
  ArcSliderStyleOptions,
  ArcSliderValueOptionsConstructorOptions,
  ArcSliderLayoutOptionsConstructorOptions,
  ArcSliderStyleOptionsConstructorOptions,
  ArcSliderOptionsConstructorOptions,
  window
} from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@ComponentV2
struct Index {
  // 通过window实例提供的setWindowBrightness()方法，即可设置屏幕亮度。
  changeBrightness(brightness: number) {
    try {
      let windowClass: window.Window | undefined = undefined;
      let promise = window.getLastWindow(this.getUIContext().getHostContext());
      promise.then((data) => {
        windowClass = data;
        windowClass.setWindowBrightness(brightness, (err: BusinessError) => {
          const errCode: number = err.code;
          if (errCode) {
            console.error(`Failed to set the Brightness value. Cause code: ${err.code}, message: ${err.message}`);
            return;
          }
        });
      });
    } catch (exception) {
      console.error(`Failed to set the Brightness value. Cause code: ${exception.code}, message: ${exception.message}`);
    }
  }

  // ArcSliderValueOptions的构造信息，设置当前进度值、最小值和最大值
  valueOptionsConstructorOptions: ArcSliderValueOptionsConstructorOptions = {
    progress: 1,
    min: 0,
    max: 1
  };
  // ArcSliderLayoutValueOptions的构造信息，设置弧形Slider从下往上滑动
  layoutOptionsConstructorOptions: ArcSliderLayoutOptionsConstructorOptions = {
    reverse: true
  };
  // ArcSliderStyleOptions的构造信息，设置弧形Slider的描边粗细、描边背景色、描边高亮色、描边背景模糊值
  styleOptionsConstructorOptions: ArcSliderStyleOptionsConstructorOptions = {
    trackThickness: 16,
    activeTrackThickness: 24,
    trackColor: '#ffd5d5d5',
    selectedColor: '#ff2787d9',
    trackBlur: 20
  };
  valueOptions: ArcSliderValueOptions = new ArcSliderValueOptions(this.valueOptionsConstructorOptions);
  layoutOptions: ArcSliderLayoutOptions = new ArcSliderLayoutOptions(this.layoutOptionsConstructorOptions);
  styleOptions: ArcSliderStyleOptions = new ArcSliderStyleOptions(this.styleOptionsConstructorOptions);
  arcSliderOptionsConstructorOptions: ArcSliderOptionsConstructorOptions = {
    valueOptions: this.valueOptions,
    layoutOptions: this.layoutOptions,
    styleOptions: this.styleOptions,
    digitalCrownSensitivity: CrownSensitivity.HIGH,
    // 弧形Slider的进度值发生变化时触发
    onChange: (progress: number) => {
      this.changeBrightness(progress);

      let windowClass: window.Window | undefined = undefined;
      let promise = window.getLastWindow(this.getUIContext().getHostContext());
      promise.then((data) => {
        windowClass = data;
        try {
          let properties = windowClass.getWindowProperties();
          let bright = properties?.brightness ?? -1;
          this.getUIContext().getPromptAction().openToast({
            message: '屏幕亮度值: ' + bright,
            duration: 2000
          }).catch(() => {
            console.error('Failed to open Toast.');
          });
        } catch (error) {
          console.error(`Failed to get the Window Properties. Cause code: ${error.code}, message: ${error.message}`);
        }
      });
    }
  };
  arcSliderOptions: ArcSliderOptions = new ArcSliderOptions(this.arcSliderOptionsConstructorOptions);

  build() {
    Column() {
      if (canIUse('SystemCapability.ArkUI.ArkUI.Circle')) {
        ArcSlider({ options: this.arcSliderOptions });
      }
    }
    .width('100%');
  }
}
```
