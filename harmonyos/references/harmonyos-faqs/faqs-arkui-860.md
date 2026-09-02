---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-860
title: 鼠标无法滑动Scroll组件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 鼠标无法滑动Scroll组件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0a1f208f9b77cd628b735fdf4d2b3e338cea5911ca85d1f08ef94f7c98c9c114
---

## 问题现象

List组件嵌套Scroll组件布局，List组件竖向滚动，ListItem内嵌套一个横向滚动、隐藏滚动条的Scroll组件，外接鼠标按下左键拖拽或滚动滚轮均无法操作Scroll组件滑动。

## 背景知识

* [Scroll](../harmonyos-references/ts-container-scroll.md)：可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
  + [scrollable](../harmonyos-references/ts-container-scroll.md#scrollable)：设置滚动方向。
  + [scrollBar](../harmonyos-references/ts-container-scroll.md#scrollbar)：设置滚动条状态。
* [Scroller](../harmonyos-references/ts-container-scroll.md#scroller)：
  + [scrollTo](../harmonyos-references/ts-container-scroll.md#scrollto)：滑动到指定位置。
  + [currentOffset](../harmonyos-references/ts-container-scroll.md#currentoffset)：获取当前的滚动偏移量。
* [gesture](../harmonyos-references/ts-gesture-settings.md#gesture)：绑定手势。
* [PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)：滑动手势事件，当滑动的最小距离达到设定的最小值时触发滑动手势事件。
  + [onActionUpdate](../harmonyos-references/ts-basic-gestures-pangesture.md#onactionupdate)：Pan手势移动过程中回调。

## 问题定位

1. 检查触屏操作时，List组件内的Scroll组件是否可正常响应滑动手势进行滚动。
2. 检查当Scroll组件外层没有其他滚动组件时，鼠标左键按下滑动和滚动滚轮是否可以控制Scroll组件滚动。
3. 检查当List组件内的Scroll组件有滚动条时，鼠标左键按下滚动条是否可以控制Scroll组件滚动。

## 分析结论

1. 仅当滚动条存在时，Scroll组件才能通过滚动条响应鼠标左键按下滑动事件进行滚动，滚动条隐藏时Scroll组件默认不响应鼠标左键按下滑动事件。
2. 当Scroll组件的上层不存在其他滚动组件时，Scroll组件能够响应鼠标滚轮滚动事件进行滚动；当Scroll组件的上层存在其他滚动组件（如List）时，鼠标滚轮滚动事件会被上层的滚动组件优先响应（List滚动）并拦截，导致Scroll组件无法响应鼠标滚轮滚动事件。

## 修改建议

给Scroll组件绑定[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)滑动手势事件来响应鼠标左键按下滑动事件，调用[Scroller](../harmonyos-references/ts-container-scroll.md#scroller)的[scrollTo](../harmonyos-references/ts-container-scroll.md#scrollto)方法实现Scroll组件跟随滚动。示例代码如下：

```ts
@Entry
@Component
struct MousePage {
  @State arr: number[] = [];
  scrollers: Scroller[] = [];

  aboutToAppear(): void {
    // 循环调用10次，初始化用于循环渲染ListItem的数组及用于控制Scroll组件的控制器数组
    for (let i = 0; i < 10; i++) {
      this.arr.push(i);
      this.scrollers.push(new Scroller());
    }
  }

  build() {
    Column() {
      List({ space: 10 }) {
        ListItem() {
          Text('Header');
        };

        ForEach(this.arr, (item: number, index: number) => {
          ListItem() {
            this.RowContent(item, this.scrollers[index]);
          };
        });
      }
      .scrollBar(BarState.Off)
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM]);
    }
    .height('100%')
    .width('100%')
    .padding({ left: 16, right: 16 });
  }

  @Builder
  RowContent(i: number, scroller: Scroller) {
    Row() {
      Text(i + 'AAAA')
        .width(80);
      Scroll(scroller) {
        Row({ space: 20 }) {
          Text('1111');
          Text('2222');
          Text('3333');
          Text('4444');
          Text('5555');
          Text('6666');
          Text('7777');
          Text('8888');
          Text('9999');
        }
        .backgroundColor(0xF1F3F5)
        .height(100);
      }
      .borderRadius(12)
      .margin({ right: 16 })
      .scrollable(ScrollDirection.Horizontal) // 设置Scroll组件横向滚动
      .scrollBar(BarState.Off) // 设置Scroll组件隐藏滚动条
      .gesture( // 给Scroll组件绑定PanGesture滑动手势事件
        PanGesture(new PanGestureOptions({ direction: PanDirection.Horizontal })) // 设置只响应水平方向的滑动手势事件
          .onActionUpdate((event: GestureEvent) => { // 监听手势移动
            if (event) {
              scroller.scrollTo({
                // 监听到Scroll组件上水平方向的滑动手势事件时，让Scroll组件滚动对应距离
                xOffset: scroller.currentOffset().xOffset -
                event.offsetX, // 在Scroll组件当前的水平滚动偏移量基础上，偏移该次手势移动的距离，当向右滑动时event.offsetX为正值否则为负值
                yOffset: 0
              });
            }
          })
      )
      .layoutWeight(1);
    }
    .width('100%');
  }
}
```

效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/SU0qCr0oQNW5UrypmqsEwA/zh-cn_image_0000002658798167.png "点击放大")

## 常见FAQ

Q：可以通过给不同的Scroll组件绑定同一个Scroller实例吗，比如想要通过这种方式实现所有Scroll组件统一滑动？

A：不可以，一个Scroller实例只能绑定和控制一个Scroll组件。
