---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scenario-fusion-arkts-api-error-code
title: ArkTS API错误码
breadcrumb: API参考 > 应用服务 > Scenario Fusion Kit（融合场景服务） > ArkTS API > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:18:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ed8f41476a8c1485e9d0f6353c99af55fc618e3a74c389f8a5a9b5bd1a2139c7
---

说明

本模块错误码请参考以下链接。

[通用错误码](errorcode-universal.md)

[ArkUI错误码](arkui-arkts-errcode.md)

[Connectivity Kit错误码](connectivity-arkts-errcode.md)

[Location Kit错误码](location-arkts-errcode.md)

[ArkTS API错误码](errorcode-utils.md)

## 1009601001 非法的服务号ID

PhonePC/2in1TabletTVWearable

**错误信息**

Invalid service account id.

**错误描述**

非法的服务号ID。

**可能原因**

1.传入的服务号ID不正确或已失效。

2.服务号状态为已冻结。

**处理步骤**

1.确认传入的服务号ID是否正确。

2.确认服务号是否为生效状态，可在[我的华为服务号](https://developer.huawei.com/consumer/cn/console/service/FastService/service/1063)查看。

## 1009601002 用户未登录华为账号

PhonePC/2in1TabletTVWearable

**错误信息**

The user has not logged in with HUAWEI ID.

**错误描述**

用户未登录华为账号。

**可能原因**

用户未登录华为账号。

**处理步骤**

用户登录华为账号。

## 1009601003 请求服务号云失败

PhonePC/2in1TabletTVWearable

**错误信息**

Request server failed.

**错误描述**

请求服务号云失败。

**可能原因**

服务号云系统出现问题。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1009601004 网络连接失败

PhonePC/2in1TabletTVWearable

**错误信息**

Network connection error.

**错误描述**

网络连接失败。

**可能原因**

手机网络未连接或其他网络异常。

**处理步骤**

检查网络连接。

## 1009601005 其他异常

PhonePC/2in1TabletTVWearable

**错误信息**

Other error.

**错误描述**

其他异常。

**可能原因**

系统出现异常或者调用太频繁。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。
