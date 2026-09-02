---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-textarea-event
title: 添加输入框文本事件监听
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 使用文本 > 添加输入框文本事件监听
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f6531ced237561253c16164e4bb63f5f96309b7c00eff960f8c24006b2f02509
---

输入框包含多种交互行为，开发者可注册事件监听并获取状态。以下以多行文本输入框为例进行说明，单行文本输入框添加文本事件监听的步骤与此类似。

要实现实时搜索功能，可注册[NODE\_TEXT\_AREA\_ON\_CHANGE](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)事件，输入框文本发生变化时会收到通知，并能获取当前文本内容。

要实现文字过滤功能，可注册[NODE\_TEXT\_AREA\_ON\_WILL\_INSERT](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)事件，在文字即将插入前会收到通知，通过返回值控制文字是否插入。

要实现用户编辑文字前后页面布局的不同，可注册[NODE\_TEXT\_AREA\_ON\_EDIT\_CHANGE](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)事件，输入框编辑状态切换时会收到通知。

以下示例基于[接入ArkTS页面章节](ndk-access-the-arkts-page.md)，说明如何监听输入框的事件及数据解析。

* 注册事件

  事件注册有统一接口，详情请参见[registerNodeEvent](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeevent)。输入框支持的事件类型，请参见NativeNode组件支持的事件类型定义[ArkUI\_NodeEventType](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)，搜索前缀NODE\_TEXT\_AREA\_。

  ```
  ArkUI_NodeHandle text = nodeApi->createNode(ARKUI_NODE_TEXT);
  ArkUI_NumberValue textWidth[] = {{.f32 = 300}};
  ArkUI_AttributeItem textWidthItem = {.value = textWidth, .size = 1};
  nodeApi->setAttribute(text, NODE_WIDTH, &textWidthItem);
  // ···
  ArkUI_NodeHandle selectionText = nodeApi->createNode(ARKUI_NODE_TEXT);
  ArkUI_NumberValue selectionTextWidth[] = {{.f32 = 300}};
  ArkUI_AttributeItem selectionTextWidthItem = {.value = selectionTextWidth, .size = 1};
  nodeApi->setAttribute(selectionText, NODE_WIDTH, &selectionTextWidthItem);
  // ···
  const ArkUI_AttributeItem *attributeItem = nodeApi->getAttribute(textArea, NODE_UNIQUE_ID);
  auto id = attributeItem->value[0].i32;
  nodeApi->registerNodeEvent(textArea, NODE_TEXT_AREA_ON_CHANGE, id, text);
  nodeApi->registerNodeEvent(textArea, NODE_TEXT_AREA_ON_PASTE, id, text);
  nodeApi->registerNodeEvent(textArea, NODE_TEXT_AREA_ON_TEXT_SELECTION_CHANGE, id, selectionText);
  ```
* 注册事件回调

  事件回调注册有统一接口，详情请参见[registerNodeEventReceiver](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeeventreceiver)。

  ```
  nodeApi->registerNodeEventReceiver([](ArkUI_NodeEvent *event) {
      ArkUI_NodeEventType eventType = OH_ArkUI_NodeEvent_GetEventType(event);
      ArkUI_AttributeItem content;
      if (eventType == NODE_TEXT_AREA_ON_CHANGE || eventType == NODE_TEXT_AREA_ON_PASTE) {
          ArkUI_StringAsyncEvent *stringEvent = OH_ArkUI_NodeEvent_GetStringAsyncEvent(event);
          content = {.string = stringEvent->pStr };
      } else if (eventType == NODE_TEXT_AREA_ON_TEXT_SELECTION_CHANGE) {
          ArkUI_NodeComponentEvent *componentEvent = OH_ArkUI_NodeEvent_GetNodeComponentEvent(event);
          std::stringstream selectContent;
          selectContent << "start: " << componentEvent->data[0].i32 << " , end: " << componentEvent->data[1].i32;
          content = {.string = selectContent.str().c_str() };
      } else {
          return;
      }
      ArkUI_NodeHandle textNode = reinterpret_cast<ArkUI_NodeHandle>(OH_ArkUI_NodeEvent_GetUserData(event));
      if (textNode) {
          ArkUI_NativeNodeAPI_1 *nodeApi = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
              OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
          nodeApi->setAttribute(textNode, NODE_TEXT_CONTENT, &content);
      }
  });
  ```
