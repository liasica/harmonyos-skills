---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsi-peripheral-types-h
title: scsi_peripheral_types.h
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 头文件 > scsi_peripheral_types.h
category: harmonyos-references
scraped_at: 2026-04-28T08:10:44+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:ef612ef617724f74bf51db43cf19bc10eb3df3274dd0229a0139591472d673d6
---

## 概述

PC/2in1

提供在SCSI Peripheral DDK（驱动开发工具包）API中使用的枚举变量、结构体和宏。

**引用文件：** <scsi\_peripheral/scsi\_peripheral\_types.h>

**库：** libscsi.z.so

**系统能力：** SystemCapability.Driver.SCSI.Extension

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

## 汇总

PC/2in1

### 结构体

PC/2in1

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ScsiPeripheral\_DeviceMemMap](capi-scsiperipheralddk-scsiperipheral-devicememmap.md) | ScsiPeripheral\_DeviceMemMap | 通过调用OH\_ScsiPeripheral\_CreateDeviceMemMap创建的设备内存映射。使用该设备内存映射的缓冲区可以提供更好的性能。 |
| [ScsiPeripheral\_IORequest](capi-scsiperipheralddk-scsiperipheral-iorequest.md) | ScsiPeripheral\_IORequest | 读/写操作的请求参数。 |
| [ScsiPeripheral\_Request](capi-scsiperipheralddk-scsiperipheral-request.md) | ScsiPeripheral\_Request | 请求参数结构体。 |
| [ScsiPeripheral\_Response](capi-scsiperipheralddk-scsiperipheral-response.md) | ScsiPeripheral\_Response | 响应参数结构体。 |
| [ScsiPeripheral\_TestUnitReadyRequest](iperipheralddk-scsiperipheral-testunitreadyrequest.md) | ScsiPeripheral\_TestUnitReadyRequest | 命令（test unit ready）的请求结构体。 |
| [ScsiPeripheral\_InquiryRequest](pi-scsiperipheralddk-scsiperipheral-inquiryrequest.md) | ScsiPeripheral\_InquiryRequest | SCSI命令（inquiry）的请求结构体。 |
| [ScsiPeripheral\_InquiryInfo](capi-scsiperipheralddk-scsiperipheral-inquiryinfo.md) | ScsiPeripheral\_InquiryInfo | SCSI inquiry 数据。 |
| [ScsiPeripheral\_ReadCapacityRequest](siperipheralddk-scsiperipheral-readcapacityrequest.md) | ScsiPeripheral\_ReadCapacityRequest | SCSI命令（read capacity）的请求结构体。 |
| [ScsiPeripheral\_CapacityInfo](capi-scsiperipheralddk-scsiperipheral-capacityinfo.md) | ScsiPeripheral\_CapacityInfo | SCSI read capacity 数据。 |
| [ScsiPeripheral\_RequestSenseRequest](siperipheralddk-scsiperipheral-requestsenserequest.md) | ScsiPeripheral\_RequestSenseRequest | SCSI命令（Request Sense）的请求结构体。 |
| [ScsiPeripheral\_BasicSenseInfo](pi-scsiperipheralddk-scsiperipheral-basicsenseinfo.md) | ScsiPeripheral\_BasicSenseInfo | sense data的基本信息。 |
| [ScsiPeripheral\_VerifyRequest](api-scsiperipheralddk-scsiperipheral-verifyrequest.md) | ScsiPeripheral\_VerifyRequest | SCSI命令（verify）的请求结构体。 |
| [ScsiPeripheral\_Device](capi-scsiperipheralddk-scsiperipheral-device.md) | ScsiPeripheral\_Device | 不透明的SCSI设备结构体。 |

### 枚举

