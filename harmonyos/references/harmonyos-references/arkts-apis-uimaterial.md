---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uimaterial
title: "@ohos.arkui.uiMaterial (系统材质)"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.uiMaterial (系统材质)
category: harmonyos-references
scraped_at: 2026-11-21T09:13:56+08:00
doc_updated_at: 2026-10-26
content_hash: sha256:cbfcb8731868e8a7cbd7757f28b314ef5cf2ea1d09bd726aafd3e9c0c7a7a9ad
---

本模块提供系统材质的接口定义。不同的系统材质对应不同的UI效果，包括背景色[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)、边框颜色[borderColor](ts-universal-attributes-border.md#bordercolor)、边框宽度[borderWidth](ts-universal-attributes-border.md#borderwidth)、阴影[shadow](ts-universal-attributes-image-effect.md#shadow)、材质层滤镜[materialFilter](ts-universal-attributes-filter-effect.md#materialfilter23)效果。当前提供的系统材质为沉浸式材质类型[ImmersiveMaterial](arkts-apis-uimaterial.md#immersivematerial)，其设备兼容性和算力分档表现，请参考[ImmersiveMaterial](arkts-apis-uimaterial.md#immersivematerial)的描述。

开发指导请参考[沉浸光感](../harmonyos-guides/arkts-immersive-light-sense-overview.md)指南文档。

**起始版本：** 26.0.0

## 导入模块

```ts
import { uiMaterial } from '@kit.ArkUI';
```

## ImmersiveMaterial

沉浸式材质类，继承自[Material](arkts-apis-uimaterial.md#material)。

组件上设置ImmersiveMaterial时，

* 指定弹窗类组件（[AlertDialog](ts-methods-alert-dialog-box.md)、[ActionSheet](ts-methods-action-sheet.md)、[CustomDialog](ts-methods-custom-dialog-box.md)、[CalendarPickerDialog](ts-methods-calendarpicker-dialog.md)、[DatePickerDialog](ts-methods-datepicker-dialog.md)、[TimePickerDialog](ts-methods-timepicker-dialog.md)、[TextPickerDialog](ts-methods-textpicker-dialog.md)、[SelectionMenu](ohos-arkui-advanced-selectionmenu.md)、[AlphabetIndexer](ts-container-alphabet-indexer.md)弹窗、[Text](ts-basic-components-text.md)设置[copyOption](ts-basic-components-text.md#copyoption9)后长按或双击触发的文本菜单）的沉浸光感效果可在全页面生效。
* 指定弹窗类接口（[PromptAction](arkts-apis-uicontext-promptaction.md)、[ArkUI\_NativeDialog](capi-arkui-nativemodule-arkui-nativedialog.md)、[@ohos.promptAction (弹窗)](js-apis-promptaction.md)、[Popup控制](ts-universal-attributes-popup.md)、[Tips控制](ts-universal-attributes-tips.md)、[菜单控制](ts-universal-attributes-menu.md)、[半模态转场](ts-universal-attributes-sheet-transition.md)）的沉浸光感效果可在全页面生效。
* [Slider](ts-basic-components-slider.md)、[Toggle](ts-basic-components-toggle.md)、[Select](ts-basic-components-select.md)的沉浸光感效果可在全页面生效。
* 其他组件仅在Navigation/NavDestination标题栏或横向Tabs中barPosition为BarPosition.End的底部TabBar中生效。在其他区域中设置沉浸光感效果不生效。

沉浸式材质根据设备是否支持沉浸式材质和设备算力有分档表现：

* 判断支持的设备：可通过[uiMaterial.isImmersiveMaterialSupported](arkts-apis-uimaterial.md#uimaterialisimmersivematerialsupported)判断设备是否支持沉浸式材质。在不支持沉浸式材质的设备上可设置沉浸式材质但无效果。
* 获取算力等级：在支持沉浸式材质的设备上，可通过[uiMaterial.getGlobalMaterialLevel](arkts-apis-uimaterial.md#uimaterialgetglobalmateriallevel)获取设备的材质等级。
* 高算力和中算力设备：通过材质层滤镜属性[materialFilter](ts-universal-attributes-filter-effect.md#materialfilter23)和阴影[shadow](ts-universal-attributes-image-effect.md#shadow)属性实现材质效果。当[systemMaterial](ts-universal-attributes-image-effect.md#systemmaterial)属性生效后，已设置的背景色属性[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)会被恢复为透明色，已设置的边框宽度[borderWidth](ts-universal-attributes-border.md#borderwidth)属性会被恢复为无边框效果。
* 低算力设备：通过背景色[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)、边框颜色[borderColor](ts-universal-attributes-border.md#bordercolor)、边框宽度[borderWidth](ts-universal-attributes-border.md#borderwidth)、阴影[shadow](ts-universal-attributes-image-effect.md#shadow)属性实现材质效果。
* 系统设置的影响：同一材质的效果，会受到系统设置应用中沉浸光感配置项的影响，不同强弱程度的沉浸光感配置下，材质的参数和效果存在差异。

### constructor

constructor(options?: ImmersiveOptions)

ImmersiveMaterial的构造函数。创建的ImmersiveMaterial对象需通过组件的[systemMaterial](ts-universal-attributes-image-effect.md#systemmaterial)通用属性设置到组件上才能生效，其设备兼容性和算力分档表现参考[ImmersiveMaterial](arkts-apis-uimaterial.md#immersivematerial)的描述。

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

可通过设置systemMaterial(uiMaterial.Material.empty)来单独关闭某个组件的沉浸式系统材质效果。如果组件不支持组件级沉浸式系统材质接口，则无法通过此方法关闭材质效果。

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
| ENABLE | 1 | 使能模式。[弹出框Dialog](../harmonyos-guides/arkts-base-dialog-overview.md)、[即时反馈（Toast）](../harmonyos-guides/arkts-create-toast.md)、[AlphabetIndexer](ts-container-alphabet-indexer.md)、[ChipGroup](ohos-arkui-advanced-chipgroup.md)、[ChipGroupV2](ohos-arkui-advanced-chipgroupv2.md)、[Chip](ohos-arkui-advanced-chip.md)、[ChipV2](ohos-arkui-advanced-chipv2.md)、[Select](ts-basic-components-select.md)、[菜单控制](ts-universal-attributes-menu.md)、[Toggle](ts-basic-components-toggle.md)、[SegmentButton](ohos-arkui-advanced-segmentbutton.md)、[SegmentButtonV2](ohos-arkui-advanced-segmentbuttonv2.md)、[Slider](ts-basic-components-slider.md)、[SelectionMenu](ohos-arkui-advanced-selectionmenu.md)、[Navigation](ts-basic-components-navigation.md)、[NavDestination](ts-basic-components-navdestination.md)组件默认开启沉浸式系统材质；[Text](ts-basic-components-text.md)设置[copyOption](ts-basic-components-text.md#copyoption9)后长按或双击触发的文本菜单默认开启沉浸式系统材质；[Tabs](ts-container-tabs.md)设置[barFloatingStyle](ts-container-tabs.md#barfloatingstyle)并生效悬浮样式，页签栏Tabbar默认开启沉浸式系统材质。此模式下，沉浸式系统材质样式生效的优先级高于组件本身设置的背景色、模糊、阴影和边框样式。其他组件需开发者主动设置。 |
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
| type | [MaterialType](arkts-apis-uimaterial.md#materialtype) | 否 | 否 | 系统材质类型标识，表示当前配置对应的材质类型，开发者无需也无法通过配置文件设置。该值仅用于类型标识，不映射到底层功能。 |

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
| materialColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 材质层赋色。不同算力档位下生效方式不同：  - 高算力和中算力设备：不设置该参数或该参数为undefined时，不额外混合纯色效果；设置为有效颜色值时，在材质层滤镜效果的基础上再混合一层纯色效果；若设置的颜色为纯不透明颜色，会遮挡材质层滤镜效果。  - 低算力设备：不设置该参数或该参数为undefined时，生效材质自带的背景色效果；设置为有效颜色值时，该颜色作为背景色[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)属性值生效。  **说明**：该参数对支持沉浸式材质的所有档位的算力设备的显示效果生效。  默认值：undefined |
| colorInvert | boolean | 否 | 是 | 设置了材质对象的节点的子树是否自动将颜色适配为材质背景色的反色。  若为false，则不会自动反色。  若为true，则当材质样式满足系统定义的反色条件时才会自动反色。具体的使用限制如下：  - 自动反色仅在高算力和中算力设备上生效，低算力设备上设置colorInvert不会产生视觉效果差异。  - 自动反色与系统沉浸光感的强弱配置相关，沉浸式系统材质越薄、沉浸光感越强，越容易符合反色要求。  - 自动反色能力使用硬编码的颜色值（如Color.White、'#FFFFFFFF'）不会触发自动反色，仅对以下属性接口设置特殊资源（见下表1）值时生效：  Text组件的[fontColor](ts-basic-components-text.md#fontcolor)，Button组件的[fontColor](ts-basic-components-button.md#fontcolor)，SymbolGlyph组件的[fontColor](ts-basic-components-symbolglyph.md#fontcolor)，Image组件的[fillColor](ts-basic-components-image.md#fillcolor)，Search组件的[placeholderColor](ts-basic-components-search.md#placeholdercolor)、[fontColor](ts-basic-components-search.md#fontcolor10)，[searchIcon](ts-basic-components-search.md#searchicon10)中的图标颜色、[cancelButton](ts-basic-components-search.md#cancelbutton10)中的图标颜色、[caretStyle](ts-basic-components-search.md#caretstyle10)中的光标颜色，[searchButton](ts-basic-components-search.md#searchbutton) 中的按钮颜色，TabContent组件的[tabBar](ts-container-tabcontent.md#tabbar)属性使用[BottomTabBarStyle](ts-container-tabcontent.md#bottomtabbarstyle9)，Chip组件的[prefixIcon](ohos-arkui-advanced-chip.md#prefixiconoptions)、suffixIcon属性的[fillColor](ohos-arkui-advanced-chip.md#iconcommonoptions)，[label](ohos-arkui-advanced-chip.md#labeloptions)属性的[fontColor](ohos-arkui-advanced-chip.md#labeloptions)，ChipGroup组件的[itemStyle](ohos-arkui-advanced-chipgroup.md#chipitemstyle)的[fontColor](ohos-arkui-advanced-chipgroup.md#chipitemstyle)，TextArea组件的[fontColor](ts-basic-components-textarea.md#fontcolor)、[placeholderColor](ts-basic-components-textarea.md#placeholdercolor)，TextInput组件的[fontColor](ts-basic-components-textinput.md#fontcolor)、[placeholderColor](ts-basic-components-textinput.md#placeholdercolor)，SegmentButton组件的[fontColor](ohos-arkui-advanced-segmentbutton.md#属性-1)、[selectedFontColor](ohos-arkui-advanced-segmentbutton.md#属性-1)，SegmentButtonV2组件的[itemFontColor](ohos-arkui-advanced-segmentbuttonv2.md#tabsegmentbuttonv2)、[itemSelectedFontColor](ohos-arkui-advanced-segmentbuttonv2.md#tabsegmentbuttonv2)、[itemIconFillColor](ohos-arkui-advanced-segmentbuttonv2.md#tabsegmentbuttonv2)、[itemSelectedIconFillColor](ohos-arkui-advanced-segmentbuttonv2.md#tabsegmentbuttonv2)、[itemSymbolFontColor](ohos-arkui-advanced-segmentbuttonv2.md#tabsegmentbuttonv2)、[itemSelectedSymbolFontColor](ohos-arkui-advanced-segmentbuttonv2.md#tabsegmentbuttonv2)，Swiper组件的[fontColor](ts-container-swiper.md#fontcolor)。  默认值：false |
| applyShadow | boolean | 否 | 是 | 是否添加材质的阴影效果。  当该参数为true时，材质中的阴影效果固定生效，优先于[shadow](ts-universal-attributes-image-effect.md#shadow)通用属性。当该参数为false时，shadow通用属性生效，材质的阴影效果不生效。  **说明**：该参数对支持沉浸式材质的所有档位的算力设备的显示效果生效。  默认值：true |
| interactive | boolean | 否 | 是 | 是否启用交互形变效果。交互形变效果是指组件在用户交互时产生形变的视觉反馈效果。  当该参数为true时，启用交互形变效果。当该参数为false时，不启用交互形变效果。  **说明**：该参数对支持沉浸式材质的所有档位的算力设备的显示效果生效。  默认值：false |
| lightEffect | [LightEffectOptions](arkts-apis-uimaterial.md#lighteffectoptions) | null | 否 | 是 | 光感交互反馈效果参数。传入LightEffectOptions对象时启用光感交互反馈；传入null时显式禁用光感交互反馈效果；不传入时默认为undefined，取决于组件是否默认有交互光感效果。  **说明**：该参数仅对支持沉浸式材质的高算力和中算力设备的显示效果生效。  默认值：undefined，跟随组件的默认效果。 |

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
      .animationDuration(400)
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/0RHgck_iQduOLtIHjQK9QQ/zh-cn_image_0000002821758513.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=458212D7B0AAD1B014997BB99A460E106EC1CF3ED53DE78A1BEEED8913B1E756)

THIN样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/xrmT6z9aSvCkEo1j8zhCJQ/zh-cn_image_0000002793038576.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=79A786B21DFD2FBA4822EE7F521E9BB3BC3DAF64611D27C6D89399A41211C865)

REGULAR样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/gsHZD12qTMKia39DAZA4Cw/zh-cn_image_0000002792878606.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=9928F2BE46841708361A99D229382CE02E2E70D15C2FF1BB41A487228E5888E3)

THICK样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/5GLKbhWJSU2mkdEsIbXURw/zh-cn_image_0000002821838513.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=931A86DA7DAEE7DF985C57BC433BAC5F6F657B6288D8E2495DA3417BA7999C3E)

ULTRA\_THICK样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/92_hiSXPTK2STEobXbfOpw/zh-cn_image_0000002821758515.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=2E62029EC138B96337132332B3131460EA025E207681F29BA2715B1400E8DA07)

在支持沉浸式材质的中算力设备上表现：

ULTRA\_THIN样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/VuGWG9MLRcCC8PJhiJQy6w/zh-cn_image_0000002793038578.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=78FF950D4AFB34570D15FD68AD508492EE76913C9222B1D85C6E86EE2B181482)

THIN样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/I_kCgMVCQ16C0U8pthSwcw/zh-cn_image_0000002792878608.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=65B64E9F5EE783D71908B365C893A7E139831B65C08FE6CA37B0AAB0DA1132C1)

REGULAR样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/Kf85_UGNQY2q8la_BGAxQA/zh-cn_image_0000002821838515.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=B906FC4FC30D1F479936A6FF3F26956B19B9CB6DF81447652A964C70CCFD2811)

THICK样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/viJCoZpKSgKd78NbqeQSgg/zh-cn_image_0000002821758517.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=E69E881034E416811D1FB8EACE5730943109662BA397B610E00A1ED0DACBC3E5)

ULTRA\_THICK样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/wUUGSyq4QkyxAfwCrbUxqQ/zh-cn_image_0000002793038580.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=98D6045A2AD5AB03EC76A8BF0186CCF5AC1DDCEAF2898210B5C309957EFD3D4A)

在支持沉浸式材质的高算力设备上表现：

ULTRA\_THIN样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/YJSTz3f5QouLkSf6I_oZHg/zh-cn_image_0000002792878610.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=8484A2A355C84F9C7562C5C24232DAE8778369A9154358A626FE51576A1C15CD)

THIN样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/kAMnlwHBSp2hSimAtdRXmQ/zh-cn_image_0000002821838517.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=86C52B99F5DC66CF66BDB7FA1A49647E051FCB682A8FF1AAEF6E6559D2109FB9)

REGULAR样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/yYS4dLcoQVW43-p_hurA_w/zh-cn_image_0000002821758519.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=9C293D5498795A42982FF1583DB8571B3D8187C4EC11298640E4EB85A6A0DAAC)

