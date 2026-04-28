---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-6101
title: Basic Services Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > Basic Services Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a49306b20b0b79cf9241d3cdfcc5dc10ba69b585d337b713fcdf375efb8d79ef
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：GZip；  API声明：gzputc(char: number): Promise<number>;  差异内容：char: number | 类名：GZip；  API声明：gzputc(ch: number): Promise<number>;  差异内容：ch: number | api/@ohos.zlib.d.ts |
| 枚举赋值发生改变 | 类名：BatteryCapacityLevel；  API声明：LEVEL\_FULL  差异内容：0 | 类名：BatteryCapacityLevel；  API声明：LEVEL\_FULL  差异内容：1 | api/@ohos.batteryInfo.d.ts |
| 枚举赋值发生改变 | 类名：BatteryCapacityLevel；  API声明：LEVEL\_HIGH  差异内容：1 | 类名：BatteryCapacityLevel；  API声明：LEVEL\_HIGH  差异内容：2 | api/@ohos.batteryInfo.d.ts |
| 枚举赋值发生改变 | 类名：BatteryCapacityLevel；  API声明：LEVEL\_NORMAL  差异内容：2 | 类名：BatteryCapacityLevel；  API声明：LEVEL\_NORMAL  差异内容：3 | api/@ohos.batteryInfo.d.ts |
| 枚举赋值发生改变 | 类名：BatteryCapacityLevel；  API声明：LEVEL\_LOW  差异内容：3 | 类名：BatteryCapacityLevel；  API声明：LEVEL\_LOW  差异内容：4 | api/@ohos.batteryInfo.d.ts |
| 枚举赋值发生改变 | 类名：BatteryCapacityLevel；  API声明：LEVEL\_WARNING  差异内容：4 | 类名：BatteryCapacityLevel；  API声明：LEVEL\_WARNING  差异内容：5 | api/@ohos.batteryInfo.d.ts |
| 枚举赋值发生改变 | 类名：BatteryCapacityLevel；  API声明：LEVEL\_CRITICAL  差异内容：5 | 类名：BatteryCapacityLevel；  API声明：LEVEL\_CRITICAL  差异内容：6 | api/@ohos.batteryInfo.d.ts |
| 枚举赋值发生改变 | 类名：BatteryCapacityLevel；  API声明：LEVEL\_SHUTDOWN  差异内容：6 | 类名：BatteryCapacityLevel；  API声明：LEVEL\_SHUTDOWN  差异内容：7 | api/@ohos.batteryInfo.d.ts |
| 新增API | NA | 类名：BatteryCapacityLevel；  API声明：LEVEL\_NONE  差异内容：LEVEL\_NONE | api/@ohos.batteryInfo.d.ts |
| 新增API | NA | 类名：ReturnStatus；  API声明：ERRNO = -1  差异内容：ERRNO = -1 | api/@ohos.zlib.d.ts |
| 新增API | NA | 类名：ReturnStatus；  API声明：STREAM\_ERROR = -2  差异内容：STREAM\_ERROR = -2 | api/@ohos.zlib.d.ts |
| 新增API | NA | 类名：ReturnStatus；  API声明：DATA\_ERROR = -3  差异内容：DATA\_ERROR = -3 | api/@ohos.zlib.d.ts |
| 新增API | NA | 类名：ReturnStatus；  API声明：MEM\_ERROR = -4  差异内容：MEM\_ERROR = -4 | api/@ohos.zlib.d.ts |
| 新增API | NA | 类名：ReturnStatus；  API声明：BUF\_ERROR = -5  差异内容：BUF\_ERROR = -5 | api/@ohos.zlib.d.ts |
| 新增API | NA | 类名：global；  API声明：export const enum SuppressWarningsType  差异内容：export const enum SuppressWarningsType | api/@ohos.annotation.d.ets |
| 新增API | NA | 类名：SuppressWarningsType；  API声明：COMPATIBILITY = 'compatibility'  差异内容：COMPATIBILITY = 'compatibility' | api/@ohos.annotation.d.ets |
| 新增API | NA | 类名：Support；  API声明：COMMON\_EVENT\_BLUETOOTH\_HOST\_SCAN\_MODE\_CHANGE = 'usual.event.bluetooth.host.SCAN\_MODE\_CHANGE'  差异内容：COMMON\_EVENT\_BLUETOOTH\_HOST\_SCAN\_MODE\_CHANGE = 'usual.event.bluetooth.host.SCAN\_MODE\_CHANGE' | api/@ohos.commonEventManager.d.ts |
| 新增API | NA | 类名：Support；  API声明：COMMON\_EVENT\_TABLET\_MODE\_CHANGED = 'usual.event.TABLET\_MODE\_CHANGED'  差异内容：COMMON\_EVENT\_TABLET\_MODE\_CHANGED = 'usual.event.TABLET\_MODE\_CHANGED' | api/@ohos.commonEventManager.d.ts |
| 新增API | NA | 类名：Support；  API声明：COMMON\_EVENT\_LID\_STATE\_CHANGED = 'usual.event.LID\_STATE\_CHANGED'  差异内容：COMMON\_EVENT\_LID\_STATE\_CHANGED = 'usual.event.LID\_STATE\_CHANGED' | api/@ohos.commonEventManager.d.ts |
| 新增API | NA | 类名：print；  API声明：interface PrintJobData  差异内容：interface PrintJobData | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobData；  API声明：printerId: string;  差异内容：printerId: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobData；  API声明：jobName: string;  差异内容：jobName: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobData；  API声明：documentFormat: PrintDocumentFormat;  差异内容：documentFormat: PrintDocumentFormat; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobData；  API声明：docFlavor: DocFlavor;  差异内容：docFlavor: DocFlavor; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobData；  API声明：copyNumber: number;  差异内容：copyNumber: number; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobData；  API声明：isLandscape: boolean;  差异内容：isLandscape: boolean; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobData；  API声明：colorMode: PrintColorMode;  差异内容：colorMode: PrintColorMode; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobData；  API声明：duplexMode: PrintDuplexMode;  差异内容：duplexMode: PrintDuplexMode; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobData；  API声明：pageSize: PrintPageSize;  差异内容：pageSize: PrintPageSize; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobData；  API声明：jobId?: string;  差异内容：jobId?: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobData；  API声明：fdList?: number[];  差异内容：fdList?: number[]; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobData；  API声明：binaryData?: Uint8Array;  差异内容：binaryData?: Uint8Array; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobData；  API声明：printQuality?: PrintQuality;  差异内容：printQuality?: PrintQuality; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobData；  API声明：mediaType?: string;  差异内容：mediaType?: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobData；  API声明：isBorderless?: boolean;  差异内容：isBorderless?: boolean; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobData；  API声明：isAutoRotate?: boolean;  差异内容：isAutoRotate?: boolean; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobData；  API声明：isReverse?: boolean;  差异内容：isReverse?: boolean; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobData；  API声明：isCollate?: boolean;  差异内容：isCollate?: boolean; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobData；  API声明：isSequential?: boolean;  差异内容：isSequential?: boolean; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobData；  API声明：options?: string;  差异内容：options?: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：enum PrintDocumentFormat  差异内容：enum PrintDocumentFormat | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintDocumentFormat；  API声明：DOCUMENT\_FORMAT\_AUTO = 0  差异内容：DOCUMENT\_FORMAT\_AUTO = 0 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintDocumentFormat；  API声明：DOCUMENT\_FORMAT\_JPEG = 1  差异内容：DOCUMENT\_FORMAT\_JPEG = 1 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintDocumentFormat；  API声明：DOCUMENT\_FORMAT\_PDF = 2  差异内容：DOCUMENT\_FORMAT\_PDF = 2 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintDocumentFormat；  API声明：DOCUMENT\_FORMAT\_POSTSCRIPT = 3  差异内容：DOCUMENT\_FORMAT\_POSTSCRIPT = 3 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintDocumentFormat；  API声明：DOCUMENT\_FORMAT\_TEXT = 4  差异内容：DOCUMENT\_FORMAT\_TEXT = 4 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintDocumentFormat；  API声明：DOCUMENT\_FORMAT\_RAW = 5  差异内容：DOCUMENT\_FORMAT\_RAW = 5 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：enum DocFlavor  差异内容：enum DocFlavor | api/@ohos.print.d.ts |
| 新增API | NA | 类名：DocFlavor；  API声明：FILE\_DESCRIPTOR = 0  差异内容：FILE\_DESCRIPTOR = 0 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：DocFlavor；  API声明：BYTES = 1  差异内容：BYTES = 1 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：function startPrint(job: PrintJobData): Promise<void>;  差异内容：function startPrint(job: PrintJobData): Promise<void>; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：cacheDownload；  API声明：enum CacheStrategy  差异内容：enum CacheStrategy | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：CacheStrategy；  API声明：FORCE = 0  差异内容：FORCE = 0 | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：CacheStrategy；  API声明：LAZY = 1  差异内容：LAZY = 1 | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：cacheDownload；  API声明：enum ErrorCode  差异内容：enum ErrorCode | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：ErrorCode；  API声明：OTHERS = 0xFF  差异内容：OTHERS = 0xFF | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：ErrorCode；  API声明：DNS = 0x00  差异内容：DNS = 0x00 | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：ErrorCode；  API声明：TCP = 0x10  差异内容：TCP = 0x10 | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：ErrorCode；  API声明：SSL = 0x20  差异内容：SSL = 0x20 | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：ErrorCode；  API声明：HTTP = 0x30  差异内容：HTTP = 0x30 | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：CacheDownloadOptions；  API声明：cacheStrategy?: CacheStrategy;  差异内容：cacheStrategy?: CacheStrategy; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：NetworkInfo；  API声明：readonly ip?: string;  差异内容：readonly ip?: string; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：cacheDownload；  API声明：interface DownloadError  差异内容：interface DownloadError | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：DownloadError；  API声明：readonly errorCode: ErrorCode;  差异内容：readonly errorCode: ErrorCode; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：DownloadError；  API声明：readonly message: string;  差异内容：readonly message: string; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：cacheDownload；  API声明：function clearMemoryCache(): void;  差异内容：function clearMemoryCache(): void; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：cacheDownload；  API声明：function clearFileCache(): void;  差异内容：function clearFileCache(): void; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：cacheDownload；  API声明：function onDownloadSuccess(url: string, callback: Callback<void>): void;  差异内容：function onDownloadSuccess(url: string, callback: Callback<void>): void; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：cacheDownload；  API声明：function onDownloadError(url: string, callback: Callback<DownloadError>): void;  差异内容：function onDownloadError(url: string, callback: Callback<DownloadError>): void; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：cacheDownload；  API声明：function offDownloadSuccess(url: string, callback?: Callback<void>): void;  差异内容：function offDownloadSuccess(url: string, callback?: Callback<void>): void; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：cacheDownload；  API声明：function offDownloadError(url: string, callback?: Callback<DownloadError>): void;  差异内容：function offDownloadError(url: string, callback?: Callback<DownloadError>): void; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：RunningLockType；  API声明：BACKGROUND\_USER\_IDLE = 129  差异内容：BACKGROUND\_USER\_IDLE = 129 | api/@ohos.runningLock.d.ts |
| 新增API | NA | 类名：settings；  API声明：function openInputMethodSettings(context: Context): void;  差异内容：function openInputMethodSettings(context: Context): void; | api/@ohos.settings.d.ts |
| 新增API | NA | 类名：settings；  API声明：function openInputMethodDetail(context: Context, bundleName: string, inputMethodId: string): void;  差异内容：function openInputMethodDetail(context: Context, bundleName: string, inputMethodId: string): void; | api/@ohos.settings.d.ts |
| 属性类型匿名对象整改不兼容 | 类名：PasteDataProperty；  API声明：additions: {  [key: string]: object;  };  差异内容：{  [key: string]: object;  } | 类名：PasteDataProperty；  API声明：additions: Record<string, object>;  差异内容：Record<string, object> | api/@ohos.pasteboard.d.ts |
| 属性类型匿名对象整改不兼容 | 类名：PasteDataRecord；  API声明：data: {  [mimeType: string]: ArrayBuffer;  };  差异内容：{  [mimeType: string]: ArrayBuffer;  } | 类名：PasteDataRecord；  API声明：data: Record<string, ArrayBuffer>;  差异内容：Record<string, ArrayBuffer> | api/@ohos.pasteboard.d.ts |
