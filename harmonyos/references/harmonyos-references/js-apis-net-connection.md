---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection
title: @ohos.net.connection (网络连接管理)
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > ArkTS API > @ohos.net.connection (网络连接管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:21+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:0d1e886871613f7408b0281144c9bc0e1196b43a134927a6d91f86241402300c
---

网络连接管理提供管理网络一些基础能力，包括获取默认激活的网络、获取所有激活网络列表、获取网络能力信息等功能。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

无特殊说明，接口默认不支持并发。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { connection } from '@kit.NetworkKit';
```

## connection.createNetConnection

PhonePC/2in1TabletTVWearable

createNetConnection(netSpecifier?: NetSpecifier, timeout?: number): NetConnection

创建一个NetConnection对象，可用于监听网络状态。[netSpecifier](js-apis-net-connection.md#netspecifier)表示需要监听网络的网络特征；timeout是超时时间（单位：毫秒)；netSpecifier是timeout的必要条件，两者都没有则表示关注默认网络。

说明

若需要监听网络状态，创建一个NetConnection对象后，还需调用[register](js-apis-net-connection.md#register)注册指定网络状态变化的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netSpecifier | [NetSpecifier](js-apis-net-connection.md#netspecifier) | 否 | 需要监听网络的网络特征，缺省则表示监听默认网络。 |
| timeout | number | 否 | 获取netSpecifier指定网络时的超时时间，传入值需为uint32\_t范围内的整数，仅netSpecifier存在时生效，默认值为0。  **说明**：当监听网络不存在时，会尝试激活此网络。若超过设置的超时时间，且注册了网络状态监听，则会触发netUnavailable事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NetConnection](js-apis-net-connection.md#netconnection) | 需要监听的网络连接对象的类型。 |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. // 示例1：仅关注默认网络, 无需指定netSpecifier参数，timeout参数未传入说明未使用超时时间，此时timeout为0。
4. let netConnection = connection.createNetConnection();

6. // 示例2：仅关注蜂窝网络，需要指定网络类型为蜂窝网络。
7. let timeout = 1000;
8. let netConnectionCellular = connection.createNetConnection({
9. netCapabilities: {
10. bearerTypes: [connection.NetBearType.BEARER_CELLULAR]
11. }
12. }, timeout);

14. // 示例3：关注蜂窝或Wi-Fi网络，需要指定网络类型为蜂窝网络和Wi-Fi网络。
15. let netConnectionCellularAndWifi = connection.createNetConnection({
16. netCapabilities: {
17. bearerTypes: [connection.NetBearType.BEARER_CELLULAR,
18. connection.NetBearType.BEARER_WIFI]
19. }
20. });
```

## connection.getDefaultNet

PhonePC/2in1TabletTVWearable

getDefaultNet(callback: AsyncCallback<NetHandle>): void

获取系统默认使用的网络句柄，包含网络ID。使用callback异步回调。

说明

* 系统默认使用的网络，该网络的capabilities必须具备[NET\_CAPABILITY\_INTERNET](js-apis-net-connection.md#netcap)且不是VPN类型的网络。
* 该接口的返回由系统决定，与应用是否指定网络无关。
* 一般情况下优先级为：以太网（PC）|蓝牙（手表）> WIFI > 蜂窝，特殊情况以实际返回结果为准。
* [NetHandle](js-apis-net-connection.md#nethandle)为网络唯一标识，当无网络可用时，返回0。其可用于[getNetCapabilities](js-apis-net-connection.md#connectiongetnetcapabilities)继续查询更多网络信息。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[NetHandle](js-apis-net-connection.md#nethandle)> | 是 | 回调函数。当成功获取默认激活网络的网络句柄时，error为undefined，data为默认网络的网络句柄；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.getDefaultNet((error: BusinessError, data: connection.NetHandle) => {
5. if (error) {
6. console.error(`Failed to get default net. Code:${error.code}, message:${error.message}`);
7. return;
8. }
9. console.info("Succeeded to get data: " + JSON.stringify(data));
10. });
```

## connection.getDefaultNet

PhonePC/2in1TabletTVWearable

getDefaultNet(): Promise<NetHandle>

获取系统默认使用的网络句柄，包含网络ID。使用Promise异步回调。

说明

* 系统默认使用的网络，该网络的capabilities必须具备[NET\_CAPABILITY\_INTERNET](js-apis-net-connection.md#netcap)且不是VPN类型的网络。
* 该接口的返回由系统决定，与应用是否指定网络无关。
* 一般情况下，优先级：以太网（PC）|蓝牙（手表）> WIFI > 蜂窝，特殊情况以实际返回结果为准。
* [NetHandle](js-apis-net-connection.md#nethandle)为网络唯一标识，当无网络可用时，返回0。其可用于[getNetCapabilities](js-apis-net-connection.md#connectiongetnetcapabilities)继续查询更多网络信息。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NetHandle](js-apis-net-connection.md#nethandle)> | 以Promise形式返回默认网络的网络句柄。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. connection.getDefaultNet().then((data: connection.NetHandle) => {
4. console.info("Succeeded to get data: " + JSON.stringify(data));
5. });
```

## connection.getDefaultNetSync9+

PhonePC/2in1TabletTVWearable

getDefaultNetSync(): NetHandle

获取系统默认使用的网络句柄，包含网络ID。使用同步方式返回。

说明

* 系统默认使用的网络，该网络的capabilities必须具备[NET\_CAPABILITY\_INTERNET](js-apis-net-connection.md#netcap)且不是VPN类型的网络。
* 该接口的返回由系统决定，与应用是否指定网络无关。
* 一般情况下，优先级：以太网（PC）|蓝牙（手表）> WIFI > 蜂窝，特殊情况以实际返回结果为准。
* [NetHandle](js-apis-net-connection.md#nethandle)为网络唯一标识，当无网络可用时，返回0。其可用于[getNetCapabilities](js-apis-net-connection.md#connectiongetnetcapabilities)继续查询更多网络信息。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NetHandle](js-apis-net-connection.md#nethandle) | 以同步方式返回默认网络的网络句柄。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. let netHandle = connection.getDefaultNetSync();
```

## connection.setAppHttpProxy11+

PhonePC/2in1TabletTVWearable

setAppHttpProxy(httpProxy: HttpProxy): void

设置应用级Http代理配置信息。

说明

若需使用本接口所配置的代理信息，则需在[HttpRequestOptions](js-apis-http.md#httprequestoptions)字段中将usingProxy设置为true以启用代理转发。本接口仅负责配置代理规则，不校验代理服务的有效性。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| httpProxy | [HttpProxy](js-apis-net-connection.md#httpproxy10) | 是 | 网络应用级Http代理配置信息。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100001 | Invalid http proxy. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { http } from '@kit.NetworkKit';

5. let exclusionStr = "192.168,baidu.com";
6. let exclusionArray = exclusionStr.split(',');
7. connection.setAppHttpProxy({
8. host: "192.168.xx.xxx",
9. port: 8080,
10. exclusionList: exclusionArray
11. } as connection.HttpProxy);
12. let httpRequest = http.createHttp();
13. let options: http.HttpRequestOptions = {
14. usingProxy: true, // 选择使用网络代理，从API 10开始支持该属性。
15. };
16. // 发起一个HTTP请求。
17. httpRequest.request("EXAMPLE_URL", options, (err: Error, data: http.HttpResponse) => {
18. if (!err) {
19. console.info(`Result: ${data.result}`);
20. console.info(`code: ${data.responseCode}`);
21. console.info(`type: ${JSON.stringify(data.resultType)}`);
22. console.info(`header: ${JSON.stringify(data.header)}`);
23. console.info(`cookies: ${data.cookies}`); // 从API version 8开始支持cookie。
24. } else {
25. console.error(`error: ${JSON.stringify(err)}`);
26. }
27. });
```

## connection.getDefaultHttpProxy10+

PhonePC/2in1TabletTVWearable

getDefaultHttpProxy(callback: AsyncCallback<HttpProxy>): void

获取网络的默认代理配置信息。使用callback异步回调。

说明

* 如果设置了全局代理，则返回全局代理配置信息。
* 如果进程使用[setAppNet](js-apis-net-connection.md#connectionsetappnet9)绑定到指定[NetHandle](js-apis-net-connection.md#nethandle)对应的网络，则返回[NetHandle](js-apis-net-connection.md#nethandle)对应网络的代理配置信息。在其它情况下，将返回默认网络的代理配置信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[HttpProxy](js-apis-net-connection.md#httpproxy10)> | 是 | 回调函数。当成功获取网络的默认代理配置信息时，error为undefined，data为网络的默认代理配置信息；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.getDefaultHttpProxy((error: BusinessError, data: connection.HttpProxy) => {
5. if (error) {
6. console.error(`Failed to get default http proxy. Code:${error.code}, message:${error.message}`);
7. return;
8. }
9. console.info("Succeeded to get data" + JSON.stringify(data));
10. });
```

## connection.getDefaultHttpProxy10+

PhonePC/2in1TabletTVWearable

getDefaultHttpProxy(): Promise<HttpProxy>

获取网络默认的代理配置信息。使用Promise异步回调。

说明

* 如果设置了全局代理，则返回全局代理配置信息。
* 如果进程使用[setAppNet](js-apis-net-connection.md#connectionsetappnet9)绑定到指定[NetHandle](js-apis-net-connection.md#nethandle)对应的网络，则返回[NetHandle](js-apis-net-connection.md#nethandle)对应网络的代理配置信息。在其它情况下，将返回默认网络的代理配置信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HttpProxy](js-apis-net-connection.md#httpproxy10)> | 以Promise形式返回网络默认的代理配置信息。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.getDefaultHttpProxy().then((data: connection.HttpProxy) => {
5. console.info(JSON.stringify(data));
6. }).catch((error: BusinessError) => {
7. console.info(JSON.stringify(error));
8. });
```

## connection.getAppNet9+

PhonePC/2in1TabletTVWearable

getAppNet(callback: AsyncCallback<NetHandle>): void

获取App绑定的网络句柄。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[NetHandle](js-apis-net-connection.md#nethandle)> | 是 | 回调函数。当成功获取App绑定的网络信息时，error为undefined，data为获取到App绑定的网络信息；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.getAppNet((error: BusinessError, data: connection.NetHandle) => {
5. if (error) {
6. console.error(`Failed to get App net. Code:${error.code}, message:${error.message}`);
7. return;
8. }
9. console.info("Succeeded to get data: " + JSON.stringify(data));
10. })
```

## connection.getAppNet9+

PhonePC/2in1TabletTVWearable

getAppNet(): Promise<NetHandle>

获取App绑定的网络信息。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NetHandle](js-apis-net-connection.md#nethandle)> | 以Promise形式返回App绑定的网络信息。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.getAppNet().then((data: connection.NetHandle) => {
5. console.info(JSON.stringify(data));
6. }).catch((error: BusinessError) => {
7. console.info(JSON.stringify(error));
8. });
```

## connection.getAppNetSync10+

PhonePC/2in1TabletTVWearable

getAppNetSync(): NetHandle

获取App绑定的网络信息。使用同步方式返回。

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NetHandle](js-apis-net-connection.md#nethandle) | 返回App绑定的数据网络。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. let netHandle = connection.getAppNetSync();
```

## connection.setAppNet9+

PhonePC/2in1TabletTVWearable

setAppNet(netHandle: NetHandle, callback: AsyncCallback<void>): void

将App绑定到特定的网络，绑定后App只能通过netHandle对应的网络访问网络。使用callback异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | [NetHandle](js-apis-net-connection.md#nethandle) | 是 | 网络句柄。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当成功绑定App到指定网络时，error为undefined，否则为错误对象。 |

说明

当应用不再使用该网络或者该网络不可用时，需要解除App和指定网络的绑定关系，以免导致应用无法上网。

如需解除App和指定网络的绑定关系，可以调用[setAppNet](js-apis-net-connection.md#connectionsetappnet9)，并传入一个netId = 0的NetHandle对象，参考以下示例。

```
1. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
2. netHandle.netId = 0;
3. connection.setAppNet(netHandle, (error: BusinessError, data: void) => {
4. if (error) {
5. console.error(`Failed to get default net. Code:${error.code}, message:${error.message}`);
6. return;
7. }
8. console.info("Succeeded to get data: " + JSON.stringify(data));
9. });
10. });
```

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

当应用绑定WIFI网络，WIFI弱信号或者断开时，如果不解绑，会导致应用无法上网。

以下示例以绑定WIFI网络为例，结合[on("netAvailable")](js-apis-net-connection.md#onnetavailable)、[on("netLost")](js-apis-net-connection.md#onnetlost)接口，当监听到WIFI网络可用时绑定WIFI网络，不可用时解绑，使用默认网络。

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 创建NetConnection对象。仅关注WIFI网络，需要指定网络类型为WIFI网络。
5. let netCon = connection.createNetConnection({
6. netCapabilities: {
7. bearerTypes: [connection.NetBearType.BEARER_WIFI]
8. }
9. });

11. // 使用on接口订阅网络可用事件
12. netCon.on('netAvailable', (netHandle: connection.NetHandle) => {
13. console.info("Succeeded to get data: " + JSON.stringify(netHandle));
14. connection.setAppNet(netHandle, (error: BusinessError, data: void) => {
15. if (error) {
16. console.error(`Failed to setAppNet. Code:${error.code}, message:${error.message}`);
17. return;
18. }
19. console.info("Succeeded to setAppNet, netid: " + JSON.stringify(netHandle.netId));
20. });
21. });

23. // 使用on接口订阅网络丢失事件。
24. netCon.on('netLost', (netHandle: connection.NetHandle) => {
25. console.info("Succeeded to get data: " + JSON.stringify(netHandle));
26. // 网络丢失时，需要主动解除指定网络的绑定关系
27. netHandle.netId = 0;
28. connection.setAppNet(netHandle, (error: BusinessError, data: void) => {
29. if (error) {
30. console.error(`Failed to setAppNet. Code:${error.code}, message:${error.message}`);
31. return;
32. }
33. console.info("Succeeded to setAppNet, netid: " + JSON.stringify(netHandle.netId));
34. });
35. });

37. // 注册网络状态变化事件。此接口要在调用on后调用。
38. netCon.register((error: BusinessError) => {
39. if (error) {
40. console.error(JSON.stringify(error));
41. }
42. });
```

