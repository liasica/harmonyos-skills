---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-canvas
title: Canvas组件错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > Canvas组件错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:04:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:45d193b55406a174cbf40707e576c9c38da1c9ab4a5c89f03789480707189520
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)。

## 103701 参数错误

**错误信息**

Parameter error.

**错误描述**

参数错误。

**可能原因**

参考报错接口的说明。

**处理步骤**

传入正确的参数。

## 103702 绘制上下文未绑定Canvas组件

**错误信息**

The drawingContext is not bound to a canvas component.

**错误描述**

当前绘制上下文未绑定任何Canvas组件。

**可能原因**

当前绘制上下文没有绑定任何Canvas组件。

**处理步骤**

将绘制上下文绑定至一个Canvas组件后再调用[getContext2DFromDrawingContext](ts-canvasrenderingcontext2d.md#getcontext2dfromdrawingcontext23)方法。

## 103704 OffscreenCanvas已经下树

**错误信息**

OffscreenCanvas object is detached.

**错误描述**

[OffscreenCanvas](ts-components-offscreencanvas.md)已经下树。

**可能原因**

OffscreenCanvas已经下树，不支持当前操作。

**处理步骤**

将当前节点挂载到树上，再执行当前操作。
