---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/monitor-guidelines
title: 事件监听开发指导（C/C++）
breadcrumb: 指南 > 系统 > 基础功能 > Input Kit（多模输入服务） > 事件监听开发指导（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7a7ca5d463b957ca341c4c4c9718cb9ffb517d50b568be575c55c965053fd355
---

## 功能介绍

从API version 12开始，多模为应用提供了按键、输入事件（鼠标、触屏和轴事件）监听能力，当前仅支持录屏类应用。使用场景例如：用户在录屏应用开启录屏时，监听设备的按键、鼠标、触摸和轴事件。

## 接口说明

创建和删除事件监听相关接口如下表所示，接口详细介绍请参考[input](../harmonyos-references/capi-input.md)。

| 接口名称 | 描述 |
| --- | --- |
| Input\_Result OH\_Input\_AddKeyEventMonitor(Input\_KeyEventCallback callback) | 创建按键事件监听。 |
| Input\_Result OH\_Input\_AddMouseEventMonitor(Input\_MouseEventCallback callback) | 创建鼠标事件监听。 |
| Input\_Result OH\_Input\_AddTouchEventMonitor(Input\_TouchEventCallback callback) | 创建触摸事件监听。 |
| Input\_Result OH\_Input\_AddAxisEventMonitorForAll(Input\_AxisEventCallback callback) | 创建所有类型轴事件监听。 |
| Input\_Result OH\_Input\_AddAxisEventMonitor(InputEvent\_AxisEventType axisEventType, Input\_AxisEventCallback callback) | 创建指定类型轴事件监听。 |
| Input\_Result OH\_Input\_RemoveKeyEventMonitor(Input\_KeyEventCallback callback) | 删除按键事件监听。 |
| Input\_Result OH\_Input\_RemoveMouseEventMonitor(Input\_MouseEventCallback callback) | 删除鼠标事件监听。 |
| Input\_Result OH\_Input\_RemoveTouchEventMonitor(Input\_TouchEventCallback callback) | 删除触摸事件监听。 |
| Input\_Result OH\_Input\_RemoveAxisEventMonitorForAll(Input\_AxisEventCallback callback) | 删除所有类型轴事件监听。 |
| Input\_Result OH\_Input\_RemoveAxisEventMonitor(InputEvent\_AxisEventType axisEventType, Input\_AxisEventCallback callback) | 删除指定类型轴事件监听。 |

## 开发步骤

### 链接动态库

调用创建和删除事件监听前，需链接相关动态库。链接动态库的方法是，在CMakeList.txt文件中新增如下配置：

```txt
target_link_libraries(entry PUBLIC libohinput.so)
```

### 申请所需权限

应用需要在module.json5中添加下面权限的配置，详细的配置方法参考声明[声明权限文档](declare-permissions.md)。

```json
"requestPermissions": [
    {
        "name": "ohos.permission.INPUT_MONITORING"
    }
]
```

### 创建事件监听

* **按键事件**

```
struct KeyEvent {
    int32_t action;
    int32_t keyCode;
    int64_t actionTime { -1 };
};

// 定义按键事件回调函数
void OnKeyEventCallback(const Input_KeyEvent* keyEvent)
{
    KeyEvent event;
    // Input_KeyEvent的生命周期仅限于回调函数内，回调函数执行完毕后会被自动销毁
    event.action = OH_Input_GetKeyEventAction(keyEvent);
    event.keyCode = OH_Input_GetKeyEventKeyCode(keyEvent);
    event.actionTime = OH_Input_GetKeyEventActionTime(keyEvent);
    // ...
}

static napi_value AddKeyEventMonitor(napi_env env, napi_callback_info info)
{
    Input_Result ret = OH_Input_AddKeyEventMonitor(OnKeyEventCallback);
    // ...
}

static napi_value RemoveKeyEventMonitor(napi_env env, napi_callback_info info)
{
    Input_Result ret = OH_Input_RemoveKeyEventMonitor(OnKeyEventCallback);
    // ...
}
```

* **鼠标事件**

