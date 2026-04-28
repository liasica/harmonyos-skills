---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-listen-to-component-events
title: 监听组件事件
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 添加交互事件 > 监听组件事件
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c721d6330478ea7b3282e8893f6bd2cee448e9f6a80ce822d681996ca0be0c05
---

NDK接口针对UI组件的事件，提供了监听函数的方式。首先，可使用[addNodeEventReceiver](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#addnodeeventreceiver)函数添加组件事件的监听器，该监听器会监听该组件上发生的所有事件，例如：点击事件、焦点事件。然后，可使用[registerNodeEvent](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeevent)函数声明组件的哪些事件需要监听，NDK接口支持的事件范围通过[ArkUI\_NodeEventType](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)枚举值定义。

说明

* 事件注册需要声明[addNodeEventReceiver](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#addnodeeventreceiver)监听器注册和[registerNodeEvent](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeevent)事件类型，监听器只能监听已声明的事件。
* 需要关注事件的反注册逻辑，如在组件销毁前调用[removeNodeEventReceiver](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#removenodeeventreceiver)移除事件监听器，[unregisterNodeEvent](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#unregisternodeevent)通知ArkUI框架已监听的事件不再需要监听。
* [addNodeEventReceiver](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#addnodeeventreceiver)可以添加多个函数指针，每个函数指针都会在对应事件触发时触发，对应的[removeNodeEventReceiver](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#removenodeeventreceiver)需要传递对应的函数指针用于移除监听。
* [registerNodeEventReceiver](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeeventreceiver)是全局监听函数，不同于[addNodeEventReceiver](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#addnodeeventreceiver)，[registerNodeEventReceiver](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeeventreceiver)能够监听所有Native组件的事件触发，但只能传递一个函数指针，多次调用使用最后一次的函数指针进行回调，释放时使用[unregisterNodeEventReceiver](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#unregisternodeeventreceiver)进行释放。

以下示例基于[接入ArkTS页面](ndk-access-the-arkts-page.md)章节，补充相关事件监听。详细代码请参考[完整示例](ndk-listen-to-component-events.md#完整示例)。

* 事件注册和事件解注册

  通过addNodeEventReceiver对节点绑定事件处理函数，接着通过调用registerNodeEvent注册对应的事件。

  说明

  事件监听函数的入参[ArkUI\_NodeEvent](../harmonyos-references/capi-arkui-nativemodule-arkui-nodeevent.md)\* event只在函数回调周期内生效，不推荐对该指针进行缓存或者进行异步处理。

  定义[ArkUI\_NativeNodeAPI\_1](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md)类型的指针：

  ```
  1. ArkUI_NativeNodeAPI_1 *nodeAPI = nullptr;
  ```

  [Common.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/Common.h#L47-L49)

  调用[OH\_ArkUI\_GetModuleInterface](../harmonyos-references/capi-native-interface-h.md#oh_arkui_getmoduleinterface)接口给定义的指针赋值：

  ```
  1. OH_ArkUI_GetModuleInterface(ARKUI_NATIVE_NODE, ArkUI_NativeNodeAPI_1, nodeAPI);
  ```

  [NativeEntry.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/NativeEntry.cpp#L70-L72)

  定义事件触发回调函数：

  ```
  1. void NodeEventReceiver(ArkUI_NodeEvent *event) {
  2. // 设置对应的事件类型触发时进行的操作，如NODE_ON_CLICK_EVENT
  3. };
  ```

  [Function.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/Function.h#L88-L92)

  创建一个节点，将事件触发回调函数绑定到该节点并进行事件注册：

  ```
  1. auto button = nodeAPI->createNode(ARKUI_NODE_BUTTON);
  2. nodeAPI->addNodeEventReceiver(button, NodeEventReceiver);
  3. nodeAPI->registerNodeEvent(button, NODE_ON_CLICK_EVENT, 0, nullptr);
  ```

  [Function.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/Function.h#L99-L103)

  详细的事件类型请参考[ArkUI\_NodeEventType](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)。

  通过unregisterNodeEvent解注册对应的事件类型，再通过removeNodeEventReceiver卸载事件处理函数。

  解注册对应的事件类型：

  ```
  1. nodeAPI->unregisterNodeEvent(button, NODE_ON_CLICK_EVENT);
  ```

  [Function.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/Function.h#L213-L215)

  卸载事件处理函数：

  ```
  1. nodeAPI->removeNodeEventReceiver(button, NodeEventReceiver);
  ```
* 全局事件监听

  使用registerNodeEventReceiver注册全局的事件处理函数，对事件进行统一的处理，结束后可使用unregisterNodeEventReceiver进行释放。

  注册全局的事件处理函数：

  ```
  1. nodeAPI->registerNodeEventReceiver([](ArkUI_NodeEvent *event) {
  2. // 从组件事件中获取基础事件对象
  3. auto *inputEvent = OH_ArkUI_NodeEvent_GetInputEvent(event);
  4. // 从组件事件获取事件类型
  5. auto eventType = OH_ArkUI_NodeEvent_GetEventType(event);
  6. // ···
  7. switch (eventType) {
  8. case NODE_ON_CLICK_EVENT: {
  9. // 触发点击事件所进行的操作，从基础事件获取事件信息
  10. // ···
  11. }
  12. default: {
  13. break;
  14. }
  15. }
  16. });
  ```

  [Function.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/Function.h#L113-L181)

  解注册全局的事件处理函数：

  ```
  1. nodeAPI->unregisterNodeEventReceiver();
  ```
* 获取事件信息

  ArkUI框架提供了[OH\_ArkUI\_NodeEvent\_GetInputEvent()](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeevent_getinputevent)接口，用于从输入交互相关的组件事件（如NODE\_ON\_CLICK\_EVENT、NODE\_TOUCH\_EVENT等，具体可参见每个枚举定义的说明）中获取基础事件对象。然后，可通过调用[OH\_ArkUI\_PointerEvent\_GetDisplayX()](../harmonyos-references/capi-ui-input-event-h.md#oh_arkui_pointerevent_getdisplayx)、[OH\_ArkUI\_PointerEvent\_GetDisplayXByIndex()](../harmonyos-references/capi-ui-input-event-h.md#oh_arkui_pointerevent_getdisplayxbyindex)、[OH\_ArkUI\_UIInputEvent\_GetAction()](../harmonyos-references/capi-ui-input-event-h.md#oh_arkui_uiinputevent_getaction)和[OH\_ArkUI\_UIInputEvent\_GetEventTime()](../harmonyos-references/capi-ui-input-event-h.md#oh_arkui_uiinputevent_geteventtime)等接口，从基础事件中获取更多信息。应用根据获取的事件信息，在事件执行过程中实现差异化交互逻辑。

  注册事件监听回调：

  ```
  1. // 注册click事件
  2. nodeAPI->registerNodeEvent(button, NODE_ON_CLICK_EVENT, 0, nullptr);
  3. // 设置组件事件的全局监听
  4. nodeAPI->registerNodeEventReceiver([](ArkUI_NodeEvent *event) {
  5. // 从组件事件中获取基础事件对象
  6. auto *inputEvent = OH_ArkUI_NodeEvent_GetInputEvent(event);
  7. // 从组件事件获取事件类型
  8. auto eventType = OH_ArkUI_NodeEvent_GetEventType(event);
  9. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
  10. "NdkAddInteractionEvent_eventInfo inputEvent = %{public}p", inputEvent);
  11. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
  12. "NdkAddInteractionEvent_eventInfo eventType = %{public}d", eventType);
  13. auto componentEvent = OH_ArkUI_NodeEvent_GetNodeComponentEvent(event);
  14. // 获取组件事件中的数字类型数据
  15. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
  16. "NdkAddInteractionEvent_eventInfo componentEvent = %{public}p", componentEvent);
  17. // 获取触发该事件的组件对象
  18. auto nodeHandle = OH_ArkUI_NodeEvent_GetNodeHandle(event);
  19. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
  20. "NdkAddInteractionEvent_eventInfo nodeHandle = %{public}p", nodeHandle);
  21. // 根据eventType来区分事件类型，进行差异化处理，其他获取事件信息的接口也可类似方式来进行差异化的处理
  22. switch (eventType) {
  23. case NODE_ON_CLICK_EVENT: {
  24. // 触发点击事件所进行的操作，从基础事件获取事件信息
  25. auto x = OH_ArkUI_PointerEvent_GetX(inputEvent);
  26. auto y = OH_ArkUI_PointerEvent_GetY(inputEvent);
  27. auto displayX = OH_ArkUI_PointerEvent_GetDisplayX(inputEvent);
  28. auto displayY = OH_ArkUI_PointerEvent_GetDisplayY(inputEvent);
  29. auto windowX = OH_ArkUI_PointerEvent_GetWindowX(inputEvent);
  30. auto windowY = OH_ArkUI_PointerEvent_GetWindowY(inputEvent);
  31. auto pointerCount = OH_ArkUI_PointerEvent_GetPointerCount(inputEvent);
  32. auto xByIndex = OH_ArkUI_PointerEvent_GetXByIndex(inputEvent, 0);
  33. auto yByIndex = OH_ArkUI_PointerEvent_GetYByIndex(inputEvent, 0);
  34. auto displayXByIndex = OH_ArkUI_PointerEvent_GetDisplayXByIndex(inputEvent, 0);
  35. auto displayYByIndex = OH_ArkUI_PointerEvent_GetDisplayYByIndex(inputEvent, 0);
  36. auto windowXByIndex = OH_ArkUI_PointerEvent_GetWindowXByIndex(inputEvent, 0);
  37. auto windowYByIndex = OH_ArkUI_PointerEvent_GetWindowYByIndex(inputEvent, 0);
  38. auto pointerId = OH_ArkUI_PointerEvent_GetPointerId(inputEvent, 0);
  39. auto pressure = OH_ArkUI_PointerEvent_GetPressure(inputEvent, 0);
  40. auto action = OH_ArkUI_UIInputEvent_GetAction(inputEvent);
  41. auto eventTime = OH_ArkUI_UIInputEvent_GetEventTime(inputEvent);
  42. auto sourceType = OH_ArkUI_UIInputEvent_GetSourceType(inputEvent);
  43. auto type = OH_ArkUI_UIInputEvent_GetType(inputEvent);
  44. std::string eventInfo =
  45. "x: " + std::to_string(x) + ", y: " + std::to_string(y) +
  46. ", displayX: " + std::to_string(displayX) + ", displayY: " + std::to_string(displayY) +
  47. ", windowX: " + std::to_string(windowX) + ", windowY: " + std::to_string(windowY) +
  48. ", pointerCount: " + std::to_string(pointerCount) + ", xByIndex: " + std::to_string(xByIndex) +
  49. ", yByIndex: " + std::to_string(yByIndex) +
  50. ", displayXByIndex: " + std::to_string(displayXByIndex) +
  51. ", displayYByIndex: " + std::to_string(displayYByIndex) +
  52. ", windowXByIndex: " + std::to_string(windowXByIndex) +
  53. ", windowYByIndex: " + std::to_string(windowYByIndex) +
  54. ", pointerId: " + std::to_string(pointerId) + ", pressure: " + std::to_string(pressure) +
  55. ", action: " + std::to_string(action) + ", eventTime: " + std::to_string(eventTime) +
  56. ", sourceType: " + std::to_string(sourceType) + ", type: " + std::to_string(type);
  57. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
  58. "NdkAddInteractionEvent_eventInfoOfCommonEvent eventInfo = %{public}s",
  59. eventInfo.c_str());
  60. break;
  61. }
  62. default: {
  63. break;
  64. }
  65. }
  66. });
  ```

  [Function.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/Function.h#L109-L182)

  解注册事件处理函数：

  ```
  1. nodeAPI->unregisterNodeEventReceiver();
  ```

  [Function.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/Function.h#L210-L212)

  解注册对应的事件类型：

  ```
  1. nodeAPI->unregisterNodeEvent(button, NODE_ON_CLICK_EVENT);
  ```

  [Function.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/Function.h#L213-L215)
* 深浅色变更事件

  ArkUI开发框架在NDK接口提供了以组件为注册单位的系统深浅色变更事件，系统通过在深浅色变更时通知注册在组件上的回调，实现NDK侧的深浅色变更能力。

  说明

  + 一个回调内可以自行设计多个组件的深浅色变更。
  + 同一组件仅能注册一个系统深浅变更回调。
  + 建议注册在页面内不会被销毁的节点，防止因节点销毁导致的回调失效。

  ```
  1. struct ColorModeInfo {
  2. const char* lightMsg;
  3. const char* darkMsg;
  4. };

  6. // 注册回调函数
  7. void onColorModeChange(ArkUI_SystemColorMode colorMode, void *userData)
  8. {
  9. ColorModeInfo* info = static_cast<ColorModeInfo*>(userData);
  10. if (colorMode == ARKUI_SYSTEM_COLOR_MODE_LIGHT) {
  11. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
  12. "NdkAddInteractionEvent_Light mode: ", info->lightMsg);
  13. } else if (colorMode == ARKUI_SYSTEM_COLOR_MODE_DARK) {
  14. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
  15. "NdkAddInteractionEvent_Dark mode: ", info->darkMsg);
  16. }
  17. }

  19. ArkUI_NodeHandle testColorModeChange(ArkUI_NativeNodeAPI_1 *nodeAPI) {
  20. ArkUI_NodeHandle text = nodeAPI->createNode(ARKUI_NODE_TEXT);
  21. static ColorModeInfo info = {"Light mode", "Dark mode"};
  22. OH_ArkUI_RegisterSystemColorModeChangeEvent(text, &info, onColorModeChange);

  24. ArkUI_AttributeItem itemstring = {nullptr, 0, ("test_light_dark")};
  25. nodeAPI->setAttribute(text, NODE_TEXT_CONTENT, &itemstring);

  27. return text;
  28. }
  ```

  [Function.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/Function.h#L58-L87)

## 完整示例

1. 在ArkUINode基类对象中实现通用事件注册逻辑。

   ```
   1. // ArkUINode.h
   2. // 提供通用属性和事件的封装。

   4. #ifndef MYAPPLICATION_ARKUINODE_H
   5. #define MYAPPLICATION_ARKUINODE_H

   7. #include "ArkUIBaseNode.h"
   8. #include "NativeModule.h"

   10. #include <arkui/native_node.h>
   11. #include <arkui/native_type.h>

   13. namespace NativeModule {

   15. class ArkUINode : public ArkUIBaseNode {
   16. public:
   17. explicit ArkUINode(ArkUI_NodeHandle handle) : ArkUIBaseNode(handle)
   18. {
   19. nativeModule_ = NativeModuleInstance::GetInstance()->GetNativeNodeAPI();
   20. // 事件触发时需要通过函数获取对应的事件对象，这边通过设置节点自定义数据将封装类指针保持在组件上，方便后续事件分发。
   21. nativeModule_->setUserData(handle_, this);
   22. // 注册节点监听事件接受器。
   23. nativeModule_->addNodeEventReceiver(handle_, ArkUINode::NodeEventReceiver);
   24. }

   26. ~ArkUINode() override
   27. {
   28. if (onClick_) {
   29. nativeModule_->unregisterNodeEvent(handle_, NODE_ON_CLICK_EVENT);
   30. }
   31. if (onTouch_) {
   32. nativeModule_->unregisterNodeEvent(handle_, NODE_TOUCH_EVENT);
   33. }
   34. if (onDisappear_) {
   35. nativeModule_->unregisterNodeEvent(handle_, NODE_EVENT_ON_DISAPPEAR);
   36. }
   37. if (onAppear_) {
   38. nativeModule_->unregisterNodeEvent(handle_, NODE_EVENT_ON_APPEAR);
   39. }
   40. nativeModule_->removeNodeEventReceiver(handle_, ArkUINode::NodeEventReceiver);
   41. }
   42. // 设置节点宽度
   43. void SetWidth(float width)
   44. {
   45. if (!handle_) {
   46. return;
   47. }
   48. ArkUI_NumberValue value[] = {{.f32 = width}};
   49. ArkUI_AttributeItem item = {value, 1};
   50. nativeModule_->setAttribute(handle_, NODE_WIDTH, &item);
   51. }
   52. // 设置节点宽度（百分比形式）
   53. void SetPercentWidth(float percent)
   54. {
   55. if (!handle_) {
   56. return;
   57. }
   58. ArkUI_NumberValue value[] = {{.f32 = percent}};
   59. ArkUI_AttributeItem item = {value, 1};
   60. nativeModule_->setAttribute(handle_, NODE_WIDTH_PERCENT, &item);
   61. }
   62. // 设置节点高度
   63. void SetHeight(float height)
   64. {
   65. if (!handle_) {
   66. return;
   67. }
   68. ArkUI_NumberValue value[] = {{.f32 = height}};
   69. ArkUI_AttributeItem item = {value, 1};
   70. nativeModule_->setAttribute(handle_, NODE_HEIGHT, &item);
   71. }
   72. // 设置节点高度（百分比形式）
   73. void SetPercentHeight(float percent)
   74. {
   75. if (!handle_) {
   76. return;
   77. }
   78. ArkUI_NumberValue value[] = {{.f32 = percent}};
   79. ArkUI_AttributeItem item = {value, 1};
   80. nativeModule_->setAttribute(handle_, NODE_HEIGHT_PERCENT, &item);
   81. }
   82. // 设置节点背景颜色
   83. void SetBackgroundColor(uint32_t color)
   84. {
   85. if (!handle_) {
   86. return;
   87. }
   88. ArkUI_NumberValue value[] = {{.u32 = color}};
   89. ArkUI_AttributeItem item = {value, 1};
   90. nativeModule_->setAttribute(handle_, NODE_BACKGROUND_COLOR, &item);
   91. }
   92. // 处理通用事件。
   93. void RegisterOnClick(const std::function<void(ArkUI_NodeEvent *event)> &onClick)
   94. {
   95. if (!handle_) {
   96. return;
   97. }
   98. onClick_ = onClick;
   99. // 注册点击事件。
   100. nativeModule_->registerNodeEvent(handle_, NODE_ON_CLICK_EVENT, 0, nullptr);
   101. }

   103. void RegisterOnTouch(const std::function<void(int32_t type, float x, float y)> &onTouch)
   104. {
   105. if (!handle_) {
   106. return;
   107. }
   108. onTouch_ = onTouch;
   109. // 注册触碰事件。
   110. nativeModule_->registerNodeEvent(handle_, NODE_TOUCH_EVENT, 0, nullptr);
   111. }

   113. void RegisterOnDisappear(const std::function<void()> &onDisappear)
   114. {
   115. if (!handle_) {
   116. return;
   117. }
   118. onDisappear_ = onDisappear;
   119. // 注册卸载事件。
   120. nativeModule_->registerNodeEvent(handle_, NODE_EVENT_ON_DISAPPEAR, 0, nullptr);
   121. }

   123. void RegisterOnAppear(const std::function<void()> &onAppear)
   124. {
   125. if (!handle_) {
   126. return;
   127. }
   128. onAppear_ = onAppear;
   129. // 注册挂载事件。
   130. nativeModule_->registerNodeEvent(handle_, NODE_EVENT_ON_APPEAR, 0, nullptr);
   131. }

   133. protected:
   134. // 事件监听器函数指针。
   135. static void NodeEventReceiver(ArkUI_NodeEvent *event)
   136. {
   137. // 获取事件发生的UI组件对象。
   138. auto nodeHandle = OH_ArkUI_NodeEvent_GetNodeHandle(event);
   139. // 获取保持在UI组件对象中的自定义数据，返回封装类指针。
   140. auto *node = reinterpret_cast<ArkUINode *>(
   141. NativeModuleInstance::GetInstance()->GetNativeNodeAPI()->getUserData(nodeHandle));
   142. // 基于封装类实例对象处理事件。
   143. node->ProcessNodeEvent(event);
   144. }
   145. void ProcessNodeEvent(ArkUI_NodeEvent *event)
   146. {
   147. auto eventType = OH_ArkUI_NodeEvent_GetEventType(event);
   148. switch (eventType) {
   149. case NODE_ON_CLICK_EVENT: {
   150. if (onClick_) {
   151. onClick_(event);
   152. }
   153. break;
   154. }
   155. case NODE_TOUCH_EVENT: {
   156. if (onTouch_) {
   157. auto *uiInputEvent = OH_ArkUI_NodeEvent_GetInputEvent(event);
   158. float x = OH_ArkUI_PointerEvent_GetX(uiInputEvent);
   159. float y = OH_ArkUI_PointerEvent_GetY(uiInputEvent);
   160. auto type = OH_ArkUI_UIInputEvent_GetAction(uiInputEvent);
   161. onTouch_(type, x, y);
   162. }
   163. }
   164. case NODE_EVENT_ON_DISAPPEAR: {
   165. if (onDisappear_) {
   166. onDisappear_();
   167. }
   168. break;
   169. }
   170. case NODE_EVENT_ON_APPEAR: {
   171. if (onAppear_) {
   172. onAppear_();
   173. }
   174. break;
   175. }
   176. default: {
   177. // 组件特有事件交给子类处理
   178. OnNodeEvent(event);
   179. }
   180. }
   181. }

   183. virtual void OnNodeEvent(ArkUI_NodeEvent *event) {}

   185. void OnAddChild(const std::shared_ptr<ArkUIBaseNode> &child) override
   186. {
   187. nativeModule_->addChild(handle_, child->GetHandle());
   188. }

   190. void OnRemoveChild(const std::shared_ptr<ArkUIBaseNode> &child) override
   191. {
   192. nativeModule_->removeChild(handle_, child->GetHandle());
   193. }

   195. void OnInsertChild(const std::shared_ptr<ArkUIBaseNode> &child, int32_t index) override
   196. {
   197. nativeModule_->insertChildAt(handle_, child->GetHandle(), index);
   198. }

   200. private:
   201. std::function<void(ArkUI_NodeEvent *event)> onClick_;
   202. std::function<void()> onDisappear_;
   203. std::function<void()> onAppear_;
   204. std::function<void(int32_t type, float x, float y)> onTouch_;
   205. };
   206. } // namespace NativeModule

   208. #endif // MYAPPLICATION_ARKUINODE_H
   ```

   [ArkUINode.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/ArkUINode.h#L16-L225)
2. 在ArkUIListNode对象中实现列表事件注册逻辑。

   ```
   1. // ArkUIListNode.h
   2. // 列表封装类对象

   4. #ifndef MYAPPLICATION_ARKUILISTNODE_H
   5. #define MYAPPLICATION_ARKUILISTNODE_H

   7. #include "ArkUINode.h"

   9. namespace NativeModule {
   10. class ArkUIListNode : public ArkUINode {
   11. public:
   12. ArkUIListNode()
   13. : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI_NODE_LIST)) {}

   15. ~ArkUIListNode() override { nativeModule_->unregisterNodeEvent(handle_, NODE_LIST_ON_SCROLL_INDEX); }

   17. void SetScrollBarState(bool isShow)
   18. {
   19. if (!handle_) {
   20. return;
   21. }
   22. ArkUI_ScrollBarDisplayMode displayMode =
   23. isShow ? ARKUI_SCROLL_BAR_DISPLAY_MODE_ON : ARKUI_SCROLL_BAR_DISPLAY_MODE_OFF;
   24. ArkUI_NumberValue value[] = {{.i32 = displayMode}};
   25. ArkUI_AttributeItem item = {value, 1};
   26. nativeModule_->setAttribute(handle_, NODE_SCROLL_BAR_DISPLAY_MODE, &item);
   27. }

   29. // 注册列表相关事件。
   30. void RegisterOnScrollIndex(const std::function<void(int32_t index)> &onScrollIndex)
   31. {
   32. if (!handle_) {
   33. return;
   34. }
   35. onScrollIndex_ = onScrollIndex;
   36. nativeModule_->registerNodeEvent(handle_, NODE_LIST_ON_SCROLL_INDEX, 0, nullptr);
   37. }

   39. protected:
   40. // 处理List相关事件。
   41. void OnNodeEvent(ArkUI_NodeEvent *event) override
   42. {
   43. auto eventType = OH_ArkUI_NodeEvent_GetEventType(event);
   44. switch (eventType) {
   45. case NODE_LIST_ON_SCROLL_INDEX: {
   46. auto index = OH_ArkUI_NodeEvent_GetNodeComponentEvent(event)->data[0];
   47. if (onScrollIndex_) {
   48. onScrollIndex_(index.i32);
   49. }
   50. }
   51. default: {
   52. }
   53. }
   54. }

   56. private:
   57. std::function<void(int32_t index)> onScrollIndex_;
   58. };
   59. } // namespace NativeModule

   61. #endif // MYAPPLICATION_ARKUILISTNODE_H
   ```

   [ArkUIListNode.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/ArkUIListNode.h#L16-L78)
3. 添加相关事件。

   ```
   1. // NormalTextListExample.h
   2. // 文本列表示例。

   4. #ifndef MYAPPLICATION_NORMALTEXTLISTEXAMPLE_H
   5. #define MYAPPLICATION_NORMALTEXTLISTEXAMPLE_H

   7. #include "ArkUIBaseNode.h"
   8. #include "ArkUIListItemNode.h"
   9. #include "ArkUIListNode.h"
   10. #include "ArkUITextNode.h"
   11. #include <hilog/log.h>

   13. const unsigned int LOG_PRINT_DOMAIN = 0xF811;
   14. const unsigned int LOOP_SIZE = 30;
   15. const unsigned int FONT_SIZE = 16;
   16. const unsigned int HEIGHT_SIZE = 200;
   17. const float PERCENT_WIDTH_1 = 1;
   18. const float PERCENT_HEIGHT_1 = 1;

   20. namespace NativeModule {

   22. std::shared_ptr<ArkUIBaseNode> CreateTextListExample()
   23. {
   24. // 创建组件并挂载
   25. // 1：创建List组件。
   26. auto list = std::make_shared<ArkUIListNode>();
   27. list->SetPercentWidth(PERCENT_WIDTH_1);
   28. list->SetPercentHeight(PERCENT_HEIGHT_1);
   29. // 2：创建ListItem子组件并挂载到List上。
   30. for (int32_t i = 0; i < LOOP_SIZE; ++i) {
   31. auto listItem = std::make_shared<ArkUIListItemNode>();
   32. auto textNode = std::make_shared<ArkUITextNode>();
   33. textNode->SetTextContent(std::to_string(i));
   34. textNode->SetFontSize(FONT_SIZE);
   35. textNode->SetPercentWidth(PERCENT_WIDTH_1);
   36. textNode->SetHeight(HEIGHT_SIZE);
   37. textNode->SetBackgroundColor(0xFFfffacd);
   38. textNode->SetTextAlign(ARKUI_TEXT_ALIGNMENT_CENTER);
   39. listItem->AddChild(textNode);
   40. // 列表项注册点击事件。
   41. auto onClick = [](ArkUI_NodeEvent *event) {
   42. // 从组件事件中获取基础事件对象
   43. auto *inputEvent = OH_ArkUI_NodeEvent_GetInputEvent(event);
   44. if (inputEvent == nullptr) {
   45. return;
   46. }
   47. // 从组件事件获取事件类型
   48. auto eventType = OH_ArkUI_NodeEvent_GetEventType(event);
   49. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
   50. "NdkAddInteractionEvent_eventInfo inputEvent = %{public}p", inputEvent);
   51. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
   52. "NdkAddInteractionEvent_eventInfo eventType = %{public}d", eventType);
   53. auto componentEvent = OH_ArkUI_NodeEvent_GetNodeComponentEvent(event);
   54. // 获取组件事件中的数字类型数据
   55. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
   56. "NdkAddInteractionEvent_eventInfo componentEvent = %{public}p", componentEvent);
   57. // 获取触发该事件的组件对象
   58. auto nodeHandle = OH_ArkUI_NodeEvent_GetNodeHandle(event);
   59. if (nodeHandle == nullptr) {
   60. return;
   61. }
   62. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
   63. "NdkAddInteractionEvent_eventInfo nodeHandle = %{public}p", nodeHandle);
   64. // 根据eventType来区分事件类型，进行差异化处理，其他获取事件信息的接口也可类似方式来进行差异化的处理
   65. switch (eventType) {
   66. case NODE_ON_CLICK_EVENT: {
   67. // 触发点击事件所进行的操作，从基础事件获取事件信息
   68. auto x = OH_ArkUI_PointerEvent_GetX(inputEvent);
   69. auto y = OH_ArkUI_PointerEvent_GetY(inputEvent);
   70. auto displayX = OH_ArkUI_PointerEvent_GetDisplayX(inputEvent);
   71. auto displayY = OH_ArkUI_PointerEvent_GetDisplayY(inputEvent);
   72. auto windowX = OH_ArkUI_PointerEvent_GetWindowX(inputEvent);
   73. auto windowY = OH_ArkUI_PointerEvent_GetWindowY(inputEvent);
   74. auto pointerCount = OH_ArkUI_PointerEvent_GetPointerCount(inputEvent);
   75. auto xByIndex = OH_ArkUI_PointerEvent_GetXByIndex(inputEvent, 0);
   76. auto yByIndex = OH_ArkUI_PointerEvent_GetYByIndex(inputEvent, 0);
   77. auto displayXByIndex = OH_ArkUI_PointerEvent_GetDisplayXByIndex(inputEvent, 0);
   78. auto displayYByIndex = OH_ArkUI_PointerEvent_GetDisplayYByIndex(inputEvent, 0);
   79. auto windowXByIndex = OH_ArkUI_PointerEvent_GetWindowXByIndex(inputEvent, 0);
   80. auto windowYByIndex = OH_ArkUI_PointerEvent_GetWindowYByIndex(inputEvent, 0);
   81. auto pointerId = OH_ArkUI_PointerEvent_GetPointerId(inputEvent, 0);
   82. auto pressure = OH_ArkUI_PointerEvent_GetPressure(inputEvent, 0);
   83. auto action = OH_ArkUI_UIInputEvent_GetAction(inputEvent);
   84. auto eventTime = OH_ArkUI_UIInputEvent_GetEventTime(inputEvent);
   85. auto sourceType = OH_ArkUI_UIInputEvent_GetSourceType(inputEvent);
   86. auto type = OH_ArkUI_UIInputEvent_GetType(inputEvent);
   87. std::string eventInfo =
   88. "x: " + std::to_string(x) + ", y: " + std::to_string(y) +
   89. ", displayX: " + std::to_string(displayX) + ", displayY: " + std::to_string(displayY) +
   90. ", windowX: " + std::to_string(windowX) + ", windowY: " + std::to_string(windowY) +
   91. ", pointerCount: " + std::to_string(pointerCount) + ", xByIndex: " + std::to_string(xByIndex) +
   92. ", yByIndex: " + std::to_string(yByIndex) +
   93. ", displayXByIndex: " + std::to_string(displayXByIndex) +
   94. ", displayYByIndex: " + std::to_string(displayYByIndex) +
   95. ", windowXByIndex: " + std::to_string(windowXByIndex) +
   96. ", windowYByIndex: " + std::to_string(windowYByIndex) +
   97. ", pointerId: " + std::to_string(pointerId) + ", pressure: " + std::to_string(pressure) +
   98. ", action: " + std::to_string(action) + ", eventTime: " + std::to_string(eventTime) +
   99. ", sourceType: " + std::to_string(sourceType) + ", type: " + std::to_string(type);
   100. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "[Sample_NdkAddInteractionEvent]",
   101. "NdkAddInteractionEvent_eventInfoOfCommonEvent eventInfo = %{public}s",
   102. eventInfo.c_str());
   103. }
   104. default: {
   105. break;
   106. }
   107. }
   108. };
   109. listItem->RegisterOnClick(onClick);
   110. list->AddChild(listItem);
   111. }
   112. // 3：注册List相关监听事件.
   113. list->RegisterOnScrollIndex([](int32_t index) { OH_LOG_INFO(LOG_APP, "on list scroll index: %{public}d", index); });
   114. // 4: 注册挂载事件。
   115. list->RegisterOnAppear([]() { OH_LOG_INFO(LOG_APP, "on list mount to tree"); });
   116. // 5: 注册卸载事件。
   117. list->RegisterOnDisappear([]() { OH_LOG_INFO(LOG_APP, "on list unmount from tree"); });
   118. return list;
   119. }
   120. } // namespace NativeModule

   122. #endif // MYAPPLICATION_NORMALTEXTLISTEXAMPLE_H
   ```

   [NormalTextListExample.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkAddInteractionEvent/entry/src/main/cpp/NormalTextListExample.h#L16-L139)

   由于使用了日志相关接口，需要在CMakeLists.txt中添加对libhilog\_ndk.z.so的引用，如下：

   ```
   1. add_library(entry SHARED napi_init.cpp NativeEntry.cpp)
   2. target_link_libraries(entry PUBLIC libace_napi.z.so libace_ndk.z.so libhilog_ndk.z.so)
   ```
