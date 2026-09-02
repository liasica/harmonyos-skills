---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-swiper-h
title: swiper.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > swiper.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d3ea22563c5180d38a8b913b1a9605e29a4dc39fdbd83135b568845a1cf42ca6
---

## 概述

定义Swiper组件的枚举和接口。

**引用文件：** <arkui/node\_attributes/swiper.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [NDKSwiperSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NDKSwiperSample)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md) | ArkUI\_SwiperIndicator | 定义Swiper组件的导航指示器风格。 |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md) | ArkUI\_SwiperDigitIndicator | 定义Swiper组件的数字导航指示器风格。 |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md) | ArkUI\_SwiperArrowStyle | 定义Swiper组件的导航箭头风格。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_SwiperArrow](capi-swiper-h.md#arkui_swiperarrow) | ArkUI\_SwiperArrow | Swiper导航点箭头枚举值。 |
| [ArkUI\_SwiperNestedScrollMode](capi-swiper-h.md#arkui_swipernestedscrollmode) | ArkUI\_SwiperNestedScrollMode | Swiper组件和父组件的嵌套滚动模式。 |
| [ArkUI\_PageFlipMode](capi-swiper-h.md#arkui_pageflipmode) | ArkUI\_PageFlipMode | Swiper组件鼠标滚轮翻页模式。 |
| [ArkUI\_SwiperAnimationMode](capi-swiper-h.md#arkui_swiperanimationmode) | ArkUI\_SwiperAnimationMode | Swiper组件跳转到目标index的动画模式。 |
| [ArkUI\_SwiperIndicatorType](capi-swiper-h.md#arkui_swiperindicatortype) | ArkUI\_SwiperIndicatorType | 定义Swiper组件的导航指示器类型。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator\* OH\_ArkUI\_SwiperIndicator\_Create(ArkUI\_SwiperIndicatorType type)](capi-swiper-h.md#oh_arkui_swiperindicator_create) | 创建Swiper组件的导航指示器。 |
| [void OH\_ArkUI\_SwiperIndicator\_Dispose(ArkUI\_SwiperIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperindicator_dispose) | 销毁Swiper组件的导航指示器指针。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetStartPosition(ArkUI\_SwiperIndicator\* indicator, float value)](capi-swiper-h.md#oh_arkui_swiperindicator_setstartposition) | 设置导航点距离Swiper组件左边的距离。 |
| [float OH\_ArkUI\_SwiperIndicator\_GetStartPosition(ArkUI\_SwiperIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperindicator_getstartposition) | 获取导航点距离Swiper组件左边的距离。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetTopPosition(ArkUI\_SwiperIndicator\* indicator, float value)](capi-swiper-h.md#oh_arkui_swiperindicator_settopposition) | 设置导航点距离Swiper组件顶部的距离。 |
| [float OH\_ArkUI\_SwiperIndicator\_GetTopPosition(ArkUI\_SwiperIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperindicator_gettopposition) | 获取导航点距离Swiper组件顶部的距离。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetEndPosition(ArkUI\_SwiperIndicator\* indicator, float value)](capi-swiper-h.md#oh_arkui_swiperindicator_setendposition) | 设置导航点距离Swiper组件右边的距离。 |
| [float OH\_ArkUI\_SwiperIndicator\_GetEndPosition(ArkUI\_SwiperIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperindicator_getendposition) | 获取导航点距离Swiper组件右边的距离。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetBottomPosition(ArkUI\_SwiperIndicator\* indicator, float value)](capi-swiper-h.md#oh_arkui_swiperindicator_setbottomposition) | 设置导航点距离Swiper组件底部的距离。 |
| [float OH\_ArkUI\_SwiperIndicator\_GetBottomPosition(ArkUI\_SwiperIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperindicator_getbottomposition) | 获取导航点距离Swiper组件底部的距离。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetIgnoreSizeOfBottom(ArkUI\_SwiperIndicator\* indicator, int32\_t ignoreSize)](capi-swiper-h.md#oh_arkui_swiperindicator_setignoresizeofbottom) | 设置OH\_ArkUI\_SwiperIndicator\_SetBottomPosition是否忽略导航点大小。 |
| [int32\_t OH\_ArkUI\_SwiperIndicator\_GetIgnoreSizeOfBottom(ArkUI\_SwiperIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperindicator_getignoresizeofbottom) | 获取OH\_ArkUI\_SwiperIndicator\_SetBottomPosition是否忽略导航点大小。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetItemWidth(ArkUI\_SwiperIndicator\* indicator, float value)](capi-swiper-h.md#oh_arkui_swiperindicator_setitemwidth) | 设置Swiper组件圆点导航指示器的宽。 |
| [float OH\_ArkUI\_SwiperIndicator\_GetItemWidth(ArkUI\_SwiperIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperindicator_getitemwidth) | 获取Swiper组件圆点导航指示器的宽。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetItemHeight(ArkUI\_SwiperIndicator\* indicator, float value)](capi-swiper-h.md#oh_arkui_swiperindicator_setitemheight) | 设置Swiper组件圆点导航指示器的高。 |
| [float OH\_ArkUI\_SwiperIndicator\_GetItemHeight(ArkUI\_SwiperIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperindicator_getitemheight) | 获取Swiper组件圆点导航指示器的高。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetSelectedItemWidth(ArkUI\_SwiperIndicator\* indicator, float value)](capi-swiper-h.md#oh_arkui_swiperindicator_setselecteditemwidth) | 设置被选中的Swiper组件圆点导航指示器的宽。 |
| [float OH\_ArkUI\_SwiperIndicator\_GetSelectedItemWidth(ArkUI\_SwiperIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperindicator_getselecteditemwidth) | 获取被选中Swiper组件圆点导航指示器的宽。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetSelectedItemHeight(ArkUI\_SwiperIndicator\* indicator, float value)](capi-swiper-h.md#oh_arkui_swiperindicator_setselecteditemheight) | 设置被选中的Swiper组件圆点导航指示器的高。 |
| [float OH\_ArkUI\_SwiperIndicator\_GetSelectedItemHeight(ArkUI\_SwiperIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperindicator_getselecteditemheight) | 获取被选中Swiper组件圆点导航指示器的高。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetMask(ArkUI\_SwiperIndicator\* indicator, int32\_t mask)](capi-swiper-h.md#oh_arkui_swiperindicator_setmask) | 设置是否显示Swiper组件圆点导航指示器的蒙版样式。 |
| [int32\_t OH\_ArkUI\_SwiperIndicator\_GetMask(ArkUI\_SwiperIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperindicator_getmask) | 获取是否显示Swiper组件圆点导航指示器的蒙版样式。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetColor(ArkUI\_SwiperIndicator\* indicator, uint32\_t color)](capi-swiper-h.md#oh_arkui_swiperindicator_setcolor) | 设置Swiper组件圆点导航指示器的颜色。 |
| [uint32\_t OH\_ArkUI\_SwiperIndicator\_GetColor(ArkUI\_SwiperIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperindicator_getcolor) | 获取Swiper组件圆点导航指示器的颜色。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetSelectedColor(ArkUI\_SwiperIndicator\* indicator, uint32\_t selectedColor)](capi-swiper-h.md#oh_arkui_swiperindicator_setselectedcolor) | 设置被选中Swiper组件圆点导航指示器的颜色。 |
| [uint32\_t OH\_ArkUI\_SwiperIndicator\_GetSelectedColor(ArkUI\_SwiperIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperindicator_getselectedcolor) | 获取被选中Swiper组件圆点导航指示器的颜色。 |
| [int32\_t OH\_ArkUI\_SwiperIndicator\_SetMaxDisplayCount(ArkUI\_SwiperIndicator\* indicator, int32\_t maxDisplayCount)](capi-swiper-h.md#oh_arkui_swiperindicator_setmaxdisplaycount) | 设置圆点导航点指示器样式下，导航点显示个数的最大值。 |
| [int32\_t OH\_ArkUI\_SwiperIndicator\_GetMaxDisplayCount(ArkUI\_SwiperIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperindicator_getmaxdisplaycount) | 获取圆点导航点指示器样式下，导航点显示个数的最大值。 |
| [ArkUI\_SwiperDigitIndicator \*OH\_ArkUI\_SwiperDigitIndicator\_Create()](capi-swiper-h.md#oh_arkui_swiperdigitindicator_create) | 创建Swiper组件的数字导航指示器。 |
| [void OH\_ArkUI\_SwiperDigitIndicator\_Destroy(ArkUI\_SwiperDigitIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperdigitindicator_destroy) | 销毁Swiper组件的数字导航指示器指针。 |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetStartPosition(ArkUI\_SwiperDigitIndicator\* indicator, float value)](capi-swiper-h.md#oh_arkui_swiperdigitindicator_setstartposition) | 设置数字导航指示器距离Swiper组件左边的距离，在从右至左显示的语言模式下，设置其距离Swiper组件右边的距离。 |
| [float OH\_ArkUI\_SwiperDigitIndicator\_GetStartPosition(ArkUI\_SwiperDigitIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperdigitindicator_getstartposition) | 获取数字导航指示器距离Swiper组件左边的距离，在从右至左显示的语言模式下，获取其距离Swiper组件右边的距离。 |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetTopPosition(ArkUI\_SwiperDigitIndicator\* indicator, float value)](capi-swiper-h.md#oh_arkui_swiperdigitindicator_settopposition) | 设置数字导航指示器距离Swiper组件顶部的距离。 |
| [float OH\_ArkUI\_SwiperDigitIndicator\_GetTopPosition(ArkUI\_SwiperDigitIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperdigitindicator_gettopposition) | 获取数字导航指示器距离Swiper组件顶部的距离。 |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetEndPosition(ArkUI\_SwiperDigitIndicator\* indicator, float value)](capi-swiper-h.md#oh_arkui_swiperdigitindicator_setendposition) | 设置数字导航指示器距离Swiper组件右边的距离，在从右至左显示的语言模式下，设置其距离Swiper组件左边的距离。 |
| [float OH\_ArkUI\_SwiperDigitIndicator\_GetEndPosition(ArkUI\_SwiperDigitIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperdigitindicator_getendposition) | 获取数字导航指示器距离Swiper组件右边的距离，在从右至左显示的语言模式下，获取其距离Swiper组件左边的距离。 |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetBottomPosition(ArkUI\_SwiperDigitIndicator\* indicator, float value)](capi-swiper-h.md#oh_arkui_swiperdigitindicator_setbottomposition) | 设置数字导航指示器距离Swiper组件底部的距离。 |
| [float OH\_ArkUI\_SwiperDigitIndicator\_GetBottomPosition(ArkUI\_SwiperDigitIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperdigitindicator_getbottomposition) | 获取数字导航指示器距离Swiper组件底部的距离。 |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetFontColor(ArkUI\_SwiperDigitIndicator\* indicator, uint32\_t color)](capi-swiper-h.md#oh_arkui_swiperdigitindicator_setfontcolor) | 设置Swiper组件数字导航指示器字体颜色。 |
| [uint32\_t OH\_ArkUI\_SwiperDigitIndicator\_GetFontColor(ArkUI\_SwiperDigitIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperdigitindicator_getfontcolor) | 获取Swiper组件数字导航指示器字体颜色。 |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetSelectedFontColor(ArkUI\_SwiperDigitIndicator\* indicator, uint32\_t selectedColor)](capi-swiper-h.md#oh_arkui_swiperdigitindicator_setselectedfontcolor) | 设置被选中Swiper组件数字导航指示器字体颜色。 |
| [uint32\_t OH\_ArkUI\_SwiperDigitIndicator\_GetSelectedFontColor(ArkUI\_SwiperDigitIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperdigitindicator_getselectedfontcolor) | 获取被选中Swiper组件数字导航指示器字体颜色。 |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetFontSize(ArkUI\_SwiperDigitIndicator\* indicator, float size)](capi-swiper-h.md#oh_arkui_swiperdigitindicator_setfontsize) | 设置Swiper组件数字导航指示器字体大小。 |
| [float OH\_ArkUI\_SwiperDigitIndicator\_GetFontSize(ArkUI\_SwiperDigitIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperdigitindicator_getfontsize) | 获取Swiper组件数字导航指示器字体大小。 |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetSelectedFontSize(ArkUI\_SwiperDigitIndicator\* indicator, float size)](capi-swiper-h.md#oh_arkui_swiperdigitindicator_setselectedfontsize) | 设置被选中Swiper组件数字导航指示器字体大小。 |
| [float OH\_ArkUI\_SwiperDigitIndicator\_GetSelectedFontSize(ArkUI\_SwiperDigitIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperdigitindicator_getselectedfontsize) | 获取被选中Swiper组件数字导航指示器字体大小。 |
| [ArkUI\_SwiperArrowStyle \*OH\_ArkUI\_SwiperArrowStyle\_Create()](capi-swiper-h.md#oh_arkui_swiperarrowstyle_create) | 创建Swiper组件的导航箭头。 |
| [void OH\_ArkUI\_SwiperArrowStyle\_Destroy(ArkUI\_SwiperArrowStyle\* arrowStyle)](capi-swiper-h.md#oh_arkui_swiperarrowstyle_destroy) | 销毁Swiper组件的导航箭头指针。 |
| [void OH\_ArkUI\_SwiperArrowStyle\_SetShowBackground(ArkUI\_SwiperArrowStyle\* arrowStyle, int32\_t showBackground)](capi-swiper-h.md#oh_arkui_swiperarrowstyle_setshowbackground) | 设置Swiper组件导航箭头底板是否显示。 |
| [int32\_t OH\_ArkUI\_SwiperArrowStyle\_GetShowBackground(ArkUI\_SwiperArrowStyle\* arrowStyle)](capi-swiper-h.md#oh_arkui_swiperarrowstyle_getshowbackground) | 获取Swiper组件导航箭头底板是否显示。 |
| [void OH\_ArkUI\_SwiperArrowStyle\_SetShowSidebarMiddle(ArkUI\_SwiperArrowStyle\* arrowStyle, int32\_t showSidebarMiddle)](capi-swiper-h.md#oh_arkui_swiperarrowstyle_setshowsidebarmiddle) | 设置Swiper组件导航箭头显示位置。 |
| [int32\_t OH\_ArkUI\_SwiperArrowStyle\_GetShowSidebarMiddle(ArkUI\_SwiperArrowStyle\* arrowStyle)](capi-swiper-h.md#oh_arkui_swiperarrowstyle_getshowsidebarmiddle) | 获取Swiper组件导航箭头显示位置。 |
| [void OH\_ArkUI\_SwiperArrowStyle\_SetBackgroundSize(ArkUI\_SwiperArrowStyle\* arrowStyle, float backgroundSize)](capi-swiper-h.md#oh_arkui_swiperarrowstyle_setbackgroundsize) | 设置Swiper组件导航箭头底板大小。 |
| [float OH\_ArkUI\_SwiperArrowStyle\_GetBackgroundSize(ArkUI\_SwiperArrowStyle\* arrowStyle)](capi-swiper-h.md#oh_arkui_swiperarrowstyle_getbackgroundsize) | 获取Swiper组件导航箭头底板大小。 |
| [void OH\_ArkUI\_SwiperArrowStyle\_SetBackgroundColor(ArkUI\_SwiperArrowStyle\* arrowStyle, uint32\_t backgroundColor)](capi-swiper-h.md#oh_arkui_swiperarrowstyle_setbackgroundcolor) | 设置Swiper组件导航箭头底板颜色。 |
| [uint32\_t OH\_ArkUI\_SwiperArrowStyle\_GetBackgroundColor(ArkUI\_SwiperArrowStyle\* arrowStyle)](capi-swiper-h.md#oh_arkui_swiperarrowstyle_getbackgroundcolor) | 获取Swiper组件导航箭头底板颜色。 |
| [void OH\_ArkUI\_SwiperArrowStyle\_SetArrowSize(ArkUI\_SwiperArrowStyle\* arrowStyle, float arrowSize)](capi-swiper-h.md#oh_arkui_swiperarrowstyle_setarrowsize) | 设置Swiper组件导航箭头大小。 |
| [float OH\_ArkUI\_SwiperArrowStyle\_GetArrowSize(ArkUI\_SwiperArrowStyle\* arrowStyle)](capi-swiper-h.md#oh_arkui_swiperarrowstyle_getarrowsize) | 获取Swiper组件导航箭头大小。 |
| [void OH\_ArkUI\_SwiperArrowStyle\_SetArrowColor(ArkUI\_SwiperArrowStyle\* arrowStyle, uint32\_t arrowColor)](capi-swiper-h.md#oh_arkui_swiperarrowstyle_setarrowcolor) | 设置Swiper组件导航箭头颜色。 |
| [uint32\_t OH\_ArkUI\_SwiperArrowStyle\_GetArrowColor(ArkUI\_SwiperArrowStyle\* arrowStyle)](capi-swiper-h.md#oh_arkui_swiperarrowstyle_getarrowcolor) | 获取Swiper组件导航箭头颜色。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetSpace(ArkUI\_SwiperIndicator\* indicator, float space)](capi-swiper-h.md#oh_arkui_swiperindicator_setspace) | 设置导航点间距。 |
| [float OH\_ArkUI\_SwiperIndicator\_GetSpace(ArkUI\_SwiperIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperindicator_getspace) | 获取导航点间距。 |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetIgnoreSizeOfBottom(ArkUI\_SwiperDigitIndicator\* indicator, int32\_t ignoreSize)](capi-swiper-h.md#oh_arkui_swiperdigitindicator_setignoresizeofbottom) | 设置OH\_ArkUI\_SwiperDigitIndicator\_SetBottomPosition是否忽略导航点大小。 |
| [int32\_t OH\_ArkUI\_SwiperDigitIndicator\_GetIgnoreSizeOfBottom(ArkUI\_SwiperDigitIndicator\* indicator)](capi-swiper-h.md#oh_arkui_swiperdigitindicator_getignoresizeofbottom) | 获取OH\_ArkUI\_SwiperDigitIndicator\_SetBottomPosition是否忽略导航点大小。 |

## 枚举类型说明

### ArkUI\_SwiperArrow

```c
enum ArkUI_SwiperArrow
```

**描述**

Swiper导航点箭头枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SWIPER\_ARROW\_HIDE = 0 | 不显示swiper中导航点箭头。 |
| ARKUI\_SWIPER\_ARROW\_SHOW | 显示swiper中导航点箭头。 |
| ARKUI\_SWIPER\_ARROW\_SHOW\_ON\_HOVER | 在hover状态下显示swiper中导航点箭头。 |

### ArkUI\_SwiperNestedScrollMode

```c
enum ArkUI_SwiperNestedScrollMode
```

**描述**

Swiper组件和父组件的嵌套滚动模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SWIPER\_NESTED\_SRCOLL\_SELF\_ONLY = 0 | Swiper只自身滚动，不与父组件联动。 |
| ARKUI\_SWIPER\_NESTED\_SRCOLL\_SELF\_FIRST | Swiper自身先滚动，自身滚动到边缘以后父组件滚动。父组件滚动到边缘以后，如果父组件有边缘效果，则父组件触发边缘效果，否则Swiper触发边缘效果。 |

### ArkUI\_PageFlipMode

```c
enum ArkUI_PageFlipMode
```

**描述**

Swiper组件鼠标滚轮翻页模式。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_PAGE\_FLIP\_MODE\_CONTINUOUS = 0 | 鼠标滚轮连续滚动时翻多页，根据鼠标事件上报次数确定。 |
| ARKUI\_PAGE\_FLIP\_MODE\_SINGLE | 一次翻页动画结束前不响应其他鼠标滚轮事件。 |

### ArkUI\_SwiperAnimationMode

```c
enum ArkUI_SwiperAnimationMode
```

**描述**

Swiper组件跳转到目标index的动画模式。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SWIPER\_NO\_ANIMATION = 0 | 无动画跳转到目标index。 |
| ARKUI\_SWIPER\_DEFAULT\_ANIMATION = 1 | 做动画跳转到目标index。 |
| ARKUI\_SWIPER\_FAST\_ANIMATION = 2 | 先无动画跳转到目标附近再做动画跳转到目标index。 |

### ArkUI\_SwiperIndicatorType

```c
enum ArkUI_SwiperIndicatorType
```

**描述**

定义Swiper组件的导航指示器类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SWIPER\_INDICATOR\_TYPE\_DOT | 圆点指示器类型。 |
| ARKUI\_SWIPER\_INDICATOR\_TYPE\_DIGIT | 数字指示器类型。 |

## 函数说明

### OH\_ArkUI\_SwiperIndicator\_Create()

```c
ArkUI_SwiperIndicator* OH_ArkUI_SwiperIndicator_Create(ArkUI_SwiperIndicatorType type)
```

**描述**

创建Swiper组件的导航指示器。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicatorType](capi-swiper-h.md#arkui_swiperindicatortype) type | 导航指示器的类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_SwiperIndicator\*](capi-arkui-nativemodule-arkui-swiperindicator.md) | 导航指示器对象指针。 |

### OH\_ArkUI\_SwiperIndicator\_Dispose()

```c
void OH_ArkUI_SwiperIndicator_Dispose(ArkUI_SwiperIndicator* indicator)
```

**描述**

销毁Swiper组件的导航指示器指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

### OH\_ArkUI\_SwiperIndicator\_SetStartPosition()

```c
void OH_ArkUI_SwiperIndicator_SetStartPosition(ArkUI_SwiperIndicator* indicator, float value)
```

**描述**

设置导航点距离Swiper组件左边的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| float value | 导航点距离Swiper组件左边的距离。默认值：0，单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_GetStartPosition()

```c
float OH_ArkUI_SwiperIndicator_GetStartPosition(ArkUI_SwiperIndicator* indicator)
```

**描述**

获取导航点距离Swiper组件左边的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 导航点距离Swiper组件左边的距离。单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_SetTopPosition()

```c
void OH_ArkUI_SwiperIndicator_SetTopPosition(ArkUI_SwiperIndicator* indicator, float value)
```

**描述**

设置导航点距离Swiper组件顶部的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| float value | 导航点距离Swiper组件顶部的距离。默认值：0，单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_GetTopPosition()

```c
float OH_ArkUI_SwiperIndicator_GetTopPosition(ArkUI_SwiperIndicator* indicator)
```

**描述**

获取导航点距离Swiper组件顶部的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 导航点距离Swiper组件顶部的距离。单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_SetEndPosition()

```c
void OH_ArkUI_SwiperIndicator_SetEndPosition(ArkUI_SwiperIndicator* indicator, float value)
```

**描述**

设置导航点距离Swiper组件右边的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| float value | 导航点距离Swiper组件右边的距离。默认值：0，单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_GetEndPosition()

```c
float OH_ArkUI_SwiperIndicator_GetEndPosition(ArkUI_SwiperIndicator* indicator)
```

**描述**

获取导航点距离Swiper组件右边的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 导航点距离Swiper组件右边的距离。单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_SetBottomPosition()

```c
void OH_ArkUI_SwiperIndicator_SetBottomPosition(ArkUI_SwiperIndicator* indicator, float value)
```

**描述**

设置导航点距离Swiper组件底部的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| float value | 导航点距离Swiper组件底部的距离。默认值：0，单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_GetBottomPosition()

```c
float OH_ArkUI_SwiperIndicator_GetBottomPosition(ArkUI_SwiperIndicator* indicator)
```

**描述**

获取导航点距离Swiper组件底部的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 导航点距离Swiper组件底部的距离。单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_SetIgnoreSizeOfBottom()

```c
void OH_ArkUI_SwiperIndicator_SetIgnoreSizeOfBottom(ArkUI_SwiperIndicator* indicator, int32_t ignoreSize)
```

**描述**

设置OH\_ArkUI\_SwiperIndicator\_SetBottomPosition是否忽略导航点大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| int32\_t ignoreSize | 是否忽略导航点大小。1表示忽略导航点大小，0表示不忽略，默认值0。 |

### OH\_ArkUI\_SwiperIndicator\_GetIgnoreSizeOfBottom()

```c
int32_t OH_ArkUI_SwiperIndicator_GetIgnoreSizeOfBottom(ArkUI_SwiperIndicator* indicator)
```

**描述**

获取OH\_ArkUI\_SwiperIndicator\_SetBottomPosition是否忽略导航点大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 是否忽略导航点大小。 |

### OH\_ArkUI\_SwiperIndicator\_SetItemWidth()

```c
void OH_ArkUI_SwiperIndicator_SetItemWidth(ArkUI_SwiperIndicator* indicator, float value)
```

**描述**

设置Swiper组件圆点导航指示器的宽。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| float value | 圆点导航指示器的宽。默认值：12，单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_GetItemWidth()

```c
float OH_ArkUI_SwiperIndicator_GetItemWidth(ArkUI_SwiperIndicator* indicator)
```

**描述**

获取Swiper组件圆点导航指示器的宽。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 圆点导航指示器的宽。单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_SetItemHeight()

```c
void OH_ArkUI_SwiperIndicator_SetItemHeight(ArkUI_SwiperIndicator* indicator, float value)
```

**描述**

设置Swiper组件圆点导航指示器的高。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| float value | 圆点导航指示器的高。默认值：6，单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_GetItemHeight()

```c
float OH_ArkUI_SwiperIndicator_GetItemHeight(ArkUI_SwiperIndicator* indicator)
```

**描述**

获取Swiper组件圆点导航指示器的高。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 圆点导航指示器的高。单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_SetSelectedItemWidth()

```c
void OH_ArkUI_SwiperIndicator_SetSelectedItemWidth(ArkUI_SwiperIndicator* indicator, float value)
```

**描述**

设置被选中的Swiper组件圆点导航指示器的宽。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| float value | 圆点导航指示器的宽。默认值：12，单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_GetSelectedItemWidth()

```c
float OH_ArkUI_SwiperIndicator_GetSelectedItemWidth(ArkUI_SwiperIndicator* indicator)
```

**描述**

获取被选中Swiper组件圆点导航指示器的宽。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 圆点导航指示器的宽。单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_SetSelectedItemHeight()

```c
void OH_ArkUI_SwiperIndicator_SetSelectedItemHeight(ArkUI_SwiperIndicator* indicator, float value)
```

**描述**

设置被选中的Swiper组件圆点导航指示器的高。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| float value | 圆点导航指示器的高。默认值：6，单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_GetSelectedItemHeight()

```c
float OH_ArkUI_SwiperIndicator_GetSelectedItemHeight(ArkUI_SwiperIndicator* indicator)
```

**描述**

获取被选中Swiper组件圆点导航指示器的高。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 圆点导航指示器的高。单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_SetMask()

```c
void OH_ArkUI_SwiperIndicator_SetMask(ArkUI_SwiperIndicator* indicator, int32_t mask)
```

**描述**

设置是否显示Swiper组件圆点导航指示器的蒙版样式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| int32\_t mask | 是否显示蒙版样式，1表示显示，0表示不显示。 |

### OH\_ArkUI\_SwiperIndicator\_GetMask()

```c
int32_t OH_ArkUI_SwiperIndicator_GetMask(ArkUI_SwiperIndicator* indicator)
```

**描述**

获取是否显示Swiper组件圆点导航指示器的蒙版样式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | mask 1表示显示圆点导航指示器的蒙版样式，0表示不显示。 |

### OH\_ArkUI\_SwiperIndicator\_SetColor()

```c
void OH_ArkUI_SwiperIndicator_SetColor(ArkUI_SwiperIndicator* indicator, uint32_t color)
```

**描述**

设置Swiper组件圆点导航指示器的颜色。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| uint32\_t color | 颜色类型，0xargb格式，形如 0xFFFF0000表示红色。 |

### OH\_ArkUI\_SwiperIndicator\_GetColor()

```c
uint32_t OH_ArkUI_SwiperIndicator_GetColor(ArkUI_SwiperIndicator* indicator)
```

**描述**

获取Swiper组件圆点导航指示器的颜色。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 颜色类型，0xargb格式，形如 0xFFFF0000表示红色。 |

### OH\_ArkUI\_SwiperIndicator\_SetSelectedColor()

```c
void OH_ArkUI_SwiperIndicator_SetSelectedColor(ArkUI_SwiperIndicator* indicator, uint32_t selectedColor)
```

**描述**

设置被选中Swiper组件圆点导航指示器的颜色。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| uint32\_t selectedColor | 颜色类型，0xargb格式，形如 0xFFFF0000表示红色。 |

### OH\_ArkUI\_SwiperIndicator\_GetSelectedColor()

```c
uint32_t OH_ArkUI_SwiperIndicator_GetSelectedColor(ArkUI_SwiperIndicator* indicator)
```

**描述**

获取被选中Swiper组件圆点导航指示器的颜色。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 颜色类型，0xargb格式，形如 0xFFFF0000表示红色。 |

### OH\_ArkUI\_SwiperIndicator\_SetMaxDisplayCount()

```c
int32_t OH_ArkUI_SwiperIndicator_SetMaxDisplayCount(ArkUI_SwiperIndicator* indicator, int32_t maxDisplayCount)
```

**描述**

设置圆点导航点指示器样式下，导航点显示个数的最大值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| int32\_t maxDisplayCount | 导航点显示个数最大值，有效取值范围[6, 9]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 如果maxDisplayCount设置范围错误，返回错误码。 |

### OH\_ArkUI\_SwiperIndicator\_GetMaxDisplayCount()

```c
int32_t OH_ArkUI_SwiperIndicator_GetMaxDisplayCount(ArkUI_SwiperIndicator* indicator)
```

**描述**

获取圆点导航点指示器样式下，导航点显示个数的最大值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 导航点显示个数最大值，有效取值范围[6, 9]。 |

### OH\_ArkUI\_SwiperDigitIndicator\_Create()

```c
ArkUI_SwiperDigitIndicator *OH_ArkUI_SwiperDigitIndicator_Create()
```

**描述**

创建Swiper组件的数字导航指示器。

**起始版本：** 19

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator \*](capi-arkui-nativemodule-arkui-swiperdigitindicator.md) | 数字导航指示器对象指针。 |

### OH\_ArkUI\_SwiperDigitIndicator\_Destroy()

```c
void OH_ArkUI_SwiperDigitIndicator_Destroy(ArkUI_SwiperDigitIndicator* indicator)
```

**描述**

销毁Swiper组件的数字导航指示器指针。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |

### OH\_ArkUI\_SwiperDigitIndicator\_SetStartPosition()

```c
void OH_ArkUI_SwiperDigitIndicator_SetStartPosition(ArkUI_SwiperDigitIndicator* indicator, float value)
```

**描述**

设置数字导航指示器距离Swiper组件左边的距离，在从右至左显示的语言模式下，设置其距离Swiper组件右边的距离。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |
| float value | 数字导航指示器距离Swiper组件左边的距离，在从右至左显示的语言模式下，其距离Swiper组件右边的距离。默认值：0，单位：vp。 |

### OH\_ArkUI\_SwiperDigitIndicator\_GetStartPosition()

```c
float OH_ArkUI_SwiperDigitIndicator_GetStartPosition(ArkUI_SwiperDigitIndicator* indicator)
```

**描述**

获取数字导航指示器距离Swiper组件左边的距离，在从右至左显示的语言模式下，获取其距离Swiper组件右边的距离。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 数字导航指示器距离Swiper组件左边的距离，在从右至左显示的语言模式下，其距离Swiper组件右边的距离。单位：vp。 |

### OH\_ArkUI\_SwiperDigitIndicator\_SetTopPosition()

```c
void OH_ArkUI_SwiperDigitIndicator_SetTopPosition(ArkUI_SwiperDigitIndicator* indicator, float value)
```

**描述**

设置数字导航指示器距离Swiper组件顶部的距离。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |
| float value | 数字导航指示器距离Swiper组件顶部的距离。默认值：0，单位：vp。 |

### OH\_ArkUI\_SwiperDigitIndicator\_GetTopPosition()

```c
float OH_ArkUI_SwiperDigitIndicator_GetTopPosition(ArkUI_SwiperDigitIndicator* indicator)
```

**描述**

获取数字导航指示器距离Swiper组件顶部的距离。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 数字导航指示器距离Swiper组件顶部的距离。单位：vp。 |

### OH\_ArkUI\_SwiperDigitIndicator\_SetEndPosition()

```c
void OH_ArkUI_SwiperDigitIndicator_SetEndPosition(ArkUI_SwiperDigitIndicator* indicator, float value)
```

**描述**

设置数字导航指示器距离Swiper组件右边的距离，在从右至左显示的语言模式下，设置其距离Swiper组件左边的距离。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |
| float value | 数字导航指示器距离Swiper组件右边的距离，在从右至左显示的语言模式下，其距离Swiper组件左边的距离。默认值：0，单位：vp。 |

### OH\_ArkUI\_SwiperDigitIndicator\_GetEndPosition()

```c
float OH_ArkUI_SwiperDigitIndicator_GetEndPosition(ArkUI_SwiperDigitIndicator* indicator)
```

**描述**

获取数字导航指示器距离Swiper组件右边的距离，在从右至左显示的语言模式下，获取其距离Swiper组件左边的距离。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 数字导航指示器距离Swiper组件右边的距离，在从右至左显示的语言模式下，其距离Swiper组件左边的距离。单位：vp。 |

### OH\_ArkUI\_SwiperDigitIndicator\_SetBottomPosition()

```c
void OH_ArkUI_SwiperDigitIndicator_SetBottomPosition(ArkUI_SwiperDigitIndicator* indicator, float value)
```

**描述**

设置数字导航指示器距离Swiper组件底部的距离。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |
| float value | 数字导航指示器距离Swiper组件底部的距离。默认值：0，单位：vp。 |

### OH\_ArkUI\_SwiperDigitIndicator\_GetBottomPosition()

```c
float OH_ArkUI_SwiperDigitIndicator_GetBottomPosition(ArkUI_SwiperDigitIndicator* indicator)
```

**描述**

获取数字导航指示器距离Swiper组件底部的距离。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 数字导航指示器距离Swiper组件底部的距离。单位：vp。 |

### OH\_ArkUI\_SwiperDigitIndicator\_SetFontColor()

```c
void OH_ArkUI_SwiperDigitIndicator_SetFontColor(ArkUI_SwiperDigitIndicator* indicator, uint32_t color)
```

**描述**

设置Swiper组件数字导航指示器字体颜色。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |
| uint32\_t color | 颜色类型，0xargb格式，形如 0xFFFF0000表示红色。默认值：0xFF182431。 |

### OH\_ArkUI\_SwiperDigitIndicator\_GetFontColor()

```c
uint32_t OH_ArkUI_SwiperDigitIndicator_GetFontColor(ArkUI_SwiperDigitIndicator* indicator)
```

**描述**

获取Swiper组件数字导航指示器字体颜色。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 颜色类型，0xargb格式，形如 0xFFFF0000表示红色。 |

### OH\_ArkUI\_SwiperDigitIndicator\_SetSelectedFontColor()

```c
void OH_ArkUI_SwiperDigitIndicator_SetSelectedFontColor(ArkUI_SwiperDigitIndicator* indicator, uint32_t selectedColor)
```

**描述**

设置被选中Swiper组件数字导航指示器字体颜色。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |
| uint32\_t selectedColor | 颜色类型，0xargb格式，形如 0xFFFF0000表示红色。默认值：0xFF182431。 |

### OH\_ArkUI\_SwiperDigitIndicator\_GetSelectedFontColor()

```c
uint32_t OH_ArkUI_SwiperDigitIndicator_GetSelectedFontColor(ArkUI_SwiperDigitIndicator* indicator)
```

**描述**

获取被选中Swiper组件数字导航指示器字体颜色。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 颜色类型，0xargb格式，形如 0xFFFF0000表示红色。 |

### OH\_ArkUI\_SwiperDigitIndicator\_SetFontSize()

```c
void OH_ArkUI_SwiperDigitIndicator_SetFontSize(ArkUI_SwiperDigitIndicator* indicator, float size)
```

**描述**

设置Swiper组件数字导航指示器字体大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |
| float size | 字体大小数值，单位为fp。 |

### OH\_ArkUI\_SwiperDigitIndicator\_GetFontSize()

```c
float OH_ArkUI_SwiperDigitIndicator_GetFontSize(ArkUI_SwiperDigitIndicator* indicator)
```

**描述**

获取Swiper组件数字导航指示器字体大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 字体大小数值，单位为fp。 |

### OH\_ArkUI\_SwiperDigitIndicator\_SetSelectedFontSize()

```c
void OH_ArkUI_SwiperDigitIndicator_SetSelectedFontSize(ArkUI_SwiperDigitIndicator* indicator, float size)
```

**描述**

设置被选中Swiper组件数字导航指示器字体大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |
| float size | 字体大小数值，单位为fp。 |

### OH\_ArkUI\_SwiperDigitIndicator\_GetSelectedFontSize()

```c
float OH_ArkUI_SwiperDigitIndicator_GetSelectedFontSize(ArkUI_SwiperDigitIndicator* indicator)
```

**描述**

获取被选中Swiper组件数字导航指示器字体大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 字体大小数值，单位为fp。 |

### OH\_ArkUI\_SwiperArrowStyle\_Create()

```c
ArkUI_SwiperArrowStyle *OH_ArkUI_SwiperArrowStyle_Create()
```

**描述**

创建Swiper组件的导航箭头。

**起始版本：** 19

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle \*](capi-arkui-nativemodule-arkui-swiperarrowstyle.md) | 导航箭头对象指针。 |

### OH\_ArkUI\_SwiperArrowStyle\_Destroy()

```c
void OH_ArkUI_SwiperArrowStyle_Destroy(ArkUI_SwiperArrowStyle* arrowStyle)
```

**描述**

销毁Swiper组件的导航箭头指针。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |

### OH\_ArkUI\_SwiperArrowStyle\_SetShowBackground()

```c
void OH_ArkUI_SwiperArrowStyle_SetShowBackground(ArkUI_SwiperArrowStyle* arrowStyle, int32_t showBackground)
```

**描述**

设置Swiper组件导航箭头底板是否显示。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |
| int32\_t showBackground | 导航箭头底板是否显示，0：不显示，1：显示，默认值：0。 |

### OH\_ArkUI\_SwiperArrowStyle\_GetShowBackground()

```c
int32_t OH_ArkUI_SwiperArrowStyle_GetShowBackground(ArkUI_SwiperArrowStyle* arrowStyle)
```

**描述**

获取Swiper组件导航箭头底板是否显示。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 导航箭头底板是否显示，0：不显示，1：显示。 |

### OH\_ArkUI\_SwiperArrowStyle\_SetShowSidebarMiddle()

```c
void OH_ArkUI_SwiperArrowStyle_SetShowSidebarMiddle(ArkUI_SwiperArrowStyle* arrowStyle, int32_t showSidebarMiddle)
```

**描述**

设置Swiper组件导航箭头显示位置。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |
| int32\_t showSidebarMiddle | 导航箭头显示位置，0：显示在导航指示器两侧，1：显示在Swiper组件两侧，默认值：0。 |

### OH\_ArkUI\_SwiperArrowStyle\_GetShowSidebarMiddle()

```c
int32_t OH_ArkUI_SwiperArrowStyle_GetShowSidebarMiddle(ArkUI_SwiperArrowStyle* arrowStyle)
```

**描述**

获取Swiper组件导航箭头显示位置。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 导航箭头显示位置，0：显示在导航指示器两侧，1：显示在Swiper组件两侧。 |

### OH\_ArkUI\_SwiperArrowStyle\_SetBackgroundSize()

```c
void OH_ArkUI_SwiperArrowStyle_SetBackgroundSize(ArkUI_SwiperArrowStyle* arrowStyle, float backgroundSize)
```

**描述**

设置Swiper组件导航箭头底板大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |
| float backgroundSize | 导航箭头底板大小，单位：vp。默认值：显示在导航指示器两侧24vp，显示在Swiper两侧32vp。 |

### OH\_ArkUI\_SwiperArrowStyle\_GetBackgroundSize()

```c
float OH_ArkUI_SwiperArrowStyle_GetBackgroundSize(ArkUI_SwiperArrowStyle* arrowStyle)
```

**描述**

获取Swiper组件导航箭头底板大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 导航箭头底板大小，单位：vp。 |

### OH\_ArkUI\_SwiperArrowStyle\_SetBackgroundColor()

```c
void OH_ArkUI_SwiperArrowStyle_SetBackgroundColor(ArkUI_SwiperArrowStyle* arrowStyle, uint32_t backgroundColor)
```

**描述**

设置Swiper组件导航箭头底板颜色。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |
| uint32\_t backgroundColor | 导航箭头底板颜色，0xargb格式，形如 0xFFFF0000表示红色。默认值：显示在导航指示器两侧为0x00000000，显示在Swiper两侧为0x19182431。 |

### OH\_ArkUI\_SwiperArrowStyle\_GetBackgroundColor()

```c
uint32_t OH_ArkUI_SwiperArrowStyle_GetBackgroundColor(ArkUI_SwiperArrowStyle* arrowStyle)
```

**描述**

获取Swiper组件导航箭头底板颜色。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 导航箭头底板颜色，0xargb格式，形如 0xFFFF0000表示红色。 |

### OH\_ArkUI\_SwiperArrowStyle\_SetArrowSize()

```c
void OH_ArkUI_SwiperArrowStyle_SetArrowSize(ArkUI_SwiperArrowStyle* arrowStyle, float arrowSize)
```

**描述**

设置Swiper组件导航箭头大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |
| float arrowSize | 导航箭头大小，单位：vp。默认值：显示在导航指示器两侧18vp，显示在Swiper两侧24vp。显示导航箭头底板时，arrowSize固定为backgroundSize的3/4。 |

### OH\_ArkUI\_SwiperArrowStyle\_GetArrowSize()

```c
float OH_ArkUI_SwiperArrowStyle_GetArrowSize(ArkUI_SwiperArrowStyle* arrowStyle)
```

**描述**

获取Swiper组件导航箭头大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 导航箭头大小，单位：vp。 |

### OH\_ArkUI\_SwiperArrowStyle\_SetArrowColor()

```c
void OH_ArkUI_SwiperArrowStyle_SetArrowColor(ArkUI_SwiperArrowStyle* arrowStyle, uint32_t arrowColor)
```

**描述**

设置Swiper组件导航箭头颜色。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |
| uint32\_t arrowColor | 导航箭头颜色，0xargb格式，形如 0xFFFF0000表示红色。 |

### OH\_ArkUI\_SwiperArrowStyle\_GetArrowColor()

```c
uint32_t OH_ArkUI_SwiperArrowStyle_GetArrowColor(ArkUI_SwiperArrowStyle* arrowStyle)
```

**描述**

获取Swiper组件导航箭头颜色。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 导航箭头颜色，0xargb格式，形如 0xFFFF0000表示红色。 |

### OH\_ArkUI\_SwiperIndicator\_SetSpace()

```c
void OH_ArkUI_SwiperIndicator_SetSpace(ArkUI_SwiperIndicator* indicator, float space)
```

**描述**

设置导航点间距。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| float space | 导航点间距。默认值：8，单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_GetSpace()

```c
float OH_ArkUI_SwiperIndicator_GetSpace(ArkUI_SwiperIndicator* indicator)
```

**描述**

获取导航点间距。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 导航点间距。单位：vp。 |

### OH\_ArkUI\_SwiperDigitIndicator\_SetIgnoreSizeOfBottom()

```c
void OH_ArkUI_SwiperDigitIndicator_SetIgnoreSizeOfBottom(ArkUI_SwiperDigitIndicator* indicator, int32_t ignoreSize)
```

**描述**

设置OH\_ArkUI\_SwiperDigitIndicator\_SetBottomPosition是否忽略导航点大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 导航指示器对象指针。 |
| int32\_t ignoreSize | 是否忽略导航点大小。1表示忽略导航点大小，0表示不忽略，默认值0。 |

### OH\_ArkUI\_SwiperDigitIndicator\_GetIgnoreSizeOfBottom()

```c
int32_t OH_ArkUI_SwiperDigitIndicator_GetIgnoreSizeOfBottom(ArkUI_SwiperDigitIndicator* indicator)
```

**描述**

获取OH\_ArkUI\_SwiperDigitIndicator\_SetBottomPosition是否忽略导航点大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 是否忽略导航点大小。 |
