---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-msceventarray
title: Hid_MscEventArray
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Hid_MscEventArray
category: harmonyos-references
scraped_at: 2026-04-29T14:01:27+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:111c1ee6d3bfe92ffacca7f34fa9c6791a8e2cc758a86365208857c1d3c12c4d
---

```
1. typedef struct Hid_MscEventArray {...} Hid_MscEventArray
```

## 概述

PC/2in1

其他特殊事件属性数组。

**起始版本：** 11

**相关模块：** [HidDdk](capi-hidddk.md)

**所在头文件：** [hid\_ddk\_types.h](capi-hid-ddk-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| [Hid\_MscEvent](capi-hid-ddk-types-h.md#hid_mscevent)\* hidMscEvent | 其他特殊事件属性编码 |
| uint16\_t length | 数组的有效长度 |
