---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xengine-kit-rt-reflection
title: 光线追踪反射
breadcrumb: 指南 > 图形 > XEngine Kit（GPU加速引擎服务） > 光线追踪反射
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:44+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:6247fdd5e93bffaa88902d520f70e72543a574cea3ae02f038bf240e02e3d107
---

从6.0.0(20) 版本开始，新增光线追踪反射特性。

XEngine Kit提供光线追踪反射（Ray-Traced Reflections）渲染能力。相比于该效果的传统光线追踪实现方式，依托于华为马良GPU的软硬结合优化，XEngine支持FERT(Flexible Entry Raytracing)求交加速技术，可以减少光线与场景几何的求交计算次数，从而降低实现高画质光追效果时的GPU负载。

## 约束与限制

* 支持的设备类型：此特性依赖设备支持Vulkan光线追踪扩展[VK\_KHR\_acceleration\_structure](https://docs.vulkan.org/refpages/latest/refpages/source/VK_KHR_acceleration_structure.html)、[VK\_KHR\_ray\_query](https://docs.vulkan.org/refpages/latest/refpages/source/VK_KHR_ray_query.html)
* 可通过以下方式查询相关扩展特性是否支持：

  对于Vulkan，使用[HMS\_XEG\_EnumerateDeviceExtensionProperties](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)扩展特性查询接口进行查询，如查询结果包含XEG\_RT\_REFLECTION\_EXTENSION\_NAME，则表示支持该特性，若查询结果未包含，则表示不支持该特性。

## 接口说明

以下接口为使用光线追踪反射特性需要使用的接口，关于这些接口的详细说明见[接口文档](../harmonyos-references/xengine-kit-xengine.md)。

| 接口名 | 描述 |
| --- | --- |
| VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_EnumerateDeviceExtensionProperties (VkPhysicalDevice physicalDevice, uint32\_t \* pPropertyCount, XEG\_ExtensionProperties \* pProperties) | XEngine Vulkan扩展特性查询接口。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CreateRTReflection(VkDevice device, const void\* pCreateInfo, XEG\_RTReflection\* pRtReflection) | 创建XEG\_RTReflection对象。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CmdRenderRTReflection(VkCommandBuffer commandBuffer, XEG\_RTReflection rtReflection, const void\* pDescription) | 录制计算RT反射命中信息命令。 |
| VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_DestroyRTReflection(XEG\_RTReflection rtReflection) | 销毁XEG\_RTReflection对象。 |

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/vRLMrd9DTBGwE927KN-0sQ/zh-cn_image_0000002589245045.png?HW-CC-KV=V1&HW-CC-Date=20260429T053643Z&HW-CC-Expire=86400&HW-CC-Sign=DE58B3449765EBAACF61E3E735C7882C42AF3CE7ACA907ECFBCA1B7EEA9588EF)

1. 用户进入光线追踪反射适用的游戏场景。
2. 游戏应用调用HMS\_XEG\_CreateRTReflection接口创建光线追踪反射实例。如果光线追踪反射创建失败，直接调用后处理并送显当前帧即可。
3. 游戏应用调用HMS\_XEG\_CmdRenderRTReflection接口计算光线追踪反射命中信息，并返回错误码。如果计算失败，直接调用后处理并送显当前帧即可。
4. 游戏应用根据3中计算的反射命中信息，生成反射图像。
5. 游戏应用将反射图像和游戏的主场景渲染结果进行融合。
6. 游戏应用完成其余后处理，并送显当前帧。
7. 用户退出光线追踪反射适用的游戏场景。
8. 游戏应用调用HMS\_XEG\_HMS\_XEG\_DestroyRTReflection接口销毁光线追踪反射实例。

## 开发步骤

本章以在Vulkan应用程序中集成为例，说明XEngine集成操作过程。

### 配置项目

编译HAP时，Native层so编译需要依赖NDK中的libxengine.so。

* 头文件引用

  ```
  1. #include <algorithm>
  2. #include <string>
  3. #include <vector>
  4. #include "xengine/xeg_vulkan_extension.h"
  5. #include <xengine/xeg_vulkan_rt_reflection.h>
  ```
* 编写CMakeLists.txt

  CMakeLists.txt部分示例代码如下

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

### 集成XEngine光线追踪反射（Vulkan）

