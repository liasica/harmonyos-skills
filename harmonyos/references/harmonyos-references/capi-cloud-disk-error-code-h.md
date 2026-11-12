---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cloud-disk-error-code-h
title: cloud_disk_error_code.h
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 头文件 > cloud_disk_error_code.h
category: harmonyos-references
scraped_at: 2026-11-12T09:55:06+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:c7c3fedccec65910be214d3c3e041d6d033b81198395556143483b37b552be1e
---

## 概述

提供云盘管理模块的错误码定义。

**引用文件：** <filemanagement/clouddiskmanager/cloud\_disk\_error\_code.h>

**库：** libohclouddiskmanager.so

**系统能力：** SystemCapability.FileManagement.CloudDiskManager

**起始版本：** 21

**相关模块：** [CloudDisk](capi-clouddisk.md)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | CloudDisk\_ErrorCode | 定义云盘管理模块的错误码。 |

## 枚举类型说明

### CloudDisk\_ErrorCode

```c
enum CloudDisk_ErrorCode
```

**描述**

定义云盘管理模块的错误码。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| CLOUD\_DISK\_OK = 0 | 接口调用成功。 |
| CLOUD\_DISK\_PERMISSION\_DENIED = 201 | 接口权限校验失败。 |
| CLOUD\_DISK\_NOT\_SUPPORTED = 801 | 当前设备不支持此功能。 |
| CLOUD\_DISK\_INVALID\_ARG = 34400001 | 输入参数无效。 |
| CLOUD\_DISK\_SYNC\_FOLDER\_PATH\_UNAUTHORIZED = 34400002 | 同步根路径未授权。同步根路径是指应用用于云同步的本地目录路径。 |
| CLOUD\_DISK\_IPC\_FAILED = 34400003 | IPC连接失败。 |
| CLOUD\_DISK\_SYNC\_FOLDER\_LIMIT\_EXCEEDED = 34400004 | 同步根路径数量超过允许的限制。 |
| CLOUD\_DISK\_CONFLICT\_THIS\_APP = 34400005 | 同步根路径和该应用现有的同步根路径发生冲突。 |
| CLOUD\_DISK\_CONFLICT\_OTHER\_APP = 34400006 | 同步根路径和其他应用现有的同步根路径发生冲突。 |
| CLOUD\_DISK\_REGISTER\_SYNC\_FOLDER\_FAILED = 34400007 | 同步根路径注册失败。 |
| CLOUD\_DISK\_SYNC\_FOLDER\_NOT\_REGISTERED = 34400008 | 同步根路径未注册。 |
| CLOUD\_DISK\_UNREGISTER\_SYNC\_FOLDER\_FAILED = 34400009 | 同步根路径取消注册失败。 |
| CLOUD\_DISK\_SYNC\_FOLDER\_PATH\_NOT\_EXIST = 34400010 | 同步根路径不存在。 |
| CLOUD\_DISK\_LISTENER\_NOT\_REGISTERED = 34400011 | 变更监听器未注册。 |
| CLOUD\_DISK\_LISTENER\_ALREADY\_REGISTERED = 34400012 | 变更监听器已注册。 |
| CLOUD\_DISK\_INVALID\_CHANGE\_SEQUENCE = 34400013 | 变更序列号无效或已过期，建议重新查询所有变更记录。 |
| CLOUD\_DISK\_TRY\_AGAIN = 34400014 | 临时失败，建议重试（如：底层I/O负载过大、内存不足等）。 |
| CLOUD\_DISK\_NOT\_ALLOWED = 34400015 | 当前设备不允许执行此功能。 |
| OH\_CLOUD\_DISK\_FILE\_ALREADY\_EXISTS = 34400016 | 目标路径下已存在同名文件。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_NOT\_A\_PLACEHOLDER = 34400017 | 目标路径不是占位符文件。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_IS\_A\_PLACEHOLDER = 34400018 | 目标路径已经是占位符文件。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_HYDRATE\_IN\_PROGRESS = 34400019 | 占位符文件正在水合中。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_NO\_SPACE\_LEFT = 34400020 | 磁盘剩余空间不足。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_CALLBACK\_NOT\_REGISTERED = 34400021 | 回调表没有注册。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_CALLBACK\_ALREADY\_REGISTERED = 34400022 | 回调表已经注册。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_NOT\_A\_DIRECTORY = 34400023 | 目标路径的父目录不是目录。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_FILE\_NOT\_EXIST = 34400024 | 目标路径不存在。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_NAME\_TOO\_LONG = 34400025 | 文件名或路径过长。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_FILE\_TOO\_LARGE = 34400026 | 文件过大。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_PLACEHOLDER\_CUSTOM\_INFO\_NOT\_FOUND = 34400027 | 占位符没有自定义信息。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_PLACEHOLDER\_NOT\_FULLY\_HYDRATED = 34400028 | 占位符文件未完全水合。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_DEHYDRATE\_DENIED = 34400029 | 应用回调拒绝脱水操作。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_CANCELLED = 34400030 | 水合任务已取消。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_ALREADY\_HYDRATED = 34400031 | 占位符文件已完全水合。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_NO\_HYDRATION\_IN\_PROGRESS = 34400032 | 没有正在进行的水合任务。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_INVALID\_PLACEHOLDER\_STATE = 34400033 | 存储的占位符状态无效。  **起始版本：** 26.0.1 |
| OH\_CLOUD\_DISK\_HYDRATION\_TASK\_LIMIT\_REACHED = 34400034 | 待处理的占位符水合任务数量达到上限。  **起始版本：** 26.0.1 |
