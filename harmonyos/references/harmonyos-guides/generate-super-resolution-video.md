---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/generate-super-resolution-video
title: 视频缩放
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(C/C++) > 视频处理 > 视频缩放
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9ce6242abdaa7c44f67ffa4b31314ab544a73be773a24d419c9c61907853283c
---

本模块提供视频细节增强的[C API接口](../harmonyos-references/capi-videoprocessing.md)，通过调用本模块的接口，可以实现视频流图像内容的清晰度增强及缩放功能，处理后的数据可以用于送显、播放和录制。

典型应用场景如：视频解码 > 视频细节增强 > XComponent显示。

## 约束与限制

1. 为保证处理能够实时响应，建议只创建一个实例。
2. 当前仅支持处理同时满足以下条件的视频：

   * 视频为SDR（Standard dynamic range）视频。
   * 视频的像素格式为NV12、NV21，输出格式与输入格式一致。
3. 本模块提供4个档位的算法，处理效果逐渐变优，但性能也会逐渐下降。

   | 档位 | 输入分辨率要求（单位：像素） | 输出分辨率要求（单位：像素） | 说明 |
   | --- | --- | --- | --- |
   | NONE | 宽：(32,2000]  高：(32,2000] | 宽：(32,2000]  高：(32,2000] | 仅适用于缩放场景，无清晰度增强效果。 |
   | LOW | 宽：(32,2000]  高：(32,2000] | 宽：(32,2000]  高：(32,2000] | 仅适用于缩放场景，等比缩放时无清晰度增强效果。  缩放时会对图像进行低质量的清晰度增强，处理速度较快。  该档位为默认设置。 |
   | MEDIUM | 宽：(32,2000]  高：(32,2000] | 宽：(32,2000]  高：(32,2000] | 仅适用于缩放场景，等比缩放时无清晰度增强效果。  缩放时会对图像进行中等质量的清晰度增强，处理速度适中。 |
   | HIGH | 宽：[512,2000]  高：[512,2000] | 宽：[512,2000]  高：[512,2000] | 适用于缩放及清晰度增强场景，等比缩放时能进行清晰度增强。  缩放时会对图像进行高质量的清晰度增强，处理速度相对较慢。 |
4. 不允许在视频处理回调函数中，直接调用视频处理相关接口或其他耗时操作，请在应用自己的线程中调用。

## 开发指导

