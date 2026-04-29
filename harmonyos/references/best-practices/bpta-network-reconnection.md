---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-network-reconnection
title: 应用网络重连
breadcrumb: 最佳实践 > 网络 > 应用网络重连
category: best-practices
scraped_at: 2026-04-29T14:11:05+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:481e9a16f9777310a776c273284c1ce8f97e907a403351c6dd20b71289a54119
---

## 概述

网络重连是指在网络连接出现中断或异常断开的情况下，设备或应用程序重新建立网络连接的过程。对于许多依赖网络的业务和应用来说，网络重连能够确保在网络出现短暂中断后，业务能够快速恢复，减少因网络故障导致的业务中断时间，提高业务的连续性和可靠性。例如，在线金融交易、远程医疗、音视频播放等对实时性和连续性要求较高的业务，网络重连功能至关重要。根据应用的实际场景，网络重连可以分为以下多种方式。

* [网络超时重连](bpta-network-reconnection.md#section090112944811)：客户端向服务器发送请求后，如果发生网络超时，那么客户端将自动尝试与服务器重新建立连接。
* [网络切换重连](bpta-network-reconnection.md#section4111121185017)：当网络连接发生变化后，客户端应用可能会出现网络异常。应用需要检测网络状态变化，并根据网络状态进行连接。
* [应用前后台切换后重连](bpta-network-reconnection.md#section6593152718515)：应用切换到后台一段时间后，网络资源会被冻结释放，需要客户端重新建立连接。

## 网络超时重连

### 场景描述

在网络请求中，经常会遇到网络波动、服务器宕机等情况，从而导致网络不可用、网络超时等问题。为了减少网络超时等带来的影响，在实际应用开发中经常使用超时机制和重试机制。如HTTP请求列表数据时，设置HTTP连接超时和请求重试。

* 网络超时机制是指在网络通信过程中，当一个操作在规定的时间内没有得到预期的响应或完成时，系统会自动判定该操作失败，并触发相应的处理逻辑。其原理是通过设置一个定时器，从网络操作开始时计时，一旦超过设定的时间阈值，就认为操作超时。
* 重试机制一般配合超时机制一起使用，指的是多次发送相同的请求来避免瞬态故障和偶然性故障。

### 实现原理

网络超时分为网络连接超时和网络读取超时。

* 网络连接超时就是在程序默认的等待时间内没有得到服务器的响应。
* 网络读取超时指客户端在读取服务器响应时等待的时间。

网络重试常用的策略有定时重试、指数退避重试、随机退避重试等。

* 定时重试：设定一个固定的重试次数，当网络请求失败时，在该次数范围内进行重试，每次重试之间的时间间隔可以是固定的，也可以根据具体情况进行调整。例如，设定重试次数为 3 次，每次重试间隔为 2 秒。
* 指数退避重试：每次重试的时间间隔按照指数级增长，如重试间隔时间依次为2、4、8、16等。
* 随机退避重试：每次重试的时间间隔在一个指定的范围内随机取值。例如，设定重试间隔时间在 1 秒到 5 秒之间随机，这样可以避免多个请求同时重试，分散服务器的负载压力，提高整体的重试成功率。

在设置重试策略时，需要根据实际的场景来进行设置，既要考虑网络超时的时间，还需要关注重试的次数和时间间隔，避免网络资源浪费。

### 开发步骤

在HarmonyOS中，在Http、RCP发生错误或者超时后，都可以使用网络超时重连的机制。HTTP超时重连的实现步骤如下所示。

* 设置HTTP请求的读取超时时间、连接超时时间。
* 可以根据网络状态进行判断，然后再进行重连。这样可以在非网络问题的情况下进行重试，可以更精准地控制重试行为，提高请求的成功率和效率。例如，对于一些表示服务错误的响应码（如 500 Internal Server Error、503 Service Unavailable 等），可以进行重试。
* 使用setTimeout进行函数执行延迟，配合使用Promise，进而同步获取网络请求结果。

HTTP超时重连的代码如下所示：

```
1. async getHttpRequest(url: string, retry: number): Promise<number | undefined> {
2. try {
3. return await this.httpRequest?.requestInStream(url,
4. { method: http.RequestMethod.GET, connectTimeout: 6000, readTimeout: 60000 })
5. .then((data: number) => {
6. if (data === 408 || data === 500 && retry > 0) {
7. return new Promise((resolve: Function) => {
8. setTimeout(() => {
9. resolve(this.getHttpRequest(url, retry - 1));
10. }, 2000);
11. });
12. } else {
13. return data;
14. }
15. });
16. } catch (err) {
17. this.isDownload = false;
18. try {
19. this.getUIContext().getPromptAction().showToast({ message: $r('app.string.download_error') });
20. } catch (error) {
21. let err = error as BusinessError;
22. hilog.error(0xFF00, 'NetworkReconnection', `showToast fail, code = ${err.code}, message = ${err.message}`);
23. }
24. return;
25. }
26. }
```

[HTTPReconnection.ets](https://gitcode.com/HarmonyOS_Samples/NetworkReconnection/blob/master/NetworkReconnection/entry/src/main/ets/pages/HTTPReconnection.ets#L130-L155)

RCP超时重连的实现与HTTP的实现步骤类似，RCP超时重连的代码如下所示：

```
1. createRCPSession(): rcp.Session | null {
2. try {
3. const customHttpEventsHandler: rcp.HttpEventsHandler = {
4. onDownloadProgress: (totalSize: number, transferredSize: number) => {
5. this.contentLength = totalSize;
6. this.downloadSize = transferredSize;
7. this.process = this.contentLength === 0 ? 0 : Math.floor(this.downloadSize / this.contentLength * 100);
8. },
9. onDataEnd: () => {
10. this.contentLength = -1;
11. this.downloadSize = 0;
12. },
13. };
14. const sessionConfig: rcp.SessionConfiguration = {
15. requestConfiguration: {
16. transfer: {
17. timeout: {
18. connectMs: 6000,
19. transferMs: 60000
20. }
21. },
22. tracing: { httpEventsHandler: customHttpEventsHandler }
23. }
24. }
25. return rcp.createSession(sessionConfig);
26. } catch (error) {
27. return null;
28. }
29. }

31. // ...

33. async getRcpRequest(url: string, retry: number): Promise<rcp.Response | undefined> {
34. try {
35. if (this.session !== null) {
36. return await this.session.get(url)
37. .then((response) => {
38. if ((response.statusCode === 408 || response.statusCode === 500) && retry > 0) {
39. return new Promise((resolve: Function) => {
40. setTimeout(() => {
41. resolve(this.getRcpRequest(url, retry - 1));
42. }, 2000)
43. })
44. } else {
45. return response;
46. }
47. })
48. } else {
49. return;
50. }
51. } catch (err) {
52. try {
53. this.getUIContext().getPromptAction().showToast({ message: $r('app.string.download_error') });
54. this.isDownload = false;
55. } catch (error) {
56. let err = error as BusinessError;
57. Logger.error('NetworkReconnection', `showToast fail, code = ${err.code}, message = ${err.message}`);
58. }
59. return;
60. }
61. }
```

[RCPReconnection.ets](https://gitcode.com/harmonyos_samples/NetworkReconnection/blob/master/NetworkReconnection/entry/src/main/ets/pages/RCPReconnection.ets#L94-L183)

## 网络切换重连

### 场景描述

在当下这个数字化时代，大部分的应用确实离不开网络，网络已经深度渗透到各类应用场景之中。然而，在网络状态切换后，如何继续保持网络连接是许多应用需要处理的问题。

### 实现原理

网络切换主要分为网络类型切换和无网络与有网络之间的切换。针对网络切换的场景，HarmonyOS提供了[网络连接管理](../harmonyos-references/js-apis-net-connection.md)能力，用于查询网络信息、监听网络连接的变化等。

在实现网络切换重连上，主要包含以下步骤。

* 使用网络连接管理的能力监听网络变化，并使用[AppStorage](../harmonyos-guides/arkts-appstorage.md)存储应用全局网络状态。
* 使用[@StorageProp](../harmonyos-guides/arkts-appstorage.md#storageprop)，将AppStorage存储的网络状态与对应的属性建立单向数据同步。
* 使用[@Watch](../harmonyos-guides/arkts-watch.md)监听状态变量的变化，当状态变量变化后，对网络进行关闭或重连。

### 开发步骤

调用connection的register()方法订阅网络变化通知，同时，订阅netCapabilitiesChange网络能力变化事件，订阅netLost网络丢失事件。在设备从有网络到无网络状态会触发netLost事件，从无网络到有网络会触发netCapabilitiesChange事件。而在网络类型切换时，也会触发netLost事件和netCapabilitiesChange事件，开发者可以根据实际场景需要在netCapabilitiesChange事件中，将网络类型及网络状态存储在AppStorage中。

```
1. private netCon: connection.NetConnection = connection.createNetConnection();

3. register() {
4. this.netCon.register((error: BusinessError) => {
5. Logger.error('net register' + JSON.stringify(error));
6. });
7. }

9. netCapabilitiesChange() {
10. this.netCon.on('netCapabilitiesChange', (data: connection.NetCapabilityInfo) => {
11. let netAvailable = false;
12. data.netCap.networkCap?.forEach((value) => {
13. if (value === connection.NetCap.NET_CAPABILITY_INTERNET) {
14. netAvailable = true;
15. }
16. })
17. Logger.info('ConnectionUtil.netAvailable:' + netAvailable);
18. AppStorage.setOrCreate('netAvailable', netAvailable);
19. })

21. this.netCon.on('netLost', (data: connection.NetHandle) => {
22. AppStorage.setOrCreate('netAvailable', false);
23. Logger.info("WifiChangeListen-- Succeeded to get data: " + JSON.stringify(data));
24. });
25. }
```

[ConnectionUtil.ets](https://gitcode.com/harmonyos_samples/NetworkReconnection/blob/master/NetworkReconnection/entry/src/main/ets/utils/ConnectionUtil.ets#L22-L46)

使用AppStorage存储应用全局网络状态。

```
1. @StorageProp('netAvailable') @Watch('onSocketUpdated') netAvailable: boolean = true;
```

[SocketReconnection.ets](https://gitcode.com/harmonyos_samples/NetworkReconnection/blob/master/NetworkReconnection/entry/src/main/ets/pages/SocketReconnection.ets#L31-L31)

使用@Watch监听状态变量的变化，并根据对应的变化和实际应用场景重新连接网络。

```
1. onSocketUpdated() {
2. this.netAvailable ? this.tcpSocketConnect() : this.tcpSocketDisconnect();
3. Logger.info('netAvailable:' + this.netAvailable);
4. }

6. // ...

8. tcpSocketConnect() {
9. if (!this.netAvailable) {
10. try {
11. this.getUIContext().getPromptAction().showToast({ message: $r('app.string.connect_error') });
12. } catch (error) {
13. let err = error as BusinessError;
14. Logger.error('NetworkReconnection', `showToast fail, code = ${err.code}, message = ${err.message}`);
15. }
16. return;
17. }

19. this.tcp = socket.constructTCPSocketInstance();
20. this.tcp.on('connect', () => {
21. Logger.info('on connect');
22. });
23. this.tcp.on('close', () => {
24. Logger.info('on close');
25. });
26. this.tcp.on('error', (error: BusinessError) => {
27. Logger.error('error:' + error.code + error.message
28. );
29. });
30. const clientIpAddress: socket.NetAddress = {
31. address: CommonConstants.IP_ADDRESS,
32. port: CommonConstants.CLIENT_IP_PORT
33. } as socket.NetAddress;

35. this.tcp.bind(clientIpAddress, (err: BusinessError) => {
36. if (err) {
37. Logger.error('bind fail' + JSON.stringify(err));
38. this.getUIContext().getPromptAction().showToast({ message: $r('app.string.connect_error') });
39. return;
40. }

42. let tcpConnect: socket.TCPConnectOptions = {} as socket.TCPConnectOptions;
43. const serverIpAddress: socket.NetAddress = {
44. address: CommonConstants.IP_ADDRESS,
45. port: CommonConstants.IP_PORT
46. } as socket.NetAddress;
47. tcpConnect.address = serverIpAddress;
48. tcpConnect.timeout = 3000;
49. this.tcp?.connect(tcpConnect, (err: BusinessError) => {
50. if (err) {
51. Logger.error('connect fail');
52. this.getUIContext().getPromptAction().showToast({ message: $r('app.string.connect_error') });
53. return;
54. }
55. });
56. });
57. }
```

[SocketReconnection.ets](https://gitcode.com/HarmonyOS_Samples/NetworkReconnection/blob/master/NetworkReconnection/entry/src/main/ets/pages/SocketReconnection.ets#L58-L168)

无网络切换有网络后重连下载效果图如下。

**图1** 无网络切换有网络后重连下载  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/p_sDlc3-TCKlIHDN_8R3Fg/zh-cn_image_0000002194011536.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061103Z&HW-CC-Expire=86400&HW-CC-Sign=B8CCC1CCEA6BD85E214FED1DEABE2A3AEB5A73A2B8F3FDACD7314D4960D4E6B1 "点击放大")

## 应用前后台切换后重连

### 场景描述

应用在使用TCPSocket、UDPSocket等通信时，如果未申请长时任务或短时任务，当应用退到后台一段时间后，可能遇到网络不可用或网络资源异常的情况，并且将应用切回前台后，继续使用之前的TCPSocket、UDPSocket等连接对象继续和服务器通信也可能出现网络异常。

### 实现原理

在HarmonyOS中，应用切换到后台2秒后，应用的网络资源会被冻结，并且在12秒后进行释放。此时，再继续使用网络资源，就会出现网络不可用的情况。如果应用有后台使用网络资源的场景，可以使用[短时任务](../harmonyos-guides/transient-task.md)或[长时任务](../harmonyos-guides/continuous-task.md)。

由于Socket通信是基于IP和端口进行通信的，在应用退到后台后，网络资源被冻结时会清空TCP、UDP连接对象的IP和端口，但是不会释放连接对象。在应用切换到前台后，系统会给连接对象重新分配新的IP和端口，继续使用之前的连接对象与服务器进行通信时，服务器会认为同一个连接对象前后IP和端口不一致，从而导致通信不可信、网络异常。

应用前后台切换后网络重连在实现上有以下两个关键部分。

* 结合[UIAbility组件生命周期](../harmonyos-guides/uiability-lifecycle.md)onForeground和onBackground，在前后台切换时，将应用前后台的状态存储在AppStorage中。
* 使用[@StorageProp](../harmonyos-guides/arkts-appstorage.md#storageprop)将AppStorage存储的前后台状态与对应的属性建立单向数据同步。并使用[@Watch](../harmonyos-guides/arkts-watch.md)监听状态变量的变化，当前后台变化后，关闭或重新连接。

### 开发步骤

前后台切换时，在UIAbility组件生命周期中存储前后台状态。

```
1. export default class EntryAbility extends UIAbility {
2. // ...

4. onForeground(): void {
5. // Ability has brought to foreground
6. // ...
7. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
8. }

10. onBackground(): void {
11. // Ability has back to background
12. // ...
13. AppStorage.setOrCreate('onForeground', false);
14. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
15. }
16. }
```

[EntryAbility.ets](https://gitcode.com/harmonyos_samples/NetworkReconnection/blob/master/NetworkReconnection/entry/src/main/ets/entryability/EntryAbility.ets#L7-L55)

使用@StorageProp同步前后台状态，并使用@Watch监听状态变化。

```
1. @StorageProp('onForeground') @Watch('onForegroundChange') onForeground: boolean = true;
2. // ...

4. onForegroundChange(): void {
5. this.onForeground ? this.tcpSocketConnect() : this.tcpSocketDisconnect();
6. }
```

[SocketReconnection.ets](https://gitcode.com/HarmonyOS_Samples/NetworkReconnection/blob/master/NetworkReconnection/entry/src/main/ets/pages/SocketReconnection.ets#L34-L54)

前后台切换网络重连实现效果如下：

**图2** 应用前后台切换后重连下载  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/9kkg5Dz3RUmUMVajmu5SqA/zh-cn_image_0000002229337333.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061103Z&HW-CC-Expire=86400&HW-CC-Sign=2EEA49A773BFDF9DBAB9B625ABF905D803E740287E7F83909CB77E179642A2FA "点击放大")

## 示例代码

* [实现应用网络重连功能](https://gitcode.com/harmonyos_samples/NetworkReconnection)
