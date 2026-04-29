---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-audio-video-synchronization
title: 音画同步
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 音画同步
category: best-practices
scraped_at: 2026-04-29T14:11:38+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:4b50a30763c81888afa3a4d7daa27845627f1672804d54930bb7dcaf3427538b
---

## 概述

精确的音视频同步是媒体播放的关键体验之一。通常来说，在录制音频和视频时需要做到同步，并且录制后的视频在播放设备（例如手机、电视、媒体播放器）上播放时也需要做到同步。目前，视频在播放时可能会出现音视频不同步现象，严重影响用户体验。

根据当前HarmonyOS APP开发过程中遇到的音画同步业务场景，总结出如下三种典型场景：

* [本地视频的音画同步](bpta-audio-video-synchronization.md#section340411415017)
* [网络视频的音画同步](bpta-audio-video-synchronization.md#section18863195213010)
* [录制视频的音画同步](bpta-audio-video-synchronization.md#section125452116310)

从上述三种典型场景出发，本文旨在指导第三方视频播放应用正确获取并使用音频和视频相关信息来保证播放时的音视频同步。

说明

如果开发者使用自研播放器引擎而非AVPlayer，也可以参考该解决方案思路实现优化。

## 实现原理

音视频数据的最小处理单元称为帧。音频流和视频流都被分割成帧，所有帧都被标记为需要按特定的时间戳显示。音频和视频可以独立下载和解码，具有匹配时间戳的音频和视频帧应同时呈现，以达到音画同步的效果。

### 音画同步标准

* PTS（送显时间戳）指音视频数据在播放时应该显示给用户的时间戳。它表示解码后的音视频数据在播放时应该出现在屏幕上或传递给音视频输出设备的时间点。PTS用于控制音视频的播放顺序和时序，以确保音视频在正确的时间点进行显示或播放。
* DTS（解码时间戳）指音视频数据在解码器中开始解码的时间戳。它表示解码器应该从输入数据流中读取和解码的特定时间点。DTS用于控制解码器的解码顺序，确保音视频数据按照正确的顺序解码。

| 帧 | 解释 |
| --- | --- |
| I帧(I-frame) | 内部画面（intra picture）或关键帧（key frame）。I帧是一个全帧压缩的编码帧，包含了一幅完整的图像数据。 |
| P帧(P-frame) | 前向预测编码帧（predictive-frame）。P帧不是完整的数据帧，而是只包含与前面I帧或P帧的差异数据。 |
| B帧(B-frame) | 双向预测内插编码帧（bi-directional interpolated prediction frame）。B帧也是一个压缩帧，它同时参考前面的I帧或P帧和后面的P帧来进行编码。 |

1. 为了衡量音画同步的性能，用对应视频帧和音频帧实际播放时间的差值作为数值指标，数值大于0ms表示声音提前画面，小于0ms表示声音落后画面。
2. 最大卡顿时长：单帧图像停滞时间超过100ms的，定义为卡顿一次，连续测试5分钟。
3. 平均播放帧率：平均每秒播放帧数，不反映每帧显示时长。

| 时间差范围 | 主观体验 |
| --- | --- |
| [-80ms, 25ms] | 无法察觉 |
| [-125ms, -80ms], [25ms, 45ms] | 能够察觉 |
| [-185ms, -125ms], [45ms, 90ms] | 无法接受 |

### 音画同步方案思路

理论上，因为音频通路存在时延，要保证播放时的音视频同步，有三种解决方案可用：

* 连续播放音频帧：使用音频播放位置作为主时间参考，并将视频播放位置与其匹配。
* 使用系统时间作为参考：将音频和视频播放与系统时间匹配。
* 使用视频播放作为参考：使用视频播放位置作为主时间参考，并将音频播放位置与其匹配。

三种方案的优缺点对比如下：

| 方案名称 | 优点 | 缺点 |
| --- | --- | --- |
| 连续播放音频帧 | 1. 用户肉眼的敏感度较弱，不易察觉视频微小的调整。 2. 视频刷新时间的调整相对便捷。 | 如果视频帧率不稳定或渲染延迟大，可能导致视频卡顿或跳帧。 |
| 使用系统时间作为参考 | 可以最大限度的保证音频和视频都不发生跳帧行为。 | 1. 需要额外依赖系统时钟，增加了系统复杂性和维护成本。 2. 系统时钟的准确性对同步效果影响较大，如果系统时钟不准确，可能导致同步效果大打折扣。 |
| 使用视频播放作为参考 | 音频可根据视频帧进行调整，减少音频跳帧的情况。 | 1. 音频播放可能会出现等待或加速的情况，相较于视频会对用户的影响更为严重和明显。 2. 如果视频帧率不稳定，可能导致音频同步困难。 |

第一个方案是具有连续音频数据流的选项，其没有对音频帧的显示时间、播放速度或持续时间进行任何调整。这些参数的任何调整都很容易被人耳注意到，并导致音频干扰故障。处理这些故障需要对音频重新采样，然而重新采样会导致音调的改变。

因此，一般的多媒体应用多使用音频播放位置作为主时间参考。以下章节主要以此解决方案进行说明（其他两个选项不在本文档的范围内）。

### 连续播放音频帧方案

该方案使用音频播放位置作为主时间参考，并将视频播放位置与其匹配，使音画同步指标达到用户无法察觉的[-80ms, 25ms]范围。

解决方案使用：

* 视频同步到音频（主流方案）。
* 获取音频渲染进度，动态调整视频渲染进度。

最终实现音画同步[-80ms, 25ms]的效果。

**连续播放音帧方案示意图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/36ssXTWdQVuM1ZG_rQIHwA/zh-cn_image_0000002519989771.png?HW-CC-KV=V1&HW-CC-Date=20260429T061134Z&HW-CC-Expire=86400&HW-CC-Sign=B25EA40DC0AA43F6E32E8341C18778998BAB90E1A5E93CE4481DD6BD9931A434 "点击放大")

音频和视频的管道必须同时以相同的时间戳呈现每帧数据。将音频播放位置用作主时间参考，而视频管道只输出与最新渲染音频帧匹配的视频帧。对于所有可能的实现，精确计算最后一次呈现的音频时间戳是至关重要的。[OH\_AudioRenderer\_GetTimestamp()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_gettimestamp) 接口用以查询音频管道各个阶段的音频时间戳和延迟信息，此信息可用于控制视频管道，使视频帧与音频帧匹配。

基于以上示意图，具体来说，在监听到视频帧的时候，首先去获取当前音频渲染位置，在获取成功的情况下计算该视频帧PTS与当前音频渲染位置的延迟时间，对延迟时间进行如下判断确定送显策略。

* **视频帧相较于音频渲染位置过早时，视频帧则等待一段时间再送显**。
* **延迟时间在可接受的延迟范围内该视频帧立即送显**。
* **当视频帧相较于音频渲染位置过晚时则丢弃该视频帧**。

## 本地视频的音画同步

从本地媒体库中选择视频资源进行播放是三方视频类应用常见的场景。

### 实现原理

系统中提供了[PhotoViewPicker()](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md)接口用于获取本地视频资源。三方视频播放应用可以使用[OH\_AVSource\_CreateWithFD()](../harmonyos-references/capi-native-avsource-h.md#oh_avsource_createwithfd)接口对本地视频资源进行解封装，获取和使用对应的音频和视频信息后，使用连续播放音频帧方案进行音频和视频的播放同步。具体开发步骤如下所示。

1. 使用[PhotoViewPicker()](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md)获取本地视频资源。
2. 使用[OH\_AVSource\_CreateWithFD()](../harmonyos-references/capi-native-avsource-h.md#oh_avsource_createwithfd)对本地视频资源进行解封装处理，获取音频和视频信息。
3. 使用[连续播放音频帧方案](bpta-audio-video-synchronization.md#section3976172773620)进行音画同步播放。

### 开发步骤

1. 使用[PhotoViewPicker()](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md)获取本地视频资源。

```
1. static async selectFileFromLocal(): Promise<string | undefined> {
2. try {
3. let result = await FileUtil.getPhotoViewPicker().select({
4. MIMEType: photoAccessHelper.PhotoViewMIMETypes.VIDEO_TYPE,
5. maxSelectNumber: 1
6. })
7. let selectFilePath = result.photoUris[0];
8. if (!selectFilePath) {
9. return undefined
10. }
11. return selectFilePath;
12. } catch (e) {
13. return undefined;
14. }
15. }
```

[FileUtil.ets](https://gitcode.com/harmonyos_samples/AudioToVideoSync/blob/master/entry/src/main/ets/common/utils/FileUtil.ets#L39-L53)

2. 使用[OH\_AVSource\_CreateWithFD()](../harmonyos-references/capi-native-avsource-h.md#oh_avsource_createwithfd)对本地视频资源进行解封装处理，获取音频帧和视频帧信息。

```
1. int32_t Demuxer::Create(SampleInfo &info) {
2. if (info.isLocal) {
3. // From the local video scenario
4. source = OH_AVSource_CreateWithFD(info.inputFd, info.inputFileOffset, info.inputFileSize);
5. } else {
6. // From the local video scenario
7. source = OH_AVSource_CreateWithURI(info.networkUri);
8. }

10. CHECK_AND_RETURN_RET_LOG(source != nullptr, AVCODEC_SAMPLE_ERR_ERROR,
11. "Create demuxer source failed, fd: %{public}d, offset: %{public}" PRId64
12. ", file size: %{public}" PRId64,
13. info.inputFd, info.inputFileOffset, info.inputFileSize);
14. demuxer = OH_AVDemuxer_CreateWithSource(source);
15. // ...
16. }
```

[Demuxer.cpp](https://gitcode.com/harmonyos_samples/AudioToVideoSync/blob/master/entry/src/main/cpp/capbilities/Demuxer.cpp#L25-L50)

3. 收到视频帧的时候，通过调用[OH\_AudioRenderer\_GetTimestamp()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_gettimestamp)接口获取音频渲染位置等信息。

```
1. // get audio render position
2. int64_t framePosition = 0;
3. int64_t timeStamp = 0;
4. int32_t ret = OH_AudioRenderer_GetTimestamp(audioRenderer, CLOCK_MONOTONIC, &framePosition, &timeStamp);

6. audioTimeStamp = timeStamp;
```

[Player.cpp](https://gitcode.com/harmonyos_samples/AudioToVideoSync/blob/master/entry/src/main/cpp/player/Player.cpp#L295-L300)

4. 音频启动前，音频播放时间timestamp和音频播放位置framePosition返回结果为0。为避免出现卡顿等问题，暂不同步，视频帧直接送显。

```
1. // audio render getTimeStamp error, render it
2. if (ret != AUDIOSTREAM_SUCCESS || (timeStamp == 0) || (framePosition == 0)) {
3. // first frame, render without wait
4. videoDecoder->FreeOutputBuffer(bufferInfo.bufferIndex, true);
5. std::this_thread::sleep_until(lastPushTime + std::chrono::microseconds(sampleInfo.frameInterval));
6. lastPushTime = std::chrono::system_clock::now();
7. continue;
8. }
```

[Player.cpp](https://gitcode.com/harmonyos_samples/AudioToVideoSync/blob/master/entry/src/main/cpp/player/Player.cpp#L303-L310)

5. 根据视频帧PTS和音频渲染位置计算延迟。

* audioPlayedTime: 音频帧期望渲染时间。
* videoPlayedTime: 视频帧期望送显时间。
* waitTimeUs : 视频帧相对于音频帧延迟时间。

```
1. // after seek, audio render flush, framePosition = 0, then writtenSampleCnt = 0
2. int64_t latency =
3. (audioDecContext->frameWrittenForSpeed - framePosition) * 1000 * 1000 / sampleInfo.audioSampleRate / speed;
4. AVCODEC_SAMPLE_LOGI("VD latency: %{public}ld writtenSampleCnt: %{public}ld", latency, writtenSampleCnt);

6. nowTimeStamp = GetCurrentTime();
7. int64_t anchorDiff = (nowTimeStamp - audioTimeStamp) / 1000;
8. // us, audio buffer accelerate render time
9. int64_t audioPlayedTime = audioDecContext->currentPosAudioBufferPts - latency + anchorDiff;
10. // us, video buffer expected render time
11. int64_t videoPlayedTime = bufferInfo.attr.pts;

13. // audio render timeStamp and now timeStamp diff
14. int64_t waitTimeUs = videoPlayedTime - audioPlayedTime;
```

[Player.cpp](https://gitcode.com/harmonyos_samples/AudioToVideoSync/blob/master/entry/src/main/cpp/player/Player.cpp#L313-L326)

6. 根据业务延迟做音画同步策略。

* [40ms, ) 视频帧较晚时，丢弃此帧。
* [0ms, 40ms) 视频帧直接送显。
* (, 0ms) 视频帧较早，根据业务需要选择渐进同步。

```
1. // video buffer is too late, drop it
2. if (waitTimeUs < WAIT_TIME_US_THRESHOLD_WARNING) {
3. dropFrame = true;
4. AVCODEC_SAMPLE_LOGE("VD buffer is too late");
5. } else {
6. AVCODEC_SAMPLE_LOGE("VD buffer is too early waitTimeUs: %{public}ld", waitTimeUs);
7. // [0, ), render it with waitTimeUs, max 1s
8. // [-40,0), render it
9. if (waitTimeUs > WAIT_TIME_US_THRESHOLD) {
10. waitTimeUs = WAIT_TIME_US_THRESHOLD;
11. }
12. // per frame render time reduced by 33ms
13. if (waitTimeUs > sampleInfo.frameInterval + PER_SINK_TIME_THRESHOLD) {
14. waitTimeUs = sampleInfo.frameInterval + PER_SINK_TIME_THRESHOLD;
15. AVCODEC_SAMPLE_LOGE("VD buffer is too early and reduced 33ms, waitTimeUs: %{public}ld", waitTimeUs);
16. }
17. }
```

[Player.cpp](https://gitcode.com/harmonyos_samples/AudioToVideoSync/blob/master/entry/src/main/cpp/player/Player.cpp#L335-L351)

7. 进行音画渐进同步。视频帧较早时，等待一段时间送显。

```
1. if (waitTimeUs > 0) {
2. std::this_thread::sleep_for(std::chrono::microseconds(waitTimeUs));
3. }
4. lastPushTime = std::chrono::system_clock::now();
5. ret = videoDecoder->FreeOutputBuffer(bufferInfo.bufferIndex, !dropFrame);
```

[Player.cpp](https://gitcode.com/harmonyos_samples/AudioToVideoSync/blob/master/entry/src/main/cpp/player/Player.cpp#L354-L358)

说明

* [OH\_AudioRenderer\_Start()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_start)接口执行后到真正写入硬件有一定延迟，因此该接口在调用[OH\_AudioRenderer\_Start()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_start)接口之后，过一会才会拿到有效值，期间音频未发声时建议画面帧先按照正常速度播放，后续再逐步追赶音频位置从而提升用户看到画面的起播时延。
* 当framePosition和timestamp以稳定的速度前进后，建议调用[OH\_AudioRenderer\_GetTimestamp()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_gettimestamp)接口不要太频繁。推荐200ms一次，可以每分钟一次，最好不要低于200ms一次。频繁调用可能会带来功耗问题，因此在能保证音画同步效果的情况下，不需要频繁的查询时间戳。
* [OH\_AudioRenderer\_Flush()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_flush)接口执行后，framePosition返回值会重新（从0）开始计算。
* [OH\_AudioRenderer\_GetFramesWritten()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_getframeswritten) 接口在Flush时候不会清空，该接口和[OH\_AudioRenderer\_GetTimestamp()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_gettimestamp)接口不建议配合使用。
* 音频设备切换过程中[OH\_AudioRenderer\_GetTimestamp()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_gettimestamp)接口返回的framePosition和timestamp保证不会倒退，但由于新设备写入有时延，会出现音频进度短暂停滞，建议画面帧保持流畅播放不要产生卡顿。
* [OH\_AudioRenderer\_GetTimestamp()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_gettimestamp)接口获取的是实际写到硬件的采样帧数，不受倍速影响。对AudioRenderer设置了倍速的场景下，播放进度计算需要特殊处理，系统保证应用设置完倍速接口后，新写入AudioRenderer的采样点才会做倍速处理。

## 网络视频的音画同步

除了播放本地视频外，三方视频应用还有播放网络视频的场景。

### 实现原理

系统提供了[OH\_AVSource\_CreateWithURI()](../harmonyos-references/capi-native-avsource-h.md#oh_avsource_createwithuri)接口，可以对网络视频资源直接进行解封装并获取对应的音频和视频信息，然后使用连续播放音频帧方案进行音频和视频的播放同步。具体开发步骤如下所示。

说明

使用[OH\_AVSource\_CreateWithURI()](../harmonyos-references/capi-native-avsource-h.md#oh_avsource_createwithuri)接口需要先配置网络权限ohos.permission.INTERNET。

1. 使用[OH\_AVSource\_CreateWithURI()](../harmonyos-references/capi-native-avsource-h.md#oh_avsource_createwithuri)接口对网络资源进行解封装处理，获取音频和视频信息。
2. 使用[连续播放音频帧方案](bpta-audio-video-synchronization.md#section3976172773620)进行音画同步播放。

### 开发步骤

1. 使用[OH\_AVSource\_CreateWithURI()](../harmonyos-references/capi-native-avsource-h.md#oh_avsource_createwithuri)接口对网络资源进行解封装处理，获取音频和视频信息。

```
1. int32_t Demuxer::Create(SampleInfo &info) {
2. if (info.isLocal) {
3. // From the local video scenario
4. source = OH_AVSource_CreateWithFD(info.inputFd, info.inputFileOffset, info.inputFileSize);
5. } else {
6. // From the local video scenario
7. source = OH_AVSource_CreateWithURI(info.networkUri);
8. }

10. CHECK_AND_RETURN_RET_LOG(source != nullptr, AVCODEC_SAMPLE_ERR_ERROR,
11. "Create demuxer source failed, fd: %{public}d, offset: %{public}" PRId64
12. ", file size: %{public}" PRId64,
13. info.inputFd, info.inputFileOffset, info.inputFileSize);
14. demuxer = OH_AVDemuxer_CreateWithSource(source);
15. // ...
16. }
```

[Demuxer.cpp](https://gitcode.com/harmonyos_samples/AudioToVideoSync/blob/master/entry/src/main/cpp/capbilities/Demuxer.cpp#L25-L50)

2. 解封资源得到音频帧和视频帧后，参考本章[本地视频的音画同步](bpta-audio-video-synchronization.md#section340411415017)的[开发步骤](bpta-audio-video-synchronization.md#section640118113514)中第3~7步进行音画同步播放。

## 录制视频的音画同步

有些三方视频应用还有录制的功能，在开发录制功能时，也需要保证录制的视频音画同步。

当前可以使用如下两种方式实现视频录制。

* **使用Camera+AVRecorder录制**：AVRecorder集成了音频捕获，音频编码，视频编码，音视频封装功能，主要适用于实现简单视频录制并直接得到本地媒体文件的场景。
* **使用Camera+AVCodec录制**：AVCodec是系统提供的底层能力接口，需要应用自己实现音视频的编码和封装功能，主要适用于对视频录制自定义程度较高的场景。

当然在录制的过程中也需要保证录制的音频和视频音画同步，以保证录制后的视频在播放过程中即使不做处理也能做到音画同步。

录制视频是将音频帧和视频帧按照时间戳（PTS）分别写入音频轨和视频轨后封装成视频文件的过程。时间戳就类似于音频轨和视频轨上的“坐标”，播放的进度到此时间戳（PTS）时，就会播放此“坐标”对应的音频帧和视频帧。所以如何给音频轨和视频轨写入时间戳（PTS）是保证录制视频音画同步的关键一步。

Camera+AVRecorder录制方案中，给音轨和视频轨的时间戳的功能由高度封装的AVRecorder接口实现，不涉及开发者自己将时间戳写入音轨和视频轨并进行同步操作的关键步骤，所以这个场景不多赘述，需要了解可以参考[基于AVRecorder录制HDR Vivid视频](bpta-hdrvivid.md#section1957156132414)。

接下来主要介绍在Camera+AVCodec录制的方案中，如何给音轨和视频轨添加时间戳并实现音画同步播放。

### 实现原理

添加时间戳（PTS）前，需要先确定时间基准，一般是以系统单调时钟为时间基准，且统一时间单位为微秒（μs）。

* **系统单调时钟**：该时钟从系统启动时开始计时，单调递增，不受系统时间修改、时区切换的影响。例如，音频启动录音时，第1秒时间戳为1000000μs，第2秒为2000000μs，以此类推。

确定时间基准后，下一步需要知道如何获取视频帧和音频帧的时间戳。

* **视频帧**：视频帧是由相机采集，采集频率由设定的帧率决定，如30fps，就代表相机每隔固定时间33.3ms 捕获一帧图像。这些原始帧的时间戳是单调递增的、间隔均匀的，但是受相机传感器、编码算力等因素影响，可能会出现帧间抖动，如30fps理论间隔时间是33.3ms，实际可能波动到30-38ms，甚至偶尔丢帧。
* **音频帧**：音频采集/编码逻辑简单、对硬件的需求低，所以在时间间隔稳定性和抗干扰能力上要比视频帧稳定。

  因为音频帧比较稳定，所以可以将每一音频帧采集时的时间戳（此时间戳基于系统单调时钟）作为坐标写入音轨。通过接口[OH\_AVBuffer\_GetBufferAttr()](../harmonyos-references/capi-native-avbuffer-h.md#oh_avbuffer_getbufferattr)获取的PTS就是此音频帧的时间戳，可作为坐标写入音轨。

而视频帧不稳定，其时间戳需要以帧率为基础来计算下，计算公式为：视频帧的时间戳 = (1000000/帧率) \* (n-1) 。

说明

* 1000000这是指的是1s = 1000000us，是系统单调时钟的单位。
* n指的是此视频帧的在此视频里面的顺序，n=1,2...n ，第1帧时n=1，第2帧时n=2，以此类推。
* 以帧率30fps的视频为例，第1帧的时间戳为0us，第2帧的时间戳为 (1000000/30) \* 1。

获取到音频帧和视频帧的时间戳后，通过[OH\_AVMuxer\_WriteSample()](../harmonyos-references/capi-native-avmuxer-h.md#oh_avmuxer_writesample)接口将时间戳分别写入对应的轨道。这样关键的一步就完成了。主要的开发步骤如下。

1. 先完成视频录制功能，视频录制的详细开发流程可以参考[基于AVCodec编码录制HDR Vivid视频](bpta-hdrvivid.md#section85025284348)。
2. 在执行音频帧和视频帧的封装操作时，参考此章节的方法，将时间戳分别写入音轨和视频轨。
3. 视频录制完成将保存在本地，后续音画同步播放参考本章[本地视频的音画同步](bpta-audio-video-synchronization.md#section340411415017)。

### 开发步骤

详细的视频录制功能已有最佳实践介绍，并且录制后的视频保存在本地，其音画同步的开发步骤和本章本地视频音画同步一样，所以不过多赘述。这里主要介绍下，在视频录制的过程中，如何给音轨和视频轨添加时间戳。

1. 使用[OH\_AVBuffer\_GetBufferAttr()](../harmonyos-references/capi-native-avbuffer-h.md#oh_avbuffer_getbufferattr)获取音频帧的时间戳。

```
1. struct CodecBufferInfo {
2. uint32_t bufferIndex = 0;
3. uintptr_t *buffer = nullptr;
4. uint8_t *bufferAddr = nullptr;
5. OH_AVCodecBufferAttr attr = {0, 0, 0, AVCODEC_BUFFER_FLAGS_NONE};

7. explicit CodecBufferInfo(uint8_t *addr) : bufferAddr(addr){};
8. CodecBufferInfo(uint8_t *addr, int32_t bufferSize)
9. : bufferAddr(addr), attr({0, bufferSize, 0, AVCODEC_BUFFER_FLAGS_NONE}){};
10. CodecBufferInfo(uint32_t argBufferIndex, OH_AVBuffer *argBuffer)
11. : bufferIndex(argBufferIndex), buffer(reinterpret_cast<uintptr_t *>(argBuffer)) {
12. OH_AVBuffer_GetBufferAttr(argBuffer, &attr);
13. };
14. };
```

[SampleInfo.h](https://gitcode.com/harmonyos_samples/AudioToVideoSync/blob/master/entry/src/main/cpp/common/SampleInfo.h#L81-L94)

2. 用[OH\_AVMuxer\_WriteSample()](../harmonyos-references/capi-native-avmuxer-h.md#oh_avmuxer_writesample)接口将时间戳写入音频轨。s

```
1. int32_t Muxer::WriteSample(int32_t trackId, OH_AVBuffer *buffer, OH_AVCodecBufferAttr &attr){
2. std::lock_guard<std::mutex> lock(writeMutex_);

4. CHECK_AND_RETURN_RET_LOG(muxer_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Muxer is null");
5. CHECK_AND_RETURN_RET_LOG(buffer != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Get a empty buffer");

7. int32_t ret = OH_AVBuffer_SetBufferAttr(buffer, &attr);
8. CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "SetBufferAttr failed");

10. ret = OH_AVMuxer_WriteSampleBuffer(muxer_, trackId, buffer);
11. CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Write sample failed");
12. return AVCODEC_SAMPLE_ERR_OK;
13. }
```

[Muxer.cpp](https://gitcode.com/harmonyos_samples/AudioToVideoSync/blob/master/entry/src/main/cpp/capbilities/Muxer.cpp#L84-L96)

```
1. void Recorder::AudioEncOutputThread() {
2. while (true) {
3. CHECK_AND_BREAK_LOG(isStarted_, "Work done, thread out");
4. std::unique_lock<std::mutex> lock(audioEncContext_->outputMutex);
5. bool condRet = audioEncContext_->outputCond.wait_for(
6. lock, 5s, [this]() { return !isStarted_ || !audioEncContext_->outputBufferInfoQueue.empty(); });
7. CHECK_AND_BREAK_LOG(isStarted_, "Work done, thread out");
8. CHECK_AND_CONTINUE_LOG(!audioEncContext_->outputBufferInfoQueue.empty(),
9. "Buffer queue is empty, continue, cond ret: %{public}d", condRet);

11. CodecBufferInfo bufferInfo = audioEncContext_->outputBufferInfoQueue.front();
12. audioEncContext_->outputBufferInfoQueue.pop();
13. audioEncContext_->outputFrameCount++;
14. AVCODEC_SAMPLE_LOGW(
15. "Audio Out buffer count: %{public}u, size: %{public}d, flag: %{public}u, pts: %{public}" PRId64,
16. audioEncContext_->outputFrameCount, bufferInfo.attr.size, bufferInfo.attr.flags, bufferInfo.attr.pts);
17. muxer_->WriteSample(muxer_->GetAudioTrackId(), reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer),
18. bufferInfo.attr);
19. int32_t ret = audioEncoder_->FreeOutputData(bufferInfo.bufferIndex);
20. CHECK_AND_BREAK_LOG(ret == AVCODEC_SAMPLE_ERR_OK, "Encoder output thread out");
21. }
22. AVCODEC_SAMPLE_LOGI("Exit, frame count: %{public}u", audioEncContext_->inputFrameCount);
23. StartRelease();
24. }
```

[Recorder.cpp](https://gitcode.com/harmonyos_samples/AudioToVideoSync/blob/master/entry/src/main/cpp/recorder/Recorder.cpp#L295-L318)

3. 计算视频帧的时间戳，用[OH\_AVMuxer\_WriteSample()](../harmonyos-references/capi-native-avmuxer-h.md#oh_avmuxer_writesample)接口将时间戳写入视频轨。

```
1. namespace {
2. // ...
3. constexpr int64_t MICROSECOND = 1000000;
4. // ...
5. }
```

[Recorder.cpp](https://gitcode.com/harmonyos_samples/AudioToVideoSync/blob/master/entry/src/main/cpp/recorder/Recorder.cpp#L24-L32)

```
1. void Recorder::EncOutputThread() {
2. while (true) {
3. CHECK_AND_BREAK_LOG(isStarted_, "Work done, thread out");
4. std::unique_lock<std::mutex> lock(encContext_->outputMutex);
5. bool condRet = encContext_->outputCond.wait_for(
6. lock, 5s, [this]() { return !isStarted_ || !encContext_->outputBufferInfoQueue.empty(); });
7. CHECK_AND_BREAK_LOG(isStarted_, "Work done, thread out");
8. CHECK_AND_CONTINUE_LOG(!encContext_->outputBufferInfoQueue.empty(),
9. "Buffer queue is empty, continue, cond ret: %{public}d", condRet);

11. CodecBufferInfo bufferInfo = encContext_->outputBufferInfoQueue.front();
12. encContext_->outputBufferInfoQueue.pop();
13. CHECK_AND_BREAK_LOG(!(bufferInfo.attr.flags & AVCODEC_BUFFER_FLAGS_EOS), "Catch EOS, thread out");
14. lock.unlock();
15. if ((bufferInfo.attr.flags & AVCODEC_BUFFER_FLAGS_SYNC_FRAME) ||
16. (bufferInfo.attr.flags == AVCODEC_BUFFER_FLAGS_NONE)) {
17. encContext_->outputFrameCount++;
18. bufferInfo.attr.pts = encContext_->outputFrameCount * MICROSECOND / sampleInfo_.frameRate;
19. } else {
20. bufferInfo.attr.pts = 0;
21. }
22. AVCODEC_SAMPLE_LOGW("Out buffer count: %{public}u, size: %{public}d, flag: %{public}u, pts: %{public}" PRId64,
23. encContext_->outputFrameCount, bufferInfo.attr.size, bufferInfo.attr.flags,
24. bufferInfo.attr.pts);

26. muxer_->WriteSample(muxer_->GetVideoTrackId(), reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer),
27. bufferInfo.attr);
28. int32_t ret = videoEncoder_->FreeOutputBuffer(bufferInfo.bufferIndex);
29. CHECK_AND_BREAK_LOG(ret == AVCODEC_SAMPLE_ERR_OK, "Encoder output thread out");
30. }
31. AVCODEC_SAMPLE_LOGI("Exit, frame count: %{public}u", encContext_->outputFrameCount);
32. StartRelease();
33. }
```

[Recorder.cpp](https://gitcode.com/harmonyos_samples/AudioToVideoSync/blob/master/entry/src/main/cpp/recorder/Recorder.cpp#L119-L151)

```
1. int32_t Muxer::WriteSample(int32_t trackId, OH_AVBuffer *buffer, OH_AVCodecBufferAttr &attr){
2. std::lock_guard<std::mutex> lock(writeMutex_);

4. CHECK_AND_RETURN_RET_LOG(muxer_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Muxer is null");
5. CHECK_AND_RETURN_RET_LOG(buffer != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Get a empty buffer");

7. int32_t ret = OH_AVBuffer_SetBufferAttr(buffer, &attr);
8. CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "SetBufferAttr failed");

10. ret = OH_AVMuxer_WriteSampleBuffer(muxer_, trackId, buffer);
11. CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Write sample failed");
12. return AVCODEC_SAMPLE_ERR_OK;
13. }
```

[Muxer.cpp](https://gitcode.com/harmonyos_samples/AudioToVideoSync/blob/master/entry/src/main/cpp/capbilities/Muxer.cpp#L84-L96)

4. 执行封装操作，将录制的音频帧和视频帧封装成本地视频文件，并存入媒体库中。

```
1. int32_t Recorder::Start() {
2. std::lock_guard<std::mutex> lock(mutex_);
3. CHECK_AND_RETURN_RET_LOG(!isStarted_, AVCODEC_SAMPLE_ERR_ERROR, "Already started.");
4. CHECK_AND_RETURN_RET_LOG(encContext_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Already started.");
5. CHECK_AND_RETURN_RET_LOG(videoEncoder_ != nullptr && muxer_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR,
6. "Already started.");

8. int32_t ret = muxer_->Start();
9. CHECK_AND_RETURN_RET_LOG(ret == AVCODEC_SAMPLE_ERR_OK, ret, "Muxer start failed");
10. ret = videoEncoder_->Start();
11. CHECK_AND_RETURN_RET_LOG(ret == AVCODEC_SAMPLE_ERR_OK, ret, "Encoder start failed");

13. isStarted_ = true;
14. encOutputThread_ = std::make_unique<std::thread>(&Recorder::EncOutputThread, this);
15. if (encOutputThread_ == nullptr) {
16. AVCODEC_SAMPLE_LOGE("Create thread failed");
17. StartRelease();
18. return AVCODEC_SAMPLE_ERR_ERROR;
19. }

21. if (audioEncContext_) {
22. // Start AudioCapturer
23. audioCapturer_->AudioCapturerStart();

25. ret = audioEncoder_->Start();
26. CHECK_AND_RETURN_RET_LOG(ret == AVCODEC_SAMPLE_ERR_OK, ret, "Audio Encoder start failed");
27. isStarted_ = true;
28. audioEncInputThread_ = std::make_unique<std::thread>(&Recorder::AudioEncInputThread, this);
29. audioEncOutputThread_ = std::make_unique<std::thread>(&Recorder::AudioEncOutputThread, this);
30. if (audioEncInputThread_ == nullptr || audioEncOutputThread_ == nullptr) {
31. AVCODEC_SAMPLE_LOGE("Create thread failed");
32. StartRelease();
33. return AVCODEC_SAMPLE_ERR_ERROR;
34. }

36. if (audioEncContext_ != nullptr) {
37. audioEncContext_->ClearCache();
38. }
39. }

41. AVCODEC_SAMPLE_LOGI("Succeed");
42. return AVCODEC_SAMPLE_ERR_OK;
43. }
```

[Recorder.cpp](https://gitcode.com/harmonyos_samples/AudioToVideoSync/blob/master/entry/src/main/cpp/recorder/Recorder.cpp#L73-L115)

5. 从媒体库中选择录制的视频，进行音画同步的播放。后续开发步骤参考本章[本地视频的音画同步](bpta-audio-video-synchronization.md#section340411415017)。

## 示例代码

* [实现音画同步播放效果](https://gitcode.com/harmonyos_samples/AudioToVideoSync)
