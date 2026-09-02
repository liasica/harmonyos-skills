---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-emititem
title: Hid_EmitItem
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Hid_EmitItem
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:10d1399824d1871ada59e468b5ba5cdb61b2185feb381ec8337e54885a321339
---

```c
typedef struct Hid_EmitItem {...} Hid_EmitItem
```

## 概述

表示HID事件信息结构体，包含事件类型、事件编码和事件值，用于描述输入设备的上报事件。在驱动开发场景中，该结构体用于传递和识别各类HID设备产生的事件。

**起始版本：** 11

**相关模块：** [HidDdk](capi-hidddk.md)

**所在头文件：** [hid\_ddk\_types.h](capi-hid-ddk-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint16\_t type | HID事件类型，用于标识事件类别，如按键、移动等。取值范围参考HID协议规范。 |
| uint16\_t code | HID事件编码，用于标识具体的HID事件。取值范围参考HID协议规范。 |
| uint32\_t value | HID事件值，表示事件的参数或状态，具体含义取决于事件类型和编码。例如：对于按键事件，表示按键状态；对于移动事件，表示移动距离等。 |
