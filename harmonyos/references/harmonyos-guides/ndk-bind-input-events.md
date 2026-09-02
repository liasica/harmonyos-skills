---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-bind-input-events
title: 绑定基础输入事件
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 添加事件响应 > 绑定基础输入事件
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a7cb359e9e9adc76b68e387171ed4dd8fbcb5b69dbf3f1000b2f867074f89eee
---

NDK接口提供了监听和处理基础输入事件的能力，可绑定点击事件（[NODE\_ON\_CLICK\_EVENT](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)）、触摸事件（[NODE\_TOUCH\_EVENT](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)）、鼠标事件（[NODE\_ON\_MOUSE](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)）、悬浮事件（[NODE\_ON\_HOVER\_EVENT](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)）、轴事件（[NODE\_ON\_AXIS](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)）、按键事件（[NODE\_ON\_KEY\_EVENT](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)），然后通过事件接收器中的回调函数获取事件的详细信息。

以下示例均需基于[接入ArkTS页面](ndk-access-the-arkts-page.md)章节，详细代码请参考[完整示例](ndk-bind-input-events.md#完整示例)。

## 点击事件

点击事件在用户点击组件时触发，可获取点击位置、触摸点数量、指针ID、压力值等信息。可对节点绑定如下处理函数。

```c
// 处理点击事件
void HandleClickEvent(ArkUI_UIInputEvent *inputEvent)
{
    auto pos = GetPointerPosition(inputEvent);
    auto baseInfo = GetBaseEventInfo(inputEvent);
    auto pointerCount = OH_ArkUI_PointerEvent_GetPointerCount(inputEvent);
    auto pointerId = OH_ArkUI_PointerEvent_GetPointerId(inputEvent, 0);
    auto pressure = OH_ArkUI_PointerEvent_GetPressure(inputEvent, 0);

    // 通过索引获取指针位置信息（支持多点触控场景）
    auto xByIndex = OH_ArkUI_PointerEvent_GetXByIndex(inputEvent, 0);
    auto yByIndex = OH_ArkUI_PointerEvent_GetYByIndex(inputEvent, 0);
    auto displayXByIndex = OH_ArkUI_PointerEvent_GetDisplayXByIndex(inputEvent, 0);
    auto displayYByIndex = OH_ArkUI_PointerEvent_GetDisplayYByIndex(inputEvent, 0);
    auto windowXByIndex = OH_ArkUI_PointerEvent_GetWindowXByIndex(inputEvent, 0);
    auto windowYByIndex = OH_ArkUI_PointerEvent_GetWindowYByIndex(inputEvent, 0);

    OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[NdkBindInputEvent]",
        "[%{public}s] Click: x=%{public}f, y=%{public}f, displayX=%{public}f, displayY=%{public}f, "
        "windowX=%{public}f, windowY=%{public}f, xByIndex=%{public}f, yByIndex=%{public}f, "
        "displayXByIndex=%{public}f, displayYByIndex=%{public}f, windowXByIndex=%{public}f, "
        "windowYByIndex=%{public}f, pointerCount=%{public}d, pointerId=%{public}d, "
        "pressure=%{public}f, action=%{public}d, eventTime=%{public}lld, sourceType=%{public}d, type=%{public}d",
        eventName_.c_str(), pos.x, pos.y, pos.displayX, pos.displayY, pos.windowX, pos.windowY,
        xByIndex, yByIndex, displayXByIndex, displayYByIndex, windowXByIndex, windowYByIndex,
        pointerCount, pointerId, pressure, baseInfo.action, baseInfo.eventTime,
        baseInfo.sourceType, baseInfo.type);
}
```

从API version 18开始，新增[NODE\_ON\_CLICK\_EVENT](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)枚举。节点自身可以注册NODE\_ON\_CLICK\_EVENT事件监听，以响应上述处理函数。

```c
nativeModule_->registerNodeEvent(handle_, NODE_ON_CLICK_EVENT, 0, this);
```

## 触摸事件

触摸事件在用户触摸屏幕时触发，除了点击事件的信息外，还可获取触摸区域宽度和高度。可对节点绑定如下处理函数。

```c
// 处理触摸事件
void HandleTouchEvent(ArkUI_UIInputEvent *inputEvent)
{
    auto pos = GetPointerPosition(inputEvent);
    auto baseInfo = GetBaseEventInfo(inputEvent);
    auto pointerCount = OH_ArkUI_PointerEvent_GetPointerCount(inputEvent);
    auto pointerId = OH_ArkUI_PointerEvent_GetPointerId(inputEvent, 0);
    auto pressure = OH_ArkUI_PointerEvent_GetPressure(inputEvent, 0);
    auto touchAreaWidth = OH_ArkUI_PointerEvent_GetTouchAreaWidth(inputEvent, 0);
    auto touchAreaHeight = OH_ArkUI_PointerEvent_GetTouchAreaHeight(inputEvent, 0);

    // 通过索引获取指针位置信息（支持多点触控场景）
    auto xByIndex = OH_ArkUI_PointerEvent_GetXByIndex(inputEvent, 0);
    auto yByIndex = OH_ArkUI_PointerEvent_GetYByIndex(inputEvent, 0);
    auto displayXByIndex = OH_ArkUI_PointerEvent_GetDisplayXByIndex(inputEvent, 0);
    auto displayYByIndex = OH_ArkUI_PointerEvent_GetDisplayYByIndex(inputEvent, 0);
    auto windowXByIndex = OH_ArkUI_PointerEvent_GetWindowXByIndex(inputEvent, 0);
    auto windowYByIndex = OH_ArkUI_PointerEvent_GetWindowYByIndex(inputEvent, 0);

    OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[NdkBindInputEvent]",
        "[%{public}s] Touch: x=%{public}f, y=%{public}f, displayX=%{public}f, displayY=%{public}f, "
        "windowX=%{public}f, windowY=%{public}f, xByIndex=%{public}f, yByIndex=%{public}f, "
        "displayXByIndex=%{public}f, displayYByIndex=%{public}f, windowXByIndex=%{public}f, "
        "windowYByIndex=%{public}f, pointerCount=%{public}d, pointerId=%{public}d, "
        "pressure=%{public}f, touchAreaWidth=%{public}f, touchAreaHeight=%{public}f, "
        "action=%{public}d, eventTime=%{public}lld, sourceType=%{public}d, type=%{public}d",
        eventName_.c_str(), pos.x, pos.y, pos.displayX, pos.displayY, pos.windowX, pos.windowY,
        xByIndex, yByIndex, displayXByIndex, displayYByIndex, windowXByIndex, windowYByIndex,
        pointerCount, pointerId, pressure, touchAreaWidth, touchAreaHeight, baseInfo.action,
        baseInfo.eventTime, baseInfo.sourceType, baseInfo.type);
}
```

节点自身需要注册[NODE\_TOUCH\_EVENT](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)事件监听，以响应上述处理函数。

```c
nativeModule_->registerNodeEvent(handle_, NODE_TOUCH_EVENT, 0, this);
```

## 鼠标事件

鼠标事件在使用鼠标操作时触发，可获取鼠标按键类型、鼠标动作类型、滚轮移动增量等信息。可对节点绑定如下处理函数。

```c
// 处理鼠标事件
void HandleMouseEvent(ArkUI_UIInputEvent *inputEvent)
{
    auto pos = GetPointerPosition(inputEvent);
    auto baseInfo = GetBaseEventInfo(inputEvent);
    auto button = OH_ArkUI_MouseEvent_GetMouseButton(inputEvent);
    auto mouseAction = OH_ArkUI_MouseEvent_GetMouseAction(inputEvent);
    auto rawDeltaX = OH_ArkUI_MouseEvent_GetRawDeltaX(inputEvent);
    auto rawDeltaY = OH_ArkUI_MouseEvent_GetRawDeltaY(inputEvent);
    auto buttonCount = GetPressedButtonsCount(inputEvent);

    OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[NdkBindInputEvent]",
        "[%{public}s] Mouse: x=%{public}f, y=%{public}f, displayX=%{public}f, displayY=%{public}f, "
        "windowX=%{public}f, windowY=%{public}f, button=%{public}d, mouseAction=%{public}d, "
        "pressedButtonsCount=%{public}d, rawDeltaX=%{public}f, rawDeltaY=%{public}f, "
        "action=%{public}d, eventTime=%{public}lld, sourceType=%{public}d, type=%{public}d",
        eventName_.c_str(), pos.x, pos.y, pos.displayX, pos.displayY, pos.windowX, pos.windowY,
        button, mouseAction, buttonCount, rawDeltaX, rawDeltaY, baseInfo.action,
        baseInfo.eventTime, baseInfo.sourceType, baseInfo.type);
}
```

节点自身需要注册[NODE\_ON\_MOUSE](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)事件监听，以响应上述处理函数。

```c
nativeModule_->registerNodeEvent(handle_, NODE_ON_MOUSE, 0, this);
```

## 悬浮事件

悬浮事件在鼠标指针移至组件上方或远离组件时触发，可获取悬浮状态。可对节点绑定如下处理函数。

```c
// 处理悬浮事件
void HandleHoverEvent(ArkUI_UIInputEvent *inputEvent)
{
    auto pos = GetPointerPosition(inputEvent);
    auto baseInfo = GetBaseEventInfo(inputEvent);
    auto isHovered = OH_ArkUI_HoverEvent_IsHovered(inputEvent);

    OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[NdkBindInputEvent]",
        "[%{public}s] Hover: x=%{public}f, y=%{public}f, displayX=%{public}f, displayY=%{public}f, "
        "windowX=%{public}f, windowY=%{public}f, isHovered=%{public}d, action=%{public}d, "
        "eventTime=%{public}lld, sourceType=%{public}d, type=%{public}d",
        eventName_.c_str(), pos.x, pos.y, pos.displayX, pos.displayY, pos.windowX, pos.windowY,
        isHovered, baseInfo.action, baseInfo.eventTime, baseInfo.sourceType, baseInfo.type);
}
```

从API version 17开始，新增[NODE\_ON\_HOVER\_EVENT](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)枚举。节点自身可以注册NODE\_ON\_HOVER\_EVENT事件监听，以响应上述处理函数。

```c
nativeModule_->registerNodeEvent(handle_, NODE_ON_HOVER_EVENT, 0, this);
```

## 轴事件

轴事件通过鼠标滚轮、游戏摇杆等设备触发，可获取轴动作类型、垂直轴值、水平轴值、缩放比例、滚动步长等信息。可对节点绑定如下处理函数。

```c
// 处理轴事件
void HandleAxisEvent(ArkUI_UIInputEvent *inputEvent)
{
    auto baseInfo = GetBaseEventInfo(inputEvent);
    auto axisAction = OH_ArkUI_AxisEvent_GetAxisAction(inputEvent);
    auto verticalAxis = OH_ArkUI_AxisEvent_GetVerticalAxisValue(inputEvent);
    auto horizontalAxis = OH_ArkUI_AxisEvent_GetHorizontalAxisValue(inputEvent);
    auto pinchAxisScale = OH_ArkUI_AxisEvent_GetPinchAxisScaleValue(inputEvent);
    auto scrollStep = OH_ArkUI_AxisEvent_GetScrollStep(inputEvent);

    OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[NdkBindInputEvent]",
        "[%{public}s] Axis: axisAction=%{public}d, verticalAxis=%{public}f, horizontalAxis=%{public}f, "
        "pinchAxisScale=%{public}f, scrollStep=%{public}d, action=%{public}d, "
        "eventTime=%{public}lld, sourceType=%{public}d, type=%{public}d",
        eventName_.c_str(), axisAction, verticalAxis, horizontalAxis, pinchAxisScale, scrollStep,
        baseInfo.action, baseInfo.eventTime, baseInfo.sourceType, baseInfo.type);
}
```

从API version 17开始，新增[NODE\_ON\_AXIS](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)枚举。节点自身可以注册NODE\_ON\_AXIS事件监听，以响应上述处理函数。

```c
nativeModule_->registerNodeEvent(handle_, NODE_ON_AXIS, 0, this);
```

## 按键事件

按键事件在用户按下或释放键盘按键时触发，可获取按键类型、按键动作、按下的键、修饰键状态、设备ID等信息。组件需要先获取焦点才能响应按键事件。可对节点绑定如下处理函数。

```c
// 处理按键事件
void HandleKeyEvent(ArkUI_UIInputEvent *inputEvent)
{
    auto type = OH_ArkUI_KeyEvent_GetType(inputEvent);
    auto baseInfo = GetBaseEventInfo(inputEvent);
    auto deviceId = OH_ArkUI_UIInputEvent_GetDeviceId(inputEvent);
    auto keyInfo = GetKeyInfo(inputEvent);

    OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[NdkBindInputEvent]",
        "[%{public}s] Key: type=%{public}d, action=%{public}d, pressedKey=%{public}d, "
        "modifierKeys=%{public}llu, deviceId=%{public}d, eventTime=%{public}lld, sourceType=%{public}d",
        eventName_.c_str(), type, baseInfo.action, keyInfo.pressedKey, keyInfo.modifierKeys,
        deviceId, baseInfo.eventTime, baseInfo.sourceType);
}
```

设置节点为可聚焦，并绑定点击事件，在点击时请求焦点。同时节点自身需要注册[NODE\_ON\_KEY\_EVENT](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)事件监听，以响应上述处理函数。

```c
// 设置为可聚焦，以便接收按键事件
ArkUI_NumberValue focusable[] = {1};
ArkUI_AttributeItem focusableItem = {focusable, 1};
nativeModule_->setAttribute(handle_, NODE_FOCUSABLE, &focusableItem);

// 注册点击事件，点击时请求焦点
nativeModule_->registerNodeEvent(handle_, NODE_ON_CLICK_EVENT, 0, this);

// 注册按键事件
nativeModule_->registerNodeEvent(handle_, NODE_ON_KEY_EVENT, 0, this);
```

## 完整示例

1. 定义基础输入事件的数据结构。

   ```c
   // InputEventTypes.h
   // 输入事件相关的类型定义和辅助函数

   #ifndef MYAPPLICATION_INPUTEVENTTYPES_H
   #define MYAPPLICATION_INPUTEVENTTYPES_H

   #include <cstdint>

   namespace NativeModule {

   // 基础事件信息结构体
   struct BaseEventInfo {
       int32_t action;
       int64_t eventTime;
       int32_t sourceType;
       int32_t type;
   };

   // 指针坐标信息结构体
   struct PointerPosition {
       float x;
       float y;
       float displayX;
       float displayY;
       float windowX;
       float windowY;
   };

   // 按键信息结构体
   struct KeyInfo {
       int32_t pressedKey;
       uint64_t modifierKeys;
   };

   } // namespace NativeModule

   #endif // MYAPPLICATION_INPUTEVENTTYPES_H
   ```
2. 注册各种基础输入事件并实现相应事件的监听。

   ```c
   // NormalTextListExample.h
   // 输入事件示例，展示基础输入事件的绑定和处理

   #ifndef MYAPPLICATION_NORMALTEXTLISTEXAMPLE_H
   #define MYAPPLICATION_NORMALTEXTLISTEXAMPLE_H

   #include "ArkUIBaseNode.h"
   #include "ArkUIListItemNode.h"
   #include "ArkUIListNode.h"
   #include "ArkUITextNode.h"
   #include "InputEventTypes.h"
   #include <arkui/native_key_event.h>
   #include <hilog/log.h>
   #include <string>

   namespace NativeModule {

   // 常量定义
   const unsigned int LOG_PRINT_DOMAIN = 0xF811;
   const unsigned int ITEM_HEIGHT = 100;
   const unsigned int FONT_SIZE = 16;

   // 自定义列表项类，用于处理不同类型的输入事件
   class InputEventListItem : public ArkUIListItemNode {
   public:
       enum EventType {
           CLICK_EVENT,
           TOUCH_EVENT,
           MOUSE_EVENT,
           HOVER_EVENT,
           AXIS_EVENT,
           KEY_EVENT
       };

       InputEventListItem(const std::string& eventName, uint32_t bgColor, EventType eventType)
           : eventName_(eventName), eventType_(eventType)
       {
           SetPercentWidth(1);
           SetHeight(ITEM_HEIGHT);
           SetBackgroundColor(bgColor);

           auto textNode = std::make_shared<ArkUITextNode>();
           textNode->SetTextContent(eventName);
           textNode->SetFontSize(FONT_SIZE);
           textNode->SetFontColor(0xFFFFFFFF);
           textNode->SetTextAlign(ARKUI_TEXT_ALIGNMENT_CENTER);
           textNode->SetPercentWidth(1);
           AddChild(textNode);

           // 注册事件监听器
           RegisterEventReceiver();
       }

   private:
       // 注册事件接收器和回调
       void RegisterEventReceiver()
       {
           if (!handle_) {
               return;
           }
           nativeModule_->addNodeEventReceiver(handle_, [](ArkUI_NodeEvent *event) {
               auto *item = static_cast<InputEventListItem*>(OH_ArkUI_NodeEvent_GetUserData(event));
               if (item) {
                   item->HandleEvent(event);
               }
           });
           RegisterEventByType();
       }

       // 根据事件类型注册具体事件
       void RegisterEventByType()
       {
           switch (eventType_) {
               case CLICK_EVENT:
                   RegisterClickEvent();
                   break;
               case TOUCH_EVENT:
                   RegisterTouchEvent();
                   break;
               case MOUSE_EVENT:
                   RegisterMouseEvent();
                   break;
               case HOVER_EVENT:
                   RegisterHoverEvent();
                   break;
               case AXIS_EVENT:
                   RegisterAxisEvent();
                   break;
               case KEY_EVENT:
                   RegisterKeyEvent();
                   break;
           }
       }

       // 注册点击事件
       void RegisterClickEvent()
       {
           nativeModule_->registerNodeEvent(handle_, NODE_ON_CLICK_EVENT, 0, this);
       }

       // 注册触摸事件
       void RegisterTouchEvent()
       {
           nativeModule_->registerNodeEvent(handle_, NODE_TOUCH_EVENT, 0, this);
       }

       // 注册鼠标事件
       void RegisterMouseEvent()
       {
           // 鼠标事件（点击、移动、释放等）
           nativeModule_->registerNodeEvent(handle_, NODE_ON_MOUSE, 0, this);
       }

       // 注册悬浮事件
       void RegisterHoverEvent()
       {
           nativeModule_->registerNodeEvent(handle_, NODE_ON_HOVER_EVENT, 0, this);
       }

       // 注册轴事件
       void RegisterAxisEvent()
       {
           // 轴事件：鼠标滚轮滚动时触发
           nativeModule_->registerNodeEvent(handle_, NODE_ON_AXIS, 0, this);
       }

       // 注册按键事件
       void RegisterKeyEvent()
       {
           // 设置为可聚焦，以便接收按键事件
           ArkUI_NumberValue focusable[] = {1};
           ArkUI_AttributeItem focusableItem = {focusable, 1};
           nativeModule_->setAttribute(handle_, NODE_FOCUSABLE, &focusableItem);

           // 注册点击事件，点击时请求焦点
           nativeModule_->registerNodeEvent(handle_, NODE_ON_CLICK_EVENT, 0, this);

           // 注册按键事件
           nativeModule_->registerNodeEvent(handle_, NODE_ON_KEY_EVENT, 0, this);
       }

       // 事件分发处理
       void HandleEvent(ArkUI_NodeEvent *event)
       {
           auto eventType = OH_ArkUI_NodeEvent_GetEventType(event);
           auto *inputEvent = OH_ArkUI_NodeEvent_GetInputEvent(event);
           auto uiType = OH_ArkUI_UIInputEvent_GetType(inputEvent);

           DispatchEvent(eventType, uiType, inputEvent);
       }

       // 根据事件类型分发到具体处理函数
       void DispatchEvent(int32_t eventType, int32_t uiType, ArkUI_UIInputEvent *inputEvent)
       {
           switch (eventType_) {
               case CLICK_EVENT:
                   if (eventType == NODE_ON_CLICK_EVENT) {
                       HandleClickEvent(inputEvent);
                   }
                   break;
               case TOUCH_EVENT:
                   if (eventType == NODE_TOUCH_EVENT && uiType == ARKUI_UIINPUTEVENT_TYPE_TOUCH) {
                       HandleTouchEvent(inputEvent);
                   }
                   break;
               case MOUSE_EVENT:
                   // 鼠标事件（点击、移动、释放等）
                   if (eventType == NODE_ON_MOUSE && uiType == ARKUI_UIINPUTEVENT_TYPE_MOUSE) {
                       HandleMouseEvent(inputEvent);
                   }
                   break;
               case HOVER_EVENT:
                   if (eventType == NODE_ON_HOVER_EVENT) {
                       HandleHoverEvent(inputEvent);
                   }
                   break;
               case AXIS_EVENT:
                   // 鼠标滚轮滚动或触控板手势时触发
                   if (eventType == NODE_ON_AXIS && uiType == ARKUI_UIINPUTEVENT_TYPE_AXIS) {
                       HandleAxisEvent(inputEvent);
                   }
                   break;
               case KEY_EVENT:
                   if (eventType == NODE_ON_CLICK_EVENT) {
                       // 点击时请求焦点
                       ArkUI_NumberValue requestFocus[] = {1};
                       ArkUI_AttributeItem requestFocusItem = {requestFocus, 1};
                       nativeModule_->setAttribute(handle_, NODE_FOCUS_STATUS, &requestFocusItem);

                       OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[NdkBindInputEvent]",
                           "[%{public}s] Focus requested", eventName_.c_str());
                   } else if (eventType == NODE_ON_KEY_EVENT && uiType == ARKUI_UIINPUTEVENT_TYPE_KEY) {
                       // 处理按键事件
                       HandleKeyEvent(inputEvent);
                   }
                   break;
           }
       }

       // 获取基础事件信息
       BaseEventInfo GetBaseEventInfo(ArkUI_UIInputEvent *inputEvent)
       {
           BaseEventInfo info;
           info.action = OH_ArkUI_UIInputEvent_GetAction(inputEvent);
           info.eventTime = OH_ArkUI_UIInputEvent_GetEventTime(inputEvent);
           info.sourceType = OH_ArkUI_UIInputEvent_GetSourceType(inputEvent);
           info.type = OH_ArkUI_UIInputEvent_GetType(inputEvent);
           return info;
       }

       // 获取事件位置信息
       PointerPosition GetPointerPosition(ArkUI_UIInputEvent *inputEvent)
       {
           PointerPosition pos;
           pos.x = OH_ArkUI_PointerEvent_GetX(inputEvent);
           pos.y = OH_ArkUI_PointerEvent_GetY(inputEvent);
           pos.displayX = OH_ArkUI_PointerEvent_GetDisplayX(inputEvent);
           pos.displayY = OH_ArkUI_PointerEvent_GetDisplayY(inputEvent);
           pos.windowX = OH_ArkUI_PointerEvent_GetWindowX(inputEvent);
           pos.windowY = OH_ArkUI_PointerEvent_GetWindowY(inputEvent);
           return pos;
       }

       // 打印事件位置信息
       void LogPointerPosition(const char *eventName, const PointerPosition &pos)
       {
           OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[NdkBindInputEvent]",
               "[%{public}s] x=%{public}f, y=%{public}f, displayX=%{public}f, displayY=%{public}f, "
               "windowX=%{public}f, windowY=%{public}f",
               eventName, pos.x, pos.y, pos.displayX, pos.displayY, pos.windowX, pos.windowY);
       }

       // 处理点击事件
       void HandleClickEvent(ArkUI_UIInputEvent *inputEvent)
       {
           auto pos = GetPointerPosition(inputEvent);
           auto baseInfo = GetBaseEventInfo(inputEvent);
           auto pointerCount = OH_ArkUI_PointerEvent_GetPointerCount(inputEvent);
           auto pointerId = OH_ArkUI_PointerEvent_GetPointerId(inputEvent, 0);
           auto pressure = OH_ArkUI_PointerEvent_GetPressure(inputEvent, 0);

           // 通过索引获取指针位置信息（支持多点触控场景）
           auto xByIndex = OH_ArkUI_PointerEvent_GetXByIndex(inputEvent, 0);
           auto yByIndex = OH_ArkUI_PointerEvent_GetYByIndex(inputEvent, 0);
           auto displayXByIndex = OH_ArkUI_PointerEvent_GetDisplayXByIndex(inputEvent, 0);
           auto displayYByIndex = OH_ArkUI_PointerEvent_GetDisplayYByIndex(inputEvent, 0);
           auto windowXByIndex = OH_ArkUI_PointerEvent_GetWindowXByIndex(inputEvent, 0);
           auto windowYByIndex = OH_ArkUI_PointerEvent_GetWindowYByIndex(inputEvent, 0);

           OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[NdkBindInputEvent]",
               "[%{public}s] Click: x=%{public}f, y=%{public}f, displayX=%{public}f, displayY=%{public}f, "
               "windowX=%{public}f, windowY=%{public}f, xByIndex=%{public}f, yByIndex=%{public}f, "
               "displayXByIndex=%{public}f, displayYByIndex=%{public}f, windowXByIndex=%{public}f, "
               "windowYByIndex=%{public}f, pointerCount=%{public}d, pointerId=%{public}d, "
               "pressure=%{public}f, action=%{public}d, eventTime=%{public}lld, sourceType=%{public}d, type=%{public}d",
               eventName_.c_str(), pos.x, pos.y, pos.displayX, pos.displayY, pos.windowX, pos.windowY,
               xByIndex, yByIndex, displayXByIndex, displayYByIndex, windowXByIndex, windowYByIndex,
               pointerCount, pointerId, pressure, baseInfo.action, baseInfo.eventTime,
               baseInfo.sourceType, baseInfo.type);
       }

       // 处理触摸事件
       void HandleTouchEvent(ArkUI_UIInputEvent *inputEvent)
       {
           auto pos = GetPointerPosition(inputEvent);
           auto baseInfo = GetBaseEventInfo(inputEvent);
           auto pointerCount = OH_ArkUI_PointerEvent_GetPointerCount(inputEvent);
           auto pointerId = OH_ArkUI_PointerEvent_GetPointerId(inputEvent, 0);
           auto pressure = OH_ArkUI_PointerEvent_GetPressure(inputEvent, 0);
           auto touchAreaWidth = OH_ArkUI_PointerEvent_GetTouchAreaWidth(inputEvent, 0);
           auto touchAreaHeight = OH_ArkUI_PointerEvent_GetTouchAreaHeight(inputEvent, 0);

           // 通过索引获取指针位置信息（支持多点触控场景）
           auto xByIndex = OH_ArkUI_PointerEvent_GetXByIndex(inputEvent, 0);
           auto yByIndex = OH_ArkUI_PointerEvent_GetYByIndex(inputEvent, 0);
           auto displayXByIndex = OH_ArkUI_PointerEvent_GetDisplayXByIndex(inputEvent, 0);
           auto displayYByIndex = OH_ArkUI_PointerEvent_GetDisplayYByIndex(inputEvent, 0);
           auto windowXByIndex = OH_ArkUI_PointerEvent_GetWindowXByIndex(inputEvent, 0);
           auto windowYByIndex = OH_ArkUI_PointerEvent_GetWindowYByIndex(inputEvent, 0);

           OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[NdkBindInputEvent]",
               "[%{public}s] Touch: x=%{public}f, y=%{public}f, displayX=%{public}f, displayY=%{public}f, "
               "windowX=%{public}f, windowY=%{public}f, xByIndex=%{public}f, yByIndex=%{public}f, "
               "displayXByIndex=%{public}f, displayYByIndex=%{public}f, windowXByIndex=%{public}f, "
               "windowYByIndex=%{public}f, pointerCount=%{public}d, pointerId=%{public}d, "
               "pressure=%{public}f, touchAreaWidth=%{public}f, touchAreaHeight=%{public}f, "
               "action=%{public}d, eventTime=%{public}lld, sourceType=%{public}d, type=%{public}d",
               eventName_.c_str(), pos.x, pos.y, pos.displayX, pos.displayY, pos.windowX, pos.windowY,
               xByIndex, yByIndex, displayXByIndex, displayYByIndex, windowXByIndex, windowYByIndex,
               pointerCount, pointerId, pressure, touchAreaWidth, touchAreaHeight, baseInfo.action,
               baseInfo.eventTime, baseInfo.sourceType, baseInfo.type);
       }

       // 处理鼠标事件
       void HandleMouseEvent(ArkUI_UIInputEvent *inputEvent)
       {
           auto pos = GetPointerPosition(inputEvent);
           auto baseInfo = GetBaseEventInfo(inputEvent);
           auto button = OH_ArkUI_MouseEvent_GetMouseButton(inputEvent);
           auto mouseAction = OH_ArkUI_MouseEvent_GetMouseAction(inputEvent);
           auto rawDeltaX = OH_ArkUI_MouseEvent_GetRawDeltaX(inputEvent);
           auto rawDeltaY = OH_ArkUI_MouseEvent_GetRawDeltaY(inputEvent);
           auto buttonCount = GetPressedButtonsCount(inputEvent);

           OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[NdkBindInputEvent]",
               "[%{public}s] Mouse: x=%{public}f, y=%{public}f, displayX=%{public}f, displayY=%{public}f, "
               "windowX=%{public}f, windowY=%{public}f, button=%{public}d, mouseAction=%{public}d, "
               "pressedButtonsCount=%{public}d, rawDeltaX=%{public}f, rawDeltaY=%{public}f, "
               "action=%{public}d, eventTime=%{public}lld, sourceType=%{public}d, type=%{public}d",
               eventName_.c_str(), pos.x, pos.y, pos.displayX, pos.displayY, pos.windowX, pos.windowY,
               button, mouseAction, buttonCount, rawDeltaX, rawDeltaY, baseInfo.action,
               baseInfo.eventTime, baseInfo.sourceType, baseInfo.type);
       }

       // 获取按下的鼠标按键数量
       int32_t GetPressedButtonsCount(ArkUI_UIInputEvent *inputEvent)
       {
           int32_t pressedButtons[5] = {};
           int32_t length = 5;
           OH_ArkUI_MouseEvent_GetPressedButtons(inputEvent, pressedButtons, &length);
           return length;
       }

       // 处理悬浮事件
       void HandleHoverEvent(ArkUI_UIInputEvent *inputEvent)
       {
           auto pos = GetPointerPosition(inputEvent);
           auto baseInfo = GetBaseEventInfo(inputEvent);
           auto isHovered = OH_ArkUI_HoverEvent_IsHovered(inputEvent);

           OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[NdkBindInputEvent]",
               "[%{public}s] Hover: x=%{public}f, y=%{public}f, displayX=%{public}f, displayY=%{public}f, "
               "windowX=%{public}f, windowY=%{public}f, isHovered=%{public}d, action=%{public}d, "
               "eventTime=%{public}lld, sourceType=%{public}d, type=%{public}d",
               eventName_.c_str(), pos.x, pos.y, pos.displayX, pos.displayY, pos.windowX, pos.windowY,
               isHovered, baseInfo.action, baseInfo.eventTime, baseInfo.sourceType, baseInfo.type);
       }

       // 处理轴事件
       void HandleAxisEvent(ArkUI_UIInputEvent *inputEvent)
       {
           auto baseInfo = GetBaseEventInfo(inputEvent);
           auto axisAction = OH_ArkUI_AxisEvent_GetAxisAction(inputEvent);
           auto verticalAxis = OH_ArkUI_AxisEvent_GetVerticalAxisValue(inputEvent);
           auto horizontalAxis = OH_ArkUI_AxisEvent_GetHorizontalAxisValue(inputEvent);
           auto pinchAxisScale = OH_ArkUI_AxisEvent_GetPinchAxisScaleValue(inputEvent);
           auto scrollStep = OH_ArkUI_AxisEvent_GetScrollStep(inputEvent);

           OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[NdkBindInputEvent]",
               "[%{public}s] Axis: axisAction=%{public}d, verticalAxis=%{public}f, horizontalAxis=%{public}f, "
               "pinchAxisScale=%{public}f, scrollStep=%{public}d, action=%{public}d, "
               "eventTime=%{public}lld, sourceType=%{public}d, type=%{public}d",
               eventName_.c_str(), axisAction, verticalAxis, horizontalAxis, pinchAxisScale, scrollStep,
               baseInfo.action, baseInfo.eventTime, baseInfo.sourceType, baseInfo.type);
       }

       // 处理按键事件
       void HandleKeyEvent(ArkUI_UIInputEvent *inputEvent)
       {
           auto type = OH_ArkUI_KeyEvent_GetType(inputEvent);
           auto baseInfo = GetBaseEventInfo(inputEvent);
           auto deviceId = OH_ArkUI_UIInputEvent_GetDeviceId(inputEvent);
           auto keyInfo = GetKeyInfo(inputEvent);

           OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[NdkBindInputEvent]",
               "[%{public}s] Key: type=%{public}d, action=%{public}d, pressedKey=%{public}d, "
               "modifierKeys=%{public}llu, deviceId=%{public}d, eventTime=%{public}lld, sourceType=%{public}d",
               eventName_.c_str(), type, baseInfo.action, keyInfo.pressedKey, keyInfo.modifierKeys,
               deviceId, baseInfo.eventTime, baseInfo.sourceType);
       }

       // 获取按键信息
       KeyInfo GetKeyInfo(ArkUI_UIInputEvent *inputEvent)
       {
           KeyInfo info;
           int32_t pressedKeys[10] = {};
           int32_t length = 10;
           OH_ArkUI_UIInputEvent_GetPressedKeys(inputEvent, pressedKeys, &length);
           info.pressedKey = length > 0 ? pressedKeys[0] : -1;

           uint64_t modifierKeys = 0;
           OH_ArkUI_UIInputEvent_GetModifierKeyStates(inputEvent, &modifierKeys);
           info.modifierKeys = modifierKeys;

           return info;
       }

       std::string eventName_;
       EventType eventType_;
   };

   // 创建列表项
   std::shared_ptr<InputEventListItem> CreateEventListItem(
       const std::string& name, uint32_t color, InputEventListItem::EventType type)
   {
       return std::make_shared<InputEventListItem>(name, color, type);
   }

   // 创建按键事件按钮
   ArkUI_NodeHandle CreateKeyEventButton(const char* name, uint32_t bgColor)
   {
       auto* nodeAPI = NativeModule::NativeModuleInstance::GetInstance()->GetNativeNodeAPI();
       ArkUI_NodeHandle buttonHandle = nodeAPI->createNode(ARKUI_NODE_BUTTON);

       // 设置按钮属性
       ArkUI_AttributeItem idItem = {.string = "keyEventButton"};
       nodeAPI->setAttribute(buttonHandle, NODE_ID, &idItem);

       ArkUI_NumberValue typeValue[] = {{.i32 = 0}};
       ArkUI_AttributeItem typeItem = {typeValue, 1};
       nodeAPI->setAttribute(buttonHandle, NODE_BUTTON_TYPE, &typeItem);

       ArkUI_NumberValue widthValue[] = {{.f32 = 1.0f}};
       ArkUI_AttributeItem widthItem = {widthValue, 1};
       nodeAPI->setAttribute(buttonHandle, NODE_WIDTH_PERCENT, &widthItem);

       ArkUI_NumberValue heightValue[] = {{.f32 = 100.0f}};
       ArkUI_AttributeItem heightItem = {heightValue, 1};
       nodeAPI->setAttribute(buttonHandle, NODE_HEIGHT, &heightItem);

       ArkUI_NumberValue bgValue[] = {{.u32 = bgColor}};
       ArkUI_AttributeItem bgItem = {bgValue, 1};
       nodeAPI->setAttribute(buttonHandle, NODE_BACKGROUND_COLOR, &bgItem);

       ArkUI_AttributeItem labelItem = {.string = name};
       nodeAPI->setAttribute(buttonHandle, NODE_BUTTON_LABEL, &labelItem);

       ArkUI_NumberValue focusable[] = {{.i32 = 1}};
       ArkUI_AttributeItem focusableItem = {focusable, 1};
       nodeAPI->setAttribute(buttonHandle, NODE_FOCUSABLE, &focusableItem);

       // 注册事件
       nodeAPI->registerNodeEvent(buttonHandle, NODE_ON_CLICK_EVENT, 0, buttonHandle);
       nodeAPI->registerNodeEvent(buttonHandle, NODE_ON_KEY_EVENT, 0, buttonHandle);

       return buttonHandle;
   }

   // 处理按键按钮的点击事件
   void HandleKeyEventButtonClick(ArkUI_NodeEvent *event)
   {
       ArkUI_NumberValue requestFocus[] = {{.i32 = 1}};
       ArkUI_AttributeItem requestFocusItem = {requestFocus, 1};
       auto* nativeModule = NativeModule::NativeModuleInstance::GetInstance()->GetNativeNodeAPI();
       nativeModule->setAttribute(
           OH_ArkUI_NodeEvent_GetNodeHandle(event), NODE_FOCUS_STATUS, &requestFocusItem);

       OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[NdkBindInputEvent]",
           "[Key Event Button] Focus requested via click");
   }

   // 处理按键按钮的按键事件
   void HandleKeyEventButtonKey(ArkUI_NodeEvent *event)
   {
       auto *inputEvent = OH_ArkUI_NodeEvent_GetInputEvent(event);
       auto type = OH_ArkUI_KeyEvent_GetType(inputEvent);
       auto action = OH_ArkUI_UIInputEvent_GetAction(inputEvent);
       auto deviceId = OH_ArkUI_UIInputEvent_GetDeviceId(inputEvent);

       int32_t pressedKeys[10] = {};
       int32_t length = 10;
       OH_ArkUI_UIInputEvent_GetPressedKeys(inputEvent, pressedKeys, &length);
       auto pressedKey = length > 0 ? pressedKeys[0] : -1;

       uint64_t modifierKeys = 0;
       OH_ArkUI_UIInputEvent_GetModifierKeyStates(inputEvent, &modifierKeys);

       OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[NdkBindInputEvent]",
           "[Key Event Button] Key: type=%{public}d, action=%{public}d, pressedKey=%{public}d, "
           "modifierKeys=%{public}llu, deviceId=%{public}d",
           type, action, pressedKey, modifierKeys, deviceId);
   }

   // 注册按键按钮的事件接收器
   void RegisterKeyEventButtonReceiver(ArkUI_NodeHandle buttonHandle)
   {
       auto* nodeAPI = NativeModule::NativeModuleInstance::GetInstance()->GetNativeNodeAPI();
       nodeAPI->addNodeEventReceiver(buttonHandle, [](ArkUI_NodeEvent *event) {
           auto eventType = OH_ArkUI_NodeEvent_GetEventType(event);
           auto uiType = OH_ArkUI_UIInputEvent_GetType(OH_ArkUI_NodeEvent_GetInputEvent(event));

           if (eventType == NODE_ON_CLICK_EVENT) {
               HandleKeyEventButtonClick(event);
           } else if (eventType == NODE_ON_KEY_EVENT && uiType == ARKUI_UIINPUTEVENT_TYPE_KEY) {
               HandleKeyEventButtonKey(event);
           }
       });
   }

   // 添加所有事件列表项到列表
   void AddEventListItems(std::shared_ptr<ArkUIListNode> list)
   {
       auto* nodeAPI = NativeModule::NativeModuleInstance::GetInstance()->GetNativeNodeAPI();

       // 点击事件
       list->AddChild(CreateEventListItem("Click Event - Tap to test", 0xFF1976D2,
           InputEventListItem::CLICK_EVENT));
       // 触摸事件
       list->AddChild(CreateEventListItem("Touch Event - Touch to test", 0xFF9E9E9E,
           InputEventListItem::TOUCH_EVENT));
       // 鼠标事件
       list->AddChild(CreateEventListItem("Mouse Event - Mouse over/click to test", 0xFF1976D2,
           InputEventListItem::MOUSE_EVENT));
       // 悬浮事件
       list->AddChild(CreateEventListItem("Hover Event - Hover to test", 0xFF9E9E9E,
           InputEventListItem::HOVER_EVENT));
       // 轴事件
       list->AddChild(CreateEventListItem("Axis Event - Use mouse wheel", 0xFF1976D2,
           InputEventListItem::AXIS_EVENT));
       // 按键事件
       ArkUI_NodeHandle keyButton = CreateKeyEventButton("Key Event - Click to focus, then press keys", 0xFF9E9E9E);
       RegisterKeyEventButtonReceiver(keyButton);
       nodeAPI->addChild(list->GetHandle(), keyButton);
   }

   // 创建输入事件列表的主函数
   std::shared_ptr<ArkUIBaseNode> CreateTextListExample()
   {
       auto list = std::make_shared<ArkUIListNode>();
       list->SetPercentWidth(1);
       list->SetPercentHeight(1);
       list->SetScrollBarState(true);
       // 添加所有事件列表项
       AddEventListItems(list);
       return list;
   }

   } // namespace NativeModule

   #endif // MYAPPLICATION_NORMALTEXTLISTEXAMPLE_H
   ```

   由于使用了日志打印接口[OH\_LOG\_Print](../harmonyos-references/capi-log-h.md#oh_log_print)，需要在CMakeLists.txt中添加对libhilog\_ndk.z.so的引用。

   ```text
   add_library(entry SHARED napi_init.cpp NativeEntry.cpp)
   target_link_libraries(entry PUBLIC libace_napi.z.so libace_ndk.z.so libhilog_ndk.z.so)
   ```
