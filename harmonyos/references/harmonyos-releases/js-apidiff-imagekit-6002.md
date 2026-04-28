---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imagekit-6002
title: Image Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > Image Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:29+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:987836524f555ccbdaaf717291f086cb1bec32cac169cc262b2e107987991d5a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：AuxiliaryPicture；  API声明：writePixelsFromBuffer(data: ArrayBuffer): Promise<void>;  差异内容：7600301,7600302 | 类名：AuxiliaryPicture；  API声明：writePixelsFromBuffer(data: ArrayBuffer): Promise<void>;  差异内容：NA | api/@ohos.multimedia.image.d.ts |
| 删除错误码 | 类名：AuxiliaryPicture；  API声明：readPixelsToBuffer(): Promise<ArrayBuffer>;  差异内容：7600301,7600302 | 类名：AuxiliaryPicture；  API声明：readPixelsToBuffer(): Promise<ArrayBuffer>;  差异内容：NA | api/@ohos.multimedia.image.d.ts |
| 删除错误码 | 类名：Metadata；  API声明：clone(): Promise<Metadata>;  差异内容：7600301,7600302 | 类名：Metadata；  API声明：clone(): Promise<Metadata>;  差异内容：NA | api/@ohos.multimedia.image.d.ts |
| 删除错误码 | 类名：ImageSource；  API声明：createPixelMapList(options?: DecodingOptions): Promise<Array<PixelMap>>;  差异内容：62980110,62980112,62980113,62980122 | 类名：ImageSource；  API声明：createPixelMapList(options?: DecodingOptions): Promise<Array<PixelMap>>;  差异内容：NA | api/@ohos.multimedia.image.d.ts |
| 删除错误码 | 类名：ImageSource；  API声明：createPixelMapList(callback: AsyncCallback<Array<PixelMap>>): void;  差异内容：62980110,62980112,62980113,62980122 | 类名：ImageSource；  API声明：createPixelMapList(callback: AsyncCallback<Array<PixelMap>>): void;  差异内容：NA | api/@ohos.multimedia.image.d.ts |
| 删除错误码 | 类名：ImageSource；  API声明：createPixelMapList(options: DecodingOptions, callback: AsyncCallback<Array<PixelMap>>): void;  差异内容：62980110,62980112,62980113,62980122 | 类名：ImageSource；  API声明：createPixelMapList(options: DecodingOptions, callback: AsyncCallback<Array<PixelMap>>): void;  差异内容：NA | api/@ohos.multimedia.image.d.ts |
| 删除错误码 | 类名：ImageSource；  API声明：getDelayTimeList(): Promise<Array<number>>;  差异内容：62980112,62980113,62980137 | 类名：ImageSource；  API声明：getDelayTimeList(): Promise<Array<number>>;  差异内容：NA | api/@ohos.multimedia.image.d.ts |
| 删除错误码 | 类名：ImageSource；  API声明：getDelayTimeList(callback: AsyncCallback<Array<number>>): void;  差异内容：62980111,62980112,62980137 | 类名：ImageSource；  API声明：getDelayTimeList(callback: AsyncCallback<Array<number>>): void;  差异内容：NA | api/@ohos.multimedia.image.d.ts |
| 删除错误码 | 类名：ImageSource；  API声明：getFrameCount(): Promise<number>;  差异内容：62980110 | 类名：ImageSource；  API声明：getFrameCount(): Promise<number>;  差异内容：NA | api/@ohos.multimedia.image.d.ts |
| 删除错误码 | 类名：ImageSource；  API声明：getFrameCount(callback: AsyncCallback<number>): void;  差异内容：62980110 | 类名：ImageSource；  API声明：getFrameCount(callback: AsyncCallback<number>): void;  差异内容：NA | api/@ohos.multimedia.image.d.ts |
| 删除错误码 | 类名：ImageSource；  API声明：getImageProperty(key: PropertyKey, options?: ImagePropertyOptions): Promise<string>;  差异内容：62980116 | 类名：ImageSource；  API声明：getImageProperty(key: PropertyKey, options?: ImagePropertyOptions): Promise<string>;  差异内容：NA | api/@ohos.multimedia.image.d.ts |
| 删除错误码 | 类名：ImageSource；  API声明：modifyImageProperties(records: Record<PropertyKey, string | null>): Promise<void>;  差异内容：62980133 | 类名：ImageSource；  API声明：modifyImageProperties(records: Record<PropertyKey, string | null>): Promise<void>;  差异内容：NA | api/@ohos.multimedia.image.d.ts |
| 删除错误码 | 类名：ImagePacker；  API声明：packToDataFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, options: PackingOptionsForSequence): Promise<ArrayBuffer>;  差异内容：7800201 | 类名：ImagePacker；  API声明：packToDataFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, options: PackingOptionsForSequence): Promise<ArrayBuffer>;  差异内容：NA | api/@ohos.multimedia.image.d.ts |
| 删除错误码 | 类名：ImagePacker；  API声明：packToFileFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, fd: number, options: PackingOptionsForSequence): Promise<void>;  差异内容：7800201 | 类名：ImagePacker；  API声明：packToFileFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, fd: number, options: PackingOptionsForSequence): Promise<void>;  差异内容：NA | api/@ohos.multimedia.image.d.ts |
| 函数变更 | 类名：image；  API声明：function createPixelMapUsingAllocator(colors: ArrayBuffer, options: InitializationOptions, allocatorType?: AllocatorType): Promise<PixelMap>;  差异内容：colors: ArrayBuffer, options: InitializationOptions, allocatorType?: AllocatorType | 类名：image；  API声明：function createPixelMapUsingAllocator(colors: ArrayBuffer, param: InitializationOptions, allocatorType?: AllocatorType): Promise<PixelMap>;  差异内容：colors: ArrayBuffer, param: InitializationOptions, allocatorType?: AllocatorType | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：function createPixelMapUsingAllocatorSync(colors: ArrayBuffer, param: InitializationOptions, allocatorType?: AllocatorType): PixelMap;  差异内容：function createPixelMapUsingAllocatorSync(colors: ArrayBuffer, param: InitializationOptions, allocatorType?: AllocatorType): PixelMap; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：function createPixelMapUsingAllocatorSync(param: InitializationOptions, allocatorType?: AllocatorType): PixelMap;  差异内容：function createPixelMapUsingAllocatorSync(param: InitializationOptions, allocatorType?: AllocatorType): PixelMap; | api/@ohos.multimedia.image.d.ts |
| 删除同名函数 | 类名：image；  API声明：function createPixelMapUsingAllocatorSync(colors: ArrayBuffer, options: InitializationOptions, allocatorType?: AllocatorType): PixelMap;  差异内容：function createPixelMapUsingAllocatorSync(colors: ArrayBuffer, options: InitializationOptions, allocatorType?: AllocatorType): PixelMap; | 类名：global；  API声明：  差异内容：NA | api/@ohos.multimedia.image.d.ts |
| 删除同名函数 | 类名：image；  API声明：function createPixelMapUsingAllocatorSync(options: InitializationOptions, allocatorType?: AllocatorType): PixelMap;  差异内容：function createPixelMapUsingAllocatorSync(options: InitializationOptions, allocatorType?: AllocatorType): PixelMap; | 类名：global；  API声明：  差异内容：NA | api/@ohos.multimedia.image.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：ImageSource；  API声明：getImagePropertySync(key: PropertyKey): string;  差异内容：getImagePropertySync(key: PropertyKey): string; | api/@ohos.multimedia.image.d.ts |
