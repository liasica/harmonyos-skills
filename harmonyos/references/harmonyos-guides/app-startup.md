---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup
title: 应用启动框架AppStartup
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > Stage模型应用组件 > 应用启动框架AppStartup
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2556d6b75c2fdb4cbf80c1ffce1b5fe7c2c6b56cd822c9416709b026fdc8c16e
---

## 概述

应用启动时通常需要执行一系列初始化启动任务，如果将启动任务都放在[HAP](hap-package.md)的[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)组件的[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)生命周期中，那么只能在主线程中依次执行，不但影响应用的启动速度，而且当启动任务过多时，任务之间复杂的依赖关系还会使得代码难以维护。

AppStartup提供了一种简单高效的应用启动方式，可以支持任务的异步启动，加快应用启动速度。同时，通过在一个配置文件中统一设置多个启动任务的执行顺序以及依赖关系，让执行启动任务的代码变得更加简洁清晰、容易维护。

## 运行机制

启动框架支持以自动模式或手动模式执行启动任务，默认采用自动模式。在构造[AbilityStage](ability-terminology.md#abilitystage)过程中开始加载开发者配置的启动任务，以自动模式执行启动任务。开发者也可以在AbilityStage创建完后调用[startupManager.run](../harmonyos-references/js-apis-app-appstartup-startupmanager.md#startupmanagerrun)方法，执行手动模式的启动任务。

**图1** 启动框架执行时机

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/rUScDWcNTGGzr8hSL6ukBg/zh-cn_image_0000002552797850.png?HW-CC-KV=V1&HW-CC-Date=20260427T233745Z&HW-CC-Expire=86400&HW-CC-Sign=AAF8BCA9E9000967DDF36FE6E25677DD7E6A3810A08BE7BDA76BDCA4D943378A)

## 支持的范围

