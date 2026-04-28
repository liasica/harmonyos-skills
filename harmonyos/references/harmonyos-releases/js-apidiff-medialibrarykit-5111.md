---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-medialibrarykit-5111
title: Media Library Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Beta1引入的API > Media Library Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:55+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:6d79e3f5b722591e866a7828748289406f5cfeeefc4040dd2c24becf9195d1a0
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：photoAccessHelper；  API声明：export enum FilterOperator  差异内容：export enum FilterOperator | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FilterOperator；  API声明：EQUAL\_TO = 0  差异内容：EQUAL\_TO = 0 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FilterOperator；  API声明：NOT\_EQUAL\_TO = 1  差异内容：NOT\_EQUAL\_TO = 1 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FilterOperator；  API声明：MORE\_THAN = 2  差异内容：MORE\_THAN = 2 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FilterOperator；  API声明：LESS\_THAN = 3  差异内容：LESS\_THAN = 3 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FilterOperator；  API声明：MORE\_THAN\_OR\_EQUAL\_TO = 4  差异内容：MORE\_THAN\_OR\_EQUAL\_TO = 4 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FilterOperator；  API声明：LESS\_THAN\_OR\_EQUAL\_TO = 5  差异内容：LESS\_THAN\_OR\_EQUAL\_TO = 5 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FilterOperator；  API声明：BETWEEN = 6  差异内容：BETWEEN = 6 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：class MimeTypeFilter  差异内容：class MimeTypeFilter | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MimeTypeFilter；  API声明：mimeTypeArray: Array<string>;  差异内容：mimeTypeArray: Array<string>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：class FileSizeFilter  差异内容：class FileSizeFilter | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FileSizeFilter；  API声明：filterOperator: FilterOperator;  差异内容：filterOperator: FilterOperator; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FileSizeFilter；  API声明：fileSize: number;  差异内容：fileSize: number; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FileSizeFilter；  API声明：extraFileSize?: number;  差异内容：extraFileSize?: number; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：class VideoDurationFilter  差异内容：class VideoDurationFilter | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：VideoDurationFilter；  API声明：filterOperator: FilterOperator;  差异内容：filterOperator: FilterOperator; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：VideoDurationFilter；  API声明：videoDuration: number;  差异内容：videoDuration: number; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：VideoDurationFilter；  API声明：extraVideoDuration?: number;  差异内容：extraVideoDuration?: number; | api/@ohos.file.photoAccessHelper.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：BaseSelectOptions；  API声明：mimeTypeFilter?: MimeTypeFilter;  差异内容：mimeTypeFilter?: MimeTypeFilter; | api/@ohos.file.photoAccessHelper.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：BaseSelectOptions；  API声明：fileSizeFilter?: FileSizeFilter;  差异内容：fileSizeFilter?: FileSizeFilter; | api/@ohos.file.photoAccessHelper.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：BaseSelectOptions；  API声明：videoDurationFilter?: VideoDurationFilter;  差异内容：videoDurationFilter?: VideoDurationFilter; | api/@ohos.file.photoAccessHelper.d.ts |
