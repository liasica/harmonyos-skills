---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netethernet-ethernet-netaddrlist
title: Ethernet_NetAddrList
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Ethernet_NetAddrList
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b4ab21f466c928a0dc27b17f10ca80416707bffe7ab2c56c80992f920dd3fd4f
---

```c
typedef struct Ethernet_NetAddrList {...} Ethernet_NetAddrList
```

## 概述

以太网网卡网络地址列表。

**起始版本：** 26.0.0

**相关模块：** [NetEthernet](capi-netethernet.md)

**所在头文件：** [net\_ethernet\_type.h](capi-net-ethernet-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Ethernet\_NetAddrInfo](capi-netethernet-ethernet-netaddrinfo.md) netAddrList[ETHERNET\_MAX\_NET\_SIZE] | 以太网网络地址列表。 |
| int32\_t netAddrListSize | netAddrList的实际大小。 |
