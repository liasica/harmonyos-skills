---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-keystate
title: Input_KeyState
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 结构体 > Input_KeyState
category: harmonyos-references
scraped_at: 2026-09-15T07:07:16+08:00
doc_updated_at: 2026-09-14
content_hash: sha256:03ec3d82346fba92e21a4de58423ab7b95869de7619c560b5f773607d63e4277
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
| [OH\_Input\_DestroyKeyState](capi-oh-input-manager-h.md#oh_input_destroykeystate) | 销毁按键状态的结构体对象。 |
