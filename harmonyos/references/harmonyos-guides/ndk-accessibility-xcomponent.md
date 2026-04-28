---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-accessibility-xcomponent
title: 通过自绘制接入无障碍
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 通过自绘制接入无障碍
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f75475f53b13fdcb6a108794ca77ee0db9f9c447f226aec5925b8866062559b7
---

通过[自定义绘制](arkts-user-defined-draw.md)接入的第三方框架平台，NDK提供了对接无障碍服务的接口函数，使三方框架组件能够支持ArkUI中的基本无障碍功能，包括焦点获取、获取无障碍节点和操作响应。

从API version 13开始，支持基于Xcomponent的自绘制方式接入。

从API version 23开始，支持基于CustomNode构建渲染节点树的自绘制方式接入。

三方框架从绘制容器组件获取到[ArkUI\_AccessibilityProvider](../harmonyos-references/pi-arkui-accessibility-arkui-accessibilityprovider.md)，通过实现其中对接无障碍的回调函数，来适配无障碍系统发出的操作[Action](../harmonyos-references/capi-native-interface-accessibility-h.md#arkui_accessibility_actiontype)，并针对组件交互行为发送无障碍事件[Event](../harmonyos-references/capi-native-interface-accessibility-h.md#arkui_accessibilityeventtype)到无障碍子系统，实现无障碍辅助应用的交互体验。

基于Xcomponent的自绘制方式接入方式通过[OH\_NativeXComponent\_GetNativeAccessibilityProvider](../harmonyos-references/capi-native-interface-xcomponent-h.md#oh_nativexcomponent_getnativeaccessibilityprovider)获得无障碍接入[ArkUI\_AccessibilityProvider](../harmonyos-references/pi-arkui-accessibility-arkui-accessibilityprovider.md)。

基于CustomNode构建渲染节点树的自绘制方式接入方式通过[OH\_ArkUI\_NativeModule\_GetNativeAccessibilityProvider](../harmonyos-references/capi-native-interface-accessibility-h.md#oh_arkui_nativemodule_getnativeaccessibilityprovider)获得无障碍接入[ArkUI\_AccessibilityProvider](../harmonyos-references/pi-arkui-accessibility-arkui-accessibilityprovider.md)。

如果需要支持单实例，通过[OH\_ArkUI\_AccessibilityProviderRegisterCallback](../harmonyos-references/capi-native-interface-accessibility-h.md#oh_arkui_accessibilityproviderregistercallback)注册接入无障碍所需的回调函数[ArkUI\_AccessibilityProviderCallbacks](../harmonyos-references/accessibility-arkui-accessibilityprovidercallbacks.md)。

如果需要支持多实例，则通过[OH\_ArkUI\_AccessibilityProviderRegisterCallbackWithInstance](../harmonyos-references/capi-native-interface-accessibility-h.md#oh_arkui_accessibilityproviderregistercallbackwithinstance)注册接入无障碍所需的回调函数[ArkUI\_AccessibilityProviderCallbacksWithInstance](../harmonyos-references/y-arkui-accessibilityprovidercallbackswithinstance.md)。

说明

* 无障碍能力：指开发者能够创建可访问的应用界面，满足视觉、听觉、运动和认知障碍等用户需求的能力。
* 实现[OH\_ArkUI\_AccessibilityProviderRegisterCallback](../harmonyos-references/capi-native-interface-accessibility-h.md#oh_arkui_accessibilityproviderregistercallback)或者[OH\_ArkUI\_AccessibilityProviderRegisterCallbackWithInstance](../harmonyos-references/capi-native-interface-accessibility-h.md#oh_arkui_accessibilityproviderregistercallbackwithinstance)回调查询接口时，查询到的每个无障碍节点信息通过[OH\_ArkUI\_AddAndGetAccessibilityElementInfo](../harmonyos-references/capi-native-interface-accessibility-h.md#oh_arkui_addandgetaccessibilityelementinfo)创建分配element内存，并将其加入到指定的elementList中。
* 使用[OH\_ArkUI\_SendAccessibilityAsyncEvent](../harmonyos-references/capi-native-interface-accessibility-h.md#oh_arkui_sendaccessibilityasyncevent)发送事件时，需要使用[OH\_ArkUI\_CreateAccessibilityEventInfo](../harmonyos-references/capi-native-interface-accessibility-h.md#oh_arkui_createaccessibilityeventinfo)创建[ArkUI\_AccessibilityEventInfo](../harmonyos-references/i-arkui-accessibility-arkui-accessibilityeventinfo.md)，使用[OH\_ArkUI\_CreateAccessibilityElementInfo](../harmonyos-references/capi-native-interface-accessibility-h.md#oh_arkui_createaccessibilityelementinfo)创建[ArkUI\_AccessibilityElementInfo](../harmonyos-references/arkui-accessibility-arkui-accessibilityelementinfo.md)，使用结束后，需要调用[OH\_ArkUI\_DestoryAccessibilityEventInfo](../harmonyos-references/capi-native-interface-accessibility-h.md#oh_arkui_destoryaccessibilityeventinfo)以及[OH\_ArkUI\_DestoryAccessibilityElementInfo](../harmonyos-references/capi-native-interface-accessibility-h.md#oh_arkui_destoryaccessibilityelementinfo)销毁函数释放内存。
* 回调函数打印日志时，携带输入的requestId，用于关联一次交互过程相关的日志，便于索引查询整个流程，协助问题定位。

## 基于Xcomponent的自绘制接入方式

以下示例提供了对接无障碍能力的实现方法，仅包含主要步骤，完整示例请参考[AccessibilityCapiSample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/AccessibilityCapi)。对接完成后，在开启无障碍功能时，可使XComponent中的三方框架绘制组件接入，实现无障碍交互。

1. 按照自定义渲染（XComponent）的[使用OH\_ArkUI\_SurfaceHolder管理Surface生命周期](napi-xcomponent-guidelines.md#管理xcomponent持有surface的生命周期)场景创建前置工程。
2. 获得无障碍接入provider并注册回调函数（以多实例场景为例）。

   ```
   1. #include <arkui/native_interface_accessibility.h>
   2. #include <string>
   3. #include "common/common.h"
   4. // 完整实现请参考AccessibilityCapiSample。
   5. #include "fakenode/fake_node.h"
   6. // 完整实现请参考AccessibilityCapiSample。
   7. #include "AccessibilityManager.h"

   9. // ...
   10. AccessibilityManager::AccessibilityManager()
   11. {
   12. // 多实例场景
   13. accessibilityProviderCallbacksWithInstance_.findAccessibilityNodeInfosById = FindAccessibilityNodeInfosById;
   14. accessibilityProviderCallbacksWithInstance_.findAccessibilityNodeInfosByText = FindAccessibilityNodeInfosByText;
   15. accessibilityProviderCallbacksWithInstance_.findFocusedAccessibilityNode = FindFocusedAccessibilityNode;
   16. accessibilityProviderCallbacksWithInstance_.findNextFocusAccessibilityNode = FindNextFocusAccessibilityNode;
   17. accessibilityProviderCallbacksWithInstance_.executeAccessibilityAction = ExecuteAccessibilityAction;
   18. accessibilityProviderCallbacksWithInstance_.clearFocusedFocusAccessibilityNode = ClearFocusedFocusAccessibilityNode;
   19. accessibilityProviderCallbacksWithInstance_.getAccessibilityNodeCursorPosition = GetAccessibilityNodeCursorPosition;
   20. // 单实例场景
   21. accessibilityProviderCallbacks_.findAccessibilityNodeInfosById = FindAccessibilityNodeInfosById;
   22. accessibilityProviderCallbacks_.findAccessibilityNodeInfosByText = FindAccessibilityNodeInfosByText;
   23. accessibilityProviderCallbacks_.findFocusedAccessibilityNode = FindFocusedAccessibilityNode;
   24. accessibilityProviderCallbacks_.findNextFocusAccessibilityNode = FindNextFocusAccessibilityNode;
   25. accessibilityProviderCallbacks_.executeAccessibilityAction = ExecuteAccessibilityAction;
   26. accessibilityProviderCallbacks_.clearFocusedFocusAccessibilityNode = ClearFocusedFocusAccessibilityNode;
   27. accessibilityProviderCallbacks_.getAccessibilityNodeCursorPosition = GetAccessibilityNodeCursorPosition;
   28. }

   30. void AccessibilityManager::Initialize(const std::string &id, OH_NativeXComponent *nativeXComponent)
   31. {
   32. int32_t ret = OH_NativeXComponent_GetNativeAccessibilityProvider(nativeXComponent, &provider);
   33. if (provider == nullptr) {
   34. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, LOG_PRINT_TEXT, "get provider is null");
   35. return;
   36. }
   37. // 2.注册回调函数
   38. ret = OH_ArkUI_AccessibilityProviderRegisterCallbackWithInstance(id.c_str(), provider,
   39. &accessibilityProviderCallbacksWithInstance_);
   40. if (ret != 0) {
   41. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, LOG_PRINT_TEXT,
   42. "InterfaceDesignTest OH_ArkUI_AccessibilityProviderRegisterCallback failed");
   43. return;
   44. }
   45. g_provider = provider;
   46. }

   48. // ...
   ```

   [AccessibilityManager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AccessibilityCapi/entry/src/main/cpp/manager/AccessibilityManager.cpp#L16-L470)
3. 三方框架需要实现如下回调函数。

* 基于指定的节点，查询所需的节点信息

  说明

  + 当无障碍系统传入的elementId为-1时，代表其约定的“根节点标识”。三方框架需将该外部标识，映射为自身内部节点树中唯一根节点的ID，以便无障碍系统正确定位到框架的根节点。
  + 三方框架需要提供一个且仅包含一个根节点。
  + 根节点的属性中的[parentId](../harmonyos-references/capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetparentid)须设置为特殊值-2100000。在无障碍树中，根节点是最顶层节点，没有父节点。这个特殊值-2100000是ArkUI无障碍框架的硬编码约定，用于明确标识 “此节点为根节点，无父节点”。使用一个特殊值而非0或-1，是为了防止与三方框架内部的有效ID产生冲突，确保系统能准确识别根节点。
  + 根节点的属性中的[enabled](../harmonyos-references/capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetenabled)须设置为true。如果设置为false，根节点被禁用，无障碍系统会认为整个控件树都不可交互，从而忽略所有子节点的查询和操作。根节点作为整个控件树的入口，必须处于可用状态，才能保证无障碍服务正常工作。
  + 根节点的属性中的[visible](../harmonyos-references/capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetvisible)须设置为true。无障碍系统只对可见的节点进行遍历和交互。如果设置为false，根节点不可见，整个控件树都会被无障碍服务忽略，导致三方框架的无障碍能力完全失效。确保用户在使用无障碍功能时，能感知到三方框架渲染的所有界面元素。

  ```
  1. int32_t AccessibilityManager::FindAccessibilityNodeInfosById(const char* instanceId, int64_t elementId,
  2. ArkUI_AccessibilitySearchMode mode, int32_t requestId, ArkUI_AccessibilityElementInfoList *elementList)
  3. {
  4. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, LOG_PRINT_TEXT,
  5. "FindAccessibilityNodeInfosById start,instanceId %{public}s elementId: %{public}ld, "
  6. "requestId: %{public}d, mode: %{public}d", instanceId,
  7. elementId, requestId, static_cast<int32_t>(mode));
  8. if (elementList == nullptr) {
  9. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, LOG_PRINT_TEXT,
  10. "FindAccessibilityNodeInfosById elementList is null");
  11. return OH_NATIVEXCOMPONENT_RESULT_FAILED;
  12. }
  13. int ret = 0;
  14. const int parentOfRoot = -2100000;
  15. if (elementId == -1) {
  16. elementId = 0;
  17. }

  19. if (mode == ARKUI_ACCESSIBILITY_NATIVE_SEARCH_MODE_PREFETCH_RECURSIVE_CHILDREN) {
  20. // 三方框架需要在该方法中实现自己的查找策略，返回无障碍节点信息给无障碍服务，以下逻辑仅为示意过程。
  21. // ArkUI框架设计的特殊值，根节点必须设置parentId为这个值。
  22. auto rootNode = OH_ArkUI_AddAndGetAccessibilityElementInfo(elementList);
  23. if (!rootNode) {
  24. return OH_NATIVEXCOMPONENT_RESULT_FAILED;
  25. }
  26. // 设置根节点信息
  27. OH_ArkUI_AccessibilityElementInfoSetElementId(rootNode, 0);
  28. OH_ArkUI_AccessibilityElementInfoSetParentId(rootNode, parentOfRoot);
  29. FakeWidget::Instance().fillAccessibilityElement(rootNode);

  31. ArkUI_AccessibleRect rect;
  32. rect.leftTopX = NUMBER_ZERO;
  33. rect.leftTopY = NUMBER_ZERO;
  34. rect.rightBottomX = NUMBER_THIRD;
  35. rect.rightBottomY = NUMBER_THIRD;
  36. ret = OH_ArkUI_AccessibilityElementInfoSetScreenRect(rootNode, &rect);
  37. // 设置根节点不可被无障碍辅助服务所识别。
  38. OH_ArkUI_AccessibilityElementInfoSetAccessibilityLevel(rootNode, "no");
  39. auto objects = FakeWidget::Instance().GetAllObjects(instanceId);
  40. int64_t childNodes[1024];
  41. for (int i = 0; i < objects.size(); i++) {
  42. int elementId = i + 1;

  44. childNodes[i] = elementId;
  45. }
  46. for (int i = 0; i < objects.size(); i++) {
  47. int elementId = i + 1;
  48. childNodes[i] = elementId;
  49. auto child = OH_ArkUI_AddAndGetAccessibilityElementInfo(elementList);
  50. // 设置子节点信息。
  51. OH_ArkUI_AccessibilityElementInfoSetElementId(child, elementId);
  52. OH_ArkUI_AccessibilityElementInfoSetParentId(child, 0);
  53. // 设置当前组件可被无障碍辅助服务所识别。
  54. OH_ArkUI_AccessibilityElementInfoSetAccessibilityLevel(child, "yes");
  55. objects[i]->fillAccessibilityElement(child);

  57. ArkUI_AccessibleRect rect;
  58. rect.leftTopX = i * NUMBER_FIRST;
  59. rect.leftTopY = NUMBER_FIRST;
  60. rect.rightBottomX = i * NUMBER_FIRST + NUMBER_FIRST;
  61. rect.rightBottomY = NUMBER_SECOND;
  62. OH_ArkUI_AccessibilityElementInfoSetScreenRect(child, &rect);
  63. if (objects[i]->ObjectType() == "FakeSlider") {
  64. auto rangeInfo = objects[i]->GetRangeInfo();
  65. OH_ArkUI_AccessibilityElementInfoSetRangeInfo(child, &rangeInfo);
  66. }
  67. if (objects[i]->ObjectType() == "FakeList") {
  68. auto gridInfo = objects[i]->GetGridInfo();
  69. OH_ArkUI_AccessibilityElementInfoSetGridInfo(child, &gridInfo);
  70. }
  71. if (objects[i]->ObjectType() == "FakeSwiper") {
  72. auto gridItemInfo = objects[i]->GetGridItemInfo();
  73. OH_ArkUI_AccessibilityElementInfoSetGridItemInfo(child, &gridItemInfo);
  74. }
  75. }

  77. ret = OH_ArkUI_AccessibilityElementInfoSetChildNodeIds(rootNode, objects.size(), childNodes);
  78. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, LOG_PRINT_TEXT,
  79. "FindAccessibilityNodeInfosById child count: %{public}ld %{public}d",
  80. objects.size(), ret);
  81. } else if (mode == ARKUI_ACCESSIBILITY_NATIVE_SEARCH_MODE_PREFETCH_CURRENT) {
  82. auto &widget = FakeWidget::Instance();
  83. AccessibleObject *obj = nullptr;
  84. if (elementId == 0) {
  85. obj = &widget;
  86. } else {
  87. obj = widget.GetChild(elementId);
  88. }
  89. if (!obj) {
  90. return OH_NATIVEXCOMPONENT_RESULT_FAILED;
  91. }
  92. auto node = OH_ArkUI_AddAndGetAccessibilityElementInfo(elementList);
  93. OH_ArkUI_AccessibilityElementInfoSetElementId(node, elementId);
  94. OH_ArkUI_AccessibilityElementInfoSetParentId(node, elementId == 0 ? parentOfRoot : 0);
  95. OH_ArkUI_AccessibilityElementInfoSetAccessibilityLevel(node, elementId == 0 ?  "no" : "yes");
  96. obj->fillAccessibilityElement(node);
  97. ArkUI_AccessibleRect rect;
  98. if (elementId == 0) {
  99. rect.leftTopX = NUMBER_ZERO;
  100. rect.leftTopY = NUMBER_ZERO;
  101. rect.rightBottomX = NUMBER_THIRD;
  102. rect.rightBottomY = NUMBER_THIRD;
  103. } else {
  104. int i = elementId - 1;
  105. rect.leftTopX = i * NUMBER_FIRST;
  106. rect.leftTopY = NUMBER_FIRST;
  107. rect.rightBottomX = i * NUMBER_FIRST + NUMBER_FIRST;
  108. rect.rightBottomY = NUMBER_SECOND;
  109. }

  111. OH_ArkUI_AccessibilityElementInfoSetScreenRect(node, &rect);
  112. if (elementId == 0) {
  113. auto objects = FakeWidget::Instance().GetAllObjects(instanceId);
  114. int64_t childNodes[1024];

  116. for (int i = 0; i < objects.size(); i++) {
  117. int elementId = i + 1;

  119. childNodes[i] = elementId;
  120. auto child = OH_ArkUI_AddAndGetAccessibilityElementInfo(elementList);
  121. OH_ArkUI_AccessibilityElementInfoSetElementId(child, elementId);
  122. OH_ArkUI_AccessibilityElementInfoSetParentId(child, 0);

  124. objects[i]->fillAccessibilityElement(child);

  126. ArkUI_AccessibleRect rect;
  127. rect.leftTopX = i * NUMBER_FIRST;
  128. rect.leftTopY = NUMBER_ZERO;
  129. rect.rightBottomX = i * NUMBER_FIRST + NUMBER_FIRST;
  130. rect.rightBottomY = NUMBER_SECOND;
  131. OH_ArkUI_AccessibilityElementInfoSetScreenRect(child, &rect);
  132. }
  133. ret = OH_ArkUI_AccessibilityElementInfoSetChildNodeIds(node, objects.size(), childNodes);
  134. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, LOG_PRINT_TEXT,
  135. "FindAccessibilityNodeInfosById child2 count: %{public}ld", objects.size());
  136. }
  137. }
  138. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, LOG_PRINT_TEXT, "FindAccessibilityNodeInfosById end");
  139. return OH_NATIVEXCOMPONENT_RESULT_SUCCESS;
  140. }
  ```

  [AccessibilityManager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AccessibilityCapi/entry/src/main/cpp/manager/AccessibilityManager.cpp#L114-L251)
* 基于指定的节点，查询下一个可聚焦的无障碍节点

  ```
  1. int32_t AccessibilityManager::FindNextFocusAccessibilityNode(const char* instanceId, int64_t elementId,
  2. ArkUI_AccessibilityFocusMoveDirection direction, int32_t requestId,
  3. ArkUI_AccessibilityElementInfo *elementInfo)
  4. {
  5. // 查找下一个可聚焦的无障碍节点，三方框架需要在该方法中实现自己的查找策略，以下逻辑仅为示意过程。
  6. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, LOG_PRINT_TEXT,
  7. "FindNextFocusAccessibilityNode instanceId %{public}s "
  8. "elementId: %{public}ld, requestId: %{public}d, direction: %{public}d",
  9. instanceId, elementId, requestId, static_cast<int32_t>(direction));
  10. auto objects = FakeWidget::Instance().GetAllObjects(instanceId);
  11. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, LOG_PRINT_TEXT, "objects.size() %{public}d", objects.size());
  12. // object.size 不包含 root节点
  13. if ((elementId < 0) || (elementId > objects.size())) {
  14. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, LOG_PRINT_TEXT, "elementId invalid");
  15. return OH_NATIVEXCOMPONENT_RESULT_FAILED;
  16. }
  17. int64_t nextElementId = -1;
  18. if (direction == ARKUI_ACCESSIBILITY_NATIVE_DIRECTION_FORWARD) {
  19. nextElementId = elementId + 1;
  20. } else {
  21. nextElementId = elementId - 1;
  22. }

  24. // 屏幕朗读约束 如果是根节点 然后backward的话需要回到最后一个节点
  25. if ((nextElementId == -1) && (direction == ARKUI_ACCESSIBILITY_NATIVE_DIRECTION_BACKWARD)) {
  26. nextElementId = objects.size();
  27. }

  29. if (nextElementId >  objects.size()) {
  30. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, LOG_PRINT_TEXT, "nextElementId invalid");
  31. return OH_NATIVEXCOMPONENT_RESULT_FAILED;
  32. }

  34. if (nextElementId <=  0) {
  35. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, LOG_PRINT_TEXT, "nextElementId less than zero");
  36. return OH_NATIVEXCOMPONENT_RESULT_FAILED;
  37. }
  38. OH_ArkUI_AccessibilityElementInfoSetElementId(elementInfo, nextElementId);
  39. OH_ArkUI_AccessibilityElementInfoSetParentId(elementInfo, 0);
  40. // id 比object索引大1
  41. objects[nextElementId - 1]->fillAccessibilityElement(elementInfo);
  42. ArkUI_AccessibleRect rect;
  43. rect.leftTopX = nextElementId * NUMBER_FIRST;
  44. rect.leftTopY = NUMBER_ZERO;
  45. rect.rightBottomX = nextElementId * NUMBER_FIRST + NUMBER_FIRST;
  46. rect.rightBottomY = NUMBER_SECOND;
  47. OH_ArkUI_AccessibilityElementInfoSetScreenRect(elementInfo, &rect);
  48. auto eventInfo = OH_ArkUI_CreateAccessibilityEventInfo();
  49. OH_ArkUI_AccessibilityEventSetRequestFocusId(eventInfo, requestId);
  50. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, LOG_PRINT_TEXT, "%{public}ld", nextElementId);
  51. return OH_NATIVEXCOMPONENT_RESULT_SUCCESS;
  52. }
  ```

  [AccessibilityManager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AccessibilityCapi/entry/src/main/cpp/manager/AccessibilityManager.cpp#L279-L331)
* 基于指定的节点，查询满足指定组件文本内容的节点信息

  ```
  1. int32_t AccessibilityManager::FindAccessibilityNodeInfosByText(const char* instanceId, int64_t elementId,
  2. const char *text, int32_t requestId, ArkUI_AccessibilityElementInfoList *elementList)
  3. {
  4. // 三方框架需实现根据文本内容查询无障碍节点的逻辑。
  5. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, LOG_PRINT_TEXT,
  6. "FindAccessibilityNodeInfosByText start,instanceId %{public}s elementId: %{public}ld, "
  7. "requestId: %{public}d, text: %{public}s.", instanceId,
  8. elementId, requestId, text);
  9. return OH_NATIVEXCOMPONENT_RESULT_SUCCESS;
  10. }
  ```

  [AccessibilityManager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AccessibilityCapi/entry/src/main/cpp/manager/AccessibilityManager.cpp#L253-L264)
* 基于指定的节点，查询已经聚焦的节点信息

  ```
  1. int32_t AccessibilityManager::FindFocusedAccessibilityNode(const char* instanceId, int64_t elementId,
  2. ArkUI_AccessibilityFocusType focusType, int32_t requestId, ArkUI_AccessibilityElementInfo *elementInfo)
  3. {
  4. // 三方框架需实现基于指定节点获取焦点元素信息的逻辑。
  5. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, LOG_PRINT_TEXT,
  6. "FindFocusedAccessibilityNode start instanceId %{public}s, "
  7. "elementId: %{public}ld, requestId: %{public}d, focusType: %{public}d",
  8. instanceId, elementId, requestId, static_cast<int32_t>(focusType));
  9. return OH_NATIVEXCOMPONENT_RESULT_SUCCESS;
  10. }
  ```

  [AccessibilityManager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AccessibilityCapi/entry/src/main/cpp/manager/AccessibilityManager.cpp#L266-L277)
* 基于指定的节点，执行指定的操作

  ```
  1. void FillEvent(ArkUI_AccessibilityEventInfo *eventInfo, ArkUI_AccessibilityElementInfo *elementInfo,
  2. ArkUI_AccessibilityEventType eventType, std::string announcedText)
  3. {
  4. if (eventInfo == nullptr) {
  5. return;
  6. }
  7. if (elementInfo == nullptr) {
  8. return;
  9. }
  10. // 设置事件类型
  11. OH_ArkUI_AccessibilityEventSetEventType(eventInfo, eventType);
  12. // 设置事件对应的元素信息
  13. OH_ArkUI_AccessibilityEventSetElementInfo(eventInfo, elementInfo);

  15. if (eventType == ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_ANNOUNCE_FOR_ACCESSIBILITY && announcedText.size() > 0) {
  16. // 给无障碍节点设置优先播报的无障碍文本
  17. OH_ArkUI_AccessibilityEventSetTextAnnouncedForAccessibility(eventInfo, announcedText.data());
  18. }
  19. }

  21. // ...

  23. void AccessibilityManager::SendAccessibilityAsyncEvent(ArkUI_AccessibilityElementInfo *elementInfo,
  24. ArkUI_AccessibilityEventType eventType,
  25. std::string announcedText)
  26. {
  27. auto eventInfo = OH_ArkUI_CreateAccessibilityEventInfo();
  28. // 1.填写event内容
  29. FillEvent(eventInfo, elementInfo, eventType, announcedText);
  30. // 2.callback
  31. auto callback = [](int32_t errorCode) {
  32. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, LOG_PRINT_TEXT, "result: %{public}d", errorCode);
  33. };
  34. // 3. 调用接口发送事件给OH侧
  35. OH_ArkUI_SendAccessibilityAsyncEvent(g_provider, eventInfo, callback);
  36. }
  37. // ...

  39. int32_t AccessibilityManager::ExecuteAccessibilityAction(const char* instanceId, int64_t elementId,
  40. ArkUI_Accessibility_ActionType action, ArkUI_AccessibilityActionArguments *actionArguments, int32_t requestId)
  41. {
  42. // 三方框架需要实现执行无障碍节点行为的逻辑。
  43. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, LOG_PRINT_TEXT,
  44. "ExecuteAccessibilityAction instanceId %{public}s elementId: %{public}ld, "
  45. "action: %{public}d, requestId: %{public}d",
  46. instanceId, elementId, action, requestId);
  47. auto object = FakeWidget::Instance().GetChild(elementId);
  48. // 传入的无障碍节点对象可能为空，需要做非空判断。
  49. if (!object) {
  50. return 0;
  51. }
  52. // 获取无障碍节点element。
  53. auto announcedText = object->GetAnnouncedForAccessibility();
  54. auto element = OH_ArkUI_CreateAccessibilityElementInfo();
  55. OH_ArkUI_AccessibilityElementInfoSetElementId(element, elementId);
  56. const char *actionKey = "some_key";
  57. char *actionValue = nullptr;
  58. OH_ArkUI_FindAccessibilityActionArgumentByKey(actionArguments, actionKey, &actionValue);
  59. // 根据action类型执行对应的行为。
  60. switch (action) {
  61. case ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_CLICK:
  62. if (object) {
  63. object->OnClick();
  64. object->fillAccessibilityElement(element);
  65. }
  66. // 向无障碍服务发送指定事件。
  67. AccessibilityManager::SendAccessibilityAsyncEvent(element,
  68. ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_CLICKED, announcedText);
  69. break;
  70. case ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_GAIN_ACCESSIBILITY_FOCUS:
  71. if (object) {
  72. object->SetFocus(true);

  74. object->fillAccessibilityElement(element);
  75. }
  76. // 向无障碍服务发送指定事件。
  77. AccessibilityManager::SendAccessibilityAsyncEvent(element,
  78. ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_ACCESSIBILITY_FOCUSED,
  79. announcedText);
  80. break;
  81. case ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_CLEAR_ACCESSIBILITY_FOCUS:
  82. if (object) {
  83. object->SetFocus(false);
  84. object->fillAccessibilityElement(element);
  85. }
  86. AccessibilityManager::SendAccessibilityAsyncEvent(
  87. element, ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_ACCESSIBILITY_FOCUS_CLEARED,
  88. announcedText);
  89. break;
  90. default:
  91. // 处理不支持的action行为。
  92. break;
  93. }
  94. OH_ArkUI_DestoryAccessibilityElementInfo(element);
  95. return OH_NATIVEXCOMPONENT_RESULT_SUCCESS;
  96. }
  ```

  [AccessibilityManager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AccessibilityCapi/entry/src/main/cpp/manager/AccessibilityManager.cpp#L36-L387)
* 清除当前获焦的节点

  ```
  1. int32_t AccessibilityManager::ClearFocusedFocusAccessibilityNode(const char* instanceId)
  2. {
  3. // 三方框架需要实现清除当前获焦的节点的行为。
  4. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, LOG_PRINT_TEXT,
  5. "ClearFocusedFocusAccessibilityNode, instanceId %{public}s", instanceId);
  6. return OH_NATIVEXCOMPONENT_RESULT_SUCCESS;
  7. }
  ```

  [AccessibilityManager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AccessibilityCapi/entry/src/main/cpp/manager/AccessibilityManager.cpp#L389-L397)
* 基于指定的节点，获取当前文本组件的光标位置

  ```
  1. int32_t AccessibilityManager::GetAccessibilityNodeCursorPosition(const char* instanceId, int64_t elementId,
  2. int32_t requestId, int32_t *index)
  3. {
  4. // 三方框架需要实现获取当前组件中（文本组件）光标位置。
  5. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, LOG_PRINT_TEXT,
  6. "GetAccessibilityNodeCursorPosition, instanceId %{public}s "
  7. "elementId: %{public}ld, requestId: %{public}d, index: %{public}d",
  8. instanceId, elementId, requestId, index);
  9. return OH_NATIVEXCOMPONENT_RESULT_SUCCESS;
  10. }
  ```

  [AccessibilityManager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AccessibilityCapi/entry/src/main/cpp/manager/AccessibilityManager.cpp#L399-L410)

1. provider通过回调函数[OH\_ArkUI\_AccessibilityProviderRegisterCallback](../harmonyos-references/capi-native-interface-accessibility-h.md#oh_arkui_accessibilityproviderregistercallback)或者[OH\_ArkUI\_AccessibilityProviderRegisterCallbackWithInstance](../harmonyos-references/capi-native-interface-accessibility-h.md#oh_arkui_accessibilityproviderregistercallbackwithinstance)对接成功后，可开启无障碍功能。

## 基于CustomNode的自绘制接入方式

说明

* 基于CustomNode的自定义绘制容器组件，仅支持类型为[ARKUI\_NODE\_CUSTOM](../harmonyos-references/capi-native-node-h.md#arkui_nodetype)且无其他子节点的[native组件](../harmonyos-references/capi-arkui-nativemodule-arkui-node8h.md)。绘制容器组件的宽和高不能为0，避免被无障碍辅助应用忽略或错误处理子节点树。

以下示例提供了对接无障碍能力的实现方法，仅包含主要步骤，完整示例请参考[AccessibilityCustomCapi](https://gitcode.com/openharmony/applications_app_samples/pull/8450)。回调函数实现请参考[基于Xcomponent的自绘制接入方式](ndk-accessibility-xcomponent.md#基于xcomponent的自绘制接入方式)。完成回调函数实现后，开启无障碍功能，基于CustomNode构建渲染节点树的三方框架即可接入无障碍服务，实现控件树的无障碍交互与信息查询。

1. 按照[基于CustomNode构建渲染节点树](ndk-embed-render-components.md)场景创建前置工程。
2. 获取无障碍接入Provider实例，将回调函数与Provider实例绑定并完成注册。

   ```
   1. int32_t AccessibilityMaker::GetAccessibilityProvider(ArkUI_NodeHandle* customNode, const char* id)
   2. {
   3. AccessibilityMaker::accessibilityProviderCallbacksWithInstance_.findAccessibilityNodeInfosById =
   4. FindAccessibilityNodeInfosById;
   5. AccessibilityMaker::accessibilityProviderCallbacksWithInstance_.findAccessibilityNodeInfosByText =
   6. FindAccessibilityNodeInfosByText;
   7. AccessibilityMaker::accessibilityProviderCallbacksWithInstance_.findFocusedAccessibilityNode =
   8. FindFocusedAccessibilityNode;
   9. AccessibilityMaker::accessibilityProviderCallbacksWithInstance_.findNextFocusAccessibilityNode =
   10. FindNextFocusAccessibilityNode;
   11. AccessibilityMaker::accessibilityProviderCallbacksWithInstance_.executeAccessibilityAction =
   12. ExecuteAccessibilityAction;
   13. AccessibilityMaker::accessibilityProviderCallbacksWithInstance_.clearFocusedFocusAccessibilityNode =
   14. ClearFocusedFocusAccessibilityNode;
   15. AccessibilityMaker::accessibilityProviderCallbacksWithInstance_.getAccessibilityNodeCursorPosition =
   16. GetAccessibilityNodeCursorPosition;

   18. // 获取 native 层提供的 accessibility provider，并为其注册回调
   19. OH_ArkUI_NativeModule_GetNativeAccessibilityProvider(customNode, &accessibilityProvider_);
   20. if (accessibilityProvider_ == nullptr) {
   21. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "AccessibilityMaker", "accessibilityProvider_ is null");
   22. return 0;
   23. }

   25. int32_t ret = OH_ArkUI_AccessibilityProviderRegisterCallbackWithInstance(id, accessibilityProvider_,
   26. &AccessibilityMaker::accessibilityProviderCallbacksWithInstance_);
   27. if (ret != 0) {
   28. return 0;
   29. }
   30. return 0;
   31. }
   ```
3. 三方框架需要实现回调函数。请参考前文的[基于Xcomponent的自绘制接入方式](ndk-accessibility-xcomponent.md#基于xcomponent的自绘制接入方式)。
