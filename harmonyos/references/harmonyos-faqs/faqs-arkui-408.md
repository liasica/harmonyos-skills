---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-408
title: Navigation组件，调用queryNavDestinationInfo返回undefined，如何正确调用这个接口
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation组件，调用queryNavDestinationInfo返回undefined，如何正确调用这个接口
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:47+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a9be6f326d4227fe57081744d35577a7f526b8856ad6ebbf6568cd1acf4dc3a0
---

queryNavDestinationInfo()接口会从当前组件的父组件开始向上查找，不包括同级组件，查找到第一个NavDestination即返回。如在NavDestination所在的自定义组件中查找会导致返回undefined。

使用说明可参考文档：[queryNavDestinationInfo](../harmonyos-references/ts-custom-component-api.md#querynavdestinationinfo)。
