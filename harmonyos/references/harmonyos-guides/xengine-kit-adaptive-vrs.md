---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xengine-kit-adaptive-vrs
title: 自适应VRS
breadcrumb: 指南 > 图形 > XEngine Kit（GPU加速引擎服务） > 自适应VRS
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:43+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:260f8705d248ba60d524538b24bdc3e3cb84ca4ef1ad2511b432ee25ffa5f96d
---

XEngine Kit提供自适应VRS功能，其通过合理分配画面的计算资源，视觉无损降低渲染频次，使不同的渲染图像使用不同的渲染速率，能够有效提高渲染性能。

## 约束与限制

* 支持的设备类型：Phone，从5.0.2(14)版本开始，新增支持Tablet、PC/2in1设备，从5.1.0(18)版本开始新增支持TV设备。
* 可通过以下方式查询相关扩展特性是否支持：

  对于OpenGL ES，使用[HMS\_XEG\_GetString](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_getstring)扩展特性查询接口进行查询，如查询结果包含[XEG\_ADAPTIVE\_VRS\_EXTENSION\_NAME](../harmonyos-references/xengine-kit-xengine.md#xeg_adaptive_vrs_extension_name)，则表示支持该特性，若查询结果未包含，则表示不支持该特性。

## 接口说明

以下接口为自适应VRS设置接口，如需使用更丰富的设置和查询接口，具体API说明详见[接口文档](../harmonyos-references/xengine-kit-xengine.md)。

| 接口名 | 描述 |
| --- | --- |
| const GLubyte \* HMS\_XEG\_GetString (GLenum name) | XEngine OpenGL ES扩展特性查询接口。 |
| GL\_APICALL void GL\_APIENTRY HMS\_XEG\_AdaptiveVRSParameter (GLenum pname, GLvoid \* param) | 设置自适应VRS的参数。 |
| GL\_APICALL void GL\_APIENTRY HMS\_XEG\_DispatchAdaptiveVRS (GLfloat \* reprojectionMatrix, GLuint inputColorImage, GLuint inputDepthImage, GLuint shadingRateImage) | 计算着色率图像。 |
| GL\_APICALL void GL\_APIENTRY HMS\_XEG\_ApplyAdaptiveVRS (GLuint shadingRateImage) | 将着色率图像应用到渲染目标中。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_EnumerateDeviceExtensionProperties (VkPhysicalDevice physicalDevice, uint32\_t \* pPropertyCount, XEG\_ExtensionProperties \* pProperties) | XEngine Vulkan扩展特性查询接口。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CreateAdaptiveVRS (VkDevice device, XEG\_AdaptiveVRSCreateInfo \* pXegAdaptiveVRSCreateInfo, XEG\_AdaptiveVRS \* pXegAdaptiveVRS) | 创建XEG\_AdaptiveVRS对象。 |
| VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_CmdDispatchAdaptiveVRS (VkCommandBuffer commandBuffer, XEG\_AdaptiveVRS xegAdaptiveVRS, XEG\_AdaptiveVRSDescription \* pXegAdaptiveVRSDescription) | 执行计算自适应可变着色率命令。 |
| VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_DestroyAdaptiveVRS (XEG\_AdaptiveVRS xegAdaptiveVRS) | 销毁XEG\_AdaptiveVRS对象。 |

## 业务流程

* 下面是基于GLES图形API平台集成自适应VRS的主要业务流程

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/jTYmabT3SxyWjPD_NEc94A/zh-cn_image_0000002589245043.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053642Z&HW-CC-Expire=86400&HW-CC-Sign=5008807E394835C3C3CEBAB7E9454460C4E08F5C8A88925D652107E2DDD9A7CC)

1. 用户在进入游戏初始化场景时调用HMS\_XEG\_GetString接口查询XEngine支持的特性，当查询接口返回支持的特性列表中包含自适应VRS时代表可以使用此特性。
2. 此时调用HMS\_XEG\_AdaptiveVRSParameter接口配置超分参数。
3. 当游戏运行时，游戏渲染当前帧纹理。
4. 在使用自适应VRS特性的阶段前，调用HMS\_XEG\_DispatchAdaptiveVRS接口计算着色率图。
5. 调用HMS\_XEG\_ApplyAdaptiveVRS将着色率图像应用到渲染目标中。
6. 游戏渲染剩下的纹理，如UI等。
7. 当前帧已全部渲染完成，进行送显。
8. 当游戏退出时，超分资源会自行释放。

* 下面是基于Vulkan图形API平台集成自适应VRS的主要业务流程

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/TC0mCJudTQabzRP5HqxKWw/zh-cn_image_0000002558765238.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053642Z&HW-CC-Expire=86400&HW-CC-Sign=E83BF3455794F815A9FBBE0BC3202FF06B6D7F5D577BDAFF1A8B23B57AD63FE8)

