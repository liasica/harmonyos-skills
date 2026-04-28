---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/synchronous-video-encoding
title: 视频编码同步模式
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > 视频编码同步模式
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:43+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:b6ebf2d6a5d053a908c730ed511db36fbb140736e03ae88905110cc81e9d327b
---

从API version 20开始，支持视频编码同步模式。

开发者可以调用本模块的Native API接口，完成同步模式的视频编码。

具体实现可参考[示例工程](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)。

当前支持的编码能力，请参考[AVCodec支持的格式](avcodec-support-formats.md#视频编码)。

视频编码的限制约束、支持的能力、状态机调用关系请参考[视频编码](video-encoding.md)。

## 适用场景

通常情况下，推荐使用异步模式。若需要主动请求buffer去送帧，则可以采用同步模式。

## 开发指导

详细的API说明请参考[VideoEncoder](../harmonyos-references/capi-native-avcodec-videoencoder-h.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/N2kAMvIoQwOy8gxM6bE95g/zh-cn_image_0000002583438591.png?HW-CC-KV=V1&HW-CC-Date=20260427T234542Z&HW-CC-Expire=86400&HW-CC-Sign=C18035C3E1372A663D5C1280BDD1DCB01F52418A705EE571CC9788E31114548D)

### 在CMake脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libnative_media_codecbase.so)
2. target_link_libraries(sample PUBLIC libnative_media_core.so)
3. target_link_libraries(sample PUBLIC libnative_media_venc.so)
```

说明

上述'sample'字样仅为示例，此处由开发者根据实际工程目录自定义。

### 定义基础结构

本部分示例代码按照C++17标准编写，仅作参考。

1. 添加头文件。

   ```
   1. #include <multimedia/player_framework/native_avcodec_videoencoder.h>
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
   ```
2. 全局变量（仅作参考，可以根据实际情况将其封装到对象中）。

   ```
   1. // 视频帧宽度。
   2. int32_t width = 320;
   3. // 视频帧高度。
   4. int32_t height = 240;
   5. // 视频宽跨距。
   6. int32_t widthStride = 0;
   7. // 视频高跨距。
   8. int32_t heightStride = 0;
   9. // 视频像素格式。
   10. OH_AVPixelFormat pixelFormat = AV_PIXEL_FORMAT_NV12;
   11. // 编码器同步锁。
   12. std::shared_mutex codecMutex;
   13. // 编码器实例指针。
   14. OH_AVCodec *videoEnc = nullptr;
   15. // 编码输出。
   16. bool outputDone = false;
   17. // 编码输入。
   18. bool inputDone = false;
   19. std::unique_ptr<std::ifstream> inFile_;
   ```

### Surface模式

参考以下示例代码，可以完成Surface模式下视频编码的全流程，实现同步模式的数据轮转。此处以输入surface数据，编码成H.264格式为例。

1. 创建编码器实例。

   通过名称创建编码器。示例中的变量说明如下：

   * videoEnc：视频编码器实例的指针。
   * capability：编码器能力查询实例的指针。
   * [OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC](../harmonyos-references/capi-native-avcodec-base-h.md#变量)：AVC格式视频编解码器。

   ```
   1. // 创建硬件编码器实例。
   2. OH_AVCapability *capability= OH_AVCodec_GetCapabilityByCategory(OH_AVCODEC_MIMETYPE_VIDEO_AVC, true, HARDWARE);
   3. const char *name = OH_AVCapability_GetName(capability);
   4. OH_AVCodec *videoEnc = OH_VideoEncoder_CreateByName(name);
   5. if (videoEnc == nullptr) {
   6. printf("create videoEnc failed");
   7. return;
   8. }
   ```
2. 调用OH\_VideoEncoder\_Configure()配置编码器。

   * 详细可配置选项的说明请参考[媒体数据键值对](../harmonyos-references/capi-codecbase.md#媒体数据键值对)。
   * 参数校验规则请参考[OH\_VideoEncoder\_Configure()](../harmonyos-references/capi-native-avcodec-videoencoder-h.md#oh_videoencoder_configure)。
   * 参数取值范围可以通过能力查询接口获取，具体示例请参考[获取支持的编解码能力](obtain-supported-codecs.md)。

   目前支持的所有格式都必须配置以下选项：视频帧宽度、视频帧高度、视频像素格式。

   ```
   1. auto format = std::shared_ptr<OH_AVFormat>(OH_AVFormat_Create(), OH_AVFormat_Destroy);
   2. if (format == nullptr) {
   3. // 异常处理。
   4. }
   5. // 写入format。
   6. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_WIDTH, width); // 必须配置。
   7. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_HEIGHT, height); // 必须配置。
   8. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_PIXEL_FORMAT, pixelFormat);// 必须配置。
   9. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_ENABLE_SYNC_MODE, 1); // 同步模式配置。
   10. // 配置编码器。
   11. OH_AVErrCode ret = OH_VideoEncoder_Configure(videoEnc, format.get());
   12. if (ret != AV_ERR_OK) {
   13. // 异常处理。
   14. }
   ```

   注意

   1. 要使能视频编码同步模式，必须将OH\_MD\_KEY\_ENABLE\_SYNC\_MODE配置为1。
   2. 同步模式在调用OH\_VideoEncoder\_Configure接口前不能调用OH\_VideoEncoder\_RegisterCallback或OH\_VideoEncoder\_RegisterParameterCallback接口，否则为异步模式。
   3. 不支持Surface模式的随帧通路的同步模式。
3. 设置surface。

   示例中的变量说明如下：

   nativeWindow：获取方式请参考[视频编码Surface模式](video-encoding.md#surface模式)的“步骤-6：设置surface”。

   ```
   1. // 获取需要输入的surface，以进行编码。
   2. OH_AVErrCode ret = OH_VideoEncoder_GetSurface(videoEnc, &nativeWindow);
   3. if (ret != AV_ERR_OK) {
   4. // 异常处理。
   5. }
   ```
4. 调用OH\_VideoEncoder\_Prepare()编码器就绪。

   该接口将在编码器运行前进行一些数据的准备工作。

   ```
   1. OH_AVErrCode ret = OH_VideoEncoder_Prepare(videoEnc);
   2. if (ret != AV_ERR_OK) {
   3. // 异常处理。
   4. }
   ```
5. 调用OH\_VideoEncoder\_Start()启动编码器。

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
6. 获取可用buffer并释放编码帧。

   * 调用[OH\_VideoEncoder\_QueryOutputBuffer](../harmonyos-references/capi-native-avcodec-videoencoder-h.md#oh_videoencoder_queryoutputbuffer)接口获取下一个可用的输出缓冲区（buffer）的索引（index）。
   * 根据获取的索引（index），调用[OH\_VideoEncoder\_GetOutputBuffer](../harmonyos-references/capi-native-avcodec-videoencoder-h.md#oh_videoencoder_getoutputbuffer)接口获取对应的缓冲区（buffer）实例。
   * 调用[OH\_VideoEncoder\_FreeOutputBuffer](../harmonyos-references/capi-native-avcodec-videoencoder-h.md#oh_videoencoder_freeoutputbuffer)接口释放编码帧。

   ```
   1. bool EncoderOutput(OH_AVCodec *videoEnc, int64_t timeoutUs)
   2. {
   3. uint32_t index;
   4. std::shared_lock<std::shared_mutex> lock(codecMutex);

   6. OH_AVErrCode ret = OH_VideoEncoder_QueryOutputBuffer(videoEnc, &index, timeoutUs);
   7. switch (ret) {
   8. case AV_ERR_OK: {
   9. OH_AVBuffer *buffer = OH_VideoEncoder_GetOutputBuffer(videoEnc, index);
   10. if (buffer == nullptr) {
   11. // 异常处理。
   12. return false;
   13. }

   15. // 获取编码后信息。
   16. OH_AVCodecBufferAttr info;
   17. OH_AVErrCode getBufferRet = OH_AVBuffer_GetBufferAttr(buffer, &info);
   18. if (getBufferRet != AV_ERR_OK) {
   19. // 异常处理。
   20. return false;
   21. }
   22. if (info.flags & AVCODEC_BUFFER_FLAGS_EOS) {
   23. outputDone = 1;
   24. }

   26. // 将编码完成帧数据buffer写入到对应输出文件中。
   27. uint8_t *addr = OH_AVBuffer_GetAddr(buffer);
   28. if (addr == nullptr) {
   29. // 异常处理。
   30. return false;
   31. }
   32. if (outputFile != nullptr && outputFile->is_open()) {
   33. outputFile->write(reinterpret_cast<char *>(addr), info.size);
   34. }
   35. // 释放已完成写入的数据，index为对应输出队列下标。
   36. OH_AVErrCode freeOutputRet = OH_VideoEncoder_FreeOutputBuffer(videoEnc, index);
   37. if (freeOutputRet != AV_ERR_OK) {
   38. // 异常处理。
   39. return false;
   40. }
   41. break;
   42. }
   43. case AV_ERR_TRY_AGAIN_LATER: {
   44. break;
   45. }
   46. case AV_ERR_STREAM_CHANGED: {
   47. auto format = std::shared_ptr<OH_AVFormat>(OH_VideoEncoder_GetOutputDescription(videoEnc), OH_AVFormat_Destroy);
   48. if (format == nullptr) {
   49. // 异常处理。
   50. }
   51. // 获取新宽高。
   52. bool getIntRet = OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_WIDTH, &width) &&
   53. OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_HEIGHT, &height);
   54. if (!getIntRet) {
   55. // 异常处理。
   56. }
   57. break;
   58. }
   59. default: {
   60. // 异常处理。
   61. return false;
   62. }
   63. }
   64. return true;
   65. }
   ```
7. 编码器出帧处理循环。

   ```
   1. bool result = true;
   2. int64_t timeoutUs = 0; // 单位：微秒（us），负值：无限等待；0：立即退出；正值：等待指定时长后退出。

   4. while (!outputDone && result) {
   5. if (!outputDone ) {
   6. result = EncoderOutput(videoEnc, timeoutUs);
   7. }
   8. }
   ```
8. 调用OH\_VideoEncoder\_NotifyEndOfStream()通知编码器结束。

   ```
   1. // Surface模式：通知视频编码器输入流已结束，只能使用此接口进行通知。
   2. OH_AVErrCode ret = OH_VideoEncoder_NotifyEndOfStream(videoEnc);
   3. if (ret != AV_ERR_OK) {
   4. // 异常处理。
   5. }
   ```
9. （可选）调用OH\_VideoEncoder\_Flush()刷新编码器。

   调用OH\_VideoEncoder\_Flush接口后，编码器仍处于运行态，但会清除编码器中缓存的输入和输出数据及参数集（如H.264格式的PPS/SPS）。此时需要调用OH\_VideoEncoder\_Start接口重新开始编码。

   ```
   1. // 通过codecMutex来避免调用Flush接口，状态切换后，编码线程还在跑会退出循环的问题。
   2. std::unique_lock<std::shared_mutex> lock(codecMutex);
   3. // 刷新编码器videoEnc。
   4. OH_AVErrCode flushRet = OH_VideoEncoder_Flush(videoEnc);
   5. if (flushRet != AV_ERR_OK) {
   6. // 异常处理。
   7. }

   9. // 重新开始编码。
   10. OH_AVErrCode startRet = OH_VideoEncoder_Start(videoEnc);
   11. if (startRet != AV_ERR_OK) {
   12. // 异常处理。
   13. }
   ```
10. （可选）调用OH\_VideoEncoder\_Reset()重置编码器。

    调用OH\_VideoEncoder\_Reset接口后，编码器回到初始化的状态，需要调用接口[OH\_VideoEncoder\_Configure](../harmonyos-references/capi-native-avcodec-videoencoder-h.md#oh_videoencoder_configure)和[OH\_VideoEncoder\_Prepare](../harmonyos-references/capi-native-avcodec-videoencoder-h.md#oh_videoencoder_prepare)重新配置。

    ```
    1. // 重置编码器videoEnc。
    2. std::unique_lock<std::shared_mutex> lock(codecMutex);
    3. OH_AVErrCode resetRet = OH_VideoEncoder_Reset(videoEnc);
    4. if (resetRet != AV_ERR_OK) {
    5. // 异常处理。
    6. }

    8. // 重新配置编码器参数。
    9. auto format = std::shared_ptr<OH_AVFormat>(OH_AVFormat_Create(), OH_AVFormat_Destroy);
    10. if (format == nullptr) {
    11. // 异常处理。
    12. }
    13. OH_AVErrCode configRet = OH_VideoEncoder_Configure(videoEnc, format.get());
    14. if (configRet != AV_ERR_OK) {
    15. // 异常处理。
    16. }

    18. // 编码器重新就绪。
    19. OH_AVErrCode prepareRet = OH_VideoEncoder_Prepare(videoEnc);
    20. if (prepareRet != AV_ERR_OK) {
    21. // 异常处理。
    22. }
    ```

    注意

    编码器回到初始化的状态，调用OH\_VideoEncoder\_Configure接口重新配置编码器参数时，同步模式需要重新配置OH\_MD\_KEY\_ENABLE\_SYNC\_MODE为1，否则为异步模式。
11. （可选）调用OH\_VideoEncoder\_Stop()停止编码器。

    调用OH\_VideoEncoder\_Stop接口后，编码器保留了编码实例，释放输入输出buffer。开发者可以直接调用OH\_VideoEncoder\_Start接口继续编码。

    ```
    1. // 终止编码器videoEnc。
    2. std::unique_lock<std::shared_mutex> lock(codecMutex);
    3. OH_AVErrCode ret = OH_VideoEncoder_Stop(videoEnc);
    4. if (ret != AV_ERR_OK) {
    5. // 异常处理。
    6. }
    ```
12. 调用OH\_VideoEncoder\_Destroy()销毁编码器实例，释放资源。

    ```
    1. // 注销编码器。
    2. std::unique_lock<std::shared_mutex> lock(codecMutex);
    3. OH_AVErrCode ret = AV_ERR_OK;
    4. if (videoEnc != nullptr) {
    5. OH_VideoEncoder_Destroy(videoEnc);
    6. videoEnc = nullptr;
    7. }
    ```

    说明

    执行该步骤之后，需要开发者将videoEnc指向nullptr，防止野指针导致程序错误。

### Buffer模式

参考以下示例代码，可以完成Buffer模式下视频编码的全流程，实现同步模式的数据轮转。此处以输入YUV文件，编码成H.264格式为例。

1. 创建编码器实例。

   与Surface模式相同，此处不再赘述。

   ```
   1. // 通过codecname创建编码器，应用有特殊需求，比如选择支持某种分辨率规格的编码器，可先查询capability，再根据codec name创建编码器。
   2. OH_AVCapability *capability = OH_AVCodec_GetCapability(OH_AVCODEC_MIMETYPE_VIDEO_AVC, true);
   3. const char *name = OH_AVCapability_GetName(capability);
   4. OH_AVCodec *videoEnc = OH_VideoEncoder_CreateByName(name);
   5. if (videoEnc == nullptr) {
   6. printf("create videoEnc failed");
   7. return;
   8. }
   ```
2. 调用OH\_VideoEncoder\_Configure()配置编码器。

   与Surface模式相同，此处不再赘述。

   ```
   1. auto format = std::shared_ptr<OH_AVFormat>(OH_AVFormat_Create(), OH_AVFormat_Destroy);
   2. if (format == nullptr) {
   3. // 异常处理。
   4. }
   5. // 写入format。
   6. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_WIDTH, width); // 必须配置。
   7. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_HEIGHT, height); // 必须配置。
   8. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_PIXEL_FORMAT, pixelFormat);// 必须配置。
   9. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_ENABLE_SYNC_MODE, 1); // 同步模式配置。
   10. // 配置编码器。
   11. OH_AVErrCode ret = OH_VideoEncoder_Configure(videoEnc, format.get());
   12. if (ret != AV_ERR_OK) {
   13. // 异常处理。
   14. }
   ```

   注意

   1. 要使能视频编码同步模式，必须将OH\_MD\_KEY\_ENABLE\_SYNC\_MODE配置为1。
   2. 同步模式在调用OH\_VideoEncoder\_Configure接口前不能调用OH\_VideoEncoder\_RegisterCallback或OH\_VideoEncoder\_RegisterParameterCallback接口，否则为异步模式。
3. 调用OH\_VideoEncoder\_Prepare()编码器就绪。

   该接口将在编码器运行前进行一些数据的准备工作。

   ```
   1. ret = OH_VideoEncoder_Prepare(videoEnc);
   2. if (ret != AV_ERR_OK) {
   3. // 异常处理。
   4. }
   ```
4. 调用OH\_VideoEncoder\_Start()启动编码器。

   配置输入文件、输出文件。

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
5. 获取可用buffer并写入码流至编码器

   * 调用[OH\_VideoEncoder\_QueryInputBuffer](../harmonyos-references/capi-native-avcodec-videoencoder-h.md#oh_videoencoder_queryinputbuffer)接口获取下一个可用的输入缓冲区（buffer）的索引（index）。
   * 根据获取的索引（index），调用[OH\_VideoEncoder\_GetInputBuffer](../harmonyos-references/capi-native-avcodec-videoencoder-h.md#oh_videoencoder_getinputbuffer)接口获取对应的缓冲区（buffer）实例。
   * 将需要编码的数据写入该缓冲区（buffer）后，调用[OH\_VideoEncoder\_PushInputBuffer](../harmonyos-references/capi-native-avcodec-videoencoder-h.md#oh_videoencoder_pushinputbuffer)接口将其送入编码输入队列进行编码。当最后一帧数据被送入编码输入队列时，需要将flag标识成[AVCODEC\_BUFFER\_FLAGS\_EOS](../harmonyos-references/capi-native-avbuffer-info-h.md#oh_avcodecbufferflags)，通知编码器输入结束。

   示例中的变量size、offset、pts、frameData、flags说明与Surface模式相同，此处不再赘述。

   ```
   1. bool EncoderInput(OH_AVCodec *videoEnc, int64_t timeoutUs)
   2. {
   3. uint32_t index;
   4. std::shared_lock<std::shared_mutex> lock(codecMutex);

   6. OH_AVErrCode ret = OH_VideoEncoder_QueryInputBuffer(videoEnc, &index, timeoutUs);
   7. switch (ret) {
   8. case AV_ERR_OK: {
   9. OH_AVBuffer *buffer = OH_VideoEncoder_GetInputBuffer(videoEnc, index);
   10. if (buffer == nullptr) {
   11. // 异常处理。
   12. return false;
   13. }

   15. // 写入图像数据。
   16. int32_t frameSize = 0;
   17. bool isFirstFrame = true;
   18. // 获取视频宽跨距和高跨距。
   19. if (isFirstFrame) {
   20. auto format = std::shared_ptr<OH_AVFormat>(OH_VideoEncoder_GetInputDescription(videoEnc), OH_AVFormat_Destroy);
   21. if (format == nullptr) {
   22. // 异常处理。
   23. }
   24. bool getIntRet = OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_VIDEO_STRIDE, &widthStride) &&
   25. OH_AVFormat_GetIntValue(format.get(), OH_MD_KEY_VIDEO_SLICE_HEIGHT, &heightStride);
   26. if (!getIntRet) {
   27. // 异常处理。
   28. }
   29. isFirstFrame = false;
   30. }
   31. if (widthStride == width && heightStride == height) {
   32. frameSize = width * height * 3 / 2; // NV12像素格式下，每帧数据大小的计算公式。
   33. // 处理文件流得到帧的长度，再将需要编码的数据写入到对应index的buffer中。
   34. uint8_t *addr = OH_AVBuffer_GetAddr(buffer);
   35. if (addr == nullptr) {
   36. // 异常处理
   37. return false;
   38. }
   39. if (inputFile != nullptr && inputFile->is_open()) {
   40. inputFile->read(reinterpret_cast<char *>(addr), frameSize);
   41. }
   42. } else {
   43. // 如果跨距不等于宽，开发者需要按照跨距进行偏移，详情请参考视频编码Buffer模式“步骤-8. 写入编码图像”。
   44. }

   46. // 配置buffer info信息。
   47. OH_AVCodecBufferAttr info;
   48. info.size = frameSize;
   49. info.offset = 0;
   50. // 注意此处和Surface模式不同，pts需要应用填充，可根据预期显示的时间进行计算写入，如：帧数 * 1000000 / frameRate。
   51. info.pts = 0;
   52. // 输入最后一帧数据时，设置AVCODEC_BUFFER_FLAGS_EOS标识。
   53. // info.flags = AVCODEC_BUFFER_FLAGS_EOS;
   54. // 避免flags随机初始化为AVCODEC_BUFFER_FLAGS_EOS导致使用异常，flags需要赋值如0（普通帧标识）。
   55. info.flags = 0;
   56. OH_AVErrCode setBufferRet = OH_AVBuffer_SetBufferAttr(buffer, &info);
   57. if (setBufferRet != AV_ERR_OK) {
   58. // 异常处理。
   59. return false;
   60. }
   61. // 送入编码输入队列进行编码，index为对应输入队列的下标。
   62. OH_AVErrCode pushInputRet = OH_VideoEncoder_PushInputBuffer(videoEnc, index);
   63. if (pushInputRet != AV_ERR_OK) {
   64. // 异常处理。
   65. return false;
   66. }
   67. if (inFile_->eof()) {
   68. inputDone = 1;
   69. }
   70. break;
   71. }
   72. case AV_ERR_TRY_AGAIN_LATER: {
   73. break;
   74. }
   75. default: {
   76. // 异常处理。
   77. return false;
   78. }
   79. }
   80. return true;
   81. }
   ```
6. 获取可用buffer并释放编码帧。

   * 调用[OH\_VideoEncoder\_QueryOutputBuffer](../harmonyos-references/capi-native-avcodec-videoencoder-h.md#oh_videoencoder_queryoutputbuffer)接口获取下一个可用的输出缓冲区（buffer）的索引（index）。
   * 根据获取的索引（index），调用[OH\_VideoEncoder\_GetOutputBuffer](../harmonyos-references/capi-native-avcodec-videoencoder-h.md#oh_videoencoder_getoutputbuffer)接口获取对应的缓冲区（buffer）实例。
   * 调用[OH\_VideoEncoder\_FreeOutputBuffer](../harmonyos-references/capi-native-avcodec-videoencoder-h.md#oh_videoencoder_freeoutputbuffer)接口释放编码帧。

   ```
   1. bool EncoderOutput(OH_AVCodec *videoEnc, int64_t timeoutUs)
   2. {
   3. uint32_t index;
   4. std::shared_lock<std::shared_mutex> lock(codecMutex);

   6. OH_AVErrCode ret = OH_VideoEncoder_QueryOutputBuffer(videoEnc, &index, timeoutUs);
   7. switch (ret) {
   8. case AV_ERR_OK: {
   9. OH_AVBuffer *buffer = OH_VideoEncoder_GetOutputBuffer(videoEnc, index);
   10. if (buffer == nullptr) {
   11. // 异常处理。
   12. return false;
   13. }

   15. // 获取编码后信息。
   16. OH_AVCodecBufferAttr info;
   17. OH_AVErrCode getBufferRet = OH_AVBuffer_GetBufferAttr(buffer, &info);
   18. if (getBufferRet != AV_ERR_OK) {
   19. // 异常处理。
   20. return false;
   21. }
   22. // 将编码完成帧数据buffer写入到对应输出文件中。
   23. uint8_t *addr = OH_AVBuffer_GetAddr(buffer);
   24. if (addr == nullptr) {
   25. // 异常处理
   26. return false;
   27. }
   28. if (outputFile != nullptr && outputFile->is_open()) {
   29. outputFile->write(reinterpret_cast<char *>(addr), info.size);
   30. }
   31. if (info.flags & AVCODEC_BUFFER_FLAGS_EOS) {
   32. outputDone = 1;
   33. }
   34. // 释放已完成处理的信息，index为对应buffer队列的下标。
   35. OH_AVErrCode freeOutputRet = OH_VideoEncoder_FreeOutputBuffer(videoEnc, index);
   36. if (freeOutputRet != AV_ERR_OK) {
   37. // 异常处理。
   38. return false;
   39. }
   40. break;
   41. }
   42. case AV_ERR_TRY_AGAIN_LATER: {
   43. break;
   44. }
   45. case AV_ERR_STREAM_CHANGED: {
   46. break;
   47. }
   48. default: {
   49. // 异常处理。
   50. return false;
   51. }
   52. }
   53. return true;
   54. }
   ```
7. 编码器送帧/出帧处理循环。

   ```
   1. bool result = true;
   2. int64_t timeoutUs = 0; // 单位：微秒（us），负值：无限等待；0：立即退出；正值：等待指定时长后退出。

   4. while (!outputDone && result) {
   5. if (!inputDone) {
   6. result = EncoderInput(videoEnc, timeoutUs);
   7. }
   8. if (!outputDone) {
   9. result = EncoderOutput(videoEnc, timeoutUs);
   10. }
   11. }
   ```

后续流程（包括刷新、重置、停止和销毁编码器）与Surface模式基本一致，请参考[Surface模式](synchronous-video-encoding.md#surface模式)的步骤9-12。
