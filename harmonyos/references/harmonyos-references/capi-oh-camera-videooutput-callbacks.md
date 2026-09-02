---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-videooutput-callbacks
title: VideoOutput_Callbacks
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > VideoOutput_Callbacks
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0ec8ddc3bf08cb1ae733d25174c4c1830f0850fd3d4b1d80d31ee36552a638f9
---

```c
typedef struct VideoOutput_Callbacks {...} VideoOutput_Callbacks
```

## 概述

用于录像输出的回调。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [video\_output.h](capi-video-output-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_VideoOutput\_OnFrameStart](capi-video-output-h.md#oh_videooutput_onframestart) onFrameStart | 录像输出帧启动事件。 |
| [OH\_VideoOutput\_OnFrameEnd](capi-video-output-h.md#oh_videooutput_onframeend) onFrameEnd | 录像输出帧结束事件。 |
| [OH\_VideoOutput\_OnError](capi-video-output-h.md#oh_videooutput_onerror) onError | 录像输出错误事件。 |
