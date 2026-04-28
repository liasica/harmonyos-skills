---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-access-token
title: 访问控制错误码
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > 错误码 > 访问控制错误码
category: harmonyos-references
scraped_at: 2026-04-28T07:59:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3723059502249dc29f571603510ac48203408baee18bbdd28ebdfc20e286808f
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 12100001 入参错误

PhonePC/2in1TabletTVWearable

**错误信息**

Invalid Parameter. Error message: messageInfo.

**错误描述**

当入参错误时，将返回该错误码。

**可能原因**

1. tokenId值为0。
2. 指定的权限名为空或者权限名长度大于256。
3. 请求授权/撤销权限的flag取值非法。
4. 注册监听的参数检查错误。
5. 指定的Context不属于当前应用。
6. 请求的权限不属于同一个权限组。
7. 请求的权限中存在应用未声明的权限。
8. 请求的全局开关类型非法。
9. 指定的权限名不是[user\_grant权限](../harmonyos-guides/permissions-for-all-user.md)。
10. 指定的数组成员个数超过1024或成员均为无效值。
11. 请求查看权限使用记录的起始结束时间不合法。
12. 指定的权限名未在应用中声明。

**处理步骤**

检查入参，修正参数值为有效值，有效值请参考各[接口参数说明](js-apis-abilityaccessctrl.md)。

## 12100004 接口未配套使用

PhonePC/2in1TabletTVWearable

**错误信息**

The API is not used in pair with others.

**错误描述**

当接口未配套使用时，将返回该错误码。

**可能原因**

1. 当前接口在未配套使用的情况下，重复调用。
2. 当前接口在未配套使用的情况下，单独调用。

**处理步骤**

1. 检查当前接口是否有配套使用，如调用启动记录的接口后，在未调用停止记录的接口前，不可再次使用相同的入参调用启动记录接口。
2. 检查当前接口是否有配套使用，如停止记录的接口需要在启动记录的接口调用之后方可调用，注销监听接口需要在注册监听接口调用之后方可调用。

## 12100005 监听器数量超过限制

PhonePC/2in1TabletTVWearable

**错误信息**

The number of listeners exceeds the limit.

**错误描述**

当监听器数量超过限制时，将返回该错误码。

**可能原因**

该错误码表示当前监听器数量超过限制200个。

**处理步骤**

及时释放已注册的无用的监听器。

## 12100007 系统服务工作异常

PhonePC/2in1TabletTVWearable

**错误信息**

The service is abnormal.

**错误描述**

当系统服务工作异常时，将返回该错误码。

**可能原因**

1. 权限管理服务无法正常启动。
2. IPC数据读取写入失败。

**处理步骤**

系统服务内部工作异常，请稍后重试，或者重启设备。

## 12100009 服务内部错误

PhonePC/2in1TabletTVWearable

**错误信息**

Common inner error.

**错误描述**

当服务内部发生错误或权限弹框发生错误时，将返回该错误码。

**可能原因**

1. 内部错误
   * 系统服务内部异常或数据库错误。
2. 权限弹框错误
   * 应用处于后台，无法正常拉起弹框。
   * 设备处于锁屏状态，无法正常拉起弹框。
   * 拉起弹框后未及时处理，弹框进程因应用退出而被系统回收，例如用户在多任务界面清理应用进程。

**处理步骤**

1. 内部错误
   * 建议重启设备后重试。
2. 权限弹框错误
   * 确认应用处于前台状态后再发起弹框请求。
   * 确认设备处于解锁状态后再发起弹框请求。
   * 确认弹框已被及时处理，若弹框进程因应用退出而被系统回收则无需额外操作。
3. 若您的问题仍无法解决，请通过在线提单提交问题说明及日志信息，支持人员会及时处理。

## 12100010 存在未被处理的请求

**错误信息**

The request already exists.

**错误描述**

当存在未被处理的请求时，将返回该错误码。

**可能原因**

上一次请求未被处理。

**处理步骤**

请处理完上次请求。

## 12100011 输入的所有权限均已被授权

PhonePC/2in1TabletTVWearable

**错误信息**

All permissions in the permission list have been granted.

**错误描述**

当输入的所有权限均已被授权时，将返回该错误码。

**可能原因**

所有权限均已被授权。

**处理步骤**

无需处理，返回此错误码表示申请权限已被授权，不会拉起权限设置弹框。

## 12100012 输入的权限中存在未被用户拒绝过的权限

PhonePC/2in1TabletTVWearable

**错误信息**

The permission list contains the permission that has not been revoked by the user.

**错误描述**

当输入的权限中存在未被用户拒绝过的权限时，将返回该错误码。

**可能原因**

存在未被用户拒绝过的权限。

**处理步骤**

请先调用requestPermissionsFromUser向用户申请权限。

## 12100013 全局开关已开启

PhonePC/2in1TabletTVWearable

**错误信息**

The specific global switch is already open.

**错误描述**

当全局开关已开启时，将返回该错误码。

**可能原因**

全局开关已开启。

**处理步骤**

无需处理，返回此错误码表示全局开关已开启，不会拉起全局开关设置弹框。

## 12100014 非预期的权限

PhonePC/2in1TabletTVWearable

**错误信息**

Unexpected permission.

**错误描述**

当输入的权限不符合使用场景时，将返回该错误码。

**可能原因**

1. [再次拉起权限设置弹框](js-apis-abilityaccessctrl.md#requestpermissiononsetting12)时，传入了manual\_settings授权方式的权限。
2. 授权或取消授权时，传入了非user\_grant和manual\_settings授权方式的权限。
3. [拉起跳转设置页弹窗](js-apis-abilityaccessctrl.md#openpermissiononsetting22)时，传入了非manual\_settings授权方式的权限。

**处理步骤**

请确认输入的权限是否符合使用场景。
