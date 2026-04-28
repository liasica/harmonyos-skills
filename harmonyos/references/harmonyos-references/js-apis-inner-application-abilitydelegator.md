---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegator
title: AbilityDelegator
breadcrumb: API参考 > 系统 > 调测调优 > Test Kit（应用测试服务） > ArkTS API > 接口依赖的元素及定义 > AbilityDelegator
category: harmonyos-references
scraped_at: 2026-04-28T08:11:34+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:55b3b81c8a3105be82ff87c874defe468d2a620eaecf3165191aae92a9aec3ad
---

AbilityDelegator模块可以通过[AbilityMonitor](js-apis-inner-application-abilitymonitor.md)实例来监听和管理[UIAbility](js-apis-app-ability-uiability.md)生命周期的变化。例如获取UIAbility当前状态（如是否已创建/是否在前台等）、查询当前获焦的UIAbility、等待UIAbility进入某个生命周期节点（如等待UIAbility进入onForeground）、启动指定UIAbility、设置超时机制等功能。

AbilityDelegator可以通过[getAbilityDelegator](js-apis-app-ability-abilitydelegatorregistry.md#abilitydelegatorregistrygetabilitydelegator)方法获取。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在[单元测试框架](../harmonyos-guides/unittest-guidelines.md)中使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
```

## AbilityDelegator

PhonePC/2in1TabletTVWearable

### addAbilityMonitor9+

PhonePC/2in1TabletTVWearable

addAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<void>): void

添加AbilityMonitor实例。使用callback异步回调。不支持多线程并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitor | [AbilityMonitor](js-apis-inner-application-abilitymonitor.md) | 是 | [AbilityMonitor](js-apis-inner-application-abilitymonitor.md)实例。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当添加AbilityMonitor实例成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling AddAbilityMonitor failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
6. let monitor: abilityDelegatorRegistry.AbilityMonitor = {
7. abilityName: 'abilityName',
8. onAbilityCreate: onAbilityCreateCallback
9. };

11. function onAbilityCreateCallback(data: UIAbility) {
12. console.info(`onAbilityCreateCallback, data: ${JSON.stringify(data)}`);
13. }

15. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
16. abilityDelegator.addAbilityMonitor(monitor, (error: BusinessError) => {
17. console.error(`addAbilityMonitor fail, error: ${JSON.stringify(error)}`);
18. });
```

### addAbilityMonitor9+

PhonePC/2in1TabletTVWearable

addAbilityMonitor(monitor: AbilityMonitor): Promise<void>

添加AbilityMonitor实例。使用Promise异步回调。不支持多线程并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitor | [AbilityMonitor](js-apis-inner-application-abilitymonitor.md) | 是 | [AbilityMonitor](js-apis-inner-application-abilitymonitor.md)实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling AddAbilityMonitor failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { UIAbility } from '@kit.AbilityKit';

4. function onAbilityCreateCallback(data: UIAbility) {
5. console.info('onAbilityCreateCallback');
6. }

8. let monitor: abilityDelegatorRegistry.AbilityMonitor = {
9. abilityName: 'abilityName',
10. onAbilityCreate: onAbilityCreateCallback
11. };
12. let abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();

14. abilityDelegator.addAbilityMonitor(monitor).then(() => {
15. console.info('addAbilityMonitor promise');
16. });
```

### addAbilityMonitorSync10+

PhonePC/2in1TabletTVWearable

addAbilityMonitorSync(monitor: AbilityMonitor): void

同步添加AbilityMonitor实例。不支持多线程并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitor | [AbilityMonitor](js-apis-inner-application-abilitymonitor.md) | 是 | [AbilityMonitor](js-apis-inner-application-abilitymonitor.md)实例。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling AddAbilityMonitorSync failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { UIAbility } from '@kit.AbilityKit';

4. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

6. function onAbilityCreateCallback(data: UIAbility) {
7. console.info('onAbilityCreateCallback');
8. }

10. let monitor: abilityDelegatorRegistry.AbilityMonitor = {
11. abilityName: 'abilityName',
12. onAbilityCreate: onAbilityCreateCallback
13. };

15. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
16. abilityDelegator.addAbilityMonitorSync(monitor);
```

### removeAbilityMonitor9+

PhonePC/2in1TabletTVWearable

removeAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<void>): void

