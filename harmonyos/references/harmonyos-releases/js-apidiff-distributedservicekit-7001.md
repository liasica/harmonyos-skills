---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-distributedservicekit-7001
title: Distributed Service Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Distributed Service Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:05+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:b4fdddb698a22f655d7125f02b8f5b11bbba0e53ec088fc26d53b267b3970cb1
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：linkEnhance；  API声明：function createServer(name: string): Server;  差异内容：NA | 类名：linkEnhance；  API声明：function createServer(name: string): Server;  差异内容：801 | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增错误码 | 类名：linkEnhance；  API声明：function createConnection(deviceId: string, name: string): Connection;  差异内容：NA | 类名：linkEnhance；  API声明：function createConnection(deviceId: string, name: string): Connection;  差异内容：801 | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增错误码 | 类名：proxyChannelManager；  API声明：function openProxyChannel(channelInfo: ChannelInfo): Promise<number>;  差异内容：NA | 类名：proxyChannelManager；  API声明：function openProxyChannel(channelInfo: ChannelInfo): Promise<number>;  差异内容：801 | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增错误码 | 类名：proxyChannelManager；  API声明：function closeProxyChannel(channelId: number): void;  差异内容：NA | 类名：proxyChannelManager；  API声明：function closeProxyChannel(channelId: number): void;  差异内容：801 | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增错误码 | 类名：proxyChannelManager；  API声明：function sendData(channelId: number, data: ArrayBuffer): Promise<void>;  差异内容：NA | 类名：proxyChannelManager；  API声明：function sendData(channelId: number, data: ArrayBuffer): Promise<void>;  差异内容：801 | api/@ohos.distributedsched.proxyChannelManager.d.ts |
