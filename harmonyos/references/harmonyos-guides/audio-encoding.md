---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-encoding
title: 音频编码
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > 音频编码
category: harmonyos-guides
scraped_at: 2026-04-29T13:34:39+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:be059318fec81139d80a0eb34c702f50cc593a5aeacaf5bda29627a0f2d5c052
---

开发者可以调用本模块的Native API接口，完成音频编码，即将音频PCM编码压缩成不同的格式。

接口不限制PCM数据的来源，开发者可以调用麦克风录制获取、也可以导入编辑后的PCM数据，通过音频编码，输出对应格式的码流，最后封装为目标格式文件。

当前支持的编码能力请参考[AVCodec支持的格式](avcodec-support-formats.md#音频编码)。

**适用场景**

* 音频录制

  通过录制传入PCM，然后编码出对应格式的码流，最后[封装](audio-video-muxer.md)为所需格式的音频文件。
* 音频编辑

  编辑PCM后导出音频文件的场景，需要编码成对应音频格式后再[封装](audio-video-muxer.md)成文件。

说明

* AAC编码器默认采用的VBR可变码率模式，与配置的预期参数可能存在偏差。
* AAC编码器默认输出携带ADTS头部，帧数据的前7字节为ADTS头部。

## 开发指导

详细的API说明请参考[native\_avcodec\_audiocodec.h](../harmonyos-references/capi-native-avcodec-audiocodec-h.md)。

参考以下示例代码，完成音频编码的全流程，包括：创建编码器、设置编码参数（采样率/码率/声道数等）、开始、刷新、重置、销毁资源。

在应用开发过程中，开发者应按一定顺序调用方法，执行对应操作，否则系统可能会抛出异常或生成其他未定义的行为。具体顺序可参考下列开发步骤及对应说明。

如下为音频编码调用关系图：

* 虚线表示可选。
* 实线表示必选。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/Z-yZSzf8SXCC9hDRmDf4vw/zh-cn_image_0000002589324911.png?HW-CC-KV=V1&HW-CC-Date=20260429T053438Z&HW-CC-Expire=86400&HW-CC-Sign=70731F71784F4AACF00883E9AF90A698D07AA3DFEBB8389DF49E0E53DED173D7)

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
2. 创建编码器实例对象，OH\_AVCodec\*为编码器实例指针。

   应用可以通过媒体类型或编解码器名称创建编码器。

   方法一：通过mime type创建编码器。

   ```
   1. // 设置判定是否为编码；设置true表示当前是编码。
   2. bool isEncoder = true;
   3. // 通过媒体类型创建编码器。
   4. OH_AVCodec *audioEnc_ = OH_AudioCodec_CreateByMime(OH_AVCODEC_MIMETYPE_AUDIO_AAC, isEncoder);
   ```

   方法二：通过codec name创建编码器。

   ```
   1. // 通过codec name创建编码器。
   2. OH_AVCapability *capability = OH_AVCodec_GetCapability(OH_AVCODEC_MIMETYPE_AUDIO_AAC, true);
   3. const char *name = OH_AVCapability_GetName(capability);
   4. OH_AVCodec *audioEnc_ = OH_AudioCodec_CreateByName(name);
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
   2. class AEncBufferSignal {
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
   15. AEncBufferSignal *signal_;
   ```
