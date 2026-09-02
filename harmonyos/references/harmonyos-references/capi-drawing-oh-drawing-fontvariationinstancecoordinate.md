---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontvariationinstancecoordinate
title: OH_Drawing_FontVariationInstanceCoordinate
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_FontVariationInstanceCoordinate
category: harmonyos-references
scraped_at: 2026-09-02T15:02:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:07ae5d36f7ca1c7772b8c876e9a018c52368442b03eeaa5aafd86532204725c6
---

```c
typedef struct {...} OH_Drawing_FontVariationInstanceCoordinate
```

## 概述

可变字体属性键值对。

**起始版本：** 24

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_text\_font\_descriptor.h](capi-drawing-text-font-descriptor-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char\* axisKey | 可变字体属性键值对中的关键字标识的字符串。 |
| double value | 可变字体属性键值对的值。 |
