---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-expectedframeraterange
title: ArkUI_ExpectedFrameRateRange
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_ExpectedFrameRateRange
category: harmonyos-references
scraped_at: 2026-09-02T15:01:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8002ae3a709432d3b84efe412302b0f2880995654ec0113921722c634deea22e
---

```c
typedef struct {...} ArkUI_ExpectedFrameRateRange
```

## 概述

设置动画的期望帧率。该结构体通过min、max和expected三个字段定义帧率范围，系统尽可能满足期望帧率。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_animate.h](capi-native-animate-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t min | 期望的最小帧率，单位为帧/秒（fps）。取值原则：min需小于等于max，且min需小于等于expected。取值需满足min <= expected <= max，不满足时该期望帧率范围设置不生效。 |
| uint32\_t max | 期望的最大帧率，单位为帧/秒（fps）。取值原则：max需大于等于min，且max需大于等于expected。三者取值需满足min <= expected <= max。 |
| uint32\_t expected | 期望的最优帧率，单位为帧/秒（fps）。取值原则：expected需在[min, max]范围内取值。 |
