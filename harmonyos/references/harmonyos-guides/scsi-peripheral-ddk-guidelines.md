---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scsi-peripheral-ddk-guidelines
title: 开发使用SCSI协议的设备驱动
breadcrumb: 指南 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > 扩展外设专项驱动开发 > 开发使用SCSI协议的设备驱动
category: harmonyos-guides
scraped_at: 2026-04-29T13:33:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4d21967f8c85d2beab5091731ade87790239ac2ef401fe8bcd7aad788d7c8073
---

## 简介

在企业级存储解决方案和工业应用场景中，对SCSI（Small Computer System Interface，小型计算机系统接口）设备的使用需求广泛存在，例如：磁盘阵列、磁带库以及特定类型的存储服务器等。当操作系统中缺乏针对这些设备的适配驱动时，会导致设备连接后无法被识别或正常使用。ScsiPeripheralDDK（SCSI Peripheral Driver Development Kit）是为开发者提供的专门用于开发SCSI设备驱动程序的套件，支持开发者基于用户态，在应用层进行SCSI设备驱动的开发。

ScsiPeripheralDDK支持SPC（SCSI Primary Commands）、SBC（SCSI Block Commands）和MMC（MultiMedia Commands）三个命令集中的七个常用命令（INQUIRY、READ CAPACITY、TEST UNIT READY、REQUEST SENSE、READ、WRITE和VERIFY），使得开发者可以使用相对熟悉的命令进行设备驱动开发。

### 基本概念

在进行ScsiPeripheralDDK开发前，开发者应了解以下基本概念：

* **SCSI**

  SCSI是一种用于计算机和外围设备如硬盘驱动器、磁带驱动器、光盘驱动器、扫描仪等之间通信的标准化协议集。
* **AMS**

  AMS（Ability Manager Service）是用于协调各Ability运行关系，以及对生命周期进行调度的系统服务。
* **BMS**

  BMS（Bundle Manager Service）在HarmonyOS上主要负责应用的安装、卸载和数据管理。
* **DDK**

  DDK（Driver Development Kit）是HarmonyOS基于扩展外设框架，为开发者提供的驱动应用开发的工具包，可针对SCSI非标外设，开发对应的驱动。
* **非标外设**

  非标外设（也称为自定义外设或专有外设）是指不遵循通用标准或专门为特定应用场景定制设计的外围设备。这类设备往往需要专门的软件支持或者特殊的接口来实现与主机系统的通信。
* **标准外设**

  标准外设指的是遵循行业广泛接受的标准规范设计的外围设备（USB键盘、鼠标）。此类设备通常具有统一的接口协议、物理尺寸和电气特性，使得其可以在不同的系统之间互换使用。
* **逻辑块**

  逻辑块（Logical Block）是一个基本的数据存储单位。它代表设备上的一块固定大小的数据区域，通常用于数据读写操作。逻辑块的大小可以是512字节、1024字节、2048字节等，具体大小取决于设备的配置和文件系统的设计。
* **CDB**

  CDB（Command Descriptor Block）即命令描述块，是 SCSI协议中用于发送命令的标准数据结构。CDB是一个固定长度的字节数组，包含了SCSI命令的操作码（Opcode）以及相关的参数，用于告诉设备执行什么操作（如读取、写入、查询等）。

### 实现原理

非标外设应用通过扩展外设管理服务获取SCSI设备的ID，通过RPC将ID和要操作的动作下发给SCSI驱动应用，SCSI驱动应用通过调用ScsiPeripheralDDK接口可获取SCSI设备基本信息，读写数据，DDK接口使用HDI服务将指令下发至内核驱动，内核驱动使用指令与设备通信。

**图1** ScsiPeripheralDDK调用原理

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/SkBFn98bROevndy_fbgWsA/zh-cn_image_0000002589244779.png?HW-CC-KV=V1&HW-CC-Date=20260429T053331Z&HW-CC-Expire=86400&HW-CC-Sign=4D94FDE874C4E55EE2D61DD4B191D7910CC85F5B470B994B51BA22C82C87F065)

