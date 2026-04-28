---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-335
title: 常用可以设置'auto'的属性的组件及其含义的介绍
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 常用可以设置'auto'的属性的组件及其含义的介绍
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0653cd9ade6b0afe0210b523b57c0bb8e2eed3d009aa04adcccc5e7f42a6ad76
---

* Row、Column和RelativeContainer组件支持width/height属性设置为'auto'，此时组件尺寸会根据子组件自动调整；
* 在TextInput组件中，将width属性设置为'auto'，表示自适应文本宽度，与布局组件不同，TextInput的auto宽度仅根据输入文本内容调整，不受子组件影响；
* flexBasis属性默认值为'auto'，表示组件在主轴方向上的基准尺寸为其原始大小。
