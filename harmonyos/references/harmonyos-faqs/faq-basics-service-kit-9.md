---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-9
title: 系统设置只展示应用申请过的权限
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 系统设置只展示应用申请过的权限
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:21+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:efac2a6f1df8dcf8895e5a35de1a3c307cf86fd5ca06b339be87240f8a7a84eb
---

应用的权限设置中只展示应用申请过的权限，该特性是系统规格，只有在调用[requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)这个接口，并且用户选择是否授予权限之后，才会在应用详情页显示该权限开关。该设计特性考量：这个可以让用户看到一个更干净的权限管理页面，一个用户从来没有打开过的应用，进入应用详情页面却有众多权限，用户也会不理解。
