---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter-oh-trafficfilter-processinfo
title: OH_TrafficFilter_ProcessInfo
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_TrafficFilter_ProcessInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6cd780cd421a4243e6cc72c5e1135aa9a4b0f2a38e23c0b736c2eb5bf502736f
---

```c
typedef struct OH_TrafficFilter_ProcessInfo {...} OH_TrafficFilter_ProcessInfo
```

## 概述

进程信息结构体。存储[OH\_TrafficFilter\_QueryProcess](capi-net-trafficfilter-h.md#oh_trafficfilter_queryprocess)返回的进程信息。

初始化规则：调用[OH\_TrafficFilter\_QueryProcess](capi-net-trafficfilter-h.md#oh_trafficfilter_queryprocess)之前，调用者必须将该结构体清零（例如使用memset），然后将[size](capi-trafficfilter-oh-trafficfilter-processinfo.md#成员变量)设置为调用者分配的结构体实际大小，通常为sizeof(OH\_TrafficFilter\_ProcessInfo)。

二进制兼容规则（ABI，即应用程序二进制接口，保证新旧版本编译的代码能互相识别结构体布局）：系统通过[size](capi-trafficfilter-oh-trafficfilter-processinfo.md#成员变量)来确定哪些输出字段可以被安全写入。只有被[size](capi-trafficfilter-oh-trafficfilter-processinfo.md#成员变量)完全覆盖的字段才会被系统写入。如果[size](capi-trafficfilter-oh-trafficfilter-processinfo.md#成员变量)小于读取[size](capi-trafficfilter-oh-trafficfilter-processinfo.md#成员变量)字段本身所需的最小大小，接口将返回[OH\_TRAFFICFILTER\_ERROR\_INVALID\_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode)。如果[size](capi-trafficfilter-oh-trafficfilter-processinfo.md#成员变量)大于系统已知的大小，多余的字段将被忽略。

输出有效性规则：当[OH\_TrafficFilter\_QueryProcess](capi-net-trafficfilter-h.md#oh_trafficfilter_queryprocess)返回[OH\_TRAFFICFILTER\_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode)时，被[size](capi-trafficfilter-oh-trafficfilter-processinfo.md#成员变量)覆盖的字段包含有效的输出值。当接口返回错误时，调用者不应依赖[size](capi-trafficfilter-oh-trafficfilter-processinfo.md#成员变量)以外的输出字段的值。

**起始版本：** 26.0.0

**相关模块：** [TrafficFilter](capi-trafficfilter.md)

**所在头文件：** [net\_trafficfilter\_type.h](capi-net-trafficfilter-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t size | 调用者分配的结构体实际大小。  **起始版本：** 26.0.0 |
| uint32\_t pid | 进程ID。  **起始版本：** 26.0.0 |
| uint32\_t uid | 应用UID。  **起始版本：** 26.0.0 |
