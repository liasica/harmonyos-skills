---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-stationary
title: @ohos.stationary (设备状态感知框架)
breadcrumb: API参考 > 系统 > 硬件 > Multimodal Awareness Kit（多模态融合感知服务） > ArkTS API > @ohos.stationary (设备状态感知框架)
category: harmonyos-references
scraped_at: 2026-04-28T08:10:54+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:2c416860097f3b9cfeeaaca00082fcd0244a9a9adf799c3c0156a809d3bd49b8
---

设备状态感知框架提供设备状态感知能力，包括绝对静止和相对静止。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块不支持在x86平台上运行。

## 导入模块

PhonePC/2in1Tablet

```
1. import { stationary } from '@kit.MultimodalAwarenessKit';
```

## ActivityResponse

PhonePC/2in1Tablet

服务响应抽象接口。

**系统能力**：SystemCapability.Msdp.DeviceStatus.Stationary

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | [ActivityState](js-apis-stationary.md#activitystate) | 否 | 否 | 设备状态变化返回值。 |

## ActivityType

PhonePC/2in1Tablet

type ActivityType = 'still' | 'relativeStill'

设备状态类型。

**系统能力**：SystemCapability.Msdp.DeviceStatus.Stationary

| 类型 | 说明 |
| --- | --- |
| 'still' | 绝对静止。 |
| 'relativeStill' | 相对静止。 |

## ActivityEvent

PhonePC/2in1Tablet

设备状态事件。

**系统能力**：SystemCapability.Msdp.DeviceStatus.Stationary

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ENTER | 1 | 进入事件。 |
| EXIT | 2 | 退出事件。 |
| ENTER\_EXIT | 3 | 进入和退出事件。 |

## ActivityState

PhonePC/2in1Tablet

设备状态返回值。

**系统能力**：SystemCapability.Msdp.DeviceStatus.Stationary

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ENTER | 1 | 进入状态。 |
| EXIT | 2 | 退出状态。 |

## stationary.on

PhonePC/2in1Tablet

on(activity: ActivityType, event: ActivityEvent, reportLatencyNs: number, callback: Callback<ActivityResponse>): void

设备状态管理，订阅设备状态服务。

**系统能力**：SystemCapability.Msdp.DeviceStatus.Stationary

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| activity | [ActivityType](js-apis-stationary.md#activitytype) | 是 | 设备状态能力类型。 |
| event | [ActivityEvent](js-apis-stationary.md#activityevent) | 是 | 事件类型。 |
| reportLatencyNs | number | 是 | 报告延时，单位为纳秒（ns）, 取值范围[1000000000-3000000000]。 |
| callback | Callback<[ActivityResponse](js-apis-stationary.md#activityresponse)> | 是 | 回调函数，接收上报状态变化事件。 |

**示例：**

```
1. let reportLatencyNs = 1000000000;
2. stationary.on('still', stationary.ActivityEvent.ENTER, reportLatencyNs, (data) => {
3. console.info('data=' + JSON.stringify(data));
4. })
```

## stationary.once

PhonePC/2in1Tablet

once(activity: ActivityType, callback: Callback<ActivityResponse>): void

设备状态管理，查询设备状态。

**系统能力**：SystemCapability.Msdp.DeviceStatus.Stationary

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| activity | [ActivityType](js-apis-stationary.md#activitytype) | 是 | 设备状态能力类型。 |
| callback | Callback<[ActivityResponse](js-apis-stationary.md#activityresponse)> | 是 | 回调函数，接收上报状态变化事件。 |

**示例：**

```
1. stationary.once('still', (data) => {
2. console.info('data=' + JSON.stringify(data));
3. })
```

## stationary.off

PhonePC/2in1Tablet

off(activity: ActivityType, event: ActivityEvent, callback?: Callback<ActivityResponse>): void

设备状态管理，取消订阅设备状态服务。

**系统能力**：SystemCapability.Msdp.DeviceStatus.Stationary

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| activity | [ActivityType](js-apis-stationary.md#activitytype) | 是 | 设备状态能力类型。 |
| event | [ActivityEvent](js-apis-stationary.md#activityevent) | 是 | 事件类型。 |
| callback | Callback<[ActivityResponse](js-apis-stationary.md#activityresponse)> | 否 | 回调函数，接收上报状态变化事件，如果没有传递callback参数或者传递的类型是undefined，会移除该进程下订阅该类型的所有callback。 |

**示例：**

```
1. stationary.off('still', stationary.ActivityEvent.ENTER);
```
