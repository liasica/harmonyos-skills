---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdr-vivid-video-recorder
title: HDR Vivid视频录制
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > HDR Vivid能力 > HDR Vivid视频录制
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:365820b712f1f23e45667fc74096d3332eaeda5cdb60e36f08837a65af2d9d8a
---

开发者可以调用本模块的Native API接口，实现在视频录制中支持HDR Vivid标准。

视频录制的主要流程是“相机采集 > 编码 > 封装成mp4文件”。

## HDR Vivid视频编码

应用创建H.265编码器，配置profile(main 10)相机底层包含HDR Vivid的surfacebuffer内容，编码器消费surfacebuffer编码生成对应码流。

说明

仅在Surface模式下支持HDR Vivid视频编码。

### 在 CMake 脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libnative_media_codecbase.so)
2. target_link_libraries(sample PUBLIC libnative_media_avdemuxer.so)
3. target_link_libraries(sample PUBLIC libnative_media_avsource.so)
4. target_link_libraries(sample PUBLIC libnative_media_core.so)
```

说明

上述'sample'字样仅为示例，此处由开发者根据实际工程目录自定义。

### 开发步骤

1. 添加头文件。

   ```
   1. #include <multimedia/player_framework/native_avcodec_videoencoder.h>
   2. #include <multimedia/player_framework/native_avcapability.h>
   3. #include <multimedia/player_framework/native_avcodec_base.h>
   4. #include <multimedia/player_framework/native_avformat.h>
   5. #include <multimedia/player_framework/native_avbuffer.h>
   6. #include <fstream>
   ```
2. 创建编码器实例。

   应用可以通过名称或媒体类型创建编码器。示例中的变量说明如下：

   * videoEnc：视频编码器实例的指针；
   * OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC：HEVC格式视频编解码器。

   ```
   1. // 通过mimetype创建H.265编码器实例。
   2. OH_AVCodec *videoEnc = OH_VideoEncoder_CreateByMime(OH_AVCODEC_MIMETYPE_VIDEO_HEVC);
   ```
3. 配置异步回调函数。

   添加头文件：

   ```
   1. #include <condition_variable>
   2. #include <queue>
   3. #include <mutex>
   ```

   ```
   1. struct CodecBufferInfo {
   2. uint32_t bufferIndex = 0;
   3. OH_AVBuffer *buffer = nullptr;
   4. uint8_t *bufferAddr = nullptr;
   5. OH_AVCodecBufferAttr attr = {0, 0, 0, AVCODEC_BUFFER_FLAGS_NONE};
   6. };
   7. std::mutex outputMutex_;
   8. std::condition_variable outputCond_;
   9. std::queue<CodecBufferInfo> outputBufferInfoQueue_;

   11. // 设置OH_AVCodecOnNewOutputBuffer回调函数，编码完成帧送入输出队列。
   12. void OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData) {
   13. (void)codec;
   14. std::unique_lock<std::mutex> lock(outputMutex_);
   15. outputBufferInfoQueue_.emplace(index, buffer);
   16. outputCond_.notify_all();
   17. }
   ```

   具体可参考：[视频编码Surface模式](video-encoding.md#surface模式)中的“步骤3：调用OH\_VideoEncoder\_RegisterCallback()设置回调函数”。
4. 配置编码器。

   可选配置视频帧宽度、视频帧高度、视频颜色格式。

   ```
   1. // 配置编码Profile为MAIN10（必须）。
   2. int32_t profile = static_cast<int32_t>(HEVC_PROFILE_MAIN_10);
   3. // 配置视频原色。
   4. int32_t primary = static_cast<int32_t>(OH_ColorPrimary::COLOR_PRIMARY_BT2020);
   5. // 配置传输特性。
   6. int32_t transfer = static_cast<int32_t>(OH_TransferCharacteristic::TRANSFER_CHARACTERISTIC_PQ);// PQ或者HLG。
   7. // 配置最大矩阵系数。
   8. int32_t matrix = static_cast<int32_t>(OH_MatrixCoefficient::MATRIX_COEFFICIENT_BT2020_CL);
   9. // 配置关键帧的间隔，单位为毫秒。
   10. int32_t iFrameInterval = 100;

   12. OH_AVFormat *format = OH_AVFormat_Create();
   13. OH_AVFormat_SetIntValue(format, OH_MD_KEY_PROFILE, profile);
   14. OH_AVFormat_SetIntValue(format, OH_MD_KEY_COLOR_PRIMARIES, primary);
   15. OH_AVFormat_SetIntValue(format, OH_MD_KEY_TRANSFER_CHARACTERISTICS, transfer);
   16. OH_AVFormat_SetIntValue(format, OH_MD_KEY_MATRIX_COEFFICIENTS, matrix);
   17. OH_AVFormat_SetIntValue(format, OH_MD_KEY_I_FRAME_INTERVAL, iFrameInterval);
   18. OH_AVFormat_SetIntValue(format, OH_MD_KEY_RANGE_FLAG, 1);
   19. // 配置编码器。
   20. int32_t ret = OH_VideoEncoder_Configure(videoEnc, format);
   21. if (ret != AV_ERR_OK) {
   22. // 异常处理。
   23. }
   24. OH_AVFormat_Destroy(format);
   ```
5. 获取surface，并设置给相机。

   具体可参考：[视频编码Surface模式](video-encoding.md#surface模式)中的“步骤6：获取surface”。
6. 调用OH\_VideoEncoder\_Start()启动编码器。

   具体可参考：[视频编码Surface模式](video-encoding.md#surface模式)中的“步骤8：调用OH\_VideoEncoder\_Start()启动编码器”。

## HDR Vivid视频封装

调用Muxer可以将HDR Vivid码流封装成文件，码流格式需指定为hevc码流，并设置宽、高、isHDRVivid信息。Color信息通常需要从编码获取并设置给封装器。

### 在 CMake 脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libnative_media_avmuxer.so)
2. target_link_libraries(sample PUBLIC libnative_media_core.so)
```

