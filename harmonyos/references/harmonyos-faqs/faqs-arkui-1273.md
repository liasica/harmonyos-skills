---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1273
title: DPI相关单位换算
breadcrumb: FAQ > 应用框架开发 > UI框架 > 屏幕管理 > DPI相关单位换算
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:dae574f22549b27b8803ee845fc5ad944bc26b05e01b930a285fc5f95196c062
---

## 问题现象

为了在不同的手机上都能够显示准确的毫米值，想清楚屏幕DPI像素单位px与1mm间有何转换关系，以及px与尺寸单位vp之间又该如何转换？

## 背景知识

[@ohos.display](../harmonyos-references/js-apis-display.md)是HarmonyOS中的一个模块，用于管理和控制设备的屏幕属性。它提供了许多接口和方法，允许开发者获取和设置屏幕的相关信息，如分辨率、刷新率等，具体可以查看[display屏幕实例属性](../harmonyos-references/js-apis-display.md#display)，其属性DPI指的是显示设备屏幕的物理像素密度，表示每英寸上的像素点数。一英寸为25.4毫米。

## 解决方案

* 实现px与1mm之间转换，需要通过display中getDefaultDisplaySync方法获取屏幕DPI及每英寸上的像素点数，再通过一英寸等于25.4毫米进行计算得出。

  ```screen
  import { display } from '@kit.ArkUI';

  @Entry
  @Component
  struct Index {
    @State px2mm: number = 0;

    aboutToAppear(): void {
      let displayClass: display.Display = display.getDefaultDisplaySync();
      // 获取屏幕高度（以像素为单位）
      let height = displayClass.height;
      // 获取屏幕的垂直方向的DPI（每英寸点数）
      let dpi = displayClass.yDPI;
      console.info(`屏幕Y方向对应的DPI:${dpi}`);
      console.info(`屏幕宽度的物理长度（mm）:${height / dpi * 25.4}`);
      console.info(`屏幕宽度一毫米有多少px:${dpi / 25.4}`);
      this.px2mm = dpi / 25.4;
    }

    build() {
      Column() {
        Text(`屏幕宽度一mm有:${this.px2mm}px`);
      }
      .margin({ top: 100 });
    }
  }
  ```
* 实现px与尺寸单位vp之间的转换，需在明确目标设备的屏幕DPI后，通过转换公式px=vp\*(DPI/160)计算即可。

## 常见FAQ

Q：display中getDefaultDisplaySync方法获取屏幕DPI受到系统缩放影响，若开发者不希望应用受显示缩放影响布局，使用setDefaultDensityEnabled()设置应用是否使用系统默认Density，如何获取默认DPI值？

A：可以用getWindowDensityInfo，里面的defaultDensity是设备的默认densityPixels，不会跟随系统变化。systemDensity是会跟随系统变化的。而customDensity是受windowStage.setDefaultDensityEnabled()影响，true时不跟随系统变化，false时跟随，[参考链接](../harmonyos-references/arkts-apis-window-window.md#getwindowdensityinfo15)。
