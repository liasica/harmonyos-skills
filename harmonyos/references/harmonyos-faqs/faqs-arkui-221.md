---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-221
title: ArkUI组件能否支持继承
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > ArkUI组件能否支持继承
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:57+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e5b3bcc6ad5dbef140c4eed73cf5847951e77cfcc703e99552928a81628400eb
---

1.ArkUI采用声明式语法，组件以struct形式定义，不支持继承，未来也没有支持继承的计划。

2.基于开发者的场景，如果开发者希望抽取公共的父类以方便组件复用，可以考虑通过动态属性设置attributeModifier来实现组件复用扩展。attributeModifier已实现部分功能，其余功能将通过需求跟踪来完善。

3.如果开发者希望在基类页面的生命周期中统一处理一些业务，可以通过无感监听页面生命周期的observer功能来实现。

**参考链接**

[属性修改器 (AttributeModifier)](../harmonyos-guides/arkts-user-defined-extension-attributemodifier.md)

[@ohos.arkui.observer (无感监听)](../harmonyos-references/js-apis-arkui-observer.md)
