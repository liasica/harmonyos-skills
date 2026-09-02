---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/p2p-development-guide
title: P2P模式开发指南
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > WLAN > P2P模式开发指南
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9bb9053430e46c3b343d699d2a5199d429f48cedb806eb6ffc7f48e7376e6043
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

   ```typescript
   import { wifiManager } from '@kit.ConnectivityKit';
   ```
2. 开启设备的Wi-Fi。
3. 需要SystemCapability.Communication.WiFi.P2P系统能力。
4. 创建/删除P2P群组。

   ```typescript
   async createGroup() {
     try {
       let deviceInfo = await wifiManager.getP2pLocalDevice();
       let config:wifiManager.WifiP2PConfig = {
         deviceAddress: deviceInfo.deviceAddress,
         netId: this.netId,
         passphrase: this.passphrase,
         groupName: this.groupName,
         goBand: this.goBand,
       }
       hilog.info(`deviceAddress: ${config.deviceAddress}, netId: ${config.netId}, pwd: ${config.passphrase}, gpname: ${config.groupName}, goBand: ${config.goBand}`);
       await wifiManager.createGroup(config);
       this.promptAction.showToast({
         message: 'createGroup success',
         duration: 2000
       });
     } catch (e) {
       hilog.info(TAG, `createGroup Error: ${JSON.stringify(e)}`);
     }
   }
   ```
5. 示例代码：

   ```ts
   import { wifiManager } from '@kit.ConnectivityKit';

   // 创建群组，将当前设备当作GO使用时，需要该步骤
   // netId：-1表示创建临时组，下次和已连接过的设备连接，需要重新进行GO协商，以及WPS密钥协商;
   // netId：-2表示创建永久组，下次和已连接过的设备连接，不需要重新进行GO和WPS密钥协商;

   let recvP2pPersistentGroupChangeFunc = () => {
     console.info("p2p persistent group change receive event");

     // 永久组创建好后需要处理的业务
   }
   // 创建永久组，需要注册永久组状态改变事件回调
   wifiManager.on("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);
   try {
     let config: wifiManager.WifiP2PConfig = {
       deviceAddress: "00:11:22:33:44:55",
       deviceAddressType: 1,
       netId: -2,
       passphrase: "12345678",
       groupName: "testGroup",
       goBand: 0
   }
     wifiManager.createGroup(config);
   } catch (error) {
     console.error("failed:" + JSON.stringify(error));
   }

   // 删除群组
   try {
     wifiManager.removeGroup();
   } catch (error) {
     console.error("failed:" + JSON.stringify(error));
   }
   ```
6. 错误码请参见[WIFI错误码](../harmonyos-references/errorcode-wifi.md)。

### 建立P2P连接

1. import需要的Wi-Fi模块。

   ```typescript
   import { wifiManager } from '@kit.ConnectivityKit';
   ```
2. 开启设备的Wi-Fi。
3. 需要SystemCapability.Communication.WiFi.P2P系统能力。
4. 注册"p2pPeerDeviceChange"事件回调，并在回调实现中执行P2P连接。

   ```typescript
   connectP2p(p2pScanInfo: wifiManager.WifiP2pDevice) {
     this.promptAction.showToast({
       message: 'connect to device',
       duration: 2000
     });
     hilog.info(TAG , `connect deviceAddress=${ p2pScanInfo.deviceAddress }`);
     hilog.info(TAG , `p2pScanInfo:` + JSON.stringify(p2pScanInfo));
     let config: wifiManager.WifiP2PConfig = {
       deviceAddress : p2pScanInfo.deviceAddress,
       netId : - 2 ,
       deviceAddressType: 1,
       passphrase : '' ,
       groupName : '' ,
       goBand : 0
     }
     wifiManager.p2pConnect(config);
   }
   ```
5. 开始P2P设备发现。

   ```typescript
   aboutToAppear() {
     // 如果wifi是开的，就记录下状态，然后扫描p2p设备，并获取连接信息
     if (!wifiManager.isWifiActive()) {
       this.promptAction.showToast({
         message: 'please active wifi',
         duration: 2000
       });
       return;
     }
     this.isSwitchOn = true;
     wifiManager.startDiscoverDevices();
     this.addListener();
   }

   aboutToDisappear() {
     wifiManager.off('p2pPeerDeviceChange');
     wifiManager.off('p2pConnectionChange');
   }
   ```
6. 示例代码：

   ```ts
   import { wifiManager } from '@kit.ConnectivityKit';

   let recvP2pConnectionChangeFunc = (result: wifiManager.WifiP2pLinkedInfo) => {
     console.info("p2p connection change receive event: " + JSON.stringify(result));
     wifiManager.getP2pLinkedInfo((err, data) => {
       if (err) {
         console.error("failed to get P2pLinkedInfo: " + JSON.stringify(err));
         return;
       }
       console.info("get getP2pLinkedInfo: " + JSON.stringify(data));
       // 添加P2P连接成功或者失败场景的业务处理
     });
   }
   // P2P连接完成，会调用"p2pConnectionChange"事件回调
   wifiManager.on("p2pConnectionChange", recvP2pConnectionChangeFunc);

   let recvP2pPeerDeviceChangeFunc = (result: wifiManager.WifiP2pDevice[]) => {
     console.info("p2p peer device change receive event: " + JSON.stringify(result));
     wifiManager.getP2pPeerDevices((err, data) => {
       if (err) {
         console.error("failed to get peer devices: " + JSON.stringify(err));
         return;
       }
       console.info("get peer devices: " + JSON.stringify(data));
       let len = data.length;
       for (let i = 0; i < len; ++i) {
         // 选择符合条件的对端P2P设备
         if (data[i].deviceName === "my_test_device") {
           console.info("p2p connect to test device: " + data[i].deviceAddress);
           let config: wifiManager.WifiP2PConfig = {
             deviceAddress: data[i].deviceAddress,
             deviceAddressType: 1,
             netId: -2,
             passphrase: "",
             groupName: "",
             goBand: 0,
           }
           // 执行P2P连接，作为GO时不能主动发起连接
           wifiManager.p2pConnect(config);
         }
       }
     });
   }
   // P2P扫描结果上报时会调用"p2pPeerDeviceChange"事件回调
   wifiManager.on("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);

   setTimeout(() => {
     wifiManager.off("p2pConnectionChange", recvP2pConnectionChangeFunc);
   }, 125 * 1000);
   setTimeout(() => {
     wifiManager.off("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);
   }, 125 * 1000);
   // 开始发现P2P设备，即，开始P2P扫描
   console.info("start discover devices -> " + wifiManager.startDiscoverDevices());
   ```
7. 错误码请参见[WIFI错误码](../harmonyos-references/errorcode-wifi.md)。

### 获取对端IP以及Socket通信

1. import需要的Wi-Fi模块。
2. 开启设备的Wi-Fi。
3. 需要SystemCapability.Communication.WiFi.P2P系统能力。
4. 通过[wifiP2pLinkedInfo.connectState](../harmonyos-references/js-apis-wifimanager.md#p2pconnectstate)获取P2P连接状态，确保连接状态为CONNECTED。
5. 通过[wifiP2pGroupInfo.goIpAddress](../harmonyos-references/js-apis-wifimanager.md#wifip2pgroupinfo)获取群组IP地址，以便Socket通信。
6. Socket通信请参考[使用Socket访问网络](socket-connection.md)。
