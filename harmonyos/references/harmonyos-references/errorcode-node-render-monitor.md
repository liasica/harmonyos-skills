---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-node-render-monitor
title: 注册节点渲染状态监听错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > 注册节点渲染状态监听错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:01:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7d8e59687a4fda359bf0c5ca64525e0fb741ee1daeddc3022d73d795390379b9
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)。

## 161001 监听渲染状态的节点数超过限制

**错误信息**

The count of nodes monitoring render state is over the limitation.

**错误描述**

监听渲染状态的节点数超过限制。

**可能原因**

调用[on('nodeRenderState')](arkts-apis-uicontext-uiobserver.md#onnoderenderstate20)接口注册节点渲染状态监听时，单个UI实例中注册的监听节点数超过限制。

**处理步骤**

请确保单个UI实例中注册监听渲染状态的节点不超过64个。
