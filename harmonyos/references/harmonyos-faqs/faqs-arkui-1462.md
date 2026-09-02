---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1462
title: 如何实现主动终止长按手势
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现主动终止长按手势
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f2d0efb2c3b3e75a7ed93dea8903c4600c5968b19d23b92c1d6b34e8bb43e0f6
---

## 问题现象

通过GestureGroup实现了长按录音的功能，现在需要录音超过60秒停止识别，如何实现主动终止长按手势？

## 背景知识

[LongPressGesture](../harmonyos-references/ts-basic-gestures-longpressgesture.md)，用于触发长按手势事件，触发长按手势的最少手指数为1，最短长按时间为500毫秒。

## 解决方案

在HarmonyOS开发中，可通过状态管理结合定时器机制实现长按手势在60秒后主动终止。通过LongPressGesture的onAction回调启动定时器，结合状态变量控制手势终止逻辑：

1. 启动长按时触发定时器，60秒后修改状态。
2. 在手势回调中判断状态以终止逻辑。
3. 通过onActionEnd清理定时器。

```screen
@Component
@Entry
struct PressGestureDemo {
  @State isLongPressActive: boolean = true; // 控制手势激活状态
  private timerId: number = 0; // 存储定时器ID

  build() {
    Row() {
      Column() {
        Button('长按60秒后自动终止')
          .gesture(
            LongPressGesture({ duration: 500 })
              .onAction(() => {
                if (!this.isLongPressActive) {
                  return;
                } // 状态终止时退出
                // 启动60秒定时器
                this.timerId = setTimeout(() => {
                  this.isLongPressActive = false;
                  // 此处可添加终止后的业务逻辑，即终止录音操作
                }, 60000);
              })
              .onActionEnd(() => {
                clearTimeout(this.timerId); // 清理定时器
                this.isLongPressActive = true; // 重置状态
              })
          );
      }.width('100%');
    }.height('100%');
  }
}
```
