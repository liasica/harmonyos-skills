---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-distributedservicekit-6112
title: Distributed Service Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Release引入的API > Distributed Service Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:213ad5a2248a9becc592ef1e3b954b8d1b49fc227d1aab21421d66049c0e094a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：proxyChannelManager；  API声明：function openProxyChannel(channelInfo: ChannelInfo): Promise<number>;  差异内容：801 | 类名：proxyChannelManager；  API声明：function openProxyChannel(channelInfo: ChannelInfo): Promise<number>;  差异内容：NA | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 删除错误码 | 类名：proxyChannelManager；  API声明：function closeProxyChannel(channelId: number): void;  差异内容：801 | 类名：proxyChannelManager；  API声明：function closeProxyChannel(channelId: number): void;  差异内容：NA | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 删除错误码 | 类名：proxyChannelManager；  API声明：function sendData(channelId: number, data: ArrayBuffer): Promise<void>;  差异内容：801 | 类名：proxyChannelManager；  API声明：function sendData(channelId: number, data: ArrayBuffer): Promise<void>;  差异内容：NA | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 删除错误码 | 类名：proxyChannelManager；  API声明：function on(type: 'receiveData', channelId: number, callback: Callback<DataInfo>): void;  差异内容：801 | 类名：proxyChannelManager；  API声明：function on(type: 'receiveData', channelId: number, callback: Callback<DataInfo>): void;  差异内容：NA | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 删除错误码 | 类名：proxyChannelManager；  API声明：function off(type: 'receiveData', channelId: number, callback?: Callback<DataInfo>): void;  差异内容：801 | 类名：proxyChannelManager；  API声明：function off(type: 'receiveData', channelId: number, callback?: Callback<DataInfo>): void;  差异内容：NA | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 删除错误码 | 类名：proxyChannelManager；  API声明：function on(type: 'channelStateChange', channelId: number, callback: Callback<ChannelStateInfo>): void;  差异内容：801 | 类名：proxyChannelManager；  API声明：function on(type: 'channelStateChange', channelId: number, callback: Callback<ChannelStateInfo>): void;  差异内容：NA | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 删除错误码 | 类名：proxyChannelManager；  API声明：function off(type: 'channelStateChange', channelId: number, callback?: Callback<ChannelStateInfo>): void;  差异内容：801 | 类名：proxyChannelManager；  API声明：function off(type: 'channelStateChange', channelId: number, callback?: Callback<ChannelStateInfo>): void;  差异内容：NA | api/@ohos.distributedsched.proxyChannelManager.d.ts |
