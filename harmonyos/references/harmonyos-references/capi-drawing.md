---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing
title: Drawing
category: harmonyos-references
scraped_at: 2026-04-28T08:14:48+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:873d10ea6b112f686e8b9ebdbdc3b38cdf7ab5bc6e9a1a7677e291b708c8d0cc
---

## 概述

PhonePC/2in1TabletTVWearable

Drawing模块提供包括2D图形渲染、文字绘制和图片显示等功能函数。

本模块采用屏幕物理像素单位px。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

## 文件汇总

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [drawing\_bitmap.h](capi-drawing-bitmap-h.md) | 文件中定义了与位图相关的功能函数。 |
| [drawing\_brush.h](capi-drawing-brush-h.md) | 文件中定义了与画刷相关的功能函数。 |
| [drawing\_canvas.h](capi-drawing-canvas-h.md) | 文件中定义了与画布相关的功能函数。  画布自带一个黑色，开启抗锯齿，不具备其他任何样式的默认画刷，当且仅当画布中主动设置的画刷和画笔都不存在时生效。 |
| [drawing\_color.h](capi-drawing-color-h.md) | 文件中定义了与颜色相关的功能函数。 |
| [drawing\_color\_filter.h](capi-drawing-color-filter-h.md) | 声明与绘图模块中的颜色滤波器对象相关的函数。 |
| [drawing\_color\_space.h](capi-drawing-color-space-h.md) | 文件中定义了与颜色空间相关的功能函数。 |
| [drawing\_error\_code.h](capi-drawing-error-code-h.md) | 声明与绘图模块中的错误码相关的函数。include native\_drawing/drawing\_error\_code.h |
| [drawing\_filter.h](capi-drawing-filter-h.md) | 声明与绘图模块中的滤波器对象相关的函数。 |
| [drawing\_font.h](capi-drawing-font-h.md) | 文件中定义了与字体相关的功能函数。 |
| [drawing\_font\_collection.h](capi-drawing-font-collection-h.md) | 定义绘制模块中与字体集合相关的函数。 |
| [drawing\_font\_mgr.h](capi-drawing-font-mgr-h.md) | 文件中定义了与字体管理相关的功能函数，用于加载和匹配系统中可用的字体。 |
| [drawing\_gpu\_context.h](capi-drawing-gpu-context-h.md) | 声明与绘图模块中的图形处理器上下文对象相关的函数。 |
| [drawing\_image.h](capi-drawing-image-h.md) | 文件中定义了与图片相关的功能函数。 |
| [drawing\_image\_filter.h](capi-drawing-image-filter-h.md) | 声明与绘图模块中的图像滤波器对象相关的函数。 |
| [drawing\_mask\_filter.h](capi-drawing-mask-filter-h.md) | 声明与绘图模块中的对象相关的函数。 |
| [drawing\_matrix.h](capi-drawing-matrix-h.md) | 文件中定义了与矩阵相关的功能函数。 |
| [drawing\_memory\_stream.h](capi-drawing-memory-stream-h.md) | 文件中定义了与内存流相关的功能函数。 |
| [drawing\_path.h](capi-drawing-path-h.md) | 文件中定义了与自定义路径相关的功能函数。 |
| [drawing\_path\_effect.h](capi-drawing-path-effect-h.md) | 文件中定义了与路径效果相关的功能函数。 |
| [drawing\_pen.h](capi-drawing-pen-h.md) | 文件中定义了与画笔相关的功能函数。 |
| [drawing\_pixel\_map.h](capi-drawing-pixel-map-h.md) | 声明与绘图模块中的像素图对象相关的函数。 |
| [drawing\_point.h](capi-drawing-point-h.md) | 文件中定义了与坐标点相关的功能函数。 |
| [drawing\_record\_cmd.h](capi-drawing-record-cmd-h.md) | 文件中定义了与录制指令对象相关的功能函数。 |
| [drawing\_rect.h](capi-drawing-rect-h.md) | 文件中定义了与矩形相关的功能函数。 |
| [drawing\_region.h](capi-drawing-region-h.md) | 定义了与区域相关的功能函数，包括区域的创建，边界设置和销毁等。 |
| [drawing\_register\_font.h](capi-drawing-register-font-h.md) | 定义绘制模块中字体管理器相关的函数。 |
| [drawing\_round\_rect.h](capi-drawing-round-rect-h.md) | 文件中定义了与圆角矩形相关的功能函数。 |
| [drawing\_sampling\_options.h](capi-drawing-sampling-options-h.md) | 文件中定义了与采样相关的功能函数。用于图片或者纹理等图像的采样。 |
| [drawing\_shader\_effect.h](capi-drawing-shader-effect-h.md) | 声明与绘图模块中的着色器对象相关的函数。 |
| [drawing\_shadow\_layer.h](capi-drawing-shadow-layer-h.md) | 声明与绘图模块中的阴影层对象相关的函数。 |
| [drawing\_surface.h](capi-drawing-surface-h.md) | 文件中定义与surface相关的功能函数，包括surface的创建、销毁和使用等。 |
| [drawing\_text\_blob.h](capi-drawing-text-blob-h.md) | 文件中定义了与文字相关的功能函数。 |
| [drawing\_text\_declaration.h](capi-drawing-text-declaration-h.md) | 提供2D绘制文本相关的数据结构声明。 |
| [drawing\_text\_font\_descriptor.h](capi-drawing-text-font-descriptor-h.md) | 定义了字体信息的相关接口，比如获取字体信息，查找指定字体等。 |
| [drawing\_text\_global.h](capi-drawing-text-global-h.md) | 提供文本全局信息的相关接口，比如设置文本渲染高对比度模式等。 |
| [drawing\_text\_line.h](capi-drawing-text-line-h.md) | 提供获取文本行内的字符位置、获取渲染单元信息和按行截断等功能。 |
| [drawing\_text\_lineTypography.h](capi-drawing-text-linetypography-h.md) | 提供排版行相关的接口，比如获取指定位置处开始可以排版的字符个数等函数。 |
| [drawing\_text\_run.h](capi-drawing-text-run-h.md) | 提供字体渲染单元的相关接口，比如绘制功能、获取排版边界功能等。 |
| [drawing\_text\_typography.h](capi-drawing-text-typography-h.md) | 定义绘制模块中排版相关的函数。 |
| [drawing\_typeface.h](capi-drawing-typeface-h.md) | 文件中定义了与字形相关的功能函数。  不同的平台有自己的默认字形，也可以从ttf文件解析出三方指定字形，如宋体、黑体字形等。 |
| [drawing\_types.h](capi-drawing-types-h.md) | 文件中定义了用于绘制2d图形的数据类型，包括画布、画笔、画刷、位图和路径。 |
