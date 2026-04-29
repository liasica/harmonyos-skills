---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-fg-extrapolation-gles
title: OpenGL ES平台
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏渲染加速服务 > 超帧功能开发 > 外插模式 > OpenGL ES平台
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c1b290598bf950f834e6c68ef953b17b45e406b3dd5a4c4b592470148f3c72d9
---

## 业务流程

基于OpenGL ES图形API平台，超帧外插模式的主要业务流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/TrjFqJFCTfiMc50NYAUg1w/zh-cn_image_0000002558605552.png?HW-CC-KV=V1&HW-CC-Date=20260429T053623Z&HW-CC-Expire=86400&HW-CC-Sign=D910375C1C5F92CA2936DE810E0C9BD6B75537E96B52B1EAEACB7DD2A75A09B7)

1. 用户进入超帧适用的游戏场景。
2. 游戏应用调用[HMS\_FG\_CreateContext\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_createcontext_gles)接口创建超帧上下文实例。如超帧上下文实例创建失败，则无需进入步骤5到步骤8的真实帧、预测帧交替渲染送显的循环流程，只需逐帧对场景进行渲染送显即可。
3. 游戏应用调用接口配置超帧实例属性。包括调用[HMS\_FG\_SetAlgorithmMode\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_setalgorithmmode_gles)（必选）设置超帧算法模式并选择外插模式；调用[HMS\_FG\_SetResolution\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_setresolution_gles)（必选）设置超帧输入输出图像分辨率；调用[HMS\_FG\_SetCvvZSemantic\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_setcvvzsemantic_gles)（可选）设置齐次裁剪空间Z/W范围及深度测试函数；调用[HMS\_FG\_SetImageFormat\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_setimageformat_gles)（可选）设置真实渲染帧颜色缓冲区图像格式；如果颜色缓冲区相对深度模板缓冲区基于y轴翻转180度，则调用[HMS\_FG\_SetDepthStencilYDirectionInverted\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_setdepthstencilydirectioninverted_gles)（可选）设置翻转状态。
4. 游戏应用调用[HMS\_FG\_Activate\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_activate_gles)接口激活超帧上下文实例。
5. 渲染游戏场景绘制真实渲染帧，缓存真实帧颜色信息、深度信息和相机矩阵等信息，用于后续超帧预测。
6. 真实渲染帧绘制UI并送显。
7. 游戏应用调用[HMS\_FG\_Dispatch\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_dispatch_gles)接口并传入历史真实渲染帧颜色信息、深度信息、相机矩阵等信息，生成预测帧，并更新预测帧缓冲区。当相机视图投影矩阵的平移分量非常大时（如超过10W），预测帧效果下降，画面易出现闪烁现象。此时可在[HMS\_FG\_Dispatch\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_dispatch_gles)接口调用前调用[HMS\_FG\_SetExtendedCameraInfo\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_setextendedcamerainfo_gles)设置相机扩展信息，从而获取精度更高的预测帧效果。
8. 预测帧绘制UI并送显，跳转至步骤5继续执行，直到退出游戏场景。
9. 用户退出超帧适用的游戏场景。
10. 游戏应用调用[HMS\_FG\_DestroyContext\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_destroycontext_gles)接口销毁超帧上下文实例并释放内存资源。

## 开发步骤

注意

外插模式需要标记模板缓冲的第8位，用于区分静态物体和动态物体。静态物体所占区域的模板值需标记为0xxx xxxx，动态物体所占区域的模板值需标记为1xxx xxxx，模板缓冲的低7位模板值开发者可自行设置。如果标记错误或漏标记，可能会造成超帧预测效果不准确，如运动物体边缘区域拖影等现象。

