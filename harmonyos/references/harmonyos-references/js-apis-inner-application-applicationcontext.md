---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationcontext
title: ApplicationContext (应用上下文)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > ApplicationContext (应用上下文)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a9cba429b3b04134b89e55a8739b40ad9fffd0bab3058259af7738d5b42861b8
---

ApplicationContext作为应用上下文，继承自[Context](js-apis-inner-application-context.md)，提供了应用生命周期监听、进程管理、应用环境设置等应用级别的管控能力。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { common } from '@kit.AbilityKit';
```

## ApplicationContext.on('abilityLifecycle')

PhonePC/2in1TabletTVWearable

on(type: 'abilityLifecycle', callback: AbilityLifecycleCallback): number

注册监听应用内UIAbility的生命周期。使用callback异步回调。仅支持主线程调用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 此类型表示应用内UIAbility的生命周期，固定为'abilityLifecycle'。 |
| callback | [AbilityLifecycleCallback](js-apis-app-ability-abilitylifecyclecallback.md) | 是 | UIAbility生命周期变化时触发的回调方法。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回此次注册的callbackID，该ID用于在[ApplicationContext.off('abilityLifecycle')](js-apis-inner-application-applicationcontext.md#applicationcontextoffabilitylifecycle)方法中取消注册对应的callback。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**示例：**

```
1. import { UIAbility, AbilityLifecycleCallback } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let lifecycleId: number;

6. export default class EntryAbility extends UIAbility {
7. onCreate() {
8. console.info('MyAbility onCreate');
9. let AbilityLifecycleCallback: AbilityLifecycleCallback = {
10. onAbilityCreate(ability) {
11. console.info(`AbilityLifecycleCallback onAbilityCreate ability: ${ability}`);
12. },
13. onWindowStageCreate(ability, windowStage) {
14. console.info(`AbilityLifecycleCallback onWindowStageCreate ability: ${ability}`);
15. console.info(`AbilityLifecycleCallback onWindowStageCreate windowStage: ${windowStage}`);
16. },
17. onWindowStageActive(ability, windowStage) {
18. console.info(`AbilityLifecycleCallback onWindowStageActive ability: ${ability}`);
19. console.info(`AbilityLifecycleCallback onWindowStageActive windowStage: ${windowStage}`);
20. },
21. onWindowStageInactive(ability, windowStage) {
22. console.info(`AbilityLifecycleCallback onWindowStageInactive ability: ${ability}`);
23. console.info(`AbilityLifecycleCallback onWindowStageInactive windowStage: ${windowStage}`);
24. },
25. onWindowStageDestroy(ability, windowStage) {
26. console.info(`AbilityLifecycleCallback onWindowStageDestroy ability: ${ability}`);
27. console.info(`AbilityLifecycleCallback onWindowStageDestroy windowStage: ${windowStage}`);
28. },
29. onAbilityDestroy(ability) {
30. console.info(`AbilityLifecycleCallback onAbilityDestroy ability: ${ability}`);
31. },
32. onAbilityForeground(ability) {
33. console.info(`AbilityLifecycleCallback onAbilityForeground ability: ${ability}`);
34. },
35. onAbilityBackground(ability) {
36. console.info(`AbilityLifecycleCallback onAbilityBackground ability: ${ability}`);
37. },
38. onAbilityContinue(ability) {
39. console.info(`AbilityLifecycleCallback onAbilityContinue ability: ${ability}`);
40. }
41. }
42. // 1.通过context属性获取applicationContext
43. let applicationContext = this.context.getApplicationContext();
44. try {
45. // 2.通过applicationContext注册监听应用内生命周期
46. lifecycleId = applicationContext.on('abilityLifecycle', AbilityLifecycleCallback);
47. } catch (paramError) {
48. console.error(`error code: ${(paramError as BusinessError).code}, error msg: ${(paramError as BusinessError).message}`);
49. }
50. console.info(`registerAbilityLifecycleCallback lifecycleId: ${lifecycleId}`);
51. }
52. }
```

## ApplicationContext.off('abilityLifecycle')

PhonePC/2in1TabletTVWearable

off(type: 'abilityLifecycle', callbackId: number, callback: AsyncCallback<void>): void

取消监听应用内UIAbility的生命周期。使用callback异步回调。仅支持主线程调用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 此类型表示应用内UIAbility的生命周期，固定为'abilityLifecycle'。 |
| callbackId | number | 是 | 通过[ApplicationContext.on('abilityLifecycle')](js-apis-inner-application-applicationcontext.md#applicationcontextonabilitylifecycle)接口注册监听应用内UIAbility的生命周期时返回的ID。 |
| callback | AsyncCallback<void> | 是 | 回调方法。当取消监听应用内生命周期成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let lifecycleId: number;

6. export default class EntryAbility extends UIAbility {
7. onDestroy() {
8. let applicationContext = this.context.getApplicationContext();
9. console.info(`stage applicationContext: ${applicationContext}`);
10. try {
11. applicationContext.off('abilityLifecycle', lifecycleId, (error, data) => {
12. if (error) {
13. console.error(`unregisterAbilityLifecycleCallback fail, err: ${JSON.stringify(error)}`);
14. } else {
15. console.info(`unregisterAbilityLifecycleCallback success, data: ${JSON.stringify(data)}`);
16. }
17. });
18. } catch (paramError) {
19. console.error(`error code: ${(paramError as BusinessError).code}, error code: ${(paramError as BusinessError).message}`);
20. }
21. }
22. }
```

