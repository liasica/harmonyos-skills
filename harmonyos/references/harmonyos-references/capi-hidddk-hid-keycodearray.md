---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-keycodearray
title: Hid_KeyCodeArray
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Hid_KeyCodeArray
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:54bff6306ceedea4695b3701a6249ed9f7a810d519b9c0d3ae8a1551fed89c60
---

```c
typedef struct Hid_KeyCodeArray {...} Hid_KeyCodeArray
```

## 概述

键值属性编码数组，用于存储HID设备支持的键值编码信息。

**起始版本：** 11

**相关模块：** [HidDdk](capi-hidddk.md)

**所在头文件：** [hid\_ddk\_types.h](capi-hid-ddk-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Hid\_KeyCode](capi-hid-ddk-types-h.md#hid_keycode)\* hidKeyCode | 键值属性编码数组的指针，指向调用方预先分配的数组（不允许为空指针），数组大小不小于length。 |
| uint16\_t length | 数组的有效长度，不超过hidKeyCode数组的实际长度。 |
