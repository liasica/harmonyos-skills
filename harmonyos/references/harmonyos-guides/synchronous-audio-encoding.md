---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/synchronous-audio-encoding
title: 音频编码同步模式
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > 音频编码同步模式
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:42+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:6953da10185186b61b902ba14d62a6a5a5b683f2fadbbccf9f74fb3e9ef5dab9
---

从API version 20开始，支持音频编码同步模式。

开发者可以调用本模块的Native API接口，完成音频编码，即将音频PCM编码压缩成不同的格式。

具体实现可参考[示例工程](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/BasicFeature/Media/AVCodec)。

接口不限制PCM数据的来源。开发者可以调用麦克风录制获取，也可以导入编辑后的PCM数据。通过音频编码，输出对应格式的码流，最后封装为目标格式文件。

支持的编码能力请参考[AVCodec支持的格式](avcodec-support-formats.md#音频编码)。

**适用场景**

通常推荐使用异步模式，异步模式请参考[音频编码](audio-encoding.md)。若需要主动请求buffer去编码PCM，则可以使用同步模式。

* 音频录制

  通过录制传入PCM，然后编码成对应格式的码流，最后封装成所需格式的文件。具体封装方法请参考[媒体数据封装](audio-video-muxer.md)。
* 音频编辑

  编辑PCM后导出音频文件的场景，需要编码成对应音频格式，最后封装成所需格式的文件。具体封装方法请参考[媒体数据封装](audio-video-muxer.md)。

说明

* AAC编码器默认采用的VBR可变码率模式，这可能导致与预期码率有偏差。
* AAC编码器默认输出携带ADTS头部，帧数据的前7字节为ADTS头部。

## 开发指导

详细的API说明请参考[AudioCodec](../harmonyos-references/capi-native-avcodec-audiocodec-h.md)。

参考以下示例代码，完成音频编码的全流程，包括：创建编码器、设置编码参数（采样率/码率/声道数等）、开始/刷新/重置/销毁资源。

在应用开发过程中，开发者应按一定顺序调用方法，执行对应操作，否则系统可能会抛出异常或生成其他未定义的行为。具体顺序可参考下列开发步骤及对应说明。

音频编解码同步模式调用关系图如下所示：

* 虚线表示可选。音频编码不涉及解密，无需调用OH\_AudioCodec\_SetDecryptionConfig。
* 实线表示必选。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/0DCIhDWbTZWDhBYO_5Q1Rw/zh-cn_image_0000002583478543.png?HW-CC-KV=V1&HW-CC-Date=20260427T234540Z&HW-CC-Expire=86400&HW-CC-Sign=A1F5C47E75B5D02E1621E2FE3BFE07E80AB90BB3F5A049CA27D91F1C56EE5614)