### 约束与限制

* ScsiPeripheralDDK开放API支持标准SCSI类外设扩展驱动开发场景。
* ScsiPeripheralDDK开放API仅允许在DriverExtensionAbility生命周期内使用。
* 使用ScsiPeripheralDDK开放API需要在module.json5中声明对应的ACL权限：ohos.permission.ACCESS\_DDK\_SCSI\_PERIPHERAL。

## 环境搭建

请参考[环境准备](environmental-preparation.md)完成开发前的准备工作。

## 开发指导

### 接口说明

| 名称 | 描述 |
| --- | --- |
| int32\_t OH\_ScsiPeripheral\_Init(void) | 初始化ScsiPeripheralDDK。 |
| int32\_t OH\_ScsiPeripheral\_Release(void) | 释放ScsiPeripheralDDK。 |
| int32\_t OH\_ScsiPeripheral\_Open(uint64\_t deviceId, uint8\_t interfaceIndex, ScsiPeripheral\_Device \*\*dev) | 打开deviceId和interfaceIndex指定的SCSI设备。其中，deviceId可以通过USB设备的总线编号左移32位后、同其设备地址进行或运算得到，interfaceIndex为需要打开的USB接口的索引值。 |
| int32\_t OH\_ScsiPeripheral\_Close(ScsiPeripheral\_Device \*\*dev) | 关闭SCSI设备。 |
| int32\_t OH\_ScsiPeripheral\_TestUnitReady(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_TestUnitReadyRequest \*request, ScsiPeripheral\_Response \*response) | 检查逻辑单元是否已经准备好。 |
| int32\_t OH\_ScsiPeripheral\_Inquiry(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_InquiryRequest \*request, ScsiPeripheral\_InquiryInfo \*inquiryInfo, ScsiPeripheral\_Response \*response) | 查询SCSI设备的基本信息。 |
| int32\_t OH\_ScsiPeripheral\_ReadCapacity10(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_ReadCapacityRequest \*request, ScsiPeripheral\_CapacityInfo \*capacityInfo, ScsiPeripheral\_Response \*response) | 获取SCSI设备的容量信息。 |
| int32\_t OH\_ScsiPeripheral\_RequestSense(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_RequestSenseRequest \*request, ScsiPeripheral\_Response \*response) | 获取sense data（SCSI设备返回给主机的信息，用于报告设备的状态、错误信息以及诊断信息）。 |
| int32\_t OH\_ScsiPeripheral\_Read10(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_IORequest \*request, ScsiPeripheral\_Response \*response) | 从指定逻辑块读取数据。 |
| int32\_t OH\_ScsiPeripheral\_Write10(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_IORequest \*request, ScsiPeripheral\_Response \*response) | 写数据到设备的指定逻辑块。 |
| int32\_t OH\_ScsiPeripheral\_Verify10(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_VerifyRequest \*request, ScsiPeripheral\_Response \*response) | 校验指定逻辑块。 |
| int32\_t OH\_ScsiPeripheral\_SendRequestByCdb(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_Request \*request, ScsiPeripheral\_Response \*response) | 以CDB方式发送SCSI命令。 |
| int32\_t OH\_ScsiPeripheral\_CreateDeviceMemMap(ScsiPeripheral\_Device \*dev, size\_t size, ScsiPeripheral\_DeviceMemMap \*\*devMmap) | 创建缓冲区。 |
| int32\_t OH\_ScsiPeripheral\_DestroyDeviceMemMap(ScsiPeripheral\_DeviceMemMap \*devMmap) | 销毁缓冲区。 |
| int32\_t OH\_ScsiPeripheral\_ParseBasicSenseInfo(uint8\_t \*senseData, uint8\_t senseDataLen, ScsiPeripheral\_BasicSenseInfo \*senseInfo) | 解析基本的sense data，包括Information、Command specific information、Sense key specific字段。 |

