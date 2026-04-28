---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthservice
title: healthService(运动健康联动服务)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > healthService(运动健康联动服务)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9d7874dab628a0535596fc8040b33add4e6f367bdb0788424954e85ac4bfcc7b
---

本模块提供运动健康联动服务。

**起始版本：** 5.0.0(12)

## 导入模块

PhoneTabletWearable

```
1. import { healthService } from '@kit.HealthServiceKit';
```

## SampleEvent

PhoneTabletWearable

联动控制事件。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| eventId | number | 否 | 否 | 事件ID。 |
| eventLevel | number | 否 | 否 | 事件等级。  取值参考：[0, 255] |
| eventData | string | 否 | 否 | 事件携带的信息。 |
| srcPkgName | string | 否 | 是 | 事件发送源包名，若未填写，默认为空。 |
| destPkgName | string | 否 | 是 | 事件发送目标包名，若未填写，默认为空。 |

## SampleReal

PhoneTabletWearable

SampleReal<K extends Record<string, [healthStore.HealthValueType](health-api-healthstore.md#healthvaluetype)> = Record<string, [healthStore.HealthValueType](health-api-healthstore.md#healthvaluetype)>>

联动实时运动数据。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| dataType | [healthStore.DataType](health-api-healthstore.md#datatype) | 否 | 否 | 实时融合数据类型。 |
| time | number | 否 | 否 | 实时融合数据产生时间，Unix时间戳，以毫秒为单位。 |
| fields | Pick<K, keyof K> | 否 | 否 | 实时融合数据字段。 |
| deviceUniqueId | string | 否 | 是 | 实时融合数据来源，若未填写，默认为空。 |

## workout

PhoneTabletWearable

提供运动健康实时数据。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.0.0(12)

### ActivityReport

PhoneTabletWearable

实时三环数据。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| steps | number | 否 | 否 | 步数。 |
| stepsGoal | number | 否 | 是 | 步数目标（若未设置过，无法读取到运动健康App中展示的默认目标）。 |
| activeCalories | number | 否 | 否 | 活动热量。  单位：卡 |
| activeCaloriesGoal | number | 否 | 是 | 活动热量目标。  单位：卡 |
| exercise | number | 否 | 否 | 锻炼时长。  单位：分钟 |
| exerciseGoal | number | 否 | 是 | 锻炼时长目标。  单位：分钟 |
| activeHours | number | 否 | 否 | 活动小时数。 |
| activeHoursGoal | number | 否 | 是 | 活动小时数目标。 |

### ConfigType

PhoneTabletWearable

type ConfigType = number | string | boolean

联动配置项类型。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

| 类型 | **说明** |
| --- | --- |
| number | 表示值类型为数字，可取任意值。 |
| string | 表示值类型为字符串，可取任意值。 |
| boolean | 表示值类型为布尔类型，可取true或false，具体含义以实际使用场景为准。 |

### DeviceState

PhoneTabletWearable

联动设备状态。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 设备ID。 |
| state | number | 否 | 否 | 设备状态。 |
| deviceName | string | 否 | 是 | 设备名称，若未填写，默认为空。 |

### Goal

PhoneTabletWearable

联动运动目标。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| type | number | 否 | 否 | 目标类型，取值参考：[TargetType](health-api-healthservice.md#targettype)。 |
| value | number | 否 | 否 | 目标值。 |

### LinkageType

PhoneTabletWearable

联动类型。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COURSE\_LINK | 0 | 课程联动。 |
| ACTIVITY\_LINK | 1 | 运动联动。 |

### StartCode

PhoneTabletWearable

联动开启结果码。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 联动开启成功。 |
| WORKOUT\_WORKING | 1 | 联动已开始。 |
| NO\_SUPPORTED\_DEVICE | 2 | 无可支持联动的设备。 |
| DEVICE\_BUSY | 3 | 联动设备忙碌。 |

### StartResult

PhoneTabletWearable

联动开启结果。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| startCode | [StartCode](health-api-healthservice.md#startcode) | 否 | 否 | 联动开启结果码。 |
| deviceState | [DeviceState](health-api-healthservice.md#devicestate)[] | 否 | 否 | 联动设备状态。 |

### TargetType

PhoneTabletWearable

联动目标类型。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 无目标。 |
| DISTANCE | 1 | 距离。 |
| CALORIE | 2 | 卡路里。 |
| TIME | 3 | 时长。 |
| SKIPPING\_TIMES | 4 | 跳绳次数。 |

### WorkoutConfig

PhoneTabletWearable

联动配置项。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| linkageType | [LinkageType](health-api-healthservice.md#linkagetype) | 否 | 否 | 联动类型。 |
| sportType | number | 否 | 否 | 运动类型，参见[锻炼记录类型常量](health-api-exercisedequencehelper.md)子数据类型id。 |
| activityGoals | [Goal](health-api-healthservice.md#goal)[] | 否 | 是 | 联动运动目标，若未填写，默认为空。 |
| extensionConfig | Record<string, [ConfigType](health-api-healthservice.md#configtype)> | 否 | 是 | 扩展配置项，若未填写，默认为空。 |

### workout.config

PhoneTabletWearable

config(workoutConfig: WorkoutConfig): Promise<void>

配置联动，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| workoutConfig | [WorkoutConfig](health-api-healthservice.md#workoutconfig) | 是 | 联动配置项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |
| [1009104003](errorcode-healthservice.md#section1009104003-非法指令) | Illegal command. Called when workout not in stoped or idle state. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthService, healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let workoutOptions: healthService.workout.WorkoutConfig = {
6. linkageType: healthService.workout.LinkageType.COURSE_LINK,
7. sportType: healthStore.exerciseSequenceHelper.running.EXERCISE_TYPE.id
8. };
9. await healthService.workout.config(workoutOptions);
10. hilog.info(0x0000, 'testTag', 'Succeed in configuring workout');
11. } catch (err) {
12. hilog.error(0x0000, 'testTag', `Failed to configure workout. Code: ${err.code}, message: ${err.message}`);
13. }
```

### workout.start

PhoneTabletWearable

start(): Promise<StartResult>

开启联动，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[StartResult](health-api-healthservice.md#startresult)> | Promise对象，返回联动开启结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [1009104001](errorcode-healthservice.md#section1009104001-联动已开启) | Sport service busy. Workout is already started by other application. |
| [1009104002](errorcode-healthservice.md#section1009104002-不支持运动类型) | Unsupported sport type. |
| [1009104003](errorcode-healthservice.md#section1009104003-非法指令) | Illegal command. Called when workout in sporting, paused or stoped state. |
| [1009104004](errorcode-healthservice.md#section1009104004-权限校验异常) | Permission verification error. Application has no permission, such as Motion Permission. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthService } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. await healthService.workout.start();
6. hilog.info(0x0000, 'testTag', 'Succeed in starting workout');
7. } catch (err) {
8. hilog.error(0x0000, 'testTag', `Failed to start workout. Code: ${err.code}, message: ${err.message}`);
9. }
```

### workout.pause

PhoneTabletWearable

pause(): Promise<void>

暂停联动，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [1009104003](errorcode-healthservice.md#section1009104003-非法指令) | Illegal command. Called when workout in ready, paused or stoped state. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthService } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. await healthService.workout.pause();
6. hilog.info(0x0000, 'testTag', 'Succeed in pausing workout');
7. } catch (err) {
8. hilog.error(0x0000, 'testTag', `Failed to pause workout. Code: ${err.code}, message: ${err.message}`);
9. }
```

### workout.resume

PhoneTabletWearable

resume(): Promise<void>

恢复联动，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [1009104003](errorcode-healthservice.md#section1009104003-非法指令) | Illegal command. Called when workout in ready, sporting or stoped state. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthService } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. await healthService.workout.resume();
6. hilog.info(0x0000, 'testTag', 'Succeed in resuming workout');
7. } catch (err) {
8. hilog.error(0x0000, 'testTag', `Failed to resume workout. Code: ${err.code}, message: ${err.message}`);
9. }
```

### workout.stop

PhoneTabletWearable

stop(): Promise<void>

停止联动，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [1009104003](errorcode-healthservice.md#section1009104003-非法指令) | Illegal command. Called when workout is not started. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthService } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. await healthService.workout.stop();
6. hilog.info(0x0000, 'testTag', 'Succeed in stopping workout');
7. } catch (err) {
8. hilog.error(0x0000, 'testTag', `Failed to stop workout. Code: ${err.code}, message: ${err.message}`);
9. }
```

### workout.onData

PhoneTabletWearable

onData(dataType: healthStore.DataType, listener: Callback<SampleReal[]>): Promise<void>

注册指定联动运动数据监听，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| dataType | [healthStore.DataType](health-api-healthstore.md#datatype) | 是 | 联动运动数据类型。 |
| listener | Callback<[SampleReal](health-api-healthservice.md#samplereal)[]> | 是 | 联动运动数据监听回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthService, healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. const callback: Callback<healthService.SampleReal[]> = (sampleReals) => {
6. hilog.info(0x0000, 'testTag', `Workout onData receive data. The sampleReals size is ${sampleReals.length}`);
7. };
8. const realTimeMotionDataType: healthStore.DataType = {
9. id: 50004
10. };
11. await healthService.workout.onData(realTimeMotionDataType, callback);
12. } catch (err) {
13. hilog.error(0x0000, 'testTag', `Failed to onData. Code: ${err.code}, message: ${err.message}`);
14. }
```

### workout.onData

PhoneTabletWearable

onData(dataType: undefined, listener: Callback<SampleReal[]>): Promise<void>

注册所有联动运动数据监听，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| dataType | undefined | 是 | 监听所有联动运动数据类型。 |
| listener | Callback<[SampleReal](health-api-healthservice.md#samplereal)[]> | 是 | 联动运动数据监听回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthService } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. const callback: Callback<healthService.SampleReal[]> = (sampleReals) => {
6. hilog.info(0x0000, 'testTag', `Workout onData receive data. The sampleReals size is ${sampleReals.length}`);
7. };
8. await healthService.workout.onData(undefined, callback);
9. } catch (err) {
10. hilog.error(0x0000, 'testTag', `Failed to onData. Code: ${err.code}, message: ${err.message}`);
11. }
```

### workout.offData

PhoneTabletWearable

offData(dataType: healthStore.DataType, listener: Callback<SampleReal[]>): Promise<void>

取消指定联动运动数据的监听，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| dataType | [healthStore.DataType](health-api-healthstore.md#datatype) | 是 | 联动运动数据类型。 |
| listener | Callback<[SampleReal](health-api-healthservice.md#samplereal)[]> | 是 | 联动运动数据监听回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthService, healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. const callback: Callback<healthService.SampleReal[]> = (sampleReals) => {
6. hilog.info(0x0000, 'testTag', `Workout offData receive data. The sampleReals size is ${sampleReals.length}`);
7. };
8. await healthService.workout.offData(healthStore.healthDataTypes.WORKOUT, callback);
9. } catch (err) {
10. hilog.error(0x0000, 'testTag', `Failed to offData. Code: ${err.code}, message: ${err.message}`);
11. }
```

### workout.offData

PhoneTabletWearable

offData(dataType: undefined, listener: Callback<SampleReal[]>): Promise<void>

取消所有联动运动数据的监听，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| dataType | undefined | 是 | 监听所有联动运动数据类型。 |
| listener | Callback<[SampleReal](health-api-healthservice.md#samplereal)[]> | 是 | 联动运动数据监听回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Parameter verification failed. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthService } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. const callback: Callback<healthService.SampleReal[]> = (sampleReals) => {
6. hilog.info(0x0000, 'testTag', `Workout offData receive data. The sampleReals size is ${sampleReals.length}`);
7. };
8. await healthService.workout.offData(undefined, callback);
9. } catch (err) {
10. hilog.error(0x0000, 'testTag', `Failed to offData. Code: ${err.code}, message: ${err.message}`);
11. }
```

### workout.onEvent("\*")

PhoneTabletWearable

onEvent(event: "\*", listener: Callback<SampleEvent>): Promise<void>

注册联动设备事件监听，使用Promise异步方式。

**系统能力：** SystemCapability.Health.HealthService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回401错误码。

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| event | string | 是 | 联动设备事件类型，支持的事件为："\*"，当联动设备运动状态改变时，触发该事件。 |
| listener | Callback<[SampleEvent](health-api-healthservice.md#sampleevent)> | 是 | 联动设备事件监听回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthService } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. const callback: Callback<healthService.SampleEvent> = (event) => {
6. hilog.info(0x0000, 'testTag', `Workout onEvent receive event. Event data: ${event.eventData}, event id: ${event.eventId}`);
7. };
8. await healthService.workout.onEvent('*', callback);
9. } catch (err) {
10. hilog.error(0x0000, 'testTag', `Failed to onEvent. Code: ${err.code}, message: ${err.message}`);
11. }
```

### workout.offEvent("\*")

PhoneTabletWearable

offEvent(event: "\*", listener: Callback<SampleEvent>): Promise<void>

取消联动设备事件的监听，使用Promise异步方式。

**系统能力：** SystemCapability.Health.HealthService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回401错误码。

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| event | string | 是 | 联动设备事件类型，支持的事件为："\*"，当联动设备运动状态改变时，触发该事件。 |
| listener | Callback<[SampleEvent](health-api-healthservice.md#sampleevent)> | 是 | 联动设备事件监听回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Parameter verification failed. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthService } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. const callback: Callback<healthService.SampleEvent> = (event) => {
6. hilog.info(0x0000, 'testTag', `Workout offEvent receive event. Event data: ${event.eventData}, event id: ${event.eventId}`);
7. };
8. await healthService.workout.offEvent('*', callback);
9. } catch (err) {
10. hilog.error(0x0000, 'testTag', `Failed to offEvent. Code: ${err.code}, message: ${err.message}`);
11. }
```

### workout.readActivityReport

PhoneTabletWearable

readActivityReport(): Promise<ActivityReport>

读取实时三环数据，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ActivityReport](health-api-healthservice.md#activityreport)> | Promise对象，返回实时三环数据。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission denied. |
| [14500101](errorcode-healthservice.md#section14500101-服务异常) | Service exception. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthService } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. const result: healthService.workout.ActivityReport = await healthService.workout.readActivityReport();

7. hilog.info(0x0000, 'testTag', 'Succeeded in reading ActivityReport');
8. Object.keys(result).forEach(key => {
9. hilog.info(0x0000, 'testTag', `the ${key} is ${result[key]}`);
10. });
11. } catch(err) {
12. hilog.error(0x0000, 'testTag', `Failed to read ActivityReport. Code: ${err.code}, message: ${err.message}`);
13. }
```

### workout.sendData

PhoneTabletWearable

sendData(sampleReal: SampleReal[]): Promise<void>

下发融合运动数据到联动设备，使用Promise异步方式。

**系统能力：** SystemCapability.Health.HealthService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回401错误码。

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| sampleReal | [SampleReal](health-api-healthservice.md#samplereal)[] | 是 | 融合运动数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthService } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. const sampleReal: healthService.SampleReal = {
6. dataType: { id: 50004 },
7. time: 1695740400000, // 2023-09-26 23:00:00,
8. fields: {
9. hr: 90
10. }
11. };
12. await healthService.workout.sendData([sampleReal]);
13. hilog.info(0x0000, 'testTag', 'Succeed in sending data.');
14. } catch (err) {
15. hilog.error(0x0000, 'testTag', `Failed to send data. Code: ${err.code}, message: ${err.message}`);
16. }
```

### workout.sendEvent

PhoneTabletWearable

sendEvent(event: SampleEvent): Promise<void>

下发控制事件到联动设备，使用Promise异步方式。

**系统能力：** SystemCapability.Health.HealthService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回401错误码。

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| event | [SampleEvent](health-api-healthservice.md#sampleevent) | 是 | 联动控制事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthService } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. const sampleEvent: healthService.SampleEvent = {
6. eventId: 800400002,
7. eventLevel: 0,
8. eventData: 'start'
9. };
10. await healthService.workout.sendEvent(sampleEvent);
11. hilog.info(0x0000, 'testTag', 'Succeed in sending event.');
12. } catch (err) {
13. hilog.error(0x0000, 'testTag', `Failed to send event. Code: ${err.code}, message: ${err.message}`);
14. }
```
