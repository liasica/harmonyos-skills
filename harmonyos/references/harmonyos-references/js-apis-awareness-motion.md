---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-awareness-motion
title: @ohos.multimodalAwareness.motion (动作感知能力)
breadcrumb: API参考 > 系统 > 硬件 > Multimodal Awareness Kit（多模态融合感知服务） > ArkTS API > @ohos.multimodalAwareness.motion (动作感知能力)
category: harmonyos-references
scraped_at: 2026-04-28T08:10:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4f142f8e3ca3ebc22718cb5cf0b19e7677e8bf08e200bd6d204d09570353486b
---

本模块提供对用户动作的感知能力，包括用户的手势、动作等。

说明

本模块首批接口从API version 15开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

Phone

```
1. import { motion } from '@kit.MultimodalAwarenessKit';
```

## OperatingHandStatus

Phone

触控操作手状态信息。

**系统能力**：SystemCapability.MultimodalAwareness.Motion

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN\_STATUS | 0 | 表示未识别。 |
| LEFT\_HAND\_OPERATED | 1 | 表示触控操作手是左手。 |
| RIGHT\_HAND\_OPERATED | 2 | 表示触控操作手是右手。 |

## HoldingHandStatus20+

Phone

手机握持手状态信息，表示握持手状态变化感知事件的结果。订阅握持手状态变化感知事件后，返回当前握持手状态信息。

**系统能力**：SystemCapability.MultimodalAwareness.Motion

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOT\_HELD | 0 | 表示未握持。 |
| LEFT\_HAND\_HELD | 1 | 表示左手握持。 |
| RIGHT\_HAND\_HELD | 2 | 表示右手握持。 |
| BOTH\_HANDS\_HELD | 3 | 表示双手握持。 |
| UNKNOWN\_STATUS | 16 | 表示未识别。 |

## motion.on('operatingHandChanged')

Phone

on(type: 'operatingHandChanged', callback: Callback<OperatingHandStatus>): void

订阅触控操作手感知事件。

如果设备不支持此功能，将返回801错误码。

**需要权限**：ohos.permission.ACTIVITY\_MOTION 或 ohos.permission.DETECT\_GESTURE

