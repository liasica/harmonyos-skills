---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1307
title: Swiper在末尾实现添加按钮
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Swiper在末尾实现添加按钮
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f7424048609e2d19dde7ef0d1ac2b84f35ca8b79af9967a4e1ddab7f2313e705
---

## 问题现象

在Swiper最后一项的尾部设置一个添加按钮，并自定义按钮的大小。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/eD3bcx09SuG7eT1nx1-YMA/zh-cn_image_0000002628758912.png "点击放大")

## 背景知识

[Scroll](../harmonyos-references/ts-container-scroll.md)：可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。

* [scrollEdge](../harmonyos-references/ts-container-scroll.md#scrolledge)：设置滚动到容器的边缘位置。
* [onScrollStop](../harmonyos-references/ts-container-scroll.md#onscrollstop9)：滚动停止时触发回调。
* [onDidScroll](../harmonyos-references/ts-container-scroll.md#ondidscroll12)：滚动事件回调，返回当前帧滚动的偏移量和当前滚动状态。

[Swiper](../harmonyos-references/ts-container-swiper.md)：滑块视图容器，提供子组件滑动轮播显示的能力。其子组件默认填充满Swiper组件，滑动时为整页滑动，不受子组件宽高影响。

## 解决方案

在外层使用Scroll组件，内部依次排列Swiper组件和添加按钮，设置Swiper优先滑动。当Swiper滑动到末尾时，继续滑动的为外层Scroll组件，显示出添加按钮。

* 在Scroll的滚动事件onDidScroll回调中，当Scroll的偏移量offset不为0时，设置Swiper不可滚动，当Scroll的偏移量为0时，重新设置Swiper可以滚动交互，以避免手指往回滑动Scroll时，Swiper也被滑动。
* 在Scroll的滚动停止onScrollStop回调中，根据手指滑动方向，设置Scroll滚动的边缘效果，以实现添加按钮跟随手指滑动的边缘对齐逻辑。

完整示例参考如下：

```ts
@Entry
@Component
struct SwiperButtonDemo {
  private scroller: Scroller = new Scroller();
  @State currentIndex: number = 0;
  @State bgColors: string[] = ['#F1F3F5', '#F1F3F5', '#F1F3F5'];
  @State swiperEnable: boolean = true; // Swiper是否可交互
  @State directionRight: boolean = false; // 控制外层Scroll是否向右滑动

  build() {
    Scroll(this.scroller) {
      Row() {
        Swiper() {
          ForEach(this.bgColors, (item: string, index: number) => {
            Row() {
              Text(`${index}`).fontSize('24fp');
            }
            .justifyContent(FlexAlign.Center)
            .borderRadius('16')
            .backgroundColor(item);
          });
        }
        .index($$this.currentIndex)
        .enabled(this.swiperEnable)
        .loop(false)
        .width('100%')
        .height('25%')
        .nestedScroll(SwiperNestedScrollMode.SELF_FIRST) // Swiper优化Scroll滑动
        .indicator(
          Indicator.dot()
            .selectedItemWidth(10)
            .selectedItemHeight(5)
            .selectedColor('#FFFFFF')
            .color('#80ffffff')
        )
        .itemSpace(6)
        .nextMargin(10)
        .prevMargin(10)
        .effectMode(EdgeEffect.None);

        if (this.bgColors.length < 10) {
          Row() {
            Text(`添加`);
          }
          .onClick(() => {
            this.bgColors.push('#F1F3F5'); // 增加Swiper数据的数量
            this.currentIndex += 1;
          })
          .margin({ 'right': '10vp' })
          .justifyContent(FlexAlign.Center)
          .borderRadius('16')
          .width(100)
          .height(100)
          .backgroundColor('#F1F3F5');
        }
      }.margin({ top: '40vp' });
    }
    .width('100%')
    .scrollable(ScrollDirection.Horizontal)
    .scrollBar(BarState.Off)
    .onDidScroll((xOffset: number) => {
      if (xOffset > 0) {
        this.directionRight = true;
      } else if (xOffset < 0) {
        this.directionRight = false;
      }
      if (this.scroller.currentOffset().xOffset === 0) {
        this.swiperEnable = true;
      } else {
        this.swiperEnable = false;
      }
    })
    .onScrollStop(() => {
      this.scroller.scrollEdge(this.directionRight ? Edge.End : Edge.Top);
    });
  }
}
```
