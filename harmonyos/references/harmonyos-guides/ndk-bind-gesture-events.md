---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-bind-gesture-events
title: 绑定手势事件
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 添加事件响应 > 绑定手势事件
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f6a7d97690f7628788bcfe371de9f917e6b9cd6555a7ae3edba7c069b8954c37
---

ArkUI开发框架在NDK接口中主要提供点击手势、滑动手势、快滑手势、长按手势、捏合手势和旋转手势，通过给指定的组件绑定不同的手势并设置相应的回调，实现期望的手势交互能力。

下面通过一个简单的示例来介绍如何实现手势绑定。

1. 创建一个Column节点，用于绑定手势。

   ```c
   // 创建Column节点
   auto column = nodeAPI->createNode(ARKUI_NODE_COLUMN);
   // 设置背景色
   ArkUI_NumberValue value[] = {{.u32 = 0xff112233}};
   ArkUI_AttributeItem item = {value, 1};
   nodeAPI->setAttribute(column, NODE_BACKGROUND_COLOR, &item);
   // 设置宽度
   ArkUI_NumberValue widthValue[] = {{400}};
   ArkUI_AttributeItem width = {widthValue, 1};
   nodeAPI->setAttribute(column, NODE_WIDTH, &width);
   // 设置高度
   ArkUI_NumberValue heightValue[] = {{400}};
   ArkUI_AttributeItem height = {heightValue, 1};
   nodeAPI->setAttribute(column, NODE_HEIGHT, &height);
   ```
2. 创建一个单指长按1秒并持续响应的长按手势。

   ```c
   // 获取手势Native接口集合
   auto gestureApi = reinterpret_cast<ArkUI_NativeGestureAPI_1 *>(
       OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_GESTURE, "ArkUI_NativeGestureAPI_1"));
   // 创建长按手势
   // DURATION_NUM_1000 = 1000
   auto longPressGesture = gestureApi->createLongPressGesture(1, true, DURATION_NUM_1000);
   ```
3. 将创建的手势和步骤一中创建的Column节点绑定。

   ```c
   auto onActionCallBack = [](ArkUI_GestureEvent *event, void *extraParam) {
       // 回调内容
       // ···
   };

   // 将手势设置到组件上
   gestureApi->setGestureEventTarget(
       longPressGesture, GESTURE_EVENT_ACTION_ACCEPT | GESTURE_EVENT_ACTION_UPDATE | GESTURE_EVENT_ACTION_END, column,
       onActionCallBack);

   gestureApi->addGestureToNode(column, longPressGesture, PARALLEL, NORMAL_GESTURE_MASK);
   ```

## 单一手势

通过上文的示例已经了解了如何将手势绑定在节点上，接下来将分别介绍不同手势的创建方法。

* 点击手势

  通过给组件绑定点击手势可在组件被点击时触发此回调，可指定触发回调需要的点击次数和手指个数。

  ```c
  // 获取手势Native接口集合
  auto gestureApi = reinterpret_cast<ArkUI_NativeGestureAPI_1 *>(
      OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_GESTURE, "ArkUI_NativeGestureAPI_1"));
  // 创建点击手势
  auto tapGesture = gestureApi->createTapGesture(1, 1);
  ```
* 滑动手势

  通过给组件绑定滑动手势可在用户滑动组件时触发回调，可指定触发回调需要的手指个数、滑动方向、滑动距离。单位为px。

  ```c
  // 获取手势Native接口集合
  auto gestureApi = reinterpret_cast<ArkUI_NativeGestureAPI_1 *>(
      OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_GESTURE, "ArkUI_NativeGestureAPI_1"));
  // 创建滑动手势
  auto panGesture = gestureApi->createPanGesture(1, GESTURE_DIRECTION_ALL, 1);
  ```
* 长按手势

  通过给组件绑定长按手势可在用户长按组件时触发回调，可指定触发回调需要的手指个数、长按时间（单位毫秒）、是否连续触发。

  ```c
  // 获取手势Native接口集合
  auto gestureApi = reinterpret_cast<ArkUI_NativeGestureAPI_1 *>(
      OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_GESTURE, "ArkUI_NativeGestureAPI_1"));
  // 创建长按手势
  // DURATION_NUM_1000 = 1000
  auto longPressGesture = gestureApi->createLongPressGesture(1, true, DURATION_NUM_1000);
  ```
* 捏合手势

  通过给组件绑定捏合手势可在用户捏合组件时触发回调，可指定触发回调需要的手指个数（最小为2）、捏合距离（单位px）。

  ```c
  // 获取手势Native接口集合
  auto gestureApi = reinterpret_cast<ArkUI_NativeGestureAPI_1 *>(
      OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_GESTURE, "ArkUI_NativeGestureAPI_1"));
  // 创建捏合手势
  // NUMBER_2 = 2，NUMBER_10 = 10
  auto pinchGesture = gestureApi->createPinchGesture(NUMBER_2, NUMBER_10);
  ```
* 旋转手势

  通过给组件绑定旋转手势可在用户旋转组件时触发回调，可指定触发回调需要的手指个数（最小为2）、旋转角度。

  ```c
  // 获取手势Native接口集合
  auto gestureApi = reinterpret_cast<ArkUI_NativeGestureAPI_1 *>(
      OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_GESTURE, "ArkUI_NativeGestureAPI_1"));
  // 创建旋转手势
  // NUMBER_2 = 2，NUMBER_10 = 10
  auto rotationGesture = gestureApi->createRotationGesture(NUMBER_2, NUMBER_10);
  ```
