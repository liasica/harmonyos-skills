---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-access-the-arkts-page
title: 接入ArkTS页面
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 接入ArkTS页面
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:957f7aef209dffc7e5958fa8580ada56a0c62cb76908edb0ba75165a13135b9e
---

## 占位组件

使用NDK接口构建UI界面时，需要在ArkTS页面创建用于挂载NDK接口创建组件的占位组件。占位组件类型为[ContentSlot](../harmonyos-references/ts-components-contentslot.md)，ContentSlot能够绑定一个[NodeContent](../harmonyos-references/js-apis-arkui-nodecontent.md)对象，该对象可通过Node-API传递到Native侧挂载显示Native组件。

* NDK配置文件entry/src/main/cpp/types/libentry/oh-package.json5如下。

  ```
  1. {
  2. "name": "libentry.so",
  3. "types": "./Index.d.ts",
  4. "version": "1.0.0",
  5. "description": "Please describe the basic information."
  6. }
  ```

  [oh-package.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonList/entry/src/main/cpp/types/libentry/oh-package.json5#L16-L23)
* 占位组件和其他ArkTS系统组件使用方法相同。详细代码请参考[示例](ndk-access-the-arkts-page.md#示例)。

  ```
  1. import nativeNode from 'libentry.so';
  2. import { NodeContent } from '@kit.ArkUI';

  4. @Entry
  5. @Component
  6. struct Index {
  7. // 初始化NodeContent对象。
  8. private rootSlot:NodeContent = new NodeContent();
  9. @State @Watch('changeNativeFlag') showNative: boolean = false;

  11. changeNativeFlag(): void {
  12. if (this.showNative) {
  13. // 传递NodeContent对象用于Native创建组件的挂载显示
  14. nativeNode.createNativeRoot(this.rootSlot)
  15. } else {
  16. // 销毁NativeModule组件
  17. nativeNode.destroyNativeRoot()
  18. }
  19. }

  21. build() {
  22. Column() {
  23. Button(this.showNative ? 'HideNativeUI' : 'ShowNativeUI')
  24. .onClick(() => {
  25. this.showNative = !this.showNative
  26. })
  27. .id('btn')
  28. Row() {
  29. // 将NodeContent和ContentSlot占位组件绑定
  30. ContentSlot(this.rootSlot)
  31. }.layoutWeight(1)
  32. }
  33. .width('100%')
  34. .height('100%')
  35. }
  36. }
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonList/entry/src/main/ets/pages/Index.ets#L16-L53)
* 占位组件可以通过相关接口在Native侧转化为挂载对象。

  ```
  1. ArkUI_NodeContentHandle contentHandle;
  2. OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &contentHandle);
  ```
* 挂载对象提供了相关挂载和卸载组件接口。

  ```
  1. OH_ArkUI_NodeContent_AddNode(handle_, myNativeNode);
  2. OH_ArkUI_NodeContent_RemoveNode(handle_, myNativeNode);
  ```

## NDK组件模块

NDK提供的UI组件能力如组件创建、树操作、属性设置、事件注册等是通过函数指针结构体（如[ArkUI\_NativeNodeAPI\_1](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md)）进行暴露，该函数指针结构体可以通过[模块查询接口](../harmonyos-references/capi-native-interface-h.md#oh_arkui_getmoduleinterface)获取。

说明

* [模块查询接口](../harmonyos-references/capi-native-interface-h.md#oh_arkui_getmoduleinterface)带有初始化NDK的逻辑，建议先调用该接口进行全局初始化，再使用NDK进行UI构造。

```
1. ArkUI_NativeNodeAPI_1* arkUINativeNodeApi = nullptr;
2. OH_ArkUI_GetModuleInterface(ARKUI_NATIVE_NODE, ArkUI_NativeNodeAPI_1, arkUINativeNodeApi);
```

在获取到函数指针结构体后，可以使用该结构体内的函数实现相关UI组件操作。

* 组件创建和销毁。

  ```
  1. auto listNode = arkUINativeNodeApi->createNode(ARKUI_NODE_LIST);
  2. arkUINativeNodeApi->disposeNode(listNode);
  ```

  获取NDK接口支持的组件范围可以通过查询[ArkUI\_NodeType](../harmonyos-references/capi-native-node-h.md#arkui_nodetype)枚举值。
* 组件树操作。

  ```
  1. auto parent = arkUINativeNodeApi->createNode(ARKUI_NODE_STACK);
  2. auto child = arkUINativeNodeApi->createNode(ARKUI_NODE_STACK);
  3. arkUINativeNodeApi->addChild(parent, child);
  4. arkUINativeNodeApi->removeChild(parent, child);
  ```
* 属性设置。

  ```
  1. auto stack = arkUINativeNodeApi->createNode(ARKUI_NODE_STACK);
  2. ArkUI_NumberValue value[] = {{.f32 = 100}};
  3. ArkUI_AttributeItem item = {value, 1};
  4. arkUINativeNodeApi->setAttribute(stack, NODE_WIDTH, &item);
  5. ArkUI_NumberValue value_color[] = {{.u32 = 0xff112233}};
  6. ArkUI_AttributeItem item_color = {value_color, 1};
  7. arkUINativeNodeApi->setAttribute(stack, NODE_BACKGROUND_COLOR, &item);
  ```

  获取NDK接口支持的属性范围可以通过查询[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)枚举值。
* 事件注册。

  ```
  1. auto stack = arkUINativeNodeApi->createNode(ARKUI_NODE_STACK);
  2. arkUINativeNodeApi->addNodeEventReceiver(stack, [](ArkUI_NodeEvent* event){
  3. // process event
  4. });
  5. arkUINativeNodeApi->registerNodeEvent(stack, NODE_ON_CLICK, 0, nullptr);
  ```

  获取NDK接口支持的事件范围可以通过查询[ArkUI\_NodeEventType](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)枚举值。

## 示例

下面的示例展示了如何使用ContentSlot挂载Native侧的文本列表。

示例代码的目录结构及其文件说明如下：

```
1. .
2. |——cpp
3. |    |——types
4. |    |      |——libentry
5. |    |      |       |——index.d.ts 提供Native和ArkTS侧的桥接方法。
6. |    |——napi_init.cpp 与index.d.ts对应的桥接方法对接Native侧的定义处。
7. |    |——NativeEntry.cpp 桥接方法的Native侧实现。
8. |    |——NativeEntry.h 桥接方法的Native侧定义。
9. |    |——NativeModule.h 提供获取ArkUI在Native侧模块的封装接口。
10. |    |——CMakeLists.txt C语言库引用文件。
11. |    |——ArkUIBaseNode.h 节点封装扩展类。
12. |    |——ArkUINode.h 节点封装扩展类。
13. |    |——ArkUIListNode.h 节点封装扩展类。
14. |    |——ArkUIListItemNode.h 节点封装扩展类。
15. |    |——ArkUITextNode.h 节点封装扩展类。
16. |    |——NormalTextListExample.h 示例代码文件。
17. |
18. |——ets
19. |    |——pages
20. |         |——entry.ets 应用启动页，加载承载Native的容器。
21. |
```

**图1** Native文本列表

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/qn6LYYTIRf2BtoLKta1JHA/zh-cn_image_0000002583438107.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234012Z&HW-CC-Expire=86400&HW-CC-Sign=C08CE82522B7E3C0F730025640B91C848D72F774C179DE18C52354545897D89A)

1. 在ArkTS页面上声明用于Native页面挂载的占位组件，并在页面创建时通知Native侧创建文本列表。

   ```
   1. import nativeNode from 'libentry.so';
   2. import { NodeContent } from '@kit.ArkUI';

   4. @Entry
   5. @Component
   6. struct Index {
   7. // 初始化NodeContent对象。
   8. private rootSlot:NodeContent = new NodeContent();
   9. @State @Watch('changeNativeFlag') showNative: boolean = false;

   11. changeNativeFlag(): void {
   12. if (this.showNative) {
   13. // 传递NodeContent对象用于Native创建组件的挂载显示
   14. nativeNode.createNativeRoot(this.rootSlot)
   15. } else {
   16. // 销毁NativeModule组件
   17. nativeNode.destroyNativeRoot()
   18. }
   19. }

   21. build() {
   22. Column() {
   23. Button(this.showNative ? 'HideNativeUI' : 'ShowNativeUI')
   24. .onClick(() => {
   25. this.showNative = !this.showNative
   26. })
   27. .id('btn')
   28. Row() {
   29. // 将NodeContent和ContentSlot占位组件绑定
   30. ContentSlot(this.rootSlot)
   31. }.layoutWeight(1)
   32. }
   33. .width('100%')
   34. .height('100%')
   35. }
   36. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonList/entry/src/main/ets/pages/Index.ets#L16-L53)
2. 使用Native模板创建工程，并在Native侧提供Node-API的桥接方法，实现ArkTS侧的NativeNode模块接口。

   接口声明。

   ```
   1. // entry/src/main/cpp/types/libentry/Index.d.ts
   2. export const createNativeRoot: (content: Object) => void;
   3. export const destroyNativeRoot: () => void;
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonList/entry/src/main/cpp/types/libentry/Index.d.ts#L15-L19)

   Native实现。

   ```
   1. // entry/src/main/cpp/napi_init.cpp
   2. #include "napi/native_api.h"
   3. #include "NativeEntry.h"

   5. EXTERN_C_START
   6. static napi_value Init(napi_env env, napi_value exports)
   7. {
   8. // 绑定Native侧的创建组件和销毁组件。
   9. napi_property_descriptor desc[] = {
   10. {"createNativeRoot", nullptr,
   11. NativeModule::CreateNativeRoot, nullptr, nullptr,
   12. nullptr, napi_default, nullptr},
   13. {"destroyNativeRoot", nullptr,
   14. NativeModule::DestroyNativeRoot, nullptr, nullptr,
   15. nullptr, napi_default, nullptr}};
   16. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   17. return exports;
   18. }
   19. EXTERN_C_END

   21. static napi_module demoModule = {
   22. .nm_version = 1,
   23. .nm_flags = 0,
   24. .nm_filename = nullptr,
   25. .nm_register_func = Init,
   26. .nm_modname = "entry",
   27. .nm_priv = ((void *)0),
   28. .reserved = {0},
   29. };

   31. extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonList/entry/src/main/cpp/napi_init.cpp#L15-L47)
3. 在NativeEntry.h文件中创建Native界面。

   ```
   1. // NativeEntry.h

   3. #ifndef MYAPPLICATION_NATIVEENTRY_H
   4. #define MYAPPLICATION_NATIVEENTRY_H

   6. #include <ArkUIBaseNode.h>
   7. #include <arkui/native_type.h>
   8. #include <js_native_api_types.h>

   10. namespace NativeModule {

   12. napi_value CreateNativeRoot(napi_env env, napi_callback_info info);

   14. napi_value DestroyNativeRoot(napi_env env, napi_callback_info info);

   16. // 管理Native组件的生命周期和内存。
   17. class NativeEntry {
   18. public:
   19. static NativeEntry *GetInstance()
   20. {
   21. static NativeEntry nativeEntry;
   22. return &nativeEntry;
   23. }

   25. void SetContentHandle(ArkUI_NodeContentHandle handle)
   26. {
   27. handle_ = handle;
   28. }

   30. void SetRootNode(const std::shared_ptr<ArkUIBaseNode> &baseNode)
   31. {
   32. root_ = baseNode;
   33. // 添加Native组件到NodeContent上用于挂载显示。
   34. OH_ArkUI_NodeContent_AddNode(handle_, root_->GetHandle());
   35. }
   36. void DisposeRootNode()
   37. {
   38. // 从NodeContent上卸载组件并销毁Native组件。
   39. OH_ArkUI_NodeContent_RemoveNode(handle_, root_->GetHandle());
   40. root_.reset();
   41. }

   43. private:
   44. std::shared_ptr<ArkUIBaseNode> root_;
   45. ArkUI_NodeContentHandle handle_;
   46. };

   48. } // namespace NativeModule

   50. #endif  // MYAPPLICATION_NATIVEENTRY_H
   ```

   [NativeEntry.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonList/entry/src/main/cpp/NativeEntry.h#L15-L66)

   对应实现文件。

   ```
   1. // NativeEntry.cpp

   3. #include <arkui/native_node_napi.h>
   4. #include <js_native_api.h>
   5. #include "NativeEntry.h"
   6. #include "NormalTextListExample.h"

   8. namespace NativeModule {

   10. napi_value CreateNativeRoot(napi_env env, napi_callback_info info)
   11. {
   12. size_t argc = 1;
   13. napi_value args[1] = {nullptr};

   15. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   17. // 获取NodeContent
   18. ArkUI_NodeContentHandle contentHandle;
   19. OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &contentHandle);
   20. NativeEntry::GetInstance()->SetContentHandle(contentHandle);

   22. // 创建文本列表
   23. auto list = CreateTextListExample();

   25. // 保持Native侧对象到管理类中，维护生命周期。
   26. NativeEntry::GetInstance()->SetRootNode(list);
   27. return nullptr;
   28. }

   30. napi_value DestroyNativeRoot(napi_env env, napi_callback_info info)
   31. {
   32. // 从管理类中释放Native侧对象。
   33. NativeEntry::GetInstance()->DisposeRootNode();
   34. return nullptr;
   35. }
   36. } // namespace NativeModule
   ```

   [NativeEntry.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonList/entry/src/main/cpp/NativeEntry.cpp#L15-L52)

   使用NDK提供的C接口需要在CMakeLists.txt中增加libace\_ndk.z.so的引用，如下所示。其中entry为工程导出的动态库名称，如当前示例使用的是默认的名称libentry.so。新增cpp文件后，同样需要在CMakeLists.txt中添加相应的cpp文件。若未进行此配置，对应的文件将不会被编译。

   ```
   1. add_library(entry SHARED napi_init.cpp NativeEntry.cpp)
   2. target_link_libraries(entry PUBLIC libace_napi.z.so libace_ndk.z.so)
   ```
4. 由于NDK接口提供的是C接口，为了使用面向对象的方式简化编程和工程管理，这里建议使用C++进行二次封装，下面示例代码展示了示例界面中所需的列表，文本组件封装类。

   1）获取ArkUI在NDK接口的入口模块[ArkUI\_NativeNodeAPI\_1](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md)，该结构体模块提供了一系列组件创建、树构建、属性设置和事件注册等函数指针。

   ```
   1. // NativeModule.h
   2. // 提供获取ArkUI在Native侧模块的封装接口

   4. #ifndef MYAPPLICATION_NATIVEMODULE_H
   5. #define MYAPPLICATION_NATIVEMODULE_H

   7. #include <arkui/native_node.h>
   8. #include <cassert>

   10. #include <arkui/native_interface.h>

   12. namespace NativeModule {

   14. class NativeModuleInstance {
   15. public:
   16. static NativeModuleInstance *GetInstance()
   17. {
   18. static NativeModuleInstance instance;
   19. return &instance;
   20. }
   21. NativeModuleInstance()
   22. {
   23. OH_ArkUI_GetModuleInterface(ARKUI_NATIVE_NODE, ArkUI_NativeNodeAPI_1, arkUINativeNodeApi_);
   24. }
   25. // 暴露给其他模块使用。
   26. ArkUI_NativeNodeAPI_1 *GetNativeNodeAPI() { return arkUINativeNodeApi_; }

   28. private:
   29. ArkUI_NativeNodeAPI_1 *arkUINativeNodeApi_ = nullptr;
   30. };

   32. } // namespace NativeModule

   34. #endif // MYAPPLICATION_NATIVEMODULE_H
   ```

   [NativeModule.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonList/entry/src/main/cpp/NativeModule.h#L15-L50)

   2）提供列表，文本组件的基类对象，用于封装通用属性和事件。

   ```
   1. // ArkUIBaseNode.h
   2. // 提供组件树操作的基类。
   3. #ifndef MYAPPLICATION_ARKUIBASENODE_H
   4. #define MYAPPLICATION_ARKUIBASENODE_H

   6. #include <arkui/native_type.h>
   7. #include <list>
   8. #include <memory>

   10. #include "NativeModule.h"

   12. namespace NativeModule {

   14. class ArkUIBaseNode {
   15. public:
   16. explicit ArkUIBaseNode(ArkUI_NodeHandle handle)
   17. : handle_(handle), nativeModule_(NativeModuleInstance::GetInstance()->GetNativeNodeAPI()) {}

   19. virtual ~ArkUIBaseNode()
   20. {
   21. // 封装析构函数，实现子节点移除功能。
   22. if (!children_.empty()) {
   23. for (const auto& child : children_) {
   24. nativeModule_->removeChild(handle_, child->GetHandle());
   25. }
   26. children_.clear();
   27. }
   28. // 封装析构函数，统一回收节点资源。
   29. nativeModule_->disposeNode(handle_);
   30. }

   32. void AddChild(const std::shared_ptr<ArkUIBaseNode> &child)
   33. {
   34. children_.emplace_back(child);
   35. OnAddChild(child);
   36. }

   38. void RemoveChild(const std::shared_ptr<ArkUIBaseNode> &child)
   39. {
   40. children_.remove(child);
   41. OnRemoveChild(child);
   42. }

   44. void InsertChild(const std::shared_ptr<ArkUIBaseNode> &child, int32_t index)
   45. {
   46. if (index >= children_.size()) {
   47. AddChild(child);
   48. } else {
   49. auto iter = children_.begin();
   50. std::advance(iter, index);
   51. children_.insert(iter, child);
   52. OnInsertChild(child, index);
   53. }
   54. }

   56. ArkUI_NodeHandle GetHandle() const { return handle_; }

   58. protected:
   59. // 针对父容器子类需要重载下面的函数，实现组件挂载和卸载。
   60. virtual void OnAddChild(const std::shared_ptr<ArkUIBaseNode> &child) {}
   61. virtual void OnRemoveChild(const std::shared_ptr<ArkUIBaseNode> &child) {}
   62. virtual void OnInsertChild(const std::shared_ptr<ArkUIBaseNode> &child, int32_t index) {}

   64. ArkUI_NodeHandle handle_;
   65. ArkUI_NativeNodeAPI_1 *nativeModule_ = nullptr;

   67. private:
   68. std::list<std::shared_ptr<ArkUIBaseNode>> children_;
   69. };
   70. } // namespace NativeModule

   72. #endif // MYAPPLICATION_ARKUIBASENODE_H
   ```

   [ArkUIBaseNode.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonList/entry/src/main/cpp/ArkUIBaseNode.h#L15-L88)

   ```
   1. // ArkUINode.h
   2. // 提供通用属性和事件的封装。
   3. #ifndef MYAPPLICATION_ARKUINODE_H
   4. #define MYAPPLICATION_ARKUINODE_H

   6. #include "ArkUIBaseNode.h"
   7. #include "NativeModule.h"
   8. #include <arkui/native_node.h>
   9. #include <arkui/native_type.h>

   11. namespace NativeModule {

   13. class ArkUINode : public ArkUIBaseNode {
   14. public:
   15. explicit ArkUINode(ArkUI_NodeHandle handle) : ArkUIBaseNode(handle) {}

   17. ~ArkUINode() override {}

   19. void SetWidth(float width)
   20. {
   21. ArkUI_NumberValue value[] = {{.f32 = width}};
   22. ArkUI_AttributeItem item = {value, 1};
   23. nativeModule_->setAttribute(handle_, NODE_WIDTH, &item);
   24. }
   25. void SetPercentWidth(float percent)
   26. {
   27. ArkUI_NumberValue value[] = {{.f32 = percent}};
   28. ArkUI_AttributeItem item = {value, 1};
   29. nativeModule_->setAttribute(handle_, NODE_WIDTH_PERCENT, &item);
   30. }
   31. void SetHeight(float height)
   32. {
   33. ArkUI_NumberValue value[] = {{.f32 = height}};
   34. ArkUI_AttributeItem item = {value, 1};
   35. nativeModule_->setAttribute(handle_, NODE_HEIGHT, &item);
   36. }
   37. void SetPercentHeight(float percent)
   38. {
   39. ArkUI_NumberValue value[] = {{.f32 = percent}};
   40. ArkUI_AttributeItem item = {value, 1};
   41. nativeModule_->setAttribute(handle_, NODE_HEIGHT_PERCENT, &item);
   42. }
   43. void SetBackgroundColor(uint32_t color)
   44. {
   45. ArkUI_NumberValue value[] = {{.u32 = color}};
   46. ArkUI_AttributeItem item = {value, 1};
   47. nativeModule_->setAttribute(handle_, NODE_BACKGROUND_COLOR, &item);
   48. }

   50. protected:
   51. // 组件树操作的实现类对接。
   52. void OnAddChild(const std::shared_ptr<ArkUIBaseNode> &child) override
   53. {
   54. nativeModule_->addChild(handle_, child->GetHandle());
   55. }
   56. void OnRemoveChild(const std::shared_ptr<ArkUIBaseNode> &child) override
   57. {
   58. nativeModule_->removeChild(handle_, child->GetHandle());
   59. }
   60. void OnInsertChild(const std::shared_ptr<ArkUIBaseNode> &child, int32_t index) override
   61. {
   62. nativeModule_->insertChildAt(handle_, child->GetHandle(), index);
   63. }
   64. };
   65. } // namespace NativeModule

   67. #endif // MYAPPLICATION_ARKUINODE_H
   ```

   [ArkUINode.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonList/entry/src/main/cpp/ArkUINode.h#L15-L83)

   3）实现列表组件。

   ```
   1. // ArkUIListNode.h
   2. // 提供列表组件的封装。
   3. #ifndef MYAPPLICATION_ARKUILISTNODE_H
   4. #define MYAPPLICATION_ARKUILISTNODE_H

   6. #include "ArkUINode.h"

   8. namespace NativeModule {
   9. class ArkUIListNode : public ArkUINode {
   10. public:
   11. ArkUIListNode()
   12. : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI_NODE_LIST)) {}

   14. ~ArkUIListNode() override {}

   16. void SetScrollBarState(bool isShow)
   17. {
   18. ArkUI_ScrollBarDisplayMode displayMode =
   19. isShow ? ARKUI_SCROLL_BAR_DISPLAY_MODE_ON : ARKUI_SCROLL_BAR_DISPLAY_MODE_OFF;
   20. ArkUI_NumberValue value[] = {{.i32 = displayMode}};
   21. ArkUI_AttributeItem item = {value, 1};
   22. nativeModule_->setAttribute(handle_, NODE_SCROLL_BAR_DISPLAY_MODE, &item);
   23. }
   24. };
   25. } // namespace NativeModule

   27. #endif // MYAPPLICATION_ARKUILISTNODE_H
   ```

   [ArkUIListNode.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonList/entry/src/main/cpp/ArkUIListNode.h#L15-L43)

   4）实现列表项组件。

   ```
   1. // ArkUIListItemNode.h
   2. // 提供列表项的封装类。
   3. #ifndef MYAPPLICATION_ARKUISTACKNODE_H
   4. #define MYAPPLICATION_ARKUISTACKNODE_H

   6. #include "ArkUINode.h"

   8. namespace NativeModule {
   9. class ArkUIListItemNode : public ArkUINode {
   10. public:
   11. ArkUIListItemNode()
   12. : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI_NODE_LIST_ITEM)) {}
   13. };
   14. } // namespace NativeModule

   16. #endif // MYAPPLICATION_ARKUISTACKNODE_H
   ```

   [ArkUIListItemNode.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonList/entry/src/main/cpp/ArkUIListItemNode.h#L15-L32)

   5）实现文本组件。

   ```
   1. // ArkUITextNode.h
   2. // 实现文本组件的封装类。
   3. #ifndef MYAPPLICATION_ARKUITEXTNODE_H
   4. #define MYAPPLICATION_ARKUITEXTNODE_H

   6. #include "ArkUINode.h"

   8. #include <string>

   10. namespace NativeModule {
   11. class ArkUITextNode : public ArkUINode {
   12. public:
   13. ArkUITextNode()
   14. : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI_NODE_TEXT)) {}

   16. void SetFontSize(float fontSize)
   17. {
   18. ArkUI_NumberValue value[] = {{.f32 = fontSize}};
   19. ArkUI_AttributeItem item = {value, 1};
   20. nativeModule_->setAttribute(handle_, NODE_FONT_SIZE, &item);
   21. }
   22. void SetFontColor(uint32_t color)
   23. {
   24. ArkUI_NumberValue value[] = {{.u32 = color}};
   25. ArkUI_AttributeItem item = {value, 1};
   26. nativeModule_->setAttribute(handle_, NODE_FONT_COLOR, &item);
   27. }
   28. void SetTextContent(const std::string &content)
   29. {
   30. ArkUI_AttributeItem item = {nullptr, 0, content.c_str()};
   31. nativeModule_->setAttribute(handle_, NODE_TEXT_CONTENT, &item);
   32. }
   33. void SetTextAlign(ArkUI_TextAlignment align)
   34. {
   35. ArkUI_NumberValue value[] = {{.i32 = align}};
   36. ArkUI_AttributeItem item = {value, 1};
   37. nativeModule_->setAttribute(handle_, NODE_TEXT_ALIGN, &item);
   38. }
   39. };
   40. } // namespace NativeModule

   42. #endif // MYAPPLICATION_ARKUITEXTNODE_H
   ```

   [ArkUITextNode.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonList/entry/src/main/cpp/ArkUITextNode.h#L15-L58)
5. 完善步骤3的CreateTextListExample函数，实现Native文本列表的创建和挂载显示。

   ```
   1. // NormalTextListExample.h

   3. #ifndef MYAPPLICATION_NORMALTEXTLISTEXAMPLE_H
   4. #define MYAPPLICATION_NORMALTEXTLISTEXAMPLE_H

   6. #include "ArkUIBaseNode.h"
   7. #include "ArkUIListItemNode.h"
   8. #include "ArkUIListNode.h"
   9. #include "ArkUITextNode.h"

   11. namespace NativeModule {

   13. std::shared_ptr<ArkUIBaseNode> CreateTextListExample()
   14. {
   15. // 创建组件并挂载
   16. // 1：使用智能指针创建List组件。
   17. auto list = std::make_shared<ArkUIListNode>();
   18. list->SetPercentWidth(1);
   19. list->SetPercentHeight(1);
   20. list->SetScrollBarState(true);
   21. const int itemCount = 30;
   22. const int fontSizes = 16;
   23. const float screenWidth = 1;
   24. const int defaultHeight = 100;
   25. // 2：创建ListItem子组件并挂载到List上。
   26. for (int32_t i = 0; i < itemCount; ++i) {
   27. auto listItem = std::make_shared<ArkUIListItemNode>();
   28. auto textNode = std::make_shared<ArkUITextNode>();
   29. textNode->SetTextContent(std::to_string(i));
   30. textNode->SetFontSize(fontSizes);
   31. textNode->SetFontColor(0xFF000000);
   32. textNode->SetPercentWidth(1);
   33. textNode->SetPercentWidth(screenWidth);
   34. textNode->SetHeight(defaultHeight);
   35. textNode->SetBackgroundColor(0xFFfffacd);
   36. textNode->SetTextAlign(ARKUI_TEXT_ALIGNMENT_CENTER);
   37. listItem->InsertChild(textNode, i);
   38. list->AddChild(listItem);
   39. }
   40. return list;
   41. }
   42. } // namespace NativeModule

   44. #endif // MYAPPLICATION_NORMALTEXTLISTEXAMPLE_H
   ```

   [NormalTextListExample.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonList/entry/src/main/cpp/NormalTextListExample.h#L15-L60)
