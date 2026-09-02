---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiosession-deactivatedevent
title: OH_AudioSession_DeactivatedEvent
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioSession_DeactivatedEvent
category: harmonyos-references
scraped_at: 2026-09-02T15:02:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9346575def33681dca1acde0743085d97518cac5e21f63c38b81ce90d6987722
---

```c
typedef struct OH_AudioSession_DeactivatedEvent {...} OH_AudioSession_DeactivatedEvent
```

## 概述

音频会话已停用事件。

**起始版本：** 12

**相关模块：** [OHAudio](capi-ohaudio.md)

**所在头文件：** [native\_audio\_session\_manager.h](capi-native-audio-session-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioSession\_DeactivatedReason](capi-native-audio-session-manager-h.md#oh_audiosession_deactivatedreason) reason | 音频会话停用原因。 |
