---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-embedded-component
title: 通过EmbeddedComponent拉起EmbeddedUIExtensionAbility
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 通过EmbeddedComponent拉起EmbeddedUIExtensionAbility
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8a69338e1530641bec7430fd9f14287742c03b13e9edba6566981a74f4e924f0
---

ArkUI在Native侧提供的能力是ArkTS的子集，某些能力不会在Native侧提供，例如声明式UI语法、自定义struct组件及UI系统预置UI组件库。

从API version 20开始，ArkUI开发框架提供了Native侧嵌入EmbeddedComponent组件的能力，此能力依赖于[EmbeddedComponent](../harmonyos-references/ts-container-embedded-component.md)机制。EmbeddedComponent用于支持在当前页面嵌入同一应用内其他[EmbeddedUIExtensionAbility](../harmonyos-references/js-apis-app-ability-embeddeduiextensionability.md)提供的UI。EmbeddedUIExtensionAbility在独立进程中运行，负责页面布局和渲染。此功能主要用于有进程隔离需求的模块化开发场景。

**说明** 

* 使用[OH\_ArkUI\_EmbeddedComponentOption\_Create](../harmonyos-references/capi-embedded-component-h.md#oh_arkui_embeddedcomponentoption_create)获取[ArkUI\_EmbeddedComponentOption](../harmonyos-references/capi-arkui-nativemodule-arkui-embeddedcomponentoption.md)后，可以使用[OH\_ArkUI\_EmbeddedComponentOption\_SetOnError](../harmonyos-references/capi-embedded-component-h.md#oh_arkui_embeddedcomponentoption_setonerror)设置onError回调，使用[OH\_ArkUI\_EmbeddedComponentOption\_SetOnTerminated](../harmonyos-references/capi-embedded-component-h.md#oh_arkui_embeddedcomponentoption_setonterminated)设置onTerminated回调。可以使用[OH\_ArkUI\_NodeUtils\_MoveTo](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_moveto)迁移节点。
* 使用[OH\_ArkUI\_EmbeddedComponentOption\_SetOnTerminated](../harmonyos-references/capi-embedded-component-h.md#oh_arkui_embeddedcomponentoption_setonterminated)设置onTerminated回调时，返回的want参数只支持解析提供方返回的key-value，不支持嵌套解析。
* 在EmbeddedComponentOption属性设置完成后，调用[OH\_ArkUI\_EmbeddedComponentOption\_Dispose](../harmonyos-references/capi-embedded-component-h.md#oh_arkui_embeddedcomponentoption_dispose)释放内存，避免内存泄漏。
* EmbeddedComponent组件需要使用[setAttribute](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setattribute)设置宽高才能显示。

本示例展示EmbeddedComponent组件NDK的基础使用方式，ability相关使用请参考[EmbeddedComponent](../harmonyos-references/ts-container-embedded-component.md)。示例应用的bundleName为"com.example.uiextensionandaccessibility"，同一应用下被拉起的EmbeddedUIExtensionAbility为"ExampleEmbeddedAbility"。本示例仅支持在具有多进程权限的设备上运行，例如PC/2in1。

```
#include <arkui/native_node.h>
#include <arkui/native_type.h>
#include <AbilityKit/ability_base/want.h> //引用元能力want头文件

// 注册事件
void onError(int32_t code, const char *name, const char *message) {}
void onTerminated(int32_t code, AbilityBase_Want *want) {}
const unsigned int LOG_PRINT_DOMAIN = 0xFF00;
#define SIZE_300 300 // 节点的宽/高数值，单位 vp（用于设置 NODE_WIDTH/NODE_HEIGHT）
#define PARAMETER_ERROR_CODE 401 // 参数错误码（OH_ArkUI_NodeContent_AddNode 返回值表示入参非法）
// ...
    // 创建节点
    ArkUI_NodeHandle embeddedNode = nodeAPI->createNode(ARKUI_NODE_EMBEDDED_COMPONENT);
    // 设置属性
    AbilityBase_Element Element = {.bundleName = "com.example.uiextensionandaccessibility",
                                   .abilityName = "ExampleEmbeddedAbility",
                                   .moduleName = "entry"};       // 由元能力提供接口
    AbilityBase_Want *want = OH_AbilityBase_CreateWant(Element); // 由元能力提供接口
    if (want == nullptr) {
        OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "AbilityBase_Want", "CreateWant failed");
        return nullptr;
    }
    ArkUI_AttributeItem itemobjwant = {.object = want};
    nodeAPI->setAttribute(embeddedNode, NODE_EMBEDDED_COMPONENT_WANT, &itemobjwant);

    auto embeddedNode_option = OH_ArkUI_EmbeddedComponentOption_Create();
    auto onErrorCallback = onError;
    auto onTerminatedCallback = onTerminated;
    OH_ArkUI_EmbeddedComponentOption_SetOnError(embeddedNode_option, onErrorCallback);
    OH_ArkUI_EmbeddedComponentOption_SetOnTerminated(embeddedNode_option, onTerminatedCallback);

    ArkUI_AttributeItem itemobjembeddedNode = {.object = embeddedNode_option};
    nodeAPI->setAttribute(embeddedNode, NODE_EMBEDDED_COMPONENT_OPTION, &itemobjembeddedNode);
    // 属性设置完成后释放 embeddedNode_option 资源，避免内存泄漏
    OH_ArkUI_EmbeddedComponentOption_Dispose(embeddedNode_option);

    // 设置基本属性，如宽高
    ArkUI_NumberValue value[] = {{.f32 = SIZE_300}};
    ArkUI_AttributeItem item = {value, sizeof(value) / sizeof(ArkUI_NumberValue)};
    nodeAPI->setAttribute(embeddedNode, NODE_WIDTH, &item);
    nodeAPI->setAttribute(embeddedNode, NODE_HEIGHT, &item);

    // 创建Column
    ArkUI_NodeHandle column = nodeAPI->createNode(ARKUI_NODE_COLUMN);
    nodeAPI->setAttribute(column, NODE_WIDTH, &item);
    ArkUI_NumberValue column_bc[] = {{.u32 = 0xFFFF00BB}};
    ArkUI_AttributeItem column_item = {column_bc, 1};
    nodeAPI->setAttribute(column, NODE_BACKGROUND_COLOR, &column_item);
    ArkUI_AttributeItem column_id = {.string = "Column_CAPI"};
    nodeAPI->setAttribute(column, NODE_ID, &column_id);

    // 上树
    nodeAPI->addChild(column, embeddedNode);
```
