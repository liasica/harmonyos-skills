---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabcontent
title: TabContent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 导航与切换 > TabContent
category: harmonyos-references
scraped_at: 2026-04-28T08:01:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d9fb640cd90d56917f0d0b28bb7996dd55382659acd18f3603a239197b4833c5
---

仅在Tabs中使用，对应一个切换页签的内容视图。

说明

* 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件默认设置了[clip](ts-universal-attributes-sharp-clipping.md#clip12)属性的值为true，若需要扩展内容区到组件外显示，需先关闭clip属性。

## 子组件

PhonePC/2in1TabletTVWearable

支持单个子组件。

说明

可内置系统组件和自定义组件，支持渲染控制类型（[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)、[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)和[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)）。

## 接口

PhonePC/2in1TabletTVWearable

TabContent()

创建TabContent页签和内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### tabBar

PhonePC/2in1TabletTVWearable

tabBar(options: string | Resource | CustomBuilder | TabBarOptions)

设置TabBar上显示内容。

如果icon采用svg格式图源，需删除svg图源内置的宽高属性值。否则，icon大小将使用svg图源内置的宽高属性值。

设置的内容超出tabBar页签时进行裁切。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | string | [Resource](ts-types.md#resource) |  [CustomBuilder](ts-types.md#custombuilder8)8+|  [TabBarOptions](ts-container-tabcontent.md#tabbaroptions18对象说明)18+ | 是 | TabBar上显示内容。  CustomBuilder： 构造器，内部可以传入组件（API version 8版本以上适用）。 |

### tabBar9+

PhonePC/2in1TabletTVWearable

tabBar(value: SubTabBarStyle | BottomTabBarStyle)

设置TabBar上显示内容。底部样式没有下划线效果。icon异常时显示灰色图块。

说明

* 子页签（[SubTabBarStyle](ts-container-tabcontent.md#subtabbarstyle9)）样式：通常为文字+下划线，文字+背板的页签风格，允许设置文本样式，建议放置在顶部或者底部使用。切换页签时默认支持动画跳转效果。适用于资讯类应用的顶部分类（如"关注、视频、数码"）、功能模块的二级导航场景。
* 底部页签/侧边页签（[BottomTabBarStyle](ts-container-tabcontent.md#bottomtabbarstyle9)）样式：无下划线和背板效果，页签样式通常为图标+文字的组合方式。切换页签时默认无动画跳转效果。底部页签通常用于应用主导航（如首页、发现、推荐）。侧边页签适用于宽屏场景，可设置vertical(true)启用纵向布局，让页签在侧边显示，默认左侧显示。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SubTabBarStyle](ts-container-tabcontent.md#subtabbarstyle9) | [BottomTabBarStyle](ts-container-tabcontent.md#bottomtabbarstyle9) | 是 | TabBar上显示内容。  SubTabBarStyle： 子页签样式。  BottomTabBarStyle： 底部页签和侧边页签样式。 |

### tabBar18+

PhonePC/2in1TabletTVWearable

tabBar(content: ComponentContent | SubTabBarStyle | BottomTabBarStyle | string | Resource | CustomBuilder | TabBarOptions)

设置TabBar上显示内容。

使用BottomTabBarStyle或TabBarOptions类型作为入参并设置icon，icon异常时显示灰色图块。如果icon采用svg格式图源，需删除svg图源内置的宽高属性值。否则，icon大小将使用svg图源内置的宽高属性值。

设置的内容超出TabBar页签时进行裁切。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](js-apis-arkui-componentcontent.md) |  [SubTabBarStyle](ts-container-tabcontent.md#subtabbarstyle9) |[BottomTabBarStyle](ts-container-tabcontent.md#bottomtabbarstyle9) |  string | [Resource](ts-types.md#resource) |  [CustomBuilder](ts-types.md#custombuilder8)|  [TabBarOptions](ts-container-tabcontent.md#tabbaroptions18对象说明) | 是 | TabBar上显示内容。  ComponentContent： 组件内容的实体封装，可以设置自定义内容。  SubTabBarStyle： 子页签样式。  BottomTabBarStyle： 底部页签和侧边页签样式，底部样式没有下划线效果。  string： 字符串类型。  Resource： 资源引用类型，引入系统资源或者应用资源中的字符串。  CustomBuilder： 构造器，内部可以传入组件。  TabBarOptions： 设置页签内的图片和文字内容。 |

说明

* TabContent组件不支持设置通用宽度属性，其宽度默认撑满Tabs父组件。
* TabContent组件不支持设置通用高度属性，其高度由Tabs父组件高度与TabBar组件高度决定。
* vertical属性为false时，上述2个限制交换。
* TabContent组件不支持内容过长时页面的滑动，如需页面滑动，可嵌套List使用。
* 建议对Tabs组件的所有TabContent子组件的tabBar属性，采用统一的参数类型。
* 若TabContent内部有可获焦组件，Tabs组件内TabContent组件和TabBar组件之间的走焦，仅支持通过键盘的方向键控制。
* TabBar的属性动态修改后，会重新进行渲染，更新相关属性并重置所有页签位置。

## TabBarOptions18+对象说明

PhonePC/2in1TabletTVWearable

设置页签内的图片和文字内容。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon7+ | string | [Resource](ts-types.md#resource) | 否 | 是 | 页签内的图片内容。未设置时不显示图片。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| text7+ | string | [Resource](ts-types.md#resource) | 否 | 是 | 页签内的文字内容。未设置时不显示文字。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## SubTabBarStyle9+

PhonePC/2in1TabletTVWearable

子页签样式。打开后在切换页签时会播放跳转动画。

### constructor

PhonePC/2in1TabletTVWearable

constructor(content: ResourceStr)

SubTabBarStyle的构造函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ResourceStr](ts-types.md#resourcestr) | 是 | 页签内的文字内容。 |

### constructor12+

PhonePC/2in1TabletTVWearable

constructor(content: ResourceStr | ComponentContent)

SubTabBarStyle的构造函数。支持ComponentContent设置自定义内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ResourceStr](ts-types.md#resourcestr) | [ComponentContent](js-apis-arkui-componentcontent.md) | 是 | 页签内的内容。  **说明：**  1.自定义内容不支持labelStyle属性。  2.自定义内容超出页签范围，则不显示超出部分。  3.自定义内容小于页签范围，则会居中对齐。  4.自定义内容异常或无可用显示组件，则显示空白。 |

### of10+

PhonePC/2in1TabletTVWearable

static of(content: ResourceStr): SubTabBarStyle

SubTabBarStyle的静态构造函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ResourceStr](ts-types.md#resourcestr) | 是 | 页签内的文字内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubTabBarStyle](ts-container-tabcontent.md#subtabbarstyle9) | 返回创建的SubTabBarStyle对象。 |

### of12+

PhonePC/2in1TabletTVWearable

static of(content: ResourceStr | ComponentContent): SubTabBarStyle

SubTabBarStyle的静态构造函数。支持ComponentContent设置自定义内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ResourceStr](ts-types.md#resourcestr) | [ComponentContent](js-apis-arkui-componentcontent.md) | 是 | 页签内的内容。支持ComponentContent设置自定义内容。  **说明：**  1.自定义内容不支持labelStyle属性。  2.自定义内容超出页签范围，则不显示超出部分。  3.自定义内容小于页签范围，则会居中对齐。  4.自定义内容异常或无可用显示组件，则显示空白。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubTabBarStyle](ts-container-tabcontent.md#subtabbarstyle9) | 返回创建的SubTabBarStyle对象。 |

### indicator10+

PhonePC/2in1TabletTVWearable

indicator(value: IndicatorStyle): SubTabBarStyle

设置选中子页签的下划线风格。子页签的下划线风格仅在水平模式下有效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [IndicatorStyle](ts-container-tabcontent.md#indicatorstyle10对象说明) | 是 | 选中子页签的下划线风格对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubTabBarStyle](ts-container-tabcontent.md#subtabbarstyle9) | 返回SubTabBarStyle对象本身。 |

### indicator22+

PhonePC/2in1TabletTVWearable

indicator(value: IndicatorStyle | DrawableTabBarIndicator): SubTabBarStyle

设置选中子页签的下划线风格。与[indicator](ts-container-tabcontent.md#indicator10)相比，新增了图片格式的下划线风格，图片的显示效果参照[ImageFit.Cover](ts-appendix-enums.md#imagefit)。子页签的下划线风格仅在水平模式下有效。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [IndicatorStyle](ts-container-tabcontent.md#indicatorstyle10对象说明) | [DrawableTabBarIndicator](ts-container-tabcontent.md#drawabletabbarindicator22对象说明) | 是 | 选中子页签的下划线风格对象。  IndicatorStyle：一般形式的下划线样式。  DrawableTabBarIndicator：图片形式的下划线样式。 |

说明

* 一般形式的下划线样式（IndicatorStyle）：为一条实线，切换页签时默认支持动画跳转效果。
* 图片形式的下划线样式（DrawableTabBarIndicator）：为一张图片，切换页签时默认无动画跳转效果。当传入无效图源时将显示一般形式的下划线。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubTabBarStyle](ts-container-tabcontent.md#subtabbarstyle9) | 返回SubTabBarStyle对象本身。 |

### selectedMode10+

PhonePC/2in1TabletTVWearable

selectedMode(value: SelectedMode): SubTabBarStyle

设置选中子页签的显示方式。子页签的显示方式仅在水平模式下有效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SelectedMode](ts-container-tabcontent.md#selectedmode10枚举说明) | 是 | 选中子页签的显示方式。  默认值：SelectedMode.INDICATOR |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubTabBarStyle](ts-container-tabcontent.md#subtabbarstyle9) | 返回SubTabBarStyle对象本身。 |

### board10+

PhonePC/2in1TabletTVWearable

board(value: BoardStyle): SubTabBarStyle

设置选中子页签的背板风格。子页签的背板风格仅在水平模式下有效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BoardStyle](ts-container-tabcontent.md#boardstyle10对象说明) | 是 | 选中子页签的背板风格对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubTabBarStyle](ts-container-tabcontent.md#subtabbarstyle9) | 返回SubTabBarStyle对象本身。 |

### labelStyle10+

PhonePC/2in1TabletTVWearable

labelStyle(value: LabelStyle): SubTabBarStyle

设置子页签的label文本和字体的样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LabelStyle](ts-container-tabcontent.md#labelstyle10对象说明) | 是 | 子页签的label文本和字体的样式对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubTabBarStyle](ts-container-tabcontent.md#subtabbarstyle9) | 返回SubTabBarStyle对象本身。 |

### padding10+

PhonePC/2in1TabletTVWearable

padding(value: Padding | Dimension): SubTabBarStyle

设置子页签的内边距属性（不支持百分比设置）。使用Dimension时，四个方向内边距同时生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Padding](ts-types.md#padding) | [Dimension](ts-types.md#dimension10) | 是 | 子页签的内边距属性。  取值范围：[0, +∞]  默认值：{left:8.0vp,right:8.0vp,top:17.0vp,bottom:18.0vp} |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubTabBarStyle](ts-container-tabcontent.md#subtabbarstyle9) | 返回SubTabBarStyle对象本身。 |

### padding12+

PhonePC/2in1TabletTVWearable

padding(padding: LocalizedPadding): SubTabBarStyle

设置子页签的内边距属性，支持镜像能力（不支持百分比设置）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| padding | [LocalizedPadding](ts-types.md#localizedpadding12) | 是 | 子页签的内边距属性。  取值范围：[0, +∞]  默认值：{start:LengthMetrics.vp(8),end:LengthMetrics.vp(8),  top:LengthMetrics.vp(17),bottom:LengthMetrics.vp(18)} |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubTabBarStyle](ts-container-tabcontent.md#subtabbarstyle9) | 返回SubTabBarStyle对象本身。 |

### id11+

PhonePC/2in1TabletTVWearable

id(value: string): SubTabBarStyle

设置子页签的[id](ts-universal-attributes-component-id.md#id)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 子页签的[id](ts-universal-attributes-component-id.md#id)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubTabBarStyle](ts-container-tabcontent.md#subtabbarstyle9) | 返回SubTabBarStyle对象本身。 |

## IndicatorStyle10+对象说明

PhonePC/2in1TabletTVWearable

下划线风格对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 下划线的颜色和背板颜色。  默认值：#FF007DFF |
| height | [Length](ts-types.md#length) | 否 | 是 | 下划线的高度（不支持百分比设置）。  默认值：2.0  单位：vp  取值范围：[0, +∞)。 |
| width | [Length](ts-types.md#length) | 否 | 是 | 下划线的宽度（不支持百分比设置）。  默认值：0.0  单位：vp  取值范围：[0, +∞)。  **说明：**  宽度设置为0时，按页签文本宽度显示。 |
| borderRadius | [Length](ts-types.md#length) | 否 | 是 | 下划线的圆角半径（不支持百分比设置）。  默认值：0.0  单位：vp  取值范围：[0, +∞)。 |
| marginTop | [Length](ts-types.md#length) | 否 | 是 | 下划线与文字的间距（不支持百分比设置）。  默认值：8.0  单位：vp  取值范围：[0, +∞)。 |

## DrawableTabBarIndicator22+对象说明

PhonePC/2in1TabletTVWearable

使用图片资源作为下划线的对象。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| drawable | [DrawableDescriptor](ts-container-tabcontent.md#drawabledescriptor22) | 否 | 是 | 下划线的图源。  支持[DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor)、[PixelMapDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#pixelmapdrawabledescriptor12)、[LayeredDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#layereddrawabledescriptor)和[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)类型。当传入无效图源时将显示默认的实线型下划线。 |
| height | [Length](ts-types.md#length) | 否 | 是 | 下划线的高度（不支持百分比设置）。  默认值：2.0  单位：vp  取值范围：[0, +∞) |
| width | [Length](ts-types.md#length) | 否 | 是 | 下划线的宽度（不支持百分比设置）。  默认值：0.0  单位：vp  取值范围：[0, +∞)  宽度设置为0时，按页签文本宽度显示。 |
| borderRadius | [Length](ts-types.md#length) | 否 | 是 | 下划线的圆角半径（不支持百分比设置）。  默认值：0.0  单位：vp  取值范围：[0, +∞) |
| marginTop | [Length](ts-types.md#length) | 否 | 是 | 下划线与文字的间距（不支持百分比设置）。  默认值：8.0  单位：vp  取值范围：[0, +∞) |

## DrawableDescriptor22+

PhonePC/2in1TabletTVWearable

type DrawableDescriptor = DrawableDescriptor

作为DrawableTabBarIndicator对象中drawable属性的入参对象。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor) | 返回一个DrawableDescriptor对象。 |

## SelectedMode10+枚举说明

PhonePC/2in1TabletTVWearable

选中子页签的显示模式枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INDICATOR | 0 | 使用下划线模式。 |
| BOARD | 1 | 使用背板模式。 |

## BoardStyle10+对象说明

PhonePC/2in1TabletTVWearable

背板风格对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| borderRadius | [Length](ts-types.md#length) | 否 | 是 | 背板的圆角半径（不支持百分比设置）。  默认值：8.0  单位：vp  取值范围：[0, +∞)。 |

## LabelStyle10+对象说明

PhonePC/2in1TabletTVWearable

label文本和字体的样式对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| overflow | [TextOverflow](ts-appendix-enums.md#textoverflow) | 否 | 是 | 设置Label文本超长时的显示方式。默认值是省略号截断。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| maxLines | number | 否 | 是 | 设置Label文本的最大行数。如果指定此参数，则文本最多不会超过指定的行。如果有多余的文本，可以通过textOverflow来指定截断方式。默认值是1。  取值范围：[1, +∞)。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| minFontSize | number | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置Label文本最小显示字号（不支持百分比设置）。需配合maxFontSize以及maxLines或布局大小限制使用。自适应文本大小生效后，font.size不生效。默认值是0.0fp，即默认自适应文本大小不生效。  取值范围：(0, +∞)。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| maxFontSize | number | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置Label文本最大显示字号（不支持百分比设置）。需配合minFontSize以及maxLines或布局大小限制使用。自适应文本大小生效后，font.size不生效。默认值是0.0fp，即默认自适应文本大小不生效。  取值范围：[minFontSize, +∞)。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| heightAdaptivePolicy | [TextHeightAdaptivePolicy](ts-appendix-enums.md#textheightadaptivepolicy10) | 否 | 是 | 设置Label文本自适应高度的方式。默认值是最大行数优先。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| font | [Font](ts-types.md#font) | 否 | 是 | 设置Label文本字体样式。  当页签为子页签时，默认值是字体大小16.0fp、字体类型'HarmonyOS Sans'，字体风格正常，选中时字重中等，未选中时字重正常。  当页签为底部页签时，默认值是字体大小10.0fp、字体类型'HarmonyOS Sans'，字体风格正常，字重中等。  从API version 12开始，底部页签内容左右排布时默认字体大小为12.0fp。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| unselectedColor12+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置Label文本字体未选中时的颜色。  默认值：#99182431  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedColor12+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置Label文本字体选中时的颜色。  默认值：#FF007DFF  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## BottomTabBarStyle9+

PhonePC/2in1TabletTVWearable

底部页签和侧边页签样式。

### constructor

PhonePC/2in1TabletTVWearable

constructor(icon: ResourceStr | TabBarSymbol, text: ResourceStr)

BottomTabBarStyle的构造函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| icon | [ResourceStr](ts-types.md#resourcestr) | [TabBarSymbol12+](ts-container-tabcontent.md#tabbarsymbol12对象说明) | 是 | 页签内的图片内容。 |
| text | [ResourceStr](ts-types.md#resourcestr) | 是 | 页签内的文字内容。 |

### of10+

PhonePC/2in1TabletTVWearable

static of(icon: ResourceStr | TabBarSymbol, text: ResourceStr): BottomTabBarStyle

BottomTabBarStyle的静态构造函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| icon | [ResourceStr](ts-types.md#resourcestr) | [TabBarSymbol12+](ts-container-tabcontent.md#tabbarsymbol12对象说明) | 是 | 页签内的图片内容。 |
| text | [ResourceStr](ts-types.md#resourcestr) | 是 | 页签内的文字内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BottomTabBarStyle](ts-container-tabcontent.md#bottomtabbarstyle9) | 返回创建的BottomTabBarStyle对象。 |

### padding10+

PhonePC/2in1TabletTVWearable

padding(value: Padding | Dimension | LocalizedPadding): BottomTabBarStyle

设置底部页签的内边距属性（不支持百分比设置）。使用Dimension时，四个方向内边距同时生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Padding](ts-types.md#padding) | [Dimension](ts-types.md#dimension10) | [LocalizedPadding12+](ts-types.md#localizedpadding12) | 是 | 底部页签的内边距。  取值范围：[0, +∞]  默认值：{left:4.0vp,right:4.0vp,top:0.0vp,bottom:0.0vp}  使用LocalizedPadding时，支持镜像能力。  默认值：{start:LengthMetrics.vp(4),end:LengthMetrics.vp(4),  top:LengthMetrics.vp(0),bottom:LengthMetrics.vp(0)} |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BottomTabBarStyle](ts-container-tabcontent.md#bottomtabbarstyle9) | 返回BottomTabBarStyle对象本身。 |

### verticalAlign10+

PhonePC/2in1TabletTVWearable

verticalAlign(value: VerticalAlign): BottomTabBarStyle

设置底部页签的图片、文字在垂直方向上的对齐格式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [VerticalAlign](ts-appendix-enums.md#verticalalign) | 是 | 底部页签的图片、文字在垂直方向上的对齐格式。  默认值：VerticalAlign.Center |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BottomTabBarStyle](ts-container-tabcontent.md#bottomtabbarstyle9) | 返回BottomTabBarStyle对象本身。 |

### layoutMode10+

PhonePC/2in1TabletTVWearable

layoutMode(value: LayoutMode): BottomTabBarStyle

设置底部页签的图片、文字排布的方式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LayoutMode](ts-container-tabcontent.md#layoutmode10枚举说明) | 是 | 底部页签的图片、文字排布的方式，具体参照LayoutMode枚举。  默认值：LayoutMode.VERTICAL |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BottomTabBarStyle](ts-container-tabcontent.md#bottomtabbarstyle9) | 返回BottomTabBarStyle对象本身。 |

### symmetricExtensible10+

PhonePC/2in1TabletTVWearable

symmetricExtensible(value: boolean): BottomTabBarStyle

设置底部页签的图片、文字是否可以对称借用左右底部页签的空余位置中的最小值，仅fixed水平模式下在底部页签之间有效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 底部页签的图片、文字是否可以对称借用左右底部页签的空余位置中的最小值。  默认值：false，底部页签的图片、文字不可以对称借用左右底部页签的空余位置中的最小值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BottomTabBarStyle](ts-container-tabcontent.md#bottomtabbarstyle9) | 返回BottomTabBarStyle对象本身。 |

### labelStyle10+

PhonePC/2in1TabletTVWearable

labelStyle(value: LabelStyle): BottomTabBarStyle

设置底部页签的label文本和字体的样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LabelStyle](ts-container-tabcontent.md#labelstyle10对象说明) | 是 | 底部页签的label文本和字体的样式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BottomTabBarStyle](ts-container-tabcontent.md#bottomtabbarstyle9) | 返回BottomTabBarStyle对象本身。 |

### id11+

PhonePC/2in1TabletTVWearable

id(value: string): BottomTabBarStyle

设置底部页签的id。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 设置底部页签的[id](ts-universal-attributes-component-id.md#id)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BottomTabBarStyle](ts-container-tabcontent.md#bottomtabbarstyle9) | 返回BottomTabBarStyle对象本身。 |

### iconStyle12+

PhonePC/2in1TabletTVWearable

iconStyle(style: TabBarIconStyle): BottomTabBarStyle

设置底部页签的label图标的样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [TabBarIconStyle](ts-container-tabcontent.md#tabbariconstyle12对象说明) | 是 | 底部页签的label图标的样式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BottomTabBarStyle](ts-container-tabcontent.md#bottomtabbarstyle9) | 返回BottomTabBarStyle对象本身。 |

## TabBarSymbol12+对象说明

PhonePC/2in1TabletTVWearable

页签内symbol图标样式对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| normal | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 否 | 页签内symbol图标普通态样式。  默认值：  fontColor：#66182431  renderingStrategy：SymbolRenderingStrategy.MULTIPLE\_OPACITY  fontSize：24vp |
| selected | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 是 | 页签内symbol图标选中态样式。  默认值：  fontColor：#ff007dff  renderingStrategy：SymbolRenderingStrategy.MULTIPLE\_OPACITY  fontSize：24vp |

## LayoutMode10+枚举说明

PhonePC/2in1TabletTVWearable

页签内容排布方式枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO | 0 | 若页签宽度大于104vp，页签内容为左右排布，否则页签内容为上下排布。仅TabBar为垂直模式或Fixed水平模式时有效。 |
| VERTICAL | 1 | 页签内容上下排布。 |
| HORIZONTAL | 2 | 页签内容左右排布。 |

## TabBarIconStyle12+对象说明

PhonePC/2in1TabletTVWearable

Label图标样式对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| unselectedColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置Label图标未选中时的颜色。  默认值：#33182431  **说明：**  仅对svg图源生效，设置后会替换svg图片的填充颜色。 |
| selectedColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置Label图标选中时的颜色。  默认值：#FF007DFF  **说明：**  仅对svg图源生效，设置后会替换svg图片的填充颜色。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onWillShow12+

PhonePC/2in1TabletTVWearable

onWillShow(event: VoidCallback)

逻辑回调，TabContent将要显示的时候触发该回调。场景包括TabContent首次显示，TabContent切换，页面切换，窗口前后台切换。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](ts-types.md#voidcallback12) | 是 | TabContent将要显示的回调函数。 |

### onWillHide12+

PhonePC/2in1TabletTVWearable

onWillHide(event: VoidCallback)

逻辑回调，TabContent将要隐藏的时候触发该回调。场景包括TabContent切换，页面切换，窗口前后台切换。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](ts-types.md#voidcallback12) | 是 | TabContent将要隐藏的回调函数。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（自定义页签切换联动）

本示例通过onAnimationStart、onChange实现切换时自定义tabBar和TabContent的联动。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabContentExample {
5. @State fontColor: string = '#182431';
6. @State selectedFontColor: string = '#007DFF';
7. @State currentIndex: number = 0;
8. @State selectedIndex: number = 0;
9. private controller: TabsController = new TabsController();

11. @Builder tabBuilder(index: number) {
12. Column() {
13. Image(this.selectedIndex === index ? '/common/public_icon_on.svg' : '/common/public_icon_off.svg')
14. .width(24)
15. .height(24)
16. .margin({ bottom: 4 })
17. .objectFit(ImageFit.Contain)
18. Text(`Tab${index + 1}`)
19. .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)
20. .fontSize(10)
21. .fontWeight(500)
22. .lineHeight(14)
23. }.width('100%')
24. }

26. build() {
27. Column() {
28. Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
29. TabContent() {
30. Column() {
31. Text('Tab1')
32. .fontSize(36)
33. .fontColor('#182431')
34. .fontWeight(500)
35. .opacity(0.4)
36. .margin({ top: 30, bottom: 56.5 })
37. Divider()
38. .strokeWidth(0.5)
39. .color('#182431')
40. .opacity(0.05)
41. }.width('100%')
42. }.tabBar(this.tabBuilder(0))

44. TabContent() {
45. Column() {
46. Text('Tab2')
47. .fontSize(36)
48. .fontColor('#182431')
49. .fontWeight(500)
50. .opacity(0.4)
51. .margin({ top: 30, bottom: 56.5 })
52. Divider()
53. .strokeWidth(0.5)
54. .color('#182431')
55. .opacity(0.05)
56. }.width('100%')
57. }.tabBar(this.tabBuilder(1))

59. TabContent() {
60. Column() {
61. Text('Tab3')
62. .fontSize(36)
63. .fontColor('#182431')
64. .fontWeight(500)
65. .opacity(0.4)
66. .margin({ top: 30, bottom: 56.5 })
67. Divider()
68. .strokeWidth(0.5)
69. .color('#182431')
70. .opacity(0.05)
71. }.width('100%')
72. }.tabBar(this.tabBuilder(2))

74. TabContent() {
75. Column() {
76. Text('Tab4')
77. .fontSize(36)
78. .fontColor('#182431')
79. .fontWeight(500)
80. .opacity(0.4)
81. .margin({ top: 30, bottom: 56.5 })
82. Divider()
83. .strokeWidth(0.5)
84. .color('#182431')
85. .opacity(0.05)
86. }.width('100%')
87. }.tabBar(this.tabBuilder(3))
88. }
89. .vertical(false)
90. .barHeight(56)
91. .onChange((index: number) => {
92. // currentIndex控制TabContent显示页签
93. this.currentIndex = index;
94. this.selectedIndex = index;
95. })
96. .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
97. if (index === targetIndex) {
98. return;
99. }
100. // selectedIndex控制自定义TabBar内Image和Text颜色切换
101. this.selectedIndex = targetIndex;
102. })
103. .width(360)
104. .height(190)
105. .backgroundColor('#F1F3F5')
106. .margin({ top: 38 })
107. }.width('100%')
108. }
109. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/PKii4FeaSJan7WO9npioeA/zh-cn_image_0000002552959686.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000137Z&HW-CC-Expire=86400&HW-CC-Sign=9CEC54D6D1BE7DDBA00E8B4255902931BD68411E3827D7F63E7E215042D15D06)

### 示例2（自定义侧边页签）

本示例通过vertical、barPosition实现侧边页签。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabContentExample {
5. @State fontColor: string = '#182431';
6. @State selectedFontColor: string = '#007DFF';
7. @State currentIndex: number = 0;
8. @State selectedIndex: number = 0;
9. private controller: TabsController = new TabsController();

11. @Builder tabBuilder(index: number) {
12. Column() {
13. Image(this.selectedIndex === index ? '/common/public_icon_on.svg' : '/common/public_icon_off.svg')
14. .width(24)
15. .height(24)
16. .margin({ bottom: 4 })
17. .objectFit(ImageFit.Contain)
18. Text('Tab')
19. .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)
20. .fontSize(10)
21. .fontWeight(500)
22. .lineHeight(14)
23. }.width('100%').height('100%').justifyContent(FlexAlign.Center)
24. }

26. build() {
27. Column() {
28. Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {
29. TabContent()
30. .tabBar(this.tabBuilder(0))
31. TabContent()
32. .tabBar(this.tabBuilder(1))
33. TabContent()
34. .tabBar(this.tabBuilder(2))
35. TabContent()
36. .tabBar(this.tabBuilder(3))
37. }
38. .vertical(true)
39. .barWidth(96)
40. .barHeight(414)
41. .onChange((index: number) => {
42. // currentIndex控制TabContent显示页签
43. this.currentIndex = index;
44. this.selectedIndex = index;
45. })
46. .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
47. if (index === targetIndex) {
48. return;
49. }
50. // selectedIndex控制自定义TabBar内Image和Text颜色切换
51. this.selectedIndex = targetIndex;
52. })
53. .width(96)
54. .height(414)
55. .backgroundColor('#F1F3F5')
56. .margin({ top: 52 })
57. }.width('100%')
58. }
59. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/lciqWLJYQu6EtIIDIFwLfQ/zh-cn_image_0000002583479687.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000137Z&HW-CC-Expire=86400&HW-CC-Sign=BBABB05413F1511A0AD74A3FD2070CF59B5C9C80A5A6853968473027488C0F65)

### 示例3（子页签/底部页签/侧边页签样式对比）

本示例使用了SubTabBarStyle、BottomTabBarStyle实现了子页签、底部页签和侧边页签。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabBarStyleExample {
5. build() {
6. Column({ space: 5 }) {
7. Text('子页签样式')
8. Column() {
9. Tabs({ barPosition: BarPosition.Start }) {
10. TabContent() {
11. Column().width('100%').height('100%').backgroundColor(Color.Pink)
12. }.tabBar(new SubTabBarStyle('Pink'))
13. .onWillShow(() => {
14. console.info('Pink will show');
15. })
16. .onWillHide(() => {
17. console.info('Pink will hide');
18. })

20. TabContent() {
21. Column().width('100%').height('100%').backgroundColor(Color.Yellow)
22. }.tabBar(new SubTabBarStyle('Yellow'))
23. .onWillShow(() => {
24. console.info('Yellow will show');
25. })
26. .onWillHide(() => {
27. console.info('Yellow will hide');
28. })

30. TabContent() {
31. Column().width('100%').height('100%').backgroundColor(Color.Blue)
32. }.tabBar(new SubTabBarStyle('Blue'))
33. .onWillShow(() => {
34. console.info('Blue will show');
35. })
36. .onWillHide(() => {
37. console.info('Blue will hide');
38. })

40. TabContent() {
41. Column().width('100%').height('100%').backgroundColor(Color.Green)
42. }.tabBar(new SubTabBarStyle('Green'))
43. .onWillShow(() => {
44. console.info('Green will show');
45. })
46. .onWillHide(() => {
47. console.info('Green will hide');
48. })
49. }
50. .vertical(false)
51. .scrollable(true)
52. .barMode(BarMode.Fixed)
53. .onChange((index: number) => {
54. console.info(index.toString());
55. })
56. .width('100%')
57. .backgroundColor(0xF1F3F5)
58. }.width('100%').height(200)
59. Text('底部页签样式')
60. Column() {
61. Tabs({ barPosition: BarPosition.End }) {
62. TabContent() {
63. Column().width('100%').height('100%').backgroundColor(Color.Pink)
64. }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Pink'))
65. .onWillShow(() => {
66. console.info('Pink will show');
67. })
68. .onWillHide(() => {
69. console.info('Pink will hide');
70. })

72. TabContent() {
73. Column().width('100%').height('100%').backgroundColor(Color.Yellow)
74. }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Yellow'))
75. .onWillShow(() => {
76. console.info('Yellow will show');
77. })
78. .onWillHide(() => {
79. console.info('Yellow will hide');
80. })

82. TabContent() {
83. Column().width('100%').height('100%').backgroundColor(Color.Blue)
84. }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Blue'))
85. .onWillShow(() => {
86. console.info('Blue will show');
87. })
88. .onWillHide(() => {
89. console.info('Blue will hide');
90. })

92. TabContent() {
93. Column().width('100%').height('100%').backgroundColor(Color.Green)
94. }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Green'))
95. .onWillShow(() => {
96. console.info('Green will show');
97. })
98. .onWillHide(() => {
99. console.info('Green will hide');
100. })
101. }
102. .vertical(false)
103. .scrollable(true)
104. .barMode(BarMode.Fixed)
105. .onChange((index: number) => {
106. console.info(index.toString());
107. })
108. .width('100%')
109. .backgroundColor(0xF1F3F5)
110. }.width('100%').height(200)
111. Text('侧边页签样式')
112. Column() {
113. Tabs({ barPosition: BarPosition.Start }) {
114. TabContent() {
115. Column().width('100%').height('100%').backgroundColor(Color.Pink)
116. }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Pink'))
117. .onWillShow(() => {
118. console.info('Pink will show');
119. })
120. .onWillHide(() => {
121. console.info('Pink will hide');
122. })

124. TabContent() {
125. Column().width('100%').height('100%').backgroundColor(Color.Yellow)
126. }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Yellow'))
127. .onWillShow(() => {
128. console.info('Yellow will show');
129. })
130. .onWillHide(() => {
131. console.info('Yellow will hide');
132. })

134. TabContent() {
135. Column().width('100%').height('100%').backgroundColor(Color.Blue)
136. }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Blue'))
137. .onWillShow(() => {
138. console.info('Blue will show');
139. })
140. .onWillHide(() => {
141. console.info('Blue will hide');
142. })

144. TabContent() {
145. Column().width('100%').height('100%').backgroundColor(Color.Green)
146. }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Green'))
147. .onWillShow(() => {
148. console.info('Green will show');
149. })
150. .onWillHide(() => {
151. console.info('Green will hide');
152. })
153. }
154. .vertical(true).scrollable(true).barMode(BarMode.Fixed)
155. .onChange((index: number) => {
156. console.info(index.toString());
157. })
158. .width('100%')
159. .backgroundColor(0xF1F3F5)
160. }.width('100%').height(400)
161. }
162. }
163. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/cqwqzSwkQDqQdsHyRM3IrQ/zh-cn_image_0000002552800038.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000137Z&HW-CC-Expire=86400&HW-CC-Sign=727BDE516FA94A5C855F303A0CB9EF9E71A2BC7A13A213A98105A51FFAD739D5)

### 示例4（设置子页签下划线基本属性）

本示例通过SubTabBarStyle中的indicator属性，实现了子页签下划线基本属性的展示。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabsAttr {
5. private controller: TabsController = new TabsController();
6. @State indicatorColor: Color = Color.Blue;
7. @State indicatorWidth: number = 40;
8. @State indicatorHeight: number = 10;
9. @State indicatorBorderRadius: number = 5;
10. @State indicatorSpace: number = 10;
11. @State subTabBorderRadius: number = 20;
12. @State selectedMode: SelectedMode = SelectedMode.INDICATOR;
13. private colorFlag: boolean = true;
14. private widthFlag: boolean = true;
15. private heightFlag: boolean = true;
16. private borderFlag: boolean = true;
17. private spaceFlag: boolean = true;

19. build() {
20. Column() {
21. Button('下划线颜色变化').width('100%').margin({ bottom: '12vp' })
22. .onClick((event?: ClickEvent) => {
23. // 对Button组件的宽高属性进行动画配置
24. if (this.colorFlag) {
25. this.getUIContext()?.animateTo({
26. duration: 1000, // 动画时长
27. curve: Curve.Linear, // 动画曲线
28. delay: 200, // 动画延迟
29. iterations: 1, // 播放次数
30. playMode: PlayMode.Normal, // 动画模式
31. onFinish: () => {
32. console.info('play end');
33. }
34. }, () => {
35. this.indicatorColor = Color.Red;
36. });
37. } else {
38. this.getUIContext()?.animateTo({
39. duration: 1000, // 动画时长
40. curve: Curve.Linear, // 动画曲线
41. delay: 200, // 动画延迟
42. iterations: 1, // 播放次数
43. playMode: PlayMode.Normal, // 动画模式
44. onFinish: () => {
45. console.info('play end');
46. }
47. }, () => {
48. this.indicatorColor = Color.Yellow;
49. });
50. }
51. this.colorFlag = !this.colorFlag;
52. })
53. Button('下划线高度变化').width('100%').margin({ bottom: '12vp' })
54. .onClick((event?: ClickEvent) => {
55. // 对Button组件的宽高属性进行动画配置
56. if (this.heightFlag) {
57. this.getUIContext()?.animateTo({
58. duration: 1000, // 动画时长
59. curve: Curve.Linear, // 动画曲线
60. delay: 200, // 动画延迟
61. iterations: 1, // 播放次数
62. playMode: PlayMode.Normal, // 动画模式
63. onFinish: () => {
64. console.info('play end');
65. }
66. }, () => {
67. this.indicatorHeight = 20;
68. });
69. } else {
70. this.getUIContext()?.animateTo({
71. duration: 1000, // 动画时长
72. curve: Curve.Linear, // 动画曲线
73. delay: 200, // 动画延迟
74. iterations: 1, // 播放次数
75. playMode: PlayMode.Normal, // 动画模式
76. onFinish: () => {
77. console.info('play end');
78. }
79. }, () => {
80. this.indicatorHeight = 10;
81. });
82. }
83. this.heightFlag = !this.heightFlag;
84. })
85. Button('下划线宽度变化').width('100%').margin({ bottom: '12vp' })
86. .onClick((event?: ClickEvent) => {
87. // 对Button组件的宽高属性进行动画配置
88. if (this.widthFlag) {
89. this.getUIContext()?.animateTo({
90. duration: 1000, // 动画时长
91. curve: Curve.Linear, // 动画曲线
92. delay: 200, // 动画延迟
93. iterations: 1, // 播放次数
94. playMode: PlayMode.Normal, // 动画模式
95. onFinish: () => {
96. console.info('play end');
97. }
98. }, () => {
99. this.indicatorWidth = 30;
100. });
101. } else {
102. this.getUIContext()?.animateTo({
103. duration: 1000, // 动画时长
104. curve: Curve.Linear, // 动画曲线
105. delay: 200, // 动画延迟
106. iterations: 1, // 播放次数
107. playMode: PlayMode.Normal, // 动画模式
108. onFinish: () => {
109. console.info('play end');
110. }
111. }, () => {
112. this.indicatorWidth = 50;
113. });
114. }
115. this.widthFlag = !this.widthFlag;
116. })
117. Button('下划线圆角半径变化').width('100%').margin({ bottom: '12vp' })
118. .onClick((event?: ClickEvent) => {
119. // 对Button组件的宽高属性进行动画配置
120. if (this.borderFlag) {
121. this.getUIContext()?.animateTo({
122. duration: 1000, // 动画时长
123. curve: Curve.Linear, // 动画曲线
124. delay: 200, // 动画延迟
125. iterations: 1, // 播放次数
126. playMode: PlayMode.Normal, // 动画模式
127. onFinish: () => {
128. console.info('play end');
129. }
130. }, () => {
131. this.indicatorBorderRadius = 0;
132. });
133. } else {
134. this.getUIContext()?.animateTo({
135. duration: 1000, // 动画时长
136. curve: Curve.Linear, // 动画曲线
137. delay: 200, // 动画延迟
138. iterations: 1, // 播放次数
139. playMode: PlayMode.Normal, // 动画模式
140. onFinish: () => {
141. console.info('play end');
142. }
143. }, () => {
144. this.indicatorBorderRadius = 5;
145. });
146. }
147. this.borderFlag = !this.borderFlag;
148. })
149. Button('下划线间距变化').width('100%').margin({ bottom: '12vp' })
150. .onClick((event?: ClickEvent) => {
151. // 对Button组件的宽高属性进行动画配置
152. if (this.spaceFlag) {
153. this.getUIContext()?.animateTo({
154. duration: 1000, // 动画时长
155. curve: Curve.Linear, // 动画曲线
156. delay: 200, // 动画延迟
157. iterations: 1, // 播放次数
158. playMode: PlayMode.Normal, // 动画模式
159. onFinish: () => {
160. console.info('play end');
161. }
162. }, () => {
163. this.indicatorSpace = 20;
164. });
165. } else {
166. this.getUIContext()?.animateTo({
167. duration: 1000, // 动画时长
168. curve: Curve.Linear, // 动画曲线
169. delay: 200, // 动画延迟
170. iterations: 1, // 播放次数
171. playMode: PlayMode.Normal, // 动画模式
172. onFinish: () => {
173. console.info('play end');
174. }
175. }, () => {
176. this.indicatorSpace = 10;
177. });
178. }
179. this.spaceFlag = !this.spaceFlag;
180. })
181. Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
182. TabContent() {
183. Column().width('100%').height('100%').backgroundColor(Color.Pink).borderRadius('12vp')
184. }.tabBar(SubTabBarStyle.of('pink')
185. .indicator({
186. color: this.indicatorColor, // 下划线颜色
187. height: this.indicatorHeight, // 下划线高度
188. width: this.indicatorWidth, // 下划线宽度
189. borderRadius: this.indicatorBorderRadius, // 下划线圆角半径
190. marginTop: this.indicatorSpace // 下划线与文字间距
191. })
192. .selectedMode(this.selectedMode)
193. .board({ borderRadius: this.subTabBorderRadius })
194. .labelStyle({})
195. )

197. TabContent() {
198. Column().width('100%').height('100%').backgroundColor(Color.Yellow).borderRadius('12vp')
199. }.tabBar('yellow')

201. TabContent() {
202. Column().width('100%').height('100%').backgroundColor(Color.Blue).borderRadius('12vp')
203. }.tabBar('blue')

205. TabContent() {
206. Column().width('100%').height('100%').backgroundColor(Color.Green).borderRadius('12vp')
207. }.tabBar('green')

209. TabContent() {
210. Column().width('100%').height('100%').backgroundColor(Color.Gray).borderRadius('12vp')
211. }.tabBar('gray')

213. TabContent() {
214. Column().width('100%').height('100%').backgroundColor(Color.Orange).borderRadius('12vp')
215. }.tabBar('orange')
216. }
217. .vertical(false)
218. .scrollable(true)
219. .barMode(BarMode.Scrollable)
220. .barHeight(140)
221. .animationDuration(400)
222. .onChange((index: number) => {
223. console.info(index.toString());
224. })
225. .backgroundColor(0xF5F5F5)
226. .height(320)
227. }.width('100%').height(250).padding({ top: '24vp', left: '24vp', right: '24vp' })
228. }
229. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/QDWjj88ESRqVnJJ1ZvMMaQ/zh-cn_image_0000002583439733.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000137Z&HW-CC-Expire=86400&HW-CC-Sign=83684EB7184E75E4C7BE95D734AF2D3D31A9AEB0AC32E7321ADC64970243CE7E)

### 示例5（设置子页签文本自适应高度属性）

本示例通过heightAdaptivePolicy实现了子页签文本高度自适应。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabsTextOverflow {
5. @State message: string = 'Hello World';
6. private controller: TabsController = new TabsController();
7. @State subTabOverflowOpaque: boolean = true;

9. build() {
10. Column() {
11. Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {
12. TabContent() {
13. Column() {
14. Text('单行省略号截断').fontSize(30).fontColor(0xFF000000)
15. }.width('100%').height('100%').backgroundColor(Color.Pink)
16. }
17. .tabBar(SubTabBarStyle.of('开始【单行省略号截断单行省略号截断单行省略号截断单行省略号截断单行省略号截断单行省略号截断单行省略号截断单行省略号截断单行省略号截断单行省略号截断】结束')
18. .labelStyle({
19. overflow: TextOverflow.Ellipsis,
20. maxLines: 1,
21. minFontSize: 10,
22. heightAdaptivePolicy: TextHeightAdaptivePolicy.MAX_LINES_FIRST,
23. font: { size: 20 }
24. }))

26. TabContent() {
27. Column() {
28. Text('先缩小再截断').fontSize(30).fontColor(0xFF000000)
29. }.width('100%').height('100%').backgroundColor(Color.Pink)
30. }
31. .tabBar(SubTabBarStyle.of('开始【先缩小再截断先缩小再截断先缩小再截断先缩小再截断先缩小再截断先缩小再截断先缩小再截断先缩小再截断先缩小再截断先缩小再截断先缩小再截断先缩小再截断先缩小再截断先缩小再截断】结束')
32. .labelStyle({
33. overflow: TextOverflow.Clip,
34. maxLines: 1,
35. minFontSize: 15,
36. maxFontSize: 15,
37. heightAdaptivePolicy: TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST,
38. font: { size: 20 }
39. }))

41. TabContent() {
42. Column() {
43. Text('先缩小再换行再截断').fontSize(30).fontColor(0xFF000000)
44. }.width('100%').height('100%').backgroundColor(Color.Pink)
45. }
46. .tabBar(SubTabBarStyle.of('开始【先缩小再换行再截断先缩小再换行再截断先缩小再换行再截断先缩小再换行再截断先缩小再换行再截断先缩小再换行再截断先缩小再换行再截断先缩小再换行再截断】结束')
47. .labelStyle({
48. overflow: TextOverflow.Clip,
49. maxLines: 2,
50. minFontSize: 15,
51. maxFontSize: 15,
52. heightAdaptivePolicy: TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST,
53. font: { size: 20 }
54. }))

56. TabContent() {
57. Column() {
58. Text('换行').fontSize(30).fontColor(0xFF000000)
59. }
60. .width('100%').height('100%').backgroundColor(Color.Pink)
61. }.tabBar(SubTabBarStyle.of('开始【换行换行换行换行换行换行换行换行换行换行换行换行换行换行换行】结束')
62. .labelStyle({
63. overflow: TextOverflow.Clip,
64. maxLines: 10,
65. minFontSize: 10,
66. heightAdaptivePolicy: TextHeightAdaptivePolicy.MAX_LINES_FIRST,
67. font: { size: 20 }
68. }))
69. }
70. .vertical(true).scrollable(true)
71. .barMode(BarMode.Fixed)
72. .barHeight(720)
73. .barWidth(200).animationDuration(400)
74. .onChange((index: number) => {
75. console.info(index.toString());
76. })
77. .height('100%').width('100%')
78. }
79. .height('100%')
80. }
81. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/y_YWfJm8R1C1DlFFzjeD_Q/zh-cn_image_0000002552959688.png?HW-CC-KV=V1&HW-CC-Date=20260428T000137Z&HW-CC-Expire=86400&HW-CC-Sign=529169F8FAFC55AA78E66B249E9226B7EA2454B3A835B9B65F645C65BCDFD220)

### 示例6（设置底部页签基本属性）

本示例通过padding、verticalAlign、layoutMode、symmetricExtensible实现了底部页签基本属性的展示。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabContentExample6 {
5. private controller: TabsController = new TabsController();
6. @State text: string = '2';
7. @State tabPadding: number = 0;
8. @State symmetricExtensible: boolean = false;
9. @State layoutMode: LayoutMode = LayoutMode.VERTICAL;
10. @State verticalAlign: VerticalAlign = VerticalAlign.Center;

12. build() {
13. Column() {
14. Row() {
15. Button('padding+10 ' + this.tabPadding)
16. .width('47%')
17. .height(50)
18. .margin({ top: 5 })
19. .onClick((event?: ClickEvent) => {
20. this.tabPadding += 10;
21. })
22. .margin({ right: '6%', bottom: '12vp' })
23. Button('padding-10 ' + this.tabPadding)
24. .width('47%')
25. .height(50)
26. .margin({ top: 5 })
27. .onClick((event?: ClickEvent) => {
28. this.tabPadding -= 10;
29. })
30. .margin({ bottom: '12vp' })
31. }

33. Row() {
34. Button('文本增加 ')
35. .width('47%')
36. .height(50)
37. .margin({ top: 5 })
38. .onClick((event?: ClickEvent) => {
39. this.text += '文本增加';
40. })
41. .margin({ right: '6%', bottom: '12vp' })
42. Button('文本重置')
43. .width('47%')
44. .height(50)
45. .margin({ top: 5 })
46. .onClick((event?: ClickEvent) => {
47. this.text = '2';
48. })
49. .margin({ bottom: '12vp' })
50. }

52. Row() {
53. Button('symmetricExtensible改变 ' + this.symmetricExtensible)
54. .width('100%')
55. .height(50)
56. .margin({ top: 5 })
57. .onClick((event?: ClickEvent) => {
58. this.symmetricExtensible = !this.symmetricExtensible;
59. })
60. .margin({ bottom: '12vp' })
61. }

63. Row() {
64. Button('layoutMode垂直 ')
65. .width('47%')
66. .height(50)
67. .margin({ top: 5 })
68. .onClick((event?: ClickEvent) => {
69. this.layoutMode = LayoutMode.VERTICAL;
70. })
71. .margin({ right: '6%', bottom: '12vp' })
72. Button('layoutMode水平 ')
73. .width('47%')
74. .height(50)
75. .margin({ top: 5 })
76. .onClick((event?: ClickEvent) => {
77. this.layoutMode = LayoutMode.HORIZONTAL;
78. })
79. .margin({ bottom: '12vp' })
80. }

82. Row() {
83. Button('verticalAlign朝上')
84. .width('100%')
85. .height(50)
86. .margin({ top: 5 })
87. .onClick((event?: ClickEvent) => {
88. this.verticalAlign = VerticalAlign.Top;
89. })
90. .margin({ bottom: '12vp' })
91. }

93. Row() {
94. Button('verticalAlign居中')
95. .width('100%')
96. .height(50)
97. .margin({ top: 5 })
98. .onClick((event?: ClickEvent) => {
99. this.verticalAlign = VerticalAlign.Center;
100. })
101. .margin({ bottom: '12vp' })
102. }

104. Row() {
105. Button('verticalAlign朝下')
106. .width('100%')
107. .height(50)
108. .margin({ top: 5 })
109. .onClick((event?: ClickEvent) => {
110. this.verticalAlign = VerticalAlign.Bottom;
111. })
112. .margin({ bottom: '12vp' })
113. }

116. Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
117. TabContent() {
118. Column().width('100%').height('100%').backgroundColor(Color.Pink)
119. }.tabBar(BottomTabBarStyle.of($r('sys.media.ohos_app_icon'), '1'))

121. TabContent() {
122. Column().width('100%').height('100%').backgroundColor(Color.Green)
123. }.tabBar(BottomTabBarStyle.of($r('sys.media.ohos_app_icon'), this.text)
124. .padding(this.tabPadding)
125. .verticalAlign(this.verticalAlign)
126. .layoutMode(this.layoutMode)
127. .symmetricExtensible(this.symmetricExtensible))

129. TabContent() {
130. Column().width('100%').height('100%').backgroundColor(Color.Blue)
131. }.tabBar(BottomTabBarStyle.of($r('sys.media.ohos_app_icon'), '3'))
132. }
133. .animationDuration(300)
134. .height('60%')
135. .backgroundColor(0xf1f3f5)
136. .barMode(BarMode.Fixed)
137. }
138. .width('100%')
139. .height(500)
140. .margin({ top: 5 })
141. .padding('24vp')
142. }
143. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/FEbI6DcZROWHZEDLiDzX9Q/zh-cn_image_0000002583479689.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000137Z&HW-CC-Expire=86400&HW-CC-Sign=A60F94EBB7880F26E0509D29D70A98F62A4CE8D562E2696D9DC4A94FF6D53CE9)

### 示例7（设置子页签/底部页签文本颜色）

本示例通过labelStyle中的unselectedColor和selectedColor改变底部页签以及子页签的文本颜色。

通过iconStyle中的unselectedColor和selectedColor改变底部页签的图标颜色。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabBarStyleExample {
5. build() {
6. Column({ space: 5 }) {
7. Text('子页签样式')
8. Column() {
9. Tabs({ barPosition: BarPosition.Start }) {
10. TabContent() {
11. Column().width('100%').height('100%').backgroundColor(Color.Pink)
12. }.tabBar(new SubTabBarStyle('Pink')
13. .labelStyle({ unselectedColor: Color.Red, selectedColor: Color.Green }))

15. TabContent() {
16. Column().width('100%').height('100%').backgroundColor(Color.Yellow)
17. }.tabBar(new SubTabBarStyle('Yellow')
18. .labelStyle({ unselectedColor: Color.Red, selectedColor: Color.Green }))

20. TabContent() {
21. Column().width('100%').height('100%').backgroundColor(Color.Blue)
22. }.tabBar(new SubTabBarStyle('Blue')
23. .labelStyle({ unselectedColor: Color.Red, selectedColor: Color.Green }))

25. TabContent() {
26. Column().width('100%').height('100%').backgroundColor(Color.Green)
27. }.tabBar(new SubTabBarStyle('Green')
28. .labelStyle({ unselectedColor: Color.Red, selectedColor: Color.Green })
29. )
30. }
31. .vertical(false)
32. .scrollable(true)
33. .barMode(BarMode.Fixed)
34. .onChange((index: number) => {
35. console.info(index.toString());
36. })
37. .width('100%')
38. .backgroundColor(0xF1F3F5)
39. }.width('100%').height(200)

41. Text('底部页签样式')
42. Column() {
43. Tabs({ barPosition: BarPosition.End }) {
44. TabContent() {
45. Column().width('100%').height('100%').backgroundColor(Color.Pink)
46. }
47. .tabBar(new BottomTabBarStyle('/common/public_icon_off.svg', 'pink')
48. .labelStyle({ unselectedColor: Color.Red, selectedColor: Color.Green })
49. .iconStyle({ unselectedColor: Color.Red, selectedColor: Color.Green })
50. )

52. TabContent() {
53. Column().width('100%').height('100%').backgroundColor(Color.Yellow)
54. }.tabBar(new BottomTabBarStyle('/common/public_icon_off.svg', 'Yellow')
55. .labelStyle({ unselectedColor: Color.Red, selectedColor: Color.Green })
56. .iconStyle({ unselectedColor: Color.Red, selectedColor: Color.Green })
57. )

59. TabContent() {
60. Column().width('100%').height('100%').backgroundColor(Color.Blue)
61. }.tabBar(new BottomTabBarStyle('/common/public_icon_off.svg', 'Blue')
62. .labelStyle({ unselectedColor: Color.Red, selectedColor: Color.Green })
63. .iconStyle({ unselectedColor: Color.Red, selectedColor: Color.Green })
64. )

66. TabContent() {
67. Column().width('100%').height('100%').backgroundColor(Color.Green)
68. }.tabBar(new BottomTabBarStyle('/common/public_icon_off.svg', 'Green')
69. .labelStyle({ unselectedColor: Color.Red, selectedColor: Color.Green })
70. .iconStyle({ unselectedColor: Color.Red, selectedColor: Color.Green })
71. )
72. }
73. .vertical(false)
74. .scrollable(true)
75. .barMode(BarMode.Fixed)
76. .onChange((index: number) => {
77. console.info(index.toString());
78. })
79. .width('100%')
80. .backgroundColor(0xF1F3F5)
81. }.width('100%').height(200)
82. }
83. }
84. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/n2dlaYSZQHekP13RqXT5Qw/zh-cn_image_0000002552800040.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000137Z&HW-CC-Expire=86400&HW-CC-Sign=F3EB512452E76469B4ED8136DF97D6566BC025A1FA3759104EAC8A1AB059F1C7)

### 示例8（设置自定义子页签）

该示例实现了通过ComponentContent设置SubTabBarStyle。

```
1. // xxx.ets
2. import { ComponentContent, UIContext } from '@kit.ArkUI';

4. class Params {
5. text: string = '';

7. constructor(text: string) {
8. this.text = text;
9. }
10. }

12. @Builder
13. function buildText(params: Params) {
14. Column() {
15. Text(params.text)
16. .fontSize(20)
17. .fontWeight(FontWeight.Bold)
18. .margin(20)
19. }
20. }

22. @Entry
23. @Component
24. struct Index {
25. @State message1: string = 'tabBar1';
26. @State message2: string = 'tabBar2';
27. context: UIContext = this.getUIContext();
28. private count1 = 0;
29. private count2 = 0;
30. private controller: TabsController = new TabsController();
31. tabBar1: ComponentContent<Params> = new ComponentContent<Params>(this.context, wrapBuilder<[Params]>(buildText), new Params(this.message1));
32. tabBar2: ComponentContent<Params> = new ComponentContent<Params>(this.context, wrapBuilder<[Params]>(buildText), new Params(this.message2));

34. build() {
35. Row() {
36. Column() {
37. Button('更新tabBar1').width('90%').margin(20)
38. .onClick((event?: ClickEvent) => {
39. this.count1 += 1;
40. const message1 = 'Update 1_' + this.count1.toString();
41. this.tabBar1.update(new Params(message1));
42. })
43. Button('更新tabBar2').width('90%').margin(20)
44. .onClick((event?: ClickEvent) => {
45. this.count2 += 1;
46. const message2 = 'Update 2_' + this.count2.toString();
47. this.tabBar2.update(new Params(message2));
48. })
49. Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {
50. TabContent() {
51. Column().width('100%').height('100%').backgroundColor(Color.Pink).borderRadius('12vp')
52. }.tabBar(new SubTabBarStyle(this.tabBar1))
53. TabContent() {
54. Column().width('100%').height('100%').backgroundColor(Color.Blue).borderRadius('12vp')
55. }.tabBar(SubTabBarStyle.of(this.tabBar2))
56. }
57. .vertical(false)
58. .barWidth(414)
59. .barHeight(96)
60. .width(414)
61. .height(414)
62. .backgroundColor('#F1F3F5')
63. .margin({ top: 20 })
64. }
65. .width('100%')
66. .height('100%')
67. }
68. .height('100%')
69. }
70. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/--Wd49ELSZqBlEl1GbgVnw/zh-cn_image_0000002583439735.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000137Z&HW-CC-Expire=86400&HW-CC-Sign=EA8BABE9512C403CF3314D557094791CB0A011F3456917482B251CC607231FA9)

### 示例9（设置底部页签使用symbol图标）

该示例实现了BottomTabBarStyle图片传入Symbol。

```
1. // xxx.ets
2. import { SymbolGlyphModifier } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Index {
7. @State symbolModifier1: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_wifi'));
8. @State symbolModifier2: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ellipsis_bubble'));
9. @State symbolModifier3: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.dot_video'));
10. @State symbolModifier4: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.exposure'));
11. build() {
12. Column({space: 5}) {
13. Text('底部页签样式')
14. Column(){
15. Tabs({barPosition: BarPosition.End}) {
16. TabContent() {
17. Column().width('100%').height('100%').backgroundColor(Color.Pink)
18. }.tabBar(new BottomTabBarStyle({
19. normal: this.symbolModifier1,
20. }, 'Pink'))
21. .onWillShow(() => {
22. console.info('Pink will show');
23. })
24. .onWillHide(() => {
25. console.info('Pink will hide');
26. })

28. TabContent() {
29. Column().width('100%').height('100%').backgroundColor(Color.Orange)
30. }.tabBar(new BottomTabBarStyle({
31. normal: this.symbolModifier2,
32. }, 'Orange'))
33. .onWillShow(() => {
34. console.info('Orange will show');
35. })
36. .onWillHide(() => {
37. console.info('Orange will hide');
38. })

40. TabContent() {
41. Column().width('100%').height('100%').backgroundColor(Color.Blue)
42. }.tabBar(new BottomTabBarStyle({
43. normal: this.symbolModifier3,
44. }, 'Blue'))
45. .onWillShow(() => {
46. console.info('Blue will show');
47. })
48. .onWillHide(() => {
49. console.info('Blue will hide');
50. })

52. TabContent() {
53. Column().width('100%').height('100%').backgroundColor(Color.Green)
54. }.tabBar(new BottomTabBarStyle({
55. normal: this.symbolModifier4,
56. }, 'Green'))
57. .onWillShow(() => {
58. console.info('Green will show');
59. })
60. .onWillHide(() => {
61. console.info('Green will hide');
62. })
63. }
64. .vertical(false)
65. .scrollable(true)
66. .barMode(BarMode.Fixed)
67. .onChange((index:number)=>{
68. console.info(index.toString());
69. })
70. .width('100%')
71. .backgroundColor(0xF1F3F5)
72. }.width('100%').height(200)
73. }
74. }
75. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/nm6EvHz6QBCf09nnuvSiWg/zh-cn_image_0000002552959690.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000137Z&HW-CC-Expire=86400&HW-CC-Sign=885C53AFED371606FCADEC1AC7FDA846DF7E3D006933CF5A3BAED263886ED30D)

### 示例10（通过ComponentContent设置TabBar）

该示例实现了通过ComponentContent封装组件内容，设置TabBar。通过ComponentContent的update函数更新TabBar。

```
1. // xxx.ets
2. import { ComponentContent, UIContext } from '@kit.ArkUI';

4. class Params {
5. text: string = '';
6. fontColor: string = '';

8. constructor(text: string, fontColor: string) {
9. this.text = text;
10. this.fontColor = fontColor;
11. }
12. }

14. @Builder
15. function buildText(params: Params) {
16. Column() {
17. Text(params.text)
18. .fontColor(params.fontColor)
19. .fontSize(20)
20. .fontWeight(FontWeight.Bold)
21. .margin(20)
22. }
23. }

25. @Entry
26. @Component
27. struct Index {
28. @State currentIndex: number = 0;
29. @State message1: string = 'tabBar1';
30. @State message2: string = 'tabBar2';
31. unselectedFontColor: string = '#182431';
32. selectedFontColor: string = '#007DFF';
33. context: UIContext = this.getUIContext();
34. private count1 = 0;
35. private count2 = 0;
36. private controller: TabsController = new TabsController();

38. getTabBar1() {
39. this.tabBar1.update(new Params(this.message1,
40. this.currentIndex === 0 ? this.selectedFontColor : this.unselectedFontColor));
41. return this.tabBar1;
42. }

44. getTabBar2() {
45. this.tabBar2.update(new Params(this.message2,
46. this.currentIndex === 1 ? this.selectedFontColor : this.unselectedFontColor));
47. return this.tabBar2;
48. }

50. tabBar1: ComponentContent<Params> =
51. new ComponentContent<Params>(this.context, wrapBuilder<[Params]>(buildText),
52. new Params(this.message1, this.selectedFontColor));
53. tabBar2: ComponentContent<Params> =
54. new ComponentContent<Params>(this.context, wrapBuilder<[Params]>(buildText),
55. new Params(this.message2, this.unselectedFontColor));

57. build() {
58. Row() {
59. Column() {
60. Button('更新tabBar1').width('90%').margin(20)
61. .onClick((event?: ClickEvent) => {
62. this.count1 += 1;
63. this.message1 = 'Update 1_' + this.count1.toString();
64. this.tabBar1.update(new Params(this.message1, this.unselectedFontColor));
65. })
66. Button('更新tabBar2').width('90%').margin(20)
67. .onClick((event?: ClickEvent) => {
68. this.count2 += 1;
69. this.message2 = 'Update 2_' + this.count2.toString();
70. this.tabBar2.update(new Params(this.message2, this.unselectedFontColor));
71. })
72. Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {
73. TabContent() {
74. Column().width('100%').height('100%').backgroundColor(Color.Pink).borderRadius('12vp')
75. }.tabBar(this.getTabBar1())

77. TabContent() {
78. Column().width('100%').height('100%').backgroundColor(Color.Blue).borderRadius('12vp')
79. }.tabBar(this.getTabBar2())
80. }
81. .vertical(false)
82. .barWidth(414)
83. .barHeight(96)
84. .width(414)
85. .height(414)
86. .backgroundColor('#F1F3F5')
87. .margin({ top: 20 })
88. .onChange((index: number) => {
89. this.currentIndex = index;
90. })
91. }
92. .width('100%')
93. .height('100%')
94. }
95. .height('100%')
96. }
97. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/V7Lj9Wv_QrGoVEZ6ch11Iw/zh-cn_image_0000002583479691.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000137Z&HW-CC-Expire=86400&HW-CC-Sign=AB7F3834DE15BC44C3D8F62DE425B39C8A887C310232708BB280FA5D82B17AF1)

### 示例11（通过ComponentContent预加载子节点）

该示例实现了通过ComponentContent设置TabBar，使用TabsController的preloadItems预加载子节点。

```
1. // xxx.ets
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { ComponentContent } from '@kit.ArkUI';

5. class Params {
6. text: string = '';
7. fontColor: string = '';

9. constructor(text: string, fontColor: string) {
10. this.text = text;
11. this.fontColor = fontColor;
12. }
13. }

15. @Component
16. struct imageCom {
17. build() {
18. Image($r('app.media.startIcon'))
19. .alt($r('app.media.background'))
20. .width(15)
21. .height(15)
22. }
23. }

25. @Builder
26. function TabBuilder(params: Params) {
27. Column({ space: 4 }) {
28. imageCom()

30. Text(params.text)
31. .fontSize(10)
32. .fontColor(params.fontColor)
33. }
34. }

36. @Entry
37. @Component
38. struct TabsPreloadItems {
39. @State currentIndex: number = 0;
40. private tabsController: TabsController = new TabsController();
41. context: UIContext = this.getUIContext();
42. unselectedFontColor: string = '#182431';
43. selectedFontColor: string = '#007DFF';

45. getTabBar1() {
46. this.tabBar1.update(new Params('green',
47. this.currentIndex === 0 ? this.selectedFontColor : this.unselectedFontColor));
48. return this.tabBar1;
49. }

51. getTabBar2() {
52. this.tabBar2.update(new Params('blue',
53. this.currentIndex === 1 ? this.selectedFontColor : this.unselectedFontColor));
54. return this.tabBar2;
55. }

57. getTabBar3() {
58. this.tabBar3.update(new Params('yellow',
59. this.currentIndex === 2 ? this.selectedFontColor : this.unselectedFontColor));
60. return this.tabBar3;
61. }

63. getTabBar4() {
64. this.tabBar4.update(new Params('pink',
65. this.currentIndex === 3 ? this.selectedFontColor : this.unselectedFontColor));
66. return this.tabBar4;
67. }

69. tabBar1: ComponentContent<Params> =
70. new ComponentContent<Params>(this.context, wrapBuilder<[Params]>(TabBuilder),
71. new Params('green', this.selectedFontColor));
72. tabBar2: ComponentContent<Params> =
73. new ComponentContent<Params>(this.context, wrapBuilder<[Params]>(TabBuilder),
74. new Params('blue', this.unselectedFontColor));
75. tabBar3: ComponentContent<Params> =
76. new ComponentContent<Params>(this.context, wrapBuilder<[Params]>(TabBuilder),
77. new Params('yellow', this.unselectedFontColor));
78. tabBar4: ComponentContent<Params> =
79. new ComponentContent<Params>(this.context, wrapBuilder<[Params]>(TabBuilder),
80. new Params('pink', this.unselectedFontColor));

82. build() {
83. Column() {
84. Tabs({ index: this.currentIndex, controller: this.tabsController }) {
85. TabContent() {
86. MyComponent({ color: '#00CB87' })
87. }.tabBar(this.getTabBar1())

89. TabContent() {
90. MyComponent({ color: '#007DFF' })
91. }.tabBar(this.getTabBar2())

93. TabContent() {
94. MyComponent({ color: '#FFBF00' })
95. }.tabBar(this.getTabBar3())

97. TabContent() {
98. MyComponent({ color: '#E67C92' })
99. }.tabBar(this.getTabBar4())
100. }
101. .width(360)
102. .height(296)
103. .backgroundColor('#F1F3F5')
104. .onChange((index: number) => {
105. this.currentIndex = index;
106. })

108. Button('preload items: [1,2,3]')
109. .margin(5)
110. .onClick(() => {
111. // 预加载index为1~3的子节点
112. this.tabsController.preloadItems([1, 2, 3])
113. .then(() => {
114. console.info('preloadItems success.');
115. })
116. .catch((error: BusinessError) => {
117. console.error('preloadItems failed, error code: ' + error.code + ', error message: ' + error.message);
118. });
119. })

121. Button('preload items: [1]')
122. .margin(5)
123. .onClick(() => {
124. // 预加载index为1的子节点
125. this.tabsController.preloadItems([1])
126. .then(() => {
127. console.info('preloadItems success.');
128. })
129. .catch((error: BusinessError) => {
130. console.error('preloadItems failed, error code: ' + error.code + ', error message: ' + error.message);
131. });
132. })
133. Button('preload items: [3]')
134. .margin(5)
135. .onClick(() => {
136. // 预加载index为3的子节点
137. this.tabsController.preloadItems([3])
138. .then(() => {
139. console.info('preloadItems success.');
140. })
141. .catch((error: BusinessError) => {
142. console.error('preloadItems failed, error code: ' + error.code + ', error message: ' + error.message);
143. });
144. })
145. }
146. }
147. }

149. @Component
150. struct MyComponent {
151. private color: string = '';

153. aboutToAppear(): void {
154. console.info('aboutToAppear backgroundColor:' + this.color);
155. }

157. aboutToDisappear(): void {
158. console.info('aboutToDisappear backgroundColor:' + this.color);
159. }

161. build() {
162. Column()
163. .width('100%')
164. .height('100%')
165. .backgroundColor(this.color)
166. }
167. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/1jnl7PdNQduOXz_DyCMyzA/zh-cn_image_0000002552800042.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000137Z&HW-CC-Expire=86400&HW-CC-Sign=EE74329F48886AC15824409FA35545CFC5E85F6D061531DD9B34955F40994499)

### 示例12（设置子页签indicator为图片）

从API version 22开始，本示例通过SubTabBarStyle中的indicator属性，实现了图片格式的子页签下划线风格。

```
1. import { DrawableDescriptor } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct TabsIndicatorExample {
6. @State isVertical: boolean = false;
7. @State text: string = '文本';
8. @State barMode: BarMode = BarMode.Fixed;
9. @State pixmapDesc: DrawableDescriptor | null = null;

11. async aboutToAppear() {
12. const resManager = this.getUIContext().getHostContext()?.resourceManager;
13. if (!resManager) {
14. return;
15. }
16. // $r('app.media.indicator')需要替换为开发者所需的图像资源文件。
17. let pixmapDescResult = resManager.getDrawableDescriptor($r('app.media.indicator').id);
18. if (pixmapDescResult) {
19. this.pixmapDesc = pixmapDescResult as DrawableDescriptor;
20. }
21. }

23. build() {
24. Column() {
25. Tabs() {
26. TabContent() {
27. Column().width('100%').height('100%').backgroundColor(Color.Pink)
28. }.tabBar(SubTabBarStyle.of('TabBar 1')
29. .indicator({
30. drawable: this.pixmapDesc,
31. height: 10,
32. width: 70,
33. borderRadius: 5,
34. marginTop: 5
35. }))

37. TabContent() {
38. Column().width('100%').height('100%').backgroundColor(Color.Green)
39. }.tabBar(SubTabBarStyle.of('TabBar 2')
40. .indicator({
41. drawable: this.pixmapDesc,
42. height: 10,
43. width: 70,
44. borderRadius: 5,
45. marginTop: 5
46. }))
47. }
48. .height('60%')
49. .backgroundColor(0xf1f3f5)
50. .barMode(BarMode.Fixed)
51. .barHeight(120)
52. .vertical(false)
53. }
54. .width('100%')
55. .height(500)
56. .padding('24vp')
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/UISbPw9rSXSMiUwzQhLzaQ/zh-cn_image_0000002583439737.png?HW-CC-KV=V1&HW-CC-Date=20260428T000137Z&HW-CC-Expire=86400&HW-CC-Sign=9D3E49704263E6506B788B3D909A0460971B49393831CF0E093295D5D7244C17)
