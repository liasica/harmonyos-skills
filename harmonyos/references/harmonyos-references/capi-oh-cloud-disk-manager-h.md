---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-cloud-disk-manager-h
title: oh_cloud_disk_manager.h
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 头文件 > oh_cloud_disk_manager.h
category: harmonyos-references
scraped_at: 2026-04-28T08:05:51+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d1bbdc900a5d3bf46592e6a3b22f6acbc942bf0dcdb67173fe85504d5428b62c
---

## 概述

PC/2in1Tablet

云盘管理模块的接口定义。

**引用文件：** <filemanagement/clouddiskmanager/oh\_cloud\_disk\_manager.h>

**库：** libohclouddiskmanager.so

**系统能力：** SystemCapability.FileManagement.CloudDiskManager

**起始版本：** 21

**相关模块：** [CloudDisk](capi-clouddisk.md)

## 汇总

PC/2in1Tablet

### 结构体

PC/2in1Tablet

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md) | CloudDisk\_PathInfo/CloudDisk\_FileIdInfo/CloudDisk\_SyncFolderPath | CloudDisk\_PathInfo：文件路径信息。  CloudDisk\_FileIdInfo：定义的文件ID。  CloudDisk\_SyncFolderPath：定义的同步根路径。 |
| [CloudDisk\_FileSyncState](capi-clouddisk-clouddisk-filesyncstate.md) | CloudDisk\_FileSyncState | 文件的同步状态。 |
| [CloudDisk\_ChangeData](capi-clouddisk-clouddisk-changedata.md) | CloudDisk\_ChangeData | 定义了同步根路径下单个文件变更事件的数据结构。该结构包含有关文件变更的详细信息，包括唯一ID、父目录的唯一ID、相对路径、变更类型、文件大小和时间戳。 |
| [CloudDisk\_ChangesResult](capi-clouddisk-clouddisk-changesresult.md) | CloudDisk\_ChangesResult | 查询同步根路径中文件变更的结果。该结构体包含同步根路径中文件的变更数据，包括下一个更新序列号、结尾标志以及变更数据项数组。 |
| [CloudDisk\_FailedList](capi-clouddisk-clouddisk-failedlist.md) | CloudDisk\_FailedList | 同步操作中失败的文件列表信息。该结构包含文件路径信息以及失败的具体错误原因。 |
| [CloudDisk\_ResultList](capi-clouddisk-clouddisk-resultlist.md) | CloudDisk\_ResultList | 表示一个文件同步操作的结果。该结构体包含文件的绝对路径、同步结果，以及同步状态或失败原因。 |
| [CloudDisk\_DisplayNameInfo](capi-clouddisk-clouddisk-displaynameinfo.md) | CloudDisk\_DisplayNameInfo | 定义同步根路径的显示名称信息。 |
| [CloudDisk\_SyncFolder](capi-clouddisk-clouddisk-syncfolder.md) | CloudDisk\_SyncFolder | 同步根属性信息。 |

### 枚举

