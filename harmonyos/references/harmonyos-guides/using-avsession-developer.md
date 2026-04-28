---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-avsession-developer
title: 媒体会话提供方
breadcrumb: 指南 > 媒体 > AVSession Kit（音视频播控服务） > 本地媒体会话 > 媒体会话提供方
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:baac514c735ce32ac1604a4b6e89ab011b1bca9f8b0ec4380c597abd76ce5bba
---

音视频应用在实现音视频功能的同时，需要作为媒体会话提供方接入媒体会话，在媒体会话控制方（例如播控中心）中展示媒体相关信息，并响应媒体会话控制方下发的播控命令。

## 基本概念

* 媒体会话元数据（AVMetadata）： 用于描述媒体数据相关属性，包含标识当前媒体的ID（assetId），上一首媒体的ID（previousAssetId），下一首媒体的ID（nextAssetId），标题（title），专辑作者（author），专辑名称（album），词作者（writer），媒体时长（duration）等属性。
* 媒体播放状态（AVPlaybackState）：用于描述媒体播放状态的相关属性，包含当前媒体的播放状态（state）、播放位置（position）、播放倍速（speed）、缓冲时间（bufferedTime）、循环模式（loopMode）、是否收藏（isFavorite）、正在播放的媒体Id（activeItemId）、自定义媒体数据（extras）等属性。

## 接口说明

媒体会话提供方使用的关键接口如下表所示。接口返回值有两种返回形式：callback和promise，下表中为callback形式接口，promise和callback只是返回值方式不一样，功能相同。

更多API说明请参考文档：[模块描述](../harmonyos-references/arkts-apis-avsession.md)。

| 接口名 | 说明 |
| --- | --- |
| createAVSession(context: Context, tag: string, type: AVSessionType, callback: AsyncCallback<AVSession>): void10+ | 创建媒体会话。  一个UIAbility只能存在一个媒体会话，重复创建会失败。 |
| setAVMetadata(data: AVMetadata, callback: AsyncCallback<void>): void10+ | 设置媒体会话元数据。 |
| setAVPlaybackState(state: AVPlaybackState, callback: AsyncCallback<void>): void10+ | 设置媒体会话播放状态。 |
| setLaunchAbility(ability: WantAgent, callback: AsyncCallback<void>): void10+ | 设置启动UIAbility。 |
| getController(callback: AsyncCallback<AVSessionController>): void10+ | 获取当前会话自身控制器。 |
| getOutputDevice(callback: AsyncCallback<OutputDeviceInfo>): void10+ | 获取播放设备相关信息。 |
| activate(callback: AsyncCallback<void>): void10+ | 激活媒体会话。 |
| deactivate(callback: AsyncCallback<void>): void10+ | 禁用当前会话。 |
| destroy(callback: AsyncCallback<void>): void10+ | 销毁媒体会话。 |
| setAVQueueItems(items: Array<AVQueueItem>, callback: AsyncCallback<void>): void 10+ | 设置媒体播放列表。 |
| setAVQueueTitle(title: string, callback: AsyncCallback<void>): void10+ | 设置媒体播放列表名称。 |
| dispatchSessionEvent(event: string, args: {[key: string]: Object}, callback: AsyncCallback<void>): void10+ | 设置会话内自定义事件。 |
| setExtras(extras: {[key: string]: Object}, callback: AsyncCallback<void>): void10+ | 设置键值对形式的自定义媒体数据包。 |
| getOutputDeviceSync(): OutputDeviceInfo10+ | 使用同步方法获取当前输出设备信息。 |

## 开发步骤

音视频应用作为媒体会话提供方接入媒体会话的基本步骤如下所示：

