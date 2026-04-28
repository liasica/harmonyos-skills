---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-6101
title: Device Security Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > Device Security Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:743319db661b7ce5fc0382c9ba6545473194a7c057aee636c5ad7e53fddb911e
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：trustedAppService；  API声明：function createAttestKey(options: AttestOptions): Promise<void>;  差异内容：NA | 类名：trustedAppService；  API声明：function createAttestKey(options: AttestOptions): Promise<void>;  差异内容：201 | api/@hms.security.trustedAppService.d.ts |
| 新增错误码 | 类名：trustedAppService；  API声明：function destroyAttestKey(): Promise<void>;  差异内容：NA | 类名：trustedAppService；  API声明：function destroyAttestKey(): Promise<void>;  差异内容：201 | api/@hms.security.trustedAppService.d.ts |
| 新增错误码 | 类名：trustedAppService；  API声明：function initializeAttestContext(userData: string, options: AttestOptions): Promise<AttestReturnResult>;  差异内容：NA | 类名：trustedAppService；  API声明：function initializeAttestContext(userData: string, options: AttestOptions): Promise<AttestReturnResult>;  差异内容：201 | api/@hms.security.trustedAppService.d.ts |
| 新增错误码 | 类名：trustedAppService；  API声明：function finalizeAttestContext(options: AttestOptions): Promise<void>;  差异内容：NA | 类名：trustedAppService；  API声明：function finalizeAttestContext(options: AttestOptions): Promise<void>;  差异内容：201 | api/@hms.security.trustedAppService.d.ts |
| 新增错误码 | 类名：trustedAppService；  API声明：function procSecImageTransform(srcSecImage: ArrayBuffer, procParams: SecImageProcParamsArray): Promise<SecImageBuffer>;  差异内容：NA | 类名：trustedAppService；  API声明：function procSecImageTransform(srcSecImage: ArrayBuffer, procParams: SecImageProcParamsArray): Promise<SecImageBuffer>;  差异内容：1011500011,201 | api/@hms.security.trustedAppService.d.ts |
| 删除错误码 | 类名：securityAudit；  API声明：function on(type: 'auditEventOccur', auditEventInfo: AuditEventInfo, callback: Callback<AuditEvent>): void;  差异内容：401 | 类名：securityAudit；  API声明：function on(type: 'auditEventOccur', auditEventInfo: AuditEventInfo, callback: Callback<AuditEvent>): void;  差异内容：NA | api/@hms.security.securityAudit.d.ts |
| 删除错误码 | 类名：securityAudit；  API声明：function off(type: 'auditEventOccur', auditEventInfo: AuditEventInfo, callback?: Callback<AuditEvent>): void;  差异内容：401 | 类名：securityAudit；  API声明：function off(type: 'auditEventOccur', auditEventInfo: AuditEventInfo, callback?: Callback<AuditEvent>): void;  差异内容：NA | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：SMB\_FILE\_SEND = 0x0F000001  差异内容：SMB\_FILE\_SEND = 0x0F000001 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：KIA\_PRE\_OPEN = 0x1C000014  差异内容：KIA\_PRE\_OPEN = 0x1C000014 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：HDC\_DEBUG = 0x27000100  差异内容：HDC\_DEBUG = 0x27000100 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：HDC\_DEBUG\_INTERCEPTED = 0x27000101  差异内容：HDC\_DEBUG\_INTERCEPTED = 0x27000101 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：USER\_SPACE\_DATA\_TRANSFER = 0x2F000000  差异内容：USER\_SPACE\_DATA\_TRANSFER = 0x2F000000 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：USER\_SPACE\_DATA\_TRANSFER\_POLICY = 0x2F000001  差异内容：USER\_SPACE\_DATA\_TRANSFER\_POLICY = 0x2F000001 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：SERIAL\_PORT\_ACCESS = 0x30000100  差异内容：SERIAL\_PORT\_ACCESS = 0x30000100 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：NETWORK\_INTERCEPTED = 0x03000002  差异内容：NETWORK\_INTERCEPTED = 0x03000002 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：WIFI\_INTERCEPTED = 0x03000100  差异内容：WIFI\_INTERCEPTED = 0x03000100 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：PRINT\_INTERCEPTED = 0x2E000001  差异内容：PRINT\_INTERCEPTED = 0x2E000001 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：dlpAntiPeep；  API声明：enum AntiPeepOptionsResult  差异内容：enum AntiPeepOptionsResult | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：AntiPeepOptionsResult；  API声明：SUCCESS = 0  差异内容：SUCCESS = 0 | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：AntiPeepOptionsResult；  API声明：FAIL = 1  差异内容：FAIL = 1 | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：AntiPeepOptionsResult；  API声明：ALREADY\_ON = 2  差异内容：ALREADY\_ON = 2 | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：dlpAntiPeep；  API声明：function requestAntiPeepOptions(context: Context): Promise<AntiPeepOptionsResult>;  差异内容：function requestAntiPeepOptions(context: Context): Promise<AntiPeepOptionsResult>; | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：dlpAntiPeep；  API声明：function publishAntiPeepInformation(): Promise<void>;  差异内容：function publishAntiPeepInformation(): Promise<void>; | api/@hms.security.dlpAntiPeep.d.ts |
