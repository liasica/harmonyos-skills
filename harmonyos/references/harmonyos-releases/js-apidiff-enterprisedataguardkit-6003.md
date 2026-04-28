---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-enterprisedataguardkit-6003
title: Enterprise Data Guard Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > Enterprise Data Guard Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:17+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:43f4729d86312d2333c17c126f5871d9fecda54ccd36e2939e4721479cf7d642
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：recoveryKey；  API声明：function verifyUserIdentityEnterprise(userId: number, userType: number, pinCode: string): Promise<void>;  差异内容：function verifyUserIdentityEnterprise(userId: number, userType: number, pinCode: string): Promise<void>; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：recoveryKey；  API声明：function getEnterpriseRecoveryKeyForResettingPin(userId: number, userType: number): Promise<EnterpriseRecoveryKeyInfo>;  差异内容：function getEnterpriseRecoveryKeyForResettingPin(userId: number, userType: number): Promise<EnterpriseRecoveryKeyInfo>; | api/@hms.pcService.recoveryKeyService.d.ts |
