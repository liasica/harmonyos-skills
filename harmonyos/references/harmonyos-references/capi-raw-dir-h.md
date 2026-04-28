---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-raw-dir-h
title: raw_dir.h
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 头文件 > raw_dir.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c2f40b05b3832a8735ebe00ea2e1f97638ec4b0919f8254f55d5a5842fb8fabf
---

## 概述

PhonePC/2in1TabletTVWearable

提供rawfile目录相关功能，包括遍历和关闭rawfile目录。

**引用文件：** <rawfile/raw\_dir.h>

**库：** librawfile.z.so

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 8

**相关模块：** [rawfile](capi-rawfile.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [RawDir](capi-rawfile-rawdir.md) | RawDir | 提供对rawfile目录的访问。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [const char \*OH\_ResourceManager\_GetRawFileName(RawDir \*rawDir, int index)](capi-raw-dir-h.md#oh_resourcemanager_getrawfilename) | 通过索引获取rawfile文件名称。可以使用此方法遍历rawfile目录。 |
| [int OH\_ResourceManager\_GetRawFileCount(RawDir \*rawDir)](capi-raw-dir-h.md#oh_resourcemanager_getrawfilecount) | 获取[RawDir](capi-rawfile-rawdir.md)中的rawfile数量。通过此方法可以获取[OH\_ResourceManager\_GetRawFileName](capi-raw-dir-h.md#oh_resourcemanager_getrawfilename)中可用的索引。 |
| [void OH\_ResourceManager\_CloseRawDir(RawDir \*rawDir)](capi-raw-dir-h.md#oh_resourcemanager_closerawdir) | 关闭已打开的[RawDir](capi-rawfile-rawdir.md)并释放所有相关联资源。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_ResourceManager\_GetRawFileName()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_ResourceManager_GetRawFileName(RawDir *rawDir, int index)
```

**描述**

通过索引获取rawfile文件名称。可以使用此方法遍历rawfile目录。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [RawDir](capi-rawfile-rawdir.md) \*rawDir | 表示指向[RawDir](capi-rawfile-rawdir.md)的指针。 |
| int index | 表示文件在[RawDir](capi-rawfile-rawdir.md)中的索引位置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char \* | 通过索引返回文件名称，此返回值可以作为[OH\_ResourceManager\_OpenRawFile](capi-raw-file-manager-h.md#oh_resourcemanager_openrawfile)的输入参数。  如果遍历完所有文件仍未找到，则返回NULL。 |

**参考：**

[OH\_ResourceManager\_OpenRawFile](capi-raw-file-manager-h.md#oh_resourcemanager_openrawfile)

### OH\_ResourceManager\_GetRawFileCount()

PhonePC/2in1TabletTVWearable

```
1. int OH_ResourceManager_GetRawFileCount(RawDir *rawDir)
```

**描述**

获取[RawDir](capi-rawfile-rawdir.md)中的rawfile数量。通过此方法可以获取[OH\_ResourceManager\_GetRawFileName](capi-raw-dir-h.md#oh_resourcemanager_getrawfilename)中可用的索引。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [RawDir](capi-rawfile-rawdir.md) \*rawDir | 表示指向[RawDir](capi-rawfile-rawdir.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回rawDir下的文件个数。如果rawDir为空时返回0。 |

**参考：**

[OH\_ResourceManager\_GetRawFileName](capi-raw-dir-h.md#oh_resourcemanager_getrawfilename)

### OH\_ResourceManager\_CloseRawDir()

PhonePC/2in1TabletTVWearable

```
1. void OH_ResourceManager_CloseRawDir(RawDir *rawDir)
```

**描述**

关闭已打开的[RawDir](capi-rawfile-rawdir.md)并释放所有相关联资源。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [RawDir](capi-rawfile-rawdir.md) \*rawDir | 表示指向[RawDir](capi-rawfile-rawdir.md)的指针。 |

**参考：**

[OH\_ResourceManager\_OpenRawDir](capi-raw-file-manager-h.md#oh_resourcemanager_openrawdir)
