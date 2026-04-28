---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor
title: @ohos.sensor (传感器)
breadcrumb: API参考 > 系统 > 硬件 > Sensor Service Kit（传感器服务） > ArkTS API > @ohos.sensor (传感器)
category: harmonyos-references
scraped_at: 2026-04-28T08:11:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8e46ac26a994554f3812cb8e7d9f8db74d6ae561d5825c775c7ea7298a46b5dd
---

sensor模块提供了获取传感器数据的能力，包括获取传感器属性列表，订阅传感器数据，以及一些通用的传感器算法。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。订阅前可使用[getSingleSensor](js-apis-sensor.md#sensorgetsinglesensor9)接口获取该传感器的信息，获取该传感器信息成功时可正常订阅传感器，异常情况详见[getSingleSensor](js-apis-sensor.md#sensorgetsinglesensor9)错误码说明，具体使用方法可参考[指南开发步骤](../harmonyos-guides/sensor-guidelines.md#开发步骤)；订阅传感器数据时确保on订阅和off取消订阅成对出现。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { sensor } from '@kit.SensorServiceKit';
```

## sensor.on

PhonePC/2in1TabletTVWearable

### ACCELEROMETER9+

PhonePC/2in1TabletTVWearable

on(type: SensorId.ACCELEROMETER, callback: Callback<AccelerometerResponse>, options?: Options): void

订阅加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).ACCELEROMETER | 是 | 传感器类型，该值固定为SensorId.ACCELEROMETER。 |
| callback | Callback<[AccelerometerResponse](js-apis-sensor.md#accelerometerresponse)> | 是 | 回调函数，异步上报的传感器数据固定为AccelerometerResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
7. console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
8. console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
9. console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
10. }, { interval: 100000000 });
11. setTimeout(() => {
12. sensor.off(sensor.SensorId.ACCELEROMETER);
13. }, 500);
14. } catch (error) {
15. let e: BusinessError = error as BusinessError;
16. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
17. }
```

### FUSION\_PRESSURE22+

PhonePC/2in1TabletTVWearable

on(type: SensorId.FUSION\_PRESSURE, callback: Callback<FusionPressureResponse>, options?: Options): void

订阅融合压力传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).FUSION\_PRESSURE | 是 | 传感器类型，该值固定为SensorId.FUSION\_PRESSURE |
| callback | Callback<[FusionPressureResponse](js-apis-sensor.md#fusionpressureresponse22)> | 是 | 回调函数，异步上报的传感器数据固定为FusionPressureResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on(sensor.SensorId.FUSION_PRESSURE, (data: sensor.FusionPressureResponse) => {
7. console.info('Succeeded in invoking on. fusionPressure: ' + data.fusionPressure);
8. }, { interval: 100000000 });
9. setTimeout(() => {
10. sensor.off(sensor.SensorId.FUSION_PRESSURE);
11. }, 500);
12. } catch (error) {
13. let e: BusinessError = error as BusinessError;
14. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
15. }
```

### ACCELEROMETER\_UNCALIBRATED9+

PhonePC/2in1TabletTVWearable

on(type: SensorId.ACCELEROMETER\_UNCALIBRATED, callback: Callback<AccelerometerUncalibratedResponse>, options?: Options): void

订阅未校准加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).ACCELEROMETER\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.ACCELEROMETER\_UNCALIBRATED。 |
| callback | Callback<[AccelerometerUncalibratedResponse](js-apis-sensor.md#accelerometeruncalibratedresponse)> | 是 | 回调函数，异步上报的传感器数据固定为AccelerometerUncalibratedResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on(sensor.SensorId.ACCELEROMETER_UNCALIBRATED, (data: sensor.AccelerometerUncalibratedResponse) => {
7. console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
8. console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
9. console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
10. console.info('Succeeded in invoking on. X-coordinate bias: ' + data.biasX);
11. console.info('Succeeded in invoking on. Y-coordinate bias: ' + data.biasY);
12. console.info('Succeeded in invoking on. Z-coordinate bias: ' + data.biasZ);
13. }, { interval: 100000000 });
14. setTimeout(() => {
15. sensor.off(sensor.SensorId.ACCELEROMETER_UNCALIBRATED);
16. }, 500);
17. } catch (error) {
18. let e: BusinessError = error as BusinessError;
19. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
20. }
```

### AMBIENT\_LIGHT9+

PhonePC/2in1TabletTVWearable

on(type: SensorId.AMBIENT\_LIGHT, callback: Callback<LightResponse>, options?: Options): void

订阅环境光传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).AMBIENT\_LIGHT | 是 | 传感器类型，该值固定为SensorId.AMBIENT\_LIGHT。 |
| callback | Callback<[LightResponse](js-apis-sensor.md#lightresponse)> | 是 | 回调函数，异步上报的传感器数据固定为LightResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on(sensor.SensorId.AMBIENT_LIGHT, (data: sensor.LightResponse) => {
7. console.info('Succeeded in getting the ambient light intensity: ' + data.intensity);
8. }, { interval: 100000000 });
9. setTimeout(() => {
10. sensor.off(sensor.SensorId.AMBIENT_LIGHT);
11. }, 500);
12. } catch (error) {
13. let e: BusinessError = error as BusinessError;
14. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
15. }
```

### AMBIENT\_TEMPERATURE9+

PhonePC/2in1TabletTVWearable

on(type: SensorId.AMBIENT\_TEMPERATURE, callback: Callback<AmbientTemperatureResponse>, options?: Options): void

订阅温度传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).AMBIENT\_TEMPERATURE | 是 | 传感器类型，该值固定为SensorId.AMBIENT\_TEMPERATURE。 |
| callback | Callback<[AmbientTemperatureResponse](js-apis-sensor.md#ambienttemperatureresponse)> | 是 | 回调函数，异步上报的传感器数据固定为AmbientTemperatureResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on(sensor.SensorId.AMBIENT_TEMPERATURE, (data: sensor.AmbientTemperatureResponse) => {
7. console.info('Succeeded in invoking on. Temperature: ' + data.temperature);
8. }, { interval: 100000000 });
9. setTimeout(() => {
10. sensor.off(sensor.SensorId.AMBIENT_TEMPERATURE);
11. }, 500);
12. } catch (error) {
13. let e: BusinessError = error as BusinessError;
14. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
15. }
```

### BAROMETER9+

PhonePC/2in1TabletTVWearable

on(type: SensorId.BAROMETER, callback: Callback<BarometerResponse>, options?: Options): void

订阅气压计传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).BAROMETER | 是 | 传感器类型，该值固定为SensorId.BAROMETER。 |
| callback | Callback<[BarometerResponse](js-apis-sensor.md#barometerresponse)> | 是 | 回调函数，异步上报的传感器数据固定为BarometerResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on(sensor.SensorId.BAROMETER, (data: sensor.BarometerResponse) => {
7. console.info('Succeeded in invoking on. Atmospheric pressure: ' + data.pressure);
8. }, { interval: 100000000 });
9. setTimeout(() => {
10. sensor.off(sensor.SensorId.BAROMETER);
11. }, 500);
12. } catch (error) {
13. let e: BusinessError = error as BusinessError;
14. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
15. }
```

### GRAVITY9+

PhonePC/2in1TabletTVWearable

on(type: SensorId.GRAVITY, callback: Callback<GravityResponse>, options?: Options): void

订阅重力传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).GRAVITY | 是 | 传感器类型，该值固定为SensorId.GRAVITY。 |
| callback | Callback<[GravityResponse](js-apis-sensor.md#gravityresponse)> | 是 | 回调函数，异步上报的传感器数据固定为GravityResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on(sensor.SensorId.GRAVITY, (data: sensor.GravityResponse) => {
7. console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
8. console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
9. console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
10. }, { interval: 100000000 });
11. setTimeout(() => {
12. sensor.off(sensor.SensorId.GRAVITY);
13. }, 500);
14. } catch (error) {
15. let e: BusinessError = error as BusinessError;
16. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
17. }
```

### GYROSCOPE9+

PhonePC/2in1TabletTVWearable

on(type: SensorId.GYROSCOPE, callback: Callback<GyroscopeResponse>, options?: Options): void

订阅校准的陀螺仪传感器数据。

**需要权限**：ohos.permission.GYROSCOPE

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).GYROSCOPE | 是 | 传感器类型，该值固定为SensorId.GYROSCOPE。 |
| callback | Callback<[GyroscopeResponse](js-apis-sensor.md#gyroscoperesponse)> | 是 | 回调函数，异步上报的传感器数据固定为GyroscopeResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on(sensor.SensorId.GYROSCOPE, (data: sensor.GyroscopeResponse) => {
7. console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
8. console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
9. console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
10. }, { interval: 100000000 });
11. setTimeout(() => {
12. sensor.off(sensor.SensorId.GYROSCOPE);
13. }, 500);
14. } catch (error) {
15. let e: BusinessError = error as BusinessError;
16. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
17. }
```

### GYROSCOPE\_UNCALIBRATED9+

PhonePC/2in1TabletTVWearable

on(type: SensorId.GYROSCOPE\_UNCALIBRATED, callback: Callback<GyroscopeUncalibratedResponse>, options?: Options): void

订阅未校准陀螺仪传感器数据。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).GYROSCOPE\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.GYROSCOPE\_UNCALIBRATED。 |
| callback | Callback<[GyroscopeUncalibratedResponse](js-apis-sensor.md#gyroscopeuncalibratedresponse)> | 是 | 回调函数，异步上报的传感器数据固定为GyroscopeUncalibratedResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on(sensor.SensorId.GYROSCOPE_UNCALIBRATED, (data: sensor.GyroscopeUncalibratedResponse) => {
7. console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
8. console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
9. console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
10. console.info('Succeeded in invoking on. X-coordinate bias: ' + data.biasX);
11. console.info('Succeeded in invoking on. Y-coordinate bias: ' + data.biasY);
12. console.info('Succeeded in invoking on. Z-coordinate bias: ' + data.biasZ);
13. }, { interval: 100000000 });
14. setTimeout(() => {
15. sensor.off(sensor.SensorId.GYROSCOPE_UNCALIBRATED);
16. }, 500);
17. } catch (error) {
18. let e: BusinessError = error as BusinessError;
19. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
20. }
```

### HALL9+

PhonePC/2in1TabletTVWearable

on(type: SensorId.HALL, callback: Callback<HallResponse>, options?: Options): void

订阅霍尔传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).HALL | 是 | 传感器类型，该值固定为SensorId.HALL。 |
| callback | Callback<[HallResponse](js-apis-sensor.md#hallresponse)> | 是 | 回调函数，异步上报的传感器数据固定为HallResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，默认值为200000000ns。当霍尔事件被触发的很频繁时，该参数用于限定事件上报的频率。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on(sensor.SensorId.HALL, (data: sensor.HallResponse) => {
7. console.info('Succeeded in invoking on. Hall status: ' + data.status);
8. }, { interval: 100000000 });
9. setTimeout(() => {
10. sensor.off(sensor.SensorId.HALL);
11. }, 500);
12. } catch (error) {
13. let e: BusinessError = error as BusinessError;
14. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
15. }
```

### HEART\_RATE9+

PhonePC/2in1TabletTVWearable

on(type: SensorId.HEART\_RATE, callback: Callback<HeartRateResponse>, options?: Options): void

订阅心率传感器数据。

**需要权限**：ohos.permission.READ\_HEALTH\_DATA

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).HEART\_RATE | 是 | 传感器类型，该值固定为SensorId.HEART\_RATE。 |
| callback | Callback<[HeartRateResponse](js-apis-sensor.md#heartrateresponse)> | 是 | 回调函数，异步上报的传感器数据固定为HeartRateResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on(sensor.SensorId.HEART_RATE, (data: sensor.HeartRateResponse) => {
7. console.info('Succeeded in invoking on. Heart rate: ' + data.heartRate);
8. }, { interval: 100000000 });
9. setTimeout(() => {
10. sensor.off(sensor.SensorId.HEART_RATE);
11. }, 500);
12. } catch (error) {
13. let e: BusinessError = error as BusinessError;
14. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
15. }
```

### HUMIDITY9+

PhonePC/2in1TabletTVWearable

on(type: SensorId.HUMIDITY, callback: Callback<HumidityResponse>, options?: Options): void

订阅湿度传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).HUMIDITY | 是 | 传感器类型，该值固定为SensorId.HUMIDITY。 |
| callback | Callback<[HumidityResponse](js-apis-sensor.md#humidityresponse)> | 是 | 回调函数，异步上报的传感器数据固定为HumidityResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on(sensor.SensorId.HUMIDITY, (data: sensor.HumidityResponse) => {
7. console.info('Succeeded in invoking on. Humidity: ' + data.humidity);
8. }, { interval: 100000000 });
9. setTimeout(() => {
10. sensor.off(sensor.SensorId.HUMIDITY);
11. }, 500);
12. } catch (error) {
13. let e: BusinessError = error as BusinessError;
14. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
15. }
```

### LINEAR\_ACCELEROMETER9+

PhonePC/2in1TabletTVWearable

on(type: SensorId.LINEAR\_ACCELEROMETER, callback: Callback<LinearAccelerometerResponse>, options?: Options): void

订阅线性加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).LINEAR\_ACCELEROMETER | 是 | 传感器类型，该值固定为SensorId.LINEAR\_ACCELEROMETER。 |
| callback | Callback<[LinearAccelerometerResponse](js-apis-sensor.md#linearaccelerometerresponse)> | 是 | 回调函数，异步上报的传感器数据固定为LinearAccelerometerResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on(sensor.SensorId.LINEAR_ACCELEROMETER, (data: sensor.LinearAccelerometerResponse) => {
7. console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
8. console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
9. console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
10. }, { interval: 100000000 });
11. setTimeout(() => {
12. sensor.off(sensor.SensorId.LINEAR_ACCELEROMETER);
13. }, 500);
14. } catch (error) {
15. let e: BusinessError = error as BusinessError;
16. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
17. }
```

### MAGNETIC\_FIELD9+

PhonePC/2in1TabletTVWearable

on(type: SensorId.MAGNETIC\_FIELD, callback: Callback<MagneticFieldResponse>, options?: Options): void

订阅地磁传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).MAGNETIC\_FIELD | 是 | 传感器类型，该值固定为SensorId.MAGNETIC\_FIELD。 |
| callback | Callback<[MagneticFieldResponse](js-apis-sensor.md#magneticfieldresponse)> | 是 | 回调函数，异步上报的传感器数据固定为MagneticFieldResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on(sensor.SensorId.MAGNETIC_FIELD, (data: sensor.MagneticFieldResponse) => {
7. console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
8. console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
9. console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
10. }, { interval: 100000000 });
11. setTimeout(() => {
12. sensor.off(sensor.SensorId.MAGNETIC_FIELD);
13. }, 500);
14. } catch (error) {
15. let e: BusinessError = error as BusinessError;
16. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
17. }
```

### MAGNETIC\_FIELD\_UNCALIBRATED9+

PhonePC/2in1TabletTVWearable

on(type: SensorId.MAGNETIC\_FIELD\_UNCALIBRATED, callback: Callback<MagneticFieldUncalibratedResponse>, options?: Options): void

订阅未校准地磁传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).MAGNETIC\_FIELD\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.MAGNETIC\_FIELD\_UNCALIBRATED。 |
| callback | Callback<[MagneticFieldUncalibratedResponse](js-apis-sensor.md#magneticfielduncalibratedresponse)> | 是 | 回调函数，异步上报的传感器数据固定为MagneticFieldUncalibratedResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on(sensor.SensorId.MAGNETIC_FIELD_UNCALIBRATED, (data: sensor.MagneticFieldUncalibratedResponse) => {
7. console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
8. console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
9. console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
10. console.info('Succeeded in invoking on. X-coordinate bias: ' + data.biasX);
11. console.info('Succeeded in invoking on. Y-coordinate bias: ' + data.biasY);
12. console.info('Succeeded in invoking on. Z-coordinate bias: ' + data.biasZ);
13. }, { interval: 100000000 });
14. setTimeout(() => {
15. sensor.off(sensor.SensorId.MAGNETIC_FIELD_UNCALIBRATED);
16. }, 500);
17. } catch (error) {
18. let e: BusinessError = error as BusinessError;
19. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
20. }
```

### ORIENTATION9+

PhonePC/2in1TabletTVWearable

on(type: SensorId.ORIENTATION, callback: Callback<OrientationResponse>, options?: Options): void

订阅方向传感器数据。

说明

调用本接口的应用或服务可以通过提示用户使用8字校准法来提高应用获取的方向传感器的精度，此传感器理论误差正负5度，具体的精度根据不同的驱动及算法实现可能存在差异。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).ORIENTATION | 是 | 传感器类型，该值固定为SensorId.ORIENTATION。 |
| callback | Callback<[OrientationResponse](js-apis-sensor.md#orientationresponse)> | 是 | 回调函数，异步上报的传感器数据固定为OrientationResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on(sensor.SensorId.ORIENTATION, (data: sensor.OrientationResponse) => {
7. console.info('Succeeded in the device rotating at an angle around the Z axis: ' + data.alpha);
8. console.info('Succeeded in the device rotating at an angle around the X axis: ' + data.beta);
9. console.info('Succeeded in the device rotating at an angle around the Y axis: ' + data.gamma);
10. }, { interval: 100000000 });
11. setTimeout(() => {
12. sensor.off(sensor.SensorId.ORIENTATION);
13. }, 500);
14. } catch (error) {
15. let e: BusinessError = error as BusinessError;
16. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
17. }
```

### PEDOMETER9+

PhonePC/2in1TabletTVWearable

on(type: SensorId.PEDOMETER, callback: Callback<PedometerResponse>, options?: Options): void

订阅计步器传感器数据。计步传感器数据上报有一定延迟，延迟时间由具体的实现产品决定。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).PEDOMETER | 是 | 传感器类型，该值固定为SensorId.PEDOMETER。 |
| callback | Callback<[PedometerResponse](js-apis-sensor.md#pedometerresponse)> | 是 | 回调函数，异步上报的传感器数据固定为PedometerResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on(sensor.SensorId.PEDOMETER, (data: sensor.PedometerResponse) => {
7. console.info('Succeeded in invoking on. Step count: ' + data.steps);
8. }, { interval: 100000000 });
9. setTimeout(() => {
10. sensor.off(sensor.SensorId.PEDOMETER);
11. }, 500);
12. } catch (error) {
13. let e: BusinessError = error as BusinessError;
14. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
15. }
```

### PEDOMETER\_DETECTION9+

PhonePC/2in1TabletTVWearable

on(type: SensorId.PEDOMETER\_DETECTION, callback: Callback<PedometerDetectionResponse>, options?: Options): void

订阅计步检测器传感器数据。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).PEDOMETER\_DETECTION | 是 | 传感器类型，该值固定为SensorId.PEDOMETER\_DETECTION。 |
| callback | Callback<[PedometerDetectionResponse](js-apis-sensor.md#pedometerdetectionresponse)> | 是 | 回调函数，异步上报的传感器数据固定为PedometerDetectionResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on(sensor.SensorId.PEDOMETER_DETECTION, (data: sensor.PedometerDetectionResponse) => {
7. console.info('Succeeded in invoking on. Pedometer scalar: ' + data.scalar);
8. }, { interval: 100000000 });
9. setTimeout(() => {
10. sensor.off(sensor.SensorId.PEDOMETER_DETECTION);
11. }, 500);
12. } catch (error) {
13. let e: BusinessError = error as BusinessError;
14. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
15. }
```

### PROXIMITY9+

PhonePC/2in1TabletTVWearable

on(type: SensorId.PROXIMITY, callback: Callback<ProximityResponse>, options?: Options): void

订阅接近光传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).PROXIMITY | 是 | 传感器类型，该值固定为SensorId.PROXIMITY。 |
| callback | Callback<[ProximityResponse](js-apis-sensor.md#proximityresponse)> | 是 | 回调函数，异步上报的传感器数据固定为ProximityResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，默认值为200000000ns。当接近光事件被触发的很频繁时，该参数用于限定事件上报的频率。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3.Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on(sensor.SensorId.PROXIMITY, (data: sensor.ProximityResponse) => {
7. console.info('Succeeded in invoking on. Distance: ' + data.distance);
8. }, { interval: 100000000 });
9. setTimeout(() => {
10. sensor.off(sensor.SensorId.PROXIMITY);
11. }, 500);
12. } catch (error) {
13. let e: BusinessError = error as BusinessError;
14. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
15. }
```

### ROTATION\_VECTOR9+

PhonePC/2in1TabletTVWearable

on(type: SensorId.ROTATION\_VECTOR, callback: Callback<RotationVectorResponse>, options?: Options): void

订阅旋转矢量传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).ROTATION\_VECTOR | 是 | 传感器类型，该值固定为SensorId.ROTATION\_VECTOR。 |
| callback | Callback<[RotationVectorResponse](js-apis-sensor.md#rotationvectorresponse)> | 是 | 回调函数，异步上报的传感器数据固定为RotationVectorResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3.Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on(sensor.SensorId.ROTATION_VECTOR, (data: sensor.RotationVectorResponse) => {
7. console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
8. console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
9. console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
10. console.info('Succeeded in invoking on. Scalar quantity: ' + data.w);
11. }, { interval: 100000000 });
12. setTimeout(() => {
13. sensor.off(sensor.SensorId.ROTATION_VECTOR);
14. }, 500);
15. } catch (error) {
16. let e: BusinessError = error as BusinessError;
17. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
18. }
```

### SIGNIFICANT\_MOTION9+

PhonePC/2in1TabletTVWearable

on(type: SensorId.SIGNIFICANT\_MOTION, callback: Callback<SignificantMotionResponse>, options?: Options): void

订阅有效运动传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).SIGNIFICANT\_MOTION | 是 | 传感器类型，该值固定为SensorId.SIGNIFICANT\_MOTION。 |
| callback | Callback<[SignificantMotionResponse](js-apis-sensor.md#significantmotionresponse)> | 是 | 回调函数，异步上报的传感器数据固定为SignificantMotionResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3.Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on(sensor.SensorId.SIGNIFICANT_MOTION, (data: sensor.SignificantMotionResponse) => {
7. console.info('Succeeded in invoking on. Scalar data: ' + data.scalar);
8. }, { interval: 100000000 });
9. setTimeout(() => {
10. sensor.off(sensor.SensorId.SIGNIFICANT_MOTION);
11. }, 500);
12. } catch (error) {
13. let e: BusinessError = error as BusinessError;
14. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
15. }
```

### WEAR\_DETECTION9+

PhonePC/2in1TabletTVWearable

on(type: SensorId.WEAR\_DETECTION, callback: Callback<WearDetectionResponse>, options?: Options): void

订阅佩戴检测传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).WEAR\_DETECTION | 是 | 传感器类型，该值固定为SensorId.WEAR\_DETECTION。 |
| callback | Callback<[WearDetectionResponse](js-apis-sensor.md#weardetectionresponse)> | 是 | 回调函数，异步上报的传感器数据固定为WearDetectionResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3.Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on(sensor.SensorId.WEAR_DETECTION, (data: sensor.WearDetectionResponse) => {
7. console.info('Succeeded in invoking on. Wear status: ' + data.value);
8. }, { interval: 100000000 });
9. setTimeout(() => {
10. sensor.off(sensor.SensorId.WEAR_DETECTION);
11. }, 500);
12. } catch (error) {
13. let e: BusinessError = error as BusinessError;
14. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
15. }
```

### sensorStatusChange19+

PhonePC/2in1TabletTVWearable

on(type: 'sensorStatusChange', callback: Callback<SensorStatusEvent>): void

监听传感器上线下线状态的变化，callback返回传感器状态事件数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'sensorStatusChange' | 是 | 固定传入'sensorStatusChange',状态监听固定参数。 |
| callback | Callback<[SensorStatusEvent](js-apis-sensor.md#sensorstatusevent19)> | 是 | 回调函数，异步上报的传感器事件数据SensorStatusEvent。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.on('sensorStatusChange', (data: sensor.SensorStatusEvent) => {
7. console.info('sensorStatusChange : ' + JSON.stringify(data));
8. });
9. setTimeout(() => {
10. sensor.off('sensorStatusChange');
11. }, 5000);
12. } catch (error) {
13. let e: BusinessError = error as BusinessError;
14. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
15. }
```

## sensor.once9+

PhonePC/2in1TabletTVWearable

### ACCELEROMETER9+

PhonePC/2in1TabletTVWearable

once(type: SensorId.ACCELEROMETER, callback: Callback<AccelerometerResponse>): void

获取一次加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).ACCELEROMETER | 是 | 传感器类型，该值固定为SensorId.ACCELEROMETER。 |
| callback | Callback<[AccelerometerResponse](js-apis-sensor.md#accelerometerresponse)> | 是 | 回调函数，异步上报的传感器数据固定为AccelerometerResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.once(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
7. console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
8. console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
9. console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
10. });
11. } catch (error) {
12. let e: BusinessError = error as BusinessError;
13. console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
14. }
```

### ACCELEROMETER\_UNCALIBRATED9+

PhonePC/2in1TabletTVWearable

once(type: SensorId.ACCELEROMETER\_UNCALIBRATED, callback: Callback<AccelerometerUncalibratedResponse>): void

获取一次未校准加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).ACCELEROMETER\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.ACCELEROMETER\_UNCALIBRATED。 |
| callback | Callback<[AccelerometerUncalibratedResponse](js-apis-sensor.md#accelerometeruncalibratedresponse)> | 是 | 回调函数，异步上报的传感器数据固定为AccelerometerUncalibratedResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.once(sensor.SensorId.ACCELEROMETER_UNCALIBRATED, (data: sensor.AccelerometerUncalibratedResponse) => {
7. console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
8. console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
9. console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
10. console.info('Succeeded in invoking once. X-coordinate bias: ' + data.biasX);
11. console.info('Succeeded in invoking once. Y-coordinate bias: ' + data.biasY);
12. console.info('Succeeded in invoking once. Z-coordinate bias: ' + data.biasZ);
13. });
14. } catch (error) {
15. let e: BusinessError = error as BusinessError;
16. console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
17. }
```

### AMBIENT\_LIGHT9+

PhonePC/2in1TabletTVWearable

once(type: SensorId.AMBIENT\_LIGHT, callback: Callback<LightResponse>): void

获取一次环境光传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).AMBIENT\_LIGHT | 是 | 传感器类型，该值固定为SensorId.AMBIENT\_LIGHT。 |
| callback | Callback<[LightResponse](js-apis-sensor.md#lightresponse)> | 是 | 回调函数，异步上报的传感器数据固定为LightResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.once(sensor.SensorId.AMBIENT_LIGHT, (data: sensor.LightResponse) => {
7. console.info('Succeeded in invoking once. the ambient light intensity: ' + data.intensity);
8. });
9. } catch (error) {
10. let e: BusinessError = error as BusinessError;
11. console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
12. }
```

### AMBIENT\_TEMPERATURE9+

PhonePC/2in1TabletTVWearable

once(type: SensorId.AMBIENT\_TEMPERATURE, callback: Callback<AmbientTemperatureResponse>): void

获取一次温度传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).AMBIENT\_TEMPERATURE | 是 | 传感器类型，该值固定为SensorId.AMBIENT\_TEMPERATURE。 |
| callback | Callback<[AmbientTemperatureResponse](js-apis-sensor.md#ambienttemperatureresponse)> | 是 | 回调函数，异步上报的传感器数据固定为AmbientTemperatureResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.once(sensor.SensorId.AMBIENT_TEMPERATURE, (data: sensor.AmbientTemperatureResponse) => {
7. console.info('Succeeded in invoking once. Temperature: ' + data.temperature);
8. });
9. } catch (error) {
10. let e: BusinessError = error as BusinessError;
11. console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
12. }
```

### BAROMETER9+

PhonePC/2in1TabletTVWearable

once(type: SensorId.BAROMETER, callback: Callback<BarometerResponse>): void

