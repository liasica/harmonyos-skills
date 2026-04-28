---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usb-ddk-types-h
title: usb_ddk_types.h
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 头文件 > usb_ddk_types.h
category: harmonyos-references
scraped_at: 2026-04-28T08:10:43+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e3ba2a0d484568e346148ead5e15350d4b989a91d21cff8a94d1f2a0ff99d04a
---

## 概述

PC/2in1

提供USB DDK中的枚举变量、结构体定义与宏定义。

**引用文件：** <usb/usb\_ddk\_types.h>

**库：** libusb\_ndk.z.so

**系统能力：** SystemCapability.Driver.USB.Extension

**起始版本：** 10

**相关模块：** [UsbDdk](capi-usbddk.md)

## 汇总

PC/2in1

### 结构体

PC/2in1

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [UsbControlRequestSetup](capi-usbddk-usbcontrolrequestsetup.md) | \_\_attribute\_\_((aligned(8))) UsbControlRequestSetup | 控制传输setup包，对应USB协议中的Setup Data。 |
| [UsbDeviceDescriptor](capi-usbddk-usbdevicedescriptor.md) | \_\_attribute\_\_((aligned(8))) UsbDeviceDescriptor | 标准设备描述符，对应USB协议中Standard Device Descriptor。 |
| [UsbConfigDescriptor](capi-usbddk-usbconfigdescriptor.md) | \_\_attribute\_\_((packed)) UsbConfigDescriptor | 标准配置描述符，对应USB协议中Standard Configuration Descriptor。 |
| [UsbInterfaceDescriptor](capi-usbddk-usbinterfacedescriptor.md) | \_\_attribute\_\_((packed)) UsbInterfaceDescriptor | 标准接口描述符，对应USB协议中Standard Interface Descriptor。 |
| [UsbEndpointDescriptor](capi-usbddk-usbendpointdescriptor.md) | \_\_attribute\_\_((packed)) UsbEndpointDescriptor | 标准端点描述符，对应USB协议中Standard Endpoint Descriptor。 |
| [UsbDdkEndpointDescriptor](capi-usbddk-usbddkendpointdescriptor.md) | UsbDdkEndpointDescriptor | 端点描述符。 |
| [UsbDdkInterfaceDescriptor](capi-usbddk-usbddkinterfacedescriptor.md) | UsbDdkInterfaceDescriptor | 接口描述符。 |
| [UsbDdkInterface](capi-usbddk-usbddkinterface.md) | UsbDdkInterface | USB接口，是特定接口下备用设置的集合。 |
| [UsbDdkConfigDescriptor](capi-usbddk-usbddkconfigdescriptor.md) | UsbDdkConfigDescriptor | 配置描述符。 |
| [UsbRequestPipe](capi-usbddk-usbrequestpipe.md) | \_\_attribute\_\_((aligned(8))) UsbRequestPipe | 请求管道。 |
| [UsbDeviceMemMap](capi-usbddk-usbdevicememmap.md) | UsbDeviceMemMap | 设备内存映射，通过OH\_Usb\_CreateDeviceMemMap创建设备内存映射，使用内存映射后的缓冲区，获得更好的性能。 |
| [Usb\_DeviceArray](capi-usbddk-usb-devicearray.md) | Usb\_DeviceArray | 设备ID清单，用于存放OH\_Usb\_GetDevices接口获取到的设备ID列表和设备数量。 |

### 枚举

PC/2in1

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [UsbDdkErrCode](capi-usb-ddk-types-h.md#usbddkerrcode) | UsbDdkErrCode | USB DDK 错误码定义。 |

## 枚举类型说明

PC/2in1

### UsbDdkErrCode

PC/2in1

```
1. enum UsbDdkErrCode
```

**描述**

USB DDK 错误码定义。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| USB\_DDK\_SUCCESS = 0 | 操作成功。 |
| USB\_DDK\_FAILED = -1 | 操作失败。  **废弃版本：** 16 |
| USB\_DDK\_NO\_PERM = 201 | 没有权限。  **起始版本：** 14 |
| USB\_DDK\_INVALID\_PARAMETER = 401 | 非法参数，在API version 16之前值为-2。 |
| USB\_DDK\_MEMORY\_ERROR = 27400001 | 内存相关的错误，包括：内存不足、内存数据拷贝失败、内存申请失败等，在API version 16之前值为-3。 |
| USB\_DDK\_INVALID\_OPERATION = 27400002 | 非法操作，在API version 16之前值为-4。 |
| USB\_DDK\_NULL\_PTR = -5 | 空指针异常。  **废弃版本：** 16 |
| USB\_DDK\_DEVICE\_BUSY = -6 | 设备忙。  **废弃版本：** 16 |
| USB\_DDK\_IO\_FAILED = 27400003 | 设备I/O操作失败。  **起始版本：** 14 |
| USB\_DDK\_TIMEOUT = 27400004 | 传输超时，在API version 16之前值为-7。 |
