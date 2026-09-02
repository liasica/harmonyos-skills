---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-awareness-devicestatus
title: "@ohos.multimodalAwareness.deviceStatus (设备状态感知)"
breadcrumb: API参考 > 系统 > 硬件 > Multimodal Awareness Kit（多模态融合感知服务） > ArkTS API > @ohos.multimodalAwareness.deviceStatus (设备状态感知)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ea48fc03d3b42a4bdb5364ee24e2609a8a9f4bed2798465dd0e3070866ff8cd1
---

本模块提供对设备状态的感知能力，通过传感器实时感知设备物理状态，可帮助开发者根据设备物理状态调整应用行为。

**说明** 

本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { deviceStatus } from '@kit.MultimodalAwarenessKit';
```

## SteadyStandingStatus

设备静止姿态感知状态（支架态）。

设备进入支架态指设备静止，且屏幕与水平面角度处于45度-135度。折叠屏手机需处于折叠状态或者完全展开状态。系统通过传感器检测设备的运动状态和角度变化，判断设备是否满足支架态条件。

**系统能力**：SystemCapability.MultimodalAwareness.DeviceStatus

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATUS\_EXIT | 0 | 表示设备退出支架态。 |
| STATUS\_ENTER | 1 | 表示设备进入支架态。 |

## deviceStatus.on('steadyStandingDetect')

on(type: 'steadyStandingDetect', callback: Callback<SteadyStandingStatus>): void

订阅设备静止姿态感知（支架态）事件。建议在不需要时调用off()取消订阅，释放资源。

**系统能力**：SystemCapability.MultimodalAwareness.DeviceStatus

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型。固定传入'steadyStandingDetect'，表示设备静止姿态（支架态）感知。 |
| callback | Callback<[SteadyStandingStatus](js-apis-awareness-devicestatus.md#steadystandingstatus)> | 是 | 回调函数，用于接收设备静止姿态（支架态）状态信息。 |

**错误码**：

以下错误码的详细介绍请参见[设备状态感知错误码](errorcode-devicestatus.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function can not work correctly due to limited device capabilities. |
| 32500001 | Service exception. |
| 32500002 | Subscription failed. |

**示例**：

```ts
try {
   deviceStatus.on('steadyStandingDetect', (data: deviceStatus.SteadyStandingStatus) => {
      console.info(`succeeded to get status, now status = ${JSON.stringify(data)}`);
   });
} catch (err) {
   console.error(`on failed. Code: ${err.code}, message: ${err.message}`);
}
```

## deviceStatus.off('steadyStandingDetect')

off(type: 'steadyStandingDetect', callback?: Callback<SteadyStandingStatus>): void

取消订阅设备静止姿态感知（支架态）事件，用于应用在退出页面或不再需要监听支架态变化的场景。调用后释放相关资源。

**系统能力**：SystemCapability.MultimodalAwareness.DeviceStatus

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型。固定传入'steadyStandingDetect'，表示设备静止姿态（支架态）感知。 |
| callback | Callback<[SteadyStandingStatus](js-apis-awareness-devicestatus.md#steadystandingstatus)> | 否 | 要注销的回调函数，需与订阅时传入的回调函数一致。若不填，则取消当前监听该事件的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[设备状态感知错误码](errorcode-devicestatus.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function can not work correctly due to limited device capabilities. |
| 32500001 | Service exception. |
| 32500003 | Unsubscription failed. |

**示例**：

示例一：取消订阅该客户端订阅设备静止姿态感知（支架态）事件的所有回调。

```ts
try {
   deviceStatus.off('steadyStandingDetect');
} catch (err) {
   console.error(`off failed. Code: ${err.code}, message: ${err.message}`);
}
```

示例二：取消订阅该客户端订阅设备静止姿态感知（支架态）事件的特定回调。

```ts
import { Callback } from '@kit.BasicServicesKit';

// 定义callback变量
let callback : Callback<deviceStatus.SteadyStandingStatus> = (data : deviceStatus.SteadyStandingStatus) => {
   console.info('succeeded to get status, now status = ' + JSON.stringify(data));
};
// 以callback为回调函数，订阅设备静止姿态感知（支架态）事件
try {
   deviceStatus.on('steadyStandingDetect', callback);
} catch (err) {
   console.error(`on failed. Code: ${err.code}, message: ${err.message}`);
}
// 取消该客户端订阅设备静止姿态感知（支架态）事件的特定回调函数
try {
   deviceStatus.off('steadyStandingDetect', callback);
} catch (err) {
   console.error(`off failed. Code: ${err.code}, message: ${err.message}`);
}
```
