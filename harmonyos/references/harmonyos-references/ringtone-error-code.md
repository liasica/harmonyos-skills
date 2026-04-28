---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ringtone-error-code
title: ArkTS API 错误码
breadcrumb: API参考 > 媒体 > Ringtone Kit（铃声服务） > ArkTS API > ArkTS API 错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:14:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:92c9b491d2715ac8affaad75468b769afd024e14af4c47952b1e310fd6b3ec74
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 1011600001 用户取消

PhoneTablet

**错误信息**

User canceled.

**错误描述**

用户拉起弹框后，未完成铃声设置功能，取消了弹框。

**可能原因**

用户操作原因。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1011600002 文件不存在

PhoneTablet

**错误信息**

The media file is not found.

**错误描述**

传入的文件路径下不存在文件。

**可能原因**

文件未创建成功就调用了[ringtone.startRingtoneSetting](ringtone-ringtone.md#ringtonestartringtonesetting)接口。

**处理步骤**

确保文件路径下传入了对应文件后再重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1011600003 弹出框错误

PhoneTablet

**错误信息**

Failed to show the dialog box.

**错误描述**

当发生系统内部错误时，将返回该错误码。

**可能原因**

其他未知错误。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1011600004 调用系统接口失败

PhoneTablet

**错误信息**

Failed to call the system API.

**错误描述**

当发生系统内部错误时，将返回该错误码。

**可能原因**

其他未知错误。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1011699999 系统内部错误

PhoneTablet

**错误信息**

System exception.

**错误描述**

当发生系统内部错误时，将返回该错误码。

**可能原因**

其他未知错误。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。
