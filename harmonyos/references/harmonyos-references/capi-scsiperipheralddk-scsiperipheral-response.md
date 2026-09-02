---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-response
title: ScsiPeripheral_Response
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_Response
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0631869d339c070b64b07462880ff20a7cf4170136739249a4faf0e51f89851a
---

```c
typedef struct ScsiPeripheral_Response {...} ScsiPeripheral_Response
```

## 概述

SCSI响应参数结构体，包含状态、错误诊断数据、传输结果等，用于接收SCSI设备响应数据、判断命令是否成功。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](capi-scsi-peripheral-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t senseData[[SCSIPERIPHERAL\_MAX\_SENSE\_DATA\_LEN](capi-scsi-peripheral-types-h.md#宏定义)] | Sense Data，SCSI设备返回给主机的状态、错误及诊断信息。 |
| [ScsiPeripheral\_Status](capi-scsi-peripheral-types-h.md#scsiperipheral_status) status | 调用完成时的状态。可能的值包括：SCSIPERIPHERAL\_STATUS\_GOOD（正常状态）、SCSIPERIPHERAL\_STATUS\_BUSY（占用中）等。 |
| uint8\_t maskedStatus | 在SCSI通用驱动中，该字段用于存储经掩码处理后的SCSI状态。 |
| uint8\_t msgStatus | 消息状态，表示SCSI命令执行完成后的消息结果。 |
| uint8\_t sbLenWr | 实际写入到Sense Buffer（感知缓冲区）的有效字节数，用于确定senseData数组中有效数据的长度，若为0表示无Sense Data。 |
| uint16\_t hostStatus | 主机适配器状态。例如：成功（0x00）、无法连接（0x01）、总线忙（0x02）、超时（0x03）。 |
| uint16\_t driverStatus | 驱动状态。例如：成功（0x00）、设备或资源忙（0x01）。 |
| int32\_t resId | 实际传输的数据长度差值，即未传输的字节数。 |
| uint32\_t duration | 执行SCSI命令消耗的时间（单位：ms）。 |
