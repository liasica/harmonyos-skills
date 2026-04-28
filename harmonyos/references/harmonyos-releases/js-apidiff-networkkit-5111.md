---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-networkkit-5111
title: Network Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Beta1引入的API > Network Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:55+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:9d81dcd855c8bf1da7934e8cc79ccaf80399b65869d7508a843dd995827689cf
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API从不支持元服务到支持元服务 | 类名：NetBearType；  API声明：BEARER\_BLUETOOTH = 2  差异内容：NA | 类名：NetBearType；  API声明：BEARER\_BLUETOOTH = 2  差异内容：atomicservice | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：webSocket；  API声明：function createWebSocketServer(): WebSocketServer;  差异内容：function createWebSocketServer(): WebSocketServer; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：webSocket；  API声明：export interface WebSocketServerConfig  差异内容：export interface WebSocketServerConfig | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketServerConfig；  API声明：serverIP?: string;  差异内容：serverIP?: string; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketServerConfig；  API声明：serverPort: number;  差异内容：serverPort: number; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketServerConfig；  API声明：serverCert?: ServerCert;  差异内容：serverCert?: ServerCert; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketServerConfig；  API声明：maxConcurrentClientsNumber: number;  差异内容：maxConcurrentClientsNumber: number; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketServerConfig；  API声明：protocol?: string;  差异内容：protocol?: string; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketServerConfig；  API声明：maxConnectionsForOneClient: number;  差异内容：maxConnectionsForOneClient: number; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：webSocket；  API声明：export interface ServerCert  差异内容：export interface ServerCert | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：ServerCert；  API声明：certPath: string;  差异内容：certPath: string; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：ServerCert；  API声明：keyPath: string;  差异内容：keyPath: string; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：webSocket；  API声明：export interface WebSocketConnection  差异内容：export interface WebSocketConnection | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketConnection；  API声明：clientIP: string;  差异内容：clientIP: string; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketConnection；  API声明：clientPort: number;  差异内容：clientPort: number; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：webSocket；  API声明：export interface WebSocketMessage  差异内容：export interface WebSocketMessage | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketMessage；  API声明：data: string | ArrayBuffer;  差异内容：data: string | ArrayBuffer; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketMessage；  API声明：clientConnection: WebSocketConnection;  差异内容：clientConnection: WebSocketConnection; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：webSocket；  API声明：export type ClientConnectionCloseCallback = (clientConnection: WebSocketConnection, closeReason: CloseResult) => void;  差异内容：export type ClientConnectionCloseCallback = (clientConnection: WebSocketConnection, closeReason: CloseResult) => void; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：webSocket；  API声明：export interface WebSocketServer  差异内容：export interface WebSocketServer | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketServer；  API声明：start(config: WebSocketServerConfig): Promise<boolean>;  差异内容：start(config: WebSocketServerConfig): Promise<boolean>; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketServer；  API声明：listAllConnections(): WebSocketConnection[];  差异内容：listAllConnections(): WebSocketConnection[]; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketServer；  API声明：close(connection: WebSocketConnection, options?: webSocket.WebSocketCloseOptions): Promise<boolean>;  差异内容：close(connection: WebSocketConnection, options?: webSocket.WebSocketCloseOptions): Promise<boolean>; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketServer；  API声明：send(data: string | ArrayBuffer, connection: WebSocketConnection): Promise<boolean>;  差异内容：send(data: string | ArrayBuffer, connection: WebSocketConnection): Promise<boolean>; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketServer；  API声明：stop(): Promise<boolean>;  差异内容：stop(): Promise<boolean>; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketServer；  API声明：on(type: 'error', callback: ErrorCallback): void;  差异内容：on(type: 'error', callback: ErrorCallback): void; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketServer；  API声明：on(type: 'connect', callback: Callback<WebSocketConnection>): void;  差异内容：on(type: 'connect', callback: Callback<WebSocketConnection>): void; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketServer；  API声明：on(type: 'messageReceive', callback: Callback<WebSocketMessage>): void;  差异内容：on(type: 'messageReceive', callback: Callback<WebSocketMessage>): void; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketServer；  API声明：on(type: 'close', callback: ClientConnectionCloseCallback): void;  差异内容：on(type: 'close', callback: ClientConnectionCloseCallback): void; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketServer；  API声明：off(type: 'error', callback?: ErrorCallback): void;  差异内容：off(type: 'error', callback?: ErrorCallback): void; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketServer；  API声明：off(type: 'connect', callback?: Callback<WebSocketConnection>): void;  差异内容：off(type: 'connect', callback?: Callback<WebSocketConnection>): void; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketServer；  API声明：off(type: 'close', callback?: ClientConnectionCloseCallback): void;  差异内容：off(type: 'close', callback?: ClientConnectionCloseCallback): void; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketServer；  API声明：off(type: 'messageReceive', callback?: Callback<WebSocketMessage>): void;  差异内容：off(type: 'messageReceive', callback?: Callback<WebSocketMessage>): void; | api/@ohos.net.webSocket.d.ts |
