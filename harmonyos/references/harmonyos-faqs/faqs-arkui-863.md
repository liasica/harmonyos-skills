---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-863
title: 上层组件滑动时，下层组件同步滑动
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 上层组件滑动时，下层组件同步滑动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5ccdec5bd250c5966081f4432a64c0a15bbe6ade5cf304bb9a467d57c7c34f30
---

## 问题现象

当上层组件被滑动时，下层组件也同步滑动。例如，登录页面覆盖在地图之上，但用户在登录页面进行滑动时，地图也随之滑动，导致交互逻辑不符合预期。

## 背景知识

* [手势事件冲突解决方案](../best-practices/bpta-gestures-practice.md)：在复杂的应用界面中，多个组件嵌套时同时绑定手势事件，或者同一个组件同时绑定多个手势，都有可能导致手势事件产生冲突，达不到用户的预期效果。
* [hitTestBehavior](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)：属性用于设置不同的触摸测试响应模式，影响触摸测试收集结果及后续触屏事件分发。具体影响参考[HitTestMode](../harmonyos-references/ts-appendix-enums.md#hittestmode9)。

## 问题定位

全局搜索关键词hitTestBehavior，可以看到对登录页面（上层组件）的触摸测试类型设置为了HitTestMode.Transparent，其特性是不阻塞兄弟节点的触摸测试，导致地图组件（下层组件）仍然能够接收并响应触摸事件，从而出现同步滑动的现象。

## 分析结论

上层组件的hitTestBehavior设置为HitTestMode.Transparent，导致下层组件仍能接收触摸事件，造成滑动行为的同步。

## 修改建议

将上层组件触摸测试类型设置为HitTestMode.Default或者HitTestMode.Block。
