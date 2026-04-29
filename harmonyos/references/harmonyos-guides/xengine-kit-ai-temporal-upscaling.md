---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xengine-kit-ai-temporal-upscaling
title: 时域AI超分
breadcrumb: 指南 > 图形 > XEngine Kit（GPU加速引擎服务） > 时域AI超分
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:43+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:9215dc4165b5b7bda34774d96f0f1c64e030b76feabe60d7ad03ba0741b104e2
---

从6.0.0(20) 版本开始，新增支持OpenGL ES协议。

XEngine Kit提供时域AI超分能力，利用相机的抖动获取不同位置的采样信息，融合时域实现超采样率和超分辨率功能，并利用神经网络达到抗锯齿效果，建议超分倍率为[1.25, 2.0]。

## 业务流程

* 下面是基于GLES图形API平台集成时域AI超分的主要业务流程

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/fXOExD8gRZaJqT2kpNzDSQ/zh-cn_image_0000002558765236.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053642Z&HW-CC-Expire=86400&HW-CC-Sign=B882EE0F70680600C53A6CCF182A5373A33802CA952707444F31A39AE626EA08)

1. 用户在进入游戏初始化场景时调用HMS\_XEG\_GetString接口查询XEngine支持的特性，当查询接口返回支持的特性列表中包含时域AI超分时代表可以使用此特性。
2. 此时调用HMS\_XEG\_TemporalUpscaleParameter接口配置超分参数。
3. 当游戏运行时，游戏渲染待超分的当前帧纹理。
4. 当待超分纹理渲染完成时，即已经做完了带jitter的主pass渲染，准备好了depth，motion vector，color等输入纹理，此时调用HMS\_XEG\_RenderTemporalUpscale接口对待超分的纹理超分。
5. 当超分渲染完成时，游戏渲染剩下的纹理，如UI等。
6. 当前帧已全部渲染完成，进行送显。
7. 当游戏退出时，超分资源会自行释放。

* 下面是基于Vulkan图形API平台集成时域AI超分的主要业务流程

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/YFKtL9syQQKlS5FxzTKtRQ/zh-cn_image_0000002558605580.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053642Z&HW-CC-Expire=86400&HW-CC-Sign=D39634DFE133D8DE514E23409A10BC8D8AFE3D513477160D4B89E6FA669C8EC7)

1. 用户在进入游戏初始化场景时调用HMS\_XEG\_EnumerateDeviceExtensionProperties接口查询XEngine支持的特性，当查询接口返回支持的特性列表中包含时域AI超分时代表可以使用此特性。
2. 此时调用HMS\_XEG\_CreateTemporalUpscale接口创建超分实例。
3. 当游戏运行时，游戏渲染待超分的当前帧纹理。
4. 当待超分纹理渲染完成时，即已经做完了带jitter的主pass渲染，准备好了depth，motion vector，color等输入纹理，此时调用HMS\_XEG\_CmdRenderTemporalUpscale接口对待超分的纹理超分。
5. 当超分渲染完成时，游戏渲染剩下的纹理，如UI等。
6. 当前帧已全部渲染完成，进行送显。
7. 当游戏退出时，调用HMS\_XEG\_DestroyTemporalUpscale接口销毁超分实例。

## 约束与限制

