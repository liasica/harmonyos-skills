---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdr-vivid-video-player
title: HDR Vivid视频播放
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > HDR Vivid能力 > HDR Vivid视频播放
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:44+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:303bd2bf670968891b61f73a612a4e9688db53f31742de9b12e66278d55ab3e6
---

开发者可以调用本模块的Native API接口，实现在视频播放中支持HDR Vivid标准。

视频播放的主要流程，是将视频文件“解封装 > 解码 > 送显/播放”。

## HDR Vivid视频解析

从视频文件中，可以解析出其是否为HDR Vivid视频，如果视频源为HDR Vivid视频，可以解析相关的信息，如元数据、颜色信息（Color）等。

### 在 CMake 脚本中链接动态库

```screen
target_link_libraries(sample PUBLIC libnative_media_codecbase.so)
target_link_libraries(sample PUBLIC libnative_media_avdemuxer.so)
target_link_libraries(sample PUBLIC libnative_media_avsource.so)
target_link_libraries(sample PUBLIC libnative_media_core.so)
```

**说明** 

上述'sample'字样仅为示例，此处由开发者根据实际工程目录自定义。

### 开发步骤

1. 添加头文件。

   ```
   #include <multimedia/player_framework/native_avdemuxer.h>
   #include <multimedia/player_framework/native_avsource.h>
   #include <multimedia/player_framework/native_avcodec_base.h>
   #include <multimedia/player_framework/native_avformat.h>
   #include <multimedia/player_framework/native_avbuffer.h>
   #include <fcntl.h>
   #include <sys/stat.h>
   #include <string>
   ```
2. 文件解析器。

   ```
   // 创建文件操作符 fd，打开时对文件实例必须有读权限（filePath 为待解封装文件路径，需预置文件，保证路径指向的文件存在）。
   std::string filePath = "test.mp4";
   int fd = open(filePath.c_str(), O_RDONLY);
   struct stat fileStatus {};
   // 获取fileSize。
   size_t fileSize = 0;
   if (stat(filePath.c_str(), &fileStatus) == 0) {
      fileSize = static_cast<size_t>(fileStatus.st_size);
   } else {
       printf("get stat failed");
       return;
   }
   // 为 fd 资源文件创建 source 资源实例。
   OH_AVSource *source = OH_AVSource_CreateWithFD(fd, 0, fileSize);
   if (source == nullptr) {
      printf("create source failed");
      return;
   }
   ```
3. 获取视频轨道信息，查询文件HDR类型。

   ```
   int32_t trackCount = 0;
   uint32_t audioTrackIndex = 0;
   uint32_t videoTrackIndex = 0;
   int32_t trackType;
   ```

   ```
   // 从文件 source 信息获取文件轨道数。
   OH_AVFormat *sourceFormat = OH_AVSource_GetSourceFormat(source);
   if (sourceFormat == nullptr) {
      printf("get source format failed");
      return;
   }
   bool getTrackRet = OH_AVFormat_GetIntValue(sourceFormat, OH_MD_KEY_TRACK_COUNT, &trackCount);
   if (!getTrackRet) {
       // 异常处理。
   }
   OH_AVFormat_Destroy(sourceFormat);
   for (uint32_t index = 0; index < (static_cast<int32_t>(trackCount)); index++) {
      // 获取轨道信息。
      OH_AVFormat *format = OH_AVSource_GetTrackFormat(source, index);
      if (format == nullptr) {
         printf("get track format failed");
         return;
      }
      // 判断轨道类型。
      static_cast<OH_MediaType>(trackType) == OH_MediaType::MEDIA_TYPE_AUD ? audioTrackIndex = index : videoTrackIndex = index;
      // 查询文件HDR类型，是否为HDR Vivid视频。
      int32_t isHDRVivid = 0;
      bool getHdrRet = OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_IS_HDR_VIVID, &isHDRVivid);
      if (getHdrRet == false || isHDRVivid == 0) {
         printf("is not HDRVivid ");
         return;
      }
      OH_AVFormat_Destroy(format); // 销毁。
   }
   ```

## HDR Vivid视频解码

应用创建H.265解码器，并配置宽、高、format信息。解码器解析码流，生成对应的视频帧数据以及元数据。

当前支持surface输出与buffer输出两种类型，差异如下：

在接口调用的过程中，两种方式的接口调用方式基本一致，但存在以下差异点：

* Surface模式下，应用在解码器就绪前，必须调用OH\_VideoDecoder\_SetSurface接口设置OHNativeWindow。
* Buffer模式下，可以通过调用OH\_AVBuffer\_GetNativeBuffer接口将buffer转换为nativebuffer，再通过调用OH\_NativeBuffer\_GetMetadataValue接口获取元数据。

### 在 CMake 脚本中链接动态库

