---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-389
title: Router路由跳转页面失败，可能有哪些原因
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Router路由跳转页面失败，可能有哪些原因
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:42+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:37029bd4c7be871cfba323e55f6856eed916b25cb6cdb67f161d7a191b3e8e5d
---

**1.har包中的page，未使用命名路由跳转**

HAR包中不支持在配置文件中声明pages页面，但是可以包含page并通过命名路由跳转，可参考：[命名路由](../harmonyos-guides/arkts-routing.md#命名路由)。

**2.import导入问题**

检查是否正确import目标页面，可以参考[命名路由](../harmonyos-guides/arkts-routing.md#命名路由)的配置进行排查。
