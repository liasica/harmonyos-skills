---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corefilekit-7002
title: Core File Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Core File Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:902f6fc50fb89ec1ba4f35250743156ec7c20726680864bee627949015d36311
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：Environment；  API声明：function getUserDownloadDir(): string;  差异内容：NA | 类名：Environment；  API声明：function getUserDownloadDir(): string;  差异内容：201 | api/@ohos.file.environment.d.ts |
| 新增错误码 | 类名：Environment；  API声明：function getUserDesktopDir(): string;  差异内容：NA | 类名：Environment；  API声明：function getUserDesktopDir(): string;  差异内容：201 | api/@ohos.file.environment.d.ts |
| 新增错误码 | 类名：Environment；  API声明：function getUserDocumentDir(): string;  差异内容：NA | 类名：Environment；  API声明：function getUserDocumentDir(): string;  差异内容：201 | api/@ohos.file.environment.d.ts |
| 权限变更 | 类名：Environment；  API声明：function getUserDownloadDir(): string;  差异内容：NA | 类名：Environment；  API声明：function getUserDownloadDir(): string;  差异内容：ohos.permission.READ\_WRITE\_DOWNLOAD\_DIRECTORY [since 11 - 11] | api/@ohos.file.environment.d.ts |
| 权限变更 | 类名：Environment；  API声明：function getUserDesktopDir(): string;  差异内容：NA | 类名：Environment；  API声明：function getUserDesktopDir(): string;  差异内容：ohos.permission.READ\_WRITE\_DESKTOP\_DIRECTORY [since 11 - 11] | api/@ohos.file.environment.d.ts |
| 权限变更 | 类名：Environment；  API声明：function getUserDocumentDir(): string;  差异内容：NA | 类名：Environment；  API声明：function getUserDocumentDir(): string;  差异内容：ohos.permission.READ\_WRITE\_DOCUMENTS\_DIRECTORY [since 11 - 11] | api/@ohos.file.environment.d.ts |
| 新增API | NA | 类名：CloudFileCache；  API声明：getCachedTotalSize(): Promise<number>;  差异内容：getCachedTotalSize(): Promise<number>; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：CloudFileCache；  API声明：cleanAllFileCache(): Promise<void>;  差异内容：cleanAllFileCache(): Promise<void>; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：global；  API声明：declare function mmap(file: number | File, mode: MappingMode, offset: number, size: number): Promise<FileMapping>;  差异内容：declare function mmap(file: number | File, mode: MappingMode, offset: number, size: number): Promise<FileMapping>; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：global；  API声明：declare function mmapSync(file: number | File, mode: MappingMode, offset: number, size: number): FileMapping;  差异内容：declare function mmapSync(file: number | File, mode: MappingMode, offset: number, size: number): FileMapping; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface FileMapping  差异内容：declare interface FileMapping | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping；  API声明：setPosition(position: number): void;  差异内容：setPosition(position: number): void; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping；  API声明：getPosition(): number;  差异内容：getPosition(): number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping；  API声明：capacity(): number;  差异内容：capacity(): number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping；  API声明：setLimit(limit: number): void;  差异内容：setLimit(limit: number): void; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping；  API声明：getLimit(): number;  差异内容：getLimit(): number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping；  API声明：flip(): void;  差异内容：flip(): void; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping；  API声明：remaining(): number;  差异内容：remaining(): number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping；  API声明：read(buffer: ArrayBuffer, length?: number): number;  差异内容：read(buffer: ArrayBuffer, length?: number): number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping；  API声明：read(position: number, buffer: ArrayBuffer, length?: number): number;  差异内容：read(position: number, buffer: ArrayBuffer, length?: number): number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping；  API声明：write(data: ArrayBuffer, length?: number): number;  差异内容：write(data: ArrayBuffer, length?: number): number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping；  API声明：write(position: number, data: ArrayBuffer, length?: number): number;  差异内容：write(position: number, data: ArrayBuffer, length?: number): number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping；  API声明：msync(): Promise<void>;  差异内容：msync(): Promise<void>; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping；  API声明：msync(position: number, length: number): Promise<void>;  差异内容：msync(position: number, length: number): Promise<void>; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping；  API声明：msyncSync(): void;  差异内容：msyncSync(): void; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping；  API声明：msyncSync(position: number, length: number): void;  差异内容：msyncSync(position: number, length: number): void; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping；  API声明：unmap(): Promise<void>;  差异内容：unmap(): Promise<void>; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping；  API声明：unmapSync(): void;  差异内容：unmapSync(): void; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum MappingMode  差异内容：declare enum MappingMode | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：MappingMode；  API声明：READ\_ONLY = 0  差异内容：READ\_ONLY = 0 | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：MappingMode；  API声明：READ\_WRITE = 1  差异内容：READ\_WRITE = 1 | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：MappingMode；  API声明：PRIVATE = 2  差异内容：PRIVATE = 2 | api/@ohos.file.fs.d.ts |
