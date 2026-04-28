---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-ohaudiosuite-oh-audiosuite-purevoicechangeoption
title: OH_AudioSuite_PureVoiceChangeOption
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioSuite_PureVoiceChangeOption
category: harmonyos-references
scraped_at: 2026-04-28T08:11:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b9d30361fddd2dcc8dc8bd25c87b7e40c0f46d73040e1aae46b663fdc91d5c5e
---

```
1. typedef struct {...} OH_AudioSuite_PureVoiceChangeOption
```

## 概述

PhonePC/2in1Tablet

定义音频编创传统变声选项。

**起始版本：** 23

**相关模块：** [OHAudioSuite](capi-ohaudiosuite.md)

**所在头文件：** [native\_audio\_suite\_base.h](capi-native-audio-suite-base-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioSuite\_PureVoiceChangeGenderOption](capi-native-audio-suite-base-h.md#oh_audiosuite_purevoicechangegenderoption) optionGender | 定义传统变声性别。 |
| [OH\_AudioSuite\_PureVoiceChangeType](capi-native-audio-suite-base-h.md#oh_audiosuite_purevoicechangetype) optionType | 定义传统变声类型。 |
| float pitch | 定义传统变声音调。如果使用系统中的默认音调以获得最佳效果, 设置为[OH\_PURE\_VOICE\_DEFAULT\_PITCH](capi-native-audio-suite-base-h.md#宏定义)。  设置自定义音调的取值范围为[0.3f, 3.0f]。 |