PC/2in1

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ScsiPeripheral\_DdkErrCode](capi-scsi-peripheral-types-h.md#scsiperipheral_ddkerrcode) | ScsiPeripheral\_DdkErrCode | SCSI Peripheral DDK错误码。 |
| [ScsiPeripheral\_Status](capi-scsi-peripheral-types-h.md#scsiperipheral_status) | ScsiPeripheral\_Status | 定义用于响应的SCSI状态。 |

## 枚举类型说明

PC/2in1

### ScsiPeripheral\_DdkErrCode

PC/2in1

```
1. enum ScsiPeripheral_DdkErrCode
```

**描述**

SCSI Peripheral DDK错误码。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| SCSIPERIPHERAL\_DDK\_NO\_PERM = 201 | 没有权限。 |
| SCSIPERIPHERAL\_DDK\_INVALID\_PARAMETER = 401 | 非法参数。 |
| SCSIPERIPHERAL\_DDK\_SUCCESS = 31700000 | 操作成功。 |
| SCSIPERIPHERAL\_DDK\_MEMORY\_ERROR = 31700001 | 与内存相关的错误，例如，内存不足、内存数据复制失败或内存申请失败。 |
| SCSIPERIPHERAL\_DDK\_INVALID\_OPERATION = 31700002 | 非法操作。 |
| SCSIPERIPHERAL\_DDK\_IO\_ERROR = 31700003 | 设备输入/输出操作失败。 |
| SCSIPERIPHERAL\_DDK\_TIMEOUT = 31700004 | 传输超时。 |
| SCSIPERIPHERAL\_DDK\_INIT\_ERROR = 31700005 | DDK初始化错误，或者DDK未初始化。 |
| SCSIPERIPHERAL\_DDK\_SERVICE\_ERROR = 31700006 | 与SCSI Peripheral DDK服务的通信失败。 |
| SCSIPERIPHERAL\_DDK\_DEVICE\_NOT\_FOUND = 31700007 | 设备未找到。 |

### ScsiPeripheral\_Status

PC/2in1

```
1. enum ScsiPeripheral_Status
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
| SCSIPERIPHERAL\_STATUS\_TASK\_ABORTED = 0x40 | 任务已终止。 |

### SCSIPERIPHERAL\_MIN\_DESCRIPTOR\_FORMAT\_SENSE

PC/2in1

```
1. SCSIPERIPHERAL_MIN_DESCRIPTOR_FORMAT_SENSE 8
```

**描述**

描述符格式感应数据的最小长度。

**起始版本：** 18

### SCSIPERIPHERAL\_MIN\_FIXED\_FORMAT\_SENSE

PC/2in1

```
1. SCSIPERIPHERAL_MIN_FIXED_FORMAT_SENSE 18
```

**描述**

固定格式感应数据的最小长度。

**起始版本：** 18

### SCSIPERIPHERAL\_MAX\_CMD\_DESC\_BLOCK\_LEN

PC/2in1

```
1. SCSIPERIPHERAL_MAX_CMD_DESC_BLOCK_LEN 16
```

**描述**

命令描述块的最大长度。

**起始版本：** 18

### SCSIPERIPHERAL\_MAX\_SENSE\_DATA\_LEN

PC/2in1

```
1. SCSIPERIPHERAL_MAX_SENSE_DATA_LEN 252
```

**描述**

感应数据的最大长度。

**起始版本：** 18

### SCSIPERIPHERAL\_VENDOR\_ID\_LEN

PC/2in1

```
1. SCSIPERIPHERAL_VENDOR_ID_LEN 8
```

**描述**

厂商标识符的长度。

**起始版本：** 18

### SCSIPERIPHERAL\_PRODUCT\_ID\_LEN

PC/2in1

```
1. SCSIPERIPHERAL_PRODUCT_ID_LEN 16
```

**描述**

产品标识符的长度。

**起始版本：** 18

### SCSIPERIPHERAL\_PRODUCT\_REV\_LEN

PC/2in1

```
1. SCSIPERIPHERAL_PRODUCT_REV_LEN 4
```

**描述**

产品修订版本号的长度。

**起始版本：** 18
