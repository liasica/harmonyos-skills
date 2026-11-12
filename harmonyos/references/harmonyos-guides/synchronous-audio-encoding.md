---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/synchronous-audio-encoding
title: 音频编码同步模式
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > 音频编码同步模式
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:b231f10ec3dde28872fb766e7591d069d01fe49890d2bd67263f74c22d056c96
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

示例代码引用了示例工程中自定义的工具宏与数据结构（如CHECK\_AND\_RETURN\_RET\_LOG、AVCODEC\_SAMPLE\_ERR\_\*、AVCODEC\_SAMPLE\_LOG\*、CodecUserData、CodecBufferInfo、SampleInfo等），不属于SDK的接口，完整定义请参见示例工程，移植时需自行实现或替换。

在应用开发过程中，开发者应按一定顺序调用方法，执行对应操作，否则系统可能会抛出异常或生成其他未定义的行为。具体顺序可参考下列开发步骤及对应说明。

音频编解码同步模式调用关系图如下所示：

* 虚线表示可选。音频编码不涉及解密，无需调用OH\_AudioCodec\_SetDecryptionConfig。
* 实线表示必选。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/WYuT9DYwQ2C943AoKYihmw/zh-cn_image_0000002786359860.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=7108E3F739F1BB8F98056EB64A0337B72656D859F90AA130399A58B60AFB3DC4)

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

   * 方法一：通过mime type创建编码器。

   ```
   int32_t AudioEncoder::Create(const std::string &codecMime)
   {
       // 设置判定是否为编码。true表示当前是编码。
       constexpr bool isEncoder = true;
       // 通过mime type创建编码器。此处传入的mime type以实际编码格式为准。
       encoder_ = OH_AudioCodec_CreateByMime(codecMime.c_str(), isEncoder);
       CHECK_AND_RETURN_RET_LOG(encoder_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Create failed");
       return AVCODEC_SAMPLE_ERR_OK;
   }
   ```

   * 方法二：通过codec name创建编码器。

   ```
   int32_t AudioEncoder::CreateByName(const std::string &codecMime)
   {
       // 通过codec name创建编码器。
       OH_AVCapability *capability = OH_AVCodec_GetCapability(codecMime.c_str(), true);
       CHECK_AND_RETURN_RET_LOG(capability != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "GetCapability failed");
       const char *name = OH_AVCapability_GetName(capability);
       encoder_ = OH_AudioCodec_CreateByName(name);
       CHECK_AND_RETURN_RET_LOG(encoder_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "CreateByName failed");
       return AVCODEC_SAMPLE_ERR_OK;
   }
   ```
3. 调用OH\_AudioCodec\_Configure配置编码器。

   配置选项key值说明：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/99PIyz4YQOyEpQ96wEZCTQ/zh-cn_image_0000002815399363.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=F2D558239EDCFDC632FE92F77D4C8BABD661A35929594BA8A94D250C103E4FA5)

   各音频编码类型参数范围说明：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/ycdnVUKCSuG1TWRL0vEhLA/zh-cn_image_0000002786519788.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=7A04DBEBE4C37FECCEE931D70FD8D5BE9381F09024CEC2C60B8473A3B34D5E9F)

   例如，对44100Hz采样率、2声道立体声、SAMPLE\_S16LE采样格式的PCM音频，以32000bps的码率进行AAC编码的调用流程如下：

   配置前建议先通过OH\_AVCapability能力查询接口校验待配置参数是否在编码器支持范围内。同步模式通过OH\_MD\_KEY\_ENABLE\_SYNC\_MODE开启：需要使用同步模式时，在Configure传入的OH\_AVFormat中将OH\_MD\_KEY\_ENABLE\_SYNC\_MODE设置为1；示例中根据是否使用同步模式决定是否设置该参数。

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

   示例工程将OH\_AudioCodec\_Prepare()封装在Config()函数中调用：在Config()函数中先完成Configure()配置，之后再调用OH\_AudioCodec\_Prepare()使编码器就绪。以下为其中Prepare部分的代码：

   ```
   {
       // 编码器就绪。
       int ret = OH_AudioCodec_Prepare(encoder_);
       CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Prepare failed, ret: %{public}d", ret);
   }
   ```
