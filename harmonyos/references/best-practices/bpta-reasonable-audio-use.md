---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-reasonable-audio-use
title: 音频资源合理使用
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 后台任务低功耗 > 后台硬件资源合理使用 > 音频资源合理使用
category: best-practices
scraped_at: 2026-04-28T08:22:45+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:78a3b8a3a92dbf5cd1f77cefe0157ca0cbe4653a728b64322f1405b29cf37621
---

无长时任务的应用退到后台时，禁止使用麦克风和扬声器。

## 约束

NA

## 示例

### 播音场景（audioRenderer）

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { audio } from '@kit.AudioKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // ...

7. export default class EntryAbility extends UIAbility {

9. // Create an AudioRenderer based on the service requirements at the foreground
10. onForeground(): void {
11. audio.createAudioRenderer(audioRendererOptions, ((err: BusinessError) => {}));
12. }

14. onBackground(): void {
15. // Return to the background to stop or pause
16. audioRenderer.stop((err: BusinessError) => {});
17. }
18. }
```

[AudioRenderer.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BptaUseResources/entry/src/main/ets/pages/music/AudioRenderer.ets#L7-L51)

### 播音场景（AVPlayer）

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. // ...

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onForeground(): void {
9. //Playing according to service requirements in the foreground
10. avPlayer.play()
11. .catch((err: BusinessError) => {
12. hilog.error(0x000, 'testTag', `avPlayer play failed, code=${err.code}, message=${err.message}`)
13. })
14. }

16. onBackground(): void {
17. // Return to the background to stop playing or pause
18. avPlayer.stop() // Or pause();
19. .catch((err: BusinessError) => {
20. hilog.error(0x000, 'testTag', `avPlayer stop failed, code=${err.code}, message=${err.message}`)
21. })
22. }
23. }
```

[AvPlayer.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BptaUseResources/entry/src/main/ets/pages/music/AvPlayer.ets#L13-L39)

### 播音场景（OpenSL ES）

```
1. //The foreground scene starts to play
2. SLPlayItfplayItf=nullptr;
3. (*pcmPlayerObject)->GetInterface(pcmPlayerObject,SL_IID_PLAY,&playItf);
4. (*playItf)->SetPlayState(playItf,SL_PLAYSTATE_PLAYING);
5. // Stop playing the background scene
6. (*playItf)->SetPlayState(playItf,SL_PLAYSTATE_STOPPED);
7. (*pcmPlayerObject)->Destroy(pcmPlayerObject);
8. (*engineObject)->Destroy(engineObject);
```

[OpenSL.cpp](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/BptaUseResources/entry/src/main/cpp/OpenSL.cpp#L21-L28)

### 播音场景（OHAudio）

```
1. //Construct the audio stream to play
2. OH_AudioRenderer*audioRenderer;
3. ret=OH_AudioStreamBuilder_GenerateRenderer(builder,&audioRenderer);

5. //The foreground scene starts to play
6. ret=OH_AudioRenderer_Start(audioRenderer);
7. // Stop playing the background scene
8. ret=OH_AudioRenderer_Stop(audioRenderer);
```

[OpenSL.cpp](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/BptaUseResources/entry/src/main/cpp/OpenSL.cpp#L37-L44)

### 播音场景（SoundPool）

```
1. import { fileIo as fs } from '@kit.CoreFileKit';
2. import { media } from '@kit.MediaKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. const SoundPool = async () => {

7. //Construct the audio stream to play
8. await fs.open('/test_01.mp3', fs.OpenMode.READ_ONLY).then((file: fs.File) => {
9. console.info("filefd:" + file.fd);
10. uri = 'fd://' + (file.fd).toString()
11. }) // '/test_01.mp3' is used as an example. The path of the file needs to be transferred
12. .catch((err: BusinessError) => {
13. hilog.error(0x000, 'testTag', `avPlayer stop failed, code=${err.code}, message=${err.message}`);
14. })
15. await soundPool.load(uri)
16. .then((soundId: number) => {
17. //The foreground scene starts to play
18. soundPool.play(soundId)
19. .then((data: number) => {
20. streamId = data;
21. hilog.info(0x000, 'testTag', 'setPreferredOrientation success');
22. })
23. .catch((err: BusinessError) => {
24. hilog.error(0x000, 'testTag', `soundPool play failed, code=${err.code}, message=${err.message}`);
25. })
26. //Stop playing in the background scenario: soundPool.stop (streamId);
27. })
28. .catch((err: BusinessError) => {
29. hilog.error(0x000, 'testTag', `soundPool load failed, code=${err.code}, message=${err.message}`);
30. })
31. }
```

[AvPlayer.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BptaUseResources/entry/src/main/ets/pages/music/AvPlayer.ets#L6-L78)

有关音频播放开发相关接口的使用，详情可以参考[音频播放](../harmonyos-guides/audio-playback.md)。

### 录音场景

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { audio } from '@kit.AudioKit';
4. // ...
5. export default class EntryAbility extends UIAbility {
6. // ...

8. onForeground(): void {
9. //Apply for the resources required by the system, or reapply for the resources released in onBackground ()
10. audio.createAudioCapturer(audioCapturerOptions, (err, data) => {
11. if (err) {
12. console.error(`InvokecreateAudioCapturerfailed,codeis${err.code},messageis${err.message}`);
13. } else {
14. console.info('InvokecreateAudioCapturersucceeded.');
15. }
16. });
17. }

19. onBackground(): void {
20. //Release resources when the UI is invisible
21. audioCapturer.stop((err: BusinessError) => {});
22. //Or pause();
23. }
24. }
```

[Recording.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BptaUseResources/entry/src/main/ets/pages/music/Recording.ets#L7-L57)

有关音频录制开发相关接口的使用，详情可以参考[音频录制](../harmonyos-guides/audio-recording.md)。