获取一次气压计传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).BAROMETER | 是 | 传感器类型，该值固定为SensorId.BAROMETER。 |
| callback | Callback<[BarometerResponse](js-apis-sensor.md#barometerresponse)> | 是 | 回调函数，异步上报的传感器数据固定为BarometerResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.once(sensor.SensorId.BAROMETER, (data: sensor.BarometerResponse) => {
7. console.info('Succeeded in invoking once. Atmospheric pressure: ' + data.pressure);
8. });
9. } catch (error) {
10. let e: BusinessError = error as BusinessError;
11. console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
12. }
```

### GRAVITY9+

PhonePC/2in1TabletTVWearable

once(type: SensorId.GRAVITY, callback: Callback<GravityResponse>): void

获取一次重力传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).GRAVITY | 是 | 传感器类型，该值固定为SensorId.GRAVITY。 |
| callback | Callback<[GravityResponse](js-apis-sensor.md#gravityresponse)> | 是 | 回调函数，异步上报的传感器数据固定为GravityResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.once(sensor.SensorId.GRAVITY, (data: sensor.GravityResponse) => {
7. console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
8. console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
9. console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
10. });
11. } catch (error) {
12. let e: BusinessError = error as BusinessError;
13. console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
14. }
```

### GYROSCOPE9+

PhonePC/2in1TabletTVWearable

once(type: SensorId.GYROSCOPE, callback: Callback<GyroscopeResponse>): void

获取一次陀螺仪传感器数据。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).GYROSCOPE | 是 | 传感器类型，该值固定为SensorId.GYROSCOPE。 |
| callback | Callback<[GyroscopeResponse](js-apis-sensor.md#gyroscoperesponse)> | 是 | 回调函数，异步上报的传感器数据固定为GyroscopeResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.once(sensor.SensorId.GYROSCOPE, (data: sensor.GyroscopeResponse) => {
7. console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
8. console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
9. console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
10. });
11. } catch (error) {
12. let e: BusinessError = error as BusinessError;
13. console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
14. }
```

### GYROSCOPE\_UNCALIBRATED9+

PhonePC/2in1TabletTVWearable

once(type: SensorId.GYROSCOPE\_UNCALIBRATED, callback: Callback<GyroscopeUncalibratedResponse>): void

获取一次未校准陀螺仪传感器数据。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).GYROSCOPE\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.GYROSCOPE\_UNCALIBRATED。 |
| callback | Callback<[GyroscopeUncalibratedResponse](js-apis-sensor.md#gyroscopeuncalibratedresponse)> | 是 | 回调函数，异步上报的传感器数据固定为GyroscopeUncalibratedResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.once(sensor.SensorId.GYROSCOPE_UNCALIBRATED, (data: sensor.GyroscopeUncalibratedResponse) => {
7. console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
8. console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
9. console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
10. console.info('Succeeded in invoking once. X-coordinate bias: ' + data.biasX);
11. console.info('Succeeded in invoking once. Y-coordinate bias: ' + data.biasY);
12. console.info('Succeeded in invoking once. Z-coordinate bias: ' + data.biasZ);
13. });
14. } catch (error) {
15. let e: BusinessError = error as BusinessError;
16. console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
17. }
```

### HALL9+

PhonePC/2in1TabletTVWearable

once(type: SensorId.HALL, callback: Callback<HallResponse>): void

获取一次霍尔传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).HALL | 是 | 传感器类型，该值固定为SensorId.HALL。 |
| callback | Callback<[HallResponse](js-apis-sensor.md#hallresponse)> | 是 | 回调函数，异步上报的传感器数据固定为HallResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.once(sensor.SensorId.HALL, (data: sensor.HallResponse) => {
7. console.info('Succeeded in invoking once. Status: ' + data.status);
8. });
9. } catch (error) {
10. let e: BusinessError = error as BusinessError;
11. console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
12. }
```

### HEART\_RATE9+

PhonePC/2in1TabletTVWearable

once(type: SensorId.HEART\_RATE, callback: Callback<HeartRateResponse>): void

获取一次心率传感器数据。

**需要权限**：ohos.permission.READ\_HEALTH\_DATA

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).HEART\_RATE | 是 | 传感器类型，该值固定为SensorId.HEART\_RATE。 |
| callback | Callback<[HeartRateResponse](js-apis-sensor.md#heartrateresponse)> | 是 | 回调函数，异步上报的传感器数据固定为HeartRateResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.once(sensor.SensorId.HEART_RATE, (data: sensor.HeartRateResponse) => {
7. console.info('Succeeded in invoking once. Heart rate: ' + data.heartRate);
8. });
9. } catch (error) {
10. let e: BusinessError = error as BusinessError;
11. console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
12. }
```

### HUMIDITY9+

PhonePC/2in1TabletTVWearable

once(type: SensorId.HUMIDITY, callback: Callback<HumidityResponse>): void

获取一次湿度传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).HUMIDITY | 是 | 传感器类型，该值固定为SensorId.HUMIDITY。 |
| callback | Callback<[HumidityResponse](js-apis-sensor.md#humidityresponse)> | 是 | 回调函数，异步上报的传感器数据固定为HumidityResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.once(sensor.SensorId.HUMIDITY, (data: sensor.HumidityResponse) => {
7. console.info('Succeeded in invoking once. Humidity: ' + data.humidity);
8. });
9. } catch (error) {
10. let e: BusinessError = error as BusinessError;
11. console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
12. }
```

### LINEAR\_ACCELEROMETER9+

PhonePC/2in1TabletTVWearable

once(type: SensorId.LINEAR\_ACCELEROMETER, callback: Callback<LinearAccelerometerResponse>): void

获取一次线性加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).LINEAR\_ACCELEROMETER | 是 | 传感器类型，该值固定为SensorId.LINEAR\_ACCELEROMETER。 |
| callback | Callback<[LinearAccelerometerResponse](js-apis-sensor.md#linearaccelerometerresponse)> | 是 | 回调函数，异步上报的传感器数据固定为LinearAccelerometerResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.once(sensor.SensorId.LINEAR_ACCELEROMETER, (data: sensor.LinearAccelerometerResponse) => {
7. console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
8. console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
9. console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
10. });
11. } catch (error) {
12. let e: BusinessError = error as BusinessError;
13. console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
14. }
```

### MAGNETIC\_FIELD9+

PhonePC/2in1TabletTVWearable

once(type: SensorId.MAGNETIC\_FIELD, callback: Callback<MagneticFieldResponse>): void

获取一次磁场传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).MAGNETIC\_FIELD | 是 | 传感器类型，该值固定为SensorId.MAGNETIC\_FIELD。 |
| callback | Callback<[MagneticFieldResponse](js-apis-sensor.md#magneticfieldresponse)> | 是 | 回调函数，异步上报的传感器数据固定为MagneticFieldResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.once(sensor.SensorId.MAGNETIC_FIELD, (data: sensor.MagneticFieldResponse) => {
7. console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
8. console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
9. console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
10. });
11. } catch (error) {
12. let e: BusinessError = error as BusinessError;
13. console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
14. }
```

### MAGNETIC\_FIELD\_UNCALIBRATED9+

PhonePC/2in1TabletTVWearable

once(type: SensorId.MAGNETIC\_FIELD\_UNCALIBRATED, callback: Callback<MagneticFieldUncalibratedResponse>): void

获取一次未经校准的磁场传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).MAGNETIC\_FIELD\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.MAGNETIC\_FIELD\_UNCALIBRATED。 |
| callback | Callback<[MagneticFieldUncalibratedResponse](js-apis-sensor.md#magneticfielduncalibratedresponse)> | 是 | 回调函数，异步上报的传感器数据固定为MagneticFieldUncalibratedResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.once(sensor.SensorId.MAGNETIC_FIELD_UNCALIBRATED, (data: sensor.MagneticFieldUncalibratedResponse) => {
7. console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
8. console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
9. console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
10. console.info('Succeeded in invoking once. X-coordinate bias: ' + data.biasX);
11. console.info('Succeeded in invoking once. Y-coordinate bias: ' + data.biasY);
12. console.info('Succeeded in invoking once. Z-coordinate bias: ' + data.biasZ);
13. });
14. } catch (error) {
15. let e: BusinessError = error as BusinessError;
16. console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
17. }
```

### ORIENTATION9+

PhonePC/2in1TabletTVWearable

once(type: SensorId.ORIENTATION, callback: Callback<OrientationResponse>): void

获取一次方向传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).ORIENTATION | 是 | 传感器类型，该值固定为SensorId.ORIENTATION。 |
| callback | Callback<[OrientationResponse](js-apis-sensor.md#orientationresponse)> | 是 | 回调函数，异步上报的传感器数据固定为OrientationResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.once(sensor.SensorId.ORIENTATION, (data: sensor.OrientationResponse) => {
7. console.info('Succeeded in the device rotating at an angle around the X axis: ' + data.beta);
8. console.info('Succeeded in the device rotating at an angle around the Y axis: ' + data.gamma);
9. console.info('Succeeded in the device rotating at an angle around the Z axis: ' + data.alpha);
10. });
11. } catch (error) {
12. let e: BusinessError = error as BusinessError;
13. console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
14. }
```

### PEDOMETER9+

PhonePC/2in1TabletTVWearable

once(type: SensorId.PEDOMETER, callback: Callback<PedometerResponse>): void

获取一次计步器传感器数据。计步传感器数据上报有一定延迟，延迟时间由具体的实现产品决定。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).PEDOMETER | 是 | 传感器类型，该值固定为SensorId.PEDOMETER。 |
| callback | Callback<[PedometerResponse](js-apis-sensor.md#pedometerresponse)> | 是 | 回调函数，异步上报的传感器数据固定为PedometerResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.once(sensor.SensorId.PEDOMETER, (data: sensor.PedometerResponse) => {
7. console.info('Succeeded in invoking once. Step count: ' + data.steps);
8. });
9. } catch (error) {
10. let e: BusinessError = error as BusinessError;
11. console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
12. }
```

### PEDOMETER\_DETECTION9+

PhonePC/2in1TabletTVWearable

once(type: SensorId.PEDOMETER\_DETECTION, callback: Callback<PedometerDetectionResponse>): void

获取一次计步检测器传感器数据。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).PEDOMETER\_DETECTION | 是 | 传感器类型，该值固定为SensorId.PEDOMETER\_DETECTION。 |
| callback | Callback<[PedometerDetectionResponse](js-apis-sensor.md#pedometerdetectionresponse)> | 是 | 回调函数，异步上报的传感器数据固定为PedometerDetectionResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.once(sensor.SensorId.PEDOMETER_DETECTION, (data: sensor.PedometerDetectionResponse) => {
7. console.info('Succeeded in invoking once. Scalar data: ' + data.scalar);
8. });
9. } catch (error) {
10. let e: BusinessError = error as BusinessError;
11. console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
12. }
```

### PROXIMITY9+

PhonePC/2in1TabletTVWearable

once(type: SensorId.PROXIMITY, callback: Callback<ProximityResponse>): void

获取一次接近光传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).PROXIMITY | 是 | 传感器类型，该值固定为SensorId.PROXIMITY。 |
| callback | Callback<[ProximityResponse](js-apis-sensor.md#proximityresponse)> | 是 | 回调函数，异步上报的传感器数据固定为ProximityResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.once(sensor.SensorId.PROXIMITY, (data: sensor.ProximityResponse) => {
7. console.info('Succeeded in invoking once. Distance: ' + data.distance);
8. });
9. } catch (error) {
10. let e: BusinessError = error as BusinessError;
11. console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
12. }
```

### ROTATION\_VECTOR9+

PhonePC/2in1TabletTVWearable

once(type: SensorId.ROTATION\_VECTOR, callback: Callback<RotationVectorResponse>): void

获取一次旋转矢量传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).ROTATION\_VECTOR | 是 | 传感器类型，该值固定为SensorId.ROTATION\_VECTOR。 |
| callback | Callback<[RotationVectorResponse](js-apis-sensor.md#rotationvectorresponse)> | 是 | 回调函数，异步上报的传感器数据固定为RotationVectorResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.once(sensor.SensorId.ROTATION_VECTOR, (data: sensor.RotationVectorResponse) => {
7. console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
8. console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
9. console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
10. console.info('Succeeded in invoking once. Scalar quantity: ' + data.w);
11. });
12. } catch (error) {
13. let e: BusinessError = error as BusinessError;
14. console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
15. }
```

### SIGNIFICANT\_MOTION9+

PhonePC/2in1TabletTVWearable

once(type: SensorId.SIGNIFICANT\_MOTION, callback: Callback<SignificantMotionResponse>): void

获取一次有效运动传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).SIGNIFICANT\_MOTION | 是 | 传感器类型，该值固定为SensorId.SIGNIFICANT\_MOTION。 |
| callback | Callback<[SignificantMotionResponse](js-apis-sensor.md#significantmotionresponse)> | 是 | 回调函数，异步上报的传感器数据固定为SignificantMotionResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.once(sensor.SensorId.SIGNIFICANT_MOTION, (data: sensor.SignificantMotionResponse) => {
7. console.info('Succeeded in invoking once. Scalar data: ' + data.scalar);
8. });
9. } catch (error) {
10. let e: BusinessError = error as BusinessError;
11. console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
12. }
```

### WEAR\_DETECTION9+

PhonePC/2in1TabletTVWearable

once(type: SensorId.WEAR\_DETECTION, callback: Callback<WearDetectionResponse>): void

获取一次佩戴检测传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).WEAR\_DETECTION | 是 | 传感器类型，该值固定为SensorId.WEAR\_DETECTION。 |
| callback | Callback<[WearDetectionResponse](js-apis-sensor.md#weardetectionresponse)> | 是 | 回调函数，异步上报的传感器数据固定为WearDetectionResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.once(sensor.SensorId.WEAR_DETECTION, (data: sensor.WearDetectionResponse) => {
7. console.info('Succeeded in invoking once. Wear status: ' + data.value);
8. });
9. } catch (error) {
10. let e: BusinessError = error as BusinessError;
11. console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
12. }
```

## sensor.off

PhonePC/2in1TabletTVWearable

### ACCELEROMETER9+

PhonePC/2in1TabletTVWearable

off(type: SensorId.ACCELEROMETER, callback?: Callback<AccelerometerResponse>): void

取消订阅加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).ACCELEROMETER | 是 | 传感器类型，该值固定为SensorId.ACCELEROMETER。 |
| callback | Callback<[AccelerometerResponse](js-apis-sensor.md#accelerometerresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback1(data: object) {
5. console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
6. }

8. function callback2(data: object) {
9. console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
10. }

12. // 使用try catch对可能出现的异常进行捕获
13. try {
14. sensor.on(sensor.SensorId.ACCELEROMETER, callback1);
15. sensor.on(sensor.SensorId.ACCELEROMETER, callback2);
16. // 仅取消callback1的注册
17. sensor.off(sensor.SensorId.ACCELEROMETER, callback1);
18. // 取消SensorId.ACCELEROMETER类型的所有回调
19. sensor.off(sensor.SensorId.ACCELEROMETER);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
23. }
```

### ACCELEROMETER19+

PhonePC/2in1TabletTVWearable

off(type: SensorId.ACCELEROMETER, sensorInfoParam?: SensorInfoParam, callback?: Callback<AccelerometerResponse>): void

取消订阅加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**元服务API**：从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).ACCELEROMETER | 是 | 传感器类型，该值固定为SensorId.ACCELEROMETER。 |
| sensorInfoParam | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[AccelerometerResponse](js-apis-sensor.md#accelerometerresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. enum Ret { OK, Failed = -1 }

6. // 传感器回调
7. const sensorCallback = (response: sensor.AccelerometerResponse) => {
8. console.info(`callback response: ${JSON.stringify(response)}`);
9. }
10. // 传感器监听类别
11. const sensorType = sensor.SensorId.ACCELEROMETER;
12. const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

14. function sensorSubscribe(): Ret {
15. let ret: Ret = Ret.OK;
16. // 使用try catch对可能出现的异常进行捕获
17. try {
18. // 查询所有的传感器
19. const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
20. if (!sensorList.length) {
21. return Ret.Failed;
22. }
23. // 根据实际业务逻辑获取目标传感器。
24. const targetSensor = sensorList
25. // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
26. .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
27. // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
28. .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
29. if (!targetSensor) {
30. return Ret.Failed;
31. }
32. sensorInfoParam.deviceId = targetSensor.deviceId;
33. sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
34. // 订阅传感器事件
35. sensor.on(sensorType, sensorCallback, { sensorInfoParam });
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
39. ret = Ret.Failed;
40. }
41. return ret;
42. }

44. function sensorUnsubscribe(): Ret {
45. let ret: Ret = Ret.OK;
46. // 使用try catch对可能出现的异常进行捕获
47. try {
48. sensor.off(sensorType, sensorInfoParam, sensorCallback);
49. } catch (error) {
50. let e: BusinessError = error as BusinessError;
51. console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
52. ret = Ret.Failed;
53. }
54. return ret;
55. }
```

### ACCELEROMETER\_UNCALIBRATED9+

PhonePC/2in1TabletTVWearable

off(type: SensorId.ACCELEROMETER\_UNCALIBRATED, callback?: Callback<AccelerometerUncalibratedResponse>): void

取消订阅未校准加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).ACCELEROMETER\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.ACCELEROMETER\_UNCALIBRATED。 |
| callback | Callback<[AccelerometerUncalibratedResponse](js-apis-sensor.md#accelerometeruncalibratedresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback1(data: object) {
5. console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
6. }

8. function callback2(data: object) {
9. console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
10. }

12. // 使用try catch对可能出现的异常进行捕获
13. try {
14. sensor.on(sensor.SensorId.ACCELEROMETER_UNCALIBRATED, callback1);
15. sensor.on(sensor.SensorId.ACCELEROMETER_UNCALIBRATED, callback2);
16. // 仅取消callback1的注册
17. sensor.off(sensor.SensorId.ACCELEROMETER_UNCALIBRATED, callback1);
18. // 取消注册SensorId.ACCELEROMETER_UNCALIBRATED类型的所有回调
19. sensor.off(sensor.SensorId.ACCELEROMETER_UNCALIBRATED);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
23. }
```

### FUSION\_PRESSURE22+

PhonePC/2in1TabletTVWearable

off(type: SensorId.FUSION\_PRESSURE, sensorInfoParam?: SensorInfoParam, callback?: Callback<FusionPressureResponse>): void

取消订阅融合压力传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).FUSION\_PRESSURE | 是 | 传感器类型，该值固定为SensorId.FUSION\_PRESSURE。 |
| sensorInfoParam | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[FusionPressureResponse](js-apis-sensor.md#fusionpressureresponse22)> | 否 | 取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. enum Ret { OK, Failed = -1 }

6. // 传感器回调
7. const sensorCallback = (response: sensor.FusionPressureResponse) => {
8. console.info(`callback response: ${JSON.stringify(response)}`);
9. }
10. // 传感器监听类型
11. const sensorType = sensor.SensorId.FUSION_PRESSURE;
12. const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

14. function sensorSubscribe(): Ret {
15. let ret: Ret = Ret.OK;
16. // 使用try catch对可能出现的异常进行捕获
17. try {
18. // 查询所有的传感器
19. const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
20. if (!sensorList.length) {
21. return Ret.Failed;
22. }
23. // 根据实际业务逻辑获取目标传感器。
24. const targetSensor = sensorList
25. // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
26. .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
27. // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
28. .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
29. if (!targetSensor) {
30. return Ret.Failed;
31. }
32. sensorInfoParam.deviceId = targetSensor.deviceId;
33. sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
34. // 订阅传感器事件
35. sensor.on(sensorType, sensorCallback, { sensorInfoParam });
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
39. ret = Ret.Failed;
40. }
41. return ret;
42. }

44. function sensorUnsubscribe(): Ret {
45. let ret: Ret = Ret.OK;
46. // 使用try catch对可能出现的异常进行捕获
47. try {
48. sensor.off(sensorType, sensorInfoParam, sensorCallback);
49. } catch (error) {
50. let e: BusinessError = error as BusinessError;
51. console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
52. ret = Ret.Failed;
53. }
54. return ret;
55. }
```

### ACCELEROMETER\_UNCALIBRATED19+

PhonePC/2in1TabletTVWearable

off(type: SensorId.ACCELEROMETER\_UNCALIBRATED, sensorInfoParam?: SensorInfoParam, callback?: Callback<AccelerometerUncalibratedResponse>): void

取消订阅未校准加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).ACCELEROMETER\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.ACCELEROMETER\_UNCALIBRATED。 |
| sensorInfoParam | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[AccelerometerUncalibratedResponse](js-apis-sensor.md#accelerometeruncalibratedresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. enum Ret { OK, Failed = -1 }

6. // 传感器回调
7. const sensorCallback = (response: sensor.AccelerometerUncalibratedResponse) => {
8. console.info(`callback response: ${JSON.stringify(response)}`);
9. }
10. // 传感器监听类型
11. const sensorType = sensor.SensorId.ACCELEROMETER_UNCALIBRATED;
12. const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

14. function sensorSubscribe(): Ret {
15. let ret: Ret = Ret.OK;
16. // 使用try catch对可能出现的异常进行捕获
17. try {
18. // 查询所有的传感器
19. const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
20. if (!sensorList.length) {
21. return Ret.Failed;
22. }
23. // 根据实际业务逻辑获取目标传感器。
24. const targetSensor = sensorList
25. // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
26. .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
27. // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
28. .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
29. if (!targetSensor) {
30. return Ret.Failed;
31. }
32. sensorInfoParam.deviceId = targetSensor.deviceId;
33. sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
34. // 订阅传感器事件
35. sensor.on(sensorType, sensorCallback, { sensorInfoParam });
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
39. ret = Ret.Failed;
40. }
41. return ret;
42. }

44. function sensorUnsubscribe(): Ret {
45. let ret: Ret = Ret.OK;
46. // 使用try catch对可能出现的异常进行捕获
47. try {
48. sensor.off(sensorType, sensorInfoParam, sensorCallback);
49. } catch (error) {
50. let e: BusinessError = error as BusinessError;
51. console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
52. ret = Ret.Failed;
53. }
54. return ret;
55. }
```

### AMBIENT\_LIGHT9+

PhonePC/2in1TabletTVWearable

off(type: SensorId.AMBIENT\_LIGHT, callback?: Callback<LightResponse>): void

取消订阅环境光传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).AMBIENT\_LIGHT | 是 | 传感器类型，该值固定为SensorId.AMBIENT\_LIGHT。 |
| callback | Callback<[LightResponse](js-apis-sensor.md#lightresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback1(data: object) {
5. console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
6. }

8. function callback2(data: object) {
9. console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
10. }

12. // 使用try catch对可能出现的异常进行捕获
13. try {
14. sensor.on(sensor.SensorId.AMBIENT_LIGHT, callback1);
15. sensor.on(sensor.SensorId.AMBIENT_LIGHT, callback2);
16. // 仅取消callback1的注册
17. sensor.off(sensor.SensorId.AMBIENT_LIGHT, callback1);
18. // 取消注册SensorId.AMBIENT_LIGHT
19. sensor.off(sensor.SensorId.AMBIENT_LIGHT);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
23. }
```

### AMBIENT\_LIGHT19+

PhonePC/2in1TabletTVWearable

off(type: SensorId.AMBIENT\_LIGHT, sensorInfoParam?: SensorInfoParam, callback?: Callback<LightResponse>): void

取消订阅环境光传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).AMBIENT\_LIGHT | 是 | 传感器类型，该值固定为SensorId.AMBIENT\_LIGHT。 |
| sensorInfoParam | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[LightResponse](js-apis-sensor.md#lightresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. enum Ret { OK, Failed = -1 }

6. // 传感器回调
7. const sensorCallback = (response: sensor.LightResponse) => {
8. console.info(`callback response: ${JSON.stringify(response)}`);
9. }
10. // 传感器监听类型
11. const sensorType = sensor.SensorId.AMBIENT_LIGHT;
12. const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

14. function sensorSubscribe(): Ret {
15. let ret: Ret = Ret.OK;
16. // 使用try catch对可能出现的异常进行捕获
17. try {
18. // 查询所有的传感器
19. const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
20. if (!sensorList.length) {
21. return Ret.Failed;
22. }
23. // 根据实际业务逻辑获取目标传感器。
24. const targetSensor = sensorList
25. // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
26. .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
27. // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
28. .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
29. if (!targetSensor) {
30. return Ret.Failed;
31. }
32. sensorInfoParam.deviceId = targetSensor.deviceId;
33. sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
34. // 订阅传感器事件
35. sensor.on(sensorType, sensorCallback, { sensorInfoParam });
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
39. ret = Ret.Failed;
40. }
41. return ret;
42. }

44. function sensorUnsubscribe(): Ret {
45. let ret: Ret = Ret.OK;
46. // 使用try catch对可能出现的异常进行捕获
47. try {
48. sensor.off(sensorType, sensorInfoParam, sensorCallback);
49. } catch (error) {
50. let e: BusinessError = error as BusinessError;
51. console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
52. ret = Ret.Failed;
53. }
54. return ret;
55. }
```

### AMBIENT\_TEMPERATURE9+

PhonePC/2in1TabletTVWearable

off(type: SensorId.AMBIENT\_TEMPERATURE, callback?: Callback<AmbientTemperatureResponse>): void

取消订阅温度传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).AMBIENT\_TEMPERATURE | 是 | 传感器类型，该值固定为SensorId.AMBIENT\_TEMPERATURE。 |
| callback | Callback<[AmbientTemperatureResponse](js-apis-sensor.md#ambienttemperatureresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback1(data: object) {
5. console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
6. }

8. function callback2(data: object) {
9. console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
10. }

12. // 使用try catch对可能出现的异常进行捕获
13. try {
14. sensor.on(sensor.SensorId.AMBIENT_TEMPERATURE, callback1);
15. sensor.on(sensor.SensorId.AMBIENT_TEMPERATURE, callback2);
16. // 仅取消callback1的注册
17. sensor.off(sensor.SensorId.AMBIENT_TEMPERATURE, callback1);
18. // 取消注册SensorId.AMBIENT_TEMPERATURE的所有回调
19. sensor.off(sensor.SensorId.AMBIENT_TEMPERATURE);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
23. }
```

### AMBIENT\_TEMPERATURE19+

PhonePC/2in1TabletTVWearable

off(type: SensorId.AMBIENT\_TEMPERATURE, sensorInfoParam?: SensorInfoParam, callback?: Callback<AmbientTemperatureResponse>): void

取消订阅温度传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).AMBIENT\_TEMPERATURE | 是 | 传感器类型，该值固定为SensorId.AMBIENT\_TEMPERATURE。 |
| sensorInfoParam | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[AmbientTemperatureResponse](js-apis-sensor.md#ambienttemperatureresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. enum Ret { OK, Failed = -1 }

6. // 传感器回调
7. const sensorCallback = (response: sensor.AmbientTemperatureResponse) => {
8. console.info(`callback response: ${JSON.stringify(response)}`);
9. }
10. // 传感器监听类型
11. const sensorType = sensor.SensorId.AMBIENT_TEMPERATURE;
12. const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

14. function sensorSubscribe(): Ret {
15. let ret: Ret = Ret.OK;
16. // 使用try catch对可能出现的异常进行捕获
17. try {
18. // 查询所有的传感器
19. const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
20. if (!sensorList.length) {
21. return Ret.Failed;
22. }
23. // 根据实际业务逻辑获取目标传感器。
24. const targetSensor = sensorList
25. // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
26. .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
27. // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
28. .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
29. if (!targetSensor) {
30. return Ret.Failed;
31. }
32. sensorInfoParam.deviceId = targetSensor.deviceId;
33. sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
34. // 订阅传感器事件
35. sensor.on(sensorType, sensorCallback, { sensorInfoParam });
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
39. ret = Ret.Failed;
40. }
41. return ret;
42. }

44. function sensorUnsubscribe(): Ret {
45. let ret: Ret = Ret.OK;
46. // 使用try catch对可能出现的异常进行捕获
47. try {
48. sensor.off(sensorType, sensorInfoParam, sensorCallback);
49. } catch (error) {
50. let e: BusinessError = error as BusinessError;
51. console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
52. ret = Ret.Failed;
53. }
54. return ret;
55. }
```

### BAROMETER9+

PhonePC/2in1TabletTVWearable

off(type: SensorId.BAROMETER, callback?: Callback<BarometerResponse>): void

取消订阅气压计传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).BAROMETER | 是 | 传感器类型，该值固定为SensorId.BAROMETER。 |
| callback | Callback<[BarometerResponse](js-apis-sensor.md#barometerresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback1(data: object) {
5. console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
6. }

8. function callback2(data: object) {
9. console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
10. }

