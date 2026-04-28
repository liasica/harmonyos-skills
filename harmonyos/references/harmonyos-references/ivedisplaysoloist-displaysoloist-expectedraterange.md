---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ivedisplaysoloist-displaysoloist-expectedraterange
title: DisplaySoloist_ExpectedRateRange
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > DisplaySoloist_ExpectedRateRange
category: harmonyos-references
scraped_at: 2026-04-28T08:15:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:48da263fc39234de6a03ffa0d5e5a926d167f00daf03ce5c1784f4395442337e
---

```
1. typedef struct {...} DisplaySoloist_ExpectedRateRange
```

## 概述

PhonePC/2in1TabletTVWearable

提供期望帧率范围结构体。

**起始版本：** 12

**相关模块：** [NativeDisplaySoloist](capi-nativedisplaysoloist.md)

**所在头文件：** [native\_display\_soloist.h](capi-native-display-soloist-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t min | 期望帧率范围最小值，取值范围为[0,120]。 |
| int32\_t max | 期望帧率范围最大值，取值范围为[0,120]。 |
| int32\_t expected | 期望帧率，取值范围为[0,120]。 |
