---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-processsamplerconfig
title: HiDebug_ProcessSamplerConfig
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiDebug_ProcessSamplerConfig
category: harmonyos-references
scraped_at: 2026-09-02T15:02:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:acb2e0fb7894ca0288a9960b76f07caf70da6490a9689c342e10f2b9494cc61c
---

```c
typedef struct HiDebug_ProcessSamplerConfig {...} HiDebug_ProcessSamplerConfig
```

## 概述

采样配置的结构定义。

**起始版本：** 22

**相关模块：** [HiDebug](capi-hidebug.md)

**所在头文件：** [hidebug\_type.h](capi-hidebug-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t\* tids | 待采样的线程号数组。最大支持10个线程的同时采样，数组长度超出时，将取前10个线程进行采样。 |
| uint32\_t size | tids指向的数组长度。该值必须与tids数组的实际长度一致。 |
| uint32\_t frequency | 采样频率，取值范围[1-200]，单位Hz。超出取值范围时取默认值100。 |
| uint32\_t duration | 采样时长，取值范围[1000-10000]，单位ms。小于1000时，接口调用异常；大于10000时，取10000。 |
| uint32\_t reserved | 保留字段。 |
