---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1534
title: 如何阻断事件传递
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何阻断事件传递
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c0b224055028dc0723981f4336776c31f3a6acb33b75fc48b86d0185b10a0987
---

## 问题现象

如何阻断事件在事件链上的传递？

## 背景知识

* [TouchEvent](../harmonyos-references/ts-universal-events-touch.md#touchevent对象说明)对象的stopPropagation方法可实现阻塞事件冒泡。
* 自定义事件拦截[onTouchIntercept](../harmonyos-references/ts-universal-attributes-on-touch-intercept.md#ontouchintercept)方法能够给组件绑定自定义事件拦截回调，并且能够在做触摸测试时回调此函数，通过返回值设置组件的触摸测试类型。触摸测试类型[HitTestMode](../harmonyos-references/ts-appendix-enums.md#hittestmode9)枚举类型有Default、Block、Transparent和None等。
* 设置了[独占控制](../harmonyos-references/ts-universal-attributes-monopolize-events.md)方法[monopolizeEvents](../harmonyos-references/ts-universal-attributes-monopolize-events.md#monopolizeevents)的窗口内，如果首先响应，则本次交互只允许此组件上设置的事件响应，窗口内其他组件上的事件不会响应。事件范围包括组件自带的事件和开发者自定义的点击、触摸、手势事件。

## 解决方案

* **方案一**：在子组件的onTouch事件中通过调用event.stopPropagation()方法，阻止事件向上冒泡至父组件。该方法适用于需要在子组件层面处理触摸事件，同时不希望影响到父组件手势识别的场景。

  ```ts
  @Entry
  @Component
  struct PageA {
    build() {
      Row() {
        Column() {
          Text('My Text')
            .fontSize(50)
            .onTouch((event: TouchEvent) => {
              if (event.type === TouchType.Down) {
                // 消耗事件，阻止向上冒泡
                event.stopPropagation();
              }
            });
        }
        .width('100%')
        .gesture(PanGesture().onActionStart(() => {
          console.info('Pan action');
        }));
      };
    }
  }
  ```
* **方案二**：使用自定义事件拦截方法。

  为每个组件绑定onTouchIntercept回调方法，该方法能够在触摸事件被传递给子组件之前进行拦截。在其中一个组件上设置onTouchIntercept，并且通过回调方法返回HitTestMode的枚举值，从而达到控制触摸事件的效果，例如返回HitTestMode.None，使组件自身不响应事件，达到隔离自身触摸事件的效果。

  ```ts
  @Entry
  @Component
  struct PageB {
    @State bgColor: string = '#F1F3F5';
    @State text: string = 'Text';

    isPolygon() {
      return true;
    }

    build() {
      Column() {
        Text(this.text)
          .textAlign(TextAlign.Center)
          .fontSize(17)
          .width('25%')
          .height('15%')
          .borderRadius(16)
          .backgroundColor(Color.White)
          .onClick(() => {
            this.text = 'Changed';
          });
      }
      .justifyContent(FlexAlign.Center)
      .onTouchIntercept(() => {
        return HitTestMode.None;
      })
      .width('100%')
      .height(300)
      .backgroundColor(this.bgColor)
      .onClick(() => {
        this.bgColor = '#668c8c8c';
      });
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/NM5rhc8WTcupXqohymB70g/zh-cn_image_0000002628607000.png "点击放大")

* **方案三**：设置事件独占控制：在其中一个组件上设置monopolizeEvents属性，并赋值为true，该组件就将独占所有事件，包括触摸、点击和手势事件，当该组件响应事件后，其他组件将不会响应任何事件，直到事件结束，达到隔离其他触摸事件的效果，具体实现可以参考官网[示例](../harmonyos-references/ts-universal-attributes-monopolize-events.md#示例)。

## 总结

| 方案 | 适用场景 |
| --- | --- |
| 调用event.stopPropagation()方法 | 阻止子组件事件到父组件的传递。 |
| 使用自定义事件拦截方法 | 通过触发触摸事件来控制组件的HitTestMode属性，适合需要根据触摸信息动态改变HitTestMode的场景。 |
| 设置事件独占控制 | 事件独占期间，只有当前事件结束才会轮到下一个事件，适合需要依次执行组件触摸事件的场景。例如：按住消息卡片触发长按效果，拖动聊天窗空白区域触发滚动效果，需要隔绝长按和滚动的冲突。 |
