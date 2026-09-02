---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-44
title: AudioRenderer设置音频流后输出设备不符合预期
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > AudioRenderer设置音频流后输出设备不符合预期
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:da1a1e33e37f1c7f5cecf6820a247a4ccf1d920bb32d16479b95b2f8a58f4da6
---

## 问题现象

```ts
export class AudioRenderPlayer {
  private renderModel: audio.AudioRenderer | undefined = undefined;
  private audioStreamInfo: audio.AudioStreamInfo = {
    samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_16000, // 采样率
    channels: audio.AudioChannel.CHANNEL_1, // 通道
    sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式
    encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式
  }
  private audioRendererInfo: audio.AudioRendererInfo = {
    usage: audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, // 音频流使用类型
    rendererFlags: 0 // 音频渲染器标志
  }
  private audioRendererOptions: audio.AudioRendererOptions = {
    streamInfo: this.audioStreamInfo,
    rendererInfo: this.audioRendererInfo
  }
}
```

通过以上代码配置音频渲染参数以便后面创建AudioRenderer实例，预期使用扬声器播放，实际从听筒发出声音，为什么？

## 背景知识

音频流类型是定义音频数据播放和录制方式的关键属性。对于播放流，其类型由[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)确定。音频流类型对输出设备的选择具有决定性影响。

## 问题定位

问题代码中音频流类型是**STREAM\_USAGE\_VOICE\_COMMUNICATION**，从音频流使用类型可知，**STREAM\_USAGE\_VOICE\_COMMUNICATION**的播放流类型为语音消息，在[音频流类型](../harmonyos-references/arkts-apis-audio-e.md#audiovolumetype)中应属于VOICE\_CALL。

## 分析结论

**STREAM\_USAGE\_VOICE\_COMMUNICATION**音频流所属的音量类型为通话音量，[默认输出设备](../harmonyos-guides/using-right-streamusage-for-playback.md#输出设备选择)为听筒，所以音频声音会从听筒发出。

## 修改建议

* 可以尝试更换音频流类型为**STREAM\_USAGE\_MUSIC**，默认会从扬声器播放。

  ```ts
  let audioRendererInfo: audio.AudioRendererInfo = {
    usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
    rendererFlags: 0 // 音频渲染器标志。
  };
  ```

  完整代码可参考：使用AudioRenderer开发音频播放功能[完整示例](../harmonyos-guides/using-audiorenderer-for-playback.md#完整示例)。
* 若默认的输入/输出设备不符合使用诉求，应用也可以调用[setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setdefaultoutputdevice12)接口主动修改默认输出设备，值得注意的是，该接口仅适用于StreamUsage为语音消息（STREAM\_USAGE\_VOICE\_MESSAGE）、VoIP语音通话（STREAM\_USAGE\_VOICE\_COMMUNICATION）或者VoIP视频通话（STREAM\_USAGE\_VIDEO\_COMMUNICATION）的场景。