1. 用户在进入游戏初始化场景时调用HMS\_XEG\_EnumerateDeviceExtensionProperties接口查询XEngine支持的特性，当查询接口返回支持的特性列表中包含自适应VRS时代表可以使用此特性。
2. 此时调用HMS\_XEG\_CreateAdaptiveVRS接口创建自适应VRS实例。
3. 使用自适应VRS特性时，需要创建能够支持VRS的vulkan资源。
4. 当游戏运行时，游戏渲染当前帧纹理。
5. 调用HMS\_XEG\_CmdDispatchAdaptiveVRS计算着色率图。
6. 将着色率图像应用到渲染目标中。
7. 渲染剩下的游戏纹理，如UI等。
8. 当前帧已全部渲染完成，进行送显。
9. 当游戏退出时，调用HMS\_XEG\_DestroyAdaptiveVRS接口销毁自适应VRS实例。

## 开发步骤

本章以OpenGL ES和Vulkan图像API集成为例，说明XEngine集成操作过程。

### 配置项目

编译HAP时，Native层so编译需要依赖NDK中的libxengine.so。

* 头文件引用

  按需引用XEngine的头文件，如使用OpenGL ES自适应VRS功能。

  ```
  1. #include <cstring>
  2. #include <cstdlib>
  3. #include <xengine/xeg_gles_extension.h>
  4. #include <xengine/xeg_gles_adaptive_vrs.h>
  ```

  按需引用XEngine的头文件，如使用Vulkan自适应VRS功能。

  ```
  1. #include <string>
  2. #include <vector>
  3. #include <algorithm>
  4. #include <xengine/xeg_vulkan_extension.h>
  5. #include <xengine/xeg_vulkan_adaptive_vrs.h>
  ```