1. 通过AVSessionManager的方法创建并激活媒体会话。

   说明

   以下示例代码仅展示创建AVSession对象的接口调用，应用在真正使用时，需要确保AVSession对象实例在应用后台播放业务活动期间一直存在，避免被系统回收、释放，导致后台发声时被系统管控。

   ```
   1. import { avSession as AVSessionManager } from '@kit.AVSessionKit';
   2. // ...

   4. @Entry
   5. @Component
   6. struct Index {
   7. @State message: string = 'hello world';
   8. // ...

   10. build() {
   11. Column() {
   12. // ...
   13. Text(this.message)
   14. .onClick(async () => {
   15. try {
   16. // 开始创建并激活媒体会话。
   17. // 创建session。
   18. let context = this.getUIContext().getHostContext() as Context;
   19. let type: AVSessionManager.AVSessionType = 'audio';
   20. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
   21. await session.activate();
   22. console.info(`session create done : sessionId : ${session.sessionId}`);
   23. // ...
   24. } catch (err) {
   25. if (err) {
   26. console.error(`AVSession create Error: Code: ${err.code}, message: ${err.message}`);
   27. // ...
   28. }
   29. }
   30. })
   31. }
   32. .width('100%')
   33. .height('100%')
   34. }
   35. }
   ```
2. 跟随媒体信息的变化，及时设置媒体会话信息。需要设置的媒体会话信息主要包括：

   * 媒体会话元数据AVMetadata。
   * 媒体播放状态AVPlaybackState。

   音视频应用设置的媒体会话信息，会被媒体会话控制方通过AVSessionController相关方法获取后进行显示或处理。

   ```
   1. import { avSession as AVSessionManager } from '@kit.AVSessionKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. // ...

   5. @Entry
   6. @Component
   7. struct Index {
   8. @State message: string = 'hello world';
   9. // ...

   11. build() {
   12. Column() {
   13. // ...
   14. Text(this.message)
   15. .onClick(async () => {
   16. let context = this.getUIContext().getHostContext() as Context;
   17. // 假设已经创建了一个session，如何创建session可以参考之前的案例。
   18. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', 'audio');
   19. // 播放器逻辑··· 引发媒体信息与播放状态的变更。
   20. // 设置必要的媒体信息。
   21. let metadata: AVSessionManager.AVMetadata = {
   22. assetId: '0', // 由应用指定，用于标识应用媒体库里的媒体。
   23. title: 'TITLE',
   24. mediaImage: 'IMAGE',
   25. artist: 'ARTIST'
   26. };
   27. session.setAVMetadata(metadata).then(() => {
   28. console.info(`SetAVMetadata successfully`);
   29. // ...
   30. }).catch((err: BusinessError) => {
   31. console.error(`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}`);
   32. // ...
   33. });
   34. // 简单设置一个播放状态 - 暂停 未收藏。
   35. let playbackState: AVSessionManager.AVPlaybackState = {
   36. state: AVSessionManager.PlaybackState.PLAYBACK_STATE_PAUSE,
   37. isFavorite: false
   38. };
   39. session.setAVPlaybackState(playbackState, (err) => {
   40. if (err) {
   41. console.error(`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}`);
   42. // ...
   43. } else {
   44. console.info(`SetAVPlaybackState successfully`);
   45. // ...
   46. }
   47. });
   48. // 设置一个播放列表。
   49. let queueItemDescription1: AVSessionManager.AVMediaDescription = {
   50. assetId: '001',
   51. title: 'music_name',
   52. subtitle: 'music_sub_name',
   53. description: 'music_description',
   54. mediaImage: 'PIXELMAP_OBJECT',
   55. extras: { 'extras': 'any' }
   56. };
   57. let queueItem1: AVSessionManager.AVQueueItem = {
   58. itemId: 1,
   59. description: queueItemDescription1
   60. };
   61. let queueItemDescription2: AVSessionManager.AVMediaDescription = {
   62. assetId: '002',
   63. title: 'music_name',
   64. subtitle: 'music_sub_name',
   65. description: 'music_description',
   66. mediaImage: 'PIXELMAP_OBJECT',
   67. extras: { 'extras': 'any' }
   68. };
   69. let queueItem2: AVSessionManager.AVQueueItem = {
   70. itemId: 2,
   71. description: queueItemDescription2
   72. };
   73. let queueItemsArray = [queueItem1, queueItem2];
   74. session.setAVQueueItems(queueItemsArray).then(() => {
   75. console.info(`SetAVQueueItems successfully`);
   76. // ...
   77. }).catch((err: BusinessError) => {
   78. console.error(`Failed to set AVQueueItem, error code: ${err.code}, error message: ${err.message}`);
   79. // ...
   80. });
   81. // 设置媒体播放列表名称。
   82. let queueTitle = 'QUEUE_TITLE';
   83. session.setAVQueueTitle(queueTitle).then(() => {
   84. console.info(`SetAVQueueTitle successfully`);
   85. // ...
   86. }).catch((err: BusinessError) => {
   87. console.error(`Failed to set AVQueueTitle, error code: ${err.code}, error message: ${err.message}`);
   88. // ...
   89. });
   90. // ...
   91. })
   92. }
   93. .width('100%')
   94. .height('100%')
   95. }
   96. }
   ```
