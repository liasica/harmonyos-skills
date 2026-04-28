---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startupmanager
title: @ohos.app.appstartup.startupManager (启动框架管理能力)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.appstartup.startupManager (启动框架管理能力)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:23+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:d9c95bdd6e8ff07bf32ef16a9475dc6db9643347a98393584fc16bd771303266
---

本模块提供[应用启动框架](../harmonyos-guides/app-startup.md)管理启动任务的能力，只能在主线程调用。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块从API version 18开始支持so预加载。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { startupManager }  from '@kit.AbilityKit';
```

## startupManager.run

PhonePC/2in1TabletTVWearable

run(startupTasks: Array<string>, config?: StartupConfig): Promise<void>

执行启动框架启动任务或加载so文件。

说明

本接口不支持执行feature类型HAP中的启动任务，如需要使用相关能力请调用[startupManager.run](js-apis-app-appstartup-startupmanager.md#startupmanagerrun20)接口。

本接口只支持[应用级so](../harmonyos-guides/ability-terminology.md#应用级so)文件加载，不支持[系统级so](../harmonyos-guides/ability-terminology.md#系统级so)文件加载。

**系统能力**：SystemCapability.Ability.AppStartup

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startupTasks | Array<string> | 是 | 表示准备执行的启动任务[StartupTask](js-apis-app-appstartup-startuptask.md)的名称或预加载so名称的数组。 |
| config | [StartupConfig](js-apis-app-appstartup-startupconfig.md) | 否 | 表示启动任务配置信息，包含启动框架超时时间与启动任务监听器配置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16000050 | Internal error. |
| 28800001 | Startup task or its dependency not found. |
| 28800002 | The startup tasks have circular dependencies. |
| 28800003 | An error occurred while running the startup tasks. |
| 28800004 | Running startup tasks timeout. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want, startupManager } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
7. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
8. let startParams = ['StartupTask_001', 'libentry_001'];
9. try {
10. // 手动调用run方法
11. startupManager.run(startParams).then(() => {
12. console.info(`StartupTest startupManager run then, startParams = ${startParams}.`);
13. }).catch((error: BusinessError) => {
14. console.error(`StartupTest promise catch failed, error code: ${error.code}, error msg: ${error.message}.`);
15. });
16. } catch (error) {
17. let errMsg = (error as BusinessError).message;
18. let errCode = (error as BusinessError).code;
19. console.error(`Startup.run failed, err code: ${errCode}, err msg: ${errMsg}.`);
20. }
21. }

23. // ...
24. }
```

## startupManager.run20+

PhonePC/2in1TabletTVWearable

run(startupTasks: Array<string>, context: common.AbilityStageContext, config: StartupConfig): Promise<void>

