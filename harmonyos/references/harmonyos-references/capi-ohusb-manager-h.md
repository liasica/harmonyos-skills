---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohusb-manager-h
title: ohusb_manager.h
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 头文件 > ohusb_manager.h
category: harmonyos-references
scraped_at: 2026-11-12T09:55:58+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:8b552d6c49f05ebe85dcac53f50f986e4496767a286605ba81f3a96a0c4d5f80
---

## 概述

声明用于USB设备管理的C API。

**引用文件：** <BasicServicesKit/ohusb\_manager.h>

**库：** libohusb\_manager.so

**系统能力：** SystemCapability.USB.USBManager

**起始版本：** 26.0.1

**相关模块：** [UsbManager](capi-usbmanager.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_UsbManager\_UsbEndpoint](capi-usbmanager-oh-usbmanager-usbendpoint.md) | OH\_UsbManager\_UsbEndpoint | 定义用于发送或接收数据的USB端点。端点从[OH\_UsbManager\_UsbInterface](capi-usbmanager-oh-usbmanager-usbinterface.md)获取。 |
| [OH\_UsbManager\_UsbInterface](capi-usbmanager-oh-usbmanager-usbinterface.md) | OH\_UsbManager\_UsbInterface | 定义USB接口。一个[OH\_UsbManager\_UsbConfig](capi-usbmanager-oh-usbmanager-usbconfig.md)可以包含多个OH\_UsbManager\_UsbInterface实例，每个实例提供特定功能。 |
| [OH\_UsbManager\_UsbConfig](capi-usbmanager-oh-usbmanager-usbconfig.md) | OH\_UsbManager\_UsbConfig | 定义USB配置。一个[OH\_UsbManager\_UsbDevice](capi-usbmanager-oh-usbmanager-usbdevice.md)可以包含多个**OH\_UsbManager\_UsbConfig**实例。 |
| [OH\_UsbManager\_UsbDevice](capi-usbmanager-oh-usbmanager-usbdevice.md) | OH\_UsbManager\_UsbDevice | 定义USB设备的扁平化表示。 |
| [OH\_UsbManager\_UsbPipe](capi-usbmanager-oh-usbmanager-usbpipe.md) | OH\_UsbManager\_UsbPipe | 定义用于与已打开设备通信的USB设备管道。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_UsbManager\_ErrorCode](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) | OH\_UsbManager\_ErrorCode | 枚举USB管理器的错误码。 |
| [OH\_UsbManager\_RequestDirection](capi-ohusb-manager-h.md#oh_usbmanager_requestdirection) | OH\_UsbManager\_RequestDirection | 枚举USB请求方向。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_UsbManager\_ErrorCode OH\_UsbManager\_GetUsbDeviceList(OH\_UsbManager\_UsbDevice \*\*devices, uint32\_t \*deviceCount)](capi-ohusb-manager-h.md#oh_usbmanager_getusbdevicelist) | - | 获取所有已连接USB设备的列表。调用者必须调用[OH\_UsbManager\_FreeUsbDeviceList](capi-ohusb-manager-h.md#oh_usbmanager_freeusbdevicelist)释放返回的数组。 |
| [void OH\_UsbManager\_FreeUsbDeviceList(OH\_UsbManager\_UsbDevice \*devices, uint32\_t deviceCount)](capi-ohusb-manager-h.md#oh_usbmanager_freeusbdevicelist) | - | 释放之前由[OH\_UsbManager\_GetUsbDeviceList](capi-ohusb-manager-h.md#oh_usbmanager_getusbdevicelist)返回的设备数组。调用后该指针失效，不得再使用。传入null或数量为0是安全的空操作。 |
| [OH\_UsbManager\_ErrorCode OH\_UsbManager\_ConnectDevice(const OH\_UsbManager\_UsbDevice \*device, OH\_UsbManager\_UsbPipe \*pipe)](capi-ohusb-manager-h.md#oh_usbmanager_connectdevice) | - | 连接USB设备并打开用于通信的管道。返回的管道必须通过调用[OH\_UsbManager\_ClosePipe](capi-ohusb-manager-h.md#oh_usbmanager_closepipe)关闭，以避免资源泄漏。仅需要设备结构体中的**busNum**和**devAddress**字段；其他字段将被忽略。 |
| [OH\_UsbManager\_ErrorCode OH\_UsbManager\_HasPermission(const char \*deviceName, bool \*result)](capi-ohusb-manager-h.md#oh_usbmanager_haspermission) | - | 检查应用是否有权限访问指定设备。 |
| [typedef void (\*OH\_UsbManager\_PermissionCallback)(OH\_UsbManager\_ErrorCode errorCode, bool result, void \*userContext)](capi-ohusb-manager-h.md#oh_usbmanager_permissioncallback) | OH\_UsbManager\_PermissionCallback | 定义用于返回[OH\_UsbManager\_RequestPermission](capi-ohusb-manager-h.md#oh_usbmanager_requestpermission)结果的回调类型。 |
| [OH\_UsbManager\_ErrorCode OH\_UsbManager\_RequestPermission(const char \*deviceName, OH\_UsbManager\_PermissionCallback callback, void \*userContext)](capi-ohusb-manager-h.md#oh_usbmanager_requestpermission) | - | 异步请求访问指定USB设备的权限。这可能触发系统弹窗询问用户是否授权。函数立即返回，结果通过回调传递。 |
| [OH\_UsbManager\_ErrorCode OH\_UsbManager\_GetFileDescriptor(const OH\_UsbManager\_UsbPipe \*pipe, int32\_t \*fd)](capi-ohusb-manager-h.md#oh_usbmanager_getfiledescriptor) | - | 获取已打开USB设备管道的文件描述符。该fd可用于基于ioctl的底层USB传输。 |
| [OH\_UsbManager\_ErrorCode OH\_UsbManager\_ClosePipe(const OH\_UsbManager\_UsbPipe \*pipe)](capi-ohusb-manager-h.md#oh_usbmanager_closepipe) | - | 关闭USB设备管道并释放底层资源。该管道必须从[OH\_UsbManager\_ConnectDevice](capi-ohusb-manager-h.md#oh_usbmanager_connectdevice)获取。 |

## 枚举类型说明

### OH\_UsbManager\_ErrorCode

```c
enum OH_UsbManager_ErrorCode
```

**描述：**

枚举USB管理器的错误码。

**起始版本：** 26.0.1

| 枚举项 | 描述 |
| --- | --- |
| OH\_USBMANAGER\_SUCCESS = 0 | 操作成功。  **起始版本：** 26.0.1 |
| OH\_USBMANAGER\_ERROR\_PERMISSION\_DENIED = 14400001 | 权限被拒绝。  **起始版本：** 26.0.1 |
| OH\_USBMANAGER\_ERROR\_SERVICE\_EXCEPTION = 14400004 | 服务异常。  **起始版本：** 26.0.1 |
| OH\_USBMANAGER\_ERROR\_NO\_DEVICE = 14400008 | 不存在该设备（可能已被断开连接）。  **起始版本：** 26.0.1 |
| OH\_USBMANAGER\_ERROR\_NO\_MEMORY = 14400009 | 内存不足。  **起始版本：** 26.0.1 |
| OH\_USBMANAGER\_ERROR\_IO\_ERROR = 14400012 | 传输I/O错误。  **起始版本：** 26.0.1 |
| OH\_USBMANAGER\_ERROR\_INVALID\_PARAMETER = 14400014 | 无效参数。对不可为空的参数传入了空指针。  **起始版本：** 26.0.1 |

### OH\_UsbManager\_RequestDirection

```c
enum OH_UsbManager_RequestDirection
```

**描述：**

枚举USB请求方向。

**起始版本：** 26.0.1

| 枚举项 | 描述 |
| --- | --- |
| OH\_USBMANAGER\_REQUEST\_DIR\_TO\_DEVICE = 0 | 用于从主机向设备写入数据的请求。  **起始版本：** 26.0.1 |
| OH\_USBMANAGER\_REQUEST\_DIR\_FROM\_DEVICE = 0x80 | 用于从设备向主机读取数据的请求。  **起始版本：** 26.0.1 |

## 函数说明

### OH\_UsbManager\_GetUsbDeviceList()

```c
OH_UsbManager_ErrorCode OH_UsbManager_GetUsbDeviceList(OH_UsbManager_UsbDevice **devices, uint32_t *deviceCount)
```

**描述：**

获取所有已连接USB设备的列表。调用者必须调用[OH\_UsbManager\_FreeUsbDeviceList](capi-ohusb-manager-h.md#oh_usbmanager_freeusbdevicelist)释放返回的数组。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UsbManager\_UsbDevice](capi-usbmanager-oh-usbmanager-usbdevice.md) \*\*devices | [出参] 指向[OH\_UsbManager\_UsbDevice](capi-usbmanager-oh-usbmanager-usbdevice.md)数组的二级指针。成功时，函数会分配该数组及所有内部字符串缓冲区。调用者不得单独释放各个字段；请改用[OH\_UsbManager\_FreeUsbDeviceList](capi-ohusb-manager-h.md#oh_usbmanager_freeusbdevicelist)。不得为空。 |
| uint32\_t \*deviceCount | [出参] 指向返回设备数量的指针。成功时，该值被设置为数组中的元素个数。为0表示当前没有设备。不得为空。 |

**资源释放：** [OH\_UsbManager\_FreeUsbDeviceList](capi-ohusb-manager-h.md#oh_usbmanager_freeusbdevicelist)

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_UsbManager\_ErrorCode](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) | [OH\_USBMANAGER\_SUCCESS](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示操作成功。  [OH\_USBMANAGER\_ERROR\_SERVICE\_EXCEPTION](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示USB服务不可用。可能原因：USB服务故障，例如服务未运行或意外停止。  [OH\_USBMANAGER\_ERROR\_NO\_MEMORY](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示设备数组或字符串的内存分配失败。可能原因：系统内存不足或连接的设备过多。处理建议：释放未使用的内存后重试。  [OH\_USBMANAGER\_ERROR\_INVALID\_PARAMETER](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示devices或deviceCount为NULL。可能原因：未提供必需的参数。处理建议：传入有效的非空指针。 |

### OH\_UsbManager\_FreeUsbDeviceList()

```c
void OH_UsbManager_FreeUsbDeviceList(OH_UsbManager_UsbDevice *devices, uint32_t deviceCount)
```

**描述：**

释放之前由[OH\_UsbManager\_GetUsbDeviceList](capi-ohusb-manager-h.md#oh_usbmanager_getusbdevicelist)返回的设备数组。调用后该指针失效，不得再使用。传入null或数量为0是安全的空操作。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UsbManager\_UsbDevice](capi-usbmanager-oh-usbmanager-usbdevice.md) \*devices | [入参] 指向由[OH\_UsbManager\_GetUsbDeviceList](capi-ohusb-manager-h.md#oh_usbmanager_getusbdevicelist)返回的数组的指针。 |
| uint32\_t deviceCount | [入参] 数组中的元素个数，由[OH\_UsbManager\_GetUsbDeviceList](capi-ohusb-manager-h.md#oh_usbmanager_getusbdevicelist)返回。 |

### OH\_UsbManager\_ConnectDevice()

```c
OH_UsbManager_ErrorCode OH_UsbManager_ConnectDevice(const OH_UsbManager_UsbDevice *device, OH_UsbManager_UsbPipe *pipe)
```

**描述：**

连接USB设备并打开用于通信的管道。返回的管道必须通过调用[OH\_UsbManager\_ClosePipe](capi-ohusb-manager-h.md#oh_usbmanager_closepipe)关闭，以避免资源泄漏。仅需要设备结构体中的**busNum**和**devAddress**字段；其他字段将被忽略。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_UsbManager\_UsbDevice](capi-usbmanager-oh-usbmanager-usbdevice.md) \*device | [入参] 指向要连接的[OH\_UsbManager\_UsbDevice](capi-usbmanager-oh-usbmanager-usbdevice.md)的指针。不得为空。 |
| [OH\_UsbManager\_UsbPipe](capi-usbmanager-oh-usbmanager-usbpipe.md) \*pipe | [出参] 指向[OH\_UsbManager\_UsbPipe](capi-usbmanager-oh-usbmanager-usbpipe.md)的指针，成功时用于接收句柄。不得为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_UsbManager\_ErrorCode](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) | [OH\_USBMANAGER\_SUCCESS](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示连接成功。  [OH\_USBMANAGER\_ERROR\_PERMISSION\_DENIED](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示应用缺少设备访问权限。  可能原因：尚未请求访问权限、权限已被撤销，或用户拒绝了请求。  处理建议：调用[OH\_UsbManager\_RequestPermission](capi-ohusb-manager-h.md#oh_usbmanager_requestpermission)请求访问权限。  [OH\_USBMANAGER\_ERROR\_SERVICE\_EXCEPTION](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示USB服务打开设备失败。  可能原因：USB服务故障（例如服务未运行或意外停止），或传入的device无效。  处理建议：如果device无效，请先通过[OH\_UsbManager\_GetUsbDeviceList](capi-ohusb-manager-h.md#oh_usbmanager_getusbdevicelist)  获取有效的设备数据后重试。  [OH\_USBMANAGER\_ERROR\_IO\_ERROR](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示无法打开设备（如已断开连接或发生I/O失败）。  可能原因：设备已断开连接或USB总线发生I/O错误。  处理建议：检查物理连接和设备状态后重试。  [OH\_USBMANAGER\_ERROR\_INVALID\_PARAMETER](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示device或pipe为NULL。  可能原因：未提供必需的参数。处理建议：传入有效的非空指针。 |

### OH\_UsbManager\_HasPermission()

```c
OH_UsbManager_ErrorCode OH_UsbManager_HasPermission(const char *deviceName, bool *result)
```

**描述：**

检查应用是否有权限访问指定设备。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*deviceName | [入参] 设备名称，格式为<总线编号>-<设备地址>。不得为空。 |
| bool \*result | [出参] 用于接收结果的指针。如果应用已被授予访问设备的权限则为true；如果权限未被授予或未被请求则为false。不得为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_UsbManager\_ErrorCode](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) | [OH\_USBMANAGER\_SUCCESS](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示操作成功。  [OH\_USBMANAGER\_ERROR\_SERVICE\_EXCEPTION](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示USB服务不可用。  可能原因：USB服务故障（例如服务未运行或意外停止），或传入的deviceName无效。  处理建议：如果deviceName无效，请先通过[OH\_UsbManager\_GetUsbDeviceList](capi-ohusb-manager-h.md#oh_usbmanager_getusbdevicelist)  获取有效的设备名称后重试。  [OH\_USBMANAGER\_ERROR\_INVALID\_PARAMETER](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示deviceName或result为NULL。  可能原因：未提供必需的参数。处理建议：传入有效的非空指针。 |

### OH\_UsbManager\_PermissionCallback()

```c
typedef void (*OH_UsbManager_PermissionCallback)(OH_UsbManager_ErrorCode errorCode, bool result, void *userContext)
```

**描述：**

定义用于返回[OH\_UsbManager\_RequestPermission](capi-ohusb-manager-h.md#oh_usbmanager_requestpermission)结果的回调类型。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UsbManager\_ErrorCode](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) errorCode | [出参] 请求的错误码。[OH\_USBMANAGER\_SUCCESS](capi-ohusb-manager-h.md#oh_usbmanager_errorcode)表示请求正常完成；其他值表示服务异常。 |
| bool result | [出参] 如果权限被授予则为true；如果用户拒绝请求则为false。该参数仅在errorCode为[OH\_USBMANAGER\_SUCCESS](capi-ohusb-manager-h.md#oh_usbmanager_errorcode)时有意义。 |
| void \*userContext | [出参] 从[OH\_UsbManager\_RequestPermission](capi-ohusb-manager-h.md#oh_usbmanager_requestpermission)透传的用户上下文。 |

### OH\_UsbManager\_RequestPermission()

```c
OH_UsbManager_ErrorCode OH_UsbManager_RequestPermission(const char *deviceName, OH_UsbManager_PermissionCallback callback, void *userContext)
```

**描述：**

异步请求访问指定USB设备的权限。这可能触发系统弹窗询问用户是否授权。函数立即返回，结果通过回调传递。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*deviceName | [入参] 设备名称，格式为<总线编号>-<设备地址>。不得为空。 |
| [OH\_UsbManager\_PermissionCallback](capi-ohusb-manager-h.md#oh_usbmanager_permissioncallback) callback | [入参] 请求完成时调用的[OH\_UsbManager\_PermissionCallback](capi-ohusb-manager-h.md#oh_usbmanager_permissioncallback)。不得为空。 |
| void \*userContext | [入参] 传递给回调的用户上下文指针。可以为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_UsbManager\_ErrorCode](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) | [OH\_USBMANAGER\_SUCCESS](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示请求成功发起。  [OH\_USBMANAGER\_ERROR\_SERVICE\_EXCEPTION](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示服务启动请求失败。  可能原因：USB服务故障（例如服务未运行或意外停止），或传入的deviceName无效。  处理建议：如果deviceName无效，请先通过[OH\_UsbManager\_GetUsbDeviceList](capi-ohusb-manager-h.md#oh_usbmanager_getusbdevicelist)  获取有效的设备名称后重试。  [OH\_USBMANAGER\_ERROR\_INVALID\_PARAMETER](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示deviceName或callback为NULL。  可能原因：未提供必需的参数。处理建议：传入有效的非空指针。 |

### OH\_UsbManager\_GetFileDescriptor()

```c
OH_UsbManager_ErrorCode OH_UsbManager_GetFileDescriptor(const OH_UsbManager_UsbPipe *pipe, int32_t *fd)
```

**描述：**

获取已打开USB设备管道的文件描述符。该fd可用于基于ioctl的底层USB传输。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_UsbManager\_UsbPipe](capi-usbmanager-oh-usbmanager-usbpipe.md) \*pipe | [入参] 指向从[OH\_UsbManager\_ConnectDevice](capi-ohusb-manager-h.md#oh_usbmanager_connectdevice)获取的[OH\_UsbManager\_UsbPipe](capi-usbmanager-oh-usbmanager-usbpipe.md)的指针。不得为空。 |
| int32\_t \*fd | [出参] 用于在成功时接收文件描述符的指针。不得为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_UsbManager\_ErrorCode](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) | [OH\_USBMANAGER\_SUCCESS](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示操作成功。  [OH\_USBMANAGER\_ERROR\_PERMISSION\_DENIED](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示应用缺少设备访问权限。  可能原因：尚未请求访问权限、权限已被撤销，或用户拒绝了请求。  处理建议：调用[OH\_UsbManager\_RequestPermission](capi-ohusb-manager-h.md#oh_usbmanager_requestpermission)请求访问权限。  [OH\_USBMANAGER\_ERROR\_SERVICE\_EXCEPTION](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示管道无效或服务失败。  可能原因：USB服务故障，或管道并非通过[OH\_UsbManager\_ConnectDevice](capi-ohusb-manager-h.md#oh_usbmanager_connectdevice)获取、  或管道已被关闭。处理建议：如果管道无效或已关闭，请通过  [OH\_UsbManager\_ConnectDevice](capi-ohusb-manager-h.md#oh_usbmanager_connectdevice)获取有效的打开管道后重试。  [OH\_USBMANAGER\_ERROR\_NO\_DEVICE](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示设备不存在或已断开连接。  可能原因：设备已被拔出。处理建议：使用[OH\_UsbManager\_GetUsbDeviceList](capi-ohusb-manager-h.md#oh_usbmanager_getusbdevicelist)  重新枚举设备并重新连接。  [OH\_USBMANAGER\_ERROR\_INVALID\_PARAMETER](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示pipe或fd为NULL。  可能原因：未提供必需的参数。处理建议：传入有效的非空指针。 |

### OH\_UsbManager\_ClosePipe()

```c
OH_UsbManager_ErrorCode OH_UsbManager_ClosePipe(const OH_UsbManager_UsbPipe *pipe)
```

**描述：**

关闭USB设备管道并释放底层资源。该管道必须从[OH\_UsbManager\_ConnectDevice](capi-ohusb-manager-h.md#oh_usbmanager_connectdevice)获取。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_UsbManager\_UsbPipe](capi-usbmanager-oh-usbmanager-usbpipe.md) \*pipe | [入参] 指向要关闭的、从[OH\_UsbManager\_ConnectDevice](capi-ohusb-manager-h.md#oh_usbmanager_connectdevice)获取的[OH\_UsbManager\_UsbPipe](capi-usbmanager-oh-usbmanager-usbpipe.md)的指针。不得为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_UsbManager\_ErrorCode](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) | [OH\_USBMANAGER\_SUCCESS](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示管道关闭成功。  [OH\_USBMANAGER\_ERROR\_PERMISSION\_DENIED](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示应用缺少设备访问权限。  可能原因：尚未请求访问权限、权限已被撤销，或用户拒绝了请求。  处理建议：调用[OH\_UsbManager\_RequestPermission](capi-ohusb-manager-h.md#oh_usbmanager_requestpermission)请求访问权限。  [OH\_USBMANAGER\_ERROR\_SERVICE\_EXCEPTION](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示关闭操作失败。  可能原因：USB服务故障，或管道无效或已被关闭。处理建议：如果管道无效或已关闭，  请通过[OH\_UsbManager\_ConnectDevice](capi-ohusb-manager-h.md#oh_usbmanager_connectdevice)获取有效的打开管道后重试。  [OH\_USBMANAGER\_ERROR\_INVALID\_PARAMETER](capi-ohusb-manager-h.md#oh_usbmanager_errorcode) 表示pipe为NULL。  可能原因：未提供必需的参数。处理建议：传入有效的非空指针。 |
