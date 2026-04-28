---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-lock-screen-immersive-live-window
title: 锁屏沉浸实况窗
breadcrumb: 最佳实践 > 应用服务 > 锁屏沉浸实况窗
category: best-practices
scraped_at: 2026-04-28T08:20:55+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:f8bbe6ad16f1d11edb9ab0c1992d23daf9add2ffb9b8d78f1ec13b27d5250901
---

## 概述

在实际应用开发中，实时信息的高效呈现始终是提升用户体验的关键。实况窗作为高效的交互组件，有助于用户聚焦并迅速查看、处理任务，具备时段性、时效性、变化性的特征。锁屏沉浸实况窗能够详细展示应用的实时活动状态，将重要信息呈现在锁屏界面上，使用户一目了然，无需解锁屏幕进入应用即可获取最新的活动状态，尤其适合于实时性要求高，需要用户及时了解状态的场景，如动态显示网约车位置的出行打车场景、实时更新外卖进度的即时配送场景、以及在锁屏界面呈现电子登机牌的航班场景等。通过[Live View Kit（实况窗服务）](../harmonyos-guides/live-view-kit-guide.md)协助开发者快速集成实况窗功能，能轻松实现锁屏沉浸式的展示效果。

**图1** 用户获取实时信息界面

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/Lw_dIlPpQu6qjGbV992-vA/zh-cn_image_0000002484414413.png?HW-CC-KV=V1&HW-CC-Date=20260428T002053Z&HW-CC-Expire=86400&HW-CC-Sign=D4DAB664B8D57D875A66A75D38D433706C0C70CD4E4904DA983DEE50BF855695 "点击放大")

当用户退出主界面操作后，可通过下拉通知栏或点击胶囊态实况窗快速获取导航概要；当设备进入锁屏状态时，将进一步展示沉浸式锁屏实况窗界面。这种设计可实现实时获取当前信息，既保证了核心业务流的持续可视化，又实现了用户注意力资源的智能分配。

本文将以车道级导航锁屏沉浸实况窗开发实践为例，介绍锁屏沉浸实况窗的实现原理、开发流程，以及开发过程中常见的问题。

### 开发准备

**图2** 在锁屏页面点击实况窗打开锁屏沉浸实况窗

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/Bh6gjqkxTqeUuD0LLJ3HZw/zh-cn_image_0000002484415005.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002053Z&HW-CC-Expire=86400&HW-CC-Sign=64CA9CDFE0174F144A53C3E7A08EF0A7147CE3182FDF270F75E987EDF47BCF65 "点击放大")

锁屏沉浸实况窗的创建依赖于实况窗功能，用户需要点击实况窗展开完整锁屏沉浸实况窗卡片。因此创建锁屏沉浸实况窗的应用需要申请实况窗权限和锁屏沉浸实况窗权限，详情请参考[Live View Kit（实况窗服务）开发准备](../harmonyos-guides/liveview-preparations.md)。

### 锁屏沉浸实况窗体验

锁屏沉浸实况窗的核心功能在于实时展示关键信息和动态数据。通过高效实时更新机制，确保界面内容与最新状态即时同步，使用户能够随时获取最新资讯。这一功能不仅帮助用户高效掌握重要信息，还提升了应用的可信度和用户体验。在典型应用场景中，车道级导航可以即时更新车辆所在车道和导航信息，音乐应用则可通过更新歌曲信息和封面来提供当前播放的歌曲详情。

**图3** 车道级导航锁屏沉浸实况窗

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/deAEeHSCRhKcjHs10_gtJw/zh-cn_image_0000002484291273.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002053Z&HW-CC-Expire=86400&HW-CC-Sign=D6632365506F039E336BF0EB5AEACD361560AB9D96B1F8693434C9DE6A9F4607 "点击放大")

由于锁屏状态的特殊性，锁屏沉浸实况窗通常为被动更新，因此需要有合理的更新策略。以车道级导航为例，当用户的车辆所在车道发生变化时，应更新车道信息，并定期更新导航信息，以保持锁屏沉浸实况窗内容的新鲜感和实时性，确保用户能够持续获取信息并合理分配注意力资源。

## 实现原理

