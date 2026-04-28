---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-file-share-h
title: oh_file_share.h
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 头文件 > oh_file_share.h
category: harmonyos-references
scraped_at: 2026-04-28T08:05:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:875f923d844f866482bb36955ba2e299bc3d40262bd0a7e228e19a8e8e1cbf60
---

## 概述

PhonePC/2in1Tablet

提供基于URI的文件及目录授予持久化权限、权限激活、权限查询等方法。

**引用文件：** <filemanagement/fileshare/oh\_file\_share.h>

**库：** libohfileshare.so

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 12

**相关模块：** [fileShare](capi-fileshare.md)

## 汇总

PhonePC/2in1Tablet

### 结构体

PhonePC/2in1Tablet

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [FileShare\_PolicyErrorResult](capi-fileshare-fileshare-policyerrorresult.md) | FileShare\_PolicyErrorResult | 授予或使能权限失败的URI策略结果。 |
| [FileShare\_PolicyInfo](capi-fileshare-fileshare-policyinfo.md) | FileShare\_PolicyInfo | 需要授予或使能权限URI的策略信息。 |

### 枚举

PhonePC/2in1Tablet

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [FileShare\_OperationMode](capi-oh-file-share-h.md#fileshare_operationmode) | FileShare\_OperationMode | URI操作模式枚举值。 |
| [FileShare\_PolicyErrorCode](capi-oh-file-share-h.md#fileshare_policyerrorcode) | FileShare\_PolicyErrorCode | 授予或使能权限策略失败的URI对应的错误码。 |

### 函数

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [FileManagement\_ErrCode OH\_FileShare\_PersistPermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum)](capi-oh-file-share-h.md#oh_fileshare_persistpermission) | 对所选择的多个文件或目录URI持久化授权。 |
| [FileManagement\_ErrCode OH\_FileShare\_RevokePermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum)](capi-oh-file-share-h.md#oh_fileshare_revokepermission) | 对所选择的多个文件或目录URI取消持久化授权。 |
| [FileManagement\_ErrCode OH\_FileShare\_ActivatePermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum)](capi-oh-file-share-h.md#oh_fileshare_activatepermission) | 使能多个已经持久化授权的文件或目录。 |
| [FileManagement\_ErrCode OH\_FileShare\_DeactivatePermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum)](capi-oh-file-share-h.md#oh_fileshare_deactivatepermission) | 取消使能持久化授权过的多个文件或目录。 |
| [FileManagement\_ErrCode OH\_FileShare\_CheckPersistentPermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, bool \*\*result, unsigned int \*resultNum)](capi-oh-file-share-h.md#oh_fileshare_checkpersistentpermission) | 校验所选择的多个文件或目录URI的持久化授权。 |
| [void OH\_FileShare\_ReleasePolicyErrorResult(FileShare\_PolicyErrorResult \*errorResult, unsigned int resultNum)](capi-oh-file-share-h.md#oh_fileshare_releasepolicyerrorresult) | 释放FileShare\_PolicyErrorResult指针指向的内存资源。 |

## 枚举类型说明

PhonePC/2in1Tablet

### FileShare\_OperationMode

PhonePC/2in1Tablet

```
1. enum FileShare_OperationMode
```

**描述**

URI操作模式枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| READ\_MODE = 1 << 0 | 读取权限。 |
| WRITE\_MODE = 1 << 1 | 写入权限。 |

### FileShare\_PolicyErrorCode

PhonePC/2in1Tablet

```
1. enum FileShare_PolicyErrorCode
```

**描述**

授予或使能权限策略失败的URI对应的错误码。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| PERSISTENCE\_FORBIDDEN = 1 | URI禁止被持久化。 |
| INVALID\_MODE = 2 | 无效的模式。 |
| INVALID\_PATH = 3 | 无效路径。 |
| PERMISSION\_NOT\_PERSISTED = 4 | 权限没有被持久化。 |

## 函数说明

PhonePC/2in1Tablet

### OH\_FileShare\_PersistPermission()

PhonePC/2in1Tablet

```
1. FileManagement_ErrCode OH_FileShare_PersistPermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, FileShare_PolicyErrorResult **result, unsigned int *resultNum)
```

**描述**

对所选择的多个文件或目录URI持久化授权。

**需要权限：** ohos.permission.FILE\_ACCESS\_PERSIST

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const FileShare\_PolicyInfo](capi-fileshare-fileshare-policyinfo.md) \*policies | 一个指向FileShare\_PolicyInfo实例的指针。 |
| unsigned int policyNum | FileShare\_PolicyInfo实例数组的大小。 |
| [FileShare\_PolicyErrorResult](capi-fileshare-fileshare-policyerrorresult.md) \*\*result | FileShare\_PolicyErrorResult数组指针。请使用OH\_FileShare\_ReleasePolicyErrorResult()进行资源释放。 |
| unsigned int \*resultNum | FileShare\_PolicyErrorResult数组大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode) | 返回FileManagement模块错误码[FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode)。  ERR\_INVALID\_PARAMETER 401 - 输入参数无效。可能的原因有：  1. 参数policies或参数result或参数resultNum为空指针；  2. 参数policyNum值为0或者超过最大长度(500)；  3. 参数policies中携带的uri为空或者length为0或者uri的长度与length不一致。  ERR\_DEVICE\_NOT\_SUPPORTED 801 - 当前设备类型不支持此接口。  ERR\_PERMISSION\_ERROR 201 - 接口权限校验失败。  ERR\_ENOMEM 13900011 - 分配或者拷贝内存失败。  ERR\_EPERM 13900001 - 操作不被允许。  ERR\_OK 0 - 接口调用成功。 |

### OH\_FileShare\_RevokePermission()

PhonePC/2in1Tablet

```
1. FileManagement_ErrCode OH_FileShare_RevokePermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, FileShare_PolicyErrorResult **result, unsigned int *resultNum)
```

**描述**

对所选择的多个文件或目录URI取消持久化授权。

**需要权限：** ohos.permission.FILE\_ACCESS\_PERSIST

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const FileShare\_PolicyInfo](capi-fileshare-fileshare-policyinfo.md) \*policies | 一个指向FileShare\_PolicyInfo实例的指针。 |
| unsigned int policyNum | FileShare\_PolicyInfo实例数组的大小。 |
| [FileShare\_PolicyErrorResult](capi-fileshare-fileshare-policyerrorresult.md) \*\*result | FileShare\_PolicyErrorResult数组指针。请使用OH\_FileShare\_ReleasePolicyErrorResult()进行资源释放。 |
| unsigned int \*resultNum | FileShare\_PolicyErrorResult数组大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode) | 返回FileManagement模块错误码[FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode)。  ERR\_INVALID\_PARAMETER 401 - 输入参数无效。可能的原因有：1. 参数policies或参数result或参数resultNum为空指针；  2. 参数policyNum值为0或者超过最大长度(500)；3. 参数policies中携带的uri为空或者length为0或者uri的长度与length不一致。  ERR\_DEVICE\_NOT\_SUPPORTED 801 - 当前设备类型不支持此接口。  ERR\_PERMISSION\_ERROR 201 - 接口权限校验失败。  ERR\_ENOMEM 13900011 - 分配或者拷贝内存失败。  ERR\_EPERM 13900001 - 操作不被允许。  ERR\_OK 0 - 接口调用成功。 |