12. // 使用try catch对可能出现的异常进行捕获
13. try {
14. sensor.on(sensor.SensorId.BAROMETER, callback1);
15. sensor.on(sensor.SensorId.BAROMETER, callback2);
16. // 仅取消callback1的注册
17. sensor.off(sensor.SensorId.BAROMETER, callback1);
18. // 取消注册SensorId.BAROMETER的所有回调
19. sensor.off(sensor.SensorId.BAROMETER);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
23. }
```

### BAROMETER19+

PhonePC/2in1TabletTVWearable

off(type: SensorId.BAROMETER, sensorInfoParam?: SensorInfoParam, callback?: Callback<BarometerResponse>): void

取消订阅气压计传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).BAROMETER | 是 | 传感器类型，该值固定为SensorId.BAROMETER。 |
| sensorInfoParam | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[BarometerResponse](js-apis-sensor.md#barometerresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. enum Ret { OK, Failed = -1 }

6. // 传感器回调
7. const sensorCallback = (response: sensor.BarometerResponse) => {
8. console.info(`callback response: ${JSON.stringify(response)}`);
9. }
10. // 传感器监听类型
11. const sensorType = sensor.SensorId.BAROMETER;
12. const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

14. function sensorSubscribe(): Ret {
15. let ret: Ret = Ret.OK;
16. // 使用try catch对可能出现的异常进行捕获
17. try {
18. // 查询所有的传感器
19. const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
20. if (!sensorList.length) {
21. return Ret.Failed;
22. }
23. // 根据实际业务逻辑获取目标传感器。
24. const targetSensor = sensorList
25. // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
26. .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
27. // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
28. .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
29. if (!targetSensor) {
30. return Ret.Failed;
31. }
32. sensorInfoParam.deviceId = targetSensor.deviceId;
33. sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
34. // 订阅传感器事件
35. sensor.on(sensorType, sensorCallback, { sensorInfoParam });
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
39. ret = Ret.Failed;
40. }
41. return ret;
42. }

44. function sensorUnsubscribe(): Ret {
45. let ret: Ret = Ret.OK;
46. // 使用try catch对可能出现的异常进行捕获
47. try {
48. sensor.off(sensorType, sensorInfoParam, sensorCallback);
49. } catch (error) {
50. let e: BusinessError = error as BusinessError;
51. console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
52. ret = Ret.Failed;
53. }
54. return ret;
55. }
```

### GRAVITY9+

PhonePC/2in1TabletTVWearable

off(type: SensorId.GRAVITY, callback?: Callback<GravityResponse>): void

取消订阅重力传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).GRAVITY | 是 | 传感器类型，该值固定为SensorId.GRAVITY。 |
| callback | Callback<[GravityResponse](js-apis-sensor.md#gravityresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback1(data: object) {
5. console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
6. }

8. function callback2(data: object) {
9. console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
10. }

12. // 使用try catch对可能出现的异常进行捕获
13. try {
14. sensor.on(sensor.SensorId.GRAVITY, callback1);
15. sensor.on(sensor.SensorId.GRAVITY, callback2);
16. // 仅取消callback1的注册
17. sensor.off(sensor.SensorId.GRAVITY, callback1);
18. // 取消注册SensorId.GRAVITY的所有回调
19. sensor.off(sensor.SensorId.GRAVITY);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
23. }
```

### GRAVITY19+

PhonePC/2in1TabletTVWearable

off(type: SensorId.GRAVITY, sensorInfoParam?: SensorInfoParam, callback?: Callback<GravityResponse>): void

取消订阅重力传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).GRAVITY | 是 | 传感器类型，该值固定为SensorId.GRAVITY。 |
| sensorInfoParam | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[GravityResponse](js-apis-sensor.md#gravityresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. enum Ret { OK, Failed = -1 }

6. // 传感器回调
7. const sensorCallback = (response: sensor.GravityResponse) => {
8. console.info(`callback response: ${JSON.stringify(response)}`);
9. }
10. // 传感器监听类型
11. const sensorType = sensor.SensorId.GRAVITY;
12. const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

14. function sensorSubscribe(): Ret {
15. let ret: Ret = Ret.OK;
16. // 使用try catch对可能出现的异常进行捕获
17. try {
18. // 查询所有的传感器
19. const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
20. if (!sensorList.length) {
21. return Ret.Failed;
22. }
23. // 根据实际业务逻辑获取目标传感器。
24. const targetSensor = sensorList
25. // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
26. .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
27. // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
28. .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
29. if (!targetSensor) {
30. return Ret.Failed;
31. }
32. sensorInfoParam.deviceId = targetSensor.deviceId;
33. sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
34. // 订阅传感器事件
35. sensor.on(sensorType, sensorCallback, { sensorInfoParam });
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
39. ret = Ret.Failed;
40. }
41. return ret;
42. }

44. function sensorUnsubscribe(): Ret {
45. let ret: Ret = Ret.OK;
46. // 使用try catch对可能出现的异常进行捕获
47. try {
48. sensor.off(sensorType, sensorInfoParam, sensorCallback);
49. } catch (error) {
50. let e: BusinessError = error as BusinessError;
51. console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
52. ret = Ret.Failed;
53. }
54. return ret;
55. }
```

### GYROSCOPE9+

PhonePC/2in1TabletTVWearable

off(type: SensorId.GYROSCOPE, callback?: Callback<GyroscopeResponse>): void

取消订阅陀螺仪传感器数据。

**需要权限**：ohos.permission.GYROSCOPE

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).GYROSCOPE | 是 | 传感器类型，该值固定为SensorId.GYROSCOPE。 |
| callback | Callback<[GyroscopeResponse](js-apis-sensor.md#gyroscoperesponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback1(data: object) {
5. console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
6. }

8. function callback2(data: object) {
9. console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
10. }

12. // 使用try catch对可能出现的异常进行捕获
13. try {
14. sensor.on(sensor.SensorId.GYROSCOPE, callback1);
15. sensor.on(sensor.SensorId.GYROSCOPE, callback2);
16. // 仅取消callback1的注册
17. sensor.off(sensor.SensorId.GYROSCOPE, callback1);
18. // 取消注册SensorId.GYROSCOPE的所有回调
19. sensor.off(sensor.SensorId.GYROSCOPE);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
23. }
```

### GYROSCOPE19+

PhonePC/2in1TabletTVWearable

off(type: SensorId.GYROSCOPE, sensorInfoParam?: SensorInfoParam, callback?: Callback<GyroscopeResponse>): void

取消订阅陀螺仪传感器数据。

**需要权限**：ohos.permission.GYROSCOPE

**元服务API**：从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).GYROSCOPE | 是 | 传感器类型，该值固定为SensorId.GYROSCOPE。 |
| sensorInfoParam | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[GyroscopeResponse](js-apis-sensor.md#gyroscoperesponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[传感器错误码](errorcode-sensor.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. enum Ret { OK, Failed = -1 }

6. // 传感器回调
7. const sensorCallback = (response: sensor.GyroscopeResponse) => {
8. console.info(`callback response: ${JSON.stringify(response)}`);
9. }
10. // 传感器监听类型
11. const sensorType = sensor.SensorId.GYROSCOPE;
12. const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

14. function sensorSubscribe(): Ret {
15. let ret: Ret = Ret.OK;
16. // 使用try catch对可能出现的异常进行捕获
17. try {
18. // 查询所有的传感器
19. const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
20. if (!sensorList.length) {
21. return Ret.Failed;
22. }
23. // 根据实际业务逻辑获取目标传感器。
24. const targetSensor = sensorList
25. // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
26. .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
27. // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
28. .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
29. if (!targetSensor) {
30. return Ret.Failed;
31. }
32. sensorInfoParam.deviceId = targetSensor.deviceId;
33. sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
34. // 订阅传感器事件
35. sensor.on(sensorType, sensorCallback, { sensorInfoParam });
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
39. ret = Ret.Failed;
40. }
41. return ret;
42. }

44. function sensorUnsubscribe(): Ret {
45. let ret: Ret = Ret.OK;
46. // 使用try catch对可能出现的异常进行捕获
47. try {
48. sensor.off(sensorType, sensorInfoParam, sensorCallback);
49. } catch (error) {
50. let e: BusinessError = error as BusinessError;
51. console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
52. ret = Ret.Failed;
53. }
54. return ret;
55. }
```

### GYROSCOPE\_UNCALIBRATED9+

PhonePC/2in1TabletTVWearable

off(type: SensorId.GYROSCOPE\_UNCALIBRATED, callback?: Callback<GyroscopeUncalibratedResponse>): void

取消订阅未校准陀螺仪传感器数据。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).GYROSCOPE\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.GYROSCOPE\_UNCALIBRATED。 |
| callback | Callback<[GyroscopeUncalibratedResponse](js-apis-sensor.md#gyroscopeuncalibratedresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback1(data: object) {
5. console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
6. }

8. function callback2(data: object) {
9. console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
10. }

12. // 使用try catch对可能出现的异常进行捕获
13. try {
14. sensor.on(sensor.SensorId.GYROSCOPE_UNCALIBRATED, callback1);
15. sensor.on(sensor.SensorId.GYROSCOPE_UNCALIBRATED, callback2);
16. // 仅取消callback1的注册
17. sensor.off(sensor.SensorId.GYROSCOPE_UNCALIBRATED, callback1);
18. // 取消注册SensorId.GYROSCOPE_UNCALIBRATED的所有回调
19. sensor.off(sensor.SensorId.GYROSCOPE_UNCALIBRATED);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
23. }
```

### GYROSCOPE\_UNCALIBRATED19+

PhonePC/2in1TabletTVWearable

off(type: SensorId.GYROSCOPE\_UNCALIBRATED, sensorInfoParam?: SensorInfoParam, callback?: Callback<GyroscopeUncalibratedResponse>): void

取消订阅未校准陀螺仪传感器数据。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).GYROSCOPE\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.GYROSCOPE\_UNCALIBRATED。 |
| sensorInfoParam | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[GyroscopeUncalibratedResponse](js-apis-sensor.md#gyroscopeuncalibratedresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[传感器错误码](errorcode-sensor.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. enum Ret { OK, Failed = -1 }

6. // 传感器回调
7. const sensorCallback = (response: sensor.GyroscopeUncalibratedResponse) => {
8. console.info(`callback response: ${JSON.stringify(response)}`);
9. }
10. // 传感器监听类型
11. const sensorType = sensor.SensorId.GYROSCOPE_UNCALIBRATED;
12. const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

14. function sensorSubscribe(): Ret {
15. let ret: Ret = Ret.OK;
16. // 使用try catch对可能出现的异常进行捕获
17. try {
18. // 查询所有的传感器
19. const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
20. if (!sensorList.length) {
21. return Ret.Failed;
22. }
23. // 根据实际业务逻辑获取目标传感器。
24. const targetSensor = sensorList
25. // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
26. .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
27. // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
28. .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
29. if (!targetSensor) {
30. return Ret.Failed;
31. }
32. sensorInfoParam.deviceId = targetSensor.deviceId;
33. sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
34. // 订阅传感器事件
35. sensor.on(sensorType, sensorCallback, { sensorInfoParam });
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
39. ret = Ret.Failed;
40. }
41. return ret;
42. }

44. function sensorUnsubscribe(): Ret {
45. let ret: Ret = Ret.OK;
46. // 使用try catch对可能出现的异常进行捕获
47. try {
48. sensor.off(sensorType, sensorInfoParam, sensorCallback);
49. } catch (error) {
50. let e: BusinessError = error as BusinessError;
51. console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
52. ret = Ret.Failed;
53. }
54. return ret;
55. }
```

### HALL9+

PhonePC/2in1TabletTVWearable

off(type: SensorId.HALL, callback?: Callback<HallResponse>): void

取消订阅霍尔传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).HALL | 是 | 传感器类型，该值固定为SensorId.HALL。 |
| callback | Callback<[HallResponse](js-apis-sensor.md#hallresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback1(data: object) {
5. console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
6. }

8. function callback2(data: object) {
9. console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
10. }

12. // 使用try catch对可能出现的异常进行捕获
13. try {
14. sensor.on(sensor.SensorId.HALL, callback1);
15. sensor.on(sensor.SensorId.HALL, callback2);
16. // 仅取消callback1的注册
17. sensor.off(sensor.SensorId.HALL, callback1);
18. // 取消注册SensorId.HALL的所有回调
19. sensor.off(sensor.SensorId.HALL);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
23. }
```

### HALL19+

PhonePC/2in1TabletTVWearable

off(type: SensorId.HALL, sensorInfoParam?: SensorInfoParam, callback?: Callback<HallResponse>): void

取消订阅霍尔传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).HALL | 是 | 传感器类型，该值固定为SensorId.HALL。 |
| sensorInfoParam | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[HallResponse](js-apis-sensor.md#hallresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. enum Ret { OK, Failed = -1 }

6. // 传感器回调
7. const sensorCallback = (response: sensor.HallResponse) => {
8. console.info(`callback response: ${JSON.stringify(response)}`);
9. }
10. // 传感器监听类型
11. const sensorType = sensor.SensorId.HALL;
12. const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

14. function sensorSubscribe(): Ret {
15. let ret: Ret = Ret.OK;
16. // 使用try catch对可能出现的异常进行捕获
17. try {
18. // 查询所有的传感器
19. const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
20. if (!sensorList.length) {
21. return Ret.Failed;
22. }
23. // 根据实际业务逻辑获取目标传感器。
24. const targetSensor = sensorList
25. // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
26. .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
27. // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
28. .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
29. if (!targetSensor) {
30. return Ret.Failed;
31. }
32. sensorInfoParam.deviceId = targetSensor.deviceId;
33. sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
34. // 订阅传感器事件
35. sensor.on(sensorType, sensorCallback, { sensorInfoParam });
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
39. ret = Ret.Failed;
40. }
41. return ret;
42. }

44. function sensorUnsubscribe(): Ret {
45. let ret: Ret = Ret.OK;
46. // 使用try catch对可能出现的异常进行捕获
47. try {
48. sensor.off(sensorType, sensorInfoParam, sensorCallback);
49. } catch (error) {
50. let e: BusinessError = error as BusinessError;
51. console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
52. ret = Ret.Failed;
53. }
54. return ret;
55. }
```

### HEART\_RATE9+

PhonePC/2in1TabletTVWearable

off(type: SensorId.HEART\_RATE, callback?: Callback<HeartRateResponse>): void

取消订阅心率传感器数据。

**需要权限**：ohos.permission.READ\_HEALTH\_DATA

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).HEART\_RATE | 是 | 传感器类型，该值固定为SensorId.HEART\_RATE。 |
| callback | Callback<[HeartRateResponse](js-apis-sensor.md#heartrateresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback1(data: object) {
5. console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
6. }

8. function callback2(data: object) {
9. console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
10. }

12. // 使用try catch对可能出现的异常进行捕获
13. try {
14. sensor.on(sensor.SensorId.HEART_RATE, callback1);
15. sensor.on(sensor.SensorId.HEART_RATE, callback2);
16. // 仅取消callback1的注册
17. sensor.off(sensor.SensorId.HEART_RATE, callback1);
18. // 取消注册SensorId.HEART_RATE的所有回调
19. sensor.off(sensor.SensorId.HEART_RATE);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
23. }
```

### HEART\_RATE19+

PhonePC/2in1TabletTVWearable

off(type: SensorId.HEART\_RATE, sensorInfoParam?: SensorInfoParam, callback?: Callback<HeartRateResponse>): void

取消订阅心率传感器数据。

**需要权限**：ohos.permission.READ\_HEALTH\_DATA

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).HEART\_RATE | 是 | 传感器类型，该值固定为SensorId.HEART\_RATE。 |
| sensorInfoParam | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[HeartRateResponse](js-apis-sensor.md#heartrateresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. enum Ret { OK, Failed = -1 }

6. // 传感器回调
7. const sensorCallback = (response: sensor.HeartRateResponse) => {
8. console.info(`callback response: ${JSON.stringify(response)}`);
9. }
10. // 传感器监听类型
11. const sensorType = sensor.SensorId.HEART_RATE;
12. const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

14. function sensorSubscribe(): Ret {
15. let ret: Ret = Ret.OK;
16. // 使用try catch对可能出现的异常进行捕获
17. try {
18. // 查询所有的传感器
19. const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
20. if (!sensorList.length) {
21. return Ret.Failed;
22. }
23. // 根据实际业务逻辑获取目标传感器。
24. const targetSensor = sensorList
25. // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
26. .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
27. // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
28. .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
29. if (!targetSensor) {
30. return Ret.Failed;
31. }
32. sensorInfoParam.deviceId = targetSensor.deviceId;
33. sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
34. // 订阅传感器事件
35. sensor.on(sensorType, sensorCallback, { sensorInfoParam });
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
39. ret = Ret.Failed;
40. }
41. return ret;
42. }

44. function sensorUnsubscribe(): Ret {
45. let ret: Ret = Ret.OK;
46. // 使用try catch对可能出现的异常进行捕获
47. try {
48. sensor.off(sensorType, sensorInfoParam, sensorCallback);
49. } catch (error) {
50. let e: BusinessError = error as BusinessError;
51. console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
52. ret = Ret.Failed;
53. }
54. return ret;
55. }
```

### HUMIDITY9+

PhonePC/2in1TabletTVWearable

off(type: SensorId.HUMIDITY, callback?: Callback<HumidityResponse>): void

取消订阅湿度传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).HUMIDITY | 是 | 传感器类型，该值固定为SensorId.HUMIDITY。 |
| callback | Callback<[HumidityResponse](js-apis-sensor.md#humidityresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback1(data: object) {
5. console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
6. }

8. function callback2(data: object) {
9. console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
10. }

12. // 使用try catch对可能出现的异常进行捕获
13. try {
14. sensor.on(sensor.SensorId.HUMIDITY, callback1);
15. sensor.on(sensor.SensorId.HUMIDITY, callback2);
16. // 仅取消callback1的注册
17. sensor.off(sensor.SensorId.HUMIDITY, callback1);
18. // 取消注册SensorId.HUMIDITY的所有回调
19. sensor.off(sensor.SensorId.HUMIDITY);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
23. }
```

### HUMIDITY19+

PhonePC/2in1TabletTVWearable

off(type: SensorId.HUMIDITY, sensorInfoParam?: SensorInfoParam, callback?: Callback<HumidityResponse>): void

取消订阅湿度传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).HUMIDITY | 是 | 传感器类型，该值固定为SensorId.HUMIDITY。 |
| sensorInfoParam | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[HumidityResponse](js-apis-sensor.md#humidityresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. enum Ret { OK, Failed = -1 }

6. // 传感器回调
7. const sensorCallback = (response: sensor.HumidityResponse) => {
8. console.info(`callback response: ${JSON.stringify(response)}`);
9. }
10. // 传感器监听类型
11. const sensorType = sensor.SensorId.HUMIDITY;
12. const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

14. function sensorSubscribe(): Ret {
15. let ret: Ret = Ret.OK;
16. // 使用try catch对可能出现的异常进行捕获
17. try {
18. // 查询所有的传感器
19. const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
20. if (!sensorList.length) {
21. return Ret.Failed;
22. }
23. // 根据实际业务逻辑获取目标传感器。
24. const targetSensor = sensorList
25. // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
26. .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
27. // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
28. .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
29. if (!targetSensor) {
30. return Ret.Failed;
31. }
32. sensorInfoParam.deviceId = targetSensor.deviceId;
33. sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
34. // 订阅传感器事件
35. sensor.on(sensorType, sensorCallback, { sensorInfoParam });
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
39. ret = Ret.Failed;
40. }
41. return ret;
42. }

44. function sensorUnsubscribe(): Ret {
45. let ret: Ret = Ret.OK;
46. // 使用try catch对可能出现的异常进行捕获
47. try {
48. sensor.off(sensorType, sensorInfoParam, sensorCallback);
49. } catch (error) {
50. let e: BusinessError = error as BusinessError;
51. console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
52. ret = Ret.Failed;
53. }
54. return ret;
55. }
```

### LINEAR\_ACCELEROMETER9+

PhonePC/2in1TabletTVWearable

off(type: SensorId.LINEAR\_ACCELEROMETER, callback?: Callback<LinearAccelerometerResponse>): void

取消订阅线性加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).LINEAR\_ACCELEROMETER | 是 | 传感器类型，该值固定为SensorId.LINEAR\_ACCELERATION。 |
| callback | Callback<[LinearAccelerometerResponse](js-apis-sensor.md#linearaccelerometerresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback1(data: object) {
5. console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
6. }

8. function callback2(data: object) {
9. console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
10. }

12. // 使用try catch对可能出现的异常进行捕获
13. try {
14. sensor.on(sensor.SensorId.LINEAR_ACCELEROMETER, callback1);
15. sensor.on(sensor.SensorId.LINEAR_ACCELEROMETER, callback2);
16. // 仅取消callback1的注册
17. sensor.off(sensor.SensorId.LINEAR_ACCELEROMETER, callback1);
18. // 取消注册SensorId.LINEAR_ACCELEROMETER的所有回调
19. sensor.off(sensor.SensorId.LINEAR_ACCELEROMETER);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
23. }
```

### LINEAR\_ACCELEROMETER19+

PhonePC/2in1TabletTVWearable

off(type: SensorId.LINEAR\_ACCELEROMETER, sensorInfoParam?: SensorInfoParam, callback?: Callback<LinearAccelerometerResponse>): void

取消订阅线性加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).LINEAR\_ACCELEROMETER | 是 | 传感器类型，该值固定为SensorId.LINEAR\_ACCELERATION。 |
| sensorInfoParam | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[LinearAccelerometerResponse](js-apis-sensor.md#linearaccelerometerresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. enum Ret { OK, Failed = -1 }

6. // 传感器回调
7. const sensorCallback = (response: sensor.LinearAccelerometerResponse) => {
8. console.info(`callback response: ${JSON.stringify(response)}`);
9. }
10. // 传感器监听类型
11. const sensorType = sensor.SensorId.LINEAR_ACCELEROMETER;
12. const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

14. function sensorSubscribe(): Ret {
15. let ret: Ret = Ret.OK;
16. // 使用try catch对可能出现的异常进行捕获
17. try {
18. // 查询所有的传感器
19. const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
20. if (!sensorList.length) {
21. return Ret.Failed;
22. }
23. // 根据实际业务逻辑获取目标传感器。
24. const targetSensor = sensorList
25. // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
26. .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
27. // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
28. .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
29. if (!targetSensor) {
30. return Ret.Failed;
31. }
32. sensorInfoParam.deviceId = targetSensor.deviceId;
33. sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
34. // 订阅传感器事件
35. sensor.on(sensorType, sensorCallback, { sensorInfoParam });
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
39. ret = Ret.Failed;
40. }
41. return ret;
42. }

44. function sensorUnsubscribe(): Ret {
45. let ret: Ret = Ret.OK;
46. // 使用try catch对可能出现的异常进行捕获
47. try {
48. sensor.off(sensorType, sensorInfoParam, sensorCallback);
49. } catch (error) {
50. let e: BusinessError = error as BusinessError;
51. console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
52. ret = Ret.Failed;
53. }
54. return ret;
55. }
```

### MAGNETIC\_FIELD9+

PhonePC/2in1TabletTVWearable

off(type: SensorId.MAGNETIC\_FIELD, callback?: Callback<MagneticFieldResponse>): void

取消订阅磁场传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).MAGNETIC\_FIELD | 是 | 传感器类型，该值固定为SensorId.MAGNETIC\_FIELD。 |
| callback | Callback<[MagneticFieldResponse](js-apis-sensor.md#magneticfieldresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback1(data: object) {
5. console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
6. }

8. function callback2(data: object) {
9. console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
10. }

12. // 使用try catch对可能出现的异常进行捕获
13. try {
14. sensor.on(sensor.SensorId.MAGNETIC_FIELD, callback1);
15. sensor.on(sensor.SensorId.MAGNETIC_FIELD, callback2);
16. // 仅取消callback1的注册
17. sensor.off(sensor.SensorId.MAGNETIC_FIELD, callback1);
18. // 取消注册SensorId.MAGNETIC_FIELD的所有回调
19. sensor.off(sensor.SensorId.MAGNETIC_FIELD);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
23. }
```

### MAGNETIC\_FIELD19+

PhonePC/2in1TabletTVWearable

off(type: SensorId.MAGNETIC\_FIELD, sensorInfoParam?: SensorInfoParam, callback?: Callback<MagneticFieldResponse>): void

取消订阅磁场传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).MAGNETIC\_FIELD | 是 | 传感器类型，该值固定为SensorId.MAGNETIC\_FIELD。 |
| sensorInfoParam | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[MagneticFieldResponse](js-apis-sensor.md#magneticfieldresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. enum Ret { OK, Failed = -1 }

6. // 传感器回调
7. const sensorCallback = (response: sensor.MagneticFieldResponse) => {
8. console.info(`callback response: ${JSON.stringify(response)}`);
9. }
10. // 传感器监听类型
11. const sensorType = sensor.SensorId.MAGNETIC_FIELD;
12. const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

14. function sensorSubscribe(): Ret {
15. let ret: Ret = Ret.OK;
16. // 使用try catch对可能出现的异常进行捕获
17. try {
18. // 查询所有的传感器
19. const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
20. if (!sensorList.length) {
21. return Ret.Failed;
22. }
23. // 根据实际业务逻辑获取目标传感器。
24. const targetSensor = sensorList
25. // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
26. .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
27. // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
28. .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
29. if (!targetSensor) {
30. return Ret.Failed;
31. }
32. sensorInfoParam.deviceId = targetSensor.deviceId;
33. sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
34. // 订阅传感器事件
35. sensor.on(sensorType, sensorCallback, { sensorInfoParam });
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
39. ret = Ret.Failed;
40. }
41. return ret;
42. }

44. function sensorUnsubscribe(): Ret {
45. let ret: Ret = Ret.OK;
46. // 使用try catch对可能出现的异常进行捕获
47. try {
48. sensor.off(sensorType, sensorInfoParam, sensorCallback);
49. } catch (error) {
50. let e: BusinessError = error as BusinessError;
51. console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
52. ret = Ret.Failed;
53. }
54. return ret;
55. }
```

### MAGNETIC\_FIELD\_UNCALIBRATED9+

PhonePC/2in1TabletTVWearable

off(type: SensorId.MAGNETIC\_FIELD\_UNCALIBRATED, callback?: Callback<MagneticFieldUncalibratedResponse>): void

取消订阅未校准的磁场传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).MAGNETIC\_FIELD\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.MAGNETIC\_FIELD\_UNCALIBRATED。 |
| callback | Callback<[MagneticFieldUncalibratedResponse](js-apis-sensor.md#magneticfielduncalibratedresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback1(data: object) {
5. console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
6. }

8. function callback2(data: object) {
9. console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
10. }

12. // 使用try catch对可能出现的异常进行捕获
13. try {
14. sensor.on(sensor.SensorId.MAGNETIC_FIELD_UNCALIBRATED, callback1);
15. sensor.on(sensor.SensorId.MAGNETIC_FIELD_UNCALIBRATED, callback2);
16. // 仅取消callback1的注册
17. sensor.off(sensor.SensorId.MAGNETIC_FIELD_UNCALIBRATED, callback1);
18. // 取消注册SensorId.MAGNETIC_FIELD_UNCALIBRATED的所有回调
19. sensor.off(sensor.SensorId.MAGNETIC_FIELD_UNCALIBRATED);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
23. }
```

### MAGNETIC\_FIELD\_UNCALIBRATED19+

PhonePC/2in1TabletTVWearable

off(type: SensorId.MAGNETIC\_FIELD\_UNCALIBRATED, sensorInfoParam?: SensorInfoParam, callback?: Callback<MagneticFieldUncalibratedResponse>): void

取消订阅未校准的磁场传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).MAGNETIC\_FIELD\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.MAGNETIC\_FIELD\_UNCALIBRATED。 |
| sensorInfoParam | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[MagneticFieldUncalibratedResponse](js-apis-sensor.md#magneticfielduncalibratedresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. enum Ret { OK, Failed = -1 }

6. // 传感器回调
7. const sensorCallback = (response: sensor.MagneticFieldUncalibratedResponse) => {
8. console.info(`callback response: ${JSON.stringify(response)}`);
9. }
10. // 传感器监听类型
11. const sensorType = sensor.SensorId.MAGNETIC_FIELD_UNCALIBRATED;
12. const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

14. function sensorSubscribe(): Ret {
15. let ret: Ret = Ret.OK;
16. // 使用try catch对可能出现的异常进行捕获
17. try {
18. // 查询所有的传感器
19. const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
20. if (!sensorList.length) {
21. return Ret.Failed;
22. }
23. // 根据实际业务逻辑获取目标传感器。
24. const targetSensor = sensorList
25. // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
26. .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
27. // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
28. .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
29. if (!targetSensor) {
30. return Ret.Failed;
31. }
32. sensorInfoParam.deviceId = targetSensor.deviceId;
33. sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
34. // 订阅传感器事件
35. sensor.on(sensorType, sensorCallback, { sensorInfoParam });
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
39. ret = Ret.Failed;
40. }
41. return ret;
42. }

44. function sensorUnsubscribe(): Ret {
45. let ret: Ret = Ret.OK;
46. // 使用try catch对可能出现的异常进行捕获
47. try {
48. sensor.off(sensorType, sensorInfoParam, sensorCallback);
49. } catch (error) {
50. let e: BusinessError = error as BusinessError;
51. console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
52. ret = Ret.Failed;
53. }
54. return ret;
55. }
```

