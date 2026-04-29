---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilityconstant
title: @ohos.app.ability.AbilityConstant (Ability相关常量)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.AbilityConstant (Ability相关常量)
category: harmonyos-references
scraped_at: 2026-04-29T13:48:25+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:458cc86299e4b93cc2a67e1f2daddc6a79fc2540b250c239d4681acf4070fa7e
---

AbilityConstant提供Ability相关的枚举，包括应用启动原因[LaunchReason](js-apis-app-ability-abilityconstant.md#launchreason)、上次退出原因[LastExitReason](js-apis-app-ability-abilityconstant.md#lastexitreason)、迁移结果[OnContinueResult](js-apis-app-ability-abilityconstant.md#oncontinueresult)等。

说明

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { AbilityConstant } from '@kit.AbilityKit';
```

## 常量

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Ability.AbilityBase

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| REASON\_MESSAGE\_DESKTOP\_SHORTCUT20+ | string | "ReasonMessage\_DesktopShortcut" | 通过桌面快捷方式启动。开发者如果从[LaunchParam](js-apis-app-ability-abilityconstant.md#launchparam)的launchReasonMessage属性中获取到该字符串，表示UIAbility是通过点击桌面快捷方式启动的。 |

## LaunchParam

PhonePC/2in1TabletTVWearable

启动参数，主要包括Ability启动原因以及上次退出原因。Ability启动时由系统自动传入，开发者无需修改。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| launchReason | [LaunchReason](js-apis-app-ability-abilityconstant.md#launchreason) | 否 | 否 | 枚举类型，表示Ability启动原因（如故障恢复拉起、意图调用拉起、元服务分享拉起等），详见[LaunchReason](js-apis-app-ability-abilityconstant.md#launchreason)。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| launchReasonMessage18+ | string | 否 | 是 | 表示Ability启动的详细原因。  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |
| lastExitReason | [LastExitReason](js-apis-app-ability-abilityconstant.md#lastexitreason) | 否 | 否 | 枚举类型，表示Ability上次退出原因。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| lastExitMessage12+ | string | 否 | 否 | 表示Ability上次退出的详细原因。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| lastExitDetailInfo18+ | [LastExitDetailInfo](js-apis-app-ability-abilityconstant.md#lastexitdetailinfo18) | 否 | 是 | 表示Ability上次退出时的关键运行信息（含进程ID、退出时间戳、RSS内存值等）。  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |
| launchUTCTime23+ | number | 否 | 是 | 表示UIAbility开始启动的UTC时间戳，单位为毫秒。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。  **约束：**  该功能仅在启动UIAbility时生效。对于其他类型的Ability（例如UIExtensionAbility），所获取的启动时间为默认值0。 |
| launchUptime23+ | number | 否 | 是 | 表示UIAbility开始启动时系统已运行的时间（自系统开机启动以来的时间），单位为毫秒。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。  **约束：**  该功能仅在启动UIAbility时生效。对于其他类型的Ability（例如UIExtensionAbility），所获取的启动时间为默认值0。 |

## LaunchReason

PhonePC/2in1TabletTVWearable

Ability启动原因，该类型为枚举，可配合UIAbility的[onCreate(want, launchParam)](js-apis-app-ability-uiability.md#oncreate)方法根据launchParam.launchReason的不同类型执行相应操作。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | 0 | 未知原因。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| START\_ABILITY | 1 | 通过[startAbility](js-apis-inner-application-uiabilitycontext.md#startability)接口启动Ability。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| CALL | 2 | 通过[startAbilityByCall](js-apis-inner-application-uiabilitycontext.md#startabilitybycall)接口启动Ability。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| CONTINUATION | 3 | 跨端迁移启动Ability。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| APP\_RECOVERY | 4 | 设置应用恢复后，应用故障时自动恢复启动Ability。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| SHARE10+ | 5 | 通过元服务分享启动Ability。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| AUTO\_STARTUP11+ | 8 | 通过设置开机自启动来启动Ability。 |
| INSIGHT\_INTENT11+ | 9 | 通过洞察意图来启动Ability。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| PREPARE\_CONTINUATION12+ | 10 | 跨端迁移提前启动Ability。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| PRELOAD20+ | 11 | 表明该UIAbility是通过预加载机制启动的。  **元服务API**：从API version 20开始，该接口支持在元服务中使用。 |

**示例：**

```
1. import { UIAbility, Want, AbilityConstant } from '@kit.AbilityKit';

3. export default class MyAbility extends UIAbility {
4. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
5. if (launchParam.launchReason === AbilityConstant.LaunchReason.START_ABILITY) {
6. console.info('The ability has been started by the way of startAbility.');
7. }
8. }
9. }
```

## LastExitReason

PhonePC/2in1TabletTVWearable

Ability上次退出原因，该类型为枚举，可配合UIAbility的[onCreate()](js-apis-app-ability-uiability.md#oncreate)方法根据launchParam.lastExitReason的不同类型执行相应操作。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | 0 | 未知原因。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| ABILITY\_NOT\_RESPONDING(deprecated) | 1 | Ability组件未响应。  **说明:** 从API version 9开始支持，从API version 10开始废弃，请使用APP\_FREEZE替代。 |
| NORMAL | 2 | 用户主动关闭应用，应用程序正常退出。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。  **说明**：当开发者直接调用[process.exit()](js-apis-process.md#processexitdeprecated)、内核kill命令等非Ability Kit提供的能力强制退出应用进程时，也会返回NORMAL。 |
| CPP\_CRASH10+ | 3 | [进程崩溃](../harmonyos-guides/cppcrash-guidelines.md)导致的应用程序退出。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| JS\_ERROR10+ | 4 | 当应用存在JS语法错误并未被开发者捕获时，触发JS\_ERROR故障，导致应用程序退出。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| APP\_FREEZE10+ | 5 | [应用冻屏](../harmonyos-guides/appfreeze-guidelines.md)导致的应用程序退出。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| PERFORMANCE\_CONTROL10+ | 6 | 因系统性能问题（如设备内存不足）导致的应用程序退出。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。  **说明**：该接口即将废弃，建议使用RESOURCE\_CONTROL替代。 |
| RESOURCE\_CONTROL10+ | 7 | 系统资源使用不当导致的应用程序退出。具体错误原因可以通过[LaunchParam.lastExitMessage](js-apis-app-ability-abilityconstant.md#launchparam)获取，可能原因如下:  - CPU Highload，CPU高负载。  - CPU\_EXT Highload，快速CPU负载检测。  - IO Manage Control，I/O管控。  - App Memory Deterioration，应用内存超限劣化。  - Temperature Control，温度管控。  - Memory Pressure，整机低内存触发按优先级由低到高终止进程。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| UPGRADE10+ | 8 | 应用升级导致的应用程序退出。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| USER\_REQUEST18+ | 9 | 应用程序因多任务中心请求而退出。  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |
| SIGNAL18+ | 10 | 应用程序因收到系统kill指令信号而退出。  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |

**示例：**

```
1. import { UIAbility, Want, AbilityConstant } from '@kit.AbilityKit';

