---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-abr
title: ABR功能开发
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏渲染加速服务 > ABR功能开发
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2e9bfd3eb8646a9497a89f116b05002751857980bcb545ab5f0412d1af3de8d9
---

## 业务流程

基于相机运动感知策略的ABR主要业务流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/Wpcbvh5mRX-9RQ5qUX8_tg/zh-cn_image_0000002589325083.png?HW-CC-KV=V1&HW-CC-Date=20260429T053627Z&HW-CC-Expire=86400&HW-CC-Sign=5AC4B5E80EE430544B1104851B8A809686FF0CDE1CC96D83B173C775586EFF94)

1. 用户进入ABR适用的游戏场景。
2. 游戏应用调用[HMS\_ABR\_CreateContext](../harmonyos-references/_graphics_accelerate.md#hms_abr_createcontext)接口并指定图形API类型，创建ABR上下文实例。
3. 游戏应用调用[HMS\_ABR\_SetTargetFps](../harmonyos-references/_graphics_accelerate.md#hms_abr_settargetfps)接口初始化ABR实例，配置目标帧率属性，ABR结合目标帧率属性实时感知GPU负载状态。
4. 游戏应用调用[HMS\_ABR\_SetScaleRange](../harmonyos-references/_graphics_accelerate.md#hms_abr_setscalerange)接口初始化ABR实例，配置Buffer分辨率因子范围属性。
5. 游戏应用调用[HMS\_ABR\_Activate](../harmonyos-references/_graphics_accelerate.md#hms_abr_activate)接口激活ABR上下文实例。
6. 游戏应用调用[HMS\_ABR\_UpdateCameraData](../harmonyos-references/_graphics_accelerate.md#hms_abr_updatecameradata)接口并传入相机运动信息，包含相机旋转、位移信息。
7. 游戏应用在使能ABR的Buffer渲染前调用[HMS\_ABR\_MarkFrameBuffer\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_abr_markframebuffer_gles)接口，对Buffer进行标记。
8. Buffer渲染处理。
9. 绘制UI。
10. 一帧送显。
11. 用户退出ABR适用的游戏场景。
12. 游戏应用调用[HMS\_ABR\_DestroyContext](../harmonyos-references/_graphics_accelerate.md#hms_abr_destroycontext)接口销毁ABR上下文实例并释放内存资源。

## 开发步骤

本节阐述基于相机运动感知策略的ABR使用，从流程上分别阐述每个步骤的实现和调用。详细代码请参考[图形开发Sample（ABR）](https://gitcode.com/harmonyos_samples/adaptive-buffer-resolution-samplecode-clientdemo-cpp)。

### 设置项目配置项

在“src/main/module.json5”的module层级中添加以下配置。

```
1. "metadata": [
2. {
3. "name": "GraphicsAccelerateKit_ABR",
4. "value": "true"
5. }
6. ]
```

### 头文件引用

引用Graphics Accelerate Kit ABR头文件：abr\_gles.h。

```
1. // 引用ABR头文件 abr_gles.h
2. #include <graphics_game_sdk/abr_gles.h>
3. #include <GLES3/gl32.h>
```

### 编写CMakeLists.txt

```
1. find_library(
2. # Sets the name of the path variable.
3. abr-lib
4. # Specifies the name of the NDK library that you want CMake to locate.
5. libabr.so
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
21. ${abr-lib} ${GLES-lib} ${hilog-lib}
22. )
```

### ABR初始化

在应用创建Surface后会触发其事件回调函数Core::OnSurfaceCreated()，在该函数中完成ABR上下文实例创建、ABR属性配置和功能激活。其中ABR上下文实例负责管理ABR整个生命周期。

1. 调用[HMS\_ABR\_CreateContext](../harmonyos-references/_graphics_accelerate.md#hms_abr_createcontext)接口创建ABR上下文实例，指定图形API类型。如果返回nullptr，则说明ABR上下文实例创建失败，或当前硬件设备不支持开启ABR。

   ```
   1. // 创建ABR上下文实例，指定图形API类型
   2. ABR_Context *context_ = HMS_ABR_CreateContext(RENDER_API_GLES);
   3. if (context_ == nullptr) {
   4. return false;
   5. }
   ```
2. 调用[HMS\_ABR\_SetTargetFps](../harmonyos-references/_graphics_accelerate.md#hms_abr_settargetfps)接口初始化ABR实例，根据游戏的目标帧率配置ABR的目标帧率属性。

   ```
   1. // 初始化ABR接口调用错误码
   2. ABR_ErrorCode errorCode = ABR_SUCCESS;

   4. // 初始化ABR实例，配置ABR的目标帧率属性。例如游戏目标帧率为120fps，则配置ABR的目标帧率属性为120fps
   5. errorCode = HMS_ABR_SetTargetFps(context_, 120);
   6. if (errorCode != ABR_SUCCESS) {
   7. return false;
   8. }
   ```
3. 调用[HMS\_ABR\_SetScaleRange](../harmonyos-references/_graphics_accelerate.md#hms_abr_setscalerange)接口初始化ABR实例，配置Buffer分辨率因子范围属性。

   ```
   1. // 初始化ABR实例，配置Buffer分辨率因子范围属性，结合具体游戏分辨率、画质设置合适的范围
   2. // 例如设置ABR对Buffer分辨率进行0.5~1.0倍的自适应调整
   3. errorCode = HMS_ABR_SetScaleRange(context_, 0.5f, 1.0f);
   4. if (errorCode != ABR_SUCCESS) {
   5. return false;
   6. }
   ```
4. 调用[HMS\_ABR\_Activate](../harmonyos-references/_graphics_accelerate.md#hms_abr_activate)接口激活ABR上下文实例。

   ```
   1. // 激活ABR上下文实例
   2. errorCode = HMS_ABR_Activate(context_);
   3. if (errorCode != ABR_SUCCESS) {
   4. return false;
   5. }
   ```

### 相机运动数据更新

在帧循环中，ABR根据获取的实时相机运动数据进行Buffer分辨率因子决策。

调用[HMS\_ABR\_UpdateCameraData](../harmonyos-references/_graphics_accelerate.md#hms_abr_updatecameradata)接口并传入相机运动信息，包含相机旋转、位移信息。

```
1. // 相机运动数据结构体，设置每帧实时相机运动数据
2. ABR_CameraData cameraData;
3. // 每帧位置
4. ABR_Vector3 position_;
5. // 每帧的相机旋转角，范围是[0, 360]
6. ABR_Vector3 rotation_;
7. cameraData.position = position_;
8. cameraData.rotation = rotation_;

10. // 每帧相机运动数据更新
11. errorCode = HMS_ABR_UpdateCameraData(context_, &cameraData);
12. if (errorCode != ABR_SUCCESS) {
13. return false;
14. }
```

### 自适应渲染

在帧循环中，ABR将对所标记的Buffer进行自适应渲染处理。

1. 选择着色器处理耗时较高的Buffer，并在Buffer渲染前绑定帧缓冲。

   ```
   1. // 创建帧缓冲对象
   2. GLuint fbo;
   3. glGenFramebuffers(1, &fbo);
   4. // 绑定帧缓冲
   5. glBindFramebuffer(GL_FRAMEBUFFER, fbo);
   ```
2. 调用[HMS\_ABR\_MarkFrameBuffer\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_abr_markframebuffer_gles)接口对Buffer进行标记。

   ```
   1. // 在Buffer渲染前调用，执行失败不影响Buffer正常渲染
   2. errorCode = HMS_ABR_MarkFrameBuffer_GLES(context_);
   3. if (errorCode != ABR_SUCCESS) {
   4. return false;
   5. }
   ```
3. 执行Buffer原有渲染流程。

### 销毁ABR实例

在Surface销毁时，会触发其事件回调函数Core::OnSurfaceDestroyed()，在该函数中完成ABR实例的销毁。

调用[HMS\_ABR\_DestroyContext](../harmonyos-references/_graphics_accelerate.md#hms_abr_destroycontext)接口销毁ABR实例，释放内存资源。

```
1. // 销毁ABR上下文实例并释放内存资源
2. ABR_ErrorCode errorCode = HMS_ABR_DestroyContext(&context_);
3. if (errorCode != ABR_SUCCESS) {
4. return false;
5. }
```
