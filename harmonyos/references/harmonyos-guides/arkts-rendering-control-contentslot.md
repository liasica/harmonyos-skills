---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-contentslot
title: ContentSlot：混合开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5c5b8e3f102ad6c1a70f260c72003d730f04a7a3ea19e4878dc2c4cad5ab3695
---

用于渲染并管理Native层使用C-API创建的组件。

支持[混合模式](complex-drawing-effect-c.md#混合模式)开发。当容器为ArkTS组件，且子组件在Native侧创建时，推荐使用ContentSlot占位组件。

说明

ContentSlot从API version 12开始支持。

本文档仅为开发指南。组件接口规范见[ContentSlot API参数说明](../harmonyos-references/ts-components-contentslot.md)。

## 接口

### ArkTS侧接口

| 接口名 | 描述 |
| --- | --- |
| ContentSlot(content: Content) | Content作为ContentSlot的管理器，通过Native侧提供的接口，可以注册并触发ContentSlot的上下树事件回调以及管理ContentSlot的子组件。 |

```
1. abstract class Content {
2. }
```

### Native侧接口

| 接口名 | 描述 |
| --- | --- |
| [OH\_ArkUI\_NodeContent\_RegisterCallback(ArkUI\_NodeContentHandle content, ArkUI\_NodeContentCallback callback)](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodecontent_registercallback) | 向管理器Content上注册事件。 |
| [OH\_ArkUI\_NodeContentEvent\_GetEventType(ArkUI\_NodeContentEvent\* event)](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodecontentevent_geteventtype) | 获取Content上触发的事件类型。 |
| [OH\_ArkUI\_NodeContent\_AddNode(ArkUI\_NodeContentHandle content, ArkUI\_NodeHandle node)](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodecontent_addnode) | 在Content上添加子组件。 |
| [OH\_ArkUI\_NodeContent\_InsertNode(ArkUI\_NodeContentHandle content, ArkUI\_NodeHandle node, int32\_t position)](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodecontent_insertnode) | 在Content上插入子组件。 |
| [OH\_ArkUI\_NodeContent\_RemoveNode(ArkUI\_NodeContentHandle content, ArkUI\_NodeHandle node)](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodecontent_removenode) | 在Content上移除子组件。 |
| [OH\_ArkUI\_GetNodeContentFromNapiValue(napi\_env env, napi\_value value, ArkUI\_NodeContentHandle\* content)](../harmonyos-references/capi-native-node-napi-h.md#oh_arkui_getnodecontentfromnapivalue) | 获取ArkTS侧创建的NodeContent对象，映射到Native侧的ArkUI\_NodeContentHandle。 |
| [OH\_ArkUI\_NodeContentEvent\_GetNodeContentHandle(ArkUI\_NodeContentEvent\* event)](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodecontentevent_getnodecontenthandle) | 获取触发上下树事件的Content对象。 |
| [OH\_ArkUI\_NodeContent\_SetUserData(ArkUI\_NodeContentHandle content, void\* userData)](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodecontent_setuserdata) | 在Content上设置用户自定义属性。 |
| [OH\_ArkUI\_NodeContent\_GetUserData(ArkUI\_NodeContentHandle content)](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodecontent_getuserdata) | 在Content上获取用户自定义属性。 |
| typedef enum {  NODE\_CONTENT\_EVENT\_ON\_ATTACH\_TO\_WINDOW = 0,  NODE\_CONTENT\_EVENT\_ON\_DETACH\_FROM\_WINDOW = 1,  } [ArkUI\_NodeContentEventType](../harmonyos-references/capi-native-node-h.md#arkui_nodecontenteventtype) | Content上会触发的上树和下树事件类型。 |

## 开发实现

### ArkTS侧代码实现

```
1. import nativeNode from 'libentry.so'; // 开发者自己实现的so
2. import { NodeContent } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Parent {
7. private nodeContent: Content = new NodeContent();
8. // ...

10. aboutToAppear() {
11. // 通过C-API创建节点，并添加到管理器nodeContent上
12. nativeNode.createNativeNode(this.nodeContent);
13. // ...
14. }

16. build() {
17. Column() {
18. // 显示nodeContent管理器里存放的Native侧的组件
19. ContentSlot(this.nodeContent);
20. // ...
21. }
22. }
23. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControlContentslotNDK/entry/src/main/ets/pages/Index.ets#L17-L58)

### Native侧代码实现

Napi的基础开发知识请查看以下文档：[开发导读](ndk-development-overview.md)。

本章节描述实现ContentSlot相关逻辑代码。创建C侧组件的具体步骤，请参阅[使用NDK接口构建UI](ndk-build-ui-overview.md)。

```
1. #include "napi/native_api.h"
2. #include "arkui/native_type.h"
3. #include "arkui/native_node.h"
4. #include "arkui/native_node_napi.h"
5. #include "arkui/native_interface.h"
6. #include "hilog/log.h"
7. // ···
8. ArkUI_NodeContentHandle nodeContentHandle_ = nullptr;
9. ArkUI_NativeNodeAPI_1 *nodeAPI;
10. const unsigned int LOG_PRINT_DOMAIN = 0xFF00;

12. // 在Native侧创建一个宽高为480vp*480vp、背景色为0xFFFF0000（红色）的Column组件。对于更详细的节点树创建方法，请参考ArkUI API文档的C API章节。
13. ArkUI_NodeHandle NodeManager::CreateNodeHandle()
14. {
15. ArkUI_NodeHandle column = nodeAPI->createNode(ARKUI_NODE_COLUMN);
16. ArkUI_NumberValue value[] = {480};
17. ArkUI_AttributeItem item{value, 1};
18. nodeAPI->setAttribute(column, NODE_WIDTH, &item);
19. nodeAPI->setAttribute(column, NODE_HEIGHT, &item);
20. value[0].u32 = 0xFFFF0000;
21. nodeAPI->setAttribute(column, NODE_BACKGROUND_COLOR, &item);
22. return column;
23. }

25. // ArkTS侧createNativeNode方法在Native侧的具体实现
26. napi_value NodeManager::CreateNativeNode(napi_env env, napi_callback_info info)
27. {
28. // napi相关处理空指针&数据越界等问题
29. if ((env == nullptr) || (info == nullptr)) {
30. return nullptr;
31. }

33. size_t argc = 1;
34. napi_value args[1] = { nullptr };
35. if (napi_get_cb_info(env, info, &argc, args, nullptr, nullptr) != napi_ok) {
36. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "Manager", "CreateNativeNode napi_get_cb_info failed");
37. }

39. if (argc != 1) {
40. return nullptr;
41. }

43. nodeAPI = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
44. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));

46. // 将nodeContentHandle_指向ArkTS侧传入的nodeContent
47. OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &nodeContentHandle_);

