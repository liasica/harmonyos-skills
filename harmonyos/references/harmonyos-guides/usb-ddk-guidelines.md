---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/usb-ddk-guidelines
title: 开发适用USB协议的设备驱动
breadcrumb: 指南 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > 扩展外设专项驱动开发 > 开发适用USB协议的设备驱动
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:58f5d35aa1d7cfee0ce0f6e121b7fde1edef2589c521ccb811ab3d29657d9025
---

## 简介

UsbDdk（USB Driver Development Kit）是为开发者提供的USB驱动程序开发套件，支持开发者基于用户态，在应用层开发USB设备驱动。提供了一系列主机侧访问设备的接口，包括主机侧打开和关闭接口、管道同步异步读写通信、控制传输、中断传输等。

凡是采用USB总线，通过USB协议传输数据的设备都可以使用UsbDdk开发设备驱动。特别是内核标准驱动不支持的扩展外设，可以通过UsbDdk开发的扩展外设驱动应用实现其独特的设备能力。

### 基本概念

在进行UsbDdk开发前，开发者应了解以下基本概念：

* **USB**

  USB（Universal Serial Bus，通用串行总线）是一种广泛使用的接口技术，用于连接计算机与各种外部设备，如键盘、鼠标、打印机、存储设备、智能手机等。USB 的设计目标是提供一种标准化、高效且易于使用的连接方式，以替代传统的串行和并行接口。
* **DDK**

  DDK（Driver Development Kit）是HarmonyOS基于扩展外设框架，为开发者提供的驱动应用开发的工具包，可针对非标USB设备，开发对应的驱动。

### 实现原理

非标外设应用通过扩展外设管理服务获取USB设备的ID，通过RPC将ID和要操作的动作下发给USB驱动应用。USB驱动应用通过调用UsbDdk接口，可获取设备描述符与配置描述符，以及发送控制传输和中断传输等请求，DDK接口使用HDI服务将指令下发至内核驱动，内核驱动使用指令与设备通信。

**图1** UsbDdk调用原理

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/g6gI9fQERYK3a6sUTNB1GA/zh-cn_image_0000002583438519.png?HW-CC-KV=V1&HW-CC-Date=20260427T234437Z&HW-CC-Expire=86400&HW-CC-Sign=80A02C1DC5E36A24C93FBBBC703729AB7CB31521DE820718BF9CFA9D5FAFAA43)

## 约束与限制

* UsbDdk开放API支持USB接口非标外设扩展驱动开发场景。
* UsbDdk开放API仅允许DriverExtensionAbility生命周期内使用。
* 使用UsbDdk开放API需要在module.json5中声明匹配的ACL权限，例如ohos.permission.ACCESS\_DDK\_USB。

## 环境搭建

请参考[环境准备](environmental-preparation.md)完成开发前的准备工作。

## 开发指导

### 接口说明

| 名称 | 描述 |
| --- | --- |
| OH\_Usb\_Init(void) | 初始化DDK。 |
| OH\_Usb\_Release(void) | 释放DDK。 |
| OH\_Usb\_GetDeviceDescriptor(uint64\_t deviceId, struct UsbDeviceDescriptor \*desc) | 获取设备描述符。 |
| OH\_Usb\_GetConfigDescriptor(uint64\_t deviceId, uint8\_t configIndex, struct UsbDdkConfigDescriptor \*\*const config) | 获取配置描述符。请在描述符使用完后使用OH\_Usb\_FreeConfigDescriptor()释放描述符，否则会造成内存泄漏。 |
| OH\_Usb\_FreeConfigDescriptor(const struct UsbDdkConfigDescriptor \*const config) | 释放配置描述符，请在描述符使用完后释放描述符，否则会造成内存泄漏。 |
| OH\_Usb\_ClaimInterface(uint64\_t deviceId, uint8\_t interfaceIndex, uint64\_t \*interfaceHandle) | 声明接口。 |
| OH\_Usb\_SelectInterfaceSetting(uint64\_t interfaceHandle, uint8\_t settingIndex) | 激活接口的备用设置。 |
| OH\_Usb\_GetCurrentInterfaceSetting(uint64\_t interfaceHandle, uint8\_t \*settingIndex) | 获取接口当前激活的备用设置。 |
| OH\_Usb\_SendControlReadRequest(uint64\_t interfaceHandle, const struct UsbControlRequestSetup \*setup, uint32\_t timeout, uint8\_t \*data, uint32\_t \*dataLen) | 发送控制读请求，该接口为同步接口。 |
| OH\_Usb\_SendControlWriteRequest(uint64\_t interfaceHandle, const struct UsbControlRequestSetup \*setup, uint32\_t timeout, const uint8\_t \*data, uint32\_t dataLen) | 发送控制写请求，该接口为同步接口。 |
| OH\_Usb\_ReleaseInterface(uint64\_t interfaceHandle) | 释放接口。 |
| OH\_Usb\_SendPipeRequest(const struct UsbRequestPipe \*pipe, UsbDeviceMemMap \*devMmap) | 发送管道请求，该接口为同步接口。中断传输和批量传输都使用该接口发送请求。 |
| OH\_Usb\_CreateDeviceMemMap(uint64\_t deviceId, size\_t size, UsbDeviceMemMap \*\*devMmap) | 创建缓冲区。请在缓冲区使用完后，调用OH\_Usb\_DestroyDeviceMemMap()销毁缓冲区，否则会造成资源泄漏。 |
| OH\_Usb\_DestroyDeviceMemMap(UsbDeviceMemMap \*devMmap) | 销毁缓冲区。请在缓冲区使用完后及时销毁缓冲区，否则会造成资源泄漏。 |
| OH\_Usb\_GetDevices(struct Usb\_DeviceArray \*devices) | 获取USB设备ID列表。请保证传入的指针参数是有效的，申请的设备ID数组的大小建议不超过128，以避免过度占用内存。在使用完结构之后，释放成员内存，否则造成资源泄漏。获取到的USB设备ID，已通过驱动配置信息中的vid进行筛选过滤。 |

