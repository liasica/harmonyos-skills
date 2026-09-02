---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avcodec-17
title: 解码器解码过程中卡住无输出
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > 解码器解码过程中卡住无输出
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a15284a04a6b407e7659bf3a0183caa0e9eb7f30968ff0fa6bf605200fc3c9e7
---

## 问题现象

在调试解码器硬解功能时发现反复拉流的时候解码器有段时间只能输入数据，但是没有数据输出。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/fFcAkcPKTsmsn9W_JunH4A/zh-cn_image_0000002628552732.png "点击放大")

## 背景知识

* 解码过程中需要注册回调函数[OH\_AVCodecOnNeedInputBuffer](../harmonyos-references/capi-native-avcodec-base-h.md#oh_avcodeconneedinputbuffer)，表示运行过程中需要新的输入数据，即解码器已准备好，可以输入数据。在运行过程中需要新的输入数据时，将调用此函数指针，并携带可用的缓冲区来填充新的输入数据。
* 解码过程中使用[VideoDecoder\_PushInputBuffer](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_pushinputbuffer)通知视频解码器已对index对应的缓冲区完成输入数据的填充。输入回调将报告可用的输入缓冲区和相应的index值，请参阅OH\_AVCodecOnNeedInputBuffer。一旦具有指定index的缓冲区提交到视频解码器，则无法再次访问缓冲区，直到再次收到输入回调，报告具有相同index的缓冲区可用。
* 解码的数据队列参考[视频解码](../harmonyos-guides/video-decoding.md)中的解码输入输出队列。
* 帧的相关配置类型：
  + 仅关键帧(I帧)：AVCODEC\_BUFFER\_FLAGS\_SYNC\_FRAME。
  + 仅配置帧(pps、sps)：AVCODEC\_BUFFER\_FLAGS\_CODEC\_DATA。
  + 是配置帧又是关键帧(pps、sps + I帧)：AVCODEC\_BUFFER\_FLAGS\_CODEC\_DATA|AVCODEC\_BUFFER\_FLAGS\_SYNC\_FRAME。
  + 普通帧(P帧/B帧)：AVCODEC\_BUFFER\_FLAGS\_NONE。

视频解码中的调用关系图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/mJEZiwmSTe6EPrvA2DGaBw/zh-cn_image_0000002658912053.png "点击放大")

## 问题定位

1. 当前仅支持传入AnnexB视频码流，不支持AVCC格式码流，检查传入的码流格式是否符合。
2. 确保buffersize大小正确传入。
3. 解码器Flush后，再次启动解码器，需要传入XPS和关键帧，否则直到传入XPS和关键帧为止，相关帧将会被丢弃。排查首帧是否未传XPS信息。
4. 发现AVCODEC\_BUFFER\_FLAGS\_CODEC\_DATA未传准确，但是修改后问题还是存在。
5. 再次测试，错误日志如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/D9ghXy32R8-khenTRu5kgg/zh-cn_image_0000002628392848.png "点击放大")
6. 根据解码输出出现问题的时间段定位到11:37的时间点。查看日志输出相关时间点发现报错如下：

   ```txt
   10-14 11:37:43.461 1561 27622 E C02B32/av_codec_service/HCODEC: [264][dec.avc][Running][OnQueueInputBuffer 865] wrong ownership: buffer id=3, owner=omx
   10-14 11:37:43.461 1561 27622 E C02B32/av_codec_service/HCODEC: [264][dec.avc][Running][OnQueueInputBuffer 865] wrong ownership: buffer id=3, owner=omx
   10-14 11:37:43.462 1561 27622 E C02B32/av_codec_service/HCODEC: [264][dec.avc][Running][OnQueueInputBuffer 865] wrong ownership: buffer id=3, owner=omx
   ```

## 分析结论

根据日志结果在此时间段有多次传入索引为3的buffer数据。分析发现此时间段内并没有接收到系统的回调，就将这几帧buffer给push传入，导致前面几帧push失败。

不可同时向解码器push多次同一index和buffer，正常情况下再次向同一个缓冲区填充数据传入队列需要等待解码器消费完数据并被释放后发起[OH\_AVCodecOnNeedInputBuffer](../harmonyos-references/capi-native-avcodec-base-h.md#oh_avcodeconneedinputbuffer)回调，用该回调的index和buffer指针成为参数来填充数据以此实现轮转。

## 修改建议

对解码器的输入队列进行上锁操作，在输入队列中有数据并要将其传入解码器时确保锁保护共享资源访问，获得锁后从解码输入队列中获取回调得到的index和buffer缓冲区出队列，后释放锁，填充帧数据到buffer后使用[PushInputBuffer](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_pushinputbuffer)送入解码器解码。

```
void Player::VideoDecInputThread()
{
    while (true) {
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

        demuxer_->ReadSample(demuxer_->GetVideoTrackId(), reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer),
                             bufferInfo.attr);

        int32_t ret = videoDecoder_->PushInputBuffer(bufferInfo);
        AVCODEC_SAMPLE_LOGW("PushInputBuffer info index:"
                            "%{public}u  framecount: %{public}u, pts: %{public}" PRId64,
                            bufferInfo.bufferIndex, videoDecContext_->inputFrameCount, bufferInfo.attr.pts);
        CHECK_AND_BREAK_LOG(ret == AVCODEC_SAMPLE_ERR_OK, "Push data failed, thread out");

        CHECK_AND_BREAK_LOG(!(bufferInfo.attr.flags & AVCODEC_BUFFER_FLAGS_EOS), "Catch EOS, thread out");
    }
}
```

index输出如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/Hp_AHMrMQP6dcRJgkAgTOw/zh-cn_image_0000002658792119.png "点击放大")

完整demo可参考[AVCodecVideo](https://gitee.com/harmonyos_samples/AVCodecVideo)。

## 总结

使用VideoDecoder\_PushInputBuffer通知视频解码器已对index对应的缓冲区完成输入数据的填充时，输入回调AVCodecOnNeedInputBuffer将报告可用的输入缓冲区和相应的index值。一旦具有指定index的缓冲区提交到视频解码器，则无法再次访问缓冲区，直到再次收到输入回调，报告具有相同index的缓冲区可用。
