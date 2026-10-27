---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/avcodec-kit-faq-0001
title: 音视频编解码与转码常见问题
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > 常见问题 > 音视频编解码与转码常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:33+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:3d6cfee98cc666ec3c5ca9ee853f98208d0a1c5bbbb3de10ce0ab45e42fbb4cf
---

**Q：音频文件如何从一种编码格式/封装格式转为另一种编码格式/封装格式？**

**A**：根据需要转换的目标音频格式不同，可以将转码需求分为两种场景：第一种场景是目标音频格式为封装格式；第二种场景是目标音频格式为编码格式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/MxEv1S_XQMaJd6A_07Eu9Q/zh-cn_image_0000002767826964.png "点击放大")

场景一，需要转为特定的封装格式：

* 音频格式为封装格式，转换为其它封装格式，例如使用AVPlayer录制音频，拿到.m4a格式的音频文件，现需要将此文件转为.amr格式。查看.m4a格式解封装后对应的编码格式为AAC，见流程图中case1,先将封装格式解封装得到AAC编码数据，再解码拿到PCM音频数据，.amr文件的音频编码格式为AMR，将PCM数据编码为AMR格式，再封装成.amr文件。

  如果原封装格式解码后的编码格式和目标封装格式支持的编码格式一致，此时只需要转封装无需转码。
* 音频格式为PCM原始数据，编码封装为.mp3格式的文件。

  将PCM音频数据转为.mp3文件，此场景见case2，PCM音频数据编码压缩成MP3格式，再封装成.mp3格式的文件。

场景二，需要转为特定的编码格式：

* 在实时语音传输系统中，需要将设备采集的amr-nb编码格式转为OPUS编码格式。见流程图中case3中amr-nb编码格式到OPUS编码格式，需解码成PCM格式再编码到OPUS编码格式。
* 流程图中case4，播放软件播放mp3音频时，需要将音频解封装到MPEG(MP3)编码格式再解码，拿到PCM音频数据输送到硬件扬声器播放。

  上述案例只是列举了几个较典型的场景，具体转换时请根据实际需要选择转封装或转码。

音视频编解码详细可参考[音频编码](../harmonyos-guides/audio-encoding.md)/[音频解码](../harmonyos-guides/audio-decoding.md)，封装解析可参考媒体文件的[封装](../harmonyos-guides/audio-video-muxer.md)与[解析](../harmonyos-guides/audio-video-demuxer.md)。

**Q：为什么PCM可以不经过编码直接封装为WAV？**

**A**：WAV是比较特殊的封装格式，它是一种无损格式，没有经过编码压缩，通过在PCM前加上一个44字节的文件头获得。

**Q：HarmonyOS应用中实现音频转码，目前是否有官方SDK可以将音频格式由AMR转为WAV？**

**A**：HarmonyOS暂无将AMR格式转为WAV格式的SDK，关于实现音频转码可参考：

方案一：将音频码流[解码](../harmonyos-guides/audio-decoding.md)为PCM码流，再[编码](../harmonyos-guides/audio-encoding.md)为WAV格式。

方案二：参考FFmpeg等第三方音频处理库。

**Q：AAC编码后是否会自动添加ADTS头吗？**

**A**：AAC编码器默认是带ADTS输出。

**Q：针对OH\_MD\_KEY\_AAC\_IS\_ADTS，AAC编码器支持配置吗？**

**A**：AAC编码器不支持配置OH\_MD\_KEY\_AAC\_IS\_ADTS。

**Q：如何确认创建的是编码器还是解码器？**

