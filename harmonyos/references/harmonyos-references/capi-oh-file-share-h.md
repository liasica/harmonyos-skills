---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-file-share-h
title: oh_file_share.h
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 头文件 > oh_file_share.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5a6065b1dfd5b4995b7b5372612696db0a3f6c33ccdebc9fb1f61852b601d75b
---

## 概述

提供基于URI的文件及目录持久化授权、取消持久化授权、权限激活、权限查询等方法，适用于跨应用文件共享场景。持久化授权用于保存访问策略，权限激活用于使已持久化的权限生效。

**引用文件：** <filemanagement/fileshare/oh\_file\_share.h>

**库：** libohfileshare.so

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 12

**相关模块：** [fileShare](capi-fileshare.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [FileShare\_PolicyErrorResult](capi-fileshare-fileshare-policyerrorresult.md) | FileShare\_PolicyErrorResult | 授予或激活权限失败的URI策略结果，用于记录失败URI、错误码和失败原因。 |
| [FileShare\_PolicyInfo](capi-fileshare-fileshare-policyinfo.md) | FileShare\_PolicyInfo | 需要授予或激活URI访问权限的策略信息，用于描述跨应用文件共享场景中的目标URI和访问模式。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [FileShare\_OperationMode](capi-oh-file-share-h.md#fileshare_operationmode) | FileShare\_OperationMode | URI操作模式枚举值。 |
| [FileShare\_PolicyErrorCode](capi-oh-file-share-h.md#fileshare_policyerrorcode) | FileShare\_PolicyErrorCode | 授予或激活权限策略失败的URI对应的错误码。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [FileManagement\_ErrCode OH\_FileShare\_PersistPermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum)](capi-oh-file-share-h.md#oh_fileshare_persistpermission) | 对所选择的多个文件或目录URI持久化授权。完成持久化授权后，可调用OH\_FileShare\_ActivatePermission()激活权限。 |
| [FileManagement\_ErrCode OH\_FileShare\_RevokePermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum)](capi-oh-file-share-h.md#oh_fileshare_revokepermission) | 对所选择的多个文件或目录URI取消持久化授权。调用此接口前，需要先完成持久化授权。 |
| [FileManagement\_ErrCode OH\_FileShare\_ActivatePermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum)](capi-oh-file-share-h.md#oh_fileshare_activatepermission) | 激活多个已经持久化授权的文件或目录。调用此接口前，需要先调用OH\_FileShare\_PersistPermission()完成持久化授权，激活后权限生效。 |
| [FileManagement\_ErrCode OH\_FileShare\_DeactivatePermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum)](capi-oh-file-share-h.md#oh_fileshare_deactivatepermission) | 取消激活持久化授权过的多个文件或目录。调用此接口前，需要先调用OH\_FileShare\_ActivatePermission()激活权限。取消激活后，持久化授权仍保留。 |
| [FileManagement\_ErrCode OH\_FileShare\_CheckPersistentPermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, bool \*\*result, unsigned int \*resultNum)](capi-oh-file-share-h.md#oh_fileshare_checkpersistentpermission) | 校验所选择的多个文件或目录URI的持久化授权。可在激活权限前调用该接口，确认目标URI是否已经完成持久化授权。 |
| [void OH\_FileShare\_ReleasePolicyErrorResult(FileShare\_PolicyErrorResult \*errorResult, unsigned int resultNum)](capi-oh-file-share-h.md#oh_fileshare_releasepolicyerrorresult) | 释放FileShare\_PolicyErrorResult指针指向的内存资源。该资源由OH\_FileShare\_PersistPermission、OH\_FileShare\_RevokePermission、OH\_FileShare\_ActivatePermission和OH\_FileShare\_DeactivatePermission通过result输出。 |

## 枚举类型说明

### FileShare\_OperationMode

```c
enum FileShare_OperationMode
```

**描述**

URI操作模式枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| READ\_MODE = 1 << 0 | 读取权限，可单独使用，也可与WRITE\_MODE组合使用。 |
| WRITE\_MODE = 1 << 1 | 写入权限，可单独使用，也可与READ\_MODE组合使用。 |

### FileShare\_PolicyErrorCode

```c
enum FileShare_PolicyErrorCode
```

**描述**

授予或激活权限策略失败的URI对应的错误码。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| PERSISTENCE\_FORBIDDEN = 1 | URI禁止被持久化，例如远端URI不支持持久化。 |
| INVALID\_MODE = 2 | 无效的模式，例如权限模式值不在支持范围内。 |
| INVALID\_PATH = 3 | 无效路径。 |
| PERMISSION\_NOT\_PERSISTED = 4 | 权限没有被持久化。 |

## 函数说明

### OH\_FileShare\_PersistPermission()

```c
FileManagement_ErrCode OH_FileShare_PersistPermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, FileShare_PolicyErrorResult **result, unsigned int *resultNum)
```

**描述**

对所选择的多个文件或目录URI持久化授权。完成持久化授权后，可调用OH\_FileShare\_ActivatePermission()激活权限。

**需要权限：** ohos.permission.FILE\_ACCESS\_PERSIST

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const FileShare\_PolicyInfo](capi-fileshare-fileshare-policyinfo.md) \*policies | 指向FileShare\_PolicyInfo实例数组的指针，表示需要持久化授权的文件或目录URI策略信息。 |
| unsigned int policyNum | FileShare\_PolicyInfo实例数组的元素个数，取值范围为[1, 500]。 |
| [FileShare\_PolicyErrorResult](capi-fileshare-fileshare-policyerrorresult.md) \*\*result | 输出参数，指向FileShare\_PolicyErrorResult数组指针。请使用OH\_FileShare\_ReleasePolicyErrorResult()进行资源释放。 |
| unsigned int \*resultNum | 输出参数，表示FileShare\_PolicyErrorResult数组的元素个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode) | 返回FileManagement模块错误码[FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode)。  ERR\_INVALID\_PARAMETER 401 - 输入参数无效。可能的原因有：  1. 参数policies或参数result或参数resultNum为空指针；  2. 参数policyNum值为0或者超过最大长度(500)；  3. 参数policies中携带的uri为空或者length为0或者uri的长度与length不一致。  ERR\_DEVICE\_NOT\_SUPPORTED 801 - 当前设备类型不支持此接口。  ERR\_PERMISSION\_ERROR 201 - 接口权限校验失败。  ERR\_ENOMEM 13900011 - 分配或者拷贝内存失败。  ERR\_EPERM 13900001 - 操作不被允许。  ERR\_OK 0 - 接口调用成功。 |

### OH\_FileShare\_RevokePermission()

```c
FileManagement_ErrCode OH_FileShare_RevokePermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, FileShare_PolicyErrorResult **result, unsigned int *resultNum)
```

**描述**

对所选择的多个文件或目录URI取消持久化授权。调用此接口前，需要先完成持久化授权。

**需要权限：** ohos.permission.FILE\_ACCESS\_PERSIST

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const FileShare\_PolicyInfo](capi-fileshare-fileshare-policyinfo.md) \*policies | 指向FileShare\_PolicyInfo实例数组的指针，表示需要取消持久化授权的文件或目录URI策略信息。 |
| unsigned int policyNum | FileShare\_PolicyInfo实例数组的元素个数，取值范围为[1, 500]。 |
| [FileShare\_PolicyErrorResult](capi-fileshare-fileshare-policyerrorresult.md) \*\*result | 输出参数，指向FileShare\_PolicyErrorResult数组指针。请使用OH\_FileShare\_ReleasePolicyErrorResult()进行资源释放。 |
| unsigned int \*resultNum | 输出参数，表示FileShare\_PolicyErrorResult数组的元素个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode) | 返回FileManagement模块错误码[FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode)。  ERR\_INVALID\_PARAMETER 401 - 输入参数无效。可能的原因有：  1. 参数policies或参数result或参数resultNum为空指针；  2. 参数policyNum值为0或者超过最大长度(500)；  3. 参数policies中携带的uri为空或者length为0或者uri的长度与length不一致。  ERR\_DEVICE\_NOT\_SUPPORTED 801 - 当前设备类型不支持此接口。  ERR\_PERMISSION\_ERROR 201 - 接口权限校验失败。  ERR\_ENOMEM 13900011 - 分配或者拷贝内存失败。  ERR\_EPERM 13900001 - 操作不被允许。  ERR\_OK 0 - 接口调用成功。 |

