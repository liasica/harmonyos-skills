---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-444
title: Scroll嵌套外层滚动容器滚动，如何设置nestedScroll，实现Scroll组件先滚动，滚动边缘后触发外层滚动容器滚动
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Scroll嵌套外层滚动容器滚动，如何设置nestedScroll，实现Scroll组件先滚动，滚动边缘后触发外层滚动容器滚动
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:55+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:f81984e50921f2dd3e9f477c9aa1be8f81b2237523d54e05695016d8016b1c4d
---

**问题背景**

Scroll外面嵌套一个滚动容器，想要实现Scroll先滚动，达到顶部或者底部之后，外面的滚动容器再滚动，该如何设置nestedScroll。

**解决措施**

针对该交互需求，可采用以下配置方案：

将nestedScroll属性的参数对象设置为[NestedScrollMode.SELF\_FIRST](../harmonyos-references/ts-appendix-enums.md#nestedscrollmode10)类型实现该效果。

NestedScrollMode.SELF\_FIRST表示自身先滚，滚动到边缘后父组件再滚动。

**参考链接**

[使用nestedScroll属性实现嵌套滚动](../harmonyos-guides/web-nested-scrolling.md#使用nestedscroll属性实现嵌套滚动)