3. 设置用于被媒体会话控制方拉起的UIAbility。当用户操作媒体会话控制方的界面时，例如点击播控中心的卡片，可以拉起此处配置的UIAbility。

   设置UIAbility时通过WantAgent接口实现，更多关于WantAgent的信息请参考[WantAgent](../harmonyos-references/js-apis-app-ability-wantagent.md)。

   ```
   1. import { avSession as AVSessionManager } from '@kit.AVSessionKit';
   2. import { wantAgent } from '@kit.AbilityKit';

   4. @Entry
   5. @Component
   6. struct Index {
   7. @State message: string = 'hello world';

   9. build() {
   10. Column() {
   11. Text(this.message)
   12. .onClick(async () => {
   13. let context = this.getUIContext().getHostContext() as Context;
   14. let type: AVSessionManager.AVSessionType = 'audio';
   15. // 假设已经创建了一个session，如何创建session可以参考之前的案例。
   16. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
   17. let wantAgentInfo: wantAgent.WantAgentInfo = {
   18. wants: [
   19. {
   20. bundleName: 'com.example.musicdemo',
   21. abilityName: 'MainAbility'
   22. }
   23. ],
   24. // OperationType.START_ABILITIES
   25. operationType: 2,
   26. requestCode: 0,
   27. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
   28. }
   29. wantAgent.getWantAgent(wantAgentInfo).then((agent) => {
   30. session.setLaunchAbility(agent);
   31. })
   32. // ...
   33. })
   34. }
   35. .width('100%')
   36. .height('100%')
   37. }
   38. }
   ```
4. 设置一个即时的自定义会话事件，以供媒体控制方接收到事件后进行相应的操作。

   说明

   通过dispatchSessionEvent方法设置的数据不会保存在会话对象或AVSession服务中。

   ```
   1. import { avSession as AVSessionManager } from '@kit.AVSessionKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. // ...

   5. @Entry
   6. @Component
   7. struct Index {
   8. @State message: string = 'hello world';
   9. // ...

   11. build() {
   12. Column() {
   13. // ...
   14. Text(this.message)
   15. .onClick(async () => {
   16. let context = this.getUIContext().getHostContext() as Context;
   17. // 假设已经创建了一个session，如何创建session可以参考之前的案例。
   18. let type: AVSessionManager.AVSessionType = 'audio';
   19. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
   20. let eventName = 'dynamic_lyric';
   21. await session.dispatchSessionEvent(eventName, { lyric: 'This is my lyric' }).then(() => {
   22. console.info(`Dispatch session event successfully`);
   23. // ...
   24. }).catch((err: BusinessError) => {
   25. console.error(`Failed to dispatch session event. Code: ${err.code}, message: ${err.message}`);
   26. // ...
   27. })
   28. // ...
   29. })
   30. }
   31. .width('100%')
   32. .height('100%')
   33. }
   34. }
   ```
