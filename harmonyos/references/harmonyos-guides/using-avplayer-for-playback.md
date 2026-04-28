---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-avplayer-for-playback
title: 使用AVPlayer播放音频(ArkTS)
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(ArkTS) > 播放 > 使用AVPlayer播放音频(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:24+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:bb6be33493617e8cd21241387187169b351912acf9101eb0c1c3058bce146862
---

使用[AVPlayer](media-kit-intro.md#avplayer)可以实现端到端播放原始媒体资源，本开发指导将以完整播放一首音乐作为示例，向开发者讲解AVPlayer音频播放相关功能。如需播放PCM音频数据，请使用[AudioRenderer](using-audiorenderer-for-playback.md)。

播放的全流程包含：创建AVPlayer，设置播放资源，设置播放参数（音量/倍速/焦点模式），播放控制（播放/暂停/跳转/停止），重置，销毁资源。

在应用开发的过程中，开发者可以通过AVPlayer的state属性主动获取当前状态，或使用on('stateChange')方法监听状态变化。如果应用在音频播放器处于错误状态时执行操作，系统可能会抛出异常或产生其他未定义的行为。

**图1** 播放状态变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/LnBd4deCSDGrLZZtk5zeBg/zh-cn_image_0000002552798946.png?HW-CC-KV=V1&HW-CC-Date=20260427T234624Z&HW-CC-Expire=86400&HW-CC-Sign=658D45A911F65D0A50CFEBDB82053C579F8417764ED93F1A7D4F79C55246BB2B)

状态的详细说明请参考[AVPlayerState](../harmonyos-references/arkts-apis-media-t.md#avplayerstate9)。当播放处于prepared / playing / paused / completed状态时，播放引擎处于工作状态，这需要占用系统大量的运行内存。当客户端暂时不使用播放器时，调用reset()或release()回收内存资源，做好资源利用。

## 开发建议

当前指导仅介绍如何实现媒体资源播放，在应用开发过程中，涉及后台播放、播放冲突等情况时，请根据实际需要参考以下说明。

* 若要实现后台播放或熄屏播放，需要接入[AVSession（媒体会话）](avsession-access-scene.md)和[申请长时任务](continuous-task.md)，避免播放被系统强制中断。
* 应用在播放过程中，若播放的媒体数据涉及音频，根据系统音频管理策略（参考[处理音频焦点事件](audio-playback-concurrency.md)），可能会被其他应用打断，建议应用主动监听音频打断事件，根据内容提示做出相应处理，避免出现应用状态与预期效果不一致的问题。
* 面对设备同时连接多个音频输出设备的情况，应用可以通过[on('audioOutputDeviceChangeWithInfo')](../harmonyos-references/arkts-apis-media-avplayer.md#onaudiooutputdevicechangewithinfo11)监听音频输出设备的变化，做出相应处理。
* 若要访问在线媒体资源，需要申请 ohos.permission.INTERNET 权限。
* 若要切换听筒/扬声器，应用可以参考[音频输出设备路由切换](audio-output-device-switcher.md)。

## 开发步骤及注意事项

详细的API说明请参考[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)。

1. 创建实例createAVPlayer()，AVPlayer初始化idle状态。

   ```
   1. import { media } from '@kit.MediaKit';

   3. // 创建avPlayer实例对象。
   4. let avPlayer = await media.createAVPlayer();
   ```
2. 设置业务需要的监听事件，搭配全流程场景使用。支持的监听事件包括：

   | 事件类型 | 说明 |
   | --- | --- |
   | stateChange | 必要事件，监听播放器的state属性改变。  需要播放器在idle状态下、未调用设置资源接口前完成设置监听，若在调用设置资源接口后再设置监听，可能导致无法收到资源设置过程中上报的stateChange事件。 |
   | error | 必要事件，监听播放器的错误信息。  需要播放器在idle状态下、未调用设置资源接口前完成设置监听，若在调用设置资源接口后再设置监听，可能导致无法收到资源设置过程中上报的error事件。 |
   | durationUpdate | 用于进度条，监听进度条长度，刷新资源时长。 |
   | timeUpdate | 用于进度条，监听进度条当前位置，刷新当前时间。 |
   | seekDone | 响应API调用，监听seek()请求完成情况。  当使用seek()跳转到指定播放位置后，如果seek操作成功，将上报该事件。 |
   | speedDone | 响应API调用，监听setSpeed()请求完成情况。  当使用setSpeed()设置播放倍速后，如果setSpeed操作成功，将上报该事件。 |
   | volumeChange | 响应API调用，监听setVolume()请求完成情况。  当使用setVolume()调节播放音量后，如果setVolume操作成功，将上报该事件。 |
   | bufferingUpdate | 用于网络播放，监听网络播放缓冲信息，用于上报缓冲百分比以及缓存播放进度。 |
   | audioInterrupt | 监听音频焦点切换信息，搭配属性audioInterruptMode使用。  如果当前设备存在多个音频正在播放，音频焦点被切换（即播放其他媒体如通话等）时将上报该事件，应用可以及时处理。 |

   ```
   1. // 此处仅为示例，开发者根据需要设置合适的监听事件。
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { audio } from '@kit.AudioKit';

   5. avPlayer.on('stateChange', async (state: string, reason: media.StateChangeReason) => {
   6. // 开发者根据需要写入业务逻辑。
   7. });
   8. avPlayer.on('error', (error: BusinessError) => {
   9. // 开发者根据需要写入业务逻辑。
   10. });
   11. avPlayer.on('durationUpdate', (duration: number) => {
   12. // 开发者根据需要写入业务逻辑。
   13. });
   14. avPlayer.on('timeUpdate', (time:number) => {
   15. // 开发者根据需要写入业务逻辑。
   16. });
   17. avPlayer.on('seekDone', (seekDoneTime:number) => {
   18. // 开发者根据需要写入业务逻辑。
   19. });
   20. avPlayer.on('speedDone', (speed:number) => {
   21. // 开发者根据需要写入业务逻辑。
   22. });
   23. avPlayer.on('volumeChange', (vol: number) => {
   24. // 开发者根据需要写入业务逻辑。
   25. });
   26. avPlayer.on('bufferingUpdate', (infoType: media.BufferingInfoType, value: number) => {
   27. // 开发者根据需要写入业务逻辑。
   28. });
   29. avPlayer.on('audioInterrupt', (info: audio.InterruptEvent) => {
   30. // 开发者根据需要写入业务逻辑。
   31. });
   ```
3. 设置资源：设置属性url，AVPlayer进入initialized状态。

   说明

   下面代码示例中的url仅作示意使用，开发者需根据实际情况，确认资源有效性并设置：

   * 如果使用本地资源播放，必须确认资源文件可用，并使用应用沙箱路径访问对应资源，参考[获取应用文件路径](application-context-stage.md#获取应用文件路径)。应用沙箱的介绍及如何向应用沙箱推送文件，请参考[文件管理](app-sandbox-directory.md)。
   * 如果使用网络播放路径，需[声明权限](declare-permissions.md)：ohos.permission.INTERNET。
   * 可以使用ResourceManager.[getRawFd](../harmonyos-references/js-apis-resource-manager.md#getrawfd9)打开HAP资源文件描述符。
   * 需要使用[支持的播放格式与协议](media-kit-intro.md#支持的格式与协议)。

   ```
   1. let url = 'https://xxx.xxx.xxx.mp3';
   2. if (avPlayer == null) {
   3. return;
   4. }
   5. avPlayer.url = url;
   ```
4. （可选）设置音频渲染：只允许在initialized状态下，第一次调用prepare()之前设置，以便音频渲染器信息在之后生效。若媒体源包含视频，则usage默认值为STREAM\_USAGE\_MOVIE，否则usage默认值为STREAM\_USAGE\_MUSIC。rendererFlags默认值为0。

   为了确保音频行为符合使用预期，建议根据具体业务场景和实际需求，主动配置[audio.AudioRendererInfo](../harmonyos-references/arkts-apis-audio-i.md#audiorendererinfo8)，为音频选择恰当的流类型[usage](using-right-streamusage-and-sourcetype.md)。

   ```
   1. import { audio } from '@kit.AudioKit';

   3. avPlayer.audioRendererInfo = {
   4. usage: audio.StreamUsage.STREAM_USAGE_MOVIE,
   5. rendererFlags: 0
   6. }
   ```
5. 准备播放：调用 prepare()方法进入准备播放阶段，AVPlayer 将切换至 prepared 状态，此时可获取视频时长（duration）并调整音量参数。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';

   3. avPlayer.prepare((err: BusinessError) => {
   4. if (err) {
   5. console.error('Failed to prepare,error message is :' + err.message);
   6. } else {
   7. console.info('Succeeded in preparing');
   8. }
   9. });
   ```
6. 音频播控：播放play()、暂停pause()、跳转seek()、停止stop() 等操作。

   说明

   在API version 23及之后版本中，播放音频时会跳过静音帧。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';

   3. // 播放操作。
   4. avPlayer.play().then(() => {
   5. console.info('Succeeded in playing');
   6. }, (err: BusinessError) => {
   7. console.error('Failed to play,error message is :' + err.message);
   8. });
   9. // 暂停操作。
   10. avPlayer.pause((err: BusinessError) => {
   11. if (err) {
   12. console.error('Failed to pause,error message is :' + err.message);
   13. } else {
   14. console.info('Succeeded in pausing');
   15. }
   16. });
   17. // 跳转操作。
   18. let seekTime: number = 1000;
   19. avPlayer.seek(seekTime, media.SeekMode.SEEK_PREV_SYNC);
   20. // 停止操作。
   21. avPlayer.stop((err: BusinessError) => {
   22. if (err) {
   23. console.error('Failed to stop,error message is :' + err.message);
   24. } else {
   25. console.info('Succeeded in stopping');
   26. }
   27. });
   ```
7. （可选）更换资源：调用reset()方法重置播放资源，AVPlayer重新进入idle状态，此时可重新设置资源url。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';

   3. await avPlayer.reset((err: BusinessError) => {
   4. avPlayer.url = url;
   5. if (err) {
   6. console.error('Failed to reset,error message is :' + err.message);
   7. } else {
   8. console.info('Succeeded in resetting');
   9. }
   10. });
   11. // 更换url。
   12. let url = 'https://xxx.xxx.xxx.mp3';
   13. if (avPlayer == null) {
   14. return;
   15. }
   16. avPlayer.url = url;
   ```
8. 退出播放：调用release()销毁实例，AVPlayer进入released状态，退出播放。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';

   3. avPlayer.release((err: BusinessError) => {
   4. if (err) {
   5. console.error('Failed to release,error message is :' + err.message);
   6. } else {
   7. console.info('Succeeded in releasing');
   8. }
   9. });
   ```

## 运行完整示例

参考以下示例，完整地播放一首音乐，实现起播后3s暂停，暂停3s重新播放的效果。

1. 新建工程，下载[示例工程](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/AVPlayer/AVPlayerArkTSAudio)，并将示例工程的以下资源复制到对应目录。

   ```
   1. AVPlayerArkTSAudio
   2. entry/src/main/ets/
   3. └── pages
   4. └── Index.ets (播放界面)
   5. entry/src/main/resources/
   6. ├── base
   7. │   ├── element
   8. │   │   ├── color.json
   9. │   │   ├── float.json
   10. │   │   └── string.json
   11. │   └── media
   12. │       ├── ic_video_play.svg  (播放键图片资源)
   13. │       └── ic_video_pause.svg (暂停键图片资源)
   14. └── rawfile
   15. └── test_01.mp3 （音频资源）
   ```
2. 编译新建工程并运行。
