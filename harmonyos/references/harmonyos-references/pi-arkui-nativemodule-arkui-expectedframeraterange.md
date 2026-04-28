---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-arkui-nativemodule-arkui-expectedframeraterange
title: ArkUI_ExpectedFrameRateRange
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_ExpectedFrameRateRange
category: harmonyos-references
scraped_at: 2026-04-28T08:04:03+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:12e85dba2ca441241beb817a64ff8f2bed8681dc25f96187a7bb1fede55cd152
---

```
1. typedef struct {...} ArkUI_ExpectedFrameRateRange
```

## 概述

PhonePC/2in1TabletTVWearable

设置动画的期望帧率。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_animate.h](capi-native-animate-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t min | 期望的最小帧率，单位为帧/秒（fps）。 |
| uint32\_t max | 期望的最大帧率，单位为帧/秒（fps）。 |
| uint32\_t expected | 期望的最优帧率，单位为帧/秒（fps）。 |
