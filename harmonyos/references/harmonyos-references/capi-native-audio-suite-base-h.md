---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h
title: native_audio_suite_base.h
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 头文件 > native_audio_suite_base.h
category: harmonyos-references
scraped_at: 2026-04-28T08:11:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c5402e7a80ced63f5713c9fde3a12c554574d18b0b8a4191e6947a6905dc45fb
---

## 概述

PhonePC/2in1Tablet

声明音频编创相关底层数据结构。

**引用文件：** <ohaudiosuite/native\_audio\_suite\_base.h>

**库：** libohaudiosuite.so

**系统能力：** SystemCapability.Multimedia.Audio.SuiteEngine

**起始版本：** 22

**相关模块：** [OHAudioSuite](capi-ohaudiosuite.md)

## 汇总

PhonePC/2in1Tablet

### 结构体

PhonePC/2in1Tablet

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioFormat](capi-ohaudiosuite-oh-audioformat.md) | OH\_AudioFormat | 定义音频编创的音频流信息，用于描述基本音频格式。 |
| [OH\_AudioDataArray](capi-ohaudiosuite-oh-audiodataarray.md) | OH\_AudioDataArray | 定义多路输出渲染接口的输入数据描述。当管线中存在多输出效果节点时，通过多输出渲染接口获取处理过后的音频数据。 |
| [OH\_EqualizerFrequencyBandGains](capi-ohaudiosuite-oh-equalizerfrequencybandgains.md) | OH\_EqualizerFrequencyBandGains | 定义音频编创均衡器效果节点配置参数。 |
| [OH\_AudioSuite\_SpaceRenderPositionParams](audiosuite-oh-audiosuite-spacerenderpositionparams.md) | OH\_AudioSuite\_SpaceRenderPositionParams | 定义3D空间渲染效果节点固定摆位模式的配置参数。左手坐标系：伸出左手，用拇指和食指形成一个“L”形。  拇指指向右侧，食指向上，其余手指指向前。  此时形成了一个3D的左手坐标系。在这个坐标系中，拇指、食指  和其他手指分别代表x轴、y轴和z轴的正方向。 |
| [OH\_AudioSuite\_SpaceRenderRotationParams](audiosuite-oh-audiosuite-spacerenderrotationparams.md) | OH\_AudioSuite\_SpaceRenderRotationParams | 定义空间渲染效果节点旋转模式配置参数。 |
| [OH\_AudioSuite\_SpaceRenderExtensionParams](udiosuite-oh-audiosuite-spacerenderextensionparams.md) | OH\_AudioSuite\_SpaceRenderExtensionParams | 定义空间渲染效果节点扩展模式配置参数。 |
| [OH\_AudioSuite\_PureVoiceChangeOption](i-ohaudiosuite-oh-audiosuite-purevoicechangeoption.md) | OH\_AudioSuite\_PureVoiceChangeOption | 定义音频编创传统变声选项。 |
| [OH\_AudioSuiteEngineStruct](capi-ohaudiosuite-oh-audiosuiteenginestruct.md) | OH\_AudioSuiteEngine | 声明音频编创引擎，用来管理音频编创管线。 |
| [OH\_AudioSuitePipelineStruct](capi-ohaudiosuite-oh-audiosuitepipelinestruct.md) | OH\_AudioSuitePipeline | 声明音频编创管线，用来管理音频编创节点。 |
| [OH\_AudioNodeStruct](capi-ohaudiosuite-oh-audionodestruct.md) | OH\_AudioNode | 声明音频编创节点，用于描述音频编创节点实例。 |
| [OH\_AudioNodeBuilderStruct](capi-ohaudiosuite-oh-audionodebuilderstruct.md) | OH\_AudioNodeBuilder | 声明音频编创节点的构造器。用于构建[OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)，配置输入输出节点数据格式，配置输入节点回调接口。 |

### 枚举

