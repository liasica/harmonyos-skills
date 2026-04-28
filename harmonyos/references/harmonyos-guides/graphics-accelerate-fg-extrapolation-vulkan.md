---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-fg-extrapolation-vulkan
title: Vulkan平台
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏渲染加速服务 > 超帧功能开发 > 外插模式 > Vulkan平台
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4b20e90f669881033bc4b5d3f6c97d98e7e2e2508a6eb3cf292bd633ee3ba61c
---

## 业务流程

基于Vulkan图形API平台，超帧外插模式的主要业务流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/UINv9mOFTjaCapA76H3N8g/zh-cn_image_0000002552799060.png?HW-CC-KV=V1&HW-CC-Date=20260427T234724Z&HW-CC-Expire=86400&HW-CC-Sign=F4B64115F2FE7BF272CEE3595EF5C3576C365B854EC49E48B023639C53C9F62E)

1. 用户进入超帧适用的游戏场景。
2. 游戏应用调用[HMS\_FG\_CreateContext\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_createcontext_vk)接口创建超帧上下文实例。如超帧上下文实例创建失败，则无需进入步骤6到步骤9的真实帧、预测帧交替渲染送显的循环流程，只需逐帧对场景进行渲染送显即可。
3. 游戏应用调用接口配置超帧实例属性。包括调用[HMS\_FG\_SetAlgorithmMode\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_setalgorithmmode_vk)（必选）设置超帧算法模式并选择外插模式；调用[HMS\_FG\_SetResolution\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_setresolution_vk)（必选）设置超帧输入输出图像分辨率；调用[HMS\_FG\_SetCvvZSemantic\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_setcvvzsemantic_vk)（可选）设置齐次裁剪空间Z/W范围及深度测试函数；调用[HMS\_FG\_SetImageFormat\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_setimageformat_vk)（可选）设置超帧输入输出图像格式；如果颜色缓冲区相对深度模板缓冲区基于y轴翻转180度，则调用[HMS\_FG\_SetDepthStencilYDirectionInverted\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_setdepthstencilydirectioninverted_vk)（可选）设置翻转状态。
4. 游戏应用调用[HMS\_FG\_Activate\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_activate_vk)接口激活超帧上下文实例。
5. 游戏应用调用[HMS\_FG\_CreateImage\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_createimage_vk)接口创建真实渲染帧颜色缓冲区图像实例、深度模板缓冲区图像实例、预测帧缓冲区图像实例。该接口将游戏应用中的VkImage、VkImageView图像资源和超帧算法实现之间建立关联。
6. 渲染游戏场景绘制真实渲染帧，缓存真实帧颜色信息、深度信息和相机矩阵等信息，用于后续超帧预测。
7. 真实渲染帧绘制UI并送显。
8. 游戏应用调用[HMS\_FG\_Dispatch\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_dispatch_vk)接口并传入历史真实渲染帧颜色信息、深度信息、相机矩阵等信息，生成预测帧，并更新预测帧缓冲区。
9. 预测帧绘制UI并送显，跳转至步骤5继续执行，直到退出游戏场景。
10. 用户退出超帧适用的游戏场景。
11. 游戏应用调用[HMS\_FG\_DestroyContext\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_destroycontext_vk)接口销毁超帧上下文实例并释放内存资源。

## 开发步骤

