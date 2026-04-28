---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-interceptoroptions
title: Input_InterceptorOptions
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 结构体 > Input_InterceptorOptions
category: harmonyos-references
scraped_at: 2026-04-28T08:10:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8294cf82fb14a89402fc3db1b306246898845698f2e6b7f911991e61e3a607c7
---

```
1. typedef struct Input_InterceptorOptions Input_InterceptorOptions
```

## 概述

PhonePC/2in1TabletTVWearable

事件拦截选项。

**起始版本：** 12

**相关模块：** [input](capi-input.md)

**所在头文件：** [oh\_input\_manager.h](capi-oh-input-manager-h.md)

**相关接口：**

| 名称 | 描述 |
| --- | --- |
| [OH\_Input\_AddKeyEventInterceptor](capi-oh-input-manager-h.md#oh_input_addkeyeventinterceptor) | 添加按键事件的拦截，重复添加只有第一次生效。仅在应用获焦时拦截按键事件。 |
| [OH\_Input\_RemoveKeyEventInterceptor](capi-oh-input-manager-h.md#oh_input_removekeyeventinterceptor) | 移除按键事件拦截。 |
| [OH\_Input\_AddInputEventInterceptor](capi-oh-input-manager-h.md#oh_input_addinputeventinterceptor) | 添加输入事件拦截，包括鼠标、触屏和轴事件，重复添加只有第一次生效。仅命中应用窗口时拦截输入事件。 |
| [OH\_Input\_RemoveInputEventInterceptor](capi-oh-input-manager-h.md#oh_input_removeinputeventinterceptor) | 移除输入事件拦截，包括鼠标、触屏和轴事件。 |