### OH\_FileShare\_ActivatePermission()

```c
FileManagement_ErrCode OH_FileShare_ActivatePermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, FileShare_PolicyErrorResult **result, unsigned int *resultNum)
```

**描述**

激活多个已经持久化授权的文件或目录。调用此接口前，需要先调用[OH\_FileShare\_PersistPermission](capi-oh-file-share-h.md#oh_fileshare_persistpermission)完成持久化授权，激活后权限生效。

**需要权限：** ohos.permission.FILE\_ACCESS\_PERSIST

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const FileShare\_PolicyInfo](capi-fileshare-fileshare-policyinfo.md) \*policies | 指向FileShare\_PolicyInfo实例数组的指针，表示需要激活权限的文件或目录URI策略信息。 |
| unsigned int policyNum | FileShare\_PolicyInfo实例数组的元素个数，取值范围为[1, 500]。 |
| [FileShare\_PolicyErrorResult](capi-fileshare-fileshare-policyerrorresult.md) \*\*result | 输出参数，指向FileShare\_PolicyErrorResult数组指针。请使用OH\_FileShare\_ReleasePolicyErrorResult()进行资源释放。 |
| unsigned int \*resultNum | 输出参数，表示FileShare\_PolicyErrorResult数组的元素个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode) | 返回FileManagement模块错误码[FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode)。  ERR\_INVALID\_PARAMETER 401 - 输入参数无效。可能的原因有：  1. 参数policies或参数result或参数resultNum为空指针；  2. 参数policyNum值为0或者超过最大长度(500)；  3. 参数policies中携带的uri为空或者length为0或者uri的长度与length不一致。  ERR\_DEVICE\_NOT\_SUPPORTED 801 - 当前设备类型不支持此接口。  ERR\_PERMISSION\_ERROR 201 - 接口权限校验失败。  ERR\_ENOMEM 13900011 - 分配或者拷贝内存失败。  ERR\_EPERM 13900001 - 操作不被允许。  ERR\_OK 0 - 接口调用成功。 |

