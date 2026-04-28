---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-abilitykit-b065
title: Ability Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Beta引入的API > Ability Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:14+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:e1f5dc03c40ed976916c70f3f724cc00cb93f433064e8d8faaf0711725c5e4d2
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：Context；  API声明：createModuleContext(moduleName: string): Context;  差异内容：NA | 类名：Context；  API声明：createModuleContext(moduleName: string): Context;  差异内容：12 | api/application/Context.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace application  差异内容： declare namespace application | api/@ohos.app.ability.application.d.ts |
| 新增API | NA | 类名：application；  API声明：export function createModuleContext(context: Context, moduleName: string): Promise<Context>;  差异内容：export function createModuleContext(context: Context, moduleName: string): Promise<Context>; | api/@ohos.app.ability.application.d.ts |
| 新增API | NA | 类名：LaunchReason；  API声明：PREPARE\_CONTINUATION = 10  差异内容：PREPARE\_CONTINUATION = 10 | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：Params；  API声明：CALLER\_REQUEST\_CODE = 'ohos.extra.param.key.callerRequestCode'  差异内容：CALLER\_REQUEST\_CODE = 'ohos.extra.param.key.callerRequestCode' | api/@ohos.app.ability.wantConstant.d.ts |
| 新增API | NA | 类名：UIAbilityContext；  API声明：backToCallerAbilityWithResult(abilityResult: AbilityResult, requestCode: string): Promise<void>;  差异内容：backToCallerAbilityWithResult(abilityResult: AbilityResult, requestCode: string): Promise<void>; | api/application/UIAbilityContext.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly cloudFileSyncEnabled: boolean;  差异内容：readonly cloudFileSyncEnabled: boolean; | api/bundleManager/ApplicationInfo.d.ts |
