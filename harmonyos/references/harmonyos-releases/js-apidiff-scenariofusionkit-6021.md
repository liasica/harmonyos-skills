---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-scenariofusionkit-6021
title: Scenario Fusion Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.2(22) > OS平台能力 > API变更清单 > Scenario Fusion Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:48+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:7a63abfc78ddbe8d028af4846237cb954d5aedb9c4cefb5573a2393aa1368964
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：functionalButtonComponentManager；  API声明：export enum CredentialType  差异内容：NA | 类名：functionalButtonComponentManager；  API声明：export enum CredentialType  差异内容：22 | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| API废弃版本变更 | 类名：CredentialType；  API声明：IDCard = 0  差异内容：NA | 类名：CredentialType；  API声明：IDCard = 0  差异内容：22 | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| API废弃版本变更 | 类名：functionalButtonComponentManager；  API声明：export interface RealNameAuthenticationInfo  差异内容：NA | 类名：functionalButtonComponentManager；  API声明：export interface RealNameAuthenticationInfo  差异内容：22 | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| API废弃版本变更 | 类名：RealNameAuthenticationInfo；  API声明：openID: string;  差异内容：NA | 类名：RealNameAuthenticationInfo；  API声明：openID: string;  差异内容：22 | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| API废弃版本变更 | 类名：RealNameAuthenticationInfo；  API声明：realName: string;  差异内容：NA | 类名：RealNameAuthenticationInfo；  API声明：realName: string;  差异内容：22 | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| API废弃版本变更 | 类名：RealNameAuthenticationInfo；  API声明：credentialID: Uint8Array;  差异内容：NA | 类名：RealNameAuthenticationInfo；  API声明：credentialID: Uint8Array;  差异内容：22 | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| API废弃版本变更 | 类名：RealNameAuthenticationInfo；  API声明：credentialType?: CredentialType;  差异内容：NA | 类名：RealNameAuthenticationInfo；  API声明：credentialType?: CredentialType;  差异内容：22 | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| API废弃版本变更 | 类名：FunctionalButtonParams；  API声明：realNameAuthenticationInfo?: RealNameAuthenticationInfo;  差异内容：NA | 类名：FunctionalButtonParams；  API声明：realNameAuthenticationInfo?: RealNameAuthenticationInfo;  差异内容：22 | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：OpenType；  API声明：GET\_PHONE\_NUMBER\_AND\_RISK\_LEVEL = 15  差异内容：GET\_PHONE\_NUMBER\_AND\_RISK\_LEVEL = 15 | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：functionalButtonComponentManager；  API声明：export interface GetPhoneNumberAndRiskLevelResult  差异内容：export interface GetPhoneNumberAndRiskLevelResult | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：GetPhoneNumberAndRiskLevelResult；  API声明：code?: string;  差异内容：code?: string; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：GetPhoneNumberAndRiskLevelResult；  API声明：errCode?: number;  差异内容：errCode?: number; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：GetPhoneNumberAndRiskLevelResult；  API声明：errMsg?: string;  差异内容：errMsg?: string; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：FunctionalButtonController；  API声明：onGetPhoneNumberAndRiskLevel(callback: Callback<GetPhoneNumberAndRiskLevelResult>): FunctionalButtonController;  差异内容：onGetPhoneNumberAndRiskLevel(callback: Callback<GetPhoneNumberAndRiskLevelResult>): FunctionalButtonController; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
