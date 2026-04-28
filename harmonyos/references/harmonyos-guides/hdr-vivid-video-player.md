---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdr-vivid-video-player
title: HDR Vivid视频播放
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > HDR Vivid能力 > HDR Vivid视频播放
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e3b7762c745ecfe34dd92ae0290b09988a6720859f66745cd647bd5e832d6db0
---

开发者可以调用本模块的Native API接口，实现在视频播放中支持HDR Vivid标准。

视频播放的主要流程，是将视频文件“解封装 > 解码 > 送显/播放”。

## HDR Vivid视频解析

从视频文件中，可以解析出其是否为HDR Vivid视频，如果视频源为HDR Vivid视频，可以解析相关的信息，如元数据、颜色信息（Color）等。

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
   1. #include <multimedia/player_framework/native_avdemuxer.h>
   2. #include <multimedia/player_framework/native_avsource.h>
   3. #include <multimedia/player_framework/native_avcodec_base.h>
   4. #include <multimedia/player_framework/native_avformat.h>
   5. #include <multimedia/player_framework/native_avbuffer.h>
   6. #include <fcntl.h>
   7. #include <sys/stat.h>
   8. #include <string>
   ```
2. 文件解析器。

   ```
   1. // 创建文件操作符 fd，打开时对文件实例必须有读权限（filePath 为待解封装文件路径，需预置文件，保证路径指向的文件存在）。
   2. std::string filePath = "test.mp4";
   3. int fd = open(filePath.c_str(), O_RDONLY);
   4. struct stat fileStatus {};
   5. // 获取fileSize。
   6. size_t fileSize = 0;
   7. if (stat(filePath.c_str(), &fileStatus) == 0) {
   8. fileSize = static_cast<size_t>(fileStatus.st_size);
   9. } else {
   10. printf("get stat failed");
   11. return;
   12. }
   13. // 为 fd 资源文件创建 source 资源实例。
   14. OH_AVSource *source = OH_AVSource_CreateWithFD(fd, 0, fileSize);
   15. if (source == nullptr) {
   16. printf("create source failed");
   17. return;
   18. }
   ```
3. 获取视频轨道信息，查询文件HDR类型。

   ```
   1. int32_t trackCount = 0;
   2. uint32_t audioTrackIndex = 0;
   3. uint32_t videoTrackIndex = 0;
   4. int32_t trackType;
   ```

   ```
   1. // 从文件 source 信息获取文件轨道数。
   2. OH_AVFormat *sourceFormat = OH_AVSource_GetSourceFormat(source);
   3. if (sourceFormat == nullptr) {
   4. printf("get source format failed");
   5. return;
   6. }
   7. bool getTrackRet = OH_AVFormat_GetIntValue(sourceFormat, OH_MD_KEY_TRACK_COUNT, &trackCount);
   8. if (!getTrackRet) {
   9. // 异常处理。
   10. }
   11. OH_AVFormat_Destroy(sourceFormat);
   12. for (uint32_t index = 0; index < (static_cast<int32_t>(trackCount)); index++) {
   13. // 获取轨道信息。
   14. OH_AVFormat *format = OH_AVSource_GetTrackFormat(source, index);
   15. if (format == nullptr) {
   16. printf("get track format failed");
   17. return;
   18. }
   19. // 判断轨道类型。
   20. static_cast<OH_MediaType>(trackType) == OH_MediaType::MEDIA_TYPE_AUD ? audioTrackIndex = index : videoTrackIndex = index;
   21. // 查询文件HDR类型，是否为HDR Vivid视频。
   22. int32_t isHDRVivid = 0;
   23. bool getHdrRet = OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_IS_HDR_VIVID, &isHDRVivid);
   24. if (getHdrRet == false || isHDRVivid == 0) {
   25. printf("is not HDRVivid ");
   26. return;
   27. }
   28. OH_AVFormat_Destroy(format); // 销毁。
   29. }
   ```

## HDR Vivid视频解码

应用创建H.265解码器，并配置宽、高、format信息。解码器解析码流，生成对应的视频帧数据以及元数据。

当前支持surface输出与buffer输出两种类型，差异如下：

在接口调用的过程中，两种方式的接口调用方式基本一致，但存在以下差异点：

* Surface模式下，应用在解码器就绪前，必须调用OH\_VideoDecoder\_SetSurface接口设置OHNativeWindow。
* Buffer模式下，可以通过调用OH\_AVBuffer\_GetNativeBuffer接口将buffer转换为nativebuffer，再通过调用OH\_NativeBuffer\_GetMetadataValue接口获取元数据。

### 在 CMake 脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libnative_media_codecbase.so)
2. target_link_libraries(sample PUBLIC libnative_media_core.so)
3. target_link_libraries(sample PUBLIC libnative_media_vdec.so)
```

