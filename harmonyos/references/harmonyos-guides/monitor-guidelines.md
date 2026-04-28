---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/monitor-guidelines
title: 事件监听开发指导（C/C++）
breadcrumb: 指南 > 系统 > 基础功能 > Input Kit（多模输入服务） > 事件监听开发指导（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4b058741e406c13d9d0f5786ddeb01f7c7e6e60c5371a0b4845066f30efea3c4
---

## 功能介绍

从API version 12开始，多模为应用提供了按键、输入事件（鼠标、触屏和轴事件）监听能力，当前仅支持录屏类应用。使用场景例如：用户在录屏应用开启录屏时，监听设备的按键、鼠标、触摸和轴事件。

## 接口说明

创建和删除事件监听相关接口如下表所示，接口详细介绍请参考[Input文档](../harmonyos-references/capi-input.md)。

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

```
1. target_link_libraries(entry PUBLIC libohinput.so)
```

### 申请所需权限

应用需要在module.json5中添加下面权限的配置，详细的配置方法参考声明[声明权限文档](declare-permissions.md)。

```
1. "requestPermissions": [
2. {
3. "name": "ohos.permission.INPUT_MONITORING"
4. }
5. ]
```

### 创建事件监听

* **按键事件**

```
1. struct KeyEvent {
2. int32_t action;
3. int32_t keyCode;
4. int64_t actionTime { -1 };
5. };

7. //定义按键事件回调函数
8. void OnKeyEventCallback(const Input_KeyEvent* keyEvent)
9. {
10. KeyEvent event;
11. //Input_KeyEvent的生命周期仅限于回调函数内，回调函数执行完毕后会被自动销毁
12. event.action = OH_Input_GetKeyEventAction(keyEvent);
13. event.keyCode = OH_Input_GetKeyEventKeyCode(keyEvent);
14. event.actionTime = OH_Input_GetKeyEventActionTime(keyEvent);
15. // ...
16. }

18. static napi_value AddKeyEventMonitor(napi_env env, napi_callback_info info)
19. {
20. Input_Result ret = OH_Input_AddKeyEventMonitor(OnKeyEventCallback);
21. // ...
22. }

24. static napi_value RemoveKeyEventMonitor(napi_env env, napi_callback_info info)
25. {
26. Input_Result ret = OH_Input_RemoveKeyEventMonitor(OnKeyEventCallback);
27. // ...
28. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputKit/NDKInputEventMonitor/entry/src/main/cpp/napi_init.cpp#L58-L114)

* **鼠标事件**

```
1. struct MouseEvent {
2. int32_t action;
3. int32_t displayX;
4. int32_t displayY;
5. int32_t button { -1 };
6. int32_t axisType { -1 };
7. float axisValue { 0.0f };
8. int64_t actionTime { -1 };
9. };

11. //定义鼠标事件回调函数
12. void OnMouseEventCallback(const Input_MouseEvent* mouseEvent)
13. {
14. MouseEvent event;
15. //Input_MouseEvent的生命周期仅限于回调函数内，回调函数执行完毕后会被自动销毁
16. event.action = OH_Input_GetMouseEventAction(mouseEvent);
17. event.displayX = OH_Input_GetMouseEventDisplayX(mouseEvent);
18. event.displayY = OH_Input_GetMouseEventDisplayY(mouseEvent);
19. event.button = OH_Input_GetMouseEventButton(mouseEvent);
20. event.axisType = OH_Input_GetMouseEventAxisType(mouseEvent);
21. event.axisValue = OH_Input_GetMouseEventAxisValue(mouseEvent);
22. event.actionTime = OH_Input_GetMouseEventActionTime(mouseEvent);
23. // ...
24. }

26. static napi_value AddMouseEventMonitor(napi_env env, napi_callback_info info)
27. {
28. Input_Result ret = OH_Input_AddMouseEventMonitor(OnMouseEventCallback);
29. // ...
30. }

