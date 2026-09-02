---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1349
title: 实现List头部插入数据时显示的项不变
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 实现List头部插入数据时显示的项不变
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:09+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:faf023300e3f2bf8f592b63ad338c5f9d5924c71903775f49e36645ccfdee063
---

## 问题现象

当用户在聊天界面上滑时，通常需要从数据库中加载更早的消息，这些消息需要插入到当前消息列表的头部，如果直接将数据插入到头部而不进行其他操作，会使当前正在查看的消息被挤出屏幕。那么如何实现往List数据源数组的头部插入数据时List显示的项不变呢？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/cqH6aatdRJKsfONtfd2N2g/zh-cn_image_0000002658840791.png "点击放大")

## 背景知识

* [onScrollIndex](../harmonyos-references/ts-container-list.md#onscrollindex)在子组件划入或划出List显示区域时触发，可用于记录List当前项的索引位置。
* [scrollToIndex](../harmonyos-references/ts-container-scroll.md#scrolltoindex)可以让ListItem滑动到指定Index，支持设置滑动额外偏移量。
* [currentOffset](../harmonyos-references/ts-container-scroll.md#currentoffset)可以获取List当前的滑动偏移量，从而计算scrollToIndex所需的滑动额外偏移量。

## 解决方案

1. 通过onScrollIndex记录当前索引位置。
2. 插入新数据时，使当前Index的值更新为oldIndex+新插入数组长度，调用scrollToIndex接口滑动到更新后的索引处。
3. 计算滑动额外偏移量：当ListItem一部分显示在可视区域内，一部分显示在可视区域外时，如果只让ListItem滑动到指定Index而不设置额外偏移量，会使当前显示的ListItem轻微滑动到完全显示，有碍阅读观感。因此需要将ListItem在可视区域外的高度作为滑动额外偏移量，使屏幕内容完全不变。完整示例代码如下：

完整示例参考如下：

```ts
@Entry
@Component
struct StableList {
  @State listData: string[] =
    ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8', 'item9', 'item10'];
  scrollerForList: Scroller = new Scroller();
  @State ListIndex: number = 0;
  @State nextItemIndex: number = 0;

  build() {
    Column() {
      Row() {
        Button('头部插入数据')
          .onClick(() => this.prependItems())
          .margin(10);
        Button('滚动到顶部')
          .onClick(() => this.scrollerForList.scrollToIndex(0))
          .margin(10);
      };

      List({ space: 20, initialIndex: this.ListIndex, scroller: this.scrollerForList }) {
        ForEach(this.listData, (item: string) => {
          ListItem() {
            Text(item)
              .fontSize(20)
              .width('100%')
              .textAlign(TextAlign.Center)
              .backgroundColor('#f5f5f5')
              .height(60);
          };
        }, (item: string) => item);
      }
      .width('100%')
      .height('80%')
      .onScrollIndex((firstIndex: number) => {
        this.ListIndex = firstIndex;
      });
    }
    .width('100%')
    .height('100%');
  }

  prependItems() {
    console.info(`索引${this.ListIndex}`, ` 偏移量${this.scrollerForList.currentOffset().yOffset}`);
    const oldIndex: number = this.ListIndex;
    const newItems: string[] = [];
    for (let i = 0; i < 5; i++) {
      newItems.push(`new item${this.nextItemIndex + i}`);
    }
    this.nextItemIndex += 5;
    this.listData = [...newItems, ...this.listData];
    // 计算新的位置并滚动
    const newListLength: number = newItems.length;
    const newIndex: number = oldIndex + newListLength;
    this.scrollerForList.scrollToIndex(newIndex, false, undefined,
      { extraOffset: { value: this.scrollerForList.currentOffset().yOffset - 80 * oldIndex, unit: 1 } });
  }
}
```
