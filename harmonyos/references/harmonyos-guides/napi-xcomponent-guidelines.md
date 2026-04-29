---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-xcomponent-guidelines
title: 自定义渲染 (XComponent)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加组件 > 自定义渲染 (XComponent)
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5b7e799187688b41cf7486e00af84b0352e238e0e296aeeb036f1c20afdb2b72
---

## 概述

XComponent组件作为一种渲染组件，可用于EGL/OpenGLES和媒体数据写入，通过使用XComponent持有的“[NativeWindow](native-window-guidelines.md)”渲染画面，满足开发需要实现高级自定义渲染的需求，例如相机预览流的显示和游戏画面的渲染。开发者可通过指定XComponent组件的type字段来实现不同的渲染方式，分别为[XComponentType](../harmonyos-references/ts-appendix-enums.md#xcomponenttype10).SURFACE和XComponentType.TEXTURE。对于SURFACE类型，开发者将定制的绘制内容单独展示到屏幕上。对于TEXTURE类型，开发者将定制的绘制内容和XComponent组件的内容合成后展示到屏幕上。

可以将XComponent类比为一个“画布”，在其上支持使用各种渲染技术（如OpenGL、Vulkan等）绘制复杂的图形，而XComponent组件则负责管理这个画布的位置、大小和各种交互事件。

目前XComponent主要用于两类场景：

| 场景类型 | 使用场景 |
| --- | --- |
| 高性能渲染 | 游戏画面、3D图形、复杂动画等。 |
| 媒体数据处理 | 相机预览、视频播放、图像处理等。 |

## 约束与限制

当开发者传输的绘制内容包含透明元素时，Surface区域的显示效果会与下方内容进行合成展示。例如，若传输的内容完全透明，且XComponent的背景色被设置为黑色，同时Surface保持默认的大小与位置，则最终显示的将是一片黑色区域。

## XComponent渲染上屏原理

XComponent持有一个Surface，开发者能通过调用[NativeWindow](native-window-guidelines.md)等接口，申请并提交Buffer至图形队列，以此方式将自绘制内容传送至该Surface，其主体流程如下：

应用RequestBuffer获取空闲帧 → 应用生产帧数据 → 应用调用FlushBuffer提交到BufferQueue → 系统渲染侧通过AcquireBuffer获取帧 → 渲染到屏幕 → 系统渲染侧通过调用ReleaseBuffer释放。

经过上述流程，应用自绘制的内容就可以显示在XComponent持有的Surface区域，而XComponent则负责将此Surface整合进UI界面，其中展示的内容正是开发者发送的自绘制内容。Surface的默认位置与大小与XComponent组件一致，开发者可利用[setXComponentSurfaceRect](../harmonyos-references/ts-basic-components-xcomponent.md#setxcomponentsurfacerect12)接口自定义调整Surface的位置和大小。XComponent组件负责创建Surface，并通过回调将Surface的相关信息告知应用。应用可以通过一系列接口设定Surface的属性。该组件本身不对所绘制的内容进行感知，亦不提供渲染绘制的接口。

说明

主体流程中提到需要应用进行的RequestBuffer和FlushBuffer操作，在具体场景下一般已经被相关API（如相机模块、播放器模块、OpenGL相关接口等）封装，应用的实际开发者只需按要求调用这些API即可，不需要直接操作BufferQueue。

## 创建XComponent和管理Surface生命周期

为满足开发者的各种需求，XComponent组件提供了多种创建方式以及多种Surface生命周期的管理方式，下面将进行介绍。

### 创建XComponent

目前ArkUI提供了三种UI组件的创建方式，分别是使用[ArkTS声明式UI描述](arkts-declarative-ui-description.md)创建、使用[ArkTS自定义组件节点](arkts-user-defined-arktsnode-framenode.md)创建以及使用[NDK接口](ndk-build-ui-overview.md)创建。

通用UI界面开发场景下，建议使用ArkTS声明式UI描述创建XComponent组件。对于需要使用ArkTS自定义组件节点创建以及NDK接口创建的具体场景请参考这两种创建方式的相关介绍。

### 管理XComponent持有Surface的生命周期

在[XComponent渲染上屏原理](napi-xcomponent-guidelines.md#xcomponent渲染上屏原理)中提到，XComponent能够显示应用自绘制的内容依赖的是其持有的Surface，因此了解如何获取XComponent持有的Surface的生命周期也十分重要。

XComponent推荐使用两种方式获取XComponent持有Surface的生命周期，分别为在ArkTS侧使用[XComponentController](../harmonyos-references/ts-basic-components-xcomponent.md#xcomponentcontroller)管理Surface生命周期，以及在Native侧使用[OH\_ArkUI\_SurfaceHolder](../harmonyos-references/component-native-xcomponent-oh-arkui-surfaceholder.md)管理Surface生命周期。

对于需要在ArkTS侧使用已封装接口进行功能开发（如相机预览、视频播放等）或对跨语言性能损耗不敏感的跨语言开发，建议直接在ArkTS侧使用XComponentController管理Surface生命周期。其生命周期的触发时机如下：

* onSurfaceCreated回调

  触发时刻：XComponent创建完成且创建好Surface后触发。

  ArkTS侧onSurfaceCreated的时序如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/5_T728FKR96xIsQQi0hijw/zh-cn_image_0000002558604722.png?HW-CC-KV=V1&HW-CC-Date=20260429T052751Z&HW-CC-Expire=86400&HW-CC-Sign=C9F284F40DFFE90320AAED412E376A6B8BCDD5ECDED27AEA63EE4F743DA3A167)
* onSurfaceChanged回调

  触发时刻：Surface大小变化触发重新布局之后触发。

  ArkTS侧onSurfaceChanged的时序如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/6Napod9_QuGV4_gAsZe2jg/zh-cn_image_0000002589324247.png?HW-CC-KV=V1&HW-CC-Date=20260429T052751Z&HW-CC-Expire=86400&HW-CC-Sign=07189377A239244527ADF8F7F8F7396ABF34ACDD6D6F6312E3F5C6DC1EF84A22)
* onSurfaceDestroyed回调

  触发时刻：XComponent组件被销毁时触发，与一般ArkUI的组件销毁时机一致。

  ArkTS侧onSurfaceDestroyed的时序图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/InrV-WiQTTiMMOpQ41lrAA/zh-cn_image_0000002589244187.png?HW-CC-KV=V1&HW-CC-Date=20260429T052751Z&HW-CC-Expire=86400&HW-CC-Sign=B74A428909AB1C5F7ED0F49B86BFA78D8CEEFF4CFE331E2F290DE3D797B636A9)

对于复杂的交互逻辑需跨语言开发，追求极致渲染性能或业务需求自主控制Surface的创建和销毁的，建议在Native侧使用OH\_ArkUI\_SurfaceHolder管理Surface生命周期。其生命周期触发时机如下：

* OnSurfaceCreated回调

  触发时刻：XComponent创建完成且Surface绑定生命周期回调后，满足以下任一条件时触发。

  1. 组件上树且autoInitialize = true。
  2. 调用OH\_ArkUI\_XComponent\_Initialize。

  Native侧OnSurfaceCreated的时序如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/u_1DoVa2Sa-TWMq2lw_kqQ/zh-cn_image_0000002558764380.png?HW-CC-KV=V1&HW-CC-Date=20260429T052751Z&HW-CC-Expire=86400&HW-CC-Sign=4B9F8EC858F93AB4A8F2DCBECB2A07A968280A9768DB0964EE4F3719133617BA)
* OnSurfaceChanged回调

  触发时刻：OnSurfaceCreated回调成功触发且Surface大小变化触发重新布局之后触发。

  Native侧OnSurfaceChanged的时序如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/F1fTofLaRXKjThho5mnA8A/zh-cn_image_0000002558604724.png?HW-CC-KV=V1&HW-CC-Date=20260429T052751Z&HW-CC-Expire=86400&HW-CC-Sign=3C6E36033D3A45CA3ACCD8D8CE28B316E40267402BB235C3E36B53D11D4B9945)
* OnSurfaceDestroyed回调

  触发时刻：组件下树且autoInitialize=true 或者调用 OH\_ArkUI\_XComponent\_Finalize后触发。

  Native侧OnSurfaceDestroyed的时序图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/7D18PE-CTJqPy674PWaNHw/zh-cn_image_0000002589324249.png?HW-CC-KV=V1&HW-CC-Date=20260429T052751Z&HW-CC-Expire=86400&HW-CC-Sign=FD3392FBCC09F6E778D17A4AEB69458F461FD5A6F8F8471F15CA56CD360DB1B0)

### XComponent的开发范式

将[创建XComponent](napi-xcomponent-guidelines.md#创建xcomponent)和[管理XComponent持有Surface的生命周期](napi-xcomponent-guidelines.md#管理xcomponent持有surface的生命周期)进行排列组合，除使用NDK接口创建的XComponent无法在ArkTS侧使用XComponentController来管理Surface生命周期外，目前共有以下五种XComponent开发范式：

* 通过ArkTS声明式UI描述来创建组件并结合XComponentController实现对Surface生命周期的管理。

  ```
  1. import nativeRender from 'libnativerender.so';

  3. // 重写XComponentController，设置生命周期回调
  4. class MyXComponentController extends XComponentController{
  5. onSurfaceCreated(surfaceId: string): void {
  6. console.info(`onSurfaceCreated surfaceId: ${surfaceId}`);
  7. nativeRender.SetSurfaceId(BigInt(surfaceId));
  8. }
  9. onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void {
  10. console.info(`onSurfaceChanged surfaceId: ${surfaceId}, rect: ${JSON.stringify(rect)}}`);
  11. // 在onSurfaceChanged中调用ChangeSurface绘制内容
  12. nativeRender.ChangeSurface(BigInt(surfaceId), rect.surfaceWidth, rect.surfaceHeight);
  13. }
  14. onSurfaceDestroyed(surfaceId: string): void {
  15. console.info(`onSurfaceDestroyed surfaceId: ${surfaceId}`);
  16. nativeRender.DestroySurface(BigInt(surfaceId));
  17. }
  18. }

  20. @Entry
  21. @Component
  22. struct Index {
  23. @State currentStatus: string = 'index';
  24. xComponentController: XComponentController = new MyXComponentController();
  25. build() {
  26. Column() {
  27. // ···
  28. // 在xxx.ets中定义XComponent
  29. Column({ space: 10 }) {
  30. XComponent({
  31. type: XComponentType.SURFACE,
  32. controller: this.xComponentController
  33. })
  34. Text(this.currentStatus)
  35. .fontSize('24fp')
  36. .fontWeight(500)
  37. }
  38. .onClick(() => {
  39. let surfaceId = this.xComponentController.getXComponentSurfaceId();
  40. nativeRender.ChangeColor(BigInt(surfaceId));
  41. let hasChangeColor: boolean = false;
  42. if (nativeRender.GetXComponentStatus(BigInt(surfaceId))) {
  43. hasChangeColor = nativeRender.GetXComponentStatus(BigInt(surfaceId)).hasChangeColor;
  44. }
  45. if (hasChangeColor) {
  46. this.currentStatus = "change color";
  47. }
  48. })
  49. // ···
  50. }
  51. .width('100%')
  52. .height('100%')
  53. }
  54. }
  ```
