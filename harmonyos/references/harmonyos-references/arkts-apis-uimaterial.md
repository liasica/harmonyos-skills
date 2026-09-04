---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uimaterial
title: "@ohos.arkui.uiMaterial (系统材质)"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.uiMaterial (系统材质)
category: harmonyos-references
scraped_at: 2026-09-05T06:16:52+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:47d88521bc20d5a70c4b99d7ed1bc0df23ca58e79f23a8bf62a2dd72fc18da79
---

本模块提供系统材质的接口定义。不同的系统材质对应不同的UI效果，包括背景色[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)、边框颜色[borderColor](ts-universal-attributes-border.md#bordercolor)、边框宽度[borderWidth](ts-universal-attributes-border.md#borderwidth)、阴影[shadow](ts-universal-attributes-image-effect.md#shadow)、材质层滤镜[materialFilter](ts-universal-attributes-filter-effect.md#materialfilter23)效果。当前提供的系统材质为沉浸式材质类型[ImmersiveMaterial](arkts-apis-uimaterial.md#immersivematerial)，沉浸式材质对象在不同设备上的表现存在差异，只有支持沉浸式材质的设备上设置才有效果，在不支持沉浸式材质的设备上可设置但无效果，可通过[isImmersiveMaterialSupported](arkts-apis-uimaterial.md#uimaterialisimmersivematerialsupported)判断设备是否支持沉浸式材质。在支持沉浸式材质的设备上，材质效果在不同算力的设备上有分档表现，可通过[getGlobalMaterialLevel](arkts-apis-uimaterial.md#uimaterialgetglobalmateriallevel)获取设备的材质等级，分档效果具体参考[ImmersiveMaterial](arkts-apis-uimaterial.md#immersivematerial)的描述。

开发指导请参考[沉浸光感](../harmonyos-guides/arkts-immersive-light-sense-overview.md)指南文档。

**起始版本：** 26.0.0

## 导入模块

```ts
import { uiMaterial } from '@kit.ArkUI';
```

## ImmersiveMaterial

沉浸式材质类，继承自[Material](arkts-apis-uimaterial.md#material)。

组件上设置ImmersiveMaterial时，

* 弹窗类组件（AlertDialog、ActionSheet、CustomDialog、CalendarPickerDialog、DatePickerDialog、TimePickerDialog、TextPickerDialog、SelectionMenu、AlphabetIndexer弹窗、Text设置copyOption后长按或双击触发的文本菜单）和弹窗类接口（PromptAction、ArkUI\_NativeDialog、@ohos.promptAction (弹窗)、Popup控制、Tips控制、菜单控制、半模态转场）以及按钮与选择类组件（Slider、Toggle、Select）可在页面内全部区域生效。
* 其他组件仅在Navigation/NavDestination标题栏或横向Tab中barPosition为BarPosition.End的底部TabBar中生效，在其他区域中设置不生效。

沉浸式材质根据设备是否支持沉浸式材质和设备算力有分档表现，可通过[isImmersiveMaterialSupported](arkts-apis-uimaterial.md#uimaterialisimmersivematerialsupported)判断设备是否支持沉浸式材质，通过[getGlobalMaterialLevel](arkts-apis-uimaterial.md#uimaterialgetglobalmateriallevel)获取设备的材质等级。在不支持沉浸式材质的设备上可设置沉浸式材质但无效果。在支持沉浸式材质的高算力和中算力设备上，通过材质层滤镜属性[materialFilter](ts-universal-attributes-filter-effect.md#materialfilter23)和阴影[shadow](ts-universal-attributes-image-effect.md#shadow)属性实现材质效果，当[systemMaterial](ts-universal-attributes-image-effect.md#systemmaterial)属性生效后，已设置的背景色属性[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)会被恢复为透明色，已设置的边框宽度[borderWidth](ts-universal-attributes-border.md#borderwidth)属性会被恢复为无边框效果。在支持沉浸式材质的低算力设备上，通过背景色[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)、边框颜色[borderColor](ts-universal-attributes-border.md#bordercolor)、边框宽度[borderWidth](ts-universal-attributes-border.md#borderwidth)、阴影[shadow](ts-universal-attributes-image-effect.md#shadow)属性实现材质效果。同一材质的效果，会受到系统设置应用中沉浸光感配置项的影响，不同强弱程度的沉浸光感配置下，材质的参数和效果存在差异。

### constructor

constructor(options?: ImmersiveOptions)

ImmersiveMaterial的构造函数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ImmersiveOptions](arkts-apis-uimaterial.md#immersiveoptions) | 否 | 系统材质配置选项，包括材质样式、材质层赋色等。  默认值参考ImmersiveOptions接口各参数的默认值，即{style:uiMaterial.ImmersiveStyle.REGULAR, materialColor:undefined, colorInvert:false, applyShadow:true, interactive:false, lightEffect:undefined}。 |

## Material

系统材质对象基类。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### empty

static get empty(): Material

返回空材质对象，用于组件单独关闭沉浸式系统材质效果。使用方式为uiMaterial.Material.empty。

在ENABLE使能模式下，可通过设置systemMaterial(uiMaterial.Material.empty)来单独关闭某个组件的沉浸式系统材质效果。如果组件未支持组件级沉浸式系统材质接口，则无法通过此方法关闭材质效果。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Material](arkts-apis-uimaterial.md#material) | 返回空材质对象，表示无材质效果。 |

## MaterialType

系统材质类型枚举。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IMMERSIVE | 2 | 沉浸式材质类型。仅用于[MaterialInfo](arkts-apis-uimaterial.md#materialinfo)接口的type属性标识当前配置的材质类型，不映射到底层功能。实际材质效果通过[ImmersiveMaterial](arkts-apis-uimaterial.md#immersivematerial)类实现。 |

## MaterialState

材质使能状态枚举，表示应用级沉浸式系统材质配置的状态。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认模式。[弹出框Dialog](../harmonyos-guides/arkts-base-dialog-overview.md)、[即时反馈（Toast）](../harmonyos-guides/arkts-create-toast.md)、[AlphabetIndexer](ts-container-alphabet-indexer.md)在组件本身未设置背景颜色、模糊参数和阴影参数时默认开启沉浸式系统材质；[Text](ts-basic-components-text.md)设置[copyOption](ts-basic-components-text.md#copyoption9)后长按或双击触发的文本菜单默认开启沉浸式系统材质；其他组件由应用主动设置。 |
| ENABLE | 1 | 使能模式。此模式下，[弹出框Dialog](../harmonyos-guides/arkts-base-dialog-overview.md)、[即时反馈（Toast）](../harmonyos-guides/arkts-create-toast.md)、[AlphabetIndexer](ts-container-alphabet-indexer.md)、[ChipGroup](ohos-arkui-advanced-chipgroup.md)、[Chip](ohos-arkui-advanced-chip.md)、[Select](ts-basic-components-select.md)、[菜单控制](ts-universal-attributes-menu.md)、[Toggle](ts-basic-components-toggle.md)、[SegmentButton](ohos-arkui-advanced-segmentbutton.md)、[SegmentButtonV2](ohos-arkui-advanced-segmentbuttonv2.md)、[Slider](ts-basic-components-slider.md)、[SelectionMenu](ohos-arkui-advanced-selectionmenu.md)默认开启沉浸式系统材质；[Text](ts-basic-components-text.md)设置[copyOption](ts-basic-components-text.md#copyoption9)后长按或双击触发的文本菜单默认开启沉浸式系统材质；[Navigation](ts-basic-components-navigation.md)/[NavDestination](ts-basic-components-navdestination.md)标题栏默认开启沉浸式系统材质；[Tabs](ts-container-tabs.md)设置[barFloatingStyle](ts-container-tabs.md#barfloatingstyle)并生效悬浮样式，页签栏Tabbar默认开启沉浸式系统材质。其他组件需开发者主动设置。此模式下，沉浸式系统材质样式生效的优先级高于组件本身设置的背景色、模糊、阴影和边框样式。 |
| DISABLE | 2 | 禁用模式。所有组件禁止开启沉浸式系统材质，即使主动为组件设置沉浸式系统材质参数也不会生效。 |

## MaterialInfo

材质配置信息，包含材质使能状态和材质类型。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | [MaterialState](arkts-apis-uimaterial.md#materialstate) | 否 | 否 | 材质使能状态配置，决定当前应用沉浸式系统材质的使能模式。不同状态影响组件默认是否开启沉浸式系统材质效果，具体参考[MaterialState](arkts-apis-uimaterial.md#materialstate)枚举说明。 |
| type | [MaterialType](arkts-apis-uimaterial.md#materialtype) | 否 | 否 | 系统材质类型标识，表示当前配置对应的材质类型。该值仅用于类型标识，不映射到底层功能。 |

## uiMaterial.getMaterialInfo

getMaterialInfo(): MaterialInfo

获取当前应用的材质配置信息。在需要根据材质使能状态决定组件是否开启或关闭沉浸式系统材质效果时，可调用此方法获取配置信息。返回的配置信息来自应用在[module.json5](../harmonyos-guides/module-configuration-file.md)中配置的metadata。只有在entry类型的module中配置的metadata才会生效。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MaterialInfo](arkts-apis-uimaterial.md#materialinfo) | 返回当前应用的材质配置信息，包含材质使能状态和材质类型。 |

## ImmersiveStyle

沉浸式材质样式枚举。不同的材质样式对应不同的材质参数，主要包括材质的模糊程度、高光效果等。开发者可根据UI场景需要选择合适的材质样式：悬浮按钮和轻量提示建议使用ULTRA\_THIN或THIN样式，常规内容区域和卡片建议使用REGULAR样式，需要强调层次感或遮挡背景的场景建议使用THICK或ULTRA\_THICK样式。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ULTRA\_THIN | 0 | 超薄样式。材质层超薄，具有很强的透明效果。 |
| THIN | 1 | 薄样式。材质层薄，具有较强的透明效果。 |
| REGULAR | 2 | 常规样式。材质层的厚度常规，具有适度的透明和模糊效果。 |
| THICK | 3 | 厚样式。材质层厚，模糊效果较强。 |
| ULTRA\_THICK | 4 | 超厚样式。材质层超厚，模糊效果很强。 |

## MaterialLevel

材质等级枚举，表示设备的算力等级。可通过[uiMaterial.getGlobalMaterialLevel](arkts-apis-uimaterial.md#uimaterialgetglobalmateriallevel)获取当前设备的材质等级。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EXQUISITE | 0 | 高算力设备的材质等级。 |
| GENTLE | 1 | 中算力设备的材质等级。 |
| SMOOTH | 2 | 低算力设备的材质等级。 |

## uiMaterial.getGlobalMaterialLevel

getGlobalMaterialLevel(): MaterialLevel

获取全局材质等级，与设备算力相关。该配置项由设备定义，不可修改。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MaterialLevel](arkts-apis-uimaterial.md#materiallevel) | 返回设备的材质等级。 |

## uiMaterial.isImmersiveMaterialSupported

isImmersiveMaterialSupported(): boolean

判断当前设备是否支持沉浸式系统材质[ImmersiveMaterial](arkts-apis-uimaterial.md#immersivematerial)。该配置项由设备定义，不可修改。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前设备是否支持ImmersiveMaterial。true表示当前设备支持ImmersiveMaterial，false表示不支持。 |

## LightEffectOptions

沉浸式材质的光感交互反馈配置。光感交互反馈是指组件在用户触摸交互时，材质表面呈现动态光感变化的视觉效果。用于自定义反馈光感的颜色。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 自定义交互反馈光感的颜色。设置后，交互反馈光感将使用该颜色作为显示颜色，替代默认的白色光感效果。  默认值：Color.White |

## ImmersiveOptions

沉浸式材质参数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| style | [ImmersiveStyle](arkts-apis-uimaterial.md#immersivestyle) | 否 | 是 | 材质样式。不同样式对应不同的材质参数，影响材质的厚度。  **说明**：该参数仅对支持沉浸式材质的高算力和中算力设备的显示效果生效。  默认值：uiMaterial.ImmersiveStyle.REGULAR |
| materialColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 材质层赋色。对于支持沉浸式材质的高算力和中算力设备，若不设置该参数或该参数为undefined，不额外混合纯色效果；若设置该参数为有效颜色值，该参数会为材质层滤镜再混合一层纯色效果，若该颜色为纯不透明的颜色，会遮挡材质层滤镜效果。对于支持沉浸式材质的低算力设备，若不设置该参数或该参数为undefined，生效低算力设备材质自带的背景色效果；若设置该参数为有效颜色值，该参数作为背景色[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)属性值。  **说明**：该参数对支持沉浸式材质的所有档位的算力设备的显示效果生效。  默认值：undefined |
| colorInvert | boolean | 否 | 是 | 设置了材质对象的节点的子树是否自动将颜色适配为材质背景色的反色。  若为false，则不会自动反色。  若为true，则当材质样式满足系统定义的反色条件时才会自动反色。具体的使用限制如下：  - 自动反色仅在高算力和中算力设备上生效，低算力设备上设置colorInvert不会产生视觉效果差异。  - 自动反色与系统沉浸光感的强弱配置相关，沉浸式系统材质越薄、沉浸光感越强，越容易符合反色要求。  - 自动反色能力使用硬编码的颜色值（如Color.White、'#FFFFFFFF'）不会触发自动反色，仅对以下属性接口设置特殊资源（见下表1）值时生效：  Text组件的[fontColor](ts-basic-components-text.md#fontcolor)，Button组件的[fontColor](ts-basic-components-button.md#fontcolor)，SymbolGlyph组件的[fontColor](ts-basic-components-symbolglyph.md#fontcolor)，Image组件的[fillColor](ts-basic-components-image.md#fillcolor)，Search组件的[placeholderColor](ts-basic-components-search.md#placeholdercolor)、[fontColor](ts-basic-components-search.md#fontcolor10)，[searchIcon](ts-basic-components-search.md#searchicon10)中的图标颜色、[cancelButton](ts-basic-components-search.md#cancelbutton10)中的图标颜色、[caretStyle](ts-basic-components-search.md#caretstyle10)中的光标颜色，[searchButton](ts-basic-components-search.md#searchbutton) 中的按钮颜色，TabContent组件的[tabBar](ts-container-tabcontent.md#tabbar)属性使用[BottomTabBarStyle](ts-container-tabcontent.md#bottomtabbarstyle9)，Chip组件的[prefixIcon](ohos-arkui-advanced-chip.md#prefixiconoptions)、suffixIcon属性的[fillColor](ohos-arkui-advanced-chip.md#iconcommonoptions)，[label](ohos-arkui-advanced-chip.md#labeloptions)属性的[fontColor](ohos-arkui-advanced-chip.md#labeloptions)，ChipGroup组件的[itemStyle](ohos-arkui-advanced-chipgroup.md#chipitemstyle)的[fontColor](ohos-arkui-advanced-chipgroup.md#chipitemstyle)，TextArea组件的[fontColor](ts-basic-components-textarea.md#fontcolor)、[placeholderColor](ts-basic-components-textarea.md#placeholdercolor)，TextInput组件的[fontColor](ts-basic-components-textinput.md#fontcolor)、[placeholderColor](ts-basic-components-textinput.md#placeholdercolor)，SegmentButton组件的[fontColor](ohos-arkui-advanced-segmentbutton.md#属性-1)，Swiper组件的[fontColor](ts-container-swiper.md#fontcolor)。  默认值：false |
| applyShadow | boolean | 否 | 是 | 是否添加材质的阴影效果。  当该参数为true时，材质中的阴影效果固定生效，优先于[shadow](ts-universal-attributes-image-effect.md#shadow)通用属性。当该参数为false时，shadow通用属性生效，材质的阴影效果不生效。  **说明**：该参数对支持沉浸式材质的所有档位的算力设备的显示效果生效。  默认值：true |
| interactive | boolean | 否 | 是 | 是否启用交互形变效果。交互形变效果是指组件在用户交互时产生形变的视觉反馈效果。  当该参数为true时，启用交互形变效果。当该参数为false时，不启用交互形变效果。  **说明**：该参数对支持沉浸式材质的所有档位的算力设备的显示效果生效。  默认值：false |
| lightEffect | [LightEffectOptions](arkts-apis-uimaterial.md#lighteffectoptions) | null | 否 | 是 | 光感交互反馈效果参数。传入LightEffectOptions对象时启用光感交互反馈；传入null时显式禁用光感交互反馈效果；不传入时默认为undefined，取决于组件是否默认有交互光感效果。  **说明**：该参数仅对支持沉浸式材质的高算力和中算力设备的显示效果生效。  默认值：undefined，不设置光感交互反馈效果。 |

**表1** 特殊资源值对应的深浅色值

| 特殊资源值 | 浅色 | 深色 |
| --- | --- | --- |
| $r('sys.color.brand') | #FF0A59F7 | #FF317AF7 |
| $r('sys.color.brand\_font') | #FF0A59F7 | #FF5291FF |
| $r('sys.color.warning') | #FFE84026 | #FFD94838 |
| $r('sys.color.font\_on\_primary') | #FFFFFFFF | #FFFFFFFF |
| $r('sys.color.font\_primary') | #E5000000 | #E5FFFFFF |
| $r('sys.color.font\_secondary') | #99000000 | #99FFFFFF |
| $r('sys.color.font\_tertiary') | #66000000 | #66FFFFFF |
| $r('sys.color.font\_fourth') | #33000000 | #33FFFFFF |
| $r('sys.color.font\_emphasize') | #FF0A59F7 | #FF5291FF |
| $r('sys.color.icon\_primary') | #E5000000 | #E5FFFFFF |
| $r('sys.color.icon\_secondary') | #99000000 | #99FFFFFF |
| $r('sys.color.icon\_tertiary') | #66000000 | #66FFFFFF |
| $r('sys.color.icon\_fourth') | #33000000 | #33FFFFFF |
| $r('sys.color.icon\_emphasize') | #FF0A59F7 | #FF5291FF |
| $r('sys.color.icon\_sub\_emphasize') | #660A59F7 | #665291FF |
| $r('sys.color.comp\_background\_primary\_contrary') | #FFFFFFFF | #FFE5E5E5 |
| $r('sys.color.comp\_background\_primary\_contrary\_secondary') | #FFFFFFFF | #FF666666 |
| $r('sys.color.comp\_background\_secondary') | #19000000 | #19FFFFFF |
| $r('sys.color.comp\_background\_tertiary') | #0C000000 | #19FFFFFF |
| $r('sys.color.comp\_background\_emphasize') | #FF0A59F7 | #FF317AF7 |
| $r('sys.color.comp\_emphasize\_secondary') | #330A59F7 | #33317AF7 |
| $r('sys.color.comp\_emphasize\_tertiary') | #190A59F7 | #19317AF7 |
| $r('sys.color.comp\_divider') | #33000000 | #33FFFFFF |
| $r('sys.color.interactive\_hover') | #0C000000 | #19FFFFFF |
| $r('sys.color.interactive\_focus') | #FF0A59F7 | #FF317AF7 |
| $r('sys.color.interactive\_pressed') | #19000000 | #26FFFFFF |

## 示例

### 示例1（设置沉浸式系统材质）

本示例介绍如何将沉浸式材质的[ImmersiveMaterial](arkts-apis-uimaterial.md#immersivematerial)对象通过[systemMaterial](ts-universal-attributes-image-effect.md#systemmaterial)属性设置给组件。

从API版本26.0.0开始，新增ImmersiveMaterial对象和systemMaterial属性。

```ts
import { uiMaterial } from '@kit.ArkUI';

@Entry
@Component
struct SystemMaterialPage {
  @State currentStyle: uiMaterial.ImmersiveStyle = uiMaterial.ImmersiveStyle.ULTRA_THIN;
  private styles: uiMaterial.ImmersiveStyle[] = [
    uiMaterial.ImmersiveStyle.ULTRA_THIN,
    uiMaterial.ImmersiveStyle.THIN,
    uiMaterial.ImmersiveStyle.REGULAR,
    uiMaterial.ImmersiveStyle.THICK,
    uiMaterial.ImmersiveStyle.ULTRA_THICK,
  ];

  build() {
    Column() {
      Tabs({ barPosition: BarPosition.End }) {
        TabContent() {
          // $r('app.media.invert')需要替换为开发者所需的图像资源文件
          Image($r('app.media.invert'))
            .width('100%')
            .height('100%')
            .objectFit(ImageFit.Cover)
        }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_icon_mask_svg'), 'ULTRA_THIN')
          .labelStyle({ selectedColor: $r('sys.color.brand'), unselectedColor: $r('sys.color.font_primary') })
          .iconStyle({ selectedColor: $r('sys.color.brand'), unselectedColor: $r('sys.color.font_primary') })
        )

        TabContent() {
          Image($r('app.media.invert'))
            .width('100%')
            .height('100%')
            .objectFit(ImageFit.Cover)
        }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_icon_mask_svg'), 'THIN')
          .labelStyle({ selectedColor: $r('sys.color.brand'), unselectedColor: $r('sys.color.font_primary') })
          .iconStyle({ selectedColor: $r('sys.color.brand'), unselectedColor: $r('sys.color.font_primary') })
        )

        TabContent() {
          Image($r('app.media.invert'))
            .width('100%')
            .height('100%')
            .objectFit(ImageFit.Cover)
        }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_icon_mask_svg'), 'REGULAR')
          .labelStyle({ selectedColor: $r('sys.color.brand'), unselectedColor: $r('sys.color.font_primary') })
          .iconStyle({ selectedColor: $r('sys.color.brand'), unselectedColor: $r('sys.color.font_primary') })
        )

        TabContent() {
          Image($r('app.media.invert'))
            .width('100%')
            .height('100%')
            .objectFit(ImageFit.Cover)
        }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_icon_mask_svg'), 'THICK')
          .labelStyle({ selectedColor: $r('sys.color.brand'), unselectedColor: $r('sys.color.font_primary') })
          .iconStyle({ selectedColor: $r('sys.color.brand'), unselectedColor: $r('sys.color.font_primary') })
        )

        TabContent() {
          Image($r('app.media.invert'))
            .width('100%')
            .height('100%')
            .objectFit(ImageFit.Cover)
        }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_icon_mask_svg'), 'ULTRA_THICK')
          .labelStyle({ selectedColor: $r('sys.color.brand'), unselectedColor: $r('sys.color.font_primary') })
          .iconStyle({ selectedColor: $r('sys.color.brand'), unselectedColor: $r('sys.color.font_primary') })
        )
      }
      .barFloatingStyle({
        systemMaterial: new uiMaterial.ImmersiveMaterial({
          style: this.currentStyle,
        }),
        maskColor: Color.Transparent,
      })
      .barOverlap(true)
      .onChange((index: number) => {
        this.currentStyle = this.styles[index];
      })
      .barWidth(500)
      .height('100%')
    }
    .width('100%')
    .height('100%')
  }
}
```

在支持沉浸式材质的低算力设备上表现：

ULTRA\_THIN样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/2_TuE6WCQ1G6paVR-vSwlg/zh-cn_image_0000002742004727.jpg)

THIN样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/tzTa2r_QSbmwHOFSr059AA/zh-cn_image_0000002712405738.jpg)

REGULAR样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/S1l5pbLeSu6lK10UWKSpqA/zh-cn_image_0000002742124687.jpg)

THICK样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/TP9rYOUUSjykK8DsBZ0vqQ/zh-cn_image_0000002712245780.jpg)

ULTRA\_THICK样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/ApBo5HrkTAu3UefqEEGoSQ/zh-cn_image_0000002742004729.jpg)

在支持沉浸式材质的中算力设备上表现：

ULTRA\_THIN样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/Sj8aVREkR66J2K3xGs-FJg/zh-cn_image_0000002712405740.jpg)

THIN样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/kpIX9AG0TPuprNy6nI7Row/zh-cn_image_0000002742124689.jpg)

REGULAR样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/C1pHIvpyQVCWGKgCZObxEA/zh-cn_image_0000002712245782.jpg)

THICK样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/XNhRqQOnRV6E7nC4yvKtAw/zh-cn_image_0000002742004731.jpg)

ULTRA\_THICK样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/O7gcVDnkS46nMJy1kh_ZTA/zh-cn_image_0000002712405742.jpg)

在支持沉浸式材质的高算力设备上表现：

ULTRA\_THIN样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/AxDuCkKeTL6GIKMIzBFz4g/zh-cn_image_0000002742124691.jpg)

THIN样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/vOD-IzwcSkeqT93QEgrHTA/zh-cn_image_0000002712245784.jpg)

REGULAR样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/AkNfJtZ6QUqj6DbdSUFroQ/zh-cn_image_0000002742004733.jpg)

THICK样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/14oIFDwNQDu0M7yWvPXL_w/zh-cn_image_0000002712405744.jpg)

ULTRA\_THICK样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/a_pZa7EuSXOuacCNyKaKEQ/zh-cn_image_0000002742124693.jpg)

