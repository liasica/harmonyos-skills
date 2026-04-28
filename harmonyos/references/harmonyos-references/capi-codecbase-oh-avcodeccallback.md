---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase-oh-avcodeccallback
title: OH_AVCodecCallback
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 结构体 > OH_AVCodecCallback
category: harmonyos-references
scraped_at: 2026-04-28T08:12:10+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bb51f3b0f253d8c3c3ce24b9c5da34e2cf8785f8f20fdb9e2ba9e396197f718f
---

```
1. typedef struct OH_AVCodecCallback {...} OH_AVCodecCallback
```

## 概述

PhonePC/2in1TabletTVWearable

OH\_AVCodec中所有异步回调函数指针的集合。将该结构体的实例注册到OH\_AVCodec实例中，并处理回调上报的信息，以保证OH\_AVCodec的正常运行。

使用指导请参见[视频编码](../harmonyos-guides/video-encoding.md)中的“Surface模式步骤-4或Buffer模式步骤-3”。

**起始版本：** 11

**相关模块：** [CodecBase](capi-codecbase.md)

**所在头文件：** [native\_avcodec\_base.h](capi-native-avcodec-base-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_AVCodecOnError](capi-native-avcodec-base-h.md#oh_avcodeconerror) onError | 监控编解码器操作错误。 |
| [OH\_AVCodecOnStreamChanged](capi-native-avcodec-base-h.md#oh_avcodeconstreamchanged) onStreamChanged | 监控编解码器流变化。 |
| [OH\_AVCodecOnNeedInputBuffer](capi-native-avcodec-base-h.md#oh_avcodeconneedinputbuffer) onNeedInputBuffer | 监控编解码器需要输入数据。 |
| [OH\_AVCodecOnNewOutputBuffer](capi-native-avcodec-base-h.md#oh_avcodeconnewoutputbuffer) onNewOutputBuffer | 监控编解码器已生成输出数据。 |
