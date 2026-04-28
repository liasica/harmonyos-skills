---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-b105
title: Connectivity Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.1(13) > OS平台能力 > API变更清单 > HarmonyOS 5.0.1(13) Beta3引入的API > Connectivity Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:03+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:1d516e9171e899ff93dbc00ee2d83d18ec236516eb022c0a77dda136887257df
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：wifiManager；  API声明：function isWifiActive(): boolean;  差异内容：201,2501000,801 | 类名：wifiManager；  API声明：function isWifiActive(): boolean;  差异内容：2501000,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager；  API声明：function removeCandidateConfig(networkId: number): Promise<void>;  差异内容：201,2501000,401,801 | 类名：wifiManager；  API声明：function removeCandidateConfig(networkId: number): Promise<void>;  差异内容：201,2501000,2501001,401,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager；  API声明：function removeCandidateConfig(networkId: number, callback: AsyncCallback<void>): void;  差异内容：201,2501000,401,801 | 类名：wifiManager；  API声明：function removeCandidateConfig(networkId: number, callback: AsyncCallback<void>): void;  差异内容：201,2501000,2501001,401,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager；  API声明：function isMeteredHotspot(): boolean;  差异内容：201,2501000,801 | 类名：wifiManager；  API声明：function isMeteredHotspot(): boolean;  差异内容：201,2501000,2501001,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager；  API声明：function getP2pLinkedInfo(callback: AsyncCallback<WifiP2pLinkedInfo>): void;  差异内容：201,2801000,801 | 类名：wifiManager；  API声明：function getP2pLinkedInfo(callback: AsyncCallback<WifiP2pLinkedInfo>): void;  差异内容：201,2801000,2801001,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager；  API声明：function getP2pPeerDevices(callback: AsyncCallback<WifiP2pDevice[]>): void;  差异内容：201,2801000,801 | 类名：wifiManager；  API声明：function getP2pPeerDevices(callback: AsyncCallback<WifiP2pDevice[]>): void;  差异内容：201,2801000,2801001,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager；  API声明：function getP2pLocalDevice(callback: AsyncCallback<WifiP2pDevice>): void;  差异内容：201,2801000,801 | 类名：wifiManager；  API声明：function getP2pLocalDevice(callback: AsyncCallback<WifiP2pDevice>): void;  差异内容：201,2801000,2801001,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager；  API声明：function createGroup(config: WifiP2PConfig): void;  差异内容：201,2801000,401,801 | 类名：wifiManager；  API声明：function createGroup(config: WifiP2PConfig): void;  差异内容：201,2801000,2801001,401,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager；  API声明：function removeGroup(): void;  差异内容：201,2801000,801 | 类名：wifiManager；  API声明：function removeGroup(): void;  差异内容：201,2801000,2801001,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager；  API声明：function p2pConnect(config: WifiP2PConfig): void;  差异内容：201,2801000,401,801 | 类名：wifiManager；  API声明：function p2pConnect(config: WifiP2PConfig): void;  差异内容：201,2801000,2801001,401,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager；  API声明：function p2pCancelConnect(): void;  差异内容：201,2801000,801 | 类名：wifiManager；  API声明：function p2pCancelConnect(): void;  差异内容：201,2801000,2801001,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager；  API声明：function startDiscoverDevices(): void;  差异内容：201,2801000,801 | 类名：wifiManager；  API声明：function startDiscoverDevices(): void;  差异内容：201,2801000,2801001,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager；  API声明：function stopDiscoverDevices(): void;  差异内容：201,2801000,801 | 类名：wifiManager；  API声明：function stopDiscoverDevices(): void;  差异内容：201,2801000,2801001,801 | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：wifiManager；  API声明：function isWifiActive(): boolean;  差异内容：ohos.permission.GET\_WIFI\_INFO | 类名：wifiManager；  API声明：function isWifiActive(): boolean;  差异内容：NA | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：CodecType；  API声明：CODEC\_TYPE\_L2HCST = 3  差异内容：CODEC\_TYPE\_L2HCST = 3 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecType；  API声明：CODEC\_TYPE\_LDAC = 4  差异内容：CODEC\_TYPE\_LDAC = 4 | api/@ohos.bluetooth.a2dp.d.ts |
