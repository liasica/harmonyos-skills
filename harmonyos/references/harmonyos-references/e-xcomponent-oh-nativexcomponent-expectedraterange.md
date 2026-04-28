---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/e-xcomponent-oh-nativexcomponent-expectedraterange
title: OH_NativeXComponent_ExpectedRateRange
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_NativeXComponent_ExpectedRateRange
category: harmonyos-references
scraped_at: 2026-04-28T08:04:15+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3608f40ab3bc2480c5de59d6272a97c2ec282bed28b2f5a0c5641086ede9c123
---

```
1. typedef struct {...} OH_NativeXComponent_ExpectedRateRange
```

## 概述

PhonePC/2in1TabletTVWearable

定义期望帧率范围。

**起始版本：** 11

**相关模块：** [OH\_NativeXComponent Native XComponent](capi-oh-nativexcomponent-native-xcomponent.md)

**所在头文件：** [native\_interface\_xcomponent.h](capi-native-interface-xcomponent-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t min | 期望帧率范围最小值。单位为帧/秒。 |
| int32\_t max | 期望帧率范围最大值。单位为帧/秒。 |
| int32\_t expected | 期望帧率。单位为帧/秒。 |