### 示例2（获取材质配置信息并使用空材质关闭沉浸式系统材质）

本示例介绍如何通过[uiMaterial.getMaterialInfo](arkts-apis-uimaterial.md#uimaterialgetmaterialinfo)获取当前应用的材质配置信息，并根据配置状态使用[empty](arkts-apis-uimaterial.md#empty)关闭特定组件的沉浸式系统材质效果。

从API版本26.0.0开始，新增uiMaterial.getMaterialInfo方法和empty方法。

首先在[module.json5](../harmonyos-guides/module-configuration-file.md)文件中配置开关信息，需注意只有在entry类型的module中配置才会生效。

```json5
{
  "module": {
    // ···
    "type": "entry", // 需注意只有在entry类型的module中配置才会生效。
    // ···
    "metadata": [{
      "name": "ohos.arkui.UIMaterial.state",
      "value": "enable"
    }],
    // ···
  }
}
```

然后按照如下内容编写示例代码。

```ts
import { uiMaterial } from '@kit.ArkUI';

@Entry
@Component
struct MaterialInfoPage {
  // 获取材质配置信息
  private info: uiMaterial.MaterialInfo = uiMaterial.getMaterialInfo();

  build() {
    Column() {
      Column({ space: 20 }) {
        Column() {
          Text(`MaterialState: ${this.info.state}`)
            .fontSize(16)
          Text(`MaterialType: ${this.info.type}`)
            .fontSize(16)
        }
        .backgroundColor(Color.White)
        .padding(15)

        // 根据状态决定组件行为
        if (this.info.state === uiMaterial.MaterialState.ENABLE) {
          // Toggle组件默认开启沉浸式系统材质
          Toggle({ type: ToggleType.Switch })
            .width(100)
            .height(50)
          // 单独关闭Toggle组件的沉浸式系统材质
          Toggle({ type: ToggleType.Switch })
            .width(100)
            .height(50)
            .systemMaterial(uiMaterial.Material.empty)
        }
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
      // $r('app.media.img')需要替换为开发者所需的图像资源文件
      .backgroundImage($r('app.media.img'))

    }.width('100%').height('100%')
  }
}
```

在支持沉浸式材质的高算力设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/SwYfm0rFRiyqXUCXSqcEzg/zh-cn_image_0000002712245786.jpg)

