---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-error-code
title: ArkTS API 错误码
breadcrumb: API参考 > 系统 > 硬件 > Pen Kit（手写笔服务） > ArkTS API 错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:11:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3f38a3d8be35e57969fe077a07d79582043a7d2e2de07b822305d884a08919d1
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 1010410001 系统内部错误

PhonePC/2in1Tablet

**错误信息**

internal recognition engine has been released.

**错误描述**

内部识别引擎已被释放。

**可能原因**

识别引擎已被释放，但仍在调用识别相关的接口。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1010400001 加载失败

PhonePC/2in1Tablet

**错误信息**

load failed.

**错误描述**

加载文件失败。

**可能原因**

其他未知错误。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1010400002 保存失败

PhonePC/2in1Tablet

**错误信息**

save failed.

**错误描述**

保存文件失败。

**可能原因**

保存路径错误。

**处理步骤**

检查保存路径，尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1013900001 IPC连接失败

PhonePC/2in1Tablet

**错误信息**

IPC communication failed.

**错误描述**

IPC连接失败。

**可能原因**

防火墙屏蔽。

**处理步骤**

检查防火墙设置，尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1013900002 内存不足

PhonePC/2in1Tablet

**错误信息**

memory is insufficient.

**错误描述**

内存不足导致接口调用失败。

**可能原因**

内存不足。

**处理步骤**

检查内存不足的原因，尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1013900003 服务不合法

PhonePC/2in1Tablet

**错误信息**

service is invalid.

**错误描述**

服务不合法。

**可能原因**

其他未知错误。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1013900004 重复调用

PhonePC/2in1Tablet

**错误信息**

multi app call.

**错误描述**

当前应用重复调用。

**可能原因**

在未返回取色结果时重复调用。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1013900005 后台服务调用

PhonePC/2in1Tablet

**错误信息**

background service call.

**错误描述**

后台调用。

**可能原因**

在后台调用该接口。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。
