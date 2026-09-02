---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xengine-kit-high-performance-gpu-sorting
title: 高性能GPU排序
breadcrumb: 指南 > 图形 > XEngine Kit（GPU加速引擎服务） > Maleoon API > 高性能GPU排序
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:51+08:00
doc_updated_at: 2026-08-03
content_hash: sha256:6cb0014b713f89af66123547e4df08633c9435a1b58fc09cc155bc88906f596a
---

从6.0.0(20) 版本开始，新增高性能GPU排序特性。

XEngine Kit高性能着色器(High Performance Shaders，HPS)特性提供GPU排序能力。相比于其它排序能力，该能力依托于华为Maleoon GPU的软硬结合优化，效率更高。

## 约束与限制

可通过以下方式查询相关扩展特性是否支持：

对于Vulkan，使用[HMS\_XEG\_EnumerateDeviceExtensionProperties](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)扩展特性查询接口进行查询，如查询结果包含XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME，则表示支持该特性，若查询结果未包含，则表示不支持该特性。

## 接口说明

以下接口为使用高性能GPU排序所需要使用的接口，关于这些接口的详细说明见[接口文档](../harmonyos-references/xengine-kit-xengine.md)。

| 接口名 | 描述 |
| --- | --- |
| VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CreateHPS (VkDevice device, const XEG\_HPSCreateInfo \*pCreateInfo, XEG\_HPS \*pHps) | 创建XEG\_HPS对象。 |
| VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_DestroyHPS (XEG\_HPS hps) | 销毁XEG\_HPS对象。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CmdRadixSortHPS (VkCommandBuffer commandBuffer, XEG\_HPS hps, const XEG\_HPSRadixSortDescription \*pDescription) | 录制HPS排序命令，使用此接口前需要通过HMS\_XEG\_EnumerateDeviceExtensionProperties接口查询是否支持XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME扩展。 |

## 业务流程

* 下面是以Vulkan应用程序渲染为例，说明使用高性能GPU排序的主要业务流程

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/AA19c6t9TOK3WY7Oseb7YQ/zh-cn_image_0000002706674814.jpg)