```screen
target_link_libraries(sample PUBLIC libnative_media_codecbase.so)
target_link_libraries(sample PUBLIC libnative_media_core.so)
target_link_libraries(sample PUBLIC libnative_media_vdec.so)
```

**说明** 

上述'sample'字样仅为示例，此处由开发者根据实际工程目录自定义。

### 定义基础结构

本部分示例代码按照C++17标准编写，仅作参考。开发者可以参考此部分，定义自己的buffer对象。

1. 添加头文件。

   ```
   #include <condition_variable>
   #include <memory>
   #include <mutex>
   #include <queue>
   #include <shared_mutex>
   #include <multimedia/player_framework/native_avcodec_videodecoder.h>
   #include <multimedia/player_framework/native_avcapability.h>
   #include <multimedia/player_framework/native_avcodec_base.h>
   #include <multimedia/player_framework/native_avformat.h>
   #include <multimedia/player_framework/native_avbuffer.h>
   #include <fstream>
   ```
2. 解码器回调buffer的信息。

   ```
   struct CodecBufferInfo {
       CodecBufferInfo(uint32_t index, OH_AVBuffer *buffer): index(index), buffer(buffer), isValid(true) {}
       // 回调buffer。
       OH_AVBuffer *buffer = nullptr;
       // 回调buffer对应的index。
       uint32_t index = 0;
       // 判断当前buffer信息是否有效。
       bool isValid = true;
   };
   ```
3. 解码输入输出队列。

   ```
   class CodecBufferQueue {
   public:
       // 将回调buffer的信息传入队列。
       void Enqueue(const std::shared_ptr<CodecBufferInfo> bufferInfo)
       {
           std::unique_lock<std::mutex> lock(mutex_);
           bufferQueue_.push(bufferInfo);
           cond_.notify_all();
       }

       // 获取回调buffer的信息。
       std::shared_ptr<CodecBufferInfo> Dequeue(int32_t timeoutMs = 1000)
       {
           std::unique_lock<std::mutex> lock(mutex_);
           (void)cond_.wait_for(lock, std::chrono::milliseconds(timeoutMs), [this]() { return !bufferQueue_.empty(); });
           if (bufferQueue_.empty()) {
               return nullptr;
           }
           std::shared_ptr<CodecBufferInfo> bufferInfo = bufferQueue_.front();
           bufferQueue_.pop();
           return bufferInfo;
       }

       // 清空队列，之前的回调buffer设置为不可用。
       void Flush()
       {
           std::unique_lock<std::mutex> lock(mutex_);
           while (!bufferQueue_.empty()) {
               std::shared_ptr<CodecBufferInfo> bufferInfo = bufferQueue_.front();
               // Flush、Stop、Reset、Destroy操作之后，之前回调的buffer信息设置为无效。
               bufferInfo->isValid = false;
               bufferQueue_.pop();
           }
       }

   private:
       std::mutex mutex_;
       std::condition_variable cond_;
       std::queue<std::shared_ptr<CodecBufferInfo>> bufferQueue_;
   };
   ```
4. 全局变量。

   仅作参考，可以根据实际情况将其封装到对象中。

   ```
   // 解码器实例指针。
   OH_AVCodec *videoDec = nullptr;
   // 解码器同步锁。
   std::shared_mutex codecMutex;
   // 解码器输入队列。
   CodecBufferQueue inQueue;
   // 解码器输出队列。
   CodecBufferQueue outQueue;
   ```

### 开发步骤

**Surface模式**

1. 创建H.265解码器实例。

   应用可以通过名称或媒体类型创建解码器。示例中的变量说明如下：

   * videoDec：视频解码器实例的指针。
   * OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC：HEVC格式视频编解码器。

   ```
   // 通过mimetype创建H.265解码器实例。
   OH_AVCodec *videoDec = OH_VideoDecoder_CreateByMime(OH_AVCODEC_MIMETYPE_VIDEO_HEVC);
   ```
2. 配置异步回调函数。

   ```
   // 解码输入回调OH_AVCodecOnNeedInputBuffer实现。
   static void OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   {
       // 输入帧的数据buffer和对应的index送入inQueue队列。
       (void)codec;
       (void)userData;
       inQueue.Enqueue(std::make_shared<CodecBufferInfo>(index, buffer));
   }
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
   // 通过mimetype创建H.265解码器实例。
   OH_AVCodec *videoDec = OH_VideoDecoder_CreateByMime(OH_AVCODEC_MIMETYPE_VIDEO_HEVC);
   ```
