---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-6003
title: Device Security Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > Device Security Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:16+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:9352cb71ccd08ea352f685e10babce74404dc861ca62e96d9ec539c38615c70f
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：trustedAuthentication；  API声明：function procContentAuthentication(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise<AuthToken>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function procContentAuthentication(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise<AuthToken>;  差异内容：1019100021 | api/@hms.security.trustedAuthentication.d.ts |
| 新增错误码 | 类名：trustedAuthentication；  API声明：function getBiometricAuthToken(operType: OperateType, tuiAuthToken: Uint8Array, bioAuthToken: Uint8Array): Promise<AuthToken>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function getBiometricAuthToken(operType: OperateType, tuiAuthToken: Uint8Array, bioAuthToken: Uint8Array): Promise<AuthToken>;  差异内容：1019100005,1019100019,1019100020 | api/@hms.security.trustedAuthentication.d.ts |
| 删除错误码 | 类名：trustedAuthentication；  API声明：function getBiometricAuthToken(operType: OperateType, tuiAuthToken: Uint8Array, bioAuthToken: Uint8Array): Promise<AuthToken>;  差异内容：1019100007 | 类名：trustedAuthentication；  API声明：function getBiometricAuthToken(operType: OperateType, tuiAuthToken: Uint8Array, bioAuthToken: Uint8Array): Promise<AuthToken>;  差异内容：NA | api/@hms.security.trustedAuthentication.d.ts |
| 枚举赋值发生改变 | 类名：NotifyEvent；  API声明：FILE\_INTERCEPTED = 0x2700003C  差异内容：0x2700003C | 类名：NotifyEvent；  API声明：FILE\_INTERCEPTED = 0x1C001100  差异内容：0x1C001100 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit；  API声明：enum AuthEvent  差异内容：enum AuthEvent | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuthEvent；  API声明：FILE\_CREATE = 0x1C801100  差异内容：FILE\_CREATE = 0x1C801100 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuthEvent；  API声明：FILE\_OPEN = 0x1C801101  差异内容：FILE\_OPEN = 0x1C801101 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuthEvent；  API声明：FILE\_RENAME = 0x1C801102  差异内容：FILE\_RENAME = 0x1C801102 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuthEvent；  API声明：FILE\_DELETE = 0x1C801103  差异内容：FILE\_DELETE = 0x1C801103 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuthEvent；  API声明：FILE\_SETEXTATTR = 0x1C801104  差异内容：FILE\_SETEXTATTR = 0x1C801104 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuthEvent；  API声明：FILE\_DELETEEXTATTR = 0x1C801105  差异内容：FILE\_DELETEEXTATTR = 0x1C801105 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit；  API声明：enum AuthResult  差异内容：enum AuthResult | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuthResult；  API声明：ALLOW = 0  差异内容：ALLOW = 0 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuthResult；  API声明：DENY = 1  差异内容：DENY = 1 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit；  API声明：interface AuthClient  差异内容：interface AuthClient | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuthClient；  API声明：subscribe(events: AuthEvent[]): void;  差异内容：subscribe(events: AuthEvent[]): void; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuthClient；  API声明：unsubscribe(events: AuthEvent[]): void;  差异内容：unsubscribe(events: AuthEvent[]): void; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuthClient；  API声明：addFilter(event: AuthEvent, filter: Filter): void;  差异内容：addFilter(event: AuthEvent, filter: Filter): void; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuthClient；  API声明：removeFilter(event: AuthEvent, filter: Filter): void;  差异内容：removeFilter(event: AuthEvent, filter: Filter): void; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuthClient；  API声明：auth(auditEvent: AuditEvent, authResult: AuthResult): void;  差异内容：auth(auditEvent: AuditEvent, authResult: AuthResult): void; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit；  API声明：function newAuthClient(callback: Callback<AuditEvent>): AuthClient;  差异内容：function newAuthClient(callback: Callback<AuditEvent>): AuthClient; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit；  API声明：function deleteAuthClient(client: AuthClient): void;  差异内容：function deleteAuthClient(client: AuthClient): void; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit；  API声明：function queryAllProcesses(): string;  差异内容：function queryAllProcesses(): string; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit；  API声明：function queryProcesses(pids: number[]): string;  差异内容：function queryProcesses(pids: number[]): string; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_GET\_REMAIN\_TIME = 1019100017  差异内容：TRUSTED\_AUTH\_ERROR\_GET\_REMAIN\_TIME = 1019100017 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_DISABLE\_BIO\_AUTH = 1019100018  差异内容：TRUSTED\_AUTH\_ERROR\_DISABLE\_BIO\_AUTH = 1019100018 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_BIO\_MISMATCH = 1019100019  差异内容：TRUSTED\_AUTH\_ERROR\_BIO\_MISMATCH = 1019100019 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_BIO\_REPEATED\_BIND = 1019100020  差异内容：TRUSTED\_AUTH\_ERROR\_BIO\_REPEATED\_BIND = 1019100020 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_NOT\_BIND\_BIO = 1019100021  差异内容：TRUSTED\_AUTH\_ERROR\_NOT\_BIND\_BIO = 1019100021 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication；  API声明：function getRemainAuthTimes(authID: bigint): Promise<number>;  差异内容：function getRemainAuthTimes(authID: bigint): Promise<number>; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication；  API声明：function disableTrustedBioAuthentication(authID: bigint, authType: AuthType): Promise<void>;  差异内容：function disableTrustedBioAuthentication(authID: bigint, authType: AuthType): Promise<void>; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：businessRiskIntelligentDetection；  API声明：interface SimulatedClickDetectionRequest  差异内容：interface SimulatedClickDetectionRequest | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增API | NA | 类名：SimulatedClickDetectionRequest；  API声明：version?: number;  差异内容：version?: number; | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增API | NA | 类名：businessRiskIntelligentDetection；  API声明：function detectSimulatedClickRisk(params: SimulatedClickDetectionRequest): Promise<string>;  差异内容：function detectSimulatedClickRisk(params: SimulatedClickDetectionRequest): Promise<string>; | api/@hms.security.businessRiskIntelligentDetection.d.ts |
