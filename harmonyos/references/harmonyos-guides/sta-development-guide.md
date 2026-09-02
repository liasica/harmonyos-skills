---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sta-development-guide
title: STA模式开发指南
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > WLAN > STA模式开发指南
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:33+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bb0dff8e2d7981ff92228a56300f1fbf776586af64b26b3123dcf7964ca59068
---

## 简介

Wi-Fi STA模式（Station Mode，站点模式）是无线设备作为客户端接入无线局域网（WLAN）的工作模式。在该模式下，设备（如手机、电脑、平板等）通过连接到接入点（AP，Access Point）或无线路由器，实现对网络的访问。

## 场景介绍

* [判断Wi-Fi状态](sta-development-guide.md#判断wi-fi状态)
* [建立Wi-Fi连接](sta-development-guide.md#建立wi-fi连接)

## 接口说明

完整的JS API说明以及示例代码请参考：[STA接口](../harmonyos-references/js-apis-wifimanager.md)。

接口具体说明如下表所示。

| 接口名 | 功能描述 |
| --- | --- |
| isWifiActive() | 查询WLAN开关是否已使能。 |
| addCandidateConfig() | 添加候选网络配置，使用前先使能WLAN。 |
| connectToCandidateConfig() | 应用使用该接口连接到自己添加的候选网络。 |
| isConnected() | 查询WLAN是否已连接。 |
| removeCandidateConfig() | 移除候选网络配置。 |
| getCandidateConfigs() | 获取候选网络配置。 |
| on(type: 'wifiStateChange') | 注册WLAN状态改变事件。 |
| off(type: 'wifiStateChange') | 取消注册WLAN状态改变事件。 |
| on(type: 'wifiConnectionChange') | 注册WLAN连接状态改变事件。 |
| off(type: 'wifiConnectionChange') | 取消注册WLAN连接状态改变事件。 |

## 主要场景开发步骤

### 判断Wi-Fi状态

1. 导入需要的Wi-Fi模块。
2. 需要SystemCapability.Communication.WiFi.STA系统能力。
3. 需要申请权限ohos.permission.GET\_WIFI\_INFO。
4. 开启设备Wi-Fi。
5. 示例代码：

   ```ts
   import { wifiManager } from '@kit.ConnectivityKit';

   let recvPowerNotifyFunc: (result: number) => void = (result: number) => {
     let wifiState = "";
     switch (result) {
       case 0:
         wifiState += 'DISABLED';
         break;
       case 1:
         wifiState += 'ENABLED';
         break;
       case 2:
         wifiState += 'ENABLING';
         break;
       case 3:
         wifiState += 'DISABLING';
         break;
       default:
         wifiState += 'UNKNOWN STATUS';
         break;
     }
     console.info(`Wi-Fi state changed: ${wifiState}`);
   };
   try {
     wifiManager.on("wifiStateChange", recvPowerNotifyFunc);
     let isWifiActive = wifiManager.isWifiActive();
     if (!isWifiActive) {
       console.info("Wi-Fi not enabled. Skipping monitor.");
     } else {
       console.info("Wi-Fi is enabled. Starting monitor...");
     }
   } catch (error) {
     console.error(`WiFi state monitor failed: ${error.message}`);
   } finally {
     try {
       wifiManager.off("wifiStateChange", recvPowerNotifyFunc);
       console.info("Wi-Fi monitor off: listener removed.");
     } catch (e) {
        console.error(`WiFi state monitor failed. ${e.message}`);
     }
   }
   ```

### 建立Wi-Fi连接

1. 导入需要的Wi-Fi模块。
2. 开启设备的Wi-Fi。
3. 需要SystemCapability.Communication.WiFi.STA系统能力。
4. 需要申请权限ohos.permission.GET\_WIFI\_INFO，ohos.permission.SET\_WIFI\_INFO。
5. 示例代码：

   ```ts
   import { wifiManager } from '@kit.ConnectivityKit';

   try {
     let recvWifiConnectionChangeFunc = (result: number) => {
       console.info("Receive wifi connection change event: " + result);
     }

     let config: wifiManager.WifiDeviceConfig = {
       ssid: "****",
       bssid: "****",
       preSharedKey: "****",
       securityType: 0
     }

     // 更新当前Wi-Fi连接状态
     wifiManager.on("wifiConnectionChange", recvWifiConnectionChangeFunc);
     // 添加候选网络配置
     wifiManager.addCandidateConfig(config).then(result => {
       // 连接指定网络
       wifiManager.connectToCandidateConfig(result);
     });

     if (!wifiManager.isConnected()) {
       console.info("Wi-Fi not connected");
     }
     // 获取连接信息
     wifiManager.getLinkedInfo().then(data => {
       console.info("get Wi-Fi linked info: " + JSON.stringify(data));
     })
     // 查询信号强度
     let rssi = -88;
     let band = 1;
     let level = wifiManager.getSignalLevel(rssi, band);
     console.info("level:" + JSON.stringify(level));

     // 取消注册，停止更新当前Wi-Fi连接状态
     wifiManager.off("wifiConnectionChange", recvWifiConnectionChangeFunc);
   } catch (error) {
     console.error(`WiFi Connection failed. ${error.message}`);
   }
   ```
6. Wi-Fi连接状态值，详情请参考[ConnState](../harmonyos-references/js-apis-wifimanager.md#connstate)。
7. 错误码详情请参见[WIFI错误码](../harmonyos-references/errorcode-wifi.md)。
