---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-38
title: 如何优化OHAudio音频播放卡顿的问题
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 如何优化OHAudio音频播放卡顿的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:44227a8d72f0411163216da25d599064fcf53661ea63c342ab0e3aff015373fd
---

## 问题现象

使用OHAudio native播放单声道采样为8000的单声道音频PCM，出现卡顿现象。

问题代码示例参考如下：

```
int32_t writeAudioData(OH_AudioRenderer* renderer, void* context, void* buffer, int32_t length){
  Audio* pAudio = (Audio*)context;
  AVData aVData;
  if (pAudio->pQueue->Pop(aVData)) {
    memcpy(buffer, aVData.frameBuffer, aVData.size);
    length = aVData.size;
    OH_LOG_INFO(LOG_APP, "这里播放音频length:%{public}d", length);
  }
  return 0;
}
```

## 背景知识

[OHAudio](../harmonyos-guides/using-ohaudio-for-playback.md)是系统在API version 10中引入的一套C API，此API在设计上实现归一，同时支持普通音频通路和低时延通路。仅支持PCM格式，适用于依赖Native层实现音频输出功能的场景。

在设置音频回调函数时API version 12新增回调函数[OH\_AudioRenderer\_OnWriteDataCallback](../harmonyos-references/capi-native-audiostream-base-h.md#oh_audiorenderer_onwritedatacallback)用于写入音频数据。

* 在能填满回调所需长度数据的情况下，返回AUDIO\_DATA\_CALLBACK\_RESULT\_VALID，系统会取用完整长度的数据缓冲进行播放。请不要在未填满数据的情况下返回AUDIO\_DATA\_CALLBACK\_RESULT\_VALID，否则会导致杂音、卡顿等现象。
* 在无法填满回调所需长度数据的情况下，建议开发者返回AUDIO\_DATA\_CALLBACK\_RESULT\_INVALID，系统不会处理该段音频数据，然后会再次向应用请求数据，确认数据填满后返回AUDIO\_DATA\_CALLBACK\_RESULT\_VALID。

## 问题定位

检查OH\_AudioData\_Callback\_Result (\*OH\_AudioRenderer\_OnWriteDataCallback)(OH\_AudioRenderer\* renderer, void\* userData,void\* audioData, int32\_t audioDataSize)回调中往audioData中所填待播放数据长度是否是audioDataSize。

## 分析结论

缓存区间长度audioDataSize较大导致往audioData中所填待播放数据长度小于audioDataSize。过大的buffer会导致声音延迟增加，或者在所填充数据不足audioDataSize时出现噪音。

## 修改建议

* 可以通过调用OH\_AudioStreamBuilder\_SetFrameSizeInCallback将audioDataSize设为20ms音频数据对应的帧长。保证往audioData中填满audioDataSize长度的待播放数据，否则会导致音频服务播放杂音。
* 在使用OH\_AudioRenderer\_OnWriteDataCallback写入音频数据时，如果无法填满回调所需长度的数据，返回AUDIO\_DATA\_CALLBACK\_RESULT\_INVALID，系统不会处理该段音频数据，然后再次向应用请求数据，确认数据填满后返回AUDIO\_DATA\_CALLBACK\_RESULT\_VALID。
