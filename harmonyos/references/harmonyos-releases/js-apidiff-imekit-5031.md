---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imekit-5031
title: IME Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta1引入的API > IME Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:41+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:a9b2e398287aeab78350e2f0d5c638bb9dabedd71af163f5f437585139552a1a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：InputMethodSetting；  API声明：getInputMethodState(): Promise<EnabledState>;  差异内容：getInputMethodState(): Promise<EnabledState>; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>;  差异内容：sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：recvMessage(msgHandler?: MessageHandler): void;  差异内容：recvMessage(msgHandler?: MessageHandler): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod；  API声明： export enum EnabledState  差异内容： export enum EnabledState | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：EnabledState；  API声明：DISABLED = 0  差异内容：DISABLED = 0 | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：EnabledState；  API声明：BASIC\_MODE  差异内容：BASIC\_MODE | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：EnabledState；  API声明：FULL\_EXPERIENCE\_MODE  差异内容：FULL\_EXPERIENCE\_MODE | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod；  API声明： interface MessageHandler  差异内容： interface MessageHandler | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：MessageHandler；  API声明：onMessage(msgId: string, msgParam?: ArrayBuffer): void;  差异内容：onMessage(msgId: string, msgParam?: ArrayBuffer): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：MessageHandler；  API声明：onTerminated(): void;  差异内容：onTerminated(): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>;  差异内容：sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：recvMessage(msgHandler?: MessageHandler): void;  差异内容：recvMessage(msgHandler?: MessageHandler): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：startMoving(): void;  差异内容：startMoving(): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：getDisplayId(): Promise<number>;  差异内容：getDisplayId(): Promise<number>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：getImmersiveMode(): ImmersiveMode;  差异内容：getImmersiveMode(): ImmersiveMode; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：PanelFlag；  API声明：FLAG\_CANDIDATE  差异内容：FLAG\_CANDIDATE | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine；  API声明： interface MessageHandler  差异内容： interface MessageHandler | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：MessageHandler；  API声明：onMessage(msgId: string, msgParam?: ArrayBuffer): void;  差异内容：onMessage(msgId: string, msgParam?: ArrayBuffer): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：MessageHandler；  API声明：onTerminated(): void;  差异内容：onTerminated(): void; | api/@ohos.inputMethodEngine.d.ts |
