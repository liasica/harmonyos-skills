---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-issupported
title: 查询是否支持NPU推理
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 查询是否支持NPU推理
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:40+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:6743d4b5df5ccfd63c0744f11a4a932a0471cabc057ab3e33cc78a4012ffa88e
---

## 场景介绍

从4.1.0(11)版本开始，CANN Kit提供[HMS\_HiAI\_GetVersion](../harmonyos-references/cannkit.md#hms_hiai_getversion)接口，用于查询当前设备是否支持CANN Kit能力。由于不同设备的支持情况存在差异，开发者可在使用前通过该接口进行能力探测。

## 开发步骤

开发者可调用CANN Kit的[HMS\_HiAI\_GetVersion](../harmonyos-references/cannkit.md#hms_hiai_getversion)接口，通过解析返回的版本字符串hiaiversion A1A2A3.X1X2X3.Y1Y2Y3.Z1Z2Z3来判断设备是否支持NPU。

X1为0，则设备不支持NPU且无法使用CANN Kit能力。

X1非0，则设备支持NPU并可正常使用CANN Kit相关能力。

```
#include <hilog/log.h>
// ...
#include "CANNKit/hiai_helper.h"
// ...
    const char *version = HMS_HiAI_GetVersion();
    OH_LOG_INFO(LOG_APP, "version is %{public}s", version);
```
