---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-emititem
title: Hid_EmitItem
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Hid_EmitItem
category: harmonyos-references
scraped_at: 2026-04-28T08:10:44+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c083af97ae3efe2aaa54196458becdde78e2662bc9f2b430e14e2d1fec7a9229
---

```
1. typedef struct Hid_EmitItem {...} Hid_EmitItem
```

## 概述

PC/2in1

事件信息。

**起始版本：** 11

**相关模块：** [HidDdk](capi-hidddk.md)

**所在头文件：** [hid\_ddk\_types.h](capi-hid-ddk-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint16\_t type | 事件类型 |
| uint16\_t code | 事件编码 |
| uint32\_t value | 事件值 |
