---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-drag-event
title: 拖拽事件
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 添加交互事件 > 拖拽事件
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5d8d82f747684d8c130a3aab931c31fa988fc51e99c82ea453e29ef004a212f6
---

ArkUI开发框架针对拖拽事件提供了[NODE\_ON\_PRE\_DRAG](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)，[NODE\_ON\_DRAG\_START](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)，[NODE\_ON\_DROP](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)，[NODE\_ON\_DRAG\_ENTER](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)，[NODE\_ON\_DRAG\_MOVE](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)，[NODE\_ON\_DRAG\_LEAVE](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)，[NODE\_ON\_DRAG\_END](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)等组件事件，当拖拽在不同的阶段时会触发对应的组件事件，完成对应的数据处理操作，实现期望的拖拽交互能力。

## 通用拖拽

ArkUI提供了使用C和C++开发拖拽功能的能力，开发者可调用C API实现拖拽功能。以下以Image组件为例，详细介绍C API实现拖拽功能的基本步骤，以及在开发过程中需要注意的事项。完整示例请参考[NativeDragDrop](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeDragDrop)。

1. 组件拖拽设置。

   通过[OH\_ArkUI\_GetModuleInterface](../harmonyos-references/capi-native-interface-h.md#oh_arkui_getmoduleinterface)接口初始化nodeAPI，创建节点等操作均需通过nodeAPI完成。

   ```
   1. ArkUI_NativeNodeAPI_1 *nativeNodeAPI = nullptr;
   2. OH_ArkUI_GetModuleInterface(ARKUI_NATIVE_NODE, ArkUI_NativeNodeAPI_1, nativeNodeAPI);
   3. nodeAPI = nativeNodeAPI;
   ```

   [manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDragDrop/entry/src/main/cpp/manager.cpp#L147-L151)

   创建Image节点，通过[OH\_ArkUI\_SetNodeDraggable](../harmonyos-references/capi-drag-and-drop-h.md#oh_arkui_setnodedraggable)设置节点可拖拽，并设置其他相关属性。

   ```
   1. dragImage2 = nodeAPI->createNode(ARKUI_NODE_IMAGE);
   2. SetId(dragImage2, "dragImage");
   3. SetCommonAttribute(dragImage2, 140.0f, 140.0f, 0xFFFFFFFF, 5.0f);
   4. // 图片src/main/resources/base/media/seagull.png需要替换为开发者所需的资源文件
   5. SetImageSrc(dragImage2, "/resources/base/media/seagull.png");
   6. OH_ArkUI_SetNodeDraggable(dragImage2, true);
   7. nodeAPI->registerNodeEvent(dragImage2, NODE_ON_DRAG_START, 1, nullptr);
   ```

   [thirdmodule.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDragDrop/entry/src/main/cpp/thirdmodule.h#L179-L187)

   ```
   1. #define DEFAULT_WIDTH 200.0
   2. // 设置节点宽度
   3. void SetWidth(ArkUI_NodeHandle &node, float width = DEFAULT_WIDTH)
   4. {
   5. if (!nodeAPI) {
   6. return;
   7. }
   8. ArkUI_NumberValue widthValue[] = {width};
   9. ArkUI_AttributeItem widthItem = {widthValue, 1};
   10. nodeAPI->setAttribute(node, NODE_WIDTH, &widthItem);
   11. }

   13. #define DEFAULT_HEIGHT 200.0
   14. // 设置节点高度
   15. void SetHeight(ArkUI_NodeHandle &node, float height = DEFAULT_HEIGHT)
   16. {
   17. if (!nodeAPI) {
   18. return;
   19. }
   20. ArkUI_NumberValue heightValue[] = {height};
   21. ArkUI_AttributeItem heightItem = {heightValue, 1};
   22. nodeAPI->setAttribute(node, NODE_HEIGHT, &heightItem);
   23. }

   25. #define DEFAULT_BG_COLOR 0xFFFFFFFF
   26. // 设置节点背景颜色
   27. void SetBackgroundColor(ArkUI_NodeHandle &node, uint32_t color = DEFAULT_BG_COLOR)
   28. {
   29. if (!nodeAPI) {
   30. return;
   31. }
   32. ArkUI_NumberValue colorValue[] = {{.u32 = color}};
   33. ArkUI_AttributeItem colorItem = {colorValue, 1};
   34. nodeAPI->setAttribute(node, NODE_BACKGROUND_COLOR, &colorItem);
   35. }

   37. #define DEFAULT_MARGIN 5.0
   38. // 设置节点外边距
   39. void SetMargin(ArkUI_NodeHandle &node, float margin = DEFAULT_MARGIN)
   40. {
   41. if (!nodeAPI) {
   42. return;
   43. }
   44. ArkUI_NumberValue marginValue[] = {margin};
   45. ArkUI_AttributeItem marginItem = {marginValue, 1};
   46. nodeAPI->setAttribute(node, NODE_MARGIN, &marginItem);
   47. }

   49. // 设置Button节点标签
   50. void SetButtonLabel(ArkUI_NodeHandle &node, const char *label)
   51. {
   52. if (!nodeAPI) {
   53. return;
   54. }
   55. ArkUI_AttributeItem NODE_Button_SRC_Item = {.string = label};
   56. nodeAPI->setAttribute(node, NODE_BUTTON_LABEL, &NODE_Button_SRC_Item);
   57. }

   59. // 设置节点标识符
   60. void SetId(ArkUI_NodeHandle &node, const char *id)
   61. {
   62. if (!nodeAPI) {
   63. return;
   64. }
   65. ArkUI_AttributeItem idItem = {.string = id};
   66. nodeAPI->setAttribute(node, NODE_ID, &idItem);
   67. }

   69. #define DEFAULT_BORDER_WIDTH 0.0
   70. // 设置节点边框宽度
   71. void SetBorderWidth(ArkUI_NodeHandle &node, float width = DEFAULT_BORDER_WIDTH)
   72. {
   73. if (!nodeAPI) {
   74. return;
   75. }
   76. ArkUI_NumberValue borderWidthValue[] = {width};
   77. ArkUI_AttributeItem borderWidthItem = {borderWidthValue, 1};
   78. nodeAPI->setAttribute(node, NODE_BORDER_WIDTH, &borderWidthItem);
   79. }

   81. #define DEFAULT_BORDER_COLOR 0xFF000000
   82. // 设置节点边框颜色
   83. void SetBorderColor(ArkUI_NodeHandle &node, uint32_t color = DEFAULT_BORDER_COLOR)
   84. {
   85. if (!nodeAPI) {
   86. return;
   87. }
   88. ArkUI_NumberValue borderColorValue[] = {{.u32 = color}};
   89. ArkUI_AttributeItem borderColorItem = {borderColorValue, 1};
   90. nodeAPI->setAttribute(node, NODE_BORDER_COLOR, &borderColorItem);
   91. }

   93. // 设置节点常用属性（宽高、背景色、外边距、边框样式）
   94. void SetCommonAttribute(ArkUI_NodeHandle &node, float width = DEFAULT_WIDTH, float height = DEFAULT_HEIGHT,
   95. unsigned int color = DEFAULT_BG_COLOR, float margin = DEFAULT_MARGIN)
   96. {
   97. SetWidth(node, width);
   98. SetHeight(node, height);
   99. SetBackgroundColor(node, color);
   100. SetMargin(node, margin);
   101. SetBorderWidth(node, DEFAULT_BORDER_WIDTH);
   102. SetBorderColor(node);
   103. }
   ```

   [common.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDragDrop/entry/src/main/cpp/common.h#L91-L195)

   ```
   1. void SetImageSrc(ArkUI_NodeHandle &node, const char *src)
   2. {
   3. if (!nodeAPI) {
   4. return;
   5. }
   6. ArkUI_AttributeItem imageSrcItem = {.string = src};
   7. nodeAPI->setAttribute(node, NODE_IMAGE_SRC, &imageSrcItem);
   8. }
   ```

   [common.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDragDrop/entry/src/main/cpp/common.h#L233-L242)
2. 自定义拖拽预览和背板图。

   创建[pixelMap](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmapnative_createpixelmap)，设置pixelMap的宽高等各项属性。设置Image节点的[ArkUI\_DragPreviewOption](../harmonyos-references/capi-arkui-nativemodule-arkui-dragpreviewoption.md)，可用于设置跟手图的圆角、角标等。

   ```
   1. // 创建pixelMap
   2. uint8_t data[960000];
   3. size_t dataSize = 960000;
   4. for (int i = 0; i < dataSize; i++) {
   5. data[i] = i + 1;
   6. }
   7. // 创建参数结构体实例，并设置参数
   8. OH_Pixelmap_InitializationOptions *createOpts;
   9. OH_PixelmapInitializationOptions_Create(&createOpts);
   10. OH_PixelmapInitializationOptions_SetWidth(createOpts, 200U);
   11. OH_PixelmapInitializationOptions_SetHeight(createOpts, 200U);
   12. OH_PixelmapInitializationOptions_SetPixelFormat(createOpts, PIXEL_FORMAT_BGRA_8888);
   13. OH_PixelmapInitializationOptions_SetAlphaType(createOpts, PIXELMAP_ALPHA_TYPE_UNKNOWN);
   14. // 设置自定义跟手图
   15. OH_PixelmapNative *pixelmap = nullptr;
   16. OH_PixelmapNative_CreatePixelmap(data, dataSize, createOpts, &pixelmap);
   17. OH_PixelmapNative_Opacity(pixelmap, 0.1f);
   18. OH_ArkUI_SetNodeDragPreview(node, pixelmap);
   19. // 设置跟手图选项
   20. auto *previewOptionsText = OH_ArkUI_CreateDragPreviewOption();
   21. OH_ArkUI_DragPreviewOption_SetScaleMode(previewOptionsText, ARKUI_DRAG_PREVIEW_SCALE_DISABLED);
   22. OH_ArkUI_DragPreviewOption_SetNumberBadgeEnabled(previewOptionsText, true);
   23. OH_ArkUI_DragPreviewOption_SetBadgeNumber(previewOptionsText, 10U);
   24. OH_ArkUI_DragPreviewOption_SetDefaultShadowEnabled(previewOptionsText, true);
   25. OH_ArkUI_DragPreviewOption_SetDefaultRadiusEnabled(previewOptionsText, true);
   26. int returnValue = OH_ArkUI_DragPreviewOption_SetDefaultAnimationBeforeLiftingEnabled(previewOptionsText, true);
   27. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "Manager",
   28. "dragTest DragPreviewOption_SetDefaultAnimationBeforeLiftingEnabled returnValue = %{public}d",
   29. returnValue);
   30. OH_ArkUI_SetNodeDragPreviewOption(node, previewOptionsText);
   ```

   [firstmodule.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDragDrop/entry/src/main/cpp/firstmodule.h#L325-L356)
3. 设置相关事件。

   C API的事件通过统一的回调来接收，当收到事件时通过[eventType](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)进行区分。

   ```
   1. nodeAPI->addNodeEventReceiver(dragNode, [](ArkUI_NodeEvent *event) {
   2. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest", "RegisterNodeEventFirstReceiver called");
   3. auto eventType = OH_ArkUI_NodeEvent_GetEventType(event);
   4. auto preDragStatus = OH_ArkUI_NodeEvent_GetPreDragStatus(event);
   5. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest",
   6. "eventType = %{public}d, preDragStatus = %{public}d", eventType, preDragStatus);
   7. auto *dragEvent = OH_ArkUI_NodeEvent_GetDragEvent(event);
   8. switch (eventType) {
   9. case NODE_ON_PRE_DRAG:
   10. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest", "NODE_ON_PRE_DRAG Event Receive");
   11. break;
   12. case NODE_ON_CLICK:
   13. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest", "NODE_ON_CLICK Event Receive");
   14. break;
   15. case NODE_ON_DROP:
   16. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest", "NODE_ON_DROP Event Receive");
   17. break;
   18. case NODE_ON_DRAG_ENTER:
   19. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest", "NODE_ON_DRAG_ENTER Event Receive");
   20. break;
   21. case NODE_ON_DRAG_MOVE:
   22. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest", "NODE_ON_DRAG_MOVE Event Receive");
   23. break;
   24. case NODE_ON_DRAG_LEAVE:
   25. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest", "NODE_ON_DRAG_LEAVE Event Receive");
   26. break;
   27. case NODE_ON_DRAG_START: {
   28. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest", "NODE_ON_DRAG_START Event Receive");
   29. // ...
   30. break;
   31. }
   32. case NODE_ON_DRAG_END: {
   33. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest", "NODE_ON_DRAG_END Event Receive");
   34. // ...
   35. break;
   36. }
   37. default:
   38. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest", "UNKNOWN Event Receive");
   39. break;
   40. }
   41. });
   ```

   [firstmodule.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDragDrop/entry/src/main/cpp/firstmodule.h#L153-L200)
4. 处理NODE\_ON\_DRAG\_START事件。

   在NODE\_ON\_DRAG\_START事件中，应用可以执行起拖阶段所需的操作，通常涉及处理起拖过程的数据。例如，创建[OH\_UdmfRecord](../harmonyos-references/capi-udmf-oh-udmfrecord.md)，将用于拖拽图片所需的数据imageValue以[OH\_UdsFileUri](../harmonyos-references/capi-udmf-oh-udsfileuri.md)类型添加到OH\_UdmfRecord中，接着将OH\_UdmfRecord设置到[OH\_UdmfData](../harmonyos-references/capi-udmf-oh-udmfdata.md)中，最后将OH\_UdmfData设置到[DragEvent](../harmonyos-references/capi-arkui-nativemodule-arkui-dragevent.md)中。

   ```
   1. void SetImageData(ArkUI_DragEvent* dragEvent)
   2. {
   3. int returnValue;
   4. OH_UdmfRecord *record = OH_UdmfRecord_Create();
   5. OH_UdsFileUri *imageValue = OH_UdsFileUri_Create();
   6. // 图片src/main/resources/base/media/seagull.png需要替换为开发者所需的资源文件
   7. returnValue = OH_UdsFileUri_SetFileUri(imageValue, "/resources/base/media/seagull.png");
   8. returnValue = OH_UdmfRecord_AddFileUri(record, imageValue);
   9. OH_UdmfData *data = OH_UdmfData_Create();
   10. returnValue = OH_UdmfData_AddRecord(data, record);
   11. returnValue = OH_ArkUI_DragEvent_SetData(dragEvent, data);
   12. }
   13. // ···
   14. case NODE_ON_DRAG_START: {
   15. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest", "NODE_ON_DRAG_START EventReceiver");
   16. SetImageData(dragEvent);
   17. break;
   18. }
   ```

   [thirdmodule.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDragDrop/entry/src/main/cpp/thirdmodule.h#L32-L102)
5. 处理NODE\_ON\_DROP事件。

   在NODE\_ON\_DROP事件中，应用可以执行与落入阶段相关的操作，通常需要获取拖拽过程中传递的数据。例如，引用[udmf\_meta.h](../harmonyos-references/capi-udmf-meta-h.md)头文件，获取[OH\_UdmfData](../harmonyos-references/capi-udmf-oh-udmfdata.md)，判断是否存在所需的数据类型，从[OH\_UdmfRecord](../harmonyos-references/capi-udmf-oh-udmfrecord.md)中提取相应的数据，最后销毁指针。

   ```
   1. void GetDragData(ArkUI_DragEvent* dragEvent)
   2. {
   3. // 获取UDMF data
   4. int returnValue;
   5. // 创建OH_UdmfData对象
   6. OH_UdmfData *data = OH_UdmfData_Create();
   7. returnValue = OH_ArkUI_DragEvent_GetUdmfData(dragEvent, data);
   8. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest",
   9. "OH_ArkUI_DragEvent_GetUdmfData returnValue = %{public}d", returnValue);
   10. // 判断OH_UdmfData是否有对应的类型
   11. bool resultUdmf = OH_UdmfData_HasType(data, UDMF_META_GENERAL_FILE);
   12. if (resultUdmf) {
   13. // 获取OH_UdmfData的记录
   14. unsigned int recordsCount = 0;
   15. OH_UdmfRecord **records = OH_UdmfData_GetRecords(data, &recordsCount);
   16. // 获取records中的元素
   17. int returnStatus;
   18. for (int i = 0; i < recordsCount; i++) {
   19. // 从OH_UdmfRecord中获取文件类型数据
   20. OH_UdsFileUri *imageValue = OH_UdsFileUri_Create();
   21. returnStatus = OH_UdmfRecord_GetFileUri(records[i], imageValue);
   22. const char *fileUri = OH_UdsFileUri_GetFileUri(imageValue);
   23. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest",
   24. "dragTest OH_UdmfRecord_GetPlainText "
   25. "returnStatus= %{public}d "
   26. "fileUri= %{public}s",
   27. returnStatus, fileUri);
   28. // 使用结束后销毁指针
   29. OH_UdsFileUri_Destroy(imageValue);
   30. }
   31. if (recordsCount != 0) {
   32. OH_ArkUI_DragEvent_SetDragResult(dragEvent, ARKUI_DRAG_RESULT_SUCCESSFUL);
   33. ArkUI_DropOperation option;
   34. OH_ArkUI_DragEvent_GetDropOperation(dragEvent, &option);
   35. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest",
   36. "OH_ArkUI_DragEvent_GetDropOperation returnValue = %{public}d", option);
   37. }
   38. } else {
   39. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest",
   40. "OH_UdmfData_HasType not contain UDMF_META_GENERAL_FILE");
   41. }
   42. int32_t count;
   43. OH_ArkUI_DragEvent_GetDataTypeCount(dragEvent, &count);
   44. if (count <= 0 || count >= 128U) {
   45. return;
   46. }
   47. char **eventTypeArray = new char *[count];
   48. for (int i = 0; i < count; i++) {
   49. eventTypeArray[i] = new char[128U];
   50. }
   51. OH_ArkUI_DragEvent_GetDataTypes(dragEvent, eventTypeArray, count, 128U);
   52. for (int i = 0; i < count; i++) {
   53. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest",
   54. "OH_ArkUI_DragEvent_GetDataTypes returnValue = %{public}s", eventTypeArray[i]);
   55. }
   56. }
   57. // ...
   58. case NODE_ON_DROP: {
   59. OH_ArkUI_DragEvent_SetSuggestedDropOperation(dragEvent, ARKUI_DROP_OPERATION_COPY);
   60. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest", "NODE_ON_DROP EventReceiver");
   61. GetDragData(dragEvent);
   62. break;
   63. }
   ```

   [firstmodule.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDragDrop/entry/src/main/cpp/firstmodule.h#L88-L225)

## DragAction主动发起拖拽

除了通用拖拽以外，ArkUI还提供了使用C API实现主动发起拖拽的能力。以下以文本拖拽为例，详细介绍C-API实现主动发起拖拽的基本步骤，以及在开发过程中需要注意的事项。完整示例请参考[NativeDragDrop](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeDragDrop)。

1. 节点注册事件。

   创建Button节点，设置按钮相关属性，同时需要注册[NODE\_ON\_TOUCH\_INTERCEPT](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)事件。

   ```
   1. // buttonTouch作为targetId，用于区分不同target的事件。
   2. enum {
   3. BUTTON_TOUCH = 1
   4. };

   6. dragButton = nodeAPI->createNode(ARKUI_NODE_BUTTON);
   7. SetId(dragButton, "dragBt3");
   8. SetCommonAttribute(dragButton, 80.0f, 50.0f, 0xFFFF0000, 20.0f);
   9. SetButtonLabel(dragButton, "拖起");
   10. nodeAPI->registerNodeEvent(dragButton, NODE_ON_TOUCH_INTERCEPT, BUTTON_TOUCH, nullptr);
   ```

   [forthmodule.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDragDrop/entry/src/main/cpp/forthmodule.h#L144-L155)

   ```
   1. #define DEFAULT_WIDTH 200.0
   2. // 设置节点宽度
   3. void SetWidth(ArkUI_NodeHandle &node, float width = DEFAULT_WIDTH)
   4. {
   5. if (!nodeAPI) {
   6. return;
   7. }
   8. ArkUI_NumberValue widthValue[] = {width};
   9. ArkUI_AttributeItem widthItem = {widthValue, 1};
   10. nodeAPI->setAttribute(node, NODE_WIDTH, &widthItem);
   11. }

   13. #define DEFAULT_HEIGHT 200.0
   14. // 设置节点高度
   15. void SetHeight(ArkUI_NodeHandle &node, float height = DEFAULT_HEIGHT)
   16. {
   17. if (!nodeAPI) {
   18. return;
   19. }
   20. ArkUI_NumberValue heightValue[] = {height};
   21. ArkUI_AttributeItem heightItem = {heightValue, 1};
   22. nodeAPI->setAttribute(node, NODE_HEIGHT, &heightItem);
   23. }

   25. #define DEFAULT_BG_COLOR 0xFFFFFFFF
   26. // 设置节点背景颜色
   27. void SetBackgroundColor(ArkUI_NodeHandle &node, uint32_t color = DEFAULT_BG_COLOR)
   28. {
   29. if (!nodeAPI) {
   30. return;
   31. }
   32. ArkUI_NumberValue colorValue[] = {{.u32 = color}};
   33. ArkUI_AttributeItem colorItem = {colorValue, 1};
   34. nodeAPI->setAttribute(node, NODE_BACKGROUND_COLOR, &colorItem);
   35. }

   37. #define DEFAULT_MARGIN 5.0
   38. // 设置节点外边距
   39. void SetMargin(ArkUI_NodeHandle &node, float margin = DEFAULT_MARGIN)
   40. {
   41. if (!nodeAPI) {
   42. return;
   43. }
   44. ArkUI_NumberValue marginValue[] = {margin};
   45. ArkUI_AttributeItem marginItem = {marginValue, 1};
   46. nodeAPI->setAttribute(node, NODE_MARGIN, &marginItem);
   47. }

   49. // 设置Button节点标签
   50. void SetButtonLabel(ArkUI_NodeHandle &node, const char *label)
   51. {
   52. if (!nodeAPI) {
   53. return;
   54. }
   55. ArkUI_AttributeItem NODE_Button_SRC_Item = {.string = label};
   56. nodeAPI->setAttribute(node, NODE_BUTTON_LABEL, &NODE_Button_SRC_Item);
   57. }

   59. // 设置节点标识符
   60. void SetId(ArkUI_NodeHandle &node, const char *id)
   61. {
   62. if (!nodeAPI) {
   63. return;
   64. }
   65. ArkUI_AttributeItem idItem = {.string = id};
   66. nodeAPI->setAttribute(node, NODE_ID, &idItem);
   67. }

   69. #define DEFAULT_BORDER_WIDTH 0.0
   70. // 设置节点边框宽度
   71. void SetBorderWidth(ArkUI_NodeHandle &node, float width = DEFAULT_BORDER_WIDTH)
   72. {
   73. if (!nodeAPI) {
   74. return;
   75. }
   76. ArkUI_NumberValue borderWidthValue[] = {width};
   77. ArkUI_AttributeItem borderWidthItem = {borderWidthValue, 1};
   78. nodeAPI->setAttribute(node, NODE_BORDER_WIDTH, &borderWidthItem);
   79. }

   81. #define DEFAULT_BORDER_COLOR 0xFF000000
   82. // 设置节点边框颜色
   83. void SetBorderColor(ArkUI_NodeHandle &node, uint32_t color = DEFAULT_BORDER_COLOR)
   84. {
   85. if (!nodeAPI) {
   86. return;
   87. }
   88. ArkUI_NumberValue borderColorValue[] = {{.u32 = color}};
   89. ArkUI_AttributeItem borderColorItem = {borderColorValue, 1};
   90. nodeAPI->setAttribute(node, NODE_BORDER_COLOR, &borderColorItem);
   91. }

   93. // 设置节点常用属性（宽高、背景色、外边距、边框样式）
   94. void SetCommonAttribute(ArkUI_NodeHandle &node, float width = DEFAULT_WIDTH, float height = DEFAULT_HEIGHT,
   95. unsigned int color = DEFAULT_BG_COLOR, float margin = DEFAULT_MARGIN)
   96. {
   97. SetWidth(node, width);
   98. SetHeight(node, height);
   99. SetBackgroundColor(node, color);
   100. SetMargin(node, margin);
   101. SetBorderWidth(node, DEFAULT_BORDER_WIDTH);
   102. SetBorderColor(node);
   103. }
   ```

   [common.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDragDrop/entry/src/main/cpp/common.h#L91-L195)
2. 接收NODE\_ON\_TOUCH\_INTERCEPT事件。

   DragAction主动发起拖拽需通过事件触发，在NODE\_ON\_TOUCH\_INTERCEPT事件中执行发起拖拽所需的操作，通过[targetId](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeevent_gettargetid)区分不同按钮触发的事件。

   ```
   1. nodeAPI->addNodeEventReceiver(dragButton, [](ArkUI_NodeEvent *event) {
   2. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest", "RegisterNodeEventForthReceiver called");
   3. auto eventType = OH_ArkUI_NodeEvent_GetEventType(event);
   4. auto preDragStatus = OH_ArkUI_NodeEvent_GetPreDragStatus(event);
   5. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest",
   6. "eventType = %{public}d, preDragStatus = %{public}d", eventType, preDragStatus);

   8. auto *dragEvent = OH_ArkUI_NodeEvent_GetDragEvent(event);
   9. switch (eventType) {
   10. case NODE_ON_TOUCH_INTERCEPT: {
   11. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest", "NODE_ON_TOUCH_INTERCEPT EventReceiver");
   12. // ...
   13. break;
   14. }
   15. default: {
   16. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest", "UNKNOWN EventReceiver");
   17. break;
   18. }
   19. }
   20. });
   ```

   [forthmodule.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDragDrop/entry/src/main/cpp/forthmodule.h#L49-L92)
3. 起拖阶段设置。

   在NODE\_ON\_TOUCH\_INTERCEPT事件中，需要对DragAction进行相关设置。为了主动发起拖拽，需要创建[pixelMap](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmapnative_createpixelmap)，设置[ArkUI\_DragPreviewOption](../harmonyos-references/capi-arkui-nativemodule-arkui-dragpreviewoption.md)和跟手点，并将拖拽过程中的文本数据设置到DragAction中。

   ```
   1. case NODE_ON_TOUCH_INTERCEPT: {
   2. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest", "NODE_ON_TOUCH_INTERCEPT EventReceiver");
   3. // 创建DragAction
   4. action = OH_ArkUI_CreateDragActionWithNode(dragButton);
   5. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest",
   6. "OH_ArkUI_CreateDragActionWithNode returnValue = %{public}p", action);
   7. // 设置pixelMap
   8. std::vector<OH_PixelmapNative *> pixelVector;
   9. SetPixelMap(pixelVector);
   10. // 设置DragPreviewOption
   11. SetDragPreviewOption();
   12. // 设置pointerId、touchPoint
   13. PrintDragActionInfos();
   14. // 设置unifiedData
   15. SetDragActionData();
   16. // startDrag
   17. int returnValue = OH_ArkUI_StartDrag(action);
   18. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest",
   19. "OH_ArkUI_StartDrag returnValue = %{public}d",
   20. returnValue);
   21. OH_ArkUI_DragAction_Dispose(action);
   22. break;
   23. }
   24. // ...
   25. void SetDragActionData()
   26. {
   27. // 创建OH_UdmfRecord对象
   28. OH_UdmfRecord *record = OH_UdmfRecord_Create();
   29. // 向OH_UdmfRecord中添加纯文本类型数据
   30. OH_UdsPlainText *plainText = OH_UdsPlainText_Create();
   31. int returnStatus;
   32. OH_UdsPlainText_SetAbstract(plainText, "this is plainText Abstract example");
   33. OH_UdsPlainText_SetContent(plainText, "this is plainText Content example");
   34. returnStatus = OH_UdmfRecord_AddPlainText(record, plainText);
   35. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest",
   36. "dragTest OH_UdmfRecord_AddPlainText returnStatus = %{public}d", returnStatus);
   37. // 创建OH_UdmfData对象
   38. OH_UdmfData *data = OH_UdmfData_Create();
   39. // 向OH_UdmfData中添加OH_UdmfRecord
   40. returnStatus = OH_UdmfData_AddRecord(data, record);
   41. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest",
   42. "dragTest OH_UdmfData_AddRecord returnStatus = %{public}d", returnStatus);
   43. int returnValue = OH_ArkUI_DragAction_SetData(action, data);
   44. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest",
   45. "OH_ArkUI_DragAction_SetData returnValue = %{public}d", returnValue);
   46. // 注册拖拽状态监听回调
   47. OH_ArkUI_DragAction_RegisterStatusListener(action, data, &DragStatusListener);
   48. }
   ```

   [forthmodule.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDragDrop/entry/src/main/cpp/forthmodule.h#L59-L196)

   ```
   1. void SetPixelMap(std::vector<OH_PixelmapNative *> &pixelVector)
   2. {
   3. uint8_t data[960000];
   4. size_t dataSize = 960000;
   5. for (int i = 0; i < dataSize; i++) {
   6. data[i] = i + 1;
   7. }
   8. // 创建参数结构体实例，并设置参数
   9. OH_Pixelmap_InitializationOptions *createOpts;
   10. OH_PixelmapInitializationOptions_Create(&createOpts);
   11. OH_PixelmapInitializationOptions_SetWidth(createOpts, 200U);
   12. OH_PixelmapInitializationOptions_SetHeight(createOpts, 300U);
   13. OH_PixelmapInitializationOptions_SetPixelFormat(createOpts, PIXEL_FORMAT_BGRA_8888);
   14. OH_PixelmapInitializationOptions_SetAlphaType(createOpts, PIXELMAP_ALPHA_TYPE_UNKNOWN);
   15. // 创建Pixelmap实例
   16. OH_PixelmapNative *pixelmap = nullptr;
   17. OH_PixelmapNative_CreatePixelmap(data, dataSize, createOpts, &pixelmap);
   18. OH_PixelmapNative_Flip(pixelmap, true, true);
   19. pixelVector.push_back(pixelmap);
   20. int returnValue = OH_ArkUI_DragAction_SetPixelMaps(action, pixelVector.data(), pixelVector.size());
   21. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest",
   22. "OH_ArkUI_DragAction_SetPixelMaps returnValue = %{public}d", returnValue);
   23. }

   25. void SetDragPreviewOption()
   26. {
   27. auto *previewOptions = OH_ArkUI_CreateDragPreviewOption();
   28. OH_ArkUI_DragPreviewOption_SetScaleMode(previewOptions,
   29. ArkUI_DragPreviewScaleMode::ARKUI_DRAG_PREVIEW_SCALE_DISABLED);
   30. OH_ArkUI_DragPreviewOption_SetDefaultShadowEnabled(previewOptions, true);
   31. OH_ArkUI_DragPreviewOption_SetDefaultRadiusEnabled(previewOptions, true);
   32. int returnValue = OH_ArkUI_DragAction_SetDragPreviewOption(action, previewOptions);
   33. OH_ArkUI_DragPreviewOption_Dispose(previewOptions);
   34. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest",
   35. "OH_ArkUI_DragAction_SetDragPreviewOption returnValue = %{public}d", returnValue);
   36. }

   38. void PrintDragActionInfos()
   39. {
   40. // 设置pointerId
   41. int returnValue = OH_ArkUI_DragAction_SetPointerId(action, 0);
   42. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest",
   43. "OH_ArkUI_DragAction_SetPointerId returnValue = %{public}d", returnValue);
   44. // 设置touchPoint
   45. returnValue = OH_ArkUI_DragAction_SetTouchPointX(action, 200.0f);
   46. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest",
   47. "OH_ArkUI_DragAction_SetTouchPointX returnValue = %{public}d", returnValue);
   48. returnValue = OH_ArkUI_DragAction_SetTouchPointY(action, 200.0f);
   49. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest",
   50. "OH_ArkUI_DragAction_SetTouchPointY returnValue = %{public}d", returnValue);
   51. }
   ```

   [common.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDragDrop/entry/src/main/cpp/common.h#L291-L343)
4. 处理NODE\_ON\_DROP事件。

   在NODE\_ON\_DROP事件中，应用可以执行与落入阶段相关的操作。通常情况下，需要从DragEvent中获取拖拽过程中传递的数据，DragAction中的拖拽数据也需要通过DragEvent获取。

   ```
   1. case NODE_ON_DROP: {
   2. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest", "NODE_ON_DROP EventReceiver");
   3. GetUdmfDataText(dragEvent);
   4. OH_ArkUI_DragAction_UnregisterStatusListener(action);
   5. break;
   6. }
   7. // ...
   8. void GetUdmfDataText(ArkUI_DragEvent* dragEvent)
   9. {
   10. // 获取UDMF data
   11. int returnValue;
   12. // 创建OH_UdmfData对象
   13. OH_UdmfData *data = OH_UdmfData_Create();
   14. returnValue = OH_ArkUI_DragEvent_GetUdmfData(dragEvent, data);
   15. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest",
   16. "OH_ArkUI_DragEvent_GetUdmfData returnValue = %{public}d", returnValue);
   17. // 判断OH_UdmfData是否有对应的类型
   18. bool resultUdmf = OH_UdmfData_HasType(data, UDMF_META_PLAIN_TEXT);
   19. if (resultUdmf) {
   20. // 获取OH_UdmfData的记录
   21. unsigned int recordsCount = 0;
   22. OH_UdmfRecord **records = OH_UdmfData_GetRecords(data, &recordsCount);
   23. // 获取records中的元素
   24. int returnStatus;
   25. for (int i = 0; i < recordsCount; i++) {
   26. // 从OH_UdmfRecord中获取纯文本类型数据
   27. OH_UdsPlainText *plainTextValue = OH_UdsPlainText_Create();
   28. returnStatus = OH_UdmfRecord_GetPlainText(records[i], plainTextValue);
   29. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest",
   30. "dragTest OH_UdmfRecord_GetPlainText "
   31. "returnStatus= %{public}d",
   32. returnStatus);
   33. auto getAbstract = OH_UdsPlainText_GetAbstract(plainTextValue);
   34. auto getContent = OH_UdsPlainText_GetContent(plainTextValue);
   35. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest",
   36. "OH_UdsPlainText_GetAbstract = "
   37. "%{public}s, OH_UdsPlainText_GetContent = "
   38. "%{public}s",
   39. getAbstract, getContent);
   40. // 使用结束后销毁指针
   41. OH_UdsPlainText_Destroy(plainTextValue);
   42. }
   43. } else {
   44. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00U, "dragTest",
   45. "OH_UdmfData_HasType not contain UDMF_META_PLAIN_TEXT");
   46. }
   47. OH_UdmfData_Destroy(data);
   48. }
   ```

   [forthmodule.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDragDrop/entry/src/main/cpp/forthmodule.h#L110-L240)
