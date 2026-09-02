---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase-oh-avcodecasynccallback
title: OH_AVCodecAsyncCallback
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 结构体 > OH_AVCodecAsyncCallback
category: harmonyos-references
scraped_at: 2026-09-02T15:02:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:48b84eefb73a9a4f7c7194138802b6679cf0326a4b66c678ac172384475f231d
---

```c
typedef struct OH_AVCodecAsyncCallback {...} OH_AVCodecAsyncCallback
```

## 概述

OH\_AVCodec中所有异步回调函数指针的集合。将该结构体的实例注册到OH\_AVCodec实例中，并处理回调上报的信息，以保证OH\_AVCodec的正常运行。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [OH\_AVCodecCallback](capi-codecbase-oh-avcodeccallback.md)

**相关模块：** [CodecBase](capi-codecbase.md)

**所在头文件：** [native\_avcodec\_base.h](capi-native-avcodec-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_AVCodecOnError](capi-native-avcodec-base-h.md#oh_avcodeconerror) onError | 监控编解码器操作错误。 |
| [OH\_AVCodecOnStreamChanged](capi-native-avcodec-base-h.md#oh_avcodeconstreamchanged) onStreamChanged | 监控编解码器流变化。 |
| [OH\_AVCodecOnNeedInputData](capi-native-avcodec-base-h.md#oh_avcodeconneedinputdata) onNeedInputData | 监控编解码器需要输入数据。 |
| [OH\_AVCodecOnNewOutputData](capi-native-avcodec-base-h.md#oh_avcodeconnewoutputdata) onNeedOutputData | 监控编解码器已生成输出数据。 |
