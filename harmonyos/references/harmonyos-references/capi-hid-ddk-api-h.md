---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hid-ddk-api-h
title: hid_ddk_api.h
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 头文件 > hid_ddk_api.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b34576a29310a0b30f913bfedbca9165ed2224e660d0b7e6d1f3704209a1d4f5
---

## 概述

声明主机侧访问输入设备的HID DDK（Driver Development Kit，驱动开发工具包）接口。该模块提供了创建、打开、读写HID设备的能力，支持设备管理和事件注入，支持两种使用模式：一是虚拟HID设备的创建与事件注入，适用于模拟键盘、鼠标、触摸屏输入等场景；二是真实HID设备的访问与通信，支持打开、读写设备报告以及获取设备信息，适用于与HID设备进行数据交互的场景。

**引用文件：** <hid/hid\_ddk\_api.h>

**库：** libhid.z.so

**系统能力：** SystemCapability.Driver.HID.Extension

**起始版本：** 11

**相关模块：** [HidDdk](capi-hidddk.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [int32\_t OH\_Hid\_CreateDevice(Hid\_Device \*hidDevice, Hid\_EventProperties \*hidEventProperties)](capi-hid-ddk-api-h.md#oh_hid_createdevice) | 创建设备。适用于需要模拟虚拟HID输入设备的场景，如模拟键盘、鼠标等输入设备进行自动化测试。必须与[OH\_Hid\_DestroyDevice](capi-hid-ddk-api-h.md#oh_hid_destroydevice)成对使用。 |
| [int32\_t OH\_Hid\_EmitEvent(int32\_t deviceId, const Hid\_EmitItem items[], uint16\_t length)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hid-ddk-api-h#oh_hid_emitevent) | 向指定设备发送事件列表，事件通过[OH\_Hid\_CreateDevice](capi-hid-ddk-api-h.md#oh_hid_createdevice)创建的虚拟设备注入到系统中，系统将其作为真实输入事件进行处理。适用于模拟用户输入事件的场景，如模拟按键、鼠标移动、点击等操作进行自动化测试或远程控制。 |
| [int32\_t OH\_Hid\_DestroyDevice(int32\_t deviceId)](capi-hid-ddk-api-h.md#oh_hid_destroydevice) | 销毁设备。必须与[OH\_Hid\_CreateDevice](capi-hid-ddk-api-h.md#oh_hid_createdevice)成对使用，只能销毁由当前调用者创建的设备。 |
| [int32\_t OH\_Hid\_Init(void)](capi-hid-ddk-api-h.md#oh_hid_init) | 初始化HID DDK。必须在使用其他所有HID DDK方法之前调用此方法。不再使用任何HID DDK功能时，必须调用[OH\_Hid\_Release](capi-hid-ddk-api-h.md#oh_hid_release)释放资源。 |
| [int32\_t OH\_Hid\_Release(void)](capi-hid-ddk-api-h.md#oh_hid_release) | 释放HID DDK。必须与[OH\_Hid\_Init](capi-hid-ddk-api-h.md#oh_hid_init)成对使用。 |
| [int32\_t OH\_Hid\_Open(uint64\_t deviceId, uint8\_t interfaceIndex, Hid\_DeviceHandle \*\*dev)](capi-hid-ddk-api-h.md#oh_hid_open) | 打开deviceId和interfaceIndex指定的设备。在使用完毕后调用[OH\_Hid\_Close](capi-hid-ddk-api-h.md#oh_hid_close)释放设备资源。 |
| [int32\_t OH\_Hid\_Close(Hid\_DeviceHandle \*\*dev)](capi-hid-ddk-api-h.md#oh_hid_close) | 关闭设备。必须与[OH\_Hid\_Open](capi-hid-ddk-api-h.md#oh_hid_open)成对使用，适用于不再需要与HID设备通信时，释放设备资源的场景。 |
| [int32\_t OH\_Hid\_Write(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t length, uint32\_t \*bytesWritten)](capi-hid-ddk-api-h.md#oh_hid_write) | 向设备写入HID报告。 |
| [int32\_t OH\_Hid\_ReadTimeout(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t bufSize, int timeout, uint32\_t \*bytesRead)](capi-hid-ddk-api-h.md#oh_hid_readtimeout) | 在指定的超时时间内从设备读取报告。 |
| [int32\_t OH\_Hid\_Read(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t bufSize, uint32\_t \*bytesRead)](capi-hid-ddk-api-h.md#oh_hid_read) | 从设备读取报告，默认为阻塞模式（阻塞等待直到有数据可读取），可以调用[OH\_Hid\_SetNonBlocking](capi-hid-ddk-api-h.md#oh_hid_setnonblocking)改变模式。 |
| [int32\_t OH\_Hid\_SetNonBlocking(Hid\_DeviceHandle \*dev, int nonBlock)](capi-hid-ddk-api-h.md#oh_hid_setnonblocking) | 设置设备读取模式为非阻塞。 |
| [int32\_t OH\_Hid\_GetRawInfo(Hid\_DeviceHandle \*dev, Hid\_RawDevInfo \*rawDevInfo)](capi-hid-ddk-api-h.md#oh_hid_getrawinfo) | 获取设备原始信息。 |
| [int32\_t OH\_Hid\_GetRawName(Hid\_DeviceHandle \*dev, char \*data, uint32\_t bufSize)](capi-hid-ddk-api-h.md#oh_hid_getrawname) | 获取设备原始名称。 |
| [int32\_t OH\_Hid\_GetPhysicalAddress(Hid\_DeviceHandle \*dev, char \*data, uint32\_t bufSize)](capi-hid-ddk-api-h.md#oh_hid_getphysicaladdress) | 获取设备物理地址。 |
| [int32\_t OH\_Hid\_GetRawUniqueId(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t bufSize)](capi-hid-ddk-api-h.md#oh_hid_getrawuniqueid) | 获取设备原始唯一标识符。 |
| [int32\_t OH\_Hid\_SendReport(Hid\_DeviceHandle \*dev, Hid\_ReportType reportType, const uint8\_t \*data, uint32\_t length)](capi-hid-ddk-api-h.md#oh_hid_sendreport) | 向设备发送指定类型的HID报告。 |
| [int32\_t OH\_Hid\_GetReport(Hid\_DeviceHandle \*dev, Hid\_ReportType reportType, uint8\_t \*data, uint32\_t bufSize)](capi-hid-ddk-api-h.md#oh_hid_getreport) | 从设备获取指定类型的HID报告。 |
| [int32\_t OH\_Hid\_GetReportDescriptor(Hid\_DeviceHandle \*dev, uint8\_t \*buf, uint32\_t bufSize, uint32\_t \*bytesRead)](capi-hid-ddk-api-h.md#oh_hid_getreportdescriptor) | 获取设备报告描述符。 |

## 函数说明

### OH\_Hid\_CreateDevice()

```c
int32_t OH_Hid_CreateDevice(Hid_Device *hidDevice, Hid_EventProperties *hidEventProperties)
```

**描述**

创建设备。适用于需要模拟虚拟HID输入设备的场景，如模拟键盘、鼠标等输入设备进行自动化测试。必须与[OH\_Hid\_DestroyDevice](capi-hid-ddk-api-h.md#oh_hid_destroydevice)成对使用。

**需要权限：** ohos.permission.ACCESS\_DDK\_HID

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Hid\_Device](capi-hidddk-hid-device.md) \*hidDevice | 创建设备需要的基本信息，包括设备名、厂商ID、产品ID等。 |
| [Hid\_EventProperties](capi-hidddk-hid-eventproperties.md) \*hidEventProperties | 创建的设备关注的事件，包括事件类型、按键事件属性、绝对坐标事件属性、相对坐标事件属性等。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | deviceID（一个非负整数）成功创建设备的ID。  [HID\_DDK\_NO\_PERM](capi-hid-ddk-types-h.md#hid_ddkerrcode) 权限校验失败。请确保应用已声明ohos.permission.ACCESS\_DDK\_HID权限。  [HID\_DDK\_INVALID\_OPERATION](capi-hid-ddk-types-h.md#hid_ddkerrcode) 连接HID DDK服务失败。可能原因：DDK服务未初始化。请调用OH\_Hid\_Init完成初始化。  [HID\_DDK\_INVALID\_PARAMETER](capi-hid-ddk-types-h.md#hid_ddkerrcode) 参数校验失败。可能的原因：1. 入参hidDevice为空指针；  2. 入参hidEventProperties为空指针；3. properties的长度超过7；4. hidEventTypes的长度超过5；  5. hidKeys的长度超过100；6. hidAbs的长度超过26；7.hidRelBits的长度超过13；  8. hidMiscellaneous的长度超过6。  [HID\_DDK\_FAILURE](capi-hid-ddk-types-h.md#hid_ddkerrcode) 设备数量达到最大值200。 |

### OH\_Hid\_EmitEvent()

```c
int32_t OH_Hid_EmitEvent(int32_t deviceId, const Hid_EmitItem items[], uint16_t length)
```

**描述**

向指定设备发送事件列表，事件通过[OH\_Hid\_CreateDevice](capi-hid-ddk-api-h.md#oh_hid_createdevice)创建的虚拟设备注入到系统中，系统将其作为真实输入事件进行处理。适用于模拟用户输入事件的场景，如模拟按键、鼠标移动、点击等操作进行自动化测试或远程控制。

**需要权限：** ohos.permission.ACCESS\_DDK\_HID

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t deviceId | 设备ID，必须是当前调用者通过[OH\_Hid\_CreateDevice](capi-hid-ddk-api-h.md#oh_hid_createdevice)创建的设备，取值为非负数。 |
| const [Hid\_EmitItem](capi-hidddk-hid-emititem.md) items[] | 发送的事件列表，事件包括类型（取值来源事件类型Hid\_EventType）、编码（取值来源同步事件编码Hid\_SynEvent、键值编码Hid\_KeyCode、绝对坐标编码Hid\_AbsAxes、相对坐标编码Hid\_RelAxes、其他类型的输入事件编码Hid\_MscEvent）、值（根据实际设备输入决定）。发送的事件将被注入到指定设备，模拟设备产生相应的输入行为。 |
| uint16\_t length | 发送事件列表长度（一次发送事件个数），取值范围为[1, 7]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [HID\_DDK\_SUCCESS](capi-hid-ddk-types-h.md#hid_ddkerrcode) 调用接口成功。  [HID\_DDK\_NO\_PERM](capi-hid-ddk-types-h.md#hid_ddkerrcode) 权限校验失败。请确保应用已声明ohos.permission.ACCESS\_DDK\_HID权限。  [HID\_DDK\_INVALID\_OPERATION](capi-hid-ddk-types-h.md#hid_ddkerrcode) 连接HID DDK服务失败或者调用方不是设备的创建者。请确保调用了OH\_Hid\_Init完成初始化，且调用方是设备的创建者。  [HID\_DDK\_INVALID\_PARAMETER](capi-hid-ddk-types-h.md#hid_ddkerrcode) 参数校验失败。可能的原因：1.设备ID小于0；2.入参length长度超过7；3.入参items为空指针。请检查参数有效性。  [HID\_DDK\_NULL\_PTR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 对应设备的注入为空。请确保使用OH\_Hid\_CreateDevice返回的有效设备ID，且设备未被销毁。 |

### OH\_Hid\_DestroyDevice()

```c
int32_t OH_Hid_DestroyDevice(int32_t deviceId)
```

**描述**

销毁设备。适用于不再需要使用虚拟HID设备时，释放系统资源的场景。必须与[OH\_Hid\_CreateDevice](capi-hid-ddk-api-h.md#oh_hid_createdevice)成对使用，只能销毁由当前调用者创建的设备。

**需要权限：** ohos.permission.ACCESS\_DDK\_HID

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t deviceId | 设备ID，必须是当前调用者创建的设备，取值为非负数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [HID\_DDK\_SUCCESS](capi-hid-ddk-types-h.md#hid_ddkerrcode) 调用接口成功。  [HID\_DDK\_NO\_PERM](capi-hid-ddk-types-h.md#hid_ddkerrcode) 权限校验失败。请确保应用已声明ohos.permission.ACCESS\_DDK\_HID权限。  [HID\_DDK\_INVALID\_OPERATION](capi-hid-ddk-types-h.md#hid_ddkerrcode) 连接HID DDK服务失败或者调用方不是设备的创建者。请确保调用了OH\_Hid\_Init完成初始化，且调用方是设备的创建者。  [HID\_DDK\_NULL\_PTR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 设备不存在。请确保使用OH\_Hid\_CreateDevice返回的有效设备ID，且设备未被销毁。 |

### OH\_Hid\_Init()

```c
int32_t OH_Hid_Init(void)
```

**描述**

初始化HID DDK。必须在使用其他所有HID DDK方法之前调用此方法。不再使用任何HID DDK功能时，必须调用[OH\_Hid\_Release](capi-hid-ddk-api-h.md#oh_hid_release)释放资源。

**需要权限：** ohos.permission.ACCESS\_DDK\_HID

**起始版本：** 18

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [HID\_DDK\_SUCCESS](capi-hid-ddk-types-h.md#hid_ddkerrcode) 操作成功。  [HID\_DDK\_NO\_PERM](capi-hid-ddk-types-h.md#hid_ddkerrcode) 权限校验失败。请确保应用已声明ohos.permission.ACCESS\_DDK\_HID权限。  [HID\_DDK\_INIT\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 初始化DDK失败。  [HID\_DDK\_SERVICE\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 与DDK服务通信失败。可能原因：服务内部错误。请检查当前操作和设备状态。 |

### OH\_Hid\_Release()

```c
int32_t OH_Hid_Release(void)
```

**描述**

释放HID DDK。必须与[OH\_Hid\_Init](capi-hid-ddk-api-h.md#oh_hid_init)成对使用。

**需要权限：** ohos.permission.ACCESS\_DDK\_HID

**起始版本：** 18

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [HID\_DDK\_SUCCESS](capi-hid-ddk-types-h.md#hid_ddkerrcode) 操作成功。  [HID\_DDK\_NO\_PERM](capi-hid-ddk-types-h.md#hid_ddkerrcode) 权限校验失败。请确保应用已声明ohos.permission.ACCESS\_DDK\_HID权限。  [HID\_DDK\_INIT\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) DDK未初始化，请确保已调用[OH\_Hid\_Init](capi-hid-ddk-api-h.md#oh_hid_init)完成初始化。  [HID\_DDK\_SERVICE\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 与DDK服务通信失败。可能原因：服务内部错误。请检查当前操作和设备状态。 |

### OH\_Hid\_Open()

```c
int32_t OH_Hid_Open(uint64_t deviceId, uint8_t interfaceIndex, Hid_DeviceHandle **dev)
```

**描述**

打开deviceId和interfaceIndex指定的设备。适用于需要与特定HID设备进行通信的场景，在使用完毕后调用[OH\_Hid\_Close](capi-hid-ddk-api-h.md#oh_hid_close)释放设备资源。

**需要权限：** ohos.permission.ACCESS\_DDK\_HID

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint64\_t deviceId | 操作设备的ID，可通过[OH\_Usb\_GetDevices](capi-usb-ddk-api-h.md#oh_usb_getdevices)查询获取。 |
| uint8\_t interfaceIndex | 接口索引，对应HID设备的接口。 |
| [Hid\_DeviceHandle](capi-hidddk-hid-devicehandle.md) \*\*dev | 设备操作句柄，输出参数。接口执行成功后会被赋值，表示打开的HID设备。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [HID\_DDK\_SUCCESS](capi-hid-ddk-types-h.md#hid_ddkerrcode) 操作成功。  [HID\_DDK\_NO\_PERM](capi-hid-ddk-types-h.md#hid_ddkerrcode) 权限校验失败。请确保应用已声明ohos.permission.ACCESS\_DDK\_HID权限。  [HID\_DDK\_INIT\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) DDK未初始化，请确保已调用[OH\_Hid\_Init](capi-hid-ddk-api-h.md#oh_hid_init)完成初始化。  [HID\_DDK\_SERVICE\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 与DDK服务通信失败。可能原因：服务内部错误。请检查当前操作和设备状态。  [HID\_DDK\_MEMORY\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) dev内存申请失败。  [HID\_DDK\_IO\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) I/O操作失败。可能原因：设备状态异常、数据传输错误等。请检查设备状态和参数。  [HID\_DDK\_INVALID\_PARAMETER](capi-hid-ddk-types-h.md#hid_ddkerrcode) dev为空或\*dev为空。  [HID\_DDK\_DEVICE\_NOT\_FOUND](capi-hid-ddk-types-h.md#hid_ddkerrcode) 根据deviceId和interfaceIndex找不到设备。 |

### OH\_Hid\_Close()

```c
int32_t OH_Hid_Close(Hid_DeviceHandle **dev)
```

**描述**

关闭设备。必须与[OH\_Hid\_Open](capi-hid-ddk-api-h.md#oh_hid_open)成对使用，适用于不再需要与HID设备通信时，释放设备资源的场景。

**需要权限：** ohos.permission.ACCESS\_DDK\_HID

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Hid\_DeviceHandle](capi-hidddk-hid-devicehandle.md) \*\*dev | 设备操作句柄，须通过[OH\_Hid\_Open](capi-hid-ddk-api-h.md#oh_hid_open)打开并获取，接口调用成功后会释放资源并置空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [HID\_DDK\_SUCCESS](capi-hid-ddk-types-h.md#hid_ddkerrcode) 操作成功。  [HID\_DDK\_NO\_PERM](capi-hid-ddk-types-h.md#hid_ddkerrcode) 权限校验失败。请确保应用已声明ohos.permission.ACCESS\_DDK\_HID权限。  [HID\_DDK\_INIT\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) DDK未初始化，请确保已调用[OH\_Hid\_Init](capi-hid-ddk-api-h.md#oh_hid_init)完成初始化。  [HID\_DDK\_SERVICE\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 与DDK服务通信失败。可能原因：服务内部错误。请检查当前操作和设备状态。  [HID\_DDK\_IO\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) I/O操作失败。可能原因：设备状态异常、数据传输错误等。请检查设备状态和参数。  [HID\_DDK\_INVALID\_PARAMETER](capi-hid-ddk-types-h.md#hid_ddkerrcode) dev为空或\*dev为空。 |

### OH\_Hid\_Write()

```c
int32_t OH_Hid_Write(Hid_DeviceHandle *dev, uint8_t *data, uint32_t length, uint32_t *bytesWritten)
```

**描述**

向设备写入HID报告。

**需要权限：** ohos.permission.ACCESS\_DDK\_HID

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Hid\_DeviceHandle](capi-hidddk-hid-devicehandle.md) \*dev | 设备操作句柄，使用前须通过[OH\_Hid\_Open](capi-hid-ddk-api-h.md#oh_hid_open)打开并获取。 |
| uint8\_t \*data | 待写入的数据。 |
| uint32\_t length | 写入数据的字节长度，大于0且最大不超过[HID\_MAX\_REPORT\_BUFFER\_SIZE](capi-hid-ddk-types-h.md#宏定义)，否则无法通过参数校验。 |
| uint32\_t \*bytesWritten | 实际写入的数据字节数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [HID\_DDK\_SUCCESS](capi-hid-ddk-types-h.md#hid_ddkerrcode) 操作成功。  [HID\_DDK\_NO\_PERM](capi-hid-ddk-types-h.md#hid_ddkerrcode) 权限校验失败。请确保应用已声明ohos.permission.ACCESS\_DDK\_HID权限。  [HID\_DDK\_INVALID\_PARAMETER](capi-hid-ddk-types-h.md#hid_ddkerrcode) 参数校验失败。可能原因：1. dev为空；  2. data为空；3. length为0；4. length超过[HID\_MAX\_REPORT\_BUFFER\_SIZE](capi-hid-ddk-types-h.md#宏定义)；  5. bytesWritten为空。  [HID\_DDK\_INIT\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) DDK未初始化，请确保已调用[OH\_Hid\_Init](capi-hid-ddk-api-h.md#oh_hid_init)完成初始化。  [HID\_DDK\_SERVICE\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 与DDK服务通信失败。可能原因：服务内部错误。请检查当前操作和设备状态。  [HID\_DDK\_IO\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) I/O操作失败。可能原因：设备状态异常、数据传输错误等。请检查设备状态和参数。 |

### OH\_Hid\_ReadTimeout()

```c
int32_t OH_Hid_ReadTimeout(Hid_DeviceHandle *dev, uint8_t *data, uint32_t bufSize, int timeout, uint32_t *bytesRead)
```

**描述**

在指定的超时时间内从设备读取报告。

**需要权限：** ohos.permission.ACCESS\_DDK\_HID

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Hid\_DeviceHandle](capi-hidddk-hid-devicehandle.md) \*dev | 设备操作句柄，使用前须通过[OH\_Hid\_Open](capi-hid-ddk-api-h.md#oh_hid_open)打开并获取。 |
| uint8\_t \*data | 存放读取数据的缓冲区。 |
| uint32\_t bufSize | 存放读取数据的缓冲区大小，大于0且最大不超过[HID\_MAX\_REPORT\_BUFFER\_SIZE](capi-hid-ddk-types-h.md#宏定义)，否则无法通过参数校验。 |
| int timeout | 超时时间（毫秒），取值说明：大于0时，表示阻塞等待的毫秒数；等于0时表示立即返回；设置为-1时表示阻塞等待直至读出数据，不会返回超时。 |
| uint32\_t \*bytesRead | 读取的字节数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [HID\_DDK\_SUCCESS](capi-hid-ddk-types-h.md#hid_ddkerrcode) 操作成功。  [HID\_DDK\_NO\_PERM](capi-hid-ddk-types-h.md#hid_ddkerrcode) 权限校验失败。请确保应用已声明ohos.permission.ACCESS\_DDK\_HID权限。  [HID\_DDK\_INVALID\_PARAMETER](capi-hid-ddk-types-h.md#hid_ddkerrcode) 参数校验失败。可能原因：1. dev为空；  2. data为空；3. bufSize为0；4. bufSize超过[HID\_MAX\_REPORT\_BUFFER\_SIZE](capi-hid-ddk-types-h.md#宏定义)；  5. bytesRead为空。  [HID\_DDK\_INIT\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) DDK未初始化，请确保已调用[OH\_Hid\_Init](capi-hid-ddk-api-h.md#oh_hid_init)完成初始化。  [HID\_DDK\_SERVICE\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 与DDK服务通信失败。可能原因：服务内部错误。请检查当前操作和设备状态。  [HID\_DDK\_MEMORY\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 内存数据拷贝失败。  [HID\_DDK\_IO\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) I/O操作失败。可能原因：设备状态异常、数据传输错误等。请检查设备状态和参数。  [HID\_DDK\_TIMEOUT](capi-hid-ddk-types-h.md#hid_ddkerrcode) 读取超时。 |

### OH\_Hid\_Read()

```c
int32_t OH_Hid_Read(Hid_DeviceHandle *dev, uint8_t *data, uint32_t bufSize, uint32_t *bytesRead)
```

**描述**

从设备读取报告，默认为阻塞模式（阻塞等待直到有数据可读取），可以调用[OH\_Hid\_SetNonBlocking](capi-hid-ddk-api-h.md#oh_hid_setnonblocking)改变模式。

**需要权限：** ohos.permission.ACCESS\_DDK\_HID

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Hid\_DeviceHandle](capi-hidddk-hid-devicehandle.md) \*dev | 设备操作句柄，使用前须通过[OH\_Hid\_Open](capi-hid-ddk-api-h.md#oh_hid_open)打开并获取。 |
| uint8\_t \*data | 存放读取数据的缓冲区。 |
| uint32\_t bufSize | 存放读取数据的缓冲区大小，大于0且最大不超过[HID\_MAX\_REPORT\_BUFFER\_SIZE](capi-hid-ddk-types-h.md#宏定义)，否则无法通过参数校验。 |
| uint32\_t \*bytesRead | 读取的字节数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [HID\_DDK\_SUCCESS](capi-hid-ddk-types-h.md#hid_ddkerrcode) 操作成功。  [HID\_DDK\_NO\_PERM](capi-hid-ddk-types-h.md#hid_ddkerrcode) 权限校验失败。请确保应用已声明ohos.permission.ACCESS\_DDK\_HID权限。  [HID\_DDK\_INVALID\_PARAMETER](capi-hid-ddk-types-h.md#hid_ddkerrcode) 参数校验失败。可能原因：1. dev为空；  2. data为空；3. bufSize为0；4. bufSize超过[HID\_MAX\_REPORT\_BUFFER\_SIZE](capi-hid-ddk-types-h.md#宏定义)；  5. bytesRead为空。  [HID\_DDK\_INIT\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) DDK未初始化，请确保已调用[OH\_Hid\_Init](capi-hid-ddk-api-h.md#oh_hid_init)完成初始化。  [HID\_DDK\_SERVICE\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 与DDK服务通信失败。可能原因：服务内部错误。请检查当前操作和设备状态。  [HID\_DDK\_MEMORY\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 内存数据拷贝失败。  [HID\_DDK\_IO\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) I/O操作失败。可能原因：设备状态异常、数据传输错误等。请检查设备状态和参数。  [HID\_DDK\_TIMEOUT](capi-hid-ddk-types-h.md#hid_ddkerrcode) 读取超时。 |

### OH\_Hid\_SetNonBlocking()

```c
int32_t OH_Hid_SetNonBlocking(Hid_DeviceHandle *dev, int nonBlock)
```

**描述**

设置设备读取模式为非阻塞。

**需要权限：** ohos.permission.ACCESS\_DDK\_HID

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Hid\_DeviceHandle](capi-hidddk-hid-devicehandle.md) \*dev | 设备操作句柄，使用前须通过[OH\_Hid\_Open](capi-hid-ddk-api-h.md#oh_hid_open)打开并获取。 |
| int nonBlock | 是否启用非阻塞模式读取数据。1：启用非阻塞模式，调用[OH\_Hid\_Read](capi-hid-ddk-api-h.md#oh_hid_read)接口时，如果设备有可读的数据，读取并返回[HID\_DDK\_SUCCESS](capi-hid-ddk-types-h.md#hid_ddkerrcode)，  如果设备没有数据可读，则返回[HID\_DDK\_TIMEOUT](capi-hid-ddk-types-h.md#hid_ddkerrcode)。0：禁用非阻塞模式，启用阻塞模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [HID\_DDK\_SUCCESS](capi-hid-ddk-types-h.md#hid_ddkerrcode) 操作成功。  [HID\_DDK\_NO\_PERM](capi-hid-ddk-types-h.md#hid_ddkerrcode) 权限校验失败。请确保应用已声明ohos.permission.ACCESS\_DDK\_HID权限。  [HID\_DDK\_INIT\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) DDK未初始化，请确保已调用[OH\_Hid\_Init](capi-hid-ddk-api-h.md#oh_hid_init)完成初始化。  [HID\_DDK\_INVALID\_PARAMETER](capi-hid-ddk-types-h.md#hid_ddkerrcode) 参数校验失败。可能原因：1. dev为空；  2. nonBlock不是1或0。  [HID\_DDK\_SERVICE\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 与DDK服务通信失败。可能原因：服务内部错误。请检查当前操作和设备状态。 |

### OH\_Hid\_GetRawInfo()

```c
int32_t OH_Hid_GetRawInfo(Hid_DeviceHandle *dev, Hid_RawDevInfo *rawDevInfo)
```

**描述**

获取设备原始信息。

**需要权限：** ohos.permission.ACCESS\_DDK\_HID

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Hid\_DeviceHandle](capi-hidddk-hid-devicehandle.md) \*dev | 设备操作句柄，使用前须通过[OH\_Hid\_Open](capi-hid-ddk-api-h.md#oh_hid_open)打开并获取。 |
| [Hid\_RawDevInfo](capi-hidddk-hid-rawdevinfo.md) \*rawDevInfo | 设备原始信息，包含厂商ID、产品ID和总线类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [HID\_DDK\_SUCCESS](capi-hid-ddk-types-h.md#hid_ddkerrcode) 操作成功。  [HID\_DDK\_NO\_PERM](capi-hid-ddk-types-h.md#hid_ddkerrcode) 权限校验失败。请确保应用已声明ohos.permission.ACCESS\_DDK\_HID权限。  [HID\_DDK\_INVALID\_PARAMETER](capi-hid-ddk-types-h.md#hid_ddkerrcode) 参数校验失败。可能原因：1. dev为空；  2. rawDevInfo为空。  [HID\_DDK\_INIT\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) DDK未初始化，请确保已调用[OH\_Hid\_Init](capi-hid-ddk-api-h.md#oh_hid_init)完成初始化。  [HID\_DDK\_SERVICE\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 与DDK服务通信失败。可能原因：服务内部错误。请检查当前操作和设备状态。  [HID\_DDK\_IO\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) I/O操作失败。可能原因：设备状态异常、数据传输错误等。请检查设备状态和参数。  [HID\_DDK\_INVALID\_OPERATION](capi-hid-ddk-types-h.md#hid_ddkerrcode) 不支持此操作。 |

### OH\_Hid\_GetRawName()

```c
int32_t OH_Hid_GetRawName(Hid_DeviceHandle *dev, char *data, uint32_t bufSize)
```

**描述**

获取设备原始名称。

**需要权限：** ohos.permission.ACCESS\_DDK\_HID

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Hid\_DeviceHandle](capi-hidddk-hid-devicehandle.md) \*dev | 设备操作句柄，使用前须通过[OH\_Hid\_Open](capi-hid-ddk-api-h.md#oh_hid_open)打开并获取。 |
| char \*data | 存放读取数据的缓冲区。 |
| uint32\_t bufSize | 存放读取数据的缓冲区大小，大于0且最大不超过[HID\_MAX\_REPORT\_BUFFER\_SIZE](capi-hid-ddk-types-h.md#宏定义)，否则无法通过参数校验。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [HID\_DDK\_SUCCESS](capi-hid-ddk-types-h.md#hid_ddkerrcode) 操作成功。  [HID\_DDK\_NO\_PERM](capi-hid-ddk-types-h.md#hid_ddkerrcode) 权限校验失败。请确保应用已声明ohos.permission.ACCESS\_DDK\_HID权限。  [HID\_DDK\_INVALID\_PARAMETER](capi-hid-ddk-types-h.md#hid_ddkerrcode) 参数校验失败。可能原因：1. dev为空；  2. data为空；3. bufSize为0；4. bufSize超过[HID\_MAX\_REPORT\_BUFFER\_SIZE](capi-hid-ddk-types-h.md#宏定义)。  [HID\_DDK\_INIT\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) DDK未初始化，请确保已调用[OH\_Hid\_Init](capi-hid-ddk-api-h.md#oh_hid_init)完成初始化。  [HID\_DDK\_SERVICE\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 与DDK服务通信失败。可能原因：服务内部错误。请检查当前操作和设备状态。  [HID\_DDK\_MEMORY\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 内存数据拷贝失败。  [HID\_DDK\_IO\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) I/O操作失败。可能原因：设备状态异常、数据传输错误等。请检查设备状态和参数。  [HID\_DDK\_INVALID\_OPERATION](capi-hid-ddk-types-h.md#hid_ddkerrcode) 不支持此操作。 |

### OH\_Hid\_GetPhysicalAddress()

```c
int32_t OH_Hid_GetPhysicalAddress(Hid_DeviceHandle *dev, char *data, uint32_t bufSize)
```

**描述**

获取设备物理地址。

**需要权限：** ohos.permission.ACCESS\_DDK\_HID

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Hid\_DeviceHandle](capi-hidddk-hid-devicehandle.md) \*dev | 设备操作句柄，使用前须通过[OH\_Hid\_Open](capi-hid-ddk-api-h.md#oh_hid_open)打开并获取。 |
| char \*data | 存放读取数据的缓冲区。 |
| uint32\_t bufSize | 存放读取数据的缓冲区大小，大于0且最大不超过[HID\_MAX\_REPORT\_BUFFER\_SIZE](capi-hid-ddk-types-h.md#宏定义)，否则无法通过参数校验。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [HID\_DDK\_SUCCESS](capi-hid-ddk-types-h.md#hid_ddkerrcode) 操作成功。  [HID\_DDK\_NO\_PERM](capi-hid-ddk-types-h.md#hid_ddkerrcode) 权限校验失败。请确保应用已声明ohos.permission.ACCESS\_DDK\_HID权限。  [HID\_DDK\_INVALID\_PARAMETER](capi-hid-ddk-types-h.md#hid_ddkerrcode) 参数校验失败。可能原因：1. dev为空；  2. data为空；3. bufSize为0；4. bufSize超过[HID\_MAX\_REPORT\_BUFFER\_SIZE](capi-hid-ddk-types-h.md#宏定义)。  [HID\_DDK\_INIT\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) DDK未初始化，请确保已调用[OH\_Hid\_Init](capi-hid-ddk-api-h.md#oh_hid_init)完成初始化。  [HID\_DDK\_SERVICE\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 与DDK服务通信失败。可能原因：服务内部错误。请检查当前操作和设备状态。  [HID\_DDK\_MEMORY\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 内存数据拷贝失败。  [HID\_DDK\_IO\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) I/O操作失败。可能原因：设备状态异常、数据传输错误等。请检查设备状态和参数。  [HID\_DDK\_INVALID\_OPERATION](capi-hid-ddk-types-h.md#hid_ddkerrcode) 不支持此操作。 |

### OH\_Hid\_GetRawUniqueId()

```c
int32_t OH_Hid_GetRawUniqueId(Hid_DeviceHandle *dev, uint8_t *data, uint32_t bufSize)
```

**描述**

获取设备原始唯一标识符。

**需要权限：** ohos.permission.ACCESS\_DDK\_HID

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Hid\_DeviceHandle](capi-hidddk-hid-devicehandle.md) \*dev | 设备操作句柄，使用前须通过[OH\_Hid\_Open](capi-hid-ddk-api-h.md#oh_hid_open)打开并获取。 |
| uint8\_t \*data | 存放读取数据的缓冲区。 |
| uint32\_t bufSize | 存放读取数据的缓冲区大小，大于0且最大不超过[HID\_MAX\_REPORT\_BUFFER\_SIZE](capi-hid-ddk-types-h.md#宏定义)，否则无法通过参数校验。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [HID\_DDK\_SUCCESS](capi-hid-ddk-types-h.md#hid_ddkerrcode) 操作成功。  [HID\_DDK\_NO\_PERM](capi-hid-ddk-types-h.md#hid_ddkerrcode) 权限校验失败。请确保应用已声明ohos.permission.ACCESS\_DDK\_HID权限。  [HID\_DDK\_INVALID\_PARAMETER](capi-hid-ddk-types-h.md#hid_ddkerrcode) 参数校验失败。可能原因：1. dev为空；  2. data为空；3. bufSize为0；4. bufSize超过[HID\_MAX\_REPORT\_BUFFER\_SIZE](capi-hid-ddk-types-h.md#宏定义)。  [HID\_DDK\_INIT\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) DDK未初始化，请确保已调用[OH\_Hid\_Init](capi-hid-ddk-api-h.md#oh_hid_init)完成初始化。  [HID\_DDK\_SERVICE\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 与DDK服务通信失败。可能原因：服务内部错误。请检查当前操作和设备状态。  [HID\_DDK\_MEMORY\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 内存数据拷贝失败。  [HID\_DDK\_IO\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) I/O操作失败。可能原因：设备状态异常、数据传输错误等。请检查设备状态和参数。  [HID\_DDK\_INVALID\_OPERATION](capi-hid-ddk-types-h.md#hid_ddkerrcode) 不支持此操作。 |

### OH\_Hid\_SendReport()

```c
int32_t OH_Hid_SendReport(Hid_DeviceHandle *dev, Hid_ReportType reportType, const uint8_t *data, uint32_t length)
```

**描述**

向设备发送指定类型的HID报告。

**需要权限：** ohos.permission.ACCESS\_DDK\_HID

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Hid\_DeviceHandle](capi-hidddk-hid-devicehandle.md) \*dev | 设备操作句柄，使用前须通过[OH\_Hid\_Open](capi-hid-ddk-api-h.md#oh_hid_open)打开并获取。 |
| [Hid\_ReportType](capi-hid-ddk-types-h.md#hid_reporttype) reportType | 报告类型，可指定为输入报告、输出报告或特性报告。 |
| const uint8\_t \*data | 待发送的数据。 |
| uint32\_t length | 发送数据的字节长度，大于0且最大不超过 [HID\_MAX\_REPORT\_BUFFER\_SIZE](capi-hid-ddk-types-h.md#宏定义)，否则无法通过参数校验。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [HID\_DDK\_SUCCESS](capi-hid-ddk-types-h.md#hid_ddkerrcode) 操作成功。  [HID\_DDK\_NO\_PERM](capi-hid-ddk-types-h.md#hid_ddkerrcode) 权限校验失败。请确保应用已声明ohos.permission.ACCESS\_DDK\_HID权限。  [HID\_DDK\_INVALID\_PARAMETER](capi-hid-ddk-types-h.md#hid_ddkerrcode) 参数校验失败。可能原因：1. dev为空；  2. data为空；3. length为0；4. length超过[HID\_MAX\_REPORT\_BUFFER\_SIZE](capi-hid-ddk-types-h.md#宏定义)。  [HID\_DDK\_INIT\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) DDK未初始化，请确保已调用[OH\_Hid\_Init](capi-hid-ddk-api-h.md#oh_hid_init)完成初始化。  [HID\_DDK\_SERVICE\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 与DDK服务通信失败。可能原因：服务内部错误。请检查当前操作和设备状态。  [HID\_DDK\_IO\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) I/O操作失败。可能原因：设备状态异常、数据传输错误等。请检查设备状态和参数。  [HID\_DDK\_INVALID\_OPERATION](capi-hid-ddk-types-h.md#hid_ddkerrcode) 不支持此操作。 |

### OH\_Hid\_GetReport()

```c
int32_t OH_Hid_GetReport(Hid_DeviceHandle *dev, Hid_ReportType reportType, uint8_t *data, uint32_t bufSize)
```

**描述**

从设备获取指定类型的HID报告。

**需要权限：** ohos.permission.ACCESS\_DDK\_HID

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Hid\_DeviceHandle](capi-hidddk-hid-devicehandle.md) \*dev | 设备操作句柄，使用前须通过[OH\_Hid\_Open](capi-hid-ddk-api-h.md#oh_hid_open)打开并获取。 |
| [Hid\_ReportType](capi-hid-ddk-types-h.md#hid_reporttype) reportType | 报告类型。 |
| uint8\_t \*data | 存放读取数据的缓冲区。 |
| uint32\_t bufSize | 存放读取数据的缓冲区大小，大于0且最大不超过[HID\_MAX\_REPORT\_BUFFER\_SIZE](capi-hid-ddk-types-h.md#宏定义)，否则无法通过参数校验。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [HID\_DDK\_SUCCESS](capi-hid-ddk-types-h.md#hid_ddkerrcode) 操作成功。  [HID\_DDK\_NO\_PERM](capi-hid-ddk-types-h.md#hid_ddkerrcode) 权限校验失败。请确保应用已声明ohos.permission.ACCESS\_DDK\_HID权限。  [HID\_DDK\_INVALID\_PARAMETER](capi-hid-ddk-types-h.md#hid_ddkerrcode) 参数校验失败。可能原因：1. dev为空；  2. data为空；3. bufSize为0；4. bufSize超过[HID\_MAX\_REPORT\_BUFFER\_SIZE](capi-hid-ddk-types-h.md#宏定义)。  [HID\_DDK\_INIT\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) DDK未初始化，请确保已调用[OH\_Hid\_Init](capi-hid-ddk-api-h.md#oh_hid_init)完成初始化。  [HID\_DDK\_SERVICE\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 与DDK服务通信失败。可能原因：服务内部错误。请检查当前操作和设备状态。  [HID\_DDK\_MEMORY\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 内存数据拷贝失败。  [HID\_DDK\_IO\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) I/O操作失败。可能原因：设备状态异常、数据传输错误等。请检查设备状态和参数。  [HID\_DDK\_INVALID\_OPERATION](capi-hid-ddk-types-h.md#hid_ddkerrcode) 不支持此操作。 |

### OH\_Hid\_GetReportDescriptor()

```c
int32_t OH_Hid_GetReportDescriptor(Hid_DeviceHandle *dev, uint8_t *buf, uint32_t bufSize, uint32_t *bytesRead)
```

**描述**

获取设备报告描述符。

**需要权限：** ohos.permission.ACCESS\_DDK\_HID

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Hid\_DeviceHandle](capi-hidddk-hid-devicehandle.md) \*dev | 设备操作句柄，使用前须通过[OH\_Hid\_Open](capi-hid-ddk-api-h.md#oh_hid_open)打开并获取。 |
| uint8\_t \*buf | 存放描述符的缓冲区。 |
| uint32\_t bufSize | 缓冲区的字节大小，大于0且最大不超过[HID\_MAX\_REPORT\_BUFFER\_SIZE](capi-hid-ddk-types-h.md#宏定义)，否则无法通过参数校验。 |
| uint32\_t \*bytesRead | 读取的字节数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [HID\_DDK\_SUCCESS](capi-hid-ddk-types-h.md#hid_ddkerrcode) 操作成功。  [HID\_DDK\_NO\_PERM](capi-hid-ddk-types-h.md#hid_ddkerrcode) 权限校验失败。请确保应用已声明ohos.permission.ACCESS\_DDK\_HID权限。  [HID\_DDK\_INVALID\_PARAMETER](capi-hid-ddk-types-h.md#hid_ddkerrcode) 参数校验失败。可能原因：1. dev为空；  2. buf为空；3. bufSize为0；4. bufSize超过[HID\_MAX\_REPORT\_BUFFER\_SIZE](capi-hid-ddk-types-h.md#宏定义)；  5. bytesRead为空。  [HID\_DDK\_INIT\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) DDK未初始化，请确保已调用[OH\_Hid\_Init](capi-hid-ddk-api-h.md#oh_hid_init)完成初始化。  [HID\_DDK\_SERVICE\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 与DDK服务通信失败。可能原因：服务内部错误。请检查当前操作和设备状态。  [HID\_DDK\_MEMORY\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) 内存数据拷贝失败。  [HID\_DDK\_IO\_ERROR](capi-hid-ddk-types-h.md#hid_ddkerrcode) I/O操作失败。可能原因：设备状态异常、数据传输错误等。请检查设备状态和参数。  [HID\_DDK\_INVALID\_OPERATION](capi-hid-ddk-types-h.md#hid_ddkerrcode) 不支持此操作。 |
