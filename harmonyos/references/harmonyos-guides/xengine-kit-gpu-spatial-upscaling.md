---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xengine-kit-gpu-spatial-upscaling
title: 空域GPU超分
breadcrumb: 指南 > 图形 > XEngine Kit（GPU加速引擎服务） > 空域GPU超分
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:42+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:7741efb7ba4aced1300a83996af8a1873fa0884813bebe993c56ddd37f700791
---

XEngine Kit提供空域GPU超分能力，其基于单帧输入图像，使用空间邻域信息实现超采样，开销较小同时收益可观，建议使用超分倍率为[1.2, 1.5]。

## 约束与限制

* 支持的设备类型：Phone，从5.0.2(14)版本开始，新增支持Tablet、PC/2in1设备，从5.1.0(18)版本开始新增支持TV设备。
* 可通过以下方式查询相关扩展特性是否支持：

  + 对于OpenGL ES，使用[HMS\_XEG\_GetString](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_getstring)扩展特性查询接口进行查询。
  + 对于Vulkan，使用[HMS\_XEG\_EnumerateDeviceExtensionProperties](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)扩展特性查询接口进行查询。

  如查询结果包含[XEG\_SPATIAL\_UPSCALE\_EXTENSION\_NAME](../harmonyos-references/xengine-kit-xengine.md#xeg_spatial_upscale_extension_name)，则表示支持该特性，若查询结果未包含，则表示不支持该特性。

## 接口说明

以下接口为OpenGL ES和Vulkan空域GPU超分设置接口，如需使用更丰富的设置和查询接口，具体API说明详见[接口文档](../harmonyos-references/xengine-kit-xengine.md)。

| 接口名 | 描述 |
| --- | --- |
| const GLubyte \* HMS\_XEG\_GetString (GLenum name) | XEngine OpenGL ES扩展特性查询接口。 |
| GL\_APICALL void GL\_APIENTRY HMS\_XEG\_SpatialUpscaleParameter (GLenum pname, GLvoid \*param) | 设置空域GPU超分输入参数。 |
| GL\_APICALL void GL\_APIENTRY HMS\_XEG\_RenderSpatialUpscale (GLuint inputTexture) | 执行空域GPU超分渲染命令。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_EnumerateDeviceExtensionProperties (VkPhysicalDevice physicalDevice, uint32\_t \*pPropertyCount, XEG\_ExtensionProperties \*pProperties) | XEngine Vulkan扩展特性查询接口。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CreateSpatialUpscale (VkDevice device, const XEG\_SpatialUpscaleCreateInfo \*pXegSpatialUpscaleCreateInfo, XEG\_SpatialUpscale \*pXegSpatialUpscale) | 创建XEG\_SpatialUpscale对象。 |
| VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_CmdRenderSpatialUpscale (VkCommandBuffer commandBuffer, XEG\_SpatialUpscale xegSpatialUpscale, XEG\_SpatialUpscaleDescription \*pXegSpatialUpscaleDescription) | 执行空域GPU超分渲染命令。 |
| VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_DestroySpatialUpscale (XEG\_SpatialUpscale xegSpatialUpscale) | 销毁XEG\_SpatialUpscale对象。 |

## 业务流程

* 下面是基于GLES图形API平台集成空域GPU超分的主要业务流程

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/Dy8YteK7Txa4mYwKHnLhSA/zh-cn_image_0000002589325105.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053641Z&HW-CC-Expire=86400&HW-CC-Sign=1A3F7977BD330E8B6B22DFAC5B12CF26F5D74D2F2546C00B88D51AF2019FA748)

1. 用户在进入游戏初始化场景时调用HMS\_XEG\_GetString接口查询XEngine支持的特性，当查询接口返回支持的特性列表中包含空域GPU超分时代表可以使用此特性。
2. 调用HMS\_XEG\_SpatialUpscaleParameter接口配置超分参数。
3. 当游戏运行时，游戏渲染待超分的当前帧纹理。
4. 当待超分纹理渲染完成时，调用HMS\_XEG\_RenderSpatialUpscale接口对待超分的纹理超分。
5. 当超分渲染完成时，游戏渲染剩下的纹理，如UI等。
6. 当前帧已全部渲染完成，进行送显。
7. 当游戏退出时，超分资源会自行释放。

* 下面是基于Vulkan图形API平台集成空域GPU超分的主要业务流程

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/PTMIzRMYSraJSDZDw_WeWA/zh-cn_image_0000002589245041.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053641Z&HW-CC-Expire=86400&HW-CC-Sign=6B99F6B2E5696B4AE6275A92C5CC52E3DF3D8EDE4073BCF95DD77C80DBBD2F1E)

1. 用户在进入游戏初始化场景时调用HMS\_XEG\_EnumerateDeviceExtensionProperties接口查询XEngine支持的特性，当查询接口返回支持的特性列表中包含空域GPU超分时代表可以使用此特性。
2. 此时调用HMS\_XEG\_CreateSpatialUpscale接口创建超分实例。
3. 当游戏运行时，游戏渲染待超分的当前帧纹理。
4. 当待超分纹理渲染完成时，调用HMS\_XEG\_CmdRenderSpatialUpscale接口对待超分的纹理超分。
5. 当超分渲染完成时，游戏渲染剩下的纹理，如UI等。
6. 当前帧已全部渲染完成，进行送显。
7. 当游戏退出时，调用HMS\_XEG\_DestroySpatialUpscale接口销毁超分实例。

