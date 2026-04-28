---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-accessibility-arkui-accessiblegriditeminfo
title: ArkUI_AccessibleGridItemInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_AccessibleGridItemInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:04:12+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:43b9553142825964d66f43cc45449534ed750d9274fa4fd66bc18092df2de01e
---

```
1. typedef struct {...} ArkUI_AccessibleGridItemInfo
```

## 概述

PhonePC/2in1TabletTVWearable

用于配置特定组件（[List](ts-container-list.md)、[Flex](ts-container-flex.md)、[Select](ts-basic-components-select.md)、[Swiper](ts-container-swiper.md)组件）的属性值。

**起始版本：** 13

**相关模块：** [ArkUI\_Accessibility](capi-arkui-accessibility.md)

**所在头文件：** [native\_interface\_accessibility.h](capi-native-interface-accessibility-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| bool heading | 是否是标题。true表示是标题，false表示不是标题。 |
| bool selected | 是否被选中。true表示被选中，false表示未被选中。 |
| int32\_t columnIndex | 列下标。取值范围为大于0的整数。 |
| int32\_t rowIndex | 行下标。取值范围为大于0的整数。 |
| int32\_t columnSpan | 列跨度。取值范围为大于0的整数。 |
| int32\_t rowSpan | 行跨度。取值范围为大于0的整数。 |
