---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontdescriptor
title: OH_Drawing_FontDescriptor
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_FontDescriptor
category: harmonyos-references
scraped_at: 2026-04-28T08:15:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:24fc1159de8e34c0c4d0fc8cd670c1fe236f21ea6322144f2655089f6b1838f4
---

```
1. typedef struct OH_Drawing_FontDescriptor {...} OH_Drawing_FontDescriptor
```

## 概述

PhonePC/2in1TabletTVWearable

描述系统字体详细信息的结构体。

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_text\_typography.h](capi-drawing-text-typography-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

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
| bool monoSpace | 系统字体是否紧凑。true表示字体紧凑，false表示字体非紧凑。 |
| bool symbolic | 系统字体是否支持符号字体。true表示支持符号字体，false表示不支持符号字体。 |
