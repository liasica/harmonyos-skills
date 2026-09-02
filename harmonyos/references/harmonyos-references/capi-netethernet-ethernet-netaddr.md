---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netethernet-ethernet-netaddr
title: Ethernet_NetAddr
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Ethernet_NetAddr
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:88354db7aa8837ff45532f576b07f47c4caf115bfb5d9257258bfc20b0e44952
---

```c
typedef struct Ethernet_NetAddr {...} Ethernet_NetAddr
```

## 概述

网络地址。

**起始版本：** 26.0.0

**相关模块：** [NetEthernet](capi-netethernet.md)

**所在头文件：** [net\_ethernet\_type.h](capi-net-ethernet-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t family | 网络地址族。IPv4 = 1，IPv6 = 2。 |
| uint8\_t prefixlen | 前缀长度。 |
| uint16\_t port | 端口号。 |
| char address[ETHERNET\_MAX\_STR\_LEN] | IP地址。 |
