---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkdata-5031
title: ArkData
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta1引入的API > ArkData
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:39+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:603ddf13b77bea785f4192f4346907bcbc527f5f5b2cd9dcf9fc3f8d7705839e
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：UnifiedRecord；  API声明：getTypes(): Array<string>;  差异内容：getTypes(): Array<string>; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UnifiedRecord；  API声明：addEntry(type: string, value: ValueType): void;  差异内容：addEntry(type: string, value: ValueType): void; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UnifiedRecord；  API声明：getEntry(type: string): ValueType;  差异内容：getEntry(type: string): ValueType; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UnifiedRecord；  API声明：getEntries(): Record<string, ValueType>;  差异内容：getEntries(): Record<string, ValueType>; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：uniformDataStruct；  API声明： interface Form  差异内容： interface Form | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：Form；  API声明：readonly uniformDataType: 'openharmony.form';  差异内容：readonly uniformDataType: 'openharmony.form'; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：Form；  API声明：formId: number;  差异内容：formId: number; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：Form；  API声明：formName: string;  差异内容：formName: string; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：Form；  API声明：bundleName: string;  差异内容：bundleName: string; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：Form；  API声明：abilityName: string;  差异内容：abilityName: string; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：Form；  API声明：module: string;  差异内容：module: string; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：Form；  API声明：details?: Record<string, number | string | Uint8Array>;  差异内容：details?: Record<string, number | string | Uint8Array>; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：uniformDataStruct；  API声明： interface FileUri  差异内容： interface FileUri | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：FileUri；  API声明：readonly uniformDataType: 'general.file-uri';  差异内容：readonly uniformDataType: 'general.file-uri'; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：FileUri；  API声明：oriUri: string;  差异内容：oriUri: string; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：FileUri；  API声明：fileType: string;  差异内容：fileType: string; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：FileUri；  API声明：details?: Record<string, number | string | Uint8Array>;  差异内容：details?: Record<string, number | string | Uint8Array>; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：uniformDataStruct；  API声明： interface PixelMap  差异内容： interface PixelMap | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：readonly uniformDataType: 'openharmony.pixel-map';  差异内容：readonly uniformDataType: 'openharmony.pixel-map'; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：pixelMap: image.PixelMap;  差异内容：pixelMap: image.PixelMap; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：details?: Record<string, number | string | Uint8Array>;  差异内容：details?: Record<string, number | string | Uint8Array>; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：FILE\_URI = 'general.file-uri'  差异内容：FILE\_URI = 'general.file-uri' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：CONTENT\_FORM = 'general.content-form'  差异内容：CONTENT\_FORM = 'general.content-form' | api/@ohos.data.uniformTypeDescriptor.d.ts |
