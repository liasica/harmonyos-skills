---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-stylusinteraction
title: stylusInteraction (手写笔交互功能)
breadcrumb: API参考 > 系统 > 硬件 > Pen Kit（手写笔服务） > ArkTS API > stylusInteraction (手写笔交互功能)
category: harmonyos-references
scraped_at: 2026-09-02T14:52:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:57db3c0865ff4c6dbddbd68087b45f5aac0d931d26736424d8c8d4e641fb347c
---

手写笔交互功能入口类，当前包含手写笔笔身轻捏事件和手写笔笔身双击事件。

**起始版本：** 5.1.1(19)

## 导入模块

```typescript
import { stylusInteraction } from '@kit.Penkit';
```

## stylusInteraction.on('squeeze')

on(type: 'squeeze', receiver: Callback<SqueezeEvent>): void

订阅手写笔笔身轻捏事件，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 5.1.1(19)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"squeeze"字符串，表示手写笔笔身轻捏事件。 |
| receiver | Callback<[SqueezeEvent](pen-stylusinteraction.md#squeezeevent)> | 是 | 回调函数，返回手写笔笔身轻捏事件的详细信息。 |

**示例：**

```typescript
try {
  stylusInteraction.on('squeeze', (event: stylusInteraction.SqueezeEvent) => {
    console.info(`got squeeze event, time: ${event.timestamp}`);
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}
```

## stylusInteraction.off('squeeze')

off(type: 'squeeze', receiver?: Callback<SqueezeEvent>): void

取消订阅手写笔笔身轻捏事件，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 5.1.1(19)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"squeeze"字符串，表示手写笔笔身轻捏事件。 |
| receiver | Callback<[SqueezeEvent](pen-stylusinteraction.md#squeezeevent)> | 否 | 回调函数，需要取消订阅的手写笔轻捏事件对象，需与订阅时传入的回调函数是同一个。若不设置此参数，则取消订阅所有的轻捏事件。 |

**示例：**

```typescript
try {
  stylusInteraction.off('squeeze', (event: stylusInteraction.SqueezeEvent) => {
    console.info(`off squeeze event, time: ${event.timestamp}`);
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}
```

## stylusInteraction.on('doubleTap')

on(type: 'doubleTap', receiver: Callback<DoubleTapEvent>): void

订阅手写笔笔身双击事件，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 5.1.1(19)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"doubleTap"字符串，表示手写笔笔身双击事件。 |
| receiver | Callback<[DoubleTapEvent](pen-stylusinteraction.md#doubletapevent)> | 是 | 回调函数，返回手写笔笔身双击事件的详细信息。 |

**示例：**

```typescript
try {
  stylusInteraction.on('doubleTap', (event: stylusInteraction.DoubleTapEvent) => {
    console.info(`got doubleTap event, time: ${event.timestamp}`);
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}
```

## stylusInteraction.off('doubleTap')

off(type: 'doubleTap', receiver?: Callback<DoubleTapEvent>): void

取消订阅手写笔笔身双击事件，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 5.1.1(19)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"doubleTap"字符串，表示手写笔笔身双击事件。 |
| receiver | Callback<[DoubleTapEvent](pen-stylusinteraction.md#doubletapevent)> | 否 | 回调函数，需要取消订阅的手写笔双击事件对象，需与订阅时传入的回调函数是同一个。若不设置此参数，则取消订阅所有的双击事件。 |

**示例：**

```typescript
try {
  stylusInteraction.off('doubleTap', (event: stylusInteraction.DoubleTapEvent) => {
    console.info(`off doubleTap event, time: ${event.timestamp}`);
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}
```

## SqueezeEvent

手写笔笔身轻捏事件信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 5.1.1(19)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timestamp | number | 否 | 否 | 时间戳，自系统启动以来经过的时间，单位：ms。 |

## DoubleTapEvent

手写笔笔身双击事件信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 5.1.1(19)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timestamp | number | 否 | 否 | 时间戳，自系统启动以来经过的时间，单位：ms。 |

## stylusInteraction.isSensorSupported

isSensorSupported(): boolean

查询当前设备是否支持手写笔传感器数据功能。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回查询结果。  - true：支持手写笔传感器数据功能。  - false：不支持手写笔传感器数据功能。 |

**示例：**

```typescript
try {
  let supported: boolean = stylusInteraction.isSensorSupported();
  console.info(`stylus sensor is supported: ${supported}`);
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}
```

## stylusInteraction.onAccelerometer

onAccelerometer(receiver: Callback<AccelerometerEvent>): void

订阅手写笔加速度传感器数据，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| receiver | Callback<[AccelerometerEvent](pen-stylusinteraction.md#accelerometerevent)> | 是 | 回调函数，返回手写笔加速度传感器数据。 |

**示例：**

```typescript
try {
  stylusInteraction.onAccelerometer((event: stylusInteraction.AccelerometerEvent) => {
    console.info(`got accelerometer event, time: ${event.timestamp}`);
    for (let i = 0; i < event.accelerometerData.length; i++) {
      console.info(`accelerometer data: x=${event.accelerometerData[i].x}, y=${event.accelerometerData[i].y}
      , z=${event.accelerometerData[i].z}`);
    }
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}
```

## stylusInteraction.offAccelerometer

offAccelerometer(receiver?: Callback<AccelerometerEvent>): void

取消订阅手写笔加速度传感器数据，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| receiver | Callback<[AccelerometerEvent](pen-stylusinteraction.md#accelerometerevent)> | 否 | 回调函数，需要取消订阅的加速度数据回调对象，需与订阅时传入的回调函数是同一个。若不设置此参数，则取消订阅所有的加速度数据回调。 |

**示例：**

```typescript
try {
  stylusInteraction.offAccelerometer((event: stylusInteraction.AccelerometerEvent) => {
    console.info(`off accelerometer event, time: ${event.timestamp}`);
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}
```

## AccelerometerData

手写笔加速度传感器数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 加速度x轴分量，单位：m/s²，4096为1个重力加速度g，取值范围[-32768, 32767]。 |
| y | number | 否 | 否 | 加速度y轴分量，单位：m/s²，4096为1个重力加速度g，取值范围[-32768, 32767]。 |
| z | number | 否 | 否 | 加速度z轴分量，单位：m/s²，4096为1个重力加速度g，取值范围[-32768, 32767]。 |

## AccelerometerEvent

手写笔加速度传感器事件数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| accelerometerData | [AccelerometerData](pen-stylusinteraction.md#accelerometerdata)[] | 否 | 否 | 手写笔加速度数组数据。 |
| timestamp | number | 否 | 否 | 加速度数据的时间戳，自系统启动以来经过的时间，单位：ms。 |

## stylusInteraction.onGyroscope

onGyroscope(receiver: Callback<GyroscopeEvent>): void

订阅手写笔陀螺仪传感器数据，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| receiver | Callback<[GyroscopeEvent](pen-stylusinteraction.md#gyroscopeevent)> | 是 | 回调函数，返回手写笔陀螺仪传感器数据。 |

**示例：**

```typescript
try {
  stylusInteraction.onGyroscope((event: stylusInteraction.GyroscopeEvent) => {
    console.info(`got gyroscope event, time: ${event.timestamp}`);
    for (let i = 0; i < event.gyroscopeData.length; i++) {
      console.info(`gyroscope data: x=${event.gyroscopeData[i].x}, y=${event.gyroscopeData[i].y}
  , z=${event.gyroscopeData[i].z}`);
    }
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}
```

## stylusInteraction.offGyroscope

offGyroscope(receiver?: Callback<GyroscopeEvent>): void

取消订阅手写笔陀螺仪传感器数据，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| receiver | Callback<[GyroscopeEvent](pen-stylusinteraction.md#gyroscopeevent)> | 否 | 回调函数，需要取消订阅的陀螺仪数据回调对象，需与订阅时传入的回调函数是同一个。若不设置此参数，则取消订阅所有的陀螺仪数据回调。 |

**示例：**

```typescript
try {
  stylusInteraction.offGyroscope((event: stylusInteraction.GyroscopeEvent) => {
    console.info(`off gyroscope event, time: ${event.timestamp}`);
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}
```

## GyroscopeData

手写笔陀螺仪传感器数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 陀螺仪x轴分量，单位：61mdps/LSB，取值范围[-32768, 32767]。 |
| y | number | 否 | 否 | 陀螺仪y轴分量，单位：61mdps/LSB，取值范围[-32768, 32767]。 |
| z | number | 否 | 否 | 陀螺仪z轴分量，单位：61mdps/LSB，取值范围[-32768, 32767]。 |

## GyroscopeEvent

手写笔陀螺仪传感器事件数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| gyroscopeData | [GyroscopeData](pen-stylusinteraction.md#gyroscopedata)[] | 否 | 否 | 手写笔陀螺仪数组数据。 |
| timestamp | number | 否 | 否 | 陀螺仪数据的时间戳，自系统启动以来经过的时间，单位：ms。 |

## stylusInteraction.onSensor

onSensor(receiver: Callback<SensorEvent>): void

订阅手写笔加速度和陀螺仪传感器数据，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| receiver | Callback<[SensorEvent](pen-stylusinteraction.md#sensorevent)> | 是 | 回调函数，返回手写笔加速度和陀螺仪传感器数据。 |

**示例：**

```typescript
try {
  stylusInteraction.onSensor((event: stylusInteraction.SensorEvent) => {
    console.info(`got sensor event, time: ${event.timestamp}`);
    for (let i = 0; i < event.sensorData.length; i++) {
      let accel = event.sensorData[i].accelerometerData;
      let gyro = event.sensorData[i].gyroscopeData;
      console.info(`sensor data: accel.x=${accel.x}, accel.y=${accel.y}, accel.z=${accel.z}, gyro.x=${gyro.x},
      gyro.y=${gyro.y}, gyro.z=${gyro.z}`);
    }
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}
```

## stylusInteraction.offSensor

offSensor(receiver?: Callback<SensorEvent>): void

取消订阅手写笔加速度和陀螺仪传感器数据，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| receiver | Callback<[SensorEvent](pen-stylusinteraction.md#sensorevent)> | 否 | 回调函数，需要取消订阅的传感器数据回调对象，需与订阅时传入的回调函数是同一个。若不设置此参数，则取消订阅所有的传感器数据回调。 |

**示例：**

```typescript
try {
  stylusInteraction.offSensor((event: stylusInteraction.SensorEvent) => {
    console.info(`off sensor event, time: ${event.timestamp}`);
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}
```

## SensorData

手写笔加速度和陀螺仪传感器数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| accelerometerData | [AccelerometerData](pen-stylusinteraction.md#accelerometerdata) | 否 | 否 | 加速度传感器数据。 |
| gyroscopeData | [GyroscopeData](pen-stylusinteraction.md#gyroscopedata) | 否 | 否 | 陀螺仪传感器数据。 |

## SensorEvent

手写笔加速度和陀螺仪传感器事件数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sensorData | [SensorData](pen-stylusinteraction.md#sensordata)[] | 否 | 否 | 手写笔加速度和陀螺仪数组数据。 |
| timestamp | number | 否 | 否 | 传感器数据的时间戳，自系统启动以来经过的时间，单位：ms。 |