使用Vulkan图形API搭建图像渲染管线，并集成光线追踪反射效果的代码需要在Native层实现，渲染结果通过[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件显示到屏幕。

在调用XEngine Kit能力前，需要先通过[Syscap](../harmonyos-references/syscap.md#判断-api-是否可以使用)查询您的目标设备是否支持SystemCapability.Graphic.XEngine系统能力。

1. 调用[HMS\_XEG\_EnumerateDeviceExtensionProperties](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口，获取XEngine支持的扩展信息，只有在支持XEG\_RT\_REFLECTION\_EXTENSION\_NAME扩展时才可以使用光线追踪反射的相关接口。

   ```
   1. // physicalDevice为Vulkan物理设备，用户需进行初始化
   2. VkPhysicalDevice physicalDevice;
   3. // 查询XEngine支持的Vulkan扩展列表
   4. std::vector<std::string> supportedExtensions;
   5. uint32_t propertyCount;
   6. HMS_XEG_EnumerateDeviceExtensionProperties(physicalDevice, &propertyCount, nullptr);
   7. if (propertyCount > 0) {
   8. std::vector<XEG_ExtensionProperties> properties(propertyCount);
   9. if (HMS_XEG_EnumerateDeviceExtensionProperties(physicalDevice, &propertyCount, &properties.front()) == VK_SUCCESS) {
   10. for (auto ext : properties) {
   11. supportedExtensions.push_back(ext.extensionName);
   12. }
   13. }
   14. }
   15. // 查询是否支持光线追踪反射特性
   16. if (std::find(supportedExtensions.begin(), supportedExtensions.end(), XEG_RT_REFLECTION_EXTENSION_NAME) ==
   17. supportedExtensions.end()) {
   18. exit(1); // 错误
   19. }
   ```
2. 声明实例句柄。

   ```
   1. XEG_RTReflection xegRTReflection;
   ```
3. 调用[HMS\_XEG\_CreateRTReflection](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_creatertreflection)接口，创建光线追踪反射实例。

   ```
   1. // 创建光线追踪反射实例所需的宽高信息为用户自定义参数，这里将以800*600的分辨率为例
   2. uint32_t reflectWidth = 800;
   3. uint32_t reflectHeight = 600;
   4. // vulkan逻辑设备，用户需进行初始化
   5. VkDevice device;
   6. // XEG_RTReflectionCreateInfo为创建xegRTReflection对象信息
   7. XEG_RTReflectionCreateInfo xegRTReflectionCreateInfo;
   8. // 指定是否开启快速求交模式。默认为0，表示不开启快速求交模式
   9. xegRTReflectionCreateInfo.enableFastTrace = 0;
   10. // 指定XEG_StructureType值，必须是XEG_STRUCTURE_TYPE_RT_REFLECTION_CREATE_INFO
   11. xegRTReflectionCreateInfo.sType = XEG_STRUCTURE_TYPE_RT_REFLECTION_CREATE_INFO;
   12. // 指定输入图像尺寸
   13. xegRTReflectionCreateInfo.renderSize = VkExtent2D{ reflectWidth, reflectHeight };
   14. VkResult ret = HMS_XEG_CreateRTReflection(device, &xegRTReflectionCreateInfo, &xegRTReflection);
   15. if (ret != VK_SUCCESS) {
   16. exit(1);  // 错误
   17. }
   ```
4. 调用[HMS\_XEG\_CmdRenderRTReflection](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_cmdrenderrtreflection)接口下发渲染命令，每帧都需要调用。

   ```
   1. // 反射渲染输入信息
   2. XEG_RTReflectionDescription xegRTReflectionDescription;
   3. // inputRayOriginImage为用户创建的光线原点图像的VkImageView
   4. VkImageView inputRayOriginImage = VK_NULL_HANDLE;
   5. // inputRayDirectionImage为用户创建的光线方向图像的VkImageView
   6. VkImageView inputRayDirectionImage = VK_NULL_HANDLE;
   7. // outputReflectionInfoImage为用户创建的用于记录光线追踪求交结果的VkImageView
   8. VkImageView outputReflectionInfoImage = VK_NULL_HANDLE;
   9. // sceneTlas是场景的Top Level光线追踪加速结构
   10. VkAccelerationStructureKHR sceneTlas = VK_NULL_HANDLE;
   11. xegRTReflectionDescription.inputRayOriginImage = inputRayOriginImage;
   12. xegRTReflectionDescription.inputRayDirectionImage = inputRayDirectionImage;
   13. xegRTReflectionDescription.outputReflectionInfoImage = outputReflectionInfoImage;
   14. xegRTReflectionDescription.accelerationStructure = sceneTlas;
   15. xegRTReflectionDescription.rayMin = 0.01;
   16. xegRTReflectionDescription.rayMax = 1e10;
   17. xegRTReflectionDescription.sType = XEG_STRUCTURE_TYPE_RT_REFLECTION_DESCRIPTION;
   18. xegRTReflectionDescription.reflectionCullMask = 0xff;
   19. // commandBuffer为命令缓冲区，用户需进行初始化
   20. VkCommandBuffer commandBuffer = VK_NULL_HANDLE;
   21. VkResult retRender = HMS_XEG_CmdRenderRTReflection(commandBuffer, xegRTReflection, &xegRTReflectionDescription);
   22. if (retRender != VK_SUCCESS) {
   23. exit(1);  // 错误
   24. }
   ```
5. 调用[HMS\_XEG\_DestroyRTReflection](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_destroyrtreflection)接口销毁实例，释放资源，当特性不再使用或应用退出时需要调用。

   ```
   1. if (xegRTReflection != VK_NULL_HANDLE) {
   2. HMS_XEG_DestroyRTReflection(xegRTReflection);
   3. }
   ```
