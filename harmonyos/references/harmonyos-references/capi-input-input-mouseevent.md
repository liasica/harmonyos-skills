---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-mouseevent
title: Input_MouseEvent
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 结构体 > Input_MouseEvent
category: harmonyos-references
scraped_at: 2026-09-02T14:52:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:46d487502302e69c43e9e9931de7515719e4e7eb6b0f8fe3f84f56e48d31082c
---

```c
typedef struct Input_MouseEvent Input_MouseEvent
```

## 概述

鼠标事件对象，用于表示用户鼠标操作产生的输入事件，包含点击信息、坐标、点击动作事件等信息，可用于处理鼠标事件输入和实现鼠标事件响应的功能。

**起始版本：** 12

**相关模块：** [input](capi-input.md)

**所在头文件：** [oh\_input\_manager.h](capi-oh-input-manager-h.md)

**相关接口：**

| 名称 | 描述 |
| --- | --- |
| [OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent) | 创建鼠标事件对象。通过调用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)销毁鼠标事件对象。 |
| [OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent) | 销毁鼠标事件对象。 |