说明

上述'sample'字样仅为示例，此处由开发者根据实际工程目录自定义。

### 定义基础结构

本部分示例代码按照C++17标准编写，仅作参考。开发者可以参考此部分，定义自己的buffer对象。

1. 添加头文件。

   ```
   1. #include <condition_variable>
   2. #include <memory>
   3. #include <mutex>
   4. #include <queue>
   5. #include <shared_mutex>
   6. #include <multimedia/player_framework/native_avcodec_videodecoder.h>
   7. #include <multimedia/player_framework/native_avcapability.h>
   8. #include <multimedia/player_framework/native_avcodec_base.h>
   9. #include <multimedia/player_framework/native_avformat.h>
   10. #include <multimedia/player_framework/native_avbuffer.h>
   11. #include <fstream>
   ```
2. 解码器回调buffer的信息。

   ```
   1. struct CodecBufferInfo {
   2. CodecBufferInfo(uint32_t index, OH_AVBuffer *buffer): index(index), buffer(buffer), isValid(true) {}
   3. // 回调buffer。
   4. OH_AVBuffer *buffer = nullptr;
   5. // 回调buffer对应的index。
   6. uint32_t index = 0;
   7. // 判断当前buffer信息是否有效。
   8. bool isValid = true;
   9. };
   ```
3. 解码输入输出队列。

   ```
   1. class CodecBufferQueue {
   2. public:
   3. // 将回调buffer的信息传入队列。
   4. void Enqueue(const std::shared_ptr<CodecBufferInfo> bufferInfo)
   5. {
   6. std::unique_lock<std::mutex> lock(mutex_);
   7. bufferQueue_.push(bufferInfo);
   8. cond_.notify_all();
   9. }

   11. // 获取回调buffer的信息。
   12. std::shared_ptr<CodecBufferInfo> Dequeue(int32_t timeoutMs = 1000)
   13. {
   14. std::unique_lock<std::mutex> lock(mutex_);
   15. (void)cond_.wait_for(lock, std::chrono::milliseconds(timeoutMs), [this]() { return !bufferQueue_.empty(); });
   16. if (bufferQueue_.empty()) {
   17. return nullptr;
   18. }
   19. std::shared_ptr<CodecBufferInfo> bufferInfo = bufferQueue_.front();
   20. bufferQueue_.pop();
   21. return bufferInfo;
   22. }

   24. // 清空队列，之前的回调buffer设置为不可用。
   25. void Flush()
   26. {
   27. std::unique_lock<std::mutex> lock(mutex_);
   28. while (!bufferQueue_.empty()) {
   29. std::shared_ptr<CodecBufferInfo> bufferInfo = bufferQueue_.front();
   30. // Flush、Stop、Reset、Destroy操作之后，之前回调的buffer信息设置为无效。
   31. bufferInfo->isValid = false;
   32. bufferQueue_.pop();
   33. }
   34. }

   36. private:
   37. std::mutex mutex_;
   38. std::condition_variable cond_;
   39. std::queue<std::shared_ptr<CodecBufferInfo>> bufferQueue_;
   40. };
   ```
