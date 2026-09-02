---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1316
title: Grid组件自动滚屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Grid组件自动滚屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:01a26941f64570ecbf6431de5e23b75d0f9af4b7aa48327b60ae23e439b993a0
---

## 问题现象

当GridItem拖拽到边缘时自滚动，拖拽到右下指定区域删除GridItem。

## 背景知识

[Grid组件](../harmonyos-references/ts-container-grid.md)是一种网格容器，由“行”和“列”分割的单元格所组成，通过指定“项目”所在的单元格做出各种各样的布局。在实现以上功能之前需要先了解基本的Grid组件[事件](../harmonyos-references/ts-container-grid.md#事件)以及官方基础参考示例： [示例5（Grid拖拽场景）](../harmonyos-references/ts-container-grid.md#示例5grid拖拽场景)。

实现拖拽到边缘的时候Grid组件自动滚动思路：

1. 通过[onScrollIndex()](../harmonyos-references/ts-container-grid.md#onscrollindex)获取Grid组件显示区域上第一个子组件和最后一个组件的索引值；
2. 在[onItemDragMove()](../harmonyos-references/ts-container-grid.md#onitemdragmove8)拖拽移动事件中，通过this.scroller.currentOffset()获取scroller的实时y坐标；
3. 通过在拖拽移动时设置边缘判定条件，并采用[scrollTo()](../harmonyos-references/ts-container-scroll.md#scrollto)方法实现滚动到指定位置，实现自动滚动能力。

## 解决方案

在自滚动的基础上新增拖动Item到指定区域删除功能，先通过onItemDrop回调中的event参数判断GridItem移动的坐标，当坐标移动到指定区域后，再删除该元素。示例如下：

```ts
.onItemDrop((event: ItemDragInfo, itemIndex: number,
  insertIndex: number) => { //绑定此事件的组件可作为拖拽释放目标，当在本组件范围内停止拖拽行为时，触发回调。
  if (event.x > 270 && event.y > 710) {
    this.numbers.splice(itemIndex, 1);
  } else {
    this.moveToIndex(itemIndex, insertIndex);
  }
  this.isShowDelete = false;
});
```

完整示例代码如下：

```ts
@Entry
@Component
struct GridDemo {
  @State numbers: string[] = [];
  @State isShowDelete: boolean = false;
  @State text: string = 'drag';
  scroller: Scroller = new Scroller();
  @State startIndex: number = 0;
  @State endIndex: number = 0;

  @Builder
  pixelMapBuilder() { // 拖拽过程样式
    Column() {
      Text('浮动内容')
        .borderRadius(12)
        .fontSize(16)
        .backgroundColor(0xF9CF93)
        .width(100)
        .height(120)
        .textAlign(TextAlign.Center);
    };
  }

  aboutToAppear() {
    for (let i = 1; i <= 20; i++) {
      this.numbers.push(`组1-${i}`);
    }
  }

  moveToIndex(index1: number, index2: number) { // 将index1位置的元素移动至 index2位置
    let temp = '';
    let num1Length = this.numbers.length;
    temp = this.numbers[index1];

    if (index2 < num1Length && index2 !== -1) {
      this.numbers[index1] = this.numbers[index2];
      this.numbers[index2] = temp;
    } else if (index2 === -1) {
      this.numbers[index1] = this.numbers[num1Length - 1];
      this.numbers[num1Length - 1] = temp;
    } else {
      this.numbers[index1] = this.numbers[num1Length - 1];
      this.numbers[num1Length - 1] = temp;
    }
  }

  build() {
    Stack() {
      Column() {
        Grid(this.scroller) {
          ForEach(this.numbers, (day: string) => {
            GridItem() {
              Text(day)
                .borderRadius(12)
                .fontSize(16)
                .backgroundColor('#f1f3f5')
                .width(100)
                .height(120)
                .textAlign(TextAlign.Center);
            };
          });
        }
        .scrollBar(BarState.Off)
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
        .padding({ left: 16, right: 16 })
        .columnsTemplate('1fr 1fr 1fr')
        .rowsGap(20)
        .editMode(true) //设置Grid是否进入编辑模式，进入编辑模式可以拖拽Grid组件内部GridItem
        .onScrollIndex((start: number, end: number) => {
          this.startIndex = start;
          this.endIndex = end;
        })
        .onItemDragStart((event: ItemDragInfo, itemIndex: number) => { //第一次拖拽此事件绑定的组件时，触发回调。
          this.text = this.numbers[itemIndex];
          return this.pixelMapBuilder(); //设置拖拽过程中显示的图片。
        })
        .onItemDragMove((event: ItemDragInfo, itemIndex: number, insertIndex: number) => {
          this.isShowDelete = true;
          // 滑出网格外自动滚动位置，判断条件根据实际情况调整
          if (insertIndex <= this.startIndex + 2) {
            const yOffset: number = this.scroller.currentOffset().yOffset;
            this.scroller.scrollTo({ xOffset: 0, yOffset: yOffset - 200, animation: true });
          }
          if (insertIndex >= this.endIndex - 2 && insertIndex <= this.numbers.length - 1) {
            const yOffset: number = this.scroller.currentOffset().yOffset;
            this.scroller.scrollTo({ xOffset: 0, yOffset: yOffset + 200, animation: true });
          }
        })
        .onItemDrop((event: ItemDragInfo, itemIndex: number,
          insertIndex: number) => { //绑定此事件的组件可作为拖拽释放目标，当在本组件范围内停止拖拽行为时，触发回调。
          if (event.x > 270 && event.y > 710) {
            this.numbers.splice(itemIndex, 1);
          } else {
            this.moveToIndex(itemIndex, insertIndex);
          }
          this.isShowDelete = false;
        });
      }
      .width('100%')
      .height('100%')
      .margin({ top: 5 });

      if (this.isShowDelete) {
        Column() {
          Text('删除')
            .fontSize(16)
            .backgroundColor(0x66F9CF93)
            .width(100)
            .height(100)
            .padding({ left: 10 })
            .textAlign(TextAlign.Start);
        };
      }
    }
    .alignContent(Alignment.BottomEnd);
  }
}
```

实现效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/fJ3AUGB6TaCYdacO-JOEaQ/zh-cn_image_0000002658838373.gif "点击放大")
