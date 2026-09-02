---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netethernet-ethernet-macaddressinfo
title: Ethernet_MacAddressInfo
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Ethernet_MacAddressInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:06cd48b87d873518b059bf922d85742e17a8e261d5e25c77922d282cf83788eb
---

```c
typedef struct Ethernet_MacAddressInfo {...} Ethernet_MacAddressInfo
```

## 概述

以太网网卡MAC地址信息。

**起始版本：** 26.0.0

**相关模块：** [NetEthernet](capi-netethernet.md)

**所在头文件：** [net\_ethernet\_type.h](capi-net-ethernet-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char ifaceName[ETHERNET\_MAX\_STR\_LEN] | 以太网网卡名称。 |
| char macAddr[ETHERNET\_MAX\_STR\_LEN] | 以太网网卡MAC地址。 |
