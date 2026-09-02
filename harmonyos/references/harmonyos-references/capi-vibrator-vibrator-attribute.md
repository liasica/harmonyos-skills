---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vibrator-vibrator-attribute
title: Vibrator_Attribute
breadcrumb: API参考 > 系统 > 硬件 > Sensor Service Kit（传感器服务） > C API > 结构体 > Vibrator_Attribute
category: harmonyos-references
scraped_at: 2026-09-02T15:02:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c84ba5a7eafc00d62180a2dd5ba189d7480ff1f41b6ba04b612af65e49325713
---

```c
typedef struct Vibrator_Attribute { ... } Vibrator_Attribute
```

## 概述

Vibrator\_Attribute结构体用于描述马达的属性信息。开发者使用该结构体可以指定马达ID和振动场景。具体使用场景和实现机制请参见[Vibrator](capi-vibrator.md)模块文档。

**起始版本：** 11

**相关模块：** [Vibrator](capi-vibrator.md)

**所在头文件：** [vibrator\_type.h](capi-vibrator-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t vibratorId | 马达ID，取值原则：通过系统接口获取有效值。指定要操作的马达设备标识，不同ID对应设备上不同的马达。取值范围为[0, 最大支持的马达数-1]。 |
| [Vibrator\_Usage](capi-vibrator-type-h.md#vibrator_usage) usage | 振动场景。指定振动的应用场景，不同场景对应不同的振动模式（如通知、按键、闹钟等各有相应的振动效果），可选值见Vibrator\_Usage枚举定义。 |
