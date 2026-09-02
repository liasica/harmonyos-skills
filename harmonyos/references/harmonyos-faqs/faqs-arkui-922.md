---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-922
title: List组件滚动优先级如何高于Scroll组件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > List组件滚动优先级如何高于Scroll组件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b4f499e194ae3eb5d3196a6555598eba24c49bb0d5efff40e28a43583c5bc978
---

## 问题现象

当TabBar吸顶且List组件上滑一段距离后，手指向下拖拽TabBar位置，如何实现以下效果：Scroll组件不进行下滑而是由List组件下滑，当List组件下滑到顶部时再由Scroll组件响应拖拽事件继续下滑。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/VxRaeWg_RXGk8vm2V1ULPA/zh-cn_image_0000002628400300.png "点击放大")

## 背景知识

* [Scroll](../harmonyos-references/ts-container-scroll.md)、[List](../harmonyos-references/ts-container-list.md)都是可滚动的容器组件，组件内部已绑定手势实现跟手滚动等功能，需要增加自定义手势操作时请参考[手势拦截增强](../harmonyos-references/ts-gesture-blocking-enhancement.md)进行处理。
* [onScrollFrameBegin](../harmonyos-references/ts-container-scroll.md#onscrollframebegin9)回调触发时，事件参数传入即将发生的滚动量，事件处理函数中可根据应用场景计算实际需要的滚动量并作为事件处理函数的返回值返回，Scroll将按照返回值的实际滚动量进行滚动。
* [触摸事件onTouch](../harmonyos-references/ts-universal-events-touch.md)是组件的通用事件，在手指触摸动作时触发该回调，回调入参类型为[TouchEvent](../harmonyos-references/ts-universal-events-touch.md#touchevent对象说明)。

## 解决方案

通过触摸事件onTouch记下手指按下的位置，同时判断当前列表是否滚动到顶部，如果当前列表在顶部则允许Scroll组件滚动，否则禁止Scroll组件滚动，并且在onScrollFrameBegin回调中根据scrollable的值判断是否滚动。

onTouch关键部分代码如下：

```ts
.onTouch(event => {
  if (event.type === TouchType.Down) {
    // 当手指按下或滑动时禁用Scroll滚动
    this.scrollable = false;
    this.lastPosition = event.changedTouches[0].y; // 记录手指按下的位置
  }
  if (event.type === TouchType.Up) {
    this.scrollable = true; // 当手指抬起时允许Scroll滚动
  }
  if (event.type === TouchType.Move) {
    // 当手指移动时，手动滚动列表
    this.scrollerForList.scrollBy(0, this.lastPosition - event.changedTouches[0].y);
  }
  if (this.scrollerForList.currentOffset().yOffset === 0) {
    // 当列表滚动到顶部时，允许Scroll滚动
    this.scrollable = true;
  }
});
```

完整示例代码如下：

```ts
@Entry
@Component
struct StickyNestedScroll {
  @State arr: number[] = []; // 用于存储列表项的数据
  private scrollerForList: Scroller = new Scroller(); // 用于控制列表的滚动
  private scrollable: boolean = true; // 判断Scroll是否可以滚动
  private lastPosition: number = 0; // 记录上一次触摸的位置
  private fontColor: string = '#182431';
  private selectedFontColor: string = '#007DFF';
  @State selectedIndex: number = 0;
  @State currentIndex: number = 0;

  @Styles
  listCard() {
    .backgroundColor(Color.White)
    .height(72)
    .width('100%')
    .borderRadius(12);
  }

  @Builder
  tabBuilder(index: number) {
    Text('Tab' + (index + 1))
      .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)
      .fontSize(20)
      .fontWeight(500)
      .lineHeight(14)
      .onTouch(event => {
        if (event.type === TouchType.Down) {
          // 当手指按下或滑动时禁用Scroll滚动
          this.scrollable = false;
          this.lastPosition = event.changedTouches[0].y; // 记录手指按下的位置
        }
        if (event.type === TouchType.Up) {
          this.scrollable = true; // 当手指抬起时允许Scroll滚动
        }
        if (event.type === TouchType.Move) {
          // 当手指移动时，手动滚动列表
          this.scrollerForList.scrollBy(0, this.lastPosition - event.changedTouches[0].y);
        }
        if (this.scrollerForList.currentOffset().yOffset === 0) {
          // 当列表滚动到顶部时，允许Scroll滚动
          this.scrollable = true;
        }
      });
  }

  build() {
    Scroll() {
      Column() {
        Text('Scroll Area')
          .width('100%')
          .height('40%')
          .backgroundColor('#0080DC')
          .textAlign(TextAlign.Center);

        Tabs({ barPosition: BarPosition.Start }) {
          TabContent() {
            List({ space: 10, scroller: this.scrollerForList }) {
              ForEach(this.arr, (item: number) => {
                ListItem() {
                  Text('item' + item)
                    .fontColor($r('sys.color.black'))
                    .fontSize(16)
                    .height(50);
                }.listCard();
              }, (item: string) => item);
            }
            .width('90%')
            .margin({ left: 16, right: 16 })
            .scrollBar(0)
            .edgeEffect(EdgeEffect.Spring)
            .nestedScroll({
              scrollForward: NestedScrollMode.PARENT_FIRST, // 设置向前滚动时的模式
              scrollBackward: NestedScrollMode.SELF_FIRST // 设置向后滚动时的模式
            });
          }.tabBar(this.tabBuilder(0));

          TabContent() {
          }.tabBar(this.tabBuilder(1));
        }
        .onChange((index: number) => {
          // currentIndex控制TabContent显示页签
          this.currentIndex = index;
          this.selectedIndex = index;
        })
        .onAnimationStart((index: number, targetIndex: number) => {
          if (index === targetIndex) {
            return;
          }
          // selectedIndex控制自定义TabBar内Image和Text颜色切换
          this.selectedIndex = targetIndex;
        })
        .vertical(false)
        .height('100%');
      }.width('100%');
    }
    .edgeEffect(EdgeEffect.Spring)
    .friction(0.6) // 设置滚动视图的摩擦力
    .backgroundColor('#DCDCDC')
    .scrollBar(BarState.Off)
    .width('100%')
    .height('100%')
    .onScrollFrameBegin((offset: number) => {
      // 设置滚动视图是否可以滚动
      if (this.scrollable) {
        return { offsetRemain: offset };
      } else {
        return { offsetRemain: 0 };
      }
    });
  }

  aboutToAppear() {
    for (let i = 0; i < 30; i++) {
      this.arr.push(i);
    }
  }
}
```
