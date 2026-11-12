---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/filemanagerservice-capi-sidebar
title: 管理侧边栏文件夹（C/C++）
breadcrumb: 指南 > 应用服务 > File Manager Service Kit（文件管理服务） > 管理侧边栏文件夹（C/C++）
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:23+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:da8e6712be3963c3a6c56ff8b70974f64bdfec164b092a2b5fa16f1f69266e7c
---

从26.0.1开始，新增支持将云盘同步文件夹添加到文件管理器侧边栏进行管理。

## 场景介绍

云盘应用将同步文件夹添加到文件管理器侧边栏后，用户可在文件管理器中直接访问该文件夹，无需打开云盘应用。典型场景包括：

* 添加侧边栏文件夹：将云盘同步文件夹添加到侧边栏，通过iconResId指定侧边栏中显示的图标，并设置显示名称、文件夹别名等属性。
* 删除侧边栏文件夹：将不再需要在侧边栏展示的文件夹移除。
* 设置文件夹图标：为文件管理器主视图中该文件夹设置自定义图标，与侧边栏图标相互独立。
* 取消设置文件夹图标：恢复文件管理器主视图中的文件夹默认图标，不影响文件夹在侧边栏中的展示。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [HMS\_FileManagerService\_AddToSidebar](../harmonyos-references/capi-filemanager-service-h.md#hms_filemanagerservice_addtosidebar)(HMS\_FileManagerService\_SupportFolderType folderType, const HMS\_FileManagerService\_SidebarFolder \*sidebarFolder) | 将文件夹添加到侧边栏。 |
| [HMS\_FileManagerService\_RemoveFromSidebar](../harmonyos-references/capi-filemanager-service-h.md#hms_filemanagerservice_removefromsidebar)(HMS\_FileManagerService\_SupportFolderType folderType, const char \*uri) | 从侧边栏删除文件夹。 |
| [HMS\_FileManagerService\_SetFolderIcon](../harmonyos-references/capi-filemanager-service-h.md#hms_filemanagerservice_setfoldericon)(HMS\_FileManagerService\_SupportFolderType folderType, const char \*uri, const char \*iconResId) | 设置文件夹图标。 |
| [HMS\_FileManagerService\_UnSetFolderIcon](../harmonyos-references/capi-filemanager-service-h.md#hms_filemanagerservice_unsetfoldericon)(HMS\_FileManagerService\_SupportFolderType folderType, const char \*uri) | 取消设置文件夹图标。 |

## 开发步骤

1. 在CMake脚本中链接相关动态库。

   ```cmake
   find_library(filemanager-service-lib libfilemanager_service_ndk.z.so)
   target_link_libraries(entry PUBLIC ${filemanager-service-lib})
   ```
2. 引入头文件。

   ```
   #include <filemanager_service.h>
   ```
3. 申请权限。使用本接口前，需要在module.json5中声明所需的权限：ohos.permission.SYNC\_ROOT\_MANAGER。具体指导可见[声明权限](declare-permissions.md)。
4. 当需要将同步文件夹展示到文件管理器侧边栏时，构造侧边栏文件夹信息，调用[HMS\_FileManagerService\_AddToSidebar](../harmonyos-references/capi-filemanager-service-h.md#hms_filemanagerservice_addtosidebar)将文件夹添加到侧边栏。

   ```
   HMS_FileManagerService_SidebarFolder folder = {0};
   folder.uri = "file://docs/storage/Users/currentUser/Documents/cloudFolder";
   folder.iconResId = "icon_cloud_folder";
   folder.displayNameResId = "str_cloud_folder_name";
   folder.alias = "cloudFolder";

   HMS_FileManagerService_AddToSidebar(HMS_FILEMANAGERSERVICE_FOLDER_TYPE_CLOUD, &folder);
   ```
5. 当需要为侧边栏文件夹设置自定义图标时，调用[HMS\_FileManagerService\_SetFolderIcon](../harmonyos-references/capi-filemanager-service-h.md#hms_filemanagerservice_setfoldericon)设置文件夹图标。

   ```
   HMS_FileManagerService_SetFolderIcon(
       HMS_FILEMANAGERSERVICE_FOLDER_TYPE_CLOUD,
       "file://docs/storage/Users/currentUser/Documents/cloudFolder",
       "icon_custom");
   ```
6. 当不再需要自定义图标时，调用[HMS\_FileManagerService\_UnSetFolderIcon](../harmonyos-references/capi-filemanager-service-h.md#hms_filemanagerservice_unsetfoldericon)取消设置文件夹图标。

   ```
   HMS_FileManagerService_UnSetFolderIcon(
       HMS_FILEMANAGERSERVICE_FOLDER_TYPE_CLOUD,
       "file://docs/storage/Users/currentUser/Documents/cloudFolder");
   ```
7. 当文件夹不再需要展示在侧边栏时，调用[HMS\_FileManagerService\_RemoveFromSidebar](../harmonyos-references/capi-filemanager-service-h.md#hms_filemanagerservice_removefromsidebar)从侧边栏删除文件夹。

   ```
   HMS_FileManagerService_RemoveFromSidebar(
       HMS_FILEMANAGERSERVICE_FOLDER_TYPE_CLOUD,
       "file://docs/storage/Users/currentUser/Documents/cloudFolder");
   ```
