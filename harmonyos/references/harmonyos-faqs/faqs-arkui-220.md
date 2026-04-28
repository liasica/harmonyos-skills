---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-220
title: Flex布局与w3c中的Flex是否有差异
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Flex布局与w3c中的Flex是否有差异
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:57+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a93ef618851d855c91eac9eaf03a730be8d60b8a63b577b24ed9862455dbceff
---

在w3c标准中，Flex组件主轴的默认大小是由子组件决定的，但是Flex的align-items的默认值是stretch，也就是拉伸，因此在父Flex组件不设置align-items时，子Flex组件会在主轴上填满父组件，而当将父组件的align-items设置为其他值时，子Flex组件由他自己的子组件决定主轴的大小了。

与w3c标准不同，在ArkTS中，Flex组件主轴的默认大小是由父组件决定的，即在主轴方向上填满父组件，因此在不设置Flex组件主轴大小的情况下，对齐方式alignItems是不会影响Flex组件的主轴大小的，且ArkTS中Flex组件的alignItems属性的默认值为ItemAlign.Start，因此设置了ItemAlign.Start后，Flex组件仍然会在主轴上填满父组件。
