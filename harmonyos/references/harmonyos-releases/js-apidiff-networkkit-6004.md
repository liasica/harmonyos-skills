---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-networkkit-6004
title: Network Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta5引入的API > Network Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:10+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:96549f42e612ec0011ee6c7a5e1b12124dabb0604204871eac7e48b24369f517
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：connection；  API声明：function setPacFileUrl(pacFileUrl: string): void;  差异内容：function setPacFileUrl(pacFileUrl: string): void; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function getPacFileUrl(): string;  差异内容：function getPacFileUrl(): string; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function findProxyForUrl(url: string): string;  差异内容：function findProxyForUrl(url: string): string; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：http；  API声明：export type SslType = 'TLS' | 'TLCP';  差异内容：export type SslType = 'TLS' | 'TLCP'; | api/@ohos.net.http.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：VpnConnection；  API声明：generateVpnId(): Promise<string>;  差异内容：generateVpnId(): Promise<string>; | api/@ohos.net.vpnExtension.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：VpnConfig；  API声明：vpnId?: string;  差异内容：vpnId?: string; | api/@ohos.net.vpnExtension.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：HttpRequestOptions；  API声明：sslType?: SslType;  差异内容：sslType?: SslType; | api/@ohos.net.http.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：HttpRequestOptions；  API声明：clientEncCert?: ClientCert;  差异内容：clientEncCert?: ClientCert; | api/@ohos.net.http.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：VpnConnection；  API声明：destroy(): Promise<void>;  差异内容：destroy(): Promise<void>; | 类名：VpnConnection；  API声明：destroy(vpnId: string): Promise<void>;  差异内容：destroy(vpnId: string): Promise<void>; | api/@ohos.net.vpnExtension.d.ts |