在支持沉浸式材质的中算力设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/4wTAmeyPQxSGIbs4GZhtyw/zh-cn_image_0000002742004735.jpg)

在支持沉浸式材质的低算力设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/26Rc4xCHRSyzgwhxSVkXdQ/zh-cn_image_0000002712405746.jpg)

### 示例3（设置组件材质的交互形变效果）

本示例介绍如何通过[ImmersiveOptions](arkts-apis-uimaterial.md#immersiveoptions)中的interactive接口使组件实现交互形变效果。

从API版本26.0.0开始，新增interactive接口。

```ts
import { uiMaterial } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Tabs({ barPosition: BarPosition.End }) {
        TabContent() {
          // $r('app.media.invert')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.invert'))
            .width('100%')
            .height('100%')
        }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_icon_mask_svg'), 'tab1')
          .labelStyle({ selectedColor: $r('sys.color.brand'), unselectedColor: $r('sys.color.font_primary') })
          .iconStyle({ selectedColor: $r('sys.color.brand'), unselectedColor: $r('sys.color.font_primary') })
        )
      }
      .barFloatingStyle({
        systemMaterial: new uiMaterial.ImmersiveMaterial({
          style: uiMaterial.ImmersiveStyle.ULTRA_THIN,
          // 开启交互形变效果
          interactive: true,
        }),
        maskColor: Color.Transparent,
      })
      .barOverlap(true)
      .height('100%')
    }
    .width('100%')
    .height('100%')
  }
}
```

在支持沉浸式材质的高算力设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/q1TFQqWOSB2AOc8Q7sAymQ/zh-cn_image_0000002742124695.gif)

