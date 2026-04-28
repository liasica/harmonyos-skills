---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/siperipheralddk-scsiperipheral-readcapacityrequest
title: ScsiPeripheral_ReadCapacityRequest
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_ReadCapacityRequest
category: harmonyos-references
scraped_at: 2026-04-28T08:10:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c225c6b68f5c3f4ddf11c1ef0ce6c2c54ff93e1fc42d7a218f5288034edf8e11
---

```
1. typedef struct ScsiPeripheral_ReadCapacityRequest {...} ScsiPeripheral_ReadCapacityRequest
```

## 概述

PC/2in1

SCSI命令（read capacity）的请求结构体。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](capi-scsi-peripheral-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint32\_t lbAddress | 逻辑单元地址。 |
| uint8\_t control | Control字段，用于指定一些控制信息。 |
| uint8\_t byte8 | CDB的第八个字节。 |
| uint32\_t timeout | 超时时间（单位: 毫秒）。 |
