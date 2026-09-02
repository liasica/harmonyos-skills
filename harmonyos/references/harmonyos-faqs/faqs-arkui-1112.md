---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1112
title: 如何设置TabContent切换动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何设置TabContent切换动画
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:dc5e80b3524b19a75f2dfc4cffee49582665a897ea415bf1aa06b2652317bc27
---

## 问题现象

场景一：TabContent切换如何实现渐隐渐显的动画效果？

场景二：点击页签，TabContent有左右切换效果，A、B、C三个页面，B页面居中，左滑A宽80%拼接B左侧20%，右滑同理。

## 背景知识

* [Tabs](../harmonyos-references/ts-container-tabs.md)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。
* [onAnimationEnd](../harmonyos-references/ts-container-tabs.md#onanimationend11)：切换动画结束时触发该回调，包括动画过程中手势中断。当animationDuration为0时动画关闭，不触发该回调。
* [customContentTransition](../harmonyos-references/ts-container-tabs.md#customcontenttransition11)：自定义Tabs页面切换动画。
* [onGestureSwipe](../harmonyos-references/ts-container-tabs.md#ongestureswipe11)：在页面跟手滑动过程中，逐帧触发该回调。
* [onTabBarClick](../harmonyos-references/ts-container-tabs.md#ontabbarclick10)：Tab页签点击后触发的事件。
* [Scroll](../harmonyos-references/ts-container-scroll.md)：可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
* [scrollTo](../harmonyos-references/ts-container-scroll.md#scrollto)：滑动到指定位置。
* [currentOffset](../harmonyos-references/ts-container-scroll.md#currentoffset)：获取当前的滚动总偏移量。
* [friction](../harmonyos-references/ts-container-scroll.md#friction10)：设置摩擦系数。
* [scrollSnap](../harmonyos-references/ts-container-scroll.md#scrollsnap10)：设置Scroll组件的限位滚动模式。

## 解决方案

**场景一：实现渐隐渐显的动画效果。**

* 方案一：通过customContentTransition实现。

  [customContentTransition](../harmonyos-references/ts-container-tabs.md#customcontenttransition11)提供自定义Tabs页面切换动画的能力，实现渐隐渐显动画，开发者可参考[示例8（自定义Tabs页面切换动画）](../harmonyos-references/ts-container-tabs.md#示例8自定义tabs页面切换动画)。
* 方案二：通过onGestureSwipe实现。

1. 监听页面手势滑动，计算滑动进度，实时修改页面的透明度、缩放等属性，实现拖拽动效。
2. 滑动结束后，重置页面样式，完成释放自动回弹还原的平滑过渡。
3. 点击页签通过onTabBarClick执行新旧页面切换动效。

参考代码如下所示：

```ts
@Entry
@Component
struct FadePage {
  private durationList: number[] = [];
  private barList: string[] = ['#33000000', '#1a000000', '#0d000000'];
  private isRestAnim: boolean = false; // 滑动回弹动画是否正在执行
  @State opacityList: number[] = [];
  @State scaleList: number[] = [];
  @State currentIndex: number = 0;

  // 点击Tab渐显渐隐
  private clickTabHandle(from: number, to: number) {
    // 页面重复点击，直接拦截
    if (from === to) {
      return;
    }
    // 如果回弹动画正在进行：强制终止、重置
    if (this.isRestAnim) {
      // 清空滑动残留的中间插值状态
      for (let i = 0; i < this.barList.length; i++) {
        this.scaleList[i] = i === from ? 1 : 0.9;
        this.opacityList[i] = i === from ? 1 : 0;
      }
      // 强制关闭回弹动画
      this.isRestAnim = false;
    }
    // 新页面初始状态
    this.opacityList[to] = 0;
    this.scaleList[to] = 0.9;
    this.getUIContext().animateTo({ duration: this.durationList[from], curve: Curve.EaseOut }, () => {
      // 原页面：透明淡出+缩小
      this.opacityList[from] = 0;
      this.scaleList[from] = 0.9;
      // 目标页面：透明淡入+放大
      this.opacityList[to] = 1;
      this.scaleList[to] = 1;
      this.currentIndex = to;
    });
  }

  // 滑动跟手渐显渐隐
  private gestureSwiperHandle(curIndex: number, event: TabsAnimationEvent) {
    let offset = event.currentOffset;
    // 判断左右滑动
    let targetIndex = offset > 0 ? curIndex - 1 : curIndex + 1;
    if (targetIndex < 0 || targetIndex >= this.opacityList.length) {
      return;
    }
    // 跟手进度计算
    let progress = Math.min(Math.abs(offset) / 300, 1);
    // 当前页面
    this.opacityList[curIndex] = 1 - progress;
    this.scaleList[curIndex] = 1 - progress * 0.1;
    // 目标页面
    this.opacityList[targetIndex] = progress;
    this.scaleList[targetIndex] = 0.9 + progress * 0.1;
  }

  // 滑动回弹复原
  private resetStyle(from: number, to: number) {
    // 开启回弹动画
    this.isRestAnim = true;
    this.getUIContext().animateTo({
      duration: this.durationList[from], curve: Curve.EaseOut, onFinish: () => {
        // 动画结束时关闭回弹动画
        this.isRestAnim = false;
      }
    }, () => {
      for (let i = 0; i < this.barList.length; i++) {
        this.scaleList[i] = i === to ? 1 : 0.9;
        this.opacityList[i] = i === to ? 1 : 0;
      }
    });
  }

  aboutToAppear(): void {
    let duration = 1000;
    for (let i = 1; i <= this.barList.length; i++) {
      this.opacityList.push(1.0);
      this.scaleList.push(1.0);
      this.durationList.push(duration * i);
    }
  }

  build() {
    Column() {
      Tabs() {
        ForEach(this.barList, (item: string, index: number) => {
          TabContent()
            .tabBar(`页签${index + 1}`)
            .backgroundColor(item)
            // 自定义动画变化透明度、缩放页面等
            .opacity(this.opacityList[index])
            .scale({ x: this.scaleList[index], y: this.scaleList[index] });
        });
      }
      .scrollable(true)
      .onAnimationEnd((index: number) => {
        this.resetStyle(this.currentIndex, index);
        this.currentIndex = index;
      })
      .onGestureSwipe((index: number, event: TabsAnimationEvent) => {
        this.gestureSwiperHandle(index, event);
      })
      .onTabBarClick((toIndex: number) => {
        let fromIndex = this.currentIndex;
        this.clickTabHandle(fromIndex, toIndex);
      });
    }
    .width('100%')
    .height('100%');
  }
}
```

效果图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/15kv_gfBTROrVG8GByiNAA/zh-cn_image_0000002658926707.png "点击放大")

* **场景二：点击页签，TabContent有左右切换效果，A、B、C三个页面，B页面居中，左滑A宽80%拼接B左侧20%，右滑同理。**

  Tabs组件无法实现页面拼接。可通过以下处理：

  1. 通过使用Scroll组件开启水平滚动，承载A、B、C三个页面。Tabs的TabBar作为页签栏，通过[visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)对TabContent进行隐藏。
  2. 通过[ScrollSnapOptions](../harmonyos-references/ts-container-scroll.md#scrollsnapoptions10对象说明)的snapPagination属性，设置Scroll组件限位滚动时的分页点，实现三个页面不同宽度的处理。
  3. 滚动结束后，触发[onScrollStop](../harmonyos-references/ts-container-scroll.md#onscrollstop9)回调，通过水平偏移量结合屏幕宽度，判断当前应当停留的目标页面，并同步更新页签索引值。

  参考代码如下所示：

  ```ts
  import { display } from '@kit.ArkUI';

  class DataItem {
    id?: number;
    name?: string;
    bg?: string;
    pageWidth?: string;

    constructor(id?: number, name?: string, bg?: string, pageWidth?: string) {
      this.id = id;
      this.name = name;
      this.bg = bg;
      this.pageWidth = pageWidth;
    }
  }

  @Entry
  @Component
  struct MatchPage {
    private scroller: Scroller = new Scroller();
    private dataList: DataItem[] = [
      new DataItem(0, 'A页面', '#33000000', '80%'),
      new DataItem(1, 'B页面', '#1a000000', '100%'),
      new DataItem(0, 'C页面', '#03000000', '80%')
    ];
    // 屏幕宽度
    private screenX: number = 0;
    // 三个页面滚动停靠位置
    private pagePersent: number[] = [0, 0.8, 1.8];
    // 页面区域判定阈值
    private pivotPersent: number[] = [0.4, 1.3];
    @State currentIndex: number = 1; // 当前页面索引

    aboutToAppear(): void {
      let screenWidthPx = display.getDefaultDisplaySync().width;
      this.screenX = this.getUIContext().px2vp(screenWidthPx);
    }

    build() {
      Column() {
        Tabs({ index: this.currentIndex }) {
          ForEach(this.dataList, (item: DataItem) => {
            TabContent()
              .tabBar(`${item.name}`)
              .visibility(Visibility.None);
          });
        }
        .barHeight(100)
        .width('100%')
        .height(100)
        .onChange((index: number) => {
          this.currentIndex = index;
          this.scroller.scrollTo({
            xOffset: this.pagePersent[index] * this.screenX,
            yOffset: 0,
            animation: { duration: 500 }
          });
        });

        Scroll(this.scroller) {
          Row() {
            ForEach(this.dataList, (item: DataItem) => {
              PageContent({ data: item });
            });
          }
          .height('100%');
        }
        .width('100%')
        .layoutWeight(1)
        .scrollBar(BarState.Off)
        .scrollable(ScrollDirection.Horizontal)
        // 设置摩擦系数
        .friction(10)
        // 限位滚动时的分页点
        .scrollSnap({
          snapAlign: ScrollSnapAlign.START,
          snapPagination: ['0%', '80%', '180%'],
          enableSnapToStart: true,
          enableSnapToEnd: true
        })
        .initialOffset({ xOffset: '80%', yOffset: 0 })
        .onScrollStop(() => {
          let offsetX = this.scroller.currentOffset().xOffset;
          let ratio = offsetX / this.screenX;
          // 根据滚动偏移判断当前落到哪个页面区间
          if (ratio < this.pivotPersent[0]) {
            this.currentIndex = 0;
          } else if (ratio < this.pivotPersent[1]) {
            this.currentIndex = 1;
          } else {
            this.currentIndex = 2;
          }
        });
      }
      .width('100%')
      .height('100%');
    }
  }

  @Component
  struct PageContent {
    data: DataItem = new DataItem();

    build() {
      Column() {
        Text(this.data.name)
          .fontSize(24)
          .fontSize(24)
          .fontWeight(FontWeight.Medium);
      }
      .width(this.data.pageWidth)
      .height('100%')
      .backgroundColor(this.data.bg)
      .justifyContent(FlexAlign.Center);
    }
  }
  ```

  效果图如下所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/PnLivEn6Tmi3i7fX59UOgA/zh-cn_image_0000002658806749.png "点击放大")

## 常见FAQ

Q：AnimationMode.NO\_ANIMATION关闭默认动画不起作用，如何解决？

A：可通过设置[animationDuration](../harmonyos-references/ts-container-tabs.md#animationduration)为0。
