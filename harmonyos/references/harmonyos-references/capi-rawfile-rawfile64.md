---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawfile64
title: RawFile64
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 结构体 > RawFile64
category: harmonyos-references
scraped_at: 2026-09-02T14:52:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6af217e7f1f51a7522c8cf351f55999cf60baa235123cf91248cb527f93e1133
---

```c
typedef struct RawFile64 RawFile64
```

## 概述

RawFile64表示一个已打开的rawfile对象，用于访问2GB及以上的大文件。通过[OH\_ResourceManager\_OpenRawFile64](capi-raw-file-manager-h.md#oh_resourcemanager_openrawfile64)函数获取，使用完后须调用[OH\_ResourceManager\_CloseRawFile64](capi-raw-file-h.md#oh_resourcemanager_closerawfile64)关闭并释放。

**起始版本：** 11

**相关模块：** [rawfile](capi-rawfile.md)

**所在头文件：** [raw\_file.h](capi-raw-file-h.md)
