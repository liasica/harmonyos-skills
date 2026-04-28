---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-333
title: 一个自定义组件内某一时机批量刷新多个@State修饰的状态变量，是否会影响性能
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 一个自定义组件内某一时机批量刷新多个@State修饰的状态变量，是否会影响性能
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b7f82619dab0b1a15e5ade3e9a66a7b37856259f7bd67a1244db49d032a5c0d2
---

**问题现象**

例如，一个自定义的Component包含20个由@State修饰的变量，每个@State变量都支持值更新操作，批量修改时会调用每个State的更新接口。这种批量更新操作可能引发组件频繁刷新，需要评估其对性能的影响。

**解决措施**

同时更新多个State接口不会导致性能问题，因为每个@State都有更新UI的能力，批量修改不会导致组件反复刷新。框架会在状态变更时合并UI更新请求，在Vsync信号到来时统一处理，因此无论修改多少个@State变量都只会触发一次组件刷新。
