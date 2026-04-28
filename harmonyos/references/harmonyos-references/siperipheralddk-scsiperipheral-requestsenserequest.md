---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/siperipheralddk-scsiperipheral-requestsenserequest
title: ScsiPeripheral_RequestSenseRequest
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_RequestSenseRequest
category: harmonyos-references
scraped_at: 2026-04-28T08:10:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4cb16c32356da7600f5fab61cc5e2ce4cef2c5f5bd97d57c0f646eb2a4932a21
---

```
1. typedef struct ScsiPeripheral_RequestSenseRequest {...} ScsiPeripheral_RequestSenseRequest
```

## 概述

PC/2in1

SCSI命令（Request Sense）的请求结构体。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](capi-scsi-peripheral-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint8\_t allocationLength | Allocation length字段，指定了请求方向发起者（通常是主机）为响应数据准备的缓冲区大小。 |
| uint8\_t control | Control字段，用于指定一些控制信息。 |
| uint8\_t byte1 | CDB的第一个字节。 |
| uint32\_t timeout | 超时时间(单位: 毫秒)。 |
