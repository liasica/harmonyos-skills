---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/continuous-task
title: 长时任务(ArkTS)
breadcrumb: 指南 > 应用框架 > Background Tasks Kit（后台任务开发服务） > 长时任务(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:10+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:eeeb0756eb0d384a178a6f4ea9ddec0b2d964bd0f44448c55389e55b7f7fd1de
---

## 概述

### 功能介绍

应用退至后台后，在后台需要长时间运行用户可感知的任务，如播放音乐、导航等。为防止应用进程被挂起，导致对应功能异常，可以申请长时任务，使应用在后台长时间运行。在长时任务中，支持同时申请多种类型的任务，也可以对任务类型进行更新。应用退至后台执行业务时，系统会做一致性校验，确保应用在执行相应的长时任务。应用在申请长时任务成功后，通知栏会显示与长时任务相关联的消息，用户删除通知栏消息时，系统会自动停止长时任务。

说明

应用退至后台后，在不同类型设备上生命周期变化存在差异，详见[不同设备生命周期的差异化行为](window-overview.md#不同设备生命周期的差异化行为)。

### 使用场景

下表给出了当前长时任务支持的类型，包含数据传输、音视频播放、录制、定位导航、蓝牙相关业务、多设备互联、音视频通话和计算任务。可以参考下表中的场景举例，选择合适的长时任务类型。

**表1** 长时任务类型

| 参数名 | 描述 | 配置项 | 场景举例 |
| --- | --- | --- | --- |
| DATA\_TRANSFER | 数据传输。 | dataTransfer | 非托管形式的上传、下载，如在浏览器后台上传或下载数据。 |
| AUDIO\_PLAYBACK | 音视频播放。 | audioPlayback | 音频、视频在后台播放，音视频投播。  **说明：** 支持在元服务中使用。 |
| AUDIO\_RECORDING | 录制。 | audioRecording | 录音、录屏退后台。 |
| LOCATION | 定位导航。 | location | 定位、导航。 |
| BLUETOOTH\_INTERACTION | 蓝牙相关业务。 | bluetoothInteraction | 通过蓝牙传输文件时退后台。 |
| MULTI\_DEVICE\_CONNECTION | 多设备互联。 | multiDeviceConnection | 分布式业务连接、投播。  **说明：** 支持在元服务中使用。 |
| VOIP | 音视频通话。  **说明：** 从API version 13开始支持。 | voip | 某些聊天类应用（具有音视频业务）音频、视频通话时退后台。 |
| TASK\_KEEPING | 计算任务。  **说明：** 从API version 21开始，对PC/2in1设备、非PC/2in1设备但申请了ACL权限为[ohos.permission.KEEP\_BACKGROUND\_RUNNING\_SYSTEM](restricted-permissions.md#ohospermissionkeep_background_running_system)的应用开放。 API version 20及之前版本，仅对PC/2in1设备开放。 | taskKeeping | 如杀毒软件。 |
| MODE\_AV\_PLAYBACK\_AND\_RECORD | 多媒体相关业务。  **说明：** 从API version 22开始支持。 | avPlaybackAndRecord | 音视频播放，录制，音视频通话时退后台。在上述三种场景下，选择本类型或对应类型的长时任务均可。例如：音视频播放场景下，选择AUDIO\_PLAYBACK或者MODE\_AV\_PLAYBACK\_AND\_RECORD任意一个即可。 |
| MODE\_SPECIAL\_SCENARIO\_PROCESSING | 特殊场景类型（仅对Phone、Tablet、PC/2in1设备开放）。  **说明：** 从API version 22开始支持。 | specialScenarioProcessing | 在后台进行导出媒体文件，使用三方投播组件在后台进行投播。 |

关于DATA\_TRANSFER（数据传输）说明：

* 在数据传输时，若应用使用[@ohos.request (上传下载)](../harmonyos-references/js-apis-request.md)托管给系统，即使申请DATA\_TRANSFER的后台任务，应用退后台时还是会被挂起。
* 在数据传输时，应用需要更新进度，如果进度长时间（首次更新超过10分钟）未更新，数据传输的长时任务会被取消。更新进度的通知类型必须为实况窗，具体实现可参考[startBackgroundRunning()](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning12)中的示例。

关于AUDIO\_PLAYBACK（音视频播放）说明：

* 音视频投播，是指将一台设备的音视频投至另一台设备播放。投播退至后台，长时任务会检测音视频播放和投屏两个业务，只要有其一正常运行，长时任务就不会终止。
* 当应用需要在后台播放媒体类型（流类型为STREAM\_USAGE\_MUSIC、STREAM\_USAGE\_MOVIE和STREAM\_USAGE\_AUDIOBOOK）和游戏类型（流类型为STREAM\_USAGE\_GAME）时，必须接入媒体会话服务（[AVSession](avsession-overview.md)）并申请AUDIO\_PLAYBACK类型长时任务。
* 除了上述播放类型，针对用户可感知的其他播放任务，如果应用需要在后台长时间运行该任务，必须申请AUDIO\_PLAYBACK类型长时任务，无需接入AVSession。
* 如果应用不满足上述接入规范，退至后台播放时会被系统静音并冻结，无法在后台正常播放，直到应用重新切回前台时，才会解除静音并恢复播放。
* 从API version 20开始，申请AUDIO\_PLAYBACK类型长时任务但不接入AVSession，申请长时任务成功后会在通知栏显示通知；接入AVSession后，后台任务模块不会发送通知栏通知，由AVSession发送通知。对于API version 19及之前的版本，后台任务模块不会在通知栏显示通知。
* 应用申请AUDIO\_PLAYBACK类型长时任务，退至后台时，如果设备没有有效音频播放，应用可能被系统冻结。

关于BLUETOOTH\_INTERACTION（蓝牙相关业务）说明：

如果应用仅申请了蓝牙长时任务，因设备远离等原因导致蓝牙断连，系统将取消应用的蓝牙长时任务。为确保蓝牙接续使用体验，在断连后的一段时间内（具体时长受系统负载影响，最长可达十分钟），系统允许满足如下条件的应用在恢复连接时重新保活，实现在后台长时间运行。

1. 主动注册长时任务暂停监听的事件以避免蓝牙断连之后长时任务被系统直接取消，可参考[on('continuousTaskSuspend')](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanageroncontinuoustasksuspend20)，这样在蓝牙断连时系统不会立即取消长时任务，而是将其标记为暂停态。
2. 为保证在蓝牙断连之后能及时恢复连接，在蓝牙连接之后通过[on('connectionStateChange')](../harmonyos-references/js-apis-bluetooth-ble.md#onconnectionstatechange)订阅蓝牙连接状态变化的事件，断连之后通过[startScan](../harmonyos-references/js-apis-bluetooth-ble.md#startscan15)主动发起BLE蓝牙扫描，订阅BLE设备扫描结果上报[on('BLEDeviceFind')](../harmonyos-references/js-apis-bluetooth-ble.md#onbledevicefind15)事件，检测设备是否重回连接范围。
3. 成功扫描到设备之后，应用需要通过[connect](../harmonyos-references/js-apis-bluetooth-ble.md#connect)主动恢复蓝牙连接，使系统检测到蓝牙恢复连接后重新激活暂停的长时任务，实现重新保活。

### 约束与限制

**申请限制**：Stage模型中，长时任务仅支持UIAbility申请；FA模型中，长时任务仅支持ServiceAbility申请。长时任务支持设备当前应用申请，也支持跨设备或跨应用申请，跨设备或跨应用仅对系统应用开放。

**数量限制**：

* 从API version 21开始，支持一个UIAbility同一时刻申请多个长时任务，最多可申请10个，具体实现可参考[startBackgroundRunning()](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning21)。对于API version 20及之前版本，一个UIAbility（FA模型则为ServiceAbility）同一时刻仅支持申请一个长时任务，即在一个长时任务结束后才能继续申请。如果一个应用同时需要申请多个长时任务，需要创建多个UIAbility。
* 如果一个应用创建了多个UIAbility，一个UIAbility申请长时任务后，整个应用下的所有进程均不会被挂起。

**运行限制**：

* 申请长时任务后，应用未执行相应的业务，系统会对应用进行管控，即应用退至后台会被挂起。如系统检测到应用申请了AUDIO\_PLAYBACK（音视频播放），但实际未播放音乐。
* 申请长时任务后，应用执行的业务类型与申请的不一致，系统会对应用进行管控，即应用退至后台会被挂起。如系统检测到应用只申请了AUDIO\_PLAYBACK（音视频播放），但实际上除了播放音乐（对应AUDIO\_PLAYBACK类型），还在进行录制（对应AUDIO\_RECORDING类型）。
* 申请长时任务后，应用的业务已执行完，系统会对应用进行管控，即应用退至后台会被挂起。
* 若运行长时任务的进程后台负载持续高于所申请类型的典型负载，系统会对应用进行管控，即应用退至后台会被挂起或终止。

说明

应用按需求申请长时任务，当应用无需在后台运行（任务结束）时，要及时主动取消长时任务，否则应用退至后台会被系统挂起。例如用户主动点击音乐暂停播放时，应用需及时取消对应的长时任务；用户再次点击音乐播放时，需重新申请长时任务。

若音频在后台播放时被[打断](audio-playback-concurrency.md)，系统会自行检测和停止长时任务，音频重启播放时，需要再次申请长时任务。

后台播放音频的应用，在停止长时任务的同时，需要暂停或停止音频流，否则应用会被系统强制终止。

## 接口说明

**表2** 主要接口

以下是长时任务开发使用的相关接口，下表均以Promise形式为例，更多接口及使用方式请见[后台任务管理](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md)。

| 接口名 | 描述 |
| --- | --- |
| [startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise<void>](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning-1) | 申请长时任务，本接口一个UIAbility同一时刻仅支持申请一个长时任务，即在一个长时任务结束后才能继续申请。 |
| [stopBackgroundRunning(context: Context): Promise<void>](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstopbackgroundrunning-1) | 取消长时任务。 |
| [startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning21) | 申请多个长时任务。本接口支持一个UIAbility同一时刻申请多个长时任务，最多可申请10个。 |
| [stopBackgroundRunning(context: Context, continuousTaskId: number): Promise<void>](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstopbackgroundrunning21) | 取消指定Id的长时任务。 |

## 开发步骤

本文以申请一个录制长时任务为例，实现如下功能：

* 点击“申请长时任务”按钮，应用申请录制长时任务成功，通知栏显示“正在运行录制任务”通知。
* 点击“取消长时任务”按钮，取消长时任务，通知栏撤销相关通知。

### Stage模型

1. 需要申请ohos.permission.KEEP\_BACKGROUND\_RUNNING权限，配置方式请参见[声明权限](declare-permissions.md)。
2. 声明后台模式类型。

   在[module.json5配置文件](module-configuration-file.md)中abilities下的backgroundModes字段里，为需要使用长时任务的UIAbility声明相应的长时任务类型，配置文件中填写长时任务类型的[配置项](continuous-task.md#使用场景)。

   ```
   1. "module": {
   2. "abilities": [
   3. {
   4. "backgroundModes": [
   5. // 长时任务类型的配置项
   6. "audioRecording",
   7. "bluetoothInteraction",
   8. "audioPlayback"
   9. ]
   10. }
   11. ],
   12. // ...
   13. }
   ```
3. 导入模块。

   长时任务相关的模块为@ohos.resourceschedule.backgroundTaskManager和@ohos.app.ability.wantAgent，其余模块按实际需要导入。

   ```
   1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { wantAgent, WantAgent } from '@kit.AbilityKit';
   4. // 在元服务中，请删除WantAgent导入
   ```
4. 申请和取消长时任务。

   **设备当前应用**申请和取消长时任务示例代码如下：

   从API version 15开始，支持通过[on('continuousTaskCancel')](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanageroncontinuoustaskcancel15)实现监听长时任务取消功能。

   从API version 16开始，支持通过[BackgroundSubMode](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundsubmode16)实现蓝牙车钥匙功能。

   ```
   1. function callback(info: backgroundTaskManager.ContinuousTaskCancelInfo) {
   2. // 长时任务id
   3. console.info('OnContinuousTaskCancel callback id ' + info.id);
   4. // 长时任务取消原因
   5. console.info('OnContinuousTaskCancel callback reason ' + info.reason);
   6. }

   8. @Entry
   9. @Component
   10. struct Index {
   11. @State message: string = 'ContinuousTask';
   12. // 通过getUIContext().getHostContext()方法，来获取page所在的UIAbility上下文
   13. private context: Context | undefined = this.getUIContext().getHostContext();

   15. // ...

   17. OnContinuousTaskCancel() {
   18. try {
   19. backgroundTaskManager.on('continuousTaskCancel', callback);
   20. console.info(`Succeeded in operationing OnContinuousTaskCancel.`);
   21. } catch (error) {
   22. console.error(`Operation OnContinuousTaskCancel failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
   23. }
   24. }

   26. OffContinuousTaskCancel() {
   27. try {
   28. // callback参数不传，则取消所有已注册的回调
   29. backgroundTaskManager.off('continuousTaskCancel', callback);
   30. console.info(`Succeeded in operationing OffContinuousTaskCancel.`);
   31. } catch (error) {
   32. console.error(`Operation OffContinuousTaskCancel failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
   33. }
   34. }

   36. // 申请长时任务.then()写法
   37. startContinuousTask() {
   38. let wantAgentInfo: wantAgent.WantAgentInfo = {
   39. // 点击通知后，将要执行的动作列表
   40. // 添加需要被拉起应用的bundleName和abilityName
   41. wants: [
   42. {
   43. bundleName: 'ohos.samples.continuoustask',
   44. abilityName: 'MainAbility'
   45. }
   46. ],
   47. // 指定点击通知栏消息后的动作是拉起ability
   48. actionType: wantAgent.OperationType.START_ABILITY,
   49. // 使用者自定义的一个私有值
   50. requestCode: 0,
   51. // 点击通知后，动作执行属性
   52. actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG],
   53. // 车钥匙长时任务子类型，从API version 16开始支持。只有申请bluetoothInteraction类型的长时任务，车钥匙子类型才能生效。
   54. // 确保extraInfo参数中的Key值为backgroundTaskManager.BackgroundModeType.SUB_MODE，否则子类型不生效。
   55. // extraInfo: {
   56. // [backgroundTaskManager.BackgroundModeType.SUB_MODE] :backgroundTaskManager.BackgroundSubMode.CAR_KEY
   57. // }
   58. };

   60. try {
   61. // 通过wantAgent模块下getWantAgent方法获取WantAgent对象
   62. // 在元服务中，使用wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: object) => {替换下面一行代码
   63. wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
   64. try {
   65. let list: string[] = ['audioPlayback'];
   66. // let list: string[] = ['bluetoothInteraction']; 长时任务类型包含bluetoothInteraction，CAR_KEY子类型合法
   67. backgroundTaskManager.startBackgroundRunning(this.context, list, wantAgentObj).
   68. then((res: backgroundTaskManager.ContinuousTaskNotification) => {
   69. console.info('Operation startBackgroundRunning succeeded');
   70. // 此处执行具体的长时任务逻辑，如播音等。
   71. // 系统会对业务场景的真实性进行检测，如果没有实际执行对应的业务，系统可能会取消对应的长时任务并挂起应用。
   72. // ...
   73. }).catch((error: BusinessError) => {
   74. console.error(`Failed to Operation startBackgroundRunning. code is ${error.code} message is ${error.message}`);
   75. });
   76. } catch (error) {
   77. console.error(`Failed to Operation startBackgroundRunning. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
   78. }
   79. });
   80. } catch (error) {
   81. console.error(`Failed to Operation getWantAgent. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
   82. }
   83. }

   85. // 取消长时任务.then()写法
   86. stopContinuousTask() {
   87. backgroundTaskManager.stopBackgroundRunning(this.context).then(() => {
   88. console.info(`Succeeded in operationing stopBackgroundRunning.`);
   89. // ...
   90. }).catch((err: BusinessError) => {
   91. console.error(`Failed to operation stopBackgroundRunning. Code is ${err.code}, message is ${err.message}`);
   92. });
   93. }

   95. build() {
   96. Row() {
   97. Column() {
   98. Text('Index')
   99. .fontSize(50)
   100. .fontWeight(FontWeight.Bold)

   102. Button() {
   103. Text('申请长时任务').fontSize(25).fontWeight(FontWeight.Bold)
   104. }
   105. .type(ButtonType.Capsule)
   106. .margin({ top: 10 })
   107. .backgroundColor('#0D9FFB')
   108. .width(250)
   109. .height(40)
   110. .id('applyContinuousTask')
   111. .onClick(() => {
   112. // 通过按钮申请长时任务
   113. this.startContinuousTask();
   114. })

   116. Button() {
   117. Text('取消长时任务').fontSize(25).fontWeight(FontWeight.Bold)
   118. }
   119. .type(ButtonType.Capsule)
   120. .margin({ top: 10 })
   121. .backgroundColor('#0D9FFB')
   122. .width(250)
   123. .height(40)
   124. .id('resetContinuousTask')
   125. .onClick(() => {
   126. // 此处结束具体的长时任务的执行

   128. // 通过按钮取消长时任务
   129. this.stopContinuousTask();
   130. })

   132. Button() {
   133. Text('注册长时任务取消回调').fontSize(25).fontWeight(FontWeight.Bold)
   134. }
   135. .type(ButtonType.Capsule)
   136. .margin({ top: 10 })
   137. .backgroundColor('#0D9FFB')
   138. .width(250)
   139. .height(40)
   140. .onClick(() => {
   141. // 通过按钮注册长时任务取消回调
   142. this.OnContinuousTaskCancel();
   143. })

   145. Button() {
   146. Text('取消注册长时任务取消回调').fontSize(25).fontWeight(FontWeight.Bold)
   147. }
   148. .type(ButtonType.Capsule)
   149. .margin({ top: 10 })
   150. .backgroundColor('#0D9FFB')
   151. .width(250)
   152. .height(40)
   153. .onClick(() => {
   154. // 通过按钮取消注册长时任务取消回调
   155. this.OffContinuousTaskCancel();
   156. })
   157. // ...
   158. }
   159. .width('100%')
   160. }
   161. .height('100%')
   162. }
   163. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/BackGroundTasksKit/ContinuousTask/entry/src/main/ets/pages/Index.ets#L22-L331)
5. 申请和取消长时任务async/await写法。

   **设备当前应用**申请和取消长时任务async/await写法示例代码如下：

   从API version 15开始，支持通过[on('continuousTaskCancel')](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanageroncontinuoustaskcancel15)实现监听长时任务取消功能。

   从API version 16开始，支持通过[BackgroundSubMode](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundsubmode16)实现蓝牙车钥匙功能。

   ```
   1. @Entry
   2. @Component
   3. struct IndexAsyncAndAwait {
   4. @State message: string = 'ContinuousTask';
   5. // 通过getUIContext().getHostContext()方法，来获取page所在的UIAbility上下文
   6. private context: Context | undefined = this.getUIContext().getHostContext();

   8. // ...

   10. // 申请长时任务async/await写法
   11. async startContinuousTask() {
   12. let wantAgentInfo: wantAgent.WantAgentInfo = {
   13. // 点击通知后，将要执行的动作列表
   14. // 添加需要被拉起应用的bundleName和abilityName
   15. wants: [
   16. {
   17. bundleName: 'ohos.samples.continuoustask',
   18. abilityName: 'MainAbility'
   19. }
   20. ],
   21. // 指定点击通知栏消息后的动作是拉起ability
   22. actionType: wantAgent.OperationType.START_ABILITY,
   23. // 使用者自定义的一个私有值
   24. requestCode: 0,
   25. // 点击通知后，动作执行属性
   26. actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG],
   27. // 车钥匙长时任务子类型，从API version 16开始支持。只有申请bluetoothInteraction类型的长时任务，车钥匙子类型才能生效。
   28. // 确保extraInfo参数中的Key值为backgroundTaskManager.BackgroundModeType.SUB_MODE，否则子类型不生效。
   29. // extraInfo: {
   30. // [backgroundTaskManager.BackgroundModeType.SUB_MODE] :backgroundTaskManager.BackgroundSubMode.CAR_KEY
   31. // }
   32. };

   34. try {
   35. // 通过wantAgent模块下getWantAgent方法获取WantAgent对象
   36. // 在元服务中，使用const wantAgentObj: object = await wantAgent.getWantAgent(wantAgentInfo);替换下面一行代码
   37. const wantAgentObj: WantAgent = await wantAgent.getWantAgent(wantAgentInfo);
   38. try {
   39. let list: string[] = ['audioPlayback'];
   40. // let list: string[] = ['bluetoothInteraction']; 长时任务类型包含bluetoothInteraction，CAR_KEY子类型合法
   41. // 在元服务中，let list: Array<string> = ["audioPlayback"];
   42. const res: backgroundTaskManager.ContinuousTaskNotification =
   43. await backgroundTaskManager.startBackgroundRunning(this.context as Context, list, wantAgentObj);
   44. console.info(`Operation startBackgroundRunning succeeded, notificationId: ${res.notificationId}`);
   45. // 此处执行具体的长时任务逻辑，如播音等。
   46. // ...
   47. } catch (error) {
   48. console.error(`Failed to Operation startBackgroundRunning. Code is ${(error as BusinessError).code}, message is ${(error as BusinessError).message}`);
   49. }
   50. } catch (error) {
   51. console.error(`Failed to Operation getWantAgent. Code is ${(error as BusinessError).code}, message is ${(error as BusinessError).message}`);
   52. }
   53. }

   55. // 取消长时任务async/await写法
   56. async stopContinuousTask() {
   57. try {
   58. await backgroundTaskManager.stopBackgroundRunning(this.context);
   59. console.info(`Succeeded in operationing stopBackgroundRunning.`);
   60. // ...
   61. } catch (error) {
   62. console.error(`Failed to operation stopBackgroundRunning. Code is ${(error as BusinessError).code}, message is ${(error as BusinessError).message}`)
   63. }
   64. }

   66. build() {
   67. Row() {
   68. Column() {
   69. Text('Index')
   70. .fontSize(50)
   71. .fontWeight(FontWeight.Bold)

   73. Button() {
   74. Text('申请长时任务').fontSize(25).fontWeight(FontWeight.Bold)
   75. }
   76. .type(ButtonType.Capsule)
   77. .margin({ top: 10 })
   78. .backgroundColor('#0D9FFB')
   79. .width(250)
   80. .height(40)
   81. .id('applyContinuousTask')
   82. .onClick(() => {
   83. // 通过按钮申请长时任务
   84. this.startContinuousTask();
   85. })

   87. Button() {
   88. Text('取消长时任务').fontSize(25).fontWeight(FontWeight.Bold)
   89. }
   90. .type(ButtonType.Capsule)
   91. .margin({ top: 10 })
   92. .backgroundColor('#0D9FFB')
   93. .width(250)
   94. .height(40)
   95. .id('resetContinuousTask')
   96. .onClick(() => {
   97. // 此处结束具体的长时任务的执行

   99. // 通过按钮取消长时任务
   100. this.stopContinuousTask();
   101. })
   102. // ...
   103. }
   104. .width('100%')
   105. }
   106. .height('100%')
   107. }
   108. }
   ```

   [IndexAsyncAndAwait.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/BackGroundTasksKit/ContinuousTask/entry/src/main/ets/pages/IndexAsyncAndAwait.ets#L22-L277)
