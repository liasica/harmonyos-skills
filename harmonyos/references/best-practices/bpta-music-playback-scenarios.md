---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-music-playback-scenarios
title: 音乐播放场景低功耗规则
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 前台任务低功耗 > 前台资源合理使用 > 音乐播放场景低功耗规则
category: best-practices
scraped_at: 2026-04-29T14:13:49+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:24372db2a7ac6528d726ab1e0372e7ea4d18fd19cc2debf05181d2ba1f161967
---

## 规则

* 音乐类应用静音时关闭音效处理算法。
* 音乐类应用播放时设置正确应用类型，走系统低功耗方案。
* 音乐类应用在后台播放时无需设置播放状态，通过接入[AVSession Kit（音视频播控服务）](../harmonyos-guides/avsession-kit.md)，设置资源的时长、播放状态（暂停、播放）、播放位置、倍速即可，不需要应用实时更新播放进度。

## 开发步骤

为了避免静音播放时冗余音效处理算法导致的快速耗电，可以通过设置当前播放实例的音效模式来解决。关闭应用音效的方法如下所示：

```
1. import { audio } from '@kit.AudioKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. audioRenderer!.setAudioEffectMode(audio.AudioEffectMode.EFFECT_NONE, (err: BusinessError) => {
4. if (err) {
5. hilog.error(0x0000, 'Sample', `Failed to set params, code is ${err.code}, message is ${err.message}`);
6. return;
7. } else {
8. hilog.info(0x0000, 'Sample', 'Callback invoked to indicate a successful audio effect mode setting.');
9. }
10. });
```

[MusicPlayRule.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/RationalUseOfFrontEndResources/entry/src/main/ets/pages/MusicPlayRule.ets#L21-L41)

设置音乐播放的usage类型为audio.StreamUsage.STREAM\_USAGE\_MUSIC，确保音乐类应用能使用系统低功耗方案。

```
1. import { audio } from '@kit.AudioKit';
2. let audioStreamInfo: audio.AudioStreamInfo = {
3. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_44100,
4. channels: audio.AudioChannel.CHANNEL_1,
5. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
6. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
7. };
8. let audioRendererInfo: audio.AudioRendererInfo = {
9. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
10. rendererFlags: 0
11. };
12. let audioRendererOptions: audio.AudioRendererOptions = {
13. streamInfo: audioStreamInfo,
14. rendererInfo: audioRendererInfo
15. };
16. audio.createAudioRenderer(audioRendererOptions, (err, data) => {
17. if (err) {
18. hilog.error(0x0000, 'Sample', `Invoke createAudioRenderer failed, code is ${err.code}, message is ${err.message}`);
19. return;
20. } else {
21. hilog.info(0x0000, 'Sample', 'Invoke createAudioRenderer succeeded.');
22. let audioRenderer = data;
23. }
24. });
```

[MusicPlayRule.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/RationalUseOfFrontEndResources/entry/src/main/ets/pages/MusicPlayRule.ets#L22-L67)

设置音乐应用后台播放时，需指定播放位置。播控中心将利用这些信息展示进度，无需频繁更新进度条，从而避免增加binder负载。

```
1. import { avSession } from '@kit.AVSessionKit';

3. const uiContext: UIContext | undefined = AppStorage.get('uiContext');
4. let context: Context = uiContext?.getHostContext()!;

6. async function setListener(): Promise<void> {
7. // Assuming that a session has been created, see the previous example for how to create a session
8. let type: avSession.AVSessionType = 'audio';
9. let session: avSession.AVSession = await avSession.createAVSession(context, 'SESSION_NAME', type);

11. // Set the duration of the property
12. let metadata: avSession.AVMetadata = {
13. assetId: '0',
14. title: 'TITLE',
15. mediaImage: 'IMAGE',
16. duration: 23000, // The duration of the resource, measured in milliseconds
17. };
18. session.setAVMetadata(metadata).then(() => {
19. hilog.info(0x0000, 'Sample', `SetAVMetadata successfully`);
20. }).catch((err: BusinessError) => {
21. hilog.error(0x0000, 'Sample', `Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}`);
22. });

24. // Set Status: Playback Status, Progress Position, Playback Speed, Cache Time
25. let playbackState: avSession.AVPlaybackState = {
26. state: avSession.PlaybackState.PLAYBACK_STATE_PLAY, // Playback status
27. position: {
28. elapsedTime: 1000, // The position that has been played, in ms
29. updateTime: new Date().getTime(), // The timestamp of when the app updated the current location, in ms
30. },
31. speed: 1.0, // Optional, the default is 1.0, the speed of playback, set according to the speed supported in the app, the system does not do verification
32. bufferedTime: 14000, // Optional, the time for which the resource is cached, in ms
33. };
34. session.setAVPlaybackState(playbackState, (err) => {
35. if (err) {
36. hilog.error(0x0000, 'Sample', `Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}`);
37. } else {
38. hilog.info(0x0000, 'Sample', `SetAVPlaybackState successfully`);
39. }
40. });
41. }
```

[MusicPlayRule.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/RationalUseOfFrontEndResources/entry/src/main/ets/pages/MusicPlayRule.ets#L27-L110)

## 调测验证

usage可以通过以下命令查看日志确认：

```
1. hdc shell
2. hilog | grep usage
```

执行效果示意如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/_YSNq_DxRdOIwd6NNPTYtw/zh-cn_image_0000002193850672.png?HW-CC-KV=V1&HW-CC-Date=20260429T061348Z&HW-CC-Expire=86400&HW-CC-Sign=75B382500BBA21B0F957B1E8608087C3566E14868815EE30F4989EC3BFE84829 "点击放大")