删除已经添加的AbilityMonitor实例。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitor | [AbilityMonitor](js-apis-inner-application-abilitymonitor.md) | 是 | [AbilityMonitor](js-apis-inner-application-abilitymonitor.md)实例。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除已经添加的AbilityMonitor实例成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling RemoveAbilityMonitor failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

7. function onAbilityCreateCallback(data: UIAbility) {
8. console.info('onAbilityCreateCallback');
9. }

11. let monitor: abilityDelegatorRegistry.AbilityMonitor = {
12. abilityName: 'abilityName',
13. onAbilityCreate: onAbilityCreateCallback
14. };

16. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
17. abilityDelegator.removeAbilityMonitor(monitor, (error: BusinessError) => {
18. console.error(`removeAbilityMonitor fail, error: ${JSON.stringify(error)}`);
19. });
```

### removeAbilityMonitor9+

PhonePC/2in1TabletTVWearable

removeAbilityMonitor(monitor: AbilityMonitor): Promise<void>

删除已经添加的AbilityMonitor实例。使用Promise异步回调。不支持多线程并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitor | [AbilityMonitor](js-apis-inner-application-abilitymonitor.md) | 是 | [AbilityMonitor](js-apis-inner-application-abilitymonitor.md)实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling RemoveAbilityMonitor failed. |

* 示例

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { UIAbility } from '@kit.AbilityKit';

4. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
5. let monitor: abilityDelegatorRegistry.AbilityMonitor = {
6. abilityName: 'abilityName',
7. onAbilityCreate: onAbilityCreateCallback
8. };

10. function onAbilityCreateCallback(data: UIAbility) {
11. console.info('onAbilityCreateCallback');
12. }

14. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
15. abilityDelegator.removeAbilityMonitor(monitor).then(() => {
16. console.info('removeAbilityMonitor promise');
17. });
```

### removeAbilityMonitorSync10+

PhonePC/2in1TabletTVWearable

removeAbilityMonitorSync(monitor: AbilityMonitor): void

同步删除已经添加的AbilityMonitor实例。不支持多线程并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitor | [AbilityMonitor](js-apis-inner-application-abilitymonitor.md) | 是 | [AbilityMonitor](js-apis-inner-application-abilitymonitor.md)实例。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling RemoveAbilityMonitorSync failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { UIAbility } from '@kit.AbilityKit';

4. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
5. let monitor: abilityDelegatorRegistry.AbilityMonitor = {
6. abilityName: 'abilityName',
7. onAbilityCreate: onAbilityCreateCallback
8. };

10. function onAbilityCreateCallback(data: UIAbility) {
11. console.info('onAbilityCreateCallback');
12. }

14. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
15. abilityDelegator.removeAbilityMonitorSync(monitor);
```

### waitAbilityMonitor9+

PhonePC/2in1TabletTVWearable

waitAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<UIAbility>): void

等待与AbilityMonitor实例匹配的Ability到达OnCreate生命周期，并返回Ability实例。使用callback异步回调。不支持多线程并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitor | [AbilityMonitor](js-apis-inner-application-abilitymonitor.md) | 是 | [AbilityMonitor](js-apis-inner-application-abilitymonitor.md)实例。 |
| callback | AsyncCallback<[UIAbility](js-apis-app-ability-uiability.md)> | 是 | 回调函数。当等待与AbilityMonitor实例匹配的Ability到达OnCreate生命周期成功，err为undefined，data为获取到的Ability实例，否则为错误对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling WaitAbilityMonitor failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
6. let monitor: abilityDelegatorRegistry.AbilityMonitor = {
7. abilityName: 'abilityName',
8. onAbilityCreate: onAbilityCreateCallback
9. };

11. function onAbilityCreateCallback(data: UIAbility) {
12. console.info(`onAbilityCreateCallback, data: ${JSON.stringify(data)}`);
13. }

15. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
16. abilityDelegator.waitAbilityMonitor(monitor, (error: BusinessError, data: UIAbility) => {
17. if (error) {
18. console.error(`waitAbilityMonitor fail, error: ${JSON.stringify(error)}`);
19. } else {
20. console.info(`waitAbilityMonitor success, data: ${JSON.stringify(data)}`);
21. }
22. });
```

### waitAbilityMonitor9+

PhonePC/2in1TabletTVWearable

waitAbilityMonitor(monitor: AbilityMonitor, timeout: number, callback: AsyncCallback<UIAbility>): void

