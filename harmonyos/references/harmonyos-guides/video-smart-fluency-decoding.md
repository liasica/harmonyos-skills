---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-smart-fluency-decoding
title: 智能流畅倍速解码
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > 智能流畅倍速解码
category: harmonyos-guides
scraped_at: 2026-10-17T06:42:05+08:00
doc_updated_at: 2026-10-16
content_hash: sha256:3af500645c84490ed7cb7da9e963430cfc700f99f486ccef12009cdf9c51e026
---

## 能力简介

从API版本26.0.0开始，新增支持智能流畅倍速解码能力，通过结合硬件解码能力与人因感知模型实现系统级解码性能优化。

在传统多媒体架构中，开启高倍速播放会导致视频理论帧率成倍增加（如60fps视频在3.0x下需每秒处理180帧），并带来以下问题。

1. 移动端设备的视频送显帧率通常受限于整机功耗管控（常为60fps），远低于高倍速下的理论帧率。此外，在高速动态画面下，受限于人眼的视觉暂留效应与动态视觉敏感度下降，强行解码并渲染超出分辨能力的微小运动帧，会产生无效的算力消耗。
2. 传统架构中的倍速丢帧通常在应用层的渲染端被动触发，此时多余帧的解码算力已经消耗。若应用层试图在解码前主动进行内容感知，则需引入高耗能的像素级计算（如光流分析），导致整体功耗反而增加。

使用智能流畅倍速解码能力，系统无需进行复杂的像素级图像分析，而是直接利用硬件解码器输出的运动矢量（Motion Vectors，简称MV）以及视频码流的时域分层特征。实现在解码前精准剔除视觉感知权重较低的非关键帧，避免无效的解码计算。该能力在降低解码与渲染负载、有效控制设备发热的同时，能提供比单纯均匀抽帧更平滑连贯的播放体验。

## 帧保留模式详解

系统提供以下三种帧保留模式，供开发者按需切换。

| 模式 | 实现原理 | 使用场景 |
| --- | --- | --- |
| **感知自适应（ADAPTIVE）** | 系统依据应用传入的当前倍速，动态分析视频运动特征，优先剔除视觉感知权重较低的非关键帧。 | **推荐使用本模式**。主要用于高倍速播放场景，提供比无内容差别均匀抽帧更符合人眼视觉连贯性的平滑体验。 |
| **全量直通（FULL）** | 对所有输入帧进行解码输出，不进行丢帧处理。 | 适用于非倍速或慢速播放场景。 |
| **平滑定比（UNIFORM）** | 系统按开发者指定的固定比例均匀地进行抽帧。 | 适用于特殊的降载与提速场景，如高温场景下的降载降温，以及编辑预览场景下的拖拽流畅性提升。 |

## 参数说明

本能力需主动下发配置才可以生效。通过在[OH\_AVFormat](../harmonyos-references/capi-core-oh-avformat.md)中配置以下键值对来精确控制行为。