32. static napi_value RemoveMouseEventMonitor(napi_env env, napi_callback_info info)
33. {
34. Input_Result ret = OH_Input_RemoveMouseEventMonitor(OnMouseEventCallback);
35. // ...
36. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputKit/NDKInputEventMonitor/entry/src/main/cpp/napi_init.cpp#L116-L184)

* **触摸事件**

```
1. struct TouchEvent {
2. int32_t action;
3. int32_t id;
4. int32_t displayX;
5. int32_t displayY;
6. int64_t actionTime { -1 };
7. };

9. void OnTouchEventCallback(const Input_TouchEvent* touchEvent)
10. {
11. TouchEvent event;
12. //Input_TouchEvent的生命周期仅限于回调函数内，回调函数执行完毕后会被自动销毁
13. event.action = OH_Input_GetTouchEventAction(touchEvent);
14. event.id = OH_Input_GetTouchEventFingerId(touchEvent);
15. event.displayX = OH_Input_GetTouchEventDisplayX(touchEvent);
16. event.displayY = OH_Input_GetTouchEventDisplayY(touchEvent);
17. event.actionTime = OH_Input_GetTouchEventActionTime(touchEvent);
18. // ...
19. }

21. static napi_value AddTouchEventMonitor(napi_env env, napi_callback_info info)
22. {
23. Input_Result ret = OH_Input_AddTouchEventMonitor(OnTouchEventCallback);
24. // ...
25. }

27. static napi_value RemoveTouchEventMonitor(napi_env env, napi_callback_info info)
28. {
29. Input_Result ret = OH_Input_RemoveTouchEventMonitor(OnTouchEventCallback);
30. // ...
31. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputKit/NDKInputEventMonitor/entry/src/main/cpp/napi_init.cpp#L186-L247)

* **轴事件**

```
1. struct AxisEvent {
2. int32_t axisAction;
3. float displayX;
4. float displayY;
5. std::map<int32_t, double> axisValues;
6. int64_t actionTime { -1 };
7. int32_t sourceType;
8. int32_t axisEventType { -1 };
9. };

11. void OnAllAxisEventCallback(const Input_AxisEvent* axisEvent)
12. {
13. AxisEvent event;
14. //Input_AxisEvent的生命周期仅限于回调函数内，回调函数执行完毕后会被自动销毁
15. InputEvent_AxisAction action = static_cast<InputEvent_AxisAction>(0);
16. Input_Result ret = OH_Input_GetAxisEventAction(axisEvent, &action);
17. event.axisAction = action;
18. ret = OH_Input_GetAxisEventDisplayX(axisEvent, &event.displayX);
19. ret = OH_Input_GetAxisEventDisplayY(axisEvent, &event.displayY);
20. ret = OH_Input_GetAxisEventActionTime(axisEvent, &event.actionTime);
21. InputEvent_SourceType sourceType = static_cast<InputEvent_SourceType>(0);
22. ret = OH_Input_GetAxisEventSourceType(axisEvent, &sourceType);
23. event.sourceType = sourceType;
24. InputEvent_AxisEventType axisEventType = static_cast<InputEvent_AxisEventType>(-1);
25. ret = OH_Input_GetAxisEventType(axisEvent, &axisEventType);
26. event.axisEventType = axisEventType;
27. if (event.axisEventType == AXIS_EVENT_TYPE_PINCH) {
28. double value = 0;
29. ret = OH_Input_GetAxisEventAxisValue(axisEvent, AXIS_TYPE_PINCH, &value);
30. event.axisValues.insert(std::make_pair(AXIS_TYPE_PINCH, value));
31. ret = OH_Input_GetAxisEventAxisValue(axisEvent, AXIS_TYPE_ROTATE, &value);
32. event.axisValues.insert(std::make_pair(AXIS_TYPE_ROTATE, value));
33. } else if (event.axisEventType == AXIS_EVENT_TYPE_SCROLL) {
34. double value = 0;
35. ret = OH_Input_GetAxisEventAxisValue(axisEvent, AXIS_TYPE_SCROLL_VERTICAL, &value);
36. event.axisValues.insert(std::make_pair(AXIS_TYPE_SCROLL_VERTICAL, value));
37. ret = OH_Input_GetAxisEventAxisValue(axisEvent, AXIS_TYPE_SCROLL_HORIZONTAL, &value);
38. event.axisValues.insert(std::make_pair(AXIS_TYPE_SCROLL_HORIZONTAL, value));
39. }
40. // ...
41. }

43. //定义捏合类型轴事件回调函数
44. void OnPinchAxisEventCallback(const Input_AxisEvent* axisEvent)
45. {
46. AxisEvent event;
47. //Input_AxisEvent的生命周期仅限于回调函数内，回调函数执行完毕后会被自动销毁
48. InputEvent_AxisAction action = static_cast<InputEvent_AxisAction>(0);
49. Input_Result ret = OH_Input_GetAxisEventAction(axisEvent, &action);
50. event.axisAction = action;
51. ret = OH_Input_GetAxisEventDisplayX(axisEvent, &event.displayX);
52. ret = OH_Input_GetAxisEventDisplayY(axisEvent, &event.displayY);
53. ret = OH_Input_GetAxisEventActionTime(axisEvent, &event.actionTime);
54. InputEvent_SourceType sourceType = static_cast<InputEvent_SourceType>(0);
55. ret = OH_Input_GetAxisEventSourceType(axisEvent, &sourceType);
56. event.sourceType = sourceType;
57. InputEvent_AxisEventType axisEventType = static_cast<InputEvent_AxisEventType>(-1);
58. ret = OH_Input_GetAxisEventType(axisEvent, &axisEventType);
59. event.axisEventType = axisEventType;
60. double value = 0;
61. ret = OH_Input_GetAxisEventAxisValue(axisEvent, AXIS_TYPE_PINCH, &value);
62. event.axisValues.insert(std::make_pair(AXIS_TYPE_PINCH, value));
63. ret = OH_Input_GetAxisEventAxisValue(axisEvent, AXIS_TYPE_ROTATE, &value);
64. event.axisValues.insert(std::make_pair(AXIS_TYPE_ROTATE, value));
65. // ...
66. }

68. void OnScrollAxisEventCallback(const Input_AxisEvent* axisEvent)
69. {
70. AxisEvent event;
71. //Input_AxisEvent的生命周期仅限于回调函数内，回调函数执行完毕后会被自动销毁
72. InputEvent_AxisAction action = static_cast<InputEvent_AxisAction>(0);
73. Input_Result ret = OH_Input_GetAxisEventAction(axisEvent, &action);
74. event.axisAction = action;
75. ret = OH_Input_GetAxisEventDisplayX(axisEvent, &event.displayX);
76. ret = OH_Input_GetAxisEventDisplayY(axisEvent, &event.displayY);
77. ret = OH_Input_GetAxisEventActionTime(axisEvent, &event.actionTime);
78. InputEvent_SourceType sourceType = static_cast<InputEvent_SourceType>(0);
79. ret = OH_Input_GetAxisEventSourceType(axisEvent, &sourceType);
80. event.sourceType = sourceType;
81. InputEvent_AxisEventType axisEventType = static_cast<InputEvent_AxisEventType>(-1);
82. ret = OH_Input_GetAxisEventType(axisEvent, &axisEventType);
83. event.axisEventType = axisEventType;
84. double value = 0;
85. ret = OH_Input_GetAxisEventAxisValue(axisEvent, AXIS_TYPE_SCROLL_VERTICAL, &value);
86. event.axisValues.insert(std::make_pair(AXIS_TYPE_SCROLL_VERTICAL, value));
87. ret = OH_Input_GetAxisEventAxisValue(axisEvent, AXIS_TYPE_SCROLL_HORIZONTAL, &value);
88. event.axisValues.insert(std::make_pair(AXIS_TYPE_SCROLL_HORIZONTAL, value));
89. // ...
90. }

92. static napi_value AddAxisEventMonitorForAll(napi_env env, napi_callback_info info)
93. {
94. Input_Result ret = OH_Input_AddAxisEventMonitorForAll(OnAllAxisEventCallback);
95. // ...
96. }

98. static napi_value RemoveAxisEventMonitorForAll(napi_env env, napi_callback_info info)
99. {
100. Input_Result ret = OH_Input_RemoveAxisEventMonitorForAll(OnAllAxisEventCallback);
101. // ...
102. }

104. static napi_value AddPinchAxisEventMonitor(napi_env env, napi_callback_info info)
105. {
106. Input_Result ret = OH_Input_AddAxisEventMonitor(AXIS_EVENT_TYPE_PINCH, OnPinchAxisEventCallback);
107. // ...
108. }

110. static napi_value RemovePinchAxisEventMonitor(napi_env env, napi_callback_info info)
111. {
112. Input_Result ret = OH_Input_RemoveAxisEventMonitor(AXIS_EVENT_TYPE_PINCH, OnPinchAxisEventCallback);
113. // ...
114. }

116. static napi_value AddScrollAxisEventMonitor(napi_env env, napi_callback_info info)
117. {
118. Input_Result ret = OH_Input_AddAxisEventMonitor(AXIS_EVENT_TYPE_SCROLL, OnScrollAxisEventCallback);
119. // ...
120. }

122. static napi_value RemoveScrollAxisEventMonitor(napi_env env, napi_callback_info info)
123. {
124. Input_Result ret =  OH_Input_RemoveAxisEventMonitor(AXIS_EVENT_TYPE_SCROLL, OnScrollAxisEventCallback);
125. // ...
126. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputKit/NDKInputEventMonitor/entry/src/main/cpp/napi_init.cpp#L249-L478)
