---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-tpms
title: 基于TracingConfiguration实现性能维测
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > 提升HTTP传输性能 > 基于TracingConfiguration实现性能维测
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a9880e994da97aea574716f0cf163e7a828631e7105aeafbba78bc4b9bcf6da1
---

## 约束与限制

性能维测能力支持Phone、2in1、Tablet、Wearable设备。并且从5.1.1(19)开始，新增支持TV设备。

## 捕获有关HTTP请求/响应流的详细信息

当需要进行性能维测时，可以采集应用中HTTP请求的详细跟踪信息时，利用[TracingConfiguration](../harmonyos-references/remote-communication-rcp.md#tracingconfiguration)进行相关配置。[TracingConfiguration](../harmonyos-references/remote-communication-rcp.md#tracingconfiguration)中可以设置verbose（启用详细跟踪）、infoToCollect（配置要收集的特定类型的信息事件）、collectTimeInfo（在跟踪过程中是否应收集与时间相关的信息）、httpEventsHandler（为HTTP请求/响应过程中的特定操作定义响应处理程序的回调）四个参数。

下面将以获取HTTP请求/响应时的数据接收时、请求头接收时、数据传输完成时等详细信息为例，进行介绍。

1. 导入需要的模块，示例中包含了利用远场通信框架发起网络请求以及请求后的响应和错误处理，所以需导入以下模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建自定义响应处理程序，在[HttpEventsHandler](../harmonyos-references/remote-communication-rcp.md#httpeventshandler)中设置onDataReceive（当接收到HTTP响应正文的一部分时调用的回调）、onHeaderReceive（用于在响应期间处理接收到的headers的回调）、onDataEnd（数据传输完成时触发的回调）。

   ```
   1. // 定义自定义响应处理程序
   2. const customHttpEventsHandler: rcp.HttpEventsHandler = {
   3. onDataReceive: (incomingData: ArrayBuffer) => {
   4. // 用于处理传入数据的自定义逻辑
   5. console.info(`Received data: ${incomingData.byteLength}`, );
   6. return incomingData.byteLength;
   7. },
   8. onHeaderReceive: (headers: rcp.RequestHeaders) => {
   9. // 处理响应头的自定义逻辑
   10. console.info(`Received headers: ${JSON.stringify(headers)}`);
   11. },
   12. onDataEnd: () => {
   13. // 用于处理数据传输完成的自定义逻辑
   14. console.info('Data transfer complete');
   15. }
   16. };
   ```
3. 设置tracingConfig对象中的verbose为true，表示启用详细跟踪，设置tracingConfig对象中的infoToCollect对象中的incomingData为true（收集传入的数据信息事件）、outgoingData为true（收集传出的数据信息事件）、incomingHeader为true（收集传入的header信息事件）、outgoingHeader为true（收集传出的header信息事件）。

   ```
   1. // 配置跟踪设置
   2. const tracingConfig: rcp.TracingConfiguration = {
   3. verbose: true,
   4. infoToCollect: {
   5. incomingHeader: true, // 收集传入的header信息事件
   6. outgoingHeader: true, // 收集传入的header信息事件
   7. incomingData: true, // 收集传入数据信息事件
   8. outgoingData: true // 收集传出数据信息事件
   9. },
   10. collectTimeInfo: true,
   11. httpEventsHandler: customHttpEventsHandler
   12. };
   13. const securityConfig: rcp.SecurityConfiguration = {
   14. tlsOptions: {
   15. tlsVersion: 'TlsV1.3'
   16. }
   17. };
   ```
4. 调用rcp.createSession()传入tracingConfig ，创建通信会话对象session。

   ```
   1. // 创建通信会话对象，并传入相关配置
   2. const session = rcp.createSession({ requestConfiguration: { tracing: tracingConfig, security: securityConfig } });
   3. session.get('http://developer.huawei.com').then((response) => {
   4. console.info(`Request succeeded, message is ${JSON.stringify(response)}`);
   5. }).catch((err: BusinessError) => {
   6. console.error(`err: error code is ${err.code}, error data is ${err.data}`);
   7. });
   ```

## HTTP请求过程中各时间点详解

在实施性能维测的过程中，HTTP请求的各个时间点至关重要。借助TimeInfo提供的详细字段，可以精准控制请求过程，无论是直接利用这些字段，还是通过它们之间的运算，都能准确获取所需的时间点，从而提升测试效率。

下面，我们将通过图片、时间线及一段示例代码，详细解析请求过程中的关键时间点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/PpqY0N2vRWWigc7kpK6Yqw/zh-cn_image_0000002552798782.png?HW-CC-KV=V1&HW-CC-Date=20260427T234406Z&HW-CC-Expire=86400&HW-CC-Sign=B244E27A6A74BE66CEB40DA05E2406E4B2C44F13FC6DF40F2E8ECBC6643F6563)

从图中可以看到HTTP请求过程的基本过程，并且有一些关键的时间点，下面将以时间线的方式对其进行说明：

### TimeInfo时间线

请求开始 （0时刻） -> nameLookupTimeMs（DNS解析）-> connectTimeMs（建立连接）-> tlsHandshakeTimeMs（TLS握手）-> preTransferTimeMs（请求业务数据发送到服务器的时间点） -> startTransferTimeMs（从服务器接收到首包数据的时间点）。

说明

各时间节点所显示的时间均相对于0时刻，即从0时刻开始计时的时间。例如tlsHandshakeTimeMs为150.1ms，指从发起请求时间0开始，直到TLS握手结束所花费的时间为150.1ms。

网络请求过程中关键节点时间计算方法：

* 首包耗时：startTransferTimeMs - preTransferTimeMs
* TLS握手（不包含建连时间）耗时：tlsHandshakeTimeMs - connectTimeMs
* 接收剩余数据的耗时：totalTimeMs - startTransferTimeMs

### 示例代码

这段代码在使用过程中会将上述说明中三个比较关键的时间点打印出来，开发者可以根据获取到的时间对应用性能实现动态调整，获取最佳体验。

```
1. import { rcp } from '@kit.RemoteCommunicationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 1、创建session、requestURL
5. const session = rcp.createSession();
6. const requestURL = "https://www.example.com";

8. // 2、在需要跟踪分析请求过程中各个时间段消耗的时间，请将此开关打开
9. const configuration: rcp.Configuration = {
10. tracing: {
11. collectTimeInfo: true
12. }
13. }

15. // 3、创建请求
16. const request = new rcp.Request(requestURL, "GET");
17. request.configuration = configuration;

19. // 4、使用fetch发起网络请求，request中携带上面配置好的configuration
20. session.fetch(request).then((response: rcp.Response) => {
21. // 由于timeInfo中各个参数有可能为undefined，所以需要在两个时间段做运算前添加判空操作
22. if (!response.timeInfo) {
23. console.error(`timeInfo is undefined ${response.timeInfo}`);
24. return;
25. }
26. let remainderDataTime = response.timeInfo?.totalTimeMs - response.timeInfo?.startTransferTimeMs;
27. let firstPackageTime = response.timeInfo?.startTransferTimeMs - response.timeInfo?.preTransferTimeMs;
28. let TLSTime = response.timeInfo?.tlsHandshakeTimeMs - response.timeInfo?.connectTimeMs;

30. console.info(`首包耗时${firstPackageTime}`);
31. console.info(`TLS握手（不包含建连时间）耗时${TLSTime}`);
32. console.info(`接收剩余数据的耗时${remainderDataTime}`);
33. }).catch((err: BusinessError) => {
34. console.error(`Response err, the error code is ${err.code}, error data is ${err.data}`);
35. })
```
