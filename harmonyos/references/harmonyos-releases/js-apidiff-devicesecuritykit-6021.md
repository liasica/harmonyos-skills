---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-6021
title: Device Security Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.2(22) > OS平台能力 > API变更清单 > Device Security Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:45+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:a227c89227c6dd81fe2fd38b1273e83465ebfac371c85c871e52f29917ffb7cb
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace superPrivacyMode  差异内容：declare namespace superPrivacyMode | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：superPrivacyMode；  API声明：function getSuperPrivacyMode(): Promise<SuperPrivacyMode>;  差异内容：function getSuperPrivacyMode(): Promise<SuperPrivacyMode>; | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：superPrivacyMode；  API声明：function on(type: 'superPrivacyModeChange', callback: Callback<SuperPrivacyMode>): void;  差异内容：function on(type: 'superPrivacyModeChange', callback: Callback<SuperPrivacyMode>): void; | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：superPrivacyMode；  API声明：enum SuperPrivacyMode  差异内容：enum SuperPrivacyMode | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：SuperPrivacyMode；  API声明：OFF = 0  差异内容：OFF = 0 | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：SuperPrivacyMode；  API声明：ON\_WHEN\_FOLDED = 1  差异内容：ON\_WHEN\_FOLDED = 1 | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：SuperPrivacyMode；  API声明：ALWAYS\_ON = 2  差异内容：ALWAYS\_ON = 2 | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：superPrivacyMode；  API声明：function off(type: 'superPrivacyModeChange', callback?: Callback<SuperPrivacyMode>): void;  差异内容：function off(type: 'superPrivacyModeChange', callback?: Callback<SuperPrivacyMode>): void; | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：businessRiskIntelligentDetection；  API声明：interface SimulatedClickDetectionEnhancedRequest  差异内容：interface SimulatedClickDetectionEnhancedRequest | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增API | NA | 类名：SimulatedClickDetectionEnhancedRequest；  API声明：version?: number;  差异内容：version?: number; | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增API | NA | 类名：SimulatedClickDetectionEnhancedRequest；  API声明：nonce: Uint8Array;  差异内容：nonce: Uint8Array; | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增API | NA | 类名：SimulatedClickDetectionEnhancedRequest；  API声明：algorithm: SigningAlgorithm;  差异内容：algorithm: SigningAlgorithm; | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增API | NA | 类名：businessRiskIntelligentDetection；  API声明：function detectSimulatedClickRiskEnhanced(params: SimulatedClickDetectionEnhancedRequest): Promise<string>;  差异内容：function detectSimulatedClickRiskEnhanced(params: SimulatedClickDetectionEnhancedRequest): Promise<string>; | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.security.superPrivacyMode.d.ts  差异内容：DeviceSecurityKit | api/@hms.security.superPrivacyMode.d.ts |
