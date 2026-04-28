---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corefilekit-6101
title: Core File Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7c1a04672d4c1607c59656710974e792f2ccfc9e795c4a107eb5b42943bc4298
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：global；  API声明：declare namespace fileAccess  差异内容：NA | 类名：global；  API声明：declare namespace fileAccess  差异内容：23 | api/@ohos.file.fileAccess.d.ts |
| 新增API | NA | 类名：FileUri；  API声明：get name(): string;  差异内容：get name(): string; | api/@ohos.file.fileuri.d.ts |
| 新增API | NA | 类名：TaskSignal；  API声明：onCancel(callback: Callback<string>): void;  差异内容：onCancel(callback: Callback<string>): void; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：DocumentSaveOptions；  API声明：autoCreateEmptyFile?: boolean;  差异内容：autoCreateEmptyFile?: boolean; | api/@ohos.file.picker.d.ts |
| 删除API | 类名：FileUri；  API声明：readonly name: string;  差异内容：readonly name: string; | NA | api/@ohos.file.fileuri.d.ts |
| 自定义类型变为接口兼容 | 类名：fileShare；  API声明：export type PolicyErrorResult = {  /\*\*  \* Indicates the failed uri of the policy information.  \*  \* @type { string }  \* @syscap SystemCapability.FileManagement.AppFileService.FolderAuthorization  \* @since 11  \*/  uri: string;  /\*\*  \* Indicates the error code of the failure in the policy information.  \*  \* @type { PolicyErrorCode }  \* @syscap SystemCapability.FileManagement.AppFileService.FolderAuthorization  \* @since 11  \*/  code: PolicyErrorCode;  /\*\*  \* Indicates the reason of the failure in the policy information.  \*  \* @type { string }  \* @syscap SystemCapability.FileManagement.AppFileService.FolderAuthorization  \* @since 11  \*/  message: string;  };  差异内容：export type PolicyErrorResult = {  /\*\*  \* Indicates the failed uri of the policy information.  \*  \* @type { string }  \* @syscap SystemCapability.FileManagement.AppFileService.FolderAuthorization  \* @since 11  \*/  uri: string;  /\*\*  \* Indicates the error code of the failure in the policy information.  \*  \* @type { PolicyErrorCode }  \* @syscap SystemCapability.FileManagement.AppFileService.FolderAuthorization  \* @since 11  \*/  code: PolicyErrorCode;  /\*\*  \* Indicates the reason of the failure in the policy information.  \*  \* @type { string }  \* @syscap SystemCapability.FileManagement.AppFileService.FolderAuthorization  \* @since 11  \*/  message: string;  }; | 类名：fileShare；  API声明：export interface PolicyErrorResult  差异内容：export interface PolicyErrorResult | api/@ohos.fileshare.d.ts |
