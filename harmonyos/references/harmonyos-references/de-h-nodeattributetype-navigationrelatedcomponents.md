---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/de-h-nodeattributetype-navigationrelatedcomponents
title: ArkUI_NodeAttributeType（导航类组件相关属性）
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_node.h > ArkUI_NodeAttributeType（导航类组件相关属性）
category: harmonyos-references
scraped_at: 2026-04-29T13:54:14+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:816eeb70f163fc62ec220d9a32ead0d9aa01469da29c977292585b3a8f32d528
---

```
1. enum ArkUI_NodeAttributeType
```

## 概述

定义ArkUI在Native侧可以设置的导航类组件相关属性样式集合，包含Swiper组件属性设置。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](capi-native-node-h.md)

## NODE\_SWIPER\_LOOP

```
1. NODE_SWIPER_LOOP = MAX_NODE_SCOPE_NUM * ARKUI_NODE_SWIPER = 1001000
```

Swiper是否开启循环，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 控制是否开启循环，0表示不循环，1表示循环，默认值为1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 控制是否开启循环，0表示不循环，1表示循环，默认值为1。 |

## NODE\_SWIPER\_AUTO\_PLAY

```
1. NODE_SWIPER_AUTO_PLAY = 1001001
```

Swiper子组件是否自动播放，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 控制子组件是否自动播放，0表示不自动播放，1表示自动播放，默认值为0。 |
| .value[1]?.i32 | 手指按下是否停止自动播放，0表示停止，1表示不停止，默认值为0。该参数从API version 16开始支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 控制子组件是否自动播放，0表示不自动播放，1表示自动播放，默认值为0。 |
| .value[1].i32 | 手指按下是否停止自动播放，0表示停止，1表示不停止。该参数从API version 16开始支持。 |

## NODE\_SWIPER\_SHOW\_INDICATOR

```
1. NODE_SWIPER_SHOW_INDICATOR = 1001002
```

Swiper是否显示导航点指示器，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否显示导航点指示器，0表示不显示导航点指示器，1表示显示导航点指示器，默认值为1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否显示导航点指示器，0表示不显示导航点指示器，1表示显示导航点指示器，默认值为1。 |

## NODE\_SWIPER\_INTERVAL

```
1. NODE_SWIPER_INTERVAL = 1001003
```

设置Swiper自动播放时播放的时间间隔，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 使用自动播放时播放的时间间隔，单位为毫秒。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 使用自动播放时播放的时间间隔，单位为毫秒。 |

## NODE\_SWIPER\_VERTICAL

```
1. NODE_SWIPER_VERTICAL = 1001004
```

设置Swiper是否为纵向滑动，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否为纵向滑动，0表示横向滑动，1表示纵向滑动，默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否为纵向滑动，0表示横向滑动，1表示纵向滑动，默认值为0。 |

## NODE\_SWIPER\_DURATION

```
1. NODE_SWIPER_DURATION = 1001005
```

设置Swiper子组件切换的动画时长，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 子组件切换的动画时长，单位为毫秒, 默认值为400。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 子组件切换的动画时长，单位为毫秒, 默认值为400。 |

## NODE\_SWIPER\_CURVE

```
1. NODE_SWIPER_CURVE = 1001006
```

