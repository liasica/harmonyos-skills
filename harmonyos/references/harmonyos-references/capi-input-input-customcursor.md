---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-customcursor
title: Input_CustomCursor
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 结构体 > Input_CustomCursor
category: harmonyos-references
scraped_at: 2026-09-02T14:52:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cf8728df6b3c50320bc6f0987fd281c3453b9261c52cce36157081cf50bb2792
---

```c
typedef struct Input_CustomCursor Input_CustomCursor
```

## 概述

自定义鼠标光标像素图资源。

**起始版本：** 22

**相关模块：** [input](capi-input.md)

**所在头文件：** [oh\_input\_manager.h](capi-oh-input-manager-h.md)

**相关接口：**

| 名称 | 描述 |
| --- | --- |
| [OH\_Input\_CustomCursor\_Create](capi-oh-input-manager-h.md#oh_input_customcursor_create) | 创建自定义鼠标光标资源对象。通过调用[OH\_Input\_CustomCursor\_Destroy](capi-oh-input-manager-h.md#oh_input_customcursor_destroy)销毁自定义鼠标光标资源对象。 |
| [OH\_Input\_CustomCursor\_Destroy](capi-oh-input-manager-h.md#oh_input_customcursor_destroy) | 销毁自定义鼠标光标资源对象。 |
