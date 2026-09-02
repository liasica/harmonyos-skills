---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-fg-interpolation-gles
title: OpenGL ES平台
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏渲染加速服务 > 超帧功能开发 > 内插模式 > OpenGL ES平台
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:21+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:4f517d90705b4a2e2f1e115197856c7cd10d18677cb1952406e5ae3e138229c3
---

## 业务流程

基于OpenGL ES图形API平台，超帧内插模式的主要业务流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/WvsVr8OyQzilpmNExuLw2Q/zh-cn_image_0000002736433865.png)

1. 用户进入超帧适用的游戏场景。
2. 游戏应用调用[HMS\_FG\_CreateContext\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_createcontext_gles)接口创建超帧上下文实例。如超帧上下文实例创建失败，则无需进入步骤5到步骤9的预测帧、真实帧交替渲染送显的循环流程，只需逐帧对场景进行渲染送显即可。
3. 游戏应用调用接口配置超帧实例属性。包括调用[HMS\_FG\_SetAlgorithmMode\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_setalgorithmmode_gles)设置超帧算法模式并选择内插模式；调用[HMS\_FG\_SetResolution\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_setresolution_gles)设置超帧输入输出图像分辨率；调用[HMS\_FG\_SetCvvZSemantic\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_setcvvzsemantic_gles)设置齐次裁剪空间Z/W范围及深度测试函数，未调用该接口则默认设置为FG\_CVV\_Z\_SEMANTIC\_MINUS\_ONE\_TO\_ONE\_FORWARD\_Z；调用[HMS\_FG\_SetImageFormat\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_setimageformat_gles)设置真实渲染帧颜色缓冲区图像格式，未调用该接口则默认设置为FG\_FORMAT\_R8G8B8A8\_UNORM；如果颜色缓冲区相对深度模板缓冲区基于y轴翻转180度，则调用[HMS\_FG\_SetDepthStencilYDirectionInverted\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_setdepthstencilydirectioninverted_gles)设置翻转状态，未调用该接口则默认无翻转。
4. 游戏应用调用[HMS\_FG\_Activate\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_activate_gles)接口激活超帧上下文实例。
5. 游戏应用调用[HMS\_FG\_Dispatch\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_dispatch_gles)接口并传入历史真实渲染帧颜色信息、深度信息、相机矩阵信息，生成预测帧，并更新预测帧缓冲区。当相机视图投影矩阵的平移分量非常大时（如超过10W），预测帧效果下降，画面易出现闪烁。此时可在[HMS\_FG\_Dispatch\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_dispatch_gles)接口调用前调用[HMS\_FG\_SetExtendedCameraInfo\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_setextendedcamerainfo_gles)设置相机扩展信息，从而获取精度更高的预测帧效果。
6. 预测帧绘制UI并送显。
7. 绘制缓存中的上一帧真实渲染帧，并绘制UI。
8. 上一帧真实渲染帧送显。
9. 渲染游戏场景获取真实渲染帧，缓存真实渲染帧颜色信息、深度信息、相机矩阵等信息，用于后续超帧预测。由于内插模式真实帧需要等待前一帧预测帧绘制并送显后再送显，因此此处缓存一帧真实帧信息。跳转至序号5继续执行，直到退出游戏场景。
10. 用户退出超帧适用的游戏场景。
11. 游戏应用调用[HMS\_FG\_DestroyContext\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_destroycontext_gles)接口销毁超帧上下文实例并释放内存资源。

## 开发步骤

