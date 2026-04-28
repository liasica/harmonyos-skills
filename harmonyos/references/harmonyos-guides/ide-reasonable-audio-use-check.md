---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-reasonable-audio-use-check
title: @performance/reasonable-audio-use-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/reasonable-audio-use-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:16+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:19ef04d63382c6f5634f9b068ecee8bf6628e48b5f82eb7c660c63915595051a
---

无长时任务的应用退到后台时，禁止使用麦克风或扬声器。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/reasonable-audio-use-check": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { audio } from '@kit.AudioKit';
3. import { media } from '@kit.MediaKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. let audioStreamInfo: audio.AudioStreamInfo = {
7. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
8. channels: audio.AudioChannel.CHANNEL_2, // 通道。
9. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
10. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
11. };
12. const audioRendererOptions: audio.AudioRendererOptions = {
13. streamInfo: audioStreamInfo,
14. rendererInfo: {
15. usage: audio.StreamUsage.STREAM_USAGE_UNKNOWN,
16. rendererFlags: 1
17. }
18. }
19. let audioCapturerInfo: audio.AudioCapturerInfo = {
20. source: audio.SourceType.SOURCE_TYPE_MIC, // 音源类型：Mic音频源。根据业务场景配置，参考SourceType。
21. capturerFlags: 0 // 音频采集器标志。
22. };
23. let audioCapturerOptions: audio.AudioCapturerOptions = {
24. streamInfo: audioStreamInfo,
25. capturerInfo: audioCapturerInfo
26. };
27. let audioRenderer: audio.AudioRenderer
28. let avPlayer: media.AVPlayer
29. let audioCapturer: audio.AudioCapturer;

31. export default class EntryAbility extends UIAbility {
32. // Create an AudioRenderer based on the service requirements at the foreground
33. onForeground(): void {
34. audio.createAudioRenderer(audioRendererOptions, ((err, data) => {
35. audioRenderer = data;
36. }));
37. avPlayer.play();
38. audio.createAudioCapturer(audioCapturerOptions, (err, data) => {
39. audioCapturer = data;
40. });
41. }

43. onBackground(): void {
44. // Return to the background to stop or pause
45. audioRenderer.stop((err: BusinessError) => {
46. });
47. avPlayer.stop();
48. audioCapturer.stop((err: BusinessError) => {
49. });
50. }
51. }
```

## 反例

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { audio } from '@kit.AudioKit';
3. import { media } from '@kit.MediaKit';

5. let audioStreamInfo: audio.AudioStreamInfo = {
6. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
7. channels: audio.AudioChannel.CHANNEL_2, // 通道。
8. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
9. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
10. };
11. const audioRendererOptions: audio.AudioRendererOptions = {
12. streamInfo: audioStreamInfo,
13. rendererInfo: {
14. usage: audio.StreamUsage.STREAM_USAGE_UNKNOWN,
15. rendererFlags: 1
16. }
17. }
18. let audioCapturerInfo: audio.AudioCapturerInfo = {
19. source: audio.SourceType.SOURCE_TYPE_MIC, // 音源类型：Mic音频源。根据业务场景配置，参考SourceType。
20. capturerFlags: 0 // 音频采集器标志。
21. };
22. let audioCapturerOptions: audio.AudioCapturerOptions = {
23. streamInfo: audioStreamInfo,
24. capturerInfo: audioCapturerInfo
25. };
26. let audioRenderer: audio.AudioRenderer
27. let avPlayer: media.AVPlayer
28. let audioCapturer: audio.AudioCapturer;

30. export default class EntryAbility extends UIAbility {
31. // Create an AudioRenderer based on the service requirements at the foreground
32. onForeground(): void {
33. audio.createAudioRenderer(audioRendererOptions, ((err, data) => {
34. audioRenderer = data;
35. }));
36. avPlayer.play();
37. audio.createAudioCapturer(audioCapturerOptions, (err, data) => {
38. audioCapturer = data;
39. });
40. }

42. onBackground(): void {
43. }
44. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
