---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-8
title: HAR包中使用window作为Toast时无法引入页面组件
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > HAR包中使用window作为Toast时无法引入页面组件
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:28+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f67e20390c07c1635fb470ee5dca5e411ac448c7f32975886e58e6ab4625d691
---

**问题现象**

在HAR包中使用一个window作为弹窗，该window通过一个page页面实现。使用window.setUIContent方法引入page时，出现导入失败的问题。

**解决措施**

1. HAR不包含page，建议在HAP中声明窗口以放置HAR或HSP组件。
2. 实现弹窗Toast，可以使用ArkTS组件来自定义弹窗组件。

**参考链接**

[自定义弹窗](../harmonyos-references/ts-methods-custom-dialog-box.md)
