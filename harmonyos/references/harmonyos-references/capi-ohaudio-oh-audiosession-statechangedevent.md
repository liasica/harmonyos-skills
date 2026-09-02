---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiosession-statechangedevent
title: OH_AudioSession_StateChangedEvent
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioSession_StateChangedEvent
category: harmonyos-references
scraped_at: 2026-09-02T15:02:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cabdbcc93125debcc8a979edda23f96f27c2838ab66bdea8aec7190b67f32c96
---

```c
typedef struct OH_AudioSession_StateChangedEvent {...} OH_AudioSession_StateChangedEvent
```

## 概述

音频会话状态变更事件。

**起始版本：** 20

**相关模块：** [OHAudio](capi-ohaudio.md)

**所在头文件：** [native\_audio\_session\_manager.h](capi-native-audio-session-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioSession\_StateChangeHint](capi-native-audio-session-manager-h.md#oh_audiosession_statechangehint) stateChangeHint | 音频会话停用的具体原因。 |
