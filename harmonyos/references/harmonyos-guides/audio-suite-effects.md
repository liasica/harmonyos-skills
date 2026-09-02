---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-suite-effects
title: 音频效果(C/C++)
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频编创 > 音频效果(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0de80ac73863660abf7a7e297e24f1df998a98c0c9077880503aabb80c3919e5
---

从API版本22开始，[OHAudioSuite](../harmonyos-references/capi-ohaudiosuite.md)提供多种音频效果节点，开发者可根据业务需求选择合适的效果节点对音频进行处理。

## 效果节点类型

| 效果类型 | 节点类型 | 起始API版本 | 用途 | 说明 |
| --- | --- | --- | --- | --- |
| [均衡器](audio-suite-effects.md#均衡器) | EFFECT\_NODE\_TYPE\_EQUALIZER | API版本22 | 频段调节，改变音频频率特性。 | - |
| [降噪](audio-suite-effects.md#降噪) | EFFECT\_NODE\_TYPE\_NOISE\_REDUCTION | API版本22 | 降低背景噪声，提升语音清晰度。 | - |
| [声场](audio-suite-effects.md#声场) | EFFECT\_NODE\_TYPE\_SOUND\_FIELD | API版本22 | 调整声音空间感和声场范围。 | - |
| [音源分离](audio-suite-effects.md#音源分离) | EFFECT\_MULTII\_OUTPUT\_NODE\_TYPE\_AUDIO\_SEPARATION | API版本22 | 分离人声与伴奏（多路输出）。 | 该功能依赖NPU，创建节点前需调用[OH\_AudioSuiteEngine\_IsNodeTypeSupported()](../harmonyos-references/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_isnodetypesupported)检查是否支持该节点类型。 |
| [声音美化](audio-suite-effects.md#声音美化) | EFFECT\_NODE\_TYPE\_VOICE\_BEAUTIFIER | API版本22 | 提升音质和听感。 | - |
| [环境效果](audio-suite-effects.md#环境效果) | EFFECT\_NODE\_TYPE\_ENVIRONMENT\_EFFECT | API版本22 | 模拟不同环境的声学效果。 | - |
| [混音](audio-suite-effects.md#混音) | EFFECT\_NODE\_TYPE\_AUDIO\_MIXER | API版本22 | 多路音频混合为一路。 | - |
| [空间渲染](audio-suite-effects.md#空间渲染) | EFFECT\_NODE\_TYPE\_SPACE\_RENDER | API版本23 | 3D空间音频定位与渲染。 | - |
| [传统变声](audio-suite-effects.md#传统变声) | EFFECT\_NODE\_TYPE\_PURE\_VOICE\_CHANGE | API版本23 | 基于性别与音调的传统变声。 | - |
| [通用变声](audio-suite-effects.md#通用变声) | EFFECT\_NODE\_TYPE\_GENERAL\_VOICE\_CHANGE | API版本23 | 多种风格化变声效果。 | - |
| [变速变调](audio-suite-effects.md#变速变调) | EFFECT\_NODE\_TYPE\_TEMPO\_PITCH | API版本23 | 改变音频速度与音调。 | - |
| [HOA空间音频](audio-suite-effects.md#hoa空间音频) | EFFECT\_NODE\_TYPE\_HOA\_SPACE\_RENDER | API版本26.0.0 | HOA高阶Ambisonics转双耳渲染。 | - |

## 均衡器

均衡器效果节点[EFFECT\_NODE\_TYPE\_EQUALIZER](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audionode_type)通过调整不同频段的增益来改变音频的频率特性，实现丰富的音乐风格效果。

### 均衡器频段

均衡器效果节点支持10个频段的增益调节，每个频段可以独立设置增益值。增益值范围为[-10, 10]，单位为分贝（dB）。开发者可以使用预设效果或自定义各频段增益。

10个频段对应的频率如下表所示：

| 频段序号 | 频率  单位为赫兹（Hz） | 增益范围  单位为分贝（dB） | 音频特性 |
| --- | --- | --- | --- |
| 0 | 31 | [-10, 10] | 超低频，影响重低音效果。 |
| 1 | 62 | [-10, 10] | 低频，影响低音鼓、贝斯等。 |
| 2 | 125 | [-10, 10] | 低中频，影响男声、吉他等。 |
| 3 | 250 | [-10, 10] | 中频，影响人声、乐器主体。 |
| 4 | 500 | [-10, 10] | 中高频，影响人声清晰度。 |
| 5 | 1000 | [-10, 10] | 中高频，影响人声明亮度。 |
| 6 | 2000 | [-10, 10] | 高频，影响人声细节、乐器泛音。 |
| 7 | 4000 | [-10, 10] | 高频，影响乐器明亮度。 |
| 8 | 8000 | [-10, 10] | 高频，影响乐器高音、打击乐。 |
| 9 | 16000 | [-10, 10] | 超高频，影响空气感、细节。 |

### 预置效果类型

均衡器节点内置以下预置效果：

* [OH\_EQUALIZER\_PARAM\_DEFAULT](../harmonyos-references/capi-native-audio-suite-base-h.md#变量)：默认效果，各频段增益为{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}。
* [OH\_EQUALIZER\_PARAM\_BALLADS](../harmonyos-references/capi-native-audio-suite-base-h.md#变量)：民谣效果，各频段增益为{3, 5, 2, -4, 1, 2, -3, 1, 4, 5}。
* [OH\_EQUALIZER\_PARAM\_CHINESE\_STYLE](../harmonyos-references/capi-native-audio-suite-base-h.md#变量)：中国风效果，各频段增益为{0, 0, 2, 0, 0, 4, 4, 2, 2, 5}。
* [OH\_EQUALIZER\_PARAM\_CLASSICAL](../harmonyos-references/capi-native-audio-suite-base-h.md#变量)：古典效果，各频段增益为{2, 3, 2, 1, 0, 0, -5, -5, -5, -6}。
* [OH\_EQUALIZER\_PARAM\_DANCE\_MUSIC](../harmonyos-references/capi-native-audio-suite-base-h.md#变量)：舞曲效果，各频段增益为{4, 3, 2, -3, 0, 0, 5, 4, 2, 0}。
* [OH\_EQUALIZER\_PARAM\_JAZZ](../harmonyos-references/capi-native-audio-suite-base-h.md#变量)：爵士效果，各频段增益为{2, 0, 2, 3, 6, 5, -1, 3, 4, 4}。
* [OH\_EQUALIZER\_PARAM\_POP](../harmonyos-references/capi-native-audio-suite-base-h.md#变量)：流行效果，各频段增益为{5, 2, 1, -1, -5, -5, -2, 1, 2, 4}。
* [OH\_EQUALIZER\_PARAM\_RB](../harmonyos-references/capi-native-audio-suite-base-h.md#变量)：R&B效果，各频段增益为{1, 4, 5, 3, -2, -2, 2, 3, 5, 5}。
* [OH\_EQUALIZER\_PARAM\_ROCK](../harmonyos-references/capi-native-audio-suite-base-h.md#变量)：摇滚效果，各频段增益为{6, 4, 4, 2, 0, 1, 3, 3, 5, 4}。

### 均衡器效果节点设置方法

```c
// 设置为均衡器节点类型。
OH_AudioSuiteNodeBuilder_SetNodeType(builder, OH_AudioNode_Type::EFFECT_NODE_TYPE_EQUALIZER);
// 创建均衡器节点。
OH_AudioSuiteEngine_CreateNode(pipeline, builder, node);
// ...
// 设置均衡器节点效果。
OH_AudioSuiteEngine_SetEqualizerFrequencyBandGains(*node, gains);
```

## 降噪

降噪效果节点[EFFECT\_NODE\_TYPE\_NOISE\_REDUCTION](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audionode_type)用于降低音频中的背景噪声，提升语音的清晰度与可懂度。

### 配置说明

降噪效果节点无需额外配置参数，创建节点并接入管线后即生效。开发者可通过[OH\_AudioSuiteEngine\_BypassEffectNode](../harmonyos-references/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_bypasseffectnode)控制是否旁路（透传）该效果。

### 降噪效果节点设置方法

```c
// 设置为降噪节点类型。
OH_AudioSuiteNodeBuilder_SetNodeType(builder, OH_AudioNode_Type::EFFECT_NODE_TYPE_NOISE_REDUCTION);
// 创建降噪节点。
OH_AudioSuiteEngine_CreateNode(pipeline, builder, node);
```

## 声场

声场效果节点[EFFECT\_NODE\_TYPE\_SOUND\_FIELD](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audionode_type)通过调整声音的空间感与声场范围，营造不同的听感氛围。

### 声场类型

声场效果节点支持以下四种声场效果，通过[OH\_SoundFieldType](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_soundfieldtype)进行设置：

| 枚举值 | 名称 | 描述 |
| --- | --- | --- |
| SOUND\_FIELD\_FRONT\_FACING = 1 | 前置声场 | 声音集中于前方，营造前向聚焦听感。 |
| SOUND\_FIELD\_GRAND = 2 | 宏大声场 | 拓宽声场范围，营造宏大开阔的空间感。 |
| SOUND\_FIELD\_NEAR = 3 | 聆听声场 | 缩短听感距离，营造贴近聆听的现场感。 |
| SOUND\_FIELD\_WIDE = 4 | 宽广声场 | 扩展左右声场宽度，增强横向包围感。 |

### 声场效果节点设置方法

```c
// 设置为声场节点类型。
OH_AudioSuiteNodeBuilder_SetNodeType(builder, OH_AudioNode_Type::EFFECT_NODE_TYPE_SOUND_FIELD);
// 创建声场节点。
OH_AudioSuiteEngine_CreateNode(pipeline, builder, node);
// 设置声场节点效果。
OH_AudioSuiteEngine_SetSoundFieldType(*node, static_cast<OH_SoundFieldType>(params.soundFieldType));
```

## 音源分离

音源分离效果节点[EFFECT\_MULTII\_OUTPUT\_NODE\_TYPE\_AUDIO\_SEPARATION](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audionode_type)可将混合音频分离为人声与伴奏两路，属于多输出效果节点，每个管线中数量不超过1个。

### 配置说明

* 音源分离效果节点只能连接输出节点，不能连接其他效果节点。
* 由于是多输出节点，需通过[OH\_AudioSuiteEngine\_MultiRenderFrame](../harmonyos-references/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_multirenderframe)获取处理后的数据。audioDataArray大小要和输出数量一一对应，人声1路、伴奏1路。

### 音源分离效果节点设置方法

参考[音源分离场景](audio-suite-manual-rendering.md#音源分离场景)进行设置。

## 声音美化

声音美化效果节点[EFFECT\_NODE\_TYPE\_VOICE\_BEAUTIFIER](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audionode_type)可以提升音频的音质和听感，为用户带来更加优质的听觉体验。

### 美化类型

声音美化效果节点支持以下四种美化效果类型，通过[OH\_VoiceBeautifierType](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_voicebeautifiertype)进行设置：

| 枚举值 | 名称 | 描述 |
| --- | --- | --- |
| VOICE\_BEAUTIFIER\_TYPE\_CLEAR = 1 | 清澈效果 | 使声音更加清晰明亮，适合需要突出细节的场景。 |
| VOICE\_BEAUTIFIER\_TYPE\_THEATRE = 2 | 剧场效果 | 营造剧场般的空间感和回响效果，适合戏剧、演出等场景。 |
| VOICE\_BEAUTIFIER\_TYPE\_CD = 3 | CD效果 | 提供专业CD音质的听感，适合高品质音乐播放场景。 |
| VOICE\_BEAUTIFIER\_TYPE\_RECORDING\_STUDIO = 4 | 录音棚效果 | 录音棚效果，营造专业录音棚的声音质感，适合录音制作场景。 |

### 美化效果节点设置方法

```c
// 设置为声音美化节点类型。
OH_AudioSuiteNodeBuilder_SetNodeType(builder, OH_AudioNode_Type::EFFECT_NODE_TYPE_VOICE_BEAUTIFIER);
// 创建声音美化节点。
OH_AudioSuiteEngine_CreateNode(pipeline, builder, node);
// 设置声音美化节点效果。
OH_AudioSuiteEngine_SetVoiceBeautifierType(*node,
                                           static_cast<OH_VoiceBeautifierType>(params.voiceBeautifierType));
```

## 环境效果

环境效果节点[EFFECT\_NODE\_TYPE\_ENVIRONMENT\_EFFECT](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audionode_type)通过模拟不同声学环境的特性，使音频呈现对应场景的听感。

### 环境类型

环境效果节点支持以下四种环境效果，通过[OH\_EnvironmentType](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_environmenttype)进行设置：

| 枚举值 | 名称 | 描述 |
| --- | --- | --- |
| ENVIRONMENT\_TYPE\_BROADCAST = 1 | 广播 | 模拟广播电台的声学特性。 |
| ENVIRONMENT\_TYPE\_EARPIECE = 2 | 电话听筒 | 模拟电话听筒的窄带听感。 |
| ENVIRONMENT\_TYPE\_UNDERWATER = 3 | 水下 | 模拟水下传播的闷响效果。 |
| ENVIRONMENT\_TYPE\_GRAMOPHONE = 4 | 留声机 | 模拟老式留声机的复古音色。 |

### 环境效果节点设置方法

```c
// 设置为环境效果节点类型。
OH_AudioSuiteNodeBuilder_SetNodeType(builder, OH_AudioNode_Type::EFFECT_NODE_TYPE_ENVIRONMENT_EFFECT);
// 创建环境效果节点。
OH_AudioSuiteEngine_CreateNode(pipeline, builder, node);
// 设置环境效果节点效果。
OH_AudioSuiteEngine_SetEnvironmentType(*node, static_cast<OH_EnvironmentType>(params.environmentType));
```

## 混音

混音效果节点[EFFECT\_NODE\_TYPE\_AUDIO\_MIXER](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audionode_type)用于将多路输入音频混合为一路输出，每个管线中混音节点的数量不超过3个。

### 混音效果节点设置方法

参考[混音与级联](audio-suite-manual-rendering.md#混音与级联)进行设置。

## 空间渲染

空间渲染效果节点[EFFECT\_NODE\_TYPE\_SPACE\_RENDER](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audionode_type)用于实现3D空间音频的定位与渲染，采用左手坐标系（拇指指向x轴正方向、食指指向y轴正方向、其余手指指向z轴正方向），详细说明请参考[空间渲染(C/C++)](audio-suite-space-render.md)。

### 渲染模式

空间渲染效果节点支持三种渲染模式，分别对应三组配置参数：

**固定摆位模式**

通过[OH\_AudioSuiteEngine\_SetSpaceRenderPositionParams](../harmonyos-references/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_setspacerenderpositionparams)进行设置，参数结构体[OH\_AudioSuite\_SpaceRenderPositionParams](../harmonyos-references/capi-ohaudiosuite-oh-audiosuite-spacerenderpositionparams.md)的成员定义如下：

| 成员 | 类型 | 取值范围 | 单位 | 说明 |
| --- | --- | --- | --- | --- |
| x | float | [-5.0, 5.0] | 米（m） | 空间中的X坐标。 |
| y | float | [-5.0, 5.0] | 米（m） | 空间中的Y坐标。 |
| z | float | [-5.0, 5.0] | 米（m） | 空间中的Z坐标。 |

**旋转模式**

通过[OH\_AudioSuiteEngine\_SetSpaceRenderRotationParams](../harmonyos-references/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_setspacerenderrotationparams)进行设置，参数结构体[OH\_AudioSuite\_SpaceRenderRotationParams](../harmonyos-references/capi-ohaudiosuite-oh-audiosuite-spacerenderrotationparams.md)的成员定义如下：

| 成员 | 类型 | 取值范围 | 单位 | 说明 |
| --- | --- | --- | --- | --- |
| x | float | [-5.0, 5.0] | 米（m） | 空间中的X坐标。 |
| y | float | [-5.0, 5.0] | 米（m） | 空间中的Y坐标。 |
| z | float | [-5.0, 5.0] | 米（m） | 空间中的Z坐标。 |
| surroundTime | int32\_t | [2, 40] | 秒（s） | 单周环绕时间。 |
| surroundDirection | [OH\_AudioSuite\_SurroundDirection](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audiosuite_surrounddirection) | [0, 1] | - | 环绕方向：0=逆时针（SPACE\_RENDER\_CCW），1=顺时针（SPACE\_RENDER\_CW）。 |

**扩展模式**

通过[OH\_AudioSuiteEngine\_SetSpaceRenderExtensionParams](../harmonyos-references/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_setspacerenderextensionparams)进行设置，参数结构体[OH\_AudioSuite\_SpaceRenderExtensionParams](../harmonyos-references/capi-ohaudiosuite-oh-audiosuite-spacerenderextensionparams.md)的成员定义如下：

| 成员 | 类型 | 取值范围 | 单位 | 说明 |
| --- | --- | --- | --- | --- |
| extRadius | float | [1.0, 5.0] | 米（m） | 扩展半径。 |
| extAngle | int32\_t | (0, 360) | 度（°） | 扩展角度。 |

### 空间渲染效果节点设置方法

```c
// 设置为空间渲染节点类型。
OH_AudioSuiteNodeBuilder_SetNodeType(builder, OH_AudioNode_Type::EFFECT_NODE_TYPE_SPACE_RENDER);
// 创建空间渲染节点。
OH_AudioSuiteEngine_CreateNode(pipeline, builder, node);
// 按场景设置空间渲染参数。
switch (params.spaceRenderMode) {
    // 固定摆位模式。
    case SPACE_RENDER_MODE_POSITION: {
        OH_AudioSuite_SpaceRenderPositionParams position;
        position.x = params.spacePositionX;
        position.y = params.spacePositionY;
        position.z = params.spacePositionZ;
        OH_AudioSuiteEngine_SetSpaceRenderPositionParams(*node, position);
        break;
    }
    // 旋转模式。
    case SPACE_RENDER_MODE_ROTATION: {
        OH_AudioSuite_SpaceRenderRotationParams rotation;
        rotation.x = params.spaceRotationX;
        rotation.y = params.spaceRotationY;
        rotation.z = params.spaceRotationZ;
        rotation.surroundTime = params.spaceRotationSurroundTime;
        rotation.surroundDirection =
            static_cast<OH_AudioSuite_SurroundDirection>(params.spaceRotationSurroundDirection);
        OH_AudioSuiteEngine_SetSpaceRenderRotationParams(*node, rotation);
        break;
    }
    // 扩展模式。
    case SPACE_RENDER_MODE_EXTENSION: {
        OH_AudioSuite_SpaceRenderExtensionParams extension;
        extension.extRadius = params.spaceExtensionRadius;
        extension.extAngle = params.spaceExtensionAngle;
        OH_AudioSuiteEngine_SetSpaceRenderExtensionParams(*node, extension);
        break;
    }
    default:
        break;
}
```

## 传统变声

传统变声效果节点[EFFECT\_NODE\_TYPE\_PURE\_VOICE\_CHANGE](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audionode_type)通过指定性别、变声类型与音调实现传统变声效果。

### 配置说明

传统变声效果节点通过结构体[OH\_AudioSuite\_PureVoiceChangeOption](../harmonyos-references/capi-ohaudiosuite-oh-audiosuite-purevoicechangeoption.md)配置，包含以下成员：

| 成员 | 类型 | 说明 |
| --- | --- | --- |
| optionGender | [OH\_AudioSuite\_PureVoiceChangeGenderOption](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audiosuite_purevoicechangegenderoption) | 变声性别：1=女声（PURE\_VOICE\_CHANGE\_FEMALE），2=男声（PURE\_VOICE\_CHANGE\_MALE）。 |
| optionType | [OH\_AudioSuite\_PureVoiceChangeType](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audiosuite_purevoicechangetype) | 参考下方变声类型。 |
| pitch | float | 音调。使用系统推荐音调设为[宏定义](../harmonyos-references/capi-native-audio-suite-base-h.md#宏定义)中的OH\_PURE\_VOICE\_DEFAULT\_PITCH（0.0f）以获得最佳效果，自定义取值范围为[0.3f, 3.0f]。 |

**变声类型**

| 枚举值 | 名称 | 描述 |
| --- | --- | --- |
| PURE\_VOICE\_CHANGE\_TYPE\_CARTOON = 1 | 卡通 | 卡通风格变声。 |
| PURE\_VOICE\_CHANGE\_TYPE\_CUTE = 2 | 萝莉 | 萝莉风格变声。 |
| PURE\_VOICE\_CHANGE\_TYPE\_FEMALE = 3 | 女声 | 女声变声。 |
| PURE\_VOICE\_CHANGE\_TYPE\_MALE = 4 | 男声 | 男声变声。 |
| PURE\_VOICE\_CHANGE\_TYPE\_MONSTER = 5 | 怪兽 | 怪兽风格变声。 |
| PURE\_VOICE\_CHANGE\_TYPE\_ROBOTS = 6 | 机器人 | 机器人风格变声。 |
| PURE\_VOICE\_CHANGE\_TYPE\_SEASONED = 7 | 大叔 | 大叔风格变声。 |

### 传统变声效果节点设置方法

```c
// 设置为传统变声节点类型。
OH_AudioSuiteNodeBuilder_SetNodeType(builder, OH_AudioNode_Type::EFFECT_NODE_TYPE_PURE_VOICE_CHANGE);
// 创建传统变声节点。
OH_AudioSuiteEngine_CreateNode(pipeline, builder, node);
// 设置传统变声节点效果。
OH_AudioSuite_PureVoiceChangeOption option;
option.optionGender = static_cast<OH_AudioSuite_PureVoiceChangeGenderOption>(params.pureVoiceChangeGender);
option.optionType = static_cast<OH_AudioSuite_PureVoiceChangeType>(params.pureVoiceChangeType);
option.pitch = params.pureVoiceChangePitch;
OH_AudioSuiteEngine_SetPureVoiceChangeOption(*node, option);
```

## 通用变声

通用变声效果节点[EFFECT\_NODE\_TYPE\_GENERAL\_VOICE\_CHANGE](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audionode_type)提供多种风格化的变声效果，适用场景更丰富。

### 变声类型

通用变声效果节点支持以下十种变声类型，通过[OH\_AudioSuite\_GeneralVoiceChangeType](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audiosuite_generalvoicechangetype)进行设置：

| 枚举值 | 名称 | 描述 |
| --- | --- | --- |
| GENERAL\_VOICE\_CHANGE\_TYPE\_CUTE = 1 | 萝莉 | 萝莉风格变声。 |
| GENERAL\_VOICE\_CHANGE\_TYPE\_CYBERPUNK = 2 | 赛博朋克 | 赛博朋克风格变声。 |
| GENERAL\_VOICE\_CHANGE\_TYPE\_FEMALE = 3 | 女声 | 女声变声。 |
| GENERAL\_VOICE\_CHANGE\_TYPE\_MALE = 4 | 男声 | 男声变声。 |
| GENERAL\_VOICE\_CHANGE\_TYPE\_MIX = 5 | 混响 | 混响风格变声。 |
| GENERAL\_VOICE\_CHANGE\_TYPE\_MONSTER = 6 | 怪兽 | 怪兽风格变声。 |
| GENERAL\_VOICE\_CHANGE\_TYPE\_SEASONED = 7 | 大叔 | 大叔风格变声。 |
| GENERAL\_VOICE\_CHANGE\_TYPE\_SYNTH = 8 | 合成器 | 合成器风格变声。 |
| GENERAL\_VOICE\_CHANGE\_TYPE\_TRILL = 9 | 颤音 | 颤音风格变声。 |
| GENERAL\_VOICE\_CHANGE\_TYPE\_WAR = 10 | 战争 | 战争风格变声。 |

### 通用变声效果节点设置方法

```c
// 设置为通用变声节点类型。
OH_AudioSuiteNodeBuilder_SetNodeType(builder, OH_AudioNode_Type::EFFECT_NODE_TYPE_GENERAL_VOICE_CHANGE);
// 创建通用变声节点。
OH_AudioSuiteEngine_CreateNode(pipeline, builder, node);
// 设置通用变声节点效果。
OH_AudioSuiteEngine_SetGeneralVoiceChangeType(
    *node, static_cast<OH_AudioSuite_GeneralVoiceChangeType>(params.generalVoiceChangeType));
```

## 变速变调

变速变调效果节点[EFFECT\_NODE\_TYPE\_TEMPO\_PITCH](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audionode_type)用于独立或同时改变音频的播放速度与音调。

### 配置说明

通过[OH\_AudioSuiteEngine\_SetTempoAndPitch](../harmonyos-references/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_settempoandpitch)设置，参数说明如下：

| 参数 | 类型 | 取值范围 | 说明 |
| --- | --- | --- | --- |
| speed | float | [0.5, 10.0] | 变速参数。1.0为原始速度，小于1.0减速，大于1.0加速。 |
| pitch | float | [0.1, 5.0] | 变调参数。1.0为原始音调，小于1.0降调，大于1.0升调。 |

### 变速变调效果节点设置方法

```c
// 设置为变速变调节点类型。
OH_AudioSuiteNodeBuilder_SetNodeType(builder, OH_AudioNode_Type::EFFECT_NODE_TYPE_TEMPO_PITCH);
// 创建变速变调节点。
OH_AudioSuiteEngine_CreateNode(pipeline, builder, node);
// 设置变速变调节点效果。
OH_AudioSuiteEngine_SetTempoAndPitch(*node, params.tempoSpeed, params.tempoPitch);
```

## HOA空间音频

HOA（High-Order Ambisonics）转双耳空间音频节点[EFFECT\_NODE\_TYPE\_HOA\_SPACE\_RENDER](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audionode_type)用于将HOA格式的空间音频转换为双耳（Binaural）立体声输出。

### 输入音频格式

该节点的前置节点必须为HOA格式的输入节点，输入音频格式要求如下：

* 采样率：[OH\_Audio\_SampleRate](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_samplerate).SAMPLE\_RATE\_16000 或 SAMPLE\_RATE\_48000。
* 采样格式：[OH\_Audio\_SampleFormat](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_sampleformat)。
* 声道布局：支持1阶至3阶HOA，取值如下：
  + [OH\_AudioChannelLayout](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_AMB\_ORDER1\_ACN\_N3D。
  + [OH\_AudioChannelLayout](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_AMB\_ORDER1\_ACN\_SN3D。
  + [OH\_AudioChannelLayout](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_AMB\_ORDER1\_FUMA。
  + [OH\_AudioChannelLayout](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_AMB\_ORDER2\_ACN\_N3D。
  + [OH\_AudioChannelLayout](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_AMB\_ORDER2\_ACN\_SN3D。
  + [OH\_AudioChannelLayout](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_AMB\_ORDER2\_FUMA。
  + [OH\_AudioChannelLayout](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_AMB\_ORDER3\_ACN\_N3D。
  + [OH\_AudioChannelLayout](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_AMB\_ORDER3\_ACN\_SN3D。
  + [OH\_AudioChannelLayout](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_AMB\_ORDER3\_FUMA。

### 配置说明

* 该节点的前置节点必须连接音频格式为HOA的输入节点。
* 如果节点未正确连接，在调用[OH\_AudioSuiteEngine\_StartPipeline](../harmonyos-references/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_startpipeline)接口时将会报错。
* 该节点无需额外配置参数，创建并正确连接后即会生效。