3. export default class MyAbility extends UIAbility {
4. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
5. if (launchParam.lastExitReason === AbilityConstant.LastExitReason.APP_FREEZE) {
6. console.info('The ability has exited last because the ability was not responding.');
7. }
8. if (launchParam.lastExitReason === AbilityConstant.LastExitReason.RESOURCE_CONTROL) {
9. console.info(`The ability has exited last because the rss control, the lastExitReason is ${launchParam.lastExitReason}, the lastExitMessage is ${launchParam.lastExitMessage}.`);
10. }
11. }
12. }
```

## LastExitDetailInfo18+

PhonePC/2in1TabletTVWearable

记录Ability所在进程上次退出时的关键运行信息。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pid | number | 否 | 否 | Ability上次退出所在进程的进程号。  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |
| processName | string | 否 | 否 | Ability上次退出所在进程的名称。  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |
| uid | number | 否 | 否 | Ability上次退出所在应用的UID。  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |
| exitSubReason | number | 否 | 否 | Ability上次退出的子原因。  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |
| exitMsg | string | 否 | 否 | Ability上次退出时所在进程被kill的描述信息。  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |
| rss | number | 否 | 否 | Ability上次退出时所在进程实际占用内存大小，单位KB。  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |
| pss | number | 否 | 否 | Ability上次退出时所在进程实际使用的物理内存大小，单位KB。  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |
| timestamp | number | 否 | 否 | Ability上次退出时的时间戳。  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |
| processState20+ | [appManager.ProcessState](js-apis-app-ability-appmanager.md#processstate10) | 否 | 是 | Ability上次退出时的进程状态。  **元服务API**：从API version 20开始，该接口支持在元服务中使用。 |

说明

建议通过[App Killed](../harmonyos-guides/appkilled-guidelines.md)检测来获取应用异常退出的信息，不再建议使用exitSubReason获取。

exitSubReason取值的含义如下：

* 100：进入户外模式查杀。
* 101：退出户外模式查杀或未申请合理的后台任务，但是后台有大量音频播放，具体错误原因可通过[LaunchParam.lastExitMessage](js-apis-app-ability-abilityconstant.md#launchparam)区分。
* 102：户外模式中查杀或应用未申请合理的后台任务，但是后台有录音，具体错误原因可通过[LaunchParam.lastExitMessage](js-apis-app-ability-abilityconstant.md#launchparam)区分。
* 103：应用后台CPU高负载。
* 105：应用IO超限。
* 106：ION内存泄漏管控或恶意使用后台任务查杀，具体错误原因可通过[LaunchParam.lastExitMessage](js-apis-app-ability-abilityconstant.md#launchparam)区分。
* 107：后台应用内存占用超过检测阈值两倍，其中PSS内存占比最高。
* 108：后台应用内存占用超过特定阈值，其中PSS内存占比最高。
* 110：GPU内存泄漏管控。
* 111：VMA内存泄漏管控。
* 112：句柄泄漏管控。
* 113：线程泄漏管控。
* 114：ASHMEM内存泄漏管控。
* 117：页表泄漏管控。
* 301：GPU内存超限或热清理。
* 3000：冻结异常管控，后台存在不合理订阅导致的回调唤醒。
* 3001：冻结异常管控，后台存在不合理订阅导致应用处理回调卡死。
* 3002：GNSS工作异常清理。
* 3003：蓝牙工作异常清理。
* 3004：RunningLock持锁异常清理。
* 3005：Kernel锁异常清理。
* 3006：省电模式清理。
* 3007：模块高耗电异常清理。
* 3030：应急模式、超级省电模式或睡眠模式的清理，具体错误原因可通过[LaunchParam.lastExitMessage](js-apis-app-ability-abilityconstant.md#launchparam)区分。

**示例**:

```
1. import { UIAbility, Want, AbilityConstant } from '@kit.AbilityKit';

