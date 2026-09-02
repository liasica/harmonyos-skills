---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-abilitykit-7003
title: Ability Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Release引入的API > Ability Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8ba984510f06ada68ca88d79ce29822c52e8e187849a2d4e1716e42e5d154e05
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| syscap变更 | 类名：systemConfiguration；  API声明：interface UpdatedCallback  差异内容：SystemCapability.Ability.AbilityRuntime.AbilityCore | 类名：systemConfiguration；  API声明：interface UpdatedCallback  差异内容：SystemCapability.Ability.AbilityRuntime.Core | api/@ohos.app.ability.systemConfiguration.d.ts |
| 新增错误码 | 类名：AtManager；  API声明：requestPermissionOnSetting(context: Context, permissionList: Array<Permissions>): Promise<Array<GrantStatus>>;  差异内容：NA | 类名：AtManager；  API声明：requestPermissionOnSetting(context: Context, permissionList: Array<Permissions>): Promise<Array<GrantStatus>>;  差异内容：12100010 | api/@ohos.abilityAccessCtrl.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace appMemoryOptimizer  差异内容：declare namespace appMemoryOptimizer | api/@ohos.app.ability.appMemoryOptimizer.d.ts |
| 新增API | NA | 类名：appMemoryOptimizer；  API声明：function evictFilePages(fileNames: Array<string>): Promise<void>;  差异内容：function evictFilePages(fileNames: Array<string>): Promise<void>; | api/@ohos.app.ability.appMemoryOptimizer.d.ts |
| 新增API | NA | 类名：appMemoryOptimizer；  API声明：function evictModuleFilePages(moduleNames: Array<string>): Promise<void>;  差异内容：function evictModuleFilePages(moduleNames: Array<string>): Promise<void>; | api/@ohos.app.ability.appMemoryOptimizer.d.ts |
| 新增API | NA | 类名：AbilityStage；  API声明：onAboutToCreateAbilityAsync(): Promise<void>;  差异内容：onAboutToCreateAbilityAsync(): Promise<void>; | api/@ohos.app.ability.AbilityStage.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.app.ability.appMemoryOptimizer.d.ts  差异内容：AbilityKit | api/@ohos.app.ability.appMemoryOptimizer.d.ts |
