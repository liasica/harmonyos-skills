---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-568
title: 如何解决自定义tabBar切换动画有明显延迟感的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决自定义tabBar切换动画有明显延迟感的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:aa49d8b5cc2ab16eeda28efc7ff9bb79b29bb2e5cd23647120c33e37ad60939a
---

## 问题现象

Tabs页面切换时，tabBar切换动画发生的比较慢，需要等到Tabs页面完成切换时，tabBar才发生切换。效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/C5-Im_FvRsmsD49vhMFa5Q/zh-cn_image_0000002628552042.png "点击放大")

## 背景知识

* [Tabs组件](../harmonyos-references/ts-container-tabs.md)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。
* [onChange](../harmonyos-references/ts-container-tabs.md#onchange)：Tab页签切换后触发的事件。
* [onAnimationStart](../harmonyos-references/ts-container-tabs.md#onanimationstart11)：切换动画开始时触发该回调。

## 问题定位

经排查发现，tabBar切换是通过在onChange事件中改变currentIndex实现，onChange回调在页签切换后触发，因此刷新tabBar会慢于TabContent的切换。

```ts
Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
  // ...
}
.vertical(false)
.barMode(BarMode.Fixed)
.animationDuration(400)
.onChange((index: number) => {
  // currentIndex控制TabContent显示页签
  this.currentIndex = index
})
```

## 分析结论

currentIndex改变的时机不正确。

## 修改建议

* 新增一个selectedIndex的索引用于标识被选择的tabBar，原来的currentIndex仍然用于TabContent页签显示的控制。
* selectedIndex的onAnimationStart事件中进行切换，就可以实现页签内容切换动画发生时，tabBar也同步切换。
* 需要注意的是，selectedIndex和currentIndex不能为了方便使用同一个，否则会出现页面切换没有动画的情况。

  ```ts
  @Entry
  @Component
  struct TabsExample {
    unSelectedColor: string = '#ffe8eaec';
    selectedColor: string = '#0A59F7';
    @State currentIndex: number = 0;
    @State selectedIndex: number = 0;
    private controller: TabsController = new TabsController();

    @Builder
    tabBuilder(index: number, name: string) {
      Column({ space: 8 }) {
        Text(name)
          .fontColor(this.selectedIndex === index ? Color.White : Color.Black)
          .fontSize(16)
          .fontWeight(this.selectedIndex === index ? 500 : 400);
      }
      .height(36)
      .padding({
        left: 16,
        right: 16
      })
      .justifyContent(FlexAlign.Center)
      .borderRadius(100)
      .backgroundColor(this.selectedIndex === index ? this.selectedColor : this.unSelectedColor);
    }

    build() {
      Column() {
        Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
          TabContent() {
            Column() {
              Column() {
                Text('顶部页签1内容')
                  .fontSize(16);
              }
              .width('100%')
              .height('33%')
              .borderRadius(16)
              .justifyContent(FlexAlign.Center)
              .backgroundColor(Color.White);
            }
            .height('100%')
            .width('100%')
            .justifyContent(FlexAlign.Start)
            .backgroundColor('#00000')
            .padding({
              top: 12,
              left: 16,
              right: 16
            });
          }
          .tabBar(this.tabBuilder(0, '顶部页签1'));

          TabContent() {
            Column() {
              Column() {
                Text('顶部页签2内容')
                  .fontSize(16);
              }
              .width('100%')
              .height('33%')
              .borderRadius(16)
              .justifyContent(FlexAlign.Center)
              .backgroundColor(Color.White);
            }
            .height('100%')
            .width('100%')
            .justifyContent(FlexAlign.Start)
            .backgroundColor('#00000')
            .padding({
              top: 12,
              left: 16,
              right: 16
            });
          }.tabBar(this.tabBuilder(1, '顶部页签2'));

          TabContent() {
            Column() {
              Column() {
                Text('顶部页签3内容')
                  .fontSize(16);
              }
              .width('100%')
              .height('33%')
              .borderRadius(16)
              .justifyContent(FlexAlign.Center)
              .backgroundColor(Color.White);
            }
            .height('100%')
            .width('100%')
            .justifyContent(FlexAlign.Start)
            .backgroundColor('#00000')
            .padding({
              top: 12,
              left: 16,
              right: 16
            });
          }.tabBar(this.tabBuilder(2, '顶部页签3'));

        }
        .vertical(false)
        .barMode(BarMode.Fixed)
        .barHeight(56)
        .animationDuration(400)
        .onChange((index: number) => {
          // currentIndex控制TabContent显示页签
          this.currentIndex = index;
          this.selectedIndex = index;
        })
        .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
          if (index === targetIndex) {
            return;
          }
          console.info(`event currentOffset ${event.currentOffset}`);
          // selectedIndex控制自定义TabBar内Image和Text颜色切换
          this.selectedIndex = targetIndex;
        });
      }
      .width('100%')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
      .padding({ top: 20 })
      .backgroundColor('#F1F3F5');
    }
  }
  ```

## 常见FAQ

Q：点击切换页签时，图片切换有延迟是什么原因造成的？

A：通常图片加载有延迟与Tabs组件没有直接关系，而是由于进行了大尺寸图片加载，导致图片解码等加载耗时过长造成视觉延迟。建议优化图片的加载策略，如使用缓存图片进行占位以改善视觉延迟等。不同场景下，性能问题会有不同的表现，建议将网络下载部分与Image的显示剥离，可提前下载或者异步下载。详情可参考[预置图片资源加载优化](../best-practices/bpta-texture-compression-improve-performance.md)。

## 总结

要实现Tabs滑动切换动画发生的时候，tabBar也同步进行切换，需要在onAnimationStart事件中进行索引更新，而且标识选中tabBar的索引要和标识选中tab页的索引区分开。
