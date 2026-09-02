---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-expectedraterange
title: OH_NativeXComponent_ExpectedRateRange
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_NativeXComponent_ExpectedRateRange
category: harmonyos-references
scraped_at: 2026-09-02T15:01:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8f436838b9b7917c713c922a4c557fc0cde74fd7bbe3f1566a4863b461b2cab2
---

```c
typedef struct {...} OH_NativeXComponent_ExpectedRateRange
```

## 概述

定义期望帧率范围，用于设置XComponent渲染时的期望帧率区间，适用于需要对动画或渲染帧率进行精确控制的场景，可帮助在画面流畅度与功耗之间取得平衡。

**起始版本：** 11

**相关模块：** [OH\_NativeXComponent Native XComponent](capi-oh-nativexcomponent-native-xcomponent.md)

**所在头文件：** [native\_interface\_xcomponent.h](capi-native-interface-xcomponent-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t min | 期望帧率范围最小值。取值需大于等于0且小于等于max。单位为帧/秒。传入无效值时不生效。取值范围：[0, +∞)。需满足 min <= max。 |
| int32\_t max | 期望帧率范围最大值。取值需大于等于min且不超过设备支持的最大帧率。单位为帧/秒。传入无效值时不生效。取值范围：[0, +∞)。需满足 max >= min。 |
| int32\_t expected | 期望帧率。取值需满足 min ≤ expected ≤ max。单位为帧/秒。取值范围：[0, +∞)，且应在[min, max]范围内。 |
