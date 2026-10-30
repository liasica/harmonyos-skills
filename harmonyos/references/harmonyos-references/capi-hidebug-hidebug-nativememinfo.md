---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-nativememinfo
title: HiDebug_NativeMemInfo
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiDebug_NativeMemInfo
category: harmonyos-references
scraped_at: 2026-10-31T07:37:41+08:00
doc_updated_at: 2026-10-30
content_hash: sha256:e9251cef82398dcfcd1f249717d5d01fee3a0f40f84c131428edbb408dbaa109
---

```c
typedef struct HiDebug_NativeMemInfo {...} HiDebug_NativeMemInfo
```

## 概述

应用程序进程本机内存信息结构类型定义。

**起始版本：** 12

**相关模块：** [HiDebug](capi-hidebug.md)

**所在头文件：** [hidebug\_type.h](capi-hidebug-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t pss | 进程比例集内存大小，以KB为单位。 |
| uint32\_t vss | 虚拟内存大小，以KB为单位。 |
| uint32\_t rss | 常驻集大小，以KB为单位。 |
| uint32\_t sharedDirty | 共享脏内存的大小，以KB为单位。 |
| uint32\_t privateDirty | 专用脏内存的大小，以KB为单位。 |
| uint32\_t sharedClean | 共享干净内存的大小，以KB为单位。 |
| uint32\_t privateClean | 专用干净内存的大小，以KB为单位。 |
