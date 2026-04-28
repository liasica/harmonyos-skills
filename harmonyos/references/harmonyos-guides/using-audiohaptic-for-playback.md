---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-audiohaptic-for-playback
title: 使用AudioHaptic开发音振协同播放功能(ArkTs)
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频播放 > 使用AudioHaptic开发音振协同播放功能(ArkTs)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dafe8a556247555e83d6d99ef5437ce208df7e2d13c18a8963acfb5e4c6e24eb
---

AudioHaptic提供音频与振动协同播放及管理的方法，适用于需要在播放音频时同步发起振动的场景，如来电铃声随振、键盘按键反馈、消息通知反馈等。

## 开发指导

使用AudioHaptic播放音频并同步开启振动，涉及到音频及振动资源的管理、音频时延模式及音频流使用类型的配置、音振播放器的创建及管理等。本开发指导将以一次音振协同播放的过程为例，向开发者讲解如何使用AudioHaptic进行音振协同播放，建议配合[audioHaptic](../harmonyos-references/js-apis-audiohaptic.md)的API说明阅读。

### 权限申请

如果应用创建的AudioHapticPlayer需要触发振动，则需要校验应用是否拥有该权限：ohos.permission.VIBRATE。

1. [声明权限](declare-permissions.md)。
2. [向用户申请授权](request-user-authorization.md)。

### 开发步骤及注意事项

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/Media/Audio/AudioRendererSampleJS)。

