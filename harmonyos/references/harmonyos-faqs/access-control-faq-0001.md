---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/access-control-faq-0001
title: 应用权限授权类型与状态查询常见问题
breadcrumb: FAQ > 系统开发 > 安全 > 程序访问控制 > 常见问题 > 应用权限授权类型与状态查询常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:08+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:d253da1329e027221ed24718a4c7c9bab1d67254ca4cf8abbc157a633fc9e876
---

**Q：在向用户申请获取定位权限时，用户可以选择多种授权类型，如何获取用户选择的是哪种授权类型？**

**A**：获取用户位置信息时需要申请授权，在申请用户位置定位权限时，授权弹窗有三种授权类型供用户选择，分别是本次使用允许、仅使用期间允许和不允许。

在用户选择后，会返回用户是否授权的[枚举状态](../harmonyos-references/js-apis-abilityaccessctrl.md#grantstatus)。

用户选择本次使用允许、仅使用期间允许表示允许授权，选择不允许表示拒绝授权，用户不选择任意一项，默认为拒绝授权（无返回值）。

[getSelfPermissionStatus](../harmonyos-references/js-apis-abilityaccessctrl.md#getselfpermissionstatus20)：从API20开始，可以使用getSelfPermissionStatus方法查询应用权限状态，同步返回结果。
