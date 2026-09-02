---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessiblerangeinfo
title: ArkUI_AccessibleRangeInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_AccessibleRangeInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:763a51d79ce3cbda72926c465be4d637088dd1a4ad0d7fbb0b48bf52ecda1025
---

```c
typedef struct {...} ArkUI_AccessibleRangeInfo
```

## 概述

用于表示特定组件（如[Slider](ts-basic-components-slider.md)、[Rating](ts-basic-components-rating.md)、[Progress](ts-basic-components-progress.md)）的范围值信息，包含当前值、最大值和最小值，供无障碍服务读取并向障碍用户播报。

**起始版本：** 13

**相关模块：** [ArkUI\_Accessibility](capi-arkui-accessibility.md)

**所在头文件：** [native\_interface\_accessibility.h](capi-native-interface-accessibility-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| double min | 组件的最小值。 |
| double max | 组件的最大值。 |
| double current | 组件的当前值。 |
