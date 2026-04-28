---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-formkit-510
title: Form Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Form Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:09+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:c764bfec82b81b805e084fddb83cf28349a359b9d13003a107382f42b66282f1
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：export default class FormEditExtensionAbility  差异内容：export default class FormEditExtensionAbility | api/@ohos.app.form.FormEditExtensionAbility.d.ts |
| 新增API | NA | 类名：FormEditExtensionAbility；  API声明：context: FormEditExtensionContext;  差异内容：context: FormEditExtensionContext; | api/@ohos.app.form.FormEditExtensionAbility.d.ts |
| 新增API | NA | 类名：global；  API声明：export default class FormEditExtensionContext  差异内容：export default class FormEditExtensionContext | api/application/FormEditExtensionContext.d.ts |
| 新增API | NA | 类名：FormEditExtensionContext；  API声明：startSecondPage(want: Want): Promise<AbilityResult>;  差异内容：startSecondPage(want: Want): Promise<AbilityResult>; | api/application/FormEditExtensionContext.d.ts |
| 新增API | NA | 类名：FormDimension；  API声明：DIMENSION\_2\_3 = 8  差异内容：DIMENSION\_2\_3 = 8 | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：FormDimension；  API声明：DIMENSION\_3\_3 = 9  差异内容：DIMENSION\_3\_3 = 9 | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：formProvider；  API声明：function openFormEditAbility(abilityName: string, formId: string, isMainPage?: boolean): void;  差异内容：function openFormEditAbility(abilityName: string, formId: string, isMainPage?: boolean): void; | api/@ohos.app.form.formProvider.d.ts |
| 新增API | NA | 类名：formProvider；  API声明：function getPublishedFormInfoById(formId: string): Promise<formInfo.FormInfo>;  差异内容：function getPublishedFormInfoById(formId: string): Promise<formInfo.FormInfo>; | api/@ohos.app.form.formProvider.d.ts |
| 新增API | NA | 类名：formProvider；  API声明：function getPublishedFormInfos(): Promise<Array<formInfo.FormInfo>>;  差异内容：function getPublishedFormInfos(): Promise<Array<formInfo.FormInfo>>; | api/@ohos.app.form.formProvider.d.ts |
| 新增API | NA | 类名：formProvider；  API声明：function openFormManager(want: Want): void;  差异内容：function openFormManager(want: Want): void; | api/@ohos.app.form.formProvider.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.app.form.FormEditExtensionAbility.d.ts  差异内容：FormKit | api/@ohos.app.form.FormEditExtensionAbility.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\application\FormEditExtensionContext.d.ts  差异内容：FormKit | api/application/FormEditExtensionContext.d.ts |
