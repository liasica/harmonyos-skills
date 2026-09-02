---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-photooutput-callbacks
title: PhotoOutput_Callbacks
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > PhotoOutput_Callbacks
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:297adce8e2b7dedf623f74a076db121dadf647b3dd1d102fe1af85f37e9d29d4
---

```c
typedef struct PhotoOutput_Callbacks {...} PhotoOutput_Callbacks
```

## 概述

拍照输出的回调。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [photo\_output.h](capi-photo-output-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_PhotoOutput\_OnFrameStart](capi-photo-output-h.md#oh_photooutput_onframestart) onFrameStart | 拍照输出帧启动事件。 |
| [OH\_PhotoOutput\_OnFrameShutter](capi-photo-output-h.md#oh_photooutput_onframeshutter) onFrameShutter | 拍照输出帧快门事件。 |
| [OH\_PhotoOutput\_OnFrameEnd](capi-photo-output-h.md#oh_photooutput_onframeend) onFrameEnd | 拍照输出帧结束事件。 |
| [OH\_PhotoOutput\_OnError](capi-photo-output-h.md#oh_photooutput_onerror) onError | 拍照输出错误事件。 |
