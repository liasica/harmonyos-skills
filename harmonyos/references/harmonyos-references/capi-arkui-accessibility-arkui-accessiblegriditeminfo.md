---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessiblegriditeminfo
title: ArkUI_AccessibleGridItemInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_AccessibleGridItemInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:26c3842217409eee2ea684c6ebfe0424f25aa37bcc0b3335d5e5084910a7d74d
---

```c
typedef struct {...} ArkUI_AccessibleGridItemInfo
```

## 概述

用于描述网格组件内某个网格项的无障碍属性。该结构体用于向无障碍服务提供网格项的位置、跨度、选中状态等信息，支持无障碍服务获取网格项的布局信息。

**起始版本：** 13

**相关模块：** [ArkUI\_Accessibility](capi-arkui-accessibility.md)

**所在头文件：** [native\_interface\_accessibility.h](capi-native-interface-accessibility-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| bool heading | 是否是标题。true表示是标题，false表示不是标题。 |
| bool selected | 是否被选中。true表示被选中，false表示未被选中。 |
| int32\_t columnIndex | 列下标。取值范围为大于等于0的整数。传入0或负数时该字段不生效。 |
| int32\_t rowIndex | 行下标。取值范围为大于等于0的整数。传入0或负数时该字段不生效。 |
| int32\_t columnSpan | 列跨度。取值范围为大于0的整数。传入0或负数时该字段不生效。 |
| int32\_t rowSpan | 行跨度。取值范围为大于0的整数。传入0或负数时该字段不生效。 |
