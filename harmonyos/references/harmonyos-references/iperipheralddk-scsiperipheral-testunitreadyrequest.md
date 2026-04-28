---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iperipheralddk-scsiperipheral-testunitreadyrequest
title: ScsiPeripheral_TestUnitReadyRequest
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_TestUnitReadyRequest
category: harmonyos-references
scraped_at: 2026-04-28T08:10:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b0b72b6e54f37569e2c6d2bf67d45e216ef32729cc37efe5c046d0a6e7349402
---

```
1. typedef struct ScsiPeripheral_TestUnitReadyRequest {...} ScsiPeripheral_TestUnitReadyRequest
```

## 概述

PC/2in1

命令（test unit ready）的请求结构体。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](capi-scsi-peripheral-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint8\_t control | Control字段，用于指定一些控制信息。 |
| uint32\_t timeout | 超时时间(单位: 毫秒)。 |
