---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/displaysync-xcomponent
title: 请求自绘制内容绘制帧率
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 使用可变帧率能力定制不同内容的绘制帧率 > 请求自绘制内容绘制帧率
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:df2dd05f0d7b2be4984f0ade153017878b299b6e4539fa54f1d83dd953078fe3
---

对于基于[XComponent](napi-xcomponent-guidelines.md)进行Native开发的业务，可以请求独立的绘制帧率进行内容开发，如游戏、自绘制UI框架对接等场景。

## 接口说明

| 函数名称 | 说明 |
| --- | --- |
| OH\_NativeXComponent\_SetExpectedFrameRateRange (OH\_NativeXComponent \*component, OH\_NativeXComponent\_ExpectedRateRange \*range) | 设置帧期望的帧率范围。 |
| OH\_NativeXComponent\_RegisterOnFrameCallback (OH\_NativeXComponent \*component, OH\_NativeXComponent\_OnFrameCallback \*callback) | 设置每帧回调函数，同时启动每帧回调。 |
| OH\_NativeXComponent\_UnregisterOnFrameCallback (OH\_NativeXComponent \*component) | 取消注册的每帧回调函数，同时停止调用回调函数。 |

详细的接口说明请参考[OH\_NativeXComponent Native XComponent](../harmonyos-references/capi-oh-nativexcomponent-native-xcomponent.md)。

## 开发步骤

说明

本范例是通过Drawing在Native侧实现图形的绘制，并将其呈现在NativeWindow上，具体可参考[使用Drawing实现图形绘制与显示](graphic-drawing-overview.md)。

