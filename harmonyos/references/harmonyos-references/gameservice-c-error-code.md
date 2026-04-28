---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-c-error-code
title: C API错误码
breadcrumb: API参考 > 应用服务 > Game Service Kit（游戏服务） > C API > C API错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:16:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f89aaae1f1d2f36f34618c53ae7601092b9991c4ad25eab1bb575369d7143033
---

说明

以下仅介绍Game Service Kit特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)。

## 1010300001 系统内部错误

**错误信息**

System internal error.

**错误描述**

系统内部错误。

**可能原因**

Game Service Kit系统内部错误。

**处理步骤**

通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101704354579010004&keyWord=Game Service Kit)提交问题，华为工程师会及时处理。

## 1010300002 鉴权失败

PhonePC/2in1Tablet

**错误信息**

Auth failed.

**错误描述**

鉴权失败。

**可能原因**

网络连接或传参错误。

**处理步骤**

1. 首次使用设备进行登录时，请确认网络连接正常。
2. 请检查[HMS\_GamePerformance\_Init](gameservice-game-performance.md#hms_gameperformance_init)接口传参是否正确。

## 1010300003 非法请求

PhonePC/2in1Tablet

**错误信息**

Invalid request.

**错误描述**

非法请求。

**可能原因**

未初始化或初始化未成功时，调用了其他接口。

**处理步骤**

请先调用[HMS\_GamePerformance\_Init](gameservice-game-performance.md#hms_gameperformance_init)接口，并确保调用成功。

## 1010300004 参数错误

**错误信息**

Parameter error.

**错误描述**

参数错误。

**可能原因**

* 必填参数为空。
* 参数校验失败。

**处理步骤**

请检查必选参数是否传入，或者传入参数是否符合要求。
