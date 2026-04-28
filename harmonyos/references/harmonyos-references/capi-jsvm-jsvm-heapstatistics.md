---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-heapstatistics
title: JSVM_HeapStatistics
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_HeapStatistics
category: harmonyos-references
scraped_at: 2026-04-28T08:19:21+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:b31824af73856118bf14698b65a314376c60f6b3c6e22f20be8bb7d1874a8b81
---

```
1. typedef struct {...} JSVM_HeapStatistics
```

## 概述

PhonePC/2in1TabletWearable

用于保存有关JavaScript堆内存使用情况的统计信息。

**起始版本：** 12

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

PhonePC/2in1TabletWearable

### 成员变量

PhonePC/2in1TabletWearable

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