### OH\_FileShare\_ActivatePermission()

PhonePC/2in1Tablet

```
1. FileManagement_ErrCode OH_FileShare_ActivatePermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, FileShare_PolicyErrorResult **result, unsigned int *resultNum)
```

**描述**

使能多个已经持久化授权的文件或目录。

**需要权限：** ohos.permission.FILE\_ACCESS\_PERSIST

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const FileShare\_PolicyInfo](capi-fileshare-fileshare-policyinfo.md) \*policies | 一个指向FileShare\_PolicyInfo实例的指针。 |
| unsigned int policyNum | FileShare\_PolicyInfo实例数组的大小。 |
| [FileShare\_PolicyErrorResult](capi-fileshare-fileshare-policyerrorresult.md) \*\*result | FileShare\_PolicyErrorResult数组指针。请使用OH\_FileShare\_ReleasePolicyErrorResult()进行资源释放。 |
| unsigned int \*resultNum | FileShare\_PolicyErrorResult数组大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode) | 返回FileManagement模块错误码[FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode)。  ERR\_INVALID\_PARAMETER 401 - 输入参数无效。可能的原因有：  1. 参数policies或参数result或参数resultNum为空指针；  2. 参数policyNum值为0或者超过最大长度(500)；  3. 参数policies中携带的uri为空或者length为0或者uri的长度与length不一致。  ERR\_DEVICE\_NOT\_SUPPORTED 801 - 当前设备类型不支持此接口。  ERR\_PERMISSION\_ERROR 201 - 接口权限校验失败。  ERR\_ENOMEM 13900011 - 分配或者拷贝内存失败。  ERR\_EPERM 13900001 - 操作不被允许。  ERR\_OK 0 - 接口调用成功。 |

