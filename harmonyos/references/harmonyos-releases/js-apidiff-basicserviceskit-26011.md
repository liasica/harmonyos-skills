---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-26011
title: Basic Services Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > Basic Services Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:53+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:ceaec76257130be6cfce7861a6e7d84ef4e5281b28487825e181be8a771c7835
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace authorization  差异内容：declare namespace authorization | api/@ohos.account.osAccount.authorization.d.ts |
| 新增API | NA | 类名：authorization；  API声明：function getAuthorizationManager(): AuthorizationManager;  差异内容：function getAuthorizationManager(): AuthorizationManager; | api/@ohos.account.osAccount.authorization.d.ts |
| 新增API | NA | 类名：authorization；  API声明：interface AuthorizationManager  差异内容：interface AuthorizationManager | api/@ohos.account.osAccount.authorization.d.ts |
| 新增API | NA | 类名：AuthorizationManager；  API声明：requestAuthorization(privilege: Privilege, context: UIAbilityContext): Promise<AuthorizationResult>;  差异内容：requestAuthorization(privilege: Privilege, context: UIAbilityContext): Promise<AuthorizationResult>; | api/@ohos.account.osAccount.authorization.d.ts |
| 新增API | NA | 类名：AuthorizationManager；  API声明：hasAuthorization(privilege: Privilege): Promise<boolean>;  差异内容：hasAuthorization(privilege: Privilege): Promise<boolean>; | api/@ohos.account.osAccount.authorization.d.ts |
| 新增API | NA | 类名：authorization；  API声明：enum Privilege  差异内容：enum Privilege | api/@ohos.account.osAccount.authorization.d.ts |
| 新增API | NA | 类名：Privilege；  API声明：PRIVILEGE\_OPERATE\_RAW\_NET\_PACKETS = 'ohos.privilege.operate\_raw\_net\_packets'  差异内容：PRIVILEGE\_OPERATE\_RAW\_NET\_PACKETS = 'ohos.privilege.operate\_raw\_net\_packets' | api/@ohos.account.osAccount.authorization.d.ts |
| 新增API | NA | 类名：authorization；  API声明：enum AuthorizationResultCode  差异内容：enum AuthorizationResultCode | api/@ohos.account.osAccount.authorization.d.ts |
| 新增API | NA | 类名：AuthorizationResultCode；  API声明：AUTHORIZATION\_GRANTED = 0  差异内容：AUTHORIZATION\_GRANTED = 0 | api/@ohos.account.osAccount.authorization.d.ts |
| 新增API | NA | 类名：AuthorizationResultCode；  API声明：AUTHORIZATION\_CANCELED = 12300301  差异内容：AUTHORIZATION\_CANCELED = 12300301 | api/@ohos.account.osAccount.authorization.d.ts |
| 新增API | NA | 类名：AuthorizationResultCode；  API声明：AUTHORIZATION\_DENIED = 12300303  差异内容：AUTHORIZATION\_DENIED = 12300303 | api/@ohos.account.osAccount.authorization.d.ts |
| 新增API | NA | 类名：AuthorizationResultCode；  API声明：AUTHORIZATION\_NOT\_SUPPORTED = 12300305  差异内容：AUTHORIZATION\_NOT\_SUPPORTED = 12300305 | api/@ohos.account.osAccount.authorization.d.ts |
| 新增API | NA | 类名：authorization；  API声明：interface AuthorizationResult  差异内容：interface AuthorizationResult | api/@ohos.account.osAccount.authorization.d.ts |
| 新增API | NA | 类名：AuthorizationResult；  API声明：resultCode: AuthorizationResultCode;  差异内容：resultCode: AuthorizationResultCode; | api/@ohos.account.osAccount.authorization.d.ts |
| 新增API | NA | 类名：AuthorizationResult；  API声明：privilege: Privilege;  差异内容：privilege: Privilege; | api/@ohos.account.osAccount.authorization.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace boardInfo  差异内容：declare namespace boardInfo | api/@ohos.boardInfo.d.ts |
| 新增API | NA | 类名：boardInfo；  API声明：const cpuId: string;  差异内容：const cpuId: string; | api/@ohos.boardInfo.d.ts |
| 新增API | NA | 类名：boardInfo；  API声明：const cpuArch: string;  差异内容：const cpuArch: string; | api/@ohos.boardInfo.d.ts |
| 新增API | NA | 类名：boardInfo；  API声明：const cpuVendor: string;  差异内容：const cpuVendor: string; | api/@ohos.boardInfo.d.ts |
| 新增API | NA | 类名：boardInfo；  API声明：const boardSn: string;  差异内容：const boardSn: string; | api/@ohos.boardInfo.d.ts |
| 新增API | NA | 类名：boardInfo；  API声明：const boardVendor: string;  差异内容：const boardVendor: string; | api/@ohos.boardInfo.d.ts |
| 新增API | NA | 类名：boardInfo；  API声明：const boardName: string;  差异内容：const boardName: string; | api/@ohos.boardInfo.d.ts |
| 新增API | NA | 类名：boardInfo；  API声明：const biosVendor: string;  差异内容：const biosVendor: string; | api/@ohos.boardInfo.d.ts |
| 新增API | NA | 类名：boardInfo；  API声明：const biosVersion: string;  差异内容：const biosVersion: string; | api/@ohos.boardInfo.d.ts |
| 新增API | NA | 类名：boardInfo；  API声明：const biosDate: string;  差异内容：const biosDate: string; | api/@ohos.boardInfo.d.ts |
| 新增API | NA | 类名：deviceInfo；  API声明：const kernelVersion: string;  差异内容：const kernelVersion: string; | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：function claimInterfaceExclusive(pipe: USBDevicePipe, iface: USBInterface, force?: boolean, onConflict?: Callback<InterfaceConflictInfo>): void;  差异内容：function claimInterfaceExclusive(pipe: USBDevicePipe, iface: USBInterface, force?: boolean, onConflict?: Callback<InterfaceConflictInfo>): void; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：interface InterfaceConflictInfo  差异内容：interface InterfaceConflictInfo | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：InterfaceConflictInfo；  API声明：busNum: number;  差异内容：busNum: number; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：InterfaceConflictInfo；  API声明：devAddr: number;  差异内容：devAddr: number; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：InterfaceConflictInfo；  API声明：interfaceId: number;  差异内容：interfaceId: number; | api/@ohos.usbManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.account.osAccount.authorization.d.ts  差异内容：BasicServicesKit | api/@ohos.account.osAccount.authorization.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.boardInfo.d.ts  差异内容：BasicServicesKit | api/@ohos.boardInfo.d.ts |
