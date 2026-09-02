---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawfiledescriptor64
title: RawFileDescriptor64
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 结构体 > RawFileDescriptor64
category: harmonyos-references
scraped_at: 2026-09-02T15:01:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9eabe374bffac1b815a9da7e502b3bcfb0bfe422b290d2036c0eab0c898d1808
---

```c
typedef struct {...} RawFileDescriptor64
```

## 概述

提供rawfile文件描述符信息，包含rawfile的文件描述符、在HAP包中的起始位置和文件长度。支持2GB以上的大文件。

通过[OH\_ResourceManager\_GetRawFileDescriptor64](capi-raw-file-h.md#oh_resourcemanager_getrawfiledescriptor64)获取，使用完后须调用[OH\_ResourceManager\_ReleaseRawFileDescriptor64](capi-raw-file-h.md#oh_resourcemanager_releaserawfiledescriptor64)释放文件描述符资源。

**起始版本：** 11

**相关模块：** [rawfile](capi-rawfile.md)

**所在头文件：** [raw\_file.h](capi-raw-file-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int fd | rawfile文件描述符。 |
| int64\_t start | rawfile文件在HAP包中的起始位置，单位为Byte。 |
| int64\_t length | rawfile文件的长度，单位为Byte。 |
