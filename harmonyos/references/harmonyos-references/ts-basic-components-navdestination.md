---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination
title: NavDestination
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 导航与切换 > NavDestination
category: harmonyos-references
scraped_at: 2026-04-29T13:51:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b3ba96214b7e764d2906a451f3b2e346f2122c149f8c1c7fe2797c2ed0971525
---

作为子页面的根容器，用于显示[Navigation](ts-basic-components-navigation.md)的内容区。

说明

* 该组件从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件从API version 11开始默认支持安全区避让特性(默认值为：expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]))，开发者可以重写该属性覆盖默认行为，API version 11之前的版本需配合[expandSafeArea](ts-universal-attributes-expand-safe-area.md)属性实现安全区避让。
* NavDestination组件必须配合Navigation使用，作为Navigation目的页面的根节点，单独使用只能作为普通容器组件，不具备路由相关属性能力。
* 如果路由栈中间页面的生命周期发生变化，跳转之前的栈顶NavDestination的生命周期(onWillShow, onShown, onHidden, onWillDisappear)与跳转之后的栈顶NavDestination的生命周期(onWillShow, onShown, onHidden, onWillDisappear)均在最后触发。
* NavDestination未设置主副标题并且没有返回键时，不显示标题栏。
* 不建议设置位置、大小等布局相关属性，可能会造成页面显示异常。例如在NavDestination上添加[zIndex](ts-universal-attributes-z-order.md#zindex)属性时，会覆盖掉系统设置的层级，可能导致出现显示异常。

## 子组件

PhonePC/2in1TabletTVWearable

说明

* 子组件类型：系统组件和自定义组件，支持渲染控制类型（[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)、[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)和[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)）。
* 子组件个数：多个。

## 接口

PhonePC/2in1TabletTVWearable

NavDestination()

创建[Navigation](ts-basic-components-navigation.md)子页面的根容器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 属性

PhonePC/2in1TabletTVWearable

支持[通用属性](ts-component-general-attributes.md)。

### title

PhonePC/2in1TabletTVWearable

title(value: string | CustomBuilder | NavDestinationCommonTitle | NavDestinationCustomTitle | Resource, options?: NavigationTitleOptions)

设置页面标题。字符串超长时，如果不设置副标题，先缩小再换行2行后以"..."截断。如果设置副标题，先缩小后以"..."截断。

说明

从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | [CustomBuilder](ts-types.md#custombuilder8) | [NavDestinationCommonTitle](ts-basic-components-navdestination.md#navdestinationcommontitle) | [NavDestinationCustomTitle](ts-basic-components-navdestination.md#navdestinationcustomtitle) | [Resource14+](ts-types.md#resource) | 是 | 页面标题。 |
| options12+ | [NavigationTitleOptions](ts-basic-components-navigation.md#navigationtitleoptions11) | 否 | 标题栏选项。 |

### hideTitleBar

PhonePC/2in1TabletTVWearable

hideTitleBar(value: boolean)

设置是否隐藏标题栏。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否隐藏标题栏。  默认值：false  true： 隐藏标题栏。  false： 显示标题栏。 |

### hideTitleBar13+

PhonePC/2in1TabletTVWearable

hideTitleBar(hide: boolean, animated: boolean)

设置是否隐藏标题栏。与[hideTitleBar](ts-basic-components-navdestination.md#hidetitlebar)相比，新增标题栏显隐时是否使用动画。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hide | boolean | 是 | 是否隐藏标题栏。  默认值：false  true：隐藏标题栏。  false：显示标题栏。 |
| animated | boolean | 是 | 设置是否使用动画显隐标题栏。  默认值：false  true：使用动画显示隐藏标题栏。  false：不使用动画显示隐藏标题栏。 |

### toolbarConfiguration13+

PhonePC/2in1TabletTVWearable

toolbarConfiguration(toolbarParam: Array<ToolbarItem> | CustomBuilder, options?: NavigationToolbarOptions)

设置工具栏内容。未调用本接口时不显示工具栏。

说明

* 从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。
* 不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| toolbarParam | Array<[ToolbarItem](ts-basic-components-navigation.md#toolbaritem10)> | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 工具栏内容。  使用Array<[ToolbarItem](ts-basic-components-navigation.md#toolbaritem10)>写法设置的工具栏有如下特性：  -工具栏所有选项均分底部工具栏，在每个均分内容区布局文本和图标。  -竖屏模式最多支持显示5个图标，多余的图标会被放入自动生成的更多图标中，点击更多图标，可以展示剩余内容。横屏模式时，如果为[Split](ts-basic-components-navigation.md#navigationmode9枚举说明)模式，仍按照竖屏模式显示，如果为[Stack](ts-basic-components-navigation.md#navigationmode9枚举说明)模式需配合[menus](ts-basic-components-navdestination.md#menus12)属性的Array<[NavigationMenuItem](ts-basic-components-navigation.md#navigationmenuitem)>使用，底部工具栏会自动隐藏，同时底部工具栏所有选项移动至页面右上角菜单。  使用[CustomBuilder](ts-types.md#custombuilder8)写法为用户自定义工具栏选项，不具备以上功能。 |
| options | [NavigationToolbarOptions](ts-basic-components-navigation.md#navigationtoolbaroptions11) | 否 | 工具栏选项。包含工具栏背景颜色、工具栏背景模糊样式及模糊选项、工具栏背景属性、工具栏布局方式、是否隐藏工具栏的文本、工具栏更多图标的菜单选项。 |

### hideToolBar13+

PhonePC/2in1TabletTVWearable

hideToolBar(hide: boolean, animated?: boolean)

设置是否隐藏工具栏。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hide | boolean | 是 | 是否隐藏工具栏。  默认值：false  true：隐藏工具栏。  false：显示工具栏。 |
| animated | boolean | 否 | 设置是否使用动画显隐工具栏。  默认值：false  true：使用动画显示隐藏工具栏。  false：不使用动画显示隐藏工具栏。 |

### mode11+

PhonePC/2in1TabletTVWearable

mode(value: NavDestinationMode)

设置NavDestination类型，不支持动态修改。

说明

从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [NavDestinationMode](ts-basic-components-navdestination.md#navdestinationmode枚举说明11) | 是 | NavDestination类型。  默认值：NavDestinationMode.STANDARD |

### backButtonIcon11+

PhonePC/2in1TabletTVWearable

backButtonIcon(value: ResourceStr | PixelMap | SymbolGlyphModifier)

设置标题栏返回键图标。

说明

* 从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。
* 不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | [PixelMap](arkts-apis-image-pixelmap.md) | [SymbolGlyphModifier12+](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 是 | 标题栏返回键图标。 |

### backButtonIcon19+

PhonePC/2in1TabletTVWearable

backButtonIcon(icon: ResourceStr | PixelMap | SymbolGlyphModifier, accessibilityText?: ResourceStr)

设置标题栏返回键图标和无障碍播报内容。

说明

* 该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。
* 不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| icon | [ResourceStr](ts-types.md#resourcestr) | [PixelMap](arkts-apis-image-pixelmap.md) | [SymbolGlyphModifier](ts-universal-attributes-attribute-modifier.md) | 是 | 标题栏返回键图标。 |
| accessibilityText | [ResourceStr](ts-types.md#resourcestr) | 否 | 返回键无障碍播报内容。  默认值：系统语言是中文时为“返回”，系统语言是英文时为“back”。 |

### menus12+

PhonePC/2in1TabletTVWearable

menus(value: Array<NavigationMenuItem> | CustomBuilder)

设置页面右上角菜单。不设置时不显示菜单项。使用Array<[NavigationMenuItem](ts-basic-components-navigation.md#navigationmenuitem)> 写法时，竖屏最多支持显示3个图标，横屏最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。

说明

* 从API version 14开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。
* 不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<[NavigationMenuItem](ts-basic-components-navigation.md#navigationmenuitem)> | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 页面右上角菜单。 |

### menus19+

PhonePC/2in1TabletTVWearable

menus(items: Array<NavigationMenuItem> | CustomBuilder, options?: NavigationMenuOptions)

设置页面右上角菜单。不设置时不显示菜单项。与[menus](ts-basic-components-navdestination.md#menus12)相比，新增菜单选项。使用Array<[NavigationMenuItem](ts-basic-components-navigation.md#navigationmenuitem)> 写法时，竖屏最多支持显示3个图标，横屏最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。

说明

* 该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。
* 不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | Array<[NavigationMenuItem](ts-basic-components-navigation.md#navigationmenuitem)> | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 页面右上角菜单。 |
| options | [NavigationMenuOptions](ts-basic-components-navigation.md#navigationmenuoptions19) | 否 | 页面右上角菜单选项。 |

### ignoreLayoutSafeArea12+

PhonePC/2in1TabletTVWearable

ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>)

控制组件的布局，使其扩展到非安全区域。

说明

* 组件设置ignoreLayoutSafeArea之后生效的条件为：

  设置LayoutSafeAreaType.SYSTEM时，组件的边界与非安全区域重合时组件能够延伸到非安全区域下。
* 若组件扩展到非安全区域内，此时在非安全区域里触发的事件（例如：点击事件）等可能会被系统拦截，优先响应状态栏等系统组件。
* 组件想要扩展到非安全区域内，需隐藏或者设置标题栏和工具栏为[STACK](ts-basic-components-navigation.md#barstyle12枚举说明)模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| types | Array <[LayoutSafeAreaType](ts-universal-attributes-expand-safe-area.md#layoutsafeareatype12)> | 否 | 配置扩展安全区域的类型。  默认值：  [LayoutSafeAreaType.SYSTEM] |
| edges | Array <[LayoutSafeAreaEdge](ts-universal-attributes-expand-safe-area.md#layoutsafeareaedge12)> | 否 | 配置扩展安全区域的方向。  默认值：  [LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM]。 |

### systemBarStyle12+

PhonePC/2in1TabletTVWearable

systemBarStyle(style: Optional<SystemBarStyle>)

当Navigation中显示当前NavDestination时，设置对应系统状态栏的样式。

说明

* 必须配合Navigation使用，作为其Navigation目的页面的根节点时才能生效。
* 其他使用限制请参考Navigation对应的[systemBarStyle](ts-basic-components-navigation.md#systembarstyle12)属性说明。
* 从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[SystemBarStyle](arkts-apis-window-i.md#systembarstyle12)> | 是 | 系统状态栏样式。 |

### systemTransition14+

PhonePC/2in1TabletTVWearable

systemTransition(type: NavigationSystemTransitionType)

设置NavDestination系统转场动画，支持分别设置系统标题栏动画和内容动画。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [NavigationSystemTransitionType](ts-basic-components-navdestination.md#navigationsystemtransitiontype14枚举说明) | 是 | 系统转场动画类型。  默认值：NavigationSystemTransitionType.DEFAULT |

### recoverable14+

PhonePC/2in1TabletTVWearable

recoverable(recoverable: Optional<boolean>)

配置NavDestination是否可恢复。如配置为可恢复，当应用进程异常退出并重新冷启动时，可自动创建该NavDestination。该功能需NavDestination对应的Navigation也配置了[可恢复属性](ts-basic-components-navigation.md#recoverable14)。

说明

该接口需要配合Navigation的[recoverable](ts-basic-components-navigation.md#recoverable14)接口使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recoverable | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | NavDestination是否可恢复，默认为不可恢复。  默认值：false  true：路由栈可恢复。  false：路由栈不可恢复。 |

### bindToScrollable14+

PhonePC/2in1TabletTVWearable

bindToScrollable(scrollers: Array<Scroller>)

绑定NavDestination组件和可滚动容器组件（支持[List](ts-container-list.md)、[Scroll](ts-container-scroll.md)、[Grid](ts-container-grid.md)、[WaterFlow](ts-container-waterflow.md)），当滑动可滚动容器组件时，会触发所有与其绑定的NavDestination组件的标题栏和工具栏的显示和隐藏动效，上滑隐藏，下滑显示。一个NavDestination可与多个可滚动容器组件绑定，一个可滚动容器组件也可与多个NavDestination绑定。使用示例参见[示例1](ts-basic-components-navdestination.md#示例1标题栏工具栏与可滚动类组件联动)。

说明

* 只有NavDestination的标题栏或工具栏设置为可见时，联动效果才会生效。
* 当多个可滚动容器组件绑定了同一个NavDestination组件时，滚动任何一个容器都会触发标题栏和工具栏的显示或隐藏效果。且当任何一个可滚动容器组件滑动到底部或顶部位置时，会立即触发标题栏和工具栏的显示动效。因此，为了获得最佳用户体验，不建议同时触发多个可滚动容器组件的滚动事件。
* 从API version 22开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scrollers | Array<[Scroller](ts-container-scroll.md#scroller)> | 是 | 可滚动容器组件的控制器。 |

### bindToNestedScrollable14+

PhonePC/2in1TabletTVWearable

bindToNestedScrollable(scrollInfos: Array<NestedScrollInfo>)

绑定NavDestination组件和嵌套的可滚动容器组件（支持[List](ts-container-list.md)、[Scroll](ts-container-scroll.md)、[Grid](ts-container-grid.md)、[WaterFlow](ts-container-waterflow.md)），当滑动父组件或子组件时，会触发所有与其绑定的NavDestination组件的标题栏和工具栏的显示和隐藏动效，上滑隐藏，下滑显示。一个NavDestination可与多个嵌套的可滚动容器组件绑定，嵌套的可滚动容器组件也可与多个NavDestination绑定。使用示例参见[示例1](ts-basic-components-navdestination.md#示例1标题栏工具栏与可滚动类组件联动)。

说明

* 只有NavDestination的标题栏或工具栏设置为可见时，联动效果才会生效。
* 当多个可滚动容器组件绑定了同一个NavDestination组件时，滚动任何一个容器都会触发标题栏和工具栏的显示或隐藏效果。且当任何一个可滚动容器组件滑动到底部或顶部位置时，会立即触发标题栏和工具栏的显示动效。因此，为了获得最佳用户体验，不建议同时触发多个可滚动容器组件的滚动事件。
* 从API version 22开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scrollInfos | Array<[NestedScrollInfo](ts-basic-components-navdestination.md#nestedscrollinfo14)> | 是 | 嵌套的可滚动容器组件的控制器。 |

### hideBackButton15+

PhonePC/2in1TabletTVWearable

hideBackButton(hide: Optional<boolean>)

设置是否隐藏标题栏中的返回键。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hide | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否隐藏标题栏中的返回键。  默认值：false  true：隐藏返回键。  false：显示返回键。 |

### customTransition15+

PhonePC/2in1TabletTVWearable

customTransition(delegate: NavDestinationTransitionDelegate)

设置NavDestination自定义转场动画。

说明

* 该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。
* 该属性与[systemTransition](ts-basic-components-navdestination.md#systemtransition14)同时设置时，后设置的属性生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| delegate | [NavDestinationTransitionDelegate](ts-basic-components-navdestination.md#navdestinationtransitiondelegate15) | 是 | NavDestination自定义动画的代理函数。 |

### preferredOrientation19+

PhonePC/2in1TabletTVWearable

preferredOrientation(orientation: Optional<Orientation>)

设置NavDestination对应的显示方向。转场到该NavDestination后，系统也会将应用主窗口切到该显示方向。

说明

* 该属性满足如下全部条件时才有效：

  1. NavDestination属于应用主窗口页面，并且主窗口为全屏窗口；
  2. NavDestination所属的Navigation的大小占满整个应用页面；
  3. NavDestination类型为[NavDestinationMode](ts-basic-components-navdestination.md#navdestinationmode枚举说明11).STANDARD。
* 设置显示方向的实际效果依赖于具体的设备支持情况，具体参考窗口的[setPreferredOrientation](arkts-apis-window-window.md#setpreferredorientation9-1)接口。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| orientation | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Orientation](ts-basic-components-navdestination.md#orientation19)> | 是 | NavDestination页面对应的Orientation。 |

### enableStatusBar19+

PhonePC/2in1TabletTVWearable

enableStatusBar(enabled: Optional<boolean>, animated?: boolean)

设置进入该NavDestination后，显示或者隐藏系统的状态栏。

说明

* 该属性满足如下全部条件时才生效：

  1. NavDestination属于应用主窗口页面，并且主窗口为全屏窗口；
  2. NavDestination所属的Navigation的大小占满整个页面；
  3. NavDestination的大小占满整个Navigation组件；
  4. NavDestination类型为[NavDestinationMode](ts-basic-components-navdestination.md#navdestinationmode枚举说明11).STANDARD。
* 设置系统状态栏的实际效果依赖于具体的设备支持情况，具体参考窗口的[setSpecificSystemBarEnabled](arkts-apis-window-window.md#setspecificsystembarenabled11)接口。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 进入该NavDestination后，系统状态栏的显示/隐藏状态。  true： 显示状态栏。  false： 隐藏状态栏。 |
| animated | boolean | 否 | 是否使用动画的方式显示/隐藏系统状态栏，默认值为：false。  true：使用动画的方式显示/隐藏系统状态栏。  false：不使用动画的方式显示/隐藏系统状态栏。 |

### enableNavigationIndicator19+

PhonePC/2in1TabletTVWearable

enableNavigationIndicator(enabled: Optional<boolean>)

设置进入该NavDestination后，显示或者隐藏系统的导航条。

说明

该属性满足如下全部条件时才生效：

1. NavDestination属于应用主窗口页面，并且主窗口为全屏窗口；
2. NavDestination所属的Navigation的大小占满整个页面；
3. NavDestination的大小占满整个Navigation组件；
4. NavDestination类型为[NavDestinationMode](ts-basic-components-navdestination.md#navdestinationmode枚举说明11).STANDARD。

设置系统导航条的实际效果依赖于具体的设备支持情况，具体参考窗口的[setSpecificSystemBarEnabled](arkts-apis-window-window.md#setspecificsystembarenabled11)接口。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 进入该NavDestination后，系统导航条的显示/隐藏状态。  true： 显示导航条。  false： 隐藏导航条。 |

## NavDestinationMode枚举说明11+

PhonePC/2in1TabletTVWearable

NavDestination类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STANDARD | 0 | 标准模式的NavDestination。 |
| DIALOG | 1 | 默认透明，进出路由栈不影响下层NavDestination的可见性（onShown、onHidden等生命周期），只会触发onActive、onInactive这两个生命周期。  API version 13之前，默认无系统转场动画。从API version 13开始，支持系统转场动画。 |

## NavigationSystemTransitionType14+枚举说明

PhonePC/2in1TabletTVWearable

系统转场动画类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认系统转场动画。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| NONE | 1 | 无系统转场动画。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| TITLE | 2 | 标题栏系统转场动画。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| CONTENT | 3 | 内容区系统转场动画。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| FADE15+ | 4 | 渐变类型的系统转场动画。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| EXPLODE15+ | 5 | 中心缩放类型的系统转场动画。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| SLIDE\_RIGHT15+ | 6 | 右侧平移类型的系统转场动画。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| SLIDE\_BOTTOM15+ | 7 | 底部平移类型的系统转场动画。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |

说明

设置系统转场动画，支持分别设置系统标题栏动画和内容动画。

系统默认转场动画中只有STANDARD页面的push和pop动画有单独的标题栏动画，存在如下限制：

1. 设置NavigationSystemTransitionType为TITLE时，系统转场只有标题栏动画。
2. 设置NavigationSystemTransitionType为CONTENT时，系统转场只有内容区动画。

设置NONE或者TITLE时没有系统转场动画，设置CONTENT和DEFAULT时默认系统转场动画。

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持如下事件：

### onShown10+

PhonePC/2in1TabletTVWearable

onShown(callback: Callback<VisibilityChangeReason>)

当该NavDestination页面显示时触发此回调。从API version 21开始，支持通过VisibilityChangeReason说明onShown触发的原因。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](js-apis-base.md#callback)<[VisibilityChangeReason](ts-basic-components-navdestination.md#visibilitychangereason21)>21+ | 是 | 当该NavDestination页面显示时触发此回调。  在API version 21之前，当NavDestination页面显示时触发回调。  从API version 21开始，回调会提供入参VisibilityChangeReason以说明onShown触发的原因。 |

### onHidden10+

PhonePC/2in1TabletTVWearable

onHidden(callback: Callback<VisibilityChangeReason>)

当该NavDestination页面隐藏时触发此回调。从API version 21开始，支持通过VisibilityChangeReason说明onHidden触发的原因。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](js-apis-base.md#callback)<[VisibilityChangeReason](ts-basic-components-navdestination.md#visibilitychangereason21)>21+ | 是 | 当该NavDestination页面隐藏时触发此回调。  在API version 21之前，当NavDestination页面隐藏时触发回调。  从API version 21开始，该回调会提供入参VisibilityChangeReason以说明onHidden触发的原因。 |

### onWillAppear12+

PhonePC/2in1TabletTVWearable

onWillAppear(callback: Callback<void>)

当该NavDestination挂载之前触发此回调。在该回调中允许修改路由栈，当前帧生效。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 是 | 当该NavDestination挂载之前触发此回调。在该回调中允许修改路由栈，当前帧生效。 |

### onWillShow12+

PhonePC/2in1TabletTVWearable

onWillShow(callback: Callback<void>)

当该NavDestination显示之前触发此回调。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 是 | 当该NavDestination显示之前触发此回调。 |

### onWillHide12+

PhonePC/2in1TabletTVWearable

onWillHide(callback: Callback<void>)

当该NavDestination隐藏之前触发此回调。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 是 | 当该NavDestination隐藏之前触发此回调。 |

### onWillDisappear12+

PhonePC/2in1TabletTVWearable

onWillDisappear(callback: Callback<void>)

当该NavDestination卸载之前触发的生命周期(有转场动画时，在转场动画开始之前触发)。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 是 | 当该NavDestination卸载之前触发的生命周期(有转场动画时，在转场动画开始之前触发)。 |

### onBackPressed10+

PhonePC/2in1TabletTVWearable

onBackPressed(callback: () => boolean)

当与Navigation绑定的导航控制器中存在内容时，此回调生效。当点击返回键时，触发该回调。

返回值为true时，表示重写返回键逻辑，返回值为false时，表示回退到上一个页面。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | () => boolean | 是 | 当与Navigation绑定的导航控制器中存在内容时，此回调生效。当点击返回键时，触发该回调。 |

### onReady11+

PhonePC/2in1TabletTVWearable

onReady(callback: [Callback](js-apis-base.md#callback)<[NavDestinationContext](ts-basic-components-navdestination.md#navdestinationcontext11)>)

当NavDestination即将构建子组件之前会触发此回调。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](js-apis-base.md#callback)<[NavDestinationContext](ts-basic-components-navdestination.md#navdestinationcontext11)> | 是 | 当NavDestination即将构建子组件之前会触发此回调。 |

### onResult15+

PhonePC/2in1TabletTVWearable

onResult(callback: Optional<Callback<ESObject>>)

NavDestination返回时触发该回调。

说明

从API version 22开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Callback](js-apis-base.md#callback)<ESObject>> | 是 | 页面返回回调，入参为[pop](ts-basic-components-navigation.md#pop11)、[popToName](ts-basic-components-navigation.md#poptoname11)、[popToIndex](ts-basic-components-navigation.md#poptoindex11)接口传入的result参数。如果不传该参数，入参为undefined。 |

### onActive17+

PhonePC/2in1TabletTVWearable

onActive(callback: Optional<Callback<NavDestinationActiveReason>>)

NavDestination处于激活态（处于栈顶可操作，且上层无特殊组件遮挡）时，触发该回调。使用示例参见[示例5](ts-basic-components-navdestination.md#示例5navdestination的onactive与oninactive生命周期)。

说明

从API version 22开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Callback](js-apis-base.md#callback)<[NavDestinationActiveReason](ts-basic-components-navdestination.md#navdestinationactivereason17)>> | 是 | NavDestination由非激活态变为激活态的原因。 |

### onInactive17+

PhonePC/2in1TabletTVWearable

onInactive(callback: Optional<Callback<NavDestinationActiveReason>>)

NavDestination处于非激活态（处于非栈顶不可操作，或处于栈顶时上层有特殊组件遮挡）时，触发该回调。使用示例参见[示例5](ts-basic-components-navdestination.md#示例5navdestination的onactive与oninactive生命周期)。

说明

从API version 22开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Callback](js-apis-base.md#callback)<[NavDestinationActiveReason](ts-basic-components-navdestination.md#navdestinationactivereason17)>> | 是 | NavDestination由激活态变为非激活态的原因。 |

### onNewParam19+

PhonePC/2in1TabletTVWearable

onNewParam(callback: Optional<Callback<ESObject>>)

当之前存在于栈中的NavDestination页面通过[launchMode.MOVE\_TO\_TOP\_SINGLETON](ts-basic-components-navigation.md#launchmode12枚举说明)或[launchMode.POP\_TO\_SINGLETON](ts-basic-components-navigation.md#launchmode12枚举说明)移动到栈顶时，触发该回调。

说明

* [replacePath](ts-basic-components-navigation.md#replacepath11)、[replaceDestination](ts-basic-components-navigation.md#replacedestination18)不会触发该回调。
* 从API version 22开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Callback](js-apis-base.md#callback)<ESObject>> | 是 | onNewParam触发时的回调函数，入参为路由跳转时传递到目标页面的数据。 |

## NavDestinationCommonTitle

PhonePC/2in1TabletTVWearable

NavDestination通用标题。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| main | string | [Resource14+](ts-types.md#resource) | 否 | 否 | 设置主标题。 |
| sub | string | [Resource14+](ts-types.md#resource) | 否 | 否 | 设置副标题。 |

## NavDestinationCustomTitle

PhonePC/2in1TabletTVWearable

NavDestination自定义标题。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| builder | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 否 | 设置标题栏内容。 |
| height | [TitleHeight](ts-appendix-enums.md#titleheight9) | [Length](ts-types.md#length) | 否 | 否 | 设置标题栏高度。  取值范围：[0, +∞)。 |

## NavDestinationContext11+

PhonePC/2in1TabletTVWearable

NavDestination上下文信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pathInfo | [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | 否 | 否 | 跳转NavDestination时指定的参数。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| pathStack | [NavPathStack](ts-basic-components-navigation.md#navpathstack10) | 否 | 否 | 当前NavDestination所处的导航控制器。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| navDestinationId12+ | string | 否 | 是 | 当前NavDestination的唯一ID，由系统自动生成，和组件通用属性id无关。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| mode22+ | [NavDestinationMode](ts-basic-components-navdestination.md#navdestinationmode枚举说明11) | 否 | 是 | 当前NavDestination的类型。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |

### getConfigInRouteMap12+

PhonePC/2in1TabletTVWearable

getConfigInRouteMap(): RouteMapConfig | undefined

获取当前NavDestination的路由配置信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RouteMapConfig](ts-basic-components-navdestination.md#routemapconfig12) | undefined | 当前页面路由配置信息。  当该页面不是通过路由表配置时返回undefined。 |

## RouteMapConfig12+

PhonePC/2in1TabletTVWearable

路由配置信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 页面名称。 |
| pageSourceFile | string | 否 | 否 | 页面在当前包中的路径。 |
| data | Object | 否 | 否 | 页面自定义字段信息。 |

## NestedScrollInfo14+

PhonePC/2in1TabletTVWearable

嵌套可滚动容器组件信息

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| parent | [Scroller](ts-container-scroll.md#scroller) | 否 | 否 | 可滚动容器组件的控制器。 |
| child | [Scroller](ts-container-scroll.md#scroller) | 否 | 否 | 可滚动容器组件的控制器，child对应的组件需要是parent对应组件的子组件，且组件间存在嵌套滚动关系。 |

### NavDestinationActiveReason17+

PhonePC/2in1TabletTVWearable

NavDestination激活态或者非激活态变化的原因。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TRANSITION | 0 | 通过页面跳转的方式使NavDestination激活态发生变化。 |
| CONTENT\_COVER | 1 | 通过全模态的开启和关闭使NavDestination激活态发生变化。 |
| SHEET | 2 | 通过半模态的开启或关闭使NavDestination激活态发生变化。 |
| DIALOG | 3 | 通过自定义Dialog开启或关闭使NavDestination激活态发生变化。 |
| OVERLAY | 4 | 通过OverlayManager开启或者关闭Overlay使NavDestination激活态发生变化。 |
| APP\_STATE | 5 | 通过前后台切换使NavDestination激活态发生变化。 |

### VisibilityChangeReason21+

PhonePC/2in1TabletTVWearable

NavDestination可见性发生变化的原因。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TRANSITION | 0 | 通过页面跳转的方式使NavDestination可见性发生变化。 |
| CONTENT\_COVER | 1 | 通过全模态的开启和关闭使NavDestination可见性发生变化。 |
| APP\_STATE | 2 | 通过前后台切换使NavDestination可见性发生变化。 |

## NavDestinationTransition15+

PhonePC/2in1TabletTVWearable

NavDestination自定义动画接口。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onTransitionEnd | Callback<void> | 否 | 是 | 转场动画结束时的回调函数。 |
| duration | number | 否 | 是 | 转场动画的持续时间，默认值为1000（毫秒）。 |
| curve | [Curve](ts-appendix-enums.md#curve) | 否 | 是 | 动画的曲线类型，默认值为[Curve.EaseInOut](ts-appendix-enums.md#curve)。 |
| delay | number | 否 | 是 | 转场动画的延迟。默认值为0（毫秒）。 |
| event | Callback<void> | 否 | 否 | 指定转场动效的闭包函数，系统会根据闭包中对组件UI状态的修改，生成对应的过渡动画。参见[animateTo](arkts-apis-uicontext-uicontext.md#animateto)中的event。 |

## NavDestinationTransitionDelegate15+

PhonePC/2in1TabletTVWearable

type NavDestinationTransitionDelegate = (operation: NavigationOperation, isEnter: boolean) => Array<NavDestinationTransition> | undefined

NavDestination自定义转场动画的代理函数。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| operation | [NavigationOperation](ts-basic-components-navigation.md#navigationoperation11枚举说明) | 是 | 当前页面转场的操作类型。 |
| isEnter | boolean | 是 | 当前页面是否为入场页面。  true： 当前页面是入场页面。  false： 当前页面不是入场页面。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[NavDestinationTransition](ts-basic-components-navdestination.md#navdestinationtransition15)> | undefined | NavDestination页面的自定义动画集合。如果返回undefined则做系统默认动画。 |

## Orientation19+

PhonePC/2in1TabletTVWearable

type Orientation = Orientation

Orientation实例对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| [Orientation](arkts-apis-window-e.md#orientation9) | 返回Orientation实例对象。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（标题栏工具栏与可滚动类组件联动）

以下示例主要演示NavDestination绑定可滚动容器组件来实现滚动内容时触发标题栏和工具栏显示隐藏的效果。

```
1. import { SymbolGlyphModifier } from '@kit.ArkUI';

3. @Component
4. struct MyPageOne {
5. private listScroller: Scroller = new Scroller();
6. private scrollScroller: Scroller = new Scroller();
7. private arr: number[] = [];

9. aboutToAppear(): void {
10. for (let i = 0; i < 30; i++) {
11. this.arr.push(i);
12. }
13. }

15. build() {
16. NavDestination() {
17. Scroll(this.scrollScroller) {
18. Column() {
19. List({ space: 0, initialIndex: 0, scroller: this.listScroller }) {
20. ForEach(this.arr, (item: number, index: number) => {
21. ListItem() {
22. Text('' + item)
23. .height(100)
24. .fontSize(16)
25. .textAlign(TextAlign.Center)
26. .width('90%')
27. .margin({ left: '5%' })
28. .borderRadius(10)
29. .backgroundColor(Color.Gray)
30. }
31. }, (item: string) => item);
32. }.width('100%').height('80%').scrollBar(BarState.Off)
33. .nestedScroll({ scrollForward: NestedScrollMode.SELF_FIRST, scrollBackward: NestedScrollMode.SELF_FIRST })

35. ForEach(this.arr, (item: number, index: number) => {
36. ListItem() {
37. Text('' + item)
38. .height(100)
39. .fontSize(16)
40. .textAlign(TextAlign.Center)
41. .width('90%')
42. .margin({ top: '5%' })
43. .borderRadius(10)
44. .backgroundColor(Color.Pink)
45. }
46. }, (item: string) => item);
47. }
48. }
49. .width('100%')
50. .scrollBar(BarState.Off)
51. .scrollable(ScrollDirection.Vertical)
52. .edgeEffect(EdgeEffect.Spring)
53. }
54. .title('PageOne', { backgroundColor: Color.Yellow, barStyle: BarStyle.STACK })
55. .toolbarConfiguration([
56. {
57. // $r('sys.symbol.phone_badge_star')需要替换为开发者所需的资源文件
58. value: 'item1',
59. symbolIcon: new SymbolGlyphModifier($r('sys.symbol.phone_badge_star'))
60. }
61. ], { backgroundColor: Color.Orange, barStyle: BarStyle.STACK })
62. // 绑定有父子关系的可滚动容器组件
63. .bindToNestedScrollable([{ parent: this.scrollScroller, child: this.listScroller }])
64. }
65. }

67. @Component
68. struct MyPageTwo {
69. private listScroller: Scroller = new Scroller();
70. private arr: number[] = [];

72. aboutToAppear(): void {
73. for (let i = 0; i < 30; i++) {
74. this.arr.push(i);
75. }
76. }

78. build() {
79. NavDestination() {
80. List({ scroller: this.listScroller }) {
81. ForEach(this.arr, (item: number, index: number) => {
82. ListItem() {
83. Text('' + item)
84. .height(100)
85. .fontSize(16)
86. .textAlign(TextAlign.Center)
87. .width('90%')
88. .margin({ left: '5%' })
89. .borderRadius(10)
90. .backgroundColor(Color.Gray)
91. }
92. }, (item: string) => item);
93. }.width('100%')
94. }
95. .title('PageTwo', { backgroundColor: Color.Yellow, barStyle: BarStyle.STACK })
96. .toolbarConfiguration([
97. {
98. // $r('sys.symbol.phone_badge_star')需要替换为开发者所需的资源文件
99. value: 'item1',
100. symbolIcon: new SymbolGlyphModifier($r('sys.symbol.phone_badge_star'))
101. }
102. ], { backgroundColor: Color.Orange, barStyle: BarStyle.STACK })
103. // 绑定可滚动容器组件
104. .bindToScrollable([this.listScroller])
105. }
106. }

108. @Entry
109. @Component
110. struct Index {
111. private stack: NavPathStack = new NavPathStack();

113. @Builder
114. MyPageMap(name: string) {
115. if (name === 'myPageOne') {
116. MyPageOne();
117. } else {
118. MyPageTwo();
119. }
120. }

122. build() {
123. Navigation(this.stack) {
124. Column() {
125. Button('push PageOne').onClick(() => {
126. this.stack.pushPath({ name: 'myPageOne' });
127. })
128. Button('push PageTwo').onClick(() => {
129. this.stack.pushPath({ name: 'myPageTwo' });
130. })
131. }.height('40%').justifyContent(FlexAlign.SpaceAround)
132. }.width('100%')
133. .height('100%')
134. .title({ main: 'MainTitle', sub: 'subTitle' })
135. .navDestination(this.MyPageMap)
136. }
137. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/TAOkrT_uQNWOIBeuyVR22Q/zh-cn_image_0000002558606534.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055150Z&HW-CC-Expire=86400&HW-CC-Sign=3C975B471E4BE56638A9017EB5DE2F9AFF36091EC3AB135259528BB6F3688B2A)

### 示例2（设置NavDestination自定义转场）

以下示例主要演示NavDestination设置自定义转场动画属性[customTransition](ts-basic-components-navdestination.md#customtransition15)的效果。

```
1. @Entry
2. @Component
3. struct NavDestinationCustomTransition {
4. stack: NavPathStack = new NavPathStack();

6. @Builder
7. pageMap(name: string) {
8. if (name) {
9. NavDest();
10. }
11. }

13. aboutToAppear(): void {
14. this.stack.pushPath({name: 'dest0'});
15. }

17. build() {
18. Navigation(this.stack) {
19. // empty
20. }
21. .navDestination(this.pageMap)
22. .hideNavBar(true)
23. .title('Main Page')
24. .titleMode(NavigationTitleMode.Mini)
25. }
26. }

28. declare type voidFunc = () => void;

30. @Component
31. struct NavDest {
32. @State name: string = 'NA';
33. @State destWidth: string = '100%';
34. stack: NavPathStack = new NavPathStack();
35. @State translateY: string = '0';

37. @Builder
38. titleBuilder() {
39. Text(this.name)
40. .fontSize(20)
41. .height(55)
42. .fontWeight(FontWeight.Bold)
43. .width('100%')
44. .padding({ left: 16, right: 16 })
45. }

47. build() {
48. NavDestination() {
49. Column() {
50. Button('push next page', { stateEffect: true, type: ButtonType.Capsule })
51. .width('80%')
52. .height(40)
53. .margin(20)
54. .onClick(() => {
55. this.stack.pushPath({ name: this.name == 'PageOne' ? "PageTwo" : "PageOne" });
56. })
57. }
58. .size({ width: '100%', height: '100%' })
59. }
60. .title(this.titleBuilder)
61. .translate({ y: this.translateY })
62. .onReady((context) => {
63. this.name = context.pathInfo.name;
64. this.stack = context.pathStack;
65. })
66. .backgroundColor(this.name == 'PageOne' ? '#F1F3F5' : '#ff11dee5')
67. .customTransition(
68. (op: NavigationOperation, isEnter: boolean)
69. : Array<NavDestinationTransition> | undefined => {
70. console.info('[NavDestinationTransition]', 'reached delegate in frontend, op: ' + op + ', isEnter: ' + isEnter);

72. let transitionOneEvent: voidFunc = () => { console.info('[NavDestinationTransition]', 'reached transitionOne, empty now!'); }
73. let transitionOneFinishEvent: voidFunc = () => { console.info('[NavDestinationTransition]', 'reached transitionOneFinish, empty now!'); }
74. let transitionOneDuration: number = 500;
75. if (op === NavigationOperation.PUSH) {
76. if (isEnter) {
77. // ENTER_PUSH
78. this.translateY = '100%';
79. transitionOneEvent = () => {
80. console.info('[NavDestinationTransition]', 'transitionOne, push & isEnter');
81. this.translateY = '0';
82. }
83. } else {
84. // EXIT_PUSH
85. this.translateY = '0';
86. transitionOneEvent = () => {
87. console.info('[NavDestinationTransition]', 'transitionOne, push & !isEnter');
88. this.translateY = '0';
89. }
90. transitionOneDuration = 450;
91. }
92. } else if (op === NavigationOperation.POP) {
93. if (isEnter) {
94. // ENTER_POP
95. this.translateY = '0';
96. transitionOneEvent = () => {
97. console.info('[NavDestinationTransition]', 'transitionOne, pop & isEnter');
98. this.translateY = '0';
99. }
100. } else {
101. // EXIT_POP
102. this.translateY = '0';
103. transitionOneEvent = () => {
104. console.info('[NavDestinationTransition]', 'transitionOne, pop & !isEnter');
105. this.translateY = '100%';
106. }
107. }
108. }

110. let transitionOne: NavDestinationTransition = {
111. duration: transitionOneDuration,
112. delay: 0,
113. curve: Curve.Friction,
114. event: transitionOneEvent,
115. onTransitionEnd: transitionOneFinishEvent
116. };

118. let transitionTwoEvent: voidFunc = () => { console.info('[NavDestinationTransition]', 'reached transitionTwo, empty now!'); }
119. let transitionTwo: NavDestinationTransition = {
120. duration: 1000,
121. delay: 0,
122. curve: Curve.EaseInOut,
123. event: transitionTwoEvent,
124. onTransitionEnd: () => { console.info('[NavDestinationTransition]', 'reached Two\'s finish'); }
125. };

127. return [
128. transitionOne,
129. transitionTwo,
130. ];
131. })
132. }
133. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/fptm5K21Q4CIKhHPoNO92g/zh-cn_image_0000002589326061.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055150Z&HW-CC-Expire=86400&HW-CC-Sign=4CD9C06916A194ACE7E86713BF603A80377982B6B8C47D541007DF2CB000DE7C)

### 示例3（设置指定的NavDestination系统转场）

以下示例主要演示NavDestination设置系统转场动画[systemTransition](ts-basic-components-navdestination.md#systemtransition14)为Fade、Explode、SlideBottom与SlideRight时的转场效果。

```
1. @Entry
2. @Component
3. struct NavDestinationSystemTransition {
4. @Provide stack: NavPathStack = new NavPathStack()
5. @Provide homePageTransitionType: NavigationSystemTransitionType = NavigationSystemTransitionType.DEFAULT;

7. @Builder
8. pageMap(name: string) {
9. if (name === 'Fade') {
10. Fade();
11. } else if (name === 'Explode') {
12. Explode();
13. } else if (name === 'SlideRight') {
14. SlideRight();
15. } else if (name === 'SlideBottom') {
16. SlideBottom();
17. } else {
18. Dest();
19. }
20. }

22. aboutToAppear(): void {
23. this.stack.pushPath({name: 'Dest'});
24. }

26. build() {
27. Navigation(this.stack) {
28. // empty
29. }
30. .navDestination(this.pageMap)
31. .hideNavBar(true)
32. }
33. }

35. @Component
36. struct Dest {
37. @Consume stack: NavPathStack;
38. @Consume homePageTransitionType: NavigationSystemTransitionType;
39. @State name: string = 'NA';

41. build() {
42. NavDestination() {
43. HomeBody();
44. }
45. .title('Navigation System Animation')
46. .onReady((context) => {
47. this.name = context.pathInfo.name;
48. })
49. .systemTransition(this.homePageTransitionType)
50. }
51. }

53. @Component
54. struct Fade {
55. @Consume stack: NavPathStack;
56. @State name: string = 'NA';

58. build() {
59. NavDestination() {
60. DestBody({
61. name: this.name
62. })
63. }
64. .title(this.name)
65. .onReady((context) => {
66. this.name = context.pathInfo.name;
67. })
68. .systemTransition(NavigationSystemTransitionType.FADE)
69. }
70. }

72. @Component
73. struct Explode {
74. @Consume stack: NavPathStack;
75. @State name: string = 'NA';

77. build() {
78. NavDestination() {
79. DestBody({
80. name: this.name
81. })
82. }
83. .title(this.name)
84. .onReady((context) => {
85. this.name = context.pathInfo.name;
86. })
87. .systemTransition(NavigationSystemTransitionType.EXPLODE)
88. }
89. }

91. @Component
92. struct SlideRight {
93. @Consume stack: NavPathStack;
94. @State name: string = 'NA';

96. build() {
97. NavDestination() {
98. DestBody({
99. name: this.name
100. })
101. }
102. .title(this.name)
103. .onReady((context) => {
104. this.name = context.pathInfo.name;
105. })
106. .systemTransition(NavigationSystemTransitionType.SLIDE_RIGHT)
107. }
108. }

110. @Component
111. struct SlideBottom {
112. @Consume stack: NavPathStack;
113. @State name: string = 'NA';

115. build() {
116. NavDestination() {
117. DestBody({
118. name: this.name
119. })
120. }
121. .title(this.name)
122. .onReady((context) => {
123. this.name = context.pathInfo.name;
124. })
125. .systemTransition(NavigationSystemTransitionType.SLIDE_BOTTOM)
126. }
127. }

129. @Component
130. struct DestBody {
131. name: string = 'NA';

133. columnTextSize: number = 22;
134. columnTextFontWeight: FontWeight = FontWeight.Bolder;
135. columnWidth: string = '65%';
136. columnPadding: number = 22;
137. columnMargin: number = 10;
138. columnBorderRadius: number = 10;

140. build() {
141. Column() {
142. Column()
143. .width('85')
144. .height(50)
145. .backgroundColor(Color.White)
146. Column() {
147. Text(this.name)
148. .fontSize(this.columnTextSize)
149. .fontWeight(this.columnTextFontWeight)
150. }
151. .width(this.columnWidth)
152. .padding(this.columnPadding)
153. .margin(this.columnMargin)
154. .borderRadius(this.columnBorderRadius)
155. .shadow(ShadowStyle.OUTER_DEFAULT_LG)
156. }
157. }
158. }

160. @Component
161. struct HomeBody {
162. @Consume stack: NavPathStack;
163. @Consume homePageTransitionType: NavigationSystemTransitionType;

165. columnTextSize: number = 22;
166. columnTextFontWeight: FontWeight = FontWeight.Bolder;
167. columnWidth: string = '85%';
168. columnPadding: number = 22;
169. columnMargin: number = 10;
170. columnBorderRadius: number = 10;
171. columnShadow: ShadowStyle = ShadowStyle.OUTER_DEFAULT_MD;

173. build() {
174. Column() {
175. Search({ value: 'Search' })
176. .width(this.columnWidth)

178. Column() {
179. Text('fade')
180. .fontSize(this.columnTextSize)
181. .fontWeight(this.columnTextFontWeight)
182. }
183. .width(this.columnWidth)
184. .padding(this.columnPadding)
185. .margin(this.columnMargin)
186. .borderRadius(this.columnBorderRadius)
187. .shadow(this.columnShadow)
188. .onClick(() => {
189. this.homePageTransitionType = NavigationSystemTransitionType.FADE;
190. this.stack.pushPath({name: 'Fade'});
191. })

193. Column() {
194. Text('explode')
195. .fontSize(this.columnTextSize)
196. .fontWeight(this.columnTextFontWeight)
197. }
198. .width(this.columnWidth)
199. .padding(this.columnPadding)
200. .margin(this.columnMargin)
201. .borderRadius(this.columnBorderRadius)
202. .shadow(this.columnShadow)
203. .onClick(() => {
204. this.homePageTransitionType = NavigationSystemTransitionType.EXPLODE;
205. this.stack.pushPath({name: 'Explode'});
206. })

208. Column() {
209. Text('slide right')
210. .fontSize(this.columnTextSize)
211. .fontWeight(this.columnTextFontWeight)
212. }
213. .width(this.columnWidth)
214. .padding(this.columnPadding)
215. .margin(this.columnMargin)
216. .borderRadius(this.columnBorderRadius)
217. .shadow(this.columnShadow)
218. .onClick(() => {
219. this.homePageTransitionType = NavigationSystemTransitionType.SLIDE_RIGHT;
220. this.stack.pushPath({name: 'SlideRight'});
221. })

223. Column() {
224. Text('slide bottom')
225. .fontSize(this.columnTextSize)
226. .fontWeight(this.columnTextFontWeight)
227. }
228. .width(this.columnWidth)
229. .padding(this.columnPadding)
230. .margin(this.columnMargin)
231. .borderRadius(this.columnBorderRadius)
232. .shadow(this.columnShadow)
233. .onClick(() => {
234. this.homePageTransitionType = NavigationSystemTransitionType.SLIDE_BOTTOM;
235. this.stack.pushPath({name: 'SlideBottom'});
236. })
237. }
238. }
239. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/QRu7i_5xQACrdcwJyz0-Vg/zh-cn_image_0000002589246003.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055150Z&HW-CC-Expire=86400&HW-CC-Sign=6906D20C239F2A2E2095224E25672B2EA7450C604B20BA22F7935A4710D18CD7)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/xbIZcIIHQ0een67Z26qiSg/zh-cn_image_0000002558766194.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055150Z&HW-CC-Expire=86400&HW-CC-Sign=D3CC599B31CAD05A6CFA1BB7846603137103A97BC44A5979EAE25D792B2D814E)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/NArEB4IOTfGnDfJzkvuxCA/zh-cn_image_0000002558606536.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055150Z&HW-CC-Expire=86400&HW-CC-Sign=766AAF2F092C18CB5FCBB9ECBF47200F7672EEB376584A95B59BB7C7B67498F9)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/53ZVxSCKStq8RaNjZfwgOw/zh-cn_image_0000002589326063.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055150Z&HW-CC-Expire=86400&HW-CC-Sign=A6CE572924ABF196F0BAD4B7F8EC19F4200EE8B9AEF4A488CFCFC8CE83E04D46)

### 示例4（NavDestination配置页面方向和对应状态栏、导航条显隐）

以下示例主要演示每个NavDestination可以配置指定的页面方向和状态栏，导航条显隐状态。

```
1. import { window } from '@kit.ArkUI';

3. @Component
4. struct PortraitPage {
5. @State info: string = '';
6. private stack: NavPathStack | undefined = undefined;
7. build() {
8. NavDestination() {
9. Stack({alignContent: Alignment.Center}) {
10. Button('push LANDSCAPE page').onClick(() => {
11. this.stack?.pushPath({name: 'landscape'});
12. })
13. }.width('100%').height('100%')
14. }
15. .width('100%').height('100%')
16. .title('PortraitPage')
17. .preferredOrientation(window.Orientation.PORTRAIT) // 竖屏方向
18. .enableStatusBar(true) // 显示状态栏
19. .enableNavigationIndicator(true) // 显示导航条
20. .backgroundColor('#ffbaece9')
21. .onResult((result: ESObject)=>{
22. this.info = result as string;
23. })
24. .onReady((ctx: NavDestinationContext) => {
25. this.stack = ctx.pathStack;
26. })
27. }
28. }

30. @Component
31. struct LandscapePage {
32. private stack: NavPathStack | undefined = undefined;
33. build() {
34. NavDestination() {
35. Stack({alignContent: Alignment.Center}) {
36. Button('push PORTRAIT page').onClick(() => {
37. this.stack?.pushPath({name: 'portrait'});
38. })
39. }.width('100%').height('100%')
40. }
41. .width('100%').height('100%')
42. .title('LandscapePage')
43. .preferredOrientation(window.Orientation.LANDSCAPE) // 横屏方向
44. .enableStatusBar(false) // 隐藏状态栏
45. .enableNavigationIndicator(false) // 隐藏导航条
46. .backgroundColor('#ffecb8b8')
47. .ignoreLayoutSafeArea([LayoutSafeAreaType.SYSTEM], [LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM])
48. .onReady((ctx: NavDestinationContext) => {
49. this.stack = ctx.pathStack;
50. })
51. }
52. }

54. @Entry
55. @Component
56. struct ExamplePage {
57. private stack: NavPathStack = new NavPathStack();

59. aboutToAppear(): void {
60. this.stack.pushPath({name: "portrait"});
61. }

63. @Builder
64. MyPageMap(name: string) {
65. if (name === 'portrait') {
66. PortraitPage();
67. } else {
68. LandscapePage();
69. }
70. }

72. build() {
73. Navigation(this.stack) {
74. }
75. .width('100%')
76. .height('100%')
77. .hideNavBar(true)
78. .navDestination(this.MyPageMap)
79. }
80. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/dLOvns6ZQhaHFvCbuG9_Bg/zh-cn_image_0000002589246005.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055150Z&HW-CC-Expire=86400&HW-CC-Sign=BF859F5809BDF6EC4F2856F51CF9940306EE0F0FF799F4D405C7BC4A367BBABA)

### 示例5（NavDestination的onActive与onInActive生命周期）

从API version 17开始，NavDestination新增[onActive](ts-basic-components-navdestination.md#onactive17)、[onInactive](ts-basic-components-navdestination.md#oninactive17)属性。该示例演示onActive与onInactive生命周期的各种触发场景。

```
1. import { promptAction, ComponentContent, OverlayManager } from '@kit.ArkUI';

3. class Params {
4. text: string = "";
5. offset: Position;

7. constructor(text: string, offset: Position) {
8. this.text = text;
9. this.offset = offset;
10. }
11. }

13. let overlayShownTag: boolean = false;

15. @Builder
16. function builderText(params: Params) {
17. Column() {
18. Text('I am ' + params.text)
19. .fontWeight(FontWeight.Bolder)
20. .align(Alignment.Center)
21. .fontSize(25)
22. .offset({ y: '10%' })
23. }
24. .backgroundColor(params.text === 'overlay' ? '#ffc' : '#ccf')
25. .width('100%')
26. .height('100%')
27. .offset(params.offset)
28. }

30. @Entry
31. @Component
32. struct Index {
33. stack: NavPathStack = new NavPathStack();

35. @Builder
36. pageMap(name: string) {
37. if (name === 'standard' || name === 'Home') {
38. NavDest({
39. name: name
40. })
41. }
42. else if (name === 'dialog') {
43. NavDest({
44. name: name,
45. mode: NavDestinationMode.DIALOG,
46. positionY: '40%'
47. })
48. }
49. }

51. aboutToAppear(): void {
52. this.stack.pushPath({name: 'Home'});
53. }

55. build() {
56. Navigation(this.stack) {

58. }
59. .hideNavBar(true)
60. .navDestination(this.pageMap)
61. }
62. }

64. @Component
65. struct NavDest {
66. @State positionY: string = '0%';
67. name: string = 'NA';
68. mode: NavDestinationMode = NavDestinationMode.STANDARD;

70. build() {
71. NavDestination() {
72. NavBody()
73. }
74. .backgroundColor(this.mode === NavDestinationMode.DIALOG ? Color.Pink : undefined)
75. .height(this.mode === NavDestinationMode.DIALOG ? '65%' : '100%')
76. .mode(this.mode)
77. .title(this.name)
78. .position({ y: this.positionY })
79. .onActive((reason: NavDestinationActiveReason) => {
80. let onActiveMsg: string = `[activeTest] ${this.name} onActive, reason: ${reason}`;
81. console.info(onActiveMsg);
82. // API version 17版本，请替换为promptAction.showToast接口。从API version 18开始，请使用示例中的promptAction.openToast接口。
83. promptAction.openToast({ message: onActiveMsg }).catch(() => {
84. console.info('open toast failed');
85. });
86. })
87. .onInactive((reason: NavDestinationActiveReason) => {
88. let onInActiveMsg: string = `[activeTest] ${this.name} onInactive, reason: ${reason}`;
89. console.info(onInActiveMsg);
90. // API version 17版本，请替换为promptAction.showToast接口。从API version 18开始，请使用示例中的promptAction.openToast接口。
91. promptAction.openToast({ message: onInActiveMsg }).catch(() => {
92. console.info('open toast failed');
93. });
94. })
95. .onBackPressed(() => {
96. if (overlayShownTag) {
97. overlayShownTag = false;
98. this.getUIContext().getOverlayManager().hideAllComponentContents();
99. return true;
100. }
101. return false;
102. })
103. }
104. }

106. @Component
107. struct NavBody {
108. @State isShow: boolean = false;
109. @State isBindSheetShow: boolean = false;
110. stack: NavPathStack = new NavPathStack();

112. aboutToAppear(): void {
113. this.stack = this.queryNavigationInfo()?.pathStack!;
114. }

116. @Builder
117. myBuilder(id: string) {
118. Column() {
119. Text('I am ' + id)
120. .fontWeight(FontWeight.Bolder)
121. .align(Alignment.Center)
122. .fontSize(25)
123. .offset({ y: '10%' })
124. }
125. .width('100%')
126. .height('100%')
127. }

129. build() {
130. Column() {
131. Row() {
132. Button('pushPath standard')
133. .margin(5)
134. .onClick(() => {
135. this.stack.pushPath({name: 'standard'});
136. })
137. Button('pushPath dialog')
138. .margin(5)
139. .onClick(() => {
140. this.stack.pushPath({name: 'dialog'});
141. })
142. }
143. Column() {
144. Row() {
145. Button("open Modal")
146. .onClick(() => {
147. this.isShow = true;
148. })
149. .fontColor(Color.Black)
150. .backgroundColor('#ccc')
151. .margin(5)
152. .bindContentCover(
153. this.isShow,
154. this.myBuilder('modal'), {
155. backgroundColor: '#fcf',
156. onDisappear: () => {
157. this.isShow = false;
158. }
159. })
160. Button("open BindSheet")
161. .onClick(() => {
162. this.isBindSheetShow = true;
163. })
164. .fontColor(Color.Black)
165. .backgroundColor('#ccc')
166. .margin(5)
167. .bindSheet($$this.isBindSheetShow, this.myBuilder('bindSheet'), {
168. height: '60%',
169. backgroundColor: '#cfc'
170. })
171. }
172. Row() {
173. Button("open Dialog")
174. .onClick(() => {
175. let componentContent = new ComponentContent(
176. this.getUIContext(), wrapBuilder<[Params]>(builderText),
177. new Params('dialog', {y: '10%'}));
178. this.getUIContext().getPromptAction().openCustomDialog(componentContent)
179. .then(() => {
180. console.info('[activeTest] open custom dialog success');
181. })
182. .catch(() => {
183. console.info('[activeTest] open custom dialog failed');
184. })
185. })
186. .fontColor(Color.Black)
187. .backgroundColor('#ccc')
188. .margin(5)
189. Button("open Overlay")
190. .onClick(() => {
191. let componentContent = new ComponentContent(
192. this.getUIContext(), wrapBuilder<[Params]>(builderText),
193. new Params('overlay', {y: '10%'}));
194. this.getUIContext().getOverlayManager().addComponentContent(componentContent);
195. this.getUIContext().getOverlayManager().showComponentContent(componentContent);
196. overlayShownTag = true;
197. })
198. .fontColor(Color.Black)
199. .backgroundColor('#ccc')
200. .margin(5)
201. }
202. }
203. .width('95%')
204. }
205. .width('100%')
206. .height('100%')
207. }
208. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/V2I1GC7jR5iLDWcJOQdfHw/zh-cn_image_0000002558766196.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055150Z&HW-CC-Expire=86400&HW-CC-Sign=9A2254D7E81A2DEBEFE0DF22FCC316DBFD414A0A9882535F5893ABC6B12174A8)

NavDestination其他用法可参考[Navigation示例](ts-basic-components-navigation.md#示例)。
