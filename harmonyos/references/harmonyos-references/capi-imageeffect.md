---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect
title: ImageEffect
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 模块 > ImageEffect
category: harmonyos-references
scraped_at: 2026-09-02T14:52:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f2cbb32b2c91cc6368bbe3faee71c5c0340f2ac0b579d6bcc901f41c0905bb83
---

## 概述

提供图片编辑能力。

对应的开发指南及样例可参考[使用ImageEffect编辑图片](../harmonyos-guides/image-effect-guidelines.md)。

**起始版本：** 12

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [image\_effect.h](capi-image-effect-h.md) | 声明效果器相关接口。  效果器提供了滤镜的添加、删除、查询等功能。开发者可以通过效果器提供的接口将多个滤镜组合串联，从而实现较为复杂的效果调节功能。  同时，效果器支持多种输入类型，如Pixelmap、URI、Surface、Picture。不同的输入类型在效果器内部都会转换为内存对象，通过滤镜的效果处理，获得处理结果。 |
| [image\_effect\_errors.h](capi-image-effect-errors-h.md) | 声明图片效果器错误码。 |
| [image\_effect\_filter.h](capi-image-effect-filter-h.md) | 声明滤镜相关接口。  开发者可以通过滤镜的接口快速实现基本的效果处理，也可以将滤镜添加到效果器中，组合成滤镜链串联执行。系统提供了如“亮度”、“裁剪”等基本的效果处理滤镜。 |
