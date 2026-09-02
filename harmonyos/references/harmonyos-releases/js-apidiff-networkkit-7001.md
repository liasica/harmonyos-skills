---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-networkkit-7001
title: Network Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Network Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:06+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:241a335c76ebc0c4d13cbff9990c6d708027370b8705d12ac74a469080df68be
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：connection；  API声明：function queryTraceRoute(destination: string, option?: TraceRouteOptions): Promise<TraceRouteInfo[]>;  差异内容：function queryTraceRoute(destination: string, option?: TraceRouteOptions): Promise<TraceRouteInfo[]>; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function queryProbeResult(destination: string, duration: number): Promise<ProbeResultInfo>;  差异内容：function queryProbeResult(destination: string, duration: number): Promise<ProbeResultInfo>; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：export enum Socks5DnsStrategy  差异内容：export enum Socks5DnsStrategy | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：Socks5DnsStrategy；  API声明：SYSTEM\_MODE = 0  差异内容：SYSTEM\_MODE = 0 | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：Socks5DnsStrategy；  API声明：PROXY\_MODE = 1  差异内容：PROXY\_MODE = 1 | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：export interface Socks5Proxy  差异内容：export interface Socks5Proxy | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：Socks5Proxy；  API声明：host: string;  差异内容：host: string; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：Socks5Proxy；  API声明：port: number;  差异内容：port: number; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：Socks5Proxy；  API声明：username?: string;  差异内容：username?: string; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：Socks5Proxy；  API声明：password?: string;  差异内容：password?: string; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：Socks5Proxy；  API声明：dnsStrategy?: Socks5DnsStrategy;  差异内容：dnsStrategy?: Socks5DnsStrategy; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：Socks5Proxy；  API声明：exclusionList?: Array<string>;  差异内容：exclusionList?: Array<string>; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：export enum PacketsType  差异内容：export enum PacketsType | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：PacketsType；  API声明：NETCONN\_PACKETS\_ICMP = 0  差异内容：NETCONN\_PACKETS\_ICMP = 0 | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：PacketsType；  API声明：NETCONN\_PACKETS\_UDP = 1  差异内容：NETCONN\_PACKETS\_UDP = 1 | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：export interface TraceRouteOptions  差异内容：export interface TraceRouteOptions | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TraceRouteOptions；  API声明：maxJumpNumber?: number;  差异内容：maxJumpNumber?: number; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TraceRouteOptions；  API声明：packetsType?: PacketsType;  差异内容：packetsType?: PacketsType; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：export interface TraceRouteInfo  差异内容：export interface TraceRouteInfo | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TraceRouteInfo；  API声明：jumpNo: number;  差异内容：jumpNo: number; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TraceRouteInfo；  API声明：address: string;  差异内容：address: string; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TraceRouteInfo；  API声明：rtt: number[];  差异内容：rtt: number[]; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：export interface ProbeResultInfo  差异内容：export interface ProbeResultInfo | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：ProbeResultInfo；  API声明：lossRate: number;  差异内容：lossRate: number; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：ProbeResultInfo；  API声明：rtt: number[];  差异内容：rtt: number[]; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：http；  API声明：type Socks5Proxy = connection.Socks5Proxy;  差异内容：type Socks5Proxy = connection.Socks5Proxy; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http；  API声明：export type QueryParamValue = string | number | boolean | null | undefined;  差异内容：export type QueryParamValue = string | number | boolean | null | undefined; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http；  API声明：export type QueryParamObject = Record<string, QueryParamValue | QueryParamValue[]>;  差异内容：export type QueryParamObject = Record<string, QueryParamValue | QueryParamValue[]>; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequestOptions；  API声明：body?: string | Object | ArrayBuffer;  差异内容：body?: string | Object | ArrayBuffer; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequestOptions；  API声明：queryParams?: string | QueryParamObject;  差异内容：queryParams?: string | QueryParamObject; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequestOptions；  API声明：enablePartialChain?: boolean;  差异内容：enablePartialChain?: boolean; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequestOptions；  API声明：reuseConnections?: boolean;  差异内容：reuseConnections?: boolean; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequestOptions；  API声明：inactivityMs?: number;  差异内容：inactivityMs?: number; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequestOptions；  API声明：usingSocks5Proxy?: Socks5Proxy;  差异内容：usingSocks5Proxy?: Socks5Proxy; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequest；  API声明：requestSync(url: string, options?: HttpRequestOptions): HttpResponse;  差异内容：requestSync(url: string, options?: HttpRequestOptions): HttpResponse; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequest；  API声明：enableAutoCookie(enable: boolean): void;  差异内容：enableAutoCookie(enable: boolean): void; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：RequestMethod；  API声明：PATCH = "PATCH"  差异内容：PATCH = "PATCH" | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：policy；  API声明：function getNetAccessPolicy(): Promise<NetAccessPolicy>;  差异内容：function getNetAccessPolicy(): Promise<NetAccessPolicy>; | api/@ohos.net.policy.d.ts |
| 新增API | NA | 类名：policy；  API声明：export interface NetAccessPolicy  差异内容：export interface NetAccessPolicy | api/@ohos.net.policy.d.ts |
| 新增API | NA | 类名：NetAccessPolicy；  API声明：allowWiFi: boolean;  差异内容：allowWiFi: boolean; | api/@ohos.net.policy.d.ts |
| 新增API | NA | 类名：NetAccessPolicy；  API声明：allowCellular: boolean;  差异内容：allowCellular: boolean; | api/@ohos.net.policy.d.ts |
| 新增API | NA | 类名：MulticastSocket；  API声明：setReuseAddress(reuse: boolean): void;  差异内容：setReuseAddress(reuse: boolean): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：vpnExtension；  API声明：function createVpnObserver(): VpnObserver;  差异内容：function createVpnObserver(): VpnObserver; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：vpnExtension；  API声明：export interface VpnObserver  差异内容：export interface VpnObserver | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：VpnObserver；  API声明：onAuthorizationResult(callback: Callback<boolean>): void;  差异内容：onAuthorizationResult(callback: Callback<boolean>): void; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：VpnObserver；  API声明：offAuthorizationResult(callback?: Callback<boolean>): void;  差异内容：offAuthorizationResult(callback?: Callback<boolean>): void; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：WebSocketRequestOptions；  API声明：minSupportTlsProtocol?: TlsProtocol;  差异内容：minSupportTlsProtocol?: TlsProtocol; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：webSocket；  API声明：export enum TlsProtocol  差异内容：export enum TlsProtocol | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：TlsProtocol；  API声明：TLS\_V\_1\_0 = 0  差异内容：TLS\_V\_1\_0 = 0 | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：TlsProtocol；  API声明：TLS\_V\_1\_1 = 1  差异内容：TLS\_V\_1\_1 = 1 | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：TlsProtocol；  API声明：TLS\_V\_1\_2 = 2  差异内容：TLS\_V\_1\_2 = 2 | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：TlsProtocol；  API声明：TLS\_V\_1\_3 = 3  差异内容：TLS\_V\_1\_3 = 3 | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：webSocket；  API声明：export interface WebSocketOpenInfo  差异内容：export interface WebSocketOpenInfo | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketOpenInfo；  API声明：status: number;  差异内容：status: number; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketOpenInfo；  API声明：message: string;  差异内容：message: string; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketOpenInfo；  API声明：protocol?: string;  差异内容：protocol?: string; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocket；  API声明：on(type: 'openInfo', callback: AsyncCallback<WebSocketOpenInfo>): void;  差异内容：on(type: 'openInfo', callback: AsyncCallback<WebSocketOpenInfo>): void; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocket；  API声明：off(type: 'openInfo', callback?: AsyncCallback<WebSocketOpenInfo>): void;  差异内容：off(type: 'openInfo', callback?: AsyncCallback<WebSocketOpenInfo>): void; | api/@ohos.net.webSocket.d.ts |
