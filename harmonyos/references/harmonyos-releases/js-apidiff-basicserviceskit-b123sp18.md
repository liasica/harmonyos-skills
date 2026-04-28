---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-b123sp18
title: Basic Services Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > OS平台能力 > API变更清单 > Basic Services Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:49+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:f6f9f35e792ab023f3e7efdd963763503769ddba0780bbcb891eb3578c1de4e7
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：AppAccountManager；  API声明：setAppAccess(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback<void>): void;  差异内容：12300001,12300002,12300003,12400001,401 | 类名：AppAccountManager；  API声明：setAppAccess(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback<void>): void;  差异内容：12300001,12300002,12300003,12400005,401 | api/@ohos.account.appAccount.d.ts |
| 错误码变更 | 类名：AppAccountManager；  API声明：setAppAccess(name: string, bundleName: string, isAccessible: boolean): Promise<void>;  差异内容：12300001,12300002,12300003,12400001,401 | 类名：AppAccountManager；  API声明：setAppAccess(name: string, bundleName: string, isAccessible: boolean): Promise<void>;  差异内容：12300001,12300002,12300003,12400005,401 | api/@ohos.account.appAccount.d.ts |
| 错误码变更 | 类名：AppAccountManager；  API声明：getAccountsByOwner(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>): void;  差异内容：12300001,12300002,12400001,401 | 类名：AppAccountManager；  API声明：getAccountsByOwner(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>): void;  差异内容：12300001,12300002,401 | api/@ohos.account.appAccount.d.ts |
| 错误码变更 | 类名：AppAccountManager；  API声明：getAccountsByOwner(owner: string): Promise<Array<AppAccountInfo>>;  差异内容：12300001,12300002,12400001,401 | 类名：AppAccountManager；  API声明：getAccountsByOwner(owner: string): Promise<Array<AppAccountInfo>>;  差异内容：12300001,12300002,401 | api/@ohos.account.appAccount.d.ts |
| 错误码变更 | 类名：AppAccountManager；  API声明：on(type: 'accountChange', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void;  差异内容：12300001,12300002,12400001,401 | 类名：AppAccountManager；  API声明：on(type: 'accountChange', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void;  差异内容：12300001,12300002,401 | api/@ohos.account.appAccount.d.ts |
| 错误码变更 | 类名：AppAccountManager；  API声明：setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean, callback: AsyncCallback<void>): void;  差异内容：12300001,12300002,12300003,12300107,12400001,12400005,401 | 类名：AppAccountManager；  API声明：setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean, callback: AsyncCallback<void>): void;  差异内容：12300001,12300002,12300003,12300107,12400005,401 | api/@ohos.account.appAccount.d.ts |
| 错误码变更 | 类名：AppAccountManager；  API声明：setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean): Promise<void>;  差异内容：12300001,12300002,12300003,12300107,12400001,12400005,401 | 类名：AppAccountManager；  API声明：setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean): Promise<void>;  差异内容：12300001,12300002,12300003,12300107,12400005,401 | api/@ohos.account.appAccount.d.ts |
| 新增API | NA | 类名：global；  API声明： export default class PrintExtensionAbility  差异内容： export default class PrintExtensionAbility | api/@ohos.app.ability.PrintExtensionAbility.d.ts |
| 新增API | NA | 类名：PrintExtensionAbility；  API声明：onCreate(want: Want): void;  差异内容：onCreate(want: Want): void; | api/@ohos.app.ability.PrintExtensionAbility.d.ts |
| 新增API | NA | 类名：PrintExtensionAbility；  API声明：onStartDiscoverPrinter(): void;  差异内容：onStartDiscoverPrinter(): void; | api/@ohos.app.ability.PrintExtensionAbility.d.ts |
| 新增API | NA | 类名：PrintExtensionAbility；  API声明：onStopDiscoverPrinter(): void;  差异内容：onStopDiscoverPrinter(): void; | api/@ohos.app.ability.PrintExtensionAbility.d.ts |
| 新增API | NA | 类名：PrintExtensionAbility；  API声明：onConnectPrinter(printerId: number): void;  差异内容：onConnectPrinter(printerId: number): void; | api/@ohos.app.ability.PrintExtensionAbility.d.ts |
| 新增API | NA | 类名：PrintExtensionAbility；  API声明：onDisconnectPrinter(printerId: number): void;  差异内容：onDisconnectPrinter(printerId: number): void; | api/@ohos.app.ability.PrintExtensionAbility.d.ts |
| 新增API | NA | 类名：PrintExtensionAbility；  API声明：onDestroy(): void;  差异内容：onDestroy(): void; | api/@ohos.app.ability.PrintExtensionAbility.d.ts |
| 新增API | NA | 类名：pasteboard；  API声明：function createData(data: Record<string, ValueType>): PasteData;  差异内容：function createData(data: Record<string, ValueType>): PasteData; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：PasteDataRecord；  API声明：addEntry(type: string, value: ValueType): void;  差异内容：addEntry(type: string, value: ValueType): void; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：PasteDataRecord；  API声明：getValidTypes(types: Array<string>): Array<string>;  差异内容：getValidTypes(types: Array<string>): Array<string>; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：PasteDataRecord；  API声明：getData(type: string): Promise<ValueType>;  差异内容：getData(type: string): Promise<ValueType>; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：SystemPasteboard；  API声明：setAppShareOptions(shareOptions: ShareOption): void;  差异内容：setAppShareOptions(shareOptions: ShareOption): void; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：SystemPasteboard；  API声明：removeAppShareOptions(): void;  差异内容：removeAppShareOptions(): void; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：SystemPasteboard；  API声明：getMimeTypes(): Promise<Array<string>>;  差异内容：getMimeTypes(): Promise<Array<string>>; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：deviceInfo；  API声明：const productModelAlias: string;  差异内容：const productModelAlias: string; | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：print；  API声明： enum PrinterState  差异内容： enum PrinterState | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterState；  API声明：PRINTER\_ADDED = 0  差异内容：PRINTER\_ADDED = 0 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterState；  API声明：PRINTER\_REMOVED = 1  差异内容：PRINTER\_REMOVED = 1 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterState；  API声明：PRINTER\_CAPABILITY\_UPDATED = 2  差异内容：PRINTER\_CAPABILITY\_UPDATED = 2 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterState；  API声明：PRINTER\_CONNECTED = 3  差异内容：PRINTER\_CONNECTED = 3 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterState；  API声明：PRINTER\_DISCONNECTED = 4  差异内容：PRINTER\_DISCONNECTED = 4 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterState；  API声明：PRINTER\_RUNNING = 5  差异内容：PRINTER\_RUNNING = 5 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明： enum PrintJobState  差异内容： enum PrintJobState | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobState；  API声明：PRINT\_JOB\_PREPARE = 0  差异内容：PRINT\_JOB\_PREPARE = 0 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobState；  API声明：PRINT\_JOB\_QUEUED = 1  差异内容：PRINT\_JOB\_QUEUED = 1 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobState；  API声明：PRINT\_JOB\_RUNNING = 2  差异内容：PRINT\_JOB\_RUNNING = 2 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobState；  API声明：PRINT\_JOB\_BLOCKED = 3  差异内容：PRINT\_JOB\_BLOCKED = 3 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobState；  API声明：PRINT\_JOB\_COMPLETED = 4  差异内容：PRINT\_JOB\_COMPLETED = 4 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明： enum PrintJobSubState  差异内容： enum PrintJobSubState | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_COMPLETED\_SUCCESS = 0  差异内容：PRINT\_JOB\_COMPLETED\_SUCCESS = 0 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_COMPLETED\_FAILED = 1  差异内容：PRINT\_JOB\_COMPLETED\_FAILED = 1 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_COMPLETED\_CANCELLED = 2  差异内容：PRINT\_JOB\_COMPLETED\_CANCELLED = 2 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_COMPLETED\_FILE\_CORRUPTED = 3  差异内容：PRINT\_JOB\_COMPLETED\_FILE\_CORRUPTED = 3 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_OFFLINE = 4  差异内容：PRINT\_JOB\_BLOCK\_OFFLINE = 4 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_BUSY = 5  差异内容：PRINT\_JOB\_BLOCK\_BUSY = 5 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_CANCELLED = 6  差异内容：PRINT\_JOB\_BLOCK\_CANCELLED = 6 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_OUT\_OF\_PAPER = 7  差异内容：PRINT\_JOB\_BLOCK\_OUT\_OF\_PAPER = 7 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_OUT\_OF\_INK = 8  差异内容：PRINT\_JOB\_BLOCK\_OUT\_OF\_INK = 8 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_OUT\_OF\_TONER = 9  差异内容：PRINT\_JOB\_BLOCK\_OUT\_OF\_TONER = 9 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_JAMMED = 10  差异内容：PRINT\_JOB\_BLOCK\_JAMMED = 10 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_DOOR\_OPEN = 11  差异内容：PRINT\_JOB\_BLOCK\_DOOR\_OPEN = 11 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_SERVICE\_REQUEST = 12  差异内容：PRINT\_JOB\_BLOCK\_SERVICE\_REQUEST = 12 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_LOW\_ON\_INK = 13  差异内容：PRINT\_JOB\_BLOCK\_LOW\_ON\_INK = 13 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_LOW\_ON\_TONER = 14  差异内容：PRINT\_JOB\_BLOCK\_LOW\_ON\_TONER = 14 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_REALLY\_LOW\_ON\_INK = 15  差异内容：PRINT\_JOB\_BLOCK\_REALLY\_LOW\_ON\_INK = 15 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_BAD\_CERTIFICATE = 16  差异内容：PRINT\_JOB\_BLOCK\_BAD\_CERTIFICATE = 16 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_ACCOUNT\_ERROR = 18  差异内容：PRINT\_JOB\_BLOCK\_ACCOUNT\_ERROR = 18 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_PRINT\_PERMISSION\_ERROR = 19  差异内容：PRINT\_JOB\_BLOCK\_PRINT\_PERMISSION\_ERROR = 19 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_PRINT\_COLOR\_PERMISSION\_ERROR = 20  差异内容：PRINT\_JOB\_BLOCK\_PRINT\_COLOR\_PERMISSION\_ERROR = 20 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_NETWORK\_ERROR = 21  差异内容：PRINT\_JOB\_BLOCK\_NETWORK\_ERROR = 21 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_SERVER\_CONNECTION\_ERROR = 22  差异内容：PRINT\_JOB\_BLOCK\_SERVER\_CONNECTION\_ERROR = 22 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_LARGE\_FILE\_ERROR = 23  差异内容：PRINT\_JOB\_BLOCK\_LARGE\_FILE\_ERROR = 23 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_FILE\_PARSING\_ERROR = 24  差异内容：PRINT\_JOB\_BLOCK\_FILE\_PARSING\_ERROR = 24 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_SLOW\_FILE\_CONVERSION = 25  差异内容：PRINT\_JOB\_BLOCK\_SLOW\_FILE\_CONVERSION = 25 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_RUNNING\_UPLOADING\_FILES = 26  差异内容：PRINT\_JOB\_RUNNING\_UPLOADING\_FILES = 26 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_RUNNING\_CONVERTING\_FILES = 27  差异内容：PRINT\_JOB\_RUNNING\_CONVERTING\_FILES = 27 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_UNKNOWN = 99  差异内容：PRINT\_JOB\_BLOCK\_UNKNOWN = 99 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明： enum PrintErrorCode  差异内容： enum PrintErrorCode | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintErrorCode；  API声明：E\_PRINT\_NONE = 0  差异内容：E\_PRINT\_NONE = 0 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintErrorCode；  API声明：E\_PRINT\_NO\_PERMISSION = 201  差异内容：E\_PRINT\_NO\_PERMISSION = 201 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintErrorCode；  API声明：E\_PRINT\_INVALID\_PARAMETER = 401  差异内容：E\_PRINT\_INVALID\_PARAMETER = 401 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintErrorCode；  API声明：E\_PRINT\_GENERIC\_FAILURE = 13100001  差异内容：E\_PRINT\_GENERIC\_FAILURE = 13100001 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintErrorCode；  API声明：E\_PRINT\_RPC\_FAILURE = 13100002  差异内容：E\_PRINT\_RPC\_FAILURE = 13100002 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintErrorCode；  API声明：E\_PRINT\_SERVER\_FAILURE = 13100003  差异内容：E\_PRINT\_SERVER\_FAILURE = 13100003 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintErrorCode；  API声明：E\_PRINT\_INVALID\_EXTENSION = 13100004  差异内容：E\_PRINT\_INVALID\_EXTENSION = 13100004 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintErrorCode；  API声明：E\_PRINT\_INVALID\_PRINTER = 13100005  差异内容：E\_PRINT\_INVALID\_PRINTER = 13100005 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintErrorCode；  API声明：E\_PRINT\_INVALID\_PRINT\_JOB = 13100006  差异内容：E\_PRINT\_INVALID\_PRINT\_JOB = 13100006 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintErrorCode；  API声明：E\_PRINT\_FILE\_IO = 13100007  差异内容：E\_PRINT\_FILE\_IO = 13100007 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明： enum ApplicationEvent  差异内容： enum ApplicationEvent | api/@ohos.print.d.ts |
| 新增API | NA | 类名：ApplicationEvent；  API声明：APPLICATION\_CREATED = 0  差异内容：APPLICATION\_CREATED = 0 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：ApplicationEvent；  API声明：APPLICATION\_CLOSED\_FOR\_STARTED = 1  差异内容：APPLICATION\_CLOSED\_FOR\_STARTED = 1 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：ApplicationEvent；  API声明：APPLICATION\_CLOSED\_FOR\_CANCELED = 2  差异内容：APPLICATION\_CLOSED\_FOR\_CANCELED = 2 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：function addPrinterToDiscovery(printerInformation: PrinterInformation): Promise<void>;  差异内容：function addPrinterToDiscovery(printerInformation: PrinterInformation): Promise<void>; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：function updatePrinterInDiscovery(printerInformation: PrinterInformation): Promise<void>;  差异内容：function updatePrinterInDiscovery(printerInformation: PrinterInformation): Promise<void>; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：function removePrinterFromDiscovery(printerId: string): Promise<void>;  差异内容：function removePrinterFromDiscovery(printerId: string): Promise<void>; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：function getPrinterInformationById(printerId: string): Promise<PrinterInformation>;  差异内容：function getPrinterInformationById(printerId: string): Promise<PrinterInformation>; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明： interface PrinterInformation  差异内容： interface PrinterInformation | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterInformation；  API声明：printerId: string;  差异内容：printerId: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterInformation；  API声明：printerName: string;  差异内容：printerName: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterInformation；  API声明：printerStatus: PrinterStatus;  差异内容：printerStatus: PrinterStatus; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterInformation；  API声明：description?: string;  差异内容：description?: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterInformation；  API声明：capability?: PrinterCapabilities;  差异内容：capability?: PrinterCapabilities; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterInformation；  API声明：uri?: string;  差异内容：uri?: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterInformation；  API声明：printerMake?: string;  差异内容：printerMake?: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterInformation；  API声明：options?: string;  差异内容：options?: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明： interface PrinterCapabilities  差异内容： interface PrinterCapabilities | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterCapabilities；  API声明：supportedPageSizes: Array<PrintPageSize>;  差异内容：supportedPageSizes: Array<PrintPageSize>; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterCapabilities；  API声明：supportedColorModes: Array<PrintColorMode>;  差异内容：supportedColorModes: Array<PrintColorMode>; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterCapabilities；  API声明：supportedDuplexModes: Array<PrintDuplexMode>;  差异内容：supportedDuplexModes: Array<PrintDuplexMode>; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterCapabilities；  API声明：supportedMediaTypes?: Array<string>;  差异内容：supportedMediaTypes?: Array<string>; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterCapabilities；  API声明：supportedQualities?: Array<PrintQuality>;  差异内容：supportedQualities?: Array<PrintQuality>; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterCapabilities；  API声明：supportedOrientations?: Array<PrintOrientationMode>;  差异内容：supportedOrientations?: Array<PrintOrientationMode>; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterCapabilities；  API声明：options?: string;  差异内容：options?: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明： enum PrintQuality  差异内容： enum PrintQuality | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintQuality；  API声明：QUALITY\_DRAFT = 3  差异内容：QUALITY\_DRAFT = 3 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintQuality；  API声明：QUALITY\_NORMAL = 4  差异内容：QUALITY\_NORMAL = 4 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintQuality；  API声明：QUALITY\_HIGH = 5  差异内容：QUALITY\_HIGH = 5 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明： enum PrintOrientationMode  差异内容： enum PrintOrientationMode | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintOrientationMode；  API声明：ORIENTATION\_MODE\_PORTRAIT = 0  差异内容：ORIENTATION\_MODE\_PORTRAIT = 0 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintOrientationMode；  API声明：ORIENTATION\_MODE\_LANDSCAPE = 1  差异内容：ORIENTATION\_MODE\_LANDSCAPE = 1 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintOrientationMode；  API声明：ORIENTATION\_MODE\_REVERSE\_LANDSCAPE = 2  差异内容：ORIENTATION\_MODE\_REVERSE\_LANDSCAPE = 2 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintOrientationMode；  API声明：ORIENTATION\_MODE\_REVERSE\_PORTRAIT = 3  差异内容：ORIENTATION\_MODE\_REVERSE\_PORTRAIT = 3 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintOrientationMode；  API声明：ORIENTATION\_MODE\_NONE = 4  差异内容：ORIENTATION\_MODE\_NONE = 4 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明： enum PrinterStatus  差异内容： enum PrinterStatus | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterStatus；  API声明：PRINTER\_IDLE = 0  差异内容：PRINTER\_IDLE = 0 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterStatus；  API声明：PRINTER\_BUSY = 1  差异内容：PRINTER\_BUSY = 1 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterStatus；  API声明：PRINTER\_UNAVAILABLE = 2  差异内容：PRINTER\_UNAVAILABLE = 2 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：function hasAccessoryRight(accessory: USBAccessory): boolean;  差异内容：function hasAccessoryRight(accessory: USBAccessory): boolean; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：function requestAccessoryRight(accessory: USBAccessory): Promise<boolean>;  差异内容：function requestAccessoryRight(accessory: USBAccessory): Promise<boolean>; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：function cancelAccessoryRight(accessory: USBAccessory): void;  差异内容：function cancelAccessoryRight(accessory: USBAccessory): void; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：function getAccessoryList(): Array<Readonly<USBAccessory>>;  差异内容：function getAccessoryList(): Array<Readonly<USBAccessory>>; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：function openAccessory(accessory: USBAccessory): USBAccessoryHandle;  差异内容：function openAccessory(accessory: USBAccessory): USBAccessoryHandle; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：function closeAccessory(accessoryHandle: USBAccessoryHandle): void;  差异内容：function closeAccessory(accessoryHandle: USBAccessoryHandle): void; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明： interface USBAccessory  差异内容： interface USBAccessory | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：USBAccessory；  API声明：manufacturer: string;  差异内容：manufacturer: string; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：USBAccessory；  API声明：product: string;  差异内容：product: string; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：USBAccessory；  API声明：description: string;  差异内容：description: string; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：USBAccessory；  API声明：version: string;  差异内容：version: string; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：USBAccessory；  API声明：serialNumber: string;  差异内容：serialNumber: string; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明： interface USBAccessoryHandle  差异内容： interface USBAccessoryHandle | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：USBAccessoryHandle；  API声明：accessoryFd: number;  差异内容：accessoryFd: number; | api/@ohos.usbManager.d.ts |
