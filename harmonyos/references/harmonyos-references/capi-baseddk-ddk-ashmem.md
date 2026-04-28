---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-baseddk-ddk-ashmem
title: DDK_Ashmem
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > DDK_Ashmem
category: harmonyos-references
scraped_at: 2026-04-28T08:10:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e3546df9fccb8ea5cfed327ecc950e5d4c6bf7637a0250e60455b25ee156c3db
---

```
1. typedef struct DDK_Ashmem {...} DDK_Ashmem
```

## 概述

PC/2in1

定义通过接口**OH\_DDK\_CreateAshmem**创建的共享内存，共享内存的缓冲区提供更好的性能。

**起始版本：** 12

**相关模块：** [Ddk](capi-baseddk.md)

**所在头文件：** [ddk\_types.h](capi-ddk-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| int32\_t ashmemFd | 共享内存的文件描述符。 |
| const uint8\_t\* address | 缓存区地址。 |
| const uint32\_t size | 缓存区大小。 |
| uint32\_t offset | 已使用缓冲区的偏移量。默认值为0，表示没有偏移，缓冲区从指定地址开始。 |
| uint32\_t bufferLength | 使用的缓冲区长度。默认情况下，该值等于size，表示使用整个缓冲区。 |
| uint32\_t transferredLength | 已传输数据的长度。 |
