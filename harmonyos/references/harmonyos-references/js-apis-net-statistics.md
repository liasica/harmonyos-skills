---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-statistics
title: @ohos.net.statistics (流量管理)
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > ArkTS API > @ohos.net.statistics (流量管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d995cce79dc4931a625a8c391fcb8de98ab6445e8179bf2b1fb1d4e9d0a19f63
---

流量管理模块提供获取指定网卡实时上行、下行流量等能力。

说明

本模块首批接口从 API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { statistics } from '@kit.NetworkKit';
```

## statistics.getIfaceRxBytes

PhonePC/2in1TabletTVWearable

getIfaceRxBytes(nic: string, callback: AsyncCallback<number>): void

获取指定网卡实时下行流量，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| nic | string | 是 | 指定查询的网卡名。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当成功获取网卡实时下行流量时，error 为 undefined，stats 为获取到的网卡实时下行流量(单位:字节)；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](errorcode-net-statistics.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2103005 | Failed to read the system map. |
| 2103011 | Failed to create a system map. |
| 2103012 | Failed to obtain the NIC name. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { statistics } from '@kit.NetworkKit';

4. statistics.getIfaceRxBytes("wlan0", (error: BusinessError, stats: number) => {
5. console.error(JSON.stringify(error));
6. console.info(JSON.stringify(stats));
7. });
```

## statistics.getIfaceRxBytes

PhonePC/2in1TabletTVWearable

getIfaceRxBytes(nic: string): Promise<number>

获取指定网卡实时下行流量，使用 Promise 异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| nic | string | 是 | 指定查询的网卡名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以 Promise 形式返回获取结果。返回网卡实时下行流量(单位:字节)。 |

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](errorcode-net-statistics.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2103005 | Failed to read the system map. |
| 2103011 | Failed to create a system map. |
| 2103012 | Failed to obtain the NIC name. |

**示例：**

```
1. import { statistics } from '@kit.NetworkKit';

3. statistics.getIfaceRxBytes("wlan0").then((stats: number) => {
4. console.info(JSON.stringify(stats));
5. });
```

## statistics.getIfaceTxBytes

PhonePC/2in1TabletTVWearable

getIfaceTxBytes(nic: string, callback: AsyncCallback<number>): void

获取指定网卡实时上行流量，使用 callback 异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| nic | string | 是 | 指定查询的网卡名。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当成功获取网卡实时上行流量时，error 为 undefined，stats 为获取到的网卡实时上行流量(单位:字节)；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](errorcode-net-statistics.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2103005 | Failed to read the system map. |
| 2103011 | Failed to create a system map. |
| 2103012 | Failed to obtain the NIC name. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { statistics } from '@kit.NetworkKit';

4. statistics.getIfaceTxBytes("wlan0", (error: BusinessError, stats: number) => {
5. console.error(JSON.stringify(error));
6. console.info(JSON.stringify(stats));
7. });
```

## statistics.getIfaceTxBytes

PhonePC/2in1TabletTVWearable

getIfaceTxBytes(nic: string): Promise<number>

获取指定网卡实时上行流量，使用 Promise 异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| nic | string | 是 | 指定查询的网卡名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以 Promise 形式返回获取结果。返回网卡实时上行流量(单位:字节)。 |

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](errorcode-net-statistics.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2103005 | Failed to read the system map. |
| 2103011 | Failed to create a system map. |
| 2103012 | Failed to obtain the NIC name. |

**示例：**

```
1. import { statistics } from '@kit.NetworkKit';

3. statistics.getIfaceTxBytes("wlan0").then((stats: number) => {
4. console.info(JSON.stringify(stats));
5. });
```

## statistics.getCellularRxBytes

PhonePC/2in1TabletTVWearable

getCellularRxBytes(callback: AsyncCallback<number>): void

获取蜂窝实时下行流量，使用 callback 异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。当成功获取蜂窝实时下行流量时，error 为 undefined，stats 为获取到的蜂窝实时下行流量(单位:字节)；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](errorcode-net-statistics.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2103005 | Failed to read the system map. |
| 2103011 | Failed to create a system map. |
| 2103012 | Failed to obtain the NIC name. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { statistics } from '@kit.NetworkKit';

4. statistics.getCellularRxBytes((error: BusinessError, stats: number) => {
5. console.error(JSON.stringify(error));
6. console.info(JSON.stringify(stats));
7. });
```

## statistics.getCellularRxBytes

PhonePC/2in1TabletTVWearable

getCellularRxBytes(): Promise<number>

获取蜂窝实时下行流量，使用 Promise 异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以 Promise 形式返回获取结果。返回蜂窝实时下行流量(单位:字节)。 |

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](errorcode-net-statistics.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2103005 | Failed to read the system map. |
| 2103011 | Failed to create a system map. |
| 2103012 | Failed to obtain the NIC name. |

**示例：**

```
1. import { statistics } from '@kit.NetworkKit';

3. statistics.getCellularRxBytes().then((stats: number) => {
4. console.info(JSON.stringify(stats));
5. });
```

## statistics.getCellularTxBytes

PhonePC/2in1TabletTVWearable

getCellularTxBytes(callback: AsyncCallback<number>): void

获取蜂窝实时上行流量，使用 callback 异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。当成功获取蜂窝实时上行流量时，error 为 undefined，stats 为获取到的蜂窝实时上行流量(单位:字节)；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](errorcode-net-statistics.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2103005 | Failed to read the system map. |
| 2103011 | Failed to create a system map. |
| 2103012 | Failed to obtain the NIC name. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { statistics } from '@kit.NetworkKit';

4. statistics.getCellularTxBytes((error: BusinessError, stats: number) => {
5. console.error(JSON.stringify(error));
6. console.info(JSON.stringify(stats));
7. });
```

## statistics.getCellularTxBytes

PhonePC/2in1TabletTVWearable

getCellularTxBytes(): Promise<number>

获取蜂窝实时上行流量，使用 Promise 异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以 Promise 形式返回获取结果。返回蜂窝实时上行流量(单位:字节)。 |

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](errorcode-net-statistics.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2103005 | Failed to read the system map. |
| 2103011 | Failed to create a system map. |
| 2103012 | Failed to obtain the NIC name. |

**示例：**

```
1. import { statistics } from '@kit.NetworkKit';

3. statistics.getCellularTxBytes().then((stats: number) => {
4. console.info(JSON.stringify(stats));
5. });
```

## statistics.getAllRxBytes

PhonePC/2in1TabletTVWearable

getAllRxBytes(callback: AsyncCallback<number>): void

获取所有网卡实时下行流量，使用 callback 异步回调。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。当成功获取所有网卡实时下行流量，error 为 undefined，stats 为获取到的所有网卡实时下行流量(单位:字节)；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](errorcode-net-statistics.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2103005 | Failed to read the system map. |
| 2103011 | Failed to create a system map. |

**示例：**

```
1. import { statistics } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. statistics.getAllRxBytes((error: BusinessError, stats: number) => {
5. console.error(JSON.stringify(error));
6. console.info(JSON.stringify(stats));
7. });
```

## statistics.getAllRxBytes

PhonePC/2in1TabletTVWearable

getAllRxBytes(): Promise<number>

获取所有网卡实时下行流量，使用 Promise 异步回调。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以 Promise 形式返回获取结果。返回所有网卡实时下行流量(单位:字节)。 |

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](errorcode-net-statistics.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2103005 | Failed to read the system map. |
| 2103011 | Failed to create a system map. |

**示例：**

```
1. import { statistics } from '@kit.NetworkKit';

3. statistics.getAllRxBytes().then((stats: number) => {
4. console.info(JSON.stringify(stats));
5. });
```

## statistics.getAllTxBytes

PhonePC/2in1TabletTVWearable

getAllTxBytes(callback: AsyncCallback<number>): void

获取所有网卡实时上行流量，使用 callback 异步回调。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。当成功获取所有网卡实时上行流量，error 为 undefined，stats 为获取到的所有网卡实时上行流量(单位:字节)；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](errorcode-net-statistics.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2103005 | Failed to read the system map. |
| 2103011 | Failed to create a system map. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { statistics } from '@kit.NetworkKit';

4. statistics.getAllTxBytes((error: BusinessError, stats: number) => {
5. console.error(JSON.stringify(error));
6. console.info(JSON.stringify(stats));
7. });
```

## statistics.getAllTxBytes

PhonePC/2in1TabletTVWearable

getAllTxBytes(): Promise<number>

获取所有网卡实时上行流量，使用 Promise 异步回调。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以 Promise 形式返回获取结果。返回所有网卡实时上行流量(单位:字节)。 |

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](errorcode-net-statistics.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2103005 | Failed to read the system map. |
| 2103011 | Failed to create a system map. |

**示例：**

```
1. import { statistics } from '@kit.NetworkKit';

3. statistics.getAllTxBytes().then((stats: number) => {
4. console.info(JSON.stringify(stats));
5. });
```

## statistics.getUidRxBytes

PhonePC/2in1TabletTVWearable

getUidRxBytes(uid: number, callback: AsyncCallback<number>): void

获取指定应用实时下行流量，使用 callback 异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | number | 是 | 指定查询的应用 uid。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当成功获取应用实时下行流量时，error 为 undefined，stats 为获取到的应用实时下行流量(单位:字节)；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](errorcode-net-statistics.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2103005 | Failed to read the system map. |
| 2103011 | Failed to create a system map. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { statistics } from '@kit.NetworkKit';

4. statistics.getUidRxBytes(20010038, (error: BusinessError, stats: number) => {
5. console.error(JSON.stringify(error));
6. console.info(JSON.stringify(stats));
7. });
```

## statistics.getUidRxBytes

PhonePC/2in1TabletTVWearable

getUidRxBytes(uid: number): Promise<number>

获取指定应用实时下行流量，使用 Promise 异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | number | 是 | 指定查询的应用 uid。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以 Promise 形式返回获取结果。返回指定应用实时下行流量(单位:字节)。 |

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](errorcode-net-statistics.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2103005 | Failed to read the system map. |
| 2103011 | Failed to create a system map. |

**示例：**

```
1. import { statistics } from '@kit.NetworkKit';

3. statistics.getUidRxBytes(20010038).then((stats: number) => {
4. console.info(JSON.stringify(stats));
5. });
```

## statistics.getUidTxBytes

PhonePC/2in1TabletTVWearable

getUidTxBytes(uid: number, callback: AsyncCallback<number>): void

获取指定应用实时上行流量，使用 callback 异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | number | 是 | 指定查询的应用 uid。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当成功获取应用实时上行流量时，error 为 undefined，stats 为获取到的应用实时上行流量(单位:字节)；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](errorcode-net-statistics.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2103005 | Failed to read the system map. |
| 2103011 | Failed to create a system map. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { statistics } from '@kit.NetworkKit';

4. statistics.getUidTxBytes(20010038, (error: BusinessError, stats: number) => {
5. console.error(JSON.stringify(error));
6. console.info(JSON.stringify(stats));
7. });
```

## statistics.getUidTxBytes

PhonePC/2in1TabletTVWearable

getUidTxBytes(uid: number): Promise<number>

获取指定应用实时上行流量，使用 Promise 异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | number | 是 | 指定查询的应用 uid。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以 Promise 形式返回获取结果。返回指定应用实时上行流量(单位:字节)。 |

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](errorcode-net-statistics.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2103005 | Failed to read the system map. |
| 2103011 | Failed to create a system map. |

**示例：**

```
1. import { statistics } from '@kit.NetworkKit';

3. statistics.getUidTxBytes(20010038).then((stats: number) => {
4. console.info(JSON.stringify(stats));
5. });
```

## statistics.getSockfdRxBytes11+

PhonePC/2in1TabletTVWearable

getSockfdRxBytes(sockfd: number, callback: AsyncCallback<number>): void

获取指定socket的下行流量信息，使用 callback 异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sockfd | number | 是 | 指定查询的socket的fd(file description)。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当成功获取socket的下行流量时，error 为 undefined，stats 为获取到的该socket的实时下行流量(单位:字节)；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](errorcode-net-statistics.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { statistics } from '@kit.NetworkKit';

4. let sockfd = 50; // 实际开发中需要先根据自己创建的socket获取到。
5. statistics.getSockfdRxBytes(sockfd, (error: BusinessError, stats: number) => {
6. console.error(JSON.stringify(error));
7. console.info(JSON.stringify(stats));
8. });
```

## statistics.getSockfdRxBytes11+

PhonePC/2in1TabletTVWearable

getSockfdRxBytes(sockfd: number): Promise<number>

获取指定socket的下行流量信息，使用 Promise 异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sockfd | number | 是 | 指定查询的socket的fd(file description)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以 Promise 形式返回获取结果，返回该socket的实时下行流量(单位:字节)。 |

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](errorcode-net-statistics.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { statistics } from '@kit.NetworkKit';

4. let sockfd = 50; // 实际开发中需要先根据自己创建的socket获取到。
5. statistics.getSockfdRxBytes(sockfd).then((stats: number) => {
6. console.info(JSON.stringify(stats));
7. }).catch((err: BusinessError) => {
8. console.error(JSON.stringify(err));
9. });
```

## statistics.getSockfdTxBytes11+

PhonePC/2in1TabletTVWearable

getSockfdTxBytes(sockfd: number, callback: AsyncCallback<number>): void

获取指定socket的上行流量信息，使用 callback 异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sockfd | number | 是 | 指定查询的socket的fd(file description)。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当成功获取socket的上行流量时，error 为 undefined，stats 为获取到的该socket的实时上行流量(单位:字节)；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](errorcode-net-statistics.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { statistics } from '@kit.NetworkKit';

4. let sockfd = 50; // 实际开发中需要先根据自己创建的socket获取到。
5. statistics.getSockfdTxBytes(sockfd, (error: BusinessError, stats: number) => {
6. console.error(JSON.stringify(error));
7. console.info(JSON.stringify(stats));
8. });
```

## statistics.getSockfdTxBytes11+

PhonePC/2in1TabletTVWearable

getSockfdTxBytes(sockfd: number): Promise<number>

获取指定socket的上行流量信息，使用 Promise 异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sockfd | number | 是 | 指定查询的socket的fd(file description)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以 Promise 形式返回获取结果，返回该socket的实时上行流量(单位:字节)。 |

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](errorcode-net-statistics.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { statistics } from '@kit.NetworkKit';

4. let sockfd = 50; // 实际开发中需要先根据自己创建的socket获取到。
5. statistics.getSockfdTxBytes(sockfd).then((stats: number) => {
6. console.info(JSON.stringify(stats));
7. }).catch((err: BusinessError) => {
8. console.error(JSON.stringify(err));
9. });
```

## statistics.getSelfTrafficStats22+

PhonePC/2in1TabletTVWearable

getSelfTrafficStats(networkInfo: NetworkInfo): Promise<NetStatsInfo>

获取指定时间段内，本应用在指定网络中的流量使用情况。使用Promise异步回调。

说明

* 当前只支持获取蜂窝和Wi-Fi流量使用情况。
* 当前只支持获取31天之内的流量使用情况，如果参数中传入的时间戳早于当前系统时间31天，会返回错误码2103019。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| networkInfo | [NetworkInfo](js-apis-net-statistics.md#networkinfo22) | 是 | 指定查询的网络信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NetStatsInfo](js-apis-net-statistics.md#netstatsinfo22)> | Promise对象，返回应用历史流量统计信息。 |

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](errorcode-net-statistics.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2103017 | Failed to read the database. |
| 2103019 | The timestamp in param is invalid. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { connection, statistics } from '@kit.NetworkKit';

4. let networkInfo: statistics.NetworkInfo = {
5. type: connection.NetBearType.BEARER_CELLULAR,
6. startTime: Math.floor(Date.now() / 1000) - 86400 * 31,
7. endTime: Math.floor(Date.now() / 1000),
8. simId: 1,
9. }

11. statistics.getSelfTrafficStats(networkInfo).then((stats: statistics.NetStatsInfo) => {
12. console.info('getSelfTrafficStats success : ' + JSON.stringify(stats));
13. }).catch((err: BusinessError) => {
14. console.error('getSelfTrafficStats error. code: ' + `${err.code}` + ', message: ' + `${err.message}`);
15. });
```

## NetBearType12+

PhonePC/2in1TabletTVWearable

type NetBearType = connection.NetBearType

网络类型。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 类型 | 说明 |
| --- | --- |
| [connection.NetBearType](js-apis-net-connection.md#netbeartype) | 枚举网络类型。 |

## NetworkInfo22+

PhonePC/2in1TabletTVWearable

网络信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [NetBearType](js-apis-net-statistics.md#netbeartype12) | 否 | 否 | 网络类型。  **注意：** 当type为蜂窝网络时，需指定simId字段。 |
| startTime | number | 否 | 否 | 开始时间戳(单位：秒)。 |
| endTime | number | 否 | 否 | 结束时间戳(单位：秒)。 |
| simId | number | 否 | 是 | SIM卡ID。默认值为uint32\_t类型最大值。  **注意：** 当type为蜂窝网络时，需指定本字段。 |

## NetStatsInfo22+

PhonePC/2in1TabletTVWearable

获取的历史流量信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rxBytes | number | 否 | 否 | 流量下行数据(单位：字节)。 |
| txBytes | number | 否 | 否 | 流量上行数据(单位：字节)。 |
| rxPackets | number | 否 | 否 | 流量下行包个数。 |
| txPackets | number | 否 | 否 | 流量上行包个数。 |
