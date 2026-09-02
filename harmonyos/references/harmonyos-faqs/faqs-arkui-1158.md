---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1158
title: List如何实现滑动翻页效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > List如何实现滑动翻页效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e31584a4d2078c78d84dd241ea150ba0d0f1f98ce53b93d531f7caa4e6c58819
---

## 问题现象

List有无enablePaging类似的方法？Scroll嵌套List后的enablePaging会失效吗？

## 背景知识

* [List](../harmonyos-references/ts-container-list.md)列表包含一系列相同宽度的列表项。
* [Scroll](../harmonyos-references/ts-container-scroll.md)可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
  + [enablePaging](../harmonyos-references/ts-container-scroll.md#enablepaging11)设置是否支持滑动翻页。如果同时设置了滑动翻页enablePaging和限位滚动scrollSnap，则scrollSnap优先生效。List没有类似方法。
* [Scroller](../harmonyos-references/ts-container-scroll.md#scroller)可滚动容器组件的控制器，可以将此组件绑定至容器组件，如Scroll、List等。
  + [scrollTo](../harmonyos-references/ts-container-scroll.md#scrollto)滑动到指定位置，可设置滑动的动画效果。
  + [currentOffset](../harmonyos-references/ts-container-scroll.md#currentoffset)获取当前的滚动偏移量。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)组件区域变化时触发该回调，可获取组件的尺寸信息。
* [onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)手指触摸动作触发该回调。包含触摸类型，触摸点坐标等信息。

## 解决方案

* **方案一**：在外层使用Scroll包裹List组件，用Scroll的enablePaging方法替代。**内层的List不能设置滚动方向上的组件长度**，否则enablePaging方法会失效。示例代码如下：此时List本身是不可滚动的，外层Scroll可以滚动。

  ```ts
  @Entry
  @Component
  struct ScrollSolution {
    private arr: number[] = new Array(30).fill(0);
    private scroller: Scroller = new Scroller();
    @State centerIndex: number = 0;

    build() {
      Column() {
        Scroll() {
          List({ space: 20, scroller: this.scroller }) {
            ForEach(this.arr, (item: number, index: number) => {
              ListItem() {
                Text(`Item ${index}`)
                  .width('100%')
                  .height(100)
                  .fontSize(16)
                  .textAlign(TextAlign.Center)
                  .borderRadius(10)
                  .backgroundColor(this.centerIndex === index ? '#0A59F7' : '#F1F3F5');
              }
              .onClick(() => {
                this.centerIndex = index;
                this.scroller.scrollToIndex(this.centerIndex, true, ScrollAlign.CENTER);
              });
            }, (item: number) => item.toString());
          }
          // 上下滚动，不能设置List的高度，否则Scroll的enablePaging会失效
          .width('100%');
        }
        .enablePaging(true) // 滑动翻页
        .friction(0.8) // 设置摩擦系数
        .width('100%')
        .height('100%');
      }.margin('20vp');
    }
  }
  ```

  效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/A9WV98ENTuK_FUzNlmC2tA/zh-cn_image_0000002628569770.png "点击放大")
* **方案二**：自定义实现List翻页效果。通过onAreaChange获取List的高度，在onTouch回调中实现滑动翻页逻辑，手指按下时，获取当前List的滚动偏移量，手指抬起时，根据手指滑动方向决定向前或向后滚动一个List高度的距离。示例代码如下：翻页判定条件为手指滑动List的距离超过List高度的三分之一。

  ```ts
  @Entry
  @Component
  struct ListSolution {
    private arr: number[] = new Array(30).fill(0);
    private scroller: Scroller = new Scroller();
    @State centerIndex: number = 0;
    @State listHeight: number = 0;
    @State listWidth: number = 0;
    @State listOffset: number = 0; // List偏移量

    build() {
      Column() {
        List({ space: 20, scroller: this.scroller }) {
          ForEach(this.arr, (item: number, index: number) => {
            ListItem() {
              Text(`Item ${item + index}`)
                .width('100%')
                .height(100)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .borderRadius(10)
                .backgroundColor(this.centerIndex === index ? '#0A59F7' : '#F1F3F5');
            }
            .onClick(() => {
              this.centerIndex = index;
              // 点击某一项，此项移动至屏幕中间
              this.scroller.scrollToIndex(this.centerIndex, true, ScrollAlign.CENTER);
            });
          }, (item: number) => item.toString());
        }
        .edgeEffect(EdgeEffect.None)
        .onAreaChange((oldValue: Area, newValue: Area) => {
          console.info(`${JSON.stringify(oldValue)} ${JSON.stringify(newValue)}`);
          this.listHeight = newValue.height as number;
          this.listWidth = newValue.width as number;
        })
        .onTouch((event: TouchEvent) => {
          if (event.type === TouchType.Down) {
            // 记录手指按下时的偏移量
            this.listOffset = this.scroller.currentOffset().yOffset;
            console.info(`this.currentOffset ${this.listOffset}`);
          }
          if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
            // 滑动距离超过页面三分之一则整页滚动
            let curOffset: number = this.scroller.currentOffset().yOffset - this.listOffset;
            let targetOffset = this.listOffset;
            if (Math.abs(curOffset) < this.listHeight / 3) {
              targetOffset = this.listOffset;
            } else if (curOffset > 0) {
              targetOffset = this.listOffset + this.listHeight;
            } else if (curOffset < 0) {
              targetOffset = this.listOffset - this.listHeight;
            }
            console.info(`targetOffset ${targetOffset} listOffset ${curOffset} `);
            this.scroller.scrollTo({
              xOffset: 0,
              yOffset: targetOffset,
              animation: true
            });
          }
        })
        .height('100%')
        .width('100%');
      }.margin('20vp');
    }
  }
  ```

  效果如下：实现整页滑动以及点击Item自动移动至屏幕中间：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/4dnMsawLQ4uMuGoLTIDynw/zh-cn_image_0000002628409866.png "点击放大")