### ORIENTATION9+

PhonePC/2in1TabletTVWearable

off(type: SensorId.ORIENTATION, callback?: Callback<OrientationResponse>): void

取消订阅方向传感器数据。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).ORIENTATION | 是 | 传感器类型，该值固定为SensorId.ORIENTATION。 |
| callback | Callback<[OrientationResponse](js-apis-sensor.md#orientationresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback1(data: object) {
5. console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
6. }

8. function callback2(data: object) {
9. console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
10. }

12. // 使用try catch对可能出现的异常进行捕获
13. try {
14. sensor.on(sensor.SensorId.ORIENTATION, callback1);
15. sensor.on(sensor.SensorId.ORIENTATION, callback2);
16. // 仅取消callback1的注册
17. sensor.off(sensor.SensorId.ORIENTATION, callback1);
18. // 取消注册SensorId.ORIENTATION的所有回调
19. sensor.off(sensor.SensorId.ORIENTATION);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
23. }
```

### ORIENTATION19+

PhonePC/2in1TabletTVWearable

off(type: SensorId.ORIENTATION, sensorInfoParam?: SensorInfoParam, callback?: Callback<OrientationResponse>): void

取消订阅方向传感器数据。

**元服务API**：从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).ORIENTATION | 是 | 传感器类型，该值固定为SensorId.ORIENTATION。 |
| sensorInfoParam | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[OrientationResponse](js-apis-sensor.md#orientationresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. enum Ret { OK, Failed = -1 }

6. // 传感器回调
7. const sensorCallback = (response: sensor.OrientationResponse) => {
8. console.info(`callback response: ${JSON.stringify(response)}`);
9. }
10. // 传感器监听类型
11. const sensorType = sensor.SensorId.ORIENTATION;
12. const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

14. function sensorSubscribe(): Ret {
15. let ret: Ret = Ret.OK;
16. // 使用try catch对可能出现的异常进行捕获
17. try {
18. // 查询所有的传感器
19. const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
20. if (!sensorList.length) {
21. return Ret.Failed;
22. }
23. // 根据实际业务逻辑获取目标传感器。
24. const targetSensor = sensorList
25. // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
26. .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
27. // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
28. .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
29. if (!targetSensor) {
30. return Ret.Failed;
31. }
32. sensorInfoParam.deviceId = targetSensor.deviceId;
33. sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
34. // 订阅传感器事件
35. sensor.on(sensorType, sensorCallback, { sensorInfoParam });
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
39. ret = Ret.Failed;
40. }
41. return ret;
42. }

44. function sensorUnsubscribe(): Ret {
45. let ret: Ret = Ret.OK;
46. // 使用try catch对可能出现的异常进行捕获
47. try {
48. sensor.off(sensorType, sensorInfoParam, sensorCallback);
49. } catch (error) {
50. let e: BusinessError = error as BusinessError;
51. console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
52. ret = Ret.Failed;
53. }
54. return ret;
55. }
```

### PEDOMETER9+

PhonePC/2in1TabletTVWearable

off(type: SensorId.PEDOMETER, callback?: Callback<PedometerResponse>): void

取消订阅计步器传感器数据。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).PEDOMETER | 是 | 传感器类型，该值固定为SensorId.PEDOMETER。 |
| callback | Callback<[PedometerResponse](js-apis-sensor.md#pedometerresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback1(data: object) {
5. console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
6. }

8. function callback2(data: object) {
9. console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
10. }

12. // 使用try catch对可能出现的异常进行捕获
13. try {
14. sensor.on(sensor.SensorId.PEDOMETER, callback1);
15. sensor.on(sensor.SensorId.PEDOMETER, callback2);
16. // 仅取消callback1的注册
17. sensor.off(sensor.SensorId.PEDOMETER, callback1);
18. // 取消注册SensorId.PEDOMETER的所有回调
19. sensor.off(sensor.SensorId.PEDOMETER);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
23. }
```

### PEDOMETER19+

PhonePC/2in1TabletTVWearable

off(type: SensorId.PEDOMETER, sensorInfoParam?: SensorInfoParam, callback?: Callback<PedometerResponse>): void

取消订阅计步器传感器数据。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).PEDOMETER | 是 | 传感器类型，该值固定为SensorId.PEDOMETER。 |
| sensorInfoParam | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[PedometerResponse](js-apis-sensor.md#pedometerresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. enum Ret { OK, Failed = -1 }

6. // 传感器回调
7. const sensorCallback = (response: sensor.PedometerResponse) => {
8. console.info(`callback response: ${JSON.stringify(response)}`);
9. }
10. // 传感器监听类型
11. const sensorType = sensor.SensorId.PEDOMETER;
12. const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

14. function sensorSubscribe(): Ret {
15. let ret: Ret = Ret.OK;
16. // 使用try catch对可能出现的异常进行捕获
17. try {
18. // 查询所有的传感器
19. const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
20. if (!sensorList.length) {
21. return Ret.Failed;
22. }
23. // 根据实际业务逻辑获取目标传感器。
24. const targetSensor = sensorList
25. // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
26. .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
27. // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
28. .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
29. if (!targetSensor) {
30. return Ret.Failed;
31. }
32. sensorInfoParam.deviceId = targetSensor.deviceId;
33. sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
34. // 订阅传感器事件
35. sensor.on(sensorType, sensorCallback, { sensorInfoParam });
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
39. ret = Ret.Failed;
40. }
41. return ret;
42. }

44. function sensorUnsubscribe(): Ret {
45. let ret: Ret = Ret.OK;
46. // 使用try catch对可能出现的异常进行捕获
47. try {
48. sensor.off(sensorType, sensorInfoParam, sensorCallback);
49. } catch (error) {
50. let e: BusinessError = error as BusinessError;
51. console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
52. ret = Ret.Failed;
53. }
54. return ret;
55. }
```

### PEDOMETER\_DETECTION9+

PhonePC/2in1TabletTVWearable

off(type: SensorId.PEDOMETER\_DETECTION, callback?: Callback<PedometerDetectionResponse>): void

取消订阅计步检测器传感器数据。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).PEDOMETER\_DETECTION | 是 | 传感器类型，该值固定为SensorId.PEDOMETER\_DETECTION。 |
| callback | Callback<[PedometerDetectionResponse](js-apis-sensor.md#pedometerdetectionresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback1(data: object) {
5. console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
6. }

8. function callback2(data: object) {
9. console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
10. }

12. // 使用try catch对可能出现的异常进行捕获
13. try {
14. sensor.on(sensor.SensorId.PEDOMETER_DETECTION, callback1);
15. sensor.on(sensor.SensorId.PEDOMETER_DETECTION, callback2);
16. // 仅取消callback1的注册
17. sensor.off(sensor.SensorId.PEDOMETER_DETECTION, callback1);
18. // 取消注册SensorId.PEDOMETER_DETECTION的所有回调
19. sensor.off(sensor.SensorId.PEDOMETER_DETECTION);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
23. }
```

### PEDOMETER\_DETECTION19+

PhonePC/2in1TabletTVWearable

off(type: SensorId.PEDOMETER\_DETECTION, sensorInfoParam?: SensorInfoParam, callback?: Callback<PedometerDetectionResponse>): void

取消订阅计步检测器传感器数据。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).PEDOMETER\_DETECTION | 是 | 传感器类型，该值固定为SensorId.PEDOMETER\_DETECTION。 |
| sensorInfoParam | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[PedometerDetectionResponse](js-apis-sensor.md#pedometerdetectionresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. enum Ret { OK, Failed = -1 }

6. // 传感器回调
7. const sensorCallback = (response: sensor.PedometerDetectionResponse) => {
8. console.info(`callback response: ${JSON.stringify(response)}`);
9. }
10. // 传感器监听类型
11. const sensorType = sensor.SensorId.PEDOMETER_DETECTION;
12. const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

14. function sensorSubscribe(): Ret {
15. let ret: Ret = Ret.OK;
16. // 使用try catch对可能出现的异常进行捕获
17. try {
18. // 查询所有的传感器
19. const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
20. if (!sensorList.length) {
21. return Ret.Failed;
22. }
23. // 根据实际业务逻辑获取目标传感器。
24. const targetSensor = sensorList
25. // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
26. .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
27. // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
28. .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
29. if (!targetSensor) {
30. return Ret.Failed;
31. }
32. sensorInfoParam.deviceId = targetSensor.deviceId;
33. sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
34. // 订阅传感器事件
35. sensor.on(sensorType, sensorCallback, { sensorInfoParam });
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
39. ret = Ret.Failed;
40. }
41. return ret;
42. }

44. function sensorUnsubscribe(): Ret {
45. let ret: Ret = Ret.OK;
46. // 使用try catch对可能出现的异常进行捕获
47. try {
48. sensor.off(sensorType, sensorInfoParam, sensorCallback);
49. } catch (error) {
50. let e: BusinessError = error as BusinessError;
51. console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
52. ret = Ret.Failed;
53. }
54. return ret;
55. }
```

### PROXIMITY9+

PhonePC/2in1TabletTVWearable

off(type: SensorId.PROXIMITY, callback?: Callback<ProximityResponse>): void

取消订阅接近光传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).PROXIMITY | 是 | 传感器类型，该值固定为SensorId.PROXIMITY。 |
| callback | Callback<[ProximityResponse](js-apis-sensor.md#proximityresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback1(data: object) {
5. console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
6. }

8. function callback2(data: object) {
9. console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
10. }

12. // 使用try catch对可能出现的异常进行捕获
13. try {
14. sensor.on(sensor.SensorId.PROXIMITY, callback1);
15. sensor.on(sensor.SensorId.PROXIMITY, callback2);
16. // 仅取消callback1的注册
17. sensor.off(sensor.SensorId.PROXIMITY, callback1);
18. // 取消注册SensorId.PROXIMITY的所有回调
19. sensor.off(sensor.SensorId.PROXIMITY);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
23. }
```

### PROXIMITY19+

PhonePC/2in1TabletTVWearable

off(type: SensorId.PROXIMITY, sensorInfoParam?: SensorInfoParam, callback?: Callback<ProximityResponse>): void

取消订阅接近光传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).PROXIMITY | 是 | 传感器类型，该值固定为SensorId.PROXIMITY。 |
| sensorInfoParam | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[ProximityResponse](js-apis-sensor.md#proximityresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. enum Ret { OK, Failed = -1 }

6. // 传感器回调
7. const sensorCallback = (response: sensor.ProximityResponse) => {
8. console.info(`callback response: ${JSON.stringify(response)}`);
9. }
10. // 传感器监听类型
11. const sensorType = sensor.SensorId.PROXIMITY;
12. const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

14. function sensorSubscribe(): Ret {
15. let ret: Ret = Ret.OK;
16. // 使用try catch对可能出现的异常进行捕获
17. try {
18. // 查询所有的传感器
19. const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
20. if (!sensorList.length) {
21. return Ret.Failed;
22. }
23. // 根据实际业务逻辑获取目标传感器。
24. const targetSensor = sensorList
25. // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
26. .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
27. // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
28. .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
29. if (!targetSensor) {
30. return Ret.Failed;
31. }
32. sensorInfoParam.deviceId = targetSensor.deviceId;
33. sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
34. // 订阅传感器事件
35. sensor.on(sensorType, sensorCallback, { sensorInfoParam });
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
39. ret = Ret.Failed;
40. }
41. return ret;
42. }

44. function sensorUnsubscribe(): Ret {
45. let ret: Ret = Ret.OK;
46. // 使用try catch对可能出现的异常进行捕获
47. try {
48. sensor.off(sensorType, sensorInfoParam, sensorCallback);
49. } catch (error) {
50. let e: BusinessError = error as BusinessError;
51. console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
52. ret = Ret.Failed;
53. }
54. return ret;
55. }
```

### ROTATION\_VECTOR9+

PhonePC/2in1TabletTVWearable

off(type: SensorId.ROTATION\_VECTOR, callback?: Callback<RotationVectorResponse>): void

取消订阅旋转矢量传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).ROTATION\_VECTOR | 是 | 传感器类型，该值固定为SensorId.ROTATION\_VECTOR。 |
| callback | Callback<[RotationVectorResponse](js-apis-sensor.md#rotationvectorresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback1(data: object) {
5. console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
6. }

8. function callback2(data: object) {
9. console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
10. }

12. // 使用try catch对可能出现的异常进行捕获
13. try {
14. sensor.on(sensor.SensorId.ROTATION_VECTOR, callback1);
15. sensor.on(sensor.SensorId.ROTATION_VECTOR, callback2);
16. // 仅取消callback1的注册
17. sensor.off(sensor.SensorId.ROTATION_VECTOR, callback1);
18. // 取消注册SensorId.ROTATION_VECTOR的所有回调
19. sensor.off(sensor.SensorId.ROTATION_VECTOR);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
23. }
```

### ROTATION\_VECTOR19+

PhonePC/2in1TabletTVWearable

off(type: SensorId.ROTATION\_VECTOR, sensorInfoParam?: SensorInfoParam, callback?: Callback<RotationVectorResponse>): void

取消订阅旋转矢量传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).ROTATION\_VECTOR | 是 | 传感器类型，该值固定为SensorId.ROTATION\_VECTOR。 |
| sensorInfoParam | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[RotationVectorResponse](js-apis-sensor.md#rotationvectorresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. enum Ret { OK, Failed = -1 }

6. // 传感器回调
7. const sensorCallback = (response: sensor.RotationVectorResponse) => {
8. console.info(`callback response: ${JSON.stringify(response)}`);
9. }
10. // 传感器监听类型
11. const sensorType = sensor.SensorId.ROTATION_VECTOR;
12. const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

14. function sensorSubscribe(): Ret {
15. let ret: Ret = Ret.OK;
16. // 使用try catch对可能出现的异常进行捕获
17. try {
18. // 查询所有的传感器
19. const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
20. if (!sensorList.length) {
21. return Ret.Failed;
22. }
23. // 根据实际业务逻辑获取目标传感器。
24. const targetSensor = sensorList
25. // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
26. .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
27. // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
28. .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
29. if (!targetSensor) {
30. return Ret.Failed;
31. }
32. sensorInfoParam.deviceId = targetSensor.deviceId;
33. sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
34. // 订阅传感器事件
35. sensor.on(sensorType, sensorCallback, { sensorInfoParam });
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
39. ret = Ret.Failed;
40. }
41. return ret;
42. }

44. function sensorUnsubscribe(): Ret {
45. let ret: Ret = Ret.OK;
46. // 使用try catch对可能出现的异常进行捕获
47. try {
48. sensor.off(sensorType, sensorInfoParam, sensorCallback);
49. } catch (error) {
50. let e: BusinessError = error as BusinessError;
51. console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
52. ret = Ret.Failed;
53. }
54. return ret;
55. }
```

### SIGNIFICANT\_MOTION9+

PhonePC/2in1TabletTVWearable

off(type: SensorId.SIGNIFICANT\_MOTION, callback?: Callback<SignificantMotionResponse>): void

取消订阅有效运动传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).SIGNIFICANT\_MOTION | 是 | 传感器类型，该值固定为SensorId.SIGNIFICANT\_MOTION。 |
| callback | Callback<[SignificantMotionResponse](js-apis-sensor.md#significantmotionresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback1(data: object) {
5. console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
6. }

8. function callback2(data: object) {
9. console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
10. }

12. // 使用try catch对可能出现的异常进行捕获
13. try {
14. sensor.on(sensor.SensorId.SIGNIFICANT_MOTION, callback1);
15. sensor.on(sensor.SensorId.SIGNIFICANT_MOTION, callback2);
16. // 仅取消callback1的注册
17. sensor.off(sensor.SensorId.SIGNIFICANT_MOTION, callback1);
18. // 取消注册SensorId.SIGNIFICANT_MOTION的所有回调
19. sensor.off(sensor.SensorId.SIGNIFICANT_MOTION);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
23. }
```

### SIGNIFICANT\_MOTION19+

PhonePC/2in1TabletTVWearable

off(type: SensorId.SIGNIFICANT\_MOTION, sensorInfoParam?: SensorInfoParam, callback?: Callback<SignificantMotionResponse>): void

取消订阅有效运动传感器数据。

**系统能力**:SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).SIGNIFICANT\_MOTION | 是 | 传感器类型，该值固定为SensorId.SIGNIFICANT\_MOTION。 |
| sensorInfoParam | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[SignificantMotionResponse](js-apis-sensor.md#significantmotionresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. enum Ret { OK, Failed = -1 }

6. // 传感器回调
7. const sensorCallback = (response: sensor.SignificantMotionResponse) => {
8. console.info(`callback response: ${JSON.stringify(response)}`);
9. }
10. // 传感器监听类型
11. const sensorType = sensor.SensorId.SIGNIFICANT_MOTION;
12. const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

14. function sensorSubscribe(): Ret {
15. let ret: Ret = Ret.OK;
16. // 使用try catch对可能出现的异常进行捕获
17. try {
18. // 查询所有的传感器
19. const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
20. if (!sensorList.length) {
21. return Ret.Failed;
22. }
23. // 根据实际业务逻辑获取目标传感器。
24. const targetSensor = sensorList
25. // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
26. .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
27. // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
28. .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
29. if (!targetSensor) {
30. return Ret.Failed;
31. }
32. sensorInfoParam.deviceId = targetSensor.deviceId;
33. sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
34. // 订阅传感器事件
35. sensor.on(sensorType, sensorCallback, { sensorInfoParam });
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
39. ret = Ret.Failed;
40. }
41. return ret;
42. }

44. function sensorUnsubscribe(): Ret {
45. let ret: Ret = Ret.OK;
46. // 使用try catch对可能出现的异常进行捕获
47. try {
48. sensor.off(sensorType, sensorInfoParam, sensorCallback);
49. } catch (error) {
50. let e: BusinessError = error as BusinessError;
51. console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
52. ret = Ret.Failed;
53. }
54. return ret;
55. }
```

### WEAR\_DETECTION9+

PhonePC/2in1TabletTVWearable

off(type: SensorId.WEAR\_DETECTION, callback?: Callback<WearDetectionResponse>): void

取消订阅佩戴检测传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).WEAR\_DETECTION | 是 | 传感器类型，该值固定为SensorId.WEAR\_DETECTION。 |
| callback | Callback<[WearDetectionResponse](js-apis-sensor.md#weardetectionresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback1(data: object) {
5. console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
6. }

8. function callback2(data: object) {
9. console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
10. }

12. // 使用try catch对可能出现的异常进行捕获
13. try {
14. sensor.on(sensor.SensorId.WEAR_DETECTION, callback1);
15. sensor.on(sensor.SensorId.WEAR_DETECTION, callback2);
16. // 仅取消callback1的注册
17. sensor.off(sensor.SensorId.WEAR_DETECTION, callback1);
18. // 取消注册SensorId.WEAR_DETECTION的所有回调
19. sensor.off(sensor.SensorId.WEAR_DETECTION);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
23. }
```

### WEAR\_DETECTION19+

PhonePC/2in1TabletTVWearable

off(type: SensorId.WEAR\_DETECTION, sensorInfoParam?: SensorInfoParam, callback?: Callback<WearDetectionResponse>): void

取消订阅佩戴检测传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9).WEAR\_DETECTION | 是 | 传感器类型，该值固定为SensorId.WEAR\_DETECTION。 |
| sensorInfoParam | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[WearDetectionResponse](js-apis-sensor.md#weardetectionresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. enum Ret { OK, Failed = -1 }

6. // 传感器回调
7. const sensorCallback = (response: sensor.WearDetectionResponse) => {
8. console.info(`callback response: ${JSON.stringify(response)}`);
9. }
10. // 传感器监听类型
11. const sensorType = sensor.SensorId.WEAR_DETECTION;
12. const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

14. function sensorSubscribe(): Ret {
15. let ret: Ret = Ret.OK;
16. // 使用try catch对可能出现的异常进行捕获
17. try {
18. // 查询所有的传感器
19. const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
20. if (!sensorList.length) {
21. return Ret.Failed;
22. }
23. // 根据实际业务逻辑获取目标传感器。
24. const targetSensor = sensorList
25. // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
26. .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
27. // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
28. .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
29. if (!targetSensor) {
30. return Ret.Failed;
31. }
32. sensorInfoParam.deviceId = targetSensor.deviceId;
33. sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
34. // 订阅传感器事件
35. sensor.on(sensorType, sensorCallback, { sensorInfoParam });
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
39. ret = Ret.Failed;
40. }
41. return ret;
42. }

44. function sensorUnsubscribe(): Ret {
45. let ret: Ret = Ret.OK;
46. // 使用try catch对可能出现的异常进行捕获
47. try {
48. sensor.off(sensorType, sensorInfoParam, sensorCallback);
49. } catch (error) {
50. let e: BusinessError = error as BusinessError;
51. console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
52. ret = Ret.Failed;
53. }
54. return ret;
55. }
```

### sensorStatusChange19+

PhonePC/2in1TabletTVWearable

off(type: 'sensorStatusChange', callback?: Callback<SensorStatusEvent>): void

取消监听传感器变化。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'sensorStatusChange' | 是 | 固定传入'sensorStatusChange',状态监听固定参数。 |
| callback | Callback<[SensorStatusEvent](js-apis-sensor.md#sensorstatusevent19)> | 否 | sensor.on传入的回调函数，不传则取消所有监听。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. const statusChangeCallback = (data: sensor.SensorStatusEvent) => {
7. console.info('sensorStatusChange : ' + JSON.stringify(data));
8. }
9. const statusChangeCallback2 = (data: sensor.SensorStatusEvent) => {
10. console.info('sensorStatusChange2 : ' + JSON.stringify(data));
11. }
12. // 注册两个设备上线消息监听回调
13. sensor.on('sensorStatusChange', statusChangeCallback);
14. sensor.on('sensorStatusChange', statusChangeCallback2);

16. // 3秒后注销第一个监听
17. setTimeout(() => {
18. sensor.off('sensorStatusChange', statusChangeCallback);
19. }, 3000);
20. // 5秒后注销所有监听
21. setTimeout(() => {
22. sensor.off('sensorStatusChange');
23. }, 5000);
24. } catch (error) {
25. let e: BusinessError = error as BusinessError;
26. console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
27. }
```

## sensor.getSensorListByDeviceSync19+

PhonePC/2in1TabletTVWearable

getSensorListByDeviceSync(deviceId?: number): Array<Sensor>

同步获取设备的所有传感器信息。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 否 | 设备ID，默认为查询本地设备，默认值为-1，表示本地设备，设备ID需通过[getSensorList](js-apis-sensor.md#sensorgetsensorlist9)查询或者监听设备上下线接口[sensorStatusChange](js-apis-sensor.md#sensorstatuschange19)获取。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Array<[Sensor](js-apis-sensor.md#sensor9)> | 传感器属性列表。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. const deviceId = 1;
6. // 第一个参数deviceId 非必填
7. const sensorList: sensor.Sensor[] = sensor.getSensorListByDeviceSync(deviceId);
8. console.info(`sensorList length: ${sensorList.length}`);
9. console.info(`sensorList: ${JSON.stringify(sensorList)}`);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. console.error(`Failed to get sensorList. Code: ${e.code}, message: ${e.message}`);
13. }
```

## sensor.getSingleSensorByDeviceSync19+

PhonePC/2in1TabletTVWearable

getSingleSensorByDeviceSync(type: SensorId, deviceId?: number): Array<Sensor>

同步获取指定设备和类型的传感器信息。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9) | 是 | 指定传感器类型。 |
| deviceId | number | 否 | 设备ID，默认为查询本地设备，默认值为-1，表示本地设备，设备ID需通过[getSensorList](js-apis-sensor.md#sensorgetsensorlist9)查询或者监听设备上下线接口[sensorStatusChange](js-apis-sensor.md#sensorstatuschange19)获取。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Array<[Sensor](js-apis-sensor.md#sensor9)> | 传感器属性列表。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. const deviceId = 1;
6. // 第二个参数deviceId 非必填
7. const sensorList: sensor.Sensor[] = sensor.getSingleSensorByDeviceSync(sensor.SensorId.ACCELEROMETER, deviceId);
8. console.info(`sensorList length: ${sensorList.length}`);
9. console.info(`sensorList Json: ${JSON.stringify(sensorList)}`);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. console.error(`Failed to get sensorList. Code: ${e.code}, message: ${e.message}`);
13. }
```

## sensor.getGeomagneticInfo9+

PhonePC/2in1TabletTVWearable

getGeomagneticInfo(locationOptions: LocationOptions, timeMillis: number, callback: AsyncCallback<GeomagneticResponse>): void

获取某时刻地球上特定位置的地磁场信息，使用Callback异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locationOptions | [LocationOptions](js-apis-sensor.md#locationoptions) | 是 | 地理位置，包括经度、纬度和海拔高度。 |
| timeMillis | number | 是 | 获取磁偏角的时间，unix时间戳，单位毫秒。 |
| callback | AsyncCallback<[GeomagneticResponse](js-apis-sensor.md#geomagneticresponse)> | 是 | 回调函数，异步返回地磁场信息。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.getGeomagneticInfo({ latitude: 80, longitude: 0, altitude: 0 }, 1580486400000,
7. (err: BusinessError, data: sensor.GeomagneticResponse) => {
8. if (err) {
9. console.error(`Failed to get geomagneticInfo. Code: ${err.code}, message: ${err.message}`);
10. return;
11. }
12. console.info("Succeeded in getting geomagneticInfo x" + data.x);
13. console.info("Succeeded in getting geomagneticInfo y" + data.y);
14. console.info("Succeeded in getting geomagneticInfo z" + data.z);
15. console.info("Succeeded in getting geomagneticInfo geomagneticDip" + data.geomagneticDip);
16. console.info("Succeeded in getting geomagneticInfo deflectionAngle" + data.deflectionAngle);
17. console.info("Succeeded in getting geomagneticInfo levelIntensity" + data.levelIntensity);
18. console.info("Succeeded in getting geomagneticInfo totalIntensity" + data.totalIntensity);
19. });
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to get geomagneticInfo. Code: ${e.code}, message: ${e.message}`);
23. }
```

## sensor.getGeomagneticInfo9+

PhonePC/2in1TabletTVWearable

getGeomagneticInfo(locationOptions: LocationOptions, timeMillis: number): Promise<GeomagneticResponse>

获取某时刻地球上特定位置的地磁场信息，使用Promise异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locationOptions | [LocationOptions](js-apis-sensor.md#locationoptions) | 是 | 地理位置，包括经度、纬度和海拔高度。 |
| timeMillis | number | 是 | 获取磁偏角的时间，unix时间戳，单位毫秒。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[GeomagneticResponse](js-apis-sensor.md#geomagneticresponse)> | Promise对象，使用异步方式返回地磁场信息。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. const promise = sensor.getGeomagneticInfo({ latitude: 80, longitude: 0, altitude: 0 }, 1580486400000);
7. promise.then((data: sensor.GeomagneticResponse) => {
8. console.info("Succeeded in getting geomagneticInfo x" + data.x);
9. console.info("Succeeded in getting geomagneticInfo y" + data.y);
10. console.info("Succeeded in getting geomagneticInfo z" + data.z);
11. console.info("Succeeded in getting geomagneticInfo geomagneticDip" + data.geomagneticDip);
12. console.info("Succeeded in getting geomagneticInfo deflectionAngle" + data.deflectionAngle);
13. console.info("Succeeded in getting geomagneticInfo levelIntensity" + data.levelIntensity);
14. console.info("Succeeded in getting geomagneticInfo totalIntensity" + data.totalIntensity);
15. }, (err: BusinessError) => {
16. console.error(`Failed to get geomagneticInfo. Code: ${err.code}, message: ${err.message}`);
17. });
18. } catch (error) {
19. let e: BusinessError = error as BusinessError;
20. console.error(`Failed to get geomagneticInfo. Code: ${e.code}, message: ${e.message}`);
21. }
```

