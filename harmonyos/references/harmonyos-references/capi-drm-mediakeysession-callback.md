---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysession-callback
title: MediaKeySession_Callback
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > MediaKeySession_Callback
category: harmonyos-references
scraped_at: 2026-09-02T15:02:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:19ce0facdc777b8bb0e25c8db628320a36bc7ab749f11b6507b97e761a9751a3
---

```c
typedef struct MediaKeySession_Callback {...} MediaKeySession_Callback
```

## 概述

MediaKeySession\_Callback结构体，用于监听密钥过期、密钥更改等事件，不返回媒体密钥会话实例，适用于单媒体密钥会话解密场景。

**起始版本：** 11

**相关模块：** [Drm](capi-drm.md)

**所在头文件：** [native\_mediakeysession.h](capi-native-mediakeysession-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [MediaKeySession\_EventCallback](capi-native-mediakeysession-h.md#mediakeysession_eventcallback) eventCallback | 正常事件回调函数指针，用于处理密钥过期等常规事件。当MediaKeySession状态发生常规变化时，系统会调用此回调函数通知应用。 |
| [MediaKeySession\_KeyChangeCallback](capi-native-mediakeysession-h.md#mediakeysession_keychangecallback) keyChangeCallback | 密钥更改事件回调函数指针，用于处理密钥状态变化事件。当密钥状态发生变化（如密钥可用、密钥过期等）时，系统会调用此回调函数通知应用，回调参数中包含变化的密钥信息。 |
