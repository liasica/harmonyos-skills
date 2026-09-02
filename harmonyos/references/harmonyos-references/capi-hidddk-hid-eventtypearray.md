---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-eventtypearray
title: Hid_EventTypeArray
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Hid_EventTypeArray
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4eda5e32eb889d3ef15120fbcb3c57a57591c02f98a5f449561da77093c06106
---

```c
typedef struct Hid_EventTypeArray {...} Hid_EventTypeArray
```

## 概述

事件类型编码数组，用于存储HID设备支持的事件类型信息。

**起始版本：** 11

**相关模块：** [HidDdk](capi-hidddk.md)

**所在头文件：** [hid\_ddk\_types.h](capi-hid-ddk-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Hid\_EventType](capi-hid-ddk-types-h.md#hid_eventtype)\* hidEventType | 事件类型编码数组的指针，指向调用方预先分配的数组（不允许为空指针），数组大小不小于length。 |
| uint16\_t length | 数组的有效长度，不超过hidEventType数组的实际长度。 |
