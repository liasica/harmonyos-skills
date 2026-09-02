---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-screentimeguard
title: ArkTS API错误码
breadcrumb: API参考 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > ArkTS API > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:03:08+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:3248024cb85eba3f610d2c640d17271338435ab7a02acb2c8e28bba6168b05c0
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参见[通用错误码](errorcode-universal.md)。

## 1019000001 内部错误

**错误信息**

Internal error.

**错误描述**

内部错误。

**可能原因**

1、当前应用运行在隐私空间或其它子空间中。

2、系统服务错误或其它内部错误。

**处理步骤**

1、切换到主空间后重试。

2、重启设备后重试。

3、若重启后仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1019000002 用户未授权

**错误信息**

The user has not authorized the application to access this interface.

**错误描述**

用户未授权应用程序访问此接口。

**可能原因**

1、应用未向用户请求授权。

2、用户拒绝了授权申请。

**处理步骤**

调用请求用户授权接口[requestUserAuth](screentimeguard-guardservice.md#requestuserauth)获取用户授权。

## 1019000003 用户取消

**错误信息**

The user canceled the operation.

**错误描述**

用户取消了操作。

**可能原因**

用户主动关闭了半模态页面。

**处理步骤**

由于用户主动取消操作，应用无需特殊处理。

## 1019000004 策略数量超限

**错误信息**

The number of strategies exceeds the upper limit.

**错误描述**

策略数量超过上限。

**可能原因**

同一应用下添加太多策略，使其数量超过50条限制。

**处理步骤**

调用策略删除接口[removeGuardStrategy](screentimeguard-guardservice.md#removeguardstrategy)删除已添加策略，以减少策略数量。

## 1019000005 策略名称重复

**错误信息**

The strategy name is already existed.

**错误描述**

策略名称已存在。

**可能原因**

在同一应用下添加具有相同名称的策略。

**处理步骤**

1、先调用策略查询接口[queryGuardStrategies](screentimeguard-guardservice.md#queryguardstrategies)获取应用名下有哪些策略。

2、将本次调用使用的策略名称更换成不重复的策略名称。

## 1019000006 策略不存在

**错误信息**

Nonexistent strategy.

**错误描述**

没有对应名称的策略。

**可能原因**

1、试图修改、删除、启用、停止不存在的策略。

2、调用查询策略运行数据接口[queryGuardStrategyData](screentimeguard-guardservice.md#queryguardstrategydata)查询不存在策略的数据。

**处理步骤**

1、先调用策略查询接口[queryGuardStrategies](screentimeguard-guardservice.md#queryguardstrategies)获取应用名下有哪些策略，判断策略是否存在。

2、调用策略添加接口[addGuardStrategy](screentimeguard-guardservice.md#addguardstrategy)添加相应的策略后再执行操作。

## 1019000007 策略重复执行

**错误信息**

The strategy is already being executed.

**错误描述**

该策略已在执行中。

**可能原因**

试图启动的管控策略已在执行中。

**处理步骤**

调用策略停止接口[stopGuardStrategy](screentimeguard-guardservice.md#stopguardstrategy)停止相应的策略后再执行操作。

## 1019000008 策略未执行

**错误信息**

This strategy has not been started yet.

**错误描述**

该策略尚未开始执行。

**可能原因**

1、试图停止的管控策略已不在执行中。

2、试图查询不在执行中的管控策略运行数据。

**处理步骤**

调用策略启动接口[startGuardStrategy](screentimeguard-guardservice.md#startguardstrategy)启动相应的策略后再执行操作。

## 1019000009 参数检查失败

**错误信息**

Parameter error. Possible causes:1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

**错误描述**

1、必填参数为空。

2、参数类型不正确。

3、参数校验失败。

**可能原因**

1、必选参数没有传入。

2、参数类型错误 (Type Error)。

3、参数数量错误 (Argument Count Error)。

4、空参数错误 (Null Argument Error)。

5、参数格式错误 (Format Error)。

6、参数值范围错误 (Value Range Error)。

**处理步骤**

请检查必选参数是否传入，或者传入的参数类型是否错误。对于参数校验失败，阅读参数规格约束，按照可能原因进行排查。

## 1019000010 该设备不支持此API

**错误信息**

Capability is not supported on current device.

**错误描述**

该设备不支持此API，因此无法正常调用。

**可能原因**

在除Phone、Tablet设备之外的设备上调用了此API。

**处理步骤**

应避免在除Phone、Tablet之外的设备上调用此API，或在代码中增加判断来规避异常场景下应用在不同设备上运行所产生的影响。

## 1019000011 策略类型不支持

**错误信息**

The strategy type is not supported.

**错误描述**

该API不支持此策略类型，因此无法正常调用。

**可能原因**

在调用查询策略运行数据接口[queryGuardStrategyData](screentimeguard-guardservice.md#queryguardstrategydata)接口时，传入了非[INCLUSIVE\_DURATION\_TYPE](screentimeguard-guardservice.md#timestrategytype)类型的策略。

**处理步骤**

请检查调用查询策略运行数据接口[queryGuardStrategyData](screentimeguard-guardservice.md#queryguardstrategydata)接口时，传入的策略类型是否为[INCLUSIVE\_DURATION\_TYPE](screentimeguard-guardservice.md#timestrategytype)。
