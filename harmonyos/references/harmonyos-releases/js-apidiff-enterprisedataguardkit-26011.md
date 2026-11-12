---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-enterprisedataguardkit-26011
title: Enterprise Data Guard Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > Enterprise Data Guard Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:53+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:7c3bc1208460e82b4df45f1bc389f36aed83ddb0e39f97d7b4207eed61494a4c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：FileGuard；  API声明：openFileWrite(path: string): Promise<number>;  差异内容：ohos.permission.FILE\_GUARD\_MANAGER | 类名：FileGuard；  API声明：openFileWrite(path: string): Promise<number>;  差异内容：ohos.permission.FILE\_GUARD\_MANAGER or ohos.permission.FILE\_GUARD\_FILE\_WRITE [since 26.0.1] | api/@hms.pcService.fileGuard.d.ts |
| 权限变更 | 类名：FileGuard；  API声明：openFileWrite(path: string, callback: AsyncCallback<number>): void;  差异内容：ohos.permission.FILE\_GUARD\_MANAGER | 类名：FileGuard；  API声明：openFileWrite(path: string, callback: AsyncCallback<number>): void;  差异内容：ohos.permission.FILE\_GUARD\_MANAGER or ohos.permission.FILE\_GUARD\_FILE\_WRITE [since 26.0.1] | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：fileGuard；  API声明：export enum DeletePolicyType  差异内容：export enum DeletePolicyType | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：DeletePolicyType；  API声明：ALL\_POLICY = 0  差异内容：ALL\_POLICY = 0 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：DeletePolicyType；  API声明：NETWORK\_POLICY = 1  差异内容：NETWORK\_POLICY = 1 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：DeletePolicyType；  API声明：KIA\_LIST = 2  差异内容：KIA\_LIST = 2 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：DeletePolicyType；  API声明：BLUETOOTH\_POLICY = 3  差异内容：BLUETOOTH\_POLICY = 3 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：DeletePolicyType；  API声明：NEARLINK\_POLICY = 4  差异内容：NEARLINK\_POLICY = 4 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：DeletePolicyType；  API声明：TRUST\_APP\_LIST\_POLICY = 5  差异内容：TRUST\_APP\_LIST\_POLICY = 5 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：DeletePolicyType；  API声明：TAG\_1 = 10  差异内容：TAG\_1 = 10 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：DeletePolicyType；  API声明：TAG\_2 = 11  差异内容：TAG\_2 = 11 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：DeletePolicyType；  API声明：TAG\_3 = 12  差异内容：TAG\_3 = 12 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：DeletePolicyType；  API声明：TAG\_4 = 13  差异内容：TAG\_4 = 13 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：DeletePolicyType；  API声明：TAG\_5 = 14  差异内容：TAG\_5 = 14 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：queryTrustedProcessUid(): Promise<Array<number>>;  差异内容：queryTrustedProcessUid(): Promise<Array<number>>; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：addTrustedProcessUid(uids: Array<number>): Promise<void>;  差异内容：addTrustedProcessUid(uids: Array<number>): Promise<void>; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：removeTrustedProcessUid(uids: Array<number>): Promise<void>;  差异内容：removeTrustedProcessUid(uids: Array<number>): Promise<void>; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：deletePolicy(type: DeletePolicyType, userId?: number): Promise<void>;  差异内容：deletePolicy(type: DeletePolicyType, userId?: number): Promise<void>; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：setKiaFileProtectionMode(protectionEnabled: boolean): Promise<void>;  差异内容：setKiaFileProtectionMode(protectionEnabled: boolean): Promise<void>; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：recoveryKey；  API声明：export interface DataVolumeEnterpriseRecoveryKeyInfo  差异内容：export interface DataVolumeEnterpriseRecoveryKeyInfo | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：DataVolumeEnterpriseRecoveryKeyInfo；  API声明：keyInfo: EnterpriseRecoveryKeyInfo;  差异内容：keyInfo: EnterpriseRecoveryKeyInfo; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：DataVolumeEnterpriseRecoveryKeyInfo；  API声明：uuid: string;  差异内容：uuid: string; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：recoveryKey；  API声明：function getDataVolumeEnterpriseRecoveryKey(path?: string): Promise<Array<DataVolumeEnterpriseRecoveryKeyInfo>>;  差异内容：function getDataVolumeEnterpriseRecoveryKey(path?: string): Promise<Array<DataVolumeEnterpriseRecoveryKeyInfo>>; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：recoveryKey；  API声明：function verifyUserByEnterpriseAuthentication(userId: number, inputData: string): Promise<void>;  差异内容：function verifyUserByEnterpriseAuthentication(userId: number, inputData: string): Promise<void>; | api/@hms.pcService.recoveryKeyService.d.ts |
