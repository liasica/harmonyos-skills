---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessibleaction
title: ArkUI_AccessibleAction
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_AccessibleAction
category: harmonyos-references
scraped_at: 2026-09-02T15:01:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:74911f88b293cf1f6f79a8907efcbbcb35bf596a956a67dbc7151b6aa85a8259
---

```c
typedef struct {...} ArkUI_AccessibleAction
```

## 概述

无障碍操作内容结构，用于描述组件支持的无障碍操作。开发者可通过该结构体定义操作类型（actionType）及对应的操作描述信息（description），以便无障碍服务向用户播报可执行的操作。支持无障碍服务向用户呈现节点可执行的操作（如点击、长按、滚动等），并提供操作的文字说明，以帮助用户理解操作含义。

**起始版本：** 13

**相关模块：** [ArkUI\_Accessibility](capi-arkui-accessibility.md)

**所在头文件：** [native\_interface\_accessibility.h](capi-native-interface-accessibility-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_Accessibility\_ActionType](capi-native-interface-accessibility-h.md#arkui_accessibility_actiontype) actionType | 无障碍操作类型。 |
| const char\* description | 无障碍操作的描述信息。 |