## connection.setAppNet9+

PhonePC/2in1TabletTVWearable

setAppNet(netHandle: NetHandle): Promise<void>

将App异步绑定到特定的网络，绑定后App只能通过netHandle对应的网络访问网络。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | [NetHandle](js-apis-net-connection.md#nethandle) | 是 | 网络句柄。 |

说明

当应用不再使用该网络或者该网络不可用时，需要解除App和指定网络的绑定关系，以免导致应用无法上网。

如需解除App和指定网络的绑定关系，可以调用[setAppNet](js-apis-net-connection.md#connectionsetappnet9)，并传入一个netId = 0的NetHandle对象，参考以下示例。

```
1. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
2. netHandle.netId = 0;
3. connection.setAppNet(netHandle).then(() => {
4. console.info("setAppNet success");
5. }).catch((error: BusinessError) => {
6. console.error(`Failed to setAppNet. Code:${error.code}, message:${error.message}`);
7. })
8. });
```

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

当应用绑定WIFI网络，WIFI弱信号或者断开时，如果不解绑，会导致应用无法上网。

以下示例以绑定WIFI网络为例，结合[on("netAvailable")](js-apis-net-connection.md#onnetavailable)、[on("netLost")](js-apis-net-connection.md#onnetlost)接口，当监听到WIFI网络可用时绑定WIFI网络，不可用时解绑，使用默认网络。

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 创建NetConnection对象。仅关注WIFI网络，需要指定网络类型为WIFI网络。
5. let netCon = connection.createNetConnection({
6. netCapabilities: {
7. bearerTypes: [connection.NetBearType.BEARER_WIFI]
8. }
9. });

11. // 使用on接口订阅网络可用事件
12. netCon.on('netAvailable', (netHandle: connection.NetHandle) => {
13. console.info("Succeeded to get data: " + JSON.stringify(netHandle));
14. connection.setAppNet(netHandle).then(() => {
15. console.info("setAppNet success, netid: " + JSON.stringify(netHandle.netId));
16. }).catch((error: BusinessError) => {
17. console.error(`Failed to setAppNet. Code:${error.code}, message:${error.message}`);
18. })
19. });

21. // 使用on接口订阅网络丢失事件。
22. netCon.on('netLost', (netHandle: connection.NetHandle) => {
23. console.info("Succeeded to get data: " + JSON.stringify(netHandle));
24. // 网络丢失时，需要主动解除指定网络的绑定关系
25. netHandle.netId = 0;
26. connection.setAppNet(netHandle).then(() => {
27. console.info("setAppNet success, netid: " + JSON.stringify(netHandle.netId));
28. }).catch((error: BusinessError) => {
29. console.error(`Failed to setAppNet. Code:${error.code}, message:${error.message}`);
30. })
31. });

33. // 注册网络状态变化事件。此接口要在调用on后调用。
34. netCon.register((error: BusinessError) => {
35. if (error) {
36. console.error(JSON.stringify(error));
37. }
38. });
```

## connection.getAllNets

PhonePC/2in1TabletTVWearable

getAllNets(callback: AsyncCallback<Array<NetHandle>>): void

获取所有处于连接状态的网络列表，使用callback异步回调。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[NetHandle](js-apis-net-connection.md#nethandle)>> | 是 | 回调函数。当成功获取所有处于连接状态的网络列表时，error为undefined，data为处于激活状态的网络列表；否则为错误对象。  **说明：** 在Wi-Fi和蜂窝数据开关均开启的情况下，若无应用指定使用蜂窝网络，则仅激活Wi-Fi网络，因此仅返回Wi-Fi的NetHandle。除非有特定应用启动蜂窝网络，才能同时获取Wi-Fi和蜂窝数据的NetHandle。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.getAllNets((error: BusinessError, data: connection.NetHandle[]) => {
5. if (error) {
6. console.error(`Failed to get all nets. Code:${error.code}, message:${error.message}`);
7. return;
8. }
9. console.info("Succeeded to get data: " + JSON.stringify(data));
10. });
```

## connection.getAllNets

PhonePC/2in1TabletTVWearable

getAllNets(): Promise<Array<NetHandle>>

获取所有处于连接状态的网络列表。使用Promise异步回调。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[NetHandle](js-apis-net-connection.md#nethandle)>> | Promise对象，返回处于激活状态的网络列表。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. connection.getAllNets().then((data: connection.NetHandle[]) => {
4. console.info("Succeeded to get data: " + JSON.stringify(data));
5. });
```

## connection.getAllNetsSync10+

PhonePC/2in1TabletTVWearable

getAllNetsSync(): Array<NetHandle>

获取所有处于连接状态的网络列表。使用同步方式返回。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[NetHandle](js-apis-net-connection.md#nethandle)> | 返回所有处于连接状态的网络列表。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. let netHandle = connection.getAllNetsSync();
```

## connection.getConnectionProperties

PhonePC/2in1TabletTVWearable

getConnectionProperties(netHandle: NetHandle, callback: AsyncCallback<ConnectionProperties>): void

获取netHandle对应的网络的连接信息，包含网卡名称、域名、链路信息、路由信息、网络地址及最大传输单元。使用callback异步回调。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | [NetHandle](js-apis-net-connection.md#nethandle) | 是 | 网络句柄。 |
| callback | AsyncCallback<[ConnectionProperties](js-apis-net-connection.md#connectionproperties)> | 是 | 回调函数。当成功获取netHandle对应的网络的连接信息时，error为undefined，data为获取的网络连接信息；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 示例： 获取当前默认网络的连接信息。
5. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
6. if (netHandle.netId == 0) {
7. // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
8. return;
9. }
10. connection.getConnectionProperties(netHandle, (error: BusinessError, data: connection.ConnectionProperties) => {
11. if (error) {
12. console.error(`Failed to get connection properties. Code:${error.code}, message:${error.message}`);
13. return;
14. }
15. console.info("Succeeded to get data: " + JSON.stringify(data));
16. })
17. });
```

## connection.getConnectionProperties

PhonePC/2in1TabletTVWearable

getConnectionProperties(netHandle: NetHandle): Promise<ConnectionProperties>

获取netHandle对应的网络的连接信息，包含网卡名称、域名、链路信息、路由信息、网络地址及最大传输单元。使用Promise异步回调。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | [NetHandle](js-apis-net-connection.md#nethandle) | 是 | 数据网络的句柄。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ConnectionProperties](js-apis-net-connection.md#connectionproperties)> | Promise对象，返回网络的连接信息。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
4. if (netHandle.netId == 0) {
5. // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
6. return;
7. }

9. connection.getConnectionProperties(netHandle).then((data: connection.ConnectionProperties) => {
10. console.info("Succeeded to get data: " + JSON.stringify(data));
11. })
12. });
```

## connection.getConnectionPropertiesSync10+

PhonePC/2in1TabletTVWearable

getConnectionPropertiesSync(netHandle: NetHandle): ConnectionProperties

获取netHandle对应的网络的连接信息，包含网卡名称、域名、链路信息、路由信息、网络地址及最大传输单元。使用同步方式返回。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | [NetHandle](js-apis-net-connection.md#nethandle) | 是 | 网络句柄。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ConnectionProperties](js-apis-net-connection.md#connectionproperties) | 返回网络的连接信息。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let netHandle: connection.NetHandle;
5. let connectionproperties: connection.ConnectionProperties;

7. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
8. if (netHandle.netId == 0) {
9. // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
10. return;
11. }
12. netHandle = connection.getDefaultNetSync();
13. connectionproperties = connection.getConnectionPropertiesSync(netHandle);
14. console.info("Succeeded to get connectionproperties: " + JSON.stringify(connectionproperties));
15. });
```

## connection.getNetCapabilities

PhonePC/2in1TabletTVWearable

getNetCapabilities(netHandle: NetHandle, callback: AsyncCallback<NetCapabilities>): void

获取netHandle对应网络的能力集，包含上/下行带宽、网络具体能力、网络类型。使用callback异步回调。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | [NetHandle](js-apis-net-connection.md#nethandle) | 是 | 网络的句柄。 |
| callback | AsyncCallback<[NetCapabilities](js-apis-net-connection.md#netcapabilities)> | 是 | 回调函数。当成功获取netHandle对应网络的能力集时，error为undefined，data为获取到的网络能力集；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
5. if (netHandle.netId == 0) {
6. // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
7. return;
8. }
9. connection.getNetCapabilities(netHandle, (error: BusinessError, data: connection.NetCapabilities) => {
10. if (error) {
11. console.error(`Failed to get net capabilities. Code:${error.code}, message:${error.message}`);
12. return;
13. }
14. console.info("Succeeded to get data: " + JSON.stringify(data));
15. })
16. }).catch((error: BusinessError) => {
17. console.error(JSON.stringify(error));
18. });
```

## connection.getNetCapabilities

PhonePC/2in1TabletTVWearable

getNetCapabilities(netHandle: NetHandle): Promise<NetCapabilities>

获取netHandle对应网络的能力集，包含上/下行带宽、网络具体能力、网络类型。使用Promise异步回调。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | [NetHandle](js-apis-net-connection.md#nethandle) | 是 | 网络句柄。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NetCapabilities](js-apis-net-connection.md#netcapabilities)> | Promise对象，返回网络的能力集。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
5. if (netHandle.netId == 0) {
6. // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
7. return;
8. }
9. connection.getNetCapabilities(netHandle).then((data: connection.NetCapabilities) => {
10. console.info("Succeeded to get data: " + JSON.stringify(data));
11. })
12. }).catch((error: BusinessError) => {
13. console.error(JSON.stringify(error));
14. });
```

## connection.getNetCapabilitiesSync10+

PhonePC/2in1TabletTVWearable

getNetCapabilitiesSync(netHandle: NetHandle): NetCapabilities

获取netHandle对应网络的能力信息，包含上/下行带宽、网络具体能力、网络类型。使用同步方式返回。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | [NetHandle](js-apis-net-connection.md#nethandle) | 是 | 网络句柄。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NetCapabilities](js-apis-net-connection.md#netcapabilities) | 返回网络的能力集。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let netHandle: connection.NetHandle;
5. let getNetCapabilitiesSync: connection.NetCapabilities;

7. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
8. if (netHandle.netId == 0) {
9. // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
10. return;
11. }

13. getNetCapabilitiesSync = connection.getNetCapabilitiesSync(netHandle);
14. console.info("Succeeded to get net capabilities sync: " + JSON.stringify(getNetCapabilitiesSync));
15. });
```

