---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-ndk-lpp-for-playback
title: 使用LPP播放器播放视频 (C/C++)
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(C/C++) > 播放 > 使用LPP播放器播放视频 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:27+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:b3b487e74f33a214e3b7c50cff841784a78ff7c30657267da1aa074ae2bffb49
---

从API version 20开始，使用LPP（low power player）播放器可以通过低功耗实现从媒体源到渲染的视频通路能力。本指南通过播放本地视频的示例，讲解如何使用LowPowerPlayer播放视频。

说明

LowPowerPlayer播放器不支持纯视频和纯音频播放。纯音频低功耗播放请参考[低功耗音频播放](power-saving-for-playback.md)。

播放流程包含：创建解封装器、创建播放器、设置回调监听函数、配置播放参数、播放控制（播放/暂停/继续/倍速/音量/停止/重置）、销毁播放器实例。

**图1** 播放状态变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/ibcd1bSjQGKT7NLOS23loQ/zh-cn_image_0000002589324969.png?HW-CC-KV=V1&HW-CC-Date=20260429T053526Z&HW-CC-Expire=86400&HW-CC-Sign=603E7F0E59DF42107B649D8E25BF56B0219CBB01E6D277CDEEF02C3671B7F880)

播放流程包含：创建（created）、初始化（initialized）、就绪（ready）、解码（decoding）和渲染（rendering）五个阶段。

应用通过调用CreateByMime初始化创建解码器实例。完成解码器参数配置Configure，切换到initialized（已初始化）状态。

在初始化完成的状态下，完成解码器资源预加载（Prepare），视频进入准备就绪状态（ready）。然后启动解码流程（StartDecode），切换到解码（decoding）状态，触发首帧渲染（RenderFirstFrame）。最后启动渲染（StartRender）流程，切换到渲染（rendering）状态。

在渲染过程中，遇到暂停（Pause）会切换到paused状态，此时解码与渲染被临时挂起，资源未释放。当恢复渲染（Resume）时，视频将恢复并回到渲染（rendering）状态。当遇到停止（Stop）时，会切换到stopped状态，该状态代表解码器已停止工作，但实例仍存在。当渲染过程中流结束（EoS）时，会切换到eos状态。

在播放过程中，如果遇到错误（OnError），会出现异常，需要重置或进入释放阶段（released）销毁解码器实例，释放所有资源。

当播放处于ready/decoding/rendering/paused/stopped状态时，播放引擎此时处于工作状态会占用较多的系统资源。当暂停使用播放器时，可调用reset或destroy回收资源。

## 开发建议

当前指导仅介绍如何实现媒体资源播放，在应用开发过程中会涉及后台播放、播放冲突等情况，请根据实际需要参考以下说明。

