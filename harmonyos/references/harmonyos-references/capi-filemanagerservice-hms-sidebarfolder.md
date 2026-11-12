---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-filemanagerservice-hms-sidebarfolder
title: HMS_FileManagerService_SidebarFolder
breadcrumb: API参考 > 应用服务 > File Manager Service Kit（文件管理服务） > C API > 头文件和结构体 > 结构体 > HMS_FileManagerService_SidebarFolder
category: harmonyos-references
scraped_at: 2026-11-12T09:57:16+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a9b0f237b511c71ee909118d72b09055661f90706fb7684cff33c6f279fb9291
---

```c
struct HMS_FileManagerService_SidebarFolder {...}
```

## 概述

定义侧边栏文件夹数据结构。

**系统能力：** SystemCapability.FileManagement.FileManagerService.Core

**起始版本：** 26.0.1

**相关模块：** [FileManagerService](capi-filemanagerservice.md)

**所在头文件：** [filemanager\_service.h](capi-filemanager-service-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char \*uri | 文件夹URI。 |
| const char \*iconResId | 文件夹图标资源ID。 |
| const char \*displayNameResId | 文件夹显示名称资源ID。 |
| const char \*alias | 文件夹别名。 |