3. export default class MyAbility extends UIAbility {
4. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
5. if (launchParam.lastExitDetailInfo) {
6. console.info(`pid: ${launchParam.lastExitDetailInfo.pid}
7. \n processName: ${launchParam.lastExitDetailInfo.processName}
8. \n uid: ${launchParam.lastExitDetailInfo.uid}
9. \n exitSubReason: ${launchParam.lastExitDetailInfo.exitSubReason}
10. \n exitMsg: ${launchParam.lastExitDetailInfo.exitMsg}
11. \n rss: ${launchParam.lastExitDetailInfo.rss}
12. \n pss: ${launchParam.lastExitDetailInfo.pss}
13. \n timestamp: ${launchParam.lastExitDetailInfo.timestamp}
14. \n processState: ${launchParam.lastExitDetailInfo.processState}.`
15. );
16. }
17. }
18. }
```

## OnContinueResult

PhonePC/2in1TabletTVWearable

Ability迁移结果，该类型为枚举，可配合UIAbility的[onContinue()](js-apis-app-ability-uiability.md#oncontinue)方法完成相应的返回。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AGREE | 0 | 表示同意。 |
| REJECT | 1 | 表示拒绝：如应用在[onContinue](js-apis-app-ability-uiability.md#oncontinue)中异常会导致迁移以后数据恢复时显示异常，则可以返回REJECT。 |
| MISMATCH | 2 | 表示版本不匹配：迁移发起端应用可以在[onContinue](js-apis-app-ability-uiability.md#oncontinue)中获取到迁移目标端应用的版本号，进行协商后，如果版本不匹配导致无法迁移，可以返回该结果。 |

**示例：**

```
1. import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

