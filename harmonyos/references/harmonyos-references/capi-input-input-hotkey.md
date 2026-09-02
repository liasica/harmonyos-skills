---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-hotkey
title: Input_Hotkey
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 结构体 > Input_Hotkey
category: harmonyos-references
scraped_at: 2026-09-02T14:52:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ea6ec77c11cb96313f3335ed0a39acdda8af0b09fd62a2603ce4602869bdac3b
---

```c
typedef struct Input_Hotkey Input_Hotkey
```

## 概述

定义快捷键结构体，用于描述快捷键的按键组合、触发条件和回调处理等设计逻辑，支持应用注册和管理自定义快捷键。

**起始版本：** 14

**相关模块：** [input](capi-input.md)

**所在头文件：** [oh\_input\_manager.h](capi-oh-input-manager-h.md)

**相关接口：**

| 名称 | 描述 |
| --- | --- |
| [OH\_Input\_CreateHotkey](capi-oh-input-manager-h.md#oh_input_createhotkey) | 创建快捷键对象。通过调用[OH\_Input\_DestroyHotkey](capi-oh-input-manager-h.md#oh_input_destroyhotkey)销毁快捷键对象。 |
| [OH\_Input\_DestroyHotkey](capi-oh-input-manager-h.md#oh_input_destroyhotkey) | 销毁快捷键对象。 |
