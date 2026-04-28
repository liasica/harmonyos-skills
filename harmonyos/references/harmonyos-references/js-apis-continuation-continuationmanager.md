---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationmanager
title: @ohos.continuation.continuationManager (流转/协同管理)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.continuation.continuationManager (流转/协同管理)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:cc07db8e6aac078ae4aa43cf6b27c2854f7a554e9772bb00a5e835d4f4b941c3
---

continuationManager模块提供了流转/协同入口管理服务能力，包括连接/取消流转管理服务，注册/解注册设备连接变化监听，拉起设备选择模块，更新连接状态。

说明

本模块首批接口从API version 8开始支持，从API version 22开始废弃，建议使用[分布式设备管理](js-apis-distributeddevicemanager.md)替代。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { continuationManager } from '@kit.AbilityKit';
```

## continuationManager.register(deprecated)

PhonePC/2in1TabletTV

register(callback: AsyncCallback<number>): void

注册流转管理服务，并获取对应的注册token，无过滤条件，使用AsyncCallback方式作为异步方法。

说明

从API version 9开始废弃，建议使用[ondevicestatechange](js-apis-distributeddevicemanager.md#ondevicestatechange)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | AsyncCallback形式返回流转管理服务连接后生成的token。 |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';

3. let token: number = -1;
4. continuationManager.register((err, data) => {
5. if (err.code != 0) {
6. console.error('register failed, cause: ' + JSON.stringify(err));
7. return;
8. }
9. console.info('register finished, ' + JSON.stringify(data));
10. token = data;
11. });
```

## continuationManager.register(deprecated)

PhonePC/2in1TabletTV

register(options: ContinuationExtraParams, callback: AsyncCallback<number>): void

连接流转管理服务，并获取对应的注册token，使用AsyncCallback方式作为异步方法。

说明

