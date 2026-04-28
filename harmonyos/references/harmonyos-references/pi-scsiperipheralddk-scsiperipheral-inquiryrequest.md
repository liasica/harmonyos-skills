---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-scsiperipheralddk-scsiperipheral-inquiryrequest
title: ScsiPeripheral_InquiryRequest
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_InquiryRequest
category: harmonyos-references
scraped_at: 2026-04-28T08:10:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a6e2e242477bec2fc19d80986a7e1fb873afdba224e4cfb5b1669385a0ff4df3
---

```
1. typedef struct ScsiPeripheral_InquiryRequest {...} ScsiPeripheral_InquiryRequest
```

## 概述

PC/2in1

SCSI命令（inquiry）的请求结构体。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](capi-scsi-peripheral-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint8\_t pageCode | Page code字段。获取设备的某些特定类型的信息时使用。当发出带有特定页面代码的 Inquiry 命令时，设备会返回与该页面代码相关的详细信息。如果 page code 设置为 0x00，则表示请求的是标准的 Inquiry 数据，而非特定页面的数据。 |
| uint16\_t allocationLength | Allocation length字段，指定了请求方向发起者（通常是主机）为响应数据准备的缓冲区大小。 |
| uint8\_t control | Control字段，用于指定一些控制信息。 |
| uint8\_t byte1 | CDB的第一个字节。 |
| uint32\_t timeout | 超时时间(单位: 毫秒)。 |
