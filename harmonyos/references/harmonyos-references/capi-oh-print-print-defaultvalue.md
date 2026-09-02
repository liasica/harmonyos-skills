---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-defaultvalue
title: Print_DefaultValue
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_DefaultValue
category: harmonyos-references
scraped_at: 2026-09-02T15:02:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dbe5d90cf4363a91069fbd5f4b5d64cfb976b9cf4b2da4233de24e52c91fcf33
---

```cpp
typedef struct {...} Print_DefaultValue
```

## 概述

表示打印机的默认属性值，包含色彩模式、双面模式、介质类型、纸张尺寸、边距、纸张来源、打印质量、份数、分辨率、方向等默认打印参数。

**起始版本：** 12

**相关模块：** [OH\_Print](capi-oh-print.md)

**所在头文件：** [ohprint.h](capi-ohprint-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Print\_ColorMode](capi-ohprint-h.md#print_colormode) defaultColorMode | 默认色彩模式，表示打印输出的色彩方式，具体取值由打印机支持的色彩模式决定。 |
| [Print\_DuplexMode](capi-ohprint-h.md#print_duplexmode) defaultDuplexMode | 默认双面模式，表示打印的单双面方式，具体取值由打印机支持的双面模式决定。 |
| char \*defaultMediaType | 默认介质类型，表示打印所使用的介质类型（如普通纸、光面纸等），具体取值由打印机支持的介质类型决定。 |
| char \*defaultPageSizeId | 默认纸张尺寸 ID，表示打印所使用的纸张尺寸标识（如"A4"、"Letter"等），具体取值由打印机支持的纸张尺寸决定。 |
| [Print\_Margin](capi-oh-print-print-margin.md) defaultMargin | 默认边距，表示打印输出页面的边距设置，具体取值由打印机支持的边距决定。 |
| char \*defaultPaperSource | 默认纸张来源，表示打印所使用的纸张来源（如自动进纸器、手动进纸等），具体取值由打印机支持的纸张来源决定。 |
| [Print\_Quality](capi-ohprint-h.md#print_quality) defaultPrintQuality | 默认打印质量，表示打印输出的质量等级设置，具体取值由打印机支持的打印质量决定。 |
| uint32\_t defaultCopies | 默认份数，取值原则：不小于 1。 |
| [Print\_Resolution](capi-oh-print-print-resolution.md) defaultResolution | 默认分辨率，表示打印输出的分辨率，具体取值由打印机支持的分辨率决定。 |
| [Print\_OrientationMode](capi-ohprint-h.md#print_orientationmode) defaultOrientation | 默认打印方向，表示打印内容的方向模式（如纵向、横向等），具体取值由打印机支持的打印方向决定。 |
| char \*otherDefaultValues | JSON 格式的其他默认值，用于表示未在上述成员变量中单独列出的额外打印默认属性，具体可设置的键值对由打印机支持的扩展能力决定。 |
