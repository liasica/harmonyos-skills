---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hid-ddk-guidelines
title: 开发适用HID协议的设备驱动
breadcrumb: 指南 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > 扩展外设专项驱动开发 > 开发适用HID协议的设备驱动
category: harmonyos-guides
scraped_at: 2026-04-29T13:33:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4de575de99a59627190b9a4299810626f4f319d755bcfb10cd568464e50a0fa6
---

## 简介

HidDdk（HID Driver Development Kit）是为开发者提供的HID设备驱动程序开发套件，支持开发者基于用户态，在应用层开发HID设备驱动。提供了一系列主机侧访问设备的接口，包括创建设备、向设备发送事件、销毁设备、打开关闭设备、读取写入报告、获取设备信息等。

凡是采用USB总线，通过HID协议传输数据的设备，或者通过扩展外设驱动创建虚拟设备，来实现与非标设备的信息交互都可以使用HidDdk开发设备驱动。

### 基本概念

在进行HidDdk开发前，开发者应了解以下基本概念：

* **HID**

  HID（Human Interface Device），中文意思是“人机接口设备”。它是一类用于实现人与计算机或其他电子设备交互的硬件设备。HID 设备的主要功能是将用户的输入（如按键、点击、移动等）转换为数据信号，并将这些信号发送给主机设备（如计算机、平板、游戏机等），从而实现用户对设备的控制和操作。
* **DDK**

  DDK（Driver Development Kit）是HarmonyOS基于扩展外设框架，为开发者提供的驱动应用开发的工具包，可针对非标USB串口设备，开发对应的驱动。

### 实现原理

非标外设应用通过扩展外设管理服务获取HID设备的ID，通过RPC将ID和要操作的动作下发给HID设备驱动应用，驱动应用通过调用HidDdk接口可创建、销毁HID设备，以及对HID设备发送事件，获取HID报文，解析报文等，DDK接口使用HDI服务将指令下发至内核驱动，内核驱动使用指令与设备通信。

**图1** HidDdk调用原理

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/ykNSUTyfQz2f8ljM7RENdQ/zh-cn_image_0000002589244779.png?HW-CC-KV=V1&HW-CC-Date=20260429T053331Z&HW-CC-Expire=86400&HW-CC-Sign=E687E1BDF4C844C0007A89D4855666BB3D6467437A86AF1195FC0499D7DE4C45)

## 约束与限制

* HidDdk开放API支持非标HID类外设扩展驱动开发场景。
* HidDdk开放API仅允许DriverExtensionAbility生命周期内使用。
* 使用HidDdk开放API需要在module.json5中声明匹配的ACL权限，例如ohos.permission.ACCESS\_DDK\_HID。

## 接口说明

| 名称 | 描述 |
| --- | --- |
| OH\_Hid\_CreateDevice(Hid\_Device \*hidDevice, Hid\_EventProperties \*hidEventProperties) | 创建HID设备。请在设备使用完后使用OH\_Hid\_DestroyDevice销毁设备。 |
| OH\_Hid\_EmitEvent(int32\_t deviceId, const Hid\_EmitItem items[], uint16\_t length) | 向指定deviceId的HID设备发送事件。 |
| OH\_Hid\_DestroyDevice(int32\_t deviceId) | 销毁指定deviceId的HID设备。 |
| int32\_t OH\_Hid\_Init(void) | 初始化HidDdk。 |
| int32\_t OH\_Hid\_Release(void) | 释放HidDdk。 |
| int32\_t OH\_Hid\_Open(uint64\_t deviceId, uint8\_t interfaceIndex, Hid\_DeviceHandle \*\*dev) | 打开deviceId和interfaceIndex指定的设备。 |
| int32\_t OH\_Hid\_Close(Hid\_DeviceHandle \*\*dev) | 关闭设备。 |
| int32\_t OH\_Hid\_Write(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t length, uint32\_t \*bytesWritten) | 向设备写入报告。 |
| int32\_t OH\_Hid\_ReadTimeout(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t buffSize, int timeout, uint32\_t \*bytesRead) | 在指定的超时时间内从设备读取报告。 |
| int32\_t OH\_Hid\_Read(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t buffSize, uint32\_t \*bytesRead) | 从设备读取报告，默认为阻塞模式（阻塞等待直到有数据可读取），可以调用OH\_Hid\_SetNonBlocking改变模式。 |
| int32\_t OH\_Hid\_SetNonBlocking(Hid\_DeviceHandle \*dev, int nonblock) | 设置设备读取模式为非阻塞。 |
| int32\_t OH\_Hid\_GetRawInfo(Hid\_DeviceHandle \*dev, Hid\_RawDevInfo \*rawDevInfo) | 获取设备原始信息。 |
| int32\_t OH\_Hid\_GetRawName(Hid\_DeviceHandle \*dev, char \*data, uint32\_t buffSize) | 获取设备原始名称。 |
| int32\_t OH\_Hid\_GetPhysicalAddress(Hid\_DeviceHandle \*dev, char \*data, uint32\_t buffSize) | 获取设备物理地址。 |
| int32\_t OH\_Hid\_GetRawUniqueId(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t buffSize) | 获取设备原始唯一标识符。 |
| int32\_t OH\_Hid\_SendReport(Hid\_DeviceHandle \*dev, Hid\_ReportType reportType, const uint8\_t \*data, uint32\_t length) | 向设备发送报告。 |
| int32\_t OH\_Hid\_GetReport(Hid\_DeviceHandle \*dev, Hid\_ReportType reportType, uint8\_t \*data, uint32\_t buffSize) | 获取设备报告。 |
| int32\_t OH\_Hid\_GetReportDescriptor(Hid\_DeviceHandle \*dev, uint8\_t \*buf, uint32\_t buffSize, uint32\_t \*bytesRead) | 获取设备报告描述符。 |

