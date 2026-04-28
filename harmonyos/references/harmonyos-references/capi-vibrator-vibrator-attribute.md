---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vibrator-vibrator-attribute
title: Vibrator_Attribute
breadcrumb: API参考 > 系统 > 硬件 > Sensor Service Kit（传感器服务） > C API > 结构体 > Vibrator_Attribute
category: harmonyos-references
scraped_at: 2026-04-28T08:11:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7b8c52ff8ed9a2efd783ebd543cf5d6ade600ee8d7dabc816310add459d245e1
---

```
1. typedef struct Vibrator_Attribute { ... } Vibrator_Attribute
```

## 概述

PhonePC/2in1TabletTVWearable

马达属性。

**起始版本：** 11

**相关模块：** [Vibrator](capi-vibrator.md)

**所在头文件：** [vibrator\_type.h](capi-vibrator-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t vibratorId | 马达ID |
| [Vibrator\_Usage](capi-vibrator-type-h.md#vibrator_usage) usage | 振动场景 |