设置等待时间，等待与AbilityMonitor实例匹配的Ability到达OnCreate生命周期，并返回Ability实例。使用callback异步回调。不支持多线程并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitor | [AbilityMonitor](js-apis-inner-application-abilitymonitor.md) | 是 | [AbilityMonitor](js-apis-inner-application-abilitymonitor.md)实例。 |
| timeout | number | 是 | 最大等待时间，单位毫秒（ms），默认值为5000毫秒。 |
| callback | AsyncCallback<[UIAbility](js-apis-app-ability-uiability.md)> | 是 | 表示指定的回调方法。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling WaitAbilityMonitor failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
6. let timeout = 100;
7. let monitor: abilityDelegatorRegistry.AbilityMonitor = {
8. abilityName: 'abilityName',
9. onAbilityCreate: onAbilityCreateCallback
10. };

12. function onAbilityCreateCallback(data: UIAbility) {
13. console.info(`onAbilityCreateCallback, data: ${JSON.stringify(data)}.`);
14. }

16. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
17. abilityDelegator.waitAbilityMonitor(monitor, timeout, (error: BusinessError, data: UIAbility) => {
18. if (error && error.code !== 0) {
19. console.error(`waitAbilityMonitor fail, error: ${JSON.stringify(error)}`);
20. } else {
21. console.info(`waitAbilityMonitor success, data: ${JSON.stringify(data)}`);
22. }
23. });
```

### waitAbilityMonitor9+

PhonePC/2in1TabletTVWearable

waitAbilityMonitor(monitor: AbilityMonitor, timeout?: number): Promise<UIAbility>

设置等待时间，等待与AbilityMonitor实例匹配的Ability到达OnCreate生命周期，并返回Ability实例。使用Promise异步回调。不支持多线程并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitor | [AbilityMonitor](js-apis-inner-application-abilitymonitor.md) | 是 | [AbilityMonitor](js-apis-inner-application-abilitymonitor.md)实例。 |
| timeout | number | 否 | 最大等待时间，单位毫秒（ms），默认值为5000毫秒。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[UIAbility](js-apis-app-ability-uiability.md)> | Promise对象，返回Ability实例。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling WaitAbilityMonitor failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { UIAbility } from '@kit.AbilityKit';

4. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
5. let monitor: abilityDelegatorRegistry.AbilityMonitor = {
6. abilityName: 'abilityName',
7. onAbilityCreate: onAbilityCreateCallback
8. };

10. function onAbilityCreateCallback(data: UIAbility) {
11. console.info('onAbilityCreateCallback');
12. }

14. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
15. abilityDelegator.waitAbilityMonitor(monitor).then((data: UIAbility) => {
16. console.info('waitAbilityMonitor promise');
17. });
```

### getAppContext9+

PhonePC/2in1TabletTVWearable

getAppContext(): Context

获取应用Context。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Context](js-apis-inner-application-context.md) | 应用[Context](js-apis-inner-application-context.md)。 |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';

3. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

5. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();

7. let context = abilityDelegator.getAppContext();
```

### getAbilityState9+

PhonePC/2in1TabletTVWearable

getAbilityState(ability: UIAbility): number

获取指定ability的生命周期状态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 指定Ability对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 指定ability的生命周期状态。状态枚举值使用[AbilityLifecycleState](js-apis-app-ability-abilitydelegatorregistry.md#abilitylifecyclestate)。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
6. let ability: UIAbility;

8. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
9. abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
10. console.info('getCurrentTopAbility callback');
11. ability = data;
12. let state = abilityDelegator.getAbilityState(ability);
13. console.info(`getAbilityState ${state}`);
14. });
```

### getCurrentTopAbility9+

PhonePC/2in1TabletTVWearable

getCurrentTopAbility(callback: AsyncCallback<UIAbility>): void

获取当前应用顶部Ability。使用callback异步回调。不支持Worker线程调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[UIAbility](js-apis-app-ability-uiability.md)> | 是 | 回调函数。当获取当前应用顶部Ability成功，err为undefined，data为获取到的Ability实例；否则为错误对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling GetCurrentTopAbility failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
6. let ability: UIAbility;

8. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
9. abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
10. console.info('getCurrentTopAbility callback');
11. ability = data;
12. });
```

### getCurrentTopAbility9+

PhonePC/2in1TabletTVWearable

getCurrentTopAbility(): Promise<UIAbility>

获取当前应用顶部Ability。使用Promise异步回调。不支持Worker线程调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[UIAbility](js-apis-app-ability-uiability.md)> | Promise对象，返回前应用顶部Ability。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000100 | Calling GetCurrentTopAbility failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { UIAbility } from '@kit.AbilityKit';

4. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
5. let ability: UIAbility;

7. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
8. abilityDelegator.getCurrentTopAbility().then((data: UIAbility) => {
9. console.info('getCurrentTopAbility promise');
10. ability = data;
11. });
```

### startAbility9+

PhonePC/2in1TabletTVWearable

startAbility(want: Want, callback: AsyncCallback<void>): void

启动指定Ability。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动Ability参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当启动指定Ability成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16200001 | The caller has been released. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
6. let want: Want = {
7. bundleName: 'bundleName',
8. abilityName: 'abilityName'
9. };

11. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
12. abilityDelegator.startAbility(want, (err: BusinessError, data: void) => {
13. console.info('startAbility callback');
14. });
```

### startAbility9+

PhonePC/2in1TabletTVWearable

startAbility(want: Want): Promise<void>

启动指定Ability。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动Ability参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16200001 | The caller has been released. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { Want } from '@kit.AbilityKit';

4. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
5. let want: Want = {
6. bundleName: 'bundleName',
7. abilityName: 'abilityName'
8. };

10. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
11. abilityDelegator.startAbility(want).then((data: void) => {
12. console.info('startAbility promise');
13. });
```

### doAbilityForeground9+

PhonePC/2in1TabletTVWearable

doAbilityForeground(ability: UIAbility, callback: AsyncCallback<void>): void

调度指定Ability生命周期状态到Foreground状态。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 指定Ability对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当调度指定Ability生命周期状态到Foreground状态成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling DoAbilityForeground failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
6. let ability: UIAbility;

8. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
9. abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
10. console.info('getCurrentTopAbility callback');
11. ability = data;
12. abilityDelegator.doAbilityForeground(ability, (err: BusinessError) => {
13. console.info("doAbilityForeground callback");
14. });
15. });
```

### doAbilityForeground9+

PhonePC/2in1TabletTVWearable

doAbilityForeground(ability: UIAbility): Promise<void>

调度指定Ability生命周期状态到Foreground状态。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 指定Ability对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling DoAbilityForeground failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
6. let ability: UIAbility;

8. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
9. abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
10. console.info('getCurrentTopAbility callback');
11. ability = data;
12. abilityDelegator.doAbilityForeground(ability).then(() => {
13. console.info("doAbilityForeground promise");
14. });
15. });
```

### doAbilityBackground9+

PhonePC/2in1TabletTVWearable

doAbilityBackground(ability: UIAbility, callback: AsyncCallback<void>): void

调度指定Ability生命周期状态到Background状态。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 指定Ability对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当调度指定Ability生命周期状态到Background状态成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling DoAbilityBackground failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
6. let ability: UIAbility;

8. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
9. abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
10. console.info('getCurrentTopAbility callback');
11. ability = data;
12. abilityDelegator.doAbilityBackground(ability, (err: BusinessError) => {
13. console.info("doAbilityBackground callback");
14. });
15. });
```

### doAbilityBackground9+

PhonePC/2in1TabletTVWearable

doAbilityBackground(ability: UIAbility): Promise<void>

调度指定Ability生命周期状态到Background状态。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 指定Ability对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling DoAbilityBackground failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
6. let ability: UIAbility;

8. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
9. abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
10. console.info('getCurrentTopAbility callback');
11. ability = data;
12. abilityDelegator.doAbilityBackground(ability).then(() => {
13. console.info("doAbilityBackground promise");
14. });
15. });
```

### printSync9+

PhonePC/2in1TabletTVWearable

printSync(msg: string): void

打印日志信息到单元测试终端控制台。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msg | string | 是 | 日志字符串。字符串最大长度为10000。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';

3. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
4. let msg = 'msg';

6. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
7. abilityDelegator.printSync(msg);
```

### print

PhonePC/2in1TabletTVWearable

print(msg: string, callback: AsyncCallback<void>): void

打印日志信息到单元测试终端控制台。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msg | string | 是 | 日志字符串。字符串最大长度为10000。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当打印日志信息到单元测试终端控制台成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
5. let msg = 'msg';

7. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
8. abilityDelegator.print(msg, (err: BusinessError) => {
9. console.info('print callback');
10. });
```

### print