详细的接口说明请参考[ScsiPeripheralDDK](../harmonyos-references/capi-scsiperipheralddk.md)。

### 开发步骤

以下步骤描述了如何使用ScsiPeripheralDDK开发非标SCSI外设的驱动：

**添加动态链接库**

CMakeLists.txt中添加以下lib。

```
1. libscsi.z.so
```

**头文件**

```
1. #include <scsi_peripheral/scsi_peripheral_api.h>
2. #include <scsi_peripheral/scsi_peripheral_types.h>
```

1. 初始化DDK。

   使用 **scsi\_peripheral\_api.h** 的 **OH\_ScsiPeripheral\_Init** 初始化ScsiPeripheralDDK。

   ```
   1. // 初始化SCSI Peripheral DDK
   2. int32_t ret = OH_ScsiPeripheral_Init();
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/ScsiPeripheralDemo/entry/src/main/cpp/hello.cpp#L111-L114)
2. 打开设备。

   初始化ScsiPeripheralDDK后，使用 **scsi\_peripheral\_api.h** 的 **OH\_ScsiPeripheral\_Open** 打开SCSI设备。

   ```
   1. ret = OH_ScsiPeripheral_Open(g_devHandle, interfaceIndex, &g_scsiPeripheralDevice);
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/ScsiPeripheralDemo/entry/src/main/cpp/hello.cpp#L125-L127)
3. 创建缓冲区（可选）。

   使用 **scsi\_peripheral\_api.h** 的 **OH\_ScsiPeripheral\_CreateDeviceMemMap** 创建内存缓冲区devMmap。

   ```
   1. ret = OH_ScsiPeripheral_CreateDeviceMemMap(g_scsiPeripheralDevice, DEVICE_MEM_MAP_SIZE, &g_scsiDeviceMemMap);
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/ScsiPeripheralDemo/entry/src/main/cpp/hello.cpp#L142-L144)
4. 检查逻辑单元是否已经准备好（可选）。

   使用 **scsi\_peripheral\_api.h** 的 **OH\_ScsiPeripheral\_TestUnitReady** 检查逻辑单元是否已经准备好。

   ```
   1. int32_t ret = OH_ScsiPeripheral_TestUnitReady(g_scsiPeripheralDevice, &request, &response);
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/ScsiPeripheralDemo/entry/src/main/cpp/hello.cpp#L414-L416)
5. 查询SCSI设备的基本信息（可选）。

   使用 **scsi\_peripheral\_api.h** 的 **OH\_ScsiPeripheral\_Inquiry** 获取SCSI设备的基本信息。

   ```
   1. int32_t ret = OH_ScsiPeripheral_Inquiry(g_scsiPeripheralDevice, &inquiryRequest, &inquiryInfo, &response);
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/ScsiPeripheralDemo/entry/src/main/cpp/hello.cpp#L226-L228)
6. 获取SCSI设备的容量信息（可选）。

   使用 **scsi\_peripheral\_api.h** 的 **OH\_ScsiPeripheral\_ReadCapacity10** 获取SCSI设备容量信息。

   ```
   1. ret = OH_ScsiPeripheral_ReadCapacity10(g_scsiPeripheralDevice, &readCapacityRequest, &capacityInfo, &response);
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/ScsiPeripheralDemo/entry/src/main/cpp/hello.cpp#L357-L359)
7. 获取sense data（可选）。

   使用 **scsi\_peripheral\_api.h** 的 **OH\_ScsiPeripheral\_RequestSense** 获取sense data。

   ```
   1. int32_t ret = OH_ScsiPeripheral_RequestSense(g_scsiPeripheralDevice, &senseRequest, &response);
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/ScsiPeripheralDemo/entry/src/main/cpp/hello.cpp#L499-L501)
8. 解析sense data（可选）。

   使用 **scsi\_peripheral\_api.h** 的 **OH\_ScsiPeripheral\_ParseBasicSenseInfo** 解析基本的sense data，包括Information、Command specific information、Sense key specific字段。

   ```
   1. int32_t ret = OH_ScsiPeripheral_ParseBasicSenseInfo(response.senseData, SCSIPERIPHERAL_MAX_SENSE_DATA_LEN,
   2. &senseInfo);
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/ScsiPeripheralDemo/entry/src/main/cpp/hello.cpp#L450-L453)
9. 读取数据（可选）。

   使用 **scsi\_peripheral\_api.h** 的 **OH\_ScsiPeripheral\_Read10** 读取指定逻辑块的数据。

   ```
   1. int32_t ret = OH_ScsiPeripheral_Read10(g_scsiPeripheralDevice, &request, &response);
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/ScsiPeripheralDemo/entry/src/main/cpp/hello.cpp#L643-L645)
10. 写入数据（可选）。

    使用 **scsi\_peripheral\_api.h** 的 **OH\_ScsiPeripheral\_Write10** 写数据到设备指定逻辑块。

    ```
    1. int32_t ret = OH_ScsiPeripheral_Write10(g_scsiPeripheralDevice, &request, &response);
    ```

    [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/ScsiPeripheralDemo/entry/src/main/cpp/hello.cpp#L722-L724)
11. 校验指定逻辑块（可选）。

    使用 **scsi\_peripheral\_api.h** 的 **OH\_ScsiPeripheral\_Verify10** 校验指定逻辑块。

    ```
    1. int32_t ret = OH_ScsiPeripheral_Verify10(g_scsiPeripheralDevice, &request, &response);
    ```

    [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/ScsiPeripheralDemo/entry/src/main/cpp/hello.cpp#L766-L768)
12. 以CDB方式发送SCSI命令（可选）。

    使用 **scsi\_peripheral\_api.h** 的 **OH\_ScsiPeripheral\_SendRequestByCdb** 发送SCSI命令。

    ```
    1. int32_t ret = OH_ScsiPeripheral_SendRequestByCdb(g_scsiPeripheralDevice, &request, &response);
    ```

    [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/ScsiPeripheralDemo/entry/src/main/cpp/hello.cpp#L900-L902)
13. 销毁缓冲区（可选）。

    在所有请求处理完毕，程序退出前，使用 **scsi\_peripheral\_api.h** 的 **OH\_ScsiPeripheral\_DestroyDeviceMemMap** 销毁缓冲区。

    ```
    1. ret = OH_ScsiPeripheral_DestroyDeviceMemMap(g_scsiDeviceMemMap);
    ```

    [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/ScsiPeripheralDemo/entry/src/main/cpp/hello.cpp#L947-L949)
14. 关闭设备。

    在销毁缓冲区后，使用 **scsi\_peripheral\_api.h** 的 **OH\_ScsiPeripheral\_Close** 关闭设备。

    ```
    1. ret = OH_ScsiPeripheral_Close(&g_scsiPeripheralDevice);
    ```

    [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/ScsiPeripheralDemo/entry/src/main/cpp/hello.cpp#L958-L960)
15. 释放DDK。

    在关闭SCSI设备后，使用 **scsi\_peripheral\_api.h** 的 **OH\_ScsiPeripheral\_Release** 释放ScsiPeripheralDDK。

    ```
    1. ret = OH_ScsiPeripheral_Release();
    ```

    [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/ScsiPeripheralDemo/entry/src/main/cpp/hello.cpp#L967-L969)

### 调测验证

驱动应用侧开发完成后，可在HarmonyOS设备上安装应用，测试步骤如下：

1. 在设备上点击驱动应用，应用在设备上被拉起。
2. 应用可以读取到SCSI设备的基础信息。
3. 选择对应的SCSI命令，输入参数，点击发送按钮，可以执行对应的SCSI命令。
4. 也可以通过输入方向、CDB数据及CDB长度，点击发送按钮，执行对应的SCSI命令。
