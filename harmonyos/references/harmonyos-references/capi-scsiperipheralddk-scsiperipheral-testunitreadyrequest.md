---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-testunitreadyrequest
title: ScsiPeripheral_TestUnitReadyRequest
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_TestUnitReadyRequest
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:87adc78174f30f5dc2ef5a5fcaae9866b0d947daffa570e86fc6e88cfc033578
---

```c
typedef struct ScsiPeripheral_TestUnitReadyRequest {...} ScsiPeripheral_TestUnitReadyRequest
```

## 概述

SCSI命令（TEST UNIT READY）的请求结构体，通常用于确认逻辑单元是否就绪（逻辑单元是SCSI设备中可独立寻址的I/O操作实体）。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](capi-scsi-peripheral-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t control | Control字段，用于指定SCSI命令的控制信息。 |
| uint32\_t timeout | 超时时间（单位：ms）。 |