## connection.isDefaultNetMetered9+

PhonePC/2in1TabletTVWearable

isDefaultNetMetered(callback: AsyncCallback<boolean>): void

检查当前默认网络上的数据流量使用是否被计费（例如：WiFi网络不会被计费，蜂窝网络会被计费）。使用callback异步回调。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回当前网络上的数据流量是否被计费。true表示会被计费，false表示不会被计费。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.isDefaultNetMetered((error: BusinessError, data: boolean) => {
5. console.error(JSON.stringify(error));
6. console.info('data: ' + data);
7. });
```

## connection.isDefaultNetMetered9+

PhonePC/2in1TabletTVWearable

isDefaultNetMetered(): Promise<boolean>

检查当前默认网络上的数据流量使用是否被计费（例如：WiFi网络不会被计费，蜂窝网络会被计费）。使用Promise异步回调。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回当前网络上的数据流量是否被计费。true表示会被计费，false表示不会被计费。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. connection.isDefaultNetMetered().then((data: boolean) => {
4. console.info('data: ' + data);
5. });
```

## connection.isDefaultNetMeteredSync10+

PhonePC/2in1TabletTVWearable

isDefaultNetMeteredSync(): boolean

检查当前网络上的数据流量使用是否被计费（例如：WiFi网络不会被计费，蜂窝网络会被计费）。使用同步方式返回。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示当前网络上的数据流量是否被计费。true表示会被计费，false表示不会被计费。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. let isMetered = connection.isDefaultNetMeteredSync();
```

## connection.hasDefaultNet

PhonePC/2in1TabletTVWearable

hasDefaultNet(callback: AsyncCallback<boolean>): void

获取当前是否有可用网络，使用callback异步回调。如果有可用网络，可以使用[getDefaultNet](js-apis-net-connection.md#connectiongetdefaultnet)获取默认网络句柄。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回当前是否有可用网络。true表示当前有可用网络，false表示当前没有可用网络。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.hasDefaultNet((error: BusinessError, data: boolean) => {
5. console.error(JSON.stringify(error));
6. console.info('data: ' + data);
7. });
```

## connection.hasDefaultNet

PhonePC/2in1TabletTVWearable

hasDefaultNet(): Promise<boolean>

获取当前是否有可用网络。使用Promise异步回调。如果有可用网络，可以使用[getDefaultNet](js-apis-net-connection.md#connectiongetdefaultnet)获取默认网络句柄。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回当前是否有可用网络。true表示当前有可用网络，false表示当前没有可用网络。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. connection.hasDefaultNet().then((data: boolean) => {
4. console.info('data: ' + data);
5. });
```

## connection.hasDefaultNetSync10+

PhonePC/2in1TabletTVWearable

hasDefaultNetSync(): boolean

获取当前是否有可用网络。使用同步方式返回。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回当前是否有可用网络。true表示当前有可用网络，false表示当前没有可用网络。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. let hasDefaultNet = connection.hasDefaultNetSync();
```

## connection.reportNetConnected

PhonePC/2in1TabletTVWearable

reportNetConnected(netHandle: NetHandle, callback: AsyncCallback<void>): void

向网络管理上报网络处于可用状态。使用callback方式异步回调。

说明

该接口用于浏览器连接portal网络，网络认证成功后，向网络管理上报网络连接成功，网络管理会触发网络探测，更新网络状态。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO 和 ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | [NetHandle](js-apis-net-connection.md#nethandle) | 是 | 网络句柄，参考[NetHandle](js-apis-net-connection.md#nethandle)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当向网络管理报告网络处于可用状态成功，error为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
5. connection.reportNetConnected(netHandle, (error: BusinessError) => {
6. console.error(JSON.stringify(error));
7. });
8. });
```

## connection.reportNetConnected

PhonePC/2in1TabletTVWearable

reportNetConnected(netHandle: NetHandle): Promise<void>

向网络管理报告网络处于可用状态。使用Promise异步回调。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO 和 ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | [NetHandle](js-apis-net-connection.md#nethandle) | 是 | 网络句柄，参考[NetHandle](js-apis-net-connection.md#nethandle)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
4. connection.reportNetConnected(netHandle).then(() => {
5. console.info(`report success`);
6. });
7. });
```

## connection.reportNetDisconnected

PhonePC/2in1TabletTVWearable

reportNetDisconnected(netHandle: NetHandle, callback: AsyncCallback<void>): void

向网络管理上报网络处于不可用状态。使用callback异步回调。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO 和 ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | [NetHandle](js-apis-net-connection.md#nethandle) | 是 | 网络句柄，参考[NetHandle](js-apis-net-connection.md#nethandle)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当向网络管理报告网络处于不可用状态成功时，error为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.getDefaultNet((error: BusinessError, netHandle: connection.NetHandle) => {
5. if (netHandle.netId == 0) {
6. // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
7. return;
8. }
9. connection.reportNetDisconnected(netHandle, (error: BusinessError, data: void) => {
10. if (error) {
11. console.error(`Failed to get default net. Code:${error.code}, message:${error.message}`);
12. return;
13. }
14. console.info("report success");
15. });
16. });
```

## connection.reportNetDisconnected

PhonePC/2in1TabletTVWearable

reportNetDisconnected(netHandle: NetHandle): Promise<void>

向网络管理上报网络处于不可用状态。使用Promise异步回调。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO 和 ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | [NetHandle](js-apis-net-connection.md#nethandle) | 是 | 网络句柄。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
4. connection.reportNetDisconnected(netHandle).then( () => {
5. console.info(`report success`);
6. });
7. });
```

## connection.getAddressesByName

PhonePC/2in1TabletTVWearable

getAddressesByName(host: string, callback: AsyncCallback<Array<NetAddress>>): void

