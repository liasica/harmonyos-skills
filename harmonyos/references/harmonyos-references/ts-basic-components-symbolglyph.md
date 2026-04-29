---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph
title: SymbolGlyph
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 文本与输入 > SymbolGlyph
category: harmonyos-references
scraped_at: 2026-04-29T13:52:13+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:e4d62bf52d389702de861caa16ea9201d2e68c75cf0179cf55dc69021f01fddf
---

显示图标小符号的组件。相关资源可参考[系统图标](../design-guides/system-icons-0000001929854962.md)。

说明

该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

不支持子组件。

## 接口

PhonePC/2in1TabletTVWearable

SymbolGlyph(value?: Resource)

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Resource](ts-types.md#resource) | 否 | SymbolGlyph组件的资源名，如 $r('sys.symbol.ohos\_wifi')。 |

说明

$r('sys.symbol.ohos\_wifi')中引用的资源为系统预置，SymbolGlyph仅支持系统预置的symbol资源名，引用非symbol资源将显示异常。

## 属性

PhonePC/2in1TabletTVWearable

支持[通用属性](ts-component-general-attributes.md)，不支持文本通用属性，仅支持以下特有属性：

### fontColor

PhonePC/2in1TabletTVWearable

fontColor(value: Array<ResourceColor>)

设置SymbolGlyph组件颜色。

说明

从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<[ResourceColor](ts-types.md#resourcecolor)> | 是 | SymbolGlyph组件颜色。  默认值：不同渲染策略下默认值不同。 |

### fontSize

PhonePC/2in1TabletTVWearable

fontSize(value: number | string | Resource)

设置SymbolGlyph组件大小。设置string类型时，支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。

组件的图标显示大小由fontSize控制，设置width或height后，其他通用属性仅对组件的占位大小生效。

说明

从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | [Resource](ts-types.md#resource) | 是 | SymbolGlyph组件大小。  默认值：16fp  单位：[fp](ts-pixel-units.md)  不支持设置百分比字符串。 |

### fontWeight

PhonePC/2in1TabletTVWearable

fontWeight(value: number | FontWeight | string)

设置SymbolGlyph组件粗细。number类型取值[100,900]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular” 、“medium”分别对应FontWeight中相应的枚举值。

sys.symbol.ohos\_lungs图标不支持设置fontWeight。

说明

从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [FontWeight](ts-appendix-enums.md#fontweight) | string | 是 | SymbolGlyph组件粗细。  默认值：FontWeight.Normal |

### renderingStrategy

PhonePC/2in1TabletTVWearable

renderingStrategy(value: SymbolRenderingStrategy)

设置SymbolGlyph组件渲染策略。

说明

从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SymbolRenderingStrategy](ts-basic-components-symbolglyph.md#symbolrenderingstrategy11枚举说明) | 是 | SymbolGlyph组件渲染策略。  默认值：SymbolRenderingStrategy.SINGLE |

不同渲染策略效果可参考以下示意图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/Kw7XpkjATGej2kgntVQkYA/zh-cn_image_0000002558766338.png?HW-CC-KV=V1&HW-CC-Date=20260429T055208Z&HW-CC-Expire=86400&HW-CC-Sign=A44AFAA9CACAB28DC503C7B9FA8BF6FE1E29D7BD70A8A51BDC27405CC694D704)

### effectStrategy

PhonePC/2in1TabletTVWearable

effectStrategy(value: SymbolEffectStrategy)

设置SymbolGlyph组件动效策略。

说明

从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SymbolEffectStrategy](ts-basic-components-symbolglyph.md#symboleffectstrategy11枚举说明) | 是 | SymbolGlyph组件动效策略。  默认值：SymbolEffectStrategy.NONE |

### symbolEffect12+

PhonePC/2in1TabletTVWearable

symbolEffect(symbolEffect: SymbolEffect, isActive?: boolean)

设置SymbolGlyph组件动效策略及播放状态。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| symbolEffect | [SymbolEffect](ts-basic-components-symbolglyph.md#symboleffect12对象说明) | 是 | SymbolGlyph组件动效策略。  默认值：[SymbolEffect](ts-basic-components-symbolglyph.md#symboleffect12对象说明) |
| isActive | boolean | 否 | SymbolGlyph组件动效播放状态。  true表示播放，false表示不播放。  默认值：false |

### symbolEffect12+

PhonePC/2in1TabletTVWearable

symbolEffect(symbolEffect: SymbolEffect, triggerValue?: number)

设置SymbolGlyph组件动效策略及播放触发器。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| symbolEffect | [SymbolEffect](ts-basic-components-symbolglyph.md#symboleffect12对象说明) | 是 | SymbolGlyph组件动效策略。  默认值：[SymbolEffect](ts-basic-components-symbolglyph.md#symboleffect12对象说明) |
| triggerValue | number | 否 | SymbolGlyph组件动效播放触发器，在数值变更时触发动效。  如果首次不希望触发动效，设置-1。 |

说明

动效属性，仅支持使用effectStrategy属性或单个symbolEffect属性，不支持多种动效属性混合使用。

### minFontScale18+

PhonePC/2in1TabletTVWearable

minFontScale(scale: Optional<number | Resource>)

设置SymbolGlyph组件最小的字体缩放倍数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number | [Resource](ts-types.md#resource)> | 是 | SymbolGlyph组件最小的字体缩放倍数。  取值范围：[0, 1]  设置为0，缩放最小。  **说明：**  设置的值小于0时，按值为0处理。设置的值大于1，按值为1处理。异常值默认不生效。 |

### maxFontScale18+

PhonePC/2in1TabletTVWearable

maxFontScale(scale: Optional<number | Resource>)

设置SymbolGlyph组件最大的字体缩放倍数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number | [Resource](ts-types.md#resource)> | 是 | SymbolGlyph组件最大的字体缩放倍数。  取值范围：[1, +∞)  **说明：**  设置的值小于1时，按值为1处理，异常值默认不生效。 |

### shaderStyle20+

PhonePC/2in1TabletTVWearable

shaderStyle(shader: Array<ShaderStyle | undefined> | ShaderStyle)

设置SymbolGlyph组件的渐变色效果。

可以显示为径向渐变[RadialGradientStyle](ts-text-common.md#radialgradientstyle20)或线性渐变[LinearGradientStyle](ts-text-common.md#lineargradientstyle20)或纯色[ColorShaderStyle](ts-text-common.md#colorshaderstyle20)的效果，shaderStyle的优先级高于[fontColor](ts-basic-components-symbolspan.md#fontcolor)和AI识别，纯色建议使用[fontColor](ts-basic-components-symbolspan.md#fontcolor)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shader | Array<[ShaderStyle](ts-text-common.md#shaderstyle20) | undefined> | [ShaderStyle](ts-text-common.md#shaderstyle20) | 是 | 径向渐变或线性渐变或纯色。  传入ShaderStyle时，覆盖所有层；传入数组时，数据项是ShaderStyle，则应用该层；数组项是undefined，则该层使用SymbolGlyph默认颜色，未设置的层也应用默认颜色。根据传入的参数区分处理径向渐变[RadialGradientStyle](ts-text-common.md#radialgradientstyle20)或线性渐变[LinearGradientStyle](ts-text-common.md#lineargradientstyle20)或纯色[ColorShaderStyle](ts-text-common.md#colorshaderstyle20)，最终设置到SymbolGlyph组件上显示为渐变色效果。  **说明：**  单位：[vp](ts-pixel-units.md)  中心点请按百分比使用。如果使用的是非百分比（例如10PX），效果等同于设置1000%。  半径建议使用百分比。  百分比是基于图标大小的百分比，建议取值范围[0, 1)。 |

### symbolShadow20+

PhonePC/2in1TabletTVWearable

symbolShadow(shadow: Optional<ShadowOptions>)

设置SymbolGlyph组件的阴影效果。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shadow | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明)> | 是 | SymbolGlyph组件的阴影效果。  单位：[vp](ts-pixel-units.md)  默认值：{  radius：0,  color：Color.Black,  offsetX：0,  offsetY：0  }  不支持fill、type属性和color中的ColoringStrategy枚举值。 |

## ScaleSymbolEffect12+

PhonePC/2in1TabletTVWearable

ScaleSymbolEffect继承自父类SymbolEffect。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scope | [EffectScope](ts-basic-components-symbolglyph.md#effectscope12枚举说明) | 否 | 是 | 动效范围。  默认值：EffectScope.LAYER |
| direction | [EffectDirection](ts-basic-components-symbolglyph.md#effectdirection12枚举说明) | 否 | 是 | 动效方向。  默认值：EffectDirection.DOWN |

### constructor12+

PhonePC/2in1TabletTVWearable

constructor(scope?: EffectScope, direction?: EffectDirection)

ScaleSymbolEffect的构造函数，缩放动效。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scope | [EffectScope](ts-basic-components-symbolglyph.md#effectscope12枚举说明) | 否 | 动效范围。  默认值：EffectScope.LAYER |
| direction | [EffectDirection](ts-basic-components-symbolglyph.md#effectdirection12枚举说明) | 否 | 动效方向。  默认值：EffectDirection.DOWN |

## HierarchicalSymbolEffect12+

PhonePC/2in1TabletTVWearable

HierarchicalSymbolEffect继承自父类SymbolEffect。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fillStyle | [EffectFillStyle](ts-basic-components-symbolglyph.md#effectfillstyle12枚举说明) | 否 | 是 | 动效模式。  默认值：EffectFillStyle.CUMULATIVE |

### constructor12+

PhonePC/2in1TabletTVWearable

constructor(fillStyle?: EffectFillStyle)

HierarchicalSymbolEffect的构造函数，层级动效。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fillStyle | [EffectFillStyle](ts-basic-components-symbolglyph.md#effectfillstyle12枚举说明) | 否 | 动效模式。  默认值：EffectFillStyle.CUMULATIVE |

## AppearSymbolEffect12+

PhonePC/2in1TabletTVWearable

AppearSymbolEffect继承自父类SymbolEffect。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scope | [EffectScope](ts-basic-components-symbolglyph.md#effectscope12枚举说明) | 否 | 是 | 动效范围。  默认值：EffectScope.LAYER |

### constructor12+

PhonePC/2in1TabletTVWearable

constructor(scope?: EffectScope)

AppearSymbolEffect的构造函数，出现动效。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scope | [EffectScope](ts-basic-components-symbolglyph.md#effectscope12枚举说明) | 否 | 动效范围。  默认值：EffectScope.LAYER |

## DisappearSymbolEffect12+

PhonePC/2in1TabletTVWearable

DisappearSymbolEffect继承自父类SymbolEffect。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scope | [EffectScope](ts-basic-components-symbolglyph.md#effectscope12枚举说明) | 否 | 是 | 动效范围。  默认值：EffectScope.LAYER |

### constructor12+

PhonePC/2in1TabletTVWearable

constructor(scope?: EffectScope)

DisappearSymbolEffect的构造函数，消失动效。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scope | [EffectScope](ts-basic-components-symbolglyph.md#effectscope12枚举说明) | 否 | 动效范围。  默认值：EffectScope.LAYER |

## BounceSymbolEffect12+

PhonePC/2in1TabletTVWearable

BounceSymbolEffect继承自父类SymbolEffect。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scope | [EffectScope](ts-basic-components-symbolglyph.md#effectscope12枚举说明) | 否 | 是 | 动效范围。  默认值：EffectScope.LAYER |
| direction | [EffectDirection](ts-basic-components-symbolglyph.md#effectdirection12枚举说明) | 否 | 是 | 动效方向。  默认值：EffectDirection.DOWN |

### constructor12+

PhonePC/2in1TabletTVWearable

constructor(scope?: EffectScope, direction?: EffectDirection)

BounceSymbolEffect的构造函数，弹跳动效。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scope | [EffectScope](ts-basic-components-symbolglyph.md#effectscope12枚举说明) | 否 | 动效范围。  默认值：EffectScope.LAYER |
| direction | [EffectDirection](ts-basic-components-symbolglyph.md#effectdirection12枚举说明) | 否 | 动效方向。  默认值：EffectDirection.DOWN |

## ReplaceSymbolEffect12+

PhonePC/2in1TabletTVWearable

ReplaceSymbolEffect继承自父类SymbolEffect。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scope | [EffectScope](ts-basic-components-symbolglyph.md#effectscope12枚举说明) | 否 | 是 | 动效范围。  默认值：EffectScope.LAYER  **卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| replaceType20+ | [ReplaceEffectType](ts-basic-components-symbolglyph.md#replaceeffecttype20枚举说明) | 否 | 是 | 替换动效类型。  默认值：ReplaceEffectType.SEQUENTIAL  **卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

### constructor12+

PhonePC/2in1TabletTVWearable

constructor(scope?: EffectScope)

ReplaceSymbolEffect的构造函数，替换动效。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scope | [EffectScope](ts-basic-components-symbolglyph.md#effectscope12枚举说明) | 否 | 动效范围。  默认值：EffectScope.LAYER |

### constructor20+

PhonePC/2in1TabletTVWearable

constructor(scope?: EffectScope, replaceType?: ReplaceEffectType)

ReplaceSymbolEffect的构造函数，替换动效。支持指定具体的替换动效类型。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scope | [EffectScope](ts-basic-components-symbolglyph.md#effectscope12枚举说明) | 否 | 动效范围。  默认值：EffectScope.LAYER |
| replaceType | [ReplaceEffectType](ts-basic-components-symbolglyph.md#replaceeffecttype20枚举说明) | 否 | 替换动效类型。  默认值：ReplaceEffectType.SEQUENTIAL |

## SymbolEffectStrategy11+枚举说明

PhonePC/2in1TabletTVWearable

动效类型的枚举值。设置动效后，动效启动即生效，无需触发。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 无动效（默认值）。 |
| SCALE | 1 | 整体缩放动效。 |
| HIERARCHICAL | 2 | 层级动效。 |

## SymbolRenderingStrategy11+枚举说明

PhonePC/2in1TabletTVWearable

渲染模式的枚举值。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SINGLE | 0 | 单色模式（默认值）。  可以设置一个或者多个颜色，默认为黑色。  当设置多个颜色时，仅生效第一个颜色。 |
| MULTIPLE\_COLOR | 1 | 多色模式。  最多可以设置三个颜色。当只设置一个颜色时，修改symbol图标的第一层颜色，其他颜色保持默认颜色。  颜色设置顺序与图标分层顺序匹配，当颜色数量大于图标分层时，多余的颜色不生效。 |
| MULTIPLE\_OPACITY | 2 | 分层模式。  默认为黑色，可以设置一个或者多个颜色。当设置多个颜色时，仅生效第一个颜色。  不透明度与图层相关，symbol通用图标的默认第一层透明度为100%、第二层透明度为50%、第三层透明度为20%。当设置的颜色包含透明度时，设置的透明度与每个图层的默认透明度进行叠加。 |

## SymbolEffect12+对象说明

PhonePC/2in1TabletTVWearable

定义SymbolEffect类。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## PulseSymbolEffect12+对象说明

PhonePC/2in1TabletTVWearable

PulseSymbolEffect继承自父类SymbolEffect，脉冲动效。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## EffectDirection12+枚举说明

PhonePC/2in1TabletTVWearable

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DOWN | 0 | 图标缩小再复原。 |
| UP | 1 | 图标放大再复原。 |

## EffectScope12+枚举说明

PhonePC/2in1TabletTVWearable

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LAYER | 0 | 分层模式。 |
| WHOLE | 1 | 整体模式。 |

## EffectFillStyle12+枚举说明

PhonePC/2in1TabletTVWearable

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CUMULATIVE | 0 | 累加模式。 |
| ITERATIVE | 1 | 迭代模式。 |

## ReplaceEffectType20+枚举说明

PhonePC/2in1TabletTVWearable

替换动效类型的枚举值。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SEQUENTIAL | 0 | 默认替换动效：当前symbol完全消失后，新symbol出现。 |
| CROSS\_FADE | 1 | 快速替换动效：当前symbol淡出的同时，新symbol淡入，产生更流畅、更快速的过渡效果。 |
| SLASH\_OVERLAY | 2 | 禁用动效：用带有斜杠遮罩层的symbol替换当前symbol，通常用于表示禁用或非活动状态。 |

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置渲染和动效策略）

从API version 11开始，该示例通过[renderingStrategy](ts-basic-components-symbolglyph.md#renderingstrategy)、[effectStrategy](ts-basic-components-symbolglyph.md#effectstrategy)属性展示了不同的渲染和动效策略。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Column() {
7. Row() {
8. Column() {
9. Text("Light")
10. SymbolGlyph($r('sys.symbol.ohos_trash'))
11. .fontWeight(FontWeight.Lighter)
12. .fontSize(96)
13. }

15. Column() {
16. Text("Normal")
17. SymbolGlyph($r('sys.symbol.ohos_trash'))
18. .fontWeight(FontWeight.Normal)
19. .fontSize(96)
20. }

22. Column() {
23. Text("Bold")
24. SymbolGlyph($r('sys.symbol.ohos_trash'))
25. .fontWeight(FontWeight.Bold)
26. .fontSize(96)
27. }
28. }

30. Row() {
31. Column() {
32. Text("单色")
33. SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
34. .fontSize(96)
35. .renderingStrategy(SymbolRenderingStrategy.SINGLE)
36. .fontColor([Color.Black, Color.Green, Color.White])
37. }

39. Column() {
40. Text("多色")
41. SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
42. .fontSize(96)
43. .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
44. .fontColor([Color.Black, Color.Green, Color.White])
45. }

47. Column() {
48. Text("分层")
49. SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
50. .fontSize(96)
51. .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)
52. .fontColor([Color.Black, Color.Green, Color.White])
53. }
54. }

56. Row() {
57. Column() {
58. Text("无动效")
59. SymbolGlyph($r('sys.symbol.ohos_wifi'))
60. .fontSize(96)
61. .effectStrategy(SymbolEffectStrategy.NONE)
62. }

64. Column() {
65. Text("整体缩放动效")
66. SymbolGlyph($r('sys.symbol.ohos_wifi'))
67. .fontSize(96)
68. .effectStrategy(SymbolEffectStrategy.SCALE)
69. }

71. Column() {
72. Text("层级动效")
73. SymbolGlyph($r('sys.symbol.ohos_wifi'))
74. .fontSize(96)
75. .effectStrategy(SymbolEffectStrategy.HIERARCHICAL)
76. }
77. }
78. }
79. }
80. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/_ghKFWWiQkqHZ7Fwx2bFYg/zh-cn_image_0000002589246149.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055208Z&HW-CC-Expire=86400&HW-CC-Sign=6BC9792C3AE1010EFFBB96CFEE32F416CA7314956CF502E940712178D5AB769A)

### 示例2（设置动效和阴影）

从API version 12开始，该示例通过[symbolEffect](ts-basic-components-symbolglyph.md#symboleffect12)属性展示了各种动效的效果以及结合[symbolShadow](ts-basic-components-symbolglyph.md#symbolshadow20)（从API version 20开始）的阴影效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. @State isActive: boolean = true;
6. @State triggerValueReplace: number = 0;
7. @State triggerValueReplace1: number = 0;
8. @State triggerValueReplace2: number = 0;
9. @State renderMode: number = 1;

11. replaceFlag: boolean = true;
12. replaceFlag1: boolean = true;
13. replaceFlag2: boolean = true;

15. options: ShadowOptions = {
16. radius: 10.0,
17. color: Color.Blue,
18. offsetX: 10,
19. offsetY: 10,
20. };

22. build() {
23. Column() {
24. Row() {
25. Column() {
26. Text("可变颜色动效")
27. SymbolGlyph($r('sys.symbol.ohos_wifi'))
28. .fontSize(96)
29. .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), this.isActive)
30. Button(this.isActive ? '关闭' : '播放')
31. .onClick(() => {
32. this.isActive = !this.isActive;
33. })
34. }
35. .margin({ right: 20 })
36. Column() {
37. Text("替换动效")
38. SymbolGlyph(this.replaceFlag ? $r('sys.symbol.checkmark_circle') : $r('sys.symbol.repeat_1'))
39. .fontSize(96)
40. .symbolEffect(new ReplaceSymbolEffect(EffectScope.WHOLE), this.triggerValueReplace)
41. Button('trigger')
42. .onClick(() => {
43. this.replaceFlag = !this.replaceFlag;
44. this.triggerValueReplace = this.triggerValueReplace + 1;
45. })
46. }
47. .margin({ right: 20 })
48. }

50. Row() {
51. Column() {
52. Text("禁用动效")
53. SymbolGlyph(this.replaceFlag1 ? $r('sys.symbol.eye_slash') : $r('sys.symbol.eye'))
54. .fontSize(96)
55. .renderingStrategy(this.renderMode)
56. .symbolEffect(new ReplaceSymbolEffect(EffectScope.LAYER, ReplaceEffectType.SLASH_OVERLAY), this.triggerValueReplace1)
57. Button('trigger')
58. .onClick(() => {
59. this.replaceFlag1 = !this.replaceFlag1;
60. this.triggerValueReplace1 = this.triggerValueReplace1 + 1;
61. })
62. }
63. .margin({ right: 20 })
64. Column() {
65. Text("快速替换动效")
66. SymbolGlyph(this.replaceFlag2 ? $r('sys.symbol.checkmark_circle') : $r('sys.symbol.repeat_1'))
67. .fontSize(96)
68. .symbolEffect(new ReplaceSymbolEffect(EffectScope.WHOLE, ReplaceEffectType.CROSS_FADE), this.triggerValueReplace2)
69. Button('trigger')
70. .onClick(() => {
71. this.replaceFlag2 = !this.replaceFlag2;
72. this.triggerValueReplace2 = this.triggerValueReplace2 + 1;
73. })
74. }
75. .margin({ right: 20 })
76. Column() {
77. Text("阴影能力")
78. SymbolGlyph($r('sys.symbol.ohos_wifi'))
79. .fontSize(96)
80. .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), this.isActive)
81. .symbolShadow(this.options)
82. Button(this.isActive ? '关闭' : '播放')
83. .onClick(() => {
84. this.isActive = !this.isActive;
85. })
86. }
87. .margin({ right: 20 })
88. }
89. }
90. .margin({
91. left: 45,
92. top: 50
93. })
94. }
95. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/zaPNiWCnT9-Jo_gl2Ey4dg/zh-cn_image_0000002558766340.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055208Z&HW-CC-Expire=86400&HW-CC-Sign=A2BE90CCB406FF79C93F548ECA076C0DDB97393E650382421AE1560301FB48EB)

### 示例3（设置颜色渐变）

从API version 20开始，该示例通过[shaderStyle](ts-basic-components-symbolglyph.md#shaderstyle20)接口实现了symbolGlyph组件显示为渐变色的功能。

```
1. @Entry
2. @Component
3. struct Index {
4. @State message: string = 'Hello World';

6. linearGradientOptions1: LinearGradientOptions = {
7. angle: 45,
8. colors: [[Color.Red, 0.0], [Color.Blue, 0.3], [Color.Green, 0.5]]
9. };

11. linearGradientOptions2: LinearGradientOptions = {
12. direction: GradientDirection.LeftTop,
13. colors: [[Color.Red, 0.0], [Color.Blue, 0.3], [Color.Green, 0.5]],
14. repeating: true,
15. };

17. radialGradientOptions: RadialGradientOptions = {
18. center: ["50%", "50%"],
19. radius: "20%",
20. colors: [[Color.Red, 0.0], [Color.Blue, 0.3], [Color.Green, 0.5]],
21. repeating: true,
22. };

24. build() {
25. Column() {
26. Row() {
27. Column() {
28. Text('angle为45°的线性渐变')
29. .fontSize(18)
30. .fontColor(0xCCCCCC)
31. .textAlign(TextAlign.Center)
32. SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
33. .fontSize(96)
34. .shaderStyle([new LinearGradientStyle(this.linearGradientOptions1)])
35. }
36. .margin({ right: 20 })
37. Column() {
38. Text('LeftTop的线性渐变')
39. .fontSize(18)
40. .fontColor(0xCCCCCC)
41. .textAlign(TextAlign.Center)
42. SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
43. .fontSize(96)
44. .shaderStyle([new LinearGradientStyle(this.linearGradientOptions2)])
45. }
46. .margin({ right: 20 })
47. }

49. Row() {
50. Column() {
51. Text('径向渐变')
52. .fontSize(18)
53. .fontColor(0xCCCCCC)
54. .textAlign(TextAlign.Center)
55. SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
56. .fontSize(96)
57. .shaderStyle([new RadialGradientStyle(this.radialGradientOptions)])
58. }
59. .margin({ right: 20 })
60. Column() {
61. Text('纯色')
62. .fontSize(18)
63. .fontColor(0xCCCCCC)
64. .textAlign(TextAlign.Center)
65. SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
66. .fontSize(96)
67. .shaderStyle([new ColorShaderStyle(Color.Red)])
68. }
69. .margin({ right: 20 })
70. Column() {
71. Text('线性和径向渐变')
72. .fontSize(18)
73. .fontColor(0xCCCCCC)
74. .textAlign(TextAlign.Center)
75. SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
76. .fontSize(96)
77. .shaderStyle([
78. new LinearGradientStyle(this.linearGradientOptions2),
79. new LinearGradientStyle(this.linearGradientOptions2),
80. new RadialGradientStyle(this.radialGradientOptions)
81. ])
82. .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)
83. }
84. .margin({ right: 20 })
85. }

87. Row() {
88. Column() {
89. Text('数组单层渐变')
90. .fontSize(18)
91. .fontColor(0xCCCCCC)
92. .textAlign(TextAlign.Center)
93. SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
94. .fontSize(96)
95. .shaderStyle([
96. new LinearGradientStyle(this.linearGradientOptions2),
97. ])
98. .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)
99. }.margin({ right: 20 })

101. Column() {
102. Text('非数组覆盖全部')
103. .fontSize(18)
104. .fontColor(0xCCCCCC)
105. .textAlign(TextAlign.Center)
106. SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
107. .fontSize(96)
108. .shaderStyle(new RadialGradientStyle(this.radialGradientOptions))
109. .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)
110. }.margin({ right: 20 })

112. Column() {
113. Text('首层为默认')
114. .fontSize(18)
115. .fontColor(0xCCCCCC)
116. .textAlign(TextAlign.Center)
117. SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
118. .fontSize(96)
119. .shaderStyle([
120. undefined,
121. new LinearGradientStyle(this.linearGradientOptions2),
122. ])
123. .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)
124. }.margin({ right: 20 })
125. }
126. }
127. .margin({
128. left: 20,
129. top: 50
130. })
131. }
132. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/bmts0TcpQ7GspNiGtS3vkw/zh-cn_image_0000002558606682.jpeg?HW-CC-KV=V1&HW-CC-Date=20260429T055208Z&HW-CC-Expire=86400&HW-CC-Sign=13FE1647AD65267910409B80726A9C76920CB8E61E40412A209E37B91A1D83E1)
