---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation
title: Navigation
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 导航与切换 > Navigation
category: harmonyos-references
scraped_at: 2026-04-28T08:01:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c9a80f5223bc1c69f6e6b95653a0d1a4b2fffd27e60a3ca3e62baeb01492148f
---

Navigation组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（Navigation的子组件）或非首页显示（[NavDestination](ts-basic-components-navdestination.md)的子组件），首页和非首页通过路由进行切换。

说明

* 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件从API version 11开始默认支持安全区避让特性(默认值为：expandSafeArea([SafeAreaType.SYSTEM, SafeAreaType.KEYBOARD, SafeAreaType.CUTOUT], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]))，开发者可以重写该属性覆盖默认行为，API version 11之前的版本需配合[expandSafeArea](ts-universal-attributes-expand-safe-area.md#expandsafearea)属性实现安全区避让。
* [NavBar](ts-basic-components-navigation.md#navbar12)嵌套使用Navigation时，内层NavDestination的生命周期不和外层NavDestination以及[全模态](ts-universal-attributes-modal-transition.md)的生命周期进行联动。
* Navigation未设置主副标题（[title](ts-basic-components-navigation.md#title)或[subTitle](ts-basic-components-navigation.md#subtitledeprecated)）且[hideBackButton](ts-basic-components-navigation.md#hidebackbutton)属性设置为true时，不显示标题栏。
* Navigation的子页面切换时，新页面会主动请求焦点。
* 不建议在[aboutToAppear](ts-custom-component-lifecycle.md#abouttoappear)中使用栈操作，此时的页面还未构建完成，会导致白屏或跳转失败等问题。

## 子组件

PhonePC/2in1TabletTVWearable

可以包含子组件。

从API version 9开始，推荐与[NavRouter](ts-basic-components-navrouter.md)组件搭配使用。

从API version 10开始，推荐使用[NavPathStack](ts-basic-components-navigation.md#navpathstack10)配合[navDestination](ts-basic-components-navigation.md#navdestination10)属性进行页面路由。

## 接口

PhonePC/2in1TabletTVWearable

### Navigation

PhonePC/2in1TabletTVWearable

Navigation()

创建路由导航的根视图容器，适用于使用[NavRouter](ts-basic-components-navrouter.md)组件进行页面路由。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### Navigation10+

PhonePC/2in1TabletTVWearable

Navigation(pathInfos: NavPathStack)

绑定导航控制器到Navigation组件，适用于使用[NavPathStack](ts-basic-components-navigation.md#navpathstack10)配合[navDestination](ts-basic-components-navigation.md#navdestination10)属性进行页面路由。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pathInfos | [NavPathStack](ts-basic-components-navigation.md#navpathstack10) | 是 | 导航控制器对象。 |

### Navigation20+

PhonePC/2in1TabletTVWearable

Navigation(pathInfos: NavPathStack, homeDestination: HomePathInfo)

绑定路由栈到Navigation组件，并且指定一个NavDestination作为Navigation的导航页（主页），适用于使用[NavPathStack](ts-basic-components-navigation.md#navpathstack10)配合[navDestination](ts-basic-components-navigation.md#navdestination10)属性或者系统路由表进行页面路由。使用示例参考[示例16（Navigation使用NavDestination作为导航页）](ts-basic-components-navigation.md#示例16navigation使用navdestination作为导航页)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pathInfos | [NavPathStack](ts-basic-components-navigation.md#navpathstack10) | 是 | 路由栈信息。 |
| homeDestination | [HomePathInfo](ts-basic-components-navigation.md#homepathinfo20) | 是 | 主页NavDestination信息。 |

说明

如果使用了主页NavDestination，则Navigation有如下变化：

* 开发者写在Navigation组件内的内容不会被创建。
* 对于Navigation的各种属性，如果主页NavDestination有对应功能的属性，则Navigation的属性不生效。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### title

PhonePC/2in1TabletTVWearable

title(value: ResourceStr | CustomBuilder | NavigationCommonTitle | NavigationCustomTitle, options?: NavigationTitleOptions)

设置页面标题。

说明

从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr)10+ | [CustomBuilder](ts-types.md#custombuilder8) | [NavigationCommonTitle](ts-basic-components-navigation.md#navigationcommontitle9)9+ | [NavigationCustomTitle](ts-basic-components-navigation.md#navigationcustomtitle9)9+ | 是 | 页面标题，使用NavigationCustomTitle类型设置height高度时，[titleMode](ts-basic-components-navigation.md#titlemode)属性不会生效。  字符串超长时，如果不设置副标题，先缩小再换行（2行）最后截断。如果设置副标题，先缩小最后截断。 |
| options11+ | [NavigationTitleOptions](ts-basic-components-navigation.md#navigationtitleoptions11) | 否 | 标题栏选项。 包含标题栏背景颜色、标题栏背景模糊样式及模糊选项、标题栏背景属性、标题栏布局方式、标题栏起始端内间距、标题栏结束端内间距、主标题属性修改器、子标题属性修改器、是否响应悬停态。 |

### menus

PhonePC/2in1TabletTVWearable

menus(value: Array<NavigationMenuItem> | CustomBuilder)

设置页面右上角菜单。不设置时不显示菜单项。使用Array<[NavigationMenuItem](ts-basic-components-navigation.md#navigationmenuitem)> 写法时，竖屏最多支持显示3个图标，横屏最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。

说明

不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<[NavigationMenuItem](ts-basic-components-navigation.md#navigationmenuitem)> | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 页面右上角菜单。 |

### menus19+

PhonePC/2in1TabletTVWearable

menus(items: Array<NavigationMenuItem> | CustomBuilder, options?: NavigationMenuOptions)

设置页面右上角菜单。不设置时不显示菜单项。与[menus](ts-basic-components-navigation.md#menus)相比，新增菜单选项。使用Array<[NavigationMenuItem](ts-basic-components-navigation.md#navigationmenuitem)> 写法时，竖屏最多支持显示3个图标，横屏最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | Array<[NavigationMenuItem](ts-basic-components-navigation.md#navigationmenuitem)> | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 页面右上角菜单。 |
| options | [NavigationMenuOptions](ts-basic-components-navigation.md#navigationmenuoptions19) | 否 | 页面右上角菜单选项。 |

### titleMode

PhonePC/2in1TabletTVWearable

titleMode(value: NavigationTitleMode)

设置页面标题栏显示模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [NavigationTitleMode](ts-basic-components-navigation.md#navigationtitlemode枚举说明) | 是 | 页面标题栏显示模式。  默认值：NavigationTitleMode.Free |

### toolbarConfiguration10+

PhonePC/2in1TabletTVWearable

toolbarConfiguration(value: Array<ToolbarItem> | CustomBuilder, options?: NavigationToolbarOptions)

设置工具栏内容。不设置时不显示工具栏。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<[ToolbarItem](ts-basic-components-navigation.md#toolbaritem10)> | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 工具栏内容，使用Array<[ToolbarItem](ts-basic-components-navigation.md#toolbaritem10)>设置的工具栏有如下特性：  工具栏所有选项均分底部工具栏，在每个均分内容区布局文本和图标。  竖屏模式最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。横屏模式时，如果为[Split](ts-basic-components-navigation.md#navigationmode9枚举说明)模式，仍按照竖屏模式显示，如果为[Stack](ts-basic-components-navigation.md#navigationmode9枚举说明)模式需配合menus属性的Array<[NavigationMenuItem](ts-basic-components-navigation.md#navigationmenuitem)>使用，底部工具栏会自动隐藏，同时底部工具栏所有选项移动至页面右上角菜单。  使用[CustomBuilder](ts-types.md#custombuilder8)写法为用户自定义工具栏选项，不具备以上功能。 |
| options11+ | [NavigationToolbarOptions](ts-basic-components-navigation.md#navigationtoolbaroptions11) | 否 | 工具栏选项。 包含工具栏背景颜色、工具栏背景模糊样式及模糊选项、工具栏背景属性、工具栏布局方式、是否隐藏工具栏的文本、工具栏更多图标的菜单选项。 |

### hideToolBar

PhonePC/2in1TabletTVWearable

hideToolBar(value: boolean)

设置是否隐藏工具栏。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否隐藏工具栏。  true：隐藏工具栏；false：显示工具栏。  传入参数非法时，按false处理。 |

### hideToolBar13+

PhonePC/2in1TabletTVWearable

hideToolBar(hide: boolean, animated: boolean)

设置是否隐藏工具栏。与[hideToolBar](ts-basic-components-navigation.md#hidetoolbar)相比，新增工具栏显隐时是否使用动画。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hide | boolean | 是 | 是否隐藏工具栏。  true：隐藏工具栏；false：显示工具栏。  传入参数非法时，按false处理。 |
| animated | boolean | 是 | 设置是否使用动画显隐工具栏。  true：使用动画显示隐藏工具栏；false：不使用动画显示隐藏工具栏。  传入参数非法时，按false处理。 |

### hideTitleBar

PhonePC/2in1TabletTVWearable

hideTitleBar(value: boolean)

设置是否隐藏标题栏。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否隐藏标题栏。  true：隐藏标题栏；false：显示标题栏。  传入参数非法时，按false处理。 |

### hideTitleBar13+

PhonePC/2in1TabletTVWearable

hideTitleBar(hide: boolean, animated: boolean)

设置是否隐藏标题栏。与[hideTitleBar](ts-basic-components-navigation.md#hidetitlebar)相比，新增标题栏显隐时是否使用动画。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hide | boolean | 是 | 是否隐藏标题栏。  true：隐藏标题栏；false：显示标题栏。  传入参数非法时，按false处理。 |
| animated | boolean | 是 | 设置是否使用动画显隐标题栏。  true：使用动画显示隐藏标题栏；false：不使用动画显示隐藏标题栏。  传入参数非法时，按false处理。 |

### hideBackButton

PhonePC/2in1TabletTVWearable

hideBackButton(value: boolean)

设置是否隐藏标题栏中的返回键。返回键仅在[titleMode](ts-basic-components-navigation.md#titlemode)设置为NavigationTitleMode.Mini时才生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否隐藏标题栏中的返回键。  true：隐藏返回键。  false：显示返回键。  传入参数非法时，按false处理。 |

### navBarWidth9+

PhonePC/2in1TabletTVWearable

navBarWidth(value: Length)

设置导航页宽度。仅在[mode](ts-basic-components-navigation.md#mode9)设置为NavigationMode.Auto或NavigationMode.Split时生效。

从API version 18开始，该参数支持[!!](../harmonyos-guides/arkts-new-binding.md)双向绑定变量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 导航页宽度。  默认值：240  单位：vp  undefined：行为不做处理，导航页宽度与默认值保持一致。 |

### navBarPosition9+

PhonePC/2in1TabletTVWearable

navBarPosition(value: NavBarPosition)

设置导航页位置。仅在[mode](ts-basic-components-navigation.md#mode9)设置为NavigationMode.Auto或NavigationMode.Split时生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [NavBarPosition](ts-basic-components-navigation.md#navbarposition9枚举说明) | 是 | 导航页位置。  默认值：NavBarPosition.Start |

### mode9+

PhonePC/2in1TabletTVWearable

mode(value: NavigationMode)

设置导航页的显示模式，支持单栏（Stack）、分栏（Split）和自适应（Auto）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [NavigationMode](ts-basic-components-navigation.md#navigationmode9枚举说明) | 是 | 导航页的显示模式。  默认值：NavigationMode.Auto  自适应：基于组件宽度自适应单栏和双栏。 |

### backButtonIcon9+

PhonePC/2in1TabletTVWearable

backButtonIcon(value: string | PixelMap | Resource | SymbolGlyphModifier)

设置标题栏中返回键图标。

说明

不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | [PixelMap](arkts-apis-image-pixelmap.md) | [Resource](ts-types.md#resource) | [SymbolGlyphModifier12+](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 是 | 标题栏中返回键图标。 |

### backButtonIcon19+

PhonePC/2in1TabletTVWearable

backButtonIcon(icon: string | PixelMap | Resource | SymbolGlyphModifier, accessibilityText?: ResourceStr)

设置标题栏中返回键图标和无障碍播报内容。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| icon | string | [PixelMap](arkts-apis-image-pixelmap.md) | [Resource](ts-types.md#resource) | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 是 | 标题栏中返回键图标。 |
| accessibilityText | [ResourceStr](ts-types.md#resourcestr) | 否 | 返回键无障碍播报内容。  默认值：系统语言是中文时为“返回”，系统语言是英文时为“back”。 |

### hideNavBar9+

PhonePC/2in1TabletTVWearable

hideNavBar(value: boolean)

设置是否隐藏导航页。设置为true时，隐藏Navigation的导航页，包括标题栏、内容区和工具栏。如果此时路由栈中存在NavDestination页面，则直接显示栈顶NavDestination页面，反之显示空白。

从API version 9开始到API version 10仅在双栏模式下生效。从API version 11开始在单栏、双栏与自适应模式均生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否隐藏导航页。  true：隐藏导航页；false：显示导航页。  传入参数非法时，按false处理。 |

### navDestination10+

PhonePC/2in1TabletTVWearable

navDestination(builder: (name: string, param: unknown) => void)

创建NavDestination组件。使用builder函数，基于name和param构造NavDestination组件。builder下只能有一个根节点。builder中允许在NavDestination组件外包含一层自定义组件， 但自定义组件不允许设置属性和事件，否则仅显示空白。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | (name: string, param: unknown) => void | 是 | 创建NavDestination组件。name：NavDestination页面名称。param：开发者设置的NavDestination页面详细参数，unknown可以是用户自定义的类型。 |

### navBarWidthRange10+

PhonePC/2in1TabletTVWearable

navBarWidthRange(value: [Dimension, Dimension])

设置导航页最小和最大宽度（双栏模式下生效）。未设置该接口时，最小宽度默认为240vp，最大宽度默认为组件宽度的40%，且不大于432vp，即导航页和内容区之间的分割线可以在此范围内进行拖拽。拖拽分割线使导航页宽度变化时，内容区的内容会被压缩。

分割线的拖拽范围：

| 条件 | 拖拽范围 |
| --- | --- |
| navBarWidthRange和minContentWidth同时设置 | 满足minContentWidth所设置的值后，在navBarWidthRange所设置的范围内进行拖拽 |
| navBarWidthRange和minContentWidth均不设置 | 在navBarWidthRange默认的最小和最大范围内进行拖拽 |
| 仅设置navBarWidthRange属性 | 在navBarWidthRange所设置的范围内进行拖拽，最大拖拽范围不能超过minContentWidth的默认值 |
| 仅设置minContentWidth属性 | 在navBarWidthRange默认的最小和最大范围内进行拖拽 |
| 仅设置navBarWidth属性 | 不支持拖拽 |

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [[Dimension](ts-types.md#dimension10), [Dimension](ts-types.md#dimension10)] | 是 | 导航页最小和最大宽度。设置异常值时按默认值处理。 |

### minContentWidth10+

PhonePC/2in1TabletTVWearable

minContentWidth(value: Dimension)

设置导航页内容区最小宽度（双栏模式下生效）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](ts-types.md#dimension10) | 是 | 导航页内容区最小宽度。  默认值：360  单位：vp  undefined：行为不做处理，导航页内容区最小宽度与默认值保持一致。  Auto模式断点计算：默认600vp，minNavBarWidth(240vp) + minContentWidth (360vp) |

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

当Navigation中显示Navigation首页时，设置对应系统状态栏的样式。

说明

1. 不建议混合使用systemBarStyle属性和window设置状态栏样式的相关接口，例如：[setWindowSystemBarProperties](arkts-apis-window-window.md#setwindowsystembarproperties9)。
2. 初次设置Navigation/NavDestination的systemBarStyle属性时，会备份当前状态栏样式用于后续的恢复场景。
3. Navigation总是以首页（路由栈内没有NavDestination时）或者栈顶NavDestination设置的状态栏样式为准。
4. Navigation首页或者任何栈顶NavDestination页面，如果设置了有效的systemBarStyle，则会使用设置的样式，反之如果之前已经备份了样式，则使用备份的样式，否则不做任何处理。
5. [Split](ts-basic-components-navigation.md#navigationmode9枚举说明)模式下的Navigation，如果内容区没有NavDestination，则遵从Navigation首页的设置，反之则遵从栈顶NavDestination的设置。
6. 仅支持在主窗口的主页面中使用systemBarStyle设置状态栏样式。
7. 仅当Navigation占满整个页面时，设置的样式才会生效，当Navigation没有占满整个页面时，如果有备份的样式，则恢复备份的样式。
8. 当页面设置不同样式时，在页面转场开始时生效。
9. 非全屏窗口下，Navigation/NavDestination设置的状态栏不生效。

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[SystemBarStyle](arkts-apis-window-i.md#systembarstyle12)> | 是 | 系统状态栏样式。 |

### recoverable14+

PhonePC/2in1TabletTVWearable

recoverable(recoverable: Optional<boolean>)

配置Navigation是否可恢复。如配置为可恢复，当应用进程异常退出并重新冷启动时，可自动创建该Navigation，并恢复至异常退出时的路由栈。

说明

1. 使用该接口需要先设置Navigation的通用属性[id](ts-universal-attributes-component-id.md#id)，否则该接口无效。
2. 该接口需要配合NavDestination的[recoverable](ts-basic-components-navdestination.md#recoverable14)接口使用。
3. 恢复的过程中不可序列化的信息，例如不可序列化的参数与用户设置的onPop等，会被丢弃，无法恢复。
4. 当应用退到后台，因系统资源不足等原因被系统终止后，如果某页面已配置为可恢复，当应用再次被唤醒至前台时，系统将自动恢复该页面。详细说明请参考[UIAbility备份恢复](../harmonyos-guides/ability-recover-guideline.md)，详细使用请参考[示例18](ts-basic-components-navigation.md#示例18设置navigation可恢复)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recoverable | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | Navigation是否可恢复，默认为不可恢复。  true：路由栈可恢复；false：路由栈不可恢复。  传入参数非法时，按false处理。 |

### enableDragBar14+

PhonePC/2in1TabletTVWearable

enableDragBar(isEnabled: Optional<boolean>)

控制分栏场景下是否显示拖拽条。该属性在PC/2in1设备上不生效。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否开启拖拽条，默认为无拖拽条样式。  true：有拖拽条样式；false：无拖拽条样式。  传入参数非法时，按false处理。 |

### enableModeChangeAnimation15+

PhonePC/2in1TabletTVWearable

enableModeChangeAnimation(isEnabled: Optional<boolean>)

控制是否开启单双栏切换时的动效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否开启单双栏切换动效。  true：开启单双栏切换动效；false：关闭单双栏切换动效。  传入参数非法时，按true处理。 |

### enableToolBarAdaptation19+

PhonePC/2in1TabletTVWearable

enableToolBarAdaptation(enable: Optional<boolean>)

设置是否启用Navigation和NavDestination的工具栏[toolbarConfiguration](ts-basic-components-navigation.md#toolbarconfiguration10)自适应能力。关闭此能力后，底部工具栏[toolbarConfiguration](ts-basic-components-navigation.md#toolbarconfiguration10)将不会再移动至页面右上角的菜单中。该接口不适配于自定义菜单，使用该接口需采用[NavigationMenuItem](ts-basic-components-navigation.md#navigationmenuitem)接口来定义[菜单](ts-basic-components-navigation.md#menus)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | Optional<boolean> | 是 | 是否启用Navigation和NavDestination的工具栏自适应能力。  默认值：true  true：启用Navigation和NavDestination的工具栏自适应能力。  false：不启用Navigation和NavDestination的工具栏自适应能力。 |

### splitPlaceholder20+

PhonePC/2in1TabletTVWearable

splitPlaceholder(placeholder: ComponentContent)

Navigation双栏模式下，支持设置右侧页面显示默认占位页，占位页仅作为UI展示页，不可获焦和响应事件。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| placeholder | [ComponentContent](js-apis-arkui-componentcontent.md#componentcontent-1) | 是 | 设置Navigation双栏模式下右侧的默认占位页。 |

### divider23+

PhonePC/2in1TabletTVWearable

divider(style: NavigationDividerStyle | null)

设置Navigation双栏模式下的分割线样式。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [NavigationDividerStyle](ts-basic-components-navigation.md#navigationdividerstyle23) | null | 是 | 设置双栏分割线样式。  - null：隐藏分割线。 |

### enableVisibilityLifecycleWithContentCover21+

PhonePC/2in1TabletTVWearable

enableVisibilityLifecycleWithContentCover(isEnabled: Optional<boolean>)

设置是否启用[NavDestination](ts-basic-components-navdestination.md)页面[onHidden](ts-basic-components-navdestination.md#onhidden10)、[onShown](ts-basic-components-navdestination.md#onshown10)生命周期与全模态的联动触发。

说明

从API version 23开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | Optional<boolean> | 是 | 是否启用NavDestination页面onShown、onHidden生命周期与全模态的联动触发。  默认值：true  true：全模态拉起时，会触发当前NavDestination页面的onHidden生命周期；全模态关闭时会触发当前NavDestination页面的onShown生命周期  false：NavDestination页面onHidden、onShown生命周期不会因为全模态的拉起、关闭而触发。 |

### subTitle(deprecated)

PhonePC/2in1TabletTVWearable

subTitle(value: string)

设置页面副标题。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[title](ts-basic-components-navigation.md#title)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 页面副标题。 |

### toolBar(deprecated)

PhonePC/2in1TabletTVWearable

toolBar(value: object | CustomBuilder)

设置工具栏内容。不设置时不显示工具栏。items均分底部工具栏，在每个均分内容区布局文本和图标，文本超长时，逐级缩小，缩小之后换行，最后截断。

说明

从API version 8开始支持，从API version 10开始废弃，建议使用[toolbarConfiguration](ts-basic-components-navigation.md#toolbarconfiguration10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | object | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 工具栏内容。 |

**object类型说明：**

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 工具栏单个选项的显示文本。 |
| icon | string | 否 | 工具栏单个选项的图标资源路径。 |
| action | () => void | 否 | 当前选项被选中的事件回调。 |

## 事件

PhonePC/2in1TabletTVWearable

### onTitleModeChange

PhonePC/2in1TabletTVWearable

onTitleModeChange(callback: (titleMode: NavigationTitleMode) => void)

当[titleMode](ts-basic-components-navigation.md#titlemode)为NavigationTitleMode.Free时，随着可滚动组件的滑动标题栏模式发生变化时触发此回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| titleMode | [NavigationTitleMode](ts-basic-components-navigation.md#navigationtitlemode枚举说明) | 是 | 标题模式。 |

### onNavBarStateChange9+

PhonePC/2in1TabletTVWearable

onNavBarStateChange(callback: (isVisible: boolean) => void)

导航页显示状态切换时触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isVisible | boolean | 是 | isVisible为true时表示显示，为false时表示隐藏。 |

### onNavigationModeChange11+

PhonePC/2in1TabletTVWearable

onNavigationModeChange(callback: (mode: NavigationMode) => void)

当Navigation首次显示或者单双栏状态发生变化时触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [NavigationMode](ts-basic-components-navigation.md#navigationmode9枚举说明) | 是 | NavigationMode.Split：当前Navigation显示为双栏;  NavigationMode.Stack：当前Navigation显示为单栏。 |

### customNavContentTransition11+

PhonePC/2in1TabletTVWearable

customNavContentTransition(delegate:(from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => NavigationAnimatedTransition | undefined)

自定义转场动画回调。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | [NavContentInfo](ts-basic-components-navigation.md#navcontentinfo11) | 是 | 退场Destination的页面。 |
| to | [NavContentInfo](ts-basic-components-navigation.md#navcontentinfo11) | 是 | 进场Destination的页面。 |
| operation | [NavigationOperation](ts-basic-components-navigation.md#navigationoperation11枚举说明) | 是 | 转场类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NavigationAnimatedTransition](ts-basic-components-navigation.md#navigationanimatedtransition11) | undefined | NavigationAnimatedTransition：自定义转场动画协议。  undefined: 返回未定义，执行默认转场动效。 |

## NavPathStack10+

PhonePC/2in1TabletTVWearable

Navigation导航控制器，以栈的数据结构管理Navigation中所有的子页面，并提供栈操作的方法用于控制Navigation中子页面的切换。

从API version 12开始，NavPathStack允许被继承，派生类对象可以替代基类NavPathStack对象使用。使用示例参见[示例10](ts-basic-components-navigation.md#示例10定义导航控制器派生类)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

说明

1.连续调用多个导航控制器操作方法时，中间过程会被忽略，显示最终的栈操作结果。

例如：在Page1页面先pop再push一个Page1，系统会认为操作前和操作后的结果一致而不进行任何操作，如果需要强行push一个Page1实例，可以使用NEW\_INSTANCE模式。

2.不建议开发者通过监听生命周期的方式管理自己的导航控制器。

3.在应用处于后台状态下，调用NavPathStack的栈操作方法，会在应用再次回到前台状态时触发刷新。

### constructor

PhonePC/2in1TabletTVWearable

constructor()

创建NavPathStack对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### pushPath10+

PhonePC/2in1TabletTVWearable

pushPath(info: NavPathInfo, animated?: boolean): void

将info指定的NavDestination页面信息入栈。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | 是 | NavDestination页面的信息。 |
| animated11+ | boolean | 否 | 是否支持转场动画。  true：支持转场动画；false：不支持转场动画。  传入参数非法时，按true处理。 |

### pushPath12+

PhonePC/2in1TabletTVWearable

pushPath(info: NavPathInfo, options?: NavigationOptions): void

将info指定的NavDestination页面信息入栈，具体根据options中指定不同的[LaunchMode](ts-basic-components-navigation.md#launchmode12枚举说明)，来实现不同的行为。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | 是 | NavDestination页面的信息。 |
| options | [NavigationOptions](ts-basic-components-navigation.md#navigationoptions12) | 否 | 路由栈操作选项。 |

### pushPathByName10+

PhonePC/2in1TabletTVWearable

pushPathByName(name: string, param: unknown, animated?: boolean): void

将name指定的NavDestination页面信息入栈，传递的数据为param。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | NavDestination页面名称。 |
| param | unknown | 是 | 开发者设置的NavDestination页面详细参数，unknown可以是用户自定义的类型。 |
| animated11+ | boolean | 否 | 是否支持转场动画。  true：支持转场动画；false：不支持转场动画。  默认值：true |

### pushPathByName11+

PhonePC/2in1TabletTVWearable

pushPathByName(name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): void

将name指定的NavDestination页面信息入栈，传递的数据为param，添加onPop回调接收入栈页面出栈时的返回结果，并进行处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | NavDestination页面名称。 |
| param | Object | 是 | 开发者设置的NavDestination页面详细参数。 |
| onPop | Callback<[PopInfo](ts-basic-components-navigation.md#popinfo11)> | 是 | Callback回调，用于页面出栈时触发该回调处理返回结果。仅[pop](ts-basic-components-navigation.md#pop11)、[popToName](ts-basic-components-navigation.md#poptoname11)、[popToIndex](ts-basic-components-navigation.md#poptoindex11)中设置result参数后触发。 |
| animated | boolean | 否 | 是否支持转场动画。  true：支持转场动画；false：不支持转场动画。  默认值：true |

### pushDestination11+

PhonePC/2in1TabletTVWearable

pushDestination(info: NavPathInfo, animated?: boolean): Promise<void>

将info指定的NavDestination页面信息入栈，使用Promise异步回调返回接口调用结果。

说明

不建议在[aboutToAppear](ts-custom-component-lifecycle.md#abouttoappear)中使用栈操作，此时的页面还未构建完成，会导致白屏或跳转失败等问题。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | 是 | NavDestination页面的信息。 |
| animated | boolean | 否 | 是否支持转场动画。  true：支持转场动画；false：不支持转场动画。  默认值：true |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异步返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |

### pushDestination12+

PhonePC/2in1TabletTVWearable

pushDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>

将info指定的NavDestination页面信息入栈，使用Promise异步回调返回接口调用结果，具体根据options中指定不同的[LaunchMode](ts-basic-components-navigation.md#launchmode12枚举说明)，来实现不同的行为。

说明

不建议在[aboutToAppear](ts-custom-component-lifecycle.md#abouttoappear)中使用栈操作，此时的页面还未构建完成，会导致白屏或跳转失败等问题。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | 是 | NavDestination页面的信息。 |
| options | [NavigationOptions](ts-basic-components-navigation.md#navigationoptions12) | 否 | 路由栈操作选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |

### pushDestinationByName11+

PhonePC/2in1TabletTVWearable

pushDestinationByName(name: string, param: Object, animated?: boolean): Promise<void>

将name指定的NavDestination页面信息入栈，传递的数据为param，使用Promise异步回调返回接口调用结果。

说明

不建议在[aboutToAppear](ts-custom-component-lifecycle.md#abouttoappear)中使用栈操作，此时的页面还未构建完成，会导致白屏或跳转失败等问题。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | NavDestination页面名称。 |
| param | Object | 是 | 开发者设置的NavDestination页面详细参数。 |
| animated | boolean | 否 | 是否支持转场动画。  true：支持转场动画；false：不支持转场动画。  默认值：true |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |

### pushDestinationByName11+

PhonePC/2in1TabletTVWearable

pushDestinationByName(name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): Promise<void>

将name指定的NavDestination页面信息入栈，传递的数据为param，并且添加用于页面出栈时处理返回结果的onPop回调，使用Promise异步回调返回接口调用结果。

说明

不建议在[aboutToAppear](ts-custom-component-lifecycle.md#abouttoappear)中使用栈操作，此时的页面还未构建完成，会导致白屏或跳转失败等问题。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | NavDestination页面名称。 |
| param | Object | 是 | 开发者设置的NavDestination页面详细参数。 |
| onPop | Callback<[PopInfo](ts-basic-components-navigation.md#popinfo11)> | 是 | Callback回调，用于页面出栈时处理返回结果。仅[pop](ts-basic-components-navigation.md#pop11)、[popToName](ts-basic-components-navigation.md#poptoname11)、[popToIndex](ts-basic-components-navigation.md#poptoindex11)中设置result参数后触发。 |
| animated | boolean | 否 | 是否支持转场动画。  true：支持转场动画；false：不支持转场动画。  默认值：true |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |

### replacePath11+

PhonePC/2in1TabletTVWearable

replacePath(info: NavPathInfo, animated?: boolean): void

将当前路由栈栈顶退出，将info指定的NavDestination页面信息入栈。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | 是 | 新栈顶页面参数信息。 |
| animated | boolean | 否 | 是否支持转场动画。  true：支持转场动画；false：不支持转场动画。  默认值：true |

### replacePath12+

PhonePC/2in1TabletTVWearable

replacePath(info: NavPathInfo, options?: NavigationOptions): void

替换路由栈操作，具体根据options中指定不同的[LaunchMode](ts-basic-components-navigation.md#launchmode12枚举说明)，来实现不同的行为。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | 是 | 新栈顶页面参数信息。 |
| options | [NavigationOptions](ts-basic-components-navigation.md#navigationoptions12) | 否 | 路由栈操作选项。 |

### replacePathByName11+

PhonePC/2in1TabletTVWearable

replacePathByName(name: string, param: Object, animated?: boolean): void

将当前路由栈栈顶退出，将name指定的页面入栈。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | NavDestination页面名称。 |
| param | Object | 是 | 开发者设置的NavDestination页面详细参数。 |
| animated11+ | boolean | 否 | 是否支持转场动画。  true：支持转场动画；false：不支持转场动画。  默认值：true |

### replaceDestination18+

PhonePC/2in1TabletTVWearable

replaceDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>

替换路由栈操作。使用Promise异步回调返回接口调用结果，具体根据options中指定不同的[LaunchMode](ts-basic-components-navigation.md#launchmode12枚举说明)，来实现不同的行为。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | 是 | NavDestination页面的信息。 |
| options | [NavigationOptions](ts-basic-components-navigation.md#navigationoptions12) | 否 | 路由栈操作选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |

### removeByIndexes11+

PhonePC/2in1TabletTVWearable

removeByIndexes(indexes: Array<number>): number

将路由栈内索引值在indexes中的NavDestination页面删除。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| indexes | Array<number> | 是 | 待删除NavDestination页面的索引值数组。索引值从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回删除的NavDestination页面数量。 |

### removeByName11+

PhonePC/2in1TabletTVWearable

removeByName(name: string): number

将路由栈内指定name的NavDestination页面删除。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 删除的NavDestination页面的名字。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回删除的NavDestination页面数量。 |

### removeByNavDestinationId12+

PhonePC/2in1TabletTVWearable

removeByNavDestinationId(navDestinationId: string): boolean

将路由栈内指定navDestinationId的NavDestination页面删除。navDestinationId可以在NavDestination的[onReady](ts-basic-components-navdestination.md#onready11)回调中获取，也可以在[NavDestinationInfo](js-apis-arkui-observer.md#navdestinationinfo)中获取。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| navDestinationId | string | 是 | 删除的NavDestination页面的唯一标识符navDestinationId。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否成功删除该页面，  true：删除成功。  false：删除失败。 |

### pop10+

PhonePC/2in1TabletTVWearable

pop(animated?: boolean): NavPathInfo | undefined

弹出路由栈栈顶元素。

说明

连续调用多个导航控制器方法时，中间被pop的页面会被缓存，后续push同名页面时会优先复用该页面，不会走新的页面创建流程。

例如：

pathStack: NavPathStack = new NavPathStack()

// 初始页面栈为：[A]

pathStack.pop()

pathStack.pushPath(A)

pathStack.pushPath(B)

// 操作后页面栈为：[A B]

此时A页面会被复用，不会走新的创建流程。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| animated11+ | boolean | 否 | 是否支持转场动画。  true：支持转场动画；false：不支持转场动画。  默认值：true |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | undefined | NavPathInfo：返回栈顶NavDestination页面的信息。  undefined: 当路由栈为空时返回undefined。 |

### pop11+

PhonePC/2in1TabletTVWearable

pop(result: Object, animated?: boolean): NavPathInfo | undefined

弹出路由栈栈顶元素，并触发onPop回调传入页面处理结果。

说明

连续调用多个导航控制器方法时，中间被pop的页面会被缓存，后续push同名页面时会优先复用该页面，不会走新的页面创建流程。

例如：

pathStack: NavPathStack = new NavPathStack()

// 初始页面栈为：[A]

pathStack.pop()

pathStack.pushPath(A)

pathStack.pushPath(B)

// 操作后页面栈为：[A B]

此时A页面会被复用，不会走新的创建流程。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | Object | 是 | 页面自定义处理结果。不支持boolean类型。 |
| animated | boolean | 否 | 是否支持转场动画。  true：支持转场动画；false：不支持转场动画。  默认值：true |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | undefined | NavPathInfo：返回栈顶NavDestination页面的信息。  undefined: 当路由栈为空时返回undefined。 |

### popToName10+

PhonePC/2in1TabletTVWearable

popToName(name: string, animated?: boolean): number

回退路由栈到由栈底开始第一个名为name的NavDestination页面。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | NavDestination页面名称。 |
| animated11+ | boolean | 否 | 是否支持转场动画。  true：支持转场动画；false：不支持转场动画。  默认值：true |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的索引，否则返回-1。 |

### popToName11+

PhonePC/2in1TabletTVWearable

popToName(name: string, result: Object, animated?: boolean): number

回退路由栈到由栈底开始第一个名为name的NavDestination页面，并触发onPop回调传入页面处理结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | NavDestination页面名称。 |
| result | Object | 是 | 页面自定义处理结果。不支持boolean类型。 |
| animated | boolean | 否 | 是否支持转场动画。  true：支持转场动画；false：不支持转场动画。  默认值：true |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的索引，否则返回-1。 |

### popToIndex10+

PhonePC/2in1TabletTVWearable

popToIndex(index: number, animated?: boolean): void

回退路由栈到index指定的NavDestination页面。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | NavDestination页面的位置索引。索引值从0开始。 |
| animated11+ | boolean | 否 | 是否支持转场动画。  true：支持转场动画；false：不支持转场动画。  默认值：true |

### popToIndex11+

PhonePC/2in1TabletTVWearable

popToIndex(index: number, result: Object, animated?: boolean): void

回退路由栈到index指定的NavDestination页面，并触发onPop回调传入页面处理结果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | NavDestination页面的位置索引。索引值从0开始。 |
| result | Object | 是 | 页面自定义处理结果。不支持boolean类型。 |
| animated | boolean | 否 | 是否支持转场动画。  true：支持转场动画；false：不支持转场动画。  默认值：true |

### moveToTop10+

PhonePC/2in1TabletTVWearable

moveToTop(name: string, animated?: boolean): number

将由栈底开始第一个名为name的NavDestination页面移到栈顶。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | NavDestination页面名称。 |
| animated11+ | boolean | 否 | 是否支持转场动画。  true：支持转场动画；false：不支持转场动画。  默认值：true |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的当前索引，否则返回-1。 |

### moveIndexToTop10+

PhonePC/2in1TabletTVWearable

moveIndexToTop(index: number, animated?: boolean): void

将index指定的NavDestination页面移到栈顶。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | NavDestination页面的位置索引。索引值从0开始。 |
| animated11+ | boolean | 否 | 是否支持转场动画。  true：支持转场动画；false：不支持转场动画。  默认值：true |

### clear10+

PhonePC/2in1TabletTVWearable

clear(animated?: boolean): void

清除栈中所有页面。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| animated11+ | boolean | 否 | 是否支持转场动画。  true：支持转场动画；false：不支持转场动画。  默认值：true |

### getAllPathName10+

PhonePC/2in1TabletTVWearable

getAllPathName(): Array<string>

获取栈中所有NavDestination页面的名称。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回栈中所有NavDestination页面的名称。 |

### getParamByIndex10+

PhonePC/2in1TabletTVWearable

getParamByIndex(index: number): unknown | undefined

获取index指定的NavDestination页面的参数信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | NavDestination页面的位置索引。 索引值从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| unknown | undefined | unknown：返回对应NavDestination页面的参数信息，unknown可以是用户自定义的类型。  undefined: 传入index无效时返回undefined。 |

### getParamByName10+

PhonePC/2in1TabletTVWearable

getParamByName(name: string): Array<unknown>

获取所有名为name的NavDestination页面的参数信息，按页面索引从小到大排序。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | NavDestination页面名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<unknown> | 返回全部名为name的NavDestination页面的参数信息，unknown可以是用户自定义的类型。 |

### getIndexByName10+

PhonePC/2in1TabletTVWearable

getIndexByName(name: string): Array<number>

获取全部名为name的NavDestination页面的位置索引。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | NavDestination页面名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<number> | 返回全部名为name的NavDestination页面的位置索引。 当路由栈中不存在此name，返回空数组。索引取值范围为[0, 路由栈大小-1] |

### size10+

PhonePC/2in1TabletTVWearable

size(): number

获取栈大小。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回栈大小。  取值范围：[0, +∞) |

### disableAnimation11+

PhonePC/2in1TabletTVWearable

disableAnimation(value: boolean): void

关闭（true）或打开（false）当前Navigation中所有转场动画。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否关闭转场动画，  默认值：false  true：关闭转场动画。  false：不关闭转场动画。 |

### getParent11+

PhonePC/2in1TabletTVWearable

getParent(): NavPathStack | null

获取父NavPathStack。

当出现Navigation嵌套Navigation的情况时（可以是直接嵌套，也可以是间接嵌套），内部Navigation的NavPathStack能够获取到外层Navigation的NavPathStack。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NavPathStack](ts-basic-components-navigation.md#navpathstack10) | null | 如果当前NavPathStack所属Navigation的外层有另外的一层Navigation，则能够获取到外层Navigation的NavPathStack。否则获取不到NavPathStack，返回null。 |

### setInterception12+

PhonePC/2in1TabletTVWearable

setInterception(interception: NavigationInterception): void

设置Navigation页面跳转拦截回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| interception | [NavigationInterception](ts-basic-components-navigation.md#navigationinterception12) | 是 | 设置Navigation跳转拦截对象。 |

### getPathStack19+

PhonePC/2in1TabletTVWearable

getPathStack(): Array<NavPathInfo>

获取当前路由栈中的路由页面信息数组。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[NavPathInfo](ts-basic-components-navigation.md#navpathinfo10)> | 当前路由栈中的路由页面信息数组。 |

### setPathStack19+

PhonePC/2in1TabletTVWearable

setPathStack(pathStack: Array<NavPathInfo>, animated?: boolean): void

将当前路由栈中的路由页面信息数组更新为指定内容，并实现路由转场。

说明

1. 开发者可以在原有栈的基础上批量添加或删除页面。批量入栈的页面中，只有可见的页面会触发创建，其他页面虽已入栈但不会立即创建，当这些页面变为可见时，才会触发创建。
2. 通过批量入栈功能更新的路由栈，各页面的生命周期事件触发顺序为从栈顶到底部依次触发，这与其它入栈接口从栈底到顶部的触发顺序不同。
3. 开发者可以通过[NavPathInfo](ts-basic-components-navigation.md#navpathinfo10)中的页面唯一标识符navDestinationId来操作已有页面，该id由系统默认生成且全局唯一（可以通过[getPathStack](ts-basic-components-navigation.md#getpathstack19)接口获取，不可主动赋新值）。若该id在当前路由栈中不存在，则表示新增页面，若在当前路由栈中存在，同时对应的name相同，则表示复用已有页面。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pathStack | Array<[NavPathInfo](ts-basic-components-navigation.md#navpathinfo10)> | 是 | 设置当前路由栈中的路由页面信息数组。  **说明：**  数组长度无限制。 |
| animated | boolean | 否 | 是否开启转场动画。  true：开启转场动画；false：不开启转场动画。  默认值：true |

## NavPathInfo10+

PhonePC/2in1TabletTVWearable

路由页面信息。

### constructor

PhonePC/2in1TabletTVWearable

constructor(name: string, param: unknown, onPop?: Callback<PopInfo>, isEntry?: boolean)

创建NavPathInfo对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | NavDestination页面名称。该名称匹配开发者设置的路由表中的name，包括以下两种：  1. 自定义路由表，开发者通过[navDestination](ts-basic-components-navigation.md#navdestination10)方法传递。  2. 系统路由表，通过routerMap中的name设置，可参考[示例2](ts-basic-components-navigation.md#示例2使用导航控制器方法)。 |
| param | unknown | 是 | 开发者设置的NavDestination页面详细参数，unknown可以是用户自定义的类型。 |
| onPop11+ | Callback<[PopInfo](ts-basic-components-navigation.md#popinfo11)> | 否 | NavDestination页面触发[pop](ts-basic-components-navigation.md#pop11)、[popToName](ts-basic-components-navigation.md#poptoname11)、[popToIndex](ts-basic-components-navigation.md#poptoindex11)时返回的回调。仅[pop](ts-basic-components-navigation.md#pop11)、[popToName](ts-basic-components-navigation.md#poptoname11)、[popToIndex](ts-basic-components-navigation.md#poptoindex11)中设置result参数后触发。 |
| isEntry12+ | boolean | 否 | 标记NavDestination是否为入口页面。  true：NavDestination是入口页面；false：NavDestination不是入口页面。  默认值：false  标记清理时机：1. 在当前navDestination页面触发一次全局返回事件。2. 应用退至后台。  **说明：**  入口NavDestination不响应应用内的全局back事件，直接触发应用间的全局back事件。 |

### 属性

PhonePC/2in1TabletTVWearable

NavPathInfo参数信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | NavDestination页面名称。该名称匹配开发者设置的路由表中的name，包括以下两种：  1. 自定义路由表，开发者通过[navDestination](ts-basic-components-navigation.md#navdestination10)方法传递。  2. 系统路由表，通过routerMap中的name设置，可参考[示例2](ts-basic-components-navigation.md#示例2使用导航控制器方法)。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| param | unknown | 否 | 是 | 开发者设置的NavDestination页面详细参数，unknown可以是用户自定义的类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onPop11+ | Callback<[PopInfo](ts-basic-components-navigation.md#popinfo11)> | 否 | 是 | NavDestination页面触发[pop](ts-basic-components-navigation.md#pop11)、[popToName](ts-basic-components-navigation.md#poptoname11)、[popToIndex](ts-basic-components-navigation.md#poptoindex11)时返回的回调。仅[pop](ts-basic-components-navigation.md#pop11)、[popToName](ts-basic-components-navigation.md#poptoname11)、[popToIndex](ts-basic-components-navigation.md#poptoindex11)中设置result参数后触发。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| isEntry12+ | boolean | 否 | 是 | 标记NavDestination是否为入口页面。  true：NavDestination是入口页面；false：NavDestination不是入口页面。  默认值：false  标记清理时机：1. 在当前navDestination页面触发一次全局back事件。2. 应用退至后台。  **说明：**  入口NavDestination不响应应用内的全局back事件，直接触发应用间的全局back事件。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| navDestinationId19+ | string | 否 | 是 | NavDestination页面唯一标识符，该id由系统默认生成且全局唯一，通过[getPathStack](ts-basic-components-navigation.md#getpathstack19)接口可读取，但不可以主动赋新值。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |

## PopInfo11+

PhonePC/2in1TabletTVWearable

下一个页面返回的回调信息载体。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| info | [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | 否 | 否 | 页面触发返回时的当前页面信息，系统自动获取填入，无需开发者传入。 |
| result | Object | 否 | 否 | 页面触发返回时的结果，开发者自定义对象。 |

## NavContentInfo11+

PhonePC/2in1TabletTVWearable

跳转Destination信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 是 | NavDestination名称，如果为根视图(NavBar)，则返回值为undefined。 |
| index | number | 否 | 否 | NavDestination在NavPathStack中的序号， 如果为根视图(NavBar)，则返回值为 -1。  取值范围：[-1, +∞)。 |
| mode | [NavDestinationMode](ts-basic-components-navdestination.md#navdestinationmode枚举说明11) | 否 | 是 | NavDestination的模式，如果是根视图(NavBar)，则返回值为undefined。 |
| param12+ | Object | 否 | 是 | NavDestination页面加载的参数。 |
| navDestinationId12+ | string | 否 | 是 | NavDestination的唯一标识符。 |

## NavigationAnimatedTransition11+

PhonePC/2in1TabletTVWearable

自定义转场动画协议，开发者需实现该协议来定义Navigation路由跳转的跳转动画。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timeout | number | 否 | 是 | 动画超时结束时间。  单位：ms。  取值范围：[0, +∞)。  默认值：可交互动画无默认值，不可交互动画默认超时时间为1000ms。 |
| transition | (transitionProxy:[NavigationTransitionProxy](ts-basic-components-navigation.md#navigationtransitionproxy-11)) => void | 否 | 否 | 自定义转场动画执行回调。  transitionProxy：自定义转场动画代理对象。 |
| onTransitionEnd | (success:boolean) => void | 否 | 是 | 转场完成回调。  success：转场是否成功。 |
| isInteractive12+ | boolean | 否 | 是 | 本次转场动画是否为可交互转场。  true：本次转场动画是可交互转场；false：本次转场动画不是可交互转场。  默认值：false |

## NavigationTransitionProxy 11+

PhonePC/2in1TabletTVWearable

自定义转场动画代理对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

PhonePC/2in1TabletTVWearable

NavigationTransitionProxy参数信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| from | [NavContentInfo](ts-basic-components-navigation.md#navcontentinfo11) | 否 | 否 | 退场页面信息。 |
| to | [NavContentInfo](ts-basic-components-navigation.md#navcontentinfo11) | 否 | 否 | 进场页面信息。 |
| isInteractive12+ | boolean | 否 | 是 | 是否为可交互转场动画。  默认值：false  true：本次转场动画是可交互转场。  false：本次转场动画不是可交互转场。 |

### finishTransition

PhonePC/2in1TabletTVWearable

finishTransition(): void;

结束本次自定义转场动画，开发者需要主动触发该方法来结束本次转场，否则系统会在timeout的时间后结束本次转场。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### cancelTransition12+

PhonePC/2in1TabletTVWearable

cancelTransition?(): void;

取消本次交互转场，恢复到页面跳转前的路由栈(不支持取消不可交互转场动画)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### updateTransition12+

PhonePC/2in1TabletTVWearable

updateTransition?(progress: number): void;

更新交互转场动画进度(不可交互动画不支持动画进度设置)。

说明

不建议在[aboutToAppear](ts-custom-component-lifecycle.md#abouttoappear)中使用栈操作，此时的页面还未构建完成，会导致白屏或跳转失败等问题。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| progress | number | 是 | 设置交互转场动画进度百分比。取值范围：[0, 1] |

## NavigationInterception12+

PhonePC/2in1TabletTVWearable

Navigation跳转拦截对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| willShow | [InterceptionShowCallback](ts-basic-components-navigation.md#interceptionshowcallback12) | 否 | 是 | 页面跳转前的回调，允许操作栈，在当前跳转中生效。拦截的页面会被创建。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| didShow | [InterceptionShowCallback](ts-basic-components-navigation.md#interceptionshowcallback12) | 否 | 是 | 页面跳转后回调。在该回调中操作栈在下一次跳转中刷新。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| modeChange | [InterceptionModeCallback](ts-basic-components-navigation.md#interceptionmodecallback12) | 否 | 是 | Navigation单双栏显示状态发生变更时触发该回调。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| interception22+ | [InterceptionCallback](ts-basic-components-navigation.md#interceptioncallback22) | 否 | 是 | 页面跳转前的回调，允许操作栈，在当前跳转中生效。拦截的页面不会被创建。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |

### InterceptionShowCallback12+

PhonePC/2in1TabletTVWearable

type InterceptionShowCallback = (from: NavDestinationContext | NavBar, to: NavDestinationContext | NavBar, operation: NavigationOperation, isAnimated: boolean) => void

Navigation页面跳转前和页面跳转后的拦截回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | [NavDestinationContext](ts-basic-components-navdestination.md#navdestinationcontext11) | [NavBar](ts-basic-components-navigation.md#navbar12) | 是 | 页面跳转之前的栈顶页面信息。参数值为navBar，则表示跳转前的页面为Navigation首页。 |
| to | [NavDestinationContext](ts-basic-components-navdestination.md#navdestinationcontext11) | [NavBar](ts-basic-components-navigation.md#navbar12) | 是 | 页面跳转之后的栈顶页面信息。参数值为navBar，则表示跳转的目标页面为Navigation首页。 |
| operation | [NavigationOperation](ts-basic-components-navigation.md#navigationoperation11枚举说明) | 是 | 当前页面跳转类型。 |
| isAnimated | boolean | 是 | 页面跳转是否有动画。  true：页面跳转有动画。  false：页面跳转没有动画。 |

### InterceptionModeCallback12+

PhonePC/2in1TabletTVWearable

type InterceptionModeCallback = (mode: NavigationMode) => void

Navigation单双栏显示状态发生变更时的拦截回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [NavigationMode](ts-basic-components-navigation.md#navigationmode9枚举说明) | 是 | 导航页的显示模式。 |

### InterceptionCallback22+

PhonePC/2in1TabletTVWearable

type InterceptionCallback = (from: NavPathInfo | NavBar, to: NavPathInfo | NavBar, pathStack: NavPathStack, operation: NavigationOperation, isAnimated: boolean) => void

Navigation页面跳转前的拦截回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) |[NavBar](ts-basic-components-navigation.md#navbar12) | 是 | 退场页面信息。参数值为navBar，则表示跳转前的页面为Navigation首页。 |
| to | [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) |[NavBar](ts-basic-components-navigation.md#navbar12) | 是 | 进场页面信息。参数值为navBar，则表示跳转的目标页面为Navigation首页。 |
| pathStack | [NavPathStack](ts-basic-components-navigation.md#navpathstack10) | 是 | 页面栈。 |
| operation | [NavigationOperation](ts-basic-components-navigation.md#navigationoperation11枚举说明) | 是 | 当前页面跳转类型。 |
| isAnimated | boolean | 是 | 页面跳转是否有动画。  true：页面跳转有动画。  false：页面跳转没有动画。 |

## NavBar12+

PhonePC/2in1TabletTVWearable

type NavBar = 'navBar'

Navigation首页名字。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| 'navBar' | Navigation首页。 |

## NavigationMenuItem

PhonePC/2in1TabletTVWearable

导航菜单项，包括菜单图标和菜单信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | string | [Resource14+](ts-types.md#resource) | 否 | 否 | API version 9：显示菜单栏单个选项的文本。  从API version 10开始，不显示菜单栏单个选项的文本。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| icon | string | [Resource14+](ts-types.md#resource) | 否 | 是 | 菜单栏单个选项的图标资源路径。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| isEnabled12+ | boolean | 否 | 是 | 使能状态，默认使能（false未使能，true使能）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| action | () => void | 否 | 是 | 当前选项被选中的事件回调。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| symbolIcon12+ | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 是 | 菜单栏单个选项的symbol资源（优先级高于icon）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## ToolbarItem10+

PhonePC/2in1TabletTVWearable

工具栏可配置参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | ResourceStr | 否 | 否 | 工具栏单个选项的显示文本。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| icon | ResourceStr | 否 | 是 | 工具栏单个选项的图标资源路径。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| action | () => void | 否 | 是 | 当前选项被选中的事件回调。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| status | [ToolbarItemStatus](ts-basic-components-navigation.md#toolbaritemstatus10枚举说明) | 否 | 是 | 工具栏单个选项的状态。  默认值：ToolbarItemStatus.NORMAL  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| activeIcon | ResourceStr | 否 | 是 | 工具栏单个选项处于ACTIVE态时的图标资源路径。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| symbolIcon12+ | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 是 | 工具栏单个选项的symbol资源（优先级高于icon）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| activeSymbolIcon12+ | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 是 | 工具栏单个选项处于ACTIVE态时的symbol资源（优先级高于activeIcon）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## ToolbarItemStatus10+枚举说明

PhonePC/2in1TabletTVWearable

工具栏单个选项的状态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 设置工具栏单个选项为NORMAL态，该选项显示默认样式，可以触发Hover，Press，Focus事件并显示对应的多态样式。 |
| DISABLED | 1 | 设置工具栏单个选项为DISABLED态， 该选项显示DISABLED态样式，并且不可交互。 |
| ACTIVE | 2 | 设置工具栏单个选项为ACTIVE态， 该选项通过点击事件可以将icon图标更新为activeIcon对应的图片资源。 |

## NavigationTitleMode枚举说明

PhonePC/2in1TabletTVWearable

标题栏显示模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Free | 0 | 当内容为满一屏的可滚动组件时，标题随着内容向上滚动而缩小（子标题的大小不变、淡出）。向下滚动内容到顶时则恢复原样。  **说明：**  标题随着内容滚动大小联动的动效在title设置为ResourceStr和NavigationCommonTitle时生效，设置成其余自定义节点类型时字体样式无法变化，下拉时只影响标题栏偏移。  可滚动组件不满一屏时，如果想使用联动效果，就要使用滚动组件提供的[edgeEffect](ts-container-list.md#edgeeffect)接口将options参数设置为true。未滚动状态，标题栏高度与Full模式一致；滚动时，标题栏的最小高度与Mini模式一致。 |
| Full | 1 | 固定为大标题模式。  默认值：只有主标题时，标题栏高度为112vp；同时有主标题和副标题时，标题栏高度为138vp。 |
| Mini | 2 | 固定为小标题模式。  默认值：API version 12之前，只有主标题时，标题栏高度为56vp；同时有主标题和副标题时，标题栏高度为82vp。从API version 12开始，该模式下标题栏高度为56vp。 |

## NavigationCommonTitle9+

PhonePC/2in1TabletTVWearable

Navigation通用标题。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| main | string | [Resource14+](ts-types.md#resource) | 否 | 否 | 设置主标题。 |
| sub | string | [Resource14+](ts-types.md#resource) | 否 | 否 | 设置副标题。 |

## NavigationCustomTitle9+

PhonePC/2in1TabletTVWearable

Navigation自定义标题。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| builder | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 否 | 设置标题栏内容。 |
| height | [TitleHeight](ts-appendix-enums.md#titleheight9) | [Length](ts-types.md#length) | 否 | 否 | 设置标题栏高度。 |

## NavigationDividerStyle23+

PhonePC/2in1TabletTVWearable

Navigation分割线颜色及上下边距。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 分割线的颜色。  默认值：#33000000，灰色。 |
| startMargin | [Length](ts-types.md#length) | 否 | 是 | 分割线与侧边栏顶端的距离。  默认值：0  单位：vp  取值范围：[0, +∞) |
| endMargin | [Length](ts-types.md#length) | 否 | 是 | 分割线与侧边栏底端的距离。  默认值：0  单位：vp  取值范围：[0, +∞) |

## NavBarPosition9+枚举说明

PhonePC/2in1TabletTVWearable

导航页位置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 说明 |
| --- | --- |
| Start | 双栏显示时，主列在主轴方向首部。 |
| End | 双栏显示时，主列在主轴方向尾部。 |

## NavigationMode9+枚举说明

PhonePC/2in1TabletTVWearable

导航页显示模式。Navigation处于分栏显示状态时，导航页和内容区之间会显示分割线。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Stack | 0 | 导航页与内容区独立显示，相当于两个页面。 |
| Split | 1 | 导航页与内容区分两栏显示。  **1.** navBarWidth最终取值与开发者设置值的关系参见表1。  **2.** 缩小组件尺寸时，先缩小内容区的尺寸至minContentWidth，然后再缩小导航页的尺寸至minNavBarWidth。若继续缩小，先缩小内容区，内容区消失后再缩小导航页。  **3.** 设置导航页为固定尺寸时，若持续缩小组件尺寸，导航页最后压缩显示。  **4.** 若只设置了navBarWidth属性，则导航页宽度为navBarWidth，且分割线不可拖动。  **5.** 分割线的热区左右各2vp，建议避让4vp以上。  **6.** Split模式下，内容区若只存在一个页面，则页面左上角不会显示返回按钮。 |
| Auto | 2 | API version 9之前：窗口宽度>=520vp时，采用Split模式显示；窗口宽度<520vp时，采用Stack模式显示。  API version 10及以上：窗口宽度>=600vp时，采用Split模式显示；窗口宽度<600vp时，采用Stack模式显示，600vp等于minNavBarWidth(240vp) + minContentWidth (360vp)。 |

**表1** navBarWidth最终取值与开发者设置值的关系表

| 开发者设置的navBarWidth值 | calcNavBarWidth计算值 | navBarWidth最终取值 |
| --- | --- | --- |
| navBarWidth < minNavBarWidth | NA | minNavBarWidth |
| navBarWidth > maxNavBarWidth | calcNavBarWidth > maxNavBarWidth | maxNavBarWidth |
| navBarWidth > maxNavBarWidth | calcNavBarWidth < minNavBarWidth | minNavBarWidth |
| navBarWidth > maxNavBarWidth | minNavBarWidth ≤ calcNavBarWidth ≤ maxNavBarWidth | calcNavBarWidth |
| minNavBarWidth ≤ navBarWidth ≤ maxNavBarWidth | calcNavBarWidth ≤ minNavBarWidth | minNavBarWidth |
| minNavBarWidth ≤ navBarWidth ≤ maxNavBarWidth | minNavBarWidth < calcNavBarWidth <= navBarWidth | calcNavBarWidth |
| minNavBarWidth ≤ navBarWidth ≤ maxNavBarWidth | calcNavBarWidth > navBarWidth | navBarWidth |

说明

为了简化表示，可以将组件宽度 - minContentWidth - 分割线宽度 (1px)称为calcNavBarWidth。

## NavigationOperation11+枚举说明

PhonePC/2in1TabletTVWearable

页面跳转类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PUSH | 1 | 本次转场为页面进场。 |
| POP | 2 | 本次转场为页面退场。 |
| REPLACE | 3 | 本次转场为页面替换。 |

## BarStyle12+枚举说明

PhonePC/2in1TabletTVWearable

标题栏或工具栏的布局样式。NavDestination的工具栏不支持设置该属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STANDARD | 0 | 指定该模式的标题栏或工具栏与内容区采用上下布局。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| STACK | 1 | 指定该模式的标题栏或工具栏与内容区采用层叠布局，标题栏或工具栏布局在内容区上层。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| SAFE\_AREA\_PADDING14+ | 2 | 将指定该模式的标题栏或工具栏设置为[组件级安全区](ts-universal-attributes-size.md#safeareapadding14)。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |

## NavigationTitleOptions11+

PhonePC/2in1TabletTVWearable

标题栏选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 标题栏背景颜色，不设置时为系统默认颜色。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 标题栏背景模糊样式，不设置时关闭背景模糊效果。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| backgroundBlurStyleOptions19+ | [BackgroundBlurStyleOptions](ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 否 | 是 | 标题栏背景模糊选项。  **说明：**  只在设置了backgroundBlurStyle时生效。  不建议与backgroundEffect同时使用。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| backgroundEffect19+ | [BackgroundEffectOptions](ts-universal-attributes-background.md#backgroundeffectoptions11) | 否 | 是 | 设置标题栏背景属性包括：模糊半径，亮度，饱和度，颜色等。  **说明：**  不建议与backgroundBlurStyleOptions同时使用。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| barStyle12+ | [BarStyle](ts-basic-components-navigation.md#barstyle12枚举说明) | 否 | 是 | 设置标题栏布局方式。  默认值：BarStyle.STANDARD  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| paddingStart12+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 标题栏起始端内间距。  仅支持以下任一场景：  1. 显示返回图标，即[hideBackButton](ts-basic-components-navigation.md#hidebackbutton)为false；  2. 使用非自定义标题，即[标题value](ts-basic-components-navigation.md#title)类型为ResourceStr或NavigationCommonTitle。  默认值：  LengthMetrics.resource($r('sys.float.margin\_left'))。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| paddingEnd12+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 标题栏结束端内间距。  仅支持以下任一场景：  1. 使用非自定义菜单，即[菜单value](ts-basic-components-navigation.md#menus)为Array<NavigationMenuItem>；  2. 没有右上角菜单，且使用非自定义标题，即[标题value](ts-basic-components-navigation.md#title)类型为ResourceStr或NavigationCommonTitle。  默认值：  LengthMetrics.resource($r('sys.float.margin\_right'))  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| mainTitleModifier13+ | [TextModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 主标题属性修改器。  1. 通过Modifier设置的属性会覆盖系统默认的属性（如果Modifier设置了fontSize，maxFontSize，minFontSize任一属性，则系统设置的大小相关属性不生效，以开发者的设置为准）；  2. 不设该属性或者设置了异常值，则恢复系统默认设置；  3. [Free](ts-basic-components-navigation.md#navigationtitlemode枚举说明)模式下设置字体大小时，原有滑动改变标题大小的效果失效。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| subTitleModifier13+ | [TextModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 子标题属性修改器。  1. 通过Modifier设置的属性会覆盖系统默认的属性（如果Modifier设置了fontSize，maxFontSize，minFontSize任一属性，则系统设置的大小相关属性不生效，以开发者的设置为准）；  2. 不设该属性或者设置了异常值，则恢复系统默认设置。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| enableHoverMode13+ | boolean | 否 | 是 | 是否响应悬停态。  使用规则：  1. 需满足Navigation为全屏大小；  2. 标题栏显示模式为[Free](ts-basic-components-navigation.md#navigationtitlemode枚举说明)时或者标题栏布局方式为[STANDARD](ts-basic-components-navigation.md#barstyle12枚举说明)时，此接口设置无效。  true：响应悬停态；false：不响应悬停态。  默认值：false  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |

## NavigationToolbarOptions11+

PhonePC/2in1TabletTVWearable

工具栏选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 工具栏背景颜色，不设置时为系统默认颜色。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 工具栏背景模糊样式，不设置时关闭背景模糊效果。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| backgroundBlurStyleOptions19+ | [BackgroundBlurStyleOptions](ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 否 | 是 | 工具栏背景模糊选项。  **说明：**  只在设置了backgroundBlurStyle时生效。  不建议与backgroundEffect同时使用。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| backgroundEffect19+ | [BackgroundEffectOptions](ts-universal-attributes-background.md#backgroundeffectoptions11) | 否 | 是 | 设置工具栏背景属性包括：模糊半径，亮度，饱和度，颜色等。  **说明：**  不建议与backgroundBlurStyleOptions同时使用。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| barStyle14+ | [BarStyle](ts-basic-components-navigation.md#barstyle12枚举说明) | 否 | 是 | 设置工具栏布局方式。  默认值：BarStyle.STANDARD  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| hideItemValue19+ | boolean | 否 | 是 | 设置是否隐藏工具栏的文本，默认显示文本。  true：隐藏工具栏的文本；false：不隐藏工具栏的文本。  默认值：false  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| moreButtonOptions19+ | [MoreButtonOptions](ts-basic-components-navigation.md#morebuttonoptions19) | 否 | 是 | 工具栏更多图标的菜单选项。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |

## NavigationMenuOptions19+

PhonePC/2in1TabletTVWearable

页面右上角菜单选项。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| moreButtonOptions | [MoreButtonOptions](ts-basic-components-navigation.md#morebuttonoptions19) | 否 | 是 | 更多图标的菜单选项。 |

## LaunchMode12+枚举说明

PhonePC/2in1TabletTVWearable

路由栈操作模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STANDARD | 0 | 系统默认的栈操作模式。  push操作会将指定的NavDestination入栈；replace操作会将当前栈顶NavDestination替换。 |
| MOVE\_TO\_TOP\_SINGLETON | 1 | 从栈底向栈顶查找，如果指定的名称已经存在，则将对应的NavDestination页面移到栈顶（replace操作会将最后的栈顶替换成指定的NavDestination），否则行为和STANDARD一致。 |
| POP\_TO\_SINGLETON | 2 | 从栈底向栈顶查找，如果指定的名称已经存在，则将其上方的NavDestination页面全部移除（replace操作会将最后的栈顶替换成指定的NavDestination），否则行为和STANDARD一致。 |
| NEW\_INSTANCE | 3 | 创建新的NavDestination实例。与STANDARD模式相比，该方法不会复用栈中同名实例。并且指定该模式时，新创建的页面默认会执行push动效。 |

## NavigationOptions12+

PhonePC/2in1TabletTVWearable

路由栈操作选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| launchMode | [LaunchMode](ts-basic-components-navigation.md#launchmode12枚举说明) | 否 | 是 | 路由栈的操作模式。  默认值：LaunchMode.STANDARD |
| animated | boolean | 否 | 是 | 是否支持转场动画。  true：支持转场动画；false：不支持转场动画。  默认值：true |

## MoreButtonOptions19+

PhonePC/2in1TabletTVWearable

更多图标的菜单选项。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| backgroundBlurStyle | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 更多图标的菜单背景模糊样式，不设置时关闭背景模糊效果。 |
| backgroundBlurStyleOptions | [BackgroundBlurStyleOptions](ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 否 | 是 | 更多图标的菜单背景模糊选项。  **说明：**  只在设置了backgroundBlurStyle时生效。  不建议与backgroundEffect同时使用。 |
| backgroundEffect | [BackgroundEffectOptions](ts-universal-attributes-background.md#backgroundeffectoptions11) | 否 | 是 | 设置更多图标的菜单背景属性包括：模糊半径，亮度，饱和度，颜色等。  **说明：**  不建议与backgroundBlurStyleOptions同时使用。 |

## SystemBarStyle12+

PhonePC/2in1TabletTVWearable

type SystemBarStyle = SystemBarStyle

状态栏的属性。在设置页面级状态栏属性时使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [SystemBarStyle](arkts-apis-window-i.md#systembarstyle12) | 状态栏文字颜色。  默认值：'#0xE5FFFFFF' |

## HomePathInfo20+

PhonePC/2in1TabletTVWearable

主页NavDestination的信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 主页NavDestination的页面名称。 |
| param | Object | 否 | 是 | 主页NavDestination的页面详细参数。 |

## 示例

PhonePC/2in1TabletTVWearable

示例效果请以真机为准，系统路由表不支持预览器以及模拟器。

### 示例1（Navigation页面布局）

该示例主要演示Navigation页面的布局包括标题栏[title](ts-basic-components-navigation.md#title)，菜单栏[menus](ts-basic-components-navigation.md#menus)，内容区和工具栏[toolbarConfiguration](ts-basic-components-navigation.md#toolbarconfiguration10)。

```
1. // xxx.ets

3. @Entry
4. @Component
5. struct NavigationExample {
6. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

8. @Builder
9. NavigationTitle() {
10. Column() {
11. Text('Title')
12. .fontColor('#182431')
13. .fontSize(30)
14. .lineHeight(41)
15. .fontWeight(700)
16. Text('subtitle')
17. .fontColor('#182431')
18. .fontSize(14)
19. .lineHeight(19)
20. .opacity(0.4)
21. .margin({ top: 2, bottom: 20 })
22. }.alignItems(HorizontalAlign.Start)
23. }

25. @Builder
26. NavigationMenus() {
27. Row() {
28. // 'resources/base/media/ic_public_add.svg'需要替换为开发者所需的资源文件
29. Image('resources/base/media/ic_public_add.svg')
30. .width(24)
31. .height(24)
32. // 'resources/base/media/ic_public_add.svg'需要替换为开发者所需的资源文件
33. Image('resources/base/media/ic_public_add.svg')
34. .width(24)
35. .height(24)
36. .margin({ left: 24 })
37. // 'resources/base/media/ic_public_more.svg'需要替换为开发者所需的资源文件
38. Image('resources/base/media/ic_public_more.svg')
39. .width(24)
40. .height(24)
41. .margin({ left: 24 })
42. }
43. }

45. build() {
46. Column() {
47. Navigation() {
48. TextInput({ placeholder: 'search...' })
49. .width('90%')
50. .height(40)
51. .backgroundColor('#FFFFFF')
52. .margin({ top: 8 })

54. List({ space: 12, initialIndex: 0 }) {
55. ForEach(this.arr, (item: number) => {
56. ListItem() {
57. Text('' + item)
58. .width('90%')
59. .height(72)
60. .backgroundColor('#FFFFFF')
61. .borderRadius(24)
62. .fontSize(16)
63. .fontWeight(500)
64. .textAlign(TextAlign.Center)
65. }
66. }, (item: number) => item.toString())
67. }
68. .height(324)
69. .width('100%')
70. .margin({ top: 12, left: '10%' })
71. }
72. .title(this.NavigationTitle)
73. .menus(this.NavigationMenus)
74. .titleMode(NavigationTitleMode.Full)
75. .toolbarConfiguration([
76. {
77. // $r("app.string.navigation_toolbar_add")和$r("app.media.ic_public_highlights_ed")需要替换为开发者所需的资源文件
78. value: $r("app.string.navigation_toolbar_add"),
79. icon: $r("app.media.ic_public_highlights_ed")
80. },
81. {
82. // $r("app.string.navigation_toolbar_app")和$r("app.media.ic_public_highlights")需要替换为开发者所需的资源文件
83. value: $r("app.string.navigation_toolbar_app"),
84. icon: $r("app.media.ic_public_highlights")
85. },
86. {
87. // $r("app.string.navigation_toolbar_collect")和$r("app.media.ic_public_highlights")需要替换为开发者所需的资源文件
88. value: $r("app.string.navigation_toolbar_collect"),
89. icon: $r("app.media.ic_public_highlights")
90. }
91. ])
92. .hideTitleBar(false)
93. .hideToolBar(false)
94. .onTitleModeChange((titleModel: NavigationTitleMode) => {
95. console.info('titleMode' + titleModel)
96. })
97. }.width('100%').height('100%').backgroundColor('#F1F3F5')
98. }
99. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/kR3oeSjnSBO0a3ag05ty3A/zh-cn_image_0000002583439707.png?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=CE7DDC2F24E432ABA8B4777F5BA35C814A03521A0A545213C2DCF12BD350927F)

### 示例2（使用导航控制器方法）

该示例主要演示[NavPathStack](ts-basic-components-navigation.md#navpathstack10)中方法的使用及路由拦截。

```
1. // Index.ets
2. @Entry
3. @Component
4. struct NavigationExample {
5. pageInfos: NavPathStack = new NavPathStack();
6. isUseInterception: boolean = false;

8. registerInterception() {
9. this.pageInfos.setInterception({
10. // 页面跳转前拦截，允许操作栈，在当前跳转中生效。
11. willShow: (from: NavDestinationContext | "navBar", to: NavDestinationContext | "navBar",
12. operation: NavigationOperation, animated: boolean) => {
13. if (!this.isUseInterception) {
14. return;
15. }
16. if (typeof to === "string") {
17. console.info("target page is navigation home");
18. return;
19. }
20. // 重定向目标页面，更改为pageTwo页面到pageOne页面。
21. let target: NavDestinationContext = to as NavDestinationContext;
22. if (target.pathInfo.name === 'pageTwo') {
23. target.pathStack.pop();
24. target.pathStack.pushPathByName('pageOne', null);
25. }
26. },
27. // 页面跳转后回调，在该回调中操作栈在下一次跳转中刷新。
28. didShow: (from: NavDestinationContext | "navBar", to: NavDestinationContext | "navBar",
29. operation: NavigationOperation, isAnimated: boolean) => {
30. if (!this.isUseInterception) {
31. return;
32. }
33. if (typeof from === "string") {
34. console.info("current transition is from navigation home");
35. } else {
36. console.info(`current transition is from  ${(from as NavDestinationContext).pathInfo.name}`);
37. }
38. if (typeof to === "string") {
39. console.info("current transition to is navBar");
40. } else {
41. console.info(`current transition is to ${(to as NavDestinationContext).pathInfo.name}`);
42. }
43. },
44. // Navigation单双栏显示状态发生变更时触发该回调。
45. modeChange: (mode: NavigationMode) => {
46. if (!this.isUseInterception) {
47. return;
48. }
49. console.info(`current navigation mode is ${mode}`);
50. }
51. })
52. }

54. build() {
55. Navigation(this.pageInfos) {
56. Column() {
57. Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
58. .width('80%')
59. .height(40)
60. .margin(20)
61. .onClick(() => {
62. this.pageInfos.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈
63. })
64. Button('use interception', { stateEffect: true, type: ButtonType.Capsule })
65. .width('80%')
66. .height(40)
67. .margin(20)
68. .onClick(() => {
69. this.isUseInterception = !this.isUseInterception;
70. if (this.isUseInterception) {
71. this.registerInterception();
72. } else {
73. this.pageInfos.setInterception(undefined);
74. }
75. })
76. }
77. }.title('NavIndex')
78. }
79. }
```

```
1. // PageOne.ets
2. class TmpClass {
3. count: number = 10;
4. }

6. @Builder
7. export function PageOneBuilder(name: string, param: Object) {
8. PageOne()
9. }

11. @Component
12. export struct PageOne {
13. pageInfos: NavPathStack = new NavPathStack();

15. build() {
16. NavDestination() {
17. Column() {
18. Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
19. .width('80%')
20. .height(40)
21. .margin(20)
22. .onClick(() => {
23. let tmp = new TmpClass();
24. this.pageInfos.pushPathByName('pageTwo', tmp); // 将name指定的NavDestination页面信息入栈，传递的数据为param
25. })
26. Button('singletonLaunchMode', { stateEffect: true, type: ButtonType.Capsule })
27. .width('80%')
28. .height(40)
29. .margin(20)
30. .onClick(() => {
31. this.pageInfos.pushPath({ name: 'pageOne' },
32. { launchMode: LaunchMode.MOVE_TO_TOP_SINGLETON }); // 从栈底向栈顶查找，如果指定的名称已经存在，则将对应的NavDestination页面移到栈顶
33. })
34. Button('popToname', { stateEffect: true, type: ButtonType.Capsule })
35. .width('80%')
36. .height(40)
37. .margin(20)
38. .onClick(() => {
39. this.pageInfos.popToName('pageTwo'); // 回退路由栈到第一个名为name的NavDestination页面
40. console.info(`popToName ${JSON.stringify(this.pageInfos)}，` +
41. `返回值 ${JSON.stringify(this.pageInfos.popToName('pageTwo'))}`);
42. })
43. Button('popToIndex', { stateEffect: true, type: ButtonType.Capsule })
44. .width('80%')
45. .height(40)
46. .margin(20)
47. .onClick(() => {
48. this.pageInfos.popToIndex(1); // 回退路由栈到index指定的NavDestination页面
49. console.info(`popToIndex ${JSON.stringify(this.pageInfos)}`);
50. })
51. Button('moveToTop', { stateEffect: true, type: ButtonType.Capsule })
52. .width('80%')
53. .height(40)
54. .margin(20)
55. .onClick(() => {
56. this.pageInfos.moveToTop('pageTwo'); // 将第一个名为name的NavDestination页面移到栈顶
57. console.info(`moveToTop ${JSON.stringify(this.pageInfos)}，` +
58. `返回值 ${JSON.stringify(this.pageInfos.popToName('pageTwo'))}`);
59. })
60. Button('moveIndexToTop', { stateEffect: true, type: ButtonType.Capsule })
61. .width('80%')
62. .height(40)
63. .margin(20)
64. .onClick(() => {
65. this.pageInfos.moveIndexToTop(1); // 将index指定的NavDestination页面移到栈顶
66. console.info(`moveIndexToTop ${JSON.stringify(this.pageInfos)}`);
67. })
68. Button('clear', { stateEffect: true, type: ButtonType.Capsule })
69. .width('80%')
70. .height(40)
71. .margin(20)
72. .onClick(() => {
73. this.pageInfos.clear(); // 清除栈中所有页面
74. })
75. Button('get', { stateEffect: true, type: ButtonType.Capsule })
76. .width('80%')
77. .height(40)
78. .margin(20)
79. .onClick(() => {
80. console.info('-------------------');
81. console.info(`获取栈中所有NavDestination页面的名称 ${JSON.stringify(this.pageInfos.getAllPathName())}`);
82. console.info(`获取index指定的NavDestination页面的参数信息 ${JSON.stringify(this.pageInfos.getParamByIndex(1))}`);
83. console.info(`获取全部名为name的NavDestination页面的参数信息 ${JSON.stringify(this.pageInfos.getParamByName('pageTwo'))}`);
84. console.info(`获取全部名为name的NavDestination页面的位置索引 ${JSON.stringify(this.pageInfos.getIndexByName('pageOne'))}`);
85. console.info(`获取栈大小 ${JSON.stringify(this.pageInfos.size())}`);
86. })
87. }.width('100%').height('100%')
88. }.title('pageOne')
89. .onBackPressed(() => {
90. const popDestinationInfo = this.pageInfos.pop(); // 弹出路由栈栈顶元素
91. console.info(`pop 返回值 ${JSON.stringify(popDestinationInfo)}`);
92. return true;
93. }).onReady((context: NavDestinationContext) => {
94. this.pageInfos = context.pathStack;
95. })
96. }
97. }
```

```
1. // PageTwo.ets
2. @Builder
3. export function PageTwoBuilder(name: string, param: Object) {
4. PageTwo()
5. }

7. @Component
8. export struct PageTwo {
9. pathStack: NavPathStack = new NavPathStack();
10. private menuItems: Array<NavigationMenuItem> = [
11. {
12. // 'resources/base/media/undo.svg'需要替换为开发者所需的资源文件
13. value: "1",
14. icon: 'resources/base/media/undo.svg',
15. },
16. {
17. // 'resources/base/media/redo.svg'需要替换为开发者所需的资源文件
18. value: "2",
19. icon: 'resources/base/media/redo.svg',
20. isEnabled: false,
21. },
22. {
23. // 'resources/base/media/ic_public_ok.svg'需要替换为开发者所需的资源文件
24. value: "3",
25. icon: 'resources/base/media/ic_public_ok.svg',
26. isEnabled: true,
27. }
28. ];

30. build() {
31. NavDestination() {
32. Column() {
33. Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
34. .width('80%')
35. .height(40)
36. .margin(20)
37. .onClick(() => {
38. this.pathStack.pushPathByName('pageOne', null);
39. })
40. }.width('100%').height('100%')
41. }.title('pageTwo')
42. .menus(this.menuItems)
43. .onBackPressed(() => {
44. this.pathStack.pop();
45. return true;
46. })
47. .onReady((context: NavDestinationContext) => {
48. this.pathStack = context.pathStack;
49. console.info(`current page config info is ${JSON.stringify(context.getConfigInRouteMap())}`);
50. })
51. }
52. }
```

在src/main目录下的[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中的module字段里配置"routerMap": "$profile:router\_map"，并在src/main/resources/base/profile目录下新增router\_map.json。router\_map.json示例如下。

```
1. {
2. "routerMap": [
3. {
4. "name": "pageOne",
5. "pageSourceFile": "src/main/ets/pages/PageOne.ets",
6. "buildFunction": "PageOneBuilder",
7. "data": {
8. "description": "this is pageOne"
9. }
10. },
11. {
12. "name": "pageTwo",
13. "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
14. "buildFunction": "PageTwoBuilder"
15. }
16. ]
17. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/oOyh9-OZQQCg5bn4QKTYsA/zh-cn_image_0000002552959662.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=DA5F7D38C98E2C7F81238B9E2E465BD8DBDA1BBB9D6093BD74361B997DB3CA2F)

### 示例3（设置可交互转场动画）

该示例主要演示设置每个[NavDestination](ts-basic-components-navdestination.md)子页面的自定义转场动画及可交互转场动画。

```
1. // Index.ets
2. import { CustomTransition, AnimateCallback } from './CustomNavigationUtils'

4. @Entry
5. @Component
6. struct NavigationExample {
7. pageInfos: NavPathStack = new NavPathStack();

9. aboutToAppear() {
10. if (this.pageInfos === undefined) {
11. this.pageInfos = new NavPathStack();
12. }
13. this.pageInfos.pushPath({ name: 'pageOne', param: CustomTransition.getInstance().getAnimationId() });
14. }

16. build() {
17. Navigation(this.pageInfos) {
18. }
19. .title('NavIndex')
20. .hideNavBar(true)
21. .customNavContentTransition((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => {
22. if (from.mode == NavDestinationMode.DIALOG || to.mode == NavDestinationMode.DIALOG) {
23. return undefined;
24. }

26. // 首页不进行自定义动画
27. if (from.index === -1 || to.index === -1) {
28. return undefined;
29. }

31. CustomTransition.getInstance().operation = operation;
32. if (CustomTransition.getInstance().interactive) {
33. let customAnimation: NavigationAnimatedTransition = {
34. onTransitionEnd: (isSuccess: boolean) => {
35. console.info("===== current transition is " + isSuccess);
36. CustomTransition.getInstance().recoverState();
37. CustomTransition.getInstance().proxy = undefined;
38. },
39. transition: (transitionProxy: NavigationTransitionProxy) => {
40. CustomTransition.getInstance().proxy = transitionProxy;
41. let targetIndex: string | undefined = operation == NavigationOperation.PUSH ?
42. (to.navDestinationId) : (from.navDestinationId);
43. if (targetIndex) {
44. CustomTransition.getInstance().fireInteractiveAnimation(targetIndex, operation);
45. }
46. },
47. isInteractive: CustomTransition.getInstance().interactive
48. }
49. return customAnimation;
50. }
51. let customAnimation: NavigationAnimatedTransition = {
52. onTransitionEnd: (isSuccess: boolean) => {
53. console.info(`current transition result is ${isSuccess}`);
54. },
55. timeout: 7000,
56. // 转场开始时系统调用该方法，并传入转场上下文代理对象
57. transition: (transitionProxy: NavigationTransitionProxy) => {
58. if (!from.navDestinationId || !to.navDestinationId) {
59. return;
60. }
61. // 从封装类CustomTransition中根据子页面的序列获取对应的转场动画回调
62. let fromParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(from.navDestinationId);
63. let toParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(to.navDestinationId);
64. if (operation == NavigationOperation.PUSH) {
65. if (toParam.start) {
66. toParam.start(true, false);
67. }
68. this.getUIContext()?.animateTo({
69. duration: 500, onFinish: () => {
70. transitionProxy.finishTransition();
71. }
72. }, () => {
73. if (toParam.finish) {
74. toParam.finish(true, false);
75. }
76. })
77. } else {
78. if (fromParam.start) {
79. fromParam.start(true, true);
80. }
81. this.getUIContext()?.animateTo({
82. duration: 500, onFinish: () => {
83. transitionProxy.finishTransition();
84. }
85. }, () => {
86. if (fromParam.finish) {
87. fromParam.finish(true, true);
88. }
89. })
90. }
91. }
92. };
93. return customAnimation;
94. })
95. }
96. }
```

```
1. // PageOne.ets
2. import { CustomTransition } from './CustomNavigationUtils';

4. @Builder
5. export function PageOneBuilder(name: string, param: Object) {
6. PageOne()
7. }

9. @Component
10. export struct PageOne {
11. pageInfos: NavPathStack = new NavPathStack();
12. @State translateX: string = '0';
13. pageId: string = '';
14. rectWidth: number = 0;
15. interactive: boolean = false;

17. registerCallback() {
18. CustomTransition.getInstance().registerNavParam(this.pageId, (isPush: boolean, isExit: boolean) => {
19. if (isPush) {
20. this.translateX = '100%';
21. } else {
22. this.translateX = '0';
23. }
24. }, (isPush: boolean, isExit: boolean) => {
25. if (isPush) {
26. this.translateX = '0';
27. } else {
28. this.translateX = '100%';
29. }
30. }, (isPush: boolean, isExit: boolean) => {
31. this.translateX = '0';
32. }, (operation: NavigationOperation) => {
33. if (operation == NavigationOperation.PUSH) {
34. this.translateX = '100%';
35. this.getUIContext()?.animateTo({
36. duration: 1000,
37. onFinish: () => {
38. this.translateX = '0';
39. }
40. }, () => {
41. this.translateX = '0';
42. })
43. } else {
44. this.translateX = '0';
45. this.getUIContext()?.animateTo({
46. duration: 1000,
47. onFinish: () => {
48. this.translateX = '0';
49. }
50. }, () => {
51. this.translateX = '100%';
52. })
53. }
54. }, 200);
55. }

57. build() {
58. NavDestination() {
59. Column() {
60. Button(`setInteractive`)
61. .onClick(() => {
62. CustomTransition.getInstance().interactive = !CustomTransition.getInstance().interactive;
63. this.interactive = CustomTransition.getInstance().interactive;
64. })

66. Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
67. .width('80%')
68. .height(40)
69. .margin(20)
70. .onClick(() => {
71. // 将name指定的NavDestination页面信息入栈，传递的数据为param
72. this.pageInfos.pushDestinationByName('pageTwo', CustomTransition.getInstance().getAnimationId());
73. })
74. }
75. .size({ width: '100%', height: '100%' })
76. }
77. .title('pageOne')
78. .onDisAppear(() => {
79. CustomTransition.getInstance().unRegisterNavParam(this.pageId);
80. })
81. .onReady((context: NavDestinationContext) => {
82. this.pageInfos = context.pathStack;
83. if (context.navDestinationId) {
84. this.pageId = context.navDestinationId;
85. this.registerCallback();
86. }
87. })
88. .translate({ x: this.translateX })
89. .backgroundColor('#F1F3F5')
90. .gesture(PanGesture()
91. .onActionStart((event: GestureEvent) => {
92. this.rectWidth = event.target.area.width as number;
93. if (event.offsetX < 0) {
94. this.pageInfos.pushPath({ name: 'pageTwo', param: CustomTransition.getInstance().getAnimationId() });
95. } else {
96. this.pageInfos.pop();
97. }
98. })
99. .onActionUpdate((event: GestureEvent) => {
100. let rate = event.fingerList[0].localX / this.rectWidth;
101. CustomTransition.getInstance().updateProgress(rate);
102. })
103. .onActionEnd((event: GestureEvent) => {
104. let rate: number = event.fingerList[0].localX / this.rectWidth;
105. CustomTransition.getInstance().finishInteractiveAnimation(rate);
106. }))
107. }
108. }
```

```
1. // PageTwo.ets
2. import { CustomTransition } from './CustomNavigationUtils'

4. @Builder
5. export function PageTwoBuilder(name: string, param: Object) {
6. PageTwo({ param: param as number })
7. }

9. @Component
10. export struct PageTwo {
11. pageInfos: NavPathStack = new NavPathStack();
12. @State translateX: string = '0';
13. pageId: string = '';
14. rectWidth: number = 0;
15. param: number = 0;

17. registerCallback() {
18. CustomTransition.getInstance().registerNavParam(this.pageId, (isPush: boolean, isExit: boolean) => {
19. if (isPush) {
20. this.translateX = '100%'
21. } else {
22. this.translateX = '0';
23. }
24. }, (isPush: boolean, isExit: boolean) => {
25. if (isPush) {
26. this.translateX = '0';
27. } else {
28. this.translateX = '100%';
29. }
30. }, (isPush: boolean, isExit: boolean) => {
31. this.translateX = '0';
32. }, (operation: NavigationOperation) => {
33. if (operation == NavigationOperation.PUSH) {
34. this.translateX = '100%';
35. this.getUIContext()?.animateTo({
36. duration: 500, onFinish: () => {
37. this.translateX = '0';
38. }
39. }, () => {
40. this.translateX = '0';
41. })
42. } else {
43. this.translateX = '0';
44. this.getUIContext()?.animateTo({
45. duration: 500, onFinish: () => {
46. this.translateX = "0";
47. }
48. }, () => {
49. this.translateX = '100%';
50. })
51. }
52. }, 2000)
53. }

55. build() {
56. NavDestination() {
57. Column() {
58. Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
59. .width('80%')
60. .height(40)
61. .margin(20)
62. .onClick(() => {
63. // 将name指定的NavDestination页面信息入栈，传递的数据为param
64. this.pageInfos.pushPath({ name: 'pageOne', param: CustomTransition.getInstance().getAnimationId() });
65. })
66. }
67. .size({ width: '100%', height: '100%' })
68. }
69. .title('pageTwo')
70. .gesture(PanGesture()
71. .onActionStart((event: GestureEvent) => {
72. this.rectWidth = event.target.area.width as number;
73. if (event.offsetX < 0) {
74. this.pageInfos.pushPath({ name: 'pageOne', param: CustomTransition.getInstance().getAnimationId() });
75. } else {
76. this.pageInfos.pop();
77. }
78. })
79. .onActionUpdate((event: GestureEvent) => {
80. let rate = event.fingerList[0].localX / this.rectWidth;
81. CustomTransition.getInstance().updateProgress(rate);
82. })
83. .onActionEnd((event: GestureEvent) => {
84. let rate = event.fingerList[0].localX / this.rectWidth;
85. CustomTransition.getInstance().finishInteractiveAnimation(rate);
86. }))
87. .onAppear(() => {
88. this.registerCallback();
89. })
90. .onDisAppear(() => {
91. CustomTransition.getInstance().unRegisterNavParam(this.pageId);
92. })
93. .onReady((context: NavDestinationContext) => {
94. this.pageInfos = context.pathStack;
95. if (context.navDestinationId) {
96. this.pageId = context.navDestinationId;
97. this.registerCallback();
98. }
99. })
100. .translate({ x: this.translateX })
101. .backgroundColor(Color.Yellow)
102. }
103. }
```

```
1. // src/main/pages/CustomNavigationUtils.ets
2. // 自定义接口，用来保存某个页面相关的转场动画回调和参数

4. export interface AnimateCallback {
5. finish: ((isPush: boolean, isExit: boolean) => void | undefined) | undefined;
6. start: ((isPush: boolean, isExit: boolean) => void | undefined) | undefined;
7. onFinish: ((isPush: boolean, isExit: boolean) => void | undefined) | undefined;
8. interactive: ((operation: NavigationOperation) => void | undefined) | undefined;
9. timeout: (number | undefined) | undefined;
10. }

12. const customTransitionMap: Map<string, AnimateCallback> = new Map();

14. export class CustomTransition {
15. static delegate = new CustomTransition();
16. interactive: boolean = false;
17. proxy: NavigationTransitionProxy | undefined = undefined;
18. private animationId: number = 0;
19. operation: NavigationOperation = NavigationOperation.PUSH;

21. static getInstance() {
22. return CustomTransition.delegate;
23. }

25. /* 注册某个页面的动画回调
26. * name: 注册页面的唯一id
27. * startCallback：用来设置动画开始时页面的状态
28. * endCallback：用来设置动画结束时页面的状态
29. * onFinish：用来执行动画结束后页面的其他操作
30. * interactiveCallback: 注册的可交互转场的动效
31. * timeout：转场结束的超时时间
32. */
33. registerNavParam(name: string, startCallback: (operation: boolean, isExit: boolean) => void,
34. endCallback: (operation: boolean, isExit: boolean) => void,
35. onFinish: (operation: boolean, isExit: boolean) => void,
36. interactiveCallback: (operation: NavigationOperation) => void,
37. timeout: number): void {
38. if (customTransitionMap.has(name)) {
39. let param = customTransitionMap.get(name);
40. if (param != undefined) {
41. param.start = startCallback;
42. param.finish = endCallback;
43. param.timeout = timeout;
44. param.onFinish = onFinish;
45. param.interactive = interactiveCallback;
46. return;
47. }
48. }
49. let params: AnimateCallback = {
50. timeout: timeout,
51. start: startCallback,
52. finish: endCallback,
53. onFinish: onFinish,
54. interactive: interactiveCallback
55. };
56. customTransitionMap.set(name, params);
57. }

59. getAnimationId() {
60. return Date.now();
61. }

63. unRegisterNavParam(name: string): void {
64. customTransitionMap.delete(name);
65. }

67. fireInteractiveAnimation(id: string, operation: NavigationOperation) {
68. let animation = customTransitionMap.get(id)?.interactive;
69. if (!animation) {
70. return;
71. }
72. animation(operation);
73. }

75. updateProgress(progress: number) {
76. if (!this.proxy?.updateTransition) {
77. return;
78. }
79. progress = this.operation == NavigationOperation.PUSH ? 1 - progress : progress;
80. this.proxy?.updateTransition(progress);
81. }

83. cancelTransition() {
84. if (this.proxy?.cancelTransition) {
85. this.proxy.cancelTransition();
86. }
87. }

89. recoverState() {
90. if (!this.proxy?.from.navDestinationId || !this.proxy?.to.navDestinationId) {
91. return;
92. }
93. let fromParam = customTransitionMap.get(this.proxy.from.navDestinationId);
94. if (fromParam?.onFinish) {
95. fromParam.onFinish(false, false);
96. }
97. let toParam = customTransitionMap.get(this.proxy?.to.navDestinationId);
98. if (toParam?.onFinish) {
99. toParam.onFinish(true, true);
100. }
101. }

103. finishTransition() {
104. this.proxy?.finishTransition();
105. }

107. finishInteractiveAnimation(rate: number) {
108. if (this.operation == NavigationOperation.PUSH) {
109. if (rate > 0.5) {
110. if (this.proxy?.cancelTransition) {
111. this.proxy.cancelTransition();
112. }
113. } else {
114. this.proxy?.finishTransition();
115. }
116. } else {
117. if (rate > 0.5) {
118. this.proxy?.finishTransition();
119. } else {
120. if (this.proxy?.cancelTransition) {
121. this.proxy.cancelTransition();
122. }
123. }
124. }
125. }

127. getAnimateParam(name: string): AnimateCallback {
128. let result: AnimateCallback = {
129. start: customTransitionMap.get(name)?.start,
130. finish: customTransitionMap.get(name)?.finish,
131. timeout: customTransitionMap.get(name)?.timeout,
132. onFinish: customTransitionMap.get(name)?.onFinish,
133. interactive: customTransitionMap.get(name)?.interactive,
134. };
135. return result;
136. }
137. }
```

在src/main目录下的[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中的module字段里配置"routerMap": "$profile:router\_map"，并在src/main/resources/base/profile目录下新增router\_map.json。router\_map.json示例如下。

```
1. {
2. "routerMap": [
3. {
4. "name": "pageOne",
5. "pageSourceFile": "src/main/ets/pages/PageOne.ets",
6. "buildFunction": "PageOneBuilder",
7. "data": {
8. "description": "this is pageOne"
9. }
10. },
11. {
12. "name": "pageTwo",
13. "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
14. "buildFunction": "PageTwoBuilder"
15. }
16. ]
17. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/08XkM5VnTZijd8G6_rdyQw/zh-cn_image_0000002583479663.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=1CB488067D80E06CEDDE10939457FD2BC359905868E2F6F88FB1AA19718D2169)

### 示例4（Navigation带参返回）

该示例主要演示Navigation通过[NavPathStack](ts-basic-components-navigation.md#navpathstack10)提供的接口来实现将设置的参数传给上一级页面。

```
1. // Index.ets
2. @Entry
3. @Component
4. struct NavigationExample {
5. pageInfo: NavPathStack = new NavPathStack();

7. build() {
8. Navigation(this.pageInfo) {
9. Column() {
10. Button('StartTest', { stateEffect: true, type: ButtonType.Capsule })
11. .width('80%')
12. .height(40)
13. .margin(20)
14. .onClick(() => {
15. this.pageInfo.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈。
16. })
17. }
18. }.title('NavIndex')
19. }
20. }
```

```
1. // PageOne.ets
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class TmpClass {
5. count: number = 10;
6. }

8. class ParamWithOp {
9. operation: number = 1;
10. count: number = 10;
11. }

13. @Builder
14. export function PageOneBuilder(name: string, param: Object) {
15. PageOne()
16. }

18. @Component
19. export struct PageOne {
20. pageInfo: NavPathStack = new NavPathStack();
21. @State message: string = 'Hello World';

23. build() {
24. NavDestination() {
25. Column() {
26. Text(this.message)
27. .width('80%')
28. .height(50)
29. .margin(10)

31. Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
32. .width('80%')
33. .height(40)
34. .margin(10)
35. .onClick(() => {
36. this.pageInfo.pushPath({
37. name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
38. this.message =
39. `[pushPath]last page is: ${popInfo.info.name},result: ${JSON.stringify(popInfo.result)}`;
40. }
41. }); // 将name指定的NavDestination页面信息入栈，传递的数据为param，添加接收处理结果的onPop回调。
42. })

44. Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
45. .width('80%')
46. .height(40)
47. .margin(10)
48. .onClick(() => {
49. let tmp = new TmpClass();
50. this.pageInfo.pushPathByName('pageTwo', tmp, (popInfo) => {
51. this.message =
52. `[pushPathByName]last page is: ${popInfo.info.name}, result: ${JSON.stringify(popInfo.result)}`;
53. }); // 将name指定的NavDestination页面信息入栈，传递的数据为param，添加接收处理结果的onPop回调。
54. })

56. Button('pushDestination', { stateEffect: true, type: ButtonType.Capsule })
57. .width('80%')
58. .height(40)
59. .margin(10)
60. .onClick(() => {
61. let tmp = new TmpClass();
62. // 将name指定的NavDestination页面信息入栈，传递的数据为param，添加接收处理结果的onPop回调。
63. this.pageInfo.pushDestination({
64. name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
65. this.message =
66. `[pushDestination]last page is: ${popInfo.info.name}, result: ${JSON.stringify(popInfo.result)}`;
67. }
68. }).catch((error: BusinessError) => {
69. console.error(`[pushDestination]failed, error code = ${error.code}, error.message = ${error.message}.`);
70. }).then(() => {
71. console.error('[pushDestination]success.');
72. });
73. })

75. Button('pushDestinationByName', { stateEffect: true, type: ButtonType.Capsule })
76. .width('80%')
77. .height(40)
78. .margin(10)
79. .onClick(() => {
80. let tmp = new TmpClass();
81. // 将name指定的NavDestination页面信息入栈，传递的数据为param，添加接收处理结果的onPop回调。
82. this.pageInfo.pushDestinationByName('pageTwo', tmp, (popInfo) => {
83. this.message =
84. `[pushDestinationByName]last page is: ${popInfo.info.name}, result: ${JSON.stringify(popInfo.result)}`;
85. }).catch((error: BusinessError) => {
86. console.error(`[pushDestinationByName]failed, error code = ${error.code}, error.message = ${error.message}.`);
87. }).then(() => {
88. console.error('[pushDestinationByName]success.');
89. });
90. })

92. Button('pushPathWithoutOnPop', { stateEffect: true, type: ButtonType.Capsule })
93. .width('80%')
94. .height(40)
95. .margin(10)
96. .onClick(() => {
97. this.pageInfo.pushPath({ name: 'pageTwo', param: new ParamWithOp() }); // 将name指定的NavDestination页面信息入栈。
98. })

100. Button('pushPathByNameWithoutOnPop', { stateEffect: true, type: ButtonType.Capsule })
101. .width('80%')
102. .height(40)
103. .margin(10)
104. .onClick(() => {
105. let tmp = new TmpClass();
106. this.pageInfo.pushPathByName('pageTwo', tmp); // 将name指定的NavDestination页面信息入栈，传递的数据为param。
107. })

109. Button('pushDestinationWithoutOnPop', { stateEffect: true, type: ButtonType.Capsule })
110. .width('80%')
111. .height(40)
112. .margin(10)
113. .onClick(() => {
114. let tmp = new TmpClass();
115. // 将name指定的NavDestination页面信息入栈，传递的数据为param，添加接收处理结果的onPop回调。
116. this.pageInfo.pushDestination({ name: 'pageTwo', param: new ParamWithOp() })
117. .catch((error: BusinessError) => {
118. console.error(`[pushDestinationWithoutOnPop]failed, error code = ${error.code}, error.message = ${error.message}.`);
119. }).then(() => {
120. console.error('[pushDestinationWithoutOnPop]success.');
121. });
122. })

124. Button('pushDestinationByNameWithoutOnPop', { stateEffect: true, type: ButtonType.Capsule })
125. .width('80%')
126. .height(40)
127. .margin(10)
128. .onClick(() => {
129. let tmp = new TmpClass();
130. // 将name指定的NavDestination页面信息入栈，传递的数据为param。
131. this.pageInfo.pushDestinationByName('pageTwo', tmp)
132. .catch((error: BusinessError) => {
133. console.error(`[pushDestinationByNameWithoutOnPop]failed, error code = ${error.code}, error.message = ${error.message}.`);
134. }).then(() => {
135. console.error('[pushDestinationByNameWithoutOnPop]success.');
136. });
137. })

139. Button('clear', { stateEffect: true, type: ButtonType.Capsule })
140. .width('80%')
141. .height(40)
142. .margin(10)
143. .onClick(() => {
144. this.pageInfo.clear(); // 清除栈中所有页面。
145. })
146. }.width('100%').height('100%')
147. }.title('pageOne')
148. .onBackPressed(() => {
149. this.pageInfo.pop({ number: 1 }); // 弹出路由栈栈顶元素。
150. return true;
151. }).onReady((context: NavDestinationContext) => {
152. this.pageInfo = context.pathStack;
153. })
154. }
155. }
```

```
1. // PageTwo.ets
2. class resultClass {
3. constructor(count: number) {
4. this.count = count;
5. }

7. count: number = 10;
8. }

10. @Builder
11. export function PageTwoBuilder() {
12. PageTwo();
13. }

15. @Component
16. export struct PageTwo {
17. pathStack: NavPathStack = new NavPathStack();

19. build() {
20. NavDestination() {
21. Column() {
22. Button('pop', { stateEffect: true, type: ButtonType.Capsule })
23. .width('80%')
24. .height(40)
25. .margin(20)
26. .onClick(() => {
27. this.pathStack.pop(new resultClass(1)); // 回退到上一个页面，将处理结果传入push的onPop回调中。
28. })

30. Button('popToName', { stateEffect: true, type: ButtonType.Capsule })
31. .width('80%')
32. .height(40)
33. .margin(20)
34. .onClick(() => {
35. this.pathStack.popToName('pageOne',
36. new resultClass(11)); // 将第一个名为name的NavDestination页面移到栈顶，将处理结果传入push的onPop回调中。
37. })

39. Button('popToIndex', { stateEffect: true, type: ButtonType.Capsule })
40. .width('80%')
41. .height(40)
42. .margin(20)
43. .onClick(() => {
44. this.pathStack.popToIndex(0, new resultClass(111)); // 将index指定的NavDestination页面移到栈顶，将处理结果传入push的onPop回调中。
45. })

47. Button('popWithoutResult', { stateEffect: true, type: ButtonType.Capsule })
48. .width('80%')
49. .height(40)
50. .margin(20)
51. .onClick(() => {
52. this.pathStack.pop();
53. })

55. Button('popToNameWithoutResult', { stateEffect: true, type: ButtonType.Capsule })
56. .width('80%')
57. .height(40)
58. .margin(20)
59. .onClick(() => {
60. this.pathStack.popToName('pageOne');
61. })

63. Button('popToIndexWithoutResult', { stateEffect: true, type: ButtonType.Capsule })
64. .width('80%')
65. .height(40)
66. .margin(20)
67. .onClick(() => {
68. this.pathStack.popToIndex(0);
69. })
70. }.width('100%').height('100%')
71. }.title('pageTwo')
72. .onBackPressed(() => {
73. this.pathStack.pop(new resultClass(0)); // 回退到上一个页面，将处理结果传入push的onPop回调。
74. return true;
75. }).onReady((context: NavDestinationContext) => {
76. this.pathStack = context.pathStack;
77. })
78. }
79. }
```

在src/main目录下的[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中的module字段里配置"routerMap": "$profile:router\_map"，并在src/main/resources/base/profile目录下新增router\_map.json。router\_map.json示例如下。

```
1. {
2. "routerMap": [
3. {
4. "name": "pageOne",
5. "pageSourceFile": "src/main/ets/pages/PageOne.ets",
6. "buildFunction": "PageOneBuilder",
7. "data": {
8. "description": "this is pageOne"
9. }
10. },
11. {
12. "name": "pageTwo",
13. "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
14. "buildFunction": "PageTwoBuilder"
15. }
16. ]
17. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/85BFPzxSRFil4f0Ryq7NpQ/zh-cn_image_0000002552800014.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=18395E1A47E060D49C4FA033CCE1AFF89A3C9494380A8AA94638F187FE001865)

### 示例5（设置背景颜色和模糊效果）

该示例主要演示设置Navigation主页的标题栏、工具栏和[NavDestination](ts-basic-components-navdestination.md)页面的标题栏的背景颜色和背景模糊效果。

```
1. // Index
2. import {
3. COLOR1,
4. COLOR2,
5. BLUR_STYLE_1,
6. BLUR_STYLE_2,
7. BLUR_STYLE_OPTION_1,
8. BLUR_STYLE_OPTION_2,
9. } from './Utils';

11. @Entry
12. @Component
13. struct Index {
14. @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack();
15. @State useColor1: boolean = true;
16. @State useBlur1: boolean = true;
17. @State useBlurOption1: boolean = true;

19. build() {
20. Navigation(this.navPathStack) {
21. Stack({ alignContent: Alignment.Center }) {
22. BackComponent()
23. .width('100%')
24. .height('100%')
25. Column() {
26. Stack({ alignContent: Alignment.Center }) {
27. Button("switch color")
28. .onClick(() => {
29. this.useColor1 = !this.useColor1;
30. })
31. }
32. .width('100%')
33. .layoutWeight(1)

35. Stack({ alignContent: Alignment.Center }) {
36. Button("switch blur")
37. .onClick(() => {
38. this.useBlur1 = !this.useBlur1;
39. })
40. }
41. .width('100%')
42. .layoutWeight(1)

44. Stack({ alignContent: Alignment.Center }) {
45. Button("switch blurOption")
46. .onClick(() => {
47. this.useBlurOption1 = !this.useBlurOption1;
48. })
49. }
50. .width('100%')
51. .layoutWeight(1)

53. Stack({ alignContent: Alignment.Center }) {
54. Button("push page")
55. .onClick(() => {
56. this.navPathStack.pushPathByName('NavigationMenu', null);
57. })
58. }
59. .width('100%')
60. .layoutWeight(1)
61. }
62. .width('100%')
63. .height('80%')
64. }.width('100%')
65. .height('100%')
66. }
67. .width('100%')
68. .height('100%')
69. // 开发者可以设置标题栏的背景颜色和背景模糊效果
70. .title("NavTitle", {
71. backgroundColor: this.useColor1 ? COLOR1 : COLOR2,
72. backgroundBlurStyle: this.useBlur1 ? BLUR_STYLE_1 : BLUR_STYLE_2,
73. barStyle: BarStyle.STACK,
74. backgroundBlurStyleOptions: this.useBlurOption1 ? BLUR_STYLE_OPTION_1 : BLUR_STYLE_OPTION_2,
75. })
76. // 开发者可以设置菜单的背景颜色和背景模糊效果
77. .menus([
78. { value: "A" },
79. { value: "B" },
80. { value: "C" },
81. { value: "D" },
82. ], {
83. moreButtonOptions: {
84. backgroundBlurStyle: this.useBlur1 ? BLUR_STYLE_1 : BLUR_STYLE_2,
85. backgroundBlurStyleOptions: this.useBlurOption1 ? BLUR_STYLE_OPTION_1 : BLUR_STYLE_OPTION_2,
86. }
87. })
88. // 开发者可以设置工具栏的背景颜色和背景模糊效果
89. .toolbarConfiguration([
90. { value: "A" },
91. { value: "B" },
92. { value: "C" },
93. { value: "D" },
94. { value: "E" },
95. { value: "F" }
96. ], {
97. backgroundColor: this.useColor1 ? COLOR1 : COLOR2,
98. backgroundBlurStyle: this.useBlur1 ? BLUR_STYLE_1 : BLUR_STYLE_2,
99. // 开发者可以设置工具栏的菜单的背景颜色和背景模糊效果
100. moreButtonOptions: {
101. backgroundBlurStyle: this.useBlur1 ? BLUR_STYLE_1 : BLUR_STYLE_2,
102. backgroundBlurStyleOptions: this.useBlurOption1 ? BLUR_STYLE_OPTION_1 : BLUR_STYLE_OPTION_2,
103. }
104. })
105. }
106. }

108. @Component
109. export struct BackComponent {
110. build() {
111. Row() {
112. Column() {
113. }
114. .height('100%')
115. .backgroundColor("#3D9DB4")
116. .layoutWeight(9)

118. Column() {
119. }
120. .height('100%')
121. .backgroundColor("#17A98D")
122. .layoutWeight(9)

124. Column() {
125. }
126. .height('100%')
127. .backgroundColor("#FFC000")
128. .layoutWeight(9)
129. }
130. .height('100%')
131. .width('100%')
132. }
133. }
```

```
1. // PageOne.ets
2. import {
3. COLOR1,
4. COLOR2,
5. BLUR_STYLE_1,
6. BLUR_STYLE_2,
7. EFFECT_OPTION_1,
8. EFFECT_OPTION_2
9. } from './Utils';
10. import { BackComponent } from './Index';

12. @Builder
13. export function PageBuilder(name: string, param?: Object) {
14. ColorAndBlur();
15. }

17. @Component
18. struct ColorAndBlur {
19. @State useColor1: boolean = true;
20. @State useBlur1: boolean = true;
21. @State useEffect1: boolean = true;

23. build() {
24. NavDestination() {
25. Stack({ alignContent: Alignment.Center }) {
26. BackComponent()
27. .width('100%')
28. .height('100%')
29. Column() {
30. Stack({ alignContent: Alignment.Center }) {
31. Button("switch color")
32. .onClick(() => {
33. this.useColor1 = !this.useColor1;
34. })
35. }
36. .width('100%')
37. .layoutWeight(1)

39. Stack({ alignContent: Alignment.Center }) {
40. Button("switch blur")
41. .onClick(() => {
42. this.useBlur1 = !this.useBlur1;
43. })
44. }
45. .width('100%')
46. .layoutWeight(1)

48. Stack({ alignContent: Alignment.Center }) {
49. Button("switch effect")
50. .onClick(() => {
51. this.useEffect1 = !this.useEffect1;
52. })
53. }
54. .width('100%')
55. .layoutWeight(1)
56. }
57. .width('100%')
58. .height('100%')
59. }.width('100%')
60. .height('100%')
61. }
62. .width('100%')
63. .height('100%')
64. // 开发者可以设置标题栏的背景颜色和背景模糊效果
65. .title("Destination Title", {
66. backgroundColor: this.useColor1 ? COLOR1 : COLOR2,
67. backgroundBlurStyle: this.useBlur1 ? BLUR_STYLE_1 : BLUR_STYLE_2,
68. barStyle: BarStyle.STACK,
69. backgroundEffect: this.useEffect1 ? EFFECT_OPTION_1 : EFFECT_OPTION_2,
70. })
71. // 开发者可以设置菜单的背景颜色和背景模糊效果
72. .menus([
73. { value: "A" },
74. { value: "B" },
75. { value: "C" },
76. { value: "D" },
77. ], {
78. moreButtonOptions: {
79. backgroundEffect: this.useEffect1 ? EFFECT_OPTION_1 : EFFECT_OPTION_2,
80. }
81. })
82. // 开发者可以设置工具栏的背景颜色和背景模糊效果
83. .toolbarConfiguration([
84. { value: "A" },
85. { value: "B" },
86. { value: "C" },
87. { value: "D" },
88. { value: "E" },
89. { value: "F" }
90. ], {
91. backgroundEffect: this.useEffect1 ? EFFECT_OPTION_1 : EFFECT_OPTION_2,
92. // 开发者可以设置工具栏的菜单的背景颜色和背景模糊效果
93. moreButtonOptions: {
94. backgroundEffect: this.useEffect1 ? EFFECT_OPTION_1 : EFFECT_OPTION_2,
95. }
96. })
97. }
98. }
```

```
1. // Utils.ets
2. export const COLOR1: string = "#80004AAF";
3. export const COLOR2: string = "#802787D9";
4. export const BLUR_STYLE_1: BlurStyle = BlurStyle.BACKGROUND_THIN;
5. export const BLUR_STYLE_2: BlurStyle = BlurStyle.BACKGROUND_THICK;
6. export const BLUR_STYLE_OPTION_1: BackgroundBlurStyleOptions = {
7. colorMode: ThemeColorMode.DARK,
8. adaptiveColor: AdaptiveColor.DEFAULT,
9. blurOptions: { grayscale: [20, 20] },
10. scale: 1
11. };
12. export const BLUR_STYLE_OPTION_2: BackgroundBlurStyleOptions = {
13. colorMode: ThemeColorMode.LIGHT,
14. adaptiveColor: AdaptiveColor.AVERAGE,
15. blurOptions: { grayscale: [20, 20] },
16. scale: 1
17. };
18. export const EFFECT_OPTION_1: BackgroundEffectOptions = {
19. radius: 20,
20. saturation: 10,
21. brightness: 0,
22. color: '#66FFFFFF',
23. adaptiveColor: AdaptiveColor.DEFAULT,
24. blurOptions: { grayscale: [0, 0] },
25. };
26. export const EFFECT_OPTION_2: BackgroundEffectOptions = {
27. radius: 60,
28. saturation: 40,
29. brightness: 1,
30. color: '#661A1A1A',
31. adaptiveColor: AdaptiveColor.AVERAGE,
32. blurOptions: { grayscale: [20, 20] },
33. };
```

在src/main目录下的[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中的module字段里配置"routerMap": "$profile:router\_map"，并在src/main/resources/base/profile目录下新增router\_map.json。router\_map.json示例如下。

```
1. {
2. "routerMap": [
3. {
4. "name": "NavigationMenu",
5. "pageSourceFile": "src/main/ets/pages/PageOne.ets",
6. "buildFunction": "PageBuilder",
7. "data": {
8. "description": "this is pageOne"
9. }
10. }
11. ]
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/eL3R-hLeS5CeO686V_4dXg/zh-cn_image_0000002583439709.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=D56B51C52C320CC099C51547B64ECA7950ED2824EFFE8AC2EDC953CA96372AEB)

### 示例6（嵌套场景下获取外层栈）

该示例主要演示在嵌套Navigation场景下，如何获取父[NavPathStack](ts-basic-components-navigation.md#navpathstack10)。

```
1. @Entry
2. @Component
3. struct NavigationExample1 {
4. @State childNavStack: NavPathStack = new NavPathStack();

6. build() {
7. Navigation() {
8. Stack({ alignContent: Alignment.Center }) {
9. Navigation(this.childNavStack) {
10. Button('push Path to parent Navigation', { stateEffect: true, type: ButtonType.Capsule })
11. .width('80%')
12. .height(40)
13. .margin(20)
14. .onClick(() => {
15. // 可以获取父NavPathStack
16. let parentStack = this.childNavStack.getParent();
17. parentStack?.pushPath({ name: "pageOne" });
18. })
19. }
20. .clip(true)
21. .backgroundColor(Color.Orange)
22. .width('80%')
23. .height('80%')
24. .title('ChildNavigation')
25. }
26. .width('100%')
27. .height('100%')
28. }
29. .backgroundColor(Color.Green)
30. .width('100%')
31. .height('100%')
32. .title('ParentNavigation')
33. }
34. }
```

```
1. // PageOne.ets
2. @Builder
3. export function PageOneBuilder(name: string) {
4. NavDestination() {
5. Text("this is " + name)
6. }
7. .title(name)
8. }
```

在src/main目录下的[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中的module字段里配置"routerMap": "$profile:router\_map"，并在src/main/resources/base/profile目录下新增router\_map.json。router\_map.json示例如下。

```
1. {
2. "routerMap": [
3. {
4. "name": "pageOne",
5. "pageSourceFile": "src/main/ets/pages/PageOne.ets",
6. "buildFunction": "PageOneBuilder",
7. "data": {
8. "description": "this is pageOne"
9. }
10. }
11. ]
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/-Y-CUMO9SCmil1AT9e9uBg/zh-cn_image_0000002552959664.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=774065A253BF691CCE4F418F934C65E9235F2DBC7EEAB74244C67415F23C3A95)

### 示例7（通过onReady获取栈）

该示例主要演示如下两点功能：

1. [NavPathStack](ts-basic-components-navigation.md#navpathstack10)无需声明为状态变量，也可以实现路由栈操作功能。
2. [NavDestination](ts-basic-components-navdestination.md)通过[onReady](ts-basic-components-navdestination.md#onready11)事件能够拿到对应的[NavPathInfo](ts-basic-components-navigation.md#navpathinfo10)和所属的[NavPathStack](ts-basic-components-navigation.md#navpathstack10)。

```
1. class PageParam {
2. constructor(num_: number) {
3. this.num = num_;
4. }

6. num: number = 0;
7. }

9. @Builder
10. export function PageOneBuilder(name: string, param: Object) {
11. PageOne();
12. }

14. @Component
15. struct PageOne {
16. private stack: NavPathStack | null = null;
17. private name: string = "";
18. private paramNum: number = 0;

20. build() {
21. NavDestination() {
22. Column() {
23. Text("NavPathInfo: name: " + this.name + ", paramNum: " + this.paramNum)
24. Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
25. .width('80%')
26. .height(40)
27. .margin(20)
28. .onClick(() => {
29. if (this.stack) {
30. let p = new PageParam(this.paramNum + 1);
31. this.stack.pushPath({ name: "pageOne", param: p });
32. }
33. })
34. Button('pop', { stateEffect: true, type: ButtonType.Capsule })
35. .width('80%')
36. .height(40)
37. .margin(20)
38. .onClick(() => {
39. this.stack?.pop();
40. })
41. }
42. .width('100%')
43. .height('100%')
44. }
45. .title('pageOne')
46. .onReady((ctx: NavDestinationContext) => {
47. // 在NavDestination中能够拿到传来的NavPathInfo和当前所处的NavPathStack
48. try {
49. this.name = ctx?.pathInfo?.name;
50. this.paramNum = (ctx?.pathInfo?.param as PageParam)?.num;
51. this.stack = ctx.pathStack;
52. } catch (e) {
53. console.error(`testTag onReady catch exception: ${JSON.stringify(e)}`);
54. }
55. })
56. }
57. }

59. @Entry
60. @Component
61. struct NavigationExample2 {
62. private stack: NavPathStack = new NavPathStack();

64. build() {
65. Navigation(this.stack) {
66. Stack({ alignContent: Alignment.Center }) {
67. Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
68. .width('80%')
69. .height(40)
70. .margin(20)
71. .onClick(() => {
72. let p = new PageParam(1);
73. this.stack.pushPath({ name: "pageOne", param: p });
74. })
75. }
76. .width('100%')
77. .height('100%')
78. }
79. .width('100%')
80. .height('100%')
81. .title('Navigation')
82. }
83. }
```

在src/main目录下的[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中的module字段里配置"routerMap": "$profile:router\_map"，并在src/main/resources/base/profile目录下新增router\_map.json。router\_map.json示例如下。

```
1. {
2. "routerMap": [
3. {
4. "name": "pageOne",
5. "pageSourceFile": "src/main/ets/pages/Index.ets",
6. "buildFunction": "PageOneBuilder",
7. "data": {
8. "description": "this is pageOne"
9. }
10. }
11. ]
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/5fRnqdmsRDu_hz3VvTOEBw/zh-cn_image_0000002583479665.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=F88ECAD63479D9C6418608D41E352736E4C23F7D81A68BE02B20FCDD22B40B47)

### 示例8（NavDestination生命周期时序）

该示例演示[NavDestination](ts-basic-components-navdestination.md)的[onAppear](ts-universal-events-show-hide.md#onappear)，[onDisAppear](ts-universal-events-show-hide.md#ondisappear)，[onShown](ts-basic-components-navdestination.md#onshown10)，[onHidden](ts-basic-components-navdestination.md#onhidden10)，[onWillAppear](ts-basic-components-navdestination.md#onwillappear12)，[onWillDisappear](ts-basic-components-navdestination.md#onwilldisappear12)，[onWillShow](ts-basic-components-navdestination.md#onwillshow12)，[onWillHide](ts-basic-components-navdestination.md#onwillhide12)接口的生命周期时序。

```
1. @Builder
2. export function PageOneBuilder(name: string, param: Object) {
3. PageOneComponent();
4. }

6. @Component
7. struct PageOneComponent {
8. private stack: NavPathStack | null = null;
9. @State eventStr: string = "";

11. build() {
12. NavDestination() {
13. Column() {
14. Text("event: " + this.eventStr)
15. Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
16. .width('80%')
17. .height(40)
18. .margin(20)
19. .onClick(() => {
20. if (this.stack) {
21. this.stack.pushPath({ name: "pageOne" });
22. }
23. })
24. Button('pop', { stateEffect: true, type: ButtonType.Capsule })
25. .width('80%')
26. .height(40)
27. .margin(20)
28. .onClick(() => {
29. this.stack?.pop();
30. })
31. }
32. .width('100%')
33. .height('100%')
34. }
35. .title('pageOne')
36. .onAppear(() => {
37. this.eventStr += "<onAppear>";
38. })
39. .onDisAppear(() => {
40. this.eventStr += "<onDisAppear>";
41. })
42. .onShown(() => {
43. this.eventStr += "<onShown>";
44. })
45. .onHidden(() => {
46. this.eventStr += "<onHidden>";
47. })
48. .onWillAppear(() => {
49. this.eventStr += "<onWillAppear>";
50. })
51. .onWillDisappear(() => {
52. this.eventStr += "<onWillDisappear>";
53. })
54. .onWillShow(() => {
55. this.eventStr += "<onWillShow>";
56. })
57. .onWillHide(() => {
58. this.eventStr += "<onWillHide>";
59. })
60. // onReady会在onAppear之前调用
61. .onReady((ctx: NavDestinationContext) => {
62. try {
63. this.eventStr += "<onReady>";
64. this.stack = ctx.pathStack;
65. } catch (e) {
66. console.error(`testTag onReady catch exception: ${JSON.stringify(e)}`);
67. }
68. })
69. }
70. }

72. @Entry
73. @Component
74. struct NavigationExample3 {
75. private stack: NavPathStack = new NavPathStack();

77. build() {
78. Navigation(this.stack) {
79. Stack({ alignContent: Alignment.Center }) {
80. Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
81. .width('80%')
82. .height(40)
83. .margin(20)
84. .onClick(() => {
85. this.stack.pushPath({ name: "pageOne" });
86. })
87. }
88. .width('100%')
89. .height('100%')
90. }
91. .width('100%')
92. .height('100%')
93. .title('Navigation')
94. }
95. }
```

在src/main目录下的[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中的module字段里配置"routerMap": "$profile:router\_map"，并在src/main/resources/base/profile目录下新增router\_map.json。router\_map.json示例如下。

```
1. {
2. "routerMap": [
3. {
4. "name": "pageOne",
5. "pageSourceFile": "src/main/ets/pages/Index.ets",
6. "buildFunction": "PageOneBuilder",
7. "data": {
8. "description": "this is pageOne"
9. }
10. }
11. ]
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/ozj-fP7OR7KrsPJ1Fb5B8A/zh-cn_image_0000002552800016.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=4858C0742C02A3B61ACE628A02D724CABCC857B2BC9A439B9364A8FEC36F63CA)

### 示例9（标题栏布局效果）

该示例演示Navigation标题栏STACK布局效果。

```
1. @Entry
2. @Component
3. struct NavigationExample {
4. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];
5. private scrollerForScroll: Scroller = new Scroller();
6. @State barStyle: BarStyle = BarStyle.STANDARD;

8. build() {
9. Column() {
10. Navigation() {
11. Column() {
12. Scroll(this.scrollerForScroll) {
13. Column() {
14. // $r('app.media.image_1')需要替换为开发者所需的资源文件
15. Image($r('app.media.image_1'))// 设置与标题栏高度一致，以便观察STACK效果
16. .height(138)
17. .width('100%')
18. Button('BarStyle.STANDARD')
19. .height('50vp')
20. .onClick(() => {
21. this.barStyle = BarStyle.STANDARD;
22. })
23. Button('BarStyle.STACK')
24. .height('50vp')
25. .margin({ top: 12 })
26. .onClick(() => {
27. this.barStyle = BarStyle.STACK;
28. })

30. ForEach(this.arr, (item: number) => {
31. ListItem() {
32. Text('' + item)
33. .width('100%')
34. .height(100)
35. .fontSize(16)
36. .textAlign(TextAlign.Center)
37. .borderRadius(10)
38. .backgroundColor(Color.Orange)
39. .margin({ top: 12 })
40. }
41. }, (item: number) => item.toString())
42. }
43. }
44. }
45. .width('100%')
46. .height('100%')
47. .backgroundColor(0xDCDCDC)
48. }
49. .title(
50. {
51. main: 'NavTitle',
52. sub: 'subtitle'
53. },
54. {
55. backgroundBlurStyle: BlurStyle.COMPONENT_THICK,
56. barStyle: this.barStyle,
57. }
58. )
59. .titleMode(NavigationTitleMode.Free)
60. .hideTitleBar(false)
61. }.width('100%').height('100%').backgroundColor('#F1F3F5')
62. }
63. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/kQc6fa_aSf6Mc4jed30dIg/zh-cn_image_0000002583439711.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=3D3F248C45E36327BC16EAB5C4D74FBC7E5CD7018942DDC1ECFCCA6C40F5AA8B)

### 示例10（定义导航控制器派生类）

该示例主要演示如何定义[NavPathStack](ts-basic-components-navigation.md#navpathstack10)的派生类和派生类在Navigation中的基本用法。

```
1. // Index.ets
2. import { DerivedNavPathStack, NewParam } from './Utils';

4. @Entry
5. @Component
6. struct Index {
7. derivedStack: DerivedNavPathStack = new DerivedNavPathStack();

9. aboutToAppear(): void {
10. this.derivedStack.setId('origin stack');
11. }

13. build() {
14. Navigation(this.derivedStack) {
15. Button('to Page One').margin(20).onClick(() => {
16. this.derivedStack.pushPath({
17. name: 'pageOne',
18. param: new NewParam('push pageOne in homePage when stack size: ' + this.derivedStack.size())
19. });
20. })
21. }
22. .title('Home Page')
23. }
24. }
```

```
1. // PageOne.ets
2. import { DerivedNavPathStack, NewParam } from './Utils';

4. @Builder
5. export function pageMap(name: string) {
6. PageOne();
7. }

9. @Component
10. struct PageOne {
11. derivedStack: DerivedNavPathStack = new DerivedNavPathStack();
12. curStringifyParam: string = "NA";

14. build() {
15. NavDestination() {
16. Column() {
17. Text(this.derivedStack.getInfo())
18. .margin(10)
19. .fontSize(25)
20. .fontWeight(FontWeight.Bold)
21. .textAlign(TextAlign.Start)
22. Text('current page param info:')
23. .margin(10)
24. .fontSize(25)
25. .fontWeight(FontWeight.Bold)
26. .textAlign(TextAlign.Start)
27. Text(this.curStringifyParam)
28. .margin(20)
29. .fontSize(20)
30. .textAlign(TextAlign.Start)
31. }.backgroundColor(Color.Pink)

33. Button('to Page One').margin(20).onClick(() => {
34. this.derivedStack.pushPath({
35. name: 'pageOne',
36. param: new NewParam('push pageOne in pageOne when stack size: ' + this.derivedStack.size())
37. });
38. })
39. }.title('Page One')
40. .onReady((context: NavDestinationContext) => {
41. console.info('[derive-test] reached PageOne\'s onReady');
42. // 从navdestinationContext获取派生堆栈
43. this.derivedStack = context.pathStack as DerivedNavPathStack;
44. console.info('[derive-test] -- got derivedStack: ' + this.derivedStack.id);
45. this.curStringifyParam = JSON.stringify(context.pathInfo.param);
46. console.info('[derive-test] -- got param: ' + this.curStringifyParam);
47. })
48. }
49. }
```

```
1. // Utils.ets
2. export class DerivedNavPathStack extends NavPathStack {
3. // 用户定义的属性'id'
4. id: string = "__default__";

6. // 派生类中的新功能
7. setId(id: string) {
8. this.id = id;
9. }

11. // 派生类中的新功能
12. getInfo(): string {
13. return "this page used Derived NavPathStack, id: " + this.id;
14. }

16. // 重载NavPathStack的功能
17. pushPath(info: NavPathInfo, animated?: boolean): void
18. pushPath(info: NavPathInfo, options?: NavigationOptions): void
19. pushPath(info: NavPathInfo, secArg?: boolean | NavigationOptions): void {
20. console.info('[derive-test] reached DerivedNavPathStack\'s pushPath');
21. if (typeof secArg === 'boolean') {
22. super.pushPath(info, secArg);
23. } else {
24. super.pushPath(info, secArg);
25. }
26. }

28. // 重写和重载NavPathStack的函数
29. pop(animated?: boolean | undefined): NavPathInfo | undefined
30. pop(result: Object, animated?: boolean | undefined): NavPathInfo | undefined
31. pop(result?: Object, animated?: boolean | undefined): NavPathInfo | undefined {
32. console.info('[derive-test] reached DerivedNavPathStack\'s pop');
33. return super.pop(result, animated);
34. }

36. // 基类的其他功能...
37. }

39. export class NewParam {
40. info: string = "__default_param__";

42. constructor(info: string) {
43. this.info = info;
44. }
45. }
```

在src/main目录下的[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中的module字段里配置"routerMap": "$profile:router\_map"，并在src/main/resources/base/profile目录下新增router\_map.json。router\_map.json示例如下。

```
1. {
2. "routerMap": [
3. {
4. "name": "pageOne",
5. "pageSourceFile": "src/main/ets/pages/PageOne.ets",
6. "buildFunction": "pageMap",
7. "data": {
8. "description": "this is pageOne"
9. }
10. }
11. ]
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/V3ufnjBfTdKSBzPp0NvXvw/zh-cn_image_0000002552959666.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=1E98F023578A0A1CF11C16B982E633FFCC41E421A071ED9DE82AB04AAE973627)

### 示例11（使用Symbol组件）

该示例主要演示Navigation和[NavDestination](ts-basic-components-navdestination.md)如何使用Symbol组件。

```
1. // Index.ets
2. import { SymbolGlyphModifier } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct NavigationExample {
7. @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack();
8. @State menuItems: Array<NavigationMenuItem> = [
9. {
10. // 'resources/base/media/ic_public_ok.svg'需要替换为开发者所需的资源文件
11. value: 'menuItem1',
12. icon: 'resources/base/media/ic_public_ok.svg' // 图标资源路径
13. },
14. {
15. // resources/base/media/ic_public_ok.svg'需要替换为开发者所需的资源文件
16. value: 'menuItem2',
17. icon: 'resources/base/media/ic_public_ok.svg', // 图标资源路径
18. symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red, Color.Green])
19. .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),
20. },
21. {
22. value: 'menuItem3',
23. symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),
24. },
25. ];
26. @State toolItems: Array<ToolbarItem> = [
27. {
28. // 'resources/base/media/ic_public_ok.svg'需要替换为开发者所需的资源文件
29. value: 'toolItem1',
30. icon: 'resources/base/media/ic_public_ok.svg', // 图标资源路径
31. symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),
32. status: ToolbarItemStatus.ACTIVE,
33. activeSymbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red,
34. Color.Green]).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),
35. action: () => {
36. }
37. },
38. {
39. // 'resources/base/media/ic_public_more.svg'需要替换为开发者所需的资源文件
40. value: 'toolItem2',
41. symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_star')),
42. status: ToolbarItemStatus.ACTIVE,
43. activeIcon: 'resources/base/media/ic_public_more.svg', // 图标资源路径
44. action: () => {
45. }
46. },
47. {
48. value: 'toolItem3',
49. symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_star')),
50. status: ToolbarItemStatus.ACTIVE,
51. activeSymbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),
52. action: () => {
53. }
54. }
55. ];

57. build() {
58. Navigation(this.navPathStack) {
59. Column() {
60. Button('跳转').onClick(() => {
61. this.navPathStack.pushPathByName('NavigationMenu', null);
62. })
63. }
64. }
65. .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos_wifi')))
66. .titleMode(NavigationTitleMode.Mini)
67. .menus(this.menuItems)
68. .toolbarConfiguration(this.toolItems)
69. .title('一级页面')
70. }
71. }
```

```
1. // PageOne.ets
2. import { SymbolGlyphModifier } from '@kit.ArkUI';

4. @Builder
5. export function myRouter(name: string, param?: Object) {
6. NavigationMenu();
7. }

9. @Component
10. export struct NavigationMenu {
11. @Consume('navPathStack') navPathStack: NavPathStack;
12. @State menuItems: Array<NavigationMenuItem> = [
13. {
14. // 'resources/base/media/ic_public_ok.svg'需要替换为开发者所需的资源文件
15. value: 'menuItem1',
16. icon: 'resources/base/media/ic_public_ok.svg', // 图标资源路径
17. action: () => {
18. }
19. },
20. {
21. value: 'menuItem2',
22. symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red, Color.Green])
23. .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),
24. action: () => {
25. }
26. },
27. {
28. value: 'menuItem3',
29. symbolIcon: new SymbolGlyphModifier($r('sys.symbol.repeat_1')),
30. action: () => {
31. }
32. },
33. ];

35. build() {
36. NavDestination() {
37. Row() {
38. Column() {
39. }
40. .width('100%')
41. }
42. .height('100%')
43. }
44. .hideTitleBar(false)
45. .title('NavDestination title')
46. .backgroundColor($r('sys.color.ohos_id_color_titlebar_sub_bg'))
47. .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos_star'))
48. .fontColor([Color.Blue]))
49. .menus(this.menuItems)
50. }
51. }
```

在src/main目录下的[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中的module字段里配置"routerMap": "$profile:router\_map"，并在src/main/resources/base/profile目录下新增router\_map.json。router\_map.json示例如下。

```
1. {
2. "routerMap": [
3. {
4. "name": "NavigationMenu",
5. "pageSourceFile": "src/main/ets/pages/PageOne.ets",
6. "buildFunction": "myRouter",
7. "data": {
8. "description": "this is pageOne"
9. }
10. }
11. ]
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/9qqehVflQ0K6j0Cp7-3HzQ/zh-cn_image_0000002583479667.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=6BF1CE9C4D5A54BB793C4E37EBBE92EB43B8973CE78E57E886C039AAB77D24C3)

### 示例12（设置自定义标题栏边距）

该示例主要演示Navigation和[NavDestination](ts-basic-components-navdestination.md)如何设置自定义标题栏边距，如何通过TextModifier修改主副标题文本样式。

```
1. // Index.ets
2. import { LengthMetrics } from '@kit.ArkUI';
3. import { MainTitleTextModifier, SubTitleTextModifier } from './Utils';

5. @Entry
6. @Component
7. struct NavigationExample {
8. private navPathStack: NavPathStack = new NavPathStack();
9. // 初始化标题栏起始端内间距
10. @State paddingStart: LengthMetrics = LengthMetrics.vp(0);
11. // 初始化标题栏结束端内间距
12. @State paddingEnd: LengthMetrics = LengthMetrics.vp(0);
13. // 主标题样式修改器
14. @State mainTitleModifier: MainTitleTextModifier = new MainTitleTextModifier();
15. // 副标题样式修改器
16. @State subTitleModifier: SubTitleTextModifier = new SubTitleTextModifier();
17. @State applyModifier: boolean = false;
18. @State useStyle1: boolean = true;

20. build() {
21. Navigation(this.navPathStack) {
22. Column() {
23. // 标题栏内间距切换
24. Button('apply padding 32vp')
25. .onClick(() => {
26. this.paddingStart = LengthMetrics.vp(32);
27. this.paddingEnd = LengthMetrics.vp(32);
28. })
29. .margin({ top: 70 })
30. .width(180)
31. Button('apply padding 20vp')
32. .onClick(() => {
33. this.paddingStart = LengthMetrics.vp(20);
34. this.paddingEnd = LengthMetrics.vp(20);
35. })
36. .margin({ top: 40 })
37. .width(180)
38. Button('pushPage')
39. .onClick(() => {
40. this.navPathStack.pushPath({ name: 'NavDestinationExample' });
41. })
42. .margin({ top: 40 })
43. .width(180)
44. Row() {
45. Text(`apply Modifier`)
46. Toggle({ isOn: this.applyModifier, type: ToggleType.Switch }).onChange((isOn: boolean) => {
47. this.applyModifier = isOn;
48. })
49. }
50. .padding({ top: 95, left: 5, right: 5 })
51. .width(180)
52. .justifyContent(FlexAlign.SpaceBetween)

54. Row() {
55. Text(`use Style1`)
56. Toggle({ isOn: this.useStyle1, type: ToggleType.Switch }).onChange((isOn: boolean) => {
57. this.mainTitleModifier.useStyle1 = isOn;
58. this.subTitleModifier.useStyle1 = isOn;
59. this.useStyle1 = isOn;
60. })
61. }
62. .padding({ top: 40, left: 5, right: 5 })
63. .width(180)
64. .justifyContent(FlexAlign.SpaceBetween)
65. }
66. .width('100%')
67. .height('100%')
68. }
69. .titleMode(NavigationTitleMode.Full)
70. .title(
71. { main: "Title", sub: "subTitle" },
72. this.applyModifier ?
73. {
74. paddingStart: this.paddingStart,
75. paddingEnd: this.paddingEnd,
76. mainTitleModifier: this.mainTitleModifier,
77. subTitleModifier: this.subTitleModifier,
78. } : {
79. paddingStart: this.paddingStart,
80. paddingEnd: this.paddingEnd
81. })
82. }
83. }
```

```
1. // PageOne.ets
2. import { LengthMetrics } from '@kit.ArkUI';
3. import { MainTitleTextModifier, SubTitleTextModifier } from './Utils';

5. @Builder
6. export function myRouter(name: string, param?: Object) {
7. NavDestinationExample();
8. }
9. @Component
10. export struct NavDestinationExample {
11. @State menuItems: Array<NavigationMenuItem> = [
12. {
13. // 'resources/base/media/ic_public_ok.svg'需要替换为开发者所需的资源文件
14. value: 'menuItem1',
15. icon: 'resources/base/media/ic_public_ok.svg', // 图标资源路径
16. action: () => {
17. }
18. }
19. ];
20. @State paddingStart: LengthMetrics = LengthMetrics.vp(0);
21. @State paddingEnd: LengthMetrics = LengthMetrics.vp(0);
22. // 主标题样式修改器
23. @State mainTitleModifier: MainTitleTextModifier = new MainTitleTextModifier();
24. // 副标题样式修改器
25. @State subTitleModifier: SubTitleTextModifier = new SubTitleTextModifier();
26. @State applyModifier: boolean = false;
27. @State useStyle1: boolean = true;

29. build() {
30. NavDestination() {
31. Column() {
32. // 标题栏内间距切换
33. Button('apply padding 32vp')
34. .onClick(() => {
35. this.paddingStart = LengthMetrics.vp(32);
36. this.paddingEnd = LengthMetrics.vp(32);
37. })
38. .margin({ top: 150 })
39. .width(180)
40. Button('apply padding 20vp')
41. .onClick(() => {
42. this.paddingStart = LengthMetrics.vp(20);
43. this.paddingEnd = LengthMetrics.vp(20);
44. })
45. .margin({ top: 40 })
46. .width(180)
47. Row() {
48. Text(`apply Modifier`)
49. Toggle({ isOn: this.applyModifier, type: ToggleType.Switch }).onChange((isOn: boolean) => {
50. this.applyModifier = isOn;
51. })
52. }
53. .padding({ top: 95, left: 5, right: 5 })
54. .width(180)
55. .justifyContent(FlexAlign.SpaceBetween)

57. Row() {
58. Text(`use Style1`)
59. Toggle({ isOn: this.useStyle1, type: ToggleType.Switch }).onChange((isOn: boolean) => {
60. this.mainTitleModifier.useStyle1 = isOn;
61. this.subTitleModifier.useStyle1 = isOn;
62. this.useStyle1 = isOn;
63. })
64. }
65. .padding({ top: 40, left: 5, right: 5 })
66. .width(180)
67. .justifyContent(FlexAlign.SpaceBetween)
68. }
69. .width('100%')
70. .height('90%')
71. }
72. .hideTitleBar(false)
73. .title(
74. { main: "Title", sub: "subTitle" },
75. this.applyModifier ?
76. {
77. paddingStart: this.paddingStart,
78. paddingEnd: this.paddingEnd,
79. mainTitleModifier: this.mainTitleModifier,
80. subTitleModifier: this.subTitleModifier,
81. } : {
82. paddingStart: this.paddingStart,
83. paddingEnd: this.paddingEnd
84. })
85. .menus(this.menuItems)
86. }
87. }
```

```
1. // Utils.ets
2. import { TextModifier } from '@kit.ArkUI';

4. export class MainTitleTextModifier extends TextModifier {
5. useStyle1: boolean = true;

7. applyNormalAttribute(instance: TextModifier): void {
8. if (this.useStyle1) {
9. console.info(`testTag mainTitle use style1`);
10. instance.fontColor('#FFFFC000');
11. instance.fontSize(35);
12. instance.fontWeight(FontWeight.Bolder);
13. instance.fontStyle(FontStyle.Normal);
14. instance.textShadow({ radius: 5, offsetX: 9 });
15. } else {
16. console.info(`testTag mainTitle use style2`);
17. instance.fontColor('#FF23A98D');
18. instance.fontSize(20);
19. instance.heightAdaptivePolicy(TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST);
20. instance.fontWeight(FontWeight.Lighter);
21. instance.fontStyle(FontStyle.Italic);
22. instance.textShadow({ radius: 3, offsetX: 3 });
23. }
24. }
25. }

27. export class SubTitleTextModifier extends TextModifier {
28. useStyle1: boolean = true;

30. applyNormalAttribute(instance: TextModifier): void {
31. if (this.useStyle1) {
32. console.info(`testTag subTitle use style1`);
33. instance.fontColor('#FFFFC000');
34. instance.fontSize(15);
35. instance.fontWeight(FontWeight.Bolder);
36. instance.fontStyle(FontStyle.Normal);
37. instance.textShadow({ radius: 5, offsetX: 9 });
38. } else {
39. console.info(`testTag subTitle use style2`);
40. instance.fontColor('#FF23A98D');
41. instance.fontSize(10);
42. instance.fontWeight(FontWeight.Lighter);
43. instance.fontStyle(FontStyle.Italic);
44. instance.textShadow({ radius: 3, offsetX: 3 });
45. }
46. }
47. }
```

在src/main目录下的[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中的module字段里配置"routerMap": "$profile:router\_map"，并在src/main/resources/base/profile目录下新增router\_map.json。router\_map.json示例如下。

```
1. {
2. "routerMap": [
3. {
4. "name": "NavDestinationExample",
5. "pageSourceFile": "src/main/ets/pages/PageOne.ets",
6. "buildFunction": "myRouter",
7. "data": {
8. "description": "this is pageOne"
9. }
10. }
11. ]
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/GWqCpmv_RnyJMaN50BlReg/zh-cn_image_0000002552800018.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=A3D571637B97750AC5D36F161FC31312C06678FE04F6E73029B91CC4883AE7CC)

### 示例13（自定义转场动画）

该示例主要实现Navigation简单的自定义转场动画。

```
1. // Index.ets
2. import { AnimateCallback, CustomTransition } from './CustomTransitionUtils'

4. @Entry
5. @Component
6. struct NavigationCustomTransitionExample {
7. pageInfos: NavPathStack = new NavPathStack();

9. aboutToAppear() {
10. this.pageInfos.pushPath({ name: 'PageOne' }, false);
11. }

13. build() {
14. Navigation(this.pageInfos) {
15. }
16. .hideNavBar(true)
17. .customNavContentTransition((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => {
18. // 首页不进行自定义动画
19. if (from.index === -1 || to.index === -1) {
20. return undefined;
21. }

23. let customAnimation: NavigationAnimatedTransition = {
24. timeout: 2000,
25. // 转场开始时系统调用该方法，并传入转场上下文代理对象
26. transition: (transitionProxy: NavigationTransitionProxy) => {
27. if (!from.navDestinationId || !to.navDestinationId) {
28. return;
29. }
30. // 从封装类CustomTransition中根据子页面的序列获取对应的转场动画回调
31. let fromParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(from.navDestinationId);
32. let toParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(to.navDestinationId);
33. // Push动画
34. if (operation == NavigationOperation.PUSH) {
35. if (fromParam.start && toParam.start) {
36. // 设置Push转场的两个页面的动画起点
37. fromParam.start(true, true);
38. toParam.start(true, false);
39. }
40. this.getUIContext()?.animateTo({
41. duration: 500, curve: Curve.Friction, onFinish: () => {
42. // 动画结束后需要手动调用finishTransition，否则在timeout时间后由系统调用
43. transitionProxy.finishTransition();
44. }
45. }, () => {
46. if (fromParam.finish && toParam.finish) {
47. // 设置Push转场的两个页面的动画终点
48. fromParam.finish(true, true);
49. toParam.finish(true, false);
50. }

52. })
53. } else if (operation == NavigationOperation.POP) {
54. // Pop动画
55. if (fromParam.start && toParam.start) {
56. // 设置Pop转场的两个页面的动画起点
57. fromParam.start(false, true);
58. toParam.start(false, false);
59. }
60. this.getUIContext()?.animateTo({
61. duration: 500, curve: Curve.Friction, onFinish: () => {
62. // 动画结束后需要手动调用finishTransition，否则在timeout时间后由系统调用
63. transitionProxy.finishTransition();
64. }
65. }, () => {
66. if (fromParam.finish && toParam.finish) {
67. // 设置Pop转场的两个页面的动画终点
68. fromParam.finish(false, true);
69. toParam.finish(false, false);
70. }
71. })
72. } else {
73. // Replace不做动画
74. }
75. }
76. };
77. return customAnimation;
78. })
79. }
80. }

83. // PageOne
84. @Builder
85. export function PageOneBuilder() {
86. PageContainer({ title: "PageOne" });
87. }

89. // PageTwo
90. @Builder
91. export function PageTwoBuilder() {
92. PageContainer({ title: "PageTwo" });
93. }

95. @Component
96. export struct PageContainer {
97. pageInfos: NavPathStack = new NavPathStack();
98. @State translateY: string = '0';
99. pageId: string = '';
100. title: string = ''

102. registerCallback() {
103. CustomTransition.getInstance().registerNavParam(this.pageId,
104. // 设置转场动画起点，根据不同的转场类型分别设置
105. (isPush: boolean, isExit: boolean) => {
106. if (isPush) {
107. if (isExit) {
108. this.translateY = '0';
109. } else {
110. this.translateY = '100%';
111. }
112. } else {
113. if (isExit) {
114. this.translateY = '0';
115. } else {
116. this.translateY = '0';
117. }
118. }
119. },
120. // 设置转场动画终点，根据不同的转场类型分别设置
121. (isPush: boolean, isExit: boolean) => {
122. if (isPush) {
123. if (isExit) {
124. this.translateY = '0';
125. } else {
126. this.translateY = '0';
127. }
128. } else {
129. if (isExit) {
130. this.translateY = '100%';
131. } else {
132. this.translateY = '0';
133. }
134. }
135. });
136. }

138. build() {
139. NavDestination() {
140. Column() {
141. Button('push next page', { stateEffect: true, type: ButtonType.Capsule })
142. .width('80%')
143. .height(40)
144. .margin(20)
145. .onClick(() => {
146. this.pageInfos.pushPath({ name: this.title == 'PageOne' ? "PageTwo" : "PageOne" });
147. })
148. }
149. .size({ width: '100%', height: '100%' })
150. }
151. .title(this.title)
152. .onDisAppear(() => {
153. // 页面销毁时解注册自定义转场动画参数
154. CustomTransition.getInstance().unRegisterNavParam(this.pageId);
155. })
156. .onReady((context: NavDestinationContext) => {
157. this.pageInfos = context.pathStack;
158. if (context.navDestinationId) {
159. this.pageId = context.navDestinationId;
160. // 页面创建时注册自定义转场动画参数
161. this.registerCallback();
162. }
163. })
164. .translate({ y: this.translateY })
165. .backgroundColor(this.title == 'PageOne' ? '#F1F3F5' : '#ff11dee5')
166. }
167. }
```

```
1. // src/main/pages/CustomTransitionUtils.ts 工具类，用来管理所有页面的自定义动画参数注册和获取等
2. // 自定义接口，用来保存某个页面相关的转场动画回调和参数
3. export interface AnimateCallback {
4. start: ((isPush: boolean, isExit: boolean) => void | undefined) | undefined;
5. finish: ((isPush: boolean, isExit: boolean) => void | undefined) | undefined;
6. }

8. const customTransitionMap: Map<string, AnimateCallback> = new Map();

10. export class CustomTransition {
11. static delegate = new CustomTransition();

13. static getInstance() {
14. return CustomTransition.delegate;
15. }

17. /* 注册某个页面的动画回调
18. * name: 注册页面的唯一id
19. * startCallback：用来设置动画开始时页面的状态
20. * endCallback：用来设置动画结束时页面的状态
21. */
22. registerNavParam(name: string, startCallback: (isPush: boolean, isExit: boolean) => void,
23. endCallback: (isPush: boolean, isExit: boolean) => void): void {
24. if (customTransitionMap.has(name)) {
25. let param = customTransitionMap.get(name);
26. if (param != undefined) {
27. param.start = startCallback;
28. param.finish = endCallback;
29. return;
30. }
31. }
32. let params: AnimateCallback = { start: startCallback, finish: endCallback };
33. customTransitionMap.set(name, params);
34. }

36. unRegisterNavParam(name: string): void {
37. customTransitionMap.delete(name);
38. }

40. getAnimateParam(name: string): AnimateCallback {
41. let result: AnimateCallback = {
42. start: customTransitionMap.get(name)?.start,
43. finish: customTransitionMap.get(name)?.finish
44. };
45. return result;
46. }
47. }
```

在src/main目录下的[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中的module字段里配置"routerMap": "$profile:router\_map"，并在src/main/resources/base/profile目录下新增router\_map.json。router\_map.json示例如下。

```
1. {
2. "routerMap": [
3. {
4. "name": "PageOne",
5. "pageSourceFile": "src/main/ets/pages/Index.ets",
6. "buildFunction": "PageOneBuilder",
7. "data": {
8. "description": "this is pageOne"
9. }
10. },
11. {
12. "name": "PageTwo",
13. "pageSourceFile": "src/main/ets/pages/Index.ets",
14. "buildFunction": "PageTwoBuilder"
15. }
16. ]
17. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/-jBm0SdlSxGDBCsrIuNPlg/zh-cn_image_0000002583439713.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=8318B6C223567DD710E91FB095A33ED60B66CD184C747D11058787369B9A4FBF)

### 示例14（设置Navigation双栏模式）

该示例主要展示Navigation组件在双栏模式下的使用效果，通过[splitPlaceholder](ts-basic-components-navigation.md#splitplaceholder20)设置右侧默认占位页，使用[navBarWidthRange](ts-basic-components-navigation.md#navbarwidthrange10)配置导航栏宽度范围，并借助[divider](ts-basic-components-navigation.md#divider23)属性自定义导航栏与内容区之间的分割线样式。

从API version 20开始，新增splitPlaceholder属性；API version 23开始，新增divider属性。

此示例在运行前需要在工程配置文件[module.json5](../harmonyos-guides/module-configuration-file.md)中的abilities字段里配置"orientation": "auto\_rotation"。

```
1. import { ComponentContent } from '@kit.ArkUI';

3. @Builder function PlaceholderPage() {
4. Column() {
5. Text("分栏模式占位页")
6. .fontSize(28)
7. .fontWeight(700)
8. .margin({ top: 200 })
9. }.width("100%")
10. .height("100%")
11. }

13. @Entry
14. @Component
15. struct NavigationExample {
16. @State minNavBarWidth: Dimension | undefined = undefined;
17. @State maxNavBarWidth: Dimension | undefined = undefined;
18. @State minContentWidth: Dimension|undefined = undefined;
19. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
20. @State currentIndex: number = 0;
21. placeholder = new ComponentContent(this.getUIContext(), wrapBuilder(PlaceholderPage))

23. @Builder
24. NavigationTitle() {
25. Column() {
26. Text('Title')
27. .fontColor('#182431')
28. .fontSize(30)
29. .lineHeight(41)
30. .fontWeight(700)
31. Text('subtitle')
32. .fontColor('#182431')
33. .fontSize(14)
34. .lineHeight(19)
35. .opacity(0.4)
36. .margin({ top: 2, bottom: 20 })
37. }.alignItems(HorizontalAlign.Start)
38. }

40. @Builder
41. NavigationMenus() {
42. Row() {
43. // $r('sys.media.ohos_ic_public_add')需要替换为开发者所需的资源文件
44. Image($r('sys.media.ohos_ic_public_add'))
45. .width(24)
46. .height(24)
47. // $r('sys.media.ohos_ic_public_add')需要替换为开发者所需的资源文件
48. Image($r('sys.media.ohos_ic_public_add'))
49. .width(24)
50. .height(24)
51. .margin({ left: 24 })
52. // $r('sys.media.ohos_ic_public_more')需要替换为开发者所需的资源文件
53. Image($r('sys.media.ohos_ic_public_more'))
54. .width(24)
55. .height(24)
56. .margin({ left: 24 })
57. }.margin({ top: 30 })
58. }

60. build() {
61. Column() {
62. Navigation() {
63. TextInput({ placeholder: 'search...' })
64. .width('90%')
65. .height(40)
66. .backgroundColor('#FFFFFF')
67. .margin({ top: 8 })

69. List({ space: 12, initialIndex: 0 }) {
70. ForEach(this.arr, (item: number) => {
71. ListItem() {
72. Text('' + item)
73. .width('90%')
74. .height(72)
75. .backgroundColor('#FFFFFF')
76. .borderRadius(24)
77. .fontSize(16)
78. .fontWeight(500)
79. .textAlign(TextAlign.Center)
80. }
81. }, (item: number) => item.toString())
82. }
83. .height(324)
84. .width('100%')
85. .margin({ top: 12, left: '10%' })
86. }
87. .title(this.NavigationTitle)
88. .padding({ left: 12 })
89. .menus(this.NavigationMenus)
90. .titleMode(NavigationTitleMode.Full)
91. .toolbarConfiguration([
92. {
93. // $r("app.string.navigation_toolbar_add")和$r("app.media.startIcon")需要替换为开发者所需的图像资源文件
94. value: $r("app.string.navigation_toolbar_add"),
95. icon: $r("app.media.startIcon")
96. },
97. {
98. // $r("app.string.navigation_toolbar_app")和$r("app.media.startIcon")需要替换为开发者所需的图像资源文件
99. value: $r("app.string.navigation_toolbar_app"),
100. icon: $r("app.media.startIcon")
101. },
102. {
103. // $r("app.string.navigation_toolbar_collect")和$r("app.media.startIcon")需要替换为开发者所需的图像资源文件
104. value: $r("app.string.navigation_toolbar_collect"),
105. icon: $r("app.media.startIcon")
106. }
107. ])
108. .mode(NavigationMode.Split) // 设置Navigation模式为Split
109. .navBarWidthRange([this.minNavBarWidth, this.maxNavBarWidth]) // 设置导航页宽度范围：[最小宽度, 最大宽度]
110. .minContentWidth(this.minContentWidth)
111. .hideTitleBar(false)
112. .hideToolBar(false)
113. .onTitleModeChange((titleModel: NavigationTitleMode) => {
114. console.info('titleMode' + titleModel)
115. })
116. .splitPlaceholder(this.placeholder)
117. .divider({ startMargin: 20, endMargin: 20, color: Color.Red}) // 从API version 23开始，新增divider属性。
118. }
119. .width('100%')
120. .height('100%')
121. .backgroundColor('#F1F3F5')
122. }
123. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/OZ5swmJ9SjKfOln9W2b2Xw/zh-cn_image_0000002552959668.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=B035CD20310E2345DE624D7067DBA8D6AEC9409A1DD934E973AB91E45E4BD3C4)

### 示例15（Navigation工具栏自适应）

该示例主要通过[enableToolBarAdaptation](ts-basic-components-navigation.md#enabletoolbaradaptation19)属性展示Navigation工具栏自适应能力的启用及关闭。

从API version 19开始，新增了enableToolBarAdaptation属性。

在工程配置文件[module.json5](../harmonyos-guides/module-configuration-file.md)中的abilities字段里配置"orientation": "landscape"（该工程配置仅方便演示在横屏模式下的Navigation工具栏自适应能力，实际配置可自行设置为"auto\_rotation"）。

```
1. import { SymbolGlyphModifier } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct NavigationExample {
6. @Provide('navPathStack') navPathStack:NavPathStack = new NavPathStack();
7. @State enable: boolean = false
8. @State menuItems:Array<NavigationMenuItem> = [
9. {
10. value:'menuItem1',
11. symbolIcon: new SymbolGlyphModifier($r('sys.symbol.card_writer')),
12. },
13. {
14. value:'menuItem2',
15. symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus'))
16. },
17. {
18. value:'menuItem3',
19. symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),
20. },
21. ]

23. @State toolItems:Array<ToolbarItem> = [
24. {
25. value:'toolItem1',
26. symbolIcon:new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),
27. action:()=>{}
28. },
29. {
30. value:'toolItem2',
31. symbolIcon:new SymbolGlyphModifier($r('sys.symbol.card_migration')),
32. action:()=>{}
33. },
34. {
35. value:'toolItem3',
36. symbolIcon:new SymbolGlyphModifier($r('sys.symbol.ohos_star')),
37. action:()=>{}
38. }
39. ]

41. build() {
42. Navigation(this.navPathStack) {
43. Column() {
44. Button('启用/关闭自适应').onClick(()=> {
45. this.enable = !this.enable;
46. })
47. Text("启用自适应能力：" + this.enable)
48. }
49. }
50. .mode(NavigationMode.Stack)
51. .enableToolBarAdaptation(this.enable) // 是否启用工具栏自适应能力
52. .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos_wifi')))
53. .titleMode(NavigationTitleMode.Mini)
54. .menus(this.menuItems)
55. .toolbarConfiguration(this.toolItems)
56. .title('一级页面')
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/utV3L146TjOmP5fOWNcO7g/zh-cn_image_0000002583479669.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=DD5565750E2535E680464226EA0D14E47B643FBC9620F7D077E360C364A7FFC3)

### 示例16（Navigation使用NavDestination作为导航页）

该示例展示了Navigation组件通过配置[homeDestination](ts-basic-components-navigation.md#navigation20)参数，实现以[NavDestination](ts-basic-components-navdestination.md)作为根导航页的效果。

从API version 20开始，新增创建Navigation组件的方式。

```
1. @Component
2. struct PageHome {
3. private stack: NavPathStack | undefined = undefined;

5. build() {
6. NavDestination() {
7. Stack({alignContent: Alignment.Center}) {
8. Button('push PageOne').onClick(() => {
9. this.stack?.pushPath({name: 'PageOne'});
10. })
11. }.width('100%').height('100%')
12. }.title('PageHome')
13. .onReady((ctx: NavDestinationContext) => {
14. this.stack = ctx.pathStack;
15. })
16. }
17. }

19. @Builder
20. function PageHomeBuilder() {
21. PageHome()
22. }

24. @Component
25. struct PageOne {
26. build() {
27. NavDestination() {
28. Stack({alignContent: Alignment.Center}) {
29. Text('PageOne')
30. }.width('100%').height('100%')
31. }.title('PageOne')
32. }
33. }

35. @Builder
36. function PageOneBuilder() {
37. PageOne()
38. }

40. @Entry
41. @Component
42. struct Index {
43. private stack: NavPathStack = new NavPathStack();

45. build() {
46. // 在这里配置主页NavDestination信息
47. Navigation(this.stack, { name: 'PageHome' }) {
48. }
49. .width('100%').height('100%')
50. }
51. }
```

在src/main目录下的[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中的module字段里配置"routerMap": "$profile:router\_map"，并在src/main/resources/base/profile目录下新增router\_map.json。router\_map.json示例如下。

```
1. {
2. "routerMap": [
3. {
4. "name": "PageHome",
5. "pageSourceFile": "src/main/ets/pages/Index.ets",
6. "buildFunction": "PageHomeBuilder",
7. "data": {
8. "description": "this is PageHome"
9. }
10. },
11. {
12. "name": "PageOne",
13. "pageSourceFile": "src/main/ets/pages/Index.ets",
14. "buildFunction": "PageOneBuilder",
15. "data": {
16. "description": "this is PageOne"
17. }
18. }
19. ]
20. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/abQNj_TGTCmTxOduj9VCLA/zh-cn_image_0000002552800020.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=BBDB98C9C05BA54A07C4AEF69DCB7FC11EBF1371DB5D5C590328357F9FA43890)

### 示例17（使用新增导航控制器方法）

该示例通过设置[setInterception](ts-basic-components-navigation.md#setinterception12)方法来实现路由拦截功能，并在[NavDestinationContext](ts-basic-components-navdestination.md#navdestinationcontext11)中获取mode。

从API version 22开始，在setInterception的参数类型[NavigationInterception](ts-basic-components-navigation.md#navigationinterception12)中新增了interception接口。

```
1. // Index.ets
2. @Entry
3. @Component
4. struct NavigationExample {
5. pageInfos: NavPathStack = new NavPathStack();
6. isUseInterception: boolean = false;

8. registerInterception() {
9. this.pageInfos.setInterception({
10. // 页面创建前拦截，允许操作栈，在当前跳转中生效。
11. interception: (from: NavPathInfo | "navBar", to: NavPathInfo | NavBar, navStack: NavPathStack,
12. operation: NavigationOperation, animated: boolean) => {
13. if (!this.isUseInterception) {
14. return;
15. }
16. if (typeof to === "string") {
17. return;
18. }
19. // 重定向目标页面，更改为pageTwo页面到pageOne页面。
20. let target: NavPathInfo = to as NavPathInfo;
21. let navStacktarget: NavPathStack = navStack as NavPathStack;
22. if (target.name === 'pageTwo') {
23. navStacktarget.pop();
24. navStacktarget.pushPathByName('pageOne', null);
25. }
26. },
27. // 页面跳转后回调，在该回调中操作栈在下一次跳转中刷新。
28. didShow: (from: NavDestinationContext | "navBar", to: NavDestinationContext | "navBar",
29. operation: NavigationOperation, isAnimated: boolean) => {
30. if (!this.isUseInterception) {
31. return;
32. }
33. if (typeof from === "string") {
34. console.info("current transition is from navigation home");
35. } else {
36. console.info(`current transition is from  ${(from as NavDestinationContext).pathInfo.name}`);
37. console.info(`current transition mode is to ${(to as NavDestinationContext).mode?.toString()}`);
38. }
39. if (typeof to === "string") {
40. console.info("current transition to is navBar");
41. } else {
42. console.info(`current transition is to ${(to as NavDestinationContext).pathInfo.name}`);
43. console.info(`current transition mode is to ${(to as NavDestinationContext).mode?.toString()}`);
44. }
45. },
46. // Navigation单双栏显示状态发生变更时触发该回调。
47. modeChange: (mode: NavigationMode) => {
48. if (!this.isUseInterception) {
49. return;
50. }
51. console.info(`current navigation mode is ${mode}`);
52. }
53. })
54. }

56. build() {
57. Navigation(this.pageInfos) {
58. Column() {
59. Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
60. .width('80%')
61. .height(40)
62. .margin(20)
63. .onClick(() => {
64. this.pageInfos.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈。
65. })
66. Button('use interception', { stateEffect: true, type: ButtonType.Capsule })
67. .width('80%')
68. .height(40)
69. .margin(20)
70. .onClick(() => {
71. this.isUseInterception = !this.isUseInterception;
72. if (this.isUseInterception) {
73. this.registerInterception();
74. } else {
75. this.pageInfos.setInterception(undefined);
76. }
77. })
78. }
79. }.title('NavIndex')
80. }
81. }
```

```
1. // PageOne.ets
2. class TmpClass {
3. count: number = 10;
4. }

6. @Builder
7. export function PageOneBuilder(name: string, param: Object) {
8. PageOne()
9. }

11. @Component
12. export struct PageOne {
13. pageInfos: NavPathStack = new NavPathStack();

15. build() {
16. NavDestination() {
17. Column() {
18. Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
19. .width('80%')
20. .height(40)
21. .margin(20)
22. .onClick(() => {
23. let tmp = new TmpClass();
24. this.pageInfos.pushPathByName('pageTwo', tmp); // 将name指定的NavDestination页面信息入栈，传递的数据为param。
25. })
26. Button('singletonLaunchMode', { stateEffect: true, type: ButtonType.Capsule })
27. .width('80%')
28. .height(40)
29. .margin(20)
30. .onClick(() => {
31. this.pageInfos.pushPath({ name: 'pageOne' },
32. { launchMode: LaunchMode.MOVE_TO_TOP_SINGLETON }); // 从栈底向栈顶查找，如果指定的名称已经存在，则将对应的NavDestination页面移到栈顶。
33. })
34. Button('popToname', { stateEffect: true, type: ButtonType.Capsule })
35. .width('80%')
36. .height(40)
37. .margin(20)
38. .onClick(() => {
39. this.pageInfos.popToName('pageTwo'); // 回退路由栈到第一个名为name的NavDestination页面。
40. console.info('popToName' + JSON.stringify(this.pageInfos),
41. '返回值' + JSON.stringify(this.pageInfos.popToName('pageTwo')));
42. })
43. Button('popToIndex', { stateEffect: true, type: ButtonType.Capsule })
44. .width('80%')
45. .height(40)
46. .margin(20)
47. .onClick(() => {
48. this.pageInfos.popToIndex(1); // 回退路由栈到index指定的NavDestination页面。
49. console.info('popToIndex' + JSON.stringify(this.pageInfos));
50. })
51. Button('moveToTop', { stateEffect: true, type: ButtonType.Capsule })
52. .width('80%')
53. .height(40)
54. .margin(20)
55. .onClick(() => {
56. this.pageInfos.moveToTop('pageTwo'); // 将第一个名为name的NavDestination页面移到栈顶。
57. console.info('moveToTop' + JSON.stringify(this.pageInfos),
58. '返回值' + JSON.stringify(this.pageInfos.moveToTop('pageTwo')));
59. })
60. Button('moveIndexToTop', { stateEffect: true, type: ButtonType.Capsule })
61. .width('80%')
62. .height(40)
63. .margin(20)
64. .onClick(() => {
65. this.pageInfos.moveIndexToTop(1); // 将index指定的NavDestination页面移到栈顶。
66. console.info('moveIndexToTop' + JSON.stringify(this.pageInfos));
67. })
68. Button('clear', { stateEffect: true, type: ButtonType.Capsule })
69. .width('80%')
70. .height(40)
71. .margin(20)
72. .onClick(() => {
73. this.pageInfos.clear(); // 清除栈中所有页面。
74. })
75. Button('get', { stateEffect: true, type: ButtonType.Capsule })
76. .width('80%')
77. .height(40)
78. .margin(20)
79. .onClick(() => {
80. console.info('-------------------');
81. console.info('获取栈中所有NavDestination页面的名称', JSON.stringify(this.pageInfos.getAllPathName()));
82. console.info('获取index指定的NavDestination页面的参数信息',
83. JSON.stringify(this.pageInfos.getParamByIndex(1)));
84. console.info('获取全部名为name的NavDestination页面的参数信息',
85. JSON.stringify(this.pageInfos.getParamByName('pageTwo')));
86. console.info('获取全部名为name的NavDestination页面的位置索引',
87. JSON.stringify(this.pageInfos.getIndexByName('pageOne')));
88. console.info('获取栈大小', JSON.stringify(this.pageInfos.size()));
89. })
90. }.width('100%').height('100%')
91. }.title('pageOne')
92. .onBackPressed(() => {
93. const popDestinationInfo = this.pageInfos.pop(); // 弹出路由栈栈顶元素。
94. console.info('pop' + '返回值' + JSON.stringify(popDestinationInfo));
95. return true;
96. }).onReady((context: NavDestinationContext) => {
97. this.pageInfos = context.pathStack;
98. })
99. }
100. }
```

```
1. // PageTwo.ets
2. @Builder
3. export function PageTwoBuilder(name: string, param: Object) {
4. PageTwo()
5. }

7. @Component
8. export struct PageTwo {
9. pathStack: NavPathStack = new NavPathStack();
10. private menuItems: Array<NavigationMenuItem> = [
11. {
12. value: "1",
13. icon: 'resources/base/media/undo.svg',
14. },
15. {
16. value: "2",
17. icon: 'resources/base/media/redo.svg',
18. isEnabled: false,
19. },
20. {
21. value: "3",
22. icon: 'resources/base/media/ic_public_ok.svg',
23. isEnabled: true,
24. }
25. ];

27. build() {
28. NavDestination() {
29. Column() {
30. Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
31. .width('80%')
32. .height(40)
33. .margin(20)
34. .onClick(() => {
35. this.pathStack.pushPathByName('pageOne', null);
36. })
37. }.width('100%').height('100%')
38. }.title('pageTwo')
39. .menus(this.menuItems)
40. .onBackPressed(() => {
41. this.pathStack.pop();
42. return true;
43. })
44. .onReady((context: NavDestinationContext) => {
45. this.pathStack = context.pathStack;
46. console.info("current page config info is " + JSON.stringify(context.getConfigInRouteMap()));
47. })
48. }
49. }
```

在src/main目录下的工程配置文件[module.json5](../harmonyos-guides/module-configuration-file.md)中的module字段里配置"routerMap": "$profile:router\_map"。

```
1. // src/main/resources/base/profile/router_map.json
2. {
3. "routerMap": [
4. {
5. "name": "pageOne",
6. "pageSourceFile": "src/main/ets/pages/PageOne.ets",
7. "buildFunction": "PageOneBuilder",
8. "data": {
9. "description": "this is pageOne"
10. }
11. },
12. {
13. "name": "pageTwo",
14. "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
15. "buildFunction": "PageTwoBuilder"
16. }
17. ]
18. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/XfavA2qOQ5Cfm-d-981OKQ/zh-cn_image_0000002583439715.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=3A97E13E4045490B0634396B7AE30B6B9C8A2CEB13C9C51AD738A3F10B595758)

### 示例18（设置Navigation可恢复）

该示例演示如何使用[recoverable](ts-basic-components-navigation.md#recoverable14)配置Navigation可恢复，需要开发者在应用模块初始化时启用[UIAbility](js-apis-app-ability-uiability.md)的备份恢复功能，可参考[UIAbility备份恢复](../harmonyos-guides/ability-recover-guideline.md)。

从API version 14开始，新增recoverable接口。

```
1. // Index.ets
2. import { SymbolGlyphModifier } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct NavigationExample {
7. navPathStack: NavPathStack = new NavPathStack();
8. @State menuItems: Array<NavigationMenuItem> = [
9. {
10. // 'resources/base/media/startIcon.png'需要替换为开发者所需的资源文件
11. value: 'menuItem1',
12. icon: 'resources/base/media/startIcon.png' // 图标资源路径
13. },
14. {
15. // resources/base/media/ic_public_ok.svg'需要替换为开发者所需的资源文件
16. value: 'menuItem2',
17. icon: 'resources/base/media/ic_public_ok.svg', // 图标资源路径
18. symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red, Color.Green])
19. .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),
20. },
21. {
22. value: 'menuItem3',
23. symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),
24. },
25. ];
26. @State toolItems: Array<ToolbarItem> = [
27. {
28. // 'resources/base/media/ic_public_ok.svg'需要替换为开发者所需的资源文件
29. value: 'toolItem1',
30. icon: 'resources/base/media/ic_public_ok.svg', // 图标资源路径
31. symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),
32. status: ToolbarItemStatus.ACTIVE,
33. activeSymbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red,
34. Color.Green]).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),
35. action: () => {
36. }
37. },
38. {
39. // 'resources/base/media/startIcon.png'需要替换为开发者所需的资源文件
40. value: 'toolItem2',
41. symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_star')),
42. status: ToolbarItemStatus.ACTIVE,
43. activeIcon: 'resources/base/media/startIcon.png', // 图标资源路径
44. action: () => {
45. }
46. },
47. {
48. value: 'toolItem3',
49. symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_star')),
50. status: ToolbarItemStatus.ACTIVE,
51. activeSymbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),
52. action: () => {
53. }
54. }
55. ];

57. build() {
58. Navigation(this.navPathStack) {
59. Column() {
60. Button('跳转').onClick(() => {
61. this.navPathStack.pushPathByName('NavigationMenu', null);
62. })
63. }
64. }
65. .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos_wifi')))
66. .titleMode(NavigationTitleMode.Mini)
67. .menus(this.menuItems)
68. .toolbarConfiguration(this.toolItems)
69. .title('一级页面')
70. .id('test')
71. .recoverable(true)
72. }
73. }
```

```
1. // PageOne.ets
2. import { SymbolGlyphModifier } from '@kit.ArkUI';

4. @Builder
5. export function myRouter(name: string, param?: Object) {
6. NavigationMenu();
7. }

9. @Component
10. export struct NavigationMenu {
11. navPathStack: NavPathStack = new NavPathStack();
12. @State menuItems: Array<NavigationMenuItem> = [
13. {
14. // 'resources/base/media/startIcon.png'需要替换为开发者所需的资源文件
15. value: 'menuItem1',
16. icon: 'resources/base/media/startIcon.png', // 图标资源路径
17. action: () => {
18. }
19. },
20. {
21. value: 'menuItem2',
22. symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red, Color.Green])
23. .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),
24. action: () => {
25. }
26. },
27. {
28. value: 'menuItem3',
29. symbolIcon: new SymbolGlyphModifier($r('sys.symbol.repeat_1')),
30. action: () => {
31. }
32. },
33. ];

35. build() {
36. NavDestination() {
37. Row() {
38. Column() {
39. }
40. .width('100%')
41. }
42. .height('100%')
43. }
44. .onReady((context: NavDestinationContext) => {
45. this.navPathStack = context.pathStack;
46. })
47. .hideTitleBar(false)
48. .title('NavDestination title')
49. .backgroundColor($r('sys.color.ohos_id_color_titlebar_sub_bg'))
50. .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos_star'))
51. .fontColor([Color.Blue]))
52. .menus(this.menuItems)
53. .recoverable(true)
54. }
55. }
```

在src/main目录下[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中的module字段里配置"routerMap": "$profile:router\_map"，并在src/main/resources/base/profile目录下新增router\_map.json文件。示例如下：

```
1. {
2. "routerMap": [
3. {
4. "name": "NavigationMenu",
5. "pageSourceFile": "src/main/ets/pages/PageOne.ets",
6. "buildFunction": "myRouter",
7. "data": {
8. "description": "this is pageOne"
9. }
10. }
11. ]
12. }
```

说明

为模拟进程异常退出并重新冷启动，可执行以下步骤：

1. 工程运行成功后点击跳转按钮。
2. 应用上划回退到后台，开启命令行窗口。
3. 输入"hdc shell"，回车后输入"pidof 工程包名"，查询pid值。
4. 输入"aa force-stop 工程包名 -p pid值 -r RESOURCE\_CONTROL"进行回车，模拟资源使用不当导致的应用退出。
5. 点击应用重新进入，可发现页面依然是点击跳转按钮后的页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/YrVraf_nTRS-jIfnEolymQ/zh-cn_image_0000002552959670.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=F52720F76F173245D8D4CA3055785859F47F5ED428D19F128B4F6F85D8F6AF0D)
