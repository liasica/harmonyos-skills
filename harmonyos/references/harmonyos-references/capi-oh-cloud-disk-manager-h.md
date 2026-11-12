---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-cloud-disk-manager-h
title: oh_cloud_disk_manager.h
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 头文件 > oh_cloud_disk_manager.h
category: harmonyos-references
scraped_at: 2026-11-12T09:55:06+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:c869f2c3ee5c859be642e26fadd1dbae6c33ac14dcd98145935215e280e14e3c
---

## 概述

云盘管理模块的接口定义，提供云盘同步根路径的注册、激活、监听和查询能力，支持监听文件变更、设置和查询文件同步状态，以及创建、判断、转换占位符文件和更新文件元数据，适用于需要在应用内实现云盘文件同步和变更监听的场景。

**引用文件：** <filemanagement/clouddiskmanager/oh\_cloud\_disk\_manager.h>

**库：** libohclouddiskmanager.so

**系统能力：** SystemCapability.FileManagement.CloudDiskManager

**起始版本：** 21

**相关模块：** [CloudDisk](capi-clouddisk.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md) | CloudDisk\_PathInfo/CloudDisk\_FileIdInfo/CloudDisk\_SyncFolderPath | CloudDisk\_PathInfo：文件路径信息。  CloudDisk\_FileIdInfo：定义的文件ID。  CloudDisk\_SyncFolderPath：定义的同步根路径。 |
| [CloudDisk\_FileSyncState](capi-clouddisk-clouddisk-filesyncstate.md) | CloudDisk\_FileSyncState | 文件的同步状态。 |
| [CloudDisk\_ChangeData](capi-clouddisk-clouddisk-changedata.md) | CloudDisk\_ChangeData | 定义了同步根路径下单个文件变更事件的数据结构。该结构包含有关文件变更的详细信息，包括唯一ID、父目录的唯一ID、相对路径、变更类型、文件大小和时间戳。 |
| [CloudDisk\_ChangesResult](capi-clouddisk-clouddisk-changesresult.md) | CloudDisk\_ChangesResult | 查询同步根路径中文件变更的结果。该结构体包含同步根路径中文件的变更数据，包括下一个更新序列号、结尾标志以及变更数据项数组。 |
| [CloudDisk\_FailedList](capi-clouddisk-clouddisk-failedlist.md) | CloudDisk\_FailedList | 同步操作中失败的文件列表信息。该结构包含文件路径信息以及失败的具体错误原因。 |
| [CloudDisk\_ResultList](capi-clouddisk-clouddisk-resultlist.md) | CloudDisk\_ResultList | 表示一个文件同步操作的结果。该结构体包含文件的绝对路径、同步结果，以及同步状态或失败原因。 |
| [CloudDisk\_DisplayNameInfo](capi-clouddisk-clouddisk-displaynameinfo.md) | CloudDisk\_DisplayNameInfo | 定义同步根路径的显示名称信息。 |
| [CloudDisk\_SyncFolder](capi-clouddisk-clouddisk-syncfolder.md) | CloudDisk\_SyncFolder | 同步根路径属性信息。 |
| [OH\_CloudDisk\_PlaceholderInfo](capi-clouddisk-oh-clouddisk-placeholderinfo.md) | OH\_CloudDisk\_PlaceholderInfo | 占位符相关操作使用的文件元数据信息。 |
| [OH\_CloudDisk\_PlaceholderCustomInfo](capi-clouddisk-oh-clouddisk-placeholdercustominfo.md) | OH\_CloudDisk\_PlaceholderCustomInfo | 与占位符关联的不透明自定义信息。 |
| [OH\_CloudDisk\_SyncFolderEx](capi-clouddisk-oh-clouddisk-syncfolderex.md) | OH\_CloudDisk\_SyncFolderEx | 支持占位符的同步根路径属性信息。使用时必须将版本字段设置为有效的版本宏(例如[OH\_CLOUD\_DISK\_SYNC\_FOLDER\_EX\_VERSION\_1](capi-oh-cloud-disk-manager-h.md#宏定义))，然后才能传递结构到任何API。运行时使用版本来确定字段有效；当指定低版本时，在较高版本中引入的字段将被忽略。 |
| [OH\_CloudDisk\_DataBuf](capi-clouddisk-oh-clouddisk-databuf.md) | OH\_CloudDisk\_DataBuf | 云盘数据缓冲区信息。 |
| [OH\_CloudDisk\_CallbackReqHead](capi-clouddisk-oh-clouddisk-callbackreqhead.md) | OH\_CloudDisk\_CallbackReqHead | 云盘回调请求头信息。 |
| [OH\_CloudDisk\_DehydrateInfo](capi-clouddisk-oh-clouddisk-dehydrateinfo.md) | OH\_CloudDisk\_DehydrateInfo | 脱水授权信息。 |
| [OH\_CloudDisk\_FetchDataRequest](capi-clouddisk-oh-clouddisk-fetchdatarequest.md) | OH\_CloudDisk\_FetchDataRequest | 获取数据请求信息。 |
| [OH\_CloudDisk\_CallbackContext](capi-clouddisk-oh-clouddisk-callbackcontext.md) | OH\_CloudDisk\_CallbackContext | 回调请求上下文信息联合体。 |
| [OH\_CloudDisk\_FetchData](capi-clouddisk-oh-clouddisk-fetchdata.md) | OH\_CloudDisk\_FetchData | 云端文件数据获取结果。 |
| [OH\_CloudDisk\_CallbackResponse](capi-clouddisk-oh-clouddisk-callbackresponse.md) | OH\_CloudDisk\_CallbackResponse | 回调响应信息联合体。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [CloudDisk\_SyncState](capi-oh-cloud-disk-manager-h.md#clouddisk_syncstate) | CloudDisk\_SyncState | 文件同步状态的枚举值。 |
| [CloudDisk\_OperationType](capi-oh-cloud-disk-manager-h.md#clouddisk_operationtype) | CloudDisk\_OperationType | 文件变更类型枚举值。 |
| [CloudDisk\_ErrorReason](capi-oh-cloud-disk-manager-h.md#clouddisk_errorreason) | CloudDisk\_ErrorReason | 文件同步失败原因的枚举值。 |
| [CloudDisk\_SyncFolderState](capi-oh-cloud-disk-manager-h.md#clouddisk_syncfolderstate) | CloudDisk\_SyncFolderState | 同步根路径状态的枚举值。 |
| [OH\_CloudDisk\_CallbackType](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_callbacktype) | OH\_CloudDisk\_CallbackType | 云盘回调类型枚举值。 |
| [OH\_CloudDisk\_HydratePriority](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_hydratepriority) | OH\_CloudDisk\_HydratePriority | 水合优先级枚举值。 |
| [OH\_CloudDisk\_PlaceholderState](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_placeholderstate) | OH\_CloudDisk\_PlaceholderState | 占位符状态的枚举值。 |

### 宏定义

| 名称 | 描述 |
| --- | --- |
| OH\_CLOUD\_DISK\_SYNC\_FOLDER\_EX\_VERSION\_1 1 | 用于标识OH\_CloudDisk\_SyncFolderEx结构体的版本。当结构体扩展新字段时，将定义新的版本宏。代码运行时通过版本信息确定有效字段，读取方应先校验OH\_CloudDisk\_SyncFolderEx结构体中的version再访问对应字段，避免访问未定义内存。  **起始版本：** 26.0.1 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_RegisterSyncFolderChanges(const CloudDisk\_SyncFolderPath syncFolderPath, void (\*callback)(const CloudDisk\_SyncFolderPath syncFolderPath, const CloudDisk\_ChangeData changeDatas[], size\_t bufferLength))](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-cloud-disk-manager-h#oh_clouddisk_registersyncfolderchanges) | 应用注册一个回调函数，用于获取同步根路径下文件的变更，适用于需要实时监听同步根路径下文件创建、删除、修改等变更事件的场景。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_UnregisterSyncFolderChanges(const CloudDisk\_SyncFolderPath syncFolderPath)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_unregistersyncfolderchanges) | 应用取消注册同步根路径下文件变更的回调，适用于应用不再需要监听文件变更、切换账号或释放监听资源的场景。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_GetSyncFolderChanges(const CloudDisk\_SyncFolderPath syncFolderPath, uint64\_t startUsn, size\_t count, CloudDisk\_ChangesResult \*\*changesResult)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_getsyncfolderchanges) | 应用获取同步根路径下的历史操作记录，适用于按需查询文件变更历史、断线重连后恢复同步进度或排查同步问题的场景。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_SetFileSyncStates(const CloudDisk\_SyncFolderPath syncFolderPath, const CloudDisk\_FileSyncState fileSyncStates[], size\_t bufferLength, CloudDisk\_FailedList \*\*failedLists, size\_t \*failedCount)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-cloud-disk-manager-h#oh_clouddisk_setfilesyncstates) | 应用设置同步根路径下文件的同步状态，适用于需要手动控制文件同步行为的场景。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_GetFileSyncStates(const CloudDisk\_SyncFolderPath syncFolderPath, const CloudDisk\_PathInfo paths[], size\_t bufferLength, CloudDisk\_ResultList \*\*resultLists, size\_t \*resultCount)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-cloud-disk-manager-h#oh_clouddisk_getfilesyncstates) | 应用查询同步根路径下文件同步状态，适用于需要在界面显示同步状态、判断文件是否已完成同步或检查文件同步是否失败的场景。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_RegisterSyncFolder(const CloudDisk\_SyncFolder \*syncFolder)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_registersyncfolder) | 应用注册同步根，适用于需要将本地目录设置为云盘同步目录的场景。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_UnregisterSyncFolder(const CloudDisk\_SyncFolderPath syncFolderPath)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_unregistersyncfolder) | 应用取消注册同步根，适用于需要移除云盘同步目录的场景。通常在取消激活同步根后调用。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_ActiveSyncFolder(const CloudDisk\_SyncFolderPath syncFolderPath)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_activesyncfolder) | 应用激活同步根，适用于需要开始或恢复同步文件的场景。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_DeactiveSyncFolder(const CloudDisk\_SyncFolderPath syncFolderPath)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_deactivesyncfolder) | 应用取消激活同步根，适用于需要暂停同步文件或释放同步资源的场景。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_GetSyncFolders(CloudDisk\_SyncFolder \*\*syncFolders, size\_t \*count)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_getsyncfolders) | 应用获取所有同步根，适用于查询当前已注册的同步目录、展示同步目录列表或恢复同步状态的场景。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_UpdateCustomAlias(const CloudDisk\_SyncFolderPath syncFolderPath, const char \*customAlias, size\_t customAliasLength)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_updatecustomalias) | 应用更新同步根别名，适用于需要为同步目录设置自定义显示名称、区分多个同步目录或在界面显示友好目录名称的场景。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_CreatePlaceholder(const CloudDisk\_SyncFolderPath syncFolderPath, const CloudDisk\_PathInfo relativePathInfo, const OH\_CloudDisk\_PlaceholderInfo placeholderInfo, const OH\_CloudDisk\_PlaceholderCustomInfo \*customInfo)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_createplaceholder) | 在已注册的同步根路径下创建占位符文件。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_IsPlaceholderFile(const CloudDisk\_SyncFolderPath syncFolderPath, const CloudDisk\_PathInfo relativePathInfo, bool \*isPlaceholder)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_isplaceholderfile) | 判断已注册的同步根路径下的文件是否为占位符文件。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_GetPlaceholderState(const CloudDisk\_SyncFolderPath syncFolderPath, const CloudDisk\_PathInfo relativePathInfo, OH\_CloudDisk\_PlaceholderState \*state)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_getplaceholderstate) | 获取已注册的同步根路径下文件的占位符状态。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_ConvertPlaceholderToFile(const CloudDisk\_SyncFolderPath syncFolderPath, const CloudDisk\_PathInfo relativePathInfo)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_convertplaceholdertofile) | 将已注册的同步根路径下的占位符文件转换为0字节的普通文件。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_MarkFileAsPlaceholder(const CloudDisk\_SyncFolderPath syncFolderPath, const CloudDisk\_PathInfo relativePathInfo)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_markfileasplaceholder) | 将普通文件标记为完全水合的占位符文件，不改变其数据或元数据。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_UnmarkPlaceholderFile(const CloudDisk\_SyncFolderPath syncFolderPath, const CloudDisk\_PathInfo relativePathInfo)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_unmarkplaceholderfile) | 将完全水合的占位符文件转换为普通文件，不改变其数据或元数据。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_HydratePlaceholder(const CloudDisk\_SyncFolderPath \*syncFolderPath, const CloudDisk\_PathInfo \*filePath, OH\_CloudDisk\_CallbackType type, OH\_CloudDisk\_HydratePriority priority)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_hydrateplaceholder) | 主动水合占位符文件或取消水合。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_Execute(const OH\_CloudDisk\_CallbackReqHead reqHead, OH\_CloudDisk\_CallbackContext reqContext, OH\_CloudDisk\_CallbackResponse rsp)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_execute) | 响应回调请求。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_DehydrateFile(const CloudDisk\_SyncFolderPath \*syncFolderPath, const CloudDisk\_PathInfo \*filePath)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_dehydratefile) | 对完全或部分水合的占位符文件执行脱水。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_UpdatePlaceholder(const CloudDisk\_SyncFolderPath syncFolderPath, const CloudDisk\_PathInfo relativePathInfo, const OH\_CloudDisk\_PlaceholderInfo placeholderInfo, const OH\_CloudDisk\_PlaceholderCustomInfo \*customInfo)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_updateplaceholder) | 更新文件元数据，支持占位符文件和普通文件。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_GetPlaceholderCustomInfo(const CloudDisk\_SyncFolderPath syncFolderPath, const CloudDisk\_PathInfo relativePathInfo, uint8\_t \*dataBuf, size\_t \*inOutDataLength)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_getplaceholdercustominfo) | 获取与占位符关联的不透明自定义信息。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_RegisterCallbackTable(const CloudDisk\_SyncFolderPath syncFolderPath, void (\*callback)(const OH\_CloudDisk\_CallbackReqHead reqHead, OH\_CloudDisk\_CallbackContext reqContext))](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_registercallbacktable) | 注册用于水合和脱水请求的回调表。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_UnregisterCallbackTable(const CloudDisk\_SyncFolderPath syncFolderPath)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_unregistercallbacktable) | 取消注册用于水合和脱水请求的回调表。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_RegisterSyncFolderEx(const OH\_CloudDisk\_SyncFolderEx \*syncFolder)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_registersyncfolderex) | 应用注册带占位符信息的同步根。 |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_GetSyncFoldersEx(OH\_CloudDisk\_SyncFolderEx \*\*syncFolders, size\_t \*count)](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_getsyncfoldersex) | 应用获取所有带占位符信息的同步根。 |

## 枚举类型说明

### CloudDisk\_SyncState

```c
enum CloudDisk_SyncState
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

```c
enum CloudDisk_OperationType
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
| OH\_CLOUD\_DISK\_CLOSE\_MODIFY = 6 | 修改内容后关闭文件。  **起始版本：** 26.0.1 |

### CloudDisk\_ErrorReason

```c
enum CloudDisk_ErrorReason
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

```c
enum CloudDisk_SyncFolderState
```

**描述**

同步根路径状态的枚举值。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| INACTIVE = 0 | 表示同步根路径的状态是未激活的。 |
| ACTIVE = 1 | 表示同步根路径的状态是激活的。 |

### OH\_CloudDisk\_CallbackType

```c
enum OH_CloudDisk_CallbackType
```

**描述**

云盘回调类型枚举值。

**起始版本：** 26.0.1

| 枚举项 | 描述 |
| --- | --- |
| OH\_CLOUD\_DISK\_CALLBACK\_TYPE\_FETCH\_DATA = 0 | 获取云端文件数据，用于水合。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_CALLBACK\_TYPE\_CANCEL\_FETCH\_DATA = 1 | 取消获取云端文件数据。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_CALLBACK\_TYPE\_DEHYDRATE = 2 | 请求脱水授权。  **起始版本：** 26.0.1 |

### OH\_CloudDisk\_HydratePriority

```c
enum OH_CloudDisk_HydratePriority
```

**描述**

水合优先级枚举值。

**起始版本：** 26.0.1

| 枚举项 | 描述 |
| --- | --- |
| OH\_CLOUD\_DISK\_HYDRATE\_PRIORITY\_LOW = 0 | 低优先级。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_HYDRATE\_PRIORITY\_NORMAL = 1 | 常规优先级。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_HYDRATE\_PRIORITY\_HIGH = 2 | 高优先级。  **起始版本：** 26.0.1 |

### OH\_CloudDisk\_PlaceholderState

```c
enum OH_CloudDisk_PlaceholderState
```

**描述**

占位符状态的枚举值。

**起始版本：** 26.0.1

| 枚举项 | 描述 |
| --- | --- |
| OH\_CLOUD\_DISK\_PLACEHOLDER\_STATE\_NONE = 0 | 该文件不是占位符。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_PLACEHOLDER\_STATE\_UNHYDRATED = 1 | 占位符没有本地数据。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_PLACEHOLDER\_STATE\_PARTIALLY\_HYDRATED = 2 | 占位符有部分本地数据。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_PLACEHOLDER\_STATE\_FULLY\_HYDRATED = 3 | 占位符有完整的本地数据。  **起始版本：** 26.0.1 |

## 函数说明

### OH\_CloudDisk\_RegisterSyncFolderChanges()

```c
CloudDisk_ErrorCode OH_CloudDisk_RegisterSyncFolderChanges(const CloudDisk_SyncFolderPath syncFolderPath, void (*callback)(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_ChangeData changeDatas[], size_t bufferLength))
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

```c
CloudDisk_ErrorCode OH_CloudDisk_UnregisterSyncFolderChanges(const CloudDisk_SyncFolderPath syncFolderPath)
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

```c
CloudDisk_ErrorCode OH_CloudDisk_GetSyncFolderChanges(const CloudDisk_SyncFolderPath syncFolderPath, uint64_t startUsn, size_t count, CloudDisk_ChangesResult **changesResult)
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

```c
CloudDisk_ErrorCode OH_CloudDisk_SetFileSyncStates(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_FileSyncState fileSyncStates[], size_t bufferLength, CloudDisk_FailedList **failedLists, size_t *failedCount)
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

```c
CloudDisk_ErrorCode OH_CloudDisk_GetFileSyncStates(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_PathInfo paths[], size_t bufferLength, CloudDisk_ResultList **resultLists, size_t *resultCount)
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

```c
CloudDisk_ErrorCode OH_CloudDisk_RegisterSyncFolder(const CloudDisk_SyncFolder *syncFolder)
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

### OH\_CloudDisk\_RegisterSyncFolderEx()

```c
CloudDisk_ErrorCode OH_CloudDisk_RegisterSyncFolderEx(const OH_CloudDisk_SyncFolderEx *syncFolder)
```

**描述**

应用注册带占位符信息的同步根，适用于需要将本地目录设置为云盘同步目录并标记是否支持占位符的场景。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_CloudDisk\_SyncFolderEx](capi-clouddisk-oh-clouddisk-syncfolderex.md) \*syncFolder | 待注册的带占位符同步根路径。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，返回[CLOUD\_DISK\_OK](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)。 |

### OH\_CloudDisk\_UnregisterSyncFolder()

```c
CloudDisk_ErrorCode OH_CloudDisk_UnregisterSyncFolder(const CloudDisk_SyncFolderPath syncFolderPath)
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

```c
CloudDisk_ErrorCode OH_CloudDisk_ActiveSyncFolder(const CloudDisk_SyncFolderPath syncFolderPath)
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

```c
CloudDisk_ErrorCode OH_CloudDisk_DeactiveSyncFolder(const CloudDisk_SyncFolderPath syncFolderPath)
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

```c
CloudDisk_ErrorCode OH_CloudDisk_GetSyncFolders(CloudDisk_SyncFolder **syncFolders, size_t *count)
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

### OH\_CloudDisk\_GetSyncFoldersEx()

```c
CloudDisk_ErrorCode OH_CloudDisk_GetSyncFoldersEx(OH_CloudDisk_SyncFolderEx **syncFolders, size_t *count)
```

**描述**

应用获取所有带占位符的同步根，适用于查询当前已注册的带占位符的同步目录、展示同步目录列表或恢复同步状态的场景。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CloudDisk\_SyncFolderEx](capi-clouddisk-oh-clouddisk-syncfolderex.md) \*\*syncFolders | 输出参数。返回带占位符的同步根路径数组[OH\_CloudDisk\_SyncFolderEx](capi-clouddisk-oh-clouddisk-syncfolderex.md)。 |
| size\_t \*count | 输出参数。当前应用注册的带占位符同步根数量。当没有带占位符同步根时为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，返回[CLOUD\_DISK\_OK](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode)。 |

### OH\_CloudDisk\_UpdateCustomAlias()

```c
CloudDisk_ErrorCode OH_CloudDisk_UpdateCustomAlias(const CloudDisk_SyncFolderPath syncFolderPath, const char *customAlias, size_t customAliasLength)
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

### OH\_CloudDisk\_CreatePlaceholder()

```c
CloudDisk_ErrorCode OH_CloudDisk_CreatePlaceholder(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_PathInfo relativePathInfo, const OH_CloudDisk_PlaceholderInfo placeholderInfo, const OH_CloudDisk_PlaceholderCustomInfo *customInfo)
```

**描述**

在已注册的同步根路径下创建占位符文件。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk\_SyncFolderPath syncFolderPath | 已注册的同步根路径。 |
| [const CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md) relativePathInfo | 占位符文件在同步根路径下的相对路径。路径不能为空，不能以"/"开头或结尾，且不能包含"./"、"../"路径段。 |
| [const OH\_CloudDisk\_PlaceholderInfo](capi-clouddisk-oh-clouddisk-placeholderinfo.md) placeholderInfo | 创建占位符文件时使用的元数据。 |
| [const OH\_CloudDisk\_PlaceholderCustomInfo](capi-clouddisk-oh-clouddisk-placeholdercustominfo.md) \*customInfo | 可选的不透明自定义信息。传NULL表示不提供。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，则返回CLOUD\_DISK\_OK；否则返回云盘管理模块的错误码CloudDisk\_ErrorCode。 |

### OH\_CloudDisk\_IsPlaceholderFile()

```c
CloudDisk_ErrorCode OH_CloudDisk_IsPlaceholderFile(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_PathInfo relativePathInfo, bool *isPlaceholder)
```

**描述**

判断已注册的同步根路径下的指定文件是否为占位符文件。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk\_SyncFolderPath syncFolderPath | 已注册的同步根路径。 |
| [const CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md) relativePathInfo | 同步根路径下待检查文件的相对路径，参考：[CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md)。 |
| bool \*isPlaceholder | 输出参数。返回值为CLOUD\_DISK\_OK时该参数有效。true表示该文件是占位符文件；false表示该文件不是占位符文件。当返回非CLOUD\_DISK\_NOT\_SUPPORTED的错误码时，该值被设置为false；当返回CLOUD\_DISK\_NOT\_SUPPORTED时，该值不被修改。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，则返回CLOUD\_DISK\_OK；如果当前设备不支持此功能，则返回CLOUD\_DISK\_NOT\_SUPPORTED；否则返回云盘管理模块的错误码CloudDisk\_ErrorCode。 |

### OH\_CloudDisk\_ConvertPlaceholderToFile()

```c
CloudDisk_ErrorCode OH_CloudDisk_ConvertPlaceholderToFile(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_PathInfo relativePathInfo)
```

**描述**

将已注册的同步根路径下的占位符文件转换为0字节的普通文件。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk\_SyncFolderPath syncFolderPath | 已注册的同步根路径。 |
| [const CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md) relativePathInfo | 同步根路径下待转换的占位符文件相对路径信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，则返回CLOUD\_DISK\_OK；如果文件不是占位符，则返回OH\_CLOUD\_DISK\_NOT\_A\_PLACEHOLDER；否则返回云盘管理模块的错误码CloudDisk\_ErrorCode。 |

### OH\_CloudDisk\_GetPlaceholderState()

```c
CloudDisk_ErrorCode OH_CloudDisk_GetPlaceholderState(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_PathInfo relativePathInfo, OH_CloudDisk_PlaceholderState *state)
```

**描述**

获取已注册的同步根路径下文件的占位符状态。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk\_SyncFolderPath syncFolderPath | 已注册的同步根路径。 |
| [const CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md) relativePathInfo | 同步根路径下待查询文件的相对路径信息。 |
| [OH\_CloudDisk\_PlaceholderState](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_placeholderstate) \*state | 输出参数。占位符状态。报错时该值将被置为OH\_CLOUD\_DISK\_PLACEHOLDER\_STATE\_NONE。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，则返回CLOUD\_DISK\_OK；如果存储的状态无效，则返回OH\_CLOUD\_DISK\_INVALID\_PLACEHOLDER\_STATE；否则返回云盘管理模块的错误码CloudDisk\_ErrorCode。 |

### OH\_CloudDisk\_MarkFileAsPlaceholder()

```c
CloudDisk_ErrorCode OH_CloudDisk_MarkFileAsPlaceholder(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_PathInfo relativePathInfo)
```

**描述**

将普通文件标记为完全水合的占位符文件，不改变其数据或元数据。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk\_SyncFolderPath syncFolderPath | 已注册的同步根路径。 |
| [const CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md) relativePathInfo | 同步根路径下待标记文件的相对路径信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，则返回CLOUD\_DISK\_OK；如果文件已经是占位符，则返回OH\_CLOUD\_DISK\_IS\_A\_PLACEHOLDER；否则返回云盘管理模块的错误码CloudDisk\_ErrorCode。 |

### OH\_CloudDisk\_UnmarkPlaceholderFile()

```c
CloudDisk_ErrorCode OH_CloudDisk_UnmarkPlaceholderFile(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_PathInfo relativePathInfo)
```

**描述**

将完全水合的占位符文件转换为普通文件，不改变其数据或元数据。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk\_SyncFolderPath syncFolderPath | 已注册的同步根路径。 |
| [const CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md) relativePathInfo | 同步根路径下待转换的占位符文件相对路径信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，则返回CLOUD\_DISK\_OK；如果文件不是占位符，则返回OH\_CLOUD\_DISK\_NOT\_A\_PLACEHOLDER；如果未完全水合，则返回OH\_CLOUD\_DISK\_PLACEHOLDER\_NOT\_FULLY\_HYDRATED；否则返回云盘管理模块的错误码CloudDisk\_ErrorCode。 |

### OH\_CloudDisk\_HydratePlaceholder()

```c
CloudDisk_ErrorCode OH_CloudDisk_HydratePlaceholder(const CloudDisk_SyncFolderPath *syncFolderPath, const CloudDisk_PathInfo *filePath, OH_CloudDisk_CallbackType type, OH_CloudDisk_HydratePriority priority)
```

**描述**

主动水合占位符文件或取消水合，具体行为由[type](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_callbacktype)参数决定：取值为OH\_CLOUD\_DISK\_CALLBACK\_TYPE\_FETCH\_DATA时执行水合，取值为OH\_CLOUD\_DISK\_CALLBACK\_TYPE\_CANCEL\_FETCH\_DATA时取消水合。该函数在任务提交后返回，不等待回调或文件水合完成。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk\_SyncFolderPath \*syncFolderPath | 指向已注册的同步根路径信息的指针。 |
| [const CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md) \*filePath | 指向同步根路径下文件相对路径信息的指针。 |
| [OH\_CloudDisk\_CallbackType](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_callbacktype) type | 水合回调类型，必须为OH\_CLOUD\_DISK\_CALLBACK\_TYPE\_FETCH\_DATA或OH\_CLOUD\_DISK\_CALLBACK\_TYPE\_CANCEL\_FETCH\_DATA。 |
| [OH\_CloudDisk\_HydratePriority](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_hydratepriority) priority | 水合优先级。取消操作不使用此值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果任务已排队或取消，则返回CLOUD\_DISK\_OK；否则返回云盘管理模块的错误码CloudDisk\_ErrorCode。 |

### OH\_CloudDisk\_Execute()

```c
CloudDisk_ErrorCode OH_CloudDisk_Execute(const OH_CloudDisk_CallbackReqHead reqHead, OH_CloudDisk_CallbackContext reqContext, OH_CloudDisk_CallbackResponse rsp)
```

**描述**

响应回调请求，将获取的数据块写入活跃的占位符水合任务。单个数据块不能超过128KiB。函数在返回前会拷贝所有输入字段和数据。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_CloudDisk\_CallbackReqHead](capi-clouddisk-oh-clouddisk-callbackreqhead.md) reqHead | 应用接收到的回调请求头。 |
| [OH\_CloudDisk\_CallbackContext](capi-clouddisk-oh-clouddisk-callbackcontext.md) reqContext | 回调请求上下文，包含回调请求的相对文件路径。 |
| [OH\_CloudDisk\_CallbackResponse](capi-clouddisk-oh-clouddisk-callbackresponse.md) rsp | 应用提供的获取数据块。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，则返回CLOUD\_DISK\_OK；否则返回云盘管理模块的错误码CloudDisk\_ErrorCode。 |

### OH\_CloudDisk\_DehydrateFile()

```c
CloudDisk_ErrorCode OH_CloudDisk_DehydrateFile(const CloudDisk_SyncFolderPath *syncFolderPath, const CloudDisk_PathInfo *filePath)
```

**描述**

在应用授权后对完全或部分水合的占位符执行脱水操作。对于部分水合的占位符，已下载的数据将被丢弃。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk\_SyncFolderPath \*syncFolderPath | 指向已注册的同步根路径信息的指针。 |
| [const CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md) \*filePath | 指向同步根路径下文件相对路径信息的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，则返回CLOUD\_DISK\_OK；如果应用拒绝脱水，则返回OH\_CLOUD\_DISK\_DEHYDRATE\_DENIED；否则返回云盘管理模块的错误码CloudDisk\_ErrorCode。 |

### OH\_CloudDisk\_UpdatePlaceholder()

```c
CloudDisk_ErrorCode OH_CloudDisk_UpdatePlaceholder(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_PathInfo relativePathInfo, const OH_CloudDisk_PlaceholderInfo placeholderInfo, const OH_CloudDisk_PlaceholderCustomInfo *customInfo)
```

**描述**

更新同步根路径下文件的元数据，支持占位符文件和普通文件。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk\_SyncFolderPath syncFolderPath | 已注册的同步根路径。 |
| [const CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md) relativePathInfo | 待更新元数据的文件相对路径信息。 |
| [const OH\_CloudDisk\_PlaceholderInfo](capi-clouddisk-oh-clouddisk-placeholderinfo.md) placeholderInfo | 待更新的文件元数据信息，参考：[OH\_CloudDisk\_PlaceholderInfo](capi-clouddisk-oh-clouddisk-placeholderinfo.md)。 |
| [const OH\_CloudDisk\_PlaceholderCustomInfo](capi-clouddisk-oh-clouddisk-placeholdercustominfo.md) \*customInfo | 可选的不透明自定义信息。传NULL表示保留现有值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，则返回CLOUD\_DISK\_OK；否则返回云盘管理模块的错误码CloudDisk\_ErrorCode。 |

### OH\_CloudDisk\_GetPlaceholderCustomInfo()

```c
CloudDisk_ErrorCode OH_CloudDisk_GetPlaceholderCustomInfo(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_PathInfo relativePathInfo, uint8_t *dataBuf, size_t *inOutDataLength)
```

**描述**

获取与占位符关联的不透明自定义信息。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk\_SyncFolderPath syncFolderPath | 已注册的同步根路径。 |
| [const CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md) relativePathInfo | 同步根路径下待查询的占位符文件相对路径信息。 |
| uint8\_t \*dataBuf | 输出参数。调用方分配的输出缓冲区。如果缓冲区容量不足，函数执行返回错误码INVALID\_ARG。 |
| size\_t \*inOutDataLength | 输出参数。调用时传入预分配的缓冲区容量；函数执行完后，会被修改为实际写入的数据长度。如果缓冲区容量不足，函数执行返回错误码INVALID\_ARG，inOutDataLength被置为成功写入所需的数据长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，则返回CLOUD\_DISK\_OK；如果占位符没有自定义信息，则返回OH\_CLOUD\_DISK\_PLACEHOLDER\_CUSTOM\_INFO\_NOT\_FOUND；其他情况下报错返回云盘管理模块的错误码CloudDisk\_ErrorCode。 |

### OH\_CloudDisk\_RegisterCallbackTable()

```c
CloudDisk_ErrorCode OH_CloudDisk_RegisterCallbackTable(const CloudDisk_SyncFolderPath syncFolderPath, void (*callback)(const OH_CloudDisk_CallbackReqHead reqHead, OH_CloudDisk_CallbackContext reqContext))
```

**描述**

注册用于水合和脱水请求的回调表。

不同回调类型的处理方式如下：

- FETCH\_DATA：异步通知，应用必须在回调返回前深拷贝请求，并在稍后调用[OH\_CloudDisk\_Execute](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_execute)响应。

- CANCEL\_FETCH\_DATA：异步通知，应用必须停止匹配的下载，无需调用OH\_CloudDisk\_Execute作为确认。

- DEHYDRATE：同步通知，在回调返回前完成处理。

回调请求中的所有指针均为借用指针，仅在回调返回前有效。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk\_SyncFolderPath syncFolderPath | 已注册的同步根路径。 |
| void (\*callback)(const OH\_CloudDisk\_CallbackReqHead reqHead, OH\_CloudDisk\_CallbackContext reqContext) | 待注册的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，则返回CLOUD\_DISK\_OK；否则返回云盘管理模块的错误码CloudDisk\_ErrorCode。 |

### OH\_CloudDisk\_UnregisterCallbackTable()

```c
CloudDisk_ErrorCode OH_CloudDisk_UnregisterCallbackTable(const CloudDisk_SyncFolderPath syncFolderPath)
```

**描述**

取消注册用于水合和脱水请求的回调表。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk\_SyncFolderPath syncFolderPath | 已注册的同步根路径。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | 如果接口调用成功，则返回CLOUD\_DISK\_OK；否则返回云盘管理模块的错误码CloudDisk\_ErrorCode。 |
