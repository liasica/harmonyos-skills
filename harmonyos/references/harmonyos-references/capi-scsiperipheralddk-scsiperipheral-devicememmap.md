---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-devicememmap
title: ScsiPeripheral_DeviceMemMap
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_DeviceMemMap
category: harmonyos-references
scraped_at: 2026-04-29T14:01:27+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:ea73ea37fff2e50e2c789db92e9074419cf9a32f18f8491ef4c36336b17b2287
---

```
1. typedef struct ScsiPeripheral_DeviceMemMap {...} ScsiPeripheral_DeviceMemMap
```

## 概述

PC/2in1

通过调用[OH\_ScsiPeripheral\_CreateDeviceMemMap](capi-scsi-peripheral-api-h.md#oh_scsiperipheral_createdevicememmap)创建的设备内存映射。使用该设备内存映射的缓冲区可以提供更好的性能。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](capi-scsi-peripheral-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint8\_t\* const address | 缓冲区地址。 |
| const size\_t size | 缓冲区大小。 |
| uint32\_t offset | 已使用缓冲区的偏移量。默认值为0，表示没有偏移，缓冲区从指定地址开始。 |
| uint32\_t bufferLength | 已使用缓冲区的长度。默认情况下，该值等于缓冲区的大小，表示整个缓冲区都被使用。 |
| uint32\_t transferredLength | 已传输数据的长度。 |
