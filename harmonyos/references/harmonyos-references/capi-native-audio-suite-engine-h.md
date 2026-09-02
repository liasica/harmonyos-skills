---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-engine-h
title: native_audio_suite_engine.h
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 头文件 > native_audio_suite_engine.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6c2608d7d5c7e41e032883aa18102359b37c588af79f3981595190a4aacd9f28
---

## 概述

声明与音频编创相关接口。（包括引擎、管线、节点）。

**引用文件：** <ohaudiosuite/native\_audio\_suite\_engine.h>

**库：** libohaudiosuite.so

**系统能力：** SystemCapability.Multimedia.Audio.SuiteEngine

**起始版本：** 22

**相关模块：** [OHAudioSuite](capi-ohaudiosuite.md)

## 汇总

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_Create(OH\_AudioSuiteEngine\*\* audioSuiteEngine)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_create) | - | 创建音频编创引擎。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_Destroy(OH\_AudioSuiteEngine\* audioSuiteEngine)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_destroy) | - | 销毁音频编创引擎句柄。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_CreatePipeline(OH\_AudioSuiteEngine\* audioSuiteEngine, OH\_AudioSuitePipeline\*\* audioSuitePipeline, OH\_AudioSuite\_PipelineWorkMode workMode)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createpipeline) | - | 在当前音频编创引擎中创建1个管线。管线是引擎内负责音频编创的执行单元，1个引擎可创建多个管线。  支持最多创建10条管线。在API版本26.0.0之前，实时预览管线最多创建1条；在API版本26.0.0及以后，不再对实时预览管线的数量做单独限制，但管线的总数仍不得超过10条。  每个管线必须至少包含1个输入节点，有且只有1个输出节点。  当管线在[OH\_AudioSuite\_PipelineWorkMode](capi-native-audio-suite-base-h.md#oh_audiosuite_pipelineworkmode).AUDIOSUITE\_PIPELINE\_EDIT\_MODE模式下工作时，支持所有的效果节点。  在API version 23之前，当管线在[OH\_AudioSuite\_PipelineWorkMode](capi-native-audio-suite-base-h.md#oh_audiosuite_pipelineworkmode).AUDIOSUITE\_PIPELINE\_REALTIME\_MODE模式下工作时，仅支持[OH\_AudioNode\_Type](capi-native-audio-suite-base-h.md#oh_audionode_type).EFFECT\_NODE\_TYPE\_EQUALIZER效果节点；  在API version 23及以后，当管线在[OH\_AudioSuite\_PipelineWorkMode](capi-native-audio-suite-base-h.md#oh_audiosuite_pipelineworkmode).AUDIOSUITE\_PIPELINE\_REALTIME\_MODE模式下工作时，支持所有效果节点。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_DestroyPipeline(OH\_AudioSuitePipeline\* audioSuitePipeline)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_destroypipeline) | - | 销毁音频编创管线句柄。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_StartPipeline(OH\_AudioSuitePipeline\* audioSuitePipeline)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_startpipeline) | - | 开始运行该管线，管线会进入[OH\_AudioSuite\_PipelineState](capi-native-audio-suite-base-h.md#oh_audiosuite_pipelinestate).AUDIOSUITE\_PIPELINE\_RUNNING运行状态。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_StopPipeline(OH\_AudioSuitePipeline\* audioSuitePipeline)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_stoppipeline) | - | 停止运行该管线，管线会进入[OH\_AudioSuite\_PipelineState](capi-native-audio-suite-base-h.md#oh_audiosuite_pipelinestate).AUDIOSUITE\_PIPELINE\_STOPPED停止状态。该函数不会改变管线中节点之间的连接关系，管线一旦被停止，[OH\_AudioSuiteEngine\_RenderFrame](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_renderframe)就不能再进行音频处理。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetPipelineState(OH\_AudioSuitePipeline\* audioSuitePipeline, OH\_AudioSuite\_PipelineState\* pipelineState)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_getpipelinestate) | - | 获取当前管线的状态。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_RenderFrame(OH\_AudioSuitePipeline\* audioSuitePipeline, void\* audioData, int32\_t requestFrameSize, int32\_t\* responseSize, bool\* finishedFlag)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_renderframe) | - | 应用调用此接口获取管线处理后的音频数据（针对单输出效果节点）。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_MultiRenderFrame(OH\_AudioSuitePipeline\* audioSuitePipeline, OH\_AudioDataArray\* audioDataArray, int32\_t\* responseSize, bool\* finishedFlag)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_multirenderframe) | - | 渲染该管线，获取管线处理后的音频数据。针对多输出效果节点，比如包含音源分离节点的管线，audioDataArray的大小需与效果节点的输出数量一一对应（例如：音源分离节点需两个：第1个为人声，第2个为背景声）。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteNodeBuilder\_Create(OH\_AudioNodeBuilder\*\* builder)](capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_create) | - | 获取一个音频编创节点构造器，用于配置并创建音频节点。构建器可复用，但若新节点属性与之前不同，必须使用[OH\_AudioSuiteNodeBuilder\_Reset](capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_reset)重置。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteNodeBuilder\_Destroy(OH\_AudioNodeBuilder\* builder)](capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_destroy) | - | 销毁一个音频编创节点构造器。使用完构造器后必须调用此函数进行销毁。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteNodeBuilder\_Reset(OH\_AudioNodeBuilder\* builder)](capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_reset) | - | 重置一个音频编创节点构造器，同时将之前使用接口设置参数重置。若需复用构建器创建属性不同的新节点，必须调用此接口清除所有属性（如节点类型等）。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteNodeBuilder\_SetNodeType(OH\_AudioNodeBuilder\* builder, OH\_AudioNode\_Type type)](capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_setnodetype) | - | 设置当前节点构造器需要构造的节点类型。创建节点时会根据类型验证其他参数，所有节点类型的创建均需设置此属性。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteNodeBuilder\_SetFormat(OH\_AudioNodeBuilder\* builder, OH\_AudioFormat audioFormat)](capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_setformat) | - | 配置输入/输出节点的音频格式。其余节点不配置，且只能在创建节点之前使用。对于输入节点，此函数可使应用指定写入数据的音频格式；  对于输出节点，此函数可使应用指定其期望获取数据的音频格式；  对于其他类型的节点则不支持调用此函数进行音频格式设置。 |
| [typedef int32\_t (\*OH\_InputNode\_RequestDataCallback)(OH\_AudioNode\* audioNode, void\* userData, void\* audioData, int32\_t audioDataSize, bool\* finished)](capi-native-audio-suite-engine-h.md#oh_inputnode_requestdatacallback) | OH\_InputNode\_RequestDataCallback | 定义输入节点请求数据的回调函数。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteNodeBuilder\_SetRequestDataCallback(OH\_AudioNodeBuilder\* builder, OH\_InputNode\_RequestDataCallback callback, void\* userData)](capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_setrequestdatacallback) | - | 配置当前输入节点构造器的写入音频数据回调函数。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_CreateNode(OH\_AudioSuitePipeline\* audioSuitePipeline, OH\_AudioNodeBuilder\* builder, OH\_AudioNode\*\* audioNode)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode) | - | 根据音频编创构造器在音频管线中构造一个音频节点。当执行此函数，系统会基于builder中设置的节点类型校验参数的合法性。  应用可以通过返回值确定错误发生的原因。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_DestroyNode(OH\_AudioNode\* audioNode)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_destroynode) | - | 销毁一个音频编创节点。节点是否可以被销毁取决于它所属管线的状态，如果管线不处于[OH\_AudioSuite\_PipelineState](capi-native-audio-suite-base-h.md#oh_audiosuite_pipelinestate).AUDIOSUITE\_PIPELINE\_STOPPED停止状态，而节点处于管线处理路径中，将销毁失败。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetNodeBypassStatus(OH\_AudioNode\* audioNode, bool\* bypassStatus)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_getnodebypassstatus) | - | 获取当前节点的效果使能状态。仅效果节点支持获取。  若对输入或输出节点调用此接口，将返回AUDIOSUITE\_ERROR\_INVALID\_PARAM错误码。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_BypassEffectNode(OH\_AudioNode\* audioNode, bool bypass)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_bypasseffectnode) | - | 设置当前节点的效果使能状态（仅效果节点支持）。当bypass为true时，效果节点仅透传数据，不进行任何效果处理。  当bypass为false时，效果节点进行对应的效果处理。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_SetAudioFormat(OH\_AudioNode\* audioNode, OH\_AudioFormat \*audioFormat)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_setaudioformat) | - | 配置输入/输出节点的音频格式，在创建节点之后使用，只有输入和输出节点能够设置。输入节点指定音源格式，输出节点指定目标格式。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_ConnectNodes(OH\_AudioNode\* sourceAudioNode, OH\_AudioNode\* destAudioNode)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_connectnodes) | - | 连接两个节点，数据流走向从sourceAudioNode到destAudioNode。连接节点将改变管线拓扑，可能导致部分数据丢失，建议在引擎停止状态下执行此操作。  节点连接顺序：输入节点 -> 效果节点 -> 输出节点。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_DisconnectNodes(OH\_AudioNode\* sourceAudioNode, OH\_AudioNode\* destAudioNode)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_disconnectnodes) | - | 断开两个节点的连接。此操作将改变管线拓扑并可能导致数据丢失，建议在引擎停止状态下执行。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_SetEqualizerFrequencyBandGains(OH\_AudioNode\* audioNode, OH\_EqualizerFrequencyBandGains frequencyBandGains)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_setequalizerfrequencybandgains) | - | 设置当前均衡器节点的频段增益效果。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetEqualizerFrequencyBandGains(OH\_AudioNode\* audioNode, OH\_EqualizerFrequencyBandGains\* frequencyBandGains)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_getequalizerfrequencybandgains) | - | 获取当前均衡器节点的频段增益效果。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_SetSoundFieldType(OH\_AudioNode\* audioNode, OH\_SoundFieldType soundFieldType)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_setsoundfieldtype) | - | 设置声场效果节点的配置参数。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetSoundFieldType(OH\_AudioNode\* audioNode, OH\_SoundFieldType\* soundFieldType)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_getsoundfieldtype) | - | 获取声场效果节点的配置参数。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_SetEnvironmentType(OH\_AudioNode\* audioNode, OH\_EnvironmentType environmentType)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_setenvironmenttype) | - | 设置环境效果节点的配置参数。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetEnvironmentType(OH\_AudioNode\* audioNode, OH\_EnvironmentType\* environmentType)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_getenvironmenttype) | - | 获取环境效果节点的配置参数。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_SetVoiceBeautifierType(OH\_AudioNode\* audioNode, OH\_VoiceBeautifierType voiceBeautifierType)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_setvoicebeautifiertype) | - | 设置声音美化效果节点的配置参数。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetVoiceBeautifierType(OH\_AudioNode\* audioNode, OH\_VoiceBeautifierType\* voiceBeautifierType)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_getvoicebeautifiertype) | - | 获取声音美化效果节点的配置参数。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_IsNodeTypeSupported(OH\_AudioNode\_Type nodeType, bool\* isSupported)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_isnodetypesupported) | - | 查询当前系统是否支持创建指定的节点类型，避免节点创建失败。调用该接口时不依赖引擎及管线状态，仅跟系统相关，无需创建引擎及管线。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_SetSpaceRenderPositionParams(OH\_AudioNode\* audioNode, OH\_AudioSuite\_SpaceRenderPositionParams position)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_setspacerenderpositionparams) | - | 设置空间渲染效果节点固定摆位模式的配置参数。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetSpaceRenderPositionParams(OH\_AudioNode\* audioNode, OH\_AudioSuite\_SpaceRenderPositionParams\* position)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_getspacerenderpositionparams) | - | 获取空间渲染效果节点固定摆位模式的配置参数。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_SetSpaceRenderRotationParams(OH\_AudioNode\* audioNode, OH\_AudioSuite\_SpaceRenderRotationParams rotation)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_setspacerenderrotationparams) | - | 设置空间渲染效果节点旋转模式的配置参数。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetSpaceRenderRotationParams(OH\_AudioNode\* audioNode, OH\_AudioSuite\_SpaceRenderRotationParams\* rotation)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_getspacerenderrotationparams) | - | 获取空间渲染效果节点旋转模式的配置参数。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_SetSpaceRenderExtensionParams(OH\_AudioNode\* audioNode, OH\_AudioSuite\_SpaceRenderExtensionParams extension)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_setspacerenderextensionparams) | - | 设置空间渲染效果节点扩展模式的配置参数。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetSpaceRenderExtensionParams(OH\_AudioNode\* audioNode, OH\_AudioSuite\_SpaceRenderExtensionParams\* extension)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_getspacerenderextensionparams) | - | 获取空间渲染效果节点扩展模式的配置参数。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_SetTempoAndPitch(OH\_AudioNode\* audioNode, float speed, float pitch)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_settempoandpitch) | - | 设置变速变调效果节点的配置参数。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetTempoAndPitch(OH\_AudioNode\* audioNode, float\* speed, float\* pitch)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_gettempoandpitch) | - | 获取变速变调效果节点的配置参数。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_SetPureVoiceChangeOption(OH\_AudioNode\* audioNode, OH\_AudioSuite\_PureVoiceChangeOption option)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_setpurevoicechangeoption) | - | 设置传统变声节点的配置参数。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetPureVoiceChangeOption(OH\_AudioNode\* audioNode, OH\_AudioSuite\_PureVoiceChangeOption\* option)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_getpurevoicechangeoption) | - | 获取传统变声节点的配置参数。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_SetGeneralVoiceChangeType(OH\_AudioNode\* audioNode, OH\_AudioSuite\_GeneralVoiceChangeType type)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_setgeneralvoicechangetype) | - | 设置通用变声节点的配置参数。 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetGeneralVoiceChangeType(OH\_AudioNode\* audioNode, OH\_AudioSuite\_GeneralVoiceChangeType\* type)](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_getgeneralvoicechangetype) | - | 获取通用变声节点的配置参数。 |
| [OH\_AudioSuite\_Result OH\_AudioSuite\_PrintInfo(OH\_AudioSuiteEngine\* audioSuiteEngine, OH\_AudioSuitePipeline\* audioSuitePipeline, int fd)](capi-native-audio-suite-engine-h.md#oh_audiosuite_printinfo) | - | 打印AudioSuite运行时快照。 |

## 函数说明

### OH\_AudioSuiteEngine\_Create()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_Create(OH_AudioSuiteEngine** audioSuiteEngine)
```

**描述**

创建音频编创引擎。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSuiteEngine](capi-ohaudiosuite-oh-audiosuiteenginestruct.md)\*\* audioSuiteEngine | 音频编创引擎句柄，指向接收audioSuiteEngine变量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数audioSuiteEngine为空指针。  AUDIOSUITE\_ERROR\_INVALID\_STATE：引擎已经被初始化。  AUDIOSUITE\_ERROR\_MEMORY\_ALLOC\_FAILED：内存申请失败。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_Destroy()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_Destroy(OH_AudioSuiteEngine* audioSuiteEngine)
```

**描述**

销毁音频编创引擎句柄。

**说明** 

销毁引擎时会同时销毁该引擎下的所有管线。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSuiteEngine](capi-ohaudiosuite-oh-audiosuiteenginestruct.md)\* audioSuiteEngine | 音频编创引擎句柄，通过[OH\_AudioSuiteEngine\_Create](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_create)获取句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数audioSuiteEngine为空指针。  AUDIOSUITE\_ERROR\_INVALID\_STATE：引擎已被去初始化、引擎未创建或引擎未初始化。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_CreatePipeline()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_CreatePipeline(OH_AudioSuiteEngine* audioSuiteEngine, OH_AudioSuitePipeline** audioSuitePipeline, OH_AudioSuite_PipelineWorkMode workMode)
```

**描述**

在当前音频编创引擎中创建1个管线。管线是引擎内负责音频编创的执行单元，1个引擎可创建多个管线。

支持最多创建10条管线。在API版本26.0.0之前，实时预览管线最多创建1条；在API版本26.0.0及以后，不再对实时预览管线的数量做单独限制，但管线的总数仍不得超过10条。

每个管线必须至少包含1个输入节点，有且只有1个输出节点。

当管线在[OH\_AudioSuite\_PipelineWorkMode](capi-native-audio-suite-base-h.md#oh_audiosuite_pipelineworkmode).AUDIOSUITE\_PIPELINE\_EDIT\_MODE模式下工作时，支持所有的效果节点。

在API version 23之前，当管线在[OH\_AudioSuite\_PipelineWorkMode](capi-native-audio-suite-base-h.md#oh_audiosuite_pipelineworkmode).AUDIOSUITE\_PIPELINE\_REALTIME\_MODE模式下工作时，仅支持[OH\_AudioNode\_Type](capi-native-audio-suite-base-h.md#oh_audionode_type).EFFECT\_NODE\_TYPE\_EQUALIZER效果节点；

在API version 23及以后，当管线在[OH\_AudioSuite\_PipelineWorkMode](capi-native-audio-suite-base-h.md#oh_audiosuite_pipelineworkmode).AUDIOSUITE\_PIPELINE\_REALTIME\_MODE模式下工作时，支持所有效果节点。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSuiteEngine](capi-ohaudiosuite-oh-audiosuiteenginestruct.md)\* audioSuiteEngine | 音频编创引擎句柄。通过[OH\_AudioSuiteEngine\_Create](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_create)获取句柄。 |
| [OH\_AudioSuitePipeline](capi-ohaudiosuite-oh-audiosuitepipelinestruct.md)\*\* audioSuitePipeline | 音频编创管线句柄。 |
| [OH\_AudioSuite\_PipelineWorkMode](capi-native-audio-suite-base-h.md#oh_audiosuite_pipelineworkmode) workMode | 管线工作模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数audioSuiteEngine为空指针或参数audioSuitePipeline为空指针。  AUDIOSUITE\_ERROR\_ENGINE\_NOT\_EXIST：未初始化引擎。  AUDIOSUITE\_ERROR\_CREATED\_EXCEED\_SYSTEM\_LIMITS：创建管线数量超过系统最大数量限制（引擎最多创建10条管线）。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_MEMORY\_ALLOC\_FAILED：内存申请失败。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_DestroyPipeline()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_DestroyPipeline(OH_AudioSuitePipeline* audioSuitePipeline)
```

**描述**

销毁音频编创管线句柄。

**说明** 

销毁管线时会同时销毁该管线下的所有节点。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSuitePipeline](capi-ohaudiosuite-oh-audiosuitepipelinestruct.md)\* audioSuitePipeline | 音频编创管线句柄。通过[OH\_AudioSuiteEngine\_CreatePipeline](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createpipeline)获取需要销毁的句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数audioSuitePipeline为空指针。  AUDIOSUITE\_ERROR\_PIPELINE\_NOT\_EXIST：管线不存在或已经被销毁。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_StartPipeline()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_StartPipeline(OH_AudioSuitePipeline* audioSuitePipeline)
```

**描述**

开始运行该管线，管线会进入[OH\_AudioSuite\_PipelineState](capi-native-audio-suite-base-h.md#oh_audiosuite_pipelinestate).AUDIOSUITE\_PIPELINE\_RUNNING运行状态。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSuitePipeline](capi-ohaudiosuite-oh-audiosuitepipelinestruct.md)\* audioSuitePipeline | 音频编创管线句柄。通过[OH\_AudioSuiteEngine\_CreatePipeline](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createpipeline)获取句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数audioSuitePipeline为空指针。  AUDIOSUITE\_ERROR\_PIPELINE\_NOT\_EXIST：管线不存在或已经被销毁。  AUDIOSUITE\_ERROR\_INVALID\_STATE：管线已在运行或节点连接异常。  可能的原因如下：  1. 管线已经在运行状态；  2. 当前管线中不存在输出类型节点；  3. 起始节点不是输入类型节点。  4. HOA（High-Order Ambisonics）音频格式的输入节点未连接HOA空间渲染节点，或HOA空间渲染节点的前置节点不是HOA格式的输入节点。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_StopPipeline()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_StopPipeline(OH_AudioSuitePipeline* audioSuitePipeline)
```

**描述**

停止运行该管线，管线会进入[OH\_AudioSuite\_PipelineState](capi-native-audio-suite-base-h.md#oh_audiosuite_pipelinestate).AUDIOSUITE\_PIPELINE\_STOPPED停止状态。该函数不会改变管线中节点之间的连接关系，管线一旦被停止，[OH\_AudioSuiteEngine\_RenderFrame](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_renderframe)就不能再进行音频处理。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSuitePipeline](capi-ohaudiosuite-oh-audiosuitepipelinestruct.md)\* audioSuitePipeline | 音频编创管线句柄。通过[OH\_AudioSuiteEngine\_CreatePipeline](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createpipeline)获取句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数audioSuitePipeline为空指针。  AUDIOSUITE\_ERROR\_PIPELINE\_NOT\_EXIST：管线不存在或已经被销毁。  AUDIOSUITE\_ERROR\_INVALID\_STATE：管线已在停止状态。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_GetPipelineState()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_GetPipelineState(OH_AudioSuitePipeline* audioSuitePipeline, OH_AudioSuite_PipelineState* pipelineState)
```

**描述**

获取当前管线的状态。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSuitePipeline](capi-ohaudiosuite-oh-audiosuitepipelinestruct.md)\* audioSuitePipeline | 音频编创管线句柄。通过[OH\_AudioSuiteEngine\_CreatePipeline](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createpipeline)获取句柄。 |
| [OH\_AudioSuite\_PipelineState](capi-native-audio-suite-base-h.md#oh_audiosuite_pipelinestate)\* pipelineState | 管线状态的输出参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。例如，audioSuitePipeline为空指针等。  AUDIOSUITE\_ERROR\_PIPELINE\_NOT\_EXIST：管线不存在或已经被销毁。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_RenderFrame()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_RenderFrame(OH_AudioSuitePipeline* audioSuitePipeline, void* audioData, int32_t requestFrameSize, int32_t* responseSize, bool* finishedFlag)
```

**描述**

应用调用此接口获取管线处理后的音频数据（针对单输出效果节点）。

**说明** 

应用程序需调用此接口获取经过效果处理后的音频数据。

* 调用后，管线会从输出节点向前依次拉取数据、应用效果处理，
* 最终将处理后的数据填充到应用程序传入的audioData指针中。
* 系统会尝试按requestFrameSize请求的大小填充数据，实际处理的数据大小通过responseSize返回给应用程序。
* 当应用程序为所有输入节点准备好数据并通过回调提交最后一次数据时，应在回调中设置完成标志。
* 当管线中所有输入都传递了完成标志后，接口处理完成后会通过finishedFlag通知应用程序。
* 若finishedFlag为true，应用程序不应再调用此接口。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSuitePipeline](capi-ohaudiosuite-oh-audiosuitepipelinestruct.md)\* audioSuitePipeline | 音频编创管线句柄。通过[OH\_AudioSuiteEngine\_CreatePipeline](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createpipeline)获取句柄。 |
| void\* audioData | 获取音频需要写入的数据地址。 |
| int32\_t requestFrameSize | audioData的内存字节大小，需大于0。 |
| int32\_t\* responseSize | 管线写入audioData的音频数据大小，不会大于requestFrameSize，单位为字节。 |
| bool\* finishedFlag | 标识当前管线是否渲染完成。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数为空指针或无效值。  可能的原因如下：  1. 参数audioSuitePipeline为空指针；  2. 参数audioData为空指针；  3. 参数requestFrameSize小于等于0；  4. 参数responseSize为空指针；  5. 参数finishedFlag为空指针。  AUDIOSUITE\_ERROR\_PIPELINE\_NOT\_EXIST：管线不存在或已经被销毁。  AUDIOSUITE\_ERROR\_INVALID\_STATE：管线不在运行状态。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：管线渲染已完成（之前调用该接口时finishedFlag已写入为true）。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_MultiRenderFrame()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_MultiRenderFrame(OH_AudioSuitePipeline* audioSuitePipeline, OH_AudioDataArray* audioDataArray, int32_t* responseSize, bool* finishedFlag)
```

**描述**

渲染该管线，获取管线处理后的音频数据。针对多输出效果节点，比如包含音源分离节点的管线，audioDataArray的大小需与效果节点的输出数量一一对应（例如：音源分离节点需两个：第1个为人声，第2个为背景声）。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSuitePipeline](capi-ohaudiosuite-oh-audiosuitepipelinestruct.md)\* audioSuitePipeline | 音频编创管线句柄。通过[OH\_AudioSuiteEngine\_CreatePipeline](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createpipeline)获取句柄。 |
| [OH\_AudioDataArray](capi-ohaudiosuite-oh-audiodataarray.md)\* audioDataArray | 用户读取音频数据时所使用的数组指针，每个一维数组大小需一致。 |
| int32\_t\* responseSize | 管线写入audioDataArray的音频数据大小。系统会确保每个一维数组被填充的数据大小一致，单位为字节（Byte）。 |
| bool\* finishedFlag | 标记当前管线是否渲染完成。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数为空指针或无效值。  可能的原因如下：  1. 参数audioSuitePipeline为空指针；  2. 参数audioDataArray为空指针；  3. 参数audioDataArray中的某个成员为空指针；  4. 参数audioDataArray中的requestFrameSize小于等于0；  5. 参数responseSize为空指针；  6. 参数finishedFlag为空指针。  AUDIOSUITE\_ERROR\_PIPELINE\_NOT\_EXIST：管线不存在或已经被销毁。  AUDIOSUITE\_ERROR\_INVALID\_STATE：管线不在运行状态。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：管线渲染已完成（之前调用该接口时finishedFlag已写入为true）。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteNodeBuilder\_Create()

```c
OH_AudioSuite_Result OH_AudioSuiteNodeBuilder_Create(OH_AudioNodeBuilder** builder)
```

**描述**

获取一个音频编创节点构造器，用于配置并创建音频节点。构建器可复用，但若新节点属性与之前不同，必须使用[OH\_AudioSuiteNodeBuilder\_Reset](capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_reset)重置。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNodeBuilder](capi-ohaudiosuite-oh-audionodebuilderstruct.md)\*\* builder | 音频编创节点构造器句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。例如，builder为空指针。  AUDIOSUITE\_ERROR\_MEMORY\_ALLOC\_FAILED：内存申请失败。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteNodeBuilder\_Destroy()

```c
OH_AudioSuite_Result OH_AudioSuiteNodeBuilder_Destroy(OH_AudioNodeBuilder* builder)
```

**描述**

销毁一个音频编创节点构造器。使用完构造器后必须调用此函数进行销毁。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNodeBuilder](capi-ohaudiosuite-oh-audionodebuilderstruct.md)\* builder | 音频编创节点构造器句柄。通过[OH\_AudioSuiteNodeBuilder\_Create](capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_create)获取句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。例如，builder为空指针。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteNodeBuilder\_Reset()

```c
OH_AudioSuite_Result OH_AudioSuiteNodeBuilder_Reset(OH_AudioNodeBuilder* builder)
```

**描述**

重置一个音频编创节点构造器，同时将之前使用接口设置参数重置。若需复用构建器创建属性不同的新节点，必须调用此接口清除所有属性（如节点类型等）。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNodeBuilder](capi-ohaudiosuite-oh-audionodebuilderstruct.md)\* builder | 音频编创节点构造器句柄。通过[OH\_AudioSuiteNodeBuilder\_Create](capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_create)获取句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。例如，builder为空指针。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteNodeBuilder\_SetNodeType()

```c
OH_AudioSuite_Result OH_AudioSuiteNodeBuilder_SetNodeType(OH_AudioNodeBuilder* builder, OH_AudioNode_Type type)
```

**描述**

设置当前节点构造器需要构造的节点类型。创建节点时会根据类型验证其他参数，所有节点类型的创建均需设置此属性。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNodeBuilder](capi-ohaudiosuite-oh-audionodebuilderstruct.md)\* builder | 音频编创节点构造器句柄。通过[OH\_AudioSuiteNodeBuilder\_Create](capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_create)获取句柄。 |
| [OH\_AudioNode\_Type](capi-native-audio-suite-base-h.md#oh_audionode_type) type | 节点类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：配置节点类型成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效，例如，builder为空指针。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteNodeBuilder\_SetFormat()

```c
OH_AudioSuite_Result OH_AudioSuiteNodeBuilder_SetFormat(OH_AudioNodeBuilder* builder, OH_AudioFormat audioFormat)
```

**描述**

配置输入/输出节点的音频格式。只能在创建节点之前使用。对于输入节点，此函数可使应用指定写入数据的音频格式；

对于输出节点，此函数可使应用指定其期望获取数据的音频格式；

对于其他类型的节点则不支持调用此函数进行音频格式设置。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNodeBuilder](capi-ohaudiosuite-oh-audionodebuilderstruct.md)\* builder | 音频编创节点构造器句柄。通过[OH\_AudioSuiteNodeBuilder\_Create](capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_create)获取句柄。 |
| [OH\_AudioFormat](capi-ohaudiosuite-oh-audioformat.md) audioFormat | 音频流格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效，例如，builder为空指针。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_FORMAT：audioFormat中的channelCount不支持。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_InputNode\_RequestDataCallback()

```c
typedef int32_t (*OH_InputNode_RequestDataCallback)(OH_AudioNode* audioNode, void* userData, void* audioData, int32_t audioDataSize, bool* finished)
```

**描述**

定义输入节点请求数据的回调函数。

**说明** 

用户把需要处理的PCM音频数据写入到audioData，OHAudioSuite从audioData拿到数据进行音频编创。

* 应用程序在此回调中向audioData写入不超过audioDataSize大小的数据。
* 当所有数据通过回调传递给管线后，应用程序应在最后一次回调中将finished设为true，此后管线不再调用此接口。
* 只有输入节点需要配置，其余节点不配置。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_AudioNode\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| void\* userData | 用户使用的数据指针。系统调用此回调函数时，将使用[OH\_AudioSuiteNodeBuilder\_SetRequestDataCallback](capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_setrequestdatacallback)接口传入的userData。 |
| void\* audioData | 系统提供的内存地址，用于将需要处理的音频数据流写入（需由用户填充）。 |
| int32\_t audioDataSize | audioData内存地址指向的音频数据大小，单位为字节（Byte）。 |
| bool\* finished | 标记audioNode节点需要处理的音频数据流是否已经写入完成。true表示已完成，false表示未完成。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 写入audioData缓冲区的有效数据长度（单位为字节）。  返回值范围必须在[0, audioDataSize]范围内，如果返回值小于0，系统会将其修改为0，  如果返回值大于audioDataSize，系统会将其修改为audioDataSize。 |

### OH\_AudioSuiteNodeBuilder\_SetRequestDataCallback()

```c
OH_AudioSuite_Result OH_AudioSuiteNodeBuilder_SetRequestDataCallback(OH_AudioNodeBuilder* builder, OH_InputNode_RequestDataCallback callback, void* userData)
```

**描述**

配置当前输入节点构造器的写入音频数据回调函数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNodeBuilder](capi-ohaudiosuite-oh-audionodebuilderstruct.md)\* builder | 音频编创节点构造器句柄。通过[OH\_AudioSuiteNodeBuilder\_Create](capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_create)获取句柄。 |
| [OH\_InputNode\_RequestDataCallback](capi-native-audio-suite-engine-h.md#oh_inputnode_requestdatacallback) callback | 写入当前节点音频数据的回调接口。 |
| void\* userData | 用户自定义数据，在回调函数callback中传入给用户。不使用时可传空指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：  可能的原因如下：  1. 参数builder为空指针；  2. 参数callback为空指针。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_CreateNode()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_CreateNode(OH_AudioSuitePipeline* audioSuitePipeline, OH_AudioNodeBuilder* builder, OH_AudioNode** audioNode)
```

**描述**

根据音频编创构造器在音频管线中构造一个音频节点。当执行此函数，系统会基于builder中设置的节点类型校验参数的合法性。

应用可以通过返回值确定错误发生的原因。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSuitePipeline](capi-ohaudiosuite-oh-audiosuitepipelinestruct.md)\* audioSuitePipeline | 音频编创管线句柄。通过[OH\_AudioSuiteEngine\_CreatePipeline](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createpipeline)获取句柄。 |
| [OH\_AudioNodeBuilder](capi-ohaudiosuite-oh-audionodebuilderstruct.md)\* builder | 音频编创节点构造器句柄。通过[OH\_AudioSuiteNodeBuilder\_Create](capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_create)获取句柄。 |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\*\* audioNode | 输出参数，用于返回创建的音频编创节点句柄的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数为空指针或无效值。  可能的原因如下：  1. 参数audioSuitePipeline为空指针；  2. 参数builder为空指针；  3. 参数audioNode为空指针。  AUDIOSUITE\_ERROR\_CREATED\_EXCEED\_SYSTEM\_LIMITS：当构建当前类型的节点数量超过管线限制。  例如，在API version 24之前，创建效果类节点的数量超过5个；在API version 24及以后，创建效果类节点的数量超过15个。  AUDIOSUITE\_ERROR\_REQUIRED\_PARAMETERS\_MISSING：构建builder中type类型的节点时缺少必要参数。  例如，builder未设置节点类型。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：当前构造器节点类型为输出节点但设置了回调函数，  或构造器节点类型为效果节点但设置了音频格式或回调函数。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_MEMORY\_ALLOC\_FAILED：内存申请失败。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_DestroyNode()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_DestroyNode(OH_AudioNode* audioNode)
```

**描述**

销毁一个音频编创节点。节点是否可以被销毁取决于它所属管线的状态，如果管线不处于[OH\_AudioSuite\_PipelineState](capi-native-audio-suite-base-h.md#oh_audiosuite_pipelinestate).AUDIOSUITE\_PIPELINE\_STOPPED停止状态，而节点处于管线处理路径中，将销毁失败。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数audioNode为空指针。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_INVALID\_STATE：管线不在停止状态。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_GetNodeBypassStatus()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_GetNodeBypassStatus(OH_AudioNode* audioNode, bool* bypassStatus)
```

