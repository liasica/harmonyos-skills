---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avcodec-15
title: 视频硬解码CPU使用率高
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > 视频硬解码CPU使用率高
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cd1a71b58b4728c604bbc57023e65d302fed757f392070a47b59d3fb7b7158c6
---

## 问题现象

在播放同一个m3u8视频时，分别使用AVCodec硬件视频解码器和ffmpeg软件解码器播放，发现使用硬件解码器时的CPU使用率要比软件的高很多。在进行视频解码的过程中，硬解码过程的CPU使用率预期比软解码过程要低。在使用ijkplayer进行测试时，CPU的使用率出现相反的情况。

CPU测试结果如下图：

硬解码：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/HHLFyAXxRXa9ka-ZgHZz-w/zh-cn_image_0000002658792067.png "点击放大")

ffmpeg软解码：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/E-YFRstNReGLN2lgW0DjqQ/zh-cn_image_0000002628552690.png "点击放大")

从CPU测试结果图来看硬件视频解码CPU使用率维持在7%到8%左右，使用ffmpeg软件解码播放时平均维持在3%左右。这与硬解码和软解码的CPU占用不符合。硬解码调用设备相关硬件进行解码，软解码调用软件（调用CPU）进行解码，预期结果应当为硬解码占用更少的CPU。

## 背景知识

* 视频硬解码：通过硬件来进行解码，特定解码硬件或者显卡核心GPU拥有独特的计算方法，解码效率高，充当解码核心的模块成本并不高。这样能够减轻CPU的负担，还能降低功耗、减少发热。但是由于硬解码起步比较晚，软件和驱动对其的支持度低，硬解码只能兼容其指定的编码格式。
* 视频软解码：通过软件来进行解码，软解码技术的解码过程中，需要对大量的视频信息进行运算，对CPU要求很高，通常会占用比较多的CPU资源，尤其是对高清晰度大码率的视频来说，巨大的运算量就会造成转换效率低、发热量大等问题。软解码由于是使用软件进行解码，兼容性非常高，通常能适配大部分的编码格式。

## 问题定位

解码代码中[AVCodecOnNeedInputBuffer](../harmonyos-references/capi-native-avcodec-base-h.md#oh_avcodeconneedinputbuffer)的代码段：

```cpp
void AVCodecOnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
{
    OHOSVDecoder *decoder = static_cast<OHOSVDecoder *>(userData);
    if (decoder == nullptr) {
        return;
    }
    decoder->OnNeedInputBuffer(codec, index, buffer);
}
```

```cpp
void OHOSVDecoder::OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer)
{
    if (codec == nullptr) {
        return;
    }
    std::shared_ptr<Frame> frame;
    {
        std::unique_lock<std::mutex> auto_lock(_frame_mutex);
        if (_input_frames.size() > 0) {
            frame = _input_frames.front();
            _input_frames.pop_front();
        }
    }
    if (frame == nullptr) {
        OH_AVCodecBufferAttr info;
        info.pts = 0;
        info.size = 0;
        info.offset = 0;
        info.flags = AVCODEC_BUFFER_FLAGS_DISCARD;
        OH_AVBuffer_SetBufferAttr(buffer, &info);
        OH_VideoDecoder_PushInputBuffer(codec, index);
        return;
    }
    std::shared_ptr<VideoFrame> video_frame = std::dynamic_pointer_cast<VideoFrame>(frame);
    OH_AVCodecBufferAttr info;
    info.pts = video_frame->pts();
    info.size = frame->Size();
    info.offset = 0;
    info.flags = AVCODEC_BUFFER_FLAGS_NONE;
    int32_t ret = OH_AVBuffer_SetBufferAttr(buffer, &info);
    if (ret != AV_ERR_OK) {
        return;
    }
    uint8_t *data = OH_AVBuffer_GetAddr(buffer);
    if (data == nullptr) {
        return;
    }
    memcpy(data, frame->Data(), frame->Size());
    ret = OH_VideoDecoder_PushInputBuffer(codec, index);
    if (ret != AV_ERR_OK) {
        return;
    }
}
```

## 分析结论

可以看见OnNeedInputBuffer函数实现中由自定义类型Frame去存储相关数据，在后续读取其中的信息到结构体[OH\_AVBuffer](../harmonyos-references/capi-core-oh-avbuffer.md)和[OH\_AVCodecBufferAttr](../harmonyos-references/capi-core-oh-avcodecbufferattr.md)中以调用函数[PushInputBuffer](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_pushinputbuffer)往视频解码队列输入数据，等待解码器解码，但在最后使用[OH\_AVBuffer\_GetAddr](../harmonyos-references/capi-native-avbuffer-h.md#oh_avbuffer_getaddr)获取的是AVBuffer的地址，使用memcpy拷贝的是地址而非实际数据，且在使用PushInputBuffer填充数据时只传入了解码器和索引，Buffer的数据没有被传递。

在视频Buffer和音频Buffer都为nullptr时，在视频源有数据不断传入时，解码器会保持空载。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/oxv4HseRSgCrWkkKG8_33Q/zh-cn_image_0000002658912009.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/1tY0CvjGQDKmqYhnmj5aBQ/zh-cn_image_0000002628392810.png "点击放大")

当传入解码队列的音频Buffer不为空，视频Buffer为nullptr时，解码器运行，只有音频输出。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/ezLA6YAXS_yuXbFJIKIPng/zh-cn_image_0000002658792093.png "点击放大")

## 修改建议

确保使用[PushInputBuffer](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_pushinputbuffer)传入给解码队列的Buffer不为空，详细过程参考视频解码[开发指导](../harmonyos-guides/video-decoding.md#开发指导)。
