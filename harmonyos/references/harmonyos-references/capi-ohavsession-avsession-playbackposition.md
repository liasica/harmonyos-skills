---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-avsession-playbackposition
title: AVSession_PlaybackPosition
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > C API > 结构体 > AVSession_PlaybackPosition
category: harmonyos-references
scraped_at: 2026-04-28T08:12:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:abc51eb170eefeb8918744654612460f33f7202b12c01e3545ab45045b11bb92
---

```
1. typedef struct AVSession_PlaybackPosition {...} AVSession_PlaybackPosition
```

## 概述

PhonePC/2in1TabletTVWearable

媒体播放位置的相关属性。

**起始版本：** 13

**相关模块：** [OHAVSession](capi-ohavsession.md)

**所在头文件：** [native\_avplaybackstate.h](capi-native-avplaybackstate-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int64\_t elapsedTime | 已用时间，单位毫秒（ms）。 |
| int64\_t updateTime | 更新时间，单位毫秒（ms）。 |
