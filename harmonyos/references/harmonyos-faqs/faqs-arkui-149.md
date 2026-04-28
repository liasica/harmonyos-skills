---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-149
title: Navigation如何隐藏导航栏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation如何隐藏导航栏
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:39+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b1f2b516704646d051a5bf91dc57a34c75313898816962070074910b9ed8b97e
---

**问题现象**

Navigation设置了隐藏属性，仍然出现空白导航栏。跳转至新页面后，导航栏会重新出现。

**解决措施**

需同时设置Navigation组件及其NavDestination子组件的hideTitleBar属性为true才能完全隐藏导航栏。

**参考链接**

[Navigation](../harmonyos-references/ts-basic-components-navigation.md#navigation10)
