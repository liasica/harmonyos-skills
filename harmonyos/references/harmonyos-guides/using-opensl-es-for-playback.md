---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-opensl-es-for-playback
title: 使用OpenSL ES开发音频播放功能(C/C++)
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > OpenSL ES开发指导(不再推荐) > 使用OpenSL ES开发音频播放功能(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:40+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:02b3c440eb49122e453fb394b17ef4fecd1547297fe26c2682e2ebb5c15d729a
---

OpenSL ES全称为Open Sound Library for Embedded Systems，是一个嵌入式、跨平台、免费的音频处理库。为嵌入式移动多媒体设备上的应用开发者提供标准化、高性能、低延迟的API。HarmonyOS的Native API基于[Khronos Group](https://www.khronos.org/)开发的[OpenSL ES](https://www.khronos.org/opensles/) 1.0.1 API 规范实现，开发者可以通过<OpenSLES.h>和<OpenSLES\_OpenHarmony.h>在HarmonyOS上使用相关API。

## 使用OHAudio替代OpenSL ES

HarmonyOS上的OpenSL ES接口，是早期SDK8版本开始提供，用于支持应用Native层音频开发的接口。但随着版本演进，接口定义的可扩展性不足，不再能满足音频系统的能力拓展，因此当前已不再推荐应用开发者继续使用此接口进行音频功能开发，可能存在一些接口能力不足的缺陷。

在SDK10版本，HarmonyOS推出了OHAudio接口，并将系统具备的所有音频功能都通过此接口开放。OHAudio接口已能够覆盖OpenSL ES在HarmonyOS中已提供的所有能力，并拓展支持音频焦点事件，低时延等新版本特性。

OHAudio的开发指南请参考：[推荐使用OHAudio开发音频播放功能(C/C++)](using-ohaudio-for-playback.md)。

考虑到一些接入HarmonyOS较早的应用开发者，这里提供了一份OpenSL ES接口切换到OHAudio的对照参考：[从OpenSL ES切换到OHAudio(C/C++)](replace-opensles-by-ohaudio.md)，便于开发者能够更快的在新版本切换到使用新接口。

## HarmonyOS上的OpenSL ES

OpenSL ES中提供了以下的接口，HarmonyOS当前仅实现了部分[接口](https://gitcode.com/openharmony/third_party_opensles/blob/master/api/1.0.1/OpenSLES.h)，可以实现音频播放的基础功能。

调用未实现接口后会返回**SL\_RESULT\_FEATURE\_UNSUPPORTED**, 当前没有相关扩展可以使用。

以下列表列举了HarmonyOS上已实现的OpenSL ES的接口，具体说明请参考[OpenSL ES](https://www.khronos.org/opensles/)规范：

* **HarmonyOS上支持的SLInterfaceID：**

  | SLInterfaceID | 说明 |
  | --- | --- |
  | SL\_IID\_ENGINE | 通用引擎，提供创建播放对象接口。 |
  | SL\_IID\_PLAY | 提供播放状态接口。 |
  | SL\_IID\_VOLUME | 提供音频播放流音量调节和读取接口。 |
  | SL\_IID\_OH\_BUFFERQUEUE | 提供音频播放流数据回调注册接口。 |
* **HarmonyOS上支持的Engine接口：**

  + SLresult (\*CreateAudioPlayer) (SLEngineItf self, SLObjectItf \* pPlayer, SLDataSource \*pAudioSrc, SLDataSink \*pAudioSnk, SLuint32 numInterfaces, const SLInterfaceID \* pInterfaceIds, const SLboolean \* pInterfaceRequired)
  + SLresult (\*CreateAudioRecorder) (SLEngineItf self, SLObjectItf \* pRecorder, SLDataSource \*pAudioSrc, SLDataSink \*pAudioSnk, SLuint32 numInterfaces, const SLInterfaceID \* pInterfaceIds, const SLboolean \* pInterfaceRequired)
  + SLresult (\*CreateOutputMix) (SLEngineItf self, SLObjectItf \* pMix, SLuint32 numInterfaces, const SLInterfaceID \* pInterfaceIds, const SLboolean \* pInterfaceRequired)
* **HarmonyOS上支持的Object接口：**

  + SLresult (\*Realize) (SLObjectItf self, SLboolean async)
  + SLresult (\*GetState) (SLObjectItf self, SLuint32 \* pState)
  + SLresult (\*GetInterface) (SLObjectItf self, const SLInterfaceID iid, void \* pInterface)
  + void (\*Destroy) (SLObjectItf self)
* **HarmonyOS上支持的Playback接口：**

  + SLresult (\*SetPlayState) (SLPlayItf self, SLuint32 state)
  + SLresult (\*GetPlayState) (SLPlayItf self, SLuint32 \*pState)
* **HarmonyOS上支持的Volume控制接口：**

  + SLresult (\*SetVolumeLevel) (SLVolumeItf self, SLmillibel level)
  + SLresult (\*GetVolumeLevel) (SLVolumeItf self, SLmillibel \*pLevel)
  + SLresult (\*GetMaxVolumeLevel) (SLVolumeItf self, SLmillibel \*pMaxLevel)
* **HarmonyOS上支持的BufferQueue接口：**

  以下接口需引入<OpenSLES\_OpenHarmony.h>使用。

  | 接口 | 说明 |
  | --- | --- |
  | SLresult (\*Enqueue) (SLOHBufferQueueItf self, const void \*buffer, SLuint32 size) | 根据情况将buffer加到相应队列中。  如果是播放操作，则将带有音频数据的buffer插入到filledBufferQ\_队列中；如果是录音操作，则将录音使用后的空闲buffer插入到freeBufferQ\_队列中。  self：表示调用该函数的BufferQueue接口对象。  buffer：播放时表示带有音频数据的buffer，录音时表示已存储完录音数据后的空闲buffer。  size：表示buffer的大小。 |
  | SLresult (\*Clear) (SLOHBufferQueueItf self) | 释放BufferQueue接口对象。  self：表示调用该函数的BufferQueue接口对象将被释放。 |
  | SLresult (\*GetState) (SLOHBufferQueueItf self, SLOHBufferQueueState \*state) | 获取BufferQueue接口对象状态。  self：表示调用该函数的BufferQueue接口对象。  state：BufferQueue的当前状态。 |
  | SLresult (\*RegisterCallback) (SLOHBufferQueueItf self, SlOHBufferQueueCallback callback, void\* pContext) | 注册回调函数。  self：表示调用该函数的BufferQueue接口对象。  callback：播放/录音时注册的回调函数。  pContext：播放时传入待播放音频文件，录音时传入将要录制的音频文件。 |
  | SLresult (\*GetBuffer) (SLOHBufferQueueItf self, SLuint8\*\* buffer, SLuint32\* size) | 根据情况获取相应的buffer。  如果是播放操作，则从freeBufferQ\_队列中获取空闲buffer；如果是录音操作，则从filledBufferQ\_队列中获取携带录音数据的buffer。  self：表示调用该函数的BufferQueue接口对象。  buffer：播放时表示空闲的buffer，录音时表示携带录音数据的buffer。  size：表示buffer的大小。 |

## 完整示例

### 在 CMake 脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libOpenSLES.so)
```

参考以下示例代码，播放一个音频文件。

1. 添加头文件。

   ```
   1. #include "SLES/OpenSLES.h"
   2. #include "SLES/OpenSLES_OpenHarmony.h"
   3. #include "SLES/OpenSLES_Platform.h"
   ```
2. 使用slCreateEngine接口和获取engine实例。

   ```
   1. SLObjectItf engineObject = nullptr;
   2. slCreateEngine(&engineObject, 0, nullptr, 0, nullptr, nullptr);
   3. (*engineObject)->Realize(engineObject, SL_BOOLEAN_FALSE);
   ```
3. 获取接口SL\_IID\_ENGINE的engineEngine实例。

   ```
   1. SLEngineItf engineEngine = nullptr;
   2. (*engineObject)->GetInterface(engineObject, SL_IID_ENGINE, &engineEngine);
   ```
4. 配置播放器信息，创建AudioPlayer。

   ```
   1. SLObjectItf outputMixObject = nullptr;
   2. (*engineEngine)->CreateOutputMix(engineEngine, &outputMixObject, 0, nullptr, nullptr);
   3. (*outputMixObject)->Realize(outputMixObject, SL_BOOLEAN_FALSE);
   4. SLDataLocator_BufferQueue slBufferQueue = {
   5. SL_DATALOCATOR_BUFFERQUEUE,
   6. 1
   7. };

   9. // 具体参数需要根据音频文件格式进行适配。
   10. SLDataFormat_PCM pcmFormat = {
   11. SL_DATAFORMAT_PCM,
   12. 2,                           // 通道数。
   13. SL_SAMPLINGRATE_48,          // 采样率。
   14. SL_PCMSAMPLEFORMAT_FIXED_16, // 音频采样格式。
   15. 16,
   16. SL_SPEAKER_FRONT_LEFT | SL_SPEAKER_FRONT_RIGHT,
   17. SL_BYTEORDER_LITTLEENDIAN
   18. };
   19. SLDataSource slSource = {
   20. &slBufferQueue,
   21. &pcmFormat
   22. };
   23. SLDataLocator_OutputMix slOutputMix = {
   24. SL_DATALOCATOR_OUTPUTMIX,
   25. outputMixObject
   26. };
   27. SLDataSink slSink = {
   28. &slOutputMix,
   29. nullptr
   30. };
   31. SLObjectItf pcmPlayerObject = nullptr;
   32. (*engineEngine)->CreateAudioPlayer(engineEngine,
   33. &pcmPlayerObject,
   34. &slSource,
   35. &slSink,
   36. 0,
   37. nullptr,
   38. nullptr);
   39. (*pcmPlayerObject)->Realize(pcmPlayerObject, SL_BOOLEAN_FALSE);
   ```
5. 获取接口SL\_IID\_OH\_BUFFERQUEUE的bufferQueueItf实例。

   ```
   1. SLOHBufferQueueItf bufferQueueItf;
   2. (*pcmPlayerObject)->GetInterface(pcmPlayerObject, SL_IID_OH_BUFFERQUEUE, &bufferQueueItf);
   ```
6. 打开音频文件，注册BufferQueueCallback回调。

   ```
   1. static void BufferQueueCallback (SLOHBufferQueueItf bufferQueueItf, void *pContext, SLuint32 size)
   2. {
   3. SLuint8 *buffer = nullptr;
   4. SLuint32 pSize;
   5. (*bufferQueueItf)->GetBuffer(bufferQueueItf, &buffer, &pSize);
   6. // 将待播放音频数据写入buffer。
   7. (*bufferQueueItf)->Enqueue(bufferQueueItf, buffer, size);
   8. }
   9. void *pContext; // 可传入自定义的上下文信息，会在Callback内收到。
   10. (*bufferQueueItf)->RegisterCallback(bufferQueueItf, BufferQueueCallback, pContext);
   ```
7. 获取接口SL\_PLAYSTATE\_PLAYING的playItf实例，开始播放。

   ```
   1. SLPlayItf playItf = nullptr;
   2. (*pcmPlayerObject)->GetInterface(pcmPlayerObject, SL_IID_PLAY, &playItf);
   3. (*playItf)->SetPlayState(playItf, SL_PLAYSTATE_PLAYING);
   ```
8. 结束音频播放。

   ```
   1. (*playItf)->SetPlayState(playItf, SL_PLAYSTATE_STOPPED);
   2. (*pcmPlayerObject)->Destroy(pcmPlayerObject);
   3. (*engineObject)->Destroy(engineObject);
   ```
