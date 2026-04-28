---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-inquiryinfo
title: ScsiPeripheral_InquiryInfo
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_InquiryInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:10:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d9e46b426273ffd7f8e586dad5d9f1e53630042ec0a19888963ee539f7743f53
---

```
1. typedef struct ScsiPeripheral_InquiryInfo {...} ScsiPeripheral_InquiryInfo
```

## 概述

PC/2in1

SCSI inquiry 数据。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](capi-scsi-peripheral-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint8\_t deviceType | 设备类型。 |
| char idVendor[[SCSIPERIPHERAL\_VENDOR\_ID\_LEN](capi-scsi-peripheral-types-h.md) + 1] | 制造商 id。 |
| char idProduct[[SCSIPERIPHERAL\_PRODUCT\_ID\_LEN](capi-scsi-peripheral-types-h.md) + 1] | 产品 id。 |
| char revProduct[[SCSIPERIPHERAL\_PRODUCT\_REV\_LEN](capi-scsi-peripheral-types-h.md) + 1] | 产品版本。 |
| ScsiPeripheral\_DeviceMemMap\* data | 所有的查询数据。 |