本节阐述基于OpenGL ES图形API平台的超帧调用示例。详细代码请参考[图形开发Sample（超帧GLES）](https://gitcode.com/harmonyos_samples/frame-generation-gles-samplecode-clientdemo-cpp)。

1. 引用Graphics Accelerate Kit超帧头文件：frame\_generation\_gles.h。

   ```cpp
   // 引用超帧frame_generation_gles.h头文件
   #include <graphics_game_sdk/frame_generation_gles.h>
   ```
2. 编写CMakeLists.txt。

   ```cpp
   find_library(framegeneration-lib libframegeneration.so REQUIRED)

   target_link_libraries(entry PUBLIC
       ${framegeneration-lib}
   )
   ```
3. 调用[HMS\_FG\_CreateContext\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_createcontext_gles)接口创建超帧上下文实例。如果返回nullptr，则说明超帧上下文实例创建失败，或当前硬件设备不支持开启超帧。

   ```cpp
   // 创建超帧上下文实例
   FG_Context_GLES* context_ = HMS_FG_CreateContext_GLES();
   if (context_ == nullptr) {
       GOLOGE("HMS_FG_CreateContext_GLES execution failed.");
       return false;
   }
   ```
4. 调用超帧实例属性配置接口，超帧算法模式选择内插模式。

   ```
   // 初始化超帧接口调用错误码
   FG_ErrorCode errorCode = FG_SUCCESS;

   // 超帧算法模式
   FG_AlgorithmModeInfo aInfo{};
   aInfo.predictionMode = FG_PREDICTION_MODE_INTERPOLATION; // 内插模式
   aInfo.meMode = FG_ME_MODE_BASIC; // 运动估计基础模式
   errorCode = HMS_FG_SetAlgorithmMode_GLES(context_, &aInfo); // 设置超帧算法模式
   if (errorCode != FG_SUCCESS) {
       GOLOGE("HMS_FG_SetAlgorithmMode_GLES execution failed, error code: %d.", errorCode);
       return false;
   }

   // 真实帧颜色缓冲区分辨率
   FG_Dimension2D inputColorResolution{};
   inputColorResolution.width = scene_.fboWidth_; // 真实帧颜色缓冲区图像宽度
   inputColorResolution.height = scene_.fboHeight_; // 真实帧颜色缓冲区图像高度
   // 真实帧深度模板缓冲区分辨率
   FG_Dimension2D inputDepthStencilResolution{};
   inputDepthStencilResolution.width = scene_.fboWidth_; // 真实帧深度模板缓冲区图像宽度
   inputDepthStencilResolution.height = scene_.fboHeight_; // 真实帧深度模板缓冲区图像高度
   // 预测帧分辨率
   FG_Dimension2D outputColorResolution{};
   outputColorResolution.width = scene_.fboWidth_; // 预测帧图像宽度
   outputColorResolution.height = scene_.fboHeight_; // 预测帧图像高度
   // 超帧输入输出图像分辨率
   FG_ResolutionInfo rInfo{};
   rInfo.inputColorResolution = inputColorResolution;
   rInfo.inputDepthStencilResolution = inputDepthStencilResolution;
   rInfo.outputColorResolution = outputColorResolution;

   errorCode = HMS_FG_SetResolution_GLES(context_, &rInfo); // 设置超帧输入输出图像分辨率
   if (errorCode != FG_SUCCESS) {
       GOLOGE("HMS_FG_SetResolution_GLES execution failed, error code: %d.", errorCode);
       return false;
   }

   // 设置齐次裁剪空间Z/W范围及深度测试模式，接口不调用时默认为FG_CVV_Z_SEMANTIC_MINUS_ONE_TO_ONE_FORWARD_Z
   errorCode = HMS_FG_SetCvvZSemantic_GLES(context_, FG_CVV_Z_SEMANTIC_MINUS_ONE_TO_ONE_FORWARD_Z);
   if (errorCode != FG_SUCCESS) {
       GOLOGE("HMS_FG_SetCvvZSemantic_GLES execution failed, error code: %d.", errorCode);
       return false;
   }

   // 设置真实渲染帧颜色缓冲区图像格式，接口不调用时默认为FG_FORMAT_R8G8B8A8_UNORM
   errorCode = HMS_FG_SetImageFormat_GLES(context_, FG_FORMAT_R8G8B8A8_UNORM);
   if (errorCode != FG_SUCCESS) {
       GOLOGE("HMS_FG_SetImageFormat_GLES execution failed, error code: %d.", errorCode);
       return false;
   }

   // 当颜色缓冲区相对深度模板缓冲区基于y轴翻转180度时，设置第二个参数为true，接口不调用时默认为false
   errorCode = HMS_FG_SetDepthStencilYDirectionInverted_GLES(context_, false);
   if (errorCode != FG_SUCCESS) {
       GOLOGE("HMS_FG_SetDepthStencilYDirectionInverted_GLES execution failed, error code: %d.", errorCode);
       return false;
   }
   ```
5. 调用[HMS\_FG\_Activate\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_activate_gles)接口激活超帧上下文实例。

   ```cpp
   // 激活超帧上下文实例
   errorCode = HMS_FG_Activate_GLES(context_);
   if (errorCode != FG_SUCCESS) {
       GOLOGE("HMS_FG_Activate_GLES execution failed, error code: %d.", errorCode);
       return false;
   }
   ```
6. 游戏运行中，真实帧和预测帧交替渲染并送显。渲染真实帧时，缓存颜色信息、深度信息和相机矩阵等属性信息。渲染预测帧时，需调用[HMS\_FG\_Dispatch\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_dispatch_gles)接口并传入上一帧真实帧属性信息，指定预测帧缓冲区索引，生成预测帧，最终更新预测帧缓冲区内存。

   ```
   // 帧生成属性配置结构体
   FG_DispatchDescription_GLES dispatchDescriptionData_ {
       .inputColor = 0U,
       .inputDepthStencil = 0U,
       .viewProj{},
       .invViewProj{},
       .outputColor = 0U
   };
   ```

   ```cpp
   bool const runPrediction = predictionEnabled_ && !predictionPaused_;
   if (runPrediction) { // 预测帧渲染阶段
       // 传入上一帧真实渲染帧颜色缓冲区索引
       dispatchDescriptionData_.inputColor = scene_.texture_;
       // 传入上一帧真实渲染帧深度模板缓冲区索引
       dispatchDescriptionData_.inputDepthStencil = scene_.depthTexture_;
       // 传入预测帧缓冲区索引
       dispatchDescriptionData_.outputColor = predictedFrame_;
       // 传入上一帧真实渲染帧视图投影矩阵
       dispatchDescriptionData_.viewProj = *reinterpret_cast<FG_Mat4x4 const *>(&lastViewProj_);
       Matrix4x4 invViewProj{};
       // 传入上一帧真实渲染帧视图投影逆矩阵
       dispatchDescriptionData_.invViewProj =
           *reinterpret_cast<FG_Mat4x4 const *>(invViewProj.Invert(lastViewProj_).data_);

       // 生成预测帧，更新预测帧缓冲区的内存
       FG_ErrorCode errorCode = HMS_FG_Dispatch_GLES(context_, &dispatchDescriptionData_);

       switch (errorCode) {
       case FG_SUCCESS: { // 生成预测帧成功
           // 绘制预测帧
           // ...
           // 绘制UI
           // ...
           // 预测帧送显
           // ...
           break;
       }

       case FG_COLLECTING_PREVIOUS_FRAMES:
           // 传入真实帧数量未达到固定阈值，无预测帧生成，基础内插模式传入真实帧数量<2时返回该状态码，此时不要将预测帧送显
           break;

       default:
           // 预测帧生成失败
           GOLOGE("HMS_FG_Dispatch_GLES execution failed, error code: %d.", errorCode);
           return false;
       }
   }
   // 真实帧渲染阶段
   // 绘制缓存中的上一帧真实帧
   // ...
   // 绘制UI
   // ...
   // 渲染当前帧渲染画面，缓存颜色、深度、相机矩阵等信息，用于下一帧预测帧生成
   // ...
   // 送显缓存中的上一帧真实帧
   // ...
   ```
7. 调用[HMS\_FG\_DestroyContext\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_destroycontext_gles)接口销毁超帧实例，释放内存资源。

   ```
   // 销毁超帧上下文实例并释放内存资源
   FG_ErrorCode errorCode = HMS_FG_DestroyContext_GLES(&context_);
   // ...
   if (errorCode != FG_SUCCESS) {
       GOLOGE("HMS_FG_DestroyContext_GLES execution failed, error code: %d.", errorCode);
       return false;
   }
   ```
