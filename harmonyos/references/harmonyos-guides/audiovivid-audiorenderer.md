---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audiovivid-audiorenderer
title: Audio Vivid播放
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > Audio Vivid能力 > Audio Vivid播放
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:15+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d704cba76e66533452537893e302c47ea67618be2a7d1027f4d72a3a0b3b74f1
---

在获取到解码后的Audio Vivid的PCM数据和元数据之后，可以调用OHAudio的相关播放接口，进行Audio Vivid格式音源的渲染播放。详细的API说明请参考[OHAudio API参考](../harmonyos-references/capi-ohaudio.md)。

## 在CMake脚本中链接到动态库

```screen
target_link_libraries(sample PUBLIC libohaudio.so)
```

## 添加头文件

```
#include <ohaudio/native_audiorenderer.h>
#include <ohaudio/native_audiostreambuilder.h>
```

## 开发步骤

开发者可以通过以下几个步骤来实现一个简单的播放功能。

1. 创建构造器。

   OHAudio提供OH\_AudioStreamBuilder接口，遵循构造器设计模式，用于构建音频流。在Audio Vivid播放场景下，需要选择OH\_AudioStream\_Type为AUDIOSTREAM\_TYPE\_RENDERER，创建一个渲染播放类型的音频构造器。

   ```
   OH_AudioStreamBuilder* builder;
   OH_AudioStreamBuilder_Create(&builder, AUDIOSTREAM_TYPE_RENDERER);
   ```
2. 配置音频流参数。

   创建音频播放构造器后，可以设置音频流所需要的参数，可以参考以下案例。

   Audio Vivid音源搭配系统空间音频渲染算法，播放效果和体验最佳。系统会根据输出音频流的工作场景（OH\_AudioStream\_Usage），选择使用对应的空间音频渲染效果，当前支持的工作场景包括音乐、电影和有声读物。

   ```
   // 设置音频采样率为48000Hz
   OH_AudioStreamBuilder_SetSamplingRate(builder, 48000);
   // 设置音频声道为10 （假定输入Audio Vivid音源是5.1.2声床 + 2对象格式）
   OH_AudioStreamBuilder_SetChannelCount(builder, 10);
   // 设置音频声道布局为5.1.2 （声道布局只考虑声床，若想使用默认声道布局，可以传入 CH_LAYOUT_UNKNOWN 参数）
   OH_AudioStreamBuilder_SetChannelLayout(builder, CH_LAYOUT_5POINT1POINT2);
   // 设置音频采样格式
   OH_AudioStreamBuilder_SetSampleFormat(builder, AUDIOSTREAM_SAMPLE_S16LE);
   // 设置音频流的编码类型为Audio Vivid编码类型
   OH_AudioStreamBuilder_SetEncodingType(builder, AUDIOSTREAM_ENCODING_TYPE_AUDIOVIVID);
   // 设置输出音频流的工作场景，根据实际工作场景选择音乐、电影、有声读物等类型
   OH_AudioStreamBuilder_SetRendererInfo(builder, AUDIOSTREAM_USAGE_MUSIC);
   ```
3. 设置音频回调函数。

   OHAudio使用回调模式进行音频流数据的写入，以及各种音频事件的上报，应用可以按需选择需要监听的音频事件。

   ```
   // 自定义音频流事件函数
   int32_t MyOnStreamEvent(
       OH_AudioRenderer* renderer,
       void* userData,
       OH_AudioStream_Event event)
   {
       // 根据event表示的音频流事件信息，更新播放器状态和界面
       return 0;
   }
   // 自定义音频中断事件函数
   int32_t MyOnInterruptEvent(
       OH_AudioRenderer* renderer,
       void* userData,
       OH_AudioInterrupt_ForceType type,
       OH_AudioInterrupt_Hint hint)
   {
       // 根据type和hint表示的音频中断信息，更新播放器状态和界面
       return 0;
   }
   // 自定义异常回调函数
   int32_t MyOnError(
       OH_AudioRenderer* renderer,
       void* userData,
       OH_AudioStream_Result error)
   {
       // 根据error表示的音频异常信息，做出相应的处理
       return 0;
   }
   // 自定义同时写入PCM数据和元数据函数
   int32_t MyOnWriteDataWithMetadata(
       OH_AudioRenderer* renderer,
       void* userData,
       void* audioData,
       int32_t audioDataSize,
       void* metadata,
       int32_t metadataSize)
   {
       // 将待播放的PCM数据和元数据，分别按audioDataSize和metadataSize写入buffer
       return 0;
   }
   ```

   调用系统的注册监听接口，将上述定义好的回调函数进行配置。

   为了避免不可预期的行为，在设置音频回调函数时，请确认OH\_AudioRenderer\_Callbacks的每一个回调都被自定义的回调方法或空指针初始化。

   对于Audio Vivid播放场景，需要另外使用OH\_AudioRenderer\_WriteDataWithMetadataCallback进行PCM和元数据写入。

   ```
   // 配置回调函数
   OH_AudioRenderer_Callbacks callbacks;
   // Audio Vivid播放时，该回调可以置空，使用元数据回调方式进行数据写入
   callbacks.OH_AudioRenderer_OnWriteData = nullptr;
   // 对音频流事件进行监听，如果不需要，可以使用 nullptr 赋值
   callbacks.OH_AudioRenderer_OnStreamEvent = MyOnStreamEvent;
   // 对音频中断事件进行监听，如果不需要，可以使用 nullptr 赋值
   callbacks.OH_AudioRenderer_OnInterruptEvent = MyOnInterruptEvent;
   // 对音频异常事件进行监听，如果不需要，可以使用 nullptr 赋值
   callbacks.OH_AudioRenderer_OnError = MyOnError;

   //设置输出音频流的回调
   OH_AudioStreamBuilder_SetRendererCallback(builder, callbacks, nullptr);

   // 配置回调函数
   OH_AudioRenderer_WriteDataWithMetadataCallback metadataCallback = MyOnWriteDataWithMetadata;
   // 设置同时写入PCM数据和元数据的回调
   OH_AudioStreamBuilder_SetWriteDataWithMetadataCallback(builder, metadataCallback, nullptr);
   ```
4. 使用配置好的构造器，构造播放音频流。

   ```
   OH_AudioRenderer* audioRenderer;
   OH_AudioStreamBuilder_GenerateRenderer(builder, &audioRenderer);
   ```
5. 使用音频流。

   可以使用以下接口，实现对音频流的控制，完成开始播放、暂停播放、停止播放、清除缓存等基本操作。

   在不再使用该条音频流时，可以释放播放实例，以便更好地管理内存。

   | 接口 | 说明 |
   | --- | --- |
   | OH\_AudioRenderer\_Start | 开始播放 |
   | OH\_AudioRenderer\_Pause | 暂停播放 |
   | OH\_AudioRenderer\_Stop | 停止播放 |
   | OH\_AudioRenderer\_Flush | 释放缓存数据 |
   | OH\_AudioRenderer\_Release | 释放播放实例 |
6. 释放构造器。

   当构造器不再使用时，需要释放相关资源。

   ```
   OH_AudioStreamBuilder_Destroy(builder);
   ```
