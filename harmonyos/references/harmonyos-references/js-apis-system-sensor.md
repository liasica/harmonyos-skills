---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-sensor
title: @system.sensor (传感器)
breadcrumb: API参考 > 系统 > 硬件 > Sensor Service Kit（传感器服务） > ArkTS API > @system.sensor (传感器)
category: harmonyos-references
scraped_at: 2026-04-28T08:11:03+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:353d0ec0a077ca1d20ac2d73ae3c43991c118004b66ebb7b2398bb575c2571fc
---

sensor模块提供订阅传感器数据基本能力，主要包含查询传感器的列表、订阅/取消传感器的数据、执行控制命令等。

根据传感器的用途，可以将传感器分为六大类：运动类传感器、环境类传感器、方向类传感器、光线类传感器、健康类传感器、其他类传感器（如霍尔传感器），每一大类传感器包含不同类型的传感器，某种类型的传感器可能是单一的物理传感器，也可能是由多个物理传感器复合而成。

说明

* 模块维护策略：
  + 对于Lite Wearable设备类型，该模块长期维护，正常使用。
  + 对于支持该模块的其他设备类型，该模块从API version 8开始不再维护，推荐使用新接口[@ohos.sensor](js-apis-sensor.md)。
* 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 该功能使用需要对应硬件支持，仅支持真机调试。

## 导入模块

WearableLite Wearable

```
1. import { Sensor } from '@kit.SensorServiceKit';
```

## Sensor.subscribeAccelerometer

WearableLite Wearable

subscribeAccelerometer(options: subscribeAccelerometerOptions): void

观察加速度数据变化。针对同一个应用，多次点击调用时，会覆盖前面的调用效果，即仅最后一次调用生效。

