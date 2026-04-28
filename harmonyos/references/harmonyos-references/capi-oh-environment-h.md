---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-environment-h
title: oh_environment.h
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 头文件 > oh_environment.h
category: harmonyos-references
scraped_at: 2026-04-28T08:05:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:68da9d96f2a4aa42491a7c6f073a481cd138d85f2b98dd5d0dce10e2df131a33
---

## 概述

PC/2in1

environment模块接口定义，使用environment提供的native接口，获取公共文件根目录的沙箱路径。

**引用文件：** <filemanagement/environment/oh\_environment.h>

**库：** libohenvironment.so

**系统能力：** SystemCapability.FileManagement.File.Environment.FolderObtain

**起始版本：** 12

**相关模块：** [Environment](capi-environment.md)

## 汇总

PC/2in1

### 函数

PC/2in1

| 名称 | 描述 |
| --- | --- |
| [FileManagement\_ErrCode OH\_Environment\_GetUserDownloadDir(char \*\*result)](capi-oh-environment-h.md#oh_environment_getuserdownloaddir) | 获取Download根目录沙箱路径。 |
| [FileManagement\_ErrCode OH\_Environment\_GetUserDesktopDir(char \*\*result)](capi-oh-environment-h.md#oh_environment_getuserdesktopdir) | 获取Desktop根目录沙箱路径。 |
| [FileManagement\_ErrCode OH\_Environment\_GetUserDocumentDir(char \*\*result)](capi-oh-environment-h.md#oh_environment_getuserdocumentdir) | 获取Document根目录沙箱路径。 |

## 函数说明

PC/2in1

### OH\_Environment\_GetUserDownloadDir()

PC/2in1

```
1. FileManagement_ErrCode OH_Environment_GetUserDownloadDir(char **result)
```

**描述**

获取Download根目录沙箱路径。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char \*\*result | Download根目录路径指针。请引用头文件malloc.h并使用free()进行资源释放。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode) | 返回FileManagement模块错误码[FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode)。 |

### OH\_Environment\_GetUserDesktopDir()

PC/2in1

```
1. FileManagement_ErrCode OH_Environment_GetUserDesktopDir(char **result)
```

**描述**

获取Desktop根目录沙箱路径。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char \*\*result | Desktop根目录路径指针。请引用头文件malloc.h并使用free()进行资源释放。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode) | 返回FileManagement模块错误码[FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode)。 |

### OH\_Environment\_GetUserDocumentDir()

PC/2in1

```
1. FileManagement_ErrCode OH_Environment_GetUserDocumentDir(char **result)
```

**描述**

获取Document根目录沙箱路径。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char \*\*result | Document根目录路径指针。请引用头文件malloc.h并使用free()进行资源释放。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode) | 返回FileManagement模块错误码[FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode)。 |