* HAP：entry类型的HAP支持以自动和手动模式启动。从API version 20开始，feature类型的HAP支持以自动和手动模式启动。
* HSP/HAR: 从API version 18开始，支持在[HSP](in-app-hsp.md)和[HAR](har-package.md)中配置启动任务。HSP和HAR的启动任务、so预加载任务无法主动配置为自动模式，但可以被HAP中自动模式的启动任务、so预加载任务拉起。
* 启动框架从API version 18开始支持配置[应用级so](ability-terminology.md#应用级so)预加载任务，so文件开发可以参考[Node-API](use-napi-process.md)创建Native C++工程。不支持配置[系统级so](ability-terminology.md#系统级so)预加载任务。

## 约束限制

* 使用启动框架必须在[HAP](hap-package.md)的[module.json5配置文件](module-configuration-file.md)中开启启动框架。
* ExtensionAbility组件启动场景单一，使用启动框架会带来额外开销，因此不支持ExtensionAbility组件启动时拉起启动框架。
* 启动任务之间或so预加载任务之间不允许存在循环依赖。

## 开发流程

1. [定义启动框架配置文件](app-startup.md#定义启动框架配置文件)：在资源文件目录下创建并定义启动框架配置文件。

   1. [创建启动框架配置文件](app-startup.md#创建启动框架配置文件)：在资源文件目录下创建启动框架配置文件，并在[module.json5](module-configuration-file.md)配置文件中引用。
   2. [定义启动参数配置](app-startup.md#定义启动参数配置)：在启动框架配置文件中添加启动参数的配置信息。
   3. [定义启动任务配置](app-startup.md#定义启动任务配置)：在启动框架配置文件中添加启动任务的配置信息
   4. [定义预加载so任务配置](app-startup.md#定义预加载so任务配置)：在启动框架配置文件中添加预加载so任务的配置信息。
2. [设置启动参数](app-startup.md#设置启动参数)：在启动参数文件中，设置超时时间和启动任务的监听器等参数。
3. [为每个待初始化功能组件添加启动任务](app-startup.md#为每个待初始化功能组件添加启动任务)：通过实现[StartupTask](../harmonyos-references/js-apis-app-appstartup-startuptask.md)接口，启动框架将会按顺序执行初始化流程。
4. [可选操作](app-startup.md#可选操作)：开发者可以在复杂场景下更精细地控制启动框架的行为。

   * [HSP与HAR中使用启动框架](app-startup.md#hsp与har中使用启动框架)：在HSP与HAR中配置启动任务、so预加载任务。实现跨模块的启动任务依赖管理，提升大型应用的启动效率和代码可维护性。
   * [修改启动模式](app-startup.md#修改启动模式)：将启动任务、so预加载任务修改为手动模式，灵活控制任务执行时机，避免不必要的启动开销。
   * [添加任务匹配规则](app-startup.md#添加任务匹配规则)：根据场景通过匹配规则过滤启动任务。精准控制任务执行范围，避免加载无关任务。
   * [设置启动任务调度阶段](app-startup.md#设置启动任务调度阶段)：设置启动任务的调度阶段，提前执行任务，节省启动时间。

## 定义启动框架配置文件

### 创建启动框架配置文件

1. 在[HAP](hap-package.md)的“resources/base/profile”路径下，新建启动框架配置文件。文件名可以自定义，本文以"startup\_config.json"为例。
2. 在[module.json5配置文件](module-configuration-file.md)的appStartup标签中，添加启动框架配置文件的索引。

   module.json5示例代码如下。

   ```
   1. {
   2. "module": {
   3. "name": "entry",
   4. "type": "entry",
   5. // ···
   6. "appStartup": "$profile:startup_config", // 启动框架的配置文件
   7. // ···
   8. }
   9. }
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/AppStartup/entry/src/main/module.json5#L15-L72)

### 定义启动参数配置

在启动框架配置文件startup\_config.json中，可以添加启动参数的配置信息。

1. 在工程的“ets”目录下创建“startup”文件夹，并在“ets/startup”路径下创建启动参数配置文件。本例中，启动参数配置文件的文件名为StartupConfig.ets。
2. 在启动框架配置文件startup\_config.json中，添加启动参数配置文件的相关信息。

   startup\_config.json文件示例如下：

   ```
   1. {
   2. "startupTasks": [
   3. // 启动任务
   4. ],
   5. "appPreloadHintStartupTasks": [
   6. // 预加载so任务
   7. ],
   8. "configEntry": "./ets/startup/StartupConfig.ets" // 启动参数的配置
   9. }
   ```

**表1** startup\_config.json配置文件标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| startupTasks | 启动任务配置信息，详见[定义启动任务配置](app-startup.md#定义启动任务配置)。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| appPreloadHintStartupTasks | 预加载so任务配置信息，详见[定义预加载so任务配置](app-startup.md#定义预加载so任务配置)。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| configEntry | 启动参数配置文件所在路径。详见[设置启动参数](app-startup.md#设置启动参数)。  **说明：**  - HSP、HAR中不允许配置configEntry字段。  - 如果应用开启了[文件名混淆](source-obfuscation.md#section-enable-filename-obfuscation)，则需要将文件路径添加到保留白名单中。具体操作详见[ArkGuard混淆原理及功能](source-obfuscation.md)的[-keep-file-name](source-obfuscation.md#section-keep-file-name)部分。 | 字符串 | 该标签不可缺省。 |

### 定义启动任务配置

假设当前应用启动框架共包含6个启动任务，任务之间的依赖关系如下图所示。为了便于并发执行启动任务，单个启动任务文件包含的启动任务应尽量单一，本例中每个启动任务对应一个启动任务文件。

**图2** 启动任务依赖关系图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/sdgWI-sjTxedyT0NnYh1Og/zh-cn_image_0000002583437545.png?HW-CC-KV=V1&HW-CC-Date=20260427T233745Z&HW-CC-Expire=86400&HW-CC-Sign=AF115AF5EA090CA8F25807EBF394AD680F6D88DECA084A22D87B8B3B76A6EC8B)

1. 在“ets/startup”路径下，依次创建6个启动任务文件。文件名称必须确保唯一性。本例中的6个文件名分别为StartupTask\_001.ets~StartupTask\_006.ets。
2. 在启动框架配置文件startup\_config.json中，添加启动任务配置。

   startup\_config.json文件示例如下：

   ```
   1. {
   2. "startupTasks": [
   3. {
   4. "name": "StartupTask_001",
   5. "srcEntry": "./ets/startup/StartupTask_001.ets",
   6. "dependencies": [
   7. "StartupTask_002",
   8. "StartupTask_003"
   9. ],
   10. "runOnThread": "taskPool",
   11. "waitOnMainThread": false
   12. },
   13. {
   14. "name": "StartupTask_002",
   15. "srcEntry": "./ets/startup/StartupTask_002.ets",
   16. "dependencies": [
   17. "StartupTask_003",
   18. "StartupTask_004"
   19. ],
   20. "runOnThread": "taskPool",
   21. "waitOnMainThread": false
   22. },
   23. {
   24. "name": "StartupTask_003",
   25. "srcEntry": "./ets/startup/StartupTask_003.ets",
   26. "dependencies": [
   27. "StartupTask_004"
   28. ],
   29. "runOnThread": "taskPool",
   30. "waitOnMainThread": false
   31. },
   32. {
   33. "name": "StartupTask_004",
   34. "srcEntry": "./ets/startup/StartupTask_004.ets",
   35. "runOnThread": "taskPool",
   36. "waitOnMainThread": false
   37. },
   38. {
   39. "name": "StartupTask_005",
   40. "srcEntry": "./ets/startup/StartupTask_005.ets",
   41. "dependencies": [
   42. "StartupTask_006"
   43. ],
   44. "runOnThread": "mainThread",
   45. "waitOnMainThread": true,
   46. "excludeFromAutoStart": true
   47. },
   48. {
   49. "name": "StartupTask_006",
   50. "srcEntry": "./ets/startup/StartupTask_006.ets",
   51. "runOnThread": "mainThread",
   52. "waitOnMainThread": false,
   53. "excludeFromAutoStart": true
   54. }
   55. ],
   56. "appPreloadHintStartupTasks": [
   57. // 预加载so任务
   58. ],
   59. "configEntry": "./ets/startup/StartupConfig.ets"
   60. }
   ```

**表2** startupTasks标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| name | 启动任务名称，可自定义，推荐与类名保持一致。 | 字符串 | 该标签不可缺省。 |
| srcEntry | 启动任务对应的文件路径。  **说明：**  如果应用开启了[文件名混淆](source-obfuscation.md#section-enable-filename-obfuscation)，则需要将文件路径添加到保留白名单中。具体操作详见[ArkGuard混淆原理及功能](source-obfuscation.md)的[-keep-file-name](source-obfuscation.md#section-keep-file-name)部分。 | 字符串 | 该标签不可缺省。 |
| dependencies | 启动任务依赖的其他启动任务的类名数组。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| excludeFromAutoStart | 是否排除自动模式，详细介绍可以查看[修改启动模式](app-startup.md#修改启动模式)。  - true：手动模式。  - false：自动模式。  **说明：**  HSP、HAR中startupTask里的excludeFromAutoStart标签必须配置为true。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| runOnThread | 执行初始化所在的线程。  - mainThread：在主线程中执行。  - taskPool：在异步线程中执行。 | 字符串 | 该标签可缺省，缺省值为mainThread。 |
| waitOnMainThread | 主线程是否需要等待启动框架执行。当runOnThread取值为taskPool时，该字段生效。  - true：主线程等待启动框架执行完之后，才会加载应用首页。  - false：主线程不等待启动任务执行。 | 布尔值 | 该标签可缺省，缺省值为true。 |
| matchRules | 该字段用于筛选需要以自动模式启动的启动任务，加速应用启动过程。适用于快速拉起某个页面的场景，例如，通过桌面卡片、通知或意图调用等方式触发的页面跳转，实现功能服务的一步直达体验。操作指导详见[添加任务匹配规则](app-startup.md#添加任务匹配规则)。  **说明：**  - 从API version 20开始，支持该字段。当前仅支持在HAP中配置该字段。  - 该字段的优先级高于excludeFromAutoStart。如果所有启动任务均匹配失败，则按任务的excludeFromAutoStart配置处理。 | 对象 | 该标签可缺省。 |
| schedulerPhase | 启动任务的调度阶段。操作指导详见[设置启动任务调度阶段](app-startup.md#设置启动任务调度阶段)。  - preAbilityStageLoad：启动任务及其依赖任务在AbilityStage模块加载前调度执行。  - postAbilityStageLoad：启动任务及其依赖任务在AbilityStage模块加载后调度执行。  **说明：**  - 从API version 21开始，支持该字段。当前仅支持在HAP中配置该字段。  - 这里的AbilityStage模块加载指的是AbilityStage.ets文件及其所依赖模块的加载。关于模块加载的详细介绍，请参考[模块化运行加载流程](module-principle.md#模块化运行加载流程)。 | 字符串 | 该标签可缺省，缺省值为postAbilityStageLoad。 |

### 定义预加载so任务配置

假设当前应用启动框架共包含6个so预加载任务，任务之间的依赖关系如下图所示。不建议应用在so文件的加载回调中运行代码逻辑，so文件的加载不宜过长，否则会影响主线程的运行。

**图3** so预加载任务依赖关系图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/iXrjDWBvRxaQSiEzGB7Xow/zh-cn_image_0000002552957500.png?HW-CC-KV=V1&HW-CC-Date=20260427T233745Z&HW-CC-Expire=86400&HW-CC-Sign=8D20FE4FB7FE10C3461A11EFE3B5328A832AD6198F82B19C80BF0BD0A6B4A0A8)

1. 参考[Node-API](use-napi-process.md)创建so文件。本例中的6个so文件名称分别为libentry\_001.so~libentry\_006.so。
2. 在启动框架配置文件startup\_config.json中，添加预加载so任务配置。

   startup\_config.json文件示例如下：

   ```
   1. {
   2. "startupTasks": [
   3. // 启动任务
   4. ],
   5. "appPreloadHintStartupTasks": [
   6. {
   7. "name": "libentry_001",
   8. "srcEntry": "libentry_001.so",
   9. "dependencies": [
   10. "libentry_002",
   11. "libentry_003"
   12. ],
   13. "runOnThread": "taskPool"
   14. },
   15. {
   16. "name": "libentry_002",
   17. "srcEntry": "libentry_002.so",
   18. "dependencies": [
   19. "libentry_003",
   20. "libentry_004"
   21. ],
   22. "runOnThread": "taskPool"
   23. },
   24. {
   25. "name": "libentry_003",
   26. "srcEntry": "libentry_003.so",
   27. "dependencies": [
   28. "libentry_004"
   29. ],
   30. "runOnThread": "taskPool"
   31. },
   32. {
   33. "name": "libentry_004",
   34. "srcEntry": "libentry_004.so",
   35. "runOnThread": "taskPool"
   36. },
   37. {
   38. "name": "libentry_005",
   39. "srcEntry": "libentry_005.so",
   40. "dependencies": [
   41. "libentry_006"
   42. ],
   43. "runOnThread": "taskPool",
   44. "excludeFromAutoStart": true
   45. },
   46. {
   47. "name": "libentry_006",
   48. "srcEntry": "libentry_006.so",
   49. "runOnThread": "taskPool",
   50. "excludeFromAutoStart": true
   51. }
   52. ],
   53. "configEntry": "./ets/startup/StartupConfig.ets"
   54. }
   ```

**表3** appPreloadHintStartupTasks标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| name | 预加载so文件名。 | 字符串 | 该标签不可缺省。 |
| srcEntry | 带后缀预加载so文件名。 | 字符串 | 该标签不可缺省。 |
| dependencies | 预加载任务依赖的其他预加载任务的so名数组。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| excludeFromAutoStart | 是否排除自动模式，详细介绍可以查看[修改启动模式](app-startup.md#修改启动模式)。  - true：手动模式。  - false：自动模式。  **说明：**  HSP、HAR中appPreloadHintStartupTask的excludeFromAutoStart标签必须配置为true。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| runOnThread | 执行预加载所在的线程。  - taskPool：在异步线程中执行。  **说明：**  so预加载只允许在taskPool线程执行。 | 字符串 | 该标签不可缺省。 |
| matchRules | 该字段用于筛选需要以自动模式启动的预加载so任务，加速应用启动过程。适用于快速拉起某个页面的场景，例如，通过桌面卡片、通知或意图调用等方式触发的页面跳转，实现功能服务的一步直达体验。操作指导详见[添加任务匹配规则](app-startup.md#添加任务匹配规则)。  **说明：**  - 从API version 20开始，支持该字段。当前仅支持在HAP中配置该字段。  - 该字段的优先级高于excludeFromAutoStart。如果所有预加载so任务均匹配失败，则按任务的excludeFromAutoStart配置处理。 | 对象 | 该标签可缺省。 |

## 设置启动参数

在启动参数配置文件（本文为“ets/startup/StartupConfig.ets”文件）中，使用[StartupConfigEntry](../harmonyos-references/js-apis-app-appstartup-startupconfigentry.md)接口实现启动框架公共参数的配置，包括超时时间和启动任务的监听器等参数，其中需要用到如下接口：

* [StartupConfig](../harmonyos-references/js-apis-app-appstartup-startupconfig.md)：用于设置任务超时时间和启动框架的监听器。
* [StartupListener](../harmonyos-references/js-apis-app-appstartup-startuplistener.md)：用于监听启动任务是否执行成功。

```
1. import { StartupConfig, StartupConfigEntry, StartupListener } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class MyStartupConfigEntry extends StartupConfigEntry {
6. onConfig() {
7. hilog.info(0x0000, 'testTag', `onConfig`);
8. let onCompletedCallback = (error: BusinessError<void>) => {
9. hilog.info(0x0000, 'testTag', `onCompletedCallback`);
10. if (error) {
11. hilog.error(0x0000, 'testTag', 'onCompletedCallback: %{public}d, message: %{public}s', error.code,
12. error.message);
13. } else {
14. hilog.info(0x0000, 'testTag', `onCompletedCallback: success.`);
15. }
16. };
17. let startupListener: StartupListener = {
18. 'onCompleted': onCompletedCallback
19. };
20. let config: StartupConfig = {
21. 'timeoutMs': 10000,
22. 'startupListener': startupListener
23. };
24. return config;
25. }
26. // ···
27. }
```

[StartupConfig.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/AppStartup/entry/src/main/ets/startup/StartupConfig.ets#L15-L56)

## 为每个待初始化功能组件添加启动任务

上述操作中已完成启动框架配置文件、启动参数的配置，还需要在每个功能组件对应的启动任务文件中，通过实现[StartupTask](../harmonyos-references/js-apis-app-appstartup-startuptask.md)来添加启动任务。其中，需要用到下面的两个方法：

* [init](../harmonyos-references/js-apis-app-appstartup-startuptask.md#init)：启动任务初始化。当该任务依赖的启动任务全部执行完毕，即onDependencyCompleted完成调用后，才会执行init方法对该任务进行初始化。
* [onDependencyCompleted](../harmonyos-references/js-apis-app-appstartup-startuptask.md#ondependencycompleted)：当前任务依赖的启动任务执行完成时，调用该方法。

下面以[startup\_config.json](app-startup.md#定义启动任务配置)中的StartupTask\_001.ets文件为例，示例代码如下。开发者需要分别为每个待初始化功能组件添加启动任务。

说明

由于StartupTask采用了[Sendable协议](arkts-sendable.md#sendable协议)，在继承该接口时，必须添加Sendable注解。

```
1. import { StartupTask, common } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Sendable
5. export default class StartupTask_001 extends StartupTask {
6. constructor() {
7. super();
8. }

10. async init(context: common.AbilityStageContext) {
11. hilog.info(0x0000, 'testTag', 'StartupTask_001 init.');
12. return 'StartupTask_001';
13. }

15. onDependencyCompleted(dependence: string, result: Object): void {
16. hilog.info(0x0000, 'testTag', 'StartupTask_001 onDependencyCompleted, dependence: %{public}s, result: %{public}s',
17. dependence, JSON.stringify(result));
18. }
19. }
```

[StartupTask\_001.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/AppStartup/entry/src/main/ets/startup/StartupTask_001.ets#L15-L35)

## 可选操作

### HSP与HAR中使用启动框架

通常大型应用会有多个[HSP](in-app-hsp.md)和[HAR](har-package.md)，本节将提供一个应用示例，以展示如何在HSP包和HAR包中使用启动框架。该示例应用包括两个HSP包（hsp1、hsp2）和一个HAR包（har1），并且包含启动任务和so预加载任务。

开发步骤如下：

1. 除[HAP](hap-package.md)外，在HSP包和HAR包的“resources/base/profile”目录下创建启动框架配置文件，不同模块可以使用相同文件名，本文以"startup\_config.json"为例。
2. 分别在各个模块的启动框架配置文件startup\_config.json中， 添加对应的配置信息。

   假设当前应用存在的启动任务与so预加载任务如下表所示。

   **表4** 应用启动任务与so预加载任务说明

   | 模块 | 启动任务 | so预加载任务 |
   | --- | --- | --- |
   | entry | HAP\_Task\_01 | libentry\_01 |
   | hsp1 | HSP1\_Task\_01  HSP1\_Task\_02 | libhsp1\_01  libhsp1\_02 |
   | hsp2 | HSP2\_Task\_01 | libhsp2\_01 |
   | har | HAR1\_Task\_01 | libhar1\_01 |

   **图4** 启动任务与so预加载依赖关系图

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/H7B6WdRqT0ym-aU8pE3KDg/zh-cn_image_0000002583477501.png?HW-CC-KV=V1&HW-CC-Date=20260427T233745Z&HW-CC-Expire=86400&HW-CC-Sign=74B2437AAC93F5D22FD0BB57BD7BD31263281982F156750FD7B7ABB9C3E121A8)

   [HAP](hap-package.md)的startup\_config.json可参考[定义启动任务配置](app-startup.md#定义启动任务配置)，HSP与HAR的startup\_config.json文件无法配置"configEntry"字段，以hsp1包配置文件为例，示例如下：

   ```
   1. {
   2. "startupTasks": [
   3. {
   4. "name": "HSP1_Task_01",
   5. "srcEntry": "./ets/startup/HSP1_Task_01.ets",
   6. "dependencies": [
   7. "HSP1_Task_02",
   8. "HAR1_Task_01"
   9. ],
   10. "runOnThread": "taskPool",
   11. "waitOnMainThread": false,
   12. "excludeFromAutoStart": true
   13. }
   14. ],
   15. "appPreloadHintStartupTasks": [
   16. {
   17. "name": "libhsp1_01",
   18. "srcEntry": "libhsp1_01.so",
   19. "dependencies": [
   20. "libhsp1_02",
   21. "libhar1_01"
   22. ],
   23. "runOnThread": "taskPool",
   24. "excludeFromAutoStart": true
   25. }
   26. ]
   27. }
   ```
3. 分别在各个模块的[module.json5配置文件](module-configuration-file.md)的appStartup标签中，添加启动框架配置文件的索引。

   hsp1、hsp2以及har1的module.json5示例代码如下。

   ```
   1. {
   2. "module": {
   3. "name": "hsp1",
   4. "type": "shared",
   5. // ···
   6. "appStartup": "$profile:startup_config", // 启动框架的配置文件
   7. // ···
   8. }
   9. }
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/AppStartup/hsp1/src/main/module.json5#L15-L34)

   ```
   1. {
   2. "module": {
   3. "name": "hsp2",
   4. "type": "shared",
   5. // ···
   6. "appStartup": "$profile:startup_config", // 启动框架的配置文件
   7. // ···
   8. }
   9. }
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/AppStartup/hsp2/src/main/module.json5#L15-L34)

   ```
   1. {
   2. "module": {
   3. "name": "har1",
   4. "type": "har",
   5. // ···
   6. "appStartup": "$profile:startup_config", // 启动框架的配置文件
   7. }
   8. }
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/AppStartup/har1/src/main/module.json5#L15-L29)

其余步骤请参考[设置启动参数](app-startup.md#设置启动参数)和[为每个待初始化功能组件添加启动任务](app-startup.md#为每个待初始化功能组件添加启动任务)章节进行配置。

### 修改启动模式

AppStartup分别提供了自动和手动两种方式来执行启动任务，entry模块中默认采用自动模式，开发者可以根据需要修改为手动模式，HSP与HAR只能配置为手动模式。

* 自动模式：当AbilityStage完成创建后，自动执行启动任务。
* 手动模式：在UIAbility完成创建后手动调用，来执行启动任务与so预加载任务。对于某些使用频率不高的模块，不需要应用最开始启动时就进行初始化。开发者可以选择将该部分启动任务修改为手动模式，在应用启动完成后调用[startupManager.run](../harmonyos-references/js-apis-app-appstartup-startupmanager.md#startupmanagerrun)方法来执行启动任务与so预加载任务。

下面以UIAbility的onCreate生命周期中为例，介绍如何采用手动模式来启动任务，示例代码如下。

```
1. import { AbilityConstant, UIAbility, Want, startupManager } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. // ···

6. export default class EntryAbility extends UIAbility {
7. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
8. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
9. let startParams = ['StartupTask_005', 'StartupTask_006'];
10. try {
11. startupManager.run(startParams).then(() => {
12. console.info(`StartupTest startupManager run then, startParams = ${JSON.stringify(startParams)}.`);
13. }).catch((error: BusinessError) => {
14. console.error(`StartupTest promise catch error, error = ${JSON.stringify(error)}.`);
15. console.error(`StartupTest promise catch error, startParams = ${JSON.stringify(startParams)}.`);
16. })
17. } catch (error) {
18. let errMsg = (error as BusinessError).message;
19. let errCode = (error as BusinessError).code;
20. console.error(`Startup catch error, errCode= ${errCode}.`);
21. console.error(`Startup catch error, errMsg= ${errMsg}.`);
22. }
23. }

25. // ···
26. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/AppStartup/entry/src/main/ets/entryability/EntryAbility.ets#L15-L77)

开发者还可以在页面加载完成后，在页面中调用启动框架手动模式，示例代码如下。

```
1. import { startupManager } from '@kit.AbilityKit';

3. @Entry
4. @Component
5. struct Index {
6. // 请将$r('app.string.manual_mode')替换为实际资源文件，在本示例中该资源文件的value值为"手动模式"
7. @State message: ResourceStr = $r('app.string.manual_mode');
8. @State startParams1: Array<string> = ['StartupTask_006'];
9. @State startParams2: Array<string> = ['libentry_006'];

11. build() {
12. RelativeContainer() {
13. Button(this.message)
14. .id('AppStartup')
15. .fontSize(20)
16. .fontWeight(FontWeight.Bold)
17. .onClick(() => {
18. if (!startupManager.isStartupTaskInitialized('StartupTask_006')) { // 判断是否已经完成初始化
19. startupManager.run(this.startParams1);
20. }
21. if (!startupManager.isStartupTaskInitialized('libentry_006')) {
22. startupManager.run(this.startParams2);
23. }
24. })
25. .alignRules({
26. center: { anchor: '__container__', align: VerticalAlign.Center },
27. middle: { anchor: '__container__', align: HorizontalAlign.Center }
28. })
29. }
30. .height('100%')
31. .width('100%')
32. }
33. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/AppStartup/entry/src/main/ets/pages/Index.ets#L15-L49)

### 添加任务匹配规则

在通过卡片、通知、意图调用等方式拉起某个页面时，为了实现功能服务一步直达，可以通过添加matchRules匹配规则，仅加载与当前场景相关的部分启动任务，无需加载全部默认的自动启动任务，以提高启动性能。

可以通过以下两种方式添加匹配规则：

* 通过matchRules中的uris、actions、insightIntents字段，根据UIAbility启动时的uri、action或意图名称，匹配不同场景启动任务及预加载so任务。
* 如果上述方式不能满足需求，可以通过matchRules中的customization自定义匹配规则。

  **表5** matchRules标签说明

  | 属性名称 | 含义 | 数据类型 | 是否可缺省 | 适用场景 |
  | --- | --- | --- | --- | --- |
  | uris | 表示自动模式执行的任务的uri取值范围。当UIAbility启动时，会将[Want](../harmonyos-references/js-apis-app-ability-want.md)中携带的uri属性，与此处配置的uris数组取值进行匹配。格式为scheme://host/path，uri中的其它内容会被忽略（如port、fragment等）。 | 字符串数组 | 可缺省，缺省值为空。 | 通过特定uri拉起UIAbility的场景。 |
  | actions | 表示自动模式执行的任务的action取值范围。当UIAbility启动时，会将[Want](../harmonyos-references/js-apis-app-ability-want.md)中携带的action属性，与此处配置的actions数组取值进行匹配。 | 字符串数组 | 可缺省，缺省值为空。 | 通过特定action拉起UIAbility的场景。 |
  | insightIntents | 表示自动模式执行的任务的意图名称取值范围。当UIAbility启动时，会将意图名称与此处配置的insightIntents数组取值进行匹配。 | 字符串数组 | 可缺省，缺省值为空。 | 通过特定意图名称拉起UIAbility的场景。 |
  | customization | 表示自动模式执行的任务的自定义规则取值范围。通过实现StartupConfigEntry的[onRequestCustomMatchRule](../harmonyos-references/js-apis-app-appstartup-startupconfigentry.md#onrequestcustommatchrule20)接口返回自定义规则值。当UIAbility启动时，会将自定义规则值与此处配置的customization数组取值进行匹配。  **说明：**  仅支持startupTasks中的任务配置。 | 字符串数组 | 可缺省，缺省值为空。 | 如果使用uris、actions、insightIntents字段无法满足要求，可以使用customization自定义规则。 |

  说明

  + uris、insightIntents、actions、customization任一属性匹配成功即为任务匹配成功。
  + 匹配成功的任务及其依赖任务都将在自动模式执行。
  + 所有任务均匹配失败，则按任务的excludeFromAutoStart配置处理。

下面以uri匹配（action和意图名称类似）和customization匹配来举例，介绍如何实现添加任务匹配规则来筛选启动任务。

**场景1：uri匹配**

假定需要用户点击通知消息跳转到通知详情页面时，仅自动执行StartupTask\_004和libentry\_006任务。若启动通知详情UIAbility时Want中的uri属性为test://com.example.startupdemo/notification，可以通过uri匹配。示例如下：

1. 对[定义启动任务配置](app-startup.md#定义启动任务配置)步骤中的startup\_config.json文件进行修改，增加StartupTask\_004任务和libentry\_006任务的matchRules配置。

   ```
   1. {
   2. "startupTasks": [
   3. {
   4. "name": "StartupTask_004",
   5. "srcEntry": "./ets/startup/StartupTask_004.ets",
   6. "runOnThread": "taskPool",
   7. "waitOnMainThread": false,
   8. "matchRules": {
   9. "uris": [
   10. "test://com.example.startupdemo/notification"
   11. ]
   12. }
   13. },
   14. ],
   15. "appPreloadHintStartupTasks": [
   16. {
   17. "name": "libentry_006",
   18. "srcEntry": "libentry_006.so",
   19. "runOnThread": "taskPool",
   20. "excludeFromAutoStart": true,
   21. "matchRules": {
   22. "uris": [
   23. "test://com.example.startupdemo/notification"
   24. ]
   25. }
   26. }
   27. ],
   28. "configEntry": "./ets/startup/StartupConfig.ets"
   29. }
   ```

**场景2：customization匹配**

假定需要用户点击天气卡片跳转到天气界面时，仅自动执行StartupTask\_006启动任务和excludeFromAutoStart=false配置的预加载so任务。若启动天气UIAbility时Want中传入的自定义参数fromType为card，可以通过customization匹配。示例如下：

1. 对[设置启动参数](app-startup.md#设置启动参数)步骤中的MyStartupConfigEntry.ets文件进行修改，新增[onRequestCustomMatchRule](../harmonyos-references/js-apis-app-appstartup-startupconfigentry.md#onrequestcustommatchrule20)方法。

   ```
   1. import { StartupConfigEntry, Want } from '@kit.AbilityKit';
   2. // ···

   4. export default class MyStartupConfigEntry extends StartupConfigEntry {
   5. // ···
   6. onRequestCustomMatchRule(want: Want): string {
   7. if (want?.parameters?.fromType == 'card') {
   8. return 'ruleCard';
   9. }
   10. return '';
   11. }

   13. }
   ```

   [StartupConfig.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/AppStartup/entry/src/main/ets/startup/StartupConfig.ets#L16-L55)
2. 对[定义启动任务配置](app-startup.md#定义启动任务配置)步骤中的startup\_config.json文件进行修改，增加StartupTask\_006任务的matchRules配置。预加载so任务不支持customization字段，按任务原有的excludeFromAutoStart配置处理。

   ```
   1. {
   2. "startupTasks": [
   3. {
   4. "name": "StartupTask_006",
   5. "srcEntry": "./ets/startup/StartupTask_006.ets",
   6. "runOnThread": "mainThread",
   7. "waitOnMainThread": false,
   8. "excludeFromAutoStart": true,
   9. "matchRules": {
   10. "customization": [
   11. "ruleCard"
   12. ]
   13. }
   14. }
   15. ],
   16. "configEntry": "./ets/startup/StartupConfig.ets"
   17. }
   ```

### 设置启动任务调度阶段

从API version 21开始，支持设置启动任务调度阶段。启动任务默认在AbilityStage模块加载后、[AbilityStage.onCreate](../harmonyos-references/js-apis-app-ability-abilitystage.md#oncreate)生命周期之前开始执行。对于大型应用，AbilityStage模块的加载可能耗时较长，开发者可以将启动任务的schedulerPhase字段配置为preAbilityStageLoad，使启动任务在AbilityStage模块加载前被调度，并在异步线程中与AbilityStage模块加载并发执行，从而缩短应用启动时间。

说明

由于启动任务在AbilityStage模块加载前被调度执行，改变了原有的执行顺序。如果启动任务依赖于AbilityStage模块的加载，可能会导致运行结果不符合预期，请参考[模块加载副作用及优化](arkts-module-side-effects.md)对依赖部分进行适配。

例如，应用首页需要通过网络请求获取Feed流数据，且希望该任务能在异步线程中与AbilityStage模块加载并发执行。假设网络请求任务为[定义启动任务配置](app-startup.md#定义启动任务配置)步骤中的StartupTask\_004，开发步骤如下：

1. 配置任务在AbilityStage模块加载前调度执行。在startup\_config.json文件中，将StartupTask\_004任务的schedulerPhase字段设为preAbilityStageLoad。
2. 配置任务在异步线程中与AbilityStage模块加载并发执行。将StartupTask\_004任务的runOnThread设为taskPool，waitOnMainThread设为false。

```
1. {
2. "startupTasks": [
3. {
4. "name": "StartupTask_004",
5. "srcEntry": "./ets/startup/StartupTask_004.ets",
6. "runOnThread": "taskPool",
7. "waitOnMainThread": false,
8. "schedulerPhase": "preAbilityStageLoad"
9. }
10. ],
11. "configEntry": "./ets/startup/StartupConfig.ets"
12. }
```
