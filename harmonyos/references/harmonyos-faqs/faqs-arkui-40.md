---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-40
title: 如何处理父子组件间的事件传递，例如，如何解决滑动冲突
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何处理父子组件间的事件传递，例如，如何解决滑动冲突
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:06+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:ec775de8e45bfdbe77e37f8a3f7f5c3651b40d28a9b177526b473b5e24e75f38
---

1. 系统基于触摸测试收集需响应事件的控件，测试顺序从父组件到子组件。后续手势识别和竞争基于hitTest结果。

2. 应用可改变组件上 hitTestBehavior 的值，以修改系统对其的 hitTest 结果。

3. 通过自定义事件和手势判定能力，可细化手势识别与竞争结果的干预。

**参考链接**

[触摸测试控制](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md)、[自定义事件分发](../harmonyos-references/ts-universal-attributes-on-child-touch-test.md)、[自定义手势判定](../harmonyos-references/ts-gesture-customize-judge.md)
