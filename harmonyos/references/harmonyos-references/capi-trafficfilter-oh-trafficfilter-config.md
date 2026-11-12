---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter-oh-trafficfilter-config
title: OH_TrafficFilter_Config
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_TrafficFilter_Config
category: harmonyos-references
scraped_at: 2026-11-12T09:55:43+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:8c42abe660fbaad8bd4a8ee493dad1423cc8efc0eb0ae4f75df7d36d69aa90b2
---

```c
typedef struct OH_TrafficFilter_Config {...} OH_TrafficFilter_Config
```

## 概述

NFQueue（Netfilter 框架里的一个“数据包排队通道”）配置结构体。

初始化规则：调用[OH\_TrafficFilter\_CreatePacketController](capi-net-trafficfilter-h.md#oh_trafficfilter_createpacketcontroller)之前，调用者必须将该结构体清零（例如使用memset），然后将[size](capi-trafficfilter-oh-trafficfilter-config.md#成员变量)设置为调用者分配的结构体实际大小，通常为sizeof(OH\_TrafficFilter\_Config)。

二进制兼容规则（ABI，即应用程序二进制接口，保证新旧版本编译的代码能互相识别结构体布局）：系统通过[size](capi-trafficfilter-oh-trafficfilter-config.md#成员变量)来确定哪些字段可以被安全读取。如果[size](capi-trafficfilter-oh-trafficfilter-config.md#成员变量)小于当前接口所需的最小大小，接口将返回[OH\_TRAFFICFILTER\_ERROR\_INVALID\_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode)。如果[size](capi-trafficfilter-oh-trafficfilter-config.md#成员变量)大于系统已知的大小，多余的字段将被忽略。

**起始版本：** 26.0.1

**相关模块：** [TrafficFilter](capi-trafficfilter.md)

**所在头文件：** [net\_trafficfilter\_type.h](capi-net-trafficfilter-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t size | 调用者分配的结构体实际大小。 |
| uint32\_t packetCopyMode | 报文拷贝模式，请参考[OH\_TrafficFilter\_PacketCopyMode](capi-trafficfilter-oh-trafficfilter-packetcopymode.md)。默认值(2) |
| uint32\_t packetCopyLen | NFQueue报文拷贝长度（字节），取值范围为[0, 0xFFFF]，0xFFFF表示复制整个报文，其他值复制指定长度的报文头部。默认值(0xFFFF) |
| uint32\_t nfqueueMaxlen | NFQueue最大队列长度（报文数量），0表示使用系统默认值（1024）。 |
| uint32\_t nfqueueFlags | NFQueue队列标志，参见[OH\_TRAFFICFILTER\_NFQUEUE\_FLAG\_FAIL\_OPEN](capi-net-trafficfilter-type-h.md#宏定义)。默认值(1) |
