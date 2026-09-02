---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-use-effect
title: 特效绘制合并
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 视效与模糊 > 特效绘制合并
category: harmonyos-references
scraped_at: 2026-09-02T15:00:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:65f4816ca3d4c476f030a333c6901206b54ffd2975589458e3390c606d5090df
---

用于设置组件是否应用效果模板，对背景模糊等特效进行绘制合并。

**说明** 

* 从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本模块接口仅可在Stage模型下使用。

## useEffect

useEffect(value: boolean): T

用于控制组件是否继承特效属性参数，对背景模糊等特效进行绘制合并。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 控制组件是否继承特效属性参数，从而合并绘制特效。  useEffect为true时子组件继承特效属性参数，为false时子组件不继承特效属性参数。  默认值：false |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## useEffect14+

useEffect(useEffect: boolean, effectType: EffectType): T

用于设置组件是否应用窗口定义的效果模板。effectType为DEFAULT时，必须在EffectComponent的子组件上使用且EffectComponent需配置特效属性才能生效；effectType为WINDOW\_EFFECT时，需配合窗口效果模板使用。不在对应容器内使用时，useEffect将不产生任何效果。效果模板是一组预定义的视觉特效参数（包括模糊半径、饱和度、亮度、颜色），应用于组件以实现统一的视觉特效风格。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| useEffect | boolean | 是 | 控制组件是否应用窗口定义的效果模板，从而合并绘制特效。  useEffect为true时表示应用窗口定义的效果模板，为false时不应用窗口定义的效果模板。  默认值：false |
| effectType | [EffectType](ts-universal-attributes-use-effect.md#effecttype14) | 是 | 设置组件应用窗口定义的效果模板，仅在useEffect为true时生效。  默认值：EffectType.DEFAULT |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## useEffect18+

useEffect(useEffect: Optional<boolean>, effectType?: EffectType): T

用于设置组件是否应用窗口定义的效果模板。与[useEffect14+](ts-universal-attributes-use-effect.md#useeffect14)相比，useEffect参数新增了对undefined类型的支持。effectType为DEFAULT时，必须在EffectComponent的子组件上使用且EffectComponent需配置特效属性才能生效；effectType为WINDOW\_EFFECT时，需配合窗口效果模板使用。不在对应容器内使用时，useEffect将不产生任何效果。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| useEffect | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 控制组件是否应用窗口定义的效果模板。  useEffect为true时表示应用窗口定义的效果模板，具体应用哪种效果模板由effectType参数决定。  useEffect为false时表示不应用效果模板。  默认值：false  当useEffect的值为undefined时，维持该属性上一次生效的取值不变。 |
| effectType | [EffectType](ts-universal-attributes-use-effect.md#effecttype14) | 否 | 指定效果模板的类型，应用窗口定义的效果模板。  默认值：EffectType.DEFAULT |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## EffectType14+

效果模板类型的枚举值。效果模板为预设的视觉效果参数配置，包含模糊半径、饱和度、亮度和颜色等参数。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 使用效果模板来渲染组件特效。 |
| WINDOW\_EFFECT | 1 | 使用窗口定义的效果模板来渲染组件特效。 |

效果模板

| 设备类型 | 模糊半径（单位：px） | 饱和度 | 亮度 | 颜色 |
| --- | --- | --- | --- | --- |
| 移动设备 | 0 | 0 | 0 | '#ffffffff'，显示为白色。 |
| 2in1设备：深色模式 | 80 | 1.5 | 1.0 | '#e52e3033'，显示为半透明的深灰色。 |
| 2in1设备：浅色模式 | 80 | 1.9 | 1.0 | '#e5ffffff'，显示为半透明的白色。 |
| Tablet设备 | 0 | 0 | 0 | '#ffffffff'，显示为白色。 |
