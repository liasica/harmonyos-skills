---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-bind-gesture-events
title: 绑定手势事件
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 添加交互事件 > 绑定手势事件
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:06f7e6c89c748f17884d5305b9784f090994a5350e271fa55502165ba16745fb
---

ArkUI开发框架在NDK接口主要提供点击手势、滑动手势、快滑手势、长按手势、捏合手势和旋转手势，通过给指定的组件绑定不同的手势并设置相应的回调，实现期望的手势交互能力。

下面通过一个简单的示例来介绍如何实现手势绑定。

1. 创建一个Column节点，用于绑定手势。

   ```
   1. // 创建Column节点
   2. auto column = nodeAPI->createNode(ARKUI_NODE_COLUMN);
   3. // 设置背景色
   4. ArkUI_NumberValue value[] = {{.u32 = 0xff112233}};
   5. ArkUI_AttributeItem item = {value, 1};
   6. nodeAPI->setAttribute(column, NODE_BACKGROUND_COLOR, &item);
   7. // 设置宽度
   8. ArkUI_NumberValue widthValue[] = {{400}};
   9. ArkUI_AttributeItem width = {widthValue, 1};
   10. nodeAPI->setAttribute(column, NODE_WIDTH, &width);
   11. // 设置高度
   12. ArkUI_NumberValue heightValue[] = {{400}};
   13. ArkUI_AttributeItem height = {heightValue, 1};
   14. nodeAPI->setAttribute(column, NODE_HEIGHT, &height);
   ```

   [Function.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/Function.h#L380-L395)
2. 创建一个单指长按1秒并持续响应的长按手势。

   ```
   1. // 获取手势Native接口集合
   2. auto gestureApi = reinterpret_cast<ArkUI_NativeGestureAPI_1 *>(
   3. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_GESTURE, "ArkUI_NativeGestureAPI_1"));
   4. // 创建长按手势
   5. // DURATION_NUM_1000 = 1000
   6. auto longPressGesture = gestureApi->createLongPressGesture(1, true, DURATION_NUM_1000);
   ```

   [Function.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/Function.h#L249-L256)
3. 将创建的手势和步骤一中创建的Column节点绑定。

   ```
   1. auto onActionCallBack = [](ArkUI_GestureEvent *event, void *extraParam) {
   2. // 回调内容
   3. // ···
   4. };

   6. // 将手势设置到组件上
   7. gestureApi->setGestureEventTarget(
   8. longPressGesture, GESTURE_EVENT_ACTION_ACCEPT | GESTURE_EVENT_ACTION_UPDATE | GESTURE_EVENT_ACTION_END, column,
   9. onActionCallBack);

   11. gestureApi->addGestureToNode(column, longPressGesture, PARALLEL, NORMAL_GESTURE_MASK);
   ```

   [Function.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/Function.h#L403-L418)

## 单一手势

通过上文的示例已经了解了如何将手势绑定在节点上，接下来将分别介绍不同手势的创建方法。

* 点击手势

  通过给组件绑定点击手势可在组件被点击时触发此回调，可指定触发回调需要的点击次数和手指个数。

  ```
  1. // 获取手势Native接口集合
  2. auto gestureApi = reinterpret_cast<ArkUI_NativeGestureAPI_1 *>(
  3. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_GESTURE, "ArkUI_NativeGestureAPI_1"));
  4. // 创建点击手势
  5. auto tapGesture = gestureApi->createTapGesture(1, 1);
  ```

  [Function.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/Function.h#L225-L231)
* 滑动手势

  通过给组件绑定滑动手势可在用户滑动组件时触发回调，可指定触发回调需要的手指个数、滑动方向、滑动距离。单位为px。

  ```
  1. // 获取手势Native接口集合
  2. auto gestureApi = reinterpret_cast<ArkUI_NativeGestureAPI_1 *>(
  3. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_GESTURE, "ArkUI_NativeGestureAPI_1"));
  4. // 创建滑动手势
  5. auto panGesture = gestureApi->createPanGesture(1, GESTURE_DIRECTION_ALL, 1);
  ```

  [Function.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/Function.h#L237-L243)
* 长按手势

  通过给组件绑定长按手势可在用户长按组件时触发回调，可指定触发回调需要的手指个数、长按时间（单位毫秒）、是否连续触发。

  ```
  1. // 获取手势Native接口集合
  2. auto gestureApi = reinterpret_cast<ArkUI_NativeGestureAPI_1 *>(
  3. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_GESTURE, "ArkUI_NativeGestureAPI_1"));
  4. // 创建长按手势
  5. // DURATION_NUM_1000 = 1000
  6. auto longPressGesture = gestureApi->createLongPressGesture(1, true, DURATION_NUM_1000);
  ```

  [Function.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/Function.h#L249-L256)
* 捏合手势

  通过给组件绑定捏合手势可在用户捏合组件时触发回调，可指定触发回调需要的手指个数（最小为2）、捏合距离（单位px）。

  ```
  1. // 获取手势Native接口集合
  2. auto gestureApi = reinterpret_cast<ArkUI_NativeGestureAPI_1 *>(
  3. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_GESTURE, "ArkUI_NativeGestureAPI_1"));
  4. // 创建捏合手势
  5. // NUMBER_2 = 2，NUMBER_10 = 10
  6. auto pinchGesture = gestureApi->createPinchGesture(NUMBER_2, NUMBER_10);
  ```

  [Function.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/Function.h#L262-L269)
* 旋转手势

  通过给组件绑定旋转手势可在用户旋转组件时触发回调，可指定触发回调需要的手指个数（最小为2）、旋转角度。

  ```
  1. // 获取手势Native接口集合
  2. auto gestureApi = reinterpret_cast<ArkUI_NativeGestureAPI_1 *>(
  3. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_GESTURE, "ArkUI_NativeGestureAPI_1"));
  4. // 创建旋转手势
  5. // NUMBER_2 = 2，NUMBER_10 = 10
  6. auto rotationGesture = gestureApi->createRotationGesture(NUMBER_2, NUMBER_10);
  ```

  [Function.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/Function.h#L275-L282)
* 快滑手势

  通过给组件绑定快滑手势可在用户快速滑动组件时触发回调，可指定触发回调需要的手指个数（最小为1）、滑动方向、滑动速度（单位px/s）。

  ```
  1. // 获取手势Native接口集合
  2. auto gestureApi = reinterpret_cast<ArkUI_NativeGestureAPI_1 *>(
  3. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_GESTURE, "ArkUI_NativeGestureAPI_1"));
  4. // 创建快滑手势
  5. // SPEED_NUM_50 = 50
  6. auto swipeGesture = gestureApi->createSwipeGesture(1, GESTURE_DIRECTION_ALL, SPEED_NUM_50);
  ```

  [Function.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/Function.h#L288-L295)

## 组合手势

可以将多个不同类型的手势组合在一起，形成一个手势组，这个手势组可以作为一个识别整体，达到对用户多个不同类型手势序列的识别目的。

通过设置[ArkUI\_GroupGestureMode](../harmonyos-references/capi-native-gesture-h.md#arkui_groupgesturemode)来指定这个手势组的识别模式，即组内的手势之间的关系，包含顺序识别SEQUENTIAL\_GROUP，并行识别PARALLEL\_GROUP，互斥识别EXCLUSIVE\_GROUP。

### 顺序识别

顺序识别组合手势对应的ArkUI\_GroupGestureMode为SEQUENTIAL\_GROUP。顺序识别组合手势将按照手势的注册顺序识别手势，直到所有的手势识别成功。当顺序识别组合手势中有一个手势识别失败时，后续手势识别均失败。顺序识别手势组仅有最后一个手势可以响应[GESTURE\_EVENT\_ACTION\_END](../harmonyos-references/capi-native-gesture-h.md#arkui_gestureeventactiontype)。

以顺序识别长按和滑动手势为例：

```
1. // LongPressAndSwipeGesture.h
2. #include <arkui/native_animate.h>
3. #include <arkui/native_gesture.h>
4. #include <arkui/native_interface.h>
5. #include <arkui/native_node.h>
6. #include <arkui/native_type.h>
7. #include <arkui/native_node_napi.h>
8. #include <hilog/log.h>
9. #include "Common.h"
10. #include "Function.h"
11. // ...
12. ArkUI_NodeHandle LongPressAndSwipeGesture()
13. {
14. auto column = nodeAPI->createNode(ARKUI_NODE_COLUMN);

16. // 创建节点
17. ArkUI_NumberValue value[] = {{.u32 = 0xff112233}};
18. ArkUI_AttributeItem item = {value, ITEM_SIZE_ONE};
19. nodeAPI->setAttribute(column, NODE_BACKGROUND_COLOR, &item);
20. ArkUI_NumberValue widthValue[] = {{WIDTH_SIZE}};
21. ArkUI_AttributeItem width = {widthValue, ITEM_SIZE_ONE};
22. nodeAPI->setAttribute(column, NODE_WIDTH, &width);
23. ArkUI_NumberValue heightValue[] = {{HEIGHT_SIZE}};
24. ArkUI_AttributeItem height = {heightValue, ITEM_SIZE_ONE};
25. nodeAPI->setAttribute(column, NODE_HEIGHT, &height);

27. // 判断是否支持创建手势
28. auto gestureApi = reinterpret_cast<ArkUI_NativeGestureAPI_1 *>(
29. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_GESTURE, "ArkUI_NativeGestureAPI_1"));
30. if (gestureApi->createGroupGesture) {
31. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
32. "NdkAddInteractionEvent_GestureSampleLog, createGroupGesture api exist");
33. } else {
34. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
35. "NdkAddInteractionEvent_GestureSampleLog, createGroupGesture api not exist");
36. }
37. auto groupGesture = gestureApi->createGroupGesture(ArkUI_GroupGestureMode::SEQUENTIAL_GROUP);

39. // 创建长按手势
40. auto longPressGesture = gestureApi->createLongPressGesture(FINGERS_NUM, true, DURATION_NUM);
41. if (gestureApi->getGestureType) {
42. ArkUI_GestureRecognizerType type = gestureApi->getGestureType(longPressGesture);
43. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
44. "NdkAddInteractionEvent_GestureSampleLog longPressGesture,"
45. "ArkUI_GestureRecognizerType%{public}d", type);
46. }
47. // 给长按手势绑定回调
48. auto onActionCallBackPanLongPress = [](ArkUI_GestureEvent *event, void *extraParam) {
49. ArkUI_GestureEventActionType actionType = OH_ArkUI_GestureEvent_GetActionType(event);

51. float velocity = OH_ArkUI_PanGesture_GetVelocity(event);
52. float velocityX = OH_ArkUI_PanGesture_GetVelocityX(event);
53. float velocityY = OH_ArkUI_PanGesture_GetVelocityY(event);
54. float offsetX = OH_ArkUI_PanGesture_GetOffsetX(event);
55. float offsetY = OH_ArkUI_PanGesture_GetOffsetY(event);
56. float scale = OH_ArkUI_PinchGesture_GetScale(event);
57. float centerX = OH_ArkUI_PinchGesture_GetCenterX(event);
58. float centerY = OH_ArkUI_PinchGesture_GetCenterY(event);
59. float angle = OH_ArkUI_SwipeGesture_GetAngle(event);
60. float velocityS = OH_ArkUI_SwipeGesture_GetVelocity(event);
61. float angleR = OH_ArkUI_RotationGesture_GetAngle(event);
62. float repeat = OH_ArkUI_LongPress_GetRepeatCount(event);

64. OH_LOG_Print(
65. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
66. "NdkAddInteractionEvent_GestureSampleLog,longPressGesturecallback actionType:%{public}d,"
67. "velocity%{public}f,velocityX%{public}f;"
68. "velocityY%{public}f,offsetX%{public}f,offsetY%{public}f,scale%{public}fcenterX"
69. "%{public}fcenterY"
70. "%{public}fangle%{public}fvelocityS%{public}fangleR%{public}frepeat%{public}f",
71. actionType, velocity, velocityX, velocityY, offsetX, offsetY, scale, centerX, centerY, angle, velocityS,
72. angleR, repeat);
73. };
74. gestureApi->setGestureEventTarget(longPressGesture,
75. GESTURE_EVENT_ACTION_ACCEPT | GESTURE_EVENT_ACTION_UPDATE |
76. GESTURE_EVENT_ACTION_CANCEL, column, onActionCallBackPanLongPress);

78. // 将长按手势添加到手势组
79. if (gestureApi->addChildGesture) {
80. gestureApi->addChildGesture(groupGesture, longPressGesture);
81. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
82. "NdkAddInteractionEvent_GestureSampleLog, addChildGesture longPressGesture");
83. }
84. // 创建快滑手势 swipe
85. auto swipeGesture = gestureApi->createSwipeGesture(1, GESTURE_DIRECTION_ALL, 100);
86. if (gestureApi->getGestureType) {
87. ArkUI_GestureRecognizerType type = gestureApi->getGestureType(swipeGesture);
88. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
89. "NdkAddInteractionEvent_GestureSampleLog, ArkUI_GestureRecognizerType %{public}d",
90. type);
91. }
92. // 给快滑手势绑定回调
93. auto onActionCallBack = [](ArkUI_GestureEvent *event, void *extraParam) {
94. ArkUI_GestureEventActionType actionType = OH_ArkUI_GestureEvent_GetActionType(event);

96. float velocity = OH_ArkUI_PanGesture_GetVelocity(event);
97. float velocityX = OH_ArkUI_PanGesture_GetVelocityX(event);
98. float velocityY = OH_ArkUI_PanGesture_GetVelocityY(event);
99. float offsetX = OH_ArkUI_PanGesture_GetOffsetX(event);
100. float offsetY = OH_ArkUI_PanGesture_GetOffsetY(event);
101. float scale = OH_ArkUI_PinchGesture_GetScale(event);
102. float centerX = OH_ArkUI_PinchGesture_GetCenterX(event);
103. float centerY = OH_ArkUI_PinchGesture_GetCenterY(event);
104. float angle = OH_ArkUI_SwipeGesture_GetAngle(event);
105. float velocityS = OH_ArkUI_SwipeGesture_GetVelocity(event);
106. float angleR = OH_ArkUI_RotationGesture_GetAngle(event);
107. float repeat = OH_ArkUI_LongPress_GetRepeatCount(event);

109. // 通过日志查看
110. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
111. "NdkAddInteractionEvent_GestureSampleLog, swipeGesture "
112. "callback actionType: %{public}d, velocity %{public}f,velocityX "
113. "%{public}f; "
114. "velocityY %{public}f, offsetX %{public}f, offsetY %{public}f, scale %{public}fcenterX "
115. "%{public}f centerY"
116. " %{public}f angle %{public}f velocityS %{public}f angleR %{public}f repeat %{public}f",
117. actionType, velocity, velocityX, velocityY, offsetX, offsetY, scale, centerX, centerY, angle,
118. velocityS, angleR, repeat);

120. ArkUI_NumberValue value[] = {{.f32 = 0}, {.f32 = 0}, {.f32 = 0}, {.f32 = angleR}, {.f32 = 0}};
121. ArkUI_AttributeItem item = {value, ITEM_SIZE_FIVE};
122. auto column = reinterpret_cast<ArkUI_NodeHandle>(extraParam);
123. nodeAPI->setAttribute(column, NODE_ROTATE, &item);
124. };

126. gestureApi->setGestureEventTarget(
127. swipeGesture, GESTURE_EVENT_ACTION_ACCEPT | GESTURE_EVENT_ACTION_UPDATE | GESTURE_EVENT_ACTION_END, column,
128. onActionCallBack);

130. // 将快滑手势添加到手势组
131. if (gestureApi->addChildGesture) {
132. gestureApi->addChildGesture(groupGesture, swipeGesture);
133. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
134. "NdkAddInteractionEvent_GestureSampleLog, addChildGesture swipeGesture");
135. }
136. // 将手势组设置到组件上
137. gestureApi->addGestureToNode(column, groupGesture, PRIORITY, NORMAL_GESTURE_MASK);
138. return column;
139. }
```

[LongPressAndSwipeGesture.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/LongPressAndSwipeGesture.h#L18-L160)

**完整示例：**

完整示例请参考[示例工程](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/ArkUISample/NdkAddInteractionEvent)。

### 并行识别

并行识别组合手势对应的ArkUI\_GroupGestureMode为PARALLEL\_GROUP。并行识别组合手势中注册的手势将同时进行识别，直到所有手势识别结束。并行识别手势组合中的手势进行识别时互不影响。

以并行识别长按和快滑手势为例：

```
1. // LongPressAndFlickGesture.h
2. #include <arkui/native_animate.h>
3. #include <arkui/native_gesture.h>
4. #include <arkui/native_interface.h>
5. #include <arkui/native_node.h>
6. #include <arkui/native_type.h>
7. #include <arkui/native_node_napi.h>
8. #include <hilog/log.h>
9. #include "Common.h"
10. #include "Function.h"
11. // ...

13. ArkUI_NodeHandle LongPressAndFlickGesture()
14. {
15. auto column = nodeAPI->createNode(ARKUI_NODE_COLUMN);

17. // 创建节点
18. ArkUI_NumberValue value[] = {{.u32 = 0xff112233}};
19. ArkUI_AttributeItem item = {value, ITEM_SIZE_ONE};
20. nodeAPI->setAttribute(column, NODE_BACKGROUND_COLOR, &item);
21. ArkUI_NumberValue widthValue[] = {{WIDTH_SIZE}};
22. ArkUI_AttributeItem width = {widthValue, ITEM_SIZE_ONE};
23. nodeAPI->setAttribute(column, NODE_WIDTH, &width);
24. ArkUI_NumberValue heightValue[] = {{HEIGHT_SIZE}};
25. ArkUI_AttributeItem height = {heightValue, ITEM_SIZE_ONE};
26. nodeAPI->setAttribute(column, NODE_HEIGHT, &height);

28. // 判断是否支持创建手势
29. auto gestureApi = reinterpret_cast<ArkUI_NativeGestureAPI_1 *>(
30. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_GESTURE, "ArkUI_NativeGestureAPI_1"));
31. if (gestureApi->createGroupGesture) {
32. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
33. "NdkAddInteractionEvent_GestureSampleLog, createGroupGesture api exist");
34. } else {
35. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
36. "NdkAddInteractionEvent_GestureSampleLog, createGroupGesture api not exist");
37. }

39. // 创建手势组
40. auto groupGesture = gestureApi->createGroupGesture(ArkUI_GroupGestureMode::PARALLEL_GROUP);

42. // 创建长按手势
43. auto longPressGesture = gestureApi->createLongPressGesture(FINGERS_NUM, true, DURATION_NUM_500);
44. if (gestureApi->getGestureType) {
45. ArkUI_GestureRecognizerType type = gestureApi->getGestureType(longPressGesture);
46. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
47. "NdkAddInteractionEvent_GestureSampleLog,ArkUI_GestureRecognizerType%{public}d", type);
48. }
49. // 给长按手势绑定回调
50. auto onActionCallBackPanLongPress = [](ArkUI_GestureEvent *event, void *extraParam) {
51. ArkUI_GestureEventActionType actionType = OH_ArkUI_GestureEvent_GetActionType(event);

53. float velocity = OH_ArkUI_PanGesture_GetVelocity(event);
54. float velocityX = OH_ArkUI_PanGesture_GetVelocityX(event);
55. float velocityY = OH_ArkUI_PanGesture_GetVelocityY(event);
56. float offsetX = OH_ArkUI_PanGesture_GetOffsetX(event);
57. float offsetY = OH_ArkUI_PanGesture_GetOffsetY(event);
58. float scale = OH_ArkUI_PinchGesture_GetScale(event);
59. float centerX = OH_ArkUI_PinchGesture_GetCenterX(event);
60. float centerY = OH_ArkUI_PinchGesture_GetCenterY(event);
61. float angle = OH_ArkUI_SwipeGesture_GetAngle(event);
62. float velocityS = OH_ArkUI_SwipeGesture_GetVelocity(event);
63. float angleR = OH_ArkUI_RotationGesture_GetAngle(event);
64. float repeat = OH_ArkUI_LongPress_GetRepeatCount(event);

66. OH_LOG_Print(
67. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
68. "NdkAddInteractionEvent_GestureSampleLog,longPressGesturecallback actionType:%{public}d,"
69. "velocity%{public}f,velocityX%{public}f;"
70. "velocityY%{public}f,offsetX%{public}f,offsetY%{public}f,scale%{public}f, centerX "
71. "%{public}fcenterY"
72. "%{public}fangle%{public}fvelocityS%{public}fangleR%{public}frepeat%{public}f",
73. actionType, velocity, velocityX, velocityY, offsetX, offsetY, scale, centerX, centerY, angle, velocityS,
74. angleR, repeat);
75. };
76. gestureApi->setGestureEventTarget(longPressGesture,
77. GESTURE_EVENT_ACTION_ACCEPT | GESTURE_EVENT_ACTION_UPDATE |
78. GESTURE_EVENT_ACTION_CANCEL,
79. column, onActionCallBackPanLongPress);

81. // 将长按手势添加到手势组
82. if (gestureApi->addChildGesture) {
83. gestureApi->addChildGesture(groupGesture, longPressGesture);
84. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
85. "NdkAddInteractionEvent_GestureSampleLog, addChildGesture longPressGesture");
86. }
87. // 创建快滑手势 swipe
88. auto swipeGesture = gestureApi->createSwipeGesture(FINGERS_NUM, GESTURE_DIRECTION_ALL, DURATION_NUM_100);
89. if (gestureApi->getGestureType) {
90. ArkUI_GestureRecognizerType type = gestureApi->getGestureType(swipeGesture);
91. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
92. "NdkAddInteractionEvent_GestureSampleLog, ArkUI_GestureRecognizerType %{public}d",
93. type);
94. }
95. // 给快滑手势绑定回调
96. auto onActionCallBack = [](ArkUI_GestureEvent *event, void *extraParam) {
97. ArkUI_GestureEventActionType actionType = OH_ArkUI_GestureEvent_GetActionType(event);

99. float velocity = OH_ArkUI_PanGesture_GetVelocity(event);
100. float velocityX = OH_ArkUI_PanGesture_GetVelocityX(event);
101. float velocityY = OH_ArkUI_PanGesture_GetVelocityY(event);
102. float offsetX = OH_ArkUI_PanGesture_GetOffsetX(event);
103. float offsetY = OH_ArkUI_PanGesture_GetOffsetY(event);
104. float scale = OH_ArkUI_PinchGesture_GetScale(event);
105. float centerX = OH_ArkUI_PinchGesture_GetCenterX(event);
106. float centerY = OH_ArkUI_PinchGesture_GetCenterY(event);
107. float angle = OH_ArkUI_SwipeGesture_GetAngle(event);
108. float velocityS = OH_ArkUI_SwipeGesture_GetVelocity(event);
109. float angleR = OH_ArkUI_RotationGesture_GetAngle(event);
110. float repeat = OH_ArkUI_LongPress_GetRepeatCount(event);

112. // 通过日志查看
113. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
114. "NdkAddInteractionEvent_GestureSampleLog, swipeGesture "
115. "callback actionType: %{public}d, velocity%{public}f,velocityX "
116. "%{public}f; "
117. "velocityY %{public}f, offsetX %{public}f, offsetY %{public}f, scale %{public}f, centerX "
118. "%{public}f centerY"
119. " %{public}f angle %{public}f velocityS %{public}f angleR %{public}f repeat %{public}f",
120. actionType, velocity, velocityX, velocityY, offsetX, offsetY, scale, centerX, centerY, angle,
121. velocityS, angleR, repeat);

123. ArkUI_NumberValue value[] = {{.f32 = 0}, {.f32 = 0}, {.f32 = 0}, {.f32 = angleR}, {.f32 = 0}};
124. ArkUI_AttributeItem item = {value, ITEM_SIZE_FIVE};
125. auto column = reinterpret_cast<ArkUI_NodeHandle>(extraParam);
126. nodeAPI->setAttribute(column, NODE_ROTATE, &item);
127. };

129. gestureApi->setGestureEventTarget(
130. swipeGesture, GESTURE_EVENT_ACTION_ACCEPT | GESTURE_EVENT_ACTION_UPDATE | GESTURE_EVENT_ACTION_END, column,
131. onActionCallBack);

133. // 将快滑手势添加到手势组
134. if (gestureApi->addChildGesture) {
135. gestureApi->addChildGesture(groupGesture, swipeGesture);
136. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
137. "NdkAddInteractionEvent_GestureSampleLog, addChildGesture swipeGesture");
138. }
139. // 将手势组设置到组件上
140. gestureApi->addGestureToNode(column, groupGesture, PRIORITY, NORMAL_GESTURE_MASK);
141. return column;
142. }
```

[LongPressAndFlickGesture.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/LongPressAndFlickGesture.h#L18-L163)

**完整示例：**

完整示例请参考[示例工程](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/ArkUISample/NdkAddInteractionEvent)。

### 互斥识别

互斥识别组合手势对应的ArkUI\_GroupGestureMode为EXCLUSIVE\_GROUP。互斥识别组合手势中注册的手势将同时进行识别，若有一个手势识别成功，则结束手势识别，其他所有手势识别失败。

以互斥识别滑动手势和捏合手势为例：

```
1. // SwipeAndPinchExclusiveGesture.h
2. #include <arkui/native_animate.h>
3. #include <arkui/native_gesture.h>
4. #include <arkui/native_interface.h>
5. #include <arkui/native_node.h>
6. #include <arkui/native_type.h>
7. #include <arkui/native_node_napi.h>
8. #include <hilog/log.h>
9. #include "Common.h"
10. #include "Function.h"
11. // ...

13. ArkUI_NodeHandle SwipeAndPinchExclusiveGesture()
14. {
15. OH_ArkUI_GetModuleInterface(ARKUI_NATIVE_NODE, ArkUI_NativeNodeAPI_1, nodeAPI);
16. if (nodeAPI == nullptr) {
17. return nullptr;
18. }
19. auto column = nodeAPI->createNode(ARKUI_NODE_COLUMN);

21. // 创建节点
22. ArkUI_NumberValue value[] = {{.u32 = 0xff112233}};
23. ArkUI_AttributeItem item = {value, 1};
24. nodeAPI->setAttribute(column, NODE_BACKGROUND_COLOR, &item);
25. ArkUI_NumberValue widthValue[] = {{WIDTH_SIZE}};
26. ArkUI_AttributeItem width = {widthValue, ITEM_SIZE_ONE};
27. nodeAPI->setAttribute(column, NODE_WIDTH, &width);
28. ArkUI_NumberValue heightValue[] = {{HEIGHT_SIZE}};
29. ArkUI_AttributeItem height = {heightValue, ITEM_SIZE_ONE};
30. nodeAPI->setAttribute(column, NODE_HEIGHT, &height);

32. // 判断是否支持创建手势
33. auto gestureApi = reinterpret_cast<ArkUI_NativeGestureAPI_1 *>(
34. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_GESTURE, "ArkUI_NativeGestureAPI_1"));
35. if (gestureApi->createGroupGesture) {
36. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
37. "NdkAddInteractionEvent_GestureSampleLog, createGroupGesture api exist");
38. } else {
39. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
40. "NdkAddInteractionEvent_GestureSampleLog, createGroupGesture api not exist");
41. }
42. auto groupGesture = gestureApi->createGroupGesture(ArkUI_GroupGestureMode::EXCLUSIVE_GROUP);

44. // 创建滑动手势
45. auto panGesture = gestureApi->createPanGesture(FINGERS_NUM, GESTURE_DIRECTION_VERTICAL, DURATION_NUM);
46. if (gestureApi->getGestureType) {
47. ArkUI_GestureRecognizerType type = gestureApi->getGestureType(panGesture);
48. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
49. "NdkAddInteractionEvent_GestureSampleLog panGesture, ArkUI_GestureRecognizerType %{public}d",
50. type);
51. }
52. // 给滑动手势绑定回调
53. auto onActionCallBackPan = [](ArkUI_GestureEvent *event, void *extraParam) {
54. ArkUI_GestureEventActionType actionType = OH_ArkUI_GestureEvent_GetActionType(event);

56. float velocity = OH_ArkUI_PanGesture_GetVelocity(event);
57. float velocityX = OH_ArkUI_PanGesture_GetVelocityX(event);
58. float velocityY = OH_ArkUI_PanGesture_GetVelocityY(event);
59. float offsetX = OH_ArkUI_PanGesture_GetOffsetX(event);
60. float offsetY = OH_ArkUI_PanGesture_GetOffsetY(event);
61. float scale = OH_ArkUI_PinchGesture_GetScale(event);
62. float centerX = OH_ArkUI_PinchGesture_GetCenterX(event);
63. float centerY = OH_ArkUI_PinchGesture_GetCenterY(event);
64. float angle = OH_ArkUI_SwipeGesture_GetAngle(event);
65. float velocityS = OH_ArkUI_SwipeGesture_GetVelocity(event);
66. float angleR = OH_ArkUI_RotationGesture_GetAngle(event);
67. float repeat = OH_ArkUI_LongPress_GetRepeatCount(event);

69. // 通过日志查看
70. OH_LOG_Print(
71. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
72. "NdkAddInteractionEvent_GestureSampleLog, panGesture callback actionType: %{public}d, "
73. "velocity %{public}f,velocityX %{public}f; "
74. "velocityY %{public}f, offsetX %{public}f, offsetY %{public}f, scale %{public}fcenterX "
75. "%{public}f centerY"
76. " %{public}f angle %{public}f velocityS %{public}f angleR %{public}f repeat %{public}f",
77. actionType, velocity, velocityX, velocityY, offsetX, offsetY, scale, centerX, centerY, angle, velocityS,
78. angleR, repeat);
79. };
80. gestureApi->setGestureEventTarget(panGesture,
81. GESTURE_EVENT_ACTION_ACCEPT | GESTURE_EVENT_ACTION_UPDATE |
82. GESTURE_EVENT_ACTION_END | GESTURE_EVENT_ACTION_CANCEL,
83. column, onActionCallBackPan);
84. // 将滑动手势添加到手势组
85. if (gestureApi->addChildGesture) {
86. gestureApi->addChildGesture(groupGesture, panGesture);
87. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
88. "NdkAddInteractionEvent_GestureSampleLog, addChildGesture panGesture");
89. }
90. // 创建捏合手势
91. auto pinchGesture = gestureApi->createPinchGesture(0, 0);
92. if (gestureApi->getGestureType) {
93. ArkUI_GestureRecognizerType type = gestureApi->getGestureType(pinchGesture);
94. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
95. "NdkAddInteractionEvent_GestureSampleLog pinchGesture, "
96. "ArkUI_GestureRecognizerType %{public}d", type);
97. }
98. // 给捏合手势绑定回调
99. auto onActionCallBack = [](ArkUI_GestureEvent *event, void *extraParam) {
100. ArkUI_GestureEventActionType actionType = OH_ArkUI_GestureEvent_GetActionType(event);

102. float velocity = OH_ArkUI_PanGesture_GetVelocity(event);
103. float velocityX = OH_ArkUI_PanGesture_GetVelocityX(event);
104. float velocityY = OH_ArkUI_PanGesture_GetVelocityY(event);
105. float offsetX = OH_ArkUI_PanGesture_GetOffsetX(event);
106. float offsetY = OH_ArkUI_PanGesture_GetOffsetY(event);
107. float scale = OH_ArkUI_PinchGesture_GetScale(event);
108. float centerX = OH_ArkUI_PinchGesture_GetCenterX(event);
109. float centerY = OH_ArkUI_PinchGesture_GetCenterY(event);
110. float angle = OH_ArkUI_SwipeGesture_GetAngle(event);
111. float velocityS = OH_ArkUI_SwipeGesture_GetVelocity(event);
112. float angleR = OH_ArkUI_RotationGesture_GetAngle(event);
113. float repeat = OH_ArkUI_LongPress_GetRepeatCount(event);

115. OH_LOG_Print(
116. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
117. "NdkAddInteractionEvent_GestureSampleLog, pinchGesture callback actionType: %{public}d, "
118. "velocity %{public}f,velocityX %{public}f; "
119. "velocityY %{public}f, offsetX %{public}f, offsetY %{public}f, scale %{public}fcenterX "
120. "%{public}f centerY"
121. " %{public}f angle %{public}f velocityS %{public}f angleR %{public}f repeat %{public}f",
122. actionType, velocity, velocityX, velocityY, offsetX, offsetY, scale, centerX, centerY, angle, velocityS,
123. angleR, repeat);
124. ArkUI_NumberValue value[] = {{.f32 = scale}, {.f32 = scale}};
125. ArkUI_AttributeItem item = {value, ITEM_SIZE_TWO};
126. auto column = reinterpret_cast<ArkUI_NodeHandle>(extraParam);
127. nodeAPI->setAttribute(column, NODE_SCALE, &item);
128. };
129. gestureApi->setGestureEventTarget(pinchGesture,
130. GESTURE_EVENT_ACTION_ACCEPT | GESTURE_EVENT_ACTION_UPDATE |
131. GESTURE_EVENT_ACTION_END | GESTURE_EVENT_ACTION_CANCEL,
132. column, onActionCallBack);
133. // 将捏合手势添加到手势组
134. if (gestureApi->addChildGesture) {
135. gestureApi->addChildGesture(groupGesture, pinchGesture);
136. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
137. "NdkAddInteractionEvent_GestureSampleLog, addChildGesture pinchGesture");
138. }
139. // 将手势组设置到组件上
140. gestureApi->addGestureToNode(column, groupGesture, PRIORITY, NORMAL_GESTURE_MASK);
141. return column;
142. }
```

[SwipeAndPinchExclusiveGesture.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/SwipeAndPinchExclusiveGesture.h#L18-L163)

**完整示例：**

完整示例请参考[示例工程](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/ArkUISample/NdkAddInteractionEvent)。

### 自定义手势判定

当用户的操作符合某个手势识别器，该识别器即将触发成功时，可通过自定义手势判定能力来动态决策，是否希望该识别器被系统认定为识别成功。通过setGestureInterrupterToNode接口，绑定一个回调在该组件上，但组件上的某个手势即将识别成功时，通过返回CONTINUE或REJECT来决定是否将成功机会让给其它手势识别器。

在上文绑定手势事件的示例中按照如下方式进行调整即可实现自定义手势判定。

1. 创建自定义手势判定回调。

   ```
   1. auto onInterruptCallback = [](ArkUI_GestureInterruptInfo *info) -> ArkUI_GestureInterruptResult {
   2. // 获取是否系统手势
   3. auto sysTag = OH_ArkUI_GestureInterruptInfo_GetSystemFlag(info);
   4. // 获取拦截的手势指针
   5. auto recognizer = OH_ArkUI_GestureInterruptInfo_GetRecognizer(info);
   6. // 获取系统手势类型
   7. auto systemRecognizerType = OH_ArkUI_GestureInterruptInfo_GetSystemRecognizerType(info);
   8. // 获取手势事件
   9. auto gestureEvent = OH_ArkUI_GestureInterruptInfo_GetGestureEvent(info);
   10. auto inputEvent = OH_ArkUI_GestureEvent_GetRawInputEvent(gestureEvent);
   11. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
   12. "NdkAddInteractionEvent_eventInfo longPressGesture");
   13. if (sysTag) {
   14. // 如果是系统手势则不拦截
   15. return GESTURE_INTERRUPT_RESULT_CONTINUE;
   16. } else {
   17. // 不是系统手势则拒绝
   18. return GESTURE_INTERRUPT_RESULT_REJECT;
   19. }
   20. };
   ```

   [Function.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/Function.h#L419-L440)
2. 绑定手势判定和节点。

   ```
   1. gestureApi->setGestureInterrupterToNode(column, onInterruptCallback);
   ```

   [Function.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/Function.h#L441-L443)

经过上述修改，将原本可以生效的长按手势做了拦截，即，此时再对Column节点长按将不会触发长按的手势回调。

## 获取事件信息

绑定手势事件已详细说明如何将手势绑定到节点上。在回调执行时，ArkUI框架提供了[OH\_ArkUI\_GestureEvent\_GetRawInputEvent()](../harmonyos-references/capi-native-gesture-h.md#oh_arkui_gestureevent_getrawinputevent)接口，可从手势事件中获取基础事件对象。之后，可通过调用[OH\_ArkUI\_PointerEvent\_GetDisplayX()](../harmonyos-references/capi-ui-input-event-h.md#oh_arkui_pointerevent_getdisplayx)、[OH\_ArkUI\_PointerEvent\_GetDisplayXByIndex()](../harmonyos-references/capi-ui-input-event-h.md#oh_arkui_pointerevent_getdisplayxbyindex)、[OH\_ArkUI\_UIInputEvent\_GetAction()](../harmonyos-references/capi-ui-input-event-h.md#oh_arkui_uiinputevent_getaction)和[OH\_ArkUI\_UIInputEvent\_GetEventTime()](../harmonyos-references/capi-ui-input-event-h.md#oh_arkui_uiinputevent_geteventtime)等接口，从基础事件中获取更多信息。应用依据获取的信息，在手势事件执行过程中实现差异化交互逻辑。

```
1. // 设置回调，在触发手势事件时执行回调处理手势事件
2. auto onActionCallback = [](ArkUI_GestureEvent *event, void *extraParams) {
3. // 从手势事件获取基础事件对象
4. auto *inputEvent = OH_ArkUI_GestureEvent_GetRawInputEvent(event);
5. // 从基础事件获取事件信息
6. auto x = OH_ArkUI_PointerEvent_GetX(inputEvent);
7. auto y = OH_ArkUI_PointerEvent_GetY(inputEvent);
8. auto displayX = OH_ArkUI_PointerEvent_GetDisplayX(inputEvent);
9. auto displayY = OH_ArkUI_PointerEvent_GetDisplayY(inputEvent);
10. auto windowX = OH_ArkUI_PointerEvent_GetWindowX(inputEvent);
11. auto windowY = OH_ArkUI_PointerEvent_GetWindowY(inputEvent);
12. auto pointerCount = OH_ArkUI_PointerEvent_GetPointerCount(inputEvent);
13. auto xByIndex = OH_ArkUI_PointerEvent_GetXByIndex(inputEvent, 0);
14. auto yByIndex = OH_ArkUI_PointerEvent_GetYByIndex(inputEvent, 0);
15. auto displayXByIndex = OH_ArkUI_PointerEvent_GetDisplayXByIndex(inputEvent, 0);
16. auto displayYByIndex = OH_ArkUI_PointerEvent_GetDisplayYByIndex(inputEvent, 0);
17. auto windowXByIndex = OH_ArkUI_PointerEvent_GetWindowXByIndex(inputEvent, 0);
18. auto windowYByIndex = OH_ArkUI_PointerEvent_GetWindowYByIndex(inputEvent, 0);
19. auto pointerId = OH_ArkUI_PointerEvent_GetPointerId(inputEvent, 0);
20. auto pressure = OH_ArkUI_PointerEvent_GetPressure(inputEvent, 0);
21. auto action = OH_ArkUI_UIInputEvent_GetAction(inputEvent);
22. auto eventTime = OH_ArkUI_UIInputEvent_GetEventTime(inputEvent);
23. auto sourceType = OH_ArkUI_UIInputEvent_GetSourceType(inputEvent);
24. auto type = OH_ArkUI_UIInputEvent_GetType(inputEvent);
25. std::string eventInfo =
26. "x: " + std::to_string(x) + ", y: " + std::to_string(y) +
27. ", displayX: " + std::to_string(displayX) + ", displayY: " + std::to_string(displayY) +
28. ", windowX: " + std::to_string(windowX) + ", windowY: " + std::to_string(windowY) + "\n" +
29. ", pointerCount: " + std::to_string(pointerCount) + ", xByIndex: " + std::to_string(xByIndex) +
30. ", yByIndex: " + std::to_string(yByIndex) +
31. ", displayXByIndex: " + std::to_string(displayXByIndex) +
32. ", displayYByIndex: " + std::to_string(displayYByIndex) +
33. ", windowXByIndex: " + std::to_string(windowXByIndex) +
34. ", windowYByIndex: " + std::to_string(windowYByIndex) + "\n" +
35. ", pointerId: " + std::to_string(pointerId) + ", pressure: " + std::to_string(pressure) +
36. ", action: " + std::to_string(action) + ", eventTime: " + std::to_string(eventTime) +
37. ", sourceType: " + std::to_string(sourceType) + ", type: " + std::to_string(type);
38. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
39. "NdkAddInteractionEvent_eventInfoOfCommonEvent eventInfo = %{public}s", eventInfo.c_str());
40. };
41. // 创建一个单指点击手势
42. auto TapGesture = gestureApi->createTapGesture(COUNT_NUM_1, FINGERS_NUM_1);
43. // 将事件回调绑定到TapGesture上，触发手势后，通过回调函数处理手势事件
44. gestureApi->setGestureEventTarget(TapGesture,
45. GESTURE_EVENT_ACTION_ACCEPT | GESTURE_EVENT_ACTION_UPDATE |
46. GESTURE_EVENT_ACTION_END | GESTURE_EVENT_ACTION_CANCEL,
47. column, onActionCallback);
48. // 将手势添加到column组件上，使column组件可以触发单指点击手势
49. gestureApi->addGestureToNode(column, TapGesture, ArkUI_GesturePriority::PARALLEL,
50. ArkUI_GestureMask::NORMAL_GESTURE_MASK);
```

[Function.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/Function.h#L318-L369)