```
struct MouseEvent {
    int32_t action;
    int32_t displayX;
    int32_t displayY;
    int32_t button { -1 };
    int32_t axisType { -1 };
    float axisValue { 0.0f };
    int64_t actionTime { -1 };
};

// 定义鼠标事件回调函数
void OnMouseEventCallback(const Input_MouseEvent* mouseEvent)
{
    MouseEvent event;
    // Input_MouseEvent的生命周期仅限于回调函数内，回调函数执行完毕后会被自动销毁
    event.action = OH_Input_GetMouseEventAction(mouseEvent);
    event.displayX = OH_Input_GetMouseEventDisplayX(mouseEvent);
    event.displayY = OH_Input_GetMouseEventDisplayY(mouseEvent);
    event.button = OH_Input_GetMouseEventButton(mouseEvent);
    event.axisType = OH_Input_GetMouseEventAxisType(mouseEvent);
    event.axisValue = OH_Input_GetMouseEventAxisValue(mouseEvent);
    event.actionTime = OH_Input_GetMouseEventActionTime(mouseEvent);
    // ...
}

static napi_value AddMouseEventMonitor(napi_env env, napi_callback_info info)
{
    Input_Result ret = OH_Input_AddMouseEventMonitor(OnMouseEventCallback);
    // ...
}

static napi_value RemoveMouseEventMonitor(napi_env env, napi_callback_info info)
{
    Input_Result ret = OH_Input_RemoveMouseEventMonitor(OnMouseEventCallback);
    // ...
}
```

* **触摸事件**

```
struct TouchEvent {
    int32_t action;
    int32_t id;
    int32_t displayX;
    int32_t displayY;
    int64_t actionTime { -1 };
};

void OnTouchEventCallback(const Input_TouchEvent* touchEvent)
{
    TouchEvent event;
    // Input_TouchEvent的生命周期仅限于回调函数内，回调函数执行完毕后会被自动销毁
    event.action = OH_Input_GetTouchEventAction(touchEvent);
    event.id = OH_Input_GetTouchEventFingerId(touchEvent);
    event.displayX = OH_Input_GetTouchEventDisplayX(touchEvent);
    event.displayY = OH_Input_GetTouchEventDisplayY(touchEvent);
    event.actionTime = OH_Input_GetTouchEventActionTime(touchEvent);
    // ...
}

static napi_value AddTouchEventMonitor(napi_env env, napi_callback_info info)
{
    Input_Result ret = OH_Input_AddTouchEventMonitor(OnTouchEventCallback);
    // ...
}

static napi_value RemoveTouchEventMonitor(napi_env env, napi_callback_info info)
{
    Input_Result ret = OH_Input_RemoveTouchEventMonitor(OnTouchEventCallback);
    // ...
}
```

* **轴事件**

