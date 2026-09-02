---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-143
title: 如何实现拖拽时列表项占位动画的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现拖拽时列表项占位动画的效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ad5d1db098e81a9f6bee872f03538d71b854f86b1a32bf3779589d3508230581
---

拖拽Grid时，列表项显示占位动画效果。实现步骤如下：

1. 在Grid组件下设置属性editMode(true)，使Grid进入编辑模式。进入编辑模式后，可以拖拽Grid组件内部的GridItem。
2. 在onItemDragStart回调中设置拖拽时显示的组件。
3. 在onItemDrop中获取拖拽起始位置和拖拽插入位置，并完成数组位置交换逻辑。

   ```ts
   @Entry
   @Component
   struct GridExample {
     @State numbers: string[] = [];
     scroller: Scroller = new Scroller();
     @State text: string = 'drag';

     @Builder
     pixelMapBuilder() {
       Column() {
         Text(this.text)
           .fontSize(16)
           .backgroundColor(0xF9CF93)
           .width(80)
           .height(80)
           .textAlign(TextAlign.Center)
       }
     }

     aboutToAppear() {
       for (let i = 1; i <= 15; i++) {
         this.numbers.push(i + '');
       }
     }

     changeIndex(index1: number, index2: number) {
       // Swap array positions
       let temp = this.numbers[index1];
       this.numbers[index1] = this.numbers[index2];
       this.numbers[index2] = temp;
     }

     build() {
       Column({ space: 5 }) {
         Grid(this.scroller) {
           ForEach(this.numbers, (day: string) => {
             GridItem() {
               Text(day)
                 .fontSize(16)
                 .backgroundColor(0xF9CF93)
                 .width(80)
                 .height(80)
                 .textAlign(TextAlign.Center)
                 .onTouch((event: TouchEvent) => {
                   if (event.type === TouchType.Up) {
                     this.text = day;
                   }
                 })
             }
           })
         }
         .columnsTemplate('1fr 1fr 1fr')
         .columnsGap(10)
         .rowsGap(10)
         .onScrollIndex((first: number) => {
           console.info(first.toString());
         })
         .width('90%')
         .backgroundColor(0xFAEEE0)
         .height(300)
         .editMode(true) // Set whether the Grid enters editing mode. When entering editing mode, you can drag and drop the GridItem inside the Grid component
         .onItemDragStart((event: ItemDragInfo, itemIndex: number) => { // When dragging the component bound to this event for the first time, a callback is triggered.
           return this.pixelMapBuilder(); //Set the image displayed during the drag and drop process.
         })
         // The component bound to this event can be used as a drag and drop release target. When the drag behavior stops within the scope of this component, a callback is triggered.
         .onItemDrop((event: ItemDragInfo, itemIndex: number, insertIndex: number, isSuccess: boolean) => {
           // Drag the starting position of itemIndex, drag the insertion position of insertIndex
           this.changeIndex(itemIndex, insertIndex)
         })
       }.width('100%').margin({ top: 5 })
     }
   }
   ```
