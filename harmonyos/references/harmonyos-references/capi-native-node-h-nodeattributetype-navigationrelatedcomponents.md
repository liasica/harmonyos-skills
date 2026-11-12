---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-navigationrelatedcomponents
title: ArkUI_NodeAttributeType（导航类组件相关属性）
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_node.h > ArkUI_NodeAttributeType（导航类组件相关属性）
category: harmonyos-references
scraped_at: 2026-11-12T09:54:43+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:ee45632e989b96e59f101d1e256b3d5a4afaef8791cffd9c96015b6e47f27f11
---

```c
enum ArkUI_NodeAttributeType
```

## 概述

定义ArkUI在Native侧可以设置的导航类组件相关属性样式集合，包含Swiper组件、ArcSwiper组件和ArcAlphabetIndexer组件属性设置。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](capi-native-node-h.md)

## NODE\_SWIPER\_LOOP

```c
NODE_SWIPER_LOOP = MAX_NODE_SCOPE_NUM * ARKUI_NODE_SWIPER = 1001000
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

```c
NODE_SWIPER_AUTO_PLAY = 1001001
```

Swiper子组件是否自动播放，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 控制子组件是否自动播放，0表示不自动播放，1表示自动播放，默认值为0。 |
| .value[1]?.i32 | 手指按下是否停止自动播放，0表示不停止自动播放，1表示停止自动播放，默认值为1。该参数从API version 16开始支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 控制子组件是否自动播放，0表示不自动播放，1表示自动播放，默认值为0。 |
| .value[1].i32 | 手指按下是否停止自动播放，0表示不停止自动播放，1表示停止自动播放。该参数从API version 16开始支持。 |

## NODE\_SWIPER\_SHOW\_INDICATOR

```c
NODE_SWIPER_SHOW_INDICATOR = 1001002
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

```c
NODE_SWIPER_INTERVAL = 1001003
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

```c
NODE_SWIPER_VERTICAL = 1001004
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

```c
NODE_SWIPER_DURATION = 1001005
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

```c
NODE_SWIPER_CURVE = 1001006
```

设置Swiper的动画曲线，支持属性设置，属性重置和属性获取接口。未设置或未重置该属性时，动画曲线为[interpolatingSpring](js-apis-curve.md#curvesinterpolatingspring10)(-1, 1, 328, 34)；设置该属性异常时，取默认值ARKUI\_CURVE\_LINEAR。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置动画曲线参数，参数类型[ArkUI\_AnimationCurve](capi-native-type-visual-h.md#arkui_animationcurve)，默认值为ARKUI\_CURVE\_LINEAR。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 设置动画曲线参数，参数类型[ArkUI\_AnimationCurve](capi-native-type-visual-h.md#arkui_animationcurve)，默认值为ARKUI\_CURVE\_LINEAR。 |

## NODE\_SWIPER\_ITEM\_SPACE

```c
NODE_SWIPER_ITEM_SPACE = 1001007
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

```c
NODE_SWIPER_INDEX = 1001008
```

