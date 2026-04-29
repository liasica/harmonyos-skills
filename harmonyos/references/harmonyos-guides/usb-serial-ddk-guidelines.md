---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/usb-serial-ddk-guidelines
title: 开发适用串口协议的设备驱动
breadcrumb: 指南 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > 扩展外设专项驱动开发 > 开发适用串口协议的设备驱动
category: harmonyos-guides
scraped_at: 2026-04-29T13:33:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:442a818e50a15ab9c71dfde4530048ddbe6908fdc123b72a6ce8fe0d824420d4
---

## 简介

在工业用途场景中和一些陈旧设备上，都有对非标串口设备的使用需求，例如：温湿度计、特殊身份读卡器等，当系统中没有适配该设备的驱动时，会导致设备接入后无法使用。USBSerialDDK（USB Serial Driver Development Kit）是为开发者提供的USB串口驱动程序开发套件，支持开发者基于用户态，在应用层开发USB串口设备驱动。USBSerialDDK提供了一系列主机侧访问设备的接口，包括主机侧打开和关闭接口、串口读写通信等。依赖这些驱动开发接口，该类三方生态外设可顺利接入HarmonyOS，满足生态安全加密场景应用需求。

### 基本概念

在进行USBSerialDDK开发前，开发者应了解以下基本概念：

* **USB 串口**

  USB 串口（USB-to-Serial）是指一种接口转换技术，它允许通过 USB（通用串行总线）接口实现与传统串行端口（如 RS-232、RS-485 等）之间的数据通信。这种技术通常通过专门的硬件适配器或特定的内置芯片来实现。
* **AMS**

  AMS（Ability Manager Service）用于协调各Ability运行关系、及对生命周期进行调度的系统服务。在驱动开发过程中用于拉起和关闭扩展驱动能力DriverExtensionAbility。
* **BMS**

  BMS（Bundle Manager Service）在HarmonyOS上主要负责应用的安装、卸载和数据管理。
* **DDK**

  DDK（Driver Development Kit）是HarmonyOS基于扩展外设框架，为开发者提供的驱动应用开发的工具包，可针对非标USB串口设备，开发对应的驱动。
* **非标外设**

  非标外设（也称为自定义外设或专有外设）是指不遵循通用标准或专门为特定应用场景定制设计的外围设备。这类设备往往需要专门的软件支持或者特殊的接口来实现与主机系统的通信。
* **标准外设**

  标准外设指的是遵循行业广泛接受的标准规范设计的外围设备（USB 键盘、鼠标）。这些设备通常具有统一的接口协议、物理尺寸和电气特性，使得其可以在不同的系统之间互换使用。

### 实现原理

非标外设应用通过扩展外设管理服务获取USB串口设备的ID，通过RPC将ID和要操作的动作下发给USB串口驱动应用，USB串口驱动应用通过调用USBSerialDDK接口可设置串口属性（波特率、数据位、校验位等），读取串口数据，DDK接口使用HDI服务将指令下发至内核驱动，内核驱动使用指令与设备通信。

**图1** USBSerialDDK调用原理

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/QgXRJxfjR9uKbnVzSaEnmA/zh-cn_image_0000002589244779.png?HW-CC-KV=V1&HW-CC-Date=20260429T053331Z&HW-CC-Expire=86400&HW-CC-Sign=9E6DD44B0E8CE7463A488C7782F5C9C2BAAE18AF4D53F93FB0AD418E493617B1)

### 约束与限制

* USBSerialDDK开放API支持USB串口接口非标外设扩展驱动开发场景。
* USBSerialDDK开放API使用范围内仅允许DriverExtensionAbility生命周期内使用。
* 使用USBSerialDDK开放API需要在module.json5中声明匹配的ACL权限，例如ohos.permission.ACCESS\_DDK\_USB\_SERIAL。

## 环境搭建

请参考[环境准备](environmental-preparation.md)完成开发前的准备工作。

## 开发指导

### 接口说明

