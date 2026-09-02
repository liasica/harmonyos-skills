---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontdescriptor
title: OH_Drawing_FontDescriptor
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_FontDescriptor
category: harmonyos-references
scraped_at: 2026-09-02T15:02:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f3f6860e0f3227c922e52285510898e3c1b9cd1f59ea8fda6ec8c0ecaf5443b7
---

```c
typedef struct OH_Drawing_FontDescriptor {...} OH_Drawing_FontDescriptor
```

## 概述

描述系统字体详细信息的结构体。

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_text\_typography.h](capi-drawing-text-typography-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char\* path | 系统字体的文件路径。 |
| char\* postScriptName | 唯一标识字体的名称。 |
| char\* fullName | 系统字体的名称。 |
| char\* fontFamily | 系统字体的字体家族。 |
| char\* fontSubfamily | 系统字体的子字体家族。 |
| int weight | 系统字体的粗细程度。 |
| int width | 系统字体的宽窄风格属性。 |
| int italic | 系统字体倾斜度。 |
| bool monoSpace | 系统字体是否等宽。true表示字体等宽，false表示字体非等宽。 |
| bool symbolic | 系统字体是否支持符号字体。true表示支持符号字体，false表示不支持符号字体。 |