PhonePC/2in1Tablet

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioNode\_Type](capi-native-audio-suite-base-h.md#oh_audionode_type) | OH\_AudioNode\_Type | 定义音频编创节点类型。 |
| [OH\_AudioSuite\_PipelineWorkMode](capi-native-audio-suite-base-h.md#oh_audiosuite_pipelineworkmode) | OH\_AudioSuite\_PipelineWorkMode | 定义音频编创管线工作模式。 |
| [OH\_AudioSuite\_PipelineState](capi-native-audio-suite-base-h.md#oh_audiosuite_pipelinestate) | OH\_AudioSuite\_PipelineState | 定义音频编创管线运行状态。 |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | OH\_AudioSuite\_Result | 音频编创错误码。 |
| [OH\_Audio\_SampleFormat](capi-native-audio-suite-base-h.md#oh_audio_sampleformat) | OH\_Audio\_SampleFormat | 定义音频编创节点音频流的位深度。 |
| [OH\_Audio\_EncodingType](capi-native-audio-suite-base-h.md#oh_audio_encodingtype) | OH\_Audio\_EncodingType | 定义音频流编码类型。 |
| [OH\_Audio\_SampleRate](capi-native-audio-suite-base-h.md#oh_audio_samplerate) | OH\_Audio\_SampleRate | 定义音频采样率。 |
| [OH\_SoundFieldType](capi-native-audio-suite-base-h.md#oh_soundfieldtype) | OH\_SoundFieldType | 定义音频编创声场效果节点的效果模式。 |
| [OH\_EnvironmentType](capi-native-audio-suite-base-h.md#oh_environmenttype) | OH\_EnvironmentType | 定义音频编创环境效果节点的模式。 |
| [OH\_VoiceBeautifierType](capi-native-audio-suite-base-h.md#oh_voicebeautifiertype) | OH\_VoiceBeautifierType | 定义音频编创美化效果节点模式。 |
| [OH\_AudioSuite\_SurroundDirection](capi-native-audio-suite-base-h.md#oh_audiosuite_surrounddirection) | OH\_AudioSuite\_SurroundDirection | 定义空间渲染效果节点旋转模式环绕方向。 |
| [OH\_AudioSuite\_PureVoiceChangeGenderOption](capi-native-audio-suite-base-h.md#oh_audiosuite_purevoicechangegenderoption) | OH\_AudioSuite\_PureVoiceChangeGenderOption | 定义音频编创传统变声效果节点的性别。 |
| [OH\_AudioSuite\_PureVoiceChangeType](capi-native-audio-suite-base-h.md#oh_audiosuite_purevoicechangetype) | OH\_AudioSuite\_PureVoiceChangeType | 定义音频编创传统变声效果节点的变声类型。 |
| [OH\_AudioSuite\_GeneralVoiceChangeType](capi-native-audio-suite-base-h.md#oh_audiosuite_generalvoicechangetype) | OH\_AudioSuite\_GeneralVoiceChangeType | 定义音频编创通用变声的节点类型。 |

### 宏定义

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| EQUALIZER\_BAND\_NUM (10) | 定义均衡器频带数量为10个。  **起始版本：** 22 |
| OH\_PURE\_VOICE\_DEFAULT\_PITCH (0.0f) | 使用系统推荐的音调。用于[OH\_AudioSuite\_PureVoiceChangeOption](i-ohaudiosuite-oh-audiosuite-purevoicechangeoption.md)。  **起始版本：** 23 |

### 变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| const [OH\_EqualizerFrequencyBandGains](capi-ohaudiosuite-oh-equalizerfrequencybandgains.md) OH\_EQUALIZER\_PARAM\_DEFAULT | 默认均衡器频带增益效果。  各频带增益：{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}。  **起始版本：** 22 |
| const [OH\_EqualizerFrequencyBandGains](capi-ohaudiosuite-oh-equalizerfrequencybandgains.md) OH\_EQUALIZER\_PARAM\_BALLADS | 均衡器节点内置民谣效果。  各频带增益：{3, 5, 2, -4, 1, 2, -3, 1, 4, 5}。  **起始版本：** 22 |
| const [OH\_EqualizerFrequencyBandGains](capi-ohaudiosuite-oh-equalizerfrequencybandgains.md) OH\_EQUALIZER\_PARAM\_CHINESE\_STYLE | 均衡器节点内置中国风效果。  各频带增益：{0, 0, 2, 0, 0, 4, 4, 2, 2, 5}。  **起始版本：** 22 |
| const [OH\_EqualizerFrequencyBandGains](capi-ohaudiosuite-oh-equalizerfrequencybandgains.md) OH\_EQUALIZER\_PARAM\_CLASSICAL | 均衡器节点内置古典效果。  各频带增益：{2, 3, 2, 1, 0, 0, -5, -5, -5, -6}。  **起始版本：** 22 |
| const [OH\_EqualizerFrequencyBandGains](capi-ohaudiosuite-oh-equalizerfrequencybandgains.md) OH\_EQUALIZER\_PARAM\_DANCE\_MUSIC | 均衡器节点内置舞曲效果。  各频带增益：{4, 3, 2, -3, 0, 0, 5, 4, 2, 0}。  **起始版本：** 22 |
| const [OH\_EqualizerFrequencyBandGains](capi-ohaudiosuite-oh-equalizerfrequencybandgains.md) OH\_EQUALIZER\_PARAM\_JAZZ | 均衡器节点内置爵士效果。  各频带增益：{2, 0, 2, 3, 6, 5, -1, 3, 4, 4}。  **起始版本：** 22 |
| const [OH\_EqualizerFrequencyBandGains](capi-ohaudiosuite-oh-equalizerfrequencybandgains.md) OH\_EQUALIZER\_PARAM\_POP | 均衡器节点内置流行效果。  各频带增益：{5, 2, 1, -1, -5, -5, -2, 1, 2, 4}。  **起始版本：** 22 |
| const [OH\_EqualizerFrequencyBandGains](capi-ohaudiosuite-oh-equalizerfrequencybandgains.md) OH\_EQUALIZER\_PARAM\_RB | 均衡器节点内置R&B效果。  各频带增益：{1, 4, 5, 3, -2, -2, 2, 3, 5, 5}。  **起始版本：** 22 |
| const [OH\_EqualizerFrequencyBandGains](capi-ohaudiosuite-oh-equalizerfrequencybandgains.md) OH\_EQUALIZER\_PARAM\_ROCK | 均衡器节点内置摇滚效果。  各频带增益：{6, 4, 4, 2, 0, 1, 3, 3, 5, 4}。  **起始版本：** 22 |

## 枚举类型说明

PhonePC/2in1Tablet

### OH\_AudioNode\_Type

PhonePC/2in1Tablet

```
1. enum OH_AudioNode_Type
```

**描述**

定义音频编创节点类型。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| INPUT\_NODE\_TYPE\_DEFAULT = 1 | 输入节点，支持从应用程序获取音频数据。 |
| OUTPUT\_NODE\_TYPE\_DEFAULT = 101 | 输出节点，支持向应用程序提供音频数据。 |
| EFFECT\_NODE\_TYPE\_EQUALIZER = 201 | 均衡器效果节点。均衡器效果节点输出的音频格式如下：  采样率：48000Hz。  采样格式：[OH\_Audio\_SampleFormat](capi-native-audio-suite-base-h.md#oh_audio_sampleformat).AUDIO\_SAMPLE\_S16LE。  声道数：2。 |
| EFFECT\_NODE\_TYPE\_NOISE\_REDUCTION = 202 | 降噪效果节点。降噪效果节点输出的音频格式如下：  采样率：16000Hz。  采样格式：[OH\_Audio\_SampleFormat](capi-native-audio-suite-base-h.md#oh_audio_sampleformat).AUDIO\_SAMPLE\_S16LE。  声道数：1。 |
| EFFECT\_NODE\_TYPE\_SOUND\_FIELD = 203 | 声场效果节点。声场效果节点支持的声场类型：[OH\_SoundFieldType](capi-native-audio-suite-base-h.md#oh_soundfieldtype)。  声场效果节点输出的音频格式如下：  采样率：48000Hz。  采样格式：[OH\_Audio\_SampleFormat](capi-native-audio-suite-base-h.md#oh_audio_sampleformat).AUDIO\_SAMPLE\_S16LE。  声道数：2。 |
| EFFECT\_MULTII\_OUTPUT\_NODE\_TYPE\_AUDIO\_SEPARATION = 204 | 音源分离效果节点。音源分离效果节点只能连接输出节点。  音源分离效果节点输出的音频格式如下：  采样率：48000Hz。  采样格式：[OH\_Audio\_SampleFormat](capi-native-audio-suite-base-h.md#oh_audio_sampleformat).AUDIO\_SAMPLE\_F32LE。  声道数：4（前2个声道用于人声，后2个声道用于伴奏）。 |
| EFFECT\_NODE\_TYPE\_VOICE\_BEAUTIFIER = 205 | 声音美化效果节点。声音美化效果节点支持的声音美化类型：[OH\_VoiceBeautifierType](capi-native-audio-suite-base-h.md#oh_voicebeautifiertype)。  声音美化效果节点输出的音频格式如下：  采样率：48000Hz。  采样格式：[OH\_Audio\_SampleFormat](capi-native-audio-suite-base-h.md#oh_audio_sampleformat).AUDIO\_SAMPLE\_S16LE。  声道数：2。 |
| EFFECT\_NODE\_TYPE\_ENVIRONMENT\_EFFECT = 206 | 环境效果节点。环境效果节点输出的音频格式如下：  采样率：48000Hz。  采样格式：[OH\_Audio\_SampleFormat](capi-native-audio-suite-base-h.md#oh_audio_sampleformat).AUDIO\_SAMPLE\_S16LE。  声道数：2。 |
| EFFECT\_NODE\_TYPE\_AUDIO\_MIXER = 207 | 混音效果节点。混音效果节点输出的音频格式如下：  采样率：[OH\_Audio\_SampleRate](capi-native-audio-suite-base-h.md#oh_audio_samplerate)。  采样格式：[OH\_Audio\_SampleFormat](capi-native-audio-suite-base-h.md#oh_audio_sampleformat).AUDIO\_SAMPLE\_F32LE。  声道数：2。 |
| EFFECT\_NODE\_TYPE\_SPACE\_RENDER = 208 | 空间渲染效果节点。空间渲染效果节点输出的音频格式如下：  采样率：48000Hz。  采样格式：[OH\_Audio\_SampleFormat](capi-native-audio-suite-base-h.md#oh_audio_sampleformat).AUDIO\_SAMPLE\_S16LE。  声道数：2。  **起始版本：** 23 |
| EFFECT\_NODE\_TYPE\_PURE\_VOICE\_CHANGE = 209 | 传统变声效果节点。传统变声效果节点输出的音频格式如下：  采样率：16000Hz。  采样格式：[OH\_Audio\_SampleFormat](capi-native-audio-suite-base-h.md#oh_audio_sampleformat).AUDIO\_SAMPLE\_S16LE。  声道数：1。  **起始版本：** 23 |
| EFFECT\_NODE\_TYPE\_GENERAL\_VOICE\_CHANGE = 210 | 通用变声效果节点。通用变声效果节点的输出音频格式如下：  采样率：48000Hz。  采样格式：[OH\_Audio\_SampleFormat](capi-native-audio-suite-base-h.md#oh_audio_sampleformat).AUDIO\_SAMPLE\_S16LE。  声道数：2。  **起始版本：** 23 |
| EFFECT\_NODE\_TYPE\_TEMPO\_PITCH = 211 | 变速变调效果节点。变速变调效果节点的输出音频格式如下：  采样率：48000Hz。  采样格式：[OH\_Audio\_SampleFormat](capi-native-audio-suite-base-h.md#oh_audio_sampleformat).AUDIO\_SAMPLE\_S16LE。  声道数：1。  **起始版本：** 23 |

### OH\_AudioSuite\_PipelineWorkMode

PhonePC/2in1Tablet

```
1. enum OH_AudioSuite_PipelineWorkMode
```

**描述**

定义音频编创管线工作模式。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSUITE\_PIPELINE\_EDIT\_MODE = 1 | 编辑模式，管线处于该工作模式下可创建多种效果节点进行音频处理。 |
| AUDIOSUITE\_PIPELINE\_REALTIME\_MODE = 2 | 实时渲染模式，即在音频处理过程中实时播放已处理的音频。  实时渲染模式下，管线仅支持均衡器效果处理。 |

### OH\_AudioSuite\_PipelineState

PhonePC/2in1Tablet

```
1. enum OH_AudioSuite_PipelineState
```

**描述**

定义音频编创管线运行状态。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSUITE\_PIPELINE\_STOPPED = 1 | 管线处于停止状态。 |
| AUDIOSUITE\_PIPELINE\_RUNNING = 2 | 管线处于运行状态。 |

### OH\_AudioSuite\_Result

PhonePC/2in1Tablet

```
1. enum OH_AudioSuite_Result
```

**描述**

音频编创错误码。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSUITE\_SUCCESS = 0 | 调用成功。 |
| AUDIOSUITE\_ERROR\_INVALID\_PARAM = 1 | 输入参数无效。 |
| AUDIOSUITE\_ERROR\_INVALID\_STATE = 2 | 非法状态。 |
| AUDIOSUITE\_ERROR\_SYSTEM = 3 | 系统通用错误。 |
| AUDIOSUITE\_ERROR\_UNSUPPORTED\_FORMAT = 4 | 不支持的音频格式，如不支持的编码类型、采样格式等。 |
| AUDIOSUITE\_ERROR\_ENGINE\_NOT\_EXIST = 5 | 引擎不存在。 |
| AUDIOSUITE\_ERROR\_PIPELINE\_NOT\_EXIST = 6 | 管线不存在。 |
| AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST = 7 | 节点不存在。 |
| AUDIOSUITE\_ERROR\_UNSUPPORTED\_CONNECT = 8 | 节点之间不支持连接。 |
| AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION = 9 | 不支持的操作。例如，效果节点不支持设置音频格式。 |
| AUDIOSUITE\_ERROR\_CREATED\_EXCEED\_SYSTEM\_LIMITS = 10 | 创建管线或者节点超过系统最大数量限制。具体情况如下：  引擎最多支持创建10条管线（其中，实时渲染管线最多创建1条）。  每一个管线中，输入节点不超过5个，输出节点不超过1个，混音节点不超过3个，音源分离节点不超过1个，其余效果节点不超过5个。 |
| AUDIOSUITE\_ERROR\_REQUIRED\_PARAMETERS\_MISSING = 11 | 参数缺少必要参数。例如，输入节点未设置回调函数、输出节点未设置音频格式。 |
| AUDIOSUITE\_ERROR\_TIMEOUT = 12 | 操作超时。 |
| AUDIOSUITE\_ERROR\_MEMORY\_ALLOC\_FAILED = 13 | 内存申请失败。 |

### OH\_Audio\_SampleFormat

PhonePC/2in1Tablet

```
1. enum OH_Audio_SampleFormat
```

**描述**

定义音频编创节点音频流的位深度。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| AUDIO\_SAMPLE\_U8 = 0 | Unsigned 8位。 |
| AUDIO\_SAMPLE\_S16LE = 1 | Short 16位小端。 |
| AUDIO\_SAMPLE\_S24LE = 2 | Short 24位小端。 |
| AUDIO\_SAMPLE\_S32LE = 3 | Short 32位小端。 |
| AUDIO\_SAMPLE\_F32LE = 4 | Float 32位小端。 |

### OH\_Audio\_EncodingType

PhonePC/2in1Tablet

```
1. enum OH_Audio_EncodingType
```

**描述**

定义音频流编码类型。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| AUDIO\_ENCODING\_TYPE\_RAW = 0 | PCM编码。 |

### OH\_Audio\_SampleRate

PhonePC/2in1Tablet

```
1. enum OH_Audio_SampleRate
```

**描述**

定义音频采样率。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| SAMPLE\_RATE\_8000 = 8000 | 采样率8kHz。 |
| SAMPLE\_RATE\_11025 = 11025 | 采样率11.025kHz。 |
| SAMPLE\_RATE\_12000 = 12000 | 采样率12kHz。 |
| SAMPLE\_RATE\_16000 = 16000 | 采样率16kHz。 |
| SAMPLE\_RATE\_22050 = 22050 | 采样率22.05kHz。 |
| SAMPLE\_RATE\_24000 = 24000 | 采样率24kHz。 |
| SAMPLE\_RATE\_32000 = 32000 | 采样率32kHz。 |
| SAMPLE\_RATE\_44100 = 44100 | 采样率44.1kHz。 |
| SAMPLE\_RATE\_48000 = 48000 | 采样率48kHz。 |
| SAMPLE\_RATE\_64000 = 64000 | 采样率64kHz。 |
| SAMPLE\_RATE\_88200 = 88200 | 采样率88.2kHz。 |
| SAMPLE\_RATE\_96000 = 96000 | 采样率96kHz。 |
| SAMPLE\_RATE\_176400 = 176400 | 采样率176.4kHz。 |
| SAMPLE\_RATE\_192000 = 192000 | 采样率192kHz。 |

### OH\_SoundFieldType

PhonePC/2in1Tablet

```
1. enum OH_SoundFieldType
```

**描述**

定义音频编创声场效果节点的效果模式。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| SOUND\_FIELD\_FRONT\_FACING = 1 | 前置声场效果。 |
| SOUND\_FIELD\_GRAND = 2 | 宏大声场效果。 |
| SOUND\_FIELD\_NEAR = 3 | 聆听声场效果。 |
| SOUND\_FIELD\_WIDE = 4 | 宽广声场效果。 |

### OH\_EnvironmentType

PhonePC/2in1Tablet

```
1. enum OH_EnvironmentType
```

**描述**

定义音频编创环境效果节点的模式。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| ENVIRONMENT\_TYPE\_BROADCAST = 1 | 环境节点效果为广播。 |
| ENVIRONMENT\_TYPE\_EARPIECE = 2 | 环境节点效果为电话听筒。 |
| ENVIRONMENT\_TYPE\_UNDERWATER = 3 | 环境节点效果为水下。 |
| ENVIRONMENT\_TYPE\_GRAMOPHONE = 4 | 环境节点效果为留声机。 |

### OH\_VoiceBeautifierType

PhonePC/2in1Tablet

```
1. enum OH_VoiceBeautifierType
```

**描述**

定义音频编创美化效果节点模式。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| VOICE\_BEAUTIFIER\_TYPE\_CLEAR = 1 | 声音美化节点效果为清澈。 |
| VOICE\_BEAUTIFIER\_TYPE\_THEATRE = 2 | 声音美化节点效果为剧场。 |
| VOICE\_BEAUTIFIER\_TYPE\_CD = 3 | 声音美化节点效果为CD。 |
| VOICE\_BEAUTIFIER\_TYPE\_RECORDING\_STUDIO = 4 | 声音美化节点效果为录音棚。 |

### OH\_AudioSuite\_SurroundDirection

PhonePC/2in1Tablet

```
1. enum OH_AudioSuite_SurroundDirection
```

**描述**

定义空间渲染效果节点旋转模式环绕方向。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| SPACE\_RENDER\_CCW = 0 | 逆时针旋转。 |
| SPACE\_RENDER\_CW = 1 | 顺时针旋转。 |

### OH\_AudioSuite\_PureVoiceChangeGenderOption

PhonePC/2in1Tablet

```
1. enum OH_AudioSuite_PureVoiceChangeGenderOption
```

**描述**

定义音频编创传统变声效果节点的性别。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| PURE\_VOICE\_CHANGE\_FEMALE = 1 | 设置女声。 |
| PURE\_VOICE\_CHANGE\_MALE = 2 | 设置男声。 |

### OH\_AudioSuite\_PureVoiceChangeType

PhonePC/2in1Tablet

```
1. enum OH_AudioSuite_PureVoiceChangeType
```

**描述**

定义音频编创传统变声效果节点的变声类型。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| PURE\_VOICE\_CHANGE\_TYPE\_CARTOON = 1 | 传统变声效果节点为卡通类型。 |
| PURE\_VOICE\_CHANGE\_TYPE\_CUTE = 2 | 传统变声效果节点为萝莉类型。 |
| PURE\_VOICE\_CHANGE\_TYPE\_FEMALE = 3 | 传统变声效果节点为女声类型。 |
| PURE\_VOICE\_CHANGE\_TYPE\_MALE = 4 | 传统变声效果节点为男声类型。 |
| PURE\_VOICE\_CHANGE\_TYPE\_MONSTER = 5 | 传统变声效果节点为怪兽类型。 |
| PURE\_VOICE\_CHANGE\_TYPE\_ROBOTS = 6 | 传统变声效果节点为机器人类型。 |
| PURE\_VOICE\_CHANGE\_TYPE\_SEASONED = 7 | 传统变声效果节点为大叔类型。 |

### OH\_AudioSuite\_GeneralVoiceChangeType

PhonePC/2in1Tablet

```
1. enum OH_AudioSuite_GeneralVoiceChangeType
```

**描述**

定义音频编创通用变声的节点类型。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| GENERAL\_VOICE\_CHANGE\_TYPE\_CUTE = 1 | 通用变声效果节点为萝莉类型。 |
| GENERAL\_VOICE\_CHANGE\_TYPE\_CYBERPUNK = 2 | 通用变声效果节点为赛博朋克类型。 |
| GENERAL\_VOICE\_CHANGE\_TYPE\_FEMALE = 3 | 通用变声效果节点为女声类型。 |
| GENERAL\_VOICE\_CHANGE\_TYPE\_MALE = 4 | 通用变声效果节点为男声类型。 |
| GENERAL\_VOICE\_CHANGE\_TYPE\_MIX = 5 | 通用变声效果节点为混响类型。 |
| GENERAL\_VOICE\_CHANGE\_TYPE\_MONSTER = 6 | 通用变声效果节点为怪兽类型。 |
| GENERAL\_VOICE\_CHANGE\_TYPE\_SEASONED = 7 | 通用变声效果节点为大叔类型。 |
| GENERAL\_VOICE\_CHANGE\_TYPE\_SYNTH = 8 | 通用变声效果节点为合成器类型。 |
| GENERAL\_VOICE\_CHANGE\_TYPE\_TRILL = 9 | 通用变声效果节点为颤音类型。 |
| GENERAL\_VOICE\_CHANGE\_TYPE\_WAR = 10 | 通用变声效果节点为战争类型。 |
