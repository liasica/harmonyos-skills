---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawfile
title: RawFile
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 结构体 > RawFile
category: harmonyos-references
scraped_at: 2026-09-02T14:52:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e57769773b4f7c906605f09027dd09de506e48d0b37c09d83efd8d741c774957
---

```c
typedef struct RawFile RawFile
```

## 概述

RawFile表示一个已打开的rawfile对象。通过[OH\_ResourceManager\_OpenRawFile](capi-raw-file-manager-h.md#oh_resourcemanager_openrawfile)函数获取，使用完后须调用[OH\_ResourceManager\_CloseRawFile](capi-raw-file-h.md#oh_resourcemanager_closerawfile)关闭并释放。

**起始版本：** 8

**相关模块：** [rawfile](capi-rawfile.md)

**所在头文件：** [raw\_file.h](capi-raw-file-h.md)