PhonePC/2in1TabletTVWearable

print(msg: string): Promise<void>

打印日志信息到单元测试终端控制台。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msg | string | 是 | 日志字符串。字符串最大长度为10000。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';

3. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
4. let msg = 'msg';

6. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
7. abilityDelegator.print(msg).then(() => {
8. console.info('print promise');
9. });
```

### executeShellCommand

PhonePC/2in1TabletTVWearable

executeShellCommand(cmd: string, callback: AsyncCallback<ShellCmdResult>): void

执行指定的shell命令。使用callback异步回调。

仅支持如下shell命令：aa, bm, cp, mkdir, rm, uinput, hilog, ppwd, echo, uitest, acm, hidumper, wukong, pkill, ps, pidof

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cmd | string | 是 | shell命令字符串。 |
| callback | AsyncCallback<[ShellCmdResult](js-apis-inner-application-shellcmdresult.md#shellcmdresult-1)> | 是 | 回调函数。当执行指定的shell命令成功，err为undefined，data为获取到的执行结果；否则为错误对象。 |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
5. let cmd = 'cmd';

7. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
8. abilityDelegator.executeShellCommand(cmd, (err: BusinessError, data: abilityDelegatorRegistry.ShellCmdResult) => {
9. console.info('executeShellCommand callback');
10. });
```

### executeShellCommand

PhonePC/2in1TabletTVWearable

executeShellCommand(cmd: string, timeoutSecs: number, callback: AsyncCallback<ShellCmdResult>): void

指定超时时间，并执行指定的shell命令。使用callback异步回调。

仅支持如下shell命令：aa, bm, cp, mkdir, rm, uinput, hilog, ppwd, echo, uitest, acm, hidumper, wukong, pkill, ps, pidof

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cmd | string | 是 | shell命令字符串。 |
| timeoutSecs | number | 是 | 设定命令超时时间，单位秒（s）。 |
| callback | AsyncCallback<[ShellCmdResult](js-apis-inner-application-shellcmdresult.md#shellcmdresult-1)> | 是 | 回调函数。当执行指定的shell命令成功，err为undefined，data为获取到的执行结果；否则为错误对象。 |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
5. let cmd = 'cmd';
6. let timeout = 100;

8. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
9. abilityDelegator.executeShellCommand(cmd, timeout, (err: BusinessError, data: abilityDelegatorRegistry.ShellCmdResult) => {
10. console.info('executeShellCommand callback');
11. });
```

### executeShellCommand

PhonePC/2in1TabletTVWearable

executeShellCommand(cmd: string, timeoutSecs?: number): Promise<ShellCmdResult>

指定超时时间，并执行指定的shell命令。使用Promise异步回调。

仅支持如下shell命令：aa, bm, cp, mkdir, rm, uinput, hilog, ppwd, echo, uitest, acm, hidumper, wukong, pkill, ps, pidof

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cmd | string | 是 | shell命令字符串。 |
| timeoutSecs | number | 否 | 设定命令超时时间，单位秒（s）。默认值为0，表示不设置超时时间。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ShellCmdResult](js-apis-inner-application-shellcmdresult.md#shellcmdresult-1)> | Promise对象，返回Shell命令执行结果[ShellCmdResult](js-apis-inner-application-shellcmdresult.md#shellcmdresult-1)对象。 |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';

3. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
4. let cmd = 'cmd';
5. let timeout = 100;

7. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
8. abilityDelegator.executeShellCommand(cmd, timeout).then((data) => {
9. console.info('executeShellCommand promise');
10. });
```

### finishTest9+

PhonePC/2in1TabletTVWearable

finishTest(msg: string, code: number, callback: AsyncCallback<void>): void

结束测试并打印日志信息到单元测试终端控制台。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msg | string | 是 | 日志字符串。 |
| code | number | 是 | 日志码。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当结束测试并打印日志信息到单元测试终端控制台成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling FinishTest failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
5. let msg = 'msg';

7. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
8. abilityDelegator.finishTest(msg, 0, (err: BusinessError) => {
9. console.info('finishTest callback');
10. });
```

### finishTest9+

PhonePC/2in1TabletTVWearable

finishTest(msg: string, code: number): Promise<void>

结束测试并打印日志信息到单元测试终端控制台。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msg | string | 是 | 日志字符串。 |
| code | number | 是 | 日志码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling FinishTest failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';

3. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
4. let msg = 'msg';

6. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
7. abilityDelegator.finishTest(msg, 0).then(() => {
8. console.info('finishTest promise');
9. });
```

### addAbilityStageMonitor9+

PhonePC/2in1TabletTVWearable

addAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<void>): void

