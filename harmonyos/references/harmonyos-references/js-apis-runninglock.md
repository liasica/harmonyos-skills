---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-runninglock
title: @ohos.runningLock (RunningLock锁)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 设备管理 > @ohos.runningLock (RunningLock锁)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dded4f289898f05354ba410a2083a3006fd599206633e241f43b4f160e6f7b3d
---

该模块为RunningLock锁相关操作的接口，提供使能接近光亮灭屏或者设备熄屏后阻止进入睡眠的能力，包括创建、查询、持锁、释放锁等操作，类型详情见[RunningLockType](js-apis-runninglock.md#runninglocktype)。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import {runningLock} from '@kit.BasicServicesKit';
```

## runningLock.isSupported9+

PhonePC/2in1TabletTVWearable

isSupported(type: RunningLockType): boolean

**方法介绍：** 查询系统是否支持该类型的锁。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [RunningLockType](js-apis-runninglock.md#runninglocktype) | 是 | 需要查询的锁的类型；该参数必须是一个枚举类。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示支持，返回false表示不支持。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**示例：**

```
1. try {
2. let isSupported = runningLock.isSupported(runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL);
3. console.info('BACKGROUND type supported: ' + isSupported);
4. } catch(err) {
5. console.error('check supported failed, err: ' + err);
6. }
```

## runningLock.create9+

PhonePC/2in1TabletTVWearable

create(name: string, type: RunningLockType, callback: AsyncCallback<RunningLock>): void

**方法介绍：** 创建RunningLock锁。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING\_LOCK

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 锁的名字；该参数必须为字符串类型。 |
| type | [RunningLockType](js-apis-runninglock.md#runninglocktype) | 是 | 要创建的锁的类型；该参数必须是一个枚举类。 |
| callback | AsyncCallback<[RunningLock](js-apis-runninglock.md#runninglock)> | 是 | 回调函数。当创建锁成功，err为undefined，data为创建的RunningLock；否则为错误对象；AsyncCallback封装了一个RunningLock类型的类。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Parameter verification failed. |
| 201 | If the permission is denied. |

**示例：**

```
1. runningLock.create('running_lock_test', runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL, (err: Error, lock: runningLock.RunningLock) => {
2. if (typeof err === 'undefined') {
3. console.info('created running lock: ' + lock);
4. } else {
5. console.error('create running lock failed, err: ' + err);
6. }
7. });
```

## runningLock.create9+

PhonePC/2in1TabletTVWearable

create(name: string, type: RunningLockType): Promise<RunningLock>

**方法介绍：** 创建RunningLock锁。使用Promise异步回调。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING\_LOCK

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 锁的名字；该参数必须为字符串类型。 |
| type | [RunningLockType](js-apis-runninglock.md#runninglocktype) | 是 | 要创建的锁的类型；该参数必须是一个枚举类。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[RunningLock](js-apis-runninglock.md#runninglock)> | Promise对象，返回RunningLock锁对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Parameter verification failed. |
| 201 | If the permission is denied. |

**示例：**

```
1. runningLock.create('running_lock_test', runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL)
2. .then((lock: runningLock.RunningLock) => {
3. console.info('created running lock: ' + lock);
4. })
5. .catch((err: Error) => {
6. console.error('create running lock failed, err: ' + err);
7. });
```

## runningLock.isRunningLockTypeSupported(deprecated)

PhonePC/2in1TabletTVWearable

isRunningLockTypeSupported(type: RunningLockType, callback: AsyncCallback<boolean>): void

说明

从API version 7开始支持，从API version 9开始不再维护，建议使用[runningLock.isSupported](js-apis-runninglock.md#runninglockissupported9)替代。

**方法介绍：** 查询系统是否支持该类型的锁。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [RunningLockType](js-apis-runninglock.md#runninglocktype) | 是 | 需要查询的锁的类型。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当查询成功，err为undefined，data为获取到的支持情况，返回true表示支持，返回false表示不支持；否则为错误对象。 |

**示例：**

```
1. runningLock.isRunningLockTypeSupported(runningLock.RunningLockType.BACKGROUND, (err: Error, data: boolean) => {
2. if (typeof err === 'undefined') {
3. console.info('BACKGROUND lock support status: ' + data);
4. } else {
5. console.error('check BACKGROUND lock support status failed, err: ' + err);
6. }
7. });
```

## runningLock.isRunningLockTypeSupported(deprecated)

PhonePC/2in1TabletTVWearable

isRunningLockTypeSupported(type: RunningLockType): Promise<boolean>

说明

从API version 7开始支持，从API version 9开始不再维护，建议使用[runningLock.isSupported](js-apis-runninglock.md#runninglockissupported9)替代。

**方法介绍：** 查询系统是否支持该类型的锁。使用Promise异步回调。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [RunningLockType](js-apis-runninglock.md#runninglocktype) | 是 | 需要查询的锁的类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示支持；返回false表示不支持。 |

**示例：**

```
1. runningLock.isRunningLockTypeSupported(runningLock.RunningLockType.BACKGROUND)
2. .then((data: boolean) => {
3. console.info('BACKGROUND lock support status: ' + data);
4. })
5. .catch((err: Error) => {
6. console.error('check BACKGROUND lock support status failed, err: ' + err);
7. });
```

## runningLock.createRunningLock(deprecated)

PhonePC/2in1TabletTVWearable

createRunningLock(name: string, type: RunningLockType, callback: AsyncCallback<RunningLock>): void

说明

从API version 7开始支持，从API version 9开始不再维护，建议使用[runningLock.create](js-apis-runninglock.md#runninglockcreate9)替代。

**方法介绍：** 创建RunningLock锁。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING\_LOCK

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 锁的名字。 |
| type | [RunningLockType](js-apis-runninglock.md#runninglocktype) | 是 | 要创建的锁的类型。 |
| callback | AsyncCallback<[RunningLock](js-apis-runninglock.md#runninglock)> | 是 | 回调函数。当创建锁成功，err为undefined，data为创建的RunningLock；否则为错误对象。 |

**示例：**

```
1. runningLock.createRunningLock('running_lock_test', runningLock.RunningLockType.BACKGROUND, (err: Error, lock: runningLock.RunningLock) => {
2. if (typeof err === 'undefined') {
3. console.info('created running lock: ' + lock);
4. } else {
5. console.error('create running lock failed, err: ' + err);
6. }
7. });
```

## runningLock.createRunningLock(deprecated)

PhonePC/2in1TabletTVWearable

createRunningLock(name: string, type: RunningLockType): Promise<RunningLock>

说明

从API version 7开始支持，从API version 9开始不再维护，建议使用[runningLock.create](js-apis-runninglock.md#runninglockcreate9)替代。

**方法介绍：** 创建RunningLock锁。使用Promise异步回调。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING\_LOCK

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 锁的名字。 |
| type | [RunningLockType](js-apis-runninglock.md#runninglocktype) | 是 | 要创建的锁的类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[RunningLock](js-apis-runninglock.md#runninglock)> | Promise对象，返回RunningLock锁对象。 |

**示例：**

```
1. runningLock.createRunningLock('running_lock_test', runningLock.RunningLockType.BACKGROUND)
2. .then((lock: runningLock.RunningLock) => {
3. console.info('created running lock: ' + lock);
4. })
5. .catch((err: Error) => {
6. console.error('create running lock failed, err: ' + err);
7. });
```

## RunningLock

PhonePC/2in1TabletTVWearable

阻止系统睡眠的锁。

### hold9+

PhonePC/2in1TabletTVWearable

hold(timeout: number): void

**方法介绍：** 锁定和持有RunningLock。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING\_LOCK

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeout | number | 是 | 锁定和持有RunningLock的时长，单位：毫秒。  该参数必须为数字类型：  **-1**：永久持锁，需要主动释放。  **0**：默认3s后超时释放。  **>0**：按传入值超时释放。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 201 | If the permission is denied. |

**示例：**

```
1. // RunningLockTest.ets
2. class RunningLockTest {
3. public static recordLock: runningLock.RunningLock;

5. public static holdRunningLock(): void {
6. if (RunningLockTest.recordLock) {
7. RunningLockTest.recordLock.hold(500);
8. console.info('hold running lock success');
9. } else {
10. runningLock.create('running_lock_test', runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL, (err: Error, lock: runningLock.RunningLock) => {
11. if (typeof err === 'undefined') {
12. console.info('create running lock: ' + lock);
13. RunningLockTest.recordLock = lock;
14. try {
15. lock.hold(500);
16. console.info('hold running lock success');
17. } catch(err) {
18. console.error('hold running lock failed, err: ' + err);
19. }
20. } else {
21. console.error('create running lock failed, err: ' + err);
22. }
23. });
24. }
25. }
26. }
```

### unhold9+

PhonePC/2in1TabletTVWearable

unhold(): void

**方法介绍：** 释放RunningLock锁。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING\_LOCK

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | If the permission is denied. |

**示例：**

```
1. // RunningLockTest.ets
2. class RunningLockTest {
3. public static recordLock: runningLock.RunningLock;

5. public static unholdRunningLock(): void {
6. if (RunningLockTest.recordLock) {
7. RunningLockTest.recordLock.unhold();
8. console.info('unhold running lock success');
9. } else {
10. runningLock.create('running_lock_test', runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL, (err: Error, lock: runningLock.RunningLock) => {
11. if (typeof err === 'undefined') {
12. console.info('create running lock: ' + lock);
13. RunningLockTest.recordLock = lock;
14. try {
15. lock.unhold();
16. console.info('unhold running lock success');
17. } catch(err) {
18. console.error('unhold running lock failed, err: ' + err);
19. }
20. } else {
21. console.error('create running lock failed, err: ' + err);
22. }
23. });
24. }
25. }
26. }
```

### isHolding9+

PhonePC/2in1TabletTVWearable

isHolding(): boolean

**方法介绍：** 查询当前RunningLock是持有状态还是释放状态。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示当前RunningLock是持有状态，返回false表示当前RunningLock是释放状态。 |

**示例：**

```
1. // RunningLockTest.ets
2. class RunningLockTest {
3. public static recordLock: runningLock.RunningLock;

5. public static isHoldingRunningLock(): void {
6. if (RunningLockTest.recordLock) {
7. let isHolding = RunningLockTest.recordLock.isHolding();
8. console.info('check running lock holding status: ' + isHolding);
9. } else {
10. runningLock.create('running_lock_test', runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL, (err: Error, lock: runningLock.RunningLock) => {
11. if (typeof err === 'undefined') {
12. console.info('create running lock: ' + lock);
13. RunningLockTest.recordLock = lock;
14. let isHolding = lock.isHolding();
15. console.info('check running lock holding status: ' + isHolding);
16. } else {
17. console.error('create running lock failed, err: ' + err);
18. }
19. });
20. }
21. }
22. }
```

### lock(deprecated)

PhonePC/2in1TabletTVWearable

lock(timeout: number): void

说明

从API version 7开始支持，从API version 9开始不再维护，建议使用[RunningLock.hold](js-apis-runninglock.md#hold9)替代。

**方法介绍：** 锁定和持有RunningLock。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING\_LOCK

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeout | number | 是 | 锁定和持有RunningLock的时长，单位：毫秒。 |

**示例：**

```
1. runningLock.createRunningLock('running_lock_test', runningLock.RunningLockType.BACKGROUND)
2. .then((lock: runningLock.RunningLock) => {
3. lock.lock(500);
4. console.info('create running lock and lock success');
5. })
6. .catch((err: Error) => {
7. console.error('create running lock failed, err: ' + err);
8. });
```

### unlock(deprecated)

PhonePC/2in1TabletTVWearable

unlock(): void

说明

从API version 7开始支持，从API version 9开始不再维护，建议使用[RunningLock.unhold](js-apis-runninglock.md#unhold9)替代。

**方法介绍：** 释放RunningLock锁。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING\_LOCK

**示例：**

```
1. runningLock.createRunningLock('running_lock_test', runningLock.RunningLockType.BACKGROUND)
2. .then((lock: runningLock.RunningLock) => {
3. lock.unlock();
4. console.info('create running lock and unlock success');
5. })
6. .catch((err: Error) => {
7. console.error('create running lock failed, err: ' + err);
8. });
```

### isUsed(deprecated)

PhonePC/2in1TabletTVWearable

isUsed(): boolean

说明

从API version 7开始支持，从API version 9开始不再维护，建议使用[RunningLock.isHolding](js-apis-runninglock.md#isholding9)替代。

**方法介绍：** 查询当前RunningLock是持有状态还是释放状态。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示当前RunningLock是持有状态，返回false表示当前RunningLock是释放状态。 |

**示例：**

```
1. runningLock.createRunningLock('running_lock_test', runningLock.RunningLockType.BACKGROUND)
2. .then((lock: runningLock.RunningLock) => {
3. let isUsed = lock.isUsed();
4. console.info('check running lock used status: ' + isUsed);
5. })
6. .catch((err: Error) => {
7. console.error('check running lock used status failed, err: ' + err);
8. });
```

## RunningLockType

PhonePC/2in1TabletTVWearable

RunningLock锁的类型。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BACKGROUND(deprecated) | 1 | 阻止系统睡眠的锁。  **说明：** 从API version 7开始支持，从API version 10开始废弃。 |
| PROXIMITY\_SCREEN\_CONTROL | 2 | 接近光锁，使能接近光传感器，并根据传感器与障碍物的距离远近发起亮灭屏流程。 |
| BACKGROUND\_USER\_IDLE23+ | 129 | 阻止系统自动睡眠的后台闲时任务锁，持锁能保证一段时间用户不活动后系统不进入自动睡眠。注意：不能阻止如PC合盖等场景系统进入强制睡眠，使用方必须监听[进入强制睡眠公共事件](commoneventmanager-definitions.md#common_event_enter_force_sleep12)，监听到事件后释放该锁。该类型锁行为存在设备差异，使用该类型锁请参考[阻止系统闲时进入睡眠开发指南](../harmonyos-guides/runninglock-dev.md)。 |
