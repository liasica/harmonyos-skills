---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-nativememinfo
title: HiDebug_NativeMemInfo
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiDebug_NativeMemInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:11:26+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e083fb4f10a52f1d0d62f79be6d1447b84f9bcb3aa071bee715e5f7031d955a9
---

```
1. typedef struct HiDebug_NativeMemInfo {...} HiDebug_NativeMemInfo
```

## 概述

PhonePC/2in1TabletTVWearable

应用程序进程本机内存信息结构类型定义。

**起始版本：** 12

**相关模块：** [HiDebug](capi-hidebug.md)

**所在头文件：** [hidebug\_type.h](capi-hidebug-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t pss | 进程比例集大小内存，以KB为单位。 |
| uint32\_t vss | 虚拟内存大小，以KB为单位。 |
| uint32\_t rss | 常驻集大小，以KB为单位。 |
| uint32\_t sharedDirty | 共享脏内存的大小，以KB为单位。 |
| uint32\_t privateDirty | 专用脏内存的大小，以KB为单位。 |
| uint32\_t sharedClean | 共享干净内存的大小，以KB为单位。 |
| uint32\_t privateClean | 专用干净内存的大小，以KB为单位。 |
