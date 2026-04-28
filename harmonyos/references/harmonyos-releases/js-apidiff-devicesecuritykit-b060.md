---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-b060
title: Device Security Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta5引入的API > Device Security Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:26+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:e51a9f7c0d984d33eb4f0a13464e7200545d2106769788a429c321aefad7880c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace businessRiskIntelligentDetection  差异内容： declare namespace businessRiskIntelligentDetection | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增API | NA | 类名：businessRiskIntelligentDetection；  API声明： enum SigningAlgorithm  差异内容： enum SigningAlgorithm | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增API | NA | 类名：SigningAlgorithm；  API声明：ES256 = 0  差异内容：ES256 = 0 | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增API | NA | 类名：businessRiskIntelligentDetection；  API声明： interface FraudDetectionRequest  差异内容： interface FraudDetectionRequest | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增API | NA | 类名：FraudDetectionRequest；  API声明：nonce: Uint8Array;  差异内容：nonce: Uint8Array; | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增API | NA | 类名：FraudDetectionRequest；  API声明：algorithm: SigningAlgorithm;  差异内容：algorithm: SigningAlgorithm; | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增API | NA | 类名：businessRiskIntelligentDetection；  API声明：function detectFraudRisk(params: FraudDetectionRequest): Promise<string>;  差异内容：function detectFraudRisk(params: FraudDetectionRequest): Promise<string>; | api/@hms.security.businessRiskIntelligentDetection.d.ts |