THICK样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/VmVFKrtqQkCeNMmVJsd-_Q/zh-cn_image_0000002793038582.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=B6CD87D7CE73A1AFC432F0C43449E353BBE0CD9A9959621A47B9BDFFE86893E8)

ULTRA\_THICK样式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/tK4qgLYqTvi-9hRTZEJ3ww/zh-cn_image_0000002792878612.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=DA67C2ED140C2A3D7C949D86AD8DD6DBFC7C809137F305DF5829F8F24D743E45)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/Go711L9TQmOobGqxfl2hwQ/zh-cn_image_0000002821838519.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=14EBCBA898FCE0DF1385150F729DC692C2BEFD6119DA1D1214B1CE8F673957BD)

在支持沉浸式材质的中算力设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/0g3dKi4CSMCXl7vKQXRXRw/zh-cn_image_0000002821758521.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=A023A13938A8F5EA62883E0B733E0A98E31C2225CF0A2DACDA3106A433B867DD)

在支持沉浸式材质的低算力设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/XWrwUA8jT4aRnWjTtqjbiQ/zh-cn_image_0000002793038584.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8829F7D64EE3D2C04A81A4BE9F264802A22476736CE818765C3DA7BB94EB6D6)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/6o9gzFmAQ2-nv6kg4qc1gg/zh-cn_image_0000002792878614.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=B7960D4B34D7B9D3EFBF485519EBF40FC987CA2393B44E26E36103DC8334ED25)

