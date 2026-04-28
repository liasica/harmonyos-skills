---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-gameservicekit-510
title: Game Service Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Game Service Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:09+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:fe003bd283bd0453c29f6048112bab07735a364a009300f062989dc5b8bb934b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace gameNearbyTransfer  差异内容：declare namespace gameNearbyTransfer | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：interface CreateParameters  差异内容：interface CreateParameters | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：CreateParameters；  API声明：moduleName: string;  差异内容：moduleName: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：CreateParameters；  API声明：abilityName: string;  差异内容：abilityName: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：CreateParameters；  API声明：needShowSystemUI?: boolean;  差异内容：needShowSystemUI?: boolean; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：CreateParameters；  API声明：context?: common.UIAbilityContext;  差异内容：context?: common.UIAbilityContext; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：interface ConnectNotification  差异内容：interface ConnectNotification | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：ConnectNotification；  API声明：connectState: ConnectState;  差异内容：connectState: ConnectState; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：ConnectNotification；  API声明：message?: string;  差异内容：message?: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：ConnectNotification；  API声明：remoteDeviceName?: string;  差异内容：remoteDeviceName?: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：interface CreateResult  差异内容：interface CreateResult | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：CreateResult；  API声明：localDeviceName: string;  差异内容：localDeviceName: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：enum ConnectState  差异内容：enum ConnectState | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：ConnectState；  API声明：CONNECTED = 0  差异内容：CONNECTED = 0 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：ConnectState；  API声明：DISCONNECTED = 1  差异内容：DISCONNECTED = 1 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：interface TransferNotification  差异内容：interface TransferNotification | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：TransferNotification；  API声明：transferState: TransferState;  差异内容：transferState: TransferState; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：TransferNotification；  API声明：transferInfo: TransferInfo;  差异内容：transferInfo: TransferInfo; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：TransferNotification；  API声明：fileStoragePath?: string;  差异内容：fileStoragePath?: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：enum TransferState  差异内容：enum TransferState | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：TransferState；  API声明：SEND\_START = 0  差异内容：SEND\_START = 0 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：TransferState；  API声明：SEND\_PROCESS = 1  差异内容：SEND\_PROCESS = 1 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：TransferState；  API声明：SEND\_FINISH = 2  差异内容：SEND\_FINISH = 2 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：TransferState；  API声明：SEND\_ERROR = 3  差异内容：SEND\_ERROR = 3 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：TransferState；  API声明：RECEIVE\_START = 4  差异内容：RECEIVE\_START = 4 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：TransferState；  API声明：RECEIVE\_PROCESS = 5  差异内容：RECEIVE\_PROCESS = 5 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：TransferState；  API声明：RECEIVE\_FINISH = 6  差异内容：RECEIVE\_FINISH = 6 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：TransferState；  API声明：RECEIVE\_ERROR = 7  差异内容：RECEIVE\_ERROR = 7 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：interface FileInfo  差异内容：interface FileInfo | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：FileInfo；  API声明：path: string;  差异内容：path: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：FileInfo；  API声明：hash?: string;  差异内容：hash?: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：interface PackageInfo  差异内容：interface PackageInfo | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：PackageInfo；  API声明：name?: string;  差异内容：name?: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：PackageInfo；  API声明：version?: string;  差异内容：version?: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：PackageInfo；  API声明：files?: Array<FileInfo>;  差异内容：files?: Array<FileInfo>; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：PackageInfo；  API声明：extraData?: string;  差异内容：extraData?: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：interface PackageFile  差异内容：interface PackageFile | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：PackageFile；  API声明：srcPath: string;  差异内容：srcPath: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：PackageFile；  API声明：destPath: string;  差异内容：destPath: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：interface PackageData  差异内容：interface PackageData | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：PackageData；  API声明：name?: string;  差异内容：name?: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：PackageData；  API声明：version?: string;  差异内容：version?: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：PackageData；  API声明：files: Array<PackageFile>;  差异内容：files: Array<PackageFile>; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：interface ReturnResult  差异内容：interface ReturnResult | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：ReturnResult；  API声明：code: number;  差异内容：code: number; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：ReturnResult；  API声明：message?: string;  差异内容：message?: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：enum PackageInfoResultCode  差异内容：enum PackageInfoResultCode | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：PackageInfoResultCode；  API声明：ERROR = -1  差异内容：ERROR = -1 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：PackageInfoResultCode；  API声明：PACKAGE\_AVAILABLE\_COMPARED = 0  差异内容：PACKAGE\_AVAILABLE\_COMPARED = 0 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：PackageInfoResultCode；  API声明：PACKAGE\_UNAVAILABLE\_COMPARED = 1  差异内容：PACKAGE\_UNAVAILABLE\_COMPARED = 1 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：interface PackageInfoResult  差异内容：interface PackageInfoResult | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：PackageInfoResult；  API声明：packageInfoResultCode: PackageInfoResultCode;  差异内容：packageInfoResultCode: PackageInfoResultCode; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：PackageInfoResult；  API声明：message?: string;  差异内容：message?: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：interface TransferInfo  差异内容：interface TransferInfo | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：TransferInfo；  API声明：expectedTime: number;  差异内容：expectedTime: number; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：TransferInfo；  API声明：transferredPackageSize: number;  差异内容：transferredPackageSize: number; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：TransferInfo；  API声明：totalPackageSize: number;  差异内容：totalPackageSize: number; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：TransferInfo；  API声明：rate: number;  差异内容：rate: number; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：enum NearbyTransferErrorCode  差异内容：enum NearbyTransferErrorCode | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：NearbyTransferErrorCode；  API声明：INTERNAL\_ERROR = 1018300001  差异内容：INTERNAL\_ERROR = 1018300001 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：NearbyTransferErrorCode；  API声明：AUTH\_FAILED = 1018300002  差异内容：AUTH\_FAILED = 1018300002 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：NearbyTransferErrorCode；  API声明：INVALID\_REQUEST = 1018300003  差异内容：INVALID\_REQUEST = 1018300003 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：NearbyTransferErrorCode；  API声明：NO\_SERVICE\_AVAILABLE = 1018300004  差异内容：NO\_SERVICE\_AVAILABLE = 1018300004 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：NearbyTransferErrorCode；  API声明：WLAN\_BLUETOOTH\_MUST\_BE\_ON = 1018300005  差异内容：WLAN\_BLUETOOTH\_MUST\_BE\_ON = 1018300005 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：NearbyTransferErrorCode；  API声明：PUBLISH\_FAILED = 1018300006  差异内容：PUBLISH\_FAILED = 1018300006 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：NearbyTransferErrorCode；  API声明：DISCOVERY\_FAILED = 1018300007  差异内容：DISCOVERY\_FAILED = 1018300007 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：function on(type: 'connectNotify', callback: Callback<ConnectNotification>): void;  差异内容：function on(type: 'connectNotify', callback: Callback<ConnectNotification>): void; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：function off(type: 'connectNotify', callback?: Callback<ConnectNotification>): void;  差异内容：function off(type: 'connectNotify', callback?: Callback<ConnectNotification>): void; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：function on(type: 'receivePackageInfo', callback: Callback<PackageInfo>): void;  差异内容：function on(type: 'receivePackageInfo', callback: Callback<PackageInfo>): void; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：function off(type: 'receivePackageInfo', callback?: Callback<PackageInfo>): void;  差异内容：function off(type: 'receivePackageInfo', callback?: Callback<PackageInfo>): void; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：function on(type: 'transferNotify', callback: Callback<TransferNotification>): void;  差异内容：function on(type: 'transferNotify', callback: Callback<TransferNotification>): void; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：function off(type: 'transferNotify', callback?: Callback<TransferNotification>): void;  差异内容：function off(type: 'transferNotify', callback?: Callback<TransferNotification>): void; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：function on(type: 'error', callback: Callback<ReturnResult>): void;  差异内容：function on(type: 'error', callback: Callback<ReturnResult>): void; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：function off(type: 'error', callback?: Callback<ReturnResult>): void;  差异内容：function off(type: 'error', callback?: Callback<ReturnResult>): void; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：function create(createParameters: CreateParameters): Promise<CreateResult>;  差异内容：function create(createParameters: CreateParameters): Promise<CreateResult>; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：function publishNearbyGame(): Promise<void>;  差异内容：function publishNearbyGame(): Promise<void>; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：function autoBindNearbyGame(): Promise<void>;  差异内容：function autoBindNearbyGame(): Promise<void>; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：function acceptCollaboration(acceptParameters: Record<string, object>): Promise<void>;  差异内容：function acceptCollaboration(acceptParameters: Record<string, object>): Promise<void>; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：function sendPackageInfo(packageInfo: PackageInfo): Promise<void>;  差异内容：function sendPackageInfo(packageInfo: PackageInfo): Promise<void>; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：function replyPackageInfoResult(packageInfoResult: PackageInfoResult): Promise<void>;  差异内容：function replyPackageInfoResult(packageInfoResult: PackageInfoResult): Promise<void>; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：function transferPackageData(packageData: PackageData): Promise<void>;  差异内容：function transferPackageData(packageData: PackageData): Promise<void>; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：function destroy(): Promise<void>;  差异内容：function destroy(): Promise<void>; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gamePerformance；  API声明：enum GameCustomTag  差异内容：enum GameCustomTag | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：GameCustomTag；  API声明：CRASH = 1  差异内容：CRASH = 1 | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：gamePerformance；  API声明：function addGameCustomData(data: Record<string, string>, tag: GameCustomTag): void;  差异内容：function addGameCustomData(data: Record<string, string>, tag: GameCustomTag): void; | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.core.gameservice.gamenearbytransfer.d.ts  差异内容：GameServiceKit | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