* 通过ArkTS声明式UI描述来创建组件并结合OH\_ArkUI\_SurfaceHolders实现对Surface生命周期的管理。

  ```
  1. import native from 'libnativerender.so';

  3. // ...

  5. @Component
  6. export struct SurfaceHolderDeclarative {
  7. @State currentStatus: string = 'init';
  8. private xcNode: FrameNode | null = null;
  9. build() {
  10. NavDestination() {
  11. // ...
  12. Column({ space: 10 }) {
  13. // 创建XComponent组件
  14. XComponent({
  15. type: XComponentType.SURFACE,
  16. })
  17. .id('XComponentSurfaceHolder')
  18. .onAttach(() => {
  19. this.xcNode = this.getUIContext().getAttachedFrameNodeById('XComponentSurfaceHolder');
  20. if (!this.xcNode) {
  21. return;
  22. }
  23. native.bindNode('XComponentSurfaceHolder', this.xcNode); // 跨语言调用至Native侧获取SurfaceHolder并绑定Surface生命周期回调
  24. })
  25. .onDetach(() => {
  26. native.unbindNode('XComponentSurfaceHolder');
  27. this.xcNode = null;
  28. })
  29. }
  30. // ...
  31. }
  32. }
  33. }
  ```

  Native侧获取SurfaceHolder并绑定Surface生命周期回调的具体实现。

  ```
  1. napi_value PluginManager::BindNode(napi_env env, napi_callback_info info)
  2. {
  3. size_t argc = 2;
  4. napi_value args[2] = {nullptr};
  5. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
  6. std::string nodeId = value2String(env, args[0]);
  7. ArkUI_NodeHandle handle;
  8. OH_ArkUI_GetNodeHandleFromNapiValue(env, args[1], &handle);             // 获取nodeHandle
  9. OH_ArkUI_SurfaceHolder *holder = OH_ArkUI_SurfaceHolder_Create(handle); // 获取SurfaceHolder
  10. nodeHandleMap_[nodeId] = handle;
  11. surfaceHolderMap_[handle] = holder;
  12. auto callback = OH_ArkUI_SurfaceCallback_Create(); // 创建SurfaceCallback
  13. callbackMap_[holder] = callback;
  14. auto render = new EGLRender();
  15. OH_ArkUI_SurfaceHolder_SetUserData(holder, render);                                // 将render保存在holder中
  16. OH_ArkUI_SurfaceCallback_SetSurfaceCreatedEvent(callback, OnSurfaceCreatedNative); // 注册OnSurfaceCreated回调
  17. OH_ArkUI_SurfaceCallback_SetSurfaceChangedEvent(callback, OnSurfaceChangedNative); // 注册OnSurfaceChanged回调
  18. OH_ArkUI_SurfaceCallback_SetSurfaceDestroyedEvent(callback, OnSurfaceDestroyedNative); // 注册OnSurfaceDestroyed回调
  19. OH_ArkUI_SurfaceHolder_AddSurfaceCallback(holder, callback);                // 注册SurfaceCallback回调
  20. // ...
  21. return nullptr;
  22. }
  ```
* 通过ArkTS自定义组件节点来创建组件并结合XComponentController实现对Surface生命周期的管理。

  ```
  1. // 重写XComponentController，设置生命周期回调
  2. class MyXComponentController extends XComponentController {
  3. onSurfaceCreated(surfaceId: string): void {
  4. console.info(`onSurfaceCreated surfaceId: ${surfaceId}`);
  5. }

  7. onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void {
  8. console.info(`onSurfaceChanged surfaceId: ${surfaceId}, rect: ${JSON.stringify(rect)}}`);
  9. }

  11. onSurfaceDestroyed(surfaceId: string): void {
  12. console.info(`onSurfaceDestroyed surfaceId: ${surfaceId}`);
  13. }
  14. }

  16. class MyNodeController extends NodeController {
  17. public xComponent: typeNode.XComponent | undefined = undefined;
  18. public xComponentId: string = 'xcp' + (new Date().getTime());
  19. public node: FrameNode | undefined = undefined;
  20. public column: typeNode.Column | undefined = undefined;
  21. private xcController: MyXComponentController = new MyXComponentController();

  23. makeNode(uiContext: UIContext): FrameNode | null {
  24. this.node = new FrameNode(uiContext);
  25. this.column = typeNode.createNode(uiContext, 'Column')
  26. this.column.initialize()
  27. .width('100%')
  28. .height('100%')
  29. try {
  30. this.node.appendChild(this.column);
  31. } catch (error) {
  32. console.error('Fail to append child: ', error);
  33. }
  34. // 创建XComponent组件节点，并绑定XComponentController
  35. this.xComponent =
  36. typeNode.createNode(uiContext, 'XComponent', { type: XComponentType.SURFACE, controller: this.xcController });
  37. this.xComponent.attribute
  38. try {
  39. this.column.appendChild(this.xComponent);
  40. } catch (error) {
  41. console.error('Fail to append child: ', error);
  42. }
  43. return this.node;
  44. }
  45. }
  ```
* 通过ArkTS自定义组件节点来创建组件并结合OH\_ArkUI\_SurfaceHolder实现对Surface生命周期的管理。

  ```
  1. import native from 'libnativerender.so';
  2. import { FrameNode, NodeController, typeNode, UIContext } from '@kit.ArkUI';

  4. class MyNodeController extends NodeController {
  5. // ...

  7. makeNode(uiContext: UIContext): FrameNode | null {
  8. // ...
  9. // 创建XComponent组件节点
  10. this.xComponent = typeNode.createNode(uiContext, 'XComponent', { type: XComponentType.SURFACE });
  11. this.xComponent.attribute
  12. .id(this.xComponentId)
  13. .focusable(true)
  14. .focusOnTouch(true)
  15. native.bindNode(this.xComponentId, this.xComponent) // 跨语言调用至Native侧绑定Surface生命周期回调
  16. // ...
  17. }

  19. // ...
  20. }

  22. // ...

  24. @Component
  25. export struct SurfaceHolderTypeNode {
  26. // ...
  27. myNodeController: MyNodeController = new MyNodeController();

  29. build() {
  30. NavDestination() {
  31. Column() {
  32. // ...
  33. Column() {
  34. if (this.isShow) {
  35. NodeContainer(this.myNodeController)
  36. .width(200)
  37. .height(200)
  38. .focusable(true)
  39. .focusOnTouch(true)
  40. .defaultFocus(true)
  41. }
  42. }.height(200)
  43. // ...
  44. }
  45. .width('100%')
  46. }
  47. }
  48. }
  ```

  Native侧绑定Surface生命周期回调的具体实现。

  ```
  1. napi_value PluginManager::BindNode(napi_env env, napi_callback_info info)
  2. {
  3. size_t argc = 2;
  4. napi_value args[2] = {nullptr};
  5. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
  6. std::string nodeId = value2String(env, args[0]);
  7. ArkUI_NodeHandle handle;
  8. OH_ArkUI_GetNodeHandleFromNapiValue(env, args[1], &handle);             // 获取nodeHandle
  9. OH_ArkUI_SurfaceHolder *holder = OH_ArkUI_SurfaceHolder_Create(handle); // 获取SurfaceHolder
  10. nodeHandleMap_[nodeId] = handle;
  11. surfaceHolderMap_[handle] = holder;
  12. auto callback = OH_ArkUI_SurfaceCallback_Create(); // 创建SurfaceCallback
  13. callbackMap_[holder] = callback;
  14. auto render = new EGLRender();
  15. OH_ArkUI_SurfaceHolder_SetUserData(holder, render);                                // 将render保存在holder中
  16. OH_ArkUI_SurfaceCallback_SetSurfaceCreatedEvent(callback, OnSurfaceCreatedNative); // 注册OnSurfaceCreated回调
  17. OH_ArkUI_SurfaceCallback_SetSurfaceChangedEvent(callback, OnSurfaceChangedNative); // 注册OnSurfaceChanged回调
  18. OH_ArkUI_SurfaceCallback_SetSurfaceDestroyedEvent(callback, OnSurfaceDestroyedNative); // 注册OnSurfaceDestroyed回调
  19. OH_ArkUI_SurfaceHolder_AddSurfaceCallback(holder, callback);                // 注册SurfaceCallback回调
  20. return nullptr;
  21. }
  ```
* 通过NDK接口来创建组件并使用OH\_ArkUI\_SurfaceHolder实现对Surface生命周期的管理。

  ```
  1. @Component
  2. export struct SurfaceHolderNDK {
  3. @State currentStatus: string = 'init';
  4. private nodeContent: NodeContent = new NodeContent();

  6. aboutToAppear(): void {
  7. nativeNode.createNativeNode(this.nodeContent, 'SurfaceHolderNDK');
  8. this.currentStatus = 'index'
  9. }

  11. build() {
  12. NavDestination() {
  13. Column() {
  14. // ...
  15. Column({ space: 10 }) {
  16. ContentSlot(this.nodeContent);
  17. // ...
  18. }
  19. // ...
  20. }
  21. .width('100%')
  22. .height('100%')
  23. }
  24. }
  25. }
  ```

  Native侧createNativeNode可以参照如下代码实现。

  ```
  1. napi_value PluginManager::createNativeNode(napi_env env, napi_callback_info info)
  2. {
  3. // ...
  4. ArkUI_NodeContentHandle nodeContentHandle_ = nullptr;
  5. OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &nodeContentHandle_);
  6. nodeAPI = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
  7. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
  8. std::string tag = value2String(env, args[1]);
  9. // ...
  10. if (nodeAPI != nullptr && nodeAPI->createNode != nullptr && nodeAPI->addChild != nullptr) {
  11. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "PluginManager", "CreateNativeNode tag=%{public}s",
  12. tag.c_str());
  13. auto nodeContentEvent = [](ArkUI_NodeContentEvent *event) {
  14. ArkUI_NodeContentHandle handle = OH_ArkUI_NodeContentEvent_GetNodeContentHandle(event);
  15. std::string *userData = reinterpret_cast<std::string *>(OH_ArkUI_NodeContent_GetUserData(handle));
  16. if (!userData) {
  17. return;
  18. }
  19. if (OH_ArkUI_NodeContentEvent_GetEventType(event) != NODE_CONTENT_EVENT_ON_ATTACH_TO_WINDOW) {
  20. return;
  21. }
  22. ArkUI_NodeHandle testNode;
  23. if (userData->find("SurfaceHolder") == std::string::npos) {
  24. // ...
  25. } else {
  26. // 创建XComponent组件并使用SurfaceHolder管理Surface生命周期
  27. testNode = CreateNodeHandleUsingSurfaceHolder(*userData);
  28. }
  29. delete userData;
  30. userData = nullptr;
  31. OH_ArkUI_NodeContent_AddNode(handle, testNode);
  32. };
  33. OH_ArkUI_NodeContent_RegisterCallback(nodeContentHandle_, nodeContentEvent);
  34. }
  35. return nullptr;
  36. }
  ```

  创建XComponent组件并使用SurfaceHolder管理Surface生命周期的实现如下。

  ```
  1. ArkUI_NodeHandle CreateNodeHandleUsingSurfaceHolder(const std::string &tag)
  2. {
  3. ArkUI_NodeHandle column = nodeAPI->createNode(ARKUI_NODE_COLUMN);
  4. // ...
  5. xc = nodeAPI->createNode(ARKUI_NODE_XCOMPONENT); // 创建XComponent节点
  6. // ...
  7. OH_ArkUI_SurfaceHolder *holder = OH_ArkUI_SurfaceHolder_Create(xc); // 获取SurfaceHolder
  8. PluginManager::surfaceHolderMap_[xc] = holder;
  9. PluginManager::nodeHandleMap_[tag] = xc;
  10. auto callback = OH_ArkUI_SurfaceCallback_Create(); // 创建SurfaceCallback
  11. PluginManager::callbackMap_[holder] = callback;
  12. auto render = new EGLRender();
  13. OH_ArkUI_SurfaceHolder_SetUserData(holder, render);                                // 将render保存在holder中
  14. OH_ArkUI_SurfaceCallback_SetSurfaceCreatedEvent(callback, OnSurfaceCreatedNative); // 注册OnSurfaceCreated回调
  15. OH_ArkUI_SurfaceCallback_SetSurfaceChangedEvent(callback, OnSurfaceChangedNative); // 注册OnSurfaceChanged回调
  16. OH_ArkUI_SurfaceCallback_SetSurfaceDestroyedEvent(callback, OnSurfaceDestroyedNative); // 注册OnSurfaceDestroyed回调
  17. OH_ArkUI_SurfaceHolder_AddSurfaceCallback(holder, callback); // 添加SurfaceCallback回调
  18. if (!nodeAPI->addNodeEventReceiver(xc, onEvent)) {           // 添加事件监听，返回成功码 0
  19. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "onBind", "addNodeEventReceiver error");
  20. }
  21. if (!nodeAPI->registerNodeEvent(xc, NODE_TOUCH_EVENT, 0, nullptr)) { // 用C接口注册touch事件，返回成功码 0
  22. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "onBind", "registerTouchEvent error");
  23. }
  24. nodeAPI->addChild(column, xc); // 将XComponent挂载到Column下
  25. return column;
  26. }
  ```

