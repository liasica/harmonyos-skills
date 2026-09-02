---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-universalkeystorekit-7003
title: Universal Keystore Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Release引入的API > Universal Keystore Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f80e7c116e12b884aafc19f803c4f7078b701c05c717b273d97eeaed22308cdb
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：huks；  API声明：function generateKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：huks；  API声明：function generateKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<void>): void;  差异内容：201 | api/@ohos.security.huks.d.ts |
| 新增错误码 | 类名：huks；  API声明：function generateKeyItem(keyAlias: string, options: HuksOptions): Promise<void>;  差异内容：NA | 类名：huks；  API声明：function generateKeyItem(keyAlias: string, options: HuksOptions): Promise<void>;  差异内容：201 | api/@ohos.security.huks.d.ts |
| 新增错误码 | 类名：huks；  API声明：function deleteKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：huks；  API声明：function deleteKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<void>): void;  差异内容：201 | api/@ohos.security.huks.d.ts |
| 新增错误码 | 类名：huks；  API声明：function deleteKeyItem(keyAlias: string, options: HuksOptions): Promise<void>;  差异内容：NA | 类名：huks；  API声明：function deleteKeyItem(keyAlias: string, options: HuksOptions): Promise<void>;  差异内容：201 | api/@ohos.security.huks.d.ts |
| 新增错误码 | 类名：huks；  API声明：function importWrappedKeyItem(keyAlias: string, wrappingKeyAlias: string, options: HuksOptions, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：huks；  API声明：function importWrappedKeyItem(keyAlias: string, wrappingKeyAlias: string, options: HuksOptions, callback: AsyncCallback<void>): void;  差异内容：201 | api/@ohos.security.huks.d.ts |
| 新增错误码 | 类名：huks；  API声明：function importWrappedKeyItem(keyAlias: string, wrappingKeyAlias: string, options: HuksOptions): Promise<void>;  差异内容：NA | 类名：huks；  API声明：function importWrappedKeyItem(keyAlias: string, wrappingKeyAlias: string, options: HuksOptions): Promise<void>;  差异内容：201 | api/@ohos.security.huks.d.ts |
| 新增错误码 | 类名：huks；  API声明：function exportKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void;  差异内容：NA | 类名：huks；  API声明：function exportKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void;  差异内容：201 | api/@ohos.security.huks.d.ts |
| 新增错误码 | 类名：huks；  API声明：function exportKeyItem(keyAlias: string, options: HuksOptions): Promise<HuksReturnResult>;  差异内容：NA | 类名：huks；  API声明：function exportKeyItem(keyAlias: string, options: HuksOptions): Promise<HuksReturnResult>;  差异内容：201 | api/@ohos.security.huks.d.ts |
| 新增错误码 | 类名：huks；  API声明：function getKeyItemProperties(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void;  差异内容：NA | 类名：huks；  API声明：function getKeyItemProperties(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void;  差异内容：201 | api/@ohos.security.huks.d.ts |
| 新增错误码 | 类名：huks；  API声明：function getKeyItemProperties(keyAlias: string, options: HuksOptions): Promise<HuksReturnResult>;  差异内容：NA | 类名：huks；  API声明：function getKeyItemProperties(keyAlias: string, options: HuksOptions): Promise<HuksReturnResult>;  差异内容：201 | api/@ohos.security.huks.d.ts |
| 新增错误码 | 类名：huks；  API声明：function initSession(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksSessionHandle>): void;  差异内容：NA | 类名：huks；  API声明：function initSession(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksSessionHandle>): void;  差异内容：201 | api/@ohos.security.huks.d.ts |
| 新增错误码 | 类名：huks；  API声明：function initSession(keyAlias: string, options: HuksOptions): Promise<HuksSessionHandle>;  差异内容：NA | 类名：huks；  API声明：function initSession(keyAlias: string, options: HuksOptions): Promise<HuksSessionHandle>;  差异内容：201 | api/@ohos.security.huks.d.ts |
| 新增错误码 | 类名：huks；  API声明：function anonAttestKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void;  差异内容：NA | 类名：huks；  API声明：function anonAttestKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void;  差异内容：201 | api/@ohos.security.huks.d.ts |
| 新增错误码 | 类名：huks；  API声明：function anonAttestKeyItem(keyAlias: string, options: HuksOptions): Promise<HuksReturnResult>;  差异内容：NA | 类名：huks；  API声明：function anonAttestKeyItem(keyAlias: string, options: HuksOptions): Promise<HuksReturnResult>;  差异内容：201 | api/@ohos.security.huks.d.ts |
| 新增错误码 | 类名：huks；  API声明：function wrapKeyItem(keyAlias: string, params: HuksOptions): Promise<HuksReturnResult>;  差异内容：NA | 类名：huks；  API声明：function wrapKeyItem(keyAlias: string, params: HuksOptions): Promise<HuksReturnResult>;  差异内容：201 | api/@ohos.security.huks.d.ts |
| 新增错误码 | 类名：huks；  API声明：function unwrapKeyItem(keyAlias: string, params: HuksOptions, wrappedKey: Uint8Array): Promise<HuksReturnResult>;  差异内容：NA | 类名：huks；  API声明：function unwrapKeyItem(keyAlias: string, params: HuksOptions, wrappedKey: Uint8Array): Promise<HuksReturnResult>;  差异内容：201 | api/@ohos.security.huks.d.ts |
| 权限变更 | 类名：HuksKeySecurityLevel；  API声明：HUKS\_KEY\_SECURITY\_LEVEL\_SE = 1  差异内容：NA | 类名：HuksKeySecurityLevel；  API声明：HUKS\_KEY\_SECURITY\_LEVEL\_SE = 1  差异内容：ohos.permission.ACCESS\_SE\_KEY | api/@ohos.security.huks.d.ts |