PC/2in1Tablet

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [CloudDisk\_SyncState](capi-oh-cloud-disk-manager-h.md#clouddisk_syncstate) | CloudDisk\_SyncState | 文件同步状态的枚举值。 |
| [CloudDisk\_OperationType](capi-oh-cloud-disk-manager-h.md#clouddisk_operationtype) | CloudDisk\_OperationType | 文件变更类型枚举值。 |
| [CloudDisk\_ErrorReason](capi-oh-cloud-disk-manager-h.md#clouddisk_errorreason) | CloudDisk\_ErrorReason | 文件同步失败原因的枚举值。 |
| [CloudDisk\_SyncFolderState](capi-oh-cloud-disk-manager-h.md#clouddisk_syncfolderstate) | CloudDisk\_SyncFolderState | 同步根路径状态的枚举值。 |

### 函数

PC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_RegisterSyncFolderChanges(const CloudDisk\_SyncFolderPath syncFolderPath, void (\*callback)(const CloudDisk\_SyncFolderPath syncFolderPath, const CloudDisk\_ChangeData changeDatas[], size\_t bufferLength))](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-cloud-disk-manager-h#oh_clouddisk_registersyncfolderchanges) | 应用注册一个回调函数，用于获取同步根路径下文件的变更。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_UnregisterSyncFolderChanges(const CloudDisk\_SyncFolderPath syncFolderPath)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_unregistersyncfolderchanges) | 应用取消注册同步根路径下文件变更的回调。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_GetSyncFolderChanges(const CloudDisk\_SyncFolderPath syncFolderPath, uint64\_t startUsn, size\_t count, CloudDisk\_ChangesResult \*\*changesResult)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_getsyncfolderchanges) | 获取同步根路径下的历史操作记录。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_SetFileSyncStates(const CloudDisk\_SyncFolderPath syncFolderPath, const CloudDisk\_FileSyncState fileSyncStates[], size\_t bufferLength, CloudDisk\_FailedList \*\*failedLists, size\_t \*failedCount)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-cloud-disk-manager-h#oh_clouddisk_setfilesyncstates) | 应用设置同步根路径下文件的同步状态。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_GetFileSyncStates(const CloudDisk\_SyncFolderPath syncFolderPath, const CloudDisk\_PathInfo paths[], size\_t bufferLength, CloudDisk\_ResultList \*\*resultLists, size\_t \*resultCount)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-cloud-disk-manager-h#oh_clouddisk_getfilesyncstates) | 应用查询同步根路径下文件同步状态。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_RegisterSyncFolder(const CloudDisk\_SyncFolder \*syncFolder)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_registersyncfolder) | 应用注册同步根。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_UnregisterSyncFolder(const CloudDisk\_SyncFolderPath syncFolderPath)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_unregistersyncfolder) | 应用取消注册同步根。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_ActiveSyncFolder(const CloudDisk\_SyncFolderPath syncFolderPath)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_activesyncfolder) | 应用激活同步根。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_DeactiveSyncFolder(const CloudDisk\_SyncFolderPath syncFolderPath)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_deactivesyncfolder) | 应用取消激活同步根。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_GetSyncFolders(CloudDisk\_SyncFolder \*\*syncFolders, size\_t \*count)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_getsyncfolders) | 应用获取所有同步根。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_UpdateCustomAlias(const CloudDisk\_SyncFolderPath syncFolderPath, const char \*customAlias, size\_t customAliasLength)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_updatecustomalias) | 应用更新同步根别名。 |

## 枚举类型说明

PC/2in1Tablet

### CloudDisk\_SyncState

PC/2in1Tablet

```
1. enum CloudDisk_SyncState
```

**描述**

文件同步状态的枚举值。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| IDLE = 0 | 目前处于空闲状态，未执行任何同步操作。 |
| SYNCING = 1 | 文件正在同步。 |
| SYNC\_SUCCEEDED = 2 | 文件同步成功。 |
| SYNC\_FAILED = 3 | 文件同步失败。 |
| SYNC\_CANCELED = 4 | 文件同步取消。 |
| SYNC\_CONFLICTED = 5 | 文件同步冲突。 |

### CloudDisk\_OperationType

PC/2in1Tablet

```
1. enum CloudDisk_OperationType
```

**描述**

文件变更类型枚举值。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| CREATE = 0 | 创建文件或目录。 |
| DELETE = 1 | 删除文件或目录。 |
| MOVE\_FROM = 2 | 移动此文件或目录。 |
| MOVE\_TO = 3 | 移动到此文件或目录。 |
| CLOSE\_WRITE = 4 | 在写入操作后关闭文件。 |
| SYNC\_FOLDER\_INVALID = 5 | 同步根路径无效。 |

### CloudDisk\_ErrorReason

PC/2in1Tablet

```
1. enum CloudDisk_ErrorReason
```

**描述**

文件同步失败原因的枚举值。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| INVALID\_ARGUMENT = 0 | 输入的参数无效。 |
| NO\_SUCH\_FILE = 1 | 操作的文件或目录不存在。 |
| NO\_SPACE\_LEFT = 2 | 设备上的剩余空间不足。 |
| OUT\_OF\_RANGE = 3 | 超出有效范围。 |
| NO\_SYNC\_STATE = 4 | 同步状态未设置。 |

### CloudDisk\_SyncFolderState

PC/2in1Tablet

```
1. enum CloudDisk_SyncFolderState
```

**描述**

同步根路径状态的枚举值。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| INACTIVE = 0 | 表示同步根路径的状态是未激活的。 |
| ACTIVE = 1 | 表示同步根路径的状态是激活的。 |

## 函数说明

PC/2in1Tablet

### OH\_CloudDisk\_RegisterSyncFolderChanges()

PC/2in1Tablet

```
1. CloudDisk_ErrorCode OH_CloudDisk_RegisterSyncFolderChanges(const CloudDisk_SyncFolderPath syncFolderPath, void (*callback)(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_ChangeData changeDatas[], size_t bufferLength))
```

**描述**

应用注册一个回调函数，用于获取同步根路径下文件的变更。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk\_SyncFolderPath syncFolderPath | 表示同步根路径，参考：[CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md)。 |
| callback | 注册的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，返回[CLOUD\_DISK\_OK](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)。 |

### OH\_CloudDisk\_UnregisterSyncFolderChanges()

PC/2in1Tablet

```
1. CloudDisk_ErrorCode OH_CloudDisk_UnregisterSyncFolderChanges(const CloudDisk_SyncFolderPath syncFolderPath)
```

**描述**

应用取消注册同步根路径下文件变更的回调。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk\_SyncFolderPath syncFolderPath | 表示同步根路径，参考：[CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，返回[CLOUD\_DISK\_OK](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)。 |

### OH\_CloudDisk\_GetSyncFolderChanges()

PC/2in1Tablet

```
1. CloudDisk_ErrorCode OH_CloudDisk_GetSyncFolderChanges(const CloudDisk_SyncFolderPath syncFolderPath, uint64_t startUsn, size_t count, CloudDisk_ChangesResult **changesResult)
```

**描述**

获取同步根路径下的历史操作记录。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk\_SyncFolderPath syncFolderPath | 查询的同步根路径，参考：[CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md)。 |
| uint64\_t startUsn | 查询起始的变更序列，范围：[0, 2^64 - 1]。 |
| size\_t count | 查询文件变更的数量，范围：[1, 100]。 |
| [CloudDisk\_ChangesResult](capi-clouddisk-clouddisk-changesresult.md) \*\*changesResult | 表示查询文件变更的结果。详情请参阅[CloudDisk\_ChangesResult](capi-clouddisk-clouddisk-changesresult.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，返回[CLOUD\_DISK\_OK](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)。 |

### OH\_CloudDisk\_SetFileSyncStates()

PC/2in1Tablet

```
1. CloudDisk_ErrorCode OH_CloudDisk_SetFileSyncStates(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_FileSyncState fileSyncStates[], size_t bufferLength, CloudDisk_FailedList **failedLists, size_t *failedCount)
```

**描述**

应用设置同步根路径下文件的同步状态。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk\_SyncFolderPath syncFolderPath | 待设置的同步根路径，参考：[CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md)。 |
| [const CloudDisk\_FileSyncState](capi-clouddisk-clouddisk-filesyncstate.md) fileSyncStates[] | 指定文件路径及其目标同步状态的[CloudDisk\_FileSyncState](capi-clouddisk-clouddisk-filesyncstate.md)数组。 |
| size\_t bufferLength | 待设置同步状态数组的长度，范围：[1, 100]。 |
| [CloudDisk\_FailedList](capi-clouddisk-clouddisk-failedlist.md) \*\*failedLists | 输出参数。返回一个指向[CloudDisk\_FailedList](capi-clouddisk-clouddisk-failedlist.md)数组的指针，该数组包含设置失败的文件。 |
| size\_t \*failedCount | 输出参数。设置同步状态失败的文件列表数组长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，返回[CLOUD\_DISK\_OK](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)。 |

### OH\_CloudDisk\_GetFileSyncStates()

PC/2in1Tablet

```
1. CloudDisk_ErrorCode OH_CloudDisk_GetFileSyncStates(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_PathInfo paths[], size_t bufferLength, CloudDisk_ResultList **resultLists, size_t *resultCount)
```

**描述**

应用查询同步根路径下文件同步状态。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk\_SyncFolderPath syncFolderPath | 待查询的同步根路径，参考：[CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md)。 |
| [const CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md) paths[] | 待查询同步状态[CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md)的数组。 |
| size\_t bufferLength | 待查询同步状态的数组的长度，范围：[1, 100]。 |
| [CloudDisk\_ResultList](capi-clouddisk-clouddisk-resultlist.md) \*\*resultLists | 输出参数。返回一个查询到的文件同步操作结果，详情可参考：[CloudDisk\_ResultList](capi-clouddisk-clouddisk-resultlist.md)。 |
| size\_t \*resultCount | 输出参数。返回失败的文件数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，返回[CLOUD\_DISK\_OK](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)。 |

### OH\_CloudDisk\_RegisterSyncFolder()

PC/2in1Tablet

```
1. CloudDisk_ErrorCode OH_CloudDisk_RegisterSyncFolder(const CloudDisk_SyncFolder *syncFolder)
```

**描述**

应用注册同步根。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const CloudDisk\_SyncFolder](capi-clouddisk-clouddisk-syncfolder.md) \*syncFolder | 待注册的同步根路径，参考：[CloudDisk\_SyncFolder](capi-clouddisk-clouddisk-syncfolder.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，返回[CLOUD\_DISK\_OK](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)。 |

### OH\_CloudDisk\_UnregisterSyncFolder()

PC/2in1Tablet

```
1. CloudDisk_ErrorCode OH_CloudDisk_UnregisterSyncFolder(const CloudDisk_SyncFolderPath syncFolderPath)
```

**描述**

应用取消注册同步根。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk\_SyncFolderPath syncFolderPath | 需要取消注册的同步根路径，参考：[CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，返回[CLOUD\_DISK\_OK](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)。 |

### OH\_CloudDisk\_ActiveSyncFolder()

PC/2in1Tablet

```
1. CloudDisk_ErrorCode OH_CloudDisk_ActiveSyncFolder(const CloudDisk_SyncFolderPath syncFolderPath)
```

**描述**

应用激活同步根。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk\_SyncFolderPath syncFolderPath | 需要激活监听的同步根路径，参考：[CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，返回[CLOUD\_DISK\_OK](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)。 |

### OH\_CloudDisk\_DeactiveSyncFolder()

PC/2in1Tablet

```
1. CloudDisk_ErrorCode OH_CloudDisk_DeactiveSyncFolder(const CloudDisk_SyncFolderPath syncFolderPath)
```

**描述**

应用取消激活同步根。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk\_SyncFolderPath syncFolderPath | 取消激活监听的同步根路径，参考：[CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，返回[CLOUD\_DISK\_OK](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)。 |

### OH\_CloudDisk\_GetSyncFolders()

PC/2in1Tablet

```
1. CloudDisk_ErrorCode OH_CloudDisk_GetSyncFolders(CloudDisk_SyncFolder **syncFolders, size_t *count)
```

**描述**

应用获取所有同步根。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CloudDisk\_SyncFolder](capi-clouddisk-clouddisk-syncfolder.md) \*\*syncFolders | 输出参数。返回同步根路径数组[CloudDisk\_SyncFolder](capi-clouddisk-clouddisk-syncfolder.md)。 |
| size\_t \*count | 输出参数。当前网盘注册的所有同步根的数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，返回[CLOUD\_DISK\_OK](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)。 |

### OH\_CloudDisk\_UpdateCustomAlias()

PC/2in1Tablet

```
1. CloudDisk_ErrorCode OH_CloudDisk_UpdateCustomAlias(const CloudDisk_SyncFolderPath syncFolderPath, const char *customAlias, size_t customAliasLength)
```

**描述**

应用更新同步根别名。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk\_SyncFolderPath syncFolderPath | 待更新别名的同步根路径，参考：[CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md)。 |
| const char \*customAlias | 用户定义的别名，不能包含字符：\/\*?<>|:"，以及不能以"."、".."和纯空格作为完整名称。 |
| size\_t customAliasLength | 用户定义的别名长度，范围：[0, 255]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，返回[CLOUD\_DISK\_OK](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)。 |
