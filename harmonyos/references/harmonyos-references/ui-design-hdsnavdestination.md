---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavdestination
title: HdsNavDestination
breadcrumb: API参考 > 应用框架 > UI Design Kit（UI设计套件） > ArkTS组件 > HdsNavDestination
category: harmonyos-references
scraped_at: 2026-04-28T08:06:41+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:78b95bda158d55a4d3761d7ae26b72aaca55cc841f3d990413cf03974971ff66
---

作为子页面的根容器，用于显示[HdsNavigation](ui-design-hdsnavigation.md)的内容区，默认支持标题栏随内容区滚动的动态模糊样式。6.0.0(20)版本以后，推荐使用[bindToScrollable](ui-design-hdsnavdestination.md#bindtoscrollable)、[bindToNestedScrollable](ui-design-hdsnavdestination.md#bindtonestedscrollable)属性绑定导航组件和可滚动容器组件后，再使用导航组件滚动相关的功能，从而获得更优的体验。如滚动生效动态模糊样式，标题栏随内容区滚动动态显隐功能等。

**起始版本：** 5.1.0(18)

说明

* HdsNavDestination组件必须配合HdsNavigation使用，作为HdsNavigation目的页面的根节点，单独使用只能作为普通容器组件，不具备路由相关属性能力。
* 如果路由栈中间页面的生命周期发生变化，跳转之前的栈顶Destination的生命周期(onWillShow, onShown, onHidden, onWillDisappear)与跳转之后的栈顶Destination的生命周期(onWillShow, onShown, onHidden, onWillDisappear)均在最后触发。
* 不支持在HdsNavDestination上添加zIndex属性，会覆盖掉系统设置的层级，可能导致出现显示异常。

## 导入模块

PhonePC/2in1TabletTV

说明

* HdsNavDestinationAttribute是用于配置HdsNavDestination组件属性的关键接口。6.0.1(21)及之前版本，导入HdsNavDestination组件后需要开发者手动导入HdsNavDestinationAttribute，否则会编译报错。从6.0.2(22)版本开始，编译工具链识别到导入HdsNavDestination组件后，会自动导入HdsNavDestinationAttribute，无需开发者手动导入。
* 如果开发者手动导入HdsNavDestinationAttribute，DevEco Studio会显示置灰，6.0.1(21)及之前版本删除会编译报错，从6.0.2(22)版本开始，删除对功能无影响。

6.0.1(21)及之前版本：

```
1. import { HdsNavDestination, HdsNavDestinationAttribute } from '@kit.UIDesignKit';
```

6.0.2(22)及之后版本：

```
1. import { HdsNavDestination } from '@kit.UIDesignKit';
```

## 子组件

PhonePC/2in1TabletTV

* 子组件类型：系统组件和自定义组件，支持渲染控制类型（[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)、[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)和[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)）。
* 子组件个数：多个。

## 接口

PhonePC/2in1TabletTV

HdsNavDestination()

创建[HdsNavigation](ui-design-hdsnavigation.md)子页面的根容器。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

## 属性

PhonePC/2in1TabletTV

支持[通用属性](ts-component-general-attributes.md)。

不推荐设置位置、大小等布局相关属性，可能会造成页面显示异常。

### titleBar

PhonePC/2in1TabletTV

titleBar(options?: HdsNavigationTitleBarOptions)

设置HdsNavDestination组件titleBar区域（包括返回图标区域、标题区域、菜单区域、背景板）样式以及内容。

标题字符串超长时，如果不设置副标题，先缩小再换行（2行）最后以"..."截断。如果设置副标题，先缩小后以"..."截断。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [HdsNavigationTitleBarOptions](ui-design-hdsnavigation.md#hdsnavigationtitlebaroptions) | 否 | 标题栏配置信息。 |

### hideTitleBar

PhonePC/2in1TabletTV

hideTitleBar(hide: boolean, animated?: boolean)

设置是否隐藏标题栏，并且可设置在标题栏显示隐藏的状态变化中是否使用动画。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hide | boolean | 是 | 是否隐藏标题栏。  默认值：false。  - true：隐藏标题栏。  - false：显示标题栏。 |
| animated | boolean | 否 | 设置是否使用动画显隐标题栏。  默认值：false。  - true：使用动画显示隐藏标题栏。  - false：不使用动画显示隐藏标题栏。 |

### hideBackButton

PhonePC/2in1TabletTV

hideBackButton(value: boolean)

设置是否隐藏标题栏中的返回键。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否隐藏标题栏中的返回键。  默认值：false。  - true：隐藏返回键。  - false：显示返回键。 |

### mode

PhonePC/2in1TabletTV

mode(value: NavDestinationMode)

设置HdsNavDestination类型，不支持动态修改。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [NavDestinationMode](ts-basic-components-navdestination.md#navdestinationmode枚举说明11) | 是 | HdsNavDestination类型。  默认值：NavDestinationMode.STANDARD。 |

### toolbarConfiguration

PhonePC/2in1TabletTV

toolbarConfiguration(toolbarParam: Array<ToolbarItem> | CustomBuilder, options?: NavigationToolbarOptions)

设置工具栏内容。未调用本接口时不显示工具栏。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| toolbarParam | Array<[ToolbarItem](ts-basic-components-navigation.md#toolbaritem10)> | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 工具栏内容。  使用Array<[ToolbarItem](ts-basic-components-navigation.md#toolbaritem10)>写法设置的工具栏有如下特性：  - 如果为[Stack](ts-basic-components-navigation.md#navigationmode9枚举说明)模式，不推荐使用该写法。推荐使用[CustomBuilder](ts-types.md#custombuilder8)配合[ToolBar](ohos-arkui-advanced-toolbar.md)组件写法，避免布局显示问题。  - 工具栏所有选项均分底部工具栏，在每个均分内容区布局文本和图标。  - 文本超长时，若工具栏选项个数小于5个，优先拓展选项的宽度，最大宽度与屏幕等宽，其次逐级缩小，缩小之后换行，最后截断。  - 最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。  使用[CustomBuilder](ts-types.md#custombuilder8)写法为用户自定义工具栏选项，除均分底部工具栏外不具备以上功能。 |
| options | [NavigationToolbarOptions](ts-basic-components-navigation.md#navigationtoolbaroptions11) | 否 | 工具栏选项。 |

说明

不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

### hideToolBar

PhonePC/2in1TabletTV

hideToolBar(hide: boolean, animated?: boolean)

设置是否隐藏工具栏，并且可设置在工具栏显示隐藏的状态变化中是否使用动画。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hide | boolean | 是 | 是否隐藏工具栏。  默认值：false。  - true：隐藏工具栏。  - false：显示工具栏。 |
| animated | boolean | 否 | 设置是否使用动画显隐工具栏。  默认值：false。  - true：使用动画显示隐藏工具栏。  - false：不使用动画显示隐藏工具栏。 |

### ignoreLayoutSafeArea

PhonePC/2in1TabletTV

ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>)

控制组件的布局，使其扩展到非安全区域。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| types | Array <[LayoutSafeAreaType](ts-universal-attributes-expand-safe-area.md#layoutsafeareatype12)> | 否 | 配置扩展安全区域的类型。  默认值：[LayoutSafeAreaType.SYSTEM]。 |
| edges | Array <[LayoutSafeAreaEdge](ts-universal-attributes-expand-safe-area.md#layoutsafeareaedge12)> | 否 | 配置扩展安全区域的方向。  默认值：[LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM]。 |

说明

组件设置LayoutSafeArea之后生效的条件为：

设置LayoutSafeAreaType.SYSTEM时，组件的边界与非安全区域重合时组件能够延伸到非安全区域下。

例如：设备顶部状态栏高度100，组件在屏幕中纵向方位的绝对偏移需要在0到100之间。

若组件延伸到非安全区域内，此时在非安全区域里触发的事件（例如：点击事件）等可能会被系统拦截，优先响应状态栏等系统组件。

### systemBarStyle

PhonePC/2in1TabletTV

systemBarStyle(originalStyle: Optional<SystemBarStyle>, scrollEffectStyle: Optional<SystemBarStyle>)

当HdsNavigation中显示当前HdsNavDestination时，设置对应系统状态栏的样式。若未与HdsNavigation配合使用，systemBarStyle属性可能不会生效，建议开发者在使用前确保已正确配置HdsNavigation组件。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| originalStyle | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[SystemBarStyle](arkts-apis-window-i.md#systembarstyle12)> | 是 | 系统状态栏初始样式。未设置systemBarStyle属性时，颜色默认值同主标题栏字体颜色。 |
| scrollEffectStyle | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[SystemBarStyle](arkts-apis-window-i.md#systembarstyle12)> | 是 | HdsNavDestination动态样式生效后，系统状态栏对应的最终动态样式。未设置systemBarStyle属性时，颜色默认值同主标题栏字体颜色。 |

说明：

1. 必须配合HdsNavigation使用，作为其HdsNavigation目的页面的根节点时才能生效。
2. 其他使用限制请参考HdsNavigation对应的[systemBarStyle](ui-design-hdsnavigation.md#systembarstyle)属性说明。

### recoverable

PhonePC/2in1TabletTV

recoverable(recoverable: Optional<boolean>)

配置HdsNavDestination是否可恢复。如配置为可恢复，当应用进程异常退出并重新冷启动时，可自动创建该HdsNavDestination。该功能需HdsNavDestination对应的HdsNavigation也配置了可恢复属性使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recoverable | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | HdsNavDestination是否可恢复，默认为不可恢复。  默认值：false。  - true：页面栈可恢复。  - false：页面栈不可恢复。 |

### dynamicHideTitleBar

PhonePC/2in1TabletTV

dynamicHideTitleBar(value: DynamicHideParams)

设置标题栏跟随内容区动态显隐配置，推荐搭配[bindToScrollable](ui-design-hdsnavigation.md#bindtoscrollable)/[bindToNestedScrollable](ui-design-hdsnavigation.md#bindtonestedscrollable)体验更佳的滑动效果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [DynamicHideParams](ui-design-hdsnavigation.md#dynamichideparams) | 是 | 标题栏跟随内容区滚动动态显隐配置。  当配置了标题栏动态显隐时，不支持配置标题栏模式动态切换。  当标题栏模式为HdsNavDestinationTitleMode.MODAL时该接口设置无效。  不支持在显隐过程中动态切换属性。 |

### bindToScrollable

PhonePC/2in1TabletTV

bindToScrollable(scrollers: Array<Scroller>)

绑定导航组件和可滚动容器组件，动态显隐标题区域，状态栏及底部自定义区域，使能动态显隐更优体验。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scrollers | Array<[Scroller](ts-container-scroll.md#scroller)> | 是 | 可滚动容器组件的控制器。 |

### bindToNestedScrollable

PhonePC/2in1TabletTV

bindToNestedScrollable(scrollers: Array<NestedScrollInfo>)

绑定导航组件和嵌套的可滚动容器组件，动态显隐标题区域，状态栏及底部自定义区域，使能动态显隐更优体验。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scrollers | Array<[NestedScrollInfo](ui-design-hdsnavigation.md#nestedscrollinfo)> | 是 | 嵌套的可滚动容器组件的控制器。 |

说明

当多个可滚动容器组件绑定了同一个导航组件时，滚动任何一个容器都会触发标题栏显示或隐藏效果。且当任何一个可滚动容器组件滑动到底部或顶部位置时，会立即触发标题栏显示动效。

因此，为了获得最佳用户体验，不建议同时触发多个可滚动容器组件的滚动事件。

### systemTransition

PhonePC/2in1TabletTV

systemTransition(type: NavigationSystemTransitionType)

设置HdsNavDestination系统转场动画，支持分别设置系统标题栏动画和内容动画。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [NavigationSystemTransitionType](ts-basic-components-navdestination.md#navigationsystemtransitiontype14枚举说明) | 是 | 系统转场动画类型。  默认值：NavigationSystemTransitionType.DEFAULT。 |

### customTransition

PhonePC/2in1TabletTV

customTransition(delegate: NavDestinationTransitionDelegate)

设置HdsNavDestination自定义转场动画。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| delegate | [NavDestinationTransitionDelegate](ts-basic-components-navdestination.md#navdestinationtransitiondelegate15) | 是 | HdsNavDestination自定义动画的代理函数。 |

### titleMode

PhonePC/2in1TabletTV

titleMode(value: HdsNavDestinationTitleMode)

设置页面标题栏显示模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [HdsNavDestinationTitleMode](ui-design-hdsnavdestination.md#hdsnavdestinationtitlemode) | 是 | 页面标题栏显示模式。默认值：HdsNavDestinationTitleMode.MINI。 |

### withTheme

PhonePC/2in1TabletTV

withTheme(value: WithThemeOptions)

设置HdsNavDestination的[WithTheme](ts-container-with-theme.md)能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.1.0(23)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [WithThemeOptions](ui-design-hdsnavigation.md#withthemeoptions) | 是 | WithTheme能力配置信息。 |

## 事件

PhonePC/2in1TabletTV

### onShown

PhonePC/2in1TabletTV

onShown(callback: Callback<void>)

当显示HdsNavDestination页面时，触发onShown回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void> | 是 | 当该HdsNavDestination页面显示时触发的回调。 |

### onShown

PhonePC/2in1TabletTV

onShown(callback: Callback<VisibilityChangeReason>)

当显示HdsNavDestination页面时，触发onShown回调。通过[VisibilityChangeReason](ts-basic-components-navdestination.md#visibilitychangereason21)说明触发的原因。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.1.0(23)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<[VisibilityChangeReason](ts-basic-components-navdestination.md#visibilitychangereason21)> | 是 | 当该HdsNavDestination页面显示时触发的回调。回调会提供入参VisibilityChangeReason以说明onShown触发的原因。 |

### onHidden

PhonePC/2in1TabletTV

onHidden(callback: Callback<void>)

当隐藏HdsNavDestination页面时，触发onHidden回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void> | 是 | 当该HdsNavDestination页面隐藏时触发的回调。 |

### onHidden

PhonePC/2in1TabletTV

onHidden(callback: Callback<VisibilityChangeReason>)

当隐藏HdsNavDestination页面时, 触发onHidden回调。通过[VisibilityChangeReason](ts-basic-components-navdestination.md#visibilitychangereason21)说明触发的原因。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.1.0(23)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<[VisibilityChangeReason](ts-basic-components-navdestination.md#visibilitychangereason21)> | 是 | 当该HdsNavDestination页面隐藏时触发的回调。回调会提供入参VisibilityChangeReason以说明onHidden触发的原因。 |

### onReady

PhonePC/2in1TabletTV

onReady(callback: Callback<NavDestinationContext>)

当HdsNavDestination即将构建子组件之前会触发此回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<[NavDestinationContext](ts-basic-components-navdestination.md#navdestinationcontext11)> | 是 | 当该HdsNavDestination即将构建子组件之前会触发的回调。 |

### onWillAppear

PhonePC/2in1TabletTV

onWillAppear(callback: Callback<void>)

当该HdsNavDestination挂载之前触发此回调。在该回调中允许修改页面栈，当前帧生效。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void> | 是 | 当该HdsNavDestination挂载之前触发的回调。 |

### onWillDisappear

PhonePC/2in1TabletTV

onWillDisappear(callback: Callback<void>)

当该HdsNavDestination卸载之前触发的生命周期（有转场动画时，在转场动画开始之前触发）。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void> | 是 | 当该HdsNavDestination卸载之前触发的生命周期（有转场动画时，在转场动画开始之前触发）。 |

### onWillShow

PhonePC/2in1TabletTV

onWillShow(callback: Callback<void>)

当该HdsNavDestination显示之前触发此回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void> | 是 | 当该HdsNavDestination显示之前触发的回调。 |

### onWillHide

PhonePC/2in1TabletTV

onWillHide(callback: Callback<void>)

当该HdsNavDestination隐藏之前触发此回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void> | 是 | 当该HdsNavDestination隐藏之前触发的回调。 |

### onBackPressed

PhonePC/2in1TabletTV

onBackPressed(callback: Callback<void, boolean>)

当与HdsNavigation绑定的页面栈中存在内容时，此回调生效。当点击返回键时，触发该回调。

返回值为true时，表示重写返回键逻辑，返回值为false时，表示回退到上一个页面。不推荐同时设置返回键自定义事件与onBackPressed回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void, boolean> | 是 | 当与HdsNavigation绑定的页面栈中存在内容时，并且点击返回键时，触发的回调。 |

### onActive

PhonePC/2in1TabletTV

onActive(callback: Optional<Callback<NavDestinationActiveReason>>)

HdsNavDestination处于激活态（处于栈顶可操作，且上层无特殊组件遮挡）时，触发该回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.1(21)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Callback](ts-types.md#callback12)<[NavDestinationActiveReason](ts-basic-components-navdestination.md#navdestinationactivereason17)>> | 是 | HdsNavDestination由非激活态变为激活态的原因。 |

### onInactive

PhonePC/2in1TabletTV

onInactive(callback: Optional<Callback<NavDestinationActiveReason>>)

HdsNavDestination处于非激活态（处于非栈顶不可操作，或处于栈顶时上层有特殊组件遮挡）时，触发该回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.1(21)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Callback](ts-types.md#callback12)<[NavDestinationActiveReason](ts-basic-components-navdestination.md#navdestinationactivereason17)>> | 是 | HdsNavDestination由激活态变为非激活态的原因。 |

## HdsNavDestinationTitleMode

PhonePC/2in1TabletTV

标题栏显示模式枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MINI | 100 | 固定为小标题模式。标题栏高度为56vp。 |
| MODAL | 101 | 固定为半模态模式。背板高度64vp，标题栏高度为56vp，上padding为8vp。 |

## 示例

PhonePC/2in1TabletTV

通过titleBar属性，自定义设置标题栏随内容区滚动的动态模糊样式。

```
1. // 从6.0.2(22)版本开始，无需手动导入HdsNavDestinationAttribute。具体请参考HdsNavDestination的导入模块说明。
2. import { HdsNavDestination, HdsNavDestinationAttribute, ScrollEffectType } from '@kit.UIDesignKit';
3. import { LengthMetrics } from '@kit.ArkUI';

5. const TITLE_BAR_HEIGHT_MINI: number = 56;

7. @Entry
8. @Component
9. struct PageOne {
10. scroller: Scroller = new Scroller();

12. build() {
13. HdsNavDestination() {
14. Scroll(this.scroller) {
15. Column() {
16. Blank().height(TITLE_BAR_HEIGHT_MINI)
17. Image($r('app.media.scenery')).width('100%') // scenery为自定义资源，开发者需替换本地资源
18. }
19. }.edgeEffect(EdgeEffect.Spring).scrollBar(BarState.Off)
20. }
21. .titleBar({
22. padding: {
23. start: LengthMetrics.vp(2),
24. end: LengthMetrics.vp(2)
25. },
26. style: {
27. scrollEffectOpts: {
28. enableScrollEffect: true,
29. scrollEffectType: ScrollEffectType.COMMON_BLUR,
30. blurEffectiveStartOffset: LengthMetrics.vp(0),
31. blurEffectiveEndOffset: LengthMetrics.vp(20)
32. },
33. originalStyle: {
34. backgroundStyle: {
35. backgroundColor: $r('sys.color.ohos_id_color_background'),
36. },
37. contentStyle: {
38. titleStyle: { mainTitleColor: $r('sys.color.font_primary'), subTitleColor: $r('sys.color.font_secondary') },
39. menuStyle: {
40. backgroundColor: $r('sys.color.comp_background_tertiary'),
41. iconColor: $r('sys.color.icon_primary')
42. },
43. backIconStyle: {
44. backgroundColor: $r('sys.color.comp_background_tertiary'),
45. iconColor: $r('sys.color.icon_primary')
46. }
47. }
48. },
49. scrollEffectStyle: {
50. backgroundStyle: {
51. backgroundColor: $r('sys.color.ohos_id_color_background_transparent'),
52. },
53. contentStyle: {
54. titleStyle: { mainTitleColor: $r('sys.color.font_primary'), subTitleColor: $r('sys.color.font_secondary') },
55. menuStyle: {
56. backgroundColor: $r('sys.color.comp_background_tertiary'),
57. iconColor: $r('sys.color.icon_primary')
58. },
59. backIconStyle: {
60. backgroundColor: $r('sys.color.comp_background_tertiary'),
61. iconColor: $r('sys.color.icon_primary')
62. }
63. }
64. }
65. },
66. content: {
67. title: {
68. mainTitle: "PageOne",
69. },
70. menu: {
71. value: [{
72. content: {
73. label: 'menu1',
74. icon: 'resources/base/media/startIcon.png',
75. isEnabled: true,
76. action: () => {
77. console.info("HdsNavDestination menu1");
78. }
79. }
80. }, {
81. content: {
82. label: 'menu2',
83. icon: 'resources/base/media/startIcon.png',
84. isEnabled: true,
85. action: () => {
86. console.info("HdsNavDestination menu2");
87. }
88. }
89. }]
90. },
91. }
92. })
93. .systemBarStyle({ statusBarContentColor: '#0A59F7' }, { statusBarContentColor: '#C7C7CD' })
94. .hideBackButton(false)
95. }
96. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/44ML8eGmSj2u31Y_6pua5g/zh-cn_image_0000002552800876.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000639Z&HW-CC-Expire=86400&HW-CC-Sign=F8A2E947D222DDA694363DA0707CE131E6374F536B717C8BC03361701BBF9AEF "点击放大")

HdsNavDestination更多示例可以参考HdsNavigation[示例](ui-design-hdsnavigation.md#示例)。
