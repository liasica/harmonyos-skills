---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-b031
title: Device Security Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Device Security Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:38+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:7d939e6c6311c25accb7c3c59461d02043c26a8d6f04f7a9e3a06bee25a320de
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：trustedAppService；  API声明：function getCurrentSecureLocation(timeout: number, priority: LocatingPriority): Promise<SecureLocation>;  差异内容：ohos.permission.APPROXIMATELY\_LOCATION | 类名：trustedAppService；  API声明：function getCurrentSecureLocation(timeout: number, priority: LocatingPriority): Promise<SecureLocation>;  差异内容：ohos.permission.LOCATION and ohos.permission.APPROXIMATELY\_LOCATION | api/@hms.security.trustedAppService.d.ts |