5. 设置与当前会话相关的自定义媒体数据包，以供媒体控制方接收到事件后进行相应的操作。

   说明

   通过setExtras方法设置的数据包会被存储在AVSession服务中，数据的生命周期与会话一致；会话对应的Controller可以使用getExtras来获取该数据。

   ```
   1. import { avSession as AVSessionManager } from '@kit.AVSessionKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. // ...

   5. @Entry
   6. @Component
   7. struct Index {
   8. @State message: string = 'hello world';
   9. // ...

   11. build() {
   12. Column() {
   13. // ...
   14. Text(this.message)
   15. .onClick(async () => {
   16. let context = this.getUIContext().getHostContext() as Context;
   17. // 假设已经创建了一个session，如何创建session可以参考之前的案例。
   18. let type: AVSessionManager.AVSessionType = 'audio';
   19. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
   20. await session.setExtras({ extra: 'This is my custom media packet' }).then(() => {
   21. console.info(`Set extras successfully`);
   22. // ...
   23. }).catch((err: BusinessError) => {
   24. console.error(`Failed to set extras. Code: ${err.code}, message: ${err.message}`);
   25. // ...
   26. })
   27. // ...
   28. })
   29. }
   30. .width('100%')
   31. .height('100%')
   32. }
   33. }
   ```
