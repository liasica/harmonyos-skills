---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-javascriptobject
title: ArkWeb_JavaScriptObject
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_JavaScriptObject
category: harmonyos-references
scraped_at: 2026-09-02T15:01:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:82a8a3b301547fd4789a869708c98ff9bce04e683cf5f676f319ade17114956b
---

```c
typedef struct {...} ArkWeb_JavaScriptObject
```

## 概述

**ArkWeb\_JavaScriptObject** 结构体用于向Web页面注入JavaScript代码并获取执行结果。适用于需要从原生应用主动调用Web页面中的JavaScript函数、读取Web页面状态或调用Web页面API的场景，可简化Web与原生应用间的数据交互流程。开发者可通过该结构体指定待注入的JavaScript脚本内容及长度，注册执行完成回调，并通过userData传递自定义上下文数据，实现Web与原生应用之间的数据交互。

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

**所在头文件：** [arkweb\_type.h](capi-arkweb-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const uint8\_t\* buffer | 注入的JavaScript代码。该缓冲区长度需与size参数一致。 |
| size\_t size | JavaScript代码长度。单位：字节。需与buffer的实际长度一致，否则可能导致越界或截断。 |
| [ArkWeb\_OnJavaScriptCallback](capi-arkweb-type-h.md#arkweb_onjavascriptcallback) callback | JavaScript执行完成的回调。回调函数指针，传入NULL表示不需要回调。 |
| void\* userData | 需要在回调中携带的自定义数据。 |