* 支持的设备类型：Phone，从5.1.0(18)版本开始新增支持Tablet、PC/2in1、TV设备。
* 可通过以下方式查询相关扩展特性是否支持：

  + 对于OpenGL ES，使用[HMS\_XEG\_GetString](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_getstring)扩展特性查询接口进行查询。
  + 对于Vulkan，使用[HMS\_XEG\_EnumerateDeviceExtensionProperties](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)扩展特性查询接口进行查询。

  如查询结果包含[XEG\_TEMPORAL\_UPSCALE\_EXTENSION\_NAME](../harmonyos-references/xengine-kit-xengine.md#xeg_temporal_upscale_extension_name)，则表示支持该特性，若查询结果未包含，则表示不支持该特性。

## 接口说明

以下接口为OpenGL ES和Vulkan时域AI超分设置接口，如需使用更丰富的设置和查询接口，具体API说明详见[接口文档](../harmonyos-references/xengine-kit-xengine.md)。

| 接口名 | 描述 |
| --- | --- |
| const GLubyte \* HMS\_XEG\_GetString (GLenum name) | XEngine OpenGL ES扩展特性查询接口。 |
| GL\_APICALL void GL\_APIENTRY HMS\_XEG\_TemporalUpscaleParameter(GLenum pname, const GLvoid \*param) | 设置时域AI超分输入参数。 |
| GL\_APICALL void GL\_APIENTRY HMS\_XEG\_RenderTemporalUpscale(  GLuint inputTexture,  GLuint depthTexture,  GLuint motionVectorTexture,  GLuint dynamicMaskTexture,  GLfloat jitterX,  GLfloat jitterY  ) | 执行时域AI超分渲染命令。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_EnumerateDeviceExtensionProperties (VkPhysicalDevice physicalDevice, uint32\_t \* pPropertyCount, XEG\_ExtensionProperties \* pProperties) | XEngine Vulkan扩展特性查询接口。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CreateTemporalUpscale (VkDevice device, XEG\_TemporalUpscaleCreateInfo \* pTemporalUpscaleInfo, XEG\_TemporalUpscale \* pTemporalUpscale) | 创建XEG\_TemporalUpscale对象。 |
| VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_CmdRenderTemporalUpscale (VkCommandBuffer commandBuffer, XEG\_TemporalUpscale temporalUpscale, XEG\_TemporalUpscaleDescription \* pDescription) | 执行时域AI超分渲染命令。 |
| VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_DestroyTemporalUpscale (XEG\_TemporalUpscale temporalUpscale) | 销毁XEG\_TemporalUpscale对象。 |

## 开发步骤

本章以OpenGL ES和Vulkan图像API集成为例，说明XEngine集成操作过程。

### 配置项目

编译HAP时，Native层so编译需要依赖NDK中的libxengine.so。

* 头文件引用

  按需引用XEngine的头文件，如使用OpenGL ES时域AI超分。

  ```
  1. #include <cstring>
  2. #include <cstdlib>
  3. #include <xengine/xeg_gles_extension.h>
  4. #include <xengine/xeg_gles_temporal_upscale.h>
  ```

  按需引用XEngine的头文件，如使用Vulkan时域AI超分。

  ```
  1. #include <algorithm>
  2. #include <string>
  3. #include <vector>
  4. #include "xengine/xeg_vulkan_temporal_upscale.h"
  5. #include "xengine/xeg_vulkan_extension.h"
  ```
* 编写CMakeLists.txt

  按需引用XEngine的CMakeLists，如使用OpenGL ES时域AI超分功能，CMakeLists.txt部分示例代码如下。

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

  按需引用XEngine的CMakeLists，如使用Vulkan时域AI超分功能，CMakeLists.txt部分示例代码如下，完整示例代码请参见[Demo（GPU加速引擎-Vulkan）](https://gitcode.com/harmonyos_samples/xengine-samplecode-vulkan-temporal-upscale-demo-cpp)。

  ```
  1. find_library(
  2. # 设置路径变量的名称。
  3. hilog-lib
  4. # 指定希望CMake定位的NDK库的名称。
  5. hilog_ndk.z
  6. )
  7. find_library(
  8. # 设置路径变量的名称。
  9. libace-lib
  10. # 指定希望CMake定位的NDK库的名称。
  11. ace_ndk.z
  12. )
  13. find_library(
  14. # 设置路径变量的名称。
  15. libnapi-lib
  16. # 指定希望CMake定位的NDK库的名称。
  17. ace_napi.z
  18. )
  19. find_library(
  20. # 设置路径变量的名称。
  21. libuv-lib
  22. # 指定希望CMake定位的NDK库的名称。
  23. uv
  24. )
  25. add_library(libassimp SHARED IMPORTED)
  26. set_target_properties(
  27. libassimp
  28. PROPERTIES
  29. IMPORTED_LOCATION
  30. ${CMAKE_CURRENT_SOURCE_DIR}/libs/arm64-v8a/libassimp.so
  31. )
  32. find_library(
  33. # 设置路径变量的名称。
  34. xengine-lib
  35. # 指定希望CMake定位的NDK库的名称。
  36. xengine
  37. )
  38. target_link_libraries(nativerender PUBLIC
  39. ${hilog-lib} ${libace-lib} ${libnapi-lib} ${libuv-lib} libnative_window.so libc++.a libktx librawfile.z.so libassimp ${xengine-lib})
  ```

### 集成XEngine时域AI超分（OpenGL ES）

使用EGL和OpenGL ES图形API搭建图像渲染管线并集成时域AI超分在Native层实现，渲染结果通过[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件显示到屏幕。

本节阐述OpenGL ES图形API的时域AI超分的使用。

在调用XEngine Kit能力前，需要先通过[Syscap](../harmonyos-references/syscap.md#判断-api-是否可以使用)查询您的目标设备是否支持SystemCapability.Graphic.XEngine系统能力。

1. 调用[HMS\_XEG\_GetString](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_getstring)接口，获取XEngine支持的扩展信息，只有在支持[XEG\_TEMPORAL\_UPSCALE\_EXTENSION\_NAME](../harmonyos-references/xengine-kit-xengine.md#xeg_temporal_upscale_extension_name)扩展时才可以使用时域AI超分的相关接口。

   ```
   1. // 查询XEngine支持的GLES扩展信息
   2. const char* extensions = (const char*)HMS_XEG_GetString(XEG_EXTENSIONS);
   3. // 检查是否支持时域AI超分
   4. if (!strstr(extensions, XEG_TEMPORAL_UPSCALE_EXTENSION_NAME)) {
   5. exit(1); // return error
   6. }
   ```
2. 调用[HMS\_XEG\_TemporalUpscaleParameter](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_temporalupscaleparameter)接口，对时域AI超分的参数赋值。

   ```
   1. // m_lowResWidth与m_lowResHeight分别为用户自定义的渲染宽度与渲染高度，此处以800*600分辨率为例
   2. uint32_t m_lowResWidth = 800;
   3. uint32_t m_lowResHeight = 600;
   4. // 设置相机抖动的周期数，此处以8为例
   5. GLuint jitterNum = 8;

   7. GLsizei inputSize[2] = {static_cast<GLsizei>(m_lowResWidth), static_cast<GLsizei>(m_lowResHeight)};
   8. // 设置超分输入纹理的真实宽高
   9. HMS_XEG_TemporalUpscaleParameter(XEG_TEMPORAL_UPSCALE_INPUT_SIZE, inputSize);

   11. HMS_XEG_TemporalUpscaleParameter(XEG_TEMPORAL_UPSCALE_JITTER_NUM, &jitterNum);

   13. // 设置是否存在深度反转，此处为不存在深度反转
   14. GLboolean isDepthReversed = GL_FALSE;
   15. HMS_XEG_TemporalUpscaleParameter(XEG_TEMPORAL_UPSCALE_DEPTH_REVERSED, &isDepthReversed);

   17. // 设置是否重置历史帧数据，true表示重置，false表示不重置。在历史帧未使用超分，并且当前帧开始使用超分的情况下建议设置为true
   18. GLboolean resetHistory = GL_TRUE;
   19. HMS_XEG_TemporalUpscaleParameter(XEG_TEMPORAL_UPSCALE_RESET_HISTORY, &resetHistory);

   21. // 设置画面偏向当前帧（鬼影少但可能存在闪烁）还是历史帧（鬼影多但是更稳定）的平衡程度。此处以0.5为例
   22. GLfloat steadyLevel = 0.5;
   23. HMS_XEG_TemporalUpscaleParameter(XEG_TEMPORAL_UPSCALE_STEADY_LEVEL, &steadyLevel);
   ```
3. 调用[HMS\_XEG\_RenderTemporalUpscale](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_rendertemporalupscale)接口进行超分，每帧都需要调用。

   其中，参数jitterX和jitterY分别为相机在X方向和Y方向的抖动，是一个类似Halton的低差异序列。

   本例使用Halton算法计算Jitter值：使用Halton算法生成一个[0, 1]的序列，再减去0.5使序列范围保持在[-0.5, 0.5]，最后除以输入图像的分辨率，得到UV坐标下的Jitter值。

   1. 根据Halton算法生成每帧需要的相机抖动（Jitter）。

      ```
      1. // Halton算法示例
      2. float GetHaltonSequence(uint32_t index, uint32_t base) {
      3. float result = 0.0;
      4. float fraction = 1.0 / base;
      5. while (index > 0) {
      6. result += fraction * (index % base);
      7. index /= base;
      8. fraction /= base;
      9. }
      10. return result;
      11. }
      12. // 当前帧数，需要每帧+1，用于确定当前帧使用的Jitter值，使Jitter值在JitterNum范围内轮转
      13. uint64_t frameNum = 0;
      14. // jitterX与jitterY分别为相机在X和Y方向上的抖动
      15. float jitterX = 0.0;
      16. float jitterY = 0.0;
      ```

      ```
      1. // 此处需要保证生成的低差异序列长度与jitterNum保持一致，且在[-0.5, 0.5]的范围内
      2. jitterX = GetHaltonSequence((frameNum % jitterNum) + 1, 2) - 0.5;
      3. jitterY = GetHaltonSequence((frameNum % jitterNum) + 1, 3) - 0.5;
      4. // m_lowResWidth与m_lowResHeight为步骤2中的输入图像的宽度和高度
      5. jitterX = jitterX / m_lowResWidth;
      6. jitterY = jitterY / m_lowResHeight;
      ```
   2. 调用时域AI超分渲染接口。

      ```
      1. // 这里表示第一帧使用超分的情况下设置resetHistory为true，否则设置为false
      2. resetHistory = frameNum == 0 ? GL_TRUE : GL_FALSE;
      3. HMS_XEG_TemporalUpscaleParameter(XEG_TEMPORAL_UPSCALE_RESET_HISTORY, &resetHistory);

      5. // m_upscaleFBO为用户自定义创建的超分后的framebuffer
      6. unsigned int m_upscaleFBO;
      7. unsigned int m_highResWidth;
      8. unsigned int m_highResHeight;
      9. unsigned int m_lowLightColorTexture;
      10. unsigned int m_lowGboDepth;
      11. unsigned int m_motionVectorTexture, m_dynamicMaskTexture;

      13. glBindFramebuffer(GL_FRAMEBUFFER, m_upscaleFBO);
      14. glViewport(0, 0, m_highResWidth, m_highResHeight);
      15. glScissor(0, 0, m_highResWidth, m_highResHeight);

      17. // m_lowLightColorTexture为超分输入纹理。
      18. // m_lowGboDepth为深度纹理。
      19. // m_motionVectorTexture为运动矢量图像。运动矢量的计算方式为当前渲染像素的NDC坐标的XY值减去上一帧的NDC坐标的XY值。
      20. // m_dynamicMaskTexture为物体的动态遮罩图像，格式需要是GL_RED或其兼容格式。R通道的合法值为0.0、0.2或1.0，其中0.0表示静态物体，0.2表示运动物体如人物，1.0表示特效或半透明物体。
      21. // jitterX 相机在X方向上的抖动。
      22. // jitterY 相机在Y方向上的抖动。
      23. HMS_XEG_RenderTemporalUpscale(m_lowLightColorTexture, m_lowGboDepth, m_motionVectorTexture, m_dynamicMaskTexture,
      24. -0.5*jitterX, -0.5*jitterY);
      ```

### 集成XEngine时域AI超分（Vulkan）

使用Vulkan图形API搭建图像渲染管线，并集成时域AI超分在Native层实现，渲染结果通过[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件显示到屏幕。

本节阐述Vulkan图形API的时域AI超分使用，详细代码请参见[Samplecode](https://gitcode.com/harmonyos_samples/xengine-samplecode-vulkan-temporal-upscale-demo-cpp)。

在调用XEngine Kit能力前，需要先通过[Syscap](../harmonyos-references/syscap.md#判断-api-是否可以使用)查询您的目标设备是否支持SystemCapability.Graphic.XEngine系统能力。

1. 调用[HMS\_XEG\_EnumerateDeviceExtensionProperties](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口，获取XEngine支持的扩展信息，只有在支持[XEG\_TEMPORAL\_UPSCALE\_EXTENSION\_NAME](../harmonyos-references/xengine-kit-xengine.md#xeg_temporal_upscale_extension_name)扩展时才可以使用时域AI超分的相关接口。

   ```
   1. // physicalDevice为Vulkan物理设备，用户需进行初始化
   2. VkPhysicalDevice physicalDevice;
   3. // 查询XEngine支持的Vulkan扩展列表
   4. std::vector<std::string> supportedExtensions;
   5. uint32_t pPropertyCount;
   6. HMS_XEG_EnumerateDeviceExtensionProperties(physicalDevice, &pPropertyCount, nullptr);
   7. if (pPropertyCount > 0) {
   8. std::vector<XEG_ExtensionProperties> pProperties(pPropertyCount);
   9. if (HMS_XEG_EnumerateDeviceExtensionProperties(physicalDevice, &pPropertyCount,
   10. &pProperties.front()) == VK_SUCCESS) {
   11. for (auto ext : pProperties) {
   12. supportedExtensions.push_back(ext.extensionName);
   13. }
   14. }
   15. }
   16. // 查询是否支持时域AI超分
   17. if (std::find(supportedExtensions.begin(), supportedExtensions.end(), XEG_TEMPORAL_UPSCALE_EXTENSION_NAME) ==
   18. supportedExtensions.end()) {
   19. exit(1); // return error;
   20. }
   ```
2. 声明实例句柄。

   ```
   1. XEG_TemporalUpscale xegTemporalUpscale;
   ```
3. 调用[HMS\_XEG\_CreateTemporalUpscale](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_createtemporalupscale)接口，创建时域AI超分实例。

   ```
   1. // 渲染宽高和超分后宽高均为用户自定义参数，这里将以800*600的分辨率进行1.5倍超分到1200*900的分辨率为例
   2. uint32_t lowResWidth = 800;
   3. uint32_t lowResHeight = 600;
   4. uint32_t highResWidth = 1200;
   5. uint32_t highResHeight = 900;
   6. const uint32_t jitterNum = 8;
   7. // Vulkan逻辑设备，用户需进行初始化
   8. VkDevice device;
   9. // XEG_TemporalUpscaleCreateInfo为创建XEG_TemporalUpscale对象所需信息
   10. XEG_TemporalUpscaleCreateInfo createInfo;
   11. // 指定输入图像的大小，即低分辨率图像的尺寸
   12. createInfo.inputSize = {lowResWidth, lowResHeight};
   13. // 指定输出图像的大小，即高分辨率图像的尺寸
   14. createInfo.outputSize = {highResWidth, highResHeight};
   15. // 指定输出图像的颜色格式
   16. createInfo.outputFormat = VK_FORMAT_R8G8B8A8_UNORM;
   17. // jitterNum为相机抖动的周期数
   18. createInfo.jitterNum = jitterNum;
   19. // 指定了深度值是否反转
   20. createInfo.isDepthReversed = true;
   21. VkResult res = HMS_XEG_CreateTemporalUpscale(device, &createInfo, &xegTemporalUpscale);
   22. if (res != VK_SUCCESS) {
   23. exit(1); // return error;
   24. }
   ```
4. 调用[HMS\_XEG\_CmdRenderTemporalUpscale](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_cmdrendertemporalupscale)接口下发超分，每帧都需要调用。

   其中，参数jitterX和jitterY分别为相机在X方向和Y方向的抖动，是一个类似Halton的低差异序列。

   本例使用Halton算法计算Jitter值：使用Halton算法生成一个[0, 1]的序列，再减去0.5使序列范围保持在[-0.5, 0.5]，最后除以输入图像的分辨率，得到UV坐标下的Jitter值。

   1. 根据Halton算法生成每帧需要的相机抖动（Jitter）。

      ```
      1. // Halton算法示例
      2. float GetHaltonSequence(uint32_t index, uint32_t base) {
      3. float result = 0.0;
      4. float fraction = 1.0 / base;
      5. while (index > 0) {
      6. result += fraction * (index % base);
      7. index /= base;
      8. fraction /= base;
      9. }
      10. return result;
      11. }
      ```
   2. 调用时域AI超分渲染接口。

      ```
      1. // 当前帧数，需要每帧+1，用于确定当前帧使用的Jitter值，使Jitter值在JitterNum范围内轮转
      2. uint64_t frameNum = 0;
      3. // jitterX与jitterY分别为相机在X和Y方向上的抖动
      4. float jitterX = 0.0;
      5. float jitterY = 0.0;
      6. // 定义XEG_TemporalUpscaleDescription对象xegDescription
      7. XEG_TemporalUpscaleDescription xegDescription;
      8. // inputImageView为用户创建的超分输入图像的VkImageView
      9. VkImageView inputImageView = VK_NULL_HANDLE;
      10. // depthImageView为用户创建的深度图像的VkImageView
      11. VkImageView motionVectorImageView= VK_NULL_HANDLE;
      12. // motionVectorImageView为用户创建的运动矢量图像的VkImageView
      13. VkImageView depthImageView = VK_NULL_HANDLE;
      14. // dynamicMaskImageView为用户创建的物体动态遮罩图像的VkImageView
      15. VkImageView dynamicMaskImageView = VK_NULL_HANDLE;
      16. // outputImageView为用户创建的超分输出图像的VkImageView
      17. VkImageView outputImageView = VK_NULL_HANDLE;
      18. // commandBuffer为命令缓冲区，用户需进行初始化
      19. VkCommandBuffer commandBuffer = VK_NULL_HANDLE;
      20. xegDescription.inputImage = inputImageView;
      21. xegDescription.depthImage = depthImageView;
      22. xegDescription.motionVectorImage = motionVectorImageView;
      23. xegDescription.dynamicMaskImage = dynamicMaskImageView;
      24. xegDescription.outputImage = outputImageView;
      25. // 此处需要保证生成的低差异序列长度与jitterNum保持一致，且在[-0.5, 0.5]的范围内
      26. jitterX = GetHaltonSequence((frameNum % jitterNum) + 1, 2) - 0.5;
      27. jitterY = GetHaltonSequence((frameNum % jitterNum) + 1, 3) - 0.5;
      28. // lowResWidth与lowResHeight为步骤3中的输入图像的宽度和高度
      29. jitterX = jitterX / lowResWidth;
      30. jitterY = jitterY / lowResHeight;
      31. xegDescription.jitterX = -jitterX;
      32. xegDescription.jitterY = -jitterY;
      33. // resetHistory为选择是否重置历史帧数据，true表示重置，false则表示不重置，此处以true为例
      34. xegDescription.resetHistory = (frameNum == 0) ? true : false;
      35. // steadyLevel为画面偏向当前帧还是历史帧的平衡程度，取值范围为[0.0, 1.0]，此处以平衡程度为0.5为例
      36. xegDescription.steadyLevel = 0.5;
      37. HMS_XEG_CmdRenderTemporalUpscale(commandBuffer, xegTemporalUpscale, &xegDescription);
      ```
5. 调用[HMS\_XEG\_DestroyTemporalUpscale](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_destroytemporalupscale)接口销毁实例。

   ```
   1. if (xegTemporalUpscale) {
   2. HMS_XEG_DestroyTemporalUpscale(xegTemporalUpscale);
   3. }
   ```
