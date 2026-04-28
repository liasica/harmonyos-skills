---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-workscheduler
title: @ohos.resourceschedule.workScheduler (延迟任务调度)
breadcrumb: API参考 > 应用框架 > Background Tasks Kit（后台任务开发服务） > ArkTS API > @ohos.resourceschedule.workScheduler (延迟任务调度)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:33+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:90a8812141e1ecf8041aa4b65ce25bc62288a9c494412c18df0ac49a7cc7b4c8
---

本模块提供延迟任务注册、取消、查询的能力。在开发过程中，对于实时性要求不高的任务，可以调用本模块接口注册延迟任务，在系统空闲时根据性能、功耗、热等情况进行调度执行。开发指导请参考[延迟任务开发指南](../harmonyos-guides/work-scheduler.md)。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { workScheduler } from '@kit.BackgroundTasksKit';
```

## workScheduler.startWork

PhonePC/2in1TabletTVWearable

startWork(work: WorkInfo): void

申请延迟任务，成功后会把任务添加到执行队列，满足触发条件后由系统调度执行。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| work | [WorkInfo](js-apis-resourceschedule-workscheduler.md#workinfo) | 是 | 指定延迟任务具体信息，比如延迟任务ID、触发条件等。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[workScheduler错误码](errorcode-workscheduler.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9700001 | Memory operation failed. |
| 9700002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9700003 | System service operation failed. |
| 9700004 | Check on workInfo failed. |
| 9700005 | Calling startWork failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { workScheduler } from '@kit.BackgroundTasksKit';

4. let workInfo: workScheduler.WorkInfo = {
5. workId: 1,
6. batteryStatus:workScheduler.BatteryStatus.BATTERY_STATUS_LOW,
7. isRepeat: false,
8. isPersisted: true,
9. bundleName: "com.example.myapplication",
10. abilityName: "MyExtension",
11. parameters: {
12. mykey0: 1,
13. mykey1: "string value",
14. mykey2: true,
15. mykey3: 1.5
16. }
17. }
18. try{
19. workScheduler.startWork(workInfo);
20. console.info('workschedulerLog startWork success');
21. } catch (error) {
22. console.error(`workschedulerLog startwork failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
23. }
```

## workScheduler.stopWork

PhonePC/2in1TabletTVWearable

stopWork(work: WorkInfo, needCancel?: boolean): void

取消延迟任务。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| work | [WorkInfo](js-apis-resourceschedule-workscheduler.md#workinfo) | 是 | 要停止或移除的延迟任务。 |
| needCancel | boolean | 否 | 是否需要移除任务。  true表示停止并移除，false表示只停止不移除。默认为false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[workScheduler错误码](errorcode-workscheduler.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9700001 | Memory operation failed. |
| 9700002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9700003 | System service operation failed. |
| 9700004 | Check on workInfo failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { workScheduler } from '@kit.BackgroundTasksKit';

4. let workInfo: workScheduler.WorkInfo = {
5. workId: 1,
6. batteryStatus:workScheduler.BatteryStatus.BATTERY_STATUS_LOW,
7. isRepeat: false,
8. isPersisted: true,
9. bundleName: "com.example.myapplication",
10. abilityName: "MyExtension",
11. parameters: {
12. mykey0: 1,
13. mykey1: "string value",
14. mykey2: true,
15. mykey3: 1.5
16. }
17. }
18. try{
19. workScheduler.stopWork(workInfo, false);
20. console.info('workschedulerLog stopWork success');
21. } catch (error) {
22. console.error(`workschedulerLog stopWork failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
23. }
```

## workScheduler.getWorkStatus

PhonePC/2in1TabletTVWearable

getWorkStatus(workId: number, callback : AsyncCallback<WorkInfo>): void

通过workId获取延迟任务，使用Callback异步回调。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| workId | number | 是 | 延迟任务Id。 |
| callback | AsyncCallback<[WorkInfo](js-apis-resourceschedule-workscheduler.md#workinfo)> | 是 | 回调函数。如果workId有效，则返回从WorkSchedulerService获取的任务，否则抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[workScheduler错误码](errorcode-workscheduler.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Parameter verification failed. |
| 9700001 | Memory operation failed. |
| 9700002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9700003 | System service operation failed. |
| 9700004 | Check on workInfo failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { workScheduler } from '@kit.BackgroundTasksKit';

4. workScheduler.getWorkStatus(50, (error: BusinessError, res: workScheduler.WorkInfo) => {
5. if (error) {
6. console.error(`workschedulerLog getWorkStatus failed. code is ${error.code} message is ${error.message}`);
7. } else {
8. console.info(`workschedulerLog getWorkStatus success, ${JSON.stringify(res)}`);
9. }
10. });
```