**描述**

获取当前节点的效果使能状态。仅效果节点支持获取。

若对输入或输出节点调用此接口，将返回AUDIOSUITE\_ERROR\_INVALID\_PARAM错误码。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| bool\* bypassStatus | 获取当前效果类节点使能状态，false表示未跳过节点处理，true表示已跳过节点处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：  参数audioNode或bypassStatus为空指针。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode节点类型为非效果类节点。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_BypassEffectNode()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_BypassEffectNode(OH_AudioNode* audioNode, bool bypass)
```

**描述**

设置当前节点的效果使能状态（仅效果节点支持）。当bypass为true时，效果节点仅透传数据，不进行任何效果处理。

当bypass为false时，效果节点进行对应的效果处理。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| bool bypass | 当前效果类节点使能状态。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数audioNode为空指针。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode为非效果节点。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_SetAudioFormat()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_SetAudioFormat(OH_AudioNode* audioNode, OH_AudioFormat* audioFormat)
```

**描述**

配置输入/输出节点的音频格式，在创建节点之后使用，只有输入和输出节点能够设置。输入节点指定音源格式，输出节点指定目标格式。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| [OH\_AudioFormat](capi-ohaudiosuite-oh-audioformat.md)\* audioFormat | 指向音频流格式的指针，用于设置音频格式信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数audioNode或audioFormat为空指针。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode是效果节点。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_FORMAT：（API版本26.0.0新增）参数audioFormat为不支持的格式。  AUDIOSUITE\_ERROR\_INVALID\_STATE：管线不在停止状态。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_ConnectNodes()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_ConnectNodes(OH_AudioNode* sourceAudioNode, OH_AudioNode* destAudioNode)
```

**描述**

连接两个节点，数据流走向从sourceAudioNode到destAudioNode。连接节点将改变管线拓扑，可能导致部分数据丢失，建议在引擎停止状态下执行此操作。

节点连接顺序：输入节点 -> 效果节点 -> 输出节点。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* sourceAudioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* destAudioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数sourceAudioNode或destAudioNode为空指针。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_CONNECT：节点之间不支持连接。  可能的原因如下：  1. 参数sourceAudioNode类型为输出类型节点；  2. 参数destAudioNode类型为输入类型节点；  3. 参数sourceAudioNode和destAudioNode为同一个节点；  4. 参数sourceAudioNode为音源分离类型，但是destAudioNode类型不为输出类型节点；  5. 参数sourceAudioNode和destAudioNode不为同一个管线中的节点；  6. 管线状态为运行状态，但是destAudioNode不为mix类型节点；  7. 管线状态为运行状态，destAudioNode为mix类型节点，但是sourceAudioNode节点未连接输入类型节点。  AUDIOSUITE\_ERROR\_INVALID\_STATE：管线为无效状态。例如，无法找到输出节点。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_DisconnectNodes()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_DisconnectNodes(OH_AudioNode* sourceAudioNode, OH_AudioNode* destAudioNode)
```