3. export default class MyAbility extends UIAbility {
4. onContinue(wantParam: Record<string, Object>) {
5. return AbilityConstant.OnContinueResult.AGREE;
6. }
7. }
```

## MemoryLevel

PhonePC/2in1TabletTVWearable

整机可用内存级别，该类型为枚举，可配合UIAbility的[onMemoryLevel()](js-apis-app-ability-ability.md#abilityonmemorylevel)方法根据level执行不同内存级别的相应操作。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MEMORY\_LEVEL\_MODERATE | 0 | 表示整机可用内存适中。由于整机内存水线的不同，在不同产品上的表现可能存在差异，参见下方说明。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| MEMORY\_LEVEL\_LOW | 1 | 表示整机可用内存低。由于整机内存水线的不同，在不同产品上的表现可能存在差异，参见下方说明。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| MEMORY\_LEVEL\_CRITICAL | 2 | 表示整机可用内存极低。由于整机内存水线的不同，在不同产品上的表现可能存在差异，参见下方说明。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |

说明

* 不同产品的触发条件可能存在差异。以12G内存的标准设备为例：
  + 当整机可用内存下降至1700MB~1800MB时，会触发取值为0的onMemoryLevel回调，表示当前整机可用内存适中。
  + 当整机可用内存下降至1600MB~1700MB时，会触发取值为1的onMemoryLevel回调，表示当前整机可用内存偏低。
  + 当整机可用内存下降至1600MB以下时，会触发取值为2的onMemoryLevel回调，表示当前整机可用内存很低。

**示例：**

```
1. import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

3. export default class MyAbility extends UIAbility {
4. onMemoryLevel(level: AbilityConstant.MemoryLevel) {
5. if (level === AbilityConstant.MemoryLevel.MEMORY_LEVEL_CRITICAL) {
6. console.info('The memory of device is critical, please release some memory.');
7. }
8. }
9. }
```

## WindowMode12+

PhonePC/2in1TabletTVWearable

启动UIAbility时窗口的创建模式，类型为枚举。可配合[startAbility](js-apis-inner-application-uiabilitycontext.md#startability-2)方法使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WINDOW\_MODE\_FULLSCREEN | 1 | 全屏模式。仅在2in1和Tablet设备上生效。 |
| WINDOW\_MODE\_SPLIT\_PRIMARY | 100 | 支持应用内拉起Ability时设置为分屏，左侧分屏。仅在折叠屏和Tablet设备上生效。 |
| WINDOW\_MODE\_SPLIT\_SECONDARY | 101 | 支持应用内拉起Ability时设置为分屏，右侧分屏。仅在折叠屏和Tablet设备上生效。 |

**示例：**

```
1. import { UIAbility, StartOptions, Want, AbilityConstant } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let targetWant: Want = {
5. bundleName: 'com.example.myapplication',
6. abilityName: 'EntryAbility'
7. };
8. let option: StartOptions = {
9. windowMode: AbilityConstant.WindowMode.WINDOW_MODE_SPLIT_PRIMARY
10. };

12. // 确保从上下文获取到context
13. export default class MyAbility extends UIAbility {
14. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
15. this.context.startAbility(targetWant, option).then(() => {
16. console.info('Succeed to start ability.');
17. }).catch((error: BusinessError) => {
18. console.error(`Failed to start ability with error: ${JSON.stringify(error)}`);
19. });
20. }
21. }
```

## OnSaveResult

PhonePC/2in1TabletTVWearable

保存应用数据的结果，该类型为枚举。配合UIAbility的[onSaveState()](js-apis-app-ability-uiability.md#onsavestate)方法使用，可以实现[UIAbility备份恢复](../harmonyos-guides/ability-recover-guideline.md)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALL\_AGREE | 0 | 总是同意保存状态。 |
| CONTINUATION\_REJECT | 1 | 拒绝迁移保存状态。 |
| CONTINUATION\_MISMATCH | 2 | 迁移不匹配。 |
| RECOVERY\_AGREE | 3 | 同意恢复保存状态。 |
| RECOVERY\_REJECT | 4 | 拒绝恢复保存状态。 |
| ALL\_REJECT | 5 | 总是拒绝保存状态。 |

**示例：**

```
1. import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