使用当前默认网络解析主机名以获取所有IP地址。使用callback异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要解析的主机名。 |
| callback | AsyncCallback<Array<[NetAddress](js-apis-net-connection.md#netaddress)>> | 是 | 回调函数。当使用默认网络解析主机名成功获取所有IP地址，error为undefined，data为获取到的所有IP地址；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.getAddressesByName("xxxx", (error: BusinessError, data: connection.NetAddress[]) => {
5. if (error) {
6. console.error(`Failed to get addresses. Code:${error.code}, message:${error.message}`);
7. return;
8. }
9. console.info("Succeeded to get data: " + JSON.stringify(data));
10. });
```

## connection.getAddressesByName

PhonePC/2in1TabletTVWearable

getAddressesByName(host: string): Promise<Array<NetAddress>>

使用当前默认网络解析主机名以获取所有IP地址。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要解析的主机名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[NetAddress](js-apis-net-connection.md#netaddress)>> | Promise对象。返回所有IP地址。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. connection.getAddressesByName("xxxx").then((data: connection.NetAddress[]) => {
4. console.info("Succeeded to get data: " + JSON.stringify(data));
5. });
```

## connection.getAddressesByNameWithOptions23+

PhonePC/2in1TabletTVWearable

getAddressesByNameWithOptions(host: string, option?: QueryOptions): Promise<Array<NetAddress>>

使用当前默认网络基于指定IP类型进行DNS解析。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要解析的主机名。例如："[www.example.com"。](http://www.example.com) |
| option | [QueryOptions](js-apis-net-connection.md#queryoptions23) | 否 | 需要查询的IP类型，默认值为FAMILY\_TYPE\_ALL。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[NetAddress](js-apis-net-connection.md#netaddress)>> | Promise对象，返回查询到的IP地址。返回值中的port字段固定为0，无需关注。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. let option: connection.QueryOptions = {
4. family: connection.FamilyType.FAMILY_TYPE_IPV4
5. };
6. connection.getAddressesByNameWithOptions("www.example.com", option).then((data: connection.NetAddress[]) => {
7. console.info(`Succeeded to get data: ${JSON.stringify(data)}`);
8. }).catch((err: BusinessError) => {
9. console.error(`get ERROR msg: ${JSON.stringify(err)}`)
10. });
```

## QueryOptions23+

PhonePC/2in1TabletTVWearable

需要查询的IP类型。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| family | [FamilyType](js-apis-net-connection.md#familytype23) | 否 | 是 | 需要查询的具体IP地址类型，默认值为FAMILY\_TYPE\_ALL。 |

## FamilyType23+

PhonePC/2in1TabletTVWearable

需要查询的具体IP地址类型。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FAMILY\_TYPE\_ALL | 0 | 查询所有IPv4和IPv6地址。 |
| FAMILY\_TYPE\_IPV4 | 1 | 仅查询IPv4地址。 |
| FAMILY\_TYPE\_IPV6 | 2 | 仅查询IPv6地址。 |

## connection.addCustomDnsRule11+

PhonePC/2in1TabletTVWearable

addCustomDnsRule(host: string, ip: Array<string>, callback: AsyncCallback<void>): void

为当前应用程序添加自定义host和对应的IP地址的映射。使用callback异步回调。

说明

不需要时可调用[removeCustomDnsRule](js-apis-net-connection.md#connectionremovecustomdnsrule11)删除某一条自定义规则或调用[clearCustomDnsRules](js-apis-net-connection.md#connectionclearcustomdnsrules11)删除当前应用程序的所有的自定义DNS规则 。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要自定义解析的主机名。 |
| ip | Array<string> | 是 | 主机名所映射的IP地址列表。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当为当前应用程序添加自定义host和对应的ip地址的映射成功，error为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.addCustomDnsRule("xxxx", ["xx.xx.xx.xx","xx.xx.xx.xx"], (error: BusinessError, data: void) => {
5. if (error) {
6. console.error(`Failed to get add custom dns rule. Code:${error.code}, message:${error.message}`);
7. return;
8. }
9. console.info("Succeeded to get data: " + JSON.stringify(data));
10. })
```

## connection.addCustomDnsRule11+

PhonePC/2in1TabletTVWearable

addCustomDnsRule(host: string, ip: Array<string>): Promise<void>

为当前应用程序添加自定义host和对应的IP地址的映射。使用Promise异步回调。

说明

不需要时可调用[removeCustomDnsRule](js-apis-net-connection.md#connectionremovecustomdnsrule11)删除某一条自定义规则或调用[clearCustomDnsRules](js-apis-net-connection.md#connectionclearcustomdnsrules11)删除当前应用程序的所有的自定义DNS规则 。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要自定义解析的主机名。 |
| ip | Array<string> | 是 | 主机名所映射的IP地址列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.addCustomDnsRule("xxxx", ["xx.xx.xx.xx","xx.xx.xx.xx"]).then(() => {
5. console.info("success");
6. }).catch((error: BusinessError) => {
7. console.error(JSON.stringify(error));
8. })
```

## connection.removeCustomDnsRule11+

PhonePC/2in1TabletTVWearable

removeCustomDnsRule(host: string, callback: AsyncCallback<void>): void

删除当前应用程序中对应host的自定义DNS规则。使用callback异步回调。

说明

可调用[addCustomDnsRule](js-apis-net-connection.md#connectionaddcustomdnsrule11)添加自定义规则。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要删除自定义DNS规则的主机名。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除当前应用程序中对应host的自定义DNS规则成功，error为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.removeCustomDnsRule("xxxx", (error: BusinessError, data: void) => {
5. if (error) {
6. console.error(`Failed to remove custom dns rule. Code:${error.code}, message:${error.message}`);
7. return;
8. }
9. console.info("Succeeded to get data: " + JSON.stringify(data));
10. })
```

## connection.removeCustomDnsRule11+

PhonePC/2in1TabletTVWearable

removeCustomDnsRule(host: string): Promise<void>

删除当前应用程序中对应host的自定义DNS规则。使用Promise异步回调。

说明

可调用[addCustomDnsRule](js-apis-net-connection.md#connectionaddcustomdnsrule11)添加自定义规则。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要删除自定义DNS规则的主机名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.removeCustomDnsRule("xxxx").then(() => {
5. console.info("success");
6. }).catch((error: BusinessError) => {
7. console.error(JSON.stringify(error));
8. })
```

## connection.clearCustomDnsRules11+

PhonePC/2in1TabletTVWearable

clearCustomDnsRules(callback: AsyncCallback<void>): void

删除当前应用程序的所有的自定义DNS规则。使用callback异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除当前应用程序的所有的自定义DNS规则成功，error为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.clearCustomDnsRules((error: BusinessError, data: void) => {
5. if (error) {
6. console.error(`Failed to clear custom dns rules. Code:${error.code}, message:${error.message}`);
7. return;
8. }
9. console.info("Succeeded to get data: " + JSON.stringify(data));
10. })
```

## connection.clearCustomDnsRules11+

PhonePC/2in1TabletTVWearable

clearCustomDnsRules(): Promise<void>

删除当前应用程序的所有的自定义DNS规则。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.clearCustomDnsRules().then(() => {
5. console.info("success");
6. }).catch((error: BusinessError) => {
7. console.error(JSON.stringify(error));
8. })
```

## connection.setPacFileUrl20+

PhonePC/2in1TabletTVWearable

setPacFileUrl(pacFileUrl: string): void

设置PAC脚本（Proxy Auto-Configuration Script，代理自动配置脚本）的URL地址，并启动PAC代理能力，比如：<http://127.0.0.1:21998/PacProxyScript.pac> 。可通过调用[findProxyForUrl](js-apis-net-connection.md#connectionfindproxyforurl20)解析URL地址来获取代理信息。

注意

1、本接口当前在PC/2in120+、Phone23+、Tablet23+、TV23+设备上支持解析脚本并启用PAC代理能力，Wearable设备类型上只保存脚本地址，不会启用PAC代理能力。

2、该接口不会校验URL真实性，PC设备上在设置完成之后，会启动PAC代理，若URL有误，则启动代理失败，返回2100002错误码。

**需要权限**：ohos.permission.SET\_PAC\_URL

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pacFileUrl | string | 是 | 当前PAC脚本的URL地址。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. let pacFileUrl = "http://example.com/proxy.pac";
4. connection.setPacFileUrl(pacFileUrl);
```

## connection.getPacFileUrl20+

PhonePC/2in1TabletTVWearable

getPacFileUrl(): string

获取当前PAC脚本的URL地址。

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 当前PAC脚本的URL地址，如果没有PAC脚本则返回空字符串。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. let pacFileUrl = connection.getPacFileUrl();
4. console.info(pacFileUrl);
```

## connection.findProxyForUrl20+

PhonePC/2in1TabletTVWearable

findProxyForUrl(url: string): string

通过设置的PAC脚本，解析指定的URL代理地址，返回对应的PAC代理信息。

说明

1、可通过 [setPacFileUrl](js-apis-net-connection.md#connectionsetpacfileurl20) 或 [setPacUrl](js-apis-net-connection.md#connectionsetpacurl15) 设置PAC脚本。

2、如果调用本接口前未设置PAC脚本，则返回空字符串。

3、由于[setPacFileUrl](js-apis-net-connection.md#connectionsetpacfileurl20)接口支持PC/2in120+、Phone23+、Tablet23+、TV23+设备解析脚本并启用PAC代理能力，因此本接口支持PC设备获取PAC代理信息。 Wearable设备调用本接口功能不生效，返回空字串。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要查找代理信息的URL。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回代理信息。 |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. let proxyInfo = connection.findProxyForUrl("http://example.com");
4. console.info(proxyInfo);
```

## connection.setPacUrl15+

PhonePC/2in1TabletTVWearable

setPacUrl(pacUrl: string): void

设置系统级代理自动配置（Proxy Auto Config，PAC）脚本地址。

说明

只支持设置脚本地址，不支持解析和启用代理功能，如需设置脚本并启用代理，则可调用[setPacFileUrl](js-apis-net-connection.md#connectionsetpacfileurl20)接口。

**需要权限**：ohos.permission.SET\_PAC\_URL

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pacUrl | string | 是 | 需要设置的PAC脚本的地址，该接口不会对脚本地址进行校验。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. let pacUrl = "xxx";
4. connection.setPacUrl(pacUrl);
```

## connection.getPacUrl15+

PhonePC/2in1TabletTVWearable

getPacUrl(): string

获取系统级代理自动配置（PAC）脚本地址。

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回PAC脚本地址。PAC脚本不存在时，抛出2100003错误码。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. let pacUrl = connection.getPacUrl();
```

## connection.setNetExtAttribute20+

PhonePC/2in1TabletTVWearable

setNetExtAttribute(netHandle: NetHandle, netExtAttribute: string): Promise<void>

为netHandle对应的网络设置扩展属性，标识网络的安全级别。使用Promise异步回调。

说明

该接口所需的权限目前仅支持PC设备。

**需要权限**：ohos.permission.SET\_NET\_EXT\_ATTRIBUTE

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | [NetHandle](js-apis-net-connection.md#nethandle) | 是 | 网络句柄。 |
| netExtAttribute | string | 是 | 需要设置的网络扩展属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
5. if (netHandle.netId == 0) {
6. // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
7. return;
8. }
9. let netExtAttribute: string = "xxx";
10. connection.setNetExtAttribute(netHandle, netExtAttribute).then(() => {
11. console.info("setNetExtAttribute success");
12. }).catch((error: BusinessError) => {
13. console.error("setNetExtAttribute failed, err: " + error.code);
14. })
15. });
```

## connection.setNetExtAttributeSync20+

PhonePC/2in1TabletTVWearable

setNetExtAttributeSync(netHandle: NetHandle, netExtAttribute: string): void

为netHandle对应的网络设置扩展属性，标识网络的安全级别。使用同步方式返回。

说明

该接口所需的权限目前仅支持PC设备。

**需要权限**：ohos.permission.SET\_NET\_EXT\_ATTRIBUTE

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | [NetHandle](js-apis-net-connection.md#nethandle) | 是 | 网络句柄。 |
| netExtAttribute | string | 是 | 需要设置的网络扩展属性。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let netExtAttribute: string = "xxx";
5. let netHandle = connection.getDefaultNetSync();
6. if (netHandle.netId != 0) {
7. connection.setNetExtAttributeSync(netHandle, netExtAttribute);
8. }
```

## connection.getNetExtAttribute20+

PhonePC/2in1TabletTVWearable

getNetExtAttribute(netHandle: NetHandle): Promise<string>

获取netHandle对应网络的扩展属性，以确定网络的安全级别。使用Promise异步回调。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | [NetHandle](js-apis-net-connection.md#nethandle) | 是 | 网络句柄。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回的网络扩展属性。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
5. if (netHandle.netId == 0) {
6. // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
7. return;
8. }
9. connection.getNetExtAttribute(netHandle).then((netExtAttribute: string) => {
10. console.info("getNetExtAttribute: " + netExtAttribute);
11. }).catch((error: BusinessError) => {
12. console.error("getNetExtAttribute failed, err: " + error.code);
13. })
14. });
```

## connection.getNetExtAttributeSync20+

PhonePC/2in1TabletTVWearable

getNetExtAttributeSync(netHandle: NetHandle): string

获取netHandle对应网络的扩展属性，以确定网络的安全级别。使用同步方式返回。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | [NetHandle](js-apis-net-connection.md#nethandle) | 是 | 网络句柄。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 以同步方式返回的网络扩展属性。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let netHandle = connection.getDefaultNetSync();
5. if (netHandle.netId != 0) {
6. let netExtAttribute: string = connection.getNetExtAttributeSync(netHandle);
7. console.info("getNetExtAttribute: " + netExtAttribute);
8. }
```

