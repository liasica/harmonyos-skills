---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-distributedservicekit-6001
title: Distributed Service Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > Distributed Service Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:39+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:b90e4e2e794391f1eacf246191fb43cd91f271ad2b9f0c9c449fea126027fe59
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace linkEnhance  差异内容：declare namespace linkEnhance | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：linkEnhance；  API声明：interface ConnectResult  差异内容：interface ConnectResult | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：ConnectResult；  API声明：deviceId: string;  差异内容：deviceId: string; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：ConnectResult；  API声明：success: boolean;  差异内容：success: boolean; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：ConnectResult；  API声明：reason: number;  差异内容：reason: number; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：linkEnhance；  API声明：interface Server  差异内容：interface Server | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Server；  API声明：start(): void;  差异内容：start(): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Server；  API声明：stop(): void;  差异内容：stop(): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Server；  API声明：close(): void;  差异内容：close(): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Server；  API声明：on(type: 'connectionAccepted', callback: Callback<Connection>): void;  差异内容：on(type: 'connectionAccepted', callback: Callback<Connection>): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Server；  API声明：off(type: 'connectionAccepted', callback?: Callback<Connection>): void;  差异内容：off(type: 'connectionAccepted', callback?: Callback<Connection>): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Server；  API声明：on(type: 'serverStopped', callback: Callback<number>): void;  差异内容：on(type: 'serverStopped', callback: Callback<number>): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Server；  API声明：off(type: 'serverStopped', callback?: Callback<number>): void;  差异内容：off(type: 'serverStopped', callback?: Callback<number>): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：linkEnhance；  API声明：function createServer(name: string): Server;  差异内容：function createServer(name: string): Server; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：linkEnhance；  API声明：interface Connection  差异内容：interface Connection | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Connection；  API声明：connect(): void;  差异内容：connect(): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Connection；  API声明：disconnect(): void;  差异内容：disconnect(): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Connection；  API声明：close(): void;  差异内容：close(): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Connection；  API声明：getPeerDeviceId(): string;  差异内容：getPeerDeviceId(): string; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Connection；  API声明：sendData(data: ArrayBuffer): void;  差异内容：sendData(data: ArrayBuffer): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Connection；  API声明：on(type: 'connectResult', callback: Callback<ConnectResult>): void;  差异内容：on(type: 'connectResult', callback: Callback<ConnectResult>): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Connection；  API声明：off(type: 'connectResult', callback?: Callback<ConnectResult>): void;  差异内容：off(type: 'connectResult', callback?: Callback<ConnectResult>): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Connection；  API声明：on(type: 'disconnected', callback: Callback<number>): void;  差异内容：on(type: 'disconnected', callback: Callback<number>): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Connection；  API声明：off(type: 'disconnected', callback?: Callback<number>): void;  差异内容：off(type: 'disconnected', callback?: Callback<number>): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Connection；  API声明：on(type: 'dataReceived', callback: Callback<ArrayBuffer>): void;  差异内容：on(type: 'dataReceived', callback: Callback<ArrayBuffer>): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Connection；  API声明：off(type: 'dataReceived', callback?: Callback<ArrayBuffer>): void;  差异内容：off(type: 'dataReceived', callback?: Callback<ArrayBuffer>): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：linkEnhance；  API声明：function createConnection(deviceId: string, name: string): Connection;  差异内容：function createConnection(deviceId: string, name: string): Connection; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.distributedsched.linkEnhance.d.ts  差异内容：DistributedServiceKit | api/@ohos.distributedsched.linkEnhance.d.ts |