1. 获取音振管理器实例，并注册音频及振动资源，资源支持情况可以查看[AudioHapticManager](../harmonyos-references/js-apis-audiohaptic.md#audiohapticmanager)。

   说明

   开发者可通过如下两种方式注册资源：

   * 方式1：使用[registerSource](../harmonyos-references/js-apis-audiohaptic.md#registersource)接口，通过文件URI来注册资源。
   * 方式2（推荐）：从API version 20开始，支持使用[registerSourceFromFd](../harmonyos-references/js-apis-audiohaptic.md#registersourcefromfd20)接口，通过文件描述符来注册资源，更便于开发者使用。

   ```
   1. import { audio, audioHaptic } from '@kit.AudioKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { common } from '@kit.AbilityKit';

   5. let audioHapticManagerInstance: audioHaptic.AudioHapticManager = audioHaptic.getAudioHapticManager();

   7. // 单个应用最多支持同时注册128个资源，超过之后将会注册失败（返回注册的资源ID为负数）。
   8. // 推荐应用合理控制注册资源数量，对于不再需要使用的资源，建议及时取消注册。

   10. // ...
   11. // 方法1：使用registerSource接口注册资源。
   12. let audioUri = 'data/audioTest.wav'; // 此处仅作示例，实际使用时需要将文件替换为应用目标音频资源的Uri。
   13. let hapticUri = 'data/hapticTest.json'; // 此处仅作示例，实际使用时需要将文件替换为应用目标振动资源的Uri。
   14. let idForUri = 0;

   16. audioHapticManagerInstance.registerSource(audioUri, hapticUri).then((value: number) => {
   17. console.info(`Promise returned to indicate that the source id of the registered source ${value}.`);
   18. idForUri = value;
   19. // ...
   20. }).catch((err: BusinessError) => {
   21. console.error(`Failed to register source ${err}`);
   22. // ...
   23. });
   24. // ...
   25. // 方法2:使用registerSourceFromFd接口注册资源。
   26. // 此处仅作示例,实际使用时需要将文件替换为应用rawfile目录下的对应文件。
   27. let audioFile = context.resourceManager.getRawFdSync('audioTest.ogg');
   28. let audioFd: audioHaptic.AudioHapticFileDescriptor = {
   29. fd: audioFile.fd,
   30. offset: audioFile.offset,
   31. length: audioFile.length,
   32. };
   33. // 此处仅作示例,实际使用时需要将文件替换为应用rawfile目录下的对应文件。
   34. let hapticFile = context.resourceManager.getRawFdSync('hapticTest.json');
   35. let hapticFd: audioHaptic.AudioHapticFileDescriptor = {
   36. fd: hapticFile.fd,
   37. offset: hapticFile.offset,
   38. length: hapticFile.length,
   39. };
   40. audioHapticManagerInstance.registerSourceFromFd(audioFd, hapticFd).then((value: number) => {
   41. console.info('Succeeded in doing registerSourceFromFd.');
   42. idForFd = value;
   43. // ...
   44. }).catch((err: BusinessError) => {
   45. console.error(`Failed to registerSourceFromFd. Code: ${err.code}, message: ${err.message}`);
   46. // ...
   47. });
   ```
2. 设置音振播放器参数，各参数作用可以查看[AudioHapticManager](../harmonyos-references/js-apis-audiohaptic.md#audiohapticmanager)。

   ```
   1. let latencyMode: audioHaptic.AudioLatencyMode = audioHaptic.AudioLatencyMode.AUDIO_LATENCY_MODE_FAST;
   2. audioHapticManagerInstance.setAudioLatencyMode(idForFd, latencyMode);

   4. let usage: audio.StreamUsage = audio.StreamUsage.STREAM_USAGE_NOTIFICATION;
   5. audioHapticManagerInstance.setStreamUsage(idForFd, usage);
   ```
3. 调用[createPlayer](../harmonyos-references/js-apis-audiohaptic.md#createplayer)方法，创建AudioHapticPlayer实例。

   ```
   1. let options: audioHaptic.AudioHapticPlayerOptions = {muteAudio: false, muteHaptics: false};
   2. let audioHapticPlayer: audioHaptic.AudioHapticPlayer | undefined = undefined;
   3. // ...
   4. audioHapticManagerInstance.createPlayer(idForFd, options).then((value: audioHaptic.AudioHapticPlayer) => {
   5. console.info(`Create the audio haptic player successfully.`);
   6. audioHapticPlayer = value;
   7. // ...
   8. }).catch((err: BusinessError) => {
   9. console.error(`Failed to create player ${err}`);
   10. // ...
   11. });
   ```
4. 调用[start](../harmonyos-references/js-apis-audiohaptic.md#start)方法，开启音频播放并同步开启振动。

   ```
   1. audioHapticPlayer.start().then(() => {
   2. console.info(`Promise returned to indicate that start playing successfully.`);
   3. // ...
   4. }).catch((err: BusinessError) => {
   5. console.error(`Failed to start playing. ${err}`);
   6. // ...
   7. });
   ```
5. 调用[stop](../harmonyos-references/js-apis-audiohaptic.md#stop)方法，停止音频播放并同步停止振动。

   ```
   1. audioHapticPlayer.stop().then(() => {
   2. console.info(`Promise returned to indicate that stop playing successfully.`);
   3. // ...
   4. }).catch((err: BusinessError) => {
   5. console.error(`Failed to stop playing. ${err}`);
   6. // ...
   7. });
   ```
6. 调用[release](../harmonyos-references/js-apis-audiohaptic.md#release)方法，释放AudioHapticPlayer实例。

   ```
   1. audioHapticPlayer.release().then(() => {
   2. console.info(`Promise returned to indicate that release the audio haptic player successfully.`);
   3. // ...
   4. }).catch((err: BusinessError) => {
   5. console.error(`Failed to release the audio haptic player. ${err}`);
   6. // ...
   7. });
   ```
7. 调用[unregisterSource](../harmonyos-references/js-apis-audiohaptic.md#unregistersource)方法，将已注册的音频及振动资源移除注册。

   ```
   1. // 对于不再需要使用的资源，建议应用及时取消注册，避免出现资源泄漏或资源数量超上限等问题。
   2. audioHapticManagerInstance.unregisterSource(idForFd).then(() => {
   3. console.info(`Promise returned to indicate that unregister source successfully`);
   4. // ...
   5. }).catch((err: BusinessError) => {
   6. console.error(`Failed to unregister source ${err}`);
   7. // ...
   8. });
   ```
