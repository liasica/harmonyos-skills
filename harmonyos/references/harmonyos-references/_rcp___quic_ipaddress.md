---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___quic_ipaddress
title: Rcp_QuicIpAddress
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_QuicIpAddress
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:66c4802361bde5499a8e035ef57d4a79bac6334f036233c0b8cb75eada0ecfac
---

## 概述

用于存储IP地址的数据结构。

**起始版本：** 26.0.0

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp\_quic.h](rcp_quic_h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char [ip](_rcp___quic_ipaddress.md#ip) [[RCP\_QUIC\_IP\_MAX\_LEN](remote-communication-overview.md#rcp_quic_ip_max_len)] | 用于存储IP地址。长度不超过40字节。 |

## 结构体成员变量说明

### ip

```cpp
char Rcp_QuicIpAddress::ip[RCP_QUIC_IP_MAX_LEN]
```

**描述**

用于存储IP地址。长度不超过40字节。