添加一个AbilityStageMonitor对象，用于监视指定AbilityStage的生命周期状态更改。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitor | [AbilityStageMonitor](js-apis-inner-application-abilitystagemonitor.md) | 是 | [AbilityStageMonitor](js-apis-inner-application-abilitystagemonitor.md) 实例。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当添加一个用于监视指定AbilityStage的生命周期状态更改的AbilityStageMonitor对象成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling AddAbilityStageMonitor failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

6. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
7. abilityDelegator.addAbilityStageMonitor({
8. moduleName: 'moduleName',
9. srcEntrance: 'srcEntrance',
10. }, (err: BusinessError) => {
11. console.info('addAbilityStageMonitor callback');
12. });
```

### addAbilityStageMonitor9+

PhonePC/2in1TabletTVWearable

addAbilityStageMonitor(monitor: AbilityStageMonitor): Promise<void>

添加一个AbilityStageMonitor对象，用于监视指定AbilityStage的生命周期状态更改。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitor | [AbilityStageMonitor](js-apis-inner-application-abilitystagemonitor.md) | 是 | [AbilityStageMonitor](js-apis-inner-application-abilitystagemonitor.md) 实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling AddAbilityStageMonitor failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';

3. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

5. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
6. abilityDelegator.addAbilityStageMonitor({
7. moduleName: 'moduleName',
8. srcEntrance: 'srcEntrance',
9. }).then(() => {
10. console.info('addAbilityStageMonitor promise');
11. });
```

### addAbilityStageMonitorSync10+

PhonePC/2in1TabletTVWearable

addAbilityStageMonitorSync(monitor: AbilityStageMonitor): void

同步添加一个AbilityStageMonitor对象，用于监视指定AbilityStage的生命周期状态更改。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitor | [AbilityStageMonitor](js-apis-inner-application-abilitystagemonitor.md) | 是 | [AbilityStageMonitor](js-apis-inner-application-abilitystagemonitor.md) 实例。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling AddAbilityStageMonitorSync failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';

3. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

5. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
6. abilityDelegator.addAbilityStageMonitorSync({
7. moduleName: 'moduleName',
8. srcEntrance: 'srcEntrance',
9. });
```

### removeAbilityStageMonitor9+

PhonePC/2in1TabletTVWearable

removeAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<void>): void

从应用程序内存中删除指定的AbilityStageMonitor对象。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitor | [AbilityStageMonitor](js-apis-inner-application-abilitystagemonitor.md) | 是 | [AbilityStageMonitor](js-apis-inner-application-abilitystagemonitor.md) 实例。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当从应用程序内存中删除指定的AbilityStageMonitor对象成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling RemoveAbilityStageMonitor failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

6. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
7. abilityDelegator.removeAbilityStageMonitor({
8. moduleName: 'moduleName',
9. srcEntrance: 'srcEntrance',
10. }, (err: BusinessError) => {
11. console.info('removeAbilityStageMonitor callback');
12. });
```

### removeAbilityStageMonitor9+

PhonePC/2in1TabletTVWearable

removeAbilityStageMonitor(monitor: AbilityStageMonitor): Promise<void>

从应用程序内存中删除指定的AbilityStageMonitor对象。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitor | [AbilityStageMonitor](js-apis-inner-application-abilitystagemonitor.md) | 是 | [AbilityStageMonitor](js-apis-inner-application-abilitystagemonitor.md) 实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling RemoveAbilityStageMonitor failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';

3. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

5. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
6. abilityDelegator.removeAbilityStageMonitor({
7. moduleName: 'moduleName',
8. srcEntrance: 'srcEntrance',
9. }).then(() => {
10. console.info('removeAbilityStageMonitor promise');
11. });
```

### removeAbilityStageMonitorSync10+

PhonePC/2in1TabletTVWearable

removeAbilityStageMonitorSync(monitor: AbilityStageMonitor): void

同步从应用程序内存中删除指定的AbilityStageMonitor对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitor | [AbilityStageMonitor](js-apis-inner-application-abilitystagemonitor.md) | 是 | [AbilityStageMonitor](js-apis-inner-application-abilitystagemonitor.md) 实例。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling RemoveAbilityStageMonitorSync failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';

3. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

5. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
6. abilityDelegator.removeAbilityStageMonitorSync({
7. moduleName: 'moduleName',
8. srcEntrance: 'srcEntrance',
9. });
```

