---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect
title: ImageEffect
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 模块 > ImageEffect
category: harmonyos-references
scraped_at: 2026-04-28T08:13:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:465987daa01649a58c37352f46505e2e7b2746623a52bc2bc6a5062b714476fb
---

## 概述

PhonePC/2in1TabletTV

提供图片编辑能力。

对应的开发指南及样例可参考[使用ImageEffect编辑图片](../harmonyos-guides/image-effect-guidelines.md)。

**起始版本：** 12

## 文件汇总

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [image\_effect.h](capi-image-effect-h.md) | 声明效果器相关接口。  效果器提供了滤镜的添加、删除、查询等功能。开发者可以通过效果器提供的接口将多个滤镜组合串联，从而实现较为复杂的效果调节功能。  同时，效果器支持多种输入类型，如Pixelmap、URI、Surface、Picture。不同的输入类型在效果器内部都会转换为内存对象，通过滤镜的效果处理，获得处理结果。 |
| [image\_effect\_errors.h](capi-image-effect-errors-h.md) | 声明图片效果器错误码。 |
| [image\_effect\_filter.h](capi-image-effect-filter-h.md) | 声明滤镜相关接口。  开发者可以通过滤镜的接口快速实现基本的效果处理，也可以将滤镜添加到效果器中，组合成滤镜链串联执行。系统提供了如“亮度”、“裁剪”等基本的效果处理滤镜。 |
