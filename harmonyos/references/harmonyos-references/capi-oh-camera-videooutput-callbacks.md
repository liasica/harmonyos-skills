---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-videooutput-callbacks
title: VideoOutput_Callbacks
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > VideoOutput_Callbacks
category: harmonyos-references
scraped_at: 2026-04-28T08:12:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0198b6634e8d5ad83bcec047987d2c60908f7eb2e2aec702bf2e6a827bc7dd15
---

```
1. typedef struct VideoOutput_Callbacks {...} VideoOutput_Callbacks
```

## 概述

PhonePC/2in1TabletTVWearable

用于录像输出的回调。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [video\_output.h](capi-video-output-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_VideoOutput\_OnFrameStart](capi-video-output-h.md#oh_videooutput_onframestart) onFrameStart | 录像输出帧启动事件。 |
| [OH\_VideoOutput\_OnFrameEnd](capi-video-output-h.md#oh_videooutput_onframeend) onFrameEnd | 录像输出帧结束事件。 |
| [OH\_VideoOutput\_OnError](capi-video-output-h.md#oh_videooutput_onerror) onError | 录像输出错误事件。 |