### waitAbilityStageMonitor9+

PhonePC/2in1TabletTVWearable

waitAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<AbilityStage>): void

返回与AbilityStageMonitor中设置条件相匹配的AbilityStage对象。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitor | [AbilityStageMonitor](js-apis-inner-application-abilitystagemonitor.md) | 是 | [AbilityStageMonitor](js-apis-inner-application-abilitystagemonitor.md) 实例。 |
| callback | AsyncCallback<AbilityStage> | 是 | 回调函数。当等待并返回与给定AbilityStageMonitor中设置的条件匹配的AbilityStage对象的操作成功，err为undefined，data为获取到的[AbilityStage](js-apis-app-ability-abilitystage.md)对象；否则为错误对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling WaitAbilityStageMonitor failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { AbilityStage } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

7. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
8. abilityDelegator.waitAbilityStageMonitor({
9. moduleName: 'moduleName',
10. srcEntrance: 'srcEntrance',
11. }, (err: BusinessError, data: AbilityStage) => {
12. console.info('waitAbilityStageMonitor callback');
13. });
```

### waitAbilityStageMonitor9+

PhonePC/2in1TabletTVWearable

waitAbilityStageMonitor(monitor: AbilityStageMonitor, timeout?: number): Promise<AbilityStage>

返回与AbilityStageMonitor中设置条件相匹配的AbilityStage对象，支持设置超时最大等待时间。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitor | [AbilityStageMonitor](js-apis-inner-application-abilitystagemonitor.md) | 是 | [AbilityStageMonitor](js-apis-inner-application-abilitystagemonitor.md) 实例。 |
| timeout | number | 否 | 超时最大等待时间，单位毫秒（ms），默认值为5000毫秒。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<AbilityStage> | Promise对象，返回[AbilityStage](js-apis-app-ability-abilitystage.md)对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling WaitAbilityStageMonitor failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { AbilityStage } from '@kit.AbilityKit';

4. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

6. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
7. abilityDelegator.waitAbilityStageMonitor({
8. moduleName: 'moduleName',
9. srcEntrance: 'srcEntrance',
10. }).then((data: AbilityStage) => {
11. console.info('waitAbilityStageMonitor promise');
12. });
```

### waitAbilityStageMonitor9+

PhonePC/2in1TabletTVWearable

waitAbilityStageMonitor(monitor: AbilityStageMonitor, timeout: number, callback: AsyncCallback<AbilityStage>): void

在指定的超时最大等待时间内，返回与AbilityStageMonitor中设置条件相匹配的AbilityStage对象。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitor | [AbilityStageMonitor](js-apis-inner-application-abilitystagemonitor.md) | 是 | [AbilityStageMonitor](js-apis-inner-application-abilitystagemonitor.md) 实例。 |
| timeout | number | 是 | 超时最大等待时间，单位毫秒（ms），默认值为5000毫秒。 |
| callback | AsyncCallback<AbilityStage> | 是 | 回调函数。当等待并返回与给定AbilityStageMonitor中设置的条件匹配的AbilityStage对象的操作成功，err为undefined，data为获取到的[AbilityStage](js-apis-app-ability-abilitystage.md)对象；否则为错误对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling WaitAbilityStageMonitor failed. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { AbilityStage } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
6. let timeout = 100;

8. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
9. abilityDelegator.waitAbilityStageMonitor({
10. moduleName: 'moduleName',
11. srcEntrance: 'srcEntrance',
12. }, timeout, (err: BusinessError, data: AbilityStage) => {
13. console.info('waitAbilityStageMonitor callback');
14. });
```

### setMockList11+

PhonePC/2in1TabletTVWearable

setMockList(mockList: Record<string, string>): void

设置模块的mock替换关系。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mockList | Record<string, string> | 是 | 模块mock替换关系的键值对象，其中key为待替换的目标路径，value为用于替换的mock实现文件的路径。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000050 | Internal error. |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';

3. let mockList: Record<string, string> = {
4. '@ohos.router': 'src/main/mock/ohos/router.mock',
5. 'common.time': 'src/main/mock/common/time.mock',
6. };
7. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

9. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
10. abilityDelegator.setMockList(mockList);
```
