---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-cursorinfo
title: Input_CursorInfo
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 结构体 > Input_CursorInfo
category: harmonyos-references
scraped_at: 2026-09-18T06:50:21+08:00
doc_updated_at: 2026-09-17
content_hash: sha256:4231089cd62b2d7f7aeb0d3b2edbf8e6965ac17df699400a67a4793ff80545a1
---

```c
typedef struct Input_CursorInfo Input_CursorInfo
```

## 概述

定义鼠标光标信息，用于在输入系统中描述鼠标光标的显示行为和外观属性。包括光标显示状态、光标样式、光标大小档位、光标颜色。

**起始版本：** 22

**相关模块：** [input](capi-input.md)

**所在头文件：** [oh\_input\_manager.h](capi-oh-input-manager-h.md)

**相关接口：**

| 名称 | 描述 |
| --- | --- |
| [OH\_Input\_CursorInfo\_Create](capi-oh-input-manager-h.md#oh_input_cursorinfo_create) | 创建鼠标光标信息对象。通过调用[OH\_Input\_CursorInfo\_Destroy](capi-oh-input-manager-h.md#oh_input_cursorinfo_destroy)销毁鼠标光标信息对象。 |
| [OH\_Input\_CursorInfo\_Destroy](capi-oh-input-manager-h.md#oh_input_cursorinfo_destroy) | 销毁鼠标光标信息对象。 |