2. 调用OH\_AudioCodec\_Start()启动编码器，进入运行态。

   ```
   int32_t AudioEncoder::Start()
   {
       CHECK_AND_RETURN_RET_LOG(encoder_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Encoder is null");

       int ret = OH_AudioCodec_Start(encoder_);
       CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Start failed, ret: %{public}d", ret);
       return AVCODEC_SAMPLE_ERR_OK;
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

   主动请求输入buffer：先通过OH\_AudioCodec\_QueryInputBuffer()查询可用的输入buffer索引，超时返回AV\_ERR\_TRY\_AGAIN\_LATER，再通过OH\_AudioCodec\_GetInputBuffer()获取该输入buffer。

   ```
   OH_AVBuffer *AudioEncoder::GetInputBuffer(CodecBufferInfo &info, int64_t timeoutUs)
   {
       CHECK_AND_RETURN_RET_LOG(encoder_ != nullptr, nullptr, "Encoder is null");
       auto ret = OH_AudioCodec_QueryInputBuffer(encoder_, &info.bufferIndex, timeoutUs);
       switch (ret) {
           case AV_ERR_OK: {
               OH_AVBuffer *buffer = OH_AudioCodec_GetInputBuffer(encoder_, info.bufferIndex);
               CHECK_AND_RETURN_RET_LOG(buffer != nullptr, nullptr, "Input buffer is null");
               // 该Buffer只能在PushInputData前填充；提交后所有权回到codec。
               info.buffer = buffer;
               return buffer;
           }
           case AV_ERR_TRY_AGAIN_LATER: {
               AVCODEC_SAMPLE_LOGE("Get input buffer timeout.");
               return nullptr;
           }
           default: {
               return nullptr;
           }
       }
       return nullptr;
   }
   ```

   需开发者填充完整的输入数据后调用。示例中以麦克风录音（AudioCapturer）作为PCM数据来源，录音数据先写入应用自定义的PCM缓存，攒够一个输入buffer的数据量后填充到编码器输入buffer并送入编码器，同步输入线程示例如下：

   ```
   void Recorder::AudioEncInputSyncThread()
   {
       while (true) {
           CHECK_AND_BREAK_LOG(isStarted_, "Audio encoder sync thread out");
           // 收到EOS后停止提交新输入，但输出线程仍会继续排空已编码样本。
           if (isEos_.load()) {
               AVCODEC_SAMPLE_LOGI("Audio input thread received EOS signal, stopping input");
               break;
           }
           // 等待缓存凑满一帧；不完整音频数据会造成时长和时间戳异常。
           if (!WaitForAudioInputFrame(100ms)) {
               if (!isStarted_ || isEos_.load()) {
                   break;
               }
               continue;
           }
           // 数据充足后才可以申请codec输入Buffer；减少申请成功后因缓存不足无法及时归还的风险。
           CodecBufferInfo bufferInfo;
           bufferInfo.bufferIndex = std::numeric_limits<uint32_t>::max();
           auto buffer = audioEncoder_->GetInputBuffer(bufferInfo, TIMEOUT_US);
           if (buffer == nullptr) {
               if (bufferInfo.bufferIndex != std::numeric_limits<uint32_t>::max()) {
                   // Query已成功但Get失败时，索引可能仍由应用持有；结束会话交由codec回收。
                   AbortRecording("Synchronous audio input buffer retrieval failed");
                   break;
               }
               AVCODEC_SAMPLE_LOGW("Get input buffer timeout, retry");
               continue;
           }
           if (!SubmitAudioInputFrame(bufferInfo, buffer, true)) {
               break;
           }
       }
   }
   ```

   在上方案例中，attr.flags表示缓冲区标记的类别。

   结束时需要将flags标识为AVCODEC\_BUFFER\_FLAGS\_EOS，示例中录制结束时获取一个输入buffer，填入长度为0的数据并标识EOS标志后送入编码器。

   ```
   int32_t AudioEncoder::NotifyEndOfStream()
   {
       CHECK_AND_RETURN_RET_LOG(encoder_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Encoder is null");

       // 使用空输入Buffer携带EOS。即使没有媒体数据也必须提交该Buffer，编码器才会输出尾部数据。
       CodecBufferInfo bufferInfo;
       auto buffer = GetInputBuffer(bufferInfo, TIMEOUT_US);
       if (buffer == nullptr) {
           AVCODEC_SAMPLE_LOGW("GetInputBuffer for EOS failed");
           return AVCODEC_SAMPLE_ERR_ERROR;
       }

       // EOS不包含有效音频字节；调用PushInputBuffer后该Buffer立即归codec管理。
       bufferInfo.attr.size = 0;
       bufferInfo.attr.flags = AVCODEC_BUFFER_FLAGS_EOS;
       int32_t ret = OH_AVBuffer_SetBufferAttr(buffer, &bufferInfo.attr);
       if (ret != AV_ERR_OK) {
           AVCODEC_SAMPLE_LOGE("SetBufferAttr for EOS failed, ret: %{public}d", ret);
           return AVCODEC_SAMPLE_ERR_ERROR;
       }

       bufferInfo.buffer = buffer;
       ret = OH_AudioCodec_PushInputBuffer(encoder_, bufferInfo.bufferIndex);
       CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR,
                                "PushInputBuffer for EOS failed, ret: %{public}d", ret);
       return AVCODEC_SAMPLE_ERR_OK;
   }
   ```

   | 枚举值 | 描述 |
   | --- | --- |
   | AVCODEC\_BUFFER\_FLAGS\_NONE | 表示为普通帧。 |
   | AVCODEC\_BUFFER\_FLAGS\_EOS | 表示缓冲区是流结束帧。 |
   | AVCODEC\_BUFFER\_FLAGS\_CODEC\_DATA | 表示缓冲区包含编解码特定数据。 |

   获取编码输出：通过OH\_AudioCodec\_QueryOutputBuffer()查询可用输出buffer。当输入的数据量可以编码出多帧数据时，需要多次调用获取输出缓冲区，才能取完编码后的数据：

   ```
   int32_t AudioEncoder::GetOutputBuffer(CodecBufferInfo &info, int64_t timeoutUs)
   {
       info.buffer = nullptr;
       CHECK_AND_RETURN_RET_LOG(encoder_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Encoder is null");
       // 一批输入可能产生多帧输出，需要持续取出并归还，直到codec暂无输出或返回EOS。
       OH_AVErrCode ret = OH_AudioCodec_QueryOutputBuffer(encoder_, &info.bufferIndex, timeoutUs);
       if (ret == AV_ERR_TRY_AGAIN_LATER) {
           // 超时，可能输入的数据不足以编码出一帧，或者超时时间设置过短。
           AVCODEC_SAMPLE_LOGW("Get output buffer timeout.");
           return AVCODEC_SAMPLE_ERR_AGAIN; // continue;
       }
       if (ret != AV_ERR_OK) {
           AVCODEC_SAMPLE_LOGE("query output buffer failed, ret: %{public}d", ret);
           return AVCODEC_SAMPLE_ERR_ERROR; // break;
       }

       OH_AVBuffer *outputBuf = OH_AudioCodec_GetOutputBuffer(encoder_, info.bufferIndex);
       if (outputBuf == nullptr) {
           // 查询成功后索引已被codec交给应用，异常路径同样需要归还。
           const int32_t freeRet = OH_AudioCodec_FreeOutputBuffer(encoder_, info.bufferIndex);
           AVCODEC_SAMPLE_LOGE("Get output buffer failed, free ret: %{public}d", freeRet);
           return AVCODEC_SAMPLE_ERR_ERROR; // break;
       }
       ret = OH_AVBuffer_GetBufferAttr(outputBuf, &info.attr);
       if (ret != AV_ERR_OK) {
           const int32_t freeRet = OH_AudioCodec_FreeOutputBuffer(encoder_, info.bufferIndex);
           AVCODEC_SAMPLE_LOGE("Get output buffer attr failed, ret: %{public}d, free ret: %{public}d", ret, freeRet);
           return AVCODEC_SAMPLE_ERR_ERROR; // break;
       }

       info.buffer = outputBuf;
       if (info.attr.flags & AVCODEC_BUFFER_FLAGS_EOS) {
           AVCODEC_SAMPLE_LOGI("Out buffer EOS flag detected");
           return AVCODEC_SAMPLE_ERR_OK;
       }
       return AVCODEC_SAMPLE_ERR_OK;
   }
   ```

   在取走编码码流后，就应及时调用OH\_AudioCodec\_FreeOutputBuffer()释放输出buffer。示例中编码输出的码流写入封装模块，假如需要封装成音频文件，可参考[媒体数据封装](audio-video-muxer.md)。同步输出线程示例如下：

   ```
   void Recorder::AudioEncOutputSyncThread()
   {
       while (true) {
           CHECK_AND_BREAK_LOG(isStarted_, "Audio encoder output thread out");
           CodecBufferInfo bufferInfo;
           int32_t errCode = audioEncoder_->GetOutputBuffer(bufferInfo, TIMEOUT_US);
           if (errCode == AVCODEC_SAMPLE_ERR_OK) {
               AVCODEC_SAMPLE_LOGI("AVCODEC_SAMPLE_ERR_OK");
           } else if (errCode == AVCODEC_SAMPLE_ERR_END || errCode == AVCODEC_SAMPLE_ERR_ERROR) {
               AVCODEC_SAMPLE_LOGW("Audio output thread received END or ERROR");
               break;
           } else {
               AVCODEC_SAMPLE_LOGW("Get output buffer timeout, retry");
               continue;
           }

           audioEncContext_->outputFrameCount++;
           AVCODEC_SAMPLE_LOGW(
               "Audio Out buffer sync count: %{public}u, size: %{public}d, flag: %{public}u, pts: %{public}" PRId64,
               audioEncContext_->outputFrameCount, bufferInfo.attr.size, bufferInfo.attr.flags, bufferInfo.attr.pts);
           const bool isEosBuffer = (bufferInfo.attr.flags & AVCODEC_BUFFER_FLAGS_EOS) != 0;
           int32_t writeRet = AVCODEC_SAMPLE_ERR_OK;
           if (!isEosBuffer && bufferInfo.attr.size > 0) {
               // Muxer写入不接管Buffer；两个目标写完后仍需显式归还原索引。
               writeRet = muxer_->WriteSample(muxer_->GetAudioTrackId(), bufferInfo.buffer, bufferInfo.attr);
               if (writeRet == AVCODEC_SAMPLE_ERR_OK && secondaryMuxer_ != nullptr) {
                   writeRet = secondaryMuxer_->WriteSample(secondaryMuxer_->GetAudioTrackId(), bufferInfo.buffer,
                       bufferInfo.attr);
               }
           }
           int32_t ret = audioEncoder_->FreeOutputData(bufferInfo.bufferIndex);
           CHECK_AND_BREAK_LOG(ret == AVCODEC_SAMPLE_ERR_OK, "Encoder output thread out");
           if (writeRet != AVCODEC_SAMPLE_ERR_OK) {
               AbortRecording("Write encoded audio sample failed");
               break;
           }
           if (isEosBuffer) {
               isAudioEos_.store(true);
               videoEosCond_.notify_all();
               AVCODEC_SAMPLE_LOGI("Audio EOS processed, exiting output thread");
               break;
           }
       }
       // 同步模式仍由视频线程触发释放；音频先结束时，视频仍在使用Muxer。
       AVCODEC_SAMPLE_LOGI("Audio output thread exited, waiting for video thread to trigger release");
   }
   ```
4. （可选）调用OH\_AudioCodec\_Reset()重置编码器。

   调用OH\_AudioCodec\_Reset()后，编码器回到初始化状态，重置前获取到的输入/输出buffer都无法继续使用，需先调用OH\_AudioCodec\_Configure()重新配置，再调用OH\_AudioCodec\_Start()重新开始编码。启动后重新获取输入/输出buffer。

   ```
   int32_t AudioEncoder::Reset()
   {
       CHECK_AND_RETURN_RET_LOG(encoder_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Encoder is null");

       // 重置编码器，之后需要重新调用Configure()配置、Start()启动。
       int32_t ret = OH_AudioCodec_Reset(encoder_);
       CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Reset failed, ret: %{public}d", ret);
       return AVCODEC_SAMPLE_ERR_OK;
   }
   ```
5. （可选）调用OH\_AudioCodec\_Stop()停止编码器。

   停止后，可以通过调用OH\_AudioCodec\_Start()重新进入已启动状态（started）。停止前获取到的输入/输出buffer都无法继续使用，需要在启动后重新获取输入/输出buffer。

   ```
   int32_t AudioEncoder::Stop()
   {
       CHECK_AND_RETURN_RET_LOG(encoder_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Encoder is null");

       int ret = Flush();
       CHECK_AND_RETURN_RET_LOG(ret == AVCODEC_SAMPLE_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR,
                                "Flush failed, ret: %{public}d", ret);

       ret = OH_AudioCodec_Stop(encoder_);
       CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Stop failed, ret: %{public}d", ret);
       return AVCODEC_SAMPLE_ERR_OK;
   }
   ```
6. 调用OH\_AudioCodec\_Destroy()销毁编码器实例，释放资源。

   **说明** 

   禁止重复销毁编码器。

   ```
   int32_t AudioEncoder::Release()
   {
       if (encoder_ != nullptr) {
           // 销毁前刷新并停止编码器，不可重复destroy。
           Flush();
           Stop();
           OH_AudioCodec_Destroy(encoder_);
           encoder_ = nullptr;
       }
       return AVCODEC_SAMPLE_ERR_OK;
   }
   ```
