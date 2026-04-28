---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/distributed-playback-guide
title: 投播组件开发指导
breadcrumb: 指南 > 媒体 > AVSession Kit（音视频播控服务） > 分布式媒体会话 > 使用投播组件 > 投播组件开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:52+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:fea9969ad0a0404e4599a33dd4a857f36e5414311ed7b4d54bd85e3c3d1b27c9
---

系统提供了音视频发声设备统一投播组件AVCastPicker，作为播控中心系统级设备切换、投播能力选择入口。应用通过接入统一投播组件，可以实现在应用内及系统播控中心，将音视频资源通过Cast+协议/DLNA协议投播到远端设备。

通过本开发指导，完成一次音视频跨设备投播。

## 约束与限制

需同时满足以下条件，才能使用该功能：

* **设备限制**

  本端设备：HarmonyOS 5.0.0及以上版本的手机、平板设备

  远端设备：HarmonyOS 5.0.0及以上版本的2in1设备、HarmonyOS 3.1及以上版本的华为智慧屏、支持标准DLNA协议的设备
* **使用限制**

  双端设备打开蓝牙和WIFI，并可访问网络。

## 接口说明

在开发具体功能前，请先查阅参考文档，获取详细的接口说明。

* [AVCastPicker](../harmonyos-references/ohos-multimedia-avcastpicker.md)：投播组件，提供设备发现认证连接的统一入口。
* [AVCastController](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md)：投播控制器，用于投播场景下，完成播放控制、远端播放状态监听等操作。

  说明

  AVCastController由系统获取并返回，在设备连接成功后获取，在设备断开后不能继续使用，否则会抛出异常。

  支持在线DRM视频资源投播能力，需注册DRM许可证请求回调函数，获取许可证后，调用处理许可证响应函数。

| 接口类 | 接口 | 说明 |
| --- | --- | --- |
| AVSession | setAVMetadata(data: AVMetadata, callback: AsyncCallback<void>): void | 配置媒体信息，包括ID、标题、作者以及DRM类型等。 |
| AVSession | on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void | 注册设备变化的回调，同时包含了设备的连接状态。 |
| AVSession | getAVCastController(callback: AsyncCallback<AVCastController>): void | 获取远端投播时的控制接口。 |
| AVCastController | sendControlCommand(command: AVCastControlCommand, callback: AsyncCallback<void>): void | 投播会话的控制接口，用于进行投播中的各种播控指令。 |
| AVCastController | prepare(item: AVQueueItem, callback: AsyncCallback<void>): void | 准备播放，进行资源加载和缓冲，不会触发真正的播放。 |
| AVCastController | start(item: AVQueueItem, callback: AsyncCallback<void>): void | 开始播放媒体资源。 |
| AVCastController | processMediaKeyResponse(assetId: string, response: Uint8Array): Promise<void> | 提供DRM资源所需的秘钥。 |
| AVCastController | on(type: 'keyRequest', callback: KeyRequestCallback): void | 注册DRM秘钥请求的回调。 |
| AVCastController | on(type: 'playbackStateChange', filter: Array<string> | 'all', callback: (state: AVPlaybackState) => void): void | 注册播放状态变化的回调。 |
| AVCastController | on(type: 'mediaItemChange', callback: Callback<AVQueueItem>): void | 注册当前播放内容更新的回调，返回当前播放的内容的信息。 |

## 开发步骤