6. 注册播控命令事件监听，便于响应用户通过媒体会话控制方，例如播控中心，下发的播控命令。

   在Session侧注册的监听分为固定播控命令和高级播控事件两种。

   6.1 固定控制命令的监听。

   说明

   媒体会话提供方在注册相关固定播控命令事件监听时，监听的事件会在媒体会话控制方的getValidCommands()方法中体现，即媒体会话控制方会认为对应的方法有效，进而根据需要触发相应暂不使用时的事件。为了保证媒体会话控制方下发的播控命令可以被正常执行，媒体会话提供方请勿进行无逻辑的空实现监听。

   Session侧的固定播控命令主要包括播放、暂停、上一首、下一首等基础操作命令，详细介绍请参见[AVControlCommand](../harmonyos-references/arkts-apis-avsession-i.md#avcontrolcommand10)。

   ```
   1. import { avSession as AVSessionManager } from '@kit.AVSessionKit';
   2. // ...

   4. @Entry
   5. @Component
   6. struct Index {
   7. @State message: string = 'hello world';
   8. // ...

   10. build() {
   11. Column() {
   12. // ...
   13. Text(this.message)
   14. .onClick(async () => {
   15. let context = this.getUIContext().getHostContext() as Context;
   16. // 假设已经创建了一个session，如何创建session可以参考之前的案例。
   17. let type: AVSessionManager.AVSessionType = 'audio';
   18. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
   19. // ...
   20. // 一般在监听器中会对播放器做相应逻辑处理。
   21. // 不要忘记处理完后需要通过set接口同步播放相关信息，参考上面的用例。
   22. session.on('play', () => {
   23. console.info(`on play , do play task`);
   24. // ...
   25. // 如暂不支持该指令，请勿注册；或在注册后但暂不使用时，通过session.off('play')取消监听。
   26. // 处理完毕后，请使用SetAVPlaybackState上报播放状态。
   27. });
   28. session.on('pause', () => {
   29. console.info(`on pause , do pause task`);
   30. // ...
   31. // 如暂不支持该指令，请勿注册；或在注册后但暂不使用时，通过session.off('pause')取消监听。
   32. // 处理完毕后，请使用SetAVPlaybackState上报播放状态。
   33. });
   34. session.on('stop', () => {
   35. console.info(`on stop , do stop task`);
   36. // ...
   37. // 如暂不支持该指令，请勿注册；或在注册后但暂不使用时，通过session.off('stop')取消监听。
   38. // 处理完毕后，请使用SetAVPlaybackState上报播放状态。
   39. });
   40. session.on('playNext', () => {
   41. console.info(`on playNext , do playNext task`);
   42. // ...
   43. // 如暂不支持该指令，请勿注册；或在注册后但暂不使用时，通过session.off('playNext')取消监听。
   44. // 处理完毕后，请使用SetAVPlaybackState上报播放状态，使用SetAVMetadata上报媒体信息。
   45. });
   46. session.on('playPrevious', () => {
   47. console.info(`on playPrevious , do playPrevious task`);
   48. // ...
   49. // 如暂不支持该指令，请勿注册；或在注册后但暂不使用时，通过session.off('playPrevious')取消监听。
   50. // 处理完毕后，请使用SetAVPlaybackState上报播放状态，使用SetAVMetadata上报媒体信息。
   51. });
   52. session.on('fastForward', () => {
   53. console.info(`on fastForward , do fastForward task`);
   54. // ...
   55. // 如暂不支持该指令，请勿注册；或在注册后但暂不使用时，通过session.off('fastForward')取消监听。
   56. // 处理完毕后，请使用SetAVPlaybackState上报播放状态和播放position。
   57. });
   58. session.on('rewind', () => {
   59. console.info(`on rewind , do rewind task`);
   60. // ...
   61. // 如暂不支持该指令，请勿注册；或在注册后但暂不使用时，通过session.off('rewind')取消监听。
   62. // 处理完毕后，请使用SetAVPlaybackState上报播放状态和播放position。
   63. });
   64. session.on('seek', (time) => {
   65. console.info(`on seek , the seek time is ${time}`);
   66. // ...
   67. // 如暂不支持该指令，请勿注册；或在注册后但暂不使用时，通过session.off('seek')取消监听。
   68. // 处理完毕后，请使用SetAVPlaybackState上报播放状态和播放position。
   69. });
   70. session.on('setSpeed', (speed) => {
   71. console.info(`on setSpeed , the speed is ${speed}`);
   72. // ...
   73. // 实现具体功能。
   74. });
   75. session.on('setLoopMode', (mode) => {
   76. console.info(`on setLoopMode , the loop mode is ${mode}`);
   77. // ...
   78. // 如暂不支持该指令，请勿注册；或在注册后但暂不使用时，通过session.off('setLoopMode')取消监听。
   79. // 应用自定下一个模式，处理完毕后，请使用SetAVPlaybackState上报切换后的LoopMode。
   80. });
   81. session.on('toggleFavorite', (assetId) => {
   82. console.info(`on toggleFavorite , the target asset Id is ${assetId}`);
   83. // ...
   84. // 如暂不支持该指令，请勿注册；或在注册后但暂不使用时，通过session.off('toggleFavorite')取消监听。
   85. // 处理完毕后，请使用SetAVPlaybackState上报收藏结果isFavorite。
   86. });
   87. // ...
   88. })
   89. }
   90. .width('100%')
   91. .height('100%')
   92. }
   93. }
   ```

   6.2 高级播控事件的监听。

   Session侧的可以注册的高级播控事件主要包括：

   * skipToQueueItem: 播放列表其中某项被选中的事件。
   * handleKeyEvent: 按键事件。
   * outputDeviceChange: 播放设备变化的事件。
   * commonCommand: 自定义控制命令变化的事件。

   ```
   1. import { avSession as AVSessionManager } from '@kit.AVSessionKit';
   2. // ...

   4. @Entry
   5. @Component
   6. struct Index {
   7. @State message: string = 'hello world';
   8. // ...

   10. build() {
   11. Column() {
   12. // ...
   13. Text(this.message)
   14. .onClick(async () => {
   15. try {
   16. let context = this.getUIContext().getHostContext() as Context;
   17. // 假设已经创建了一个session，如何创建session可以参考之前的案例。
   18. let type: AVSessionManager.AVSessionType = 'audio';
   19. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
   20. // ...
   21. // 一般在监听器中会对播放器做相应逻辑处理。
   22. // 不要忘记处理完后需要通过set接口同步播放相关信息，参考上面的用例。
   23. session.on('skipToQueueItem', (itemId) => {
   24. console.info(`on skipToQueueItem , do skip task`);
   25. // ...
   26. // 实现具体功能。
   27. });
   28. session.on('handleKeyEvent', (event) => {
   29. console.info(`on handleKeyEvent , the event is ${JSON.stringify(event)}`);
   30. // ...
   31. // 实现具体功能。
   32. });
   33. session.on('outputDeviceChange', (device) => {
   34. console.info(`on outputDeviceChange , the device info is ${JSON.stringify(device)}`);
   35. // ...
   36. // 实现具体功能。
   37. });
   38. session.on('commonCommand', (commandString, args) => {
   39. console.info(`on commonCommand , command is ${commandString}, args are ${JSON.stringify(args)}`);
   40. // ...
   41. // 实现具体功能。
   42. });
   43. // ...
   44. } catch (err) {
   45. if (err) {
   46. console.error(`AVSession create Error: Code: ${err.code}, message: ${err.message}`);
   47. // ...
   48. }
   49. }
   50. })
   51. }
   52. .width('100%')
   53. .height('100%')
   54. }
   55. }
   ```
7. 获取当前媒体会话自身的控制器，与媒体会话对应进行通信交互。

   ```
   1. import { avSession as AVSessionManager } from '@kit.AVSessionKit';
   2. // ...

   4. @Entry
   5. @Component
   6. struct Index {
   7. @State message: string = 'hello world';
   8. // ...

   10. build() {
   11. Column() {
   12. // ...
   13. Text(this.message)
   14. .onClick(async () => {
   15. try {
   16. let context = this.getUIContext().getHostContext() as Context;
   17. // 假设已经创建了一个session，如何创建session可以参考之前的案例。
   18. let type: AVSessionManager.AVSessionType = 'audio';
   19. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);

   21. // 通过已有session获取一个controller对象。
   22. let controller = await session.getController();
   23. // ...

   25. // controller可以与原session对象进行基本的通信交互，比如下发播放命令。
   26. let avCommand: AVSessionManager.AVControlCommand = { command: 'play' };
   27. controller.sendControlCommand(avCommand);

   29. // 或者做状态变更监听。
   30. controller.on('playbackStateChange', 'all', (state) => {

   32. // do some things.
   33. });
   34. // ...
   35. } catch (err) {
   36. if (err) {
   37. console.error(`AVSession create or getController Error: Code: ${err.code}, message: ${err.message}`);
   38. // ...
   39. }
   40. }
   41. })
   42. }
   43. .width('100%')
   44. .height('100%')
   45. }
   46. }
   ```
8. 音视频应用在退出，并且不需要继续播放时，及时取消监听以及销毁媒体会话释放资源。

   取消播控命令监听的示例代码如下所示 ：

   ```
   1. import { avSession as AVSessionManager } from '@kit.AVSessionKit';

   3. @Entry
   4. @Component
   5. struct Index {
   6. @State message: string = 'hello world';

   8. build() {
   9. Column() {
   10. Text(this.message)
   11. .onClick(async () => {
   12. let context = this.getUIContext().getHostContext() as Context;
   13. // 假设已经创建了一个session，如何创建session可以参考之前的案例。
   14. let type: AVSessionManager.AVSessionType = 'audio';
   15. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);

   17. // 取消指定session下的相关监听。
   18. session.off('play');
   19. session.off('pause');
   20. session.off('stop');
   21. session.off('playNext');
   22. session.off('playPrevious');
   23. session.off('skipToQueueItem');
   24. session.off('handleKeyEvent');
   25. session.off('outputDeviceChange');
   26. session.off('commonCommand');
   27. // ...
   28. })
   29. }
   30. .width('100%')
   31. .height('100%')
   32. }
   33. }
   ```

   销毁媒体会话示例代码如下所示：

   ```
   1. import { avSession as AVSessionManager } from '@kit.AVSessionKit';
   2. // ...

   4. @Entry
   5. @Component
   6. struct Index {
   7. @State message: string = 'hello world';
   8. // ...

   10. build() {
   11. Column() {
   12. // ...
   13. Text(this.message)
   14. .onClick(async () => {
   15. let context = this.getUIContext().getHostContext() as Context;
   16. // 假设已经创建了一个session，如何创建session可以参考之前的案例。
   17. let type: AVSessionManager.AVSessionType = 'audio';
   18. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
   19. // 主动销毁已创建的session。
   20. session.destroy((err) => {
   21. if (err) {
   22. console.error(`Failed to destroy session. Code: ${err.code}, message: ${err.message}`);
   23. // ...
   24. } else {
   25. console.info(`Destroy : SUCCESS `);
   26. // ...
   27. }
   28. });
   29. })
   30. }
   31. .width('100%')
   32. .height('100%')
   33. }
   34. }
   ```
