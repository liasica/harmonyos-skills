---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-632
title: 长列表使用scrollToIndex卡顿问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 长列表使用scrollToIndex卡顿问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:08+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:d2e9558abbb8ccc680d5ee00c9a60b64e2e269caccdd55e7d3761d424faf6a63
---

## 问题现象

使用List和Scroller嵌套实现的长列表使用scrollToIndex()方法跳转跨越过多项时性能低下，如何优化？

```ts
@Entry
@ComponentV2
export struct ListTest {
  private readonly list: string[] = Array
    .from({ length: 2000 }, (_: number, i: number) => i + 1)
    .map((i: number) => `index: ${i}`);
  private readonly scroller: Scroller = new Scroller();

  build() {
    Column() {
      Row({ space: 10 }) {
        Button('scroll to top').onClick(() => this.scroller.scrollToIndex(0, true)).fontSize(13);
        Button('scroll to bottom').onClick(() => this.scroller.scrollToIndex(this.list.length - 1, true)).fontSize(13);
        Button('jump 1000').onClick(() => this.scroller.scrollToIndex(1000, false)).fontSize(13);
      }
      .width('100%')
      .margin({ left: 25 });

      List({
        scroller: this.scroller,
      }) {
        Repeat(this.list)
          .key((item: string) => item)
          .virtualScroll({ totalCount: this.list.length })
          .templateId(() => '1')
          .template('1', (repeatItem: RepeatItem<string>) => {
            ListItem() {
              Text(repeatItem.item)
                .width('100%')
                .height(50)
                .padding(5)
                .textAlign(TextAlign.Center);
            };
          })
          .each((repeatItem: RepeatItem<string>) => {
            ListItem() {
              Text(repeatItem.item)
                .width('100%')
                .height(50)
                .padding(5);
            };
          });
      }
      .width('100%')
      .layoutWeight(1);
    }
    .backgroundColor(Color.White);
  }
}
```

## 背景知识

* 使用工具Profiler查看性能参数可以参考[使用Profiler进行性能调优](../harmonyos-guides/ide-profiler-introduction.md)。
* [currentOffset](../harmonyos-references/ts-container-scroll.md#currentoffset)可以用来获取当前的滚动偏移量。
* [scrollToIndex](../harmonyos-references/ts-container-scroll.md#scrolltoindex)开启smooth动效时，会对经过的所有item进行加载和布局计算，当大量加载item时会导致性能问题，导致整个列表卡顿。

## 解决方案

* 可以采用先调用scrollToIndex关闭动画跳转到目标附近位置，再调用scrollToIndex开启动画滚动到目标位置的间接跳转的方式，优化性能。

  以纵向滚动的5000个元素的长列表，调用scroller反复滚动到列表顶部和底部为例。

  ```ts
  @Entry
  @ComponentV2
  export struct virtrulScroll {
    private itemHeight: number = 50;
    private readonly list: string[] = Array
      .from({ length: 5000 }, (_: number, i: number) => i + 1)
      .map((i: number) => `index: ${i}`);
    private readonly scroller: Scroller = new Scroller();

    build() {
      Column() {
        Row({ space: 10 }) {
          Button('scroll to top')
            .fontSize(13)
            .onClick(() => {
              // 用currentOffset().yOffset获取当前滑动偏移量除以单项高度获得index做判断，离目标位置超过200项则以关闭动效先滚动到目标位置附近
              if (this.scroller.currentOffset().yOffset / this.itemHeight >= 200) {
                this.scroller.scrollToIndex(200, false);
              }
              this.scroller.scrollToIndex(0, true);
            });
          Button('scroll to bottom')
            .fontSize(13)
            .onClick(() => {
              if (this.scroller.currentOffset().yOffset / this.itemHeight <= this.list.length - 200) {
                this.scroller.scrollToIndex(this.list.length - 200, false);
              }
              this.scroller.scrollToIndex(this.list.length - 1, true);
            });
          Button('jump 1000')
            .fontSize(13)
            .onClick(() => {
              console.info('currentoffset: ', this.scroller.currentOffset().yOffset);
              this.scroller.scrollToIndex(1000, false);
            });
        };

        List({
          scroller: this.scroller,
        }) {
          Repeat(this.list)
            .key((item: string) => item)
            .virtualScroll({ totalCount: this.list.length })
            .templateId(() => '1')
            .template('1', (repeatItem: RepeatItem<string>) => {
              ListItem() {
                Text(repeatItem.item)
                  .width('100%')
                  .height(this.itemHeight)
                  .padding(5)
                  .textAlign(TextAlign.Center);
              };
            })
            .each((repeatItem: RepeatItem<string>) => {
              ListItem() {
                Text(repeatItem.item)
                  .width('100%')
                  .height(this.itemHeight)
                  .padding(5);
              };
            });
        }
        .width('100%')
        .height(200)
        .layoutWeight(1);
      }.backgroundColor(Color.White);
    }
  }
  ```
* 开动效直接跳到目标位置和先关动效跳到附近位置再开启动效跳转到目标位置对比，通过DevEco Studio的Profiler抓取launch数据可以得到如下，可以明显看出实现了性能优化。
  + 直接跳转：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/HCTDB0nsSiyIYyyA7h0NuA/zh-cn_image_0000002658793543.png "点击放大")
  + 间接跳转：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/wGxKuxomQJ25RM18Jqj9yA/zh-cn_image_0000002628554176.png "点击放大")
  + 数据对比：

    | 对比数据 | 直接跳转 | 间接跳转 |
    | --- | --- | --- |
    | 布局任务数量LayoutTasks/个 | 4968 | 185 |
    | 布局时间/ms | 518.811 | 16.480 |
  + 实际运行效果比较：

    | 优化前 | 优化后 |
    | --- | --- |
    |  |  |
