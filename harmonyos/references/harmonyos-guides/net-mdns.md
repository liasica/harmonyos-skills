---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-mdns
title: 使用MDNS访问局域网服务
breadcrumb: 指南 > 系统 > 网络 > Network Kit（网络服务） > 访问网络 > 使用MDNS访问局域网服务
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ed0d730bb0fcd433bd78a843f62f1087f8cfb9f62474eba6385f62597eec864d
---

## 简介

MDNS即多播DNS（Multicast DNS），提供局域网内的本地服务添加、移除、发现、解析等能力。

* 本地服务：局域网内服务的提供方，比如打印机、扫描仪等。

MDNS管理的典型场景有：

* 管理本地服务，通过对本地服务的创建，删除和解析等管理本地服务。
* 发现本地服务，通过[DiscoveryService](../harmonyos-references/js-apis-net-mdns.md#discoveryservice)对象，对指定类型的本地服务状态变化进行监听。

说明

为了保证应用的运行效率，大部分API调用都是异步的，对于异步调用的API均提供了callback和Promise两种方式，以下示例均采用promise函数，更多方式可以查阅[@ohos.net.mdns (MDNS管理)](../harmonyos-references/js-apis-net-mdns.md)。

以下分别介绍具体开发方式。

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

## 管理本地服务

1. 设备连接WiFi。
2. 从@kit.NetworkKit里导入mdns、错误码、以及[common命名空间](../harmonyos-references/js-apis-app-ability-common.md)。

   ```
   1. // 从@kit.NetworkKit中导入mdns命名空间。
   2. import { mdns } from '@kit.NetworkKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { common } from '@kit.AbilityKit';
   5. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/MDNS_case/entry/src/main/ets/pages/Index.ets#L16-L22)
3. 调用[addLocalService](../harmonyos-references/js-apis-net-mdns.md#mdnsaddlocalservice-1)方法，添加本地服务。

   ```
   1. // 建立LocalService对象。
   2. private localServiceInfo: mdns.LocalServiceInfo = {
   3. serviceType: '_print._tcp',
   4. serviceName: 'servicename',
   5. port: 5555,
   6. host: {
   7. address: '127.0.0.1'
   8. },
   9. serviceAttribute: [{ key: '111', value: [1] }]
   10. };
   11. // ...
   12. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   13. // addLocalService添加本地服务。
   14. mdns.addLocalService(context, this.localServiceInfo).then((data) => {
   15. // ...
   16. hilog.info(0x0000, 'testTag', `Local Service Added: ${JSON.stringify(data)}`);
   17. })
   18. // ...
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/MDNS_case/entry/src/main/ets/pages/Index.ets#L169-L199)
4. 通过[resolveLocalService](../harmonyos-references/js-apis-net-mdns.md#mdnsresolvelocalservice-1)方法，解析本地网络的IP地址（非必要，根据需求使用）。

   ```
   1. // resolveLocalService解析本地服务对象（非必要，根据需求使用）。
   2. mdns.resolveLocalService(context, this.localServiceInfo).then((data: mdns.LocalServiceInfo) => {
   3. // ...
   4. hilog.info(0x0000, 'testTag', `Resolved Local Service: ${JSON.stringify(data)}`);
   5. })
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/MDNS_case/entry/src/main/ets/pages/Index.ets#L204-L212)
5. 通过[removeLocalService](../harmonyos-references/js-apis-net-mdns.md#mdnsremovelocalservice-1)方法，移除本地服务。

   ```
   1. // removeLocalService移除本地服务。
   2. mdns.removeLocalService(context, this.localServiceInfo).then((data: mdns.LocalServiceInfo) => {
   3. // ...
   4. hilog.info(0x0000, 'testTag', `Local Service Removed: ${JSON.stringify(data)}`);
   5. })
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/MDNS_case/entry/src/main/ets/pages/Index.ets#L224-L232)

## 发现本地服务

1. 设备连接WiFi。
2. 从@kit.NetworkKit里导入mdns的命名空间。

   ```
   1. // 从@kit.NetworkKit中导入mdns命名空间。
   2. import { mdns } from '@kit.NetworkKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { common } from '@kit.AbilityKit';
   5. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/MDNS_case/entry/src/main/ets/pages/Index.ets#L16-L22)
3. 创建[DiscoveryService](../harmonyos-references/js-apis-net-mdns.md#mdnscreatediscoveryservice)对象，用于发现指定服务类型的MDNS服务。

   ```
   1. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

   3. // ...
   4. // 创建DiscoveryService对象，用于发现指定服务类型的MDNS服务。
   5. let serviceType = '_print._tcp';
   6. let discoveryService = mdns.createDiscoveryService(context, serviceType);
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/MDNS_case/entry/src/main/ets/pages/Index.ets#L240-L254)
4. 订阅MDNS服务发现相关状态变化。

   ```
   1. // 订阅MDNS服务发现相关状态变化。
   2. discoveryService.on('discoveryStart', (data: mdns.DiscoveryEventInfo) => {
   3. hilog.info(0x0000, 'testTag', JSON.stringify(data));
   4. });
   5. discoveryService.on('discoveryStop', (data: mdns.DiscoveryEventInfo) => {
   6. hilog.info(0x0000, 'testTag', JSON.stringify(data));
   7. });
   8. discoveryService.on('serviceFound', (data: mdns.LocalServiceInfo) => {
   9. hilog.info(0x0000, 'testTag', JSON.stringify(data));
   10. // ...
   11. });
   12. discoveryService.on('serviceLost', (data: mdns.LocalServiceInfo) => {
   13. hilog.info(0x0000, 'testTag', JSON.stringify(data));
   14. // ...
   15. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/MDNS_case/entry/src/main/ets/pages/Index.ets#L262-L282)
5. 启动搜索局域网内的MDNS服务。

   ```
   1. // 启动搜索局域网内的MDNS服务。
   2. discoveryService.startSearchingMDNS();
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/MDNS_case/entry/src/main/ets/pages/Index.ets#L285-L288)
6. 停止搜索局域网内的MDNS服务。

   ```
   1. // 停止搜索局域网内的MDNS服务。
   2. discoveryService.stopSearchingMDNS();
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/MDNS_case/entry/src/main/ets/pages/Index.ets#L303-L306)
7. 取消订阅的MDNS服务。

   ```
   1. // 取消订阅的MDNS服务。
   2. discoveryService.off('discoveryStart', (data: mdns.DiscoveryEventInfo) => {
   3. hilog.info(0x0000, 'testTag', JSON.stringify(data));
   4. });
   5. discoveryService.off('discoveryStop', (data: mdns.DiscoveryEventInfo) => {
   6. hilog.info(0x0000, 'testTag', JSON.stringify(data));
   7. });
   8. discoveryService.off('serviceFound', (data: mdns.LocalServiceInfo) => {
   9. hilog.info(0x0000, 'testTag', JSON.stringify(data));
   10. // ...
   11. });
   12. discoveryService.off('serviceLost', (data: mdns.LocalServiceInfo) => {
   13. hilog.info(0x0000, 'testTag', JSON.stringify(data));
   14. // ...
   15. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/MDNS_case/entry/src/main/ets/pages/Index.ets#L308-L328)
