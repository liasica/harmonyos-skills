---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice
title: ArkTS API错误码
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-09-02T14:53:20+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:6ed7271eacb0c4d1349841d997f77d7f1ca5a207f331f618c3a51a2af9b18661
---

以下授权相关错误码的详细介绍请参见[华为账号服务ArkTS错误码](errorcode-account-kit.md)。

| **名称** | **值** | **说明** |
| --- | --- | --- |
| PACKAGE\_FINGERPRINT\_CHECK\_ERROR | [1001500001](errorcode-account-kit.md#section1001500001-应用指纹证书校验失败) | 应用指纹证书校验失败。 |
| DUPLICATE\_REQUEST\_REJECTED | [1001500002](errorcode-account-kit.md#section1001500002-重复请求) | 重复请求，当已有相同的请求在处理时，返回此错误码，此错误码不需要处理。你的应用需实现点击控制，防止连续点击发起相同请求。 |
| ACCOUNT\_NOT\_LOGGED\_IN | [1001502001](errorcode-account-kit.md#section1001502001-用户未登录华为账号) | 华为账号未登录。 |
| APP\_NOT\_AUTHORIZED | [1001502002](errorcode-account-kit.md#section1001502002-应用未授权) | 应用未授权。 |
| PARAMETER\_INVALID | [1001502003](errorcode-account-kit.md#section1001502003-输入参数值无效) | 无效参数，接口传参异常等。 |
| NETWORK\_ERROR | [1001502005](errorcode-account-kit.md#section1001502005-网络错误) | 网络异常。 |
| INTERNAL\_ERROR | [1001502009](errorcode-account-kit.md#section1001502009-内部错误) | 内部错误，如华为账号服务器错误或其他内部错误等。 |
| USER\_CANCELED | [1001502012](errorcode-account-kit.md#section1001502012-用户取消授权) | 用户取消授权。 |
| SCOPE\_OR\_PERMISSION\_NOT\_REQUESTED | [1001502014](errorcode-account-kit.md#section1001502014-应用未申请scopes或permissions权限) | 应用未申请scopes或permissions权限。 |

## 1002700001 系统内部错误

**错误信息**

System internal error.

**错误描述**

系统内部错误。

**可能原因**

未知。

**处理步骤**

不同场景，根据具体message提示解决。若仍无法解决，通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1002700002 数据库异常

**错误信息**

Database processing error.

**错误描述**

数据库异常。

**可能原因**

未知。

**处理步骤**

重启设备后重试。若仍无法解决，通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1002701001 网络错误

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

**错误信息**

Account error. Failed to obtain account information with HUAWEI ID.

**错误描述**

账号异常。

**可能原因**

账号异常。

**处理步骤**

重启设备后重试。若仍无法解决，通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1002703001 用户隐私未同意

**错误信息**

User privacy is not agreed.

**错误描述**

用户隐私未同意。

**可能原因**

用户从未启动过运动健康App。

**处理步骤**

引导用户启动运动健康App，参考[FAQ](../harmonyos-guides/health-faqs.md)。

## 1009104001 联动已开启

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

**错误信息**

Unsupported sport type.

**错误描述**

联动不支持该运动类型。

**可能原因**

传入了不支持的运动类型。

**处理步骤**

检查传入的运动类型，请参见[锻炼记录类型常量](health-api-exercisesequencehelper.md)。

## 1009104003 非法指令

**错误信息**

Illegal command.

**错误描述**

在当前状态下，指令非法。

**可能原因**

1、应用自身调用接口时机错误；其他应用已开启联动。

2、应用自身调用接口时机错误；联动未开启。

3、应用自身调用接口时机错误；联动未结束。

**处理步骤**

1、检查应用自身业务流程。

2、捕获异常处理其他应用开启联动场景。

3、重新选择时机调用接口。

## 1009104004 权限校验异常

**错误信息**

Permission verification error. Application has no permission, such as Motion Permission.

**错误描述**

应用未具有相关权限，如健身运动权限。

**可能原因**

应用未具有相关权限。

**处理步骤**

请检查是否有调用API的权限。

## 1009104005 动态库加载异常

**错误信息**

Failed to load the dynamic library.

**错误描述**

动态库加载异常。

**可能原因**

动态库文件不存在或已经有动态库被加载。

**处理步骤**

1、检查load传入路径是否正确。

2、调用[load](health-api-healthservice-lite.md#workoutload)函数，检查是否返回该错误码，返回则代表动态库已经被加载，需要先调用[unload](health-api-healthservice-lite.md#workoutunload)函数卸载动态库。

## 1009104006 动态库卸载异常

**错误信息**

Failed to unload the dynamic library.

**错误描述**

动态库卸载异常。

**可能原因**

动态库已经被卸载。

**处理步骤**

1、检查unload传入路径是否正确。

2、调用[unload](health-api-healthservice-lite.md#workoutunload)函数，检查是否返回该错误码，返回则代表动态库已经被卸载，不返回错误码代表动态库卸载成功。

## 1009104999 通用错误码

**错误信息**

System internal error.

**错误描述**

其他异常。

**可能原因**

其他。

**处理步骤**

不同场景，根据具体message提示解决。若仍无法解决，通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 14500101 服务异常

**错误信息**

Service exception.

**错误描述**

服务异常。

**可能原因**

未知。

**处理步骤**

重启设备后重试。通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## Health Service Kit调用失败返回201

错误码201是[通用错误码](errorcode-universal.md#section201-权限校验失败)，标识参数检查失败。

Health Service Kit出现201错误码时表示鉴权失败，可能由以下情况导致：

**可能原因**

1、应用指纹配置不正确。

2、缺少权限。

3、部分接口仅白名单用户可调用。

4、测试用户数已达上限。

**解决措施**

1、检查AGC上应用的指纹证书，详情请见[添加公钥指纹](../harmonyos-guides/application-dev-overview.md#条件必选添加公钥指纹)。

2、参考[管理用户授权](../harmonyos-guides/health-add-permissions.md)，确认用户已授权相关权限。

3、用户申请成为测试用户失败，请尽快参考[申请验证获取正式权限](../harmonyos-guides/health-verification.md)，完成管理台应用验收。

4、通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。