### OH\_FileShare\_DeactivatePermission()

PhonePC/2in1Tablet

```
1. FileManagement_ErrCode OH_FileShare_DeactivatePermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, FileShare_PolicyErrorResult **result, unsigned int *resultNum)
```

**描述**

取消使能持久化授权过的多个文件或目录。

**需要权限：** ohos.permission.FILE\_ACCESS\_PERSIST

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const FileShare\_PolicyInfo](capi-fileshare-fileshare-policyinfo.md) \*policies | 一个指向FileShare\_PolicyInfo实例的指针。 |
| unsigned int policyNum | FileShare\_PolicyInfo实例数组的大小。 |
| [FileShare\_PolicyErrorResult](capi-fileshare-fileshare-policyerrorresult.md) \*\*result | FileShare\_PolicyErrorResult数组指针。请使用OH\_FileShare\_ReleasePolicyErrorResult()进行资源释放。 |
| unsigned int \*resultNum | FileShare\_PolicyErrorResult数组大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode) | 返回FileManagement模块错误码[FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode)。  ERR\_INVALID\_PARAMETER 401 - 输入参数无效。可能的原因有：  1. 参数policies或参数result或参数resultNum为空指针；  2. 参数policyNum值为0或者超过最大长度(500)；  3. 参数policies中携带的uri为空或者length为0或者uri的长度与length不一致。  ERR\_DEVICE\_NOT\_SUPPORTED 801 - 当前设备类型不支持此接口。  ERR\_PERMISSION\_ERROR 201 - 接口权限校验失败。  ERR\_ENOMEM 13900011 - 分配或者拷贝内存失败。  ERR\_EPERM 13900001 - 操作不被允许。  ERR\_OK 0 - 接口调用成功。 |

### OH\_FileShare\_CheckPersistentPermission()

PhonePC/2in1Tablet

```
1. FileManagement_ErrCode OH_FileShare_CheckPersistentPermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, bool **result, unsigned int *resultNum)
```

**描述**

校验所选择的多个文件或目录URI的持久化授权。

**需要权限：** ohos.permission.FILE\_ACCESS\_PERSIST

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const FileShare\_PolicyInfo](capi-fileshare-fileshare-policyinfo.md) \*policies | 一个指向FileShare\_PolicyInfo实例的指针。 |
| unsigned int policyNum | FileShare\_PolicyInfo实例数组的大小。 |
| bool \*\*result | 授权校验结果指针。true表示有持久化授权；false表示不具有持久化授权。请引用头文件malloc.h并使用free()进行资源释放。 |
| unsigned int \*resultNum | 校验结果数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode) | 返回FileManagement模块错误码[FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode)。  ERR\_INVALID\_PARAMETER 401 - 输入参数无效。可能的原因有：  1. 参数policies或参数result或参数resultNum为空指针；  2. 参数policyNum值为0或者超过最大长度(500)；  3. 参数policies中携带的uri为空或者length为0或者uri的长度与length不一致。  ERR\_DEVICE\_NOT\_SUPPORTED 801 - 当前设备类型不支持此接口。  ERR\_PERMISSION\_ERROR 201 - 接口权限校验失败。  ERR\_ENOMEM 13900011 - 分配或者拷贝内存失败。  ERR\_EPERM 13900001 - 操作不被允许。可能的原因为policies中携带的所有uri都不符合规范或者uri转换出来的路径不存在。  ERR\_OK 0 - 接口调用成功。 |

### OH\_FileShare\_ReleasePolicyErrorResult()

PhonePC/2in1Tablet

```
1. void OH_FileShare_ReleasePolicyErrorResult(FileShare_PolicyErrorResult *errorResult, unsigned int resultNum)
```

**描述**

释放FileShare\_PolicyErrorResult指针指向的内存资源。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [FileShare\_PolicyErrorResult](capi-fileshare-fileshare-policyerrorresult.md) \*errorResult | 一个指向FileShare\_PolicyErrorResult实例的指针。 |
| unsigned int resultNum | FileShare\_PolicyErrorResult实例数组的大小。 |
