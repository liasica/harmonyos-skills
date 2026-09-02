---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-interceptoreventcallback
title: Input_InterceptorEventCallback
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 结构体 > Input_InterceptorEventCallback
category: harmonyos-references
scraped_at: 2026-09-02T15:02:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8cd64e46c33900606bd070075a8b6b31c2f95737861f1073eb3291d6edc05c2e
---

```c
typedef struct Input_InterceptorEventCallback {...} Input_InterceptorEventCallback
```

## 概述

拦截回调事件结构体，用于定义输入事件拦截所需的回调函数类型，支持拦截鼠标事件、触屏输入事件、按键事件和轴事件。

**起始版本：** 12

**相关模块：** [input](capi-input.md)

**所在头文件：** [oh\_input\_manager.h](capi-oh-input-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Input\_MouseEventCallback](capi-oh-input-manager-h.md#input_mouseeventcallback) mouseCallback | 鼠标事件的回调函数。 |
| [Input\_TouchEventCallback](capi-oh-input-manager-h.md#input_toucheventcallback) touchCallback | 触屏输入事件的回调函数。 |
| [Input\_AxisEventCallback](capi-oh-input-manager-h.md#input_axiseventcallback) axisCallback | 轴事件的回调函数。 |