**A**：编解码器状态不是在运行时判断，而是在创建实例时进行设置的。通过[OH\_AudioCodec\_CreateByMime()](../harmonyos-references/capi-native-avcodec-audiocodec-h.md#oh_audiocodec_createbymime)中设置参数isEncoder，当参数值为true时创建编码器，反之则是创建解码器。

**Q：如何通过URL在线播放音频并获取AAC编码数据？**

**A**：整体步骤为解封装→音频解码→PCM→音频编码→AAC。解封装和音频解码为PCM流可参考AVCodec完整示例，主要参考audio\_decoder.cpp、audio\_encoder.cpp、demuxer.cpp等文件。需将[OH\_AVSource\_CreateWithFD](../harmonyos-references/capi-native-avsource-h.md#oh_avsource_createwithfd)替换为[OH\_AVSource\_CreateWithURI](../harmonyos-references/capi-native-avsource-h.md#oh_avsource_createwithuri)来支持通过URL创建媒体源。m3u8格式每次解封装得到的只有部分ts数据，需要持续读取。PCM编码为AAC格式可参考[音频编码](../harmonyos-guides/audio-encoding.md)开发步骤。

**Q：投屏或者视频直播类场景下，服务端与客户端之间视频流数据的传递采用H264格式编码，客户端需要持续接收H264裸流数据并实时解码送到页面渲染，如何实现这种功能？**

**A**：基于demo：[AVCodecVideo](https://gitee.com/harmonyos_samples/AVCodecVideo)。

针对Annex-B格式的H264数据流，修改工程当中的解封装步骤，可实现逐帧解码送显，修改步骤如下：

1. 修改解封装Demuxer创建过程（entry/src/main/cpp/capbilities/Demuxer.cpp的Create函数），解码器类型选择OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC，其余视频相关参数需要业务自行定义；

   ```
   int32_t Demuxer::Create(SampleInfo &info)
   {
       info.videoCodecMime = OH_AVCODEC_MIMETYPE_VIDEO_AVC;
       info.videoWidth = 1290; // 仅供参考，按业务实际情况修改
       info.videoHeight = 720; // 仅供参考，按业务实际情况修改
       info.frameRate = 52.390670553935863; // 仅供参考，按业务实际情况修改
       info.bitrate = 452184; // 仅供参考，按业务实际情况修改
       info.rotation = 0; // 仅供参考，按业务实际情况修改
       return AVCODEC_SAMPLE_ERR_OK;
   }
   ```
2. entry/src/main/cpp/sample/player/Player.cpp定义Annex-B和avcc相关常量：

   ```
   constexpr uint8_t ANNEXB_FRAME_HEAD[] = {0, 0, 0, 1};
   constexpr uint8_t ANNEXB_FRAME_HEAD_LEN = sizeof(ANNEXB_FRAME_HEAD);
   constexpr uint8_t AVCC_FRAME_HEAD_LEN = 4;
   ```
3. 修改视频流输入（entry/src/main/cpp/sample/player/Player.cpp的VideoDecInputThread函数），Annex-B格式的H264数据流需要根据数据帧前缀逐帧读取，（一般格式为0x00 00 00 01）把数据通过内存拷贝进输入buffer当中去，重新设置buffer的attr属性：

   ```
   void Player::VideoDecInputThread()
   {
       int32_t index = 0;
       uint8_t pBuffer[1500000];

       while (true) {
           int32_t buffSize = pread(sampleInfo_.inputFd, pBuffer, 1500000, index);
           CHECK_AND_BREAK_LOG(isStarted_, "Decoder input thread out");
           std::unique_lock<std::mutex> lock(videoDecContext_->inputMutex);
           bool condRet = videoDecContext_->inputCond.wait_for(
               lock, 5s, [this]() { return !isStarted_ || !videoDecContext_->inputBufferInfoQueue.empty(); });
           CHECK_AND_BREAK_LOG(isStarted_, "Work done, thread out");
           CHECK_AND_CONTINUE_LOG(!videoDecContext_->inputBufferInfoQueue.empty(),
                                  "Buffer queue is empty, continue, cond ret: %{public}d", condRet);

           CodecBufferInfo bufferInfo = videoDecContext_->inputBufferInfoQueue.front();
           videoDecContext_->inputBufferInfoQueue.pop();
           videoDecContext_->inputFrameCount++;
           lock.unlock();

           // 修改视频流输入，逐帧数据读取，拷贝至输入buffer内存当中，设置buffer的attr属性
           // 根据Annex-B格式数据前缀取帧
           int32_t bufferSize = OH_AVBuffer_GetCapacity(reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer));
           auto pos = std::search(pBuffer + ANNEXB_FRAME_HEAD_LEN,
               pBuffer + bufferSize, std::begin(ANNEXB_FRAME_HEAD), std::end(ANNEXB_FRAME_HEAD));
           uint32_t size = std::distance(pBuffer, pos);
           uint8_t * bufferArray = OH_AVBuffer_GetAddr(reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer)); // 通过OH_AVBuffer_GetAddr获取OH_AVBuffer内存地址
           memcpy(bufferArray, pBuffer, size); // 逐帧数据拷贝进OH_AVBuffer当中
           bufferInfo.attr.flags = IsCodecData(pBuffer) ? AVCODEC_BUFFER_FLAGS_CODEC_DATA : AVCODEC_BUFFER_FLAGS_NONE;
           bufferInfo.attr.size = size; // 设置帧buffer长度
           bufferInfo.attr.pts = videoDecContext_->inputFrameCount * ((sampleInfo_.frameInterval == 0) ? 1 : sampleInfo_.frameInterval) *
                       1000;
           OH_AVBuffer_SetBufferAttr(reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer), &bufferInfo.attr); // 通过OH_AVBuffer_SetBufferAttr设置输入buffer的attr属性，（必须，否则解码器没有输入数据）
           index += size;

           int32_t ret = videoDecoder_->PushInputBuffer(bufferInfo);
           CHECK_AND_BREAK_LOG(ret == AVCODEC_SAMPLE_ERR_OK, "Push data failed, thread out");

           CHECK_AND_BREAK_LOG(!(bufferInfo.attr.flags & AVCODEC_BUFFER_FLAGS_EOS), "Catch EOS, thread out");
       }
   }

   bool Player::IsCodecData(const uint8_t *const bufferAddr)
   {
       bool isH264Stream = true;

       // 0x1F:avc nalu type mask;0x7E:hevc nalu type mask
       uint8_t naluType =
           isH264Stream ? (bufferAddr[AVCC_FRAME_HEAD_LEN] & 0x1F) : ((bufferAddr[AVCC_FRAME_HEAD_LEN] & 0x7E) >> 1);

       constexpr uint8_t avcSps = 7;
       constexpr uint8_t avcPps = 8;
       constexpr uint8_t hevcVps = 32;
       constexpr uint8_t hevcSps = 33;
       constexpr uint8_t hevcPps = 34;
       if ((isH264Stream && ((naluType == avcSps) || (naluType == avcPps))) ||
           (!isH264Stream && ((naluType == hevcVps) || (naluType == hevcSps) || (naluType == hevcPps)))) {
           return true;
       }
       return false;
   }
   ```
4. 最终把entry/src/main/ets/pages/Index.ets当中的photoPicker改为documentPicker，即可尝试选取H264文件进行播放测试。

**Q：往解码器中喂帧，数据如何填充至OH\_AVBuffer当中？**

**A**：通过OH\_AVBuffer\_GetAddr获取OH\_AVBuffer内存地址，memcpy写入帧数据，通过OH\_AVBuffer\_SetBufferAttr设置输入buffer的长度等attr属性。

**Q：往解码器中喂帧，无视频流输出，输出buffer为空？**

**A**：OH\_AVBuffer\_SetBufferAttr设置attr属性时，需要先确保attr里flags、size、pts等字段的值正确，否则解码器无法正确获取输入流。

**Q：avcc格式如何播放？**

**A**：解码器只能处理Annex-B格式数据，avcc格式需要先转换为Annex-B再填充至OH\_AVBuffer当中。

**Q：H265格式的码流如何播放？**

**A**：同理，修改解码器MIME类型为OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC即可，更多格式可参考[媒体编解码格式](../harmonyos-references/capi-codecbase.md#媒体编解码格式)。

**Q：如何拿到sps信息和pps信息？**

**A**：缓冲区标记的类别flag为AVCODEC\_BUFFER\_FLAGS\_CODEC\_DATA有对应信息，可以从缓冲区buffer里面拿到。

**Q：从ArkTS层获取的裸流数据放入队列后进行解码，为何会解码一段时间后暂停解码？**

**A**：获取的H264裸流数据存入一个新队列，再让解码输入线程去该队列取数据同时属于两个线程，需要对存取队列数据的步骤进行增加互斥锁。否则会导致队列数据混乱，使得解码流程出现问题，导致暂停解码播放。
