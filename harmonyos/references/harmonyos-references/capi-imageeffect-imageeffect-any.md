---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect-imageeffect-any
title: ImageEffect_Any
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > ImageEffect_Any
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:edb4447fb7a333cf3fe7cfb49060b3f4e2e4e062f7d435f964f1584cf4b0b239
---

```c
typedef struct ImageEffect_Any {...} ImageEffect_Any
```

## 概述

参数结构体。

**起始版本：** 12

**相关模块：** [ImageEffect](capi-imageeffect.md)

**所在头文件：** [image\_effect\_filter.h](capi-image-effect-filter-h.md)

## 汇总

### 成员变量

**支持C++语言语法的声明如下：**

| 名称 | 描述 |
| --- | --- |
| [ImageEffect\_DataType](capi-image-effect-filter-h.md#imageeffect_datatype) dataType = [ImageEffect\_DataType](capi-image-effect-filter-h.md#imageeffect_datatype)::EFFECT\_DATA\_TYPE\_UNKNOWN | 参数类型，默认为未定义类型。 |
| [ImageEffect\_DataValue](capi-imageeffect-imageeffect-datavalue.md) dataValue = { 0 } | 参数值，默认为空。 |

**支持C语言语法的声明如下：**

| 名称 | 描述 |
| --- | --- |
| [ImageEffect\_DataType](capi-image-effect-filter-h.md#imageeffect_datatype) dataType | 参数类型。 |
| [ImageEffect\_DataValue](capi-imageeffect-imageeffect-datavalue.md) dataValue | 参数值。 |
