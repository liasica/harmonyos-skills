---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation
title: HdsNavigation
breadcrumb: API参考 > 应用框架 > UI Design Kit（UI设计套件） > ArkTS组件 > HdsNavigation
category: harmonyos-references
scraped_at: 2026-04-28T08:06:42+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:1b201134e9347f93ad2da0f516115d158d78cdf49ceb6a33244b4c56232c6790
---

本模块提供导航组件的能力，默认支持标题栏随内容区滚动的动态模糊样式。6.0.0(20)版本以后，推荐使用[bindToScrollable](ui-design-hdsnavigation.md#bindtoscrollable)、[bindToNestedScrollable](ui-design-hdsnavigation.md#bindtonestedscrollable)属性绑定导航组件和可滚动容器组件后，再使用导航组件滚动相关的功能，从而获得更优的体验。如滚动生效动态模糊样式，标题栏随内容区滚动动态显隐功能等。

HdsNavigation组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏。其中内容区默认首页显示导航内容（HdsNavigation的子组件）或非首页显示（[HdsNavDestination](ui-design-hdsnavdestination.md)的子组件），首页和非首页通过路由进行切换。

**起始版本：** 5.1.0(18)

## 导入模块

PhonePC/2in1TabletTV

说明

* HdsNavigationAttribute是用于配置HdsNavigation组件属性的关键接口。6.0.1(21)及之前版本，导入HdsNavigation组件后需要开发者手动导入HdsNavigationAttribute，否则会编译报错。从6.0.2(22)版本开始，编译工具链识别到导入HdsNavigation组件后，会自动导入HdsNavigationAttribute，无需开发者手动导入。
* 如果开发者手动导入HdsNavigationAttribute，DevEco Studio会显示置灰，6.0.1(21)及之前版本删除会编译报错，从6.0.2(22)版本开始，删除对功能无影响。

6.0.1(21)及之前版本：

```
1. import { HdsNavigation, HdsNavigationAttribute } from '@kit.UIDesignKit';
```

6.0.2(22)及之后版本：

```
1. import { HdsNavigation } from '@kit.UIDesignKit';
```

## 子组件

PhonePC/2in1TabletTV

可以包含子组件。 推荐使用[NavPathStack](ts-basic-components-navigation.md#navpathstack10)配合[HdsNavDestination](ui-design-hdsnavdestination.md)属性进行页面路由。

## 接口

PhonePC/2in1TabletTV

HdsNavigation(pathInfos?: NavPathStack)

绑定路由栈到HdsNavigation组件。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pathInfos | [NavPathStack](ts-basic-components-navigation.md#navpathstack10) | 否 | 路由栈信息。 |

## 属性

PhonePC/2in1TabletTV

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### titleBar

PhonePC/2in1TabletTV

titleBar(options?: HdsNavigationTitleBarOptions)

设置HdsNavigation组件titleBar区域（包含返回图标区域、标题区域、菜单区域、背景板）样式以及内容。

标题字符串超长时，如果不设置副标题，先缩小再换行（2行）最后以"..."截断。如果设置副标题，先缩小后以"..."截断。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [HdsNavigationTitleBarOptions](ui-design-hdsnavigation.md#hdsnavigationtitlebaroptions) | 否 | 标题栏配置信息。 |

### titleMode

PhonePC/2in1TabletTV

titleMode(value: HdsNavigationTitleMode)

设置页面标题栏显示模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [HdsNavigationTitleMode](ui-design-hdsnavigation.md#hdsnavigationtitlemode) | 是 | 页面标题栏显示模式。  默认值：HdsNavigationTitleMode.FREE。 |

### toolbarConfiguration

PhonePC/2in1TabletTV

toolbarConfiguration(value: Array<ToolbarItem> | CustomBuilder, options?: NavigationToolbarOptions)

说明

不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

设置工具栏内容。不设置时不显示工具栏。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<[ToolbarItem](ts-basic-components-navigation.md#toolbaritem10)> | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 工具栏内容。  使用Array<[ToolbarItem](ts-basic-components-navigation.md#toolbaritem10)>写法设置的工具栏有如下特性：  - 如果为[Stack](ts-basic-components-navigation.md#navigationmode9枚举说明)模式，不推荐使用该写法。推荐使用[CustomBuilder](ts-types.md#custombuilder8)配合[ToolBar](ohos-arkui-advanced-toolbar.md)组件写法，避免布局显示问题。  - 工具栏所有选项均分底部工具栏，在每个均分内容区布局文本和图标。  - 文本超长时，若工具栏选项个数小于5个，优先拓展选项的宽度，最大宽度与屏幕等宽，其次逐级缩小，缩小之后换行，最后截断。  - 最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。  使用[CustomBuilder](ts-types.md#custombuilder8)写法为用户自定义工具栏选项，除均分底部工具栏外不具备以上功能。 |
| options | [NavigationToolbarOptions](ts-basic-components-navigation.md#navigationtoolbaroptions11) | 否 | 工具栏选项。 |

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
| hide | boolean | 是 | 是否隐藏工具栏。  默认值：false。  - true： 隐藏工具栏。  - false：显示工具栏。 |
| animated | boolean | 否 | 设置是否使用动画显隐工具栏。  默认值：false。  - true：使用动画显示隐藏工具栏。  - false：不使用动画显示隐藏工具栏。 |

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

设置是否隐藏标题栏中的返回键。返回键仅针对[titleMode](ui-design-hdsnavigation.md#titlemode)为HdsNavigationTitleMode.MINI时才生效。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否隐藏标题栏中的返回键。  默认值：false。  - true：隐藏返回键。  - false：显示返回键。 |

### navBarWidth

PhonePC/2in1TabletTV

navBarWidth(value: Length)

设置导航栏宽度。仅在HdsNavigation组件分栏时生效。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 导航栏宽度。  默认值：240。单位：vp。  undefined：行为不做处理，导航栏宽度与默认值保持一致。 |

### navBarPosition

PhonePC/2in1TabletTV

navBarPosition(value: NavBarPosition)

设置导航栏位置。仅在HdsNavigation组件分栏时生效。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [NavBarPosition](ts-basic-components-navigation.md#navbarposition9枚举说明) | 是 | 导航栏位置。  默认值：NavBarPosition.Start。 |

### mode

PhonePC/2in1TabletTV

mode(value: NavigationMode)

设置导航栏的显示模式。支持Stack、Split与Auto模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [NavigationMode](ts-basic-components-navigation.md#navigationmode9枚举说明) | 是 | 导航栏的显示模式。  默认值：NavigationMode.Auto。  自适应：基于组件宽度自适应单栏和双栏。 |

### divider

PhonePC/2in1TabletTV

divider(style: NavigationDividerStyle | null)

设置HdsNavigation双栏模式下的分割线样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [NavigationDividerStyle](ts-basic-components-navigation.md#navigationdividerstyle23) | null | 是 | 设置双栏分割线样式。  配置为null时：隐藏分割线。 |

### hideNavBar

PhonePC/2in1TabletTV

hideNavBar(value: boolean)

设置是否隐藏导航栏。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否隐藏导航栏。设置为false时，不隐藏导航栏。设置为true时，隐藏HdsNavigation的导航栏，包括标题栏、内容区和工具栏。如果此时路由栈中存在HdsNavDestination页面，则直接显示栈顶HdsNavDestination页面，反之显示空白。  默认值：false。 |

### navDestination

PhonePC/2in1TabletTV

navDestination(builder: NavDestinationBuilder)

创建HdsNavDestination组件。使用builder函数，基于name和pageInfos构造HdsNavDestination组件。builder下只能有一个根节点。builder中允许在HdsNavDestination组件外包含一层自定义组件， 但自定义组件不允许设置属性和事件，否则仅显示空白。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | [NavDestinationBuilder](ui-design-hdsnavigation.md#navdestinationbuilder) | 是 | 创建HdsNavDestination组件。 |

### navBarWidthRange

PhonePC/2in1TabletTV

navBarWidthRange(value: NavBarWidthRangeOptions)

设置导航栏最小和最大宽度（双栏模式下生效）。

**规则：** 优先级规则详见[minContentWidth](ui-design-hdsnavigation.md#mincontentwidth)属性的说明。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [NavBarWidthRangeOptions](ui-design-hdsnavigation.md#navbarwidthrangeoptions) | 是 | 导航栏最小和最大宽度配置。 |

### minContentWidth

PhonePC/2in1TabletTV

minContentWidth(value: Dimension)

设置导航栏内容区最小宽度（双栏模式下生效）。

**规则：** 优先级规则详见说明。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](ts-types.md#dimension10) | 是 | 导航栏内容区最小宽度。  默认值：360。单位：vp。  undefined：行为不做处理，导航栏内容区最小宽度与默认值保持一致。 |

说明

1. 仅设置navBarWidth时，不支持HdsNavigation分割线拖拽。
2. navBarWidthRange指定分割线可以拖拽范围。如果不设置值，则按照默认值处理。拖拽范围需要满足navBarWidthRange设置的范围和minContentWidth限制。
3. HdsNavigation显示范围缩小顺序：a. 缩小内容区大小。如果不设置minContentWidth属性，则可以缩小内容区至0， 否则最小缩小至minContentWidth。b. 缩小导航栏大小，缩小时需要满足导航栏宽度大于navBarRange的下限。c. 对显示内容进行裁切。

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

设置LayoutSafeAreaType.SYSTEM时，组件的边界与非安全区域重合时组件能够延伸到非安全区域下。例如：设备顶部状态栏高度100，组件在屏幕中纵向方位的绝对偏移需要在0到100之间。

若组件延伸到非安全区域内，此时在非安全区域里触发的事件（例如：点击事件）等可能会被系统拦截，优先响应状态栏等系统组件。

### systemBarStyle

PhonePC/2in1TabletTV

systemBarStyle(originalStyle: Optional<SystemBarStyle>, scrollEffectStyle: Optional<SystemBarStyle>)

当HdsNavigation中显示HdsNavigation首页时，设置对应系统状态栏的样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| originalStyle | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[SystemBarStyle](arkts-apis-window-i.md#systembarstyle12)> | 是 | 系统状态栏初始样式。未设置systemBarStyle属性时，颜色默认值同主标题栏字体颜色。 |
| scrollEffectStyle | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[SystemBarStyle](arkts-apis-window-i.md#systembarstyle12)> | 是 | HdsNavigation动态样式生效后，系统状态栏对应的动态样式。未设置systemBarStyle属性时，颜色默认值同主标题栏字体颜色。 |

说明

1. 不建议混合使用systemBarStyle属性和window设置状态栏样式的相关接口，例如：[setWindowSystemBarProperties](arkts-apis-window-window.md#setwindowsystembarproperties9)。
2. [Split](ts-basic-components-navigation.md#navigationmode9枚举说明)模式下的HdsNavigation，如果内容区没有HdsNavDestination，则遵从HdsNavigation首页的设置，反之则遵从栈顶HdsNavDestination的设置。
3. 仅支持在主窗口的主页面中使用systemBarStyle设置状态栏样式。
4. 当页面设置不同样式时，在页面转场开始时生效。
5. 非全屏窗口下，HdsNavigation/HdsNavDestination设置的状态栏不生效。

### recoverable

PhonePC/2in1TabletTV

recoverable(recoverable: Optional<boolean>)

配置HdsNavigation是否可恢复。如配置为可恢复，当应用进程异常退出并重新冷启动时，可自动创建该HdsNavigation，并恢复至异常退出时的页面栈。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recoverable | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | HdsNavigation是否可恢复，默认为不可恢复。  默认值：false。  - true：页面栈可恢复。  - false：页面栈不可恢复。 |

说明

使用该接口需要先设置HdsNavigation的[id属性](ts-universal-attributes-component-id.md#id)，否则该接口无效。

该接口需要配合HdsNavDestination的[recoverable](ui-design-hdsnavdestination.md#recoverable)接口使用。

恢复的过程中不可序列化的信息，例如不可序列化的参数与用户设置的onPop等，会被丢弃，无法恢复。

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
| value | [DynamicHideParams](ui-design-hdsnavigation.md#dynamichideparams) | 是 | 标题栏跟随内容区滚动动态显隐配置。  当标题栏模式为HdsNavigationTitleMode.MODAL时该接口设置无效。  不支持在显隐过程中动态切换属性。 |

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

绑定导航组件和嵌套的可滚动容器组件，动态显隐标题区域、状态栏及底部自定义区域，使能动态显隐更优体验。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scrollers | Array<[NestedScrollInfo](ui-design-hdsnavigation.md#nestedscrollinfo)> | 是 | 嵌套的可滚动容器组件的控制器。 |

说明

当多个可滚动容器组件绑定了同一个导航组件时，滚动任何一个容器都会触发标题栏显示或隐藏效果。且当任何一个可滚动容器组件滑动到底部或顶部位

置时，会立即触发标题栏显示动效。因此，为了获得最佳用户体验，不建议同时触发多个可滚动容器组件的滚动事件。

### enableDragBar

PhonePC/2in1TabletTV

enableDragBar(isEnabled: Optional<boolean>)

控制分栏场景下是否显示拖拽条。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否开启拖拽条，默认为无拖拽条样式。  默认值：false。  - true：有拖拽条样式。  - false：无拖拽条样式。 |

### enableModeChangeAnimation

PhonePC/2in1TabletTV

enableModeChangeAnimation(isEnabled: Optional<boolean>)

控制是否开启[NavigationMode](ts-basic-components-navigation.md#navigationmode9枚举说明)单双栏切换时的动效。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否开启单双栏切换动效。  默认值：true。  - true：开启单双栏切换动效。  - false：关闭单双栏切换动效。 |

### withTheme

PhonePC/2in1TabletTV

withTheme(value: WithThemeOptions)

设置HdsNavigation的[WithTheme](ts-container-with-theme.md)能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.1.0(23)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [WithThemeOptions](ui-design-hdsnavigation.md#withthemeoptions) | 是 | WithTheme能力配置信息。 |

### splitPlaceholder

PhonePC/2in1TabletTV

splitPlaceholder(placeholder: ComponentContent)

HdsNavigation双栏模式下，支持设置右侧页面显示默认占位页，占位页仅作为UI展示页，不可获焦和响应事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.1.0(23)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| placeholder | [ComponentContent](js-apis-arkui-componentcontent.md) | 是 | 设置Navigation双栏模式下右侧的默认占位页。 |

### enableVisibilityLifecycleWithContentCover

PhonePC/2in1TabletTV

enableVisibilityLifecycleWithContentCover(isEnabled: Optional<boolean>)

设置是否启用HdsNavDestination页面的[onHidden](ui-design-hdsnavdestination.md#onhidden)、[onShown](ui-design-hdsnavdestination.md#onshown)生命周期与全模态的联动触发。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.1.0(23)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否启用HdsNavDestination页面onShown、onHidden生命周期与全模态的联动触发。  默认值：true。  - true：全模态拉起时，会触发当前HdsNavDestination页面的onHidden生命周期；全模态关闭时，会触发当前HdsNavDestination页面的onShown生命周期。  - false：HdsNavDestination页面onHidden、onShown生命周期不会因为全模态的拉起、关闭而触发。 |

## 事件

PhonePC/2in1TabletTV

### onNavBarStateChange

PhonePC/2in1TabletTV

onNavBarStateChange(callback: Callback<boolean>)

导航栏显示状态切换时触发该回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callBack | [Callback](ts-types.md#callback12)<boolean> | 是 | 参数为true时表示显示导航栏，为false时表示隐藏导航栏。 |

### onNavigationModeChange

PhonePC/2in1TabletTV

onNavigationModeChange(callback: Callback<NavigationMode>)

当HdsNavigation首次显示或者单双栏状态发生变化时触发该回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<[NavigationMode](ts-basic-components-navigation.md#navigationmode9枚举说明)> | 是 | - 参数为NavigationMode.Split时：当前HdsNavigation显示为双栏。  - 参数为NavigationMode.Stack时：当前HdsNavigation显示为单栏。 |

### onTitleModeChange

PhonePC/2in1TabletTV

onTitleModeChange(callback: Callback<HdsNavigationTitleMode>)

当titleMode为HdsNavigationTitleMode.FREE时，随着可滚动组件的滑动标题栏模式发生变化时触发此回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<[HdsNavigationTitleMode](ui-design-hdsnavigation.md#hdsnavigationtitlemode)> | 是 | 参数为标题栏显示模式。 |

### customNavContentTransition

PhonePC/2in1TabletTV

customNavContentTransition(delegate: CustomTransitionDelegate)

自定义转场动画回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| delegate | [CustomTransitionDelegate](ui-design-hdsnavigation.md#customtransitiondelegate) | 是 | 自定义转场动画回调方法。 |

## ScrollEffectType

PhonePC/2in1TabletTV

标题栏模糊样式枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COMMON\_BLUR | 0 | 标题栏的模糊样式类型：通用模糊。  对组件背景进行均匀的模糊处理，模糊强度一致，边界清晰，用于强调控件与内容的层级分隔。  滑动内容进入/离开标题栏区域过程中，模糊背板和分割线透明渐变出现/消失。此方式适用于非沉浸式场景。 |
| GRADUAL\_BLUR | 1 | 标题栏的模糊样式类型：过渡模糊。  对组件背景进行均匀的模糊处理，模糊强度一致，边界清晰，用于强调控件与内容的层级分隔。  滑动前后标题栏内容发生颜色/状态变化，滑动过程中，线性跟手变化。此样式适用于沉浸式图文类的场景。  **起始版本：** 6.0.0(20) |
| GRADIENT\_BLUR | 2 | 标题栏的模糊样式类型：渐变模糊。  模糊效果在空间维度上呈现渐强/渐弱的变化，模糊边界柔和，用于增强页面沉浸感。  - 当[ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions).enableScrollEffect属性配置为true时，标题栏样式从[originalStyle](ui-design-hdsnavigation.md#titlebarstyleoptions)到[scrollEffectStyle](ui-design-hdsnavigation.md#titlebarstyleoptions)线性过渡。  - 当[ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions).enableScrollEffect属性配置为false时，直接生效模糊。此方式适用于列表型非沉浸式场景。  **起始版本：** 6.0.0(20) |
| IMMERSIVE\_GRADIENT\_BLUR | 3 | 标题栏的模糊样式类型：沉浸式渐变模糊。  模糊效果在空间维度上呈现渐强/渐弱的变化，模糊边界柔和，用于增强页面沉浸感。  - 当[ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions).enableScrollEffect属性配置为true时，标题栏样式从[originalStyle](ui-design-hdsnavigation.md#titlebarstyleoptions)到[scrollEffectStyle](ui-design-hdsnavigation.md#titlebarstyleoptions)线性过渡。  - 当[ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions).enableScrollEffect属性配置为false时，直接生效模糊。此样式适用于沉浸式图文类的场景。  **起始版本：** 6.1.0(23) |

## HdsNavigationTitleMode

PhonePC/2in1TabletTV

标题栏显示模式枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FREE | 0 | 标题随着内容向上滚动而缩小（子标题的大小不变、淡出）。向下滚动内容到顶时则恢复原样。  未滚动状态，标题栏高度与FULL模式一致；滚动时，标题栏的最小高度与MINI模式一致。  推荐搭配[bindToScrollable](ui-design-hdsnavigation.md#bindtoscrollable)/[bindToNestedScrollable](ui-design-hdsnavigation.md#bindtonestedscrollable)体验更佳的联动效果。 |
| FULL | 1 | 固定为大标题模式。  默认值：只有主标题时，标题栏高度为112vp；同时有主标题和副标题时，标题栏高度为138vp。 |
| MINI | 2 | 固定为小标题模式。标题栏高度为56vp。 |
| MODAL | 3 | 固定为半模态模式。  - 一级页面只有主标题时，背板高度64vp，标题栏高度为56vp，上padding为8vp。  - 一级页面有主标题和副标题时，背板高度为80vp，标题栏为72vp，上padding为8vp。  **起始版本：** 6.0.0(20) |

## DividerShowType

PhonePC/2in1TabletTV

分割线显示类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OFF | 0 | 分割线始终不显示。 |
| ON | 1 | 分割线始终显示。 |
| AUTO | 2 | 分割线随内容区滚动跟手显示。 |

## TextStyleMode

PhonePC/2in1TabletTV

文字型图标模式枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 200 | 普通文本模式。  胶囊按钮，圆角为sys.float.corner\_radius\_level10。 |
| SINGLE\_CHARACTER | 201 | 单字文本模式。  圆形按钮。 |

## BottomBuilderShowType

PhonePC/2in1TabletTV

bottomBuilder显示类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DIRECTLY\_SHOW | 0 | 直接显示bottomBuilder。 |
| OVERDRAG\_SHOW | 1 | 过度拖拽场景下，显示bottomBuilder。 |

## HideMode

PhonePC/2in1TabletTV

标题栏动态显隐模式枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCROLL\_UP\_TO | 0 | 上滑到固定位置隐藏，下滑到固定位置显示。 |
| SCROLL\_UP | 1 | 任意位置上滑隐藏，下滑显示。仅针对连续滑动场景生效，使用滚动组件接口触发的滚动不生效该隐藏模式。 |
| SCROLL\_DOWN | 2 | 任意位置上滑显示，下滑隐藏。仅标题栏模式为HdsNavigationTitleMode.MINI或者HdsNavDestinationTitleMode.MINI时该配置生效。仅针对连续滑动场景生效，使用滚动组件接口触发的滚动不生效该隐藏模式。 |
| SCROLL\_UP\_TO\_BLEND\_SCROLL\_UP | 3 | 混合隐藏模式，bottomBuilder使用SCROLL\_UP\_TO隐藏模式，标题栏使用SCROLL\_UP隐藏模式。 |

## IconStyleMode

PhonePC/2in1TabletTV

图片型图标模式枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SMALL | 100 | 小图标模式，图标默认大小为18vp \* 18vp。 |
| NORMAL | 101 | 普通图标模式，图标默认大小为24vp \* 24vp。 |
| LARGE | 102 | 大图标模式，图标默认大小为40vp \* 40vp。 |

## BlurStrategy

PhonePC/2in1TabletTV

模糊效果生效策略枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ENABLE | 0 | 使能模糊效果。 |
| DISABLE | 1 | 不使能模糊效果。 |
| ADAPTIVE | 2 | 模糊效果生效策略将根据系统策略进行调整。共设置三档系统策略：精美、轻柔、流畅，只有精美档位配置能够生效模糊效果。  系统策略由设备厂商根据设备性能配置，未配置时默认执行精美策略。 |

## TitleSize

PhonePC/2in1TabletTV

标题字号大小。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TITLE\_S | 0 | 小号标题。 |
| TITLE\_ML | 1 | 中等偏大号标题。 |

## NavDestinationBuilder

PhonePC/2in1TabletTV

type NavDestinationBuilder = (name: string, pageInfos: Object) => void

基于name和pageInfos构造HdsNavDestination组件的Builder方法。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 创建的HdsNavDestination页面的名称。 |
| pageInfos | Object | 是 | 创建的HdsNavDestination页面的详细参数。 |

## CustomTransitionDelegate

PhonePC/2in1TabletTV

type CustomTransitionDelegate = (from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => NavigationAnimatedTransition | undefined

自定义转场动画回调方法。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | [NavContentInfo](ts-basic-components-navigation.md#navcontentinfo11) | 是 | 退场Destination的页面。 |
| to | [NavContentInfo](ts-basic-components-navigation.md#navcontentinfo11) | 是 | 进场Destination的页面。 |
| operation | [NavigationOperation](ts-basic-components-navigation.md#navigationoperation11枚举说明) | 是 | 转场类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NavigationAnimatedTransition](ts-basic-components-navigation.md#navigationanimatedtransition11) | undefined | 自定义转场动画协议。  undefined：返回未定义，执行默认转场动效。 |

## IconType

PhonePC/2in1TabletTV

type IconType = ResourceStr | SymbolGlyphModifier | PixelMap

HdsNavigation标题栏上单个图标型菜单项支持的图片资源类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 类型 | 说明 |
| --- | --- |
| [ResourceStr](ts-types.md#resourcestr) | 字符串类型。 |
| [SymbolGlyphModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | symbol资源类型。 |
| [PixelMap](arkts-apis-image-pixelmap.md) | 图像像素类型。  **起始版本：** 6.0.0(20) |

## HdsNavigationMenuItemOptions

PhonePC/2in1TabletTV

type HdsNavigationMenuItemOptions = HdsNavigationBadgeIconOptions

HdsNavigation标题栏菜单项配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 类型 | 说明 |
| --- | --- |
| [HdsNavigationBadgeIconOptions](ui-design-hdsnavigation.md#hdsnavigationbadgeiconoptions) | 带信息提醒的图标配置信息。 |

## HdsNavigationBackButtonItemOptions

PhonePC/2in1TabletTV

type HdsNavigationBackButtonItemOptions = HdsNavigationIconOptions

HdsNavigation标题栏返回按钮配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 类型 | 说明 |
| --- | --- |
| [HdsNavigationIconOptions](ui-design-hdsnavigation.md#hdsnavigationiconoptions) | 图标配置信息。 |

## HdsNavigationBackgroundStyle

PhonePC/2in1TabletTV

HdsNavigation标题栏背景板样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 标题栏背景板背景色。  默认值：  模糊样式类型为COMMON\_BLUR或GRADUAL\_BLUR时，背景色默认值均为透明色。  模糊样式类型为GRADIENT\_BLUR时，背景色生效线性径向渐变色，具体默认值分以下场景：  - 若[ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions).enableScrollEffect为true，在[TitleBarStyleOptions](ui-design-hdsnavigation.md#titlebarstyleoptions).originalStyle中，backgroundColor默认值为透明色；在[TitleBarStyleOptions](ui-design-hdsnavigation.md#titlebarstyleoptions).scrollEffectStyle中，backgroundColor默认值为#99000000。  - 若[ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions).enableScrollEffect为false，仅在[TitleBarStyleOptions](ui-design-hdsnavigation.md#titlebarstyleoptions).originalStyle中，backgroundColor生效，默认值为透明色。  从6.1.0(23)开始，新增如下背景色默认规则：  当模糊样式类型为GRADIENT\_BLUR并已配置systemMaterialEffect，或者模糊类型为IMMERSIVE\_GRADIENT\_BLUR时，对应默认值如下：  - 若[ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions).enableScrollEffect为true，默认值为透明色；若[ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions).enableScrollEffect为false，默认值为$r('sys.color.comp\_background\_gray')。  - 仅当[ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions).enableScrollEffect为true时生效，默认值为r('sys.color.comp\_background\_gray')。 |
| maskExtraHeight | number | 否 | 是 | 标题栏模糊蒙层超出标题栏的额外高度。该配置只在模糊样式类型配置为GRADIENT\_BLUR时生效。单位：vp。  默认值：32。单位：vp。  **起始版本：** 6.0.0(20) |
| blurRadius | number | 否 | 是 | 标题栏模糊半径。仅在模糊样式类型配置为渐变模糊GRADIENT\_BLUR及沉浸式渐变模糊IMMERSIVE\_GRADIENT\_BLUR时生效。取值范围为[0.0, 128.0]。超出取值范围时，按默认值处理。  默认值：  - 作为[TitleBarStyleOptions](ui-design-hdsnavigation.md#titlebarstyleoptions).originalStyle中的属性时，当[ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions).enableScrollEffect为true时，默认值为0.0；当[ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions).enableScrollEffect为false，未配置systemMaterialEffect时，默认值为16.0，配置systemMaterialEffect时，默认值为12.0。  - 作为[TitleBarStyleOptions](ui-design-hdsnavigation.md#titlebarstyleoptions).scrollEffectStyle中的属性时，仅在[ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions).enableScrollEffect为true时生效，未配置systemMaterialEffect时，默认值为16.0，配置systemMaterialEffect时，默认值为12.0。  **起始版本：** 6.1.0(23) |

## HdsNavigationTitleStyle

PhonePC/2in1TabletTV

HdsNavigation标题栏的标题样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mainTitleColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 标题栏主标题颜色。  默认值：  - 当模糊样式类型配置为COMMON\_BLUR时，主标题默认颜色为$r('sys.color.font\_primary')。  - 当模糊样式类型配置为GRADUAL\_BLUR时，动态样式生效前，主标题默认颜色为$r('sys.color.font\_on\_primary')，动态样式生效后，主标题默认颜色为$r('sys.color.font\_primary')。  - 当模糊样式类型配置为GRADIENT\_BLUR且[ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions).enableScrollEffect配置为false时，主标题默认颜色为$r('sys.color.font\_on\_primary')。  - 当模糊样式类型配置为GRADIENT\_BLUR且[ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions).enableScrollEffect配置为true时，动态样式生效前，主标题默认颜色为$r('sys.color.font\_primary')，动态样式生效后，主标题默认颜色为$r('sys.color.font\_on\_primary')。 |
| subTitleColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 标题栏副标题颜色。  默认值：  - 当模糊样式类型配置为COMMON\_BLUR时，副标题默认颜色为$r('sys.color.font\_secondary')。  - 当模糊样式类型配置为GRADUAL\_BLUR时，动态样式生效前，副标题默认颜色为$r('sys.color.font\_on\_secondary')，动态样式生效后，副标题默认颜色为$r('sys.color.font\_secondary')。  - 当模糊样式类型配置为GRADIENT\_BLUR且[ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions).enableScrollEffect配置为false时，副标题默认颜色为$r('sys.color.font\_on\_secondary')。  - 当模糊样式类型配置为GRADIENT\_BLUR且[ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions).enableScrollEffect配置为true时，动态样式生效前，副标题默认颜色为$r('sys.color.font\_secondary')，动态样式生效后，副标题默认颜色为$r('sys.color.font\_on\_secondary')。 |
| mainTitleShadowColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 标题栏主标题投影颜色，仅在配置systemMaterialEffect场景生效。  默认值为：$r('sys.color.comp\_background\_gary')。  **起始版本：** 6.1.0(23) |
| subTitleShadowColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 标题栏副标题投影颜色，仅在配置systemMaterialEffect场景生效。  默认值为：$r('sys.color.comp\_background\_gary')。  **起始版本：** 6.1.0(23) |

## HdsNavigationIconItemStyle

PhonePC/2in1TabletTV

HdsNavigation标题栏的图标样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 标题栏图标背景色。  默认值：  - 当模糊样式类型配置为COMMON\_BLUR时，图标背板默认色为$r('sys.color.comp\_background\_tertiary')。  - 当模糊样式类型配置为GRADUAL\_BLUR时，默认值为透明色，同时生效提亮压暗样式。  - 当模糊样式类型配置为GRADIENT\_BLUR且[ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions).enableScrollEffect配置为false时，默认值为透明色，同时生效提亮压暗样式。  - 当模糊样式类型配置为GRADIENT\_BLUR且[ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions).enableScrollEffect配置为true时，动态样式生效前，背景色默认值为$r('sys.color.comp\_background\_tertiary')，动态样式生效后，默认值为透明色，同时生效提亮压暗样式。 |
| iconColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 标题栏图标色。在配置了图标模式为[IconStyleMode](ui-design-hdsnavigation.md#iconstylemode)时生效。  默认值：  - 当模糊样式类型配置为COMMON\_BLUR时，默认值为$r('sys.color.icon\_primary')。  - 当模糊样式类型配置为GRADUAL\_BLUR时，在动态样式生效前，默认值为$r('sys.color.icon\_on\_primary')；动态样式生效后，默认值为$r('sys.color.icon\_primary')。  - 当模糊样式类型配置为GRADIENT\_BLUR且[ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions).enableScrollEffect配置为false时，默认值为$r('sys.color.icon\_on\_primary')。  - 当模糊样式类型配置为GRADIENT\_BLUR且[ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions).enableScrollEffect配置为true时，动态样式生效前，默认值为$r('sys.color.icon\_primary')，动态样式生效后，默认值为$r('sys.color.icon\_on\_primary')。 |
| textColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 标题栏图标文本色。在配置了图标模式为[TextStyleMode](ui-design-hdsnavigation.md#textstylemode)时生效。  默认值：  - 当模糊样式类型配置为COMMON\_BLUR时，默认值为$r('sys.color.font\_primary')。  - 当模糊样式类型配置为GRADUAL\_BLUR时，在动态样式生效前，默认值为$r('sys.color.font\_on\_primary')；动态样式生效后，默认值为$r('sys.color.font\_primary')。  - 当模糊样式类型配置为GRADIENT\_BLUR且[ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions).enableScrollEffect配置为false时，默认值为$r('sys.color.font\_on\_primary')。  - 当模糊样式类型配置为GRADIENT\_BLUR且[ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions).enableScrollEffect配置为true时，动态样式生效前，默认值为$r('sys.color.font\_primary')，动态样式生效后，默认值为$r('sys.color.font\_on\_primary')。  **起始版本：** 6.0.0(20) |

## HdsNavigationDividerStyle

PhonePC/2in1TabletTV

HdsNavigation标题栏的分割线样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dividerColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 标题栏分割线颜色。  默认值：$r('sys.color.comp\_divider')。 |

## HdsTitleBarContentStyle

PhonePC/2in1TabletTV

HdsNavigation标题栏的内容区样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| titleStyle | [HdsNavigationTitleStyle](ui-design-hdsnavigation.md#hdsnavigationtitlestyle) | 否 | 是 | 标题栏内容区标题样式。 |
| menuStyle | [HdsNavigationIconItemStyle](ui-design-hdsnavigation.md#hdsnavigationiconitemstyle) | 否 | 是 | 标题栏内容区菜单栏样式。 |
| backIconStyle | [HdsNavigationIconItemStyle](ui-design-hdsnavigation.md#hdsnavigationiconitemstyle) | 否 | 是 | 标题栏内容区返回图标样式。 |
| subIconStyle | [HdsNavigationIconItemStyle](ui-design-hdsnavigation.md#hdsnavigationiconitemstyle) | 否 | 是 | 标题栏内容区子图标样式。  **起始版本：** 6.0.0(20) |
| dividerStyle | [HdsNavigationDividerStyle](ui-design-hdsnavigation.md#hdsnavigationdividerstyle) | 否 | 是 | 标题栏内容区分割线样式。  **起始版本：** 6.0.0(20) |

## HdsNavigationTitleBarStyle

PhonePC/2in1TabletTV

HdsNavigation标题栏样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| backgroundStyle | [HdsNavigationBackgroundStyle](ui-design-hdsnavigation.md#hdsnavigationbackgroundstyle) | 否 | 是 | HdsNavigation标题栏背板样式。 |
| contentStyle | [HdsTitleBarContentStyle](ui-design-hdsnavigation.md#hdstitlebarcontentstyle) | 否 | 是 | HdsNavigation标题栏内容区样式。 |

## ScrollEffectOptions

PhonePC/2in1TabletTV

HdsNavigation标题栏的动态样式参数配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enableScrollEffect | boolean | 否 | 是 | 配置标题栏是否随内容区滚动的总偏移量动态生效标题栏样式。  默认值：true。  - true：内容区滚动的总偏移量从blurEffectiveStartOffset到blurEffectiveEndOffset，标题栏样式从[originalStyle](ui-design-hdsnavigation.md#titlebarstyleoptions)到[scrollEffectStyle](ui-design-hdsnavigation.md#titlebarstyleoptions)线性过渡。  - false：不随内容区滚动动态生效标题栏样式，仅生效[originalStyle](ui-design-hdsnavigation.md#titlebarstyleoptions)。 |
| scrollEffectType | [ScrollEffectType](ui-design-hdsnavigation.md#scrolleffecttype) | 否 | 是 | 标题栏模糊样式类型。  默认值：ScrollEffectType.COMMON\_BLUR。 |
| enableRefreshOffsetChange | boolean | 否 | 是 | 是否响应内容区Refresh组件的滚动。  默认值：true。  - true：随内容区Refresh组件的滚动变化生效对应的标题栏样式。  - false：不随内容区Refresh组件的滚动变化生效对应的标题栏样式。  **起始版本：** 6.1.0(23) |
| blurEffectiveStartOffset | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 动态样式线性过渡的起始位置。当内容区滚动的总偏移量超过该值时，标题栏开始从[originalStyle](ui-design-hdsnavigation.md#titlebarstyleoptions)到[scrollEffectStyle](ui-design-hdsnavigation.md#titlebarstyleoptions)线性过渡。  取值范围[0,+∞)。  默认值：LengthMetric.vp(0)。  超出取值范围时，按默认值处理。 |
| blurEffectiveEndOffset | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 动态样式线性过渡的终点位置。当内容区滚动的总偏移量超过该值时，标题栏的动态样式过渡结束，固定为[scrollEffectStyle](ui-design-hdsnavigation.md#titlebarstyleoptions)。  取值范围[0,+∞)。  若设置数值小于blurEffectiveStartOffset，按默认值处理。  默认值：  - 标题栏模糊样式类型设置为ScrollEffectType.COMMON\_BLUR或者ScrollEffectType.GRADIENT\_BLUR时，默认值为LengthMetric.vp(8)。  - 标题栏模糊样式类型设置为ScrollEffectType.GRADUAL\_BLUR，默认值为LengthMetric.vp(56)。 |

## TitleBarStyleOptions

PhonePC/2in1TabletTV

HdsNavigation标题栏的样式配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scrollEffectOpts | [ScrollEffectOptions](ui-design-hdsnavigation.md#scrolleffectoptions) | 否 | 是 | 标题栏的动态样式参数配置。 |
| originalStyle | [HdsNavigationTitleBarStyle](ui-design-hdsnavigation.md#hdsnavigationtitlebarstyle) | 否 | 是 | 设置标题栏的初始样式。 |
| scrollEffectStyle | [HdsNavigationTitleBarStyle](ui-design-hdsnavigation.md#hdsnavigationtitlebarstyle) | 否 | 是 | 设置标题栏随内容区滚动生效的终点样式。  如果设置的模糊参数与模糊样式类型不匹配时，按照模糊样式类型对应的默认样式生效。 |
| blurStrategy | [BlurStrategy](ui-design-hdsnavigation.md#blurstrategy) | 否 | 是 | 设置标题栏的模糊生效策略。  默认值：BlurStrategy.ADAPTIVE。  **起始版本：** 6.0.0(20) |
| thermoCtrl | boolean | 否 | 是 | 设置组件样式的生效策略是否跟随热管理档位[ThermalLevel](js-apis-thermal.md#thermallevel)信息管理。  默认值：false。  - true：跟随热管理档位信息生效组件样式，组件创建时，若ThermalLevel > OVERHEATED，关闭组件模糊效果。  - false：不跟随热管理档位信息生效组件样式。  **起始版本：** 6.1.0(23) |
| systemMaterialEffect | [SystemMaterialParams](ui-design-hdsnavigation.md#systemmaterialparams) | 否 | 是 | 设置标题栏沉浸光感样式。  **起始版本：** 6.1.0(23) |

## HdsNavigationBadgeOptions

PhonePC/2in1TabletTV

HdsNavigation标题栏的信息标记配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| count | number | 否 | 是 | 设置提醒信息数，大于99时，显示“99+”。  取值范围：[-2147483648,2147483647]。超出范围时会加上或减去4294967296，使得值仍在范围内，非整数时会舍去小数部分取整数部分。  默认值：-1。  设置为小于等于0时，不显示信息标记。 |
| value | string | 否 | 是 | 提示内容的文本字符串。  - 同时设置value和count属性时，优先显示开发者设置的value。  - 开发者不设置value时，信息标记按照count属性配置生效。  - value配置为空字符串时，信息标记显示为“小红点”。 |
| accessibilityText | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 标题栏信息标记的的无障碍文本属性。  当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。  默认值：""。  **起始版本：** 6.0.0(20) |

## HdsNavigationIconOptions

PhonePC/2in1TabletTV

HdsNavigation标题栏上图标配置信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [IconType](ui-design-hdsnavigation.md#icontype) | 否 | 是 | 图标型菜单项支持的图片资源类型。  不配置时，显示空白。 |
| label | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 图标型菜单项的文本。  默认值：""。 |
| isEnabled | boolean | 否 | 是 | 是否使能。  默认值：true。  - true：使能。  - false：未使能。 |
| action | [Callback](ts-types.md#callback12)<void> | 否 | 是 | 当前选项被选中的事件回调。 |
| componentId | string | 否 | 是 | 组件Id，组件的唯一标识，唯一性由使用者保证。  默认值：""。  **起始版本：** 6.0.0(20) |
| type | [IconStyleMode](ui-design-hdsnavigation.md#iconstylemode) | [TextStyleMode](ui-design-hdsnavigation.md#textstylemode) | 否 | 是 | 标题栏图标类型。当图标类型配置为TextStyleMode.NORMAL时，该图标不支持设置badge属性。  默认值：IconStyleMode.NORMAL。  **起始版本：** 6.0.0(20) |

## HdsNavigationBadgeIconOptions

PhonePC/2in1TabletTV

HdsNavigation标题栏上带信息提醒的图标配置信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | [HdsNavigationIconOptions](ui-design-hdsnavigation.md#hdsnavigationiconoptions) | 否 | 是 | 图标配置信息。 |
| badge | [HdsNavigationBadgeOptions](ui-design-hdsnavigation.md#hdsnavigationbadgeoptions) | 否 | 是 | 信息标记配置。 |

## HdsNavigationMenuContentOptions

PhonePC/2in1TabletTV

HdsNavigation标题栏的菜单区域内容配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | Array<[HdsNavigationMenuItemOptions](ui-design-hdsnavigation.md#hdsnavigationmenuitemoptions)> | 否 | 是 | 菜单栏的图标配置。 |
| maxCount | number | 否 | 是 | 菜单栏最多显示的图标个数，默认最多支持显示3个图标，多余的图标会被放入自动生成的更多图标。 |
| multiWindowEntryInAPPMenu | [MultiWindowEntryInAPPMenuParams](ui-design-hdsnavigation.md#multiwindowentryinappmenuparams) | 否 | 是 | 应用内多窗菜单栏配置。  **说明**：  依赖全景多窗特性，只有当前设备及屏幕状态支持全景多窗，才支持设置此功能。目前支持全景多窗的设备形态有：  - 双折叠：展开态。  - 三折叠：双屏态，三屏态的横屏态。  - 平板：横屏态。  对于不支持的设备形态，该组件不可交互，不响应点击事件。  **起始版本：** 6.0.0(20) |

## MultiWindowEntryInAPPMenuParams

PhonePC/2in1TabletTV

HdsNavigation标题栏的菜单区域应用内多窗配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 否 | 否 | 需要启动窗口的参数，有以下要求：  - 必填字段：abilityName, moduleName和bundleName；  - 应用限制：所有指定的名称（abilityName, moduleName 和bundleName）必须属于当前应用；  - 跨应用限制：多窗口功能不支持跨应用的能力。 |

## HdsNavigationTitle

PhonePC/2in1TabletTV

HdsNavigation标题栏的标题资源配置。字符串超长时，如果不设置副标题，先缩小再换行（2行）最后以"..."截断。如果设置副标题，先缩小最后以"..."截断。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mainTitle | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 设置标题栏主标题。 |
| subTitle | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置标题栏副标题。不设置时，不显示副标题。 |
| subTitleBuilder | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 是 | 设置副标题自定义区域。配置subTitle时，从subTitle尾部开始布局。该配置只在标题栏模式为HdsNavigationTitleMode.MODAL或者HdsNavDestinationTitleMode.MODAL时生效。  **起始版本：** 6.0.0(20) |
| subTitleComponent | [ComponentContent](js-apis-arkui-componentcontent.md) | 否 | 是 | 设置副标题自定义区域。配置subTitle时，从subTitle尾部开始布局。该配置只在标题栏模式为HdsNavigationTitleMode.MODAL或者HdsNavDestinationTitleMode.MODAL时生效。  当同时配置了subTitleBuilder属性与subTitleComponent属性时，生效subTitleComponent属性。  **起始版本：** 6.0.1(21) |
| mainTitleId | string | 否 | 是 | 设置主标题的组件ID。  默认值：""。  **起始版本：** 6.0.0(20) |
| subTitleId | string | 否 | 是 | 设置副标题的组件ID。  默认值：""。  **起始版本：** 6.0.0(20) |
| mainTitleAccessibilityText | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置主标题的无障碍文本。  **起始版本：** 6.1.0(23) |
| subTitleAccessibilityText | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置副标题的无障碍文本。  **起始版本：** 6.1.0(23) |
| mainTitleSize | [TitleSize](ui-design-hdsnavigation.md#titlesize) | 否 | 是 | 设置主标题字号。该配置只在标题栏模式为HdsNavigationTitleMode.MINI或者HdsNavDestinationTitleMode.MINI时生效。  **起始版本：** 6.1.0(23) |

## BottomBuilderParams

PhonePC/2in1TabletTV

HdsNavigation标题栏底部自定义区域配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| builder | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 否 | 设置标题底部自定义区域内容。 |
| builderComponent | [ComponentContent](js-apis-arkui-componentcontent.md) | 否 | 是 | 设置标题底部自定义区域内容。  当同时配置了builder属性与builderComponent属性时，生效builderComponent属性。  **起始版本：** 6.0.1(21) |
| height | [Length](ts-types.md#length) | 否 | 是 | 设置标题栏底部自定义区域高度。不支持设置百分比单位。  默认值：56vp。 |
| showType | [BottomBuilderShowType](ui-design-hdsnavigation.md#bottombuildershowtype) | 否 | 是 | 设置标题栏底部自定义区域显示类型。仅在HideMode配置为HideMode.SCROLL\_UP\_TO时，该配置生效。  默认值：BottomBuilderShowType.DIRECTLY\_SHOW。 |

## HdsNavigationDividerParams

PhonePC/2in1TabletTV

HdsNavigation标题栏分割线配置，该参数不支持动态切换。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| showType | [DividerShowType](ui-design-hdsnavigation.md#dividershowtype) | 否 | 是 | 设置标题栏分割线显示类型。  默认值：DividerShowType.AUTO。 |

## TitleBarContentOptions

PhonePC/2in1TabletTV

HdsNavigation标题栏的内容区配置信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | [HdsNavigationTitle](ui-design-hdsnavigation.md#hdsnavigationtitle) | 否 | 是 | 设置标题栏标题内容。 |
| menu | [HdsNavigationMenuContentOptions](ui-design-hdsnavigation.md#hdsnavigationmenucontentoptions) | 否 | 是 | 设置标题栏菜单栏内容。 |
| backIcon | [HdsNavigationBackButtonItemOptions](ui-design-hdsnavigation.md#hdsnavigationbackbuttonitemoptions) | 否 | 是 | 设置标题栏的返回按钮内容。 |
| stackBuilder | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 是 | 设置标题栏顶部自定义区域。  **起始版本：** 6.0.0(20) |
| stackBuilderComponent | [ComponentContent](js-apis-arkui-componentcontent.md) | 否 | 是 | 设置标题栏顶部自定义区域。  当同时配置了stackBuilder属性与stackBuilderComponent属性时，生效stackBuilderComponent属性。  **起始版本：** 6.0.1(21) |
| bottomBuilder | [BottomBuilderParams](ui-design-hdsnavigation.md#bottombuilderparams) | 否 | 是 | 设置标题栏底部自定义区域。  **起始版本：** 6.0.0(20) |
| divider | [HdsNavigationDividerParams](ui-design-hdsnavigation.md#hdsnavigationdividerparams) | 否 | 是 | 设置标题栏分割线内容。  **起始版本：** 6.0.0(20) |
| subIcon | [HdsNavigationBadgeIconOptions](ui-design-hdsnavigation.md#hdsnavigationbadgeiconoptions) | 否 | 是 | 设置标题栏子图标内容。  **起始版本：** 6.0.0(20) |

## PaddingOptions

PhonePC/2in1TabletTV

标题栏的内间距配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 标题栏起始端内间距。  默认值：页面宽度小于600vp时，默认值为16vp，页面宽度大于等于840vp时，默认值为32vp，其他场景默认值为24vp。 |
| end | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 标题栏结束端内间距。  默认值：页面宽度小于600vp时，默认值为16vp，页面宽度大于等于800vp时，默认值为32vp，其他场景默认值为24vp。 |

## NavBarWidthRangeOptions

PhonePC/2in1TabletTV

导航栏最大最小宽度配置信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| minWidth | [Dimension](ts-types.md#dimension10) | 否 | 是 | 导航栏最小宽度。  默认值：240vp。 |
| maxWidth | [Dimension](ts-types.md#dimension10) | 否 | 是 | 导航栏最大宽度。  默认值：组件宽度的40% ，且不大于 432，单位：vp。 |

## HdsNavigationTitleBarOptions

PhonePC/2in1TabletTV

HdsNavigation标题栏配置信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| padding | [PaddingOptions](ui-design-hdsnavigation.md#paddingoptions) | 否 | 是 | 标题栏内间距设置。 |
| style | [TitleBarStyleOptions](ui-design-hdsnavigation.md#titlebarstyleoptions) | 否 | 是 | 标题栏样式设置。 |
| content | [TitleBarContentOptions](ui-design-hdsnavigation.md#titlebarcontentoptions) | 否 | 是 | 标题栏内容区设置。 |
| enableHoverMode | boolean | 否 | 是 | 是否响应悬停态。  使用规则：  1. 需满足HdsNavigation为全屏大小；  2. 标题栏显示模式为HdsNavigationTitleMode.FREE时此接口设置无效。  默认值：false。  - true：响应悬停态。  - false：不响应悬停态。  **起始版本：** 6.0.0(20) |
| avoidLayoutSafeArea | boolean | 否 | 是 | 是否需要标题栏主动避让安全区。  默认值：false。  - true：需要标题栏主动避让安全区。  - false：不需要标题栏主动避让安全区。  **起始版本：** 6.0.0(20) |
| enableComponentSafeArea | boolean | 否 | 是 | 是否将标题栏设置为[组件级安全区](ts-universal-attributes-size.md#safeareapadding14)。  默认值：false。  - true：将标题栏设置为组件级安全区。  - false：不将标题栏设置为组件级安全区。  **起始版本：** 6.0.0(20) |

## DynamicHideParams

PhonePC/2in1TabletTV

HdsNavigation标题栏动态显隐配置信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| hideTitleArea | boolean | 否 | 是 | 是否隐藏标题区域。  默认值：false。  - true：隐藏标题区域。  - false：不隐藏标题区域。 |
| hideBottomBuilder | boolean | 否 | 是 | 是否隐藏标题栏底部自定义区域。  默认值：false。  - true：隐藏标题栏底部自定义区域。  - false：不隐藏标题栏底部自定义区域。 |
| hideStatusBar | boolean | 否 | 是 | 是否隐藏状态栏区域。只有在配置隐藏标题区域时，配置隐藏状态栏才能生效  默认值：false。  - true：隐藏状态栏区域。  - false：不隐藏状态栏区域。 |
| mode | [HideMode](ui-design-hdsnavigation.md#hidemode) | 否 | 是 | 标题栏动态隐藏模式。  默认值：HideMode.SCROLL\_UP\_TO。 |
| hideOffset | number | 否 | 是 | 设置标题栏开始隐藏的滚动距离。只在HideMode.SCROLL\_UP\_TO隐藏模式下生效。  默认值：0。单位：vp。 |
| hideRatio | number | 否 | 是 | 设置内容区滚动距离与标题栏隐藏的比例，取值范围[1.0,3.0]。  当内容区每滚动1vp，标题栏隐藏1/hideRatio vp。  超出取值范围，按默认值处理。  默认值：2.0。 |

## NestedScrollInfo

PhonePC/2in1TabletTV

嵌套可滚动容器组件信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| parent | [Scroller](ts-container-scroll.md#scroller) | 否 | 否 | 可滚动容器组件的控制器。 |
| child | [Scroller](ts-container-scroll.md#scroller) | 否 | 否 | 可滚动容器组件的控制器，child对应的组件需要是parent对应组件的子组件，且组件间存在嵌套滚动关系。 |

## WithThemeOptions

PhonePC/2in1TabletTV

标题栏[WithTheme](ts-container-with-theme.md)能力配置信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enableThemeColorMode | boolean | 否 | 是 | 是否支持WithTheme作用域内组件自定义深浅色配置。  默认值：false。  - true：支持WithTheme作用域内自定义深浅色配置。  - false：不支持WithTheme作用域内自定义深浅色配置。 |

## SystemMaterialParams

PhonePC/2in1TabletTV

材质效果参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| materialType | [hdsMaterial.MaterialType](ui-design-hdsmaterial.md#materialtype) | 否 | 是 | 设置材质类型。  默认值：hdsMaterial.MaterialType.NONE。 |
| materialLevel | [hdsMaterial.MaterialLevel](ui-design-hdsmaterial.md#materiallevel) | 否 | 是 | 设置材质等级。  默认值：hdsMaterial.MaterialLevel.ADAPTIVE  **说明**：  **推荐使用默认值ADAPTIVE档位：** 该模式下，系统会根据当前设备的算力动态调整组件的材质效果，实现性能与显示效果的最佳平衡体验。  **若未采用系统自适应能力：** 请先调用[getSystemMaterialTypes()](ui-design-hdsmaterial.md#getsystemmaterialtypes)接口查询当前设备支持的材质能力，再根据查询结果选用相应的材质效果枚举：  1. 如果查询结果显示当前设备支持IMMERSIVE材质类型，可选用EXQUISITE或GENTLE效果。  2. 如果查询结果显示当前设备不支持IMMERSIVE材质类型，则建议使用SMOOTH效果，以降低卡顿和发热风险，保障用户体验。  **详细使用指导：** 请参见[HDS组件使用沉浸光感材质指南](../harmonyos-guides/ui-design-hds-component-material.md#使用自定义沉浸光感效果)。 |

## 示例

PhonePC/2in1TabletTV

### 设置动态模糊样式

通过titleBar属性，自定义设置标题栏随内容区滚动的动态模糊样式。

```
1. // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
2. import { HdsNavigation, HdsNavigationAttribute, ScrollEffectType, HdsNavigationTitleMode } from '@kit.UIDesignKit';
3. import { LengthMetrics } from '@kit.ArkUI';

5. const TITLE_BAR_HEIGHT_FREE: number = 138;

7. @Entry
8. @Component
9. struct Index {
10. @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();
11. scroller: Scroller = new Scroller();
12. @State blankHeight: number = TITLE_BAR_HEIGHT_FREE;
13. @State isHideBackButton: boolean = false;
14. @State titleMode: HdsNavigationTitleMode = HdsNavigationTitleMode.FREE;
15. @State subTitle: string = 'Sub';

17. build() {
18. HdsNavigation(this.pageInfos) {
19. Column() {
20. Stack() {
21. Scroll(this.scroller) {
22. Column() {
23. Blank().height(this.blankHeight)
24. Image($r('app.media.scenery')).width('100%') // scenery为自定义资源，开发者需替换本地资源
25. }
26. }.edgeEffect(EdgeEffect.Spring).scrollBar(BarState.Off)
27. }
28. }
29. }
30. .titleBar({
31. padding: {
32. start: LengthMetrics.vp(2),
33. end: LengthMetrics.vp(2)
34. },
35. style: {
36. scrollEffectOpts: {
37. enableScrollEffect: true,
38. scrollEffectType: ScrollEffectType.COMMON_BLUR,
39. blurEffectiveStartOffset: LengthMetrics.vp(0),
40. blurEffectiveEndOffset: LengthMetrics.vp(20)
41. },
42. originalStyle: {
43. backgroundStyle: {
44. backgroundColor: $r('sys.color.ohos_id_color_background'),
45. },
46. contentStyle: {
47. titleStyle: { mainTitleColor: $r('sys.color.font_primary'), subTitleColor: $r('sys.color.font_secondary') },
48. menuStyle: {
49. backgroundColor: $r('sys.color.comp_background_tertiary'),
50. iconColor: $r('sys.color.icon_primary')
51. },
52. backIconStyle: {
53. backgroundColor: $r('sys.color.comp_background_tertiary'),
54. iconColor: $r('sys.color.icon_primary')
55. }
56. }
57. },
58. scrollEffectStyle: {
59. backgroundStyle: {
60. backgroundColor: $r('sys.color.ohos_id_color_background_transparent'),
61. },
62. contentStyle: {
63. titleStyle: { mainTitleColor: $r('sys.color.font_primary'), subTitleColor: $r('sys.color.font_secondary') },
64. menuStyle: {
65. backgroundColor: $r('sys.color.comp_background_tertiary'),
66. iconColor: $r('sys.color.icon_primary')
67. },
68. backIconStyle: {
69. backgroundColor: $r('sys.color.comp_background_tertiary'),
70. iconColor: $r('sys.color.icon_primary')
71. }
72. }
73. }
74. },
75. content: {
76. title: {
77. mainTitle: 'Main',
78. subTitle: this.subTitle
79. },
80. menu: {
81. value: [{
82. content: {
83. label: 'menu1',
84. icon: $r('sys.symbol.ohos_wifi'),
85. isEnabled: true,
86. action: () => {
87. console.info("HdsNavigation menu1");
88. }
89. }
90. }, {
91. content: {
92. label: 'menu2',
93. icon: $r('sys.symbol.plus'),
94. isEnabled: true,
95. }
96. }, {
97. content: {
98. label: 'menu3',
99. icon: $r('sys.symbol.lock'),
100. }
101. }, {
102. content: {
103. label: 'menu4',
104. icon: $r('sys.symbol.trunk'),
105. }
106. }]
107. },
108. backIcon: {
109. label: 'backButton',
110. icon: $r('sys.symbol.trunk'),
111. isEnabled: true,
112. }
113. }
114. })
115. .systemBarStyle({ statusBarContentColor: '#0A59F7' }, { statusBarContentColor: '#C7C7CD' })
116. .titleMode(this.titleMode)
117. .hideBackButton(this.isHideBackButton)
118. .hideTitleBar(false)
119. }
120. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/UdYJyG7KRv-JrHGrmOyMhQ/zh-cn_image_0000002552960520.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000639Z&HW-CC-Expire=86400&HW-CC-Sign=064D2908C77D00E8A33A150819217BE9003F711B587A2C3EC4EBA18DC0DEF83A "点击放大")

### 设置菜单消息提醒

通过设置标题栏上菜单配置中的Badge属性，使用信息提醒能力，在菜单项右上角附加消息提醒。

```
1. // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
2. import { HdsNavigation, HdsNavigationAttribute } from '@kit.UIDesignKit';

4. const TITLE_BAR_HEIGHT_FREE: number = 138;

6. @Entry
7. @Component
8. struct Index {
9. @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();
10. @State blankHeight: number = TITLE_BAR_HEIGHT_FREE;
11. @State subTitle: string = 'Sub';

13. build() {
14. HdsNavigation(this.pageInfos) {
15. Column() {
16. Stack() {
17. Column() {
18. Blank().height(this.blankHeight)
19. Image($r('app.media.background1')) // background1为自定义资源，开发者需替换本地资源
20. .width('100%')
21. }
22. }
23. }
24. }
25. .titleBar({
26. content: {
27. title: {
28. mainTitle: "Main",
29. subTitle: this.subTitle
30. },
31. menu: {
32. value: [{
33. content: {
34. label: 'menu1',
35. icon: $r('sys.symbol.plus'),
36. isEnabled: true,
37. },
38. badge: {
39. count: 1,
40. }
41. }, {
42. content: {
43. label: 'menu2',
44. icon: $r('sys.symbol.trunk'),
45. isEnabled: true,
46. },
47. badge: {
48. count: 100,
49. }
50. }]
51. },
52. }
53. })
54. }
55. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/kV2fRGFMT4Wpi7Zwj8od4g/zh-cn_image_0000002583480521.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000639Z&HW-CC-Expire=86400&HW-CC-Sign=FBBFA2275ACD95F058001AA39B240FD09D419B2C1FF6A905C378D61E8D54E5D5 "点击放大")

### 设置自定义区域

通过设置titleBar属性中的stackBuilder，bottomBuilder属性，可以使用标题栏的自定义区域设置能力。

```
1. // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
2. import { HdsNavigation, HdsNavigationAttribute, ScrollEffectType } from '@kit.UIDesignKit';
3. import { LengthMetrics } from '@kit.ArkUI';

5. const TITLE_BAR_HEIGHT_FREE: number = 138;
6. const BOTTOM_BUILDER_HEIGHT: number = 56;

8. @Entry
9. @Component
10. struct Index {
11. scroller: Scroller = new Scroller();
12. @State blankHeight: number = TITLE_BAR_HEIGHT_FREE + BOTTOM_BUILDER_HEIGHT;

14. @Builder
15. StackBuilder() {
16. Column() {
17. Button("HdsNavigation")
18. }
19. .height(56)
20. .justifyContent(FlexAlign.Center)
21. }

23. @Builder
24. BottomBuilder() {
25. Column() {
26. Search()
27. }
28. .width('100%')
29. .height(56)
30. }

32. build() {
33. Column() {
34. HdsNavigation() {
35. Scroll(this.scroller) {
36. Column() {
37. Blank().height(this.blankHeight).width('100%')
38. Image($r('app.media.scenery')).width('100%') // scenery为自定义资源，开发者需替换本地资源
39. }
40. }.edgeEffect(EdgeEffect.Spring).scrollBar(BarState.Off)
41. }
42. .titleBar({
43. style: {
44. scrollEffectOpts: {
45. enableScrollEffect: true,
46. scrollEffectType: ScrollEffectType.GRADIENT_BLUR,
47. blurEffectiveStartOffset: LengthMetrics.vp(0),
48. blurEffectiveEndOffset: LengthMetrics.vp(20)
49. },
50. scrollEffectStyle: {
51. backgroundStyle: { maskExtraHeight: 56.0 },
52. }
53. },
54. content: {
55. title: {
56. mainTitle: 'MainTitle',
57. subTitle: 'SubTitle'
58. },
59. stackBuilder: (): void => this.StackBuilder(),
60. bottomBuilder: { builder: (): void => this.BottomBuilder() },
61. menu: {
62. value: [{
63. content: {
64. label: 'menu1',
65. icon: $r('sys.symbol.plus'),
66. },
67. }, {
68. content: {
69. label: 'menu2',
70. icon: $r('sys.symbol.lock'),
71. }
72. }]
73. }
74. }
75. })
76. .bindToScrollable([this.scroller])
77. }
78. }
79. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/JcKFodHNQFS-Rj-P8C7vPw/zh-cn_image_0000002552800872.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000639Z&HW-CC-Expire=86400&HW-CC-Sign=2FAF200363C8C17CEB79D14584C0EE7B332C8B3CF817EAE6265D1386DFCDAF4F "点击放大")

### 设置标题栏的动态显隐

通过设置dynamicHideTitleBar属性，可以使用标题栏随内容区动态显隐能力。

```
1. // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
2. import { HdsNavigation, HdsNavigationAttribute, HideMode } from '@kit.UIDesignKit';

4. const TITLE_BAR_HEIGHT_FREE: number = 138;
5. const BOTTOM_BUILDER_HEIGHT: number = 56;

7. @Entry
8. @Component
9. struct Index {
10. scroller: Scroller = new Scroller();
11. @State blankHeight: number = TITLE_BAR_HEIGHT_FREE + BOTTOM_BUILDER_HEIGHT;

13. @Builder
14. BottomBuilder() {
15. Column() {
16. Search()
17. }
18. .width('100%')
19. .height(56)
20. }

22. build() {
23. Column() {
24. HdsNavigation() {
25. Scroll(this.scroller) {
26. Column() {
27. Blank().height(this.blankHeight).width('100%')
28. Image($r('app.media.scenery')).width('100%') // scenery为自定义资源，开发者需替换本地资源
29. }
30. }.edgeEffect(EdgeEffect.Spring).scrollBar(BarState.Off)
31. }
32. .titleBar({
33. content: {
34. title: {
35. mainTitle: 'MainTitle',
36. subTitle: 'SubTitle'
37. },
38. bottomBuilder: { builder: (): void => this.BottomBuilder() },
39. menu: {
40. value: [{
41. content: {
42. label: 'menu1',
43. icon: $r('sys.symbol.plus'),
44. },
45. }]
46. }
47. }
48. })
49. .bindToScrollable([this.scroller])
50. .dynamicHideTitleBar({
51. hideTitleArea: true,
52. hideBottomBuilder: true,
53. hideStatusBar: false,
54. mode: HideMode.SCROLL_UP_TO
55. })
56. }
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/dMEsiMxGSki427p7ZPe8Ow/zh-cn_image_0000002583440567.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000639Z&HW-CC-Expire=86400&HW-CC-Sign=C34339616AA134E59E5D9DD44E93373F1EC3D4A5C96D2F18211BC33E7CC5C6E8 "点击放大")

### 设置标题栏图标样式

通过设置HdsNavigationIconOptions属性中的type属性，可以设置图标为文字型或者图片型图标。

```
1. // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
2. import {
3. HdsNavigation,
4. HdsNavigationAttribute,
5. HdsNavigationTitleMode,
6. IconStyleMode,
7. TextStyleMode,
8. DividerShowType
9. } from '@kit.UIDesignKit';

11. const TITLE_BAR_HEIGHT_MINI: number = 56;

13. @Entry
14. @Component
15. struct Index {
16. scroller: Scroller = new Scroller();
17. @State blankHeight: number = TITLE_BAR_HEIGHT_MINI;

19. build() {
20. Column() {
21. HdsNavigation() {
22. Scroll(this.scroller) {
23. Column() {
24. Blank().height(this.blankHeight).width('100%')
25. Image($r('app.media.background1')).width('100%')
26. }
27. }.edgeEffect(EdgeEffect.Spring).scrollBar(BarState.Off)
28. }
29. .titleMode(HdsNavigationTitleMode.MINI)
30. .hideBackButton(true)
31. .titleBar({
32. content: {
33. title: {
34. mainTitle: 'Main',
35. subTitle: 'Sub'
36. },
37. menu: {
38. value: [{
39. content: {
40. label: 'CAPSULE',
41. type: TextStyleMode.NORMAL,
42. }
43. }, {
44. content: {
45. label: '5',
46. type: TextStyleMode.SINGLE_CHARACTER,
47. }
48. }, {
49. content: {
50. label: 'smallIcon',
51. icon: $r('sys.symbol.plus'),
52. type: IconStyleMode.LARGE,
53. }
54. }]
55. },
56. subIcon: {
57. content: {
58. label: 'headIcon',
59. icon: $r('sys.symbol.lock'),
60. type: IconStyleMode.SMALL,
61. }
62. },
63. divider: { showType: DividerShowType.ON },
64. }
65. })
66. }
67. }
68. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/SV-TmxQuRTqwFslubgwAXA/zh-cn_image_0000002552960522.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000639Z&HW-CC-Expire=86400&HW-CC-Sign=9D44772F50C77481455C00A6B8B53B2834DB53AE535A51CA4B4F371AF3424939 "点击放大")

### 半模态标题栏样式

通过titleMode设置半模态标题栏显示模式，半模态模式下，可以在subTitle右侧区域设置用户自定义的subTitleBuilder。半模态样式下，设置图标类型为IconStyleMode.SMALL，同时不设置图标资源时，默认显示关闭按钮。

```
1. // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
2. import { HdsNavigation, HdsNavigationAttribute, HdsNavigationTitleMode, IconStyleMode } from '@kit.UIDesignKit';

4. const TITLE_BAR_HEIGHT_MODAL: number = 80;

6. @Entry
7. @Component
8. struct SheetTransitionExample {
9. @State isShow: boolean = false;
10. @State blankHeight: number = TITLE_BAR_HEIGHT_MODAL;
11. scroller: Scroller = new Scroller();

13. @Builder
14. SubTitleBuilder() {
15. Text("click to share")
16. .fontColor(Color.Blue)
17. .maxFontScale(1)
18. .lineHeight(`${14 * 1.49}vp`)
19. .fontSize(14)
20. .onClick(() => {
21. console.info("click to share");
22. })
23. }

25. // 创建半模态页面显示内容
26. @Builder
27. myBuilder() {
28. Column() {
29. HdsNavigation() {
30. Scroll(this.scroller) {
31. Column() {
32. Blank().height(this.blankHeight).width('100%')
33. Image($r('app.media.background1')) // background1为自定义资源，开发者需替换本地资源
34. .width('100%')
35. }
36. }.edgeEffect(EdgeEffect.Spring).scrollBar(BarState.Off)
37. }
38. .titleMode(HdsNavigationTitleMode.MODAL) // 设置显示的HdsNavigation为半模态样式
39. .titleBar({
40. content: {
41. title: {
42. mainTitle: 'MainTitle',
43. subTitle: 'SubTitle',
44. subTitleBuilder: this.SubTitleBuilder.bind(this), // 自定义副标题区域
45. },
46. menu: {
47. value: [{
48. content: {
49. label: 'modal_cancel',
50. isEnabled: true,
51. type: IconStyleMode.SMALL,
52. action: () => {
53. console.info("model cancel");
54. }
55. }
56. }]
57. },
58. subIcon: {
59. content: {
60. label: 'leftIcon',
61. icon: $r('sys.symbol.ohos_wifi'),
62. isEnabled: true,
63. }
64. },
65. }
66. })
67. }
68. }

70. build() {
71. Column() {
72. Button("transition modal")
73. .onClick(() => {
74. this.isShow = true;
75. })
76. .fontSize(20)
77. .margin(10)
78. .bindSheet($$this.isShow, this.myBuilder(), { showClose: false }) // 绑定半模态页面
79. }
80. .justifyContent(FlexAlign.Center)
81. .width('100%')
82. .height('100%')
83. }
84. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/23zp3jZtTbOe_FuZK5gnBQ/zh-cn_image_0000002583480523.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000639Z&HW-CC-Expire=86400&HW-CC-Sign=A3EB582D2F5925CCF8A722AE8AA0D5E5213DBE08F6A46154D0274DF3A25FAEF3 "点击放大")

### 图标上绑定自定义menu

通过设置菜单项HdsNavigationIconOptions中的componentId属性，结合promptAction.openMenu方法，绑定TargetInfo中的Id属性为设置的componentId，可以在对应的图标上弹出用户自定义菜单。

```
1. // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
2. import { HdsNavigation, HdsNavigationAttribute, HdsNavigationTitleMode } from '@kit.UIDesignKit';
3. import { ComponentContent, LengthMetrics, Prompt } from '@kit.ArkUI';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. const TITLE_BAR_HEIGHT_FULL: number = 138;

8. @Builder
9. function menuComponent() {
10. Menu() {
11. MenuItem({ content: "copy" }).onClick(() => {
12. Prompt.showToast({ message: 'on click' });
13. })
14. MenuItem({ content: "paste" }).enabled(false)
15. }
16. .width(224).menuItemDivider({ strokeWidth: LengthMetrics.px(1), color: $r('sys.color.comp_divider') })
17. }

19. @Entry
20. @Component
21. struct Index {
22. scroller: Scroller = new Scroller();
23. @State blankHeight: number = TITLE_BAR_HEIGHT_FULL;
24. private targetId: string = 'bindMenu';

26. build() {
27. Column() {
28. HdsNavigation() {
29. Scroll(this.scroller) {
30. Column() {
31. Blank().height(this.blankHeight).width('100%')
32. Image($r('app.media.background1'))
33. .width('100%')
34. }
35. }.edgeEffect(EdgeEffect.Spring).scrollBar(BarState.Off)
36. }
37. .titleMode(HdsNavigationTitleMode.FULL)
38. .titleBar({
39. content: {
40. title: {
41. mainTitle: 'MainTitle',
42. subTitle: 'SubTitle'
43. },
44. menu: {
45. value: [{
46. content: {
47. label: 'menu1',
48. icon: $r('sys.symbol.plus'),
49. isEnabled: true,
50. componentId: this.targetId,
51. action: () => {
52. let uiContext = this.getUIContext();
53. let promptAction = uiContext.getPromptAction();
54. let contentNode = new ComponentContent(uiContext, wrapBuilder(menuComponent));
55. try {
56. promptAction.openMenu(
57. contentNode,
58. { id: this.targetId },
59. { backgroundColor: Color.Yellow });
60. } catch (error) {
61. let message = (error as BusinessError).message;
62. let code = (error as BusinessError).code;
63. console.error(`openMenu args error code is ${code}, message is ${message}`);
64. }
65. console.info("model cancel");
66. }
67. }
68. }, {
69. content: {
70. label: 'menu2',
71. icon: $r('sys.symbol.ohos_wifi'),
72. }
73. }]
74. },
75. }
76. })
77. }
78. }
79. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/-k9WQcmzRRygfZ_5cBB9Ng/zh-cn_image_0000002552800874.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000639Z&HW-CC-Expire=86400&HW-CC-Sign=BA4A8D7CCE43F2DB8414155C3FD1264C7956D953BA9CCB257C9AD8E830161E5C "点击放大")

### 设置应用内多窗图标

创建一级导航组件，通过配置titleBar中的menu上的multiWindowEntryInAPPMenu属性，实现应用内多窗图标设置。

```
1. // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
2. import { HdsNavigation, HdsNavigationAttribute, HdsNavigationMenuContentOptions } from '@kit.UIDesignKit';
3. import { Want } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct MultiWindowEntryInAPPTest {
8. private want: Want = {
9. // 修改为当前应用的bundleName、moduleName、abilityName，启动应用内的UIAbility
10. bundleName: "com.example.myapplication",
11. moduleName: "entry",
12. abilityName: "FuncAbility",
13. }
14. @State menuContent: HdsNavigationMenuContentOptions = {
15. multiWindowEntryInAPPMenu: {
16. want: this.want,
17. },
18. maxCount: 3,
19. value: [
20. { content: { label: 'menu1', icon: $r('sys.symbol.search_things'), } },
21. { content: { label: 'menu2', icon: $r('sys.symbol.plus'), } }
22. ]
23. }

25. build() {
26. HdsNavigation() {
27. Stack() {
28. Text("Page1")
29. }.alignContent(Alignment.Center)
30. .width("100%")
31. .height("100%")
32. }
33. .hideToolBar(false)
34. .navBarWidth('100%')
35. .titleBar({
36. content: {
37. title: {
38. mainTitle: "Index"
39. },
40. menu: this.menuContent
41. }
42. })
43. }
44. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/857eU764TeiSG1G5-PsaLw/zh-cn_image_0000002583440569.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000639Z&HW-CC-Expire=86400&HW-CC-Sign=8AAD0953F581C3E07A076FD2CA3844FC491810D692A83309B379BEB4F7CD2E83 "点击放大")

### 设置HdsNavigation双栏模式

该示例主要展示HdsNavigation在双栏模式下，右侧显示默认占位页。

```
1. // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
2. import { HdsNavigation, HdsNavigationAttribute, HdsNavigationTitleMode } from '@kit.UIDesignKit';
3. import { ComponentContent } from '@kit.ArkUI';

5. @Builder
6. function PlaceholderPage() {
7. Column() {
8. Text("分栏模式占位页")
9. .fontSize(28)
10. .fontWeight(700)
11. .margin({ top: 200 })
12. }.width("100%")
13. .height("100%")
14. }

16. @Entry
17. @Component
18. struct Index {
19. scroller: Scroller = new Scroller();
20. placeholder = new ComponentContent(this.getUIContext(), wrapBuilder(PlaceholderPage))
21. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

23. build() {
24. HdsNavigation() {
25. List({ space: 12, initialIndex: 0, scroller: this.scroller }) {
26. ForEach(this.arr, (item: number) => {
27. ListItem() {
28. Text('' + item)
29. .width('90%')
30. .height(72)
31. .backgroundColor('#FFFFFF')
32. .borderRadius(24)
33. .fontSize(16)
34. .fontWeight(500)
35. .textAlign(TextAlign.Center)
36. }
37. }, (item: number) => item.toString())
38. }
39. .height(324)
40. .width('100%')
41. .margin({ top: 12, left: '10%' })
42. }
43. .mode(NavigationMode.Split) // 设置HdsNavigation模式为Split
44. .splitPlaceholder(this.placeholder)
45. .titleMode(HdsNavigationTitleMode.MINI)
46. .titleBar({
47. enableComponentSafeArea: true,
48. content: {
49. title: {
50. mainTitle: 'Main',
51. subTitle: 'Sub'
52. },
53. }
54. })
55. .bindToScrollable([this.scroller])
56. .divider({ startMargin: 20, endMargin: 20, color: Color.Red }) // 从6.1.0(23)开始，新增divider属性。
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/CxTA4pWGS8SqbPenk8QG8A/zh-cn_image_0000002552960524.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000639Z&HW-CC-Expire=86400&HW-CC-Sign=FDFD799B258073FB1EBF183991776EEC72679FFDFA01A91E95F32B16E9B9F9AF "点击放大")

### 设置标题栏沉浸式样式

该示例主要展示HdsNavigation配置沉浸式模糊和材质的各类型效果。

```
1. // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
2. import {
3. hdsMaterial,
4. HdsNavigation,
5. HdsNavigationAttribute,
6. HdsNavigationTitleMode,
7. ScrollEffectType,
8. } from '@kit.UIDesignKit'
9. import { promptAction } from '@kit.ArkUI'

11. @Entry
12. @Component
13. struct Index {
14. private scrollerForScroll: Scroller = new Scroller();
15. @State materialLevel: hdsMaterial.MaterialLevel = hdsMaterial.MaterialLevel.ADAPTIVE;
16. @State materialType: hdsMaterial.MaterialType = hdsMaterial.MaterialType.IMMERSIVE;

18. aboutToAppear(): void {
19. // 该示例以系统支持的材质类型为hdsMaterial.MaterialType.IMMERSIVE为例
20. try {
21. let materialTypes: Array<hdsMaterial.MaterialType> = hdsMaterial.getSystemMaterialTypes();
22. console.info(`getSystemMaterialTypes successed, types: ${materialTypes}`);
23. } catch (err) {
24. let message = (err as BusinessError).message;
25. let code = (err as BusinessError).code;
26. console.error(`getSystemMaterialTypes failed, code: ${code}, message: ${message}`);
27. }
28. }

30. build() {
31. HdsNavigation() {
32. Scroll(this.scrollerForScroll) {
33. Column() {
34. // 'app.media.demo_img'需要替换为开发者所需的资源文件
35. Image($r('app.media.demo_img'))
36. .width('100%')
37. Text(`当前材质Level为: ${this.materialLevel}`).fontSize(20).fontWeight(FontWeight.Bold)
38. Text(`当前材质Type为: ${this.materialType}`).fontSize(20).fontWeight(FontWeight.Bold)
39. Button('切换材质Type为IMMERSIVE').onClick(() => {
40. // 沉浸式材质效果，该示例场景ADAPTIVE为沉浸式材质
41. this.materialType = hdsMaterial.MaterialType.IMMERSIVE;
42. }).margin({ top: 2 })
43. Button('切换材质Type为None').onClick(() => {
44. // 无材质效果
45. this.materialType = hdsMaterial.MaterialType.NONE;
46. }).margin({ top: 2 })
47. }.height('100%')
48. }.edgeEffect(EdgeEffect.Spring).height('100%')
49. }
50. .titleBar({
51. content: {
52. title: {
53. mainTitle: '主标题',
54. },
55. menu: {
56. value: [{
57. content: {
58. icon: $r('sys.symbol.search_things'),
59. label: 'search',
60. action: () => {
61. promptAction.openToast({ message: 'on click' });
62. },
63. }
64. }]
65. },
66. },
67. style: {
68. scrollEffectOpts: {
69. // 从6.1.0(23)开始， 新增IMMERSIVE_GRADIENT_BLUR类型，标题文字和图标样式从白色到黑色线性过渡。
70. scrollEffectType: ScrollEffectType.IMMERSIVE_GRADIENT_BLUR,
71. },
72. // 从6.1.0(23)开始，支持材质相关属性。
73. // 推荐与ScrollEffectType.IMMERSIVE_GRADIENT_BLUR（推荐沉浸式图文类的场景使用） 或 ScrollEffectType.GRADIENT_BLUR（推荐非沉浸式列表类的场景使用）搭配使用。
74. systemMaterialEffect: {
75. materialType: this.materialType,
76. materialLevel: this.materialLevel
77. }
78. },
79. })
80. .bindToScrollable([this.scrollerForScroll])
81. .hideBackButton(true)
82. .titleMode(HdsNavigationTitleMode.MINI)
83. .ignoreLayoutSafeArea([LayoutSafeAreaType.SYSTEM], [LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM])
84. }
85. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/RVY9XJvoReu7g2tXXu7l4Q/zh-cn_image_0000002583480525.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000639Z&HW-CC-Expire=86400&HW-CC-Sign=CCCA170D29B64AD18BE360A241A562E33193EA98A40F6074044576900C353359 "点击放大")
