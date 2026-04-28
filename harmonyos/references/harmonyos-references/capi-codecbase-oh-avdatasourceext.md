---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase-oh-avdatasourceext
title: OH_AVDataSourceExt
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 结构体 > OH_AVDataSourceExt
category: harmonyos-references
scraped_at: 2026-04-28T08:12:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:fa09f62f5c1b2da163deeb1fb3527653794b1edd19dd22ec304e5b3597842571
---

```
1. typedef struct OH_AVDataSourceExt {...} OH_AVDataSourceExt
```

## 概述

PhonePC/2in1TabletTVWearable

用户自定义数据源，回调支持通过userData传递用户自定义数据。

**起始版本：** 20

**相关模块：** [CodecBase](capi-codecbase.md)

**所在头文件：** [native\_avcodec\_base.h](capi-native-avcodec-base-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int64\_t size | 数据源的总大小。 |
| [OH\_AVDataSourceReadAtExt](capi-native-avcodec-base-h.md#oh_avdatasourcereadatext) readAt | 数据源的数据回调。 |
