---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-abilitykit-6012
title: Ability Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Release引入的API > Ability Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:52+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:8c41967cf1a750ef7ff9ec2520da4a8a10112a861bf5677efd432fa2107fd5b9
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API跨平台权限变更 | 类名：ApplicationContext；  API声明：setLanguage(language: string): void;  差异内容：NA | 类名：ApplicationContext；  API声明：setLanguage(language: string): void;  差异内容：crossplatform | api/application/ApplicationContext.d.ts |
| API跨平台权限变更 | 类名：ApplicationContext；  API声明：setFont(font: string): void;  差异内容：NA | 类名：ApplicationContext；  API声明：setFont(font: string): void;  差异内容：crossplatform | api/application/ApplicationContext.d.ts |
| API跨平台权限变更 | 类名：ApplicationContext；  API声明：setFontSizeScale(fontSizeScale: number): void;  差异内容：NA | 类名：ApplicationContext；  API声明：setFontSizeScale(fontSizeScale: number): void;  差异内容：crossplatform | api/application/ApplicationContext.d.ts |
| API跨平台权限变更 | 类名：UIAbilityContext；  API声明：windowStage: window.WindowStage;  差异内容：NA | 类名：UIAbilityContext；  API声明：windowStage: window.WindowStage;  差异内容：crossplatform | api/application/UIAbilityContext.d.ts |
| 删除错误码 | 类名：ApplicationContext；  API声明：setLanguage(language: string): void;  差异内容：401 | 类名：ApplicationContext；  API声明：setLanguage(language: string): void;  差异内容：NA | api/application/ApplicationContext.d.ts |
| 删除错误码 | 类名：ApplicationContext；  API声明：setFont(font: string): void;  差异内容：401 | 类名：ApplicationContext；  API声明：setFont(font: string): void;  差异内容：NA | api/application/ApplicationContext.d.ts |
| 删除错误码 | 类名：ApplicationContext；  API声明：setFontSizeScale(fontSizeScale: number): void;  差异内容：401 | 类名：ApplicationContext；  API声明：setFontSizeScale(fontSizeScale: number): void;  差异内容：NA | api/application/ApplicationContext.d.ts |
| 新增API | NA | 类名：ChildProcessOptions；  API声明：isolationUid?: boolean;  差异内容：isolationUid?: boolean; | api/@ohos.app.ability.ChildProcessOptions.d.ts |
