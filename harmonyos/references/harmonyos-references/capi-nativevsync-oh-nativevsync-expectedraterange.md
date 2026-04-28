---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativevsync-oh-nativevsync-expectedraterange
title: OH_NativeVSync_ExpectedRateRange
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_NativeVSync_ExpectedRateRange
category: harmonyos-references
scraped_at: 2026-04-28T08:15:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:537e9f3d986a59c03634cd6e23157e1295c7b3607cd2a342e071a32e42da4817
---

```
1. typedef struct {...} OH_NativeVSync_ExpectedRateRange
```

## 概述

PhonePC/2in1TabletTVWearable

期望帧率范围结构体。

**起始版本：** 20

**相关模块：** [NativeVsync](capi-nativevsync.md)

**所在头文件：** [native\_vsync.h](capi-native-vsync-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t min | 帧率范围的最小帧率。 |
| int32\_t max | 帧率范围的最大帧率。 |
| int32\_t expected | 帧率范围的期望帧率。 |
