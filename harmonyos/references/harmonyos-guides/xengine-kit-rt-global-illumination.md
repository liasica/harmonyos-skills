---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xengine-kit-rt-global-illumination
title: 光线追踪全局光照
breadcrumb: 指南 > 图形 > XEngine Kit（GPU加速引擎服务） > 光线追踪全局光照
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2e7fb4aaeefd2ae173d9c7c468c563e832ba8be9f9ed538152367651a4874ca3
---

从6.0.0(20) 版本开始，新增光线追踪全局光照特性。

XEngine Kit提供端侧光线追踪全局光照（Ray-Traced Global Illumination，RTGI）能力，包含动态漫反射全局光照（DDGI）算法和神经网络全局光照（NNGI）算法。

## 约束与限制

* 支持的设备类型：此特性依赖设备支持Vulkan光线追踪扩展[VK\_KHR\_acceleration\_structure](https://docs.vulkan.org/refpages/latest/refpages/source/VK_KHR_acceleration_structure.html)、[VK\_KHR\_ray\_query](https://docs.vulkan.org/refpages/latest/refpages/source/VK_KHR_ray_query.html)
* 可通过以下方式查询相关扩展特性是否支持：

  对于Vulkan，使用[HMS\_XEG\_EnumerateDeviceExtensionProperties](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)扩展特性查询接口进行查询，如查询结果包含XEG\_RTGI\_EXTENSION\_NAME，则表示支持该特性，若查询结果未包含，则表示不支持该特性。

## 应用场景

DDGI算法：根据视角中的探针信息，分帧更新探针光照，实现使用光线追踪实时渲染动态全局光照的效果。同时可与端云渲染相结合，利用端侧光追算力，计算动态全局光照，结合云侧下发的静态全局光照信息，实时生成高质量全场景光线追踪全局光照。

NNGI算法：结合了AI和光线追踪技术，通过非常小分辨率（例如64×32）对场景进行光线追踪渲染，然后将延迟渲染的几何数据和光追结果输入给NPU推理出整个场景的全局光照结果，从而实现少量光线即可实现全局光照效果。同时基于马良GPU的异构协同技术，NPU和GPU可以同时工作，降低整体时延。

## 接口说明

以下接口为RTGI设置接口，如需使用更丰富的设置和查询接口，具体API说明详见[接口文档](../harmonyos-references/xengine-kit-xengine.md)。

| 接口名 | 描述 |
| --- | --- |
| VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_EnumerateDeviceExtensionProperties (VkPhysicalDevice physicalDevice, uint32\_t \*pPropertyCount, XEG\_ExtensionProperties \*pProperties) | XEngine Vulkan扩展特性查询接口。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CreateRTGI (VkDevice device, const void \*pCreateInfo, XEG\_RTGI \*pRtGI) | 创建XEG\_RTGI对象。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CmdRenderRTGI (VkCommandBuffer commandBuffer, XEG\_RTGI rtGI, const void \*pDescription) | 执行渲染命令。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CmdSetSynchronization (VkCommandBuffer commandBuffer, const void \*xegHandle) | 设置同步信号，等待渲染结果写入指定图像。使用RTGI特性时，为等待GI渲染结果写入指定图像。 |
| VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_DestroyRTGI (XEG\_RTGI rtGI) | 销毁XEG\_RTGI对象。 |

## DDGI开发步骤

本章以Vulkan图像API集成为例，说明XEngine集成操作过程。

### 配置项目

编译HAP时，Native层so编译需要依赖NDK中的libxengine.so。

* 头文件引用

  ```
  1. #include <algorithm>
  2. #include <string>
  3. #include <vector>
  4. #include <xengine/xeg_vulkan_rtgi.h>
  5. #include <xengine/xeg_vulkan_extension.h>
  6. #include <xengine/xeg_extension_defs.h>
  ```
* 编写CMakeLists.txt

  CMakeLists.txt部分示例代码如下。

  ```
  1. find_library(
  2. # Sets the name of the path variable.
  3. xengine-lib
  4. # Specifies the name of the NDK library that you want CMake to locate.
  5. xengine
  6. )
  7. target_link_libraries(ohosmain PUBLIC
  8. ...... // 其他库文件
  9. ${xengine-lib} RenderBehavior SceneLoader VulkanBase
  10. )
  ```

### 业务流程

* 下面是基于Vulkan图形API平台集成动态漫反射全局光照的主要业务流程

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/YrsWNZKbTOyQnWjKtZ95dA/zh-cn_image_0000002583478741.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234753Z&HW-CC-Expire=86400&HW-CC-Sign=FCC21D0CD40D0573CA158E6D183A1FA0B872FE730BF6CB68FD4C55182755E9B9)

