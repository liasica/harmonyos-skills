---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-inquiryinfo
title: ScsiPeripheral_InquiryInfo
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_InquiryInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:134c1d810c08dd1753364a9a9eb7f52ae1091e261ab383198d16a68f84e163e1
---

```c
typedef struct ScsiPeripheral_InquiryInfo {...} ScsiPeripheral_InquiryInfo
```

## 概述

SCSI INQUIRY 数据，用于存储SCSI外设的INQUIRY命令查询结果。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](capi-scsi-peripheral-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t deviceType | SCSI外设的设备类型，具体类型值定义参见SCSI标准协议。 |
| char idVendor[[SCSIPERIPHERAL\_VENDOR\_ID\_LEN](capi-scsi-peripheral-types-h.md#宏定义) + 1] | 制造商 ID。 |
| char idProduct[[SCSIPERIPHERAL\_PRODUCT\_ID\_LEN](capi-scsi-peripheral-types-h.md#宏定义) + 1] | 产品 ID。 |
| char revProduct[[SCSIPERIPHERAL\_PRODUCT\_REV\_LEN](capi-scsi-peripheral-types-h.md#宏定义) + 1] | 产品版本。 |
| [ScsiPeripheral\_DeviceMemMap](capi-scsiperipheralddk-scsiperipheral-devicememmap.md)\* data | 指向设备内存映射的指针，用于存储查询得到的数据。 |