3. export default class MyAbility extends UIAbility {
4. onSaveState(reason: AbilityConstant.StateType, wantParam: Record<string, Object>) {
5. return AbilityConstant.OnSaveResult.ALL_AGREE;
6. }
7. }
```

## StateType

PhonePC/2in1TabletTVWearable

保存应用数据场景原因，该类型为枚举。配合UIAbility的[onSaveState()](js-apis-app-ability-uiability.md#onsavestate)方法使用，可以实现[UIAbility备份恢复](../harmonyos-guides/ability-recover-guideline.md)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONTINUATION | 0 | 应用迁移场景。 |
| APP\_RECOVERY | 1 | 应用故障恢复场景。 |

**示例：**

```
1. import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

3. export default class MyAbility extends UIAbility {
4. onSaveState(reason: AbilityConstant.StateType, wantParam: Record<string, Object>) {
5. if (reason === AbilityConstant.StateType.CONTINUATION) {
6. console.info('Save the ability data when the ability is continuing.');
7. }
8. return AbilityConstant.OnSaveResult.ALL_AGREE;
9. }
10. }
```

## ContinueState10+

PhonePC/2in1TabletTVWearable

流转状态枚举值。用于表示当前应用任务流转的状态。可配合[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)的[setMissionContinueState](js-apis-inner-application-uiabilitycontext.md#setmissioncontinuestate10)方法进行设置。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACTIVE | 0 | 指示当前应用任务流转处于激活状态。 |
| INACTIVE | 1 | 指示当前应用任务流转处于未激活状态。 |

**示例：**

```
1. import { UIAbility, Want, AbilityConstant } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class MyAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
6. this.context.setMissionContinueState(AbilityConstant.ContinueState.INACTIVE, (result: BusinessError) => {
7. console.info(`setMissionContinueState: ${JSON.stringify(result)}`);
8. });
9. }
10. }
```

## CollaborateResult18+

PhonePC/2in1TabletTVWearable

应用协同状态，该类型为枚举。用于多设备场景下，调用方应用拉起协同方应用时，协同方应用是否接受协同。需要配合UIAbility的[onCollaborate()](js-apis-app-ability-uiability.md#oncollaborate18)方法进行设置。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACCEPT | 0 | 接受协同。 |
| REJECT | 1 | 拒绝协同。 |

**示例：**

```
1. import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

3. export default class MyAbility extends UIAbility {
4. onCollaborate(wantParam: Record<string, Object>) {
5. return AbilityConstant.CollaborateResult.ACCEPT;
6. }
7. }
```

## PrepareTermination15+

PhonePC/2in1TabletTVWearable

应用准备关闭时返回的动作，该类型为枚举。需要配合[AbilityStage](js-apis-app-ability-abilitystage.md)的[onPrepareTermination](js-apis-app-ability-abilitystage.md#onpreparetermination15)或者[onPrepareTerminationAsync](js-apis-app-ability-abilitystage.md#onprepareterminationasync15)方法使用。

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TERMINATE\_IMMEDIATELY | 0 | 表示立即执行结束动作，默认值。 |
| CANCEL | 1 | 表示取消结束动作。 |

**示例：**

```
1. import { AbilityConstant, AbilityStage } from '@kit.AbilityKit';

3. export default class MyAbilityStage extends AbilityStage {
4. onPrepareTermination(): AbilityConstant.PrepareTermination {
5. console.info('MyAbilityStage.onPrepareTermination is called');
6. return AbilityConstant.PrepareTermination.CANCEL;
7. }
8. }
```
