---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsi-peripheral-types-h
title: scsi_peripheral_types.h
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 头文件 > scsi_peripheral_types.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9148a6860443c1713ee9c8c834c258260df38055ffed32a0c4e7dcef7055ee81
---

## 概述

提供在SCSI Peripheral DDK（驱动开发工具包）API中使用的枚举变量、结构体和宏。

**引用文件：** <scsi\_peripheral/scsi\_peripheral\_types.h>

**库：** libscsi.z.so

**系统能力：** SystemCapability.Driver.SCSI.Extension

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ScsiPeripheral\_DeviceMemMap](capi-scsiperipheralddk-scsiperipheral-devicememmap.md) | ScsiPeripheral\_DeviceMemMap | 通过调用[OH\_ScsiPeripheral\_CreateDeviceMemMap](capi-scsi-peripheral-api-h.md#oh_scsiperipheral_createdevicememmap)创建的设备内存映射。使用该设备内存映射的缓冲区可以提供更好的性能。 |
| [ScsiPeripheral\_IORequest](capi-scsiperipheralddk-scsiperipheral-iorequest.md) | ScsiPeripheral\_IORequest | 读/写操作的请求参数。该结构体定义了SCSI外设进行读/写操作时所需的请求参数，包括逻辑块起始地址、传输长度、控制信息等。 |
| [ScsiPeripheral\_Request](capi-scsiperipheralddk-scsiperipheral-request.md) | ScsiPeripheral\_Request | SCSI请求参数结构体，用于构造与SCSI设备交互的请求参数，支持配置命令描述符块、数据缓冲区、超时时间等。 |
| [ScsiPeripheral\_Response](capi-scsiperipheralddk-scsiperipheral-response.md) | ScsiPeripheral\_Response | SCSI响应参数结构体，包含状态、错误诊断数据、传输结果等，用于接收SCSI设备响应数据、判断命令是否成功。 |
| [ScsiPeripheral\_TestUnitReadyRequest](capi-scsiperipheralddk-scsiperipheral-testunitreadyrequest.md) | ScsiPeripheral\_TestUnitReadyRequest | SCSI命令（TEST UNIT READY）的请求结构体，通常用于确认逻辑单元是否就绪（逻辑单元是SCSI设备中可独立寻址的I/O操作实体）。 |
| [ScsiPeripheral\_InquiryRequest](capi-scsiperipheralddk-scsiperipheral-inquiryrequest.md) | ScsiPeripheral\_InquiryRequest | SCSI命令（INQUIRY）的请求结构体，通常用于查询设备的基本信息。 |
| [ScsiPeripheral\_InquiryInfo](capi-scsiperipheralddk-scsiperipheral-inquiryinfo.md) | ScsiPeripheral\_InquiryInfo | SCSI INQUIRY 数据，用于存储SCSI外设的INQUIRY命令查询结果。 |
| [ScsiPeripheral\_ReadCapacityRequest](capi-scsiperipheralddk-scsiperipheral-readcapacityrequest.md) | ScsiPeripheral\_ReadCapacityRequest | SCSI命令（READ CAPACITY）的请求结构体，用于发送读取存储容量的命令，可帮助获取设备的逻辑块大小和总块数。 |
| [ScsiPeripheral\_CapacityInfo](capi-scsiperipheralddk-scsiperipheral-capacityinfo.md) | ScsiPeripheral\_CapacityInfo | SCSI READ CAPACITY结构体。用于在开发SCSI设备驱动时获取设备的存储容量信息，支持进行分区管理、可用空间检查和存储资源分配等操作。 |
| [ScsiPeripheral\_RequestSenseRequest](capi-scsiperipheralddk-scsiperipheral-requestsenserequest.md) | ScsiPeripheral\_RequestSenseRequest | SCSI命令（REQUEST SENSE）的请求结构体，该命令通常用于获取设备的错误信息。 |
| [ScsiPeripheral\_BasicSenseInfo](capi-scsiperipheralddk-scsiperipheral-basicsenseinfo.md) | ScsiPeripheral\_BasicSenseInfo | SCSI Sense Data的基本信息结构体，用于封装SCSI命令执行后返回的sense数据。该结构体包含响应码、状态标志位以及各类信息字段，用于驱动程序获取和分析SCSI设备的错误状态和命令执行结果。 |
| [ScsiPeripheral\_VerifyRequest](capi-scsiperipheralddk-scsiperipheral-verifyrequest.md) | ScsiPeripheral\_VerifyRequest | SCSI命令（VERIFY）的请求结构体，该命令通常用于校验逻辑块的数据完整性。 |
| [ScsiPeripheral\_Device](capi-scsiperipheralddk-scsiperipheral-device.md) | ScsiPeripheral\_Device | 不透明的SCSI设备结构体，用于表示与SCSI外设交互的设备句柄。 |

### 宏定义

| 名称 | 描述 |
| --- | --- |
| SCSIPERIPHERAL\_MIN\_DESCRIPTOR\_FORMAT\_SENSE 8 | 描述符格式感知数据的最小长度。 **起始版本：** 18 |
| SCSIPERIPHERAL\_MIN\_FIXED\_FORMAT\_SENSE 18 | 固定格式感知数据的最小长度。 **起始版本：** 18 |
| SCSIPERIPHERAL\_MAX\_CMD\_DESC\_BLOCK\_LEN 16 | 命令描述符块的最大长度。 **起始版本：** 18 |
| SCSIPERIPHERAL\_MAX\_SENSE\_DATA\_LEN 252 | 感知数据的最大长度。 **起始版本：** 18 |
| SCSIPERIPHERAL\_VENDOR\_ID\_LEN 8 | 厂商标识符的长度。 **起始版本：** 18 |
| SCSIPERIPHERAL\_PRODUCT\_ID\_LEN 16 | 产品标识符的长度。 **起始版本：** 18 |
| SCSIPERIPHERAL\_PRODUCT\_REV\_LEN 4 | 产品修订版本号的长度。 **起始版本：** 18 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ScsiPeripheral\_DdkErrCode](capi-scsi-peripheral-types-h.md#scsiperipheral_ddkerrcode) | ScsiPeripheral\_DdkErrCode | SCSI Peripheral DDK错误码。 |
| [ScsiPeripheral\_Status](capi-scsi-peripheral-types-h.md#scsiperipheral_status) | ScsiPeripheral\_Status | 定义用于响应的SCSI状态。 |

## 枚举类型说明

### ScsiPeripheral\_DdkErrCode

```c
enum ScsiPeripheral_DdkErrCode
```

**描述**

SCSI Peripheral DDK错误码。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| SCSIPERIPHERAL\_DDK\_NO\_PERM = 201 | 没有权限。请确保应用已正确声明所需的权限。 |
| SCSIPERIPHERAL\_DDK\_INVALID\_PARAMETER = 401 | 非法参数。请检查参数是否符合要求。 |
| SCSIPERIPHERAL\_DDK\_SUCCESS = 31700000 | 操作成功。 |
| SCSIPERIPHERAL\_DDK\_MEMORY\_ERROR = 31700001 | 与内存相关的错误，例如，内存不足、内存数据复制失败或内存申请失败。请检查内存状态和相关参数。 |
| SCSIPERIPHERAL\_DDK\_INVALID\_OPERATION = 31700002 | 非法操作。请检查操作逻辑是否正确。 |
| SCSIPERIPHERAL\_DDK\_IO\_ERROR = 31700003 | 设备输入/输出操作失败。请检查传输参数和设备规格。 |
| SCSIPERIPHERAL\_DDK\_TIMEOUT = 31700004 | 传输超时。请检查超时参数和设备状态。 |
| SCSIPERIPHERAL\_DDK\_INIT\_ERROR = 31700005 | DDK初始化错误，或者DDK未初始化。请先初始化DDK服务。 |
| SCSIPERIPHERAL\_DDK\_SERVICE\_ERROR = 31700006 | 与SCSI Peripheral DDK服务的通信失败。请检查DDK服务是否正常运行。 |
| SCSIPERIPHERAL\_DDK\_DEVICE\_NOT\_FOUND = 31700007 | 设备未找到。请确保传入的设备信息正确。 |

### ScsiPeripheral\_Status

```c
enum ScsiPeripheral_Status
```

**描述**

定义用于响应的SCSI状态。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| SCSIPERIPHERAL\_STATUS\_GOOD = 0x00 | 正常状态。 |
| SCSIPERIPHERAL\_STATUS\_CHECK\_CONDITION\_NEEDED = 0x02 | 需要状态检查。 |
| SCSIPERIPHERAL\_STATUS\_CONDITION\_MET = 0x04 | 条件满足。 |
| SCSIPERIPHERAL\_STATUS\_BUSY = 0x08 | 占用中。 |
| SCSIPERIPHERAL\_STATUS\_RESERVATION\_CONFLICT = 0x18 | 资源保留冲突。 |
| SCSIPERIPHERAL\_STATUS\_TASK\_SET\_FULL = 0x28 | 任务集已满。 |
| SCSIPERIPHERAL\_STATUS\_ACA\_ACTIVE = 0x30 | ACA活动状态。 |
| SCSIPERIPHERAL\_STATUS\_TASK\_ABORTED = 0x40 | 任务已中止。 |
