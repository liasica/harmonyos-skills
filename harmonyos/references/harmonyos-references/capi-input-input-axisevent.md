---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-axisevent
title: Input_AxisEvent
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 结构体 > Input_AxisEvent
category: harmonyos-references
scraped_at: 2026-09-02T14:52:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5afc88e8f5daeb677c7b71b388fb84f4eb676936f40c63ba5860761c42b560c7
---

```c
typedef struct Input_AxisEvent Input_AxisEvent
```

## 概述

轴事件对象。用于表示输入设备的轴事件数据，如游戏手柄的摇杆移动、鼠标滚轮滚动等场景。开发者可以通过轴事件获取输入设备的轴值变化，实现精细的输入控制，提升用户交互体验。

**起始版本：** 12

**相关模块：** [input](capi-input.md)

**所在头文件：** [oh\_input\_manager.h](capi-oh-input-manager-h.md)

**相关接口：**

| 名称 | 描述 |
| --- | --- |
| [OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent) | 创建轴事件对象。通过调用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)销毁轴事件对象。 |
| [OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent) | 销毁轴事件对象。 |
