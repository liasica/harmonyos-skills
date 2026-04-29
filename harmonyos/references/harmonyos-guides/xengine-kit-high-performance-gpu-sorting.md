---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xengine-kit-high-performance-gpu-sorting
title: 高性能GPU排序
breadcrumb: 指南 > 图形 > XEngine Kit（GPU加速引擎服务） > Maleoon API > 高性能GPU排序
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:44+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:ab254ce0f73b747e0570797c2f85e0b551ccdcb2c639e28bc41aaa3977ead20a
---

从6.0.0(20) 版本开始，新增高性能GPU排序特性。

XEngine Kit HPS特性提供高性能GPU排序能力。相比于其它排序能力，该能力依托于华为Maleoon GPU的软硬结合优化，效率更高。

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

## 开发步骤

本章以在Vulkan应用程序渲染为例，说明使用高性能GPU排序的开发步骤。

### 配置项目

编译HAP时，Native层so需要依赖NDK中的XEngine相关库和头文件。

* 头文件引用

  ```
  1. #include <algorithm>
  2. #include <vector>
  3. #include <string>
  4. #include <xengine/xeg_vulkan_hps.h>
  5. #include <xengine/xeg_vulkan_extension.h>
  6. #include <xengine/xeg_extension_defs.h>
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

### 集成高性能GPU排序（Vulkan）

XEngine 高性能GPU排序可以独立使用。相关代码在Native层实现。

在调用XEngine Kit特性接口前，需要先通过[Syscap](../harmonyos-references/syscap.md#判断-api-是否可以使用)查询确认您的目标设备支持SystemCapability.Graphic.XEngine系统能力。

1. 调用[HMS\_XEG\_EnumerateDeviceExtensionProperties](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口，获取XEngine支持的扩展信息，只有在支持XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME扩展时才可以使用高性能GPU排序接口。

   ```
   1. VkPhysicalDevice physicalDevice;
   2. std::vector<std::string> supportedExtensions;
   3. uint32_t propertyCount;
   4. HMS_XEG_EnumerateDeviceExtensionProperties(physicalDevice, &propertyCount, nullptr);
   5. if (propertyCount > 0) {
   6. std::vector<XEG_ExtensionProperties> properties(propertyCount);
   7. if (HMS_XEG_EnumerateDeviceExtensionProperties(physicalDevice, &propertyCount, &properties.front()) ==
   8. VK_SUCCESS) {
   9. for (auto ext : properties) {
   10. supportedExtensions.push_back(ext.extensionName);
   11. }
   12. }
   13. }
   14. if (std::find(supportedExtensions.begin(), supportedExtensions.end(), XEG_HPS_RADIX_SORT_EXTENSION_NAME) ==
   15. supportedExtensions.end()) {
   16. exit(1);
   17. }
   ```
2. 准备HPS相关资源。

   ```
   1. VkDevice device;
   2. VkCommandBuffer cmdBuffer;
   3. VkQueue queue;
   4. // 要被排序的key
   5. VkBuffer keyBuffer;
   6. // 与key对应的value
   7. VkBuffer indexBuffer;
   8. // 排序量
   9. VkBuffer sortCount;
   ```
3. 声明实例句柄。

   ```
   1. XEG_HPS xegHPS { VK_NULL_HANDLE };
   ```
4. 调用[HMS\_XEG\_CreateHPS](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_createhps)接口，实例化句柄。

   ```
   1. // 构造输入描述符
   2. XEG_HPSRadixSort sorInfo{
   3. XEG_STRUCTURE_TYPE_HPS_RADIX_SORT,
   4. nullptr
   5. };

   7. XEG_HPSCreateInfo info {
   8. XEG_STRUCTURE_TYPE_HPS_CREATE_INFO,
   9. &sorInfo
   10. };
   11. // 实例化句柄
   12. HMS_XEG_CreateHPS(device, &info, &xegHPS);
   ```
5. 构造排序描述符，调用[HMS\_XEG\_CmdRadixSortHPS](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_cmdradixsorthps)接口录制排序命令。

   ```
   1. VkCommandBufferBeginInfo cmdBufferBeginInfo {};
   2. cmdBufferBeginInfo.sType = VK_STRUCTURE_TYPE_COMMAND_BUFFER_BEGIN_INFO;

   4. // 录制排序命令
   5. vkBeginCommandBuffer(cmdBuffer, &cmdBufferBeginInfo);
   6. XEG_HPSRadixSortDescription sortDescription{
   7. XEG_STRUCTURE_TYPE_HPS_RADIX_SORT_DESCRIPTION,
   8. nullptr,
   9. sortCount,
   10. keyBuffer,
   11. indexBuffer
   12. };
   13. HMS_XEG_CmdRadixSortHPS(cmdBuffer, xegHPS, &sortDescription);
   14. vkEndCommandBuffer(cmdBuffer);
   ```
6. 提交排序命令。

   ```
   1. // 提交command buffer
   2. VkResult res;
   3. {
   4. VkSubmitInfo submitInfo{};
   5. submitInfo.sType = VK_STRUCTURE_TYPE_SUBMIT_INFO;
   6. submitInfo.waitSemaphoreCount = 0;
   7. submitInfo.signalSemaphoreCount = 0;
   8. submitInfo.pSignalSemaphores = nullptr;
   9. submitInfo.commandBufferCount = 1;
   10. submitInfo.pCommandBuffers = &cmdBuffer;
   11. submitInfo.pWaitSemaphores = nullptr;
   12. res = vkQueueSubmit(queue, 1, &submitInfo, nullptr);
   13. }
   14. // 等待结束
   15. vkDeviceWaitIdle(device);
   ```
7. 销毁HPS对象。

   ```
   1. if(xegHPS){
   2. HMS_XEG_DestroyHPS(xegHPS);
   3. }
   ```
