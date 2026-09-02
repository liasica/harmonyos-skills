---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativevsync-oh-nativevsync-expectedraterange
title: OH_NativeVSync_ExpectedRateRange
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_NativeVSync_ExpectedRateRange
category: harmonyos-references
scraped_at: 2026-09-02T15:02:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2d5d904b3cc07b982afda6f292ee2c22e8528cc8041cbad73ea6ee048236a79b
---

```c
typedef struct {...} OH_NativeVSync_ExpectedRateRange
```

## 概述

期望帧率范围结构体。

**起始版本：** 20

**相关模块：** [NativeVsync](capi-nativevsync.md)

**所在头文件：** [native\_vsync.h](capi-native-vsync-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t min | 帧率范围的最小帧率。 |
| int32\_t max | 帧率范围的最大帧率。 |
| int32\_t expected | 帧率范围的期望帧率。 |