在支持沉浸式材质的中算力设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/teDX8E1gSGaDC10jMB98qw/zh-cn_image_0000002821838521.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=3B71316074EB8F3B854C287106946A722710D3206187B73BB9595F22556B22B0)

在支持沉浸式材质的低算力设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/FoUMMTwHTLGdqauaUby35Q/zh-cn_image_0000002821758523.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3BA4C04D82D9B7279383D03FB6BCF585CE7F7DBA235A3A29D14688BE2EFD3D1)

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
  @State titleHeight: number = 100;

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
    .height(this.titleHeight)
  }

  build() {
    Stack() {
      // $r('app.media.invert')需要替换为开发者所需的图像资源文件
      Image($r('app.media.invert'))
      Navigation() {
        // 页面内容
      }
      .title({ builder: this.CustomMenuBuilder(), height: this.titleHeight })
    }
    .width('100%')
    .height('100%')
  }
}
```

在支持沉浸式材质的高算力设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/EYDRqpS8QqaT4YvBK81R4g/zh-cn_image_0000002793038586.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=9FE6D097B5F0D07726A73912FFD89362B8815799A24F24721DD71A5CB9FE2501)

在支持沉浸式材质的中算力设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/0CYvN2QAQ1SXfDygvqo61g/zh-cn_image_0000002792878616.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=6361BEDD2896B5A9EF9D58A5ED2DDD05FD8E6EBF4CFC1CF07EF629628945FFA6)

在支持沉浸式材质的低算力设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/_IEXDpo5SHu15zPpQdAgJw/zh-cn_image_0000002821838523.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=9FA60CB3BBC1CDF868D6736BF9D227F4324D8FC819F76B928BEECB0DE76F671B)

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
  @State titleHeight: number = 100;

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
    .height(this.titleHeight)
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
      .title({ builder: this.CustomMenuBuilder(), height: this.titleHeight })
    }
    .width('100%')
    .height('100%')
  }
}
```

在支持沉浸式材质的高算力设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/GA78sWSYRbu4AcYyw4Y9tg/zh-cn_image_0000002821758525.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A62DA21DBA623268DCCCF9715348011A109B15122C35AC152F67AA09C4A80F0)

在支持沉浸式材质的中算力设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/QFG3EEztS5GvDQe_9K3RrQ/zh-cn_image_0000002793038588.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=DEAD8FE284B381A657AD3B70E65665043C1B59D8389381565E836955B8D15569)

在支持沉浸式材质的低算力设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/b_jCy8ITTtu5xIkn7Sj9Sw/zh-cn_image_0000002792878618.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=16B3A4AB1848DD62211E20691534298EF0822957A9A97E7C87220C716FFCCD2E)

在不支持沉浸式材质的设备上表现：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/GLlnkiocQQOEyHgjtqk1GQ/zh-cn_image_0000002821838525.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011355Z&HW-CC-Expire=31536000000&HW-CC-Sign=5434C74276786465A795BC0C8CFC939F7CF95475214CCD3BE7D52B6A3E3458D7)
