---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthservice
title: healthService (运动健康联动服务)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > healthService (运动健康联动服务)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:55+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:726dc72d75d3b77c65461791c4d3601d6c9e4542fd4c6389518560d4f7278ff7
---

本模块提供运动健康联动服务。

**说明** 

针对系统能力SystemCapability.Health.HealthService，请先使用[canIUse()](js-apis-syscap.md#caniuse)接口判断当前设备是否支持此syscap及对应接口。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { healthService } from '@kit.HealthServiceKit';
```

## SampleEvent

联动控制事件。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| eventId | number | 否 | 否 | 事件ID。 |
| eventLevel | number | 否 | 否 | 事件等级。  取值参考：[0, 255] |
| eventData | string | 否 | 否 | 事件携带的信息。 |
| srcPkgName | string | 否 | 是 | 事件发送源包名，若未填写，默认为空。 |
| destPkgName | string | 否 | 是 | 事件发送目标包名，若未填写，默认为空。 |

## SampleReal

SampleReal<K extends Record<string, [healthStore.HealthValueType](health-api-healthstore.md#healthvaluetype)> = Record<string, [healthStore.HealthValueType](health-api-healthstore.md#healthvaluetype)>>

联动实时运动数据。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| dataType | [healthStore.DataType](health-api-healthstore.md#datatype) | 否 | 否 | 实时融合数据类型。 |
| time | number | 否 | 否 | 实时融合数据产生时间，Unix时间戳，单位：ms。 |
| fields | Pick<K, keyof K> | 否 | 否 | 实时融合数据字段。 |
| deviceUniqueId | string | 否 | 是 | 实时融合数据来源，若未填写，默认为空。 |

## workout

提供运动健康实时数据。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

### ActivityReport

实时三环数据。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| steps | number | 否 | 否 | 步数。 |
| stepsGoal | number | 否 | 是 | 步数目标（若未设置过，无法读取到运动健康App中展示的默认目标）。 |
| activeCalories | number | 否 | 否 | 活动热量。  单位：cal |
| activeCaloriesGoal | number | 否 | 是 | 活动热量目标，默认值为运动健康App中展示的默认目标。  单位：cal |
| exercise | number | 否 | 否 | 锻炼时长。  单位：min |
| exerciseGoal | number | 否 | 是 | 锻炼时长目标，默认值为运动健康App中展示的默认目标。  单位：min |
| activeHours | number | 否 | 否 | 活动小时数（某个小时时段内进行身体活动超过一分钟，该时段被标记为活动小时）。 |
| activeHoursGoal | number | 否 | 是 | 活动小时数目标（某个小时时段内进行身体活动超过一分钟，该时段被标记为活动小时），默认值为运动健康App中展示的默认目标。 |

### ConfigType

type ConfigType = number | string | boolean

联动配置项类型。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| number | 表示值类型为数字，可取任意值。 |
| string | 表示值类型为字符串，可取任意值。 |
| boolean | 表示值类型为布尔类型，可取true或false，具体含义以实际使用场景为准。 |

### DeviceState

联动设备状态。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 设备ID。 |
| state | number | 否 | 否 | 设备状态。 |
| deviceName | string | 否 | 是 | 设备名称，若未填写，默认为空。 |

### Goal

联动运动目标。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| type | number | 否 | 否 | 目标类型，取值参考：[TargetType](health-api-healthservice.md#targettype)。 |
| value | number | 否 | 否 | 目标值。 |

### LinkageType

联动类型。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COURSE\_LINK | 0 | 课程联动。 |
| ACTIVITY\_LINK | 1 | 运动联动。 |

### StartCode

联动开启结果码。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 联动开启成功。 |
| WORKOUT\_WORKING | 1 | 联动已开始。 |
| NO\_SUPPORTED\_DEVICE | 2 | 无可支持联动的设备。 |
| DEVICE\_BUSY | 3 | 联动设备忙碌。 |

### StartResult

联动开启结果。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| startCode | [StartCode](health-api-healthservice.md#startcode) | 否 | 否 | 联动开启结果码。 |
| deviceState | [DeviceState](health-api-healthservice.md#devicestate)[] | 否 | 否 | 联动设备状态。 |

### SportInfo

运动状态信息。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在Stage模型下使用。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| sportType | number | 否 | 否 | 运动类型，参见[锻炼记录类型常量](health-api-exercisesequencehelper.md)子数据类型id。 |
| sportState | [SportState](health-api-healthservice.md#sportstate) | 否 | 否 | 运动状态。 |

### SportState

运动状态类型。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IDLE | 0 | 初始化。 |
| READY | 1 | 就绪。 |
| RUNNING | 2 | 运动中。 |
| PAUSED | 3 | 暂停。 |
| STOPPED | 4 | 停止。 |

### TargetType

联动目标类型。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 无目标。 |
| DISTANCE | 1 | 距离。 |
| CALORIE | 2 | 卡路里。 |
| TIME | 3 | 时长。 |
| SKIPPING\_TIMES | 4 | 跳绳次数。 |

### WorkoutConfig

联动配置项。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| linkageType | [LinkageType](health-api-healthservice.md#linkagetype) | 否 | 否 | 联动类型。 |
| sportType | number | 否 | 否 | 运动类型，参见[锻炼记录类型常量](health-api-exercisesequencehelper.md)子数据类型id。 |
| activityGoals | [Goal](health-api-healthservice.md#goal)[] | 否 | 是 | 联动运动目标，若未填写，默认为空。 |
| extensionConfig | Record<string, [ConfigType](health-api-healthservice.md#configtype)> | 否 | 是 | 扩展配置项，若未填写，默认为空。 |

### workout.config

config(workoutConfig: WorkoutConfig): Promise<void>

配置联动，使用Promise异步回调。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| workoutConfig | [WorkoutConfig](health-api-healthservice.md#workoutconfig) | 是 | 联动配置项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |
| [1009104003](errorcode-healthservice.md#section1009104003-非法指令) | Illegal command. Called when workout not in stopped or idle state. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

**说明** 

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService, healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let workoutOptions: healthService.workout.WorkoutConfig = {
    linkageType: healthService.workout.LinkageType.COURSE_LINK,
    sportType: healthStore.exerciseSequenceHelper.running.EXERCISE_TYPE.id
  };
  await healthService.workout.config(workoutOptions);
  hilog.info(0x0000, 'testTag', 'Succeeded in configuring workout');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to configure workout. Code: ${err.code}, message: ${err.message}`);
}
```

### workout.start

start(): Promise<StartResult>

开启联动，使用Promise异步回调。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[StartResult](health-api-healthservice.md#startresult)> | Promise对象，返回联动开启结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. |
| [1009104001](errorcode-healthservice.md#section1009104001-联动已开启) | Sport service busy. Workout is already started by other application. |
| [1009104002](errorcode-healthservice.md#section1009104002-不支持运动类型) | Unsupported sport type. |
| [1009104003](errorcode-healthservice.md#section1009104003-非法指令) | Illegal command. Called when workout in sporting, paused or stopped state. |
| [1009104004](errorcode-healthservice.md#section1009104004-权限校验异常) | Permission verification error. Application has no permission, such as Motion Permission. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

**说明** 

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  await healthService.workout.start();
  hilog.info(0x0000, 'testTag', 'Succeeded in starting workout');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to start workout. Code: ${err.code}, message: ${err.message}`);
}
```

### workout.pause

pause(): Promise<void>

暂停联动，使用Promise异步回调。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. |
| [1009104003](errorcode-healthservice.md#section1009104003-非法指令) | Illegal command. Called when workout in ready, paused or stopped state. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

**说明** 

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  await healthService.workout.pause();
  hilog.info(0x0000, 'testTag', 'Succeeded in pausing workout');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to pause workout. Code: ${err.code}, message: ${err.message}`);
}
```

### workout.resume

resume(): Promise<void>

恢复联动，使用Promise异步回调。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. |
| [1009104003](errorcode-healthservice.md#section1009104003-非法指令) | Illegal command. Called when workout in ready, sporting or stopped state. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

**说明** 

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  await healthService.workout.resume();
  hilog.info(0x0000, 'testTag', 'Succeeded in resuming workout');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to resume workout. Code: ${err.code}, message: ${err.message}`);
}
```

### workout.stop

stop(): Promise<void>

停止联动，使用Promise异步回调。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. |
| [1009104003](errorcode-healthservice.md#section1009104003-非法指令) | Illegal command. Called when workout is not started. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

**说明** 

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  await healthService.workout.stop();
  hilog.info(0x0000, 'testTag', 'Succeeded in stopping workout');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to stop workout. Code: ${err.code}, message: ${err.message}`);
}
```

### workout.onData

onData(dataType: healthStore.DataType, listener: Callback<SampleReal[]>): Promise<void>

注册指定联动运动数据监听，建议最多订阅三种类型的数据，使用Promise异步回调。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| dataType | [healthStore.DataType](health-api-healthstore.md#datatype) | 是 | 联动运动数据类型。 |
| listener | Callback<[SampleReal](health-api-healthservice.md#samplereal)[]> | 是 | 回调函数，返回联动运动数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types. |

**说明** 

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService, healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const callback: Callback<healthService.SampleReal[]> = (sampleReals) => {
    hilog.info(0x0000, 'testTag', `Succeeded in receiving data. The sampleReals size is ${sampleReals.length}`);
  };
  const realTimeMotionDataType: healthStore.DataType = {
    id: 50004
  };
  await healthService.workout.onData(realTimeMotionDataType, callback);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to onData. Code: ${err.code}, message: ${err.message}`);
}
```

### workout.onData

onData(dataType: undefined, listener: Callback<SampleReal[]>): Promise<void>

注册所有联动运动数据监听，使用Promise异步回调。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| dataType | undefined | 是 | 监听所有联动运动数据类型。 |
| listener | Callback<[SampleReal](health-api-healthservice.md#samplereal)[]> | 是 | 回调函数，返回联动运动数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |

**说明** 

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const callback: Callback<healthService.SampleReal[]> = (sampleReals) => {
    hilog.info(0x0000, 'testTag', `Succeeded in receiving data. The sampleReals size is ${sampleReals.length}`);
  };
  await healthService.workout.onData(undefined, callback);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to onData. Code: ${err.code}, message: ${err.message}`);
}
```

### workout.offData

offData(dataType: healthStore.DataType, listener: Callback<SampleReal[]>): Promise<void>

取消指定联动运动数据的监听，使用Promise异步回调。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| dataType | [healthStore.DataType](health-api-healthstore.md#datatype) | 是 | 联动运动数据类型。 |
| listener | Callback<[SampleReal](health-api-healthservice.md#samplereal)[]> | 是 | 回调函数，返回联动运动数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |

**说明** 

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService, healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const callback: Callback<healthService.SampleReal[]> = (sampleReals) => {
    hilog.info(0x0000, 'testTag', `Succeeded in receiving data. The sampleReals size is ${sampleReals.length}`);
  };
  await healthService.workout.offData(healthStore.healthDataTypes.WORKOUT, callback);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to offData. Code: ${err.code}, message: ${err.message}`);
}
```

### workout.offData

offData(dataType: undefined, listener: Callback<SampleReal[]>): Promise<void>

取消所有联动运动数据的监听，使用Promise异步回调。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| dataType | undefined | 是 | 监听所有联动运动数据类型。 |
| listener | Callback<[SampleReal](health-api-healthservice.md#samplereal)[]> | 是 | 回调函数，返回联动运动数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Parameter verification failed. |

**说明** 

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const callback: Callback<healthService.SampleReal[]> = (sampleReals) => {
    hilog.info(0x0000, 'testTag', `Succeeded in receiving data. The sampleReals size is ${sampleReals.length}`);
  };
  await healthService.workout.offData(undefined, callback);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to offData. Code: ${err.code}, message: ${err.message}`);
}
```

### workout.onEvent("\*")

onEvent(event: "\*", listener: Callback<SampleEvent>): Promise<void>

注册联动设备事件监听，使用Promise异步回调。

**系统能力：** SystemCapability.Health.HealthService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回401错误码。

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| event | string | 是 | 联动设备事件类型，支持的事件为："\*"，当联动设备运动状态改变时，触发该事件。 |
| listener | Callback<[SampleEvent](health-api-healthservice.md#sampleevent)> | 是 | 回调函数，返回联动设备事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |

**说明** 

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const callback: Callback<healthService.SampleEvent> = (event) => {
    hilog.info(0x0000, 'testTag', `Succeeded in receiving event. Event data: ${event.eventData}, event id: ${event.eventId}`);
  };
  await healthService.workout.onEvent('*', callback);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to onEvent. Code: ${err.code}, message: ${err.message}`);
}
```

### workout.offEvent("\*")

offEvent(event: "\*", listener: Callback<SampleEvent>): Promise<void>

取消联动设备事件的监听，使用Promise异步回调。

**系统能力：** SystemCapability.Health.HealthService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回401错误码。

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| event | string | 是 | 联动设备事件类型，支持的事件为："\*"，当联动设备运动状态改变时，触发该事件。 |
| listener | Callback<[SampleEvent](health-api-healthservice.md#sampleevent)> | 是 | 回调函数，返回联动设备事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Parameter verification failed. |

**说明** 

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const callback: Callback<healthService.SampleEvent> = (event) => {
    hilog.info(0x0000, 'testTag', `Succeeded in receiving event. Event data: ${event.eventData}, event id: ${event.eventId}`);
  };
  await healthService.workout.offEvent('*', callback);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to offEvent. Code: ${err.code}, message: ${err.message}`);
}
```

### workout.readActivityReport

readActivityReport(): Promise<ActivityReport>

读取实时三环数据，需要DAILY\_ACTIVITIES数据类型权限，使用Promise异步回调。

该接口从API 19 Release开始，支持Wearable设备开发。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ActivityReport](health-api-healthservice.md#activityreport)> | Promise对象，返回实时三环数据。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission denied. |
| [14500101](errorcode-healthservice.md#section14500101-服务异常) | Service exception. |

**说明** 

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const result: healthService.workout.ActivityReport = await healthService.workout.readActivityReport();
  
  hilog.info(0x0000, 'testTag', 'Succeeded in reading ActivityReport');
  Object.keys(result).forEach(key => {
    hilog.info(0x0000, 'testTag', `the ${key} is ${result[key]}`);
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to read ActivityReport. Code: ${err.code}, message: ${err.message}`);
}
```

### workout.sendData

sendData(sampleReal: SampleReal[]): Promise<void>

下发融合运动数据到联动设备，使用Promise异步回调。

**系统能力：** SystemCapability.Health.HealthService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回401错误码。

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| sampleReal | [SampleReal](health-api-healthservice.md#samplereal)[] | 是 | 融合运动数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types. |

**说明** 

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const sampleReal: healthService.SampleReal = {
    dataType: { id: 50004 },
    time: 1695740400000, // 2023-09-26 23:00:00,
    fields: {
      hr: 90
    }
  };
  await healthService.workout.sendData([sampleReal]);
  hilog.info(0x0000, 'testTag', 'Succeeded in sending data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to send data. Code: ${err.code}, message: ${err.message}`);
}
```

### workout.sendEvent

sendEvent(event: SampleEvent): Promise<void>

下发控制事件到联动设备，使用Promise异步回调。

**系统能力：** SystemCapability.Health.HealthService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回401错误码。

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| event | [SampleEvent](health-api-healthservice.md#sampleevent) | 是 | 联动控制事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |

**说明** 

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const sampleEvent: healthService.SampleEvent = {
    eventId: 800400002,
    eventLevel: 0,
    eventData: 'start'
  };
  await healthService.workout.sendEvent(sampleEvent);
  hilog.info(0x0000, 'testTag', 'Succeeded in sending event.');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to send event. Code: ${err.code}, message: ${err.message}`);
}
```

### workout.getCurrentSportInfo

getCurrentSportInfo(): Promise<SportInfo>

获取运动状态，使用Promise异步回调。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SportInfo](health-api-healthservice.md#sportinfo)> | Promise对象，返回运动状态信息。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. Require workout management permission.Refer to the development documentation for permission request. |

**说明** 

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  await healthService.workout.getCurrentSportInfo();
  hilog.info(0x0000, 'testTag', 'Succeeded in getting current sportInfo');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to getting current sportInfo'. Code: ${err.code}, message: ${err.message}`);
}
```
