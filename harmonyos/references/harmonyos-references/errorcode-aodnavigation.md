---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-aodnavigation
title: ArkTS API错误码
breadcrumb: API参考 > 系统 > 硬件 > AOD Navigation Kit（熄屏导航服务） > ArkTS API > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:15+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:0c134aca7bcb1eadcfa6f1401b9714e1c7590a337a9f21c87561badc4246ccb9
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 1028300001 AOD导航服务初始化失败

**错误信息**

AOD navigation service initialization failed.

**错误描述**

熄屏导航服务初始化失败。

**可能原因**

熄屏导航服务初始化过程中发生异常，如进程启动失败等。

**处理步骤**

进行重试操作或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1028300002 序列化或反序列化失败

**错误信息**

Marshalling or unmarshalling error.

**错误描述**

序列化或反序列化错误。

**可能原因**

熄屏导航服务异常。

**处理步骤**

进行重试操作或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1028300003 依赖服务异常

**错误信息**

Service dependency error.

**错误描述**

依赖服务发生错误。

**可能原因**

AOD导航依赖的服务异常。

**处理步骤**

进行重试操作或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1028300004 AOD导航权益未申请

**错误信息**

The AOD navigation permission is not enabled.

**错误描述**

熄屏导航服务的权益未申请。

**可能原因**

应用未申请熄屏导航服务的权益。

**处理步骤**

若未申请熄屏导航服务权益，请参考[开发准备](../harmonyos-guides/aodnavigation-preparations.md)步骤2。

## 1028300005 AOD导航开关未使能

**错误信息**

The AOD navigation switch is not enabled.

**错误描述**

AOD导航开关未启用。

**可能原因**

应用的AOD导航开关为关闭状态。

**处理步骤**

在“设置 > 桌面和个性化 > 熄屏显示 > 熄屏导航”中，选择打开开关。

## 1028300006 AOD导航配置未设置

**错误信息**

The AOD navigation configuration has not been set up.

**错误描述**

未进行AOD导航配置初始化。

**可能原因**

应用未进行配置初始化即调用其他方法。

**处理步骤**

先完成初始化[setupAodNaviConfig](aodnavigation-aodnavimanager.md#aodnavimanagersetupaodnaviconfig)和事件注册监听[onAodNaviEvent](aodnavigation-aodnavimanager.md#aodnavimanageronaodnavievent)后再调用其他接口。

## 1028300007 轨迹路线点数量超限

**错误信息**

The number of route points exceeds the limit.

**错误描述**

轨迹路线点数量超限。

**可能原因**

应用下发的轨迹点数量超过限制。

**处理步骤**

请减少轨迹点数量后重新调用。

## 1028300008 无效的事件ID

**错误信息**

Invalid event ID.

**错误描述**

应用未下发正确的事件ID。

**可能原因**

应用下发了自定义或者无效的eventId。

**处理步骤**

检查eventId是否正确使用，需要使用回调事件信息[AodNaviEventInfo](aodnavigation-aodnavimanager.md#aodnavieventinfo)中的eventId，不支持自定义。

## 1028300009 AOD显示参数配置错误

**错误信息**

Invalid AOD view data configuration. Possible causes:

1. Data count must be within the range of 1 to 6.
2. Data count does not match the number of configured entries.
3. Configuration includes items unsupported by the current device.

**错误描述**

AOD界面显示参数配置错误。

**可能原因**

1. 参数个数必须在1~6个以内。
2. 参数个数和配置项个数不匹配。
3. 配置了设备不支持的配置项。

**处理步骤**

请根据错误信息检查AOD视图数据配置，确保参数个数在1~6范围内，配置项个数匹配，且仅使用设备支持的配置项。

## 1028300010 休眠策略下不允许调用UpdateAodViewData

**错误信息**

UpdateAodViewData must not be called under the hibernate strategy.

**错误描述**

应用休眠策略下不允许调用[updateAodViewData](aodnavigation-aodnavimanager.md#aodnavimanagerupdateaodviewdata)方法。

**可能原因**

在应用休眠策略下调用了[updateAodViewData](aodnavigation-aodnavimanager.md#aodnavimanagerupdateaodviewdata)方法。

**处理步骤**

如果选择应用休眠策略，请调用[setNaviDataToAod](aodnavigation-aodnavimanager.md#aodnavimanagersetnavidatatoaod)方法传递数据，而不是[updateAodViewData](aodnavigation-aodnavimanager.md#aodnavimanagerupdateaodviewdata)方法。

## 1028300011 路线轨迹点保存失败

**错误信息**

Failed to save the route points.

**错误描述**

路线轨迹点保存失败。

**可能原因**

轨迹点数据保存异常。

**处理步骤**

进行重试操作或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。
