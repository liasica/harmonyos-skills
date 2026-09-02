---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ethernet-h
title: net_ethernet.h
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 头文件 > net_ethernet.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a7f28100921dd93bf4edc0201509c5033d8d143f6cf511a22dc58726297fc13f
---

## 概述

为以太网网卡模块提供C接口。

**引用文件：** <network/netmanager\_ext/net\_ethernet.h>

**库：** libnet\_ethernet.so

**系统能力：** SystemCapability.Communication.NetManager.Ethernet

**起始版本：** 26.0.0

**相关模块：** [NetEthernet](capi-netethernet.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [int32\_t OH\_Ethernet\_GetMacAddress(Ethernet\_MacAddrInfoList \*macAddrList)](capi-net-ethernet-h.md#oh_ethernet_getmacaddress) | 获取以太网网卡MAC地址列表。 |
| [int32\_t OH\_Ethernet\_GetNetAddress(Ethernet\_NetAddrList \*netAddrList)](capi-net-ethernet-h.md#oh_ethernet_getnetaddress) | 获取以太网网卡IP地址列表。 |

## 函数说明

### OH\_Ethernet\_GetMacAddress()

```c
int32_t OH_Ethernet_GetMacAddress(Ethernet_MacAddrInfoList *macAddrList)
```

**描述**

获取以太网网卡MAC地址列表。

**系统能力：** SystemCapability.Communication.NetManager.Ethernet

**需要权限：** ohos.permission.GET\_ETHERNET\_LOCAL\_MAC

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Ethernet\_MacAddrInfoList](capi-netethernet-ethernet-macaddrinfolist.md) \*macAddrList | 以太网网卡MAC地址列表。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。 201 - 缺少权限。  2200001 - 参数错误。 2200002 - 无法连接到服务。  2201005 - 设备信息不存在。 |

### OH\_Ethernet\_GetNetAddress()

```c
int32_t OH_Ethernet_GetNetAddress(Ethernet_NetAddrList *netAddrList)
```

**描述**

获取以太网网卡IP地址列表。

**系统能力：** SystemCapability.Communication.NetManager.Ethernet

**需要权限：** ohos.permission.GET\_NETWORK\_INFO

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Ethernet\_NetAddrList](capi-netethernet-ethernet-netaddrlist.md) \*netAddrList | 以太网网卡IP地址列表。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。 201 - 缺少权限。  2200001 - 参数错误。 2200002 - 无法连接到服务。  2201005 - 设备信息不存在。 |