1. **OH\_MD\_KEY\_VIDEO\_DECODER\_FRAME\_RETENTION\_MODE（模式配置）**

   * 类型：int32\_t
   * 取值范围：参考[OH\_FrameRetentionMode](../harmonyos-references/capi-native-avcodec-base-h.md#oh_frameretentionmode)。
   * 描述：能力的总开关与模式选择，可通过[OH\_VideoDecoder\_Configure()](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_configure)在初始化阶段配置，也可通过[OH\_VideoDecoder\_SetParameter()](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_setparameter)在运行态切换。正常倍速起播时，建议初始化为全量直通模式。
2. **OH\_MD\_KEY\_VIDEO\_DECODER\_SPEED（解码倍速）**

   * 类型：double
   * 取值范围：严格大于0.0。
   * 描述：配置或切换到感知自适应模式时，建议同时显式配置当前播放倍速，以获得最佳的算法准确性；倍速变化时建议同步更新。初始化为全量直通模式时无需配置。
3. **OH\_MD\_KEY\_VIDEO\_DECODER\_FRAME\_RETENTION\_RATIO（保留比例）**

   * 类型：double
   * 取值范围：[0.01, 1.0]（例如0.5表示保留50%的解码帧）。
   * 描述：仅在平滑定比模式下生效。当配置越界或异常时，系统默认以30fps为目标帧率进行兜底。

## 约束与限制

* **格式支持**：此能力仅在视频解码链路生效，当前仅支持H.264、H.265及H.266码流格式。
* **参数异常兜底**：在平滑定比模式下，若传入的保留比例非法或未明确指定，系统将默认以30fps为目标输出帧率进行解码与送显。
* **硬件能力降级**：感知自适应模式依赖硬件解码器输出运动矢量（MV）信息的能力。在无法提供MV数据的硬件平台上，系统将在底层自动触发基础降级策略（对外仍保留感知自适应模式状态）。此时系统仍能维持基础的流畅播放效果，但无法获得基于内容感知的最佳收益。
* **MV信息输出**：感知自适应模式依赖解码过程中输出的MV信息，具体配置要求随系统版本不同而变化。
  + 在搭载HarmonyOS 7.0.0.109及以上版本的设备上，无论初始化时配置为哪种帧保留模式，运行态切换到感知自适应模式后均可获取MV信息。MV信息是否可用仍取决于硬件解码器的支持能力。
  + 在HarmonyOS 7.0.0.109之前支持本能力的系统版本中，需在初始化阶段配置感知自适应模式，才能获取MV信息。若初始化为其他模式，运行态切换到感知自适应模式后将无法获取MV信息，丢帧策略退化为按固定间隔丢帧（解码帧率≥45fps时目标输出帧率为45fps，否则不丢帧），感知自适应收益降低。
* **音视频同步（AV Sync）安全**：智能倍速丢帧机制仅决定帧的存留，不会修改保留帧原始的PTS（显示时间戳）与DTS（解码时间戳）信息，不影响音画同步。

## 倍速播放场景开发实践

对于常规视频播放业务，建议采用**初始化阶段配置与动态切换结合**的策略。

* **初始化配置**：以正常倍速起播时，在视频起播前配置为全量直通模式，无需设置解码倍速参数。
* **动态切换**：在播放过程中，当目标倍速大于1.0x时，通过OH\_VideoDecoder\_SetParameter()在同一个OH\_AVFormat中下发感知自适应模式与当前倍速；当恢复至1.0x及以下倍速时，切回全量直通模式，恢复全量帧解码输出。

### 初始化阶段配置

以下示例以正常倍速起播，配置全量直通模式。SetOptionalFormatFeatures在完成同步模式配置后，当sampleInfo.codec.isSmartFluencySupported为true时调用ConfigureSmartFluency(format)并检查返回值。随后由VideoDecoder::Configure调用OH\_VideoDecoder\_Configure()完成配置。该辅助函数仅设置本能力的参数，不负责创建或销毁OH\_AVFormat。

如果业务直接以高倍速起播，也可在初始化阶段配置感知自适应模式，建议同时显式设置OH\_MD\_KEY\_VIDEO\_DECODER\_SPEED为实际起播倍速。

```
bool ConfigureSmartFluency(OH_AVFormat *format)
{
    bool ret = OH_AVFormat_SetIntValue(format, OH_MD_KEY_VIDEO_DECODER_FRAME_RETENTION_MODE,
        OH_FRAME_RETENTION_MODE_FULL);
    CHECK_AND_RETURN_RET_LOG(ret, false, "Set smart fluency initial mode failed");
    return true;
}
```

### 运行态按需切换

系统支持在运行态下动态切换帧保留模式。开发者可通过调用OH\_VideoDecoder\_SetParameter()实时下发配置，参数的生效时机与该接口的标准行为一致。

```
int32_t VideoDecoder::OnUserSpeedChanged(double targetSpeed)
{
    OH_AVFormat *param = OH_AVFormat_Create();
    CHECK_AND_RETURN_RET_LOG(param != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "AVFormat create failed");

    // 引入epsilon处理double类型的精度比较。
    const double EPSILON = 1e-6;

    const bool enableAdaptive = targetSpeed > 1.0 + EPSILON;
    if (enableAdaptive) {
        // 场景：高倍速播放(如1.5x，2.0x，3.0x等)。
        // 策略：使能感知自适应模式。
        OH_AVFormat_SetIntValue(param, OH_MD_KEY_VIDEO_DECODER_FRAME_RETENTION_MODE,
                                OH_FRAME_RETENTION_MODE_ADAPTIVE);
        OH_AVFormat_SetDoubleValue(param, OH_MD_KEY_VIDEO_DECODER_SPEED, targetSpeed);
    } else {
        // 场景：正常播放(1.0x)或慢速播放(<1.0x)。
        // 策略：切换到全量直通模式，保障帧帧送显。
        OH_AVFormat_SetIntValue(param, OH_MD_KEY_VIDEO_DECODER_FRAME_RETENTION_MODE,
                                OH_FRAME_RETENTION_MODE_FULL);
    }

    // 实时下发参数，动态调整系统帧保留策略。
    int32_t ret = OH_VideoDecoder_SetParameter(decoder_, param);
    OH_AVFormat_Destroy(param);
    CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR,
                             "SetParameter failed, ret: %{public}d", ret);
    if (enableAdaptive) {
        AVCODEC_SAMPLE_LOGI("Smart fluency mode changed to ADAPTIVE, speed: %{public}.2f", targetSpeed);
    } else {
        AVCODEC_SAMPLE_LOGI("Smart fluency mode changed to FULL");
    }
    return AVCODEC_SAMPLE_ERR_OK;
}
```

## 其他有益场景开发实践

除了在倍速播放场景下推荐使用本能力外，以下场景也可通过使用本能力获得性能和体验收益。

* **高温场景下的降载降温**：当设备发热触发温控告警时，控制功耗的需求将高于维持高帧率。开发者可切换至平滑定比模式，并配置较低的帧保留比例（如0.3），通过减少解码和显示帧率来降低系统负载，从而有效辅助设备降温。
* **编辑预览场景下的拖拽流畅性提升**：在视频编辑等需要频繁拖拽进度条的场景中，全量解码途经帧会显著拖慢画面的刷新响应。开发者可在此状态下临时切入平滑定比模式，并配置较低的帧保留比例，通过适当减少途经画面的解码帧数来换取更快的画面刷新速度，从而显著提升交互的跟手感与流畅性。

**示例（以应对温控告警为例）：**

```
int32_t VideoDecoder::OnThermalWarningReceived(double ratio)
{
    OH_AVFormat *param = OH_AVFormat_Create();
    CHECK_AND_RETURN_RET_LOG(param != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "AVFormat create failed");

    // 采用UNIFORM平滑定比模式。
    OH_AVFormat_SetIntValue(param, OH_MD_KEY_VIDEO_DECODER_FRAME_RETENTION_MODE,
                            OH_FRAME_RETENTION_MODE_UNIFORM);

    // 设定保留比例（如0.3表示仅保留30%的解码帧输出）。
    OH_AVFormat_SetDoubleValue(param, OH_MD_KEY_VIDEO_DECODER_FRAME_RETENTION_RATIO, ratio);

    // 实时下发生效，系统将执行均匀的抽帧剔除，降低整机负载。
    int32_t ret = OH_VideoDecoder_SetParameter(decoder_, param);
    OH_AVFormat_Destroy(param);
    CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR,
                             "SetParameter failed, ret: %{public}d", ret);
    return AVCODEC_SAMPLE_ERR_OK;
}
```