| 名称 | 描述 |
| --- | --- |
| OH\_UsbSerial\_Init(void) | 初始化USBSerialDDK。 |
| OH\_UsbSerial\_Release(void) | 释放USBSerialDDK。 |
| OH\_UsbSerial\_Open(uint64\_t deviceId, uint8\_t interfaceIndex, UsbSerial\_Device \*\*dev) | 通过deviceId和interfaceIndex打开USB串口设备。请在设备使用完后调用OH\_UsbSerial\_Close()关闭设备，否则会造成内存泄漏。 |
| OH\_UsbSerial\_Close(UsbSerial\_Device \*\*dev) | 关闭USB串口设备，请在设备使用完后关闭设备，否则会造成内存泄漏。 |
| OH\_UsbSerial\_Read(UsbSerial\_Device \*dev, uint8\_t \*buff, uint32\_t bufferSize, uint32\_t \*bytesRead) | 从USB串口设备读取数据到缓冲区。 |
| OH\_UsbSerial\_Write(UsbSerial\_Device \*dev, uint8\_t \*buff, uint32\_t bufferSize, uint32\_t \*bytesWritten) | 将buff中的数据写入USB串口设备。 |
| OH\_UsbSerial\_SetBaudRate(UsbSerial\_Device \*dev, uint32\_t baudRate) | 设置USB串口设备的波特率。如果USB串口设备的参数为默认值（数据位为8，停止位为1，数据传输无校验），则只需要调用该接口设置波特率即可。 |
| OH\_UsbSerial\_SetParams(UsbSerial\_Device \*dev, UsbSerial\_Params \*params) | 设置USB串口设备的参数，包含波特率、数据传输位、停止位、校验设置。 |
| OH\_UsbSerial\_SetTimeout(UsbSerial\_Device \*dev, int timeout) | 设置读取USB串口设备上报数据的超时时间，默认时间为0。 |
| OH\_UsbSerial\_SetFlowControl(UsbSerial\_Device \*dev, UsbSerial\_FlowControl flowControl) | 设置流控参数。 |
| OH\_UsbSerial\_Flush(UsbSerial\_Device \*dev) | 写入完成后清空输入和输出缓冲区。 |
| OH\_UsbSerial\_FlushInput(UsbSerial\_Device \*dev) | 刷新输入缓冲区，缓冲区中的数据会被立刻清空。 |
| OH\_UsbSerial\_FlushOutput(UsbSerial\_Device \*dev) | 刷新输出缓冲区，缓冲区中的数据会被立刻清空。 |

详细的接口说明请参考[USBSerialDDK](../harmonyos-references/capi-serialddk.md)。

### 开发步骤

以下步骤描述了如何使用 **USBSerialDDK**开发USB串口驱动：

**添加动态链接库**

CMakeLists.txt中添加以下lib。

```
1. libusb_serial_ndk.z.so
```

**头文件**

```
1. #include <usb_serial/usb_serial_api.h>
2. #include <usb_serial/usb_serial_types.h>
```

