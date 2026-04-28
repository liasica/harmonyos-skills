---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cloud-disk-error-code-h
title: cloud_disk_error_code.h
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 头文件 > cloud_disk_error_code.h
category: harmonyos-references
scraped_at: 2026-04-28T08:05:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e28696786e3e28fa55deeeb980ac30697ea046b68948ebc52e374f228aaeeed4
---

## 概述

PC/2in1Tablet

提供云盘管理模块的错误码定义。

**引用文件：** <filemanagement/clouddiskmanager/cloud\_disk\_error\_code.h>

**库：** libohclouddiskmanager.so

**系统能力：** SystemCapability.FileManagement.CloudDiskManager

**起始版本：** 21

**相关模块：** [CloudDisk](capi-clouddisk.md)

## 汇总

PC/2in1Tablet

### 枚举

PC/2in1Tablet

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [CloudDisk\_ErrorCode](capi-cloud-disk-error-code-h.md#clouddisk_errorcode) | CloudDisk\_ErrorCode | 定义云盘管理模块的错误码。 |

## 枚举类型说明

PC/2in1Tablet

### CloudDisk\_ErrorCode

PC/2in1Tablet

```
1. enum CloudDisk_ErrorCode
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
| CLOUD\_DISK\_SYNC\_FOLDER\_PATH\_UNAUTHORIZED = 34400002 | 同步根路径未授权。 |
| CLOUD\_DISK\_IPC\_FAILED = 34400003 | IPC连接失败。 |
| CLOUD\_DISK\_SYNC\_FOLDER\_LIMIT\_EXCEEDED = 34400004 | 同步根路径数量超过允许的限制。 |
| CLOUD\_DISK\_CONFLICT\_THIS\_APP = 34400005 | 同步根路径和该应用现有的同步根路径发生冲突。 |
| CLOUD\_DISK\_CONFLICT\_OTHER\_APP = 34400006 | 同步根路径和其他应用现有的同步根路径发生冲突。 |
| CLOUD\_DISK\_REGISTER\_SYNC\_FOLDER\_FAILED = 34400007 | 同步根路径注册失败。 |
| CLOUD\_DISK\_SYNC\_FOLDER\_NOT\_REGISTERED = 34400008 | 同步根路径未注册。 |
| CLOUD\_DISK\_UNREGISTER\_SYNC\_FOLDER\_FAILED = 34400009 | 同步根路径取消注册失败。 |
| CLOUD\_DISK\_SYNC\_FOLDER\_PATH\_NOT\_EXIST = 34400010 | 同步根路径不存在。 |
| CLOUD\_DISK\_LISTENER\_NOT\_REGISTERED = 34400011 | 变更的监听未注册。 |
| CLOUD\_DISK\_LISTENER\_ALREADY\_REGISTERED = 34400012 | 变更的监听已注册。 |
| CLOUD\_DISK\_INVALID\_CHANGE\_SEQUENCE = 34400013 | 无效的变更序列，建议进行全部查询。 |
| CLOUD\_DISK\_TRY\_AGAIN = 34400014 | 临时失败，建议重试（如：底层io负载过大、内存不足等）。 |
| CLOUD\_DISK\_NOT\_ALLOWED = 34400015 | 当前设备不允许执行此功能。 |