本节阐述基于Vulkan图形API平台的超帧调用示例。详细代码请参考[图形开发Sample（超帧Vulkan）](https://gitcode.com/harmonyos_samples/frame-generation-vulkan-samplecode-clientdemo-cpp)。

1. 引用Graphics Accelerate Kit超帧头文件：frame\_generation\_vk.h。

   ```
   1. // 引用超帧frame_generation_vk.h头文件
   2. #include <graphics_game_sdk/frame_generation_vk.h>
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
3. 调用[HMS\_FG\_CreateContext\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_createcontext_vk)接口创建超帧上下文实例。如果返回nullptr，则说明超帧上下文实例创建失败，或当前硬件设备不支持开启超帧。

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
4. 调用超帧实例属性配置接口，超帧算法模式选择外插模式。

   ```
   1. // 初始化超帧接口调用错误码
   2. FG_ErrorCode errorCode = FG_SUCCESS;

   4. // 超帧算法模式
   5. FG_AlgorithmModeInfo aInfo{};
   6. aInfo.predictionMode = FG_PREDICTION_MODE_EXTRAPOLATION;                  // 外插模式
   7. aInfo.meMode = FG_ME_MODE_BASIC;                                          // 运动估计基础模式
   8. errorCode = HMS_FG_SetAlgorithmMode_VK(m_context, &aInfo);                // [必选] 设置超帧算法模式
   9. if (errorCode != FG_SUCCESS) {
   10. return false;
   11. }

   13. // 真实帧颜色缓冲区分辨率
   14. FG_Dimension2D inputColorResolution{};
   15. inputColorResolution.width = 1280;                                        // 真实帧颜色缓冲区图像宽度
   16. inputColorResolution.height = 720;                                        // 真实帧颜色缓冲区图像高度
   17. // 真实帧深度模板缓冲区分辨率
   18. FG_Dimension2D inputDepthStencilResolution{};
   19. inputDepthStencilResolution.width = 1280;                                 // 真实帧深度模板缓冲区图像宽度
   20. inputDepthStencilResolution.height = 720;                                 // 真实帧深度模板缓冲区图像高度
   21. // 预测帧分辨率
   22. FG_Dimension2D outputColorResolution{};
   23. outputColorResolution.width = 1280;                                       // 预测帧图像宽度
   24. outputColorResolution.height = 720;                                       // 预测帧图像高度
   25. // 超帧输入输出图像分辨率
   26. FG_ResolutionInfo rInfo{};
   27. rInfo.inputColorResolution = inputColorResolution;
   28. rInfo.inputDepthStencilResolution = inputDepthStencilResolution;
   29. rInfo.outputColorResolution = outputColorResolution;
   30. errorCode = HMS_FG_SetResolution_VK(m_context, &rInfo);                    // [必选] 设置超帧输入输出图像分辨率
   31. if (errorCode != FG_SUCCESS) {
   32. return false;
   33. }

   35. // [可选] 设置齐次裁剪空间Z/W范围及深度测试模式，接口不调用时默认为FG_CVV_Z_SEMANTIC_ZERO_TO_ONE_FORWARD_Z
   36. errorCode = HMS_FG_SetCvvZSemantic_VK(m_context, FG_CVV_Z_SEMANTIC_ZERO_TO_ONE_FORWARD_Z);
   37. if (errorCode != FG_SUCCESS) {
   38. return false;
   39. }

   41. // [可选] 设置超帧输入输出图像格式
   42. FG_ImageFormat_VK imageFormat{};
   43. imageFormat.inputColorFormat = VK_FORMAT_R8G8B8A8_UNORM;
   44. imageFormat.inputDepthStencilFormat = VK_FORMAT_D24_UNORM_S8_UINT;
   45. imageFormat.outputColorFormat = VK_FORMAT_R8G8B8A8_UNORM;
   46. errorCode = HMS_FG_SetImageFormat_VK(m_context, &imageFormat);
   47. if (errorCode != FG_SUCCESS) {
   48. return false;
   49. }

   51. // [可选] 当颜色缓冲区相对深度模板缓冲区基于y轴翻转180度时，设置第二个参数为true，接口不调用时默认为false
   52. errorCode = HMS_FG_SetDepthStencilYDirectionInverted_VK(m_context, true);
   53. if (errorCode != FG_SUCCESS) {
   54. return false;
   55. }
   ```
5. 调用[HMS\_FG\_Activate\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_activate_vk)接口激活超帧上下文实例。

   ```
   1. // 激活超帧上下文实例
   2. errorCode = HMS_FG_Activate_VK(m_context);
   3. if (errorCode != FG_SUCCESS) {
   4. return false;
   5. }
   ```
6. 调用[HMS\_FG\_CreateImage\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_createimage_vk)接口创建真实渲染帧颜色缓冲区图像实例、深度模板缓冲区图像实例、预测帧缓冲区图像实例。

   ```
   1. // 变量声明
   2. VkImage inputColorImage = VK_NULL_HANDLE;
   3. VkImageView inputColorImageView = VK_NULL_HANDLE;
   4. VkImage inputDepthStencilImage = VK_NULL_HANDLE;
   5. VkImageView inputDepthStencilImageView = VK_NULL_HANDLE;
   6. VkImage outputColorImage = VK_NULL_HANDLE;
   7. VkImageView outputColorImageView = VK_NULL_HANDLE;

   9. // 创建真实帧颜色缓冲区图像实例
   10. FG_Image_VK* inputColor = HMS_FG_CreateImage_VK(m_context, inputColorImage, inputColorImageView);
   11. if (!inputColor) {
   12. return false;
   13. }
   14. // 创建真实帧深度模板缓冲区图像实例
   15. FG_Image_VK* inputDepthStencil = HMS_FG_CreateImage_VK(m_context, inputDepthStencilImage, inputDepthStencilImageView);
   16. if (!inputDepthStencil) {
   17. return false;
   18. }
   19. // 创建预测帧缓冲区图像实例
   20. FG_Image_VK* outputColor = HMS_FG_CreateImage_VK(m_context, outputColorImage, outputColorImageView);
   21. if (!outputColor) {
   22. return false;
   23. }
   ```
7. 游戏运行中，真实帧和预测帧交替渲染并送显。渲染真实帧时，缓存颜色信息、深度信息和相机矩阵等属性信息。渲染预测帧时，需调用[HMS\_FG\_Dispatch\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_dispatch_vk)接口并传入上一帧真实帧属性信息，指定预测帧缓冲区索引，生成预测帧，最终更新预测帧缓冲区内存。

   ```
   1. // 帧计数
   2. uint32_t frameNum = 0;

   4. // 帧循环
   5. while (true) {
   6. frameNum += 1;
   7. if ((frameNum & 1) != 0) { // 真实帧渲染阶段
   8. // 渲染当前帧渲染画面，缓存颜色、深度、相机矩阵等信息，用于下一帧预测帧生成
   9. // ...

   11. // 绘制真实帧
   12. // ...

   14. // 绘制UI
   15. // ...

   17. // 送显真实帧
   18. // ...
   19. } else { // 预测帧渲染阶段
   20. // 设置预测帧生成前真实帧颜色缓冲区同步状态
   21. FG_ImageSync_VK inputColorInitImageSync{};
   22. inputColorInitImageSync.stages = VK_PIPELINE_STAGE_COLOR_ATTACHMENT_OUTPUT_BIT;
   23. inputColorInitImageSync.layout = VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL;
   24. inputColorInitImageSync.accessMask = VK_ACCESS_COLOR_ATTACHMENT_WRITE_BIT;

   26. // 设置预测帧生成后真实帧颜色缓冲区同步状态
   27. FG_ImageSync_VK inputColorFinalImageSync{};
   28. inputColorFinalImageSync.stages = VK_PIPELINE_STAGE_TRANSFER_BIT;
   29. inputColorFinalImageSync.layout = VK_IMAGE_LAYOUT_TRANSFER_SRC_OPTIMAL;
   30. inputColorFinalImageSync.accessMask = VK_ACCESS_TRANSFER_READ_BIT;

   32. // 创建真实帧颜色缓冲区图像属性实例
   33. FG_ImageInfo_VK inputColorImageInfo{};
   34. inputColorImageInfo.image = inputColor;
   35. inputColorImageInfo.initialSync = inputColorInitImageSync;
   36. inputColorImageInfo.finalSync = inputColorFinalImageSync;

   38. // 设置预测帧生成前深度模板缓冲区同步状态
   39. FG_ImageSync_VK depthInitImageSync{};
   40. depthInitImageSync.stages = VK_PIPELINE_STAGE_LATE_FRAGMENT_TESTS_BIT;
   41. depthInitImageSync.layout = VK_IMAGE_LAYOUT_DEPTH_STENCIL_ATTACHMENT_OPTIMAL;
   42. depthInitImageSync.accessMask = VK_ACCESS_DEPTH_STENCIL_ATTACHMENT_WRITE_BIT;

   44. // 设置预测帧生成后深度模板缓冲区同步状态
   45. FG_ImageSync_VK depthFinalImageSync{};
   46. depthFinalImageSync.stages = VK_PIPELINE_STAGE_LATE_FRAGMENT_TESTS_BIT;
   47. depthFinalImageSync.layout = VK_IMAGE_LAYOUT_DEPTH_STENCIL_ATTACHMENT_OPTIMAL;
   48. depthFinalImageSync.accessMask = VK_ACCESS_DEPTH_STENCIL_ATTACHMENT_READ_BIT;

   50. // 创建真实帧深度模板缓冲区图像属性实例
   51. FG_ImageInfo_VK depthImageInfo{};
   52. depthImageInfo.image = inputDepthStencil;
   53. depthImageInfo.initialSync = depthInitImageSync;
   54. depthImageInfo.finalSync = depthFinalImageSync;

   56. // 设置预测帧生成前预测帧缓冲区同步状态
   57. FG_ImageSync_VK outputColorInitImageSync{};
   58. outputColorInitImageSync.stages = VK_PIPELINE_STAGE_ALL_GRAPHICS_BIT;
   59. outputColorInitImageSync.layout = VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL;
   60. outputColorInitImageSync.accessMask = VK_ACCESS_SHADER_WRITE_BIT;

   62. // 设置预测帧生成后预测帧缓冲区同步状态
   63. FG_ImageSync_VK outputColorFinalImageSync{};
   64. outputColorFinalImageSync.stages = VK_PIPELINE_STAGE_TRANSFER_BIT;
   65. outputColorFinalImageSync.layout = VK_IMAGE_LAYOUT_TRANSFER_SRC_OPTIMAL;
   66. outputColorFinalImageSync.accessMask = VK_ACCESS_TRANSFER_READ_BIT;

   68. // 创建预测帧缓冲区图像属性实例
   69. FG_ImageInfo_VK outputColorImageInfo{};
   70. outputColorImageInfo.image = outputColor;
   71. outputColorImageInfo.initialSync = outputColorInitImageSync;
   72. outputColorImageInfo.finalSync = outputColorFinalImageSync;

   74. // 帧生成属性配置结构体
   75. FG_DispatchDescription_VK dispatchDescription{};
   76. // 传入真实渲染帧颜色缓冲区属性信息
   77. dispatchDescription.inputColorInfo = inputColorImageInfo;
   78. // 传入真实渲染帧深度模板缓冲区属性信息
   79. dispatchDescription.inputDepthStencilInfo = depthImageInfo;
   80. // 传入预测帧缓冲区属性信息
   81. dispatchDescription.outputColorInfo = outputColorImageInfo;

   83. // 变量声明
   84. FG_Mat4x4 preViewProj;
   85. FG_Mat4x4 preInvViewProj;
   86. VkCommandBuffer vkCommandBuffer = VK_NULL_HANDLE;

   88. // 传入上一帧真实渲染帧视图投影矩阵
   89. dispatchDescription.viewProj = preViewProj;
   90. // 传入上一帧真实渲染帧视图投影逆矩阵
   91. dispatchDescription.invViewProj = preInvViewProj;
   92. // 传入用于录入超帧绘制指令的命令缓冲区句柄
   93. dispatchDescription.vkCommandBuffer = vkCommandBuffer;
   94. // 传入当前帧序号
   95. dispatchDescription.frameIdx = 0;

   97. // 生成预测帧，更新预测帧缓冲区的内存
   98. errorCode = HMS_FG_Dispatch_VK(m_context, &dispatchDescription);
   99. if (errorCode != FG_SUCCESS) {
   100. return false;
   101. }

   103. switch (errorCode) {
   104. case FG_SUCCESS: {
   105. // 绘制预测帧
   106. // ...

   108. // 绘制UI
   109. // ...

   111. // 送显预测帧
   112. // ...
   113. break;
   114. }
   115. case FG_COLLECTING_PREVIOUS_FRAMES:
   116. // 传入真实帧数量未达到固定阈值，无预测帧生成，外插模式传入真实帧数量<3时返回该状态码，此时不要将预测帧送显
   117. break;
   118. default:
   119. // 预测帧生成失败
   120. return false;
   121. }
   122. }
   123. }
   ```
8. 调用[HMS\_FG\_DestroyContext\_VK](../harmonyos-references/_graphics_accelerate.md#hms_fg_destroycontext_vk)接口销毁超帧实例，释放内存资源。

   ```
   1. // 销毁超帧上下文实例并释放内存资源
   2. errorCode = HMS_FG_DestroyContext_VK(&m_context);
   3. if (errorCode != FG_SUCCESS) {
   4. return false;
   5. }
   ```
