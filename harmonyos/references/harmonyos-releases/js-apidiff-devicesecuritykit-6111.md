---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-6111
title: Device Security Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > Device Security Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:29d302869c51e70fd1c5f0c17eb249aafd2f1b19926fbce98f5e5512dca2b778
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：trustedAuthentication；  API声明：function enableTrustedAuthentication(challenge: Uint8Array, pwdInfo: PasswordInfo, label: TUILable): Promise<AuthInfo>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function enableTrustedAuthentication(challenge: Uint8Array, pwdInfo: PasswordInfo, label: TUILable): Promise<AuthInfo>;  差异内容：1019100025 | api/@hms.security.trustedAuthentication.d.ts |
| 新增错误码 | 类名：trustedAuthentication；  API声明：function modifyTrustedAuthenticationPwd(challenge: Uint8Array, pwdInfo: PasswordInfo, authID: bigint, label: TUILable): Promise<AuthToken>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function modifyTrustedAuthenticationPwd(challenge: Uint8Array, pwdInfo: PasswordInfo, authID: bigint, label: TUILable): Promise<AuthToken>;  差异内容：1019100025 | api/@hms.security.trustedAuthentication.d.ts |
| 新增错误码 | 类名：trustedAuthentication；  API声明：function disableTrustedAuthentication(challenge: Uint8Array, needAuth: boolean, authID: bigint, label: TUILable): Promise<AuthToken>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function disableTrustedAuthentication(challenge: Uint8Array, needAuth: boolean, authID: bigint, label: TUILable): Promise<AuthToken>;  差异内容：1019100025 | api/@hms.security.trustedAuthentication.d.ts |
| 新增错误码 | 类名：trustedAuthentication；  API声明：function trustedAuthentication(challenge: Uint8Array, authID: bigint, label: TUILable): Promise<AuthToken>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function trustedAuthentication(challenge: Uint8Array, authID: bigint, label: TUILable): Promise<AuthToken>;  差异内容：1019100025 | api/@hms.security.trustedAuthentication.d.ts |
| 新增错误码 | 类名：trustedAuthentication；  API声明：function procContentAuthentication(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise<AuthToken>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function procContentAuthentication(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise<AuthToken>;  差异内容：1019100025 | api/@hms.security.trustedAuthentication.d.ts |
| 新增错误码 | 类名：trustedAuthentication；  API声明：function exportData(authID: bigint, label: TUILable): Promise<ArrayBuffer>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function exportData(authID: bigint, label: TUILable): Promise<ArrayBuffer>;  差异内容：1019100025 | api/@hms.security.trustedAuthentication.d.ts |
| 新增错误码 | 类名：trustedAuthentication；  API声明：function checkConfirmUITextFormat(text: string): Promise<TextCheckResult>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function checkConfirmUITextFormat(text: string): Promise<TextCheckResult>;  差异内容：1019100025 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_TUI\_OCCUPIED = 1019100025  差异内容：TRUSTED\_AUTH\_ERROR\_TUI\_OCCUPIED = 1019100025 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：CS\_VERIFY\_NULL = 0x12001081  差异内容：CS\_VERIFY\_NULL = 0x12001081 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：CS\_VERIFY\_ABNORMAL = 0x12001082  差异内容：CS\_VERIFY\_ABNORMAL = 0x12001082 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：FS\_MOUNT\_ABNORMAL = 0x1C001102  差异内容：FS\_MOUNT\_ABNORMAL = 0x1C001102 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：DRIVER\_CS\_ABNORMAL = 0x1C001200  差异内容：DRIVER\_CS\_ABNORMAL = 0x1C001200 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：DRIVER\_MMAP\_ABNORMAL = 0x1C001201  差异内容：DRIVER\_MMAP\_ABNORMAL = 0x1C001201 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：KERNEL\_MEMORY\_ABNORMAL = 0x1C001300  差异内容：KERNEL\_MEMORY\_ABNORMAL = 0x1C001300 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：PROCESS\_DEBUG\_ABNORMAL = 0x1C001401  差异内容：PROCESS\_DEBUG\_ABNORMAL = 0x1C001401 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：PROCESS\_CRASH\_ABNORMAL = 0x1C001402  差异内容：PROCESS\_CRASH\_ABNORMAL = 0x1C001402 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：PROCESS\_PRIVILEGE\_ESCALATION = 0x1C001403  差异内容：PROCESS\_PRIVILEGE\_ESCALATION = 0x1C001403 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit；  API声明：function acquireCodeSign(path: string): string;  差异内容：function acquireCodeSign(path: string): string; | api/@hms.security.securityAudit.d.ts |
| API从不支持元服务到支持元服务 | 类名：global；  API声明：declare namespace businessRiskIntelligentDetection  差异内容：NA | 类名：global；  API声明：declare namespace businessRiskIntelligentDetection  差异内容：atomicservice | api/@hms.security.businessRiskIntelligentDetection.d.ts |
