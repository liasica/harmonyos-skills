---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmedia-base-h
title: avmedia_base.h
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 头文件 > avmedia_base.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fee7c39ec3d8a3057eda326325bf09cccfb05346b7f62cb591e2a083edb6c684
---

## 概述

PhonePC/2in1TabletTVWearable

定义AVMedia的结构体和枚举类型。

**引用文件：** <multimedia/player\_framework/avmedia\_base.h>

**库：** libavmedia\_base.so

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 23

**相关模块：** [AVMediaBase](capi-avmediabase.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVMedia\_SeekMode](capi-avmedia-base-h.md#oh_avmedia_seekmode) | OH\_AVMedia\_SeekMode | 指定时间点和帧对应关系的枚举类型。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_AVMedia\_SeekMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_AVMedia_SeekMode
```

**描述**

指定时间点和帧对应关系的枚举类型。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| OH\_AVMEDIA\_SEEK\_NEXT\_SYNC = 0 | 表示选取传入时间点或之后的关键帧。 |
| OH\_AVMEDIA\_SEEK\_PREVIOUS\_SYNC = 1 | 表示选取传入时间点或之前的关键帧。 |
| OH\_AVMEDIA\_SEEK\_CLOSEST\_SYNC = 2 | 表示选取离传入时间点最近的关键帧。 |
| OH\_AVMEDIA\_SEEK\_CLOSEST = 3 | 表示选取离传入时间点最近的帧，该帧不一定是关键帧。 |