1. 添加开发依赖。

   CMakeLists.txt中添加以下lib。

   ```
   1. target_link_libraries(entry PUBLIC libace_napi.z.so libnative_drawing.so libnative_window.so libace_ndk.z.so)
   ```

   [CMakeLists.txt](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySync/entry/src/main/cpp/CMakeLists.txt#L20-L22)

   导入依赖的相关头文件。

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

   [sample\_xcomponent.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySync/entry/src/main/cpp/samples/sample_xcomponent.h#L17-L33)

   ```
   1. #include <native_drawing/drawing_text_typography.h>
   ```

   [sample\_xcomponent.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySync/entry/src/main/cpp/samples/sample_xcomponent.cpp#L17-L19)
2. 定义ArkTS接口文件XComponentContext.ts，用来对接Native层。

   ```
   1. export default interface XComponentContext {
   2. register(): void;

   4. unregister(): void;
   5. };
   ```

   [XComponentContext.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySync/entry/src/main/ets/interface/XComponentContext.ts#L15-L21)
3. 定义演示页面，包含两个XComponent组件。

   ```
   1. import XComponentContext from '../interface/XComponentContext';
   2. // ...

   4. @Entry
   5. @Component
   6. struct Index {
   7. private xComponentContext1: XComponentContext | undefined = undefined;
   8. private xComponentContext2: XComponentContext | undefined = undefined;

   10. build() {
   11. Column() {
   12. Row() {
   13. // ...

   15. XComponent({
   16. id: 'xcomponentId_30',
   17. type: XComponentType.SURFACE,
   18. libraryname: 'entry'
   19. })
   20. .onLoad((xComponentContext) => {
   21. this.xComponentContext1 = xComponentContext as XComponentContext;
   22. }).width('640px')
   23. // ...
   24. }.height('40%')

   26. Row() {
   27. // ...

   29. XComponent({
   30. id: 'xcomponentId_120',
   31. type: XComponentType.SURFACE,
   32. libraryname: 'entry'
   33. })
   34. .onLoad((xComponentContext) => {
   35. this.xComponentContext2 = xComponentContext as XComponentContext;
   36. }).width('640px')
   37. // ...
   38. }.height('40%')

   40. // ...
   41. }
   42. }
   43. }
   ```

   [XComponentDisplaySync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySync/entry/src/main/ets/DispalySync/XComponentDisplaySync.ets#L15-L141)
4. Native层配置帧率和注册回调函数。

   ```
   1. static void TestCallback(OH_NativeXComponent *component, uint64_t timestamp, uint64_t targetTimestamp)
   2. {
   3. // ...

   5. int32_t xSize = OH_NativeXComponent_GetXComponentSize(component, nativeWindow, &width, &height);
   6. if ((xSize == OH_NATIVEXCOMPONENT_RESULT_SUCCESS) && (render != nullptr)) {
   7. render->Prepare();
   8. render->Create();
   9. if (id == "xcomponentId_30") {
   10. int offset = 16;
   11. render->ConstructPath(offset, offset, render->defaultOffsetY);
   12. }
   13. if (id == "xcomponentId_120") {
   14. int offset = 4;
   15. render->ConstructPath(offset, offset, render->defaultOffsetY);
   16. }
   17. // ...
   18. }
   19. }
   ```

   [sample\_xcomponent.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySync/entry/src/main/cpp/samples/sample_xcomponent.cpp#L68-L112)

   说明

   * Callback回调函数运行于UI主线程，故涉及UI线程的耗时操作不应运行于回调函数中，以免影响性能。
   * 实例在调用OH\_NativeXComponent\_RegisterOnFrameCallback后，在不需要进行帧率控制时，应进行OH\_NativeXComponent\_UnregisterOnFrameCallback操作，避免内存泄漏及性能功耗影响。
   * API version 18之前，应用调用OH\_NativeXComponent\_RegisterOnFrameCallback接口设置回调函数，如果没有取消注册，在XComponent实例存在期间，能一直收到期望回调。
   * 从API version 18开始，应用调用OH\_NativeXComponent\_RegisterOnFrameCallback接口设置回调函数，如果没有取消注册，只在XComponent上树期间，能收到期望回调。

   ```
   1. void SampleXComponent::RegisterOnFrameCallback(OH_NativeXComponent *nativeXComponent)
   2. {
   3. // ...
   4. OH_NativeXComponent_RegisterOnFrameCallback(nativeXComponent, TestCallback);
   5. }
   ```

   [sample\_xcomponent.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySync/entry/src/main/cpp/samples/sample_xcomponent.cpp#L425-L433)

   ```
   1. napi_value SampleXComponent::NapiRegister(napi_env env, napi_callback_info info)
   2. {
   3. // ...
   4. render->RegisterOnFrameCallback(nativeXComponent);
   5. // ...
   6. }
   ```

   [sample\_xcomponent.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySync/entry/src/main/cpp/samples/sample_xcomponent.cpp#L251-L305)

   ```
   1. napi_value SampleXComponent::NapiUnregister(napi_env env, napi_callback_info info)
   2. {
   3. // ...
   4. OH_NativeXComponent_UnregisterOnFrameCallback(nativeXComponent);
   5. // ...
   6. }
   ```

   [sample\_xcomponent.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySync/entry/src/main/cpp/samples/sample_xcomponent.cpp#L307-L355)
5. TS层注册和取消注册每帧回调。

   ```
   1. Row() {
   2. Button('Start')
   3. .id('Start')
   4. .fontSize(14)
   5. .fontWeight(500)
   6. .margin({ bottom: 20, right: 6, left: 6 })
   7. .onClick(() => {
   8. if (this.xComponentContext1) {
   9. this.xComponentContext1.register();
   10. }
   11. if (this.xComponentContext2) {
   12. this.xComponentContext2.register();
   13. }
   14. })
   15. .width('30%')
   16. .height(40)
   17. .shadow(ShadowStyle.OUTER_DEFAULT_LG)

   19. Button('Stop')
   20. .id('Stop')
   21. .fontSize(14)
   22. .fontWeight(500)
   23. .margin({ bottom: 20, left: 6 })
   24. .onClick(() => {
   25. if (this.xComponentContext1) {
   26. this.xComponentContext1.unregister();
   27. }
   28. if (this.xComponentContext2) {
   29. this.xComponentContext2.unregister();
   30. }
   31. })
   32. .width('30%')
   33. .height(40)
   34. .shadow(ShadowStyle.OUTER_DEFAULT_LG)

   36. // ...
   37. }
   ```

   [XComponentDisplaySync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySync/entry/src/main/ets/DispalySync/XComponentDisplaySync.ets#L78-L134)
