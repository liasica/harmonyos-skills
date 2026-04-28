---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdslistitemcard
title: HdsListItemCard
breadcrumb: API参考 > 应用框架 > UI Design Kit（UI设计套件） > ArkTS组件 > HdsListItemCard
category: harmonyos-references
scraped_at: 2026-04-28T08:06:44+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:87b3d47382b2e8315caaf5e95c2b3609173d6038677f8f669905ab971f3a0913
---

本模块提供一个HdsListItemCard组件，提升视觉体验，统一组件风格样式，应用使用HdsListItemCard组件实现多设备上的系统列表样式。

**起始版本：** 6.0.0(20)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { HdsListItemCard } from '@kit.UIDesignKit';
```

## 接口

PhonePC/2in1TabletTVWearable

HdsListItemCard(options: HdsListItemCardOptions)

HdsListItemCard列表项组件。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**设备行为异常：** 该接口在TV中与ux规范不一致（获焦态和悬停态组件未放大，获焦态背板颜色未变化，Button内部的text默认颜色等），在其他设备类型中可正常使用。

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [HdsListItemCardOptions](ui-design-hdslistitemcard.md#hdslistitemcardoptions) | 是 | HdsListItemCard列表项内容。 |

## 属性

PhonePC/2in1TabletTVWearable

当前仅支持[通用属性](ts-component-general-attributes.md)。

说明

1. 该通用属性针对的是HdsListItemCard组件，无法通过其设置组件内部的左侧元素，中间元素，右侧元素的属性。
2. 对于[HdsListItemCardOptions](ui-design-hdslistitemcard.md#hdslistitemcardoptions)中已经有的列表项属性，比如的cardWidth，cardHeight，cardBackgroundColor，onClick，enable，cardId等，建议直接使用[HdsListItemCardOptions](ui-design-hdslistitemcard.md#hdslistitemcardoptions)进行属性设置，不要使用通用属性。否则，会出现混淆或者不生效。
3. 不建议使用padding，margin，borderWidth，borderColor，scale等通用属性，会跟HdsListItemCard组件本身内置的属性相冲突，导致布局异常或者不生效。

## PrefixItem

PhonePC/2in1TabletTVWearable

定义PrefixItem类，HdsListItemCard列表项的A区（列表左侧）元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

## PrefixImage

PhonePC/2in1TabletTVWearable

PrefixImage继承自父类[PrefixItem](ui-design-hdslistitemcard.md#prefixitem)，A区（列表左侧）Image元素，穿戴设备中Image大小不可修改，为固定值46vp\*46vp。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [ImageClickOptions](ui-design-hdslistitemcard.md#imageclickoptions) | 否 | 是 | A区（列表左侧）Image元素的配置项。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: ImageClickOptions)

PrefixImage的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ImageClickOptions](ui-design-hdslistitemcard.md#imageclickoptions) | 否 | A区（列表左侧）Image元素的配置项。 |

## PrefixIcon

PhonePC/2in1TabletTVWearable

PrefixIcon继承自父类[PrefixItem](ui-design-hdslistitemcard.md#prefixitem)，A区（列表左侧）Icon元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [PrefixIconOptions](ui-design-hdslistitemcard.md#prefixiconoptions) | 否 | 是 | A区（列表左侧）Icon元素的配置项。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: PrefixIconOptions)

PrefixIcon的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [PrefixIconOptions](ui-design-hdslistitemcard.md#prefixiconoptions) | 否 | A区（列表左侧）Icon元素的配置项。 |

## PrefixBadge

PhonePC/2in1TabletTVWearable

PrefixBadge继承自父类[PrefixItem](ui-design-hdslistitemcard.md#prefixitem)，A区（列表左侧）Badge元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [BadgeOptions](ui-design-hdslistitemcard.md#badgeoptions) | 否 | 是 | A区（列表左侧）Badge元素的配置项。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: BadgeOptions)

PrefixBadge的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [BadgeOptions](ui-design-hdslistitemcard.md#badgeoptions) | 否 | A区（列表左侧）Badge元素的配置项。 |

## PrefixSwitch

PhonePC/2in1TabletTVWearable

PrefixSwitch继承自父类[PrefixItem](ui-design-hdslistitemcard.md#prefixitem)，A区（列表左侧）Switch元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [CheckOptions](ui-design-hdslistitemcard.md#checkoptions) | 否 | 是 | A区（列表左侧）Switch元素的配置项。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: CheckOptions)

PrefixSwitch的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CheckOptions](ui-design-hdslistitemcard.md#checkoptions) | 否 | A区（列表左侧）Switch元素的配置项。 |

## PrefixToggleButton

PhonePC/2in1TabletTVWearable

PrefixToggleButton继承自父类[PrefixItem](ui-design-hdslistitemcard.md#prefixitem)，A区（列表左侧）ToggleButton元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [ToggleButtonOptions](ui-design-hdslistitemcard.md#togglebuttonoptions) | 否 | 是 | A区（列表左侧）ToggleButton元素的配置项。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: ToggleButtonOptions)

PrefixToggleButton的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ToggleButtonOptions](ui-design-hdslistitemcard.md#togglebuttonoptions) | 否 | A区（列表左侧）ToggleButton元素的配置项。 |

## PrefixButton

PhonePC/2in1TabletTVWearable

PrefixButton继承自父类[PrefixItem](ui-design-hdslistitemcard.md#prefixitem)，A区（列表左侧）Button元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [ButtonOptions](ui-design-hdslistitemcard.md#buttonoptions) | 否 | 是 | A区（列表左侧）Button元素的配置项。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: ButtonOptions)

PrefixButton的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ButtonOptions](ui-design-hdslistitemcard.md#buttonoptions) | 否 | A区（列表左侧）Button元素的配置项。 |

## PrefixCustomBuilder

PhonePC/2in1TabletTVWearable

PrefixCustomBuilder继承自父类[PrefixItem](ui-design-hdslistitemcard.md#prefixitem)，A区（列表左侧）自定义内容。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| customBuilder | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 是 | A区（列表左侧）自定义内容。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(customBuilder?: CustomBuilder)

PrefixCustomBuilder的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| customBuilder | [CustomBuilder](ts-types.md#custombuilder8) | 否 | A区（列表左侧）自定义内容。 |

## SuffixItem

PhonePC/2in1TabletTVWearable

定义SuffixItem类，HdsListItemCard列表项的C区（列表右侧）元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

## SuffixText

PhonePC/2in1TabletTVWearable

SuffixText继承自父类[SuffixItem](ui-design-hdslistitemcard.md#suffixitem)，C区（列表右侧）Text元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [TextOptions](ui-design-hdslistitemcard.md#textoptions) | 否 | 是 | C区（列表右侧）Text元素的配置项。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: TextOptions)

SuffixText的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TextOptions](ui-design-hdslistitemcard.md#textoptions) | 否 | C区（列表右侧）Text元素的配置项。 |

## SuffixImage

PhonePC/2in1TabletTVWearable

SuffixImage继承自父类[SuffixItem](ui-design-hdslistitemcard.md#suffixitem)，C区（列表右侧）Image元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [ImageClickOptions](ui-design-hdslistitemcard.md#imageclickoptions) | 否 | 是 | C区（列表右侧）Image元素的配置项。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: ImageClickOptions)

SuffixImage的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ImageClickOptions](ui-design-hdslistitemcard.md#imageclickoptions) | 否 | C区（列表右侧）Image元素的配置项。 |

## SuffixLoadingProgress

PhonePC/2in1TabletTVWearable

SuffixLoadingProgress继承自父类[SuffixItem](ui-design-hdslistitemcard.md#suffixitem)，C区（列表右侧）LoadingProgress元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [ColorOptions](ui-design-hdslistitemcard.md#coloroptions) | 否 | 是 | C区（列表右侧）LoadingProgress元素的配置项。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: ColorOptions)

SuffixLoadingProgress的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ColorOptions](ui-design-hdslistitemcard.md#coloroptions) | 否 | C区（列表右侧）LoadingProgress元素的配置项。 |

## SuffixRadio

PhonePC/2in1TabletTVWearable

SuffixRadio继承自父类[SuffixItem](ui-design-hdslistitemcard.md#suffixitem)，C区（列表右侧）Radio元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [CheckOptions](ui-design-hdslistitemcard.md#checkoptions) | 否 | 是 | C区（列表右侧）Radio元素的配置项。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: CheckOptions)

SuffixRadio的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CheckOptions](ui-design-hdslistitemcard.md#checkoptions) | 否 | C区（列表右侧）Radio元素的配置项。 |

## SuffixCheckbox

PhonePC/2in1TabletTVWearable

SuffixCheckbox继承自父类[SuffixItem](ui-design-hdslistitemcard.md#suffixitem)，C区（列表右侧）Checkbox元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [CheckOptions](ui-design-hdslistitemcard.md#checkoptions) | 否 | 是 | C区（列表右侧）Checkbox元素的配置项。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: CheckOptions)

SuffixCheckbox的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CheckOptions](ui-design-hdslistitemcard.md#checkoptions) | 否 | C区（列表右侧）Checkbox元素的配置项。 |

## SuffixSwitch

PhonePC/2in1TabletTVWearable

SuffixSwitch继承自父类[SuffixItem](ui-design-hdslistitemcard.md#suffixitem)，C区（列表右侧）Switch元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [CheckOptions](ui-design-hdslistitemcard.md#checkoptions) | 否 | 是 | C区（列表右侧）Switch元素的配置项。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: CheckOptions)

SuffixSwitch的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CheckOptions](ui-design-hdslistitemcard.md#checkoptions) | 否 | C区（列表右侧）Switch元素的配置项。 |

## SuffixArrow

PhonePC/2in1TabletTVWearable

SuffixArrow继承自父类[SuffixItem](ui-design-hdslistitemcard.md#suffixitem)，C区（列表右侧）Arrow元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [ColorOptions](ui-design-hdslistitemcard.md#coloroptions) | 否 | 是 | C区（列表右侧）Arrow元素的配置项。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: ColorOptions)

SuffixArrow的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ColorOptions](ui-design-hdslistitemcard.md#coloroptions) | 否 | C区（列表右侧）Arrow元素的配置项。 |

## SuffixBadge

PhonePC/2in1TabletTVWearable

SuffixBadge继承自父类[SuffixItem](ui-design-hdslistitemcard.md#suffixitem)，C区（列表右侧）Badge元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [BadgeOptions](ui-design-hdslistitemcard.md#badgeoptions) | 否 | 是 | C区（列表右侧）Badge元素的配置项。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: BadgeOptions)

SuffixBadge的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [BadgeOptions](ui-design-hdslistitemcard.md#badgeoptions) | 否 | C区（列表右侧）Badge元素的配置项。 |

## SuffixButton

PhonePC/2in1TabletTVWearable

SuffixButton继承自父类[SuffixItem](ui-design-hdslistitemcard.md#suffixitem)，C区（列表右侧）Button元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [ButtonOptions](ui-design-hdslistitemcard.md#buttonoptions) | 否 | 是 | C区（列表右侧）Button元素的配置项。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: ButtonOptions)

SuffixButton的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ButtonOptions](ui-design-hdslistitemcard.md#buttonoptions) | 否 | C区（列表右侧）Button元素的配置项。 |

## SuffixIcon

PhonePC/2in1TabletTVWearable

SuffixIcon继承自父类[SuffixItem](ui-design-hdslistitemcard.md#suffixitem)，C区（列表右侧）单个Icon元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [SuffixIconOptions](ui-design-hdslistitemcard.md#suffixiconoptions) | 否 | 是 | C区（列表右侧）单个Icon元素的配置项。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: SuffixIconOptions)

SuffixIcon的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SuffixIconOptions](ui-design-hdslistitemcard.md#suffixiconoptions) | 否 | C区（列表右侧）单个Icon元素的配置项。 |

## SuffixSubIcon

PhonePC/2in1TabletTVWearable

SuffixSubIcon继承自父类[SuffixItem](ui-design-hdslistitemcard.md#suffixitem)，C区（列表右侧）两个Icon元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [SuffixIconOptions](ui-design-hdslistitemcard.md#suffixiconoptions) | 否 | 是 | C区（列表右侧）第一个Icon元素的配置项。 |
| subOptions | [SuffixIconOptions](ui-design-hdslistitemcard.md#suffixiconoptions) | 否 | 是 | C区（列表右侧）第二个Icon元素的配置项。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: SuffixIconOptions, subOptions?: SuffixIconOptions)

SuffixSubIcon的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SuffixIconOptions](ui-design-hdslistitemcard.md#suffixiconoptions) | 否 | C区（列表右侧）第一个Icon元素的配置项。 |
| subOptions | [SuffixIconOptions](ui-design-hdslistitemcard.md#suffixiconoptions) | 否 | C区（列表右侧）第二个Icon元素的配置项。 |

## SuffixSelect

PhonePC/2in1TabletTVWearable

SuffixSelect继承自父类[SuffixItem](ui-design-hdslistitemcard.md#suffixitem)，C区（列表右侧）Select元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [SelectStyle](ui-design-hdslistitemcard.md#selectstyle) | 否 | 是 | C区（列表右侧）Select元素的配置项。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: SelectStyle)

SuffixSelect的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SelectStyle](ui-design-hdslistitemcard.md#selectstyle) | 否 | C区（列表右侧）Select的配置项。 |

## SuffixToggleButton

PhonePC/2in1TabletTVWearable

SuffixToggleButton继承自父类[SuffixItem](ui-design-hdslistitemcard.md#suffixitem)，C区（列表右侧）ToggleButton元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [ToggleButtonOptions](ui-design-hdslistitemcard.md#togglebuttonoptions) | 否 | 是 | C区（列表右侧）ToggleButton的配置项。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: ToggleButtonOptions)

SuffixToggleButton的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ToggleButtonOptions](ui-design-hdslistitemcard.md#togglebuttonoptions) | 否 | C区（列表右侧）ToggleButton的配置项。 |

## SuffixBadgeAndArrow

PhonePC/2in1TabletTVWearable

SuffixBadgeAndArrow继承自父类[SuffixItem](ui-design-hdslistitemcard.md#suffixitem)，C区（列表右侧）Badge和Arrow组合元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| badgeOptions | [BadgeOptions](ui-design-hdslistitemcard.md#badgeoptions) | 否 | 是 | C区（列表右侧）Badge和Arrow组合元素中Badge的配置项。 |
| arrowOptions | [ColorOptions](ui-design-hdslistitemcard.md#coloroptions) | 否 | 是 | C区（列表右侧）Badge和Arrow组合元素中Arrow的配置项。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(badgeOptions?: BadgeOptions, arrowOptions?: ColorOptions)

SuffixBadgeAndArrow的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| badgeOptions | [BadgeOptions](ui-design-hdslistitemcard.md#badgeoptions) | 否 | C区（列表右侧）Badge和Arrow组合元素中Badge的配置项。 |
| arrowOptions | [ColorOptions](ui-design-hdslistitemcard.md#coloroptions) | 否 | C区（列表右侧）Badge和Arrow组合元素中Arrow的配置项。 |

## SuffixTextAndArrow

PhonePC/2in1TabletTVWearable

SuffixTextAndArrow继承自父类[SuffixItem](ui-design-hdslistitemcard.md#suffixitem)，C区（列表右侧）Text和Arrow组合元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| textOptions | [TextOptions](ui-design-hdslistitemcard.md#textoptions) | 否 | 是 | C区（列表右侧）Text和Arrow组合元素中Text的配置项。 |
| arrowOptions | [ColorOptions](ui-design-hdslistitemcard.md#coloroptions) | 否 | 是 | C区（列表右侧）Text和Arrow组合元素中Arrow的配置项 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(textOptions?: TextOptions, arrowOptions?: ColorOptions)

SuffixTextAndArrow的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| textOptions | [TextOptions](ui-design-hdslistitemcard.md#textoptions) | 否 | C区（列表右侧）Text和Arrow组合元素中Text的配置项。 |
| arrowOptions | [ColorOptions](ui-design-hdslistitemcard.md#coloroptions) | 否 | C区（列表右侧）Text和Arrow组合元素中Arrow的配置项。 |

## SuffixArrowIconText

PhonePC/2in1TabletTVWearable

SuffixArrowIconText继承自父类[SuffixItem](ui-design-hdslistitemcard.md#suffixitem)，C区（列表右侧）Arrow、Text和Arrow组合元素。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [SuffixArrowIconTextOptions](ui-design-hdslistitemcard.md#suffixarrowicontextoptions) | 否 | 是 | C区（列表右侧）Text、Arrow和Icon组合元素的配置项。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: SuffixArrowIconTextOptions)

SuffixArrowIconText的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SuffixArrowIconTextOptions](ui-design-hdslistitemcard.md#suffixarrowicontextoptions) | 否 | C区（列表右侧）Text、Arrow和Icon组合元素的配置项。 |

## SuffixCustomBuilder

PhonePC/2in1TabletTVWearable

SuffixCustomBuilder继承自父类[SuffixItem](ui-design-hdslistitemcard.md#suffixitem)，C区（列表右侧）自定义内容。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| customBuilder | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 是 | C区（列表右侧）自定义内容。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(customBuilder?: CustomBuilder)

SuffixCustomBuilder的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| customBuilder | [CustomBuilder](ts-types.md#custombuilder8) | 否 | C区（列表右侧）自定义内容。 |

## HdsListItemCardOptions

PhonePC/2in1TabletTVWearable

HdsListItemCard列表项内元素配置选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**设备行为异常：** 该接口在TV中与ux规范不一致（获焦态和悬停态组件未放大，获焦态背板颜色未变化，Button内部的text默认颜色等），在其他设备类型中可正常使用。

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| prefixItem | [PrefixItem](ui-design-hdslistitemcard.md#prefixitem) | 否 | 是 | HdsListItemCard列表项的A区（左侧）元素。 |
| textItem | [TextItemOptions](ui-design-hdslistitemcard.md#textitemoptions) | 否 | 是 | HdsListItemCard列表项的B区（中间）元素。 |
| suffixItem | [SuffixItem](ui-design-hdslistitemcard.md#suffixitem) | 否 | 是 | HdsListItemCard列表项的C区（右侧）元素。 |
| onClick | [OnClickCallback](ui-design-hdslistitemcard.md#onclickcallback) | 否 | 是 | HdsListItemCard列表项的点击回调。 |
| cardHeight | [Dimension](ts-types.md#dimension10) | 否 | 是 | HdsListItemCard列表项的高度，目前不支持使用Percentage设置。 |
| cardWidth | [Dimension](ts-types.md#dimension10) | 否 | 是 | HdsListItemCard列表项的宽度，目前不支持使用Percentage设置。 |
| cardBackgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | HdsListItemCard列表项的背景颜色。 |
| cardBorderRadius | [Dimension](ts-types.md#dimension10) | 否 | 是 | HdsListItemCard列表项的边框圆角。 |
| cardPrefixMargin | [Dimension](ts-types.md#dimension10) | 否 | 是 | HdsListItemCard列表项距离屏幕左侧的边距。 |
| cardSuffixMargin | [Dimension](ts-types.md#dimension10) | 否 | 是 | HdsListItemCard列表项距离屏幕右侧的边距。 |
| hoverBorderRadius | [Dimension](ts-types.md#dimension10) | 否 | 是 | HdsListItemCard列表项在悬浮状态下的边框圆角。 |
| enable | boolean | 否 | 是 | HdsListItemCard列表项是否被启用。  true：列表项被启用。  false：列表项被禁用。  默认值：true。 |
| cardId | string | 否 | 是 | HdsListItemCard列表项的Id。 |
| accessibilityOptions | [AccessibilityOptions](ui-design-hdslistitemcard.md#accessibilityoptions) | 否 | 是 | HdsListItemCard列表项的无障碍播放能力选项。 |

说明

从6.1.0(23)开始，若同时满足如下两个条件，焦点将默认组合聚焦播报：

1. HdsListItemCard上未定义accessibilityOptions和onClick事件。
2. 列表项A区（左侧）和C区（右侧）仅有一个可点击事件。

该功能是通过修改accessibilityOptions中isGroup， stateControllerId，actionControllerId的值来实现的，其中isGroup的值会被修改为true，stateControllerId和actionControllerId的值会被修改为可点击子组件的id。

## TextItemOptions

PhonePC/2in1TabletTVWearable

HdsListItemCard列表项的B区（列表中间）元素配置选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| primaryText | [TextOptions](ui-design-hdslistitemcard.md#textoptions) | 否 | 是 | B区（列表中间）元素的标题内容。 |
| primaryPrefixSymbol | [TextSymbolGlyphOptions](ui-design-hdslistitemcard.md#textsymbolglyphoptions) | 否 | 是 | 标题内容左侧第一个Symbol图标。 |
| primarySuffixSymbol | [TextSymbolGlyphOptions](ui-design-hdslistitemcard.md#textsymbolglyphoptions) | 否 | 是 | 标题内容右侧第一个Symbol图标。 |
| primaryPrefixSubSymbol | [TextSymbolGlyphOptions](ui-design-hdslistitemcard.md#textsymbolglyphoptions) | 否 | 是 | 标题内容左侧Symbol第二个图标，仅在左侧第一个Symbol图标存在时才显示。 |
| primarySuffixSubSymbol | [TextSymbolGlyphOptions](ui-design-hdslistitemcard.md#textsymbolglyphoptions) | 否 | 是 | 标题内容右侧Symbol第二个图标，仅在右侧第一个Symbol图标存在时才显示。 |
| secondaryText | [TextOptions](ui-design-hdslistitemcard.md#textoptions) | 否 | 是 | B区（列表中间）元素的副标题内容。 |
| secondaryPrefixSymbol | [TextSymbolGlyphOptions](ui-design-hdslistitemcard.md#textsymbolglyphoptions) | 否 | 是 | 副标题内容左侧第一个Symbol图标。 |
| secondarySuffixSymbol | [TextSymbolGlyphOptions](ui-design-hdslistitemcard.md#textsymbolglyphoptions) | 否 | 是 | 副标题内容右侧第一个Symbol图标。 |
| secondaryPrefixSubSymbol | [TextSymbolGlyphOptions](ui-design-hdslistitemcard.md#textsymbolglyphoptions) | 否 | 是 | 副标题内容左侧Symbol第二个图标，仅在左侧第一个Symbol图标存在时才显示。 |
| secondarySuffixSubSymbol | [TextSymbolGlyphOptions](ui-design-hdslistitemcard.md#textsymbolglyphoptions) | 否 | 是 | 副标题内容右侧Symbol第二个图标，仅在右侧第一个Symbol图标存在时才显示。 |
| description | [TextOptions](ui-design-hdslistitemcard.md#textoptions) | 否 | 是 | B区（列表中间）元素的描述内容。 |
| descriptionPrefixSymbol | [TextSymbolGlyphOptions](ui-design-hdslistitemcard.md#textsymbolglyphoptions) | 否 | 是 | 描述内容左侧第一个Symbol图标。 |
| descriptionSuffixSymbol | [TextSymbolGlyphOptions](ui-design-hdslistitemcard.md#textsymbolglyphoptions) | 否 | 是 | 描述内容右侧第一个Symbol图标。 |
| descriptionPrefixSubSymbol | [TextSymbolGlyphOptions](ui-design-hdslistitemcard.md#textsymbolglyphoptions) | 否 | 是 | 描述内容左侧Symbol第二个图标，仅在左侧第一个Symbol图标存在时才显示。 |
| descriptionSuffixSubSymbol | [TextSymbolGlyphOptions](ui-design-hdslistitemcard.md#textsymbolglyphoptions) | 否 | 是 | 描述内容右侧Symbol第二个图标，仅在右侧第一个Symbol图标存在时才显示。 |
| accessibilityOptions | [AccessibilityOptions](ui-design-hdslistitemcard.md#accessibilityoptions) | 否 | 是 | B区（列表中间）元素的无障碍播放能力选项。  **起始版本：** 6.1.0(23) |
| customBuilder | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 是 | B区（列表中间）自定义内容。 |

说明

TextItemOptions中customBuilder优先级高于其它接口。

## AccessibilityOptions

PhonePC/2in1TabletTVWearable

HdsListItemCard无障碍播放能力选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| accessibilityText | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 列表的无障碍文本属性。当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。  默认值：""。 |
| accessibilityDescription | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 列表的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。  默认值：类型为switch时，默认值为"单指双击即可开启/关闭"，类型为checkbox时，默认值为"单指双击即可选中/取消选中"，其它类型默认值为"单指双击即可执行"。 |
| accessibilityLevel | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 无障碍重要性，用于控制当前项是否可被无障碍辅助服务所识别。  支持的值为：  "auto"：当前组件会转换"yes"。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"。 |
| accessibilityGroup | [AccessibilityGroupOptions](ui-design-hdslistitemcard.md#accessibilitygroupoptions) | 否 | 是 | 是否作为群组响应无障碍操作。启用无障碍分组后，组件及其子组件作为一整个可选组件，无障碍服务不再关注子组件内容。  **起始版本：** 6.1.0(23) |
| accessibilityChecked | boolean | 否 | 是 | 设置无障碍节点是否选中。用于支持多选的情况使用，表示组件是否被选中。此接口只影响屏幕朗读场景下的组件状态播报信息。  true：当前组件被选中。  false：当前组件未被选中。  undefined：由组件自行确定选中状态。  默认值：undefined  **起始版本：** 6.1.0(23) |
| accessibilitySelected | boolean | 否 | 是 | 设置无障碍节点是否选中。用于支持单选的情况使用，表示组件是否被选中。此接口只影响屏幕朗读场景下的组件状态播报信息。  true：当前组件被选中。  false：当前组件未被选中。  undefined：由组件自行确定选中状态。  默认值：undefined  **起始版本：** 6.1.0(23) |
| accessibilityRole | [AccessibilityRoleType](ts-universal-attributes-accessibility.md#accessibilityroletype18枚举说明) | 否 | 是 | 设置无障碍节点的组件类型。特定组件类型有特定的朗读方式，可以根据应用诉求，修改组件类型，用于控制无障碍模式下对组件的朗读方式和朗读内容。不设置的时候，默认使用节点自身的组件类型。  **起始版本：** 6.1.0(23) |
| onAccessibilityActionIntercept | [AccessibilityActionInterceptCallback](ts-universal-accessibility-event.md#accessibilityactioninterceptcallback20) | 否 | 是 | 注册onAccessibilityActionIntercept回调。该回调会在无障碍控制操作触发前调用，由注册方决定是否拦截该次无障碍动作，对不支持Click的组件注册也无法触发回调。  **起始版本：** 6.1.0(23) |

说明

accessibilityChecked属性代表组件是多选模式，accessibilitySelected属性代表组件是单选模式。组件不能同时存在两种选择模式，会造成无障碍状态冲突，导致屏幕朗读等无障碍辅助应用无法正确识别选中状态。如使用accessibilityChecked设置组件为多选模式（设置为true、false），需要保证未设置accessibilitySelected属性，或已将accessibilitySelected属性值重置为undefined，反之亦然。

## AccessibilityGroupOptions

PhonePC/2in1TabletTVWearable

HdsListItemCard无障碍分组能力选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isGroup | boolean | 否 | 是 | 设置是否启用无障碍分组。  true：表示该组件及其所有子组件为一整个可以选中的组件，无障碍服务将不再关注其子组件内容，会合并子组件的文本与无障碍信息，并将其发送至无障碍服务。  false：表示不启用无障碍分组。  默认值：false。 |
| groupControllerOptions | [AccessibilityGroupControllerOptions](ui-design-hdslistitemcard.md#accessibilitygroupcontrolleroptions) | 否 | 是 | 无障碍分组相关的其他属性，用于进一步控制播报内容。比如accessibilityPreferred可用于控制是否优先拼接无障碍文本进行朗读，stateController和actionController可用于指定特定的子组件进行聚合播报。 |

## AccessibilityGroupControllerOptions

PhonePC/2in1TabletTVWearable

HdsListItemCard无障碍播放能力选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始本：** 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isAccessibilityPreferred | boolean | 否 | 是 | 若accessibilityPreferred设置为true，则深度遍历每个子节点时优先选择该子节点的无障碍文本accessibilityText。  若无障碍文本为空则选择本身Text文本，最终将拼接完成的文本设置给accessibilityText与Text都为空的父节点。  若accessibilityPreferred设置为false，表示不启用此功能。  默认值：false |
| stateControllerRoleType | [AccessibilityRoleType](ts-universal-attributes-accessibility.md#accessibilityroletype18枚举说明) | 否 | 是 | 指定特定类型的子组件。配置[AccessibilityGroupOptions](ui-design-hdslistitemcard.md#accessibilitygroupoptions)的容器组件进行无障碍聚合后，会将该特定类型的子组件的选中状态和状态播报文本作为聚合组件的状态和播报文本。从而聚合屏幕朗读下的状态播报，避免需要对子组件单独进行聚焦。  **说明：**  如果聚合组件内有多个相同类型的子组件，则以组件树上该聚合组件下的第一个查找到的子组件为控制组件。  不支持跨进程嵌入式组件内的特定类型，例如：卡片、EmbededUiextension。  默认值：无指定组件 |
| stateControllerId | string | 否 | 是 | 指定特定[唯一标识ID](ts-universal-attributes-component-id.md#id)的子组件。配置[AccessibilityGroupOptions](ui-design-hdslistitemcard.md#accessibilitygroupoptions)的容器组件进行无障碍聚合后，会将该特定标识的子组件的选中状态和状态播报文本作为聚合组件的状态和播报文本。从而聚合屏幕朗读下的状态播报，避免需要对子组件单独进行聚焦。  **说明：**  如果聚合组件内有多个相同类型的子组件，则以组件树上该聚合组件下的第一个查找到的子组件为控制组件。  如果与stateControllerRoleType同时配置，则优先匹配ID一致的组件。  不支持跨进程嵌入式组件内的特定类型，例如：卡片、EmbededUiextension。  默认值：无指定组件 |
| actionControllerRoleType | [AccessibilityRoleType](ts-universal-attributes-accessibility.md#accessibilityroletype18枚举说明) | 否 | 是 | 指定特定类型的子组件。配置[AccessibilityGroupOptions](ui-design-hdslistitemcard.md#accessibilitygroupoptions)的容器组件进行无障碍聚合后，如果触发无障碍的控制操作时，会将操作转发给该特定类型的子组件。从而聚合屏幕朗读下的点击事件，避免需要对子组件单独进行聚焦。  **说明：**  如果聚合组件内有多个相同类型的子组件，则以组件树上该聚合组件下的第一个查找到的子组件为控制组件。  当前只支持无障碍点击操作。  不支持跨进程嵌入式组件内的特定类型，例如：卡片、EmbededUiextension。  默认值：无指定组件 |
| actionControllerId | string | 否 | 是 | 指定特定[唯一标识ID](ts-universal-attributes-component-id.md#id)的子组件。配置[AccessibilityGroupOptions](ui-design-hdslistitemcard.md#accessibilitygroupoptions)的容器组件进行无障碍聚合后，如果触发无障碍的控制操作时，会将操作转发给该特定标识的子组件。从而聚合屏幕朗读下的点击事件，避免需要对子组件单独进行聚焦。  **说明：**  如果聚合组件内有多个相同类型的子组件，则以组件树上该聚合组件下的第一个查找到的子组件为控制组件。  当前只支持无障碍点击操作。  如果与actionControllerRoleType同时配置，则优先匹配ID一致的组件。  不支持跨进程嵌入式组件内的特定类型，例如：卡片、EmbededUiextension。  默认值：无指定组件 |

## ImageOptions

PhonePC/2in1TabletTVWearable

HdsListItemCard中Image样式选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| image | [ImageType](ui-design-hdslistitemcard.md#imagetype) | 否 | 是 | Image资源类型。 |
| modifier | [ImageModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | Image属性样式修改器。 |

## ImageClickOptions

PhonePC/2in1TabletTVWearable

HdsListItemCard中支持点击的Image样式选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| image | [ImageType](ui-design-hdslistitemcard.md#imagetype) | 否 | 是 | Image资源类型。 |
| modifier | [ImageModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | Image属性样式修改器。 |
| onClick | [OnClickCallback](ui-design-hdslistitemcard.md#onclickcallback) | 否 | 是 | Image的点击回调。 |
| enable | boolean | 否 | 是 | Image是否被启用。  true：Image被启用。  false：Image被禁用。  默认值：true。 |
| accessibilityOptions | [AccessibilityOptions](ui-design-hdslistitemcard.md#accessibilityoptions) | 否 | 是 | Image的无障碍播放能力选项。 |

## SymbolGlyphOptions

PhonePC/2in1TabletTVWearable

HdsListItemCard中Symbol样式选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| symbol | [SymbolType](ui-design-hdslistitemcard.md#symboltype) | 否 | 是 | Symbol资源类型。 |

## TextSymbolGlyphOptions

PhonePC/2in1TabletTVWearable

HdsListItemCard中B区（列表中间）Text左右两侧的Symbol样式选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| symbol | [SymbolType](ui-design-hdslistitemcard.md#symboltype) | 否 | 是 | B区（列表中间）Text左右两侧Symbol资源类型。 |
| onClick | [OnClickCallback](ui-design-hdslistitemcard.md#onclickcallback) | 否 | 是 | B区（列表中间）Text左右两侧Symbol的点击回调。 |
| enable | boolean | 否 | 是 | B区（列表中间）Text左右两侧Symbol是否被启用。  true：B区（列表中间）Text左右两侧Symbol被启用。  false：B区（列表中间）Text左右两侧Symbol被禁用。  默认值：true。 |
| accessibilityOptions | [AccessibilityOptions](ui-design-hdslistitemcard.md#accessibilityoptions) | 否 | 是 | B区（列表中间）Text左右两侧Symbol的无障碍播放能力选项。 |

## PrefixIconOptions

PhonePC/2in1TabletTVWearable

HdsListItemCard中A区（列表左侧）Icon样式选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| iconSize | [IconSize](ui-design-hdslistitemcard.md#iconsize) | 否 | 是 | A区（列表左侧）Icon样式。  默认值：[IconSize](ui-design-hdslistitemcard.md#iconsize).SYSTEM\_ICON。 |
| iconValue | [PrefixIconType](ui-design-hdslistitemcard.md#prefixicontype) | 否 | 是 | A区（列表左侧）Icon资源类型。 |

## BadgeOptions

PhonePC/2in1TabletTVWearable

HdsListItemCard中Badge样式选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| badgeValue | number | 否 | 是 | 设置提醒信息数，大于99时，显示“99+”。  默认值：-1。  设置为小于0时，不显示信息标记。 |
| badgeColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | Badge背板颜色。  显示信息标记时默认值：$r('sys.color.warning')。  不显示信息标记时默认值：$r('sys.color.comp\_background\_emphasize')。 |
| textColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | Badge中数字颜色。  默认值：$r('sys.color.font\_on\_primary')。 |
| badgeId | string | 否 | 是 | Badge的Id。 |

## CheckOptions

PhonePC/2in1TabletTVWearable

HdsListItemCard中选择类元素样式选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isCheck | boolean | 否 | 是 | 选择类元素的初始选中状态。  true：元素被选中。  false：元素未被选中。  默认值：false。 |
| selectColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 选择类元素被选中后的背板颜色。 |
| onChange | [OnChangeCallback](ui-design-hdslistitemcard.md#onchangecallback) | 否 | 是 | 选择类元素的onChange回调。 |
| onClick | [OnClickCallback](ui-design-hdslistitemcard.md#onclickcallback) | 否 | 是 | 选择类元素的点击事件回调。 |
| enable | boolean | 否 | 是 | 选择类元素是否被启用。  true：选择类元素被启用。  false：选择类元素被禁用。  默认值：true。 |
| checkId | string | 否 | 是 | 选择类元素的Id。 |
| accessibilityOptions | [AccessibilityOptions](ui-design-hdslistitemcard.md#accessibilityoptions) | 否 | 是 | 选择类元素的无障碍播放能力选项。 |

## ToggleButtonOptions

PhonePC/2in1TabletTVWearable

HdsListItemCard中ToggleButton样式选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isCheck | boolean | 否 | 是 | ToggleButton的初始选中状态。  true：元素被选中。  false：元素未被选中。  默认值：false。 |
| iconValue | [SymbolType](ui-design-hdslistitemcard.md#symboltype) | 否 | 是 | ToggleButton内部图标的Symbol资源。 |
| selectColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | ToggleButton被选中后的背板颜色。  默认值：#00000000。 |
| onChange | [OnChangeCallback](ui-design-hdslistitemcard.md#onchangecallback) | 否 | 是 | ToggleButton的onChange回调。 |
| enable | boolean | 否 | 是 | ToggleButton是否被启用。  true：ToggleButton被启用。  false：ToggleButton被禁用。  默认值：true。 |
| toggleButtonId | string | 否 | 是 | ToggleButton的Id。 |
| accessibilityOptions | [AccessibilityOptions](ui-design-hdslistitemcard.md#accessibilityoptions) | 否 | 是 | ToggleButton的无障碍播放能力选项。 |

## TextOptions

PhonePC/2in1TabletTVWearable

HdsListItemCard中Text样式选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | Text资源类型。 |
| modifier | [TextModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | Text属性样式修改器。 |

## ColorOptions

PhonePC/2in1TabletTVWearable

HdsListItemCard中Color样式选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 对应元素的颜色修改。 |
| componentId | string | 否 | 是 | 对应元素的Id。 |

## ButtonOptions

PhonePC/2in1TabletTVWearable

HdsListItemCard中Button样式选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**设备行为异常：** 该接口在TV中与ux规范不一致（获焦态和悬停态组件未放大，获焦态背板颜色未变化，Button内部的text默认颜色等），在其他设备类型中可正常使用。

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | Button内部的text文本内容。 |
| textColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | Button内部的text文本颜色。  TV上默认值为$r('sys.color.font\_primary')，其他设备上默认值为$r('sys.color.font\_emphasize')。 |
| onClick | [OnClickCallback](ui-design-hdslistitemcard.md#onclickcallback) | 否 | 是 | Button的点击回调。 |
| enable | boolean | 否 | 是 | Button是否被启用。  true：Button被启用。  false：Button被禁用。  默认值：true。 |
| buttonId | string | 否 | 是 | Button的Id。 |
| accessibilityOptions | [AccessibilityOptions](ui-design-hdslistitemcard.md#accessibilityoptions) | 否 | 是 | Button的无障碍播放能力选项。 |

## SuffixIconOptions

PhonePC/2in1TabletTVWearable

HdsListItemCard中C区（列表右侧）Icon样式选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| iconValue | [PrefixIconType](ui-design-hdslistitemcard.md#prefixicontype) | 否 | 是 | C区（列表右侧）Icon的图标资源。 |
| onClick | [OnClickCallback](ui-design-hdslistitemcard.md#onclickcallback) | 否 | 是 | C区（列表右侧）Icon的点击回调。 |
| enable | boolean | 否 | 是 | C区（列表右侧）Icon是否被启用。  true：C区（列表右侧）Icon被启用。  false：C区（列表右侧）Icon被禁用。  默认值：true。 |
| accessibilityOptions | [AccessibilityOptions](ui-design-hdslistitemcard.md#accessibilityoptions) | 否 | 是 | C区（列表右侧）Icon的无障碍播放能力选项。 |

## SuffixArrowIconTextOptions

PhonePC/2in1TabletTVWearable

HdsListItemCard中C区（列表右侧）箭头图标文本选项 。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| startArrow | [SuffixArrowIconOptions](ui-design-hdslistitemcard.md#suffixarrowiconoptions) | 否 | 是 | C区（列表右侧）起始箭头的选项。 |
| text | [TextOptions](ui-design-hdslistitemcard.md#textoptions) | 否 | 是 | C区（列表右侧）文本选项。 |
| endArrow | [SuffixArrowIconOptions](ui-design-hdslistitemcard.md#suffixarrowiconoptions) | 否 | 是 | C区（列表右侧）结束箭头的选项。 |

## SuffixArrowIconOptions

PhonePC/2in1TabletTVWearable

HdsListItemCard中C区（列表右侧）箭头图标选项 。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| arrowColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | C区（列表右侧）箭头的颜色。 |
| onClick | [OnClickCallback](ui-design-hdslistitemcard.md#onclickcallback) | 否 | 是 | C区（列表右侧）箭头的点击回调。 |
| arrowId | string | 否 | 是 | C区（列表右侧）箭头的ID。 |
| enable | boolean | 否 | 是 | C区（列表右侧）箭头是否被启用。  true：C区（列表右侧）箭头被启用。  false：C区（列表右侧）箭头被禁用。  默认值：true。 |
| accessibilityOptions | [AccessibilityOptions](ui-design-hdslistitemcard.md#accessibilityoptions) | 否 | 是 | C区（列表右侧）箭头的无障碍播放能力选项。 |

## SelectStyle

PhonePC/2in1TabletTVWearable

HdsListItemCard中下拉按钮样式选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 下拉按钮本身的文本内容。 |
| valueColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 下拉按钮本身的文本颜色。  默认值：$r('sys.color.font\_secondary')。 |
| arrowColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 下拉按钮箭头的颜色。  默认值：$r('sys.color.icon\_secondary')。 |
| optionValues | Array<[ResourceStr](ts-types.md#resourcestr)> | 否 | 否 | 下拉选项内容。 |
| optionSymbol | Array<[SymbolGlyphModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier)> | 否 | 否 | 下拉选项Symbol图片。 |
| onSelect | [OnSelectCallback](ui-design-hdslistitemcard.md#onselectcallback) | 否 | 是 | 下拉菜单选中某一项的回调。 |
| showDefaultSelectedIcon | boolean | 否 | 是 | 是否显示默认选定的图标。  true：显示默认选定的图标。  false：不显示默认选定的图标。  默认值：false。 |
| enable | boolean | 否 | 是 | 下拉按钮是否被启用。  true：下拉按钮被启用。  false：下拉按钮被禁用。  默认值：true。 |
| selectId | string | 否 | 是 | 下拉按钮的Id。 |
| accessibilityOptions | [AccessibilityOptions](ui-design-hdslistitemcard.md#accessibilityoptions) | 否 | 是 | 下拉按钮的无障碍播放能力选项。 |
| selected | number | 否 | 是 | 设置下拉菜单初始选项的索引，第一项的索引为0。当不设置selected属性或设置为异常值时，默认选中值为-1，菜单项不选中。  默认值：-1。  **起始版本：** 6.1.0(23) |

## SymbolType

PhonePC/2in1TabletTVWearable

type SymbolType= ResourceStr | SymbolGlyphModifier

HdsListItemCard中支持Symbol图标资源类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ResourceStr](ts-types.md#resourcestr) | 字符串类型。 |
| [SymbolGlyphModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | SymbolGlyph属性样式修改器。 |

## PrefixIconType

PhonePC/2in1TabletTVWearable

type PrefixIconType= ImageOptions | SymbolGlyphOptions

HdsListItemCard中支持A区（列表左侧）Icon图标资源类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageOptions](ui-design-hdslistitemcard.md#accessibilitygroupoptions) | Image类型。 |
| [SymbolGlyphOptions](ui-design-hdslistitemcard.md#symbolglyphoptions) | SymbolGlyph类型。 |

## ImageType

PhonePC/2in1TabletTVWearable

type ImageType = ResourceStr | image.PixelMap

HdsListItemCard中支持Image资源类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ResourceStr](ts-types.md#resourcestr) | 字符串类型。 |
| image.[PixelMap](arkts-apis-image-pixelmap.md) | PixelMap类型。 |

## IconSize

PhonePC/2in1TabletTVWearable

PrefixIcon图标大小枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SMALL\_ICON | 1 | A区（列表左侧）Icon图标类型：小图标类型，大小为16vp \* 16vp（穿戴设备上为28vp\*28vp）。 |
| SYSTEM\_ICON | 2 | A区（列表左侧）Icon图标类型：系统图标类型，大小为24vp \* 24vp（穿戴设备上为32vp\*32vp）。 |

说明

上述描述中所有左侧、中间、右侧均是在LTR模式下。

## OnClickCallback

PhonePC/2in1TabletTVWearable

type OnClickCallback = () => void

HdsListItemCard中的点击事件回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

## OnChangeCallback

PhonePC/2in1TabletTVWearable

type OnChangeCallback = (isOn: boolean) => void

HdsListItemCard中的onChange事件回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isOn | boolean | 是 | HdsListItemCard中的Switch/CheckBox/Radio/ToggleButton选中状态。  - isOn为true时，表示从未选中变为选中。  - isOn为false时，表示从选中变为未选中。 |

## OnSelectCallback

PhonePC/2in1TabletTVWearable

type OnSelectCallback = (index: number, text: string) => void

HdsListItemCard中的onSelect事件回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Full

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 选中项的索引，取值范围大于等于0。 |
| text | string | 是 | 选中项的值，无位数要求。 |

## HdsListItemCardModifier

PhonePC/2in1TabletTV

动态设置HdsListItemCard组件的属性和样式，继承自[HdsListItemCardAttribute](ui-design-hdslistitemcard.md#属性)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.1.0(23)

### applyNormalAttribute

PhonePC/2in1TabletTV

applyNormalAttribute?(instance: HdsListItemCardAttribute): void

组件普通状态时的样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instance | [HdsListItemCardAttribute](ui-design-hdslistitemcard.md#属性) | 是 | 动态设置HdsListItemCard组件的属性。 |

## 示例

PhonePC/2in1TabletTVWearable

以设置简单的列表项为例

```
1. import {
2. HdsListItemCard,
3. IconSize,
4. PrefixImage,
5. PrefixIcon,
6. SuffixIcon,
7. SuffixSwitch,
8. SuffixBadgeAndArrow
9. } from '@kit.UIDesignKit';
10. import { promptAction, ImageModifier, TextModifier } from '@kit.ArkUI';

