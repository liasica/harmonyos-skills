---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/synchronous-audio-encoding
title: 音频编码同步模式
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > 音频编码同步模式
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:46+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:9efbccedb2658de5c0386c7fba5f9f8e34489bf7d31a7f930f97457601067846
---

从API version 20开始，支持音频编码同步模式。

开发者可以调用本模块的Native API接口，完成音频编码，即将音频PCM编码压缩成不同的格式。

接口不限制PCM数据的来源。开发者可以调用麦克风录制获取，也可以导入编辑后的PCM数据。通过音频编码，输出对应格式的码流，最后封装为目标格式文件。

支持的编码能力请参考[AVCodec支持的格式](avcodec-support-formats.md#音频编码)。

**适用场景**

通常推荐使用异步模式，异步模式请参考[音频编码](audio-encoding.md)。若需要主动请求buffer去编码PCM，则可以使用同步模式。

* 音频录制

  通过录制传入PCM，然后编码成对应格式的码流，最后封装成所需格式的文件。具体封装方法请参考[媒体数据封装](audio-video-muxer.md)。
* 音频编辑

  编辑PCM后导出音频文件的场景，需要编码成对应音频格式，最后封装成所需格式的文件。具体封装方法请参考[媒体数据封装](audio-video-muxer.md)。

**说明** 

* AAC编码器默认采用的VBR可变码率模式，这可能导致与预期码率有偏差。
* AAC编码器默认输出携带ADTS头部，帧数据的前7字节为ADTS头部。

## 开发指导

详细的API说明请参考[AudioCodec](../harmonyos-references/capi-native-avcodec-audiocodec-h.md)。

参考以下示例代码，完成音频编码的全流程，包括：创建编码器、设置编码参数（采样率/码率/声道数等）、开始/刷新/重置/销毁资源。

在应用开发过程中，开发者应按一定顺序调用方法，执行对应操作，否则系统可能会抛出异常或生成其他未定义的行为。具体顺序可参考下列开发步骤及对应说明。

音频编解码同步模式调用关系图如下所示：

* 虚线表示可选。音频编码不涉及解密，无需调用OH\_AudioCodec\_SetDecryptionConfig。
* 实线表示必选。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/D1OPrC3ORvq-vDBQE2dgcw/zh-cn_image_0000002742123639.png)

### 在CMake脚本中链接动态库

```cmake
target_link_libraries(sample PUBLIC libnative_media_codecbase.so)
target_link_libraries(sample PUBLIC libnative_media_core.so)
target_link_libraries(sample PUBLIC libnative_media_acodec.so)
```

**说明** 

上述'sample'字样仅为示例，此处由开发者根据实际工程目录自定义。

### 开发步骤

1. 添加头文件和命名空间。

   ```cpp
   #include <multimedia/player_framework/native_avcodec_audiocodec.h>
   #include <multimedia/native_audio_channel_layout.h>
   #include <multimedia/player_framework/native_avcapability.h>
   #include <multimedia/player_framework/native_avcodec_base.h>
   #include <multimedia/player_framework/native_avformat.h>
   #include <multimedia/player_framework/native_avbuffer.h>

   // c++标准库命名空间。
   using namespace std;
   ```
2. 创建编码器实例对象，OH\_AVCodec \*为编码器实例指针。

   应用可以通过媒体类型或编解码器名称创建编码器。

   方法一：通过Mimetype创建编码器。

   ```cpp
   // 通过Mimetype创建编码器，这里示例创建的是AAC编码器，第二个参数设置为true表示当前是编码。
   OH_AVCodec *audioEnc_ = OH_AudioCodec_CreateByMime(OH_AVCODEC_MIMETYPE_AUDIO_AAC, true);
   ```

   方法二：通过codec name创建编码器。

   ```cpp
   // 通过codec name创建编码器。
   OH_AVCapability *capability = OH_AVCodec_GetCapability(OH_AVCODEC_MIMETYPE_AUDIO_AAC, true);
   const char *name = OH_AVCapability_GetName(capability);
   OH_AVCodec *audioEnc_ = OH_AudioCodec_CreateByName(name);
   ```
