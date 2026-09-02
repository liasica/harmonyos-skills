---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-touchevent
title: Input_TouchEvent
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 结构体 > Input_TouchEvent
category: harmonyos-references
scraped_at: 2026-09-02T14:52:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e1b81dde12466547a5390537393613744f499f4e576ea1231ae2041ebc3a659f
---

```c
typedef struct Input_TouchEvent Input_TouchEvent
```

## 概述

触屏输入事件对象，用于表示触屏输入的详细信息，包括触摸点位置、触摸状态、时间戳等。

**起始版本：** 12

**相关模块：** [input](capi-input.md)

**所在头文件：** [oh\_input\_manager.h](capi-oh-input-manager-h.md)

**相关接口：**

| 名称 | 描述 |
| --- | --- |
| [OH\_Input\_CreateTouchEvent](capi-oh-input-manager-h.md#oh_input_createtouchevent) | 创建触屏输入事件对象。通过调用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)销毁触屏输入事件对象。 |
| [OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent) | 销毁触屏输入事件对象。 |
