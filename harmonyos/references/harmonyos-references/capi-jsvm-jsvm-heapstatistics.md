---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-heapstatistics
title: JSVM_HeapStatistics
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_HeapStatistics
category: harmonyos-references
scraped_at: 2026-09-02T15:03:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2ab7dc94419e5b0254c3204b5f272f9da81be8b2ae794ebcd513de02af9bd810
---

```c
typedef struct {...} JSVM_HeapStatistics
```

## 概述

用于保存有关JavaScript堆内存使用情况的统计信息。

**使用场景：** 性能监控：实时监测应用的堆内存使用情况，评估内存占用水平。内存优化：通过分析堆内存数据，识别内存使用瓶颈，优化内存配置。内存泄漏检测：通过numberOfNativeContexts等字段，辅助发现潜在的内存泄漏问题。

**解决问题：** 帮助开发者了解应用的内存使用状况，为性能优化和内存管理提供数据支撑，支持内存问题的排查和分析。

**收益：** 提升应用的内存使用效率，降低内存相关问题的排查成本，改善应用的整体性能和稳定性。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 12

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| size\_t totalHeapSize | 总堆大小，单位KB。 |
| size\_t totalHeapSizeExecutable | 可执行堆的总大小，单位KB。 |
| size\_t totalPhysicalSize | 总的物理内存大小，单位KB。 |
| size\_t totalAvailableSize | 总的可用内存大小，单位KB。 |
| size\_t usedHeapSize | 已使用的堆大小，单位KB。 |
| size\_t heapSizeLimit | 堆大小限制，单位KB。 |
| size\_t mallocedMemory | 已分配内存的大小，单位KB。 |
| size\_t externalMemory | 外部内存大小，单位KB。 |
| size\_t peakMallocedMemory | 最大可分配内存的大小，单位KB。 |
| size\_t numberOfNativeContexts | 表示当前活跃的native上下文的数量，该数值一直增加可能指示存在内存泄漏。 |
| size\_t numberOfDetachedContexts | 表示已经脱离的上下文数量。 |
| size\_t totalGlobalHandlesSize | 全局Handle的总大小，单位KB。 |
| size\_t usedGlobalHandlesSize | 已经使用的全局Handle的大小，单位KB。 |
