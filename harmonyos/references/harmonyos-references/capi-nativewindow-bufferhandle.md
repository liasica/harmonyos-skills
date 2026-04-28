---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow-bufferhandle
title: BufferHandle
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > BufferHandle
category: harmonyos-references
scraped_at: 2026-04-28T08:15:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3eac07d9e86d6149f7cff7c0fa80d069ea1ef551265601d40df94bdbd424a0fa
---

```
1. typedef struct {...} BufferHandle
```

## 概述

PhonePC/2in1TabletTVWearable

缓冲区句柄，用于对缓冲区的信息传递和获取。句柄包含了缓冲区的文件描述符、尺寸、格式、用途、虚拟地址、共享内存键、物理地址、自定义数据。

**起始版本：** 8

**相关模块：** [NativeWindow](capi-nativewindow.md)

**所在头文件：** [buffer\_handle.h](capi-buffer-handle-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t fd | 缓冲区文件描述符，若不支持则为-1。 |
| int32\_t width | 缓冲区内存的宽度，单位为像素。 |
| int32\_t stride | 缓冲区内存的步幅，单位为字节。 |
| int32\_t height | 缓冲区内存的高度，单位为像素。 |
| int32\_t size | 缓冲区内存的大小，单位为字节。 |
| int32\_t format | 缓冲区内存的格式，取值具体可见[OH\_NativeBuffer\_Format](capi-buffer-common-h.md#oh_nativebuffer_format)枚举值。 |
| uint64\_t usage | 缓冲区内存的用途，按位标志位，取值具体可见[OH\_NativeBuffer\_Format](capi-buffer-common-h.md#oh_nativebuffer_format)枚举值。 |
| void\* virAddr | 缓冲区内存的虚拟地址。 |
| int32\_t key | 缓冲区共享内存键值。 |
| uint64\_t phyAddr | 缓冲区内存的物理地址。 |
| uint32\_t reserveFds | 额外数据的文件描述符数量。 |
| uint32\_t reserveInts | 额外数据的整型值数量。 |
| int32\_t reserve[0] | 额外数据。 |
