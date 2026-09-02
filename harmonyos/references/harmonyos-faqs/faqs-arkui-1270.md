---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1270
title: Swiper嵌套Scroll组件滑动问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Swiper嵌套Scroll组件滑动问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ef13cd51551049043638ecea3b438b74540cad62383983ea7c27b4c5842fb088
---

## 问题现象

Swiper嵌套Scroll组件，Swiper不同索引内容高度不一样的情况下，如何实现Scroll组件可以滚动并且内容顶部对齐的效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/KS0Ie8_hQV-0MfudAFev8A/zh-cn_image_0000002628756012.gif "点击放大")

## 背景知识

* [Swiper](../harmonyos-references/ts-container-swiper.md)：滑块视图容器，提供子组件滑动轮播显示的能力。
* [Scroll](../harmonyos-references/ts-container-scroll.md)：可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
* [align](../harmonyos-references/ts-universal-attributes-location.md#align)：设置容器元素绘制区域内的子元素的对齐方式。

## 解决方案

Scroll组件不能滚动的原因是将Scroll包裹的Column组件的高度值设置为100%，将高度去掉之后可以实现滚动效果但内容会居中显示，这时将Scroll组件的align属性值设置为Alignment.Top即可实现内容顶部对齐效果。

```ts
@Entry
@Component
export struct ScrollPage {
  controller: SwiperController = new SwiperController();
  @State dataList: string[] = ['1', '2', '3', '4'];
  private swiperCurrentIndex: number = 0;

  build() {
    Column() {
      Text('标题');

      Swiper(this.controller) {
        ForEach(this.dataList, (data: string, index: number) => {
          Scroll() {
            Column() {
              if (index === 1) {
                Column() {
                  Row().width('100%').height(300).backgroundColor('#0A59F7');
                  Row().width('100%').height(300).backgroundColor('#ff0af7c0');
                  Row().width('100%').height(300).backgroundColor('#ffeff70a');
                };
              } else if (index === 2) {
                Column() {
                  Row().width('100%').height(300).backgroundColor('#fff7790a');
                  Row().width('100%').height(300).backgroundColor('#ff0af7e3');
                  Row().width('100%').height(300).backgroundColor('#ee0a88f7');
                  Row().width('100%').height(300).backgroundColor('#ddf7eb0a');
                  Row().width('100%').height(300).backgroundColor('#dd0af7f7');
                };
              } else {
                Text(data + '内容顶部对齐').alignSelf(ItemAlign.Start);
              }
            }
            // .height("100%") 这里将高度去掉
            .alignItems(HorizontalAlign.Start).justifyContent(FlexAlign.Start);
          }
          // 设置Alignment.Top
          .align(Alignment.Top)
          .nestedScroll({ scrollForward: NestedScrollMode.PARENT_FIRST, scrollBackward: NestedScrollMode.SELF_FIRST });

        }, (item: string) => JSON.stringify(item));
      }
      .layoutWeight(1)
      .cachedCount(1)
      .backgroundColor(Color.Transparent)
      .index(this.swiperCurrentIndex)
      .width('100%')
      .loop(false)
      .autoPlay(false)
      .indicator(false);

      Blank();
      Text('底部组件');
    };
  }
}
```
