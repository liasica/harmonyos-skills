---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corefilekit-6003
title: Core File Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > Core File Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:16+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:ddb891cc105fd883cb4d655fd18bcf6047acf03fb56c915e17f83f8fef3b2808
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API跨平台权限变更 | 类名：global；  API声明：declare function createRandomAccessFile(file: string | File, mode?: number, options?: RandomAccessFileOptions): Promise<RandomAccessFile>;  差异内容：NA | 类名：global；  API声明：declare function createRandomAccessFile(file: string | File, mode?: number, options?: RandomAccessFileOptions): Promise<RandomAccessFile>;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：global；  API声明：declare function createRandomAccessFile(file: string | File, callback: AsyncCallback<RandomAccessFile>): void;  差异内容：NA | 类名：global；  API声明：declare function createRandomAccessFile(file: string | File, callback: AsyncCallback<RandomAccessFile>): void;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：global；  API声明：declare function createRandomAccessFile(file: string | File, mode: number, callback: AsyncCallback<RandomAccessFile>): void;  差异内容：NA | 类名：global；  API声明：declare function createRandomAccessFile(file: string | File, mode: number, callback: AsyncCallback<RandomAccessFile>): void;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：global；  API声明：declare function createRandomAccessFileSync(file: string | File, mode?: number, options?: RandomAccessFileOptions): RandomAccessFile;  差异内容：NA | 类名：global；  API声明：declare function createRandomAccessFileSync(file: string | File, mode?: number, options?: RandomAccessFileOptions): RandomAccessFile;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：global；  API声明：declare function createWatcher(path: string, events: number, listener: WatchEventListener): Watcher;  差异内容：NA | 类名：global；  API声明：declare function createWatcher(path: string, events: number, listener: WatchEventListener): Watcher;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：global；  API声明：declare function fdopenStream(fd: number, mode: string): Promise<Stream>;  差异内容：NA | 类名：global；  API声明：declare function fdopenStream(fd: number, mode: string): Promise<Stream>;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：global；  API声明：declare function fdopenStream(fd: number, mode: string, callback: AsyncCallback<Stream>): void;  差异内容：NA | 类名：global；  API声明：declare function fdopenStream(fd: number, mode: string, callback: AsyncCallback<Stream>): void;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：global；  API声明：declare function fdopenStreamSync(fd: number, mode: string): Stream;  差异内容：NA | 类名：global；  API声明：declare function fdopenStreamSync(fd: number, mode: string): Stream;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：global；  API声明：declare function readLines(filePath: string, options?: Options): Promise<ReaderIterator>;  差异内容：NA | 类名：global；  API声明：declare function readLines(filePath: string, options?: Options): Promise<ReaderIterator>;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：global；  API声明：declare function readLines(filePath: string, callback: AsyncCallback<ReaderIterator>): void;  差异内容：NA | 类名：global；  API声明：declare function readLines(filePath: string, callback: AsyncCallback<ReaderIterator>): void;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：global；  API声明：declare function readLines(filePath: string, options: Options, callback: AsyncCallback<ReaderIterator>): void;  差异内容：NA | 类名：global；  API声明：declare function readLines(filePath: string, options: Options, callback: AsyncCallback<ReaderIterator>): void;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：global；  API声明：declare function readLinesSync(filePath: string, options?: Options): ReaderIterator;  差异内容：NA | 类名：global；  API声明：declare function readLinesSync(filePath: string, options?: Options): ReaderIterator;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：File；  API声明：getParent(): string;  差异内容：NA | 类名：File；  API声明：getParent(): string;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：global；  API声明：declare interface RandomAccessFile  差异内容：NA | 类名：global；  API声明：declare interface RandomAccessFile  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：RandomAccessFile；  API声明：readonly fd: number;  差异内容：NA | 类名：RandomAccessFile；  API声明：readonly fd: number;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：RandomAccessFile；  API声明：readonly filePointer: number;  差异内容：NA | 类名：RandomAccessFile；  API声明：readonly filePointer: number;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：RandomAccessFile；  API声明：setFilePointer(filePointer: number): void;  差异内容：NA | 类名：RandomAccessFile；  API声明：setFilePointer(filePointer: number): void;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：RandomAccessFile；  API声明：close(): void;  差异内容：NA | 类名：RandomAccessFile；  API声明：close(): void;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：RandomAccessFile；  API声明：write(buffer: ArrayBuffer | string, options?: WriteOptions): Promise<number>;  差异内容：NA | 类名：RandomAccessFile；  API声明：write(buffer: ArrayBuffer | string, options?: WriteOptions): Promise<number>;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：RandomAccessFile；  API声明：write(buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：RandomAccessFile；  API声明：write(buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：RandomAccessFile；  API声明：write(buffer: ArrayBuffer | string, options: WriteOptions, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：RandomAccessFile；  API声明：write(buffer: ArrayBuffer | string, options: WriteOptions, callback: AsyncCallback<number>): void;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：RandomAccessFile；  API声明：writeSync(buffer: ArrayBuffer | string, options?: WriteOptions): number;  差异内容：NA | 类名：RandomAccessFile；  API声明：writeSync(buffer: ArrayBuffer | string, options?: WriteOptions): number;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：RandomAccessFile；  API声明：read(buffer: ArrayBuffer, options?: ReadOptions): Promise<number>;  差异内容：NA | 类名：RandomAccessFile；  API声明：read(buffer: ArrayBuffer, options?: ReadOptions): Promise<number>;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：RandomAccessFile；  API声明：read(buffer: ArrayBuffer, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：RandomAccessFile；  API声明：read(buffer: ArrayBuffer, callback: AsyncCallback<number>): void;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：RandomAccessFile；  API声明：read(buffer: ArrayBuffer, options: ReadOptions, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：RandomAccessFile；  API声明：read(buffer: ArrayBuffer, options: ReadOptions, callback: AsyncCallback<number>): void;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：RandomAccessFile；  API声明：readSync(buffer: ArrayBuffer, options?: ReadOptions): number;  差异内容：NA | 类名：RandomAccessFile；  API声明：readSync(buffer: ArrayBuffer, options?: ReadOptions): number;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：global；  API声明：export class AtomicFile  差异内容：NA | 类名：global；  API声明：export class AtomicFile  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：AtomicFile；  API声明：getBaseFile(): File;  差异内容：NA | 类名：AtomicFile；  API声明：getBaseFile(): File;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：AtomicFile；  API声明：openRead(): ReadStream;  差异内容：NA | 类名：AtomicFile；  API声明：openRead(): ReadStream;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：AtomicFile；  API声明：readFully(): ArrayBuffer;  差异内容：NA | 类名：AtomicFile；  API声明：readFully(): ArrayBuffer;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：AtomicFile；  API声明：startWrite(): WriteStream;  差异内容：NA | 类名：AtomicFile；  API声明：startWrite(): WriteStream;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：AtomicFile；  API声明：finishWrite(): void;  差异内容：NA | 类名：AtomicFile；  API声明：finishWrite(): void;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：AtomicFile；  API声明：failWrite(): void;  差异内容：NA | 类名：AtomicFile；  API声明：failWrite(): void;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：AtomicFile；  API声明：delete(): void;  差异内容：NA | 类名：AtomicFile；  API声明：delete(): void;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：global；  API声明：export interface WatchEventListener  差异内容：NA | 类名：global；  API声明：export interface WatchEventListener  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：global；  API声明：export interface WatchEvent  差异内容：NA | 类名：global；  API声明：export interface WatchEvent  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：WatchEvent；  API声明：readonly fileName: string;  差异内容：NA | 类名：WatchEvent；  API声明：readonly fileName: string;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：WatchEvent；  API声明：readonly event: number;  差异内容：NA | 类名：WatchEvent；  API声明：readonly event: number;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：WatchEvent；  API声明：readonly cookie: number;  差异内容：NA | 类名：WatchEvent；  API声明：readonly cookie: number;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：global；  API声明：export interface Watcher  差异内容：NA | 类名：global；  API声明：export interface Watcher  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：Watcher；  API声明：start(): void;  差异内容：NA | 类名：Watcher；  API声明：start(): void;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：Watcher；  API声明：stop(): void;  差异内容：NA | 类名：Watcher；  API声明：stop(): void;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：global；  API声明：export interface ReaderIteratorResult  差异内容：NA | 类名：global；  API声明：export interface ReaderIteratorResult  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：ReaderIteratorResult；  API声明：done: boolean;  差异内容：NA | 类名：ReaderIteratorResult；  API声明：done: boolean;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：ReaderIteratorResult；  API声明：value: string;  差异内容：NA | 类名：ReaderIteratorResult；  API声明：value: string;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：global；  API声明：declare interface ReaderIterator  差异内容：NA | 类名：global；  API声明：declare interface ReaderIterator  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：ReaderIterator；  API声明：next(): ReaderIteratorResult;  差异内容：NA | 类名：ReaderIterator；  API声明：next(): ReaderIteratorResult;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：global；  API声明：export interface Options  差异内容：NA | 类名：global；  API声明：export interface Options  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：Options；  API声明：encoding?: string;  差异内容：NA | 类名：Options；  API声明：encoding?: string;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：global；  API声明：export interface RandomAccessFileOptions  差异内容：NA | 类名：global；  API声明：export interface RandomAccessFileOptions  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：RandomAccessFileOptions；  API声明：start?: number;  差异内容：NA | 类名：RandomAccessFileOptions；  API声明：start?: number;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：RandomAccessFileOptions；  API声明：end?: number;  差异内容：NA | 类名：RandomAccessFileOptions；  API声明：end?: number;  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：global；  API声明：declare enum WhenceType  差异内容：NA | 类名：global；  API声明：declare enum WhenceType  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：WhenceType；  API声明：SEEK\_SET = 0  差异内容：NA | 类名：WhenceType；  API声明：SEEK\_SET = 0  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：WhenceType；  API声明：SEEK\_CUR = 1  差异内容：NA | 类名：WhenceType；  API声明：SEEK\_CUR = 1  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| API跨平台权限变更 | 类名：WhenceType；  API声明：SEEK\_END = 2  差异内容：NA | 类名：WhenceType；  API声明：SEEK\_END = 2  差异内容：crossplatform | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：cloudSync；  API声明：enum DownloadFileType  差异内容：enum DownloadFileType | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：DownloadFileType；  API声明：CONTENT = 0  差异内容：CONTENT = 0 | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：DownloadFileType；  API声明：THUMBNAIL = 1  差异内容：THUMBNAIL = 1 | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：DownloadFileType；  API声明：LCD = 2  差异内容：LCD = 2 | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：cloudSync；  API声明：interface FailedFileInfo  差异内容：interface FailedFileInfo | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：FailedFileInfo；  API声明：uri: string;  差异内容：uri: string; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：FailedFileInfo；  API声明：error: DownloadErrorType;  差异内容：error: DownloadErrorType; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：cloudSync；  API声明：class MultiDownloadProgress  差异内容：class MultiDownloadProgress | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：MultiDownloadProgress；  API声明：state: State;  差异内容：state: State; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：MultiDownloadProgress；  API声明：taskId: number;  差异内容：taskId: number; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：MultiDownloadProgress；  API声明：successfulCount: number;  差异内容：successfulCount: number; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：MultiDownloadProgress；  API声明：failedCount: number;  差异内容：failedCount: number; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：MultiDownloadProgress；  API声明：totalCount: number;  差异内容：totalCount: number; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：MultiDownloadProgress；  API声明：downloadedSize: number;  差异内容：downloadedSize: number; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：MultiDownloadProgress；  API声明：totalSize: number;  差异内容：totalSize: number; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：MultiDownloadProgress；  API声明：errType: DownloadErrorType;  差异内容：errType: DownloadErrorType; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：MultiDownloadProgress；  API声明：getFailedFiles(): Array<FailedFileInfo>;  差异内容：getFailedFiles(): Array<FailedFileInfo>; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：MultiDownloadProgress；  API声明：getSuccessfulFiles(): Array<string>;  差异内容：getSuccessfulFiles(): Array<string>; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：cloudSync；  API声明：enum FileState  差异内容：enum FileState | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：FileState；  API声明：INITIAL\_AFTER\_DOWNLOAD = 0  差异内容：INITIAL\_AFTER\_DOWNLOAD = 0 | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：FileState；  API声明：UPLOADING = 1  差异内容：UPLOADING = 1 | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：FileState；  API声明：STOPPED = 2  差异内容：STOPPED = 2 | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：FileState；  API声明：TO\_BE\_UPLOADED = 3  差异内容：TO\_BE\_UPLOADED = 3 | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：FileState；  API声明：UPLOAD\_SUCCESS = 4  差异内容：UPLOAD\_SUCCESS = 4 | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：FileState；  API声明：UPLOAD\_FAILURE = 5  差异内容：UPLOAD\_FAILURE = 5 | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：cloudSync；  API声明：function getCoreFileSyncState(uri: string): FileState;  差异内容：function getCoreFileSyncState(uri: string): FileState; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：cloudSync；  API声明：interface HistoryVersion  差异内容：interface HistoryVersion | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：HistoryVersion；  API声明：editedTime: number;  差异内容：editedTime: number; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：HistoryVersion；  API声明：fileSize: number;  差异内容：fileSize: number; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：HistoryVersion；  API声明：versionId: string;  差异内容：versionId: string; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：HistoryVersion；  API声明：originalFileName: string;  差异内容：originalFileName: string; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：HistoryVersion；  API声明：sha256: string;  差异内容：sha256: string; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：HistoryVersion；  API声明：autoResolved: boolean;  差异内容：autoResolved: boolean; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：cloudSync；  API声明：interface VersionDownloadProgress  差异内容：interface VersionDownloadProgress | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：VersionDownloadProgress；  API声明：state: State;  差异内容：state: State; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：VersionDownloadProgress；  API声明：progress: number;  差异内容：progress: number; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：VersionDownloadProgress；  API声明：errType: DownloadErrorType;  差异内容：errType: DownloadErrorType; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：cloudSync；  API声明：class FileVersion  差异内容：class FileVersion | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：FileVersion；  API声明：getHistoryVersionList(uri: string, versionNumLimit: number): Promise<Array<HistoryVersion>>;  差异内容：getHistoryVersionList(uri: string, versionNumLimit: number): Promise<Array<HistoryVersion>>; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：FileVersion；  API声明：downloadHistoryVersion(uri: string, versionId: string, callback: Callback<VersionDownloadProgress>): Promise<string>;  差异内容：downloadHistoryVersion(uri: string, versionId: string, callback: Callback<VersionDownloadProgress>): Promise<string>; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：FileVersion；  API声明：replaceFileWithHistoryVersion(originalUri: string, versionUri: string): Promise<void>;  差异内容：replaceFileWithHistoryVersion(originalUri: string, versionUri: string): Promise<void>; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：FileVersion；  API声明：isFileConflict(uri: string): Promise<boolean>;  差异内容：isFileConflict(uri: string): Promise<boolean>; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：FileVersion；  API声明：clearFileConflict(uri: string): Promise<void>;  差异内容：clearFileConflict(uri: string): Promise<void>; | api/@ohos.file.cloudSync.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CloudFileCache；  API声明：on(event: 'batchDownload', callback: Callback<MultiDownloadProgress>): void;  差异内容：on(event: 'batchDownload', callback: Callback<MultiDownloadProgress>): void; | api/@ohos.file.cloudSync.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CloudFileCache；  API声明：off(event: 'batchDownload', callback?: Callback<MultiDownloadProgress>): void;  差异内容：off(event: 'batchDownload', callback?: Callback<MultiDownloadProgress>): void; | api/@ohos.file.cloudSync.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CloudFileCache；  API声明：startBatch(uris: Array<string>, fileType?: DownloadFileType): Promise<number>;  差异内容：startBatch(uris: Array<string>, fileType?: DownloadFileType): Promise<number>; | api/@ohos.file.cloudSync.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CloudFileCache；  API声明：stopBatch(downloadId: number, needClean?: boolean): Promise<void>;  差异内容：stopBatch(downloadId: number, needClean?: boolean): Promise<void>; | api/@ohos.file.cloudSync.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CloudFileCache；  API声明：cleanFileCache(uri: string): void;  差异内容：cleanFileCache(uri: string): void; | api/@ohos.file.cloudSync.d.ts |
