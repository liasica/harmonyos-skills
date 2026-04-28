---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-use-effect
title: 特效绘制合并
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 视效与模糊 > 特效绘制合并
category: harmonyos-references
scraped_at: 2026-04-28T08:01:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9f5244f6c191e1b66e943c33c23065985151d0de8c52ab83dfaf964adec076d1
---

用于对背景模糊等特效进行绘制合并。

说明

从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## useEffect

PhonePC/2in1TabletTVWearable

useEffect(value: boolean): T

用于对背景模糊等特效进行绘制合并。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 控制组件是否继承特效绘制合并组件的特效属性参数，从而合并绘制特效。  useEffect为true时子组件继承特效绘制合并组件的特效属性参数，为false时子组件不继承特效绘制合并组件的特效属性参数。  默认值：false |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## useEffect14+

PhonePC/2in1TabletTVWearable

useEffect(useEffect: boolean, effectType: EffectType): T

用于设置组件是否应用窗口定义的效果模板。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| useEffect | boolean | 是 | 控制组件是否应用窗口定义的效果模板。  useEffect为true时表示应用窗口定义的效果模板。  默认值：false |
| effectType | [EffectType](ts-universal-attributes-use-effect.md#effecttype14) | 是 | 设置组件应用窗口定义的效果模板。  默认值：EffectType.DEFAULT |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## useEffect18+

PhonePC/2in1TabletTVWearable

useEffect(useEffect: Optional<boolean>, effectType?: EffectType): T

用于设置组件是否应用窗口定义的效果模板。与[useEffect14+](ts-universal-attributes-use-effect.md#useeffect14)相比，useEffect参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| useEffect | Optional<boolean> | 是 | 控制组件是否应用窗口定义的效果模板。  useEffect为true时表示应用窗口定义的效果模板。  默认值：false  当useEffect的值为undefined时，维持之前取值。 |
| effectType | [EffectType](ts-universal-attributes-use-effect.md#effecttype14) | 否 | 设置组件应用窗口定义的效果模板。  默认值：EffectType.DEFAULT |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## EffectType14+

PhonePC/2in1TabletTVWearable

使用效果模板种类的枚举值。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 使用效果模板进行定义。 |
| WINDOW\_EFFECT | 1 | 使用窗口定义的效果模板进行定义。 |

效果模板

| 设备类型 | 模糊半径(单位: px) | 饱和度 | 亮度 | 颜色 |
| --- | --- | --- | --- | --- |
| 移动设备 | 0 | 0 | 0 | '#ffffffff'，显示为白色。 |
| 2in1设备：深色模式 | 80 | 1.5 | 1.0 | '#e52e3033'，显示为淡红色的半透明效果。 |
| 2in1设备：浅色模式 | 80 | 1.9 | 1.0 | '#e5ffffff'，显示为半透明的深红色。 |
| Tablet设备 | 0 | 0 | 0 | '#ffffffff'，显示为白色。 |
