---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawfiledescriptor
title: RawFileDescriptor
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 结构体 > RawFileDescriptor
category: harmonyos-references
scraped_at: 2026-04-28T08:06:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1e489e239256292151736ddf3eb1d58a281b0fd1f27116f279a48edc4ee7395c
---

```
1. typedef struct {...} RawFileDescriptor
```

## 概述

PhonePC/2in1TabletTVWearable

提供rawfile文件描述符信息。RawFileDescriptor是[OH\_ResourceManager\_GetRawFileDescriptor](capi-raw-file-h.md#oh_resourcemanager_getrawfiledescriptor)的输出参数，涵盖了rawfile文件的文件描述符以及在HAP包中的起始位置和长度。

**起始版本：** 8

**相关模块：** [rawfile](capi-rawfile.md)

**所在头文件：** [raw\_file.h](capi-raw-file-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int fd | rawfile文件描述符，单位为int。 |
| long start | rawfile在HAP包中的起始位置，单位为long。 |
| long length | rawfile在HAP包中的长度，单位为long。 |
