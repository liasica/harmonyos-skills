---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-fg-systempresent-vulkan
title: Vulkan平台
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏渲染加速服务 > 超帧功能开发 > 系统送显模式 > Vulkan平台
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bb6c2dd424f724817b9c59148f573086ee34bea38d0301f409abd2bd1bf39fbc
---

## 业务流程

基于Vulkan图形API平台，系统送显模式的主要业务流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/hU2rYW3ETmaVwWUXij_Iuw/zh-cn_image_0000002706834718.png)

1. 用户进入超帧适用的游戏场景。
2. 游戏应用调用[HMS\_FG\_CreateContext\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_createcontext_vk)接口创建超帧上下文实例。如超帧上下文实例创建失败，则无需在步骤6提供当前帧信息，只需逐帧对场景进行渲染送显即可。
3. 游戏应用调用接口配置超帧实例属性。包括调用[HMS\_FG\_SetAlgorithmMode\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_setalgorithmmode_vk)（必选）设置超帧算法模式并选择内插模式；按需调用其他插帧相关配置接口。
4. 设置系统侧的集成模式。

   系统侧的集成模式默认选择游戏送显模式；若选择系统送显模式，开发者可以调用[HMS\_FG\_SetIntegrationMode\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_setintegrationmode_vk)，设置超帧预测的集成信息[FG\_IntegrationInfo](../harmonyos-references/_f_g___intergration_info.md)。送显模式参见[FG\_PresentMode](../harmonyos-references/_graphics_accelerate.md#fg_presentmode-1)。

   在系统送显模式下，开发者可以调用[HMS\_FG\_SetUiPredictionEnabled\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_setuipredictionenabled_vk)，启用UI预测功能；若不启用，预测帧会复用上一帧的UI进行展示。

   在系统送显模式下，开发者可以调用[HMS\_FG\_SetTargetFps\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_settargetfps_vk)，设置超帧后的目标帧率，未调用则默认设置为60帧。
5. 游戏应用调用[HMS\_FG\_Activate\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_activate_vk)接口激活超帧上下文实例。
6. 游戏应用渲染真实帧，调用[HMS\_FG\_Dispatch\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_dispatch_vk)接口并传入真实帧颜色信息、深度信息、相机矩阵信息，生成预测帧。
7. 游戏应用完成UI绘制，并送显当前真实帧。
8. 用户退出超帧适用的游戏场景。
9. 游戏应用调用[HMS\_FG\_DestroyContext\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_destroycontext_vk)接口销毁超帧上下文实例并释放内存资源。

## 开发步骤

本节阐述基于Vulkan图形API平台的系统送显模式调用示例。详细代码请参考[图形开发Sample（超帧Vulkan）](https://gitcode.com/harmonyos_samples/frame-generation-vulkan-samplecode-clientdemo-cpp)。

1. 设置meta-data。在应用的module.json5中声明meta-data以支持系统送显模式。

   ```json5
   {
     "module": {
       // ...
       "metadata": [
         {
           "name": "GraphicsAccelerateKit_FusionAware",
           "value": "Vulkan"
         },
         // ...
       ],
       // ...
     }
   }
   ```
2. 引用Graphics Accelerate Kit超帧头文件：frame\_generation\_vk.h。

   ```cpp
   // 引用超帧frame_generation_vk.h头文件
   #include <graphics_game_sdk/frame_generation_vk.h>
   ```
3. 调用[HMS\_FG\_CreateContext\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_createcontext_vk)接口创建超帧上下文实例。如果返回nullptr，则说明超帧上下文实例创建失败，或当前硬件设备不支持开启超帧。

   ```cpp
    // 变量声明
    VkInstance vkInstance = VK_NULL_HANDLE; // vkInstance通过调用vkCreateInstance创建
    VkPhysicalDevice vkPhysicalDevice = VK_NULL_HANDLE; // vkPhysicalDevice通过调用vkEnumeratePhysicalDevices枚举
    VkDevice vkDevice = VK_NULL_HANDLE; // vkDevice通过调用vkCreateDevice创建

    // 创建超帧上下文实例
   FG_ContextDescription_VK contextDescription{};
   contextDescription.vkInstance = vkInstance;
   contextDescription.vkPhysicalDevice = vkPhysicalDevice;
   contextDescription.vkDevice = vkDevice;
   contextDescription.framesInFlight = 1;
   contextDescription.fnVulkanLoaderFunction = vkGetInstanceProcAddr;
   FG_Context_VK* m_context = HMS_FG_CreateContext_VK(&contextDescription);
   if (m_context == nullptr) {
       GOLOGE("HMS_FG_CreateContext_VK execution failed.");
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

   errorCode = HMS_FG_SetAlgorithmMode_VK(m_context, &aInfo); // 设置超帧算法模式
   if (errorCode != FG_SUCCESS) {
       GOLOGE("HMS_FG_SetAlgorithmMode_VK execution failed, error code: %d.", errorCode);
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
   errorCode = HMS_FG_SetIntegrationMode_VK(m_context, &integrationInfo);
   if (errorCode != FG_SUCCESS) {
       GOLOGE("HMS_FG_SetIntegrationMode_VK execution failed, error code: %d.", errorCode);
       return false;
   }

   // 当颜色缓冲区相对深度模板缓冲区基于y轴翻转180度时，设置第二个参数为true，接口不调用时默认为false
   errorCode = HMS_FG_SetDepthStencilYDirectionInverted_VK(m_context, false);
   if (errorCode != FG_SUCCESS) {
       GOLOGE("HMS_FG_SetDepthStencilYDirectionInverted_VK execution failed, error code: %d.", errorCode);
       return false;
   }

   // 设置超帧后的目标帧率，仅在系统送显模式下且游戏上架后有效，在游戏送显模式下无效，接口不调用默认不会限制帧率，取决于游戏渲染帧率
   errorCode = HMS_FG_SetTargetFps_VK(m_context, 60);
   if (errorCode != FG_SUCCESS) {
       GOLOGE("HMS_FG_SetTargetFps_VK execution failed, error code: %d.", errorCode);
       return false;
   }
   ```
5. 调用[HMS\_FG\_Activate\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_activate_vk)接口激活超帧上下文实例。

   ```
   // 激活超帧上下文实例
   FG_ErrorCode errorCode = HMS_FG_Activate_VK(m_context);
   if (errorCode != FG_SUCCESS) {
       GOLOGE("HMS_FG_Activate_VK execution failed, error code: %d.", errorCode);
       // ...
       return false;
   }
   ```
6. 调用[HMS\_FG\_CreateImage\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_createimage_vk)接口创建真实渲染帧颜色缓冲区图像实例、深度模板缓冲区图像实例。

   ```cpp
   // 变量声明
   FG_Image_VK *m_ffSceneColor = nullptr;
   VulkanFG::Image m_sceneColor{};
   FG_Image_VK *m_ffDepthStencil = nullptr;
   VulkanFG::Image m_sceneDepthStencil{};
   ```

   ```
   // 创建真实帧颜色缓冲区图像实例
   m_ffSceneColor = HMS_FG_CreateImage_VK(m_context, m_sceneColor.GetNativeImage(), m_sceneColor.GetNativeImageView());
   if (!m_ffSceneColor) {
       GOLOGE("HMS_FG_CreateImage_VK m_ffSceneColor execution failed.");
       return false;
   }
   // 创建真实帧深度模板缓冲区图像实例
   m_ffDepthStencil = HMS_FG_CreateImage_VK(m_context, m_sceneDepthStencil.GetNativeImage(),
                                            m_sceneDepthStencil.GetNativeImageView());
   if (!m_ffDepthStencil) {
       GOLOGE("HMS_FG_CreateImage_VK m_ffDepthStencil execution failed.");
       return false;
   }
   ```
7. 游戏运行中，渲染真实帧时，缓存颜色信息、深度信息和相机矩阵等属性信息。渲染预测帧时，需调用[HMS\_FG\_Dispatch\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_dispatch_vk)接口并传入真实帧属性信息，指定预测帧缓冲区索引，生成预测帧。游戏送显自己真实帧，系统会在真实帧和上一帧间完成预测帧的展示。

   ```cpp
   // 变量声明
   FG_Mat4x4 m_viewProj{};
   FG_Mat4x4 m_invViewProj{};
   FG_DispatchDescription_VK dispatch{};
   ```

   ```
   // 真实帧渲染阶段
   // 渲染当前帧渲染画面，缓存颜色、深度、相机矩阵等信息，用于下一帧预测帧生成，绘制真实帧
   // ...

   // 绘制UI
   // ...

   bool const runPrediction = m_predictionEnabled & !m_predictionPaused;
   if (runPrediction) { // 预测帧渲染阶段
       dispatch = {
           // 传入真实渲染帧颜色缓冲区属性信息
           .inputColorInfo = {
               .image = m_ffSceneColor,
               // 设置预测帧生成前真实帧颜色缓冲区同步状态
               .initialSync {
                   .accessMask = VK_ACCESS_SHADER_READ_BIT,
                   .layout = VK_IMAGE_LAYOUT_SHADER_READ_ONLY_OPTIMAL,
                   .stages = VK_PIPELINE_STAGE_FRAGMENT_SHADER_BIT
               },
               // 设置预测帧生成后真实帧颜色缓冲区同步状态
               .finalSync {
                   .accessMask = VK_ACCESS_SHADER_READ_BIT,
                   .layout = VK_IMAGE_LAYOUT_SHADER_READ_ONLY_OPTIMAL,
                   .stages = VK_PIPELINE_STAGE_FRAGMENT_SHADER_BIT
               }
           },
           // 传入真实渲染帧深度模板缓冲区属性信息
           .inputDepthStencilInfo = {
               .image = m_ffDepthStencil,
               // 设置预测帧生成前深度模板缓冲区同步状态
               .initialSync {
                   .accessMask = VK_ACCESS_SHADER_READ_BIT,
                   .layout = VK_IMAGE_LAYOUT_SHADER_READ_ONLY_OPTIMAL,
                   .stages = VK_PIPELINE_STAGE_FRAGMENT_SHADER_BIT
               },
               // 设置预测帧生成后深度模板缓冲区同步状态
               .finalSync {
                   .accessMask = VK_ACCESS_SHADER_READ_BIT,
                   .layout = VK_IMAGE_LAYOUT_SHADER_READ_ONLY_OPTIMAL,
                   .stages = VK_PIPELINE_STAGE_FRAGMENT_SHADER_BIT
               }
           },
           // 传入预测帧缓冲区属性信息
           .outputColorInfo = {
               .image = m_ffPredictedColor,
               // 设置预测帧生成前预测帧缓冲区同步状态
               .initialSync {
                   .accessMask = VK_ACCESS_SHADER_READ_BIT,
                   .layout = VK_IMAGE_LAYOUT_SHADER_READ_ONLY_OPTIMAL,
                   .stages = VK_PIPELINE_STAGE_FRAGMENT_SHADER_BIT
               },
               // 设置预测帧生成后预测帧缓冲区同步状态
               .finalSync {
                   .accessMask = VK_ACCESS_SHADER_READ_BIT,
                   .layout = VK_IMAGE_LAYOUT_SHADER_READ_ONLY_OPTIMAL,
                   .stages = VK_PIPELINE_STAGE_FRAGMENT_SHADER_BIT
               }
           },
           // 传入上一帧真实渲染帧视图投影矩阵
           .viewProj = m_viewProj,
           // 传入上一帧真实渲染帧视图投影逆矩阵
           .invViewProj = m_invViewProj,
           // 传入用于录入超帧绘制指令的命令缓冲区句柄
           .vkCommandBuffer = fif->commandBuffer,
           // 传入当前帧序号
           .frameIdx = fifIndex
       };
       // ...
       // 生成预测帧，更新预测帧缓冲区的内存
       FG_ErrorCode const errorCode = HMS_FG_Dispatch_VK(m_context, &dispatch);
       if (errorCode != FG_SUCCESS) {
           GOLOGE("HMS_FG_Dispatch_VK execution failed, error code: %d", errorCode);
       }
   }
       
   // ...
   // 送显真实帧
   // ...
   ```
8. 调用[HMS\_FG\_DestroyContext\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_destroycontext_vk)接口销毁超帧实例，释放内存资源。

   ```cpp
   // 销毁超帧上下文实例并释放内存资源
   errorCode = HMS_FG_DestroyContext_VK(&m_context);
   if (errorCode != FG_SUCCESS) {
       GOLOGE("HMS_FG_DestroyContext_VK execution failed, error code: %d", errorCode);
       return false;
   }
   ```
