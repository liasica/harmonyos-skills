---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/car-smartmobilitycommon
title: smartMobilityCommon（智慧出行场景）
breadcrumb: API参考 > 系统 > 硬件 > Car Kit（车服务） > ArkTS API > smartMobilityCommon（智慧出行场景）
category: harmonyos-references
scraped_at: 2026-04-28T08:10:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1f2c85c8b846da772f2e4c6b747c72ed42abb0303929cec207f9ca817be1bc9d
---

作为分布式业务公共功能提供给应用，实现监听分布式业务（HiCar、超级桌面等）的状态，以及事件监听的能力。

**起始版本：** 5.0.0(12)

## 导入模块

PhoneTablet

```
1. import { smartMobilityCommon } from '@kit.CarKit';
```

## SmartMobilityEvent

PhoneTablet

公共事件。

**系统能力：** SystemCapability.CarService.DistributedEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| eventName | string | 否 | 否 | 事件名，由业务方自定义。 |
| type | [SmartMobilityType](car-smartmobilitycommon.md#smartmobilitytype) | 否 | 否 | 业务类型。 |
| data | Record<string, Object> | 否 | 否 | 事件详细信息，内容由智慧出行业务和应用双方约定。 |

## SmartMobilityInfo

PhoneTablet

该类为智慧出行的状态信息，定义了当前的业务类型、连接状态、业务数据。

**系统能力：** SystemCapability.CarService.DistributedEngine

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| status | [SmartMobilityStatus](car-smartmobilitycommon.md#smartmobilitystatus) | 否 | 否 | 业务连接状态。 |
| type | [SmartMobilityType](car-smartmobilitycommon.md#smartmobilitytype) | 否 | 否 | 业务类型。 |
| data | Record<string, Object> | 否 | 否 | 连接详细信息，内容由智慧出行业务和应用双方约定。 |

## SmartMobilityStatus

PhoneTablet

业务连接状态枚举值。

**系统能力：** SystemCapability.CarService.DistributedEngine

**起始版本：** 5.0.0(12)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| IDLE | 0 | 业务处于空闲态，业务未启动时，默认为该值。 |
| RUNNING | 1 | 业务处于运行中。 |

## SmartMobilityType

PhoneTablet

业务类型枚举值。

**系统能力：** SystemCapability.CarService.DistributedEngine

**起始版本：** 5.0.0(12)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| HICAR | 0 | HiCar。 |
| SUPER\_LAUNCHER | 1 | 超级桌面。 |
| CAR\_HOP | 2 | 流转。 |

## getSmartMobilityAwareness

PhoneTablet

getSmartMobilityAwareness(): SmartMobilityAwareness

用于获取智慧出行管理类。

**系统能力：** SystemCapability.CarService.DistributedEngine

**设备行为差异**：对于6.0.0(22)及之前的版本，该接口在Phone中可正常使用，在其他设备类型中返回801错误码。在6.1.0(23)及之后版本该接口在Phone、Tablet中均可正常使用。

**需要权限：** ohos.permission.ACCESS\_CAR\_DISTRIBUTED\_ENGINE

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SmartMobilityAwareness](car-smartmobilitycommon.md#smartmobilityawareness) | 智慧出行管理类。 |

**示例：**

```
1. import { smartMobilityCommon } from '@kit.CarKit';

3. let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
```

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](car-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

## SmartMobilityAwareness

PhoneTablet

智慧出行管理类，用于调用智慧出行接口。

**系统能力：** SystemCapability.CarService.DistributedEngine

**起始版本：** 5.0.0(12)

### on('smartMobilityEvent')

PhoneTablet

on(type: 'smartMobilityEvent', smartMobilityTypes: SmartMobilityType[],callback: Callback<SmartMobilityEvent>): void

注册智慧出行业务的事件监听，例如导航流转完成后通知事件时，触发此回调执行。

**系统能力：** SystemCapability.CarService.DistributedEngine

**设备行为差异**：对于6.0.0(22)及之前的版本，该接口在Phone中可正常使用，在其他设备类型中返回801错误码。在6.1.0(23)及之后版本该接口在Phone、Tablet中均可正常使用。

**需要权限：** ohos.permission.ACCESS\_CAR\_DISTRIBUTED\_ENGINE

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅类型，该位置为常量值：  'smartMobilityEvent'，表示订阅事件监听。 |
| smartMobilityTypes | [SmartMobilityType](car-smartmobilitycommon.md#smartmobilitytype)[] | 是 | 业务类型数组，支持同时订阅多个业务。 |
| callback | Callback<[SmartMobilityEvent](car-smartmobilitycommon.md#smartmobilityevent)> | 是 | 出行业务事件回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](car-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter type;  3. Parameter verification failed;  4. The size of specified type is greater than 255. |
| 801 | Capability not supported. |

**示例：**

```
1. import { smartMobilityCommon } from '@kit.CarKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. // Get single instance of SmartMobilityAwareness.
6. let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
7. // 业务类型
8. let types: smartMobilityCommon.SmartMobilityType[] = [smartMobilityCommon.SmartMobilityType.CAR_HOP];
9. // 出行业务事件回调函数
10. const callBack = (event: smartMobilityCommon.SmartMobilityEvent) => {
11. hilog.info(0x0000, 'testTag', 'Received smart mobility event: ', JSON.stringify(event));
12. };
13. // 注册出行业务事件监听
14. awareness.on('smartMobilityEvent', types, callBack);
15. } catch (e) {
16. // 捕获接口调用异常时的错误码并做相应处理
17. hilog.error(0x0000, 'testTag', `on smart mobility event error, error code: ${e?.code}`);
18. }
```

### off('smartMobilityEvent')

PhoneTablet

off(type: 'smartMobilityEvent', smartMobilityTypes: SmartMobilityType[], callback?: Callback<SmartMobilityEvent>): void

取消注册智慧出行业务的事件监听。

**系统能力：** SystemCapability.CarService.DistributedEngine

**设备行为差异**：对于6.0.0(22)及之前的版本，该接口在Phone中可正常使用，在其他设备类型中返回801错误码。在6.1.0(23)及之后版本该接口在Phone、Tablet中均可正常使用。

**需要权限：** ohos.permission.ACCESS\_CAR\_DISTRIBUTED\_ENGINE

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅类型，该位置为常量值：  'smartMobilityEvent'，表示取消事件监听。 |
| smartMobilityTypes | [SmartMobilityType](car-smartmobilitycommon.md#smartmobilitytype)[] | 是 | 业务类型数组，支持同时取消多个业务监听。 |
| callback | Callback<[SmartMobilityEvent](car-smartmobilitycommon.md#smartmobilityevent)> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](car-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter type;  3. Parameter verification failed;  4. The size of specified type is greater than 255. |
| 801 | Capability not supported. |

**示例：**

```
1. import { smartMobilityCommon } from '@kit.CarKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. // Get single instance of SmartMobilityAwareness.
6. let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
7. // 业务类型
8. let types: smartMobilityCommon.SmartMobilityType[] = [smartMobilityCommon.SmartMobilityType.CAR_HOP];
9. // 出行业务事件回调函数
10. const callBack = (event: smartMobilityCommon.SmartMobilityEvent) => {
11. hilog.info(0x0000, 'testTag', 'Received smart mobility event: ', JSON.stringify(event));
12. };

14. // 解注册出行业务事件监听
15. awareness.off('smartMobilityEvent', types, callBack);
16. } catch (e) {
17. // 捕获接口调用异常时的错误码并做相应处理
18. hilog.error(0x0000, 'testTag', `off smart mobility event error, error code: ${e?.code}`);
19. }
```

### getSmartMobilityEvent

PhoneTablet

getSmartMobilityEvent(type: SmartMobilityType, eventName: string): SmartMobilityEvent

应用获取指定事件的信息。

**系统能力：** SystemCapability.CarService.DistributedEngine

**设备行为差异**：对于6.0.0(22)及之前的版本，该接口在Phone中可正常使用，在其他设备类型中返回801错误码。在6.1.0(23)及之后版本该接口在Phone、Tablet中均可正常使用。

**需要权限：** ohos.permission.ACCESS\_CAR\_DISTRIBUTED\_ENGINE

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SmartMobilityType](car-smartmobilitycommon.md#smartmobilitytype) | 是 | 业务类型。 |
| eventName | string | 是 | 事件名。取值有下面3种：  CAR\_HOP\_EVENT，流转事件。  HICAR\_EVENT，HiCar事件。  SUPER\_LAUNCHER\_EVENT，超级桌面事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SmartMobilityEvent](car-smartmobilitycommon.md#smartmobilityevent) | 公共事件信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](car-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter type;  3. Parameter verification failed;  4. The size of specified type is greater than 255. |
| 801 | Capability not supported. |

**示例：**

```
1. import { smartMobilityCommon } from '@kit.CarKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. // Get single instance of SmartMobilityAwareness.
6. let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
7. // 业务类型
8. let type = smartMobilityCommon.SmartMobilityType.CAR_HOP;
9. // 事件名称
10. let eventName: string = 'CAR_HOP_EVENT';
11. // 获取公共事件信息
12. let event: smartMobilityCommon.SmartMobilityEvent = awareness.getSmartMobilityEvent(type, eventName);
13. } catch (e) {
14. // 捕获接口调用异常时的错误码并做相应处理
15. hilog.error(0x0000, 'testTag', `get smart mobility event error, error code: ${e?.code}`);
16. }
```

### on('smartMobilityStatus')

PhoneTablet

on(type: 'smartMobilityStatus', smartMobilityTypes: SmartMobilityType[], callback: Callback<SmartMobilityInfo>): void

注册智慧出行连接状态的监听。

**系统能力：** SystemCapability.CarService.DistributedEngine

**设备行为差异**：对于6.0.0(22)及之前的版本，该接口在Phone中可正常使用，在其他设备类型中返回801错误码。在6.1.0(23)及之后版本该接口在Phone、Tablet中均可正常使用。

**需要权限：** ohos.permission.ACCESS\_CAR\_DISTRIBUTED\_ENGINE

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅类型，该位置为常量值：  'smartMobilityStatus'，表示订阅业务连接状态监听。 |
| smartMobilityTypes | [SmartMobilityType](car-smartmobilitycommon.md#smartmobilitytype)[] | 是 | 业务类型数组，支持同时订阅多个业务。 |
| callback | Callback<[SmartMobilityInfo](car-smartmobilitycommon.md#smartmobilityinfo)> | 是 | 出行连接状态回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](car-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter type;  3. Parameter verification failed;  4. The size of specified type is greater than 255. |
| 801 | Capability not supported. |

**示例：**

```
1. import { smartMobilityCommon } from '@kit.CarKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. // Get single instance of SmartMobilityAwareness.
6. let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
7. // 业务类型
8. let types: smartMobilityCommon.SmartMobilityType[] = [smartMobilityCommon.SmartMobilityType.HICAR];
9. // 出行连接状态回调函数
10. const callBack = (info: smartMobilityCommon.SmartMobilityInfo) => {
11. hilog.info(0x0000, 'testTag', 'Received smart mobility info: ', JSON.stringify(info));
12. };
13. // 注册智慧出行连接状态的监听
14. awareness.on('smartMobilityStatus', types, callBack);
15. } catch (e) {
16. // 捕获接口调用异常时的错误码并做相应处理
17. hilog.error(0x0000, 'testTag', `on smart mobility status error, error code: ${e?.code}`);
18. }
```

### off('smartMobilityStatus')

PhoneTablet

off(type: 'smartMobilityStatus', smartMobilityTypes: SmartMobilityType[], callback?: Callback<SmartMobilityInfo>): void

取消注册智慧出行连接状态的监听。

**系统能力：** SystemCapability.CarService.DistributedEngine

**设备行为差异**：对于6.0.0(22)及之前的版本，该接口在Phone中可正常使用，在其他设备类型中返回801错误码。在6.1.0(23)及之后版本该接口在Phone、Tablet中均可正常使用。

**需要权限：** ohos.permission.ACCESS\_CAR\_DISTRIBUTED\_ENGINE

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅类型，该位置为常量值：  'smartMobilityStatus'，表示取消业务连接状态监听。 |
| smartMobilityTypes | [SmartMobilityType](car-smartmobilitycommon.md#smartmobilitytype)[] | 是 | 业务类型数组，支持同时取消多个业务监听。 |
| callback | Callback<[SmartMobilityInfo](car-smartmobilitycommon.md#smartmobilityinfo)> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](car-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter type;  3. Parameter verification failed;  4. The size of specified type is greater than 255. |
| 801 | Capability not supported. |

**示例：**

```
1. import { smartMobilityCommon } from '@kit.CarKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. // Get single instance of SmartMobilityAwareness.
6. let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
7. // 业务类型
8. let types: smartMobilityCommon.SmartMobilityType[] = [smartMobilityCommon.SmartMobilityType.HICAR];
9. // 出行连接状态回调函数
10. const callBack = (info: smartMobilityCommon.SmartMobilityInfo) => {
11. hilog.info(0x0000, 'testTag', 'Received smart mobility info: ', JSON.stringify(info));
12. };
13. // 取消注册智慧出行连接状态的监听
14. awareness.off('smartMobilityStatus', types);
15. } catch (e) {
16. // 捕获接口调用异常时的错误码并做相应处理
17. hilog.error(0x0000, 'testTag', `off smart mobility status error, error code: ${e?.code}`);
18. }
```

### getSmartMobilityStatus

PhoneTablet

getSmartMobilityStatus(type: SmartMobilityType): SmartMobilityInfo

获取智慧出行连接状态。

**系统能力：** SystemCapability.CarService.DistributedEngine

**设备行为差异**：对于6.0.0(22)及之前的版本，该接口在Phone中可正常使用，在其他设备类型中返回801错误码。在6.1.0(23)及之后版本该接口在Phone、Tablet中均可正常使用。

**需要权限：** ohos.permission.ACCESS\_CAR\_DISTRIBUTED\_ENGINE

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SmartMobilityType](car-smartmobilitycommon.md#smartmobilitytype) | 是 | 业务类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SmartMobilityInfo](car-smartmobilitycommon.md#smartmobilityinfo) | 业务状态信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](car-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter type;  3. Parameter verification failed;  4. The size of specified type is greater than 255. |
| 801 | Capability not supported. |

**示例：**

```
1. import { smartMobilityCommon } from '@kit.CarKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
6. // 业务类型
7. let type = smartMobilityCommon.SmartMobilityType.HICAR;
8. // 获取业务状态信息
9. let ret = awareness.getSmartMobilityStatus(type);
10. } catch (e) {
11. // 捕获接口调用异常时的错误码并做相应处理
12. hilog.error(0x0000, 'testTag', `get smart mobility status error, error code: ${e?.code}`);
13. }
```
