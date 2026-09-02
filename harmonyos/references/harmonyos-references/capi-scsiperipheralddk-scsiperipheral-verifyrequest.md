---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-verifyrequest
title: ScsiPeripheral_VerifyRequest
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_VerifyRequest
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:66121af0e49386e5f148ca4c1c21ac61645258a8d31467bba6bf45895da312eb
---

```c
typedef struct ScsiPeripheral_VerifyRequest {...} ScsiPeripheral_VerifyRequest
```

## 概述

SCSI命令（VERIFY）的请求结构体，该命令通常用于校验逻辑块的数据完整性。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](capi-scsi-peripheral-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t lbAddress | 起始逻辑块地址。 |
| uint16\_t verificationLength | 要校验的连续逻辑块的数量。 |
| uint8\_t control | Control字段，用于指定SCSI命令的控制信息。 |
| uint8\_t byte1 | CDB（Command Descriptor Block，命令描述符块）的第一个字节。 |
| uint8\_t byte6 | CDB（Command Descriptor Block，命令描述符块）的第六个字节。 |
| uint32\_t timeout | 超时时间（单位：ms）。 |