12. @Entry
13. @Component
14. struct HdsListItemCardExample {
15. private scroller: ListScroller = new ListScroller();

17. build() {
18. Column() {
19. List({ space: 5, scroller: this.scroller }) {
20. ListItem() {
21. HdsListItemCard({
22. prefixItem: new PrefixIcon({
23. iconSize: IconSize.SYSTEM_ICON,
24. iconValue: {
25. image: $r('app.media.startIcon')
26. },
27. }),
28. textItem: {
29. primaryText: {
30. text: 'Primary Text'
31. },
32. secondaryText: {
33. text: 'Secondary Text'
34. },
35. description: {
36. text: 'Description Text'
37. },
38. },
39. suffixItem: new SuffixIcon({
40. iconValue: {
41. symbol: $r('sys.symbol.circle_dashed')
42. },
43. onClick: () => {
44. promptAction.openToast({ message: 'onclick icon' });
45. }
46. }),
47. onClick: () => {
48. promptAction.openToast({ message: 'onclick hdslistitem' });
49. },
50. })
51. }

53. ListItem() {
54. HdsListItemCard({
55. prefixItem: new PrefixImage({
56. image: $r('app.media.startIcon'),
57. modifier: new ImageModifier().width(70).height(70).borderRadius(20)
58. }),
59. textItem: {
60. primaryText: {
61. text: 'Primary Text'
62. },
63. secondaryText: {
64. text: 'Secondary Text'
65. },
66. description: {
67. text: 'Description Text'
68. },
69. },
70. suffixItem: new SuffixSwitch({
71. isCheck: false,
72. selectColor: Color.Orange,
73. onChange: (num: boolean) => {
74. if (num) {
75. promptAction.openToast({ message: 'switch is true' });
76. } else {
77. promptAction.openToast({ message: 'switch is false' });
78. }
79. },
80. })
81. })
82. }

84. ListItem() {
85. HdsListItemCard({
86. prefixItem: new PrefixIcon({
87. iconSize: IconSize.SYSTEM_ICON,
88. iconValue: {
89. symbol: $r('sys.symbol.ohos_trash')
90. },
91. }),
92. textItem: {
93. primaryText: {
94. text: 'Primary Text',
95. modifier: new TextModifier().fontColor(Color.Pink),
96. }
97. },
98. suffixItem: new SuffixBadgeAndArrow({
99. badgeValue: 9,
100. badgeColor: Color.Orange,
101. textColor: Color.Blue,
102. }, {
103. color: Color.Orange
104. })
105. })
106. }
107. }
108. .width('100%')
109. .height('100%')
110. .margin(10)
111. }.backgroundColor(0x1a0a59f7).height('100%')
112. }
113. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/ww4kDSKqRdqjtdrWMKMauQ/zh-cn_image_0000002552800882.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000641Z&HW-CC-Expire=86400&HW-CC-Sign=A58457037A34F8F4BF4CCA0B171C53322201994A94608AEEF96AF5422EED2C6C)
