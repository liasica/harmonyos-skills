---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-capacityinfo
title: ScsiPeripheral_CapacityInfo
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_CapacityInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1d3c09dfe44e07f6bd1b25d2e27166b3b93cc1ca24d37a84611a43f9c1daab84
---

```c
typedef struct ScsiPeripheral_CapacityInfo {...} ScsiPeripheral_CapacityInfo
```

## 概述

SCSI READ CAPACITY结构体。用于在开发SCSI设备驱动时获取设备的存储容量信息，支持进行分区管理、可用空间检查和存储资源分配等操作。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](capi-scsi-peripheral-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t lbAddress | 返回的逻辑块地址，表示可寻址的最后一块逻辑块的编号，逻辑块总数为该值加1。 |
| uint32\_t lbLength | 单个逻辑块长度（单位：Byte）。表示每个逻辑块的字节大小，通常为512、2048或4096等标准值，具体取决于设备类型和格式化方式。 |
