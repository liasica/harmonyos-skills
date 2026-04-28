---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-node-render-monitor
title: 注册节点渲染状态监听错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > 注册节点渲染状态监听错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:04:55+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:78f2478a499d58d46ed35e4f0d411f8c5427e5e797bef918a89097a9b8951ee7
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)。

## 161001 监视渲染状态的节点数超过限制

PhonePC/2in1TabletTVWearable

**错误信息**

The count of nodes monitoring render state is over the limitation.

**错误描述**

当注册的监视渲染状态的节点数超过限制时，系统会产生此错误码。

**可能原因**

监视渲染状态的节点数超过限制。

**处理步骤**

请确保注册的监视渲染状态的节点数小于64。
