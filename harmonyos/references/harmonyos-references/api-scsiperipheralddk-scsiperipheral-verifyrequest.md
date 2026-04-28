---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-scsiperipheralddk-scsiperipheral-verifyrequest
title: ScsiPeripheral_VerifyRequest
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_VerifyRequest
category: harmonyos-references
scraped_at: 2026-04-28T08:10:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:167386460482206cd8da85c5cce3d5b5bf68afde1c1480cdb56b500d2a53ef5c
---

```
1. typedef struct ScsiPeripheral_VerifyRequest {...} ScsiPeripheral_VerifyRequest
```

## 概述

PC/2in1

SCSI命令（verify）的请求结构体。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](capi-scsi-peripheral-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint32\_t lbAddress | 起始逻辑块地址。 |
| uint16\_t verificationLength | 连续校验逻辑块的个数。 |
| uint8\_t control | Control字段，用于指定一些控制信息。 |
| uint8\_t byte1 | CDB的第一个字节。 |
| uint8\_t byte6 | CDB的第六个字节。 |
| uint32\_t timeout | 超时时间(单位: 毫秒)。 |
