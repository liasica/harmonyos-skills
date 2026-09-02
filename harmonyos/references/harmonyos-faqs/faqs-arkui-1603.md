---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1603
title: List如何实时获取可见的ListItem索引值
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > List如何实时获取可见的ListItem索引值
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d54c494e0ac446d2ae58342586c2954cd22604e0300d738ec69a9785a2635df6
---

## 问题现象

滚动List组件，如何实时获取第一个可见的Item和最后一个可见的Item的索引位置？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/WgABFLgjS_eBx2rYIur4Dg/zh-cn_image_0000002628613340.png "点击放大")

## 背景知识

* [List](../harmonyos-references/ts-container-list.md)：列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。
* [ListItem](../harmonyos-references/ts-container-listitem.md)：用来展示列表具体Item，必须配合List来使用。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)在组件大小变化时触发，可用于获取组件的坐标和宽高。
* List显示区域内第一个子组件的索引值或最后一个子组件的索引值有变化时会触发[onScrollIndex](../harmonyos-references/ts-container-list.md#onscrollindex)，列表滑动停止时触发[onScrollStop](../harmonyos-references/ts-container-list.md#onscrollstop)。

## 解决方案

具体实现如下：

1. 使用onAreaChange获取List组件的宽高，用于后续判断Item是否在List区域内。
2. 列表初始化后需要先使用onScrollIndex获取第一个和最后一个Item，后续使用onScrollStop来获取首尾的Item。
3. 获取到的首尾Item后，判断其是否完全可见，首部Item不完全可见则取后一位，尾部Item不完全可见则取前一位。

```ts
@Entry
@Component
struct ListVisibleByH {
  private arr: number[] = [];
  private scrollerForList: Scroller = new Scroller();
  @State startStr: string = '';
  startIndex = 0; // 保存第一个可见Item
  endIndex = 0; // 保存最后一个可见Item
  listHeight: number = 0; // 保存list的高度

  private judgeVisibleByHeight() {
    console.info('judgeVisibleByHeight');
    this.startStr = '';
    // 判断是否遮挡，判断条件可自行调节，这里设置3vp的误差
    let rect = this.scrollerForList.getItemRect(this.startIndex);
    if (rect.y < -3) {
      this.startIndex = this.startIndex + 1; // 上方元素y坐标小于-3，被遮挡
    }
    rect = this.scrollerForList.getItemRect(this.endIndex);
    if (rect.y + rect.height > this.listHeight + 3) {
      this.endIndex = this.endIndex - 1; // 下方元素高度超过父组件的高度，被遮挡
    }
    if (this.startIndex <= this.endIndex) {
      this.startStr = `首尾可见Item：${this.startIndex}, ${this.endIndex}`;
    } else {
      this.startStr = '没有能全部显示的Item';
    }
  }

  aboutToAppear() {
    for (let i = 0; i < 20; i++) {
      this.arr.push(i);
    }
  }

  build() {
    Flex({ direction: FlexDirection.Column }) {
      Text(this.startStr)
        .textAlign(TextAlign.Center)
        .height(50)
        .width('100%');
      Row() {
        List({ space: 20, initialIndex: 0, scroller: this.scrollerForList }) {
          ForEach(this.arr, (item: number) => {
            ListItem() {
              Text(`${item}`)
                .width('100%').fontSize(16)
                .textAlign(TextAlign.Center);
            }
            .borderRadius(16).backgroundColor('#F1F3F5')
            .width('90%')
            .height(200);
          }, (item: number) => item.toString());
        }
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
        .alignListItem(ListItemAlign.Center)
        .listDirection(Axis.Vertical)
        .height('100%')
        .width('100%')
        .borderRadius(10)
        .onAreaChange((oldValue, newValue) => {
          console.info(`onAreaChange ${oldValue}`);
          this.listHeight = newValue.height as number; // list的高度
          this.judgeVisibleByHeight(); // 初始判断
        })
        .onScrollIndex((start, end) => {
          this.startIndex = start;
          this.endIndex = end;
        })
        .onScrollStop(() => {
          // 缓存开始结束索引：在最后一项继续滑动，不会触发onScrollIndex
          let tmpStart = this.startIndex;
          let tmpEnd = this.endIndex;
          this.judgeVisibleByHeight();
          this.startIndex = tmpStart;
          this.endIndex = tmpEnd;
        });
      }.width('100%').height('100%');
    }.width('100%').height('100%');
  }
}
```

## 常见FAQ

Q：在List组件中使用ListItemGroup的情况下，如何获取其中ListItem的索引值？

A：onScrollIndex回调将ListItemGroup作为一个整体占一个索引值，不计算ListItemGroup内部ListItem的索引值，因此就会获取不到当前ListItemGroup内ListItem的索引值。可以用[onVisibleAreaChange](../harmonyos-references/ts-universal-component-visible-area-change-event.md#onvisibleareachange)回调来监听ListItem的可见状态变化。

Q：怎么设置多个ListItemGroup同时出现时，只显示最顶部的header中的Button按钮？

A：通过给ListItemGroup组件添加onVisibleAreaChange事件中，判断当前显示了哪些ListItemGroup，同时选择其中最顶部的ListItemGroup显示Button。
