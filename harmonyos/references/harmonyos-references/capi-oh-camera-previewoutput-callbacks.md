---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-previewoutput-callbacks
title: PreviewOutput_Callbacks
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > PreviewOutput_Callbacks
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:416eaf17d25cdca2d9b41c24ad7699cb7ea98380689dbcee06e6981df4ef296f
---

```c
typedef struct PreviewOutput_Callbacks {...} PreviewOutput_Callbacks
```

## 概述

用于预览输出的回调。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [preview\_output.h](capi-preview-output-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_PreviewOutput\_OnFrameStart](capi-preview-output-h.md#oh_previewoutput_onframestart) onFrameStart | 预览输出帧开始事件。 |
| [OH\_PreviewOutput\_OnFrameEnd](capi-preview-output-h.md#oh_previewoutput_onframeend) onFrameEnd | 预览输出帧结束事件。 |
| [OH\_PreviewOutput\_OnError](capi-preview-output-h.md#oh_previewoutput_onerror) onError | 预览输出错误事件。 |