1. 初始化DDK。

   使用 **usb\_serial\_api.h** 的 **OH\_UsbSerial\_Init** 初始化DDK。

   ```
   1. // 初始化USB Serial DDK
   2. OH_UsbSerial_Init();
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/UsbSerialDriverDemo/entry/src/main/cpp/hello.cpp#L201-L204)
2. 打开USB串口设备。

   使用 **usb\_serial\_api.h** 的 **OH\_UsbSerial\_Open** 打开设备。

   ```
   1. UsbSerial_Device *dev = NULL;
   2. uint64_t deviceId = 1;
   3. uint8_t interfaceIndex = 0;
   4. // 打开deviceId和interfaceIndex指定的USB串口设备
   5. OH_UsbSerial_Open(deviceId, interfaceIndex, &dev);
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/UsbSerialDriverDemo/entry/src/main/cpp/hello.cpp#L209-L215)
3. 设置USB串口设备的参数（可选）。

   使用 **usb\_serial\_api.h** 的 **OH\_UsbSerial\_SetParams** 接口设置串口参数，或者直接调用 **OH\_UsbSerial\_SetBaudRate** 设置波特率，使用 **OH\_UsbSerial\_SetTimeout** 设置读取数据的超时时间。

   ```
   1. UsbSerial_Params params;
   2. params.baudRate = NUM_BAUDRATE;
   3. params.nDataBits = NUM_EIGHT;
   4. params.nStopBits = 1;
   5. params.parity = 0;
   6. // 设置串口参数
   7. OH_UsbSerial_SetParams(dev, &params);

   9. // 设置波特率
   10. uint32_t baudRate = NUM_BAUDRATE;
   11. OH_UsbSerial_SetBaudRate(dev, baudRate);

   13. // 设置超时时间
   14. int timeout = 500;
   15. OH_UsbSerial_SetTimeout(dev, timeout);
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/UsbSerialDriverDemo/entry/src/main/cpp/hello.cpp#L221-L237)
4. 设置流控、清空缓冲区（可选）。

   使用 **usb\_serial\_api.h** 的 **OH\_UsbSerial\_SetFlowControl** 设置流控方式，使用 **OH\_UsbSerial\_Flush** 清空缓冲区，使用 **OH\_UsbSerial\_FlushInput** 清空输入缓冲区，使用 **OH\_UsbSerial\_FlushOutput** 清空输出缓冲区。

   ```
   1. // 设置软件流控
   2. OH_UsbSerial_SetFlowControl(dev, USB_SERIAL_SOFTWARE_FLOW_CONTROL);

   4. // 清空缓冲区
   5. OH_UsbSerial_Flush(dev);

   7. // 清空输入缓冲区
   8. OH_UsbSerial_FlushInput(dev);

   10. // 清空输出缓冲区
   11. OH_UsbSerial_FlushOutput(dev);
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/UsbSerialDriverDemo/entry/src/main/cpp/hello.cpp#L243-L255)
5. 向USB串口设备写入/读取数据（可选）。

   使用 **usb\_serial\_api.h** 的 **OH\_UsbSerial\_Write** 给设备发送数据，并使用 **OH\_UsbSerial\_Read** 读取设备发送过来的数据。

   ```
   1. uint32_t bytesWritten = 0;
   2. // 测试设备读取指令，具体指令根据设备协议而定
   3. uint8_t writeBuff[NUM_EIGHT] = {0x01, 0x03, 0x00, 0x00, 0x00, 0x01, 0x84, 0xA};
   4. // 发送数据
   5. OH_UsbSerial_Write(dev, writeBuff, sizeof(writeBuff), &bytesWritten);

   7. // 接收数据
   8. uint8_t readBuff[100];
   9. uint32_t bytesRead = 0;
   10. OH_UsbSerial_Read(dev, readBuff, sizeof(readBuff), &bytesRead);
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/UsbSerialDriverDemo/entry/src/main/cpp/hello.cpp#L260-L271)
6. 关闭USB串口设备。

   在所有请求处理完毕，程序退出前，使用 **usb\_serial\_api.h** 的 **OH\_UsbSerial\_Close** 关闭设备。

   ```
   1. // 关闭设备
   2. OH_UsbSerial_Close(&dev);
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/UsbSerialDriverDemo/entry/src/main/cpp/hello.cpp#L276-L279)
7. 释放DDK。

   在关闭USB串口设备后，使用 **usb\_serial\_api.h** 的 **OH\_UsbSerial\_Release** 释放DDK。

   ```
   1. // 释放USB Serial DDK
   2. OH_UsbSerial_Release();
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/UsbSerialDriverDemo/entry/src/main/cpp/hello.cpp#L284-L287)

### 调测验证

驱动应用侧开发完成后，可在HarmonyOS设备上安装应用，测试步骤如下：

1. 在设备上点击驱动应用，应用在设备上被拉起。
2. 点击波特率等设置按钮，可以设置串口属性。
3. 点击数据读取按钮，可以读取到串口设备数据。