1. 创建播放器，并创建AVSession。

   通过AVSessionManager创建并激活媒体会话。

   示例中的context的获取方式请参见[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

   ```
   1. import  { avSession }  from '@kit.AVSessionKit'; // 导入AVSession模块

   3. // 声明全局的session对象，此写法是加在class类外的声明，如果需要在class类内申明全局变量，需要去掉 export let
   4. export let session: avSession.AVSession;
   5. // 创建session
   6. async createSession(context: Context) {
   7. // 创建的AVSession在基础播控与投播场景可以共用
   8. session = await avSession.createAVSession(context, 'video_test', 'video'); // 'audio'代表音频应用，'video'代表视频应用
   9. await session.activate();
   10. // 请按照如下参数设置，告知系统应用当前支持投播，才能成功投播。
   11. session.setExtras({
   12. requireAbilityList: ['url-cast'],
   13. });
   14. console.info(`Session created. sessionId: ${session.sessionId}`);
   15. }
   ```
2. 设置媒体资源信息，注册基础播控回调，接入系统播控中心的基础播控。

   说明

   * 接入投播组件前需要先适配媒体播控中心的基础播控业务，具体需要接入的内容请按照应用类型参考[应用接入自检表](playback-control-access-checklist.md)。
   * 应用可以通过filter字段设置需要发现和过滤的协议类型，来匹配应用期望的投播设备。

     注意，投播后，应用播放器切换上下集时，若下一集不支持投播，可以通过filter参数控制系统播控中心是否显示可投播设备列表，filter参数设置为0，播控会识别当前媒体内容为不支持投播，隐藏可投播设备显示。避免用户从播控中心投播，应用资源不可用。
   * 需要在AVCastPicker中仅显示支持DRM资源投播的设备时，应在AVMetadata设置明确的drmSchemes。

   ```
   1. // 与session声明不在同一文件时，需要import
   2. import  { avSession }  from '@kit.AVSessionKit'; // 导入AVSession模块
   3. export let session: avSession.AVSession;
   4. @Entry
   5. @Component
   6. struct Index{
   7. public setAVMetadata(playInfo: avSession.AVMediaDescription): Promise<void> {
   8. const metadata: avSession.AVMetadata = {
   9. assetId: playInfo.assetId, // 需要配置实际id
   10. title: playInfo.title, // 播放媒体资源的标题
   11. subtitle: playInfo.subtitle,// 播放媒体资源的副标题
   12. // 发现Cast+ Stream 和 DLNA协议设备，TYPE_CAST_PLUS_STREAM为默认必选。
   13. filter: avSession.ProtocolType.TYPE_CAST_PLUS_STREAM|avSession.ProtocolType.TYPE_DLNA,
   14. mediaImage: playInfo.mediaImage,
   15. artist: playInfo.artist,
   16. // 如果是DRM资源，配置支持的DRM uuid 用于设备过滤。非DRM资源不配置。
   17. drmSchemes: ['3d5e6d35-9b9a-41e8-b843-dd3c6e72c42c']
   18. };
   19. return session.setAVMetadata(metadata);
   20. }
   21. public setSessionListener() {
   22. // 请按照自检接入表按需注册并实现基础播控的控制指令，以下为举例
   23. session?.on('play', () => {
   24. });
   25. session?.on('pause', () => {
   26. });
   27. }
   28. build(){
   29. Column()
   30. }
   31. }
   ```
3. 在需要投播的播放界面创建投播组件AVCastPicker。

   说明

   * 若创建AVCastPicker后应用界面未显示，或点开Picker显示空白，请排查是否按步骤1、2接入了系统播控中心的基础播控，且正确设置了AVMetadata与Extras参数。
   * 系统AVCastPicker提供CustomerPicker参数，应用可以通过该参数自定义Picker按钮的显示，具体开发请参考[自定义样式](using-switch-call-devices.md#自定义样式实现)。

   ```
   1. import { AVCastPicker, AVCastPickerState } from '@kit.AVSessionKit';

   3. // 应用可以通过onStateChange接口监听组件拉起的面板的显示/消失状态，当面板显示时建议不要销毁AVCastPicker组件；当面板消失时，再根据业务需要隐藏AVCastPicker。
   4. private onStateChange(state: AVCastPickerState) {
   5. if (state == AVCastPickerState.STATE_APPEARING) {
   6. console.info('The picker starts showing.');
   7. } else if (state == AVCastPickerState.STATE_DISAPPEARING) {
   8. console.info('The picker finishes presenting.');
   9. }
   10. }

   12. // 创建组件，并设置大小
   13. build() {
   14. Row() {
   15. Column() {
   16. AVCastPicker({
   17. normalColor: Color.Red,
   18. onStateChange: this.onStateChange
   19. })
   20. .width('40vp')
   21. .height('40vp')
   22. .border({ width: 1, color: Color.Red })
   23. }.height('50%')
   24. }.width('50%')
   25. }
   ```
4. 注册AVSession投播控制回调。用于感知投播设备连接。

   说明

   下面代码展示设备连接成功后的相应的处理

   * 连接成功后通过session获取AVCastController，用于后期的投播控制；
   * 应用监听on('outputDeviceChange')回调，在收到设备切换到对端的信息时，就可以刷新应用内的播放界面为“投播页面或遥控器页面”，并暂停本机播放。在收到切换设备到本机的信息时，可以刷新应用内的播放界面为“本地播放页面”，并开始在本机播放。
   * 可以在on('outputDeviceChange')回调中使用[castCategory](../harmonyos-references/arkts-apis-avsession-e.md#avcastcategory10)来判断是否连接到远端设备。
   * on('outputDeviceChange')回调具体取值来自[ProtocolType](../harmonyos-references/arkts-apis-avsession-e.md#protocoltype11)，可以是protocoltype中的某个协议或多个协议的组合，设备仅支持一种协议，返回对应枚举值；设备支持多种协议，返回对应枚举值之和。
   * 如需要推送DRM在线资源，根据远端设备支持的DRM能力，从服务端获取对应的资源。
   * 推送DRM资源后，应注册监听许可证请求事件，从服务器端获取许可证后，通过处理许可证响应函数提供给远端。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { avSession } from '@kit.AVSessionKit';
   3. import { session } from './xxx'; // session声明的文件

   5. castController: avSession.AVCastController | undefined = undefined;
   6. getAVCastController() {
   7. // 如支持投播，可使用下面接口监听设备连接状态的变化
   8. session.on('outputDeviceChange', async (connectState: avSession.ConnectionState,
   9. device: avSession.OutputDeviceInfo) => {
   10. // 可以通过当前设备及设备连接状态来更新应用内播放界面的显示
   11. let currentDevice: avSession.DeviceInfo = device?.devices?.[0];
   12. if (currentDevice.castCategory === avSession.AVCastCategory.CATEGORY_REMOTE && connectState === avSession.ConnectionState.STATE_CONNECTED) { // 设备连接成功
   13. console.info(`Device connected: ${device}`);
   14. this.castController = await session.getAVCastController();
   15. console.info('Succeeded in getting a cast controller');
   16. // 查询当前播放的状态
   17. let avPlaybackState = await this.castController?.getAVPlaybackState();
   18. console.info(`Succeeded in AVPlaybackState resource obtained: ${avPlaybackState}`);
   19. // 监听播放状态的变化
   20. this.castController?.on('playbackStateChange', 'all', (state: avSession.AVPlaybackState) => {
   21. console.info(`Succeeded in Playback state changed: ${state}`);
   22. });
   23. // 根据currentDevice.supportedProtocols可以判断设备支持的协议类型，设备支持单个或多个协议类型
   24. if (currentDevice.supportedProtocols) {
   25. if ((currentDevice.supportedProtocols &
   26. avSession.ProtocolType.TYPE_CAST_PLUS_STREAM) === avSession.ProtocolType.TYPE_CAST_PLUS_STREAM) {
   27. // 此设备支持cast+投播协议
   28. } else if ((currentDevice.supportedProtocols & avSession.ProtocolType.TYPE_DLNA) === avSession.ProtocolType.TYPE_DLNA) {
   29. // 此设备支持DLNA投播协议
   30. }
   31. }
   32. // 此设备支持chinaDRM，监听许可证请求事件，也可在发起DRM资源投播前监听。
   33. if (currentDevice.supportedDrmCapabilities?.includes('3d5e6d35-9b9a-41e8-b843-dd3c6e72c42c')) {
   34. this.castController?.on('keyRequest', this.keyRequestCallback);
   35. }
   36. }
   37. })
   38. }

   40. // 处理DRM许可证请求事件
   41. private keyRequestCallback: avSession.KeyRequestCallback = async (assetId: string, requestData: Uint8Array) => {
   42. // 根据assetId获取对应的DRM url
   43. let drmUrl: string = 'http://license.xxx.xxx.com:8080/drmproxy/getLicense';
   44. // 从服务器获取许可证，具体实现可参考附录。
   45. let licenseResponseData = await this.getLicense(drmUrl, requestData);
   46. try {
   47. // 处理DRM许可证响应
   48. await this.castController?.processMediaKeyResponse(assetId, licenseResponseData);
   49. } catch (error) {
   50. console.error(`Failed to process the response corresponding to the media key. Error: ${error}`);
   51. }
   52. }
   ```
5. 使用AVCastController进行资源播放。

   说明

   下面代码示例中的url仅作示意使用，开发者需根据实际情况，确认资源有效性并设置：

   * 如果使用本地资源播放，必须确认资源文件可用，并使用应用沙箱路径访问对应资源，参考[获取应用文件路径](application-context-stage.md#获取应用文件路径)。应用沙箱的介绍及如何向应用沙箱推送文件，请参考[文件管理](app-sandbox-directory.md)。
   * 如果通过FilePicker使用用户文件，请参考[选择用户文件](select-user-file.md)。
   * 如果使用网络播放路径，需[申请相关权限](declare-permissions.md)：ohos.permission.INTERNET。
   * 如果是DRM资源，需配置drmSchemes字段。

   ```
   1. playItem() {
   2. // 设置播放参数，开始播放
   3. let playItem : avSession.AVQueueItem = {
   4. itemId: 0,
   5. description: {
   6. assetId: 'VIDEO-1',
   7. title: 'ExampleTitle',
   8. artist: 'ExampleArtist',
   9. // 网络资源投播，设置mediaUri; 本地资源投播，将本地文件打开后，相关的文件描述符设置到fdSrc
   10. mediaUri: 'https://xxx.xxx.com/example.mp4',
   11. // 该字段大写，音频'AUDIO'，视频'VIDEO'
   12. mediaType: 'VIDEO',
   13. mediaSize: 1000,
   14. // startPosition为投播当前进度，设置该字段可将本机播放进度同步到远端
   15. startPosition: 0,
   16. // 投播资源播放时长，设置该字段可将本机播放时长同步到远端显示
   17. duration: 100000,
   18. albumCoverUri: 'https://www.example.jpeg',
   19. albumTitle: '《ExampleAlbum》',
   20. appName: 'ExampleApp',
   21. // DRM资源，需要配置支持的DRM类型, 以chinaDRM为例。
   22. drmScheme: '3d5e6d35-9b9a-41e8-b843-dd3c6e72c42c',
   23. }
   24. };
   25. // 准备播放，这个不会触发真正的播放，会进行加载和缓冲
   26. this.castController?.prepare(playItem, () => {
   27. console.info('Preparation done');
   28. // 启动播放，真正触发对端播放。请在Prepare成功后再调用start。
   29. this.castController?.start(playItem, () => {
   30. console.info('Playback started');
   31. });
   32. });
   33. }
   ```
6. 使用AVCastController，监听控制命令和进行播放控制。

   说明

   * 应用可以通过如下监听与控制指令，实现从应用内控制投播设备，及响应来自对端设备或者系统播控中心的控制。
   * 系统播控中心会按照应用的注册监听，来动态置灰和点亮控制卡片的按钮。
   * 当前系统暂不支持清晰度调节，应用如需向用户提供清晰度调节入口，需要在用户选定不同清晰度时按照新的清晰度重新下发资源。

   ```
   1. playControl() {
   2. // 记录从avsession获取的远端控制器this.castController
   3. // 应用向对端设备下发播放命令
   4. let avCommand: avSession.AVCastControlCommand = {command:'play'};
   5. this.castController?.sendControlCommand(avCommand);

   7. // 应用向对端设备下发暂停命令
   8. avCommand = {command:'pause'};
   9. this.castController?.sendControlCommand(avCommand);

   11. // 应用调节对端设备音量
   12. avCommand = {
   13. command: 'setVolume',
   14. parameter: 1
   15. };
   16. this.castController?.sendControlCommand(avCommand);

   18. // 应用调节对端设备进度
   19. avCommand = {
   20. command: 'seek',
   21. parameter: 1
   22. };
   23. this.castController?.sendControlCommand(avCommand);
   24. // 更多控制指令请参考AVCastControlCommand
   25. }
   26. controlListener() {
   27. // 应用监听对端或播控中心上下一首/上下一集切换
   28. this.castController?.on('playPrevious', () => {
   29. console.info('PlayPrevious done');
   30. });
   31. this.castController?.on('playNext', () => {
   32. console.info('PlayNext done');
   33. });

   35. // 应用监听对端或播控中心播放状态、实时进度和音量变化事件
   36. this.castController?.on('playbackStateChange', (playbackState: avSession.AVPlaybackState)=>{
   37. if (playbackState?.state) {
   38. // 播放状态变化
   39. }
   40. if (playbackState?.position) {
   41. // 进度变化，可以根据position来获取对端播放的进度
   42. }
   43. if (playbackState?.volume) {
   44. // 音量变化
   45. }
   46. });

   48. // 应用监听对端投播内容播放完毕事件。应用监听到此回调，可以按照业务在以下三种选其一实现，否则无内容播放，对端出现黑屏。
   49. // 1. 有下一集时，自动切换下一集投播，此时需要调用Prepare和start重新设置新的url，参考步骤5
   50. // 2. 无下一集时，建议循环播放同一集，重新调用prepare和start来设置当前新的url，参考步骤5
   51. // 3. 业务不再支持投播，可以主动断开投播，参考步骤9。
   52. this.castController?.on('endOfStream', () => {
   53. // 按业务处理
   54. });

   56. // 应用监听对端或播控中心的进度调节完成事件，包括快进、快退、进度条拖拽完毕
   57. this.castController?.on('seekDone', (position: number) => {
   58. // seekDone表示用户在对端或是播控内进度调节完毕，可以在收到该回调后，根据'playbackStateChange'回调的position刷新绘制应用内进度条
   59. // 应用主动调用seek调节对端进度后，也请等待seekDone回调再根据'playbackStateChange'中的position来刷新，更精准
   60. });
   61. }
   ```
7. 申请投播长时任务，避免应用在投播时进入后台时被系统冻结，导致无法持续投播。

   说明

   在申请长时任务时，需要在module.json5文件中：

   1. 配置长时任务权限ohos.permission.KEEP\_BACKGROUND\_RUNNING。
   2. 为需要使用长时任务的UIAbility声明相应的后台模式类型：AUDIO\_PLAYBACK。选其一申请即可，都可保证音频在应用后台、锁屏、熄屏投播时不会被中断。

   ```
   1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
   2. import { wantAgent } from '@kit.AbilityKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. let context: Context = getContext(this);

   7. function startContinuousTask() {
   8. let wantAgentInfo: wantAgent.WantAgentInfo = {
   9. // 点击通知后，将要执行的动作列表
   10. wants: [
   11. {
   12. bundleName: "com.example.myapplication",
   13. abilityName: "EntryAbility",
   14. }
   15. ],
   16. // 点击通知后，动作类型
   17. operationType: wantAgent.OperationType.START_ABILITY,
   18. // 使用者自定义的一个私有值
   19. requestCode: 0,
   20. // 点击通知后，动作执行属性
   21. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
   22. };

   24. // 通过wantAgent模块的getWantAgent方法获取WantAgent对象
   25. try {
   26. wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
   27. try {
   28. backgroundTaskManager.startBackgroundRunning(context,
   29. backgroundTaskManager.BackgroundMode.AUDIO_PLAYBACK, wantAgentObj).then(() => {
   30. console.info('Succeeded in requesting to start running in background');
   31. }).catch((error: BusinessError) => {
   32. console.error(`Failed to request to start running in background. Code: ${error.code}, message: ${error.message}`);
   33. });
   34. } catch (error) {
   35. console.error(`Failed to request to start running in background. Error: ${error}`);
   36. }
   37. });
   38. } catch (error) {
   39. console.error(`Failed to get WantAgent. Error: ${error}`);
   40. }
   41. }
   ```
8. 投播后资源切换。

   * 应用已开始投播，再次进入播放详情页时可以通过getOutputDevice()接口获取当前播放设备，来判断此时是否正在投播中。

     ```
     1. import  { avSession }  from '@kit.AVSessionKit'; // 导入AVSession模块
     2. // 与session声明不在同一文件时，需要import
     3. import { session } from './xxx'; // session声明的文件
     4. this.session?.getOutputDevice().then((outputDeviceInfo: avSession.OutputDeviceInfo) => {
     5. // 当前设备的castCategory为Remote，则表示正在投播中
     6. let isCasting = outputDeviceInfo.devices[0].castCategory === avSession.AVCastCategory.CATEGORY_REMOTE;
     7. }).catch((err: BusinessError) => {
     8. console.error(`GetOutputDevice BusinessError: code: ${err.code}, message: ${err.message}`);
     9. });
     ```
   * 应用已开始投播，从播放详情页退出到应用首页时，建议不要断开投播即调用stopCasting，可以给用户留一个回到“投播的界面”的入口。
   * 投播时用户在应用侧退出详情页，如果点击了其他视频播放，应用识别新的资源是否可以投播，可以根据以下两种情况处理：

     + 情况一：如新的视频资源可以投播，有以下两种方式可处理：

       方式一：直接调用prepare和start更换投播资源，参考步骤5。对端播放新的视频资源，本地显示切换为“正在投播的界面”，不需要断开投播重新投播。

       方式二：不主动切换投播资源，正常绘制应用投播业务的按钮但不要创建AVCastPicker，用户点击后直接调用prepare和start更换投播资源，本地显示切换为“正在投播的界面”，不需要断开投播重新投播。
     + 情况二：如此时不可以投播，当前视频就在本地播放，隐藏投播业务的按钮显示即可。
9. 处理音频焦点。请参考[多音频并发处理](audio-playback-concurrency.md)。

   在应用进入投播后，当前应用需要取消注册焦点处理事件，以免被其他应用的焦点申请而影响。
10. 结束投播。

* 当远端设备断开的时候，应用会收到事件，系统会自动断开连接。
* 应用也可以使用断开投播的接口，主动进行投播连接的断开。

  ```
  1. async release() {
  2. // 一般来说，应用退出时，而不希望继续投播，可以主动结束
  3. await session.stopCasting();
  4. }
  ```
* 建议应用监听并保存AVCastController.on('playbackStateChange')回调中的position，当投播断开时，可以刷新为“本地播放详情页”在本端继续播放，并根据这个position来调整本地播放的进度。

## 镜像投屏自动切换资源投播

适用场景：用户通过“无线投屏”功能实现手机等设备和大屏等的镜像投屏，然后打开视频应用进入视频播放，此时会自动切换为资源投播。要达到上述目标体验，还需要做一些额外的适配工作。

1. 应用进入播放页后，需要调用[getOutputDevicesync](../harmonyos-references/arkts-apis-avsession-avsession.md#getoutputdevicesync10)接口来判断当前是否存在投屏的设备，避免和其他应用冲突。

   通过[开发步骤](distributed-playback-guide.md#开发步骤)第四步进行投播设备判断，如果存在投播设备，表示此时可以进行资源投播；否则表示没有可以投播的设备,或者系统当前虽然在镜像投屏，此时有别的APP在投播，此时应用应在本地播放。
2. 应用正常投播后，仍然监听设备状态断开等场景，流程同[投播组件开发步骤](distributed-playback-guide.md#开发步骤)中的内容描述。

### 附录

**从服务器获取许可证**

开发者需要根据实际的资源和服务地址获取DRM许可证，以下示例代码仅作为参考。

```
1. import { http } from '@kit.NetworkKit';

3. // 获取DRM许可证, 仅做参考，需要结合实际资源和服务地址进行获取。
4. async getLicense(drmUrl: string, requestData: Uint8Array): Promise<Uint8Array | undefined> {
5. let licenseRequestStr: string = this.byteToString(requestData);
6. let licenseResponseStr: string = 'defaultStr';
7. let httpRequest = http.createHttp();
8. try {
9. let response: http.HttpResponse = await httpRequest.request(drmUrl, {
10. method: http.RequestMethod.POST,
11. header: {
12. 'Content-Type': 'application/json',
13. 'Accept-Encoding': 'gzip, deflate',
14. },
15. extraData: licenseRequestStr,
16. expectDataType: http.HttpDataType.STRING,
17. });
18. if (response?.responseCode == http.ResponseCode.OK) {
19. if (typeof response.result == 'string') {
20. licenseResponseStr = response.result;
21. }
22. }
23. httpRequest.destroy();
24. } catch (error) {
25. console.error(`Failed to request Http. Error: ${error}`);
26. return undefined;
27. }
28. return this.stringToByte(licenseResponseStr);
29. }

31. /**
32. * Uint8Array to string
33. * @param arr Uint8Array
34. * @returns string
35. */
36. byteToString(arr: Uint8Array): string {
37. let str: string = ''
38. let _arr: Uint8Array = arr

40. for (let i = 0; i < _arr.length; i++) {
41. // 将数值转为二进制字符串
42. let binaryStr: string = _arr[i].toString(2)
43. let matchArray = binaryStr.match(new RegExp('/^1+?(?=0)/'))
44. if (matchArray && binaryStr.length == 8) {
45. let bytesLength: number = matchArray[0].length
46. let store: string = _arr[i].toString(2).slice(7 - bytesLength)

48. for (let j = 1; j < bytesLength; j++) {
49. store += _arr[j + i].toString(2).slice(2)
50. }
51. str += String.fromCharCode(Number.parseInt(store, 2))
52. i += bytesLength - 1
53. } else {
54. str += String.fromCharCode(_arr[i])
55. }
56. }
57. return str
58. }

60. /**
61. * string 转 Uint8Array
62. * @param str string
63. * @returns Uint8Array
64. */
65. stringToByte(str: string): Uint8Array {
66. let bytes: number[] = new Array()
67. let unicode: number

69. for (let i = 0; i < str.length; i++) {
70. unicode = str.charCodeAt(i)
71. if (unicode >= 0x010000 && unicode <= 0x10FFFF) {
72. bytes.push(((unicode >> 18) & 0x07) | 0xf0)
73. bytes.push(((unicode >> 12) & 0x3F) | 0x80)
74. bytes.push(((unicode >> 6) & 0x3F) | 0x80)
75. bytes.push((unicode & 0x3F) | 0x80)
76. } else if (unicode >= 0x000800 && unicode <= 0x00FFF) {
77. bytes.push(((unicode >> 12) & 0x07) | 0xf0)
78. bytes.push(((unicode >> 6) & 0x3F) | 0x80)
79. bytes.push((unicode & 0x3F) | 0x80)
80. } else if (unicode >= 0x000800 && unicode <= 0x0007FF) {
81. bytes.push(((unicode >> 6) & 0x3F) | 0x80)
82. bytes.push((unicode & 0x3F) | 0x80)
83. } else {
84. bytes.push(unicode & 0xFF)
85. }
86. }
87. return new Uint8Array(bytes);
88. }
```
