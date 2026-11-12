---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-networkkit-26011
title: Network Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > Network Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:54+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:6005bdb81e018ec2dc94822ac47482823ab5229c10c5e4dded72692c354d7473
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：VpnConnection；  API声明：create(config: VpnConfig): Promise<number>;  差异内容：NA | 类名：VpnConnection；  API声明：create(config: VpnConfig): Promise<number>;  差异内容：201 | api/@ohos.net.vpnExtension.d.ts |
| 权限变更 | 类名：VpnConnection；  API声明：create(config: VpnConfig): Promise<number>;  差异内容：NA | 类名：VpnConnection；  API声明：create(config: VpnConfig): Promise<number>;  差异内容：ohos.permission.INTERNET | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：eap；  API声明：interface EthEapConfig  差异内容：interface EthEapConfig | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapConfig；  API声明：profile: EthEapProfile;  差异内容：profile: EthEapProfile; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapConfig；  API声明：enabled: boolean;  差异内容：enabled: boolean; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapConfig；  API声明：autoAuth: boolean;  差异内容：autoAuth: boolean; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapConfig；  API声明：locked: boolean;  差异内容：locked: boolean; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap；  API声明：enum EthEapState  差异内容：enum EthEapState | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapState；  API声明：STATE\_IDLE = 0  差异内容：STATE\_IDLE = 0 | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapState；  API声明：STATE\_AUTHENTICATING = 1  差异内容：STATE\_AUTHENTICATING = 1 | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapState；  API声明：STATE\_AUTHENTICATED = 2  差异内容：STATE\_AUTHENTICATED = 2 | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapState；  API声明：STATE\_FAILED = 3  差异内容：STATE\_FAILED = 3 | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapState；  API声明：STATE\_RETRYING = 4  差异内容：STATE\_RETRYING = 4 | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap；  API声明：interface EthEapStateInfo  差异内容：interface EthEapStateInfo | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapStateInfo；  API声明：state: EthEapState;  差异内容：state: EthEapState; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapStateInfo；  API声明：retryCount: number;  差异内容：retryCount: number; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapStateInfo；  API声明：message?: string;  差异内容：message?: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap；  API声明：function setEthEapConfig(config: EthEapConfig): void;  差异内容：function setEthEapConfig(config: EthEapConfig): void; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap；  API声明：function getEthEapConfig(): Promise<EthEapConfig>;  差异内容：function getEthEapConfig(): Promise<EthEapConfig>; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap；  API声明：function deleteEthEapConfig(): Promise<void>;  差异内容：function deleteEthEapConfig(): Promise<void>; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap；  API声明：function getEthEapStateInfo(): EthEapStateInfo;  差异内容：function getEthEapStateInfo(): EthEapStateInfo; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap；  API声明：function onStateChange(callback: Callback<EthEapStateInfo>): void;  差异内容：function onStateChange(callback: Callback<EthEapStateInfo>): void; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap；  API声明：function offStateChange(callback?: Callback<EthEapStateInfo>): void;  差异内容：function offStateChange(callback?: Callback<EthEapStateInfo>): void; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap；  API声明：enum EthEapConnectAction  差异内容：enum EthEapConnectAction | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapConnectAction；  API声明：ACTION\_CONNECT = 0  差异内容：ACTION\_CONNECT = 0 | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapConnectAction；  API声明：ACTION\_DISCONNECT = 1  差异内容：ACTION\_DISCONNECT = 1 | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap；  API声明：function connect(action: EthEapConnectAction): Promise<void>;  差异内容：function connect(action: EthEapConnectAction): Promise<void>; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：socket；  API声明：export type NetAddress = connection.NetAddress;  差异内容：export type NetAddress = connection.NetAddress; | api/@ohos.net.socket.d.ts |
