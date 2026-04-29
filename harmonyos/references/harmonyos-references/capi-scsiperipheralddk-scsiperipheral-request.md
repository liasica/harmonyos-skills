---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-request
title: ScsiPeripheral_Request
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_Request
category: harmonyos-references
scraped_at: 2026-04-29T14:01:28+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:b16b25a2c7ea890305c61075a4be4c62a5334019d419373e6ca79fb4a50e23cb
---

```
1. typedef struct ScsiPeripheral_Request {...} ScsiPeripheral_Request
```

## 概述

PC/2in1

请求参数结构体。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](capi-scsi-peripheral-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint8\_t commandDescriptorBlock[[SCSIPERIPHERAL\_MAX\_CMD\_DESC\_BLOCK\_LEN](capi-scsi-peripheral-types-h.md)] | 命令描述符块。 |
| uint8\_t cdbLength | 命令描述符块的长度。 |
| int8\_t dataTransferDirection | 数据传输方向：-1为无数据传输的命令，-2为从主机到设备的数据传输(写)，-3为从设备到主机的数据传输(读)，-4为双向数据传输。 |
| [ScsiPeripheral\_DeviceMemMap](capi-scsiperipheralddk-scsiperipheral-devicememmap.md)\* data | 数据传输的缓冲区。 |
| uint32\_t timeout | 超时时间（单位：毫秒）。 |