## connection.getIpNeighTable22+

PhonePC/2in1TabletTVWearable

getIpNeighTable(): Promise<Array<NetIpMacInfo>>

获取本地设备IP邻居表条目信息，包括IPv4和IPv6，每个条目信息包括IP地址、MAC地址、网卡名。使用Promise异步回调。

说明

该接口获取IP邻居表的缓存的数据，并非局域网内所有连接的数据。

开发者可使用此接口排查网络异常、解析IP地址与MAC地址映射。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO 和 ohos.permission.GET\_IP\_MAC\_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[NetIpMacInfo](js-apis-net-connection.md#netipmacinfo22)>> | Promise对象，返回ip邻居表条目信息。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.getIpNeighTable().then((data: connection.NetIpMacInfo[]) => {
5. if (data.length !== 0) {
6. console.info(`ipAddress:${data[0].ipAddress}`);
7. console.info(`ifaceName:${data[0].iface}`);
8. console.info(`macAddress:${data[0].macAddress}`);
9. }
10. }).catch((error: BusinessError) => {
11. console.error(`error fetching ip neigh table. Code:${error.code}, message:${error.message}`);
12. });
```

## connection.getConnectOwnerUid23+

PhonePC/2in1TabletTVWearable

getConnectOwnerUid(protocol: ProtocolType, local: NetAddress, remote: NetAddress): Promise<number>

用于查询发起指定网络连接的应用UID。使用Promise异步回调。

说明

* 该接口仅限在VPN应用中调用。
* 调用接口时请设置local和remote参数的端口号。若未设置端口号或将端口号设置为0，接口会基于其他参数筛选出符合条件的UID的集合，并从中返回一个匹配的UID。
* protocol参数为PROTO\_TYPE\_UDP时，若通过local，remote参数未筛选出符合条件的UID，则仅基于local参数筛选并返回匹配的UID。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| protocol | [ProtocolType](js-apis-net-connection.md#protocoltype23) | 是 | 网络协议的类型。 |
| local | [NetAddress](js-apis-net-connection.md#netaddress) | 是 | 源网络地址。 |
| remote | [NetAddress](js-apis-net-connection.md#netaddress) | 是 | 目标网络地址。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回应用程序的UID。如果不存在匹配的UID则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100301 | Incorrect usage in non-VPN application. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let protocol = connection.ProtocolType.PROTO_TYPE_TCP;
5. let local: connection.NetAddress = { address: '192.168.1.100', family: 1, port: 6666 };
6. let remote: connection.NetAddress = { address: '192.168.1.200', family: 1, port: 8888 };
7. connection.getConnectOwnerUid(protocol, local, remote).then((uid) => {
8. console.info(`uid: ${uid}`);
9. }).catch((error: BusinessError) => {
10. console.error(`getConnectOwnerUid failed. errorCode: ${error.code} message:${error.message}`);
11. });
```

## connection.getConnectOwnerUidSync23+

PhonePC/2in1TabletTVWearable

getConnectOwnerUidSync(protocol: ProtocolType, local: NetAddress, remote: NetAddress): number

用于查询发起指定网络连接的应用UID。使用同步方式返回。

说明

