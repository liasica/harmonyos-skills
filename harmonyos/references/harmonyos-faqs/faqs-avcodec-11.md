---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avcodec-11
title: 如何实现对H264裸流数据实时解码渲染
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > 如何实现对H264裸流数据实时解码渲染
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fb131c9bd22404da114bdbea7e243a0921555505862fd1c1154cb1de713526ec
---

## 问题现象

投屏或者视频直播类场景下，服务端与客户端之间视频流数据的传递采用H264格式编码，客户端需要持续接收H264裸流数据并实时解码送到页面渲染，如何实现这种功能。

## 背景知识

H264主要分为两层：编码层(Video Coding Layer，VCL)和网络抽象层(NetworkAbstraction Layer (NAL))；前者定义了各种编码的算法，后者将前者编码的数据按照一定的方式进行打包存储或者传输。

NAL单元(NALU)作为单独可以解码的结构，整个H264的码流可以理解为由多个NALU组成，NALU由头部和负荷组成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/3og7xlJITWSBbuxGmRQVRA/zh-cn_image_0000002628392796.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/cfD3sAl1T2uMSL-vMYb-1A/zh-cn_image_0000002658792065.png)

H264码流主要分为avcc和Annex-B两种打包格式：

* avcc格式是在每个NALU前面添加一个标记NALU长度的字段，该字段可能的长度为1字节或者2字节或者4字节，通常为了保证该字段可以足够描述NALU的长度，会设置为4个字节，可以通过解析extradata（也称为sequence header）的头信息来获取帧长度；
* Annex-B格式没有固定长度的字段来表示NALU的长度，而是使用固定字符串来作为不同NALU的分隔符，有0x00 00 01和0x00 00 00 01，同时为了防止NALU中本身带有0x00 00 01或者0x00 00 00 01而导致的解析分隔失败，引入了0x03的防止竞争字节。

## 解决方案

基于demo：[AVCodecVideo](https://gitee.com/harmonyos_samples/AVCodecVideo)。

针对Annex-B格式的H264数据流，修改工程当中的解封装步骤，可实现逐帧解码送显，修改步骤如下：

1. 修改解封装Demuxer创建过程（**entry/src/main/cpp/capbilities/Demuxer.cpp**的**Create**函数），解码器类型选择OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC，其余视频相关参数需要业务自行定义；

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
2. **entry/src/main/cpp/sample/player/Player.cpp**定义Annex-B和avcc相关常量：

   ```
   constexpr uint8_t ANNEXB_FRAME_HEAD[] = {0, 0, 0, 1};
   constexpr uint8_t ANNEXB_FRAME_HEAD_LEN = sizeof(ANNEXB_FRAME_HEAD);
   constexpr uint8_t AVCC_FRAME_HEAD_LEN = 4;
   ```
3. 修改视频流输入（**entry/src/main/cpp/sample/player/Player.cpp**的**VideoDecInputThread**函数），Annex-B格式的H264数据流需要根据数据帧前缀逐帧读取，（一般格式为0x00 00 00 01）把数据通过内存拷贝进输入buffer当中去，重新设置buffer的attr属性：

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

## 常见FAQ

Q：往解码器中喂帧，数据如何填充至OH\_AVBuffer当中？

A：通过OH\_AVBuffer\_GetAddr获取OH\_AVBuffer内存地址，memcpy写入帧数据，通过OH\_AVBuffer\_SetBufferAttr设置输入buffer的长度等attr属性。

Q：往解码器中喂帧，无视频流输出，输出buffer为空？

A：OH\_AVBuffer\_SetBufferAttr设置attr属性时，需要先确保attr里flags、size、pts等字段的值正确，否则解码器无法正确获取输入流。

Q：avcc格式如何播放？

A：解码器只能处理Annex-B格式数据，avcc格式需要先转换为Annex-B再填充至OH\_AVBuffer当中。

Q：H265格式的码流如何播放？

A：同理，修改解码器MIME类型为OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC即可，更多格式可参考[媒体编解码格式](../harmonyos-references/capi-codecbase.md#媒体编解码格式)。

Q：如何拿到sps信息和pps信息？

A：缓冲区标记的类别flag为AVCODEC\_BUFFER\_FLAGS\_CODEC\_DATA有对应信息，可以从缓冲区buffer里面拿到。

Q：从ArkTS层获取的裸流数据放入队列后进行解码，为何会解码一段时间后暂停解码？

A：获取的H264裸流数据存入一个新队列，再让解码输入线程去该队列取数据同时属于两个线程，需要对存取队列数据的步骤进行增加互斥锁。否则会导致队列数据混乱，使得解码流程出现问题，导致暂停解码播放。
