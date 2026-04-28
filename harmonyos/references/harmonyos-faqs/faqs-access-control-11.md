---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-access-control-11
title: 应用申请位置信息权限为什么没有弹窗
breadcrumb: FAQ > 系统开发 > 安全 > 程序访问控制 > 应用申请位置信息权限为什么没有弹窗
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:54+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:bd31a4bcbe309162f17809de177e8001d11512fdcb8f40ec3d7c043a838c57aa
---

**可能原因**

未申请ohos.permission.LOCATION权限。

**解决措施**

开发应用时，需要先申请权限ohos.permission.LOCATION，才能获取位置信息。

**参考链接**

[开放权限（系统授权）](../harmonyos-guides/permissions-for-all.md)
