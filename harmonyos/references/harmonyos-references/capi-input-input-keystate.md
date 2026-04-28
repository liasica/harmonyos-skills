---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-keystate
title: Input_KeyState
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 结构体 > Input_KeyState
category: harmonyos-references
scraped_at: 2026-04-28T08:10:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:45070731e4f72faac582ea10608ad011ba7bbf19e74b5bc872bea5a393495503
---

```
1. typedef struct Input_KeyState Input_KeyState
```

## 概述

PhonePC/2in1TabletTVWearable

定义按键信息，用于标识按键行为。例如，“Ctrl”按键信息包含键值和键类型。

**起始版本：** 12

**相关模块：** [input](capi-input.md)

**所在头文件：** [oh\_input\_manager.h](capi-oh-input-manager-h.md)

**相关接口：**

| 名称 | 描述 |
| --- | --- |
| [OH\_Input\_CreateKeyState](capi-oh-input-manager-h.md#oh_input_createkeystate) | 创建按键状态的枚举对象。通过调用[OH\_Input\_DestroyKeyState](capi-oh-input-manager-h.md#oh_input_destroykeystate)销毁按键状态的枚举对象。 |
| [OH\_Input\_DestroyKeyState](capi-oh-input-manager-h.md#oh_input_destroykeystate) | 销毁按键状态的枚举对象。 |
