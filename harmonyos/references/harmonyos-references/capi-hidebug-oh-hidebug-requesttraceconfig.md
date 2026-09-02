---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-oh-hidebug-requesttraceconfig
title: OH_HiDebug_RequestTraceConfig
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > OH_HiDebug_RequestTraceConfig
category: harmonyos-references
scraped_at: 2026-09-02T15:02:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d303e6ff3555e753a50466dced5f652db2cd04a0fb60a2843a23f4cf37294c69
---

```c
typedef struct OH_HiDebug_RequestTraceConfig {...} OH_HiDebug_RequestTraceConfig
```

## 概述

请求trace采集的配置结构类型定义。用于在应用性能分析和调试场景中配置trace采集参数，如定位应用启动慢、UI卡顿、CPU占用高等性能问题。

**起始版本：** 24

**相关模块：** [HiDebug](capi-hidebug.md)

**所在头文件：** [hidebug\_type.h](capi-hidebug-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char\* identifier | 采集trace输出的文件名前缀。文件名前缀只取字符串前20个字符，超过部分将抛弃。前20个字符只包含大小写字母和下划线，若不符合则默认为空字符串。 |
| uint32\_t bufferSizeKb | trace文件的缓存大小，以KB为单位。取值范围为[1024, 15360]，传入参数超过取值范围，参数将被设置为最近的边界值。 |
| uint32\_t durationMs | trace采集时长，以ms为单位。取值范围为[1000, 15000]，传入参数超过取值范围，参数将被设置为最近的边界值。 |
| uint32\_t reserved | 预留字段，可以设置为0。 |
