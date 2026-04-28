---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase-oh-avdatasource
title: OH_AVDataSource
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 结构体 > OH_AVDataSource
category: harmonyos-references
scraped_at: 2026-04-28T08:12:08+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:653a6c999cf442678043f8ec24dca877b2b6463c566b2d05e55f171b402b145e
---

```
1. typedef struct OH_AVDataSource {...} OH_AVDataSource
```

## 概述

PhonePC/2in1TabletTVWearable

用户自定义数据源。

**起始版本：** 12

**相关模块：** [CodecBase](capi-codecbase.md)

**所在头文件：** [native\_avcodec\_base.h](capi-native-avcodec-base-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int64\_t size | 数据源的总大小。 |
| [OH\_AVDataSourceReadAt](capi-native-avcodec-base-h.md#oh_avdatasourcereadat) readAt | 数据源的数据回调。 |
