---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-ethernet
title: "@ohos.net.ethernet (以太网连接管理)"
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > ArkTS API > @ohos.net.ethernet (以太网连接管理)
category: harmonyos-references
scraped_at: 2026-09-18T06:49:52+08:00
doc_updated_at: 2026-09-17
content_hash: sha256:3dc161ecf6746ce8b792fc77b9e3a5211f6d4f03baf618cfd9f48b2933513579
---

本模块提供以太网连接管理能力，包括有线网络能力、获取有线网络的IP地址等信息。

**说明** 

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { ethernet } from '@kit.NetworkKit';
```

## HttpProxy10+

type HttpProxy = connection.HttpProxy

网络代理配置信息。

**系统能力**：SystemCapability.Communication.NetManager.Ethernet

| 类型 | 说明 |
| --- | --- |
| connection.HttpProxy | 网络代理配置信息。 |

## ethernet.getMacAddress14+

getMacAddress(): Promise<Array<MacAddressInfo>>

获取所有以太网网卡名称及对应网卡的MAC地址信息，使用Promise异步回调。

**需要权限**：ohos.permission.GET\_ETHERNET\_LOCAL\_MAC

**系统能力**：SystemCapability.Communication.NetManager.Ethernet

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[MacAddressInfo](js-apis-net-ethernet.md#macaddressinfo14)>> | Promise对象，返回所有以太网网卡名称及对应网卡的MAC地址信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[以太网连接错误码](errorcode-net-ethernet.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2200002 | Operation failed. Cannot connect to service. |
| 2201005 | Device information does not exist. |

**示例：**

```ts
import { ethernet } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

ethernet.getMacAddress().then((data: Array<ethernet.MacAddressInfo>) => {
  console.info(`getMacAddress promise data = ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
  console.error(`getMacAddress promise error = ${JSON.stringify(error)}`);
});
```

## MacAddressInfo14+

以太网网卡名称及MAC地址信息。

**系统能力**：SystemCapability.Communication.NetManager.Ethernet

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| iface | string | 否 | 否 | 以太网网卡名称，如"eth0"。可通过[getMacAddress](js-apis-net-ethernet.md#ethernetgetmacaddress14)获取。 |
| macAddress | string | 否 | 否 | 以太网网卡MAC地址信息，格式为"XX:XX:XX:XX:XX:XX"。 |
