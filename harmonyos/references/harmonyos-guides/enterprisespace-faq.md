---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-faq
title: Enterprise Space Kit常见问题
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > Enterprise Space Kit常见问题
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2666d93b2de552c07eed8625369c1574dc1a12521fac0899dcb07be66419079b
---

## 编译失败，该如何解决

**问题现象**

编译不通过，签名证书缺少所需权限，报错：install failed due to grant request permissions failed.

**解决措施**

1. 参考[访问控制概述](access-token-overview.md)，检查应用签名是否正常配置权限。
2. 如还未解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 切换空间时，后台空间的应用无法启动或被终止

**问题现象**

切换空间时后台空间的应用被系统冻结，导致应用无法启动或被终止。

**可能原因**

为防止企业数据泄漏，空间切换时，后台空间的应用不可访问前台空间数据。

**解决措施**

调用[setLockdownExemptionApps](../harmonyos-references/enterprisespace-spacemanager.md#setlockdownexemptionapps)接口将应用加入豁免应用列表，确保应用可在后台空间正常运行，不会被冻结。