**描述**

断开两个节点的连接。此操作将改变管线拓扑并可能导致数据丢失，建议在引擎停止状态下执行。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* sourceAudioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* destAudioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数sourceAudioNode或destAudioNode为空指针。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：不支持操作。  可能的原因如下：  1. 参数sourceAudioNode类型为输出类型节点；  2. 参数destAudioNode类型为输入类型节点；  3. 参数sourceAudioNode和destAudioNode为同一个节点；  4. 参数sourceAudioNode和destAudioNode不为同一个管线中的节点；  5. 管线状态为运行状态，但是destAudioNode不为mix类型节点；  6. 管线状态为运行状态，destAudioNode为mix类型节点，但是mix节点当前只连接了sourceAudioNode一个输入。  AUDIOSUITE\_ERROR\_INVALID\_STATE：管线为无效状态。例如，无法找到输出节点。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_SetEqualizerFrequencyBandGains()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_SetEqualizerFrequencyBandGains(OH_AudioNode* audioNode, OH_EqualizerFrequencyBandGains frequencyBandGains)
```

**描述**

设置当前均衡器节点的频段增益效果。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| [OH\_EqualizerFrequencyBandGains](capi-ohaudiosuite-oh-equalizerfrequencybandgains.md) frequencyBandGains | 均衡器节点的均衡参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode节点类型为非均衡器节点。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：  可能的原因如下：  1. 参数audioNode为空指针；  2. 参数frequencyBandGains每个成员的值不在[-10, 10]范围内。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_GetEqualizerFrequencyBandGains()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_GetEqualizerFrequencyBandGains(OH_AudioNode* audioNode, OH_EqualizerFrequencyBandGains* frequencyBandGains)
```

