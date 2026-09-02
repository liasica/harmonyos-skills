---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-avscreencapture-oh-nativebuffer
title: OH_NativeBuffer
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_NativeBuffer
category: harmonyos-references
scraped_at: 2026-09-02T14:53:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d8279c1f4aa75a4df460f989687605be5c1455d4c7dc2f175dfec2bdc35bc6c8
---

```c
typedef struct OH_NativeBuffer OH_NativeBuffer
```

## 概述

提供录屏的视频原始数据缓冲区结构体。OH\_NativeBuffer提供录屏的视频原始数据处理能力，支持对录屏过程中产生的视频原始数据进行封装、传输和管理。

用于在AVScreenCapture录屏场景中承载获取的视频帧原始数据。可用于录屏数据的二次处理场景，如视频编辑应用中对录屏帧数据进行像素级操作、直播推流场景中对原始码流进行编码推送等。

**起始版本：** 10

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](capi-native-avscreen-capture-base-h.md)
