---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sta-development-guide
title: STA模式开发指南
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > WLAN > STA模式开发指南
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:43+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c779748ae1087676dc4986d3b59a969d7d4f5eae761d55a1da28b10209679659
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

   ```
   1. import { wifiManager } from '@kit.ConnectivityKit';

   3. let recvPowerNotifyFunc: (result: number) => void = (result: number) => {
   4. let wifiState = "";
   5. switch (result) {
   6. case 0:
   7. wifiState += 'DISABLED';
   8. break;
   9. case 1:
   10. wifiState += 'ENABLED';
   11. break;
   12. case 2:
   13. wifiState += 'ENABLING';
   14. break;
   15. case 3:
   16. wifiState += 'DISABLING';
   17. break;
   18. default:
   19. wifiState += 'UNKNOWN STATUS';
   20. break;
   21. }
   22. console.info(`Wi-Fi state changed: ${wifiState}`);
   23. };
   24. try {
   25. wifiManager.on("wifiStateChange", recvPowerNotifyFunc);
   26. let isWifiActive = wifiManager.isWifiActive();
   27. if (!isWifiActive) {
   28. console.info("Wi-Fi not enabled. Skipping monitor.");
   29. } else {
   30. console.info("Wi-Fi is enabled. Starting monitor...");
   31. }
   32. } catch (error) {
   33. console.error(`WiFi state monitor failed: ${error.message}`);
   34. } finally {
   35. try {
   36. wifiManager.off("wifiStateChange", recvPowerNotifyFunc);
   37. console.info("Wi-Fi monitor off: listener removed.");
   38. } catch (e) {
   39. console.error(`WiFi state monitor failed. ${e.message}`);
   40. }
   41. }
   ```

### 建立Wi-Fi连接

1. 导入需要的Wi-Fi模块。
2. 开启设备的Wi-Fi。
3. 需要SystemCapability.Communication.WiFi.STA系统能力。
4. 需要申请权限ohos.permission.GET\_WIFI\_INFO，ohos.permission.SET\_WIFI\_INFO。
5. 示例代码：

   ```
   1. import { wifiManager } from '@kit.ConnectivityKit';

   3. try {
   4. let recvWifiConnectionChangeFunc = (result: number) => {
   5. console.info("Receive wifi connection change event: " + result);
   6. }

   8. let config: wifiManager.WifiDeviceConfig = {
   9. ssid: "****",
   10. bssid: "****",
   11. preSharedKey: "****",
   12. securityType: 0
   13. }

   15. // 更新当前Wi-Fi连接状态
   16. wifiManager.on("wifiConnectionChange", recvWifiConnectionChangeFunc);
   17. // 添加候选网络配置
   18. wifiManager.addCandidateConfig(config).then(result => {
   19. // 连接指定网络
   20. wifiManager.connectToCandidateConfig(result);
   21. });

   23. if (!wifiManager.isConnected()) {
   24. console.info("Wi-Fi not connected");
   25. }
   26. // 获取连接信息
   27. wifiManager.getLinkedInfo().then(data => {
   28. console.info("get Wi-Fi linked info: " + JSON.stringify(data));
   29. })
   30. // 查询信号强度
   31. let rssi = -88;
   32. let band = 1;
   33. let level = wifiManager.getSignalLevel(rssi, band);
   34. console.info("level:" + JSON.stringify(level));

   36. // 取消注册，停止更新当前Wi-Fi连接状态
   37. wifiManager.off("wifiConnectionChange", recvWifiConnectionChangeFunc);
   38. } catch (error) {
   39. console.error(`WiFi Connection failed. ${error.message}`);
   40. }
   ```
6. Wi-Fi连接状态值，详情请参考[ConnState](../harmonyos-references/js-apis-wifimanager.md#connstate)。
7. 错误码详情请参见[WIFI错误码](../harmonyos-references/errorcode-wifi.md)。
