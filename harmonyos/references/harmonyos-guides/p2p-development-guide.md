---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/p2p-development-guide
title: P2P模式开发指南
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > WLAN > P2P模式开发指南
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:44+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:ef91c3f94269ff288c49dcf7dc0d0a9b6ee7b5966d8dc5cc1ee29a4731889a2e
---

## 简介

P2P模式，主要提供了WLAN设备的一种点对点连接技术，它可以在两台STA之间直接建立TCP/IP连接，并不需要AP的参与。

## 场景介绍

主要场景有：

* 创建/删除P2P群组
* 建立P2P连接

## 接口说明

完整的JS API说明以及示例代码请参考：[P2P接口](../harmonyos-references/js-apis-wifimanager.md)。

具体接口说明如下表。

| 接口名 | 功能描述 |
| --- | --- |
| createGroup() | 创建群组。 |
| removeGroup() | 删除群组。 |
| startDiscoverDevices() | 开始发现设备。 |
| getP2pPeerDevices() | 获取P2P对端设备列表信息。 |
| p2pConnect() | 执行P2P连接。 |
| getP2pLinkedInfo() | 获取P2P连接信息。 |
| on(type: 'p2pPersistentGroupChange') | 注册P2P永久组状态改变事件。 |
| off(type: 'p2pPersistentGroupChange') | 取消注册P2P永久组状态改变事件。 |
| on(type: 'p2pPeerDeviceChange') | 注册P2P对端设备状态改变事件。 |
| off(type: 'p2pPeerDeviceChange') | 取消注册P2P对端设备状态改变事件。 |
| on(type: 'p2pConnectionChange') | 注册P2P连接状态改变事件。 |
| off(type: 'p2pConnectionChange') | 取消注册P2P连接状态改变事件。 |

## 主要场景开发步骤

### 创建/删除P2P群组

1. import需要的Wi-Fi模块。

   ```
   1. import { wifiManager } from '@kit.ConnectivityKit';
   ```
2. 开启设备的Wi-Fi。
3. 需要SystemCapability.Communication.WiFi.P2P系统能力。
4. 创建/删除P2P群组。

   ```
   1. async createGroup() {
   2. try {
   3. let deviceInfo = await wifiManager.getP2pLocalDevice();
   4. let config:wifiManager.WifiP2PConfig = {
   5. deviceAddress: deviceInfo.deviceAddress,
   6. netId: this.netId,
   7. passphrase: this.passphrase,
   8. groupName: this.groupName,
   9. goBand: this.goBand,
   10. }
   11. hilog.info(`deviceAddress: ${config.deviceAddress}, netId: ${config.netId}, pwd: ${config.passphrase}, gpname: ${config.groupName}, goBand: ${config.goBand}`);
   12. await wifiManager.createGroup(config);
   13. this.promptAction.showToast({
   14. message: 'createGroup success',
   15. duration: 2000
   16. });
   17. } catch (e) {
   18. hilog.info(TAG, `createGroup Error: ${JSON.stringify(e)}`);
   19. }
   20. }
   ```
5. 示例代码：

   ```
   1. import { wifiManager } from '@kit.ConnectivityKit';

   3. // 创建群组，将当前设备当作GO使用时，需要该步骤
   4. // netId：-1表示创建临时组，下次和已连接过的设备连接，需要重新进行GO协商，以及WPS密钥协商;
   5. // netId：-2表示创建永久组，下次和已连接过的设备连接，不需要重新进行GO和WPS密钥协商;

   7. let recvP2pPersistentGroupChangeFunc = () => {
   8. console.info("p2p persistent group change receive event");

   10. // 永久组创建好后需要处理的业务
   11. }
   12. // 创建永久组，需要注册永久组状态改变事件回调
   13. wifiManager.on("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);
   14. try {
   15. let config: wifiManager.WifiP2PConfig = {
   16. deviceAddress: "00:11:22:33:44:55",
   17. deviceAddressType: 1,
   18. netId: -2,
   19. passphrase: "12345678",
   20. groupName: "testGroup",
   21. goBand: 0
   22. }
   23. wifiManager.createGroup(config);
   24. } catch (error) {
   25. console.error("failed:" + JSON.stringify(error));
   26. }

   28. // 删除群组
   29. try {
   30. wifiManager.removeGroup();
   31. } catch (error) {
   32. console.error("failed:" + JSON.stringify(error));
   33. }
   ```
6. 错误码请参见[WIFI错误码](../harmonyos-references/errorcode-wifi.md)。

### 建立P2P连接

1. import需要的Wi-Fi模块。

   ```
   1. import { wifiManager } from '@kit.ConnectivityKit';
   ```
