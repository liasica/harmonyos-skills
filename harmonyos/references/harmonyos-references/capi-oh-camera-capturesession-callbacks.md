---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-capturesession-callbacks
title: CaptureSession_Callbacks
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > CaptureSession_Callbacks
category: harmonyos-references
scraped_at: 2026-04-28T08:12:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e951e906b60ca169781f2dee46ddb062074ec82f4e1963b422bef039b8d9eb04
---

```
1. typedef struct CaptureSession_Callbacks {...} CaptureSession_Callbacks
```

## 概述

PhonePC/2in1TabletTVWearable

捕获会话的回调。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [capture\_session.h](capi-capture-session-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_CaptureSession\_OnFocusStateChange](capi-capture-session-h.md#oh_capturesession_onfocusstatechange) onFocusStateChange | 捕获会话焦点状态更改事件。 |
| [OH\_CaptureSession\_OnError](capi-capture-session-h.md#oh_capturesession_onerror) onError | 捕获会话错误事件。 |
