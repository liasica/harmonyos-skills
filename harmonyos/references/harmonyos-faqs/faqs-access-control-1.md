---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-access-control-1
title: 权限申请被拒绝后，再次申请权限，是否出现申请权限弹窗
breadcrumb: FAQ > 系统开发 > 安全 > 程序访问控制 > 权限申请被拒绝后，再次申请权限，是否出现申请权限弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:1ec5307b3c758769625383d5b0c73acc0693a35b1482b011a6c137a9c036a33b
---

当用户拒绝过一次权限申请后，再次调用[requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)接口申请同一权限时，系统将不会再次弹出权限申请弹窗。对于申请授权的返回值请参见：[PermissionRequestResult](../harmonyos-references/js-apis-permissionrequestresult.md)。
