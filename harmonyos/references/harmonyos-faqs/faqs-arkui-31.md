---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-31
title: 如何实现类似插槽的功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现类似插槽的功能
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:05+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2573a7505cfc7d3c468bb15326f9f8a8b434f3d4c57e84a89882df0ff13e7239
---

* ArkUI 提供了一种轻量的 UI 元素复用机制 @Builder。使用 @Builder装饰的函数需遵循 build()函数的语法规则。开发者可以将重复使用的 UI 元素抽象成一个方法，并在build方法中调用。
* ArkUI 引入了 @BuilderParam 装饰器，用于装饰指向 @Builder 方法的变量。开发者在初始化自定义组件时，可以对此属性进行赋值，为自定义组件增加特定功能。该装饰器用于声明任意 UI 描述的元素，类似于 slot 占位符。具体代码示例如下：

  ```
  1. @Component
  2. struct Child {
  3. @Builder funABuilder0() {}
  4. @BuilderParam aBuilder0: () => void = this.funABuilder0;

  6. build() {
  7. Column() {
  8. this.aBuilder0()
  9. }
  10. }
  11. }

  13. @Entry
  14. @Component
  15. struct Parent {
  16. @Builder componentBuilder() {
  17. Text(`Parent builder `)
  18. }

  20. build() {
  21. Column() {
  22. Child({ aBuilder0: this.componentBuilder })
  23. }
  24. }
  25. }
  ```

  [ImplementSlotFunction.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImplementSlotFunction.ets#L21-L45)

**参考链接**

[@Builder装饰器：自定义构建函数](../harmonyos-guides/arkts-builder.md)

[@BuilderParam装饰器：引用@Builder函数](../harmonyos-guides/arkts-builderparam.md)
