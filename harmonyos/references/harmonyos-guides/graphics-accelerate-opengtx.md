---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-opengtx
title: OpenGTX功能开发
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏渲染加速服务 > OpenGTX功能开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:897c46e48512534449a8b56bd4cb075717aa7e88fc9a976c93d41909ea413045
---

## 概述

OpenGTX是GPU Turbo X的开放式入口，根据游戏开发者主动提供的游戏过程中的关键信息，使能LTPO（动态帧率/刷新率）等游戏加速方案，助力游戏开发者打造高画质、高流畅、低功耗极致体验。LTPO通过动态感知游戏渲染状态、游戏场景、设备状态等关键信息，动态调整游戏的帧率/刷新率以及设备的SOC/DDR频率。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/yi3X6EsvQDuOE7EWKOez_g/zh-cn_image_0000002583438759.png?HW-CC-KV=V1&HW-CC-Date=20260427T234726Z&HW-CC-Expire=86400&HW-CC-Sign=77A573B659AAB2DD098662879EA5158E94F577ED962A98DB457D91A0C028FC18)

## 业务流程

LTPO的主要业务流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/9-_nIbU9RIC5beVmVhEhYg/zh-cn_image_0000002552958714.png?HW-CC-KV=V1&HW-CC-Date=20260427T234726Z&HW-CC-Expire=86400&HW-CC-Sign=BE6A84642EB6F8F2CC0B2B4CB9AF040CAB802D9E35F94D0B8AAA4C4AA4C8CE7A)

