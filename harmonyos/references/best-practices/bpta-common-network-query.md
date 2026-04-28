---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-common-network-query
title: 网络信息查询与连接管理
breadcrumb: 最佳实践 > 网络 > 网络信息查询与连接管理
category: best-practices
scraped_at: 2026-04-28T08:20:21+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:52c9299e0dd07aef0416866557b9f8ec3542e10a3de182646c1fdc3ef3926bc8
---

## 概述

[Network Kit](../harmonyos-references/network-api.md)提供常用的网络信息查询与连接管理功能，包括获取网络类型、检查网络可用性、监听网络状态变化、查询Wi-Fi及蜂窝网络信息等。这些能力帮助开发者灵活应对复杂多变的网络环境，精准实现各类场景需求，显著提升用户的网络使用体验。

## 连接到指定网络场景

### 场景描述

在特定业务场景中（如企业或校园内网），应用必须通过指定的网络连接到专用服务器以获取关键数据。若连接指定网络失败，将直接导致网络配置中断、身份认证受阻或核心资源无法访问，从而中断业务流程。

本章将通过以下示例，介绍如何连接到指定的Wi-Fi。该示例具备以下功能：

* 判断设备是否已连接到指定的Wi-Fi
* 获取系统扫描的Wi-Fi列表
* 通过点击Wi-Fi列表连接到相应的Wi-Fi

**图1** 连接到指定网络效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/cnqAswEqQr6YYny_bsht5Q/zh-cn_image_0000002408087960.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002018Z&HW-CC-Expire=86400&HW-CC-Sign=1FC532B8B59BDCC1ED0CECF5DD05431630ED8BA620FDC41A0C7FCBABF09FEC22 "点击放大")

### 实现方案

连接到指定Wi-Fi场景主要通过[@ohos.wifiManager (WLAN)](../harmonyos-references/js-apis-wifimanager.md)模块结合[@ohos.net.connection (网络连接管理)](../harmonyos-references/js-apis-net-connection.md)模块相关API来实现。通过@ohos.wifiManager模块检查Wi-Fi是否启用，获取系统扫描的Wi-Fi列表，选中指定Wi-Fi后发起连接请求；通过@ohos.net.connection模块检测网络连通性，判断是否需要进行登录认证（如 Portal 认证）才能正常访问网络。流程图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/ezPC4K6kTVa4Fr3tnPDyXg/zh-cn_image_0000002441647377.png?HW-CC-KV=V1&HW-CC-Date=20260428T002018Z&HW-CC-Expire=86400&HW-CC-Sign=3F71D147166BF56B54B174C76CB824484C31A81B8E1E8CAE9BC98F2BAEDDEA60 "点击放大")

### 开发步骤