具体实现可参考[示例工程](https://gitcode.com/HarmonyOS_Samples/VideoProcessing)。

### 在 CMake 脚本中链接动态库

```screen
target_link_libraries(sample PUBLIC libvideo_processing.so)
```

### 开发步骤

1. 添加头文件。

   ```cpp
   #include <ace/xcomponent/native_interface_xcomponent.h>
   #include <multimedia/player_framework/native_avformat.h>
   #include <multimedia/video_processing_engine/video_processing.h>
   #include <multimedia/video_processing_engine/video_processing_types.h>
   #include <native_window/external_window.h>
   #include <native_buffer/native_buffer.h>
   ```
2. （可选）创建解码实例。

   细节增强模块的输入可以是来自系统解码的视频流，也可以由应用自行往window填充视频数据（例如：应用内部软解后直接将数据填充到window中）。若选择系统解码器对视频文件或视频流媒体进行处理，则可以创建解码实例来作为细节增强模块的输入。

   ```cpp
   // 创建Demuxer（媒体多路分解器）解析音视频信息(详见代码示例)
   OH_AVSource* source_ = OH_AVSource_CreateWithFD(inputFd, inputFileOffset, inputFileSize);
   OH_AVDemuxer* demuxer_ = OH_AVDemuxer_CreateWithSource(source_);
   auto sourceFormat = std::shared_ptr<OH_AVFormat>(OH_AVSource_GetSourceFormat(source_), OH_AVFormat_Destroy);
   // 创建视频解码器
   OH_AVCodec * decoder_ = OH_VideoDecoder_CreateByMime(videoCodecMime.c_str());
   // 配置视频信息
   OH_AVFormat *format = OH_AVFormat_Create();
   OH_AVFormat_SetIntValue(format, OH_MD_KEY_WIDTH, videoWidth);
   OH_AVFormat_SetIntValue(format, OH_MD_KEY_HEIGHT, videoHeight);
   OH_AVFormat_SetDoubleValue(format, OH_MD_KEY_FRAME_RATE, frameRate);
   OH_AVFormat_SetIntValue(format, OH_MD_KEY_PIXEL_FORMAT, pixelFormat);
   OH_AVFormat_SetIntValue(format, OH_MD_KEY_ROTATION, rotation);
   int ret = OH_VideoDecoder_Configure(decoder_, format);
   OH_AVFormat_Destroy(format);
   // 配置回调，维护视频解码器buffer队列（详见代码示例）
   OH_VideoDecoder_RegisterCallback(decoder_,
           {SampleCallback::OnCodecError, SampleCallback::OnCodecFormatChange,
            SampleCallback::OnNeedInputBuffer, SampleCallback::OnNewOutputBuffer}, videoDecContext_);
   // 准备视频解码器
   int ret = OH_VideoDecoder_Prepare(decoder_);
   // 创建解码上下文
   videoDecContext_ = new CodecUserData;
   ```
3. （可选）初始化环境。

   一般在进程内第一次使用时调用，可提前完成部分耗时操作。

   ```cpp
   VideoProcessing_ErrorCode ret = OH_VideoProcessing_InitializeEnvironment();
   ```
4. 创建细节增强模块。

   应用可以通过视频处理引擎模块类型来创建细节增强模块。示例中的变量说明如下：

   * videoProcessor：细节增强模块实例。
   * VIDEO\_PROCESSING\_TYPE\_DETAIL\_ENHANCER：细节增强类型。
   * 预期返回值：VIDEO\_PROCESSING\_SUCCESS

   ```cpp
   // 通过指定视频处理引擎类型创建细节增强模块实例
   VideoProcessing_ErrorCode ret = OH_VideoProcessing_Create(&videoProcessor, VIDEO_PROCESSING_TYPE_DETAIL_ENHANCER);
   ```
5. 配置异步回调函数。

   ```cpp
   // 创建回调实例
   ret = OH_VideoProcessingCallback_Create(&callback);
   // 绑定回调函数
   OH_VideoProcessingCallback_BindOnError(callback, OnError);
   OH_VideoProcessingCallback_BindOnState(callback, OnState);
   OH_VideoProcessingCallback_BindOnNewOutputBuffer(callback, OnNewOutputBuffer);
   // 注册回调函数
   ret = OH_VideoProcessing_RegisterCallback(videoProcessor, callback, this);
   // 回调函数声明（其中userData会传递注册回调时传入的用户数据，如：this指针）
   void OnError(OH_VideoProcessing* videoProcessor, VideoProcessing_ErrorCode error, void* userData);
   void OnState(OH_VideoProcessing* videoProcessor, VideoProcessing_State state, void* userData);
   void OnNewOutputBuffer(OH_VideoProcessing* videoProcessor, uint32_t index, void* userData);
   ```
6. （可选）配置细节增强档位，当前有高中低三档及NONE可选，若不配置则默认档位为LOW档。

   ```cpp
   // 创建format实例
   OH_AVFormat* parameter = OH_AVFormat_Create();
   // 指定档位
   OH_AVFormat_SetIntValue(parameter, VIDEO_DETAIL_ENHANCER_PARAMETER_KEY_QUALITY_LEVEL, VIDEO_DETAIL_ENHANCER_QUALITY_LEVEL_HIGH);
   // 配置参数
   OH_VideoProcessing_SetParameter(videoProcessor, parameter);
   ```
7. 获取Surface。

   ```cpp
   //配置算法的输入
   ret = OH_VideoProcessing_GetSurface(videoProcessor, inputWindow);
   // 将解码器的输出与算法的输入进行绑定，解码器输出的window分辨率即为算法输入分辨率
   OH_VideoDecoder_SetSurface(decoder_,  inputWindow_);
   ```
8. 设置Surface（配置送显）。

   ```cpp
   // 配置算法的输出，配置的输出window的分辨率即为算法输出分辨率
   ret = OH_VideoProcessing_SetSurface(videoProcessor, outWindow);
   ```
9. 创建解码器输入输出线程。

   ```cpp
   std::unique_ptr<std::thread> videoDecInputThread_ = std::make_unique<std::thread>(&Player::VideoDecInputThread, this);
   std::unique_ptr<std::thread> videoDecOutputThread_ = std::make_unique<std::thread>(&Player::VideoDecOutputThread, this);
   ```
10. 启动细节增强处理。

    ```cpp
    // 启动解码
    int ret = OH_VideoDecoder_Start(decoder_);
    // 启动细节增强处理
    ret = OH_VideoProcessing_Start(videoProcessor);
    ```
11. 调用[OH\_VideoProcessing\_Stop()](../harmonyos-references/capi-video-processing-h.md#oh_videoprocessing_stop)停止细节增强。

    ```cpp
    VideoProcessing_ErrorCode ret = OH_VideoProcessing_Stop(videoProcessor);
    ```
12. 释放处理实例。

    ```cpp
    VideoProcessing_ErrorCode ret = OH_VideoProcessing_Destroy(videoProcessor)；
    videoProcessor = nullptr;
    VideoProcessing_ErrorCode ret = OH_VideoProcessingCallback_Destroy(callback);
    callback = nullptr;
    ```
13. 释放处理资源。

    ```cpp
    VideoProcessing_ErrorCode ret = OH_VideoProcessing_DeinitializeEnvironment();
    ```