### 在CMake脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libnative_media_codecbase.so)
2. target_link_libraries(sample PUBLIC libnative_media_core.so)
3. target_link_libraries(sample PUBLIC libnative_media_acodec.so)
```

说明

上述'sample'字样仅为示例，此处由开发者根据实际工程目录自定义。

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
2. 创建编码器实例对象，OH\_AVCodec \*为编码器实例指针。

   应用可以通过媒体类型或编解码器名称创建编码器。

   方法一：通过Mimetype创建编码器。

   ```
   1. // 通过Mimetype创建编码器，这里示例创建的是AAC编码器，第二个参数设置为true表示当前是编码。
   2. OH_AVCodec *audioEnc_ = OH_AudioCodec_CreateByMime(OH_AVCODEC_MIMETYPE_AUDIO_AAC, true);
   ```

   方法二：通过codec name创建编码器。

   ```
   1. // 通过codec name创建编码器。
   2. OH_AVCapability *capability = OH_AVCodec_GetCapability(OH_AVCODEC_MIMETYPE_AUDIO_AAC, true);
   3. const char *name = OH_AVCapability_GetName(capability);
   4. OH_AVCodec *audioEnc_ = OH_AudioCodec_CreateByName(name);
   ```
3. 调用OH\_AudioCodec\_Configure配置编码器。

   配置选项key值说明：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/wBXmYOV6TsivUCCAW8wCAQ/zh-cn_image_0000002583438587.png?HW-CC-KV=V1&HW-CC-Date=20260427T234540Z&HW-CC-Expire=86400&HW-CC-Sign=588AA6F4C090B86DBEA735C18814315AF1D97F01804575A6D643F54081FA6588)

   各音频编码类型参数范围说明：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/MiZguBdOQI2q2NtouLzfgA/zh-cn_image_0000002552958542.png?HW-CC-KV=V1&HW-CC-Date=20260427T234540Z&HW-CC-Expire=86400&HW-CC-Sign=314052436337945ED115F8449BDE8809FA84B9AB20D44E2F01B9D4EAFE1EBD22)

   例如，对44100Hz采样率、2声道立体声、SAMPLE\_S16LE采样格式的PCM音频，以32000bps的码率进行AAC编码的调用流程如下：

```
1. OH_AVErrCode ret;
2. // 配置音频采样率（必须）
3. constexpr uint32_t DEFAULT_SAMPLERATE = 44100;
4. // 配置音频码率（必须）
5. constexpr uint64_t DEFAULT_BITRATE = 32000;
6. // 配置音频声道数（必须）
7. constexpr uint32_t DEFAULT_CHANNEL_COUNT = 2;
8. // 配置音频位深（必须）
9. constexpr OH_BitsPerSample SAMPLE_FORMAT = OH_BitsPerSample::SAMPLE_S16LE;
10. // 配置AAC profile（可选，默认值：AAC_PROFILE_LC，其他可选值：AAC_PROFILE_HE、AAC_PROFILE_HE_V2）
11. constexpr int32_t AAC_PROFILE = OH_AACProfile::AAC_PROFILE_LC;
12. OH_AVFormat *format = OH_AVFormat_Create();
13. // 写入format
14. OH_AVFormat_SetIntValue(format,OH_MD_KEY_AUD_CHANNEL_COUNT, DEFAULT_CHANNEL_COUNT);
15. OH_AVFormat_SetIntValue(format,OH_MD_KEY_AUD_SAMPLE_RATE, DEFAULT_SAMPLERATE);
16. OH_AVFormat_SetLongValue(format,OH_MD_KEY_BITRATE, DEFAULT_BITRATE);
17. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_SAMPLE_FORMAT, SAMPLE_FORMAT);
18. OH_AVFormat_SetLongValue(format,OH_MD_KEY_CHANNEL_LAYOUT, CHANNEL_LAYOUT);
19. OH_AVFormat_SetIntValue(format, OH_MD_KEY_PROFILE, AAC_PROFILE);
20. OH_AVFormat_SetIntValue(format, OH_MD_KEY_ENABLE_SYNC_MODE, 1); // 同步模式配置。
21. // 配置编码器
22. ret = OH_AudioCodec_Configure(audioEnc_, format);
23. if (ret != AV_ERR_OK) {
24. // 异常处理
25. }
```

FLAC编码调用示例：

```
1. OH_AVErrCode ret;
2. // 配置音频采样率（必须）。
3. constexpr uint32_t DEFAULT_SAMPLERATE = 44100;
4. // 配置音频码率（必须）。
5. constexpr uint64_t DEFAULT_BITRATE = 261000;
6. // 配置音频声道数（必须）。
7. constexpr uint32_t DEFAULT_CHANNEL_COUNT = 2;
8. // 配置音频声道布局（必须）。
9. // 值为CH_LAYOUT_MONO、CH_LAYOUT_STEREO、CH_LAYOUT_SURROUND、CH_LAYOUT_QUAD、CH_LAYOUT_5POINT0、CH_LAYOUT_5POINT1、CH_LAYOUT_6POINT1或CH_LAYOUT_7POINT1其中一项。
10. constexpr OH_AudioChannelLayout CHANNEL_LAYOUT = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
11. // 配置音频位深（必须） FLAC只有SAMPLE_S16LE和SAMPLE_S32LE。
12. constexpr OH_BitsPerSample SAMPLE_FORMAT = OH_BitsPerSample::SAMPLE_S32LE;
13. // 配置音频compliance level（默认值0，取值范围[-2,2]）。
14. constexpr int32_t COMPLIANCE_LEVEL = 0;