4. 全局变量。

   仅作参考，可以根据实际情况将其封装到对象中。

   ```
   1. // 解码器实例指针。
   2. OH_AVCodec *videoDec = nullptr;
   3. // 解码器同步锁。
   4. std::shared_mutex codecMutex;
   5. // 解码器输入队列。
   6. CodecBufferQueue inQueue;
   7. // 解码器输出队列。
   8. CodecBufferQueue outQueue;
   ```

### 开发步骤

**Surface模式**

1. 创建H.265解码器实例。

   应用可以通过名称或媒体类型创建解码器。示例中的变量说明如下：

   * videoDec：视频解码器实例的指针。
   * OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC：HEVC格式视频编解码器。

   ```
   1. // 通过mimetype创建H.265解码器实例。
   2. OH_AVCodec *videoDec = OH_VideoDecoder_CreateByMime(OH_AVCODEC_MIMETYPE_VIDEO_HEVC);
   ```
2. 配置异步回调函数。

   ```
   1. // 解码输入回调OH_AVCodecOnNeedInputBuffer实现。
   2. static void OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   3. {
   4. // 输入帧的数据buffer和对应的index送入inQueue队列。
   5. (void)codec;
   6. (void)userData;
   7. inQueue.Enqueue(std::make_shared<CodecBufferInfo>(index, buffer));
   8. }
   ```

   具体可参考：[视频解码Surface模式](video-decoding.md#surface模式)中的“步骤-3：调用OH\_VideoDecoder\_RegisterCallback()设置回调函数”。
3. 配置解码器。

   具体可参考：[视频解码Surface模式](video-decoding.md#surface模式)中的“步骤-5：调用OH\_VideoDecoder\_Configure()配置解码器”。
4. 设置surface。

   具体可参考：[视频解码Surface模式](video-decoding.md#surface模式)中的“步骤-6：设置surface”。
5. 调用OH\_VideoDecoder\_Start()启动解码器。

   具体可参考：[视频解码Surface模式](video-decoding.md#surface模式)中的“步骤-8：调用OH\_VideoDecoder\_Start()启动解码器”。

**Buffer模式**

1. 创建H.265解码器实例。

   应用可以通过名称或媒体类型创建解码器。示例中的变量说明如下：

   * videoDec：视频解码器实例的指针。
   * OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC：HEVC格式视频编解码器。

   ```
   1. // 通过mimetype创建H.265解码器实例。
   2. OH_AVCodec *videoDec = OH_VideoDecoder_CreateByMime(OH_AVCODEC_MIMETYPE_VIDEO_HEVC);
   ```
2. 配置异步回调函数。

   ```
   1. // 解码输入回调OH_AVCodecOnNeedInputBuffer实现。
   2. static void OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   3. {
   4. // 输入帧的数据buffer和对应的index送入inQueue队列。
   5. (void)codec;
   6. (void)userData;
   7. inQueue.Enqueue(std::make_shared<CodecBufferInfo>(index, buffer));
   8. }

   10. // 解码输出回调OH_AVCodecOnNewOutputBuffer实现。
   11. static void OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   12. {
   13. // 完成帧的数据buffer和对应的index送入outQueue队列。
   14. (void)userData;
   15. outQueue.Enqueue(std::make_shared<CodecBufferInfo>(index, buffer));
   16. }
   ```

   具体可参考：[视频解码Buffer模式](video-decoding.md#buffer模式)中的“步骤-3：调用OH\_VideoDecoder\_RegisterCallback()设置回调函数”。
3. 配置解码器。

   具体可参考：[视频解码Buffer模式](video-decoding.md#buffer模式)中的“步骤-5：调用OH\_VideoDecoder\_Configure()配置解码器”。
4. 调用OH\_VideoDecoder\_Start()启动解码器。

   具体可参考：[视频解码Buffer模式](video-decoding.md#buffer模式)中的“步骤-7：调用OH\_VideoDecoder\_Start()启动解码器”。
5. 获取元数据。

   在 CMake 脚本中链接动态库。

   ```
   1. target_link_libraries(sample PUBLIC libnative_buffer.so)
   ```

   添加头文件。

   ```
   1. #include <string.h>
   2. #include <native_buffer/native_buffer.h>
   ```

   示例代码如下：

   ```
   1. // 元数据的大小。
   2. int32_t size = 0;
   3. // 元数据实例指针。
   4. uint8_t *metadata = nullptr;
   5. // 存储元数据的容器。
   6. std::vector<uint8_t> meta;

   8. // 取出回调函数OnNewOutputBuffer存到输出队列的帧buffer。
   9. std::shared_ptr<CodecBufferInfo> bufferInfo = outQueue.Dequeue();
   10. std::shared_lock<std::shared_mutex> lock(codecMutex);
   11. if (bufferInfo == nullptr || !bufferInfo->isValid) {
   12. // 异常处理。
   13. }
   14. // 获取OH_NativeBuffer指针实例。
   15. OH_NativeBuffer *nativeBuffer = OH_AVBuffer_GetNativeBuffer(bufferInfo.buffer);
   16. if (nativeBuffer != nullptr){
   17. // 获取static元数据。
   18. if (OH_NativeBuffer_GetMetadataValue(nativeBuffer, OH_HDR_STATIC_METADATA, &size, &metadata) != 0){
   19. // 异常处理。
   20. } else {
   21. meta.resize(size);
   22. memcpy(&meta[0], metadata, size);
   23. delete[] metadata;
   24. metadata = nullptr;
   25. }
   26. // 获取dynamic元数据。
   27. if (OH_NativeBuffer_GetMetadataValue(nativeBuffer, OH_HDR_DYNAMIC_METADATA, &size, &metadata) != 0){
   28. // 异常处理。
   29. } else {
   30. meta.resize(size);
   31. memcpy(&meta[0], metadata, size);
   32. delete[] metadata;
   33. metadata = nullptr;
   34. }
   35. }
   36. //销毁nativebuffer。
   37. if (nativeBuffer != nullptr) {
   38. OH_NativeBuffer_Unreference(nativeBuffer);
   39. nativeBuffer = nullptr;
   40. }
   ```

## 处理视频帧数据

1. 解封装，循环获取帧数据。

   ```
   1. bool videoIsEnd = false;
   2. // 为资源实例创建对应的解封装器。
   3. OH_AVDemuxer *demuxer = OH_AVDemuxer_CreateWithSource(source);
   4. // 取出回调函数OnNeedInputBuffer存到输入队列的帧buffer。
   5. std::shared_ptr<CodecBufferInfo> bufferInfo = inQueue.Dequeue();
   6. std::shared_lock<std::shared_mutex> lock(codecMutex);
   7. if (bufferInfo == nullptr || !bufferInfo->isValid) {
   8. // 异常处理。
   9. }
   10. // 解封装帧数据。
   11. int32_t ret = OH_AVDemuxer_ReadSampleBuffer(demuxer, videoTrackIndex, bufferInfo->buffer);
   12. if (ret == AV_ERR_OK) {
   13. // 可通过buffer获取并处理视频帧数据。
   14. OH_AVCodecBufferAttr info;
   15. OH_AVErrCode getBufferRet = OH_AVBuffer_GetBufferAttr(bufferInfo->buffer, &info);
   16. if (getBufferRet != AV_ERR_OK) {
   17. // 异常处理。
   18. }
   19. if (info.flags == OH_AVCodecBufferFlags::AVCODEC_BUFFER_FLAGS_EOS) {
   20. videoIsEnd = true;
   21. }
   22. }
   ```
2. 将解封装后的视频帧数据送入解码输入队列。

   ```
   1. // 送入解码输入队列进行解码，index为对应队列下标。
   2. ret = OH_VideoDecoder_PushInputBuffer(videoDec, bufferInfo->index);
   3. if (ret != AV_ERR_OK) {
   4. // 异常处理。
   5. }
   ```

   后续步骤具体可参考：[视频解码](video-decoding.md)。
