---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-keycodearray
title: Hid_KeyCodeArray
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Hid_KeyCodeArray
category: harmonyos-references
scraped_at: 2026-04-28T08:10:45+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:eb5bee395c4c9b4e70361f5fd21fc5416af85a02f545df2c0e951114c052968a
---

```
1. typedef struct Hid_KeyCodeArray {...} Hid_KeyCodeArray
```

## 概述

PC/2in1

键值属性数组。

**起始版本：** 11

**相关模块：** [HidDdk](capi-hidddk.md)

**所在头文件：** [hid\_ddk\_types.h](capi-hid-ddk-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| Hid\_KeyCode\* hidKeyCode | 键值编码 |
| uint16\_t length | 数组的有效长度 |
