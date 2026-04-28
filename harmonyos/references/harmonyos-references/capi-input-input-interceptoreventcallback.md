---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-interceptoreventcallback
title: Input_InterceptorEventCallback
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 结构体 > Input_InterceptorEventCallback
category: harmonyos-references
scraped_at: 2026-04-28T08:10:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d8b1951fbd60cacdd67c7a96e0a987d71c059d3e9f64e11f8ad830fb7c73a789
---

```
1. typedef struct Input_InterceptorEventCallback {...} Input_InterceptorEventCallback
```

## 概述

PhonePC/2in1TabletTVWearable

拦截回调事件结构体，拦截鼠标事件、触屏输入事件和轴事件。

**起始版本：** 12

**相关模块：** [input](capi-input.md)

**所在头文件：** [oh\_input\_manager.h](capi-oh-input-manager-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Input\_MouseEventCallback](capi-input-input-interceptoreventcallback.md#input_mouseeventcallback) mouseCallback | 鼠标事件的回调函数。 |
| [Input\_TouchEventCallback](capi-input-input-interceptoreventcallback.md#input_toucheventcallback) touchCallback | 触屏输入事件的回调函数。 |
| [Input\_AxisEventCallback](capi-input-input-interceptoreventcallback.md#input_axiseventcallback) axisCallback | 轴事件的回调函数。 |

### 成员函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*Input\_KeyEventCallback)(const Input\_KeyEvent\* keyEvent)](capi-input-input-interceptoreventcallback.md#input_keyeventcallback) | Input\_KeyEventCallback() | 按键事件的回调函数，keyEvent的生命周期为回调函数内。 |
| [typedef void (\*Input\_MouseEventCallback)(const Input\_MouseEvent\* mouseEvent)](capi-input-input-interceptoreventcallback.md#input_mouseeventcallback) | Input\_MouseEventCallback() | 鼠标事件的回调函数，mouseEvent的生命周期为回调函数内。 |
| [typedef void (\*Input\_TouchEventCallback)(const Input\_TouchEvent\* touchEvent)](capi-input-input-interceptoreventcallback.md#input_toucheventcallback) | Input\_TouchEventCallback() | 触屏输入事件的回调函数，touchEvent的生命周期为回调函数内。 |
| [typedef void (\*Input\_AxisEventCallback)(const Input\_AxisEvent\* axisEvent)](capi-input-input-interceptoreventcallback.md#input_axiseventcallback) | Input\_AxisEventCallback() | 轴事件的回调函数，axisEvent的生命周期为回调函数内。 |

## 成员函数说明

PhonePC/2in1TabletTVWearable

### Input\_KeyEventCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Input_KeyEventCallback)(const Input_KeyEvent* keyEvent)
```

**描述**

按键事件的回调函数，keyEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_KeyEvent](capi-input-input-keyevent.md)\* keyEvent | 按键事件对象。 |

### Input\_MouseEventCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Input_MouseEventCallback)(const Input_MouseEvent* mouseEvent)
```

**描述**

鼠标事件的回调函数，mouseEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象。 |

### Input\_TouchEventCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Input_TouchEventCallback)(const Input_TouchEvent* touchEvent)
```

**描述**

触屏输入事件的回调函数，touchEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_TouchEvent](capi-input-input-touchevent.md)\* touchEvent | 触屏输入事件对象。 |

### Input\_AxisEventCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Input_AxisEventCallback)(const Input_AxisEvent* axisEvent)
```

**描述**

轴事件的回调函数，axisEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象。 |
