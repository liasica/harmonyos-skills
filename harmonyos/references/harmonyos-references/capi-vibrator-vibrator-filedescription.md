---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vibrator-vibrator-filedescription
title: Vibrator_FileDescription
breadcrumb: API参考 > 系统 > 硬件 > Sensor Service Kit（传感器服务） > C API > 结构体 > Vibrator_FileDescription
category: harmonyos-references
scraped_at: 2026-04-28T08:11:12+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0309d766ed897916175ed2e1bcb292a37ea11c1f101d6b4b6c0b462f03829d8f
---

```
1. typedef struct Vibrator_FileDescription { ... } Vibrator_FileDescription
```

## 概述

PhonePC/2in1TabletTVWearable

振动文件描述。

**起始版本：** 11

**相关模块：** [Vibrator](capi-vibrator.md)

**所在头文件：** [vibrator\_type.h](capi-vibrator-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t fd | 自定义振动序列的文件句柄。 |
| int64\_t offset | 自定义振动序列的偏移地址。 |
| int64\_t length | 自定义振动序列的总长度。 |
