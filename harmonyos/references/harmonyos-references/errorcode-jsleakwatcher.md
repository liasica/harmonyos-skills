---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-jsleakwatcher
title: JsLeakWatcher错误码
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 错误码 > JsLeakWatcher错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4081e7aa0e41834e4ac1b0f6b1507d21035143d64eb70ac84eec35fe14b8a71a
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 10801001 参数isEnabled无效

**错误信息**

The parameter isEnabled is invalid.

**错误描述**

在调用接口函数enableLeakWatcher时，传入无效参数isEnabled。

**可能原因**

1. 传入参数isEnabled的类型错误。
2. 必填参数未指定。

**处理步骤**

确保传入参数isEnabled的类型正确，且必填参数已指定。

## 10801002 参数config无效

**错误信息**

The parameter config is invalid.

**错误描述**

在调用接口函数enableLeakWatcher时，传入无效参数config。

**可能原因**

1. 传入参数config的类型错误。
2. 必填参数未指定。
3. 参数校验失败。该参数为字符串类型数组，数组元素必须包含：XComponent、NodeContainer、Window、CustomComponent或Ability中一个或者多个。

**处理步骤**

确保传入参数config的类型正确，必填参数已指定，且数组元素包含XComponent、NodeContainer、Window、CustomComponent或Ability中的一个或多个。

## 10801003 参数callback无效

**错误信息**

The parameter callback is invalid.

**错误描述**

在调用接口函数enableLeakWatcher时，传入无效参数callback。

**可能原因**

1. 传入参数callback的类型错误。
2. 必填参数未指定。
3. 参数校验失败。校验callback回调函数入参是一个包含两个元素字符串类型数组。

**处理步骤**

确保传入参数callback的类型正确，必填参数已指定，且该回调函数入参是一个包含两个元素字符串类型数组。

索引0为泄漏列表文件名，后缀为.jsleaklist；索引1为虚拟机内存快照文件名，后缀为.rawheap。
