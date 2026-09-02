---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-876
title: 页面滑动幅度过大
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 页面滑动幅度过大
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:375a126a09e64e7cb176416ed40e0b025017f521aa3f1df0ef16b292f0617541
---

## 问题现象

页面滚动时，当用户快速滑动列表会导致滑动幅度过大（即单次滑动距离超过预期范围），造成页面跳动感明显，影响用户体验。

## 背景知识

* [Scroller组件](../harmonyos-references/ts-container-scroll.md#scroller)：ArkUI中用于实现滚动功能的容器组件，支持自定义滚动行为（如摩擦力、边缘效果等）。
* [friction属性](../harmonyos-references/ts-container-list.md#friction10)：控制滚动的阻尼系数，值越大滚动越“吃力”（滑动幅度减小），但无法直接限制单次最大滑动距离。
* [onScrollFrameBegin](../harmonyos-references/ts-container-list.md#onscrollframebegin9)：在每次滚动帧开始时触发，允许开发者通过返回offsetRemain动态修改当前滚动偏移量，可用于实现滑动限制逻辑。

## 问题定位

* 检查List属性是否设置friction，通过friction增加滑动阻力。
* 检查List属性是否设置onScrollFrameBegin，是否通过onScrollFrameBegin限制滑动偏移量。

## 分析结论

未设置onScrollFrameBegin或者较高的friction来限制滑动偏移量，导致即使用户小幅度的交互，也会引起大幅度的滑动。

## 修改建议

以下是通过friction与onScrollFrameBegin限制滑动偏移量的实现方案：

```ts
@Entry
@Component
struct ScrollerPage1 {
  scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];

  build() {
    Column() {
      List({ space: 20, initialIndex: 0, scroller: this.scroller }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text('' + item)
              .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF);
          };
        }, (item: number) => item.toString());
      }
      .listDirection(Axis.Vertical)
      .scrollBar(BarState.Off)
      .friction(3)
      .divider({
        strokeWidth: 2,
        color: 0xFFFFFF,
        startMargin: 20,
        endMargin: 20
      })
      .width('90%');
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 });
  }
}
```

或者设置onScrollFrameBegin：

```ts
@Entry
@Component
struct ScrollerPage2 {
  scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];

  build() {
    Column() {
      List({ space: 20, initialIndex: 0, scroller: this.scroller }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text('' + item)
              .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF);
          };
        }, (item: number) => item.toString());
      }
      .listDirection(Axis.Vertical)
      .scrollBar(BarState.Off)
      .divider({
        strokeWidth: 2,
        color: 0xFFFFFF,
        startMargin: 20,
        endMargin: 20
      })
      .width('90%')
      .onScrollFrameBegin((offset: number) => {
        if (offset > 5) {
          offset = 5;
        }
        if (offset < -5) {
          offset = -5;
        }
        return { offsetRemain: offset };
      });
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 });
  }
}
```
