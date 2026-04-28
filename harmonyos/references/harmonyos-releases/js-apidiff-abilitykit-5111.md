---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-abilitykit-5111
title: Ability Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Beta1引入的API > Ability Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:49+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:6ced1313c71e77251a4fc23cd78c5c578738c4e97b376291a3c84b4a63abfaba
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：continueManager；  API声明：function on(type: 'prepareContinue', context: Context, callback: AsyncCallback<ContinueResultInfo>): void;  差异内容：401 | 类名：continueManager；  API声明：function on(type: 'prepareContinue', context: Context, callback: AsyncCallback<ContinueResultInfo>): void;  差异内容：NA | api/@ohos.app.ability.continueManager.d.ts |
| 删除错误码 | 类名：continueManager；  API声明：function off(type: 'prepareContinue', context: Context, callback?: AsyncCallback<ContinueResultInfo>): void;  差异内容：401 | 类名：continueManager；  API声明：function off(type: 'prepareContinue', context: Context, callback?: AsyncCallback<ContinueResultInfo>): void;  差异内容：NA | api/@ohos.app.ability.continueManager.d.ts |
| 删除错误码 | 类名：UIExtensionContentSession；  API声明：loadContentByName(name: string, storage?: LocalStorage): void;  差异内容：401 | 类名：UIExtensionContentSession；  API声明：loadContentByName(name: string, storage?: LocalStorage): void;  差异内容：NA | api/@ohos.app.ability.UIExtensionContentSession.d.ts |
| 删除错误码 | 类名：Context；  API声明：createAreaModeContext(areaMode: contextConstant.AreaMode): Context;  差异内容：401 | 类名：Context；  API声明：createAreaModeContext(areaMode: contextConstant.AreaMode): Context;  差异内容：NA | api/application/Context.d.ts |
| 删除错误码 | 类名：UIAbilityContext；  API声明：setColorMode(colorMode: ConfigurationConstant.ColorMode): void;  差异内容：401 | 类名：UIAbilityContext；  API声明：setColorMode(colorMode: ConfigurationConstant.ColorMode): void;  差异内容：NA | api/application/UIAbilityContext.d.ts |
| 删除错误码 | 类名：UIExtensionContext；  API声明：setColorMode(colorMode: ConfigurationConstant.ColorMode): void;  差异内容：401 | 类名：UIExtensionContext；  API声明：setColorMode(colorMode: ConfigurationConstant.ColorMode): void;  差异内容：NA | api/application/UIExtensionContext.d.ts |
| 新增API | NA | 类名：application；  API声明：export function createPluginModuleContext(context: Context, pluginBundleName: string, pluginModuleName: string): Promise<Context>;  差异内容：export function createPluginModuleContext(context: Context, pluginBundleName: string, pluginModuleName: string): Promise<Context>; | api/@ohos.app.ability.application.d.ts |
| 新增API | NA | 类名：Params；  API声明：APP\_LAUNCH\_TRUSTLIST = 'ohos.params.appLaunchTrustList'  差异内容：APP\_LAUNCH\_TRUSTLIST = 'ohos.params.appLaunchTrustList' | api/@ohos.app.ability.wantConstant.d.ts |
| 新增API | NA | 类名：Params；  API声明：DESTINATION\_PLUGIN\_ABILITY = 'ohos.params.pluginAbility'  差异内容：DESTINATION\_PLUGIN\_ABILITY = 'ohos.params.pluginAbility' | api/@ohos.app.ability.wantConstant.d.ts |
| 新增API | NA | 类名：ExtensionAbilityType；  API声明：CALLER\_INFO\_QUERY = 25  差异内容：CALLER\_INFO\_QUERY = 25 | api/@ohos.bundle.bundleManager.d.ts |