* 快滑手势

  通过给组件绑定快滑手势可在用户快速滑动组件时触发回调，可指定触发回调需要的手指个数（最小为1）、滑动方向、滑动速度（单位px/s）。

  ```c
  // 获取手势Native接口集合
  auto gestureApi = reinterpret_cast<ArkUI_NativeGestureAPI_1 *>(
      OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_GESTURE, "ArkUI_NativeGestureAPI_1"));
  // 创建快滑手势
  // SPEED_NUM_50 = 50
  auto swipeGesture = gestureApi->createSwipeGesture(1, GESTURE_DIRECTION_ALL, SPEED_NUM_50);
  ```

## 组合手势

可以将多个不同类型的手势组合在一起，形成一个手势组，这个手势组可以作为一个识别整体，达到对用户多个不同类型手势序列的识别目的。

通过设置[ArkUI\_GroupGestureMode](../harmonyos-references/capi-native-gesture-h.md#arkui_groupgesturemode)来指定这个手势组的识别模式，即组内的手势之间的关系，包含顺序识别SEQUENTIAL\_GROUP，并行识别PARALLEL\_GROUP，互斥识别EXCLUSIVE\_GROUP。

### 顺序识别

顺序识别组合手势对应的ArkUI\_GroupGestureMode为SEQUENTIAL\_GROUP。顺序识别组合手势将按照手势的注册顺序识别手势，直到所有的手势识别成功。当顺序识别组合手势中有一个手势识别失败时，后续手势识别均失败。顺序识别手势组仅有最后一个手势可以响应[GESTURE\_EVENT\_ACTION\_END](../harmonyos-references/capi-native-gesture-h.md#arkui_gestureeventactiontype)。

以顺序识别长按和快滑手势为例：

```c
// LongPressAndSwipeGesture.h
#include <arkui/native_animate.h>
#include <arkui/native_gesture.h>
#include <arkui/native_interface.h>
#include <arkui/native_node.h>
#include <arkui/native_type.h>
#include <arkui/native_node_napi.h>
#include <hilog/log.h>
#include "Common.h"
#include "Function.h"
// ...
ArkUI_NodeHandle LongPressAndSwipeGesture()
{
    auto column = nodeAPI->createNode(ARKUI_NODE_COLUMN);

    // 创建节点
    ArkUI_NumberValue value[] = {{.u32 = 0xff112233}};
    ArkUI_AttributeItem item = {value, ITEM_SIZE_ONE};
    nodeAPI->setAttribute(column, NODE_BACKGROUND_COLOR, &item);
    ArkUI_NumberValue widthValue[] = {{WIDTH_SIZE}};
    ArkUI_AttributeItem width = {widthValue, ITEM_SIZE_ONE};
    nodeAPI->setAttribute(column, NODE_WIDTH, &width);
    ArkUI_NumberValue heightValue[] = {{HEIGHT_SIZE}};
    ArkUI_AttributeItem height = {heightValue, ITEM_SIZE_ONE};
    nodeAPI->setAttribute(column, NODE_HEIGHT, &height);

    // 判断是否支持创建手势
    auto gestureApi = reinterpret_cast<ArkUI_NativeGestureAPI_1 *>(
        OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_GESTURE, "ArkUI_NativeGestureAPI_1"));
    if (gestureApi->createGroupGesture) {
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
                     "NdkAddInteractionEvent_GestureSampleLog, createGroupGesture api exist");
    } else {
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
                     "NdkAddInteractionEvent_GestureSampleLog, createGroupGesture api not exist");
    }
    auto groupGesture = gestureApi->createGroupGesture(ArkUI_GroupGestureMode::SEQUENTIAL_GROUP);

    // 创建长按手势
    auto longPressGesture = gestureApi->createLongPressGesture(FINGERS_NUM, true, DURATION_NUM);
    if (gestureApi->getGestureType) {
        ArkUI_GestureRecognizerType type = gestureApi->getGestureType(longPressGesture);
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
                     "NdkAddInteractionEvent_GestureSampleLog longPressGesture,"
                     "ArkUI_GestureRecognizerType%{public}d", type);
    }
    // 给长按手势绑定回调
    auto onActionCallBackPanLongPress = [](ArkUI_GestureEvent *event, void *extraParam) {
        ArkUI_GestureEventActionType actionType = OH_ArkUI_GestureEvent_GetActionType(event);

        float velocity = OH_ArkUI_PanGesture_GetVelocity(event);
        float velocityX = OH_ArkUI_PanGesture_GetVelocityX(event);
        float velocityY = OH_ArkUI_PanGesture_GetVelocityY(event);
        float offsetX = OH_ArkUI_PanGesture_GetOffsetX(event);
        float offsetY = OH_ArkUI_PanGesture_GetOffsetY(event);
        float scale = OH_ArkUI_PinchGesture_GetScale(event);
        float centerX = OH_ArkUI_PinchGesture_GetCenterX(event);
        float centerY = OH_ArkUI_PinchGesture_GetCenterY(event);
        float angle = OH_ArkUI_SwipeGesture_GetAngle(event);
        float velocityS = OH_ArkUI_SwipeGesture_GetVelocity(event);
        float angleR = OH_ArkUI_RotationGesture_GetAngle(event);
        float repeat = OH_ArkUI_LongPress_GetRepeatCount(event);

        OH_LOG_Print(
            LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
            "NdkAddInteractionEvent_GestureSampleLog,longPressGesturecallback actionType:%{public}d,"
            "velocity%{public}f,velocityX%{public}f;"
            "velocityY%{public}f,offsetX%{public}f,offsetY%{public}f,scale%{public}fcenterX"
            "%{public}fcenterY"
            "%{public}fangle%{public}fvelocityS%{public}fangleR%{public}frepeat%{public}f",
            actionType, velocity, velocityX, velocityY, offsetX, offsetY, scale, centerX, centerY, angle, velocityS,
            angleR, repeat);
    };
    gestureApi->setGestureEventTarget(longPressGesture,
                                      GESTURE_EVENT_ACTION_ACCEPT | GESTURE_EVENT_ACTION_UPDATE |
                                      GESTURE_EVENT_ACTION_CANCEL, column, onActionCallBackPanLongPress);

    // 将长按手势添加到手势组
    if (gestureApi->addChildGesture) {
        gestureApi->addChildGesture(groupGesture, longPressGesture);
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
                     "NdkAddInteractionEvent_GestureSampleLog, addChildGesture longPressGesture");
    }
    // 创建快滑手势 swipe
    auto swipeGesture = gestureApi->createSwipeGesture(1, GESTURE_DIRECTION_ALL, 100);
    if (gestureApi->getGestureType) {
        ArkUI_GestureRecognizerType type = gestureApi->getGestureType(swipeGesture);
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
                     "NdkAddInteractionEvent_GestureSampleLog, ArkUI_GestureRecognizerType %{public}d",
                     type);
    }
    // 给快滑手势绑定回调
    auto onActionCallBack = [](ArkUI_GestureEvent *event, void *extraParam) {
        ArkUI_GestureEventActionType actionType = OH_ArkUI_GestureEvent_GetActionType(event);

        float velocity = OH_ArkUI_PanGesture_GetVelocity(event);
        float velocityX = OH_ArkUI_PanGesture_GetVelocityX(event);
        float velocityY = OH_ArkUI_PanGesture_GetVelocityY(event);
        float offsetX = OH_ArkUI_PanGesture_GetOffsetX(event);
        float offsetY = OH_ArkUI_PanGesture_GetOffsetY(event);
        float scale = OH_ArkUI_PinchGesture_GetScale(event);
        float centerX = OH_ArkUI_PinchGesture_GetCenterX(event);
        float centerY = OH_ArkUI_PinchGesture_GetCenterY(event);
        float angle = OH_ArkUI_SwipeGesture_GetAngle(event);
        float velocityS = OH_ArkUI_SwipeGesture_GetVelocity(event);
        float angleR = OH_ArkUI_RotationGesture_GetAngle(event);
        float repeat = OH_ArkUI_LongPress_GetRepeatCount(event);
        
        // 通过日志查看
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
                     "NdkAddInteractionEvent_GestureSampleLog, swipeGesture "
                     "callback actionType: %{public}d, velocity %{public}f,velocityX "
                     "%{public}f; "
                     "velocityY %{public}f, offsetX %{public}f, offsetY %{public}f, scale %{public}fcenterX "
                     "%{public}f centerY"
                     " %{public}f angle %{public}f velocityS %{public}f angleR %{public}f repeat %{public}f",
                     actionType, velocity, velocityX, velocityY, offsetX, offsetY, scale, centerX, centerY, angle,
                     velocityS, angleR, repeat);

        ArkUI_NumberValue value[] = {{.f32 = 0}, {.f32 = 0}, {.f32 = 0}, {.f32 = angleR}, {.f32 = 0}};
        ArkUI_AttributeItem item = {value, ITEM_SIZE_FIVE};
        auto column = reinterpret_cast<ArkUI_NodeHandle>(extraParam);
        nodeAPI->setAttribute(column, NODE_ROTATE, &item);
    };

    gestureApi->setGestureEventTarget(
        swipeGesture, GESTURE_EVENT_ACTION_ACCEPT | GESTURE_EVENT_ACTION_UPDATE | GESTURE_EVENT_ACTION_END, column,
        onActionCallBack);

    // 将快滑手势添加到手势组
    if (gestureApi->addChildGesture) {
        gestureApi->addChildGesture(groupGesture, swipeGesture);
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
                     "NdkAddInteractionEvent_GestureSampleLog, addChildGesture swipeGesture");
    }
    // 将手势组设置到组件上
    gestureApi->addGestureToNode(column, groupGesture, PRIORITY, NORMAL_GESTURE_MASK);
    return column;
}
```

**完整示例：**

完整示例请参考[示例工程](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NdkAddInteractionEvent)。

### 并行识别

并行识别组合手势对应的ArkUI\_GroupGestureMode为PARALLEL\_GROUP。并行识别组合手势中注册的手势将同时进行识别，直到所有手势识别结束。并行识别手势组合中的手势进行识别时互不影响。

以并行识别长按和快滑手势为例：

```c
// LongPressAndFlickGesture.h
#include <arkui/native_animate.h>
#include <arkui/native_gesture.h>
#include <arkui/native_interface.h>
#include <arkui/native_node.h>
#include <arkui/native_type.h>
#include <arkui/native_node_napi.h>
#include <hilog/log.h>
#include "Common.h"
#include "Function.h"
// ...

ArkUI_NodeHandle LongPressAndFlickGesture()
{
    auto column = nodeAPI->createNode(ARKUI_NODE_COLUMN);

    // 创建节点
    ArkUI_NumberValue value[] = {{.u32 = 0xff112233}};
    ArkUI_AttributeItem item = {value, ITEM_SIZE_ONE};
    nodeAPI->setAttribute(column, NODE_BACKGROUND_COLOR, &item);
    ArkUI_NumberValue widthValue[] = {{WIDTH_SIZE}};
    ArkUI_AttributeItem width = {widthValue, ITEM_SIZE_ONE};
    nodeAPI->setAttribute(column, NODE_WIDTH, &width);
    ArkUI_NumberValue heightValue[] = {{HEIGHT_SIZE}};
    ArkUI_AttributeItem height = {heightValue, ITEM_SIZE_ONE};
    nodeAPI->setAttribute(column, NODE_HEIGHT, &height);

    // 判断是否支持创建手势
    auto gestureApi = reinterpret_cast<ArkUI_NativeGestureAPI_1 *>(
        OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_GESTURE, "ArkUI_NativeGestureAPI_1"));
    if (gestureApi->createGroupGesture) {
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
                     "NdkAddInteractionEvent_GestureSampleLog, createGroupGesture api exist");
    } else {
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
                     "NdkAddInteractionEvent_GestureSampleLog, createGroupGesture api not exist");
    }

    // 创建手势组
    auto groupGesture = gestureApi->createGroupGesture(ArkUI_GroupGestureMode::PARALLEL_GROUP);

    // 创建长按手势
    auto longPressGesture = gestureApi->createLongPressGesture(FINGERS_NUM, true, DURATION_NUM_500);
    if (gestureApi->getGestureType) {
        ArkUI_GestureRecognizerType type = gestureApi->getGestureType(longPressGesture);
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
                     "NdkAddInteractionEvent_GestureSampleLog,ArkUI_GestureRecognizerType%{public}d", type);
    }
    // 给长按手势绑定回调
    auto onActionCallBackPanLongPress = [](ArkUI_GestureEvent *event, void *extraParam) {
        ArkUI_GestureEventActionType actionType = OH_ArkUI_GestureEvent_GetActionType(event);

        float velocity = OH_ArkUI_PanGesture_GetVelocity(event);
        float velocityX = OH_ArkUI_PanGesture_GetVelocityX(event);
        float velocityY = OH_ArkUI_PanGesture_GetVelocityY(event);
        float offsetX = OH_ArkUI_PanGesture_GetOffsetX(event);
        float offsetY = OH_ArkUI_PanGesture_GetOffsetY(event);
        float scale = OH_ArkUI_PinchGesture_GetScale(event);
        float centerX = OH_ArkUI_PinchGesture_GetCenterX(event);
        float centerY = OH_ArkUI_PinchGesture_GetCenterY(event);
        float angle = OH_ArkUI_SwipeGesture_GetAngle(event);
        float velocityS = OH_ArkUI_SwipeGesture_GetVelocity(event);
        float angleR = OH_ArkUI_RotationGesture_GetAngle(event);
        float repeat = OH_ArkUI_LongPress_GetRepeatCount(event);

        OH_LOG_Print(
            LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
            "NdkAddInteractionEvent_GestureSampleLog,longPressGesturecallback actionType:%{public}d,"
            "velocity%{public}f,velocityX%{public}f;"
            "velocityY%{public}f,offsetX%{public}f,offsetY%{public}f,scale%{public}f, centerX "
            "%{public}fcenterY"
            "%{public}fangle%{public}fvelocityS%{public}fangleR%{public}frepeat%{public}f",
            actionType, velocity, velocityX, velocityY, offsetX, offsetY, scale, centerX, centerY, angle, velocityS,
            angleR, repeat);
    };
    gestureApi->setGestureEventTarget(longPressGesture,
                                      GESTURE_EVENT_ACTION_ACCEPT | GESTURE_EVENT_ACTION_UPDATE |
                                            GESTURE_EVENT_ACTION_CANCEL,
                                      column, onActionCallBackPanLongPress);

    // 将长按手势添加到手势组
    if (gestureApi->addChildGesture) {
        gestureApi->addChildGesture(groupGesture, longPressGesture);
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
                     "NdkAddInteractionEvent_GestureSampleLog, addChildGesture longPressGesture");
    }
    // 创建快滑手势 swipe
    auto swipeGesture = gestureApi->createSwipeGesture(FINGERS_NUM, GESTURE_DIRECTION_ALL, DURATION_NUM_100);
    if (gestureApi->getGestureType) {
        ArkUI_GestureRecognizerType type = gestureApi->getGestureType(swipeGesture);
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
                     "NdkAddInteractionEvent_GestureSampleLog, ArkUI_GestureRecognizerType %{public}d",
                     type);
    }
    // 给快滑手势绑定回调
    auto onActionCallBack = [](ArkUI_GestureEvent *event, void *extraParam) {
        ArkUI_GestureEventActionType actionType = OH_ArkUI_GestureEvent_GetActionType(event);

        float velocity = OH_ArkUI_PanGesture_GetVelocity(event);
        float velocityX = OH_ArkUI_PanGesture_GetVelocityX(event);
        float velocityY = OH_ArkUI_PanGesture_GetVelocityY(event);
        float offsetX = OH_ArkUI_PanGesture_GetOffsetX(event);
        float offsetY = OH_ArkUI_PanGesture_GetOffsetY(event);
        float scale = OH_ArkUI_PinchGesture_GetScale(event);
        float centerX = OH_ArkUI_PinchGesture_GetCenterX(event);
        float centerY = OH_ArkUI_PinchGesture_GetCenterY(event);
        float angle = OH_ArkUI_SwipeGesture_GetAngle(event);
        float velocityS = OH_ArkUI_SwipeGesture_GetVelocity(event);
        float angleR = OH_ArkUI_RotationGesture_GetAngle(event);
        float repeat = OH_ArkUI_LongPress_GetRepeatCount(event);
        
        // 通过日志查看
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
                     "NdkAddInteractionEvent_GestureSampleLog, swipeGesture "
                     "callback actionType: %{public}d, velocity%{public}f,velocityX "
                     "%{public}f; "
                     "velocityY %{public}f, offsetX %{public}f, offsetY %{public}f, scale %{public}f, centerX "
                     "%{public}f centerY"
                     " %{public}f angle %{public}f velocityS %{public}f angleR %{public}f repeat %{public}f",
                     actionType, velocity, velocityX, velocityY, offsetX, offsetY, scale, centerX, centerY, angle,
                     velocityS, angleR, repeat);

        ArkUI_NumberValue value[] = {{.f32 = 0}, {.f32 = 0}, {.f32 = 0}, {.f32 = angleR}, {.f32 = 0}};
        ArkUI_AttributeItem item = {value, ITEM_SIZE_FIVE};
        auto column = reinterpret_cast<ArkUI_NodeHandle>(extraParam);
        nodeAPI->setAttribute(column, NODE_ROTATE, &item);
    };

    gestureApi->setGestureEventTarget(
        swipeGesture, GESTURE_EVENT_ACTION_ACCEPT | GESTURE_EVENT_ACTION_UPDATE | GESTURE_EVENT_ACTION_END, column,
        onActionCallBack);

    // 将快滑手势添加到手势组
    if (gestureApi->addChildGesture) {
        gestureApi->addChildGesture(groupGesture, swipeGesture);
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
                     "NdkAddInteractionEvent_GestureSampleLog, addChildGesture swipeGesture");
    }
    // 将手势组设置到组件上
    gestureApi->addGestureToNode(column, groupGesture, PRIORITY, NORMAL_GESTURE_MASK);
    return column;
}
```

**完整示例：**

完整示例请参考[示例工程](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NdkAddInteractionEvent)。

### 互斥识别

互斥识别组合手势对应的ArkUI\_GroupGestureMode为EXCLUSIVE\_GROUP。互斥识别组合手势中注册的手势将同时进行识别，若有一个手势识别成功，则结束手势识别，其他所有手势识别失败。

以互斥识别滑动手势和捏合手势为例：

```c
// SwipeAndPinchExclusiveGesture.h
#include <arkui/native_animate.h>
#include <arkui/native_gesture.h>
#include <arkui/native_interface.h>
#include <arkui/native_node.h>
#include <arkui/native_type.h>
#include <arkui/native_node_napi.h>
#include <hilog/log.h>
#include "Common.h"
#include "Function.h"
// ...

ArkUI_NodeHandle SwipeAndPinchExclusiveGesture()
{
    OH_ArkUI_GetModuleInterface(ARKUI_NATIVE_NODE, ArkUI_NativeNodeAPI_1, nodeAPI);
    if (nodeAPI == nullptr) {
        return nullptr;
    }
    auto column = nodeAPI->createNode(ARKUI_NODE_COLUMN);

    // 创建节点
    ArkUI_NumberValue value[] = {{.u32 = 0xff112233}};
    ArkUI_AttributeItem item = {value, 1};
    nodeAPI->setAttribute(column, NODE_BACKGROUND_COLOR, &item);
    ArkUI_NumberValue widthValue[] = {{WIDTH_SIZE}};
    ArkUI_AttributeItem width = {widthValue, ITEM_SIZE_ONE};
    nodeAPI->setAttribute(column, NODE_WIDTH, &width);
    ArkUI_NumberValue heightValue[] = {{HEIGHT_SIZE}};
    ArkUI_AttributeItem height = {heightValue, ITEM_SIZE_ONE};
    nodeAPI->setAttribute(column, NODE_HEIGHT, &height);

    // 判断是否支持创建手势
    auto gestureApi = reinterpret_cast<ArkUI_NativeGestureAPI_1 *>(
        OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_GESTURE, "ArkUI_NativeGestureAPI_1"));
    if (gestureApi->createGroupGesture) {
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
                     "NdkAddInteractionEvent_GestureSampleLog, createGroupGesture api exist");
    } else {
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
                     "NdkAddInteractionEvent_GestureSampleLog, createGroupGesture api not exist");
    }
    auto groupGesture = gestureApi->createGroupGesture(ArkUI_GroupGestureMode::EXCLUSIVE_GROUP);

    // 创建滑动手势
    auto panGesture = gestureApi->createPanGesture(FINGERS_NUM, GESTURE_DIRECTION_VERTICAL, DURATION_NUM);
    if (gestureApi->getGestureType) {
        ArkUI_GestureRecognizerType type = gestureApi->getGestureType(panGesture);
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
                     "NdkAddInteractionEvent_GestureSampleLog panGesture, ArkUI_GestureRecognizerType %{public}d",
                     type);
    }
    // 给滑动手势绑定回调
    auto onActionCallBackPan = [](ArkUI_GestureEvent *event, void *extraParam) {
        ArkUI_GestureEventActionType actionType = OH_ArkUI_GestureEvent_GetActionType(event);

        float velocity = OH_ArkUI_PanGesture_GetVelocity(event);
        float velocityX = OH_ArkUI_PanGesture_GetVelocityX(event);
        float velocityY = OH_ArkUI_PanGesture_GetVelocityY(event);
        float offsetX = OH_ArkUI_PanGesture_GetOffsetX(event);
        float offsetY = OH_ArkUI_PanGesture_GetOffsetY(event);
        float scale = OH_ArkUI_PinchGesture_GetScale(event);
        float centerX = OH_ArkUI_PinchGesture_GetCenterX(event);
        float centerY = OH_ArkUI_PinchGesture_GetCenterY(event);
        float angle = OH_ArkUI_SwipeGesture_GetAngle(event);
        float velocityS = OH_ArkUI_SwipeGesture_GetVelocity(event);
        float angleR = OH_ArkUI_RotationGesture_GetAngle(event);
        float repeat = OH_ArkUI_LongPress_GetRepeatCount(event);

        // 通过日志查看
        OH_LOG_Print(
            LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
            "NdkAddInteractionEvent_GestureSampleLog, panGesture callback actionType: %{public}d, "
            "velocity %{public}f,velocityX %{public}f; "
            "velocityY %{public}f, offsetX %{public}f, offsetY %{public}f, scale %{public}fcenterX "
            "%{public}f centerY"
            " %{public}f angle %{public}f velocityS %{public}f angleR %{public}f repeat %{public}f",
            actionType, velocity, velocityX, velocityY, offsetX, offsetY, scale, centerX, centerY, angle, velocityS,
            angleR, repeat);
    };
    gestureApi->setGestureEventTarget(panGesture,
                                      GESTURE_EVENT_ACTION_ACCEPT | GESTURE_EVENT_ACTION_UPDATE |
                                          GESTURE_EVENT_ACTION_END | GESTURE_EVENT_ACTION_CANCEL,
                                      column, onActionCallBackPan);
    // 将滑动手势添加到手势组
    if (gestureApi->addChildGesture) {
        gestureApi->addChildGesture(groupGesture, panGesture);
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
                     "NdkAddInteractionEvent_GestureSampleLog, addChildGesture panGesture");
    }
    // 创建捏合手势
    // NUMBER_2 = 2，NUMBER_10 = 10
    auto pinchGesture = gestureApi->createPinchGesture(NUMBER_2, NUMBER_10);
    if (gestureApi->getGestureType) {
        ArkUI_GestureRecognizerType type = gestureApi->getGestureType(pinchGesture);
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
                     "NdkAddInteractionEvent_GestureSampleLog pinchGesture, "
                     "ArkUI_GestureRecognizerType %{public}d", type);
    }
    // 给捏合手势绑定回调
    auto onActionCallBack = [](ArkUI_GestureEvent *event, void *extraParam) {
        ArkUI_GestureEventActionType actionType = OH_ArkUI_GestureEvent_GetActionType(event);

        float velocity = OH_ArkUI_PanGesture_GetVelocity(event);
        float velocityX = OH_ArkUI_PanGesture_GetVelocityX(event);
        float velocityY = OH_ArkUI_PanGesture_GetVelocityY(event);
        float offsetX = OH_ArkUI_PanGesture_GetOffsetX(event);
        float offsetY = OH_ArkUI_PanGesture_GetOffsetY(event);
        float scale = OH_ArkUI_PinchGesture_GetScale(event);
        float centerX = OH_ArkUI_PinchGesture_GetCenterX(event);
        float centerY = OH_ArkUI_PinchGesture_GetCenterY(event);
        float angle = OH_ArkUI_SwipeGesture_GetAngle(event);
        float velocityS = OH_ArkUI_SwipeGesture_GetVelocity(event);
        float angleR = OH_ArkUI_RotationGesture_GetAngle(event);
        float repeat = OH_ArkUI_LongPress_GetRepeatCount(event);
        
        OH_LOG_Print(
            LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
            "NdkAddInteractionEvent_GestureSampleLog, pinchGesture callback actionType: %{public}d, "
            "velocity %{public}f,velocityX %{public}f; "
            "velocityY %{public}f, offsetX %{public}f, offsetY %{public}f, scale %{public}fcenterX "
            "%{public}f centerY"
            " %{public}f angle %{public}f velocityS %{public}f angleR %{public}f repeat %{public}f",
            actionType, velocity, velocityX, velocityY, offsetX, offsetY, scale, centerX, centerY, angle, velocityS,
            angleR, repeat);
        ArkUI_NumberValue value[] = {{.f32 = scale}, {.f32 = scale}};
        ArkUI_AttributeItem item = {value, ITEM_SIZE_TWO};
        auto column = reinterpret_cast<ArkUI_NodeHandle>(extraParam);
        nodeAPI->setAttribute(column, NODE_SCALE, &item);
    };
    gestureApi->setGestureEventTarget(pinchGesture,
                                      GESTURE_EVENT_ACTION_ACCEPT | GESTURE_EVENT_ACTION_UPDATE |
                                          GESTURE_EVENT_ACTION_END | GESTURE_EVENT_ACTION_CANCEL,
                                      column, onActionCallBack);
    // 将捏合手势添加到手势组
    if (gestureApi->addChildGesture) {
        gestureApi->addChildGesture(groupGesture, pinchGesture);
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
                     "NdkAddInteractionEvent_GestureSampleLog, addChildGesture pinchGesture");
    }
    // 将手势组设置到组件上
    gestureApi->addGestureToNode(column, groupGesture, PRIORITY, NORMAL_GESTURE_MASK);
    return column;
}
```

**完整示例：**

完整示例请参考[示例工程](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NdkAddInteractionEvent)。

### 自定义手势判定

当用户的操作符合某个手势识别器，该识别器即将触发成功时，可通过自定义手势判定能力来动态决策，是否希望该识别器被系统认定为识别成功。通过setGestureInterrupterToNode接口，绑定一个回调在该组件上，当组件上的某个手势即将识别成功时，通过返回CONTINUE或REJECT来决定是否将成功机会让给其它手势识别器。

在上文绑定手势事件的示例中按照如下方式进行调整即可实现自定义手势判定。

1. 创建自定义手势判定回调。

   ```c
   auto onInterruptCallback = [](ArkUI_GestureInterruptInfo *info) -> ArkUI_GestureInterruptResult {
       // 获取是否系统手势
       auto sysTag = OH_ArkUI_GestureInterruptInfo_GetSystemFlag(info);
       // 获取拦截的手势指针
       auto recognizer = OH_ArkUI_GestureInterruptInfo_GetRecognizer(info);
       // 获取系统手势类型
       auto systemRecognizerType = OH_ArkUI_GestureInterruptInfo_GetSystemRecognizerType(info);
       // 获取手势事件
       auto gestureEvent = OH_ArkUI_GestureInterruptInfo_GetGestureEvent(info);
       auto inputEvent = OH_ArkUI_GestureEvent_GetRawInputEvent(gestureEvent);
       OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
           "NdkAddInteractionEvent_eventInfo longPressGesture");
       if (sysTag) {
           // 如果是系统手势则不拦截
           return GESTURE_INTERRUPT_RESULT_CONTINUE;
       } else {
           // 不是系统手势则拒绝
           return GESTURE_INTERRUPT_RESULT_REJECT;
       }
   };
   ```
2. 绑定手势判定和节点。

   ```c
   gestureApi->setGestureInterrupterToNode(column, onInterruptCallback);
   ```

经过上述修改，将原本可以生效的长按手势做了拦截，即，此时再对Column节点长按将不会触发长按的手势回调。

## 获取事件信息

绑定手势事件已详细说明如何将手势绑定到节点上。在回调执行时，ArkUI框架提供了[OH\_ArkUI\_GestureEvent\_GetRawInputEvent()](../harmonyos-references/capi-native-gesture-h.md#oh_arkui_gestureevent_getrawinputevent)接口，可从手势事件中获取基础事件对象。之后，可通过调用[OH\_ArkUI\_PointerEvent\_GetDisplayX()](../harmonyos-references/capi-ui-input-event-h.md#oh_arkui_pointerevent_getdisplayx)、[OH\_ArkUI\_PointerEvent\_GetDisplayXByIndex()](../harmonyos-references/capi-ui-input-event-h.md#oh_arkui_pointerevent_getdisplayxbyindex)、[OH\_ArkUI\_UIInputEvent\_GetAction()](../harmonyos-references/capi-ui-input-event-h.md#oh_arkui_uiinputevent_getaction)和[OH\_ArkUI\_UIInputEvent\_GetEventTime()](../harmonyos-references/capi-ui-input-event-h.md#oh_arkui_uiinputevent_geteventtime)等接口，从基础事件中获取更多信息。应用依据获取的信息，在手势事件执行过程中实现差异化交互逻辑。

```c
// 设置回调，在触发手势事件时执行回调处理手势事件
auto onActionCallback = [](ArkUI_GestureEvent *event, void *extraParams) {
    // 从手势事件获取基础事件对象
    auto *inputEvent = OH_ArkUI_GestureEvent_GetRawInputEvent(event);
    // 从基础事件获取事件信息
    auto x = OH_ArkUI_PointerEvent_GetX(inputEvent);
    auto y = OH_ArkUI_PointerEvent_GetY(inputEvent);
    auto displayX = OH_ArkUI_PointerEvent_GetDisplayX(inputEvent);
    auto displayY = OH_ArkUI_PointerEvent_GetDisplayY(inputEvent);
    auto windowX = OH_ArkUI_PointerEvent_GetWindowX(inputEvent);
    auto windowY = OH_ArkUI_PointerEvent_GetWindowY(inputEvent);
    auto pointerCount = OH_ArkUI_PointerEvent_GetPointerCount(inputEvent);
    auto xByIndex = OH_ArkUI_PointerEvent_GetXByIndex(inputEvent, 0);
    auto yByIndex = OH_ArkUI_PointerEvent_GetYByIndex(inputEvent, 0);
    auto displayXByIndex = OH_ArkUI_PointerEvent_GetDisplayXByIndex(inputEvent, 0);
    auto displayYByIndex = OH_ArkUI_PointerEvent_GetDisplayYByIndex(inputEvent, 0);
    auto windowXByIndex = OH_ArkUI_PointerEvent_GetWindowXByIndex(inputEvent, 0);
    auto windowYByIndex = OH_ArkUI_PointerEvent_GetWindowYByIndex(inputEvent, 0);
    auto pointerId = OH_ArkUI_PointerEvent_GetPointerId(inputEvent, 0);
    auto pressure = OH_ArkUI_PointerEvent_GetPressure(inputEvent, 0);
    auto action = OH_ArkUI_UIInputEvent_GetAction(inputEvent);
    auto eventTime = OH_ArkUI_UIInputEvent_GetEventTime(inputEvent);
    auto sourceType = OH_ArkUI_UIInputEvent_GetSourceType(inputEvent);
    auto type = OH_ArkUI_UIInputEvent_GetType(inputEvent);
    std::string eventInfo =
        "x: " + std::to_string(x) + ", y: " + std::to_string(y) +
        ", displayX: " + std::to_string(displayX) + ", displayY: " + std::to_string(displayY) +
        ", windowX: " + std::to_string(windowX) + ", windowY: " + std::to_string(windowY) + "\n" +
        ", pointerCount: " + std::to_string(pointerCount) + ", xByIndex: " + std::to_string(xByIndex) +
        ", yByIndex: " + std::to_string(yByIndex) +
        ", displayXByIndex: " + std::to_string(displayXByIndex) +
        ", displayYByIndex: " + std::to_string(displayYByIndex) +
        ", windowXByIndex: " + std::to_string(windowXByIndex) +
        ", windowYByIndex: " + std::to_string(windowYByIndex) + "\n" +
        ", pointerId: " + std::to_string(pointerId) + ", pressure: " + std::to_string(pressure) +
        ", action: " + std::to_string(action) + ", eventTime: " + std::to_string(eventTime) +
        ", sourceType: " + std::to_string(sourceType) + ", type: " + std::to_string(type);
    OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
                 "NdkAddInteractionEvent_eventInfoOfCommonEvent eventInfo = %{public}s", eventInfo.c_str());
};
// 创建一个单指点击手势
auto TapGesture = gestureApi->createTapGesture(COUNT_NUM_1, FINGERS_NUM_1);
// 将事件回调绑定到TapGesture上，触发手势后，通过回调函数处理手势事件
gestureApi->setGestureEventTarget(TapGesture,
                                  GESTURE_EVENT_ACTION_ACCEPT | GESTURE_EVENT_ACTION_UPDATE |
                                  GESTURE_EVENT_ACTION_END | GESTURE_EVENT_ACTION_CANCEL,
                                  column, onActionCallback);
// 将手势添加到column组件上，使column组件可以触发单指点击手势
gestureApi->addGestureToNode(column, TapGesture, ArkUI_GesturePriority::PARALLEL,
                             ArkUI_GestureMask::NORMAL_GESTURE_MASK);
```

## 自定义干预事件和手势的收集结果

从API版本26.0.0开始，在手势、触摸事件发起时，系统会收集已绑定手势、触摸识别器的识别结果。开发者可以在NODE\_ON\_GESTURE\_COLLECT\_INTERCEPT回调中对收集到的响应识别器和触摸识别器进行干预，通过设置收集干预策略来动态控制对识别器的收集行为，例如丢弃特定节点的识别结果等。

下面通过示例介绍如何实现自定义干预事件和手势的收集结果。

1. 注册NODE\_ON\_GESTURE\_COLLECT\_INTERCEPT节点事件并绑定回调处理函数。在回调中使用[OH\_ArkUI\_GestureCollectInterceptInfo\_GetResponseRecognizers](../harmonyos-references/capi-native-gesture-h.md#oh_arkui_gesturecollectinterceptinfo_getresponserecognizers)获取手势识别器、[OH\_ArkUI\_GestureCollectInterceptInfo\_GetTouchRecognizers](../harmonyos-references/capi-native-gesture-h.md#oh_arkui_gesturecollectinterceptinfo_gettouchrecognizers)获取触摸识别器，并结合处理函数完成干预。

   ```c
   nodeAPI->registerNodeEvent(row2, NODE_ON_GESTURE_COLLECT_INTERCEPT, 1, &row2);
   nodeAPI->addNodeEventReceiver(row2, [](ArkUI_NodeEvent *event) {
       if (OH_ArkUI_NodeEvent_GetEventType(event) == NODE_ON_GESTURE_COLLECT_INTERCEPT) {
           ArkUI_GestureCollectInterceptInfo *info = nullptr;
           ArkUI_GestureRecognizerHandleArray array;
           ArkUI_TouchRecognizerHandleArray arrayTouch;
           int32_t size;
           info = OH_ArkUI_NodeEvent_GetGestureCollectInterceptInfo(event);
           OH_ArkUI_GestureCollectInterceptInfo_GetTouchRecognizers(info, &arrayTouch, &size);
           OH_ArkUI_GestureCollectInterceptInfo_GetResponseRecognizers(info, &array, &size);
           int32_t uniqueId = 0;
           if (!GestureRecognizerModule(array, uniqueId, size, info)) {
               return;
           }
           TouchRecognizerModule(arrayTouch, size);
           OH_ArkUI_GestureCollectInterceptInfo_SetGestureCollectIntervention(
               info, OH_ArkUI_GestureCollectIntervention::OH_ARKUI_GESTURE_COLLECT_INTERVENTION_CONTINUE);
       } else if (OH_ArkUI_NodeEvent_GetEventType(event) == NODE_TOUCH_EVENT) {
           OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkEventGestureIntercept]",
                        "NdkEventGestureIntercept_SampleLog, row2 NODE_TOUCH_EVENT NodeEvent");
       }
   });
   ```
2. 创建手势收集干预处理函数，在处理函数中可调用以下接口对响应识别器和触摸识别器进行干预。

   * 通过[OH\_ArkUI\_GetGestureBindNodeUniqueId](../harmonyos-references/capi-native-gesture-h.md#oh_arkui_getgesturebindnodeuniqueid)接口获取绑定节点ID。
   * 通过[OH\_ArkUI\_GestureRecognizer\_IsHostBelongsTo](../harmonyos-references/capi-native-gesture-h.md#oh_arkui_gesturerecognizer_ishostbelongsto)接口判断手势识别器是否为指定节点的后代。
   * 通过[OH\_ArkUI\_TouchRecognizer\_IsHostBelongsTo](../harmonyos-references/capi-native-gesture-h.md#oh_arkui_touchrecognizer_ishostbelongsto)接口判断触摸识别器是否为指定节点的后代。
   * 通过[OH\_ArkUI\_GestureCollectInterceptInfo\_SetGestureCollectIntervention](../harmonyos-references/capi-native-gesture-h.md#oh_arkui_gesturecollectinterceptinfo_setgesturecollectintervention)接口设置收集干预策略。

   ```c
   // 处理手势识别器
   bool GestureRecognizerModule(ArkUI_GestureRecognizerHandleArray &array, int32_t &uniqueId, int32_t size,
                                ArkUI_GestureCollectInterceptInfo *info)
   {
       for (auto i = 0; i < size; i++) {
           OH_ArkUI_GetGestureBindNodeUniqueId(array[i], &uniqueId);
           if (OH_ArkUI_GestureRecognizer_IsHostBelongsTo(array[i], uniqueId)) {
               OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkEventGestureIntercept]",
                            "NdkEventGestureIntercept_SampleLog, gestureRecognizer isHostBelongsTo");
           }
           // 根据uniqueId判断事件是否来自右侧button
           if (uniqueId == g_buttonId) {
               OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkEventGestureIntercept]",
                            "NdkEventGestureIntercept_SampleLog, gestureRecognizer is from Button2");
               OH_ArkUI_GestureCollectInterceptInfo_SetGestureCollectIntervention(
                   info, OH_ArkUI_GestureCollectIntervention::OH_ARKUI_GESTURE_COLLECT_INTERVENTION_DISCARD_SELF);
               return false;
           }
       }
       return true;
   }
   // 处理触摸识别器
   void TouchRecognizerModule(ArkUI_TouchRecognizerHandleArray &arrayTouch, int32_t size)
   {
       for (auto i = 0; i < size; i++) {
           if (OH_ArkUI_TouchRecognizer_IsHostBelongsTo(arrayTouch[i], NODE_ID)) {
               OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkEventGestureIntercept]",
                            "NdkEventGestureIntercept_SampleLog, touchRecognizer isHostBelongsTo");
           } else {
               OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkEventGestureIntercept]",
                            "NdkEventGestureIntercept_SampleLog, touchRecognizer not isHostBelongsTo");
           }
       }
   }
   ```

**完整示例：**

完整示例请参考[示例工程](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NdkEventGestureIntercept)。
