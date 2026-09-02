---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-7002
title: Basic Services Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Basic Services Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:03+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:ecb0f62c7f554c0d9e62c5a70f1ef267e4dc9130373846884091a1a98498681b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：print；  API声明：function print(files: Array<string>, callback: AsyncCallback<PrintTask>): void;  差异内容：NA | 类名：print；  API声明：function print(files: Array<string>, callback: AsyncCallback<PrintTask>): void;  差异内容：26.0.0 | api/@ohos.print.d.ts |
| API废弃版本变更 | 类名：print；  API声明：function print(files: Array<string>): Promise<PrintTask>;  差异内容：NA | 类名：print；  API声明：function print(files: Array<string>): Promise<PrintTask>;  差异内容：26.0.0 | api/@ohos.print.d.ts |
| API废弃版本变更 | 类名：settings；  API声明：function enableAirplaneMode(enable: boolean, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：settings；  API声明：function enableAirplaneMode(enable: boolean, callback: AsyncCallback<void>): void;  差异内容：26.0.0 | api/@ohos.settings.d.ts |
| API废弃版本变更 | 类名：settings；  API声明：function enableAirplaneMode(enable: boolean): Promise<void>;  差异内容：NA | 类名：settings；  API声明：function enableAirplaneMode(enable: boolean): Promise<void>;  差异内容：26.0.0 | api/@ohos.settings.d.ts |
| API废弃版本变更 | 类名：settings；  API声明：function canShowFloating(callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：settings；  API声明：function canShowFloating(callback: AsyncCallback<boolean>): void;  差异内容：26.0.0 | api/@ohos.settings.d.ts |
| API废弃版本变更 | 类名：settings；  API声明：function canShowFloating(): Promise<boolean>;  差异内容：NA | 类名：settings；  API声明：function canShowFloating(): Promise<boolean>;  差异内容：26.0.0 | api/@ohos.settings.d.ts |
| API废弃版本变更 | 类名：settings；  API声明：function getUriSync(name: string): string;  差异内容：NA | 类名：settings；  API声明：function getUriSync(name: string): string;  差异内容：26.0.0 | api/@ohos.settings.d.ts |
| 新增错误码 | 类名：AccountManager；  API声明：getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：AccountManager；  API声明：getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo, callback: AsyncCallback<number>): void;  差异内容：12300003 | api/@ohos.account.osAccount.d.ts |
| 新增错误码 | 类名：AccountManager；  API声明：getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo): Promise<number>;  差异内容：NA | 类名：AccountManager；  API声明：getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo): Promise<number>;  差异内容：12300003 | api/@ohos.account.osAccount.d.ts |
| 新增错误码 | 类名：Task；  API声明：on(event: 'progress', callback: (progress: Progress) => void): void;  差异内容：NA | 类名：Task；  API声明：on(event: 'progress', callback: (progress: Progress) => void): void;  差异内容：21900005 | api/@ohos.request.d.ts |
| 新增错误码 | 类名：Task；  API声明：off(event: 'progress', callback?: (progress: Progress) => void): void;  差异内容：NA | 类名：Task；  API声明：off(event: 'progress', callback?: (progress: Progress) => void): void;  差异内容：21900005 | api/@ohos.request.d.ts |
| 新增错误码 | 类名：Task；  API声明：on(event: 'completed', callback: (progress: Progress) => void): void;  差异内容：NA | 类名：Task；  API声明：on(event: 'completed', callback: (progress: Progress) => void): void;  差异内容：21900005 | api/@ohos.request.d.ts |
| 新增错误码 | 类名：Task；  API声明：off(event: 'completed', callback?: (progress: Progress) => void): void;  差异内容：NA | 类名：Task；  API声明：off(event: 'completed', callback?: (progress: Progress) => void): void;  差异内容：21900005 | api/@ohos.request.d.ts |
| 新增错误码 | 类名：Task；  API声明：on(event: 'failed', callback: (progress: Progress) => void): void;  差异内容：NA | 类名：Task；  API声明：on(event: 'failed', callback: (progress: Progress) => void): void;  差异内容：21900005 | api/@ohos.request.d.ts |
| 新增错误码 | 类名：Task；  API声明：off(event: 'failed', callback?: (progress: Progress) => void): void;  差异内容：NA | 类名：Task；  API声明：off(event: 'failed', callback?: (progress: Progress) => void): void;  差异内容：21900005 | api/@ohos.request.d.ts |
| 新增错误码 | 类名：Task；  API声明：pause(callback: AsyncCallback<void>): void;  差异内容：NA | 类名：Task；  API声明：pause(callback: AsyncCallback<void>): void;  差异内容：21900005 | api/@ohos.request.d.ts |
| 新增错误码 | 类名：Task；  API声明：pause(): Promise<void>;  差异内容：NA | 类名：Task；  API声明：pause(): Promise<void>;  差异内容：21900005 | api/@ohos.request.d.ts |
| 新增错误码 | 类名：Task；  API声明：resume(callback: AsyncCallback<void>): void;  差异内容：NA | 类名：Task；  API声明：resume(callback: AsyncCallback<void>): void;  差异内容：21900005 | api/@ohos.request.d.ts |
| 新增错误码 | 类名：Task；  API声明：resume(): Promise<void>;  差异内容：NA | 类名：Task；  API声明：resume(): Promise<void>;  差异内容：21900005 | api/@ohos.request.d.ts |
| 删除错误码 | 类名：AccountManager；  API声明：getCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>): void;  差异内容：401 | 类名：AccountManager；  API声明：getCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>): void;  差异内容：NA | api/@ohos.account.osAccount.d.ts |
| 错误码变更 | 类名：AppAccountManager；  API声明：setAppAccess(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback<void>): void;  差异内容：12300001,12300002,12300003,12400005,401 | 类名：AppAccountManager；  API声明：setAppAccess(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback<void>): void;  差异内容：12300001,12300002,12300003,12400001,12400005 | api/@ohos.account.appAccount.d.ts |
| 错误码变更 | 类名：AppAccountManager；  API声明：setAppAccess(name: string, bundleName: string, isAccessible: boolean): Promise<void>;  差异内容：12300001,12300002,12300003,12400005,401 | 类名：AppAccountManager；  API声明：setAppAccess(name: string, bundleName: string, isAccessible: boolean): Promise<void>;  差异内容：12300001,12300002,12300003,12400001,12400005 | api/@ohos.account.appAccount.d.ts |
| 错误码变更 | 类名：AppAccountManager；  API声明：getAccountsByOwner(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>): void;  差异内容：12300001,12300002,401 | 类名：AppAccountManager；  API声明：getAccountsByOwner(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>): void;  差异内容：12300001,12300002,12400001 | api/@ohos.account.appAccount.d.ts |
| 错误码变更 | 类名：AppAccountManager；  API声明：getAccountsByOwner(owner: string): Promise<Array<AppAccountInfo>>;  差异内容：12300001,12300002,401 | 类名：AppAccountManager；  API声明：getAccountsByOwner(owner: string): Promise<Array<AppAccountInfo>>;  差异内容：12300001,12300002,12400001 | api/@ohos.account.appAccount.d.ts |
| 错误码变更 | 类名：AppAccountManager；  API声明：on(type: 'accountChange', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void;  差异内容：12300001,12300002,401 | 类名：AppAccountManager；  API声明：on(type: 'accountChange', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void;  差异内容：12300001,12300002,12400001 | api/@ohos.account.appAccount.d.ts |
| 错误码变更 | 类名：AppAccountManager；  API声明：setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean, callback: AsyncCallback<void>): void;  差异内容：12300001,12300002,12300003,12300107,12400005,401 | 类名：AppAccountManager；  API声明：setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean, callback: AsyncCallback<void>): void;  差异内容：12300001,12300002,12300003,12300107,12400001,12400005 | api/@ohos.account.appAccount.d.ts |
| 错误码变更 | 类名：AppAccountManager；  API声明：setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean): Promise<void>;  差异内容：12300001,12300002,12300003,12300107,12400005,401 | 类名：AppAccountManager；  API声明：setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean): Promise<void>;  差异内容：12300001,12300002,12300003,12300107,12400001,12400005 | api/@ohos.account.appAccount.d.ts |
| 权限变更 | 类名：AccountManager；  API声明：getCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>): void;  差异内容：ohos.permission.MANAGE\_LOCAL\_ACCOUNTS or ohos.permission.GET\_LOCAL\_ACCOUNTS | 类名：AccountManager；  API声明：getCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>): void;  差异内容：ohos.permission.MANAGE\_LOCAL\_ACCOUNTS or ohos.permission.GET\_LOCAL\_ACCOUNTS [since 10] | api/@ohos.account.osAccount.d.ts |
| 权限变更 | 类名：AccountManager；  API声明：getCurrentOsAccount(): Promise<OsAccountInfo>;  差异内容：ohos.permission.MANAGE\_LOCAL\_ACCOUNTS or ohos.permission.GET\_LOCAL\_ACCOUNTS | 类名：AccountManager；  API声明：getCurrentOsAccount(): Promise<OsAccountInfo>;  差异内容：ohos.permission.MANAGE\_LOCAL\_ACCOUNTS or ohos.permission.GET\_LOCAL\_ACCOUNTS [since 10] | api/@ohos.account.osAccount.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace serial  差异内容：declare namespace serial | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：serial；  API声明：function getSerialPortList(): Promise<SerialPort[]>;  差异内容：function getSerialPortList(): Promise<SerialPort[]>; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：serial；  API声明：interface SerialPort  差异内容：interface SerialPort | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialPort；  API声明：readonly portInfo: SerialPortInfo;  差异内容：readonly portInfo: SerialPortInfo; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialPort；  API声明：open(config?: SerialConfigs): Promise<void>;  差异内容：open(config?: SerialConfigs): Promise<void>; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialPort；  API声明：close(): Promise<void>;  差异内容：close(): Promise<void>; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialPort；  API声明：write(data: Uint8Array, timeout?: number): Promise<number>;  差异内容：write(data: Uint8Array, timeout?: number): Promise<number>; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialPort；  API声明：onDataRead(callback: Callback<Uint8Array>): void;  差异内容：onDataRead(callback: Callback<Uint8Array>): void; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialPort；  API声明：offDataRead(callback?: Callback<Uint8Array>): void;  差异内容：offDataRead(callback?: Callback<Uint8Array>): void; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialPort；  API声明：flush(): Promise<void>;  差异内容：flush(): Promise<void>; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialPort；  API声明：drain(): Promise<void>;  差异内容：drain(): Promise<void>; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialPort；  API声明：setRts(enable: boolean): Promise<void>;  差异内容：setRts(enable: boolean): Promise<void>; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialPort；  API声明：getCts(): Promise<boolean>;  差异内容：getCts(): Promise<boolean>; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialPort；  API声明：sendBrk(): Promise<void>;  差异内容：sendBrk(): Promise<void>; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialPort；  API声明：onDisconnect(callback: Callback<void>): void;  差异内容：onDisconnect(callback: Callback<void>): void; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialPort；  API声明：offDisconnect(callback?: Callback<void>): void;  差异内容：offDisconnect(callback?: Callback<void>): void; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialPort；  API声明：setDtr(enable: boolean): Promise<void>;  差异内容：setDtr(enable: boolean): Promise<void>; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialPort；  API声明：getDsr(): Promise<boolean>;  差异内容：getDsr(): Promise<boolean>; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：serial；  API声明：interface SerialPortInfo  差异内容：interface SerialPortInfo | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialPortInfo；  API声明：portName: string;  差异内容：portName: string; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialPortInfo；  API声明：vendorId?: number;  差异内容：vendorId?: number; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialPortInfo；  API声明：productId?: number;  差异内容：productId?: number; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialPortInfo；  API声明：manufacturer?: string;  差异内容：manufacturer?: string; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：serial；  API声明：enum DataBits  差异内容：enum DataBits | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：DataBits；  API声明：FIVE = 5  差异内容：FIVE = 5 | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：DataBits；  API声明：SIX = 6  差异内容：SIX = 6 | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：DataBits；  API声明：SEVEN = 7  差异内容：SEVEN = 7 | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：DataBits；  API声明：EIGHT = 8  差异内容：EIGHT = 8 | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：serial；  API声明：enum StopBits  差异内容：enum StopBits | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：StopBits；  API声明：ONE = 1  差异内容：ONE = 1 | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：StopBits；  API声明：TWO = 2  差异内容：TWO = 2 | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：serial；  API声明：enum Parity  差异内容：enum Parity | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：Parity；  API声明：NONE = 'none'  差异内容：NONE = 'none' | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：Parity；  API声明：EVEN = 'even'  差异内容：EVEN = 'even' | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：Parity；  API声明：ODD = 'odd'  差异内容：ODD = 'odd' | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：Parity；  API声明：MARK = 'mark'  差异内容：MARK = 'mark' | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：Parity；  API声明：SPACE = 'space'  差异内容：SPACE = 'space' | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：serial；  API声明：interface SerialConfigs  差异内容：interface SerialConfigs | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialConfigs；  API声明：baudRate?: number;  差异内容：baudRate?: number; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialConfigs；  API声明：dataBits?: DataBits;  差异内容：dataBits?: DataBits; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialConfigs；  API声明：stopBits?: StopBits;  差异内容：stopBits?: StopBits; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialConfigs；  API声明：parity?: Parity;  差异内容：parity?: Parity; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialConfigs；  API声明：rtscts?: boolean;  差异内容：rtscts?: boolean; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialConfigs；  API声明：xon?: boolean;  差异内容：xon?: boolean; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialConfigs；  API声明：xoff?: boolean;  差异内容：xoff?: boolean; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：SerialConfigs；  API声明：xany?: boolean;  差异内容：xany?: boolean; | api/@ohos.busManager.serial.d.ts |
| 新增API | NA | 类名：global；  API声明：export default class PrintExtensionContext  差异内容：export default class PrintExtensionContext | api/application/PrintExtensionContext.d.ts |
| 新增API | NA | 类名：Support；  API声明：COMMON\_EVENT\_VOLUME\_DECRYPTED = 'usual.event.VOLUME\_DECRYPTED'  差异内容：COMMON\_EVENT\_VOLUME\_DECRYPTED = 'usual.event.VOLUME\_DECRYPTED' | api/@ohos.commonEventManager.d.ts |
| 新增API | NA | 类名：Support；  API声明：COMMON\_EVENT\_VOLUME\_ENCRYPTED = 'usual.event.VOLUME\_ENCRYPTED'  差异内容：COMMON\_EVENT\_VOLUME\_ENCRYPTED = 'usual.event.VOLUME\_ENCRYPTED' | api/@ohos.commonEventManager.d.ts |
| 新增API | NA | 类名：Support；  API声明：COMMON\_EVENT\_VOLUME\_ENCRYPTION\_POLICY\_SET = 'usual.event.VOLUME\_ENCRYPTION\_POLICY\_SET'  差异内容：COMMON\_EVENT\_VOLUME\_ENCRYPTION\_POLICY\_SET = 'usual.event.VOLUME\_ENCRYPTION\_POLICY\_SET' | api/@ohos.commonEventManager.d.ts |
| 新增API | NA | 类名：Support；  API声明：COMMON\_EVENT\_SKILL\_CHANGED = 'usual.event.SKILL\_CHANGED'  差异内容：COMMON\_EVENT\_SKILL\_CHANGED = 'usual.event.SKILL\_CHANGED' | api/@ohos.commonEventManager.d.ts |
| 新增API | NA | 类名：PrintJob；  API声明：vendorOptions?: string;  差异内容：vendorOptions?: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobData；  API声明：vendorOptions?: string;  差异内容：vendorOptions?: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterCapabilities；  API声明：vendorPrinterPrefAbility?: string;  差异内容：vendorPrinterPrefAbility?: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterCapabilities；  API声明：vendorJobAttrAbility?: string;  差异内容：vendorJobAttrAbility?: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterPreferences；  API声明：vendorOptions?: string;  差异内容：vendorOptions?: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintExtensionAbility；  API声明：context: PrintExtensionContext;  差异内容：context: PrintExtensionContext; | api/@ohos.app.ability.PrintExtensionAbility.d.ts |
| 新增API | NA | 类名：cacheDownload；  API声明：interface TimeoutOptions  差异内容：interface TimeoutOptions | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：TimeoutOptions；  API声明：networkCheckTimeout?: number;  差异内容：networkCheckTimeout?: number; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：TimeoutOptions；  API声明：httpTotalTimeout?: number;  差异内容：httpTotalTimeout?: number; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：cacheDownload；  API声明：interface RetryOptions  差异内容：interface RetryOptions | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：RetryOptions；  API声明：maxRetryCount?: number;  差异内容：maxRetryCount?: number; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：CacheDownloadOptions；  API声明：retry?: RetryOptions;  差异内容：retry?: RetryOptions; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：CacheDownloadOptions；  API声明：timeout?: TimeoutOptions;  差异内容：timeout?: TimeoutOptions; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：cacheDownload；  API声明：function setGlobalRetryOptions(options?: RetryOptions): void;  差异内容：function setGlobalRetryOptions(options?: RetryOptions): void; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：cacheDownload；  API声明：function setGlobalTimeoutOptions(options?: TimeoutOptions): void;  差异内容：function setGlobalTimeoutOptions(options?: TimeoutOptions): void; | api/@ohos.request.cacheDownload.d.ts |
| 起始版本有变化 | 类名：commonEventManager；  API声明：export type CommonEventSubscribeInfo = \_CommonEventSubscribeInfo;  差异内容：11 | 类名：commonEventManager；  API声明：export type CommonEventSubscribeInfo = \_CommonEventSubscribeInfo;  差异内容：10 | api/@ohos.commonEventManager.d.ts |
| 新增kit | 类名：global；  API声明：api\commonEvent\commonEventSubscriber.d.ts  差异内容：NA | 类名：global；  API声明：api\commonEvent\commonEventSubscriber.d.ts  差异内容：BasicServicesKit | api/commonEvent/commonEventSubscriber.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.busManager.serial.d.ts  差异内容：BasicServicesKit | api/@ohos.busManager.serial.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\application\PrintExtensionContext.d.ts  差异内容：BasicServicesKit | api/application/PrintExtensionContext.d.ts |
