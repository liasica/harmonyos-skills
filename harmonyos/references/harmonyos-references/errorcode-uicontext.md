---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uicontext
title: UI上下文错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > UI上下文错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:01:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a27fa036cdcb09c60ad74d20fd31c6aca563957c31f2332ab1f77deb76bf0a7c
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 190001 无效的UIContext对象

**错误信息**

The uiContext is invalid.

**错误描述**

无效的UIContext对象。

**可能原因**

传入的UIContext对象无效。

**处理步骤**

传入有效的UIContext对象。

## 190002 无效的回调函数

**错误信息**

The callback function is invalid.

**错误描述**

无效的回调函数。

**可能原因**

传入的回调函数类型错误。

**处理步骤**

传入非空且符合接口签名要求的回调函数。

## 100101 小于0的非法值

**错误信息**

The parameter value cannot be less than 0.

**错误描述**

参数不能小于0。

**可能原因**

开发者传入了小于0的非法值。

**处理步骤**

传入大于或等于0的参数。

## 100102 参数类型错误

**错误信息**

The parameter value cannot be a floating-point number.

**错误描述**

参数不能为浮点数。

**可能原因**

开发者传入了浮点数。

**处理步骤**

传入整数。

## 100103 调用线程错误

**错误信息**

The function cannot be called from a non-main thread.

**错误描述**

不能在非主线程中调用该函数。

**可能原因**

开发者在非主线程中调用了该函数。

**处理步骤**

在主线程中调用该函数。

## 120007 实例不存在

**错误信息**

The UIContext is not available.

**错误描述**

UIContext不可用。

**可能原因**

传入的实例非法或者对应的实例已销毁。

**处理步骤**

传入有效的UIContext对象。
