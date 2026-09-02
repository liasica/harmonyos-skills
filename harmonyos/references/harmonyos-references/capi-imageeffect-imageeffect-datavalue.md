---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect-imageeffect-datavalue
title: ImageEffect_DataValue
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > ImageEffect_DataValue
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:652febee9f450b842e23ed89e7fbd92948d499864f56eeb9373b4ad6bb00faf4
---

```c
typedef union ImageEffect_DataValue {...} ImageEffect_DataValue
```

## 概述

数据值联合体。

**起始版本：** 12

**相关模块：** [ImageEffect](capi-imageeffect.md)

**所在头文件：** [image\_effect\_filter.h](capi-image-effect-filter-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t int32Value | 整型值，对应[EFFECT\_DATA\_TYPE\_INT32](capi-image-effect-filter-h.md#imageeffect_datatype)。 |
| float floatValue | 单精度浮点值，对应[EFFECT\_DATA\_TYPE\_FLOAT](capi-image-effect-filter-h.md#imageeffect_datatype)。 |
| double doubleValue | 双精度浮点值，对应[EFFECT\_DATA\_TYPE\_DOUBLE](capi-image-effect-filter-h.md#imageeffect_datatype)。 |
| char charValue | 字节值，对应[EFFECT\_DATA\_TYPE\_CHAR](capi-image-effect-filter-h.md#imageeffect_datatype)。 |
| long longValue | 长整型值，对应[EFFECT\_DATA\_TYPE\_LONG](capi-image-effect-filter-h.md#imageeffect_datatype)。 |
| bool boolValue | 布尔值，对应[EFFECT\_DATA\_TYPE\_BOOL](capi-image-effect-filter-h.md#imageeffect_datatype)。 |
| void \*ptrValue | 指针值，对应[EFFECT\_DATA\_TYPE\_PTR](capi-image-effect-filter-h.md#imageeffect_datatype)。 |
