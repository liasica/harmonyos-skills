---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-839
title: Scroll滚动到顶/底部后，下/上拖执行自定义方法
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Scroll滚动到顶/底部后，下/上拖执行自定义方法
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:502f2af4c92825fa30ce15c2a7165e4453cade82e74aeb208690439070233b19
---

## 问题现象

Scroll滚动到顶部时继续下拖和滚动到底部时继续上拖，如何执行自定义方法？

## 背景知识

* [Scroll](../harmonyos-references/ts-container-scroll.md)可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
  + [currentOffset](../harmonyos-references/ts-container-scroll.md#currentoffset)获取Scroll当前的偏移量。
  + [isAtEnd](../harmonyos-references/ts-container-scroll.md#isatend10)查询Scroll是否滚动到底部。
* [PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)可以为组件绑定滑动手势事件，其中手势回调的event.offsetY在从上向下滑动为正，反之为负。

## 解决方案

使用PanGesture为Scroll绑定平移事件，在滑动结束即onActionEnd中判断Scroll位置以进行相应处理。

* Scroll滑到顶部继续下拖判断：
  + 调用currentOffset获取Scroll当前位置，若Y方向小于等于0，则已滑至顶部。
  + 通过onActionEnd的event判断是否继续下拖，若event.offsetY大于0表示继续下拖，则执行自定义操作。
* Scroll滑到底部继续上拖判断：
  + 调用isAtEnd判断Scroll是否已滑至底部。
  + 通过onActionEnd的event判断是否继续上拖，若event.offsetY小于0表示继续上拖，则执行自定义操作。

```ts
@Entry
@Component
struct ScrollDemo {
  private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Vertical });
  private scrollerForScroll: Scroller = new Scroller();

  build() {
    Column() {
      Scroll(this.scrollerForScroll) {
        // 此处'app.media.startIcon'仅作示例
        Image($r('app.media.startIcon'))
          .size({ width: 400, height: 1050 });
      }
      .width('100%')
      .height('100%')
      .edgeEffect(EdgeEffect.Spring)
      .parallelGesture(
        PanGesture(this.panOption)
          .onActionEnd((event: GestureEvent) => {
            console.info('PanGesture end');
            // 滑动到底部并且继续滑动
            if (this.scrollerForScroll.isAtEnd() && event.offsetY < 0) {
              console.info('执行自定义操作1');
            }
            // 滑动到顶部并且继续滑动
            const offsetRes = this.scrollerForScroll.currentOffset(); // 获取Scroll现在的位置
            if (offsetRes.yOffset <= 0 && event.offsetY > 0) {
              console.info('执行自定义操作2');
            }
          }), GestureMask.Normal);
    };
  }
}
```