2. 开启设备的Wi-Fi。
3. 需要SystemCapability.Communication.WiFi.P2P系统能力。
4. 注册"p2pPeerDeviceChange"事件回调，并在回调实现中执行P2P连接。

   ```
   1. connectP2p(p2pScanInfo: wifiManager.WifiP2pDevice) {
   2. this.promptAction.showToast({
   3. message: 'connect to device',
   4. duration: 2000
   5. });
   6. hilog.info(TAG , `connect deviceAddress=${ p2pScanInfo.deviceAddress }`);
   7. hilog.info(TAG , `p2pScanInfo:` + JSON.stringify(p2pScanInfo));
   8. let config: wifiManager.WifiP2PConfig = {
   9. deviceAddress : p2pScanInfo.deviceAddress,
   10. netId : - 2 ,
   11. deviceAddressType: 1,
   12. passphrase : '' ,
   13. groupName : '' ,
   14. goBand : 0
   15. }
   16. wifiManager.p2pConnect(config);
   17. }
   ```
5. 开始P2P设备发现。

   ```
   1. aboutToAppear() {
   2. // 如果wifi是开的，就记录下状态，然后扫描p2p设备，并获取连接信息
   3. if (!wifiManager.isWifiActive()) {
   4. this.promptAction.showToast({
   5. message: 'please activate wifi',
   6. duration: 2000
   7. });
   8. return;
   9. }
   10. this.isSwitchOn = true;
   11. wifiManager.startDiscoverDevices();
   12. this.addListener();
   13. }

   15. aboutToDisappear() {
   16. wifiManager.off('p2pPeerDeviceChange');
   17. wifiManager.off('p2pConnectionChange');
   18. }
   ```
6. 示例代码：

   ```
   1. import { wifiManager } from '@kit.ConnectivityKit';

   3. let recvP2pConnectionChangeFunc = (result: wifiManager.WifiP2pLinkedInfo) => {
   4. console.info("p2p connection change receive event: " + JSON.stringify(result));
   5. wifiManager.getP2pLinkedInfo((err, data) => {
   6. if (err) {
   7. console.error("failed to get P2pLinkedInfo: " + JSON.stringify(err));
   8. return;
   9. }
   10. console.info("get getP2pLinkedInfo: " + JSON.stringify(data));
   11. // 添加P2P连接成功或者失败场景的业务处理
   12. });
   13. }
   14. // P2P连接完成，会调用"p2pConnectionChange"事件回调
   15. wifiManager.on("p2pConnectionChange", recvP2pConnectionChangeFunc);

   17. let recvP2pPeerDeviceChangeFunc = (result: wifiManager.WifiP2pDevice[]) => {
   18. console.info("p2p peer device change receive event: " + JSON.stringify(result));
   19. wifiManager.getP2pPeerDevices((err, data) => {
   20. if (err) {
   21. console.error("failed to get peer devices: " + JSON.stringify(err));
   22. return;
   23. }
   24. console.info("get peer devices: " + JSON.stringify(data));
   25. let len = data.length;
   26. for (let i = 0; i < len; ++i) {
   27. // 选择符合条件的对端P2P设备
   28. if (data[i].deviceName === "my_test_device") {
   29. console.info("p2p connect to test device: " + data[i].deviceAddress);
   30. let config: wifiManager.WifiP2PConfig = {
   31. deviceAddress: data[i].deviceAddress,
   32. deviceAddressType: 1,
   33. netId: -2,
   34. passphrase: "",
   35. groupName: "",
   36. goBand: 0,
   37. }
   38. // 执行P2P连接，作为GO时不能主动发起连接
   39. wifiManager.p2pConnect(config);
   40. }
   41. }
   42. });
   43. }
   44. // P2P扫描结果上报时会调用"p2pPeerDeviceChange"事件回调
   45. wifiManager.on("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);

   47. setTimeout(() => {
   48. wifiManager.off("p2pConnectionChange", recvP2pConnectionChangeFunc);
   49. }, 125 * 1000);
   50. setTimeout(() => {
   51. wifiManager.off("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);
   52. }, 125 * 1000);
   53. // 开始发现P2P设备，即，开始P2P扫描
   54. console.info("start discover devices -> " + wifiManager.startDiscoverDevices());
   ```
7. 错误码请参见[WIFI错误码](../harmonyos-references/errorcode-wifi.md)。

### 获取对端IP以及Socket通信

1. import需要的Wi-Fi模块。
2. 开启设备的Wi-Fi。
3. 需要SystemCapability.Communication.WiFi.P2P系统能力。
4. 通过[wifiP2pLinkedInfo.connectState](../harmonyos-references/js-apis-wifimanager.md#p2pconnectstate)获取P2P连接状态，确保连接状态为CONNECTED。
5. 通过[wifiP2pGroupInfo.goIpAddress](../harmonyos-references/js-apis-wifimanager.md#wifip2pgroupinfo)获取群组IP地址，以便Socket通信。
6. Socket通信请参考[使用Socket访问网络](socket-connection.md)。
