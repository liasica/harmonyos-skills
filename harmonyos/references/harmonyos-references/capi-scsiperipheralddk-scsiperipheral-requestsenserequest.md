---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-requestsenserequest
title: ScsiPeripheral_RequestSenseRequest
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_RequestSenseRequest
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c913c6367c764724bf6f5ec0242c83970da2f7fca254e2ebb9a6e1b4a9e53262
---

```c
typedef struct ScsiPeripheral_RequestSenseRequest {...} ScsiPeripheral_RequestSenseRequest
```

## 概述

SCSI命令（REQUEST SENSE）的请求结构体，该命令通常用于获取设备的错误信息。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](capi-scsi-peripheral-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t allocationLength | Allocation length字段，指定了请求发起者（通常是主机）为响应数据准备的缓冲区大小，单位：Byte。 |
| uint8\_t control | Control字段，用于指定SCSI命令的控制信息。 |
| uint8\_t byte1 | CDB（Command Descriptor Block，命令描述符块）的第一个字节。 |
| uint32\_t timeout | 超时时间（单位：ms）。 |
