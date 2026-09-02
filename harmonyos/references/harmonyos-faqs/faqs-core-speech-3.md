---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-core-speech-3
title: 语音识别数据源问题
breadcrumb: FAQ > AI功能开发 > 机器学习 > 基础语音（Core Speech） > 语音识别数据源问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:c5a439c86052e052245df22fc031cf2da0b56254901d7d391e54016c697b76dc
---

## 问题现象

录制一个小于60s的pcm格式数据源用于语音识别，但是录入的音频文件过大，识别结果报错：errorCode: 1002200003 errorMessage: write audio fail with beyond max of audio，对于这种情况该如何识别。音频采集配置代码为：

```screen
import audio from '@ohos.multimedia.audio';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率
  channels: audio.AudioChannel.CHANNEL_2, // 通道
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式
}
let audioCapturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE_TYPE_MIC, // 音源类型
  capturerFlags: 0 // 音频采集器标志
}
let audioCapturerOptions: audio.AudioCapturerOptions = {
  streamInfo: audioStreamInfo,
  capturerInfo: audioCapturerInfo
}
```

## 背景知识

[AudioInfo](../harmonyos-references/hms-ai-speechrecognizer.md#audioinfo)是启动语音识别的音频配置信息，有以下几个关键参数：

* audioType（音频类型）：当前仅支持“pcm”。
* sampleRate（音频的采样率）：当前仅支持16000采样率。
* sampleBit（音频返回的采样位数）：当前仅支持16位。
* soundChannel（音频返回的通道数信息）：当前仅支持通道1。

其中pcm音频字节大小计算规则：sampleRate \* (sampleBit / 8) \* soundChannel \* 时间，60s音频的最大字节数为16000 \* 16 / 8 \* 1 \* 60 = 1920KByte。

## 解决方案

根据AudioInfo的配置信息，将原本的audioStreamInfo的samplingRate（采样率）修改为：audio.AudioSamplingRate.SAMPLE\_RATE\_16000，将channels（通道）修改为audio.AudioChannel.CHANNEL\_1。

## 常见FAQ

Q：根据API文档相关介绍，当前speechRecognizer只支持pcm格式的音频数据。传入mp3格式的音频数据，调用startListener后只有onStart回调，其他如onError或者onComplete无回调。对于mp3，wav格式的文件是否有第三方库支持语音识别？

A：目前语音识别仅支持pcm格式，如果需要转其他格式可以考虑使用三方库提供的转码支持功能，将录制的数据转码成pcm格式。

Q：在使用语音识别功能时，使用AudioCapturer的录音功能，录制后的文件不能正常播放(有文件大小，导出后播放提示文件已损坏)。

A：AudioCapturer是音频采集器，用于录制pcm（Pulse Code Modulation）音频数据，得到的pcm格式文件不支持预览。验证阶段可以把录音文件导出来，用三方软件比如Audacity转为可以播放的格式。

Q：点击writeAudio按钮后，运行到本段代码被阻断，asrEngine.writeAudio("123456", unit8Array)未执行到就打印出日志，是缺少什么权限吗？

```screen
private async writeAudio() {
  console.info("writeAudio start")
  let ctx = this.getUIContext().getHostContext();
  let filenames: string[] = fileIo.listFileSync(ctx.filesDir);
  if (filenames.length <= 0) {
    console.info("writeAudio stop")
    return;
  }
}
```

A：writeAudio()中的filename<0是因为文件没有推到手机里/权限不够，导致asrEngine.writeAudio("123456", unit8Array)未执行到。可以在测试真机中导入pcm格式文件并打开读写权限，即可正常运行，导入方法：

```screen
hdc_std list targets
hdc_std file send long.pcm /data/app/el2/100/base/com.huawei.ohos.hiaiuser/haps/hiaiuser/files
hdc_std shell chmod 777 /data/app/el2/100/base/com.huawei.ohos.hiaiuser/haps/hiaiuser/files/long.pcm
```

Q：语音识别功能的识别率有点低，该怎么设置来提高识别率，后期会不会更加强大？

A：识别率在于模型，后面模型肯定会优化的。

Q：语音转文字报错：1002200009 Failed to write audio data。

A：错误码1002200009表示写入音频数据失败。参考[writeAudio](../harmonyos-references/hms-ai-speechrecognizer.md#writeaudio)，该报错的原因可能有：

1. 最大音频长度超过60000ms。
2. 会话id字符不合法。
3. 未将pcm音频文件数据处理为640字节或1280字节。

Q：语音转文字报错：1002200010 write audio failed because the start listening is failed。

A：错误码[1002200010](../harmonyos-references/errorcode-corespeech.md#section1002200010-语音识别未启动)表示语音识别未启动。该报错的原因可能是启动语音识别的相关参数出现错误，常见的是传入的音频文件不是pcm格式。
