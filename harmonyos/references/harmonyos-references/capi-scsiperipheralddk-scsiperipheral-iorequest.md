---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-iorequest
title: ScsiPeripheral_IORequest
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_IORequest
category: harmonyos-references
scraped_at: 2026-04-29T14:01:28+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:a3880c3ba834a6eb3db1f3beafaaad7bb50486f858979bd3ea899fe4e3bce4e9
---

```
1. typedef struct ScsiPeripheral_IORequest {...} ScsiPeripheral_IORequest
```

## 概述

PC/2in1

读/写操作的请求参数。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](capi-scsi-peripheral-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint32\_t lbAddress | 逻辑块起始地址。 |
| uint16\_t transferLength | 需要操作的连续逻辑块的数量。 |
| uint8\_t control | Control字段，用于指定一些控制信息。 |
| uint8\_t byte1 | CDB的第一个字节。 |
| uint8\_t byte6 | CDB的第六个字节。 |
| [ScsiPeripheral\_DeviceMemMap](capi-scsiperipheralddk-scsiperipheral-devicememmap.md)\* data | 数据传输的缓冲区。 |
| uint32\_t timeout | 超时时间（单位：毫秒）。 |