说明

上述'sample'字样仅为示例，此处由开发者根据实际工程目录自定义。

### 开发步骤

1. 添加头文件。

   ```
   1. #include <multimedia/player_framework/native_avmuxer.h>
   2. #include <multimedia/player_framework/native_avcodec_base.h>
   3. #include <multimedia/player_framework/native_avformat.h>
   4. #include <multimedia/player_framework/native_avbuffer.h>
   5. #include <fcntl.h>
   ```
2. 调用OH\_AVMuxer\_Create()创建封装器实例对象。

   ```
   1. // 设置封装格式为mp4。
   2. OH_AVOutputFormat outputFormat = AV_OUTPUT_FORMAT_MPEG_4;
   3. // 以读写方式创建fd。
   4. int32_t fd = open("test.mp4", O_CREAT | O_RDWR | O_TRUNC, S_IRUSR | S_IWUSR);
   5. OH_AVMuxer *muxer = OH_AVMuxer_Create(fd, outputFormat);
   ```
3. 添加视频轨，并指定类型为HDR Vivid类型。

   ```
   1. int videoTrackId = -1;
   2. uint8_t *buffer = ...; // 编码config data，如果没有可以不传。
   3. size_t size = ...;  // 编码config data的长度，根据实际情况配置。

   5. OH_AVFormat *formatVideo = OH_AVFormat_Create();
   6. OH_AVFormat_SetStringValue(formatVideo, OH_MD_KEY_CODEC_MIME, OH_AVCODEC_MIMETYPE_VIDEO_HEVC); // 必填。
   7. OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_WIDTH, 1280); // 必填。
   8. OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_HEIGHT, 720); // 必填。
   9. // (可选)HDR Vivid视频封装时必填，指定为HDR Vivid视频。
   10. OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_VIDEO_IS_HDR_VIVID, 1);
   11. // （可不设置，封装器从编码码流xps自动解析） 设置Color信息，如下。
   12. // 这些信息也可以通过调用OH_VideoEncoder_GetOutputDescription(OH_AVCodec *codec)接口从编码器中获取。
   13. OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_RANGE_FLAG, 1);
   14. OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_COLOR_PRIMARIES, OH_ColorPrimary::COLOR_PRIMARY_BT2020);
   15. OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_TRANSFER_CHARACTERISTICS, OH_TransferCharacteristic::TRANSFER_CHARACTERISTIC_PQ); // PQ或者HLG。
   16. OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_MATRIX_COEFFICIENTS, OH_MatrixCoefficient::MATRIX_COEFFICIENT_BT2020_CL);

   18. ret = OH_AVMuxer_AddTrack(muxer, &videoTrackId, formatVideo);
   19. if (ret != AV_ERR_OK || videoTrackId < 0) {
   20. // 视频轨添加失败。
   21. }
   22. OH_AVFormat_Destroy(formatVideo); // 销毁。
   ```

## 处理视频帧数据

1. 写入封装数据。

   ```
   1. // start后，才能开始写入数据。
   2. int trackId = videoTrackId; // 选择写的媒体轨。
   3. // 取出回调函数OnNewOutputBuffer送入输出队列的帧buffer。
   4. CodecBufferInfo bufferInfo = outputBufferInfoQueue_.front();
   5. outputBufferInfoQueue_.pop();
   6. ret = OH_AVMuxer_WriteSampleBuffer(muxer, trackId, bufferInfo.buffer);
   7. if (ret != AV_ERR_OK) {
   8. // 异常处理。
   9. }
   ```
2. 调用OH\_VideoEncoder\_FreeOutputBuffer()释放编码帧。

   ```
   1. // 释放已完成写入的数据，index为对应输出队列的下标。
   2. ret = OH_VideoEncoder_FreeOutputBuffer(videoEnc, bufferInfo.bufferIndex);
   3. if (ret != AV_ERR_OK) {
   4. // 异常处理。
   5. }
   ```