详细的接口说明请参考[HidDdk](../harmonyos-references/capi-hidddk.md)。

## 开发步骤

### HID基础驱动能力开发

以下步骤描述了如何使用 **HidDdk**开发HID设备驱动：

**添加动态链接库**

CMakeLists.txt中添加以下lib。

```
1. libhid.z.so
```

**头文件**

```
1. #include <hid/hid_ddk_api.h>
2. #include <hid/hid_ddk_types.h>
```

1. 创建设备。

   使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_CreateDevice** 接口创建HID设备，成功返回设备deviceId，失败返回[Hid\_DdkErrCode](../harmonyos-references/capi-hid-ddk-types-h.md#hid_ddkerrcode)。

   ```
   1. Hid_Device hidDevice = {
   2. .deviceName = deviceName.c_str(),
   3. .vendorId = 0x6006,
   4. .productId = 0x6008,
   5. .version = 1,
   6. .bustype = BUS_USB
   7. };
   8. std::vector<Hid_EventType> eventType = {HID_EV_KEY};
   9. Hid_EventTypeArray eventTypeArray = {.hidEventType = eventType.data(), .length = (uint16_t)eventType.size()};
   10. std::vector<Hid_KeyCode> keyCode = {
   11. HID_KEY_1,          HID_KEY_SPACE,       HID_KEY_BACKSPACE,   HID_KEY_ENTER,     HID_KEY_ESC, HID_KEY_SYSRQ,
   12. HID_KEY_LEFT_SHIFT, HID_KEY_RIGHT_SHIFT, HID_KEY_VOLUME_DOWN, HID_KEY_VOLUME_UP, HID_KEY_0,   HID_KEY_2,
   13. HID_KEY_3,          HID_KEY_4,           HID_KEY_5,           HID_KEY_6,         HID_KEY_7,   HID_KEY_8,
   14. HID_KEY_9,          HID_KEY_A,           HID_KEY_B,           HID_KEY_C,         HID_KEY_D,   HID_KEY_E,
   15. HID_KEY_F,          HID_KEY_G,           HID_KEY_H,           HID_KEY_I,         HID_KEY_J,   HID_KEY_K,
   16. HID_KEY_L,          HID_KEY_M,           HID_KEY_N,           HID_KEY_O,         HID_KEY_P,   HID_KEY_Q,
   17. HID_KEY_R,          HID_KEY_S,           HID_KEY_T,           HID_KEY_U,         HID_KEY_V,   HID_KEY_W,
   18. HID_KEY_X,          HID_KEY_Y,           HID_KEY_Z,           HID_KEY_DELETE};
   19. Hid_KeyCodeArray keyCodeArray = {.hidKeyCode = keyCode.data(), .length = (uint16_t)keyCode.size()};
   20. Hid_EventProperties hidEventProp = {.hidEventTypes = eventTypeArray, .hidKeys = keyCodeArray};
   21. int deviceId = OH_Hid_CreateDevice(&hidDevice, &hidEventProp);
   ```

   [inject\_thread.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/UsbDriverDemo/entry/src/main/cpp/inject_thread.cpp#L152-L174)
2. 向指定deviceId的HID设备发送事件。

   使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_EmitEvent** 向指定的deviceId的设备发送事件。

   ```
   1. // 向指定deviceId的设备发送事件，事件来源于物理外设，通过InjectEvent方法注入
   2. int32_t ret = OH_Hid_EmitEvent(item.first, item.second.data(), (uint16_t)item.second.size());
   3. if (ret != HID_DDK_SUCCESS) {
   4. OH_LOG_ERROR(LOG_APP, "OH_Hid_EmitEvent failed, deviceId:%{public}d", item.first);
   5. }
   ```

   [inject\_thread.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/UsbDriverDemo/entry/src/main/cpp/inject_thread.cpp#L66-L72)
3. 释放资源。

   在所有请求处理完毕，程序退出前，使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_DestroyDevice** 接口销毁HID设备。

   ```
   1. // 销毁HID设备
   2. int32_t res = OH_Hid_DestroyDevice(deviceId);
   ```

   [inject\_thread.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/UsbDriverDemo/entry/src/main/cpp/inject_thread.cpp#L127-L130)

### HID报文通信驱动能力开发

以下步骤描述了如何使用 **HidDdk** 开发HID报文通信驱动：

**添加动态链接库**

CMakeLists.txt中添加以下lib。

```
1. libhid.z.so
```

**头文件**

```
1. #include <hid/hid_ddk_api.h>
2. #include <hid/hid_ddk_types.h>
```

1. 初始化DDK。

   使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_Init** 初始化HidDdk。

   ```
   1. // 初始化HID DDK
   2. int32_t ret = OH_Hid_Init();
   3. if (ret != HID_DDK_SUCCESS) {
   4. OH_LOG_ERROR(LOG_APP, "OH_Hid_Init() return failed: %{public}d", ret);
   5. return ret;
   6. }
   ```

   [data\_parser.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/HidDriverDemo/entry/src/main/cpp/data_parser.cpp#L36-L43)
2. 打开设备。

   初始化HidDdk后，使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_Open** 打开HID设备。

   ```
   1. uint32_t bInterfaceNum1 = 0x00;
   2. // 打开deviceId和interfaceIndex1指定的HID设备（一般为/dev/hidraw0设备文件）
   3. ret = OH_Hid_Open(deviceID_, bInterfaceNum1, &hid_);
   4. if (ret != 0) {
   5. OH_LOG_ERROR(LOG_APP, "Failed to open hid device, interface number:%{public}u ret:%{public}d",
   6. bInterfaceNum1, ret);
   7. return ret;
   8. }
   9. uint32_t bInterfaceNum2 = 0x01;
   10. // 打开deviceId和interfaceIndex2指定的HID设备（一般为/dev/hidraw1设备文件）
   11. ret = OH_Hid_Open(deviceID_, bInterfaceNum2, &hid2_);
   12. if (ret != 0) {
   13. OH_LOG_ERROR(LOG_APP, "Failed to open hid device, interface number:%{public}u ret:%{public}d",
   14. bInterfaceNum2, ret);
   15. return ret;
   16. }
   ```

   [data\_parser.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/HidDriverDemo/entry/src/main/cpp/data_parser.cpp#L45-L62)
3. 向HID设备写入/发送报告（HID设备与主机之间交换的数据包）（可选）。

   * 当报告类型为HID\_OUTPUT\_REPORT（输出报告）时，支持如下两种写入/发送方式。
     + 使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_Write** 向HID设备写入一个输出报告。

       ```
       1. uint32_t bytesWritten;
       2. // 写入报告
       3. int32_t ret = OH_Hid_Write(DataParser::GetInstance().getHidObject(), dataBuff, sizeof(dataBuff), &bytesWritten);
       4. if (ret != HID_DDK_SUCCESS) {
       5. OH_LOG_ERROR(LOG_APP, "OH_Hid_Write failed. ret: %{public}u", ret);
       6. }
       ```

       [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/HidDriverDemo/entry/src/main/cpp/hello.cpp#L470-L477)
     + 使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_SendReport** 向HID设备发送一个输出报告。

       ```
       1. // 发送输出报告
       2. int32_t ret = OH_Hid_SendReport(DataParser::GetInstance().getHidObject(), HID_OUTPUT_REPORT, dataBuff,
       3. sizeof(dataBuff));
       4. if (ret != HID_DDK_SUCCESS) {
       5. OH_LOG_ERROR(LOG_APP, "OH_Hid_SendReport failed. ret: %{public}u", ret);
       6. }
       ```

       [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/HidDriverDemo/entry/src/main/cpp/hello.cpp#L408-L415)
     + 当报告类型为HID\_FEATURE\_REPORT（特性报告）时，使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_SendReport** 向HID设备发送一个特性报告。

       ```
       1. uint8_t dataBuff[NUM_EIGHT] = { 0x00 };
       2. string str(hexFormat);
       3. HexStringToUint8Array(str, dataBuff, sizeof(dataBuff));
       4. // 发送特性报告
       5. int32_t ret = OH_Hid_SendReport(DataParser::GetInstance().getHid2Object(), HID_FEATURE_REPORT, dataBuff,
       6. sizeof(dataBuff));
       7. if (ret != HID_DDK_SUCCESS) {
       8. OH_LOG_ERROR(LOG_APP, "OH_Hid_SendReport failed. ret: %{public}u", ret);
       9. }
       ```

       [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/HidDriverDemo/entry/src/main/cpp/hello.cpp#L570-L580)
4. 从HID设备读取报告（可选）。

   * 当报告类型为HID\_INPUT\_REPORT（输入报告）时，支持如下三种读取方式。
     + 使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_SetNonBlocking** 设置读取模式。

       ```
       1. // nonblock取值：1启用非阻塞，0禁用非阻塞
       2. ret = OH_Hid_SetNonBlocking(DataParser::GetInstance().getHidObject(), nonblockTag);
       3. if (ret != HID_DDK_SUCCESS) {
       4. OH_LOG_ERROR(LOG_APP, "OH_Hid_SetNonBlocking failed. ret: %{public}u", ret);
       5. return false;
       6. }
       ```

       [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/HidDriverDemo/entry/src/main/cpp/hello.cpp#L252-L259)
     + 使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_Read** 或者 **OH\_Hid\_ReadTimeout** 以非阻塞模式或者阻塞模式从HID设备读取一个输入报告。

       ```
       1. if (nonblock) {
       2. ret = OH_Hid_Read(DataParser::GetInstance().getHidObject(), dataBuff, sizeof(dataBuff), &bytesRead);
       3. } else {
       4. ret = OH_Hid_ReadTimeout(DataParser::GetInstance().getHidObject(), dataBuff, sizeof(dataBuff),
       5. CONST_TIMEOUT, &bytesRead);
       6. }
       ```

       [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/HidDriverDemo/entry/src/main/cpp/hello.cpp#L333-L340)
     + 使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_GetReport** 从HID设备读取一个输入报告。

       ```
       1. uint8_t dataBuff[NUM_NINE] = { 0x00 };
       2. // 读取输入报告
       3. int32_t ret = OH_Hid_GetReport(DataParser::GetInstance().getHidObject(), HID_INPUT_REPORT, dataBuff,
       4. sizeof(dataBuff));
       5. if (ret != HID_DDK_SUCCESS) {
       6. OH_LOG_ERROR(LOG_APP, "OH_Hid_GetReport failed. ret: %{public}u", ret);
       7. return nullptr;
       8. }
       ```

       [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/HidDriverDemo/entry/src/main/cpp/hello.cpp#L185-L194)
     + 当报告类型为HID\_FEATURE\_REPORT（特性报告）时，使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_GetReport** 从HID设备读取一个特性报告。

       ```
       1. uint8_t dataBuff[NUM_EIGHT] = { 0x00 };
       2. // 指定报告编号
       3. dataBuff[0] = 0x07;
       4. // 读取特性报告
       5. int32_t ret = OH_Hid_GetReport(DataParser::GetInstance().getHid2Object(), HID_FEATURE_REPORT, dataBuff,
       6. sizeof(dataBuff));
       7. if (ret != HID_DDK_SUCCESS) {
       8. OH_LOG_ERROR(LOG_APP, "OH_Hid_GetReport failed. ret: %{public}u", ret);
       9. return nullptr;
       10. }
       ```

       [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/HidDriverDemo/entry/src/main/cpp/hello.cpp#L489-L500)
5. 获取设备原始信息、原始名称、物理地址、原始唯一标识符（可选）。

   使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_GetRawInfo** 获取HID设备原始信息，使用 **OH\_Hid\_GetRawName** 获取HID设备原始名称，使用 **OH\_Hid\_GetPhysicalAddress** 获取HID设备物理地址，使用 **OH\_Hid\_GetRawUniqueId** 获取HID设备原始唯一标识符。这些信息可被上层应用引用，例如在界面中展示设备信息等。

   ```
   1. Hid_RawDevInfo rawDevInfo;
   2. int32_t ret = OH_Hid_GetRawInfo(DataParser::GetInstance().getHidObject(), &rawDevInfo);
   3. if (ret != HID_DDK_SUCCESS) {
   4. OH_LOG_ERROR(LOG_APP, "OH_Hid_GetRawInfo failed, ret:%{public}d", ret);
   5. return nullptr;
   6. }
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/HidDriverDemo/entry/src/main/cpp/hello.cpp#L80-L87)

   ```
   1. char dataBuff[DATA_BUFF_SIZE];
   2. int32_t ret = OH_Hid_GetRawName(DataParser::GetInstance().getHidObject(), dataBuff, sizeof(dataBuff));
   3. if (ret != HID_DDK_SUCCESS) {
   4. OH_LOG_ERROR(LOG_APP, "OH_Hid_GetRawName failed, ret:%{public}d", ret);
   5. return nullptr;
   6. }
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/HidDriverDemo/entry/src/main/cpp/hello.cpp#L103-L110)

   ```
   1. char dataBuff[DATA_BUFF_SIZE];
   2. int32_t ret = OH_Hid_GetPhysicalAddress(DataParser::GetInstance().getHidObject(), dataBuff, sizeof(dataBuff));
   3. if (ret != HID_DDK_SUCCESS) {
   4. OH_LOG_ERROR(LOG_APP, "OH_Hid_GetPhysicalAddress failed, ret:%{public}d", ret);
   5. return nullptr;
   6. }
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/HidDriverDemo/entry/src/main/cpp/hello.cpp#L121-L128)

   ```
   1. uint8_t dataBuff[NUM_SIXTY_FOUR];
   2. int32_t ret = OH_Hid_GetRawUniqueId(DataParser::GetInstance().getHidObject(), dataBuff, sizeof(dataBuff));
   3. if (ret != HID_DDK_SUCCESS) {
   4. OH_LOG_ERROR(LOG_APP, "OH_Hid_GetRawUniqueId failed, ret:%{public}d", ret);
   5. return nullptr;
   6. }
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/HidDriverDemo/entry/src/main/cpp/hello.cpp#L139-L146)
6. 获取报告描述符（可选）。

   使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_GetReportDescriptor** 获取HID设备报告描述符。

   ```
   1. uint8_t dataBuff[DATA_BUFF_SIZE1];
   2. uint32_t bytesRead;
   3. int32_t ret = OH_Hid_GetReportDescriptor(DataParser::GetInstance().getHidObject(), dataBuff, sizeof(dataBuff),
   4. &bytesRead);
   5. if (ret != HID_DDK_SUCCESS) {
   6. OH_LOG_ERROR(LOG_APP, "OH_Hid_GetReportDescriptor failed, ret:%{public}d", ret);
   7. return nullptr;
   8. }
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/HidDriverDemo/entry/src/main/cpp/hello.cpp#L591-L600)
7. 关闭设备。

   在所有请求处理完毕后，使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_Close** 关闭设备。

   ```
   1. Hid_DeviceHandle *hid = DataParser::GetInstance().getHidObject();
   2. int32_t ret1 = OH_Hid_Close(&hid);
   3. DataParser::GetInstance().UpdateHid(hid);
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/HidDriverDemo/entry/src/main/cpp/hello.cpp#L622-L626)
8. 释放DDK。

   在关闭HID设备后，使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_Release** 释放HidDdk。

   ```
   1. ret1 = OH_Hid_Release();
   2. if (ret1 != HID_DDK_SUCCESS) {
   3. OH_LOG_ERROR(LOG_APP, "OH_Hid_Init() return failed: %{public}d", ret1);
   4. }
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/DriverDevelopmentKit/HidDriverDemo/entry/src/main/cpp/hello.cpp#L635-L640)