* 编写CMakeLists.txt

  按需引用XEngine的CMakeLists，如使用OpenGL ES自适应VRS功能，CMakeLists.txt部分示例代码如下，完整示例代码请参见[Demo（GPU加速引擎-GLES）](https://gitcode.com/harmonyos_samples/xengine-samplecode-gles-demo-cpp)。

  ```
  1. find_library(
  2. # 设置路径变量的名称。
  3. xengine-lib
  4. # 指定希望CMake定位的NDK库的名称。
  5. xengine
  6. )
  7. find_library(
  8. # 设置路径变量的名称。
  9. EGL-lib
  10. # 指定希望CMake定位的NDK库的名称。
  11. EGL
  12. )
  13. find_library(
  14. # 设置路径变量的名称。
  15. GLES-lib
  16. # 指定希望CMake定位的NDK库的名称。
  17. GLESv3
  18. )

  20. target_link_libraries(nativerender PUBLIC
  21. ${EGL-lib} ${GLES-lib} ${xengine-lib})
  ```

  按需引用XEngine的CMakeLists，如使用Vulkan自适应VRS功能，CMakeLists.txt部分示例代码如下，完整示例代码请参见[Demo（GPU加速引擎-Vulkan）](https://gitcode.com/harmonyos_samples/xengine-samplecode-vulkan-demo-cpp)。

  ```
  1. find_library(
  2. # 设置路径变量的名称。
  3. xengine-lib
  4. # 指定希望CMake定位的NDK库的名称。
  5. xengine
  6. )
  7. find_library(
  8. # 设置路径变量的名称。
  9. Vulkan-lib
  10. # 指定希望CMake定位的NDK库的名称。
  11. vulkan
  12. )

  14. target_link_libraries(nativerender PUBLIC
  15. ${Vulkan-lib} ${xengine-lib})
  ```

### 集成自适应VRS功能（OpenGL ES）

自适应VRS功能OpenGL ES版本的着色率纹理创建和绑定由特性提供的接口实现。

在调用XEngine Kit能力前，需要先通过[Syscap](../harmonyos-references/syscap.md#判断-api-是否可以使用)查询您的目标设备是否支持SystemCapability.Graphic.XEngine系统能力。

1. 调用[HMS\_XEG\_GetString](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_getstring)接口，获取XEngine支持的扩展信息，只有在支持[XEG\_ADAPTIVE\_VRS\_EXTENSION\_NAME](../harmonyos-references/xengine-kit-xengine.md#xeg_adaptive_vrs_extension_name)扩展时才可以使用自适应VRS的相关接口。

   ```
   1. // 查询XEngine支持的GLES扩展信息
   2. const char* extensions = (const char*)HMS_XEG_GetString(XEG_EXTENSIONS);
   3. // 查询是否支持自适应VRS
   4. if (!strstr(extensions, XEG_ADAPTIVE_VRS_EXTENSION_NAME)) {
   5. exit(1); // return error
   6. }
   ```
2. 调用[HMS\_XEG\_AdaptiveVRSParameter](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter)接口，对自适应VRS的参数赋值。

   ```
   1. // renderWidth与renderHeight分别为用户自定义的渲染宽度与渲染高度，此处以800*600分辨率为例
   2. uint32_t renderWidth = 800;
   3. uint32_t renderHeight = 600;
   4. // inputSize为上一帧渲染管线最终渲染的图像尺寸，用户可自定义
   5. GLsizei inputSize[2] = {static_cast<GLsizei>(renderWidth), static_cast<GLsizei>(renderHeight)};
   6. HMS_XEG_AdaptiveVRSParameter(XEG_ADAPTIVE_VRS_INPUT_SIZE, inputSize);
   7. // inputRegion为上一帧渲染管线最终渲染的图像区域，用户可自定义
   8. GLuint inputRegion[4] = {0, 0, renderWidth, renderHeight};
   9. HMS_XEG_AdaptiveVRSParameter(XEG_ADAPTIVE_VRS_INPUT_REGION, inputRegion);
   10. // texelSizes为渲染的分片大小，用户可自定义，当前支持[8, 8]和[16, 16]两种规格
   11. GLsizei texelSizes[2] = {8, 8};
   12. HMS_XEG_AdaptiveVRSParameter(XEG_ADAPTIVE_VRS_TEXEL_SIZE, texelSizes);
   13. // sensitivity为控制生成着色率图像的阈值，用户可自定义，建议取值范围为[0, 1]
   14. GLfloat sensitivity = 0.15;
   15. HMS_XEG_AdaptiveVRSParameter(XEG_ADAPTIVE_VRS_ERROR_SENSITIVITY, &sensitivity);
   16. // flip为判断是否执行图像上下翻转，为true表示不进行图像上下翻转，false则表示进行图像上下翻转，此处以false为例
   17. GLboolean flip = false;
   18. HMS_XEG_AdaptiveVRSParameter(XEG_ADAPTIVE_VRS_FLIP, &flip);
   ```
3. 调用[HMS\_XEG\_DispatchAdaptiveVRS](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_dispatchadaptivevrs)接口计算着色率图像。

   ```
   1. // inputColorImage为用户自定义上一帧渲染管线最终渲染结果颜色附件纹理
   2. GLuint inputColorImage;
   3. // inputDepthImage为用户自定义当前帧渲染管线最终渲染结果深度附件纹理
   4. GLuint inputDepthImage;
   5. // outputShadingRateImage为用户可自定义生成着色率图像信息的纹理
   6. GLuint outputShadingRateImage;
   7. // reprojectionMatrix为用户根据投影矩阵和观察矩阵计算得来的重投影矩阵
   8. float *reprojectionMatrix = nullptr;
   9. HMS_XEG_DispatchAdaptiveVRS(reprojectionMatrix, inputColorImage, inputDepthImage, outputShadingRateImage);
   ```
4. 调用[HMS\_XEG\_ApplyAdaptiveVRS](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_applyadaptivevrs)接口，将着色率图像应用到渲染目标中。

   ```
   1. HMS_XEG_ApplyAdaptiveVRS(outputShadingRateImage);
   ```

### 集成自适应VRS功能（Vulkan）

在调用XEngine Kit能力前，需要先通过[Syscap](../harmonyos-references/syscap.md#判断-api-是否可以使用)查询您的目标设备是否支持SystemCapability.Graphic.XEngine系统能力。

1. 调用[HMS\_XEG\_EnumerateDeviceExtensionProperties](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口，获取XEngine支持的扩展信息，只有在支持[XEG\_ADAPTIVE\_VRS\_EXTENSION\_NAME](../harmonyos-references/xengine-kit-xengine.md#xeg_adaptive_vrs_extension_name)扩展时才可以使用自适应VRS的相关接口。

   ```
   1. // physicalDevice为Vulkan物理设备，用户需进行初始化
   2. VkPhysicalDevice physicalDevice;
   3. // 查询XEngine支持的Vulkan扩展列表
   4. std::vector<std::string> supportedExtensions;
   5. uint32_t pPropertyCount;
   6. HMS_XEG_EnumerateDeviceExtensionProperties(physicalDevice, &pPropertyCount, nullptr);
   7. if (pPropertyCount > 0) {
   8. std::vector<XEG_ExtensionProperties> pProperties(pPropertyCount);
   9. if (HMS_XEG_EnumerateDeviceExtensionProperties(physicalDevice, &pPropertyCount, &pProperties.front()) == VK_SUCCESS) {
   10. for (auto ext : pProperties) {
   11. supportedExtensions.push_back(ext.extensionName);
   12. }
   13. }
   14. }
   15. // 查询是否支持自适应VRS
   16. if (std::find(supportedExtensions.begin(), supportedExtensions.end(), XEG_ADAPTIVE_VRS_EXTENSION_NAME) == supportedExtensions.end()) {
   17. exit(1); // return error
   18. }
   ```
2. 声明实例句柄。

   ```
   1. XEG_AdaptiveVRS xeg_adaptiveVRS;
   ```
3. 调用[HMS\_XEG\_CreateAdaptiveVRS](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_createadaptivevrs)接口，定义并创建实例。

   ```
   1. // m_renderWidth与m_renderHeight分别为纹理采样宽高
   2. int m_renderWidth;
   3. int m_renderHeight;
   4. // VRS_TILE_SIZE为自适应VRS的渲染的分片大小
   5. int VRS_TILE_SIZE;
   6. // Vulkan逻辑设备，用户需进行初始化
   7. VkDevice device;
   8. // XEG_AdaptiveVRSCreateInfo为自适应VRS实例句柄对象的参数信息
   9. XEG_AdaptiveVRSCreateInfo xeg_createInfo;
   10. // XEG_AdaptiveVRSDescription为下发绘制着色率纹理命令所需参数信息
   11. XEG_AdaptiveVRSDescription xeg_description;
   12. // VkExtent2D inputSize为上一帧渲染管线最终渲染的图像尺寸，用户可自定义
   13. VkExtent2D inputSize;
   14. inputSize.width = m_renderWidth;
   15. inputSize.height = m_renderHeight;
   16. // VkRect2D为Vulkan指定的二维区域结构
   17. // inputRegion为自适应VRS输入纹理区域，用户可自定义
   18. VkRect2D inputRegion {};
   19. // inputRegion.extent.width与inputRegion.extent.height分别为纹理采样宽高
   20. inputRegion.extent.width = m_renderWidth;
   21. inputRegion.extent.height = m_renderHeight;
   22. // inputRegion.offset.x和inputRegion.offset.y为原点偏移量
   23. inputRegion.offset.x = 0;
   24. inputRegion.offset.y = 0;
   25. // xeg_createInfo.inputSize为上一帧渲染管线最终渲染的图像尺寸
   26. xeg_createInfo.inputSize = inputSize;
   27. // xeg_createInfo.inputRegion为上一帧渲染管线最终渲染的图像区域
   28. xeg_createInfo.inputRegion = inputRegion;
   29. // xeg_createInfo.adaptiveTileSize为自适应VRS的渲染的分片大小
   30. xeg_createInfo.adaptiveTileSize = VRS_TILE_SIZE;
   31. // xeg_createInfo.errorSensitivity为控制最终生成着色率纹理结果的阈值，此处以阈值为0.5为例
   32. xeg_createInfo.errorSensitivity = 0.5;
   33. // xeg_createInfo.flip为判断是否执行图像上下翻转，为true表示进行图像上下翻转，false则表示不进行图像上下翻转，此处以false为例
   34. xeg_createInfo.flip = false;
   35. HMS_XEG_CreateAdaptiveVRS(device, &xeg_createInfo, &xeg_adaptiveVRS);
   ```
4. 调用[HMS\_XEG\_CmdDispatchAdaptiveVRS](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_cmddispatchadaptivevrs)接口，下发自适应VRS命令，生成perImage着色率纹理。

   ```
   1. // inputColorImageView为用户自定义的上一帧渲染管线最终渲染结果颜色附件纹理
   2. VkImageView inputColorImageView = VK_NULL_HANDLE;
   3. // inputDepthImageView为用户自定义的当前帧渲染管线最终渲染结果深度附件纹理
   4. VkImageView inputDepthImageView = VK_NULL_HANDLE;
   5. // outputShadingRateImage为用户自定义的生成着色率图信息的纹理
   6. VkImageView outputShadingRateImage = VK_NULL_HANDLE;
   7. // cmdBuff为命令缓冲区，用户需进行初始化
   8. VkCommandBuffer commandBuffer = VK_NULL_HANDLE ;
   9. xeg_description.inputColorImage = inputColorImageView;
   10. xeg_description.inputDepthImage = inputDepthImageView;
   11. xeg_description.outputShadingRateImage = outputShadingRateImage;
   12. // xeg_description.reprojectionMatrix为使用投影矩阵和观察矩阵计算而来的重投影矩阵
   13. xeg_description.reprojectionMatrix = nullptr;
   14. HMS_XEG_CmdDispatchAdaptiveVRS(commandBuffer, xeg_adaptiveVRS, &xeg_description);
   ```
5. 调用[HMS\_XEG\_DestroyAdaptiveVRS](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_destroyadaptivevrs)接口，卸载VRS实例，清理VRS相关资源。

   ```
   1. HMS_XEG_DestroyAdaptiveVRS(xeg_adaptiveVRS);
   ```
