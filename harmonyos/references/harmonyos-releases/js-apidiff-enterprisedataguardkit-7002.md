---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-enterprisedataguardkit-7002
title: Enterprise Data Guard Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Enterprise Data Guard Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-08-04
content_hash: sha256:7d15f6abcb57fbbe0475a04b91a154345589d9d1d6a8a4ce95249f1703cc8417
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：FileGuard；  API声明：startFileScanTask(type: CommonDirScanType, callback: ScanFileCallback, batchNum?: number): void;  差异内容：NA | 类名：FileGuard；  API声明：startFileScanTask(type: CommonDirScanType, callback: ScanFileCallback, batchNum?: number): void;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：startFileScanTask(path: string, callback: ScanFileCallback, batchNum?: number): void;  差异内容：NA | 类名：FileGuard；  API声明：startFileScanTask(path: string, callback: ScanFileCallback, batchNum?: number): void;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：openFile(path: string, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：FileGuard；  API声明：openFile(path: string, callback: AsyncCallback<number>): void;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：openFile(path: string): Promise<number>;  差异内容：NA | 类名：FileGuard；  API声明：openFile(path: string): Promise<number>;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：setFileTag(path: string, level: SecurityLevel, tag: string, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：FileGuard；  API声明：setFileTag(path: string, level: SecurityLevel, tag: string, callback: AsyncCallback<void>): void;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：setFileTag(path: string, level: SecurityLevel, tag: string): Promise<void>;  差异内容：NA | 类名：FileGuard；  API声明：setFileTag(path: string, level: SecurityLevel, tag: string): Promise<void>;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：queryFileTag(path: string, callback: AsyncCallback<FileTagInfo>): void;  差异内容：NA | 类名：FileGuard；  API声明：queryFileTag(path: string, callback: AsyncCallback<FileTagInfo>): void;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：queryFileTag(path: string): Promise<FileTagInfo>;  差异内容：NA | 类名：FileGuard；  API声明：queryFileTag(path: string): Promise<FileTagInfo>;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：getFileUri(path: string, callback: AsyncCallback<FilePathInfo>): void;  差异内容：NA | 类名：FileGuard；  API声明：getFileUri(path: string, callback: AsyncCallback<FilePathInfo>): void;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：getFileUri(path: string): Promise<FilePathInfo>;  差异内容：NA | 类名：FileGuard；  API声明：getFileUri(path: string): Promise<FilePathInfo>;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：deleteFile(path: string, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：FileGuard；  API声明：deleteFile(path: string, callback: AsyncCallback<void>): void;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：deleteFile(path: string): Promise<void>;  差异内容：NA | 类名：FileGuard；  API声明：deleteFile(path: string): Promise<void>;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：updatePolicy(policy: string, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：FileGuard；  API声明：updatePolicy(policy: string, callback: AsyncCallback<void>): void;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：updatePolicy(policy: string): Promise<void>;  差异内容：NA | 类名：FileGuard；  API声明：updatePolicy(policy: string): Promise<void>;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：getPolicy(): Promise<string | null>;  差异内容：NA | 类名：FileGuard；  API声明：getPolicy(): Promise<string | null>;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：setKiaFilelist(filelist: string, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：FileGuard；  API声明：setKiaFilelist(filelist: string, callback: AsyncCallback<void>): void;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：setKiaFilelist(filelist: string): Promise<void>;  差异内容：NA | 类名：FileGuard；  API声明：setKiaFilelist(filelist: string): Promise<void>;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：isKia(path: string): boolean;  差异内容：NA | 类名：FileGuard；  API声明：isKia(path: string): boolean;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：on(type: 'kiaCopy', callback: Callback<string>): void;  差异内容：NA | 类名：FileGuard；  API声明：on(type: 'kiaCopy', callback: Callback<string>): void;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：off(type: 'kiaCopy', callback?: Callback<string>): void;  差异内容：NA | 类名：FileGuard；  API声明：off(type: 'kiaCopy', callback?: Callback<string>): void;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：on(type: 'kiaRename', callback: Callback<string>): void;  差异内容：NA | 类名：FileGuard；  API声明：on(type: 'kiaRename', callback: Callback<string>): void;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：off(type: 'kiaRename', callback?: Callback<string>): void;  差异内容：NA | 类名：FileGuard；  API声明：off(type: 'kiaRename', callback?: Callback<string>): void;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：on(type: 'kiaCompress', callback: Callback<string>): void;  差异内容：NA | 类名：FileGuard；  API声明：on(type: 'kiaCompress', callback: Callback<string>): void;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：off(type: 'kiaCompress', callback?: Callback<string>): void;  差异内容：NA | 类名：FileGuard；  API声明：off(type: 'kiaCompress', callback?: Callback<string>): void;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：setKiaWatermarkImage(image: Uint8Array, info: string): Promise<void>;  差异内容：NA | 类名：FileGuard；  API声明：setKiaWatermarkImage(image: Uint8Array, info: string): Promise<void>;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：openFileWrite(path: string): Promise<number>;  差异内容：NA | 类名：FileGuard；  API声明：openFileWrite(path: string): Promise<number>;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：openFileWrite(path: string, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：FileGuard；  API声明：openFileWrite(path: string, callback: AsyncCallback<number>): void;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：setFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：FileGuard；  API声明：setFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：setFileCustomTag(path: string, tagList: Array<string>): Promise<void>;  差异内容：NA | 类名：FileGuard；  API声明：setFileCustomTag(path: string, tagList: Array<string>): Promise<void>;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：unsetFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：FileGuard；  API声明：unsetFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：unsetFileCustomTag(path: string, tagList: Array<string>): Promise<void>;  差异内容：NA | 类名：FileGuard；  API声明：unsetFileCustomTag(path: string, tagList: Array<string>): Promise<void>;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：addUnrestrictedApplicationList(appIds: Array<string>, userId?: number): Promise<void>;  差异内容：NA | 类名：FileGuard；  API声明：addUnrestrictedApplicationList(appIds: Array<string>, userId?: number): Promise<void>;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：removeUnrestrictedApplicationList(appIds: Array<string>, userId?: number): Promise<void>;  差异内容：NA | 类名：FileGuard；  API声明：removeUnrestrictedApplicationList(appIds: Array<string>, userId?: number): Promise<void>;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：getUnrestrictedApplicationList(userId?: number): Promise<Array<string>>;  差异内容：NA | 类名：FileGuard；  API声明：getUnrestrictedApplicationList(userId?: number): Promise<Array<string>>;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：setHdcAuthenticationKey(devType: AuthenticateDeviceType, keyType: AuthenticateKeyType, key: Uint8Array): Promise<void>;  差异内容：NA | 类名：FileGuard；  API声明：setHdcAuthenticationKey(devType: AuthenticateDeviceType, keyType: AuthenticateKeyType, key: Uint8Array): Promise<void>;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：onPrintStartup(callback: Callback<void>): void;  差异内容：NA | 类名：FileGuard；  API声明：onPrintStartup(callback: Callback<void>): void;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：FileGuard；  API声明：offPrintStartup(callback?: Callback<void>): void;  差异内容：NA | 类名：FileGuard；  API声明：offPrintStartup(callback?: Callback<void>): void;  差异内容：801 | api/@hms.pcService.fileGuard.d.ts |
| 新增错误码 | 类名：recoveryKey；  API声明：function getAuthChallenge(): Promise<Uint8Array>;  差异内容：NA | 类名：recoveryKey；  API声明：function getAuthChallenge(): Promise<Uint8Array>;  差异内容：801 | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增错误码 | 类名：recoveryKey；  API声明：function updateEnterpriseCertificate(signature: Uint8Array, cert: Uint8Array): Promise<number>;  差异内容：NA | 类名：recoveryKey；  API声明：function updateEnterpriseCertificate(signature: Uint8Array, cert: Uint8Array): Promise<number>;  差异内容：801 | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增错误码 | 类名：recoveryKey；  API声明：function getEnterpriseRecoveryKey(userId: number): Promise<EnterpriseRecoveryKeyInfo>;  差异内容：NA | 类名：recoveryKey；  API声明：function getEnterpriseRecoveryKey(userId: number): Promise<EnterpriseRecoveryKeyInfo>;  差异内容：801 | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增错误码 | 类名：recoveryKey；  API声明：function deleteEnterpriseRecoveryKey(userId: number, signature: Uint8Array): Promise<number>;  差异内容：NA | 类名：recoveryKey；  API声明：function deleteEnterpriseRecoveryKey(userId: number, signature: Uint8Array): Promise<number>;  差异内容：801 | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增错误码 | 类名：recoveryKey；  API声明：function verifyUserIdentityEnterprise(userId: number, userType: number, pinCode: string): Promise<void>;  差异内容：NA | 类名：recoveryKey；  API声明：function verifyUserIdentityEnterprise(userId: number, userType: number, pinCode: string): Promise<void>;  差异内容：801 | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增错误码 | 类名：recoveryKey；  API声明：function getEnterpriseRecoveryKeyForResettingPin(userId: number, userType: number): Promise<EnterpriseRecoveryKeyInfo>;  差异内容：NA | 类名：recoveryKey；  API声明：function getEnterpriseRecoveryKeyForResettingPin(userId: number, userType: number): Promise<EnterpriseRecoveryKeyInfo>;  差异内容：801 | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增错误码 | 类名：recoveryKey；  API声明：function verifyUserByDialog(userId: number): Promise<void>;  差异内容：NA | 类名：recoveryKey；  API声明：function verifyUserByDialog(userId: number): Promise<void>;  差异内容：801 | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：fileGuard；  API声明：export enum ManagedProcessStatus  差异内容：export enum ManagedProcessStatus | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：ManagedProcessStatus；  API声明：TIME\_BASED = 0  差异内容：TIME\_BASED = 0 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：ManagedProcessStatus；  API声明：LIFE\_LONG = 1  差异内容：LIFE\_LONG = 1 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：fileGuard；  API声明：export interface ManagedProcessPolicy  差异内容：export interface ManagedProcessPolicy | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：ManagedProcessPolicy；  API声明：status: ManagedProcessStatus;  差异内容：status: ManagedProcessStatus; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：ManagedProcessPolicy；  API声明：time?: number;  差异内容：time?: number; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：fileGuard；  API声明：export interface ManagedProcessInfo  差异内容：export interface ManagedProcessInfo | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：ManagedProcessInfo；  API声明：pid: number;  差异内容：pid: number; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：ManagedProcessInfo；  API声明：policy?: string;  差异内容：policy?: string; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：getManagedProcessPolicy(): Promise<ManagedProcessPolicy | null>;  差异内容：getManagedProcessPolicy(): Promise<ManagedProcessPolicy | null>; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：setManagedProcessPolicy(policy: ManagedProcessPolicy): Promise<void>;  差异内容：setManagedProcessPolicy(policy: ManagedProcessPolicy): Promise<void>; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：getManagedProcessList(): Promise<ManagedProcessInfo[]>;  差异内容：getManagedProcessList(): Promise<ManagedProcessInfo[]>; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：addManagedProcess(processInfo: ManagedProcessInfo): Promise<void>;  差异内容：addManagedProcess(processInfo: ManagedProcessInfo): Promise<void>; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：removeManagedProcess(processInfo: ManagedProcessInfo): Promise<void>;  差异内容：removeManagedProcess(processInfo: ManagedProcessInfo): Promise<void>; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：isFileGuardSupported(): boolean;  差异内容：isFileGuardSupported(): boolean; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：recoveryKey；  API声明：function isRecoveryKeySupported(): boolean;  差异内容：function isRecoveryKeySupported(): boolean; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：recoveryKey；  API声明：function isRecoveryKeyForResettingPinSupported(): boolean;  差异内容：function isRecoveryKeyForResettingPinSupported(): boolean; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：recoveryKey；  API声明：function isDataVolumeRecoveryKeySupported(): boolean;  差异内容：function isDataVolumeRecoveryKeySupported(): boolean; | api/@hms.pcService.recoveryKeyService.d.ts |
