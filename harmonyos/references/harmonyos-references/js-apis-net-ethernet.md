---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-ethernet
title: @ohos.net.ethernet (以太网连接管理)
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > ArkTS API > @ohos.net.ethernet (以太网连接管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:23+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:fbbe3d579b64955f8ee8d6b4634450b1958318604b7aaa1f6b0522ccb80b969c
---

本模块提供以太网连接管理能力，包括有线网络能力、获取有线网络的IP地址等信息。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { ethernet } from '@kit.NetworkKit';
```

## HttpProxy10+

PhonePC/2in1TabletTV

type HttpProxy = connection.HttpProxy

网络代理配置信息。

**系统能力**：SystemCapability.Communication.NetManager.Ethernet

| 类型 | 说明 |
| --- | --- |
| connection.HttpProxy | 网络代理配置信息。 |

## ethernet.getMacAddress14+

PhonePC/2in1TabletTV

getMacAddress(): Promise<Array<MacAddressInfo>>

获取所有以太网网卡名称及对应网卡的MAC地址信息，使用Promise方式作为异步方法。

**需要权限**：ohos.permission.GET\_ETHERNET\_LOCAL\_MAC

**系统能力**：SystemCapability.Communication.NetManager.Ethernet

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array[<MacAddressInfo>](js-apis-net-ethernet.md#macaddressinfo14)> | 以Promise形式返回接口信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2200002 | Operation failed. Cannot connect to service. |
| 2201005 | Device information does not exist. |

**示例：**

```
1. import { ethernet } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. ethernet.getMacAddress().then((data: Array<ethernet.MacAddressInfo>) => {
5. console.info("getMacAddress promise data = " + JSON.stringify(data));
6. }).catch((error: BusinessError) => {
7. console.error("getMacAddress promise error = " + JSON.stringify(error));
8. });
```

## MacAddressInfo14+

PhonePC/2in1TabletTV

以太网网卡名称及MAC地址信息。

**系统能力**：SystemCapability.Communication.NetManager.Ethernet

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| iface | string | 否 | 否 | 以太网网卡名称。 |
| macAddress | string | 否 | 否 | 以太网网卡MAC地址信息。 |