## sensor.getDeviceAltitude9+

PhonePC/2in1TabletTVWearable

getDeviceAltitude(seaPressure: number, currentPressure: number, callback: AsyncCallback<number>): void

根据气压值获取海拔高度，使用Callback异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| seaPressure | number | 是 | 海平面气压值，单位为hPa。 |
| currentPressure | number | 是 | 指定的气压值，单位为hPa。 |
| callback | AsyncCallback<number> | 是 | 回调函数，异步返回指定的气压值对应的海拔高度，单位为米。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. let seaPressure = 1013.2;
7. let currentPressure = 1500.0;
8. sensor.getDeviceAltitude(seaPressure, currentPressure, (err: BusinessError, data: number) => {
9. if (err) {
10. console.error(`Failed to get altitude. Code: ${err.code}, message: ${err.message}`);
11. return;
12. }
13. console.info('Succeeded in getting altitude: ' + data);
14. });
15. } catch (error) {
16. let e: BusinessError = error as BusinessError;
17. console.error(`Failed to get altitude. Code: ${e.code}, message: ${e.message}`);
18. }
```

## sensor.getDeviceAltitude9+

PhonePC/2in1TabletTVWearable

getDeviceAltitude(seaPressure: number, currentPressure: number): Promise<number>

根据气压值获取海拔高度，使用Promise异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| seaPressure | number | 是 | 海平面气压值，单位为hPa。 |
| currentPressure | number | 是 | 指定的气压值，单位为hPa。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，使用异步方式返回指定的气压值对应的海拔高度，单位为米。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. let seaPressure = 1013.2;
7. let currentPressure = 1500.0;
8. const promise = sensor.getDeviceAltitude(seaPressure, currentPressure);
9. promise.then((data: number) => {
10. console.info('Succeeded in getting sensor_getDeviceAltitude_Promise', data);
11. }, (err: BusinessError) => {
12. console.error(`Failed to get altitude. Code: ${err.code}, message: ${err.message}`);
13. });
14. } catch (error) {
15. let e: BusinessError = error as BusinessError;
16. console.error(`Failed to get altitude. Code: ${e.code}, message: ${e.message}`);
17. }
```

## sensor.getInclination9+

PhonePC/2in1TabletTVWearable

getInclination(inclinationMatrix: Array<number>, callback: AsyncCallback<number>): void

根据倾斜矩阵计算地磁倾角，使用Callback异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inclinationMatrix | Array<number> | 是 | 倾斜矩阵。 |
| callback | AsyncCallback<number> | 是 | 回调函数，异步返回地磁倾角，单位为弧度。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. // inclinationMatrix可以为3*3，或者4*4
7. let inclinationMatrix = [
8. 1, 0, 0,
9. 0, 1, 0,
10. 0, 0, 1
11. ]
12. sensor.getInclination(inclinationMatrix, (err: BusinessError, data: number) => {
13. if (err) {
14. console.error(`Failed to get inclination. Code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. console.info('Succeeded in getting inclination: ' + data);
18. })
19. } catch (error) {
20. let e: BusinessError = error as BusinessError;
21. console.error(`Failed to get inclination. Code: ${e.code}, message: ${e.message}`);
22. }
```

## sensor.getInclination9+

PhonePC/2in1TabletTVWearable

getInclination(inclinationMatrix: Array<number>): Promise<number>

根据倾斜矩阵计算地磁倾角，使用Promise异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inclinationMatrix | Array<number> | 是 | 倾斜矩阵。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，使用异步方式返回地磁倾斜角，单位为弧度。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. // inclinationMatrix可以为3*3，或者4*4
7. let inclinationMatrix = [
8. 1, 0, 0,
9. 0, 1, 0,
10. 0, 0, 1
11. ]
12. const promise = sensor.getInclination(inclinationMatrix);
13. promise.then((data: number) => {
14. console.info('Succeeded in getting inclination: ' + data);
15. }, (err: BusinessError) => {
16. console.error(`Failed to get inclination. Code: ${err.code}, message: ${err.message}`);
17. });
18. } catch (error) {
19. let e: BusinessError = error as BusinessError;
20. console.error(`Failed to get inclination. Code: ${e.code}, message: ${e.message}`);
21. }
```

## sensor.getAngleVariation9+

PhonePC/2in1TabletTVWearable

getAngleVariation(currentRotationMatrix: Array<number>, preRotationMatrix: Array<number>, callback: AsyncCallback<Array<number>>): void

计算两个旋转矩阵之间的角度变化，使用Callback异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| currentRotationMatrix | Array<number> | 是 | 当前旋转矩阵。 |
| preRotationMatrix | Array<number> | 是 | 相对旋转矩阵。 |
| callback | AsyncCallback<Array<number>> | 是 | 回调函数，异步返回绕z、x、y轴方向的旋转角度，单位度（°）。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. // 旋转矩阵可以为3*3，或者4*4
7. let currentRotationMatrix = [
8. 1, 0, 0,
9. 0, 1, 0,
10. 0, 0, 1
11. ];
12. let preRotationMatrix = [
13. 1, 0, 0,
14. 0, 0.87, -0.50,
15. 0, 0.50, 0.87
16. ];
17. sensor.getAngleVariation(currentRotationMatrix, preRotationMatrix, (err: BusinessError, data: Array<number>) => {
18. if (err) {
19. console.error(`Failed to get angle variation. Code: ${err.code}, message: ${err.message}`);
20. return;
21. }
22. if (data.length < 3) {
23. console.error("Failed to get angle variation, length" + data.length);
24. return;
25. }
26. console.info("Z: " + data[0]);
27. console.info("X: " + data[1]);
28. console.info("Y: " + data[2]);
29. })
30. } catch (error) {
31. let e: BusinessError = error as BusinessError;
32. console.error(`Failed to get angle variation. Code: ${e.code}, message: ${e.message}`);
33. }
```

## sensor.getAngleVariation9+

PhonePC/2in1TabletTVWearable

getAngleVariation(currentRotationMatrix: Array<number>, preRotationMatrix: Array<number>): Promise<Array<number>>

得到两个旋转矩阵之间的角度变化，使用Promise异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| currentRotationMatrix | Array<number> | 是 | 当前旋转矩阵。 |
| preRotationMatrix | Array<number> | 是 | 相对旋转矩阵。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，使用异步方式返回绕z、x、y轴方向的旋转角度，单位度（°）。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. // 旋转矩阵可以为3*3，或者4*4
7. let currentRotationMatrix = [
8. 1, 0, 0,
9. 0, 1, 0,
10. 0, 0, 1
11. ];
12. let preRotationMatrix = [
13. 1, 0, 0,
14. 0, 0.87, -0.50,
15. 0, 0.50, 0.87
16. ];
17. const promise = sensor.getAngleVariation(currentRotationMatrix, preRotationMatrix);
18. promise.then((data: Array<number>) => {
19. if (data.length < 3) {
20. console.error("Failed to get angle variation, length" + data.length);
21. return;
22. }
23. console.info("Z: " + data[0]);
24. console.info("X: " + data[1]);
25. console.info("Y: " + data[2]);
26. }, (err: BusinessError) => {
27. console.error(`Failed to get angle variation. Code: ${err.code}, message: ${err.message}`);
28. });
29. } catch (error) {
30. let e: BusinessError = error as BusinessError;
31. console.error(`Failed to get angle variation. Code: ${e.code}, message: ${e.message}`);
32. }
```

## sensor.getRotationMatrix9+

PhonePC/2in1TabletTVWearable

getRotationMatrix(rotationVector: Array<number>, callback: AsyncCallback<Array<number>>): void

根据旋转矢量获取旋转矩阵，使用Callback异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotationVector | Array<number> | 是 | 旋转矢量。 |
| callback | AsyncCallback<Array<number>> | 是 | 回调函数，异步返回3\*3旋转矩阵。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. let rotationVector = [0.20046076, 0.21907, 0.73978853, 0.60376877];
7. sensor.getRotationMatrix(rotationVector, (err: BusinessError, data: Array<number>) => {
8. if (err) {
9. console.error(`Failed to get rotationMatrix. Code: ${err.code}, message: ${err.message}`);
10. return;
11. }
12. for (let i = 0; i < data.length; i++) {
13. console.info('Succeeded in getting data[' + i + ']: ' + data[i]);
14. }
15. })
16. } catch (error) {
17. let e: BusinessError = error as BusinessError;
18. console.error(`Failed to get rotationMatrix. Code: ${e.code}, message: ${e.message}`);
19. }
```

## sensor.getRotationMatrix9+

PhonePC/2in1TabletTVWearable

getRotationMatrix(rotationVector: Array<number>): Promise<Array<number>>

根据旋转矢量获取旋转矩阵，使用Promise异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotationVector | Array<number> | 是 | 旋转矢量。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，使用异步方式返回旋转矩阵。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. let rotationVector = [0.20046076, 0.21907, 0.73978853, 0.60376877];
7. const promise = sensor.getRotationMatrix(rotationVector);
8. promise.then((data: Array<number>) => {
9. for (let i = 0; i < data.length; i++) {
10. console.info('Succeeded in getting data[' + i + ']: ' + data[i]);
11. }
12. }, (err: BusinessError) => {
13. console.error(`Failed to get rotationMatrix. Code: ${err.code}, message: ${err.message}`);
14. });
15. } catch (error) {
16. let e: BusinessError = error as BusinessError;
17. console.error(`Failed to get rotationMatrix. Code: ${e.code}, message: ${e.message}`);
18. }
```

## sensor.transformRotationMatrix9+

PhonePC/2in1TabletTVWearable

transformRotationMatrix(inRotationVector: Array<number>, coordinates: CoordinatesOptions, callback: AsyncCallback<Array<number>>): void

根据指定坐标系映射旋转矩阵，使用Callback异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inRotationVector | Array<number> | 是 | 旋转矩阵。 |
| coordinates | [CoordinatesOptions](js-apis-sensor.md#coordinatesoptions) | 是 | 指定坐标系方向。 |
| callback | AsyncCallback<Array<number>> | 是 | 回调函数，异步返回映射后的旋转矩阵。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. let rotationMatrix = [
7. 1, 0, 0,
8. 0, 0.87, -0.50,
9. 0, 0.50, 0.87
10. ];
11. sensor.transformRotationMatrix(rotationMatrix, { x: 1, y: 3 }, (err: BusinessError, data: Array<number>) => {
12. if (err) {
13. console.error(`Failed to transform rotationMatrix. Code: ${err.code}, message: ${err.message}`);
14. return;
15. }
16. for (let i = 0; i < data.length; i++) {
17. console.info('Succeeded in getting data[' + i + '] = ' + data[i]);
18. }
19. })
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. console.error(`Failed to transform rotationMatrix. Code: ${e.code}, message: ${e.message}`);
23. }
```

## sensor.transformRotationMatrix9+

PhonePC/2in1TabletTVWearable

transformRotationMatrix(inRotationVector: Array<number>, coordinates: CoordinatesOptions): Promise<Array<number>>

根据指定坐标系映射旋转矩阵，使用Promise异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inRotationVector | Array<number> | 是 | 旋转矩阵。 |
| coordinates | [CoordinatesOptions](js-apis-sensor.md#coordinatesoptions) | 是 | 指定坐标系方向。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，使用异步方式返回转换后的旋转矩阵。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例** ：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. let rotationMatrix = [
7. 1, 0, 0,
8. 0, 0.87, -0.50,
9. 0, 0.50, 0.87
10. ];
11. const promise = sensor.transformRotationMatrix(rotationMatrix, { x: 1, y: 3 });
12. promise.then((data: Array<number>) => {
13. for (let i = 0; i < data.length; i++) {
14. console.info('Succeeded in getting data[' + i + ']: ' + data[i]);
15. }
16. }, (err: BusinessError) => {
17. console.error(`Failed to transform rotationMatrix. Code: ${err.code}, message: ${err.message}`);
18. });
19. } catch (error) {
20. let e: BusinessError = error as BusinessError;
21. console.error(`Failed to transform rotationMatrix. Code: ${e.code}, message: ${e.message}`);
22. }
```

## sensor.getQuaternion9+

PhonePC/2in1TabletTVWearable

getQuaternion(rotationVector: Array<number>, callback: AsyncCallback<Array<number>>): void

根据旋转向量计算归一化四元数，使用Callback异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotationVector | Array<number> | 是 | 旋转矢量。 |
| callback | AsyncCallback<Array<number>> | 是 | 回调函数，异步返回归一化四元数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. let rotationVector = [0.20046076, 0.21907, 0.73978853, 0.60376877];
7. sensor.getQuaternion(rotationVector, (err: BusinessError, data: Array<number>) => {
8. if (err) {
9. console.error(`Failed to get quaternion. Code: ${err.code}, message: ${err.message}`);
10. return;
11. }
12. for (let i = 0; i < data.length; i++) {
13. console.info('Succeeded in getting data[' + i + ']: ' + data[i]);
14. }
15. })
16. } catch (error) {
17. let e: BusinessError = error as BusinessError;
18. console.error(`Failed to get quaternion. Code: ${e.code}, message: ${e.message}`);
19. }
```

## sensor.getQuaternion9+

PhonePC/2in1TabletTVWearable

getQuaternion(rotationVector: Array<number>): Promise<Array<number>>

根据旋转向量计算归一化四元数，使用Promise异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotationVector | Array<number> | 是 | 旋转矢量。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise，使用异步方式对象返归一化回四元数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. let rotationVector = [0.20046076, 0.21907, 0.73978853, 0.60376877];
7. const promise = sensor.getQuaternion(rotationVector);
8. promise.then((data: Array<number>) => {
9. for (let i = 0; i < data.length; i++) {
10. console.info('Succeeded in getting data[' + i + ']: ' + data[i]);
11. }
12. }, (err: BusinessError) => {
13. console.error(`Failed to get quaternion. Code: ${err.code}, message: ${err.message}`);
14. });
15. } catch (error) {
16. let e: BusinessError = error as BusinessError;
17. console.error(`Failed to get quaternion. Code: ${e.code}, message: ${e.message}`);
18. }
```

## sensor.getOrientation9+

PhonePC/2in1TabletTVWearable

getOrientation(rotationMatrix: Array<number>, callback: AsyncCallback<Array<number>>): void

根据旋转矩阵计算设备方向，使用Callback异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotationMatrix | Array<number> | 是 | 旋转矩阵。 |
| callback | AsyncCallback<Array<number>> | 是 | 回调函数，异步返回围绕z、x、y轴方向的旋转角度，单位度（°）。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. let preRotationMatrix = [
7. 1, 0, 0,
8. 0, 0.87, -0.50,
9. 0, 0.50, 0.87
10. ];
11. sensor.getOrientation(preRotationMatrix, (err: BusinessError, data: Array<number>) => {
12. if (err) {
13. console.error(`Failed to get orientation. Code: ${err.code}, message: ${err.message}`);
14. return;
15. }
16. if (data.length < 3) {
17. console.error("Failed to get orientation, length" + data.length);
18. }
19. console.info("Succeeded in getting data. Z: " + data[0]);
20. console.info("Succeeded in getting data. X: " + data[1]);
21. console.info("Succeeded in getting data. Y: " + data[2]);
22. })
23. } catch (error) {
24. let e: BusinessError = error as BusinessError;
25. console.error(`Failed to get orientation. Code: ${e.code}, message: ${e.message}`);
26. }
```

## sensor.getOrientation9+

PhonePC/2in1TabletTVWearable

getOrientation(rotationMatrix: Array<number>): Promise<Array<number>>

根据旋转矩阵计算设备的方向，使用Promise异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotationMatrix | Array<number> | 是 | 旋转矩阵。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，使用异步方式返回围绕z、x、y轴方向的旋转角度，单位度（°）。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. let preRotationMatrix = [
7. 1, 0, 0,
8. 0, 0.87, -0.50,
9. 0, 0.50, 0.87
10. ];
11. const promise = sensor.getOrientation(preRotationMatrix);
12. promise.then((data: Array<number>) => {
13. for (let i = 0; i < data.length; i++) {
14. console.info('Succeeded in getting data[' + i + ']: ' + data[i]);
15. }
16. }, (err: BusinessError) => {
17. console.error(`Failed to getOrientation. Code: ${err.code}, message: ${err.message}`);
18. });
19. } catch (error) {
20. let e: BusinessError = error as BusinessError;
21. console.error(`Failed to getOrientation Code: ${e.code}, message: ${e.message}`);
22. }
```

## sensor.getRotationMatrix9+

PhonePC/2in1TabletTVWearable

getRotationMatrix(gravity: Array<number>, geomagnetic: Array<number>, callback: AsyncCallback<RotationMatrixResponse>): void

根据重力矢量和地磁矢量计算旋转矩阵，使用Callback异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| gravity | Array<number> | 是 | 重力矢量。 |
| geomagnetic | Array<number> | 是 | 地磁矢量。 |
| callback | AsyncCallback<[RotationMatrixResponse](js-apis-sensor.md#rotationmatrixresponse)> | 是 | 回调函数，异步返回旋转矩阵。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. let gravity = [-0.27775216, 0.5351276, 9.788099];
7. let geomagnetic = [210.87253, -78.6096, -111.44444];
8. sensor.getRotationMatrix(gravity, geomagnetic, (err: BusinessError, data: sensor.RotationMatrixResponse) => {
9. if (err) {
10. console.error(`Failed to get rotationMatrix. Code: ${err.code}, message: ${err.message}`);
11. return;
12. }
13. console.info('Succeeded in getting rotationMatrix' + JSON.stringify(data));
14. })
15. } catch (error) {
16. let e: BusinessError = error as BusinessError;
17. console.error(`Failed to get rotationMatrix. Code: ${e.code}, message: ${e.message}`);
18. }
```

## sensor.getRotationMatrix9+

PhonePC/2in1TabletTVWearable

getRotationMatrix(gravity: Array<number>, geomagnetic: Array<number>): Promise<RotationMatrixResponse>

根据重力矢量和地磁矢量计算旋转矩阵，使用Promise异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| gravity | Array<number> | 是 | 重力向量。 |
| geomagnetic | Array<number> | 是 | 地磁矢量。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[RotationMatrixResponse](js-apis-sensor.md#rotationmatrixresponse)> | Promise对象，使用异步方式返回旋转矩阵。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. let gravity = [-0.27775216, 0.5351276, 9.788099];
7. let geomagnetic = [210.87253, -78.6096, -111.44444];
8. const promise = sensor.getRotationMatrix(gravity, geomagnetic);
9. promise.then((data: sensor.RotationMatrixResponse) => {
10. console.info('Succeeded in getting rotationMatrix' + JSON.stringify(data));
11. }, (err: BusinessError) => {
12. console.error(`Failed to get rotationMatrix. Code: ${err.code}, message: ${err.message}`);
13. });
14. } catch (error) {
15. let e: BusinessError = error as BusinessError;
16. console.error(`Failed to get rotationMatrix. Code: ${e.code}, message: ${e.message}`);
17. }
```

## sensor.getSensorList9+

PhonePC/2in1TabletTVWearable

getSensorList(callback: AsyncCallback<Array<Sensor>>): void

获取设备上的所有传感器信息，使用Callback异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[Sensor](js-apis-sensor.md#sensor9)>> | 是 | 回调函数，异步返回传感器属性列表。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.getSensorList((err: BusinessError, data: Array<sensor.Sensor>) => {
7. if (err) {
8. console.error(`Failed to get sensorList. Code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. for (let i = 0; i < data.length; i++) {
12. console.info('Succeeded in getting data[' + i + ']: ' + JSON.stringify(data[i]));
13. }
14. });
15. } catch (error) {
16. let e: BusinessError = error as BusinessError;
17. console.error(`Failed to get sensorList. Code: ${e.code}, message: ${e.message}`);
18. }
```

## sensor.getSensorList9+

PhonePC/2in1TabletTVWearable

getSensorList(): Promise<Array<Sensor>>

获取设备上的所有传感器信息，使用Promise异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[Sensor](js-apis-sensor.md#sensor9)>> | Promise对象，使用异步方式返回传感器属性列表。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.getSensorList().then((data: Array<sensor.Sensor>) => {
7. for (let i = 0; i < data.length; i++) {
8. console.info('Succeeded in getting data[' + i + ']: ' + JSON.stringify(data[i]));
9. }
10. }, (err: BusinessError) => {
11. console.error(`Failed to get sensorList. Code: ${err.code}, message: ${err.message}`);
12. });
13. } catch (error) {
14. let e: BusinessError = error as BusinessError;
15. console.error(`Failed to get sensorList. Code: ${e.code}, message: ${e.message}`);
16. }
```

## sensor.getSensorListSync12+

PhonePC/2in1TabletTVWearable

getSensorListSync(): Array<Sensor>

获取设备上的所有传感器信息，使用同步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Array<[Sensor](js-apis-sensor.md#sensor9)> | 使用同步方式返回传感器属性列表。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. let ret = sensor.getSensorListSync()
7. for (let i = 0; i < ret.length; i++) {
8. console.info('Succeeded in getting sensor: ' + JSON.stringify(ret[i]));
9. }
10. } catch(error) {
11. let e: BusinessError = error as BusinessError;
12. console.error(`Failed to get singleSensor . Code: ${e.code}, message: ${e.message}`);
13. }
```

## sensor.getSingleSensor9+

PhonePC/2in1TabletTVWearable

getSingleSensor(type: SensorId, callback: AsyncCallback<Sensor>): void

获取指定传感器类型的属性信息，使用Callback异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9) | 是 | 指定传感器类型。 |
| callback | AsyncCallback<[Sensor](js-apis-sensor.md#sensor9)> | 是 | 回调函数，异步返回指定传感器的属性信息。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |
| 14500102 | The sensor is not supported by the device. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.getSingleSensor(sensor.SensorId.ACCELEROMETER, (err: BusinessError, data: sensor.Sensor) => {
7. if (err) {
8. console.error(`Failed to get singleSensor. Code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. console.info('Succeeded in getting sensor: ' + JSON.stringify(data));
12. sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
13. console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
14. console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
15. console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
16. }, { interval: 100000000 });
17. setTimeout(() => {
18. sensor.off(sensor.SensorId.ACCELEROMETER);
19. }, 500);
20. });
21. } catch (error) {
22. let e: BusinessError = error as BusinessError;
23. console.error(`Failed to get singleSensor. Code: ${e.code}, message: ${e.message}`);
24. }
```

## sensor.getSingleSensor9+

PhonePC/2in1TabletTVWearable

getSingleSensor(type: SensorId): Promise<Sensor>

获取指定类型的传感器信息，使用Promise异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9) | 是 | 传感器类型。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[Sensor](js-apis-sensor.md#sensor9)> | 使用异步方式返回传感器信息。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |
| 14500102 | The sensor is not supported by the device. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. sensor.getSingleSensor(sensor.SensorId.ACCELEROMETER).then((data: sensor.Sensor) => {
7. console.info('Succeeded in getting sensor: ' + JSON.stringify(data));
8. }, (err: BusinessError) => {
9. console.error(`Failed to get singleSensor . Code: ${err.code}, message: ${err.message}`);
10. });
11. } catch (error) {
12. let e: BusinessError = error as BusinessError;
13. console.error(`Failed to get singleSensor . Code: ${e.code}, message: ${e.message}`);
14. }
```

## sensor.getSingleSensorSync12+

PhonePC/2in1TabletTVWearable

getSingleSensorSync(type: SensorId): Sensor