在支持沉浸式材质的中算力设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/CUV4UcqTQ9u-amNCQQkV5w/zh-cn_image_0000002712245788.gif)

在支持沉浸式材质的低算力设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/nfcBp1XtSP-9axvChiUJbA/zh-cn_image_0000002742004737.gif)

### 示例4（设置组件材质的光感交互反馈效果）

本示例介绍如何通过[ImmersiveOptions](arkts-apis-uimaterial.md#immersiveoptions)中的lightEffect接口使组件实现光感交互反馈效果。

从API版本26.0.0开始，新增lightEffect接口。

```ts
// xxx.ets
import { uiMaterial } from '@kit.ArkUI';

@Styles
function systemMaterialStyle() {
  .margin(5)
  .width(70)
  .height(70)
  .borderRadius(50)
}

@Entry
@Component
struct NavigationTitleMaterialDemo {
  @State myMaterial: uiMaterial.ImmersiveMaterial = new uiMaterial.ImmersiveMaterial({
    style: uiMaterial.ImmersiveStyle.ULTRA_THIN,
    interactive: true,
    lightEffect: {},
  });

  @Builder
  CustomMenuBuilder() {
    Stack() {
      Row() {
        Text('Title')
          .fontSize(30)
          .fontColor(Color.White)
          .margin({ right: 50 })

        Column() {
        }
        .systemMaterialStyle()
        .systemMaterial(this.myMaterial)

        Column() {
        }
        .systemMaterialStyle()
        .systemMaterial(this.myMaterial)

        Column() {
        }
        .systemMaterialStyle()
        .systemMaterial(this.myMaterial)
      }
      .justifyContent(FlexAlign.End)
    }
    .width('100%')
    .height(100)
  }

  build() {
    Stack() {
      // $r('app.media.invert')需要替换为开发者所需的图像资源文件
      Image($r('app.media.invert'))
      Navigation() {
        // 页面内容
      }
      .title(this.CustomMenuBuilder())
    }
    .width('100%')
    .height('100%')
  }
}
```

在支持沉浸式材质的高算力设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/H0XYapPhRkqj-w1MA-HHnA/zh-cn_image_0000002712405748.gif)

