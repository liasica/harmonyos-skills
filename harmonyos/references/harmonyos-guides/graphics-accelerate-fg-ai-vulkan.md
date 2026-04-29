---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-fg-ai-vulkan
title: Vulkan平台
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏渲染加速服务 > 超帧功能开发 > AI超帧模式 > Vulkan平台
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e02e944dcf1536b6ba4c0a6cfa325325cd2f96ea8c0234c371071e409384fcd3
---

## 业务流程

AI超帧调用流程上依赖系统送显模式功能，但与基本的系统送显模式相比，无需调用新方法，只需要在传输帧信息的时候不传输深度信息即可。

下面是基于Vulkan图形API平台，集成AI超帧的主要业务流程：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/3x1LJMraSA-jnuf8TX9_NA/zh-cn_image_0000002558605556.png?HW-CC-KV=V1&HW-CC-Date=20260429T053627Z&HW-CC-Expire=86400&HW-CC-Sign=3B5E3906C879C9C9F6AE95314B226D910EE8569761B0C2022C66EC22F6C18E50)

1. 用户进入超帧适用的游戏场景。
2. 游戏应用调用[HMS\_FG\_CreateContext\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_createcontext_vk)接口创建超帧上下文实例。如超帧上下文实例创建失败，则无需在步骤6提供当前帧信息，只需逐帧对场景进行渲染送显即可。
3. 游戏应用调用接口配置超帧实例属性。包括调用[HMS\_FG\_SetAlgorithmMode\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_setalgorithmmode_vk)（必选）设置超帧算法模式并选择内插模式；按需调用其他插帧相关配置接口。
4. 设置集成模式，选择系统侧集成调用[HMS\_FG\_SetIntegrationMode\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_setintegrationmode_vk)（可选）设置超帧预测的集成信息[FG\_IntegrationInfo](../harmonyos-references/_graphics_accelerate.md#fg_integrationinfo)并选择系统侧送显；系统送显预测帧模式下可通过[HMS\_FG\_SetUiPredictionEnabled\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_setuipredictionenabled_vk)（可选）启用UI预测功能，不启用时预测帧会复用上一帧的UI进行展示；系统送显模式下可通过[HMS\_FG\_SetTargetFps\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_settargetfps_vk)（可选）设置超帧后的目标帧率。
5. 游戏应用调用[HMS\_FG\_Activate\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_activate_vk)接口激活超帧上下文实例。
6. 游戏应用渲染真实帧，调用[HMS\_FG\_Dispatch\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_dispatch_vk)接口并传入真实帧颜色信息、相机矩阵信息，生成预测帧。请避免传入深度信息，否则会触发增强超帧算法。
7. 游戏应用完成UI绘制，并送显当前真实帧。
8. 用户退出超帧适用的游戏场景。
9. 游戏应用调用[HMS\_FG\_DestroyContext\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_destroycontext_vk)接口销毁超帧上下文实例并释放内存资源。

## 开发步骤

本节阐述基于Vulkan图形API平台的系统送显模式调用示例。

1. 设置meta-data。在应用的module.json5中声明meta-data以支持系统送显模式。

   ```
   1. {
   2. "module": {
   3. // 其他的配置项
   4. // ...
   5. "metadata": [
   6. {
   7. "name": "GraphicsAccelerateKit_FusionAware",
   8. "value": "Vulkan"
   9. }
   10. ]
   11. }
   12. }
   ```
2. 编写CMakeLists.txt。

   ```
   1. find_library(
   2. # Sets the name of the path variable.
   3. framegeneration-lib
   4. # Specifies the name of the NDK library that you want CMake to locate.
   5. libframegeneration.so
   6. )
   7. find_library(
   8. # Sets the name of the path variable.
   9. vulkan-lib
   10. # Specifies the name of the NDK library that you want CMake to locate.
   11. vulkan
   12. )

   14. target_link_libraries(entry PUBLIC
   15. ${framegeneration-lib} ${vulkan-lib}
   16. )
   ```
3. 引用Graphics Accelerate Kit超帧头文件：frame\_generation\_vk.h。

   ```
   1. // 引用超帧frame_generation_vk.h头文件
   2. #include <graphics_game_sdk/frame_generation_vk.h>
   ```
4. 调用[HMS\_FG\_CreateContext\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_createcontext_vk)接口创建超帧上下文实例。如果返回nullptr，则说明超帧上下文实例创建失败，或当前硬件设备不支持开启超帧。

   ```
   1. // 变量声明
   2. VkInstance vkInstance = VK_NULL_HANDLE;
   3. VkPhysicalDevice vkPhysicalDevice = VK_NULL_HANDLE;
   4. VkDevice vkDevice = VK_NULL_HANDLE;

   6. // 创建超帧上下文实例
   7. FG_ContextDescription_VK contextDescription{};
   8. contextDescription.vkInstance = vkInstance;
   9. contextDescription.vkPhysicalDevice = vkPhysicalDevice;
   10. contextDescription.vkDevice = vkDevice;
   11. contextDescription.framesInFlight = 1;
   12. contextDescription.fnVulkanLoaderFunction = vkGetInstanceProcAddr;
   13. FG_Context_VK* m_context = HMS_FG_CreateContext_VK(&contextDescription);
   14. if (m_context == nullptr) {
   15. return false;
   16. }
   ```
5. 调用超帧实例属性配置接口，超帧算法模式选择内插增强模式并指定系统送显预测帧模式。

   ```
   1. // 初始化超帧接口调用错误码
   2. FG_ErrorCode errorCode = FG_SUCCESS;

   4. // 超帧算法模式
   5. FG_AlgorithmModeInfo aInfo{};
   6. aInfo.predictionMode = FG_PREDICTION_MODE_INTERPOLATION;                  // 内插模式
   7. aInfo.meMode = FG_ME_MODE_ENHANCED;                                       // 增强模式
   8. errorCode = HMS_FG_SetAlgorithmMode_VK(m_context, &aInfo);                // [必选] 设置超帧算法模式
   9. if (errorCode != FG_SUCCESS) {
   10. return false;
   11. }

   13. // 调用其他插帧相关配置接口
   14. // ...

   16. // 超帧预测的集成信息
   17. FG_IntegrationInfo integrationInfo {};
   18. integrationInfo.presentMode = FG_PRESENT_BY_SYSTEM;                       // 预测帧送显模式
   19. integrationInfo.textureCachedByGame = false;                              // 输入的颜色纹理游戏侧缓存 系统不会复制一份再做预测 默认游戏不会缓存
   20. integrationInfo.needFlipInputColor = false;                               // 颜色纹理需要翻转 默认false
   21. integrationInfo.needFlipOutputColor = false;                              // 预测帧需要翻转 默认false
   22. // 设置超帧预测的集成信息
   23. errorCode = HMS_FG_SetIntegrationMode_VK(m_context, &integrationInfo);
   24. if (errorCode != FG_SUCCESS) {
   25. return false;
   26. }
   ```
6. 调用[HMS\_FG\_Activate\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_activate_vk)接口激活超帧上下文实例。

   ```
   1. // 激活超帧上下文实例
   2. errorCode = HMS_FG_Activate_VK(m_context);
   3. if (errorCode != FG_SUCCESS) {
   4. return false;
   5. }
   ```
7. 调用[HMS\_FG\_CreateImage\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_createimage_vk)接口创建真实渲染帧颜色缓冲区图像实例。

   ```
   1. // 变量声明
   2. VkImage inputColorImage = VK_NULL_HANDLE;
   3. VkImageView inputColorImageView = VK_NULL_HANDLE;

   5. // 创建真实帧颜色缓冲区图像实例
   6. FG_Image_VK* inputColor = HMS_FG_CreateImage_VK(m_context, inputColorImage, inputColorImageView);
   7. if (!inputColor) {
   8. return false;
   9. }
   ```
8. 游戏运行中，渲染真实帧时，缓存颜色信息和相机矩阵等属性信息。渲染预测帧时，需调用[HMS\_FG\_Dispatch\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_dispatch_vk)接口并传入真实帧属性信息，指定预测帧缓冲区索引，生成预测帧。游戏送显自己真实帧，系统会在真实帧和上一帧间完成预测帧的展示。

   ```
   1. // 帧循环
   2. while (true) {
   3. // 真实帧渲染阶段
   4. // 渲染当前帧渲染画面，缓存颜色、相机矩阵等信息，用于下一帧预测帧生成
   5. // ...

   7. // 绘制真实帧
   8. // ...

   10. // 绘制UI
   11. // ...

   13. // 预测帧渲染阶段
   14. // 设置预测帧生成前真实帧颜色缓冲区同步状态
   15. FG_ImageSync_VK inputColorInitImageSync{};
   16. inputColorInitImageSync.stages = VK_PIPELINE_STAGE_COLOR_ATTACHMENT_OUTPUT_BIT;
   17. inputColorInitImageSync.layout = VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL;
   18. inputColorInitImageSync.accessMask = VK_ACCESS_COLOR_ATTACHMENT_WRITE_BIT;

   20. // 设置预测帧生成后真实帧颜色缓冲区同步状态
   21. FG_ImageSync_VK inputColorFinalImageSync{};
   22. inputColorFinalImageSync.stages = VK_PIPELINE_STAGE_TRANSFER_BIT;
   23. inputColorFinalImageSync.layout = VK_IMAGE_LAYOUT_TRANSFER_SRC_OPTIMAL;
   24. inputColorFinalImageSync.accessMask = VK_ACCESS_TRANSFER_READ_BIT;

   26. // 创建真实帧颜色缓冲区图像属性实例
   27. FG_ImageInfo_VK inputColorImageInfo{};
   28. inputColorImageInfo.image = inputColor;
   29. inputColorImageInfo.initialSync = inputColorInitImageSync;
   30. inputColorImageInfo.finalSync = inputColorFinalImageSync;

   32. // 帧生成属性配置结构体
   33. FG_DispatchDescription_VK dispatchDescription{};
   34. // 传入真实渲染帧颜色缓冲区属性信息
   35. dispatchDescription.inputColorInfo = inputColorImageInfo;

   37. // 变量声明
   38. FG_Mat4x4 preViewProj;
   39. FG_Mat4x4 preInvViewProj;
   40. VkCommandBuffer vkCommandBuffer = VK_NULL_HANDLE;

   42. // 传入上一帧真实渲染帧视图投影矩阵
   43. dispatchDescription.viewProj = preViewProj;
   44. // 传入上一帧真实渲染帧视图投影逆矩阵
   45. dispatchDescription.invViewProj = preInvViewProj;
   46. // 传入用于录入超帧绘制指令的命令缓冲区句柄
   47. dispatchDescription.vkCommandBuffer = vkCommandBuffer;

   49. // 生成预测帧
   50. errorCode = HMS_FG_Dispatch_VK(m_context, &dispatchDescription);
   51. if (errorCode != FG_SUCCESS) {
   52. return false;
   53. }

   55. switch (errorCode) {
   56. case FG_SUCCESS: {
   57. // 预测成功
   58. break;
   59. }
   60. case FG_COLLECTING_PREVIOUS_FRAMES:
   61. // 传入真实帧数量未达到固定阈值，无预测帧生成，外插模式传入真实帧数量<3时返回该状态码，此时不要将预测帧送显
   62. break;
   63. default:
   64. // 预测帧生成失败
   65. break;
   66. }

   68. // 送显真实帧
   69. // ...
   70. }
   ```
9. 调用[HMS\_FG\_DestroyContext\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_destroycontext_vk)接口销毁超帧实例，释放内存资源。

   ```
   1. // 销毁超帧上下文实例并释放内存资源
   2. errorCode = HMS_FG_DestroyContext_VK(&m_context);
   3. if (errorCode != FG_SUCCESS) {
   4. return false;
   5. }
   ```
