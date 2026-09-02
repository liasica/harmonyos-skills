---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-request
title: ScsiPeripheral_Request
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_Request
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2f233377b383ae6953ad8060ef95639e0c8eda16560dcb0e78eced1a621c0199
---

```c
typedef struct ScsiPeripheral_Request {...} ScsiPeripheral_Request
```

## 概述

SCSI请求参数结构体，用于构造与SCSI设备交互的请求参数，支持配置命令描述符块、数据缓冲区、超时时间等。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](capi-scsi-peripheral-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t commandDescriptorBlock[[SCSIPERIPHERAL\_MAX\_CMD\_DESC\_BLOCK\_LEN](capi-scsi-peripheral-types-h.md#宏定义)] | 命令描述符块，应遵循SCSI命令规范，填充对应命令的标准描述符格式。 |
| uint8\_t cdbLength | 命令描述符块的长度，应确保长度和实际命令匹配，最大不超过[SCSIPERIPHERAL\_MAX\_CMD\_DESC\_BLOCK\_LEN](capi-scsi-peripheral-types-h.md#宏定义)。 |
| int8\_t dataTransferDirection | 数据传输方向：-1为无数据传输的命令，-2为从主机到设备的数据传输（写），-3为从设备到主机的数据传输（读），-4为双向数据传输。 |
| [ScsiPeripheral\_DeviceMemMap](capi-scsiperipheralddk-scsiperipheral-devicememmap.md)\* data | 数据传输缓冲区的指针。 |
| uint32\_t timeout | 超时时间（单位：ms）。 |