执行启动框架启动任务或加载so文件。支持指定[AbilityStageContext](js-apis-inner-application-abilitystagecontext.md)用于启动任务的加载。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AppStartup

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startupTasks | Array<string> | 是 | 表示准备执行的启动任务[StartupTask](js-apis-app-appstartup-startuptask.md)的名称或预加载so名称的数组。 |
| context | [common.AbilityStageContext](js-apis-inner-application-abilitystagecontext.md) | 是 | 表示执行启动任务[StartupTask](js-apis-app-appstartup-startuptask.md)的AbilityStage上下文，作为入参传给启动任务的[init](js-apis-app-appstartup-startuptask.md#init)。 |
| config | [StartupConfig](js-apis-app-appstartup-startupconfig.md) | 是 | 表示启动任务配置信息，包含启动框架超时时间与启动任务监听器配置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. |
| 28800001 | Startup task or its dependency not found. |
| 28800002 | The startup tasks have circular dependencies. |
| 28800003 | An error occurred while running the startup tasks. |
| 28800004 | Running startup tasks timeout. |

**示例：**

```
1. import { AbilityStage, startupManager, StartupListener, StartupConfig } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class MyAbilityStage extends AbilityStage {
6. onCreate(): void {
7. hilog.info(0x0000, 'testTag', 'AbilityStage onCreate');
8. let onCompletedCallback = (error: BusinessError<void>) => {
9. if (error) {
10. hilog.error(0x0000, 'testTag', `onCompletedCallback error code: ${error.code}, error msg: ${error.message}`);
11. } else {
12. hilog.info(0x0000, 'testTag', 'onCompletedCallback: success.');
13. }
14. };
15. let startupListener: StartupListener = {
16. 'onCompleted': onCompletedCallback
17. };
18. let config: StartupConfig = {
19. 'timeoutMs': 10000,
20. 'startupListener': startupListener
21. };

23. try {
24. // 手动调用run方法
25. startupManager.run(['StartupTask_001', 'libentry_001'], this.context, config).then(() => {
26. hilog.info(0x0000, 'testTag', '%{public}s', 'startupManager.run success');
27. }).catch((error: BusinessError<void>) => {
28. hilog.error(0x0000, 'testTag', `startupManager.run promise catch error code: ${error.code}, error msg: ${error.message}`);
29. })
30. } catch (error) {
31. hilog.error(0x0000, 'testTag', `startupManager.run catch error code: ${error.code}, error msg: ${error.message}`);
32. }
33. }
34. // ...
35. }
```

## startupManager.removeAllStartupTaskResults

PhonePC/2in1TabletTVWearable

removeAllStartupTaskResults(): void

删除所有启动任务结果。

如果存在so预加载任务，则将对应so文件置为未加载状态。对于缓存中已加载的so文件，不会被移除。

**系统能力**：SystemCapability.Ability.AppStartup

**示例：**

```
1. import { AbilityConstant, UIAbility, Want, startupManager } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class EntryAbility extends UIAbility {
7. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
8. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
9. try {
10. startupManager.run(['StartupTask_001', 'libentry_001']).then(() => {
11. hilog.info(0x0000, 'testTag', 'StartupTask_001 init successful');
12. }).catch((error: BusinessError) => {
13. hilog.error(0x0000, 'testTag', `StartupTask_001 promise catch failed, error code: ${error.code}, error msg: ${error.message}`);
14. });
15. } catch (error) {
16. hilog.error(0x0000, 'testTag', `StartupTask_001.run failed, error code: ${error.code}, error msg: ${error.message}`);
17. }
18. }

20. onWindowStageCreate(windowStage: window.WindowStage) {
21. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
22. startupManager.removeAllStartupTaskResults(); // 移除所有启动任务结果

24. windowStage.loadContent('pages/Index', (err, data) => {
25. if (err.code) {
26. hilog.error(0x0000, 'testTag', `Failed to load the content. Cause error code: ${err.code}, error msg: ${err.message}`);
27. return;
28. }
29. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
30. });
31. }
32. }
```

## startupManager.getStartupTaskResult

PhonePC/2in1TabletTVWearable

getStartupTaskResult(startupTask: string): Object

获取指定启动任务或so预加载任务的执行结果。

**系统能力**：SystemCapability.Ability.AppStartup

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startupTask | string | 是 | 启动任务[StartupTask](js-apis-app-appstartup-startuptask.md)的名称或预加载so名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 输入为启动任务名时，返回指定的启动任务[init](js-apis-app-appstartup-startuptask.md#init)返回的执行结果。  输入为so文件名时，返回undefined。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want, startupManager } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class EntryAbility extends UIAbility {
7. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
8. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
9. try {
10. startupManager.run(['StartupTask_001']).then(() => {
11. hilog.info(0x0000, 'testTag', 'StartupTask_001 init successful');
12. }).catch((error: BusinessError) => {
13. hilog.error(0x0000, 'testTag', `StartupTask_001 promise catch failed, error code: ${error.code}, error msg: ${error.message}`);
14. });
15. } catch (error) {
16. hilog.error(0x0000, 'testTag', `StartupTask_001.run failed, error code: ${error.code}, error msg: ${error.message}`);
17. }
18. }

20. onWindowStageCreate(windowStage: window.WindowStage) {
21. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
22. let result = startupManager.getStartupTaskResult('StartupTask_001'); // 手动获取启动任务结果
23. hilog.info(0x0000, 'testTag', 'getStartupTaskResult result = %{public}s', result);
24. windowStage.loadContent('pages/Index', (err, data) => {
25. if (err.code) {
26. hilog.error(0x0000, 'testTag', `Failed to load the content. Cause error code: ${err.code}, error msg: ${err.message}`);
27. return;
28. }
29. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
30. });
31. }
32. }
```

## startupManager.isStartupTaskInitialized

PhonePC/2in1TabletTVWearable

isStartupTaskInitialized(startupTask: string): boolean

获取指定启动任务或so预加载任务是否已初始化。

**系统能力**：SystemCapability.Ability.AppStartup

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startupTask | string | 是 | 启动任务[StartupTask](js-apis-app-appstartup-startuptask.md)的名称或预加载so名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回布尔值，true表示该启动任务或so预加载任务已执行完成，false表示该启动任务或so预加载任务尚未执行完成。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want, startupManager } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class EntryAbility extends UIAbility {
7. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
8. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
9. try {
10. startupManager.run(['StartupTask_001', 'libentry_001']).then(() => {
11. hilog.info(0x0000, 'testTag', 'StartupTask_001 init successful');
12. }).catch((error: BusinessError) => {
13. hilog.error(0x0000, 'testTag', `StartupTask_001 promise catch failed, error code: ${error.code}, error msg: ${error.message}`);
14. });
15. } catch (error) {
16. hilog.error(0x0000, 'testTag', `StartupTask_001.run failed, error code: ${error.code}, error msg: ${error.message}`);
17. }
18. }

20. onWindowStageCreate(windowStage: window.WindowStage) {
21. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
22. let result1 = startupManager.isStartupTaskInitialized('StartupTask_001');
23. let result2 = startupManager.isStartupTaskInitialized('libentry_001');
24. if (result1) {
25. console.info('StartupTask_001 init successful');
26. } else {
27. console.info('StartupTask_001 uninitialized');
28. }
29. if (result2) {
30. console.info('libentry_001 init successful');
31. } else {
32. console.info('libentry_001 uninitialized');
33. }

35. windowStage.loadContent('pages/Index', (err, data) => {
36. if (err.code) {
37. hilog.error(0x0000, 'testTag', `Failed to load the content. Cause error code: ${err.code}, error msg: ${err.message}`);
38. return;
39. }
40. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
41. });
42. }
43. }
```

