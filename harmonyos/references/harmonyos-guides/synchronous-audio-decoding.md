---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/synchronous-audio-decoding
title: 音频解码同步模式
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > 音频解码同步模式
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:43+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:6499a2eabca4a8237315e749504974923d8f1199b7a4b07a305aacf08df45673
---

从API version 20开始，支持音频解码同步模式。

开发者可以调用本模块的Native API接口，完成同步模式的音频解码，即将媒体数据解码为PCM码流。

具体实现可参考[示例工程](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/BasicFeature/Media/AVCodec)。

支持的解码能力请参考[AVCodec支持的格式](avcodec-support-formats.md#音频解码)。

**适用场景**

通常推荐使用异步模式，详细内容请参考[音频解码](audio-decoding.md)。若需要主动请求buffer去送帧，则可以使用同步模式。

将音视频文件解码为PCM码流，通常需要以下步骤：[媒体数据解析](audio-video-demuxer.md) -> 音频解码。

本指南描述音频解码过程：输入音频帧和解码出PCM码流。

## 开发指导

详细的API说明请参考[AudioCodec](../harmonyos-references/capi-native-avcodec-audiocodec-h.md)。

参考以下示例代码，完成音频解码的全流程，包括：创建解码器、设置解码参数（采样率/码率/声道数等）、开始/刷新/重置/销毁资源。

在应用开发过程中，开发者应按顺序调用方法，执行操作，否则系统可能会抛出异常或生成其他未定义的行为。具体顺序可参考下列开发步骤及对应说明。

音频编解码同步模式调用关系图如下所示：

* 虚线表示可选。
* 实线表示必选。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/bCaYhJdYRiWoA2cByerUZw/zh-cn_image_0000002583478543.png?HW-CC-KV=V1&HW-CC-Date=20260427T234542Z&HW-CC-Expire=86400&HW-CC-Sign=CF4F94F991BFA1E3F9798A3DBA1981B8E4B5F1B0EFA05F7C7477EF4E53DE53E9)

### 在 CMake 脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libnative_media_codecbase.so)
2. target_link_libraries(sample PUBLIC libnative_media_core.so)
3. target_link_libraries(sample PUBLIC libnative_media_acodec.so)
```

说明

上述'sample'字样仅为示例，开发者需根据实际工程目录进行自定义。

### 开发步骤

1. 添加头文件和命名空间。

   ```
   1. #include <multimedia/player_framework/native_avcodec_audiocodec.h>
   2. #include <multimedia/native_audio_channel_layout.h>
   3. #include <multimedia/player_framework/native_avcapability.h>
   4. #include <multimedia/player_framework/native_avcodec_base.h>
   5. #include <multimedia/player_framework/native_avformat.h>
   6. #include <multimedia/player_framework/native_avbuffer.h>

   8. // c++标准库命名空间。
   9. using namespace std;
   ```
2. 创建解码器实例对象，OH\_AVCodec \*为解码器实例指针。

   应用可以通过媒体类型或编解码器名称创建解码器。

   方法一：通过Mimetype创建解码器。

   ```
   1. // 通过Mimetype创建解码器，这里示例创建的是AAC编码格式，第二个入参设置false表示当前是解码。
   2. OH_AVCodec *audioDec_ = OH_AudioCodec_CreateByMime(OH_AVCODEC_MIMETYPE_AUDIO_AAC, false);
   ```

   方法二：通过codec name创建解码器。

   ```
   1. // 通过codec name创建解码器。
   2. OH_AVCapability *capability = OH_AVCodec_GetCapability(OH_AVCODEC_MIMETYPE_AUDIO_AAC, false);
   3. const char *name = OH_AVCapability_GetName(capability);
   4. OH_AVCodec *audioDec_ = OH_AudioCodec_CreateByName(name);
   ```
3. （可选）OH\_AudioCodec\_SetDecryptionConfig设置解密配置。

   当获取到DRM信息（参考[音视频解封装](audio-video-demuxer.md)开发步骤第4步）后，通过此接口进行解密配置。

   DRM相关接口详见[DRM](../harmonyos-references/capi-drm.md)。

   此接口需在Prepare前调用。

   添加头文件：

   ```
   1. #include <multimedia/drm_framework/native_mediakeysystem.h>
   2. #include <multimedia/drm_framework/native_mediakeysession.h>
   3. #include <multimedia/drm_framework/native_drm_err.h>
   4. #include <multimedia/drm_framework/native_drm_common.h>
   ```

   在CMake脚本中链接动态库：

   ```
   1. target_link_libraries(sample PUBLIC libnative_drm.so)
   ```

   使用示例：

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
   14. // 如果创建失败，请查看DRM接口文档及日志信息。
   15. printf("create media key session failed.");
   16. return;
   17. }
   18. if (session == nullptr) {
   19. printf("media key session is nullptr.");
   20. return;
   21. }
   22. // 获取许可证请求、设置许可证响应等。
   23. // 设置解密信息。将解密会话设置到解码器中。当前音频解密不支持安全解码器，设置为false。
   24. bool secureAudio = false;
   25. ret = OH_AudioCodec_SetDecryptionConfig(audioDec_, session, secureAudio);
   ```