## ApplicationContext.off('abilityLifecycle')

PhonePC/2in1TabletTVWearable

off(type: 'abilityLifecycle', callbackId: number): Promise<void>

取消监听应用内UIAbility的生命周期。使用Promise异步回调。仅支持主线程调用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 此类型表示应用内UIAbility的生命周期，固定为'abilityLifecycle'。 |
| callbackId | number | 是 | 通过[ApplicationContext.on('abilityLifecycle')](js-apis-inner-application-applicationcontext.md#applicationcontextonabilitylifecycle)接口注册监听应用内UIAbility的生命周期时返回的ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let lifecycleId: number;

6. export default class MyAbility extends UIAbility {
7. onDestroy() {
8. let applicationContext = this.context.getApplicationContext();
9. console.info(`stage applicationContext: ${applicationContext}`);
10. try {
11. applicationContext.off('abilityLifecycle', lifecycleId);
12. } catch (paramError) {
13. console.error(`error code: ${(paramError as BusinessError).code}, error msg: ${(paramError as BusinessError).message}`);
14. }
15. }
16. }
```

## ApplicationContext.on('environment')

PhonePC/2in1TabletTVWearable

on(type: 'environment', callback: EnvironmentCallback): number

注册对系统环境变化的监听。使用callback异步回调。仅支持主线程调用。

说明

* 使用[onConfigurationUpdate](js-apis-app-ability-ability.md#abilityonconfigurationupdate)也可以实现对系统环境变量的监听。相较于Ability的[onConfigurationUpdate](js-apis-app-ability-ability.md#abilityonconfigurationupdate)接口，当前接口的使用场景更加灵活，不仅可以在应用组件中使用，还可以在页面中使用，但是支持订阅的环境变量与Ability的[onConfigurationUpdate](js-apis-app-ability-ability.md#abilityonconfigurationupdate)接口存在差异，如不支持订阅direction、screenDensity、displayId，详见[Configuration](js-apis-app-ability-configuration.md#configuration)中各个环境变量的说明。
* 当前接口在实际触发时存在一定限制。例如如果开发者通过[setLanguage](js-apis-inner-application-applicationcontext.md#applicationcontextsetlanguage11)接口设置应用的语言，即便系统语言发生变化，系统也不再触发当前接口的[callback](js-apis-app-ability-environmentcallback.md)回调。详见[使用场景](../harmonyos-guides/subscribe-system-environment-variable-changes.md#使用场景)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 此类型表示系统环境变化，如系统深浅色发生变化，固定为'environment'。 |
| callback | [EnvironmentCallback](js-apis-app-ability-environmentcallback.md) | 是 | 系统环境变化时触发的回调方法。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回此次注册的callbackID，该ID用于在[ApplicationContext.off('environment')](js-apis-inner-application-applicationcontext.md#applicationcontextoffenvironment)方法中取消注册对应的callback。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**示例：**

```
1. import { UIAbility, EnvironmentCallback } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let callbackId: number;

6. export default class EntryAbility extends UIAbility {
7. onCreate() {
8. console.info('MyAbility onCreate')
9. let environmentCallback: EnvironmentCallback = {
10. onConfigurationUpdated(config) {
11. console.info(`onConfigurationUpdated config: ${JSON.stringify(config)}`);
12. },
13. onMemoryLevel(level) {
14. console.info(`onMemoryLevel level: ${level}`);
15. }
16. };
17. // 1.获取applicationContext
18. let applicationContext = this.context.getApplicationContext();
19. try {
20. // 2.通过applicationContext注册监听系统环境变化
21. callbackId = applicationContext.on('environment', environmentCallback);
22. } catch (paramError) {
23. console.error(`error code: ${(paramError as BusinessError).code}, error msg: ${(paramError as BusinessError).message}`);
24. }
25. console.info(`registerEnvironmentCallback callbackId: ${callbackId}`);
26. }
27. }
```

## ApplicationContext.off('environment')

PhonePC/2in1TabletTVWearable

off(type: 'environment', callbackId: number, callback: AsyncCallback<void>): void

取消对系统环境变化的监听。使用callback异步回调。仅支持主线程调用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 此类型表示系统环境变化，如系统深浅色发生变化，固定为'environment'。 |
| callbackId | number | 是 | 通过[ApplicationContext.on('environment')](js-apis-inner-application-applicationcontext.md#applicationcontextonenvironment)接口注册监听系统环境变化时返回的ID。 |
| callback | AsyncCallback<void> | 是 | 回调方法。当取消对系统环境变化的监听成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let callbackId: number;

6. export default class EntryAbility extends UIAbility {
7. onDestroy() {
8. let applicationContext = this.context.getApplicationContext();
9. try {
10. applicationContext.off('environment', callbackId, (error, data) => {
11. if (error) {
12. console.error(`unregisterEnvironmentCallback fail, err: ${JSON.stringify(error)}`);
13. } else {
14. console.info(`unregisterEnvironmentCallback success, data: ${JSON.stringify(data)}`);
15. }
16. });
17. } catch (paramError) {
18. console.error(`error code: ${(paramError as BusinessError).code}, error msg: ${(paramError as BusinessError).message}`);
19. }
20. }
21. }
```

## ApplicationContext.off('environment')

PhonePC/2in1TabletTVWearable

off(type: 'environment', callbackId: number): Promise<void>

取消对系统环境变化的监听。使用Promise异步回调。仅支持主线程调用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 此类型表示系统环境变化，如系统深浅色发生变化，固定为'environment'。 |
| callbackId | number | 是 | 通过[ApplicationContext.on('environment')](js-apis-inner-application-applicationcontext.md#applicationcontextonenvironment)接口注册监听系统环境变化时返回的ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let callbackId: number;

6. export default class MyAbility extends UIAbility {
7. onDestroy() {
8. let applicationContext = this.context.getApplicationContext();
9. try {
10. applicationContext.off('environment', callbackId);
11. } catch (paramError) {
12. console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
13. }
14. }
15. }
```

## ApplicationContext.on('applicationStateChange')10+

PhonePC/2in1TabletTVWearable

on(type: 'applicationStateChange', callback: ApplicationStateChangeCallback): void

注册对当前应用进程状态变化的监听。使用callback异步回调。仅支持主线程调用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 此类型表示当前应用进程状态变化，固定为'applicationStateChange'。 |
| callback | [ApplicationStateChangeCallback](js-apis-app-ability-applicationstatechangecallback.md) | 是 | 当前应用进程状态切换时触发的回调方法。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**示例：**

```
1. import { UIAbility, ApplicationStateChangeCallback } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class MyAbility extends UIAbility {
5. onCreate() {
6. console.info('MyAbility onCreate');
7. let applicationStateChangeCallback: ApplicationStateChangeCallback = {
8. onApplicationForeground() {
9. console.info('applicationStateChangeCallback onApplicationForeground');
10. },
11. onApplicationBackground() {
12. console.info('applicationStateChangeCallback onApplicationBackground');
13. }
14. }

16. // 1.获取applicationContext
17. let applicationContext = this.context.getApplicationContext();
18. try {
19. // 2.通过applicationContext注册当前应用进程状态监听
20. applicationContext.on('applicationStateChange', applicationStateChangeCallback);
21. } catch (paramError) {
22. console.error(`error code: ${(paramError as BusinessError).code}, error msg: ${(paramError as BusinessError).message}`);
23. }
24. console.info('Register applicationStateChangeCallback');
25. }
26. }
```

## ApplicationContext.off('applicationStateChange')10+

PhonePC/2in1TabletTVWearable

off(type: 'applicationStateChange', callback?: ApplicationStateChangeCallback): void

取消对当前应用进程状态变化的监听。使用callback异步回调。仅支持主线程调用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 此类型表示当前应用进程状态变化，固定为'applicationStateChange'。 |
| callback | [ApplicationStateChangeCallback](js-apis-app-ability-applicationstatechangecallback.md) | 否 | 回调函数。取值可以为使用[ApplicationContext.on('applicationStateChange')](js-apis-inner-application-applicationcontext.md#applicationcontextonapplicationstatechange10)方法定义的callback回调，也可以为空。  - 如果传入已定义的回调，则取消该监听。  - 如果未传入参数，则取消所有已注册的该类型事件的监听。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**示例：**

假定已使用[ApplicationContext.on('applicationStateChange')](js-apis-inner-application-applicationcontext.md#applicationcontextonapplicationstatechange10)方法注册名为applicationStateChangeCallback回调，下面示例展示如何取消对应的事件监听。

```
1. import { UIAbility, ApplicationStateChangeCallback } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let applicationStateChangeCallback: ApplicationStateChangeCallback = {
5. onApplicationForeground() {
6. console.info('applicationStateChangeCallback onApplicationForeground');
7. },
8. onApplicationBackground() {
9. console.info('applicationStateChangeCallback onApplicationBackground');
10. }
11. };

13. export default class MyAbility extends UIAbility {
14. onDestroy() {
15. let applicationContext = this.context.getApplicationContext();
16. try {
17. // 本例中的callback字段取值为ApplicationStateChangeCallback，需要替换为实际值。
18. // 如果callback字段不传入参数，则取消所有已注册的该类型事件的监听。
19. applicationContext.off('applicationStateChange', applicationStateChangeCallback);
20. } catch (paramError) {
21. console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
22. }
23. }
24. }
```

## ApplicationContext.getRunningProcessInformation

PhonePC/2in1TabletTVWearable

getRunningProcessInformation(): Promise<Array<ProcessInformation>>

获取运行中的进程信息。使用Promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[ProcessInformation](js-apis-inner-application-processinformation.md)>> | Promise对象，返回接口运行结果及有关运行进程的信息，可进行错误处理或其他自定义处理。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class MyAbility extends UIAbility {
5. onForeground() {
6. let applicationContext = this.context.getApplicationContext();
7. applicationContext.getRunningProcessInformation().then((data) => {
8. console.info(`The process running information is: ${JSON.stringify(data)}`);
9. }).catch((error: BusinessError) => {
10. console.error(`error code: ${error.code}, error msg: ${error.message}`);
11. });
12. }
13. }
```

## ApplicationContext.getRunningProcessInformation

PhonePC/2in1TabletTVWearable

getRunningProcessInformation(callback: AsyncCallback<Array<ProcessInformation>>): void

获取运行中的进程信息。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[ProcessInformation](js-apis-inner-application-processinformation.md)>> | 是 | 回调函数，返回有关运行进程的信息。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';

3. export default class MyAbility extends UIAbility {
4. onForeground() {
5. let applicationContext = this.context.getApplicationContext();
6. applicationContext.getRunningProcessInformation((err, data) => {
7. if (err) {
8. console.error(`getRunningProcessInformation failed, err: ${JSON.stringify(err)}`);
9. } else {
10. console.info(`The process running information is: ${JSON.stringify(data)}`);
11. }
12. })
13. }
14. }
```

## ApplicationContext.killAllProcesses

PhonePC/2in1TabletTVWearable

killAllProcesses(): Promise<void>

终止应用的所有进程，进程退出时不会正常执行完整的应用生命周期流程。使用Promise异步回调。仅支持主线程调用。

说明

该接口用于应用异常场景中强制退出应用。如需正常退出应用，可以使用[terminateSelf()](js-apis-inner-application-uiabilitycontext.md#terminateself-1)接口。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';

3. export default class MyAbility extends UIAbility {
4. onBackground() {
5. let applicationContext = this.context.getApplicationContext();
6. applicationContext.killAllProcesses();
7. }
8. }
```

## ApplicationContext.killAllProcesses14+

PhonePC/2in1TabletTVWearable

killAllProcesses(clearPageStack: boolean): Promise<void>

终止应用的所有进程，进程退出时不会正常执行完整的应用生命周期流程。使用Promise异步回调。仅支持主线程调用。

说明

该接口用于应用异常场景中强制退出应用。如需正常退出应用，可以使用[terminateSelf()](js-apis-inner-application-uiabilitycontext.md#terminateself-1)接口。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clearPageStack | boolean | 是 | 表示是否清除页面堆栈。true表示清除，false表示不清除。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 16000011 | The context does not exist. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';

3. let isClearPageStack = false;

5. export default class MyAbility extends UIAbility {
6. onBackground() {
7. let applicationContext = this.context.getApplicationContext();
8. applicationContext.killAllProcesses(isClearPageStack);
9. }
10. }
```

## ApplicationContext.killAllProcesses

PhonePC/2in1TabletTVWearable

killAllProcesses(callback: AsyncCallback<void>): void

终止应用的所有进程，进程退出时不会正常执行完整的应用生命周期流程。使用callback异步回调。仅支持主线程调用。

说明

该接口用于应用异常场景中强制退出应用。如需正常退出应用，可以使用[terminateSelf()](js-apis-inner-application-uiabilitycontext.md#terminateself-1)接口。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当终止应用所在的进程成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';

3. export default class MyAbility extends UIAbility {
4. onBackground() {
5. let applicationContext = this.context.getApplicationContext();
6. applicationContext.killAllProcesses(error => {
7. if (error) {
8. console.error(`killAllProcesses fail, error: ${JSON.stringify(error)}`);
9. }
10. });
11. }
12. }
```

## ApplicationContext.setColorMode11+

PhonePC/2in1TabletTVWearable

setColorMode(colorMode: ConfigurationConstant.ColorMode): void

设置应用的深浅色模式。仅支持主线程调用。

说明

调用该接口前，需要确保窗口已完成创建、且UIAbility对应的页面已完成加载，即在[onWindowStageCreate()](js-apis-app-ability-uiability.md#onwindowstagecreate)生命周期中通过[loadContent](arkts-apis-window-windowstage.md#loadcontent9)方法加载页面之后调用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorMode | [ConfigurationConstant.ColorMode](js-apis-app-ability-configurationconstant.md#colormode) | 是 | 深浅色模式，包括：深色模式、浅色模式、未设置颜色模式（默认）。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |

**示例：**

```
1. import { UIAbility, ConfigurationConstant } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';

4. export default class MyAbility extends UIAbility {
5. onWindowStageCreate(windowStage: window.WindowStage) {
6. console.info("Ability onWindowStageCreate");
7. windowStage.loadContent('pages/Index', (err, data) => {
8. if (err.code) {
9. console.error(`Failed to load the content. Code: ${err.code}, message: ${err.message}`);
10. return;
11. }
12. console.info(`Succeeded in loading the content. Data: ${JSON.stringify(data)}`);
13. let applicationContext = this.context.getApplicationContext();
14. applicationContext.setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_DARK);
15. });
16. }
17. }
```

## ApplicationContext.setLanguage11+

PhonePC/2in1TabletTVWearable

setLanguage(language: string): void

设置应用的语言。仅支持主线程调用。

说明

调用该接口前，需要确保窗口已完成创建、且UIAbility对应的页面已完成加载，即在[onWindowStageCreate()](js-apis-app-ability-uiability.md#onwindowstagecreate)生命周期中通过[loadContent](arkts-apis-window-windowstage.md#loadcontent9)方法加载页面之后调用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| language | string | 是 | 设置语言，当前支持的语言列表可以通过[getSystemLanguages()](js-apis-i18n.md#getsystemlanguages9)获取。 |

**错误码**：

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';

4. export default class MyAbility extends UIAbility {
5. onWindowStageCreate(windowStage: window.WindowStage) {
6. console.info("Ability onWindowStageCreate");
7. windowStage.loadContent('pages/Index', (err, data) => {
8. if (err.code) {
9. console.error(`Failed to load the content. Code: ${err.code}, message: ${err.message}`);
10. return;
11. }
12. console.info(`Succeeded in loading the content. Data: ${JSON.stringify(data)}`);
13. });
14. let applicationContext = this.context.getApplicationContext();
15. applicationContext.setLanguage('zh-cn');
16. }
17. }
```

## ApplicationContext.clearUpApplicationData11+

PhonePC/2in1TabletTVWearable

clearUpApplicationData(): Promise<void>

清理当前应用的应用文件路径下的所有数据，同时撤销应用向用户申请的权限。使用Promise异步回调。仅支持主线程调用。

说明

应用文件路径详见[应用文件目录信息](../harmonyos-guides/app-sandbox-directory.md#应用文件目录与应用文件路径)。图中仅标识了el1~el2目录下的应用文件路径，其他文件加密类型目录下的应用文件路径可以参考el1。

该接口会停止应用进程，应用进程停止后，后续的所有回调都不会再触发。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';

3. export default class MyAbility extends UIAbility {
4. onBackground() {
5. let applicationContext = this.context.getApplicationContext();
6. applicationContext.clearUpApplicationData();
7. }
8. }
```

## ApplicationContext.clearUpApplicationData11+

PhonePC/2in1TabletTVWearable

clearUpApplicationData(callback: AsyncCallback<void>): void

清理当前应用的应用文件路径下的所有数据，同时撤销应用向用户申请的权限。使用callback异步回调。仅支持主线程调用。

说明

应用文件路径详见[应用文件目录信息](../harmonyos-guides/app-sandbox-directory.md#应用文件目录与应用文件路径)。图中仅标识了el1~el2目录下的应用文件路径，其他文件加密类型目录下的应用文件路径可以参考el1。

该接口会停止应用进程，应用进程停止后，后续的所有回调都不会再触发。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调方法。清理应用本身的数据成功时，error为undefined，否则返回错误对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';

3. export default class MyAbility extends UIAbility {
4. onBackground() {
5. let applicationContext = this.context.getApplicationContext();
6. applicationContext.clearUpApplicationData(error => {
7. if (error) {
8. console.error(`clearUpApplicationData fail, error: ${JSON.stringify(error)}`);
9. }
10. });
11. }
12. }
```

## ApplicationContext.restartApp12+

PhonePC/2in1TabletTVWearable

restartApp(want: Want): void

应用重启并拉起自身指定UIAbility。仅支持主线程调用，且待重启的应用需要处于获焦状态。

说明

通过该接口重启应用时，不会触发应用中Ability的onDestroy生命周期回调。

在元服务调用本接口成功后的3秒内，再次调用本接口、[restartSelfAtomicService()](js-apis-app-ability-abilitymanager.md#abilitymanagerrestartselfatomicservice20)或[UIAbilityContext.restartApp()](js-apis-inner-application-uiabilitycontext.md#restartapp22)接口中的任一接口，系统将返回错误码16000064。

在应用调用本接口成功后的3秒内，若再次调用本接口或[UIAbilityContext.restartApp()](js-apis-inner-application-uiabilitycontext.md#restartapp22)接口中的任一接口，系统将返回错误码16000064。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | Want类型参数，传入需要启动的UIAbility信息，校验abilityName，不校验bundleName。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000063 | The target to restart does not belong to the current application or is not a UIAbility. |
| 16000064 | Restart too frequently. Try again at least 3s later. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { common, Want } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'restartApp';
8. private context = this.getUIContext().getHostContext()?.getApplicationContext() as common.ApplicationContext;

10. build() {
11. RelativeContainer() {
12. Text(this.message)
13. .id('HelloWorld')
14. .fontSize($r('app.float.page_text_font_size'))
15. .fontWeight(FontWeight.Bold)
16. .alignRules({
17. center: { anchor: '__container__', align: VerticalAlign.Center },
18. middle: { anchor: '__container__', align: HorizontalAlign.Center }
19. })
20. .onClick(() => {
21. let want: Want = {
22. bundleName: 'com.example.myapplication',
23. abilityName: 'EntryAbility'
24. };
25. if (this.context) {
26. try {
27. this.context.restartApp(want);
28. } catch (err) {
29. hilog.error(0x0000, 'testTag', `restart failed: ${err.code}, ${err.message}`);
30. }
31. } else {
32. hilog.error(0x0000, 'testTag', "%{public}s", 'AppContext is null');
33. }
34. })
35. }
36. .height('100%')
37. .width('100%')
38. }
39. }
```

## ApplicationContext.getCurrentAppCloneIndex12+

PhonePC/2in1TabletTVWearable

getCurrentAppCloneIndex(): number

获取当前应用的分身索引。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前应用的分身索引。 |

**错误码**：

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |
| 16000071 | The MultiAppMode is not App\_CLONE. |

以上错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';

3. export default class MyAbility extends UIAbility {
4. onBackground() {
5. let applicationContext = this.context.getApplicationContext();
6. try {
7. let appCloneIndex = applicationContext.getCurrentAppCloneIndex();
8. } catch (error) {
9. console.error(`getCurrentAppCloneIndex fail, error: ${JSON.stringify(error)}`);
10. }
11. }
12. }
```

## ApplicationContext.setFont12+

PhonePC/2in1TabletTVWearable

setFont(font: string): void

设置应用的字体类型。仅支持主线程调用。

说明

调用该接口前，需要确保窗口已完成创建、且UIAbility对应的页面已完成加载，即在[onWindowStageCreate()](js-apis-app-ability-uiability.md#onwindowstagecreate)生命周期中通过[loadContent](arkts-apis-window-windowstage.md#loadcontent9)方法加载页面之后调用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| font | string | 是 | 设置字体类型，字体可以通过[UIContext.registerFont](arkts-apis-uicontext-font.md#registerfont)方法进行注册使用。 |

**错误码**：

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'Hello World';
7. context = this.getUIContext().getHostContext() as common.UIAbilityContext;

9. aboutToAppear() {
10. this.getUIContext().getFont().registerFont({
11. familyName: 'fontName',
12. familySrc: $rawfile('font/medium.ttf')  // 'font/medium.ttf'仅作为示例，实际使用时请替换为真实的字体资源文件。
13. });

15. this.context.getApplicationContext().setFont('fontName');
16. }

18. build() {
19. Row() {
20. Column() {
21. Text(this.message)
22. .fontSize(50)
23. .fontWeight(50)
24. }
25. .width('100%')
26. }
27. .height('100%')
28. }
29. }
```

## ApplicationContext.setSupportedProcessCache12+

PhonePC/2in1TabletTVWearable

setSupportedProcessCache(isSupported : boolean): void

设置当前应用进程是否支持进程资源的缓存，便于应用再次启动时复用缓存的进程资源。仅支持主线程调用。

该接口仅对单个进程实例生效，不同进程实例互不影响。应用进程实例销毁后，已设置的状态不保留，需要重新设置。

说明

* 该接口仅表示应用自身是否为缓存后快速启动做好了准备，还需综合其他条件来判断最终是否为应用启用快速启动。
* 为了确保该接口在进程退出前生效，调用时机应尽量提前。建议在[AbilityStage](js-apis-app-ability-abilitystage.md)的onCreate()中调用该接口。
* 在同一进程多次调用该接口时，会以最后一次调用的结果为准。当存在多个AbilityStage时，为了确保结果符合预期，需要在各个AbilityStage中分别调用该接口并配置相同的取值。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口仅在Phone和2in1设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isSupported | boolean | 是 | 表示应用是否支持进程资源的缓存。true表示支持，false表示不支持。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)、[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 801 | Capability not supported. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. import { AbilityStage, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class MyAbilityStage extends AbilityStage {
5. onCreate() {
6. let applicationContext = this.context.getApplicationContext();
7. try {
8. applicationContext.setSupportedProcessCache(true);
9. } catch (error) {
10. let code = (error as BusinessError).code;
11. let message = (error as BusinessError).message;
12. console.error(`setSupportedProcessCache fail, code: ${code}, msg: ${message}`);
13. }
14. }
15. }
```

## ApplicationContext.setFontSizeScale13+

PhonePC/2in1TabletTVWearable

setFontSizeScale(fontSizeScale: number): void

设置应用字体大小缩放比例。仅支持主线程调用。

**元服务API**：从API version 13开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fontSizeScale | number | 是 | 表示字体缩放比例，取值为非负数。当应用字体[跟随系统](../harmonyos-guides/app-configuration-file.md#configuration标签)且该字段取值超过[fontSizeMaxScale](../harmonyos-guides/app-configuration-file.md#configuration标签)取值时，实际生效值为[fontSizeMaxScale](../harmonyos-guides/app-configuration-file.md#configuration标签)取值。 |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';

4. export default class MyAbility extends UIAbility {
5. onWindowStageCreate(windowStage: window.WindowStage) {
6. windowStage.loadContent('pages/Index', (err, data) => {
7. if (err.code) {
8. return;
9. }
10. let applicationContext = this.context.getApplicationContext();
11. applicationContext.setFontSizeScale(2);
12. });
13. }
14. }
```

## ApplicationContext.getCurrentInstanceKey14+

PhonePC/2in1TabletTVWearable

getCurrentInstanceKey(): string

获取当前应用多实例的唯一实例标识。仅支持主线程调用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口仅在2in1设备中可正常调用，在其他设备中返回16000078错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回当前应用多实例的唯一实例标识。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |
| 16000078 | The multi-instance is not supported. |

**示例：**

```
1. import { AbilityStage } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class MyAbilityStage extends AbilityStage {
5. onCreate() {
6. let applicationContext = this.context.getApplicationContext();
7. let currentInstanceKey = '';
8. try {
9. currentInstanceKey = applicationContext.getCurrentInstanceKey();
10. } catch (error) {
11. let code = (error as BusinessError).code;
12. let message = (error as BusinessError).message;
13. console.error(`getCurrentInstanceKey fail, code: ${code}, msg: ${message}`);
14. }
15. console.info(`currentInstanceKey: ${currentInstanceKey}`);
16. }
17. }
```

## ApplicationContext.getAllRunningInstanceKeys14+

PhonePC/2in1TabletTVWearable

getAllRunningInstanceKeys(): Promise<Array<string>>;

获取应用的所有多实例的唯一实例标识。使用Promise异步回调。仅支持主线程调用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口仅在PC/2in1设备中可正常调用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回应用的所有多实例的唯一实例标识。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16000078 | The multi-instance is not supported. |

**示例：**

```
1. import { AbilityStage } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class MyAbilityStage extends AbilityStage {
5. onCreate() {
6. let applicationContext = this.context.getApplicationContext();
7. try {
8. applicationContext.getAllRunningInstanceKeys();
9. } catch (error) {
10. let code = (error as BusinessError).code;
11. let message = (error as BusinessError).message;
12. console.error(`getAllRunningInstanceKeys fail, code: ${code}, msg: ${message}`);
13. }
14. }
15. }
```

## ApplicationContext.getAllWindowStages23+

PhonePC/2in1TabletTVWearable

getAllWindowStages(): Promise<Array<window.WindowStage>>

获取应用当前进程内的所有WindowStage对象。使用Promise异步回调。仅支持主线程调用。

该接口主要用于包含多个UIAbility的应用进行多窗口管理，例如管理多个WindowStage的状态、同一应用的多个窗口间的状态或数据同步等。

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[window.WindowStage](arkts-apis-window-windowstage.md)>> | Promise对象，返回应用当前进程内的所有WindowStage对象。 |

**示例：**

```
1. import { AbilityStage } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. export default class MyAbilityStage extends AbilityStage {
6. onCreate() {
7. let applicationContext = this.context.getApplicationContext();
8. try {
9. applicationContext.getAllWindowStages().then((data: window.WindowStage[]) => {
10. let windowStage: window.WindowStage[] = data;
11. console.info(`WindowStages size ${windowStage.length}`);
12. }).catch((error: BusinessError) => {
13. console.error(`getAllWindowStages error, code: ${error.code}, error msg: ${error.message}`);
14. });
15. } catch (error) {
16. let code = (error as BusinessError).code;
17. let message = (error as BusinessError).message;
18. console.error(`getAllWindowStages fail, code: ${code}, msg: ${message}`);
19. }
20. }
21. }
```