**系统能力**：SystemCapability.MultimodalAwareness.Motion

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型。type为“operatingHandChanged”，表示操作手状态变化。 |
| callback | Callback<[OperatingHandStatus](js-apis-awareness-motion.md#operatinghandstatus)> | 是 | 回调函数，返回操作手结果。 |

**错误码**：

以下错误码的详细介绍请参见[动作感知错误码](errorcode-motion.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. An attempt was made to subscribe operatingHandChanged event forbidden by permission: ohos.permission.ACTIVITY\_MOTION or ohos.permission.DETECT\_GESTURE. |
| 401 | Parameter error. Parameter verification failed. |
| 801 | Capability not supported. Function can not work correctly due to limited device capabilities. |
| 31500001 | Service exception. Possible causes: 1. A system error, such as null pointer, container-related exception; 2. N-API invocation exception, invalid N-API status. |
| 31500002 | Subscription failed. Possible causes: 1. Callback registration failure; 2. Failed to bind native object to js wrapper; 3. N-API invocation exception, invalid N-API status; 4. IPC request exception. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let callback:Callback<motion.OperatingHandStatus> = (data:motion.OperatingHandStatus) => {
4. console.info('callback succeeded' + data);
5. };

7. try {
8. motion.on('operatingHandChanged', callback);
9. console.info("on succeeded");
10. } catch (err) {
11. let error = err as BusinessError;
12. console.error("Failed on and err code is " + error.code);
13. }
```

## motion.off('operatingHandChanged')

Phone

off(type: 'operatingHandChanged', callback?: Callback<OperatingHandStatus>): void

取消订阅触控操作手感知事件。

**需要权限**：ohos.permission.ACTIVITY\_MOTION 或 ohos.permission.DETECT\_GESTURE

**系统能力**：SystemCapability.MultimodalAwareness.Motion

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型。type为“operatingHandChanged”，表示操作手状态变化。 |
| callback | Callback<[OperatingHandStatus](js-apis-awareness-motion.md#operatinghandstatus)> | 否 | 回调函数，返回操作手结果。 |

**错误码**：

以下错误码的详细介绍请参见[动作感知错误码](errorcode-motion.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. An attempt was made to unsubscribe operatingHandChanged event forbidden by permission: ohos.permission.ACTIVITY\_MOTION or ohos.permission.DETECT\_GESTURE. |
| 401 | Parameter error. Parameter verification failed. |
| 801 | Capability not supported. Function can not work correctly due to limited device capabilities. |
| 31500001 | Service exception. Possible causes: 1. A system error, such as null pointer, container-related exception; 2. N-API invocation exception, invalid N-API status. |
| 31500003 | Unsubscription failed. Possible causes: 1. Callback failure; 2. N-API invocation exception, invalid N-API status; 3. IPC request exception. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. motion.off('operatingHandChanged');
5. console.info("off succeeded");
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error("Failed off and err code is " + error.code);
9. }
```

## motion.getRecentOperatingHandStatus()

Phone

getRecentOperatingHandStatus(): OperatingHandStatus

获取最新触控操作手状态。

**需要权限**：ohos.permission.ACTIVITY\_MOTION 或 ohos.permission.DETECT\_GESTURE

**系统能力**：SystemCapability.MultimodalAwareness.Motion

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [OperatingHandStatus](js-apis-awareness-motion.md#operatinghandstatus) | 返回触控操作手状态信息。 |

**错误码**：

以下错误码的详细介绍请参见[动作感知错误码](errorcode-motion.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. An attempt was made to get the recent operating hand status forbidden by permission: ohos.permission.ACTIVITY\_MOTION or ohos.permission.DETECT\_GESTURE. |
| 801 | Capability not supported. Function can not work correctly due to limited device capabilities. |
| 31500001 | Service exception. Possible causes: 1. A system error, such as null pointer, container-related exception; 2. N-API invocation exception, invalid N-API status. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let data:motion.OperatingHandStatus = motion.getRecentOperatingHandStatus();
5. console.info('get succeeded' + data);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error("Failed get and err code is " + error.code);
9. }
```

## motion.on('holdingHandChanged') 20+

Phone

on(type: 'holdingHandChanged', callback: Callback<HoldingHandStatus>): void

订阅握持手状态变化感知事件。

**需要权限**：ohos.permission.DETECT\_GESTURE

**系统能力**：SystemCapability.MultimodalAwareness.Motion

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，type为"holdingHandChanged"。 |
| callback | Callback<[HoldingHandStatus](js-apis-awareness-motion.md#holdinghandstatus20)> | 是 | 回调函数，返回握持手状态结果。 |

**错误码**

以下错误码的详细介绍请参见[动作感知错误码](errorcode-motion.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. An attempt was made to subscribe holdingHandChanged event forbidden by permission: ohos.permission.DETECT\_GESTURE. |
| 801 | Capability not supported. Function can not work correctly due to limited device capabilities. |
| 31500001 | Service exception. Possible causes: 1. A system error, such as null pointer, container-related exception; 2. N-API invocation exception, invalid N-API status. |
| 31500002 | Subscription failed. Possible causes: 1. Callback registration failure; 2. Failed to bind native object to js wrapper; 3. N-API invocation exception, invalid N-API status; 4. IPC request exception. |

**示例**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let callback:Callback<motion.HoldingHandStatus> = (data:motion.HoldingHandStatus) => {
4. console.info('callback succeeded: ' + data);
5. };

7. try {
8. motion.on('holdingHandChanged', callback);
9. console.info('on succeeded');
10. } catch (err) {
11. let error = err as BusinessError;
12. console.error('Failed on; err code = ' + error.code);
13. }
```

## motion.off('holdingHandChanged') 20+

Phone

off(type: 'holdingHandChanged', callback?: Callback<HoldingHandStatus>): void

取消订阅握持手状态变化感知事件。

**需要权限**：ohos.permission.DETECT\_GESTURE

**系统能力**：SystemCapability.MultimodalAwareness.Motion

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，type为"holdingHandChanged"。 |
| callback | Callback<[HoldingHandStatus](js-apis-awareness-motion.md#holdinghandstatus20)> | 否 | 需取消的回调函数。省略则移除该事件的所有回调。 |

**错误码**

以下错误码的详细介绍请参见[动作感知错误码](errorcode-motion.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. An attempt was made to unsubscribe holdingHandChanged event forbidden by permission: ohos.permission.DETECT\_GESTURE. |
| 801 | Capability not supported. Function can not work correctly due to limited device capabilities. |
| 31500001 | Service exception. Possible causes: 1. A system error, such as null pointer, container-related exception; 2. N-API invocation exception, invalid N-API status. |
| 31500003 | Unsubscription failed. Possible causes: 1. Callback failure; 2. N-API invocation exception, invalid N-API status; 3. IPC request exception. |

**示例**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. motion.off('holdingHandChanged'); // 移除所有同类订阅
5. console.info('off succeeded');
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error('Failed off; err code = ' + error.code);
9. }
```
