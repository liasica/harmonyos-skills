---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-decoding
title: 视频解码
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > 视频解码
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8dbeb3483bf9652b90a8278be2a02cf9a1443f93d9eb46bbf8013f6891d92ab0
---

开发者可以调用本模块的Native API接口，完成视频解码，即将媒体数据解码成YUV文件或送显。

具体实现可参考[示例工程](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)。

当前支持的解码能力请参考[AVCodec支持的格式](avcodec-support-formats.md#视频解码)。

如果需要对HDRVivid视频进行解码，需要配置MimeType为H265 (OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC)，本功能从API version 11开始支持。

通过视频解码，应用可以实现以下重点能力，包括：

| 支持的能力 | 使用简述 |
| --- | --- |
| 变分辨率 | 解码器支持输入码流分辨率发生变化，发生变化后会触发OH\_VideoDecoder\_RegisterCallback接口设置的回调函数OnStreamChanged()。具体可参考下文中：Surface模式步骤-3或Buffer模式步骤-3 |
| 动态切换surface | 通过调用OH\_VideoDecoder\_SetSurface接口配置，仅Surface模式支持。具体可参考下文中：Surface模式步骤-6 |
| 低时延解码 | 通过调用OH\_VideoDecoder\_Configure接口配置，具体可参考下文中：Surface模式的步骤-5或Buffer模式步骤-5 |

## 限制约束

1. Flush，Reset，Stop之后，重新Start时，需要重新传PPS/SPS。具体示例请参考[Surface模式](video-decoding.md#surface模式)“步骤-13：调用OH\_VideoDecoder\_Flush()”。
2. Flush，Reset，Stop，Destroy在非回调线程中执行时，会等待所有回调执行完成后，将执行结果返回给开发者。
3. 由于硬件解码器资源有限，每个解码器在使用完毕后都必须调用OH\_VideoDecoder\_Destroy接口来销毁实例并释放资源。
4. 视频解码输入码流仅支持AnnexB格式，且支持的AnnexB格式支持多slice，要求同一帧的多个slice一次送入解码器。
5. 在调用Flush，Reset，Stop的过程中，开发者不应对之前回调函数获取到的OH\_AVBuffer继续进行操作。
6. DRM解密能力在[Surface模式](video-decoding.md#surface模式)下既支持非安全视频通路，也支持安全视频通路，在[Buffer模式](video-decoding.md#buffer模式)下仅支持非安全视频通路。
7. Buffer模式和Surface模式使用方式一致的接口，所以只提供了Surface模式的示例。
8. 在Buffer模式下，开发者通过输出回调函数OH\_AVCodecOnNewOutputBuffer获取到OH\_AVBuffer的指针实例后，必须通过调用OH\_VideoDecoder\_FreeOutputBuffer接口来通知系统该实例已被使用完毕。这样系统才能够将后续解码的数据写入到相应的位置。如果开发者在调用OH\_AVBuffer\_GetNativeBuffer接口时获取到OH\_NativeBuffer指针实例，并且该实例的生命周期超过了当前的OH\_AVBuffer指针实例，那么需要进行一次数据的拷贝操作。在这种情况下，开发者需要自行管理新生成的OH\_NativeBuffer实例的生命周期，确保其正确使用和释放。
9. 为确保系统服务的持续可用性，系统会实时检测应用对实例的占用行为，当检测到应用存在异常的实例占用行为，系统会自动介入并终止该应用实例。需要注意的是：持续的实例管理不当可能导致进程被终止，开发者可通过查询以下日志来确认应用实例是否被系统终止。

   日志匹配规则：HardwareDecoding.\*kill\s+进程名:进程pid

   示例：

   HardwareDecoding process background, kill com.test:1887

   HardwareDecoding reachLimit and background, kill com.test:1887

   HardwareDecoding killPercentage, kill com.test:1887

## surface输出与buffer输出

1. 两者数据的输出方式不同。
2. 两者的适用场景不同：

   * surface输出是指用OHNativeWindow来传递输出数据，可以与其他模块对接，例如XComponent。
   * buffer输出是指经过解码的数据会以共享内存的方式输出。
3. 在接口调用的过程中，两种方式的接口调用方式基本一致，但存在以下差异点：

   * 在Surface模式下，可选择调用OH\_VideoDecoder\_FreeOutputBuffer接口丢弃输出帧（不送显）；在Buffer模式下，应用必须调用OH\_VideoDecoder\_FreeOutputBuffer接口释放数据。
   * Surface模式下，应用在解码器就绪前，必须调用[OH\_VideoDecoder\_SetSurface](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_setsurface)接口设置OHNativeWindow。启动后，调用[OH\_VideoDecoder\_RenderOutputBuffer](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_renderoutputbuffer)接口显示并释放解码帧，或调用[OH\_VideoDecoder\_RenderOutputBufferAtTime](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_renderoutputbufferattime)接口在指定时间点显示并释放解码帧。如需实现音画同步或者控制显示速度，建议优先调用OH\_VideoDecoder\_RenderOutputBufferAtTime接口送显。
   * 输出回调传出的buffer，在Buffer模式下，可以获取共享内存的地址和数据信息；在Surface模式下，只能获取buffer的数据信息。

两种模式的开发步骤详细说明请参考：[Surface模式](video-decoding.md#surface模式)和[Buffer模式](video-decoding.md#buffer模式)。

## 状态机调用关系

如下为状态机调用关系图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/m31sHnV7Rdy7MkV1VAzMTg/zh-cn_image_0000002552958544.png?HW-CC-KV=V1&HW-CC-Date=20260427T234543Z&HW-CC-Expire=86400&HW-CC-Sign=1E8F4FEE8917BDC1A6935C58766C0D9DACAF1DB33C4F7B5623B6E04B9889ACF2)

1. 有两种方式可以使解码器进入Initialized状态：

   * 初始创建解码器实例时，解码器处于Initialized状态。
   * 任何状态下，调用OH\_VideoDecoder\_Reset接口，解码器将会移回Initialized状态。
2. Initialized状态下，调用OH\_VideoDecoder\_Configure接口配置解码器，配置成功后解码器进入Configured状态。
3. Configured状态下，调用OH\_VideoDecoder\_Prepare接口进入Prepared状态。
4. Prepared状态下，调用OH\_VideoDecoder\_Start接口使解码器进入Executing状态：

   * 处于Executing状态时，调用OH\_VideoDecoder\_Stop接口可以使解码器返回到Prepared状态。
5. 在极少数情况下，解码器可能会遇到错误并进入Error状态。解码器的错误传递，可以通过队列操作返回无效值或者抛出异常：

   * Error状态下，可以调用解码器OH\_VideoDecoder\_Reset接口将解码器移到Initialized状态；或者调用OH\_VideoDecoder\_Destroy接口移动到最后的Released状态。
6. Executing状态具有三个子状态：Flushed、Running和End-of-Stream：

   * 在调用了OH\_VideoDecoder\_Start接口之后，解码器立即进入Running子状态。
   * 对于处于Executing状态的解码器，可以调用OH\_VideoDecoder\_Flush接口返回到Flushed子状态。
   * 当待处理数据全部传递给解码器后，在input buffers队列中为最后一个入队的input buffer中添加[AVCODEC\_BUFFER\_FLAGS\_EOS](../harmonyos-references/capi-native-avbuffer-info-h.md#oh_avcodecbufferflags)标记，遇到这个标记时，解码器会转换为End-of-Stream子状态。在此状态下，解码器不再接受新的输入，但是仍然会继续生成输出，直到输出到达尾帧。
7. 使用完解码器后，必须调用OH\_VideoDecoder\_Destroy接口销毁解码器实例，使解码器进入Released状态。

## 开发指导

详细的API说明请参考[native\_avcodec\_videodecoder.h](../harmonyos-references/capi-native-avcodec-videodecoder-h.md)。

如下为视频解码调用关系图：

* 虚线表示可选。
* 实线表示必选。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/EOlYhzCxRiiUjVMDOFJ6OQ/zh-cn_image_0000002583478551.png?HW-CC-KV=V1&HW-CC-Date=20260427T234543Z&HW-CC-Expire=86400&HW-CC-Sign=1F7A57471C6E1C4343338A774A495BA54C7C993B50C4431A5AEDB75C2C8B750A)

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
   1. // 视频帧宽度。
   2. int32_t width = 320;
   3. // 视频帧高度。
   4. int32_t height = 240;
   5. // 视频像素格式。
   6. OH_AVPixelFormat pixelFormat = AV_PIXEL_FORMAT_NV12;
   7. // 视频宽跨距。
   8. int32_t widthStride = 0;
   9. // 视频高跨距。
   10. int32_t heightStride = 0;
   11. // 解码器实例指针。
   12. OH_AVCodec *videoDec = nullptr;
   13. // 解码器同步锁。
   14. std::shared_mutex codecMutex;
   15. // 解码器输入队列。
   16. CodecBufferQueue inQueue;
   17. // 解码器输出队列。
   18. CodecBufferQueue outQueue;
   ```

### Surface模式

参考以下示例代码，可以完成Surface模式下视频解码的全流程，实现异步模式的数据轮转。此处以输入H.264码流文件，解码送显输出为例。

1. 添加头文件。

   ```
   1. #include <multimedia/player_framework/native_avcodec_videodecoder.h>
   2. #include <multimedia/player_framework/native_avcapability.h>
   3. #include <multimedia/player_framework/native_avcodec_base.h>
   4. #include <multimedia/player_framework/native_avformat.h>
   5. #include <multimedia/player_framework/native_avbuffer.h>
   6. #include <fstream>
   ```
2. 创建解码器实例。

   开发者可以通过名称或媒体类型创建解码器。示例中的变量说明如下：

   * videoDec：视频解码器实例的指针；
   * capability：解码器能力查询实例的指针；
   * OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC：AVC格式视频编解码器。

   ```
   1. // 通过codecname创建解码器，应用有特殊需求，比如选择支持某种分辨率规格的解码器，可先查询capability，再根据codec name创建解码器。
   2. OH_AVCapability *capability = OH_AVCodec_GetCapability(OH_AVCODEC_MIMETYPE_VIDEO_AVC, false);
   3. // 创建硬件解码器实例。
   4. OH_AVCapability *capability= OH_AVCodec_GetCapabilityByCategory(OH_AVCODEC_MIMETYPE_VIDEO_AVC, false, HARDWARE);
   5. const char *name = OH_AVCapability_GetName(capability);
   6. OH_AVCodec *videoDec = OH_VideoDecoder_CreateByName(name);
   ```

   ```
   1. // 通过MIME TYPE创建解码器，只能创建系统推荐的特定编解码器。
   2. // 涉及创建多路编解码器时，优先创建硬件解码器实例，硬件资源不够时再创建软件解码器实例。
   3. // 软/硬解：创建H.264解码器实例。
   4. OH_AVCodec *videoDec = OH_VideoDecoder_CreateByMime(OH_AVCODEC_MIMETYPE_VIDEO_AVC);
   5. // 软/硬解：创建H.265解码器实例。
   6. OH_AVCodec *videoDec = OH_VideoDecoder_CreateByMime(OH_AVCODEC_MIMETYPE_VIDEO_HEVC);
   ```
3. 调用OH\_VideoDecoder\_RegisterCallback()设置回调函数。

   注册回调函数指针集合OH\_AVCodecCallback，包括：

   * OH\_AVCodecOnError 解码器运行错误，返回的错误码详情请参见：[OH\_AVCodecOnError](../harmonyos-references/capi-native-avcodec-base-h.md#oh_avcodeconerror)；
   * OH\_AVCodecOnStreamChanged 码流信息变化，如码流宽、高变化；
   * OH\_AVCodecOnNeedInputBuffer 运行过程中需要新的输入数据，即解码器已准备好，可以输入数据；
   * OH\_AVCodecOnNewOutputBuffer 运行过程中产生了新的输出数据，即解码完成。

   开发者可以通过处理该回调报告的信息，确保解码器正常运转。

   回调函数的具体实现可参考[示例工程](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)。

   ```
   1. // 解码异常回调OH_AVCodecOnError实现。
   2. static void OnError(OH_AVCodec *codec, int32_t errorCode, void *userData)
   3. {
   4. // 回调的错误码由开发者判断处理。
   5. (void)codec;
   6. (void)errorCode;
   7. (void)userData;
   8. }

   10. // 解码数据流变化回调OH_AVCodecOnStreamChanged实现。
   11. static void OnStreamChanged(OH_AVCodec *codec, OH_AVFormat *format, void *userData)
   12. {
   13. // 可通过format获取到变化后的视频宽、高等。
   14. (void)codec;
   15. (void)userData;
   16. bool ret = OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_PIC_WIDTH, &width) &&
   17. OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_PIC_HEIGHT, &height);
   18. if (!ret) {
   19. // 异常处理。
   20. }
   21. }

   23. // 解码输入回调OH_AVCodecOnNeedInputBuffer实现。
   24. static void OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   25. {
   26. // 输入帧的数据buffer和对应的index送入inQueue队列。
   27. (void)codec;
   28. (void)userData;
   29. inQueue.Enqueue(std::make_shared<CodecBufferInfo>(index, buffer));
   30. }

   32. // 解码输出回调OH_AVCodecOnNewOutputBuffer实现。
   33. static void OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   34. {
   35. // 完成帧的数据buffer和对应的index送入outQueue队列。
   36. (void)codec;
   37. (void)userData;
   38. outQueue.Enqueue(std::make_shared<CodecBufferInfo>(index, buffer));
   39. }

   41. // 配置异步回调，调用 OH_VideoDecoder_RegisterCallback 接口。
   42. OH_AVCodecCallback cb = {&OnError, &OnStreamChanged, &OnNeedInputBuffer, &OnNewOutputBuffer};
   43. // 配置异步回调。
   44. OH_AVErrCode ret = OH_VideoDecoder_RegisterCallback(videoDec, cb, nullptr); // nullptr:开发者执行回调所依赖的数据userData为空。
   45. if (ret != AV_ERR_OK) {
   46. // 异常处理。
   47. }
   ```

   说明

   1. 在回调函数中，对数据队列进行操作时，需要注意多线程同步的问题。
   2. 播放视频时，若视频码流的SPS中包含颜色信息，解码器会把这些信息（RangeFlag、ColorPrimary、MatrixCoefficient、TransferCharacteristic）通过OH\_AVCodecOnStreamChanged接口中的OH\_AVFormat返回。
   3. 视频解码的Surface模式下，内部数据默认是走HEBC（High Efficiency Bandwidth Compression，高效带宽压缩），无法获取到widthStride和heightStride的值。
4. （可选）OH\_VideoDecoder\_SetDecryptionConfig设置解密配置。在获取到DRM信息（参考[音视频解封装](audio-video-demuxer.md)开发步骤第4步），完成DRM许可证申请后，通过此接口进行解密配置。此接口需在Prepare前调用。在Surface模式下，DRM解密能力既支持安全视频通路，也支持非安全视频通路。DRM相关接口详见[DRM API文档](../harmonyos-references/capi-drm.md)。

   添加头文件。

   ```
   1. #include <multimedia/drm_framework/native_mediakeysystem.h>
   2. #include <multimedia/drm_framework/native_mediakeysession.h>
   3. #include <multimedia/drm_framework/native_drm_err.h>
   4. #include <multimedia/drm_framework/native_drm_common.h>
   ```

   在 CMake 脚本中链接动态库。

   ```
   1. target_link_libraries(sample PUBLIC libnative_drm.so)
   ```

   根据DRM码流要求的内容保护级别和硬件设备支持的内容保护级别创建对应的通路。

   如果DRM码流要求的内容保护级别是硬件级保护，则推荐使用安全视频通路，示例如下：

   ```
   1. // 根据DRM信息创建指定的DRM系统, 以创建"com.wiseplay.drm"为例
   2. MediaKeySystem *system = nullptr;
   3. int32_t ret = OH_MediaKeySystem_Create("com.wiseplay.drm", &system);
   4. if (system == nullptr) {
   5. printf("create media key system failed");
   6. return;
   7. }

   9. // 创建解密会话，如果使用安全视频通路，应创建CONTENT_PROTECTION_LEVEL_HW_CRYPTO及其以上内容保护级别的MediaKeySession；
   10. MediaKeySession *session = nullptr;
   11. DRM_ContentProtectionLevel contentProtectionLevel = CONTENT_PROTECTION_LEVEL_HW_CRYPTO;
   12. ret = OH_MediaKeySystem_CreateMediaKeySession(system, &contentProtectionLevel, &session);
   13. if (ret != DRM_OK) {
   14. // 如创建失败，请查看DRM接口文档及日志信息
   15. printf("create media key session failed.");
   16. return;
   17. }
   18. if (session == nullptr) {
   19. printf("media key session is nullptr.");
   20. return;
   21. }

   23. // 获取许可证请求、设置许可证响应等

   25. // 设置解密配置, 即将解密会话、安全视频通路标志设置到解码器中
   26. // 如果DRM解决方案支持安全视频通路，在使用安全视频通路时，需将secureVideoPath设置为true，并在此之前须创建安全解码器
   27. // 即在步骤3使用OH_VideoDecoder_CreateByName函数、参数为解码器名称后拼接.secure（如“[CodecName].secure”）创建安全解码器
   28. bool secureVideoPath = true;
   29. ret = OH_VideoDecoder_SetDecryptionConfig(videoDec, session, secureVideoPath);
   ```

   如果DRM码流要求的内容保护级别是软件级保护，则推荐使用非安全视频通路，示例如下：

   ```
   1. // 根据DRM信息创建指定的DRM系统，以创建"com.wiseplay.drm"为例。
   2. MediaKeySystem *system = nullptr;
   3. int32_t ret = OH_MediaKeySystem_Create("com.wiseplay.drm", &system);
   4. if (system == nullptr) {
   5. printf("create media key system failed");
   6. return;
   7. }

   9. // 创建解密会话，如果使用安全视频通路，应创建CONTENT_PROTECTION_LEVEL_HW_CRYPTO及其以上内容保护级别的MediaKeySession；
   10. // 如果使用非安全视频通路，应创建CONTENT_PROTECTION_LEVEL_SW_CRYPTO及以上内容保护级别的MediaKeySession。
   11. MediaKeySession *session = nullptr;
   12. DRM_ContentProtectionLevel contentProtectionLevel = CONTENT_PROTECTION_LEVEL_SW_CRYPTO;
   13. ret = OH_MediaKeySystem_CreateMediaKeySession(system, &contentProtectionLevel, &session);
   14. if (ret != DRM_ERR_OK) {
   15. // 如创建失败，请查看DRM接口文档及日志信息。
   16. printf("create media key session failed.");
   17. return;
   18. }
   19. if (session == nullptr) {
   20. printf("media key session is nullptr.");
   21. return;
   22. }

   24. // 获取许可证请求、设置许可证响应等。

   26. // 设置解密配置，即将解密会话、安全视频通路标志设置到解码器中。
   27. // 如果DRM解决方案支持安全视频通路，在使用安全视频通路时，需将secureVideoPath设置为true，并在此之前须创建安全解码器。
   28. // 即在步骤2使用OH_VideoDecoder_CreateByName函数、参数为解码器名称后拼接.secure（如“[CodecName].secure”）创建安全解码器。
   29. bool secureVideoPath = false;
   30. ret = OH_VideoDecoder_SetDecryptionConfig(videoDec, session, secureVideoPath);
   ```
5. 调用OH\_VideoDecoder\_Configure()配置解码器。

   详细可配置选项的说明请参考[视频专有键值对](../harmonyos-references/capi-codecbase.md#媒体数据键值对)。

   参数校验规则请参考[OH\_VideoDecoder\_Configure() 参考文档](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_configure)。

   参数取值范围可以通过能力查询接口获取，具体示例请参考[获取支持的编解码能力](obtain-supported-codecs.md)。

   目前支持的所有格式都必须配置以下选项：视频帧宽度、视频帧高度。

   ```
   1. auto format = std::shared_ptr<OH_AVFormat>(OH_AVFormat_Create(), OH_AVFormat_Destroy);
   2. if (format == nullptr) {
   3. // 异常处理。
   4. }
   5. // 写入format。
   6. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_WIDTH, width); // 必须配置。
   7. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_HEIGHT, height); // 必须配置。
   8. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_PIXEL_FORMAT, pixelFormat);
   9. // 可选，配置低时延解码。
   10. // 若平台支持，当使能OH_MD_KEY_VIDEO_ENABLE_LOW_LATENCY接口时，视频解码器将按照解码序输出帧。
   11. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_VIDEO_ENABLE_LOW_LATENCY, 1);
   12. // 配置解码器。
   13. OH_AVErrCode ret = OH_VideoDecoder_Configure(videoDec, format.get());
   14. if (ret != AV_ERR_OK) {
   15. // 异常处理。
   16. }
   ```
6. 设置surface。

   本例中的nativeWindow，有两种方式获取：

   6.1 如果解码后直接显示，则从XComponent组件获取。

   添加头文件。

   ```
   1. #include <native_window/external_window.h>
   ```

   在 CMake 脚本中链接动态库。

   ```
   1. target_link_libraries(sample PUBLIC libnative_window.so)
   ```

   6.1.1 在ArkTS侧，通过xComponentController组件的getXComponentSurfaceId接口获取XComponent对应的surface的ID。详情请参考[自定义渲染 (XComponent)](napi-xcomponent-guidelines.md)。

   6.1.2 在Native侧，调用OH\_NativeWindow\_CreateNativeWindowFromSurfaceId接口创建出NativeWindow实例。

   ```
   1. OHNativeWindow* nativeWindow;
   2. // 基于步骤1.1中获取的surfaceId创建对应的nativeWindow实例。
   3. OH_NativeWindow_CreateNativeWindowFromSurfaceId(surfaceId, &nativeWindow);
   ```

   6.2 如果解码后接OpenGL后处理，则从NativeImage获取，获取方式请参考 [NativeImage](native-image-guidelines.md)。

   Surface模式，开发者可以在解码过程中执行该步骤，即动态切换surface。

   ```
   1. // 设置surface。
   2. // 配置送显窗口参数。
   3. OH_AVErrCode ret = OH_VideoDecoder_SetSurface(videoDec, nativeWindow);  // nativeWindow通过以上两种方式获取。
   4. if (ret != AV_ERR_OK) {
   5. // 异常处理。
   6. }
   7. // 配置视频与显示屏匹配模式（缓冲区按原比例缩放，使得缓冲区的较小边与窗口匹配，较长边超出窗口的部分被视为透明）。
   8. OH_NativeWindow_NativeWindowSetScalingModeV2(nativeWindow, OH_SCALING_MODE_SCALE_CROP_V2);
   ```

   注意

   若应用对1号和2号解码器均通过调用OH\_VideoDecoder\_SetSurface接口绑定至同一个NativeWindow。在2号解码器处于Running状态时，1号解码器调用OH\_VideoDecoder\_Destroy接口后，会导致2号解码器的视频播放画面卡住。

   可以采用以下方案进行更改：

   1. 等1号解码器完全释放后，再调用OH\_VideoDecoder\_Start接口启动2号解码器；
   2. 1号解码器用surface1，2号解码器先调用OH\_ConsumerSurface\_Create接口创建临时surface，等1号解码器释放后，再调用OH\_VideoDecoder\_SetSurface接口将2号解码器绑定至surface1上，详情请参见：[创建视频解码器和NativeWindow初始化并行](parallel-decoding-nativewindow.md)。
7. 调用OH\_VideoDecoder\_Prepare()解码器就绪。

   该接口将在解码器运行前进行一些数据的准备工作。

   ```
   1. OH_AVErrCode ret = OH_VideoDecoder_Prepare(videoDec);
   2. if (ret != AV_ERR_OK) {
   3. // 异常处理。
   4. }
   ```
8. 调用OH\_VideoDecoder\_Start()启动解码器。

   ```
   1. // 启动解码器，开始解码。
   2. OH_AVErrCode ret = OH_VideoDecoder_Start(videoDec);
   3. if (ret != AV_ERR_OK) {
   4. // 异常处理。
   5. }
   ```
9. （可选）OH\_VideoDecoder\_SetParameter()动态配置解码器surface参数。

   详细可配置选项的说明请参考[视频专有键值对](../harmonyos-references/capi-codecbase.md#媒体数据键值对)。

   ```
   1. auto format = std::shared_ptr<OH_AVFormat>(OH_AVFormat_Create(), OH_AVFormat_Destroy);
   2. if (format == nullptr) {
   3. // 异常处理。
   4. }
   5. // 配置显示旋转角度。
   6. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_ROTATION, 90);
   7. OH_AVErrCode ret = OH_VideoDecoder_SetParameter(videoDec, format.get());
   8. if (ret != AV_ERR_OK) {
   9. // 异常处理。
   10. }
   ```
10. （可选）调用OH\_AVCencInfo\_SetAVBuffer()，设置cencInfo。

    若当前播放的节目是DRM加密节目，应用自行实现媒体解封装功能而非使用系统[解封装](audio-video-demuxer.md)功能时，需调用OH\_AVCencInfo\_SetAVBuffer()将cencInfo设置到AVBuffer，这样AVBuffer携带待解密的数据以及cencInfo，以实现AVBuffer中媒体数据的解密。当应用使用系统[解封装](audio-video-demuxer.md)功能时，则无需调用此接口。

    添加头文件。

    ```
    1. #include <multimedia/player_framework/native_cencinfo.h>
    ```

    在 CMake 脚本中链接动态库。

    ```
    1. target_link_libraries(sample PUBLIC libnative_media_avcencinfo.so)
    ```

    使用示例：

    * buffer：回调函数OnNeedInputBuffer传入的参数。

    ```
    1. uint32_t keyIdLen = DRM_KEY_ID_SIZE;
    2. uint8_t keyId[] = {
    3. 0xd4, 0xb2, 0x01, 0xe4, 0x61, 0xc8, 0x98, 0x96,
    4. 0xcf, 0x05, 0x22, 0x39, 0x8d, 0x09, 0xe6, 0x28};
    5. uint32_t ivLen = DRM_KEY_IV_SIZE;
    6. uint8_t iv[] = {
    7. 0xbf, 0x77, 0xed, 0x51, 0x81, 0xde, 0x36, 0x3e,
    8. 0x52, 0xf7, 0x20, 0x4f, 0x72, 0x14, 0xa3, 0x95};
    9. uint32_t encryptedBlockCount = 0;
    10. uint32_t skippedBlockCount = 0;
    11. uint32_t firstEncryptedOffset = 0;
    12. uint32_t subsampleCount = 1;
    13. DrmSubsample subsamples[1] = { {0x10, 0x16} };
    14. // 创建CencInfo实例。
    15. OH_AVCencInfo *cencInfo = OH_AVCencInfo_Create();
    16. if (cencInfo == nullptr) {
    17. // 异常处理。
    18. }
    19. // 设置解密算法。
    20. OH_AVErrCode errNo = OH_AVCencInfo_SetAlgorithm(cencInfo, DRM_ALG_CENC_AES_CTR);
    21. if (errNo != AV_ERR_OK) {
    22. // 异常处理。
    23. }
    24. // 设置KeyId和Iv。
    25. errNo = OH_AVCencInfo_SetKeyIdAndIv(cencInfo, keyId, keyIdLen, iv, ivLen);
    26. if (errNo != AV_ERR_OK) {
    27. // 异常处理。
    28. }
    29. // 设置Sample信息。
    30. errNo = OH_AVCencInfo_SetSubsampleInfo(cencInfo, encryptedBlockCount, skippedBlockCount, firstEncryptedOffset,
    31. subsampleCount, subsamples);
    32. if (errNo != AV_ERR_OK) {
    33. // 异常处理。
    34. }
    35. // 设置模式：KeyId、Iv和SubSamples已被设置。
    36. errNo = OH_AVCencInfo_SetMode(cencInfo, DRM_CENC_INFO_KEY_IV_SUBSAMPLES_SET);
    37. if (errNo != AV_ERR_OK) {
    38. // 异常处理。
    39. }
    40. // 将CencInfo设置到AVBuffer中。
    41. errNo = OH_AVCencInfo_SetAVBuffer(cencInfo, buffer);
    42. if (errNo != AV_ERR_OK) {
    43. // 异常处理。
    44. }
    45. // 销毁CencInfo实例。
    46. errNo = OH_AVCencInfo_Destroy(cencInfo);
    47. if (errNo != AV_ERR_OK) {
    48. // 异常处理。
    49. }
    ```
11. 调用OH\_VideoDecoder\_PushInputBuffer()写入解码码流。

    送入输入队列进行解码，以下示例中：

    * size、offset、pts、frameData：输入尺寸、偏移量、时间戳、帧数据等字段信息，获取方式可以参考[音视频解封装](audio-video-demuxer.md)“步骤-9：开始解封装，循环获取sample”。
    * flags：缓冲区标记的类别，请参考[OH\_AVCodecBufferFlags](../harmonyos-references/capi-native-avbuffer-info-h.md#oh_avcodecbufferflags)。

    bufferInfo的成员变量：

    * buffer：回调函数OnNeedInputBuffer传入的参数，可以通过[OH\_AVBuffer\_GetAddr](../harmonyos-references/capi-native-avbuffer-h.md#oh_avbuffer_getaddr)接口获取输入码流虚拟地址。
    * index：回调函数OnNeedInputBuffer传入的参数，与buffer唯一对应的标识。
    * isValid：bufferInfo中存储的buffer实例是否有效。

    ```
    1. std::shared_ptr<CodecBufferInfo> bufferInfo = inQueue.Dequeue();
    2. std::shared_lock<std::shared_mutex> lock(codecMutex);
    3. if (bufferInfo == nullptr || !bufferInfo->isValid) {
    4. // 异常处理。
    5. }
    6. // 写入码流数据。
    7. uint8_t *addr = OH_AVBuffer_GetAddr(bufferInfo->buffer);
    8. if (addr == nullptr) {
    9. // 异常处理。
    10. }
    11. int32_t capacity = OH_AVBuffer_GetCapacity(bufferInfo->buffer);
    12. if (size > capacity) {
    13. // 异常处理。
    14. }
    15. memcpy(addr, frameData, size);
    16. // 配置帧数据的输入尺寸、偏移量、时间戳等字段信息。
    17. OH_AVCodecBufferAttr info;
    18. info.size = size;
    19. info.offset = offset;
    20. info.pts = pts;
    21. info.flags = flags;
    22. // info信息写入buffer。
    23. OH_AVErrCode setBufferRet = OH_AVBuffer_SetBufferAttr(bufferInfo->buffer, &info);
    24. if (setBufferRet != AV_ERR_OK) {
    25. // 异常处理。
    26. }
    27. // 送入解码输入队列进行解码。
    28. OH_AVErrCode pushInputRet = OH_VideoDecoder_PushInputBuffer(videoDec, bufferInfo->index);
    29. if (pushInputRet != AV_ERR_OK) {
    30. // 异常处理。
    31. }
    ```
12. 调用OH\_VideoDecoder\_RenderOutputBuffer()/OH\_VideoDecoder\_RenderOutputBufferAtTime()显示并释放解码帧，或调用OH\_VideoDecoder\_FreeOutputBuffer()释放解码帧。

    以下示例中，bufferInfo的成员变量：

    * index：回调函数OnNewOutputBuffer传入的参数，与buffer唯一对应的标识；
    * buffer：回调函数OnNewOutputBuffer传入的参数，Surface模式开发者无法通过[OH\_AVBuffer\_GetAddr](../harmonyos-references/capi-native-avbuffer-h.md#oh_avbuffer_getaddr)接口获取图像虚拟地址；
    * isValid：bufferInfo中存储的buffer实例是否有效。

    ```
    1. std::shared_ptr<CodecBufferInfo> bufferInfo = outQueue.Dequeue();
    2. std::shared_lock<std::shared_mutex> lock(codecMutex);
    3. if (bufferInfo == nullptr || !bufferInfo->isValid) {
    4. // 异常处理。
    5. }
    6. // 获取解码后信息。
    7. OH_AVCodecBufferAttr info;
    8. OH_AVErrCode getBufferRet = OH_AVBuffer_GetBufferAttr(bufferInfo->buffer, &info);
    9. if (getBufferRet != AV_ERR_OK) {
    10. // 异常处理。
    11. }
    12. // 值由开发者决定。
    13. bool isRender;
    14. bool isNeedRenderAtTime;
    15. OH_AVErrCode ret = AV_ERR_OK;
    16. if (isRender) {
    17. // 显示并释放已完成处理的信息，index为对应buffer队列的下标。
    18. if (isNeedRenderAtTime){
    19. // 获取系统绝对时间，renderTimestamp由开发者结合业务指定显示时间。
    20. int64_t renderTimestamp =
    21. std::chrono::duration_cast<std::chrono::nanoseconds>(std::chrono::high_resolution_clock::now().time_since_epoch()).count();
    22. ret = OH_VideoDecoder_RenderOutputBufferAtTime(videoDec, bufferInfo->index, renderTimestamp);
    23. } else {
    24. ret = OH_VideoDecoder_RenderOutputBuffer(videoDec, bufferInfo->index);
    25. }

    27. } else {
    28. // 释放已完成处理的信息。
    29. ret = OH_VideoDecoder_FreeOutputBuffer(videoDec, bufferInfo->index);
    30. }
    31. if (ret != AV_ERR_OK) {
    32. // 异常处理。
    33. }
    ```

    注意

    1. 如果要获取buffer的属性，如pixel\_format、stride等可通过调用[OH\_NativeWindow\_NativeWindowHandleOpt](../harmonyos-references/capi-external-window-h.md#oh_nativewindow_nativewindowhandleopt)接口获取。
    2. 显示并释放解码帧时，推荐优先调用[OH\_VideoDecoder\_RenderOutputBufferAtTime](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_renderoutputbufferattime)接口。
13. （可选）调用OH\_VideoDecoder\_Flush()刷新解码器。

    调用OH\_VideoDecoder\_Flush接口后，解码器仍处于运行态，但会清除解码器中缓存的输入和输出数据及参数集如H.264格式的PPS/SPS。此时需要调用OH\_VideoDecoder\_Start接口重新开始解码。

    以下示例中：

    * xpsData、xpsSize：PPS/SPS信息，获取方式可以参考[音视频解封装](audio-video-demuxer.md)。

    ```
    1. std::unique_lock<std::shared_mutex> lock(codecMutex);
    2. // 刷新解码器videoDec。
    3. OH_AVErrCode flushRet = OH_VideoDecoder_Flush(videoDec);
    4. if (flushRet != AV_ERR_OK) {
    5. // 异常处理。
    6. }
    7. inQueue.Flush();
    8. outQueue.Flush();
    9. // 重新开始解码。
    10. OH_AVErrCode startRet = OH_VideoDecoder_Start(videoDec);
    11. if (startRet != AV_ERR_OK) {
    12. // 异常处理。
    13. }

    15. std::shared_ptr<CodecBufferInfo> bufferInfo = inQueue.Dequeue();
    16. if (bufferInfo == nullptr || !bufferInfo->isValid) {
    17. // 异常处理。
    18. }
    19. // 重传PPS/SPS。
    20. // 配置帧数据PPS/SPS信息。
    21. uint8_t *addr = OH_AVBuffer_GetAddr(bufferInfo->buffer);
    22. if (addr == nullptr) {
    23. // 异常处理
    24. }
    25. int32_t capacity = OH_AVBuffer_GetCapacity(bufferInfo->buffer);
    26. if (xpsSize > capacity) {
    27. // 异常处理。
    28. }
    29. memcpy(addr, xpsData, xpsSize);
    30. OH_AVCodecBufferAttr info;
    31. info.flags = AVCODEC_BUFFER_FLAG_CODEC_DATA;
    32. // info信息写入buffer。
    33. OH_AVErrCode setBufferRet = OH_AVBuffer_SetBufferAttr(bufferInfo->buffer, &info);
    34. if (setBufferRet != AV_ERR_OK) {
    35. // 异常处理。
    36. }
    37. // 将帧数据推送到解码器中，index为对应buffer队列的下标。
    38. OH_AVErrCode pushInputRet = OH_VideoDecoder_PushInputBuffer(videoDec, bufferInfo->index);
    39. if (pushInputRet != AV_ERR_OK) {
    40. // 异常处理。
    41. }
    ```

    注意

    Flush之后，重新调用OH\_VideoDecoder\_Start接口时，需要重新传PPS/SPS。
14. （可选）调用OH\_VideoDecoder\_Reset()重置解码器。

    调用OH\_VideoDecoder\_Reset接口后，解码器回到初始化的状态，需要调用OH\_VideoDecoder\_Configure接口、OH\_VideoDecoder\_SetSurface接口和OH\_VideoDecoder\_Prepare接口重新配置。

    ```
    1. std::unique_lock<std::shared_mutex> lock(codecMutex);
    2. // 重置解码器videoDec。
    3. OH_AVErrCode resetRet = OH_VideoDecoder_Reset(videoDec);
    4. if (resetRet != AV_ERR_OK) {
    5. // 异常处理。
    6. }
    7. inQueue.Flush();
    8. outQueue.Flush();
    9. // 重新配置解码器参数。
    10. auto format = std::shared_ptr<OH_AVFormat>(OH_AVFormat_Create(), OH_AVFormat_Destroy);
    11. if (format == nullptr) {
    12. // 异常处理。
    13. }
    14. OH_AVErrCode configRet = OH_VideoDecoder_Configure(videoDec, format.get());
    15. if (configRet != AV_ERR_OK) {
    16. // 异常处理。
    17. }
    18. // Surface模式重新配置surface，而Buffer模式不需要配置surface。
    19. OH_AVErrCode setRet = OH_VideoDecoder_SetSurface(videoDec, nativeWindow);
    20. if (setRet != AV_ERR_OK) {
    21. // 异常处理。
    22. }
    23. // 解码器重新就绪。
    24. OH_AVErrCode prepareRet = OH_VideoDecoder_Prepare(videoDec);
    25. if (prepareRet != AV_ERR_OK) {
    26. // 异常处理。
    27. }
    ```
15. （可选）调用OH\_VideoDecoder\_Stop()停止解码器。

    调用OH\_VideoDecoder\_Stop()后，解码器保留了解码实例，释放输入输出buffer。开发者可以直接调用OH\_VideoDecoder\_Start接口继续解码，输入的第一个buffer需要携带参数集，从IDR帧开始送入。

    ```
    1. std::unique_lock<std::shared_mutex> lock(codecMutex);
    2. // 终止解码器videoDec。
    3. OH_AVErrCode ret = OH_VideoDecoder_Stop(videoDec);
    4. if (ret != AV_ERR_OK) {
    5. // 异常处理。
    6. }
    7. inQueue.Flush();
    8. outQueue.Flush();
    ```
16. 调用OH\_VideoDecoder\_Destroy()销毁解码器实例，释放资源。

    说明

    1. 不能在回调函数中调用；
    2. 执行该步骤之后，需要开发者将videoDec指向nullptr，防止野指针导致程序错误。

    ```
    1. std::unique_lock<std::shared_mutex> lock(codecMutex);
    2. // 释放nativeWindow实例。
    3. if(nativeWindow != nullptr){
    4. OH_NativeWindow_DestroyNativeWindow(nativeWindow);
    5. nativeWindow = nullptr;
    6. }
    7. // 调用OH_VideoDecoder_Destroy，注销解码器。
    8. OH_AVErrCode ret = AV_ERR_OK;
    9. if (videoDec != nullptr) {
    10. OH_VideoDecoder_Destroy(videoDec);
    11. videoDec = nullptr;
    12. }
    13. inQueue.Flush();
    14. outQueue.Flush();
    ```

### Buffer模式

参考以下示例代码，可以完成Buffer模式下视频解码的全流程，实现异步模式的数据轮转。此处以输入H.264码流文件，解码成YUV文件为例。

1. 添加头文件。

   ```
   1. #include <multimedia/player_framework/native_avcodec_videodecoder.h>
   2. #include <multimedia/player_framework/native_avcapability.h>
   3. #include <multimedia/player_framework/native_avcodec_base.h>
   4. #include <multimedia/player_framework/native_avformat.h>
   5. #include <multimedia/player_framework/native_avbuffer.h>
   6. #include <native_buffer/native_buffer.h>
   7. #include <fstream>
   ```
2. 创建解码器实例。

   与Surface模式相同，此处不再赘述。

   ```
   1. // 通过codecname创建解码器，应用有特殊需求，比如选择支持某种分辨率规格的解码器，可先查询capability，再根据codec name创建解码器。
   2. OH_AVCapability *capability = OH_AVCodec_GetCapability(OH_AVCODEC_MIMETYPE_VIDEO_AVC, false);
   3. const char *name = OH_AVCapability_GetName(capability);
   4. OH_AVCodec *videoDec = OH_VideoDecoder_CreateByName(name);
   ```

   ```
   1. // 通过MIME TYPE创建解码器，只能创建系统推荐的特定编解码器。
   2. // 涉及创建多路编解码器时，优先创建硬件解码器实例，硬件资源不够时再创建软件解码器实例。
   3. // 软/硬解：创建H.264解码器。
   4. OH_AVCodec *videoDec = OH_VideoDecoder_CreateByMime(OH_AVCODEC_MIMETYPE_VIDEO_AVC);
   5. // 硬解：创建H.265解码器。
   6. OH_AVCodec *videoDec = OH_VideoDecoder_CreateByMime(OH_AVCODEC_MIMETYPE_VIDEO_HEVC);
   ```
3. 调用OH\_VideoDecoder\_RegisterCallback()设置回调函数。

   注册回调函数指针集合OH\_AVCodecCallback，包括：

   * OH\_AVCodecOnError 解码器运行错误，返回的错误码详情请参见：[OH\_AVCodecOnError](../harmonyos-references/capi-native-avcodec-base-h.md#oh_avcodeconerror)；
   * OH\_AVCodecOnStreamChanged 码流信息变化，如码流宽、高变化；
   * OH\_AVCodecOnNeedInputBuffer 运行过程中需要新的输入数据，即解码器已准备好，可以输入数据；
   * OH\_AVCodecOnNewOutputBuffer 运行过程中产生了新的输出数据，即解码完成。

   开发者可以通过处理该回调报告的信息，确保解码器正常运转。

   回调函数的具体实现可参考[示例工程](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)。

   ```
   1. int32_t cropTop = 0;
   2. int32_t cropBottom = 0;
   3. int32_t cropLeft = 0;
   4. int32_t cropRight = 0;
   5. bool isFirstFrame = true;
   6. // 解码异常回调OH_AVCodecOnError实现。
   7. static void OnError(OH_AVCodec *codec, int32_t errorCode, void *userData)
   8. {
   9. // 回调的错误码由开发者判断处理。
   10. (void)codec;
   11. (void)errorCode;
   12. (void)userData;
   13. }

   15. // 解码数据流变化回调OH_AVCodecOnStreamChanged实现。
   16. static void OnStreamChanged(OH_AVCodec *codec, OH_AVFormat *format, void *userData)
   17. {
   18. // 可选，开发者需要获取视频宽、高、跨距等时可配置。
   19. // 可通过format获取到变化后的视频宽、高、跨距等。
   20. (void)codec;
   21. (void)userData;
   22. bool ret = OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_PIC_WIDTH, &width) &&
   23. OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_PIC_HEIGHT, &height) &&
   24. OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_STRIDE, &widthStride) &&
   25. OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_SLICE_HEIGHT, &heightStride) &&
   26. // 获取裁剪矩形信息可选。
   27. OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_CROP_TOP, &cropTop) &&
   28. OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_CROP_BOTTOM, &cropBottom) &&
   29. OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_CROP_LEFT, &cropLeft) &&
   30. OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_CROP_RIGHT, &cropRight);
   31. if (!ret) {
   32. // 异常处理。
   33. }
   34. }

   36. // 解码输入回调OH_AVCodecOnNeedInputBuffer实现。
   37. static void OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   38. {
   39. // 输入帧的数据buffer和对应的index送入inQueue队列。
   40. (void)codec;
   41. (void)userData;
   42. inQueue.Enqueue(std::make_shared<CodecBufferInfo>(index, buffer));
   43. }

   45. // 解码输出回调OH_AVCodecOnNewOutputBuffer实现。
   46. static void OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   47. {
   48. // 可选，开发者需要获取视频宽、高、跨距等时可配置。
   49. // 获取视频宽、高、跨距。
   50. if (isFirstFrame) {
   51. auto format = std::shared_ptr<OH_AVFormat>(OH_VideoDecoder_GetOutputDescription(codec), OH_AVFormat_Destroy);
   52. if (format == nullptr) {
   53. // 异常处理。
   54. }
   55. bool ret = OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_VIDEO_PIC_WIDTH, &width) &&
   56. OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_VIDEO_PIC_HEIGHT, &height) &&
   57. OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_VIDEO_STRIDE, &widthStride) &&
   58. OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_VIDEO_SLICE_HEIGHT, &heightStride) &&
   59. // 获取裁剪矩形信息可选。
   60. OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_VIDEO_CROP_TOP, &cropTop) &&
   61. OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_VIDEO_CROP_BOTTOM, &cropBottom) &&
   62. OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_VIDEO_CROP_LEFT, &cropLeft) &&
   63. OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_VIDEO_CROP_RIGHT, &cropRight);
   64. if (!ret) {
   65. // 异常处理。
   66. }
   67. isFirstFrame = false;
   68. }
   69. // 完成帧的数据buffer和对应的index送入outQueue队列。
   70. (void)userData;
   71. outQueue.Enqueue(std::make_shared<CodecBufferInfo>(index, buffer));
   72. }
   73. // 配置异步回调，调用OH_VideoDecoder_RegisterCallback接口。
   74. OH_AVCodecCallback cb = {&OnError, &OnStreamChanged, &OnNeedInputBuffer, &OnNewOutputBuffer};
   75. // 配置异步回调。
   76. OH_AVErrCode ret = OH_VideoDecoder_RegisterCallback(videoDec, cb, nullptr); // nullptr:开发者执行回调所依赖的数据userData为空。
   77. if (ret != AV_ERR_OK) {
   78. // 异常处理。
   79. }
   ```

   说明

   在回调函数中，对数据队列进行操作时，需要注意多线程同步的问题。
4. （可选）OH\_VideoDecoder\_SetDecryptionConfig设置解密配置。在获取到DRM信息（参考[音视频解封装](audio-video-demuxer.md)开发步骤第4步），完成DRM许可证申请后，通过此接口进行解密配置。此接口需在Prepare前调用。在Buffer模式下，DRM解密能力仅支持非安全视频通路。DRM相关接口详见[DRM API文档](../harmonyos-references/capi-drm.md)。

   添加头文件。

   ```
   1. #include <multimedia/drm_framework/native_mediakeysystem.h>
   2. #include <multimedia/drm_framework/native_mediakeysession.h>
   3. #include <multimedia/drm_framework/native_drm_err.h>
   4. #include <multimedia/drm_framework/native_drm_common.h>
   ```

   在 CMake 脚本中链接动态库。

   ```
   1. target_link_libraries(sample PUBLIC libnative_drm.so)
   ```

   使用示例：

   ```
   1. // 根据DRM信息创建指定的DRM系统，以创建"com.wiseplay.drm"为例。
   2. MediaKeySystem *system = nullptr;
   3. int32_t ret = OH_MediaKeySystem_Create("com.wiseplay.drm", &system);
   4. if (system == nullptr) {
   5. printf("create media key system failed");
   6. return;
   7. }

   9. // 创建解密会话。
   10. // 使用非安全视频通路，应创建CONTENT_PROTECTION_LEVEL_SW_CRYPTO及以上内容保护级别的MediaKeySession。
   11. MediaKeySession *session = nullptr;
   12. DRM_ContentProtectionLevel contentProtectionLevel = CONTENT_PROTECTION_LEVEL_SW_CRYPTO;
   13. ret = OH_MediaKeySystem_CreateMediaKeySession(system, &contentProtectionLevel, &session);
   14. if (ret != DRM_ERR_OK) {
   15. // 如创建失败，请查看DRM接口文档及日志信息。
   16. printf("create media key session failed.");
   17. return;
   18. }
   19. if (session == nullptr) {
   20. printf("media key session is nullptr.");
   21. return;
   22. }
   23. // 获取许可证请求、设置许可证响应等。
   24. // 设置解密配置，即将解密会话、安全视频通路标志设置到解码器中。
   25. bool secureVideoPath = false;
   26. ret = OH_VideoDecoder_SetDecryptionConfig(videoDec, session, secureVideoPath);
   ```
5. 调用OH\_VideoDecoder\_Configure()配置解码器。

   与Surface模式相同，此处不再赘述。

   ```
   1. auto format = std::shared_ptr<OH_AVFormat>(OH_AVFormat_Create(), OH_AVFormat_Destroy);
   2. if (format == nullptr) {
   3. // 异常处理。
   4. }
   5. // 写入format。
   6. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_WIDTH, width); // 必须配置。
   7. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_HEIGHT, height); // 必须配置。
   8. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_PIXEL_FORMAT, pixelFormat);
   9. // 配置解码器。
   10. OH_AVErrCode ret = OH_VideoDecoder_Configure(videoDec, format.get());
   11. if (ret != AV_ERR_OK) {
   12. // 异常处理。
   13. }
   ```
6. 调用OH\_VideoDecoder\_Prepare()解码器就绪。

   该接口将在解码器运行前进行一些数据的准备工作。

   ```
   1. OH_AVErrCode ret = OH_VideoDecoder_Prepare(videoDec);
   2. if (ret != AV_ERR_OK) {
   3. // 异常处理。
   4. }
   ```
7. 调用OH\_VideoDecoder\_Start()启动解码器。

   ```
   1. std::unique_ptr<std::ofstream> outputFile = std::make_unique<std::ofstream>();
   2. if (outputFile != nullptr) {
   3. outputFile->open("/*yourpath*.yuv", std::ios::out | std::ios::binary | std::ios::ate);
   4. }
   5. // 启动解码器，开始解码。
   6. OH_AVErrCode ret = OH_VideoDecoder_Start(videoDec);
   7. if (ret != AV_ERR_OK) {
   8. // 异常处理。
   9. }
   ```
8. （可选）OH\_VideoDecoder\_SetParameter()动态配置解码器参数。

   详细可配置选项的说明请参考[视频专有键值对](../harmonyos-references/capi-codecbase.md#媒体数据键值对)。

   ```
   1. auto format = std::shared_ptr<OH_AVFormat>(OH_AVFormat_Create(), OH_AVFormat_Destroy);
   2. if (format == nullptr) {
   3. // 异常处理。
   4. }
   5. // 配置帧率。
   6. OH_AVFormat_SetDoubleValue(format.get(), OH_MD_KEY_FRAME_RATE, 30.0);
   7. OH_AVErrCode ret = OH_VideoDecoder_SetParameter(videoDec, format.get());
   8. if (ret != AV_ERR_OK) {
   9. // 异常处理。
   10. }
   ```
9. （可选）调用OH\_AVCencInfo\_SetAVBuffer()，设置cencInfo。

   与Surface模式相同，此处不再赘述。

   使用示例：

   ```
   1. uint32_t keyIdLen = DRM_KEY_ID_SIZE;
   2. uint8_t keyId[] = {
   3. 0xd4, 0xb2, 0x01, 0xe4, 0x61, 0xc8, 0x98, 0x96,
   4. 0xcf, 0x05, 0x22, 0x39, 0x8d, 0x09, 0xe6, 0x28};
   5. uint32_t ivLen = DRM_KEY_IV_SIZE;
   6. uint8_t iv[] = {
   7. 0xbf, 0x77, 0xed, 0x51, 0x81, 0xde, 0x36, 0x3e,
   8. 0x52, 0xf7, 0x20, 0x4f, 0x72, 0x14, 0xa3, 0x95};
   9. uint32_t encryptedBlockCount = 0;
   10. uint32_t skippedBlockCount = 0;
   11. uint32_t firstEncryptedOffset = 0;
   12. uint32_t subsampleCount = 1;
   13. DrmSubsample subsamples[1] = { {0x10, 0x16} };
   14. // 创建CencInfo实例。
   15. OH_AVCencInfo *cencInfo = OH_AVCencInfo_Create();
   16. if (cencInfo == nullptr) {
   17. // 异常处理。
   18. }
   19. // 设置解密算法。
   20. OH_AVErrCode errNo = OH_AVCencInfo_SetAlgorithm(cencInfo, DRM_ALG_CENC_AES_CTR);
   21. if (errNo != AV_ERR_OK) {
   22. // 异常处理。
   23. }
   24. // 设置KeyId和Iv。
   25. errNo = OH_AVCencInfo_SetKeyIdAndIv(cencInfo, keyId, keyIdLen, iv, ivLen);
   26. if (errNo != AV_ERR_OK) {
   27. // 异常处理。
   28. }
   29. // 设置Sample信息。
   30. errNo = OH_AVCencInfo_SetSubsampleInfo(cencInfo, encryptedBlockCount, skippedBlockCount, firstEncryptedOffset,
   31. subsampleCount, subsamples);
   32. if (errNo != AV_ERR_OK) {
   33. // 异常处理。
   34. }
   35. // 设置模式：KeyId、Iv和SubSamples已被设置。
   36. errNo = OH_AVCencInfo_SetMode(cencInfo, DRM_CENC_INFO_KEY_IV_SUBSAMPLES_SET);
   37. if (errNo != AV_ERR_OK) {
   38. // 异常处理。
   39. }
   40. // 将CencInfo设置到AVBuffer中。
   41. errNo = OH_AVCencInfo_SetAVBuffer(cencInfo, buffer);
   42. if (errNo != AV_ERR_OK) {
   43. // 异常处理。
   44. }
   45. // 销毁CencInfo实例。
   46. errNo = OH_AVCencInfo_Destroy(cencInfo);
   47. if (errNo != AV_ERR_OK) {
   48. // 异常处理。
   49. }
   ```
10. 调用OH\_VideoDecoder\_PushInputBuffer()写入解码码流。

    与Surface模式相同，此处不再赘述。

    ```
    1. std::shared_ptr<CodecBufferInfo> bufferInfo = inQueue.Dequeue();
    2. std::shared_lock<std::shared_mutex> lock(codecMutex);
    3. if (bufferInfo == nullptr || !bufferInfo->isValid) {
    4. // 异常处理。
    5. }
    6. // 写入码流数据。
    7. uint8_t *addr = OH_AVBuffer_GetAddr(bufferInfo->buffer);
    8. if (addr == nullptr) {
    9. // 异常处理。
    10. }
    11. int32_t capacity = OH_AVBuffer_GetCapacity(bufferInfo->buffer);
    12. if (size > capacity) {
    13. // 异常处理。
    14. }
    15. memcpy(addr, frameData, size);
    16. // 配置帧数据的输入尺寸、偏移量、时间戳等字段信息。
    17. OH_AVCodecBufferAttr info;
    18. info.size = size;
    19. info.offset = offset;
    20. info.pts = pts;
    21. info.flags = flags;
    22. // info信息写入buffer。
    23. OH_AVErrCode setBufferRet = OH_AVBuffer_SetBufferAttr(bufferInfo->buffer, &info);
    24. if (setBufferRet != AV_ERR_OK) {
    25. // 异常处理。
    26. }
    27. // 送入解码输入队列进行解码，index为对应buffer队列的下标。
    28. OH_AVErrCode pushInputRet = OH_VideoDecoder_PushInputBuffer(videoDec, bufferInfo->index);
    29. if (pushInputRet != AV_ERR_OK) {
    30. // 异常处理。
    31. }
    ```
11. 调用OH\_VideoDecoder\_FreeOutputBuffer()释放解码帧。

    以下示例中，bufferInfo的成员变量：

    * index：回调函数OnNewOutputBuffer传入的参数，与buffer唯一对应的标识；
    * buffer： 回调函数OnNewOutputBuffer传入的参数，可以通过[OH\_AVBuffer\_GetAddr](../harmonyos-references/capi-native-avbuffer-h.md#oh_avbuffer_getaddr)接口获取图像虚拟地址；
    * isValid：bufferInfo中存储的buffer实例是否有效。

    ```
    1. std::shared_ptr<CodecBufferInfo> bufferInfo = outQueue.Dequeue();
    2. std::shared_lock<std::shared_mutex> lock(codecMutex);
    3. if (bufferInfo == nullptr || !bufferInfo->isValid) {
    4. // 异常处理。
    5. }
    6. // 获取解码后信息。
    7. OH_AVCodecBufferAttr info;
    8. OH_AVErrCode getBufferRet = OH_AVBuffer_GetBufferAttr(bufferInfo->buffer, &info);
    9. if (getBufferRet != AV_ERR_OK) {
    10. // 异常处理。
    11. }
    12. // 将解码完成数据data写入到对应输出文件中。
    13. uint8_t *addr = OH_AVBuffer_GetAddr(bufferInfo->buffer);
    14. if (addr == nullptr) {
    15. // 异常处理。
    16. }
    17. if (outputFile != nullptr && outputFile->is_open()) {
    18. outputFile->write(reinterpret_cast<char *>(addr), info.size);
    19. }
    20. // Buffer模式，释放已完成写入的数据，index为对应buffer队列的下标。
    21. OH_AVErrCode freeOutputRet = OH_VideoDecoder_FreeOutputBuffer(videoDec, bufferInfo->index);
    22. if (freeOutputRet != AV_ERR_OK) {
    23. // 异常处理。
    24. }
    ```

    NV12/NV21图像如果需要依次将Y、U、V三个分量拷贝至另一块buffer中，以NV12图像为例，按行拷贝示例如下：

    以NV12图像为例，width、height、wStride、hStride图像排布参考下图：

    * OH\_MD\_KEY\_VIDEO\_PIC\_WIDTH表示width；
    * OH\_MD\_KEY\_VIDEO\_PIC\_HEIGHT表示height；
    * OH\_MD\_KEY\_VIDEO\_STRIDE表示wStride；
    * OH\_MD\_KEY\_VIDEO\_SLICE\_HEIGHT表示hStride。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/Z7oL28PXR7SVJ3SNRMzIUw/zh-cn_image_0000002552798902.png?HW-CC-KV=V1&HW-CC-Date=20260427T234543Z&HW-CC-Expire=86400&HW-CC-Sign=21126352C1533871516FEAE8ACCEB62AC97A72C476633996C7E09F1BFD1464DD)

    添加头文件。

    ```
    1. #include <string.h>
    ```

    使用示例：

    ```
    1. // 源内存区域的宽、高，通过回调函数OnStreamChanged或接口OH_VideoDecoder_GetOutputDescription获取。
    2. struct Rect
    3. {
    4. int32_t width;
    5. int32_t height;
    6. };

    8. struct DstRect // 目标内存区域的宽跨距、高跨距，由开发者自行设置。
    9. {
    10. int32_t wStride;
    11. int32_t hStride;
    12. };
    13. // 源内存区域的宽跨距、高跨距，通过回调函数OnStreamChanged或接口OH_VideoDecoder_GetOutputDescription获取。
    14. struct SrcRect
    15. {
    16. int32_t wStride;
    17. int32_t hStride;
    18. };

    20. Rect rect = {320, 240};
    21. DstRect dstRect = {320, 240};
    22. SrcRect srcRect = {320, 256};
    23. uint8_t* dst = new uint8_t[dstRect.hStride * dstRect.wStride * 3 / 2]; // 目标内存区域的指针。
    24. uint8_t* src = new uint8_t[srcRect.hStride * srcRect.wStride * 3 / 2]; // 源内存区域的指针。
    25. uint8_t* dstTemp = dst;
    26. uint8_t* srcTemp = src;
    27. rect.height = ((rect.height + 1) / 2)  * 2 // 避免height为奇数；
    28. rect.width = ((rect.width + 1) / 2)  * 2 // 避免width为奇数；

    30. // Y 将Y区域的源数据复制到另一个区域的目标数据中。
    31. for (int32_t i = 0; i < rect.height; ++i) {
    32. // 将源数据的一行数据复制到目标数据的一行中。
    33. memcpy(dstTemp, srcTemp, rect.width);
    34. // 更新源数据和目标数据的指针，进行下一行的复制。每更新一次源数据和目标数据的指针都向下移动一个wStride。
    35. dstTemp += dstRect.wStride;
    36. srcTemp += srcRect.wStride;
    37. }
    38. // padding。
    39. // 更新源数据和目标数据的指针，指针都向下移动一个padding。
    40. dstTemp += (dstRect.hStride - rect.height) * dstRect.wStride;
    41. srcTemp += (srcRect.hStride - rect.height) * srcRect.wStride;
    42. rect.height >>= 1;
    43. // UV 将UV区域的源数据复制到另一个区域的目标数据中。
    44. for (int32_t i = 0; i < rect.height; ++i) {
    45. memcpy(dstTemp, srcTemp, rect.width);
    46. dstTemp += dstRect.wStride;
    47. srcTemp += srcRect.wStride;
    48. }

    50. delete[] dst;
    51. dst = nullptr;
    52. delete[] src;
    53. src = nullptr;
    ```

    硬件解码在处理buffer数据时（释放数据前），输出回调开发者收到的AVbuffer是宽、高对齐后的图像数据。

    一般需要获取数据的宽、高、跨距、像素格式来保证解码输出数据被正确的处理。

    具体实现请参考：[Buffer模式](video-decoding.md#buffer模式)的步骤3-调用OH\_VideoDecoder\_RegisterCallback()设置回调函数来获取数据的宽、高、跨距、像素格式。

后续流程（包括刷新、重置、停止和销毁解码器）与Surface模式基本一致，请参考[Surface模式](video-decoding.md#surface模式)的步骤13-16。

## 示例代码

* [基于AVCodec能力的视频编解码](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)
