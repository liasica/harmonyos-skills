---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-avscreencapturecallback
title: OH_AVScreenCaptureCallback
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AVScreenCaptureCallback
category: harmonyos-references
scraped_at: 2026-04-28T08:14:04+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:d2dafb5220fc2bc985ed861f07883b64bb5f187278eb3029658dd62109939cd1
---

```
1. typedef struct OH_AVScreenCaptureCallback {...} OH_AVScreenCaptureCallback
```

## 概述

PhonePC/2in1TabletTV

OH\_AVScreenCapture中包含所有异步回调函数指针的集合。将该结构体的实例注册到OH\_AVScreenCapture实例中，以便处理回调上报的信息，从而保证OH\_AVScreenCapture的正常运行。

从API version 12开始，推荐使用接口[OH\_AVScreenCapture\_OnError](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onerror)、[OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)替代。

**起始版本：** 10

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](capi-native-avscreen-capture-base-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [OH\_AVScreenCaptureOnError](capi-native-avscreen-capture-base-h.md#oh_avscreencaptureonerror) onError | 监控录屏调用操作错误。  从API version 12开始，推荐使用接口[OH\_AVScreenCapture\_OnError](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onerror)替代。 |
| [OH\_AVScreenCaptureOnAudioBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencaptureonaudiobufferavailable) onAudioBufferAvailable | 监控音频码流是否有数据产生。  从API version 12开始，推荐使用接口[OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)替代。 |
| [OH\_AVScreenCaptureOnVideoBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencaptureonvideobufferavailable) onVideoBufferAvailable | 监控视频码流是否有数据产生。  从API version 12开始，推荐使用接口[OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)替代。 |
