---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-encoding
title: 视频编码
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > 视频编码
category: harmonyos-guides
scraped_at: 2026-04-29T13:34:40+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:3a0f94b12ae0bffadc15426ea00b2918b79845dad114f89e12f2291e7a0be4c5
---

开发者可以调用本模块的Native API接口，完成视频编码，即将未压缩的视频数据压缩成视频码流。

具体实现可参考[示例工程](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)。

当前支持的编码能力请参考[AVCodec支持的格式](avcodec-support-formats.md#视频编码)。

如果需要对HDRVivid视频进行编码，需要配置MimeType为H265 (OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC)，本功能从API version 11开始支持。

视频编码支持以下能力：

| 支持的能力 | 使用简述 |
| --- | --- |
| 运行时配置编码器参数，包括帧率、码率、QPMin/QPMax | 通过调用OH\_VideoEncoder\_SetParameter()配置， 具体可参考下文中：Surface模式的步骤-9 |
| 随帧设置编码QPMin/QPMax | 通过调用OH\_VideoEncoder\_RegisterParameterCallback()注册随帧参数回调时配置，具体可参考下文中：Surface模式的步骤-4 |
| 分层编码，LTR设置 | 具体可参考：[时域可分层视频编码](video-encoding-temporal-scalability.md) |
| 获取编码每帧平均量化参数（QPAverage）、平方误差（mseValue） | 在配置回调函数OnNewOutputBuffer()时获取，具体可参考下文中：Surface模式的步骤-3 |
| 变分辨率 | 编码器支持输入图像分辨率发生变化。目前仅Surface模式支持且图像的宽、高不能超过OH\_VideoEncoder\_Configure接口配置的宽、高，具体可参考下文中：Surface模式的步骤-5 |

## 限制约束

1. Buffer模式不支持10bit的图像数据。
2. 由于硬件编码器资源有限，每个编码器在使用完毕后都必须调用OH\_VideoEncoder\_Destroy接口来销毁实例并释放资源。
3. Flush，Reset，Stop，Destroy在非回调线程中执行时，会等待所有回调执行完成后，将执行结果返回给开发者。
4. 一旦调用Flush，Reset，Stop接口，会触发系统回收OH\_AVBuffer，开发者不应对之前回调函数获取到的OH\_AVBuffer继续进行操作。
5. Buffer模式和Surface模式使用方式一致的接口，所以只提供了Surface模式的示例。
6. 在Buffer模式下，开发者通过输入回调函数OH\_AVCodecOnNeedInputBuffer获取到OH\_AVBuffer的指针实例后，必须通过调用OH\_VideoEncoder\_PushInputBuffer接口来通知系统该实例已被使用完毕。这样系统才能够将该实例里面的数据进行编码。如果开发者在调用OH\_AVBuffer\_GetNativeBuffer接口时获取到OH\_NativeBuffer指针实例，并且该实例的生命周期超过了当前的OH\_AVBuffer指针实例，那么需要进行一次数据的拷贝操作。在这种情况下，开发者需要自行管理新生成的OH\_NativeBuffer实例的生命周期，确保其正确使用和释放。
7. 为确保系统服务的持续可用性，当检测到应用存在异常实例占用行为时，系统将自动介入。开发者应注意：持续的实例管理不当可能导致进程被终止。

## surface输入与buffer输入

1. 两者的数据来源不同。
2. 两者的适用场景不同：

   * surface输入是指用OHNativeWindow来传递输入数据，可以与其他模块对接，例如相机模块。
   * buffer输入是指有一块预先分配好的内存区域，开发者需要将原始数据拷贝进这块内存区域中。更适用于从文件中读取视频数据等场景。
3. 在接口调用的过程中，两种方式的接口调用方式基本一致，但存在以下差异点：

   * Buffer模式下，开发者通过OH\_VideoEncoder\_PushInputBuffer接口输入数据；Surface模式下，开发者应在编码器就绪前调用OH\_VideoEncoder\_GetSurface接口，获取OHNativeWindow用于传递视频数据。
   * Buffer模式下，开发者通过OH\_AVBuffer中的attr传入结束flag，编码器读取到尾帧后，停止编码；Surface模式下，需要调用OH\_VideoEncoder\_NotifyEndOfStream接口通知编码器输入流结束。

两种模式的开发步骤详细说明请参考：[Surface模式](video-encoding.md#surface模式)和[Buffer模式](video-encoding.md#buffer模式)。

## 状态机调用关系

如下为状态机调用关系图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/1lMuuPJTSI-P2x3J4BhLKw/zh-cn_image_0000002558765044.png?HW-CC-KV=V1&HW-CC-Date=20260429T053438Z&HW-CC-Expire=86400&HW-CC-Sign=C36A2295E7523D14C6A2C3DF7153BE0B6A973064BF4B9A3E1124CA193DDF8F65)

1. 有两种方式可以使编码器进入Initialized状态：

   * 初始创建编码器实例时，编码器处于Initialized状态。
   * 任何状态下，调用OH\_VideoEncoder\_Reset接口，编码器将会移回Initialized状态。
2. Initialized状态下，调用OH\_VideoEncoder\_Configure接口配置编码器，配置成功后编码器进入Configured状态。
3. Configured状态下，调用OH\_VideoEncoder\_Prepare()进入Prepared状态。
4. Prepared状态下，调用OH\_VideoEncoder\_Start接口使编码器进入Executing状态：

   * 处于Executing状态时，调用OH\_VideoEncoder\_Stop接口可以使编码器返回到Prepared状态。
5. 在极少数情况下，编码器可能会遇到错误并进入Error状态。编码器的错误传递，可以通过队列操作返回无效值或者抛出异常：

   * Error状态下，可以调用OH\_VideoEncoder\_Reset接口将编码器移到Initialized状态；或者调用OH\_VideoEncoder\_Destroy接口移动到最后的Released状态。
6. Executing 状态具有三个子状态：Flushed、Running和End-of-Stream：

   * 在调用了OH\_VideoEncoder\_Start接口之后，编码器立即进入Running子状态。
   * 对于处于Executing状态的编码器，可以调用OH\_VideoEncoder\_Flush接口返回到Flushed子状态。
   * 当待处理数据全部传递给编码器后，可以在input buffers队列中为最后一个入队的input buffer中添加[AVCODEC\_BUFFER\_FLAGS\_EOS](../harmonyos-references/capi-native-avbuffer-info-h.md#oh_avcodecbufferflags)标记，遇到这个标记时，编码器会转换为End-of-Stream子状态。在此状态下，编码器不再接受新的输入，但是仍然会继续生成输出，直到输出到达尾帧。
7. 使用完编码器后，必须调用OH\_VideoEncoder\_Destroy接口销毁编码器实例，使编码器进入Released状态。

## 开发指导

详细的API说明请参考[native\_avcodec\_videoencoder.h](../harmonyos-references/capi-native-avcodec-videoencoder-h.md)。

如下为视频编码调用关系图：

* 虚线表示可选。
* 实线表示必选。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/SBRWlT08Shi7sDWJ9qg4ZQ/zh-cn_image_0000002558605388.png?HW-CC-KV=V1&HW-CC-Date=20260429T053438Z&HW-CC-Expire=86400&HW-CC-Sign=0A9A8DD1EED1D56E6EC3E24CA153591EF80793C5D540136F2D0847207499E1A4)

### 在 CMake 脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libnative_media_codecbase.so)
2. target_link_libraries(sample PUBLIC libnative_media_core.so)
3. target_link_libraries(sample PUBLIC libnative_media_venc.so)
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
2. 编码器回调buffer的信息。

   ```
   1. struct CodecBufferInfo {
   2. CodecBufferInfo(uint32_t index, OH_AVBuffer *buffer): index(index), buffer(buffer), isValid(true) {}
   3. CodecBufferInfo(uint32_t index, OH_AVFormat *parameter): index(index), parameter(parameter), isValid(true) {}
   4. // 回调buffer。
   5. OH_AVBuffer *buffer = nullptr;
   6. // Surface模式下，输入回调的随帧参数，需要注册随帧通路后使用。
   7. OH_AVFormat *parameter = nullptr;
   8. // 回调buffer对应的index。
   9. uint32_t index = 0;
   10. // 判断当前buffer信息是否有效。
   11. bool isValid = true;
   12. };
   ```
3. 编码输入输出队列。

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
   11. // 编码器实例指针。
   12. OH_AVCodec *videoEnc = nullptr;
   13. // 编码器同步锁。
   14. std::shared_mutex codecMutex;
   15. // 编码器输入队列。
   16. CodecBufferQueue inQueue;
   17. // 编码器输出队列。
   18. CodecBufferQueue outQueue;
   ```

### Surface模式

参考以下示例代码，可以完成Surface模式下视频编码的全流程，实现异步模式的数据轮转。此处以输入surface数据，编码成H.264格式为例。

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

   开发者可以通过名称或媒体类型创建编码器。示例中的变量说明如下：

   * videoEnc：视频编码器实例的指针；
   * capability：编解码器能力查询实例的指针；
   * OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC：AVC格式视频编解码器。

   创建方式示例如下：

   ```
   1. // 通过codec name创建编码器，应用有特殊需求，比如选择支持某种分辨率规格的编码器，可先查询capability，再根据codec name创建编码器。
   2. OH_AVCapability *capability = OH_AVCodec_GetCapability(OH_AVCODEC_MIMETYPE_VIDEO_AVC, true);
   3. // 创建硬件编码器实例。
   4. OH_AVCapability *capability= OH_AVCodec_GetCapabilityByCategory(OH_AVCODEC_MIMETYPE_VIDEO_AVC, true, HARDWARE);
   5. const char *codecName = OH_AVCapability_GetName(capability);
   6. OH_AVCodec *videoEnc = OH_VideoEncoder_CreateByName(codecName);
   ```

   ```
   1. // 通过MIME TYPE创建编码器。
   2. OH_AVCodec *videoEnc = OH_VideoEncoder_CreateByMime(OH_AVCODEC_MIMETYPE_VIDEO_AVC);
   ```
3. 调用OH\_VideoEncoder\_RegisterCallback()设置回调函数。

   注册回调函数指针集合OH\_AVCodecCallback，包括：

   * OH\_AVCodecOnError 编码器运行错误，返回的错误码详情请参见[OH\_AVCodecOnError](../harmonyos-references/capi-native-avcodec-base-h.md#oh_avcodeconerror)；
   * OH\_AVCodecOnStreamChanged 码流信息变化，如格式变化等；
   * OH\_AVCodecOnNeedInputBuffer 输入回调无作用，开发者通过获取的surface输入数据；
   * OH\_AVCodecOnNewOutputBuffer 运行过程中产生了新的输出数据，即编码完成。

   回调函数的具体实现可参考[示例工程](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)。

   示例如下所示：

   ```
   1. // 设置OH_AVCodecOnError 回调函数，编码异常。
   2. static void OnError(OH_AVCodec *codec, int32_t errorCode, void *userData)
   3. {
   4. // 回调的错误码由开发者判断处理。
   5. (void)codec;
   6. (void)errorCode;
   7. (void)userData;
   8. }
   ```

   ```
   1. // 设置OH_AVCodecOnStreamChanged 回调函数，编码数据流变化
   2. static void OnStreamChanged(OH_AVCodec *codec, OH_AVFormat *format, void *userData)
   3. {
   4. (void)codec;
   5. (void)format;
   6. (void)userData;
   7. // 可通过format获取到分辨率变化后的视频宽、高
   8. OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_PIC_WIDTH, &width);
   9. OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_PIC_HEIGHT, &height);
   10. }
   ```

   ```
   1. // 设置 OH_AVCodecOnNeedInputBuffer 回调函数，编码输入帧送入数据队列。
   2. static void OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   3. {
   4. // Surface模式下，该回调函数无作用，开发者通过获取的surface输入数据。
   5. (void)userData;
   6. (void)index;
   7. (void)buffer;
   8. }
   ```

   ```
   1. // 设置 OH_AVCodecOnNewOutputBuffer 回调函数，编码完成帧送入输出队列。
   2. static void OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   3. {
   4. // 完成帧的数据buffer和对应的index送入outQueue队列。
   5. (void)codec;
   6. (void)userData;
   7. outQueue.Enqueue(std::make_shared<CodecBufferInfo>(index, buffer));
   8. }
   ```

   ```
   1. // 配置异步回调，调用 OH_VideoEncoder_RegisterCallback()接口。
   2. OH_AVCodecCallback cb = {&OnError, &OnStreamChanged, &OnNeedInputBuffer, &OnNewOutputBuffer};
   3. OH_AVErrCode ret = OH_VideoEncoder_RegisterCallback(videoEnc, cb, nullptr); // nullptr:开发者执行回调所依赖的数据userData为空。
   4. if (ret != AV_ERR_OK) {
   5. // 异常处理。
   6. }
   ```

   说明

   在回调函数中，对数据队列进行操作时，需要注意多线程同步的问题。
4. （可选）调用OH\_VideoEncoder\_RegisterParameterCallback()在Configure接口之前注册随帧通路回调。

   详情请参考[时域可分层视频编码](video-encoding-temporal-scalability.md)。

   ```
   1. // 4.1 编码输入参数回调OH_VideoEncoder_OnNeedInputParameter实现
   2. static void OnNeedInputParameter(OH_AVCodec *codec, uint32_t index, OH_AVFormat *parameter, void *userData)
   3. {
   4. // 输入帧parameter对应的index，送入InParameterIndexQueue队列
   5. // 输入帧的数据parameter送入InParameterQueue队列
   6. // 数据处理
   7. // 随帧参数写入
   8. // 配置OH_MD_KEY_VIDEO_ENCODER_QP_MAX 的值应大于等于OH_MD_KEY_VIDEO_ENCODER_QP_MIN
   9. OH_AVFormat_SetIntValue(parameter, OH_MD_KEY_VIDEO_ENCODER_QP_MAX, 30);
   10. OH_AVFormat_SetIntValue(parameter, OH_MD_KEY_VIDEO_ENCODER_QP_MIN, 20);
   11. inQueue.Enqueue(std::make_shared<CodecBufferInfo>(index, parameter));
   12. }

   14. // 4.2 注册随帧参数回调
   15. OH_VideoEncoder_OnNeedInputParameter inParaCb = OnNeedInputParameter;
   16. OH_VideoEncoder_RegisterParameterCallback(videoEnc, inParaCb, NULL); // NULL:用户特定数据userData为空
   ```
5. 调用OH\_VideoEncoder\_Configure()配置编码器。

   详细可配置选项的说明请参考[视频专有键值对](../harmonyos-references/capi-codecbase.md#媒体数据键值对)。

   参数校验规则请参考[OH\_VideoEncoder\_Configure()参考文档](../harmonyos-references/capi-native-avcodec-videoencoder-h.md#oh_videoencoder_configure)。

   参数取值范围可以通过能力查询接口获取，具体示例请参考[获取支持的编解码能力文档](obtain-supported-codecs.md)。

   目前支持的所有格式都必须配置以下选项：视频帧宽度、视频帧高度、视频像素格式。

   ```
   1. // 配置视频帧速率。
   2. double frameRate = 30.0;
   3. // 配置视频YUV值范围标志。
   4. int32_t rangeFlag = 0;
   5. // 配置视频原色。
   6. int32_t primary = static_cast<int32_t>(OH_ColorPrimary::COLOR_PRIMARY_BT709);
   7. // 配置传输特性。
   8. int32_t transfer = static_cast<int32_t>(OH_TransferCharacteristic::TRANSFER_CHARACTERISTIC_BT709);
   9. // 配置最大矩阵系数。
   10. int32_t matrix = static_cast<int32_t>(OH_MatrixCoefficient::MATRIX_COEFFICIENT_IDENTITY);
   11. // 配置编码Profile。
   12. int32_t profile = static_cast<int32_t>(OH_AVCProfile::AVC_PROFILE_HIGH);
   13. // 配置编码比特率模式。
   14. int32_t rateMode = static_cast<int32_t>(OH_BitrateMode::BITRATE_MODE_VBR);
   15. // 配置关键帧的间隔，单位为毫秒。
   16. int32_t iFrameInterval = 1000;
   17. // 配置质量稳定码率因子。
   18. int32_t sqrFactor = 30;
   19. // 配置最大比特率，单位为bps。
   20. int64_t maxBitRate = 20000000;
   21. // 配置比特率，单位为bps。
   22. int64_t bitRate = 5000000;
   23. // 配置编码质量。
   24. int64_t quality = 90;

   26. auto format = std::shared_ptr<OH_AVFormat>(OH_AVFormat_Create(), OH_AVFormat_Destroy);
   27. if (format == nullptr) {
   28. // 异常处理。
   29. }
   30. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_WIDTH, width); // 必须配置。
   31. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_HEIGHT, height); // 必须配置。
   32. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_PIXEL_FORMAT, pixelFormat); // 必须配置，

   34. OH_AVFormat_SetDoubleValue(format.get(), OH_MD_KEY_FRAME_RATE, frameRate);
   35. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_RANGE_FLAG, rangeFlag);
   36. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_COLOR_PRIMARIES, primary);
   37. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_TRANSFER_CHARACTERISTICS, transfer);
   38. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_MATRIX_COEFFICIENTS, matrix);
   39. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_I_FRAME_INTERVAL, iFrameInterval);
   40. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_PROFILE, profile);
   41. // 只有当OH_BitrateMode = BITRATE_MODE_CQ时，才需要配置OH_MD_KEY_QUALITY。
   42. if (rateMode == static_cast<int32_t>(OH_BitrateMode::BITRATE_MODE_CQ)) {
   43. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_QUALITY, quality);
   44. } else if (rateMode == static_cast<int32_t>(OH_BitrateMode::BITRATE_MODE_SQR)) {
   45. // 只有当OH_BitrateMode = BITRATE_MODE_SQR时，才需要配置OH_MD_KEY_MAX_BITRATE和OH_MD_KEY_SQR_FACTOR。
   46. OH_AVFormat_SetLongValue(format.get(), OH_MD_KEY_MAX_BITRATE, maxBitRate);
   47. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_SQR_FACTOR, sqrFactor);
   48. } else if (rateMode == static_cast<int32_t>(OH_BitrateMode::BITRATE_MODE_CBR) ||
   49. rateMode == static_cast<int32_t>(OH_BitrateMode::BITRATE_MODE_VBR)){
   50. OH_AVFormat_SetLongValue(format.get(), OH_MD_KEY_BITRATE, bitRate);
   51. }
   52. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_VIDEO_ENCODE_BITRATE_MODE, rateMode);
   53. OH_AVErrCode ret = OH_VideoEncoder_Configure(videoEnc, format.get());
   54. if (ret != AV_ERR_OK) {
   55. // 异常处理。
   56. }
   ```

   注意

   配置非必须参数错误时，会返回AV\_ERR\_INVALID\_VAL错误码。但OH\_VideoEncoder\_Configure()不会失败，而是使用默认值继续执行。
6. 获取surface。

   获取编码器Surface模式的OHNativeWindow输入，获取surface需要在调用OH\_VideoEncoder\_Prepare接口之前完成。

   ```
   1. // 获取需要输入的surface，以进行编码。
   2. OHNativeWindow *nativeWindow;
   3. OH_AVErrCode ret = OH_VideoEncoder_GetSurface(videoEnc, &nativeWindow);
   4. if (ret != AV_ERR_OK) {
   5. // 异常处理。
   6. }
   7. // 通过OHNativeWindow*变量类型，可通过生产者接口获取待填充数据地址。
   ```

   OHNativeWindow\*变量类型的使用方法请参考图形子系统 [OHNativeWindow](../harmonyos-references/capi-nativewindow.md)。
7. 调用OH\_VideoEncoder\_Prepare()编码器就绪。

   该接口将在编码器运行前进行一些数据的准备工作。

   ```
   1. OH_AVErrCode ret = OH_VideoEncoder_Prepare(videoEnc);
   2. if (ret != AV_ERR_OK) {
   3. // 异常处理。
   4. }
   ```
8. 调用OH\_VideoEncoder\_Start()启动编码器。

   ```
   1. // 配置待编码文件路径。
   2. std::string_view outputFilePath = "/*yourpath*.h264";
   3. std::unique_ptr<std::ofstream> outputFile = std::make_unique<std::ofstream>();
   4. if (outputFile != nullptr) {
   5. outputFile->open(outputFilePath.data(), std::ios::out | std::ios::binary | std::ios::ate);
   6. }
   7. // 启动编码器，开始编码。
   8. OH_AVErrCode ret = OH_VideoEncoder_Start(videoEnc);
   9. if (ret != AV_ERR_OK) {
   10. // 异常处理。
   11. }
   ```
9. （可选）OH\_VideoEncoder\_SetParameter()在运行过程中动态配置编码器参数。

   ```
   1. OH_AVFormat *format = OH_AVFormat_Create();

   3. // 支持动态请求IDR帧
   4. OH_AVFormat_SetIntValue(format, OH_MD_KEY_REQUEST_I_FRAME, true);
   5. // 支持动态重置比特率
   6. int64_t bitRate = 2000000;
   7. OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, bitRate);
   8. // 支持动态重置视频帧速率
   9. double frameRate = 60.0;
   10. OH_AVFormat_SetDoubleValue(format, OH_MD_KEY_FRAME_RATE, frameRate);
   11. // 支持动态设置QP值
   12. // 配置OH_MD_KEY_VIDEO_ENCODER_QP_MAX 的值应大于等于OH_MD_KEY_VIDEO_ENCODER_QP_MIN
   13. OH_AVFormat_SetIntValue(format, OH_MD_KEY_VIDEO_ENCODER_QP_MAX, 30);
   14. OH_AVFormat_SetIntValue(format, OH_MD_KEY_VIDEO_ENCODER_QP_MIN, 20);

   16. int32_t ret = OH_VideoEncoder_SetParameter(videoEnc, format);
   17. if (ret != AV_ERR_OK) {
   18. // 异常处理
   19. }
   20. OH_AVFormat_Destroy(format);
   ```
10. 写入编码图像。

    在之前的第6步中，开发者已经对OH\_VideoEncoder\_GetSurface接口返回的OHNativeWindow\*类型变量进行配置。因为编码所需的数据，由配置的surface进行持续地输入，所以开发者无需对OnNeedInputBuffer回调函数进行处理，也无需使用OH\_VideoEncoder\_PushInputBuffer接口输入数据。

    在变分辨率场景中，此规则也同样适用。
11. （可选）调用OH\_VideoEncoder\_PushInputParameter()通知编码器随帧参数配置输入完成。

    在之前的第4步中，开发者已经注册随帧通路回调。

    以下示例中：

    * index：回调函数OnNeedInputParameter传入的参数，与buffer唯一对应的标识。

    ```
    1. std::shared_ptr<CodecBufferInfo> bufferInfo = inQueue.Dequeue();
    2. std::shared_lock<std::shared_mutex> lock(codecMutex);
    3. if (bufferInfo == nullptr || !bufferInfo->isValid) {
    4. // 异常处理。
    5. }
    6. // 值由开发者决定。
    7. int32_t isIFrame;
    8. OH_AVFormat_SetIntValue(bufferInfo->parameter, OH_MD_KEY_REQUEST_I_FRAME, isIFrame);
    9. OH_AVErrCode ret = OH_VideoEncoder_PushInputParameter(videoEnc, bufferInfo->index);
    10. if (ret != AV_ERR_OK) {
    11. // 异常处理。
    12. }
    ```
12. 调用OH\_VideoEncoder\_NotifyEndOfStream()通知编码器结束。

    ```
    1. // Surface模式：通知视频编码器输入流已结束，只能使用此接口进行通知。
    2. // 不能像Buffer模式中将flag设为AVCODEC_BUFFER_FLAGS_EOS，再调用OH_VideoEncoder_PushInputBuffer接口通知编码器输入结束。
    3. OH_AVErrCode ret = OH_VideoEncoder_NotifyEndOfStream(videoEnc);
    4. if (ret != AV_ERR_OK) {
    5. // 异常处理。
    6. }
    ```
13. 调用OH\_VideoEncoder\_FreeOutputBuffer()释放编码帧。

    以下示例中，bufferInfo的成员变量：

    * index：回调函数OnNewOutputBuffer传入的参数，与buffer唯一对应的标识；
    * buffer：回调函数OnNewOutputBuffer传入的参数，可以通过[OH\_AVBuffer\_GetAddr](../harmonyos-references/capi-native-avbuffer-h.md#oh_avbuffer_getaddr)接口得到共享内存地址的指针；
    * isValid：bufferInfo中存储的buffer实例是否有效。

    ```
    1. std::shared_ptr<CodecBufferInfo> bufferInfo = outQueue.Dequeue();
    2. std::shared_lock<std::shared_mutex> lock(codecMutex);
    3. if (bufferInfo == nullptr || !bufferInfo->isValid) {
    4. // 异常处理。
    5. }
    6. int32_t qpAverage = 20;
    7. double mseValue = 0.0;
    8. OH_AVFormat *format = OH_AVBuffer_GetParameter(bufferInfo->buffer);
    9. OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_ENCODER_QP_AVERAGE, &qpAverage);
    10. OH_AVFormat_GetDoubleValue(format, OH_MD_KEY_VIDEO_ENCODER_MSE, &mseValue);
    11. OH_AVFormat_Destroy(format);
    12. // 获取编码后信息。
    13. OH_AVCodecBufferAttr info;
    14. int32_t ret = OH_AVBuffer_GetBufferAttr(bufferInfo->buffer, &info);
    15. if (ret != AV_ERR_OK) {
    16. // 异常处理。
    17. }
    18. // 将编码完成帧数据buffer写入到对应输出文件中。
    19. outputFile->write(reinterpret_cast<char *>(OH_AVBuffer_GetAddr(bufferInfo->buffer)), info.size);
    20. // 释放已完成写入的数据，index为对应输出队列下标
    21. ret = OH_VideoEncoder_FreeOutputBuffer(videoEnc, bufferInfo->index);
    22. if (ret != AV_ERR_OK) {
    23. // 异常处理。
    24. }
    ```
14. （可选）调用OH\_VideoEncoder\_Flush()刷新编码器。

    调用OH\_VideoEncoder\_Flush接口后，编码器仍处于运行态，但会清除编码器中缓存的输入和输出数据及参数集如H.264格式的PPS/SPS。

    此时需要调用OH\_VideoEncoder\_Start接口重新开始编码。

    ```
    1. std::unique_lock<std::shared_mutex> lock(codecMutex);
    2. // 刷新编码器videoEnc。
    3. OH_AVErrCode flushRet = OH_VideoEncoder_Flush(videoEnc);
    4. if (flushRet != AV_ERR_OK) {
    5. // 异常处理。
    6. }
    7. inQueue.Flush();
    8. outQueue.Flush();
    9. // 重新开始编码。
    10. OH_AVErrCode startRet = OH_VideoEncoder_Start(videoEnc);
    11. if (startRet != AV_ERR_OK) {
    12. // 异常处理。
    13. }
    ```
15. （可选）调用OH\_VideoEncoder\_Reset()重置编码器。

    调用OH\_VideoEncoder\_Reset接口后，编码器将回到初始化的状态，需要调用OH\_VideoEncoder\_Configure接口和OH\_VideoEncoder\_Prepare接口重新配置。

    ```
    1. std::unique_lock<std::shared_mutex> lock(codecMutex);
    2. // 重置编码器videoEnc。
    3. OH_AVErrCode resetRet = OH_VideoEncoder_Reset(videoEnc);
    4. if (resetRet != AV_ERR_OK) {
    5. // 异常处理。
    6. }
    7. inQueue.Flush();
    8. outQueue.Flush();
    9. // 重新配置编码器参数。
    10. auto format = std::shared_ptr<OH_AVFormat>(OH_AVFormat_Create(), OH_AVFormat_Destroy);
    11. if (format == nullptr) {
    12. // 异常处理。
    13. }
    14. OH_AVErrCode configRet = OH_VideoEncoder_Configure(videoEnc, format.get());
    15. if (configRet != AV_ERR_OK) {
    16. // 异常处理。
    17. }
    18. // 编码器重新就绪。
    19. OH_AVErrCode prepareRet = OH_VideoEncoder_Prepare(videoEnc);
    20. if (prepareRet != AV_ERR_OK) {
    21. // 异常处理。
    22. }
    ```
16. （可选）调用OH\_VideoEncoder\_Stop()停止编码器。

    调用OH\_VideoEncoder\_Stop接口后，编码器保留了编码实例，释放输入输出buffer。开发者可以直接调用OH\_VideoEncoder\_Start接口继续编码。

    ```
    1. std::unique_lock<std::shared_mutex> lock(codecMutex);
    2. // 终止编码器videoEnc。
    3. OH_AVErrCode ret = OH_VideoEncoder_Stop(videoEnc);
    4. if (ret != AV_ERR_OK) {
    5. // 异常处理。
    6. }
    7. inQueue.Flush();
    8. outQueue.Flush();
    ```
17. 调用OH\_VideoEncoder\_Destroy()销毁编码器实例，释放资源。

    说明

    1. 不能在回调函数中调用；
    2. 执行该步骤之后，需要开发者将videoEnc指向nullptr，防止野指针导致程序错误。

    ```
    1. std::unique_lock<std::shared_mutex> lock(codecMutex);
    2. // 释放nativeWindow实例。
    3. if(nativeWindow != nullptr){
    4. OH_NativeWindow_DestroyNativeWindow(nativeWindow);
    5. nativeWindow = nullptr;
    6. }
    7. // 调用OH_VideoEncoder_Destroy，注销编码器。
    8. OH_AVErrCode ret = AV_ERR_OK;
    9. if (videoEnc != nullptr) {
    10. OH_VideoEncoder_Destroy(videoEnc);
    11. videoEnc = nullptr;
    12. }
    13. inQueue.Flush();
    14. outQueue.Flush();
    ```

### Buffer模式

参考以下示例代码，可以完成Buffer模式下视频编码的全流程，实现异步模式的数据轮转。此处以输入YUV文件，编码成H.264格式为例。

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

   与Surface模式相同，此处不再赘述。

   ```
   1. // 通过codec name创建编码器，应用有特殊需求，比如选择支持某种分辨率规格的编码器，可先查询capability，再根据codec name创建编码器。
   2. OH_AVCapability *capability = OH_AVCodec_GetCapability(OH_AVCODEC_MIMETYPE_VIDEO_AVC, true);
   3. const char *codecName = OH_AVCapability_GetName(capability);
   4. OH_AVCodec *videoEnc = OH_VideoEncoder_CreateByName(codecName);
   ```

   ```
   1. // 通过MIME TYPE创建编码器。
   2. OH_AVCodec *videoEnc = OH_VideoEncoder_CreateByMime(OH_AVCODEC_MIMETYPE_VIDEO_AVC);
   ```
3. 调用OH\_VideoEncoder\_RegisterCallback()设置回调函数。

   注册回调函数指针集合OH\_AVCodecCallback，包括：

   * OH\_AVCodecOnError 编码器运行错误，返回的错误码详情请参见[OH\_AVCodecOnError](../harmonyos-references/capi-native-avcodec-base-h.md#oh_avcodeconerror)；
   * OH\_AVCodecOnStreamChanged 码流信息变化，如格式变化等；
   * OH\_AVCodecOnNeedInputBuffer 运行过程中需要新的输入数据，即编码器已准备好，可以输入YUV/RGB数据；
   * OH\_AVCodecOnNewOutputBuffer 运行过程中产生了新的输出数据，即编码完成。

   开发者可以通过处理该回调报告的信息，确保编码器正常运转。

   回调函数的具体实现可参考[示例工程](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)。

   ```
   1. bool isFirstFrame = true;
   2. int32_t qpAverage = 20;
   3. double mseValue = 0.0;
   ```

   ```
   1. // 编码异常回调OH_AVCodecOnError实现。
   2. static void OnError(OH_AVCodec *codec, int32_t errorCode, void *userData)
   3. {
   4. // 回调的错误码由开发者判断处理。
   5. (void)codec;
   6. (void)errorCode;
   7. (void)userData;
   8. }
   ```

   ```
   1. // 编码数据流变化回调OH_AVCodecOnStreamChanged实现。
   2. static void OnStreamChanged(OH_AVCodec *codec, OH_AVFormat *format, void *userData)
   3. {
   4. // Buffer模式下，该回调函数无作用。
   5. (void)codec;
   6. (void)format;
   7. (void)userData;
   8. }
   ```

   ```
   1. // 编码输入回调OH_AVCodecOnNeedInputBuffer实现。
   2. static void OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   3. {
   4. // 获取视频宽跨距、高跨距。
   5. if (isFirstFrame) {
   6. auto format = std::shared_ptr<OH_AVFormat>(OH_VideoEncoder_GetInputDescription(codec), OH_AVFormat_Destroy);
   7. if (format == nullptr) {
   8. // 异常处理。
   9. }
   10. bool ret = OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_VIDEO_STRIDE, &widthStride) &&
   11. OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_VIDEO_SLICE_HEIGHT, &heightStride);
   12. if (!ret) {
   13. // 异常处理。
   14. }
   15. isFirstFrame = false;
   16. }
   17. // 输入帧的数据buffer和对应的index送入inQueue队列。
   18. (void)codec;
   19. (void)userData;
   20. inQueue.Enqueue(std::make_shared<CodecBufferInfo>(index, buffer));
   21. }
   ```

   ```
   1. // 编码输出回调OH_AVCodecOnNewOutputBuffer实现
   2. static void OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   3. {
   4. // 获取视频帧的平均量化参数，平方误差
   5. OH_AVFormat *format = OH_AVBuffer_GetParameter(buffer);
   6. OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_ENCODER_QP_AVERAGE, &qpAverage);
   7. OH_AVFormat_GetDoubleValue(format, OH_MD_KEY_VIDEO_ENCODER_MSE, &mseValue);
   8. OH_AVFormat_Destroy(format);
   9. // 完成帧的数据buffer和对应的index送入outQueue队列
   10. (void)userData;
   11. outQueue.Enqueue(std::make_shared<CodecBufferInfo>(index, buffer));
   12. }
   ```

   ```
   1. // 配置异步回调，调用OH_VideoEncoder_RegisterCallback接口。
   2. OH_AVCodecCallback cb = {&OnError, &OnStreamChanged, &OnNeedInputBuffer, &OnNewOutputBuffer};
   3. OH_AVErrCode ret = OH_VideoEncoder_RegisterCallback(videoEnc, cb, nullptr);
   4. if (ret != AV_ERR_OK) {
   5. // 异常处理。
   6. }
   ```

   说明

   在回调函数中，对数据队列进行操作时，需要注意多线程同步的问题。
4. 调用OH\_VideoEncoder\_Configure()配置编码器。

   与Surface模式相同，此处不再赘述。

   ```
   1. auto format = std::shared_ptr<OH_AVFormat>(OH_AVFormat_Create(), OH_AVFormat_Destroy);
   2. if (format == nullptr) {
   3. // 异常处理。
   4. }
   5. // 写入format。
   6. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_WIDTH, width); // 必须配置。
   7. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_HEIGHT, height); // 必须配置。
   8. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_PIXEL_FORMAT, pixelFormat); // 必须配置。
   9. // 配置编码器。
   10. OH_AVErrCode ret = OH_VideoEncoder_Configure(videoEnc, format.get());
   11. if (ret != AV_ERR_OK) {
   12. // 异常处理。
   13. }
   ```
5. 调用OH\_VideoEncoder\_Prepare()编码器就绪。

   该接口将在编码器运行前进行一些数据的准备工作。

   ```
   1. OH_AVErrCode ret = OH_VideoEncoder_Prepare(videoEnc);
   2. if (ret != AV_ERR_OK) {
   3. // 异常处理。
   4. }
   ```
6. 调用OH\_VideoEncoder\_Start()启动编码器，进入运行态。

   启动编码器后，回调函数将开始响应事件。所以，需要先配置输入文件、输出文件。

   ```
   1. // 配置待编码文件路径。
   2. std::string_view inputFilePath = "/*yourpath*.yuv";
   3. std::string_view outputFilePath = "/*yourpath*.h264";
   4. std::unique_ptr<std::ifstream> inputFile = std::make_unique<std::ifstream>();
   5. std::unique_ptr<std::ofstream> outputFile = std::make_unique<std::ofstream>();
   6. if (inputFile != nullptr) {
   7. inputFile->open(inputFilePath.data(), std::ios::in | std::ios::binary);
   8. }
   9. if (outputFile != nullptr) {
   10. outputFile->open(outputFilePath.data(), std::ios::out | std::ios::binary | std::ios::ate);
   11. }
   12. // 启动编码器，开始编码。
   13. OH_AVErrCode ret = OH_VideoEncoder_Start(videoEnc);
   14. if (ret != AV_ERR_OK) {
   15. // 异常处理。
   16. }
   ```
7. （可选）在运行过程中动态配置编码器参数。

   ```
   1. OH_AVFormat *format = OH_AVFormat_Create();

   3. // 支持动态请求IDR帧
   4. OH_AVFormat_SetIntValue(format, OH_MD_KEY_REQUEST_I_FRAME, true);
   5. // 支持动态重置比特率
   6. int64_t bitRate = 2000000;
   7. OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, bitRate);
   8. // 支持动态重置视频帧速率
   9. double frameRate = 60.0;
   10. OH_AVFormat_SetDoubleValue(format, OH_MD_KEY_FRAME_RATE, frameRate);

   12. int32_t ret = OH_VideoEncoder_SetParameter(videoEnc, format);
   13. if (ret != AV_ERR_OK) {
   14. // 异常处理
   15. }
   16. OH_AVFormat_Destroy(format);
   ```
8. 调用OH\_VideoEncoder\_PushInputBuffer()写入编码图像。

   送入输入队列进行编码，以下示例中：

   * widthStride: 获取到的buffer数据的宽跨距。
   * heightStride：获取到的buffer数据的高跨距。

   bufferInfo的成员变量：

   * buffer：回调函数OnNeedInputBuffer传入的参数，可以通过[OH\_AVBuffer\_GetAddr](../harmonyos-references/capi-native-avbuffer-h.md#oh_avbuffer_getaddr)接口得到共享内存地址的指针；
   * index：回调函数OnNeedInputBuffer传入的参数，与buffer唯一对应的标识；
   * isValid：bufferInfo中存储的buffer实例是否有效。

   ```
   1. std::shared_ptr<CodecBufferInfo> bufferInfo = inQueue.Dequeue();
   2. std::shared_lock<std::shared_mutex> lock(codecMutex);
   3. if (bufferInfo == nullptr || !bufferInfo->isValid) {
   4. // 异常处理。
   5. }
   6. // 写入图像数据。
   7. int32_t frameSize = 0;
   8. if (widthStride == width && heightStride == height) {
   9. frameSize = width * height * 3 / 2; // NV12像素格式下，每帧数据大小的计算公式
   10. int32_t capacity = OH_AVBuffer_GetCapacity(bufferInfo->buffer);
   11. if (frameSize > capacity) {
   12. // 异常处理。
   13. }
   14. // 处理文件流得到帧的长度，再将需要编码的数据写入到对应index的buffer中。
   15. uint8_t *addr = OH_AVBuffer_GetAddr(bufferInfo->buffer);
   16. if (addr == nullptr) {
   17. // 异常处理。
   18. }
   19. if (inputFile != nullptr && inputFile->is_open()) {
   20. inputFile->read(reinterpret_cast<char *>(addr), frameSize);
   21. }
   22. } else {
   23. // 如果跨距不等于宽，需要开发者按照跨距进行偏移，具体可参考以下示例。
   24. }
   25. // 配置buffer info信息。
   26. OH_AVCodecBufferAttr info;
   27. info.size = frameSize;
   28. info.offset = 0;
   29. // 注意此处和Surface模式不同，pts需要应用填充，可根据预期显示的时间进行计算写入，如：帧数 * 1000000 / frameRate。
   30. info.pts = 0;
   31. // 避免flags随机初始化为AVCODEC_BUFFER_FLAGS_EOS导致使用异常，flags需要赋值如0（普通帧标识）。
   32. info.flags = 0;
   33. OH_AVErrCode setBufferRet = OH_AVBuffer_SetBufferAttr(bufferInfo->buffer, &info);
   34. if (setBufferRet != AV_ERR_OK) {
   35. // 异常处理。
   36. }
   37. // 配置buffer 随帧信息。
   38. // 值由开发者决定。
   39. int32_t isIFrame;
   40. auto parameter = std::shared_ptr<OH_AVFormat>(OH_AVBuffer_GetParameter(bufferInfo->buffer), OH_AVFormat_Destroy);
   41. if (parameter == nullptr) {
   42. // 异常处理。
   43. }
   44. OH_AVFormat_SetIntValue(parameter.get(), OH_MD_KEY_REQUEST_I_FRAME, isIFrame);
   45. OH_AVErrCode parameterRet = OH_AVBuffer_SetParameter(bufferInfo->buffer, parameter.get());
   46. if (parameterRet != AV_ERR_OK) {
   47. // 异常处理。
   48. }
   49. // 送入编码输入队列进行编码，index为对应输入队列的下标。
   50. OH_AVErrCode pushInputRet = OH_VideoEncoder_PushInputBuffer(videoEnc, bufferInfo->index);
   51. if (pushInputRet != AV_ERR_OK) {
   52. // 异常处理。
   53. }
   ```

   对跨距进行偏移，以NV12图像为例，示例如下：

   以NV12图像为例，width、height、wStride、hStride图像排布参考下图：

   * OH\_MD\_KEY\_WIDTH表示width；
   * OH\_MD\_KEY\_HEIGHT表示height；
   * OH\_MD\_KEY\_VIDEO\_STRIDE表示wStride；
   * OH\_MD\_KEY\_VIDEO\_SLICE\_HEIGHT表示hStride。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/QJv59bBGQp2xLqsi1_lhHA/zh-cn_image_0000002589324915.png?HW-CC-KV=V1&HW-CC-Date=20260429T053438Z&HW-CC-Expire=86400&HW-CC-Sign=97DF4676A71FC9960FE57F1B8B6889A28F69CE714737C18B1610ABCF1EC618DA)

   添加头文件。

   ```
   1. #include <string.h>
   ```

   使用示例：

   ```
   1. struct Rect   // 源内存区域的宽、高，由开发者自行设置。
   2. {
   3. int32_t width;
   4. int32_t height;
   5. };

   7. struct DstRect // 目标内存区域的宽跨距、高跨距，通过接口OH_VideoEncoder_GetInputDescription获取。
   8. {
   9. int32_t wStride;
   10. int32_t hStride;
   11. };

   13. struct SrcRect // 源内存区域的宽跨距、高跨距，由开发者自行设置。
   14. {
   15. int32_t wStride;
   16. int32_t hStride;
   17. };

   19. Rect rect = {320, 240};
   20. DstRect dstRect = {320, 256};
   21. SrcRect srcRect = {320, 250};
   22. uint8_t* dst = new uint8_t[dstRect.hStride * dstRect.wStride * 3 / 2]; // 目标内存区域的指针。
   23. uint8_t* src = new uint8_t[srcRect.hStride * srcRect.wStride * 3 / 2]; // 源内存区域的指针。
   24. uint8_t* dstTemp = dst;
   25. uint8_t* srcTemp = src;
   26. rect.height = ((rect.height + 1) / 2)  * 2; // 避免height为奇数。
   27. rect.width = ((rect.width + 1) / 2)  * 2; // 避免width为奇数。

   29. // Y 将Y区域的源数据复制到另一个区域的目标数据中。
   30. for (int32_t i = 0; i < rect.height; ++i) {
   31. // 将源数据的一行数据复制到目标数据的一行中。
   32. memcpy(dstTemp, srcTemp, rect.width);
   33. // 更新源数据和目标数据的指针，进行下一行的复制。每更新一次源数据和目标数据的指针都向下移动一个wStride。
   34. dstTemp += dstRect.wStride;
   35. srcTemp += srcRect.wStride;
   36. }
   37. // padding。
   38. // 更新源数据和目标数据的指针，指针都向下移动一个padding。
   39. dstTemp += (dstRect.hStride - rect.height) * dstRect.wStride;
   40. srcTemp += (srcRect.hStride - rect.height) * srcRect.wStride;
   41. rect.height >>= 1;
   42. // UV 将UV区域的源数据复制到另一个区域的目标数据中。
   43. for (int32_t i = 0; i < rect.height; ++i) {
   44. memcpy(dstTemp, srcTemp, rect.width);
   45. dstTemp += dstRect.wStride;
   46. srcTemp += srcRect.wStride;
   47. }

   49. delete[] dst;
   50. dst = nullptr;
   51. delete[] src;
   52. src = nullptr;
   ```

   硬件编码在处理buffer数据时（推送数据前），需要开发者拷贝宽、高对齐后的图像数据到输入回调的AVbuffer中。

   一般需要获取数据的宽、高、跨距、像素格式来保证编码输入数据被正确的处理。

   具体实现请参考：[Buffer模式](video-encoding.md#buffer模式)的步骤3-调用OH\_VideoEncoder\_RegisterCallback接口设置回调函数来获取数据的宽、高、跨距、像素格式。
9. 通知编码器结束。

   在编码过程中，当最后一帧数据被送入编码输入队列时，需要设置bufferInfo的flag标识为AVCODEC\_BUFFER\_FLAGS\_EOS，通知编码器输入结束。

   以下示例中，bufferInfo的成员变量：

   * index：回调函数OnNeedInputBuffer传入的参数，与buffer唯一对应的标识；
   * buffer：回调函数OnNeedInputBuffer传入的参数，可以通过[OH\_AVBuffer\_GetAddr](../harmonyos-references/capi-native-avbuffer-h.md#oh_avbuffer_getaddr)接口得到共享内存地址的指针;
   * isValid：bufferInfo中存储的buffer实例是否有效。

   ```
   1. std::shared_ptr<CodecBufferInfo> bufferInfo = inQueue.Dequeue();
   2. std::shared_lock<std::shared_mutex> lock(codecMutex);
   3. if (bufferInfo == nullptr || !bufferInfo->isValid) {
   4. // 异常处理。
   5. }
   6. // 写入最后一帧图像数据，参考"步骤-8. 写入编码图像"。
   7. // 配置buffer info信息，设置AVCODEC_BUFFER_FLAGS_EOS标识。
   8. OH_AVCodecBufferAttr info;
   9. info.size = frameSize;
   10. info.offset = 0;
   11. // 注意此处和Surface模式不同，pts需要应用填充，可根据预期显示的时间进行计算写入，如：帧数 * 1000000 / frameRate。
   12. info.pts = 0;
   13. info.flags = AVCODEC_BUFFER_FLAGS_EOS;
   14. OH_AVErrCode setBufferRet = OH_AVBuffer_SetBufferAttr(bufferInfo->buffer, &info);
   15. if (setBufferRet != AV_ERR_OK) {
   16. // 异常处理。
   17. }
   18. OH_AVErrCode pushInputRet = OH_VideoEncoder_PushInputBuffer(videoEnc, bufferInfo->index);
   19. if (pushInputRet != AV_ERR_OK) {
   20. // 异常处理。
   21. }
   ```
10. 调用OH\_VideoEncoder\_FreeOutputBuffer()释放编码帧。

    与Surface模式相同，此处不再赘述。

    ```
    1. std::shared_ptr<CodecBufferInfo> bufferInfo = outQueue.Dequeue();
    2. std::shared_lock<std::shared_mutex> lock(codecMutex);
    3. if (bufferInfo == nullptr || !bufferInfo->isValid) {
    4. // 异常处理。
    5. }
    6. // 获取编码后信息。
    7. OH_AVCodecBufferAttr info;
    8. OH_AVErrCode getBufferRet = OH_AVBuffer_GetBufferAttr(bufferInfo->buffer, &info);
    9. if (getBufferRet != AV_ERR_OK) {
    10. // 异常处理。
    11. }
    12. // 将编码完成帧数据buffer写入到对应输出文件中。
    13. uint8_t *addr = OH_AVBuffer_GetAddr(bufferInfo->buffer);
    14. if (addr == nullptr) {
    15. // 异常处理。
    16. }
    17. if (outputFile != nullptr && outputFile->is_open()) {
    18. outputFile->write(reinterpret_cast<char *>(addr), info.size);
    19. }
    20. // 释放已完成写入的数据，index为对应输出队列的下标。
    21. OH_AVErrCode freeOutputRet = OH_VideoEncoder_FreeOutputBuffer(videoEnc, bufferInfo->index);
    22. if (freeOutputRet != AV_ERR_OK) {
    23. // 异常处理。
    24. }
    ```

后续流程（包括刷新、重置、停止和销毁编码器）与Surface模式一致，请参考[Surface模式](video-encoding.md#surface模式)的步骤14-17。
