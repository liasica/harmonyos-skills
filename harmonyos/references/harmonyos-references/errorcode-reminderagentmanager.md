---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-reminderagentmanager
title: reminderAgentManager错误码
breadcrumb: API参考 > 应用框架 > Background Tasks Kit（后台任务开发服务） > 错误码 > reminderAgentManager错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:01:30+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3529612525f4040d437683f6bfb77df2e682c7a5509f7e54127b23bc5ce6f8e1
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 1700001 通知使能未开启

**错误信息**

Notification is not enabled.

**错误描述**

当调用发布提醒接口时，不允许应用发送通知。

**可能原因**

1. 未申请通知使能权限。
2. 应用的通知开关为关闭状态。

**处理步骤**

1. 申请通知使能权限弹窗[notificationManager.requestEnableNotification](js-apis-notificationmanager.md#notificationmanagerrequestenablenotification10)。
2. 通知设置里开启应用通知开关。

## 1700002 提醒数量超出限制

**错误信息**

The number of reminders exceeds the limit.

**错误描述**

当调用发布提醒接口时，提醒数量超出最大限制。

**可能原因**

1. 因管控限制，普通应用如果没有代理提醒的使用权限，视为这个普通应用提醒数量上限为0。
2. 应用数量上限因API版本而异：
   * API版本26.0.0及以上，单个普通应用最多支持64个提醒。
   * API version 25及以下，单个普通应用最多支持30个提醒。
3. 从API version 10开始，所有应用提醒数量总和不超过12000个。API version 9及之前的版本，提醒数量总和不超过2000个。

**处理步骤**

1. 首先，确认是否[申请了代理提醒的使用权限](../harmonyos-guides/agent-powered-reminder.md#约束与限制)。由于系统限制且HarmonyOS 5.1.1(19)及其之前版本存量设备较少，新申请的权限在HarmonyOS 5.1.1(19)及其之前版本不再生效，建议升级至HarmonyOS 6.0.0(20)及以上版本。
2. 然后，在申请通过情况下，优先检查签名是否配置正确，如果配置不正确，需要重新生成Profile文件并使用[手动签名](../harmonyos-guides/ide-signing-manual.md)；其次检查提醒数量是否超过规定数量，及时删除不必要的提醒。

## 1700003 提醒不存在

**错误信息**

The reminder does not exist.

**错误描述**

当调用取消提醒接口时，未找到对应的提醒。

**可能原因**

1. 提醒已过期。
2. 提醒已被删除。

**处理步骤**

1. 检查提醒是否有效。
2. 检查提醒是否已被删除。

## 1700004 包名不存在

**错误信息**

The bundle name does not exist.

**错误描述**

未找到传入的包名信息。

**可能原因**

1. 包名不正确。
2. 应用未安装。

**处理步骤**

检查应用包名是否存在。

## 1700007 参数错误

**错误信息**

If the input parameter is not valid parameter.

**错误描述**

输入参数不是有效参数。

**可能原因**

参数不符合规则。

**处理步骤**

请检查必选参数是否传入，或者传入的参数类型是否错误。对于参数校验失败，阅读参数规格约束，按照可能原因进行排查。
