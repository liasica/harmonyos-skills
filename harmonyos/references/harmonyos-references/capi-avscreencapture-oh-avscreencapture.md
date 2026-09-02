---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-avscreencapture
title: OH_AVScreenCapture
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AVScreenCapture
category: harmonyos-references
scraped_at: 2026-09-02T14:53:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bd412984dca7f55bbf8ca374fcaf468fc3b8e59450f4e460b447d299f8d31619
---

```c
typedef struct OH_AVScreenCapture OH_AVScreenCapture
```

## 概述

通过OH\_AVScreenCapture可以获取视频与音频的原始码流。

开发者需通过相关接口创建实例并配置采集参数后进行屏幕录制以获取码流数据。详细的模块设计逻辑与实现机制请参见[AVScreenCapture](capi-avscreencapture.md)。适用于屏幕录制、直播推流等需要捕获屏幕内容及系统/麦克风音频的场景，可帮助应用实现高质量的屏幕采集与音视频数据获取。

**起始版本：** 10

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](capi-native-avscreen-capture-base-h.md)
