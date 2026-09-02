---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-audiosuite-purevoicechangeoption
title: OH_AudioSuite_PureVoiceChangeOption
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioSuite_PureVoiceChangeOption
category: harmonyos-references
scraped_at: 2026-09-02T15:02:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4da09951d83b6db034894d88169de4c870de5acbcedc41b7daccaab521df6e27
---

```c
typedef struct {...} OH_AudioSuite_PureVoiceChangeOption
```

## 概述

定义音频编创传统变声选项。

**起始版本：** 23

**相关模块：** [OHAudioSuite](capi-ohaudiosuite.md)

**所在头文件：** [native\_audio\_suite\_base.h](capi-native-audio-suite-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioSuite\_PureVoiceChangeGenderOption](capi-native-audio-suite-base-h.md#oh_audiosuite_purevoicechangegenderoption) optionGender | 指定传统变声性别。 |
| [OH\_AudioSuite\_PureVoiceChangeType](capi-native-audio-suite-base-h.md#oh_audiosuite_purevoicechangetype) optionType | 指定传统变声类型。 |
| float pitch | 指定传统变声音调。如果使用系统中的默认音调以获得最佳效果，设置为[宏定义](capi-native-audio-suite-base-h.md#宏定义)中的OH\_PURE\_VOICE\_DEFAULT\_PITCH。  设置自定义音调的取值范围为[0.3f, 3.0f]。 |
