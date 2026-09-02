---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-967
title: 手势触发的前提
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 手势触发的前提
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1a9f3c6f8587c3df172c1a0e95460bcea43be97c4f7b957ecc2449feff9cb8ec
---

## 问题现象

Gesture手势一定要完成注册才能触发吗？

## 解决方案

* 手势识别需要注册后才能触发。因为手势事件处理器是基于事件驱动的，只有已注册的手势会被系统监测和处理。因此，在为组件添加手势时，必须等待组件UI在视图上完全渲染后，通过操作组件来识别对应的手势，从而触发相应的回调。
* gesture、priorityGesture和parallelGesture当前不支持使用三目运算符（条件? 表达式1 : 表达式2）切换手势绑定，详细参考[绑定手势方法](../harmonyos-references/ts-gesture-settings.md)。
