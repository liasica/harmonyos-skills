---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthservice-lite
title: healthService (运动健康联动服务)(Lite)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > healthService (运动健康联动服务)(Lite)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:55+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:85aa1911540cc90e5545a9da31e6e718d5b4cd9c942a17e6c9942e2ee342de9a
---

本模块提供运动健康联动服务。

**起始版本：** 6.1.1(24)

## 导入模块

```javascript
import healthService from '@hms.health.service';
```

## SampleReal

SampleReal<K extends Record<string, [healthStore.HealthValueType](health-api-healthstore-lite.md#healthvaluetype)> = Record<string, [healthStore.HealthValueType](health-api-healthstore-lite.md#healthvaluetype)>>

联动实时运动数据。

**系统能力：** SystemCapability.Health.HealthService.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| dataType | [healthStore.DataType](health-api-healthstore-lite.md#datatype) | 否 | 否 | 实时融合数据类型。 |
| time | number | 否 | 否 | 实时融合数据产生时间，Unix时间戳，单位：ms。 |
| fields | Pick<K, keyof K> | 否 | 否 | 实时融合数据字段。 |
| deviceUniqueId | string | 否 | 是 | 实时融合数据来源，若未填写，默认为空。 |

## workout

提供运动健康实时数据。

**系统能力：** SystemCapability.Health.HealthService.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

### ConfigType

type ConfigType = number | string | boolean

联动配置项类型。

**系统能力：** SystemCapability.Health.HealthService.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| number | 表示值类型为数字，可取任意值。 |
| string | 表示值类型为字符串，可取任意值。 |
| boolean | 表示值类型为布尔类型，可取true或false，具体含义以实际使用场景为准。 |

### DeviceState

联动设备状态。

**系统能力：** SystemCapability.Health.HealthService.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 设备ID。 |
| state | number | 否 | 否 | 设备状态。 |
| deviceName | string | 否 | 是 | 设备名称，若未填写，默认为空。 |

### Goal

联动运动目标。

**系统能力：** SystemCapability.Health.HealthService.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| type | number | 否 | 否 | 目标类型，取值参考：[TargetType](health-api-healthservice-lite.md#targettype)。 |
| value | number | 否 | 否 | 目标值。 |

### LinkageType

联动类型。

**系统能力：** SystemCapability.Health.HealthService.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COURSE\_LINK | 0 | 课程联动。 |
| ACTIVITY\_LINK | 1 | 运动联动。 |

### StartCode

联动开启结果码。

**系统能力：** SystemCapability.Health.HealthService.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 联动开启成功。 |
| WORKOUT\_WORKING | 1 | 联动已开始。 |
| NO\_SUPPORTED\_DEVICE | 2 | 无可支持联动的设备。 |
| DEVICE\_BUSY | 3 | 联动设备忙碌。 |

### StartResult

联动开启结果。

**系统能力：** SystemCapability.Health.HealthService.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| startCode | [StartCode](health-api-healthservice-lite.md#startcode) | 否 | 否 | 联动开启结果码。 |
| deviceState | [DeviceState](health-api-healthservice-lite.md#devicestate)[] | 否 | 否 | 联动设备状态。 |

### TargetType

联动目标类型。

**系统能力：** SystemCapability.Health.HealthService.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 无目标。 |
| DISTANCE | 1 | 距离。 |
| CALORIE | 2 | 卡路里。 |
| TIME | 3 | 时长。 |
| SKIPPING\_TIMES | 4 | 跳绳次数。 |

### WorkoutConfig

联动配置项。

**系统能力：** SystemCapability.Health.HealthService.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| linkageType | [LinkageType](health-api-healthservice-lite.md#linkagetype) | 否 | 否 | 联动类型。 |
| sportType | number | 否 | 否 | 运动类型，参见[锻炼记录类型常量](health-api-exercisesequencehelper-lite.md)子数据类型id。 |
| activityGoals | [Goal](health-api-healthservice-lite.md#goal)[] | 否 | 是 | 联动运动目标，若未填写，默认为空。 |
| extensionConfig | Record<string, [ConfigType](health-api-healthservice-lite.md#configtype)> | 否 | 是 | 扩展配置项，若未填写，默认为空。 |

### DynamicLibResult

加载算法库操作结果类型。

**系统能力：** SystemCapability.Health.HealthService.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| operationCode | [DynamicLibErrorCode](health-api-healthservice-lite.md#dynamicliberrorcode) | 否 | 否 | 加载算法库操作结果码。 |

### DynamicLibErrorCode

加载或卸载算法库文件操作结果码。

**系统能力：** SystemCapability.Health.HealthService.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OPERATION\_SUCCESS | 0 | 操作成功。 |
| FILE\_NOT\_FOUND | 1 | 算法库文件未找到。 |
| SERVICE\_BUSY | 2 | 算法库文件已被加载。 |
| OPERATION\_FAILED | 3 | 操作失败。 |
| SYSTEM\_INTERNAL\_ERROR | 4 | 未知错误。 |

### workout.config

config(workoutConfig: WorkoutConfig): void

运动联动配置。

**系统能力：** SystemCapability.Health.HealthService.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| workoutConfig | [WorkoutConfig](health-api-healthservice-lite.md#workoutconfig) | 是 | 联动配置项。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. Please ensure that the app has applied for the Health Service Kit, selected the product type, enabled the corresponding data read and write permissions, and the user has completed authorization. |
| [1009104003](errorcode-healthservice.md#section1009104003-非法指令) | Illegal command. Called when workout not in stoped or idle state. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

**示例：**

```javascript
import healthService from '@hms.health.service';
import healthStore from '@hms.health.store';

try {
  let workoutOptions = {
    linkageType: healthService.workout.LinkageType.ACTIVITY_LINK,
    sportType: healthStore.exerciseSequenceHelper.badminton.EXERCISE_TYPE.id
  };
  healthService.workout.config(workoutOptions);
} catch (err) {
  // 异常处理流程
}
```

### workout.start

start(): StartResult

开启运动联动。

**说明** 

该接口调用前，需先使用[config](health-api-healthservice-lite.md#workoutconfig)方法进行联动配置。

**系统能力：** SystemCapability.Health.HealthService.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [StartResult](health-api-healthservice-lite.md#startresult) | 返回联动开启结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. Please ensure that the app has applied for the Health Service Kit, selected the product type, enabled the corresponding data read and write permissions, and the user has completed authorization. |
| [1009104001](errorcode-healthservice.md#section1009104001-联动已开启) | Sport service busy. Workout is already started by other application. |
| [1009104002](errorcode-healthservice.md#section1009104002-不支持运动类型) | Unsupported sport type. |
| [1009104003](errorcode-healthservice.md#section1009104003-非法指令) | Illegal command. Called when workout in sporting, paused or stopped state. |
| [1009104004](errorcode-healthservice.md#section1009104004-权限校验异常) | Permission verification error. Application has no permission, such as Motion Permission. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

**示例：**

```javascript
import healthService from '@hms.health.service';
import healthStore from '@hms.health.store';

try {
  healthService.workout.start();
} catch (err) {
  // 异常处理流程
}
```

### workout.pause

pause(): void

暂停运动联动。

**说明** 

该接口调用前，需先使用[start](health-api-healthservice-lite.md#workoutstart)方法确保运动联动已经开启。

**系统能力：** SystemCapability.Health.HealthService.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. Please ensure that the app has applied for the Health Service Kit, selected the product type, enabled the corresponding data read and write permissions, and the user has completed authorization. |
| [1009104001](errorcode-healthservice.md#section1009104001-联动已开启) | Sport service busy. Workout is already started by other application. |
| [1009104003](errorcode-healthservice.md#section1009104003-非法指令) | Illegal command. Called when workout in ready, paused or stoped state. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

**示例：**

```javascript
import healthService from '@hms.health.service';

try {
  healthService.workout.pause();
} catch (err) {
  // 异常处理流程
}
```

### workout.resume

resume(): void

恢复运动联动。

**说明** 

该接口调用前，需先使用[pause](health-api-healthservice-lite.md#workoutpause)方法暂停运动联动。

**系统能力：** SystemCapability.Health.HealthService.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. Please ensure that the app has applied for the Health Service Kit, selected the product type, enabled the corresponding data read and write permissions, and the user has completed authorization. |
| [1009104001](errorcode-healthservice.md#section1009104001-联动已开启) | Sport service busy. Workout is already started by other application. |
| [1009104003](errorcode-healthservice.md#section1009104003-非法指令) | Illegal command. Called when workout in ready, sporting or stopped state. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

**示例：**

```javascript
import healthService from '@hms.health.service';

try {
  healthService.workout.resume();
} catch (err) {
  // 异常处理流程
}
```

### workout.stop

stop(): void

停止联动。

**说明** 

该接口调用前，需先使用[start](health-api-healthservice-lite.md#workoutstart)方法确保联动已经开启，上述接口调用后，当前运动联动被停止，其他运动可开启联动。

**系统能力：** SystemCapability.Health.HealthService.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. Please ensure that the app has applied for the Health Service Kit, selected the product type, enabled the corresponding data read and write permissions, and the user has completed authorization. |
| [1009104003](errorcode-healthservice.md#section1009104003-非法指令) | Illegal command. Called when workout is not started. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

**示例：**

```javascript
import healthService from '@hms.health.service';

try {
  healthService.workout.stop();
} catch (err) {
  // 异常处理流程
}
```

### workout.onData(deprecated)

onData(dataType: undefined, listener: Callback<SampleReal[]>): void

订阅所有类型的数据，使用callback异步回调。

**说明** 

该接口调用前，需先使用[start](health-api-healthservice-lite.md#workoutstart)方法确保联动已经开启。

**系统能力：** SystemCapability.Health.HealthService.Lite

**模型约束：** 此接口仅可在FA模型下使用。

**起始版本：** 6.1.1(24)

**废弃版本：** 26.0.0

**替代接口：** [workout.onData](health-api-healthservice-lite.md#workoutondata)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| dataType | undefined | 是 | 监听所有联动运动数据类型。 |
| listener | Callback<[SampleReal](health-api-healthservice-lite.md#samplereal)[]> | 是 | 回调函数，返回联动运动数据。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. Please ensure that the app has applied for the Health Service Kit, selected the product type, enabled the corresponding data read and write permissions, and the user has completed authorization. |
| [1009104001](errorcode-healthservice.md#section1009104001-联动已开启) | Sport service busy. Workout is already started by other application. |
| [1009104003](errorcode-healthservice.md#section1009104003-非法指令) | Illegal command. Called when workout is not started. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

**示例：**

```javascript
import healthService from '@hms.health.service';

try {
  const callback = (sampleReals) => {
    // 运动数据回调处理流程
  };
  healthService.workout.onData(undefined, callback);
} catch (err) {
  // 异常处理流程
}
```

### workout.onData

onData(listener: Callback<SampleReal[]>): void

订阅所有类型的数据，使用callback异步回调。

**说明** 

该接口调用前，需先使用[start](health-api-healthservice-lite.md#workoutstart)方法确保联动已经开启。

**系统能力：** SystemCapability.Health.HealthService.Lite

**模型约束：** 此接口仅可在FA模型下使用。

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| listener | Callback<[SampleReal](health-api-healthservice-lite.md#samplereal)[]> | 是 | 回调函数，返回联动运动数据。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. For the app, ensure that you have requested Health Service Kit, selected the product type, and enabled required data read and write permissions, and that the user has granted authorization. |
| [1009104001](errorcode-healthservice.md#section1009104001-联动已开启) | Sports service busy. Workout has already been started by another app. |
| [1009104003](errorcode-healthservice.md#section1009104003-非法指令) | Invalid command. The API is called when workout is not started. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | Internal system error. |

**示例：**

```javascript
import healthService from '@hms.health.service';

try {
  const callback = (sampleReals) => {
    // 运动数据回调处理流程
  };
  healthService.workout.onData(callback);
} catch (err) {
  // 异常处理流程
}
```

### workout.offData(deprecated)

offData(dataType: undefined, listener?: Callback<SampleReal[]>): void

取消订阅所有类型的数据。

**说明** 

该接口调用前，需先使用[start](health-api-healthservice-lite.md#workoutstart)方法确保联动已经开启。

**系统能力：** SystemCapability.Health.HealthService.Lite

**模型约束：** 此接口仅可在FA模型下使用。

**起始版本：** 6.1.1(24)

**废弃版本：** 26.0.0

**替代接口：** [workout.offData](health-api-healthservice-lite.md#workoutoffdata)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| dataType | undefined | 是 | 监听所有联动运动数据类型。 |
| listener | Callback<[SampleReal](health-api-healthservice-lite.md#samplereal)[]> | 否 | 需要取消订阅的回调函数，若不填写则代表取消所有监听。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. Please ensure that the app has applied for the Health Service Kit, selected the product type, enabled the corresponding data read and write permissions, and the user has completed authorization. |
| [1009104001](errorcode-healthservice.md#section1009104001-联动已开启) | Sport service busy. Workout is already started by other application. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

**示例：**

```javascript
import healthService from '@hms.health.service';

try {
  const callback = (sampleReals) => {
    // 数据回调处理流程
  };
  healthService.workout.offData(undefined, callback);
} catch (err) {
  // 异常处理流程
}
```

### workout.offData

offData(listener?: Callback<SampleReal[]>): void

取消订阅所有类型的数据。

**说明** 

该接口调用前，需先使用[start](health-api-healthservice-lite.md#workoutstart)方法确保联动已经开启。

**系统能力：** SystemCapability.Health.HealthService.Lite

**模型约束：** 此接口仅可在FA模型下使用。

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| listener | Callback<[SampleReal](health-api-healthservice-lite.md#samplereal)[]> | 否 | 需要取消订阅的回调函数，若不填写则代表取消所有监听。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. For the app, ensure that you have requested Health Service Kit, selected the product type, and enabled required data read and write permissions, and that the user has granted authorization. |
| [1009104001](errorcode-healthservice.md#section1009104001-联动已开启) | Sports service busy. Workout has already been started by another app. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | Internal system error. |

**示例：**

```javascript
import healthService from '@hms.health.service';

try {
  const callback = (sampleReals) => {
    // 数据回调处理流程
  };
  healthService.workout.offData(callback);
} catch (err) {
  // 异常处理流程
}
```

### workout.sendData

sendData(sampleReal: SampleReal[]): void

下发融合运动数据到联动设备。

**说明** 

该接口调用前，需先使用[start](health-api-healthservice-lite.md#workoutstart)方法确保联动已经开启。

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Health.HealthService.Lite

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| sampleReal | [SampleReal](health-api-healthservice-lite.md#samplereal)[] | 是 | 融合运动数据。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. Please ensure that the app has applied for the Health Service Kit, selected the product type, enabled the corresponding data read and write permissions, and the user has completed authorization. |
| [1009104001](errorcode-healthservice.md#section1009104001-联动已开启) | Sport service busy. Workout is already started by other application. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

**示例：**

```javascript
import healthService from '@hms.health.service';
import healthStore from '@hms.health.store';

try {
  const sampleReal = {
    dataType: { id: healthStore.healthDataTypes.WORKOUT_REALTIME.id },
    time: 1695740400000, // 2023-09-26 23:00:00,
    fields: {
      forehandStroke: 45
    }
  };
  healthService.workout.sendData([sampleReal]);
} catch (err) {
    // 异常处理流程
}
```

### workout.load

load(path: string): void

加载算法库文件，加载后可使用算法库算法。

**系统能力：** SystemCapability.Health.HealthService.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| path | string | 是 | 算法库文件在代码工程中存放的路径，例如：common/dynamic\_example.so。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. Please ensure that the app has applied for the Health Service Kit, selected the product type, enabled the corresponding data read and write permissions, and the user has completed authorization. |
| [1009104001](errorcode-healthservice.md#section1009104001-联动已开启) | Sport service busy. Workout is already started by other application. |
| [1009104003](errorcode-healthservice.md#section1009104003-非法指令) | Illegal command. Called when workout is not started. |
| [1009104004](errorcode-healthservice.md#section1009104004-权限校验异常) | Permission verification error. Application has no permission, such as Motion Permission. |
| [1009104005](errorcode-healthservice.md#section1009104005-动态库加载异常) | Failed to load the dynamic library. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

**示例：**

```javascript
import healthService from '@hms.health.service';

try {
  const path = "common/dynamic_example.so";
  healthService.workout.load(path);
} catch (err) {
  // 异常处理流程
}
```

### workout.load

load(path: string, callback: Callback<[DynamicLibResult](health-api-healthservice-lite.md#dynamiclibresult)>): void

加载算法库文件，加载后可使用算法库算法，使用callback异步回调。

**系统能力：** SystemCapability.Health.HealthService.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| path | string | 是 | 算法库文件在代码工程中存放的路径，例如：common/dynamic\_example.so。 |
| callback | Callback<[DynamicLibResult](health-api-healthservice-lite.md#dynamiclibresult)> | 是 | 回调函数，返回算法库加载结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. Please ensure that the app has applied for the Health Service Kit, selected the product type, enabled the corresponding data read and write permissions, and the user has completed authorization. |
| [1009104001](errorcode-healthservice.md#section1009104001-联动已开启) | Sport service busy. Workout is already started by other application. |
| [1009104003](errorcode-healthservice.md#section1009104003-非法指令) | Illegal command. Called when workout is not started. |
| [1009104004](errorcode-healthservice.md#section1009104004-权限校验异常) | Permission verification error. Application has no permission, such as Motion Permission. |
| [1009104005](errorcode-healthservice.md#section1009104005-动态库加载异常) | Failed to load the dynamic library. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

**示例：**

```javascript
import healthService from '@hms.health.service';

try {
  const path = "common/dynamic_example.so";
  healthService.workout.load(path, (result) => {
    switch (result.operationCode) {
      case healthService.workout.DynamicLibErrorCode.OPERATION_SUCCESS:
          // 加载成功处理流程
          break;
      case healthService.workout.DynamicLibErrorCode.FILE_NOT_FOUND:
          // so文件未找到处理流程
          break;
      case healthService.workout.DynamicLibErrorCode.SERVICE_BUSY:
          // so文件已加载处理流程
          break;
      case healthService.workout.DynamicLibErrorCode.OPERATION_FAILED:
          // 操作失败处理流程
          break;
      default :
          // 未知错误处理流程
    }
  });
} catch (err) {
  // 异常处理流程
}
```

### workout.unload

unload(path: string): void

卸载算法库文件，卸载后无法使用算法库算法。

**系统能力：** SystemCapability.Health.HealthService.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| path | string | 是 | 算法库文件在代码工程中存放的路径，例如：common/dynamic\_example.so。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. Please ensure that the app has applied for the Health Service Kit, selected the product type, enabled the corresponding data read and write permissions, and the user has completed authorization. |
| [1009104001](errorcode-healthservice.md#section1009104001-联动已开启) | Sport service busy. Workout is already started by other application. |
| [1009104003](errorcode-healthservice.md#section1009104003-非法指令) | Illegal command. Called when workout is not started. |
| [1009104004](errorcode-healthservice.md#section1009104004-权限校验异常) | Permission verification error. Application has no permission, such as Motion Permission. |
| [1009104006](errorcode-healthservice.md#section1009104006-动态库卸载异常) | Failed to unload the dynamic library. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

**示例：**

```javascript
import healthService from '@hms.health.service';

try {
  const path = "common/dynamic_example.so";
  healthService.workout.unload(path);
} catch (err) {
  // 异常处理流程
}
```

### workout.unload

unload(path: string, callback: Callback<[DynamicLibResult](health-api-healthservice-lite.md#dynamiclibresult)>): void

卸载算法库文件，卸载后无法使用算法库算法，使用callback异步回调。

**系统能力：** SystemCapability.Health.HealthService.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| path | string | 是 | 算法库文件在代码工程中存放的路径，例如：common/dynamic\_example.so。 |
| callback | Callback<[DynamicLibResult](health-api-healthservice-lite.md#dynamiclibresult)> | 是 | 回调函数，返回算法库卸载结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. Please ensure that the app has applied for the Health Service Kit, selected the product type, enabled the corresponding data read and write permissions, and the user has completed authorization. |
| [1009104001](errorcode-healthservice.md#section1009104001-联动已开启) | Sport service busy. Workout is already started by other application. |
| [1009104003](errorcode-healthservice.md#section1009104003-非法指令) | Illegal command. Called when workout is not started. |
| [1009104004](errorcode-healthservice.md#section1009104004-权限校验异常) | Permission verification error. Application has no permission, such as Motion Permission. |
| [1009104006](errorcode-healthservice.md#section1009104006-动态库卸载异常) | Failed to unload the dynamic library. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

**示例：**

```javascript
import healthService from '@hms.health.service';

try {
  const path = "common/dynamic_example.so";
  healthService.workout.unload(path, (result) => {
    switch (result.operationCode) {
      case healthService.workout.DynamicLibErrorCode.OPERATION_SUCCESS:
        // 加载成功处理流程
        break;
      case healthService.workout.DynamicLibErrorCode.FILE_NOT_FOUND:
        // so文件未找到处理流程
        break;
      case healthService.workout.DynamicLibErrorCode.OPERATION_FAILED:
        // 操作失败处理流程
        break;
      default :
        // 未知错误处理流程
    }
  });
} catch (err) {
  // 异常处理流程
}
```
