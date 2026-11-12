---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-filemanager-service-h
title: filemanager_service.h
breadcrumb: API参考 > 应用服务 > File Manager Service Kit（文件管理服务） > C API > 头文件和结构体 > 头文件 > filemanager_service.h
category: harmonyos-references
scraped_at: 2026-11-12T09:57:16+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:9dc45dcfe1501a7dd68cbeb00611643cf9270db4e9fb5716eb5adbcd8875c186
---

## 概述

声明文件管理服务的数据结构和函数。

**库：** libfilemanager\_service\_ndk.z.so

**起始版本：** 26.0.1

**相关模块：** [FileManagerService](capi-filemanagerservice.md)

## 汇总

### 结构体

| 名称 | 描述 |
| --- | --- |
| [HMS\_FileManagerService\_SidebarFolder](capi-filemanagerservice-hms-sidebarfolder.md) | 侧边栏文件夹数据结构。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [HMS\_FileManagerService\_ErrCode](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) | HMS\_FileManagerService\_ErrCode | 定义文件管理服务错误码。 |
| [HMS\_FileManagerService\_SupportFolderType](capi-filemanager-service-h.md#hms_filemanagerservice_supportfoldertype) | HMS\_FileManagerService\_SupportFolderType | 支持的文件夹类型枚举值。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [HMS\_FileManagerService\_ErrCode HMS\_FileManagerService\_AddToSidebar(HMS\_FileManagerService\_SupportFolderType folderType, const HMS\_FileManagerService\_SidebarFolder \*sidebarFolder)](capi-filemanager-service-h.md#hms_filemanagerservice_addtosidebar) | 将文件夹添加到侧边栏。 |
| [HMS\_FileManagerService\_ErrCode HMS\_FileManagerService\_RemoveFromSidebar(HMS\_FileManagerService\_SupportFolderType folderType, const char \*uri)](capi-filemanager-service-h.md#hms_filemanagerservice_removefromsidebar) | 从侧边栏删除文件夹。 |
| [HMS\_FileManagerService\_ErrCode HMS\_FileManagerService\_SetFolderIcon(HMS\_FileManagerService\_SupportFolderType folderType, const char \*uri, const char \*iconResId)](capi-filemanager-service-h.md#hms_filemanagerservice_setfoldericon) | 设置文件夹图标。 |
| [HMS\_FileManagerService\_ErrCode HMS\_FileManagerService\_UnSetFolderIcon(HMS\_FileManagerService\_SupportFolderType folderType, const char \*uri)](capi-filemanager-service-h.md#hms_filemanagerservice_unsetfoldericon) | 取消设置文件夹图标。 |

## 枚举类型说明

### HMS\_FileManagerService\_ErrCode

```c
enum HMS_FileManagerService_ErrCode
```

**描述：**

定义文件管理服务错误码。

**起始版本：** 26.0.1

| 枚举项 | 描述 |
| --- | --- |
| HMS\_FILEMANAGERSERVICE\_ERRCODE\_SUCCESS = 0 | 执行成功。 |
| HMS\_FILEMANAGERSERVICE\_ERRCODE\_PERMISSION\_DENIED = 201 | 权限校验失败，应用无权限使用该API，需要申请权限。 |
| HMS\_FILEMANAGERSERVICE\_ERRCODE\_PARAM\_ERROR = 401 | 参数错误。 |
| HMS\_FILEMANAGERSERVICE\_ERRCODE\_SERVICE\_ERROR = 1014000004 | 服务错误。 |
| HMS\_FILEMANAGERSERVICE\_ERRCODE\_NOT\_SYNC\_FOLDER = 1014015024 | 文件夹非云盘同步文件夹。 |
| HMS\_FILEMANAGERSERVICE\_ERRCODE\_BUNDLE\_NAME\_MISMATCH = 1014015026 | 不允许操作其它应用添加的内容。 |
| HMS\_FILEMANAGERSERVICE\_ERRCODE\_URI\_NOT\_EXIST = 1014015027 | URI不存在。 |
| HMS\_FILEMANAGERSERVICE\_ERRCODE\_SIDEBAR\_FOLDER\_ALREADY\_EXIST = 1014015028 | 侧边栏文件夹已存在。 |
| HMS\_FILEMANAGERSERVICE\_ERRCODE\_SIDEBAR\_FOLDER\_NOT\_EXIST = 1014015029 | URI未位于侧边栏中。 |

### HMS\_FileManagerService\_SupportFolderType

```c
enum HMS_FileManagerService_SupportFolderType
```

**描述：**

支持的文件夹类型枚举值。

**起始版本：** 26.0.1

| 枚举项 | 描述 |
| --- | --- |
| HMS\_FILEMANAGERSERVICE\_FOLDER\_TYPE\_CLOUD = 0 | 云文件夹。 |

## 函数说明

### HMS\_FileManagerService\_AddToSidebar()

```c
HMS_FileManagerService_ErrCode HMS_FileManagerService_AddToSidebar(HMS_FileManagerService_SupportFolderType folderType, const HMS_FileManagerService_SidebarFolder *sidebarFolder)
```

**描述：**

将文件夹添加到侧边栏。

**需要权限：** ohos.permission.SYNC\_ROOT\_MANAGER

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HMS\_FileManagerService\_SupportFolderType](capi-filemanager-service-h.md#hms_filemanagerservice_supportfoldertype) folderType | 文件夹类型。 |
| [const HMS\_FileManagerService\_SidebarFolder](capi-filemanagerservice-hms-sidebarfolder.md) \*sidebarFolder | 要添加的侧边栏文件夹。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HMS\_FileManagerService\_ErrCode](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) | 操作结果码。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_SUCCESS](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 0 -执行成功。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_PERMISSION\_DENIED](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 201 -权限校验失败，应用无权限使用该API，需要申请权限。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_SERVICE\_ERROR](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 1014000004 -服务错误。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_NOT\_SYNC\_FOLDER](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 1014015024 -文件夹非云盘同步文件夹。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_URI\_NOT\_EXIST](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 1014015027 -URI不存在。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_SIDEBAR\_FOLDER\_ALREADY\_EXIST](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 1014015028 -侧边栏文件夹已存在。 |

### HMS\_FileManagerService\_RemoveFromSidebar()

```c
HMS_FileManagerService_ErrCode HMS_FileManagerService_RemoveFromSidebar(HMS_FileManagerService_SupportFolderType folderType, const char *uri)
```

**描述：**

从侧边栏删除文件夹。

**需要权限：** ohos.permission.SYNC\_ROOT\_MANAGER

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HMS\_FileManagerService\_SupportFolderType](capi-filemanager-service-h.md#hms_filemanagerservice_supportfoldertype) folderType | 文件夹类型。 |
| const char \*uri | 要删除的侧边栏文件夹的URI。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HMS\_FileManagerService\_ErrCode](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) | 操作结果码。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_SUCCESS](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 0 -执行成功。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_PERMISSION\_DENIED](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 201 -权限校验失败，应用无权限使用该API，需要申请权限。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_SERVICE\_ERROR](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 1014000004 -服务错误。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_NOT\_SYNC\_FOLDER](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 1014015024 -文件夹非云盘同步文件夹。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_BUNDLE\_NAME\_MISMATCH](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 1014015026 -不允许操作其它应用添加的内容。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_URI\_NOT\_EXIST](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 1014015027 -URI不存在。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_SIDEBAR\_FOLDER\_NOT\_EXIST](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 1014015029 -URI未位于侧边栏中。 |

### HMS\_FileManagerService\_SetFolderIcon()

```c
HMS_FileManagerService_ErrCode HMS_FileManagerService_SetFolderIcon(HMS_FileManagerService_SupportFolderType folderType, const char *uri, const char *iconResId)
```

**描述：**

设置文件夹图标。

**需要权限：** ohos.permission.SYNC\_ROOT\_MANAGER

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HMS\_FileManagerService\_SupportFolderType](capi-filemanager-service-h.md#hms_filemanagerservice_supportfoldertype) folderType | 文件夹类型。 |
| const char \*uri | 需要设置图标的文件夹的URI。 |
| const char \*iconResId | 图标资源ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HMS\_FileManagerService\_ErrCode](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) | 操作结果码。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_SUCCESS](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 0 -执行成功。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_PERMISSION\_DENIED](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 201 -权限校验失败，应用无权限使用该API，需要申请权限。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_SERVICE\_ERROR](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 1014000004 -服务错误。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_NOT\_SYNC\_FOLDER](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 1014015024 -文件夹非云盘同步文件夹。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_BUNDLE\_NAME\_MISMATCH](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 1014015026 -不允许操作其它应用添加的内容。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_URI\_NOT\_EXIST](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 1014015027 -URI不存在。 |

### HMS\_FileManagerService\_UnSetFolderIcon()

```c
HMS_FileManagerService_ErrCode HMS_FileManagerService_UnSetFolderIcon(HMS_FileManagerService_SupportFolderType folderType, const char *uri)
```

**描述：**

取消设置文件夹图标。

**需要权限：** ohos.permission.SYNC\_ROOT\_MANAGER

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HMS\_FileManagerService\_SupportFolderType](capi-filemanager-service-h.md#hms_filemanagerservice_supportfoldertype) folderType | 文件夹类型。 |
| const char \*uri | 需要取消设置图标的文件夹的URI。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HMS\_FileManagerService\_ErrCode](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) | 操作结果码。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_SUCCESS](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 0 -执行成功。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_PERMISSION\_DENIED](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 201 -权限校验失败，应用无权限使用该API，需要申请权限。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_SERVICE\_ERROR](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 1014000004 -服务错误。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_NOT\_SYNC\_FOLDER](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 1014015024 -文件夹非云盘同步文件夹。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_BUNDLE\_NAME\_MISMATCH](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 1014015026 -不允许操作其它应用添加的内容。  [HMS\_FILEMANAGERSERVICE\_ERRCODE\_URI\_NOT\_EXIST](capi-filemanager-service-h.md#hms_filemanagerservice_errcode) 1014015027 -URI不存在。 |
