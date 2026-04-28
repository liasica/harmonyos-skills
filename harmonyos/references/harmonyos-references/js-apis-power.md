---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-power
title: @ohos.power (系统电源管理)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 设备管理 > @ohos.power (系统电源管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cd70341943f380abd99b3fbacc55949994f951e94ce33153781eab51ba776f06
---

该模块主要提供重启、关机、查询屏幕状态等接口。开发者可以使用该模块的接口获取设备的活动状态、电源模式、亮灭屏状态等。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import {power} from '@kit.BasicServicesKit';
```

## power.isActive9+

PhonePC/2in1TabletTVWearable

isActive(): boolean

检测当前设备是否处于活动状态。

* 有屏的设备亮屏时为活动状态，熄屏时为非活动状态。
* 无屏的设备非休眠时为活动状态，休眠时为非活动状态。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 活动状态返回true，非活动状态返回false。 |

**示例：**

```
1. let isActive = power.isActive();
2. console.info('power is active: ' + isActive);
```

## power.rebootDevice(deprecated)

PhonePC/2in1TabletTVWearable

rebootDevice(reason: string): void

说明

从API version 7开始支持，从API version 9开始不再维护，替代接口能力仅对系统应用开放。

重启设备。

**需要权限：** ohos.permission.REBOOT,该权限仅系统应用可申请。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reason | string | 是 | 重启原因。 |

**示例：**

```
1. power.rebootDevice('reboot_test');
```

## power.getPowerMode9+

PhonePC/2in1TabletTVWearable

getPowerMode(): DevicePowerMode

获取当前设备的电源模式。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DevicePowerMode](js-apis-power.md#devicepowermode9) | 电源模式。 |

**示例：**

```
1. let mode = power.getPowerMode();
2. console.info('power mode: ' + mode);
```

## power.isStandby10+

PhonePC/2in1TabletTVWearable

isStandby(): boolean

检测当前设备是否进入待机低功耗续航模式。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 进入待机模式返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[系统电源管理错误码](errorcode-power.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 4900101 | Failed to connect to the service. |

**示例：**

```
1. try {
2. let isStandby = power.isStandby();
3. console.info('device is in standby: ' + isStandby);
4. } catch(err) {
5. console.error('check isStandby failed, err: ' + err);
6. }
```

## power.isScreenOn(deprecated)

PhonePC/2in1TabletTVWearable

isScreenOn(callback: AsyncCallback<boolean>): void

说明

从API version 7开始支持，从API version 9开始不再维护，建议使用[power.isActive](js-apis-power.md#powerisactive9)替代。

检测当前设备的亮灭屏状态。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当检测成功，err为undefined，data为获取到的亮灭屏状态，返回true表示亮屏，返回false表示灭屏；否则为错误对象。 |

**示例：**

```
1. power.isScreenOn((err: Error, data: boolean) => {
2. if (typeof err === 'undefined') {
3. console.info('screen on status is ' + data);
4. } else {
5. console.error('check screen status failed, err: ' + err);
6. }
7. })
```

## power.isScreenOn(deprecated)

PhonePC/2in1TabletTVWearable

isScreenOn(): Promise<boolean>

说明

从API version 7开始支持，从API version 9开始不再维护，建议使用[power.isActive](js-apis-power.md#powerisactive9)替代。

检测当前设备的亮灭屏状态。使用Promise异步回调。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示亮屏；返回false表示灭屏。 |

**示例：**

```
1. power.isScreenOn()
2. .then((data: boolean) => {
3. console.info('screen on status is ' + data);
4. })
5. .catch((err: Error) => {
6. console.error('check screen status failed, err: ' + err);
7. })
```

## DevicePowerMode9+

PhonePC/2in1TabletTVWearable

表示电源模式的枚举值。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MODE\_NORMAL | 600 | 表示标准模式，默认值。 |
| MODE\_POWER\_SAVE | 601 | 表示省电模式。 |
| MODE\_PERFORMANCE | 602 | 表示性能模式。 |
| MODE\_EXTREME\_POWER\_SAVE | 603 | 表示超级省电模式。 |
| MODE\_CUSTOM\_POWER\_SAVE20+ | 650 | 表示自定义省电模式。 |

## PowerKeyFilteringStrategy21+

PhonePC/2in1TabletTVWearable

表示电源键过滤策略。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DISABLE\_LONG\_PRESS\_FILTERING | 0 | 表示不使能电源键过滤策略，默认值。 |
| LONG\_PRESS\_FILTERING\_ONCE | 1 | 表示仅过滤当前电源键长按事件，下一次不过滤。 |
