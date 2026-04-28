---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-formkit-6002
title: Form Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > Form Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:29+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:28409eff8e1866ea1939078f1ae3108c8344f993ca43fb29211bc9c23691fb23
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：formProvider；  API声明：function getFormRect(formId: string): Promise<formInfo.Rect>;  差异内容：function getFormRect(formId: string): Promise<formInfo.Rect>; | api/@ohos.app.form.formProvider.d.ts |
| 删除API | 类名：FormParam；  API声明：FORM\_WIDTH\_VP\_KEY = 'ohos.extra.param.key.form\_width\_vp'  差异内容：FORM\_WIDTH\_VP\_KEY = 'ohos.extra.param.key.form\_width\_vp' | NA | api/@ohos.app.form.formInfo.d.ts |
| 删除API | 类名：FormParam；  API声明：FORM\_HEIGHT\_VP\_KEY = 'ohos.extra.param.key.form\_height\_vp'  差异内容：FORM\_HEIGHT\_VP\_KEY = 'ohos.extra.param.key.form\_height\_vp' | NA | api/@ohos.app.form.formInfo.d.ts |
| 删除API | 类名：LiveFormExtensionContext；  API声明：setBackgroundImage(res: Resource): Promise<void>;  差异内容：setBackgroundImage(res: Resource): Promise<void>; | NA | api/application/LiveFormExtensionContext.d.ts |
| API从不支持元服务到支持元服务 | 类名：formInfo；  API声明：interface OverflowInfo  差异内容：NA | 类名：formInfo；  API声明：interface OverflowInfo  差异内容：atomicservice | api/@ohos.app.form.formInfo.d.ts |
| API从不支持元服务到支持元服务 | 类名：OverflowInfo；  API声明：area: Rect;  差异内容：NA | 类名：OverflowInfo；  API声明：area: Rect;  差异内容：atomicservice | api/@ohos.app.form.formInfo.d.ts |
| API从不支持元服务到支持元服务 | 类名：OverflowInfo；  API声明：duration: number;  差异内容：NA | 类名：OverflowInfo；  API声明：duration: number;  差异内容：atomicservice | api/@ohos.app.form.formInfo.d.ts |
| API从不支持元服务到支持元服务 | 类名：formInfo；  API声明：interface Rect  差异内容：NA | 类名：formInfo；  API声明：interface Rect  差异内容：atomicservice | api/@ohos.app.form.formInfo.d.ts |
| API从不支持元服务到支持元服务 | 类名：Rect；  API声明：left: number;  差异内容：NA | 类名：Rect；  API声明：left: number;  差异内容：atomicservice | api/@ohos.app.form.formInfo.d.ts |
| API从不支持元服务到支持元服务 | 类名：Rect；  API声明：top: number;  差异内容：NA | 类名：Rect；  API声明：top: number;  差异内容：atomicservice | api/@ohos.app.form.formInfo.d.ts |
| API从不支持元服务到支持元服务 | 类名：Rect；  API声明：width: number;  差异内容：NA | 类名：Rect；  API声明：width: number;  差异内容：atomicservice | api/@ohos.app.form.formInfo.d.ts |
| API从不支持元服务到支持元服务 | 类名：Rect；  API声明：height: number;  差异内容：NA | 类名：Rect；  API声明：height: number;  差异内容：atomicservice | api/@ohos.app.form.formInfo.d.ts |
| API从不支持元服务到支持元服务 | 类名：formProvider；  API声明：function requestOverflow(formId: string, overflowInfo: formInfo.OverflowInfo): Promise<void>;  差异内容：NA | 类名：formProvider；  API声明：function requestOverflow(formId: string, overflowInfo: formInfo.OverflowInfo): Promise<void>;  差异内容：atomicservice | api/@ohos.app.form.formProvider.d.ts |
| API从不支持元服务到支持元服务 | 类名：formProvider；  API声明：function cancelOverflow(formId: string): Promise<void>;  差异内容：NA | 类名：formProvider；  API声明：function cancelOverflow(formId: string): Promise<void>;  差异内容：atomicservice | api/@ohos.app.form.formProvider.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：OverflowInfo；  API声明：useDefaultAnimation?: boolean;  差异内容：useDefaultAnimation?: boolean; | api/@ohos.app.form.formInfo.d.ts |
