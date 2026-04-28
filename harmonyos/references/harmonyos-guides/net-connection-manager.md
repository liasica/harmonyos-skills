---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-connection-manager
title: 管理网络连接
breadcrumb: 指南 > 系统 > 网络 > Network Kit（网络服务） > 连接网络 > 管理网络连接
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:30a1ea934d6d825a43033baf3acc1dbf71484f39579fa8b53cdeef1bd147007c
---

## 简介

网络连接管理提供管理网络的一些基础能力，包括WiFi/蜂窝/Ethernet等多网络连接优先级管理、网络质量评估、订阅默认/指定网络连接状态变化、查询网络连接信息、DNS解析等功能。

说明

为了保证应用的运行效率，大部分API调用都是异步的，对于异步调用的API，均提供了callback和Promise两种方式，以下示例均采用promise函数，更多方式可以查阅[@ohos.net.connection (网络连接管理)](../harmonyos-references/js-apis-net-connection.md)。

## 基本概念

* 网络生产者：数据网络的提供方。例如WiFi、蜂窝、Ethernet等。
* 网络消费者：数据网络的使用方。例如应用或系统服务。
* 网络探测：检测网络有效性，避免将网络从可用网络切换到不可用网络。包括绑定网络探测、DNS探测、HTTP探测及HTTPS探测。
* 网络优选：处理多网络共存时选择最优网络。在网络状态、网络信息及评分发生变化时被触发。
* 默认网络：系统默认使用的网络。由系统决定，与应用是否指定网络无关，通常为WIFI /蜂窝/以太网/蓝牙其中之一。
* 网络句柄：网络的唯一标识。

## 场景介绍

网络连接管理的典型场景如下所示。

* 接收指定网络的状态变化通知。
* 获取所有注册的网络。
* 查询默认网络或者指定网络的连接信息。
* 使用默认网络解析域名，获取所有IP。

具体开发方式介绍如下。

## 接收指定网络的状态变化通知

