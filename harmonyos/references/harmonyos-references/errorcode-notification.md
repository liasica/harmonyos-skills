---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-notification
title: 通知错误码
breadcrumb: API参考 > 应用服务 > Notification Kit（用户通知服务） > 错误码 > 通知错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:03:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d783ee0bf95955c0dba63c1c22c0a69d47b4aacf224573ed897b9c4eff926730
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 1600001 内部错误

**错误信息**

Internal error.

**错误描述**

多线程处理异常、内部指针校验错误等内部处理错误时，方法将返回该错误码。

**可能原因**

多线程处理、内部处理异常等内核通用错误。

**处理步骤**

确认系统资源是否足够。

## 1600002 序列化或反序列化错误

**错误信息**

Marshalling or unmarshalling error.

**错误描述**

数据传输前，进行序列化或反序列化错误，方法将返回该错误码。

**可能原因**

应用与通知服务字段未匹配。

**处理步骤**

检查应用sdk版本与系统版本是否匹配。

## 1600003 连接通知服务失败

**错误信息**

Failed to connect to the service.

**错误描述**

应用连接通知服务失败，方法将返回该错误码。

**可能原因**

通知服务繁忙或异常。

**处理步骤**

等待一段时间后重试，或检查通知服务运行状态，必要时重启通知服务。

## 1600004 通知开关关闭

**错误信息**

Notification disabled.

**错误描述**

当通知开关为关闭状态时，方法将返回该错误码。

**可能原因**

应用的通知开关为关闭状态。

**处理步骤**

[通知设置](../harmonyos-guides/notification-glossary.md#notification-setting通知设置)里开启应用通知开关。

## 1600005 通知渠道关闭

**错误信息**

Notification slot disabled.

**错误描述**

当[通知渠道](../harmonyos-guides/notification-glossary.md#notification-slot通知渠道)关闭时，方法将返回该错误码。

**可能原因**

通知渠道关闭状态，或未添加该类型渠道。

**处理步骤**

1. [通知设置](../harmonyos-guides/notification-glossary.md#notification-setting通知设置)里查看应用是否有该类型渠道，没有需要新增。
2. 通知设置里查看应用该类型渠道状态，要保持开启状态。

## 1600007 通知不存在

**错误信息**

The notification does not exist.

**错误描述**

通知服务未找到该通知，方法将返回该错误码。

**可能原因**

通知已被取消或删除。

**处理步骤**

无。

## 1600008 用户不存在

**错误信息**

The user does not exist.

**错误描述**

传入的用户信息系统里未查询到，方法将返回该错误码。

**可能原因**

传入用户信息有误。

**处理步骤**

确认传入的用户信息是否正确。

## 1600009 通知发布频度超过限制

**错误信息**

The notification sending frequency reaches the upper limit.

**错误描述**

通知发送频率超过限制，方法将返回该错误码。

**可能原因**

通知发送频率超过每秒10个，或者更新频率超过每秒20条。

**处理步骤**

降低通知发送频率。

## 1600010 分布式操作失败

**错误信息**

Distributed operation failed.

**错误描述**

分布式数据库操作异常或分布式接口调用异常，方法将返回该错误码。

**可能原因**

分布式数据库操作异常或分布式接口调用异常。

**处理步骤**

检查分布式连接是否正常。

## 1600012 内存空间不足

**错误信息**

No memory space.

**错误描述**

内存申请可能因内存空间不足出现错误，方法将返回该错误码。

**可能原因**

1. 内存空间不足。
2. 内存申请出现错误。

**处理步骤**

确认系统内存是否足够。

## 1600013 通知弹窗已弹出

**错误信息**

A notification dialog box is already displayed.

**错误描述**

通知弹窗已经弹出，方法将返回该错误码。

**可能原因**

通知弹窗已经弹出。

**处理步骤**

确认通知弹窗是否弹出。

## 1600014 没有相关权限

**错误信息**

1. No permission.
2. The right of liveView is not enabled.

**错误描述**

1. 没有相关权限，方法将返回该错误码。
2. 当应用发布三方实况类型通知，且未申请实况窗权益时，将返回该错误码。

**可能原因**

1. 没有相关权限。
2. 应用未申请对应场景的权益。

**处理步骤**

1. 确认是否具有相关权限。
2. 请确认是否申请实况窗权益。

## 1600015 当前通知状态不支持重复配置

**错误信息**

The current notification status does not support duplicate configurations.

**错误描述**

当前通知状态不支持重复配置，方法将返回该错误码。

**可能原因**

当前通知状态不支持重复配置。

**处理步骤**

确认是否重复配置通知状态。

## 1600016 本次更新的通知版本太低

**错误信息**

The notification version for this update is too low.

**错误描述**

本次更新的通知版本太低，方法将返回该错误码。

**可能原因**

本次更新的通知版本太低。

**处理步骤**

确认通知版本。

## 1600018 通知设置页面已经拉起

**错误信息**

The notification settings window is already displayed.

**错误描述**

[通知设置](../harmonyos-guides/notification-glossary.md#notification-setting通知设置)页面已经拉起，方法将返回该错误码。

**可能原因**

通知设置页面已经拉起。

**处理步骤**

确认通知设置页面是否拉起。

## 1600020 不允许权限管控名单中的应用发布通知

**错误信息**

The application is not allowed to send notifications due to permission settings.

**错误描述**

当发布通知时，若应用被列入权限管控名单，将返回该错误码。

**可能原因**

该场景为企业定制设备场景。

**处理步骤**

该应用受到[企业设备管理](../harmonyos-guides/mdm-kit-intro.md)的权限管控，应用无法主动退出权限管控名单。

## 1600023 应用未实现NotificationSubscriberExtensionAbility

**错误信息**

The application does not implement the NotificationSubscriberExtensionAbility.

**错误描述**

应用未实现NotificationSubscriberExtensionAbility，将返回该错误码。

**可能原因**

应用未设置或未正确设置[NotificationSubscriberExtensionAbility](js-apis-notificationsubscriberextensionability.md)。

**处理步骤**

应用需创建NotificationSubscriberExtensionAbility，具体配置方法参考[ExtensionAbility组件](../harmonyos-guides/extensionability-overview.md)中的[NotificationSubscriberExtensionAbility](js-apis-notificationsubscriberextensionability.md)。

## 1600029 系统无法找到实况窗卡片自定义扩展区的ExtensionAbility

**错误信息**

The system failed to find the ExtensionAbility instance for the custom Live View widget template.

**错误描述**

当应用发布三方实况类型通知时，系统未找到自定义扩展区的ExtensionAbility实例，方法将返回该错误码。

**可能原因**

应用未配置或未正确配置实况窗卡片自定义扩展区的ExtensionAbility。

**处理步骤**

检查应用是否正确配置实况窗卡片自定义扩展区的ExtensionAbility。