```
struct AxisEvent {
    int32_t axisAction;
    float displayX;
    float displayY;
    std::map<int32_t, double> axisValues;
    int64_t actionTime { -1 };
    int32_t sourceType;
    int32_t axisEventType { -1 };
};

void OnAllAxisEventCallback(const Input_AxisEvent* axisEvent)
{
    AxisEvent event;
    // Input_AxisEvent的生命周期仅限于回调函数内，回调函数执行完毕后会被自动销毁
    InputEvent_AxisAction action = static_cast<InputEvent_AxisAction>(0);
    Input_Result ret = OH_Input_GetAxisEventAction(axisEvent, &action);
    event.axisAction = action;
    ret = OH_Input_GetAxisEventDisplayX(axisEvent, &event.displayX);
    ret = OH_Input_GetAxisEventDisplayY(axisEvent, &event.displayY);
    ret = OH_Input_GetAxisEventActionTime(axisEvent, &event.actionTime);
    InputEvent_SourceType sourceType = static_cast<InputEvent_SourceType>(0);
    ret = OH_Input_GetAxisEventSourceType(axisEvent, &sourceType);
    event.sourceType = sourceType;
    InputEvent_AxisEventType axisEventType = static_cast<InputEvent_AxisEventType>(-1);
    ret = OH_Input_GetAxisEventType(axisEvent, &axisEventType);
    event.axisEventType = axisEventType;
    if (event.axisEventType == AXIS_EVENT_TYPE_PINCH) {
        double value = 0;
        ret = OH_Input_GetAxisEventAxisValue(axisEvent, AXIS_TYPE_PINCH, &value);
        event.axisValues.insert(std::make_pair(AXIS_TYPE_PINCH, value));
        ret = OH_Input_GetAxisEventAxisValue(axisEvent, AXIS_TYPE_ROTATE, &value);
        event.axisValues.insert(std::make_pair(AXIS_TYPE_ROTATE, value));
    } else if (event.axisEventType == AXIS_EVENT_TYPE_SCROLL) {
        double value = 0;
        ret = OH_Input_GetAxisEventAxisValue(axisEvent, AXIS_TYPE_SCROLL_VERTICAL, &value);
        event.axisValues.insert(std::make_pair(AXIS_TYPE_SCROLL_VERTICAL, value));
        ret = OH_Input_GetAxisEventAxisValue(axisEvent, AXIS_TYPE_SCROLL_HORIZONTAL, &value);
        event.axisValues.insert(std::make_pair(AXIS_TYPE_SCROLL_HORIZONTAL, value));
    }
    // ...
}

// 定义捏合类型轴事件回调函数
void OnPinchAxisEventCallback(const Input_AxisEvent* axisEvent)
{
    AxisEvent event;
    // Input_AxisEvent的生命周期仅限于回调函数内，回调函数执行完毕后会被自动销毁
    InputEvent_AxisAction action = static_cast<InputEvent_AxisAction>(0);
    Input_Result ret = OH_Input_GetAxisEventAction(axisEvent, &action);
    event.axisAction = action;
    ret = OH_Input_GetAxisEventDisplayX(axisEvent, &event.displayX);
    ret = OH_Input_GetAxisEventDisplayY(axisEvent, &event.displayY);
    ret = OH_Input_GetAxisEventActionTime(axisEvent, &event.actionTime);
    InputEvent_SourceType sourceType = static_cast<InputEvent_SourceType>(0);
    ret = OH_Input_GetAxisEventSourceType(axisEvent, &sourceType);
    event.sourceType = sourceType;
    InputEvent_AxisEventType axisEventType = static_cast<InputEvent_AxisEventType>(-1);
    ret = OH_Input_GetAxisEventType(axisEvent, &axisEventType);
    event.axisEventType = axisEventType;
    double value = 0;
    ret = OH_Input_GetAxisEventAxisValue(axisEvent, AXIS_TYPE_PINCH, &value);
    event.axisValues.insert(std::make_pair(AXIS_TYPE_PINCH, value));
    ret = OH_Input_GetAxisEventAxisValue(axisEvent, AXIS_TYPE_ROTATE, &value);
    event.axisValues.insert(std::make_pair(AXIS_TYPE_ROTATE, value));
    // ...
}

void OnScrollAxisEventCallback(const Input_AxisEvent* axisEvent)
{
    AxisEvent event;
    // Input_AxisEvent的生命周期仅限于回调函数内，回调函数执行完毕后会被自动销毁
    InputEvent_AxisAction action = static_cast<InputEvent_AxisAction>(0);
    Input_Result ret = OH_Input_GetAxisEventAction(axisEvent, &action);
    event.axisAction = action;
    ret = OH_Input_GetAxisEventDisplayX(axisEvent, &event.displayX);
    ret = OH_Input_GetAxisEventDisplayY(axisEvent, &event.displayY);
    ret = OH_Input_GetAxisEventActionTime(axisEvent, &event.actionTime);
    InputEvent_SourceType sourceType = static_cast<InputEvent_SourceType>(0);
    ret = OH_Input_GetAxisEventSourceType(axisEvent, &sourceType);
    event.sourceType = sourceType;
    InputEvent_AxisEventType axisEventType = static_cast<InputEvent_AxisEventType>(-1);
    ret = OH_Input_GetAxisEventType(axisEvent, &axisEventType);
    event.axisEventType = axisEventType;
    double value = 0;
    ret = OH_Input_GetAxisEventAxisValue(axisEvent, AXIS_TYPE_SCROLL_VERTICAL, &value);
    event.axisValues.insert(std::make_pair(AXIS_TYPE_SCROLL_VERTICAL, value));
    ret = OH_Input_GetAxisEventAxisValue(axisEvent, AXIS_TYPE_SCROLL_HORIZONTAL, &value);
    event.axisValues.insert(std::make_pair(AXIS_TYPE_SCROLL_HORIZONTAL, value));
    // ...
}

static napi_value AddAxisEventMonitorForAll(napi_env env, napi_callback_info info)
{
    Input_Result ret = OH_Input_AddAxisEventMonitorForAll(OnAllAxisEventCallback);
    // ...
}

static napi_value RemoveAxisEventMonitorForAll(napi_env env, napi_callback_info info)
{
    Input_Result ret = OH_Input_RemoveAxisEventMonitorForAll(OnAllAxisEventCallback);
    // ...
}

static napi_value AddPinchAxisEventMonitor(napi_env env, napi_callback_info info)
{
    Input_Result ret = OH_Input_AddAxisEventMonitor(AXIS_EVENT_TYPE_PINCH, OnPinchAxisEventCallback);
    // ...
}

static napi_value RemovePinchAxisEventMonitor(napi_env env, napi_callback_info info)
{
    Input_Result ret = OH_Input_RemoveAxisEventMonitor(AXIS_EVENT_TYPE_PINCH, OnPinchAxisEventCallback);
    // ...
}

static napi_value AddScrollAxisEventMonitor(napi_env env, napi_callback_info info)
{
    Input_Result ret = OH_Input_AddAxisEventMonitor(AXIS_EVENT_TYPE_SCROLL, OnScrollAxisEventCallback);
    // ...
}

static napi_value RemoveScrollAxisEventMonitor(napi_env env, napi_callback_info info)
{
    Input_Result ret =  OH_Input_RemoveAxisEventMonitor(AXIS_EVENT_TYPE_SCROLL, OnScrollAxisEventCallback);
    // ...
}
```
