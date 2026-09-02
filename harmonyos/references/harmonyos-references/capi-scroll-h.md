---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scroll-h
title: scroll.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > scroll.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1c4997ba1b9fca124cc0229798395d2e90c49651757a13862ee8d224582a535f
---

## 概述

提供滚动方向、边缘效果、滚动条状态、内容裁剪、嵌套滚动、滚动状态和滚动来源等枚举，用于配置和监听Scroll组件及相关可滚动组件的行为。

**引用文件：** <arkui/node\_attributes/scroll.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [ScrollableNDK](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/ScrollableNDK)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_EdgeEffect](capi-scroll-h.md#arkui_edgeeffect) | ArkUI\_EdgeEffect | 定义边缘滑动效果枚举值。 |
| [ArkUI\_BarState](capi-scroll-h.md#arkui_barstate) | ArkUI\_BarState | 定义TextArea和TextEditor组件的滚动条状态枚举值。 |
| [ArkUI\_EffectEdge](capi-scroll-h.md#arkui_effectedge) | ArkUI\_EffectEdge | 定义边缘效果生效边缘的方向枚举值。 |
| [ArkUI\_ScrollDirection](capi-scroll-h.md#arkui_scrolldirection) | ArkUI\_ScrollDirection | 定义[Scroll](ts-container-scroll.md)组件排列方向枚举值。 |
| [ArkUI\_ScrollSnapAlign](capi-scroll-h.md#arkui_scrollsnapalign) | ArkUI\_ScrollSnapAlign | 定义列表项滚动结束对齐效果枚举值。 |
| [ArkUI\_ScrollBarDisplayMode](capi-scroll-h.md#arkui_scrollbardisplaymode) | ArkUI\_ScrollBarDisplayMode | 定义滚动条状态枚举值。 |
| [ArkUI\_ContentClipMode](capi-scroll-h.md#arkui_contentclipmode) | ArkUI\_ContentClipMode | 定义滚动容器的内容层裁剪区域枚举值。 |
| [ArkUI\_ScrollNestedMode](capi-scroll-h.md#arkui_scrollnestedmode) | ArkUI\_ScrollNestedMode | 定义嵌套滚动选项。 |
| [ArkUI\_ScrollEdge](capi-scroll-h.md#arkui_scrolledge) | ArkUI\_ScrollEdge | 定义滚动到的边缘位置。 |
| [ArkUI\_ScrollAlignment](capi-scroll-h.md#arkui_scrollalignment) | ArkUI\_ScrollAlignment | 滚动到具体item时的对齐方式。 |
| [ArkUI\_ScrollState](capi-scroll-h.md#arkui_scrollstate) | ArkUI\_ScrollState | 定义当前滚动状态。 |
| [ArkUI\_ScrollSource](capi-scroll-h.md#arkui_scrollsource) | ArkUI\_ScrollSource | 定义滚动来源枚举值。 |
| [ArkUI\_ScrollSnapAnimationSpeed](capi-scroll-h.md#arkui_scrollsnapanimationspeed) | ArkUI\_ScrollSnapAnimationSpeed | 列表限位滚动动画速度。 |

## 枚举类型说明

### ArkUI\_EdgeEffect

```c
enum ArkUI_EdgeEffect
```

**描述：**

定义边缘滑动效果枚举值。Grid、Scroll、WaterFlow组件默认值为ARKUI\_EDGE\_EFFECT\_NONE，List组件默认值为ARKUI\_EDGE\_EFFECT\_SPRING。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_EDGE\_EFFECT\_SPRING = 0 | 弹性物理动效，滑动到边缘后可以根据初始速度或通过触摸事件继续滑动一段距离，松手后回弹。 |
| ARKUI\_EDGE\_EFFECT\_FADE = 1 | 阴影效果，滑动到边缘后会有圆弧状的阴影。 |
| ARKUI\_EDGE\_EFFECT\_NONE = 2 | 滑动到边缘后无效果。 |

### ArkUI\_BarState

```c
enum ArkUI_BarState
```

**描述：**

定义TextArea和TextEditor组件的滚动条状态枚举值。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_BAR\_STATE\_OFF = 0 | 不显示。 |
| ARKUI\_BAR\_STATE\_AUTO = 1 | 按需显示（在触摸时显示滚动条，2秒后自动消失）。 |
| ARKUI\_BAR\_STATE\_ON = 2 | 常驻显示。 |

### ArkUI\_EffectEdge

```c
enum ArkUI_EffectEdge
```

**描述：**

定义边缘效果生效边缘的方向枚举值。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_EFFECT\_EDGE\_START = 1 | 起始边生效。 |
| ARKUI\_EFFECT\_EDGE\_END = 2 | 末尾边生效。 |

### ArkUI\_ScrollDirection

```c
enum ArkUI_ScrollDirection
```

**描述：**

定义[Scroll](ts-container-scroll.md)组件排列方向枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SCROLL\_DIRECTION\_VERTICAL = 0 | 仅支持竖直方向滚动。 |
| ARKUI\_SCROLL\_DIRECTION\_HORIZONTAL = 1 | 仅支持水平方向滚动。 |
| ARKUI\_SCROLL\_DIRECTION\_NONE = 3 | 禁止滚动。 |
| ARKUI\_SCROLL\_DIRECTION\_FREE = 4 | 自由滚动，支持竖直和水平方向滚动，仅在Scroll组件中可用。  **起始版本：** 20 |

### ArkUI\_ScrollSnapAlign

```c
enum ArkUI_ScrollSnapAlign
```

**描述：**

定义列表项滚动结束对齐效果枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SCROLL\_SNAP\_ALIGN\_NONE = 0 | 默认无列表滚动对齐效果。 |
| ARKUI\_SCROLL\_SNAP\_ALIGN\_START = 1 | 视图中的第一项将在列表的开头对齐。 |
| ARKUI\_SCROLL\_SNAP\_ALIGN\_CENTER = 2 | 视图中的中间项将在列表中心对齐。 |
| ARKUI\_SCROLL\_SNAP\_ALIGN\_END = 3 | 视图中的最后一项将在列表末尾对齐。 |

### ArkUI\_ScrollBarDisplayMode

```c
enum ArkUI_ScrollBarDisplayMode
```

**描述：**

定义滚动条状态枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_OFF = 0 | 不显示。 |
| ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_AUTO = 1 | 按需显示(触摸时显示，2s后消失)。 |
| ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_ON = 2 | 常驻显示。 |

### ArkUI\_ContentClipMode

```c
enum ArkUI_ContentClipMode
```

**描述：**

定义滚动容器的内容层裁剪区域枚举值。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_CONTENT\_CLIP\_MODE\_CONTENT\_ONLY = 0 | 按内容区裁剪。 |
| ARKUI\_CONTENT\_CLIP\_MODE\_BOUNDARY = 1 | 按组件区域裁剪。 |
| ARKUI\_CONTENT\_CLIP\_MODE\_SAFE\_AREA = 2 | 按组件配置的[安全区域](ts-universal-attributes-expand-safe-area.md)裁剪。 |

### ArkUI\_ScrollNestedMode

```c
enum ArkUI_ScrollNestedMode
```

**描述：**

定义嵌套滚动选项。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SCROLL\_NESTED\_MODE\_SELF\_ONLY = 0 | 只自身滚动，不与父组件联动。 |
| ARKUI\_SCROLL\_NESTED\_MODE\_SELF\_FIRST = 1 | 自身先滚动，自身滚动到边缘以后父组件滚动。父组件滚动到边缘以后，如果父组件有边缘效果，则父组件触发边缘效果，否则子组件触发边缘效果。 |
| ARKUI\_SCROLL\_NESTED\_MODE\_PARENT\_FIRST = 2 | 父组件先滚动，父组件滚动到边缘以后自身滚动。自身滚动到边缘后，如果有边缘效果，会触发自身的边缘效果，否则触发父组件的边缘效果。 |
| ARKUI\_SCROLL\_NESTED\_MODE\_PARALLEL = 3 | 自身和父组件同时滚动，自身和父组件都到达边缘以后，如果自身有边缘效果，则自身触发边缘效果，否则父组件触发边缘效果。 |

### ArkUI\_ScrollEdge

```c
enum ArkUI_ScrollEdge
```

**描述：**

定义滚动到的边缘位置。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SCROLL\_EDGE\_TOP = 0 | 竖直方向上边缘。 |
| ARKUI\_SCROLL\_EDGE\_BOTTOM = 1 | 竖直方向下边缘。 |
| ARKUI\_SCROLL\_EDGE\_START = 2 | 水平方向起始位置。 |
| ARKUI\_SCROLL\_EDGE\_END = 3 | 水平方向末尾位置。 |

### ArkUI\_ScrollAlignment

```c
enum ArkUI_ScrollAlignment
```

**描述：**

滚动到具体item时的对齐方式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SCROLL\_ALIGNMENT\_START = 0 | 首部对齐。指定item首部与容器首部对齐。 |
| ARKUI\_SCROLL\_ALIGNMENT\_CENTER = 1 | 居中对齐。指定item主轴方向居中对齐于容器。 |
| ARKUI\_SCROLL\_ALIGNMENT\_END = 2 | 尾部对齐。指定item尾部与容器尾部对齐。 |
| ARKUI\_SCROLL\_ALIGNMENT\_AUTO = 3 | 自动对齐。若指定item完全处于显示区，不做调整。否则依照滑动距离最短的原则，将指定item首部对齐或尾部对齐于容器，使指定item完全处于显示区。 |

### ArkUI\_ScrollState

```c
enum ArkUI_ScrollState
```

**描述：**

定义当前滚动状态。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SCROLL\_STATE\_IDLE = 0 | 空闲状态。使用控制器提供的方法控制滚动时触发，拖动滚动条滚动时触发。 |
| ARKUI\_SCROLL\_STATE\_SCROLL = 1 | 滚动状态。使用手指拖动容器滚动时触发。 |
| ARKUI\_SCROLL\_STATE\_FLING = 2 | 惯性滚动状态。快速划动松手后进行惯性滚动和划动到边缘回弹时触发。 |

### ArkUI\_ScrollSource

```c
enum ArkUI_ScrollSource
```

**描述：**

定义滚动来源枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SCROLL\_SOURCE\_DRAG = 0 | 手指拖动。 |
| ARKUI\_SCROLL\_SOURCE\_FLING = 1 | 手指拖动后的惯性滚动。 |
| ARKUI\_SCROLL\_SOURCE\_EDGE\_EFFECT = 2 | 在过界时执行[EdgeEffect.Spring](ts-appendix-enums.md#edgeeffect)边缘特效。 |
| ARKUI\_SCROLL\_SOURCE\_OTHER\_USER\_INPUT = 3 | 除了拖动以外的其他用户输入，如鼠标滚轮、键盘事件等。 |
| ARKUI\_SCROLL\_SOURCE\_SCROLL\_BAR = 4 | 拖动滚动条。 |
| ARKUI\_SCROLL\_SOURCE\_SCROLL\_BAR\_FLING = 5 | 拖动滚动条后的惯性滚动。 |
| ARKUI\_SCROLL\_SOURCE\_SCROLLER = 6 | 滚动控制器引起的无动画的滚动。 |
| ARKUI\_SCROLL\_SOURCE\_ANIMATION = 7 | 滚动控制器引起的带动画的滚动。 |

### ArkUI\_ScrollSnapAnimationSpeed

```c
enum ArkUI_ScrollSnapAnimationSpeed
```

**描述：**

列表限位滚动动画速度。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SCROLL\_SNAP\_ANIMATION\_NORMAL = 0 | 限位滚动动画速度正常。 |
| ARKUI\_SCROLL\_SNAP\_ANIMATION\_SLOW = 1 | 限位滚动动画速度慢。 |
