---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-26011
title: Device Security Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > Device Security Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:53+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:adf45dd75f5e824bc9f9e8f7d584d77c0a7789514433ceb5a6787b197010ddf1
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace sideloading  差异内容：declare namespace sideloading | api/@hms.security.sideloading.d.ts |
| 新增API | NA | 类名：sideloading；  API声明：function isExternalBinaryLoadingEnabled(): Promise<boolean>;  差异内容：function isExternalBinaryLoadingEnabled(): Promise<boolean>; | api/@hms.security.sideloading.d.ts |
| 新增API | NA | 类名：sideloading；  API声明：function enableExternalBinaryLoadingOnSetting(context: common.Context): Promise<ExternalBinaryLoadingStatus>;  差异内容：function enableExternalBinaryLoadingOnSetting(context: common.Context): Promise<ExternalBinaryLoadingStatus>; | api/@hms.security.sideloading.d.ts |
| 新增API | NA | 类名：sideloading；  API声明：enum ExternalBinaryLoadingStatus  差异内容：enum ExternalBinaryLoadingStatus | api/@hms.security.sideloading.d.ts |
| 新增API | NA | 类名：ExternalBinaryLoadingStatus；  API声明：DENY = 0  差异内容：DENY = 0 | api/@hms.security.sideloading.d.ts |
| 新增API | NA | 类名：ExternalBinaryLoadingStatus；  API声明：ALLOW = 1  差异内容：ALLOW = 1 | api/@hms.security.sideloading.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：CUSTOMIZED\_DLP\_FILE\_ACCESS = 0x0F000007  差异内容：CUSTOMIZED\_DLP\_FILE\_ACCESS = 0x0F000007 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：DISC\_BURNING\_INTERCEPTED = 0x0F000008  差异内容：DISC\_BURNING\_INTERCEPTED = 0x0F000008 | api/@hms.security.securityAudit.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.security.sideloading.d.ts  差异内容：DeviceSecurityKit | api/@hms.security.sideloading.d.ts |
