---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-list-item-h
title: list_item.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > list_item.h
category: harmonyos-references
scraped_at: 2026-11-12T09:54:43+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:6eeba0c184cc41ab1158f6d167f725270bd1c997a98d3359d5cd20fba0d01174
---

## 概述

定义ListItem组件侧滑操作相关的枚举和接口，支持设置侧滑操作项内容、长距滑动删除距离阈值及滑动状态变化回调，可用于实现列表项侧滑显示操作菜单或长距滑动删除等交互场景。

**引用文件：** <arkui/node\_attributes/list\_item.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_ListItemSwipeActionItem](capi-arkui-nativemodule-arkui-listitemswipeactionitem.md) | ArkUI\_ListItemSwipeActionItem | 定义ListItem组件swipeAction方法内Item的配置信息。 |
| [ArkUI\_ListItemSwipeActionOption](capi-arkui-nativemodule-arkui-listitemswipeactionoption.md) | ArkUI\_ListItemSwipeActionOption | 定义ListItem组件swipeAction方法的配置信息。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_ListItemSwipeActionState](capi-list-item-h.md#arkui_listitemswipeactionstate) | ArkUI\_ListItemSwipeActionState | 定义[ListItem](ts-container-listitem.md#listitem10)组件[swipeAction](ts-container-listitem.md#swipeaction9)方法的列表项滑动状态。 |
| [ArkUI\_ListItemSwipeEdgeEffect](capi-list-item-h.md#arkui_listitemswipeedgeeffect) | ArkUI\_ListItemSwipeEdgeEffect | 定义[ListItem](ts-container-listitem.md#listitem10)组件[swipeAction](ts-container-listitem.md#swipeaction9)方法的边缘滑动效果。 |
| [ArkUI\_ListItemSwipeActionDirection](capi-list-item-h.md#arkui_listitemswipeactiondirection) | ArkUI\_ListItemSwipeActionDirection | ListItem划出菜单的展开方向。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem\* OH\_ArkUI\_ListItemSwipeActionItem\_Create()](capi-list-item-h.md#oh_arkui_listitemswipeactionitem_create) | 创建ListItem组件swipeAction方法设置的Item配置项。 |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_Dispose(ArkUI\_ListItemSwipeActionItem\* item)](capi-list-item-h.md#oh_arkui_listitemswipeactionitem_dispose) | 销毁由OH\_ArkUI\_ListItemSwipeActionItem\_Create创建的ListItemSwipeActionItem实例。 |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetContent(ArkUI\_ListItemSwipeActionItem\* item, ArkUI\_NodeHandle node)](capi-list-item-h.md#oh_arkui_listitemswipeactionitem_setcontent) | 设置ListItemSwipeActionItem的布局内容。 |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetActionAreaDistance(ArkUI\_ListItemSwipeActionItem\* item, float distance)](capi-list-item-h.md#oh_arkui_listitemswipeactionitem_setactionareadistance) | 设置组件长距离滑动删除距离阈值。 |
| [float OH\_ArkUI\_ListItemSwipeActionItem\_GetActionAreaDistance(ArkUI\_ListItemSwipeActionItem\* item)](capi-list-item-h.md#oh_arkui_listitemswipeactionitem_getactionareadistance) | 获取组件长距离滑动删除距离阈值。 |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnEnterActionArea(ArkUI\_ListItemSwipeActionItem\* item, void (\*callback)())](capi-list-item-h.md#oh_arkui_listitemswipeactionitem_setonenteractionarea) | 设置滑动条目进入长距删除区时调用的事件。 |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnEnterActionAreaWithUserData(ArkUI\_ListItemSwipeActionItem\* item, void\* userData, void (\*callback)(void\* userData))](capi-list-item-h.md#oh_arkui_listitemswipeactionitem_setonenteractionareawithuserdata) | 设置滑动条目进入长距删除区时调用的事件，回调事件会传入用户自定义数据。 |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnAction(ArkUI\_ListItemSwipeActionItem\* item, void (\*callback)())](capi-list-item-h.md#oh_arkui_listitemswipeactionitem_setonaction) | 设置滑动条目进入长距删除区后抬手删除ListItem时调用的事件。 |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnActionWithUserData(ArkUI\_ListItemSwipeActionItem\* item, void\* userData, void (\*callback)(void\* userData))](capi-list-item-h.md#oh_arkui_listitemswipeactionitem_setonactionwithuserdata) | 设置滑动条目进入长距删除区后抬手删除ListItem时调用的事件，回调事件会传入用户自定义数据。 |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnExitActionArea(ArkUI\_ListItemSwipeActionItem\* item, void (\*callback)())](capi-list-item-h.md#oh_arkui_listitemswipeactionitem_setonexitactionarea) | 设置滑动条目退出长距删除区时调用的事件。 |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnExitActionAreaWithUserData(ArkUI\_ListItemSwipeActionItem\* item, void\* userData, void (\*callback)(void\* userData))](capi-list-item-h.md#oh_arkui_listitemswipeactionitem_setonexitactionareawithuserdata) | 设置滑动条目退出长距删除区时调用的事件，回调事件会传入用户自定义数据。 |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnStateChange(ArkUI\_ListItemSwipeActionItem\* item, void (\*callback)(ArkUI\_ListItemSwipeActionState swipeActionState))](capi-list-item-h.md#oh_arkui_listitemswipeactionitem_setonstatechange) | 设置列表项滑动状态变化时触发的事件。 |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnStateChangeWithUserData(ArkUI\_ListItemSwipeActionItem\* item, void\* userData, void (\*callback)(ArkUI\_ListItemSwipeActionState swipeActionState, void\* userData))](capi-list-item-h.md#oh_arkui_listitemswipeactionitem_setonstatechangewithuserdata) | 设置列表项滑动状态变化时触发的事件，回调事件会传入用户自定义数据。 |
| [ArkUI\_ListItemSwipeActionOption\* OH\_ArkUI\_ListItemSwipeActionOption\_Create()](capi-list-item-h.md#oh_arkui_listitemswipeactionoption_create) | 创建ListItem组件swipeAction方法设置的配置项。 |
| [void OH\_ArkUI\_ListItemSwipeActionOption\_Dispose(ArkUI\_ListItemSwipeActionOption\* option)](capi-list-item-h.md#oh_arkui_listitemswipeactionoption_dispose) | 销毁由OH\_ArkUI\_ListItemSwipeActionOption\_Create创建的ListItemSwipeActionOption实例。 |
| [void OH\_ArkUI\_ListItemSwipeActionOption\_SetStart(ArkUI\_ListItemSwipeActionOption\* option, ArkUI\_ListItemSwipeActionItem\* item)](capi-list-item-h.md#oh_arkui_listitemswipeactionoption_setstart) | 设置ListItemSwipeActionItem的左侧（垂直布局）或上方（横向布局）布局内容。 |
| [void OH\_ArkUI\_ListItemSwipeActionOption\_SetEnd(ArkUI\_ListItemSwipeActionOption\* option, ArkUI\_ListItemSwipeActionItem\* item)](capi-list-item-h.md#oh_arkui_listitemswipeactionoption_setend) | 设置ListItemSwipeActionItem的右侧（垂直布局）或下方（横向布局）布局内容。 |
| [void OH\_ArkUI\_ListItemSwipeActionOption\_SetEdgeEffect(ArkUI\_ListItemSwipeActionOption\* option, ArkUI\_ListItemSwipeEdgeEffect edgeEffect)](capi-list-item-h.md#oh_arkui_listitemswipeactionoption_setedgeeffect) | 设置边缘滑动效果。 |
| [int32\_t OH\_ArkUI\_ListItemSwipeActionOption\_GetEdgeEffect(ArkUI\_ListItemSwipeActionOption\* option)](capi-list-item-h.md#oh_arkui_listitemswipeactionoption_getedgeeffect) | 获取边缘滑动效果。 |
| [void OH\_ArkUI\_ListItemSwipeActionOption\_SetOnOffsetChange(ArkUI\_ListItemSwipeActionOption\* option, void (\*callback)(float offset))](capi-list-item-h.md#oh_arkui_listitemswipeactionoption_setonoffsetchange) | 滑动操作偏移量更改时调用的事件。 |
| [void OH\_ArkUI\_ListItemSwipeActionOption\_SetOnOffsetChangeWithUserData(ArkUI\_ListItemSwipeActionOption\* option, void\* userData, void (\*callback)(float offset, void\* userData))](capi-list-item-h.md#oh_arkui_listitemswipeactionoption_setonoffsetchangewithuserdata) | 滑动操作偏移量更改时调用的事件，回调事件会传入用户自定义数据。 |
| [int32\_t OH\_ArkUI\_ListItemSwipeAction\_Expand(ArkUI\_NodeHandle node, ArkUI\_ListItemSwipeActionDirection direction)](capi-list-item-h.md#oh_arkui_listitemswipeaction_expand) | 展开指定ListItem的划出菜单。 |
| [int32\_t OH\_ArkUI\_ListItemSwipeAction\_Collapse(ArkUI\_NodeHandle node)](capi-list-item-h.md#oh_arkui_listitemswipeaction_collapse) | 收起指定ListItem的划出菜单。 |

## 枚举类型说明

### ArkUI\_ListItemSwipeActionState

```c
enum ArkUI_ListItemSwipeActionState
```

**描述：**

定义[ListItem](ts-container-listitem.md#listitem10)组件[swipeAction](ts-container-listitem.md#swipeaction9)方法的列表项滑动状态。侧滑操作在垂直列表中沿水平方向进行，在水平列表中沿垂直方向进行。默认值为ARKUI\_LIST\_ITEM\_SWIPE\_ACTION\_STATE\_COLLAPSED。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LIST\_ITEM\_SWIPE\_ACTION\_STATE\_COLLAPSED = 0 | 收起状态，操作项处于隐藏状态。 |
| ARKUI\_LIST\_ITEM\_SWIPE\_ACTION\_STATE\_EXPANDED = 1 | 展开状态，操作项处于显示状态。 |
| ARKUI\_LIST\_ITEM\_SWIPE\_ACTION\_STATE\_ACTIONING = 2 | 长距离状态，表示ListItem进入长距删除区后处于删除操作中的状态。 |

### ArkUI\_ListItemSwipeEdgeEffect

```c
enum ArkUI_ListItemSwipeEdgeEffect
```

**描述：**

定义ListItem组件[swipeAction](ts-container-listitem.md#swipeaction9)方法的边缘滑动效果，默认值为ARKUI\_LIST\_ITEM\_SWIPE\_EDGE\_EFFECT\_SPRING。其中，划出组件是指侧滑操作时展示的操作项内容。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LIST\_ITEM\_SWIPE\_EDGE\_EFFECT\_SPRING = 0 | ListItem滑动距离超过划出组件大小后可以继续滑动。 |
| ARKUI\_LIST\_ITEM\_SWIPE\_EDGE\_EFFECT\_NONE = 1 | ListItem滑动距离不能超过划出组件大小。 |

### ArkUI\_ListItemSwipeActionDirection

```c
enum ArkUI_ListItemSwipeActionDirection
```

**描述：**

ListItem划出菜单的展开方向。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LIST\_ITEM\_SWIPE\_ACTION\_DIRECTION\_START = 0 | 当列表方向为垂直时，LTR模式下表示ListItem的左边，RTL模式下表示ListItem的右边。当列表方向为水平时，表示ListItem的上边。 |
| ARKUI\_LIST\_ITEM\_SWIPE\_ACTION\_DIRECTION\_END = 1 | 当列表方向为垂直时，LTR模式下表示ListItem的右边，RTL模式下表示ListItem的左边。当列表方向为水平时，表示ListItem的下边。 |

## 函数说明

### OH\_ArkUI\_ListItemSwipeActionItem\_Create()

```c
ArkUI_ListItemSwipeActionItem* OH_ArkUI_ListItemSwipeActionItem_Create()
```

**描述：**

创建ListItem组件swipeAction方法设置的Item配置项。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](capi-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* | ListItemSwipeActionItem配置项实例，用于设置侧滑操作项的布局内容、长距滑动删除距离阈值及滑动状态变化回调。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_Dispose()

```c
void OH_ArkUI_ListItemSwipeActionItem_Dispose(ArkUI_ListItemSwipeActionItem* item)
```

**描述：**

销毁由OH\_ArkUI\_ListItemSwipeActionItem\_Create创建的ListItemSwipeActionItem实例，使用完毕后需调用本接口释放，避免内存泄漏。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](capi-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | 要销毁的ListItemSwipeActionItem实例。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_SetContent()

```c
void OH_ArkUI_ListItemSwipeActionItem_SetContent(ArkUI_ListItemSwipeActionItem* item, ArkUI_NodeHandle node)
```

**描述：**

设置ListItemSwipeActionItem的布局内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](capi-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | ListItemSwipeActionItem实例。 |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 侧滑操作项的内容节点。不设置时，侧滑操作项无可显示内容。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_SetActionAreaDistance()

```c
void OH_ArkUI_ListItemSwipeActionItem_SetActionAreaDistance(ArkUI_ListItemSwipeActionItem* item, float distance)
```

**描述：**

设置组件长距离滑动删除距离阈值，即列表项侧滑删除的触发距离。当划出组件被完全滑出后继续滑动，且该阈值取值大于0并小于ListItem在滑动方向上的尺寸减去划出组件在滑动方向上的尺寸时，继续滑动距离超过或等于该阈值后ListItem进入长距删除区。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](capi-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | ListItemSwipeActionItem实例。 |
| float distance | 组件长距离滑动删除距离阈值，单位vp。默认值为56vp；取值小于等于0或大于等于ListItem在滑动方向上的尺寸减去划出组件在滑动方向上的尺寸时，不会形成长距删除区；进入长距删除区时会触发OH\_ArkUI\_ListItemSwipeActionItem\_SetOnEnterActionArea或OH\_ArkUI\_ListItemSwipeActionItem\_SetOnEnterActionAreaWithUserData设置的回调，退出长距删除区时会触发OH\_ArkUI\_ListItemSwipeActionItem\_SetOnExitActionArea或OH\_ArkUI\_ListItemSwipeActionItem\_SetOnExitActionAreaWithUserData设置的回调。建议配合OH\_ArkUI\_ListItemSwipeActionItem\_SetOnAction或OH\_ArkUI\_ListItemSwipeActionItem\_SetOnActionWithUserData回调使用。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_GetActionAreaDistance()

```c
float OH_ArkUI_ListItemSwipeActionItem_GetActionAreaDistance(ArkUI_ListItemSwipeActionItem* item)
```

**描述：**

获取组件长距离滑动删除距离阈值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](capi-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | ListItemSwipeActionItem实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 组件长距离滑动删除距离阈值，单位vp。未显式设置时返回默认值56vp，异常时返回值：-1.0f。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_SetOnEnterActionArea()

```c
void OH_ArkUI_ListItemSwipeActionItem_SetOnEnterActionArea(ArkUI_ListItemSwipeActionItem* item, void (*callback)())
```

**描述：**

设置滑动条目进入长距删除区时调用的事件。仅当长距删除距离阈值有效并形成长距删除区时触发。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](capi-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | ListItemSwipeActionItem实例。 |
| void (\*callback)() | 回调事件。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_SetOnEnterActionAreaWithUserData()

```c
void OH_ArkUI_ListItemSwipeActionItem_SetOnEnterActionAreaWithUserData(ArkUI_ListItemSwipeActionItem* item, void* userData, void (*callback)(void* userData))
```

**描述：**

设置滑动条目进入长距删除区时调用的事件，回调事件会传入用户自定义数据。仅当长距删除距离阈值有效并形成长距删除区时触发。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](capi-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | ListItemSwipeActionItem实例。 |
| void\* userData | 用户自定义数据。 |
| void (\*callback)(void\* userData) | 回调事件。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_SetOnAction()

```c
void OH_ArkUI_ListItemSwipeActionItem_SetOnAction(ArkUI_ListItemSwipeActionItem* item, void (*callback)())
```

**描述：**

设置滑动条目进入长距删除区后抬手删除[ListItem](ts-container-listitem.md)时调用的事件。仅在删除距离阈值处于有效取值范围（大于0且小于ListItem在滑动方向上的尺寸减去划出组件在滑动方向上的尺寸），且滑动后松手位置超过或等于该阈值时触发。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](capi-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | ListItemSwipeActionItem实例。 |
| void (\*callback)() | 回调事件。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_SetOnActionWithUserData()

```c
void OH_ArkUI_ListItemSwipeActionItem_SetOnActionWithUserData(ArkUI_ListItemSwipeActionItem* item, void* userData, void (*callback)(void* userData))
```

**描述：**

设置滑动条目进入长距删除区后抬手删除ListItem时调用的事件，回调事件会传入用户自定义数据。仅在删除距离阈值处于有效取值范围（大于0且小于ListItem在滑动方向上的尺寸减去划出组件在滑动方向上的尺寸），且滑动后松手位置超过或等于该阈值时触发。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](capi-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | ListItemSwipeActionItem实例。 |
| void\* userData | 用户自定义数据。 |
| void (\*callback)(void\* userData) | 回调事件。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_SetOnExitActionArea()

```c
void OH_ArkUI_ListItemSwipeActionItem_SetOnExitActionArea(ArkUI_ListItemSwipeActionItem* item, void (*callback)())
```

**描述：**

设置滑动条目退出长距删除区时调用的事件。仅当长距删除距离阈值有效并形成长距删除区时触发。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](capi-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | ListItemSwipeActionItem实例。 |
| void (\*callback)() | 回调事件。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_SetOnExitActionAreaWithUserData()

```c
void OH_ArkUI_ListItemSwipeActionItem_SetOnExitActionAreaWithUserData(ArkUI_ListItemSwipeActionItem* item, void* userData, void (*callback)(void* userData))
```

**描述：**

设置滑动条目退出长距删除区时调用的事件，回调事件会传入用户自定义数据。仅当长距删除距离阈值有效并形成长距删除区时触发。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](capi-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | ListItemSwipeActionItem实例。 |
| void\* userData | 用户自定义数据。 |
| void (\*callback)(void\* userData) | 回调事件。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_SetOnStateChange()

```c
void OH_ArkUI_ListItemSwipeActionItem_SetOnStateChange(ArkUI_ListItemSwipeActionItem* item, void (*callback)(ArkUI_ListItemSwipeActionState swipeActionState))
```

**描述：**

设置列表项滑动状态变化时触发的事件。列表项滑动状态会在收起、展开和长距离状态之间切换，具体状态见[ArkUI\_ListItemSwipeActionState](capi-list-item-h.md#arkui_listitemswipeactionstate)。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](capi-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | ListItemSwipeActionItem实例。 |
| void (\*callback)(ArkUI\_ListItemSwipeActionState swipeActionState) | 回调事件。传入参数为swipeActionState，表示列表项滑动状态。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_SetOnStateChangeWithUserData()

```c
void OH_ArkUI_ListItemSwipeActionItem_SetOnStateChangeWithUserData(ArkUI_ListItemSwipeActionItem* item, void* userData, void (*callback)(ArkUI_ListItemSwipeActionState swipeActionState, void* userData))
```

**描述：**

设置列表项滑动状态变化时触发的事件，回调事件会传入用户自定义数据。列表项滑动状态会在收起、展开和长距离状态之间切换，具体状态见[ArkUI\_ListItemSwipeActionState](capi-list-item-h.md#arkui_listitemswipeactionstate)。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](capi-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | ListItemSwipeActionItem实例。 |
| void\* userData | 用户自定义数据。 |
| void (\*callback)(ArkUI\_ListItemSwipeActionState swipeActionState, void\* userData) | 回调事件。传入参数为swipeActionState，表示列表项滑动状态。 |

### OH\_ArkUI\_ListItemSwipeActionOption\_Create()

```c
ArkUI_ListItemSwipeActionOption* OH_ArkUI_ListItemSwipeActionOption_Create()
```

**描述：**

创建ListItem组件swipeAction方法设置的配置项。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionOption](capi-arkui-nativemodule-arkui-listitemswipeactionoption.md)\* | ListItemSwipeActionOption配置项实例，用于设置ListItem侧滑操作项在起始侧和结束侧的布局内容、边缘滑动效果及偏移量变化回调。 |

### OH\_ArkUI\_ListItemSwipeActionOption\_Dispose()

```c
void OH_ArkUI_ListItemSwipeActionOption_Dispose(ArkUI_ListItemSwipeActionOption* option)
```

**描述：**

销毁由OH\_ArkUI\_ListItemSwipeActionOption\_Create创建的ListItemSwipeActionOption实例，使用完毕后需调用本接口释放，避免内存泄漏。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionOption](capi-arkui-nativemodule-arkui-listitemswipeactionoption.md)\* option | 要销毁的ListItemSwipeActionOption实例。 |

### OH\_ArkUI\_ListItemSwipeActionOption\_SetStart()

```c
void OH_ArkUI_ListItemSwipeActionOption_SetStart(ArkUI_ListItemSwipeActionOption* option, ArkUI_ListItemSwipeActionItem* item)
```

**描述：**

设置ListItemSwipeActionItem的左侧（垂直布局）或上方（横向布局）布局内容，该布局内容可通过OH\_ArkUI\_ListItemSwipeAction\_Expand接口以编程方式展开。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionOption](capi-arkui-nativemodule-arkui-listitemswipeactionoption.md)\* option | ListItemSwipeActionOption实例。 |
| [ArkUI\_ListItemSwipeActionItem](capi-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | 待设置到起始侧的ListItemSwipeActionItem实例。不设置时，ListItem起始侧不展示侧滑操作项。 |

### OH\_ArkUI\_ListItemSwipeActionOption\_SetEnd()

```c
void OH_ArkUI_ListItemSwipeActionOption_SetEnd(ArkUI_ListItemSwipeActionOption* option, ArkUI_ListItemSwipeActionItem* item)
```

**描述：**

设置ListItemSwipeActionItem的右侧（垂直布局）或下方（横向布局）布局内容，该布局内容可通过OH\_ArkUI\_ListItemSwipeAction\_Expand接口以编程方式展开。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionOption](capi-arkui-nativemodule-arkui-listitemswipeactionoption.md)\* option | ListItemSwipeActionOption实例。 |
| [ArkUI\_ListItemSwipeActionItem](capi-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | 待设置到结束侧的ListItemSwipeActionItem实例。不设置时，ListItem结束侧不展示侧滑操作项。 |

### OH\_ArkUI\_ListItemSwipeActionOption\_SetEdgeEffect()

```c
void OH_ArkUI_ListItemSwipeActionOption_SetEdgeEffect(ArkUI_ListItemSwipeActionOption* option, ArkUI_ListItemSwipeEdgeEffect edgeEffect)
```

**描述：**

设置边缘滑动效果。需要允许滑动距离超过划出组件大小时，使用ARKUI\_LIST\_ITEM\_SWIPE\_EDGE\_EFFECT\_SPRING；需要限制滑动距离不超过划出组件大小时，使用ARKUI\_LIST\_ITEM\_SWIPE\_EDGE\_EFFECT\_NONE。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionOption](capi-arkui-nativemodule-arkui-listitemswipeactionoption.md)\* option | ListItemSwipeActionOption实例。 |
| [ArkUI\_ListItemSwipeEdgeEffect](capi-list-item-h.md#arkui_listitemswipeedgeeffect) edgeEffect | 边缘滑动效果。 |

### OH\_ArkUI\_ListItemSwipeActionOption\_GetEdgeEffect()

```c
int32_t OH_ArkUI_ListItemSwipeActionOption_GetEdgeEffect(ArkUI_ListItemSwipeActionOption* option)
```

**描述：**

获取边缘滑动效果。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionOption](capi-arkui-nativemodule-arkui-listitemswipeactionoption.md)\* option | ListItemSwipeActionOption实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 边缘滑动效果。取值包括[ARKUI\_LIST\_ITEM\_SWIPE\_EDGE\_EFFECT\_SPRING](capi-list-item-h.md#arkui_listitemswipeedgeeffect)（0）和[ARKUI\_LIST\_ITEM\_SWIPE\_EDGE\_EFFECT\_NONE](capi-list-item-h.md#arkui_listitemswipeedgeeffect)（1），默认返回值为[ARKUI\_LIST\_ITEM\_SWIPE\_EDGE\_EFFECT\_SPRING](capi-list-item-h.md#arkui_listitemswipeedgeeffect)，异常时返回-1。 |

### OH\_ArkUI\_ListItemSwipeActionOption\_SetOnOffsetChange()

```c
void OH_ArkUI_ListItemSwipeActionOption_SetOnOffsetChange(ArkUI_ListItemSwipeActionOption* option, void (*callback)(float offset))
```

**描述：**

滑动操作偏移量更改时调用的事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionOption](capi-arkui-nativemodule-arkui-listitemswipeactionoption.md)\* option | ListItemSwipeActionOption实例。 |
| void (\*callback)(float offset) | 回调事件。offset为滑动偏移量，单位vp。该回调在滑动过程中可能频繁触发，建议避免执行耗时操作。 |

### OH\_ArkUI\_ListItemSwipeActionOption\_SetOnOffsetChangeWithUserData()

```c
void OH_ArkUI_ListItemSwipeActionOption_SetOnOffsetChangeWithUserData(ArkUI_ListItemSwipeActionOption* option, void* userData, void (*callback)(float offset, void* userData))
```

**描述：**

滑动操作偏移量更改时调用的事件，回调事件会传入用户自定义数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionOption](capi-arkui-nativemodule-arkui-listitemswipeactionoption.md)\* option | ListItemSwipeActionOption实例。 |
| void\* userData | 用户自定义数据。 |
| void (\*callback)(float offset, void\* userData) | 回调事件。offset为滑动偏移量，单位vp。该回调在滑动过程中可能频繁触发，建议避免执行耗时操作。 |

### OH\_ArkUI\_ListItemSwipeAction\_Expand()

```c
int32_t OH_ArkUI_ListItemSwipeAction_Expand(ArkUI_NodeHandle node, ArkUI_ListItemSwipeActionDirection direction)
```

**描述：**

展开指定ListItem的划出菜单（即侧滑操作时展示的操作项区域）。direction为ARKUI\_LIST\_ITEM\_SWIPE\_ACTION\_DIRECTION\_START时，展开通过OH\_ArkUI\_ListItemSwipeActionOption\_SetStart设置的划出菜单；direction为ARKUI\_LIST\_ITEM\_SWIPE\_ACTION\_DIRECTION\_END时，展开通过OH\_ArkUI\_ListItemSwipeActionOption\_SetEnd设置的划出菜单。展开后的划出菜单可通过OH\_ArkUI\_ListItemSwipeAction\_Collapse接口收起。也可在应用响应用户点击"更多"等按钮后调用本接口，以编程方式展开划出菜单。

**说明** 

* 如果List组件设置了NODE\_LIST\_CACHED\_COUNT属性以启用预加载，则List显示区域外已预加载完成的ListItem支持展开；否则，List显示区域外的节点不支持展开。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | ListItem节点对象。 |
| [ArkUI\_ListItemSwipeActionDirection](capi-list-item-h.md#arkui_listitemswipeactiondirection) direction | ListItem划出菜单的展开方向。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 传入的节点对象类型错误，请检查传入的节点是否为ListItem节点。  [ARKUI\_ERROR\_CODE\_NODE\_NOT\_ON\_MAIN\_TREE](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 传入的节点未挂载到组件树上，请先将节点挂载到组件树上再执行该操作。 |

### OH\_ArkUI\_ListItemSwipeAction\_Collapse()

```c
int32_t OH_ArkUI_ListItemSwipeAction_Collapse(ArkUI_NodeHandle node)
```

**描述：**

收起由OH\_ArkUI\_ListItemSwipeAction\_Expand展开的指定ListItem的划出菜单（即侧滑操作时展示的操作项区域），也可在用户完成划出菜单操作或切换其他列表项时以编程方式调用。

**说明** 

* 如果List组件设置了NODE\_LIST\_CACHED\_COUNT属性以启用预加载，则List显示区域外已预加载完成的ListItem支持收起；否则，List显示区域外的节点不支持收起。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | ListItem节点对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 传入的节点对象类型错误，请检查传入的节点是否为ListItem节点。  [ARKUI\_ERROR\_CODE\_NODE\_NOT\_ON\_MAIN\_TREE](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 传入的节点未挂载到组件树上，请先将节点挂载到组件树上再执行该操作。 |
