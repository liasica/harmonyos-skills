---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xengine-kit-rt-shadow-and-ao
title: 光线追踪阴影和环境光遮蔽
breadcrumb: 指南 > 图形 > XEngine Kit（GPU加速引擎服务） > 光线追踪阴影和环境光遮蔽
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:44+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:1480d6cd25abf85b9711a5c279dd7e7ea4680dd1c12c4a8d53f53406ffeb2656
---

从6.0.0(20) 版本开始，新增光线追踪阴影和环境光遮蔽特性。

XEngine VisibleMask特性提供开箱即用的光线追踪阴影和环境光遮蔽（Ray-Traced Shadow and AO）渲染能力。相比于这些效果的传统光线追踪实现方式，依托于华为马良GPU的软硬结合优化，XEngine支持FERT(Flexible Entry Raytracing)求交加速技术，可以减少光线与场景几何的求交计算次数，从而降低实现高画质光追效果时的GPU负载。此外，XEngine通过高度优化的时空域降噪技术，解决光线追踪渲染时因为光线数量不足而引入的噪声问题，可以在发射较少光线数的情况下达成高画质表现，实现同等画质GPU负载更轻，同等负载下画质更好的效果。

## 约束与限制

* 支持的设备类型：此特性依赖设备支持Vulkan光线追踪扩展[VK\_KHR\_acceleration\_structure](https://docs.vulkan.org/refpages/latest/refpages/source/VK_KHR_acceleration_structure.html)、[VK\_KHR\_ray\_query](https://docs.vulkan.org/refpages/latest/refpages/source/VK_KHR_ray_query.html)。
* 可通过以下方式查询相关扩展特性是否支持：

  对于Vulkan，使用[HMS\_XEG\_EnumerateDeviceExtensionProperties](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)扩展特性查询接口进行查询，如查询结果包含XEG\_RT\_SHADOW\_AO\_EXTENSION\_NAME，则表示支持该特性，若查询结果未包含，则表示不支持该特性。

## 接口说明

以下接口为使用光线追踪阴影和环境光遮蔽特性需要使用的接口，关于这些接口的详细说明见[接口文档](../harmonyos-references/xengine-kit-xengine.md)。

| 接口名 | 描述 |
| --- | --- |
| VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_EnumerateDeviceExtensionProperties (VkPhysicalDevice physicalDevice, uint32\_t \* pPropertyCount, XEG\_ExtensionProperties \* pProperties) | XEngine Vulkan扩展特性查询接口。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CreateRTVisibleMask (VkDevice device, const void \*pCreateInfo, XEG\_RTVisibleMask \*pRTVisibleMask) | 创建XEG\_RTVisibleMask对象。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CmdRenderRTVisibleMask (VkCommandBuffer commandBuffer, XEG\_RTVisibleMask rtVisibleMask, const void \*pDescription) | 录制光线追踪VisibleMask渲染命令。 |
| VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_DestroyRTVisibleMask (XEG\_RTVisibleMask rtVisibleMask) | 销毁XEG\_RTVisibleMask对象。 |

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/nMFlo3FEROSrlkr7aIoF-w/zh-cn_image_0000002558765240.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053643Z&HW-CC-Expire=86400&HW-CC-Sign=32B3EA149BA353F99BC76A37F4772F42A6B8A27BFC951C634C73B956B6D54211)

1. 游戏进入适用光线追踪阴影和环境光遮蔽效果的游戏场景。
2. 在确认设备支持光线追踪扩展和XEG\_RT\_SHADOW\_AO\_EXTENSION\_NAME扩展时，调用HMS\_XEG\_CreateRTVisibleMask接口创建实例。
3. 游戏构建或更新场景的光线追踪加速结构
4. 在延迟渲染GBuffer渲染阶段后，调用HMS\_XEG\_CmdRenderRTVisibleMask接口计算阴影和环境光遮蔽贴图。
5. 在延迟渲染光照计算阶段，采样前一步生成的阴影和环境光遮蔽值，进行光照效果计算。
6. 进行后续渲染流程，如后处理和UI渲染，完成一帧渲染后送显当前帧。
7. 用户退出游戏场景时，游戏应用调用HMS\_XEG\_DestroyRTVisibleMask接口销毁XEngine实例。

