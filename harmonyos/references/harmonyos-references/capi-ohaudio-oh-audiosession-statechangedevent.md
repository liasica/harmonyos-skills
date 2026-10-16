---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiosession-statechangedevent
title: OH_AudioSession_StateChangedEvent
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioSession_StateChangedEvent
category: harmonyos-references
scraped_at: 2026-10-17T06:47:41+08:00
doc_updated_at: 2026-10-16
content_hash: sha256:fe12ebcb7721aa293d222ede70818c4b2e16295f8e3d1fc78cf3ca7eb99d4065
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
| [OH\_AudioSession\_StateChangeHint](capi-native-audio-session-manager-h.md#oh_audiosession_statechangehint) stateChangeHint | 音频会话状态变更提示，用于表示状态变化的类型，如静音、取消静音、暂停、恢复等。 |
