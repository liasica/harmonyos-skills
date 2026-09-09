---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-telephony-data-h
title: telephony_data.h
breadcrumb: API参考 > 系统 > 网络 > Telephony Kit（蜂窝通信服务） > C API > 头文件 > telephony_data.h
category: harmonyos-references
scraped_at: 2026-09-10T06:27:22+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:9cb7f87fe15c1960900431ba178af0506bcfdffb98e20188ac440a1b2598b053
---

## 概述

为电话蜂窝数据定义C接口。

**引用文件：** <telephony/cellular\_data/telephony\_data.h>

**库：** libtelephony\_data.so

**系统能力：** SystemCapability.Telephony.CellularData

**起始版本：** 13

**相关模块：** [Telephony](capi-telephony.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [int32\_t OH\_Telephony\_GetDefaultCellularDataSlotId(void)](capi-telephony-data-h.md#oh_telephony_getdefaultcellulardataslotid) | 获取默认移动数据的SIM卡接口。 |

## 函数说明

### OH\_Telephony\_GetDefaultCellularDataSlotId()

```c
int32_t OH_Telephony_GetDefaultCellularDataSlotId(void)
```

**描述**

获取默认移动数据的SIM卡接口。

**系统能力：** SystemCapability.Telephony.CellularData

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 默认移动数据的卡槽（0表示卡槽1，1表示卡槽2）。 |
