---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-scenariofusionkit-b031
title: Scenario Fusion Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Scenario Fusion Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:42+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:696b1f4bd07d70524fffa5975e11d6c88fde55b4dc57cfb1721c5f43a72e9900
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：OpenType；  API声明：REAL\_NAME\_AUTHENTICATION = 7  差异内容：REAL\_NAME\_AUTHENTICATION = 7 | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：OpenType；  API声明：FACE\_AUTHENTICATION = 8  差异内容：FACE\_AUTHENTICATION = 8 | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：functionalButtonComponentManager；  API声明： export interface RealNameAuthenticationResult  差异内容： export interface RealNameAuthenticationResult | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：RealNameAuthenticationResult；  API声明：authCode?: string;  差异内容：authCode?: string; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：RealNameAuthenticationResult；  API声明：openID?: string;  差异内容：openID?: string; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：functionalButtonComponentManager；  API声明： export interface FaceAuthenticationResult  差异内容： export interface FaceAuthenticationResult | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：FaceAuthenticationResult；  API声明：authCode?: string;  差异内容：authCode?: string; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：FaceAuthenticationResult；  API声明：openID?: string;  差异内容：openID?: string; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：functionalButtonComponentManager；  API声明： export interface FaceVerificationResult  差异内容： export interface FaceVerificationResult | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：FaceVerificationResult；  API声明：facialRecognitionVerificationToken?: string;  差异内容：facialRecognitionVerificationToken?: string; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：FaceVerificationResult；  API声明：state?: string;  差异内容：state?: string; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：FunctionalButtonController；  API声明：onRealNameAuthentication(callback: AsyncCallback<RealNameAuthenticationResult>): FunctionalButtonController;  差异内容：onRealNameAuthentication(callback: AsyncCallback<RealNameAuthenticationResult>): FunctionalButtonController; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：FunctionalButtonController；  API声明：onFaceAuthentication(callback: AsyncCallback<FaceAuthenticationResult>): FunctionalButtonController;  差异内容：onFaceAuthentication(callback: AsyncCallback<FaceAuthenticationResult>): FunctionalButtonController; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：FunctionalButtonController；  API声明：onFaceVerification(verifyToken: string, callback: AsyncCallback<FaceVerificationResult>): void;  差异内容：onFaceVerification(verifyToken: string, callback: AsyncCallback<FaceVerificationResult>): void; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
