---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-iorequest
title: ScsiPeripheral_IORequest
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_IORequest
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ff79e7761b1d82249e6e99c5b73496edb9a4507d31619ed269bed4838c538a4a
---

```c
typedef struct ScsiPeripheral_IORequest {...} ScsiPeripheral_IORequest
```

## 概述

读/写操作的请求参数。该结构体定义了SCSI外设进行读/写操作时所需的请求参数，包括逻辑块起始地址、传输长度、控制信息等。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](capi-scsi-peripheral-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t lbAddress | 逻辑块起始地址，用于指定SCSI外设读/写操作的起始逻辑块位置。 |
| uint16\_t transferLength | 需要操作的连续逻辑块的数量，必须是正整数且不超过设备单次传输的最大逻辑块数限制。 |
| uint8\_t control | Control字段，用于指定SCSI命令的控制标志，如优先级、链接命令等控制选项。 |
| uint8\_t byte1 | SCSI命令描述符块（CDB）的第一个字节，通常包含操作码和操作组信息。 |
| uint8\_t byte6 | SCSI命令描述符块（CDB）的第六个字节，根据命令类型包含不同的参数或标志信息。 |
| [ScsiPeripheral\_DeviceMemMap](capi-scsiperipheralddk-scsiperipheral-devicememmap.md)\* data | 数据传输的缓冲区。 |
| uint32\_t timeout | 超时时间（单位：ms）。 |
