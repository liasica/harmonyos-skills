---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1329
title: 如何实现不同分组间元素拖拽切换效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现不同分组间元素拖拽切换效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:48201340fcd7246f3498176876d55cba4bb33043cab206f91ea441c656c2c54b
---

## 问题现象

如下图所示，需求是现在有A、B两个组，A、B两组中的元素可以拖动，并且A组中的元素可以拖动到B组，B组的元素同样可以拖动到A组，请问如何实现这种多组之间相互拖拽的效果？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/wo78RaQuRt6tHihBjg1fNg/zh-cn_image_0000002628599868.png "点击放大")

## 背景知识

* 使用[Grid](../harmonyos-references/ts-container-grid.md)组件构建网格元素布局，启动[editMode](../harmonyos-references/ts-container-grid.md#editmode8)编辑模式，进入编辑模式可以拖拽Grid组件内部[GridItem](../harmonyos-references/ts-container-griditem.md)。
* [onItemDragStart](../harmonyos-references/ts-container-grid.md#onitemdragstart8)和[onItemDrop](../harmonyos-references/ts-container-grid.md#onitemdrop8)事件分别在开始拖拽网格元素时触发和停止拖拽时触发，通过事件的组合完成交换数组位置的逻辑。

## 解决方案

1. 使用Grid布局构建界面。其中，[columnsTemplate](../harmonyos-references/ts-container-grid.md#columnstemplate)可设置当前网格布局列的数量、固定列宽或最小列宽值；[columnsGap](../harmonyos-references/ts-container-grid.md#columnsgap)可设置列与列的间距；[rowsGap](../harmonyos-references/ts-container-grid.md#rowsgap)可设置行与行的间距。

   ```ts
   Grid(this.scroller) {
     GridItem() {
       Text('标题1-' + this.numbers.length)
         .fontSize(16)
         .width('100%')
         .height(30)
         .padding({ left: 10 })
         .textAlign(TextAlign.Start);
     }
     .onClick(() => {
       this.isShowGroup1 = !this.isShowGroup1;
     });

     if (this.isShowGroup1) {
       ForEach(this.numbers, (day: string) => {
         GridItem() {
           Text(day)
             .fontSize(16)
             .backgroundColor('#f1f3f5')
             .width('100%')
             .height(30)
             .textAlign(TextAlign.Center);
         };
       });
     }
     GridItem() {
       Text('标题2-' + this.numbers2.length)
         .fontSize(16)
         .width('100%')
         .height(30)
         .padding({ left: 10 })
         .textAlign(TextAlign.Start);
     }
     .onClick(() => {
       this.isShowGroup2 = !this.isShowGroup2;
     });

     if (this.isShowGroup2) {
       ForEach(this.numbers2, (day: string) => {
         GridItem() {
           Text(day)
             .fontSize(16)
             .backgroundColor('#f1f3f5')
             .width('100%')
             .height(30)
             .textAlign(TextAlign.Center);
         };
       });
     }
   }
   .columnsTemplate('1fr')
   .columnsGap(2)
   .rowsGap(2)
   .scrollBar(BarState.Off)
   ```
2. 给Grid组件设置[editMode](../harmonyos-references/ts-container-grid.md#editmode8)为true，即Grid进入编辑模式，进入编辑模式可以拖拽Grid组件内部GridItem。设置[supportAnimation](../harmonyos-references/ts-container-grid.md#supportanimation8)为true，即Grid拖拽元素时支持动画。

   ```ts
   .supportAnimation(true)
   .editMode(true) // 设置Grid是否进入编辑模式，进入编辑模式可以拖拽Grid组件内部GridItem
   ```
3. 定义GridItem被拖拽时元素的样式，元素被拖拽时展示浮动内容。

   ```ts
   @Builder
   pixelMapBuilder() { // 拖拽过程样式
     Column() {
       Text('浮动内容' + this.text)
         .fontSize(16)
         .backgroundColor('#f1f3f5')
         .width('90%')
         .height(30)
         .textAlign(TextAlign.Center);
     };
   }
   ```
4. 判断当前移动的是不是标题，如果是标题禁止拖动。

   ```ts
   // 判断是否是标题
   isTitle(index: number) {
     if (index === 0) {
       return true;
     }
     if (!this.isShowGroup1 && index === 1) {
       return true;
     }
     if (this.isShowGroup1 && index === this.numbers.length + 1) {
       return true;
     }
     return false;
   }
   ```
5. 定义拖拽过程中的数组交换逻辑。

   ```ts
   moveToIndex(index1: number, index2: number) { // 将index1位置的元素移动至 index2位置
     let temp = '';
     let num1Length = 1 + (this.numbers.length - 1) * Number(this.isShowGroup1);
     if (index1 <= num1Length) {
       temp = this.numbers.splice(index1 - 1, 1)[0];
     } else {
       index1 = index1 - this.numbers.length - 1;
       temp = this.numbers2.splice(index1 - 1, 1)[0];
     }
     if (index2 <= num1Length) {
       this.numbers.splice(index2 - 1, 0, temp);
     } else {
       index2 = index2 - this.numbers.length - 1;
       this.numbers2.splice(index2 - 1, 0, temp);
     }
   }
   ```
6. 给Grid组件绑定[onItemDragStart](../harmonyos-references/ts-container-grid.md#onitemdragstart8)和[onItemDrop](../harmonyos-references/ts-container-grid.md#onitemdrop8)事件，在[onItemDragStart](../harmonyos-references/ts-container-grid.md#onitemdragstart8)回调中设置拖拽过程中显示的图片，并在[onItemDrop](../harmonyos-references/ts-container-grid.md#onitemdrop8)中完成交换数组位置的逻辑。

   ```ts
   .onItemDragStart((event: ItemDragInfo, itemIndex: number) => { // 第一次拖拽此事件绑定的组件时，触发回调。
     if (this.isTitle(itemIndex)) {
       return;
     }
     if (itemIndex > this.numbers.length) {
       itemIndex = itemIndex - this.numbers.length - 1;
       this.text = this.numbers2[itemIndex - 1];
     } else {
       this.text = this.numbers[itemIndex - 1];
     }
     return this.pixelMapBuilder(); // 设置拖拽过程中显示的图片。
   })
   .onItemDrop((event: ItemDragInfo, itemIndex: number,
     insertIndex: number) => { // 绑定此事件的组件可作为拖拽释放目标，当在本组件范围内停止拖拽行为时，触发回调。
     console.info(`eventX: ${event.x}`);
     this.moveToIndex(itemIndex, insertIndex);
   });
   ```

完整示例如下：

```ts
@Entry
@Component
struct GridDemo {
  @State numbers: string[] = [];
  @State numbers2: string[] = [];
  @State isShowGroup1: boolean = true;
  @State isShowGroup2: boolean = true;
  @State text: string = 'drag';
  scroller: Scroller = new Scroller();

  @Builder
  pixelMapBuilder() { // 拖拽过程样式
    Column() {
      Text('浮动内容' + this.text)
        .fontSize(16)
        .backgroundColor('#f1f3f5')
        .width('90%')
        .height(30)
        .textAlign(TextAlign.Center);
    };
  }

  aboutToAppear() {
    for (let i = 1; i <= 15; i++) {
      this.numbers.push('组1-' + i);
      this.numbers2.push('组2-' + i);
    }
  }

  moveToIndex(index1: number, index2: number) { // 将index1位置的元素移动至 index2位置
    let temp = '';
    let num1Length = 1 + (this.numbers.length - 1) * Number(this.isShowGroup1);
    if (index1 <= num1Length) {
      temp = this.numbers.splice(index1 - 1, 1)[0];
    } else {
      index1 = index1 - this.numbers.length - 1;
      temp = this.numbers2.splice(index1 - 1, 1)[0];
    }
    if (index2 <= num1Length) {
      this.numbers.splice(index2 - 1, 0, temp);
    } else {
      index2 = index2 - this.numbers.length - 1;
      this.numbers2.splice(index2 - 1, 0, temp);
    }
  }

  // 判断是否是标题
  isTitle(index: number) {
    if (index === 0) {
      return true;
    }
    if (!this.isShowGroup1 && index === 1) {
      return true;
    }
    if (this.isShowGroup1 && index === this.numbers.length + 1) {
      return true;
    }
    return false;
  }

  build() {
    Column({ space: 5 }) {
      Column() {
        Grid(this.scroller) {
          GridItem() {
            Text('标题1-' + this.numbers.length)
              .fontSize(16)
              .width('100%')
              .height(30)
              .padding({ left: 10 })
              .textAlign(TextAlign.Start);
          }
          .onClick(() => {
            this.isShowGroup1 = !this.isShowGroup1;
          });

          if (this.isShowGroup1) {
            ForEach(this.numbers, (day: string) => {
              GridItem() {
                Text(day)
                  .fontSize(16)
                  .backgroundColor('#f1f3f5')
                  .width('100%')
                  .height(30)
                  .textAlign(TextAlign.Center);
              };
            });
          }
          GridItem() {
            Text('标题2-' + this.numbers2.length)
              .fontSize(16)
              .width('100%')
              .height(30)
              .padding({ left: 10 })
              .textAlign(TextAlign.Start);
          }
          .onClick(() => {
            this.isShowGroup2 = !this.isShowGroup2;
          });

          if (this.isShowGroup2) {
            ForEach(this.numbers2, (day: string) => {
              GridItem() {
                Text(day)
                  .fontSize(16)
                  .backgroundColor('#f1f3f5')
                  .width('100%')
                  .height(30)
                  .textAlign(TextAlign.Center);
              };
            });
          }
        }
        .columnsTemplate('1fr')
        .columnsGap(2)
        .rowsGap(2)
        .scrollBar(BarState.Off)
        .onScrollIndex((first: number) => {
          console.info(first.toString());
        })
        .width('90%')
        .supportAnimation(true)
        .editMode(true) // 设置Grid是否进入编辑模式，进入编辑模式可以拖拽Grid组件内部GridItem
        .onItemDragStart((event: ItemDragInfo, itemIndex: number) => { // 第一次拖拽此事件绑定的组件时，触发回调。
          if (this.isTitle(itemIndex)) {
            return;
          }
          if (itemIndex > this.numbers.length) {
            itemIndex = itemIndex - this.numbers.length - 1;
            this.text = this.numbers2[itemIndex - 1];
          } else {
            this.text = this.numbers[itemIndex - 1];
          }
          return this.pixelMapBuilder(); // 设置拖拽过程中显示的图片。
        })
        .onItemDrop((event: ItemDragInfo, itemIndex: number,
          insertIndex: number) => { // 绑定此事件的组件可作为拖拽释放目标，当在本组件范围内停止拖拽行为时，触发回调。
          console.info(`eventX: ${event.x}`);
          this.moveToIndex(itemIndex, insertIndex);
        });

      };
    }.width('100%').margin({ top: 5 });
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/TovCOIr3SUq1HID522KBnQ/zh-cn_image_0000002628759786.png "点击放大")
