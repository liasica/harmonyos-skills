---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/filemanagerservice-arkts-errorcode
title: ArkTS API错误码
breadcrumb: API参考 > 应用服务 > File Manager Service Kit（文件管理服务） > ArkTS API > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:16:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:637696e07941ef23c26b23886d22c55449595aed424fcd09fc0c618f5209721e
---

说明

以下仅介绍本模块特有错误码，通用错误码请参见[通用错误码](errorcode-universal.md)。

## 1014000001 操作不允许

PhonePC/2in1Tablet

**错误信息**

Operation not permitted

**错误描述**

操作不允许。

**可能原因**

当前用户文件操作不被允许，URI或path访问未授权。

**处理步骤**

1、通过系统文件选择器（FilePicker），[选择用户文件](../harmonyos-guides/select-user-file.md)从而获取URI临时权限。

2、通过程序访问控制机制，[向用户申请授权](../harmonyos-guides/request-user-authorization.md)从而获取目录权限。

## 1014000002 没有该文件或目录

PhonePC/2in1Tablet

**错误信息**

No such file or directory

**错误描述**

没有该文件或目录。

**可能原因**

1、文件或目录不存在。

2、当前调用方对该文件或目录无访问权限。

**处理步骤**

1、确认文件路径是否存在。

2、确认当前调用方对该文件或目录是否有访问权限。

## 1014000003 存储空间不足

PhonePC/2in1Tablet

**错误信息**

No space left on device

**错误描述**

存储空间不足。

**可能原因**

存储空间不足。

**处理步骤**

清理设备存储空间。

## 1014000004 系统内部错误

PhonePC/2in1Tablet

**错误信息**

System inner fail

**错误描述**

系统内部错误。

**可能原因**

系统异常，发生错误。

**处理步骤**

重启设备，或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1014000005 无效的快捷方式文件

PhonePC/2in1Tablet

**错误信息**

Invalid shortcut file

**错误描述**

无效的快捷方式文件。

**可能原因**

快捷方式文件URI或内容错误，无法正常解析。

**处理步骤**

请确认传入正确的快捷方式文件URI。
