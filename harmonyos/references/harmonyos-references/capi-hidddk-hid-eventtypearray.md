---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-eventtypearray
title: Hid_EventTypeArray
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Hid_EventTypeArray
category: harmonyos-references
scraped_at: 2026-04-28T08:10:45+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:8b6e1fe4d4e24ebb6b9b20c7e4054dba3af0dd50139e791b0946761eaec5c687
---

```
1. typedef struct Hid_EventTypeArray {...} Hid_EventTypeArray
```

## 概述

PC/2in1

事件类型编码数组。

**起始版本：** 11

**相关模块：** [HidDdk](capi-hidddk.md)

**所在头文件：** [hid\_ddk\_types.h](capi-hid-ddk-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| Hid\_EventType\* hidEventType | 事件类型编码 |
| uint16\_t length | 数组的有效长度 |
