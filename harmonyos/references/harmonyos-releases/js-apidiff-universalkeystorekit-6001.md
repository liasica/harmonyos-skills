---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-universalkeystorekit-6001
title: Universal Keystore Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > Universal Keystore Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:44+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:4474985d3ef13bc18eff8e75e885c4eaed87272ab7ae745e6397f224afebd23e
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：huks；  API声明：function wrapKeyItem(keyAlias: string, params: HuksOptions): Promise<HuksReturnResult>;  差异内容：function wrapKeyItem(keyAlias: string, params: HuksOptions): Promise<HuksReturnResult>; | api/@ohos.security.huks.d.ts |
| 新增API | NA | 类名：huks；  API声明：function unwrapKeyItem(keyAlias: string, params: HuksOptions, wrappedKey: Uint8Array): Promise<HuksReturnResult>;  差异内容：function unwrapKeyItem(keyAlias: string, params: HuksOptions, wrappedKey: Uint8Array): Promise<HuksReturnResult>; | api/@ohos.security.huks.d.ts |
| 新增API | NA | 类名：HuksExceptionErrCode；  API声明：HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018  差异内容：HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018 | api/@ohos.security.huks.d.ts |
| 新增API | NA | 类名：HuksUserAuthType；  API声明：HUKS\_USER\_AUTH\_TYPE\_TUI\_PIN = 1 << 5  差异内容：HUKS\_USER\_AUTH\_TYPE\_TUI\_PIN = 1 << 5 | api/@ohos.security.huks.d.ts |
| 新增API | NA | 类名：huks；  API声明：export enum HuksKeyWrapType  差异内容：export enum HuksKeyWrapType | api/@ohos.security.huks.d.ts |
| 新增API | NA | 类名：HuksKeyWrapType；  API声明：HUKS\_KEY\_WRAP\_TYPE\_HUK\_BASED = 2  差异内容：HUKS\_KEY\_WRAP\_TYPE\_HUK\_BASED = 2 | api/@ohos.security.huks.d.ts |
