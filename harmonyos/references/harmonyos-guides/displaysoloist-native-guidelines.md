---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/displaysoloist-native-guidelines
title: NativeDisplaySoloist开发指导 (C/C++)
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 使用可变帧率能力定制不同内容的绘制帧率 > NativeDisplaySoloist开发指导 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:27e44ebbf5256ae6344cfb578643abcb9d0d741fd1d7eec70a77d86a3a231f03
---

如果开发者想在独立线程中实现帧率控制的Native侧业务，可以通过DisplaySoloist来实现，如游戏、自绘制UI框架对接等场景。

开发者可以选择多个DisplaySoloist实例共享一个线程，也可以选择每个DisplaySoloist实例独占一个线程。

## 接口说明

| 函数名称 | 说明 |
| --- | --- |
| OH\_DisplaySoloist\* OH\_DisplaySoloist\_Create (bool useExclusiveThread) | 创建一个OH\_DisplaySoloist实例。 |
| OH\_DisplaySoloist\_Destroy (OH\_DisplaySoloist \* displaySoloist) | 销毁一个OH\_DisplaySoloist实例。 |
| OH\_DisplaySoloist\_Start (OH\_DisplaySoloist \* displaySoloist, OH\_DisplaySoloist\_FrameCallback callback, void \* data ) | 设置每帧回调函数，每次VSync信号到来时启动每帧回调。 |
| OH\_DisplaySoloist\_Stop (OH\_DisplaySoloist \* displaySoloist) | 停止请求下一次VSync信号，并停止调用回调函数callback。 |
| OH\_DisplaySoloist\_SetExpectedFrameRateRange (OH\_DisplaySoloist\* displaySoloist, DisplaySoloist\_ExpectedRateRange\* range) | 设置期望帧率范围。 |

详细的接口说明请参考[NativeDisplaySoloist](../harmonyos-references/capi-nativedisplaysoloist.md)。

## 开发示例

本范例是通过Drawing在Native侧实现图形的绘制，通过异步线程设置期望的帧率，再根据帧率进行图形的绘制并将其呈现在NativeWindow上，图形绘制部分可参考[使用Drawing实现图形绘制与显示](graphic-drawing-overview.md)。

### 添加开发依赖

**添加动态链接库**

CMakeLists.txt中添加以下lib。

```
1. target_link_libraries(entry PUBLIC libace_napi.z.so libnative_drawing.so libnative_window.so libace_ndk.z.so libnative_display_soloist.so)
```

