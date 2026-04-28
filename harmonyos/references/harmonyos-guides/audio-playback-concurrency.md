---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-playback-concurrency
title: 音频焦点介绍
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频焦点和音频会话管理 > 音频焦点介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:de68bb24610c869f405d4d02d6f94ee7cf9a5dba11d613eb4c1a889710c9c4ab
---

在应用播放或录制声音时，常出现与其他音频流的并发或中断情况，这对用户体验构成显著影响。例如，当应用启动视频播放时，若后台正在播放音乐，用户会期望音乐能自动暂停，以确保视频音频优先播放，这正是音频焦点功能的体现。对于涉及音频服务的应用而言，妥善地管理音频焦点非常重要，它可以显著提升用户的音频体验。

本文档将介绍系统的音频焦点策略，以及应对焦点变化的方法。同时，系统提供了[音频会话管理](audio-session-management.md)机制，允许应用自定义其音频流的焦点策略。

## 音频焦点

系统预设了默认的[音频焦点策略](audio-playback-concurrency.md#音频焦点策略)，根据音频流的类型及启动的先后顺序，对所有播放和录制音频流进行统一管理。

在启动播放或录制功能前，应用需要先[申请音频焦点](audio-playback-concurrency.md#申请音频焦点)；而在播放或录制结束后，应适时[释放音频焦点](audio-playback-concurrency.md#释放音频焦点)。在播放或录制的过程中，可能会因其他音频流的介入而失去焦点，此时，应用需依据焦点变化采取相应措施[处理音频焦点变化](audio-playback-concurrency.md#处理音频焦点变化)。

对于应用而言，为了确保为用户提供优质的音频焦点体验，应当注意以下几点：

* 在启动播放或录制操作前，应根据音频的具体用途，选择并[使用合适的音频流类型](using-right-streamusage-and-sourcetype.md)，即准确设置[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)或[SourceType](../harmonyos-references/arkts-apis-audio-e.md#sourcetype8)。
* 在播放或录制的过程中，需通过监听音频焦点来[处理音频焦点变化](audio-playback-concurrency.md#处理音频焦点变化)事件，并在接收到音频焦点中断事件（[InterruptEvent](../harmonyos-references/arkts-apis-audio-i.md#interruptevent9)）时，采取相应的处理措施。
* 如果应用程序有意主动管理音频焦点，可使用[音频会话管理](audio-session-management.md)相关的接口进行操作。

### 申请音频焦点

**当应用开始播放或录制音频时，系统将自动为相应的音频流申请音频焦点。**

例如，应用[使用AudioRenderer开发音频播放功能(ArkTs)](using-audiorenderer-for-playback.md)，当调用AudioRenderer的[start](../harmonyos-references/arkts-apis-audio-audiorenderer.md#start8)时，系统会自动为应用请求音频焦点。

若音频焦点请求成功，音频流将正常启动；反之，若音频焦点请求被拒绝，音频流将无法开始播放或录制。

建议应用主动通过监听音频焦点来[处理音频焦点变化](audio-playback-concurrency.md#处理音频焦点变化)事件，一旦音频焦点请求被拒绝，应用将接收到[音频焦点事件（InterruptEvent）](../harmonyos-references/arkts-apis-audio-i.md#interruptevent9)。

如果应用希望只申请一次焦点，连续播放多条音频流不被中断，可使用[音频会话管理](audio-session-management.md)相关的接口进行操作。

**特殊场景：**

1. **短音播放**：若应用[使用SoundPool播放短音频(ArkTS)](using-soundpool-for-playback.md)，且[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)指定为Music、Movie、AudioBook等类型，播放短音，则其申请焦点时默认为并发模式，不会影响其他音频。
2. **静音播放**：若应用以静音状态开始播放音频（或视频），并且希望静音阶段不影响其他音频，当后续解除静音的时候，再以正常策略申请音频焦点，则可以调用静音并发播放模式的相关接口。具体可参考：

   * [使用AVPlayer播放音频(ArkTS)](using-avplayer-for-playback.md)，可以调用[setMediaMuted](../harmonyos-references/arkts-apis-media-avplayer.md#setmediamuted12)函数。
   * [使用AudioRenderer开发音频播放功能(ArkTs)](using-audiorenderer-for-playback.md)，可调用[setSilentModeAndMixWithOthers](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setsilentmodeandmixwithothers12)函数。
   * [使用OHAudio开发音频播放功能(C/C++)](using-ohaudio-for-playback.md)，可调用[OH\_AudioRenderer\_SetSilentModeAndMixWithOthers](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_setsilentmodeandmixwithothers)函数。

### 释放音频焦点

**当应用结束播放或录制音频时，系统会自动为相应的音频流释放音频焦点。**

例如，应用[使用AudioRenderer开发音频播放功能(ArkTs)](using-audiorenderer-for-playback.md)，当调用AudioRenderer的[pause](../harmonyos-references/arkts-apis-audio-audiorenderer.md#pause8)、[stop](../harmonyos-references/arkts-apis-audio-audiorenderer.md#stop8)、[release](../harmonyos-references/arkts-apis-audio-audiorenderer.md#release8)等时，系统会为其释放音频焦点。

当音频流释放音频焦点时，若存在受其影响的其他音频流（如音量被调低或被暂停的流），将触发恢复操作。

如果应用不希望在音频流停止时立即释放音频焦点，可使用[音频会话管理](audio-session-management.md)的相关接口，实现音频焦点释放的延迟效果。

如果应用通过激活[音频会话管理](audio-session-management.md)申请过焦点，需要结束AudioSession以释放焦点。

### 音频焦点策略

当音频流申请或释放音频焦点时，系统依据音频焦点策略，对所有音频流（包括播放和录制）实施焦点管理，决定哪些音频流可正常运行，哪些需被打断或执行其他操作。

系统预设的默认音频焦点策略，主要依据音频流类型（即播放流的[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)和录制流的[SourceType](../harmonyos-references/arkts-apis-audio-e.md#sourcetype8)）及音频流启动的顺序进行决策。

为防止焦点变化不符合预期，应用在启动播放或录制前，应根据音频流的用途，准确设置StreamUsage或SourceType。关于各类型的详细说明，请参考[使用合适的音频流类型](using-right-streamusage-and-sourcetype.md)。

常见的音频焦点场景示例如下：

* 开始播放Movie音频流时，将导致正在播放的Music音频流暂停，但Movie播放停止后，Music不会收到恢复播放的通知。
* 开始Navigation音频流时，会自动降低正在播放的Music音频流音量，Navigation停止后，Music音量将恢复至原样。
* Music音频流与Game音频流可并发混音播放，相互之间不会影响音量或播放状态。
* VoiceCommunication开始播放时，将暂停正在播放的Music音频流，VoiceCommunication停止后，Music将收到恢复播放的通知。
* 开始录制VoiceMessage时，Music音频流会被暂停，VoiceMessage录制停止后，Music将收到恢复播放的通知。

若默认的音频焦点策略无法满足特定场景的需求，应用程序可利用[音频会话管理](audio-session-management.md)，调整本应用音频流所采用的音频焦点策略。

### 焦点模式

针对同一应用创建的多个音频流，应用可通过设置[焦点模式（InterruptMode）](../harmonyos-references/arkts-apis-audio-e.md#interruptmode9)，选择由应用自主管控，或由系统统一管理。

系统预设了两种焦点模式：

* 共享焦点模式（SHARE\_MODE）：同一应用创建的多个音频流共享一个音频焦点。这些音频流之间的并发规则由应用自行决定，音频焦点策略不会介入。仅当其他应用创建的音频流与该应用的音频流同时播放时，才会触发音频焦点策略的管理。
* 独立焦点模式（INDEPENDENT\_MODE）：应用创建的每个音频流均独立拥有一个音频焦点，多个音频流同时播放时，将触发音频焦点策略的管理。

应用可根据需求选择合适的焦点模式。在创建音频流时，系统默认采用共享焦点模式（SHARE\_MODE），应用可主动设置所需模式。

设置焦点模式的方法：

* 若[使用AVPlayer播放音频(ArkTS)](using-avplayer-for-playback.md)，则可以通过修改AVPlayer的[audioInterruptMode](../harmonyos-references/arkts-apis-media-avplayer.md#属性)属性进行设置。
* 若[使用AVPlayer播放音频(C/C++)](using-ndk-avplayer-for-playback.md)，则可以调用[OH\_AVPlayer\_SetAudioInterruptMode](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setaudiointerruptmode)函数进行设置。
* 若[使用AudioRenderer开发音频播放功能(ArkTs)](using-audiorenderer-for-playback.md)，则可以调用[setInterruptMode](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setinterruptmode9)函数进行设置。
* 若[使用OHAudio开发音频播放功能(C/C++)](using-ohaudio-for-playback.md)，则可以调用[OH\_AudioStreamBuilder\_SetRendererInterruptMode](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererinterruptmode)函数进行设置。

### 处理音频焦点变化

在应用播放或录制音频的过程中，若有其他音频流申请焦点，系统会根据[音频焦点策略](audio-playback-concurrency.md#音频焦点策略)进行焦点处理。若判定本音频流的焦点有变化，需要执行暂停、继续、降低音量、恢复音量等操作，则系统会自动执行一些必要的操作，并通过[音频焦点事件（InterruptEvent）](../harmonyos-references/arkts-apis-audio-i.md#interruptevent9)通知应用。

因此，为了维持应用和系统的状态一致性，保证良好的用户体验，推荐应用监听音频焦点事件，并在焦点发生变化时，根据[InterruptEvent](../harmonyos-references/arkts-apis-audio-i.md#interruptevent9)做出必要的响应。

**使用不同方式开发时，如何监听音频焦点事件：**

* 若[使用AVPlayer播放音频(ArkTS)](using-avplayer-for-playback.md)，可以调用[on('audioInterrupt')](../harmonyos-references/arkts-apis-media-avplayer.md#onaudiointerrupt9)接口，监听音频焦点事件[InterruptEvent](../harmonyos-references/arkts-apis-audio-i.md#interruptevent9)。
* 若[使用AVPlayer播放音频(C/C++)](using-ndk-avplayer-for-playback.md)，可以调用[OH\_AVPlayer\_SetOnInfoCallback()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setoninfocallback)接口，监听音频焦点事件[OH\_AVPlayerOnInfoCallback](../harmonyos-references/capi-avplayer-base-h.md#oh_avplayeroninfocallback)。
* 若[使用AudioRenderer开发音频播放功能(ArkTs)](using-audiorenderer-for-playback.md)，可以调用[on('audioInterrupt')](../harmonyos-references/arkts-apis-audio-audiorenderer.md#onaudiointerrupt9)接口，监听音频焦点事件[InterruptEvent](../harmonyos-references/arkts-apis-audio-i.md#interruptevent9)。
* 若[使用OHAudio开发音频播放功能(C/C++)](using-ohaudio-for-playback.md)，可以调用[OH\_AudioStreamBuilder\_SetRendererCallback](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrenderercallback)接口，监听音频焦点事件[OH\_AudioRenderer\_OnInterruptEvent](../harmonyos-references/capi-ohaudio-oh-audiorenderer-callbacks-struct.md#oh_audiorenderer_oninterruptevent)。
* 若[使用AudioCapturer开发音频录制功能(ArkTs)](using-audiocapturer-for-recording.md)，可以调用[on('audioInterrupt')](../harmonyos-references/arkts-apis-audio-audiocapturer.md#onaudiointerrupt10)接口，监听音频焦点事件[InterruptEvent](../harmonyos-references/arkts-apis-audio-i.md#interruptevent9)。
* 若[使用OHAudio开发音频录制功能(C/C++)](using-ohaudio-for-recording.md)，可以调用[OH\_AudioStreamBuilder\_SetCapturerCallback](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturercallback)接口，监听音频焦点事件[OH\_AudioCapturer\_OnInterruptEvent](../harmonyos-references/capi-ohaudio-oh-audiocapturer-callbacks-struct.md#oh_audiocapturer_oninterruptevent)。

应用在收到音频焦点事件（[InterruptEvent](../harmonyos-references/arkts-apis-audio-i.md#interruptevent9)）时，需要根据其中信息，做出相应的处理，以保持应用与系统状态一致，带给用户良好的音频体验。

在音频焦点事件中，应用应重点关注两个信息：打断类型（InterruptForceType）和打断提示（InterruptHint）。

* 打断类型（[InterruptForceType](../harmonyos-references/arkts-apis-audio-e.md#interruptforcetype9)）：

  InterruptForceType参数提示应用该焦点变化是否已由系统强制操作：

  + 强制打断类型（INTERRUPT\_FORCE）：由系统进行操作，强制执行。应用收到打断提示后无需再调用系统相关接口，只需做一些必要的处理，例如更新状态、更新界面显示等。
  + 共享打断类型（INTERRUPT\_SHARE）：由应用进行操作，应用可以选择响应或忽略，系统不会干涉。

  系统默认优先采用强制打断类型（INTERRUPT\_FORCE），应用无法更改。

  注意

  对于一些系统无法强制执行的操作（例如INTERRUPT\_HINT\_RESUME），会采用共享打断类型（INTERRUPT\_SHARE）。
* 打断提示（[InterruptHint](../harmonyos-references/arkts-apis-audio-e.md#interrupthint)）：

  InterruptHint参数用于提示应用音频流的状态：

  + 继续（INTERRUPT\_HINT\_RESUME）：音频流可恢复播放或录制，仅会接收到PAUSE（暂停提示）之后收到。

    此操作无法由系统强制执行，其对应的InterruptForceType一定为INTERRUPT\_SHARE类型。
  + 暂停（INTERRUPT\_HINT\_PAUSE）：音频暂停，暂时失去音频焦点。后续待焦点可用时，会再收到INTERRUPT\_HINT\_RESUME。
  + 停止（INTERRUPT\_HINT\_STOP）：音频停止，彻底失去音频焦点。
  + 降低音量（INTERRUPT\_HINT\_DUCK）：音频降低音量播放，而不会停止。默认降低至正常音量的20%。
  + 恢复音量（INTERRUPT\_HINT\_UNDUCK）：音频恢复正常音量。

### 典型场景

典型焦点的适配场景如下表所示。

| 先播放的音频类型 | 推荐流类型 | 后播放的音频类型 | 推荐流类型 | 推荐体验 | 适配方案 |
| --- | --- | --- | --- | --- | --- |
| 音乐 | STREAM\_USAGE\_MUSIC | 音乐 | STREAM\_USAGE\_MUSIC | 后播音乐正常播放，先播音乐停止播放，UI变成停止播放状态。 | 先播音乐应用注册焦点事件监听，接收到INTERRUPT\_HINT\_STOP事件时，停止音乐播放，并更新UI界面。 |
| 音乐 | STREAM\_USAGE\_MUSIC | 导航 | STREAM\_USAGE\_NAVIGATION | 导航正常播放，音乐降低音量播放。  导航结束后，音乐恢复正常音量。 | 音乐应用注册焦点事件监听，接收到INTERRUPT\_HINT\_DUCK和INTERRUPT\_HINT\_UNDUCK事件时，可以选择更新UI界面。 |
| 视频 | STREAM\_USAGE\_MOVIE | 闹铃 | STREAM\_USAGE\_ALARM | 闹铃响起后，视频暂停播放。  闹钟结束后，视频继续播放。 | 视频应用注册焦点事件监听。接收到INTERRUPT\_HINT\_PAUSE事件时，直接暂停视频播放，并更新UI界面。  当闹铃结束后，视频应用接收到INTERRUPT\_HINT\_RESUME事件，重新启动播放。 |
| 音乐 | STREAM\_USAGE\_MUSIC | 来电铃声 | STREAM\_USAGE\_RINGTONE | 开始响铃，音乐暂停播放。  不接通或者接通再挂断后，音乐恢复播放。 | 音乐应用注册焦点事件监听。接收到INTERRUPT\_HINT\_PAUSE事件时，直接暂停音乐播放，并更新UI界面。  当电话结束后，音频应用接收到INTERRUPT\_HINT\_RESUME事件，重新启动播放。 |
| 音乐 | STREAM\_USAGE\_MUSIC | VoIP通话 | STREAM\_USAGE\_VOICE\_COMMUNICATION | 通话接通时，音乐暂停播放。  通话挂断后，音乐恢复播放。 | 音乐应用注册焦点事件监听。  接收到INTERRUPT\_HINT\_PAUSE事件时，直接暂停音乐播放，并更新UI界面。  当通话结束后，音乐应用接收到INTERRUPT\_HINT\_RESUME事件，重新启动播放。 |

**处理音频焦点示例:**

为了带给用户更好的音频体验，针对不同的音频焦点事件内容，应用需要做出相应的处理操作。此处以[使用AudioRenderer开发音频播放功能(ArkTs)](using-audiorenderer-for-playback.md)为例，展示推荐应用采取的处理方法，提供伪代码供开发者参考。

在监听音频播放焦点变化事件之前，需要先获取[AudioRenderer](../harmonyos-references/arkts-apis-audio-f.md#audiocreateaudiorenderer8)实例。若使用其他接口开发音频播放或音频录制功能，处理方法类似，具体的代码实现，开发者可结合实际情况编写，处理方法也可自行调整。

```
1. import { audio } from '@kit.AudioKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. // ...

5. let isPlay: boolean; // 是否正在播放，实际开发中，对应与音频播放状态相关的模块。
6. let isDucked: boolean; // 是否降低音量，实际开发中，对应与音频音量相关的模块。
7. let started: boolean; // 标识符，记录“开始播放（start）”操作是否成功。

9. async function onAudioInterrupt(): Promise<void> {
10. if (audioRenderer == undefined) {
11. return;
12. }
13. // 此处以使用AudioRenderer开发音频播放功能举例，变量audioRenderer即为播放时创建的AudioRenderer实例。
14. audioRenderer.on('audioInterrupt', async(interruptEvent: audio.InterruptEvent) => {
15. // ...
16. // 在发生音频焦点变化时，audioRenderer收到interruptEvent回调，此处根据其内容做相应处理。
17. // 1. 可选：读取interruptEvent.forceType的类型，判断系统是否已强制执行相应操作。
18. // 注：默认焦点策略下，INTERRUPT_HINT_RESUME为INTERRUPT_SHARE类型，其余hintType均为INTERRUPT_FORCE类型。因此对forceType可不做判断。
19. // 2. 必选：读取interruptEvent.hintType的类型，做出相应的处理。
20. if (interruptEvent.forceType === audio.InterruptForceType.INTERRUPT_FORCE) {
21. // 强制打断类型（INTERRUPT_FORCE）：音频相关处理已由系统执行，应用需更新自身状态，做相应调整。
22. switch (interruptEvent.hintType) {
23. case audio.InterruptHint.INTERRUPT_HINT_PAUSE:
24. // 此分支表示系统已将音频流暂停（临时失去焦点），为保持状态一致，应用需切换至音频暂停状态。
25. // 临时失去焦点：待其他音频流释放音频焦点后，本音频流会收到resume对应的音频焦点事件，到时可自行继续播放。
26. isPlay = false; // 此句为简化处理，代表应用切换至音频暂停状态的若干操作。
27. break;
28. case audio.InterruptHint.INTERRUPT_HINT_STOP:
29. // 此分支表示系统已将音频流停止（永久失去焦点），为保持状态一致，应用需切换至音频暂停状态。
30. // 永久失去焦点：后续不会再收到任何音频焦点事件，若想恢复播放，需要用户主动触发。
31. isPlay = false; // 此句为简化处理，代表应用切换至音频暂停状态的若干操作。
32. break;
33. case audio.InterruptHint.INTERRUPT_HINT_DUCK:
34. // 此分支表示系统已将音频音量降低（默认降到正常音量的20%）。
35. isDucked = true; // 此句为简化处理，代表应用切换至降低音量播放状态的若干操作。
36. break;
37. case audio.InterruptHint.INTERRUPT_HINT_UNDUCK:
38. // 此分支表示系统已将音频音量恢复正常。
39. isDucked = false; // 此句为简化处理，代表应用切换至正常音量播放状态的若干操作。
40. break;
41. default:
42. break;
43. }
44. } else if (interruptEvent.forceType === audio.InterruptForceType.INTERRUPT_SHARE) {
45. // 共享打断类型（INTERRUPT_SHARE）：应用可自主选择执行相关操作或忽略音频焦点事件。
46. switch (interruptEvent.hintType) {
47. case audio.InterruptHint.INTERRUPT_HINT_RESUME:
48. // 此分支表示临时失去焦点后被暂停的音频流此时可以继续播放，建议应用继续播放，切换至音频播放状态。
49. // 若应用此时不想继续播放，可以忽略此音频焦点事件，不进行处理即可。
50. // 继续播放，此处主动执行start()，以标识符变量started记录start()的执行结果。
51. if (audioRenderer == undefined) {
52. return;
53. }
54. await audioRenderer.start().then(() => {
55. started = true; // start()执行成功。
56. }).catch((err: BusinessError) => {
57. started = false; // start()执行失败。
58. });
59. // 若start()执行成功，则切换至音频播放状态。
60. if (started) {
61. isPlay = true; // 此句为简化处理，代表应用切换至音频播放状态的若干操作。
62. } else {
63. // 音频继续播放的操作执行失败。
64. }
65. break;
66. default:
67. break;
68. }
69. }
70. });
71. }
```
