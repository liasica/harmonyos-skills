---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ethernet-type-h
title: net_ethernet_type.h
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 头文件 > net_ethernet_type.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:aa401237dee38a6fa28e2a5e4332783279684583b09151b5427376513624bc94
---

## 概述

为以太网网卡模块C接口定义数据结构。

**引用文件：** <network/netmanager\_ext/net\_ethernet\_type.h>

**库：** libnet\_ethernet.so

**系统能力：** SystemCapability.Communication.NetManager.Ethernet

**起始版本：** 26.0.0

**相关模块：** [NetEthernet](capi-netethernet.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Ethernet\_MacAddressInfo](capi-netethernet-ethernet-macaddressinfo.md) | Ethernet\_MacAddressInfo | 以太网网卡MAC地址信息。 |
| [Ethernet\_MacAddrInfoList](capi-netethernet-ethernet-macaddrinfolist.md) | Ethernet\_MacAddrInfoList | 以太网网卡MAC地址信息列表。 |
| [Ethernet\_NetAddr](capi-netethernet-ethernet-netaddr.md) | Ethernet\_NetAddr | 网络地址。 |
| [Ethernet\_NetAddrInfo](capi-netethernet-ethernet-netaddrinfo.md) | Ethernet\_NetAddrInfo | 以太网网卡网络地址信息，包含以太网网卡名称及网络地址信息。 |
| [Ethernet\_NetAddrList](capi-netethernet-ethernet-netaddrlist.md) | Ethernet\_NetAddrList | 以太网网卡网络地址列表。 |

### 宏定义

| 名称 | 描述 |
| --- | --- |
| ETHERNET\_MAX\_NET\_SIZE 32 | 以太网网卡最大连接数量。  **起始版本：** 26.0.0 |
| ETHERNET\_MAX\_STR\_LEN 256 | 以太网网卡MAC地址、IP地址最大长度。  **起始版本：** 26.0.0 |
