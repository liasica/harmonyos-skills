---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-networkkit-7002
title: Network Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Network Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:4fef76e32db0b44f139ee2839d409375747cd59b58c35d1443146ece5c4c91a7
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：HttpRequest；  API声明：request(url: string, callback: AsyncCallback<HttpResponse>): void;  差异内容：NA | 类名：HttpRequest；  API声明：request(url: string, callback: AsyncCallback<HttpResponse>): void;  差异内容：2300996 | api/@ohos.net.http.d.ts |
| 新增错误码 | 类名：HttpRequest；  API声明：request(url: string, options: HttpRequestOptions, callback: AsyncCallback<HttpResponse>): void;  差异内容：NA | 类名：HttpRequest；  API声明：request(url: string, options: HttpRequestOptions, callback: AsyncCallback<HttpResponse>): void;  差异内容：2300996 | api/@ohos.net.http.d.ts |
| 新增错误码 | 类名：HttpRequest；  API声明：request(url: string, options?: HttpRequestOptions): Promise<HttpResponse>;  差异内容：NA | 类名：HttpRequest；  API声明：request(url: string, options?: HttpRequestOptions): Promise<HttpResponse>;  差异内容：2300996 | api/@ohos.net.http.d.ts |
| 新增错误码 | 类名：HttpRequest；  API声明：requestSync(url: string, options?: HttpRequestOptions): HttpResponse;  差异内容：NA | 类名：HttpRequest；  API声明：requestSync(url: string, options?: HttpRequestOptions): HttpResponse;  差异内容：2300996 | api/@ohos.net.http.d.ts |
| 新增错误码 | 类名：HttpRequest；  API声明：requestInStream(url: string, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：HttpRequest；  API声明：requestInStream(url: string, callback: AsyncCallback<number>): void;  差异内容：2300996 | api/@ohos.net.http.d.ts |
| 新增错误码 | 类名：HttpRequest；  API声明：requestInStream(url: string, options: HttpRequestOptions, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：HttpRequest；  API声明：requestInStream(url: string, options: HttpRequestOptions, callback: AsyncCallback<number>): void;  差异内容：2300996 | api/@ohos.net.http.d.ts |
| 新增错误码 | 类名：HttpRequest；  API声明：requestInStream(url: string, options?: HttpRequestOptions): Promise<number>;  差异内容：NA | 类名：HttpRequest；  API声明：requestInStream(url: string, options?: HttpRequestOptions): Promise<number>;  差异内容：2300996 | api/@ohos.net.http.d.ts |
| 新增错误码 | 类名：statistics；  API声明：function getUidRxBytes(uid: number, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：statistics；  API声明：function getUidRxBytes(uid: number, callback: AsyncCallback<number>): void;  差异内容：201 | api/@ohos.net.statistics.d.ts |
| 新增错误码 | 类名：statistics；  API声明：function getUidRxBytes(uid: number): Promise<number>;  差异内容：NA | 类名：statistics；  API声明：function getUidRxBytes(uid: number): Promise<number>;  差异内容：201 | api/@ohos.net.statistics.d.ts |
| 新增错误码 | 类名：statistics；  API声明：function getUidTxBytes(uid: number, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：statistics；  API声明：function getUidTxBytes(uid: number, callback: AsyncCallback<number>): void;  差异内容：201 | api/@ohos.net.statistics.d.ts |
| 新增错误码 | 类名：statistics；  API声明：function getUidTxBytes(uid: number): Promise<number>;  差异内容：NA | 类名：statistics；  API声明：function getUidTxBytes(uid: number): Promise<number>;  差异内容：201 | api/@ohos.net.statistics.d.ts |
| 权限变更 | 类名：statistics；  API声明：function getUidRxBytes(uid: number, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：statistics；  API声明：function getUidRxBytes(uid: number, callback: AsyncCallback<number>): void;  差异内容：ohos.permission.GET\_NETWORK\_STATS | api/@ohos.net.statistics.d.ts |
| 权限变更 | 类名：statistics；  API声明：function getUidRxBytes(uid: number): Promise<number>;  差异内容：NA | 类名：statistics；  API声明：function getUidRxBytes(uid: number): Promise<number>;  差异内容：ohos.permission.GET\_NETWORK\_STATS | api/@ohos.net.statistics.d.ts |
| 权限变更 | 类名：statistics；  API声明：function getUidTxBytes(uid: number, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：statistics；  API声明：function getUidTxBytes(uid: number, callback: AsyncCallback<number>): void;  差异内容：ohos.permission.GET\_NETWORK\_STATS | api/@ohos.net.statistics.d.ts |
| 权限变更 | 类名：statistics；  API声明：function getUidTxBytes(uid: number): Promise<number>;  差异内容：NA | 类名：statistics；  API声明：function getUidTxBytes(uid: number): Promise<number>;  差异内容：ohos.permission.GET\_NETWORK\_STATS | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：http；  API声明：export type X509Cert = cert.X509Cert;  差异内容：export type X509Cert = cert.X509Cert; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http；  API声明：export interface ValidationContext  差异内容：export interface ValidationContext | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ValidationContext；  API声明：pemCerts: string[];  差异内容：pemCerts: string[]; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ValidationContext；  API声明：x509Certs: X509Cert[];  差异内容：x509Certs: X509Cert[]; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ValidationContext；  API声明：host: string;  差异内容：host: string; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ValidationContext；  API声明：ip: string;  差异内容：ip: string; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http；  API声明：export type ValidationCallback = (context: ValidationContext) => boolean | Promise<boolean>;  差异内容：export type ValidationCallback = (context: ValidationContext) => boolean | Promise<boolean>; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：connection；  API声明：function refreshGlobalHttpProxy(): Promise<HttpProxy>;  差异内容：function refreshGlobalHttpProxy(): Promise<HttpProxy>; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：NetFirewallRule；  API声明：interface?: string;  差异内容：interface?: string; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：networkSecurity；  API声明：export function verifyCertChain(cert: CertBlob[], caCert?: CertBlob, hostname?: string): Promise<CertBlob[]>;  差异内容：export function verifyCertChain(cert: CertBlob[], caCert?: CertBlob, hostname?: string): Promise<CertBlob[]>; | api/@ohos.net.networkSecurity.d.ts |
| 新增API | NA | 类名：WebSocketRequestOptions；  API声明：supportOriginPort?: boolean;  差异内容：supportOriginPort?: boolean; | api/@ohos.net.webSocket.d.ts |