3. 调用OH\_AudioCodec\_Configure配置编码器。

   配置选项key值说明：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/9ZNwO9hUS_K-U7rw7ybH8g/zh-cn_image_0000002742003677.png)

   各音频编码类型参数范围说明：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/y2Alf-4tQ5q7ieAjxTe_sw/zh-cn_image_0000002712404690.png)

   例如，对44100Hz采样率、2声道立体声、SAMPLE\_S16LE采样格式的PCM音频，以32000bps的码率进行AAC编码的调用流程如下：

```cpp
   OH_AVErrCode ret;
   // 配置音频采样率（必须）
   constexpr uint32_t DEFAULT_SAMPLERATE = 44100;
   // 配置音频码率（必须）
   constexpr uint64_t DEFAULT_BITRATE = 32000;
   // 配置音频声道数（必须）
   constexpr uint32_t DEFAULT_CHANNEL_COUNT = 2;
   // 配置音频位深（必须）
   constexpr OH_BitsPerSample SAMPLE_FORMAT = OH_BitsPerSample::SAMPLE_S16LE;
   // 配置AAC profile（可选，默认值：AAC_PROFILE_LC，其他可选值：AAC_PROFILE_HE、AAC_PROFILE_HE_V2）
   constexpr int32_t AAC_PROFILE = OH_AACProfile::AAC_PROFILE_LC;
   OH_AVFormat *format = OH_AVFormat_Create();
   // 写入format
   OH_AVFormat_SetIntValue(format,OH_MD_KEY_AUD_CHANNEL_COUNT, DEFAULT_CHANNEL_COUNT);
   OH_AVFormat_SetIntValue(format,OH_MD_KEY_AUD_SAMPLE_RATE, DEFAULT_SAMPLERATE);
   OH_AVFormat_SetLongValue(format,OH_MD_KEY_BITRATE, DEFAULT_BITRATE);
   OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_SAMPLE_FORMAT, SAMPLE_FORMAT);
   OH_AVFormat_SetLongValue(format,OH_MD_KEY_CHANNEL_LAYOUT, CHANNEL_LAYOUT);
   OH_AVFormat_SetIntValue(format, OH_MD_KEY_PROFILE, AAC_PROFILE);
   OH_AVFormat_SetIntValue(format, OH_MD_KEY_ENABLE_SYNC_MODE, 1); // 同步模式配置。
   // 配置编码器
   ret = OH_AudioCodec_Configure(audioEnc_, format);
   if (ret != AV_ERR_OK) {
       // 异常处理
   }
```

FLAC编码调用示例：

```cpp
OH_AVErrCode ret;
// 配置音频采样率（必须）。
constexpr uint32_t DEFAULT_SAMPLERATE = 44100;
// 配置音频码率（必须）。
constexpr uint64_t DEFAULT_BITRATE = 261000;
// 配置音频声道数（必须）。
constexpr uint32_t DEFAULT_CHANNEL_COUNT = 2;
// 配置音频声道布局（必须）。
// 值为CH_LAYOUT_MONO、CH_LAYOUT_STEREO、CH_LAYOUT_SURROUND、CH_LAYOUT_QUAD、CH_LAYOUT_5POINT0、CH_LAYOUT_5POINT1、CH_LAYOUT_6POINT1或CH_LAYOUT_7POINT1其中一项。
constexpr OH_AudioChannelLayout CHANNEL_LAYOUT = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
// 配置音频位深（必须） FLAC只有SAMPLE_S16LE和SAMPLE_S32LE。
constexpr OH_BitsPerSample SAMPLE_FORMAT = OH_BitsPerSample::SAMPLE_S32LE;
// 配置音频compliance level（默认值0，取值范围[-2,2]）。
constexpr int32_t COMPLIANCE_LEVEL = 0;

OH_AVFormat *format = OH_AVFormat_Create();
// 写入format。
OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_CHANNEL_COUNT, DEFAULT_CHANNEL_COUNT);
OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_SAMPLE_RATE, DEFAULT_SAMPLERATE);
OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, DEFAULT_BITRATE);
OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_SAMPLE_FORMAT, SAMPLE_FORMAT);
OH_AVFormat_SetLongValue(format, OH_MD_KEY_CHANNEL_LAYOUT, CHANNEL_LAYOUT);
OH_AVFormat_SetLongValue(format, OH_MD_KEY_COMPLIANCE_LEVEL, COMPLIANCE_LEVEL);
OH_AVFormat_SetIntValue(format, OH_MD_KEY_ENABLE_SYNC_MODE, 1); // 同步模式配置。
// 配置编码器。
ret = OH_AudioCodec_Configure(audioEnc_, format);
if (ret != AV_ERR_OK) {
    // 异常处理。
}
```

