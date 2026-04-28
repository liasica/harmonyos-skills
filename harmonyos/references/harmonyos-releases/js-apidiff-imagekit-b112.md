---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imagekit-b112
title: Image Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.1(13) > OS平台能力 > API变更清单 > HarmonyOS 5.0.1(13) Release引入的API > Image Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:00+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:599b08a703765f542e38540b12af5c9c02f013bc819ac40e4b376c3434bddf51
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：ImagePacker；  API声明：packing(source: ImageSource, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void;  差异内容：NA | 类名：ImagePacker；  API声明：packing(source: ImageSource, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void;  差异内容：13 | api/@ohos.multimedia.image.d.ts |
| API废弃版本变更 | 类名：ImagePacker；  API声明：packing(source: ImageSource, option: PackingOption): Promise<ArrayBuffer>;  差异内容：NA | 类名：ImagePacker；  API声明：packing(source: ImageSource, option: PackingOption): Promise<ArrayBuffer>;  差异内容：13 | api/@ohos.multimedia.image.d.ts |
| API废弃版本变更 | 类名：ImagePacker；  API声明：packing(source: PixelMap, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void;  差异内容：NA | 类名：ImagePacker；  API声明：packing(source: PixelMap, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void;  差异内容：13 | api/@ohos.multimedia.image.d.ts |
| API废弃版本变更 | 类名：ImagePacker；  API声明：packing(source: PixelMap, option: PackingOption): Promise<ArrayBuffer>;  差异内容：NA | 类名：ImagePacker；  API声明：packing(source: PixelMap, option: PackingOption): Promise<ArrayBuffer>;  差异内容：13 | api/@ohos.multimedia.image.d.ts |
| 错误码变更 | 类名：ImagePacker；  API声明：packToFile(source: ImageSource, fd: number, options: PackingOption, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：ImagePacker；  API声明：packToFile(source: ImageSource, fd: number, options: PackingOption, callback: AsyncCallback<void>): void;  差异内容：62980096,62980101,62980106,62980113,62980115,62980119,62980120,62980172,62980252 | api/@ohos.multimedia.image.d.ts |
| 错误码变更 | 类名：ImagePacker；  API声明：packToFile(source: ImageSource, fd: number, options: PackingOption): Promise<void>;  差异内容：NA | 类名：ImagePacker；  API声明：packToFile(source: ImageSource, fd: number, options: PackingOption): Promise<void>;  差异内容：62980096,62980101,62980106,62980113,62980115,62980119,62980120,62980172,62980252 | api/@ohos.multimedia.image.d.ts |
| 错误码变更 | 类名：ImagePacker；  API声明：packToFile(source: PixelMap, fd: number, options: PackingOption, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：ImagePacker；  API声明：packToFile(source: PixelMap, fd: number, options: PackingOption, callback: AsyncCallback<void>): void;  差异内容：62980096,62980101,62980106,62980113,62980115,62980119,62980120,62980172,62980252 | api/@ohos.multimedia.image.d.ts |
| 错误码变更 | 类名：ImagePacker；  API声明：packToFile(source: PixelMap, fd: number, options: PackingOption): Promise<void>;  差异内容：NA | 类名：ImagePacker；  API声明：packToFile(source: PixelMap, fd: number, options: PackingOption): Promise<void>;  差异内容：62980096,62980101,62980106,62980113,62980115,62980119,62980120,62980172,62980252 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImagePacker；  API声明：packToData(source: ImageSource, options: PackingOption): Promise<ArrayBuffer>;  差异内容：packToData(source: ImageSource, options: PackingOption): Promise<ArrayBuffer>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImagePacker；  API声明：packToData(source: PixelMap, options: PackingOption): Promise<ArrayBuffer>;  差异内容：packToData(source: PixelMap, options: PackingOption): Promise<ArrayBuffer>; | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：image；  API声明： interface PackingOptionsForSequence  差异内容： interface PackingOptionsForSequence | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：PackingOptionsForSequence；  API声明：frameCount: number;  差异内容：frameCount: number; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：PackingOptionsForSequence；  API声明：delayTimeList: Array<number>;  差异内容：delayTimeList: Array<number>; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：PackingOptionsForSequence；  API声明：disposalTypes?: Array<number>;  差异内容：disposalTypes?: Array<number>; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：PackingOptionsForSequence；  API声明：loopCount?: number;  差异内容：loopCount?: number; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：ImagePacker；  API声明：packing(pixelmapSequence: Array<PixelMap>, options: PackingOptionsForSequence): Promise<ArrayBuffer>;  差异内容：packing(pixelmapSequence: Array<PixelMap>, options: PackingOptionsForSequence): Promise<ArrayBuffer>; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：ImagePacker；  API声明：packToFile(pixelmapSequence: Array<PixelMap>, fd: number, options: PackingOptionsForSequence): Promise<void>;  差异内容：packToFile(pixelmapSequence: Array<PixelMap>, fd: number, options: PackingOptionsForSequence): Promise<void>; | NA | api/@ohos.multimedia.image.d.ts |
