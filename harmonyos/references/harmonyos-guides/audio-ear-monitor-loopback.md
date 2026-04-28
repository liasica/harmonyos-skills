---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-ear-monitor-loopback
title: 实现音频低时延耳返
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频录制 > 实现音频低时延耳返
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9f380b51b23bdf702c4ee9d3aa3a1c21538eb23c1eb3e4f2550176274366e97a
---

从API version 20开始，支持音频低时延耳返。

AudioLoopback是音频返听器，可将音频以更低时延的方式实时传输到耳机中，让用户可以实时听到自己或者其他的相关声音。

常用于K歌类应用，将录制的人声和背景音乐实时传送到耳机中，使用户通过反馈即时进行调整，获得更好的使用体验。

当启用音频返听时，系统会创建低时延渲染器与低时延采集器，实现低时延耳返功能。采集的音频直接通过内部路由返回到渲染器。对于渲染器，其音频焦点策略与[STREAM\_USAGE\_MUSIC](../harmonyos-references/arkts-apis-audio-e.md#streamusage)相匹配。对于采集器，其音频焦点策略与[SOURCE\_TYPE\_MIC](../harmonyos-references/arkts-apis-audio-e.md#sourcetype8)相匹配。

输入/输出设备由系统自动选择。如果当前输入/输出不支持低时延，则音频返听无法启用。在运行过程中，如果音频焦点被另一个音频流抢占，输入/输出设备切换到不支持低时延的设备，系统会自动禁用音频返听。

## 使用前提

* 当前仅支持通过有线耳机实现低时延返听功能，音频由有线耳机进行采集并播放。
* 低功耗渲染器和低时延渲染器在API version 20不能实现并发。若要启用渲染器，建议采用[STREAM\_USAGE\_UNKNOWN](../harmonyos-references/arkts-apis-audio-e.md#streamusage)；系统内决策采用[STREAM\_USAGE\_MUSIC](../harmonyos-references/arkts-apis-audio-e.md#streamusage)创建普通渲染器。

## 开发指导

使用AudioLoopback音频返听涉及到[isAudioLoopbackSupported](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#isaudioloopbacksupported20)返听能力查询、AudioLoopback实例创建、返听音量设置、返听状态监听与返听启用禁用等。本开发指导将以一次启用返听的过程为例，向开发者讲解如何使用AudioLoopback进行音频返听，建议搭配[AudioLoopback](../harmonyos-references/arkts-apis-audio-audioloopback.md)的API说明阅读。

下图展示了AudioLoopback的状态变化。在创建实例后，调用对应的方法可以进入指定的状态实现对应行为。

需要注意的是在确定的状态执行不合适的方法可能导致AudioLoopback发生错误，建议开发者在调用状态转换的方法前进行状态检查，避免程序运行产生预期以外的结果。

**AudioLoopback状态变化示意图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/fsZ9jfyeRoi1cknxKzibGw/zh-cn_image_0000002583438577.png?HW-CC-KV=V1&HW-CC-Date=20260427T234534Z&HW-CC-Expire=86400&HW-CC-Sign=E257CF58BD377EAF84651214062F04FF337CF32AD1AF47D166089E4DF17ED247)

使用[on('statusChange')](../harmonyos-references/arkts-apis-audio-audioloopback.md#onstatuschange20)方法可以监听AudioLoopback的状态变化，每个状态对应值与说明见[AudioLoopbackStatus](../harmonyos-references/arkts-apis-audio-e.md#audioloopbackstatus20)。

### 开发步骤及注意事项

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/Media/Audio/AudioCaptureSampleJS)。

1. 查询返听能力并创建AudioLoopback实例，音频返听模式可以查看[AudioLoopbackMode](../harmonyos-references/arkts-apis-audio-e.md#audioloopbackmode20)。

   说明

   返听需要申请麦克风权限ohos.permission.MICROPHONE，申请方式参考：[向用户申请授权](request-user-authorization.md)。

   ```
   1. import { audio } from '@kit.AudioKit'; // 导入audio模块。
   2. import { BusinessError } from '@kit.BasicServicesKit'; // 导入BusinessError。
   3. // ...
   4. let mode: audio.AudioLoopbackMode = audio.AudioLoopbackMode.HARDWARE;
   5. let audioLoopback: audio.AudioLoopback | undefined = undefined;
   6. // ...
   7. let isSupported = audio.getAudioManager().getStreamManager().isAudioLoopbackSupported(mode);
   8. if (isSupported) {
   9. audio.createAudioLoopback(mode).then((loopback) => {
   10. console.info('Invoke createAudioLoopback succeeded.');
   11. // ...
   12. audioLoopback = loopback;
   13. }).catch((err: BusinessError) => {
   14. console.error(`Invoke createAudioLoopback failed, code is ${err.code}, message is ${err.message}.`);
   15. // ...
   16. });
   17. } else {
   18. console.error('Audio loopback is unsupported.');
   19. // ...
   20. }
   ```
2. 调用[getStatus](../harmonyos-references/arkts-apis-audio-audioloopback.md#getstatus20)方法，查询当前返听状态。

   注意

   音频返听状态受音频焦点、低时延管控、采集与播放设备等因素影响。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit'; // 导入BusinessError。
   2. // ...
   3. audioLoopback.getStatus().then((status: audio.AudioLoopbackStatus) => {
   4. console.info(`getStatus success, status is ${status}.`);
   5. // ...
   6. }).catch((err: BusinessError) => {
   7. console.error(`getStatus failed, code is ${err.code}, message is ${err.message}.`);
   8. // ...
   9. })
   ```
3. 调用[setVolume](../harmonyos-references/arkts-apis-audio-audioloopback.md#setvolume20)方法，设置音频返听音量。

   注意

   * 在启用返听前设置音量，音量将在启用返听成功后生效。
   * 在启用返听后设置音量，音量将立即生效。
   * 启用返听前未设置音量，启用返听时将采用默认音量0.5。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit'; // 导入BusinessError。
   2. // ...
   3. try {
   4. await audioLoopback.setVolume(volume);
   5. console.info(`Invoke setVolume ${volume} succeeded.`);
   6. // ...
   7. } catch (err) {
   8. console.error(`Invoke setVolume failed, code is ${err.code}, message is ${err.message}.`);
   9. // ...
   10. }
   ```
4. 从API21开始，支持调用[setReverbPreset](../harmonyos-references/arkts-apis-audio-audioloopback.md#setreverbpreset21)方法，设置音频返听的混响模式。

   注意

   * 在启用返听前设置混响模式，混响模式将在启用返听成功后生效。
   * 在启用返听后设置混响模式，混响模式将立即生效。
   * 启用返听前未设置混响模式，启用返听时将采用默认混响模式[THEATER](../harmonyos-references/arkts-apis-audio-e.md#audioloopbackreverbpreset21)。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit'; // 导入BusinessError。
   2. // ...
   3. try {
   4. audioLoopback.setReverbPreset(preset);
   5. console.info(`setReverbPreset( ${preset} succeeded.`);
   6. // ...
   7. currentReverbPreset = audioLoopback.getReverbPreset(); // 查询当前的混响模式，防止设置失败。
   8. } catch (err) {
   9. console.error(`setReverbPreset( failed, code is ${err.code}, message is ${err.message}.`);
   10. // ...
   11. }
   ```
5. 从API21开始，支持调用[getReverbPreset](../harmonyos-references/arkts-apis-audio-audioloopback.md#getreverbpreset21)方法，查询当前的音频返听的混响模式。

   注意

   若未设置混响模式，查询得到将是默认混响模式[THEATER](../harmonyos-references/arkts-apis-audio-e.md#audioloopbackreverbpreset21)。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit'; // 导入BusinessError。
   2. // ...
   3. try {
   4. let reverbPreset = audioLoopback.getReverbPreset();
   5. } catch (err) {
   6. console.error(`getReverbPreset:ERROR: ${err}`);
   7. // ...
   8. }
   ```
6. 从API21开始，支持调用[setEqualizerPreset](../harmonyos-references/arkts-apis-audio-audioloopback.md#setequalizerpreset21)方法，设置音频返听的均衡器类型。

   注意

   * 在启用返听前设置均衡器类型，均衡器类型将在启用返听成功后生效。
   * 在启用返听后设置均衡器类型，均衡器类型将立即生效。
   * 启用返听前未设置均衡器类型，启用返听时将采用默认均衡器类型[FULL](../harmonyos-references/arkts-apis-audio-e.md#audioloopbackequalizerpreset21)。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. try {
   3. audioLoopback.setEqualizerPreset(audio.AudioLoopbackEqualizerPreset.FULL);
   4. } catch (err) {
   5. console.error(`setEqualizerPreset :ERROR: ${err}`);
   6. }
   ```
7. 从API21开始，支持调用[getEqualizerPreset](../harmonyos-references/arkts-apis-audio-audioloopback.md#getequalizerpreset21)方法，查询当前的音频返听的均衡器类型。

   注意

   若未设置均衡器类型，查询得到将是默认均衡器类型[FULL](../harmonyos-references/arkts-apis-audio-e.md#audioloopbackequalizerpreset21)。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit'; // 导入BusinessError。
   2. // ...
   3. try {
   4. let equalizerPreset = audioLoopback.getEqualizerPreset();
   5. } catch (err) {
   6. console.error(`getEqualizerPreset:ERROR: ${err}`);
   7. // ...
   8. }
   ```
8. 调用[enable](../harmonyos-references/arkts-apis-audio-audioloopback.md#enable20)方法，启用或禁用音频返听功能。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit'; // 导入BusinessError。
   2. // ...
   3. // 设置监听事件，启用音频返听。
   4. async function enable(updateCallback?: (msg: string, isError: boolean) => void): Promise<void> {
   5. if (audioLoopback !== undefined) {
   6. try {
   7. let status = await audioLoopback.getStatus();
   8. if (status == audio.AudioLoopbackStatus.AVAILABLE_IDLE) {
   9. // 注册监听。
   10. audioLoopback.on('statusChange', statusChangeCallback);
   11. // 启动返听。
   12. let success = await audioLoopback.enable(true);
   13. if (success) {
   14. console.info('Invoke enable succeeded');
   15. // ...
   16. } else {
   17. status = await audioLoopback.getStatus();
   18. statusChangeCallback(status);
   19. }
   20. } else {
   21. statusChangeCallback(status);
   22. }
   23. } catch (err) {
   24. console.error(`Invoke enable failed, code is ${err.code}, message is ${err.message}.`);
   25. // ...
   26. }
   27. } else {
   28. console.error('Audio loopback not created.');
   29. // ...
   30. }
   31. }

   33. // 禁用音频返听，关闭监听事件。
   34. async function disable(updateCallback?: (msg: string, isError: boolean) => void): Promise<void> {
   35. if (audioLoopback !== undefined) {
   36. try {
   37. let status = await audioLoopback.getStatus();
   38. if (status == audio.AudioLoopbackStatus.AVAILABLE_RUNNING) {
   39. // 禁用返听。
   40. let success = await audioLoopback.enable(false);
   41. if (success) {
   42. console.info('Invoke disable succeeded');
   43. // ...
   44. // 关闭监听。
   45. audioLoopback.off('statusChange', statusChangeCallback);
   46. } else {
   47. status = await audioLoopback.getStatus();
   48. statusChangeCallback(status);
   49. }
   50. } else {
   51. statusChangeCallback(status);
   52. }
   53. } catch (err) {
   54. console.error(`Invoke disable failed, code is ${err.code}, message is ${err.message}.`);
   55. // ...
   56. }
   57. } else {
   58. console.error('Audio loopback not created.');
   59. // ...
   60. }
   61. }
   ```

### 完整示例

使用AudioLoopback启用音频低时延返听示例代码如下所示。

```
1. import { audio } from '@kit.AudioKit'; // 导入audio模块。
2. import { BusinessError } from '@kit.BasicServicesKit'; // 导入BusinessError。
3. import { common, abilityAccessCtrl, PermissionRequestResult } from '@kit.AbilityKit'; // 导入UIAbilityContext。

5. const TAG = 'AudioLoopbackDemo';
6. let mode: audio.AudioLoopbackMode = audio.AudioLoopbackMode.HARDWARE;
7. let audioLoopback: audio.AudioLoopback | undefined = undefined;
8. let currentReverbPreset: audio.AudioLoopbackReverbPreset = audio.AudioLoopbackReverbPreset.THEATER;
9. let currentEqualizerPreset: audio.AudioLoopbackEqualizerPreset = audio.AudioLoopbackEqualizerPreset.FULL;
10. // ...

12. // ...

14. // 查询能力，创建实例。
15. function init(updateCallback?: (msg: string, isError: boolean) => void): void {
16. let isSupported = audio.getAudioManager().getStreamManager().isAudioLoopbackSupported(mode);
17. if (isSupported) {
18. audio.createAudioLoopback(mode).then((loopback) => {
19. console.info('Invoke createAudioLoopback succeeded.');
20. // ...
21. audioLoopback = loopback;
22. }).catch((err: BusinessError) => {
23. console.error(`Invoke createAudioLoopback failed, code is ${err.code}, message is ${err.message}.`);
24. // ...
25. });
26. } else {
27. console.error('Audio loopback is unsupported.');
28. // ...
29. }
30. }

32. // 设置音频返听音量。
33. async function setVolume(volume: number, updateCallback?: (msg: string, isError: boolean) => void): Promise<void> {
34. if (audioLoopback !== undefined) {
35. try {
36. await audioLoopback.setVolume(volume);
37. console.info(`Invoke setVolume ${volume} succeeded.`);
38. // ...
39. } catch (err) {
40. console.error(`Invoke setVolume failed, code is ${err.code}, message is ${err.message}.`);
41. // ...
42. }
43. } else {
44. console.error('Audio loopback not created.');
45. // ...
46. }
47. }

49. // 设置音频返听的混响模式。
50. async function setReverbPreset(preset: audio.AudioLoopbackReverbPreset, updateCallback?: (msg: string,
51. isError: boolean) => void): Promise<void> {
52. if (audioLoopback !== undefined) {
53. try {
54. audioLoopback.setReverbPreset(preset);
55. console.info(`setReverbPreset( ${preset} succeeded.`);
56. // ...
57. currentReverbPreset = audioLoopback.getReverbPreset(); // 查询当前的混响模式，防止设置失败。
58. } catch (err) {
59. console.error(`setReverbPreset( failed, code is ${err.code}, message is ${err.message}.`);
60. // ...
61. }
62. } else {
63. console.error('Audio loopback not created.');
64. // ...
65. }
66. }

68. // 设置音频返听的均衡器类型。
69. async function setEqualizerPreset(preset: audio.AudioLoopbackEqualizerPreset, updateCallback?:
70. (msg: string, isError: boolean) => void): Promise<void> {
71. if (audioLoopback !== undefined) {
72. try {
73. audioLoopback.setEqualizerPreset(preset);
74. console.info(`setEqualizerPreset ${preset} succeeded.`);
75. // ...
76. currentEqualizerPreset = audioLoopback.getEqualizerPreset(); // 查询当前的均衡器类型，防止设置失败。
77. } catch (err) {
78. console.error(`setEqualizerPreset failed, code is ${err.code}, message is ${err.message}.`);
79. // ...
80. }
81. } else {
82. console.error('Audio loopback not created.');
83. // ...
84. }
85. }

87. // 设置监听事件，启用音频返听。
88. async function enable(updateCallback?: (msg: string, isError: boolean) => void): Promise<void> {
89. if (audioLoopback !== undefined) {
90. try {
91. let status = await audioLoopback.getStatus();
92. if (status == audio.AudioLoopbackStatus.AVAILABLE_IDLE) {
93. // 注册监听。
94. audioLoopback.on('statusChange', statusChangeCallback);
95. // 启动返听。
96. let success = await audioLoopback.enable(true);
97. if (success) {
98. console.info('Invoke enable succeeded');
99. // ...
100. } else {
101. status = await audioLoopback.getStatus();
102. statusChangeCallback(status);
103. }
104. } else {
105. statusChangeCallback(status);
106. }
107. } catch (err) {
108. console.error(`Invoke enable failed, code is ${err.code}, message is ${err.message}.`);
109. // ...
110. }
111. } else {
112. console.error('Audio loopback not created.');
113. // ...
114. }
115. }

117. // 禁用音频返听，关闭监听事件。
118. async function disable(updateCallback?: (msg: string, isError: boolean) => void): Promise<void> {
119. if (audioLoopback !== undefined) {
120. try {
121. let status = await audioLoopback.getStatus();
122. if (status == audio.AudioLoopbackStatus.AVAILABLE_RUNNING) {
123. // 禁用返听。
124. let success = await audioLoopback.enable(false);
125. if (success) {
126. console.info('Invoke disable succeeded');
127. // ...
128. // 关闭监听。
129. audioLoopback.off('statusChange', statusChangeCallback);
130. } else {
131. status = await audioLoopback.getStatus();
132. statusChangeCallback(status);
133. }
134. } else {
135. statusChangeCallback(status);
136. }
137. } catch (err) {
138. console.error(`Invoke disable failed, code is ${err.code}, message is ${err.message}.`);
139. // ...
140. }
141. } else {
142. console.error('Audio loopback not created.');
143. // ...
144. }
145. }
```