1. 声明接口调用所需要的权限：ohos.permission.GET\_NETWORK\_INFO。

   此权限级别为normal，在申请权限前，请保证符合[权限使用的基本原则](app-permission-mgmt-overview.md#权限使用的基本原则)。然后参考[访问控制-声明权限](declare-permissions.md)声明对应权限。
2. 从@kit.NetworkKit中导入connection命名空间。

   ```
   1. // 引入包名。
   2. import { connection } from '@kit.NetworkKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [ConnectNetworkBtn.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetConnection_Manage_case/entry/src/main/ets/pages/ConnectNetworkBtn.ets#L16-L21)
3. 调用[createNetConnection](../harmonyos-references/js-apis-net-connection.md#connectioncreatenetconnection)方法，指定网络能力、网络类型和超时时间(可选，如不传入代表默认网络；创建不同于默认网络时可通过指定这些参数完成)，创建一个NetConnection对象。

   ```
   1. let netSpecifier: connection.NetSpecifier = {
   2. netCapabilities: {
   3. // 假设当前默认网络是蜂窝网络连接，需要创建WIFI网络连接，可指定网络类型为WIFI
   4. bearerTypes: [connection.NetBearType.BEARER_WIFI],
   5. // 指定网络能力为Internet
   6. networkCap: [connection.NetCap.NET_CAPABILITY_INTERNET],
   7. }
   8. };

   10. // 指定超时时间为10s(默认值为0)
   11. let TIMEOUT = 10 * NETWORK_CONNECTION_TIMEOUT;

   13. // 创建NetConnection对象
   14. let conn = connection.createNetConnection(netSpecifier, TIMEOUT);
   ```

   [ConnectNetworkBtn.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetConnection_Manage_case/entry/src/main/ets/pages/ConnectNetworkBtn.ets#L28-L43)
4. 调用该对象的[on()](../harmonyos-references/js-apis-net-connection.md#onnetavailable)方法，传入type和callback，订阅关心的事件。

   ```
   1. // 订阅事件，如果当前指定网络可用，通过on_netAvailable通知用户
   2. conn.on('netAvailable', (data: connection.NetHandle) => {
   3. hilog.info(0x0000, 'testTag', 'Network available, NetId is ' + data.netId);
   4. // ...
   5. });

   7. // 订阅事件，如果当前指定网络不可用，通过on_netUnavailable通知用户
   8. conn.on('netUnavailable', (data: void) => {
   9. hilog.info(0x0000, 'testTag', 'Network unavailable, data is ' + JSON.stringify(data));
   10. // ...
   11. });
   12. // 订阅网络能力变化事件，如果当前指定网络的能力发生变化，通过on_netCapabilitiesChange通知用户
   13. conn.on('netCapabilitiesChange', (data: connection.NetCapabilityInfo) => {
   14. hilog.info(0x0000, 'testTag', 'Network netCapabilitiesChange, data is ' + JSON.stringify(data));
   15. // ...
   16. });

   18. // 订阅网络连接信息变化事件，如果当前指定网络的连接信息发生变化，通过on_netConnectionPropertiesChange通知用户
   19. conn.on('netConnectionPropertiesChange', (data: connection.NetConnectionPropertyInfo) => {
   20. hilog.info(0x0000, 'testTag', 'Network netConnectionPropertiesChange, data is ' + JSON.stringify(data));
   21. // ...
   22. });

   24. // 订阅网络丢失事件，如果当前处于连接状态的指定网络断开，通过on_netLost通知用户
   25. conn.on('netLost', (data: connection.NetHandle) => {
   26. hilog.info(0x0000, 'testTag', 'Network netLost, data is ' + JSON.stringify(data));
   27. // ...
   28. });
   ```

   [ConnectNetworkBtn.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetConnection_Manage_case/entry/src/main/ets/pages/ConnectNetworkBtn.ets#L79-L95)
5. 调用该对象的[register()](../harmonyos-references/js-apis-net-connection.md#register)方法，订阅指定网络状态变化的通知。当网络可用时，会触发netAvailable事件的回调；当网络从连接到断开时，会触发netLost事件的回调；当网络连接信息变化时（例如linkAddresses增加V6地址），会触发netConnectionPropertiesChange事件回调；当网络能力发生变化时（例如网络的连通性发生变化），会触发netCapabilitiesChange回调。

   ```
   1. // 订阅连接状态变化
   2. conn.register((err: BusinessError, data: void) => {
   3. // ...
   4. hilog.error(0x0000, 'testTag', 'Error occurred during connection:', JSON.stringify(err));
   5. // ...
   6. });
   ```

   [ConnectNetworkBtn.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetConnection_Manage_case/entry/src/main/ets/pages/ConnectNetworkBtn.ets#L97-L110)
6. 当不使用该网络时，可以调用该对象的[unregister()](../harmonyos-references/js-apis-net-connection.md#unregister)方法，取消订阅。

   ```
   1. // 当不使用该网络时，可以调用该对象的unregister()方法，取消订阅。
   2. conn.unregister((err: BusinessError, data: void) => {
   3. if (err) {
   4. hilog.error(0x0000, 'testTag', 'Error occurred during unsubscription:', JSON.stringify(err));
   5. } else {
   6. // ...
   7. hilog.info(0x0000, 'testTag', 'Network connection disconnected.');
   8. }
   9. });
   ```

   [ConnectNetworkBtn.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetConnection_Manage_case/entry/src/main/ets/pages/ConnectNetworkBtn.ets#L116-L128)

## 监控默认网络变化并主动重建网络连接

根据当前网络状态及网络质量情况，默认网络可能会发生变化，如下所示。

1. 在WiFi弱信号的情况下，默认网络可能会切换到蜂窝网络。
2. 在蜂窝网络状态差的情况下，默认网络可能会切换到WiFi。
3. 关闭WiFi后，默认网络可能会切换到蜂窝网络。
4. 关闭蜂窝网络后，默认网络可能会切换到WiFi。
5. 在WiFi弱信号的情况下，默认网络可能会切换到其他WiFi(存在跨网情况)。
6. 在蜂窝网络状态差的情况下，默认网络可能会切换到其他蜂窝(存在跨网情况)。

本节旨在介绍监控默认网络的变化后，应用报文能够快速迁移到新默认网络上，具体做法如下。

### 导入connection命名空间

```
1. import { connection, socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetConnection_Manage_case/entry/src/main/ets/pages/Index.ets#L17-L21)

### 监控默认网络变化

```
1. const netConnection = connection.createNetConnection();
2. /* 监听默认网络改变 */
3. netConnection.on('netAvailable', (data: connection.NetHandle) => {
4. hilog.info(0x0000, 'testTag', JSON.stringify(data));
5. });
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetConnection_Manage_case/entry/src/main/ets/pages/Index.ets#L41-L47)

### 默认网络变化后重新建立网络连接

**原网络连接使用Socket模块建立连接**

```
1. // 创建socket对象。
2. let sock: socket.TCPSocket = socket.constructTCPSocketInstance();

4. // 原网络连接使用Socket模块建立连接
5. function useSocket() {
6. let netAddress: socket.NetAddress = {
7. address: '192.168.xx.xxx',
8. port: 8080 // 端口号，默认设置为8080
9. };

11. let tcpConnectOptions: socket.TCPConnectOptions = {
12. address: netAddress,
13. timeout: 6000 // 连接超时时间
14. };

16. // 建立socket连接
17. sock.connect(tcpConnectOptions, (err: BusinessError) => {
18. if (err) {
19. hilog.error(0x0000, 'testTag', 'connect fail: '+JSON.stringify(err));
20. // ···
21. return;
22. }
23. hilog.info(0x0000, 'testTag', 'connect success');

25. // 通过socket发送数据
26. let tcpSendOptions: socket.TCPSendOptions = {
27. data: 'Hello, server!'
28. };
29. socketSend(tcpSendOptions);
30. });
31. }

33. // 通过socket发送数据。
34. function socketSend(tcpSendOptions: socket.TCPSendOptions) {
35. sock.send(tcpSendOptions).then(() => {
36. hilog.info(0x0000, 'testTag', 'send success');
37. // ···
38. }).catch((err: BusinessError) => {
39. hilog.error(0x0000, 'testTag', 'send fail');
40. // ···
41. });
42. }

44. function socketTest() {
45. const netConnection = connection.createNetConnection();
46. // 网络切换会导致网络发生中断，原socket失效，故需重新建立socket。
47. netConnection.on('netAvailable', (netHandle: connection.NetHandle) => {
48. hilog.info(0x0000, 'testTag', 'default network changed: ' + JSON.stringify(netHandle));
49. sock.close();
50. sock = socket.constructTCPSocketInstance();
51. // 通过socket发送数据。
52. useSocket();
53. });
54. // ···
55. // 订阅指定网络状态变化的通知。
56. netConnection.register((error: BusinessError) => {
57. if (error) {
58. hilog.error(0x0000, 'testTag', 'register fail: ' + JSON.stringify(error));
59. } else {
60. hilog.info(0x0000, 'testTag', 'register success');
61. }
62. });
63. // ···
64. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetConnection_Manage_case/entry/src/main/ets/pages/Index.ets#L50-L140)

**原网络连接使用Socket Library建立网络连接**

监控到默认网络变化后关闭原有Socket并重新建立Socket连接。

## 获取所有注册的网络

1. 声明接口调用所需要的权限：ohos.permission.GET\_NETWORK\_INFO。

   此权限级别为normal，在申请权限前，请保证符合[权限使用的基本原则](app-permission-mgmt-overview.md#权限使用的基本原则)。然后参考[访问控制-声明权限](declare-permissions.md)声明对应权限。
2. 示例代码

   ```
   1. // 从@kit.NetworkKit中导入connection命名空间。
   2. import { connection } from '@kit.NetworkKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. // ...
   5. // 调用getAllNets,获取所有处于连接状态的网络列表(Array<NetHandle>)
   6. connection.getAllNets().then((data: connection.NetHandle[]) => {
   7. hilog.info(0x0000, 'testTag', 'getAllNets get data: ' + JSON.stringify(data));
   8. if (data) {
   9. // ...
   10. GlobalContext.getContext().netList = data;
   11. // ...
   12. }
   13. });
   ```

   [GetAllNets.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetConnection_Manage_case/entry/src/main/ets/pages/GetAllNets.ets#L16-L100)

## 查询默认网络或者指定网络的连接信息

1. 声明接口调用所需要的权限：ohos.permission.GET\_NETWORK\_INFO。

   此权限级别为normal，在申请权限前，请保证符合[权限使用的基本原则](app-permission-mgmt-overview.md#权限使用的基本原则)。然后参考[访问控制-声明权限](declare-permissions.md)声明对应权限。
2. 查询默认网络或指定网络连接信息代码示例

   通过调用[getDefaultNet](../harmonyos-references/js-apis-net-connection.md#connectiongetdefaultnet)方法，获取默认的数据网络(NetHandle)；调用[getNetCapabilities](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilities)方法，获取该NetHandle对应网络的能力信息。能力信息包含了网络类型(蜂窝网络、Wi-Fi网络、以太网网络等)、网络具体能力等网络信息。也可以调用[getConnectionProperties](../harmonyos-references/js-apis-net-connection.md#connectiongetconnectionproperties)方法，获取该NetHandle对应网络的连接信息。

   ```
   1. // 从@kit.NetworkKit中导入connection命名空间。
   2. import { connection } from '@kit.NetworkKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. // ···
   5. let netHandleInfo:connection.NetHandle|null = null;
   6. // 调用getDefaultNet方法，获取默认的数据网络(NetHandle)
   7. connection.getDefaultNet().then((data: connection.NetHandle) => {
   8. if (data.netId == 0) {
   9. hilog.info(0x0000, 'testTag', `don't have defaultNet`);
   10. // 当前无默认网络时，获取的netHandler的netid为0,属于异常情况，需要额外处理
   11. return;
   12. }
   13. if (data) {
   14. // ···
   15. hilog.info(0x0000, 'testTag', 'getDefaultNet get data: ' + JSON.stringify(data));
   16. // 获取netHandle对应网络的能力信息。能力信息包含了网络类型、网络具体能力等网络信息
   17. netHandleInfo = data;
   18. connection.getNetCapabilities(netHandleInfo).then(
   19. (data: connection.NetCapabilities) => {
   20. hilog.info(0x0000, 'testTag', 'getNetCapabilities get data: ' + JSON.stringify(data));
   21. // 获取网络类型(bearerTypes)
   22. let bearerTypes: Set<number> = new Set(data.bearerTypes);
   23. let bearerTypesNum = Array.from(bearerTypes.values());
   24. for (let item of bearerTypesNum) {
   25. if (item == 0) {
   26. // 蜂窝网络
   27. hilog.info(0x0000, 'testTag', JSON.stringify('BEARER_CELLULAR'));
   28. } else if (item == 1) {
   29. // Wi-Fi网络
   30. hilog.info(0x0000, 'testTag', JSON.stringify('BEARER_WIFI'));
   31. } else if (item == 3) {
   32. // 以太网网络
   33. hilog.info(0x0000, 'testTag', JSON.stringify('BEARER_ETHERNET'));
   34. }
   35. }

   37. // 获取网络具体能力(networkCap)
   38. let itemNumber: Set<number> = new Set(data.networkCap);
   39. let dataNumber = Array.from(itemNumber.values());
   40. for (let item of dataNumber) {
   41. if (item == 0) {
   42. // 表示网络可以访问运营商的MMSC(Multimedia Message Service，多媒体短信服务)发送和接收彩信
   43. hilog.info(0x0000, 'testTag', JSON.stringify('NET_CAPABILITY_MMS'));
   44. } else if (item == 11) {
   45. // 表示网络流量未被计费
   46. hilog.info(0x0000, 'testTag', JSON.stringify('NET_CAPABILITY_NOT_METERED'));
   47. } else if (item == 12) {
   48. // 表示该网络应具有访问Internet的能力，该能力由网络提供者设置
   49. hilog.info(0x0000, 'testTag', JSON.stringify('NET_CAPABILITY_INTERNET'));
   50. } else if (item == 15) {
   51. // 表示网络不使用VPN（Virtual Private Network，虚拟专用网络）
   52. hilog.info(0x0000, 'testTag', JSON.stringify('NET_CAPABILITY_NOT_VPN'));
   53. } else if (item == 16) {
   54. // 表示该网络访问Internet的能力被网络管理成功验证，该能力由网络管理模块设置
   55. hilog.info(0x0000, 'testTag', JSON.stringify('NET_CAPABILITY_VALIDATED'));
   56. }
   57. }
   58. });
   59. }
   60. });

   62. // 获取netHandle对应的网络的连接信息。
   63. connection.getConnectionProperties(netHandleInfo).then((data: connection.ConnectionProperties) => {
   64. hilog.info(0x0000, 'testTag', 'getConnectionProperties get data: ' + JSON.stringify(data));
   65. })
   66. // ···
   ```

   [DefaultNetworkBtn.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetConnection_Manage_case/entry/src/main/ets/pages/DefaultNetworkBtn.ets#L16-L116)
3. 查询所有网络连接信息代码示例

   通过调用[getAllNets](../harmonyos-references/js-apis-net-connection.md#connectiongetallnets)方法，获取所有处于连接状态的网络列表(Array<NetHandle>)。然后遍历获取到的NetHandle数组，分别调用[getNetCapabilities](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilities)方法，获取该NetHandle对应网络的能力信息，能力信息包含了网络类型(蜂窝网络、Wi-Fi网络、以太网网络等)、网络具体能力等网络信息。也可以调用[getConnectionProperties](../harmonyos-references/js-apis-net-connection.md#connectiongetconnectionproperties)方法，获取该NetHandle对应网络的连接信息。

   ```
   1. // 从@kit.NetworkKit中导入connection命名空间。
   2. import { connection } from '@kit.NetworkKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. // ...
   5. getAllNetworks() {
   6. // 调用getAllNets,获取所有处于连接状态的网络列表(Array<NetHandle>)。
   7. connection.getAllNets().then((data: connection.NetHandle[]) => {
   8. hilog.info(0x0000, 'testTag', 'getAllNets get data: ' + JSON.stringify(data));
   9. if (data) {
   10. // ...
   11. let itemNumber: Set<connection.NetHandle> = new Set(data);
   12. let dataNumber = Array.from(itemNumber.values());
   13. for (let item of dataNumber) {
   14. // 循环获取网络列表每个netHandle对应网络的能力信息
   15. connection.getNetCapabilities(item).then((data: connection.NetCapabilities) => {
   16. hilog.info(0x0000, 'testTag', 'getNetCapabilities get data: ' + JSON.stringify(data));
   17. });

   19. // 循环获取网络列表每个netHandle对应的网络的连接信息
   20. connection.getConnectionProperties(item).then((data: connection.ConnectionProperties) => {
   21. hilog.info(0x0000, 'testTag', 'getConnectionProperties get data: ' + JSON.stringify(data));
   22. });
   23. }
   24. }
   25. });
   26. }
   ```

   [AllNetworksBtn.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetConnection_Manage_case/entry/src/main/ets/pages/AllNetworksBtn.ets#L16-L101)

## 判断默认网络是否可以访问互联网

如果应用需要检查当前连接的网络是否可以访问互联网，可参考以下步骤进行判断：

1. 声明接口调用所需要的权限：ohos.permission.GET\_NETWORK\_INFO

   此权限级别为normal，在申请权限前，请保证符合[权限使用的基本原则](app-permission-mgmt-overview.md#权限使用的基本原则)。然后参考[访问控制-声明权限](declare-permissions.md)声明对应权限。
2. 代码示例

   调用[getDefaultNetSync](../harmonyos-references/js-apis-net-connection.md#connectiongetdefaultnetsync9)方法，获取当前默认网络的netHandle，netHandle有效的情况下，调用[getNetCapabilitiesSync](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilitiessync10)方法，获取NetHandle对应网络的能力信息，根据获取到的能力信息，判断networkCap数组中的值判断网络是否可用。

   NET\_CAPABILITY\_CHECKING\_CONNECTIVITY表示在进行连通性判断的过程中，当不处于连通性判断过程中，且networkCap数组中包含NET\_CAPABILITY\_VALIDATED表示网络连通性校验通过，可以访问互联网。

   ```
   1. // 从@kit.NetworkKit中导入connection命名空间。
   2. import { connection } from '@kit.NetworkKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. // ...
   5. // 获取默认激活的数据网络。
   6. let netHandle = connection.getDefaultNetSync();
   7. if (!netHandle || netHandle.netId === 0) {
   8. hilog.error(0x0000, 'testTag', 'getDefaultNetSync fail');
   9. // ...
   10. } else {
   11. hilog.info(0x0000, 'testTag', 'default network: ' + JSON.stringify(netHandle));
   12. // 获取netHandle对应网络的能力信息。
   13. let netCapabilities = connection.getNetCapabilitiesSync(netHandle);
   14. let cap = netCapabilities.networkCap;
   15. hilog.info(0x0000, 'testTag', 'network capabilities: ' + JSON.stringify(netCapabilities));
   16. // 判断网络是否可以访问互联网。
   17. if (cap?.includes(connection.NetCap.NET_CAPABILITY_CHECKING_CONNECTIVITY)) {
   18. // 正在验证网络连通性，请稍后重试。
   19. hilog.info(0x0000, 'testTag', 'default network is checking, please try again later');
   20. } else {
   21. if (cap?.includes(connection.NetCap.NET_CAPABILITY_VALIDATED)) {
   22. // 网络连通性验证成功，当前默认网络可以访问互联网。
   23. hilog.info(0x0000, 'testTag', 'default network is validated');
   24. // ...
   25. } else {
   26. // 网络连通性验证失败，当前默认网络不可以访问互联网。
   27. hilog.info(0x0000, 'testTag', 'default network is not validated');
   28. // ...
   29. }
   30. }
   31. }
   ```

   [DefaultNetSyncBtn.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetConnection_Manage_case/entry/src/main/ets/pages/DefaultNetSyncBtn.ets#L16-L83)

## 使用默认网络解析域名，获取所有IP

1. 声明接口调用所需要的权限：ohos.permission.GET\_NETWORK\_INFO

   此权限级别为normal，在申请权限前，请保证符合[权限使用的基本原则](app-permission-mgmt-overview.md#权限使用的基本原则)。然后参考[访问控制-声明权限](declare-permissions.md)声明对应权限。
2. 代码示例

   调用[getAddressesByName](../harmonyos-references/js-apis-net-connection.md#connectiongetaddressesbyname)方法，使用默认网络解析主机名以获取所有IP地址。

   ```
   1. // 从@kit.NetworkKit中导入connection命名空间。
   2. import { connection } from '@kit.NetworkKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';
   5. // ...
   6. // 使用默认网络解析主机名以获取所有IP地址
   7. connection.getAddressesByName('xxxx').then((data: connection.NetAddress[]) => {
   8. hilog.info(0x0000, 'testTag', 'Successfully retrieved default network IP address: ' + JSON.stringify(data));
   9. // ...
   10. })
   ```

   [DefaultNetworkIPBtn.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetConnection_Manage_case/entry/src/main/ets/pages/DefaultNetworkIPBtn.ets#L16-L64)
