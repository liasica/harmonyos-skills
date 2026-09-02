---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-readcapacityrequest
title: ScsiPeripheral_ReadCapacityRequest
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_ReadCapacityRequest
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:237c967a7116612525767835b5b5d652ed816967f535f6a6abfc68b1a7e3d780
---

```c
typedef struct ScsiPeripheral_ReadCapacityRequest {...} ScsiPeripheral_ReadCapacityRequest
```

## 概述

SCSI命令（READ CAPACITY）的请求结构体，用于发送读取存储容量的命令，可帮助获取设备的逻辑块大小和总块数。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](capi-scsi-peripheral-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t lbAddress | 逻辑块地址，用于指定读取容量的起始逻辑块位置。取值为0时获取设备整体容量信息。 |
| uint8\_t control | Control字段，用于指定SCSI命令的控制信息。 |
| uint8\_t byte8 | CDB（Command Descriptor Block，命令描述符块）的第八个字节。 |
| uint32\_t timeout | 超时时间（单位：ms）。 |
