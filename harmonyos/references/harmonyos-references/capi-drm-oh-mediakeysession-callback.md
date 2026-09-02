---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-oh-mediakeysession-callback
title: OH_MediaKeySession_Callback
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > OH_MediaKeySession_Callback
category: harmonyos-references
scraped_at: 2026-09-02T15:02:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:52b0e97d08f66f841f24c010c1b3c7efdf041acb92770276d75496ff2b43b039
---

```c
typedef struct OH_MediaKeySession_Callback {...} OH_MediaKeySession_Callback
```

## 概述

OH\_MediaKeySession\_Callback结构体，用于监听密钥过期、密钥更改等事件，返回媒体密钥会话实例，适用于多个媒体密钥会话的解密场景。

**起始版本：** 12

**相关模块：** [Drm](capi-drm.md)

**所在头文件：** [native\_mediakeysession.h](capi-native-mediakeysession-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_MediaKeySession\_EventCallback](capi-native-mediakeysession-h.md#oh_mediakeysession_eventcallback) eventCallback | 正常事件回调函数指针，用于处理密钥过期等常规事件。当MediaKeySession状态发生常规变化时，系统会调用此回调函数通知应用。 |
| [OH\_MediaKeySession\_KeyChangeCallback](capi-native-mediakeysession-h.md#oh_mediakeysession_keychangecallback) keyChangeCallback | 密钥更改事件回调函数指针，用于处理密钥状态变化事件。当密钥状态发生变化（如密钥可用、密钥过期等）时，系统会调用此回调函数通知应用，回调参数中包含变化的密钥信息。 |