设置Swiper当前在容器中显示的子组件的索引值，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 子组件的索引值。 |
| .value[1]?.i32 | 跳转动画模式，参数类型[ArkUI\_SwiperAnimationMode](capi-swiper-h.md#arkui_swiperanimationmode)。仅当次调用有效。  该参数从API version 15开始支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 子组件的索引值。 |

## NODE\_SWIPER\_DISPLAY\_COUNT

```c
NODE_SWIPER_DISPLAY_COUNT = 1001009
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

```c
NODE_SWIPER_DISABLE_SWIPE = 1001010
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

```c
NODE_SWIPER_SHOW_DISPLAY_ARROW = 1001011
```

设置Swiper是否显示导航箭头，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置是否显示导航点箭头，参数类型[ArkUI\_SwiperArrow](capi-swiper-h.md#arkui_swiperarrow)，默认值为ARKUI\_SWIPER\_ARROW\_HIDE。 |
| .?object | 显示导航箭头时设置箭头样式，参数类型为[ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)。该参数从API version 19开始支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 设置是否显示导航点箭头，参数类型[ArkUI\_SwiperArrow](capi-swiper-h.md#arkui_swiperarrow)。 |
| .object | 箭头样式，参数类型为[ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)。该参数从API version 19开始支持。 |

## NODE\_SWIPER\_EDGE\_EFFECT\_MODE

```c
NODE_SWIPER_EDGE_EFFECT_MODE = 1001012
```

设置Swiper的边缘滑动效果，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 边缘滑动效果，参数类型[ArkUI\_EdgeEffect](capi-scroll-h.md#arkui_edgeeffect)，  默认值为ARKUI\_EDGE\_EFFECT\_SPRING。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 边缘滑动效果，参数类型[ArkUI\_EdgeEffect](capi-scroll-h.md#arkui_edgeeffect)。 |

## NODE\_SWIPER\_NODE\_ADAPTER

```c
NODE_SWIPER_NODE_ADAPTER = 1001013
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

```c
NODE_SWIPER_CACHED_COUNT = 1001014
```

swiper组件Adapter缓存数量，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 配合swiper组件Adapter使用，设置adapter中的缓存数量。 |
| .value[1]?.i32 | 是否显示缓存节点，0：不显示，1：显示，默认值：0。该参数从API version 19开始支持。 |
| .value[2]?.i32 | 缓存数量是否按组计算，即预加载子组件个数以组为基本单位。1：缓存数量为真实设置数量，0：当NODE\_SWIPER\_DISPLAY\_COUNT设置按组翻页时，缓存数量按组计算，不设置时为真实设置数量。默认值：0。该参数从API version 24开始支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | adapter中的缓存数量。 |
| .value[1].i32 | 是否显示缓存节点，0：不显示，1：显示。该参数从API version 19开始支持。 |
| .value[2].i32 | 缓存数量是否按组计算。该参数从API version 24开始支持。 \n |

## NODE\_SWIPER\_PREV\_MARGIN

```c
NODE_SWIPER_PREV_MARGIN = 1001015
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
| .value[0].f32 | 前边距数值，单位为vp。 |
| .value[1].i32 | 是否忽略空白，1表示忽略空白，0表示不忽略空白。 |

## NODE\_SWIPER\_NEXT\_MARGIN

```c
NODE_SWIPER_NEXT_MARGIN = 1001016
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
| .value[0].f32 | 后边距数值，单位为vp。 |
| .value[1].i32 | 是否忽略空白，1表示忽略空白，0表示不忽略空白。 |

## NODE\_SWIPER\_INDICATOR

```c
NODE_SWIPER_INDICATOR = 1001017
```

设置 Swiper 组件的导航指示器类型，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置导航指示器的类型，参数类型[ArkUI\_SwiperIndicatorType](capi-swiper-h.md#arkui_swiperindicatortype)。 |
| .object | 导航指示器的类型为ARKUI\_SWIPER\_INDICATOR\_TYPE\_DOT时参数类型为[ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)。  导航指示器的类型为ARKUI\_SWIPER\_INDICATOR\_TYPE\_DIGIT时参数类型为[ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)。  ArkUI\_SwiperDigitIndicator类型从API version 19开始支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 导航指示器的类型，参数类型[ArkUI\_SwiperIndicatorType](capi-swiper-h.md#arkui_swiperindicatortype)。 |
| .object | 导航指示器的类型为ARKUI\_SWIPER\_INDICATOR\_TYPE\_DOT时参数类型为[ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)。  导航指示器的类型为ARKUI\_SWIPER\_INDICATOR\_TYPE\_DIGIT时参数类型为[ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)。  ArkUI\_SwiperDigitIndicator类型从API version 19开始支持。 |

## NODE\_SWIPER\_NESTED\_SCROLL

```c
NODE_SWIPER_NESTED_SCROLL = 1001018
```

设置Swiper组件和父组件的嵌套滚动模式。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Swiper组件和父组件的嵌套滚动模式，参数类型[ArkUI\_SwiperNestedScrollMode](capi-swiper-h.md#arkui_swipernestedscrollmode)  默认值为：ARKUI\_SWIPER\_NESTED\_SRCOLL\_SELF\_ONLY。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Swiper组件和父组件的嵌套滚动模式，参数类型[ArkUI\_SwiperNestedScrollMode](capi-swiper-h.md#arkui_swipernestedscrollmode)。 |

## NODE\_SWIPER\_SWIPE\_TO\_INDEX

```c
NODE_SWIPER_SWIPE_TO_INDEX = 1001019
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

```c
NODE_SWIPER_INDICATOR_INTERACTIVE = 1001020
```

设置组件导航点是否可交互。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置组件导航点交互功能，0表示导航点不可交互，1表示导航点可交互，默认值为1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 组件导航点是否可交互，0表示不可交互，1表示可交互。 |

## NODE\_SWIPER\_PAGE\_FLIP\_MODE

```c
NODE_SWIPER_PAGE_FLIP_MODE = 1001021
```

设置组件鼠标滚轮翻页模式。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下，作为属性获取方法返回值[ArkUI\_PageFlipMode](capi-swiper-h.md#arkui_pageflipmode)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置组件鼠标滚轮翻页模式，参数类型[ArkUI\_PageFlipMode](capi-swiper-h.md#arkui_pageflipmode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 鼠标滚轮翻页模式。 |

## NODE\_SWIPER\_AUTO\_FILL

```c
NODE_SWIPER_AUTO_FILL = 1001022
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

```c
NODE_SWIPER_MAINTAIN_VISIBLE_CONTENT_POSITION = 1001023
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

```c
NODE_SWIPER_ITEMFILLPOLICY = 1001024
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

## NODE\_ARC\_ALPHABET\_INDEXER\_ARRAY

```c
NODE_ARC_ALPHABET_INDEXER_ARRAY = MAX_NODE_SCOPE_NUM * ARKUI_NODE_ARC_ALPHABET_INDEXER = 23000
```

设置索引字符串数组，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 索引字符串数组，类型为字符串数组。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 索引字符串数组，类型为字符串数组。 |

## NODE\_ARC\_ALPHABET\_INDEXER\_COLOR

```c
NODE_ARC_ALPHABET_INDEXER_COLOR = 23001
```

设置索引项在非选中状态下的文本颜色，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 文本颜色，0xargb格式。默认值为0xFFFFFFFF，表示白色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 文本颜色，0xargb格式。 |

## NODE\_ARC\_ALPHABET\_INDEXER\_SELECTED\_COLOR

```c
NODE_ARC_ALPHABET_INDEXER_SELECTED_COLOR = 23002
```

设置索引项在选中状态下的文本颜色，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 文本颜色，0xargb格式。默认值为0xFFFFFFFF，表示白色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 文本颜色，0xargb格式。 |

## NODE\_ARC\_ALPHABET\_INDEXER\_POPUP\_COLOR

```c
NODE_ARC_ALPHABET_INDEXER_POPUP_COLOR = 23003
```

设置提示弹窗的文本颜色，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 文本颜色，0xargb格式。默认值为0xFFFFFFFF，表示白色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 文本颜色，0xargb格式。 |

## NODE\_ARC\_ALPHABET\_INDEXER\_SELECTED\_BACKGROUND\_COLOR

```c
NODE_ARC_ALPHABET_INDEXER_SELECTED_BACKGROUND_COLOR = 23004
```

设置索引项在选中状态下的背景颜色，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 背景颜色，0xargb格式。默认值为0xFF1F71FF，表示蓝色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 背景颜色，0xargb格式。 |

## NODE\_ARC\_ALPHABET\_INDEXER\_POPUP\_BACKGROUND\_COLOR

```c
NODE_ARC_ALPHABET_INDEXER_POPUP_BACKGROUND_COLOR = 23005
```

设置提示弹窗的背景颜色，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 背景颜色，0xargb格式。默认值为0xD8404040，表示深灰色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 背景颜色，0xargb格式。 |

## NODE\_ARC\_ALPHABET\_INDEXER\_USE\_POPUP

```c
NODE_ARC_ALPHABET_INDEXER_USE_POPUP = 23006
```

设置是否使用提示弹窗，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否使用提示弹窗，0表示不使用弹窗，1表示使用弹窗，默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否使用提示弹窗。 |

## NODE\_ARC\_ALPHABET\_SELECTED\_FONT

```c
NODE_ARC_ALPHABET_SELECTED_FONT = 23007
```

设置选中索引项的字体样式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 字体族，多个字体使用','进行分割，为可选参数。默认值为“HarmonyOS Sans”。 |
| .value[0].f32 | 字体大小，单位为fp，为可选参数，默认值为13。 |
| .value[1].i32 | 字体粗细，为可选参数，参数类型[ArkUI\_FontWeight](capi-text-h.md#arkui_fontweight)，默认值为ARKUI\_FONT\_WEIGHT\_W500。 |
| .value[2].i32 | 字体样式，为可选参数，参数类型[ArkUI\_FontStyle](capi-text-h.md#arkui_fontstyle)，默认值为ARKUI\_FONT\_STYLE\_NORMAL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 字体族，多个字体使用','进行分割。 |
| .value[0].f32 | 字体大小，单位为fp。 |
| .value[1].i32 | 字体粗细，参数类型[ArkUI\_FontWeight](capi-text-h.md#arkui_fontweight)。 |
| .value[2].i32 | 字体样式，参数类型[ArkUI\_FontStyle](capi-text-h.md#arkui_fontstyle)。 |

## NODE\_ARC\_ALPHABET\_INDEXER\_POPUP\_FONT

```c
NODE_ARC_ALPHABET_INDEXER_POPUP_FONT = 23008
```

设置提示弹窗的字体样式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 字体族，多个字体使用','进行分割，为可选参数。默认值为“HarmonyOS Sans”。 |
| .value[0].f32 | 字体大小，单位为fp，为可选参数，默认值为19。 |
| .value[1].i32 | 字体粗细，为可选参数，参数类型[ArkUI\_FontWeight](capi-text-h.md#arkui_fontweight)，默认值为ARKUI\_FONT\_WEIGHT\_W500。 |
| .value[2].i32 | 字体样式，为可选参数，参数类型[ArkUI\_FontStyle](capi-text-h.md#arkui_fontstyle)，默认值为ARKUI\_FONT\_STYLE\_NORMAL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 字体族，多个字体使用','进行分割。 |
| .value[0].f32 | 字体大小，单位为fp。 |
| .value[1].i32 | 字体粗细，参数类型[ArkUI\_FontWeight](capi-text-h.md#arkui_fontweight)。 |
| .value[2].i32 | 字体样式，参数类型[ArkUI\_FontStyle](capi-text-h.md#arkui_fontstyle)。 |

## NODE\_ARC\_ALPHABET\_FONT

```c
NODE_ARC_ALPHABET_FONT = 23009
```

设置索引项的默认字体样式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 字体族，多个字体使用','进行分割，为可选参数。默认值为“HarmonyOS Sans”。 |
| .value[0].f32 | 字体大小，单位为fp，为可选参数，默认值为13。 |
| .value[1].i32 | 字体粗细，为可选参数，参数类型[ArkUI\_FontWeight](capi-text-h.md#arkui_fontweight)，默认值为ARKUI\_FONT\_WEIGHT\_W500。 |
| .value[2].i32 | 字体样式，为可选参数，参数类型[ArkUI\_FontStyle](capi-text-h.md#arkui_fontstyle)，默认值为ARKUI\_FONT\_STYLE\_NORMAL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 字体族，多个字体使用','进行分割。 |
| .value[0].f32 | 字体大小，单位为fp。 |
| .value[1].i32 | 字体粗细，参数类型[ArkUI\_FontWeight](capi-text-h.md#arkui_fontweight)。 |
| .value[2].i32 | 字体样式，参数类型[ArkUI\_FontStyle](capi-text-h.md#arkui_fontstyle)。 |

## NODE\_ARC\_ALPHABET\_INDEXER\_ITEM\_SIZE

```c
NODE_ARC_ALPHABET_INDEXER_ITEM_SIZE = 23010
```

设置字母索引条字母区域大小，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 字母区域为圆形，设置该圆形的直径，单位为vp，默认值为24。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 字母区域为圆形，设置该圆形的直径，单位为vp。 |

## NODE\_ARC\_ALPHABET\_INDEXER\_SELECTED

```c
NODE_ARC_ALPHABET_INDEXER_SELECTED = 23011
```

设置选中项的索引，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 选中项的索引，默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 选中项的索引。 |

## NODE\_ARC\_ALPHABET\_AUTO\_COLLAPSE

```c
NODE_ARC_ALPHABET_AUTO_COLLAPSE = 23012
```

设置当索引条空间不足以显示全部字符时是否折叠字符，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 当索引条空间不足以显示全部字符时是否折叠字符，1表示自动折叠字符，0表示不折叠，默认值为1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 当索引条空间不足以显示全部字符时是否折叠字符。 |

## NODE\_ARC\_ALPHABET\_POPUP\_BACKGROUND\_BLUR\_STYLE

```c
NODE_ARC_ALPHABET_POPUP_BACKGROUND_BLUR_STYLE = 23013
```

设置提示弹窗的背景模糊样式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 提示弹窗的背景模糊样式，参数类型[ArkUI\_BlurStyle](capi-native-type-visual-h.md#arkui_blurstyle)，默认值为ARKUI\_BLUR\_STYLE\_NONE。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 提示弹窗的背景模糊样式。 |

## NODE\_ARC\_SWIPER\_INDEX

```c
NODE_ARC_SWIPER_INDEX = MAX_NODE_SCOPE_NUM * ARKUI_NODE_ARC_SWIPER = 1022000
```

设置当前在ArcSwiper容器中显示的子组件的索引，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 子组件的索引值，默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 子组件的索引值。 |

## NODE\_ARC\_SWIPER\_INDICATOR

```c
NODE_ARC_SWIPER_INDICATOR = 1022001
```

设置ArcSwiper的导航点指示器，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否显示导航点指示器，1表示显示导航点指示器，0表示不显示，默认值为1。 |
| .value[1].i32 | ArcSwiper导航点指示器的方向，参数类型[OH\_ArkUI\_ArcDirection](capi-native-type-h.md#oh_arkui_arcdirection)，默认值为OH\_ARKUI\_ARCDIRECTION\_SIX\_CLOCK\_DIRECTION，为可选参数。 |
| .value[2].i32 | 未选中点的颜色，0xargb格式，默认值为0xA9FFFFFF，表示白色，为可选参数。 |
| .value[3].i32 | 选中点的颜色，0xargb格式，默认值为0xFF5EA1FF，表示蓝色，为可选参数。 |
| .value[4].i32 | 长按后ArcSwiper导航点指示器的背景颜色，0xargb格式，默认值为0xFF5EA1FF，表示蓝色，为可选参数。 |
| .object | 遮罩的渐变颜色，为可选参数。颜色停止点数组，每个颜色停止点由一种颜色及其停止位置组成。参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。无效颜色会被自动跳过。colors：颜色停止点的颜色。stops：颜色停止点的停止位置。size：颜色数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否显示导航点指示器。 |
| .value[1].i32 | ArcSwiper导航点指示器的方向。 |
| .value[2].u32 | 未选中点的颜色。 |
| .value[3].u32 | 选中点的颜色。 |
| .value[4].u32 | 长按后ArcSwiper导航点指示器的背景颜色。 |
| .object | 遮罩的渐变颜色。 |

## NODE\_ARC\_SWIPER\_DURATION

```c
NODE_ARC_SWIPER_DURATION = 1022002
```

设置子组件切换的动画时长，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 子组件切换的动画时长，单位为毫秒，默认值为400。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 子组件切换的动画时长，单位为毫秒。 |

## NODE\_ARC\_SWIPER\_VERTICAL

```c
NODE_ARC_SWIPER_VERTICAL = 1022003
```

设置是否为纵向滑动，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否为纵向滑动，1表示纵向滑动，0表示横向滑动，默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否为纵向滑动。 |

## NODE\_ARC\_SWIPER\_DISABLE\_SWIPE

```c
NODE_ARC_SWIPER_DISABLE_SWIPE = 1022004
```

设置是否禁用滑动功能，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否禁用滑动功能，1表示禁用滑动功能，0表示不禁用，默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否禁用滑动功能。 |

## NODE\_ARC\_SWIPER\_DIGITAL\_CROWN\_SENSITIVITY

```c
NODE_ARC_SWIPER_DIGITAL_CROWN_SENSITIVITY = 1022005
```

设置转动表冠的灵敏度，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 转动表冠的灵敏度，参数类型[ArkUI\_CrownSensitivity](capi-native-type-h.md#arkui_crownsensitivity)，默认值为ARKUI\_CROWN\_SENSITIVITY\_MEDIUM。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 转动表冠的灵敏度。 |

## NODE\_ARC\_SWIPER\_EFFECT\_MODE

```c
NODE_ARC_SWIPER_EFFECT_MODE = 1022006
```

设置滑动到可滚动内容的边界时ArcSwiper边缘的滑动效果，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 滑动到可滚动内容的边界时ArcSwiper边缘的滑动效果，参数类型[ArkUI\_EdgeEffect](capi-scroll-h.md#arkui_edgeeffect)，默认值为ARKUI\_EDGE\_EFFECT\_SPRING。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 滑动到可滚动内容的边界时ArcSwiper边缘的滑动效果，参数类型[ArkUI\_EdgeEffect](capi-scroll-h.md#arkui_edgeeffect)。 |

## NODE\_ARC\_SWIPER\_DISABLE\_TRANSITION\_ANIMATION

```c
NODE_ARC_SWIPER_DISABLE_TRANSITION_ANIMATION = 1022007
```

设置是否禁用转场动画，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否禁用转场动画，1表示禁用转场动画，0表示不禁用，默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否禁用转场动画。 |