* 完整示例

  本篇示例仅提供核心接口的调用方法，完整的示例工程请参考[TextAreaEventNDK](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/TextAreaEventNDK)。

  ```
  #include "manager.h"
  #include <sstream>
  #include <arkui/native_interface.h>
  #include <arkui/styled_string.h>
  #include <hilog/log.h>

  #define CUSTOM_LOG_TAG "manager"
  #define LOG_ERROR(...) OH_LOG_Print(LOG_APP, LOG_ERROR, 0xD001400, CUSTOM_LOG_TAG, __VA_ARGS__)
  #define LOG_INFO(...) OH_LOG_Print(LOG_APP, LOG_INFO, 0xD001400, CUSTOM_LOG_TAG, __VA_ARGS__)

  namespace ConstIde {
  const uint32_t NUMBER_0 = 0;
  const uint32_t NUMBER_1 = 1;
  constexpr const char *K_LOG_DOMAIN = "Manager";
  } // namespace ConstIde

  Manager Manager::manager_;
  ArkUI_NativeNodeAPI_1 *Manager::nodeAPI_ = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
      OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
  template <class MakeNodeFn>
  static napi_value CreateNativeNode(napi_env env, napi_callback_info info, const char *who, MakeNodeFn makeNodeFn)
  {
      OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, ConstIde::K_LOG_DOMAIN, "%{public}s BEGIN", who);

      if ((env == nullptr) || (info == nullptr)) {
          OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, ConstIde::K_LOG_DOMAIN, "%{public}s env or info is null",
                       who);
          return nullptr;
      }

      size_t argc = ConstIde::NUMBER_1;
      napi_value args[ConstIde::NUMBER_1] = {nullptr};
      napi_status st = napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
      if (st != napi_ok || argc < ConstIde::NUMBER_1) {
          OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, ConstIde::K_LOG_DOMAIN, "%{public}s napi_get_cb_info failed",
                       who);
          return nullptr;
      }

      ArkUI_NodeContentHandle nodeContentHandle = nullptr;
      OH_ArkUI_GetNodeContentFromNapiValue(env, args[ConstIde::NUMBER_0], &nodeContentHandle);
      if (nodeContentHandle == nullptr) {
          OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, ConstIde::K_LOG_DOMAIN,
                       "%{public}s nodeContentHandle is null", who);
          return nullptr;
      }

      OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, ConstIde::K_LOG_DOMAIN, "%{public}s after GetNodeContent", who);

      // 可选：保留对 nodeAPI_ 的健壮性检查（与你现有代码一致）
      if (Manager::nodeAPI_ == nullptr) {
          OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, ConstIde::K_LOG_DOMAIN, "%{public}s nodeAPI_ is null", who);
          return nullptr;
      }

      // 构建具体节点 & 挂载
      ArkUI_NodeHandle page = makeNodeFn();
      if (page == nullptr) {
          OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, ConstIde::K_LOG_DOMAIN, "%{public}s makeNodeFn return null",
                       who);
          return nullptr;
      }

      OH_ArkUI_NodeContent_AddNode(nodeContentHandle, page);
      return nullptr;
  }

  constexpr int32_t NUM_10 = 10;
  constexpr int32_t NUM_28 = 28;
  constexpr int32_t NUM_400 = 400;

  napi_value Manager::CreateTextAreaNativeNode(napi_env__* env, napi_callback_info__* info)
  {
      return CreateNativeNode(env, info, "CreateTextAreaNativeNode",
                              []() -> ArkUI_NodeHandle { return CreateTextAreaNativeNode(); });
  }

  ArkUI_NodeHandle Manager::CreateTextAreaNativeNode()
  {
      ArkUI_NativeNodeAPI_1 *nodeApi = Manager::nodeAPI_;

      ArkUI_NodeHandle column = nodeApi->createNode(ARKUI_NODE_COLUMN);
      ArkUI_NumberValue colWidth[] = {{.f32 = 300}};
      ArkUI_AttributeItem widthItem = {.value = colWidth, .size = 1};
      nodeApi->setAttribute(column, NODE_WIDTH, &widthItem);

      ArkUI_NodeHandle text = nodeApi->createNode(ARKUI_NODE_TEXT);
      ArkUI_NumberValue textWidth[] = {{.f32 = 300}};
      ArkUI_AttributeItem textWidthItem = {.value = textWidth, .size = 1};
      nodeApi->setAttribute(text, NODE_WIDTH, &textWidthItem);
      ArkUI_NumberValue textHeight[] = {{.f32 = 100}};
      ArkUI_AttributeItem textHeightItem = {.value = textHeight, .size = 1};
      nodeApi->setAttribute(text, NODE_HEIGHT, &textHeightItem);
      
      nodeApi->addChild(column, text);
      
      ArkUI_NodeHandle selectionText = nodeApi->createNode(ARKUI_NODE_TEXT);
      ArkUI_NumberValue selectionTextWidth[] = {{.f32 = 300}};
      ArkUI_AttributeItem selectionTextWidthItem = {.value = selectionTextWidth, .size = 1};
      nodeApi->setAttribute(selectionText, NODE_WIDTH, &selectionTextWidthItem);
      nodeApi->addChild(column, selectionText);
      ArkUI_NodeHandle textArea = nodeApi->createNode(ARKUI_NODE_TEXT_AREA);
      ArkUI_NumberValue textAreaWidth[] = {{.f32 = 300}};
      ArkUI_AttributeItem textAreaWidthItem = {.value = textAreaWidth, .size = 1};
      nodeApi->setAttribute(textArea, NODE_WIDTH, &textAreaWidthItem);

      ArkUI_NumberValue borderWidth[] = {{.f32 = 1}};
      ArkUI_AttributeItem borderWidthItem = {.value = borderWidth, .size = 1};
      nodeApi->setAttribute(textArea, NODE_BORDER_WIDTH, &borderWidthItem);

      const ArkUI_AttributeItem *attributeItem = nodeApi->getAttribute(textArea, NODE_UNIQUE_ID);
      auto id = attributeItem->value[0].i32;
      nodeApi->registerNodeEvent(textArea, NODE_TEXT_AREA_ON_CHANGE, id, text);
      nodeApi->registerNodeEvent(textArea, NODE_TEXT_AREA_ON_PASTE, id, text);
      nodeApi->registerNodeEvent(textArea, NODE_TEXT_AREA_ON_TEXT_SELECTION_CHANGE, id, selectionText);
      TextAreaNodeEventReceiver(nodeApi);
      nodeApi->addChild(column, textArea);
      return column;
  }

  void Manager::TextAreaNodeEventReceiver(ArkUI_NativeNodeAPI_1* nodeApi)
  {
      nodeApi->registerNodeEventReceiver([](ArkUI_NodeEvent *event) {
          ArkUI_NodeEventType eventType = OH_ArkUI_NodeEvent_GetEventType(event);
          ArkUI_AttributeItem content;
          if (eventType == NODE_TEXT_AREA_ON_CHANGE || eventType == NODE_TEXT_AREA_ON_PASTE) {
              ArkUI_StringAsyncEvent *stringEvent = OH_ArkUI_NodeEvent_GetStringAsyncEvent(event);
              content = {.string = stringEvent->pStr };
          } else if (eventType == NODE_TEXT_AREA_ON_TEXT_SELECTION_CHANGE) {
              ArkUI_NodeComponentEvent *componentEvent = OH_ArkUI_NodeEvent_GetNodeComponentEvent(event);
              std::stringstream selectContent;
              selectContent << "start: " << componentEvent->data[0].i32 << " , end: " << componentEvent->data[1].i32;
              content = {.string = selectContent.str().c_str() };
          } else {
              return;
          }
          ArkUI_NodeHandle textNode = reinterpret_cast<ArkUI_NodeHandle>(OH_ArkUI_NodeEvent_GetUserData(event));
          if (textNode) {
              ArkUI_NativeNodeAPI_1 *nodeApi = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
                  OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
              nodeApi->setAttribute(textNode, NODE_TEXT_CONTENT, &content);
          }
      });
  }
  ```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/-Lox6giSTSCxDzhf145b2A/zh-cn_image_0000002736433051.gif)
