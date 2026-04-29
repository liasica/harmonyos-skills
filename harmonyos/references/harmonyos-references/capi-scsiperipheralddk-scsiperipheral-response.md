---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-response
title: ScsiPeripheral_Response
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_Response
category: harmonyos-references
scraped_at: 2026-04-29T14:01:28+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:73df2785c9c8464558ef305f59e098815fa01b8b15d4c993e000edbaba54e872
---

```
1. typedef struct ScsiPeripheral_Response {...} ScsiPeripheral_Response
```

## 概述

PC/2in1

响应参数结构体。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](capi-scsi-peripheral-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint8\_t senseData[[SCSIPERIPHERAL\_MAX\_SENSE\_DATA\_LEN](capi-scsi-peripheral-types-h.md)] | sense data（SCSI设备返回给主机的信息，用于报告设备的状态、错误信息以及诊断信息）。 |
| [ScsiPeripheral\_Status](capi-scsi-peripheral-types-h.md#scsiperipheral_status) status | 调用完成时的状态，例如良好（Good）、忙（Busy）。 |
| uint8\_t maskedStatus | 在Linux的SCSI通用接口（SG）中，masked\_status 字段用于存储经过处理后的SCSI状态，以便应用程序可以更方便地读取和解析。 |
| uint8\_t msgStatus | 消息状态。 |
| uint8\_t sbLenWr | 指的是实际写入到 Sense Buffer（感应缓冲区）的字节数。 |
| uint16\_t hostStatus | 主机适配器状态。 例如：成功(0x00)、无法连接(0x01)、总线忙(0x02)、超时(0x03)。 |
| uint16\_t driverStatus | 驱动状态。 例如：成功（0x00）、设备或资源忙(0x01)。 |
| int32\_t resId | 实际传输的数据长度差值，即未传输的字节数。 |
| uint32\_t duration | 执行命令消耗的时间 (单位: 毫秒)。 |
