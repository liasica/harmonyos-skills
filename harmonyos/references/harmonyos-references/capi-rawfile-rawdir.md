---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawdir
title: RawDir
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 结构体 > RawDir
category: harmonyos-references
scraped_at: 2026-09-02T14:52:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:70e1998ad8ded116667c63b3c71c9327882e17e437f74be7c00c4c7370a31486
---

```c
typedef struct RawDir RawDir
```

## 概述

RawDir表示一个已打开的rawfile目录对象，可用于遍历目录和目录下文件。通过[OH\_ResourceManager\_OpenRawDir](capi-raw-file-manager-h.md#oh_resourcemanager_openrawdir)函数获取，使用完后须调用[OH\_ResourceManager\_CloseRawDir](capi-raw-dir-h.md#oh_resourcemanager_closerawdir)关闭并释放。

**起始版本：** 8

**相关模块：** [rawfile](capi-rawfile.md)

**所在头文件：** [raw\_dir.h](capi-raw-dir-h.md)
