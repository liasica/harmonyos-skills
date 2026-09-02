---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-cursorconfig
title: Input_CursorConfig
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 结构体 > Input_CursorConfig
category: harmonyos-references
scraped_at: 2026-09-02T14:52:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:404b8e793af9827e478cf5c0b8c3d5163dd3960ef606018d38def98d7090a475
---

```c
typedef struct Input_CursorConfig Input_CursorConfig
```

## 概述

自定义鼠标光标配置，用于定义和管理应用程序中鼠标光标的显示样式和交互行为。支持设置不同类型的光标样式（如默认、手形、文本输入等），为用户提供更直观的操作反馈，提升用户体验。

**起始版本：** 22

**相关模块：** [input](capi-input.md)

**所在头文件：** [oh\_input\_manager.h](capi-oh-input-manager-h.md)

**相关接口：**

| 名称 | 描述 |
| --- | --- |
| [OH\_Input\_CursorConfig\_Create](capi-oh-input-manager-h.md#oh_input_cursorconfig_create) | 创建自定义鼠标光标配置对象。通过调用[OH\_Input\_CursorConfig\_Destroy](capi-oh-input-manager-h.md#oh_input_cursorconfig_destroy)销毁自定义鼠标光标配置对象。 |
| [OH\_Input\_CursorConfig\_Destroy](capi-oh-input-manager-h.md#oh_input_cursorconfig_destroy) | 销毁自定义鼠标光标配置对象。 |
