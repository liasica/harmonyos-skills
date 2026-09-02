---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1132
title: 拖拽List组件内的子组件时，如何解决被拖拽的子组件位置会向两边偏移的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 拖拽List组件内的子组件时，如何解决被拖拽的子组件位置会向两边偏移的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ace75e1143abc54bb93a889e928e658ce7766c46d735f57a9c0f723317d074ef
---

## 问题现象

当在List组件内拖拽交换子组件位置时，拖拽开始时，被拖拽的子组件位置会偏到左侧或右侧。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/xPsrIlVYT0q6XdXFq7v-ZQ/zh-cn_image_0000002658808791.png "点击放大")

## 背景知识

* 拖拽是移动端常见的操作，常用于编辑列表、网格中的元素顺序。ArkTS组件List，Grid等组件提供了简单的实现拖拽效果的API：[onItemDragStart](../harmonyos-references/ts-container-list.md#onitemdragstart8)。
* 可通过[组合手势GestureGroup](../harmonyos-guides/arkts-gesture-events-combined-gestures.md)和[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)，实现自定义拖拽效果。

## 解决方案

可以采用组合手势和显示动画的方式来控制子组件拖拽时的位置变化情况，实现平滑拖动效果。

1. 顺序识别组合手势。
   * 长按手势事件LongPressGesture，标记被拖拽元素。
   * 拖动手势事件PanGesture，记录被拖拽元素的位移。
2. 在元素缩放和位移过程中，使用显示动画animateTo控制动画效果。

   ```ts
   import curves from '@ohos.curves';
   import Curves from '@ohos.curves';

   @Entry
   @Component
   struct ListItemExample {
     @State private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
     @State dragItem: number = -1;
     @State scaleItem: number = -1;
     @State neighborItem: number = -1;
     @State neighborScale: number = -1;
     private dragRefOffset: number = 0;
     @State offsetY: number = 0;
     private ITEM_INTV: number = 120;

     scaleSelect(item: number): number {
       if (this.scaleItem === item) {
         return 1.05;
       } else if (this.neighborItem === item) {
         return this.neighborScale;
       } else {
         return 1;
       };
     }

     itemMove(index: number, newIndex: number): void {
       let tmp = this.arr.splice(index, 1);
       this.arr.splice(newIndex, 0, tmp[0]);
     }

     build() {
       Stack() {
         List({ space: 20, initialIndex: 0 }) {
           ForEach(this.arr, (item: number) => {
             ListItem() {
               Text(item.toString())
                 .width('100%')
                 .height(100)
                 .fontSize(16)
                 .textAlign(TextAlign.Center)
                 .borderRadius(10)
                 .backgroundColor(0xFFFFFF)
                 .shadow(this.scaleItem === item ? {
                   radius: 70,
                   color: '#15000000',
                   offsetX: 0,
                   offsetY: 0
                 } :
                   {
                     radius: 0,
                     color: '#15000000',
                     offsetX: 0,
                     offsetY: 0
                   })
                 .animation({ curve: Curve.Sharp, duration: 300 });
             }
             .margin({ left: 12, right: 12 })
             .scale({ x: this.scaleSelect(item), y: this.scaleSelect(item) })
             .zIndex(this.dragItem === item ? 1 : 0)
             .translate(this.dragItem === item ? { y: this.offsetY } : { y: 0 })
             .gesture(
               // 以下组合手势为顺序识别，当长按手势事件未正常触发时则不会触发拖动手势事件
               GestureGroup(GestureMode.Sequence,
                 LongPressGesture({ repeat: true })
                   .onAction((event?: GestureEvent) => {
                     this.getUIContext().animateTo({ curve: Curve.Friction, duration: 300 }, () => {
                       this.scaleItem = item;
                       console.info(`event: ${event}`);
                     });
                   })
                   .onActionEnd(() => {
                     this.getUIContext().animateTo({ curve: Curve.Friction, duration: 300 }, () => {
                       this.scaleItem = -1;
                     });
                   }),
                 PanGesture({ fingers: 1, direction: null, distance: 0 })
                   .onActionStart(() => {
                     this.dragItem = item;
                     this.dragRefOffset = 0;
                   })
                   .onActionUpdate((event: GestureEvent) => {
                     this.offsetY = event.offsetY - this.dragRefOffset;
                     this.neighborItem = -1;
                     let index = this.arr.indexOf(item);
                     let curveValue = Curves.initCurve(Curve.Sharp);
                     let value: number = 0;
                     // 根据位移计算相邻项的缩放
                     if (this.offsetY < 0) {
                       value = curveValue.interpolate(-this.offsetY / this.ITEM_INTV);
                       this.neighborItem = this.arr[index-1];
                       this.neighborScale = 1 - value / 20;
                       console.info(`neighborScale: ${this.neighborScale}`);
                     } else if (this.offsetY > 0) {
                       value = curveValue.interpolate(this.offsetY / this.ITEM_INTV);
                       this.neighborItem = this.arr[index+1];
                       this.neighborScale = 1 - value / 20;
                     }
                     // 根据位移交换排序
                     if (this.offsetY > this.ITEM_INTV / 2) {
                       this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
                         this.offsetY -= this.ITEM_INTV;
                         this.dragRefOffset += this.ITEM_INTV;
                         this.itemMove(index, index + 1);
                       });
                     } else if (this.offsetY < -this.ITEM_INTV / 2) {
                       this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
                         this.offsetY += this.ITEM_INTV;
                         this.dragRefOffset -= this.ITEM_INTV;
                         this.itemMove(index, index - 1);
                       });
                     }
                   })
                   .onActionEnd((event: GestureEvent) => {
                     console.info(`event: ${event}`);
                     this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
                       this.dragItem = -1;
                       this.neighborItem = -1;
                     });
                     this.getUIContext().animateTo({
                       curve: curves.interpolatingSpring(14, 1, 170, 17), delay: 150
                     }, () => {
                       this.scaleItem = -1;
                     });
                   })
               )
                 .onCancel(() => {
                   this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
                     this.dragItem = -1;
                     this.neighborItem = -1;
                   });
                   this.getUIContext().animateTo({
                     curve: curves.interpolatingSpring(14, 1, 170, 17), delay: 150
                   }, () => {
                     this.scaleItem = -1;
                   });
                 })
             );
           }, (item: number) => item.toString());
         };
       }
       .width('100%')
       .height('100%')
       .backgroundColor(0xDCDCDC)
       .padding({ top: 5 });
     }
   }
   ```