本节阐述基于OpenGL ES图形API平台的超帧调用示例。详细代码请参考[图形开发Sample（超帧GLES）](https://gitcode.com/harmonyos_samples/frame-generation-gles-samplecode-clientdemo-cpp)。

1. 引用Graphics Accelerate Kit超帧头文件：frame\_generation\_gles.h。

   ```
   1. // 引用超帧frame_generation_gles.h头文件
   2. #include <graphics_game_sdk/frame_generation_gles.h>
   ```
2. 编写CMakeLists.txt。

   ```
   1. find_library(
   2. # Sets the name of the path variable.
   3. framegeneration-lib
   4. # Specifies the name of the NDK library that you want CMake to locate.
   5. libframegeneration.so
   6. )

   8. target_link_libraries(entry PUBLIC
   9. ${framegeneration-lib}
   10. )
   ```
3. 调用[HMS\_FG\_CreateContext\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_createcontext_gles)接口创建超帧上下文实例。如果返回nullptr，则说明超帧上下文实例创建失败，或当前硬件设备不支持开启超帧。

   ```
   1. // 创建超帧上下文实例
   2. FG_Context_GLES* context_ = HMS_FG_CreateContext_GLES();
   3. if (context_ == nullptr) {
   4. return false;
   5. }
   ```
4. 调用超帧实例属性配置接口，超帧算法模式选择外插模式。

   ```
   1. // 初始化超帧接口调用错误码
   2. FG_ErrorCode errorCode = FG_SUCCESS;

   4. // 超帧算法模式
   5. FG_AlgorithmModeInfo aInfo{};
   6. aInfo.predictionMode = FG_PREDICTION_MODE_EXTRAPOLATION;                  // 外插模式
   7. aInfo.meMode = FG_ME_MODE_BASIC;                                          // 运动估计基础模式
   8. errorCode = HMS_FG_SetAlgorithmMode_GLES(context_, &aInfo);               // [必选] 设置超帧算法模式
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
   30. errorCode = HMS_FG_SetResolution_GLES(context_, &rInfo);                  // [必选] 设置超帧输入输出图像分辨率
   31. if (errorCode != FG_SUCCESS) {
   32. return false;
   33. }

   35. // [可选] 设置齐次裁剪空间Z/W范围及深度测试模式，接口不调用时默认为FG_CVV_Z_SEMANTIC_MINUS_ONE_TO_ONE_FORWARD_Z
   36. errorCode = HMS_FG_SetCvvZSemantic_GLES(context_, FG_CVV_Z_SEMANTIC_MINUS_ONE_TO_ONE_FORWARD_Z);
   37. if (errorCode != FG_SUCCESS) {
   38. return false;
   39. }

   41. // [可选] 设置真实渲染帧颜色缓冲区图像格式，接口不调用时默认为FG_FORMAT_R8G8B8A8_UNORM
   42. errorCode = HMS_FG_SetImageFormat_GLES(context_, FG_FORMAT_R8G8B8A8_UNORM);
   43. if (errorCode != FG_SUCCESS) {
   44. return false;
   45. }

   47. // [可选] 当颜色缓冲区相对深度模板缓冲区基于y轴翻转180度时，设置第二个参数为true，接口不调用时默认为无翻转
   48. errorCode = HMS_FG_SetDepthStencilYDirectionInverted_GLES(context_, true);
   49. if (errorCode != FG_SUCCESS) {
   50. return false;
   51. }
   ```
5. 调用[HMS\_FG\_Activate\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_activate_gles)接口激活超帧上下文实例。

   ```
   1. // 激活超帧上下文实例
   2. errorCode = HMS_FG_Activate_GLES(context_);
   3. if (errorCode != FG_SUCCESS) {
   4. return false;
   5. }
   ```
6. 游戏运行中，真实渲染帧和预测帧交替渲染并送显。渲染真实帧时，缓存颜色信息、深度信息和相机矩阵等属性信息。渲染预测帧时，需调用[HMS\_FG\_Dispatch\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_dispatch_gles)接口并传入上一帧真实帧属性信息，指定预测帧缓冲区索引，生成预测帧，最终更新预测帧缓冲区内存。

   ```
   1. // 帧计数
   2. uint32_t frameNum = 0;
   3. // 帧生成属性配置结构体
   4. FG_DispatchDescription_GLES dispatchDescriptionData_ {
   5. .inputColor = 0U,
   6. .inputDepthStencil = 0U,
   7. .viewProj{},
   8. .invViewProj{},
   9. .outputColor = 0U
   10. };

   12. // 变量声明
   13. uint32_t inputColor = 0;
   14. uint32_t inputDepthStencil = 0;
   15. uint32_t outputColor = 0;
   16. FG_Mat4x4 preViewProj;
   17. FG_Mat4x4 preInvViewProj;

   19. // 帧循环
   20. while (true) {
   21. frameNum += 1;
   22. if ((frameNum & 1) != 0) { // 真实帧渲染阶段
   23. // 渲染当前帧渲染画面，缓存颜色、深度、相机矩阵等信息，用于下一帧预测帧生成
   24. // ...

   26. // 绘制真实帧
   27. // ...

   29. // 绘制UI
   30. // ...

   32. // 送显真实帧
   33. // ...
   34. } else { // 预测帧渲染阶段
   35. // 传入上一帧真实渲染帧颜色缓冲区索引
   36. dispatchDescriptionData_.inputColor = inputColor;
   37. // 传入上一帧真实渲染帧深度模板缓冲区索引
   38. dispatchDescriptionData_.inputDepthStencil = inputDepthStencil;
   39. // 传入预测帧缓冲区索引
   40. dispatchDescriptionData_.outputColor = outputColor;
   41. // 传入上一帧真实渲染帧视图投影矩阵
   42. dispatchDescriptionData_.viewProj = preViewProj;
   43. // 传入上一帧真实渲染帧视图投影逆矩阵
   44. dispatchDescriptionData_.invViewProj = preInvViewProj;

   46. // 生成预测帧，更新预测帧缓冲区的内存
   47. errorCode = HMS_FG_Dispatch_GLES(context_, &dispatchDescriptionData_);

   49. switch (errorCode) {
   50. case FG_SUCCESS: {
   51. // 绘制预测帧
   52. // ...

   54. // 绘制UI
   55. // ...

   57. // 送显预测帧
   58. // ...
   59. break;
   60. }
   61. case FG_COLLECTING_PREVIOUS_FRAMES:
   62. // 传入真实帧数量未达到固定阈值，无预测帧生成，基础外插模式传入真实帧数量<3时返回该状态码，增强外插模式传入真实帧数量<2时返回该状态码，此时不要将预测帧送显
   63. break;
   64. default:
   65. // 预测帧生成失败
   66. return false;
   67. }
   68. }
   69. }
   ```
7. 调用[HMS\_FG\_DestroyContext\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_fg_destroycontext_gles)接口销毁超帧实例，释放内存资源。

   ```
   1. // 销毁超帧上下文实例并释放内存资源
   2. errorCode = HMS_FG_DestroyContext_GLES(&context_);
   3. if (errorCode != FG_SUCCESS) {
   4. return false;
   5. }
   ```
