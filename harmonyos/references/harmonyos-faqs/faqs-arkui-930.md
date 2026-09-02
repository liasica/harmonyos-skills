---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-930
title: 如何解决Scroll嵌套的ColumnSplit无法滑动的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决Scroll嵌套的ColumnSplit无法滑动的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:8ea7dbbc6b73d2b3cba53916f5a83692b8960792e628b156aac380571a5ba2d0
---

## 问题现象

Scroll中嵌套ColumnSplit，如果ColumnSplit内容超出屏幕，需要滑动浏览时，触摸在ColumnSplit组件的区域，无法滑动页面，只有触摸滚动条或者页面中非ColumnSplit组件的部分，才可以滑动页面。造成这种现象的原因何在？如何解决？

问题代码示例参考如下：

```screen
@Entry
@Component
struct ColumnSplitExample {
  private scroller: Scroller = new Scroller();
  @State scrollerEdge: Edge = Edge.Top;

  build() {
    Scroll(this.scroller) {
      Column() {
        Blank(50)
        ColumnSplit() {
          Text('1').width('100%').height('20%').backgroundColor('#F1F3F5').textAlign(TextAlign.Center);
          Text('2').width('100%').height('20%').backgroundColor('#E5E5EA').textAlign(TextAlign.Center);
          Text('3').width('100%').height('20%').backgroundColor('#F1F3F5').textAlign(TextAlign.Center);
          Text('4').width('100%').height('20%').backgroundColor('#E5E5EA').textAlign(TextAlign.Center);
          Text('5').width('100%').height('20%').backgroundColor('#F1F3F5').textAlign(TextAlign.Center);
        }
        .width('90%')
        .height('100%');
      }.width('100%');
    }
    .height('100%')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
    .onScrollEdge((side) => {
      this.scrollerEdge = side;
    });
  }
}
```

## 背景知识

* ColumnSplit组件可通过[resizeable](../harmonyos-references/ts-container-columnsplit.md#resizeable)属性设置分割线是否可拖拽。
* [手势响应控制方法](../harmonyos-guides/arkts-gesture-event-conflict-faq.md#动态控制自定义手势是否响应)中的[手势拦截增强](../harmonyos-references/ts-gesture-blocking-enhancement.md)能力，可以动态控制手势事件的触发。
* 通过[onGestureRecognizerJudgeBegin](../harmonyos-references/ts-gesture-blocking-enhancement.md#ongesturerecognizerjudgebegin)属性可以自定义不同手势下的回调，可参考[嵌套场景下拦截内部容器手势](../harmonyos-references/ts-gesture-blocking-enhancement.md#示例2嵌套场景下拦截内部容器手势)示例。

## 解决方案

ColumnSplit组件的resizeable属性支持拖拽，即使设置为false，其拖拽手势的优先级依然在滑动之上，在ColumnSplit组件区域内，ColumnSplit的拖拽事件与Scroll的滚动事件产生冲突，因此触摸在ColumnSplit组件区域，无法滑动页面。

如果需要触摸在ColumnSplit组件的区域时也能滑动页面，可以参考手势拦截增强的[示例2（嵌套场景下拦截内部容器手势）](../harmonyos-references/ts-gesture-blocking-enhancement.md#示例2嵌套场景下拦截内部容器手势)，给子组件绑定自定义手势识别器判定回调onGestureRecognizerJudgeBegin。

对于ColumnSplit组件，可以分两种场景：

* 场景一：resizeable属性设置为false，不支持分割线拖拽时，屏蔽ColumnSplit的拖拽事件，使滚动事件能够正常响应。

  ```screen
  @Entry
  @Component
  struct ColumnSplitExample2 {
    private scroller: Scroller = new Scroller();
    @State scrollerEdge: Edge = Edge.Top;

    build() {
      Scroll(this.scroller) {
        Column() {
          Blank(50)
          ColumnSplit() {
            Text('1').width('100%').height('20%').backgroundColor('#F1F3F5').textAlign(TextAlign.Center);
            Text('2').width('100%').height('20%').backgroundColor('#E5E5EA').textAlign(TextAlign.Center);
            Text('3').width('100%').height('20%').backgroundColor('#F1F3F5').textAlign(TextAlign.Center);
            Text('4').width('100%').height('20%').backgroundColor('#E5E5EA').textAlign(TextAlign.Center);
            Text('5').width('100%').height('20%').backgroundColor('#F1F3F5').textAlign(TextAlign.Center);
          }
          .resizeable(false)
          .onGestureRecognizerJudgeBegin((_event: BaseGestureEvent, _current: GestureRecognizer,
            _others: Array<GestureRecognizer>): GestureJudgeResult => { // 在识别器即将要成功时，根据当前组件状态，设置识别器使能状态
            console.info(`${_event}${_current}${_others}`);
            return GestureJudgeResult.REJECT;
          })
          .width('90%')
          .height('100%');
        }.width('100%');
      }
      .height('100%')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
      .onScrollEdge((side) => {
        this.scrollerEdge = side;
      });
    }
  }
  ```
* 场景二：resizeable属性设置为true，支持分割线拖拽时，需要确定响应滚动事件和响应分割线拖拽事件的时机，避免冲突。以仅支持滚动到边缘时为例：当滚动条在上边缘时，无法继续上滑，此时从上往下的滑动手势支持拖拽分割线，从下往上的滑动手势支持滚动条下滑；当滚动条在下边缘时，无法继续下滑，此时从下往上的滑动手势支持拖拽分割线，从上往下的滑动手势支持滚动条上滑。

  ```screen
  @Entry
  @Component
  struct ColumnSplitExample3 {
    private scroller: Scroller = new Scroller();
    @State scrollerEdge: Edge = Edge.Top;

    build() {
      Scroll(this.scroller) {
        Column() {
          Blank(50)
          ColumnSplit() {
            Text('1').width('100%').height('20%').backgroundColor('#F1F3F5').textAlign(TextAlign.Center);
            Text('2').width('100%').height('20%').backgroundColor('#E5E5EA').textAlign(TextAlign.Center);
            Text('3').width('100%').height('20%').backgroundColor('#F1F3F5').textAlign(TextAlign.Center);
            Text('4').width('100%').height('20%').backgroundColor('#E5E5EA').textAlign(TextAlign.Center);
            Text('5').width('100%').height('20%').backgroundColor('#F1F3F5').textAlign(TextAlign.Center);
          }
          .resizeable(true)
          .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
            _others: Array<GestureRecognizer>): GestureJudgeResult => { // 在识别器即将要成功时，根据当前组件状态，设置识别器使能状态
            console.info(`${_others}`);
            if (current) {
              let target = current.getEventTargetInfo();
              if (target && current.isBuiltIn() && current.getType() == GestureControl.GestureType.PAN_GESTURE) {
                let panEvent = event as PanGestureEvent;
                if (panEvent && panEvent.velocityY < 0 && this.scrollerEdge === Edge.Bottom) { // 外层Scroll滑动到尽头
                  return GestureJudgeResult.CONTINUE;
                }
                if (panEvent && panEvent.velocityY > 0 && this.scrollerEdge === Edge.Top) { // 外层Scroll滑动到开头
                  return GestureJudgeResult.CONTINUE;
                }
              }
            }
            return GestureJudgeResult.REJECT;
          })
          .width('90%')
          .height('100%');
        }.width('100%');
      }
      .height('100%')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
      .onScrollEdge((side) => {
        this.scrollerEdge = side;
      });
    }
  }
  ```
