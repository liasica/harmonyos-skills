---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-enterprisedataguardkit-5032
title: Enterprise DataGuard Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:35+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:f411d1edb9470232f5e3dbac1c9632dfbe54f375a12229939dde5807ed29dc96
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace recoveryKey  差异内容： declare namespace recoveryKey | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：recoveryKey；  API声明： export interface EnterpriseRecoveryKeyInfo  差异内容： export interface EnterpriseRecoveryKeyInfo | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：EnterpriseRecoveryKeyInfo；  API声明：enterpriseRecoveryKey: Uint8Array;  差异内容：enterpriseRecoveryKey: Uint8Array; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：EnterpriseRecoveryKeyInfo；  API声明：exportPublicKey: Uint8Array;  差异内容：exportPublicKey: Uint8Array; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：EnterpriseRecoveryKeyInfo；  API声明：iv: Uint8Array;  差异内容：iv: Uint8Array; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：EnterpriseRecoveryKeyInfo；  API声明：tag: Uint8Array;  差异内容：tag: Uint8Array; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：recoveryKey；  API声明：function getAuthChallenge(): Promise<Uint8Array>;  差异内容：function getAuthChallenge(): Promise<Uint8Array>; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：recoveryKey；  API声明：function updateEnterpriseCertificate(signature: Uint8Array, cert: Uint8Array): Promise<number>;  差异内容：function updateEnterpriseCertificate(signature: Uint8Array, cert: Uint8Array): Promise<number>; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：recoveryKey；  API声明：function getEnterpriseRecoveryKey(userId: number): Promise<EnterpriseRecoveryKeyInfo>;  差异内容：function getEnterpriseRecoveryKey(userId: number): Promise<EnterpriseRecoveryKeyInfo>; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：recoveryKey；  API声明：function deleteEnterpriseRecoveryKey(userId: number, signature: Uint8Array): Promise<number>;  差异内容：function deleteEnterpriseRecoveryKey(userId: number, signature: Uint8Array): Promise<number>; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：on(type: 'kiaCopy', callback: Callback<string>): void;  差异内容：on(type: 'kiaCopy', callback: Callback<string>): void; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：off(type: 'kiaCopy', callback?: Callback<string>): void;  差异内容：off(type: 'kiaCopy', callback?: Callback<string>): void; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：on(type: 'kiaRename', callback: Callback<string>): void;  差异内容：on(type: 'kiaRename', callback: Callback<string>): void; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：off(type: 'kiaRename', callback?: Callback<string>): void;  差异内容：off(type: 'kiaRename', callback?: Callback<string>): void; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：on(type: 'kiaCompress', callback: Callback<string>): void;  差异内容：on(type: 'kiaCompress', callback: Callback<string>): void; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：off(type: 'kiaCompress', callback?: Callback<string>): void;  差异内容：off(type: 'kiaCompress', callback?: Callback<string>): void; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：setKiaWatermarkImage(image: Uint8Array, info: string): Promise<void>;  差异内容：setKiaWatermarkImage(image: Uint8Array, info: string): Promise<void>; | api/@hms.pcService.fileGuard.d.ts |
| kit变更 | NA | EnterpriseDataGuardKit | api/@hms.pcService.recoveryKeyService.d.ts |