## OH\_NativeXComponent向OH\_ArkUI\_SurfaceHolder的迁移

从API version 8开始，开发者可以通过基于[OH\_NativeXComponent](../harmonyos-references/vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例相关的接口进行XComponent组件Surface的生命周期监听、获取NativeWindow实例以及监听基础事件，实现渲染绘制和响应交互功能。但使用OH\_NativeXComponent相关的接口存在以下问题：

* OH\_NativeXComponent实例生命周期与XComponent组件强相关，开发者如果在XComponent组件销毁后仍然操作该对象将可能出现稳定性问题，造成应用的崩溃。
* OH\_NativeXComponent提供的交互事件接口不够丰富，只提供基础的触摸、鼠标、键盘交互接口，开发者若想识别长按、拖拽等高级手势需要自己写识别逻辑。

基于上述问题，建议使用OH\_ArkUI\_SurfaceHolder相关接口代替OH\_NativeXComponent相关接口，以下以使用ArkTS声明式UI描述创建组件为例，介绍如何将使用OH\_NativeXComponent管理Surface生命周期切换为使用OH\_ArkUI\_SurfaceHolder管理Surface生命周期。

### 组件创建

组件创建过程中的主要差异在于使用OH\_NativeXComponent需要传入id和libraryname属性以支持在Native侧获取对应的OH\_NativeXComponent实例；而使用OH\_ArkUI\_SurfaceHolder管理Surface生命周期的XComponent不再需要在XComponent的构造参数中传入id和libraryname属性，而是直接将组件对应的FrameNode节点传递至Native侧进行生命周期绑定和其他设置。

* OH\_NativeXComponent

  ```
  1. XComponent({
  2. id: 'xcomponentId',
  3. type: XComponentType.SURFACE,
  4. libraryname: 'nativerender' // 利用id和libraryname属性在Native侧获取NativeXcomponent并绑定Surface生命周期
  5. })
  6. .onLoad((xComponentContext) => {
  7. this.xComponentContext = xComponentContext as XComponentContext;
  8. this.currentStatus = 'index';
  9. })
  10. .onDestroy(() => {
  11. console.info('onDestroy');
  12. })
  13. .id('xcomponent')
  ```
* OH\_ArkUI\_SurfaceHolder

  ```
  1. XComponent({
  2. type: XComponentType.SURFACE,
  3. })
  4. .id('XComponentSurfaceHolder')
  5. .onAttach(() => {
  6. this.xcNode = this.getUIContext().getAttachedFrameNodeById('XComponentSurfaceHolder');
  7. if (!this.xcNode) {
  8. return;
  9. }
  10. native.bindNode('XComponentSurfaceHolder', this.xcNode); // 跨语言调用至Native侧获取SurfaceHolder并绑定Surface生命周期回调
  11. this.currentStatus = 'index';
  12. })
  13. .onDetach(() => {
  14. native.unbindNode('XComponentSurfaceHolder');
  15. this.xcNode = null;
  16. })
  ```

### 绑定Surface生命周期

绑定Surface生命周期中的主要差异在于注册生命周期回调的接口不同，具体回调内执行的逻辑基本保持不变。

* OH\_NativeXComponent

  ```
  1. void PluginManager::Export(napi_env env, napi_value exports)
  2. {
  3. if ((env == nullptr) || (exports == nullptr)) {
  4. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "PluginManager", "Export: env or exports is null");
  5. return;
  6. }

  8. napi_value exportInstance = nullptr;
  9. // 利用OH_NATIVE_XCOMPONENT_OBJ字段获取NativeXComponent实例
  10. if (napi_get_named_property(env, exports, OH_NATIVE_XCOMPONENT_OBJ, &exportInstance) != napi_ok) {
  11. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "PluginManager", "Export: napi_get_named_property fail");
  12. return;
  13. }

  15. OH_NativeXComponent *nativeXComponent = nullptr;
  16. if (napi_unwrap(env, exportInstance, reinterpret_cast<void **>(&nativeXComponent)) != napi_ok) {
  17. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "PluginManager", "Export: napi_unwrap fail");
  18. return;
  19. }

  21. char idStr[OH_XCOMPONENT_ID_LEN_MAX + 1] = {'\0'};
  22. uint64_t idSize = OH_XCOMPONENT_ID_LEN_MAX + 1;
  23. // 从NativeXComponent实例中获取id属性用来和ArkTS侧的XComponent组件一一对应
  24. if (OH_NativeXComponent_GetXComponentId(nativeXComponent, idStr, &idSize) != OH_NATIVEXCOMPONENT_RESULT_SUCCESS) {
  25. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "PluginManager",
  26. "Export: OH_NativeXComponent_GetXComponentId fail");
  27. return;
  28. }

  30. std::string id(idStr);
  31. auto context = PluginManager::GetInstance();
  32. if ((context != nullptr) && (nativeXComponent != nullptr)) {
  33. context->SetNativeXComponent(id, nativeXComponent);
  34. auto render = context->GetRender(id);
  35. if (render != nullptr) {
  36. // 注册Surface生命周期
  37. render->RegisterCallback(nativeXComponent);
  38. render->Export(env, exports);
  39. }
  40. }
  41. }
  ```

  注册Surface生命周期。

  ```
  1. void PluginRender::RegisterCallback(OH_NativeXComponent* nativeXComponent)
  2. {
  3. renderCallback_.OnSurfaceCreated = OnSurfaceCreatedCB;
  4. renderCallback_.OnSurfaceChanged = OnSurfaceChangedCB;
  5. renderCallback_.OnSurfaceDestroyed = OnSurfaceDestroyedCB;
  6. // ...
  7. OH_NativeXComponent_RegisterCallback(nativeXComponent, &renderCallback_);
  8. // ...
  9. }
  ```
* OH\_ArkUI\_SurfaceHolder

  ```
  1. napi_value PluginManager::BindNode(napi_env env, napi_callback_info info)
  2. {
  3. size_t argc = 2;
  4. napi_value args[2] = {nullptr};
  5. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
  6. std::string nodeId = value2String(env, args[0]);
  7. ArkUI_NodeHandle handle;
  8. OH_ArkUI_GetNodeHandleFromNapiValue(env, args[1], &handle);             // 获取nodeHandle
  9. OH_ArkUI_SurfaceHolder *holder = OH_ArkUI_SurfaceHolder_Create(handle); // 获取SurfaceHolder
  10. nodeHandleMap_[nodeId] = handle;
  11. surfaceHolderMap_[handle] = holder;
  12. auto callback = OH_ArkUI_SurfaceCallback_Create(); // 创建SurfaceCallback
  13. callbackMap_[holder] = callback;
  14. auto render = new EGLRender();
  15. OH_ArkUI_SurfaceHolder_SetUserData(holder, render);                                // 将render保存在holder中
  16. OH_ArkUI_SurfaceCallback_SetSurfaceCreatedEvent(callback, OnSurfaceCreatedNative); // 注册OnSurfaceCreated回调
  17. OH_ArkUI_SurfaceCallback_SetSurfaceChangedEvent(callback, OnSurfaceChangedNative); // 注册OnSurfaceChanged回调
  18. OH_ArkUI_SurfaceCallback_SetSurfaceDestroyedEvent(callback, OnSurfaceDestroyedNative); // 注册OnSurfaceDestroyed回调
  19. OH_ArkUI_SurfaceHolder_AddSurfaceCallback(holder, callback);                // 注册SurfaceCallback回调
  20. // ...
  21. return nullptr;
  22. }
  ```

### 获取NativeWindow方式

获取NativeWindow方式的差异如下：

* OH\_NativeXComponent

  在OnSurfaceCreated等生命周期回调返回的参数(即下面的void \*window)中获取。

  ```
  1. void OnSurfaceCreatedCB(OH_NativeXComponent *component, void *window)
  2. {
  3. // ...
  4. }
  5. void OnSurfaceChangedCB(OH_NativeXComponent *component, void *window)
  6. {
  7. // ...
  8. }
  9. void OnSurfaceDestroyedCB(OH_NativeXComponent *component, void *window)
  10. {
  11. // ...
  12. }
  13. void DispatchTouchEventCB(OH_NativeXComponent *component, void *window)
  14. {
  15. // ...
  16. }
  ```
* OH\_ArkUI\_SurfaceHolder

  调用OH\_ArkUI\_XComponent\_GetNativeWindow接口从OH\_ArkUI\_SurfaceHolder中获取。

  ```
  1. void OnSurfaceCreatedNative(OH_ArkUI_SurfaceHolder *holder)
  2. {
  3. auto window = OH_ArkUI_XComponent_GetNativeWindow(holder); // 获取native window
  4. // ...
  5. }
  ```

### 监听交互事件

使用OH\_NativeXComponent方式进行交互事件的监听，只能使用OH\_NativeXComponent上相关的接口监听触摸、鼠标、按键等基础事件。而使用OH\_ArkUI\_SurfaceHolder相关的接口，除监听基础事件外还能监听长按、拖拽等高级手势。

* OH\_NativeXComponent

  ```
  1. renderCallback_.DispatchTouchEvent = DispatchTouchEventCB; // 注册触摸事件
  2. OH_NativeXComponent_RegisterCallback(nativeXComponent, &renderCallback_);
  3. mouseCallback_.DispatchMouseEvent = DispatchMouseEventCB;
  4. mouseCallback_.DispatchHoverEvent = DispatchHoverEventCB;
  5. OH_NativeXComponent_RegisterMouseEventCallback(nativeXComponent, &mouseCallback_); // 注册鼠标事件

  7. OH_NativeXComponent_RegisterFocusEventCallback(nativeXComponent, OnFocusEventCB); // 注册获焦事件
  8. OH_NativeXComponent_RegisterKeyEventCallback(nativeXComponent, OnKeyEventCB);  // 注册按键事件
  9. OH_NativeXComponent_RegisterBlurEventCallback(nativeXComponent, OnBlurEventCB); // 注册失焦事件
  ```
* OH\_ArkUI\_SurfaceHolder

  以下只以注册touch事件为例，鼠标、按键以及更多的手势请参考[监听组件事件](ndk-listen-to-component-events.md)。

  ```
  1. if (!nodeAPI->addNodeEventReceiver(handle, onEvent)) { // 添加事件监听，返回成功码 0
  2. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "onBind", "addNodeEventReceiver error");
  3. }
  4. if (!nodeAPI->registerNodeEvent(handle, NODE_TOUCH_EVENT, 0, nullptr)) { // 用C接口注册touch事件，返回成功码 0
  5. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "onBind", "registerTouchEvent error");
  6. }
  ```

## 开发示例

### 在Native侧使用NativeWindow进行渲染绘制

以下展示完整使用NativeWindow和EGL接口进行自绘制的示例，主要开发场景如下：

* 在ArkTS侧创建的XComponent组件可以将其对应的FrameNode节点传递到Native侧以获取ArkUI\_NodeHandle，或者在Native侧直接创建XComponent组件对应的ArkUI\_NodeHandle，然后调用OH\_ArkUI\_SurfaceHolder\_Create接口创建OH\_ArkUI\_SurfaceHolder实例。
* 基于OH\_ArkUI\_SurfaceHolder实例注册相应的生命周期回调，获取NativeWindow实例。
* 利用NativeWindow和EGL接口开发自定义绘制内容，并申请提交Buffer到图形队列。
* XComponent组件相关的无障碍、可变帧率等能力根据ArkUI\_NodeHandle通过相关接口来实现。
* XComponent组件上的基础事件（如点击、触摸）和手势事件（如滑动、缩放）可通过ArkUI\_NodeHandle对象使用ArkUI NDK接口来监听，具体可参考[监听组件事件](ndk-listen-to-component-events.md)。

**接口说明**

| 接口名 | 描述 |
| --- | --- |
| OH\_ArkUI\_QueryModuleInterfaceByName(ArkUI\_NativeAPIVariantKind type, const char\* structName) | 获取指定类型的Native模块接口集合。 |
| OH\_ArkUI\_XComponent\_GetNativeWindow(OH\_ArkUI\_SurfaceHolder\* surfaceHolder) | 获取与OH\_ArkUI\_SurfaceHolder实例关联的nativeWindow。 |
| OH\_ArkUI\_SurfaceHolder\_RemoveSurfaceCallback(OH\_ArkUI\_SurfaceHolder\* surfaceHolder, OH\_ArkUI\_SurfaceCallback\* callback) | 从OH\_ArkUI\_SurfaceHolder实例中移除先前添加的Surface生命周期回调。 |
| OH\_ArkUI\_SurfaceCallback\_Dispose(OH\_ArkUI\_SurfaceCallback\* callback) | 释放OH\_ArkUI\_SurfaceCallback对象。 |
| OH\_ArkUI\_SurfaceHolder\_Dispose(OH\_ArkUI\_SurfaceHolder\* surfaceHolder) | 释放OH\_ArkUI\_SurfaceHolder对象。 |
| OH\_ArkUI\_NodeEvent\_GetEventType(ArkUI\_NodeEvent\* event) | 从组件事件获取事件类型。 |
| OH\_ArkUI\_NodeEvent\_GetNodeHandle(ArkUI\_NodeEvent\* event) | 获取触发组件事件的组件对象。 |
| OH\_ArkUI\_GetNodeHandleFromNapiValue(napi\_env env, napi\_value frameNode, ArkUI\_NodeHandle\* handle) | 获取ArkTS侧创建的FrameNode节点对象映射到Native侧的ArkUI\_NodeHandle。 |
| OH\_ArkUI\_SurfaceHolder\_Create(ArkUI\_NodeHandle node) | 从XComponent节点创建一个OH\_ArkUI\_SurfaceHolder对象。 |
| OH\_ArkUI\_SurfaceCallback\_Create() | 创建一个OH\_ArkUI\_SurfaceCallback对象。 |
| OH\_ArkUI\_SurfaceCallback\_SetSurfaceCreatedEvent(OH\_ArkUI\_SurfaceCallback\* callback, void (\*onSurfaceCreated)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder)) | 往OH\_ArkUI\_SurfaceCallback对象中注册onSurfaceCreated回调。 |
| OH\_ArkUI\_SurfaceCallback\_SetSurfaceChangedEvent(OH\_ArkUI\_SurfaceCallback\* callback, void (\*onSurfaceChanged)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder, uint64\_t width, uint64\_t height)) | 往OH\_ArkUI\_SurfaceCallback对象中注册onSurfaceChanged回调。 |
| OH\_ArkUI\_SurfaceCallback\_SetSurfaceDestroyedEvent(OH\_ArkUI\_SurfaceCallback\* callback, void (\*onSurfaceDestroyed)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder)) | 往OH\_ArkUI\_SurfaceCallback对象中注册onSurfaceDestroyed回调。 |
| OH\_ArkUI\_SurfaceCallback\_SetSurfaceShowEvent(OH\_ArkUI\_SurfaceCallback\* callback, void (\*onSurfaceShow)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder)) | 往OH\_ArkUI\_SurfaceCallback对象中注册onSurfaceShow回调。 |
| OH\_ArkUI\_SurfaceCallback\_SetSurfaceHideEvent(OH\_ArkUI\_SurfaceCallback\* callback, void (\*onSurfaceHide)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder)) | 往OH\_ArkUI\_SurfaceCallback对象中注册onSurfaceHide回调。 |
| OH\_ArkUI\_XComponent\_RegisterOnFrameCallback(ArkUI\_NodeHandle node, void (\*callback)(ArkUI\_NodeHandle node, uint64\_t timestamp, uint64\_t targetTimestamp)) | 为XComponent节点注册onFrame回调。 |
| OH\_ArkUI\_SurfaceHolder\_AddSurfaceCallback(OH\_ArkUI\_SurfaceHolder\* surfaceHolder, OH\_ArkUI\_SurfaceCallback\* callback) | 往OH\_ArkUI\_SurfaceHolder实例注册OH\_ArkUI\_SurfaceCallback对象。 |
| OH\_ArkUI\_AccessibilityProvider\_Create(ArkUI\_NodeHandle node) | 从XComponent节点创建一个ArkUI\_AccessibilityProvider对象。 |
| OH\_ArkUI\_XComponent\_UnregisterOnFrameCallback(ArkUI\_NodeHandle node) | 取消注册XComponent节点的onFrame回调。 |
| OH\_ArkUI\_AccessibilityProvider\_Dispose(ArkUI\_AccessibilityProvider\* provider) | 释放ArkUI\_AccessibilityProvider对象。 |
| OH\_ArkUI\_XComponent\_SetExpectedFrameRateRange(ArkUI\_NodeHandle node, OH\_NativeXComponent\_ExpectedRateRange range) | 为XComponent节点设置预期的帧率范围。 |
| OH\_ArkUI\_XComponent\_SetNeedSoftKeyboard(ArkUI\_NodeHandle node, bool needSoftKeyboard) | 设置XComponent节点在获得焦点时是否需要显示软键盘。 |

