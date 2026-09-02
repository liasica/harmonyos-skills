---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawfiledescriptor
title: RawFileDescriptor
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 结构体 > RawFileDescriptor
category: harmonyos-references
scraped_at: 2026-09-02T15:01:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8a22dfe4d1a2e01b652052a3fa435843646bdb3e568c5aef797c2585257240c7
---

```c
typedef struct {...} RawFileDescriptor
```

## 概述

提供rawfile文件描述符信息，包含rawfile的文件描述符、在HAP包中的起始位置和文件长度。

通过[OH\_ResourceManager\_GetRawFileDescriptorData](capi-raw-file-h.md#oh_resourcemanager_getrawfiledescriptordata)获取，使用完后须调用[OH\_ResourceManager\_ReleaseRawFileDescriptorData](capi-raw-file-h.md#oh_resourcemanager_releaserawfiledescriptordata)释放文件描述符资源。

**起始版本：** 8

**相关模块：** [rawfile](capi-rawfile.md)

**所在头文件：** [raw\_file.h](capi-raw-file-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int fd | rawfile文件描述符。 |
| long start | rawfile文件在HAP包中的起始位置，单位为Byte。 |
| long length | rawfile文件的长度，单位为Byte。 |
