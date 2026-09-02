---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-802
title: 返回顶部按钮功能异常
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 返回顶部按钮功能异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1b0b02159843ef78c826b6b4949ca937cc73bf3205f0f80b655347a8d4c43c95
---

## 问题现象

商品详情页点击回到顶部按钮，页面向上滚动但未回到顶部，且滚动效果不连贯。

## 背景知识

* [List](../harmonyos-references/ts-container-list.md)列表包含一系列相同宽度的列表项。
* [Scroller](../harmonyos-references/ts-container-scroll.md#scroller)可滚动容器组件的控制器，可以控制容器组件的滚动。
  + [scrollTo](../harmonyos-references/ts-container-scroll.md#scrollto)：滑动到指定位置，可以设置动画效果。
  + [scrollEdge](../harmonyos-references/ts-container-scroll.md#scrolledge)：滚动到容器边缘，Scroll组件默认有动画，Grid、List、WaterFlow组件默认无动画。

## 问题定位

1. 使用DevEco Testing查看滚动的组件，滚动组件为List，ListItem中是图片。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/J_qlXIM_RWCA-iS4g3S3Vw/zh-cn_image_0000002628557790.png "点击放大")
2. 检查List组件的滑动控制器Scroller，滑动位置是否设置有误，是否设置了滑动动画。

## 分析结论

点击返回顶部按钮时，List组件的滑动控制器Scroller设置的滑动位置未设置到顶部，且未配置动画属性。

## 修改建议

点击返回顶部按钮时，使用scrollTo或scrollEdge来实现滚动到顶部，并同时设置滚动动画效果。

```ts
@Entry
@Component
struct ListExample {
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
  private scroller: Scroller = new Scroller();

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
              .backgroundColor(0xFFFFFF)
          }
        }, (item: string) => item)
      }
      .listDirection(Axis.Vertical) // 排列方向
      .scrollBar(BarState.Off)
      .friction(0.6)
      .edgeEffect(EdgeEffect.Spring) // 边缘效果设置为Spring
      .onAppear(() => {
        this.scroller.scrollToIndex(0, false, ScrollAlign.CENTER);
      })
      .width('90%')
      .height('94%')

      Button('返回顶部')
        .onClick(() => {
          this.scroller.scrollTo({
            // 设置滚动到顶部，并配置动画
            xOffset: 0, yOffset: 0, animation: {
              duration: 1000
            }
          });
        })
        .margin(3)
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 })
  }
}
```
