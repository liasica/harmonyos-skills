---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-enterprise-foundation
title: ArkTS API错误码
breadcrumb: API参考 > 系统 > 基础功能 > Enterprise Foundation Kit（企业办公开发服务） > ArkTS API > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-11-12T09:55:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:73120597322c5571d2849e10df7e91b2e6f337d61cb22ae7320b39d169da8895
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1029200001 企业批量部署还原服务未启动

**错误信息**

The enterprise batch deploy restore service is not started.

**错误描述**

企业批量部署还原服务未启动。

**可能原因**

未开启企业批量部署还原服务。

**处理步骤**

使用企业批量部署还原服务前，需要在HEM（华为企业管理平台）上开启该服务，操作指导请参见：[如何管理部署策略](https://developer.huawei.com/business/cn/doc/HEM/hem_user-guide_add-reseller_management-devices-ot-0000002307766441)。

## 1029200002 企业批量部署还原服务繁忙

**错误信息**

The enterprise batch deploy restore service is busy.

**错误描述**

企业批量部署还原服务繁忙。

**可能原因**

当前正在执行备份或还原任务。

**处理步骤**

1. 请等待当前任务执行完成。
2. 请手动取消当前任务。

## 1029200003 无正在执行的备份或还原任务

**错误信息**

No backup or restore task in progress.

**错误描述**

无正在执行的备份或还原任务。

**可能原因**

当前没有正在执行的备份或还原任务。

**处理步骤**

请确认是否有正在执行的备份或还原任务。

## 1029200004 用户取消备份或还原操作

**错误信息**

The backup or restore operation was canceled by the user.

**错误描述**

用户取消备份或还原操作。

**可能原因**

备份或还原任务已经被用户取消。

**处理步骤**

请确认是否触发了取消备份或还原操作。

## 1029200005 目录不存在

**错误信息**

No such directory.

**错误描述**

目录不存在。

**可能原因**

指定的目录不存在。

**处理步骤**

请确认参数是否符合要求。

## 1029200006 不是一个目录

**错误信息**

Not a directory.

**错误描述**

不是一个目录。

**可能原因**

指定的路径不是目录。

**处理步骤**

请确认参数是否符合要求。

## 1029200007 企业批量部署还原服务异常

**错误信息**

The enterprise batch deploy restore service is abnormal.Possible causes: File operation exception.

**错误描述**

企业批量部署还原服务异常。可能的原因：文件操作异常。

**可能原因**

系统服务异常。

**处理步骤**

若遇到系统服务异常，请尝试重试操作，并在必要时通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题以获取技术支持。
