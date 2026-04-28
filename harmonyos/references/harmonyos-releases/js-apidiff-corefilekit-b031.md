---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corefilekit-b031
title: Core File Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Core File Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:38+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:a01f35173da53a91a9ff990589cf098fe574f5d323918a72d0266a15d71d22e4
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：global；  API声明：declare function disconnectDfs(networkId: string): Promise<void>;  差异内容：201,401 | 类名：global；  API声明：declare function disconnectDfs(networkId: string): Promise<void>;  差异内容：13600004,201,401 | api/@ohos.file.fs.d.ts |
| 错误码变更 | 类名：Environment；  API声明：function getUserDownloadDir(): string;  差异内容：13900042,201,801 | 类名：Environment；  API声明：function getUserDownloadDir(): string;  差异内容：13900042,801 | api/@ohos.file.environment.d.ts |
| 错误码变更 | 类名：Environment；  API声明：function getUserDesktopDir(): string;  差异内容：13900042,201,801 | 类名：Environment；  API声明：function getUserDesktopDir(): string;  差异内容：13900042,801 | api/@ohos.file.environment.d.ts |
| 错误码变更 | 类名：Environment；  API声明：function getUserDocumentDir(): string;  差异内容：13900042,201,801 | 类名：Environment；  API声明：function getUserDocumentDir(): string;  差异内容：13900042,801 | api/@ohos.file.environment.d.ts |
| 权限变更 | 类名：global；  API声明：declare function connectDfs(networkId: string, listeners: DfsListeners): Promise<void>;  差异内容：NA | 类名：global；  API声明：declare function connectDfs(networkId: string, listeners: DfsListeners): Promise<void>;  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | api/@ohos.file.fs.d.ts |
| 权限变更 | 类名：global；  API声明：declare function disconnectDfs(networkId: string): Promise<void>;  差异内容：NA | 类名：global；  API声明：declare function disconnectDfs(networkId: string): Promise<void>;  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | api/@ohos.file.fs.d.ts |
| 权限变更 | 类名：Environment；  API声明：function getUserDownloadDir(): string;  差异内容：ohos.permission.READ\_WRITE\_DOWNLOAD\_DIRECTORY | 类名：Environment；  API声明：function getUserDownloadDir(): string;  差异内容：NA | api/@ohos.file.environment.d.ts |
| 权限变更 | 类名：Environment；  API声明：function getUserDesktopDir(): string;  差异内容：ohos.permission.READ\_WRITE\_DESKTOP\_DIRECTORY | 类名：Environment；  API声明：function getUserDesktopDir(): string;  差异内容：NA | api/@ohos.file.environment.d.ts |
| 权限变更 | 类名：Environment；  API声明：function getUserDocumentDir(): string;  差异内容：ohos.permission.READ\_WRITE\_DOCUMENTS\_DIRECTORY | 类名：Environment；  API声明：function getUserDocumentDir(): string;  差异内容：NA | api/@ohos.file.environment.d.ts |
| 函数变更 | 类名：global；  API声明：declare function createRandomAccessFile(file: string | File, mode?: number): Promise<RandomAccessFile>;  差异内容：NA | 类名：global；  API声明：declare function createRandomAccessFile(file: string | File, mode?: number, options?: RandomAccessFileOptions): Promise<RandomAccessFile>;  差异内容：options?: RandomAccessFileOptions | api/@ohos.file.fs.d.ts |
| 函数变更 | 类名：global；  API声明：declare function createRandomAccessFileSync(file: string | File, mode?: number): RandomAccessFile;  差异内容：NA | 类名：global；  API声明：declare function createRandomAccessFileSync(file: string | File, mode?: number, options?: RandomAccessFileOptions): RandomAccessFile;  差异内容：options?: RandomAccessFileOptions | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：global；  API声明：declare function createReadStream(path: string, options?: ReadStreamOptions): ReadStream;  差异内容：declare function createReadStream(path: string, options?: ReadStreamOptions): ReadStream; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：global；  API声明：declare function createWriteStream(path: string, options?: WriteStreamOptions): WriteStream;  差异内容：declare function createWriteStream(path: string, options?: WriteStreamOptions): WriteStream; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：global；  API声明： export class TaskSignal  差异内容： export class TaskSignal | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：TaskSignal；  API声明：cancel(): void;  差异内容：cancel(): void; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：TaskSignal；  API声明：onCancel(): Promise<string>;  差异内容：onCancel(): Promise<string>; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：CopyOptions；  API声明：copySignal?: TaskSignal;  差异内容：copySignal?: TaskSignal; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：RandomAccessFile；  API声明：getReadStream(): ReadStream;  差异内容：getReadStream(): ReadStream; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：RandomAccessFile；  API声明：getWriteStream(): WriteStream;  差异内容：getWriteStream(): WriteStream; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class ReadStream  差异内容： declare class ReadStream | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：ReadStream；  API声明：readonly bytesRead: number;  差异内容：readonly bytesRead: number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：ReadStream；  API声明：readonly path: string;  差异内容：readonly path: string; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：ReadStream；  API声明：seek(offset: number, whence?: WhenceType): number;  差异内容：seek(offset: number, whence?: WhenceType): number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：ReadStream；  API声明：close(): void;  差异内容：close(): void; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class WriteStream  差异内容： declare class WriteStream | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：WriteStream；  API声明：readonly bytesWritten: number;  差异内容：readonly bytesWritten: number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：WriteStream；  API声明：readonly path: string;  差异内容：readonly path: string; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：WriteStream；  API声明：seek(offset: number, whence?: WhenceType): number;  差异内容：seek(offset: number, whence?: WhenceType): number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：WriteStream；  API声明：close(): void;  差异内容：close(): void; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface RandomAccessFileOptions  差异内容： export interface RandomAccessFileOptions | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：RandomAccessFileOptions；  API声明：start?: number;  差异内容：start?: number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：RandomAccessFileOptions；  API声明：end?: number;  差异内容：end?: number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface ReadStreamOptions  差异内容： export interface ReadStreamOptions | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：ReadStreamOptions；  API声明：start?: number;  差异内容：start?: number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：ReadStreamOptions；  API声明：end?: number;  差异内容：end?: number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface WriteStreamOptions  差异内容： export interface WriteStreamOptions | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：WriteStreamOptions；  API声明：mode?: number;  差异内容：mode?: number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：WriteStreamOptions；  API声明：start?: number;  差异内容：start?: number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：BackupExtensionAbility；  API声明：onBackupEx(backupInfo: string): string | Promise<string>;  差异内容：onBackupEx(backupInfo: string): string | Promise<string>; | api/@ohos.application.BackupExtensionAbility.d.ts |
| 新增API | NA | 类名：hash；  API声明： class HashStream  差异内容： class HashStream | api/@ohos.file.hash.d.ts |
| 新增API | NA | 类名：HashStream；  API声明：digest(): string;  差异内容：digest(): string; | api/@ohos.file.hash.d.ts |
| 新增API | NA | 类名：HashStream；  API声明：update(data: ArrayBuffer): void;  差异内容：update(data: ArrayBuffer): void; | api/@ohos.file.hash.d.ts |
| 新增API | NA | 类名：hash；  API声明：function createHash(algorithm: string): HashStream;  差异内容：function createHash(algorithm: string): HashStream; | api/@ohos.file.hash.d.ts |