**图****4 锁屏沉浸实况窗架构图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/KyGO6agfTbKTrWpEfC7uCg/zh-cn_image_0000002309310946.png?HW-CC-KV=V1&HW-CC-Date=20260428T002053Z&HW-CC-Expire=86400&HW-CC-Sign=436B9CC6FEC0CC2CF8CB65E4D87993E371D6DD97FD16D9DBDB27E41F8F4EBBE2 "点击放大")

锁屏沉浸实况窗的创建和更新依赖于[Live View Kit（实况窗服务）](../harmonyos-guides/live-view-kit-guide.md)，具体流程如下：

1. 应用主进程创建实况窗：应用主进程通过调用[Live View Kit（实况窗服务）](../harmonyos-guides/live-view-kit-guide.md)创建实况窗。
2. 关联实况窗和锁屏沉浸实况窗：在创建实况窗时，需在参数中传入[LiveViewLockScreenExtensionAbility](../harmonyos-references/liveview-lock-screen-ability.md)名称，以便将实况窗与锁屏沉浸实况窗关联。此步骤需调用[Live View Kit（实况窗服务）](../harmonyos-guides/live-view-kit-guide.md)中的liveViewManager模块实现，具体实现方法请参阅[开发实况窗场景](../harmonyos-guides/liveview-scenes.md)。
3. 应用主进程接收数据：应用主进程通过后台长时任务接收来自数据源的数据。
4. 应用主进程发布公共事件传递数据源数据。
5. 锁屏沉浸实况窗更新页面：
   1. 锁屏沉浸实况窗订阅相应的公共事件，接收数据源的数据；
   2. 锁屏沉浸实况窗检测到数据更新后，进行页面的更新。

## 锁屏沉浸实况窗创建

### 场景描述

通过LiveView对象与[LiveViewLockScreenExtensionAbility](../harmonyos-references/liveview-lock-screen-ability.md)关联，并通过回调创建锁屏沉浸实况窗，以实现锁屏沉浸实况窗的展示。

### 开发步骤

在创建实况窗时，需在LiveView对象中指定[LiveViewLockScreenExtensionAbility](../harmonyos-references/liveview-lock-screen-ability.md)的名称，以便系统能够正确关联并渲染锁屏沉浸式实况窗。

