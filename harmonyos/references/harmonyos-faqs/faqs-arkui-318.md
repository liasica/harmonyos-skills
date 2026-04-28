---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-318
title: RelativeContainer组件height设置为auto，子组件以容器作为锚点，为什么auto不生效
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > RelativeContainer组件height设置为auto，子组件以容器作为锚点，为什么auto不生效
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:20+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9cb1e149d71a5280ea69761ccf45e623e1e16060c46a774aab5d89bf5a81b8c7
---

由于子组件布局需要先确定容器高度，而容器高度又依赖子组件布局结果，形成循环依赖导致必须进行二次布局。因为此时子组件的布局是相对于容器的垂直方向，而父组件的布局又需要依赖子组件布局后的结果再次进行布局。

**参考链接：**

[示例3（设置容器大小自适应内容）](../harmonyos-references/ts-container-relativecontainer.md#示例3设置容器大小自适应内容)
