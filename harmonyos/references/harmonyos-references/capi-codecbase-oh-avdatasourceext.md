---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase-oh-avdatasourceext
title: OH_AVDataSourceExt
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 结构体 > OH_AVDataSourceExt
category: harmonyos-references
scraped_at: 2026-09-02T15:02:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:11895219d93e5085e5ebc3c017de01e004793df2cca140f023d290679bb0cafd
---

```c
typedef struct OH_AVDataSourceExt {...} OH_AVDataSourceExt
```

## 概述

用户自定义数据源，回调支持通过userData传递用户自定义数据。

**起始版本：** 20

**相关模块：** [CodecBase](capi-codecbase.md)

**所在头文件：** [native\_avcodec\_base.h](capi-native-avcodec-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int64\_t size | 数据源的总大小，单位为字节。 |
| [OH\_AVDataSourceReadAtExt](capi-native-avcodec-base-h.md#oh_avdatasourcereadatext) readAt | 数据源的数据读取回调。 |
