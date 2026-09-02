---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usb-serial-types-h
title: usb_serial_types.h
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 头文件 > usb_serial_types.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:419e125eb76c1fc76baed719708f3cee096bea939b2df64f1e0ae9026c39a5ca
---

## 概述

提供USB Serial DDK中的枚举类型与结构体的定义，用于USB串口驱动开发，简化串口设备参数配置、返回码处理和流量控制等操作，提升驱动开发效率。

**引用文件：** <usb\_serial/usb\_serial\_types.h>

**库：** libusb\_serial\_ndk.z.so

**系统能力：** SystemCapability.Driver.UsbSerial.Extension

**起始版本：** 18

**相关模块：** [USBSerialDDK](capi-serialddk.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [UsbSerial\_Params](capi-serialddk-usbserial-params.md) | UsbSerial\_Params | 定义USB Serial DDK使用的USB串口参数，用于USB转串口设备的通信参数配置，需与目标通信设备的配置保持一致，否则可能无法正常通信。常见于工业控制设备、调试工具、传感器数据采集等需要通过USB串口与设备通信的场景。 |
| [UsbSerial\_Device](capi-serialddk-usbserial-devicehandle.md) | UsbSerial\_Device | USB串口设备数据结构（不透明），用于表示USB串口设备。开发者应通过[OH\_UsbSerial\_Open](capi-usb-serial-api-h.md#oh_usbserial_open)接口函数获取此结构体实例。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [UsbSerial\_DdkRetCode](capi-usb-serial-types-h.md#usbserial_ddkretcode) | UsbSerial\_DdkRetCode | 定义USB Serial DDK使用的返回码。 |
| [UsbSerial\_FlowControl](capi-usb-serial-types-h.md#usbserial_flowcontrol) | UsbSerial\_FlowControl | 定义USB Serial DDK中的流量控制。在使用USB串口进行数据传输时，需要根据通信场景选择合适的流量控制方式。例如，在高速大数据量传输场景下，建议使用硬件流控以避免数据丢失；在低速或对实时性要求不高的场景下，可使用软件流控；在短距离、可靠的点对点通信场景下，可选择无流控。 |
| [UsbSerial\_Parity](capi-usb-serial-types-h.md#usbserial_parity) | UsbSerial\_Parity | 定义USB Serial DDK使用的校验参数枚举。在配置USB串口通信参数时，需要根据数据传输的可靠性要求选择合适的校验方式。例如，在对数据完整性要求较高的工业控制场景下，建议使用奇校验或偶校验来检测传输错误；在高噪声干扰环境下，校验可以帮助识别错误数据；在短距离、可靠的通信场景下，为提高传输效率，可选择无校验。 |

## 枚举类型说明

### UsbSerial\_DdkRetCode

```c
enum UsbSerial_DdkRetCode
```

**描述**

定义USB Serial DDK使用的返回码。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| USB\_SERIAL\_DDK\_NO\_PERM = 201 | 权限被拒绝。请确保应用在module.json5文件中声明了所需的权限。 |
| USB\_SERIAL\_DDK\_INVALID\_PARAMETER = 401 | 无效参数。请确保传入的参数值在有效范围内，参考相关接口的参数说明。 |
| USB\_SERIAL\_DDK\_SUCCESS = 31600000 | 操作成功。 |
| USB\_SERIAL\_DDK\_INVALID\_OPERATION = 31600001 | 无效操作，例如使用了无效的设备句柄。请检查确保设备处于正常打开的状态。 |
| USB\_SERIAL\_DDK\_INIT\_ERROR = 31600002 | 初始化失败。请先初始化DDK服务。 |
| USB\_SERIAL\_DDK\_SERVICE\_ERROR = 31600003 | 服务错误。请检查DDK服务状态和接口调用逻辑是否正常。 |
| USB\_SERIAL\_DDK\_MEMORY\_ERROR = 31600004 | 内存相关错误，例如内存不足、内存数据复制失败或内存申请故障。建议优化内存参数，及时释放不再需要的资源。 |
| USB\_SERIAL\_DDK\_IO\_ERROR = 31600005 | I/O 错误。请检查设备连接是否正常、传输线是否完好、设备是否处于正常工作状态。 |
| USB\_SERIAL\_DDK\_DEVICE\_NOT\_FOUND = 31600006 | 未找到设备。请检查参数和设备连接状态。 |

### UsbSerial\_FlowControl

```c
enum UsbSerial_FlowControl
```

**描述**

定义USB Serial DDK中的流量控制。在使用USB串口进行数据传输时，需要根据通信场景选择合适的流量控制方式。例如，在高速大数据量传输场景下，建议使用硬件流控以避免数据丢失；在低速或对实时性要求不高的场景下，可使用软件流控；在短距离、可靠的点对点通信场景下，可选择无流控。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| USB\_SERIAL\_NO\_FLOW\_CONTROL = 0 | 无流量控制。适用于低速传输或无需流控的场景，但可能导致数据丢失。 |
| USB\_SERIAL\_SOFTWARE\_FLOW\_CONTROL = 1 | 软件流控。使用XON/XOFF字符控制，适用于不支持硬件流控的设备。 |
| USB\_SERIAL\_HARDWARE\_FLOW\_CONTROL = 2 | 硬件流控。使用RTS/CTS信号线，适用于高速数据传输，可靠性高。 |

### UsbSerial\_Parity

```c
enum UsbSerial_Parity
```

**描述**

定义USB Serial DDK使用的校验参数枚举。在配置USB串口通信参数时，需要根据数据传输的可靠性要求选择合适的校验方式。例如，在对数据完整性要求较高的工业控制场景下，建议使用奇校验或偶校验来检测传输错误；在高噪声干扰环境下，校验可以帮助识别错误数据；在短距离、可靠的通信场景下，为提高传输效率，可选择无校验。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| USB\_SERIAL\_PARITY\_NONE = 0 | 无校验。在短距离、可靠的通信场景下，为提高传输效率，可选择无校验。 |
| USB\_SERIAL\_PARITY\_ODD = 1 | 奇校验。适用于对数据完整性要求较高的场景。 |
| USB\_SERIAL\_PARITY\_EVEN = 2 | 偶校验。适用于对数据完整性要求较高的场景。 |