## 开发步骤

本章以OpenGL ES和Vulkan图像API集成为例，说明XEngine集成操作过程。

### 配置项目

编译HAP时，Native层so编译需要依赖NDK中的libxengine.so。

* 头文件引用

  按需引用XEngine的头文件，如使用OpenGL ES空域GPU超分。

  ```
  1. #include <cstring>
  2. #include <cstdlib>
  3. #include <xengine/xeg_gles_extension.h>
  4. #include <xengine/xeg_gles_spatial_upscale.h>
  ```

  按需引用XEngine的头文件，如使用Vulkan空域GPU超分。

  ```
  1. #include <string>
  2. #include <vector>
  3. #include <algorithm>
  4. #include <xengine/xeg_vulkan_extension.h>
  5. #include <xengine/xeg_vulkan_spatial_upscale.h>
  ```
* 编写CMakeLists.txt

  按需引用XEngine的CMakeLists，如使用OpenGL ES空域GPU超分功能，CMakeLists.txt部分示例代码如下，完整示例代码请参见[Demo（GPU加速引擎-GLES）](https://gitcode.com/harmonyos_samples/xengine-samplecode-gles-demo-cpp)。

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

  按需引用XEngine的CMakeLists，如使用Vulkan空域GPU超分功能，CMakeLists.txt部分示例代码如下，完整示例代码请参见[Demo（GPU加速引擎-Vulkan）](https://gitcode.com/harmonyos_samples/xengine-samplecode-vulkan-demo-cpp)。

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

### 集成XEngine空域GPU超分（OpenGL ES）

使用EGL和OpenGL ES图形API搭建图像渲染管线并集成空域GPU超分在Native层实现，渲染结果通过[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件显示到屏幕。

本节阐述OpenGL ES图形API的空域GPU超分的使用，详细代码请参见[Demo（GPU加速引擎-GLES）](https://gitcode.com/harmonyos_samples/xengine-samplecode-gles-demo-cpp)。

在调用XEngine Kit能力前，需要先通过[Syscap](../harmonyos-references/syscap.md#判断-api-是否可以使用)查询您的目标设备是否支持SystemCapability.Graphic.XEngine系统能力。

1. 调用[HMS\_XEG\_GetString](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_getstring)接口，获取XEngine支持的扩展信息，只有在支持XEG\_SPATIAL\_UPSCALE\_EXTENSION\_NAME扩展时才可以使用空域GPU超分的相关接口。

   ```
   1. // 查询XEngine支持的GLES扩展信息
   2. const char* extensions = (const char*)HMS_XEG_GetString(XEG_EXTENSIONS);
   3. // 检查是否支持空域GPU超分
   4. if (!strstr(extensions, XEG_SPATIAL_UPSCALE_EXTENSION_NAME)) {
   5. exit(1); // return error
   6. }
   ```
2. 调用[HMS\_XEG\_SpatialUpscaleParameter](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_spatialupscaleparameter)接口，对空域GPU超分的参数赋值。

   ```
   1. // m_sharpness为用户自定义超分锐化参数，此处以参数为0.3f为例
   2. float m_sharpness = 0.3f;
   3. // m_renderWidth与m_renderHeight分别为用户自定义的渲染宽度与渲染高度，此处以800*600分辨率为例
   4. uint32_t m_renderWidth = 800;
   5. uint32_t m_renderHeight = 600;
   6. HMS_XEG_SpatialUpscaleParameter(XEG_SPATIAL_UPSCALE_SHARPNESS, &m_sharpness);
   7. // upscaleScissor为超分输入图像的采样区域
   8. int upscaleScissor[4] = {0, 0, static_cast<int>(m_renderWidth), static_cast<int>(m_renderHeight)};
   9. HMS_XEG_SpatialUpscaleParameter(XEG_SPATIAL_UPSCALE_SCISSOR, upscaleScissor);
   ```
3. 调用[HMS\_XEG\_RenderSpatialUpscale](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_renderspatialupscale)接口进行超分。

   ```
   1. // upscaleFBO为用户自定义创建的framebuffer
   2. unsigned int upscaleFBO;
   3. glBindFramebuffer(GL_FRAMEBUFFER, upscaleFBO);
   4. // m_upscaleWidth和m_upscaleHeight分别为用户自定义超分宽度和超分高度，此处以超分至1200*900分辨率为例
   5. uint32_t m_upscaleWidth = 1200;
   6. uint32_t m_upscaleHeight = 900;
   7. glViewport(0, 0, m_upscaleWidth, m_upscaleHeight);
   8. glScissor(0, 0, m_upscaleWidth, m_upscaleHeight);
   9. // upscaleColorBuffer为纹理附件，用户可自定义
   10. unsigned int upscaleColorBuffer;
   11. HMS_XEG_RenderSpatialUpscale(upscaleColorBuffer);
   ```

   upscaleFBO是已创建完成的framebuffer，并绑定纹理，超分接口调用后绘制到纹理上。

### 集成XEngine空域GPU超分（Vulkan）

使用Vulkan图形API搭建图像渲染管线并集成空域GPU超分在Native层实现，渲染结果通过[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件显示到屏幕。

本节阐述Vulkan图形API的空域GPU超分使用，详细代码请参见[Demo（GPU加速引擎-Vulkan）](https://gitcode.com/harmonyos_samples/xengine-samplecode-vulkan-demo-cpp)。

在调用XEngine Kit能力前，需要先通过[Syscap](../harmonyos-references/syscap.md#判断-api-是否可以使用)查询您的目标设备是否支持SystemCapability.Graphic.XEngine系统能力。

1. 调用[HMS\_XEG\_EnumerateDeviceExtensionProperties](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口，获取XEngine支持的扩展信息，只有在支持XEG\_SPATIAL\_UPSCALE\_EXTENSION\_NAME扩展时才可以使用空域GPU超分的相关接口。

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
   15. // 查询是否支持空域GPU超分
   16. if (std::find(supportedExtensions.begin(), supportedExtensions.end(), XEG_SPATIAL_UPSCALE_EXTENSION_NAME) == supportedExtensions.end()) {
   17. exit(1); // return error
   18. }
   ```
2. 声明实例句柄。

   ```
   1. XEG_SpatialUpscale xegSpatialUpscale;
   ```
3. 调用[HMS\_XEG\_CreateSpatialUpscale](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_createspatialupscale)接口，创建超分实例。

   ```
   1. // 渲染宽高和超分后宽高均为用户自定义参数，此处以将800*600分辨率超分至1200*900分辨率为例
   2. uint32_t m_renderWidth = 800;
   3. uint32_t m_renderHeight = 600;
   4. uint32_t m_upscaleWidth = 1200;
   5. uint32_t m_upscaleHeight = 900;
   6. // Vulkan逻辑设备，用户需进行初始化
   7. VkDevice device;
   8. // VkRect2D为Vulkan指定的二维区域结构
   9. // srcRect2D为超分输入纹理区域，用户可自定义
   10. VkRect2D srcRect2D;
   11. // srcRect2D.offset.x和srcRect2D.offset.y为原点偏移量
   12. srcRect2D.offset.x = 0;
   13. srcRect2D.offset.y = 0;
   14. // srcRect2D.extent.width与srcRect2D.extent.height为输入纹理宽高
   15. srcRect2D.extent.width = m_renderWidth;
   16. srcRect2D.extent.height = m_renderHeight;
   17. // dstRect2D为超分输出纹理区域，用户可自定义
   18. VkRect2D dstRect2D;
   19. // dstRect2D.offset.x和dstRect2D.offset.y为原点偏移量
   20. dstRect2D.offset.x = 0;
   21. dstRect2D.offset.y = 0;
   22. // dstRect2D.extent.width与dstRect2D.extent.height为超分纹理宽高
   23. dstRect2D.extent.width = m_upscaleWidth;
   24. dstRect2D.extent.height = m_upscaleHeight;
   25. XEG_SpatialUpscaleCreateInfo createInfo;
   26. createInfo.format = VK_FORMAT_R8G8B8A8_UNORM;
   27. // sharpness为用户自定义超分锐化参数，此处以参数为0.3f为例
   28. createInfo.sharpness = 0.3f;
   29. createInfo.outputSize = dstRect2D.extent;
   30. createInfo.inputRegion = srcRect2D;
   31. createInfo.outputRegion = dstRect2D;
   32. createInfo.inputSize = srcRect2D.extent;
   33. HMS_XEG_CreateSpatialUpscale(device, &createInfo, &xegSpatialUpscale);
   ```
4. 调用[HMS\_XEG\_CmdRenderSpatialUpscale](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_cmdrenderspatialupscale)接口下发超分，每帧都需要调用。

   ```
   1. // inputImageView为用户创建的超分输入图像的VkImageView
   2. VkImageView inputImageView = VK_NULL_HANDLE;
   3. // outputImageView为用户创建的超分输出图像的VkImageView
   4. VkImageView outputImageView = VK_NULL_HANDLE;
   5. // cmdBuff为命令缓冲区，用户需进行初始化
   6. VkCommandBuffer cmdBuff = VK_NULL_HANDLE ;
   7. XEG_SpatialUpscaleDescription xegDescription;
   8. xegDescription.inputImage = inputImageView;
   9. xegDescription.outputImage = outputImageView;
   10. HMS_XEG_CmdRenderSpatialUpscale(cmdBuff, xegSpatialUpscale, &xegDescription);
   ```
5. 调用[HMS\_XEG\_DestroySpatialUpscale](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_destroyspatialupscale)接口销毁实例。

   ```
   1. HMS_XEG_DestroySpatialUpscale(xegSpatialUpscale);
   ```
