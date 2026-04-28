---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-appmanager
title: @ohos.app.ability.appManager (应用管理)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 通用能力的接口(推荐) > @ohos.app.ability.appManager (应用管理)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:641d9dbba0e698b947f7307a84ea6bc990745141af73850fde2d5e3be0c473ba
---

appManager模块提供应用管理的能力，包括查询当前系统是否处于稳定性测试场景、查询当前设备是否为RAM（Random Access Memory，随机存取存储器）受限设备、获取当前应用程序可以使用的最大内存值、获取有关运行进程的信息等。

说明

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { appManager } from '@kit.AbilityKit';
```

## ProcessState10+

PhonePC/2in1TabletTVWearable

表示进程状态的枚举。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE\_CREATE | 0 | 进程创建完成。 |
| STATE\_FOREGROUND | 1 | 进程处于前台。 |
| STATE\_ACTIVE | 2 | 进程中至少有一个窗口获焦。 |
| STATE\_BACKGROUND | 3 | 进程处于后台。 |
| STATE\_DESTROY | 4 | 进程销毁完成。 |

## appManager.isRunningInStabilityTest

PhonePC/2in1TabletTVWearable

isRunningInStabilityTest(callback: AsyncCallback<boolean>): void

查询当前系统是否处于稳定性测试场景。使用callback异步回调。

说明

稳定性测试场景指为验证应用在复杂、极端或长期运行条件下的可靠性而设计的特定测试环境。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当接口调用成功，err为undefined，data为当前系统是否处于稳定性测试场景的结果；否则为错误对象。可进行错误处理或其他自定义处理。  返回true表示系统处于稳定性测试场景；返回false表示系统不处于稳定性测试场景。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |

**示例：**

```
1. import { appManager } from '@kit.AbilityKit';

