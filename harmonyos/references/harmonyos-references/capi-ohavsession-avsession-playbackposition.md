---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-avsession-playbackposition
title: AVSession_PlaybackPosition
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > C API > 结构体 > AVSession_PlaybackPosition
category: harmonyos-references
scraped_at: 2026-09-02T15:02:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d2a781e181d39972d33e6025ce9d7231ad818204ec56227fa4a419cba4a74fd7
---

```c
typedef struct AVSession_PlaybackPosition {...} AVSession_PlaybackPosition
```

## 概述

媒体播放位置的相关属性。

**起始版本：** 13

**相关模块：** [OHAVSession](capi-ohavsession.md)

**所在头文件：** [native\_avplaybackstate.h](capi-native-avplaybackstate-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int64\_t elapsedTime | 已用时间，单位为毫秒（ms）。 |
| int64\_t updateTime | 更新时间，单位为毫秒（ms）。 |
