---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveview-error-code
title: ArkTS API错误码
breadcrumb: API参考 > 应用服务 > Live View Kit（实况窗服务） > ArkTS API > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5a8be660ba12add8fb120c5cd4bebe5a63dc2722595d35b51e7d27a0776bb8c8
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 1003500001 系统错误

**错误信息**

Internal error.

**错误描述**

当发生系统内部错误时，将返回该错误码。

**可能原因**

系统内部错误。

**处理步骤**

进行重试操作或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1003500002 序列化或反序列化失败

**错误信息**

Marshalling or unmarshalling error.

**错误描述**

序列化或反序列化错误时，将返回该错误码。

**可能原因**

实况窗服务异常。

**处理步骤**

进行重试操作或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1003500003 连接服务失败

**错误信息**

Failed to connect service.

**错误描述**

当连接实况窗服务发生错误时，将返回该错误码。

**可能原因**

实况窗服务繁忙或异常。

**处理步骤**

进行重试操作或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1003500004 实况窗开关关闭

**错误信息**

LiveView is not enabled.

**错误描述**

当实况窗开关为关闭状态时，方法将返回该错误码。

**可能原因**

应用的实况窗开关为关闭状态。

**处理步骤**

在设置 > 应用和元服务中，选择应用开启实况窗开关。

## 1003500005 实况窗权益未申请

**错误信息**

The right of liveView is not enabled.

**错误描述**

当实况窗权益未申请时，将返回该错误码。

**可能原因**

应用未申请对应场景的权益。

**处理步骤**

若已申请实况窗权益，请确认event字段与开通权益的场景匹配；若未申请实况窗权益，请参考[开发准备](../harmonyos-guides/liveview-preparations.md)，完成实况窗权益申请。

## 1003500006 实况窗已存在

**错误信息**

The liveView already exists.

**错误描述**

当创建实况窗id重复时，将返回该错误码。

**可能原因**

应用创建的实况窗id与已创建的重复。

**处理步骤**

请更换[实况窗id](liveview-liveviewmanager.md#liveview)。

## 1003500007 无法连接服务器

**错误信息**

Couldn't connect to server.

**错误描述**

当网络不可达时，将返回该错误码。

**可能原因**

设备未联网。

**处理步骤**

请检查网络。

## 1003500008 实况窗频度超过限制

**错误信息**

Over max number liveViews per second.

**错误描述**

当实况窗频率超过限制时，将返回该错误码。

**可能原因**

对同一个应用的实况窗创建频率超过每秒10个或更新频率超过每秒20个。

**处理步骤**

请降低实况窗调用频率。

## 1003500009 实况窗id不存在

**错误信息**

The liveView does not exist.

**错误描述**

当实况窗id不存在时，将返回该错误码。

**可能原因**

实况窗id不存在或者实况窗已被删除。

**处理步骤**

1. 检查[创建实况窗](liveview-liveviewmanager.md#liveviewmanagerstartliveview)是否成功。
2. 若创建成功，检查端侧通知中心实况窗是否存在。若不存在，请停止调用此[实况窗id](liveview-liveviewmanager.md#liveview)的接口。

## 1003500010 实况窗已结束

**错误信息**

The liveView has ended.

**错误描述**

当实况窗已经结束，继续更新或结束该实况窗时，将返回该错误码。

**可能原因**

当应用调用[liveViewManager.stopLiveView](liveview-liveviewmanager.md#liveviewmanagerstopliveview)函数结束实况窗后，在应用设置的keepTime内实况窗仍保留在通知中心。此时调用[liveViewManager.updateLiveView](liveview-liveviewmanager.md#liveviewmanagerupdateliveview)或[liveViewManager.stopLiveView](liveview-liveviewmanager.md#liveviewmanagerstopliveview)更新或结束同一id的实况窗。

**处理步骤**

应用调用[liveViewManager.stopLiveView](liveview-liveviewmanager.md#liveviewmanagerstopliveview)结束实况窗并设置keepTime，实况窗保留在通知中心期间，请勿复用该[实况窗id](liveview-liveviewmanager.md#liveview)调用更新、结束接口。

## 1003500011 实况窗顺序不正确

**错误信息**

The liveView sequence is incorrect.

**错误描述**

当应用更新或结束实况窗的序列号小于等于当前的序列号时，将返回该错误码。

**可能原因**

应用调用更新或结束的序列号小于等于当前的序列号。

**处理步骤**

请修改序列号[sequence](liveview-liveviewmanager.md#liveview)后重新更新或结束实况窗。

## 1003500017 超过条件实况窗次数限制

**错误信息**

Over max number liveViews by trigger.

**错误描述**

条件触发的实况窗超过最大次数限制。

**可能原因**

开发者发送条件触发实况消息超过5次。

**处理步骤**

地理围栏实况每日每应用每设备限制发送5次，等到第2日再发送条件触发实况消息。

## 1003500018 基于地理位置的实况窗提醒开关关闭

**错误信息**

Geofencing-based liveView is not enabled.

**错误描述**

基于地理位置的实况窗提醒开关未打开。

**可能原因**

用户关闭了基于地理位置的实况窗提醒开关。

**处理步骤**

需要用户打开基于地理位置的实况窗提醒开关，才能发送地理围栏触发实况的消息。可选择“设置 > 通知和状态栏 > 实况窗”，点击页面右上方4个点标记，点击“个性化提醒”，打开页面中“基于地理位置的实况窗提醒”开关。

## 1003500019 位置功能的开关关闭

**错误信息**

The location switch is off.

**错误描述**

位置功能的开关未开启导致注册地理围栏失败。

**可能原因**

位置功能的开关未开启，导致持续定位、单次定位和地理围栏等功能不可用。

**处理步骤**

需要用户选择设置->隐私和安全->位置，打开“访问我的位置”开关。

## 1003500020 感知与提醒的开关关闭

**错误信息**

The "Awareness & suggestions" switch of the location-based service is turned off.

**错误描述**

位置系统服务的"感知与提醒"开关关闭，导致注册地理围栏失败。

**可能原因**

设置->隐私和安全->位置->最底部"系统服务"->感知与提醒开关被关闭。

**处理步骤**

需要用户选择设置->隐私和安全->位置->最底部"系统服务"，打开访问“感知与提醒”开关。

## 1003500021 系统无法找到实况窗卡片自定义扩展区的ExtensionAbility

**错误信息**

The system failed to find the ExtensionAbility instance for the custom Live View widget template.

**错误描述**

找不到实况窗卡片自定义扩展区的[LiveViewCardExtensionAbility](liveview-card-ability.md)，导致实况窗创建失败。

**可能原因**

开发者在创建实况窗卡片自定义扩展区时，传入的[CustomLayout.abilityName](liveview-liveviewmanager.md#customlayout)不存在。

**处理步骤**

1. 需要开发者在工程内创建一个ExtensionAbility类型的组件并且继承[LiveViewCardExtensionAbility](liveview-card-ability.md)。
2. 开发者在创建实况窗卡片自定义扩展区时，传入的[CustomLayout.abilityName](liveview-liveviewmanager.md#customlayout)为开发者创建的该ExtensionAbility类型的组件的名称。