1. 用户进入游戏。
2. 游戏应用调用[HMS\_OpenGTX\_CreateContext](../harmonyos-references/_graphics_accelerate.md#hms_opengtx_createcontext)接口创建OpenGTX上下文实例。
3. 游戏应用调用[HMS\_OpenGTX\_SetConfiguration](../harmonyos-references/_graphics_accelerate.md#hms_opengtx_setconfiguration)接口初始化配置实例属性，包含LTPO模式、目标帧率、包名、游戏类型、分辨率、游戏关键线程等属性。
4. 游戏应用调用[HMS\_OpenGTX\_Activate](../harmonyos-references/_graphics_accelerate.md#hms_opengtx_activate)接口激活OpenGTX上下文实例。
5. 游戏切换不同游戏场景后调用[HMS\_OpenGTX\_DispatchGameSceneInfo](../harmonyos-references/_graphics_accelerate.md#hms_opengtx_dispatchgamesceneinfo)接口发送游戏场景信息，包含场景类型、指定帧率、调度帧率范围、当前分辨率等信息。
6. 游戏应用在每帧渲染前调用[HMS\_OpenGTX\_DispatchFrameRenderInfo](../harmonyos-references/_graphics_accelerate.md#hms_opengtx_dispatchframerenderinfo)接口发送游戏帧渲染信息，包含游戏主相机的位置和欧拉角。
7. 游戏应用在每帧渲染前如遇到网络时延档位变化，调用[HMS\_OpenGTX\_DispatchNetworkInfo](../harmonyos-references/_graphics_accelerate.md#hms_opengtx_dispatchnetworkinfo)接口发送游戏网络信息，包含服务器IP地址、网络时延等信息。
8. 游戏应用正常绘制。
9. 一帧送显。
10. 每帧结束，将帧尾决策帧率、决策设备频率通知到设备。
11. 用户退出游戏。
12. 游戏应用调用[HMS\_OpenGTX\_DestroyContext](../harmonyos-references/_graphics_accelerate.md#hms_opengtx_destroycontext)接口销毁OpenGTX上下文实例并释放内存资源。

## 开发步骤

本节介绍OpenGTX的开发接入，从流程上分别阐述每个步骤的实现和调用。详细代码请参考[OpenGTX Sample](https://gitcode.com/harmonyos_samples/open-gtx-samplecode-clientdemo-cpp)。

### 设置项目配置项

在“src/main/module.json5”的module层级中添加以下配置。

```
1. "metadata": [
2. {
3. "name": "GraphicsAccelerateKit_LTPO",
4. "value": "true"
5. }
6. ]
```

### 头文件引用

引用Graphics Accelerate Kit OpenGTX头文件：opengtx\_base.h。

```
1. // 引用OpenGTX头文件 opengtx_base.h
2. #include <graphics_game_sdk/opengtx_base.h>
```

### 编写CMakeLists.txt

```
1. find_library(
2. # Sets the name of the path variable.
3. opengtx-lib
4. # Specifies the name of the NDK library that you want CMake to locate.
5. libopengtx.so
6. )
7. find_library(
8. # Sets the name of the path variable.
9. GLES-lib
10. # Specifies the name of the NDK library that you want CMake to locate.
11. GLESv3
12. )
13. find_library(
14. # Sets the name of the path variable.
15. hilog-lib
16. # Specifies the name of the NDK library that you want CMake to locate.
17. hilog_ndk.z
18. )

20. target_link_libraries(entry PUBLIC
21. ${opengtx-lib} ${GLES-lib} ${hilog-lib}
22. )
```

### OpenGTX初始化

在surface创建后，会触发其事件回调函数Core::OnSurfaceCreated()，在该函数中完成OpenGTX上下文实例创建、OpenGTX属性配置和功能激活。其中OpenGTX上下文实例负责管理OpenGTX整个生命周期。

1. 调用[HMS\_OpenGTX\_CreateContext](../harmonyos-references/_graphics_accelerate.md#hms_opengtx_createcontext)接口创建OpenGTX上下文实例。如果返回nullptr，则说明OpenGTX上下文实例创建失败，或当前硬件设备不支持开启OpenGTX。

   ```
   1. // 创建OpenGTX上下文实例
   2. OpenGTX_Context *context_ = HMS_OpenGTX_CreateContext(nullptr);
   3. if (context_ == nullptr) {
   4. return false;
   5. }
   ```
2. 调用[HMS\_OpenGTX\_SetConfiguration](../harmonyos-references/_graphics_accelerate.md#hms_opengtx_setconfiguration)接口属性配置，包含LTPO模式、目标帧率、包名、游戏类型、分辨率、游戏关键线程等属性。

   ```
   1. // 初始化OpenGTX接口调用错误码
   2. OpenGTX_ErrorCode errorCode = OPENGTX_SUCCESS;
   3. // OpenGTX属性配置结构体
   4. OpenGTX_ConfigDescription config;
   5. // LTPO调度模式
   6. config.mode = ADAPTIVE_MODE;
   7. // 游戏设置目标帧率
   8. config.targetFPS = 120;
   9. // 游戏包名
   10. config.packageName = (char*)"OpenGTX";
   11. // 游戏版本
   12. config.appVersion = (char*)"1.1.0";
   13. // 引擎类型
   14. config.engineType = UNREAL;
   15. // 引擎版本
   16. config.engineVersion = (char*)"4.26.2";
   17. // 游戏类别
   18. config.gameType = RPG;
   19. // 游戏最高画质等级
   20. config.pictureQualityMaxLevel = HD;
   21. // 游戏设置最大分辨率
   22. config.resolutionMaxValue = OpenGTX_ResolutionValue { 1280, 720};
   23. // 游戏逻辑线程
   24. config.gameMainThreadId = 11;
   25. // 游戏渲染线程
   26. config.gameRenderThreadId = 11;
   27. // 游戏运行其他关键线程
   28. config.gameKeyThreadIds[0] = 0;
   29. config.gameKeyThreadIds[1] = 0;
   30. config.gameKeyThreadIds[2] = 0;
   31. config.gameKeyThreadIds[3] = 0;
   32. config.gameKeyThreadIds[4] = 0;
   33. // 游戏图形API是否为Vulkan
   34. config.vulkanSupport = false;
   35. // 初始化OpenGTX实例，配置OpenGTX属性
   36. errorCode = HMS_OpenGTX_SetConfiguration(context_, &config);
   37. if (errorCode != OPENGTX_SUCCESS) {
   38. return false;
   39. }
   ```
3. 调用[HMS\_OpenGTX\_Activate](../harmonyos-references/_graphics_accelerate.md#hms_opengtx_activate)接口激活OpenGTX上下文实例。

   ```
   1. // 激活OpenGTX上下文实例
   2. errorCode = HMS_OpenGTX_Activate(context_);
   3. if (errorCode != OPENGTX_SUCCESS) {
   4. return false;
   5. }
   ```
4. 调用[HMS\_OpenGTX\_Deactivate](../harmonyos-references/_graphics_accelerate.md#hms_opengtx_deactivate)接口去激活OpenGTX上下文实例。（在需要关闭OpenGTX功能时调用此接口。去激活后，调用[HMS\_OpenGTX\_DispatchGameSceneInfo](../harmonyos-references/_graphics_accelerate.md#hms_opengtx_dispatchgamesceneinfo)等接口将不会生效）。

   ```
   1. // 去激活OpenGTX上下文实例
   2. errorCode = HMS_OpenGTX_Deactivate(context_);
   3. if (errorCode != OPENGTX_SUCCESS) {
   4. return false;
   5. }
   ```

### OpenGTX关键信息更新

1. 游戏切换不同游戏场景后调用[HMS\_OpenGTX\_DispatchGameSceneInfo](../harmonyos-references/_graphics_accelerate.md#hms_opengtx_dispatchgamesceneinfo)接口发送游戏场景信息，包含场景类型、指定帧率、调度帧率范围、当前分辨率等信息。

   ```
   1. // OpenGTX游戏场景信息结构体
   2. OpenGTX_GameSceneInfo gameSceneInfo;
   3. // 游戏场景类型ID
   4. gameSceneInfo.sceneID = OTHERS_SCENE;
   5. // 游戏场景描述
   6. gameSceneInfo.description = (char*)"其他场景";
   7. // 游戏场景推荐帧率
   8. gameSceneInfo.recommendFPS = 60;
   9. // 游戏场景最小帧率
   10. gameSceneInfo.minFPS = 30;
   11. // 游戏场景最大帧率
   12. gameSceneInfo.maxFPS = 90;
   13. // 屏幕分辨率 高度
   14. gameSceneInfo.resolutionCurValue.height = 360;
   15. // 屏幕分辨率 宽度
   16. gameSceneInfo.resolutionCurValue.width = 1920;
   17. // OpenGTX接收游戏场景信息
   18. errorCode = HMS_OpenGTX_DispatchGameSceneInfo(context_, &gameSceneInfo);
   19. if (errorCode != OPENGTX_SUCCESS) {
   20. return false;
   21. }
   ```
2. 每帧渲染前调用[HMS\_OpenGTX\_DispatchFrameRenderInfo](../harmonyos-references/_graphics_accelerate.md#hms_opengtx_dispatchframerenderinfo)接口发送游戏帧渲染信息，包含游戏主相机的位置和欧拉角。

   ```
   1. // OpenGTX游戏渲染信息结构体
   2. OpenGTX_FrameRenderInfo frameRenderInfo;
   3. // 主相机位置
   4. frameRenderInfo.mainCameraPosition = { 0.0f, 0.0f, 0.0f };
   5. // 主相机欧拉角
   6. frameRenderInfo.mainCameraRotate = { 0.0f, 0.0f, 0.0f };
   7. // OpenGTX接收游戏渲染信息
   8. errorCode = HMS_OpenGTX_DispatchFrameRenderInfo(context_, &frameRenderInfo);
   9. if (errorCode != OPENGTX_SUCCESS) {
   10. return false;
   11. }
   ```
3. 每帧渲染前如遇到网络时延档位变化，调用[HMS\_OpenGTX\_DispatchNetworkInfo](../harmonyos-references/_graphics_accelerate.md#hms_opengtx_dispatchnetworkinfo)接口发送游戏网络信息。包含服务器IP地址、网络时延等信息。

   ```
   1. // OpenGTX游戏网络信息结构体
   2. OpenGTX_NetworkInfo networkInfo;
   3. // OpenGTX游戏网络时延结构体
   4. OpenGTX_NetworkLatency networkLatency;
   5. // 网络总时延
   6. networkLatency.total = 50;
   7. // 网络上行时延
   8. networkLatency.up = 10;
   9. // 网络下行时延
   10. networkLatency.down = 40;
   11. // 游戏网络时延
   12. networkInfo.networkLatency = networkLatency;
   13. // 游戏服务器IP地址
   14. networkInfo.networkServerIP = (char*)"10.10.10.10";
   15. // OpenGTX接收游戏网络信息
   16. errorCode = HMS_OpenGTX_DispatchNetworkInfo(context_, &networkInfo);
   17. if (errorCode != OPENGTX_SUCCESS) {
   18. return false;
   19. }
   ```

### 销毁OpenGTX实例

在surface销毁时，会触发其事件回调函数Core::OnSurfaceDestroyed()，在该函数中完成OpenGTX实例的销毁。

调用[HMS\_OpenGTX\_DestroyContext](../harmonyos-references/_graphics_accelerate.md#hms_opengtx_destroycontext)接口销毁OpenGTX实例，释放内存资源。

```
1. // 销毁OpenGTX上下文实例并释放内存资源
2. errorCode = HMS_OpenGTX_DestroyContext(&context_);
3. if (errorCode != OPENGTX_SUCCESS) {
4. return false;
5. }
```