从API version 9开始废弃，建议使用[onDeviceStateChange](js-apis-distributeddevicemanager.md#ondevicestatechange)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ContinuationExtraParams](js-apis-continuation-continuationextraparams.md) | 是 | 过滤可选择设备列表的额外参数。 |
| callback | AsyncCallback<number> | 是 | AsyncCallback形式返回流转管理服务连接后生成的token。 |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';

3. let token: number = -1;
4. continuationManager.register(
5. {
6. deviceType: ["00E"]
7. },
8. (err, data) => {
9. if (err.code != 0) {
10. console.error('register failed, cause: ' + JSON.stringify(err));
11. return;
12. }
13. console.info('register finished, ' + JSON.stringify(data));
14. token = data;
15. });
```

## continuationManager.register(deprecated)

PhonePC/2in1TabletTV

register(options?: ContinuationExtraParams): Promise<number>

连接流转管理服务，并获取对应的注册token，使用Promise方式作为异步方法。

说明

从API version 9开始废弃，建议使用[onDeviceStateChange](js-apis-distributeddevicemanager.md#ondevicestatechange)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ContinuationExtraParams](js-apis-continuation-continuationextraparams.md) | 否 | 过滤可选择设备列表的额外参数，该参数可缺省。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise形式返回流转管理服务连接后生成的token。 |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let token: number = -1;
5. continuationManager.register(
6. { deviceType: ["00E"] }).then((data) => {
7. console.info('register finished, ' + JSON.stringify(data));
8. token = data;
9. }).catch((err: BusinessError) => {
10. console.error('register failed, cause: ' + JSON.stringify(err));
11. });
```

## continuationManager.registerContinuation(deprecated)

PhonePC/2in1TabletTV

registerContinuation(callback: AsyncCallback<number>): void

注册流转管理服务，并获取对应的注册token，无过滤条件，使用AsyncCallback方式作为异步方法。

说明

从API version 9开始支持，从API version 22开始废弃，建议使用[onDeviceStateChange](js-apis-distributeddevicemanager.md#ondevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | AsyncCallback形式返回流转管理服务连接后生成的token。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DistributedSchedule错误码](errorcode-distributedschedule.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600003 | The number of token registration times has reached the upper limit. |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';

3. let token: number = -1;
4. try {
5. continuationManager.registerContinuation((err, data) => {
6. if (err.code != 0) {
7. console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
8. return;
9. }
10. console.info('registerContinuation finished, ' + JSON.stringify(data));
11. token = data;
12. });
13. } catch (err) {
14. console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
15. }
```

## continuationManager.registerContinuation(deprecated)

PhonePC/2in1TabletTV

registerContinuation(options: ContinuationExtraParams, callback: AsyncCallback<number>): void

连接流转管理服务，并获取对应的注册token，使用AsyncCallback方式作为异步方法。

说明

从API version 9开始支持，从API version 22开始废弃，建议使用[onDeviceStateChange](js-apis-distributeddevicemanager.md#ondevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ContinuationExtraParams](js-apis-continuation-continuationextraparams.md) | 是 | 过滤可选择设备列表的额外参数。 |
| callback | AsyncCallback<number> | 是 | AsyncCallback形式返回流转管理服务连接后生成的token。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DistributedSchedule错误码](errorcode-distributedschedule.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600003 | The number of token registration times has reached the upper limit. |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';

3. let token: number = -1;
4. try {
5. continuationManager.registerContinuation(
6. {
7. deviceType: ["00E"]
8. },
9. (err, data) => {
10. if (err.code != 0) {
11. console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
12. return;
13. }
14. console.info('registerContinuation finished, ' + JSON.stringify(data));
15. token = data;
16. });
17. } catch (err) {
18. console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
19. }
```

## continuationManager.registerContinuation(deprecated)

PhonePC/2in1TabletTV

registerContinuation(options?: ContinuationExtraParams): Promise<number>

连接流转管理服务，并获取对应的注册token，使用Promise方式作为异步方法。

说明

从API version 9开始支持，从API version 22开始废弃，建议使用[onDeviceStateChange](js-apis-distributeddevicemanager.md#ondevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ContinuationExtraParams](js-apis-continuation-continuationextraparams.md) | 否 | 过滤可选择设备列表的额外参数，该参数可缺省。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise形式返回流转管理服务连接后生成的token。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DistributedSchedule错误码](errorcode-distributedschedule.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600003 | The number of token registration times has reached the upper limit. |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let token: number = -1;
5. try {
6. continuationManager.registerContinuation(
7. {
8. deviceType: ["00E"]
9. }).then((data) => {
10. console.info('registerContinuation finished, ' + JSON.stringify(data));
11. token = data;
12. }).catch((err: BusinessError) => {
13. console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
14. });
15. } catch (err) {
16. console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
17. }
```

## continuationManager.on('deviceConnect')(deprecated)

PhonePC/2in1TabletTV

on(type: 'deviceConnect', callback: Callback<ContinuationResult>): void

异步方法，监听设备连接状态，使用Callback形式返回连接的设备信息。

说明

从API version 9开始废弃，建议使用[onDeviceStateChange](js-apis-distributeddevicemanager.md#ondevicestatechange)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，固定值"deviceConnect"。 |
| callback | Callback<[ContinuationResult](js-apis-continuation-continuationresult.md)> | 是 | 当用户从设备选择模块中选择设备时调用，返回设备ID、设备类型和设备名称供开发者使用。 |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';

3. continuationManager.on("deviceConnect", (data) => {
4. console.info('onDeviceConnect deviceId: ' + JSON.stringify(data.id));
5. console.info('onDeviceConnect deviceType: ' + JSON.stringify(data.type));
6. console.info('onDeviceConnect deviceName: ' + JSON.stringify(data.name));
7. });
```

## continuationManager.on('deviceDisconnect')(deprecated)

PhonePC/2in1TabletTV

on(type: 'deviceDisconnect', callback: Callback<string>): void

异步方法，监听设备断开状态，使用Callback形式返回断开的设备信息。

说明

从API version 9开始废弃，建议使用[onDeviceStateChange](js-apis-distributeddevicemanager.md#ondevicestatechange)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，固定值"deviceDisconnect"。 |
| callback | Callback<string> | 是 | 当用户从设备选择模块中断开设备时调用，返回设备ID供开发者使用。 |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';

3. continuationManager.on("deviceDisconnect", (data) => {
4. console.info('onDeviceDisconnect deviceId: ' + JSON.stringify(data));
5. });
```

## continuationManager.off('deviceConnect')(deprecated)

PhonePC/2in1TabletTV

off(type: 'deviceConnect', callback?: Callback<ContinuationResult>): void

异步方法，取消监听设备连接状态，使用Callback形式返回连接的设备信息。

说明

从API version 9开始废弃，建议使用[offDeviceStateChange](js-apis-distributeddevicemanager.md#offdevicestatechange)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听的事件类型，固定值"deviceConnect"。 |
| callback | Callback<[ContinuationResult](js-apis-continuation-continuationresult.md)> | 否 | 当用户从设备选择模块中选择设备时调用，返回设备ID、设备类型和设备名称供开发者使用。 |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';

3. continuationManager.off("deviceConnect", (data) => {
4. console.info('onDeviceConnect deviceId: ' + JSON.stringify(data.id));
5. console.info('onDeviceConnect deviceType: ' + JSON.stringify(data.type));
6. console.info('onDeviceConnect deviceName: ' + JSON.stringify(data.name));
7. });
```

## continuationManager.off('deviceDisconnect')(deprecated)

PhonePC/2in1TabletTV

off(type: 'deviceDisconnect', callback?: Callback<string>): void

异步方法，取消监听设备断开状态，使用Callback形式返回连接的设备信息。

说明

从API version 9开始废弃，建议使用[offDeviceStateChange](js-apis-distributeddevicemanager.md#offdevicestatechange)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听的事件类型，固定值"deviceDisconnect"。 |
| callback | Callback<string> | 否 | 当用户从设备选择模块中断开设备时调用，返回设备ID供开发者使用。 |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';

3. continuationManager.off("deviceDisconnect", (data) => {
4. console.info('onDeviceDisconnect deviceId: ' + JSON.stringify(data));
5. });
```

## continuationManager.on('deviceSelected')(deprecated)

PhonePC/2in1TabletTV

on(type: 'deviceSelected', token: number, callback: Callback<Array<ContinuationResult>>): void

异步方法，监听设备连接状态，使用Callback形式返回连接的设备信息。

说明

从API version 9开始支持，从API version 22开始废弃，建议使用[onDeviceStateChange](js-apis-distributeddevicemanager.md#ondevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，固定值"deviceSelected"。 |
| token | number | 是 | 注册后的token。 |
| callback | Callback<Array<[ContinuationResult](js-apis-continuation-continuationresult.md)>> | 是 | 当用户从设备选择模块中选择设备时调用，返回设备ID、设备类型和设备名称供开发者使用。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DistributedSchedule错误码](errorcode-distributedschedule.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |
| 16600004 | The specified callback has been registered. |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';

3. let token: number = 1;
4. try {
5. continuationManager.on("deviceSelected", token, (data) => {
6. console.info('onDeviceSelected len: ' + data.length);
7. for (let i = 0; i < data.length; i++) {
8. console.info('onDeviceSelected deviceId: ' + JSON.stringify(data[i].id));
9. console.info('onDeviceSelected deviceType: ' + JSON.stringify(data[i].type));
10. console.info('onDeviceSelected deviceName: ' + JSON.stringify(data[i].name));
11. }
12. });
13. } catch (err) {
14. console.error('on failed, cause: ' + JSON.stringify(err));
15. }
```

## continuationManager.on('deviceUnselected')(deprecated)

PhonePC/2in1TabletTV

on(type: 'deviceUnselected', token: number, callback: Callback<Array<ContinuationResult>>): void

异步方法，监听设备断开状态，使用Callback形式返回断开的设备信息。

说明

从API version 9开始支持，从API version 22开始废弃，建议使用[onDeviceStateChange](js-apis-distributeddevicemanager.md#ondevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，固定值"deviceUnselected"。 |
| token | number | 是 | 注册后的token。 |
| callback | Callback<Array<[ContinuationResult](js-apis-continuation-continuationresult.md)>> | 是 | 当用户从设备选择模块中断开设备时调用，返回设备ID、设备类型和设备名称供开发者使用。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DistributedSchedule错误码](errorcode-distributedschedule.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |
| 16600004 | The specified callback has been registered. |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';

3. let token: number = 1;
4. try {
5. continuationManager.on("deviceUnselected", token, (data) => {
6. console.info('onDeviceUnselected len: ' + data.length);
7. for (let i = 0; i < data.length; i++) {
8. console.info('onDeviceUnselected deviceId: ' + JSON.stringify(data[i].id));
9. console.info('onDeviceUnselected deviceType: ' + JSON.stringify(data[i].type));
10. console.info('onDeviceUnselected deviceName: ' + JSON.stringify(data[i].name));
11. }
12. console.info('onDeviceUnselected finished.');
13. });
14. } catch (err) {
15. console.error('on failed, cause: ' + JSON.stringify(err));
16. }
```

## continuationManager.off('deviceSelected')(deprecated)

PhonePC/2in1TabletTV

off(type: 'deviceSelected', token: number): void

取消监听设备连接状态。

说明

从API version 9开始支持，从API version 22开始废弃，建议使用[offDeviceStateChange](js-apis-distributeddevicemanager.md#offdevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听的事件类型，固定值"deviceSelected"。 |
| token | number | 是 | 注册后的token。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DistributedSchedule错误码](errorcode-distributedschedule.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |
| 16600004 | The specified callback has been registered. |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';

3. let token: number = 1;
4. try {
5. continuationManager.off("deviceSelected", token);
6. } catch (err) {
7. console.error('off failed, cause: ' + JSON.stringify(err));
8. }
```

## continuationManager.off('deviceUnselected')(deprecated)

PhonePC/2in1TabletTV

off(type: 'deviceUnselected', token: number): void

取消监听设备断开状态。

说明

从API version 9开始支持，从API version 22开始废弃，建议使用[offDeviceStateChange](js-apis-distributeddevicemanager.md#offdevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听的事件类型，固定值"deviceUnselected"。 |
| token | number | 是 | 注册后的token。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DistributedSchedule错误码](errorcode-distributedschedule.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |
| 16600004 | The specified callback has been registered. |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';

3. let token: number = 1;
4. try {
5. continuationManager.off("deviceUnselected", token);
6. } catch (err) {
7. console.error('off failed, cause: ' + JSON.stringify(err));
8. }
```

## continuationManager.startDeviceManager(deprecated)

PhonePC/2in1TabletTV

startDeviceManager(token: number, callback: AsyncCallback<void>): void

拉起设备选择模块，可显示组网内可选择设备列表信息，无过滤条件，使用AsyncCallback方式作为异步方法。

说明

从API version 9开始废弃，建议使用[startDiscovering](js-apis-distributeddevicemanager.md#startdiscovering)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当模块选择完成，err为undefined，否则返回错误对象。 |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';

3. let token: number = 1;
4. continuationManager.startDeviceManager(token, (err) => {
5. if (err.code != 0) {
6. console.error('startDeviceManager failed, cause: ' + JSON.stringify(err));
7. return;
8. }
9. console.info('startDeviceManager finished. ');
10. });
```

## continuationManager.startDeviceManager(deprecated)

PhonePC/2in1TabletTV

startDeviceManager(token: number, options: ContinuationExtraParams, callback: AsyncCallback<void>): void

拉起设备选择模块，可显示组网内可选择设备列表信息，使用AsyncCallback方式作为异步方法。

说明

从API version 9开始废弃，建议使用[startDiscovering](js-apis-distributeddevicemanager.md#startdiscovering)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| options | [ContinuationExtraParams](js-apis-continuation-continuationextraparams.md) | 是 | 过滤可选择设备列表的额外参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当模块选择完成，err为undefined，否则返回错误对象。 |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';

3. let token: number = 1;
4. continuationManager.startDeviceManager(
5. token,
6. {
7. deviceType: ["00E"]
8. },
9. (err) => {
10. if (err.code != 0) {
11. console.error('startDeviceManager failed, cause: ' + JSON.stringify(err));
12. return;
13. }
14. console.info('startDeviceManager finished. ');
15. });
```

## continuationManager.startDeviceManager(deprecated)

PhonePC/2in1TabletTV

startDeviceManager(token: number, options?: ContinuationExtraParams): Promise<void>

拉起设备选择模块，可显示组网内可选择设备列表信息，使用Promise方式作为异步方法。

说明

从API version 9开始废弃，建议使用[startDiscovering](js-apis-distributeddevicemanager.md#startdiscovering)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| options | [ContinuationExtraParams](js-apis-continuation-continuationextraparams.md) | 否 | 过滤可选择设备列表的额外参数，该参数可缺省。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise形式返回接口调用结果。 |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let token: number = -1;
5. continuationManager.startDeviceManager(
6. token,
7. {
8. deviceType: ["00E"]
9. }).then(() => {
10. console.info('startDeviceManager finished. ');
11. }).catch((err: BusinessError) => {
12. console.error('startDeviceManager failed, cause: ' + JSON.stringify(err));
13. });
```

## continuationManager.startContinuationDeviceManager(deprecated)

PhonePC/2in1TabletTV

startContinuationDeviceManager(token: number, callback: AsyncCallback<void>): void

拉起设备选择模块，可显示组网内可选择设备列表信息，无过滤条件，使用AsyncCallback方式作为异步方法。

说明

从API version 9开始支持，从API version 22开始废弃，建议使用[startDiscovering](js-apis-distributeddevicemanager.md#startdiscovering)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当模块选择完成，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DistributedSchedule错误码](errorcode-distributedschedule.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';

3. let token: number = -1;
4. try {
5. continuationManager.startContinuationDeviceManager(token, (err) => {
6. if (err.code != 0) {
7. console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
8. return;
9. }
10. console.info('startContinuationDeviceManager finished. ');
11. });
12. } catch (err) {
13. console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
14. }
```

## continuationManager.startContinuationDeviceManager(deprecated)

PhonePC/2in1TabletTV

startContinuationDeviceManager(token: number, options: ContinuationExtraParams, callback: AsyncCallback<void>): void

拉起设备选择模块，可显示组网内可选择设备列表信息，使用AsyncCallback方式作为异步方法。

说明

从API version 9开始支持，从API version 22开始废弃，建议使用[startDiscovering](js-apis-distributeddevicemanager.md#startdiscovering)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| options | [ContinuationExtraParams](js-apis-continuation-continuationextraparams.md) | 是 | 过滤可选择设备列表的额外参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当模块选择完成，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DistributedSchedule错误码](errorcode-distributedschedule.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';

3. let token: number = -1;
4. try {
5. continuationManager.startContinuationDeviceManager(
6. token,
7. {
8. deviceType: ["00E"]
9. },
10. (err) => {
11. if (err.code != 0) {
12. console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
13. return;
14. }
15. console.info('startContinuationDeviceManager finished. ');
16. });
17. } catch (err) {
18. console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
19. }
```

## continuationManager.startContinuationDeviceManager(deprecated)

PhonePC/2in1TabletTV

startContinuationDeviceManager(token: number, options?: ContinuationExtraParams): Promise<void>

拉起设备选择模块，可显示组网内可选择设备列表信息，使用Promise方式作为异步方法。

说明

从API version 9开始支持，从API version 22开始废弃，建议使用[startDiscovering](js-apis-distributeddevicemanager.md#startdiscovering)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| options | [ContinuationExtraParams](js-apis-continuation-continuationextraparams.md) | 否 | 过滤可选择设备列表的额外参数，该参数可缺省。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise形式返回接口调用结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DistributedSchedule错误码](errorcode-distributedschedule.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let token: number = -1;
5. try {
6. continuationManager.startContinuationDeviceManager(
7. token,
8. {
9. deviceType: ["00E"]
10. }).then(() => {
11. console.info('startContinuationDeviceManager finished. ');
12. }).catch((err: BusinessError) => {
13. console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
14. });
15. } catch (err) {
16. console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
17. }
```

## continuationManager.updateConnectStatus(deprecated)

PhonePC/2in1TabletTV

updateConnectStatus(token: number, deviceId: string, status: DeviceConnectState, callback: AsyncCallback<void>): void

通知设备选择模块，更新当前的连接状态，使用AsyncCallback方式作为异步方法。

说明

从API version 9开始废弃，建议使用[getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| deviceId | string | 是 | 设备ID。 |
| status | [DeviceConnectState](js-apis-continuation-continuationmanager.md#deviceconnectstatedeprecated) | 是 | 设备连接状态。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当通知设备成功，err为undefined，否则返回错误对象。 |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';

3. let token: number = -1;
4. let deviceId: string = "test deviceId";
5. continuationManager.updateConnectStatus(token, deviceId, continuationManager.DeviceConnectState.CONNECTED, (err) => {
6. if (err.code != 0) {
7. console.error('updateConnectStatus failed, cause: ' + JSON.stringify(err));
8. return;
9. }
10. console.info('updateConnectStatus finished. ');
11. });
```

## continuationManager.updateConnectStatus(deprecated)

PhonePC/2in1TabletTV

updateConnectStatus(token: number, deviceId: string, status: DeviceConnectState): Promise<void>

通知设备选择模块，更新当前的连接状态，使用Promise方式作为异步方法。

说明

从API version 9开始废弃，建议使用[getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| deviceId | string | 是 | 设备ID。 |
| status | [DeviceConnectState](js-apis-continuation-continuationmanager.md#deviceconnectstatedeprecated) | 是 | 设备连接状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise形式返回接口调用结果。 |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let token: number = 1;
5. let deviceId: string = "test deviceId";
6. continuationManager.updateConnectStatus(token, deviceId, continuationManager.DeviceConnectState.CONNECTED)
7. .then(() => {
8. console.info('updateConnectStatus finished. ');
9. })
10. .catch((err: BusinessError) => {
11. console.error('updateConnectStatus failed, cause: ' + JSON.stringify(err));
12. });
```

## continuationManager.updateContinuationState(deprecated)

PhonePC/2in1TabletTV

updateContinuationState(token: number, deviceId: string, status: DeviceConnectState, callback: AsyncCallback<void>): void

通知设备选择模块，更新当前的连接状态，使用AsyncCallback方式作为异步方法。

说明

从API version 9开始支持，从API version 22开始废弃，建议使用[getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| deviceId | string | 是 | 设备ID。 |
| status | [DeviceConnectState](js-apis-continuation-continuationmanager.md#deviceconnectstatedeprecated) | 是 | 设备连接状态。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当通知设备成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DistributedSchedule错误码](errorcode-distributedschedule.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';

3. let token: number = 1;
4. let deviceId: string = "test deviceId";
5. try {
6. continuationManager.updateContinuationState(token, deviceId, continuationManager.DeviceConnectState.CONNECTED, (err) => {
7. if (err.code != 0) {
8. console.error('updateContinuationState failed, cause: ' + JSON.stringify(err));
9. return;
10. }
11. console.info('updateContinuationState finished. ');
12. });
13. } catch (err) {
14. console.error('updateContinuationState failed, cause: ' + JSON.stringify(err));
15. }
```

## continuationManager.updateContinuationState(deprecated)

PhonePC/2in1TabletTV

updateContinuationState(token: number, deviceId: string, status: DeviceConnectState): Promise<void>

通知设备选择模块，更新当前的连接状态，使用Promise方式作为异步方法。

说明

从API version 9开始支持，从API version 22开始废弃，建议使用[getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| deviceId | string | 是 | 设备ID。 |
| status | [DeviceConnectState](js-apis-continuation-continuationmanager.md#deviceconnectstatedeprecated) | 是 | 设备连接状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise形式返回接口调用结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DistributedSchedule错误码](errorcode-distributedschedule.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let token: number = 1;
5. let deviceId: string = "test deviceId";
6. try {
7. continuationManager.updateContinuationState(token, deviceId, continuationManager.DeviceConnectState.CONNECTED)
8. .then(() => {
9. console.info('updateContinuationState finished. ');
10. })
11. .catch((err: BusinessError) => {
12. console.error('updateContinuationState failed, cause: ' + JSON.stringify(err));
13. });
14. } catch (err) {
15. console.error('updateContinuationState failed, cause: ' + JSON.stringify(err));
16. }
```

## continuationManager.unregister(deprecated)

PhonePC/2in1TabletTV

unregister(token: number, callback: AsyncCallback<void>): void

解注册流转管理服务，传入注册时获取的token进行解注册，使用AsyncCallback方式作为异步方法。

说明

从API version 9开始废弃，建议使用[offDeviceStateChange](js-apis-distributeddevicemanager.md#offdevicestatechange)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当解注册成功，err为undefined，否则返回错误对象。 |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';

3. let token: number = 1;
4. continuationManager.unregister(token, (err) => {
5. if (err.code != 0) {
6. console.error('unregister failed, cause: ' + JSON.stringify(err));
7. return;
8. }
9. console.info('unregister finished. ');
10. });
```

## continuationManager.unregister(deprecated)

PhonePC/2in1TabletTV

unregister(token: number): Promise<void>

解注册流转管理服务，传入注册时获取的token进行解注册，使用Promise方式作为异步方法。

说明

从API version 9开始废弃，建议使用[offDeviceStateChange](js-apis-distributeddevicemanager.md#offdevicestatechange)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise形式返回接口调用结果。 |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let token: number = 1;
5. continuationManager.unregister(token)
6. .then(() => {
7. console.info('unregister finished. ');
8. }).catch((err: BusinessError) => {
9. console.error('unregister failed, cause: ' + JSON.stringify(err));
10. });
```

## continuationManager.unregisterContinuation(deprecated)

PhonePC/2in1TabletTV

unregisterContinuation(token: number, callback: AsyncCallback<void>): void

解注册流转管理服务，传入注册时获取的token进行解注册，使用AsyncCallback方式作为异步方法。

说明

从API version 9开始支持，从API version 22开始废弃，建议使用[offDeviceStateChange](js-apis-distributeddevicemanager.md#offdevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当解注册成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DistributedSchedule错误码](errorcode-distributedschedule.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';

3. let token: number = 1;
4. try {
5. continuationManager.unregisterContinuation(token, (err) => {
6. if (err.code != 0) {
7. console.error('unregisterContinuation failed, cause: ' + JSON.stringify(err));
8. return;
9. }
10. console.info('unregisterContinuation finished. ');
11. });
12. } catch (err) {
13. console.error('unregisterContinuation failed, cause: ' + JSON.stringify(err));
14. }
```

## continuationManager.unregisterContinuation(deprecated)

PhonePC/2in1TabletTV

unregisterContinuation(token: number): Promise<void>

解注册流转管理服务，传入注册时获取的token进行解注册，使用Promise方式作为异步方法。

说明

从API version 9开始支持，从API version 22开始废弃，建议使用[offDeviceStateChange](js-apis-distributeddevicemanager.md#offdevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise形式返回接口调用结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DistributedSchedule错误码](errorcode-distributedschedule.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

**示例：**

```
1. import { continuationManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let token: number = -1;
5. try {
6. continuationManager.unregisterContinuation(token).then(() => {
7. console.info('unregisterContinuation finished. ');
8. }).catch((err: BusinessError) => {
9. console.error('unregisterContinuation failed, cause: ' + JSON.stringify(err));
10. });
11. } catch (err) {
12. console.error('unregisterContinuation failed, cause: ' + JSON.stringify(err));
13. }
```

## DeviceConnectState(deprecated)

PhonePC/2in1TabletTV

设备连接状态。

说明

从API version 22开始废弃，建议使用[DeviceStateChange](js-apis-distributeddevicemanager.md#devicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IDLE | 0 | 设备连接初始状态。 |
| CONNECTING | 1 | 设备连接中状态。 |
| CONNECTED | 2 | 设备已连接状态。 |
| DISCONNECTING | 3 | 设备断开连接状态。 |

## ContinuationMode(deprecated)

PhonePC/2in1TabletTV

设备选择模块连接模式。

说明

从API version 22开始废弃，建议使用[DeviceStateChange](js-apis-distributeddevicemanager.md#devicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COLLABORATION\_SINGLE | 0 | 设备选择模块单选模式。 |
| COLLABORATION\_MULTIPLE | 1 | 设备选择模块多选模式。 |

## ContinuationResult(deprecated)

PhonePC/2in1TabletTV

type ContinuationResult = \_ContinuationResult

流转管理入口返回的设备信息。

说明

从API version 10开始支持，从API version 22开始废弃，建议使用[DeviceBasicInfo](js-apis-distributeddevicemanager.md#devicebasicinfo)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

| 类型 | 说明 |
| --- | --- |
| [\_ContinuationResult](js-apis-continuation-continuationresult.md) | 表示流转管理入口返回的设备信息。 |

## ContinuationExtraParams(deprecated)

PhonePC/2in1TabletTV

type ContinuationExtraParams = \_ContinuationExtraParams

流转管理入口中设备选择模块所需的过滤参数。

说明

从API version 10开始支持，从API version 22开始废弃，建议使用[DeviceBasicInfo](js-apis-distributeddevicemanager.md#devicebasicinfo)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

| 类型 | 说明 |
| --- | --- |
| [\_ContinuationExtraParams](js-apis-continuation-continuationextraparams.md) | 表示流转管理入口中设备选择模块所需的过滤参数。 |