* 该接口仅限在VPN应用中调用。
* 调用接口时请设置local和remote参数的端口号。若未设置端口号或将端口号设置为0，接口会基于其他参数筛选出符合条件的UID的集合，并从中返回一个匹配的UID。
* protocol参数为PROTO\_TYPE\_UDP时，若通过local，remote参数未筛选出符合条件的UID，则仅基于local参数筛选并返回匹配的UID。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| protocol | [ProtocolType](js-apis-net-connection.md#protocoltype23) | 是 | 网络协议的类型。 |
| local | [NetAddress](js-apis-net-connection.md#netaddress) | 是 | 源网络地址。 |
| remote | [NetAddress](js-apis-net-connection.md#netaddress) | 是 | 目标网络地址。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回应用程序的UID。如果不存在匹配的UID则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100301 | Incorrect usage in non-VPN application. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let protocol = connection.ProtocolType.PROTO_TYPE_TCP;
5. let local: connection.NetAddress = { address: '192.168.1.100', family: 1, port: 6666 };
6. let remote: connection.NetAddress = { address: '192.168.1.200', family: 1, port: 8888 };
7. try {
8. let uid = connection.getConnectOwnerUidSync(protocol, local, remote);
9. console.info(`uid: ${uid}`);
10. } catch (e) {
11. let err = e as BusinessError;
12. console.error(`getConnectOwnerUid failed. errorCode: ${err.code} message:${err.message}`);
13. }
```

## connection.getDnsAscii23+

PhonePC/2in1TabletTVWearable

getDnsAscii(host: string, flag?: ConversionProcess): string

将Unicode编码形式的主机名转换为ASCII编码形式，并可通过可选的转换流程参数（conversionProcess）控制转换行为。

说明

conversionProcess设置为NO\_CONFIGURATION时，只能转换已正式分配含义的Unicode字符所对应的域名。

conversionProcess设置为ALLOW\_UNASSIGNED时，可以转换包含尚未分配含义的Unicode字符的域名。

conversionProcess设置为USE\_STD3\_ASCII\_RULES时，会在转换过程中强制按照STD-3 ASCII规则（即RFC 1123标准）对生成的ASCII域名进行检查。

传入参数中的数字和英文不做转码。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 要转换的主机名（host）。每个标签（点分隔的部分）长度不超过63字节。 |
| flag | [ConversionProcess](js-apis-net-connection.md#conversionprocess23) | 否 | 转换流程参数，默认值为NO\_CONFIGURATION。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回转换结果。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. let result = connection.getDnsAscii("www.示例.com", connection.ConversionProcess.NO_CONFIGURATION);
4. console.info(result);  // 预期结果：www.xn--fsq092h.com
5. let result = connection.getDnsAscii("www.example.com", connection.ConversionProcess.NO_CONFIGURATION);
6. console.info(result);  // 预期结果：www.example.com
```

## connection.getDnsUnicode23+

PhonePC/2in1TabletTVWearable

getDnsUnicode(host: string, flag?: ConversionProcess): string

使用Punycode编码方式，将ASCII编码形式的主机名转换为Unicode编码形式，并通过可选的conversionProcess参数控制转换行为。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 要转换的主机名（host）。 |
| flag | [ConversionProcess](js-apis-net-connection.md#conversionprocess23) | 否 | 转换流程参数，默认值为NO\_CONFIGURATION。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回转换结果。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. let result = connection.getDnsUnicode("www.xn--fsq092h.com", connection.ConversionProcess.NO_CONFIGURATION);
4. console.info(result);  // 预期结果：www.示例.com
5. let result = connection.getDnsUnicode("www.example.com", connection.ConversionProcess.NO_CONFIGURATION);
6. console.info(result);  // 预期结果：www.example.com
```

## NetConnection

PhonePC/2in1TabletTVWearable

网络连接对象类型。

说明

（1）设备从无网络状态转变为有网络状态时，将触发netAvailable事件、netCapabilitiesChange事件和netConnectionPropertiesChange事件；

（2）接收到netAvailable事件后，若设备从有网络状态转变为无网络状态，将触发netLost事件；

（3）若未接收到netAvailable事件，则将直接接收到netUnavailable事件；

（4）设备从WiFi网络切换至蜂窝网络时，将先触发netLost事件（WiFi丢失），随后触发netAvailable事件（蜂窝可用）。

### register

PhonePC/2in1TabletTVWearable

register(callback: AsyncCallback<void>): void

订阅指定网络状态变化的通知。如需监听特定事件，确保调用on监听事件后再调用register进行注册。

注意

使用完register接口后需要及时调用unregister取消注册。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当订阅指定网络状态变化的通知成功，error为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2101008 | The callback already exists. |
| 2101022 | The number of requests exceeded the maximum allowed. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let netCon: connection.NetConnection = connection.createNetConnection();
5. netCon.register((error: BusinessError) => {
6. console.error(JSON.stringify(error));
7. });
```

### unregister

PhonePC/2in1TabletTVWearable

unregister(callback: AsyncCallback<void>): void

取消订阅默认网络状态变化的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当取消订阅指定网络状态变化的通知成功，error为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2101007 | The callback does not exist. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let netCon: connection.NetConnection = connection.createNetConnection();
5. netCon.unregister((error: BusinessError) => {
6. console.error(JSON.stringify(error));
7. });
```

### on('netAvailable')

PhonePC/2in1TabletTVWearable

on(type: 'netAvailable', callback: Callback<NetHandle>): void

订阅网络可用事件。此接口需在调用register接口之前调用。若无需接收网络状态变化的回调通知，应使用unregister取消订阅默认的网络状态变化通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅事件，固定为'netAvailable'。  netAvailable：数据网络可用事件。 |
| callback | Callback<[NetHandle](js-apis-net-connection.md#nethandle)> | 是 | 回调函数，返回数据网络句柄。 |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 创建NetConnection对象。
5. let netCon: connection.NetConnection = connection.createNetConnection();

7. // 先使用on接口订阅网络可用事件。
8. netCon.on('netAvailable', (data: connection.NetHandle) => {
9. console.info("Succeeded to get data: " + JSON.stringify(data));
10. });

12. // 注册网络状态变化事件。此接口要在调用on后调用。
13. netCon.register((error: BusinessError) => {
14. console.error(JSON.stringify(error));
15. });

17. // 使用unregister接口取消订阅网络可用事件。
18. netCon.unregister((error: BusinessError) => {
19. console.error(JSON.stringify(error));
20. });
```

### on('netBlockStatusChange')

PhonePC/2in1TabletTVWearable

on(type: 'netBlockStatusChange', callback: Callback<NetBlockStatusInfo>): void

订阅网络阻塞状态事件。此接口需要在调用register接口之前调用。若无需接收网络状态变化的回调通知，应使用unregister取消订阅默认的网络状态变化通知。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅事件，固定为'netBlockStatusChange'。  netBlockStatusChange：网络阻塞状态事件。 |
| callback | Callback<[NetBlockStatusInfo](js-apis-net-connection.md#netblockstatusinfo11)> | 是 | 回调函数，获取网络阻塞状态信息。 |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 创建NetConnection对象。
5. let netCon: connection.NetConnection = connection.createNetConnection();

7. // 先使用on接口订阅网络阻塞状态事件。
8. netCon.on('netBlockStatusChange', (data: connection.NetBlockStatusInfo) => {
9. console.info("Succeeded to get data: " + JSON.stringify(data));
10. });

12. // 注册网络状态变化事件。此接口要在调用on后调用。
13. netCon.register((error: BusinessError) => {
14. console.error(JSON.stringify(error));
15. });

17. // 使用unregister接口取消订阅网络阻塞状态事件。
18. netCon.unregister((error: BusinessError) => {
19. console.error(JSON.stringify(error));
20. });
```

### on('netCapabilitiesChange')

PhonePC/2in1TabletTVWearable

on(type: 'netCapabilitiesChange', callback: Callback<NetCapabilityInfo>): void

订阅网络能力变化事件。此接口要在register接口调用前调用，不需要网络状态变化回调通知时，使用unregister取消订阅默认网络状态变化的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅事件，固定为'netCapabilitiesChange'。  netCapabilitiesChange：网络能力变化事件。 |
| callback | Callback<[NetCapabilityInfo](js-apis-net-connection.md#netcapabilityinfo10)> | 是 | 回调函数，返回数据网络句柄(netHandle)和网络的能力信息(netCap)。 |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 创建NetConnection对象。
5. let netCon: connection.NetConnection = connection.createNetConnection();

7. // 先使用on接口订阅网络能力变化事件。
8. netCon.on('netCapabilitiesChange', (data: connection.NetCapabilityInfo) => {
9. console.info("Succeeded to get data: " + JSON.stringify(data));
10. });

12. // 注册网络状态变化事件。此接口要在调用on后调用。
13. netCon.register((error: BusinessError) => {
14. console.error(JSON.stringify(error));
15. });

17. // 使用unregister接口取消订阅网络能力变化事件。
18. netCon.unregister((error: BusinessError) => {
19. console.error(JSON.stringify(error));
20. });
```

### on('netConnectionPropertiesChange')

PhonePC/2in1TabletTVWearable

on(type: 'netConnectionPropertiesChange', callback: Callback<NetConnectionPropertyInfo>): void

订阅网络连接信息变化事件。此接口要在register接口调用前调用，不需要网络状态变化回调通知时，使用unregister取消订阅默认网络状态变化的通知。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅事件，固定为'netConnectionPropertiesChange'。  netConnectionPropertiesChange：网络连接信息变化事件。 |
| callback | Callback<[NetConnectionPropertyInfo](js-apis-net-connection.md#netconnectionpropertyinfo11)> | 是 | 回调函数，获取网络连接属性信息。 |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 创建NetConnection对象。
5. let netCon: connection.NetConnection = connection.createNetConnection();

7. // 先使用on接口订阅网络连接信息变化事件。
8. netCon.on('netConnectionPropertiesChange', (data: connection.NetConnectionPropertyInfo) => {
9. console.info("Succeeded to get data: " + JSON.stringify(data));
10. });

12. // 注册网络状态变化事件。此接口要在调用on后调用。
13. netCon.register((error: BusinessError) => {
14. console.error(JSON.stringify(error));
15. });

17. // 使用unregister接口取消订阅网络连接信息变化事件。
18. netCon.unregister((error: BusinessError) => {
19. console.error(JSON.stringify(error));
20. });
```

### on('netLost')

PhonePC/2in1TabletTVWearable

on(type: 'netLost', callback: Callback<NetHandle>): void

订阅网络丢失事件。此接口要在register接口调用前调用，不需要网络状态变化回调通知时，使用unregister取消订阅默认网络状态变化的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅事件，固定为'netLost'。  netLost：网络严重中断或正常断开事件。 |
| callback | Callback<[NetHandle](js-apis-net-connection.md#nethandle)> | 是 | 回调函数，数据网络句柄(netHandle)。 |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 创建NetConnection对象。
5. let netCon: connection.NetConnection = connection.createNetConnection();

7. // 先使用on接口订阅网络丢失事件。
8. netCon.on('netLost', (data: connection.NetHandle) => {
9. console.info("Succeeded to get data: " + JSON.stringify(data));
10. });

12. // 注册网络状态变化事件。此接口要在调用on后调用。
13. netCon.register((error: BusinessError) => {
14. console.error(JSON.stringify(error));
15. });

17. // 使用unregister接口取消订阅网络丢失事件。
18. netCon.unregister((error: BusinessError) => {
19. console.error(JSON.stringify(error));
20. });
```

### on('netUnavailable')

PhonePC/2in1TabletTVWearable

on(type: 'netUnavailable', callback: Callback<void>): void

订阅网络不可用事件。此接口要在register接口调用前调用，不需要网络状态变化回调通知时，使用unregister取消订阅默认网络状态变化的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅事件，固定为'netUnavailable'。  netUnavailable：网络不可用事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果。 |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 创建NetConnection对象。
5. let netCon: connection.NetConnection = connection.createNetConnection();

7. // 先使用on接口订阅网络不可用事件。
8. netCon.on('netUnavailable', () => {
9. console.info("Succeeded to get unavailable net event");
10. });

12. // 注册网络状态变化事件。此接口要在调用on后调用。
13. netCon.register((error: BusinessError) => {
14. console.error(JSON.stringify(error));
15. });

17. // 使用unregister接口取消订阅网络不可用事件。
18. netCon.unregister((error: BusinessError) => {
19. console.error(JSON.stringify(error));
20. });
```

## NetHandle

PhonePC/2in1TabletTVWearable

网络句柄。

在调用NetHandle的方法之前，需要先获取NetHandle对象。例如可通过[getDefaultNet](js-apis-net-connection.md#connectiongetdefaultnet)获取系统当前默认网络的网络句柄。

**系统能力**：SystemCapability.Communication.NetManager.Core

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| netId | number | 否 | 否 | 网络ID，取值为0代表没有默认网络，其余有效取值必须大于等于100。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

### bindSocket9+

PhonePC/2in1TabletTVWearable

bindSocket(socketParam: TCPSocket | UDPSocket, callback: AsyncCallback<void>): void

将TCPSocket或UDPSocket绑定到当前NetHandle对应的网络。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| socketParam | [TCPSocket](js-apis-socket.md#tcpsocket) | [UDPSocket](js-apis-socket.md#udpsocket) | 是 | 待绑定的TCPSocket或UDPSocket对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当TCPSocket或UDPSocket成功绑定到当前网络，error为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection, socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. interface Data {
5. message: ArrayBuffer,
6. remoteInfo: socket.SocketRemoteInfo
7. }

9. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
10. if (netHandle.netId == 0) {
11. // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
12. }
13. let tcp : socket.TCPSocket = socket.constructTCPSocketInstance();
14. let udp : socket.UDPSocket = socket.constructUDPSocketInstance();
15. let socketType = "TCPSocket";
16. if (socketType == "TCPSocket") {
17. tcp.bind({address:"192.168.xxx.xxx",
18. port:8080,
19. family:1} as socket.NetAddress, (error: Error) => {
20. if (error) {
21. console.error('bind fail');
22. return;
23. }
24. netHandle.bindSocket(tcp, (error: BusinessError, data: void) => {
25. if (error) {
26. console.error(`Failed to bind socket. Code:${error.code}, message:${error.message}`);
27. return;
28. } else {
29. console.info(JSON.stringify(data));
30. }
31. });
32. });
33. } else {
34. let callback: (value: Data) => void = (value: Data) => {
35. console.info("on message, message:" + value.message + ", remoteInfo:" + value.remoteInfo);
36. };
37. udp.bind({address:"192.168.xxx.xxx",
38. port:8080,
39. family:1} as socket.NetAddress, (error: BusinessError) => {
40. if (error) {
41. console.error(`Failed to bind. Code:${error.code}, message:${error.message}`);
42. return;
43. }
44. udp.on('message', (data: Data) => {
45. console.info("Succeeded to get data: " + JSON.stringify(data));
46. });
47. netHandle.bindSocket(udp, (error: BusinessError, data: void) => {
48. if (error) {
49. console.error(`Failed to bind socket. Code:${error.code}, message:${error.message}`);
50. return;
51. } else {
52. console.info(JSON.stringify(data));
53. }
54. });
55. });
56. }
57. })
```

### bindSocket9+

PhonePC/2in1TabletTVWearable

bindSocket(socketParam: TCPSocket | UDPSocket): Promise<void>

将TCPSocket或UDPSocket绑定到当前NetHandle对应的网络。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| socketParam | [TCPSocket](js-apis-socket.md#tcpsocket) | [UDPSocket](js-apis-socket.md#udpsocket) | 是 | 待绑定的TCPSocket或UDPSocket对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection, socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. interface Data {
5. message: ArrayBuffer,
6. remoteInfo: socket.SocketRemoteInfo
7. }

9. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
10. if (netHandle.netId == 0) {
11. // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
12. return;
13. }
14. let tcp : socket.TCPSocket = socket.constructTCPSocketInstance();
15. let udp : socket.UDPSocket = socket.constructUDPSocketInstance();
16. let socketType = "TCPSocket";
17. if (socketType == "TCPSocket") {
18. tcp.bind({address:"192.168.xxx.xxx",
19. port:8080,
20. family:1} as socket.NetAddress, (error: Error) => {
21. if (error) {
22. console.error('bind fail');
23. return;
24. }
25. netHandle.bindSocket(tcp).then(() => {
26. console.info("bind socket success");
27. }).catch((error: BusinessError) => {
28. console.error(`Failed to bind socket. Code:${error.code}, message:${error.message}`);
29. });
30. });
31. } else {
32. let callback: (value: Data) => void = (value: Data) => {
33. console.info("on message, message:" + value.message + ", remoteInfo:" + value.remoteInfo);
34. }
35. udp.bind({address:"192.168.xxx.xxx",
36. port:8080,
37. family:1} as socket.NetAddress, (error: BusinessError) => {
38. if (error) {
39. console.error(`Failed to bind. Code:${error.code}, message:${error.message}`);
40. return;
41. }
42. udp.on('message', (data: Data) => {
43. console.info("Succeeded to get data: " + JSON.stringify(data));
44. });
45. netHandle.bindSocket(udp).then(() => {
46. console.info("bind socket success");
47. }).catch((error: BusinessError) => {
48. console.error(`Failed to bind socket. Code:${error.code}, message:${error.message}`);
49. });
50. });
51. }
52. });
```

### getAddressesByName

PhonePC/2in1TabletTVWearable

getAddressesByName(host: string, callback: AsyncCallback<Array<NetAddress>>): void

使用当前NetHandle对应的网络解析主机名获取到的所有IP地址。使用callback异步回调。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要解析的主机名。例如："[www.example.com"。](http://www.example.com) |
| callback | AsyncCallback<Array<[NetAddress](js-apis-net-connection.md#netaddress)>> | 是 | 回调函数。当使用对应网络解析主机名成功获取所有IP地址，error为undefined，data为获取到的所有IP地址；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
5. if (netHandle.netId == 0) {
6. // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
7. return;
8. }
9. let host = "www.example.com";
10. netHandle.getAddressesByName(host, (error: BusinessError, data: connection.NetAddress[]) => {
11. if (error) {
12. console.error(`Failed to get addresses. Code:${error.code}, message:${error.message}`);
13. return;
14. }
15. console.info("Succeeded to get data: " + JSON.stringify(data));
16. });
17. });
```

### getAddressesByName

PhonePC/2in1TabletTVWearable

getAddressesByName(host: string): Promise<Array<NetAddress>>

使用当前NetHandle对应的网络解析主机名获取到的所有IP地址。使用Promise异步回调。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要解析的主机名。例如："[www.example.com"。](http://www.example.com) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[NetAddress](js-apis-net-connection.md#netaddress)>> | Promise对象，返回所有IP地址。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
4. if (netHandle.netId == 0) {
5. // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
6. return;
7. }
8. let host = "www.example.com";
9. netHandle.getAddressesByName(host).then((data: connection.NetAddress[]) => {
10. console.info("Succeeded to get data: " + JSON.stringify(data));
11. });
12. });
```

### getAddressesByNameWithOptions23+

PhonePC/2in1TabletTVWearable

getAddressesByNameWithOptions(host: string, option?: QueryOptions): Promise<Array<NetAddress>>

使用当前NetHandle对应的网络基于指定IP类型进行DNS解析。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要解析的主机名。例如："[www.example.com"。](http://www.example.com) |
| option | [QueryOptions](js-apis-net-connection.md#queryoptions23) | 否 | 需要查询的IP类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[NetAddress](js-apis-net-connection.md#netaddress)>> | Promise对象，返回查询到的IP地址。返回值中的port字段固定为0，无需关注。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
5. if (netHandle.netId == 0) {
6. // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
7. return;
8. }
9. let host = "www.example.com";
10. let option: connection.QueryOptions = {
11. family: connection.FamilyType.FAMILY_TYPE_IPV4
12. };
13. netHandle.getAddressesByNameWithOptions(host, option).then((data: connection.NetAddress[]) => {
14. console.info(`Succeeded to get data: ${JSON.stringify(data)}`);
15. }).catch((err: BusinessError) => {
16. console.error(`get ERROR msg: ${JSON.stringify(err)}`)
17. });
18. });
```

### getAddressByName

PhonePC/2in1TabletTVWearable

getAddressByName(host: string, callback: AsyncCallback<NetAddress>): void

使用当前NetHandle对应的网络解析主机名获取到的第一个IP地址。使用callback异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要解析的主机名。例如："[www.example.com"。](http://www.example.com) |
| callback | AsyncCallback<[NetAddress](js-apis-net-connection.md#netaddress)> | 是 | 回调函数。当使用对应网络解析主机名获取第一个IP地址成功，error为undefined，data为获取的第一个IP地址；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
5. if (netHandle.netId == 0) {
6. // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
7. return;
8. }
9. let host = "www.example.com";
10. netHandle.getAddressByName(host, (error: BusinessError, data: connection.NetAddress) => {
11. if (error) {
12. console.error(`Failed to get address. Code:${error.code}, message:${error.message}`);
13. return;
14. }
15. console.info("Succeeded to get data: " + JSON.stringify(data));
16. });
17. });
```

### getAddressByName

PhonePC/2in1TabletTVWearable

getAddressByName(host: string): Promise<NetAddress>

使用当前NetHandle对应的网络解析主机名获取到的第一个IP地址。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要解析的主机名。例如："[www.example.com"。](http://www.example.com) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NetAddress](js-apis-net-connection.md#netaddress)> | Promise对象，返回获取到的第一个IP地址。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](errorcode-net-connection.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';

3. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
4. if (netHandle.netId == 0) {
5. // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
6. return;
7. }
8. let host = "www.example.com";
9. netHandle.getAddressByName(host).then((data: connection.NetAddress) => {
10. console.info("Succeeded to get data: " + JSON.stringify(data));
11. });
12. });
```

## NetCap

PhonePC/2in1TabletTVWearable

网络具体能力。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NET\_CAPABILITY\_MMS | 0 | 表示网络可以访问运营商的MMSC（Multimedia Message Service，多媒体短信服务）发送和接收彩信。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| NET\_CAPABILITY\_NOT\_METERED | 11 | 表示网络流量未被计费。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| NET\_CAPABILITY\_INTERNET | 12 | 表示该网络应具有访问Internet的能力，此能力由网络提供者设置，但该网络访问Internet的连通性并未被网络管理成功验证。网络连通性可以通过NET\_CAPABILITY\_VALIDATED和NET\_CAPABILITY\_CHECKING\_CONNECTIVITY判断。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| NET\_CAPABILITY\_NOT\_VPN | 15 | 表示网络不使用VPN（Virtual Private Network，虚拟专用网络）。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| NET\_CAPABILITY\_VALIDATED | 16 | 表示网络管理通过该网络与华为云地址成功建立连接，此能力由网络管理模块设置。  **注意：** 网络管理可能会与华为云地址建立连接失败，导致网络能力不具备此标记位，但不完全代表该网络无法访问互联网。另外，对于新完成连接的网络，由于网络正在进行连通性验证，此值可能无法反映真实的验证结果。对此，应用可以通过NET\_CAPABILITY\_CHECKING\_CONNECTIVITY12+检查网络是否正在检测连通性。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| NET\_CAPABILITY\_PORTAL12+ | 17 | 表示系统发现该网络存在强制网络门户，需要用户登陆认证，该能力由网络管理模块设置。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| NET\_CAPABILITY\_CHECKING\_CONNECTIVITY12+ | 31 | 表示网络管理正在检验当前网络的连通性，此值会在网络连接时设置。当此值存在时，NET\_CAPABILITY\_VALIDATED的值不准确，连通性检测结束后不再设置，此时可以通过判断NetCap是否包含NET\_CAPABILITY\_VALIDATED判断连通性。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## NetBearType

PhonePC/2in1TabletTVWearable

网络类型。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BEARER\_CELLULAR | 0 | 蜂窝网络。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| BEARER\_WIFI | 1 | Wi-Fi网络。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| BEARER\_BLUETOOTH12+ | 2 | 蓝牙网络。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| BEARER\_ETHERNET | 3 | 以太网网络。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| BEARER\_VPN12+ | 4 | VPN网络。 |

## ConversionProcess23+

PhonePC/2in1TabletTVWearable

ASCII/Unicode转码转换流程参数的枚举。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_CONFIGURATION | 0 | 仅允许转换已分配的Unicode代码点的域名（Unicode为每个字符分配一个唯一的数字，这个数字就叫做代码点）。 |
| ALLOW\_UNASSIGNED | 1 | 允许转换包含未分配Unicode代码点的域名(在Unicode字符集中，并非所有代码点都已分配字符，即未分配Unicode代码点)。 |
| USE\_STD3\_ASCII\_RULES | 2 | 在转换过程中，强制使用STD-3 ASCII规则（即RFC 1123标准）检查生成的ASCII域名。 |

## HttpProxy10+

PhonePC/2in1TabletTVWearable

网络代理配置信息

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| host | string | 否 | 否 | 代理服务器主机名。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| port | number | 否 | 否 | 主机端口。取值范围[0,65535]。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| exclusionList | Array<string> | 否 | 否 | 不使用代理的主机名列表，主机名支持域名、IP地址以及通配符形式，详细匹配规则如下：  1、域名匹配规则：  （1）完全匹配：代理服务器主机名只要与列表中的任意一个主机名完全相同，就可以匹配。  （2）包含匹配：代理服务器主机名只要包含列表中的任意一个主机名，就可以匹配。  例如，如果在主机名列表中设置了 “ample.com”，则 “ample.com”、“www.ample.com”、“ample.com:80”都会被匹配，而 “www.example.com”、“ample.com.org”则不会被匹配。  2、IP地址匹配规则：代理服务器主机名只要与列表中的任意一个IP地址完全相同，就可以匹配。  3、域名跟IP地址可以同时添加到列表中进行匹配。  4、单个“\*”是唯一有效的通配符，当列表中只有通配符时，将与所有代理服务器主机名匹配，表示禁用代理。通配符只能单独添加，不可以与其他域名、IP地址一起添加到列表中，否则通配符将不生效。  5、匹配规则不区分主机名大小写。  6、匹配主机名时，不考虑http和https等协议前缀。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| username12+ | string | 否 | 是 | 使用代理的用户名。  **说明:** 需同时设置password参数才会生效。 |
| password12+ | string | 否 | 是 | 使用代理的用户密码。  **说明:** 需同时设置username参数才会生效。 |

## NetSpecifier

PhonePC/2in1TabletTVWearable

提供承载数据网络能力的实例。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| netCapabilities | [NetCapabilities](js-apis-net-connection.md#netcapabilities) | 否 | 否 | 存储数据网络的传输能力和承载类型。 |
| bearerPrivateIdentifier | string | 否 | 是 | 网络标识符，蜂窝网络的标识符是"slot0"（对应SIM卡1）、"slot1"（对应SIM卡2）。从API12开始可以通过传递注册的WLAN热点信息表示应用希望激活的指定的WLAN网络。 |

**示例：**

```
1. import { connection } from '@kit.NetworkKit';
2. import { wifiManager } from '@kit.ConnectivityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let config: wifiManager.WifiDeviceConfig = {
6. ssid: "TEST",
7. preSharedKey: "**********",
8. securityType: wifiManager.WifiSecurityType.WIFI_SEC_TYPE_PSK
9. };
10. // 通过wifiManager.addCandidateConfig获取注册WLAN的networkId。
11. wifiManager.addCandidateConfig(config,(error,networkId) => {
12. let netConnectionWlan = connection.createNetConnection({
13. netCapabilities: {
14. bearerTypes: [connection.NetBearType.BEARER_WIFI]
15. },
16. bearerPrivateIdentifier: `${networkId}`
17. });
18. netConnectionWlan.register((error: BusinessError) => {
19. console.error(JSON.stringify(error));
20. });
21. });
```

## NetCapabilityInfo10+

PhonePC/2in1TabletTVWearable

提供承载数据网络能力的实例。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| netHandle | [NetHandle](js-apis-net-connection.md#nethandle) | 否 | 否 | 网络句柄。 |
| netCap | [NetCapabilities](js-apis-net-connection.md#netcapabilities) | 否 | 否 | 存储数据网络的传输能力和承载类型。 |

## NetCapabilities

PhonePC/2in1TabletTVWearable

网络的能力集。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| linkUpBandwidthKbps | number | 否 | 是 | 上行（设备到网络）带宽，单位(kb/s)。0表示无法评估当前网络带宽。 |
| linkDownBandwidthKbps | number | 否 | 是 | 下行（网络到设备）带宽，单位(kb/s)。0表示无法评估当前网络带宽。 |
| networkCap | Array<[NetCap](js-apis-net-connection.md#netcap)> | 否 | 是 | 网络具体能力。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| bearerTypes | Array<[NetBearType](js-apis-net-connection.md#netbeartype)> | 否 | 否 | 网络类型。数组里面只包含了一种网络类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## NetConnectionPropertyInfo11+

PhonePC/2in1TabletTVWearable

网络连接信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| netHandle | [NetHandle](js-apis-net-connection.md#nethandle) | 否 | 否 | 网络句柄。 |
| connectionProperties | [ConnectionProperties](js-apis-net-connection.md#connectionproperties) | 否 | 否 | 网络连接信息。 |

## NetBlockStatusInfo11+

PhonePC/2in1TabletTVWearable

获取网络状态信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| netHandle | [NetHandle](js-apis-net-connection.md#nethandle) | 否 | 否 | 网络句柄。 |
| blocked | boolean | 否 | 否 | 标识当前网络是否是堵塞状态。true：标识当前网络是堵塞状态；false：标识当前网络不是堵塞状态。 |

## ConnectionProperties

PhonePC/2in1TabletTVWearable

网络连接信息。

注意

linkAddresses、routes和dnses可能为空，需要做好空值保护，建议使用前先判断对象是否存在。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| interfaceName | string | 否 | 否 | 网卡名称。 |
| domains | string | 否 | 否 | 域名。 |
| linkAddresses | Array<[LinkAddress](js-apis-net-connection.md#linkaddress)> | 否 | 否 | 链路信息。 |
| routes | Array<[RouteInfo](js-apis-net-connection.md#routeinfo)> | 否 | 否 | 路由信息。 |
| dnses | Array<[NetAddress](js-apis-net-connection.md#netaddress)> | 否 | 否 | 网络地址，参考[NetAddress](js-apis-net-connection.md#netaddress)。 |
| mtu | number | 否 | 否 | 最大传输单元。 |

## RouteInfo

PhonePC/2in1TabletTVWearable

网络路由信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| interface | string | 否 | 否 | 网卡名称。 |
| destination | [LinkAddress](js-apis-net-connection.md#linkaddress) | 否 | 否 | 目的地址。 |
| gateway | [NetAddress](js-apis-net-connection.md#netaddress) | 否 | 否 | 网关地址。 |
| hasGateway | boolean | 否 | 否 | 是否有网关。true：有网关；false：无网关。 |
| isDefaultRoute | boolean | 否 | 否 | 是否为默认路由。true：默认路由；false：非默认路由。  **说明：** IPv4默认路由是指目的地址为0.0.0.0/0的路由；IPv6默认路由是指目的地址为::/0的路由。 |
| isExcludedRoute20+ | boolean | 否 | 是 | 是否为排除路由。true表示排除路由，false表示非排除路由，默认值为false。 |

## LinkAddress

PhonePC/2in1TabletTVWearable

网络链路信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | [NetAddress](js-apis-net-connection.md#netaddress) | 否 | 否 | 链路地址。 |
| prefixLength | number | 否 | 否 | 链路地址前缀的长度。 |

## NetAddress

PhonePC/2in1TabletTVWearable

网络地址。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 地址。 |
| family | number | 否 | 是 | IPv4 = 1，IPv6 = 2，默认IPv4。 |
| port | number | 否 | 是 | 端口，取值范围[0, 65535]，默认值为0。 |

## HttpRequest

PhonePC/2in1TabletTVWearable

type HttpRequest = http.HttpRequest

定义一个HTTP请求，可以通过[http.createHttp](js-apis-http.md#httpcreatehttp)创建。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| http.HttpRequest | 定义HTTP请求任务。在调用HttpRequest提供的API之前。 |

## TCPSocket

PhonePC/2in1TabletTVWearable

type TCPSocket = socket.TCPSocket

定义一个TCPSocket对象，可以通过[socket.constructTCPSocketInstance](js-apis-socket.md#socketconstructtcpsocketinstance)创建。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| socket.TCPSocket | 定义一个TCPSocket连接。 |

## UDPSocket

PhonePC/2in1TabletTVWearable

type UDPSocket = socket.UDPSocket

定义一个UDPSocket对象，可以通过[socket.constructUDPSocketInstance](js-apis-socket.md#socketconstructudpsocketinstance)创建。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| socket.UDPSocket | 定义UDPSocket连接。 |

## NetIpMacInfo22+

PhonePC/2in1TabletTVWearable

IP邻居表条目信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ipAddress | [NetAddress](js-apis-net-connection.md#netaddress) | 否 | 否 | IP地址相关信息。 |
| iface | string | 否 | 否 | 网卡名。 |
| macAddress | string | 否 | 否 | MAC地址。 |

## ProtocolType23+

PhonePC/2in1TabletTVWearable

网络协议类型的枚举。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PROTO\_TYPE\_TCP | 6 | TCP网络协议。 |
| PROTO\_TYPE\_UDP | 17 | UDP网络协议。 |
