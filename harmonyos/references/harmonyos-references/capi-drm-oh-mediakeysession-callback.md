---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-oh-mediakeysession-callback
title: OH_MediaKeySession_Callback
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > OH_MediaKeySession_Callback
category: harmonyos-references
scraped_at: 2026-04-28T08:13:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:70a73e2a0fad0c49f86e5d06f9ef895163162c582197a5fb932cc7558fa1da10
---

```
1. typedef struct OH_MediaKeySession_Callback {...} OH_MediaKeySession_Callback
```

## 概述

PhonePC/2in1TabletTVWearable

OH\_MediaKeySession\_Callback结构体，用于监听密钥过期、密钥更改等事件，返回媒体密钥会话实例，适用于多个媒体密钥会话的解密场景。

**起始版本：** 12

**相关模块：** [Drm](capi-drm.md)

**所在头文件：** [native\_mediakeysession.h](capi-native-mediakeysession-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_MediaKeySession\_EventCallback](capi-native-mediakeysession-h.md#oh_mediakeysession_eventcallback) eventCallback | 正常事件回调，如密钥过期等。 |
| [OH\_MediaKeySession\_KeyChangeCallback](capi-native-mediakeysession-h.md#oh_mediakeysession_keychangecallback) keyChangeCallback | 密钥更改事件的密钥更改回调。 |
