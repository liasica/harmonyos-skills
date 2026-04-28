---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-javascriptobject
title: ArkWeb_JavaScriptObject
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_JavaScriptObject
category: harmonyos-references
scraped_at: 2026-04-28T08:05:30+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9acd56363656c2b1de88b14bfbdd7cc1e2e23b93c7d9d3d6264d7385424dbf2d
---

```
1. typedef struct {...} ArkWeb_JavaScriptObject
```

## 概述

PhonePC/2in1TabletTVWearable

注入的JavaScript结构体。

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

**所在头文件：** [arkweb\_type.h](capi-arkweb-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const uint8\_t\* buffer | 注入的JavaScript代码。 |
| size\_t size | JavaScript代码长度。 |
| [ArkWeb\_OnJavaScriptCallback](capi-arkweb-type-h.md#arkweb_onjavascriptcallback) callback | JavaScript执行完成的回调。 |
| void\* userData | 需要在回调中携带的自定义数据。 |
