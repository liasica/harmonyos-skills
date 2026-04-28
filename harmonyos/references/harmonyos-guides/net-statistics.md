---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-statistics
title: 统计网络流量消耗
breadcrumb: 指南 > 系统 > 网络 > Network Kit（网络服务） > 管理网络 > 统计网络流量消耗
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1479cb539dcfd36beea51c458a4d3a6b79ae84a027322b9f0cbb48726417704f
---

## 简介

流量管理提供了基于物理网络的数据流量统计能力，支持基于网卡/UID 的流量统计。

流量管理主要实现功能有：

* 支持基于网卡/UID 的实时流量统计。
* 支持基于网卡/UID 的历史流量统计。
* 支持基于网卡/UID 的流量变化订阅。

说明

为了保证应用的运行效率，大部分 API 调用都是异步的，对于异步调用的 API 均提供了 callback 和 Promise 两种方式，以下示例均采用 Promise 函数，更多方式可以查阅[@ohos.net.statistics (流量管理)](../harmonyos-references/js-apis-net-statistics.md)。

以下分别介绍具体开发方式。

## 开发步骤

1. 导入[statistics](../harmonyos-references/js-apis-net-statistics.md)、[socket](../harmonyos-references/js-apis-socket.md)以及错误码模块。

   ```
   1. import { socket, statistics } from '@kit.NetworkKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/FlowManagement_case/entry/src/main/ets/pages/Index.ets#L16-L20)
2. 获取指定网卡实时流量数据

   调用[getIfaceRxBytes](../harmonyos-references/js-apis-net-statistics.md#statisticsgetifacerxbytes-1)接口传入网卡名获取实时下行流量数据。

   ```
   1. // wlan0为主WiFi网卡名，获取主WiFi实时下行流量数据。
   2. statistics.getIfaceRxBytes('wlan0').then((stats: number) => {
   3. hilog.info(0x0000, 'testTag', JSON.stringify(stats));
   4. // ...
   5. })
   6. .catch((err: BusinessError) => {
   7. hilog.error(0x0000, 'testTag', JSON.stringify(err));
   8. // ...
   9. });
   10. // ...
   11. // wlan0为主WiFi网卡名，获取主WiFi实时上行流量数据。
   12. statistics.getIfaceTxBytes('wlan0').then((stats: number) => {
   13. hilog.info(0x0000, 'testTag', JSON.stringify(stats));
   14. // ...
   15. })
   16. .catch((err: BusinessError) => {
   17. hilog.error(0x0000, 'testTag', JSON.stringify(err));
   18. // ...
   19. });
   20. // ...
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/FlowManagement_case/entry/src/main/ets/pages/Index.ets#L178-L213)
3. 获取蜂窝实时流量数据

   调用[getCellularRxBytes](../harmonyos-references/js-apis-net-statistics.md#statisticsgetcellularrxbytes-1)接口获取蜂窝实时上下行流量数据。

   ```
   1. // 获取蜂窝实时下行流量数据。
   2. statistics.getCellularRxBytes().then((stats: number) => {
   3. hilog.info(0x0000, 'testTag', JSON.stringify(stats));
   4. // ...
   5. })
   6. // ...
   7. // 获取蜂窝实时上行流量数据。
   8. statistics.getCellularTxBytes().then((stats: number) => {
   9. hilog.info(0x0000, 'testTag', JSON.stringify(stats));
   10. // ...
   11. })
   12. // ...
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/FlowManagement_case/entry/src/main/ets/pages/Index.ets#L216-L245)
4. 获取所有网卡实时流量数据

   调用[getAllRxBytes](../harmonyos-references/js-apis-net-statistics.md#statisticsgetallrxbytes-1)接口获取所有网卡实时上下行流量数据。

   ```
   1. // 获取所有网卡实时下行流量数据。
   2. statistics.getAllRxBytes().then((stats: number) => {
   3. hilog.info(0x0000, 'testTag', JSON.stringify(stats));
   4. // ...
   5. })
   6. // ...
   7. // 获取所有网卡实时上行流量数据。
   8. statistics.getAllTxBytes().then((stats: number) => {
   9. hilog.info(0x0000, 'testTag', JSON.stringify(stats));
   10. // ...
   11. })
   12. // ...
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/FlowManagement_case/entry/src/main/ets/pages/Index.ets#L248-L277)
5. 获取指定应用实时流量数据

   调用[getUidRxBytes](../harmonyos-references/js-apis-net-statistics.md#statisticsgetuidrxbytes-1)接口，传入UID获取指定应用实时上下行流量数据。

   ```
   1. let UID = 20010038;
   ```

   ```
   1. // 获取指定应用实时下行流量数据。
   2. // ...
   3. statistics.getUidRxBytes(UID).then((stats: number) => {
   4. hilog.info(0x0000, 'testTag', JSON.stringify(stats));
   5. // ...
   6. })
   7. // ...
   8. // 获取指定应用实时上行流量数据。
   9. // ...
   10. statistics.getUidTxBytes(UID).then((stats: number) => {
   11. hilog.info(0x0000, 'testTag', JSON.stringify(stats));
   12. // ...
   13. })
   14. // ...
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/FlowManagement_case/entry/src/main/ets/pages/Index.ets#L282-L317)
6. 获取指定socket实时流量数据

   调用[getSockfdRxBytes](../harmonyos-references/js-apis-net-statistics.md#statisticsgetsockfdrxbytes11-1)接口，传入指定的sockFd获取指定socket实时上下行流量数据。

   ```
   1. // 获取指定socket实时下行流量数据。
   2. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
   3. // ...
   4. tcp.getSocketFd().then((sockfd: number) => {
   5. statistics.getSockfdRxBytes(sockfd).then((stats: number) => {
   6. hilog.info(0x0000, 'testTag', JSON.stringify(stats));
   7. // ...
   8. }).catch((err: BusinessError) => {
   9. hilog.error(0x0000, 'testTag', JSON.stringify(err));
   10. // ...
   11. });
   12. })
   13. // ...
   14. // 获取指定socket实时上行流量数据。
   15. tcp.getSocketFd().then((sockfd: number) => {
   16. statistics.getSockfdTxBytes(sockfd).then((stats: number) => {
   17. hilog.info(0x0000, 'testTag', JSON.stringify(stats));
   18. // ...
   19. }).catch((err: BusinessError) => {
   20. hilog.error(0x0000, 'testTag', JSON.stringify(err));
   21. // ...
   22. });
   23. })
   24. // ...
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/FlowManagement_case/entry/src/main/ets/pages/Index.ets#L321-L399)