1. 将[LiveViewLockScreenExtensionAbility](../harmonyos-references/liveview-lock-screen-ability.md)的名称写入创建实况窗时创建的liveView对象中。

   ```
   1. import { liveViewManager } from '@kit.LiveViewKit';
   2. // ...
   3. // Construct live window request body.
   4. let liveView: liveViewManager.LiveView = {
   5. id: 0,
   6. sequence: this.sequence,
   7. // Application scenarios of the live window. NAVIGATION: Navigation.
   8. event: 'NAVIGATION',
   9. liveViewData: {
   10. // Live view capsule related parameters
   11. capsule: {
   12. type: liveViewManager.CapsuleType.CAPSULE_TYPE_TEXT,
   13. status: 1,
   14. icon: 'turn_right_light_square.png',
   15. backgroundColor: this.getStringSync($r('app.string.live_view_background').id),
   16. title: this.getStringSync($r('app.string.live_view_title').id),
   17. },
   18. // Live view card related parameters
   19. primary: {
   20. title: this.getStringSync($r('app.string.live_view_title').id),
   21. content: [{ text: this.getStringSync($r('app.string.live_view_content').id) }],
   22. // Add LiveViewLockScreenExtensionAbility name to build lock screen live view
   23. liveViewLockScreenAbilityName: 'LiveViewExtAbility',
   24. liveViewLockScreenAbilityParameters: { liveViewParameters: '' },
   25. keepTime: 0,
   26. clickAction: await LiveViewUtil.buildWantAgent()
   27. }
   28. }
   29. };
   ```

   [LiveViewUtil.ets](https://gitcode.com/harmonyos_samples/LiveViewLockScreen/blob/master/entry/src/main/ets/utils/LiveViewUtil.ets#L19-L175)
2. 在应用module.json5中配置[LiveViewLockScreenExtensionAbility](../harmonyos-references/liveview-lock-screen-ability.md)的名称。

   ```
   1. "extensionAbilities": [
   2. {
   3. // Keep it consistent with LiveViewLockScreenExtensionAbility name in live view instance
   4. "name": "LiveViewExtAbility",
   5. "type": "liveViewLockScreen",
   6. // LiveViewLockScreenExtensionAbility location
   7. "srcEntry": "./ets/liveview/LiveViewExtAbility.ets",
   8. "exported": false
   9. }
   10. ],
   ```

   [module.json5](https://gitcode.com/harmonyos_samples/LiveViewLockScreen/blob/master/entry/src/main/module.json5#L39-L48)
3. 在[LiveViewLockScreenExtensionAbility](../harmonyos-references/liveview-lock-screen-ability.md)的onSessionCreate()方法中完成锁屏沉浸实况窗页面的创建。

   ```
   1. // Core logic when creating UI session.
   2. onSessionCreate(_want: Want, session: UIExtensionContentSession): void {
   3. // ...
   4. try {
   5. session.loadContent('liveview/LockScreenPage');
   6. } catch (error) {
   7. const err: BusinessError = error as BusinessError;
   8. hilog.error(0x0000, TAG, `Session load content failed. code: ${err.code}, message: ${err.message}`);
   9. }
   10. }
   ```

   [LiveViewExtAbility.ets](https://gitcode.com/harmonyos_samples/LiveViewLockScreen/blob/master/entry/src/main/ets/liveview/LiveViewExtAbility.ets#L83-L141)

## 锁屏沉浸实况窗实时更新

### 场景描述

在通过[LiveViewLockScreenExtensionAbility](../harmonyos-references/liveview-lock-screen-ability.md)生命周期回调创建锁屏沉浸实况窗后，为了满足用户及时获取信息更新的需求，该实况窗需要实时更新。本章节将介绍如何实现锁屏沉浸实况窗的数据实时更新。

**图5** 锁屏沉浸实况窗实时更新

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/DaWLEkBlS66kC0YTL8Wf9w/zh-cn_image_0000002484410785.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002053Z&HW-CC-Expire=86400&HW-CC-Sign=73794618590C54C62FEC5B31308D911025FA87388A6CA478574D9F72DF9A00FF "点击放大")

### 开发步骤

沉浸式实况窗进程与应用主进程之间的数据通信需根据不同场景兼顾实时性和初始化需求。以下是不同场景下的推荐方案：

1. 公共事件方案（适用于多数场景）：通过注册公共事件和监听公共事件的方式，实现锁屏沉浸实况窗进程与应用主进程间的数据通信。
   * 优点：实现简单，支持跨进程广播通信。
   * 缺点：无法获取初始数据。
2. liveViewLockScreenAbilityParameters参数方案（适用于有初始化需求的场景）：将数据携带在liveview对象的liveViewLockScreenAbilityParameters中，锁屏沉浸实况窗启动时可通过want直接获取。
   * 优点：启动时可立即获取初始数据。
   * 缺点：数据不可更新，更新需重启锁屏沉浸实况窗，可能导致闪屏。
3. 文件共享方案（适用于大数据传输场景，谨慎使用）：应用主进程将数据保存至沙箱文件中，在沉浸实况进程中监听文件内容变动以获取数据。
   * 优点：适合大数据量传输，可持久化存储。
   * 缺点：读写文件效率较低，锁屏沉浸实况窗进程无法直接获取沙箱路径，需由应用主进程通过其他方式传入沙箱路径。

综合考虑实现复杂度、性能表现和业务需求，在对初始数据无特殊要求的场景下，推荐开发者采用公共事件方案。该方案在实现难度和功能完整性之间取得了平衡，能够满足大多数场景下的通信需求。

如果开发者对锁屏沉浸实况窗的初始数据有特殊要求，可以结合使用liveViewLockScreenAbilityParameters参数方案和公共事件方案：使用liveViewLockScreenAbilityParameters参数传入初始数据，通过注册和监听公共事件的方式进行后续数据更新。下文将以公共事件方案为例，介绍如何实现锁屏沉浸式实况窗的实时更新。

**图6** 锁屏沉浸实况窗实时更新时序图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/C05yk0UwTtWJ2si07KIQYw/zh-cn_image_0000002343349997.png?HW-CC-KV=V1&HW-CC-Date=20260428T002053Z&HW-CC-Expire=86400&HW-CC-Sign=8094A0439CCB19A80B30B36978A609FE988B3D277F8C7733C9E02E7EC4B35B67 "点击放大")

1. 申请后台长时任务，确保在后台能够发布公共事件以传递更新数据。
   * 在申请后台长时任务之前，需确认应用已在module.json5中声明后台运行权限。

     ```
     1. "requestPermissions": [
     2. {
     3. "name": "ohos.permission.KEEP_BACKGROUND_RUNNING",
     4. "reason": "$string:reason_background",
     5. "usedScene": {
     6. "abilities": [
     7. "EntryAbility"
     8. ],
     9. "when": "always"
     10. }
     11. },
     12. ],
     ```

     [module.json5](https://gitcode.com/harmonyos_samples/LiveViewLockScreen/blob/master/entry/src/main/module.json5#L51-L62)
   * 应用创建长时任务，并声明长时任务类型。

     ```
     1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
     2. // ...
     3. // Internal method to manage background tasks
     4. private startContinuousRunningTask() {
     5. // Configure WantAgent for background operation
     6. let wantAgentInfo: wantAgent.WantAgentInfo = {
     7. wants: [
     8. {
     9. bundleName: 'com.example.mapliveviewsample',
     10. abilityName: 'EntryAbility'
     11. }
     12. ],
     13. actionType: wantAgent.OperationType.START_ABILITY,
     14. requestCode: 0,
     15. actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
     16. };

     18. try {
     19. // Acquire WantAgent for background operations
     20. wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
     21. try {
     22. hilog.info(0x0000, TAG, '%{public}s', 'Operation startBackgroundRunning begin.');
     23. // Required background resource types
     24. const list: string[] = ['location'];
     25. // Request background running permission
     26. if (canIUse('SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask')) {
     27. backgroundTaskManager.startBackgroundRunning(this.context, list, wantAgentObj).then(() => {
     28. hilog.info(0x0000, TAG, '%{public}s', 'Operation startBackgroundRunning succeeded.');
     29. }).catch((error: BusinessError) => {
     30. hilog.error(0x0000, TAG, '%{public}s',
     31. `Failed to Operation startBackgroundRunning. code is ${error.code} message is ${error.message}`);
     32. });
     33. }
     34. } catch (error) {
     35. hilog.error(0x0000, TAG, '%{public}s',
     36. `Failed to Operation startBackgroundRunning. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
     37. }
     38. });
     39. } catch (error) {
     40. hilog.error(0x0000, TAG, '%{public}s',
     41. `Failed to Operation getWantAgent. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
     42. }
     43. }
     ```

     [LiveView.ets](https://gitcode.com/harmonyos_samples/LiveViewLockScreen/blob/master/entry/src/main/ets/utils/LiveView.ets#L18-L178)
2. 发布公共事件传递更新数据到锁屏沉浸实况窗。

   应用在主页面中通过[commonEventManager.publish()](../harmonyos-references/js-apis-commoneventmanager.md#commoneventmanagerpublish)接口发布公共事件'live\_view\_lock\_screen'，并在[CommonEventPublishData](../harmonyos-references/js-apis-inner-commonevent-commoneventpublishdata.md)的parameters属性中附带锁屏沉浸实况窗的创建和更新数据。

   ```
   1. import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
   2. // ...
   3. // Prepare common event data
   4. let options: commonEventManager.CommonEventPublishData = {
   5. data: 'data',
   6. bundleName: 'com.example.mapliveviewsample',
   7. parameters: {
   8. 'laneData': routeData.laneData
   9. }
   10. };
   11. // Publish system event for lock screen updates
   12. commonEventManager.publish('live_view_lock_screen', options, (error: BusinessError) => {
   13. if (error) {
   14. hilog.error(0x0000, TAG, '%{public}s',
   15. `Failed to publish commonEvent. code is ${error.code} message is ${error.message}`);
   16. } else {
   17. hilog.info(0x0000, TAG, '%{public}s', 'Succeeded in publishing commonEvent.')
   18. }
   19. });
   ```

   [LiveView.ets](https://gitcode.com/harmonyos_samples/LiveViewLockScreen/blob/master/entry/src/main/ets/utils/LiveView.ets#L21-L91)
3. 订阅公共事件更新锁屏沉浸实况窗。

   锁屏沉浸实况窗进程在[LiveViewLockScreenExtensionAbility](../harmonyos-references/liveview-lock-screen-ability.md)中，使用[commonEventManager.createSubscriber()](../harmonyos-references/js-apis-commoneventmanager.md#commoneventmanagercreatesubscriber)接口创建主页面创建的公共事件'live\_view\_lock\_screen'的订阅者，通过[AppStorage（应用全局的UI状态存储）](../harmonyos-guides/arkts-appstorage.md)将主页面传递的数据传入LockScreenPage.ets，以实现锁屏沉浸实况窗的创建和更新。

   ```
   1. import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
   2. // ...

   4. // Initialize event subscription.
   5. let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
   6. events: ['live_view_lock_screen'],
   7. publisherBundleName: 'com.example.mapliveviewsample',
   8. priority: 0
   9. };
   10. commonEventManager.createSubscriber(subscribeInfo,
   11. (error: BusinessError, data: commonEventManager.CommonEventSubscriber) => {
   12. if (error) {
   13. hilog.error(0x0000, TAG, '%{public}s',
   14. `Failed to create subscriber. code is ${error.code} message is ${error.message}.`);
   15. return;
   16. }
   17. this.subscriber = data;
   18. hilog.info(0x0000, TAG, '%{public}s', 'Succeeded in creating subscriber.');
   19. // Event handling logic.
   20. commonEventManager.subscribe(this.subscriber,
   21. async (error: BusinessError, data: commonEventManager.CommonEventData) => {
   22. if (error) {
   23. hilog.error(0x0000, TAG, '%{public}s',
   24. `Failed to subscribe commonEvent. code is ${error.code} message is ${error.message}.`);
   25. return;
   26. }
   27. hilog.info(0x0000, TAG, '%{public}s', 'Succeeded in subscribe commonEvent success.');
   28. if (data.parameters) {
   29. let laneData = data.parameters['laneData'] as LaneData;
   30. AppStorage.setOrCreate('laneData', laneData);
   31. hilog.info(0x0000, TAG, '%{public}s', 'Succeeded in receive commonEvent.');
   32. }
   33. });
   34. })
   ```

   [LiveViewExtAbility.ets](https://gitcode.com/harmonyos_samples/LiveViewLockScreen/blob/master/entry/src/main/ets/liveview/LiveViewExtAbility.ets#L23-L131)

## 锁屏沉浸实况窗结束

### 场景描述

当用户实时获取信息的需求结束时，应用应及时关闭实况窗及锁屏沉浸实况窗，以优化设备性能和电池续航，避免不必要功耗问题。

### 开发步骤

为确保结束锁屏沉浸实况窗时可以完整释放系统资源，结束流程需按以下顺序执行：

1. 停止数据源接收：关闭数据输入通道，停止数据采集。本开发实践为结束定时器任务，停止更新车道数据。

   ```
   1. // Clear periodic updates
   2. if (this.updateInterval !== undefined) {
   3. clearInterval(this.updateInterval);
   4. this.updateInterval = undefined;
   5. hilog.info(0x0000, TAG, 'Timer has been cleared');
   6. }
   ```

   [LiveView.ets](https://gitcode.com/harmonyos_samples/LiveViewLockScreen/blob/master/entry/src/main/ets/utils/LiveView.ets#L107-L112)
2. 结束界面更新：停止实况窗和沉浸实况窗的内容更新与展示。

   ```
   1. // Close live view.
   2. public async closeLiveView() {
   3. // Ensure that the sequence is greater than the current live window page.
   4. this.sequence++;
   5. this.defaultLiveView = await this.createPrimaryLiveView();
   6. await liveViewManager.stopLiveView(this.defaultLiveView).then(() => {
   7. this.sequence = 0;
   8. this.defaultLiveView = undefined;
   9. hilog.info(0x0000, TAG, '%{public}s', 'Succeeded in stopping liveView, result: %{public}');
   10. }).catch((error: BusinessError) => {
   11. hilog.error(0x0000, TAG, '%{public}s',
   12. `Failed to stop liveView. Cause code: ${error.code}, message: ${error.message}`);
   13. });
   14. return;
   15. }
   ```

   [LiveViewUtil.ets](https://gitcode.com/harmonyos_samples/LiveViewLockScreen/blob/master/entry/src/main/ets/utils/LiveViewUtil.ets#L74-L89)
3. 清理后台任务：结束关联的后台长时运行任务。

   ```
   1. // Stop background tasks
   2. try {
   3. if (canIUse('SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask')) {
   4. backgroundTaskManager.stopBackgroundRunning(this.context).then(() => {
   5. hilog.info(0x0000, TAG, '%{public}s', 'Operation stopBackgroundRunning succeeded');
   6. }).catch((error: BusinessError) => {
   7. hilog.error(0x0000, TAG, '%{public}s',
   8. `Operation stopBackgroundRunning failed. code is ${error.code} message is ${error.message}`);
   9. });
   10. }
   11. } catch (error) {
   12. hilog.error(0x0000, TAG, '%{public}s',
   13. `Operation stopBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
   14. }
   ```

   [LiveView.ets](https://gitcode.com/harmonyos_samples/LiveViewLockScreen/blob/master/entry/src/main/ets/utils/LiveView.ets#L119-L132)

## 锁屏沉浸实况窗多设备适配

### 场景描述

**图7** 手机折叠态和展开态锁屏沉浸实况窗对比图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/x5Q0b5w0SyGXnV4AthE6lg/zh-cn_image_0000002451295374.png?HW-CC-KV=V1&HW-CC-Date=20260428T002053Z&HW-CC-Expire=86400&HW-CC-Sign=0D17B721AD2CA7574A605142620158EBEE4944A4D213CB251911B0A813ED8A00 "点击放大")

为了适配不同尺寸的实况卡片和多样化的设备形态，沉浸式实况展示应采用自适应的多断点布局方案，以确保在各种产品上能够实现自适应布局。可以参考[断点](bpta-multi-device-responsive-layout.md#section1532120147301)。

锁屏沉浸实况窗在不同设备形态上的布局存在差异，主要体现在手机折叠态与展开态两种显示模式中。在手机展开状态下，锁屏沉浸实况窗的高宽比会减少，页面变得更宽。然而，无论是在哪种形态下，横断点都属于sm断点（[断点的定义](bpta-multi-device-responsive-layout.md#section186821126131515)），因此需要使用基于高宽比的纵断点进行区分，以实现多适配。

### 开发步骤

1. 在[LiveViewLockScreenExtensionAbility](../harmonyos-references/liveview-lock-screen-ability.md)中注册页面布局变化的监听器。

   ```
   1. import { AbilityConstant, UIExtensionContentSession, Want } from '@kit.AbilityKit';
   2. import { display, window } from '@kit.ArkUI';
   3. // ...
   4. try {
   5. // Window size listener.
   6. const extensionWindow = session.getUIExtensionWindowProxy();
   7. extensionWindow.on('windowSizeChange', (windowSize: window.Size) => {
   8. this.updateBreakPoint(windowSize);
   9. });
   10. } catch (error) {
   11. const err: BusinessError = error as BusinessError;
   12. hilog.error(0x0000, TAG, `Session update break point failed. code: ${err.code}, message: ${err.message}`);
   13. }
   ```

   [LiveViewExtAbility.ets](https://gitcode.com/harmonyos_samples/LiveViewLockScreen/blob/master/entry/src/main/ets/liveview/LiveViewExtAbility.ets#L17-L97)
2. 当检测到锁屏沉浸实况窗布局发生变化时，触发纵向断点的重新计算。

   ```
   1. import { display, window } from '@kit.ArkUI';
   2. // ...
   3. // Distinguish page layout using vertical breakpoints.
   4. private updateBreakPoint(windowSize: window.Size): void {
   5. try {
   6. let windowWidthVp: number = windowSize.width / display.getDefaultDisplaySync().densityPixels;
   7. let windowHeightVp: number = windowSize.height / display.getDefaultDisplaySync().densityPixels;
   8. let windowRatio: number = windowWidthVp / windowHeightVp;
   9. let verticalBreakpoint: string = Constants.BREAK_POINT_SM;
   10. // Vertical breakpoints are distinguished by aspect ratio.
   11. if (windowRatio < 0.8) {
   12. verticalBreakpoint = Constants.BREAK_POINT_SM;
   13. } else if (windowRatio > 1.2) {
   14. verticalBreakpoint = Constants.BREAK_POINT_LG;
   15. } else {
   16. verticalBreakpoint = Constants.BREAK_POINT_MD;
   17. }
   18. if (this.verticalBreakpoint !== verticalBreakpoint) {
   19. this.verticalBreakpoint = verticalBreakpoint;
   20. AppStorage.setOrCreate('verticalBreakpoint', this.verticalBreakpoint);
   21. }
   22. hilog.info(0x0000, TAG, `updateBreakpoint ${verticalBreakpoint}`);
   23. } catch (error) {
   24. hilog.error(0x0000, TAG, `updateBreakpoint catch err:`, (error as BusinessError).message);
   25. }
   26. }
   ```

   [LiveViewExtAbility.ets](https://gitcode.com/harmonyos_samples/LiveViewLockScreen/blob/master/entry/src/main/ets/liveview/LiveViewExtAbility.ets#L19-L63)
3. 在 LockScreenPage中采用纵向断点监听机制，根据窗口大小动态切换布局样式。

   ```
   1. @StorageLink('verticalBreakpoint') verticalBreakpoint: string = Constants.BREAK_POINT_SM;
   2. @StorageProp('laneData') laneData: LaneData | undefined = undefined;

   4. build() {
   5. Stack({ alignContent: Alignment.Top }) {
   6. Image(this.verticalBreakpoint === Constants.BREAK_POINT_MD ? $r('app.media.ic_lock') : $r('app.media.ic_lock_md'))
   7. .width('100%')
   8. .height('100%')

   10. Row() {
   11. Stack() {
   12. Image($r('app.media.ic_light'))
   13. .width(this.verticalBreakpoint === Constants.BREAK_POINT_MD ? 73.5 : 106)
   14. .height(this.verticalBreakpoint === Constants.BREAK_POINT_MD ? 36 : 52)
   15. Text(JSON.stringify(this.laneData?.lightTime ?? 90))
   16. .fontColor($r('sys.color.white'))
   17. .fontSize(this.verticalBreakpoint === Constants.BREAK_POINT_MD ? 24 : 30)
   18. .margin({ right: this.verticalBreakpoint === Constants.BREAK_POINT_MD ? 8 : 16 })
   19. }
   20. .alignContent(Alignment.End)
   21. }
   22. .width(this.verticalBreakpoint === Constants.BREAK_POINT_MD ? 73.5 : 106)
   23. .height(this.verticalBreakpoint === Constants.BREAK_POINT_MD ? 36 : 52)
   24. .position({
   25. // Layout based on vertical breakpoint.
   26. right: 20,
   27. top: this.verticalBreakpoint === Constants.BREAK_POINT_MD ? 32 : 25
   28. })
   29. }
   30. .width('100%')
   31. .height('100%')
   32. .alignContent(Alignment.Center)
   33. }
   ```

   [LockScreenPage.ets](https://gitcode.com/harmonyos_samples/LiveViewLockScreen/blob/master/entry/src/main/ets/liveview/LockScreenPage.ets#L22-L54)

## 常见问题

### 应用接入锁屏沉浸实况窗后存在功耗上升现象

当应用接入锁屏沉浸实况窗后，因需实时更新锁屏沉浸实况窗页面，可能会导致功耗上升。其优化策略是采用智能后台更新机制，仅在应用进入后台时触发实况窗的刷新及数据同步。可使用[appManager.getRunningProcessInformation()](../harmonyos-references/js-apis-app-ability-appmanager.md#appmanagergetrunningprocessinformation)接口来获取当前应用运行进程的相关信息，并通过返回的[ProcessInformation](../harmonyos-references/js-apis-inner-application-processinformation.md)模块中的state来判断当前进程的运行状态。

```
1. // Set up periodic state checking
2. this.updateInterval = setInterval(() => {
3. // Monitor application state changes
4. appManager.getRunningProcessInformation().then((data: Array<appManager.ProcessInformation>) => {
5. hilog.info(0x0000, TAG, '%{public}s', 'Success to getRunningProcessInformation');
6. // Handle background state
7. if (data[0].state === appManager.ProcessState.STATE_BACKGROUND) {
8. // ...
9. }
10. }).catch((error: BusinessError) => {
11. hilog.error(0x0000, TAG, '%{public}s',
12. `Failed to getRunningProcessInformation. code is ${error.code} message is ${error.message}`);
13. });
14. }, 1000)
```

[LiveView.ets](https://gitcode.com/harmonyos_samples/LiveViewLockScreen/blob/master/entry/src/main/ets/utils/LiveView.ets#L62-L99)

## 示例代码

* [实现锁屏沉浸实况窗](https://gitcode.com/harmonyos_samples/LiveViewLockScreen)
