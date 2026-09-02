---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-statistics
title: 统计网络流量消耗
breadcrumb: 指南 > 系统 > 网络 > Network Kit（网络服务） > 管理网络 > 统计网络流量消耗
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ecf86d42e489bb01afeedb15601d74552a9f2c207b13ac196dcd00085ce8062b
---

## 简介

流量管理提供了基于物理网络的数据流量统计能力，支持基于网卡/UID的流量统计。

流量管理主要实现功能有：

* 支持基于网卡的流量统计。
* 支持基于应用UID的流量统计。

  > \*\*说明：\*\* > > - 为了保证应用的运行效率，大部分API调用都是异步的，对于异步调用的API均提供了callback和Promise两种方式，以下示例均采用Promise函数，更多方式可以查阅[@ohos.net.statistics (流量管理)](../reference/apis-network-kit/js-apis-net-statistics.md)。 > - 上行流量是指由终端设备向网络侧发送的数据量，下行流量是指由网络侧向终端设备发起传输的数据量。

以下分别介绍具体开发方式。

## 开发步骤

1. 导入[statistics](../harmonyos-references/js-apis-net-statistics.md)、[socket](../harmonyos-references/js-apis-socket.md)以及错误码模块。

   ```typescript
   import { socket, statistics } from '@kit.NetworkKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 获取指定网卡流量数据。

   分别调用[getIfaceRxBytes](../harmonyos-references/js-apis-net-statistics.md#statisticsgetifacerxbytes-1)和[getIfaceTxBytes](../harmonyos-references/js-apis-net-statistics.md#statisticsgetifacetxbytes-1)接口传入网卡名获取指定网卡从最近一次开机至今的下行和上行流量数据。

   ```typescript
     // wlan0为主WiFi网卡名，获取主WiFi实时下行流量数据。
     statistics.getIfaceRxBytes('wlan0').then((stats: number) => {
       hilog.info(0x0000, 'testTag', JSON.stringify(stats));
       // ...
     })
     .catch((err: BusinessError) => {
       hilog.error(0x0000, 'testTag', JSON.stringify(err));
       // ...
     });
     // ...
     // wlan0为主WiFi网卡名，获取主WiFi实时上行流量数据。
     statistics.getIfaceTxBytes('wlan0').then((stats: number) => {
       hilog.info(0x0000, 'testTag', JSON.stringify(stats));
       // ...
     })
     .catch((err: BusinessError) => {
       hilog.error(0x0000, 'testTag', JSON.stringify(err));
       // ...
     });
   // ...
   ```
3. 获取蜂窝流量数据。

   分别调用[getCellularRxBytes](../harmonyos-references/js-apis-net-statistics.md#statisticsgetcellularrxbytes-1)和[getCellularTxBytes](../harmonyos-references/js-apis-net-statistics.md#statisticsgetcellulartxbytes-1)接口获取从最近一次开机至今的蜂窝下行和上行流量数据。

   ```typescript
   // 获取蜂窝实时下行流量数据。
   statistics.getCellularRxBytes().then((stats: number) => {
     hilog.info(0x0000, 'testTag', JSON.stringify(stats));
     // ...
   })
   // ...
   // 获取蜂窝实时上行流量数据。
   statistics.getCellularTxBytes().then((stats: number) => {
     hilog.info(0x0000, 'testTag', JSON.stringify(stats));
     // ...
   })
   // ...
   ```
4. 获取所有网卡流量数据。

   分别调用[getAllRxBytes](../harmonyos-references/js-apis-net-statistics.md#statisticsgetallrxbytes-1)和[getAllTxBytes](../harmonyos-references/js-apis-net-statistics.md#statisticsgetalltxbytes-1)接口获取所有网卡从最近一次开机到现在的下行和上行流量数据。

   ```typescript
   // 获取所有网卡实时下行流量数据。
   statistics.getAllRxBytes().then((stats: number) => {
     hilog.info(0x0000, 'testTag', JSON.stringify(stats));
     // ...
   })
   // ...
   // 获取所有网卡实时上行流量数据。
   statistics.getAllTxBytes().then((stats: number) => {
     hilog.info(0x0000, 'testTag', JSON.stringify(stats));
     // ...
   })
   // ...
   ```
5. 获取指定应用流量数据。

   分别调用[getUidRxBytes](../harmonyos-references/js-apis-net-statistics.md#statisticsgetuidrxbytes-1)和[getUidTxBytes](../harmonyos-references/js-apis-net-statistics.md#statisticsgetuidtxbytes-1)接口，传入UID获取指定应用从最近一次开机至今的下行和上行流量数据。

   此处仅以应用UID为20010038为例，实际调用时需修改为真实UID。

   ```ts
    let UID = 20010038;
   ```

   ```typescript
   // 获取指定应用实时下行流量数据。
   // ...
   statistics.getUidRxBytes(UID).then((stats: number) => {
     hilog.info(0x0000, 'testTag', JSON.stringify(stats));
     // ...
   })
   // ...
   // 获取指定应用实时上行流量数据。
   // ...
   statistics.getUidTxBytes(UID).then((stats: number) => {
     hilog.info(0x0000, 'testTag', JSON.stringify(stats));
     // ...
   })
   // ...
   ```
6. 获取指定Socket流量数据。

   分别调用[getSockfdRxBytes](../harmonyos-references/js-apis-net-statistics.md#statisticsgetsockfdrxbytes11-1)和[getSockfdTxBytes](../harmonyos-references/js-apis-net-statistics.md#statisticsgetsockfdtxbytes11-1)接口，传入Socket FD获取指定Socket的下行和上行流量数据。

   ```typescript
   // 获取指定socket实时下行流量数据。
   let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
   // ...
   tcp.getSocketFd().then((sockfd: number) => {
     statistics.getSockfdRxBytes(sockfd).then((stats: number) => {
       hilog.info(0x0000, 'testTag', JSON.stringify(stats));
       // ...
     }).catch((err: BusinessError) => {
       hilog.error(0x0000, 'testTag', JSON.stringify(err));
       // ...
     });
   })
   // ...
   // 获取指定socket实时上行流量数据。
   tcp.getSocketFd().then((sockfd: number) => {
     statistics.getSockfdTxBytes(sockfd).then((stats: number) => {
       hilog.info(0x0000, 'testTag', JSON.stringify(stats));
       // ...
     }).catch((err: BusinessError) => {
       hilog.error(0x0000, 'testTag', JSON.stringify(err));
       // ...
     });
   })
   // ...
   ```
