---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-embed-arkts-components
title: 嵌入ArkTS组件
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 嵌入ArkTS组件
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2cf0f37555987d2584fbd27014b3ce126daa60ebd798610bcd62159bfa798db3
---

ArkUI在Native侧提供的能力作为ArkTS的子集，部分能力不会在Native侧提供，如声明式UI语法，自定义struct组件，UI高级组件。

针对需要使用ArkTS侧独立能力的场景，ArkUI开发框架提供了Native侧嵌入ArkTS组件的能力，该能力依赖[ComponentContent](../harmonyos-references/js-apis-arkui-componentcontent.md)机制，通过ComponentContent完成对ArkTS组件的封装，然后将封装对象传递到Native侧，通过Native侧的[OH\_ArkUI\_GetNodeHandleFromNapiValue](../harmonyos-references/capi-native-node-napi-h.md#oh_arkui_getnodehandlefromnapivalue)接口转化为ArkUI\_NodeHandle对象用于Native侧组件挂载使用。

说明

* 通过OH\_ArkUI\_GetNodeHandleFromNapiValue接口获得的ArkUI\_NodeHandle对象只能作为子组件参数使用，如[addChild](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#addchild)接口的第二个参数，将该对象使用在其他场景下，如[setAttribute](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setattribute)设置属性将不生效并返回错误码。
* 针对Native侧修改ArkTS组件的场景，需要在Native侧通过Node-API方式构建ArkTS侧的更新数据，再通过ComponentContent的[update](../harmonyos-references/js-apis-arkui-componentcontent.md#update)接口更新。
* [构建自定义组件](ndk-build-custom-components.md)时，相关函数如measureNode等无法对ArkTS模块内部的组件进行调用。

以下示例代码在[接入ArkTS页面](ndk-access-the-arkts-page.md)章节基础上引入ArkTS的Refresh组件。

**图1** Refresh组件挂载文本列表

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/aG3v7p7UQcuQwtR5RrDmIA/zh-cn_image_0000002558604904.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052833Z&HW-CC-Expire=86400&HW-CC-Sign=F3CFAEDD72CDB7725F6A2B69319DB9FA9BDBCBF8C0AC846C5DB63405D98A3F80)

1. 注册ArkTS组件创建函数给Native侧，以便Native侧调用，创建函数使用ComponentContent能力进行封装。

   ```
   1. // 使用ComponentContent能力创建ArkTS组件

   3. import { NodeContent, UIContext, RefreshModifier, ComponentContent } from '@kit.ArkUI';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';

   6. const DOMAIN = 0x0000;

   8. // 定义Native侧和ArkTS进行交互的数据对象。
   9. interface NativeRefreshAttribute {
   10. isRefreshing: boolean;
   11. width?: number;
   12. height?: number;
   13. backgroundColor?: number;
   14. refreshOffset?: number;
   15. pullToRefresh?: boolean;
   16. onRefreshing?: () => void;
   17. onOffsetChange?: (offset: number) => void;
   18. }

   20. // 定义@Builder函数的入参格式。
   21. interface RefreshAttribute {
   22. isRefreshing: boolean;
   23. // 属性设置通过Modifier优化性能
   24. modifier?: RefreshModifier;
   25. slot?: NodeContent;
   26. onRefreshing?: () => void;
   27. onOffsetChange?: (offset: number) => void;
   28. }

   30. // ComponentContent封装ArkTS组件依赖全局@Builder函数，涉及复杂自定义组件场景，可以在@Builder函数中嵌套@Component自定义组件。
   31. // @Builder函数提供入参方式，方便后续通过ComponentContent的update接口进行参数更新。
   32. @Builder
   33. function mixedRefresh(attribute: RefreshAttribute) {
   34. Refresh({ refreshing: attribute.isRefreshing }) {
   35. // Refresh作为容器组件，需要使用ContentSlot机制预留子组件占位
   36. ContentSlot(attribute.slot);
   37. }.attributeModifier(attribute.modifier)
   38. .onRefreshing(() => {
   39. hilog.info(DOMAIN, 'testTag', 'on onRefreshing');
   40. if (attribute.onRefreshing) {
   41. hilog.info(DOMAIN, 'testTag', 'on native onRefreshing');
   42. attribute.onRefreshing();
   43. }
   44. })
   45. .onOffsetChange((value: number) => {
   46. hilog.info(DOMAIN, 'testTag', 'on offset change: ' + value);
   47. if (attribute.onOffsetChange) {
   48. hilog.info(DOMAIN, 'testTag', 'on native onOffsetChange');
   49. attribute.onOffsetChange(value);
   50. }
   51. });
   52. }

   54. // 定义创建函数的返回值，用于ArkTS侧和Native侧的交互。
   55. interface MixedModuleResult {
   56. // 定义针对Refresh构建函数的封装对象，用于Native侧转化为ArkUI_NodeHandle对象。
   57. content?: ComponentContent<RefreshAttribute>;
   58. // Refresh作为容器组件，需要使用ContentSlot机制挂载Native侧的子组件。
   59. childSlot?: NodeContent;
   60. }

   62. // 提供创建ArkTS组件的入口函数。
   63. export function createMixedRefresh(value: NativeRefreshAttribute): MixedModuleResult {
   64. hilog.info(DOMAIN, 'testTag', 'createMixedRefresh');
   65. // 通过AppStorage对象在Ability启动的时候保持UI上下文对象。
   66. let uiContent = AppStorage.get<UIContext>('context');
   67. let modifier = new RefreshModifier();
   68. if (value.width) {
   69. modifier.width(value.width);
   70. }
   71. if (value.height) {
   72. modifier.height(value.height);
   73. }
   74. if (value.backgroundColor) {
   75. modifier.backgroundColor(value.backgroundColor);
   76. }
   77. if (value.pullToRefresh) {
   78. modifier.pullToRefresh(value.pullToRefresh);
   79. }
   80. if (value.refreshOffset) {
   81. modifier.refreshOffset(value.refreshOffset);
   82. }
   83. // 创建NodeContent插槽对象用于Refresh子组件挂载。
   84. let nodeSlot = new NodeContent();
   85. // 通过ComponentContent创建Refresh组件并将它封装起来。
   86. let content = new ComponentContent<RefreshAttribute>(uiContent!, wrapBuilder<[RefreshAttribute]>(mixedRefresh),
   87. {
   88. isRefreshing: value.isRefreshing,
   89. modifier: modifier,
   90. slot: nodeSlot,
   91. onRefreshing: value.onRefreshing,
   92. onOffsetChange: value.onOffsetChange
   93. });
   94. // 将Refresh组件的封装对象及其子组件插槽对象传递给Native侧。
   95. return { content: content, childSlot: nodeSlot };
   96. }

   98. // 定义Refresh组件的更新函数，用于Native侧更新。
   99. // 在更新场景下，需要将Refresh组件的封装对象及其子组件插槽对象返回，防止组件重新创建。
   100. export function updateMixedRefresh(refresh: ComponentContent<RefreshAttribute>, childSlot: NodeContent,
   101. value: NativeRefreshAttribute): void {
   102. let modifier = new RefreshModifier();
   103. if (value.width) {
   104. modifier.width(value.width);
   105. }
   106. if (value.height) {
   107. modifier.height(value.height);
   108. }
   109. if (value.backgroundColor) {
   110. modifier.backgroundColor(value.backgroundColor);
   111. }
   112. if (value.pullToRefresh) {
   113. modifier.pullToRefresh(value.pullToRefresh);
   114. }
   115. if (value.refreshOffset) {
   116. modifier.refreshOffset(value.refreshOffset);
   117. }
   118. // 调用ComponentContent的update接口进行更新。
   119. refresh.update({
   120. isRefreshing: value.isRefreshing,
   121. modifier: modifier,
   122. slot: childSlot,
   123. onRefreshing: value.onRefreshing,
   124. onOffsetChange: value.onOffsetChange
   125. });
   126. }
   ```

   [MixedModule.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/ets/pages/MixedModule.ets#L15-L144)
2. 将创建和更新函数注册给Native侧。

   ```
   1. //  Index.ets
   2. import nativeNode from 'libentry.so';
   3. import { NodeContent } from '@kit.ArkUI';
   4. import { createMixedRefresh, updateMixedRefresh } from './MixedModule';

   6. @Entry
   7. @Component
   8. struct Index {
   9. private rootSlot = new NodeContent();
   10. @State @Watch('changeNativeFlag') showNative: boolean = false;

   12. aboutToAppear(): void {
   13. // 设置uiContext;
   14. AppStorage.setOrCreate<UIContext>('context', this.getUIContext());
   15. // 设置混合模式下的builder函数。
   16. nativeNode.registerCreateMixedRefreshNode(createMixedRefresh);
   17. nativeNode.registerUpdateMixedRefreshNode(updateMixedRefresh);
   18. }

   20. changeNativeFlag(): void {
   21. if (this.showNative) {
   22. // 创建NativeModule组件挂载
   23. nativeNode.createNativeRoot(this.rootSlot);
   24. } else {
   25. // 销毁NativeModule组件
   26. nativeNode.destroyNativeRoot();
   27. }
   28. }

   30. build() {
   31. Column() {
   32. Button(this.showNative ? 'HideNativeUI' : 'ShowNativeUI').onClick(() => {
   33. this.showNative = !this.showNative;
   34. });
   35. Row() {
   36. // ArkTS插入Native组件。
   37. ContentSlot(this.rootSlot);
   38. }.layoutWeight(1)
   39. .id('row_');
   40. }
   41. .width('100%')
   42. .height('100%');
   43. }
   44. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/ets/pages/Index.ets#L15-L61)

   ```
   1. // native_init.cpp
   2. #include "napi/native_api.h"
   3. #include "ArkUIMixedRefresh.h"
   4. #include "NativeEntry.h"

   6. EXTERN_C_START
   7. static napi_value Init(napi_env env, napi_value exports)
   8. {
   9. napi_property_descriptor desc[] = {
   10. {"createNativeRoot", nullptr, NativeModule::CreateNativeRoot, nullptr, nullptr, nullptr, napi_default, nullptr},
   11. {"registerCreateMixedRefreshNode", nullptr, NativeModule::ArkUIMixedRefresh::RegisterCreateRefresh, nullptr,
   12. nullptr, nullptr, napi_default, nullptr},
   13. {"registerUpdateMixedRefreshNode", nullptr, NativeModule::ArkUIMixedRefresh::RegisterUpdateRefresh, nullptr,
   14. nullptr, nullptr, napi_default, nullptr},
   15. {"destroyNativeRoot", nullptr, NativeModule::DestroyNativeRoot, nullptr, nullptr, nullptr, napi_default,
   16. nullptr}};
   17. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   18. return exports;
   19. }
   20. EXTERN_C_END

   22. static napi_module demoModule = {
   23. .nm_version = 1,
   24. .nm_flags = 0,
   25. .nm_filename = nullptr,
   26. .nm_register_func = Init,
   27. .nm_modname = "entry",
   28. .nm_priv = ((void *)0),
   29. .reserved = {0},
   30. };

   32. extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
   ```

   [NapiInit.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/cpp/NapiInit.cpp#L15-L48)
3. Native侧通过Node-API保存创建和更新函数，用于后续调用。

   ```
   1. // 混合模式交互类。

   3. #ifndef MYAPPLICATION_ARKUIMIXEDREFRESHTEMPLATE_H
   4. #define MYAPPLICATION_ARKUIMIXEDREFRESHTEMPLATE_H

   6. #include "ArkUIMixedNode.h"

   8. #include <optional>

   10. #include <arkui/native_node_napi.h>
   11. #include <js_native_api_types.h>

   13. namespace NativeModule {

   15. class ArkUIMixedRefresh : public ArkUIMixedNode {
   16. public:
   17. static napi_value RegisterCreateAndUpdateRefresh(napi_env env, napi_callback_info info);
   18. };

   20. } // namespace NativeModule

   22. #endif // MYAPPLICATION_ARKUIMIXEDREFRESHTEMPLATE_H
   ```

   [ArkUIMixedRefreshTemplate.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/cpp/ArkUIMixedRefreshTemplate.h#L15-L39)

   相关实现类说明：

   ```
   1. // 混合模式交互类。

   3. #include "ArkUIMixedRefreshTemplate.h"

   5. namespace NativeModule {
   6. namespace {
   7. napi_env g_env;
   8. napi_ref g_createRefresh;
   9. napi_ref g_updateRefresh;
   10. } // namespace

   12. napi_value ArkUIMixedRefresh::RegisterCreateAndUpdateRefresh(napi_env env, napi_callback_info info)
   13. {
   14. size_t argc = 1;
   15. napi_value args[1] = {nullptr};

   17. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   19. g_env = env;
   20. napi_ref refer;
   21. // 创建引用之后保存，防止释放。
   22. napi_create_reference(env, args[0], 1, &refer);

   24. g_createRefresh = refer;
   25. return nullptr;
   26. }

   28. } // namespace NativeModule
   ```

   [ArkUIMixedRefreshTemplate.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/cpp/ArkUIMixedRefreshTemplate.cpp#L15-L45)

   相关的CMakeLists的配置：

   ```
   1. # CMakeLists.txt

   3. # the minimum version of CMake.
   4. cmake_minimum_required(VERSION 3.4.1)
   5. project(testndk)

   7. # optional依赖C++17
   8. set(CMAKE_CXX_STANDARD 17)
   9. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

   11. include_directories(${NATIVERENDER_ROOT_PATH}
   12. ${NATIVERENDER_ROOT_PATH}/include)

   14. add_library(entry SHARED NativeEntry.cpp ArkUIMixedRefresh.cpp napi_init.cpp)
   15. # target_link_libraries(entry PUBLIC libace_napi.z.so, libace_ndk.z.so, libhilog_ndk.z.so)

   17. find_library(
   18. # Sets the name of the path variable.
   19. hilog-lib
   20. # Specifies the name of the NDK library that
   21. # you want CMake to locate.
   22. hilog_ndk.z
   23. )

   25. find_library(
   26. # Sets the name of the path variable.
   27. libace-lib
   28. # Specifies the name of the NDK library that
   29. # you want CMake to locate.
   30. ace_ndk.z
   31. )

   33. find_library(
   34. # Sets the name of the path variable.
   35. libnapi-lib
   36. # Specifies the name of the NDK library that
   37. # you want CMake to locate.
   38. ace_napi.z
   39. )

   41. find_library(
   42. # Sets the name of the path variable.
   43. libuv-lib
   44. uv
   45. )

   47. target_link_libraries(entry PUBLIC
   48. ${hilog-lib} ${libace-lib} ${libnapi-lib} ${libuv-lib} )
   ```
4. 抽象混合模式下组件的基类，用于通用逻辑管理。

   ```
   1. // ArkUIMixedNode.h
   2. // 混合模式基类。

   4. #ifndef MYAPPLICATION_ARKUIMIXEDNODE_H
   5. #define MYAPPLICATION_ARKUIMIXEDNODE_H

   7. #include <js_native_api.h>
   8. #include <js_native_api_types.h>

   10. #include "ArkUIBaseNode.h"
   11. #include "NativeModule.h"

   13. namespace NativeModule {

   15. // Wrap ArkTS Node
   16. class ArkUIMixedNode : public ArkUIBaseNode {
   17. public:
   18. ArkUIMixedNode(ArkUI_NodeHandle handle, napi_env env, napi_ref componentContent)
   19. : ArkUIBaseNode(handle), env_(env), componentContent_(componentContent) {}

   21. // 在基类析构的时候需要把混合模式在ArkTS侧的对象释放掉。
   22. ~ArkUIMixedNode() override { napi_delete_reference(env_, componentContent_); }

   24. protected:
   25. napi_env env_;
   26. napi_ref componentContent_;
   27. };

   29. } // namespace NativeModule

   31. #endif // MYAPPLICATION_ARKUIMIXEDNODE_H
   ```

   [ArkUIMixedNode.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/cpp/ArkUIMixedNode.h#L15-L47)
5. 实现Refresh组件的混合模式封装对象。

   ```
   1. // ArkUIMixedRefresh.h
   2. // Refresh混合模式在Native侧的封装对象。

   4. #ifndef MYAPPLICATION_ARKUIMIXEDREFRESH_H
   5. #define MYAPPLICATION_ARKUIMIXEDREFRESH_H

   7. #include "ArkUIMixedNode.h"
   8. #include "ArkUIBaseNode.h"

   10. #include <optional>

   12. #include <arkui/native_node_napi.h>
   13. #include <js_native_api_types.h>

   15. namespace NativeModule {

   17. // 定义Native侧和ArkTS侧的交互数据结构。
   18. struct NativeRefreshAttribute {
   19. std::optional<bool> isRefreshing;
   20. std::optional<float> width;
   21. std::optional<float> height;
   22. std::optional<uint32_t> backgroundColor;
   23. std::optional<float> refreshOffset;
   24. std::optional<bool> pullToRefresh;
   25. std::function<void()> onRefreshing;
   26. std::function<void(float)> onOffsetChange;
   27. };

   29. class ArkUIMixedRefresh : public ArkUIMixedNode {
   30. public:
   31. // 调用ArkTS的方法创建Refresh组件。
   32. static const std::shared_ptr<ArkUIMixedRefresh> Create(const NativeRefreshAttribute &attribute);

   34. ArkUIMixedRefresh(ArkUI_NodeHandle handle, ArkUI_NodeContentHandle contentHandle, napi_env env,
   35. napi_ref componentContent, napi_ref nodeContent)
   36. : ArkUIMixedNode(handle, env, componentContent), contentHandle_(contentHandle), nodeContent_(nodeContent) {}

   38. ArkUIMixedRefresh() : ArkUIMixedNode(nullptr, nullptr, nullptr) {}

   40. ~ArkUIMixedRefresh() override { napi_delete_reference(env_, nodeContent_); } // 释放子节点占位组件插槽对象。

   42. void SetWidth(float width) { attribute_.width = width; }

   44. void SetHeight(float height) { attribute_.height = height; }

   46. void SetBackgroundColor(uint32_t color) { attribute_.backgroundColor = color; }

   48. void SetRefreshState(bool isRefreshing) { attribute_.isRefreshing = isRefreshing; }

   50. void SetPullToRefresh(bool pullToRefresh) { attribute_.pullToRefresh = pullToRefresh; }

   52. void SetRefreshOffset(float offset) { attribute_.refreshOffset = offset; }

   54. void SetRefreshCallback(const std::function<void()> &callback) { attribute_.onRefreshing = callback; }

   56. void SetOnOffsetChange(const std::function<void(float)> &callback) { attribute_.onOffsetChange = callback; }

   58. // 避免频繁跨语言，在Native侧缓存属性事件，批量通知。
   59. void FlushMixedModeCmd();

   61. static napi_value RegisterCreateRefresh(napi_env env, napi_callback_info info);
   62. static napi_value RegisterUpdateRefresh(napi_env env, napi_callback_info info);

   64. protected:
   65. void OnAddChild(const std::shared_ptr<ArkUIBaseNode> &child) override
   66. {
   67. // 使用NodeContent挂载组件（可以使用ArkTS在Native侧通过ComponentContent的转化对象，也可以是纯Native组件）到ArkTS组件下面。
   68. OH_ArkUI_NodeContent_AddNode(contentHandle_, child->GetHandle());
   69. }

   71. void OnRemoveChild(const std::shared_ptr<ArkUIBaseNode> &child) override
   72. {
   73. // 使用NodeContent卸载组件。
   74. OH_ArkUI_NodeContent_RemoveNode(contentHandle_, child->GetHandle());
   75. }

   77. void OnInsertChild(const std::shared_ptr<ArkUIBaseNode> &child, int32_t index) override
   78. {
   79. // 使用NodeContent插入组件。
   80. OH_ArkUI_NodeContent_InsertNode(contentHandle_, child->GetHandle(), index);
   81. }

   83. private:
   84. // 使用napi接口创建ArkTS侧的数据结构。
   85. static napi_value CreateRefreshAttribute(const NativeRefreshAttribute &attribute, void *userData);

   87. static void Attribute2Descriptor(const NativeRefreshAttribute &attribute, napi_property_descriptor *desc);

   89. ArkUI_NodeContentHandle contentHandle_;
   90. napi_ref nodeContent_;
   91. NativeRefreshAttribute attribute_;
   92. };

   94. } // namespace NativeModule

   96. #endif // MYAPPLICATION_ARKUIMIXEDREFRESH_H
   ```

   [ArkUIMixedRefresh.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/cpp/ArkUIMixedRefresh.h#L15-L112)

   相关实现类说明：

   ```
   1. // ArkUIMixedRefresh.cpp

   3. #include "ArkUIMixedRefresh.h"
   4. #include <hilog/log.h>

   6. namespace NativeModule {
   7. namespace {
   8. napi_env g_env;
   9. napi_ref g_createRefresh;
   10. napi_ref g_updateRefresh;
   11. const int REFRESH_OFFSET_INDEX0 = 0;
   12. const int REFRESH_OFFSET_INDEX1 = 1;
   13. const int REFRESH_OFFSET_INDEX2 = 2;
   14. const int REFRESH_OFFSET_INDEX3 = 3;
   15. const int REFRESH_OFFSET_INDEX4 = 4;
   16. const int REFRESH_OFFSET_INDEX5 = 5;
   17. const int REFRESH_OFFSET_INDEX6 = 6;
   18. const int REFRESH_OFFSET_INDEX7 = 7;
   19. } // namespace

   21. void ArkUIMixedRefresh::Attribute2Descriptor(const NativeRefreshAttribute &attribute, napi_property_descriptor *desc)
   22. {
   23. if (attribute.width) {
   24. napi_value width;
   25. napi_create_double(g_env, attribute.width.value(), &width);
   26. desc[REFRESH_OFFSET_INDEX0].value = width;
   27. }
   28. if (attribute.height) {
   29. napi_value height;
   30. napi_create_double(g_env, attribute.height.value(), &height);
   31. desc[REFRESH_OFFSET_INDEX1].value = height;
   32. }
   33. if (attribute.backgroundColor) {
   34. napi_value backgroundColor;
   35. napi_create_uint32(g_env, attribute.backgroundColor.value(), &backgroundColor);
   36. desc[REFRESH_OFFSET_INDEX2].value = backgroundColor;
   37. }
   38. if (attribute.pullToRefresh) {
   39. napi_value pullToRefresh;
   40. napi_create_int32(g_env, attribute.pullToRefresh.value(), &pullToRefresh);
   41. desc[REFRESH_OFFSET_INDEX3].value = pullToRefresh;
   42. }
   43. if (attribute.isRefreshing) {
   44. napi_value isRefreshing;
   45. napi_create_int32(g_env, attribute.isRefreshing.value(), &isRefreshing);
   46. desc[REFRESH_OFFSET_INDEX4].value = isRefreshing;
   47. }
   48. if (attribute.refreshOffset) {
   49. napi_value refreshOffset;
   50. napi_create_double(g_env, attribute.refreshOffset.value(), &refreshOffset);
   51. desc[REFRESH_OFFSET_INDEX5].value = refreshOffset;
   52. }
   53. if (attribute.onRefreshing) {
   54. OH_LOG_INFO(LOG_APP, "onRefreshing start");
   55. desc[REFRESH_OFFSET_INDEX6].method = [](napi_env env, napi_callback_info info) -> napi_value {
   56. OH_LOG_INFO(LOG_APP, "onRefreshing callback");
   57. size_t argc = 0;
   58. napi_value args[0];
   59. void *data;
   60. napi_get_cb_info(env, info, &argc, args, nullptr, &data);
   61. auto refresh = reinterpret_cast<ArkUIMixedRefresh *>(data);
   62. if (refresh && refresh->attribute_.onRefreshing) {
   63. refresh->attribute_.onRefreshing();
   64. }
   65. return nullptr;
   66. };
   67. }
   68. }

   70. // 使用Napi接口创建与ArkTS侧交互的数据结构，用于Refresh组件的创建和更新。
   71. napi_value ArkUIMixedRefresh::CreateRefreshAttribute(const NativeRefreshAttribute &attribute, void *userData)
   72. {
   73. napi_property_descriptor desc[] = {
   74. {"width", nullptr, nullptr, nullptr, nullptr, nullptr, napi_default, userData},
   75. {"height", nullptr, nullptr, nullptr, nullptr, nullptr, napi_default, userData},
   76. {"backgroundColor", nullptr, nullptr, nullptr, nullptr, nullptr, napi_default, userData},
   77. {"pullToRefresh", nullptr, nullptr, nullptr, nullptr, nullptr, napi_default, userData},
   78. {"isRefreshing", nullptr, nullptr, nullptr, nullptr, nullptr, napi_default, userData},
   79. {"refreshOffset", nullptr, nullptr, nullptr, nullptr, nullptr, napi_default, userData},
   80. {"onRefreshing", nullptr, nullptr, nullptr, nullptr, nullptr, napi_default, userData},
   81. {"onOffsetChange", nullptr, nullptr, nullptr, nullptr, nullptr, napi_default, userData},
   82. };
   83. Attribute2Descriptor(attribute, desc);
   84. if (attribute.onOffsetChange) {
   85. OH_LOG_INFO(LOG_APP, "onOffsetChange start");
   86. desc[REFRESH_OFFSET_INDEX7].method = [](napi_env env, napi_callback_info info) -> napi_value {
   87. OH_LOG_INFO(LOG_APP, "onOffsetChange callback");
   88. size_t argc = 1;
   89. napi_value args[1] = {nullptr};
   90. void *data;
   91. napi_get_cb_info(env, info, &argc, args, nullptr, &data);
   92. double offset = 0.0;
   93. napi_get_value_double(env, args[0], &offset);
   94. auto refresh = reinterpret_cast<ArkUIMixedRefresh *>(data);
   95. if (refresh && refresh->attribute_.onOffsetChange) {
   96. refresh->attribute_.onOffsetChange(offset);
   97. }
   98. return nullptr;
   99. };
   100. }
   101. napi_value refreshAttribute = nullptr;
   102. auto result = napi_create_object_with_properties(g_env, &refreshAttribute, sizeof(desc) / sizeof(desc[0]), desc);
   103. if (result != napi_ok) {
   104. return nullptr;
   105. }
   106. return refreshAttribute;
   107. }

   109. // 创建ArkTS侧的组件并保存在Native侧的封装对象中。
   110. const std::shared_ptr<ArkUIMixedRefresh> ArkUIMixedRefresh::Create(const NativeRefreshAttribute &attribute)
   111. {
   112. napi_handle_scope scope;
   113. napi_open_handle_scope(g_env, &scope);
   114. auto refresh = std::make_shared<ArkUIMixedRefresh>();
   115. auto refreshAttribute = CreateRefreshAttribute(attribute, refresh.get());
   116. if (refreshAttribute == nullptr) {
   117. napi_close_handle_scope(g_env, scope);
   118. return nullptr;
   119. }
   120. napi_value result = nullptr;
   121. napi_value argv[1] = {refreshAttribute};
   122. napi_value createRefresh = nullptr;
   123. napi_get_reference_value(g_env, g_createRefresh, &createRefresh);
   124. // 调用ArkTS的Create函数创建ArkTS的ComponentContent。
   125. napi_call_function(g_env, nullptr, createRefresh, 1, argv, &result);

   127. // 获取ArkTS的Refresh组件。
   128. napi_value componentContent = nullptr;
   129. napi_get_named_property(g_env, result, "content", &componentContent);
   130. ArkUI_NodeHandle handle;
   131. OH_ArkUI_GetNodeHandleFromNapiValue(g_env, componentContent, &handle);
   132. // 获取ArkTS的Refresh组件的子组件插槽。
   133. napi_value nodeContent = nullptr;
   134. napi_get_named_property(g_env, result, "childSlot", &nodeContent);
   135. ArkUI_NodeContentHandle contentHandle;
   136. OH_ArkUI_GetNodeContentFromNapiValue(g_env, nodeContent, &contentHandle);
   137. // 保存ArkTS的ComponentContent用于防止ArkTS侧对象释放以及后续的更新。
   138. napi_ref componentContentRef;
   139. napi_create_reference(g_env, componentContent, 1, &componentContentRef);
   140. // 保存ArkTS的NodeContent用于防止ArkTS侧对象释放以及后续的更新。
   141. napi_ref nodeContentRef;
   142. napi_create_reference(g_env, nodeContent, 1, &nodeContentRef);
   143. // 更新Refresh组件相关参数。
   144. refresh->handle_ = handle;
   145. refresh->env_ = g_env;
   146. refresh->componentContent_ = componentContentRef;
   147. refresh->nodeContent_ = nodeContentRef;
   148. refresh->contentHandle_ = contentHandle;
   149. refresh->attribute_ = attribute;
   150. return refresh;
   151. }
   152. // 更新函数实现。
   153. void ArkUIMixedRefresh::FlushMixedModeCmd()
   154. {
   155. napi_handle_scope scope;
   156. napi_open_handle_scope(g_env, &scope);
   157. // 创建调用ArkTS接口入参。
   158. auto refreshAttribute = CreateRefreshAttribute(attribute_, this);
   159. if (refreshAttribute == nullptr) {
   160. napi_close_handle_scope(g_env, scope);
   161. return;
   162. }
   163. // 获取更新接口的剩余两个接口参数。
   164. napi_value componentContent = nullptr;
   165. napi_get_reference_value(g_env, componentContent_, &componentContent);
   166. napi_value nodeContent = nullptr;
   167. napi_get_reference_value(g_env, nodeContent_, &nodeContent);

   169. napi_value argv[3] = {componentContent, nodeContent, refreshAttribute};
   170. napi_value updateRefresh = nullptr;
   171. napi_get_reference_value(g_env, g_updateRefresh, &updateRefresh);
   172. // 调用ArkTS的Update函数进行更新。
   173. napi_value result = nullptr;
   174. napi_call_function(g_env, nullptr, updateRefresh, sizeof(argv) / sizeof(argv[0]), argv, &result);
   175. }

   177. napi_value ArkUIMixedRefresh::RegisterCreateRefresh(napi_env env, napi_callback_info info)
   178. {
   179. size_t argc = 1;
   180. napi_value args[1] = {nullptr};

   182. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   184. g_env = env;
   185. napi_ref refer;
   186. napi_create_reference(env, args[0], 1, &refer);

   188. g_createRefresh = refer;
   189. return nullptr;
   190. }

   192. napi_value ArkUIMixedRefresh::RegisterUpdateRefresh(napi_env env, napi_callback_info info)
   193. {
   194. size_t argc = 1;
   195. napi_value args[1] = {nullptr};

   197. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   199. g_env = env;
   200. napi_ref refer;
   201. napi_create_reference(env, args[0], 1, &refer);

   203. g_updateRefresh = refer;
   204. return nullptr;
   205. }

   207. } // namespace NativeModule
   ```

   [ArkUIMixedRefresh.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/cpp/ArkUIMixedRefresh.cpp#L15-L223)
6. 定时器模块相关简单实现。

   ```
   1. // UITimer.h
   2. // 定时器模块。

   4. #ifndef MYAPPLICATION_UITIMER_H
   5. #define MYAPPLICATION_UITIMER_H

   7. #include <hilog/log.h>
   8. #include <js_native_api.h>
   9. #include <js_native_api_types.h>
   10. #include <node_api.h>
   11. #include <node_api_types.h>
   12. #include <string>
   13. #include <thread>
   14. #include <uv.h>

   16. namespace NativeModule {

   18. struct UIData {
   19. void *userData = nullptr;
   20. int32_t count = 0;
   21. int32_t totalCount = 0;
   22. void (*func)(void *userData, int32_t count) = nullptr;
   23. };

   25. napi_threadsafe_function threadSafeFunction = nullptr;

   27. void CreateNativeTimer(napi_env env, void *userData, int32_t totalCount, void (*func)(void *userData, int32_t count))
   28. {
   29. napi_value name;
   30. std::string str = "UICallback";
   31. napi_create_string_utf8(env, str.c_str(), str.size(), &name);
   32. // UI主线程回调函数。
   33. napi_create_threadsafe_function(
   34. env, nullptr, nullptr, name, 0, 1, nullptr, nullptr, nullptr,
   35. [](napi_env env, napi_value value, void *context, void *data) {
   36. auto userdata = reinterpret_cast<UIData *>(data);
   37. userdata->func(userdata->userData, userdata->count);
   38. delete userdata;
   39. },
   40. &threadSafeFunction);
   41. // 启动定时器，模拟数据变化。
   42. std::thread timerThread([data = userData, totalCount, func]() {
   43. uv_loop_t *loop = uv_loop_new();
   44. uv_timer_t *timer = new uv_timer_t();
   45. uv_timer_init(loop, timer);
   46. timer->data = new UIData{data, 0, totalCount, func};
   47. uint64_t timeout = 4000;
   48. uint64_t repeat = 4000;
   49. uv_timer_start(
   50. timer,
   51. [](uv_timer_t *handle) {
   52. OH_LOG_INFO(LOG_APP, "on timeout");
   53. napi_acquire_threadsafe_function(threadSafeFunction);
   54. auto *customData = reinterpret_cast<UIData *>(handle->data);
   55. // 创建回调数据。
   56. auto *callbackData =
   57. new UIData{customData->userData, customData->count, customData->totalCount, customData->func};
   58. napi_call_threadsafe_function(threadSafeFunction, callbackData, napi_tsfn_blocking);
   59. customData->count++;
   60. if (customData->count > customData->totalCount) {
   61. uv_timer_stop(handle);
   62. delete handle;
   63. delete customData;
   64. }
   65. },
   66. timeout, repeat);
   67. uv_run(loop, UV_RUN_DEFAULT);
   68. uv_loop_delete(loop);
   69. });
   70. timerThread.detach();
   71. }
   72. } // namespace NativeModule

   74. #endif // MYAPPLICATION_UITIMER_H
   ```

   [UITimer.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/cpp/UITimer.h#L15-L90)
7. 使用[接入ArkTS页面](ndk-access-the-arkts-page.md)章节的页面结构，将Refresh组件作为文本列表的父组件。

   ```
   1. // MixedRefreshExample.h
   2. // 混合模式示例代码。

   4. #ifndef MYAPPLICATION_MIXEDREFRESHEXAMPLE_H
   5. #define MYAPPLICATION_MIXEDREFRESHEXAMPLE_H

   7. #include "ArkUIBaseNode.h"
   8. #include "ArkUIMixedRefresh.h"
   9. #include "NormalTextListExample.h"
   10. #include "UITimer.h"

   12. #include <js_native_api_types.h>

   14. namespace NativeModule {

   16. std::shared_ptr<ArkUIBaseNode> CreateMixedRefreshList(napi_env env)
   17. {
   18. auto list = CreateTextListExample();
   19. // 混合模式创建Refresh组件并挂载List组件。
   20. NativeRefreshAttribute nativeRefreshAttribute{
   21. .backgroundColor = 0xFF89CFF0, .refreshOffset = 64, .pullToRefresh = true};
   22. auto refresh = ArkUIMixedRefresh::Create(nativeRefreshAttribute);
   23. refresh->AddChild(list);

   25. // 设置混合模式下的事件。
   26. refresh->SetOnOffsetChange(
   27. [](float offset) { OH_LOG_INFO(LOG_APP, "on refresh offset changed: %{public}f", offset); });
   28. refresh->SetRefreshCallback([refreshPtr = refresh.get(), env]() {
   29. OH_LOG_INFO(LOG_APP, "on refreshing");
   30. // 启动定时器，模拟数据获取。
   31. CreateNativeTimer(env, refreshPtr, 1, [](void *userData, int32_t count) {
   32. // 数据获取后关闭刷新。
   33. auto refresh = reinterpret_cast<ArkUIMixedRefresh *>(userData);
   34. refresh->SetRefreshState(false);
   35. refresh->FlushMixedModeCmd();
   36. });
   37. });

   39. // 更新事件到ArkTS侧。
   40. refresh->FlushMixedModeCmd();
   41. return refresh;
   42. }

   44. } // namespace NativeModule

   46. #endif // MYAPPLICATION_MIXEDREFRESHEXAMPLE_H
   ```

   [MixedRefreshExample.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/cpp/MixedRefreshExample.h#L15-L62)

   替换入口组件创建为下拉刷新文本列表。

   ```
   1. // NativeEntry.cpp

   3. #include "NativeEntry.h"

   5. #include "ArkUIMixedRefresh.h"
   6. #include "MixedRefreshExample.h"
   7. #include "NormalTextListExample.h"

   9. #include <arkui/native_node_napi.h>
   10. #include <arkui/native_type.h>
   11. #include <js_native_api.h>
   12. #include <uv.h>

   14. namespace NativeModule {

   16. napi_value CreateNativeRoot(napi_env env, napi_callback_info info)
   17. {
   18. size_t argc = 1;
   19. napi_value args[1] = {nullptr};

   21. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   23. // 获取NodeContent
   24. ArkUI_NodeContentHandle contentHandle;
   25. OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &contentHandle);
   26. NativeEntry::GetInstance()->SetContentHandle(contentHandle);

   28. // 创建Refresh文本列表
   29. auto refresh = CreateMixedRefreshList(env);

   31. // 保持Native侧对象到管理类中，维护生命周期。
   32. NativeEntry::GetInstance()->SetRootNode(refresh);
   33. return nullptr;
   34. }

   36. napi_value DestroyNativeRoot(napi_env env, napi_callback_info info)
   37. {
   38. // 从管理类中释放Native侧对象。
   39. NativeEntry::GetInstance()->DisposeRootNode();
   40. return nullptr;
   41. }

   43. } // namespace NativeModule
   ```

   [NativeEntry.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/cpp/NativeEntry.cpp#L15-L59)
8. 在Native侧提供Node-API的桥接方法，实现ArkTS侧的NativeNode模块接口。

   ```
   1. export const createNativeRoot: (content: Object) => void;
   2. export const destroyNativeRoot: () => void;

   4. export const registerCreateMixedRefreshNode: (content: Object) => void;
   5. export const registerUpdateMixedRefreshNode: (content: Object) => void;
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/cpp/types/libentry/Index.d.ts#L15-L21)
