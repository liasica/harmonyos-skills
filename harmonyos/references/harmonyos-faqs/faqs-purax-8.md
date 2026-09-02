---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-purax-8
title: 折叠屏展开态下，图片被拉伸
breadcrumb: FAQ > 多设备场景 > 手机 > Pura X常见问题 > 折叠屏展开态下，图片被拉伸
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a37020019d1b4d89ca313347c7338d049840fe564a9106205327765ea91a2de8
---

## 问题现象

在折叠屏展开态下，部分图片分辨率异常，被拉伸。

## 背景知识

* [Image](../harmonyos-references/ts-basic-components-image.md)组件的[objectFit](../harmonyos-references/ts-basic-components-image.md#objectfit)属性，用于设置图片的填充效果。
* [display.on('foldDisplayModeChange')](../harmonyos-references/js-apis-display.md#displayonfolddisplaymodechange10)监听设备屏幕显示模式的变化，如果要监听设备物理折叠状态的变化，需要使用[display.on('foldStatusChange')](../harmonyos-references/js-apis-display.md#displayonfoldstatuschange10)接口。
* [on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)可监听窗口尺寸的变化，当窗口尺寸变化时，应用可通过改变自身的布局以适配不同的窗口尺寸。

## 问题定位

1. 排查图片中设置objectFit属性的填充方式是否按照图片宽高比进行放大缩小。如设置为ImageFit.Fill会导致图片不保持宽高比进行放大缩小，导致变形。
2. 排查代码中是否使用display.on('foldDisplayModeChange')监听折叠状态变化，或者是否使用on('windowSizeChange')监听屏幕尺寸变化，来动态调整布局。

## 分析结论

1. Image组件的objectFit属性设置不合理。
2. 应用未适配折叠屏展开态，来动态调整布局。

## 修改建议

将图片组件的objectFit属性设置为能够始终保持图片宽高比的Contain或者Cover属性。或者使用display.on('foldDisplayModeChange')监听当前屏幕显示模式是折叠态还是展开态，动态修改整体布局。核心示例代码如下：

```ts
import { Callback } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State imgWidth: number = 100;
  @State imgHeight: number = 100;

  aboutToAppear() {
    let callback: Callback<display.FoldDisplayMode> = (data: display.FoldDisplayMode) => {
      if (data === 1) {
        // 监听到屏幕属性变为展开态显示时，动态修改图片尺寸
        this.imgWidth = 200;
        this.imgHeight = 200;
      } else if (data === 2) {
        // 监听到屏幕属性变为折叠态显示时，还原图片尺寸
        this.imgWidth = 100;
        this.imgHeight = 100;
      }
    };
    display.on('foldDisplayModeChange', callback);
  };

  build() {
    Column() {
      Image($r('app.media.example')) // 图片实际开发中替换为实际资源
        .width(this.imgWidth)
        .height(this.imgHeight)// 修改宽高或者修改objectFit属性
        .objectFit(ImageFit.Cover);
    }
    .height('100%')
    .width('100%');
  }
}
```