3. appManager.isRunningInStabilityTest((err, flag) => {
4. if (err) {
5. console.error(`isRunningInStabilityTest fail, err: ${JSON.stringify(err)}`);
6. } else {
7. console.info(`The result of isRunningInStabilityTest is: ${JSON.stringify(flag)}`);
8. }
9. });
```

## appManager.isRunningInStabilityTest

PhonePC/2in1TabletTVWearable

isRunningInStabilityTest(): Promise<boolean>

查询当前系统是否处于稳定性测试场景。使用Promise异步回调。

说明

稳定性测试场景指为验证应用在复杂、极端或长期运行条件下的可靠性而设计的特定测试环境。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示系统处于稳定性测试场景；返回false表示系统不处于稳定性测试场景。 |

**错误码**：

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. |

**示例：**

```
1. import { appManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. appManager.isRunningInStabilityTest().then((flag) => {
5. console.info(`The result of isRunningInStabilityTest is: ${JSON.stringify(flag)}`);
6. }).catch((error: BusinessError) => {
7. console.error(`error: ${JSON.stringify(error)}`);
8. });
```

## appManager.isRamConstrainedDevice

PhonePC/2in1TabletTVWearable

isRamConstrainedDevice(): Promise<boolean>

查询当前设备是否为RAM受限设备（内存资源严重受限的设备）。使用Promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前设备为RAM受限设备；返回false表示当前设备为非RAM受限设备。 |

**错误码**：

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. |

**示例：**

```
1. import { appManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. appManager.isRamConstrainedDevice().then((data) => {
5. console.info(`The result of isRamConstrainedDevice is: ${JSON.stringify(data)}`);
6. }).catch((error: BusinessError) => {
7. console.error(`error: ${JSON.stringify(error)}`);
8. });
```

## appManager.isRamConstrainedDevice

PhonePC/2in1TabletTVWearable

isRamConstrainedDevice(callback: AsyncCallback<boolean>): void

查询当前设备是否为RAM受限设备（内存资源严重受限的设备）。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当接口调用成功，err为undefined，data为当前设备是否为RAM受限设备的结果；否则为错误对象。可进行错误处理或其他自定义处理。  返回true表示当前设备为RAM受限设备；返回false表示当前设备为非RAM受限设备。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |

**示例：**

```
1. import { appManager } from '@kit.AbilityKit';

3. appManager.isRamConstrainedDevice((err, data) => {
4. if (err) {
5. console.error(`isRamConstrainedDevice fail, err: ${JSON.stringify(err)}`);
6. } else {
7. console.info(`The result of isRamConstrainedDevice is: ${JSON.stringify(data)}`);
8. }
9. });
```

## appManager.getAppMemorySize

PhonePC/2in1TabletTVWearable

getAppMemorySize(): Promise<number>

获取当前应用程序可以使用的最大内存（RAM）值。使用Promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回当前应用程序可以使用的最大内存（RAM）值，可根据此值进行错误处理或其他自定义处理，单位是M。 |

**错误码**：

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. |

**示例：**

```
1. import { appManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. appManager.getAppMemorySize().then((data) => {
5. console.info(`The size of app memory is: ${JSON.stringify(data)}`);
6. }).catch((error: BusinessError) => {
7. console.error(`error: ${JSON.stringify(error)}`);
8. });
```

## appManager.getAppMemorySize

PhonePC/2in1TabletTVWearable

getAppMemorySize(callback: AsyncCallback<number>): void

获取当前应用程序可以使用的最大内存（RAM）值。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。当接口调用成功，err为undefined，data为当前应用程序可以使用的最大内存（RAM）值，单位是M；否则为错误对象。可根据此值进行错误处理或其他自定义处理。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |

**示例：**

```
1. import { appManager } from '@kit.AbilityKit';

3. appManager.getAppMemorySize((err, data) => {
4. if (err) {
5. console.error(`getAppMemorySize fail, err: ${JSON.stringify(err)}`);
6. } else {
7. console.info(`The size of app memory is: ${JSON.stringify(data)}`);
8. }
9. });
```

## appManager.getRunningProcessInformation

PhonePC/2in1TabletTVWearable

getRunningProcessInformation(): Promise<Array<ProcessInformation>>

获取当前应用运行进程的相关信息。使用Promise异步回调。

说明

* 对于API version 11之前的版本，该接口需要申请权限ohos.permission.GET\_RUNNING\_INFO（该权限仅系统应用可申请）。
* 从API version 11开始，该接口仅用于获取调用方自身的进程信息，不再需要申请权限。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[ProcessInformation](js-apis-inner-application-processinformation.md)>> | Promise对象，返回接口运行结果及有关运行进程的信息，可进行错误处理或其他自定义处理。 |

**错误码**：

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. |

**示例：**

```
1. import { appManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. appManager.getRunningProcessInformation().then((data) => {
5. console.info(`The running process information is: ${JSON.stringify(data)}`);
6. }).catch((error: BusinessError) => {
7. console.error(`error: ${JSON.stringify(error)}`);
8. });
```

## appManager.getRunningProcessInformation

PhonePC/2in1TabletTVWearable

getRunningProcessInformation(callback: AsyncCallback<Array<ProcessInformation>>): void

获取当前应用运行进程的相关信息。使用callback异步回调。

说明

* 对于API version 11之前的版本，该接口需要申请权限ohos.permission.GET\_RUNNING\_INFO（该权限仅系统应用可申请）。
* 从API version 11开始，该接口仅用于获取调用方自身的进程信息，不再需要申请权限。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[ProcessInformation](js-apis-inner-application-processinformation.md)>> | 是 | 回调函数。当接口调用成功，err为undefined，data为当前应用运行进程的信息；否则为错误对象。可进行错误处理或其他自定义处理。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |

**示例：**

```
1. import { appManager } from '@kit.AbilityKit';

3. appManager.getRunningProcessInformation((err, data) => {
4. if (err) {
5. console.error(`getRunningProcessInformation fail, err: ${JSON.stringify(err)}`);
6. } else {
7. console.info(`The running process information is: ${JSON.stringify(data)}`);
8. }
9. });
```

## appManager.on('applicationState')14+

PhonePC/2in1TabletTVWearable

on(type: 'applicationState', observer: ApplicationStateObserver): number

注册所有应用程序的状态监听器。

**需要权限**：ohos.permission.RUNNING\_STATE\_OBSERVER

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 调用接口类型，固定填'applicationState'字符串。 |
| observer | [ApplicationStateObserver](js-apis-inner-application-applicationstateobserver.md) | 是 | 应用状态监听器，用于监听应用的生命周期变化。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 已注册监听器ID，调用方可以通过[off('applicationState')](js-apis-app-ability-appmanager.md#appmanageroffapplicationstate14)传入该监听器ID来注销监听器。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |

**示例：**

```
1. import { appManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let applicationStateObserver: appManager.ApplicationStateObserver = {
5. onForegroundApplicationChanged(appStateData) {
6. console.info(`[appManager] onForegroundApplicationChanged: ${JSON.stringify(appStateData)}`);
7. },
8. onAbilityStateChanged(abilityStateData) {
9. console.info(`[appManager] onAbilityStateChanged: ${JSON.stringify(abilityStateData)}`);
10. },
11. onProcessCreated(processData) {
12. console.info(`[appManager] onProcessCreated: ${JSON.stringify(processData)}`);
13. },
14. onProcessDied(processData) {
15. console.info(`[appManager] onProcessDied: ${JSON.stringify(processData)}`);
16. },
17. onProcessStateChanged(processData) {
18. console.info(`[appManager] onProcessStateChanged: ${JSON.stringify(processData)}`);
19. },
20. onAppStarted(appStateData) {
21. console.info(`[appManager] onAppStarted: ${JSON.stringify(appStateData)}`);
22. },
23. onAppStopped(appStateData) {
24. console.info(`[appManager] onAppStopped: ${JSON.stringify(appStateData)}`);
25. }
26. };

28. try {
29. const observerId = appManager.on('applicationState', applicationStateObserver);
30. console.info(`[appManager] observerCode: ${observerId}`);
31. } catch (paramError) {
32. let code = (paramError as BusinessError).code;
33. let message = (paramError as BusinessError).message;
34. console.error(`[appManager] error: ${code}, ${message}`);
35. }
```

## appManager.on('applicationState')14+

PhonePC/2in1TabletTVWearable

on(type: 'applicationState', observer: ApplicationStateObserver, bundleNameList: Array<string>): number

注册指定应用程序的状态监听器。

**需要权限**：ohos.permission.RUNNING\_STATE\_OBSERVER

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 调用接口类型，固定填'applicationState'字符串。 |
| observer | [ApplicationStateObserver](js-apis-inner-application-applicationstateobserver.md) | 是 | 应用状态监听器，用于监听应用的生命周期变化。 |
| bundleNameList | Array<string> | 是 | 表示需要注册监听的bundleName数组。最大值128。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 已注册监听器ID，调用方可以通过[off('applicationState')](js-apis-app-ability-appmanager.md#appmanageroffapplicationstate14)传入该监听器ID来注销监听器。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |

**示例：**

```
1. import { appManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let applicationStateObserver: appManager.ApplicationStateObserver = {
5. onForegroundApplicationChanged(appStateData) {
6. console.info(`[appManager] onForegroundApplicationChanged: ${JSON.stringify(appStateData)}`);
7. },
8. onAbilityStateChanged(abilityStateData) {
9. console.info(`[appManager] onAbilityStateChanged: ${JSON.stringify(abilityStateData)}`);
10. },
11. onProcessCreated(processData) {
12. console.info(`[appManager] onProcessCreated: ${JSON.stringify(processData)}`);
13. },
14. onProcessDied(processData) {
15. console.info(`[appManager] onProcessDied: ${JSON.stringify(processData)}`);
16. },
17. onProcessStateChanged(processData) {
18. console.info(`[appManager] onProcessStateChanged: ${JSON.stringify(processData)}`);
19. },
20. onAppStarted(appStateData) {
21. console.info(`[appManager] onAppStarted: ${JSON.stringify(appStateData)}`);
22. },
23. onAppStopped(appStateData) {
24. console.info(`[appManager] onAppStopped: ${JSON.stringify(appStateData)}`);
25. }
26. };

28. let bundleNameList = ['bundleName1', 'bundleName2'];

30. try {
31. const observerId = appManager.on('applicationState', applicationStateObserver, bundleNameList);
32. console.info(`[appManager] observerCode: ${observerId}`);
33. } catch (paramError) {
34. let code = (paramError as BusinessError).code;
35. let message = (paramError as BusinessError).message;
36. console.error(`[appManager] error: ${code}, ${message}`);
37. }
```

## appManager.off('applicationState')14+

PhonePC/2in1TabletTVWearable

off(type: 'applicationState', observerId: number): Promise<void>

注销应用状态监听器。使用Promise异步回调。

**需要权限**：ohos.permission.RUNNING\_STATE\_OBSERVER

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 调用接口类型，固定填'applicationState'字符串。 |
| observerId | number | 是 | 注册的应用状态监听器ID，即[on('applicationState')](js-apis-app-ability-appmanager.md#appmanageronapplicationstate14)返回的监听器ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |

**示例：**

```
1. import { appManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let observerId = 0;

6. // 1.注册应用状态监听器
7. let applicationStateObserver: appManager.ApplicationStateObserver = {
8. onForegroundApplicationChanged(appStateData) {
9. console.info(`[appManager] onForegroundApplicationChanged: ${JSON.stringify(appStateData)}`);
10. },
11. onAbilityStateChanged(abilityStateData) {
12. console.info(`[appManager] onAbilityStateChanged: ${JSON.stringify(abilityStateData)}`);
13. },
14. onProcessCreated(processData) {
15. console.info(`[appManager] onProcessCreated: ${JSON.stringify(processData)}`);
16. },
17. onProcessDied(processData) {
18. console.info(`[appManager] onProcessDied: ${JSON.stringify(processData)}`);
19. },
20. onProcessStateChanged(processData) {
21. console.info(`[appManager] onProcessStateChanged: ${JSON.stringify(processData)}`);
22. },
23. onAppStarted(appStateData) {
24. console.info(`[appManager] onAppStarted: ${JSON.stringify(appStateData)}`);
25. },
26. onAppStopped(appStateData) {
27. console.info(`[appManager] onAppStopped: ${JSON.stringify(appStateData)}`);
28. }
29. };
30. let bundleNameList = ['bundleName1', 'bundleName2'];

32. try {
33. observerId = appManager.on('applicationState', applicationStateObserver, bundleNameList);
34. } catch (paramError) {
35. let code = (paramError as BusinessError).code;
36. let message = (paramError as BusinessError).message;
37. console.error(`[appManager] error: ${code}, ${message}`);
38. }

40. // 2.注销应用状态监听器
41. try {
42. appManager.off('applicationState', observerId).then((data) => {
43. console.info(`unregisterApplicationStateObserver success, data: ${JSON.stringify(data)}`);
44. }).catch((err: BusinessError) => {
45. console.error(`unregisterApplicationStateObserver fail, err: ${JSON.stringify(err)}`);
46. });
47. } catch (paramError) {
48. let code = (paramError as BusinessError).code;
49. let message = (paramError as BusinessError).message;
50. console.error(`[appManager] error: ${code}, ${message}`);
51. }
```

## appManager.off('applicationState')15+

PhonePC/2in1TabletTVWearable

off(type: 'applicationState', observerId: number, callback: AsyncCallback<void>): void

注销应用状态监听器。使用callback异步回调。

**需要权限**：ohos.permission.RUNNING\_STATE\_OBSERVER

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 调用接口类型，固定填'applicationState'字符串。 |
| observerId | number | 是 | 注册的应用状态监听器ID，即[on('applicationState')](js-apis-app-ability-appmanager.md#appmanageronapplicationstate14)返回的监听器ID。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当取消注册应用程序状态观测器成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |

**示例：**

```
1. import { appManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let observerId = 0;

6. // 1.注册应用状态监听器
7. let applicationStateObserver: appManager.ApplicationStateObserver = {
8. onForegroundApplicationChanged(appStateData) {
9. console.info(`[appManager] onForegroundApplicationChanged: ${JSON.stringify(appStateData)}`);
10. },
11. onAbilityStateChanged(abilityStateData) {
12. console.info(`[appManager] onAbilityStateChanged: ${JSON.stringify(abilityStateData)}`);
13. },
14. onProcessCreated(processData) {
15. console.info(`[appManager] onProcessCreated: ${JSON.stringify(processData)}`);
16. },
17. onProcessDied(processData) {
18. console.info(`[appManager] onProcessDied: ${JSON.stringify(processData)}`);
19. },
20. onProcessStateChanged(processData) {
21. console.info(`[appManager] onProcessStateChanged: ${JSON.stringify(processData)}`);
22. },
23. onAppStarted(appStateData) {
24. console.info(`[appManager] onAppStarted: ${JSON.stringify(appStateData)}`);
25. },
26. onAppStopped(appStateData) {
27. console.info(`[appManager] onAppStopped: ${JSON.stringify(appStateData)}`);
28. }
29. };
30. let bundleNameList = ['bundleName1', 'bundleName2'];

32. try {
33. observerId = appManager.on('applicationState', applicationStateObserver, bundleNameList);
34. } catch (paramError) {
35. let code = (paramError as BusinessError).code;
36. let message = (paramError as BusinessError).message;
37. console.error(`[appManager] error: ${code}, ${message}`);
38. }

40. function offCallback(err: BusinessError) {
41. if (err) {
42. console.error(`appmanager.off failed, code: ${err.code}, msg: ${err.message}`);
43. } else {
44. console.info(`appmanager.off success.`);
45. }
46. }

48. // 2.注销应用状态监听器
49. try {
50. appManager.off('applicationState', observerId, offCallback);
51. } catch (paramError) {
52. let code = (paramError as BusinessError).code;
53. let message = (paramError as BusinessError).message;
54. console.error(`[appManager] error: ${code}, ${message}`);
55. }
```

## appManager.killProcessesByBundleName14+

PhonePC/2in1TabletTVWearable

killProcessesByBundleName(bundleName: string, clearPageStack: boolean, appIndex?: number): Promise<void>

终止指定应用包名的应用进程。使用Promise异步回调。

**需要权限**：ohos.permission.KILL\_APP\_PROCESSES 或 ohos.permission.CLEAN\_BACKGROUND\_PROCESSES

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 表示需要终止进程的应用包名。 |
| clearPageStack | boolean | 是 | 表示是否清除页面堆栈。true表示清除，false表示不清除。 |
| appIndex | number | 否 | 应用分身Id，默认值为0。取值为0时，表示终止主应用的所有进程。取值大于0时，表示终止指定分身应用的所有进程。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | If the input parameter is not valid parameter. |
| 16000050 | Internal error. |

**示例：**

```
1. import { appManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let bundleName = 'bundleName';
5. let isClearPageStack = false;
6. let appIndex = 1;

8. try {
9. appManager.killProcessesByBundleName(bundleName, isClearPageStack, appIndex).then((data) => {
10. console.info('killProcessesByBundleName success.');
11. }).catch((err: BusinessError) => {
12. console.error(`killProcessesByBundleName fail, err: ${JSON.stringify(err)}`);
13. });
14. } catch (paramError) {
15. let code = (paramError as BusinessError).code;
16. let message = (paramError as BusinessError).message;
17. console.error(`[appManager] error: ${code}, ${message}`);
18. }
```

## appManager.isAppRunning14+

PhonePC/2in1TabletTVWearable

isAppRunning(bundleName: string, appCloneIndex?: number): Promise<boolean>

判断所有用户下指定包名和分身应用索引的应用是否正在运行。使用Promise异步回调。

说明

如果当前用户未安装该应用，则返回错误码16000073；如果当前用户已安装该应用，则判断所有用户下该指定应用是否正在运行。

**需要权限**：ohos.permission.GET\_RUNNING\_INFO

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 查询的应用包名。 |
| appCloneIndex | number | 否 | 分身应用索引，默认值为0。取值范围：0~1000。取值为0时表示主应用；取值大于0时表示指定分身应用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示至少存在一个用户正在运行指定包名和分身应用索引的应用；返回false表示所有用户下指定包名和分身应用索引的应用都没有运行。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16000050 | Internal error. |
| 16000073 | The app clone index is invalid. |

**示例：**

```
1. import { appManager } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let bundleName = "ohos.samples.etsclock";
7. appManager.isAppRunning(bundleName).then((data: boolean) => {
8. hilog.info(0x0000, 'testTag', `data: ${JSON.stringify(data)}`);
9. }).catch((err: BusinessError) => {
10. hilog.error(0x0000, 'testTag', `isAppRunning error, code: ${err.code}, msg:${err.message}`);
11. })
12. } catch (err) {
13. hilog.error(0x0000, 'testTag', `isAppRunning error, code: ${err.code}, msg:${err.message}`);
14. }
```

## AbilityStateData14+

PhonePC/2in1TabletTVWearable

type AbilityStateData = \_AbilityStateData.default

Ability状态信息。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_AbilityStateData.default](js-apis-inner-application-abilitystatedata.md) | Ability状态信息。 |

## AppStateData14+

PhonePC/2in1TabletTVWearable

type AppStateData = \_AppStateData.default

应用状态信息。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_AppStateData.default](js-apis-inner-application-appstatedata.md) | 应用状态信息。 |

## ApplicationStateObserver14+

PhonePC/2in1TabletTVWearable

type ApplicationStateObserver = \_ApplicationStateObserver.default

应用状态监听器。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_ApplicationStateObserver.default](js-apis-inner-application-applicationstateobserver.md) | 应用状态监听器。 |

## ProcessInformation

PhonePC/2in1TabletTVWearable

type ProcessInformation = \_ProcessInformation

进程信息。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_ProcessInformation](js-apis-inner-application-processinformation.md) | 进程信息。 |

## ProcessData14+

PhonePC/2in1TabletTVWearable

type ProcessData = \_ProcessData.default

进程数据。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_ProcessData.default](js-apis-inner-application-processdata.md) | 进程数据。 |
