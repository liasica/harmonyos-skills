---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-scsiperipheralddk-scsiperipheral-basicsenseinfo
title: ScsiPeripheral_BasicSenseInfo
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_BasicSenseInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:10:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d8195ef50ea30d96313f3d337696ff59f74119db5dd33de8fa6fc63bc1fdb107
---

```
1. typedef struct ScsiPeripheral_BasicSenseInfo {...} ScsiPeripheral_BasicSenseInfo
```

## 概述

PC/2in1

sense data的基本信息。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](capi-scsi-peripheral-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint8\_t responseCode | 响应码。 |
| bool valid | 信息有效标志位。 |
| uint64\_t information | Information字段。 |
| uint64\_t commandSpecific | Command-specific information字段。 |
| bool sksv | Sense key specific字段的标志位。 |
| uint32\_t senseKeySpecific | Sense key specific字段。 |
