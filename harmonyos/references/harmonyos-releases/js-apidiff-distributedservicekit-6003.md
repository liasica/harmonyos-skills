---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-distributedservicekit-6003
title: Distributed Service Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > Distributed Service Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:17+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:b47ad497932d89d8c337b3647a328281c83c0a0f708fac48a266a95489cedad9
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace proxyChannelManager  差异内容：declare namespace proxyChannelManager | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：proxyChannelManager；  API声明：function openProxyChannel(channelInfo: ChannelInfo): Promise<number>;  差异内容：function openProxyChannel(channelInfo: ChannelInfo): Promise<number>; | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：proxyChannelManager；  API声明：function closeProxyChannel(channelId: number): void;  差异内容：function closeProxyChannel(channelId: number): void; | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：proxyChannelManager；  API声明：function sendData(channelId: number, data: ArrayBuffer): Promise<void>;  差异内容：function sendData(channelId: number, data: ArrayBuffer): Promise<void>; | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：proxyChannelManager；  API声明：function on(type: 'receiveData', channelId: number, callback: Callback<DataInfo>): void;  差异内容：function on(type: 'receiveData', channelId: number, callback: Callback<DataInfo>): void; | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：proxyChannelManager；  API声明：function off(type: 'receiveData', channelId: number, callback?: Callback<DataInfo>): void;  差异内容：function off(type: 'receiveData', channelId: number, callback?: Callback<DataInfo>): void; | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：proxyChannelManager；  API声明：function on(type: 'channelStateChange', channelId: number, callback: Callback<ChannelStateInfo>): void;  差异内容：function on(type: 'channelStateChange', channelId: number, callback: Callback<ChannelStateInfo>): void; | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：proxyChannelManager；  API声明：function off(type: 'channelStateChange', channelId: number, callback?: Callback<ChannelStateInfo>): void;  差异内容：function off(type: 'channelStateChange', channelId: number, callback?: Callback<ChannelStateInfo>): void; | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：proxyChannelManager；  API声明：interface DataInfo  差异内容：interface DataInfo | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：DataInfo；  API声明：channelId: number;  差异内容：channelId: number; | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：DataInfo；  API声明：data: ArrayBuffer;  差异内容：data: ArrayBuffer; | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：proxyChannelManager；  API声明：enum LinkType  差异内容：enum LinkType | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：LinkType；  API声明：LINK\_BR = 0  差异内容：LINK\_BR = 0 | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：proxyChannelManager；  API声明：interface ChannelInfo  差异内容：interface ChannelInfo | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：ChannelInfo；  API声明：linkType: LinkType;  差异内容：linkType: LinkType; | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：ChannelInfo；  API声明：peerDevAddr: string;  差异内容：peerDevAddr: string; | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：ChannelInfo；  API声明：peerUuid: string;  差异内容：peerUuid: string; | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：proxyChannelManager；  API声明：enum ChannelState  差异内容：enum ChannelState | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：ChannelState；  API声明：CHANNEL\_WAIT\_RESUME = 0  差异内容：CHANNEL\_WAIT\_RESUME = 0 | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：ChannelState；  API声明：CHANNEL\_RESUME = 1  差异内容：CHANNEL\_RESUME = 1 | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：ChannelState；  API声明：CHANNEL\_EXCEPTION\_SOFTWARE\_FAILED = 2  差异内容：CHANNEL\_EXCEPTION\_SOFTWARE\_FAILED = 2 | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：ChannelState；  API声明：CHANNEL\_BR\_NO\_PAIRED = 3  差异内容：CHANNEL\_BR\_NO\_PAIRED = 3 | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：proxyChannelManager；  API声明：interface ChannelStateInfo  差异内容：interface ChannelStateInfo | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：ChannelStateInfo；  API声明：channelId: number;  差异内容：channelId: number; | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增API | NA | 类名：ChannelStateInfo；  API声明：state: ChannelState;  差异内容：state: ChannelState; | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.distributedsched.proxyChannelManager.d.ts  差异内容：DistributedServiceKit | api/@ohos.distributedsched.proxyChannelManager.d.ts |