获取指定类型的传感器信息，使用同步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorId](js-apis-sensor.md#sensorid9) | 是 | 传感器类型。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Sensor | 使用同步方式返回传感器信息。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](errorcode-sensor.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |
| 14500102 | The sensor is not supported by the device. |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. let ret = sensor.getSingleSensorSync(sensor.SensorId.ACCELEROMETER);
7. console.info('Succeeded in getting sensor: ' + JSON.stringify(ret));
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. console.error(`Failed to get singleSensor . Code: ${e.code}, message: ${e.message}`);
11. }
```

## SensorId9+

PhonePC/2in1TabletTVWearable

表示当前支持订阅或取消订阅的传感器类型。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACCELEROMETER | 1 | 加速度传感器。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| GYROSCOPE | 2 | 陀螺仪传感器。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| AMBIENT\_LIGHT | 5 | 环境光传感器。 |
| MAGNETIC\_FIELD | 6 | 磁场传感器。 |
| BAROMETER | 8 | 气压计传感器。 |
| HALL | 10 | 霍尔传感器。 |
| PROXIMITY | 12 | 接近光传感器。 |
| HUMIDITY | 13 | 湿度传感器。 |
| ORIENTATION | 256 | 方向传感器。  **元服务API**：从API version 11开始，该接口在支持元服务中使用。 |
| GRAVITY | 257 | 重力传感器。 |
| LINEAR\_ACCELEROMETER | 258 | 线性加速度传感器。 |
| ROTATION\_VECTOR | 259 | 旋转矢量传感器。 |
| AMBIENT\_TEMPERATURE | 260 | 环境温度传感器。 |
| MAGNETIC\_FIELD\_UNCALIBRATED | 261 | 未校准磁场传感器。 |
| GYROSCOPE\_UNCALIBRATED | 263 | 未校准陀螺仪传感器。 |
| SIGNIFICANT\_MOTION | 264 | 有效运动传感器。 |
| PEDOMETER\_DETECTION | 265 | 计步检测传感器。 |
| PEDOMETER | 266 | 计步传感器。 |
| HEART\_RATE | 278 | 心率传感器。 |
| WEAR\_DETECTION | 280 | 佩戴检测传感器。 |
| ACCELEROMETER\_UNCALIBRATED | 281 | 未校准加速度计传感器。 |
| FUSION\_PRESSURE22+ | 283 | 融合压力传感器。  仅智能表有该传感器 |

## SensorInfoParam19+

PhonePC/2in1TabletTVWearable

传感器传入设置参数，多传感器情况下通过deviceId、sensorIndex控制指定传感器。

**系统能力**：SystemCapability.Sensors.Sensor

**元服务API**：从API version 19开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | number | 否 | 是 | 设备ID：默认值为-1，表示本地设备，设备ID需通过[getSensorList](js-apis-sensor.md#sensorgetsensorlist9)查询或者监听设备上下线接口[sensorStatusChange](js-apis-sensor.md#sensorstatuschange19)获取。  **元服务API**：从API version 19开始，该接口支持在元服务中使用。 |
| sensorIndex | number | 否 | 是 | 传感器索引：默认值为0，为设备上的默认传感器，其它传感器ID需通过[getSensorList](js-apis-sensor.md#sensorgetsensorlist9)查询或者监听设备上下线接口[sensorStatusChange](js-apis-sensor.md#sensorstatuschange19)获取。  **元服务API**：从API version 19开始，该接口支持在元服务中使用。 |

## SensorStatusEvent19+

PhonePC/2in1TabletTVWearable

设备状态变化事件数据。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timestamp | number | 否 | 否 | 事件发生的时间戳，单位ms。 |
| sensorId | number | 否 | 否 | 传感器ID。 |
| sensorIndex | number | 否 | 否 | 传感器索引。 |
| isSensorOnline | boolean | 否 | 否 | 传感器上线或者下线，true为上线，false为下线。 |
| deviceId | number | 否 | 否 | 设备ID。 |
| deviceName | string | 否 | 否 | 设备名称。 |

## SensorAccuracy11+

PhonePC/2in1TabletTVWearable

传感器数据的精度。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACCURACY\_UNRELIABLE | 0 | 传感器数据不可信。 |
| ACCURACY\_LOW | 1 | 传感器低挡位精度。 |
| ACCURACY\_MEDIUM | 2 | 传感器中挡位精度。 |
| ACCURACY\_HIGH | 3 | 传感器高挡位精度。 |

## Response

PhonePC/2in1TabletTVWearable

传感器数据的时间戳。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timestamp | number | 否 | 否 | 传感器数据上报的时间戳。从设备开机开始计时到上报数据的时间，单位 : ns。 |
| accuracy11+ | [SensorAccuracy](js-apis-sensor.md#sensoraccuracy11)11+ | 否 | 否 | 传感器数据上报的精度挡位值。 |

## Sensor9+

PhonePC/2in1TabletTVWearable

指示传感器信息。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sensorName | string | 否 | 否 | 传感器名称。 |
| vendorName | string | 否 | 否 | 传感器供应商。 |
| firmwareVersion | string | 否 | 否 | 传感器固件版本。 |
| hardwareVersion | string | 否 | 否 | 传感器硬件版本。 |
| sensorId | number | 否 | 否 | 传感器类型id。 |
| maxRange | number | 否 | 否 | 传感器测量范围的最大值。 |
| minSamplePeriod | number | 否 | 否 | 允许的最小采样周期。 |
| maxSamplePeriod | number | 否 | 否 | 允许的最大采样周期。 |
| precision | number | 否 | 否 | 传感器精度。 |
| power | number | 否 | 否 | 传感器功率的估计值，单位：mA。 |
| sensorIndex19+ | number | 否 | 是 | 传感器索引。 |
| deviceId19+ | number | 否 | 是 | 设备ID。 |
| deviceName19+ | string | 否 | 是 | 设备名称。 |
| isLocalSensor19+ | boolean | 否 | 是 | 是否本地传感器，true为本地传感器，false为非本地传感器。 |
| isMockSensor23+ | boolean | 否 | 是 | 是否mock传感器，true为mock传感器，false为非mock传感器。 |

## AccelerometerResponse

PhonePC/2in1TabletTVWearable

加速度传感器数据，继承于[Response](js-apis-sensor.md#response)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 施加在设备x轴的加速度，单位 : m/s²；取值为实际上报物理量。 |
| y | number | 否 | 否 | 施加在设备y轴的加速度，单位 : m/s²；取值为实际上报物理量。 |
| z | number | 否 | 否 | 施加在设备z轴的加速度，单位 : m/s²；取值为实际上报物理量。 |

## LinearAccelerometerResponse

PhonePC/2in1TabletTVWearable

线性加速度传感器数据，继承于[Response](js-apis-sensor.md#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 施加在设备x轴的线性加速度，单位 : m/s²。 |
| y | number | 否 | 否 | 施加在设备y轴的线性加速度，单位 : m/s²。 |
| z | number | 否 | 否 | 施加在设备z轴的线性加速度，单位 : m/s²。 |

## AccelerometerUncalibratedResponse

PhonePC/2in1TabletTVWearable

未校准加速度计传感器数据，继承于[Response](js-apis-sensor.md#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 施加在设备x轴未校准的加速度，单位 : m/s²。 |
| y | number | 否 | 否 | 施加在设备y轴未校准的加速度，单位 : m/s²。 |
| z | number | 否 | 否 | 施加在设备z轴未校准的加速度，单位 : m/s²。 |
| biasX | number | 否 | 否 | 施加在设备x轴未校准的加速度偏量，单位 : m/s²。 |
| biasY | number | 否 | 否 | 施加在设备y轴未校准的加速度偏量，单位 : m/s²。 |
| biasZ | number | 否 | 否 | 施加在设备z轴未校准的加速度偏量，单位 : m/s²。 |

## FusionPressureResponse22+

PhonePC/2in1TabletTVWearable

融合压力传感器数据，继承于[Response](js-apis-sensor.md#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fusionPressure | number | 否 | 否 | 施加在融合压力传感器上的压力值百分比，单位 : % |

## GravityResponse

PhonePC/2in1TabletTVWearable

重力传感器数据，继承于[Response](js-apis-sensor.md#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 施加在设备x轴的重力加速度，单位 : m/s²。 |
| y | number | 否 | 否 | 施加在设备y轴的重力加速度，单位 : m/s²。 |
| z | number | 否 | 否 | 施加在设备z轴的重力加速度，单位 : m/s²。 |

## OrientationResponse

PhonePC/2in1TabletTVWearable

方向传感器数据，继承于[Response](js-apis-sensor.md#response)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| alpha | number | 否 | 否 | 设备围绕Z轴的旋转角度，单位：度；取值范围为0-360度。 |
| beta | number | 否 | 否 | 设备围绕X轴的旋转角度，单位：度；取值范围为0-±180度。 |
| gamma | number | 否 | 否 | 设备围绕Y轴的旋转角度，单位：度；取值范围为0-±90度。 |

## RotationVectorResponse

PhonePC/2in1TabletTVWearable

旋转矢量传感器数据，继承于[Response](js-apis-sensor.md#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 旋转矢量x轴分量。 |
| y | number | 否 | 否 | 旋转矢量y轴分量。 |
| z | number | 否 | 否 | 旋转矢量z轴分量。 |
| w | number | 否 | 否 | 标量，描述设备相对于某个参考方向的旋转状态，单位：弧度。 |

## GyroscopeResponse

PhonePC/2in1TabletTVWearable

陀螺仪传感器数据，继承于[Response](js-apis-sensor.md#response)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 设备x轴的旋转角速度，单位rad/s；取值为实际上报物理量。 |
| y | number | 否 | 否 | 设备y轴的旋转角速度，单位rad/s；取值为实际上报物理量。 |
| z | number | 否 | 否 | 设备z轴的旋转角速度，单位rad/s；取值为实际上报物理量。 |

## GyroscopeUncalibratedResponse

PhonePC/2in1TabletTVWearable

未校准陀螺仪传感器数据，继承于[Response](js-apis-sensor.md#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 设备x轴未校准的旋转角速度，单位rad/s。 |
| y | number | 否 | 否 | 设备y轴未校准的旋转角速度，单位rad/s。 |
| z | number | 否 | 否 | 设备z轴未校准的旋转角速度，单位rad/s。 |
| biasX | number | 否 | 否 | 设备x轴未校准的旋转角速度偏量，单位rad/s。 |
| biasY | number | 否 | 否 | 设备y轴未校准的旋转角速度偏量，单位rad/s。 |
| biasZ | number | 否 | 否 | 设备z轴未校准的旋转角速度偏量，单位rad/s。 |

## SignificantMotionResponse

PhonePC/2in1TabletTVWearable

有效运动传感器数据，继承于[Response](js-apis-sensor.md#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scalar | number | 否 | 否 | 表示剧烈运动程度。测量三个物理轴（x、y 和 z）上，设备是否存在大幅度运动；若存在大幅度运动则数据上报为1。 |

## ProximityResponse

PhonePC/2in1TabletTVWearable

接近光传感器数据，继承于[Response](js-apis-sensor.md#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| distance | number | 否 | 否 | 可见物体与设备显示器的接近程度。0表示接近，大于0表示远离。 |

## LightResponse

PhonePC/2in1TabletTVWearable

环境光传感器数据，继承于[Response](js-apis-sensor.md#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| intensity | number | 否 | 否 | 光强（单位：勒克斯）。 |
| colorTemperature12+ | number | 否 | 是 | 色温（单位：开尔文），可选参数，如果该参数不支持则返回固定值（固定值由传感器自定义），支持则返回正常数值。 |
| infraredLuminance12+ | number | 否 | 是 | 红外亮度（单位：cd/m²），可选参数，如果该参数不支持则返回固定值（固定值由传感器自定义），支持则返回正常数值。 |

## HallResponse

PhonePC/2in1TabletTVWearable

霍尔传感器数据，继承于[Response](js-apis-sensor.md#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| status | number | 否 | 否 | 显示霍尔状态。测量设备周围是否存在磁力吸引，0表示没有，大于0表示有。 |

## MagneticFieldResponse

PhonePC/2in1TabletTVWearable

磁场传感器数据，继承于[Response](js-apis-sensor.md#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | x轴环境磁场强度，单位 : μT。 |
| y | number | 否 | 否 | y轴环境磁场强度，单位 : μT。 |
| z | number | 否 | 否 | z轴环境磁场强度，单位 : μT。 |

## MagneticFieldUncalibratedResponse

PhonePC/2in1TabletTVWearable

未校准磁场传感器数据，继承于[Response](js-apis-sensor.md#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | x轴未校准环境磁场强度，单位 : μT。 |
| y | number | 否 | 否 | y轴未校准环境磁场强度，单位 : μT。 |
| z | number | 否 | 否 | z轴未校准环境磁场强度，单位 : μT。 |
| biasX | number | 否 | 否 | x轴未校准环境磁场强度偏量，单位 : μT。 |
| biasY | number | 否 | 否 | y轴未校准环境磁场强度偏量，单位 : μT。 |
| biasZ | number | 否 | 否 | z轴未校准环境磁场强度偏量，单位 : μT。 |

## PedometerResponse

PhonePC/2in1TabletTVWearable

计步传感器数据，继承于[Response](js-apis-sensor.md#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| steps | number | 否 | 否 | 用户的行走步数。 |

## HumidityResponse

PhonePC/2in1TabletTVWearable

湿度传感器数据，继承于[Response](js-apis-sensor.md#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| humidity | number | 否 | 否 | 湿度值。测量环境的相对湿度，以百分比 (%) 表示。 |

## PedometerDetectionResponse

PhonePC/2in1TabletTVWearable

计步检测传感器数据，继承于[Response](js-apis-sensor.md#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scalar | number | 否 | 否 | 计步器检测。检测用户的计步动作，如果取值为1则代表用户产生了计步行走的动作，取值为0则代表用户没有发生运动。 |

## AmbientTemperatureResponse

PhonePC/2in1TabletTVWearable

温度传感器数据，继承于[Response](js-apis-sensor.md#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| temperature | number | 否 | 否 | 环境温度（单位：摄氏度）。 |

## BarometerResponse

PhonePC/2in1TabletTVWearable

气压计传感器数据，继承于[Response](js-apis-sensor.md#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pressure | number | 否 | 否 | 压力值（单位：百帕）。 |

## HeartRateResponse

PhonePC/2in1TabletTVWearable

心率传感器数据，继承于[Response](js-apis-sensor.md#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| heartRate | number | 否 | 否 | 心率值。测量用户的心率数值，单位：bpm。 |

## WearDetectionResponse

PhonePC/2in1TabletTVWearable

佩戴检测传感器数据，继承于[Response](js-apis-sensor.md#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | number | 否 | 否 | 表示设备是否被穿戴（1表示已穿戴，0表示未穿戴）。 |

## Options

PhonePC/2in1TabletTVWearable

设置传感器上报频率。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| interval | number|[SensorFrequency](js-apis-sensor.md#sensorfrequency11)11+ | 否 | 是 | 表示传感器的上报频率，默认值为200000000ns。该属性有最小值和最大值的限制，由硬件支持的上报频率决定，当设置频率大于最大值时以最大值上报数据，小于最小值时以最小值上报数据。 |
| sensorInfoParam19+ | [SensorInfoParam](js-apis-sensor.md#sensorinfoparam19) | 否 | 是 | 传感器传入设置参数，可指定deviceId、sensorIndex。  **元服务API**：从API version 19开始，该接口支持在元服务中使用。 |

## SensorFrequency11+

PhonePC/2in1TabletTVWearable

type SensorFrequency = 'game' | 'ui' | 'normal'

传感器上报频率模式。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

| 类型 | 说明 |
| --- | --- |
| 'game' | 用于指定传感器上报频率，频率值为20000000ns，该频率被设置在硬件支持的频率范围内时会生效，值固定为'game'字符串。 |
| 'ui' | 用于指定传感器上报频率，频率值为60000000ns，该频率被设置在硬件支持的频率范围内时会生效，值固定为'ui'字符串。 |
| 'normal' | 用于指定传感器上报频率，频率值为200000000ns，该频率被设置在硬件支持的频率范围内时会生效，值固定为'normal'字符串。 |

## RotationMatrixResponse

PhonePC/2in1TabletTVWearable

设置旋转矩阵响应对象。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rotation | Array<number> | 否 | 否 | 旋转矩阵。 |
| inclination | Array<number> | 否 | 否 | 倾斜矩阵。 |

## CoordinatesOptions

PhonePC/2in1TabletTVWearable

设置坐标选项对象。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | x坐标方向。 |
| y | number | 否 | 否 | y坐标方向。 |

## GeomagneticResponse

PhonePC/2in1TabletTVWearable

设置地磁响应对象。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 地磁场的北分量，单位nT。 |
| y | number | 否 | 否 | 地磁场的东分量，单位nT。 |
| z | number | 否 | 否 | 地磁场的垂直分量，单位nT。 |
| geomagneticDip | number | 否 | 否 | 地磁倾角，即地球磁场线与水平面的夹角，单位度（°）。 |
| deflectionAngle | number | 否 | 否 | 地磁偏角，即地磁北方向与正北方向在水平面上的角度，单位度（°）。 |
| levelIntensity | number | 否 | 否 | 地磁场的水平强度，单位nT。 |
| totalIntensity | number | 否 | 否 | 地磁场的总强度，单位nT。 |

## LocationOptions

PhonePC/2in1TabletTVWearable

指示地理位置。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| latitude | number | 否 | 否 | 纬度，单位度（°）。 |
| longitude | number | 否 | 否 | 经度，单位度（°）。 |
| altitude | number | 否 | 否 | 海拔高度，单位m。 |

## sensor.on(deprecated)

PhonePC/2in1TabletTVWearable

### ACCELEROMETER(deprecated)

PhonePC/2in1TabletTVWearable

on(type: SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER, callback: Callback<AccelerometerResponse>,options?: Options): void

监听加速度传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.ACCELEROMETER](js-apis-sensor.md#accelerometer9)9+代替。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_ACCELEROMETER | 是 | 要订阅的加速度传感器类型为SENSOR\_TYPE\_ID\_ACCELEROMETER。 |
| callback | Callback<[AccelerometerResponse](js-apis-sensor.md#accelerometerresponse)> | 是 | 注册加速度传感器的回调函数，上报的数据类型为AccelerometerResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.on(sensor.SensorType.SENSOR_TYPE_ID_ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
4. console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
7. },
8. { interval: 100000000 }
9. );
```

### LINEAR\_ACCELERATION(deprecated)

PhonePC/2in1TabletTVWearable

on(type: SensorType.SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION,callback:Callback<LinearAccelerometerResponse>, options?: Options): void

监听线性加速度传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.LINEAR\_ACCELEROMETER](js-apis-sensor.md#linear_accelerometer9)9+代替。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION | 是 | 要订阅的线性加速度传感器类型为SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION。 |
| callback | Callback<[LinearAccelerometerResponse](js-apis-sensor.md#linearaccelerometerresponse)> | 是 | 注册线性加速度传感器的回调函数，上报的数据类型为LinearAccelerometerResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

### ACCELEROMETER\_UNCALIBRATED(deprecated)

PhonePC/2in1TabletTVWearable

on(type: SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED,callback: Callback<AccelerometerUncalibratedResponse>, options?: Options): void

监听未校准加速度计传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.ACCELEROMETER\_UNCALIBRATED](js-apis-sensor.md#accelerometer_uncalibrated9)9+代替。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED | 是 | 要订阅的未校准加速度计传感器类型为SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED。 |
| callback | Callback<[AccelerometerUncalibratedResponse](js-apis-sensor.md#accelerometeruncalibratedresponse)> | 是 | 注册未校准加速度计传感器的回调函数，上报的数据类型为AccelerometerUncalibratedResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.on(sensor.SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED, (data: sensor.AccelerometerUncalibratedResponse) => {
4. console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
7. console.info('Succeeded in invoking on. X-coordinate bias: ' + data.biasX);
8. console.info('Succeeded in invoking on. Y-coordinate bias: ' + data.biasY);
9. console.info('Succeeded in invoking on. Z-coordinate bias: ' + data.biasZ);
10. },
11. { interval: 100000000 }
12. );
```

### GRAVITY(deprecated)

PhonePC/2in1TabletTVWearable

on(type: SensorType.SENSOR\_TYPE\_ID\_GRAVITY, callback: Callback<GravityResponse>,options?: Options): void

监听重力传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.GRAVITY](js-apis-sensor.md#gravity9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_GRAVITY | 是 | 要订阅的重力传感器类型为SENSOR\_TYPE\_ID\_GRAVITY。 |
| callback | Callback<[GravityResponse](js-apis-sensor.md#gravityresponse)> | 是 | 注册重力传感器的回调函数，上报的数据类型为GravityResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.on(sensor.SensorType.SENSOR_TYPE_ID_GRAVITY, (data: sensor.GravityResponse) => {
4. console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
7. },
8. { interval: 100000000 }
9. );
```

### GYROSCOPE(deprecated)

PhonePC/2in1TabletTVWearable

on(type: SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE, callback: Callback<GyroscopeResponse>, options?: Options): void

监听陀螺仪传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.GYROSCOPE](js-apis-sensor.md#gyroscope9)9+代替。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_GYROSCOPE | 是 | 要订阅的陀螺仪传感器类型为SENSOR\_TYPE\_ID\_GYROSCOPE。 |
| callback | Callback<[GyroscopeResponse](js-apis-sensor.md#gyroscoperesponse)> | 是 | 注册陀螺仪传感器的回调函数，上报的数据类型为GyroscopeResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.on(sensor.SensorType.SENSOR_TYPE_ID_GYROSCOPE, (data: sensor.GyroscopeResponse) => {
4. console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
7. },
8. { interval: 100000000 }
9. );
```

### GYROSCOPE\_UNCALIBRATED(deprecated)

PhonePC/2in1TabletTVWearable

on(type: SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED,callback:Callback<GyroscopeUncalibratedResponse>, options?: Options): void

监听未校准陀螺仪传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.GYROSCOPE\_UNCALIBRATED](js-apis-sensor.md#gyroscope_uncalibrated9)9+代替。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED | 是 | 要订阅的未校准陀螺仪传感器类型为SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED。 |
| callback | Callback<[GyroscopeUncalibratedResponse](js-apis-sensor.md#gyroscopeuncalibratedresponse)> | 是 | 注册未校准陀螺仪传感器的回调函数，上报的数据类型为GyroscopeUncalibratedResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.on(sensor.SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED, (data: sensor.GyroscopeUncalibratedResponse) => {
4. console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
7. console.info('Succeeded in invoking on. X-coordinate bias: ' + data.biasX);
8. console.info('Succeeded in invoking on. Y-coordinate bias: ' + data.biasY);
9. console.info('Succeeded in invoking on. Z-coordinate bias: ' + data.biasZ);
10. },
11. { interval: 100000000 }
12. );
```

### SIGNIFICANT\_MOTION(deprecated)

PhonePC/2in1TabletTVWearable

on(type: SensorType.SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION, callback: Callback<SignificantMotionResponse>, options?: Options): void

监听有效运动传感器数据变化。如果多次调用该接口，仅最后一次调用生效。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.SIGNIFICANT\_MOTION](js-apis-sensor.md#significant_motion9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION | 是 | 要订阅的有效运动传感器类型为SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION。 |
| callback | Callback<[SignificantMotionResponse](js-apis-sensor.md#significantmotionresponse)> | 是 | 注册有效运动传感器的回调函数，上报的数据类型为SignificantMotionResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.on(sensor.SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION, (data: sensor.SignificantMotionResponse) => {
4. console.info('Succeeded in invoking on. Scalar data: ' + data.scalar);
5. },
6. { interval: 100000000 }
7. );
```

### PEDOMETER\_DETECTION(deprecated)

PhonePC/2in1TabletTVWearable

on(type: SensorType.SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION, callback: Callback<PedometerDetectionResponse>, options?: Options): void

监听计步检测传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.PEDOMETER\_DETECTION](js-apis-sensor.md#pedometer_detection9)9+代替。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION | 是 | 要订阅的计步检测传感器类型为SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION。 |
| callback | Callback<[PedometerDetectionResponse](js-apis-sensor.md#pedometerdetectionresponse)> | 是 | 注册计步检测传感器的回调函数，上报的数据类型为PedometerDetectionResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.on(sensor.SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, (data: sensor.PedometerDetectionResponse) => {
4. console.info('Succeeded in invoking on. Scalar data: ' + data.scalar);
5. },
6. { interval: 100000000 }
7. );
```

### PEDOMETER(deprecated)

PhonePC/2in1TabletTVWearable

on(type: SensorType.SENSOR\_TYPE\_ID\_PEDOMETER, callback: Callback<PedometerResponse>, options?: Options): void

监听计步传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.PEDOMETER](js-apis-sensor.md#pedometer9)9+代替。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_PEDOMETER | 是 | 要订阅的计步传感器类型为SENSOR\_TYPE\_ID\_PEDOMETER。 |
| callback | Callback<[PedometerResponse](js-apis-sensor.md#pedometerresponse)> | 是 | 注册计步传感器的回调函数，上报的数据类型为PedometerResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.on(sensor.SensorType.SENSOR_TYPE_ID_PEDOMETER, (data: sensor.PedometerResponse) => {
4. console.info('Succeeded in invoking on. Steps: ' + data.steps);
5. },
6. { interval: 100000000 }
7. );
```

### AMBIENT\_TEMPERATURE(deprecated)

PhonePC/2in1TabletTVWearable

on(type: SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE,callback:Callback<AmbientTemperatureResponse>, options?: Options): void

监听环境温度传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.AMBIENT\_TEMPERATURE](js-apis-sensor.md#ambient_temperature9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE | 是 | 要订阅的环境温度传感器类型为SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE。 |
| callback | Callback<[AmbientTemperatureResponse](js-apis-sensor.md#ambienttemperatureresponse)> | 是 | 注册环境温度传感器的回调函数，上报的数据类型为AmbientTemperatureResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.on(sensor.SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE, (data: sensor.AmbientTemperatureResponse) => {
4. console.info('Succeeded in invoking on. Temperature: ' + data.temperature);
5. },
6. { interval: 100000000 }
7. );
```

### MAGNETIC\_FIELD(deprecated)

PhonePC/2in1TabletTVWearable

on(type: SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD, callback: Callback<MagneticFieldResponse>,options?: Options): void

监听磁场传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.MAGNETIC\_FIELD](js-apis-sensor.md#magnetic_field9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD | 是 | 要订阅的磁场传感器类型为SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD。 |
| callback | Callback<[MagneticFieldResponse](js-apis-sensor.md#magneticfieldresponse)> | 是 | 注册磁场传感器的回调函数，上报的数据类型为MagneticFieldResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.on(sensor.SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD, (data: sensor.MagneticFieldResponse) => {
4. console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
7. },
8. { interval: 100000000 }
9. );
```

### MAGNETIC\_FIELD\_UNCALIBRATED(deprecated)

PhonePC/2in1TabletTVWearable

on(type: SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED,callback: Callback<MagneticFieldUncalibratedResponse>, options?: Options): void

监听未校准磁场传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.MAGNETIC\_FIELD\_UNCALIBRATED](js-apis-sensor.md#magnetic_field_uncalibrated9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED | 是 | 要订阅的未校准磁场传感器类型为SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED。 |
| callback | Callback<[MagneticFieldUncalibratedResponse](js-apis-sensor.md#magneticfielduncalibratedresponse)> | 是 | 注册未校准磁场传感器的回调函数，上报的数据类型为MagneticFieldUncalibratedResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.on(sensor.SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED, (data: sensor.MagneticFieldUncalibratedResponse) => {
4. console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
7. console.info('Succeeded in invoking on. X-coordinate bias: ' + data.biasX);
8. console.info('Succeeded in invoking on. Y-coordinate bias: ' + data.biasY);
9. console.info('Succeeded in invoking on. Z-coordinate bias: ' + data.biasZ);
10. },
11. { interval: 100000000 }
12. );
```

### PROXIMITY(deprecated)

PhonePC/2in1TabletTVWearable

on(type: SensorType.SENSOR\_TYPE\_ID\_PROXIMITY, callback: Callback<ProximityResponse>,options?: Options): void

监听接近光传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.PROXIMITY](js-apis-sensor.md#proximity9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_PROXIMITY | 是 | 要订阅的接近光传感器类型为SENSOR\_TYPE\_ID\_PROXIMITY。 |
| callback | Callback<[ProximityResponse](js-apis-sensor.md#proximityresponse)> | 是 | 注册接近光传感器的回调函数，上报的数据类型为ProximityResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，默认值为200000000ns。当接近光事件被触发的很频繁时，该参数用于限定事件上报的频率。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.on(sensor.SensorType.SENSOR_TYPE_ID_PROXIMITY, (data: sensor.ProximityResponse) => {
4. console.info('Succeeded in invoking on. Distance: ' + data.distance);
5. },
6. { interval: 100000000 }
7. );
```

### HUMIDITY(deprecated)

PhonePC/2in1TabletTVWearable

on(type: SensorType.SENSOR\_TYPE\_ID\_HUMIDITY, callback: Callback<HumidityResponse>,options?: Options): void

监听湿度传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.HUMIDITY](js-apis-sensor.md#humidity9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_HUMIDITY | 是 | 要订阅的湿度传感器类型为SENSOR\_TYPE\_ID\_HUMIDITY。 |
| callback | Callback<[HumidityResponse](js-apis-sensor.md#humidityresponse)> | 是 | 注册湿度传感器的回调函数，上报的数据类型为HumidityResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.on(sensor.SensorType.SENSOR_TYPE_ID_HUMIDITY, (data: sensor.HumidityResponse) => {
4. console.info('Succeeded in invoking on. Humidity: ' + data.humidity);
5. },
6. { interval: 100000000 }
7. );
```

### BAROMETER(deprecated)

PhonePC/2in1TabletTVWearable

on(type: SensorType.SENSOR\_TYPE\_ID\_BAROMETER, callback: Callback<BarometerResponse>,options?: Options): void

监听气压计传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.BAROMETER](js-apis-sensor.md#barometer9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_BAROMETER | 是 | 要订阅的气压计传感器类型为SENSOR\_TYPE\_ID\_BAROMETER。 |
| callback | Callback<[BarometerResponse](js-apis-sensor.md#barometerresponse)> | 是 | 注册气压计传感器的回调函数，上报的数据类型为BarometerResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.on(sensor.SensorType.SENSOR_TYPE_ID_BAROMETER, (data: sensor.BarometerResponse) => {
4. console.info('Succeeded in invoking on. Atmospheric pressure: ' + data.pressure);
5. },
6. { interval: 100000000 }
7. );
```

### HALL(deprecated)

PhonePC/2in1TabletTVWearable

on(type: SensorType.SENSOR\_TYPE\_ID\_HALL, callback: Callback<HallResponse>, options?: Options): void

监听霍尔传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.HALL](js-apis-sensor.md#hall9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_HALL | 是 | 要订阅的霍尔传感器类型为SENSOR\_TYPE\_ID\_HALL。 |
| callback | Callback<[HallResponse](js-apis-sensor.md#hallresponse)> | 是 | 注册霍尔传感器的回调函数，上报的数据类型为 HallResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，默认值为200000000ns。当霍尔事件被触发的很频繁时，该参数用于限定事件上报的频率。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.on(sensor.SensorType.SENSOR_TYPE_ID_HALL, (data: sensor.HallResponse) => {
4. console.info('Succeeded in invoking on. Status: ' + data.status);
5. },
6. { interval: 100000000 }
7. );
```

### AMBIENT\_LIGHT(deprecated)

PhonePC/2in1TabletTVWearable

on(type: SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT, callback: Callback<LightResponse>, options?: Options): void

监听环境光传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.AMBIENT\_LIGHT](js-apis-sensor.md#ambient_light9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT | 是 | 要订阅的环境光传感器类型为SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT。 |
| callback | Callback<[LightResponse](js-apis-sensor.md#lightresponse)> | 是 | 注册环境光传感器的回调函数，上报的数据类型为LightResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.on(sensor.SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT, (data: sensor.LightResponse) => {
4. console.info('Succeeded in invoking on. Illumination: ' + data.intensity);
5. },
6. { interval: 100000000 }
7. );
```

### ORIENTATION(deprecated)

PhonePC/2in1TabletTVWearable

on(type: SensorType.SENSOR\_TYPE\_ID\_ORIENTATION, callback: Callback<OrientationResponse>, options?: Options): void

监听方向传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.ORIENTATION](js-apis-sensor.md#orientation9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_ORIENTATION | 是 | 要订阅的方向传感器类型为SENSOR\_TYPE\_ID\_ORIENTATION。 |
| callback | Callback<[OrientationResponse](js-apis-sensor.md#orientationresponse)> | 是 | 注册方向传感器的回调函数，上报的数据类型为OrientationResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.on(sensor.SensorType.SENSOR_TYPE_ID_ORIENTATION, (data: sensor.OrientationResponse) => {
4. console.info('Succeeded in the device rotating at an angle around the X axis: ' + data.beta);
5. console.info('Succeeded in the device rotating at an angle around the Y axis: ' + data.gamma);
6. console.info('Succeeded in the device rotating at an angle around the Z axis: ' + data.alpha);
7. },
8. { interval: 100000000 }
9. );
```

