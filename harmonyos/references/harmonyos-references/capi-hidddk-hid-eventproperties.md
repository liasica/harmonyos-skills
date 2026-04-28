---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-eventproperties
title: Hid_EventProperties
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Hid_EventProperties
category: harmonyos-references
scraped_at: 2026-04-28T08:10:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4726fd21582f8d88d6cfada1c77c5aacb35995512ef2c629b9b894a921b72be2
---

```
1. typedef struct Hid_EventProperties {...} Hid_EventProperties
```

## 概述

PC/2in1

设备关注事件属性。

**起始版本：** 11

**相关模块：** [HidDdk](capi-hidddk.md)

**所在头文件：** [hid\_ddk\_types.h](capi-hid-ddk-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| struct Hid\_EventTypeArray hidEventTypes | 事件类型属性编码数组 |
| struct Hid\_KeyCodeArray hidKeys | 键值属性编码数组 |
| struct Hid\_AbsAxesArray hidAbs | 绝对坐标属性编码数组 |
| struct Hid\_RelAxesArray hidRelBits | 相对坐标属性编码数组 |
| struct Hid\_MscEventArray hidMiscellaneous | 其它特殊事件属性编码数组 |
| int32\_t hidAbsMax[64] | 绝对坐标属性最大值 |
| int32\_t hidAbsMin[64] | 绝对坐标属性最小值 |
| int32\_t hidAbsFuzz[64] | 绝对坐标属性模糊值 |
| int32\_t hidAbsFlat[64] | 绝对坐标属性固定值 |
