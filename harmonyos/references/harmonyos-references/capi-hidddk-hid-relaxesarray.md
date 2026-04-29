---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-relaxesarray
title: Hid_RelAxesArray
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Hid_RelAxesArray
category: harmonyos-references
scraped_at: 2026-04-29T14:01:27+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:9c04592d501ea56740c4a4ba2fe38e1bf3c37bdb980bfff8ece5405d596511b2
---

```
1. typedef struct Hid_RelAxesArray {...} Hid_RelAxesArray
```

## 概述

PC/2in1

相对坐标属性数组。

**起始版本：** 11

**相关模块：** [HidDdk](capi-hidddk.md)

**所在头文件：** [hid\_ddk\_types.h](capi-hid-ddk-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| [Hid\_RelAxes](capi-hid-ddk-types-h.md#hid_relaxes)\* hidRelAxes | 相对坐标属性编码 |
| uint16\_t length | 数组的有效长度 |
