---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessiblegridinfo
title: ArkUI_AccessibleGridInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_AccessibleGridInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:04:12+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:cc9e2b2233081d8a2974dc41392650f8c315d82edf317475b7a645082c139c48
---

```
1. typedef struct {...} ArkUI_AccessibleGridInfo
```

## 概述

PhonePC/2in1TabletTVWearable

用于配置特定组件（如[List](ts-container-list.md)、[Flex](ts-container-flex.md)、[Select](ts-basic-components-select.md)、[Swiper](ts-container-swiper.md)组件）的网格布局属性。

**起始版本：** 13

**相关模块：** [ArkUI\_Accessibility](capi-arkui-accessibility.md)

**所在头文件：** [native\_interface\_accessibility.h](capi-native-interface-accessibility-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t rowCount | 组件的行数。取值范围为大于0的整数。 |
| int32\_t columnCount | 组件的列数。取值范围为大于0的整数。 |
| int32\_t selectionMode | 值为0时表示仅选中网格的一行，非0值时表示选中网格的多行。 |
