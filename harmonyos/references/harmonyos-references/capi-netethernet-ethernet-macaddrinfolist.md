---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netethernet-ethernet-macaddrinfolist
title: Ethernet_MacAddrInfoList
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Ethernet_MacAddrInfoList
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4a25c3deb6d2d75a2a4b193c8500de4816a2a1f10a4ceffc40b14ec3379999d5
---

```c
typedef struct Ethernet_MacAddrInfoList {...} Ethernet_MacAddrInfoList
```

## 概述

以太网网卡MAC地址信息列表。

**起始版本：** 26.0.0

**相关模块：** [NetEthernet](capi-netethernet.md)

**所在头文件：** [net\_ethernet\_type.h](capi-net-ethernet-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Ethernet\_MacAddressInfo](capi-netethernet-ethernet-macaddressinfo.md) macInfoList[ETHERNET\_MAX\_NET\_SIZE] | 以太网网卡MAC地址列表。 |
| int32\_t macInfoListSize | macInfoList数组的实际大小。 |