**开发步骤**

以下步骤通过在ArkTS侧创建SURFACE类型的XComponent为例（Native侧如何创建XComponent组件对应的ArkUI\_NodeHandle可参考[ArkUI\_NativeNodeAPI\_1](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md)），描述了如何使用XComponent组件调用OH\_ArkUI\_SurfaceHolder相关接口管理Surface生命周期，并在Native侧创建EGL/GLES环境，实现在主页面绘制图形，以及可以改变图形的颜色。

1. 在界面中定义XComponent。

   ```
   1. import native from 'libnativerender.so';
   2. import { common } from '@kit.AbilityKit';
   3. // ...
   4. @Component
   5. export struct PageThree {
   6. @State isShow: boolean = true;
   7. @State minRate: number = 0;
   8. @State maxRate: number = 120;
   9. @State expected: number = 60;
   10. needSoftKeyboard: boolean = false;
   11. @State needSoftKeyboardState: string = 'needSoftKeyboard=' + this.needSoftKeyboard;
   12. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   13. // 请将$r('app.string.pagethree_text1')替换为实际资源文件，在本示例中该资源文件的value值为"单指点击XComponent软键盘消失"
   14. @State text: ResourceStr = $r('app.string.pagethree_text1');
   15. controller: TextInputController = new TextInputController();
   16. myNodeController: MyNodeController = new MyNodeController();

   18. build() {
   19. NavDestination() {
   20. Column() {
   21. TextInput({ text: this.text, placeholder: 'please input ...', controller: this.controller })
   22. .id('textInput')
   23. .placeholderColor(Color.Grey)
   24. .placeholderFont({ size: 14, weight: 400 })
   25. .caretColor(Color.Blue)
   26. .width(400)
   27. .height(40)
   28. .margin(10)
   29. .fontSize(14)
   30. .fontColor(Color.Black)
   31. .onChange((value: string) => {
   32. this.text = value
   33. })
   34. Column() {
   35. if (this.isShow) {
   36. NodeContainer(this.myNodeController)
   37. .width(200)
   38. .height(200)
   39. .focusable(true)
   40. .focusOnTouch(true)
   41. .defaultFocus(true)
   42. }
   43. }.height(200)

   45. // 请将$r('app.string.pagethree_text2')替换为实际资源文件，在本示例中该资源文件的value值为"创建/销毁"
   46. Button($r('app.string.pagethree_text2')).onClick(() => {
   47. this.isShow = !this.isShow;
   48. }).width('50%')
   49. .margin({
   50. top: 10,
   51. bottom: 10,
   52. left: 12,
   53. right: 12
   54. })

   56. Column() {
   57. // 请将$r('app.string.pagethree_text3')替换为实际资源文件，在本示例中该资源文件的value值为"期望帧率设置："
   58. Text($r('app.string.pagethree_text3'))
   59. .textAlign(TextAlign.Start)
   60. .fontSize(15)
   61. .border({ width: 1 })
   62. .padding(10)
   63. .width('100%')
   64. .margin(5)
   65. Text('min: ' + this.minRate)
   66. Slider({
   67. value: this.minRate,
   68. min: 0,
   69. max: 240,
   70. step: 1
   71. }).onChange((value: number, mode: SliderChangeMode) => {
   72. this.minRate = value;
   73. native.setFrameRate(this.myNodeController.xComponentId, this.minRate, this.maxRate, this.expected)
   74. }).width('100%')
   75. .id('minSlider')
   76. Text('max: ' + this.maxRate)
   77. Slider({
   78. value: this.maxRate,
   79. min: 0,
   80. max: 240,
   81. step: 1
   82. }).onChange((value: number, mode: SliderChangeMode) => {
   83. this.maxRate = value;
   84. native.setFrameRate(this.myNodeController.xComponentId, this.minRate, this.maxRate, this.expected)
   85. }).width('100%')
   86. .id('maxSlider')
   87. Text('expected: ' + this.expected)
   88. Slider({
   89. value: this.expected,
   90. min: 0,
   91. max: 240,
   92. step: 1
   93. }).onChange((value: number, mode: SliderChangeMode) => {
   94. this.expected = value;
   95. native.setFrameRate(this.myNodeController.xComponentId, this.minRate, this.maxRate, this.expected)
   96. }).width('100%')
   97. .id('expectedSlider')
   98. }.backgroundColor('#F0FAFF')

   100. Button(this.needSoftKeyboardState)
   101. .onClick(() => {
   102. this.needSoftKeyboard = !this.needSoftKeyboard;
   103. this.needSoftKeyboardState = 'needSoftKeyboard=' + this.needSoftKeyboard;
   104. native.setNeedSoftKeyboard(this.myNodeController.xComponentId, this.needSoftKeyboard);
   105. // 请将$r('app.string.pagethree_text4')替换为实际资源文件，在本示例中该资源文件的value值为"单指点击XComponent软键盘不消失"
   106. // 请将$r('app.string.pagethree_text1')替换为实际资源文件，在本示例中该资源文件的value值为"单指点击XComponent软键盘消失"
   107. this.text = this.needSoftKeyboard ? $r('app.string.pagethree_text4') : $r('app.string.pagethree_text1')
   108. })
   109. .width('50%')
   110. .margin({
   111. top: 10,
   112. bottom: 10,
   113. left: 12,
   114. right: 12
   115. })
   116. // ...
   117. }
   118. .width('100%')
   119. }
   120. }
   121. }
   ```

   [PageThree.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeXComponentSample/entry/src/main/ets/pages/PageThree.ets#L15-L210)
2. Node-API模块注册，具体使用请参考[Node-API开发规范](napi-guidelines.md)。

   ```
   1. #include <hilog/log.h>

   3. #include "common/common.h"
   4. #include "manager/plugin_manager.h"

   6. namespace NativeXComponentSample {
   7. // 在napi_init.cpp文件中，Init方法注册接口函数，从而将封装的C++方法传递出来，供ArkTS侧调用
   8. EXTERN_C_START
   9. static napi_value Init(napi_env env, napi_value exports)
   10. {
   11. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "Init", "Init begins");
   12. if ((env == nullptr) || (exports == nullptr)) {
   13. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "Init", "env or exports is null");
   14. return nullptr;
   15. }
   16. // 向ArkTS侧暴露接口
   17. napi_property_descriptor desc[] = {
   18. // ···
   19. {"bindNode", nullptr, PluginManager::BindNode, nullptr, nullptr, nullptr, napi_default, nullptr},
   20. {"unbindNode", nullptr, PluginManager::UnbindNode, nullptr, nullptr, nullptr, napi_default, nullptr},
   21. {"setFrameRate", nullptr, PluginManager::SetFrameRate, nullptr, nullptr, nullptr, napi_default, nullptr},
   22. {"setNeedSoftKeyboard", nullptr, PluginManager::SetNeedSoftKeyboard, nullptr, nullptr, nullptr, napi_default,
   23. nullptr},
   24. // ···
   25. };
   26. if (napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc) != napi_ok) {
   27. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "Init", "napi_define_properties failed");
   28. return nullptr;
   29. }
   30. PluginManager::GetInstance()->Export(env, exports);
   31. return exports;
   32. }
   33. EXTERN_C_END

   35. // 编写接口的描述信息，根据实际需要可以修改对应参数
   36. static napi_module nativerenderModule = { .nm_version = 1,
   37. .nm_flags = 0,
   38. .nm_filename = nullptr,
   39. // 入口函数
   40. .nm_register_func = Init, // 指定加载对应模块时的回调函数
   41. // 模块名称
   42. .nm_modname = "nativerender", // 指定模块名称，对于XComponent相关开发，这个名称必须和ArkTS侧XComponent中libraryname的值保持一致
   43. .nm_priv = ((void*)0),
   44. .reserved = { 0 } };

   46. // __attribute__((constructor))修饰的方法由系统自动调用，使用Node-API接口napi_module_register()传入模块描述信息进行模块注册
   47. extern "C" __attribute__((constructor)) void RegisterModule(void)
   48. {
   49. napi_module_register(&nativerenderModule);
   50. }
   51. } // namespace NativeXComponentSample
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeXComponentSample/entry/src/main/cpp/napi_init.cpp#L15-L88)
3. 注册XComponent生命周期、事件、无障碍和可变帧率回调，使用CAPI实现往XComponent注册回调函数。

   (1) 定义BindNode、UnbindNode、SetFrameRate、SetNeedSoftKeyboard方法，暴露到ArkTS侧的bindNode、unbindNode、setFrameRate、setNeedSoftKeyboard方法会执行该方法。

   ```
   1. // plugin_manager.h
   2. namespace NativeXComponentSample {
   3. // ···
   4. class PluginManager {
   5. public:
   6. // ···
   7. static napi_value BindNode(napi_env env, napi_callback_info info);
   8. static napi_value UnbindNode(napi_env env, napi_callback_info info);
   9. static napi_value SetFrameRate(napi_env env, napi_callback_info info);
   10. static napi_value SetNeedSoftKeyboard(napi_env env, napi_callback_info info);
   11. // ···

   13. public:
   14. // ···
   15. static std::unordered_map<std::string, ArkUI_NodeHandle> nodeHandleMap_;
   16. static std::unordered_map<void *, OH_ArkUI_SurfaceCallback *> callbackMap_;
   17. static std::unordered_map<void *, OH_ArkUI_SurfaceHolder *> surfaceHolderMap_;
   18. static ArkUI_AccessibilityProvider *provider_;
   19. };
   20. } // namespace NativeXComponentSample
   ```

   [plugin\_manager.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeXComponentSample/entry/src/main/cpp/manager/plugin_manager.h#L31-L107)

   ```
   1. // plugin_manager.cpp
   2. std::unordered_map<std::string, ArkUI_NodeHandle> PluginManager::nodeHandleMap_;
   3. std::unordered_map<void *, OH_ArkUI_SurfaceCallback *> PluginManager::callbackMap_;
   4. std::unordered_map<void *, OH_ArkUI_SurfaceHolder *> PluginManager::surfaceHolderMap_;
   5. ArkUI_AccessibilityProvider *PluginManager::provider_ = nullptr;
   6. ArkUI_NativeNodeAPI_1 *nodeAPI = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
   7. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
   8. // ···
   9. static std::string value2String(napi_env env, napi_value value)
   10. {
   11. size_t stringSize = 0;
   12. napi_get_value_string_utf8(env, value, nullptr, 0, &stringSize);
   13. std::string valueString;
   14. valueString.resize(stringSize);
   15. napi_get_value_string_utf8(env, value, &valueString[0], stringSize+1, &stringSize);
   16. return valueString;
   17. }
   18. // ···
   19. napi_value PluginManager::BindNode(napi_env env, napi_callback_info info)
   20. {
   21. size_t argc = 2;
   22. napi_value args[2] = {nullptr};
   23. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   24. std::string nodeId = value2String(env, args[0]);
   25. ArkUI_NodeHandle handle;
   26. OH_ArkUI_GetNodeHandleFromNapiValue(env, args[1], &handle);             // 获取nodeHandle
   27. OH_ArkUI_SurfaceHolder *holder = OH_ArkUI_SurfaceHolder_Create(handle); // 获取SurfaceHolder
   28. nodeHandleMap_[nodeId] = handle;
   29. surfaceHolderMap_[handle] = holder;
   30. auto callback = OH_ArkUI_SurfaceCallback_Create(); // 创建SurfaceCallback
   31. callbackMap_[holder] = callback;
   32. auto render = new EGLRender();
   33. OH_ArkUI_SurfaceHolder_SetUserData(holder, render); // 将render保存在holder中
   34. OH_ArkUI_SurfaceCallback_SetSurfaceCreatedEvent(callback, OnSurfaceCreatedNative);     // 注册OnSurfaceCreated回调
   35. OH_ArkUI_SurfaceCallback_SetSurfaceChangedEvent(callback, OnSurfaceChangedNative);     // 注册OnSurfaceChanged回调
   36. OH_ArkUI_SurfaceCallback_SetSurfaceDestroyedEvent(callback, OnSurfaceDestroyedNative); // 注册OnSurfaceDestroyed回调
   37. OH_ArkUI_SurfaceCallback_SetSurfaceShowEvent(callback, OnSurfaceShowNative);           // 注册OnSurfaceShow回调
   38. OH_ArkUI_SurfaceCallback_SetSurfaceHideEvent(callback, OnSurfaceHideNative);           // 注册OnSurfaceHide回调
   39. OH_ArkUI_XComponent_RegisterOnFrameCallback(handle, OnFrameCallbackNative);            // 注册OnFrameCallback回调
   40. OH_ArkUI_SurfaceHolder_AddSurfaceCallback(holder, callback);                     // 注册SurfaceCallback回调
   41. if (!nodeAPI->addNodeEventReceiver(handle, onEvent)) { // 添加事件监听，返回成功码 0
   42. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "onBind", "addNodeEventReceiver error");
   43. }
   44. if (!nodeAPI->registerNodeEvent(handle, NODE_TOUCH_EVENT, 0, nullptr)) { // 用C接口注册touch事件，返回成功码 0
   45. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "onBind", "registerTouchEvent error");
   46. }
   47. provider_ = OH_ArkUI_AccessibilityProvider_Create(handle); // 创建一个ArkUI_AccessibilityProvider类型的对象
   48. /**
   49. * 获取ArkUI_AccessibilityProvider后，如果注册无障碍回调函数请参考：
   50. * https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/ui/ndk-accessibility-xcomponent.md
   51. * **/
   52. return nullptr;
   53. }

   55. napi_value PluginManager::UnbindNode(napi_env env, napi_callback_info info)
   56. {
   57. size_t argc = 1;
   58. napi_value args[1] = {nullptr};
   59. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   60. std::string nodeId = value2String(env, args[0]);
   61. ArkUI_NodeHandle node;
   62. if (nodeHandleMap_.find(nodeId) == nodeHandleMap_.end()) {
   63. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "SetNeedSoftKeyboard", "nodeId not exit error");
   64. return nullptr;
   65. }
   66. node = nodeHandleMap_[nodeId];
   67. OH_ArkUI_XComponent_UnregisterOnFrameCallback(node); // 解注册帧回调
   68. OH_ArkUI_AccessibilityProvider_Dispose(provider_);   // 销毁ArkUI_AccessibilityProvider
   69. auto holder = surfaceHolderMap_[node];
   70. if (PluginManager::callbackMap_.count(holder)) {
   71. auto callback = PluginManager::callbackMap_[holder];
   72. OH_ArkUI_SurfaceHolder_RemoveSurfaceCallback(holder, callback); // 移除SurfaceCallback
   73. OH_ArkUI_SurfaceCallback_Dispose(callback);                     // 销毁surfaceCallback
   74. PluginManager::callbackMap_.erase(holder);
   75. }
   76. auto render = reinterpret_cast<EGLRender*>(OH_ArkUI_SurfaceHolder_GetUserData(holder));
   77. delete render; // 销毁EGLRender对象
   78. OH_ArkUI_SurfaceHolder_Dispose(holder); // 销毁surfaceHolder
   79. nodeAPI->disposeNode(node);             // 销毁nodeHandle
   80. nodeHandleMap_.erase(nodeId);
   81. return nullptr;
   82. }

   84. napi_value PluginManager::SetFrameRate(napi_env env, napi_callback_info info)
   85. {
   86. size_t argc = 4;
   87. napi_value args[4] = {nullptr};
   88. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   89. std::string nodeId = value2String(env, args[0]);
   90. auto node = nodeHandleMap_[nodeId];

   92. int32_t min = 0;
   93. napi_get_value_int32(env, args[FIRST_ARG], &min);

   95. int32_t max = 0;
   96. napi_get_value_int32(env, args[SECOND_ARG], &max);

   98. int32_t expected = 0;
   99. napi_get_value_int32(env, args[THIRD_ARG], &expected);
   100. OH_NativeXComponent_ExpectedRateRange range = {.min = min, .max = max, .expected = expected};
   101. OH_ArkUI_XComponent_SetExpectedFrameRateRange(node, range); // 设置期望帧率
   102. return nullptr;
   103. }

   105. napi_value PluginManager::SetNeedSoftKeyboard(napi_env env, napi_callback_info info)
   106. {
   107. size_t argc = 2;
   108. napi_value args[2] = {nullptr};
   109. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   110. std::string nodeId = value2String(env, args[0]);
   111. ArkUI_NodeHandle node;
   112. if (nodeHandleMap_.find(nodeId) == nodeHandleMap_.end()) {
   113. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "SetNeedSoftKeyboard", "nodeId not exit error");
   114. return nullptr;
   115. }
   116. node = nodeHandleMap_[nodeId];

   118. bool needSoftKeyboard = false;
   119. napi_get_value_bool(env, args[1], &needSoftKeyboard);
   120. OH_ArkUI_XComponent_SetNeedSoftKeyboard(node, needSoftKeyboard); // 设置是否需要软键盘
   121. return nullptr;
   122. }
   ```

   [plugin\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeXComponentSample/entry/src/main/cpp/manager/plugin_manager.cpp#L33-L656)

   (2) 定义Surface创建成功，发生改变，销毁和事件，可变帧率回调接口。

   ```
   1. void OnSurfaceCreatedNative(OH_ArkUI_SurfaceHolder *holder)
   2. {
   3. auto window = OH_ArkUI_XComponent_GetNativeWindow(holder); // 获取native window
   4. auto render = reinterpret_cast<EGLRender*>(OH_ArkUI_SurfaceHolder_GetUserData(holder));
   5. render->SetUpEGLContext(window); // 初始化egl环境
   6. }

   8. void OnSurfaceChangedNative(OH_ArkUI_SurfaceHolder *holder, uint64_t width, uint64_t height)
   9. {
   10. EGLRender* render = reinterpret_cast<EGLRender*>(OH_ArkUI_SurfaceHolder_GetUserData(holder));
   11. render->SetEGLWindowSize(width, height); // 设置绘制区域大小
   12. render->DrawStar(true);                  // 绘制五角星
   13. }

   15. void OnSurfaceDestroyedNative(OH_ArkUI_SurfaceHolder *holder)
   16. {
   17. OH_LOG_Print(LOG_APP, LOG_ERROR, 0xff00, "onBind", "on destroyed");
   18. EGLRender* render = reinterpret_cast<EGLRender*>(OH_ArkUI_SurfaceHolder_GetUserData(holder));
   19. render->DestroySurface();  // 销毁eglSurface相关资源
   20. }

   22. void OnSurfaceShowNative(OH_ArkUI_SurfaceHolder *holder)
   23. {
   24. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "onBind", "on surface show");
   25. }

   27. void OnSurfaceHideNative(OH_ArkUI_SurfaceHolder *holder)
   28. {
   29. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "onBind", "on surface hide");
   30. }

   32. void OnFrameCallbackNative(ArkUI_NodeHandle node, uint64_t timestamp, uint64_t targetTimestamp)
   33. {
   34. if (!PluginManager::surfaceHolderMap_.count(node)) {
   35. return;
   36. }
   37. static uint64_t count = 0;
   38. count++;
   39. // 在头文件plugin_manager.h中定义，FRAME_COUNT的值为50
   40. if (count % FRAME_COUNT == 0) {
   41. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "onBind", "OnFrameCallback count = %{public}ld", count);
   42. }
   43. }

   45. void onEvent(ArkUI_NodeEvent *event)
   46. {
   47. auto eventType = OH_ArkUI_NodeEvent_GetEventType(event); // 获取组件事件类型
   48. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "onBind", "on event");
   49. if (eventType == NODE_TOUCH_EVENT) {
   50. ArkUI_NodeHandle handle = OH_ArkUI_NodeEvent_GetNodeHandle(event); // 获取触发该事件的组件对象
   51. auto holder = PluginManager::surfaceHolderMap_[handle];
   52. EGLRender* render = reinterpret_cast<EGLRender*>(OH_ArkUI_SurfaceHolder_GetUserData(holder));
   53. render->DrawStar(false); // 绘制五角星
   54. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "onBind", "on touch");
   55. }
   56. }
   ```

   [plugin\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeXComponentSample/entry/src/main/cpp/manager/plugin_manager.cpp#L66-L123)
4. 初始化环境，包括初始化可用的EGLDisplay、确定可用的Surface配置、创建渲染区域Surface、创建并关联上下文等。

   ```
   1. // EGLConst.h
   2. #include <EGL/egl.h>
   3. #include <EGL/eglext.h>
   4. #include <GLES3/gl3.h>

   6. const unsigned int LOG_PRINT_DOMAIN = 0xFF00;

   8. /**
   9. * Program 错误
   10. */
   11. const GLuint PROGRAM_ERROR = 0;

   13. /**
   14. * 位置错误。
   15. */
   16. const GLint POSITION_ERROR = -1;

   18. /**
   19. * 默认x坐标。
   20. */
   21. const int DEFAULT_X_POSITION = 0;

   23. /**
   24. * 默认y坐标。
   25. */
   26. const int DEFAULT_Y_POSITION = 0;

   28. /**
   29. * Gl 红色默认值。
   30. */
   31. const GLfloat GL_RED_DEFAULT = 0.0;

   33. /**
   34. * Gl 绿色默认值。
   35. */
   36. const GLfloat GL_GREEN_DEFAULT = 0.0;

   38. /**
   39. * Gl 蓝色默认值。
   40. */
   41. const GLfloat GL_BLUE_DEFAULT = 0.0;

   43. /**
   44. * Gl 透明度。
   45. */
   46. const GLfloat GL_ALPHA_DEFAULT = 1.0;

   48. /**
   49. * Pointer 数量。
   50. */
   51. const GLint POINTER_SIZE = 2;

   53. /**
   54. * Triangle fan 尺寸。
   55. */
   56. const GLsizei TRIANGLE_FAN_SIZE = 4;

   58. /**
   59. * 50%。
   60. */
   61. const float FIFTY_PERCENT = 0.5;

   63. /**
   64. * 位置句柄名字。
   65. */
   66. const char POSITION_NAME[] = "a_position";

   68. // ···

   70. /**
   71. * 背景色 #f4f4f4.
   72. */
   73. const GLfloat BACKGROUND_COLOR[] = {244.0f / 255, 244.0f / 255, 244.0f / 255, 1.0f};

   75. // ···

   77. /**
   78. * Draw 颜色 #7E8FFB.
   79. */
   80. const GLfloat DRAW_COLOR[] = {126.0f / 255, 143.0f / 255, 251.0f / 255, 1.0f};

   82. /**
   83. * Change 颜色 #92D6CC.
   84. */
   85. const GLfloat CHANGE_COLOR[] = {146.0f / 255, 214.0f / 255, 204.0f / 255, 1.0f};

   87. /**
   88. * 背景区域。
   89. */
   90. const GLfloat BACKGROUND_RECTANGLE_VERTICES[] = {-1.0f, 1.0f, 1.0f, 1.0f, 1.0f, -1.0f, -1.0f, -1.0f};

   92. const EGLint ATTRIB_LIST[] = {
   93. // 键，值。
   94. EGL_SURFACE_TYPE, EGL_WINDOW_BIT, EGL_RED_SIZE, 8, EGL_GREEN_SIZE, 8, EGL_BLUE_SIZE, 8, EGL_ALPHA_SIZE, 8,
   95. EGL_RENDERABLE_TYPE, EGL_OPENGL_ES2_BIT,
   96. // 结束。
   97. EGL_NONE};

   99. const EGLint CONTEXT_ATTRIBS[] = {EGL_CONTEXT_CLIENT_VERSION, 2, EGL_NONE};

   101. /**
   102. * 顶点着色器
   103. */
   104. const char VERTEX_SHADER[] = "#version 300 es\n"
   105. "layout(location = 0) in vec4 a_position;\n"
   106. "layout(location = 1) in vec4 a_color;   \n"
   107. "out vec4 v_color;                       \n"
   108. "void main()                             \n"
   109. "{                                       \n"
   110. "   gl_Position = a_position;            \n"
   111. "   v_color = a_color;                   \n"
   112. "}                                       \n";

   114. /**
   115. * 片元着色器。
   116. */
   117. const char FRAGMENT_SHADER[] = "#version 300 es\n"
   118. "precision mediump float;                  \n"
   119. "in vec4 v_color;                          \n"
   120. "out vec4 fragColor;                       \n"
   121. "void main()                               \n"
   122. "{                                         \n"
   123. "   fragColor = v_color;                   \n"
   124. "}                                         \n";
   ```

   [EGLConst.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeXComponentSample/entry/src/main/cpp/render/EGLConst.h#L18-L158)

   ```
   1. // EGLRender.h
   2. #include "EGLConst.h"
   3. #include <EGL/egl.h>
   4. #include <EGL/eglext.h>
   5. #include <EGL/eglplatform.h>
   6. #include <GLES3/gl3.h>
   7. #include <string>

   9. class EGLRender {
   10. public:
   11. bool SetUpEGLContext(void *window);
   12. void SetEGLWindowSize(int width, int height);
   13. void DrawStar(bool drawColor);
   14. void DestroySurface();
   15. // ···

   17. std::string xcomponentId;
   18. EGLNativeWindowType eglWindow_;

   20. EGLDisplay eglDisplay_ = EGL_NO_DISPLAY;
   21. EGLConfig eglConfig_ = EGL_NO_CONFIG_KHR;
   22. EGLSurface eglSurface_ = EGL_NO_SURFACE;
   23. EGLContext eglContext_ = EGL_NO_CONTEXT;
   24. GLuint program_;
   25. int width_ = 0;
   26. int height_ = 0;

   28. private:
   29. GLint PrepareDraw();
   30. bool ExecuteDraw(GLint position, const GLfloat *color, const GLfloat shapeVertices[]);
   31. };
   ```

   [EGLRender.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeXComponentSample/entry/src/main/cpp/render/EGLRender.h#L18-L52)

   ```
   1. // EGLRender.cpp
   2. #include "EGLRender.h"
   3. #include "EGLConst.h"
   4. #include <EGL/egl.h>
   5. #include <EGL/eglext.h>
   6. #include <GLES3/gl3.h>
   7. #include <cmath>
   8. #include <cstdio>
   9. #include <algorithm>
   10. #include <hilog/log.h>
   11. #include <iostream>

   13. namespace {
   14. void Rotate2d(GLfloat centerX, GLfloat centerY, GLfloat *rotateX, GLfloat *rotateY, GLfloat theta)
   15. {
   16. GLfloat tempX = cos(theta) * (*rotateX - centerX) - sin(theta) * (*rotateY - centerY);
   17. GLfloat tempY = sin(theta) * (*rotateX - centerX) + cos(theta) * (*rotateY - centerY);
   18. *rotateX = tempX + centerX;
   19. *rotateY = tempY + centerY;
   20. }

   22. GLuint LoadShader(GLenum type, const char *shaderSrc)
   23. {
   24. if ((type <= 0) || (shaderSrc == nullptr)) {
   25. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender", "glCreateShader type or shaderSrc error");
   26. return PROGRAM_ERROR;
   27. }

   29. GLuint shader = glCreateShader(type);
   30. if (shader == 0) {
   31. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender", "glCreateShader unable to load shader");
   32. return PROGRAM_ERROR;
   33. }

   35. // The gl function has no return value.
   36. glShaderSource(shader, 1, &shaderSrc, nullptr);
   37. glCompileShader(shader);

   39. GLint compiled;
   40. glGetShaderiv(shader, GL_COMPILE_STATUS, &compiled);
   41. if (compiled != 0) {
   42. return shader;
   43. }

   45. GLint infoLen = 0;
   46. glGetShaderiv(shader, GL_INFO_LOG_LENGTH, &infoLen);
   47. if (infoLen <= 1) {
   48. glDeleteShader(shader);
   49. return PROGRAM_ERROR;
   50. }

   52. char *infoLog = (char *)malloc(sizeof(char) * (infoLen + 1));
   53. if (infoLog != nullptr) {
   54. memset(infoLog, 0, infoLen + 1);
   55. glGetShaderInfoLog(shader, infoLen, nullptr, infoLog);
   56. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender", "glCompileShader error = %s", infoLog);
   57. free(infoLog);
   58. infoLog = nullptr;
   59. }
   60. glDeleteShader(shader);
   61. return PROGRAM_ERROR;
   62. }

   64. // 创建program
   65. GLuint CreateProgram(const char *vertexShader, const char *fragShader)
   66. {
   67. if ((vertexShader == nullptr) || (fragShader == nullptr)) {
   68. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender",
   69. "createProgram: vertexShader or fragShader is null");
   70. return PROGRAM_ERROR;
   71. }

   73. GLuint vertex = LoadShader(GL_VERTEX_SHADER, vertexShader);
   74. if (vertex == PROGRAM_ERROR) {
   75. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender", "createProgram vertex error");
   76. return PROGRAM_ERROR;
   77. }

   79. GLuint fragment = LoadShader(GL_FRAGMENT_SHADER, fragShader);
   80. if (fragment == PROGRAM_ERROR) {
   81. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender", "createProgram fragment error");
   82. return PROGRAM_ERROR;
   83. }

   85. GLuint program = glCreateProgram();
   86. if (program == PROGRAM_ERROR) {
   87. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender", "createProgram program error");
   88. glDeleteShader(vertex);
   89. glDeleteShader(fragment);
   90. return PROGRAM_ERROR;
   91. }

   93. // 该gl函数没有返回值。
   94. glAttachShader(program, vertex);
   95. glAttachShader(program, fragment);
   96. glLinkProgram(program);

   98. GLint linked;
   99. glGetProgramiv(program, GL_LINK_STATUS, &linked);
   100. if (linked != 0) {
   101. glDeleteShader(vertex);
   102. glDeleteShader(fragment);
   103. return program;
   104. }

   106. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender", "createProgram linked error");
   107. GLint infoLen = 0;
   108. glGetProgramiv(program, GL_INFO_LOG_LENGTH, &infoLen);
   109. if (infoLen > 1) {
   110. char *infoLog = (char *)malloc(sizeof(char) * (infoLen + 1));
   111. memset(infoLog, 0, infoLen + 1);
   112. glGetProgramInfoLog(program, infoLen, nullptr, infoLog);
   113. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender", "glLinkProgram error = %s", infoLog);
   114. free(infoLog);
   115. infoLog = nullptr;
   116. }
   117. glDeleteShader(vertex);
   118. glDeleteShader(fragment);
   119. glDeleteProgram(program);
   120. return PROGRAM_ERROR;
   121. }
   122. } // namespace

   124. bool EGLRender::SetUpEGLContext(void *window)
   125. {
   126. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "EGLRender", "EglContextInit execute");
   127. eglWindow_ = (EGLNativeWindowType)(window);
   128. // 初始化display。
   129. eglDisplay_ = eglGetDisplay(EGL_DEFAULT_DISPLAY);
   130. if (eglDisplay_ == EGL_NO_DISPLAY) {
   131. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender", "eglGetDisplay: unable to get EGL display");
   132. return false;
   133. }
   134. EGLint majorVersion;
   135. EGLint minorVersion;
   136. if (!eglInitialize(eglDisplay_, &majorVersion, &minorVersion)) {
   137. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender",
   138. "eglInitialize: unable to get initialize EGL display");
   139. return false;
   140. };
   141. // 选择配置。
   142. const EGLint maxConfigSize = 1;
   143. EGLint numConfigs;
   144. if (!eglChooseConfig(eglDisplay_, ATTRIB_LIST, &eglConfig_, maxConfigSize, &numConfigs)) {
   145. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender", "eglChooseConfig: unable to choose configs");
   146. return false;
   147. };
   148. // 创建环境。
   149. // 创建 Surface。
   150. eglSurface_ = eglCreateWindowSurface(eglDisplay_, eglConfig_, eglWindow_, NULL);
   151. if (eglSurface_ == nullptr) {
   152. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender",
   153. "eglCreateWindowSurface: unable to create surface");
   154. return false;
   155. }
   156. if (eglSurface_ == nullptr) {
   157. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender",
   158. "eglCreateWindowSurface: unable to create surface");
   159. return false;
   160. }
   161. // 创建上下文。
   162. eglContext_ = eglCreateContext(eglDisplay_, eglConfig_, EGL_NO_CONTEXT, CONTEXT_ATTRIBS);
   163. if (!eglMakeCurrent(eglDisplay_, eglSurface_, eglSurface_, eglContext_)) {
   164. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender", "eglMakeCurrent failed");
   165. return false;
   166. }
   167. // 创建program。
   168. program_ = CreateProgram(VERTEX_SHADER, FRAGMENT_SHADER);
   169. if (program_ == PROGRAM_ERROR) {
   170. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender", "CreateProgram: unable to create program");
   171. return false;
   172. }
   173. return true;
   174. }

   176. GLint EGLRender::PrepareDraw()
   177. {
   178. if ((eglDisplay_ == nullptr) || (eglSurface_ == nullptr) || (eglContext_ == nullptr) ||
   179. (!eglMakeCurrent(eglDisplay_, eglSurface_, eglSurface_, eglContext_))) {
   180. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender", "PrepareDraw: param error");
   181. return POSITION_ERROR;
   182. }

   184. // 该gl函数没有返回值。
   185. glViewport(DEFAULT_X_POSITION, DEFAULT_Y_POSITION, width_, height_);
   186. glClearColor(GL_RED_DEFAULT, GL_GREEN_DEFAULT, GL_BLUE_DEFAULT, GL_ALPHA_DEFAULT);
   187. glClear(GL_COLOR_BUFFER_BIT);
   188. glUseProgram(program_);

   190. return glGetAttribLocation(program_, POSITION_NAME);
   191. }

   193. // 绘制五角星
   194. void EGLRender::DrawStar(bool drawColor)
   195. {
   196. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "EGLRender", "Draw");
   197. GLint position = PrepareDraw();
   198. if (position == POSITION_ERROR) {
   199. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender", "Draw get position failed");
   200. return;
   201. }

   203. // 绘制背景
   204. if (!ExecuteDraw(position, BACKGROUND_COLOR, BACKGROUND_RECTANGLE_VERTICES)) {
   205. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender", "Draw execute draw background failed");
   206. return;
   207. }

   209. // 将其划分为五个四边形，并计算其中一个四边形的顶点
   210. GLfloat rotateX = 0;
   211. GLfloat rotateY = FIFTY_PERCENT * height_;
   212. GLfloat centerX = 0;
   213. // 将角度 54° 和 18° 转换为弧度
   214. GLfloat centerY = -rotateY * (M_PI / 180 * 54) * (M_PI / 180 * 18);
   215. // 将角度 18° 转换为弧度
   216. GLfloat leftX = -rotateY * (M_PI / 180 * 18);
   217. GLfloat leftY = 0;
   218. // 将角度 18° 转换为弧度
   219. GLfloat rightX = rotateY * (M_PI / 180 * 18);
   220. GLfloat rightY = 0;

   222. // 确定绘制四边形的顶点，使用绘制区域的百分比表示
   223. const GLfloat shapeVertices[] = {centerX / width_, centerY / height_, leftX / width_,  leftY / height_,
   224. rotateX / width_, rotateY / height_, rightX / width_, rightY / height_};
   225. auto color = drawColor ? DRAW_COLOR : CHANGE_COLOR;
   226. if (!ExecuteDraw(position, color, shapeVertices)) {
   227. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender", "Draw execute draw shape failed");
   228. return;
   229. }

   231. // 将角度 72° 转换为弧度
   232. GLfloat rad = M_PI / 180 * 72;
   233. // 旋转四次。
   234. // 在头文件EGLConst.h中定义，NUM_0的值为0，NUM_4的值为4
   235. for (int i = NUM_0; i < NUM_4; ++i) {
   236. // 旋转得其他四个四边形的顶点
   237. Rotate2d(centerX, centerY, &rotateX, &rotateY, rad);
   238. Rotate2d(centerX, centerY, &leftX, &leftY, rad);
   239. Rotate2d(centerX, centerY, &rightX, &rightY, rad);

   241. // 确定绘制四边形的顶点，使用绘制区域的百分比表示
   242. const GLfloat shapeVertices[] = {centerX / width_, centerY / height_, leftX / width_,  leftY / height_,
   243. rotateX / width_, rotateY / height_, rightX / width_, rightY / height_};

   245. // 绘制图形
   246. if (!ExecuteDraw(position, color, shapeVertices)) {
   247. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender", "Draw execute draw shape failed");
   248. return;
   249. }
   250. }
   251. // 将绘制命令提交给GPU，GPU执行完成后将渲染结果显示到屏幕
   252. glFlush();
   253. glFinish();
   254. if (!eglSwapBuffers(eglDisplay_, eglSurface_)) {
   255. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender", "Draw FinishDraw failed");
   256. return;
   257. }
   258. }

   260. // ···

   262. bool EGLRender::ExecuteDraw(GLint position, const GLfloat *color, const GLfloat shapeVertices[])
   263. {
   264. if ((position > 0) || (color == nullptr)) {
   265. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLRender", "ExecuteDraw: param error");
   266. return false;
   267. }

   269. // 该gl函数没有返回值。
   270. glVertexAttribPointer(position, POINTER_SIZE, GL_FLOAT, GL_FALSE, 0, shapeVertices);
   271. glEnableVertexAttribArray(position);
   272. glVertexAttrib4fv(1, color);
   273. glDrawArrays(GL_TRIANGLE_FAN, 0, TRIANGLE_FAN_SIZE);
   274. glDisableVertexAttribArray(position);

   276. return true;
   277. }

   279. void EGLRender::SetEGLWindowSize(int width, int height)
   280. {
   281. width_ = width;
   282. height_ = height;
   283. }

   285. // 释放相关资源
   286. void EGLRender::DestroySurface()
   287. {
   288. if ((eglDisplay_ == nullptr) || (eglSurface_ == nullptr) || (!eglDestroySurface(eglDisplay_, eglSurface_))) {
   289. OH_LOG_Print(LOG_APP, LOG_ERROR, 0xff00, "EGLRender", "Release eglDestroySurface failed");
   290. }

   292. if ((eglDisplay_ == nullptr) || (eglContext_ == nullptr) || (!eglDestroyContext(eglDisplay_, eglContext_))) {
   293. OH_LOG_Print(LOG_APP, LOG_ERROR, 0xff00, "EGLRender", "Release eglDestroySurface failed");
   294. }

   296. if ((eglDisplay_ == nullptr) || (!eglTerminate(eglDisplay_))) {
   297. OH_LOG_Print(LOG_APP, LOG_ERROR, 0xff00, "EGLRender", "Release eglDestroySurface failed");
   298. }
   299. eglDisplay_ = EGL_NO_DISPLAY;
   300. eglSurface_ = EGL_NO_SURFACE;
   301. eglContext_ = EGL_NO_CONTEXT;
   302. }
   ```

   [EGLRender.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeXComponentSample/entry/src/main/cpp/render/EGLRender.cpp#L15-L335)
5. CMakeLists，使用CMake工具链将C++源代码编译成动态链接库文件。

   ```
   1. # the minimum version of CMake.
   2. cmake_minimum_required(VERSION 3.5.0)
   3. project(LCNXComponent2)

   5. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

   7. if(DEFINED PACKAGE_FIND_FILE)
   8. include(${PACKAGE_FIND_FILE})
   9. endif()

   11. include_directories(${NATIVERENDER_ROOT_PATH}
   12. ${NATIVERENDER_ROOT_PATH}/render
   13. ${NATIVERENDER_ROOT_PATH}/manager)

   15. add_library(nativerender SHARED
   16. render/EGLRender.cpp
   17. manager/plugin_manager.cpp
   18. napi_init.cpp)
   19. find_library(
   20. # 设置路径变量的名称。
   21. EGL-lib
   22. # 指定要让CMake查找的NDK库的名称。
   23. EGL
   24. )

   26. find_library(
   27. # 设置路径变量的名称。
   28. GLES-lib
   29. # 指定要让CMake查找的NDK库的名称。
   30. GLESv3
   31. )

   33. find_library(
   34. # 设置路径变量的名称。
   35. hilog-lib
   36. # 指定要让CMake查找的NDK库的名称。
   37. hilog_ndk.z
   38. )

   40. find_library(
   41. # 设置路径变量的名称。
   42. libace-lib
   43. # 指定要让CMake查找的NDK库的名称。
   44. ace_ndk.z
   45. )

   47. find_library(
   48. # 设置路径变量的名称。
   49. libnapi-lib
   50. # 指定要让CMake查找的NDK库的名称。
   51. ace_napi.z
   52. )

   54. find_library(
   55. # 设置路径变量的名称。
   56. libuv-lib
   57. # 指定要让CMake查找的NDK库的名称。
   58. uv
   59. )

   61. target_link_libraries(nativerender PUBLIC ${EGL-lib} ${GLES-lib} ${hilog-lib} ${libace-lib} ${libnapi-lib} ${libuv-lib} libnative_window.so)
   ```

   上述用例具体实现可参考[NativeXComponent](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/NativeXComponentSample)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/3TNJ-I3YSGuvcsXfJhrRYQ/zh-cn_image_0000002589244189.jpeg?HW-CC-KV=V1&HW-CC-Date=20260429T052751Z&HW-CC-Expire=86400&HW-CC-Sign=1DFB0510F1300394C41B3B75002FD793D9DE86F59146E0A2F737FD537DFE812A)

### 在ArkTS侧使用SurfaceId进行渲染绘制

完整使用SurfaceId进行渲染绘制的示例及其主要开发场景如下：

* 在ArkTS侧创建XComponent组件，并使用XComponentController来管理其持有的Surface生命周期。
* 在OnSurfaceCreated回调内获取surfaceId并将其传递给AVPlayer。
* 使用surfaceId初始化AVPlayer，并为其设置必要信息，实现视频的播放。

说明

更多AVPlayer用法请参考[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)。

**接口说明**

| 接口名 | 描述 |
| --- | --- |
| onSurfaceCreated(surfaceId: string): void | 当XComponent持有的Surface创建后进行该回调。 |

**开发步骤**

以下步骤展示如何在ArkTS侧创建SURFACE类型的XComponent，获取surfaceId，并将其设置给AVPlayer实现视频播放。

1. 创建XComponent并传入XComponentController。

   ```
   1. XComponent({ type: XComponentType.SURFACE, controller: this.videoXComponentController })
   ```

   [XComponentAVPlayer.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/VideoPlayer/entry/src/main/ets/pages/XComponentAVPlayer.ets#L127-L129)
2. 在XComponentController中注册onSurfaceCreated生命周期，并在其中获取surfaceId，将获取到的surfaceId和待播的视频源信息传递给AVPlayer。

   ```
   1. class VideoXComponentController extends XComponentController {
   2. private avPlayerController: AVPlayerController;

   4. constructor(avPlayerController: AVPlayerController) {
   5. super();
   6. this.avPlayerController = avPlayerController;
   7. }

   9. onSurfaceCreated(surfaceId: string): void {
   10. let source: VideoData = {
   11. type: VideoDataType.RAW_FILE,
   12. videoSrc: 'videoTest.mp4'
   13. };
   14. // 将surfaceId和视频源信息传递给AVPlayer
   15. this.avPlayerController.initAVPlayer(source, surfaceId);
   16. }
   17. }
   ```

   [XComponentAVPlayer.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/VideoPlayer/entry/src/main/ets/pages/XComponentAVPlayer.ets#L25-L43)
3. 初始化AVPlayer。

   ```
   1. public async initAVPlayer(source: VideoData, surfaceId: string) {
   2. this.curSource = source;
   3. if (source.seekTime) {
   4. this.seekTime = source.seekTime;
   5. }
   6. if (source.isMuted) {
   7. this.isMuted = source.isMuted;
   8. }
   9. if (!this.curSource) {
   10. return;
   11. }
   12. this.surfaceID = surfaceId; // 存储surfaceId
   13. try {
   14. this.avPlayer = await media.createAVPlayer();
   15. this.setAVPlayerCallback();
   16. // 根据不同的视频文件格式设置视频源
   17. switch (this.curSource.type) {
   18. case VideoDataType.RAW_FILE:
   19. let fileDescriptor = await this.context?.resourceManager.getRawFd(this.curSource.videoSrc);
   20. this.avPlayer.fdSrc = fileDescriptor;
   21. break;
   22. case VideoDataType.URL:
   23. this.avPlayer.url = this.curSource.videoSrc;
   24. break;
   25. case VideoDataType.RAW_M3U8_FILE:
   26. // ...
   27. case VideoDataType.RAW_MAP4_FILE:
   28. // ...
   29. default:
   30. break;
   31. }
   32. } catch (err) {
   33. hilog.error(CommonConstants.LOG_DOMAIN, TAG,
   34. `InitPlayer failed, code is ${err.code}, message is ${err.message}`);
   35. }
   36. }

   38. private setAVPlayerCallback() {
   39. if (!this.avPlayer) {
   40. return;
   41. }
   42. this.avPlayer.on('durationUpdate', (time: number) => {
   43. AppStorage.setOrCreate('DurationTime', time); // 更新视频总时长
   44. });
   45. this.avPlayer.on('timeUpdate', (time: number) => {
   46. this.currentTime = time; // 更新当前进度
   47. AppStorage.setOrCreate('CurrentTime', time);
   48. });
   49. this.avPlayer.on('error', (err: BusinessError) => {
   50. if (!this.avPlayer) {
   51. return;
   52. }
   53. hilog.error(CommonConstants.LOG_DOMAIN, TAG,
   54. `Invoke avPlayer failed, code is ${err.code}, message is ${err.message}`);
   55. this.avPlayer.reset().catch((err: BusinessError) => {
   56. hilog.error(CommonConstants.LOG_DOMAIN, TAG,
   57. `Reset failed, code is ${err.code}, message is ${err.message}`);
   58. });
   59. })
   60. this.setStateChangeCallback();
   61. }

   63. private setStateChangeCallback() {
   64. if (!this.avPlayer) {
   65. return;
   66. }
   67. this.avPlayer.on('stateChange', async (state) => {
   68. if (!this.avPlayer) {
   69. return;
   70. }
   71. switch (state) {
   72. case 'idle':
   73. hilog.info(CommonConstants.LOG_DOMAIN, TAG, `setAVPlayerCallback AVPlayer state idle called.`);
   74. break;
   75. case 'initialized':
   76. this.avPlayer.surfaceId = this.surfaceID; // 设置surfaceId，作为视频画面承载的画布
   77. this.avPlayer.prepare().catch((err: BusinessError) => {
   78. hilog.error(CommonConstants.LOG_DOMAIN, TAG,
   79. `prepare failed, code is ${err.code}, message is ${err.message}`);
   80. });
   81. break;
   82. case 'prepared':
   83. // ...
   84. // 实现自动播放
   85. this.avPlayer.play().catch((err: BusinessError) => {
   86. hilog.error(CommonConstants.LOG_DOMAIN, TAG, `play failed, code is ${err.code}, message is ${err.message}`);
   87. })
   88. break;
   89. case 'playing':
   90. this.isPlaying = true;
   91. break;
   92. case 'completed':
   93. this.currentTime = 0;
   94. break;
   95. default:
   96. break;
   97. }
   98. });
   99. }
   ```

   [AVPlayerController.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/VideoPlayer/entry/src/main/ets/avplayertool/AVPlayerController.ets#L42-L177)