2. 配置异步回调函数。

   ```
   // 解码输入回调OH_AVCodecOnNeedInputBuffer实现。
   static void OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   {
       // 输入帧的数据buffer和对应的index送入inQueue队列。
       (void)codec;
       (void)userData;
       inQueue.Enqueue(std::make_shared<CodecBufferInfo>(index, buffer));
   }

   // 解码输出回调OH_AVCodecOnNewOutputBuffer实现。
   static void OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   {
       // 完成帧的数据buffer和对应的index送入outQueue队列。
       (void)userData;
       outQueue.Enqueue(std::make_shared<CodecBufferInfo>(index, buffer));
   }
   ```

   具体可参考：[视频解码Buffer模式](video-decoding.md#buffer模式)中的“步骤-3：调用OH\_VideoDecoder\_RegisterCallback()设置回调函数”。
3. 配置解码器。

   具体可参考：[视频解码Buffer模式](video-decoding.md#buffer模式)中的“步骤-5：调用OH\_VideoDecoder\_Configure()配置解码器”。
4. 调用OH\_VideoDecoder\_Start()启动解码器。

   具体可参考：[视频解码Buffer模式](video-decoding.md#buffer模式)中的“步骤-7：调用OH\_VideoDecoder\_Start()启动解码器”。
5. 获取元数据。

   在 CMake 脚本中链接动态库。

   ```screen
   target_link_libraries(sample PUBLIC libnative_buffer.so)
   ```

   添加头文件。

   ```
   #include <string.h>
   #include <native_buffer/native_buffer.h>
   ```

   示例代码如下：

   ```
   // 元数据的大小。
   int32_t size = 0;
   // 元数据实例指针。
   uint8_t *metadata = nullptr;
   // 存储元数据的容器。
   std::vector<uint8_t> meta;

   // 取出回调函数OnNewOutputBuffer存到输出队列的帧buffer。
   std::shared_ptr<CodecBufferInfo> bufferInfo = outQueue.Dequeue();
   std::shared_lock<std::shared_mutex> lock(codecMutex);
   if (bufferInfo == nullptr || !bufferInfo->isValid) {
       // 异常处理。
   }
   // 获取OH_NativeBuffer指针实例。
   OH_NativeBuffer *nativeBuffer = OH_AVBuffer_GetNativeBuffer(bufferInfo.buffer);
   if (nativeBuffer != nullptr){
       // 获取static元数据。
       if (OH_NativeBuffer_GetMetadataValue(nativeBuffer, OH_HDR_STATIC_METADATA, &size, &metadata) != 0){
           // 异常处理。
       } else {
           meta.resize(size);
           memcpy(&meta[0], metadata, size);
           delete[] metadata;
           metadata = nullptr;
       }
       // 获取dynamic元数据。
       if (OH_NativeBuffer_GetMetadataValue(nativeBuffer, OH_HDR_DYNAMIC_METADATA, &size, &metadata) != 0){
           // 异常处理。
       } else {
           meta.resize(size);
           memcpy(&meta[0], metadata, size);
           delete[] metadata;
           metadata = nullptr;
       }
   }
   //销毁nativebuffer。
   if (nativeBuffer != nullptr) {
       OH_NativeBuffer_Unreference(nativeBuffer);
       nativeBuffer = nullptr;
   }
   ```

## 处理视频帧数据

1. 解封装，循环获取帧数据。

   ```
   bool videoIsEnd = false;
   // 为资源实例创建对应的解封装器。
   OH_AVDemuxer *demuxer = OH_AVDemuxer_CreateWithSource(source);
   // 取出回调函数OnNeedInputBuffer存到输入队列的帧buffer。
   std::shared_ptr<CodecBufferInfo> bufferInfo = inQueue.Dequeue();
   std::shared_lock<std::shared_mutex> lock(codecMutex);
   if (bufferInfo == nullptr || !bufferInfo->isValid) {
       // 异常处理。
   }
   // 解封装帧数据。
   int32_t ret = OH_AVDemuxer_ReadSampleBuffer(demuxer, videoTrackIndex, bufferInfo->buffer);
   if (ret == AV_ERR_OK) {
      // 可通过buffer获取并处理视频帧数据。
       OH_AVCodecBufferAttr info;
       OH_AVErrCode getBufferRet = OH_AVBuffer_GetBufferAttr(bufferInfo->buffer, &info);
       if (getBufferRet != AV_ERR_OK) {
           // 异常处理。
       }
       if (info.flags == OH_AVCodecBufferFlags::AVCODEC_BUFFER_FLAGS_EOS) {
           videoIsEnd = true;
       }
   }
   ```
2. 将解封装后的视频帧数据送入解码输入队列。

   ```
   // 送入解码输入队列进行解码，index为对应队列下标。
   ret = OH_VideoDecoder_PushInputBuffer(videoDec, bufferInfo->index);
   if (ret != AV_ERR_OK) {
      // 异常处理。
   }
   ```

   后续步骤具体可参考：[视频解码](video-decoding.md)。
