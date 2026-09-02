---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-43
title: 如何生成播放一段脉冲音频
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 如何生成播放一段脉冲音频
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:66fae172163058cd14af2f2e0880072095e6300a4b50e0086f952db132f9eafb
---

## 问题现象

在实现音频开发过程中，能否不通过现有音频或者录制音频，直接生成一段脉冲音频并进行播放？

## 背景知识

[AudioRenderer](../harmonyos-guides/using-audiorenderer-for-playback.md)：用于音频输出的API，仅支持PCM格式，需要应用持续写入音频数据进行工作。应用可以在输入前添加数据预处理，如设定音频文件的采样率、位宽等，要求开发者具备音频处理的基础知识，适用于更专业、更多样化的媒体播放应用开发。

## 解决方案

以生成一段正弦脉冲波为例。

```ts
private renderer?: audio.AudioRenderer;
private data = new Uint8Array(0);
private writeOffset = 0;
static SAMPLE_RATE = 44100;
static DURATION_MS = 10000;
static FREQUENCY = 1000;

/**
 * 生成脉冲音频
 * */
private generatePulse() {
  let numSamples = Math.floor(PulseAudioGenerator.SAMPLE_RATE * (PulseAudioGenerator.DURATION_MS / 1000));
  let uint16Max = Math.pow(2, 15) - 1;
  let data = new Uint16Array(numSamples);
  for (let i = 0; i < numSamples; i++) {
    let angle = 2.0 * Math.PI * i / (PulseAudioGenerator.SAMPLE_RATE / PulseAudioGenerator.FREQUENCY);
    let envelope = Math.exp(-i / (numSamples / 5.0));
    data[i] = Math.floor(uint16Max * Math.sin(angle) * envelope);
  }
  this.data = new Uint8Array(data.buffer);
}
```

生成正弦波脉冲音频后，可以使用[AudioRenderer](../harmonyos-guides/using-audiorenderer-for-playback.md)进行播放，其中需要调用[on('writeData')方法](../harmonyos-references/arkts-apis-audio-audiorenderer.md#onwritedata11)，订阅监听音频数据写入回调。此处将生成的data中的数据写入到创建的bufferView中，再送到AudioRenderer进行播放。

```ts
/**
 * 启动播放
 * */
async startRenderer() {
  this.generatePulse();
  let audioStreamInfo: audio.AudioStreamInfo = {
    channels: audio.AudioChannel.CHANNEL_1,
    samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_44100,
    encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW,
    sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
  };

  let audioRendererInfo: audio.AudioRendererInfo = {
    usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
    rendererFlags: 0
  };

  let audioRendererOptions: audio.AudioRendererOptions = {
    streamInfo: audioStreamInfo,
    rendererInfo: audioRendererInfo,
  };

  this.renderer = await audio.createAudioRenderer(audioRendererOptions);
  this.writeOffset = 0;
  this.renderer.on('writeData', (buffer: ArrayBuffer) => {
    let bufferView = new Uint8Array(buffer);
    let writeLen = Math.min(buffer.byteLength, this.data.byteLength - this.writeOffset);
    if (writeLen <= 0) {
      this.writeOffset = 0;
      this.stopAndRelease();
      console.info('Play Done');
      return audio.AudioDataCallbackResult.INVALID;
    }
    bufferView.set(this.data.slice(this.writeOffset, this.writeOffset + writeLen));
    this.writeOffset += writeLen;
    return audio.AudioDataCallbackResult.VALID;
  });

  await this.renderer.start();
}

/**
 * 释放资源
 * */

async stopAndRelease() {
  if (this.renderer === undefined) {
    return;
  }
  await this.renderer.stop();
  await this.renderer.release();
  this.renderer = undefined;
}
```

## 总结

将脉冲采样点保存到内存Buffer或者沙箱文件中就相当于创建了一段脉冲音频。后续可以从内存Buffer或沙箱文件中读出脉冲数据，通过AudioRenderer播放。
