---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avcodec-23
title: 配置视频文件的旋转角度失败
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > 配置视频文件的旋转角度失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:40aad6254a44568a29cdf849231023fddbdd9a4e270b613fefc43a6f2f20c0ac
---

## 问题现象

推流端过来的流不是正向的，流的封装格式是mp4，使用OH\_AVMuxer\_SetRotation函数配置旋转90度没有生效。

## 背景知识

需要生成旋转后的视频文件，可以对原mp4文件进行解封装和重新封装步骤，并使用[OH\_AVMuxer\_SetRotation](../harmonyos-references/capi-native-avmuxer-h.md#oh_avmuxer_setrotation)接口在[媒体数据封装](../harmonyos-guides/audio-video-muxer.md)过程中对视频进行配置，使得最后新封装出来的视频按照配置的角度旋转。

## 问题定位

在OH\_AVMuxer\_SetRotation函数调用前，添加日志打印查看配置的旋转角度，发现虽然在全局变量配置了90度旋转，但是在最后给OH\_AVMuxer\_SetRotation的参数为0，从而导致没有旋转。

```txt
03-12 11:49:19.095   8687-8687     A02B66/com.sam...ferMode/Muxer  com.sampl...fferMode  I     {Config():58} test Muxer rotation 0
```

## 分析结论

进一步定位发现是该全局变量也会用来存储解封装步骤中解析出来的旋转角度。在解析原本的mp4文件时，由于原本mp4本身没有配置旋转角度，所以通过OH\_AVFormat\_GetIntValue获取的OH\_MD\_KEY\_ROTATION为0，该值将该全局变量覆盖为0，导致配置的旋转角度为0。

```cpp
auto trackFormat =
    std::shared_ptr<OH_AVFormat>(OH_AVSource_GetTrackFormat(source_, index), OH_AVFormat_Destroy);
OH_AVFormat_GetIntValue(trackFormat.get(), OH_MD_KEY_TRACK_TYPE, &trackType);
if (trackType == MEDIA_TYPE_VID) {
    OH_AVDemuxer_SelectTrackByID(demuxer_, index);
    // 获取其他配置参数步骤，如分辨率、轨道ID等
    char *videoCodecMime;
    OH_AVFormat_GetStringValue(trackFormat.get(), OH_MD_KEY_CODEC_MIME,
                               const_cast<char const **>(&videoCodecMime));
    info.videoCodecMime = videoCodecMime;
    OH_AVFormat_GetIntValue(trackFormat.get(), OH_MD_KEY_PROFILE, &info.hevcProfile);
    videoTrackId_ = index;
    OH_AVFormat_GetIntValue(trackFormat.get(), OH_MD_KEY_WIDTH, &info.videoWidth);
    OH_AVFormat_GetIntValue(trackFormat.get(), OH_MD_KEY_HEIGHT, &info.videoHeight);
    OH_AVFormat_GetDoubleValue(trackFormat.get(), OH_MD_KEY_FRAME_RATE, &info.frameRate);
    OH_AVFormat_GetLongValue(trackFormat.get(), OH_MD_KEY_BITRATE, &info.bitrate);

    // 问题代码，此处获取的OH_MD_KEY_ROTATION为0
    OH_AVFormat_GetIntValue(trackFormat.get(), OH_MD_KEY_ROTATION, &info.rotation);
}
```

## 修改建议

增加新全局变量存储需要旋转的角度，给OH\_AVMuxer\_SetRotation函数配置的参数使用解析出来的旋转角度加上实际需要旋转的角度即可。

## 常见FAQ

Q：如果仅需要视频在渲染播放时旋转，应该如何配置操作？

A：仅需要在播放时使得播放结果旋转，可以使用[Surface模式视频解码](../harmonyos-guides/video-decoding.md#surface模式)，并在解码过程的配置步骤中使用[OH\_AVFormat\_SetIntValue](../harmonyos-references/capi-native-avformat-h.md#oh_avformat_setintvalue)接口给OH\_MD\_KEY\_ROTATION键值对配置指定的旋转角度。
