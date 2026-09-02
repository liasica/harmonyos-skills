---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-grid-element-drag-exchange
title: Grid网格元素拖拽
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 列表与网格 > Grid网格元素拖拽
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:17+08:00
doc_updated_at: 2026-08-11
content_hash: sha256:c496cc23fe6fae85094c2997270e91fffe4684f5e2212c1874debda86ddb5654
---

## 概述

Grid网格元素拖拽交换功能在应用中经常会被使用，如当编辑九宫格图片需要拖拽图片改变排序时，就会使用到该功能。当网格中图片进行拖拽交换时，元素排列会跟随图片拖拽的位置而发生变化，并且会有对应的动画效果，以达到良好的用户体验。

Grid网格布局一般由[Grid](../harmonyos-references/ts-container-grid.md)容器组件和子组件[GridItem](../harmonyos-references/ts-container-griditem.md)构建组成，Grid用于设置网格布局相关参数，GridItem定义子组件相关特征。网格布局中含有网格元素，当给Grid容器组件设置[editMode](../harmonyos-references/ts-container-grid.md#editmode8)属性为true时，可开启Grid组件的编辑模式。首先，开启编辑模式。然后，给[GridItem](../harmonyos-references/ts-container-griditem.md)组件绑定[长按](../harmonyos-references/ts-basic-gestures-longpressgesture.md)、[拖拽](../harmonyos-references/ts-basic-gestures-pangesture.md)等手势。最后，需要添加动画属性[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)，并设置相应的动画效果。最终，呈现出网格元素拖拽交换的动效过程，如下示意图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/V4zHodG1R9qdbWxglHaVEQ/zh-cn_image_0000002706673578.gif)

## 实现原理

### 关键技术

Grid网格元素拖拽交换功能实现是通过[Grid](../harmonyos-references/ts-container-grid.md)容器组件、[组合手势](../harmonyos-references/ts-combined-gestures.md)、动画属性[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)结合来实现的。

* Grid组件可以构建网格元素布局。
* 组合手势可以实现元素拖拽交换的效果。
* 显式动画可以给元素拖拽交换的过程中，添加动画效果。

**说明** 

Grid组件当前支持GridItem拖拽动画，通过给Grid容器组件设置[supportAnimation](../harmonyos-references/ts-container-grid.md#supportanimation8)为true，即可开启动画效果。但仅支持在滚动模式下（设置[rowsTemplate](../harmonyos-references/ts-container-grid.md#rowstemplate)、[columnsTemplate](../harmonyos-references/ts-container-grid.md#columnstemplate)其中一个）支持动画。且仅在大小规则的Grid中支持拖拽动画，跨行或跨列场景不支持。因此，在跨行或跨列场景下，需要通过自定义Grid布局、自定义手势和显式动画来实现拖拽交换的效果。

### 开发流程

在需要拖拽交换的场景中：

* 实现Grid布局，启动[editMode](../harmonyos-references/ts-container-grid.md#editmode8)编辑模式，进入编辑模式可以拖拽Grid组件内部[GridItem](../harmonyos-references/ts-container-griditem.md)。
* 给网格元素[GridItem](../harmonyos-references/ts-container-griditem.md)绑定相关手势，实现可拖拽操作。
* 使用显式动画[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)，实现[GridItem](../harmonyos-references/ts-container-griditem.md)拖拽过程中的动画效果。

## 相同大小网格元素，长按拖拽

### 场景描述

在编辑九宫格等多图的场景中，长按图片（网格元素）可以拖拽交换排序，拖拽图片的过程中，旁边的图片也会即时移动，以产生新的宫格排布。

示意效果图如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/zqoq1kpGSRyv3p5lST3qEw/zh-cn_image_0000002736432669.gif)

### 开发步骤

1. Grid布局及相同大小的GridItem界面开发。其中，[scrollBar](../harmonyos-references/ts-container-grid.md#scrollbar)可设置滚动条状态，值为BarState.Off时，表示不显示滚动条；[columnsTemplate](../harmonyos-references/ts-container-grid.md#columnstemplate)可设置当前网格布局列的数量、固定列宽或最小列宽值；[columnsGap](../harmonyos-references/ts-container-grid.md#columnsgap)可设置列与列的间距；[rowsGap](../harmonyos-references/ts-container-grid.md#rowsgap)可设置行与行的间距。

   ```ts
   Grid() {
     ForEach(this.numbers, (item: number) => {
       GridItem() {
         Image($r(`app.media.image${item}`))
           .width('100%')
           .height(this.curBp === 'md' ? 131 : 105)
           .draggable(false)
           .animation({ curve: Curve.Sharp, duration: 300 })
       }
     }, (item: number) => item.toString())
   }
   .width(this.curBp === 'md' ? '66%' : '100%')
   .scrollBar(BarState.Off)
   .columnsTemplate('1fr 1fr 1fr')
   .columnsGap(this.curBp === 'md' ? 6 : 4)
   .rowsGap(this.curBp === 'md' ? 6 : 4)
   .height(this.curBp === 'md' ? 406 : 323)
   ```
2. 给Grid组件设置[editMode](../harmonyos-references/ts-container-grid.md#editmode8)为true，即Grid进入编辑模式，进入编辑模式可以拖拽Grid组件内部[GridItem](../harmonyos-references/ts-container-griditem.md)。设置[supportAnimation](../harmonyos-references/ts-container-grid.md#supportanimation8)为true，即Grid拖拽元素时支持动画。

   ```ts
   .editMode(true)
   .supportAnimation(true)
   ```
3. 定义拖拽过程中的数组交换逻辑。

   ```ts
   changeIndex(index1: number, index2: number) {
     let tmp = this.numbers.splice(index1, 1);
     this.numbers.splice(index2, 0, tmp[0])
   }
   ```
4. 给Grid组件绑定[onItemDragStart](../harmonyos-references/ts-container-grid.md#onitemdragstart8)和[onItemDrop](../harmonyos-references/ts-container-grid.md#onitemdrop8)事件，在[onItemDragStart](../harmonyos-references/ts-container-grid.md#onitemdragstart8)回调中设置拖拽过程中显示的图片，并在[onItemDrop](../harmonyos-references/ts-container-grid.md#onitemdrop8)中完成交换数组位置的逻辑。

   [onItemDragStart](../harmonyos-references/ts-container-grid.md#onitemdragstart8)回调在开始拖拽网格元素时触发，[onItemDrop](../harmonyos-references/ts-container-grid.md#onitemdrop8)回调当在网格元素内停止拖拽时触发。

   ```ts
   .onItemDragStart((_, itemIndex: number) => {
     this.imageNum = this.numbers[itemIndex];
     return this.pixelMapBuilder();
   })
   .onItemDrop((_, itemIndex: number, insertIndex: number, isSuccess: boolean) => {
     if (!isSuccess || insertIndex >= this.numbers.length) {
       return;
     }
     this.changeIndex(itemIndex, insertIndex);
   })
   ```

## 不同大小网格元素，长按拖拽

### 场景描述

在一些展示设备的场景中，会有大小不同的网格元素。当用户想改变设备排序时，可以长按设备图片（网格元素）拖拽交换排序，拖拽的过程中，也会改变排列顺序，以产生新的宫格排布。

示意效果图如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/qrSEkQYCQ6ieW2MDfGB28w/zh-cn_image_0000002706833514.gif)

**说明** 

当前方案仅适用于页面包含一个较大网格元素的布局。

### 开发步骤

1. Grid布局及不同大小的GridItem界面开发。

   ```ts
   Grid() {
     ForEach(this.numbers, (item: number) => {
       GridItem() {
         Stack({ alignContent: Alignment.TopEnd }) {
           Image(this.changeImage(item))
             .width('100%')
             .borderRadius(16)
             .objectFit(this.curBp === 'md' ? ImageFit.Fill : ImageFit.Cover)
             .draggable(false)
             .animation({ curve: Curve.Sharp, duration: 300 })
         }
       }
       .rowStart(0)
       .rowEnd(this.getRowEnd(item))
       .scale({ x: this.scaleItem === item ? 1.02 : 1, y: this.scaleItem === item ? 1.02 : 1 })
       .zIndex(this.dragItem === item ? 1 : 0)
       .translate(this.dragItem === item ? { x: this.offsetX, y: this.offsetY } : { x: 0, y: 0 })
       .hitTestBehavior(this.isDraggable(this.numbers.indexOf(item)) ? HitTestMode.Default : HitTestMode.None)
       // ...
     }, (item: number) => item.toString())
   }
   .width('100%')
   .height('100%')
   .editMode(true)
   .scrollBar(BarState.Off)
   .columnsTemplate('1fr 1fr')
   .supportAnimation(true)
   .columnsGap(12)
   .rowsGap(12)
   .enableScrollInteraction(true)
   ```
2. 定义网格元素移动过程中的相关计算函数，其中itemMove()方法是实现元素交换重新排序的方法。

   ```ts
   itemMove(index: number, newIndex: number): void {
     if (!this.isDraggable(newIndex)) {
       return;
     }
     let tmp = this.numbers.splice(index, 1);
     this.numbers.splice(newIndex, 0, tmp[0]);
     this.bigItemIndex = this.numbers.findIndex((item) => item === 0);
   }

   isInLeft(index: number) {
     if (index === this.bigItemIndex) {
       return index % 2 == 0;
     }
     if (this.bigItemIndex % 2 === 0) {
       if (index - this.bigItemIndex === 2 || index - this.bigItemIndex === 1) {
         return false;
       }
     } else {
       if (index - this.bigItemIndex === 1) {
         return false;
       }
     }
     if (index > this.bigItemIndex) {
       return index % 2 == 1;
     } else {
       return index % 2 == 0;
     }
   }

   down(index: number): void {
     if ([this.numbers.length - 1, this.numbers.length - 2].includes(index)) {
       return;
     }
     if (this.bigItemIndex - index === 1) {
       return;
     }
     if ([14, 15].includes(this.bigItemIndex) && this.bigItemIndex === index) {
       return;
     }
     this.offsetY -= this.FIX_VP_Y;
     this.dragRefOffSetY += this.FIX_VP_Y;
     if (index - 1 === this.bigItemIndex) {
       this.itemMove(index, index + 1);
     } else {
       this.itemMove(index, index + 2);
     }
   }

   up(index: number): void {
     if (!this.isDraggable(index - 2)) {
       return;
     }
     if (index - this.bigItemIndex === 3) {
       return;
     }
     this.offsetY += this.FIX_VP_Y;
     this.dragRefOffSetY -= this.FIX_VP_Y;
     if (this.bigItemIndex === index) {
       this.itemMove(index, index - 2);
     } else {
       if (index - 2 === this.bigItemIndex) {
         this.itemMove(index, index - 1);
       } else {
         this.itemMove(index, index - 2);
       }
     }
   }

   left(index: number): void {
     if (this.bigItemIndex % 2 === 0) {
       if (index - this.bigItemIndex === 2) {
         return;
       }
     }
     if (this.isInLeft(index)) {
       return;
     }
     if (!this.isDraggable(index - 1)) {
       return;
     }
     this.offsetX += this.FIX_VP_X;
     this.dragRefOffSetX -= this.FIX_VP_X;
     this.itemMove(index, index - 1)
   }

   right(index: number): void {
     if (this.bigItemIndex % 2 === 1) {
       if (index - this.bigItemIndex === 1) {
         return;
       }
     }
     if (!this.isInLeft(index)) {
       return;
     }
     if (!this.isDraggable(index + 1)) {
       return;
     }
     this.offsetX -= this.FIX_VP_X;
     this.dragRefOffSetX += this.FIX_VP_X;
     this.itemMove(index, index + 1)
   }

   isDraggable(index: number): boolean {
     return index >= 0;
   }
   ```
3. GridItem绑定组合手势：长按，拖拽。并在手势的回调函数中设置显式动画。

   ```ts
   .gesture(
     GestureGroup(GestureMode.Sequence,
       LongPressGesture({ repeat: true })
         .onAction(() => {
           this.getUIContext().animateTo({ curve: Curve.Friction, duration: 300 }, () => {
             this.scaleItem = item;
           })
         })
         .onActionEnd(() => {
           this.getUIContext().animateTo({ curve: Curve.Friction, duration: 300 }, () => {
             this.scaleItem = -1;
           })
         }),
       PanGesture({ fingers: 1, direction: null, distance: 0 })
         .onActionStart(() => {
           this.dragItem = item;
           this.dragRefOffSetX = 0;
           this.dragRefOffSetY = 0;
         })
         .onActionUpdate((event: GestureEvent) => {
           this.offsetX = event.offsetX - this.dragRefOffSetX;
           this.offsetY = event.offsetY - this.dragRefOffSetY;
           this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
             let index = this.numbers.indexOf(this.dragItem);
             if (this.offsetY >= this.FIX_VP_Y / 2 && (this.offsetX <= 44 && this.offsetX >= -44)) {
               this.down(index);
             } else if (this.offsetY <= -this.FIX_VP_Y / 2 && (this.offsetX <= 44 && this.offsetX >= -44)) {
               this.up(index);
             } else if (this.offsetX >= this.FIX_VP_X / 2 && (this.offsetY <= 50 && this.offsetY >= -50)) {
               this.right(index);
             } else if (this.offsetX <= -this.FIX_VP_X / 2 && (this.offsetY <= 50 && this.offsetY >= -50)) {
               this.left(index);
             }
           })
         })
         .onActionEnd(() => {
           this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
             this.dragItem = -1;
           })
           this.getUIContext().animateTo({ curve: curves.interpolatingSpring(14, 1, 170, 17), delay: 150 }, () => {
             this.scaleItem = -1;
           })
         })
     )
       .onCancel(() => {
         this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
           this.dragItem = -1;
         })
         this.getUIContext().animateTo({ curve: curves.interpolatingSpring(14, 1, 170, 17), delay: 150 }, () => {
           this.scaleItem = -1;
         })
       })
   )
   ```

## 两个Grid之间网格元素交换

当场景涉及两个Grid之间的网格元素交换时，可使用[GridObjectSortComponent](../harmonyos-references/ohos-arkui-advanced-gridobjectsortcomponent.md)组件来实现。可以点击添加或者移除按钮，对网格元素进行交换。详细实现步骤请参见：[示例](../harmonyos-references/ohos-arkui-advanced-gridobjectsortcomponent.md#示例)。开发者也可以在[GridObjectSortComponent](../harmonyos-references/ohos-arkui-advanced-gridobjectsortcomponent.md)组件的[源码](https://gitcode.com/openharmony/arkui_ace_engine/blob/master/advanced_ui_component/gridobjectsortcomponent/source/GridObjectSortComponent.ets)基础上进行相应修改，实现更加丰富的功能。

## 网格元素直接拖拽，不需长按

### 场景描述

在不需要长按拖拽的场景下，开发者可以将元素设置成直接拖拽，无需长按，即可完成元素的拖拽交换。

示意效果图如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/5q3RIm8xS3mvEjM7-gW0aA/zh-cn_image_0000002736312623.gif)

### 开发步骤

1. 使用Grid布局及GridItem界面开发。

   ```ts
   Grid() {
     ForEach(this.numbers, (item: number) => {
       GridItem() {
         Column() {
           Image($r(`app.media.space${item}`))
             .width(44)
             .height(44)
             .draggable(false)
           Image($r('app.media.space_bottom'))
             .width(16)
             .height(16)
             .draggable(false)
         }
         .width('100%')
         .height(73)
         .justifyContent(FlexAlign.Center)
         .borderRadius(10)
         .backgroundColor('#F1F3F5')
         .animation({ curve: Curve.Sharp, duration: 300 })
       }
       .scale({ x: this.scaleItem === item ? 1.05 : 1, y: this.scaleItem === item ? 1.05 : 1 })
       .zIndex(this.dragItem === item ? 1 : 0)
       .translate(this.dragItem === item ? { x: this.offsetX, y: this.offsetY } : { x: 0, y: 0 })
       // ...
     }, (item: number) => item.toString())
   }
   .width('100%')
   .editMode(true)
   .scrollBar(BarState.Off)
   .columnsTemplate(this.curBp === 'md' ? '1fr 1fr 1fr 1fr 1fr' : '1fr 1fr 1fr 1fr')
   .columnsGap(12)
   .rowsGap(12)
   .margin({ top: 5 })
   ```
2. 定义网格元素移动过程中的相关计算函数。

   ```ts
   itemMove(index: number, newIndex: number): void {
     if (!this.isDraggable(newIndex)) {
       return;
     }
     let tmp = this.numbers.splice(index, 1);
     this.numbers.splice(newIndex, 0, tmp[0]);
   }

   down(index: number): void {
     if (!this.isDraggable(index + 5)) {
       return;
     }
     this.offsetY -= this.FIX_VP_Y;
     this.dragRefOffSetY += this.FIX_VP_Y;
     this.itemMove(index, index + 5)
   }

   up(index: number): void {
     if (this.curBp === 'md') {
       if (!this.isDraggable(index - 5)) {
         return;
       }
       this.offsetY += this.FIX_VP_Y;
       this.dragRefOffSetY -= this.FIX_VP_Y;
       this.itemMove(index, index - 5)
     } else {
       if (!this.isDraggable(index - 4)) {
         return;
       }
       this.offsetY += this.FIX_VP_Y;
       this.dragRefOffSetY -= this.FIX_VP_Y;
       this.itemMove(index, index - 4)
     }
   }

   left(index: number): void {
     if (!this.isDraggable(index - 1)) {
       return;
     }
     this.offsetX += this.FIX_VP_X;
     this.dragRefOffSetX -= this.FIX_VP_X;
     this.itemMove(index, index - 1)
   }

   right(index: number): void {
     if (!this.isDraggable(index + 1)) {
       return;
     }
     this.offsetX -= this.FIX_VP_X;
     this.dragRefOffSetX += this.FIX_VP_X;
     this.itemMove(index, index + 1)
   }

   lowerRight(index: number): void {
     if (!this.isDraggable(index + 3)) {
       return;
     }
     this.offsetX -= this.FIX_VP_X;
     this.dragRefOffSetX += this.FIX_VP_X;
     this.offsetY -= this.FIX_VP_Y;
     this.dragRefOffSetY += this.FIX_VP_Y;
     this.itemMove(index, index + 3);
   }

   upperRight(index: number): void {
     if (!this.isDraggable(index - 3)) {
       return;
     }
     this.offsetX -= this.FIX_VP_X;
     this.dragRefOffSetX += this.FIX_VP_X;
     this.offsetY += this.FIX_VP_Y;
     this.dragRefOffSetY -= this.FIX_VP_Y;
     this.itemMove(index, index - 3);
   }

   lowerLeft(index: number): void {
     if (!this.isDraggable(index + 3)) {
       return;
     }
     this.offsetX += this.FIX_VP_X;
     this.dragRefOffSetX -= this.FIX_VP_X;
     this.offsetY -= this.FIX_VP_Y;
     this.dragRefOffSetY += this.FIX_VP_Y;
     this.itemMove(index, index + 3);
   }

   upperLeft(index: number): void {
     if (!this.isDraggable(index - 3)) {
       return;
     }
     this.offsetX += this.FIX_VP_X;
     this.dragRefOffSetX -= this.FIX_VP_X;
     this.offsetY += this.FIX_VP_Y;
     this.dragRefOffSetY -= this.FIX_VP_Y;
     this.itemMove(index, index - 3);
   }

   isDraggable(index: number): boolean {
     return index >= 0;
   }
   ```
3. GridItem绑定拖拽手势，并在手势的回调函数中设置显式动画。

   ```ts
   .gesture(
     PanGesture({ fingers: 1, direction: null, distance: 0 })
       .onActionStart(() => {
         this.dragItem = item;
         this.dragRefOffSetX = 0;
         this.dragRefOffSetY = 0;
       })
       .onActionUpdate((event: GestureEvent) => {
         this.offsetX = event.offsetX - this.dragRefOffSetX;
         this.offsetY = event.offsetY - this.dragRefOffSetY;
         this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
           let index = this.numbers.indexOf(this.dragItem);
           if (this.curBp === 'md') {
             if (this.offsetX >= this.FIX_VP_X / 2 && (this.offsetY <= 50 && this.offsetY >= -50) &&
               ![4].includes(index)) {
               this.right(index);
             } else if (this.offsetX <= -this.FIX_VP_X / 2 && (this.offsetY <= 50 && this.offsetY >= -50)) {
               this.left(index);
             }
           } else {
             if (this.offsetY >= this.FIX_VP_Y / 2 && (this.offsetX <= 44 && this.offsetX >= -44) &&
               ![1, 2, 3, 4].includes(index)) {
               this.down(index);
             } else if (this.offsetY <= -this.FIX_VP_Y / 2 && (this.offsetX <= 44 && this.offsetX >= -44)) {
               this.up(index);
             } else if (this.offsetX >= this.FIX_VP_X / 2 && (this.offsetY <= 50 && this.offsetY >= -50) &&
               ![3, 4].includes(index)) {
               this.right(index);
             } else if (this.offsetX <= -this.FIX_VP_Y / 2 && (this.offsetY <= 50 && this.offsetY >= -50) &&
               ![4].includes(index)) {
               this.left(index);
             } else if (this.offsetX >= this.FIX_VP_X / 2 && this.offsetY >= this.FIX_VP_Y / 2) {
               this.lowerRight(index);
             } else if (this.offsetX >= this.FIX_VP_X / 2 && this.offsetY <= -this.FIX_VP_Y / 2) {
               this.upperRight(index);
             } else if (this.offsetX <= -this.FIX_VP_X / 2 && this.offsetY >= this.FIX_VP_Y / 2) {
               this.lowerLeft(index);
             } else if (this.offsetX <= -this.FIX_VP_X / 2 && this.offsetY <= -this.FIX_VP_Y / 2) {
               this.upperLeft(index);
             }
           }
         })
       })
       .onActionEnd(() => {
         this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
           this.dragItem = -1;
         })
         this.getUIContext().animateTo({ curve: curves.interpolatingSpring(14, 1, 170, 17), delay: 150 }, () => {
           this.scaleItem = -1;
         })
       })
   )
   ```

## 网格元素长按后，显示抖动动画

### 场景描述

在设备列表页面时，如果想要移除设备，在选中设备并长按后，可对网格元素进行编辑。此时，设备图片会有抖动的效果。

示意效果图如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/f7yI-NDnT_-Z1AXsrCe0Kg/zh-cn_image_0000002706673580.gif)

### 开发步骤

1. 使用Grid布局及GridItem界面开发。

   ```ts
   Grid() {
     ForEach(this.numbers, (item: number) => {
       GridItem() {
         Stack({ alignContent: Alignment.TopEnd }) {
           Column() {
             Image($r(`app.media.space${item}`))
               .width(44)
               .height(44)
               .draggable(false)
             Image($r('app.media.space_bottom'))
               .width(16)
               .height(16)
               .draggable(false)
           }
           .width('100%')
           .height(73)
           .justifyContent(FlexAlign.Center)
           .borderRadius(10)
           .backgroundColor('#F1F3F5')
           .animation({ curve: Curve.Sharp, duration: 300 })
           .onClick(() => {
             return;
           })

           if (this.isEdit) {
             Image($r('app.media.close'))
               .width(20)
               .height(20)
               .objectFit(ImageFit.Contain)
               .draggable(false)
               .position({
                 x: this.isFoldAble && this.foldStatus === 2 ? 60 :
                   this.isFoldAble && this.foldStatus === 1 ? 86 : 70,
                 y: -8
               })
               .onClick(() => {
                 this.getUIContext().animateTo({ duration: 300 }, () => {
                   this.numbers = this.numbers.filter((element) => element !== item);
                 })
               })
           }
         }
       }
       .rotate({
         z: this.rotateZ,
         angle: 1,
         centerX: '50%',
         centerY: '50%'
       })
       .width('100%')
       .zIndex(this.dragItem === item ? 1 : 0)
       .translate(this.dragItem === item ? { x: this.offsetX, y: this.offsetY } : { x: 0, y: 0 })
       // ...
     }, (item: number) => item.toString())
   }
   .width('100%')
   .height('100%')
   .editMode(true)
   .clip(false)
   .scrollBar(BarState.Off)
   .columnsTemplate(this.curBp === 'md' ? '1fr 1fr 1fr 1fr 1fr' : '1fr 1fr 1fr 1fr')
   .columnsGap(12)
   .rowsGap(12)
   .margin({ top: 5 })
   ```
2. 添加抖动动画。

   ```ts
   private jumpWithSpeed(speed: number) {
     if (this.isEdit) {
       this.rotateZ = -1;
       this.getUIContext().animateTo({
         delay: 0,
         tempo: speed,
         duration: 1000,
         curve: Curve.Smooth,
         playMode: PlayMode.Normal,
         iterations: -1
       }, () => {
         this.rotateZ = 1;
       })
     } else {
       this.stopJump();
     }
   }
   ```
3. 定义stopJump()方法，执行后，能使网格元素停止抖动。

   ```ts
   private stopJump() {
     this.getUIContext().animateTo({
       delay: 0,
       tempo: 5,
       duration: 0,
       curve: Curve.Smooth,
       playMode: PlayMode.Normal,
       iterations: 1
     }, () => {
       this.rotateZ = 0;
     })
   }
   ```
4. GridItem绑定组合手势：长按、拖拽。并在手势的回调函数中设置显式动画。

   ```ts
   .gesture(
     GestureGroup(GestureMode.Sequence,
       LongPressGesture({ repeat: true })
         .onAction(() => {
           if (!this.isEdit) {
             this.isEdit = true;
             this.jumpWithSpeed(5);
           }
         }),
       PanGesture({ fingers: 1, direction: null, distance: 0 })
         .onActionStart(() => {
           this.dragItem = item;
           this.dragRefOffSetX = 0;
           this.dragRefOffSetY = 0;
         })
         .onActionUpdate((event: GestureEvent) => {
           this.offsetX = event.offsetX - this.dragRefOffSetX;
           this.offsetY = event.offsetY - this.dragRefOffSetY;
           this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
             let index = this.numbers.indexOf(this.dragItem);
             if (this.curBp === 'md') {
               if (this.offsetX >= this.FIX_VP_X / 2 && (this.offsetY <= 50 && this.offsetY >= -50) &&
                 ![4].includes(index)) {
                 this.right(index);
                 this.stopJump();
                 this.jumpWithSpeed(5);
               } else if (this.offsetX <= -this.FIX_VP_X / 2 &&
                 (this.offsetY <= 50 && this.offsetY >= -50)) {
                 this.left(index);
                 this.stopJump();
                 this.jumpWithSpeed(5);
               }
             } else {
               if (this.offsetY >= this.FIX_VP_Y / 2 && (this.offsetX <= 44 && this.offsetX >= -44) &&
               [...this.downArr].includes(index)) {
                 this.down(index);
                 this.stopJump();
                 this.jumpWithSpeed(5);
               } else if (this.offsetY <= -this.FIX_VP_Y / 2 &&
                 (this.offsetX <= 44 && this.offsetX >= -44)) {
                 this.up(index);
                 this.stopJump();
                 this.jumpWithSpeed(5);
               } else if (this.offsetX >= this.FIX_VP_X / 2 && (this.offsetY <= 50 && this.offsetY >= -50) &&
                 ![...this.rightArr].includes(index)) {
                 this.right(index);
                 this.stopJump();
                 this.jumpWithSpeed(5);
               } else if (this.offsetX <= -this.FIX_VP_Y / 2 &&
                 (this.offsetY <= 50 && this.offsetY >= -50) &&
                 ![...this.leftArr].includes(index)) {
                 this.left(index);
                 this.stopJump();
                 this.jumpWithSpeed(5);
               }
             }
           })
         })
         .onActionEnd(() => {
           this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
             this.dragItem = -1;
           })
         })
     )
   )
   ```

## 示例代码

* [实现Grid网格元素拖拽交换排序能力](https://gitcode.com/harmonyos_samples/grid-drag-sort)
