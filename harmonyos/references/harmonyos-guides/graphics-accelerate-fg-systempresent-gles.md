---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-fg-systempresent-gles
title: OpenGL ES平台
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏渲染加速服务 > 超帧功能开发 > 系统送显模式 > OpenGL ES平台
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:21+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:fe650c7b059cab33e1eb4ded45e21656417ed66b659ea4da6d859dc302def8a7
---

## 业务流程

基于OpenGL ES图形API平台，系统送显模式的主要业务流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/IFb9Zin2SWao8ehkxK12OA/zh-cn_image_0000002736433869.png)

1. 用户进入超帧适用的游戏场景。
2. 游戏应用调用[HMS\_FG\_CreateContext\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_createcontext_gles)接口创建超帧上下文实例。如超帧上下文实例创建失败，则无需在步骤6提供当前帧信息，只需逐帧对场景进行渲染送显即可。
3. 游戏应用调用接口配置超帧实例属性。包括调用[HMS\_FG\_SetAlgorithmMode\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_setalgorithmmode_gles)（必选）设置超帧算法模式并选择内插模式；按需调用其他插帧相关配置接口。
4. 设置系统侧的集成模式。

   系统侧的集成模式默认选择游戏送显模式；若选择系统送显模式，开发者可以调用[HMS\_FG\_SetIntegrationMode\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_setintegrationmode_gles)，设置超帧预测的集成信息[FG\_IntegrationInfo](../harmonyos-references/_f_g___intergration_info.md)。送显模式参见[FG\_PresentMode](../harmonyos-references/_graphics_accelerate.md#fg_presentmode-1)。

   在系统送显模式下，开发者可以调用[HMS\_FG\_SetUiPredictionEnabled\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_setuipredictionenabled_gles)，启用UI预测功能；若不启用，预测帧会复用上一帧的UI进行展示。

   在系统送显模式下，开发者可以调用[HMS\_FG\_SetTargetFps\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_settargetfps_gles)，设置超帧后的目标帧率。
5. 游戏应用调用[HMS\_FG\_Activate\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_activate_gles)接口激活超帧上下文实例。
6. 游戏应用渲染真实帧，调用[HMS\_FG\_Dispatch\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_dispatch_gles)接口并传入真实帧颜色信息、深度信息、相机矩阵信息，生成预测帧。
7. 游戏应用完成UI绘制，并送显当前真实帧。
8. 用户退出超帧适用的游戏场景。
9. 游戏应用调用[HMS\_FG\_DestroyContext\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_destroycontext_gles)接口销毁超帧上下文实例并释放内存资源。

## 开发步骤

本节阐述基于OpenGL ES图形API平台的系统送显模式调用示例。详细代码请参考[图形开发Sample（超帧GLES）](https://gitcode.com/harmonyos_samples/frame-generation-gles-samplecode-clientdemo-cpp)。

1. 设置meta-data。在应用的module.json5中声明meta-data以支持系统送显模式。

   ```json5
   {
       "module": {
           // ...
           "metadata": [
               {
                   "name": "GraphicsAccelerateKit_FusionAware",
                   "value": "GLES"
               }
           ],
           // ...
       }
   }
   ```
2. 引用Graphics Accelerate Kit超帧头文件：frame\_generation\_gles.h。

   ```cpp
   // 引用超帧frame_generation_gles.h头文件
   #include <graphics_game_sdk/frame_generation_gles.h>
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
4. 调用超帧实例属性配置接口，超帧算法模式选择内插模式并指定系统送显预测帧模式。

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

   // 调用其他插帧相关配置接口
   // ...

   // 超帧预测的集成信息
   FG_IntegrationInfo integrationInfo {};
   integrationInfo.presentMode = FG_PRESENT_BY_SYSTEM; // 预测帧送显模式
   integrationInfo.textureCachedByGame = false; // 输入的颜色纹理和深度纹理游戏侧缓存 系统不会复制一份再做预测 默认游戏不会缓存
   integrationInfo.needFlipInputColor = false; // 颜色纹理需要翻转 默认false
   integrationInfo.needFlipOutputColor = false; // 预测帧需要翻转 默认false
   // 设置超帧预测的集成信息
   errorCode = HMS_FG_SetIntegrationMode_GLES(context_, &integrationInfo);
   if (errorCode != FG_SUCCESS) {
       GOLOGE("HMS_FG_SetIntegrationMode_GLES execution failed, error code: %d.", errorCode);
       return false;
   }
       
   // 设置是否启用UI预测功能，仅在系统送显模式下有效，在游戏送显模式下无效，接口不调用默认为false，预测帧会复用上一帧的UI进行展示
   errorCode = HMS_FG_SetUiPredictionEnabled_GLES(context_, false);
   if (errorCode != FG_SUCCESS) {
       GOLOGE("HMS_FG_SetUiPredictionEnabled_GLES execution failed, error code: %d.", errorCode);
       return false;
   }
       
   // 设置超帧后的目标帧率，仅在系统送显模式下且游戏上架后有效，在游戏送显模式下无效，接口不调用默认不会限制帧率，取决于游戏渲染帧率
   errorCode = HMS_FG_SetTargetFps_GLES(context_, 60);
   if (errorCode != FG_SUCCESS) {
       GOLOGE("HMS_FG_SetTargetFps_GLES execution failed, error code: %d.", errorCode);
       return false;
   }
   ```
5. 调用[HMS\_FG\_Activate\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_activate_gles)接口激活超帧上下文实例。

   ```
   // 激活超帧上下文实例
   errorCode = HMS_FG_Activate_GLES(context_);
   if (errorCode != FG_SUCCESS) {
       GOLOGE("HMS_FG_Activate_GLES execution failed, error code: %d.", errorCode);
       return false;
   }
   ```
6. 游戏运行中，渲染真实帧时，缓存颜色信息、深度信息和相机矩阵等属性信息。渲染预测帧时，需调用[HMS\_FG\_Dispatch\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_dispatch_gles)接口并传入真实帧属性信息，生成预测帧。游戏送显真实帧，系统会在真实帧和上一帧间完成预测帧的展示。

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

   ```
    // 渲染当前帧渲染画面，缓存颜色、深度、相机矩阵等信息，用于下一帧预测帧生成
    // ...

    // 绘制真实帧
    // ...
    // 绘制UI
    // ...
    bool const runPrediction = predictionEnabled_ && !predictionPaused_;
    if (runPrediction) { // 预测帧渲染阶段
        // 传入上一帧真实渲染帧颜色缓冲区索引
        dispatchDescriptionData_.inputColor = scene_.texture_;
        // 传入上一帧真实渲染帧深度模板缓冲区索引
        dispatchDescriptionData_.inputDepthStencil = scene_.depthTexture_;
        // 传入上一帧真实渲染帧视图投影矩阵
        dispatchDescriptionData_.viewProj = *reinterpret_cast<FG_Mat4x4 const *>(&lastViewProj_);
        Matrix4x4 invViewProj{};
        // 传入上一帧真实渲染帧视图投影逆矩阵
        dispatchDescriptionData_.invViewProj =
            *reinterpret_cast<FG_Mat4x4 const *>(invViewProj.Invert(lastViewProj_).data_);
        if (!dispatchDescriptionData_.inputColor || !dispatchDescriptionData_.inputDepthStencil) {
            GOLOGE("HMS_FG_SetImageFormat_GLES is invalid.");
        }
        glBindFramebuffer(GL_DRAW_FRAMEBUFFER, scene_);
        // 生成预测帧，更新预测帧缓冲区的内存
        FG_ErrorCode errorCode = HMS_FG_Dispatch_GLES(context_, &dispatchDescriptionData_);
        glBindFramebuffer(GL_DRAW_FRAMEBUFFER, 0U);

        switch (errorCode) {
            case FG_SUCCESS: {
                // 生成预测帧成功，绘制UI
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

    // 送显真实帧
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
