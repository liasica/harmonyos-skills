---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1453
title: 如何获取组件在屏幕中显示的比例
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何获取组件在屏幕中显示的比例
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:adf8c3f5b4117f126150a8da95db07478537a98e49f811e93f3f1529d182a1fd
---

## 问题现象

检查组件在屏幕中是否被遮挡住显示不全，如何获取组件在屏幕中的显示比例？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/_lTbABIdS221zqZoSS6Oxg/zh-cn_image_0000002658843533.png "点击放大")

## 背景知识

* [display.getAllDisplays](../harmonyos-references/js-apis-display.md#displaygetalldisplays9)是获取屏幕信息，返回的[Display](../harmonyos-references/js-apis-display.md#display)对象中包含了屏幕的宽度和高度，单位为px。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)是组件区域变化时触发该回调。返回的Area对象中包含目标元素的宽度和高度，单位vp。
* [vp2px](../harmonyos-references/arkts-apis-uicontext-uicontext.md#vp2px12)可以将vp单位的数值转换为以px为单位的数值。

## 解决方案

使用display.getAllDisplays获取到屏幕的宽高，再使用onAreaChange获取组件宽高，最后通过计算获得组件在屏幕中的显示比例。

代码示例如下：

```ts
import { display, UIContext } from '@kit.ArkUI';

@Entry
@Component
struct AreaExample {
  @State value: string = '举头望明月，低头思故乡。';
  @State screenWidth: number = 0;
  @State screenHeight: number = 0;
  @State Ratio: number = 0;
  uiContext: UIContext = new UIContext();

  aboutToAppear() {
    display.getAllDisplays((err, data) => {
      this.screenWidth = data[0].width;
      this.screenHeight = data[0].height;
    });
  }

  build() {
    Column() {
      Text(this.value)
        .padding(10)
        .backgroundColor('#ffd6d6d6')
        .fontSize(20)
        .onClick(() => {
          this.value = `${this.value}举头望明月，低头思故乡。`;
        })
        .onAreaChange((oldValue: Area, newValue: Area) => {
          let width = newValue.width as number;
          let height = newValue.height as number;
          this.Ratio =
            (this.uiContext.vp2px(width) * this.uiContext.vp2px(height)) / (this.screenWidth * this.screenHeight);
        });
      Text(`组件在屏幕中显示的比例：${'\n'} ${this.Ratio}`).margin({ right: 30, left: 30 });
    }
    .width('100%').height('100%');
  }
}
```