### OH\_FileShare\_DeactivatePermission()

```c
FileManagement_ErrCode OH_FileShare_DeactivatePermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, FileShare_PolicyErrorResult **result, unsigned int *resultNum)
```

**描述**

取消激活持久化授权过的多个文件或目录。调用此接口前，需要先调用[OH\_FileShare\_ActivatePermission](capi-oh-file-share-h.md#oh_fileshare_activatepermission)激活权限。取消激活后，持久化授权仍保留。

**需要权限：** ohos.permission.FILE\_ACCESS\_PERSIST

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const FileShare\_PolicyInfo](capi-fileshare-fileshare-policyinfo.md) \*policies | 指向FileShare\_PolicyInfo实例数组的指针，表示需要取消激活权限的文件或目录URI策略信息。 |
| unsigned int policyNum | FileShare\_PolicyInfo实例数组的元素个数，取值范围为[1, 500]。 |
| [FileShare\_PolicyErrorResult](capi-fileshare-fileshare-policyerrorresult.md) \*\*result | 输出参数，指向FileShare\_PolicyErrorResult数组指针。请使用OH\_FileShare\_ReleasePolicyErrorResult()进行资源释放。 |
| unsigned int \*resultNum | 输出参数，表示FileShare\_PolicyErrorResult数组的元素个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode) | 返回FileManagement模块错误码[FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode)。  ERR\_INVALID\_PARAMETER 401 - 输入参数无效。可能的原因有：  1. 参数policies或参数result或参数resultNum为空指针；  2. 参数policyNum值为0或者超过最大长度(500)；  3. 参数policies中携带的uri为空或者length为0或者uri的长度与length不一致。  ERR\_DEVICE\_NOT\_SUPPORTED 801 - 当前设备类型不支持此接口。  ERR\_PERMISSION\_ERROR 201 - 接口权限校验失败。  ERR\_ENOMEM 13900011 - 分配或者拷贝内存失败。  ERR\_EPERM 13900001 - 操作不被允许。  ERR\_OK 0 - 接口调用成功。 |

### OH\_FileShare\_CheckPersistentPermission()

```c
FileManagement_ErrCode OH_FileShare_CheckPersistentPermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, bool **result, unsigned int *resultNum)
```

**描述**

校验所选择的多个文件或目录URI的持久化授权。可在激活权限前调用该接口，确认目标URI是否已经完成持久化授权。

**需要权限：** ohos.permission.FILE\_ACCESS\_PERSIST

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const FileShare\_PolicyInfo](capi-fileshare-fileshare-policyinfo.md) \*policies | 指向FileShare\_PolicyInfo实例数组的指针，表示需要校验持久化授权的文件或目录URI策略信息。 |
| unsigned int policyNum | FileShare\_PolicyInfo实例数组的元素个数，取值范围为[1, 500]。 |
| bool \*\*result | 输出参数，指向授权校验结果数组。数组元素与policies数组元素一一对应，true表示有持久化授权；false表示不具有持久化授权。需要使用standard library标准库的free()方法释放申请的资源。 |
| unsigned int \*resultNum | 输出参数，表示校验结果数组的元素个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode) | 返回FileManagement模块错误码[FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode)。  ERR\_INVALID\_PARAMETER 401 - 输入参数无效。可能的原因有：  1. 参数policies或参数result或参数resultNum为空指针；  2. 参数policyNum值为0或者超过最大长度(500)；  3. 参数policies中携带的uri为空或者length为0或者uri的长度与length不一致。  ERR\_DEVICE\_NOT\_SUPPORTED 801 - 当前设备类型不支持此接口。  ERR\_PERMISSION\_ERROR 201 - 接口权限校验失败。  ERR\_ENOMEM 13900011 - 分配或者拷贝内存失败。  ERR\_EPERM 13900001 - 操作不被允许。可能的原因为policies中携带的所有uri都不符合规范或者uri转换出来的路径不存在。  ERR\_OK 0 - 接口调用成功。 |

### OH\_FileShare\_ReleasePolicyErrorResult()

```c
void OH_FileShare_ReleasePolicyErrorResult(FileShare_PolicyErrorResult *errorResult, unsigned int resultNum)
```

**描述**

释放FileShare\_PolicyErrorResult指针指向的内存资源。该资源由OH\_FileShare\_PersistPermission、OH\_FileShare\_RevokePermission、OH\_FileShare\_ActivatePermission和OH\_FileShare\_DeactivatePermission通过result输出。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [FileShare\_PolicyErrorResult](capi-fileshare-fileshare-policyerrorresult.md) \*errorResult | 指向FileShare\_PolicyErrorResult实例数组的指针。 |
| unsigned int resultNum | FileShare\_PolicyErrorResult实例数组的元素个数。 |
