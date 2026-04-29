---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-eventtypearray
title: Hid_EventTypeArray
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Hid_EventTypeArray
category: harmonyos-references
scraped_at: 2026-04-29T14:01:26+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:d99a71fc48dc47a790cb47478952d55a5543795a66e2089102f544cd8ac44e91
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
| [Hid\_EventType](capi-hid-ddk-types-h.md#hid_eventtype)\* hidEventType | 事件类型编码 |
| uint16\_t length | 数组的有效长度 |