1. 应用调用[HMS\_XEG\_EnumerateDeviceExtensionProperties](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口获取XEngine Kit支持的扩展属性列表。检查返回列表中是否包含[XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](../harmonyos-references/xengine-kit-xengine.md#xeg_hps_radix_sort_extension_name)。若不包含，则当前设备不支持此特性，流程终止。
2. 应用准备HPS相关资源（keyBuffer、indexBuffer等）。
3. 应用调用[HMS\_XEG\_CreateHPS](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_createhps)接口创建HPS实例。
4. 应用调用[HMS\_XEG\_CmdRadixSortHPS](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_cmdradixsorthps)录制排序命令，并提交到GPU队列执行。
5. 当不再需要排序时，应用调用[HMS\_XEG\_DestroyHPS](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_destroyhps)接口销毁HPS实例，释放全部GPU资源。销毁后HPS句柄失效，不可再使用。

## 开发步骤

本章以在Vulkan应用程序渲染为例，说明使用高性能GPU排序的开发步骤。

### 配置项目

编译HAP包时，Native层so需要依赖NDK中的XEngine相关库和头文件。

* 头文件引用

  ```cpp
  #include <algorithm>
  #include <vector>
  #include <string>
  #include <xengine/xeg_vulkan_hps.h>
  #include <xengine/xeg_vulkan_extension.h>
  #include <xengine/xeg_extension_defs.h>
  ```
* CMakeLists.txt添加库依赖

  CMakeLists.txt中添加对XEngine动态链接库依赖的代码如下。

  ```cpp
  find_library(
      # 设置路径变量的名称。
      xengine-lib
      # 指定希望CMake定位的NDK库的名称。
      xengine
  )
  target_link_libraries(nativerender PUBLIC
      # 其他库文件
      # ...
      ${xengine-lib})
  ```

### 集成高性能GPU排序（Vulkan）

XEngine 高性能GPU排序可以独立使用。相关代码在Native层实现。

在调用XEngine Kit特性接口前，需要先通过[Syscap](../harmonyos-references/syscap.md#什么是systemcapabilitysyscap)查询确认您的目标设备支持SystemCapability.Graphic.XEngine系统能力。

1. 调用[HMS\_XEG\_EnumerateDeviceExtensionProperties](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口，获取XEngine支持的扩展信息，只有在支持XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME扩展时才可以使用高性能GPU排序接口。

   ```cpp
   VkPhysicalDevice physicalDevice;
   std::vector<std::string> supportedExtensions;
   uint32_t propertyCount;
   HMS_XEG_EnumerateDeviceExtensionProperties(physicalDevice, &propertyCount, nullptr);
   if (propertyCount > 0) {
       std::vector<XEG_ExtensionProperties> properties(propertyCount);
       if (HMS_XEG_EnumerateDeviceExtensionProperties(physicalDevice, &propertyCount, &properties.front()) ==
           VK_SUCCESS) {
           for (auto ext : properties) {
               supportedExtensions.push_back(ext.extensionName);
           }
       }
   }
   if (std::find(supportedExtensions.begin(), supportedExtensions.end(), XEG_HPS_RADIX_SORT_EXTENSION_NAME) ==
       supportedExtensions.end()) {
       exit(1);
   }
   ```
2. 准备HPS相关资源。

   ```cpp
   VkDevice device;
   VkCommandBuffer cmdBuffer;
   VkQueue queue;
   // 要被排序的key
   VkBuffer keyBuffer;
   // 与key对应的value
   VkBuffer indexBuffer;
   // 排序量
   VkBuffer sortCount;
   ```
3. 声明实例句柄。

   ```cpp
   XEG_HPS xegHPS { VK_NULL_HANDLE };
   ```
4. 调用[HMS\_XEG\_CreateHPS](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_createhps)接口，实例化句柄。

   ```cpp
   // 构造输入描述符
   XEG_HPSRadixSort sortInfo{
       XEG_STRUCTURE_TYPE_HPS_RADIX_SORT,
       nullptr
   };

   XEG_HPSCreateInfo info {
       XEG_STRUCTURE_TYPE_HPS_CREATE_INFO,
       &sortInfo
   };
   // 实例化句柄
   VkResult res = HMS_XEG_CreateHPS(device, &info, &xegHPS);
   if (res != VK_SUCCESS) {
       // 错误处理
       // ...
   }
   ```
5. 构造排序描述符，调用[HMS\_XEG\_CmdRadixSortHPS](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_cmdradixsorthps)接口录制排序命令。

   ```cpp
   VkCommandBufferBeginInfo cmdBufferBeginInfo {};
   cmdBufferBeginInfo.sType = VK_STRUCTURE_TYPE_COMMAND_BUFFER_BEGIN_INFO;

   // 录制排序命令
   vkBeginCommandBuffer(cmdBuffer, &cmdBufferBeginInfo);
   XEG_HPSRadixSortDescription sortDescription{
       XEG_STRUCTURE_TYPE_HPS_RADIX_SORT_DESCRIPTION,
       nullptr,
       sortCount,
       keyBuffer,
       indexBuffer
   };
   VkResult res = HMS_XEG_CmdRadixSortHPS(cmdBuffer, xegHPS, &sortDescription);
   if (res != VK_SUCCESS) {
       // 错误处理
       // ...
   }
   vkEndCommandBuffer(cmdBuffer);
   ```
6. 提交排序命令。

   ```cpp
   // 提交command buffer
   VkResult res;
   {
       VkSubmitInfo submitInfo{};
       submitInfo.sType = VK_STRUCTURE_TYPE_SUBMIT_INFO;
       submitInfo.waitSemaphoreCount = 0;
       submitInfo.signalSemaphoreCount = 0;
       submitInfo.pSignalSemaphores = nullptr;
       submitInfo.commandBufferCount = 1;
       submitInfo.pCommandBuffers = &cmdBuffer;
       submitInfo.pWaitSemaphores = nullptr;
       res = vkQueueSubmit(queue, 1, &submitInfo, nullptr);
   }
   // 等待结束
   vkDeviceWaitIdle(device);
   ```
7. 销毁HPS对象。

   ```cpp
   if(xegHPS){
       HMS_XEG_DestroyHPS(xegHPS);
   }
   ```
