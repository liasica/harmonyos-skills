---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-networkkit-6021
title: Network Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.2(22) > OS平台能力 > API变更清单 > Network Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:47+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:934915b121f997e13ae610e708beaabef45059ace650145026ad78dcf7606037
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：connection；  API声明：function getIpNeighTable(): Promise<Array<NetIpMacInfo>>;  差异内容：function getIpNeighTable(): Promise<Array<NetIpMacInfo>>; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：export interface NetIpMacInfo  差异内容：export interface NetIpMacInfo | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：NetIpMacInfo；  API声明：ipAddress: NetAddress;  差异内容：ipAddress: NetAddress; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：NetIpMacInfo；  API声明：macAddress: string;  差异内容：macAddress: string; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：NetIpMacInfo；  API声明：iface: string;  差异内容：iface: string; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：http；  API声明：export enum InterceptorType  差异内容：export enum InterceptorType | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：InterceptorType；  API声明：INITIAL\_REQUEST = 'INITIAL\_REQUEST'  差异内容：INITIAL\_REQUEST = 'INITIAL\_REQUEST' | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：InterceptorType；  API声明：REDIRECTION = 'REDIRECTION'  差异内容：REDIRECTION = 'REDIRECTION' | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：InterceptorType；  API声明：CACHE\_CHECKED = 'READ\_CACHE'  差异内容：CACHE\_CHECKED = 'READ\_CACHE' | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：InterceptorType；  API声明：NETWORK\_CONNECT = 'CONNECT\_NETWORK'  差异内容：NETWORK\_CONNECT = 'CONNECT\_NETWORK' | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：InterceptorType；  API声明：FINAL\_RESPONSE = 'FINAL\_RESPONSE'  差异内容：FINAL\_RESPONSE = 'FINAL\_RESPONSE' | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http；  API声明：export interface HttpRequestContext  差异内容：export interface HttpRequestContext | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequestContext；  API声明：url: string;  差异内容：url: string; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequestContext；  API声明：header: Object;  差异内容：header: Object; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequestContext；  API声明：body: Object;  差异内容：body: Object; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http；  API声明：export type ChainContinue = boolean;  差异内容：export type ChainContinue = boolean; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http；  API声明：export interface HttpInterceptor  差异内容：export interface HttpInterceptor | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpInterceptor；  API声明：interceptorType: InterceptorType;  差异内容：interceptorType: InterceptorType; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpInterceptor；  API声明：interceptorHandle(reqContext: HttpRequestContext, rspContext: HttpResponse): Promise<ChainContinue>;  差异内容：interceptorHandle(reqContext: HttpRequestContext, rspContext: HttpResponse): Promise<ChainContinue>; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http；  API声明：export class HttpInterceptorChain  差异内容：export class HttpInterceptorChain | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpInterceptorChain；  API声明：public getChain(): HttpInterceptor[];  差异内容：public getChain(): HttpInterceptor[]; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpInterceptorChain；  API声明：public addChain(chain: HttpInterceptor[]): boolean;  差异内容：public addChain(chain: HttpInterceptor[]): boolean; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpInterceptorChain；  API声明：public apply(httpRequest: HttpRequest): boolean;  差异内容：public apply(httpRequest: HttpRequest): boolean; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：policy；  API声明：function showAppNetPolicySettings(context: Context): Promise<void>;  差异内容：function showAppNetPolicySettings(context: Context): Promise<void>; | api/@ohos.net.policy.d.ts |
| 新增API | NA | 类名：TLSConnectOptions；  API声明：timeout?: number;  差异内容：timeout?: number; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：statistics；  API声明：export interface NetStatsInfo  差异内容：export interface NetStatsInfo | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：NetStatsInfo；  API声明：rxBytes: number;  差异内容：rxBytes: number; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：NetStatsInfo；  API声明：txBytes: number;  差异内容：txBytes: number; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：NetStatsInfo；  API声明：rxPackets: number;  差异内容：rxPackets: number; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：NetStatsInfo；  API声明：txPackets: number;  差异内容：txPackets: number; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics；  API声明：export interface NetworkInfo  差异内容：export interface NetworkInfo | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：NetworkInfo；  API声明：type: NetBearType;  差异内容：type: NetBearType; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：NetworkInfo；  API声明：startTime: number;  差异内容：startTime: number; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：NetworkInfo；  API声明：endTime: number;  差异内容：endTime: number; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：NetworkInfo；  API声明：simId?: number;  差异内容：simId?: number; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics；  API声明：function getSelfTrafficStats(networkInfo: NetworkInfo): Promise<NetStatsInfo>;  差异内容：function getSelfTrafficStats(networkInfo: NetworkInfo): Promise<NetStatsInfo>; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：VpnConnection；  API声明：protectProcessNet(): Promise<void>;  差异内容：protectProcessNet(): Promise<void>; | api/@ohos.net.vpnExtension.d.ts |
