---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pen-image-feature-picker
title: 接入全局取色
breadcrumb: 指南 > 系统 > 硬件 > Pen Kit（手写笔服务） > 手写功能开发 > 接入全局取色
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:09+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:2a6c7422816b50be3766cc5b2041733283e632cc114b91a0a0bee01aba5e06b4
---

接入全局取色功能，用户可以使用手指或者手写笔操作取色器在屏幕上移动，在目标位置抬起手指/抬起手写笔，会生成该位置色值对应的图像信息。

## 场景介绍

在应用中拉起全局取色，效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/sQhD79rFT9-lS-th0d-fYw/zh-cn_image_0000002736433561.png)

支持获取当前屏幕上选中位置的色值和色域空间。

## 限制与约束

* 全局取色能力支持设备：Tablet、PC/2in1，并且从5.1.1(19)版本开始，新增支持设备：Phone。
* 设备不支持连接手写笔的话，无法使用全局取色能力。

## 接口说明

| 类名 | 接口名 | 说明 |
| --- | --- | --- |
| [imageFeaturePicker](../harmonyos-references/pen-imagefeaturepicker.md) | [pickForResult](../harmonyos-references/pen-imagefeaturepicker.md#pickforresult)(x?:number, y?:number):Promise<[PickedColorInfo](../harmonyos-references/pen-imagefeaturepicker.md#pickedcolorinfo)> | 启动取色器。此API用于启动取色器，在取色器移动时不显示色值。该接口要求设备支持手写笔功能，若设备不支持手写笔，则无法启动取色器。 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { imageFeaturePicker } from '@kit.Penkit';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct Index {
     @State message: string = 'Hello World';

     build() {
       Stack({ alignContent: Alignment.Center }) {
         Column() {
           Row() {
             Button() {
               Text('Call GlobalColorPicker from ets side')
                 .fontSize(18)
                 .fontWeight(FontWeight.Normal)
             }
             .width('50%')
             .height('60vp')
             .align(Alignment.Center)
             .onClick((event) => {
               // 此处的 displayX 和 displayY 为触摸事件触发时屏幕上的坐标位置
               imageFeaturePicker.pickForResult(event.displayX, event.displayY)
                 .then((colorInfo: imageFeaturePicker.PickedColorInfo) => {
                   if (colorInfo) {
                     console.info('colorInfo=' + JSON.stringify(colorInfo));
                   }
                 }).catch((err: BusinessError) => {
                 console.error(`pickForResult failed. Code is ${err.code}, message is ${err.message}`);
               })
             })
           }
         }
         .align(Alignment.Center)
       }
       .width('100%')
       .height('100%')
     }
   }
   ```