## startupManager.removeStartupTaskResult

PhonePC/2in1TabletTVWearable

removeStartupTaskResult(startupTask: string): void

删除指定启动任务或so预加载任务的初始化结果。

* 输入为启动任务名时，删除指定启动任务的初始化结果。
* 输入为so文件时，将该so文件置为未加载，缓存中已加载的so文件不会被移除。

**系统能力**：SystemCapability.Ability.AppStartup

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startupTask | string | 是 | 启动任务[StartupTask](js-apis-app-appstartup-startuptask.md)的名称或预加载so名称。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want, startupManager } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class EntryAbility extends UIAbility {
7. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
8. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
9. try{
10. startupManager.run(['StartupTask_001', 'libentry_001']).then(() => {
11. hilog.info(0x0000, 'testTag', 'StartupTask_001 init successful');
12. }).catch((error: BusinessError) => {
13. hilog.error(0x0000, 'testTag', `StartupTask_001 promise catch failed, error code: ${error.code}, error msg: ${error.message}`);
14. });
15. } catch (error) {
16. hilog.error(0x0000, 'testTag', `StartupTask_001.run failed, error code: ${error.code}, error msg: ${error.message}`);
17. }
18. }

20. onWindowStageCreate(windowStage: window.WindowStage) {
21. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
22. startupManager.removeStartupTaskResult('StartupTask_001');
23. startupManager.removeStartupTaskResult('libentry_001');

25. windowStage.loadContent('pages/Index', (err, data) => {
26. if (err.code) {
27. hilog.error(0x0000, 'testTag', `Failed to load the content. Cause error code: ${err.code}, error msg: ${err.message}`);
28. return;
29. }
30. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
31. });
32. }
33. }
```