3. 调用OH\_AudioCodec\_RegisterCallback()注册回调函数。

   注册回调函数指针集合OH\_AVCodecCallback，包括：

   * OH\_AVCodecOnError：编码器运行错误。
   * OH\_AVCodecOnStreamChanged：音频编码器暂未支持此回调。
   * OH\_AVCodecOnNeedInputBuffer：运行过程中需要新的输入数据，即编码器已准备好，可以输入PCM数据。
   * OH\_AVCodecOnNewOutputBuffer：运行过程中产生了新的输出数据，即编码完成。

   开发者可以通过处理该回调报告的信息，确保编码器正常运转。

   注意

   请勿在回调中调用编码器的相关接口或进行耗时操作。

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
   12. (void)format;
   13. (void)userData;
   14. }
   15. // OH_AVCodecOnNeedInputBuffer回调函数的实现。
   16. static void OnInputBufferAvailable(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *data, void *userData)
   17. {
   18. (void)codec;
   19. // 编码输入码流送入InputBuffer队列。
   20. AEncBufferSignal *signal = static_cast<AEncBufferSignal *>(userData);
   21. unique_lock<mutex> lock(signal->inMutex_);
   22. signal->inQueue_.push(index);
   23. signal->inBufferQueue_.push(data);
   24. signal->inCond_.notify_all();
   25. }
   26. // OH_AVCodecOnNewOutputBuffer回调函数的实现。
   27. static void OnOutputBufferAvailable(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *data, void *userData)
   28. {
   29. (void)codec;
   30. // 将对应输出buffer的index送入OutputQueue_队列。
   31. // 将对应编码完成的数据data送入outBuffer队列。
   32. AEncBufferSignal *signal = static_cast<AEncBufferSignal *>(userData);
   33. unique_lock<mutex> lock(signal->outMutex_);
   34. signal->outQueue_.push(index);
   35. signal->outBufferQueue_.push(data);
   36. signal->outCond_.notify_all();
   37. }
   ```

   配置回调：

   ```
   1. signal_ = new AEncBufferSignal();
   2. OH_AVCodecCallback cb_ = {&OnError, &OnOutputFormatChanged, &OnInputBufferAvailable, &OnOutputBufferAvailable};
   3. // 配置异步回调。
   4. int32_t ret = OH_AudioCodec_RegisterCallback(audioEnc_, cb_, signal_);
   5. if (ret != AV_ERR_OK) {
   6. // 异常处理。
   7. }
   ```
4. 调用OH\_AudioCodec\_Configure设置编码器。

   配置选项key值说明：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/FhLZyDdGT_uFzGaPJJpkdw/zh-cn_image_0000002589244847.png?HW-CC-KV=V1&HW-CC-Date=20260429T053438Z&HW-CC-Expire=86400&HW-CC-Sign=36EA696FF84AB650ED3D1E3463647AD5A12A83A1935C90B77128C8B02E345794)

   各音频编码类型参数范围说明：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/dsBMxpMxQSiJl-Dmdx3Nmg/zh-cn_image_0000002558765042.png?HW-CC-KV=V1&HW-CC-Date=20260429T053438Z&HW-CC-Expire=86400&HW-CC-Sign=F71338B32FE570C1F6DC90EB261F6B27277F0801CCAE08ADBE0947DCF3000F9D)

   例如对一个44100Hz采样率、2声道立体声、SAMPLE\_S16LE采样格式的PCM音频，以32000bps的码率进行AAC编码的调用流程如下：

```
1. int32_t ret;
2. // 配置音频采样率（必须）
3. constexpr uint32_t DEFAULT_SAMPLERATE = 44100;
4. // 配置音频码率（必须）
5. constexpr uint64_t DEFAULT_BITRATE = 32000;
6. // 配置音频声道数（必须）
7. constexpr uint32_t DEFAULT_CHANNEL_COUNT = 2;
8. // 配置音频声道类型（必须）
9. constexpr OH_AudioChannelLayout CHANNEL_LAYOUT = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
10. // 配置音频位深（必须）
11. constexpr OH_BitsPerSample SAMPLE_FORMAT = OH_BitsPerSample::SAMPLE_S16LE;
12. // 配置AAC profile（可选，默认值：AAC_PROFILE_LC，其他可选值：AAC_PROFILE_HE、AAC_PROFILE_HE_V2）
13. constexpr int32_t AAC_PROFILE = OH_AACProfile::AAC_PROFILE_LC;

15. OH_AVFormat *format = OH_AVFormat_Create();
16. // 写入format
17. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_CHANNEL_COUNT, DEFAULT_CHANNEL_COUNT);
18. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_SAMPLE_RATE, DEFAULT_SAMPLERATE);
19. OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, DEFAULT_BITRATE);
20. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_SAMPLE_FORMAT, SAMPLE_FORMAT);
21. OH_AVFormat_SetLongValue(format, OH_MD_KEY_CHANNEL_LAYOUT, CHANNEL_LAYOUT);
22. OH_AVFormat_SetIntValue(format, OH_MD_KEY_PROFILE, AAC_PROFILE);
23. // 配置编码器
24. ret = OH_AudioCodec_Configure(audioEnc_, format);
25. if (ret != AV_ERR_OK) {
26. // 异常处理
27. }
```

例FLAC调用流程：

```
1. int32_t ret;
2. // 配置音频采样率（必须）。
3. constexpr uint32_t DEFAULT_SAMPLERATE = 44100;
4. // 配置音频码率（必须）。
5. constexpr uint64_t DEFAULT_BITRATE = 261000;
6. // 配置音频声道数（必须）。
7. constexpr uint32_t DEFAULT_CHANNEL_COUNT = 2;
8. // 配置音频声道布局（必须）。
9. // 值为CH_LAYOUT_MONO、CH_LAYOUT_STEREO、CH_LAYOUT_SURROUND、CH_LAYOUT_QUAD、CH_LAYOUT_5POINT0、CH_LAYOUT_5POINT1、CH_LAYOUT_6POINT1或CH_LAYOUT_7POINT1其中一项。
10. constexpr OH_AudioChannelLayout CHANNEL_LAYOUT = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
11. // 配置音频位深（必须） flac只有SAMPLE_S16LE和SAMPLE_S32LE。
12. constexpr OH_BitsPerSample SAMPLE_FORMAT = OH_BitsPerSample::SAMPLE_S32LE;
13. // 配置音频compliance level (默认值0，取值范围-2~2)。
14. constexpr int32_t COMPLIANCE_LEVEL = 0;

