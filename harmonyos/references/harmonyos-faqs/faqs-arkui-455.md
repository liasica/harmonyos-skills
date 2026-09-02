---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-455
title: 如何控制Tabs内容页单向滑动切换
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何控制Tabs内容页单向滑动切换
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:73334de3d5c349c0b9d3949ecabed7803087b2e9d9d24d4d6e65034178761cc1
---

**背景知识**

[scrollable](../harmonyos-references/ts-container-tabs.md#scrollable)：设置是否可以通过滑动页面进行Tab页面切换，默认支持向左向右两个方向滑动。

gesture：通用属性手势绑定，可绑定[TapGesture](../harmonyos-references/ts-basic-gestures-tapgesture.md)、[LongPressGesture](../harmonyos-references/ts-basic-gestures-longpressgesture.md)、[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)、[PinchGesture](../harmonyos-references/ts-basic-gestures-pinchgesture.md)、[RotationGesture](../harmonyos-references/ts-basic-gestures-rotationgesture.md)、[SwipeGesture](../harmonyos-references/ts-basic-gestures-swipegesture.md)等手势。

**解决方案**

1. 创建活动手势的[PanGestureOptions](../harmonyos-references/ts-basic-gestures-pangesture.md#pangestureoptions)，指定滑动方向为向右滑动。

   panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Right })
2. 给除第一个tab外，其他每个tab的内容父组件绑定gesture滑动手势，指定为第一步创建的panOption。

   .gesture(PanGesture(this.panOption))

示例代码如下：

```typescript
@Component
struct TabsPageSwitching {
  @State currentIndex: number = 0;
  private controller: TabsController = new TabsController();
  private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Right });

  @Builder
  tabBuilder(index: number, name: string) {
    Column() {
      Text(name)
        .fontSize(16)
        .lineHeight(22)
        .margin({ top: 16, bottom: 16 })
        .fontColor(this.currentIndex === index ? Color.Blue : Color.Black)

      Divider()
        .strokeWidth(2)
        .color(Color.Blue)
        .opacity(this.currentIndex === index ? 1 : 0)
    }
    .width('100%')
  }

  build() {
    Column() {
      Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
        TabContent() {
          Column()
            .width('100%')
            .height('100%')
            .backgroundColor(Color.Green)
        }
        .tabBar(this.tabBuilder(0, 'Tab1'))

        TabContent() {
          Column()
            .width('100%')
            .height('100%')
            .backgroundColor(Color.Pink)
            .gesture(PanGesture(this.panOption))
        }
        .tabBar(this.tabBuilder(1, 'Tab2'))

        TabContent() {
          Column()
            .width('100%')
            .height('100%')
            .backgroundColor(Color.Orange)
            .gesture(PanGesture(this.panOption))
        }
        .tabBar(this.tabBuilder(2, 'Tab3'))
      }
      .vertical(false)
      .barMode(BarMode.Fixed)
      .barWidth(360)
      .barHeight(56)
      .animationDuration(200)
      .onChange((index: number) => {
        this.currentIndex = index;
      })
      .width('100%')
      .height(296)
      .margin({ top: 52 })
    }
    .width('100%')
  }
}
```
