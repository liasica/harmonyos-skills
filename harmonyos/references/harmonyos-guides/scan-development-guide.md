---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-development-guide
title: Wi-Fi扫描开发指南
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > WLAN > Wi-Fi扫描开发指南
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:44+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9eeecfc26259d88b9c879c8f748d092d8895422ba1b202a98fbd1fc40c344ecc
---

## 简介

Wi-Fi扫描是指设备（如手机、电脑、路由器等）搜索周围可用Wi-Fi网络的过程。通过扫描，设备可以获取附近网络的基本信息（如网络名称、信号强度、加密方式等），从而实现连接、管理或分析周围网络。

## 场景介绍

* [Wi-Fi扫描](scan-development-guide.md#wi-fi扫描)
* [PNO扫描](scan-development-guide.md#pno扫描)
* [周期扫描](scan-development-guide.md#周期扫描)
* [扫描管控](scan-development-guide.md#扫描管控)

## 接口说明

完整的JS API说明以及示例代码请参考：[SCAN接口](../harmonyos-references/js-apis-wifimanager.md)。

接口具体说明如下表所示。

| 接口名 | 功能描述 |
| --- | --- |
| getScanInfoList() | 获取扫描结果。 |
| on(type: 'wifiScanStateChange') | 注册扫描状态改变事件。 |
| off(type: 'wifiScanStateChange') | 取消注册扫描状态改变事件。 |

## 开发步骤

### Wi-Fi扫描

1. 导入需要的Wi-Fi模块。
2. 需要SystemCapability.Communication.WiFi.STA系统能力。
3. 需要权限ohos.permission.GET\_WIFI\_INFO。
4. 开启设备的Wi-Fi。
5. 示例代码：

   说明

   主动扫描接口，从API version 10开始废弃。替代接口仅向系统应用开放。

   ```
   1. import { wifiManager } from '@kit.ConnectivityKit';

   3. try {
   4. let recvWifiScanStateChangeFunc = (result:number) => {
   5. console.info("Receive Wifi scan state change event: " + result);
   6. }

   8. // 获取扫描状态 0：扫描失败；1：扫描成功。
   9. wifiManager.on("wifiScanStateChange", recvWifiScanStateChangeFunc);

   11. let isWifiActive = wifiManager.isWifiActive();
   12. if (!isWifiActive) {
   13. console.error("wifi not enable"); // 请先手动打开WiFi
   14. return;
   15. }

   17. let scanInfoList = wifiManager.getScanInfoList();

   19. let len = scanInfoList.length;
   20. console.info("wifi received scan info: " + len);
   21. if(len > 0){
   22. for (let i = 0; i < len; ++i) {
   23. console.info("ssid: " + scanInfoList[i].ssid);
   24. console.info("bssid: " + scanInfoList[i].bssid);
   25. console.info("capabilities: " + scanInfoList[i].capabilities);
   26. console.info("securityType: " + scanInfoList[i].securityType);
   27. console.info("rssi: " + scanInfoList[i].rssi);
   28. console.info("band: " + scanInfoList[i].band);
   29. console.info("frequency: " + scanInfoList[i].frequency);
   30. console.info("channelWidth: " + scanInfoList[i].channelWidth);
   31. console.info("timestamp: " + scanInfoList[i].timestamp);
   32. console.info("supportedWifiCategory: " + scanInfoList[i].supportedWifiCategory);
   33. console.info("isHiLinkNetwork: " + scanInfoList[i].isHiLinkNetwork);
   34. }
   35. }

   37. // 取消注册，停止获取扫描状态。
   38. wifiManager.off("wifiScanStateChange", recvWifiScanStateChangeFunc);
   39. } catch (error) {
   40. console.error(`WiFi scan fail. ${error.message}`);
   41. }
   ```
6. 错误码详情请参见[WIFI错误码](../harmonyos-references/errorcode-wifi.md)。

### PNO扫描

PNO扫描即首选分流网络扫描（Preferred Network Offload scanning），是一种用于降低移动设备功耗的Wi-Fi扫描技术。

触发PNO扫描条件：当设备未连接Wi-Fi且屏幕关闭后，会触发PNO扫描，支持设备在后台寻找并连接首选的Wi-Fi网络。

### 周期扫描

WiFi周期扫描是指无线设备（如智能手机、平板电脑、笔记本电脑等）按照一定的时间间隔，自动搜索周围可用的WiFi网络的过程。

触发场景描述：

1. 设备亮屏且与Wi-Fi已连接：判断当前链路是否支持上网。支持上网，扫描间隔1h；不支持上网，判断是否静止，静止场景下扫描周期从20s开始倍增，最大300s；非静止场景扫描周期从20s开始，最大160s。
2. 设备亮屏且与Wi-Fi未连接：静止场景扫描周期从20s开始倍增，最大300s；非静止场景扫描周期从20s开始，最大160s。

### 扫描管控

WiFi扫描管控是指对无线设备扫描WiFi网络的行为进行管理和控制。

以下是一些常见的管控方式和应用场景：

1. WiFi在关闭的情况下不触发周期扫描和PNO扫描。
2. WiFi连接过程中不允许触发扫描。
3. 前台应用2分钟内最多发起4次扫描。
4. 设备温度达到阈值，设备扫描会被管控。
5. 扫描接口从API version 9开始支持，从API version 10开始废弃，替代接口仅向系统应用开放。
6. 扫描结果获取真实bssid，需要申请ohos.permission.GET\_WIFI\_PEERS\_MAC权限。