* 由于硬件差异，LPP播放器能力仅在部分手机上支持。从API version 21开始，建议通过[OH\_LowPowerAVSink\_GetCapability](../harmonyos-references/capi-lowpower-avsink-base-h.md#oh_lowpoweravsink_getcapability)查询LPP播放器能力是否支持。如果不支持，使用[AVCodec](avcodec-kit-intro.md)能力实现播放。
* 当应用在播放过程中时，播放的媒体数据涉及音频，根据系统音频管理策略（参考[处理音频焦点变化](audio-playback-concurrency.md#处理音频焦点变化)事件）可知这会被其他应用打断，建议通过[OH\_LowPowerAudioSinkCallback\_SetInterruptListener](../harmonyos-references/capi-lowpower-audio-sink-h.md#oh_lowpoweraudiosinkcallback_setinterruptlistener)主动监听音频打断事件，根据其回调参数提示做出相应的处理，避免出现应用状态与预期效果不一致的问题。
* 当设备同时连接多个音频输出设备时，建议通过[OH\_LowPowerAudioSinkCallback\_SetDeviceChangeListener](../harmonyos-references/capi-lowpower-audio-sink-h.md#oh_lowpoweraudiosinkcallback_setdevicechangelistener)主动监听音频输出设备改变事件，并做出相应处理。
* 当应用在执行过程中，可能出现系统内部异常。如网络异常、内存不足、媒体服务死亡不可用等，建议通过 [OH\_LowPowerAudioSinkCallback\_SetErrorListener](../harmonyos-references/capi-lowpower-audio-sink-h.md#oh_lowpoweraudiosinkcallback_seterrorlistener)或[OH\_LowPowerVideoSinkCallback\_SetErrorListener](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosinkcallback_seterrorlistener)对应接口设置错误监听回调函数，根据不同错误类型和错误信息，做出相应处理，避免出现播放异常。
* 在播放过程中，播放器需要的数据要通过 [OH\_AVDemuxer\_ReadSampleBuffer](../harmonyos-references/capi-native-avdemuxer-h.md#oh_avdemuxer_readsamplebuffer)接口获取指定轨道的buffer，并通过 [OH\_AVSamplesBuffer\_AppendOneBuffer](../harmonyos-references/capi-lowpower-avsink-base-h.md#oh_avsamplesbuffer_appendonebuffer)进行多个buffer的封装，然后再通过 [OH\_LowPowerAudioSink\_ReturnSamples](../harmonyos-references/capi-lowpower-audio-sink-h.md#oh_lowpoweraudiosink_returnsamples)或[OH\_LowPowerVideoSink\_ReturnSamples](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosink_returnsamples)通知播放器进行消费，当播放器需要数据时，会触发通过 [OH\_LowPowerAudioSinkCallback\_SetDataNeededListener](../harmonyos-references/capi-lowpower-audio-sink-h.md#oh_lowpoweraudiosinkcallback_setdataneededlistener)或[OH\_LowPowerVideoSinkCallback\_SetDataNeededListener](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosinkcallback_setdataneededlistener)接口注册的回调函数。
* 需要注意函数的调用时机。根据状态示意图和详细的接口文档进行合理调用。在程序执行完成后，调用OH\_\*\*\*\_Create方法的同时必须调用对应的OH\_\*\*\*\_Destroy方法，进行资源释放。
* 用户在注册回调函数时，可在最后一个参数void \*userData中来配置自定义数据，以便在回调函数中执行某些设置（如状态改变等）。

  其他回调函数：

  [OH\_LowPowerAudioSinkCallback\_SetPositionUpdateListener](../harmonyos-references/capi-lowpower-audio-sink-h.md#oh_lowpoweraudiosinkcallback_setpositionupdatelistener)：可获取播放进度。

  [OH\_LowPowerAudioSinkCallback\_SetEosListener](../harmonyos-references/capi-lowpower-audio-sink-h.md#oh_lowpoweraudiosinkcallback_seteoslistener)或[OH\_LowPowerVideoSinkCallback\_SetEosListener](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosinkcallback_seteoslistener)：播放结束触发。

  [OH\_LowPowerVideoSinkCallback\_SetRenderStartListener](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosinkcallback_setrenderstartlistener)：视频开始渲染。

  [OH\_LowPowerVideoSink\_SetTargetStartFrame](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosink_settargetstartframe)：到达目标帧。

  [OH\_LowPowerVideoSinkCallback\_SetStreamChangedListener](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosinkcallback_setstreamchangedlistener)：视频流切换。

  [OH\_LowPowerVideoSinkCallback\_SetFirstFrameDecodedListener](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosinkcallback_setfirstframedecodedlistener)：首帧视频渲染完毕。

## 开发步骤及注意事项

在CMake脚本中链接动态库。

```
1. target_link_libraries(sample PUBLIC liblowpower_avsink.so)
```

头文件引入。

```
1. #include "multimedia/player_framework/lowpower_audio_sink_base.h"
2. #include "multimedia/player_framework/lowpower_audio_sink.h"
3. #include "multimedia/player_framework/lowpower_video_sink.h"
4. #include "multimedia/player_framework/lowpower_video_sink_base.h"
```

开发者使用系统日志能力时，需引入如下头文件：

```
1. #include <hilog/log.h>
```

并需要在CMake脚本中链接如下动态库：

```
1. target_link_libraries(sample PUBLIC libhilog_ndk.z.so)
```

使用该模块时，需要链接的库如下所示：解封装、基础解码、显示渲染等能力。

```
1. set(BASE_LIBRARY
2. libnative_media_codecbase.so libnative_media_core.so libnative_media_vdec.so libnative_window.so
3. libnative_media_venc.so libnative_media_acodec.so libnative_media_avdemuxer.so libnative_media_avsource.so
4. libohaudio.so
5. )
6. target_link_libraries(sample PUBLIC ${BASE_LIBRARY})
```

开发者通过引入[lowpower\_audio\_sink\_base.h](../harmonyos-references/capi-lowpower-audio-sink-base-h.md)、[lowpower\_audio\_sink.h](../harmonyos-references/capi-lowpower-audio-sink-h.md)、[lowpower\_video\_sink.h](../harmonyos-references/capi-lowpower-video-sink-h.md)、 [lowpower\_video\_sink\_base.h](../harmonyos-references/capi-lowpower-video-sink-base-h.md) 头文件，使用音视频播放相关API。

1. 创建播放器。

   根据实际情况，应用可使用自研解封装或可通过[OH\_AVSource\_CreateWithDataSource()](../harmonyos-references/capi-native-avsource-h.md#oh_avsource_createwithdatasource)/[OH\_AVSource\_CreateWithFD()](../harmonyos-references/capi-native-avsource-h.md#oh_avsource_createwithfd)/[OH\_AVSource\_CreateWithURI()](../harmonyos-references/capi-native-avsource-h.md#oh_avsource_createwithuri)来创建[OH\_AVSource](../harmonyos-references/capi-avsource-oh-avsource.md) ，通过OH\_AVSource调用[OH\_AVDemuxer\_CreateWithSource()](../harmonyos-references/capi-native-avdemuxer-h.md#oh_avdemuxer_createwithsource)，创建解封装器，获取视频的元信息。

   ```
   1. source_ = OH_AVSource_CreateWithFD(info.inputFd, info.inputFileOffset, info.inputFileSize);
   2. demuxer_ = OH_AVDemuxer_CreateWithSource(source_);
   3. int32_t ret = GetTrackInfo(sourceFormat, info);
   ```
2. 根据视频元信息，调用 [OH\_LowPowerAudioSink\_CreateByMime](../harmonyos-references/capi-lowpower-audio-sink-h.md#oh_lowpoweraudiosink_createbymime)或[OH\_LowPowerVideoSink\_CreateByMime](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosink_createbymime)来创建播放器。

   ```
   1. lppVideoStreamer_ = OH_LowPowerVideoSink_CreateByMime(codecMime.c_str());
   2. lppAudioStreamer_ = OH_LowPowerAudioSink_CreateByMime(codecMime.c_str());
   ```
3. 设置回调监听函数。

   调用[OH\_LowPowerAudioSinkCallback\_Create](../harmonyos-references/capi-lowpower-audio-sink-h.md#oh_lowpoweraudiosinkcallback_create)或[OH\_LowPowerVideoSinkCallback\_Create](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosinkcallback_create)创建[OH\_LowPowerAudioSinkCallback](../harmonyos-references/api-lowpoweraudiosink-oh-lowpoweraudiosinkcallback.md)或[OH\_LowPowerVideoSinkCallback](../harmonyos-references/api-lowpowervideosink-oh-lowpowervideosinkcallback.md)的回调函数的整合，通过setListener函数向该结构体添加对应的回调函数，完成registerCallback的一次性注册。

   ```
   1. lppAudioStreamerCallback_ = OH_LowPowerAudioSinkCallback_Create();
   2. OH_LowPowerAudioSinkCallback_SetDataNeededListener(lppAudioStreamerCallback_, LppCallback::OnDataNeeded, lppUserData);
   3. OH_LowPowerAudioSinkCallback_SetPositionUpdateListener(lppAudioStreamerCallback_, LppCallback::OnPositionUpdated, lppUserData);
   4. ret = OH_LowPowerAudioSink_RegisterCallback(lppAudioStreamer_, lppAudioStreamerCallback_);
   ```
4. 配置播放器。

   根据之前通过解封装获得的元信息，创建并配置[OH\_AVFormat](../harmonyos-references/capi-core-oh-avformat.md)。通过configure接口 [OH\_LowPowerAudioSink\_Configure](../harmonyos-references/capi-lowpower-audio-sink-h.md#oh_lowpoweraudiosink_configure) / [OH\_LowPowerVideoSink\_Configure](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosink_configure)进行播放器的配置，详细参数可参考示例代码。视频流需要使用[OH\_LowPowerVideoSink\_SetVideoSurface](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosink_setvideosurface)接口来设置显示窗口。

   ```
   1. OH_AVFormat *format = OH_AVFormat_Create();

   3. OH_AVFormat_SetIntValue(format, OH_MD_KEY_WIDTH, sampleInfo.videoWidth);
   4. OH_AVFormat_SetIntValue(format, OH_MD_KEY_HEIGHT, sampleInfo.videoHeight);
   5. OH_AVFormat_SetDoubleValue(format, OH_MD_KEY_FRAME_RATE, sampleInfo.frameRate);
   6. OH_AVFormat_SetIntValue(format, OH_MD_KEY_PIXEL_FORMAT, sampleInfo.pixelFormat);
   7. OH_AVFormat_SetIntValue(format, OH_MD_KEY_ROTATION, sampleInfo.rotation);

   9. int ret = OH_LowPowerVideoSink_Configure(lppVideoStreamer_, format);
   ```
5. 准备播放。

   准备播放前，需要调用[OH\_LowPowerVideoSink\_SetSyncAudioSink](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosink_setsyncaudiosink)设置音画同步绑定。然后调用prepare方法，[OH\_LowPowerAudioSink\_Prepare](../harmonyos-references/capi-lowpower-audio-sink-h.md#oh_lowpoweraudiosink_prepare)或[OH\_LowPowerVideoSink\_Prepare](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosink_prepare)进入'准备'阶段。

   ```
   1. OH_LowPowerVideoSink_Prepare(lppVideoStreamer_);
   ```
6. 开始播放。

   调用[OH\_LowPowerAudioSink\_Start](../harmonyos-references/capi-lowpower-audio-sink-h.md#oh_lowpoweraudiosink_start)或[OH\_LowPowerVideoSink\_StartRenderer](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosink_startrenderer)开始渲染。视频流需要在渲染开始前调用[OH\_LowPowerVideoSink\_StartDecoder](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosink_startdecoder)开始解码或调用 [OH\_LowPowerVideoSink\_RenderFirstFrame](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosink_renderfirstframe)开始解码并送显首帧'接口'进入解码。

   ```
   1. OH_LowPowerVideoSink_StartDecoder(lppVideoStreamer_);
   2. OH_LowPowerVideoSink_StartRenderer(lppVideoStreamer_);
   ```
7. 播放控制（可选）。

   暂停：[OH\_LowPowerAudioSink\_Pause](../harmonyos-references/capi-lowpower-audio-sink-h.md#oh_lowpoweraudiosink_pause)或 [OH\_LowPowerVideoSink\_Pause](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosink_pause)

   恢复播放：[OH\_LowPowerAudioSink\_Resume](../harmonyos-references/capi-lowpower-audio-sink-h.md#oh_lowpoweraudiosink_resume)或 [OH\_LowPowerVideoSink\_Resume](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosink_resume)

   停止：[OH\_LowPowerAudioSink\_Stop](../harmonyos-references/capi-lowpower-audio-sink-h.md#oh_lowpoweraudiosink_stop)或[OH\_LowPowerVideoSink\_Stop](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosink_stop)

   设置声音：[OH\_LowPowerAudioSink\_SetVolume](../harmonyos-references/capi-lowpower-audio-sink-h.md#oh_lowpoweraudiosink_setvolume)

   设置播放速度：[OH\_LowPowerAudioSink\_SetPlaybackSpeed](../harmonyos-references/capi-lowpower-audio-sink-h.md#oh_lowpoweraudiosink_setplaybackspeed)或[OH\_LowPowerVideoSink\_SetPlaybackSpeed](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosink_setplaybackspeed)

   清空缓存数据，可用于seek操作：[OH\_LowPowerAudioSink\_Flush](../harmonyos-references/capi-lowpower-audio-sink-h.md#oh_lowpoweraudiosink_flush)或[OH\_LowPowerVideoSink\_Flush](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosink_flush)
8. 更换资源（可选）。

   调用[OH\_LowPowerAudioSink\_Reset](../harmonyos-references/capi-lowpower-audio-sink-h.md#oh_lowpoweraudiosink_reset)或[OH\_LowPowerVideoSink\_Reset](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosink_reset)重置资源，允许更换资源，重新配置播放器。
9. 退出播放。

   调用[OH\_LowPowerAudioSink\_Destroy](../harmonyos-references/capi-lowpower-audio-sink-h.md#oh_lowpoweraudiosink_destroy)或[OH\_LowPowerVideoSink\_Destroy](../harmonyos-references/capi-lowpower-video-sink-h.md#oh_lowpowervideosink_destroy)销毁实例，AVPlayer进入'RELEASED'状态，退出播放。

## 运行完整示例

1. 新建工程。下载[示例工程](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/MediaKit/LowPowerAVSInk/lowPowerAVSinkSample)，并将示例工程的以下资源复制到对应目录。

   ```
   1. lpp_demo-sample/entry/src/main/
   2. ├── cpp                                # Native层
   3. │   ├── capabilities                   # 能力接口和实现
   4. │   │   ├── include                    # 能力接口
   5. │   │   ├── demuxer.cpp                # 解封装实现
   6. │   │   ├── lpp_audio_streamer.cpp     # 低功耗音频流实现
   7. │   │   └── lpp_video_streamer.cpp     # 低功耗视频流实现
   8. │   ├── common                         # 公共模块
   9. │   │   ├── dfx                        # 日志
   10. │   │   ├── lpp_callback.cpp           # 低功耗音视频回调实现
   11. │   │   ├── lpp_callback.h             # 低功耗音视频回调接口
   12. │   │   └── sample_info.h              # 功能实现公共类
   13. │   ├── render                         # 送显模块接口和实现 * window player设置
   14. │   │   ├── include                    # 送显模块接口
   15. │   │   ├── egl_core.cpp               # 送显参数设置
   16. │   │   ├── plugin_manager.cpp         # 送显模块管理实现
   17. │   │   └── plugin_render.cpp          # 送显逻辑实现
   18. │   ├── sample                         # Native层
   19. │   │   ├── player                     # Native层播放接口和实现
   20. │   │   │   ├── Player.cpp             # Native层播放功能调用逻辑的实现
   21. │   │   │   ├── Player.h               # Native层播放功能调用逻辑的接口
   22. │   │   │   ├── PlayerNative.cpp       # Native层播放的入口
   23. │   │   │   └── PlayerNative.h         # Native层暴露上来的接口
   24. │   ├── types                          #
   25. │   │   └── libplayer                  # 播放模块暴露给UI层的接口
   26. │   └── CMakeLists.txt                 # 编译入口
   27. ├── ets                                # UI层
   28. │   ├── common                         # 公共模块
   29. │   │   ├── utils                      # 共用的工具类
   30. │   │   │   ├── DateTimeUtils.ets      # 获取当前时间
   31. │   │   │   └── Logger.ts              # 日志工具
   32. │   |   └───CommonConstants.ets        # 参数常量
   33. │   ├── entryability                   # 应用的入口
   34. │   │   └── EntryAbility.ts            # 申请权限弹窗实现
   35. │   ├── pages                          # EntryAbility包含的页面
   36. │   │   └── Index.ets                  # 首页/播放页面
   37. ├── resources                          # 用于存放应用所用到的资源文件
   38. │   ├── base                           # 该目录下的资源文件会被赋予唯一的ID
   39. │   │   ├── element                    # 用于存放字体和颜色
   40. │   │   ├── media                      # 用于存放图片
   41. │   │   └── profile                    # 应用入口首页
   42. │   ├── en_US                          # 设备语言是美式英文时，优先匹配此目录下资源
   43. │   └── zh_CN                          # 设备语言是简体中文时，优先匹配此目录下资源
   44. └── module.json5                       # 模块配置信息
   ```
2. 编译新建工程并运行。