[CMakeLists.txt](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySoloist/entry/src/main/cpp/CMakeLists.txt#L23-L25)

**头文件**

```
1. #include <ace/xcomponent/native_interface_xcomponent.h>
2. #include <arpa/nameser.h>
3. #include <bits/alltypes.h>
4. #include <native_window/external_window.h>
5. #include <native_drawing/drawing_bitmap.h>
6. #include <native_drawing/drawing_color.h>
7. #include <native_drawing/drawing_canvas.h>
8. #include <native_drawing/drawing_pen.h>
9. #include <native_drawing/drawing_brush.h>
10. #include <native_drawing/drawing_path.h>
11. #include <cstdint>
12. #include <map>
13. #include <sys/mman.h>
14. #include <string>
15. #include "napi/native_api.h"
```

[sample\_xcomponent.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySoloist/entry/src/main/cpp/samples/sample_xcomponent.h#L17-L33)

```
1. #include <native_display_soloist/native_display_soloist.h>
```

[sample\_xcomponent.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySoloist/entry/src/main/cpp/samples/sample_xcomponent.cpp#L18-L20)

### 开发步骤

1. 定义ArkTS接口文件XComponentContext.ts，用来对接Native层。

   ```
   1. export default interface XComponentContext {
   2. register(): void;

   4. unregister(): void;

   6. destroy(): void;
   7. };
   ```

   [XComponentContext.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySoloist/entry/src/main/ets/interface/XComponentContext.ts#L15-L23)
2. 定义演示页面，包含两个XComponent组件。

   ```
   1. import XComponentContext from '../interface/XComponentContext';
   2. // ...

   4. @Entry
   5. @Component
   6. struct Index {
   7. private xComponentContext1: XComponentContext | undefined = undefined;
   8. private xComponentContext2: XComponentContext | undefined = undefined;

   10. // ...

   12. build() {
   13. Column() {
   14. Row() {
   15. // ...

   17. XComponent({
   18. id: 'xcomponentId_30',
   19. type: XComponentType.SURFACE,
   20. libraryname: 'entry'
   21. })
   22. .onLoad((xComponentContext) => {
   23. this.xComponentContext1 = xComponentContext as XComponentContext;
   24. }).width('640px')
   25. // ...
   26. }.height('40%')

   28. Row() {
   29. // ...

   31. XComponent({
   32. id: 'xcomponentId_120',
   33. type: XComponentType.SURFACE,
   34. libraryname: 'entry'
   35. })
   36. .onLoad((xComponentContext) => {
   37. this.xComponentContext2 = xComponentContext as XComponentContext;
   38. }).width('640px')
   39. // ...
   40. }.height('40%')

   42. // ...
   43. }
   44. }
   45. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySoloist/entry/src/main/ets/pages/Index.ets#L15-L144)
3. 在 Native C++层获取NativeXComponent。建议使用单例模式保存XComponent。此步骤需要在napi\_init的过程中处理。

   创建一个PluginManager单例类，用于管理NativeXComponent。

   ```
   1. class PluginManager {
   2. public:
   3. ~PluginManager();

   5. static PluginManager *GetInstance();

   7. void SetNativeXComponent(std::string &id, OH_NativeXComponent *nativeXComponent);
   8. SampleXComponent *GetRender(std::string &id);
   9. void Export(napi_env env, napi_value exports);

   11. private:
   12. std::unordered_map<std::string, OH_NativeXComponent *> nativeXComponentMap_;
   13. std::unordered_map<std::string, SampleXComponent *> pluginRenderMap_;
   14. };
   ```

   [plugin\_manager.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySoloist/entry/src/main/cpp/plugin/plugin_manager.h#L25-L40)

   SampleXComponent类会在后面的绘制图形中创建。

   ```
   1. void PluginManager::Export(napi_env env, napi_value exports)
   2. {
   3. nativeXComponentMap_.clear();
   4. pluginRenderMap_.clear();
   5. if ((env == nullptr) || (exports == nullptr)) {
   6. SAMPLE_LOGE("Export: env or exports is null");
   7. return;
   8. }

   10. napi_value exportInstance = nullptr;
   11. if (napi_get_named_property(env, exports, OH_NATIVE_XCOMPONENT_OBJ, &exportInstance) != napi_ok) {
   12. SAMPLE_LOGE("Export: napi_get_named_property fail");
   13. return;
   14. }

   16. OH_NativeXComponent *nativeXComponent = nullptr;
   17. if (napi_unwrap(env, exportInstance, reinterpret_cast<void **>(&nativeXComponent)) != napi_ok) {
   18. SAMPLE_LOGE("Export: napi_unwrap fail");
   19. return;
   20. }

   22. char idStr[OH_XCOMPONENT_ID_LEN_MAX + 1] = {'\0'};
   23. uint64_t idSize = OH_XCOMPONENT_ID_LEN_MAX + 1;
   24. if (OH_NativeXComponent_GetXComponentId(nativeXComponent, idStr, &idSize) != OH_NATIVEXCOMPONENT_RESULT_SUCCESS) {
   25. SAMPLE_LOGE("Export: OH_NativeXComponent_GetXComponentId fail");
   26. return;
   27. }

   29. std::string id(idStr);
   30. auto context = PluginManager::GetInstance();
   31. if ((context != nullptr) && (nativeXComponent != nullptr)) {
   32. context->SetNativeXComponent(id, nativeXComponent);
   33. auto render = context->GetRender(id);
   34. if (render != nullptr) {
   35. render->RegisterCallback(nativeXComponent);
   36. render->Export(env, exports);
   37. } else {
   38. SAMPLE_LOGE("render is nullptr");
   39. }
   40. }
   41. }
   ```

   [plugin\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySoloist/entry/src/main/cpp/plugin/plugin_manager.cpp#L49-L91)
4. Native层配置帧率和注册回调函数。

   定义每帧回调函数内容。

   ```
   1. static void TestCallback(long long timestamp, long long targetTimestamp, void *data)
   2. {
   3. // ...
   4. OH_NativeXComponent *component = nullptr;
   5. component = static_cast<OH_NativeXComponent *>(data);
   6. if (component == nullptr) {
   7. SAMPLE_LOGE("TestCallback: component is null");
   8. return;
   9. }

   11. char idStr[OH_XCOMPONENT_ID_LEN_MAX + 1] = {'\0'};
   12. uint64_t idSize = OH_XCOMPONENT_ID_LEN_MAX + 1;
   13. if (OH_NativeXComponent_GetXComponentId(component, idStr, &idSize) != OH_NATIVEXCOMPONENT_RESULT_SUCCESS) {
   14. SAMPLE_LOGE("TestCallback: Unable to get XComponent id");
   15. return;
   16. }

   18. std::string id(idStr);
   19. auto render = SampleXComponent::GetInstance(id);
   20. OHNativeWindow *nativeWindow = render->GetNativeWindow();
   21. uint64_t width;
   22. uint64_t height;

   24. int32_t xSize = OH_NativeXComponent_GetXComponentSize(component, nativeWindow, &width, &height);
   25. if ((xSize == OH_NATIVEXCOMPONENT_RESULT_SUCCESS) && (render != nullptr)) {
   26. render->Prepare();
   27. render->Create();
   28. if (id == "xcomponentId_30") {
   29. int offset = 16;
   30. render->ConstructPath(offset, offset, render->defaultOffsetY);
   31. }
   32. if (id == "xcomponentId_120") {
   33. int offset = 4;
   34. render->ConstructPath(offset, offset, render->defaultOffsetY);
   35. }
   36. // ...
   37. }
   38. }
   ```

   [sample\_xcomponent.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySoloist/entry/src/main/cpp/samples/sample_xcomponent.cpp#L74-L120)

   使用DisplaySoloist接口配置帧率和注册每帧回调函数。如果使用OH\_DisplaySoloist\_Create创建DisplaySoloist实例时传入的参数useExclusiveThread为true，则OH\_DisplaySoloist\_FrameCallback以独占线程方式执行，否则OH\_DisplaySoloist\_FrameCallback以共享线程方式执行。

   说明

   * 实例在调用NapiRegister后，在不需要进行帧率控制时，应进行NapiUnregister操作，避免内存泄漏问题。
   * 在页面跳转时，应进行NapiUnregister和NapiDestroy操作，避免内存泄漏问题。

   ```
   1. static std::unordered_map<std::string, OH_DisplaySoloist *> g_displaySync;

   3. // ...

   5. void ExecuteDisplaySoloist(std::string id, DisplaySoloist_ExpectedRateRange range, bool useExclusiveThread,
   6. OH_NativeXComponent *nativeXComponent)
   7. {
   8. OH_DisplaySoloist *nativeDisplaySoloist = nullptr;
   9. if (g_displaySync.find(id) == g_displaySync.end()) {
   10. g_displaySync[id] = OH_DisplaySoloist_Create(useExclusiveThread);
   11. }
   12. nativeDisplaySoloist = g_displaySync[id];
   13. OH_DisplaySoloist_SetExpectedFrameRateRange(nativeDisplaySoloist, &range);
   14. OH_DisplaySoloist_Start(nativeDisplaySoloist, TestCallback, nativeXComponent);
   15. }

   17. napi_value SampleXComponent::NapiRegister(napi_env env, napi_callback_info info)
   18. {
   19. // ...

   21. napi_value thisArg;
   22. if (napi_get_cb_info(env, info, nullptr, nullptr, &thisArg, nullptr) != napi_ok) {
   23. SAMPLE_LOGE("NapiRegister: napi_get_cb_info fail");
   24. return nullptr;
   25. }

   27. napi_value exportInstance;
   28. if (napi_get_named_property(env, thisArg, OH_NATIVE_XCOMPONENT_OBJ, &exportInstance) != napi_ok) {
   29. SAMPLE_LOGE("NapiRegister: napi_get_named_property fail");
   30. return nullptr;
   31. }

   33. OH_NativeXComponent *nativeXComponent = nullptr;
   34. if (napi_unwrap(env, exportInstance, reinterpret_cast<void **>(&nativeXComponent)) != napi_ok) {
   35. SAMPLE_LOGE("NapiRegister: napi_unwrap fail");
   36. return nullptr;
   37. }

   39. char idStr[OH_XCOMPONENT_ID_LEN_MAX + 1] = {'\0'};
   40. uint64_t idSize = OH_XCOMPONENT_ID_LEN_MAX + 1;
   41. if (OH_NativeXComponent_GetXComponentId(nativeXComponent, idStr, &idSize) != OH_NATIVEXCOMPONENT_RESULT_SUCCESS) {
   42. SAMPLE_LOGE("NapiRegister: Unable to get XComponent id");
   43. return nullptr;
   44. }
   45. SAMPLE_LOGI("RegisterID = %{public}s", idStr);
   46. std::string id(idStr);
   47. SampleXComponent *render = SampleXComponent().GetInstance(id);
   48. if (render != nullptr) {
   49. DisplaySoloist_ExpectedRateRange range;
   50. bool useExclusiveThread = false;
   51. if (id == "xcomponentId30") {
   52. range = {30, 120, 30};
   53. }

   55. if (id == "xcomponentId120") {
   56. range = {30, 120, 120};
   57. }
   58. ExecuteDisplaySoloist(id, range, useExclusiveThread, nativeXComponent);
   59. }
   60. return nullptr;
   61. }

   63. napi_value SampleXComponent::NapiUnregister(napi_env env, napi_callback_info info)
   64. {
   65. // ...
   66. OH_DisplaySoloist_Stop(g_displaySync[id]);
   67. // ...
   68. }

   70. napi_value SampleXComponent::NapiDestroy(napi_env env, napi_callback_info info)
   71. {
   72. // ...
   73. OH_DisplaySoloist_Destroy(g_displaySync[id]);
   74. g_displaySync.erase(id);
   75. // ...
   76. }

   78. // ...

   80. void SampleXComponent::Export(napi_env env, napi_value exports)
   81. {
   82. if ((env == nullptr) || (exports == nullptr)) {
   83. SAMPLE_LOGE("Export: env or exports is null");
   84. return;
   85. }
   86. napi_property_descriptor desc[] = {
   87. {"register", nullptr, SampleXComponent::NapiRegister, nullptr, nullptr, nullptr, napi_default, nullptr},
   88. {"unregister", nullptr, SampleXComponent::NapiUnregister, nullptr, nullptr, nullptr, napi_default, nullptr},
   89. {"destroy", nullptr, SampleXComponent::NapiDestroy, nullptr, nullptr, nullptr, napi_default, nullptr}};

   91. if (napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc) != napi_ok) {
   92. SAMPLE_LOGE("Export: napi_define_properties failed");
   93. }
   94. }
   ```

   [sample\_xcomponent.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySoloist/entry/src/main/cpp/samples/sample_xcomponent.cpp#L25-L471)
5. TS层注册和取消注册每帧回调，销毁OH\_DisplaySoloist实例。

   ```
   1. aboutToDisappear(): void {
   2. // ...
   3. if (this.xComponentContext1) {
   4. this.xComponentContext1.unregister();
   5. this.xComponentContext1.destroy();
   6. }
   7. if (this.xComponentContext2) {
   8. this.xComponentContext2.unregister();
   9. this.xComponentContext2.destroy();
   10. }
   11. }

   13. // ...

   15. Row() {
   16. Button('Start')
   17. .id('Start')
   18. .fontSize(14)
   19. .fontWeight(500)
   20. .margin({ bottom: 20, right: 6, left: 6 })
   21. .onClick(() => {
   22. if (this.xComponentContext1) {
   23. this.xComponentContext1.register();
   24. }
   25. if (this.xComponentContext2) {
   26. this.xComponentContext2.register();
   27. }
   28. })
   29. .width('30%')
   30. .height(40)
   31. .shadow(ShadowStyle.OUTER_DEFAULT_LG)

   33. Button('Stop')
   34. .id('Stop')
   35. .fontSize(14)
   36. .fontWeight(500)
   37. .margin({ bottom: 20, left: 6 })
   38. .onClick(() => {
   39. if (this.xComponentContext1) {
   40. this.xComponentContext1.unregister();
   41. }
   42. if (this.xComponentContext2) {
   43. this.xComponentContext2.unregister();
   44. }
   45. })
   46. .width('30%')
   47. .height(40)
   48. .shadow(ShadowStyle.OUTER_DEFAULT_LG)
   49. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySoloist/entry/src/main/ets/pages/Index.ets#L30-L135)
