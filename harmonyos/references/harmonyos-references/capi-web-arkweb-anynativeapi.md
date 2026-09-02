---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-anynativeapi
title: ArkWeb_AnyNativeAPI
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_AnyNativeAPI
category: harmonyos-references
scraped_at: 2026-09-02T15:01:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e967471c2924478f65680dcdaf816e196076321b8f208a0387852c031b16f45f
---

```c
typedef struct {...} ArkWeb_AnyNativeAPI
```

## 概述

ArkWeb\_AnyNativeAPI是ArkWeb Native API的基础结构体类型，用于统一表示通过[OH\_ArkWeb\_GetNativeAPI](capi-arkweb-interface-h.md#oh_arkweb_getnativeapi)接口获取到的各类Native API结构体指针。该结构体包含一个size\_t类型的size成员，用于记录当前结构体的大小。

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

**所在头文件：** [arkweb\_interface.h](capi-arkweb-interface-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| size\_t size | 结构体对应的大小。 |
