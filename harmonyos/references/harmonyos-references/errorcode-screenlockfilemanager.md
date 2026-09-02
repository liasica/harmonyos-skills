---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-screenlockfilemanager
title: 锁屏敏感数据管理错误码
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > 错误码 > 锁屏敏感数据管理错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:00:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:23af687dd168c8d7f6bd5158c4f30f9eb99acaa541431b7ea491f3d184859b7e
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 29300002 系统服务工作异常

**错误信息**

The system ability works abnormally.

**错误描述**

当系统服务工作异常时，将返回该错误码。

**可能原因**

该错误码表示系统服务工作异常。

1. 锁屏敏感数据管理服务无法正常启动。
2. IPC数据读取写入失败。

**处理步骤**

系统服务内部工作异常，请稍后重试，或者重启设备。

## 29300003 应用未开启锁屏敏感数据保护功能

**错误信息**

The application has not enabled the data protection function under lock screen.

**错误描述**

当应用未开启锁屏敏感数据保护功能时，将返回该错误码。

**可能原因**

1. 应用未在[requestpermissions](../harmonyos-guides/declare-permissions.md#在配置文件中声明权限)配置权限ohos.permission.PROTECT\_SCREEN\_LOCK\_DATA开启应用锁屏敏感数据保护功能。
2. 当前硬件不支持锁屏敏感数据保护功能。

**处理步骤**

在[requestpermissions](../harmonyos-guides/declare-permissions.md#在配置文件中声明权限)中配置权限ohos.permission.PROTECT\_SCREEN\_LOCK\_DATA开启应用锁屏敏感数据保护功能。

## 29300004 锁屏敏感数据访问权限已释放

**错误信息**

The file access is denied due to security strategy.

**错误描述**

文件访问被拒绝。当锁屏敏感数据访问权限已被释放时，将返回该错误码。

**可能原因**

锁屏敏感数据访问权限已释放。

**处理步骤**

锁屏下无法访问敏感数据。如需继续使用，请引导用户重新解锁屏幕，待解锁完成后可恢复正常访问。

## 29300005 未申请锁屏敏感数据访问权限

**错误信息**

File access is not acquired.

**错误描述**

当未申请锁屏敏感数据访问权限时，将返回该错误码。

**可能原因**

该错误码表示释放前，未申请锁屏敏感数据访问权限。

**处理步骤**

检查当前接口是否有配套使用，请在释放前先申请锁屏敏感数据访问权限。
