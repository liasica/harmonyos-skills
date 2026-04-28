---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-power
title: 系统电源管理错误码
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 错误码 > 系统电源管理错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:09:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:97020fe69dfaae967389cbfc130aa63b87d4c6c1e5296e020a99a363f9e8b796
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 4900101 连接服务失败

PhonePC/2in1TabletTVWearable

**错误信息**

Failed to connect to the service.

**错误描述**

操作失败，连接系统服务发生异常。

**可能原因**

1. 系统服务停止运行。
2. 系统服务内部通讯发生异常。

**处理步骤**

检查系统服务是否正常运行。

1. 在控制台中输入如下命令，查看当前的系统服务列表。

   ```
   1. > hdc shell hidumper -ls
   ```
2. 查看系统服务列表中是否包含PowerManagerService系统服务。

## 4900102 正在关机中

**错误信息**

Operation failed. The system is shutting down.

**错误描述**

操作失败，系统正在关机。

**可能原因**

系统正在处于关机过程中。

**处理步骤**

在系统正常运行的状态下进行操作。

## 4900201 接口调用间隔过短

**错误信息**

The device activity is being refreshed too frequently; the minimum timeinterval is 100 ms.

**错误描述**

频繁刷新设备活跃状态导致刷新失败，刷新设备活跃状态最小时间间隔为100ms。

**可能原因**

频繁刷新设备活跃状态。

**处理步骤**

此错误说明100ms内已经刷新设备活跃状态，无需再次刷新设备活跃状态。如需再次刷新，请在100ms后进行重试。

## 4900301 电源模式设置失败

**错误信息**

Setting the power mode failed.

**错误描述**

设置电源模式失败。

**可能原因**

电源模式管控规则导致设置电源模式失败。

**处理步骤**

当前电源模式不可切换至目标电源模式，可使用[getPowerMode](js-apis-power.md#powergetpowermode9)接口查询当前电源模式。
