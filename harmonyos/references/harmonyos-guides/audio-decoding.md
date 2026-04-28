---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-decoding
title: 音频解码
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > 音频解码
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:42+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:66d75c9a96c3fa6b5c1d7487f7a37d69af77cca789d5299684db7361e527bc47
---

开发者可以调用本模块的Native API接口，完成音频解码，即将媒体数据解码为PCM码流。

当前支持的解码能力请参考[AVCodec支持的格式](avcodec-support-formats.md#音频解码)。

**适用场景**

* 音频播放

  在播放音频之前，需要先解码音频，再将数据输送到硬件扬声器播放。
* 音频渲染

  在对音频文件进行音效处理之前，需要先解码再由音频处理模块进行音频渲染。
* 音频编辑

  音频编辑（如调整单个声道的播放倍速等）需要基于PCM码流进行，所以需要先将音频文件解码。

说明

通过MP3音频编码流程生成的码流无法直接通过MP3音频解码流程进行解码。建议通过（PCM码流->MP3音频编码->封装->解封装->MP3音频解码）流程进行。

## 开发指导

详细的API说明请参考[native\_avcodec\_audiocodec.h](../harmonyos-references/capi-native-avcodec-audiocodec-h.md)。

参考以下示例代码，完成音频解码的全流程，包括：创建解码器、设置解码参数（采样率/码率/声道数等）、开始、刷新、重置、销毁资源。

在应用开发过程中，开发者应按一定顺序调用方法，执行对应操作，否则系统可能会抛出异常或产生其他未定义的行为。具体顺序可参考下列开发步骤及对应说明。

如下为音频解码调用关系图：

* 虚线表示可选。
* 实线表示必选。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/kKdbx3JKSgytZ_69IWdhGQ/zh-cn_image_0000002552798892.png?HW-CC-KV=V1&HW-CC-Date=20260427T234541Z&HW-CC-Expire=86400&HW-CC-Sign=3099B519B79CCDA9353CEE07746873AEDF78FEC7AED8CCE0AB1FBD072675EFF8)