设置Swiper的动画曲线，支持属性设置，属性重置和属性获取接口。未设置或未重置该属性时，动画曲线为[interpolatingSpring](js-apis-curve.md#curvesinterpolatingspring10)(-1, 1, 328, 34)；设置该属性异常时，取默认值ARKUI\_CURVE\_LINEAR。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置动画曲线参数，参数类型[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)，默认值为ARKUI\_CURVE\_LINEAR。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 设置动画曲线参数，参数类型[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)，默认值为ARKUI\_CURVE\_LINEAR。 |

## NODE\_SWIPER\_ITEM\_SPACE

```
1. NODE_SWIPER_ITEM_SPACE = 1001007
```

设置Swiper子组件与子组件之间间隙，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 子组件与子组件之间间隙数值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 子组件与子组件之间间隙数值。 |

## NODE\_SWIPER\_INDEX

```
1. NODE_SWIPER_INDEX = 1001008
```

设置Swiper当前在容器中显示的子组件的索引值，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 子组件的索引值。 |
| .value[1]?.i32 | 跳转动画模式，参数类型[ArkUI\_SwiperAnimationMode](capi-native-type-h.md#arkui_swiperanimationmode)。仅当次调用有效。  该参数从API version 15开始支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 子组件的索引值。 |

## NODE\_SWIPER\_DISPLAY\_COUNT

```
1. NODE_SWIPER_DISPLAY_COUNT = 1001009
```

设置Swiper一页内元素显示个数，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 视窗内显示的子元素个数。 |
| .value[1]?.i32 | 是否按组翻页，0：按子元素翻页，1：视窗内显示的子元素按组翻页，默认值：0。 |
| .string? | 此参数只能设置为“auto”。当设置为“auto”时，value[] 参数将被忽略。  该参数从API version 19开始支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 视窗内显示的子元素个数。 |
| .value[1].i32 | 是否按组翻页。该参数从API version 19开始支持。 |

## NODE\_SWIPER\_DISABLE\_SWIPE

```
1. NODE_SWIPER_DISABLE_SWIPE = 1001010
```

设置Swiper禁用组件滑动切换功能，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否禁用组件滑动切换功能，0表示不禁用滑动切换功能，1表示禁用滑动切换功能，默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否禁用组件滑动切换功能，0表示不禁用滑动切换功能，1表示禁用滑动切换功能，默认值为0。 |

## NODE\_SWIPER\_SHOW\_DISPLAY\_ARROW

```
1. NODE_SWIPER_SHOW_DISPLAY_ARROW = 1001011
```

设置Swiper是否显示导航点箭头，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置是否显示导航点箭头，参数类型[ArkUI\_SwiperArrow](capi-native-type-h.md#arkui_swiperarrow)，默认值为ARKUI\_SWIPER\_ARROW\_HIDE。 |
| .?object | 显示导航箭头时设置箭头样式，参数类型为[ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)。该参数从API version 19开始支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 设置是否显示导航点箭头，参数类型[ArkUI\_SwiperArrow](capi-native-type-h.md#arkui_swiperarrow)。 |
| .object | 箭头样式，参数类型为[ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)。该参数从API version 19开始支持。 |

## NODE\_SWIPER\_EDGE\_EFFECT\_MODE

```
1. NODE_SWIPER_EDGE_EFFECT_MODE = 1001012
```

设置Swiper的边缘滑动效果，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 边缘滑动效果，参数类型[ArkUI\_EdgeEffect](capi-native-type-h.md#arkui_edgeeffect)，  默认值为ARKUI\_EDGE\_EFFECT\_SPRING。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 边缘滑动效果，参数类型[ArkUI\_EdgeEffect](capi-native-type-h.md#arkui_edgeeffect)。 |

## NODE\_SWIPER\_NODE\_ADAPTER

```
1. NODE_SWIPER_NODE_ADAPTER = 1001013
```

swiper组件适配器，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 使用[ArkUI\_NodeAdapter](capi-arkui-nativemodule-arkui-nodeadapter8h.md)对象作为适配器。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 返回值格式为[ArkUI\_NodeAdapter](capi-arkui-nativemodule-arkui-nodeadapter8h.md)。 |

## NODE\_SWIPER\_CACHED\_COUNT

```
1. NODE_SWIPER_CACHED_COUNT = 1001014
```

swiper组件Adapter缓存数量，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 配合swiper组件Adapter使用，设置adapter中的缓存数量。 |
| .value[1]?.i32 | 是否显示缓存节点，0：不显示，1：显示，默认值：0。该参数从API version 19开始支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | adapter中的缓存数量。 |
| .value[1].i32 | 是否显示缓存节点，0：不显示，1：显示。该参数从API version 19开始支持。 |

## NODE\_SWIPER\_PREV\_MARGIN

```
1. NODE_SWIPER_PREV_MARGIN = 1001015
```

设置 Swiper 组件的前边距，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 前边距数值，单位为vp，默认值为0。 |
| .value[1]?.i32 | 是否忽略空白，1表示忽略空白，0表示不忽略空白。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 前边距数值，单位为vp。.value[1].i32：是否忽略空白，1表示忽略空白，0表示不忽略空白。 |

## NODE\_SWIPER\_NEXT\_MARGIN

```
1. NODE_SWIPER_NEXT_MARGIN = 1001016
```

设置 Swiper 组件的后边距，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 后边距数值，单位为vp，默认值为0。 |
| .value[1]?.i32 | 是否忽略空白，1表示忽略空白，0表示不忽略空白。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 后边距数值，单位为vp。.value[1].i32：是否忽略空白，1表示忽略空白，0表示不忽略空白。 |

## NODE\_SWIPER\_INDICATOR

```
1. NODE_SWIPER_INDICATOR = 1001017
```

设置 Swiper 组件的导航指示器类型，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置导航指示器的类型，参数类型[ArkUI\_SwiperIndicatorType](capi-native-type-h.md#arkui_swiperindicatortype)。 |
| .object | 导航指示器的类型为ARKUI\_SWIPER\_INDICATOR\_TYPE\_DOT时参数类型为[ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)。  导航指示器的类型为ARKUI\_SWIPER\_INDICATOR\_TYPE\_DIGIT时参数类型为[ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)。  ArkUI\_SwiperDigitIndicator类型从API version 19开始支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 导航指示器的类型，参数类型[ArkUI\_SwiperIndicatorType](capi-native-type-h.md#arkui_swiperindicatortype)。 |
| .object | 导航指示器的类型为ARKUI\_SWIPER\_INDICATOR\_TYPE\_DOT时参数类型为[ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)。  导航指示器的类型为ARKUI\_SWIPER\_INDICATOR\_TYPE\_DIGIT时参数类型为[ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)。  ArkUI\_SwiperDigitIndicator类型从API version 19开始支持。 |

## NODE\_SWIPER\_NESTED\_SCROLL

```
1. NODE_SWIPER_NESTED_SCROLL = 1001018
```

设置Swiper组件和父组件的嵌套滚动模式。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Swiper组件和父组件的嵌套滚动模式，参数类型[ArkUI\_SwiperNestedScrollMode](capi-native-type-h.md#arkui_swipernestedscrollmode)  默认值为：ARKUI\_SWIPER\_NESTED\_SRCOLL\_SELF\_ONLY。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Swiper组件和父组件的嵌套滚动模式，参数类型[ArkUI\_SwiperNestedScrollMode](capi-native-type-h.md#arkui_swipernestedscrollmode)。 |

## NODE\_SWIPER\_SWIPE\_TO\_INDEX

```
1. NODE_SWIPER_SWIPE_TO_INDEX = 1001019
```

设置swiper组件翻至指定页面。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 指定页面在Swiper中的索引值。 |
| .value[1]?.i32 | 设置翻至指定页面时是否有动效。1表示有动效，0表示没有动效, 默认值：0。 |

## NODE\_SWIPER\_INDICATOR\_INTERACTIVE

```
1. NODE_SWIPER_INDICATOR_INTERACTIVE = 1001020
```

设置禁用组件导航点交互功能。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置禁用组件导航点交互功能，设置为true时表示导航点可交互，设置为false时表示导航点不可交互，默认值true。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 设置禁用组件导航点交互功能。 |

## NODE\_SWIPER\_PAGE\_FLIP\_MODE

```
1. NODE_SWIPER_PAGE_FLIP_MODE = 1001021
```

设置组件鼠标滚轮翻页模式。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置组件鼠标滚轮翻页模式，参数类型[ArkUI\_PageFlipMode](capi-native-type-h.md#arkui_pageflipmode)。  属性获取方法返回值[ArkUI\_PageFlipMode](capi-native-type-h.md#arkui_pageflipmode)格式： |
| .value[0].i32 | 鼠标滚轮翻页模式。 |

## NODE\_SWIPER\_AUTO\_FILL

```
1. NODE_SWIPER_AUTO_FILL = 1001022
```

设置Swiper一页内元素显示个数根据元素最小宽度自适应，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 元素显示最小宽度，单位：vp。 |
| .value[1]?.i32 | 是否按组翻页，0：按子元素翻页，1：视窗内显示的子元素按组翻页，默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 元素显示最小宽度，单位：vp。 |
| .value[1].i32 | 是否按组翻页。 |

## NODE\_SWIPER\_MAINTAIN\_VISIBLE\_CONTENT\_POSITION

```
1. NODE_SWIPER_MAINTAIN_VISIBLE_CONTENT_POSITION = 1001023
```

设置Swiper显示区域外插入或删除数据是否保持可见内容位置不变。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Swiper显示区域外插入或删除数据是否保持可见内容位置不变。0表示不保持可见内容位置，1表示保持可见内容位置，默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Swiper显示区域外插入或删除数据是否保持可见内容位置不变。0表示不保持可见内容位置，1表示保持可见内容位置，默认值为0。 |

## NODE\_SWIPER\_ITEMFILLPOLICY

```
1. NODE_SWIPER_ITEMFILLPOLICY = 1001024
```

Swiper组件的响应式列数布局策略，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 在不同断点规格下的列数，数据类型[ArkUI\_ItemFillPolicy](capi-native-type-h.md#arkui_itemfillpolicy)。 |
| .value[1]?.i32 | 是否按组翻页，0：按子元素翻页，1：视窗内显示的子元素按组翻页，默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 在不同断点规格下的列数，数据类型[ArkUI\_ItemFillPolicy](capi-native-type-h.md#arkui_itemfillpolicy)。 |
| .value[1].i32 | 是否按组翻页。 |
