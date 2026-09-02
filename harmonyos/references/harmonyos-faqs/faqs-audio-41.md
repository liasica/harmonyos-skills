---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-41
title: 使用OHAudio播放音频码流如何让音量最大
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 使用OHAudio播放音频码流如何让音量最大
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:32398db246bc25cc038b984641e07c3408bba5124d9eb174426a14e19db9c82d
---

## 问题现象

使用OHAudio播放音频码流如何让声音最大？

## 背景知识

* [OH\_AudioRenderer\_SetVolume](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_setvolume)可以设置当前音频流音量值。
* [OH\_AudioRenderer\_SetDefaultOutputDevice()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_setdefaultoutputdevice)可以设置默认本机内置发声设备。
* PCM码流本身也可以通过乘数的方式手动提高音量。

## 解决方案

使用OHAudio播放音频码流可以通过以下三种方式提高音量：

* 开发者可使用OH\_AudioRenderer\_SetVolume接口设置当前音频流音量值，1.0为最大值。

  ```screen
  // 要设置的音量值，音量值的范围是[0.0f, 1.0f]。
  float volume = 1.0f;
  // 设置当前音频流音量值。
  OH_AudioStream_Result state = OH_AudioRenderer_SetVolume(m_renderer, volume);
  ```
* 当音频流类型[OH\_AudioStream\_Usage](../harmonyos-references/capi-native-audiostream-base-h.md#oh_audiostream_usage)为语音消息、VoIP语音通话或者VoIP视频通话的场景时可以使用OH\_AudioRenderer\_SetDefaultOutputDevice()方法设置本机内置发声设备为扬声器获得最大音量的效果。

  ```screen
  // 设置本机内置发声设备为扬声器。
  OH_AudioRenderer_SetDefaultOutputDevice(m_renderer, AUDIO_DEVICE_TYPE_SPEAKER);
  ```
* PCM码流本身可以直接做乘以系数的操作以提高音量。

  ```screen
  void AudioHelper::RaiseVolume(char *buf, uint32_t size, double vol) {
      OH_LOG_INFO(LOG_APP, "RaiseVolume");
      if (!size) {
          return;
      }
      for (int i = 0; i < size; i += 2) {
          // 根据不同位数的PCM数据设置上下界，此处以16位PCM为例
          signed long minData = -0x8000;
          signed long maxData = 0x7FFF;
          // 拼接单个16位样本
          signed short wData = buf[i + 1];
          wData = MAKEWORD(buf[i], buf[i + 1]);
          signed long dwData = wData;
          // 对样本做数乘和上下限控制
          dwData = dwData * vol;
          if (dwData < minData) {
              dwData = minData;
          } else if (dwData > maxData) {
              dwData = maxData;
          }
          wData = LOWORD(dwData);
          // 将处理后的数据保存
          buf[i] = LOBYTE(wData);
          buf[i + 1] = HIBYTE(wData);
      }
  }
  ```

  OH\_AudioRenderer\_SetDefaultOutputDevice()接口允许在AudioRenderer创建以后的任何时间被调用，系统会记录应用设置的默认本机内置发声设备。在应用启动播放时，若有外接设备如蓝牙耳机/有线耳机接入，系统优先从外接设备发声；否则系统遵循应用设置的默认本机内置发声设备发声。