### HEART\_RATE(deprecated)

PhonePC/2in1TabletTVWearable

on(type: SensorType.SENSOR\_TYPE\_ID\_HEART\_RATE, callback: Callback<HeartRateResponse>, options?: Options): void

监听心率传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.HEART\_RATE](js-apis-sensor.md#heart_rate9)9+代替。

**需要权限**：ohos.permission.HEALTH\_DATA

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_HEART\_RATE | 是 | 要订阅的心率传感器类型为SENSOR\_TYPE\_ID\_HEART\_RATE。 |
| callback | Callback<[HeartRateResponse](js-apis-sensor.md#heartrateresponse)> | 是 | 注册心率传感器的回调函数，上报的数据类型为HeartRateResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

### ROTATION\_VECTOR(deprecated)

PhonePC/2in1TabletTVWearable

on(type: SensorType.SENSOR\_TYPE\_ID\_ROTATION\_VECTOR,callback: Callback<RotationVectorResponse>,options?: Options): void

监听旋转矢量传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.ROTATION\_VECTOR](js-apis-sensor.md#rotation_vector9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_ROTATION\_VECTOR | 是 | 要订阅的旋转矢量传感器类型为SENSOR\_TYPE\_ID\_ROTATION\_VECTOR。 |
| callback | Callback<[RotationVectorResponse](js-apis-sensor.md#rotationvectorresponse)> | 是 | 注册旋转矢量传感器的回调函数，上报的数据类型为RotationVectorResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.on(sensor.SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR, (data: sensor.RotationVectorResponse) => {
4. console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
7. console.info('Succeeded in invoking on. Scalar quantity: ' + data.w);
8. },
9. { interval: 100000000 }
10. );
```

### WEAR\_DETECTION(deprecated)

PhonePC/2in1TabletTVWearable

on(type: SensorType.SENSOR\_TYPE\_ID\_WEAR\_DETECTION, callback: Callback<WearDetectionResponse>,options?: Options): void

监听所佩戴的检测传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.WEAR\_DETECTION](js-apis-sensor.md#wear_detection9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_WEAR\_DETECTION | 是 | 要订阅的佩戴检测传感器类型为SENSOR\_TYPE\_ID\_WEAR\_DETECTION。 |
| callback | Callback<[WearDetectionResponse](js-apis-sensor.md#weardetectionresponse)> | 是 | 注册佩戴检测传感器的回调函数，上报的数据类型为WearDetectionResponse。 |
| options | [Options](js-apis-sensor.md#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.on(sensor.SensorType.SENSOR_TYPE_ID_WEAR_DETECTION, (data: sensor.WearDetectionResponse) => {
4. console.info('Succeeded in invoking on. Wear status: ' + data.value);
5. },
6. { interval: 100000000 }
7. );
```

## sensor.once(deprecated)

PhonePC/2in1TabletTVWearable

### ACCELEROMETER(deprecated)

PhonePC/2in1TabletTVWearable

once(type: SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER, callback: Callback<AccelerometerResponse>): void

监听加速度传感器的数据变化一次。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.ACCELEROMETER](js-apis-sensor.md#accelerometer9-1)9+代替。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_ACCELEROMETER | 是 | 加速度传感器类型为SENSOR\_TYPE\_ID\_ACCELEROMETER。 |
| callback | Callback<[AccelerometerResponse](js-apis-sensor.md#accelerometerresponse)> | 是 | 注册一次加速度传感器的回调函数，上报的数据类型为AccelerometerResponse。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.once(sensor.SensorType.SENSOR_TYPE_ID_ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
4. console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
7. });
```

### LINEAR\_ACCELERATION(deprecated)

PhonePC/2in1TabletTVWearable

once(type: SensorType.SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION,callback:Callback<LinearAccelerometerResponse>): void

监听线性加速度传感器数据变化一次。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.LINEAR\_ACCELEROMETER](js-apis-sensor.md#linear_accelerometer9-1)9+代替。

**需要权限**：ohos.permission.ACCELERATION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION | 是 | 线性加速度传感器类型为SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION。 |
| callback | Callback<[LinearAccelerometerResponse](js-apis-sensor.md#linearaccelerometerresponse)> | 是 | 注册一次线性加速度传感器的回调函数，上报的数据类型为LinearAccelerometerResponse。 |

### ACCELEROMETER\_UNCALIBRATED(deprecated)

PhonePC/2in1TabletTVWearable

once(type: SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED,callback: Callback<AccelerometerUncalibratedResponse>): void

监听未校准加速度传感器的数据变化一次。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.ACCELEROMETER\_UNCALIBRATED](js-apis-sensor.md#accelerometer_uncalibrated9-1)9+代替。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED | 是 | 未校准加速度传感器类型为SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED。 |
| callback | Callback<[AccelerometerUncalibratedResponse](js-apis-sensor.md#accelerometeruncalibratedresponse)> | 是 | 注册一次未校准加速度传感器的回调函数，上报的数据类型为AccelerometerUncalibratedResponse。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.once(sensor.SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED, (data: sensor.AccelerometerUncalibratedResponse) => {
4. console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
7. console.info('Succeeded in invoking once. X-coordinate bias: ' + data.biasX);
8. console.info('Succeeded in invoking once. Y-coordinate bias: ' + data.biasY);
9. console.info('Succeeded in invoking once. Z-coordinate bias: ' + data.biasZ);
10. });
```

### GRAVITY(deprecated)

PhonePC/2in1TabletTVWearable

once(type: SensorType.SENSOR\_TYPE\_ID\_GRAVITY, callback: Callback<GravityResponse>): void

监听重力传感器的数据变化一次。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.GRAVITY](js-apis-sensor.md#gravity9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_GRAVITY | 是 | 重力传感器类型为SENSOR\_TYPE\_ID\_GRAVITY。 |
| callback | Callback<[GravityResponse](js-apis-sensor.md#gravityresponse)> | 是 | 注册一次重力传感器的回调函数，上报的数据类型为GravityResponse。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.once(sensor.SensorType.SENSOR_TYPE_ID_GRAVITY, (data: sensor.GravityResponse) => {
4. console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
7. });
```

### GYROSCOPE(deprecated)

PhonePC/2in1TabletTVWearable

once(type: SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE, callback: Callback<GyroscopeResponse>): void

监听陀螺仪传感器的数据变化一次。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.GYROSCOPE](js-apis-sensor.md#gyroscope9-1)9+代替。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_GYROSCOPE | 是 | 陀螺仪传感器类型为SENSOR\_TYPE\_ID\_GYROSCOPE。 |
| callback | Callback<[GyroscopeResponse](js-apis-sensor.md#gyroscoperesponse)> | 是 | 注册一次陀螺仪传感器的回调函数，上报的数据类型为GyroscopeResponse。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.once(sensor.SensorType.SENSOR_TYPE_ID_GYROSCOPE, (data: sensor.GyroscopeResponse) => {
4. console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
7. });
```

### GYROSCOPE\_UNCALIBRATED(deprecated)

PhonePC/2in1TabletTVWearable

once(type: SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED,callback: Callback<GyroscopeUncalibratedResponse>): void

监听未校准陀螺仪传感器的数据变化一次。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.GYROSCOPE\_UNCALIBRATED](js-apis-sensor.md#gyroscope_uncalibrated9-1)9+代替。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED | 是 | 未校准陀螺仪传感器类型为SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED。 |
| callback | Callback<[GyroscopeUncalibratedResponse](js-apis-sensor.md#gyroscopeuncalibratedresponse)> | 是 | 注册一次未校准陀螺仪传感器的回调函数，上报的数据类型为GyroscopeUncalibratedResponse。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.once(sensor.SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED, (data: sensor.GyroscopeUncalibratedResponse) => {
4. console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
7. console.info('Succeeded in invoking once. X-coordinate bias: ' + data.biasX);
8. console.info('Succeeded in invoking once. Y-coordinate bias: ' + data.biasY);
9. console.info('Succeeded in invoking once. Z-coordinate bias: ' + data.biasZ);
10. });
```

### SIGNIFICANT\_MOTION(deprecated)

PhonePC/2in1TabletTVWearable

once(type: SensorType.SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION,callback: Callback<SignificantMotionResponse>): void

监听有效运动传感器的数据变化一次。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.SIGNIFICANT\_MOTION](js-apis-sensor.md#significant_motion9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION | 是 | 有效运动传感器类型为SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION。 |
| callback | Callback<[SignificantMotionResponse](js-apis-sensor.md#significantmotionresponse)> | 是 | 注册一次有效运动传感器的回调函数，上报的数据类型为SignificantMotionResponse。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.once(sensor.SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION, (data: sensor.SignificantMotionResponse) => {
4. console.info('Succeeded in invoking once. Scalar data: ' + data.scalar);
5. });
```

### PEDOMETER\_DETECTION(deprecated)

PhonePC/2in1TabletTVWearable

once(type: SensorType.SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION,callback: Callback<PedometerDetectionResponse>): void

监听计步检测传感器数据变化一次。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.PEDOMETER\_DETECTION](js-apis-sensor.md#pedometer_detection9-1)9+代替。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION | 是 | 计步检测传感器类型为SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION。 |
| callback | Callback<[PedometerDetectionResponse](js-apis-sensor.md#pedometerdetectionresponse)> | 是 | 注册一次计步检测传感器的回调函数，上报的数据类型为PedometerDetectionResponse。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.once(sensor.SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, (data: sensor.PedometerDetectionResponse) => {
4. console.info('Succeeded in invoking once. Scalar data: ' + data.scalar);
5. });
```

### PEDOMETER(deprecated)

PhonePC/2in1TabletTVWearable

once(type: SensorType.SENSOR\_TYPE\_ID\_PEDOMETER, callback: Callback<PedometerResponse>): void

监听计步器传感器数据变化一次。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.PEDOMETER](js-apis-sensor.md#pedometer9-1)9+代替。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_PEDOMETER | 是 | 计步传感器类型为SENSOR\_TYPE\_ID\_PEDOMETER。 |
| callback | Callback<[PedometerResponse](js-apis-sensor.md#pedometerresponse)> | 是 | 注册一次计步传感器的回调函数，上报的数据类型为PedometerResponse。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.once(sensor.SensorType.SENSOR_TYPE_ID_PEDOMETER, (data: sensor.PedometerResponse) => {
4. console.info('Succeeded in invoking once. Steps: ' + data.steps);
5. });
```

### AMBIENT\_TEMPERATURE(deprecated)

PhonePC/2in1TabletTVWearable

once(type: SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE,callback: Callback<AmbientTemperatureResponse>): void

监听环境温度传感器数据变化一次。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.AMBIENT\_TEMPERATURE](js-apis-sensor.md#ambient_temperature9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE | 是 | 环境温度传感器类型为SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE。 |
| callback | Callback<[AmbientTemperatureResponse](js-apis-sensor.md#ambienttemperatureresponse)> | 是 | 注册一次环境温度传感器的回调函数，上报的数据类型为AmbientTemperatureResponse。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.once(sensor.SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE, (data: sensor.AmbientTemperatureResponse) => {
4. console.info('Succeeded in invoking once. Temperature: ' + data.temperature);
5. });
```

### MAGNETIC\_FIELD(deprecated)

PhonePC/2in1TabletTVWearable

once(type: SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD, callback: Callback<MagneticFieldResponse>): void

监听磁场传感器数据变化一次。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.MAGNETIC\_FIELD](js-apis-sensor.md#magnetic_field9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD | 是 | 磁场传感器类型为SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD。 |
| callback | Callback<[MagneticFieldResponse](js-apis-sensor.md#magneticfieldresponse)> | 是 | 注册一次磁场传感器的回调函数，上报的数据类型为MagneticFieldResponse。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.once(sensor.SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD, (data: sensor.MagneticFieldResponse) => {
4. console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
7. });
```

### MAGNETIC\_FIELD\_UNCALIBRATED(deprecated)

PhonePC/2in1TabletTVWearable

once(type: SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED,callback: Callback<MagneticFieldUncalibratedResponse>): void

监听未校准磁场传感器数据变化一次。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.MAGNETIC\_FIELD\_UNCALIBRATED](js-apis-sensor.md#magnetic_field_uncalibrated9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED | 是 | 未校准磁场传感器类型为SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED。 |
| callback | Callback<[MagneticFieldUncalibratedResponse](js-apis-sensor.md#magneticfielduncalibratedresponse)> | 是 | 注册一次未校准磁场传感器的回调函数，上报的数据类型为MagneticFieldUncalibratedResponse。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.once(sensor.SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED, (data: sensor.MagneticFieldUncalibratedResponse) => {
4. console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
7. console.info('Succeeded in invoking once. X-coordinate bias: ' + data.biasX);
8. console.info('Succeeded in invoking once. Y-coordinate bias: ' + data.biasY);
9. console.info('Succeeded in invoking once. Z-coordinate bias: ' + data.biasZ);
10. });
```

### PROXIMITY(deprecated)

PhonePC/2in1TabletTVWearable

once(type: SensorType.SENSOR\_TYPE\_ID\_PROXIMITY, callback: Callback<ProximityResponse>): void

监听接近光传感器数据变化一次。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.PROXIMITY](js-apis-sensor.md#proximity9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_PROXIMITY | 是 | 接近光传感器类型为SENSOR\_TYPE\_ID\_PROXIMITY。 |
| callback | Callback<[ProximityResponse](js-apis-sensor.md#proximityresponse)> | 是 | 注册一次接近光传感器的回调函数，上报的数据类型为ProximityResponse。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.once(sensor.SensorType.SENSOR_TYPE_ID_PROXIMITY, (data: sensor.ProximityResponse) => {
4. console.info('Succeeded in invoking once. Distance: ' + data.distance);
5. }
6. );
```

### HUMIDITY(deprecated)

PhonePC/2in1TabletTVWearable

once(type: SensorType.SENSOR\_TYPE\_ID\_HUMIDITY, callback: Callback<HumidityResponse>): void

监听湿度传感器数据变化一次。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.HUMIDITY](js-apis-sensor.md#humidity9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_HUMIDITY | 是 | 湿度传感器类型为SENSOR\_TYPE\_ID\_HUMIDITY。 |
| callback | Callback<[HumidityResponse](js-apis-sensor.md#humidityresponse)> | 是 | 注册一次湿度传感器的回调函数，上报的数据类型为HumidityResponse。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.once(sensor.SensorType.SENSOR_TYPE_ID_HUMIDITY, (data: sensor.HumidityResponse) => {
4. console.info('Succeeded in invoking once. Humidity: ' + data.humidity);
5. });
```

### BAROMETER(deprecated)

PhonePC/2in1TabletTVWearable

once(type: SensorType.SENSOR\_TYPE\_ID\_BAROMETER, callback: Callback<BarometerResponse>): void

监听气压计传感器数据变化一次。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.BAROMETER](js-apis-sensor.md#barometer9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_BAROMETER | 是 | 气压计传感器类型为SENSOR\_TYPE\_ID\_BAROMETER。 |
| callback | Callback<[BarometerResponse](js-apis-sensor.md#barometerresponse)> | 是 | 注册一次气压计传感器的回调函数，上报的数据类型为BarometerResponse。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.once(sensor.SensorType.SENSOR_TYPE_ID_BAROMETER, (data: sensor.BarometerResponse) => {
4. console.info('Succeeded in invoking once. Atmospheric pressure: ' + data.pressure);
5. });
```

### HALL(deprecated)

PhonePC/2in1TabletTVWearable

once(type: SensorType.SENSOR\_TYPE\_ID\_HALL, callback: Callback<HallResponse>): void

监听霍尔传感器数据变化一次。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.HALL](js-apis-sensor.md#hall9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_HALL | 是 | 霍尔传感器类型为SENSOR\_TYPE\_ID\_HALL。 |
| callback | Callback<[HallResponse](js-apis-sensor.md#hallresponse)> | 是 | 注册一次霍尔传感器的回调函数，上报的数据类型为HallResponse。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.once(sensor.SensorType.SENSOR_TYPE_ID_HALL, (data: sensor.HallResponse) => {
4. console.info('Succeeded in invoking once. Status: ' + data.status);
5. });
```

### AMBIENT\_LIGHT(deprecated)

PhonePC/2in1TabletTVWearable

once(type: SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT, callback: Callback<LightResponse>): void

监听环境光传感器数据变化一次。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.AMBIENT\_LIGHT](js-apis-sensor.md#ambient_light9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT | 是 | 环境光传感器类型为SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT。 |
| callback | Callback<[LightResponse](js-apis-sensor.md#lightresponse)> | 是 | 注册一次环境光传感器的回调函数，上报的数据类型为LightResponse。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.once(sensor.SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT, (data: sensor.LightResponse) => {
4. console.info('Succeeded in invoking once. invoking once. Illumination: ' + data.intensity);
5. });
```

### ORIENTATION(deprecated)

PhonePC/2in1TabletTVWearable

once(type: SensorType.SENSOR\_TYPE\_ID\_ORIENTATION, callback: Callback<OrientationResponse>): void

监听方向传感器数据变化一次。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.ORIENTATION](js-apis-sensor.md#orientation9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_ORIENTATION | 是 | 方向传感器类型为SENSOR\_TYPE\_ID\_ORIENTATION。 |
| callback | Callback<[OrientationResponse](js-apis-sensor.md#orientationresponse)> | 是 | 注册一次方向传感器的回调函数，上报的数据类型为OrientationResponse。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.once(sensor.SensorType.SENSOR_TYPE_ID_ORIENTATION, (data: sensor.OrientationResponse) => {
4. console.info('Succeeded in invoking the device rotating at an angle around the X axis: ' + data.beta);
5. console.info('Succeeded in invoking the device rotating at an angle around the Y axis: ' + data.gamma);
6. console.info('Succeeded in invoking the device rotating at an angle around the Z axis: ' + data.alpha);
7. });
```

### ROTATION\_VECTOR(deprecated)

PhonePC/2in1TabletTVWearable

once(type: SensorType.SENSOR\_TYPE\_ID\_ROTATION\_VECTOR, callback: Callback<RotationVectorResponse>): void

监听旋转矢量传感器数据变化一次。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.ROTATION\_VECTOR](js-apis-sensor.md#rotation_vector9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_ROTATION\_VECTOR | 是 | 旋转矢量传感器类型为SENSOR\_TYPE\_ID\_ROTATION\_VECTOR。 |
| callback | Callback<[RotationVectorResponse](js-apis-sensor.md#rotationvectorresponse)> | 是 | 注册一次旋转矢量传感器的回调函数，上报的数据类型为RotationVectorResponse。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.once(sensor.SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR, (data: sensor.RotationVectorResponse) => {
4. console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
7. console.info('Succeeded in invoking once. Scalar quantity: ' + data.w);
8. });
```

### HEART\_RATE(deprecated)

PhonePC/2in1TabletTVWearable

once(type: SensorType.SENSOR\_TYPE\_ID\_HEART\_RATE, callback: Callback<HeartRateResponse>): void

监听心率传感器数据变化一次。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.HEART\_RATE](js-apis-sensor.md#heart_rate9-1)9+代替。

**需要权限**：ohos.permission.HEART\_RATE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_HEART\_RATE | 是 | 心率传感器类型为SENSOR\_TYPE\_ID\_HEART\_RATE。 |
| callback | Callback<[HeartRateResponse](js-apis-sensor.md#heartrateresponse)> | 是 | 注册一次心率传感器的回调函数，上报的数据类型为HeartRateResponse。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.once(sensor.SensorType.SENSOR_TYPE_ID_HEART_RATE, (data: sensor.HeartRateResponse) => {
4. console.info("Succeeded in invoking once. Heart rate: " + data.heartRate);
5. });
```

### WEAR\_DETECTION(deprecated)

PhonePC/2in1TabletTVWearable

once(type: SensorType.SENSOR\_TYPE\_ID\_WEAR\_DETECTION, callback: Callback<WearDetectionResponse>): void

监听所佩戴的检测传感器的数据变化一次。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.WEAR\_DETECTION](js-apis-sensor.md#wear_detection9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_WEAR\_DETECTION | 是 | 佩戴检测传感器类型为SENSOR\_TYPE\_ID\_WEAR\_DETECTION。 |
| callback | Callback<[WearDetectionResponse](js-apis-sensor.md#weardetectionresponse)> | 是 | 注册一次穿戴检测传感器的回调函数，上报的数据类型为WearDetectionResponse。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. sensor.once(sensor.SensorType.SENSOR_TYPE_ID_WEAR_DETECTION, (data: sensor.WearDetectionResponse) => {
4. console.info("Succeeded in invoking once. Wear status: " + data.value);
5. });
```

## sensor.off(deprecated)

PhonePC/2in1TabletTVWearable

### ACCELEROMETER(deprecated)

PhonePC/2in1TabletTVWearable

off(type: SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER, callback?: Callback<AccelerometerResponse>): void

