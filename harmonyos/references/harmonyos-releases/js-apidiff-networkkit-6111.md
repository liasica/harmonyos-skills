---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-networkkit-6111
title: Network Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > Network Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:08+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:7dcf24f78d129b404f3a334b174bdc40bf717b0b6bd359ea349dbe1d72b92cb2
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：WebSocketServer；  API声明：start(config: WebSocketServerConfig): Promise<boolean>;  差异内容：NA | 类名：WebSocketServer；  API声明：start(config: WebSocketServerConfig): Promise<boolean>;  差异内容：2302007 | api/@ohos.net.webSocket.d.ts |
| 属性变更 | 类名：TLSSecureOptions；  API声明：cert?: string;  差异内容：string | 类名：TLSSecureOptions；  API声明：cert?: string | Array<string>;  差异内容：string,Array<string> | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：connection；  API声明：function getSystemNetPortStates(): Promise<NetPortStatesInfo>;  差异内容：function getSystemNetPortStates(): Promise<NetPortStatesInfo>; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：export interface NetPortStatesInfo  差异内容：export interface NetPortStatesInfo | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：NetPortStatesInfo；  API声明：tcpPortStatesInfo?: Array<TcpNetPortStatesInfo>;  差异内容：tcpPortStatesInfo?: Array<TcpNetPortStatesInfo>; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：NetPortStatesInfo；  API声明：udpPortStatesInfo?: Array<UdpNetPortStatesInfo>;  差异内容：udpPortStatesInfo?: Array<UdpNetPortStatesInfo>; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：export interface TcpNetPortStatesInfo  差异内容：export interface TcpNetPortStatesInfo | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TcpNetPortStatesInfo；  API声明：tcpLocalIp: string;  差异内容：tcpLocalIp: string; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TcpNetPortStatesInfo；  API声明：tcpLocalPort: number;  差异内容：tcpLocalPort: number; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TcpNetPortStatesInfo；  API声明：tcpRemoteIp: string;  差异内容：tcpRemoteIp: string; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TcpNetPortStatesInfo；  API声明：tcpRemotePort: number;  差异内容：tcpRemotePort: number; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TcpNetPortStatesInfo；  API声明：tcpUid: number;  差异内容：tcpUid: number; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TcpNetPortStatesInfo；  API声明：tcpPid: number;  差异内容：tcpPid: number; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TcpNetPortStatesInfo；  API声明：tcpState: TcpState;  差异内容：tcpState: TcpState; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：export interface UdpNetPortStatesInfo  差异内容：export interface UdpNetPortStatesInfo | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：UdpNetPortStatesInfo；  API声明：udpLocalIp: string;  差异内容：udpLocalIp: string; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：UdpNetPortStatesInfo；  API声明：udpLocalPort: number;  差异内容：udpLocalPort: number; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：UdpNetPortStatesInfo；  API声明：udpUid: number;  差异内容：udpUid: number; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：UdpNetPortStatesInfo；  API声明：udpPid: number;  差异内容：udpPid: number; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：export enum TcpState  差异内容：export enum TcpState | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TcpState；  API声明：TCP\_ESTABLISHED = 1  差异内容：TCP\_ESTABLISHED = 1 | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TcpState；  API声明：TCP\_SYN\_SENT = 2  差异内容：TCP\_SYN\_SENT = 2 | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TcpState；  API声明：TCP\_SYN\_RECV = 3  差异内容：TCP\_SYN\_RECV = 3 | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TcpState；  API声明：TCP\_FIN\_WAIT1 = 4  差异内容：TCP\_FIN\_WAIT1 = 4 | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TcpState；  API声明：TCP\_FIN\_WAIT2 = 5  差异内容：TCP\_FIN\_WAIT2 = 5 | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TcpState；  API声明：TCP\_TIME\_WAIT = 6  差异内容：TCP\_TIME\_WAIT = 6 | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TcpState；  API声明：TCP\_CLOSE = 7  差异内容：TCP\_CLOSE = 7 | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TcpState；  API声明：TCP\_CLOSE\_WAIT = 8  差异内容：TCP\_CLOSE\_WAIT = 8 | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TcpState；  API声明：TCP\_LAST\_ACK = 9  差异内容：TCP\_LAST\_ACK = 9 | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TcpState；  API声明：TCP\_LISTEN = 10  差异内容：TCP\_LISTEN = 10 | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TcpState；  API声明：TCP\_CLOSING = 11  差异内容：TCP\_CLOSING = 11 | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：ConnectionProperties；  API声明：isIPv4LinkValid?: boolean;  差异内容：isIPv4LinkValid?: boolean; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：ConnectionProperties；  API声明：isIPv6LinkValid?: boolean;  差异内容：isIPv6LinkValid?: boolean; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TCPExtraOptions；  API声明：tcpFastOpen?: boolean;  差异内容：tcpFastOpen?: boolean; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：HttpResponse；  API声明：connectionExtraInfo?: ConnectionExtraInfo;  差异内容：connectionExtraInfo?: ConnectionExtraInfo; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http；  API声明：export interface ConnectionExtraInfo  差异内容：export interface ConnectionExtraInfo | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ConnectionExtraInfo；  API声明：networkProtocolName: string;  差异内容：networkProtocolName: string; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ConnectionExtraInfo；  API声明：tlsVersion?: TlsVersion;  差异内容：tlsVersion?: TlsVersion; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ConnectionExtraInfo；  API声明：cipherSuite?: CipherSuite;  差异内容：cipherSuite?: CipherSuite; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ConnectionExtraInfo；  API声明：localAddress: string;  差异内容：localAddress: string; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ConnectionExtraInfo；  API声明：remoteAddress: string;  差异内容：remoteAddress: string; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ConnectionExtraInfo；  API声明：localPort: number;  差异内容：localPort: number; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ConnectionExtraInfo；  API声明：remotePort: number;  差异内容：remotePort: number; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ConnectionExtraInfo；  API声明：isReusedConnection: boolean;  差异内容：isReusedConnection: boolean; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ConnectionExtraInfo；  API声明：isProxyConnection: boolean;  差异内容：isProxyConnection: boolean; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ConnectionExtraInfo；  API声明：isCacheHit: boolean;  差异内容：isCacheHit: boolean; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ConnectionExtraInfo；  API声明：redirectCount: number;  差异内容：redirectCount: number; | api/@ohos.net.http.d.ts |