1. 用户在使用动态漫反射全局光照特性前需要查询硬件平台是否支持光线追踪扩展。
2. 用户在进入游戏初始化场景时调用HMS\_XEG\_EnumerateDeviceExtensionProperties接口查询XEngine支持的特性，当查询接口返回支持的特性列表中包含动态漫反射全局光照特性时代表可以使用此特性。
3. 创建动态漫反射全局光照使用的创建信息，调用HMS\_XEG\_CmdRenderRTGI接口创建动态漫反射全局光照实例。
4. 当游戏运行时，渲染动态漫反射全局光照特性需要的纹理。
5. 调用HMS\_XEG\_CmdRenderRTGI执行全局光照渲染任务。
6. 调用HMS\_XEG\_CmdSetSynchronization设置同步信号，等待渲染结果写入指定图像。
7. 游戏使用全局光照纹理，进行其他的渲染任务，如UI等。
8. 当前帧已全部渲染完成，进行送显。
9. 当游戏退出时，调用HMS\_XEG\_DestroyRTGI接口销毁动态漫反射全局光照实例。

### 集成XEngine RT DDGI（Vulkan）

使用Vulkan图形API搭建图像渲染管线，并集成RT DDGI在Native层实现，渲染结果通过[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件显示到屏幕。

本节阐述Vulkan图形API的RT DDGI使用。

在调用XEngine Kit能力前，需要先通过[Syscap](../harmonyos-references/syscap.md#判断-api-是否可以使用)查询您的目标设备是否支持SystemCapability.Graphic.XEngine系统能力。

1. 调用[HMS\_XEG\_EnumerateDeviceExtensionProperties](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口，获取XEngine支持的扩展信息，只有在支持XEG\_RTGI\_EXTENSION\_NAME扩展时才可以使用RT DDGI的相关接口。

   ```
   1. // physicalDevice为Vulkan物理设备，用户需进行初始化
   2. VkPhysicalDevice physicalDevice;
   3. // 查询XEngine支持的Vulkan扩展列表
   4. std::vector<std::string> supportedExtensions;
   5. uint32_t propertyCount;
   6. HMS_XEG_EnumerateDeviceExtensionProperties(physicalDevice, &propertyCount, nullptr);
   7. if (propertyCount> 0) {
   8. std::vector<XEG_ExtensionProperties> properties(propertyCount);
   9. if (HMS_XEG_EnumerateDeviceExtensionProperties(physicalDevice, &propertyCount,
   10. &properties.front()) == VK_SUCCESS) {
   11. for (auto ext : properties) {
   12. supportedExtensions.push_back(ext.extensionName);
   13. }
   14. }
   15. }
   16. // 查询是否支持RT DDGI
   17. if (std::find(supportedExtensions.begin(), supportedExtensions.end(), XEG_RTGI_EXTENSION_NAME) ==
   18. supportedExtensions.end()) {
   19. exit(1);
   20. }
   ```
2. 声明实例句柄。

   ```
   1. XEG_RTGI xegRTGI;
   ```
3. 调用[HMS\_XEG\_CreateRTGI](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_creatertgi)接口，创建RT DDGI实例。

   ```
   1. // 渲染宽高以及缩放倍率可以由用户设定，这里用1280*720为例，缩放倍率为1
   2. VkExtent2D outputSize;
   3. outputSize.width = 1280;
   4. outputSize.height = 720;
   5. VkExtent2D scaled;
   6. scaled.width = 1;
   7. scaled.height = 1;
   8. // Vulkan逻辑设备，用户需进行初始化
   9. VkDevice device;
   10. // XEG_DDGICreateInfo为创建XEG_RTGI对象所需信息
   11. struct XEG_DDGICreateInfo DDGICreateInfo;
   12. // 指定当前结构体类型为create info
   13. DDGICreateInfo.sType = XEG_STRUCTURE_TYPE_DDGI_CREATE_INFO;
   14. // 指定扩展为空
   15. DDGICreateInfo.pNext = nullptr;
   16. // 指定质量模式为平衡
   17. DDGICreateInfo.qualityMode = XEG_RTGI_QUALITY_MODE_BALANCED;
   18. // 指定当前场景中需要同时渲染的最大体积数量，范围为[1, 9]
   19. DDGICreateInfo.numberVolume = 4;
   20. // 指定渲染宽高缩小倍率，建议范围为[1, 4]，必须不小于1
   21. DDGICreateInfo.scaledView = scaled;
   22. // 指定输出GI图像的渲染宽高
   23. DDGICreateInfo.viewSize = outputSize;
   24. // 指定是否开启端云模式，true为开启，false为关闭
   25. DDGICreateInfo.enableCloud = false;
   26. VkResult res = HMS_XEG_CreateRTGI(device, &DDGICreateInfo, &xegRTGI);
   27. if (res != VK_SUCCESS) {
   28. exit(1);
   29. }
   ```
4. 调用[HMS\_XEG\_CmdRenderRTGI](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_cmdrenderrtgi)接口执行渲染命令，每帧都需要调用。

   ```
   1. // probeIrradianceSH为用户创建的存储探针光照二阶球谐系数的3D图像的VkImageView
   2. // 存储当前接口渲染结果，通过对该图像进行三线性插值采样，可以计算GI光照值
   3. VkImageView probeIrradianceSH = VK_NULL_HANDLE;
   4. // 定义XEG_DDGIVolumeEntryParameters对象DDGIVolumeEntryParameters
   5. struct XEG_DDGIVolumeEntryParameters DDGIVolumeEntryParameters;
   6. // 体积索引，范围为[0, 65535]，且唯一
   7. DDGIVolumeEntryParameters.volumeIndex = 0;
   8. // 探针发射光线数量，范围为[1, 1024]
   9. DDGIVolumeEntryParameters.raysPerProbe = 128;
   10. // 光线求交最远距离
   11. DDGIVolumeEntryParameters.probeMaxRayDistance = 1000.0f;
   12. // 体积中心点坐标
   13. DDGIVolumeEntryParameters.volumePosition[0] = 0.0f;
   14. DDGIVolumeEntryParameters.volumePosition[1] = 0.0f;
   15. DDGIVolumeEntryParameters.volumePosition[2] = 0.0f;
   16. // 探针放置间距，必须大于0
   17. DDGIVolumeEntryParameters.probeSpacing[0] = 10.0f;
   18. DDGIVolumeEntryParameters.probeSpacing[1] = 10.0f;
   19. DDGIVolumeEntryParameters.probeSpacing[2] = 10.0f;
   20. // 体积光照通道标记
   21. DDGIVolumeEntryParameters.volumeLightingChannelMask = 0xFFFFFFFF;
   22. // 探针放置数量，必须大于0，范围为[1, 32]
   23. DDGIVolumeEntryParameters.volumeProbeGridCounts[0] = 6;
   24. DDGIVolumeEntryParameters.volumeProbeGridCounts[1] = 6;
   25. DDGIVolumeEntryParameters.volumeProbeGridCounts[2] = 6;
   26. // 光照的伽马校正系数，必须不为0
   27. DDGIVolumeEntryParameters.volumeProbeIrradianceEncodingGamma = 5.0f;
   28. // 探针光照历史权重，范围为[0, 1]
   29. DDGIVolumeEntryParameters.probeHysteresis = 0.95f;
   30. // 探针变化阈值
   31. DDGIVolumeEntryParameters.probeChangeThreshold = 1.0f;
   32. // 探针亮度阈值
   33. DDGIVolumeEntryParameters.probeBrightnessThreshold = 1.0f;
   34. // 探针法向偏移量
   35. DDGIVolumeEntryParameters.volumeNormalBias = 0.12f;
   36. // 探针视角偏移量
   37. DDGIVolumeEntryParameters.volumeViewBias = 0.48f;
   38. // 体积光照混合距离
   39. DDGIVolumeEntryParameters.volumeBlendDistance = 1.0;
   40. // 体积边缘光照渐暗范围
   41. DDGIVolumeEntryParameters.volumeBlendDistanceBlack = 1.0;
   42. // 探针反向判断阈值
   43. DDGIVolumeEntryParameters.probeBackfaceThreshold = 1.0;
   44. // 探针正向最小距离
   45. DDGIVolumeEntryParameters.probeMinFrontfaceDistance = 1.0;
   46. // 体积光照缩放倍率，必须非负
   47. DDGIVolumeEntryParameters.volumeIrradianceScalar = 1.0;
   48. // 发射光线强度倍率，必须非负
   49. DDGIVolumeEntryParameters.emissiveMultiplier = 1.0;
   50. // 光照倍率，必须非负
   51. DDGIVolumeEntryParameters.lightingMultiplier = 1.0;
   52. // 是否强制更新所有探针，true为强制全部更新，false为选择部分更新
   53. DDGIVolumeEntryParameters.bForceUpdate = false;
   54. DDGIVolumeEntryParameters.probeIrradianceSH = probeIrradianceSH;

   56. // 定义XEG_DDGIDescription对象DDGIDescription
   57. struct XEG_DDGIDescription DDGIDescription;
   58. // inputNormalImage为用户创建的法线图像的VkImageView
   59. VkImageView inputNormalImage = VK_NULL_HANDLE;
   60. // inputDepthImage为用户创建的深度图像的VkImageView
   61. VkImageView inputDepthImage = VK_NULL_HANDLE;
   62. // inputBasecolorMetallicImage为用户创建的颜色及金属度图像的VkImageView
   63. VkImageView inputBasecolorMetallicImage = VK_NULL_HANDLE;
   64. // inputDirectionImage为用户创建的发射光线方向图像的VkImageView
   65. VkImageView inputDirectionImage = VK_NULL_HANDLE;
   66. // inputRayRadianceDistanceImage为用户创建的发射光线交点光照及距离图像的VkImageView
   67. VkImageView inputRayRadianceDistanceImage = VK_NULL_HANDLE;
   68. // inputRayHitNormalAndMetallicImage为用户创建的发射光线交点法线及金属度图像的VkImageView
   69. VkImageView inputRayHitNormalAndMetallicImage = VK_NULL_HANDLE;
   70. // inputVolumeIndexAndProbeIndex为用户创建的输入probe索引缓冲区VkBuffer
   71. VkBuffer inputVolumeIndexAndProbeIndex = VK_NULL_HANDLE;
   72. // outputVolumeIndexAndProbeIndex为用户创建的输出probe索引缓冲区VkBuffer
   73. VkBuffer outputVolumeIndexAndProbeIndex = VK_NULL_HANDLE;
   74. // outputProbeCount为用户创建的输出probe数量缓冲区VkBuffer
   75. VkBuffer outputProbeCount = VK_NULL_HANDLE;
   76. // outputGIImage为用户创建的全局光照图像的VkImageView
   77. VkImageView outputGIImage = VK_NULL_HANDLE;
   78. // commandBuffer为命令缓冲区，用户需进行初始化
   79. VkCommandBuffer commandBuffer = VK_NULL_HANDLE;
   80. // 指定当前结构体类型为DDGI description
   81. DDGIDescription.sType = XEG_STRUCTURE_TYPE_DDGI_DESCRIPTION;
   82. // 指定扩展为空
   83. DDGIDescription.pNext = nullptr;
   84. // 设置相机相关矩阵
   85. for (uint32_t i = 0; i < 16; ++i) {
   86. DDGIDescription.viewMatrix[i] = 1.0f;
   87. DDGIDescription.projectionMatrix[i] = 1.0f;
   88. }
   89. DDGIDescription.inputNormalImage = inputNormalImage;
   90. DDGIDescription.inputDepthImage = inputDepthImage;
   91. DDGIDescription.inputBasecolorMetallicImage = inputBasecolorMetallicImage;
   92. DDGIDescription.inputDirectionImage = inputDirectionImage;
   93. DDGIDescription.inputRayRadianceDistanceImage = inputRayRadianceDistanceImage;
   94. DDGIDescription.inputRayHitNormalAndMetallicImage = inputRayHitNormalAndMetallicImage;
   95. DDGIDescription.inputVolumeIndexAndProbeIndex = inputVolumeIndexAndProbeIndex;
   96. // 输入probe信息数量
   97. DDGIDescription.inputProbeCount = 10;
   98. DDGIDescription.outputVolumeIndexAndProbeIndex = outputVolumeIndexAndProbeIndex;
   99. DDGIDescription.outputProbeCount = outputProbeCount;
   100. DDGIDescription.outputGIImage = outputGIImage;
   101. // 使用的volume数量
   102. DDGIDescription.enableVolumeNumber = 1;
   103. DDGIDescription.pVolumeEntryParameters = &DDGIVolumeEntryParameters;
   104. HMS_XEG_CmdRenderRTGI(commandBuffer, xegRTGI, &DDGIDescription);
   ```
5. 若使用延迟渲染管线，则可以在调用[HMS\_XEG\_CmdRenderRTGI](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_cmdrenderrtgi)接口之后，调用[HMS\_XEG\_CmdSetSynchronization](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_cmdsetsynchronization)接口，设置同步信号，等待GI渲染结果写入指定图像，[HMS\_XEG\_CmdSetSynchronization](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_cmdsetsynchronization)接口需要每帧调用。

   ```
   1. // GI渲染结果会写入到XEG_DDGIDescription中的outputGIImage图像中
   2. HMS_XEG_CmdSetSynchronization(commandBuffer, &xegRTGI);
   ```
6. 调用[HMS\_XEG\_DestroyRTGI](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_destroyrtgi)接口销毁实例。

   ```
   1. if (xegRTGI) {
   2. HMS_XEG_DestroyRTGI(xegRTGI);
   3. }
   ```

## NNGI开发步骤

本章以Vulkan图像API集成为例，说明XEngine集成操作过程。

### 配置项目

编译HAP时，Native层so编译需要依赖NDK中的libxengine.so。

* 头文件引用

  ```
  1. #include <algorithm>
  2. #include <string>
  3. #include <vector>
  4. #include "xengine/xeg_vulkan_rtgi.h"
  5. #include "xengine/xeg_vulkan_extension.h"
  ```
* 编写CMakeLists.txt

  CMakeLists.txt部分示例代码如下。

  ```
  1. find_library(
  2. # Sets the name of the path variable.
  3. xengine-lib
  4. # Specifies the name of the NDK library that you want CMake to locate.
  5. xengine
  6. )
  7. target_link_libraries(nativerender PUBLIC
  8. ...... // 其他库文件
  9. ${xengine-lib})
  ```

### 业务流程

下面是基于Vulkan图形API平台集成神经网络全局光照的主要业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/Io8dDrIRTouFO-nGGQt2Lg/zh-cn_image_0000002552799092.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234753Z&HW-CC-Expire=86400&HW-CC-Sign=E429B2BDCDDC1E394E8E22CA82160BB423F95BEC30D3BCCBF6F2807655F62D08)

1. 用户在使用神经网络全局光照特性前需要查询硬件平台是否支持光线追踪扩展。
2. 用户在进入游戏初始化场景时调用HMS\_XEG\_EnumerateDeviceExtensionProperties接口查询XEngine支持的特性，当查询接口返回支持的特性列表中包含神经网络全局光照特性时代表可以使用此特性。
3. 创建神经网络全局光照使用的创建信息，调用HMS\_XEG\_CmdRenderRTGI接口创建神经网络全局光照实例。
4. 当游戏运行时，渲染神经网络全局光照特性需要的纹理。
5. 调用HMS\_XEG\_CmdRenderRTGI执行全局光照渲染任务。
6. 调用HMS\_XEG\_CmdSetSynchronization执行训练任务。
7. 游戏使用全局光照纹理，进行其他的渲染任务，如UI等。
8. 当前帧已全部渲染完成，进行送显。
9. 当游戏退出时，调用HMS\_XEG\_DestroyRTGI接口销毁神经网络全局光照实例。

### 集成XEngine RT NNGI（Vulkan）

使用Vulkan图形API搭建图像渲染管线，并集成RT NNGI在Native层实现，渲染结果通过[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件显示到屏幕。

本节阐述Vulkan图形API的RT NNGI使用。

在调用XEngine Kit能力前，需要先通过[Syscap](../harmonyos-references/syscap.md#判断-api-是否可以使用)查询您的目标设备是否支持SystemCapability.Graphic.XEngine系统能力。

1. 调用[HMS\_XEG\_EnumerateDeviceExtensionProperties](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口，获取XEngine支持的扩展信息，只有在支持XEG\_RTGI\_EXTENSION\_NAME扩展时才可以使用RT NNGI的相关接口。

   ```
   1. // physicalDevice为Vulkan物理设备，用户需进行初始化
   2. VkPhysicalDevice physicalDevice;
   3. // 查询XEngine支持的Vulkan扩展列表
   4. std::vector<std::string> supportedExtensions;
   5. uint32_t propertyCount;
   6. HMS_XEG_EnumerateDeviceExtensionProperties(physicalDevice, &propertyCount, nullptr);
   7. if (propertyCount> 0) {
   8. std::vector<XEG_ExtensionProperties> properties(propertyCount);
   9. if (HMS_XEG_EnumerateDeviceExtensionProperties(physicalDevice, &propertyCount,
   10. &properties.front()) == VK_SUCCESS) {
   11. for (auto ext : properties) {
   12. supportedExtensions.push_back(ext.extensionName);
   13. }
   14. }
   15. }
   16. // 查询是否支持RT NNGI
   17. if (std::find(supportedExtensions.begin(), supportedExtensions.end(), XEG_RTGI_EXTENSION_NAME) ==
   18. supportedExtensions.end()) {
   19. exit(1);
   20. }
   ```
2. 声明实例句柄。

   ```
   1. XEG_RTGI xegRTGI;
   ```
3. 调用[HMS\_XEG\_CreateRTGI](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_creatertgi)接口，创建RT NNGI实例。

   ```
   1. // Vulkan逻辑设备，用户需进行初始化
   2. VkDevice device;
   3. // XEG_DDGICreateInfo为创建XEG_RTGI对象所需信息
   4. XEG_NNGICreateInfo NNGICreateInfo;
   5. // 指定当前结构体类型为create info
   6. NNGICreateInfo.sType = XEG_STRUCTURE_TYPE_NNGI_CREATE_INFO;
   7. // 指定扩展为空
   8. NNGICreateInfo.pNext = nullptr;
   9. // 指定质量模式为平衡
   10. NNGICreateInfo.qualityMode = XEG_RTGI_QUALITY_MODE_BALANCED;
   11. // 指定推理输入图像的分辨率
   12. NNGICreateInfo.inferenceInputSize = {1280,720};
   13. // 指定推理输出图像的分辨率，当前仅支持（640，328）
   14. NNGICreateInfo.inferenceOutputSize = {640, 368};
   15. // 指定训练图像的分辨率
   16. NNGICreateInfo.trainingSize = {64, 32};
   17. VkResult res = HMS_XEG_CreateRTGI(device, &NNGICreateInfo, &xegRTGI);
   18. if (res != VK_SUCCESS) {
   19. exit(1);
   20. }
   ```
4. 调用[HMS\_XEG\_CmdRenderRTGI](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_cmdrenderrtgi)接口执行渲染命令，每帧都需要调用。

   ```
   1. // 定义XEG_NNGIDescription对象NNGIDescription
   2. struct XEG_NNGIDescription NNGIDescription;
   3. // inferenceInputDepthImage为用户创建的推理输入深度图像的VkImageView
   4. VkImageView inferenceInputDepthImage = VK_NULL_HANDLE;
   5. // inferenceInputNormalImage为用户创建的推理输入法向量图像的VkImageView
   6. VkImageView inferenceInputNormalImage = VK_NULL_HANDLE;
   7. // inferenceInputBaseColorMetallicImage为用户创建的推理输入基础颜色和金属度图像的VkImageView
   8. VkImageView inferenceInputBaseColorMetallicImage = VK_NULL_HANDLE;
   9. // inferenceOutputGIImage为用户创建的推理输出全局光照图像的VkImageView
   10. VkImageView inferenceOutputGIImage = VK_NULL_HANDLE;
   11. // trainingInputPositionImage为用户创建的训练输入位置图像的VkImageView
   12. VkImageView trainingInputPositionImage = VK_NULL_HANDLE;
   13. // trainingInputNormalImage为用户创建的训练输入法向量图像的VkImageView
   14. VkImageView trainingInputNormalImage = VK_NULL_HANDLE;
   15. // trainingInputBaseColorMetallicImage为用户创建的训练输入基础颜色和金属度图像的VkImageView
   16. VkImageView trainingInputBaseColorMetallicImage = VK_NULL_HANDLE;
   17. // trainingInputGIImage为用户创建的训练输入全局光照图像的VkImageView
   18. VkImageView trainingInputGIImage = VK_NULL_HANDLE;
   19. // sceneAabb为用户创建的渲染包围盒范围VkAabbPositionsKHR
   20. VkAabbPositionsKHR sceneAabb = {0,0,0,1,1,1};
   21. // isSceneUnbounded指定渲染场景是否无界，当前只支持false
   22. bool isSceneUnbounded = false;
   23. // spatialScaleFactor为场景缩放因子，对于有界场景，无需设置，XEngine根据sceneAabb计算该值
   24. float spatialScaleFactor = 0;
   25. // commandBuffer为命令缓冲区，用户需进行初始化
   26. VkCommandBuffer commandBuffer = VK_NULL_HANDLE;
   27. // 指定当前结构体类型为DDGI description
   28. NNGIDescription.sType = XEG_STRUCTURE_TYPE_NNGI_DESCRIPTION;
   29. // 指定扩展为空
   30. NNGIDescription.pNext = nullptr;
   31. // 设置推理图像的相机相关矩阵，此处仅为示例，使用时需要用户进行初始化
   32. float inferenceCameraViewMatrix[16];
   33. float inferenceCameraProjectionMatrix[16];
   34. memcpy(NNGIDescription.inferenceCameraViewMatrix, &inferenceCameraViewMatrix, sizeof(NNGIDescription.inferenceCameraViewMatrix));
   35. memcpy(NNGIDescription.inferenceCameraProjectionMatrix, &inferenceCameraProjectionMatrix, sizeof(NNGIDescription.inferenceCameraProjectionMatrix));
   36. // 设置训练图像的相机相关矩阵，此处仅为示例，使用时需要用户进行初始化
   37. float trainingCameraViewMatrix[16];
   38. float trainingCameraProjectionMatrix[16];
   39. memcpy(NNGIDescription.trainingCameraViewMatrix, &trainingCameraViewMatrix, sizeof(NNGIDescription.trainingCameraViewMatrix));
   40. memcpy(NNGIDescription.trainingCameraProjectionMatrix, &trainingCameraProjectionMatrix, sizeof(NNGIDescription.trainingCameraProjectionMatrix));
   41. NNGIDescription.inferenceInputDepthImage = inferenceInputDepthImage;
   42. NNGIDescription.inferenceInputNormalImage = inferenceInputNormalImage;
   43. NNGIDescription.inferenceInputBaseColorMetallicImage = inferenceInputBaseColorMetallicImage;
   44. NNGIDescription.inferenceOutputGIImage = inferenceOutputGIImage;
   45. NNGIDescription.trainingInputPositionImage = trainingInputPositionImage;
   46. NNGIDescription.trainingInputNormalImage = trainingInputNormalImage;
   47. NNGIDescription.trainingInputBaseColorMetallicImage = trainingInputBaseColorMetallicImage;
   48. NNGIDescription.trainingInputGIImage = trainingInputGIImage;
   49. NNGIDescription.sceneAabb = sceneAabb;
   50. NNGIDescription.isSceneUnbounded = isSceneUnbounded;
   51. NNGIDescription.spatialScaleFactor = spatialScaleFactor;
   52. HMS_XEG_CmdRenderRTGI(commandBuffer, xegRTGI, &NNGIDescription);
   ```
5. 在调用[HMS\_XEG\_CmdRenderRTGI](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_cmdrenderrtgi)接口之后，调用[HMS\_XEG\_CmdSetSynchronization](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_cmdsetsynchronization)接口，执行训练步骤，[HMS\_XEG\_CmdSetSynchronization](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_cmdsetsynchronization)接口需要每帧调用。

   ```
   1. // GI渲染结果会写入到XEG_NNGIDescription中的inferenceOutputGIImage图像中
   2. HMS_XEG_CmdSetSynchronization(commandBuffer, &xegRTGI);
   ```
6. 调用[HMS\_XEG\_DestroyRTGI](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_destroyrtgi)接口销毁实例。

   ```
   1. if (xegRTGI) {
   2. HMS_XEG_DestroyRTGI(xegRTGI);
   3. }
   ```