### 在 CMake 脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libnative_media_codecbase.so)
2. target_link_libraries(sample PUBLIC libnative_media_core.so)
3. target_link_libraries(sample PUBLIC libnative_media_acodec.so)
```

说明

上述'sample'字样仅为示例，此处由开发者根据实际工程目录自定义。

### 开发步骤

1. 添加所需的头文件。

   ```
   1. #include <multimedia/player_framework/native_avcodec_audiocodec.h>
   2. #include <multimedia/native_audio_channel_layout.h>
   3. #include <multimedia/player_framework/native_avcapability.h>
   4. #include <multimedia/player_framework/native_avcodec_base.h>
   5. #include <multimedia/player_framework/native_avformat.h>
   6. #include <multimedia/player_framework/native_avbuffer.h>
   ```
2. 创建解码器实例对象，OH\_AVCodec \*为解码器实例指针。

   应用可以通过媒体类型或编解码器名称创建解码器。

   方法一：通过 Mimetype 创建解码器。

   ```
   1. // 设置判定是否为编码；设置false表示当前是解码。
   2. bool isEncoder = false;
   3. // 通过 Mimetype 创建解码器。
   4. OH_AVCodec *audioDec_ = OH_AudioCodec_CreateByMime(OH_AVCODEC_MIMETYPE_AUDIO_AAC, isEncoder);
   ```

   方法二：通过 codec name 创建解码器。

   ```
   1. // 通过 codec name 创建解码器。
   2. OH_AVCapability *capability = OH_AVCodec_GetCapability(OH_AVCODEC_MIMETYPE_AUDIO_AAC, false);
   3. const char *name = OH_AVCapability_GetName(capability);
   4. OH_AVCodec *audioDec_ = OH_AudioCodec_CreateByName(name);
   ```

   添加头文件和命名空间:

   ```
   1. #include <mutex>
   2. #include <queue>
   3. // c++标准库命名空间。
   4. using namespace std;
   ```

   示例代码：

   ```
   1. // 初始化队列。
   2. class ADecBufferSignal {
   3. public:
   4. std::mutex inMutex_;
   5. std::mutex outMutex_;
   6. std::mutex startMutex_;
   7. std::condition_variable inCond_;
   8. std::condition_variable outCond_;
   9. std::condition_variable startCond_;
   10. std::queue<uint32_t> inQueue_;
   11. std::queue<uint32_t> outQueue_;
   12. std::queue<OH_AVBuffer *> inBufferQueue_;
   13. std::queue<OH_AVBuffer *> outBufferQueue_;
   14. };
   15. ADecBufferSignal *signal_;
   ```
3. 调用OH\_AudioCodec\_RegisterCallback()注册回调函数。

   注册回调函数指针集合OH\_AVCodecCallback，包括：

   * OH\_AVCodecOnError：解码器运行错误。
   * OH\_AVCodecOnStreamChanged：码流信息变化回调，包括采样率变化、声道数变化、音频采样格式变化，支持检测此变化的解码格式有：Audio Vivid，AAC，FLAC，MP3，VORBIS。(API version 15开始支持)
   * OH\_AVCodecOnNeedInputBuffer：运行过程中需要新的输入数据，即解码器已准备好，可以输入数据。
   * OH\_AVCodecOnNewOutputBuffer：运行过程中产生了新的输出数据，即解码完成。

   开发者可以通过处理该回调报告的信息，确保解码器正常运转。

   注意

   请勿在回调中调用解码器的相关接口或进行耗时操作。

   ```
   1. // OH_AVCodecOnError回调函数的实现。
   2. static void OnError(OH_AVCodec *codec, int32_t errorCode, void *userData)
   3. {
   4. (void)codec;
   5. (void)errorCode;
   6. (void)userData;
   7. }
   8. // OH_AVCodecOnStreamChanged回调函数的实现。
   9. static void OnOutputFormatChanged(OH_AVCodec *codec, OH_AVFormat *format, void *userData)
   10. {
   11. (void)codec;
   12. (void)userData;
   13. // 解码输出参数变化后的回调处理，应用根据实际情况进行处理。
   14. int32_t sampleRate;
   15. int32_t channelCount;
   16. int32_t sampleFormat;
   17. if (OH_AVFormat_GetIntValue(format, OH_MD_KEY_AUD_SAMPLE_RATE, &sampleRate)) {
   18. // 判断采样率是否发生变化，进行对应处理。
   19. }
   20. if (OH_AVFormat_GetIntValue(format, OH_MD_KEY_AUD_CHANNEL_COUNT, &channelCount)) {
   21. // 判断声道数是否发生变化，进行对应处理。
   22. }
   23. if (OH_AVFormat_GetIntValue(format, OH_MD_KEY_AUDIO_SAMPLE_FORMAT, &sampleFormat)) {
   24. // 判断音频采样格式是否发生变化，进行对应处理。
   25. }
   26. }
   27. // OH_AVCodecOnNeedInputBuffer回调函数的实现。
   28. static void OnInputBufferAvailable(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *data, void *userData)
   29. {
   30. (void)codec;
   31. ADecBufferSignal *signal = static_cast<ADecBufferSignal *>(userData);
   32. unique_lock<mutex> lock(signal->inMutex_);
   33. signal->inQueue_.push(index);
   34. signal->inBufferQueue_.push(data);
   35. signal->inCond_.notify_all();
   36. // 解码输入码流送入inBufferQueue_队列。
   37. }
   38. // OH_AVCodecOnNewOutputBuffer回调函数的实现。
   39. static void OnOutputBufferAvailable(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *data, void *userData)
   40. {
   41. (void)codec;
   42. ADecBufferSignal *signal = static_cast<ADecBufferSignal *>(userData);
   43. unique_lock<mutex> lock(signal->outMutex_);
   44. signal->outQueue_.push(index);
   45. signal->outBufferQueue_.push(data);
   46. signal->outCond_.notify_all();
   47. // 将对应输出buffer的 index 送入outQueue_队列。
   48. // 将对应解码完成的数据data送入outBufferQueue_队列。
   49. }
   ```

   配置回调：

   ```
   1. signal_ = new ADecBufferSignal();
   2. OH_AVCodecCallback cb_ = {&OnError, &OnOutputFormatChanged, &OnInputBufferAvailable, &OnOutputBufferAvailable};
   3. // 配置异步回调。
   4. int32_t ret = OH_AudioCodec_RegisterCallback(audioDec_, cb_, signal_);
   5. if (ret != AV_ERR_OK) {
   6. // 异常处理。
   7. }
   ```
4. （可选）OH\_AudioCodec\_SetDecryptionConfig设置解密配置。

   当获取到DRM信息(参考[音视频解封装](audio-video-demuxer.md)开发步骤第4步)后，通过此接口进行解密配置。

   DRM相关接口详见[DRM API文档](../harmonyos-references/capi-drm.md)。

   此接口需在Prepare前调用。

   添加头文件:

   ```
   1. #include <multimedia/drm_framework/native_mediakeysystem.h>
   2. #include <multimedia/drm_framework/native_mediakeysession.h>
   3. #include <multimedia/drm_framework/native_drm_err.h>
   4. #include <multimedia/drm_framework/native_drm_common.h>
   ```

   在 CMake 脚本中链接动态库:

   ```
   1. target_link_libraries(sample PUBLIC libnative_drm.so)
   ```

   使用示例:

   ```
   1. // 根据DRM信息创建指定的DRM系统, 以创建"com.wiseplay.drm"为例。
   2. MediaKeySystem *system = nullptr;
   3. int32_t ret = OH_MediaKeySystem_Create("com.wiseplay.drm", &system);
   4. if (system == nullptr) {
   5. printf("create media key system failed");
   6. return;
   7. }

   9. // 创建解密会话。
   10. MediaKeySession *session = nullptr;
   11. DRM_ContentProtectionLevel contentProtectionLevel = CONTENT_PROTECTION_LEVEL_SW_CRYPTO;
   12. ret = OH_MediaKeySystem_CreateMediaKeySession(system, &contentProtectionLevel, &session);
   13. if (ret != DRM_ERR_OK) {
   14. // 如创建失败，请查看DRM接口文档及日志信息。
   15. printf("create media key session failed.");
   16. return;
   17. }
   18. if (session == nullptr) {
   19. printf("media key session is nullptr.");
   20. return;
   21. }
   22. // 获取许可证请求、设置许可证响应等。
   23. // 设置解密配置, 即将解密会话、安全通路标志(当前音频解密不支持安全通路，应设置为false)设置到解码器中。
   24. bool secureAudio = false;
   25. ret = OH_AudioCodec_SetDecryptionConfig(audioDec_, session, secureAudio);
   ```
5. 调用OH\_AudioCodec\_Configure()配置解码器。

   配置选项key值说明：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/CY3QGzupTTK0TopQkYm_6g/zh-cn_image_0000002552798894.png?HW-CC-KV=V1&HW-CC-Date=20260427T234541Z&HW-CC-Expire=86400&HW-CC-Sign=5A866841DDD022B7A402CD76EC477C33F00885014703CE32C678594908BDBD6B)

   各音频解码类型参数范围说明：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/l7GO19bxTmOBDNpywmzqIg/zh-cn_image_0000002583438589.png?HW-CC-KV=V1&HW-CC-Date=20260427T234541Z&HW-CC-Expire=86400&HW-CC-Sign=7ADB118C653B223782AE1715DAF75A33F00C46095BBD8FF50CBCFB367DFEAC2F)

   从API version 20开始，支持[采样率范围](../harmonyos-references/capi-native-avcapability-h.md#oh_avcapability_getaudiosupportedsamplerateranges)能力查询，以下几种音频解码类型支持对范围内的任意采样率进行解码：

   | 音频解码类型 | 采样率(Hz) |
   | --- | --- |
   | Flac | 8000 ~ 384000 |
   | Vorbis | 8000 ~ 192000 |
   | APE | 1 ~ 2147483647 |

   ```
   1. // 配置音频采样率（必须）。
   2. constexpr uint32_t DEFAULT_SAMPLERATE = 44100;
   3. // 配置音频码率（可选）。
   4. constexpr uint32_t DEFAULT_BITRATE = 32000;
   5. // 配置音频声道数（必须）。
   6. constexpr uint32_t DEFAULT_CHANNEL_COUNT = 2;
   7. // 配置最大输入长度（可选）。
   8. constexpr uint32_t DEFAULT_MAX_INPUT_SIZE = 1152;
   9. // 配置是否为ADTS解码（aac解码时可选）。
   10. constexpr uint32_t DEFAULT_AAC_TYPE = 1;
   11. // 配置划分音频数据块字节数，从API version 22开始支持，仅WMAV1、WMAV2、WMA PRO解码时必须配置。
   12. constexpr int32_t DEFAULT_BLOCK_ALIGN = 1;
   13. OH_AVFormat *format = OH_AVFormat_Create();
   14. // 写入format。
   15. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_SAMPLE_RATE, DEFAULT_SAMPLERATE);
   16. OH_AVFormat_SetIntValue(format, OH_MD_KEY_BITRATE, DEFAULT_BITRATE);
   17. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_CHANNEL_COUNT, DEFAULT_CHANNEL_COUNT);
   18. OH_AVFormat_SetIntValue(format, OH_MD_KEY_MAX_INPUT_SIZE, DEFAULT_MAX_INPUT_SIZE);
   19. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AAC_IS_ADTS, DEFAULT_AAC_TYPE);
   20. OH_AVFormat_SetIntValue(format, OH_MD_KEY_BLOCK_ALIGN, DEFAULT_BLOCK_ALIGN);
   21. // 配置解码器。
   22. int32_t ret = OH_AudioCodec_Configure(audioDec_, format);
   23. if (ret != AV_ERR_OK) {
   24. // 异常处理。
   25. }
   ```
6. 调用OH\_AudioCodec\_Prepare()，解码器就绪。

   ```
   1. int32_t ret = OH_AudioCodec_Prepare(audioDec_);
   2. if (ret != AV_ERR_OK) {
   3. // 异常处理。
   4. }
   ```
7. 调用OH\_AudioCodec\_Start()启动解码器，进入运行态。

   添加头文件：

   ```
   1. #include <fstream>
   ```

   使用示例：

   ```
   1. ifstream inputFile_;
   2. ofstream outFile_;

   4. // 根据实际使用情况填写输入文件路径。
   5. const char* inputFilePath = "/";
   6. // 根据实际使用情况填写输出文件路径。
   7. const char* outputFilePath = "/";
   8. // 打开待解码二进制文件路径。
   9. inputFile_.open(inputFilePath, ios::in | ios::binary);
   10. // 配置解码文件输出路径。
   11. outFile_.open(outputFilePath, ios::out | ios::binary);
   12. // 开始解码。
   13. int32_t ret = OH_AudioCodec_Start(audioDec_);
   14. if (ret != AV_ERR_OK) {
   15. // 异常处理。
   16. }
   ```
8. （可选）调用OH\_AVCencInfo\_SetAVBuffer()，设置cencInfo。

   若当前播放的节目是DRM加密节目，且由上层应用做[媒体解封装](audio-video-demuxer.md)，则须调用OH\_AVCencInfo\_SetAVBuffer()将cencInfo设置给AVBuffer，以实现AVBuffer中媒体数据的解密。

   添加头文件：

   ```
   1. #include <multimedia/player_framework/native_cencinfo.h>
   ```

   在 CMake 脚本中链接动态库：

   ```
   1. target_link_libraries(sample PUBLIC libnative_media_avcencinfo.so)
   ```

   使用示例：

   ```
   1. auto buffer = signal_->inBufferQueue_.front();
   2. uint32_t keyIdLen = DRM_KEY_ID_SIZE;
   3. uint8_t keyId[] = {
   4. 0xd4, 0xb2, 0x01, 0xe4, 0x61, 0xc8, 0x98, 0x96,
   5. 0xcf, 0x05, 0x22, 0x39, 0x8d, 0x09, 0xe6, 0x28};
   6. uint32_t ivLen = DRM_KEY_IV_SIZE;
   7. uint8_t iv[] = {
   8. 0xbf, 0x77, 0xed, 0x51, 0x81, 0xde, 0x36, 0x3e,
   9. 0x52, 0xf7, 0x20, 0x4f, 0x72, 0x14, 0xa3, 0x95};
   10. uint32_t encryptedBlockCount = 0;
   11. uint32_t skippedBlockCount = 0;
   12. uint32_t firstEncryptedOffset = 0;
   13. uint32_t subsampleCount = 1;
   14. DrmSubsample subsamples[1] = { {0x10, 0x16} };
   15. // 创建CencInfo实例。
   16. OH_AVCencInfo *cencInfo = OH_AVCencInfo_Create();
   17. if (cencInfo == nullptr) {
   18. // 异常处理。
   19. }
   20. // 设置解密算法。
   21. OH_AVErrCode errNo = OH_AVCencInfo_SetAlgorithm(cencInfo, DRM_ALG_CENC_AES_CTR);
   22. if (errNo != AV_ERR_OK) {
   23. // 异常处理。
   24. }
   25. // 设置KeyId和Iv。
   26. errNo = OH_AVCencInfo_SetKeyIdAndIv(cencInfo, keyId, keyIdLen, iv, ivLen);
   27. if (errNo != AV_ERR_OK) {
   28. // 异常处理。
   29. }
   30. // 设置Sample信息。
   31. errNo = OH_AVCencInfo_SetSubsampleInfo(cencInfo, encryptedBlockCount, skippedBlockCount, firstEncryptedOffset,
   32. subsampleCount, subsamples);
   33. if (errNo != AV_ERR_OK) {
   34. // 异常处理。
   35. }
   36. // 设置模式：KeyId、Iv和SubSamples已被设置。
   37. errNo = OH_AVCencInfo_SetMode(cencInfo, DRM_CENC_INFO_KEY_IV_SUBSAMPLES_SET);
   38. if (errNo != AV_ERR_OK) {
   39. // 异常处理。
   40. }
   41. // 将CencInfo设置到AVBuffer中。
   42. errNo = OH_AVCencInfo_SetAVBuffer(cencInfo, buffer);
   43. if (errNo != AV_ERR_OK) {
   44. // 异常处理。
   45. }
   46. // 销毁CencInfo实例。
   47. errNo = OH_AVCencInfo_Destroy(cencInfo);
   48. if (errNo != AV_ERR_OK) {
   49. // 异常处理。
   50. }
   ```
9. 调用OH\_AudioCodec\_PushInputBuffer()，写入待解码的数据。

   需开发者填充完整的输入数据后调用。

   结束时需要将flags标识为AVCODEC\_BUFFER\_FLAGS\_EOS。

   ```
   1. uint32_t index = signal_->inQueue_.front();
   2. auto buffer = signal_->inBufferQueue_.front();
   3. int32_t size;
   4. int64_t pts;
   5. // size是待解码数据的每帧帧长度。pts是每帧的时间戳，用于指示音频应该何时被播放。
   6. // size和pts的获取来源：音视频资源文件或者待解码的数据流。
   7. // 若是解码音视频资源文件，则需从解封装OH_AVDemuxer_ReadSampleBuffer的buffer中获取。
   8. // 若是解码数据流，则需要从数据流的提供者获取。
   9. // 此处为了介绍解码功能以测试文件中保存的size和pts为示例。
   10. inputFile_.read(reinterpret_cast<char *>(&size), sizeof(size));
   11. inputFile_.read(reinterpret_cast<char *>(&pts), sizeof(pts));
   12. inputFile_.read((char *)OH_AVBuffer_GetAddr(buffer), size);
   13. OH_AVCodecBufferAttr attr = {0};
   14. if (inputFile_.eof()) {
   15. attr.size = 0;
   16. attr.flags = AVCODEC_BUFFER_FLAGS_EOS;
   17. } else {
   18. attr.size = size;
   19. attr.flags = AVCODEC_BUFFER_FLAGS_NONE;
   20. }
   21. attr.pts = pts;
   22. OH_AVBuffer_SetBufferAttr(buffer, &attr);
   23. int32_t ret = OH_AudioCodec_PushInputBuffer(audioDec_, index);
   24. if (ret != AV_ERR_OK) {
   25. // 异常处理。
   26. }
   ```
10. 调用OH\_AudioCodec\_FreeOutputBuffer()，释放解码后的数据。

    在获取解码PCM码流后，应及时调用OH\_AudioCodec\_FreeOutputBuffer()进行释放。

    ```
    1. uint32_t index = signal_->outQueue_.front();
    2. OH_AVBuffer *data = signal_->outBufferQueue_.front();
    3. if (data == nullptr) {
    4. // 异常处理
    5. }
    6. // 获取buffer attributes。
    7. OH_AVCodecBufferAttr attr = {0};
    8. int32_t ret = OH_AVBuffer_GetBufferAttr(data, &attr);
    9. if (ret != AV_ERR_OK) {
    10. // 异常处理。
    11. }
    12. // 将解码完成数据data写入到对应输出文件中。
    13. outFile_.write(reinterpret_cast<char *>(OH_AVBuffer_GetAddr(data)), attr.size);
    14. ret = OH_AudioCodec_FreeOutputBuffer(audioDec_, index);
    15. if (ret != AV_ERR_OK) {
    16. // 异常处理。
    17. }
    18. if (attr.flags == AVCODEC_BUFFER_FLAGS_EOS) {
    19. // 结束。
    20. }
    ```

从API version 11开始，Audio Vivid新增获取元数据。

```
1. uint32_t index = signal_->outQueue_.front();
2. OH_AVBuffer *data = signal_->outBufferQueue_.front();
3. // 获取buffer attributes。
4. OH_AVCodecBufferAttr attr = {0};
5. int32_t ret = OH_AVBuffer_GetBufferAttr(data, &attr);
6. if (ret != AV_ERR_OK) {
7. // 异常处理。
8. }
9. // 将解码完成数据data写入到对应输出文件中。
10. outFile_.write(reinterpret_cast<char *>(OH_AVBuffer_GetAddr(data)), attr.size);

