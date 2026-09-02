---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-basicsenseinfo
title: ScsiPeripheral_BasicSenseInfo
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_BasicSenseInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bd4f5fa129921758698a87d1055d05358b4d84526dafc2546aa712ab0ea1f717
---

```c
typedef struct ScsiPeripheral_BasicSenseInfo {...} ScsiPeripheral_BasicSenseInfo
```

## 概述

SCSI Sense Data的基本信息结构体，用于封装SCSI命令执行后返回的sense数据。该结构体包含响应码、状态标志位以及各类信息字段，用于驱动程序获取和分析SCSI设备的错误状态和命令执行结果。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](capi-scsi-peripheral-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t responseCode | 响应码。由驱动层在收到Sense Data时自动设置。 |
| bool valid | 信息有效标志位。为true时表示information和commandSpecific字段有效，为false时这些字段应被忽略。使用前应先检查此标志位以避免读取无效数据。 |
| uint64\_t information | Information字段，取值遵循SCSI标准协议。 |
| uint64\_t commandSpecific | Command-specific information字段，取值遵循SCSI标准协议。 |
| bool sksv | Sense key specific字段的标志位。当为true时，表示senseKeySpecific字段有效，包含sense key specific data；为false时应忽略senseKeySpecific字段。使用前应先检查此标志位以避免读取无效数据。 |
| uint32\_t senseKeySpecific | Sense key specific字段，取值遵循SCSI标准协议。 |
