---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawfiledescriptor64
title: RawFileDescriptor64
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 结构体 > RawFileDescriptor64
category: harmonyos-references
scraped_at: 2026-04-28T08:06:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4293698bb55141f2a26f63c65b1d3bb10154d1ab65297d405fafe3dc5418d261
---

```
1. typedef struct {...} RawFileDescriptor64
```

## 概述

PhonePC/2in1TabletTVWearable

提供较大rawfile文件描述符信息。RawFileDescriptor64是[OH\_ResourceManager\_GetRawFileDescriptor64](capi-raw-file-h.md#oh_resourcemanager_getrawfiledescriptor64)的输出参数,涵盖了rawfile文件的文件描述符以及在HAP包中的起始位置和长度。

**起始版本：** 11

**相关模块：** [rawfile](capi-rawfile.md)

**所在头文件：** [raw\_file.h](capi-raw-file-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int fd | rawfile文件描述符，单位为int。 |
| int64\_t start | rawfile在HAP包中的起始位置，单位为int64\_t。 |
| int64\_t length | rawfile在HAP包中的长度，单位为int64\_t。 |
