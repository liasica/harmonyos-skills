---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-absaxesarray
title: Hid_AbsAxesArray
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Hid_AbsAxesArray
category: harmonyos-references
scraped_at: 2026-04-28T08:10:46+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:11e58c357914ddf0f4d94dafef2b0339b5026352db8f84c3e5c13fb2a5e775fe
---

```
1. typedef struct Hid_AbsAxesArray {...} Hid_AbsAxesArray
```

## 概述

PC/2in1

绝对坐标属性数组。

**起始版本：** 11

**相关模块：** [HidDdk](capi-hidddk.md)

**所在头文件：** [hid\_ddk\_types.h](capi-hid-ddk-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| Hid\_AbsAxes\* hidAbsAxes | 绝对坐标属性编码 |
| uint16\_t length | 数组的有效长度 |
