---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-capturesession-callbacks
title: CaptureSession_Callbacks
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > CaptureSession_Callbacks
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a7bf0730be90180c8d4cdeaf810ccec57b8f2cce7888dcc8429fd025785a0434
---

```c
typedef struct CaptureSession_Callbacks {...} CaptureSession_Callbacks
```

## 概述

捕获会话的回调。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [capture\_session.h](capi-capture-session-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_CaptureSession\_OnFocusStateChange](capi-capture-session-h.md#oh_capturesession_onfocusstatechange) onFocusStateChange | 捕获会话焦点状态更改事件。 |
| [OH\_CaptureSession\_OnError](capi-capture-session-h.md#oh_capturesession_onerror) onError | 捕获会话错误事件。 |
