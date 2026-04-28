---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessiblerangeinfo
title: ArkUI_AccessibleRangeInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_AccessibleRangeInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:04:11+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1a0622040fdd75158add29f3578ab12f04940f45a21ef2fab5bef04cd5371a0d
---

```
1. typedef struct {...} ArkUI_AccessibleRangeInfo
```

## 概述

PhonePC/2in1TabletTVWearable

用于为特定组件（如[Slider](ts-basic-components-slider.md)、[Rating](ts-basic-components-rating.md)、[Progress](ts-basic-components-progress.md)组件）设置和获取其当前值、最大值和最小值。

**起始版本：** 13

**相关模块：** [ArkUI\_Accessibility](capi-arkui-accessibility.md)

**所在头文件：** [native\_interface\_accessibility.h](capi-native-interface-accessibility-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| double min | 组件的最小值。 |
| double max | 组件的最大值。 |
| double current | 组件的当前值。 |
