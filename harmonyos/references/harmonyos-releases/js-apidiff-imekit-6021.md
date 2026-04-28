---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imekit-6021
title: IME Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.2(22) > OS平台能力 > API变更清单 > IME Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:46+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:ed749d93551007964d9494b3e4f5e49a856c0523192bb6a566c94296f5e26112
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：export type CustomValueType = number | string | boolean;  差异内容：export type CustomValueType = number | string | boolean; | api/@ohos.inputMethod.ExtraConfig.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface InputMethodExtraConfig  差异内容：export interface InputMethodExtraConfig | api/@ohos.inputMethod.ExtraConfig.d.ts |
| 新增API | NA | 类名：InputMethodExtraConfig；  API声明：customSettings: Record<string, CustomValueType>;  差异内容：customSettings: Record<string, CustomValueType>; | api/@ohos.inputMethod.ExtraConfig.d.ts |
| 新增API | NA | 类名：inputMethod；  API声明：function onAttachmentDidFail(callback: Callback<AttachFailureReason>): void;  差异内容：function onAttachmentDidFail(callback: Callback<AttachFailureReason>): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod；  API声明：function offAttachmentDidFail(callback?: Callback<AttachFailureReason>): void;  差异内容：function offAttachmentDidFail(callback?: Callback<AttachFailureReason>): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod；  API声明：export enum AttachFailureReason  差异内容：export enum AttachFailureReason | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：AttachFailureReason；  API声明：CALLER\_NOT\_FOCUSED = 0  差异内容：CALLER\_NOT\_FOCUSED = 0 | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：AttachFailureReason；  API声明：IME\_ABNORMAL  差异内容：IME\_ABNORMAL | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：AttachFailureReason；  API声明：SERVICE\_ABNORMAL  差异内容：SERVICE\_ABNORMAL | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：Panel；  API声明：setSystemPanelButtonColor(fillColor: string | undefined, backgroundColor: string | undefined): Promise<void>;  差异内容：setSystemPanelButtonColor(fillColor: string | undefined, backgroundColor: string | undefined): Promise<void>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：EditorAttribute；  API声明：readonly extraConfig?: InputMethodExtraConfig;  差异内容：readonly extraConfig?: InputMethodExtraConfig; | api/@ohos.inputMethodEngine.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.inputMethod.ExtraConfig.d.ts  差异内容：IMEKit | api/@ohos.inputMethod.ExtraConfig.d.ts |
