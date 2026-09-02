---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-devicememmap
title: ScsiPeripheral_DeviceMemMap
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_DeviceMemMap
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bee620f6f39ead0196a851e5868879afdac4c40c27d05b3dc331289c5302698b
---

```c
typedef struct ScsiPeripheral_DeviceMemMap {...} ScsiPeripheral_DeviceMemMap
```

## 概述

通过调用[OH\_ScsiPeripheral\_CreateDeviceMemMap](capi-scsi-peripheral-api-h.md#oh_scsiperipheral_createdevicememmap)创建的设备内存映射。使用该设备内存映射的缓冲区可以提供更好的性能。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](capi-scsi-peripheral-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t\* const address | 设备内存映射的缓冲区起始地址，指向映射的设备内存空间。该缓冲区用于存储SCSI设备数据，提供高性能的内存访问能力。 |
| const size\_t size | 缓冲区大小，单位：Byte。取值原则：必须大于0。 |
| uint32\_t offset | 缓冲区读写起始偏移量，单位：Byte。默认值为0，表示没有偏移，缓冲区从指定地址开始。取值范围为[0, size]，当需要从缓冲区特定位置开始读写时设置此参数，不同的offset值对应不同的起始读写位置。 |
| uint32\_t bufferLength | 要使用的缓冲区长度，单位：Byte。默认情况下，该值等于缓冲区的大小，表示整个缓冲区都被使用。当只使用缓冲区的一部分时设置此参数，bufferLength加offset的值应小于等于size。 |
| uint32\_t transferredLength | 已传输数据的长度，单位：Byte。初始值为0，表示尚未传输任何数据。该字段在SCSI数据传输完成后更新，表示实际传输的数据量，可用于监控传输进度。 |
