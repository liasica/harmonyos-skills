---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-7001
title: Device Security Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Device Security Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:06+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:228aab01d35d6e84196a86f3d3a7a59b2da05f7788b4488b109e7aca4ac965a5
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：trustedAuthentication；  API声明：function procContentAuthentication(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise<AuthToken>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function procContentAuthentication(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise<AuthToken>;  差异内容：1019100024 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace riskControlEngine  差异内容：declare namespace riskControlEngine | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：riskControlEngine；  API声明：type ValueType = number | boolean | string;  差异内容：type ValueType = number | boolean | string; | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：riskControlEngine；  API声明：interface AppFactorData  差异内容：interface AppFactorData | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：AppFactorData；  API声明：factorName: string;  差异内容：factorName: string; | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：AppFactorData；  API声明：factorValue: ValueType;  差异内容：factorValue: ValueType; | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：riskControlEngine；  API声明：interface ImportData  差异内容：interface ImportData | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：ImportData；  API声明：appFactorData: Array<AppFactorData>;  差异内容：appFactorData: Array<AppFactorData>; | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：ImportData；  API声明：nonce: string;  差异内容：nonce: string; | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：riskControlEngine；  API声明：function importRiskFactors(data: ImportData): Promise<void>;  差异内容：function importRiskFactors(data: ImportData): Promise<void>; | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：riskControlEngine；  API声明：interface RiskControlDetectionRequest  差异内容：interface RiskControlDetectionRequest | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：RiskControlDetectionRequest；  API声明：policyName: string;  差异内容：policyName: string; | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：RiskControlDetectionRequest；  API声明：nonce: string;  差异内容：nonce: string; | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：riskControlEngine；  API声明：interface RiskControlDetectionResponse  差异内容：interface RiskControlDetectionResponse | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：RiskControlDetectionResponse；  API声明：result: string;  差异内容：result: string; | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：riskControlEngine；  API声明：function getRiskControlResult(req: RiskControlDetectionRequest): Promise<RiskControlDetectionResponse>;  差异内容：function getRiskControlResult(req: RiskControlDetectionRequest): Promise<RiskControlDetectionResponse>; | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：safetyDetect；  API声明：enum RiskFactorType  差异内容：enum RiskFactorType | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType；  API声明：HDC\_DEBUG\_STATE = 'hdcDebugState'  差异内容：HDC\_DEBUG\_STATE = 'hdcDebugState' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType；  API声明：IS\_DEVELOPER\_MODE = 'isDeveloperMode'  差异内容：IS\_DEVELOPER\_MODE = 'isDeveloperMode' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType；  API声明：IS\_VPN\_STATUS = 'isVpnStatus'  差异内容：IS\_VPN\_STATUS = 'isVpnStatus' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType；  API声明：IS\_NET\_PROXY\_STATUS = 'isNetProxyStatus'  差异内容：IS\_NET\_PROXY\_STATUS = 'isNetProxyStatus' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType；  API声明：SIM\_CNT = 'simCnt'  差异内容：SIM\_CNT = 'simCnt' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType；  API声明：OOBE\_CNT = 'oobeCnt'  差异内容：OOBE\_CNT = 'oobeCnt' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType；  API声明：ODID\_RESET\_CNT = 'odidResetCnt'  差异内容：ODID\_RESET\_CNT = 'odidResetCnt' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType；  API声明：ODID = 'odid'  差异内容：ODID = 'odid' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType；  API声明：IS\_DISPLAY\_CAPTURED = 'isDisplayCaptured'  差异内容：IS\_DISPLAY\_CAPTURED = 'isDisplayCaptured' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType；  API声明：GLOBAL\_WINDOW\_STATE = 'globalWindowState'  差异内容：GLOBAL\_WINDOW\_STATE = 'globalWindowState' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType；  API声明：BATTERY\_CHARGE\_STATE = 'batteryChargeState'  差异内容：BATTERY\_CHARGE\_STATE = 'batteryChargeState' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType；  API声明：BATTERY\_HEALTH\_STATE = 'batteryHealthState'  差异内容：BATTERY\_HEALTH\_STATE = 'batteryHealthState' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType；  API声明：ON\_CALL\_STATE = 'onCallState'  差异内容：ON\_CALL\_STATE = 'onCallState' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：safetyDetect；  API声明：interface RiskFactorRequest  差异内容：interface RiskFactorRequest | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorRequest；  API声明：nonce: string;  差异内容：nonce: string; | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorRequest；  API声明：queries: Array<FactorQuery>;  差异内容：queries: Array<FactorQuery>; | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：safetyDetect；  API声明：interface FactorQuery  差异内容：interface FactorQuery | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：FactorQuery；  API声明：factor: RiskFactorType;  差异内容：factor: RiskFactorType; | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：safetyDetect；  API声明：interface RiskFactorResponse  差异内容：interface RiskFactorResponse | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorResponse；  API声明：result: string;  差异内容：result: string; | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：safetyDetect；  API声明：function queryRiskFactors(req: RiskFactorRequest): Promise<RiskFactorResponse>;  差异内容：function queryRiskFactors(req: RiskFactorRequest): Promise<RiskFactorResponse>; | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：FILE\_SHARE = 0x0F000002  差异内容：FILE\_SHARE = 0x0F000002 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：DATA\_DRAG = 0x0F000003  差异内容：DATA\_DRAG = 0x0F000003 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：DLP\_FILE\_ACCESS = 0x0F000006  差异内容：DLP\_FILE\_ACCESS = 0x0F000006 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：FILE\_CREATE = 0x1C001104  差异内容：FILE\_CREATE = 0x1C001104 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：FILE\_OPEN = 0x1C001105  差异内容：FILE\_OPEN = 0x1C001105 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：FILE\_CLOSE = 0x1C001106  差异内容：FILE\_CLOSE = 0x1C001106 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：FILE\_DELETE = 0x1C001107  差异内容：FILE\_DELETE = 0x1C001107 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：FILE\_RENAME = 0x1C001108  差异内容：FILE\_RENAME = 0x1C001108 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：FILE\_COPY = 0x1C001109  差异内容：FILE\_COPY = 0x1C001109 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：FILE\_SETOWNER = 0x1C00110A  差异内容：FILE\_SETOWNER = 0x1C00110A | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：FILE\_SETMODE = 0x1C00110B  差异内容：FILE\_SETMODE = 0x1C00110B | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：FILE\_SETEXTATTR = 0x1C00110C  差异内容：FILE\_SETEXTATTR = 0x1C00110C | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：FILE\_DELETEEXTATTR = 0x1C00110D  差异内容：FILE\_DELETEEXTATTR = 0x1C00110D | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：FILE\_WRITE = 0x1C00110E  差异内容：FILE\_WRITE = 0x1C00110E | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：FilterType；  API声明：FILE\_PATH\_REGULAR = 0x00010003  差异内容：FILE\_PATH\_REGULAR = 0x00010003 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit；  API声明：function acquireAllClientsInfo(): string;  差异内容：function acquireAllClientsInfo(): string; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：superPrivacyMode；  API声明：enum PrivacySensorType  差异内容：enum PrivacySensorType | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：PrivacySensorType；  API声明：CAMERA = 0  差异内容：CAMERA = 0 | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：PrivacySensorType；  API声明：MICROPHONE = 1  差异内容：MICROPHONE = 1 | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：PrivacySensorType；  API声明：LOCATION = 2  差异内容：LOCATION = 2 | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：superPrivacyMode；  API声明：enum PrivacySensorState  差异内容：enum PrivacySensorState | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：PrivacySensorState；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：PrivacySensorState；  API声明：ENABLED\_UNDER\_SUPER\_PRIVACY = 1  差异内容：ENABLED\_UNDER\_SUPER\_PRIVACY = 1 | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：PrivacySensorState；  API声明：DISABLED\_UNDER\_SUPER\_PRIVACY = 2  差异内容：DISABLED\_UNDER\_SUPER\_PRIVACY = 2 | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：superPrivacyMode；  API声明：interface SuperPrivacyPolicy  差异内容：interface SuperPrivacyPolicy | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：SuperPrivacyPolicy；  API声明：sensorType: PrivacySensorType;  差异内容：sensorType: PrivacySensorType; | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：SuperPrivacyPolicy；  API声明：sensorState: PrivacySensorState;  差异内容：sensorState: PrivacySensorState; | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：superPrivacyMode；  API声明：interface SuperPrivacyPolicyInfo  差异内容：interface SuperPrivacyPolicyInfo | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：SuperPrivacyPolicyInfo；  API声明：superPrivacyMode: SuperPrivacyMode;  差异内容：superPrivacyMode: SuperPrivacyMode; | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：SuperPrivacyPolicyInfo；  API声明：superPrivacyPolicies: SuperPrivacyPolicy[];  差异内容：superPrivacyPolicies: SuperPrivacyPolicy[]; | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：superPrivacyMode；  API声明：function getSuperPrivacyPolicies(): Promise<SuperPrivacyPolicyInfo>;  差异内容：function getSuperPrivacyPolicies(): Promise<SuperPrivacyPolicyInfo>; | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：superPrivacyMode；  API声明：function onSuperPrivacyModeOrPolicyChange(callback: Callback<SuperPrivacyPolicyInfo>): void;  差异内容：function onSuperPrivacyModeOrPolicyChange(callback: Callback<SuperPrivacyPolicyInfo>): void; | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：superPrivacyMode；  API声明：function offSuperPrivacyModeOrPolicyChange(callback?: Callback<SuperPrivacyPolicyInfo>): void;  差异内容：function offSuperPrivacyModeOrPolicyChange(callback?: Callback<SuperPrivacyPolicyInfo>): void; | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_BIO\_ID\_INVALID = 1019100024  差异内容：TRUSTED\_AUTH\_ERROR\_BIO\_ID\_INVALID = 1019100024 | api/@hms.security.trustedAuthentication.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.security.riskControlEngine.d.ts  差异内容：DeviceSecurityKit | api/@hms.security.riskControlEngine.d.ts |
| API从不支持元服务到支持元服务 | 类名：global；  API声明：declare namespace trustedAuthentication  差异内容：NA | 类名：global；  API声明：declare namespace trustedAuthentication  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication；  API声明：export enum AuthType  差异内容：NA | 类名：trustedAuthentication；  API声明：export enum AuthType  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：AuthType；  API声明：AUTH\_TYPE\_FACE = 2  差异内容：NA | 类名：AuthType；  API声明：AUTH\_TYPE\_FACE = 2  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：AuthType；  API声明：AUTH\_TYPE\_FINGERPRINT = 4  差异内容：NA | 类名：AuthType；  API声明：AUTH\_TYPE\_FINGERPRINT = 4  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：AuthType；  API声明：AUTH\_TYPE\_TUI\_PIN = 32  差异内容：NA | 类名：AuthType；  API声明：AUTH\_TYPE\_TUI\_PIN = 32  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication；  API声明：export enum PasswordType  差异内容：NA | 类名：trustedAuthentication；  API声明：export enum PasswordType  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：PasswordType；  API声明：PASSWORD\_TYPE\_DIGITAL = 0  差异内容：NA | 类名：PasswordType；  API声明：PASSWORD\_TYPE\_DIGITAL = 0  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：PasswordType；  API声明：PASSWORD\_TYPE\_MIXED = 1  差异内容：NA | 类名：PasswordType；  API声明：PASSWORD\_TYPE\_MIXED = 1  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication；  API声明：export enum OperateType  差异内容：NA | 类名：trustedAuthentication；  API声明：export enum OperateType  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：OperateType；  API声明：OPERATE\_TYPE\_BIOMETRIC\_AUTH = 1  差异内容：NA | 类名：OperateType；  API声明：OPERATE\_TYPE\_BIOMETRIC\_AUTH = 1  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：OperateType；  API声明：OPERATE\_TYPE\_CONTENT\_AUTH = 2  差异内容：NA | 类名：OperateType；  API声明：OPERATE\_TYPE\_CONTENT\_AUTH = 2  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication；  API声明：export enum TrustedAuthErrorCode  差异内容：NA | 类名：trustedAuthentication；  API声明：export enum TrustedAuthErrorCode  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_NO\_PERMISSION = 1019100001  差异内容：NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_NO\_PERMISSION = 1019100001  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_ILLEGAL\_ARGUMENT = 1019100002  差异内容：NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_ILLEGAL\_ARGUMENT = 1019100002  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_PWD\_LIMIT\_REACHED = 1019100003  差异内容：NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_PWD\_LIMIT\_REACHED = 1019100003  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_PWD\_DELETE\_FAILED = 1019100004  差异内容：NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_PWD\_DELETE\_FAILED = 1019100004  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_VERIFY\_FAILED = 1019100005  差异内容：NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_VERIFY\_FAILED = 1019100005  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_CHECK\_CONFIRM\_TEXT\_FAILED = 1019100006  差异内容：NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_CHECK\_CONFIRM\_TEXT\_FAILED = 1019100006  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_NOT\_SUPPORT\_IMAGE = 1019100007  差异内容：NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_NOT\_SUPPORT\_IMAGE = 1019100007  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_USER\_REQ\_CANCEL = 1019100008  差异内容：NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_USER\_REQ\_CANCEL = 1019100008  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_EXPORT\_DATA\_FAILED = 1019100009  差异内容：NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_EXPORT\_DATA\_FAILED = 1019100009  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_IMPORT\_DATA\_FAILED = 1019100010  差异内容：NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_IMPORT\_DATA\_FAILED = 1019100010  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_INVALID\_CONTENT = 1019100011  差异内容：NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_INVALID\_CONTENT = 1019100011  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_INVALID\_AUTH\_ID = 1019100012  差异内容：NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_INVALID\_AUTH\_ID = 1019100012  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_SET\_PWD\_FAILED = 1019100013  差异内容：NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_SET\_PWD\_FAILED = 1019100013  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_MODIFY\_PWD\_FAILED = 1019100014  差异内容：NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_MODIFY\_PWD\_FAILED = 1019100014  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_BIO\_RESIGN\_FAILED = 1019100015  差异内容：NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_BIO\_RESIGN\_FAILED = 1019100015  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_FEATURE\_INITIALIZATION\_FAILED = 1019100016  差异内容：NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_FEATURE\_INITIALIZATION\_FAILED = 1019100016  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_GET\_REMAIN\_TIME = 1019100017  差异内容：NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_GET\_REMAIN\_TIME = 1019100017  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_DISABLE\_BIO\_AUTH = 1019100018  差异内容：NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_DISABLE\_BIO\_AUTH = 1019100018  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_BIO\_MISMATCH = 1019100019  差异内容：NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_BIO\_MISMATCH = 1019100019  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_BIO\_REPEATED\_BIND = 1019100020  差异内容：NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_BIO\_REPEATED\_BIND = 1019100020  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_NOT\_BIND\_BIO = 1019100021  差异内容：NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_NOT\_BIND\_BIO = 1019100021  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_TUI\_OCCUPIED = 1019100025  差异内容：NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_TUI\_OCCUPIED = 1019100025  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication；  API声明：export interface PasswordInfo  差异内容：NA | 类名：trustedAuthentication；  API声明：export interface PasswordInfo  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：PasswordInfo；  API声明：pwdType: PasswordType;  差异内容：NA | 类名：PasswordInfo；  API声明：pwdType: PasswordType;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：PasswordInfo；  API声明：pwdMaxLength: number;  差异内容：NA | 类名：PasswordInfo；  API声明：pwdMaxLength: number;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：PasswordInfo；  API声明：pwdMinLength: number;  差异内容：NA | 类名：PasswordInfo；  API声明：pwdMinLength: number;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：PasswordInfo；  API声明：maxAuthFailCount: number;  差异内容：NA | 类名：PasswordInfo；  API声明：maxAuthFailCount: number;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication；  API声明：export interface AuthReqParams  差异内容：NA | 类名：trustedAuthentication；  API声明：export interface AuthReqParams  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：AuthReqParams；  API声明：reqType: AuthType;  差异内容：NA | 类名：AuthReqParams；  API声明：reqType: AuthType;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：AuthReqParams；  API声明：authContent: Array<string>;  差异内容：NA | 类名：AuthReqParams；  API声明：authContent: Array<string>;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication；  API声明：export interface TUILable  差异内容：NA | 类名：trustedAuthentication；  API声明：export interface TUILable  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TUILable；  API声明：image: ArrayBuffer;  差异内容：NA | 类名：TUILable；  API声明：image: ArrayBuffer;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TUILable；  API声明：title: string;  差异内容：NA | 类名：TUILable；  API声明：title: string;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication；  API声明：export interface AuthToken  差异内容：NA | 类名：trustedAuthentication；  API声明：export interface AuthToken  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：AuthToken；  API声明：authToken: Uint8Array;  差异内容：NA | 类名：AuthToken；  API声明：authToken: Uint8Array;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication；  API声明：export interface AuthInfo  差异内容：NA | 类名：trustedAuthentication；  API声明：export interface AuthInfo  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：AuthInfo；  API声明：authToken: Uint8Array;  差异内容：NA | 类名：AuthInfo；  API声明：authToken: Uint8Array;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：AuthInfo；  API声明：authID: bigint;  差异内容：NA | 类名：AuthInfo；  API声明：authID: bigint;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication；  API声明：export interface TextCheckResult  差异内容：NA | 类名：trustedAuthentication；  API声明：export interface TextCheckResult  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextCheckResult；  API声明：result: number;  差异内容：NA | 类名：TextCheckResult；  API声明：result: number;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextCheckResult；  API声明：lastIndex: number;  差异内容：NA | 类名：TextCheckResult；  API声明：lastIndex: number;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication；  API声明：function enableTrustedAuthentication(challenge: Uint8Array, pwdInfo: PasswordInfo, label: TUILable): Promise<AuthInfo>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function enableTrustedAuthentication(challenge: Uint8Array, pwdInfo: PasswordInfo, label: TUILable): Promise<AuthInfo>;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication；  API声明：function modifyTrustedAuthenticationPwd(challenge: Uint8Array, pwdInfo: PasswordInfo, authID: bigint, label: TUILable): Promise<AuthToken>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function modifyTrustedAuthenticationPwd(challenge: Uint8Array, pwdInfo: PasswordInfo, authID: bigint, label: TUILable): Promise<AuthToken>;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication；  API声明：function disableTrustedAuthentication(challenge: Uint8Array, needAuth: boolean, authID: bigint, label: TUILable): Promise<AuthToken>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function disableTrustedAuthentication(challenge: Uint8Array, needAuth: boolean, authID: bigint, label: TUILable): Promise<AuthToken>;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication；  API声明：function trustedAuthentication(challenge: Uint8Array, authID: bigint, label: TUILable): Promise<AuthToken>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function trustedAuthentication(challenge: Uint8Array, authID: bigint, label: TUILable): Promise<AuthToken>;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication；  API声明：function procContentAuthentication(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise<AuthToken>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function procContentAuthentication(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise<AuthToken>;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication；  API声明：function getBiometricAuthToken(operType: OperateType, tuiAuthToken: Uint8Array, bioAuthToken: Uint8Array): Promise<AuthToken>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function getBiometricAuthToken(operType: OperateType, tuiAuthToken: Uint8Array, bioAuthToken: Uint8Array): Promise<AuthToken>;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication；  API声明：function importData(data: ArrayBuffer, authID: bigint): Promise<void>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function importData(data: ArrayBuffer, authID: bigint): Promise<void>;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication；  API声明：function exportData(authID: bigint, label: TUILable): Promise<ArrayBuffer>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function exportData(authID: bigint, label: TUILable): Promise<ArrayBuffer>;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication；  API声明：function checkConfirmUITextFormat(text: string): Promise<TextCheckResult>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function checkConfirmUITextFormat(text: string): Promise<TextCheckResult>;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication；  API声明：function getRemainAuthTimes(authID: bigint): Promise<number>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function getRemainAuthTimes(authID: bigint): Promise<number>;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication；  API声明：function disableTrustedBioAuthentication(authID: bigint, authType: AuthType): Promise<void>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function disableTrustedBioAuthentication(authID: bigint, authType: AuthType): Promise<void>;  差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
