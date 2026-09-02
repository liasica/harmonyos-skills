---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-oh-hidebug-resprofilerconfig
title: OH_HiDebug_ResProfilerConfig
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > OH_HiDebug_ResProfilerConfig
category: harmonyos-references
scraped_at: 2026-09-02T15:02:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4359c5b20e9f123a8141d825f98d825b659a495b514ac789d7a1483e287763eb
---

```c
typedef struct OH_HiDebug_ResProfilerConfig {...} OH_HiDebug_ResProfilerConfig
```

## 概述

定义资源采集配置结构体类型。

**起始版本：** 24

**相关模块：** [HiDebug](capi-hidebug.md)

**所在头文件：** [hidebug\_type.h](capi-hidebug-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t maxDuration | 最大采集时长，取值范围为 [1, 3600]，单位为秒。  传入参数超出取值范围，接口将返回错误码[HIDEBUG\_RES\_PROF\_INVALID\_MAX\_DURATION](capi-hidebug-type-h.md#hidebug_errorcode)。  **起始版本：** 24 |
| uint32\_t filterSize | 过滤大小，取值范围为 [1, 4294967295]，单位为字节。  传入参数超出取值范围，接口将返回错误码[HIDEBUG\_RES\_PROF\_INVALID\_FILTER\_SIZE](capi-hidebug-type-h.md#hidebug_errorcode)。  **起始版本：** 24 |
| uint32\_t maxStackDepth | 最大栈追踪深度，取值范围为 [0, 30]，单位为帧。建议根据实际需求设置合适的栈深度，深度越大采集开销越大。  传入参数超出取值范围，接口将返回错误码[HIDEBUG\_RES\_PROF\_INVALID\_MAX\_STACK\_DEPTH](capi-hidebug-type-h.md#hidebug_errorcode)。  **起始版本：** 24 |
| uint32\_t statisticsInterval | 统计间隔，取值范围为 [0, 3600]，单位为秒。  传入参数超出取值范围，接口将返回错误码[HIDEBUG\_RES\_PROF\_INVALID\_STATISTICS\_INTERVAL](capi-hidebug-type-h.md#hidebug_errorcode)。  **起始版本：** 24 |
| uint32\_t sampleInterval | 采样大小，取值范围为 [384, 4294967295]，单位为字节。  在采样模式下，如果内存分配大小小于等于采样大小，则概率性采样，否则全量采样。  传入参数超出取值范围，接口将返回错误码[HIDEBUG\_RES\_PROF\_INVALID\_SAMPLE\_INTERVAL](capi-hidebug-type-h.md#hidebug_errorcode)。  **起始版本：** 24 |