16. OH_AVFormat *format = OH_AVFormat_Create();
17. // 写入format。
18. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_CHANNEL_COUNT, DEFAULT_CHANNEL_COUNT);
19. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_SAMPLE_RATE, DEFAULT_SAMPLERATE);
20. OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, DEFAULT_BITRATE);
21. // 配置音频精度。API version 20前，FLAC编码必须设置此参数，设置为1即可；未设置此参数配置FLAC编码器时，调用OH_AudioCodec_Configure会返回错误码AV_ERR_INVALID_VAL。该值无实际作   用，不会影响编码结果。从API version 20开始，无需设置此参数。
22. // constexpr int32_t BITS_PER_CODED_SAMPLE = 1;
23. // OH_AVFormat_SetIntValue(format, OH_MD_KEY_BITS_PER_CODED_SAMPLE, BITS_PER_CODED_SAMPLE);
24. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_SAMPLE_FORMAT, SAMPLE_FORMAT);
25. OH_AVFormat_SetLongValue(format, OH_MD_KEY_CHANNEL_LAYOUT, CHANNEL_LAYOUT);
26. OH_AVFormat_SetLongValue(format, OH_MD_KEY_COMPLIANCE_LEVEL, COMPLIANCE_LEVEL);
27. // 配置编码器。
28. ret = OH_AudioCodec_Configure(audioEnc_, format);
29. if (ret != AV_ERR_OK) {
30. // 异常处理。
31. }
```

例AMR编码调用流程：

```
1. int32_t ret;
2. // 配置音频采样率（必须），amr-nb输入采样率为8000hz的PCM，amr-wb输入采样率为16000hz的PCM
3. constexpr uint32_t DEFAULT_SAMPLERATE = 8000;
4. // 配置音频码率（必须）
5. // amr-nb支持码率4750、5150、5900、6700、7400、7950、10200、12200
6. // amr-wb支持码率6600、8850、12650、14250、15850、18250、19850、23050、23850
7. constexpr uint64_t DEFAULT_BITRATE = 10200;
8. // 配置音频声道数（必须）
9. constexpr uint32_t DEFAULT_CHANNEL_COUNT = 1;
10. // 配置音频声道类型（必须）
11. constexpr OH_AudioChannelLayout CHANNEL_LAYOUT = OH_AudioChannelLayout::CH_LAYOUT_MONO;
12. // 配置音频位深（必须）
13. constexpr OH_BitsPerSample SAMPLE_FORMAT = OH_BitsPerSample::SAMPLE_S16LE;
14. OH_AVFormat *format = OH_AVFormat_Create();
15. // 写入format
16. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_CHANNEL_COUNT, DEFAULT_CHANNEL_COUNT);
17. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_SAMPLE_RATE, DEFAULT_SAMPLERATE);
18. OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, DEFAULT_BITRATE);
19. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_SAMPLE_FORMAT, SAMPLE_FORMAT);
20. OH_AVFormat_SetLongValue(format, OH_MD_KEY_CHANNEL_LAYOUT, CHANNEL_LAYOUT);
21. // 配置编码器
22. ret = OH_AudioCodec_Configure(audioEnc_, format);
23. if (ret != AV_ERR_OK) {
24. // 异常处理
25. }
```

例opus编码调用流程：

```
1. int32_t ret;
2. // 配置音频采样率（必须）
3. // opus编码支持采样率：8000、12000、16000、24000、48000
4. constexpr uint32_t DEFAULT_SAMPLERATE = 8000;
5. // 配置音频码率（必须）
6. // opus编码码率范围：[6000, 510000]
7. constexpr uint64_t DEFAULT_BITRATE = 6000;
8. // 配置音频声道数（必须）
9. // opus编码支持声道数：1、2
10. constexpr uint32_t DEFAULT_CHANNEL_COUNT = 1;
11. // 配置音频位深（必须）
12. // opus编码支持位深：SAMPLE_S16LE
13. constexpr OH_BitsPerSample SAMPLE_FORMAT = OH_BitsPerSample::SAMPLE_S16LE;
14. OH_AVFormat *format = OH_AVFormat_Create();
15. // 写入format
16. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_CHANNEL_COUNT, DEFAULT_CHANNEL_COUNT);
17. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_SAMPLE_RATE, DEFAULT_SAMPLERATE);
18. OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, DEFAULT_BITRATE);
19. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_SAMPLE_FORMAT, SAMPLE_FORMAT);
20. // 配置编码器
21. ret = OH_AudioCodec_Configure(audioEnc_, format);
22. if (ret != AV_ERR_OK) {
23. // 异常处理
24. }
```

1. 调用OH\_AudioCodec\_Prepare()，编码器就绪。

   ```
   1. int32_t ret = OH_AudioCodec_Prepare(audioEnc_);
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
   10. // 配置编码文件输出路径（此处以输出为编码码流文件为例）。
   11. outFile_.open(outputFilePath, ios::out | ios::binary);
   12. // 开始编码。
   13. int32_t ret = OH_AudioCodec_Start(audioEnc_);
   14. if (ret != AV_ERR_OK) {
   15. // 异常处理。
   16. }
   ```
3. 调用OH\_AudioCodec\_PushInputBuffer()，写入待编码的数据。需开发者填充完整的输入数据后调用。

   每次输入的采样点数（SAMPLES\_PER\_FRAME）取值方法如下：

   AAC-LC编码每帧包含1024个PCM样点，建议单次输入1024个样点的数据量。

   HE-AAC编码每帧包含2048个PCM样点，建议单次输入2048个样点的数据量。

   flac比较特殊，需要根据如下表格进行设置。

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

   说明

   单次编码输入的数据量（单位：字节）为：采样点数（SAMPLES\_PER\_FRAME） \* 声道数 \* 单个采样点的占用字节。

   flac编码的样点数建议参考表格根据采样率对应的样点数进行设置，否则可能出现编码文件损坏问题。

   ```
   1. // 声道数。
   2. constexpr int32_t DEFAULT_CHANNEL_COUNT = 2;
   3. // 采样点数，这里以AAC-LC为例，采样点数为1024。
   4. constexpr int32_t SAMPLES_PER_FRAME = 1024;
   5. // 单次编码输入的数据量（单位：字节）为：采样点数 * 声道数 * 单个采样点的占用字节（以采样格式SAMPLE_S16LE为例）。
   6. // 如果最后一帧数据不满足长度，建议进行丢弃或填充处理。
   7. constexpr int32_t INPUT_FRAME_BYTES = SAMPLES_PER_FRAME * DEFAULT_CHANNEL_COUNT * sizeof(short);
   8. uint32_t index = signal_->inQueue_.front();
   9. auto buffer = signal_->inBufferQueue_.front();
   10. OH_AVCodecBufferAttr attr = {0};
   11. if (!inputFile_.eof()) {
   12. inputFile_.read((char *)OH_AVBuffer_GetAddr(buffer), INPUT_FRAME_BYTES);
   13. attr.size = INPUT_FRAME_BYTES;
   14. attr.flags = AVCODEC_BUFFER_FLAGS_NONE;
   15. } else {
   16. attr.size = 0;
   17. attr.flags = AVCODEC_BUFFER_FLAGS_EOS;
   18. }
   19. OH_AVBuffer_SetBufferAttr(buffer, &attr);
   20. // 送入编码输入队列进行编码, index为对应队列下标。
   21. int32_t ret = OH_AudioCodec_PushInputBuffer(audioEnc_, index);
   22. if (ret != AV_ERR_OK) {
   23. // 异常处理。
   24. }
   ```

   在上方案例中，attr.flags代表缓冲区标记的类别。

   结束时需要将flags标识为AVCODEC\_BUFFER\_FLAGS\_EOS。

   | 枚举值 | 描述 |
   | --- | --- |
   | AVCODEC\_BUFFER\_FLAGS\_NONE | 表示为普通帧。 |
   | AVCODEC\_BUFFER\_FLAGS\_EOS | 表示缓冲区是流结束帧。 |
   | AVCODEC\_BUFFER\_FLAGS\_CODEC\_DATA | 表示缓冲区包含编解码特定数据。 |
4. 调用OH\_AudioCodec\_FreeOutputBuffer()，释放编码后的数据。

   在取走编码码流后，就应及时调用OH\_AudioCodec\_FreeOutputBuffer()进行释放。

   ```
   1. uint32_t index = signal_->outQueue_.front();
   2. OH_AVBuffer *avBuffer = signal_->outBufferQueue_.front();
   3. if (avBuffer == nullptr) {
   4. // 异常处理
   5. }
   6. // 获取buffer attributes。
   7. OH_AVCodecBufferAttr attr = {0};
   8. int32_t ret = OH_AVBuffer_GetBufferAttr(avBuffer, &attr);
   9. if (ret != AV_ERR_OK) {
   10. // 异常处理。
   11. }
   12. // 将编码完成数据data写入到对应输出文件中。
   13. outFile_.write(reinterpret_cast<char *>(OH_AVBuffer_GetAddr(avBuffer)), attr.size);
   14. // 释放已完成写入的数据。
   15. ret = OH_AudioCodec_FreeOutputBuffer(audioEnc_, index);
   16. if (ret != AV_ERR_OK) {
   17. // 异常处理。
   18. }
   19. if (attr.flags == AVCODEC_BUFFER_FLAGS_EOS) {
   20. // 结束。
   21. }
   ```
5. （可选）调用OH\_AudioCodec\_Flush()刷新编码器。

   调用OH\_AudioCodec\_Flush()后，编码器处于Flush状态，会将当前编码队列清空。

   此时需要调用OH\_AudioCodec\_Start()重新开始编码。

   使用情况：

   * 在编码输出buffer属性为AVCODEC\_BUFFER\_FLAGS\_EOS后，若想重新使用相同配置进行编码时，需要调用刷新。
   * 在执行过程中遇到可继续执行的错误时（即OH\_AudioCodec\_IsValid()为true）可以调用刷新，然后调用OH\_AudioCodec\_Start()重新开始编码。

   ```
   1. // 刷新编码器 audioEnc_。
   2. int32_t ret = OH_AudioCodec_Flush(audioEnc_);
   3. if (ret != AV_ERR_OK) {
   4. // 异常处理。
   5. }
   6. // 重新开始编码。
   7. ret = OH_AudioCodec_Start(audioEnc_);
   8. if (ret != AV_ERR_OK) {
   9. // 异常处理。
   10. }
   ```
6. （可选）调用OH\_AudioCodec\_Reset()重置编码器。

   调用OH\_AudioCodec\_Reset()后，编码器回到初始化状态，重置前获取到的输入/输出buffer都无法继续使用，需先调用OH\_AudioCodec\_Configure()重新配置，再调用OH\_AudioCodec\_Start()重新开始编码。启动后重新获取输入/输出buffer。

   ```
   1. // 重置编码器 audioEnc_。
   2. int32_t ret = OH_AudioCodec_Reset(audioEnc_);
   3. if (ret != AV_ERR_OK) {
   4. // 异常处理。
   5. }
   6. // 重新配置编码器参数。
   7. ret = OH_AudioCodec_Configure(audioEnc_, format);
   8. if (ret != AV_ERR_OK) {
   9. // 异常处理。
   10. }
   ```
7. 调用OH\_AudioCodec\_Stop()停止编码器。

   停止后，可以通过调用OH\_AudioCodec\_Start()重新进入已启动状态（started）。停止前获取到的输入/输出buffer都无法继续使用，需要在启动后重新获取输入/输出buffer。

   ```
   1. // 终止编码器 audioEnc_。
   2. int32_t ret = OH_AudioCodec_Stop(audioEnc_);
   3. if (ret != AV_ERR_OK) {
   4. // 异常处理。
   5. }
   ```
8. 调用OH\_AudioCodec\_Destroy()销毁编码器实例，释放资源。

   说明

   禁止重复销毁编码器。

   ```
   1. // 调用OH_AudioCodec_Destroy, 销毁编码器。
   2. int32_t ret = OH_AudioCodec_Destroy(audioEnc_);
   3. if (ret != AV_ERR_OK) {
   4. // 异常处理。
   5. } else {
   6. audioEnc_ = NULL; // 不可重复destroy。
   7. }
   ```