详细的接口说明请参考[UsbDdk](../harmonyos-references/capi-usbddk.md)。

### 开发步骤

以下步骤描述了如何使用 **UsbDdk**开发USB驱动：

**添加动态链接库**

CMakeLists.txt中添加以下lib。

```
1. libusb_ndk.z.so
```

**头文件**

```
1. #include <usb/usb_ddk_api.h>
2. #include <usb/usb_ddk_types.h>
```

1. 获取设备描述符。

   使用 **usb\_ddk\_api.h** 的 **OH\_Usb\_Init** 接口初始化DDK，并使用 **OH\_Usb\_GetDeviceDescriptor**获取到设备描述符。

   ```
   1. // 初始化USB DDK
   2. int32_t ret = OH_Usb_Init();
   3. OH_LOG_INFO(LOG_APP, "OH_Usb_Init ret=:%{public}d\n", ret);
   4. // ...
   5. struct UsbDeviceDescriptor devDesc;
   6. // 获取设备描述符
   7. ret = OH_Usb_GetDeviceDescriptor(g_devHandle, &devDesc);
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/UsbDriverDemo/entry/src/main/cpp/hello.cpp#L329-L342)
2. 获取配置描述符及声明接口。

   使用 **usb\_ddk\_api.h** 的 **OH\_Usb\_GetConfigDescriptor** 接口获取配置描述符 **config**，并使用 **OH\_Usb\_ClaimInterface** 声明"认领"接口。

   ```
   1. struct UsbDdkConfigDescriptor *config = nullptr;
   2. // 获取配置描述符
   3. auto ret = OH_Usb_GetConfigDescriptor(g_devHandle, 1, &config);
   4. OH_LOG_INFO(LOG_APP, "OH_Usb_GetConfigDescriptor ret = %{public}d", ret);
   5. if (ret != 0) {
   6. OH_LOG_ERROR(LOG_APP, "get config desc failed:%{public}d", ret);
   7. return false;
   8. }
   9. // 从配置描述符中找到手写板相关的接口和端点
   10. auto [res, interface, endpoint, maxPktSize] = GetInterfaceAndEndpoint(config);
   11. OH_LOG_INFO(LOG_APP, "OH_Usb_GetConfigDescriptor ret = %{public}d", res);
   12. if (!res) {
   13. OH_LOG_ERROR(LOG_APP, "GetInterfaceAndEndpoint failed");
   14. return false;
   15. }
   16. // 释放配置描述符，防止内存泄露
   17. OH_Usb_FreeConfigDescriptor(config);
   18. g_dataEp = endpoint;
   19. g_maxPktSize = maxPktSize;
   20. g_interface = interface;
   21. // 占用接口，同时也会卸载内核键盘驱动
   22. ret = OH_Usb_ClaimInterface(g_devHandle, g_interface, &g_interfaceHandle);
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/UsbDriverDemo/entry/src/main/cpp/hello.cpp#L296-L319)
3. 获取当前激活接口的备用设置及激活备用设置（可选）。

   使用 **usb\_ddk\_api.h** 的 **OH\_Usb\_GetCurrentInterfaceSetting** 获取备用设置，并使用 **OH\_Usb\_SelectInterfaceSetting** 激活备用设置。

   ```
   1. uint8_t settingIndex = 0;
   2. // 接口获取备用设置
   3. int32_t ret = OH_Usb_GetCurrentInterfaceSetting(g_interfaceHandle, &settingIndex);
   4. if (ret != USB_DDK_SUCCESS) {
   5. OH_LOG_ERROR(LOG_APP, "OH_Usb_GetCurrentInterfaceSetting failed, ret=%{public}d", ret);
   6. }

   8. // 激活备用设置
   9. ret = OH_Usb_SelectInterfaceSetting(g_interfaceHandle, settingIndex);
   10. if (ret != USB_DDK_SUCCESS) {
   11. OH_LOG_ERROR(LOG_APP, "OH_Usb_SelectInterfaceSetting failed, ret=%{public}d", ret);
   12. }
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/UsbDriverDemo/entry/src/main/cpp/hello.cpp#L202-L215)
4. 发送控制读请求、发送控制写请求（可选）。

   使用 **usb\_ddk\_api.h** 的**OH\_Usb\_SendControlReadRequest**发送控制读请求，或者使用**OH\_Usb\_SendControlWriteRequest**发送控制写请求。

   ```
   1. uint8_t strDesc[100] = {0};
   2. // 获取产品字符串描述符
   3. uint32_t len = 100;
   4. struct UsbControlRequestSetup strDescSetup;
   5. strDescSetup.bmRequestType = 0x80;
   6. strDescSetup.bRequest = 0x06;
   7. strDescSetup.wValue = (0x03 << BIT_EIGHT) | (iProduct); // desc Index
   8. strDescSetup.wIndex = 0x409;                    // language Id
   9. strDescSetup.wLength = len;
   10. auto ret = OH_Usb_SendControlReadRequest(g_interfaceHandle, &strDescSetup, UINT32_MAX, strDesc, &len);
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/UsbDriverDemo/entry/src/main/cpp/hello.cpp#L234-L245)

   ```
   1. // 设置feature
   2. uint32_t timeout = 5000;
   3. struct UsbControlRequestSetup strDescSetup;
   4. strDescSetup.bmRequestType = 0x21;
   5. strDescSetup.bRequest = 0x09;
   6. strDescSetup.wValue = ((0x03 << BIT_EIGHT) | 0x02); // desc Index
   7. strDescSetup.wIndex = 0x0;
   8. strDescSetup.wLength = 0x02;
   9. uint8_t data[128] = {0x02, 0x02};
   10. uint32_t dataLen = 2;
   11. int32_t ret = OH_Usb_SendControlWriteRequest(g_interfaceHandle, &strDescSetup, timeout, data, dataLen);
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/UsbDriverDemo/entry/src/main/cpp/hello.cpp#L366-L378)
5. 创建内存映射缓冲区及发送请求（可选）。

   使用 **usb\_ddk\_api.h** 的**OH\_Usb\_CreateDeviceMemMap**接口创建内存映射缓冲区**devMmap**，并使用**OH\_Usb\_SendPipeRequest**发送请求。

   ```
   1. // 占用接口，同时也会卸载内核键盘驱动
   2. // 创建用于存放数据的缓冲区
   3. int32_t ret = OH_Usb_CreateDeviceMemMap(g_devHandle, bufferLen, &devMmap);
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/UsbDriverDemo/entry/src/main/cpp/hello.cpp#L118-L122)

   ```
   1. struct UsbRequestPipe pipe;
   2. pipe.interfaceHandle = g_interfaceHandle;
   3. pipe.endpoint = g_dataEp;
   4. pipe.timeout = 4; // 中断传输超时时间，保持和手写板bInterval保持一致
   5. // 读取手写板数据
   6. // 通过USB中断传输方式，读取键值
   7. ret = OH_Usb_SendPipeRequest(&pipe, devMmap);
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/UsbDriverDemo/entry/src/main/cpp/hello.cpp#L136-L144)
6. 释放资源。

   在所有请求处理完毕，程序退出前，使用 **usb\_ddk\_api.h** 的 **OH\_Usb\_DestroyDeviceMemMap** 接口销毁缓冲区。使用**OH\_Usb\_ReleaseInterface**释放接口。使用**OH\_Usb\_Release**释放UsbDdk。

   ```
   1. // 销毁缓冲区
   2. OH_Usb_DestroyDeviceMemMap(devMmap);
   3. // 释放接口
   4. int32_t ret = OH_Usb_ReleaseInterface(g_interfaceHandle);
   5. if (ret != 0) {
   6. OH_LOG_ERROR(LOG_APP, "ReleaseInterface failed %{public}d", ret);
   7. }
   8. // 释放USB DDK
   9. OH_Usb_Release();
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/UsbDriverDemo/entry/src/main/cpp/hello.cpp#L434-L444)
7. 获取可识别的USB设备列表（独立步骤，可选）。

   驱动拉起后调用**OH\_Usb\_GetDevices**接口获取驱动配置信息中匹配vid（vid是设备厂商的vendor id，在驱动应用里面配置，表示驱动适配哪些设备，查询到的设备ID都需要通过vid进行过滤）的设备ID，以供后续应用开发使用。

   ```
   1. constexpr size_t maxUsbDeviceNum = 128;
   2. struct Usb_DeviceArray deviceArray;
   3. deviceArray.deviceIds = new uint64_t[maxUsbDeviceNum];
   4. // 获取设备列表
   5. int32_t ret = OH_Usb_GetDevices(&deviceArray);
   6. if (ret != USB_DDK_SUCCESS) {
   7. OH_LOG_ERROR(LOG_APP, "OH_Usb_GetDevices failed, ret=%{public}d", ret);
   8. }
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/UsbDriverDemo/entry/src/main/cpp/hello.cpp#L220-L229)