1. 网络权限声明

   在进行网络相关操作前，需在应用的module.json5配置文件中声明所需权限。涉及的权限包括：

   * ohos.permission.GET\_NETWORK\_INFO：用于获取网络信息，如默认网络、网络类型等。
   * ohos.permission.GET\_WIFI\_INFO：用于获取Wi-Fi相关信息，如Wi-Fi是否打开、Wi-Fi列表等。
   * ohos.permission.SET\_WIFI\_INFO：用于执行Wi-Fi连接操作。
   * ohos.permission.INTERNET：用于访问Internet网络。

   ```
   1. {
   2. "module": {
   3. // ...
   4. "requestPermissions": [
   5. {
   6. "name": "ohos.permission.INTERNET",
   7. // ...
   8. },
   9. {
   10. "name": "ohos.permission.GET_NETWORK_INFO",
   11. // ...
   12. },
   13. {
   14. "name": "ohos.permission.SET_WIFI_INFO",
   15. // ...
   16. },
   17. {
   18. "name": "ohos.permission.GET_WIFI_INFO",
   19. // ...
   20. },
   21. // ...
   22. ]
   23. }
   24. }
   ```

   [module.json5](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/module.json5#L2-L134)
2. 获取Wi-Fi信息，判断是否连接到指定Wi-Fi

   先使用[getDefaultNetSync()](../harmonyos-references/js-apis-net-connection.md#connectiongetdefaultnetsync9)接口判断默认网络是否连接，并通过[getNetCapabilitiesSync()](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilitiessync10)方法获取默认连接网络类型。若网络类型为Wi-Fi，则使用[getLinkedInfoSync()](../harmonyos-references/js-apis-wifimanager.md#wifimanagergetlinkedinfosync18)方法获取当前连接的Wi-Fi信息，该信息包含SSID等内容。将获取到的SSID与指定Wi-Fi的SSID进行比对，若一致则表示已连接到指定Wi-Fi。

   ```
   1. checkNetwork(): void {
   2. try {
   3. // Use the synchronization method to obtain the default activated data network handle (default network)
   4. let netHandle = connection.getDefaultNetSync();
   5. if (netHandle.netId === 0) {
   6. // If there is no network connected, the netid of the obtained netHandler is 0
   7. showToast(this.uiContext, $r('app.string.no_network_tips'));
   8. return;
   9. }
   10. // Obtain the capability information of the network corresponding to the netHandle
   11. let netCapability = connection.getNetCapabilitiesSync(netHandle);
   12. let networkCap = netCapability.networkCap || [];
   13. let bearerTypes: connection.NetBearType[] = netCapability.bearerTypes;
   14. let isWifi = bearerTypes.includes(connection.NetBearType.BEARER_WIFI);
   15. if (!isWifi) {
   16. showToast(this.uiContext, $r('app.string.network_is_not_wifi'));
   17. return;
   18. }
   19. // The network type is WIFI to get network connection information
   20. let linkedInfo = wifiManager.getLinkedInfoSync();
   21. let ssid: string = linkedInfo.ssid;
   22. if (ssid === TARGET_WIFI_SSID) {
   23. // Connected to the target wifi
   24. // ...
   25. } else {
   26. showToast(this.uiContext, $r('app.string.not_connected_spec_wifi'));
   27. }
   28. } catch (err) {
   29. let error = err as BusinessError;
   30. Logger.error(TAG, `checkNetwork err, code: ${error.code}, message: ${error.message}`);
   31. }
   32. }
   ```

   [WifiConnector.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/view/WifiConnector.ets#L50-L92)

   通过[getNetCapabilitiesSync()](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilitiessync10)方法获取网络能力信息对象，其networkCap属性包含网络的具体能力。若networkCap中包含connection.NetCap.NET\_CAPABILITY\_VALIDATED，则表示网络具备访问互联网的能力（即网络可用）；若networkCap中包含connection.NetCap.NET\_CAPABILITY\_PORTAL，则说明网络需要认证登录之后才能正常使用。

   ```
   1. if (ssid === TARGET_WIFI_SSID) {
   2. // Connected to the target wifi
   3. if (networkCap.includes(connection.NetCap.NET_CAPABILITY_VALIDATED)) {
   4. showToast(this.uiContext, $r('app.string.connected_to_spec_wifi'));
   5. } else if (networkCap.includes(connection.NetCap.NET_CAPABILITY_PORTAL)) {
   6. // Login verification is required for the current network
   7. showToast(this.uiContext, $r('app.string.network_need_auth'));
   8. } else {
   9. showToast(this.uiContext, $r('app.string.result_network_unavailable'));
   10. }
   11. } else {
   12. showToast(this.uiContext, $r('app.string.not_connected_spec_wifi'));
   13. }
   ```

   [WifiConnector.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/view/WifiConnector.ets#L72-L86)
3. 获取系统扫描Wi-Fi列表

   在获取Wi-Fi列表之前，需要通过[isWifiActive()](../harmonyos-references/js-apis-wifimanager.md#wifimanageriswifiactive)方法判断Wi-Fi开关是否已打开。如果已打开，则通过调用[getScanInfoList()](../harmonyos-references/js-apis-wifimanager.md#wifimanagergetscaninfolist10)方法获取系统扫描附近的Wi-Fi网络，并返回一个包含所有扫描到的Wi-Fi信息的数组。数组中的每个元素包含了Wi-Fi的SSID、加密类型、信号强度等详细信息。

   ```
   1. getScanList(): void {
   2. try {
   3. let isWifiActive = wifiManager.isWifiActive();
   4. if (!isWifiActive) {
   5. showToast(this.uiContext, $r('app.string.turn_on_wlan_tips'));
   6. return;
   7. }
   8. this.getLinkedInfo();
   9. let temp = wifiManager.getScanInfoList();
   10. if (temp.length > 0) {
   11. // Remove duplicate WiFi data
   12. this.scanInfoList = this.uniqueBySsid(temp);
   13. Logger.info(TAG, `getScanList length: ${this.scanInfoList.length}`);
   14. }
   15. } catch (err) {
   16. let error = err as BusinessError;
   17. Logger.error(TAG, `getScanList err, code: ${error.code}, message: ${error.message}`);
   18. }
   19. }
   ```

   [WifiConnector.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/view/WifiConnector.ets#L131-L149)
4. 连接到指定Wi-Fi

   首先，创建一个包含要连接的Wi-Fi的SSID、密码及安全类型（如WPA2\_PSK）等信息的Wi-Fi配置对象，使用[addCandidateConfig()](../harmonyos-references/js-apis-wifimanager.md#wifimanageraddcandidateconfig)方法，传入该配置对象以添加候选网络配置。然后，调用[connectToCandidateConfig()](../harmonyos-references/js-apis-wifimanager.md#wifimanagerconnecttocandidateconfig)方法发起连接请求。

   ```
   1. connectWifi() {
   2. // Add a candidate network
   3. let config: wifiManager.WifiDeviceConfig = {
   4. ssid: this.ssid,
   5. preSharedKey: this.wifiPassword,
   6. securityType: this.securityType
   7. }

   9. try {
   10. wifiManager.addCandidateConfig(config).then(result => {
   11. Logger.info(TAG, `addCandidateConfig success, networkId: ${result}`);
   12. // Connect to a certain wifi
   13. wifiManager.connectToCandidateConfig(result);
   14. });
   15. } catch (err) {
   16. Logger.error(TAG, `connectWifi error: ${JSON.stringify(err)}`);
   17. }
   18. }
   ```

   [WlanItem.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/component/WlanItem.ets#L30-L47)

## 网络状态感知场景

### 场景描述

本章以网络视频播放场景为例，围绕网络状态感知展开，介绍如何在监听到网络状态变化后，动态调整视频播放行为，以优化播放体验。本章实现的网络视频播放优化体验如下：

* 当网络从Wi-Fi切换到蜂窝网络，及时暂停播放，并提醒用户已切换到蜂窝网络，以避免产生流量费用。
* 当网络从蜂窝切换到的Wi-Fi时，自动播放之前暂停的视频，让用户无需手动操作即可继续观看。

* 当监听到弱网状态时，提示用户当前网络不佳。同时，系统可能会根据当前的网络质量情况切换网络。

* 当监听到网络中断时，提示用户检查网络连接，以避免视频突然中断带来的不良体验。

### 实现方案

网络状态感知的实现方案以实时监测网络状态变化并联动视频播放业务的调整为核心，主要依赖于[@ohos.net.connection（网络连接管理）](../harmonyos-references/js-apis-net-connection.md)模块和[netQuality（网络质量）](../harmonyos-references/networkboost-netquality.md)模块来实现。本章重点介绍网络视频播放时对网络状态变化的感知，视频播放的具体实现可参考[示例代码](bpta-common-network-query.md#section14109114818615)章节。为避免网络波动影响播放流畅性，建议开发者进行缓存处理。

网络状态的监听主要通过以下接口实现：

* [on('netCapabilitiesChange')](../harmonyos-references/js-apis-net-connection.md#onnetcapabilitieschange)：订阅网络能力变化事件，当网络类型切换（如从Wi-Fi切换到蜂窝网络）、网络状态从无到有等，该事件将被触发。
* [on('netLost')](../harmonyos-references/js-apis-net-connection.md#onnetlost)：订阅网络丢失事件，当网络严重中断或正常断开时触发该事件。
* [on('netUnavailable')](../harmonyos-references/js-apis-net-connection.md#onnetunavailable)：订阅网络不可用事件，当网络不可用时触发该事件。
* [on('netAvailable')](../harmonyos-references/js-apis-net-connection.md#onnetavailable)：订阅网络可用事件，当网络可用时触发该事件。
* [netQuality.on( 'netSceneChange')](../harmonyos-references/networkboost-netquality.md#section132431252185419)：订阅网络场景信息，如从正常网络进入到弱网环境。

以视频播放场景为例，网络状态感知体验如下：

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 网络状态感知 | 网络类型变化 | | 网络能力变化 | | | |
| Wi-Fi切蜂窝 | 蜂窝切换Wi-Fi | 弱网场景 | 网络断开 | 网络不可用 | 网络可用 |
| 应用处理 | 暂停播放，提示将使用流量播放 | 正常播放 | 弹窗提示网络不佳。（开发者可以提供切换视频清晰度播放的功能，在弱网场景下提示用户切换清晰度。） | 弹窗提示网络已断开，视频加载失败后展示错误页面 | 弹窗提示网络不可用，视频加载失败后展示错误页面 | 和网络类型变化规格一致 |

### 开发步骤

1. 订阅网络可用/不可用事件

   使用[on('netAvailable')](../harmonyos-references/js-apis-net-connection.md#onnetavailable)订阅网络可用事件通知，接收到网络可用通知时，检测当前网络是否具备访问Internet的能力。若网络能正常访问Internet且此前因网络问题导致播放失败，则重置播放器并继续播放视频。

   ```
   1. import { connection } from '@kit.NetworkKit';
   ```

   [NetworkMonitor.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/view/NetworkMonitor.ets#L18-L18)

   ```
   1. // Create a NetConnection object
   2. this.netCon = connection.createNetConnection();
   3. // Subscribe to a network available event that triggers when the network is available
   4. this.netCon.on('netAvailable', (data: connection.NetHandle) => {
   5. Logger.info(TAG, `on netAvailable, Succeeded to get netAvailable: ${JSON.stringify(data)}`);
   6. this.isNetAvailable = NetworkUtil.isNetworkAvailable();
   7. this.isCellular = NetworkUtil.isCellular();
   8. if (this.isNetAvailable && this.isPlayError && !this.isCellular) {
   9. this.controller.reset();
   10. }
   11. });
   ```

   [NetworkMonitor.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/view/NetworkMonitor.ets#L78-L88)

   ```
   1. public static isNetworkAvailable(): boolean {
   2. try {
   3. let netHandle = connection.getDefaultNetSync();
   4. if (netHandle.netId === 0) {
   5. // If there is no network connected, the netid of the obtained netHandler is 0
   6. return false;
   7. }
   8. let netCapability = connection.getNetCapabilitiesSync(netHandle);
   9. let networkCaps: connection.NetCap[] = netCapability.networkCap || [];
   10. return networkCaps.includes(connection.NetCap.NET_CAPABILITY_VALIDATED);
   11. } catch (err) {
   12. let error = err as BusinessError;
   13. Logger.error(TAG, `getNetworkType err, errCode: ${error.code}, error mesage: ${error.message}`);
   14. }
   15. return false;
   16. }
   ```

   [NetworkUtil.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/common/NetworkUtil.ets#L46-L61)

   使用[on('netUnavailable')](../harmonyos-references/js-apis-net-connection.md#onnetunavailable)订阅网络不可用事件通知，接收到网络不可用事件时，使用Toast弹窗提示用户网络不可用。

   ```
   1. // Subscribe to a network unavailability event that triggers when the network is unavailable
   2. this.netCon.on('netUnavailable', () => {
   3. Logger.info(TAG, 'on netUnavailable, Succeeded to get unavailable net event');
   4. this.isNetAvailable = false;
   5. showToast(this.uiContext, $r('app.string.result_network_unavailable'));
   6. });
   ```

   [NetworkMonitor.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/view/NetworkMonitor.ets#L92-L97)
2. 订阅网络能力变化事件

   通过[on('netCapabilitiesChange')](../harmonyos-references/js-apis-net-connection.md#onnetcapabilitieschange)方法可以订阅Wi-Fi和蜂窝网络切换的事件通知，当网络切换为蜂窝时暂停播放，否则继续播放视频。

   ```
   1. // Subscribe to network capability change events that trigger when network capability changes,
   2. // such as from no network to network with network, or when switching from WIFI to cellular
   3. this.netCon.on('netCapabilitiesChange', (data: connection.NetCapabilityInfo) => {
   4. Logger.info(TAG, `on netCapabilitiesChange, Succeeded to get netCapabilitiesChange: ${JSON.stringify(data)}`);
   5. if (data.netCap.bearerTypes.includes(connection.NetBearType.BEARER_CELLULAR)) {
   6. // For cellular networks, pause playback
   7. this.isCellular = true;
   8. this.isShowController = false;
   9. this.controller.pause();
   10. showToast(this.getUIContext(), $r('app.string.current_cellular_tips'))
   11. this.isShowGoOn = true;
   12. } else {
   13. this.isCellular = false;
   14. this.isShowController = true;
   15. this.controller.start();
   16. this.isShowGoOn = false;
   17. }
   18. });
   ```

   [NetworkMonitor.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/view/NetworkMonitor.ets#L101-L118)

   从Wi-Fi切换为蜂窝网络效果图如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/8GH6egDBRa-5MieR-wiUsw/zh-cn_image_0000002407928064.png?HW-CC-KV=V1&HW-CC-Date=20260428T002018Z&HW-CC-Expire=86400&HW-CC-Sign=C96B6E2E9A811D365D11820D0CE645F7977AFBC76726D32C2603449A63BB4DE6 "点击放大")
3. 订阅网络丢失事件

   通过[on('netLost')](../harmonyos-references/js-apis-net-connection.md#onnetlost)方法可以订阅网络丢失的事件通知，使用Toast提示用户网络已断开。

   ```
   1. // Subscribe to a network loss event, triggered when the network is severely interrupted or normally disconnected,
   2. // and the network interruption pauses playback
   3. this.netCon.on('netLost', (data: connection.NetHandle) => {
   4. Logger.info(TAG, `on netLost, Succeeded to get netLost: ${JSON.stringify(data)}`);
   5. this.isNetAvailable = false;
   6. this.isCellular = false;
   7. showToast(this.uiContext, $r('app.string.network_disconnect_tips'));
   8. });
   ```

   [NetworkMonitor.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/view/NetworkMonitor.ets#L122-L129)

   网络断开时效果图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/VastCeEPT5mOUsE4_Ie9yg/zh-cn_image_0000002441567241.png?HW-CC-KV=V1&HW-CC-Date=20260428T002018Z&HW-CC-Expire=86400&HW-CC-Sign=23B30F7620B96FF4B80A398617BA49276AFBC7C7B0C94FE01FEC5AFCB7BA3B90 "点击放大")

   当网络断开时，将继续播放视频缓存；缓存播放完毕后，将触发Video组件的onError方法。若此时网络仍未连接，需提示用户检查网络。

   ```
   1. Video({ src: this.videoUrl, controller: this.controller })
   2. // ...
   3. .onError(() => {
   4. Logger.error(TAG, 'Video onError');
   5. this.lastTime = this.currentTime;
   6. this.isShowController = false;
   7. this.isPlayError = true;
   8. this.isPlaying = false;
   9. this.isNetAvailable = NetworkUtil.isNetworkAvailable();
   10. })
   ```

   [NetworkMonitor.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/view/NetworkMonitor.ets#L163-L199)

   播放错误时效果图

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/XeKF1Sd9Toq9jTndbspSBQ/zh-cn_image_0000002408087964.png?HW-CC-KV=V1&HW-CC-Date=20260428T002018Z&HW-CC-Expire=86400&HW-CC-Sign=9C09A66F97915BE26336A2F1A5F9F339F813417B073C04D6E1FECB508EA6B367 "点击放大")
4. 订阅网络状态变化通知

   接下来需要调用[register()](../harmonyos-references/js-apis-net-connection.md#register)接口，用来订阅指定的网络状态变化通知，该接口需在on()方法调用之后使用。例如，若指定的网络可用，将触发on('netAvailable')、on('netCapabilitiesChange')回调；若超时时间内网络不可用，将触发on('netUnavailable')回调。若断网，将触发on('netLost')回调。

   ```
   1. this.netCon.register((error: BusinessError) => {
   2. if (error) {
   3. Logger.error(TAG, `networkListen fail: ${JSON.stringify(error)}`);
   4. }
   5. });
   ```

   [NetworkMonitor.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/view/NetworkMonitor.ets#L133-L137)
5. 订阅网络场景变化

   使用[netQuality.on('netSceneChange')](../harmonyos-references/networkboost-netquality.md#section132431252185419)方法订阅网络场景变化通知，当网络为弱信号场景（weakSignal）或者拥塞场景（congestion）时，使用Toast弹窗提示用户当前网络不佳。建议开发者实现多种不同清晰度资源切换的功能，在此场景下，提示用户切换清晰度。

   ```
   1. import { netQuality } from '@kit.NetworkBoostKit';
   2. onNetSceneChange() {
   3. // Subscribe to network scene information
   4. try {
   5. netQuality.on('netSceneChange', (list: netQuality.NetworkScene[]) => {
   6. Logger.info(TAG, `on netSceneChange, Succeeded receive netSceneChange info: ${list.length}`);
   7. if (list.length > 0) {
   8. list.forEach((networkScene) => {
   9. if (networkScene.scene === 'weakSignal' || networkScene.scene === 'congestion') {
   10. this.promptAction.showToast({ message: $r('app.string.network_bad_tips') });
   11. }
   12. });
   13. }
   14. });
   15. } catch (err) {
   16. Logger.error(TAG, `on netSceneChange err: ${JSON.stringify(err)}`);
   17. }
   18. }
   ```

   [NetworkMonitor.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/view/NetworkMonitor.ets#L21-L73)
6. 取消订阅网络变化/取消订阅场景变化通知

   在退出页面时，通过调用[unregister()](../harmonyos-references/js-apis-net-connection.md#unregister)取消订阅网络状态变化通知，使用[netQuality.off('netSceneChange')](../harmonyos-references/networkboost-netquality.md#section32441952155417)取消订阅场景变化。

   ```
   1. aboutToDisappear(): void {
   2. // Unsubscribe from network status changes
   3. this.netCon?.unregister((err: BusinessError) => {
   4. if (err) {
   5. Logger.error(TAG, `unregister failed, err: ${JSON.stringify(err)}`);
   6. }
   7. });
   8. // Unsubscribe from network scenario information
   9. try {
   10. netQuality.off('netSceneChange');
   11. } catch (err) {
   12. Logger.error(TAG, `off netSceneChange err: ${JSON.stringify(err)}`);
   13. }
   14. }
   ```

   [NetworkMonitor.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/view/NetworkMonitor.ets#L142-L156)

## 获取Wi-Fi信息

### 场景描述

在公司考勤中，有些企业使用基于WLAN定位的网络打卡方式。员工需连接公司指定Wi-Fi，应用获取Wi-Fi的MAC地址后方可打卡。本章将介绍如何获取该MAC地址。

**图2** 获取Wi-Fi MAC地址效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/2zgeOKqWSdegy4XbDxOwKw/zh-cn_image_0000002441647385.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002018Z&HW-CC-Expire=86400&HW-CC-Sign=5EF75B5EFBB9E88345088A6468547CB09A0E7690114751FE5A42B1DAB78D3C92 "点击放大")

### 实现方案

使用[@ohos.geoLocationManager (位置服务)](../harmonyos-references/js-apis-geolocationmanager.md)模块的[getCurrentWifiBssidForLocating()](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentwifibssidforlocating14)方法获取当前连接的Wi-Fi MAC地址（Bssid）。通过将获取的MAC地址与业务服务端保存的Wi-Fi MAC地址进行比对，判断打卡是否成功。关于业务服务端的实现逻辑需要开发者自己实现，本文不做介绍。

说明

需要注意的是，虽然@ohos.wifiManager的[getLinkedInfo()](../harmonyos-references/js-apis-wifimanager.md#wifimanagergetlinkedinfo)也能获取当前连接Wi-Fi的MAC地址（Bssid），但需要申请ohos.permission.GET\_WIFI\_PEERS\_MAC权限（仅系统应用可申请）才能返回真实地址，否则为随机地址，因此不推荐用于Wi-Fi打卡和其他需要真实MAC地址的场景。

### 开发步骤

1. 检查WLAN连接状态

   通过[wifiManager.isWifiActive()](../harmonyos-references/js-apis-wifimanager.md#wifimanageriswifiactive)和[wifiManager.isConnected()](../harmonyos-references/js-apis-wifimanager.md#wifimanagerisconnected)分别获取WLAN开关的状态和连接状态，确保已经连接了Wi-Fi网络。

   ```
   1. import { wifiManager } from '@kit.ConnectivityKit';
   2. isWiFiConnected(): boolean {
   3. try {
   4. if (!wifiManager.isWifiActive()) {
   5. showToast(this.getUIContext(), $r('app.string.turn_on_wlan_tips'));
   6. return false;
   7. }

   9. if (wifiManager.isConnected()) {
   10. return true;
   11. } else {
   12. showToast(this.getUIContext(), $r('app.string.wifi_not_connect_tips'));
   13. return false;
   14. }
   15. } catch (err) {
   16. let error = err as BusinessError;
   17. Logger.error(TAG, `checkWifiStatus err, errCode: ${error.code}, error mesage: ${error.message}`);
   18. }
   19. return false;
   20. }
   ```

   [WlanLocation.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/view/WlanLocation.ets#L24-L91)
2. 申请位置信息权限

   获取当前连接Wi-Fi的MAC地址（Bssid）需要申请位置权限ohos.permission.LOCATION和ohos.permission.APPROXIMATELY\_LOCATION，首先在module.json5中声明位置权限。

   ```
   1. {
   2. "module": {
   3. // ...
   4. "requestPermissions": [
   5. // ...
   6. {
   7. "name": "ohos.permission.LOCATION",
   8. // ...
   9. },
   10. {
   11. "name": "ohos.permission.APPROXIMATELY_LOCATION",
   12. // ...
   13. }
   14. ]
   15. }
   16. }
   ```

   [module.json5](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/module.json5#L3-L135)

   动态申请位置权限。

   ```
   1. import { abilityAccessCtrl, bundleManager, Permissions } from '@kit.AbilityKit';
   2. async requestPermissions(): Promise<number> {

   4. return new Promise((resolve, reject) => {
   5. try {
   6. const permissions: Permissions[] = ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION'];
   7. const accessManager = abilityAccessCtrl.createAtManager();
   8. const bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION;
   9. const bundleInfo = bundleManager.getBundleInfoForSelfSync(bundleFlags);
   10. const grantStatus = accessManager.checkAccessTokenSync(bundleInfo.appInfo.accessTokenId, permissions[0]);
   11. if (grantStatus === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
   12. resolve(0);
   13. return;
   14. }
   15. accessManager.requestPermissionsFromUser(this.getUIContext().getHostContext(), permissions).then((data) => {
   16. Logger.info(TAG, `request permissions result: ${JSON.stringify(data)}`);
   17. let grantStatus: number[] = data.authResults;
   18. if (grantStatus.length > 0 && grantStatus[0] === 0) {
   19. Logger.info(TAG, 'request permissions granted');
   20. resolve(0);
   21. } else {
   22. Logger.info('request permissions denied');
   23. showToast(this.getUIContext(), $r('app.string.no_location_permission_tips'));
   24. resolve(-1);
   25. }
   26. }).catch((error: BusinessError) => {
   27. Logger.error(TAG, `request permissions exception, Catch error:${JSON.stringify(error)}`);
   28. reject(error);
   29. })
   30. } catch (err) {
   31. let error = err as BusinessError;
   32. Logger.error(TAG, `requestPermissions err, errCode: ${error.code}, error mesage: ${error.message}`);
   33. }
   34. });
   35. }
   ```

   [WlanLocation.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/view/WlanLocation.ets#L17-L69)
3. 获取连接Wi-Fi的MAC地址

   使用[geoLocationManager.getCurrentWifiBssidForLocating()](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentwifibssidforlocating14)方法获取Wi-Fi的MAC地址。

   ```
   1. import { geoLocationManager } from '@kit.LocationKit';
   2. getWiFiBssid() {
   3. if (this.isWiFiConnected()) {
   4. this.requestPermissions().then(result => {
   5. if (result === 0) {
   6. Logger.info(TAG, 'request location permissions success');
   7. try {
   8. let bssid: string = geoLocationManager.getCurrentWifiBssidForLocating();
   9. Logger.info(TAG, `getCurrentWifiBssidForLocating wifi bssid success: ${bssid}`);
   10. this.macAddress = bssid;
   11. } catch (error) {
   12. Logger.error(TAG, `getCurrentWifiBssidForLocatingerror: ${JSON.stringify(error)}`);
   13. }
   14. }
   15. });
   16. }
   17. }
   ```

   [WlanLocation.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/view/WlanLocation.ets#L21-L110)

## 网络故障诊断分析场景

### 场景描述

用户在使用应用的网络功能时，网络故障（如无法访问、加载缓慢、连接中断）是常见的问题。为了方便定位问题，需要获取路由、网络类型、代理、DNS、网关、运营商及信号强度、时延等信息。通过分析这些数据，可以判断问题出在设备、运营商还是服务器，从而采取相应措施恢复网络和应用的正常运行。

本章将介绍一些常见网络信息的获取，主要包含以下信息：

* 网络类型
* 网络代理信息
* 路由信息
* 当前网络的IP地址
* 当前网络的DNS服务器
* 当前Wi-Fi信号强度
* 当前设备Wi-Fi MAC地址
* 蜂窝网络制式
* 蜂窝主卡的Radio是否打开
* 运营商名称
* 蜂窝网络是否处于漫游状态
* 蜂窝网络信号强度
* 网络时延

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/e1q6hnR6TYKt3qpalvQK9w/zh-cn_image_0000002407928068.png?HW-CC-KV=V1&HW-CC-Date=20260428T002018Z&HW-CC-Expire=86400&HW-CC-Sign=2FBC11F743201DDD4A822AE9873DBA4AAD259765956FB11D48573655A5724D73 "点击放大")

### 实现方案

主要通过以下模块的相关API获取网络故障诊断场景所需的网络信息：

* [@ohos.net.connection (网络连接管理)](../harmonyos-references/js-apis-net-connection.md)：用于获取网络的基本信息，如网络类型、IP 地址、网关、DNS 服务器等。通过[getNetCapabilitiesSync()](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilitiessync10)方法获取网络能力信息，包括网络类型、网络是否可用等；[getConnectionPropertiesSync()](../harmonyos-references/js-apis-net-connection.md#connectiongetconnectionpropertiessync10)方法获取网络配置信息，包括 IP、网关、DNS等
* [@ohos.wifiManager (WLAN)](../harmonyos-references/js-apis-wifimanager.md)：获取Wi-Fi网络的信号强度、设备MAC地址等信息。使用[getLinkedInfoSync()](../harmonyos-references/js-apis-wifimanager.md#wifimanagergetlinkedinfosync18)方法获取当前连接Wi-Fi的信号强度（rssi属性）和MAC 地址（bssid属性）。
* [@ohos.telephony.radio (网络搜索)](../harmonyos-references/js-apis-radio.md)：获取蜂窝网络的相关信息，如运营商名称、网络制式、信号强度、是否处于漫游状态以及主卡Radio是否打开等。例如，[getOperatorNameSync()](../harmonyos-references/js-apis-radio.md#radiogetoperatornamesync10)方法获取运营商名称，[getSignalInformationSync()](../harmonyos-references/js-apis-radio.md#radiogetsignalinformationsync10)方法获取信号强度信息和网络制式。
* [netQuality(网络质量)](../harmonyos-references/networkboost-netquality.md)：提供网络质量实时评估、网络场景识别以及弱信号预测等能力。使用[netQuality.on( 'netQosChange')](../harmonyos-references/networkboost-netquality.md#section13106021163)订阅网络质量信息，包含信号强度、下载速度、网络时延等。

本章提供了网络故障诊断分析场景的检测项和规格，以下内容仅供参考，开发者可根据自身业务需求选择检测项并定义规格。

* 网络可用性是否可用：如果不可用，则检测结果为网络不可用。
* 网络是否连接：如果未连接，则检测结果为网络未连接。
* 网络信号强度：如果Wi-Fi低于-70dbm，蜂窝信号强度低于-100dbm，则检测结果为当前网络不佳。
* 时延：如果rttMs>500ms，则检测结果为当前网络不佳。
* 下载速度：如果下载速度小于<1MB/s，则检测结果为当前网络不佳。

以上检测项都未异常，则检测结果为网络正常。其中信号强度、时延和下载速度的获取，通过开启下载任务[request.agent.create()](../harmonyos-references/js-apis-request.md#requestagentcreate10-1)，取10秒的平均值。

### 开发步骤

1. 获取网络连接信息

   该步骤整合了通过@ohos.net.connection模块可获取的各类网络基础连接信息，通过[getNetCapabilitiesSync()](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilitiessync10)方法获取网络类型和是否可用。

   ```
   1. checkNetAvailable(): void {
   2. try {
   3. let netHandle = connection.getDefaultNetSync();
   4. if (netHandle.netId === 0) {
   5. // If there is no network connected, the netid of the obtained netHandler is 0
   6. this.hasNetwork = false;
   7. this.checkResult = $r('app.string.result_network_not_connect');
   8. return;
   9. }
   10. this.hasNetwork = true;
   11. let netCapability = connection.getNetCapabilitiesSync(netHandle);
   12. let bearerTypes: connection.NetBearType[] = netCapability.bearerTypes;
   13. let netCaps: connection.NetCap[] = netCapability.networkCap || [];
   14. this.networkType = NetworkUtil.getNetworkTypeStr(bearerTypes[0]);
   15. this.isNetAvailable = netCaps.includes(connection.NetCap.NET_CAPABILITY_VALIDATED);
   16. if (this.isNetAvailable) {
   17. this.checkResult = $r('app.string.result_network_available');
   18. } else {
   19. this.checkResult = $r('app.string.result_network_unavailable');
   20. }
   21. } catch (err) {
   22. let error = err as BusinessError;
   23. Logger.error(TAG, `getNetworkType err, errCode: ${error.code}, error mesage: ${error.message}`);
   24. }
   25. }
   ```

   [NetworkDiagnostics.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/view/NetworkDiagnostics.ets#L89-L114)

   通过[getConnectionPropertiesSync()](../harmonyos-references/js-apis-net-connection.md#connectiongetconnectionpropertiessync10)方法获取路由信息、IP信息、DNS服务信息，通过[getDefaultHttpProxy()](../harmonyos-references/js-apis-net-connection.md#connectiongetdefaulthttpproxy10-1)方法获取代理信息。

   ```
   1. getConnectionInfo(): void {
   2. try {
   3. let netHandle = connection.getDefaultNetSync();
   4. let properties = connection.getConnectionPropertiesSync(netHandle);
   5. // route info
   6. let routes = properties.routes || [];
   7. // ip address info
   8. let addresses = properties.linkAddresses || [];
   9. // dns service info
   10. let dnses = properties.dnses || [];
   11. // ...
   12. // get proxy info
   13. connection.getDefaultHttpProxy().then((data: connection.HttpProxy) => {
   14. Logger.info(TAG, `getDefaultHttpProxy success, data: ${JSON.stringify(data)}`);
   15. this.proxyInfo = JSON.stringify(data);
   16. }).catch((error: BusinessError) => {
   17. Logger.error(TAG, `getDefaultHttpProxy err, code: ${error.code}, mesage: ${error.message}`);
   18. });
   19. } catch (err) {
   20. let error = err as BusinessError;
   21. Logger.error(TAG, `getConnectionInfo err, code: ${error.code}, message: ${error.message}`);
   22. }
   23. }
   ```

   [NetworkDiagnostics.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/view/NetworkDiagnostics.ets#L200-L227)
2. 获取Wi-Fi信息

   通过@ohos.wifiManager模块的[getLinkedInfoSync()](../harmonyos-references/js-apis-wifimanager.md#wifimanagergetlinkedinfosync18)方法获取信号强度和MAC地址信息，这些信息对诊断Wi-Fi连接不稳定、信号弱等问题至关重要。

   ```
   1. getWifiInfo(): void {
   2. try {
   3. let linkInfo = wifiManager.getLinkedInfoSync();
   4. this.wifiSignal = `${linkInfo.rssi}dBm`;
   5. this.wifiMac = linkInfo.macAddress;
   6. } catch (err) {
   7. let error = err as BusinessError;
   8. Logger.error(TAG, `getWifiRssi err, code: ${error.code}, message: ${error.message}`);
   9. }
   10. }
   ```

   [NetworkDiagnostics.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/view/NetworkDiagnostics.ets#L231-L241)
3. 获取蜂窝网络信息

   通过@ohos.telephony.radio模块获取蜂窝网络相关信息。

   * 使用[radio.getOperatorNameSync()](../harmonyos-references/js-apis-radio.md#radiogetoperatornamesync10)方法获取运营商名称。
   * 使用[radio.isRadioOn()](../harmonyos-references/js-apis-radio.md#radioisradioon7-1)方法检查蜂窝主卡的Radio是否开启。
   * 使用[radio.getNetworkState()](../harmonyos-references/js-apis-radio.md#radiogetnetworkstate-2)方法判断蜂窝网络是否处于漫游状态。
   * 使用[radio.getSignalInformationSync()](../harmonyos-references/js-apis-radio.md#radiogetsignalinformationsync10)方法获取蜂窝网络信号强度和网络制式。

   ```
   1. async getCellularInfo(): Promise<void> {
   2. try {
   3. let primarySlotId = await radio.getPrimarySlotId();
   4. // Get the carrier name
   5. this.operatorName = radio.getOperatorNameSync(primarySlotId);
   6. // Whether the radio on the cellular main card is turned on
   7. this.isRadioOn = await radio.isRadioOn(primarySlotId);
   8. let networkState = await radio.getNetworkState(primarySlotId);
   9. // Determine whether the cellular network is roaming
   10. this.isRoaming = networkState.isRoaming + '';
   11. let signalInfos: radio.SignalInformation[] = radio.getSignalInformationSync(primarySlotId);
   12. if (signalInfos.length > 0) {
   13. let signalInfo = signalInfos[0];
   14. // Get cellular network signal strength
   15. this.cellularSignal = signalInfo.dBm + 'dBm';
   16. // Get the cellular network standard
   17. this.cellularType = NetworkUtil.getCellularTypeStr(signalInfo.signalType);
   18. }
   19. } catch (err) {
   20. let error = err as BusinessError;
   21. Logger.error(TAG, `getCellularInfo err, errCode: ${error.code}, error mesage: ${error.message}`);
   22. }
   23. }
   ```

   [NetworkDiagnostics.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/view/NetworkDiagnostics.ets#L245-L268)
4. 检测网络质量

   首先判断网络是否连接和是否可用，如果未连接或者不可用，则显示网络未连接和网络不可用的结果。

   ```
   1. checkNetAvailable(): void {
   2. try {
   3. let netHandle = connection.getDefaultNetSync();
   4. if (netHandle.netId === 0) {
   5. // If there is no network connected, the netid of the obtained netHandler is 0
   6. this.hasNetwork = false;
   7. this.checkResult = $r('app.string.result_network_not_connect');
   8. return;
   9. }
   10. this.hasNetwork = true;
   11. let netCapability = connection.getNetCapabilitiesSync(netHandle);
   12. let bearerTypes: connection.NetBearType[] = netCapability.bearerTypes;
   13. let netCaps: connection.NetCap[] = netCapability.networkCap || [];
   14. this.networkType = NetworkUtil.getNetworkTypeStr(bearerTypes[0]);
   15. this.isNetAvailable = netCaps.includes(connection.NetCap.NET_CAPABILITY_VALIDATED);
   16. if (this.isNetAvailable) {
   17. this.checkResult = $r('app.string.result_network_available');
   18. } else {
   19. this.checkResult = $r('app.string.result_network_unavailable');
   20. }
   21. } catch (err) {
   22. let error = err as BusinessError;
   23. Logger.error(TAG, `getNetworkType err, errCode: ${error.code}, error mesage: ${error.message}`);
   24. }
   25. }
   ```

   [NetworkDiagnostics.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/view/NetworkDiagnostics.ets#L89-L114)

   如果有网络连接，则开启下载任务用于网络质量测试，下载任务持续时间为10秒。

   ```
   1. queryNetworkInfo() {
   2. this.checkNetAvailable();
   3. if (!this.hasNetwork) {
   4. this.clearContent();
   5. return;
   6. }
   7. this.getConnectionInfo();
   8. this.getWifiInfo();
   9. this.getCellularInfo();

   11. if (this.timeoutId === -1 && TEST_DOWNLOAD_URL !== '') {
   12. this.checkResult = $r('app.string.result_is_checking');
   13. // Start download file
   14. NetworkUtil.downloadFile(this.context, TEST_DOWNLOAD_URL, this.cachePath);
   15. this.timeoutId = setTimeout(() => {
   16. // Remove download task after 10 seconds
   17. NetworkUtil.removeTask();
   18. this.timeoutId = -1;
   19. }, 10000)
   20. }
   21. }
   ```

   [NetworkDiagnostics.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/view/NetworkDiagnostics.ets#L65-L85)

   在下载任务期间，通过netQuality模块的on('netQosChange')接口实时监听网络质量变化，获取时延、下载速度等关键指标。并计算10秒内的平均下载速度、平均时延、Wi-Fi和蜂窝的平均信号强度。并根据这些指标和规格数据对比，获取检测结果，数据规格参考[实现方案](bpta-common-network-query.md#section488194602211)小节。

   ```
   1. onQosChange(): void {
   2. try {
   3. netQuality.on('netQosChange', (list: netQuality.NetworkQos[]) => {
   4. if (list.length > 0) {
   5. list.forEach(async (qos) => {
   6. // ...
   7. if (this.timeoutId !== -1 && TEST_DOWNLOAD_URL !== '') {
   8. let wifiRssi = NetworkUtil.getWifiSignalRssi();
   9. let cellularRssi = await NetworkUtil.getCellularSignalRssi();
   10. this.totalSpeed += qos.linkDownRate;
   11. this.totalRttMs += qos.rttMs;
   12. this.totalWifiRssi += wifiRssi;
   13. this.totalCellularRssi += cellularRssi;
   14. this.rttMsTimes += 1;
   15. }
   16. if ((this.timeoutId === -1) && (this.rttMsTimes !== 0) && (TEST_DOWNLOAD_URL !== '')) {
   17. // Average download speed
   18. let avgSpeed = this.totalSpeed / 8 / 1024 / 1024 / 10;
   19. // Average latency
   20. let avgRttMs = this.totalRttMs / this.rttMsTimes;
   21. // Average wifi signal strength
   22. let avgWifiRssi = this.totalWifiRssi / this.rttMsTimes;
   23. // Average cellular signal strength
   24. let avgCellularRssi = this.totalCellularRssi / this.rttMsTimes;
   25. // ...
   26. if (avgSpeed < 1 || avgRttMs > 100) {
   27. this.checkResult = $r('app.string.network_bad_tips');
   28. return;
   29. }
   30. // The network is considered poor when the WiFi signal strength is below -70dBm
   31. // or the cellular network signal strength is below -100dBm
   32. if ((this.networkType === 'wifi' && avgWifiRssi < -70) ||
   33. (this.networkType === 'cellular' && avgCellularRssi < -100)) {
   34. this.checkResult = $r('app.string.network_bad_tips');
   35. } else {
   36. this.checkResult = $r('app.string.result_network_normal');
   37. }
   38. }
   39. });
   40. }
   41. });
   42. } catch (err) {
   43. let error = err as BusinessError;
   44. Logger.error(TAG, `on netQosChange err, code: ${error.code}, message: ${error.message}`);
   45. }
   46. }
   ```

   [NetworkDiagnostics.ets](https://gitcode.com/harmonyos_samples/network-query/blob/master/entry/src/main/ets/view/NetworkDiagnostics.ets#L136-L196)

## 示例代码

* [实现常见网络信息查询](https://gitcode.com/harmonyos_samples/network-query)
