---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-audio-in-ear-monitor
title: 基于Audio能力实现音频耳返
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 基于Audio能力实现音频耳返
category: best-practices
scraped_at: 2026-04-28T08:20:48+08:00
doc_updated_at: 2026-04-01
content_hash: sha256:4d0c81f2b933d0a3215044b662b2e0e077ccb2f08d9d4a78cf3b313e5b9b61ca
---

## 概述

耳返是指通过耳机系统将音频实时传输到耳机中，让使用者能够听到自己的声音、伴奏或其它需要的信息。例如在K歌类应用中，将录制的人声和背景音乐实时送到耳机中，使用户通过反馈即时调整，获得更好的使用体验。

当前系统支持耳返的两种方案如下：

|  |  |  |  |
| --- | --- | --- | --- |
|  | 实现方案 | 优点 | 缺点 |
| 硬件耳返 | 基于[AudioLoopback](../harmonyos-references/arkts-apis-audio-audioloopback.md)实现音频耳返 | 1. 物理耳返，延时低。 2. 在API21，提供混响和均衡器等音效。 | 1. 当前仅支持有线耳机，不支持蓝牙耳机。 2. 在耳返的场景下，仅支持录制麦克风。 |
| 软件耳返 | 基于[OHAudio](../harmonyos-references/capi-ohaudio.md)实现音频耳返 | 1. 可以支持有线耳机和蓝牙耳机。 2. 可以支持耳返（使用者自己的声音或其它需要的信息等）和背景音乐同时录制写入到文件中。 | 1. 暂无硬件耳返的接口，软件耳返延时比硬件耳返高。 2. 无音效相关的接口，音效等算法需要自行实现。 |

本文将介绍以下两种实现音频耳返方案：

* [基于AudioLoopback实现音频耳返](bpta-audio-in-ear-monitor.md#section1720354614413)
* [基于OHAudio实现音频耳返](bpta-audio-in-ear-monitor.md#section144598624518)

## 基于AudioLoopback实现音频耳返

### 场景描述

点击进入AudioLoopback页面，连接有线耳机，点击录制按钮开启耳返。开启耳返后开发者可通过麦克风在耳机中实时听到自己或周围的声音，同时进行耳返内音频的录制，并且可通过Slider滑块实现耳返音量调节功能。录制完成后进入播放页面，播放录制的音频资源。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/mz9i99eUTl-6Cw5WQcVpsA/zh-cn_image_0000002544829543.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002046Z&HW-CC-Expire=86400&HW-CC-Sign=EC975F8CEAF94F37A5E2E2A617239968FD5E912CDA714DA6E7F16EFD2E048551 "点击放大")

### 实现原理

AudioLoopback是HarmonyOS提供的音频返听接口，用于实现低时延耳返功能，支持自动创建低时延渲染器与采集器，采集的音频可直接通过内部路由返回到渲染器，实时传输到耳机。

AudioLoopback的状态变化如下图所示，在创建AudioLoopback实例后，调用对应的方法可以进入指定的状态实现对应行为。同时需要注意的是，在确定的状态执行不合适的方法，可能导致AudioLoopback发生错误，建议开发者在调用状态转换的方法前进行状态检查，避免程序运行产生预期以外的结果，详细开发指导请参考：[实现音频低时延耳返](../harmonyos-guides/audio-ear-monitor-loopback.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/179pRqqPRCSEe0Pz192oSg/zh-cn_image_0000002513149636.png?HW-CC-KV=V1&HW-CC-Date=20260428T002046Z&HW-CC-Expire=86400&HW-CC-Sign=292AA11B4AEAADCB4D002DC2EC6FEB73D0E445050DE54147E051A68E7E290A06 "点击放大")

### 开发步骤

使用AudioLoopback控制耳返的开启和关闭，结合[AVRecorder](../harmonyos-references/arkts-apis-media-avrecorder.md)实现音频的录制，将录制的音频保存在应用沙箱目录，并通过[@ohos.file.fs (文件管理)](../harmonyos-references/js-apis-file-fs.md)打开录制的音频文件，再通过[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)实现已录制音频的播放控制，详细流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/8IT_x_bIT4KkWLuz4x9WBA/zh-cn_image_0000002513309570.png?HW-CC-KV=V1&HW-CC-Date=20260428T002046Z&HW-CC-Expire=86400&HW-CC-Sign=6F8EE3F04BF4715DED3F60CF3DDFDE7C74393CA3F1012E4D7B7E62D268577015 "点击放大")

具体开发步骤如下：

