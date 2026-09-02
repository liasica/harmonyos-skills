---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pen-stylus-interaction
title: 接入手写交互
breadcrumb: 指南 > 系统 > 硬件 > Pen Kit（手写笔服务） > 手写功能开发 > 接入手写交互
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:37+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:e1070c50926535cab80e0193df8c77a4caeb410dc89f9682fccf86ebdbb0aef5
---

为实现手写笔的双击、轻捏及传感器数据交互，开发者应用可集成对应接口以订阅相关事件，并通过回调机制触发应用内部指定操作。

## 接口说明

| 类名 | 接口名 | 说明 |
| --- | --- | --- |
| stylusInteraction | [on](../harmonyos-references/pen-stylusinteraction.md#stylusinteractiononsqueeze)(type: 'squeeze', receiver: Callback<[SqueezeEvent](../harmonyos-references/pen-stylusinteraction.md#squeezeevent)>): void | 订阅手写笔轻捏事件。 |
| stylusInteraction | [off](../harmonyos-references/pen-stylusinteraction.md#stylusinteractionoffsqueeze)(type: 'squeeze', receiver?: Callback<[SqueezeEvent](../harmonyos-references/pen-stylusinteraction.md#squeezeevent)>): void | 取消订阅手写笔轻捏事件。 |
| stylusInteraction | [on](../harmonyos-references/pen-stylusinteraction.md#stylusinteractionondoubletap)(type: 'doubleTap', receiver: Callback<[DoubleTapEvent](../harmonyos-references/pen-stylusinteraction.md#doubletapevent)>): void | 订阅手写笔双击事件。 |
| stylusInteraction | [off](../harmonyos-references/pen-stylusinteraction.md#stylusinteractionoffdoubletap)(type: 'doubleTap', receiver?: Callback<[DoubleTapEvent](../harmonyos-references/pen-stylusinteraction.md#doubletapevent)>): void | 取消订阅手写笔双击事件。 |
| stylusInteraction | [isSensorSupported](../harmonyos-references/pen-stylusinteraction.md#stylusinteractionissensorsupported)(): boolean | 查询设备是否支持手写笔传感器数据功能。 |
| stylusInteraction | [onAccelerometer](../harmonyos-references/pen-stylusinteraction.md#stylusinteractiononaccelerometer)(receiver: Callback<[AccelerometerEvent](../harmonyos-references/pen-stylusinteraction.md#accelerometerevent)>): void | 订阅手写笔加速度传感器数据。 |
| stylusInteraction | [offAccelerometer](../harmonyos-references/pen-stylusinteraction.md#stylusinteractionoffaccelerometer)(receiver?: Callback<[AccelerometerEvent](../harmonyos-references/pen-stylusinteraction.md#accelerometerevent)>): void | 取消订阅手写笔加速度传感器数据。 |
| stylusInteraction | [onGyroscope](../harmonyos-references/pen-stylusinteraction.md#stylusinteractionongyroscope)(receiver: Callback<[GyroscopeEvent](../harmonyos-references/pen-stylusinteraction.md#gyroscopeevent)>): void | 订阅手写笔陀螺仪传感器数据。 |
| stylusInteraction | [offGyroscope](../harmonyos-references/pen-stylusinteraction.md#stylusinteractionoffgyroscope)(receiver?: Callback<[GyroscopeEvent](../harmonyos-references/pen-stylusinteraction.md#gyroscopeevent)>): void | 取消订阅手写笔陀螺仪传感器数据。 |
| stylusInteraction | [onSensor](../harmonyos-references/pen-stylusinteraction.md#stylusinteractiononsensor)(receiver: Callback<[SensorEvent](../harmonyos-references/pen-stylusinteraction.md#sensorevent)>): void | 订阅手写笔加速度和陀螺仪传感器数据。 |
| stylusInteraction | [offSensor](../harmonyos-references/pen-stylusinteraction.md#stylusinteractionoffsensor)(receiver?: Callback<[SensorEvent](../harmonyos-references/pen-stylusinteraction.md#sensorevent)>): void | 取消订阅手写笔加速度和陀螺仪传感器数据。 |

## 开发步骤

### 手写笔轻捏事件

1. 导入相关模块。

   ```typescript
   import { stylusInteraction } from '@kit.Penkit';
   ```
2. 订阅手写笔轻捏事件。

   ```typescript
   try {
     stylusInteraction.on('squeeze', (event: stylusInteraction.SqueezeEvent) => {
       console.info(`got squeeze event, time: ${event.timestamp}`);
     });
   } catch (error) {
     console.error(`${error.code}: ${error.message}`);
   }
   ```
3. 取消订阅手写笔轻捏事件。

   ```typescript
   try {
     stylusInteraction.off('squeeze', (event: stylusInteraction.SqueezeEvent) => {
       console.info(`off squeeze event, time: ${event.timestamp}`);
     });
   } catch (error) {
     console.error(`${error.code}: ${error.message}`);
   }
   ```

### 手写笔双击事件

1. 导入相关模块。

   ```typescript
   import { stylusInteraction } from '@kit.Penkit';
   ```
2. 订阅手写笔双击事件。

   ```typescript
   try {
     stylusInteraction.on('doubleTap', (event: stylusInteraction.DoubleTapEvent) => {
       console.info(`got doubleTap event, time: ${event.timestamp}`);
     });
   } catch (error) {
     console.error(`${error.code}: ${error.message}`);
   }
   ```
3. 取消订阅手写笔双击事件。

   ```typescript
   try {
     stylusInteraction.off('doubleTap', (event: stylusInteraction.DoubleTapEvent) => {
       console.info(`off doubleTap event, time: ${event.timestamp}`);
     });
   } catch (error) {
     console.error(`${error.code}: ${error.message}`);
   }
   ```

### 手写笔传感器功能

1. 导入相关模块。

   ```typescript
   import { stylusInteraction } from '@kit.Penkit';
   ```
2. 查询设备是否支持手写笔传感器数据功能。

   ```typescript
    try {
      let supported: boolean = stylusInteraction.isSensorSupported();
      console.info(`stylus sensor is supported: ${supported}`);
    } catch (error) {
      console.error(`${error.code}: ${error.message}`);
    }
   ```
3. 订阅手写笔加速度传感器数据。

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
4. 取消订阅手写笔加速度传感器数据。

   ```typescript
   try {
     stylusInteraction.offAccelerometer((event: stylusInteraction.AccelerometerEvent) => {
       console.info(`off accelerometer event, time: ${event.timestamp}`);
     });
   } catch (error) {
     console.error(`${error.code}: ${error.message}`);
   }
   ```
5. 订阅手写笔陀螺仪传感器数据。

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
6. 取消订阅手写笔陀螺仪传感器数据。

   ```typescript
   try {
     stylusInteraction.offGyroscope((event: stylusInteraction.GyroscopeEvent) => {
       console.info(`off gyroscope event, time: ${event.timestamp}`);
     });
   } catch (error) {
     console.error(`${error.code}: ${error.message}`);
   }
   ```
7. 订阅手写笔加速度和陀螺仪传感器数据。

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
8. 取消订阅手写笔加速度和陀螺仪传感器数据。

   ```typescript
   try {
     stylusInteraction.offSensor((event: stylusInteraction.SensorEvent) => {
       console.info(`off sensor event, time: ${event.timestamp}`);
     });
   } catch (error) {
     console.error(`${error.code}: ${error.message}`);
   }
   ```
