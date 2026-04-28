---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-drag-event
title: 拖拽事件错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > 拖拽事件错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:04:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b91868a3b36dac96ac747c573d7922b1cf2f28272cbb095f413046845d98652d
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 190001 数据未取得

**错误信息**

Data not found.

**错误描述**

当开发者调用DragEvent的[getData](ts-universal-events-drag-drop.md#getdata10)接口时，若还未获取到数据，会抛出此错误码。

**可能原因**

DragEvent的数据暂未获取成功。

**处理步骤**

NA

## 190002 获取数据错误

**错误信息**

Data error.

**错误描述**

当开发者调用DragEvent的[getData](ts-universal-events-drag-drop.md#getdata10)接口时，若取得的数据有错误，会抛出此错误码。

**可能原因**

数据获取错误。

**处理步骤**

NA

## 190003 当前阶段不允许操作

**错误信息**

Operation not allowed for current phase.

**错误描述**

如果开发者在非[onDrop](ts-universal-events-drag-drop.md#ondrop)阶段调用仅支持该阶段调用的接口，会抛出此错误码。

**可能原因**

当前所处阶段错误。

**处理步骤**

在[onDrop](ts-universal-events-drag-drop.md#ondrop)阶段调用相应接口。

## 190004 操作失败

PhonePC/2in1TabletTVWearable

**错误信息**

Operation failed.

**错误描述**

如果开发者在数据未加载或加载完成后调用[cancelDataLoading](arkts-apis-uicontext-dragcontroller.md#canceldataloading15)接口，会抛出此错误码。

**可能原因**

调用时机错误。

**处理步骤**

在数据加载过程中调用[cancelDataLoading](arkts-apis-uicontext-dragcontroller.md#canceldataloading15)接口。
