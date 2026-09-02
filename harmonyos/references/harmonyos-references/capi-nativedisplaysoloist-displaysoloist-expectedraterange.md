---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaysoloist-displaysoloist-expectedraterange
title: DisplaySoloist_ExpectedRateRange
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > DisplaySoloist_ExpectedRateRange
category: harmonyos-references
scraped_at: 2026-09-02T15:02:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f4b27028262f90e9906f451c1a1663302cf654dc8ce33e023339bc543cac08b4
---

```c
typedef struct {...} DisplaySoloist_ExpectedRateRange
```

## 概述

期望帧率范围结构体，用于设置DisplaySoloist（可变帧率独立线程绘制）的期望帧率范围。设置的期望帧率范围将作为系统调度的参考，系统会尽量在此范围内调整绘制帧率。

**起始版本：** 12

**相关模块：** [NativeDisplaySoloist](capi-nativedisplaysoloist.md)

**所在头文件：** [native\_display\_soloist.h](capi-native-display-soloist-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t min | 期望的最小帧率，单位为帧/秒（fps），取值范围为[0, 设备支持的最大刷新率]。 |
| int32\_t max | 期望的最大帧率，单位为帧/秒（fps），取值范围为[min, 设备支持的最大刷新率]。 |
| int32\_t expected | 期望的目标帧率，单位为帧/秒（fps），取值范围为[min, max]。 |
