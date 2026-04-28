---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice
title: ArkTS API错误码
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:16:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5e3165c6c4fe0cb328c6ffe529f906a63abc54cbabaa9a1e90d6f4aa26b016cd
---

以下授权相关错误码的详细介绍请参见[华为账号服务ArkTS错误码](account-api-error-code.md)。

| **名称** | **值** | **说明** |
| --- | --- | --- |
| PACKAGE\_FINGERPRINT\_CHECK\_ERROR | [1001500001](account-api-error-code.md#section1001500001-应用指纹证书校验失败) | 应用指纹证书校验失败。 |
| DUPLICATE\_REQUEST\_REJECTED | [1001500002](account-api-error-code.md#section1001500002-重复请求) | 重复请求，当已有相同的请求在处理时，返回此错误码，此错误码不需要处理。你的应用需实现点击控制，防止连续点击发起相同请求。 |
| ACCOUNT\_NOT\_LOGGED\_IN | [1001502001](account-api-error-code.md#section1001502001-用户未登录华为账号) | 华为账号未登录。 |
| APP\_NOT\_AUTHORIZED | [1001502002](account-api-error-code.md#section1001502002-应用未授权) | 应用未授权。 |
| PARAMETER\_INVALID | [1001502003](account-api-error-code.md#section1001502003-输入参数值无效) | 无效参数，接口传参异常等。 |
| NETWORK\_ERROR | [1001502005](account-api-error-code.md#section1001502005-网络错误) | 网络异常。 |
| INTERNAL\_ERROR | [1001502009](account-api-error-code.md#section1001502009-内部错误) | 内部错误，如华为账号服务器错误或其他内部错误等。 |
| USER\_CANCELED | [1001502012](account-api-error-code.md#section1001502012-用户取消授权) | 用户取消授权。 |
| SCOPE\_OR\_PERMISSION\_NOT\_REQUESTED | [1001502014](account-api-error-code.md#section1001502014-应用未申请scopes或permissions权限) | 应用未申请scopes或permissions权限。 |

## 201 鉴权失败

PhoneTabletWearable

**错误信息**

Permission verification failed.

**错误描述**

鉴权失败。

**可能原因**

1、应用指纹配置不正确。

2、缺少权限。

3、部分接口仅白名单用户可调用。

4、测试用户数已达上限。

**处理步骤**

1、检查AGC上应用的指纹证书，详情请见[添加公钥指纹](../harmonyos-guides/application-dev-overview.md#section1726913517284)。

2、参考[管理用户授权](../harmonyos-guides/health-add-permissions.md)，确认用户已授权相关权限。

3、用户申请成为测试用户失败，请尽快参考[申请验证获取正式权限](../harmonyos-guides/health-verification.md)，完成管理台应用验收。

4、通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 401 参数不合法

PhoneTabletWearable

**错误信息**

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed.

**错误描述**

参数错误。

**可能原因**

参数填写不正确。

**处理步骤**

1、参考文档确认数据必填项、取值范围等是否填写正确。

2、通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 801 该设备不支持此API

PhoneTabletWearable

**错误信息**

Capability not supported. Failed to call the API due to limited device capabilities.

**错误描述**

该设备不支持此API，因此无法正常调用。

**可能原因**

可能出现该错误码的场景为：该设备已支持该API所属的Syscap, 但是并不支持此API。

**处理步骤**

应避免在该设备上使用此API，或在代码中通过判断来规避异常场景下应用在不同设备上运行所产生的影响。

## 1002700001 系统内部错误

PhoneTabletWearable

**错误信息**

System internal error.

**错误描述**

系统内部错误。

**可能原因**

未知。

**处理步骤**

不同场景，根据具体message提示解决。若仍无法解决，通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1002700002 数据库异常

PhoneTabletWearable

**错误信息**

Database processing error.

**错误描述**

数据库异常。

**可能原因**

未知。

**处理步骤**

通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1002701001 网络错误

PhoneTabletWearable

**错误信息**

Network error. The network is unavailable.

**错误描述**

网络错误。

**可能原因**

网络未连接。

**处理步骤**

1、检查网络配置。

2、通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1002702001 账号未登录

PhoneTabletWearable

**错误信息**

Account error. The user has not logged in with HUAWEI ID.

**错误描述**

账号未登录。

**可能原因**

账号未登录。

**处理步骤**

1、参考[管理用户授权](../harmonyos-guides/health-add-permissions.md)，拉起登录授权，登录账号后再重新调用接口。

2、通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1002702002 账号异常

PhoneTabletWearable

**错误信息**

Account error. Failed to obtain account information with HUAWEI ID.

**错误描述**

账号异常。

**可能原因**

账号异常。

**处理步骤**

通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1002703001 用户隐私未同意

PhoneTabletWearable

**错误信息**

User privacy is not agreed.

**错误描述**

用户隐私未同意。

**可能原因**

用户从未启动过运动健康App。

**处理步骤**

引导用户启动运动健康App，参考[FAQ](../harmonyos-guides/health-faqs.md)。

## 1009104001 联动已开启

PhoneTabletWearable

**错误信息**

Sport service busy. Workout is already started by other application.

**错误描述**

联动已开启。

**可能原因**

应用/其他应用已调用start开启联动。

**处理步骤**

1、检查自身业务流程是否有重复开启联动操作。

2、捕获异常处理其他应用开启联动场景。

## 1009104002 不支持运动类型

PhoneTabletWearable

**错误信息**

Unsupported sport type.

**错误描述**

联动不支持该运动类型。

**可能原因**

传入了不支持的运动类型。

**处理步骤**

检查传入的运动类型，请参见[锻炼记录类型常量](health-api-exercisedequencehelper.md)。

## 1009104003 非法指令

PhoneTabletWearable

**错误信息**

Illegal command.

**错误描述**

在当前状态下，指令非法。

**可能原因**

应用自身调用接口时机错误；其他应用已开启联动。

**处理步骤**

1、检查应用自身业务流程。

2、捕获异常处理其他应用开启联动场景。

## 1009104004 权限校验异常

PhoneTabletWearable

**错误信息**

Permission verification error. Application has no permission, such as Motion Permission.

**错误描述**

应用未具有相关权限，如健身运动权限。

**可能原因**

应用未具有相关权限。

**处理步骤**

请检查是否有调用API的权限。

## 1009104999 通用错误码

PhoneTabletWearable

**错误信息**

System internal error.

**错误描述**

其他异常。

**可能原因**

其他。

**处理步骤**

不同场景，根据具体message提示解决。若仍无法解决，通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 14500101 服务异常

PhoneTabletWearable

**错误信息**

Service exception.

**错误描述**

服务异常。

**可能原因**

未知。

**处理步骤**

通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。
