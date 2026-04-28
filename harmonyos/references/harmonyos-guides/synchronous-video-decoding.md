---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/synchronous-video-decoding
title: 视频解码同步模式
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > 视频解码同步模式
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:45+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:10498c443fd0273530f4f1da2ea815ec9730e8c0f1bc1e99e2992edba7d2107a
---

从API version 20开始，支持视频解码同步模式。

开发者可以调用本模块的Native API接口，完成同步模式的视频解码。

具体实现可参考[示例工程](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)。

当前支持的解码能力，请参考[AVCodec支持的格式](avcodec-support-formats.md#视频解码)。

视频解码的限制约束、支持的能力、状态机调用关系请参考[视频解码](video-decoding.md)。

## 适用场景

通常情况下，推荐使用异步模式。若需要主动请求buffer去送帧，则可以采用同步模式。

## 开发指导

详细的API说明请参考[VideoDecoder](../harmonyos-references/capi-native-avcodec-videodecoder-h.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/D8TacKgqQ6uIKD6fm4X_Sw/zh-cn_image_0000002583438597.png?HW-CC-KV=V1&HW-CC-Date=20260427T234544Z&HW-CC-Expire=86400&HW-CC-Sign=E335855A27AACAD2031E47C55AE6504C0E46EADAFF237CC34F11B42B5503DAEF)

### 在CMake脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libnative_media_codecbase.so)
2. target_link_libraries(sample PUBLIC libnative_media_core.so)
3. target_link_libraries(sample PUBLIC libnative_media_vdec.so)
```

说明

上述'sample'字样仅为示例，此处由开发者根据实际工程目录自定义。

### 定义基础结构

本部分示例代码按照C++17标准编写，仅作参考。

1. 添加头文件。

   ```
   1. #include <multimedia/player_framework/native_avcodec_videodecoder.h>
   2. #include <multimedia/player_framework/native_avcapability.h>
   3. #include <multimedia/player_framework/native_avcodec_base.h>
   4. #include <multimedia/player_framework/native_avformat.h>
   5. #include <multimedia/player_framework/native_avbuffer.h>
   6. #include <multimedia/player_framework/native_averrors.h>
   7. #include <native_buffer/native_buffer.h>
   8. #include <memory>
   9. #include <fstream>
   10. #include <mutex>
   11. #include <shared_mutex>
   12. #include <string.h>
   ```
2. 全局变量（仅作参考，可以根据实际情况将其封装到对象中）。

   ```
   1. // 视频帧宽度。
   2. int32_t width = 320;
   3. // 视频帧高度。
   4. int32_t height = 240;
   5. // 视频像素格式。
   6. OH_AVPixelFormat pixelFormat = AV_PIXEL_FORMAT_NV12;
   7. // 解码器同步锁。
   8. std::shared_mutex codecMutex;
   9. // 解码器实例指针。
   10. OH_AVCodec *videoDec = nullptr;
   11. // 解码输出。
   12. bool outputDone = false;
   13. // 解码输入。
   14. bool inputDone = false;
   15. std::unique_ptr<std::ifstream> inFile_;
   ```

### Surface模式

参考以下示例代码，可以完成Surface模式下视频解码的全流程，实现同步模式的数据轮转。此处以输入H.264码流文件，解码送显输出为例。

1. 创建解码器实例。

   通过名称创建解码器。示例中的变量说明如下：

   * videoDec：视频解码器实例的指针。
   * capability：解码器能力查询实例的指针。
   * OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC：AVC格式视频编解码器。

   ```
   1. // 创建硬件解码器实例。
   2. OH_AVCapability *capability= OH_AVCodec_GetCapabilityByCategory(OH_AVCODEC_MIMETYPE_VIDEO_AVC, false, HARDWARE);
   3. const char *name = OH_AVCapability_GetName(capability);
   4. OH_AVCodec *videoDec = OH_VideoDecoder_CreateByName(name);
   5. if (videoDec == nullptr) {
   6. printf("create videoDec failed");
   7. return;
   8. }
   ```
2. 调用OH\_VideoDecoder\_Configure()配置解码器。

   * 详细可配置选项的说明请参考[媒体数据键值对](../harmonyos-references/capi-codecbase.md#媒体数据键值对)。
   * 参数校验规则请参考[OH\_VideoDecoder\_Configure()](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_configure)。
   * 参数取值范围可以通过能力查询接口获取，具体示例请参考[获取支持的编解码能力](obtain-supported-codecs.md)。

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
   9. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_ENABLE_SYNC_MODE, 1); // 同步模式配置。
   10. // 配置解码器。
   11. OH_AVErrCode ret = OH_VideoDecoder_Configure(videoDec, format.get());
   12. if (ret != AV_ERR_OK) {
   13. // 异常处理。
   14. }
   ```

   注意

   1. 要使能视频解码同步模式，必须将OH\_MD\_KEY\_ENABLE\_SYNC\_MODE配置为1。
   2. 同步模式在调用OH\_VideoDecoder\_Configure接口前不能调用OH\_VideoDecoder\_RegisterCallback接口，否则为异步模式。
3. 设置surface。

   示例中的变量说明如下：

   nativeWindow：获取方式请参考[视频解码Surface模式](video-decoding.md#surface模式)的“步骤-6：设置surface”。

   ```
   1. // 设置surface。
   2. // 配置送显窗口参数。
   3. OH_AVErrCode ret = OH_VideoDecoder_SetSurface(videoDec, nativeWindow);
   4. if (ret != AV_ERR_OK) {
   5. // 异常处理。
   6. }
   ```
4. 调用OH\_VideoDecoder\_Prepare()解码器就绪。

   该接口将在解码器运行前进行一些数据的准备工作。

   ```
   1. OH_AVErrCode ret = OH_VideoDecoder_Prepare(videoDec);
   2. if (ret != AV_ERR_OK) {
   3. // 异常处理。
   4. }
   ```
5. 调用OH\_VideoDecoder\_Start()启动解码器。

   ```
   1. // 启动解码器，开始解码。
   2. OH_AVErrCode ret = OH_VideoDecoder_Start(videoDec);
   3. if (ret != AV_ERR_OK) {
   4. // 异常处理。
   5. }
   ```
6. 获取可用buffer并写入码流至解码器。

   * 调用[OH\_VideoDecoder\_QueryInputBuffer](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_queryinputbuffer)接口获取下一个可用的输入缓冲区（buffer）的索引（index）。
   * 根据获取的索引（index），调用[OH\_VideoDecoder\_GetInputBuffer](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_getinputbuffer)接口获取对应的缓冲区（buffer）实例。
   * 将待解码数据写入该缓冲区（buffer）后，调用[OH\_VideoDecoder\_PushInputBuffer](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_pushinputbuffer)接口提交至解码器进行解码。当所有待处理数据全部传递给解码器后，需要将flag标识成AVCODEC\_BUFFER\_FLAGS\_EOS，通知解码器输入结束。

   送入输入队列进行解码，示例中的变量说明如下：

   * size、offset、pts、frameData：输入尺寸、偏移量、时间戳、帧数据等字段信息，获取方式可以参考[媒体数据解析](audio-video-demuxer.md#开发步骤)“步骤-9：开始解封装，循环获取sample”。
   * flags：缓冲区标记的类别，请参考[OH\_AVCodecBufferFlags](../harmonyos-references/capi-native-avbuffer-info-h.md#oh_avcodecbufferflags)。

   ```
   1. bool DecoderInput(OH_AVCodec *videoDec, int64_t timeoutUs)
   2. {
   3. uint32_t index;
   4. std::shared_lock<std::shared_mutex> lock(codecMutex);

   6. OH_AVErrCode ret = OH_VideoDecoder_QueryInputBuffer(videoDec, &index, timeoutUs);
   7. switch (ret) {
   8. case AV_ERR_OK: {
   9. OH_AVBuffer *buffer = OH_VideoDecoder_GetInputBuffer(videoDec, index);
   10. if (buffer == nullptr) {
   11. // 异常处理。
   12. return false;
   13. }
   14. // 写入码流数据。
   15. uint8_t *addr = OH_AVBuffer_GetAddr(buffer);
   16. if (addr == nullptr) {
   17. // 异常处理。
   18. return false;
   19. }
   20. // buffer数据填充。
   21. int32_t capacity = OH_AVBuffer_GetCapacity(buffer);
   22. if (size > capacity) {
   23. // 异常处理。
   24. }
   25. memcpy(addr, frameData, size);

   27. OH_AVCodecBufferAttr info;
   28. // buffer属性配置。
   29. // 配置帧数据的输入尺寸、偏移量、时间戳等字段信息。
   30. info.size = size;
   31. info.offset = offset;
   32. info.pts = pts;
   33. if (inFile_->eof()) {
   34. info.flags = AVCODEC_BUFFER_FLAGS_EOS;
   35. } else {
   36. info.flags = flags;
   37. }
   38. OH_AVErrCode setBufferRet = OH_AVBuffer_SetBufferAttr(buffer, &info);
   39. if (setBufferRet != AV_ERR_OK) {
   40. // 异常处理。
   41. return false;
   42. }
   43. OH_AVErrCode pushInputRet = OH_VideoDecoder_PushInputBuffer(videoDec, index);
   44. if (pushInputRet != AV_ERR_OK) {
   45. // 异常处理。
   46. return false;
   47. }
   48. if (inFile_->eof()) {
   49. inputDone = 1;
   50. }
   51. break;
   52. }
   53. case AV_ERR_TRY_AGAIN_LATER: {
   54. break;
   55. }
   56. default: {
   57. // 异常处理。
   58. return false;
   59. }
   60. }
   61. return true;
   62. }
   ```
7. 获取可用buffer显示并释放解码帧。

   * 调用[OH\_VideoDecoder\_QueryOutputBuffer](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_queryoutputbuffer)接口获取下一个可用的输出缓冲区（buffer）的索引（index）。
   * 根据获取的索引（index），调用[OH\_VideoDecoder\_GetOutputBuffer](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_getoutputbuffer)接口获取对应的缓冲区（buffer）实例。
   * 根据开发者设置的isRender标志决定后续操作：若无需送显，则调用[OH\_VideoDecoder\_FreeOutputBuffer](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_freeoutputbuffer)接口释放解码帧。若需送显，则可调用[OH\_VideoDecoder\_RenderOutputBuffer](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_renderoutputbuffer)接口显示并自动释放解码帧，或调用[OH\_VideoDecoder\_RenderOutputBufferAtTime](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_renderoutputbufferattime)接口在指定时间点显示并释放解码帧。

   ```
   1. bool DecoderOutput(OH_AVCodec *videoDec, int64_t timeoutUs)
   2. {
   3. uint32_t index;
   4. std::shared_lock<std::shared_mutex> lock(codecMutex);

   6. OH_AVErrCode ret = OH_VideoDecoder_QueryOutputBuffer(videoDec, &index, timeoutUs);
   7. switch (ret) {
   8. case AV_ERR_OK: {
   9. OH_AVBuffer *buffer = OH_VideoDecoder_GetOutputBuffer(videoDec, index);
   10. if (buffer == nullptr) {
   11. // 异常处理。
   12. return false;
   13. }

   15. // 获取解码后信息。
   16. OH_AVCodecBufferAttr info;
   17. OH_AVErrCode getBufferRet = OH_AVBuffer_GetBufferAttr(buffer, &info);
   18. if (getBufferRet != AV_ERR_OK) {
   19. // 异常处理。
   20. return false;
   21. }
   22. if (info.flags & AVCODEC_BUFFER_FLAGS_EOS) {
   23. outputDone = 1;
   24. }

   26. // 解码输出数据处理。
   27. // 值由开发者决定。
   28. bool isRender;
   29. bool isNeedRenderAtTime;
   30. OH_AVErrCode result = AV_ERR_OK;
   31. if (isRender) {
   32. // 显示并释放已完成处理的信息，index为对应buffer队列的下标。
   33. if (isNeedRenderAtTime){
   34. // 获取系统绝对时间，renderTimestamp由开发者结合业务指定显示时间。
   35. int64_t renderTimestamp =
   36. std::chrono::duration_cast<std::chrono::nanoseconds>(std::chrono::high_resolution_clock::now().time_since_epoch()).count();
   37. result = OH_VideoDecoder_RenderOutputBufferAtTime(videoDec, index, renderTimestamp);
   38. } else {
   39. result = OH_VideoDecoder_RenderOutputBuffer(videoDec, index);
   40. }
   41. } else {
   42. // 释放已完成处理的信息。
   43. result = OH_VideoDecoder_FreeOutputBuffer(videoDec, index);
   44. }
   45. if (result != AV_ERR_OK) {
   46. // 异常处理。
   47. return false;
   48. }
   49. break;
   50. }
   51. case AV_ERR_TRY_AGAIN_LATER: {
   52. break;
   53. }
   54. case AV_ERR_STREAM_CHANGED: {
   55. auto format = std::shared_ptr<OH_AVFormat>(OH_VideoDecoder_GetOutputDescription(videoDec), OH_AVFormat_Destroy);
   56. if (format == nullptr) {
   57. // 异常处理。
   58. }
   59. // 获取新宽高。
   60. bool getIntRet = OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_VIDEO_PIC_WIDTH, &width) &&
   61. OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_VIDEO_PIC_HEIGHT, &height);
   62. if (!getIntRet) {
   63. // 异常处理。
   64. }
   65. break;
   66. }
   67. default: {
   68. // 异常处理。
   69. return false;
   70. }
   71. }
   72. return true;
   73. }
   ```
8. 解码器送帧/出帧处理循环。

   ```
   1. bool result = true;
   2. int64_t timeoutUs = 0; // 单位：微秒（us），负值：无限等待；0：立即退出；正值：指定时间后结束后退出。

   4. while (!outputDone && result) {
   5. if (!inputDone) {
   6. result = DecoderInput(videoDec, timeoutUs);
   7. }
   8. if (!outputDone) {
   9. result = DecoderOutput(videoDec, timeoutUs);
   10. }
   11. }
   ```
9. （可选）调用OH\_VideoDecoder\_Flush()刷新解码器。

   调用OH\_VideoDecoder\_Flush接口后，解码器仍处于运行态，但会清除解码器中缓存的输入和输出数据及参数集（如H.264格式的PPS/SPS）。此时需要调用OH\_VideoDecoder\_Start接口重新开始解码。

   ```
   1. // 通过codecMutex来避免调用Flush接口，状态切换后，解码线程还在跑会退出循环的问题。
   2. std::unique_lock<std::shared_mutex> lock(codecMutex);
   3. // 刷新解码器videoDec。
   4. OH_AVErrCode ret = OH_VideoDecoder_Flush(videoDec);
   5. if (ret != AV_ERR_OK) {
   6. // 异常处理。
   7. }

   9. // 重新开始解码。
   10. ret = OH_VideoDecoder_Start(videoDec);
   11. if (ret != AV_ERR_OK) {
   12. // 异常处理。
   13. }
   ```
10. （可选）调用OH\_VideoDecoder\_Reset()重置解码器。

    调用OH\_VideoDecoder\_Reset接口后，解码器回到初始化的状态，需要调用接口[OH\_VideoDecoder\_Configure](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_configure)、[OH\_VideoDecoder\_SetSurface](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_setsurface)和[OH\_VideoDecoder\_Prepare](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_prepare)重新配置。

    ```
    1. // 重置解码器videoDec。
    2. std::unique_lock<std::shared_mutex> lock(codecMutex);
    3. OH_AVErrCode resetRet = OH_VideoDecoder_Reset(videoDec);
    4. if (resetRet != AV_ERR_OK) {
    5. // 异常处理。
    6. }

    8. // 重新配置解码器参数。
    9. auto format = std::shared_ptr<OH_AVFormat>(OH_AVFormat_Create(), OH_AVFormat_Destroy);
    10. if (format == nullptr) {
    11. // 异常处理。
    12. }
    13. OH_AVErrCode configRet = OH_VideoDecoder_Configure(videoDec, format.get());
    14. if (configRet != AV_ERR_OK) {
    15. // 异常处理。
    16. }

    18. // Surface模式需要重新配置surface，而Buffer模式不需要配置surface。
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

    注意

    解码器回到初始化的状态，调用OH\_VideoDecoder\_Configure接口重新配置解码器参数时，同步模式需要重新配置OH\_MD\_KEY\_ENABLE\_SYNC\_MODE为1，否则为异步模式。
11. （可选）调用OH\_VideoDecoder\_Stop()停止解码器。

    调用OH\_VideoDecoder\_Stop()后，解码器保留解码实例，释放输入输出buffer。

    ```
    1. // 终止解码器videoDec。
    2. std::unique_lock<std::shared_mutex> lock(codecMutex);
    3. OH_AVErrCode ret = OH_VideoDecoder_Stop(videoDec);
    4. if (ret != AV_ERR_OK) {
    5. // 异常处理。
    6. }
    ```
12. 调用OH\_VideoDecoder\_Destroy()销毁解码器实例，释放资源。

    ```
    1. // 调用OH_VideoDecoder_Destroy，注销解码器。
    2. std::unique_lock<std::shared_mutex> lock(codecMutex);
    3. OH_AVErrCode ret = AV_ERR_OK;
    4. if (videoDec != nullptr) {
    5. OH_VideoDecoder_Destroy(videoDec);
    6. videoDec = nullptr;
    7. }
    ```

    说明

    执行该步骤之后，需要开发者将videoDec指向nullptr，防止野指针导致程序错误。

### Buffer模式

参考以下示例代码，可以完成Buffer模式下视频解码的全流程，实现同步模式的数据轮转。此处以输入H.264码流文件，解码成YUV文件为例。

1. 创建解码器实例。

   与Surface模式相同，此处不再赘述。

   ```
   1. // 通过codecname创建解码器，应用有特殊需求，比如选择支持某种分辨率规格的解码器，可先查询capability，再根据codec name创建解码器。
   2. OH_AVCapability *capability = OH_AVCodec_GetCapability(OH_AVCODEC_MIMETYPE_VIDEO_AVC, false);
   3. const char *name = OH_AVCapability_GetName(capability);
   4. OH_AVCodec *videoDec = OH_VideoDecoder_CreateByName(name);
   5. if (videoDec == nullptr) {
   6. printf("create videoDec failed");
   7. return;
   8. }
   ```
2. 调用OH\_VideoDecoder\_Configure()配置解码器。

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
   9. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_ENABLE_SYNC_MODE, 1); // 同步模式配置。
   10. // 配置解码器。
   11. OH_AVErrCode ret = OH_VideoDecoder_Configure(videoDec, format.get());
   12. if (ret != AV_ERR_OK) {
   13. // 异常处理。
   14. }
   ```

   注意

   1. 要使能视频解码同步模式，必须将OH\_MD\_KEY\_ENABLE\_SYNC\_MODE配置为1。
   2. 同步模式在调用OH\_VideoDecoder\_Configure接口前不能调用OH\_VideoDecoder\_RegisterCallback接口，否则为异步模式。
3. 调用OH\_VideoDecoder\_Prepare()解码器就绪。

   该接口将在解码器运行前进行一些数据的准备工作。

   ```
   1. OH_AVErrCode ret = OH_VideoDecoder_Prepare(videoDec);
   2. if (ret != AV_ERR_OK) {
   3. // 异常处理。
   4. }
   ```
4. 调用OH\_VideoDecoder\_Start()启动解码器。

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
5. 获取可用buffer并写入码流至解码器。

   * 调用[OH\_VideoDecoder\_QueryInputBuffer](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_queryinputbuffer)接口获取下一个可用的输入缓冲区（buffer）的索引（index）。
   * 根据获取的索引（index），调用[OH\_VideoDecoder\_GetInputBuffer](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_getinputbuffer)接口获取对应的缓冲区（buffer）实例。
   * 将待解码数据写入该缓冲区（buffer）后，调用[OH\_VideoDecoder\_PushInputBuffer](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_pushinputbuffer)接口提交至解码器进行解码。当所有待处理数据全部传递给解码器后，需要将flag标识成AVCODEC\_BUFFER\_FLAGS\_EOS，通知解码器输入结束。

   示例中的变量size、offset、pts、frameData、flags说明与Surface模式相同，此处不再赘述。

   ```
   1. bool DecoderInput(OH_AVCodec *videoDec, int64_t timeoutUs)
   2. {
   3. uint32_t index;
   4. std::shared_lock<std::shared_mutex> lock(codecMutex);

   6. OH_AVErrCode ret = OH_VideoDecoder_QueryInputBuffer(videoDec, &index, timeoutUs);
   7. switch (ret) {
   8. case AV_ERR_OK: {
   9. OH_AVBuffer *buffer = OH_VideoDecoder_GetInputBuffer(videoDec, index);
   10. if (buffer == nullptr) {
   11. // 异常处理。
   12. return false;
   13. }
   14. // 写入码流数据。
   15. uint8_t *addr = OH_AVBuffer_GetAddr(buffer);
   16. if (addr == nullptr) {
   17. // 异常处理。
   18. return false;
   19. }
   20. // buffer数据填充。
   21. int32_t capacity = OH_AVBuffer_GetCapacity(buffer);
   22. if (size > capacity) {
   23. // 异常处理。
   24. }
   25. memcpy(addr, frameData, size);

   27. OH_AVCodecBufferAttr info;
   28. // buffer属性配置。
   29. // 配置帧数据的输入尺寸、偏移量、时间戳等字段信息。
   30. info.size = size;
   31. info.offset = offset;
   32. info.pts = pts;
   33. if (inFile_->eof()) {
   34. info.flags = AVCODEC_BUFFER_FLAGS_EOS;
   35. } else {
   36. info.flags = flags;
   37. }
   38. OH_AVErrCode setBufferRet = OH_AVBuffer_SetBufferAttr(buffer, &info);
   39. if (setBufferRet != AV_ERR_OK) {
   40. // 异常处理。
   41. return false;
   42. }
   43. OH_AVErrCode pushInputRet = OH_VideoDecoder_PushInputBuffer(videoDec, index);
   44. if (pushInputRet != AV_ERR_OK) {
   45. // 异常处理。
   46. return false;
   47. }
   48. if (inFile_->eof()) {
   49. inputDone = 1;
   50. }
   51. break;
   52. }
   53. case AV_ERR_TRY_AGAIN_LATER: {
   54. break;
   55. }
   56. default: {
   57. // 异常处理。
   58. return false;
   59. }
   60. }
   61. return true;
   62. }
   ```
6. 获取可用buffer并释放解码帧。

   * 调用[OH\_VideoDecoder\_QueryOutputBuffer](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_queryoutputbuffer)接口获取下一个可用的输出缓冲区（buffer）的索引（index）。
   * 根据获取的索引（index），调用[OH\_VideoDecoder\_GetOutputBuffer](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_getoutputbuffer)接口获取对应的缓冲区（buffer）实例。
   * 调用[OH\_VideoDecoder\_FreeOutputBuffer](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_freeoutputbuffer)接口释放解码帧。

   ```
   1. bool DecoderOutput(OH_AVCodec *videoDec, int64_t timeoutUs)
   2. {
   3. uint32_t index;
   4. int32_t cropTop = 0;
   5. int32_t cropBottom = 0;
   6. int32_t cropLeft = 0;
   7. int32_t cropRight = 0;
   8. int32_t widthStride = 0;
   9. int32_t heightStride = 0;
   10. std::shared_lock<std::shared_mutex> lock(codecMutex);

   12. OH_AVErrCode ret = OH_VideoDecoder_QueryOutputBuffer(videoDec, &index, timeoutUs);
   13. switch (ret) {
   14. case AV_ERR_OK: {
   15. OH_AVBuffer *buffer = OH_VideoDecoder_GetOutputBuffer(videoDec, index);
   16. if (buffer == nullptr) {
   17. // 异常处理。
   18. return false;
   19. }

   21. // 获取解码后信息。
   22. OH_AVCodecBufferAttr info;
   23. OH_AVErrCode getBufferRet = OH_AVBuffer_GetBufferAttr(buffer, &info);
   24. if (getBufferRet != AV_ERR_OK) {
   25. // 异常处理。
   26. return false;
   27. }
   28. if (info.flags & AVCODEC_BUFFER_FLAGS_EOS) {
   29. outputDone = 1;
   30. }

   32. // 释放已完成处理的信息，index为对应buffer队列的下标。
   33. OH_AVErrCode freeOutputRet = OH_VideoDecoder_FreeOutputBuffer(videoDec, index);
   34. if (freeOutputRet != AV_ERR_OK) {
   35. // 异常处理。
   36. return false;
   37. }
   38. break;
   39. }
   40. case AV_ERR_TRY_AGAIN_LATER: {
   41. break;
   42. }
   43. case AV_ERR_STREAM_CHANGED: {
   44. auto format = std::shared_ptr<OH_AVFormat>(OH_VideoDecoder_GetOutputDescription(videoDec), OH_AVFormat_Destroy);
   45. if (format == nullptr) {
   46. // 异常处理。
   47. }
   48. // 获取到变化后的视频宽、高、跨距。
   49. bool getIntRet = OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_VIDEO_PIC_WIDTH, &width) &&
   50. OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_VIDEO_PIC_HEIGHT, &height) &&
   51. OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_VIDEO_STRIDE, &widthStride) &&
   52. OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_VIDEO_SLICE_HEIGHT, &heightStride) &&
   53. // 获取裁剪矩形信息可选。
   54. OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_VIDEO_CROP_TOP, &cropTop) &&
   55. OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_VIDEO_CROP_BOTTOM, &cropBottom) &&
   56. OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_VIDEO_CROP_LEFT, &cropLeft) &&
   57. OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_VIDEO_CROP_RIGHT, &cropRight);
   58. if (!getIntRet) {
   59. // 异常处理。
   60. }
   61. break;
   62. }
   63. default: {
   64. // 异常处理。
   65. return false;
   66. }
   67. }
   68. return true;
   69. }
   ```
7. 解码器送帧/出帧处理循环。

   ```
   1. bool result = true;
   2. int64_t timeoutUs = 0; // 单位：微秒（us），负值：无限等待；0：立即退出；正值：等待指定时长后退出。

   4. while (!outputDone && result) {
   5. if (!inputDone) {
   6. result = DecoderInput(videoDec, timeoutUs);
   7. }
   8. if (!outputDone) {
   9. result = DecoderOutput(videoDec, timeoutUs);
   10. }
   11. }
   ```

后续流程（包括刷新、重置停止和销毁解码器）与Surface模式基本一致，请参考[Surface模式](synchronous-video-decoding.md#surface模式)的步骤9-12。