1. 创建AudioLoopback。
   * 通过[isAudioLoopbackSupported()](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#isaudioloopbacksupported20)查询当前系统是否支持音频返听模式。若支持，则调用[audio.createAudioLoopback()](../harmonyos-references/arkts-apis-audio-f.md#audiocreateaudioloopback20)接口创建音频返听器。

     ```
     1. private audioLoopback: audio.AudioLoopback | undefined = undefined;
     2. // ...

     4. // Query capability, create AudioLoopback instance.
     5. public initAudioLoopback(): void {
     6. try {
     7. // Check whether the current system supports hardware in-ear monitor cancellation mode.
     8. let isSupported = audio.getAudioManager().getStreamManager().isAudioLoopbackSupported(this.mode);
     9. if (isSupported) {
     10. audio.createAudioLoopback(this.mode)
     11. .then((loopback) => {
     12. this.audioLoopback = loopback;
     13. })
     14. .catch((err: BusinessError) => {
     15. logger.error(`Invoke createAudioLoopback failed, code is ${err.code}, message is ${err.message}.`);
     16. });
     17. }
     18. } catch (error) {
     19. let err = error as BusinessError;
     20. logger.error(`Failed to use isAudioLoopbackSupported, code=${err.code}, message=${err.message}}`);
     21. }
     22. }
     ```

     [AudioLoopbackController.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/controller/AudioLoopbackController.ets#L23-L47)
   * 通过AudioLoopback的[getStatus()](../harmonyos-references/arkts-apis-audio-audioloopback.md#getstatus20)方获取音频返听状态，当返听状态为AVAILABLE\_IDLE时，表示返听可用，此时可调用[enable()](../harmonyos-references/arkts-apis-audio-audioloopback.md#enable20)方法传入参数true，开启音频返听。

     ```
     1. // Set up a listening event and enable audio feedback.
     2. public async enable(): Promise<void> {
     3. // ...

     5. try {
     6. let status = await this.audioLoopback.getStatus();
     7. if (status === audio.AudioLoopbackStatus.AVAILABLE_IDLE) {
     8. // Enable in-ear monitor.
     9. await this.audioLoopback.enable(true)
     10. .then((isSuccess: boolean) => {
     11. if (isSuccess) {
     12. this.setAudioReverbPreset(audio.AudioLoopbackReverbPreset.ORIGINAL);
     13. this.setEqualizerPreset(audio.AudioLoopbackEqualizerPreset.FULL);
     14. }
     15. })
     16. .catch((err: BusinessError) => {
     17. logger.error(`Audio loopback enable failed. code=${err.code}, message=${err.message}`);
     18. })
     19. } else {
     20. this.statusChangeCallback(status);
     21. }
     22. } catch (err) {
     23. logger.error(`code is ${err.code}, message is ${err.message}.`);
     24. }
     25. }
     ```

     [AudioLoopbackController.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/controller/AudioLoopbackController.ets#L51-L80)
   * 当返听状态为AVAILABLE\_RUNNING时，表示返听在运行中，调用[enable()](../harmonyos-references/arkts-apis-audio-audioloopback.md#enable20)方法传入参数false，禁用音频返听。

     ```
     1. // Disable audio playback, close monitoring event.
     2. public async disable(): Promise<void> {
     3. // ...
     4. try {
     5. let status = await this.audioLoopback.getStatus();
     6. if (status === audio.AudioLoopbackStatus.AVAILABLE_RUNNING) {
     7. // Disable in-ear monitor.
     8. await this.audioLoopback.enable(false)
     9. .then((isSuccess: boolean) => {
     10. if (isSuccess) {
     11. // Close monitoring.
     12. this.audioLoopback?.off('statusChange', this.statusChangeCallback);
     13. }
     14. })
     15. .catch((err: BusinessError) => {
     16. logger.error(`Audio loopback enable failed. code=${err.code}, message=${err.message}`);
     17. })
     18. } else {
     19. this.statusChangeCallback(status);
     20. }
     21. } catch (err) {
     22. logger.error(`Invoke disable failed, code is ${err.code}, message is ${err.message}.`);
     23. }
     24. }
     ```

     [AudioLoopbackController.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/controller/AudioLoopbackController.ets#L132-L160)
   * 调用[setVolume()](../harmonyos-references/arkts-apis-audio-audioloopback.md#setvolume20)方法实现音频返听音量的调节。

     ```
     1. // Set audio playback volume.
     2. public async setVolume(volume: number): Promise<void> {
     3. // ...
     4. try {
     5. await this.audioLoopback.setVolume(volume);
     6. logger.info(`Invoke setVolume ${volume} succeeded.`);
     7. } catch (err) {
     8. logger.error(`Invoke setVolume failed, code is ${err.code}, message is ${err.message}.`);
     9. }
     10. }
     ```

     [AudioLoopbackController.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/controller/AudioLoopbackController.ets#L84-L98)
2. 创建AVRecorder。
   * 调用[media.createAVRecorder()](../harmonyos-references/arkts-apis-media-f.md#mediacreateavrecorder9)方法，用于创建AVRecorder实例。

     ```
     1. private avRecorder: media.AVRecorder | undefined = undefined;

     3. // Create an avRecorder instance.
     4. public async initAVRecorder() {
     5. try {
     6. this.avRecorder = await media.createAVRecorder();
     7. } catch (err) {
     8. let error: BusinessError = err as BusinessError;
     9. logger.error(`Failed to create avRecorder, error code: ${error.code}, message: ${error.message}`);
     10. }
     11. }
     ```

     [RecorderController.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/controller/RecorderController.ets#L22-L32)
   * 调用[prepare()](../harmonyos-references/arkts-apis-media-avrecorder.md#prepare9)方法设置音频录制的音频编码比特率、采集声道数、编码格式、采样率和容器格式等信息。

     ```
     1. // Configure audio recording parameters.
     2. public prepareAVRecorder(uiContext: Context) {
     3. // Audio recording configuration file.
     4. let avProfile: media.AVRecorderProfile = {
     5. audioBitrate: 112000, // Audio Bit Rate.
     6. audioChannels: 2, // Number of audio channels.
     7. audioCodec: media.CodecMimeType.AUDIO_AAC, // Audio encoding format.
     8. audioSampleRate: 48000, // Audio sampling rate.
     9. fileFormat: media.ContainerFormatType.CFT_MPEG_4A // Container format.
     10. };

     12. const context: Context = uiContext;
     13. let filePath: string = context.filesDir + '/example.mp3';
     14. try {
     15. let audioFile: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
     16. let fileFd: number = audioFile?.fd as number;
     17. // Parameter settings for audio recording.
     18. let avConfig: media.AVRecorderConfig = {
     19. audioSourceType: media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC, // Audio input source, set as microphone here
     20. profile: avProfile,
     21. url: 'fd://' + fileFd
     22. };
     23. AppStorage.setOrCreate('fdSrc', fileFd);
     24. if(!this.avRecorder) {
     25. return;
     26. }
     27. if (this.avRecorder.state === 'idle' || this.avRecorder.state === 'stopped') {
     28. this.avRecorder.prepare(avConfig, (err: BusinessError) => {
     29. if (!err) {
     30. this.startRecorder();
     31. }
     32. });
     33. }
     34. } catch (error) {
     35. let err = error as BusinessError;
     36. logger.error(`Failed to open file, error code: ${err.code}, message: ${err.message}`);
     37. }
     38. }
     ```

     [RecorderController.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/controller/RecorderController.ets#L36-L73)
   * 调用[start()](../harmonyos-references/arkts-apis-media-avrecorder.md#start9)方法开始音频录制。

     ```
     1. // Start recording.
     2. public startRecorder() {
     3. // ...
     4. this.avRecorder.start((err: BusinessError) => {
     5. if (!err) {
     6. logger.info('Succeeded in start avRecorder');
     7. }
     8. });
     9. }
     ```

     [RecorderController.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/controller/RecorderController.ets#L77-L89)
   * 调用[pause()](../harmonyos-references/arkts-apis-media-avrecorder.md#pause9)方法暂停音频录制。

     ```
     1. // Pause recording.
     2. public pauseRecorder() {
     3. // ...
     4. this.avRecorder.pause((err: BusinessError) => {
     5. if (!err) {
     6. logger.info('Succeeded in pause avRecorder');
     7. }
     8. });
     9. }
     ```

     [RecorderController.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/controller/RecorderController.ets#L93-L105)
   * 调用[resume()](../harmonyos-references/arkts-apis-media-avrecorder.md#resume9)方法恢复音频录制。

     ```
     1. // Resume recording.
     2. public resumeRecorder() {
     3. // ...
     4. this.avRecorder.resume((err: BusinessError) => {
     5. if (!err) {
     6. logger.info('Succeeded in resume avRecorder');
     7. }
     8. });
     9. }
     ```

     [RecorderController.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/controller/RecorderController.ets#L109-L121)
   * 调用[stop()](../harmonyos-references/arkts-apis-media-avrecorder.md#stop9)方法停止音频录制。

     ```
     1. // Stop recording.
     2. public stopRecorder() {
     3. // ...
     4. this.avRecorder.stop((err: BusinessError) => {
     5. if (!err) {
     6. logger.info('Succeeded in stop avRecorder');
     7. }
     8. });
     9. }
     ```

     [RecorderController.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/controller/RecorderController.ets#L125-L137)
   * 调用[release()](../harmonyos-references/arkts-apis-media-avrecorder.md#release9)方法释放音频录制资源。

     ```
     1. // Release audio recording resources.
     2. public releaseRecorder() {
     3. // ...
     4. this.avRecorder.release((err: BusinessError) => {
     5. if (!err) {
     6. logger.info('Succeeded in release avRecorder');
     7. }
     8. });
     9. }
     ```

     [RecorderController.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/controller/RecorderController.ets#L141-L153)
3. 创建AVPlayer。
   * 调用[media.createAVPlayer()](../harmonyos-references/arkts-apis-media-f.md#mediacreateavplayer9-1)方法创建AVPlayer实例。

     ```
     1. private avPlayer: media.AVPlayer | undefined = undefined;

     3. // Initialize and create an AVPlayer instance.
     4. async initAVPlayer(fd: number, isPlay: boolean): Promise<void> {
     5. try {
     6. this.avPlayer = await media.createAVPlayer();
     7. await this.setAVPlayerCallback(isPlay);
     8. this.avPlayer.fdSrc = { fd: fd };
     9. } catch (error) {
     10. let err = error as BusinessError;
     11. logger.error(`AVPlayer init fail. code=${err.code}, message=${err.message}`);
     12. }
     13. }
     ```

     [AVPlayerController.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/controller/AVPlayerController.ets#L26-L38)
   * 调用[play()](../harmonyos-references/arkts-apis-media-avplayer.md#play9-1)方法，用于播放录制的音频资源。

     ```
     1. // Play audio.
     2. play(): void {
     3. // ...
     4. this.avPlayer.play()
     5. .catch(() => {
     6. logger.error('AVPlayerController play error!');
     7. })
     8. }
     ```

     [AVPlayerController.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/controller/AVPlayerController.ets#L67-L78)
   * 调用[pause()](../harmonyos-references/arkts-apis-media-avplayer.md#pause9-1)方法，暂停播放音频。

     ```
     1. // Pause playback.
     2. pause(): void {
     3. // ...
     4. this.avPlayer.pause()
     5. .catch(() => {
     6. logger.error('AVPlayerController pause error!');
     7. })
     8. }
     ```

     [AVPlayerController.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/controller/AVPlayerController.ets#L82-L93)
   * 调用[release()](../harmonyos-references/arkts-apis-media-avplayer.md#release9-1)方法，释放播放资源。

     ```
     1. // Destruction of playback resources.
     2. release(): void {
     3. // ...
     4. this.avPlayer.release()
     5. .catch(() => {
     6. logger.error('AVPlayerController release error!');
     7. });
     8. }
     ```

     [AVPlayerController.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/controller/AVPlayerController.ets#L105-L116)
4. 在页面内点击录制按钮后，请求用户授权麦克风权限，通过AudioLoopback开启耳返，同时通过AVRecorder进行耳返音频的录制。
   * 开启耳返并录制音频。

     [@ohos.abilityAccessCtrl (程序访问控制管理)](../harmonyos-references/js-apis-abilityaccessctrl.md)提供了应用程序的权限校验和管理能力，通过[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)接口拉起弹框，向用户请求授权麦克风权限。

     ```
     1. // Pull up the pop-up box and request user authorization.
     2. atManager.requestPermissionsFromUser(this.getUIContext().getHostContext(), ['ohos.permission.MICROPHONE'])
     3. .then((data) => {
     4. if (data.authResults[0] !== 0) {
     5. return;
     6. }
     7. this.capturesStart();
     8. })
     9. .catch((err: BusinessError) => {
     10. logger.error(`requestPermissionsFromUser fail. err.code=${err.code}, err.message=${err.message}}`);
     11. });
     ```

     [InEarMonitorPage.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/pages/InEarMonitorPage.ets#L259-L269)

     调用自定义capturesStart()方法，通过AudioLoopback的enable()开启耳返，并通过prepareAVRecorder()进行耳返音频的录制。

     ```
     1. // Start collecting audio.
     2. capturesStart() {
     3. try {
     4. // Enable in-ear monitor.
     5. if (this.isArkTS) {
     6. this.audioLoopbackController.enable();
     7. } else {
     8. // ...
     9. }
     10. this.recorderController.prepareAVRecorder(this.getUIContext().getHostContext()!); // Start recording.
     11. this.recordSec = 0; // Initialize recording duration.
     12. this.showTime = '00:00:00'; // Initialize audio capture time.
     13. this.recordState = CommonConstants.PLAY_STARTED; // Start recording status.
     14. clearInterval(this.interval); // Clear timer.
     15. this.interval = setInterval(async () => {
     16. // ...
     17. this.recordSec++;
     18. this.showTime = FormatTimeTools.getTimesBySecond(this.recordSec); // Audio acquisition time conversion
     19. }, 1000)
     20. } catch (error) {
     21. let err = error as BusinessError;
     22. logger.error(`AudioRecording:audioCapturer start err.code = ${err.code}, err.message=${err.message}`);
     23. }
     24. }
     ```

     [InEarMonitorPage.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/pages/InEarMonitorPage.ets#L66-L105)
   * 暂停录制。

     定义capturesPause()方法，在其中调用pauseRecorder()暂停音频录制，并调用disable()禁用音频返听。

     ```
     1. // Pause audio capture.
     2. capturesPause() {
     3. try {
     4. clearInterval(this.interval);
     5. this.recordState = CommonConstants.PLAY_PAUSED;
     6. this.recorderController.pauseRecorder(); // Pause recording.
     7. // Disable in-ear monitor.
     8. if (this.isArkTS) {
     9. this.audioLoopbackController.disable();
     10. } else {
     11. // ...
     12. }
     13. } catch (error) {
     14. let err = error as BusinessError;
     15. logger.error(`AudioRecording:audioCapturer stop. err.code=${err.code}, err.message=${err.message}}`);
     16. }
     17. }
     ```

     [InEarMonitorPage.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/pages/InEarMonitorPage.ets#L109-L133)
   * 继续录制。

     定义capturesContinue()方法，在其中调用enable()重启音频返听，并通过resumeRecorder()恢复录制。

     ```
     1. // Continue to collect.
     2. capturesContinue() {
     3. try {
     4. // ...
     5. this.recordState = CommonConstants.PLAY_CONTINUED;
     6. // Enable in-ear monitor.
     7. if (this.isArkTS) {
     8. this.audioLoopbackController.enable();
     9. } else {
     10. // ...
     11. }
     12. this.recorderController.resumeRecorder(); // Resume recording
     13. this.interval = setInterval(async () => {
     14. // ...
     15. this.recordSec++;
     16. this.showTime = FormatTimeTools.getTimesBySecond(this.recordSec);
     17. }, 1000);
     18. } catch (err) {
     19. logger.error(`AudioRecording:audioCapturer start err = ${JSON.stringify(err)}`);
     20. }
     21. }
     ```

     [InEarMonitorPage.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/pages/InEarMonitorPage.ets#L137-L179)
   * 调节耳返音量。

     在Slider组件的onChange()事件中，调用audioLoopbackController的setVolume()方法，并传入value值，实现耳返音量的调节。

     ```
     1. Slider({
     2. min: 0,
     3. max: 1,
     4. step: 0.1,
     5. value: this.volumeValue,
     6. })
     7. .width('75%')
     8. .onChange((value: number) => {
     9. this.volumeValue = value;
     10. if (this.isArkTS) {
     11. this.audioLoopbackController.setVolume(value);
     12. } else {
     13. // ...
     14. }
     15. })
     ```

     [InEarMonitorPage.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/pages/InEarMonitorPage.ets#L356-L376)
   * 停止录制。

     定义capturesStop()方法，在其中调用stopRecorder()方法停止录制，并通过disable()禁用音频返听。

     ```
     1. // Stop audio collection
     2. capturesStop() {
     3. clearInterval(this.interval);
     4. this.recorderController.stopRecorder(); // Stop recording.
     5. // Disable in-ear monitor.
     6. if (this.isArkTS) {
     7. this.audioLoopbackController.disable();
     8. } else {
     9. // ...
     10. }
     11. }
     ```

     [InEarMonitorPage.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/pages/InEarMonitorPage.ets#L183-L201)
5. 播放音频。
   * 初始化AVPlayer实例，并传入音频资源句柄。

     ```
     1. private avPlayerController: AVPlayerController = new AVPlayerController();
     2. private fdSrc: number | undefined = 0;

     4. aboutToAppear(): void {
     5. this.fdSrc = AppStorage.get('fdSrc') as number;
     6. this.avPlayerController.initAVPlayer(this.fdSrc, false);
     7. }
     ```

     [PlayAudioPage.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/pages/PlayAudioPage.ets#L34-L40)
   * 在点击事件中，调用avPlayerController的play()方法或pause()方法，实现音频资源的播放和暂停。

     ```
     1. Column() {
     2. // ...
     3. }
     4. // ...
     5. .onClick(() => {
     6. this.isPlay = !this.isPlay;
     7. if (this.fdSrc) {
     8. this.isPlay ? this.avPlayerController.play() : this.avPlayerController.pause();
     9. }
     10. })
     ```

     [PlayAudioPage.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/pages/PlayAudioPage.ets#L54-L100)

## 基于OHAudio实现音频耳返

### 场景描述

点击进入OHAudio页面，连接有线耳机或蓝牙耳机，点击录制按钮开启耳返。开启耳返后开发者同样可以通过麦克风在耳机中实时听到自己或周围的声音，并进行耳返音频的录制，以及可以通过Slider滑块实现耳返音量的调节。录制完成后进入播放页面，播放录制的音频资源。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/XcfbXFWATBy1r6ewUSO6Sg/zh-cn_image_0000002544789547.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002046Z&HW-CC-Expire=86400&HW-CC-Sign=B763A1B12BE955B86F0A8835D29B14D152B2E98E2F487A1CBCB5986A8F20DCAB "点击放大")

### 实现原理

在C/C++侧实现耳返依赖OHAudio提供的低时延模式进行录制和播放。

1. 通过native\_audiocapturer采集麦克风数据，并将数据写入到音频录制与播放间的数据中转区，即音频的公共缓存中。
2. 读取音频的公共缓存，通过native\_audiorenderer播放音频，实现返听。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/0Q116WRpTqWBvJ-GZ-PrmA/zh-cn_image_0000002544829551.png?HW-CC-KV=V1&HW-CC-Date=20260428T002046Z&HW-CC-Expire=86400&HW-CC-Sign=3939377909F81CEAE7ED7E9B66EBD2CB217335D72427928B97F00F27924D25A0 "点击放大")

### 开发步骤

1. 录制音频数据。
   * 调用[OH\_AudioStreamBuilder\_Create()](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)，并指定[OH\_AudioStream\_Type](../harmonyos-references/capi-native-audiostream-base-h.md#oh_audiostream_type)音频流类型为AUDIOSTREAM\_TYPE\_CAPTURER，创建输入类型的音频流构造器实例，并设置输入音频流的采样率、声道数、低时延模式、采样格式、编码类型及工作场景等属性。

     ```
     1. static napi_value AudioCapturerInit(napi_env env, napi_callback_info info) {
     2. if (audioCapturer) {
     3. OH_AudioCapturer_Release(audioCapturer);
     4. OH_AudioStreamBuilder_Destroy(builder);
     5. audioCapturer = nullptr;
     6. builder = nullptr;
     7. }
     8. codecUserData = new CodecUserData();

     10. // Create builder.
     11. OH_AudioStream_Type type = AUDIOSTREAM_TYPE_CAPTURER;
     12. // Create an audio stream constructor of input type.
     13. OH_AudioStreamBuilder_Create(&builder, type);
     14. // Set the sampling rate of the audio stream.
     15. OH_AudioStreamBuilder_SetSamplingRate(builder, g_samplingRate);
     16. // Set the number of channels for the audio stream.
     17. OH_AudioStreamBuilder_SetChannelCount(builder, g_channelCount);
     18. // Set up low-latency audio streaming.
     19. OH_AudioStreamBuilder_SetLatencyMode(builder, AUDIOSTREAM_LATENCY_MODE_FAST);
     20. // Set the sampling format of the audio stream.
     21. OH_AudioStreamBuilder_SetSampleFormat(builder, AUDIOSTREAM_SAMPLE_S16LE);
     22. // Set the encoding type of the audio stream.
     23. OH_AudioStreamBuilder_SetEncodingType(builder, AUDIOSTREAM_ENCODING_TYPE_RAW);
     24. // Set a working scenario for inputting audio streams.
     25. OH_AudioStreamBuilder_SetCapturerInfo(builder, AUDIOSTREAM_SOURCE_TYPE_MIC);
     26. // ...

     28. // Create OH_AudioCapturer.
     29. OH_AudioStreamBuilder_GenerateCapturer(builder, &audioCapturer);
     30. return nullptr;
     31. }
     ```

     [AudioRecording.cpp](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/cpp/AudioRecording.cpp#L85-L122)
   * 调用[OH\_AudioCapturer\_Start()](../harmonyos-references/capi-native-audiocapturer-h.md#oh_audiocapturer_start)启动音频采集器，获取音频数据。

     ```
     1. static napi_value AudioCapturerStart(napi_env env, napi_callback_info info) {
     2. // start
     3. OH_AudioCapturer_Start(audioCapturer);
     4. return nullptr;
     5. }
     ```

     [AudioRecording.cpp](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/cpp/AudioRecording.cpp#L126-L130)
   * 调用[OH\_AudioCapturer\_Pause()](../harmonyos-references/capi-native-audiocapturer-h.md#oh_audiocapturer_pause)暂停音频流数据输入。

     ```
     1. static napi_value AudioCapturerPause(napi_env env, napi_callback_info info) {
     2. OH_AudioCapturer_Pause(audioCapturer);
     3. return nullptr;
     4. }
     ```

     [AudioRecording.cpp](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/cpp/AudioRecording.cpp#L134-L137)
   * 调用[OH\_AudioCapturer\_Stop()](../harmonyos-references/capi-native-audiocapturer-h.md#oh_audiocapturer_stop)停止音频采集器，停止音频流数据输入。

     ```
     1. static napi_value AudioCapturerStop(napi_env env, napi_callback_info info) {
     2. OH_AudioCapturer_Stop(audioCapturer);
     3. return nullptr;
     4. }
     ```

     [AudioRecording.cpp](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/cpp/AudioRecording.cpp#L141-L144)
   * 调用[OH\_AudioCapturer\_Release()](../harmonyos-references/capi-native-audiocapturer-h.md#oh_audiocapturer_release)释放输入音频流，并通过[OH\_AudioStreamBuilder\_Destroy()](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_destroy)销毁输入类型的音频流构造器。

     ```
     1. static napi_value AudioCapturerRelease(napi_env env, napi_callback_info info) {
     2. if (audioCapturer) {
     3. OH_AudioCapturer_Release(audioCapturer);
     4. if (builder) {
     5. OH_AudioStreamBuilder_Destroy(builder);
     6. }
     7. audioCapturer = nullptr;
     8. builder = nullptr;
     9. }
     10. // ...
     11. return nullptr;
     12. }
     ```

     [AudioRecording.cpp](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/cpp/AudioRecording.cpp#L148-L164)
2. 播放音频数据。
   * 调用[OH\_AudioStreamBuilder\_Create()](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)，并指定[OH\_AudioStream\_Type](../harmonyos-references/capi-native-audiostream-base-h.md#oh_audiostream_type)音频流类型为AUDIOSTREAM\_TYPE\_RENDERER，创建输出类型的音频流构造器实例，并设置输出音频流的采样率、声道数、低时延模式、音频播放回调帧长、采样格式、编码类型及工作场景等。

     ```
     1. static napi_value AudioRendererInit(napi_env env, napi_callback_info info) {
     2. if (audioRenderer) {
     3. OH_AudioRenderer_Release(audioRenderer);
     4. OH_AudioStreamBuilder_Destroy(rendererBuilder);

     6. audioRenderer = nullptr;
     7. rendererBuilder = nullptr;
     8. }

     10. // Create an audio stream builder of output type.
     11. OH_AudioStream_Type type = AUDIOSTREAM_TYPE_RENDERER;
     12. OH_AudioStreamBuilder_Create(&rendererBuilder, type);

     14. // Set the sampling rate of the audio stream.
     15. OH_AudioStreamBuilder_SetSamplingRate(rendererBuilder, g_samplingRate);
     16. // Set the number of channels for the audio stream.
     17. OH_AudioStreamBuilder_SetChannelCount(rendererBuilder, g_channelCount);
     18. // Set up low-latency audio streaming.
     19. OH_AudioStreamBuilder_SetLatencyMode(rendererBuilder, AUDIOSTREAM_LATENCY_MODE_FAST);
     20. OH_AudioStreamBuilder_SetFrameSizeInCallback(rendererBuilder, 2500);
     21. // Set the sampling format of the audio stream.
     22. OH_AudioStreamBuilder_SetSampleFormat(rendererBuilder, AUDIOSTREAM_SAMPLE_S16LE);
     23. // Set the working scenario for outputting audio streams.
     24. OH_AudioStreamBuilder_SetRendererInfo(rendererBuilder, AUDIOSTREAM_USAGE_MUSIC);
     25. OH_AudioStreamBuilder_SetRendererWriteDataCallback(rendererBuilder, AudioRendererOnWriteData, codecUserData);

     27. // Create an instance of output audio stream.
     28. OH_AudioStreamBuilder_GenerateRenderer(rendererBuilder, &audioRenderer);
     29. g_readEnd = false;
     30. g_rendererLowLatency = false;
     31. return nullptr;
     32. }
     ```

     [AudioRecording.cpp](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/cpp/AudioRecording.cpp#L168-L199)
   * 调用[OH\_AudioRenderer\_Start()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_start)输出音频数据。

     ```
     1. static napi_value AudioRendererStart(napi_env env, napi_callback_info info) {
     2. g_readEnd = false;
     3. // start
     4. OH_AudioRenderer_Start(audioRenderer);
     5. return nullptr;
     6. }
     ```

     [AudioRecording.cpp](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/cpp/AudioRecording.cpp#L203-L208)
   * 调用[OH\_AudioRenderer\_Pause()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_pause)暂停输出音频数据。

     ```
     1. static napi_value AudioRendererPause(napi_env env, napi_callback_info info) {
     2. g_readEnd = false;
     3. OH_AudioRenderer_Pause(audioRenderer);
     4. return nullptr;
     5. }
     ```

     [AudioRecording.cpp](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/cpp/AudioRecording.cpp#L212-L216)
   * 调用[OH\_AudioRenderer\_SetVolume()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_setvolume)设置音频流音量值。

     ```
     1. static napi_value AudioRendererSetVolume(napi_env env, napi_callback_info info) {
     2. size_t argc = 1;
     3. napi_value args[1] = {nullptr};
     4. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
     5. double volume = 1;
     6. napi_get_value_double(env, args[0], &volume);
     7. OH_AudioRenderer_SetVolume(audioRenderer, volume);
     8. return nullptr;
     9. }
     ```

     [AudioRecording.cpp](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/cpp/AudioRecording.cpp#L220-L228)
   * 调用[OH\_AudioRenderer\_Stop()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_stop)停止输出音频流。

     ```
     1. static napi_value AudioRendererStop(napi_env env, napi_callback_info info) {
     2. g_readEnd = false;
     3. OH_AudioRenderer_Stop(audioRenderer);
     4. return nullptr;
     5. }
     ```

     [AudioRecording.cpp](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/cpp/AudioRecording.cpp#L232-L236)
   * 调用[OH\_AudioRenderer\_Release()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_release)释放输出音频流资源，并通过OH\_AudioStreamBuilder\_Destroy()销毁输出类型的音频流构造器。

     ```
     1. static napi_value AudioRendererRelease(napi_env env, napi_callback_info info) {
     2. if (audioRenderer) {
     3. OH_AudioRenderer_Release(audioRenderer);
     4. OH_AudioStreamBuilder_Destroy(rendererBuilder);
     5. audioRenderer = nullptr;
     6. rendererBuilder = nullptr;
     7. }
     8. return nullptr;
     9. }
     ```

     [AudioRecording.cpp](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/cpp/AudioRecording.cpp#L240-L248)
3. 在页面内点击录制按钮后，通过C/C++侧定义的方法实现耳返的开启或关闭，并通过AVRecorder进行耳返音频的录制。
   * 开启耳返并录制音频。

     调用audioCapturesStart()方法获取音频数据，并调用audioRendererStart()方法将音频数据通过耳机进行输出实现返听，以及通过prepareAVRecorder()方法进行耳返音频的录制。

     ```
     1. // Start collecting audio.
     2. capturesStart() {
     3. try {
     4. // Enable in-ear monitor.
     5. if (this.isArkTS) {
     6. // ...
     7. } else {
     8. nativeRecord.audioCapturesStart();
     9. nativeRecord.audioRendererStart();
     10. }
     11. this.recorderController.prepareAVRecorder(this.getUIContext().getHostContext()!); // Start recording.
     12. this.recordSec = 0; // Initialize recording duration.
     13. this.showTime = '00:00:00'; // Initialize audio capture time.
     14. this.recordState = CommonConstants.PLAY_STARTED; // Start recording status.
     15. clearInterval(this.interval); // Clear timer.
     16. this.interval = setInterval(async () => {
     17. // ...
     18. this.recordSec++;
     19. this.showTime = FormatTimeTools.getTimesBySecond(this.recordSec); // Audio acquisition time conversion
     20. }, 1000)
     21. } catch (error) {
     22. let err = error as BusinessError;
     23. logger.error(`AudioRecording:audioCapturer start err.code = ${err.code}, err.message=${err.message}`);
     24. }
     25. }
     ```

     [InEarMonitorPage.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/pages/InEarMonitorPage.ets#L67-L104)
   * 暂停录制。

     调用pauseRecorder()方法暂停音频录制，并通过audioCapturesPause()方法及audioRendererPause()方法暂停音频数据的输入和输出，关闭音频返听。

     ```
     1. // Pause audio capture.
     2. capturesPause() {
     3. try {
     4. clearInterval(this.interval);
     5. this.recordState = CommonConstants.PLAY_PAUSED;
     6. this.recorderController.pauseRecorder(); // Pause recording.
     7. // Disable in-ear monitor.
     8. if (this.isArkTS) {
     9. // ...
     10. } else {
     11. nativeRecord.audioCapturesPause();
     12. nativeRecord.audioRendererPause();
     13. }
     14. } catch (error) {
     15. let err = error as BusinessError;
     16. logger.error(`AudioRecording:audioCapturer stop. err.code=${err.code}, err.message=${err.message}}`);
     17. }
     18. }
     ```

     [InEarMonitorPage.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/pages/InEarMonitorPage.ets#L110-L132)
   * 继续录制。

     调用audioCapturesStart()方法和audioRendererStart()方法获取并输出音频数据，开启返听，并通过resumeRecorder()恢复录制。

     ```
     1. // Continue to collect.
     2. capturesContinue() {
     3. try {
     4. // ...
     5. this.recordState = CommonConstants.PLAY_CONTINUED;
     6. // Enable in-ear monitor.
     7. if (this.isArkTS) {
     8. // ...
     9. } else {
     10. nativeRecord.audioCapturesStart();
     11. nativeRecord.audioRendererStart();
     12. }
     13. this.recorderController.resumeRecorder(); // Resume recording
     14. this.interval = setInterval(async () => {
     15. // ...
     16. this.recordSec++;
     17. this.showTime = FormatTimeTools.getTimesBySecond(this.recordSec);
     18. }, 1000);
     19. } catch (err) {
     20. logger.error(`AudioRecording:audioCapturer start err = ${JSON.stringify(err)}`);
     21. }
     22. }
     ```

     [InEarMonitorPage.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/pages/InEarMonitorPage.ets#L138-L178)
   * 调节返听音量。

     在Slider组件的onChange()事件中，调用audioRendererSetVolume()方法，并传入value值，设置返听音量。

     ```
     1. Slider({
     2. min: 0,
     3. max: 1,
     4. step: 0.1,
     5. value: this.volumeValue,
     6. })
     7. .width('75%')
     8. .onChange((value: number) => {
     9. this.volumeValue = value;
     10. if (this.isArkTS) {
     11. // ...
     12. } else {
     13. nativeRecord.audioRendererSetVolume(value);
     14. }
     15. })
     ```

     [InEarMonitorPage.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/pages/InEarMonitorPage.ets#L357-L375)
   * 停止录制。

     调用stopRecorder()方法停止录制，并通过audioCapturesStop()方法和audioRendererStop()方法实现音频流数据的输入和输出，关闭耳返。

     ```
     1. // Stop audio collection
     2. capturesStop() {
     3. clearInterval(this.interval);
     4. this.recorderController.stopRecorder(); // Stop recording.
     5. // Disable in-ear monitor.
     6. if (this.isArkTS) {
     7. // ...
     8. } else {
     9. nativeRecord.audioCapturesStop();
     10. nativeRecord.audioRendererStop();
     11. }
     12. }
     ```

     [InEarMonitorPage.ets](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor/blob/master/entry/src/main/ets/pages/InEarMonitorPage.ets#L184-L200)
4. 音频播放，请参考基于AudioLoopback实现音频耳返场景中[播放音频](bpta-audio-in-ear-monitor.md#li11370953124216)小节。

## 示例代码

* [实现音频耳返](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor)