## workScheduler.getWorkStatus

PhonePC/2in1TabletTVWearable

getWorkStatus(workId: number): Promise<WorkInfo>

通过workId获取延迟任务，使用Promise异步回调。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| workId | number | 是 | 延迟任务Id。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[WorkInfo](js-apis-resourceschedule-workscheduler.md#workinfo)> | Promise对象，如果workId有效，则返回从WorkSchedulerService获取的任务，否则抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[workScheduler错误码](errorcode-workscheduler.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Parameter verification failed. |
| 9700001 | Memory operation failed. |
| 9700002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9700003 | System service operation failed. |
| 9700004 | Check on workInfo failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { workScheduler } from '@kit.BackgroundTasksKit';

4. workScheduler.getWorkStatus(50).then((res: workScheduler.WorkInfo) => {
5. console.info(`workschedulerLog getWorkStatus success, ${JSON.stringify(res)}`);
6. }).catch((error: BusinessError) => {
7. console.error(`workschedulerLog getWorkStatus failed. code is ${error.code} message is ${error.message}`);
8. })
```

## workScheduler.obtainAllWorks(deprecated)

PhonePC/2in1TabletTVWearable

obtainAllWorks(callback : AsyncCallback<void>) : Array<WorkInfo>

获取当前应用所有的延迟任务，使用Callback异步回调。

说明

从API version 9开始支持，从API version 10开始废弃，建议使用[obtainAllWorks10+](js-apis-resourceschedule-workscheduler.md#workschedulerobtainallworks10)替代。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数，获取成功时，err为undefined，否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[WorkInfo](js-apis-resourceschedule-workscheduler.md#workinfo)> | 延迟任务列表，如果已添加延迟任务到执行队列，则返回当前应用所有的延迟任务列表；否则返回空列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[workScheduler错误码](errorcode-workscheduler.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 9700001 | Memory operation failed. |
| 9700002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9700003 | System service operation failed. |

## workScheduler.obtainAllWorks10+

PhonePC/2in1TabletTVWearable

obtainAllWorks(callback : AsyncCallback<Array<WorkInfo>>): void

获取当前应用所有的延迟任务，使用Callback异步回调。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<WorkInfo>> | 是 | 回调函数，获取成功时，返回当前应用所有的延迟任务列表，否则抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[workScheduler错误码](errorcode-workscheduler.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 9700001 | Memory operation failed. |
| 9700002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9700003 | System service operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { workScheduler } from '@kit.BackgroundTasksKit';

4. workScheduler.obtainAllWorks((error: BusinessError, res: Array<workScheduler.WorkInfo>) =>{
5. if (error) {
6. console.error(`workschedulerLog obtainAllWorks failed. code is ${error.code} message is ${error.message}`);
7. } else {
8. console.info(`workschedulerLog obtainAllWorks success, data is: ${JSON.stringify(res)}`);
9. }
10. });
```

## workScheduler.obtainAllWorks

PhonePC/2in1TabletTVWearable

obtainAllWorks(): Promise<Array<WorkInfo>>

获取当前应用所有的延迟任务，使用Promise异步回调。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[WorkInfo](js-apis-resourceschedule-workscheduler.md#workinfo)>> | Promise对象，返回当前应用所有的延迟任务。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[workScheduler错误码](errorcode-workscheduler.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 9700001 | Memory operation failed. |
| 9700002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9700003 | System service operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { workScheduler } from '@kit.BackgroundTasksKit';

4. workScheduler.obtainAllWorks().then((res: Array<workScheduler.WorkInfo>) => {
5. console.info(`workschedulerLog obtainAllWorks success, data is: ${JSON.stringify(res)}`);
6. }).catch((error: BusinessError) => {
7. console.error(`workschedulerLog obtainAllWorks failed. code is ${error.code} message is ${error.message}`);
8. })
```

## workScheduler.stopAndClearWorks

PhonePC/2in1TabletTVWearable

stopAndClearWorks(): void

停止和取消当前应用所有的延迟任务。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[workScheduler错误码](errorcode-workscheduler.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 9700001 | Memory operation failed. |
| 9700002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9700003 | System service operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { workScheduler } from '@kit.BackgroundTasksKit';

4. try{
5. workScheduler.stopAndClearWorks();
6. console.info(`workschedulerLog stopAndClearWorks success`);
7. } catch (error) {
8. console.error(`workschedulerLog stopAndClearWorks failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
9. }
```

## workScheduler.isLastWorkTimeOut(deprecated)

PhonePC/2in1TabletTVWearable

isLastWorkTimeOut(workId: number, callback : AsyncCallback<void>): boolean

从API version 9开始支持，从API version 10开始废弃，建议使用[isLastWorkTimeOut10+](js-apis-resourceschedule-workscheduler.md#workschedulerislastworktimeout10)替代。

检查延迟任务的最后一次执行是否超时，使用Callback异步回调。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| workId | number | 是 | 指定延迟任务的Id。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 检查延迟任务最后一次执行是否超时，如果workId有效，则返回从WorkSchedulerService获取的任务最后一次执行是否超时；否则，抛出异常。true，对应workId延迟任务最后一次执行超时，false，对应workId延迟任务最后一次执行未超时。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[workScheduler错误码](errorcode-workscheduler.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Parameter verification failed. |
| 9700001 | Memory operation failed. |
| 9700002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9700003 | System service operation failed. |
| 9700004 | Check on workInfo failed. |

## workScheduler.isLastWorkTimeOut10+

PhonePC/2in1TabletTVWearable

isLastWorkTimeOut(workId: number, callback : AsyncCallback<boolean>): void

检查延迟任务的最后一次执行是否超时，使用Callback异步回调。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| workId | number | 是 | 指定延迟任务的Id。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[workScheduler错误码](errorcode-workscheduler.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Parameter verification failed. |
| 9700001 | Memory operation failed. |
| 9700002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9700003 | System service operation failed. |
| 9700004 | Check on workInfo failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { workScheduler } from '@kit.BackgroundTasksKit';

4. workScheduler.isLastWorkTimeOut(500, (error: BusinessError, res: boolean) =>{
5. if (error) {
6. console.error(`workschedulerLog isLastWorkTimeOut failed. code is ${error.code} message is ${error.message}`);
7. } else {
8. console.info(`workschedulerLog isLastWorkTimeOut success, data is: ${res}`);
9. }
10. });
```

## workScheduler.isLastWorkTimeOut

PhonePC/2in1TabletTVWearable

isLastWorkTimeOut(workId: number): Promise<boolean>

检查延迟任务的最后一次执行是否超时，使用Promise形式返回。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| workId | number | 是 | 指定延迟任务的Id。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示指定任务的最后一次执行超时，false表示未超时。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[workScheduler错误码](errorcode-workscheduler.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Parameter verification failed. |
| 9700001 | Memory operation failed. |
| 9700002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9700003 | System service operation failed. |
| 9700004 | Check on workInfo failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { workScheduler } from '@kit.BackgroundTasksKit';

4. workScheduler.isLastWorkTimeOut(500)
5. .then((res: boolean) => {
6. console.info(`workschedulerLog isLastWorkTimeOut success, data is: ${res}`);
7. })
8. .catch((error: BusinessError) =>  {
9. console.error(`workschedulerLog isLastWorkTimeOut failed. code is ${error.code} message is ${error.message}`);
10. });
```

## WorkInfo

PhonePC/2in1TabletTVWearable

延迟任务的具体信息, 用于设置延迟任务的触发条件等。

说明

WorkInfo参数设置时需遵循以下规则：

1. workId、bundleName、abilityName为必填项，bundleName需为本应用包名。
2. 携带参数信息仅支持number、string、boolean三种类型。
3. 至少设置一个满足的条件，包括网络类型、充电类型、存储状态、电池状态等。
4. 对于循环任务，任务执行间隔至少2小时。设置了循环任务时间间隔时，须同时设置是否循环或循环次数中的一个。
5. 对于可选参数，如果缺省表示延迟任务的触发不依赖该条件。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| workId | number | 否 | 否 | 延迟任务ID。 |
| bundleName | string | 否 | 否 | 延迟任务所在应用的包名。 |
| abilityName | string | 否 | 否 | 包内ability名称。 |
| networkType | [NetworkType](js-apis-resourceschedule-workscheduler.md#networktype) | 否 | 是 | 网络类型。 |
| isCharging | boolean | 否 | 是 | 是否充电，默认为false。  - true表示充电触发延迟任务回调。  - false表示不充电触发延迟任务回调。 |
| chargerType | [ChargingType](js-apis-resourceschedule-workscheduler.md#chargingtype) | 否 | 是 | 充电类型。 |
| batteryLevel | number | 否 | 是 | 电量。  取值范围：[0, 100] |
| batteryStatus | [BatteryStatus](js-apis-resourceschedule-workscheduler.md#batterystatus) | 否 | 是 | 电池状态。 |
| storageRequest | [StorageRequest](js-apis-resourceschedule-workscheduler.md#storagerequest) | 否 | 是 | 存储状态。 |
| isRepeat | boolean | 否 | 是 | 是否循环任务，默认为false。  - true表示循环任务。  - false表示非循环任务。 |
| repeatCycleTime | number | 否 | 是 | 循环间隔，单位：ms。 |
| repeatCount | number | 否 | 是 | 循环次数。 |
| isPersisted | boolean | 否 | 是 | 注册的延迟任务是否可保存在系统中，默认为false。  - true表示可保存，即系统重启后，任务可恢复。  - false表示不可保存。 |
| isDeepIdle | boolean | 否 | 是 | 是否要求设备进入空闲状态，默认为false。  - true表示需要。  - false表示不需要。 |
| idleWaitTime | number | 否 | 是 | 空闲等待时间，单位：ms。 |
| parameters | Record<string, number | string | boolean> | 否 | 是 | 携带参数信息。 |
| earliestStartTime22+ | number | 否 | 是 | 任务首次执行时间距离任务申请时间的间隔，单位：ms，默认为0，范围大于等于0。 |

## NetworkType

PhonePC/2in1TabletTVWearable

触发延迟任务回调的网络类型。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NETWORK\_TYPE\_ANY | 0 | 表示这个触发条件是任何类型的网络连接。 |
| NETWORK\_TYPE\_MOBILE | 1 | 表示这个触发条件是Mobile网络连接。 |
| NETWORK\_TYPE\_WIFI | 2 | 表示这个触发条件是Wifi类型的网络连接。 |
| NETWORK\_TYPE\_BLUETOOTH | 3 | 表示这个触发条件是Bluetooth网络连接。 |
| NETWORK\_TYPE\_WIFI\_P2P | 4 | 表示这个触发条件是Wifi P2P网络连接。 |
| NETWORK\_TYPE\_ETHERNET | 5 | 表示这个触发条件是有线网络连接。 |

## ChargingType

PhonePC/2in1TabletTVWearable

触发延迟任务回调的充电类型。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CHARGING\_PLUGGED\_ANY | 0 | 表示这个触发条件是任何类型的充电器连接。 |
| CHARGING\_PLUGGED\_AC | 1 | 表示这个触发条件是直流充电器连接。 |
| CHARGING\_PLUGGED\_USB | 2 | 表示这个触发条件是USB充电连接。 |
| CHARGING\_PLUGGED\_WIRELESS | 3 | 表示这个触发条件是无线充电器连接。 |

## BatteryStatus

PhonePC/2in1TabletTVWearable

触发延迟任务回调的电池状态。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BATTERY\_STATUS\_LOW | 0 | 表示这个触发条件是低电告警。 |
| BATTERY\_STATUS\_OKAY | 1 | 表示这个触发条件是从低电恢复到正常电量。 |
| BATTERY\_STATUS\_LOW\_OR\_OKAY | 2 | 表示这个触发条件是从低电恢复到正常电量或者低电告警。 |

## StorageRequest

PhonePC/2in1TabletTVWearable

触发延迟任务回调的存储状态。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STORAGE\_LEVEL\_LOW | 0 | 表示这个触发条件是存储空间不足。 |
| STORAGE\_LEVEL\_OKAY | 1 | 表示这个触发条件是从存储空间不足恢复到正常。 |
| STORAGE\_LEVEL\_LOW\_OR\_OKAY | 2 | 表示这个触发条件是存储空间不足或者从存储空间不足恢复到正常。 |
