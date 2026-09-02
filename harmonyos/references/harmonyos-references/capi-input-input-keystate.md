---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-keystate
title: Input_KeyState
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 结构体 > Input_KeyState
category: harmonyos-references
scraped_at: 2026-09-02T14:52:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:311d894dc643538ec6dedbf0b8251c2a584d36db0eab1b2db0c61d594f1c4af2
---

```c
typedef struct Input_KeyState Input_KeyState
```

## 概述

定义按键信息，用于标识按键行为。例如，“Ctrl”按键信息包含键值和键状态。适用于快捷键处理、输入事件状态管理、按键状态检测等场景。

**起始版本：** 12

**相关模块：** [input](capi-input.md)

**所在头文件：** [oh\_input\_manager.h](capi-oh-input-manager-h.md)

**相关接口：**

| 名称 | 描述 |
| --- | --- |
| [OH\_Input\_CreateKeyState](capi-oh-input-manager-h.md#oh_input_createkeystate) | 创建按键状态的结构体对象。通过调用[OH\_Input\_DestroyKeyState](capi-oh-input-manager-h.md#oh_input_destroykeystate)销毁按键状态的结构体对象。 |
| [OH\_Input\_DestroyKeyState](capi-oh-input-manager-h.md#oh_input_destroykeystate) | 销毁按键状态的枚举对象。 |