16. OH_AVFormat *format = OH_AVFormat_Create();
17. // 写入format。
18. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_CHANNEL_COUNT, DEFAULT_CHANNEL_COUNT);
19. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_SAMPLE_RATE, DEFAULT_SAMPLERATE);
20. OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, DEFAULT_BITRATE);
21. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_SAMPLE_FORMAT, SAMPLE_FORMAT);
22. OH_AVFormat_SetLongValue(format, OH_MD_KEY_CHANNEL_LAYOUT, CHANNEL_LAYOUT);
23. OH_AVFormat_SetLongValue(format, OH_MD_KEY_COMPLIANCE_LEVEL, COMPLIANCE_LEVEL);
24. OH_AVFormat_SetIntValue(format, OH_MD_KEY_ENABLE_SYNC_MODE, 1); // 同步模式配置。
25. // 配置编码器。
26. ret = OH_AudioCodec_Configure(audioEnc_, format);
27. if (ret != AV_ERR_OK) {
28. // 异常处理。
29. }
```

1. 调用OH\_AudioCodec\_Prepare()，编码器就绪。

   ```
   1. OH_AVErrCode ret = OH_AudioCodec_Prepare(audioEnc_);
   2. if (ret != AV_ERR_OK) {
   3. // 异常处理。
   4. }
   ```
2. 调用OH\_AudioCodec\_Start()启动编码器，进入运行态。

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
   8. // 打开待编码二进制文件路径（此处以输入为PCM文件为例）。
   9. inputFile_.open(inputFilePath, ios::in | ios::binary);
   10. // 配置编码文件输出路径（此处以输出为编码码流文件为例，并非可播放的音频文件，可播放的音频文件需要音频码流封装到容器内生成）。
   11. outFile_.open(outputFilePath, ios::out | ios::binary);
   12. // 开始编码。
   13. OH_AVErrCode ret = OH_AudioCodec_Start(audioEnc_);
   14. if (ret != AV_ERR_OK) {
   15. // 异常处理。
   16. }
   ```
3. 同步模式调用，写入待编码的PCM，获取编码输出的音频帧。

   示例代码中，每次输入的采样点数SAMPLES\_PER\_FRAME取值方法如下：

   AAC LC编码每帧包含1024个PCM样点，建议单次输入1024个样点的数据量。

   HE-AAC编码每帧包含2048个PCM样点，建议单次输入2048个样点的数据量。

   FLAC需要根据如下表格进行设置。

   | 采样率 | 样点数 |
   | --- | --- |
   | 8000 | 576 |
   | 16000 | 1152 |
   | 22050 | 2304 |
   | 24000 | 2304 |
   | 32000 | 2304 |
   | 44100 | 4608 |
   | 48000 | 4608 |
   | 88200 | 8192 |
   | 96000 | 8192 |

   单次编码输入的数据量（单位：字节）为：SAMPLES\_PER\_FRAME \* 声道数 \* 单个采样点的占用字节。

   使用示例：

   ```
   1. int32_t SAMPLES_PER_FRAME = 1024;
   2. // AAC LC编码一帧包含1024采样点，2声道，输入数据为S16LE，16比特数据，占用2字节。
   3. int32_t inputFrameBytes = SAMPLES_PER_FRAME * 2 * 2;
   4. bool inputFinished = false;
   5. OH_AVErrCode ret;
   6. OH_AVCodecBufferAttr attr;

   8. for (;;) {
   9. uint32_t index = 0;
   10. if (!inputFinished) {
   11. ret = OH_AudioCodec_QueryInputBuffer(audioEnc_, &index, 20000); // 20000us
   12. if (ret == AV_ERR_TRY_AGAIN_LATER) {
   13. continue;
   14. }
   15. if (ret != AV_ERR_OK) {
   16. // 异常处理。
   17. break;
   18. }
   19. OH_AVBuffer *inputBuf = OH_AudioCodec_GetInputBuffer(audioEnc_, index);
   20. if (inputBuf == nullptr) {
   21. // 异常处理。
   22. break;
   23. }
   24. memset(&attr, 0, sizeof(attr));
   25. if (!inputFile_.eof()) {
   26. inputFile_.read((char *)OH_AVBuffer_GetAddr(inputBuf), inputFrameBytes);
   27. int32_t readSize = inputFile_.gcount();
   28. attr.size = readSize;
   29. attr.flags = readSize != 0 ? AVCODEC_BUFFER_FLAGS_NONE : AVCODEC_BUFFER_FLAGS_EOS;
   30. } else {
   31. inputFinished = true;
   32. attr.size = 0;
   33. attr.flags = AVCODEC_BUFFER_FLAGS_EOS;
   34. }
   35. if (OH_AVBuffer_SetBufferAttr(inputBuf, &attr) != AV_ERR_OK) {
   36. // 异常处理。
   37. }
   38. if (OH_AudioCodec_PushInputBuffer(audioEnc_, index) != AV_ERR_OK) {
   39. // 异常处理。
   40. }
   41. }
   42. // 当输入的数据量可以编码出多帧数据时，需要多次调用获取输出缓冲区，才能取完编码后的数据。
   43. ret = OH_AudioCodec_QueryOutputBuffer(audioEnc_, &index, 20000); // 20000us
   44. if (ret == AV_ERR_TRY_AGAIN_LATER) {
   45. // 超时，可能输入的数据不足以编码出一帧，或者超时时间设置过短。
   46. continue;
   47. }
   48. if (ret != AV_ERR_OK) {
   49. // 异常处理。
   50. break;
   51. }
   52. OH_AVBuffer *outputBuf = OH_AudioCodec_GetOutputBuffer(audioEnc_, index);
   53. if (outputBuf == nullptr) {
   54. // 异常处理。
   55. break;
   56. }
   57. if (OH_AVBuffer_GetBufferAttr(outputBuf, &attr) != AV_ERR_OK) {
   58. // 异常处理。
   59. break;
   60. }
   61. if (attr.flags & AVCODEC_BUFFER_FLAGS_EOS) {
   62. // 输出结束。
   63. break;
   64. }
   65. // 这里示例仅将数据写入文件记录。假如需要封装成音频文件，可参考媒体数据封装，调用OH_AVMuxer_WriteSampleBuffer封装数据。
   66. outFile_.write(reinterpret_cast<char *>(OH_AVBuffer_GetAddr(outputBuf)), attr.size);
   67. OH_AudioCodec_FreeOutputBuffer(audioEnc_, index);
   68. }
   ```

   在上方案例中，attr.flags表示缓冲区标记的类别。

   结束时需要将flags标识为AVCODEC\_BUFFER\_FLAGS\_EOS。

   | 枚举值 | 描述 |
   | --- | --- |
   | AVCODEC\_BUFFER\_FLAGS\_NONE | 表示为普通帧。 |
   | AVCODEC\_BUFFER\_FLAGS\_EOS | 表示缓冲区是流结束帧。 |
   | AVCODEC\_BUFFER\_FLAGS\_CODEC\_DATA | 表示缓冲区包含编解码特定数据。 |