在支持沉浸式材质的中算力设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/zgq7yxCKShGbVaE0yjlnqA/zh-cn_image_0000002742124697.gif)

在支持沉浸式材质的低算力设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/WZKUcl2tSxuLkWZlJnzmkg/zh-cn_image_0000002712245790.gif)

### 示例5（查询材质等级与是否支持沉浸式材质）

本示例介绍如何通过[getGlobalMaterialLevel](arkts-apis-uimaterial.md#uimaterialgetglobalmateriallevel)获取设备的材质等级，并通过[isImmersiveMaterialSupported](arkts-apis-uimaterial.md#uimaterialisimmersivematerialsupported)判断设备是否支持沉浸式材质，据此决定是否为组件设置沉浸式材质。通过此种适配方式，应用可以在支持和不支持沉浸式材质的不同设备上复用同一套代码，在不支持沉浸式材质的设备上自动降级为普通样式，无需为不同设备编写不同代码。

从API版本26.0.0开始，新增getGlobalMaterialLevel和isImmersiveMaterialSupported方法。

```ts
// xxx.ets
import { uiMaterial } from '@kit.ArkUI';

@Styles
function systemMaterialStyle() {
  .margin(5)
  .width(70)
  .height(70)
  .borderRadius(50)
}

@Entry
@Component
struct NavigationTitleMaterialDemo {
  private materialLevel: uiMaterial.MaterialLevel = uiMaterial.getGlobalMaterialLevel(); // 材质档位由设备决定，应用运行后不会改变
  private isSupported: boolean = uiMaterial.isImmersiveMaterialSupported(); // 是否支持沉浸式材质由设备决定，应用运行后不会改变

  @Builder
  CustomMenuBuilder() {
    Stack() {
      Row() {
        Text('Title')
          .fontSize(30)
          .fontColor(Color.White)
          .margin({ right: 50 })

        Column() {
        }
        .systemMaterialStyle()
        .backgroundColor(this.isSupported ? Color.Transparent :
          '#f2f1f3f5') // 背景色写到systemMaterial之前，在支持沉浸式材质的低算力设备上，沉浸式材质中包含的背景色效果最终生效
        // 在支持沉浸式材质的设备上，设置透明的背景色和沉浸式材质，沉浸式材质后设置生效；在不支持沉浸式材质的设备上，设置'#f2f1f3f5'的背景色和undefined的无材质效果，'#f2f1f3f5'的背景色属性生效
        .systemMaterial(this.isSupported ? new uiMaterial.ImmersiveMaterial({
          style: uiMaterial.ImmersiveStyle.REGULAR,
        }) : undefined)

        Column() {
        }
        .systemMaterialStyle()
        .backgroundColor(this.isSupported ? Color.Transparent :
          $r('sys.color.comp_background_emphasize')) // 背景色写到systemMaterial之前，在支持沉浸式材质的低算力设备上，沉浸式材质中包含的背景色效果最终生效
        // 在支持沉浸式材质的设备上，设置透明的背景色和带赋色的沉浸式材质，带赋色的沉浸式材质后设置生效；在不支持沉浸式材质的设备上，设置资源值的背景色和undefined的无材质效果，资源值的背景色属性生效
        .systemMaterial(this.isSupported ? new uiMaterial.ImmersiveMaterial({
          style: uiMaterial.ImmersiveStyle.REGULAR,
          materialColor: $r('sys.color.comp_background_emphasize'),
        }) : undefined)

        Column() {
        }
        .systemMaterialStyle()
        .backgroundColor($r('sys.color.comp_background_emphasize')) // 背景色写到systemMaterial之前，在支持沉浸式材质的低算力设备上，沉浸式材质中包含的背景色效果最终生效
        // 在支持沉浸式材质的设备上，如果是高算力或中算力设备，后设置的沉浸式材质会清除背景色效果为透明色，使用材质效果；如果是低算力设备，后设置的沉浸式材质中包含的背景色效果覆盖了backgroundColor属性的效果，使用材质颜色
        // 在不支持沉浸式材质的设备上，设置systemMaterial无作用，资源值的背景色属性生效
        .systemMaterial(new uiMaterial.ImmersiveMaterial({
          style: uiMaterial.ImmersiveStyle.REGULAR,
          materialColor: $r('sys.color.comp_background_emphasize')
        }))
      }
      .justifyContent(FlexAlign.End)
    }
    .backgroundColor('#99000000')
    .width('100%')
    .height(100)
  }

  build() {
    Stack() {
      // $r('app.media.invert')需要替换为开发者所需的图像资源文件
      Image($r('app.media.invert'))

      Navigation() {
        Column() {
          Text(`MaterialLevel: ${this.materialLevel}`)
            .fontSize(16)

          Text(`IsImmersiveMaterialSupported: ${this.isSupported}`)
            .fontSize(16)
        }
        .backgroundColor(Color.White)
        .margin({ top: 100 })
        .padding(15)
      }
      .title(this.CustomMenuBuilder())
    }
    .width('100%')
    .height('100%')
  }
}
```

在支持沉浸式材质的高算力设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/dGXMk1aSRs6E1LldYUTZFw/zh-cn_image_0000002742004739.jpg)

在支持沉浸式材质的中算力设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/nRCZ41OZT5OOrC5na_eDiw/zh-cn_image_0000002712405750.jpg)

在支持沉浸式材质的低算力设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/sSpTuAovRAGXqi5kSSgRxw/zh-cn_image_0000002742124699.jpg)

在不支持沉浸式材质的设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/LuF1jFjfTiqAlbetLHDuEg/zh-cn_image_0000002712245792.jpg)
