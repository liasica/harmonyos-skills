---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audiovivid-audiorenderer
title: Audio Vivid播放
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > Audio Vivid能力 > Audio Vivid播放
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:46+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:144f041f559b14aab82de6789b523e692d8ac3a719814803f8ff14e90c89e965
---

在获取到解码后的Audio Vivid的PCM数据和元数据之后，可以调用OHAudio的相关播放接口，进行Audio Vivid格式音源的渲染播放。详细的API说明请参考[OHAudio API参考](../harmonyos-references/capi-ohaudio.md)。

## 在CMake脚本中链接到动态库

```
1. target_link_libraries(sample PUBLIC libohaudio.so)
```

## 添加头文件

```
1. #include <ohaudio/native_audiorenderer.h>
2. #include <ohaudio/native_audiostreambuilder.h>
```

## 开发步骤

开发者可以通过以下几个步骤来实现一个简单的播放功能。

1. 创建构造器。

   OHAudio提供OH\_AudioStreamBuilder接口，遵循构造器设计模式，用于构建音频流。在Audio Vivid播放场景下，需要选择OH\_AudioStream\_Type为AUDIOSTREAM\_TYPE\_RENDERER，创建一个渲染播放类型的音频构造器。

   ```
   1. OH_AudioStreamBuilder* builder;
   2. OH_AudioStreamBuilder_Create(&builder, AUDIOSTREAM_TYPE_RENDERER);
   ```
2. 配置音频流参数。

   创建音频播放构造器后，可以设置音频流所需要的参数，可以参考以下案例。

   Audio Vivid音源搭配系统空间音频渲染算法，播放效果和体验最佳。系统会根据输出音频流的工作场景（OH\_AudioStream\_Usage），选择使用对应的空间音频渲染效果，当前支持的工作场景包括音乐、电影和有声读物。

   ```
   1. // 设置音频采样率为48000Hz
   2. OH_AudioStreamBuilder_SetSamplingRate(builder, 48000);
   3. // 设置音频声道为10 （假定输入Audio Vivid音源是5.1.2声床 + 2对象格式）
   4. OH_AudioStreamBuilder_SetChannelCount(builder, 10);
   5. // 设置音频声道布局为5.1.2 （声道布局只考虑声床，若想使用默认声道布局，可以传入 CH_LAYOUT_UNKNOWN 参数）
   6. OH_AudioStreamBuilder_SetChannelLayout(builder, CH_LAYOUT_5POINT1POINT2);
   7. // 设置音频采样格式
   8. OH_AudioStreamBuilder_SetSampleFormat(builder, AUDIOSTREAM_SAMPLE_S16LE);
   9. // 设置音频流的编码类型为Audio Vivid编码类型
   10. OH_AudioStreamBuilder_SetEncodingType(builder, AUDIOSTREAM_ENCODING_TYPE_AUDIOVIVID);
   11. // 设置输出音频流的工作场景，根据实际工作场景选择音乐、电影、有声读物等类型
   12. OH_AudioStreamBuilder_SetRendererInfo(builder, AUDIOSTREAM_USAGE_MUSIC);
   ```
3. 设置音频回调函数。

   OHAudio使用回调模式进行音频流数据的写入，以及各种音频事件的上报，应用可以按需选择需要监听的音频事件。

   ```
   1. // 自定义音频流事件函数
   2. int32_t MyOnStreamEvent(
   3. OH_AudioRenderer* renderer,
   4. void* userData,
   5. OH_AudioStream_Event event)
   6. {
   7. // 根据event表示的音频流事件信息，更新播放器状态和界面
   8. return 0;
   9. }
   10. // 自定义音频中断事件函数
   11. int32_t MyOnInterruptEvent(
   12. OH_AudioRenderer* renderer,
   13. void* userData,
   14. OH_AudioInterrupt_ForceType type,
   15. OH_AudioInterrupt_Hint hint)
   16. {
   17. // 根据type和hint表示的音频中断信息，更新播放器状态和界面
   18. return 0;
   19. }
   20. // 自定义异常回调函数
   21. int32_t MyOnError(
   22. OH_AudioRenderer* renderer,
   23. void* userData,
   24. OH_AudioStream_Result error)
   25. {
   26. // 根据error表示的音频异常信息，做出相应的处理
   27. return 0;
   28. }
   29. // 自定义同时写入PCM数据和元数据函数
   30. int32_t MyOnWriteDataWithMetadata(
   31. OH_AudioRenderer* renderer,
   32. void* userData,
   33. void* audioData,
   34. int32_t audioDataSize,
   35. void* metadata,
   36. int32_t metadataSize)
   37. {
   38. // 将待播放的PCM数据和元数据，分别按audioDataSize和metadataSize写入buffer
   39. return 0;
   40. }
   ```

   调用系统的注册监听接口，将上述定义好的回调函数进行配置。

   为了避免不可预期的行为，在设置音频回调函数时，请确认OH\_AudioRenderer\_Callbacks的每一个回调都被自定义的回调方法或空指针初始化。

   对于Audio Vivid播放场景，需要另外使用OH\_AudioRenderer\_WriteDataWithMetadataCallback进行PCM和元数据写入。

   ```
   1. // 配置回调函数
   2. OH_AudioRenderer_Callbacks callbacks;
   3. // Audio Vivid播放时，该回调可以置空，使用元数据回调方式进行数据写入
   4. callbacks.OH_AudioRenderer_OnWriteData = nullptr;
   5. // 对音频流事件进行监听，如果不需要，可以使用 nullptr 赋值
   6. callbacks.OH_AudioRenderer_OnStreamEvent = MyOnStreamEvent;
   7. // 对音频中断事件进行监听，如果不需要，可以使用 nullptr 赋值
   8. callbacks.OH_AudioRenderer_OnInterruptEvent = MyOnInterruptEvent;
   9. // 对音频异常事件进行监听，如果不需要，可以使用 nullptr 赋值
   10. callbacks.OH_AudioRenderer_OnError = MyOnError;

   12. //设置输出音频流的回调
   13. OH_AudioStreamBuilder_SetRendererCallback(builder, callbacks, nullptr);

   15. // 配置回调函数
   16. OH_AudioRenderer_WriteDataWithMetadataCallback metadataCallback = MyOnWriteDataWithMetadata;
   17. // 设置同时写入PCM数据和元数据的回调
   18. OH_AudioStreamBuilder_SetWriteDataWithMetadataCallback(builder, metadataCallback, nullptr);
   ```
4. 使用配置好的构造器，构造播放音频流。

   ```
   1. OH_AudioRenderer* audioRenderer;
   2. OH_AudioStreamBuilder_GenerateRenderer(builder, &audioRenderer);
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
   1. OH_AudioStreamBuilder_Destroy(builder);
   ```
