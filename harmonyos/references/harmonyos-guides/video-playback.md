---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-playback
title: 使用AVPlayer播放视频(ArkTS)
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(ArkTS) > 播放 > 使用AVPlayer播放视频(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:23+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:c188bc1b04b326e0a953df60870b2cf5c6c3c48852711eb64ada7ac7d1bcdb8e
---

当前提供两种视频播放开发的方案：

* [AVPlayer](media-kit-intro.md#avplayer)：功能较完善的音视频播放ArkTS/JS API，集成了流媒体和本地资源解析，媒体资源解封装，视频解码和渲染功能，适用于对媒体资源进行端到端播放的场景，可直接播放mp4、mkv等格式的视频文件。
* Video组件：封装了视频播放的基础能力，需要设置数据源及基础信息即可播放视频，但相对扩展能力较弱。Video组件由ArkUI提供能力，相关指导请参考UI开发文档-[Video组件](arkts-common-components-video-player.md)。

本开发指导将介绍如何使用AVPlayer开发视频播放功能，以完整播放一个视频作为示例，实现端到端播放原始媒体资源。

播放的全流程包含：创建AVPlayer，设置播放资源和窗口，设置播放参数（音量/倍速/缩放模式），播放控制（播放/暂停/跳转/停止），重置，销毁资源。在进行应用开发的过程中，开发者可以通过AVPlayer的state属性主动获取当前状态或使用on('stateChange')方法监听状态变化。如果应用在视频播放器处于错误状态时执行操作，系统可能会抛出异常或生成其他未定义的行为。

**图1** 播放状态变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/rL-Mt6tMR4GqgCX3ECfW6w/zh-cn_image_0000002589244901.png?HW-CC-KV=V1&HW-CC-Date=20260429T053522Z&HW-CC-Expire=86400&HW-CC-Sign=E305AB54D90099CCD5E02DD07D01417AA3872C604E493DD9055C4F4FEB39E5E9)

状态的详细说明请参考[AVPlayerState](../harmonyos-references/arkts-apis-media-t.md#avplayerstate9)。当播放处于prepared / playing / paused / completed状态时，播放引擎处于工作状态，这需要占用系统较多的运行内存。当客户端暂时不使用播放器时，调用reset()或release()回收内存资源，做好资源释放。

## 开发建议

当前指导仅介绍如何实现媒体资源播放，在应用开发过程中可能会涉及后台播放、播放冲突等情况，请根据实际需要参考以下说明。

* 如果要实现后台播放或熄屏播放，需要接入[AVSession（媒体会话）](avsession-access-scene.md)和[申请长时任务](continuous-task.md)，避免播放被系统强制中断。
* 应用在播放过程中，若播放的媒体数据涉及音频，根据系统音频管理策略（参考[处理音频焦点事件](audio-playback-concurrency.md)），可能会被其他应用打断，建议应用主动监听音频打断事件，根据其内容提示，做出相应的处理，避免出现应用状态与预期效果不一致的问题。
* 面对设备同时连接多个音频输出设备的情况，应用可以通过[on('audioOutputDeviceChangeWithInfo')](../harmonyos-references/arkts-apis-media-avplayer.md#onaudiooutputdevicechangewithinfo11)监听音频输出设备的变化，从而做出相应处理。
* 如果需要访问在线媒体资源，需要申请 ohos.permission.INTERNET 权限。

## 开发步骤及注意事项

详细的API说明请参考[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)。

1. 调用createAVPlayer()创建AVPlayer实例，初始化进入idle状态。

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
   | bitrateDone | 响应API调用，用于HLS协议流，监听setBitrate()请求完成情况。  当使用setBitrate()指定播放比特率后，如果setBitrate操作成功，将上报该事件。 |
   | availableBitrates | 用于HLS协议流，监听HLS资源的可选bitrates，用于setBitrate()。 |
   | bufferingUpdate | 用于网络播放，监听网络播放缓冲信息。 |
   | startRenderFrame | 用于视频播放，监听视频播放首帧渲染时间。  当AVPlayer首次起播进入playing状态后，等到首帧视频画面被渲染到显示画面时，将上报该事件。应用通常可以利用此事件上报，进行视频封面移除，达成封面与视频画面的顺利衔接。 |
   | videoSizeChange | 用于视频播放，监听视频播放的宽高信息，可用于调整窗口大小、比例。 |
   | audioInterrupt | 监听音频焦点切换信息，搭配属性audioInterruptMode使用。  如果当前设备存在多个媒体正在播放，音频焦点被切换（即播放其他媒体如通话等）时将上报该事件，应用可以及时处理。 |

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
   26. avPlayer.on('bitrateDone', (bitrate:number) => {
   27. // 开发者根据需要写入业务逻辑。
   28. });
   29. avPlayer.on('availableBitrates', (bitrates: Array<number>) => {
   30. // 开发者根据需要写入业务逻辑。
   31. });
   32. avPlayer.on('bufferingUpdate', (infoType: media.BufferingInfoType, value: number) => {
   33. // 开发者根据需要写入业务逻辑。
   34. });
   35. avPlayer.on('startRenderFrame', () => {
   36. // 开发者根据需要写入业务逻辑。
   37. });
   38. avPlayer.on('videoSizeChange', (width: number, height: number) => {
   39. // 开发者根据需要写入业务逻辑。
   40. });
   41. avPlayer.on('audioInterrupt', (info: audio.InterruptEvent) => {
   42. // 开发者根据需要写入业务逻辑。
   43. });
   ```
3. 设置资源：设置属性url，AVPlayer进入initialized状态。

   说明

   下面代码示例中的url仅作示意使用，开发者需根据实际情况，确认资源有效性并设置：

   * 如果使用本地资源播放，必须确认资源文件可用，并使用应用沙箱路径访问对应资源，参考[获取应用文件路径](application-context-stage.md#获取应用文件路径)。应用沙箱的介绍及如何向应用沙箱推送文件，请参考[文件管理](app-sandbox-directory.md)。
   * 如果使用网络播放路径，需[声明权限](declare-permissions.md)：ohos.permission.INTERNET。
   * 可以使用ResourceManager.[getRawFd](../harmonyos-references/js-apis-resource-manager.md#getrawfd9)打开HAP资源文件描述符。
   * 需要使用[支持的播放格式与协议](media-kit-intro.md#支持的格式与协议)。

   ```
   1. let url = 'https://xxx.xxx.xxx.mp4';
   2. if (avPlayer == null) {
   3. return;
   4. }
   5. avPlayer.url = url;
   ```
4. 设置窗口：获取并设置属性surfaceId，用于设置显示画面。

   应用需要从XComponent组件获取surfaceId，获取方式请参考[getXComponentSurfaceId](../harmonyos-references/ts-basic-components-xcomponent.md#getxcomponentsurfaceid9)。

   ```
   1. // 通过接口getXComponentSurfaceId获取surfaceId。
   2. let surfaceId = '';
   3. if (avPlayer == null) {
   4. return;
   5. }
   6. if (surfaceId === '') {
   7. return;
   8. }
   9. avPlayer.surfaceId = surfaceId;
   ```
5. 准备播放：调用prepare()，AVPlayer进入prepared状态，此时可以获取duration，设置缩放模式、音量等。

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
6. 视频播控：播放play()，暂停pause()，跳转seek()，停止stop() 等操作。

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
7. （可选）更换资源：调用reset()重置资源，AVPlayer重新进入idle状态，允许更换资源url。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';

   3. avPlayer.reset((err: BusinessError) => {
   4. avPlayer.url = url;
   5. if (err) {
   6. console.error('Failed to reset,error message is :' + err.message);
   7. } else {
   8. console.info('Succeeded in resetting');
   9. }
   10. });
   11. // 更换url。
   12. let url = 'https://xxx.xxx.xxx.mp4';
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

1. 新建工程，下载[示例工程](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/AVPlayer/AVPlayerArkTSVideo)，并将示例工程的以下资源复制到对应目录。

   ```
   1. AVPlayerArkTSVideo
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
   15. └── test1.mp4 （视频资源）
   ```
2. 编译新建工程并运行。
