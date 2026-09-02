---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-enterprise-space
title: ArkTS API错误码
breadcrumb: API参考 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > ArkTS API > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:53+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:807cee005bff05a294e11551d2e24a67383da8d97ea6ff9ddc6906a43cf7e46c
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1020300001 系统服务异常

**错误信息**

System service exception.

**错误描述**

系统服务异常。

**可能原因**

无效工作空间ID，或者未知文件处理类型。

**处理步骤**

若遇到系统服务异常，请尝试重试操作，并在必要时通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题以获取技术支持。

## 1020300002 请求参数无效

**错误信息**

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**错误描述**

请求参数无效。

**可能原因**

必填参数为空、参数类型错误或者参数校验失败。

**处理步骤**

请确认参数符合要求。

## 1020400001 系统服务异常

**错误信息**

System service exception.

**错误描述**

系统服务异常。

**可能原因**

系统服务繁忙，或者网络异常。

**处理步骤**

若遇到系统服务异常，请尝试重试操作，并在必要时通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题以获取技术支持。

## 1020400002 请求参数无效

**错误信息**

Parameter error.

**错误描述**

请求参数无效。

**可能原因**

必填参数为空或者参数类型错误。

**处理步骤**

请确认参数符合要求。

## 1020400003 工作空间无效

**错误信息**

Invalid workspace.

**错误描述**

工作空间无效。

**可能原因**

1. 工作空间不存在。
2. 工作空间类型不支持。
3. 当前工作空间数量等于2个，无法继续创建。
4. 企业账号不存在。

**处理步骤**

1. 确认工作空间ID是否正确。
2. 确认工作空间类型是否在[WorkspaceType](enterprisespace-spacemanager.md#workspacetype)的枚举中存在。
3. 删除不必要的工作空间后再创建。
4. 确认当前空间是否是企业空间。
5. 请根据[WorkspaceInfo](enterprisespace-spacemanager.md#workspaceinfo)中的定义确认当前工作空间信息是否符合要求。

## 1020400004 企业认证失败

**错误信息**

Authentication failed.

**错误描述**

企业认证失败。

**可能原因**

1. 企业认证超时。
2. 认证服务器不存在。
3. 认证服务异常。

**处理步骤**

请检查认证服务器的相关配置项是否正确。

## 1020400005 配置信息未设置

**错误信息**

Configuration not set.

**错误描述**

配置信息未设置。

**可能原因**

查询配置信息时，配置信息未设置。常见场景包括：

1. 未设置工作空间策略。
2. 未设置跨空间消息提醒配置。

**处理步骤**

请确认相关配置信息已在系统中正确设置。

## 1020400006 SA进程异常退出，导致连接中断

**错误信息**

Session disconnected.

**错误描述**

SA进程异常退出，导致连接中断。

**可能原因**

当存在应用订阅了空间事件时，服务进程异常退出。

**处理步骤**

请在应用中重新订阅空间相关的事件以恢复连接。

## 1020400007 企业空间未开启

**错误信息**

Enterprise workspace not enabled.

**错误描述**

企业空间未开启。

**可能原因**

企业管理员未使能企业空间功能。

**处理步骤**

企业管理员请按照[enableWorkspace](enterprisespace-spacemanager.md#enableworkspace)使能双空间特性。

## 1020400008 账号名或密码无效

**错误信息**

Invalid account name or password.

**错误描述**

无效的账号名或密码。

**可能原因**

企业认证时，输入错误的账号名或密码。

**处理步骤**

请核对输入的企业账号名和密码是否准确无误。

## 1020400009 企业账号已锁定

**错误信息**

The account is locked.

**错误描述**

企业账号已锁定。

**可能原因**

企业认证服务器中账号已锁定。

**处理步骤**

请等待企业认证服务器自动解锁该账号，或联系企业管理员手动解锁。

## 1020400010 企业认证服务器不可达

**错误信息**

Enterprise authentication server unreachable.

**错误描述**

企业认证服务器不可达。

**可能原因**

1. 网络未连接。
2. 企业认证服务器异常。

**处理步骤**

1. 检查设备与企业认证服务器的网络是否连通。
2. 检查企业认证服务器是否异常。

## 1020400011 禁止创建账号

**错误信息**

Account creation is not permitted.

**错误描述**

禁止创建账号。

**可能原因**

企业管理员设置禁止用户添加账号。

**处理步骤**

企业管理员设置允许用户添加账号。

## 1020400012 全盘加密未开启

**错误信息**

Full disk encryption is not enabled.

**错误描述**

全盘加密未开启。

**可能原因**

企业管理员设置关闭全盘加密。

**处理步骤**

企业管理员设置开启全盘加密。

## 1020400014 跨空间消息提醒配置超限

**错误信息**

Configuration quantity exceeds the limit.

**错误描述**

当前系统中已配置的跨空间消息提醒规则总数，已超过系统规定的最大阈值（20 条）。

**可能原因**

企业管理员在调用[setNotificationConfig](enterprisespace-spacemanager.md#setnotificationconfig)接口时，尝试新增或更新的配置项导致总数量突破系统上限（20 条）。

**处理步骤**

清理冗余配置，检查并删除不再使用的跨空间消息提醒配置。