除Lite Wearable外，从API Version8开始，推荐使用[ACCELEROMETER](js-apis-sensor.md#accelerometer9)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**需要权限**：ohos.permission.ACCELEROMETER，该权限为系统权限

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [subscribeAccelerometerOptions](js-apis-system-sensor.md#subscribeaccelerometeroptions) | 是 | 监听加速度传感器数据的回调函数的执行频率。 |

**示例**：

```
1. import { Sensor, AccelerometerResponse, subscribeAccelerometerOptions } from '@kit.SensorServiceKit';

3. let accelerometerOptions: subscribeAccelerometerOptions = {
4. interval: 'normal',
5. success: (ret: AccelerometerResponse) => {
6. console.info('Succeeded in subscribing. X-axis data: ' + ret.x);
7. console.info('Succeeded in subscribing. Y-axis data: ' + ret.y);
8. console.info('Succeeded in subscribing. Z-axis data: ' + ret.z);
9. },
10. fail: (data: string, code: number) => {
11. console.error(`Failed to subscribe. Code: ${code}, data: ${data}`);
12. },
13. };
14. Sensor.subscribeAccelerometer(accelerometerOptions);
```

说明

建议在页面销毁时，即onDestroy回调中，取消数据订阅，避免不必要的性能开销。

## Sensor.unsubscribeAccelerometer

WearableLite Wearable

unsubscribeAccelerometer(): void

取消订阅加速度数据。

除Lite Wearable外，从API Version8开始，推荐使用[ACCELEROMETER](js-apis-sensor.md#accelerometerdeprecated-2)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**需要权限**：ohos.permission.ACCELEROMETER，该权限为系统权限

**示例**：

```
1. Sensor.unsubscribeAccelerometer();
```

## Sensor.subscribeCompass

WearableLite Wearable

subscribeCompass(options: SubscribeCompassOptions): void

订阅罗盘数据变化。针对同一个应用，多次点击调用时，会覆盖前面的调用效果，即仅最后一次调用生效。

除Lite Wearable外，从API Version8开始，推荐使用[ORIENTATION](js-apis-sensor.md#orientationdeprecated)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeCompassOptions](js-apis-system-sensor.md#subscribecompassoptions) | 是 | 当罗盘传感器数据发生变化时调用。 |

**示例**：

```
1. import { Sensor, CompassResponse, SubscribeCompassOptions } from '@kit.SensorServiceKit';

3. let subscribeCompassOptions: SubscribeCompassOptions = {
4. success: (ret: CompassResponse) => {
5. console.info('Succeeded in subscribing. Get data direction:' + ret.direction);
6. },
7. fail: (data: string, code: number) => {
8. console.error(`Failed to subscribe. Code: ${code}, data: ${data}`);
9. },
10. };
11. Sensor.subscribeCompass(subscribeCompassOptions);
```

说明

建议在页面销毁时，即onDestroy回调中，取消数据订阅，避免不必要的性能开销。

## Sensor.unsubscribeCompass

WearableLite Wearable

unsubscribeCompass(): void

取消订阅罗盘。

除Lite Wearable外，从API Version8开始，推荐使用[ORIENTATION](js-apis-sensor.md#orientationdeprecated-2)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**示例**：

```
1. Sensor.unsubscribeCompass();
```

## Sensor.subscribeProximity

WearableLite Wearable

subscribeProximity(options: SubscribeProximityOptions): void

订阅距离感应数据变化。针对同一个应用，多次点击调用时，会覆盖前面的调用效果，即仅最后一次调用生效。

除Lite Wearable外，从API Version8开始，推荐使用[PROXIMITY](js-apis-sensor.md#proximitydeprecated)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeProximityOptions](js-apis-system-sensor.md#subscribeproximityoptions) | 是 | 当距离传感器数据发生变化时调用。 |

**示例**：

```
1. import { Sensor, ProximityResponse, SubscribeProximityOptions } from '@kit.SensorServiceKit';

3. let subscribeProximityOptions: SubscribeProximityOptions = {
4. success: (ret: ProximityResponse) => {
5. console.info('Succeeded in subscribing. Get data distance:' + ret.distance);
6. },
7. fail: (data: string, code: number) => {
8. console.error(`Failed to subscribe. Code: ${code}, data: ${data}`);
9. },
10. };
11. Sensor.subscribeProximity(subscribeProximityOptions);
```

说明

建议在页面销毁时，即onDestroy回调中，取消数据订阅，避免不必要的性能开销。

## Sensor.unsubscribeProximity

WearableLite Wearable

unsubscribeProximity(): void

取消订阅距离感应。

除Lite Wearable外，从API Version8开始，推荐使用[PROXIMITY](js-apis-sensor.md#proximitydeprecated-2)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。

**示例**：

```
1. Sensor.unsubscribeProximity();
```

## Sensor.subscribeLight

WearableLite Wearable

subscribeLight(options: SubscribeLightOptions): void

订阅环境光线感应数据变化。再次调用时，会覆盖前一次调用效果，即仅最后一次调用生效。

除Lite Wearable外，从API Version8开始，推荐使用[AMBIENT\_LIGHT](js-apis-sensor.md#ambient_lightdeprecated)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeLightOptions](js-apis-system-sensor.md#subscribelightoptions) | 是 | 当环境光传感器数据发生变化时调用。 |

**示例**：

```
1. import { Sensor, LightResponse, SubscribeLightOptions } from '@kit.SensorServiceKit';

3. let subscribeLightOptions: SubscribeLightOptions = {
4. success: (ret: LightResponse) => {
5. console.info('Succeeded in subscribing. Get data intensity:' + ret.intensity);
6. },
7. fail: (data: string, code: number) => {
8. console.error(`Failed to subscribe. Code: ${code}, data: ${data}`);
9. },
10. };
11. Sensor.subscribeLight(subscribeLightOptions);
```

说明

建议在页面销毁时，即onDestroy回调中，取消数据订阅，避免不必要的性能开销。

## Sensor.unsubscribeLight

WearableLite Wearable

unsubscribeLight(): void

取消订阅环境光线感应。

除Lite Wearable外，从API Version8开始，推荐使用[AMBIENT\_LIGHT](js-apis-sensor.md#ambient_lightdeprecated-2)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。

**示例**：

```
1. Sensor.unsubscribeLight();
```

## Sensor.subscribeStepCounter

WearableLite Wearable

subscribeStepCounter(options: SubscribeStepCounterOptions): void

订阅计步传感器数据变化。针对同一个应用，多次点击调用时，会覆盖前面的调用效果，即仅最后一次调用生效。

除Lite Wearable外，从API Version8开始，推荐使用[PEDOMETER](js-apis-sensor.md#pedometerdeprecated)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeStepCounterOptions](js-apis-system-sensor.md#subscribestepcounteroptions) | 是 | 当步进计数器传感器数据发生变化时调用。 |

**示例**：

```
1. import { Sensor, StepCounterResponse, SubscribeStepCounterOptions } from '@kit.SensorServiceKit';

3. let subscribeStepCounterOptions: SubscribeStepCounterOptions = {
4. success: (ret: StepCounterResponse) => {
5. console.info('Succeeded in subscribing. Get step value:' + ret.steps);
6. },
7. fail: (data: string, code: number) => {
8. console.error(`Failed to subscribe. Code: ${code}, data: ${data}`);
9. },
10. };
11. Sensor.subscribeStepCounter(subscribeStepCounterOptions);
```

说明

建议在页面销毁时，即onDestroy回调中，取消数据订阅，避免不必要的性能开销。

## Sensor.unsubscribeStepCounter

WearableLite Wearable

unsubscribeStepCounter(): void

取消订阅计步传感器。

除Lite Wearable外，从API Version8开始，推荐使用[PEDOMETER](js-apis-sensor.md#pedometerdeprecated-2)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**示例**：

```
1. Sensor.unsubscribeStepCounter();
```

## Sensor.subscribeBarometer

WearableLite Wearable

subscribeBarometer(options: SubscribeBarometerOptions): void

订阅气压计传感器数据变化。针对同一个应用，多次点击调用时，会覆盖前面的调用效果，即仅最后一次调用生效。

除Lite Wearable外，从API Version8开始，推荐使用[BAROMETER](js-apis-sensor.md#barometerdeprecated-1)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeBarometerOptions](js-apis-system-sensor.md#subscribebarometeroptions) | 是 | 当气压计传感器数据发生变化时调用。 |

**示例**：

```
1. import { Sensor, BarometerResponse, SubscribeBarometerOptions } from '@kit.SensorServiceKit';

3. let subscribeBarometerOptions: SubscribeBarometerOptions = {
4. success: (ret: BarometerResponse) => {
5. console.info('Succeeded in subscribing. Get data value:' + ret.pressure);
6. },
7. fail: (data: string, code: number) => {
8. console.error(`Failed to subscribe. Code: ${code}, data: ${data}`);
9. },
10. };
11. Sensor.subscribeBarometer(subscribeBarometerOptions);
```

说明

建议在页面销毁时，即onDestroy回调中，取消数据订阅，避免不必要的性能开销。

## Sensor.unsubscribeBarometer

WearableLite Wearable

unsubscribeBarometer(): void

取消订阅气压计传感器。

除Lite Wearable外，从API Version8开始，推荐使用[BAROMETER](js-apis-sensor.md#barometerdeprecated-2)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**示例**：

```
1. Sensor.unsubscribeBarometer();
```

## Sensor.subscribeHeartRate

WearableLite Wearable

subscribeHeartRate(options: SubscribeHeartRateOptions): void

订阅心率传感器数据变化。针对同一个应用，多次点击调用时，会覆盖前面的调用效果，即仅最后一次调用生效。

除Lite Wearable外，从API Version8开始，推荐使用[HEART\_RATE](js-apis-sensor.md#heart_ratedeprecated)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**需要权限**：ohos.permission.READ\_HEALTH\_DATA

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeHeartRateOptions](js-apis-system-sensor.md#subscribeheartrateoptions) | 是 | 当心率传感器数据发生变化时调用。 |

**示例**：

```
1. import { Sensor, HeartRateResponse, SubscribeHeartRateOptions } from '@kit.SensorServiceKit';

3. let subscribeHeartRateOptions: SubscribeHeartRateOptions = {
4. success: (ret: HeartRateResponse) => {
5. console.info('Succeeded in subscribing. Get heartRate value:' + ret.heartRate);
6. },
7. fail: (data: string, code: number) => {
8. console.error(`Failed to subscribe. Code: ${code}, data: ${data}`);
9. },
10. };
11. Sensor.subscribeHeartRate(subscribeHeartRateOptions);
```

说明

建议在页面销毁时，即onDestroy回调中，取消数据订阅，避免不必要的性能开销。

## Sensor.unsubscribeHeartRate

WearableLite Wearable

unsubscribeHeartRate(): void

取消订阅心率传感器。

除Lite Wearable外，从API Version8开始，推荐使用[HEART\_RATE](js-apis-sensor.md#heart_ratedeprecated-2)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**需要权限**：ohos.permission.READ\_HEALTH\_DATA

**示例**：

```
1. Sensor.unsubscribeHeartRate();
```

## Sensor.subscribeOnBodyState

WearableLite Wearable

subscribeOnBodyState(options: SubscribeOnBodyStateOptions): void

订阅设备佩戴状态。针对同一个应用，多次点击调用时，会覆盖前面的调用效果，即仅最后一次调用生效。

除Lite Wearable外，从API Version8开始，推荐使用[WEAR\_DETECTION](js-apis-sensor.md#wear_detectiondeprecated)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeOnBodyStateOptions](js-apis-system-sensor.md#subscribeonbodystateoptions) | 是 | 当穿着状态改变时调用。 |

**示例**：

```
1. import { Sensor, OnBodyStateResponse, SubscribeOnBodyStateOptions } from '@kit.SensorServiceKit';

3. let subscribeOnBodyStateOptions: SubscribeOnBodyStateOptions = {
4. success: (ret: OnBodyStateResponse) => {
5. console.info('Succeeded in subscribing. Get on-body state value:' + ret.value);
6. },
7. fail: (data: string, code: number) => {
8. console.error(`Failed to subscribe. Code: ${code}, data: ${data}`);
9. },
10. };
11. Sensor.subscribeOnBodyState(subscribeOnBodyStateOptions);
```

说明

建议在页面销毁时，即onDestroy回调中，取消数据订阅，避免不必要的性能开销。

## Sensor.unsubscribeOnBodyState

WearableLite Wearable

unsubscribeOnBodyState(): void

取消订阅设备佩戴状态。

除Lite Wearable外，从API Version8开始，推荐使用[WEAR\_DETECTION](js-apis-sensor.md#wear_detectiondeprecated-2)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**示例**：

```
1. Sensor.unsubscribeOnBodyState();
```

## Sensor.getOnBodyState

WearableLite Wearable

getOnBodyState(options: GetOnBodyStateOptions): void

获取设备佩戴状态。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [GetOnBodyStateOptions](js-apis-system-sensor.md#getonbodystateoptions) | 是 | 获取传感器所在设备穿戴状态时调用。 |

**示例**：

```
1. import { Sensor, OnBodyStateResponse, GetOnBodyStateOptions } from '@kit.SensorServiceKit';

3. let getOnBodyStateOptions: GetOnBodyStateOptions = {
4. success: (ret: OnBodyStateResponse) => {
5. console.info('Succeeded in subscribing. On body state: ' + ret.value);
6. },
7. fail: (data: string, code: number) => {
8. console.error(`Failed to subscribe. Code: ${code}, data: ${data}`);
9. },
10. };
11. Sensor.getOnBodyState(getOnBodyStateOptions);
```

## Sensor.subscribeDeviceOrientation6+

WearableLite Wearable

subscribeDeviceOrientation(options: SubscribeDeviceOrientationOptions): void

观察设备方向传感器数据变化。

针对同一个应用，多次点击调用时，会覆盖前面的调用效果，即仅最后一次调用生效；针对同一个方法内，不支持多次调用。

除Lite Wearable外，从API Version8开始，推荐使用[ORIENTATION](js-apis-sensor.md#orientationdeprecated)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeDeviceOrientationOptions](js-apis-system-sensor.md#subscribedeviceorientationoptions6) | 是 | 用于监听设备方向传感器数据的回调函数的执行频率。 |

**示例**：

```
1. import { Sensor, DeviceOrientationResponse, SubscribeDeviceOrientationOptions } from '@kit.SensorServiceKit';

3. let subscribeDeviceOrientationOptions: SubscribeDeviceOrientationOptions = {
4. interval: 'normal',
5. success: (ret: DeviceOrientationResponse) => {
6. console.info('Succeeded in subscribing. Alpha data: ' + ret.alpha);
7. console.info('Succeeded in subscribing. Beta data: ' + ret.beta);
8. console.info('Succeeded in subscribing. Gamma data: ' + ret.gamma);
9. },
10. fail: (data: string, code: number) => {
11. console.error(`Failed to subscribe. Code: ${code}, data: ${data}`);
12. }
13. };
14. Sensor.subscribeDeviceOrientation(subscribeDeviceOrientationOptions);
```

说明

建议在页面销毁时，即onDestroy回调中，取消数据订阅，避免不必要的性能开销。

## Sensor.unsubscribeDeviceOrientation6+

WearableLite Wearable

unsubscribeDeviceOrientation(): void

取消订阅设备方向传感器数据。

除Lite Wearable外，从API Version8开始，推荐使用[ORIENTATION](js-apis-sensor.md#orientationdeprecated-2)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。

**示例**：

```
1. Sensor.unsubscribeDeviceOrientation();
```

## Sensor.subscribeGyroscope6+

WearableLite Wearable

subscribeGyroscope(options: SubscribeGyroscopeOptions): void

观察陀螺仪传感器数据变化。

针对同一个应用，多次点击调用时，会覆盖前面的调用效果，即仅最后一次调用生效；针对同一个方法内，不支持多次调用。

除Lite Wearable外，从API Version8开始，推荐使用[GYROSCOPE](js-apis-sensor.md#gyroscopedeprecated)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**需要权限**：ohos.permission.GYROSCOPE，该权限为系统权限

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeGyroscopeOptions](js-apis-system-sensor.md#subscribegyroscopeoptions6) | 是 | 用于侦听陀螺仪传感器数据的回调函数的执行频率。 |

**示例**：

```
1. import { Sensor, GyroscopeResponse, SubscribeGyroscopeOptions } from '@kit.SensorServiceKit';

3. let subscribeGyroscopeOptions: SubscribeGyroscopeOptions = {
4. interval: 'normal',
5. success: (ret: GyroscopeResponse) => {
6. console.info('Succeeded in subscribing. X-axis data: ' + ret.x);
7. console.info('Succeeded in subscribing. Y-axis data: ' + ret.y);
8. console.info('Succeeded in subscribing. Z-axis data: ' + ret.z);
9. },
10. fail: (data: string, code: number) => {
11. console.error(`Failed to subscribe. Code: ${code}, data: ${data}`);
12. }
13. };
14. Sensor.subscribeGyroscope(subscribeGyroscopeOptions);
```

说明

建议在页面销毁时，即onDestroy回调中，取消数据订阅，避免不必要的性能开销。

## Sensor.unsubscribeGyroscope6+

WearableLite Wearable

unsubscribeGyroscope(): void

取消订阅陀螺仪传感器数据。

除Lite Wearable外，从API Version8开始，推荐使用[GYROSCOPE](js-apis-sensor.md#gyroscopedeprecated-2)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**需要权限**：ohos.permission.GYROSCOPE，该权限为系统权限

**示例**：

```
1. Sensor.unsubscribeGyroscope();
```

## subscribeAccelerometerOptions

WearableLite Wearable

用于监听加速度传感器数据的回调函数的执行频率。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**需要权限**：ohos.permission.ACCELEROMETER

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| interval | string | 是 | 频率参数，加速度的回调函数执行频率。  默认为normal，可选值有：  game：极高的回调频率，20ms/次，适用于游戏。  ui：较高的回调频率，60ms/次，适用于UI更新。  normal：普通的回调频率，200ms/次，低功耗。 |
| success | [AccelerometerResponse](js-apis-system-sensor.md#accelerometerresponse) | 是 | 感应到加速度数据变化后的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |

## AccelerometerResponse

WearableLite Wearable

感应到加速度数据变化后的回调函数。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**需要权限**：ohos.permission.ACCELEROMETER

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | x轴的加速度。 |
| y | number | 是 | y轴的加速度。 |
| z | number | 是 | z轴的加速度。 |

## SubscribeCompassOptions

WearableLite Wearable

当罗盘传感器数据发生变化时调用。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | [CompassResponse](js-apis-system-sensor.md#compassresponse) | 是 | 罗盘数据改变后触发的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |

## CompassResponse

WearableLite Wearable

罗盘数据改变后触发的回调函数。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| direction | number | 是 | 设备面对的方向度数。 |

## SubscribeProximityOptions

WearableLite Wearable

当距离传感器数据发生变化时调用。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | [ProximityResponse](js-apis-system-sensor.md#proximityresponse) | 是 | 距离感应数据改变后调用的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |

## ProximityResponse

WearableLite Wearable

距离感应数据改变后调用的回调函数。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| distance | number | 是 | 可见物体相对于设备显示屏的接近或远离状态。 |

## SubscribeLightOptions

WearableLite Wearable

当环境光传感器数据发生变化时调用。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | [LightResponse](js-apis-system-sensor.md#lightresponse) | 是 | 光线感应数据改变后的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |

## LightResponse

WearableLite Wearable

光线感应数据改变后的回调函数。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| intensity | number | 是 | 光线强度，单位为lux。 |

## SubscribeStepCounterOptions

WearableLite Wearable

当步进计数器传感器数据发生变化时调用。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | [StepCounterResponse](js-apis-system-sensor.md#stepcounterresponse) | 是 | 计步传感器数据改变后的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |

## StepCounterResponse

WearableLite Wearable

计步传感器数据改变后的回调函数。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| steps | number | 是 | 计步传感器重启后累计记录的步数。 |

## SubscribeBarometerOptions

WearableLite Wearable

当气压计传感器数据发生变化时调用。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | [BarometerResponse](js-apis-system-sensor.md#barometerresponse) | 是 | 气压计传感器数据改变后的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |

## BarometerResponse

WearableLite Wearable

气压计传感器数据改变后的回调函数。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pressure | number | 是 | 气压值，单位：帕斯卡。 |

## SubscribeHeartRateOptions

WearableLite Wearable

当心率传感器数据发生变化时调用。

**需要权限**：ohos.permission.READ\_HEALTH\_DATA

**系统能力**：SystemCapability.Sensors.Sensor.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | [HeartRateResponse](js-apis-system-sensor.md#heartrateresponse) | 是 | 心率传感器数据改变后的回调函数，默认频率5s/次。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |

## HeartRateResponse

WearableLite Wearable

心率传感器数据改变后的回调函数，默认频率5s/次。

**需要权限**：ohos.permission.READ\_HEALTH\_DATA

**系统能力**：SystemCapability.Sensors.Sensor.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| heartRate | number | 是 | 心率值。 |

## SubscribeOnBodyStateOptions

WearableLite Wearable

当传感器所在设备穿戴状态改变时调用，分为已穿戴和未穿戴。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | [OnBodyStateResponse](js-apis-system-sensor.md#onbodystateresponse) | 是 | 传感器所在设备穿戴状态改变后的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |

## OnBodyStateResponse

WearableLite Wearable

传感器所在设备是否穿戴。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否已佩戴设备，当返回true表示已佩戴，否则未佩戴。 |

## GetOnBodyStateOptions

WearableLite Wearable

获取传感器所在设备穿戴状态时调用。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | [OnBodyStateResponse](js-apis-system-sensor.md#onbodystateresponse) | 是 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

## SubscribeDeviceOrientationOptions6+

WearableLite Wearable

用于监听设备方向传感器数据的回调函数的执行频率。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| interval | string | 是 | 频率参数，设备方向传感器的回调函数执行频率。  默认为normal，可选值有：  - game：极高的回调频率，20ms/次，适用于游戏。  - ui：较高的回调频率，60ms/次，适用于UI更新。  - normal：普通的回调频率，200ms/次，低功耗。 |
| success | [DeviceOrientationResponse](js-apis-system-sensor.md#deviceorientationresponse6) | 是 | 感应到设备方向传感器数据变化后的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |

## DeviceOrientationResponse6+

WearableLite Wearable

感应到设备方向传感器数据变化后的回调函数。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alpha | number | 是 | 当设备坐标 X/Y 和地球 X/Y 重合时，绕着 Z 轴转动的夹角为 alpha。 |
| beta | number | 是 | 当设备坐标 Y/Z 和地球 Y/Z 重合时，绕着 X 轴转动的夹角为 beta。 |
| gamma | number | 是 | 当设备 X/Z 和地球 X/Z 重合时，绕着 Y 轴转动的夹角为 gamma。 |

## SubscribeGyroscopeOptions6+

WearableLite Wearable

用于侦听陀螺仪传感器数据的回调函数的执行频率。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| interval | string | 是 | 频率参数，陀螺仪的回调函数执行频率。  默认为normal，可选值有：  game：极高的回调频率，20ms/次，适用于游戏。  ui：较高的回调频率，60ms/次，适用于UI更新。  normal：普通的回调频率，200ms/次，低功耗。 |
| success | [GyroscopeResponse](js-apis-system-sensor.md#gyroscoperesponse6) | 是 | 感应到陀螺仪数据变化后的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |

## GyroscopeResponse6+

WearableLite Wearable

感应到陀螺仪传感器数据变化后的回调函数。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | x轴的旋转角速度。 |
| y | number | 是 | y轴的旋转角速度。 |
| z | number | 是 | z轴的旋转角速度。 |