取消订阅传感器数据。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.ACCELEROMETER9+](js-apis-sensor.md#accelerometer9-2)代替。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_ACCELEROMETER | 是 | 要取消订阅的加速度传感器类型为SENSOR\_TYPE\_ID\_ACCELEROMETER。 |
| callback | Callback<[AccelerometerResponse](js-apis-sensor.md#accelerometerresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. function callback(data: sensor.AccelerometerResponse) {
4. console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
7. }

9. sensor.off(sensor.SensorType.SENSOR_TYPE_ID_ACCELEROMETER, callback);
```

### ACCELEROMETER\_UNCALIBRATED(deprecated)

PhonePC/2in1TabletTVWearable

off(type: SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED, callback?: Callback<AccelerometerUncalibratedResponse>): void

取消订阅传感器数据。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.ACCELEROMETER\_UNCALIBRATED](js-apis-sensor.md#accelerometer_uncalibrated9-2)9+代替。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED | 是 | 要取消订阅的未校准加速度计传感器类型为SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED。 |
| callback | Callback<[AccelerometerUncalibratedResponse](js-apis-sensor.md#accelerometeruncalibratedresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. function callback(data: sensor.AccelerometerUncalibratedResponse) {
4. console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
7. console.info('Succeeded in invoking off. X-coordinate bias: ' + data.biasX);
8. console.info('Succeeded in invoking off. Y-coordinate bias: ' + data.biasY);
9. console.info('Succeeded in invoking off. Z-coordinate bias: ' + data.biasZ);
10. }

12. sensor.off(sensor.SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED, callback);
```

### AMBIENT\_LIGHT(deprecated)

PhonePC/2in1TabletTVWearable

off(type: SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT, callback?: Callback<LightResponse>): void

取消订阅传感器数据。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.AMBIENT\_LIGHT](js-apis-sensor.md#ambient_light9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT | 是 | 要取消订阅的环境光传感器类型为SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT。 |
| callback | Callback<[LightResponse](js-apis-sensor.md#lightresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. function callback(data: sensor.LightResponse) {
4. console.info('Succeeded in invoking off. Illumination: ' + data.intensity);
5. }

7. sensor.off(sensor.SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT, callback);
```

### AMBIENT\_TEMPERATURE(deprecated)

PhonePC/2in1TabletTVWearable

off(type: SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE, callback?: Callback<AmbientTemperatureResponse>): void

取消订阅传感器数据。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.AMBIENT\_TEMPERATURE](js-apis-sensor.md#ambient_temperature9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE | 是 | 要取消订阅的环境温度传感器类型为SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE。 |
| callback | Callback<[AmbientTemperatureResponse](js-apis-sensor.md#ambienttemperatureresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. function callback(data: sensor.AmbientTemperatureResponse) {
4. console.info('Succeeded in invoking off. Temperature: ' + data.temperature);
5. }

7. sensor.off(sensor.SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE, callback);
```

### BAROMETER(deprecated)

PhonePC/2in1TabletTVWearable

off(type: SensorType.SENSOR\_TYPE\_ID\_BAROMETER, callback?: Callback<BarometerResponse>): void

取消订阅传感器数据。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.BAROMETER](js-apis-sensor.md#barometer9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_BAROMETER | 是 | 要取消订阅的气压计传感器类型为SENSOR\_TYPE\_ID\_BAROMETER。 |
| callback | Callback<[BarometerResponse](js-apis-sensor.md#barometerresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. function callback(data: sensor.BarometerResponse) {
4. console.info('Succeeded in invoking off. Atmospheric pressure: ' + data.pressure);
5. }

7. sensor.off(sensor.SensorType.SENSOR_TYPE_ID_BAROMETER, callback);
```

### GRAVITY(deprecated)

PhonePC/2in1TabletTVWearable

off(type: SensorType.SENSOR\_TYPE\_ID\_GRAVITY, callback?: Callback<GravityResponse>): void

取消订阅传感器数据。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.GRAVITY](js-apis-sensor.md#gravity9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_GRAVITY | 是 | 要取消订阅的重力传感器类型为SENSOR\_TYPE\_ID\_GRAVITY。 |
| callback | Callback<[GravityResponse](js-apis-sensor.md#gravityresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. function callback(data: sensor.GravityResponse) {
4. console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
7. }

9. sensor.off(sensor.SensorType.SENSOR_TYPE_ID_GRAVITY, callback);
```

### GYROSCOPE(deprecated)

PhonePC/2in1TabletTVWearable

off(type: SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE, callback?: Callback<GyroscopeResponse>): void

取消订阅传感器数据。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.GYROSCOPE](js-apis-sensor.md#gyroscope9-2)9+代替。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_GYROSCOPE | 是 | 要取消订阅的陀螺仪传感器类型为SENSOR\_TYPE\_ID\_GYROSCOPE。 |
| callback | Callback<[GyroscopeResponse](js-apis-sensor.md#gyroscoperesponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. function callback(data: sensor.GyroscopeResponse) {
4. console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
7. }

9. sensor.off(sensor.SensorType.SENSOR_TYPE_ID_GYROSCOPE, callback);
```

### GYROSCOPE\_UNCALIBRATED(deprecated)

PhonePC/2in1TabletTVWearable

off(type: SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED, callback?: Callback<GyroscopeUncalibratedResponse>): void

取消订阅传感器数据。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.GYROSCOPE\_UNCALIBRATED](js-apis-sensor.md#gyroscope_uncalibrated9-2)9+代替。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED | 是 | 要取消订阅的未校准陀螺仪传感器类型为SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED。 |
| callback | Callback<[GyroscopeUncalibratedResponse](js-apis-sensor.md#gyroscopeuncalibratedresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. function callback(data: sensor.GyroscopeUncalibratedResponse) {
4. console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
7. }

9. sensor.off(sensor.SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED, callback);
```

### HALL(deprecated)

PhonePC/2in1TabletTVWearable

off(type: SensorType.SENSOR\_TYPE\_ID\_HALL, callback?: Callback<HallResponse>): void

取消订阅传感器数据。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.HALL](js-apis-sensor.md#hall9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_HALL | 是 | 要取消订阅的霍尔传感器类型为SENSOR\_TYPE\_ID\_HALL。 |
| callback | Callback<[HallResponse](js-apis-sensor.md#hallresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. function callback(data: sensor.HallResponse) {
4. console.info('Succeeded in invoking off. Status: ' + data.status);
5. }

7. sensor.off(sensor.SensorType.SENSOR_TYPE_ID_HALL, callback);
```

### HEART\_RATE(deprecated)

PhonePC/2in1TabletTVWearable

off(type: SensorType.SENSOR\_TYPE\_ID\_HEART\_RATE, callback?: Callback<HeartRateResponse>): void

取消订阅传感器数据。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.HEART\_RATE](js-apis-sensor.md#heart_rate9-2)9+代替。

**需要权限**：ohos.permission.HEALTH\_DATA

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_HEART\_RATE | 是 | 要取消订阅的心率传感器类型为SENSOR\_TYPE\_ID\_HEART\_RATE。 |
| callback | Callback<[HeartRateResponse](js-apis-sensor.md#heartrateresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. function callback(data: sensor.HeartRateResponse) {
4. console.info('Succeeded in invoking off. Heart rate: ' + data.heartRate);
5. }

7. sensor.off(sensor.SensorType.SENSOR_TYPE_ID_HEART_RATE, callback);
```

### HUMIDITY(deprecated)

PhonePC/2in1TabletTVWearable

off(type: SensorType.SENSOR\_TYPE\_ID\_HUMIDITY, callback?: Callback<HumidityResponse>): void

取消订阅传感器数据。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.HUMIDITY](js-apis-sensor.md#humidity9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_HUMIDITY | 是 | 要取消订阅的湿度传感器类型为SENSOR\_TYPE\_ID\_HUMIDITY。 |
| callback | Callback<[HumidityResponse](js-apis-sensor.md#humidityresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. function callback(data: sensor.HumidityResponse) {
4. console.info('Succeeded in invoking off. Humidity: ' + data.humidity);
5. }

7. sensor.off(sensor.SensorType.SENSOR_TYPE_ID_HUMIDITY, callback);
```

### LINEAR\_ACCELERATION(deprecated)

PhonePC/2in1TabletTVWearable

off(type: SensorType.SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION, callback?: Callback<LinearAccelerometerResponse>): void

取消订阅传感器数据。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.LINEAR\_ACCELEROMETER](js-apis-sensor.md#linear_accelerometer9-2)9+代替。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION | 是 | 要取消订阅的线性加速度传感器类型为SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION。 |
| callback | Callback<[LinearAccelerometerResponse](js-apis-sensor.md#linearaccelerometerresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. function callback(data: sensor.LinearAccelerometerResponse) {
4. console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
7. }

9. sensor.off(sensor.SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION, callback);
```

### MAGNETIC\_FIELD(deprecated)

PhonePC/2in1TabletTVWearable

off(type: SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD, callback?: Callback<MagneticFieldResponse>): void

取消订阅传感器数据。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.MAGNETIC\_FIELD](js-apis-sensor.md#magnetic_field9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD | 是 | 要取消订阅的磁场传感器类型为SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD。 |
| callback | Callback<[MagneticFieldResponse](js-apis-sensor.md#magneticfieldresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. function callback(data: sensor.MagneticFieldResponse) {
4. console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
7. }

9. sensor.off(sensor.SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD, callback);
```

### MAGNETIC\_FIELD\_UNCALIBRATED(deprecated)

PhonePC/2in1TabletTVWearable

off(type: SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED, callback?: Callback<MagneticFieldUncalibratedResponse>): void

取消订阅传感器数据。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.MAGNETIC\_FIELD\_UNCALIBRATED](js-apis-sensor.md#magnetic_field_uncalibrated9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED | 是 | 要取消订阅的未校准磁场传感器类型为SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED。 |
| callback | Callback<[MagneticFieldUncalibratedResponse](js-apis-sensor.md#magneticfielduncalibratedresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. function callback(data: sensor.MagneticFieldUncalibratedResponse) {
4. console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
7. console.info('Succeeded in invoking off. X-coordinate bias: ' + data.biasX);
8. console.info('Succeeded in invoking off. Y-coordinate bias: ' + data.biasY);
9. console.info('Succeeded in invoking off. Z-coordinate bias: ' + data.biasZ);
10. }

12. sensor.off(sensor.SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED, callback);
```

### ORIENTATION(deprecated)

PhonePC/2in1TabletTVWearable

off(type: SensorType.SENSOR\_TYPE\_ID\_ORIENTATION, callback?: Callback<OrientationResponse>): void

取消订阅传感器数据。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.ORIENTATION](js-apis-sensor.md#orientation9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_ORIENTATION | 是 | 要取消订阅的方向传感器类型为SENSOR\_TYPE\_ID\_ORIENTATION。 |
| callback | Callback<[OrientationResponse](js-apis-sensor.md#orientationresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. function callback(data: sensor.OrientationResponse) {
4. console.info('Succeeded in invoking off. The device rotates at an angle around the X axis: ' + data.beta);
5. console.info('Succeeded in invoking off. The device rotates at an angle around the Y axis: ' + data.gamma);
6. console.info('Succeeded in invoking off. The device rotates at an angle around the Z axis: ' + data.alpha);
7. }

9. sensor.off(sensor.SensorType.SENSOR_TYPE_ID_ORIENTATION, callback);
```

### PEDOMETER(deprecated)

PhonePC/2in1TabletTVWearable

off(type: SensorType.SENSOR\_TYPE\_ID\_PEDOMETER, callback?: Callback<PedometerResponse>): void

取消订阅传感器数据。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.PEDOMETER](js-apis-sensor.md#pedometer9-2)9+代替。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_PEDOMETER | 是 | 要取消订阅的计步传感器类型为SENSOR\_TYPE\_ID\_PEDOMETER。 |
| callback | Callback<[PedometerResponse](js-apis-sensor.md#pedometerresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. function callback(data: sensor.PedometerResponse) {
4. console.info('Succeeded in invoking off. Steps: ' + data.steps);
5. }

7. sensor.off(sensor.SensorType.SENSOR_TYPE_ID_PEDOMETER, callback);
```

### PEDOMETER\_DETECTION(deprecated)

PhonePC/2in1TabletTVWearable

off(type: SensorType.SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION, callback?: Callback<PedometerDetectionResponse>): void

取消订阅传感器数据。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.PEDOMETER\_DETECTION](js-apis-sensor.md#pedometer_detection9-2)9+代替。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION | 是 | 要取消订阅的计步检测传感器类型为SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION。 |
| callback | Callback<[PedometerDetectionResponse](js-apis-sensor.md#pedometerdetectionresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. function callback(data: sensor.PedometerDetectionResponse) {
4. console.info('Succeeded in invoking off. Scalar data: ' + data.scalar);
5. }

7. sensor.off(sensor.SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, callback);
```

### PROXIMITY(deprecated)

PhonePC/2in1TabletTVWearable

off(type: SensorType.SENSOR\_TYPE\_ID\_PROXIMITY, callback?: Callback<ProximityResponse>): void

取消订阅传感器数据。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.PROXIMITY](js-apis-sensor.md#proximity9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_PROXIMITY | 是 | 要取消订阅的接近光传感器类型为SENSOR\_TYPE\_ID\_PROXIMITY。 |
| callback | Callback<[ProximityResponse](js-apis-sensor.md#proximityresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. function callback(data: sensor.ProximityResponse) {
4. console.info('Succeeded in invoking off. Distance: ' + data.distance);
5. }

7. sensor.off(sensor.SensorType.SENSOR_TYPE_ID_PROXIMITY, callback);
```

### ROTATION\_VECTOR(deprecated)

PhonePC/2in1TabletTVWearable

off(type: SensorType.SENSOR\_TYPE\_ID\_ROTATION\_VECTOR, callback?: Callback<RotationVectorResponse>): void

取消订阅传感器数据。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.ROTATION\_VECTOR](js-apis-sensor.md#rotation_vector9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_ROTATION\_VECTOR | 是 | 要取消订阅的旋转矢量传感器类型为SENSOR\_TYPE\_ID\_ROTATION\_VECTOR。 |
| callback | Callback<[RotationVectorResponse](js-apis-sensor.md#rotationvectorresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. function callback(data: sensor.RotationVectorResponse) {
4. console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
5. console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
6. console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
7. console.info('Succeeded in invoking off. Scalar quantity: ' + data.w);
8. }

10. sensor.off(sensor.SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR, callback);
```

### SIGNIFICANT\_MOTION(deprecated)

PhonePC/2in1TabletTVWearable

off(type: SensorType.SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION, callback?: Callback<SignificantMotionResponse>): void

取消订阅有效运动传感器数据。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.SIGNIFICANT\_MOTION](js-apis-sensor.md#significant_motion9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION | 是 | 要取消订阅的有效运动传感器类型为SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION。 |
| callback | Callback<[SignificantMotionResponse](js-apis-sensor.md#significantmotionresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. function callback(data: sensor.SignificantMotionResponse) {
4. console.info('Succeeded in invoking off. Scalar data: ' + data.scalar);
5. }

7. sensor.off(sensor.SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION, callback);
```

### WEAR\_DETECTION(deprecated)

PhonePC/2in1TabletTVWearable

off(type: SensorType.SENSOR\_TYPE\_ID\_WEAR\_DETECTION, callback?: Callback<WearDetectionResponse>): void

取消订阅传感器数据。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.WEAR\_DETECTION](js-apis-sensor.md#wear_detection9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SensorType](js-apis-sensor.md#sensortypedeprecated).SENSOR\_TYPE\_ID\_WEAR\_DETECTION | 是 | 要取消订阅的佩戴检测传感器类型为SENSOR\_TYPE\_ID\_WEAR\_DETECTION。 |
| callback | Callback<[WearDetectionResponse](js-apis-sensor.md#weardetectionresponse)> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';

3. function accCallback(data: sensor.WearDetectionResponse) {
4. console.info('Succeeded in invoking off. Wear status: ' + data.value);
5. }

7. sensor.off(sensor.SensorType.SENSOR_TYPE_ID_WEAR_DETECTION, accCallback);
```

## sensor.transformCoordinateSystem(deprecated)

PhonePC/2in1TabletTVWearable

transformCoordinateSystem(inRotationVector: Array<number>, coordinates: CoordinatesOptions, callback: AsyncCallback<Array<number>>): void

旋转提供的旋转矩阵，使其可以以不同的方式表示坐标系，使用Callback异步方式返回结果。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.transformRotationMatrix](js-apis-sensor.md#sensortransformrotationmatrix9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inRotationVector | Array<number> | 是 | 表示旋转矩阵。 |
| coordinates | [CoordinatesOptions](js-apis-sensor.md#coordinatesoptions) | 是 | 表示坐标系方向。 |
| callback | AsyncCallback<Array<number>> | 是 | 异步返回转换后的旋转矩阵。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. sensor.transformCoordinateSystem([1, 0, 0, 0, 1, 0, 0, 0, 1], { x: 2, y: 3 },
5. (err: BusinessError, data: Array<number>) => {
6. if (err) {
7. console.error(`Failed to operate. Code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info("Succeeded in starting Operation. Data obtained: " + data);
11. for (let i = 0; i < data.length; i++) {
12. console.info("Succeeded in getting transformCoordinateSystem data[ " + i + "] = " + data[i]);
13. }
14. })
```

## sensor.transformCoordinateSystem(deprecated)

PhonePC/2in1TabletTVWearable

transformCoordinateSystem(inRotationVector: Array<number>, coordinates: CoordinatesOptions): Promise<Array<number>>

旋转提供的旋转矩阵，使其可以以不同的方式表示坐标系，使用Promise异步方式返回结果。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.transformRotationMatrix](js-apis-sensor.md#sensortransformrotationmatrix9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inRotationVector | Array<number> | 是 | 表示旋转矩阵。 |
| coordinates | [CoordinatesOptions](js-apis-sensor.md#coordinatesoptions) | 是 | 表示坐标系方向。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | 使用异步方式返回转换后的旋转矩阵。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const promise = sensor.transformCoordinateSystem([1, 0, 0, 0, 1, 0, 0, 0, 1], { x: 2, y: 3 });
5. promise.then((data: Array<number>) => {
6. console.info("Succeeded in starting Operation");
7. for (let i = 0; i < data.length; i++) {
8. console.info("Succeeded in getting transformCoordinateSystem data[ " + i + "] = " + data[i]);
9. }
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to operate.`);
12. })
```

## sensor.getGeomagneticField(deprecated)

PhonePC/2in1TabletTVWearable

getGeomagneticField(locationOptions: LocationOptions, timeMillis: number, callback: AsyncCallback<GeomagneticResponse>): void

获取地球上特定位置的地磁场，使用callback异步方式返回结果。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getGeomagneticInfo](js-apis-sensor.md#sensorgetgeomagneticinfo9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locationOptions | [LocationOptions](js-apis-sensor.md#locationoptions) | 是 | 地理位置。 |
| timeMillis | number | 是 | 表示获取磁偏角的时间，单位为毫秒。 |
| callback | AsyncCallback<[GeomagneticResponse](js-apis-sensor.md#geomagneticresponse)> | 是 | 异步返回磁场信息。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. sensor.getGeomagneticField({ latitude: 80, longitude: 0, altitude: 0 }, 1580486400000,
5. (err: BusinessError, data: sensor.GeomagneticResponse) => {
6. if (err) {
7. console.error(`Failed to operate. Code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info('Succeeded in getting sensor_getGeomagneticField_callback x: ' + data.x + ',y: ' + data.y + ',z: ' +
11. data.z + ',geomagneticDip: ' + data.geomagneticDip + ',deflectionAngle: ' + data.deflectionAngle +
12. ',levelIntensity: ' + data.levelIntensity + ',totalIntensity: ' + data.totalIntensity);
13. });
```

## sensor.getGeomagneticField(deprecated)

PhonePC/2in1TabletTVWearable

getGeomagneticField(locationOptions: LocationOptions, timeMillis: number): Promise<GeomagneticResponse>

获取地球上特定位置的地磁场，使用Promise异步方式返回结果。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getGeomagneticInfo](js-apis-sensor.md#sensorgetgeomagneticinfo9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locationOptions | [LocationOptions](js-apis-sensor.md#locationoptions) | 是 | 地理位置。 |
| timeMillis | number | 是 | 表示获取磁偏角的时间，单位为毫秒。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[GeomagneticResponse](js-apis-sensor.md#geomagneticresponse)> | 使用异步方式返回磁场信息。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const promise = sensor.getGeomagneticField({ latitude: 80, longitude: 0, altitude: 0 }, 1580486400000);
5. promise.then((data: sensor.GeomagneticResponse) => {
6. console.info('Succeeded in getting sensor_getGeomagneticField_promise x: ' + data.x + ',y: ' + data.y + ',z: ' +
7. data.z + ',geomagneticDip: ' + data.geomagneticDip + ',deflectionAngle: ' + data.deflectionAngle +
8. ',levelIntensity: ' + data.levelIntensity + ',totalIntensity: ' + data.totalIntensity);
9. }).catch((reason: BusinessError) => {
10. console.error(`Failed to operate.`);
11. })
```

## sensor.getAltitude(deprecated)

PhonePC/2in1TabletTVWearable

getAltitude(seaPressure: number, currentPressure: number, callback: AsyncCallback<number>): void

根据气压值获取设备所在的海拔高度，使用Callback异步方式返回结果。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getDeviceAltitude](js-apis-sensor.md#sensorgetdevicealtitude9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| seaPressure | number | 是 | 表示海平面气压值，单位为hPa。 |
| currentPressure | number | 是 | 表示设备所在高度的气压值，单位为hPa。 |
| callback | AsyncCallback<number> | 是 | 异步返回设备所在的海拔高度，单位为米。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. sensor.getAltitude(0, 200, (err: BusinessError, data: number) => {
5. if (err) {
6. console.error(`Failed to operate. Code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info("Succeeded in getting getAltitude interface get data: " + data);
10. });
```

## sensor.getAltitude(deprecated)

PhonePC/2in1TabletTVWearable

getAltitude(seaPressure: number, currentPressure: number): Promise<number>

根据气压值获取设备所在的海拔高度，使用Promise异步方式返回结果。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getDeviceAltitude](js-apis-sensor.md#sensorgetdevicealtitude9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| seaPressure | number | 是 | 表示海平面气压值，单位为hPa。 |
| currentPressure | number | 是 | 表示设备所在高度的气压值，单位为hPa。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 使用异步方式返回设备所在的海拔高度（单位：米）。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const promise = sensor.getAltitude(0, 200);
5. promise.then((data: number) => {
6. console.info('Succeeded in getting sensor_getAltitude_Promise success', data);
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to operate.`);
9. })
```

## sensor.getGeomagneticDip(deprecated)

PhonePC/2in1TabletTVWearable

getGeomagneticDip(inclinationMatrix: Array<number>, callback: AsyncCallback<number>): void

根据倾斜矩阵计算地磁倾斜角，使用Callback异步方式返回结果。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getInclination](js-apis-sensor.md#sensorgetinclination9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inclinationMatrix | Array<number> | 是 | 表示倾斜矩阵。 |
| callback | AsyncCallback<number> | 是 | 异步返回地磁倾斜角，单位为弧度。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. sensor.getGeomagneticDip([1, 0, 0, 0, 1, 0, 0, 0, 1], (err: BusinessError, data: number) => {
5. if (err) {
6. console.error(`Failed to register data. Code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info("Succeeded in getting getGeomagneticDip interface get data: " + data);
10. })
```

## sensor.getGeomagneticDip(deprecated)

PhonePC/2in1TabletTVWearable

getGeomagneticDip(inclinationMatrix: Array<number>): Promise<number>

根据倾斜矩阵计算地磁倾斜角，使用Promise异步方式返回结果。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getInclination](js-apis-sensor.md#sensorgetinclination9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inclinationMatrix | Array<number> | 是 | 表示倾斜矩阵。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 使用异步方式返回地磁倾斜角，单位为弧度。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const promise = sensor.getGeomagneticDip([1, 0, 0, 0, 1, 0, 0, 0, 1]);
5. promise.then((data: number) => {
6. console.info('Succeeded in get GeomagneticDip_promise', data);
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to operate.`);
9. })
```

## sensor. getAngleModify(deprecated)

PhonePC/2in1TabletTVWearable

getAngleModify(currentRotationMatrix: Array<number>, preRotationMatrix: Array<number>, callback: AsyncCallback<Array<number>>): void

获取两个旋转矩阵之间的角度变化，使用Callback异步方式返回结果。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getAngleVariation](js-apis-sensor.md#sensorgetanglevariation9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| currentRotationMatrix | Array<number> | 是 | 表示当前旋转矩阵。 |
| preRotationMatrix | Array<number> | 是 | 表示旋转矩阵。 |
| callback | AsyncCallback<Array<number>> | 是 | 异步返回z、x、y轴方向的旋转角度变化，单位度（°）。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. sensor.getAngleModify([1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0.87, -0.50, 0, 0.50, 0.87],
5. (err: BusinessError, data: Array<number>) => {
6. if (err) {
7. console.error(`Failed to register data. Code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. for (let i = 0; i < data.length; i++) {
11. console.info("data[" + i + "]: " + data[i]);
12. }
13. })
```

## sensor. getAngleModify(deprecated)

PhonePC/2in1TabletTVWearable

getAngleModify(currentRotationMatrix: Array<number>, preRotationMatrix: Array<number>): Promise<Array<number>>

获取两个旋转矩阵之间的角度变化，使用Promise异步方式返回结果。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getAngleVariation](js-apis-sensor.md#sensorgetanglevariation9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| currentRotationMatrix | Array<number> | 是 | 表示当前旋转矩阵。 |
| preRotationMatrix | Array<number> | 是 | 表示旋转矩阵。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | 使用异步方式返回z、x、y轴方向的旋转角度变化，单位度（°）。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const promise = sensor.getAngleModify([1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0.87, -0.50, 0, 0.50, 0.87]);
5. promise.then((data: Array<number>) => {
6. console.info('Succeeded in getting AngleModify_promise.');
7. for (let i = 0; i < data.length; i++) {
8. console.info("Succeeded in getting data[" + i + "]: " + data[i]);
9. }
10. }).catch((reason: BusinessError) => {
11. let e: BusinessError = reason as BusinessError;
12. console.info("Succeeded in getting promise::catch", e);
13. })
```

## sensor.createRotationMatrix(deprecated)

PhonePC/2in1TabletTVWearable

createRotationMatrix(rotationVector: Array<number>, callback: AsyncCallback<Array<number>>): void

将旋转矢量转换为旋转矩阵，使用Callback异步方式返回结果。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getRotationMatrix](js-apis-sensor.md#sensorgetrotationmatrix9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotationVector | Array<number> | 是 | 表示旋转矢量。 |
| callback | AsyncCallback<Array<number>> | 是 | 异步返回旋转矩阵。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. sensor.createRotationMatrix([0.20046076, 0.21907, 0.73978853, 0.60376877],
5. (err: BusinessError, data: Array<number>) => {
6. if (err) {
7. console.error(`Failed to register data. Code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. for (let i = 0; i < data.length; i++) {
11. console.info("Succeeded in getting data[" + i + "]: " + data[i]);
12. }
13. })
```

## sensor.createRotationMatrix(deprecated)

PhonePC/2in1TabletTVWearable

createRotationMatrix(rotationVector: Array<number>): Promise<Array<number>>

将旋转矢量转换为旋转矩阵，使用Promise异步方式返回结果。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getRotationMatrix](js-apis-sensor.md#sensorgetrotationmatrix9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotationVector | Array<number> | 是 | 表示旋转矢量。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | 使用异步方式返回旋转矩阵。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const promise = sensor.createRotationMatrix([0.20046076, 0.21907, 0.73978853, 0.60376877]);
5. promise.then((data: Array<number>) => {
6. console.info('Succeeded in getting createRotationMatrix_promise');
7. for (let i = 0; i < data.length; i++) {
8. console.info("data[" + i + "]: " + data[i]);
9. }
10. }).catch((reason: BusinessError) => {
11. console.info("Succeeded in getting promise::catch", reason);
12. })
```

## sensor.createQuaternion(deprecated)

PhonePC/2in1TabletTVWearable

createQuaternion(rotationVector: Array<number>, callback: AsyncCallback<Array<number>>): void

将旋转矢量转换为四元数，使用Callback异步方式返回结果。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getQuaternion](js-apis-sensor.md#sensorgetquaternion9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotationVector | Array<number> | 是 | 表示旋转矢量。 |
| callback | AsyncCallback<Array<number>> | 是 | 异步返回四元数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. sensor.createQuaternion([0.20046076, 0.21907, 0.73978853, 0.60376877],
5. (err: BusinessError, data: Array<number>) => {
6. if (err) {
7. console.error(`Failed to register data. Code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. for (let i = 0; i < data.length; i++) {
11. console.info("Succeeded in getting data[" + i + "]: " + data[i]);
12. }
13. })
```

## sensor.createQuaternion(deprecated)

PhonePC/2in1TabletTVWearable

createQuaternion(rotationVector: Array<number>): Promise<Array<number>>

将旋转矢量转换为四元数，使用Promise异步方式返回结果。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getQuaternion](js-apis-sensor.md#sensorgetquaternion9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotationVector | Array<number> | 是 | 表示旋转矢量。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | 使用异步方式返回四元数。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const promise = sensor.createQuaternion([0.20046076, 0.21907, 0.73978853, 0.60376877]);
5. promise.then((data: Array<number>) => {
6. console.info('Succeeded in getting createQuaternion_promise');
7. for (let i = 0; i < data.length; i++) {
8. console.info("data[" + i + "]: " + data[i]);
9. }
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to get promise.`);
12. })
```

## sensor.getDirection(deprecated)

PhonePC/2in1TabletTVWearable

getDirection(rotationMatrix: Array<number>, callback: AsyncCallback<Array<number>>): void

根据旋转矩阵计算设备的方向，使用Callback异步方式返回结果。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getOrientation](js-apis-sensor.md#sensorgetorientation9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotationMatrix | Array<number> | 是 | 表示旋转矩阵。 |
| callback | AsyncCallback<Array<number>> | 是 | 异步返回围绕z、x、y轴方向的旋转角度，单位度（°）。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. sensor.getDirection([1, 0, 0, 0, 1, 0, 0, 0, 1], (err: BusinessError, data: Array<number>) => {
5. if (err) {
6. console.error(`Failed to register data. Code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info("Succeeded in getting getDirection interface get data: " + data);
10. for (let i = 1; i < data.length; i++) {
11. console.info("Succeeded in getting sensor_getDirection_callback" + data[i]);
12. }
13. })
```

## sensor.getDirection(deprecated)

PhonePC/2in1TabletTVWearable

getDirection(rotationMatrix: Array<number>): Promise<Array<number>>

根据旋转矩阵计算设备的方向，使用Promise异步方式返回结果。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getOrientation](js-apis-sensor.md#sensorgetorientation9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotationMatrix | Array<number> | 是 | 表示旋转矩阵。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | 使用异步方式返回围绕z、x、y轴方向的旋转角度，单位度（°）。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const promise = sensor.getDirection([1, 0, 0, 0, 1, 0, 0, 0, 1]);
5. promise.then((data: Array<number>) => {
6. console.info('Succeeded in getting sensor_getAltitude_Promise', data);
7. for (let i = 1; i < data.length; i++) {
8. console.info("Succeeded in getting sensor_getDirection_promise" + data[i]);
9. }
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to get promise.`);
12. })
```

## sensor.createRotationMatrix(deprecated)

PhonePC/2in1TabletTVWearable

createRotationMatrix(gravity: Array<number>, geomagnetic: Array<number>, callback: AsyncCallback<RotationMatrixResponse>): void

根据重力矢量和地磁矢量计算旋转矩阵，使用Callback异步方式返回结果。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getRotationMatrix](js-apis-sensor.md#sensorgetrotationmatrix9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| gravity | Array<number> | 是 | 表示重力向量。 |
| geomagnetic | Array<number> | 是 | 表示地磁矢量。 |
| callback | AsyncCallback<[RotationMatrixResponse](js-apis-sensor.md#rotationmatrixresponse)> | 是 | 异步返回旋转矩阵。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. sensor.createRotationMatrix([-0.27775216, 0.5351276, 9.788099], [210.87253, -78.6096, -111.44444],
5. (err: BusinessError, data: sensor.RotationMatrixResponse) => {
6. if (err) {
7. console.error(`Failed to get create rotationMatrix. Code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info(JSON.stringify(data));
11. })
```

## sensor.createRotationMatrix(deprecated)

PhonePC/2in1TabletTVWearable

createRotationMatrix(gravity: Array<number>, geomagnetic: Array<number>): Promise<RotationMatrixResponse>

根据重力矢量和地磁矢量计算旋转矩阵，使用Promise异步方式返回结果。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getRotationMatrix](js-apis-sensor.md#sensorgetrotationmatrix9-3)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| gravity | Array<number> | 是 | 表示重力向量。 |
| geomagnetic | Array<number> | 是 | 表示地磁矢量。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[RotationMatrixResponse](js-apis-sensor.md#rotationmatrixresponse)> | 使用异步方式返回旋转矩阵。 |

**示例**：

```
1. import { sensor } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const promise = sensor.createRotationMatrix([-0.27775216, 0.5351276, 9.788099], [210.87253, -78.6096, -111.44444]);
5. promise.then((data: sensor.RotationMatrixResponse) => {
6. console.info(JSON.stringify(data));
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to get promise.`);
9. })
```

## SensorType(deprecated)

PhonePC/2in1TabletTVWearable

表示要订阅或取消订阅的传感器类型。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[SensorId](js-apis-sensor.md#sensorid9)代替。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SENSOR\_TYPE\_ID\_ACCELEROMETER | 1 | 加速度传感器。 |
| SENSOR\_TYPE\_ID\_GYROSCOPE | 2 | 陀螺仪传感器。 |
| SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT | 5 | 环境光传感器。 |
| SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD | 6 | 磁场传感器。 |
| SENSOR\_TYPE\_ID\_BAROMETER | 8 | 气压计传感器。 |
| SENSOR\_TYPE\_ID\_HALL | 10 | 霍尔传感器。 |
| SENSOR\_TYPE\_ID\_PROXIMITY | 12 | 接近光传感器。 |
| SENSOR\_TYPE\_ID\_HUMIDITY | 13 | 湿度传感器。 |
| SENSOR\_TYPE\_ID\_ORIENTATION | 256 | 方向传感器。 |
| SENSOR\_TYPE\_ID\_GRAVITY | 257 | 重力传感器。 |
| SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION | 258 | 线性加速度传感器。 |
| SENSOR\_TYPE\_ID\_ROTATION\_VECTOR | 259 | 旋转矢量传感器。 |
| SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE | 260 | 环境温度传感器。 |
| SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED | 261 | 未校准磁场传感器。 |
| SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED | 263 | 未校准陀螺仪传感器。 |
| SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION | 264 | 有效运动传感器。 |
| SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION | 265 | 计步检测传感器。 |
| SENSOR\_TYPE\_ID\_PEDOMETER | 266 | 计步传感器。 |
| SENSOR\_TYPE\_ID\_HEART\_RATE | 278 | 心率传感器。 |
| SENSOR\_TYPE\_ID\_WEAR\_DETECTION | 280 | 佩戴检测传感器。 |
| SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED | 281 | 未校准加速度计传感器。 |
