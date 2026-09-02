---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netethernet-ethernet-netaddrinfo
title: Ethernet_NetAddrInfo
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Ethernet_NetAddrInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9cbe8165dcaa98183d05e28d344db7861b297549cfff7eac830202886a0d7094
---

```c
typedef struct Ethernet_NetAddrInfo {...} Ethernet_NetAddrInfo
```

## 概述

以太网网卡网络地址信息，包含以太网网卡名称及网络地址信息。

**起始版本：** 26.0.0

**相关模块：** [NetEthernet](capi-netethernet.md)

**所在头文件：** [net\_ethernet\_type.h](capi-net-ethernet-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char ifaceName[ETHERNET\_MAX\_STR\_LEN] | 以太网网卡名称 |
| [Ethernet\_NetAddr](capi-netethernet-ethernet-netaddr.md) netAddrInfo[ETHERNET\_MAX\_NET\_SIZE] | 网络地址。 |
| int32\_t netAddrInfoSize | 网络地址数组的实际大小。 |
