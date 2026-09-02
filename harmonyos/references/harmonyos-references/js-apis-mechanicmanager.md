---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mechanicmanager
title: "@ohos.distributedHardware.mechanicManager (机械体控制模块)"
breadcrumb: API参考 > 系统 > 硬件 > Mechanic Kit（机械设备管理服务） > ArkTS API > @ohos.distributedHardware.mechanicManager (机械体控制模块)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5076e28462d3971522aff8290e6aa6ad1d4fe4026b20c4378c6adbecadb9343e
---

本模块提供与机械体设备交互的能力，包括设备连接状态监听、跟踪控制和跟踪状态监听功能。

**说明** 

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```js
import { mechanicManager } from '@kit.MechanicKit';
```

## mechanicManager.on('attachStateChange')

on(type: 'attachStateChange', callback: Callback<AttachStateChangeInfo>): void

注册连接状态变化事件的回调监听，等待连接状态变化。使用callback异步回调。

**系统能力**：SystemCapability.Mechanic.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'attachStateChange' | 是 | 注册监听事件的类型。取值为：'attachStateChange'。 |
| callback | Callback<[AttachStateChangeInfo](js-apis-mechanicmanager.md#attachstatechangeinfo)> | 是 | 回调函数，返回机械体设备连接变化信息。 |

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](errorcode-mechanic.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 33300001 | Service exception. |

**示例：**

```ts
// 定义连接状态变化回调函数，result为设备连接状态变化信息
let callback = (result: mechanicManager.AttachStateChangeInfo) => {
  console.info(`'callback result:' ${result}`);
};

// 打印日志，表示开始注册监听
console.info('Register');
// 注册"attachStateChange"事件监听，当设备连接状态变化时触发callback回调
mechanicManager.on("attachStateChange", callback);
// 打印日志，表示注册监听成功
console.info('Succeeded in registering callback.');
```

## mechanicManager.off('attachStateChange')

off(type: 'attachStateChange', callback?: Callback<AttachStateChangeInfo>): void

取消注册连接状态变化事件的回调监听。使用callback异步回调。

**系统能力**：SystemCapability.Mechanic.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'attachStateChange' | 是 | 取消注册监听事件的类型。取值为：'attachStateChange'。 |
| callback | Callback<[AttachStateChangeInfo](js-apis-mechanicmanager.md#attachstatechangeinfo)> | 否 | 回调函数，返回机械体设备连接变化信息。 |

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](errorcode-mechanic.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 33300001 | Service exception. |

**示例：**

```ts
// 定义连接状态变化回调函数
let callback = (result: mechanicManager.AttachStateChangeInfo) => {
  console.info(`'callback result:' ${result}`);
};

console.info('Unregister');
// 取消注册"attachStateChange"事件监听
mechanicManager.off("attachStateChange", callback);
console.info('Succeeded in unregistering callback.');
```

## mechanicManager.getAttachedMechDevices

getAttachedMechDevices(): MechInfo[]

获取已连接的机械体设备列表。

**系统能力**：SystemCapability.Mechanic.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MechInfo](js-apis-mechanicmanager.md#mechinfo)[] | 已连接机械体设备的列表。 |

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](errorcode-mechanic.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 33300001 | Service exception. |

**示例：**

```ts
console.info('Query device list');
// 调用getAttachedMechDevices方法获取已连接的机械体设备列表
let mechanicInfos = mechanicManager.getAttachedMechDevices();
console.info(`'device list:' ${mechanicInfos}`);
```

## mechanicManager.setCameraTrackingEnabled

setCameraTrackingEnabled(isEnabled: boolean): void

启用或禁用当前机械体设备摄像头跟踪。

**系统能力**：SystemCapability.Mechanic.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | boolean | 是 | 是否启用摄像头跟踪， true表示启用摄像头跟踪，false表示禁用摄像头跟踪。 |

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](errorcode-mechanic.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 33300001 | Service exception. |
| 33300002 | Device not connected. |
| 33300003 | Feature not supported. |

**示例：**

```ts
console.info('Enable tracing');
// 调用setCameraTrackingEnabled方法，参数true表示启用摄像头跟踪
mechanicManager.setCameraTrackingEnabled(true);
console.info('Succeeded in enabling tracking.');
```

## mechanicManager.getCameraTrackingEnabled

getCameraTrackingEnabled(): boolean

检查当前机械体设备是否启用了摄像头跟踪。

**系统能力**：SystemCapability.Mechanic.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 摄像头跟踪启用状态，true表示已启用，false表示已禁用。 |

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](errorcode-mechanic.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 33300001 | Service exception. |
| 33300002 | Device not connected. |

**示例：**

```ts
console.info('Get tracking status');
// 调用getCameraTrackingEnabled方法获取当前摄像头跟踪是否启用
let enabled = mechanicManager.getCameraTrackingEnabled();
console.info(`'current tracking status:' ${enabled}`);
```

## mechanicManager.on('trackingStateChange')

on(type: 'trackingStateChange', callback: Callback<TrackingEventInfo>): void

注册跟踪状态变化事件的回调监听。使用callback异步回调。

**系统能力**：SystemCapability.Mechanic.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'trackingStateChange' | 是 | 注册监听事件的类型。取值为：'trackingStateChange'。 |
| callback | Callback<[TrackingEventInfo](js-apis-mechanicmanager.md#trackingeventinfo)> | 是 | 回调函数，返回跟踪事件信息。 |

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](errorcode-mechanic.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 33300001 | Service exception. |

**示例：**

```ts
// 定义跟踪状态变化回调函数，result为跟踪事件信息
let callback = (result: mechanicManager.TrackingEventInfo) => {
  console.info(`'callback result:' ${result}`);
};

console.info('Register');
// 注册"trackingStateChange"事件监听，当跟踪状态变化时触发callback回调
mechanicManager.on("trackingStateChange", callback);
console.info('Succeeded in registering callback.');
```

## mechanicManager.off('trackingStateChange')

off(type: 'trackingStateChange', callback?: Callback<TrackingEventInfo>): void

取消注册跟踪状态变化事件的回调监听。使用callback异步回调。

**系统能力**：SystemCapability.Mechanic.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'trackingStateChange' | 是 | 取消注册的监听事件类型。取值为：'trackingStateChange'。 |
| callback | Callback<[TrackingEventInfo](js-apis-mechanicmanager.md#trackingeventinfo)> | 否 | 回调函数，返回跟踪事件信息。 |

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](errorcode-mechanic.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 33300001 | Service exception. |

**示例：**

```ts
// 定义跟踪状态变化回调函数
let callback = (result: mechanicManager.TrackingEventInfo) => {
  console.info(`'callback result:' ${result}`);
};

console.info('Unregister');
// 取消注册"trackingStateChange"事件监听
mechanicManager.off("trackingStateChange", callback);
console.info('Succeeded in unregistering callback.');
```

## mechanicManager.getCameraTrackingLayout

getCameraTrackingLayout(): CameraTrackingLayout

获取当前机械体设备摄像头跟踪布局。

**系统能力**：SystemCapability.Mechanic.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraTrackingLayout](js-apis-mechanicmanager.md#cameratrackinglayout) | 获取到的当前机械体设备摄像头跟踪布局。 |

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](errorcode-mechanic.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 33300001 | Service exception. |
| 33300002 | Device not connected. |

**示例：**

```ts
console.info('Query layout');
// 调用getCameraTrackingLayout方法获取当前摄像头跟踪布局
let layout = mechanicManager.getCameraTrackingLayout();
console.info(`'Succeeded in querying layout, current layout:' ${layout}`);
```

## mechanicManager.isControlSupported()

isControlSupported(mechDeviceType?: MechDeviceType): boolean

应用判断当前设备是否支持对特定设备类型的机械体设备控制，以便作出相应的功能选择，例如决定使用APP内部的跟踪控制功能还是系统的默认控制功能，或者给予用户相应的提示。三方厂商APP可以根据此接口判断当前设备是否支持对特定类型的设备的机械控制和智能跟踪功能，以决定是否使用自身APP的跟踪控制功能，还是直接使用系统提供的跟踪功能，或者给予用户相应的提示。

**起始版本：** 26.0.0

**系统能力**：SystemCapability.Mechanic.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mechDeviceType | [MechDeviceType](js-apis-mechanicmanager.md#mechdevicetype) | 否 | 机械体设备的类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前设备是否支持某类设备的机械体设备控制。true表示支持，false表示不支持。 |

**示例：**

```ts
console.info('Check whether control is supported');
// 调用isControlSupported方法，传入MechDeviceType.GIMBAL_DEVICE类型，判断是否支持云台设备控制
let isSupported = mechanicManager.isControlSupported(mechanicManager.MechDeviceType.GIMBAL_DEVICE);
console.info(`isSupported: ${isSupported}`);
```

## MechInfo

机械体设备信息。

**系统能力**：SystemCapability.Mechanic.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mechId | number | 否 | 否 | 机械体设备ID，取值为大于等于0的整数。 |
| mechDeviceType | [MechDeviceType](js-apis-mechanicmanager.md#mechdevicetype) | 否 | 否 | 机械体设备的类型。 |
| mechName | string | 否 | 否 | 机械体设备名称，长度不超过64字符。 |

## TrackingEventInfo

跟踪事件信息。

**系统能力**：SystemCapability.Mechanic.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| event | [TrackingEvent](js-apis-mechanicmanager.md#trackingevent) | 否 | 否 | 跟踪事件。 |

## AttachStateChangeInfo

设备连接状态变化的信息。

**系统能力**：SystemCapability.Mechanic.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | [AttachState](js-apis-mechanicmanager.md#attachstate) | 否 | 否 | 设备连接状态。 |
| mechInfo | [MechInfo](js-apis-mechanicmanager.md#mechinfo) | 否 | 否 | 机械体设备信息。 |

## TrackingEvent

跟踪事件的枚举。

**系统能力**：SystemCapability.Mechanic.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CAMERA\_TRACKING\_USER\_ENABLED | 0 | 用户启用了摄像头跟踪。 |
| CAMERA\_TRACKING\_USER\_DISABLED | 1 | 用户禁用了摄像头跟踪。 |
| CAMERA\_TRACKING\_LAYOUT\_CHANGED | 2 | 摄像头跟踪构图变更。 |

## MechDeviceType

机械体设备类型的枚举。

**系统能力**：SystemCapability.Mechanic.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GIMBAL\_DEVICE | 0 | 便携式云台设备。 |

## AttachState

设备连接状态的枚举。

**系统能力**：SystemCapability.Mechanic.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ATTACHED | 0 | 设备已连接。 |
| DETACHED | 1 | 设备已断开。 |

## CameraTrackingLayout

摄像头跟踪布局的枚举。

**系统能力**：SystemCapability.Mechanic.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 系统默认跟踪布局。 |
| LEFT | 1 | 靠左布局。 |
| MIDDLE | 2 | 居中布局。 |
| RIGHT | 3 | 靠右布局。 |
