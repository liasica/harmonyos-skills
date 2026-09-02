---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-computer-2
title: PC上不能通过鼠标控制图片滑动
breadcrumb: FAQ > 多设备场景 > 电脑 > 常见问题 > PC上不能通过鼠标控制图片滑动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7e18abedf8a3088174d3dd836628b04c9f289cb445507a691d92a391b8068a28
---

## 问题现象

PC上的应用，不能通过鼠标控制图片滑动。

## 背景知识

* [PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)：滑动手势事件。当滑动的最小距离达到设定的最小值时触发滑动手势事件。
* [Swiper](../harmonyos-references/ts-container-swiper.md)：滑块视图容器，提供子组件滑动轮播显示的能力。
* [鼠标事件](../harmonyos-references/ts-universal-mouse-key.md)：在鼠标的单个动作触发多个事件时，事件的顺序是固定的，鼠标事件默认透传。

## 问题定位

1. 检查容器是否绑定滑动手势事件。如PanGesture事件。

   ```ts
    Column() {
     Text('PanGesture offset:\nX: ' + this.offsetX + '\n' + 'Y: ' + this.offsetY)
   }
   .translate({ x: this.offsetX, y: this.offsetY, z: 0 }) // 以组件左上角为坐标原点进行移动
   // 左右滑动触发该手势事件
   .gesture(
     PanGesture(this.panOption)
       .onActionStart((event: GestureEvent) => {
         console.info(`Pan start`);
         console.info(`Pan start timeStamp is: ${event.timestamp}`);
       })
   )
   ```
2. 确保父容器未阻拦鼠标事件。如父组件设置了[hitTestBehavior](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)(HitTestMode.BLOCK\_DESCENDANTS)则会阻塞子节点响应触摸测试。

## 分析结论

1. 组件未声明支持鼠标拖拽事件。
2. 父容器阻拦了鼠标事件。

## 修改建议

1. 组件未声明支持鼠标拖拽事件：
   * 组件绑定PanGesture事件实现左右滑动。参考[示例](../harmonyos-references/ts-basic-gestures-pangesture.md#示例)。
   * 如果是Swiper组件，将[disableSwipe](../harmonyos-references/ts-container-swiper.md#disableswipe8)设为false。因为Swiper组件内包含了[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)拖动手势事件，用于滑动轮播子组件。disableSwipe属性设为true会取消内部的PanGesture事件监听。

2. 建议启用鼠标事件传递（参考：[如何实现事件透传](faqs-arkui-155.md)）。
