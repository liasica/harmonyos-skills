---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-memorylimit
title: HiDebug_MemoryLimit
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiDebug_MemoryLimit
category: harmonyos-references
scraped_at: 2026-09-02T15:02:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d1e0ab6d9d2af6a0fca197b76ab064d49d111849dded908d13dab323e2961c66
---

```c
typedef struct HiDebug_MemoryLimit {...} HiDebug_MemoryLimit
```

## 概述

应用程序进程内存限制结构类型定义。

**起始版本：** 12

**相关模块：** [HiDebug](capi-hidebug.md)

**所在头文件：** [hidebug\_type.h](capi-hidebug-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint64\_t rssLimit | 应用程序进程可用的物理内存限制，以KB为单位，实际当前系统未对进程可用物理内存做限制，但是进程的可用物理内存仍然不会超过设备的实际最大可用物理内存，当前设备的物理内存使用情况可通过[OH\_HiDebug\_GetSystemMemInfo](capi-hidebug-h.md#oh_hidebug_getsystemmeminfo)获取。 |
| uint64\_t vssLimit | 应用程序进程的虚拟内存限制，以KB为单位。 |