## 开发步骤

本章以在Vulkan应用程序延迟渲染管线中集成为例，说明使用XEngine光线追踪阴影和环境光遮蔽特性的开发步骤。

### 配置项目

编译HAP时，Native层so需要依赖NDK中的XEngine相关库和头文件。

* 头文件引用

  ```
  1. #include <vector>
  2. #include <algorithm>
  3. #include <string>
  4. #include <xengine/xeg_vulkan_extension.h>
  5. #include <xengine/xeg_vulkan_rt_visible_mask.h>
  ```
* CMakeLists.txt添加库依赖

  CMakeLists.txt中添加对XEngine动态链接库依赖的代码如下。

  ```
  1. find_library(
  2. # 设置路径变量的名称。
  3. xengine-lib
  4. # 指定希望CMake定位的NDK库的名称。
  5. xengine
  6. )
  7. target_link_libraries(nativerender PUBLIC
  8. ...... // 其他库文件
  9. ${xengine-lib})
  ```

### 集成XEngine光线追踪阴影和环境光遮蔽（Vulkan）

XEngine VisibleMask特性的光线追踪阴影（Ray-Traced Shadow，简称RTShadow）和环境光遮蔽（Ray-Traced AO，简称RTAO）效果API需要与Vulkan API延迟渲染管线配合使用。相关代码在Native层实现，渲染结果通过[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件显示到屏幕。

在调用XEngine Kit特性接口前，需要先通过[Syscap](../harmonyos-references/syscap.md#判断-api-是否可以使用)查询确认您的目标设备支持SystemCapability.Graphic.XEngine系统能力。

1. 调用[HMS\_XEG\_EnumerateDeviceExtensionProperties](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口，获取XEngine支持的扩展信息，只有在支持XEG\_RT\_SHADOW\_AO\_EXTENSION\_NAME扩展时才可以使用光线追踪阴影和环境光遮蔽特性的接口。

   ```
   1. // physicalDevice为当前应用程序的Vulkan物理设备，需用户进行初始化
   2. VkPhysicalDevice physicalDevice;
   3. // 查询XEngine支持的Vulkan扩展列表
   4. std::vector<std::string> supportedExtensions;
   5. uint32_t propertyCount;
   6. HMS_XEG_EnumerateDeviceExtensionProperties(physicalDevice, &propertyCount, nullptr);
   7. if (propertyCount > 0) {
   8. std::vector<XEG_ExtensionProperties> properties(propertyCount);
   9. if (HMS_XEG_EnumerateDeviceExtensionProperties(physicalDevice, &propertyCount, &properties.front())
   10. == VK_SUCCESS) {
   11. for (auto ext : properties) {
   12. supportedExtensions.push_back(ext.extensionName);
   13. }
   14. }
   15. }
   16. // 查询是否支持XEngine光线追踪阴影和环境光遮蔽特性
   17. if (std::find(supportedExtensions.begin(), supportedExtensions.end(), XEG_RT_SHADOW_AO_EXTENSION_NAME)
   18. == supportedExtensions.end()) {
   19. exit(1);  // 不支持时处理错误
   20. }
   ```
2. 调用[HMS\_XEG\_CreateRTVisibleMask](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_creatertvisiblemask)接口，创建实例句柄。

   ```
   1. // 声明实例句柄
   2. XEG_RTVisibleMask rtVisibleMask = VK_NULL_HANDLE;
   3. // RTShadow和RTAO初始化信息
   4. XEG_RTShadowAOCreateInfo createInfo;
   5. createInfo.sType = XEG_STRUCTURE_TYPE_RT_SHADOWAO_CREATE_INFO;
   6. createInfo.pNext = nullptr;
   7. // GBuffer图像大小
   8. createInfo.rtInputGbufferSize = {1280, 720};
   9. // 输出的RTShadow和RTAO图像大小，需要与GBuffer等比例
   10. createInfo.rtShadowAOSize = {640, 360};
   11. createInfo.enableRTShadow = true;
   12. createInfo.enableRTAO = true;
   13. // 去噪器质量模式设置为平衡模式
   14. createInfo.denoiseMode = XEG_DENOISE_QUALITY_MODE_BALANCED;
   15. // 场景遍历模式设置为性能模式
   16. createInfo.traversalMode = XEG_TRAVERSAL_MODE_PERFORMANCES;
   17. createInfo.aoOnlyInShadow = false;
   18. createInfo.reverseZ = false;
   19. // device为当前应用程序的Vulkan设备对象，需用户进行初始化
   20. VkDevice device;
   21. if (HMS_XEG_CreateRTVisibleMask(device, &createInfo, &rtVisibleMask) != VK_SUCCESS) {
   22. exit(1);  // 创建失败，进行错误处理
   23. }
   ```
3. 调用[HMS\_XEG\_CmdRenderRTVisibleMask](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_cmdrenderrtvisiblemask)接口执行渲染命令，每帧都需要调用。

   ```
   1. // RTShadow算法参数设置
   2. XEG_RTShadowParameters shadowParameters;
   3. // RTAO算法参数设置
   4. XEG_RTAOParameters aoParameters;
   5. // 去噪器参数设置
   6. XEG_RTShadowAODenoiserParameters denoiserParameters;
   7. // RTShadow和RTAO渲染输入信息
   8. XEG_RTShadowAODescription description;
   9. // 光线求交只考虑不透明物体
   10. const uint32_t gl_RayFlagsOpaqueEXT = 1U;
   11. // 在找到第一个相交点时即停止光线求交查询
   12. const uint32_t gl_RayFlagsTerminateOnFirstHitEXT = 4U;
   13. const uint32_t rayFlags = (gl_RayFlagsOpaqueEXT | gl_RayFlagsTerminateOnFirstHitEXT) << 8;

   15. shadowParameters.rayTMax = 200.0f;
   16. shadowParameters.rayTMin = 1.0f;
   17. shadowParameters.sunDirection[0] = 0.1;
   18. shadowParameters.sunDirection[1] = 0.1;
   19. shadowParameters.sunDirection[2] = 0.1;
   20. shadowParameters.raySourceAngleInDegree = 0.35f;
   21. shadowParameters.shadowCullMask = rayFlags | 0xFF;
   22. shadowParameters.shadowCullDistance = 2000.0f;

   24. aoParameters.rayTMax = 30.0f;
   25. aoParameters.rayTMin = 0.1f;
   26. aoParameters.aoIntensity = 0.8f;
   27. aoParameters.aoNormalBias = 0.5f;
   28. aoParameters.aoCullMask = rayFlags | 0xFF;
   29. aoParameters.aoCullDistance = 2000.0f;

   31. denoiserParameters.temporalBlendFactor = 0.75f;
   32. denoiserParameters.positionConstantDistance = 5.0f;
   33. denoiserParameters.spatialDenoiseTimes = 2;
   34. denoiserParameters.ghostingAlpha = 0.5;
   35. denoiserParameters.spatialNormalWeight = 0.0f;
   36. denoiserParameters.spatialMaxKernelStep = 1;

   38. description.sType = XEG_STRUCTURE_TYPE_RT_SHADOWAO_DESCRIPTION;
   39. description.pNext = nullptr;
   40. description.worldCameraOrigin[0] = 0.0; // 以相机实际位置的x坐标为准
   41. description.worldCameraOrigin[1] = 0.0; // 以相机实际位置的y坐标为准
   42. description.worldCameraOrigin[2] = 0.0; // 以相机实际位置的z坐标为准
   43. // gBufferDepth是GBuffer深度图像的VkImageView，需要用户进行初始化
   44. VkImageView gBufferDepth;
   45. description.inputDepthImage = gBufferDepth;
   46. // gBufferNormal是GBuffer法线图像的VkImageView，需要用户进行初始化，关于法线的格式和编码详见API参考
   47. VkImageView gBufferNormal;
   48. description.inputNormalImage = gBufferNormal;
   49. // outputShadowAOView是保存XEngine RTShadow和RTAO渲染输出的VkImageView，需要用户进行初始化
   50. VkImageView outputShadowAOView;
   51. description.outputShadowAOImage = outputShadowAOView;
   52. // sceneTlas是场景的Top Level光线追踪加速结构，需要用户进行初始化
   53. VkAccelerationStructureKHR sceneTlas;
   54. description.accelerationStructure = sceneTlas;
   55. float viewMatrix[16]; // 相机观察矩阵，需要用户进行初始化
   56. float projectionMatrix[16]; // 相机投影矩阵，需要用户进行初始化
   57. memcpy(description.viewMatrix, viewMatrix, sizeof(viewMatrix));
   58. memcpy(description.projectionMatrix, projectionMatrix, sizeof(projectionMatrix));
   59. VkCommandBuffer vkCommandBuffer; // Vulkan命令缓冲区，需要用户进行初始化
   60. VkResult ret = HMS_XEG_CmdRenderRTVisibleMask(vkCommandBuffer, rtVisibleMask, &description);
   61. if (ret != VK_SUCCESS) {
   62. // 录制命令错误，进行错误处理
   63. }
   64. // 设置Pipeline Barrier以同步对RTShadow和RTAO渲染输出的读取
   65. VkImageMemoryBarrier imageMemoryBarrier;
   66. imageMemoryBarrier.sType = VK_STRUCTURE_TYPE_IMAGE_MEMORY_BARRIER;
   67. imageMemoryBarrier.pNext = nullptr;
   68. imageMemoryBarrier.srcAccessMask = VK_ACCESS_COLOR_ATTACHMENT_WRITE_BIT;
   69. imageMemoryBarrier.dstAccessMask = VK_ACCESS_COLOR_ATTACHMENT_READ_BIT; // 根据实际访问方式设置
   70. imageMemoryBarrier.oldLayout = VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL;
   71. imageMemoryBarrier.newLayout = VK_IMAGE_LAYOUT_SHADER_READ_ONLY_OPTIMAL;
   72. imageMemoryBarrier.srcQueueFamilyIndex = VK_QUEUE_FAMILY_IGNORED;
   73. imageMemoryBarrier.dstQueueFamilyIndex = VK_QUEUE_FAMILY_IGNORED;
   74. VkImage outputShadowAOImage; // outputShadowAO是保存RTShadow和RTAO渲染输出的VkImage，需要用户进行初始化
   75. imageMemoryBarrier.image = outputShadowAOImage;
   76. imageMemoryBarrier.subresourceRange = { VK_IMAGE_ASPECT_COLOR_BIT, 0, 1, 0, 1 };
   77. vkCmdPipelineBarrier(vkCommandBuffer,
   78. VK_PIPELINE_STAGE_COLOR_ATTACHMENT_OUTPUT_BIT,
   79. VK_PIPELINE_STAGE_FRAGMENT_SHADER_BIT, // 根据实际访问stage设置
   80. 0, 0, nullptr, 0, nullptr, 1, &imageMemoryBarrier);
   ```

   应用RTShadow和RTAO输出的outputShadowAOImage贴图到光照计算过程中，计算着色点颜色时的Shader片段示例：

   ```
   1. // lighting_pass.frag code
   2. layout (binding = 0) uniform sampler2D textureRayTracingOutputShadowAO;

   4. // color为当前着色点不考虑阴影和环境光遮蔽时的颜色值
   5. vec3 color;
   6. // 用户的着色点颜色计算过程...
   7. // 应用RTShadow和RTAO至最终光照结果
   8. vec2 shadowAO = texture(textureRayTracingOutputShadowAO, TexCoords).xy;
   9. float shadow = shadowAO.x;
   10. float ao = shadowAO.y;
   11. vec3 finalColor = color * pow(ao, 2.0) * shadow; // finalColor为最终颜色值
   ```
4. 调用[HMS\_XEG\_DestroyRTVisibleMask](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_destroyrtvisiblemask)接口销毁特性实例句柄以释放资源，在不需要再使用特性或应用退出时需要调用。

   ```
   1. if (rtVisibleMask != VK_NULL_HANDLE) {
   2. HMS_XEG_DestroyRTVisibleMask(rtVisibleMask);
   3. }
   ```