4. 调用OH\_AudioCodec\_Configure()配置解码器。

   配置选项key值说明：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/g0ufsyd4Qm-pejsGVKBgEQ/zh-cn_image_0000002552798894.png?HW-CC-KV=V1&HW-CC-Date=20260427T234542Z&HW-CC-Expire=86400&HW-CC-Sign=1BCC6F613F073BFC8E81DD514AB790D38F7F8C2011B6D5E041641FB4734B5F41)

   各音频解码类型参数范围说明：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/oAyarMUVQMeOoxuNdkrTCw/zh-cn_image_0000002583438589.png?HW-CC-KV=V1&HW-CC-Date=20260427T234542Z&HW-CC-Expire=86400&HW-CC-Sign=C89D8A11E9FFAF2A3E12D5DAD1FC6BBF7966F011B5D0D42030AB07590BC22807)

   从API version 20开始，支持[采样率范围](../harmonyos-references/capi-native-avcapability-h.md#oh_avcapability_getaudiosupportedsamplerateranges)能力查询，以下几种音频解码类型支持对范围内的任意采样率进行解码：

   | 音频解码类型 | 采样率(Hz) |
   | --- | --- |
   | Flac | 8000 ~ 384000 |
   | Vorbis | 8000 ~ 192000 |
   | APE | 1 ~ 2147483647 |

   ```
   1. // 配置音频采样率（必须）。
   2. constexpr uint32_t DEFAULT_SAMPLERATE = 44100;
   3. // 配置音频声道数（必须）。
   4. constexpr uint32_t DEFAULT_CHANNEL_COUNT = 2;
   5. // 配置是否为ADTS解码（aac解码时可选）。
   6. constexpr uint32_t DEFAULT_AAC_TYPE = 1;
   7. OH_AVFormat *format = OH_AVFormat_Create();
   8. // 写入format。
   9. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_SAMPLE_RATE, DEFAULT_SAMPLERATE);
   10. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_CHANNEL_COUNT, DEFAULT_CHANNEL_COUNT);
   11. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AAC_IS_ADTS, DEFAULT_AAC_TYPE);
   12. OH_AVFormat_SetIntValue(format, OH_MD_KEY_ENABLE_SYNC_MODE, 1); // 同步模式配置。
   13. // 配置解码器。
   14. OH_AVErrCode ret = OH_AudioCodec_Configure(audioDec_, format);
   15. if (ret != AV_ERR_OK) {
   16. // 异常处理。
   17. }
   ```
5. 调用OH\_AudioCodec\_Prepare()，解码器就绪。

   ```
   1. OH_AVErrCode ret = OH_AudioCodec_Prepare(audioDec_);
   2. if (ret != AV_ERR_OK) {
   3. // 异常处理。
   4. }
   ```
6. 调用OH\_AudioCodec\_Start()启动解码器，进入运行态。

   添加头文件：

   ```
   1. #include <fstream>
   ```

   使用示例：

   ```
   1. ifstream inputFile_;
   2. ofstream outFile_;

   4. // 根据实际使用情况填写输入文件路径。为便于演示音频解码功能，此处输入文件包含音频帧及相关信息，而非可直接播放的音频文件。
   5. const char* inputFilePath = "/";
   6. // 根据实际使用情况填写输出文件路径。本指南仅演示音频解码功能，解码后的PCM数据保存到文件中，未作进一步处理。
   7. const char* outputFilePath = "/";
   8. // 打开待解码二进制文件路径。
   9. inputFile_.open(inputFilePath, ios::in | ios::binary);
   10. // 配置解码文件输出路径。
   11. outFile_.open(outputFilePath, ios::out | ios::binary);
   12. // 开始解码。
   13. OH_AVErrCode ret = OH_AudioCodec_Start(audioDec_);
   14. if (ret != AV_ERR_OK) {
   15. // 异常处理。
   16. }
   ```
7. （可选）调用OH\_AVCencInfo\_SetAVBuffer()，设置cencInfo。

   如果当前播放的节目是DRM加密节目，并且由上层应用进行[媒体数据解析](audio-video-demuxer.md)，则需要调用OH\_AVCencInfo\_SetAVBuffer()将cencInfo设置给AVBuffer，以实现媒体数据的解密。

   添加头文件：

   ```
   1. #include <multimedia/player_framework/native_cencinfo.h>
   ```

   在CMake脚本中链接动态库：

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
8. 同步模式调用，写入待解码的数据，获取解码的输出。

   读取数据：

   ```
   1. // size是待解码数据的每帧帧长度。pts是每帧的时间戳，用于指示音频应该何时被播放。
   2. // size和pts的获取来源：音视频资源文件或者待解码的数据流。
   3. // 如果是解码音视频资源文件，则需要从解封装OH_AVDemuxer_ReadSampleBuffer的buffer中获取。
   4. // 如果是解码数据流，则需要从数据流的提供者获取。
   5. // 此处为了介绍解码功能以测试文件中保存的size和pts为示例。
   6. bool DecoderFillInputBuffer(OH_AVBuffer *buffer, ifstream &inputFile)
   7. {
   8. OH_AVCodecBufferAttr attr;
   9. memset(&attr, 0, sizeof(attr));
   10. attr.flags = AVCODEC_BUFFER_FLAGS_EOS;
   11. bool finished = true;
   12. do {
   13. int64_t size;
   14. inputFile.read(reinterpret_cast<char *>(&size), sizeof(size));
   15. if (inputFile.eof() || inputFile.gcount() != sizeof(size)) {
   16. break;
   17. }
   18. inputFile.read(reinterpret_cast<char *>(&attr.pts), sizeof(attr.pts));
   19. if (inputFile.gcount() != sizeof(attr.pts)) {
   20. break;
   21. }
   22. attr.size = static_cast<int32_t>(size);
   23. if (attr.size > 0) {
   24. inputFile.read((char *)OH_AVBuffer_GetAddr(buffer), attr.size);
   25. attr.flags = AVCODEC_BUFFER_FLAGS_NONE;
   26. finished = false;
   27. }
   28. } while (0);
   29. OH_AVBuffer_SetBufferAttr(buffer, &attr);
   30. return finished;
   31. }
   32. bool InputOneFrame(OH_AVCodec *codec, ifstream &inputFile)
   33. {
   34. uint32_t index = 0;
   35. bool finished = true;
   36. OH_AVErrCode ret = OH_AudioCodec_QueryInputBuffer(codec, &index, 20000); // 20000us
   37. if (ret == AV_ERR_TRY_AGAIN_LATER) {
   38. // 超时，异常处理，设置的超时时间过短或输入输出buffer没有消耗/释放导致解码阻塞。
   39. return finished;
   40. }
   41. if (ret != AV_ERR_OK) {
   42. // 异常处理。
   43. return finished;
   44. }
   45. OH_AVBuffer *inputBuf = OH_AudioCodec_GetInputBuffer(codec, index);
   46. if (inputBuf == nullptr) {
   47. // 异常处理。
   48. return finished;
   49. }
   50. finished = DecoderFillInputBuffer(inputBuf, inputFile);
   51. OH_AudioCodec_PushInputBuffer(codec, index);
   52. return finished;
   53. }
   ```

   需开发者填充完整的输入数据后调用。

   结束时需要将flags标识为AVCODEC\_BUFFER\_FLAGS\_EOS。

   ```
   1. bool inputFinished = false;
   2. for (;;) {
   3. if (!inputFinished) {
   4. inputFinished = InputOneFrame(audioDec_, inputFile_);
   5. }
   6. uint32_t index;
   7. OH_AVErrCode ret = OH_AudioCodec_QueryOutputBuffer(audioDec_, &index, 20000); // 20000us
   8. if (ret == AV_ERR_TRY_AGAIN_LATER) {
   9. // 超时，异常处理，设置的超时时间过短或输入输出buffer没有消耗/释放导致解码阻塞。
   10. continue;
   11. } else if (ret == AV_ERR_STREAM_CHANGED) {
   12. // 解码输出参数变化后的回调处理，应用根据实际情况进行处理。
   13. OH_AVFormat *outFormat = OH_AudioCodec_GetOutputDescription(audioDec_);
   14. int32_t sampleRate;
   15. int32_t channelCount;
   16. int32_t sampleFormat;
   17. if (OH_AVFormat_GetIntValue(outFormat, OH_MD_KEY_AUD_SAMPLE_RATE, &sampleRate)) {
   18. // 判断采样率是否发生变化，进行对应处理。
   19. }
   20. if (OH_AVFormat_GetIntValue(outFormat, OH_MD_KEY_AUD_CHANNEL_COUNT, &channelCount)) {
   21. // 判断声道数是否发生变化，进行对应处理。
   22. }
   23. if (OH_AVFormat_GetIntValue(outFormat, OH_MD_KEY_AUDIO_SAMPLE_FORMAT, &sampleFormat)) {
   24. // 判断音频采样格式是否发生变化，进行对应处理。
   25. }
   26. continue;
   27. }
   28. if (ret != AV_ERR_OK) {
   29. // 异常处理。
   30. break;
   31. }
   32. OH_AVBuffer *outputBuf = OH_AudioCodec_GetOutputBuffer(audioDec_, index);
   33. if (outputBuf == nullptr) {
   34. // 异常处理。
   35. break;
   36. }
   37. OH_AVCodecBufferAttr attr;
   38. if (OH_AVBuffer_GetBufferAttr(outputBuf, &attr) != AV_ERR_OK) {
   39. // 异常处理。
   40. break;
   41. }
   42. if (attr.flags & AVCODEC_BUFFER_FLAGS_EOS) {
   43. OH_AudioCodec_FreeOutputBuffer(audioDec_, index);
   44. // 解码输出结束。
   45. break;
   46. }
   47. outFile_.write(reinterpret_cast<char *>(OH_AVBuffer_GetAddr(outputBuf)), attr.size);
   48. OH_AudioCodec_FreeOutputBuffer(audioDec_, index);
   49. }
   ```
9. （可选）调用OH\_AudioCodec\_Flush()刷新解码器。

   调用OH\_AudioCodec\_Flush()后，解码器仍处于运行态，但会清空当前队列，释放已解码的数据。刷新前获取到的输入/输出buffer都无法继续使用。

   此时需要调用OH\_AudioCodec\_Start()重新开始解码。

   使用情况：

   * 之前输入的数据不再使用的场景，例如在解封装seek之后，调用刷新。
   * 在解码输出buffer属性为AVCODEC\_BUFFER\_FLAGS\_EOS后，若想重新使用相同配置进行解码时，需要调用刷新。
   * 在执行过程中遇到可继续执行的错误时（即OH\_AudioCodec\_IsValid()为true）可以调用刷新，然后调用OH\_AudioCodec\_Start()重新开始解码。

   ```
   1. // 刷新解码器audioDec_。
   2. OH_AVErrCode ret = OH_AudioCodec_Flush(audioDec_);
   3. if (ret != AV_ERR_OK) {
   4. // 异常处理。
   5. }
   6. // 重新开始解码。
   7. ret = OH_AudioCodec_Start(audioDec_);
   8. if (ret != AV_ERR_OK) {
   9. // 异常处理。
   10. }
   ```
10. （可选）调用OH\_AudioCodec\_Reset()重置解码器。

    调用OH\_AudioCodec\_Reset()后，解码器回到初始化状态，重置前获取到的输入/输出buffer都无法继续使用，需先调用OH\_AudioCodec\_Configure()重新配置，再调用OH\_AudioCodec\_Start()重新开始解码。启动后重新获取输入/输出buffer。

    ```
    1. // 重置解码器audioDec_。
    2. OH_AVErrCode ret = OH_AudioCodec_Reset(audioDec_);
    3. if (ret != AV_ERR_OK) {
    4. // 异常处理。
    5. }
    6. // 重新配置解码器参数。
    7. ret = OH_AudioCodec_Configure(audioDec_, format);
    8. if (ret != AV_ERR_OK) {
    9. // 异常处理。
    10. }
    ```
11. 调用OH\_AudioCodec\_Stop()停止解码器。

    停止后，可以通过调用OH\_AudioCodec\_Start()重新进入已启动状态（started）。停止前获取到的输入/输出buffer都无法继续使用，需要在启动后重新获取输入/输出buffer。

    ```
    1. // 终止解码器audioDec_。
    2. OH_AVErrCode ret = OH_AudioCodec_Stop(audioDec_);
    3. if (ret != AV_ERR_OK) {
    4. // 异常处理。
    5. }
    ```
12. 调用OH\_AudioCodec\_Destroy()销毁解码器实例，释放资源。

    说明

    禁止重复销毁解码器。

    ```
    1. // 调用OH_AudioCodec_Destroy, 销毁解码器。
    2. OH_AVErrCode ret = OH_AudioCodec_Destroy(audioDec_);
    3. if (ret != AV_ERR_OK) {
    4. // 异常处理。
    5. } else {
    6. audioDec_ = NULL; // 不可重复destroy。
    7. }
    ```
