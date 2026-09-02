---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-scrollablecontainer
title: ArkUI_NodeAttributeType（滚动容器类组件相关属性）
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_node.h > ArkUI_NodeAttributeType（滚动容器类组件相关属性）
category: harmonyos-references
scraped_at: 2026-09-02T15:01:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7c502e0dd7ca0b4b6299ac8e4063f7293acd4bed435264b42794301d4f4424f2
---

```c
enum ArkUI_NodeAttributeType
```

## 概述

定义ArkUI在Native侧可以设置的滚动容器类组件相关属性样式集合，包含Scroll、List、ListItem、ListItemGroup、Refresh、WaterFlow、Grid、GridItem、ArcList、ArcListItem、ArcScrollBar等组件属性设置。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](capi-native-node-h.md)

## NODE\_SCROLL\_BAR\_DISPLAY\_MODE

```c
NODE_SCROLL_BAR_DISPLAY_MODE = MAX_NODE_SCOPE_NUM * ARKUI_NODE_SCROLL = 1002000
```

设置滚动条状态，支持属性设置，属性重置和属性获取接口。[List](ts-container-list.md)/[Scroll](ts-container-scroll.md)/[WaterFlow](ts-container-waterflow.md)从API version 12开始支持，[Grid](ts-container-grid.md)从API version 22开始支持。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 滚动条状态，数据类型[ArkUI\_ScrollBarDisplayMode](capi-scroll-h.md#arkui_scrollbardisplaymode)，List、Grid、Scroll组件默认值为[ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_AUTO](capi-scroll-h.md#arkui_scrollbardisplaymode)，WaterFlow组件默认值为[ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_OFF](capi-scroll-h.md#arkui_scrollbardisplaymode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 滚动条状态，数据类型[ArkUI\_ScrollBarDisplayMode](capi-scroll-h.md#arkui_scrollbardisplaymode)。 |

## NODE\_SCROLL\_BAR\_WIDTH

```c
NODE_SCROLL_BAR_WIDTH = 1002001
```

设置滚动条的宽度，支持属性设置，属性重置和属性获取接口。[List](ts-container-list.md)/[Scroll](ts-container-scroll.md)/[WaterFlow](ts-container-waterflow.md)从API version 12开始支持，[Grid](ts-container-grid.md)从API version 22开始支持。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 滚动条宽度，单位vp，默认值4。  取值范围：[0, +∞)。设置为小于0的值时，按默认值处理，儿童智能表则恢复至默认值5vp。设置为0时，不显示滚动条。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 滚动条宽度，单位vp。 |

## NODE\_SCROLL\_BAR\_COLOR

```c
NODE_SCROLL_BAR_COLOR = 1002002
```

设置滚动条的颜色，支持属性设置，属性重置和属性获取接口。[List](ts-container-list.md)/[Scroll](ts-container-scroll.md)/[WaterFlow](ts-container-waterflow.md)从API version 12开始支持，[Grid](ts-container-grid.md)从API version 22开始支持。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .data[0].u32 | 滚动条颜色，0xargb类型。儿童智能表的默认值颜色：0xffffffff，表示白色（100%不透明度）。其他设备默认值：0x66182431，表示深蓝灰色（40%不透明度）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .data[0].u32 | 滚动条颜色，0xargb类型。 |

## NODE\_SCROLL\_SCROLL\_DIRECTION

```c
NODE_SCROLL_SCROLL_DIRECTION = 1002003
```

设置滚动方向，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 滚动方向，数据类型[ArkUI\_ScrollDirection](capi-scroll-h.md#arkui_scrolldirection)，默认值[ARKUI\_SCROLL\_DIRECTION\_VERTICAL](capi-scroll-h.md#arkui_scrolldirection)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 滚动方向，数据类型[ArkUI\_ScrollDirection](capi-scroll-h.md#arkui_scrolldirection)。 |

## NODE\_SCROLL\_EDGE\_EFFECT

```c
NODE_SCROLL_EDGE_EFFECT = 1002004
```

设置边缘滑动效果，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 边缘滑动效果，参数类型[ArkUI\_EdgeEffect](capi-scroll-h.md#arkui_edgeeffect)，Grid、Scroll、WaterFlow组件默认值为[ARKUI\_EDGE\_EFFECT\_NONE](capi-scroll-h.md#arkui_edgeeffect)，List组件默认值为[ARKUI\_EDGE\_EFFECT\_SPRING](capi-scroll-h.md#arkui_edgeeffect)。 |
| .value[1]?.i32 | 可选值，组件内容大小小于组件自身时，设置是否开启滑动效果，开启为1，关闭为0，List、Grid、WaterFlow组件默认值为0，Scroll组件默认值为1。 |
| .value[2]?.i32 | 边缘效果生效的方向，参数类型[ArkUI\_EffectEdge](capi-scroll-h.md#arkui_effectedge)，默认值[ARKUI\_EFFECT\_EDGE\_START](capi-scroll-h.md#arkui_effectedge) | [ARKUI\_EFFECT\_EDGE\_END](capi-scroll-h.md#arkui_effectedge)。  该参数从API version 16开始支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 边缘滑动效果，参数类型[ArkUI\_EdgeEffect](capi-scroll-h.md#arkui_edgeeffect)。 |
| .value[1].i32 | 组件内容大小小于组件自身时，设置是否开启滑动效果，开启为1，关闭为0。 |
| .value[2].i32 | 边缘效果生效的方向，参数类型[ArkUI\_EffectEdge](capi-scroll-h.md#arkui_effectedge)。该参数从API version 16开始支持。 |

## NODE\_SCROLL\_ENABLE\_SCROLL\_INTERACTION

```c
NODE_SCROLL_ENABLE_SCROLL_INTERACTION = 1002005
```

设置是否支持滚动手势，当设置为0时，无法通过手指或者鼠标滚动，但不影响控制器的滚动接口。

List/Scroll/WaterFlow从API version 12开始支持，Grid从API version 22开始支持。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否支持滚动手势，默认值1。1：支持滚动手势，0：不支持滚动手势。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否支持滚动手势。1：支持滚动手势，0：不支持滚动手势。 |

## NODE\_SCROLL\_FRICTION

```c
NODE_SCROLL_FRICTION = 1002006
```

设置摩擦系数，手动滑动滚动区域时生效，只对惯性滚动过程有影响，对惯性滚动过程中的链式效果有间接影响。

List/Scroll/WaterFlow从API version 12开始支持，Grid从API version 22开始支持。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 摩擦系数，默认值：非可穿戴设备为0.6，可穿戴设备为0.9。取值范围：(0, +∞)，设置为小于等于0的值时，按默认值处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 摩擦系数。 |

## NODE\_SCROLL\_SNAP

```c
NODE_SCROLL_SNAP = 1002007
```

设置[Scroll](ts-container-scroll.md)组件的限位滚动模式，支持属性设置，属性重置和属性获取接口。如果同时设置了滑动翻页和限位滚动，则限位滚动优先生效，滑动翻页不生效。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Scroll组件限位滚动时的对齐方式，数据类型[ArkUI\_ScrollSnapAlign](capi-scroll-h.md#arkui_scrollsnapalign)，默认值[ARKUI\_SCROLL\_SNAP\_ALIGN\_NONE](capi-scroll-h.md#arkui_scrollsnapalign)。 |
| .value[1].i32 | 在Scroll组件限位滚动模式下，该参数设置为1（true）后，不允许Scroll在开头和第一页间自由滑动，设置为0（false）后，允许Scroll在开头和第一页间自由滑动，默认值1（true）。该参数仅在限位点为2个及以上时生效。 |
| .value[2].i32 | 在Scroll组件限位滚动模式下，该参数设置为1（true）后，不允许Scroll在最后一页和末尾间自由滑动，设置为0（false）后，允许Scroll在最后一页和末尾间自由滑动，默认值1（true）。该参数仅在限位点为2个及以上时生效。 |
| .value[3...].f32 | Scroll组件限位滚动时的限位点，限位点即为Scroll组件能滑动停靠的偏移量，单位：vp。可以1个或多个。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Scroll组件限位滚动时的对齐方式，数据类型[ArkUI\_ScrollSnapAlign](capi-scroll-h.md#arkui_scrollsnapalign)。 |
| .value[1].i32 | 在Scroll组件限位滚动模式下，该参数设置为1（true）后，不允许Scroll在开头和第一页间自由滑动，设置为0（false）后，允许Scroll在开头和第一页间自由滑动，默认值1（true）。该参数仅在限位点为2个及以上时生效。 |
| .value[2].i32 | 在Scroll组件限位滚动模式下，该参数设置为1（true）后，不允许Scroll在最后一页和末尾间自由滑动，设置为0（false）后，允许Scroll在最后一页和末尾间自由滑动，默认值1（true）。该参数仅在限位点为2个及以上时生效。 |
| .value[3...].f32 | Scroll组件限位滚动时的限位点，限位点即为Scroll组件能滑动停靠的偏移量，单位：vp。 |

## NODE\_SCROLL\_NESTED\_SCROLL

```c
NODE_SCROLL_NESTED_SCROLL = 1002008
```

设置嵌套滚动选项，支持属性设置，属性重置和属性获取。List/Scroll/WaterFlow从API version 12开始支持，Grid从API version 22开始支持。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 可滚动组件往末尾端滚动时的嵌套滚动，参数类型[ArkUI\_ScrollNestedMode](capi-scroll-h.md#arkui_scrollnestedmode)。 |
| .value[1].i32 | 可滚动组件往起始端滚动时的嵌套滚动，参数类型[ArkUI\_ScrollNestedMode](capi-scroll-h.md#arkui_scrollnestedmode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 可滚动组件往末尾端滚动时的嵌套滚动，参数类型[ArkUI\_ScrollNestedMode](capi-scroll-h.md#arkui_scrollnestedmode)。 |
| .value[1].i32 | 可滚动组件往起始端滚动时的嵌套滚动，参数类型[ArkUI\_ScrollNestedMode](capi-scroll-h.md#arkui_scrollnestedmode)。 |

## NODE\_SCROLL\_OFFSET

```c
NODE_SCROLL_OFFSET = 1002009
```

设置[Scroll](ts-container-scroll.md)组件滑动到指定位置，支持属性设置，属性重置和属性获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 水平滑动偏移，单位为vp。取值范围：[0, +∞)，设置为小于0的值时按0处理。值为0时滚动到起始位置，值大于0时滚动到指定偏移位置。 |
| .value[1].f32 | 垂直滑动偏移，单位为vp。取值范围：[0, +∞)，设置为小于0的值时按0处理。值为0时滚动到起始位置，值大于0时滚动到指定偏移位置。 |
| .value[2]?.i32 | 可选值，滚动时长，单位为毫秒，默认值1000。滚动时长大于0或使能默认弹簧动效时，滚动带动画效果。 |
| .value[3]?.i32 | 可选值，滚动曲线，参数类型[ArkUI\_AnimationCurve](capi-native-type-visual-h.md#arkui_animationcurve)。默认值为[ARKUI\_CURVE\_EASE](capi-native-type-visual-h.md#arkui_animationcurve)。 |
| .value[4]?.i32 | 可选值，是否使能默认弹簧动效，默认值为0不使能。 |
| .value[5]?.i32 | 可选值，设置动画滚动到边界是否转换为越界回弹动画，默认值为0不转换越界回弹动画。 |
| .value[6]?.i32 | 可选值，设置滚动是否可以停留在越界位置，默认值为0不停留在越界位置。该参数从API version 20开始支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 水平滑动偏移，单位为vp。 |
| .value[1].f32 | 垂直滑动偏移，单位为vp。 |

## NODE\_SCROLL\_EDGE

```c
NODE_SCROLL_EDGE = 1002010
```

设置[Scroll](ts-container-scroll.md)组件滚动到容器边缘位置，支持属性设置和属性获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 容器边缘位置，参数类型[ArkUI\_ScrollEdge](capi-scroll-h.md#arkui_scrolledge)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 容器是否位于边缘。-1表示未处于边缘；处于边缘状态时，返回值为[ArkUI\_ScrollEdge](capi-scroll-h.md#arkui_scrolledge)枚举值，表示具体边缘位置。 |

## NODE\_SCROLL\_ENABLE\_PAGING

```c
NODE_SCROLL_ENABLE_PAGING = 1002011
```

设置是否支持滑动翻页，支持属性设置，属性重置和属性获取接口。如果同时设置了滑动翻页[enablePaging](ts-container-scroll.md#enablepaging11)和限位滚动[scrollSnap](ts-container-scroll.md#scrollsnap10)，则[scrollSnap](ts-container-scroll.md#scrollsnap10)优先生效，[enablePaging](ts-container-scroll.md#enablepaging11)不生效。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否支持滑动翻页，默认值0。0：不支持滑动翻页，1：支持滑动翻页。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否支持滑动翻页。0：不支持滑动翻页，1：支持滑动翻页。 |

## NODE\_SCROLL\_PAGE

```c
NODE_SCROLL_PAGE = 1002012
```

滚动到下一页或者上一页。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 翻页方向。0表示向下翻页，1表示向上翻页。 |
| .value[1]?.i32 | 是否开启翻页动画效果。1有动画，0无动画。默认值：0。 |

## NODE\_SCROLL\_BY

```c
NODE_SCROLL_BY = 1002013
```

滑动指定距离。从API version 12开始List/Scroll/WaterFlow组件支持滑动指定距离，从API版本26.0.0开始Grid组件支持滑动指定距离。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 水平方向滚动距离，单位：vp。 |
| .value[1].f32 | 垂直方向滚动距离，单位：vp。 |

## NODE\_SCROLL\_FLING

```c
NODE_SCROLL_FLING = 1002014
```

滚动类组件按传入的初始速度进行惯性滚动。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 惯性滚动的初始速度，单位：vp/s。值设置为0，视为异常值，本次滚动不生效。如果值为正数，则向下滚动；如果值为负数，则向上滚动。 |

## NODE\_SCROLL\_FADING\_EDGE

```c
NODE_SCROLL_FADING_EDGE = 1002015
```

设置滚动类组件边缘渐隐效果。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否使能边缘渐隐效果。0表示关闭边缘效果，1表示开启边缘效果，默认值0。 |
| .value[1]?.f32 | 边缘渐隐效果长度。单位：vp，默认值：32。  取值范围：值必须大于等于0。仅在开启边缘渐隐效果时生效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否使能边缘渐隐效果。0表示关闭边缘效果，1表示开启边缘效果。 |
| .value[1].f32 | 边缘渐隐效果长度。单位：vp。 |

## NODE\_SCROLL\_SIZE

```c
NODE_SCROLL_SIZE = 1002016
```

获取滚动类组件所有子组件全展开尺寸。

作为属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 14

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 滚动类组件所有子组件全展开的宽度，默认单位为vp。 |
| .value[1].f32 | 滚动类组件所有子组件全展开的高度，默认单位为vp。  设置NODE\_PADDING、NODE\_MARGIN或NODE\_BORDER\_WIDTH后，NODE\_PADDING、NODE\_MARGIN或NODE\_BORDER\_WIDTH在单位vp转换成单位px时会进行像素取整，返回值根据取整后的值计算。 |

## NODE\_SCROLL\_CONTENT\_START\_OFFSET

```c
NODE_SCROLL_CONTENT_START_OFFSET = 1002017
```

设置滚动类组件内容起始端偏移量。[List](ts-container-list.md)组件从API version 15开始支持，[Grid](ts-container-grid.md)/[Scroll](ts-container-scroll.md)/[WaterFlow](ts-container-waterflow.md)从API version 22开始支持。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 内容起始端偏移量，单位vp。默认值：0。取值范围：[0, +∞)。设置为负数时，按0处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 内容起始端偏移量，单位vp。 |

## NODE\_SCROLL\_CONTENT\_END\_OFFSET

```c
NODE_SCROLL_CONTENT_END_OFFSET = 1002018
```

设置滚动类组件内容末尾端偏移量。[List](ts-container-list.md)组件从API version 15开始支持，[Grid](ts-container-grid.md)/[Scroll](ts-container-scroll.md)/[WaterFlow](ts-container-waterflow.md)从API version 22开始支持。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 内容末尾端偏移量，单位vp。默认值：0。取值范围：[0, +∞)。设置为负数时，按0处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 内容末尾端偏移量，单位vp。 |

## NODE\_SCROLL\_FLING\_SPEED\_LIMIT

```c
NODE_SCROLL_FLING_SPEED_LIMIT = 1002019
```

限制跟手滑动结束后，Fling动效开始时的最大初始速度。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | Fling动效开始时的最大初始速度，单位：vp/s。非Wearable设备默认值为9000，Wearable设备默认值为5000。取值范围：(0, +∞)。设置为小于等于0的值时，按默认值处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | Fling动效开始时的最大初始速度，单位：vp/s。 |

## NODE\_SCROLL\_CLIP\_CONTENT

```c
NODE_SCROLL_CLIP_CONTENT = 1002020
```

设置滚动容器的内容层裁剪区域。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 内容裁剪模式，参数类型[ArkUI\_ContentClipMode](capi-scroll-h.md#arkui_contentclipmode)。[Grid](ts-container-grid.md)、[Scroll](ts-container-scroll.md)组件默认值为[ARKUI\_CONTENT\_CLIP\_MODE\_BOUNDARY](capi-scroll-h.md#arkui_contentclipmode)，[List](ts-container-list.md)、[WaterFlow](ts-container-waterflow.md)组件默认值为[ARKUI\_CONTENT\_CLIP\_MODE\_CONTENT\_ONLY](capi-scroll-h.md#arkui_contentclipmode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 内容裁剪模式，参数类型[ArkUI\_ContentClipMode](capi-scroll-h.md#arkui_contentclipmode)。 |

## NODE\_SCROLL\_BACK\_TO\_TOP

```c
NODE_SCROLL_BACK_TO_TOP = 1002021
```

设置滚动容器是否在点击状态栏时回到顶部。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否回到顶部，1表示回到顶部，0表示保持当前位置不变，默认值：API version 18之前：0。API version 18及以后：滚动方向是水平方向时为0，是垂直方向时为1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否回到顶部。1表示回到顶部，0表示保持当前位置不变。 |

## NODE\_SCROLL\_BAR\_MARGIN

```c
NODE_SCROLL_BAR_MARGIN = 1002022
```

设置滚动条的边距，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 设置滚动条起始边距，儿童智能表默认值为42，其他设备默认值为0，单位：vp。 |
| .value[1].f32 | 设置滚动条末尾边距，默认值为0，单位：vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 滚动条起始边距，单位：vp。 |
| .value[1].f32 | 滚动条末尾边距，单位：vp。 |

## NODE\_SCROLL\_MAX\_ZOOM\_SCALE

```c
NODE_SCROLL_MAX_ZOOM_SCALE = 1002023
```

设置滚动内容最大缩放比例。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 设置内容最大缩放比例。默认值：1  取值范围：(0, +∞)，小于或等于0时按默认值1处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 获取内容最大缩放比例。 |

## NODE\_SCROLL\_MIN\_ZOOM\_SCALE

```c
NODE_SCROLL_MIN_ZOOM_SCALE = 1002024
```

设置滚动内容最小缩放比例。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 设置内容最小缩放比例，默认值：1  取值范围：(0, NODE\_SCROLL\_MAX\_ZOOM\_SCALE]，小于或等于0时按默认值1处理，大于NODE\_SCROLL\_MAX\_ZOOM\_SCALE时按NODE\_SCROLL\_MAX\_ZOOM\_SCALE处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 获取内容最小缩放比例。 |

## NODE\_SCROLL\_ZOOM\_SCALE

```c
NODE_SCROLL_ZOOM_SCALE = 1002025
```

设置滚动内容缩放比例。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 设置内容缩放比例，默认值：1  取值范围：(0, +∞)，小于或等于0时按默认值1处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 获取内容缩放比例。 |

## NODE\_SCROLL\_ENABLE\_BOUNCES\_ZOOM

```c
NODE_SCROLL_ENABLE_BOUNCES_ZOOM = 1002026
```

设置是否支持过缩放回弹效果。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否支持过缩放回弹效果，0：不支持，1：支持。默认值：1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否支持过缩放回弹效果，0：不支持，1：支持。 |

## NODE\_SCROLL\_ENABLE\_SCROLL\_WITH\_MOUSE

```c
NODE_SCROLL_ENABLE_SCROLL_WITH_MOUSE = 1002027
```

设置是否支持鼠标左键按下拖动滚动，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否支持鼠标左键按下拖动滚动，0：不支持鼠标左键按下拖动滚动，1：支持鼠标左键按下拖动滚动。默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否支持鼠标左键按下拖动滚动，0：不支持鼠标左键按下拖动滚动，1：支持鼠标左键按下拖动滚动。 |

## NODE\_SCROLL\_AUTO\_ADJUST\_MARGIN

```c
NODE_SCROLL_AUTO_ADJUST_MARGIN = 1002028
```

设置滚动条是否自动调整边距以避让组件NODE\_PADDING、NODE\_SCROLL\_CONTENT\_START\_OFFSET或NODE\_SCROLL\_CONTENT\_END\_OFFSET的区域，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否自动调整边距，0：自动调整边距，1：不自动调整边距。默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否自动调整边距，0：自动调整边距，1：不自动调整边距。 |

## NODE\_SCROLL\_BAR\_HEIGHT

```c
NODE_SCROLL_BAR_HEIGHT = 1002029
```

设置滚动条滑轨高度。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 滚动条滑轨高度，单位：vp。默认值：自适应滚动组件高度。  取值范围：[0, +∞)。设置为小于0时使用默认值，儿童智能表则恢复至默认值37vp。设置为0时不显示滚动条。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 滚动条滑轨高度，单位：vp。 |

## NODE\_LIST\_DIRECTION

```c
NODE_LIST_DIRECTION = MAX_NODE_SCOPE_NUM * ARKUI_NODE_LIST = 1003000
```

设置[List](ts-container-list.md)组件排列方向。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | List组件排列方向，数据类型[ArkUI\_Axis](capi-layout-h.md#arkui_axis)，默认值ARKUI\_AXIS\_VERTICAL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | List组件排列方向，数据类型[ArkUI\_Axis](capi-layout-h.md#arkui_axis)。 |

## NODE\_LIST\_STICKY

```c
NODE_LIST_STICKY = 1003001
```

配合[ListItemGroup](ts-container-listitemgroup.md)组件使用，设置ListItemGroup中header和footer是否要吸顶或吸底，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 配合ListItemGroup组件使用，设置ListItemGroup中header和footer是否要吸顶或吸底。数据类型[ArkUI\_StickyStyle](capi-list-h.md#arkui_stickystyle)，默认值ARKUI\_STICKY\_STYLE\_NONE。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 配合ListItemGroup组件使用，设置ListItemGroup中header和footer是否要吸顶或吸底。数据类型[ArkUI\_StickyStyle](capi-list-h.md#arkui_stickystyle)。 |

## NODE\_LIST\_SPACE

```c
NODE_LIST_SPACE = 1003002
```

设置列表项间距，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 子组件主轴方向的间隔，单位vp，默认值0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 子组件主轴方向的间隔。 |

## NODE\_LIST\_NODE\_ADAPTER

```c
NODE_LIST_NODE_ADAPTER = 1003003
```

List组件适配器，支持属性设置，属性重置和属性获取接口。

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

## NODE\_LIST\_CACHED\_COUNT

```c
NODE_LIST_CACHED_COUNT = 1003004
```

List组件Adapter缓存数量，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 配合List组件Adapter使用，设置adapter中的缓存数量。 |
| .value[1]?.i32 | 是否显示缓存节点，0：不显示，1：显示，默认值：0。该参数从API version 15开始支持。 |
| .value[2]?.i32 | 设置List最大缓存数量，默认值与第一个参数相同。该参数从API version 22开始支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | adapter中的缓存数量。 |
| .value[1].i32 | 是否显示缓存节点，0：不显示，1：显示。该参数从API version 15开始支持。 |
| .value[2].i32 | List最大缓存数量。该参数从API version 22开始支持。 |

## NODE\_LIST\_SCROLL\_TO\_INDEX

```c
NODE_LIST_SCROLL_TO_INDEX = 1003005
```

滑动到指定index。开启平滑滚动动效时，会对经过的所有item进行加载和布局计算，当大量加载item时会导致性能问题。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 要滑动到的目标元素在当前容器中的索引值。传入-1时，指滑动到当前容器的最后一个元素。 |
| .value[1]?.i32 | 设置滑动到列表项在列表中的索引值时是否有动效，1表示有动效，0表示没有动效。默认值：0。 |
| .value[2]?.i32 | 指定滑动到的元素与当前容器的对齐方式，参数类型[ArkUI\_ScrollAlignment](capi-scroll-h.md#arkui_scrollalignment)，默认值：[ARKUI\_SCROLL\_ALIGNMENT\_START](capi-scroll-h.md#arkui_scrollalignment)。 |
| .value[3]?.f32 | 额外偏移量，默认值：0，单位：vp。正数表示向末尾端额外偏移，负数表示向起始端额外偏移。该参数从API version 15开始支持。 |

## NODE\_LIST\_ALIGN\_LIST\_ITEM

```c
NODE_LIST_ALIGN_LIST_ITEM = 1003006
```

设置List交叉轴方向宽度大于ListItem交叉轴宽度乘以布局数量时，ListItem在List交叉轴方向的布局方式。List垂直滚动时，布局数量为列数；List水平滚动时，布局数量为行数。支持属性设置、属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 交叉轴方向的布局方式。参数类型[ArkUI\_ListItemAlign](capi-list-h.md#arkui_listitemalignment)。默认值：ARKUI\_LIST\_ITEM\_ALIGNMENT\_START。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 交叉轴方向的布局方式。参数类型[ArkUI\_ListItemAlign](capi-list-h.md#arkui_listitemalignment)。 |

## NODE\_LIST\_CHILDREN\_MAIN\_SIZE

```c
NODE_LIST_CHILDREN_MAIN_SIZE = 1003007
```

设置List子组件默认主轴尺寸。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 参数格式为[ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 参数格式为[ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)。 |

## NODE\_LIST\_INITIAL\_INDEX

```c
NODE_LIST_INITIAL_INDEX = 1003008
```

设置当前List初次加载时视口起始位置显示的item的索引值，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 当前List初次加载时视口起始位置显示的item的索引值。默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 当前List初次加载时视口起始位置显示的item的索引值。 |

## NODE\_LIST\_DIVIDER

```c
NODE_LIST_DIVIDER = 1003009
```

设置ListItem分割线样式，默认无分割线，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 分割线颜色，0xargb类型，默认值为0x08000000。 |
| .value[1].f32 | 分割线宽，默认值：0，单位vp。 |
| .value[2].f32 | 分割线距离列表侧边起始端的距离，默认值：0，单位vp。 |
| .value[3].f32 | 分割线距离列表侧边结束端的距离，默认值：0，单位vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 分割线颜色，0xargb类型。 |
| .value[1].f32 | 分割线宽，单位vp。 |
| .value[2].f32 | 分割线距离列表侧边起始端的距离，单位vp。 |
| .value[3].f32 | 分割线距离列表侧边结束端的距离，单位vp。 |

## NODE\_LIST\_SCROLL\_TO\_INDEX\_IN\_GROUP

```c
NODE_LIST_SCROLL_TO_INDEX_IN_GROUP = 1003010
```

滑动到指定[ListItemGroup](ts-container-listitemgroup.md)中指定index。开启smooth动效时，会对经过的所有item进行加载和布局计算，当大量加载item时会导致性能问题。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 要滑动到的目标[ListItemGroup](ts-container-listitemgroup.md)在当前[List](ts-container-list.md)中的索引值。 |
| .value[1].i32 | 要滑动到的目标[ListItem](ts-container-listitem.md)在[ListItemGroup](ts-container-listitemgroup.md)中的索引值。 |
| .value[2]?.i32 | 设置滑动到列表项在列表中的索引值时是否有动效，1表示有动效，0表示没有动效。默认值：0。 |
| .value[3]?.i32 | 指定滑动到的元素与当前容器的对齐方式，参数类型[ArkUI\_ScrollAlignment](capi-scroll-h.md#arkui_scrollalignment)。默认值：[ARKUI\_SCROLL\_ALIGNMENT\_START](capi-scroll-h.md#arkui_scrollalignment)。 |

## NODE\_LIST\_LANES

```c
NODE_LIST_LANES = 1003011
```

设置List列数（List垂直滚动时表示列数，水平滚动时表示行数），支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | List布局列数或行数，List垂直滚动时表示列数，水平滚动时表示行数；如果同时设置了最小、最大列宽或行高，则设置列数或行数不生效；默认值：1，取值范围：[1, +∞)，设置异常值时使用默认值。 |
| .value[1]?.f32 | 最小列宽或行高，单位vp，默认值：-1（未设置）。 |
| .value[2]?.f32 | 最大列宽或行高，单位vp，默认值：-1（未设置）。 |
| .value[3]?.f32 | 列间距或行间距，默认值：0，单位vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 当前List布局列数或行数，List垂直滚动时表示列数，水平滚动时表示行数。 |
| .value[1].f32 | 最小列宽或行高，单位vp。 |
| .value[2].f32 | 最大列宽或行高，单位vp。 |
| .value[3].f32 | 列间距或行间距，单位vp。 |

## NODE\_LIST\_SCROLL\_SNAP\_ALIGN

```c
NODE_LIST_SCROLL_SNAP_ALIGN = 1003012
```

设置List限位对齐模式。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | List组件限位滚动时的对齐方式，数据类型[ArkUI\_ScrollSnapAlign](capi-scroll-h.md#arkui_scrollsnapalign)，默认值[ARKUI\_SCROLL\_SNAP\_ALIGN\_NONE](capi-scroll-h.md#arkui_scrollsnapalign)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | List组件限位滚动时的对齐方式，数据类型[ArkUI\_ScrollSnapAlign](capi-scroll-h.md#arkui_scrollsnapalign)。 |

## NODE\_LIST\_MAINTAIN\_VISIBLE\_CONTENT\_POSITION

```c
NODE_LIST_MAINTAIN_VISIBLE_CONTENT_POSITION = 1003013
```

设置List显示区域外插入或删除数据是否保持可见内容位置不变。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | List显示区域外插入或删除数据是否保持可见内容位置不变。0表示不保持可见内容位置，1表示保持可见内容位置，默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | List显示区域外插入或删除数据是否保持可见内容位置不变。0表示不保持可见内容位置，1表示保持可见内容位置，默认值为0。 |

## NODE\_LIST\_STACK\_FROM\_END

```c
NODE_LIST_STACK_FROM_END = 1003014
```

设置List从末尾开始布局。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置List是否从末尾开始布局。0表示从顶部开始布局，1表示从末尾开始布局，默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 设置List是否从末尾开始布局。0表示从顶部开始布局，1表示从末尾开始布局，默认值为0。 |

## NODE\_LIST\_FOCUS\_WRAP\_MODE

```c
NODE_LIST_FOCUS_WRAP_MODE = 1003015
```

List组件走焦换行模式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | List组件走焦换行模式，参数取值为[ArkUI\_FocusWrapMode](capi-native-type-h.md#arkui_focuswrapmode)下的枚举，默认值为ARKUI\_FOCUS\_WRAP\_MODE\_DEFAULT。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | List组件走焦换行模式，参数类型[ArkUI\_FocusWrapMode](capi-native-type-h.md#arkui_focuswrapmode)。 |

## NODE\_LIST\_SYNC\_LOAD

```c
NODE_LIST_SYNC_LOAD = 1003016
```

List组件是否同步加载子节点，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | List组件是否同步加载子节点。0：分帧加载，1：同步加载，默认值为1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | List组件是否同步加载子节点。0：分帧加载，1：同步加载。 |

## NODE\_LIST\_SCROLL\_SNAP\_ANIMATION\_SPEED

```c
NODE_LIST_SCROLL_SNAP_ANIMATION_SPEED = 1003017
```

List组件限位滚动动画速度，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | List组件限位滚动动画速度，数据类型[ArkUI\_ScrollSnapAnimationSpeed](capi-scroll-h.md#arkui_scrollsnapanimationspeed)。默认值：ARKUI\_SCROLL\_SNAP\_ANIMATION\_NORMAL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | List组件限位滚动动画速度，数据类型[ArkUI\_ScrollSnapAnimationSpeed](capi-scroll-h.md#arkui_scrollsnapanimationspeed)。 |

## NODE\_LIST\_LANES\_ITEMFILLPOLICY

```c
NODE_LIST_LANES_ITEMFILLPOLICY = 1003018
```

List组件的响应式列数布局策略，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 在不同断点规格下的列数，数据类型[ArkUI\_ItemFillPolicy](capi-native-type-h.md#arkui_itemfillpolicy)。 |
| .value[1]?.f32 | 列间距，单位vp。默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 在不同断点规格下的列数，数据类型[ArkUI\_ItemFillPolicy](capi-native-type-h.md#arkui_itemfillpolicy)。 |
| .value[1].f32 | 列间距，单位vp。 |

## NODE\_LIST\_SUPPORT\_EMPTY\_BRANCH\_IN\_LAZY\_LOADING

```c
NODE_LIST_SUPPORT_EMPTY_BRANCH_IN_LAZY_LOADING = 1003019
```

设置当前List组件是否支持在LazyForEach或Repeat中使用if/else渲染控制语法生成不包含任何子组件的空分支节点。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | List组件是否支持空分支。0：不支持，1：支持。默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | List组件是否支持空分支。0：不支持，1：支持。 |

## NODE\_LIST\_BACK\_PRESS\_BEHAVIOR

```c
NODE_LIST_BACK_PRESS_BEHAVIOR = 1003020
```

设置List组件的系统返回键行为，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 系统返回键生效时是否收起ListItem的划出组件。0：不收起，1：收起。默认值：1 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 系统返回键生效时是否收起ListItem的划出组件。0：不收起，1：收起。 |

## NODE\_LIST\_ENABLE\_EDIT\_MODE

```c
NODE_LIST_ENABLE_EDIT_MODE = 1003021
```

设置List组件是否启用编辑模式。进入编辑模式后，默认显示复选框，并支持手指滑动多选。支持属性设置、属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | List组件是否启用编辑模式。0：不启用，1：启用。默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | List组件是否启用编辑模式。0：未启用，1：已启用。 |

## NODE\_LIST\_EDIT\_MODE\_OPTIONS

```c
NODE_LIST_EDIT_MODE_OPTIONS = 1003022
```

设置List组件的编辑模式选项，支持属性设置、属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | List组件是否使用默认多选样式。0：不使用，1：使用。默认值：1。 |
| .value[1].i32 | List组件是否启用双指滑动多选。0：不启用，1：启用。默认值：1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | List组件是否使用默认多选样式。0：不使用，1：使用。 |
| .value[1].i32 | List组件是否启用双指滑动多选。0：未启用，1：已启用。 |

## NODE\_LIST\_ITEM\_SWIPE\_ACTION

```c
NODE_LIST_ITEM_SWIPE_ACTION = MAX_NODE_SCOPE_NUM * ARKUI_NODE_LIST_ITEM = 1004000
```

设置ListItem的划出组件，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 使用[ArkUI\_ListItemSwipeActionOption](capi-arkui-nativemodule-arkui-listitemswipeactionoption.md)对象构造。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 使用[ArkUI\_ListItemSwipeActionOption](capi-arkui-nativemodule-arkui-listitemswipeactionoption.md)对象构造。 |

## NODE\_LIST\_ITEM\_GROUP\_SET\_HEADER

```c
NODE_LIST_ITEM_GROUP_SET_HEADER = MAX_NODE_SCOPE_NUM * ARKUI_NODE_LIST_ITEM_GROUP = 1005000
```

设置 ListItemGroup 头部组件，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 使用[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)对象作为ListItemGroup头部组件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 使用[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)对象作为ListItemGroup头部组件。 |

## NODE\_LIST\_ITEM\_GROUP\_SET\_FOOTER

```c
NODE_LIST_ITEM_GROUP_SET_FOOTER = 1005001
```

设置 ListItemGroup 尾部组件，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 使用[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)对象作为ListItemGroup尾部组件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 使用[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)对象作为ListItemGroup尾部组件。 |

## NODE\_LIST\_ITEM\_GROUP\_SET\_DIVIDER

```c
NODE_LIST_ITEM_GROUP_SET_DIVIDER = 1005002
```

设置ListItem分割线样式，默认无分割线，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 颜色，0xargb类型，默认值为0x08000000。 |
| .value[1].f32 | 分割线宽，默认值：0，单位vp。 |
| .value[2].f32 | 分割线距离列表侧边起始端的距离，默认值：0，单位vp。 |
| .value[3].f32 | 分割线距离列表侧边结束端的距离，默认值：0，单位vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 颜色，0xargb类型。 |
| .value[1].f32 | 分割线宽，单位vp。 |
| .value[2].f32 | 分割线距离列表侧边起始端的距离，单位vp。 |
| .value[3].f32 | 分割线距离列表侧边结束端的距离，单位vp。 |

## NODE\_LIST\_ITEM\_GROUP\_CHILDREN\_MAIN\_SIZE

```c
NODE_LIST_ITEM_GROUP_CHILDREN_MAIN_SIZE = 1005003
```

设置ListItemGroup子组件默认主轴尺寸。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 参数格式为[ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 参数格式为[ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)。 |

## NODE\_LIST\_ITEM\_GROUP\_NODE\_ADAPTER

```c
NODE_LIST_ITEM_GROUP_NODE_ADAPTER = 1005004
```

[ListItemGroup](ts-container-listitemgroup.md)组件适配器，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 使用[ArkUI\_NodeAdapter](capi-arkui-nativemodule-arkui-nodeadapter8h.md)对象作为适配器。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 返回值格式为[ArkUI\_NodeAdapter](capi-arkui-nativemodule-arkui-nodeadapter8h.md)。 |

## NODE\_REFRESH\_REFRESHING

```c
NODE_REFRESH_REFRESHING = MAX_NODE_SCOPE_NUM * ARKUI_NODE_REFRESH = 1009000
```

设置组件是否正在刷新，支持属性设置，属性获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 参数值为1或者0，1表示正在刷新，0表示不在刷新。默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 参数值为1或者0，1表示正在刷新，0表示不在刷新。 |

## NODE\_REFRESH\_CONTENT

```c
NODE_REFRESH_CONTENT = 1009001
```

设置下拉区域的自定义内容，支持属性设置和重置。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 参数类型[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)。 |

## NODE\_REFRESH\_PULL\_DOWN\_RATIO

```c
NODE_REFRESH_PULL_DOWN_RATIO = 1009002
```

设置下拉跟手系数，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 下拉跟手系数，取值范围：[0, 1]。设置小于0或大于1的值时，属性设置失败。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 下拉跟手系数，取值范围：[0, 1]。 |

## NODE\_REFRESH\_OFFSET

```c
NODE_REFRESH_OFFSET = 1009003
```

设置触发刷新的下拉偏移量，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 下拉偏移量，单位vp， 默认值：64vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 下拉偏移量，单位vp， 默认值：64vp。 |

## NODE\_REFRESH\_PULL\_TO\_REFRESH

```c
NODE_REFRESH_PULL_TO_REFRESH = 1009004
```

设置当下拉距离超过[refreshOffset](ts-container-refresh.md#refreshoffset12)时是否触发刷新，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否触发刷新。支持取值为0或1，其中1为触发刷新，0为不触发刷新。默认值：1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否触发刷新，1为触发刷新，0为不触发刷新。 |

## NODE\_REFRESH\_MAX\_PULL\_DOWN\_DISTANCE

```c
NODE_REFRESH_MAX_PULL_DOWN_DISTANCE = 1009005
```

设置刷新的最大下拉距离。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 最大下拉距离，单位：vp。取值范围：[0, +∞)，设置小于0的值时按0处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 最大下拉距离，单位：vp。 |

## NODE\_REFRESH\_PULL\_UP\_TO\_CANCEL\_REFRESH

```c
NODE_REFRESH_PULL_UP_TO_CANCEL_REFRESH = 1009006
```

设置上划是否取消刷新。支持属性设置，属性重置和属性获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 上划是否取消刷新。支持取值为0或1，其中0为上划不取消刷新，1为上划取消刷新。默认值：1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 上划是否取消刷新。0为上划不取消刷新，1为上划取消刷新。 |

## NODE\_WATER\_FLOW\_LAYOUT\_DIRECTION

```c
NODE_WATER_FLOW_LAYOUT_DIRECTION = MAX_NODE_SCOPE_NUM * ARKUI_NODE_WATER_FLOW = 1010000
```

定义瀑布流组件布局主轴方向，支持属性设置、重置和获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 主轴方向，参数类型[ArkUI\_FlexDirection](capi-layout-h.md#arkui_flexdirection)。默认值[ARKUI\_FLEX\_DIRECTION\_COLUMN](capi-layout-h.md#arkui_flexdirection)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 主轴方向，参数类型[ArkUI\_FlexDirection](capi-layout-h.md#arkui_flexdirection)。 |

## NODE\_WATER\_FLOW\_COLUMN\_TEMPLATE

```c
NODE_WATER_FLOW_COLUMN_TEMPLATE = 1010001
```

设置当前瀑布流组件布局列的数量，不设置时默认1列，支持属性设置、重置和获取。例如，'1fr 1fr 2fr' 是将父组件分3列，将父组件允许的宽分为4等份，第1列占1份，第2列占1份，第3列占2份。可使用[columnsTemplate](ts-container-waterflow.md#columnstemplate)('repeat(auto-fill,track-size)')根据给定的列宽track-size自动计算列数，其中repeat、auto-fill为关键字，track-size为可设置的宽度，支持的单位包括px、vp、%或有效数字，默认单位为vp。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 布局列的数量。默认值：'1fr'。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 布局列的数量。 |

## NODE\_WATER\_FLOW\_ROW\_TEMPLATE

```c
NODE_WATER_FLOW_ROW_TEMPLATE = 1010002
```

设置当前瀑布流组件布局行的数量，不设置时默认1行，支持属性设置、重置和获取。例如，'1fr 1fr 2fr'是将父组件分3行，将父组件允许的高分为4等份，第1行占1份，第2行占1份，第3行占2份。可使用[rowsTemplate](ts-container-waterflow.md#rowstemplate)('repeat(auto-fill,track-size)')根据给定的行高track-size自动计算行数，其中repeat、auto-fill为关键字，track-size为可设置的高度，支持的单位包括px、vp、%或有效数字，默认单位为vp。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 布局行的数量。默认值：'1fr'。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 布局行的数量。 |

## NODE\_WATER\_FLOW\_COLUMN\_GAP

```c
NODE_WATER_FLOW_COLUMN_GAP = 1010003
```

设置列与列的间距，支持属性设置、重置和获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 列与列的间距，默认值：0，单位vp。取值范围：[0, +∞)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 列与列的间距，单位vp。 |

## NODE\_WATER\_FLOW\_ROW\_GAP

```c
NODE_WATER_FLOW_ROW_GAP = 1010004
```

设置行与行的间距，支持属性设置、重置和获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 行与行的间距，默认值：0，单位vp。取值范围：[0, +∞)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 行与行的间距，单位vp。 |

## NODE\_WATER\_FLOW\_SECTION\_OPTION

```c
NODE_WATER_FLOW_SECTION_OPTION = 1010005
```

设置FlowItem分组配置信息，支持属性设置、重置和获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 从0开始计算的索引，会转换为整数，表示要开始改变分组的位置。 |
| .object | 参数格式为[ArkUI\_WaterFlowSectionOption](capi-arkui-nativemodule-arkui-waterflowsectionoption.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 返回值格式为[ArkUI\_WaterFlowSectionOption](capi-arkui-nativemodule-arkui-waterflowsectionoption.md)。 |

## NODE\_WATER\_FLOW\_NODE\_ADAPTER

```c
NODE_WATER_FLOW_NODE_ADAPTER = 1010006
```

[WaterFlow](ts-container-waterflow.md)组件适配器，支持属性设置，属性重置和属性获取接口。

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

## NODE\_WATER\_FLOW\_CACHED\_COUNT

```c
NODE_WATER_FLOW_CACHED_COUNT = 1010007
```

[WaterFlow](ts-container-waterflow.md)组件Adapter缓存数量，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 配合WaterFlow组件Adapter使用，设置adapter中的缓存数量。 |
| .value[1]?.i32 | 是否显示缓存节点，0：不显示，1：显示，默认值：0。该参数从API version 16开始支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | adapter中的缓存数量。 |
| .value[1].i32 | 是否显示缓存节点，0：不显示，1：显示。该参数从API version 16开始支持。 |

## NODE\_WATER\_FLOW\_FOOTER

```c
NODE_WATER_FLOW_FOOTER = 1010008
```

设置瀑布流组件末尾的自定义显示组件。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 参数类型[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)。 |

## NODE\_WATER\_FLOW\_SCROLL\_TO\_INDEX

```c
NODE_WATER_FLOW_SCROLL_TO_INDEX = 1010009
```

滑动到指定index。开启smooth动效时，会对经过的所有item进行加载和布局计算，当大量加载item时会导致性能问题。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 要滑动到的目标元素在当前容器中的索引值。 |
| .value[1]?.i32 | 设置滑动到列表项在列表中的索引值时是否有动效，1表示有动效，0表示没有动效。默认值：0。 |
| .value[2]?.i32 | 指定滑动到的元素与当前容器的对齐方式，参数类型[ArkUI\_ScrollAlignment](capi-scroll-h.md#arkui_scrollalignment)。默认值为：[ARKUI\_SCROLL\_ALIGNMENT\_START](capi-scroll-h.md#arkui_scrollalignment)。 |
| .value[3]?.f32 | 滑动到目标元素后的额外偏移量，默认值：0，单位：vp。如果值为正数，则向底部额外偏移；如果值为负数，则向顶部额外偏移。该参数从API version 23开始支持。 |

## NODE\_WATER\_FLOW\_ITEM\_CONSTRAINT\_SIZE

```c
NODE_WATER_FLOW_ITEM_CONSTRAINT_SIZE = 1010010
```

设置当前瀑布流子组件的约束尺寸属性，约束子组件尺寸范围，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 最小宽度，单位：vp。使用-1表示不设置。 |
| .value[1].f32 | 最大宽度，单位：vp。使用-1表示不设置。 |
| .value[2].f32 | 最小高度，单位：vp。使用-1表示不设置。 |
| .value[3].f32 | 最大高度，单位：vp。使用-1表示不设置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 最小宽度，单位：vp。使用-1表示不设置。 |
| .value[1].f32 | 最大宽度，单位：vp。使用-1表示不设置。 |
| .value[2].f32 | 最小高度，单位：vp。使用-1表示不设置。 |
| .value[3].f32 | 最大高度，单位：vp。使用-1表示不设置。 |

## NODE\_WATER\_FLOW\_LAYOUT\_MODE

```c
NODE_WATER_FLOW_LAYOUT_MODE = 1010011
```

定义瀑布流组件布局模式，支持属性设置、重置和获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 布局模式，参数类型[ArkUI\_WaterFlowLayoutMode](capi-water-flow-h.md#arkui_waterflowlayoutmode)，默认值：[ARKUI\_WATER\_FLOW\_LAYOUT\_MODE\_ALWAYS\_TOP\_DOWN](capi-water-flow-h.md#arkui_waterflowlayoutmode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 布局模式，参数类型[ArkUI\_WaterFlowLayoutMode](capi-water-flow-h.md#arkui_waterflowlayoutmode)。 |

## NODE\_WATER\_FLOW\_SYNC\_LOAD

```c
NODE_WATER_FLOW_SYNC_LOAD = 1010012
```

WaterFlow组件是否同步加载子节点，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | WaterFlow组件是否同步加载子节点。0：分帧加载，1：同步加载。默认值：1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | WaterFlow组件是否同步加载子节点。0：分帧加载，1：同步加载。 |

## NODE\_WATER\_FLOW\_COLUMN\_TEMPLATE\_ITEMFILLPOLICY

```c
NODE_WATER_FLOW_COLUMN_TEMPLATE_ITEMFILLPOLICY  = 1010013
```

WaterFlow组件的响应式列数布局策略，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 在不同断点规格下的列数，数据类型[ArkUI\_ItemFillPolicy](capi-native-type-h.md#arkui_itemfillpolicy)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 在不同断点规格下的列数，数据类型[ArkUI\_ItemFillPolicy](capi-native-type-h.md#arkui_itemfillpolicy)。 |

## NODE\_WATER\_FLOW\_SUPPORT\_EMPTY\_BRANCH\_IN\_LAZY\_LOADING

```c
NODE_WATER_FLOW_SUPPORT_EMPTY_BRANCH_IN_LAZY_LOADING = 1010014
```

设置当前WaterFlow组件是否支持在LazyForEach或Repeat中使用if/else渲染控制语法生成不包含任何子组件的空分支节点。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**说明** 

当通过[NODE\_WATER\_FLOW\_SECTION\_OPTION](capi-native-node-h-nodeattributetype-scrollablecontainer.md#node_water_flow_section_option)设置了[ArkUI\_WaterFlowSectionOption](capi-arkui-nativemodule-arkui-waterflowsectionoption.md)分组，或通过[NODE\_WATER\_FLOW\_LAYOUT\_MODE](capi-native-node-h-nodeattributetype-scrollablecontainer.md#node_water_flow_layout_mode)设置为[ARKUI\_WATER\_FLOW\_LAYOUT\_MODE\_SLIDING\_WINDOW](capi-water-flow-h.md#arkui_waterflowlayoutmode)布局模式时，设置0或1时空分支后的FlowItem都会显示。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | WaterFlow组件是否支持空分支。0：不支持，1：支持。默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | WaterFlow组件是否支持空分支。0：不支持，1：支持。 |

## NODE\_GRID\_COLUMN\_TEMPLATE

```c
NODE_GRID_COLUMN_TEMPLATE = MAX_NODE_SCOPE_NUM * ARKUI_NODE_GRID = 1013000
```

设置当前Grid组件布局列的数量，不设置时默认1列，支持属性设置、重置和获取。例如，'1fr 1fr 2fr' 是将父组件分3列，将父组件允许的宽分为4等份，第1列占1份，第2列占1份，第3列占2份。可使用[columnsTemplate](ts-container-grid.md#columnstemplate)('repeat(auto-fill,track-size)')根据给定的列宽track-size自动计算列数，其中repeat、auto-fill为关键字，track-size为可设置的宽度，支持的单位包括px、vp、%或有效数字，默认单位为vp。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 布局列的数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 布局列的数量。 |

## NODE\_GRID\_ROW\_TEMPLATE

```c
NODE_GRID_ROW_TEMPLATE = 1013001
```

设置当前Grid布局行的数量或最小行高值，不设置时默认1行，支持属性设置、重置和获取。例如，'1fr 1fr 2fr'是将父组件分3行，将父组件允许的高分为4等份，第1行占1份，第2行占1份，第3行占2份。可使用[rowsTemplate](ts-container-grid.md#rowstemplate)('repeat(auto-fill,track-size)')根据给定的行高track-size自动计算行数，其中repeat、auto-fill为关键字，track-size为可设置的高度，支持的单位包括px、vp、%或有效数字，默认单位为vp。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 布局行的数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 布局行的数量。 |

## NODE\_GRID\_COLUMN\_GAP

```c
NODE_GRID_COLUMN_GAP = 1013002
```

设置列与列的间距，支持属性设置、重置和获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 列与列的间距，默认值：0，单位vp。取值范围：[0, +∞)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 列与列的间距，单位vp。 |

## NODE\_GRID\_ROW\_GAP

```c
NODE_GRID_ROW_GAP = 1013003
```

设置行与行的间距，支持属性设置、重置和获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 行与行的间距，默认值：0，单位vp。取值范围：[0, +∞)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 行与行的间距，单位vp。 |

## NODE\_GRID\_NODE\_ADAPTER

```c
NODE_GRID_NODE_ADAPTER = 1013004
```

[Grid](ts-container-grid.md)组件适配器，支持属性设置，属性重置和属性获取接口。

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

## NODE\_GRID\_CACHED\_COUNT

```c
NODE_GRID_CACHED_COUNT = 1013005
```

[Grid](ts-container-grid.md)组件适配器缓存数量，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 配合Grid组件适配器使用，设置[ArkUI\_NodeAdapter](capi-arkui-nativemodule-arkui-nodeadapter8h.md)的缓存数量。 |
| .value[1].i32 | 是否显示缓存节点，0：不显示缓存节点，1：显示缓存节点。可选参数，默认值：0。从API版本26.0.0开始支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Grid组件适配器的缓存数量。 |
| .value[1].i32 | 是否显示缓存节点，0：不显示，1：显示。该参数从API版本26.0.0开始支持。 |

## NODE\_GRID\_FOCUS\_WRAP\_MODE

```c
NODE_GRID_FOCUS_WRAP_MODE = 1013006
```

[Grid](ts-container-grid.md)组件走焦换行模式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Grid组件走焦换行模式，参数类型[ArkUI\_FocusWrapMode](capi-native-type-h.md#arkui_focuswrapmode)。默认值：[ARKUI\_FOCUS\_WRAP\_MODE\_DEFAULT](capi-native-type-h.md#arkui_focuswrapmode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Grid组件走焦换行模式，参数类型[ArkUI\_FocusWrapMode](capi-native-type-h.md#arkui_focuswrapmode)。 |

## NODE\_GRID\_SYNC\_LOAD

```c
NODE_GRID_SYNC_LOAD = 1013007
```

[Grid](ts-container-grid.md)组件是否同步加载子节点，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Grid组件是否同步加载子节点。0：分帧加载，1：同步加载。默认值：1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Grid组件是否同步加载子节点。0：分帧加载，1：同步加载。 |

## NODE\_GRID\_ALIGN\_ITEMS

```c
NODE_GRID_ALIGN_ITEMS = 1013008
```

设置Grid中[GridItem](ts-container-griditem.md)的对齐方式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Grid中GridItem的对齐方式，参数取值为[ArkUI\_GridItemAlignment](capi-grid-h.md#arkui_griditemalignment)下的枚举，默认值为ARKUI\_GRID\_ITEM\_ALIGNMENT\_DEFAULT。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Grid中GridItem的对齐方式，参数类型[ArkUI\_GridItemAlignment](capi-grid-h.md#arkui_griditemalignment)。 |

## NODE\_GRID\_LAYOUT\_OPTIONS

```c
NODE_GRID_LAYOUT_OPTIONS = 1013009
```

设置Grid布局选项，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 参数格式为[ArkUI\_GridLayoutOptions](capi-arkui-nativemodule-arkui-gridlayoutoptions.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 返回值格式为[ArkUI\_GridLayoutOptions](capi-arkui-nativemodule-arkui-gridlayoutoptions.md)。 |

## NODE\_GRID\_COLUMN\_TEMPLATE\_ITEMFILLPOLICY

```c
NODE_GRID_COLUMN_TEMPLATE_ITEMFILLPOLICY = 1013010
```

Grid组件的响应式列数布局策略，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 在不同断点规格下的列数，数据类型[ArkUI\_ItemFillPolicy](capi-native-type-h.md#arkui_itemfillpolicy)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 在不同断点规格下的列数，数据类型[ArkUI\_ItemFillPolicy](capi-native-type-h.md#arkui_itemfillpolicy)。 |

## NODE\_GRID\_EDIT\_MODE

```c
NODE_GRID_EDIT_MODE = 1013011
```

Grid组件是否进入编辑模式。进入编辑模式后，可以通过NODE\_GRID\_ON\_ITEM\_DRAG\_START事件拖拽GridItem。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Grid组件是否进入编辑模式。0：不可编辑，1：可以编辑。默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Grid组件是否进入编辑模式。0：不可编辑，1：可以编辑。 |

## NODE\_GRID\_DRAG\_ANIMATION

```c
NODE_GRID_DRAG_ANIMATION = 1013012
```

Grid组件是否启用GridItem拖拽动画。支持属性设置，属性重置和属性获取接口。

仅在滚动模式下（只设置NODE\_GRID\_ROW\_TEMPLATE、NODE\_GRID\_COLUMN\_TEMPLATE其中一个）支持动画。

仅在大小规则的Grid中支持拖拽动画，跨行或跨列场景不支持。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Grid组件是否启用GridItem拖拽动画。0：不启用，1：启用。默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Grid组件是否启用GridItem拖拽动画。0：不启用，1：启用。 |

## NODE\_GRID\_MULTI\_SELECTABLE

```c
NODE_GRID_MULTI_SELECTABLE = 1013013
```

Grid组件是否启用鼠标框选。支持属性设置，属性重置和属性获取接口。

启用后在Grid范围内鼠标框选会触发GridItem的[NODE\_GRID\_ITEM\_ON\_SELECT](capi-native-node-h.md#arkui_nodeeventtype)事件。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Grid组件是否启用鼠标框选。0：不启用，1：启用。默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Grid组件是否启用鼠标框选。0：不启用，1：启用。 |

## NODE\_GRID\_SCROLL\_TO\_INDEX

```c
NODE_GRID_SCROLL_TO_INDEX = 1013014
```

滑动到指定index。

开启动效时，会对经过的所有子组件进行加载和布局计算，当大量加载子组件时会导致性能问题。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 要滑动到的目标元素在当前容器中的索引值。 |
| .value[1]?.i32 | 设置滑动到目标元素时是否有动效，1表示有动效，0表示没有动效。默认值：0。 |
| .value[2]?.i32 | 指定滑动到的目标元素与当前容器的对齐方式，参数类型[ArkUI\_ScrollAlignment](capi-scroll-h.md#arkui_scrollalignment)。默认值：ARKUI\_SCROLL\_ALIGNMENT\_AUTO。 |
| .value[3]?.f32 | 滑动到目标元素后的额外偏移量，默认值：0，单位：vp。如果值为正数，则向底部额外偏移；如果值为负数，则向顶部额外偏移。 |

## NODE\_GRID\_SUPPORT\_EMPTY\_BRANCH\_IN\_LAZY\_LOADING

```c
NODE_GRID_SUPPORT_EMPTY_BRANCH_IN_LAZY_LOADING = 1013015
```

设置当前Grid组件是否支持在LazyForEach或Repeat中使用if/else渲染控制语法生成不包含任何子组件的空分支节点。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Grid组件是否支持空分支。0：不支持，1：支持。默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Grid组件是否支持空分支。0：不支持，1：支持。 |

## NODE\_GRID\_ENABLE\_EDIT\_MODE

```c
NODE_GRID_ENABLE_EDIT_MODE = 1013016
```

设置Grid组件是否启用编辑模式。进入编辑模式后，默认显示复选框，并支持手指滑动多选。支持属性设置、属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Grid组件是否启用编辑模式。0：不启用，1：启用。默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Grid组件是否启用编辑模式。0：未启用，1：已启用。 |

## NODE\_GRID\_EDIT\_MODE\_OPTIONS

```c
NODE_GRID_EDIT_MODE_OPTIONS = 1013017
```

设置Grid组件的编辑模式选项，支持属性设置、属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Grid组件是否使用默认多选样式。0：不使用，1：使用。默认值：1。 |
| .value[1].i32 | Grid组件是否启用双指滑动多选。0：不启用，1：启用。默认值：1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Grid组件是否使用默认多选样式。0：不使用，1：使用。 |
| .value[1].i32 | Grid组件是否启用双指滑动多选。0：未启用，1：已启用。 |

## NODE\_GRID\_ITEM\_STYLE

```c
NODE_GRID_ITEM_STYLE = MAX_NODE_SCOPE_NUM * ARKUI_NODE_GRID_ITEM = 1014000
```

设置GridItem样式，支持属性设置，属性重置和属性获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | GridItem样式，参数取值为[ArkUI\_GridItemStyle](capi-grid-h.md#arkui_griditemstyle)下的枚举，默认值为ARKUI\_GRID\_ITEM\_STYLE\_NONE。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | GridItem样式，参数类型[ArkUI\_GridItemStyle](capi-grid-h.md#arkui_griditemstyle)。 |

## NODE\_GRID\_ITEM\_SELECTABLE

```c
NODE_GRID_ITEM_SELECTABLE = 1014001
```

设置GridItem是否可以被鼠标框选。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | GridItem是否可以被鼠标框选。0：不可以，1：可以。默认值：1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | GridItem是否可以被鼠标框选。0：不可以，1：可以。 |

## NODE\_GRID\_ITEM\_SELECTED

```c
NODE_GRID_ITEM_SELECTED = 1014002
```

设置GridItem选中状态。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | GridItem选中状态。0：未选中，1：已选中。默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | GridItem选中状态。0：未选中，1：已选中。 |

## NODE\_ARC\_LIST\_DIGITAL\_CROWN\_SENSITIVITY

```c
NODE_ARC_LIST_DIGITAL_CROWN_SENSITIVITY = MAX_NODE_SCOPE_NUM * ARKUI_NODE_ARC_LIST = 1019000
```

设置ArcList组件表冠灵敏度，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表冠灵敏度类型，数据类型[ArkUI\_CrownSensitivity](capi-native-type-h.md#arkui_crownsensitivity)，默认值为[ARKUI\_CROWN\_SENSITIVITY\_MEDIUM](capi-native-type-h.md#arkui_crownsensitivity)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表冠灵敏度类型，数据类型[ArkUI\_CrownSensitivity](capi-native-type-h.md#arkui_crownsensitivity)。 |

## NODE\_ARC\_LIST\_SPACE

```c
NODE_ARC_LIST_SPACE = 1019001
```

设置ArcList子组件主轴方向的间隔，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 子组件主轴方向的间隔，单位为vp，默认值0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 子组件主轴方向的间隔，单位：vp。 |

## NODE\_ARC\_LIST\_CACHED\_COUNT

```c
NODE_ARC_LIST_CACHED_COUNT = 1019002
```

设置ArcList组件缓存数量，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 缓存数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 缓存数量。 |

## NODE\_ARC\_LIST\_SCROLL\_TO\_INDEX

```c
NODE_ARC_LIST_SCROLL_TO_INDEX = 1019003
```

滑动到指定索引值对应的列表项。开启动效时，会对经过的所有列表项进行加载和布局计算，当大量加载列表项时会导致性能问题。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 要滑动到的目标元素在当前容器中的索引值。传入-1时，指滑动到当前容器的最后一个元素。 |
| .value[1]?.i32 | 设置滑动到指定索引值对应的列表项时是否有动效，1表示有动效，0表示没有动效。默认值：0。 |
| .value[2]?.i32 | 指定滑动到的列表项与当前容器的对齐方式，参数类型[ArkUI\_ScrollAlignment](capi-scroll-h.md#arkui_scrollalignment)，默认值：[ARKUI\_SCROLL\_ALIGNMENT\_START](capi-scroll-h.md#arkui_scrollalignment)。 |
| .value[3]?.f32 | 额外偏移量，默认值：0，单位：vp。正数表示向末尾端额外偏移，负数表示向起始端额外偏移。 |

## NODE\_ARC\_LIST\_CHAIN\_ANIMATION

```c
NODE_ARC_LIST_CHAIN_ANIMATION = 1019004
```

设置ArcList是否启用链式联动动效，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否启用链式联动动效，0：不启用，1：启用，默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否启用链式联动动效。0：不启用，1：启用。 |

## NODE\_ARC\_LIST\_CHILDREN\_MAIN\_SIZE

```c
NODE_ARC_LIST_CHILDREN_MAIN_SIZE = 1019005
```

设置ArcList子组件默认主轴尺寸，支持属性设置和属性重置接口。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 参数格式为[ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)。定义ArcList的所有子项主轴尺寸信息的结构体。  通过[OH\_ArkUI\_ListChildrenMainSizeOption\_Create](capi-list-h.md#oh_arkui_listchildrenmainsizeoption_create)接口来创建，并且可以使用[OH\_ArkUI\_ListChildrenMainSizeOption\_Splice](capi-list-h.md#oh_arkui_listchildrenmainsizeoption_splice)方法对ArcList组件子项主轴尺寸数组进行大小调整。 |

## NODE\_ARC\_LIST\_SET\_HEADER

```c
NODE_ARC_LIST_SET_HEADER = 1019006
```

设置ArcList头部组件，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 使用[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)对象作为ArcList头部组件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 使用[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)对象作为ArcList头部组件。 |

## NODE\_ARC\_LIST\_SCROLL\_BAR

```c
NODE_ARC_LIST_SCROLL_BAR = 1019007
```

设置ArcList组件的滚动条状态，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 滚动条状态，数据类型[ArkUI\_ScrollBarDisplayMode](capi-scroll-h.md#arkui_scrollbardisplaymode)，默认值为[ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_AUTO](capi-scroll-h.md#arkui_scrollbardisplaymode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 滚动条状态，数据类型[ArkUI\_ScrollBarDisplayMode](capi-scroll-h.md#arkui_scrollbardisplaymode)。 |

## NODE\_ARC\_LIST\_SCROLL\_BAR\_COLOR

```c
NODE_ARC_LIST_SCROLL_BAR_COLOR = 1019008
```

设置ArcList组件滚动条的颜色，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .data[0].u32 | 滚动条颜色，0xargb类型。默认值：0x66182431。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .data[0].u32 | 滚动条颜色，0xargb类型。 |

## NODE\_ARC\_LIST\_SCROLL\_BAR\_WIDTH

```c
NODE_ARC_LIST_SCROLL_BAR_WIDTH = 1019009
```

设置ArcList组件滚动条的宽度，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 滚动条宽度，单位vp，默认值4。  取值范围：[0, +∞)。设置为小于0的值时，按默认值处理。设置为0时，不显示滚动条。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 滚动条宽度，单位vp。 |

## NODE\_ARC\_LIST\_ENABLE\_SCROLL\_INTERACTION

```c
NODE_ARC_LIST_ENABLE_SCROLL_INTERACTION = 1019010
```

设置ArcList是否支持滚动手势，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否支持滚动手势，默认值1。1：支持滚动手势，0：不支持滚动手势。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否支持滚动手势。1：支持滚动手势，0：不支持滚动手势。 |

## NODE\_ARC\_LIST\_FADING\_EDGE

```c
NODE_ARC_LIST_FADING_EDGE = 1019011
```

设置ArcList边缘渐隐效果，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否使能边缘渐隐效果。0表示关闭边缘效果，1表示开启边缘效果。默认值：0。 |
| .value[1]?.f32 | 边缘渐隐效果长度。单位：vp，默认值：32。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否使能边缘渐隐效果。0表示关闭边缘效果，1表示开启边缘效果。 |
| .value[1].f32 | 边缘渐隐效果长度。单位：vp。 |

## NODE\_ARC\_LIST\_FRICTION

```c
NODE_ARC_LIST_FRICTION = 1019012
```

设置ArcList摩擦系数，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 摩擦系数，默认值：0.8。取值范围：(0, +∞)，设置为小于等于0的值时，按默认值处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 摩擦系数。 |

## NODE\_ARC\_LIST\_FLING\_SPEED\_LIMIT

```c
NODE_ARC_LIST_FLING_SPEED_LIMIT = 1019013
```

设置ArcList限制Fling动效最大初始速度，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | Fling动效开始时的最大初始速度，单位：vp/s。默认值：9000。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | Fling动效开始时的最大初始速度，单位：vp/s。 |

## NODE\_ARC\_LIST\_ITEM\_AUTO\_SCALE

```c
NODE_ARC_LIST_ITEM_AUTO_SCALE = MAX_NODE_SCOPE_NUM * ARKUI_NODE_ARC_LIST_ITEM = 1020000
```

设置ArcListItem是否启用自动缩放，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否启用自动缩放，0：不启用，1：启用，默认值：1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否启用自动缩放。0：不启用，1：启用。 |

## NODE\_ARC\_LIST\_ITEM\_SWIPE\_ACTION

```c
NODE_ARC_LIST_ITEM_SWIPE_ACTION = 1020001
```

设置ArcListItem的划出组件，支持属性设置和属性重置接口。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 使用[ArkUI\_ListItemSwipeActionOption](capi-arkui-nativemodule-arkui-listitemswipeactionoption.md)对象构造。  定义ArcListItem的划出组件信息的结构体。通过[OH\_ArkUI\_ListItemSwipeActionOption\_Create](capi-native-type-h.md#oh_arkui_listitemswipeactionoption_create)接口来创建，并且可以使用[OH\_ArkUI\_ListItemSwipeActionOption\_SetStart](capi-native-type-h.md#oh_arkui_listitemswipeactionoption_setstart)方法设置ListItemSwipeActionItem左侧（垂直布局）或上方（横向布局）内容。 |

## NODE\_ARC\_SCROLL\_BAR\_BIND\_SCROLLABLE

```c
NODE_ARC_SCROLL_BAR_BIND_SCROLLABLE = MAX_NODE_SCOPE_NUM * ARKUI_NODE_ARC_SCROLL_BAR = 1021000
```

设置ArcScrollBar绑定的可滚动组件，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 使用[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)对象作为滚动条绑定的可滚动组件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 使用[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)对象作为滚动条绑定的可滚动组件。 |

## NODE\_ARC\_SCROLL\_BAR\_DISPLAY\_MODE

```c
NODE_ARC_SCROLL_BAR_DISPLAY_MODE = 1021001
```

设置ArcScrollBar滚动条状态，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 滚动条状态，数据类型[ArkUI\_ScrollBarDisplayMode](capi-scroll-h.md#arkui_scrollbardisplaymode)，默认值为ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_AUTO。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 滚动条状态，数据类型[ArkUI\_ScrollBarDisplayMode](capi-scroll-h.md#arkui_scrollbardisplaymode)。 |
