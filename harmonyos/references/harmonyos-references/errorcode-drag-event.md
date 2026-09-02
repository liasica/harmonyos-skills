---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-drag-event
title: 拖拽事件错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > 拖拽事件错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:01:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7a084de86ae15d6a572b04451f5dc41178515234e8af9bfca6c5041188ef1bf9
---

**说明** 

本文档介绍拖拽事件模块特有的错误码，涵盖数据获取、操作阶段和数据加载过程中的常见异常，帮助开发者识别错误原因并采取对应的处理措施。通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 190001 数据未找到

**错误信息**

Data not found.

**错误描述**

当开发者调用DragEvent的[getData](ts-universal-events-drag-drop.md#getdata10)接口时，若还未获取到数据，会抛出此错误码。该错误码为string类型。

**可能原因**

DragEvent的数据暂未获取成功。

**处理步骤**

NA

## 190002 获取数据错误

**错误信息**

Data error.

**错误描述**

当开发者调用DragEvent的[getData](ts-universal-events-drag-drop.md#getdata10)接口时，若获取的数据有错误，会抛出此错误码。该错误码为string类型。

**可能原因**

数据获取错误。

**处理步骤**

NA

## 190003 当前阶段不允许操作

**错误信息**

Operation not allowed for current phase.

**错误描述**

如果开发者在非[onDrop](ts-universal-events-drag-drop.md#ondrop)阶段调用仅支持在该阶段调用的接口，会抛出此错误码。该错误码为string类型。

**可能原因**

当前处于非[onDrop](ts-universal-events-drag-drop.md#ondrop)阶段。

**处理步骤**

在[onDrop](ts-universal-events-drag-drop.md#ondrop)阶段调用相应接口。

## 190004 操作失败

**错误信息**

Operation failed.

**错误描述**

如果开发者未在拖拽释放后的数据加载过程中调用[cancelDataLoading](arkts-apis-uicontext-dragcontroller.md#canceldataloading15)接口，会抛出此错误码。该错误码为string类型。

**可能原因**

调用时机错误。

**处理步骤**

在数据加载过程中调用[cancelDataLoading](arkts-apis-uicontext-dragcontroller.md#canceldataloading15)接口。
