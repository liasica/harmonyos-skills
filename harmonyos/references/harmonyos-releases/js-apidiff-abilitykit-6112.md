---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-abilitykit-6112
title: Ability Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Release引入的API > Ability Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:c96799031b953959bcfebce6a715bf0cde7aa1601684eaf443894988fa95d919
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：UIAbilityContext；  API声明：connectServiceExtensionAbility(want: Want, options: ConnectOptions): number;  差异内容：NA | 类名：UIAbilityContext；  API声明：connectServiceExtensionAbility(want: Want, options: ConnectOptions): number;  差异内容：16000012,16000013 | api/application/UIAbilityContext.d.ts |
| 新增错误码 | 类名：UIExtensionContext；  API声明：connectServiceExtensionAbility(want: Want, options: ConnectOptions): number;  差异内容：NA | 类名：UIExtensionContext；  API声明：connectServiceExtensionAbility(want: Want, options: ConnectOptions): number;  差异内容：16000012,16000013 | api/application/UIExtensionContext.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace hyperSnapManager  差异内容：declare namespace hyperSnapManager | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：hyperSnapManager；  API声明：function setHyperSnapEnabled(enableFlag: boolean): void;  差异内容：function setHyperSnapEnabled(enableFlag: boolean): void; | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：hyperSnapManager；  API声明：function requestRebuildHyperSnap(): void;  差异内容：function requestRebuildHyperSnap(): void; | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：AbilityStage；  API声明：onLaunchFromHyperSnap(): void;  差异内容：onLaunchFromHyperSnap(): void; | api/@ohos.app.ability.AbilityStage.d.ts |
| 新增API | NA | 类名：AbilityStage；  API声明：onAboutToCreateAbility(): void;  差异内容：onAboutToCreateAbility(): void; | api/@ohos.app.ability.AbilityStage.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.app.ability.hyperSnapManager.d.ts  差异内容：AbilityKit | api/@ohos.app.ability.hyperSnapManager.d.ts |
