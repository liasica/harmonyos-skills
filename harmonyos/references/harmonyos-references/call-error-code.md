---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/call-error-code
title: ArkTS API错误码
breadcrumb: API参考 > 应用服务 > Call Service Kit（通话服务） > ArkTS API > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:16:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e84bd3fe0b12badad77e7a657db09c6caa98c454aaf46e67e390be2a4686f9fb
---

说明

以下仅介绍本模块特有错误码，通用错误码请参见[通用错误码](errorcode-universal.md)。

## 1007200001 参数无效

PhoneTabletWearable

**错误信息**

Invalid parameter value.

**错误描述**

参数异常。

**可能原因**

1、参数数量错误，例如必填参数未传递等。

2、通话状态错误，最常见的是上报去电，如果状态不是VOIP\_CALL\_STATE\_DIALING，则上报失败。

3、通话类型错误，目前通话类型只支持语音通话VOIP\_CALL\_VOICE和视频通话VOIP\_CALL\_VIDEO两种。

4、callId不匹配，例如，上报通话状态改变、上报音频状态改变时，如果传入的callId在已有的通话中查不到，则上报失败。

5、重复上报，例如，同一路通话，如果上报了两次去电，则上报失败。

**处理步骤**

1、请确认上述参数传递正确。

2、也可以通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1007200002 服务未启动

PhoneTabletWearable

**错误信息**

Operation failed. Cannot connect to service.

**错误描述**

Call Service Kit未启动。

**可能原因**

调用接口后Call Service Kit服务启动失败。

**处理步骤**

通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1007200003 内部错误

PhoneTabletWearable

**错误信息**

System internal error.

**错误描述**

Call Service Kit内部错误。

**可能原因**

1、通话数量超限，来电最多允许3路，去电只能有1路，超过会上报失败。

2、与运营商通话冲突，例如有运营商通话存在时，不能发起应用内通话去电。

**处理步骤**

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1007200999 未知错误

PhoneTabletWearable

**错误信息**

Unknown error code.

**错误描述**

Call Service Kit未知错误。

**可能原因**

未知。

**处理步骤**

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 8300001 参数无效

PhonePC/2in1TabletWearable

**错误信息**

Invalid parameter value.

**错误描述**

参数异常。

**可能原因**

1、参数数量错误，例如必填参数未传递等。

2、上下文错误，最常见的是无效上下文，不是Stage模型上下文等。

**处理步骤**

1、请确认上述参数传递正确。

2、也可以通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 8300002 无企业来电权限

PhonePC/2in1TabletWearable

**错误信息**

The enterprise permission is not verified.

**错误描述**

无企业来电权限。

**可能原因**

没有申请企业来电权限。

**处理步骤**

通过[申请接入](../harmonyos-guides/callservice-enterprise-contact-display.md#申请接入)申请企业来电权限，或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 8300003 内部错误

PhonePC/2in1TabletWearable

**错误信息**

System internal error.

**错误描述**

Call Service Kit内部错误。

**可能原因**

查询企业应用超时或上下文中获取token失败。

**处理步骤**

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 8300999 未知错误

PhonePC/2in1TabletWearable

**错误信息**

Unknown error code.

**错误描述**

Call Service Kit未知错误。

**可能原因**

未知。

**处理步骤**

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。
