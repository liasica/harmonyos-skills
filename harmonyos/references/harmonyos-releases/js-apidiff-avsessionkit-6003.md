---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-avsessionkit-6003
title: AVSession Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > AVSession Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:15+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:1ff5373abcae52db3554e215220a02e1da33bf6989da71a608e15d9a6ef0a1a8
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API从不支持元服务到支持元服务 | 类名：AVMediaDescription；  API声明：pcmSrc?: boolean;  差异内容：NA | 类名：AVMediaDescription；  API声明：pcmSrc?: boolean;  差异内容：atomicservice | api/@ohos.multimedia.avsession.d.ts |
| API从不支持元服务到支持元服务 | 类名：DeviceInfo；  API声明：audioCapabilities?: AudioCapabilities;  差异内容：NA | 类名：DeviceInfo；  API声明：audioCapabilities?: AudioCapabilities;  差异内容：atomicservice | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AVSession；  API声明：on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void;  差异内容：on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AVSession；  API声明：off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void;  差异内容：off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AVSession；  API声明：sendCustomData(data: Record<string, Object>): Promise<void>;  差异内容：sendCustomData(data: Record<string, Object>): Promise<void>; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AVCastController；  API声明：sendCustomData(data: Record<string, Object>): Promise<void>;  差异内容：sendCustomData(data: Record<string, Object>): Promise<void>; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AVCastController；  API声明：on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void;  差异内容：on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AVCastController；  API声明：off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void;  差异内容：off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AVSessionController；  API声明：sendCustomData(data: Record<string, Object>): Promise<void>;  差异内容：sendCustomData(data: Record<string, Object>): Promise<void>; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AVSessionController；  API声明：on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void;  差异内容：on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AVSessionController；  API声明：off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void;  差异内容：off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：AVMediaDescription；  API声明：launchClientData?: string;  差异内容：launchClientData?: string; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：DeviceInfo；  API声明：supportedPullClients?: Array<number>;  差异内容：supportedPullClients?: Array<number>; | api/@ohos.multimedia.avsession.d.ts |
