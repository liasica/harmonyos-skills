---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-scenariofusionkit-b123sp18
title: Scenario Fusion Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > OS平台能力 > API变更清单 > Scenario Fusion Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:53+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:d8da50c997d578884c1d2810f75051e403e0a7d35cef575d9d78705c48e16af5
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace fileUriService  差异内容： declare namespace fileUriService | api/@hms.core.scenarioFusionComponent.fileUriService.d.ts |
| 新增API | NA | 类名：fileUriService；  API声明：function convertFileUris(sourceFileUris: Array<string>): Promise<Array<FileUriResult>>;  差异内容：function convertFileUris(sourceFileUris: Array<string>): Promise<Array<FileUriResult>>; | api/@hms.core.scenarioFusionComponent.fileUriService.d.ts |
| 新增API | NA | 类名：fileUriService；  API声明： interface FileUriResult  差异内容： interface FileUriResult | api/@hms.core.scenarioFusionComponent.fileUriService.d.ts |
| 新增API | NA | 类名：FileUriResult；  API声明：sourceUri: string;  差异内容：sourceUri: string; | api/@hms.core.scenarioFusionComponent.fileUriService.d.ts |
| 新增API | NA | 类名：FileUriResult；  API声明：targetUri: string;  差异内容：targetUri: string; | api/@hms.core.scenarioFusionComponent.fileUriService.d.ts |
| 新增API | NA | 类名：FileUriResult；  API声明：targetType: TargetType;  差异内容：targetType: TargetType; | api/@hms.core.scenarioFusionComponent.fileUriService.d.ts |
| 新增API | NA | 类名：fileUriService；  API声明： export enum TargetType  差异内容： export enum TargetType | api/@hms.core.scenarioFusionComponent.fileUriService.d.ts |
| 新增API | NA | 类名：TargetType；  API声明：UNKNOWN = 0  差异内容：UNKNOWN = 0 | api/@hms.core.scenarioFusionComponent.fileUriService.d.ts |
| 新增API | NA | 类名：TargetType；  API声明：MEDIA = 1  差异内容：MEDIA = 1 | api/@hms.core.scenarioFusionComponent.fileUriService.d.ts |
| 新增API | NA | 类名：TargetType；  API声明：FILE = 2  差异内容：FILE = 2 | api/@hms.core.scenarioFusionComponent.fileUriService.d.ts |
| 新增API | NA | 类名：OpenType；  API声明：PERMISSION\_SETTING = 11  差异内容：PERMISSION\_SETTING = 11 | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：FunctionalButtonParams；  API声明：permissionListParam?: Array<Permissions>;  差异内容：permissionListParam?: Array<Permissions>; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：functionalButtonComponentManager；  API声明： export interface PermissionSettingResult  差异内容： export interface PermissionSettingResult | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：PermissionSettingResult；  API声明：permissionResult: Array<abilityAccessCtrl.GrantStatus>;  差异内容：permissionResult: Array<abilityAccessCtrl.GrantStatus>; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：FunctionalButtonController；  API声明：onPermissionSetting(callback: AsyncCallback<PermissionSettingResult>): FunctionalButtonController;  差异内容：onPermissionSetting(callback: AsyncCallback<PermissionSettingResult>): FunctionalButtonController; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
