---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-5112
title: ArkUI
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Release引入的API > ArkUI
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:48+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:48d92c247fc8eafcbedd064a03b4e9d32c6afbc7bc25a05d0a623f04343461f3
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：Window；  API声明：destroyWindow(callback: AsyncCallback<void>): void;  差异内容：1300003 | 类名：Window；  API声明：destroyWindow(callback: AsyncCallback<void>): void;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：Window；  API声明：destroyWindow(): Promise<void>;  差异内容：1300003 | 类名：Window；  API声明：destroyWindow(): Promise<void>;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：Window；  API声明：loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void;  差异内容：1300003 | 类名：Window；  API声明：loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：Window；  API声明：loadContent(path: string, storage: LocalStorage): Promise<void>;  差异内容：1300003 | 类名：Window；  API声明：loadContent(path: string, storage: LocalStorage): Promise<void>;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：Window；  API声明：setUIContent(path: string, callback: AsyncCallback<void>): void;  差异内容：1300003 | 类名：Window；  API声明：setUIContent(path: string, callback: AsyncCallback<void>): void;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：Window；  API声明：setUIContent(path: string): Promise<void>;  差异内容：1300003 | 类名：Window；  API声明：setUIContent(path: string): Promise<void>;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：WindowStage；  API声明：createSubWindow(name: string): Promise<Window>;  差异内容：1300005 | 类名：WindowStage；  API声明：createSubWindow(name: string): Promise<Window>;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：WindowStage；  API声明：createSubWindow(name: string, callback: AsyncCallback<Window>): void;  差异内容：1300005 | 类名：WindowStage；  API声明：createSubWindow(name: string, callback: AsyncCallback<Window>): void;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：WindowStage；  API声明：loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void;  差异内容：1300005 | 类名：WindowStage；  API声明：loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：WindowStage；  API声明：loadContent(path: string, storage?: LocalStorage): Promise<void>;  差异内容：1300005 | 类名：WindowStage；  API声明：loadContent(path: string, storage?: LocalStorage): Promise<void>;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：WindowStage；  API声明：loadContent(path: string, callback: AsyncCallback<void>): void;  差异内容：1300005 | 类名：WindowStage；  API声明：loadContent(path: string, callback: AsyncCallback<void>): void;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：WindowStage；  API声明：loadContentByName(name: string, storage: LocalStorage, callback: AsyncCallback<void>): void;  差异内容：1300003 | 类名：WindowStage；  API声明：loadContentByName(name: string, storage: LocalStorage, callback: AsyncCallback<void>): void;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：WindowStage；  API声明：loadContentByName(name: string, callback: AsyncCallback<void>): void;  差异内容：1300003 | 类名：WindowStage；  API声明：loadContentByName(name: string, callback: AsyncCallback<void>): void;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：WindowStage；  API声明：loadContentByName(name: string, storage?: LocalStorage): Promise<void>;  差异内容：1300003 | 类名：WindowStage；  API声明：loadContentByName(name: string, storage?: LocalStorage): Promise<void>;  差异内容：NA | api/@ohos.window.d.ts |
| 错误码变更 | 类名：WindowStage；  API声明：getSubWindow(): Promise<Array<Window>>;  差异内容：1300005 | 类名：WindowStage；  API声明：getSubWindow(): Promise<Array<Window>>;  差异内容：1300002 | api/@ohos.window.d.ts |
| 错误码变更 | 类名：WindowStage；  API声明：getSubWindow(callback: AsyncCallback<Array<Window>>): void;  差异内容：1300005 | 类名：WindowStage；  API声明：getSubWindow(callback: AsyncCallback<Array<Window>>): void;  差异内容：1300002 | api/@ohos.window.d.ts |
