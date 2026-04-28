---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-medialibrarykit-5031
title: Media Library Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta1引入的API > Media Library Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:42+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:619db9186d0ed641b9e65852eafdba301803c783bfb0e62398e0b534913c78a2
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：MediaAssetManager；  API声明：static requestVideoFile(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, fileUri: string, dataHandler: MediaAssetDataHandler<boolean>): Promise<string>;  差异内容：14000011,201,401 | 类名：MediaAssetManager；  API声明：static requestVideoFile(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, fileUri: string, dataHandler: MediaAssetDataHandler<boolean>): Promise<string>;  差异内容：14000011,201,401,801 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： enum CompatibleMode  差异内容： enum CompatibleMode | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：CompatibleMode；  API声明：ORIGINAL\_FORMAT\_MODE = 0  差异内容：ORIGINAL\_FORMAT\_MODE = 0 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：CompatibleMode；  API声明：COMPATIBLE\_FORMAT\_MODE = 1  差异内容：COMPATIBLE\_FORMAT\_MODE = 1 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： interface MediaAssetProgressHandler  差异内容： interface MediaAssetProgressHandler | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetProgressHandler；  API声明：onProgress(progress: number): void;  差异内容：onProgress(progress: number): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：RequestOptions；  API声明：compatibleMode?: CompatibleMode;  差异内容：compatibleMode?: CompatibleMode; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：RequestOptions；  API声明：mediaAssetProgressHandler?: MediaAssetProgressHandler;  差异内容：mediaAssetProgressHandler?: MediaAssetProgressHandler; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetChangeRequest；  API声明：setOrientation(orientation: number): void;  差异内容：setOrientation(orientation: number): void; | api/@ohos.file.photoAccessHelper.d.ts |
