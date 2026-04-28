---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-abilitykit-5032
title: Ability Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta2引入的API > Ability Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:32+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:7357519210c17868f9dc547b0171ca57a2b386b1ffcd0f2dabe907624c9fe216
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：appManager；  API声明：function off(type: 'applicationState', observerId: number, callback: AsyncCallback<void>): void;  差异内容：function off(type: 'applicationState', observerId: number, callback: AsyncCallback<void>): void; | api/@ohos.app.ability.appManager.d.ts |
| 新增API | NA | 类名：AbilityConstant；  API声明： export enum PrepareTermination  差异内容： export enum PrepareTermination | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：PrepareTermination；  API声明：TERMINATE\_IMMEDIATELY = 0  差异内容：TERMINATE\_IMMEDIATELY = 0 | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：PrepareTermination；  API声明：CANCEL = 1  差异内容：CANCEL = 1 | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：AbilityStage；  API声明：onPrepareTermination(): AbilityConstant.PrepareTermination;  差异内容：onPrepareTermination(): AbilityConstant.PrepareTermination; | api/@ohos.app.ability.AbilityStage.d.ts |
| 新增API | NA | 类名：AbilityStage；  API声明：onPrepareTerminationAsync(): Promise<AbilityConstant.PrepareTermination>;  差异内容：onPrepareTerminationAsync(): Promise<AbilityConstant.PrepareTermination>; | api/@ohos.app.ability.AbilityStage.d.ts |
| 新增API | NA | 类名：UIAbility；  API声明：onPrepareToTerminateAsync(): Promise<boolean>;  差异内容：onPrepareToTerminateAsync(): Promise<boolean>; | api/@ohos.app.ability.UIAbility.d.ts |
| 新增API | NA | 类名：Context；  API声明：createDisplayContext(displayId: number): Context;  差异内容：createDisplayContext(displayId: number): Context; | api/application/Context.d.ts |
| 新增API | NA | 类名：UIAbilityContext；  API声明：setAbilityInstanceInfo(label: string, icon: image.PixelMap): Promise<void>;  差异内容：setAbilityInstanceInfo(label: string, icon: image.PixelMap): Promise<void>; | api/application/UIAbilityContext.d.ts |
