---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-awareness-devicestatus
title: @ohos.multimodalAwareness.deviceStatus (设备状态感知)
breadcrumb: API参考 > 系统 > 硬件 > Multimodal Awareness Kit（多模态融合感知服务） > ArkTS API > @ohos.multimodalAwareness.deviceStatus (设备状态感知)
category: harmonyos-references
scraped_at: 2026-04-28T08:10:56+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:0f5fc9ad25e5c055138f0dbe52c8914c8a6de19aad3f14f12bb85c4e1f3ba18e
---

本模块提供对设备状态的感知能力。

说明

本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

Phone

```
1. import { deviceStatus } from '@kit.MultimodalAwarenessKit';
```

## SteadyStandingStatus

Phone

设备静止姿态感知状态（支架态）。

设备进入支架态指设备静止，且屏幕与水平面角度处于45度-135度。折叠屏手机需处于折叠状态或者完全展开状态。

**系统能力**：SystemCapability.MultimodalAwareness.DeviceStatus

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATUS\_EXIT | 0 | 表示设备退出支架态。 |
| STATUS\_ENTER | 1 | 表示设备进入支架态。 |

## deviceStatus.on('steadyStandingDetect')

Phone

on(type: 'steadyStandingDetect', callback: Callback<SteadyStandingStatus>): void

订阅设备静止姿态感知（支架态）事件。

**系统能力**：SystemCapability.MultimodalAwareness.DeviceStatus

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型。type为“steadyStandingDetect”，表示设备静止姿态（支架态）感知。 |
| callback | Callback<[SteadyStandingStatus](js-apis-awareness-devicestatus.md#steadystandingstatus)> | 是 | 回调函数，返回设备静止姿态感知（支架态）状态信息。 |

**错误码**：

以下错误码的详细介绍请参见[设备状态感知错误码](errorcode-devicestatus.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function can not work correctly due to limited device capabilities. |
| 32500001 | Service exception. |
| 32500002 | Subscription failed. |

**示例**：

```
1. try {
2. deviceStatus.on('steadyStandingDetect', (data:deviceStatus.SteadyStandingStatus) => {
3. console.info('succeed to get status, now status = ' + data);
4. });
5. } catch (err) {
6. console.error('on failed, err = ' + err);
7. }
```

## deviceStatus.off('steadyStandingDetect')

Phone

off(type: 'steadyStandingDetect', callback?: Callback<SteadyStandingStatus>): void

取消订阅设备静止姿态感知（支架态）事件。

**系统能力**：SystemCapability.MultimodalAwareness.DeviceStatus

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型。type为“steadyStandingDetect”，表示设备静止姿态（支架态）感知。 |
| callback | Callback<[SteadyStandingStatus](js-apis-awareness-devicestatus.md#steadystandingstatus)> | 否 | 回调函数，返回设备静止姿态感知（支架态）状态信息。 |

**错误码**：

以下错误码的详细介绍请参见[设备状态感知错误码](errorcode-devicestatus.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function can not work correctly due to limited device capabilities. |
| 32500001 | Service exception. |
| 32500003 | Unsubscription failed. |

**示例**：

示例一：取消订阅该客户端订阅设备静止姿态感知（支架态）事件的所有回调。

```
1. try {
2. deviceStatus.off('steadyStandingDetect');
3. } catch (err) {
4. console.error('off failed, err = ' + err);
5. }
```

示例二：取消订阅该客户端订阅设备静止姿态感知（支架态）事件的特定回调。

```
1. // 定义callback变量
2. let callback : Callback<deviceStatus.SteadyStandingStatus> = (data : deviceStatus.SteadyStandingStatus) => {
3. console.info('succeed to get status, now status = ' + data);
4. };
5. // 以callback为回调函数，订阅设备静止姿态感知（支架态）事件
6. try {
7. deviceStatus.on('steadyStandingDetect', callback);
8. } catch (err) {
9. console.error('on failed, err = ' + err);
10. }
11. // 取消该客户端订阅设备静止姿态感知（支架态）事件的特定回调函数
12. try {
13. deviceStatus.off('steadyStandingDetect', callback);
14. } catch (err) {
15. console.error('off failed, err = ' + err);
16. }
```
