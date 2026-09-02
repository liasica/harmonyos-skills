---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-162
title: 组件如何拦截多次快速点击事件
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 组件如何拦截多次快速点击事件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f06fac05d2a222284f9fe817e4d56c1692738daded5cc7128f96534ffcb6ee7a
---

## 问题现象

如何拦截用户短时间内多次快速点击，避免事件处理函数多次意外触发？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/gcuQ-YR7TV6bIySB9fLLLw/zh-cn_image_0000002659258281.png "点击放大")

## 背景知识

[onClick](../harmonyos-references/ts-universal-events-click.md#onclick)：点击动作触发该回调，多次点击会多次触发。在开发过程中，有场景需要拦截短时间内多次快速点击事件，有以下两种方式：

* 节流：n秒内只运行一次，若在n秒内重复触发，只有一次生效。
* 防抖：n秒后再执行该事件，若在n秒内被重复触发，则重新计时。

## 解决方案

防抖、节流两种实现方式：

```ts
// 防抖:在一段时间内函数被多次触发，防抖让函数在一段时间后最终只执行一次
export function debounce(func: (event: ClickEvent) => void, delay?: number) {
  let timer: number;
  return (event: ClickEvent) => {
    clearTimeout(timer);
    timer = setTimeout(() => {
      func(event);
    }, delay ? delay : 1000);
  };
}

// 节流:在规定的时间内，只执行一次
export function throttle(func: (event: ClickEvent) => void, delay?: number) {
  let inThrottle: boolean;
  return (event: ClickEvent) => {
    if (!inThrottle) {
      func(event);
      inThrottle = true;
      setTimeout(() => inThrottle = false, delay ? delay : 1000);
    }
  };
}

@Entry
@Component
struct Index {
  @State num: number = 0;
  @State num1: number = 0;

  build() {
    Row() {
      Column() {
        Text(this.num.toString());
        Button('节流示例')
          .onClick(
            throttle(() => {
              this.num++;
            }, 5000));
        Text(this.num1.toString());
        Button('防抖示例')
          .onClick(
            debounce(() => {
              this.num1++;
            }, 5000));
      }
      .width('100%');
    }
    .height('100%');
  }
}
```

## 常见FAQ

Q：如何限制点击事件只执行一次？

A：定义一个全局状态变量控制按钮的[enabled](../harmonyos-references/ts-universal-attributes-enable.md#enabled)属性。例如定义全局状态变量hasClick记录点击事件是否被点击，在onClick里判断是否已执行过点击事件，以此决定是否执行此次点击事件。