**描述**

获取当前均衡器节点的频段增益效果。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| [OH\_EqualizerFrequencyBandGains](capi-ohaudiosuite-oh-equalizerfrequencybandgains.md)\* frequencyBandGains | 均衡器节点的均衡参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode节点类型为非均衡器节点。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。例如，audioNode或frequencyBandGains为空指针。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_SetSoundFieldType()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_SetSoundFieldType(OH_AudioNode* audioNode, OH_SoundFieldType soundFieldType)
```

**描述**

设置声场效果节点的配置参数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| [OH\_SoundFieldType](capi-native-audio-suite-base-h.md#oh_soundfieldtype) soundFieldType | 声场效果节点的配置参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode节点类型为非声场节点。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。例如，audioNode为空指针。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_GetSoundFieldType()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_GetSoundFieldType(OH_AudioNode* audioNode, OH_SoundFieldType* soundFieldType)
```

**描述**

获取声场效果节点的配置参数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| [OH\_SoundFieldType](capi-native-audio-suite-base-h.md#oh_soundfieldtype)\* soundFieldType | 声场效果节点的配置参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode节点类型为非soundFieldType节点。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。例如，audioNode或soundFieldType为空指针。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_SetEnvironmentType()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_SetEnvironmentType(OH_AudioNode* audioNode, OH_EnvironmentType environmentType)
```

**描述**

设置环境效果节点的配置参数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| [OH\_EnvironmentType](capi-native-audio-suite-base-h.md#oh_environmenttype) environmentType | 环境效果节点的配置参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode节点类型为非环境节点。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。例如，audioNode为空指针。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_GetEnvironmentType()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_GetEnvironmentType(OH_AudioNode* audioNode, OH_EnvironmentType* environmentType)
```

**描述**

获取环境效果节点的配置参数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| [OH\_EnvironmentType](capi-native-audio-suite-base-h.md#oh_environmenttype)\* environmentType | 环境效果节点的配置参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode节点类型为非环境效果节点。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。例如，audioNode或environmentType为空指针。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_SetVoiceBeautifierType()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_SetVoiceBeautifierType(OH_AudioNode* audioNode, OH_VoiceBeautifierType voiceBeautifierType)
```

**描述**

设置声音美化效果节点的配置参数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| [OH\_VoiceBeautifierType](capi-native-audio-suite-base-h.md#oh_voicebeautifiertype) voiceBeautifierType | 声音美化效果节点的配置参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode节点类型为非声音美化效果节点。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。例如，audioNode为空指针。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_GetVoiceBeautifierType()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_GetVoiceBeautifierType(OH_AudioNode* audioNode, OH_VoiceBeautifierType* voiceBeautifierType)
```

**描述**

获取声音美化效果节点的配置参数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| [OH\_VoiceBeautifierType](capi-native-audio-suite-base-h.md#oh_voicebeautifiertype)\* voiceBeautifierType | 声音美化效果节点的配置参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode节点类型为非声音美化效果节点。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。  例如，audioNode或voiceBeautifierType为空指针。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_IsNodeTypeSupported()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_IsNodeTypeSupported(OH_AudioNode_Type nodeType, bool* isSupported)
```

**描述**

查询当前系统是否支持创建指定的节点类型，避免节点创建失败。调用该接口时不依赖引擎及管线状态，仅跟系统相关，无需创建引擎及管线。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode\_Type](capi-native-audio-suite-base-h.md#oh_audionode_type) nodeType | 待查的节点类型。 |
| bool\* isSupported | 表示是否支持当前节点的创建。false表示未支持，true表示已支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：查询函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：传入非法参数。  例如，入参nodeType不在OH\_AudioNode\_Type枚举类型范围内、isSupported为空指针等。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_SetSpaceRenderPositionParams()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_SetSpaceRenderPositionParams(OH_AudioNode* audioNode, OH_AudioSuite_SpaceRenderPositionParams position)
```

**描述**

设置空间渲染效果节点固定摆位模式的配置参数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| [OH\_AudioSuite\_SpaceRenderPositionParams](capi-ohaudiosuite-oh-audiosuite-spacerenderpositionparams.md) position | 空间渲染效果节点固定摆位模式的配置参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode节点类型为非空间渲染效果节点。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。例如，audioNode为空指针。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_GetSpaceRenderPositionParams()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_GetSpaceRenderPositionParams(OH_AudioNode* audioNode, OH_AudioSuite_SpaceRenderPositionParams* position)
```

**描述**

获取空间渲染效果节点固定摆位模式的配置参数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| [OH\_AudioSuite\_SpaceRenderPositionParams](capi-ohaudiosuite-oh-audiosuite-spacerenderpositionparams.md)\* position | 空间渲染效果节点固定摆位模式的配置参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode节点类型为非空间渲染效果节点。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。例如，audioNode为空指针。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_SetSpaceRenderRotationParams()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_SetSpaceRenderRotationParams(OH_AudioNode* audioNode, OH_AudioSuite_SpaceRenderRotationParams rotation)
```

**描述**

设置空间渲染效果节点旋转模式的配置参数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| [OH\_AudioSuite\_SpaceRenderRotationParams](capi-ohaudiosuite-oh-audiosuite-spacerenderrotationparams.md) rotation | 空间渲染效果节点旋转模式的配置参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode节点类型为非空间渲染效果节点。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。例如，audioNode为空指针。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_GetSpaceRenderRotationParams()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_GetSpaceRenderRotationParams(OH_AudioNode* audioNode, OH_AudioSuite_SpaceRenderRotationParams* rotation)
```

**描述**

获取空间渲染效果节点旋转模式的配置参数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| [OH\_AudioSuite\_SpaceRenderRotationParams](capi-ohaudiosuite-oh-audiosuite-spacerenderrotationparams.md)\* rotation | 空间渲染效果节点旋转模式的配置参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode节点类型为非空间渲染效果节点。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。例如，audioNode为空指针。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_SetSpaceRenderExtensionParams()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_SetSpaceRenderExtensionParams(OH_AudioNode* audioNode, OH_AudioSuite_SpaceRenderExtensionParams extension)
```

**描述**

设置空间渲染效果节点扩展模式的配置参数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| [OH\_AudioSuite\_SpaceRenderExtensionParams](capi-ohaudiosuite-oh-audiosuite-spacerenderextensionparams.md) extension | 空间渲染效果节点扩展模式的配置参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode节点类型为非空间渲染效果节点。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。例如，audioNode为空指针。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_GetSpaceRenderExtensionParams()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_GetSpaceRenderExtensionParams(OH_AudioNode* audioNode, OH_AudioSuite_SpaceRenderExtensionParams* extension)
```

**描述**

获取空间渲染效果节点扩展模式的配置参数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| [OH\_AudioSuite\_SpaceRenderExtensionParams](capi-ohaudiosuite-oh-audiosuite-spacerenderextensionparams.md)\* extension | 空间渲染效果节点扩展模式的配置参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode节点类型为非空间渲染效果节点。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。例如，audioNode为空指针。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_SetTempoAndPitch()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_SetTempoAndPitch(OH_AudioNode* audioNode, float speed, float pitch)
```

**描述**

设置变速变调效果节点的配置参数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| float speed | 变速参数。取值范围为[0.5, 10.0]。 |
| float pitch | 变调参数。取值范围为[0.1, 5.0]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode节点类型为非变速变调效果节点。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。例如，audioNode为空指针。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_GetTempoAndPitch()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_GetTempoAndPitch(OH_AudioNode* audioNode, float* speed, float* pitch)
```

**描述**

获取变速变调效果节点的配置参数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| float\* speed | 变速参数。取值范围为[0.5, 10.0]。 |
| float\* pitch | 变调参数。取值范围为[0.1, 5.0]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode节点类型为非变速变调效果节点。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。例如，audioNode为空指针。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_SetPureVoiceChangeOption()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_SetPureVoiceChangeOption(OH_AudioNode* audioNode, OH_AudioSuite_PureVoiceChangeOption option)
```

**描述**

设置传统变声节点的配置参数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| [OH\_AudioSuite\_PureVoiceChangeOption](capi-ohaudiosuite-oh-audiosuite-purevoicechangeoption.md) option | 传统变声效果节点的配置参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode节点类型为非传统变声效果节点。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。例如，audioNode为空指针。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_GetPureVoiceChangeOption()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_GetPureVoiceChangeOption(OH_AudioNode* audioNode, OH_AudioSuite_PureVoiceChangeOption* option)
```

**描述**

获取传统变声节点的配置参数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| [OH\_AudioSuite\_PureVoiceChangeOption](capi-ohaudiosuite-oh-audiosuite-purevoicechangeoption.md)\* option | 传统变声效果节点的配置参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode节点类型为非传统变声效果节点。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。例如，audioNode为空指针。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_SetGeneralVoiceChangeType()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_SetGeneralVoiceChangeType(OH_AudioNode* audioNode, OH_AudioSuite_GeneralVoiceChangeType type)
```

**描述**

设置通用变声节点的配置参数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| [OH\_AudioSuite\_GeneralVoiceChangeType](capi-native-audio-suite-base-h.md#oh_audiosuite_generalvoicechangetype) type | 通用变声节点的配置参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode节点类型为非通用变声效果节点。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。例如，audioNode为空指针。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuiteEngine\_GetGeneralVoiceChangeType()

```c
OH_AudioSuite_Result OH_AudioSuiteEngine_GetGeneralVoiceChangeType(OH_AudioNode* audioNode, OH_AudioSuite_GeneralVoiceChangeType* type)
```

**描述**

获取通用变声节点的配置参数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioNode](capi-ohaudiosuite-oh-audionodestruct.md)\* audioNode | 音频编创节点句柄。通过[OH\_AudioSuiteEngine\_CreateNode](capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_createnode)获取句柄。 |
| [OH\_AudioSuite\_GeneralVoiceChangeType](capi-native-audio-suite-base-h.md#oh_audiosuite_generalvoicechangetype)\* type | 通用变声节点的配置参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST：节点不存在或者当前节点已经被销毁。  AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION：audioNode节点类型为非通用变声效果节点。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数无效。例如，audioNode为空指针。  AUDIOSUITE\_ERROR\_TIMEOUT：操作处理超时。  AUDIOSUITE\_ERROR\_SYSTEM：系统发生其他异常。 |

### OH\_AudioSuite\_PrintInfo()

```c
OH_AudioSuite_Result OH_AudioSuite_PrintInfo(OH_AudioSuiteEngine* audioSuiteEngine, OH_AudioSuitePipeline* audioSuitePipeline, int fd)
```

**描述**

打印AudioSuite运行时快照。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSuiteEngine](capi-ohaudiosuite-oh-audiosuiteenginestruct.md)\* audioSuiteEngine | 指向需要显示运行时快照的AudioSuiteEngine的指针。 |
| [OH\_AudioSuitePipeline](capi-ohaudiosuite-oh-audiosuitepipelinestruct.md)\* audioSuitePipeline | 指向需要显示运行时快照的AudioSuitePipeline的指针。  如果audioSuitePipeline为空，输出所有管线（引擎下的所有管线/节点）。否则，仅输出此管线和节点的快照。 |
| int fd | 文件句柄，表示快照信息存储的位置。  如果fd小于0，快照信息存储在日志中。否则，快照将以追加模式存储在由fd句柄指向的文件中。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioSuite\_Result](capi-native-audio-suite-base-h.md#oh_audiosuite_result) | AUDIOSUITE\_SUCCESS：函数执行成功。  AUDIOSUITE\_ERROR\_INVALID\_PARAM：参数为nullptr或无效值。  AUDIOSUITE\_ERROR\_SYSTEM：系统存在其他异常。 |
