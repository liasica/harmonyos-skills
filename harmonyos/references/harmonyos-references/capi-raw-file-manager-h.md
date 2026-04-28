---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-raw-file-manager-h
title: raw_file_manager.h
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 头文件 > raw_file_manager.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:47174762c0e9681fc6745c43f704225640f3543ba48daa3e263302574495d384
---

## 概述

PhonePC/2in1TabletTVWearable

提供资源管理rawfile相关功能，可以使用ResourceManager打开rawfile进行后续相关操作，像搜索和读取等。

**引用文件：** <rawfile/raw\_file\_manager.h>

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
| [NativeResourceManager](capi-rawfile-nativeresourcemanager.md) | NativeResourceManager | 代表native侧的ResourceManager。此类封装了JavaScript resource manager的native实现，**ResourceManager**指针可以通过调用[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [NativeResourceManager \*OH\_ResourceManager\_InitNativeResourceManager(napi\_env env, napi\_value jsResMgr)](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager) | 基于JavaScript侧的ResourceManager获取native侧的ResourceManager，用来完成rawfile相关功能。 |
| [void OH\_ResourceManager\_ReleaseNativeResourceManager(NativeResourceManager \*resMgr)](capi-raw-file-manager-h.md#oh_resourcemanager_releasenativeresourcemanager) | 释放native侧ResourceManager。 |
| [RawDir \*OH\_ResourceManager\_OpenRawDir(const NativeResourceManager \*mgr, const char \*dirName)](capi-raw-file-manager-h.md#oh_resourcemanager_openrawdir) | 打开rawfile目录，打开后可以遍历对应目录下的rawfile文件。 |
| [RawFile \*OH\_ResourceManager\_OpenRawFile(const NativeResourceManager \*mgr, const char \*fileName)](capi-raw-file-manager-h.md#oh_resourcemanager_openrawfile) | 打开rawfile文件，打开后可以读取它的数据。 |
| [RawFile64 \*OH\_ResourceManager\_OpenRawFile64(const NativeResourceManager \*mgr, const char \*fileName)](capi-raw-file-manager-h.md#oh_resourcemanager_openrawfile64) | 打开较大的rawfile文件，打开后可以读取它的数据。 |
| [bool OH\_ResourceManager\_IsRawDir(const NativeResourceManager \*mgr, const char \*path)](capi-raw-file-manager-h.md#oh_resourcemanager_israwdir) | 判断路径是否是rawfile下的目录。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_ResourceManager\_InitNativeResourceManager()

PhonePC/2in1TabletTVWearable

```
1. NativeResourceManager *OH_ResourceManager_InitNativeResourceManager(napi_env env, napi_value jsResMgr)
```

**描述**

基于JavaScript侧的ResourceManager获取native侧的ResourceManager，用来完成rawfile相关功能。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | 表示JavaScript Native Interface（napi）环境指针。 |
| napi\_value jsResMgr | 表示JavaScript resource manager。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [NativeResourceManager \*](capi-rawfile-nativeresourcemanager.md) | 返回[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)指针，如果失败返回空指针。 |

### OH\_ResourceManager\_ReleaseNativeResourceManager()

PhonePC/2in1TabletTVWearable

```
1. void OH_ResourceManager_ReleaseNativeResourceManager(NativeResourceManager *resMgr)
```

**描述**

释放native侧ResourceManager。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*resMgr | 表示[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)指针。 |

### OH\_ResourceManager\_OpenRawDir()

PhonePC/2in1TabletTVWearable

```
1. RawDir *OH_ResourceManager_OpenRawDir(const NativeResourceManager *mgr, const char *dirName)
```

**描述**

打开rawfile目录，打开后可以遍历对应目录下的rawfile文件。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 表示指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针是通过调用[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取的。 |
| const char \*dirName | 表示要打开的rawfile目录名称，当传递一个空字符串时表示打开rawfile根目录。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [RawDir \*](capi-rawfile-rawdir.md) | 返回[RawDir](capi-rawfile-rawdir.md)指针。使用完此指针后，调用[OH\_ResourceManager\_CloseRawDir](capi-raw-dir-h.md#oh_resourcemanager_closerawdir)释放。如果失败或者mgr为空时返回空指针。 |

**参考：**

[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)

[OH\_ResourceManager\_CloseRawDir](capi-raw-dir-h.md#oh_resourcemanager_closerawdir)

### OH\_ResourceManager\_OpenRawFile()

PhonePC/2in1TabletTVWearable

```
1. RawFile *OH_ResourceManager_OpenRawFile(const NativeResourceManager *mgr, const char *fileName)
```

**描述**

打开rawfile文件，打开后可以读取它的数据。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 表示指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过调用[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| const char \*fileName | 表示基于rawfile根目录的相对路径下的文件名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [RawFile \*](capi-rawfile-rawfile.md) | 返回[RawFile](capi-rawfile-rawfile.md)指针。当使用完此指针，调用[OH\_ResourceManager\_CloseRawFile](capi-raw-file-h.md#oh_resourcemanager_closerawfile)释放。如果失败或者mgr和fileName为空时返回空指针。 |

**参考：**

[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)

[OH\_ResourceManager\_CloseRawFile](capi-raw-file-h.md#oh_resourcemanager_closerawfile)

### OH\_ResourceManager\_OpenRawFile64()

PhonePC/2in1TabletTVWearable

```
1. RawFile64 *OH_ResourceManager_OpenRawFile64(const NativeResourceManager *mgr, const char *fileName)
```

**描述**

打开较大的rawfile文件，打开后可以读取它的数据。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 表示指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过调用[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| const char \*fileName | 表示基于rawfile根目录的相对路径下的文件名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [RawFile64 \*](capi-rawfile-rawfile64.md) | 返回[RawFile64](capi-rawfile-rawfile64.md)指针。当使用完此指针，调用[OH\_ResourceManager\_CloseRawFile64](capi-raw-file-h.md#oh_resourcemanager_closerawfile64)释放。如果失败或者mgr和fileName为空时返回空指针。 |

**参考：**

[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)

[OH\_ResourceManager\_CloseRawFile64](capi-raw-file-h.md#oh_resourcemanager_closerawfile64)

### OH\_ResourceManager\_IsRawDir()

PhonePC/2in1TabletTVWearable

```
1. bool OH_ResourceManager_IsRawDir(const NativeResourceManager *mgr, const char *path)
```

**描述**

判断路径是否是rawfile下的目录。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 表示指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过调用[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| const char \*path | rawfile路径。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回true表示是rawfile下的目录，返回false表示不是rawfile下的目录。 |
