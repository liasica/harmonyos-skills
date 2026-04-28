---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-formkit-6001
title: Form Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > Form Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:40+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:f1aac82ca3d7c38e0c982755fd432aadbe0ae4f42b1981c283114fda6bd8e000
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：FormInfo；  API声明：colorMode: ColorMode;  差异内容：NA | 类名：FormInfo；  API声明：colorMode: ColorMode;  差异内容：20 | api/@ohos.app.form.formInfo.d.ts |
| API废弃版本变更 | 类名：formInfo；  API声明：enum ColorMode  差异内容：NA | 类名：formInfo；  API声明：enum ColorMode  差异内容：20 | api/@ohos.app.form.formInfo.d.ts |
| API废弃版本变更 | 类名：ColorMode；  API声明：MODE\_AUTO = -1  差异内容：NA | 类名：ColorMode；  API声明：MODE\_AUTO = -1  差异内容：20 | api/@ohos.app.form.formInfo.d.ts |
| API废弃版本变更 | 类名：ColorMode；  API声明：MODE\_DARK = 0  差异内容：NA | 类名：ColorMode；  API声明：MODE\_DARK = 0  差异内容：20 | api/@ohos.app.form.formInfo.d.ts |
| API废弃版本变更 | 类名：ColorMode；  API声明：MODE\_LIGHT = 1  差异内容：NA | 类名：ColorMode；  API声明：MODE\_LIGHT = 1  差异内容：20 | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface LiveFormInfo  差异内容：export interface LiveFormInfo | api/@ohos.app.form.LiveFormExtensionAbility.d.ts |
| 新增API | NA | 类名：LiveFormInfo；  API声明：formId: string;  差异内容：formId: string; | api/@ohos.app.form.LiveFormExtensionAbility.d.ts |
| 新增API | NA | 类名：LiveFormInfo；  API声明：rect: formInfo.Rect;  差异内容：rect: formInfo.Rect; | api/@ohos.app.form.LiveFormExtensionAbility.d.ts |
| 新增API | NA | 类名：LiveFormInfo；  API声明：borderRadius: number;  差异内容：borderRadius: number; | api/@ohos.app.form.LiveFormExtensionAbility.d.ts |
| 新增API | NA | 类名：global；  API声明：export default class LiveFormExtensionAbility  差异内容：export default class LiveFormExtensionAbility | api/@ohos.app.form.LiveFormExtensionAbility.d.ts |
| 新增API | NA | 类名：LiveFormExtensionAbility；  API声明：context: LiveFormExtensionContext;  差异内容：context: LiveFormExtensionContext; | api/@ohos.app.form.LiveFormExtensionAbility.d.ts |
| 新增API | NA | 类名：LiveFormExtensionAbility；  API声明：onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession): void;  差异内容：onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession): void; | api/@ohos.app.form.LiveFormExtensionAbility.d.ts |
| 新增API | NA | 类名：LiveFormExtensionAbility；  API声明：onLiveFormDestroy(liveFormInfo: LiveFormInfo): void;  差异内容：onLiveFormDestroy(liveFormInfo: LiveFormInfo): void; | api/@ohos.app.form.LiveFormExtensionAbility.d.ts |
| 新增API | NA | 类名：global；  API声明：export default class LiveFormExtensionContext  差异内容：export default class LiveFormExtensionContext | api/application/LiveFormExtensionContext.d.ts |
| 新增API | NA | 类名：LiveFormExtensionContext；  API声明：setBackgroundImage(res: Resource): Promise<void>;  差异内容：setBackgroundImage(res: Resource): Promise<void>; | api/application/LiveFormExtensionContext.d.ts |
| 新增API | NA | 类名：FormParam；  API声明：FORM\_WIDTH\_VP\_KEY = 'ohos.extra.param.key.form\_width\_vp'  差异内容：FORM\_WIDTH\_VP\_KEY = 'ohos.extra.param.key.form\_width\_vp' | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：FormParam；  API声明：FORM\_HEIGHT\_VP\_KEY = 'ohos.extra.param.key.form\_height\_vp'  差异内容：FORM\_HEIGHT\_VP\_KEY = 'ohos.extra.param.key.form\_height\_vp' | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：formInfo；  API声明：interface OverflowInfo  差异内容：interface OverflowInfo | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：OverflowInfo；  API声明：area: Rect;  差异内容：area: Rect; | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：OverflowInfo；  API声明：duration: number;  差异内容：duration: number; | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：formInfo；  API声明：interface Rect  差异内容：interface Rect | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：Rect；  API声明：left: number;  差异内容：left: number; | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：Rect；  API声明：top: number;  差异内容：top: number; | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：Rect；  API声明：width: number;  差异内容：width: number; | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：Rect；  API声明：height: number;  差异内容：height: number; | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：formProvider；  API声明：function requestOverflow(formId: string, overflowInfo: formInfo.OverflowInfo): Promise<void>;  差异内容：function requestOverflow(formId: string, overflowInfo: formInfo.OverflowInfo): Promise<void>; | api/@ohos.app.form.formProvider.d.ts |
| 新增API | NA | 类名：formProvider；  API声明：function cancelOverflow(formId: string): Promise<void>;  差异内容：function cancelOverflow(formId: string): Promise<void>; | api/@ohos.app.form.formProvider.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.app.form.LiveFormExtensionAbility.d.ts  差异内容：FormKit | api/@ohos.app.form.LiveFormExtensionAbility.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\application\LiveFormExtensionContext.d.ts  差异内容：FormKit | api/application/LiveFormExtensionContext.d.ts |
