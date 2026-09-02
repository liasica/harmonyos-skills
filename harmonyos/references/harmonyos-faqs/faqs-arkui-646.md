---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-646
title: 如何为RichEditor中插入的图片绑定缩放手势
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何为RichEditor中插入的图片绑定缩放手势
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5d4359c220062b68d029146cdf08f5d0bbbc6f9f994ff50f43ee072ba02dfa43
---

## 问题现象

RichEditor是支持图文混排和文本交互式编辑的组件。在RichEditor中插入图片，如何为插入的图片绑定缩放手势？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/WoOL9OsZRzmbhdDVU0vaRQ/zh-cn_image_0000002658913727.gif "点击放大")

## 背景知识

* RichEditor组件提供了[addBuilderSpan](../harmonyos-references/ts-basic-components-richeditor.md#addbuilderspan11)接口用于添加用户自定义布局Span，支持绑定手势事件。
* [PinchGesture](../harmonyos-references/ts-basic-gestures-pinchgesture.md)方法用于触发捏合手势，最少需要2指，最多5指，最小识别距离为5vp。
* [addBuilderSpan](../harmonyos-references/ts-basic-components-richeditor.md#addbuilderspan11)在RichEditor中添加用户自定义布局（BuilderSpan）。

## 解决方案

通过添加用户自定义布局Span绑定手势实现缩放，具体思路如下：

1. 实现PinchGestureExample子组件，Image添加放大缩放手势。
2. 使用addBuilderSpan自定义布局，将PinchGestureExample添加到addBuilderSpan方法中。

   ```ts
   @Component
   struct PinchGestureExample {
     @State scaleValue: number = 1;
     @State pinchValue: number = 1;
     @State pinchX: number = 0;
     @State pinchY: number = 0;

     build() {
       Stack({ alignContent: Alignment.TopStart }) {
         Image($r('app.media.startIcon'))
           .height('100%')
           .width('100%')
           .objectFit(ImageFit.Contain)
           .scale({ x: this.scaleValue, y: this.scaleValue, z: 1 })
             // 2指捏合触发该手势事件
           .gesture(
             PinchGesture({ fingers: 2 })
               .onActionStart(() => {
                 console.info('Pinch start');
               })
               .onActionUpdate((event: GestureEvent) => {
                 if (event) {
                   this.scaleValue = this.pinchValue * event.scale;
                   this.pinchX = event.pinchCenterX;
                   this.pinchY = event.pinchCenterY;
                 }
               })
               .onActionEnd(() => {
                 this.pinchValue = this.scaleValue;
                 console.info('Pinch end');
               })
           );
       }.width('100%');
     }
   }

   @Entry
   @Component
   struct PinchGestureIndex {
     controller: RichEditorController = new RichEditorController();
     option: RichEditorOptions = { controller: this.controller };
     private myOffset: number | undefined = undefined;
     private myBuilder: CustomBuilder = undefined;

     @Builder
     placeholderBuilder() {
       Row({ space: 2 }) {
         PinchGestureExample();
       }.width(200).height(200).padding(5);
     }

     build() {
       Column() {
         Column() {
           RichEditor(this.option)
             .onReady(() => {
             })
             .borderWidth(1)
             .borderColor('#0A59F7')
             .width('100%')
             .height('30%');
           Button('add span')
             .onClick(() => {
               this.myBuilder = () => {
                 this.placeholderBuilder();
               };
               let num = this.controller.addBuilderSpan(this.myBuilder, { offset: this.myOffset });
               console.info(`addBuilderSpan return ${num}`);
             })
             .margin(16);
         }
         .borderWidth(1)
         .borderColor('#0A59F7')
         .width('100%')
         .height('70%');
       }
       .padding(16);
     }
   }
   ```
