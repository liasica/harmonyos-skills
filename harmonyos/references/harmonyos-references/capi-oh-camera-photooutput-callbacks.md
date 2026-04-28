---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-photooutput-callbacks
title: PhotoOutput_Callbacks
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > PhotoOutput_Callbacks
category: harmonyos-references
scraped_at: 2026-04-28T08:12:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:da402433d683f9979c8ea9f4b26d2b647dc7636f5a3fcff413e2f1eb51f6c109
---

```
1. typedef struct PhotoOutput_Callbacks {...} PhotoOutput_Callbacks
```

## 概述

PhonePC/2in1TabletTVWearable

拍照输出的回调。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [photo\_output.h](capi-photo-output-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_PhotoOutput\_OnFrameStart](capi-photo-output-h.md#oh_photooutput_onframestart) onFrameStart | 拍照输出帧启动事件。 |
| [OH\_PhotoOutput\_OnFrameShutter](capi-photo-output-h.md#oh_photooutput_onframeshutter) onFrameShutter | 拍照输出帧快门事件。 |
| [OH\_PhotoOutput\_OnFrameEnd](capi-photo-output-h.md#oh_photooutput_onframeend) onFrameEnd | 拍照输出帧结束事件。 |
| [OH\_PhotoOutput\_OnError](capi-photo-output-h.md#oh_photooutput_onerror) onError | 拍照输出错误事件。 |