4. （可选）调用OH\_AudioCodec\_Reset()重置编码器。

   调用OH\_AudioCodec\_Reset()后，编码器回到初始化状态，重置前获取到的输入/输出buffer都无法继续使用，需先调用OH\_AudioCodec\_Configure()重新配置，再调用OH\_AudioCodec\_Start()重新开始编码。启动后重新获取输入/输出buffer。

   ```
   1. // 重置编码器。
   2. OH_AVErrCode ret = OH_AudioCodec_Reset(audioEnc_);
   3. if (ret != AV_ERR_OK) {
   4. // 异常处理。
   5. }
   6. // 重新配置编码器参数。
   7. ret = OH_AudioCodec_Configure(audioEnc_, format);
   8. if (ret != AV_ERR_OK) {
   9. // 异常处理。
   10. }
   ```
5. （可选）调用OH\_AudioCodec\_Stop()停止编码器。

   停止后，可以通过调用OH\_AudioCodec\_Start()重新进入已启动状态（started）。停止前获取到的输入/输出buffer都无法继续使用，需要在启动后重新获取输入/输出buffer。

   ```
   1. // 停止编码器。
   2. OH_AVErrCode ret = OH_AudioCodec_Stop(audioEnc_);
   3. if (ret != AV_ERR_OK) {
   4. // 异常处理。
   5. }
   ```
6. 调用OH\_AudioCodec\_Destroy()销毁编码器实例，释放资源。

   说明

   禁止重复销毁编码器。

   ```
   1. // 调用OH_AudioCodec_Destroy，销毁编码器。
   2. OH_AVErrCode ret = OH_AudioCodec_Destroy(audioEnc_);
   3. if (ret != AV_ERR_OK) {
   4. // 异常处理。
   5. } else {
   6. audioEnc_ = NULL; // 不可重复destroy。
   7. }
   ```
