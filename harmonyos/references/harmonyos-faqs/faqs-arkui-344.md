---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-344
title: 如何在Tabs的tabBar中添加其他组件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何在Tabs的tabBar中添加其他组件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:221a25d6893a1b9c2305a46853be29f25b264f9a30784eea85fbeb41014f93fc
---

标准Tabs组件不支持在tabBar中添加其他组件，但通过自定义Tabs可实现该需求。

示例代码如下：

```ts
import { componentUtils } from '@kit.ArkUI';

@Entry
@Component
struct TabsDemo {
  @State tabArray: Array<number> = [0, 1, 2];
  @State lastTabIndex: number = this.tabArray.length - 1;
  @State currentIndex: number = 0;
  @State animationDuration: number = 300;
  @State indicatorLeftMargin: number = 0;
  @State indicatorWidth: number = 0;
  private controller: TabsController = new TabsController();
  private tabsWidth: number = 0;

  // Single tab
  @Builder
  tab(tabName: string, tabItem: number, tabIndex: number) {
    Row({ space: 20 }) {
      Text(tabName).fontSize(18)
        .fontColor(tabItem === this.currentIndex ? Color.Red : Color.Black)
        .id(tabIndex.toString())
        .onAreaChange((oldValue: Area, newValue: Area) => {
          if (this.currentIndex === tabIndex && (this.indicatorLeftMargin === 0 || this.indicatorWidth === 0)) {
            if (newValue.position.x !== undefined) {
              let positionX = Number.parseFloat(newValue.position.x.toString());
              this.indicatorLeftMargin = Number.isNaN(positionX) ? 0 : positionX;
            }
            let width = Number.parseFloat(newValue.width.toString());
            this.indicatorWidth = Number.isNaN(width) ? 0 : width;
          }
        })
    }
    .justifyContent(FlexAlign.Center)
    .constraintSize({ minWidth: 35 })
    .width(80)
    .height(35)
    .borderRadius({
      topLeft: 10,
      topRight: 10
    })
    .onClick(() => {
      this.controller.changeIndex(tabIndex);
      this.currentIndex = tabIndex;
    })
  }

  build() {
    Column() {
      // Tab bar
      Stack({ alignContent: Alignment.TopStart }) {
        Scroll() {
          Row() {
            ForEach(this.tabArray, (item: number, index: number) => {
              this.tab('Tab' + item, item, index);
            })
            Text('+')
              .width(36)
              .height(50)
              .fontSize(28)
              .borderRadius(5)
              .padding({
                left: 5,
                bottom: 2
              })
              .onClick(() => {
                if (this.tabArray.length < 1000) {
                  this.tabArray.push(++this.lastTabIndex);
                }
              })
          }
          .justifyContent(FlexAlign.SpaceBetween)
        }
        .align(Alignment.Start)
        .scrollable(ScrollDirection.Horizontal)
        .scrollBar(BarState.Off)
        .width('100%')

        Column()
          .width(this.indicatorWidth)
          .height(2)
          .backgroundColor(Color.Red)
          .borderRadius(2)
          .margin({
            left: this.indicatorLeftMargin,
            top: 38
          })
      }
      .width('100%')

      Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {
        ForEach(this.tabArray, (item: number, index: number) => {
          TabContent() {
            Text('I am the content of page ' + item)
              .height(300)
              .width('100%')
              .fontSize(30)
              .textAlign(TextAlign.Center)
          }
          .backgroundColor(Color.Pink)
        })
      }
      .onAreaChange((oldValue: Area, newValue: Area) => {
        let width = Number.parseFloat(newValue.width.toString());
        this.tabsWidth = Number.isNaN(width) ? 0 : width;
      })
      .barWidth('100%')
      .barHeight(0)
      .width('100%')
      .height('100%')
      .backgroundColor('#F1F3F5')
      .animationDuration(this.animationDuration)
      .onChange((index: number) => {
        this.currentIndex = index; // Listen for index changes to switch tab content.
      })
      .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
        // Callback when the switching animation starts. The underline slides with the page and the width changes.
        this.currentIndex = targetIndex;
        let targetIndexInfo = this.getTextInfo(targetIndex);
        this.startAnimateTo(this.animationDuration, targetIndexInfo.left, targetIndexInfo.width);
      })
      .onAnimationEnd((index: number, event: TabsAnimationEvent) => {
        // Callback when the switching animation ends. The underline animation stops.
        let currentIndicatorInfo = this.getCurrentIndicatorInfo(index, event);
        this.startAnimateTo(0, currentIndicatorInfo.left, currentIndicatorInfo.width);
      })
      .onGestureSwipe((index: number, event: TabsAnimationEvent) => {
        // Callback triggered frame by frame during page swipe.
        let currentIndicatorInfo = this.getCurrentIndicatorInfo(index, event);
        this.currentIndex = currentIndicatorInfo.index;
        this.indicatorLeftMargin = currentIndicatorInfo.left;
        this.indicatorWidth = currentIndicatorInfo.width;
      })
    }
    .height('100%')
  }

  // Get component size, position, translation, scaling, rotation, and affine matrix attribute information.
  private getTextInfo(index: number): Record<string, number> {
    let modePosition: componentUtils.ComponentInfo =
      this.getUIContext().getComponentUtils().getRectangleById(index.toString());
    return {
      'left': this.getUIContext().px2vp(modePosition?.windowOffset?.x ?? 0),
      'width': this.getUIContext().px2vp(modePosition.size.width)
    };
  }

  /*
   * Calculate indicator dynamic position information
   * @param index Current page index
   * @param event Swipe event object
   * @returns {left: Indicator left shift, width: Indicator width, index: Target page index}
   */
  private getCurrentIndicatorInfo(index: number, event: TabsAnimationEvent): Record<string, number> {
    let nextIndex = index;
    if (index > 0 && event.currentOffset > 0) {
      nextIndex--;
    } else if (index < 3 && event.currentOffset < 0) {
      nextIndex++;
    }
    let indexInfo = this.getTextInfo(index);
    let nextIndexInfo = this.getTextInfo(nextIndex);
    let swipeRatio = Math.abs(event.currentOffset / this.tabsWidth);
    // When page sliding exceeds half, tabBar switches to the next page.
    let currentIndex = swipeRatio > 0.5 ? nextIndex : index;
    let currentLeft = indexInfo.left + (nextIndexInfo.left - indexInfo.left) * swipeRatio;
    let currentWidth = indexInfo.width + (nextIndexInfo.width - indexInfo.width) * swipeRatio;
    return { 'index': currentIndex, 'left': currentLeft, 'width': currentWidth };
  }

  private startAnimateTo(duration: number, leftMargin: number, width: number) {
    this.getUIContext().animateTo({
      // Animation duration
      duration: duration,
      // Animation curve
      curve: Curve.Linear,
      // Number of iterations
      iterations: 1,
      // Animation mode
      playMode: PlayMode.Normal,
      onFinish: () => {
        console.info('play end');
      }
    }, () => {
      this.indicatorLeftMargin = leftMargin;
      this.indicatorWidth = width;
    })
  }
}
```
