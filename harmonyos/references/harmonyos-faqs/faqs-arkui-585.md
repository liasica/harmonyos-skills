---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-585
title: 如何实现文字轮播卡片
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现文字轮播卡片
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:aa2c634f1921cdd4dadcce17a405ddaa02c522c70e160b6a751d49c35b6c4e15
---

## 问题现象

实现文字轮播卡片功能时，如何确保在文字滚动至控件边界时暂停滚动，并同步等待其他文字轮播动画结束，以实现动画间的协调控制。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/1-dvoCAZTkSvhJs_GmC1Ww/zh-cn_image_0000002658911715.png "点击放大")

## 背景知识

* [Scroll](../harmonyos-references/ts-container-scroll.md)：可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
* [Scroller](../harmonyos-references/ts-container-scroll.md#scroller)：可滚动容器组件的控制器，可以将此组件绑定至容器组件，然后通过它控制容器组件的滚动。

## 解决方案

通过Scroller控制Scroll滑动并添加动画效果，实现类似跑马灯的文字轮播效果。同时，设置定时器实现自动滚动，利用Scroller的[isAtEnd](../harmonyos-references/ts-container-scroll.md#isatend10)方法监听滚动状态，判断组件是否已滚动到底部，以此确定文字是否已完全展示。

```ts
// 入口组件
@Entry
@Component
struct MarqueePage {
  @State textList: string[] = [
    'this is a test string1 this is a test string1 this is a test string1.',
    'this is a test string2 this is a test string2.',
    'this is a test string3 this is a test string3 this is a test string3 this is a test string3.',
  ];

  build() {
    Row() {
      Column() {
        myMarqueeCard({
          textList: this.textList,
        });
      }
      .width('100%');
    }
    .height('100%');
  }
}
```

```ts
// 自定义走马灯效果
@Component
export struct myMarqueeCard {
  @Prop textList: string[];
  scroller1: Scroller = new Scroller();
  scroller2: Scroller = new Scroller();
  scroller3: Scroller = new Scroller();

  build() {
    Column() {
      this.SingleText(this.textList[0], this.scroller1);
      this.SingleText(this.textList[1], this.scroller2);
      this.SingleText(this.textList[2], this.scroller3);
    };
  }

  @Builder
  SingleText(text: string, scroller: Scroller) {
    Scroll(scroller) {
      Row() {
        Text(text).fontSize(30);
      };
    }
    .width(300)
    .scrollable(ScrollDirection.Horizontal)
    .enableScrollInteraction(false)
    .scrollBar(BarState.Off)
    .onAppear(() => {
      this.handleScroll(scroller);
    });
  }

  handleScroll(scroller: Scroller) {
    let timer: number = setInterval(() => {
      const curOffset: OffsetResult = scroller.currentOffset();
      scroller.scrollTo({
        xOffset: curOffset.xOffset + 50, yOffset: curOffset.yOffset, animation: {
          duration: 1000,
          curve: Curve.Linear
        }
      });
      if (scroller.isAtEnd()) {
        clearInterval(timer);
        if (this.scroller1.isAtEnd() && this.scroller2.isAtEnd() && this.scroller3.isAtEnd()) {
          this.scroller1.scrollTo({ xOffset: 0, yOffset: 0, animation: { duration: 0 } });
          this.scroller2.scrollTo({ xOffset: 0, yOffset: 0, animation: { duration: 0 } });
          this.scroller3.scrollTo({ xOffset: 0, yOffset: 0, animation: { duration: 0 } });
        }
      }
    }, 500);
  }
}
```