49. if (nodeAPI != nullptr) {
50. if (nodeAPI->createNode != nullptr && nodeAPI->addChild != nullptr) {
51. ArkUI_NodeHandle component;
52. // 创建C侧组件
53. component = CreateNodeHandle();
54. // 将组件添加到nodeContent管理器中
55. OH_ArkUI_NodeContent_AddNode(nodeContentHandle_, component);
56. // ···
57. }
58. }
59. return nullptr;
60. }
```

[manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControlContentslotNDK/entry/src/main/cpp/manager.cpp#L16-L92)

### Native侧主要接口使用说明

* 注册上下树事件，并通过事件获取对应的Content对象。

  ```
  1. auto nodeContentEvent = [](ArkUI_NodeContentEvent *event) {
  2. ArkUI_NodeContentHandle content = OH_ArkUI_NodeContentEvent_GetNodeContentHandle(event);
  3. // 针对不同content需要额外做的逻辑
  4. if (OH_ArkUI_NodeContentEvent_GetEventType(event) == NODE_CONTENT_EVENT_ON_ATTACH_TO_WINDOW) {
  5. // ContentSlot上树时需要触发的逻辑
  6. // ···
  7. } else if (OH_ArkUI_NodeContentEvent_GetEventType(event) == NODE_CONTENT_EVENT_ON_DETACH_FROM_WINDOW) {
  8. // ContentSlot下树时需要触发的逻辑
  9. // ···
  10. };
  11. };
  12. // 将该事件注册到nodeContent上
  13. OH_ArkUI_NodeContent_RegisterCallback(nodeContentHandle_, nodeContentEvent);
  ```

  [manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControlContentslotNDK/entry/src/main/cpp/manager.cpp#L119-L141)
* 添加子组件。

  ```
  1. ArkUI_NodeHandle component;
  2. // 创建C侧组件
  3. component = CreateNodeHandle();
  4. // 将组件添加到nodeContent管理器中
  5. OH_ArkUI_NodeContent_AddNode(nodeContentHandle_, component);
  ```

  [manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControlContentslotNDK/entry/src/main/cpp/manager.cpp#L69-L75)
* 插入子组件。

  ```
  1. size_t position = 0;
  2. ArkUI_NodeHandle component1 = CreateNodeHandle();
  3. // 将组件插入nodeContent管理器对应位置
  4. OH_ArkUI_NodeContent_InsertNode(nodeContentHandle_, component1, position);
  ```

  [manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControlContentslotNDK/entry/src/main/cpp/manager.cpp#L77-L82)
* 删除子组件。

  ```
  1. // 在nodeContent中移除对应组件
  2. OH_ArkUI_NodeContent_RemoveNode(nodeContentHandle_, component1);
  ```

  [manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControlContentslotNDK/entry/src/main/cpp/manager.cpp#L83-L86)
* 设置自定义属性。

  ```
  1. // 创建需要定义的自定义数据
  2. void *userData = CreateUserData();
  3. OH_ArkUI_NodeContent_SetUserData(nodeContentHandle_, userData);
  ```

  [manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControlContentslotNDK/entry/src/main/cpp/manager.cpp#L110-L114)
* 获取自定义属性。

  ```
  1. void *userData = OH_ArkUI_NodeContent_GetUserData(nodeContentHandle_);
  ```

  [manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControlContentslotNDK/entry/src/main/cpp/manager.cpp#L102-L104)

## 绑定规则说明

如果将同一个Content对象绑定到多个ContentSlot组件，最终该Content的内容仅在最后一个绑定的ContentSlot中显示，其他ContentSlot将不显示任何内容。

**原因说明：**

Content与ContentSlot节点具有一对一的绑定关系。同一Content不能同时关联多个ContentSlot节点。如果尝试将同一Content挂载到多个ContentSlot节点，仅最后一次挂载生效，之前的ContentSlot节点将失去Content的关联，导致组件内容无法显示。

若需在多个ContentSlot节点下显示相同内容，每个节点需创建单独的Content。示例如下：

```
1. import nativeNode from 'libentry.so'; // 开发者自己实现的so
2. import { NodeContent } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Parent {
7. // ···
8. private nodeContent_1: Content = new NodeContent();
9. private nodeContent_2: Content = new NodeContent();

11. aboutToAppear() {
12. // ···
13. // 通过C-API创建节点，并添加到管理器nodeContent_1和nodeContent_2上
14. nativeNode.createNativeNode(this.nodeContent_1);
15. nativeNode.createNativeNode(this.nodeContent_2);
16. }

18. build() {
19. Column() {
20. // ···
21. ContentSlot(this.nodeContent_1);// nodeContent_1将被挂载到下一个Contentslot节点，此处无法显示
22. ContentSlot(this.nodeContent_1); // 正常显示
23. ContentSlot(this.nodeContent_2); // 正常显示
24. }
25. }
26. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControlContentslotNDK/entry/src/main/ets/pages/Index.ets#L16-L59)
