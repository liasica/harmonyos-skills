---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-840
title: 如何解决拖拽功能和长按功能的冲突问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决拖拽功能和长按功能的冲突问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:619021cf9c061f136d5b4dd9d0c4c1d06b642b6780480d6ac54eb8d3b56aeb32
---

## 问题现象

在List组件中，单个ListItem在同时设置拖拽功能与长按功能时，实际运行之后会产生冲突，如何解决单个ListItem拖拽功能和长按功能的冲突问题？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/JaJqfeo3QrWTYWDvpj6z-g/zh-cn_image_0000002628398638.gif "点击放大")

## 背景知识

* [支持统一拖拽](../harmonyos-guides/arkts-common-events-drag-event.md)提供了一种通过鼠标或手势触屏传递数据的机制，即从一个组件位置拖出数据并将其拖入到另一个组件位置，以触发响应。
* [长按手势](../harmonyos-guides/arkts-gesture-events-single-gesture.md#长按手势longpressgesture)通过长按屏幕触发长按手势事件。
* 由于拖拽事件和长按手势都需要通过长按来触发，因此这种[组合手势](../harmonyos-guides/arkts-gesture-events-combined-gestures.md)类型会出现冲突，例如[List](../harmonyos-references/ts-container-list.md)组件中每个[ListItem](../harmonyos-references/ts-container-listitem.md)都设置单独的长按事件时，拖拽功能和长按手势功能就会出现冲突。
* [Grid](../harmonyos-references/ts-container-grid.md)网格容器，由“行”和“列”分割的单元格所组成，通过指定“项目”所在的单元格做出各种各样的布局。
* 滑动手势[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)，能够提供自定义拖拽事件的功能。

## 解决方案

由于在ListItem中设置单独的长按事件会与拖拽事件产生冲突，因此建议放弃List本身的拖拽事件，使用滑动手势PanGesture，自行实现拖拽过程的逻辑，然后再通过组合手势的功能，去实现其他的长按事件。

```ts
import curves from '@ohos.curves';

@Entry
@Component
struct Page {
  // 元素数组
  @State numbers: number[] = [];
  // 多列
  private str: string = '';
  row: number = 4;
  // 元素数组中最后一个元素的索引
  @State lastIndex: number = 0;
  @State dragItem: number = -1;
  @State scaleItem: number = -1;
  item: number = -1;
  private dragRefOffsetX: number = 0;
  private dragRefOffsetY: number = 0;
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  private FIX_VP_X: number = 108;
  private FIX_VP_Y: number = 120;

  aboutToAppear() {
    for (let i = 1; i <= 36; i++) {
      this.numbers.push(i);
    }
    this.lastIndex = this.numbers.length - 1;
    // 多列
    for (let i = 0; i < this.row; i++) {
      this.str = this.str + '1fr ';
    }
  }

  itemMove(index: number, newIndex: number): void {
    console.info('index:' + index + ' newIndex:' + newIndex);
    if (!this.isDraggable(newIndex)) {
      return;
    }
    let tmp = this.numbers.splice(index, 1);
    this.numbers.splice(newIndex, 0, tmp[0]);
  }

  // 向下滑
  down(index: number): void {
    if (!this.isDraggable(index + this.row)) {
      return;
    }
    this.offsetY -= this.FIX_VP_Y;
    this.dragRefOffsetY += this.FIX_VP_Y;
    // 多列
    this.itemMove(index, index + this.row);
  }

  // 向下滑(右下角为空)
  down2(index: number): void {
    if (!this.isDraggable(index + 3)) {
      return;
    }
    this.offsetY -= this.FIX_VP_Y;
    this.dragRefOffsetY += this.FIX_VP_Y;
    this.itemMove(index, index + 3);
  }

  // 向上滑
  up(index: number): void {
    if (!this.isDraggable(index - this.row)) {
      return;
    }
    this.offsetY += this.FIX_VP_Y;
    this.dragRefOffsetY -= this.FIX_VP_Y;
    this.itemMove(index, index - this.row);
  }

  // 向左滑
  left(index: number): void {
    if (!this.isDraggable(index - 1)) {
      return;
    }
    this.offsetX += this.FIX_VP_X;
    this.dragRefOffsetX -= this.FIX_VP_X;
    this.itemMove(index, index - 1);
  }

  // 向右滑
  right(index: number): void {
    if (!this.isDraggable(index + 1)) {
      return;
    }
    this.offsetX -= this.FIX_VP_X;
    this.dragRefOffsetX += this.FIX_VP_X;
    this.itemMove(index, index + 1);
  }

  // 向右下滑
  lowerRight(index: number): void {
    if (!this.isDraggable(index + this.row + 1)) {
      return;
    }
    this.offsetX -= this.FIX_VP_X;
    this.dragRefOffsetX += this.FIX_VP_X;
    this.offsetY -= this.FIX_VP_Y;
    this.dragRefOffsetY += this.FIX_VP_Y;
    this.itemMove(index, index + this.row + 1);
  }

  // 向右上滑
  upperRight(index: number): void {
    if (!this.isDraggable(index - (this.row - 1))) {
      return;
    }
    this.offsetX -= this.FIX_VP_X;
    this.dragRefOffsetX += this.FIX_VP_X;
    this.offsetY += this.FIX_VP_Y;
    this.dragRefOffsetY -= this.FIX_VP_Y;
    this.itemMove(index, index - (this.row - 1));
  }

  // 向左下滑
  lowerLeft(index: number): void {
    if (!this.isDraggable(index + (this.row - 1))) {
      return;
    }
    this.offsetX += this.FIX_VP_X;
    this.dragRefOffsetX -= this.FIX_VP_X;
    this.offsetY -= this.FIX_VP_Y;
    this.dragRefOffsetY += this.FIX_VP_Y;
    this.itemMove(index, index + (this.row - 1));
  }

  // 向左上滑
  upperLeft(index: number): void {
    if (!this.isDraggable(index - (this.row + 1))) {
      return;
    }
    this.offsetX += this.FIX_VP_X;
    this.dragRefOffsetX -= this.FIX_VP_X;
    this.offsetY += this.FIX_VP_Y;
    this.dragRefOffsetY -= this.FIX_VP_Y;
    this.itemMove(index, index - (this.row + 1));
  }

  // 通过元素的索引，控制对应元素是否能移动排序
  isDraggable(index: number): boolean {
    console.info(`index: ${index}`);
    return index > -1; // 恒成立，所有元素均可移动排序
  }

  build() {
    Column() {
      Grid() {
        ForEach(this.numbers, (item: number) => {
          GridItem() {
            Text(item + '')
              .fontSize(16)
              .width('100%')
              .textAlign(TextAlign.Center)
              .height(100)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
              .shadow(this.scaleItem == item ? {
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
          // 添加震动
          .onTouch(() => {
          })
          .onAreaChange((oldVal, newVal) => {
            // 多列
            this.FIX_VP_X = Math.round(newVal.width as number);
            this.FIX_VP_Y = Math.round(newVal.height as number);
            console.info(`oldVal:${JSON.stringify(oldVal)}`);
          })
          // 指定固定GridItem不响应事件
          .hitTestBehavior(this.isDraggable(this.numbers.indexOf(item)) ? HitTestMode.Default : HitTestMode.None)
          .scale({ x: this.scaleItem == item ? 1.05 : 1, y: this.scaleItem == item ? 1.05 : 1 })
          .zIndex(this.dragItem == item ? 1 : 0)
          .translate(this.dragItem == item ? { x: this.offsetX, y: this.offsetY } : { x: 0, y: 0 })
          .padding(10)
          .gesture(
            GestureGroup(GestureMode.Sequence,
              LongPressGesture({ repeat: true, duration: 50 })
                .onAction((event?: GestureEvent) => {
                  console.info(`event: ${event}`);
                  this.getUIContext().animateTo({ curve: Curve.Friction, duration: 300 }, () => {
                    this.scaleItem = item;
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
                  this.dragRefOffsetX = 0;
                  this.dragRefOffsetY = 0;
                })
                .onActionUpdate((event: GestureEvent) => {
                  this.offsetY = event.offsetY - this.dragRefOffsetY;
                  this.offsetX = event.offsetX - this.dragRefOffsetX;
                  console.info(`移动过程中event.offsetY：${event.offsetY}`,
                    ` this.dragRefOffsetY: ${this.dragRefOffsetY}`, `this.offsetY: ${this.offsetY}`);
                  console.info(`移动过程中event.offsetX：${event.offsetX}`,
                    ` this.dragRefOffsetX: ${this.dragRefOffsetX}`, `this.offsetX: ${this.offsetX}`);
                  this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
                    let index = this.numbers.indexOf(this.dragItem);
                    console.info('index= ', index);
                    if (this.offsetY >= this.FIX_VP_Y / 2 &&
                      (this.offsetX <= this.FIX_VP_X / 2 && this.offsetX >= -this.FIX_VP_X / 2)
                      && (index + this.row <= this.lastIndex)) {
                      // 向下滑
                      this.down(index);
                    } else if (this.offsetY <= -this.FIX_VP_Y / 2 &&
                      (this.offsetX <= this.FIX_VP_X / 2 && this.offsetX >= -this.FIX_VP_X / 2)
                      && index - this.row >= 0) {
                      // 向上滑
                      this.up(index);
                    } else if (this.offsetX >= this.FIX_VP_X / 2 &&
                      (this.offsetY <= this.FIX_VP_Y / 2 && this.offsetY >= -this.FIX_VP_Y / 2)
                      && !(((index - (this.row - 1)) % this.row == 0) || index == this.lastIndex)) {
                      // 向右滑
                      this.right(index);
                    } else if (this.offsetX <= -this.FIX_VP_X / 2 &&
                      (this.offsetY <= this.FIX_VP_Y / 2 && this.offsetY >= -this.FIX_VP_Y / 2)
                      && !(index % this.row == 0)) {
                      // 向左滑
                      this.left(index);
                    } else if (this.offsetX >= this.FIX_VP_X / 2 && this.offsetY >= this.FIX_VP_Y / 2
                      && ((index + this.row + 1 <= this.lastIndex && !((index - (this.row - 1)) % this.row == 0)) ||
                        !((index - (this.row - 1)) % this.row == 0))) {
                      // 向右下滑
                      this.lowerRight(index);
                    } else if (this.offsetX >= this.FIX_VP_X / 2 && this.offsetY <= -this.FIX_VP_Y / 2
                      && !((index - this.row < 0) || ((index - (this.row - 1)) % this.row == 0))) {
                      // 向右上滑
                      this.upperRight(index);
                    } else if (this.offsetX <= -this.FIX_VP_X / 2 && this.offsetY >= this.FIX_VP_Y / 2
                      && (!(index % this.row == 0) && (index + (this.row - 1) <= this.lastIndex))) {
                      // 向左下滑
                      this.lowerLeft(index);
                    } else if (this.offsetX <= -this.FIX_VP_X / 2 && this.offsetY <= -this.FIX_VP_Y / 2
                      && !((index <= this.row - 1) || (index % this.row == 0))) {
                      // 向左上滑
                      this.upperLeft(index);
                    } else if (this.offsetX >= this.FIX_VP_X / 2 && this.offsetY >= this.FIX_VP_Y / 2
                      && (index == this.lastIndex)) {
                      // 向右下滑(右下角为空)
                      this.down2(index);
                    }
                  });
                })
                .onActionEnd(() => {
                  this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
                    this.dragItem = -1;
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
                });
                this.getUIContext().animateTo({
                  curve: curves.interpolatingSpring(14, 1, 170, 17)
                }, () => {
                  this.scaleItem = -1;
                });
              })
          );
        }, (item: number) => item.toString());
      }
      .width('90%')
      .editMode(true)
      .scrollBar(BarState.Off)
      // 多列
      .columnsTemplate(this.str);
    }
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
    .width('100%').height('100%').backgroundColor('#f1f3f5').padding({ top: 5 });
  }
}
```

## 常见FAQ

Q：Grid上下左右拖拽动画如何实现？

A：在跨行或跨列场景下，可以通过自定义Grid布局、自定义手势和显式动画来实现拖拽交换的效果。
