---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-effect-types-h
title: effect_types.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > effect_types.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:05+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9b4a6a8e2feb9bbc09b5922b4021d5ae29a28b50c15bde4ff4093ad9834bf9ee
---

## 概述

PhonePC/2in1TabletTVWearable

声明滤镜效果的数据类型。

**引用文件：** <native\_effect/effect\_types.h>

**库：** libnative\_effect.so

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**相关模块：** [effectKit](capi-effectkit.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Filter\_ColorMatrix](capi-effectkit-oh-filter-colormatrix.md) | - | 定义一个用来创建滤镜效果的矩阵。 |
| [OH\_Filter](capi-effectkit-oh-filter.md) | OH\_Filter | 滤镜结构体，用来生成滤镜位图。 |
| [OH\_PixelmapNative](capi-drawing-oh-pixelmapnative.md) | OH\_PixelmapNative | 定义一个位图。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [EffectErrorCode](capi-effect-types-h.md#effecterrorcode) | EffectErrorCode | 定义滤镜效果的状态码。 |
| [EffectTileMode](capi-effect-types-h.md#effecttilemode) | EffectTileMode | 定义着色器效果平铺模式的枚举。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### EffectErrorCode

PhonePC/2in1TabletTVWearable

```
1. enum EffectErrorCode
```

**描述**

定义滤镜效果的状态码。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| EFFECT\_SUCCESS = 0 | 成功。 |
| EFFECT\_BAD\_PARAMETER = 401 | 无效的参数。 |
| EFFECT\_UNSUPPORTED\_OPERATION = 7600201 | 不支持的操作。 |
| EFFECT\_UNKNOWN\_ERROR = 7600901 | 未知错误。 |

### EffectTileMode

PhonePC/2in1TabletTVWearable

```
1. enum EffectTileMode
```

**描述**

定义着色器效果平铺模式的枚举。

**起始版本：** 14

| 枚举项 | 描述 |
| --- | --- |
| CLAMP = 0 | 如果着色器效果超出其原始边界，剩余区域使用着色器的边缘颜色填充。 |
| REPEAT | 在水平和垂直方向上重复着色器效果。 |
| MIRROR | 在水平和垂直方向上重复着色器效果，交替镜像图像，以便相邻图像始终接合。 |
| DECAL | 仅在其原始边界内渲染着色器效果。 |
