---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-790
title: 如何实现屏幕像素(px)和毫米(mm)的互相转换以及应用场景
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现屏幕像素(px)和毫米(mm)的互相转换以及应用场景
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a56e4986f24aee8935b1d31a201696ccc54903b5cc29f9bcf48a1f29147dd067
---

## 问题现象

在ArkTS中，如何实现屏幕像素(px)和毫米(mm)的互相转换以及应用场景？比如在线测量工具尺子如何实现？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/5ETgcQuKRNeMNAGg_OzfDQ/zh-cn_image_0000002658796999.png "点击放大")

## 背景知识

* [@ohos.display](../harmonyos-references/js-apis-display.md)屏幕属性提供管理显示设备的一些基础能力，包括获取默认显示设备的信息，获取所有显示设备的信息以及监听显示设备的插拔行为。
* DPI（Dots Per Inch，每英寸点数）是一个量度单位，表示在每英寸长度上可以打印或显示的点数，这些点可以是墨点、像素或其他形式的显示元素。

## 解决方案

在ArkTS中实现屏幕像素(px)到毫米(mm)的转换，需要结合设备DPI参数进行计算，以下是具体实现方案：

1. **核心转换公式。**
   * 基础换算原理。

     像素与毫米的转换需依赖DPI（每英寸像素数）参数，计算公式为：

     毫米值=(像素值×25.4) / DPI，其中25.4为1英寸对应的毫米数。
   * 设备DPI获取。

     通过[display.getDefaultDisplaySync()](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)获取屏幕参数[display](../harmonyos-references/js-apis-display.md#display)。
2. **完整转换函数实现。**

   通过转换公式计算，毫米值=(像素值×25.4) / DPI。示例代码如下：

   ```ts
   // mm转px函数
   function mmToPx(mmValue: number, isYaxis: boolean) {
     let displayInfo = display.getDefaultDisplaySync();
     if (isYaxis) {
       return (mmValue / 25.4) * displayInfo.yDPI; // 应用标准公式
     } else {
       return (mmValue / 25.4) * displayInfo.xDPI; // 应用标准公式
     }
   }
   ```

   实际应用场景：在线测量工具尺子，完整示例代码如下：

   ```ts
   import { display, window } from '@kit.ArkUI';
   import { common } from '@kit.AbilityKit';

   // 直尺线类
   class RulerLineInfo {
     index: number;
     height: number;
     mmPx: number; // 1毫米对应的像素值
     textWidth: number; // 刻度文字宽度
     textHeight: number; // 刻度文字高度

     constructor(index: number, height: number, mmPx: number) {
       this.index = index;
       this.height = height;
       this.mmPx = mmPx;
       this.textWidth = mmPx * 2 * (((index / 10) > 9 ? 2 : 1));
       this.textHeight = mmPx * 4;
     }

     showNumber(): string {
       return this.index % 10 === 0 ? `${Math.floor(this.index / 10)}` : '';
     }
   }

   // mm转px函数
   function mmToPx(mmValue: number, isYaxis: boolean) {
     let displayInfo = display.getDefaultDisplaySync();
     if (isYaxis) {
       return (mmValue / 25.4) * displayInfo.yDPI; // 应用标准公式
     } else {
       return (mmValue / 25.4) * displayInfo.xDPI; // 应用标准公式
     }
   }

   @Entry
   @Component
   struct RulerComponent {
     @State rulerLines: RulerLineInfo[] = [];

     aboutToAppear(): void {
       let mmPx = mmToPx(1, true);
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       window.getLastWindow(context).then((windowClass) => {
         windowClass.setPreferredOrientation(window.Orientation.LANDSCAPE);
       });

       // 初始化直尺线类
       for (let i = 0; i <= 10 * 10; i++) {
         let lineHeight: number = (i % 10 === 0) ? 90 : (i % 5 === 0) ? 60 : 45;
         this.rulerLines.push(new RulerLineInfo(i, lineHeight, mmPx));
       }
     }

     build() {
       Column() {
         Row() {
           ForEach(this.rulerLines, (line: RulerLineInfo, index: number) => {
             // 生成直线
             Line()
               .width(0.5)
               .height(`${line.height}px`)
               .backgroundColor(Color.Black)
               .stroke(Color.Black)
               .position({ x: `${line.mmPx * index}px`, y: 0 })
             // 生成数字
             Text(line.showNumber())
               .fontColor(Color.Black)
               .fontSize(18)
               .width(`${line.textWidth}px`)
               .height(`${line.textHeight}px`)
               .textAlign(TextAlign.Center)
               .position({
                 x: `${line.mmPx * index - line.textWidth / 2}px`,
                 y: `${line.height}px`
               })
           });
         }
         .width('100%')
         .height('30%')
         .margin({ left: 150 })
       }
       .height('100%')
       .width('100%')
       .justifyContent(FlexAlign.Center)
     }
   }
   ```
