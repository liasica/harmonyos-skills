---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-configurationconstant
title: @ohos.app.ability.ConfigurationConstant (环境变量相关的常量定义)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 通用能力的接口(推荐) > @ohos.app.ability.ConfigurationConstant (环境变量相关的常量定义)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3f924ed27c58c9b3f33eb2d020b1f5bdb6c668f47fbf302af8c5f0b913c8eb76
---

ConfigurationConstant模块提供了[Configuration](js-apis-app-ability-configuration.md)操作相关的系统预置枚举。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { ConfigurationConstant } from '@kit.AbilityKit';
```

## ColorMode

PhonePC/2in1TabletTVWearable

表示深浅色模式的枚举，用于[Configuration.colorMode](js-apis-app-ability-configuration.md#configuration)字段。开发者可以使用这些预置枚举设置或获取系统/应用的深浅色模式。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityBase

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COLOR\_MODE\_NOT\_SET | -1 | 表示未设置颜色模式。 |
| COLOR\_MODE\_DARK | 0 | 表示深色模式。 |
| COLOR\_MODE\_LIGHT | 1 | 表示浅色模式。 |

## Direction

PhonePC/2in1TabletTVWearable

表示屏幕方向的枚举，用于[Configuration.direction](js-apis-app-ability-configuration.md#configuration)字段。开发者可以使用这些预置枚举设置或获取系统/应用的显示方向。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityBase

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DIRECTION\_NOT\_SET | -1 | 表示未设置方向。 |
| DIRECTION\_VERTICAL | 0 | 表示垂直方向。 |
| DIRECTION\_HORIZONTAL | 1 | 表示水平方向。 |

## ScreenDensity

PhonePC/2in1TabletTVWearable

表示屏幕像素密度的枚举，用于[Configuration.screenDensity](js-apis-app-ability-configuration.md#configuration)字段。开发者可以使用这些预置枚举设置或获取屏幕的像素密度。

字体显示大小与屏幕像素密度呈正相关关系。通过监听屏幕像素密度变化，可以感知字体显示大小的调整。通常情况下，对于相同的物理尺寸，屏幕像素密度越高，字体显示效果越大。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityBase

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCREEN\_DENSITY\_NOT\_SET | 0 | 表示未设置屏幕像素密度。 |
| SCREEN\_DENSITY\_SDPI | 120 | 表示屏幕像素密度为'SDPI'。 |
| SCREEN\_DENSITY\_MDPI | 160 | 表示屏幕像素密度为'MDPI'。 |
| SCREEN\_DENSITY\_LDPI | 240 | 表示屏幕像素密度为'LDPI'。 |
| SCREEN\_DENSITY\_XLDPI | 320 | 表示屏幕像素密度为'XLDPI'。 |
| SCREEN\_DENSITY\_XXLDPI | 480 | 表示屏幕像素密度为'XXLDPI'。 |
| SCREEN\_DENSITY\_XXXLDPI | 640 | 表示屏幕像素密度为'XXXLDPI'。 |
