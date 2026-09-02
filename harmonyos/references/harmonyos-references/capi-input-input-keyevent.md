---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-keyevent
title: Input_KeyEvent
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 结构体 > Input_KeyEvent
category: harmonyos-references
scraped_at: 2026-09-02T14:52:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:03a48d63f04c0172caba75a9cb6ca37ccc4a85e05a3a66fa10314e6eefd7af12
---

```c
typedef struct Input_KeyEvent Input_KeyEvent
```

## 概述

按键事件对象，用于表示用户按键操作产生的输入事件，包含按键码、按键状态等信息，可用于处理键盘输入和实现按键响应功能。

**起始版本：** 12

**相关模块：** [input](capi-input.md)

**所在头文件：** [oh\_input\_manager.h](capi-oh-input-manager-h.md)

**相关接口：**

| 名称 | 描述 |
| --- | --- |
| [OH\_Input\_CreateKeyEvent](capi-oh-input-manager-h.md#oh_input_createkeyevent) | 创建按键事件对象。通过调用[OH\_Input\_DestroyKeyEvent](capi-oh-input-manager-h.md#oh_input_destroykeyevent)销毁按键事件对象。 |
| [OH\_Input\_DestroyKeyEvent](capi-oh-input-manager-h.md#oh_input_destroykeyevent) | 销毁按键事件对象。 |
