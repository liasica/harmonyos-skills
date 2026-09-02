---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-633
title: 如何解决Grid组件中设置onGetIrregularSizeByIndex属性失效问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决Grid组件中设置onGetIrregularSizeByIndex属性失效问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:f8489d4154bd9ac15f70a5f16c61652740a171edbc0793a1a0f7e4fe0ffc3450
---

## 问题现象

在Grid组件中，通过设置onGetIrregularSizeByIndex属性实现第一个元素占据两行两列空间的效果，但是得到的结果却是只占据了一行两列，问题图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/Zox5_9c6S26Qr7Ikx69_kg/zh-cn_image_0000002685942295.png "点击放大")

问题代码如下：

```ts
@Entry
@Component
struct Index {
  @State numbers: String[] = ['0', '1', '2'];
  scroller: Scroller = new Scroller();
  layoutOptions2: GridLayoutOptions = {
    regularSize: [1, 1],
    irregularIndexes: [0, 1, 2],
    onGetIrregularSizeByIndex: (index: number) => {
      if (index === 0) {
        return [2, 2];
      } else {
        return [1, 2]
      }
    }
  };

  build() {
    Column({ space: 5 }) {
      Grid(this.scroller, this.layoutOptions2) {
        ForEach(this.numbers, (item: string) => {
          GridItem() {
            Text(item)
              .fontSize(16)
              .backgroundColor('#ACC6F6')
              .width('100%')
              .height(80)
              .borderRadius(15)
              .textAlign(TextAlign.Center)
          }
        }, (item: string) => item)
      }
      .columnsTemplate('1fr 1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .scrollBar(BarState.Off)
      .width('95%')
      .height(170)
    }
    .width('100%')
  }
}
```

## 背景知识

* [Grid](../harmonyos-references/ts-container-grid.md)：网格容器，由“行”和“列”分割的单元格所组成，通过指定“项目”所在的单元格做出各种各样的布局。
* [GridLayoutOptions](../harmonyos-references/ts-container-grid.md#gridlayoutoptions10对象说明)：Grid布局选项。其中的属性onGetIrregularSizeByIndex需要配合irregularIndexes使用，以此来设置不规则GridItem占用的行数和列数。

## 问题定位

通过问题图可知第一个元素高度是一行的高度，查看代码onGetIrregularSizeByIndex的用法，以及GridItem的高度设置。

## 分析结论

分析问题代码可知，onGetIrregularSizeByIndex设置方法没有问题。问题是由于GridItem中的Text组件的高度写成了固定的一行高度，所以展示的效果是一行两列。

## 修改建议

可以通过三元运算符来设置Text组件的高度，当通过索引判断出是第一个元素时，将高度设置为100%，除此之外的元素高度不变，例如：height(index === 0 ? '100%' : 80)，修改代码如下：

```ts
@Entry
@Component
struct GridHeight {
  @State numbers: String[] = ['0', '1', '2'];
  scroller: Scroller = new Scroller();
  layoutOptions2: GridLayoutOptions = {
    regularSize: [1, 1],
    irregularIndexes: [0, 1, 2],
    onGetIrregularSizeByIndex: (index: number) => {
      if (index === 0) {
        return [2, 2];
      } else {
        return [1, 2];
      }
    }
  };

  build() {
    Column({ space: 0 }) {
      Grid(this.scroller, this.layoutOptions2) {
        ForEach(this.numbers, (item: string, index: number) => {
          GridItem() {
            Text(item)
              .fontSize(16)
              .backgroundColor('#ACC6F6')
              .width('100%')
              .borderRadius(15)
              .height(index === 0 ? '100%' : 80) // 给第一个元素设置高度为100%，即两列的高度
              .textAlign(TextAlign.Center);
          };
        }, (item: string) => item);
      }
      .columnsTemplate('1fr 1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .scrollBar(BarState.Off)
      .width('95%')
      .height(170);
    }
    .width('100%');
  }
}
```

修改后效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/NcKxk5ChSGaRUGbW4qOfRQ/zh-cn_image_0000002686102381.png "点击放大")