12. // API version 11开始提供 获取audio vivid 元数据。
13. OH_AVFormat *format = OH_AVBuffer_GetParameter(data);
14. uint8_t *metadata = nullptr;
15. size_t metaSize;
16. OH_AVFormat_GetBuffer(format, OH_MD_KEY_AUDIO_VIVID_METADATA, &metadata, &metaSize);

18. ret = OH_AudioCodec_FreeOutputBuffer(audioDec_, index);
19. if (ret != AV_ERR_OK) {
20. // 异常处理。
21. }
22. if (attr.flags == AVCODEC_BUFFER_FLAGS_EOS) {
23. // 结束。
24. }
```

1. （可选）调用OH\_AudioCodec\_Flush()刷新解码器。

   调用OH\_AudioCodec\_Flush()后，解码器仍处于运行态，但会将当前队列清空，将已解码的数据释放。

   此时需要调用OH\_AudioCodec\_Start()重新开始解码。

   使用情况：

   * 在解码输出buffer属性为AVCODEC\_BUFFER\_FLAGS\_EOS后，若想重新使用相同配置进行解码时，需要调用刷新。
   * 在执行过程中遇到可继续执行的错误时（即OH\_AudioCodec\_IsValid()为true）可以调用刷新，然后调用OH\_AudioCodec\_Start()重新开始解码。

   ```
   1. // 刷新解码器 audioDec_。
   2. int32_t ret = OH_AudioCodec_Flush(audioDec_);
   3. if (ret != AV_ERR_OK) {
   4. // 异常处理。
   5. }
   6. // 重新开始解码。
   7. ret = OH_AudioCodec_Start(audioDec_);
   8. if (ret != AV_ERR_OK) {
   9. // 异常处理。
   10. }
   ```
2. （可选）调用OH\_AudioCodec\_Reset()重置解码器。

   调用OH\_AudioCodec\_Reset()后，解码器回到初始化状态，重置前获取到的输入/输出buffer都无法继续使用，需先调用OH\_AudioCodec\_Configure()重新配置，再调用OH\_AudioCodec\_Start()重新开始解码。启动后重新获取输入/输出buffer。

   ```
   1. // 重置解码器 audioDec_。
   2. int32_t ret = OH_AudioCodec_Reset(audioDec_);
   3. if (ret != AV_ERR_OK) {
   4. // 异常处理。
   5. }
   6. // 重新配置解码器参数。
   7. ret = OH_AudioCodec_Configure(audioDec_, format);
   8. if (ret != AV_ERR_OK) {
   9. // 异常处理。
   10. }
   ```
3. 调用OH\_AudioCodec\_Stop()停止解码器。

   停止后，可以通过调用OH\_AudioCodec\_Start()重新进入已启动状态（started）。停止前获取到的输入/输出buffer都无法继续使用，需要在启动后重新获取输入/输出buffer。

   ```
   1. // 终止解码器 audioDec_。
   2. int32_t ret = OH_AudioCodec_Stop(audioDec_);
   3. if (ret != AV_ERR_OK) {
   4. // 异常处理。
   5. }
   ```
4. 调用OH\_AudioCodec\_Destroy()销毁解码器实例，释放资源。

   说明

   禁止重复销毁解码器。

   ```
   1. // 调用OH_AudioCodec_Destroy, 销毁解码器。
   2. int32_t ret = OH_AudioCodec_Destroy(audioDec_);
   3. if (ret != AV_ERR_OK) {
   4. // 异常处理。
   5. } else {
   6. audioDec_ = NULL; // 不可重复destroy。
   7. }
   ```
