---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysession-callback
title: MediaKeySession_Callback
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > MediaKeySession_Callback
category: harmonyos-references
scraped_at: 2026-04-28T08:13:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:79a2bed9a11ccf6340a78b315f0b8a0560981435446f45354069636f8a0f8fa5
---

```
1. typedef struct MediaKeySession_Callback {...} MediaKeySession_Callback
```

## 概述

PhonePC/2in1TabletTVWearable

MediaKeySession\_Callback结构体，用于监听密钥过期、密钥更改等事件，不返回媒体密钥会话实例，适用于单媒体密钥会话解密场景。

**起始版本：** 11

**相关模块：** [Drm](capi-drm.md)

**所在头文件：** [native\_mediakeysession.h](capi-native-mediakeysession-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [MediaKeySession\_EventCallback](capi-native-mediakeysession-h.md#mediakeysession_eventcallback) eventCallback | 正常事件回调，如密钥过期等。 |
| [MediaKeySession\_KeyChangeCallback](capi-native-mediakeysession-h.md#mediakeysession_keychangecallback) keyChangeCallback | 密钥更改事件的密钥更改回调。 |
