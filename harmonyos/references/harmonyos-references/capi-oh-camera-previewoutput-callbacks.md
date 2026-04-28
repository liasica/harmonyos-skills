---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-previewoutput-callbacks
title: PreviewOutput_Callbacks
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > PreviewOutput_Callbacks
category: harmonyos-references
scraped_at: 2026-04-28T08:12:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ca6adeef1d4a8fbd51963751af5bbbe8d1f266f2b38ff7790b3d954a9e4c0ea7
---

```
1. typedef struct PreviewOutput_Callbacks {...} PreviewOutput_Callbacks
```

## 概述

PhonePC/2in1TabletTVWearable

用于预览输出的回调。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [preview\_output.h](capi-preview-output-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_PreviewOutput\_OnFrameStart](capi-preview-output-h.md#oh_previewoutput_onframestart) onFrameStart | 预览输出帧开始事件。 |
| [OH\_PreviewOutput\_OnFrameEnd](capi-preview-output-h.md#oh_previewoutput_onframeend) onFrameEnd | 预览输出帧结束事件。 |
| [OH\_PreviewOutput\_OnError](capi-preview-output-h.md#oh_previewoutput_onerror) onError | 预览输出错误事件。 |
