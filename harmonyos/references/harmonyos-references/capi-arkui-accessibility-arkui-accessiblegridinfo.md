---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessiblegridinfo
title: ArkUI_AccessibleGridInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_AccessibleGridInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5c64b68f4abdecee5d0c4bf77227c3f85040284e26b0ae5d3ae2ae361fd39a15
---

```c
typedef struct {...} ArkUI_AccessibleGridInfo
```

## 概述

用于描述网格组件的整体布局属性。该结构体用于向无障碍服务提供网格组件的行数、列数和选择模式等信息，支持无障碍服务获取网格的整体布局信息。

**起始版本：** 13

**相关模块：** [ArkUI\_Accessibility](capi-arkui-accessibility.md)

**所在头文件：** [native\_interface\_accessibility.h](capi-native-interface-accessibility-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t rowCount | 网格的行数。取值范围为大于0的整数，传入非正整数时不生效。 |
| int32\_t columnCount | 网格的列数。取值范围为大于0的整数，传入非正整数时不生效。 |
| int32\_t selectionMode | 选中模式。值为0时表示仅选中网格的一行，非0值时表示选中网格的多行。 |