除上述配置的参数外，还可以在Configure阶段配置以下可选参数：

* OH\_MD\_KEY\_AUDIO\_MAX\_INPUT\_BUFFER\_SIZE：配置音频编码器最大输入缓冲区大小（单位：字节）。FLAC、MP3等帧对齐编码器设置该参数后会启用内部PCM缓存机制，允许输入数据无需按帧大小对齐，编码器会自动进行缓存与拆帧。实际缓冲区大小受编码器实现限制，如果设置的值超出上限，会被设置为上限值（上限为10MB）。
* OH\_MD\_KEY\_AUDIO\_ENCODER\_PTS\_MODE：配置音频编码器输出PTS模式，值类型为[OH\_AudioEncoderPTSMode](../harmonyos-references/capi-native-avcodec-base-h.md#oh_audioencoderptsmode)。不同模式下输出帧的PTS计算方式不同：

  + OH\_AUDIO\_ENCODER\_PTS\_MODE\_DEFAULT：默认行为，不同编码器的PTS输出方式可能不同。
  + OH\_AUDIO\_ENCODER\_PTS\_MODE\_ZERO\_START：PTS从0开始，按帧时长递增。适用于不依赖输入PTS、需要从0开始计时的场景。
  + OH\_AUDIO\_ENCODER\_PTS\_MODE\_FIRST\_INPUT\_START：PTS从首个输入帧的PTS开始，按帧时长递增。适用于需要保持与输入流PTS连续性的场景。
* OH\_MD\_KEY\_AUDIO\_ENCODER\_ENABLE\_SAMPLE\_FORMAT\_CONVERT：配置音频编码器采样格式转换开关，1表示开启，0表示关闭（默认）。音频编码器原生支持的采样格式有限（例如G711mu仅支持SAMPLE\_S16LE），开启后编码器会自动将输入的PCM数据转换为编码器支持的格式进行编码，支持的输入采样格式扩展为：SAMPLE\_U8、SAMPLE\_S16LE、SAMPLE\_S24LE、SAMPLE\_S32LE、SAMPLE\_F32LE。适用于输入PCM格式与编码器原生格式不一致的场景。

```cpp
// 配置编码器最大输入缓冲区大小（可选），FLAC/MP3设置后可接受非帧对齐的输入数据。此处4096仅为参考值，开发者可按实际需要动态设置。
OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_MAX_INPUT_BUFFER_SIZE, 4096);
// 配置编码器PTS输出模式（可选）。
OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_ENCODER_PTS_MODE,
    OH_AUDIO_ENCODER_PTS_MODE_FIRST_INPUT_START);
// 配置编码器采样格式转换开关（可选），开启后支持更多采样格式输入。
OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_ENCODER_ENABLE_SAMPLE_FORMAT_CONVERT, 1);
```

1. 调用OH\_AudioCodec\_Prepare()，编码器就绪。

   ```cpp
   OH_AVErrCode ret = OH_AudioCodec_Prepare(audioEnc_);
   if (ret != AV_ERR_OK) {
       // 异常处理。
   }
   ```
2. 调用OH\_AudioCodec\_Start()启动编码器，进入运行态。

   添加头文件：

   ```
   #include <fstream>
   ```

   使用示例：

   ```
   ifstream inputFile_;
   ofstream outFile_;

   // 根据实际使用情况填写输入文件路径。
   const char* inputFilePath = "/";
   // 根据实际使用情况填写输出文件路径。
   const char* outputFilePath = "/";
   // 打开待编码二进制文件路径（此处以输入为PCM文件为例）。
   inputFile_.open(inputFilePath, ios::in | ios::binary);
   // 配置编码文件输出路径（此处以输出为编码码流文件为例，并非可播放的音频文件，可播放的音频文件需要音频码流封装到容器内生成）。
   outFile_.open(outputFilePath, ios::out | ios::binary);
   // 开始编码。
   OH_AVErrCode ret = OH_AudioCodec_Start(audioEnc_);
   if (ret != AV_ERR_OK) {
       // 异常处理。
   }
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
   int32_t SAMPLES_PER_FRAME = 1024;
   // AAC LC编码一帧包含1024采样点，2声道，输入数据为S16LE，16比特数据，占用2字节。
   int32_t inputFrameBytes = SAMPLES_PER_FRAME * 2 * 2;
   bool inputFinished = false;
   OH_AVErrCode ret;
   OH_AVCodecBufferAttr attr;

   for (;;) {
       uint32_t index = 0;
       if (!inputFinished) {
           ret = OH_AudioCodec_QueryInputBuffer(audioEnc_, &index, 20000); // 20000us
           if (ret == AV_ERR_TRY_AGAIN_LATER) {
               continue;
           }
           if (ret != AV_ERR_OK) {
               // 异常处理。
               break;
           }
           OH_AVBuffer *inputBuf = OH_AudioCodec_GetInputBuffer(audioEnc_, index);
           if (inputBuf == nullptr) {
               // 异常处理。
               break;
           }
           memset(&attr, 0, sizeof(attr));
           if (!inputFile_.eof()) {
               inputFile_.read((char *)OH_AVBuffer_GetAddr(inputBuf), inputFrameBytes);
               int32_t readSize = inputFile_.gcount();
               attr.size = readSize;
               attr.flags = readSize != 0 ? AVCODEC_BUFFER_FLAGS_NONE : AVCODEC_BUFFER_FLAGS_EOS;
           } else {
               inputFinished = true;
               attr.size = 0;
               attr.flags = AVCODEC_BUFFER_FLAGS_EOS;
           }
           if (OH_AVBuffer_SetBufferAttr(inputBuf, &attr) != AV_ERR_OK) {
               // 异常处理。
           }
           if (OH_AudioCodec_PushInputBuffer(audioEnc_, index) != AV_ERR_OK) {
               // 异常处理。
           }
       }
       // 当输入的数据量可以编码出多帧数据时，需要多次调用获取输出缓冲区，才能取完编码后的数据。
       ret = OH_AudioCodec_QueryOutputBuffer(audioEnc_, &index, 20000); // 20000us
       if (ret == AV_ERR_TRY_AGAIN_LATER) {
           // 超时，可能输入的数据不足以编码出一帧，或者超时时间设置过短。
           continue;
       }
       if (ret != AV_ERR_OK) {
           // 异常处理。
           break;
       }
       OH_AVBuffer *outputBuf = OH_AudioCodec_GetOutputBuffer(audioEnc_, index);
       if (outputBuf == nullptr) {
           // 异常处理。
           break;
       }
       if (OH_AVBuffer_GetBufferAttr(outputBuf, &attr) != AV_ERR_OK) {
           // 异常处理。
           break;
       }
       if (attr.flags & AVCODEC_BUFFER_FLAGS_EOS) {
           // 输出结束。
           break;
       }
       // 这里示例仅将数据写入文件记录。假如需要封装成音频文件，可参考媒体数据封装，调用OH_AVMuxer_WriteSampleBuffer封装数据。
       outFile_.write(reinterpret_cast<char *>(OH_AVBuffer_GetAddr(outputBuf)), attr.size);
       OH_AudioCodec_FreeOutputBuffer(audioEnc_, index);
   }
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
   // 重置编码器。
   OH_AVErrCode ret = OH_AudioCodec_Reset(audioEnc_);
   if (ret != AV_ERR_OK) {
       // 异常处理。
   }
   // 重新配置编码器参数。
   ret = OH_AudioCodec_Configure(audioEnc_, format);
   if (ret != AV_ERR_OK) {
       // 异常处理。
   }
   ```
5. （可选）调用OH\_AudioCodec\_Stop()停止编码器。

   停止后，可以通过调用OH\_AudioCodec\_Start()重新进入已启动状态（started）。停止前获取到的输入/输出buffer都无法继续使用，需要在启动后重新获取输入/输出buffer。

   ```
   // 停止编码器。
   OH_AVErrCode ret = OH_AudioCodec_Stop(audioEnc_);
   if (ret != AV_ERR_OK) {
       // 异常处理。
   }
   ```
6. 调用OH\_AudioCodec\_Destroy()销毁编码器实例，释放资源。

   **说明** 

   禁止重复销毁编码器。

   ```
   // 调用OH_AudioCodec_Destroy，销毁编码器。
   OH_AVErrCode ret = OH_AudioCodec_Destroy(audioEnc_);
   if (ret != AV_ERR_OK) {
       // 异常处理。
   } else {
       audioEnc_ = NULL; // 不可重复destroy。
   }
   ```
