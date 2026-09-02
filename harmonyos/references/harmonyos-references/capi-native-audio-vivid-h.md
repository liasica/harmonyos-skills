---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-vivid-h
title: native_audio_vivid.h
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 头文件 > native_audio_vivid.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:91be76c132f5afe8d6ef7d15e48dfedeaf73e4aba6f580ee634485106226c6f6
---

## 概述

声明Audio Vivid相关的函数和枚举。

**引用文件：** <multimedia/player\_framework/native\_audio\_vivid.h>

**库：** libnative\_media\_core.so

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 26.0.0

**相关模块：** [Core](capi-core.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_CartesianPosition](capi-core-oh-cartesianposition.md) | OH\_CartesianPosition | 表示对象声源在笛卡尔坐标系（Cartesian coordinate system）中的位置。笛卡尔坐标系使用x、y、z轴定义三维空间中的位置。 |
| [OH\_PolarPosition](capi-core-oh-polarposition.md) | OH\_PolarPosition | 表示极坐标系（polar coordinate system，也叫球坐标系）中的位置。极坐标系使用方位角、俯仰角和距离定义对象声源在三维空间中的位置。 |
| [OH\_AudioObjectPosition](capi-core-oh-audioobjectposition.md) | OH\_AudioObjectPosition | 表示音频对象声源在三维空间中的位置。该位置可以用笛卡尔坐标或极坐标表示。 |
| [OH\_AudioVividMetaBuilderStruct](capi-core-oh-audiovividmetabuilderstruct.md) | OH\_AudioVividMetaBuilder | OH\_AudioVividMetaBuilder的前向声明。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioVividSignalFormat](capi-native-audio-vivid-h.md#oh_audiovividsignalformat) | OH\_AudioVividSignalFormat | Audio Vivid编码器信号格式枚举。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_AVErrCode OH\_AudioVividMetaBuilder\_Create(OH\_AudioVividMetaBuilder \*\*builder, const OH\_AVFormat \*format)](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_create) | 创建Audio Vivid元数据构建器。 |
| [OH\_AVErrCode OH\_AudioVividMetaBuilder\_UpdateObjectPos(OH\_AudioVividMetaBuilder \*builder, int32\_t objectIndex, OH\_AudioObjectPosition pos)](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_updateobjectpos) | 更新Audio Vivid信号格式为[OH\_AudioVividSignalFormat](capi-native-audio-vivid-h.md#oh_audiovividsignalformat).OH\_AUDIO\_VIVID\_SIGNAL\_FORMAT\_MIX时的音频对象位置。在此信号格式下，输入编码的PCM（Pulse Code Modulation）数据中，声道排列顺序为：声床声道在前，对象声道在后。  对象声道按顺序与objectIndex对应，从0开始编号。 |
| [OH\_AVErrCode OH\_AudioVividMetaBuilder\_UpdateObjectGain(OH\_AudioVividMetaBuilder \*builder, int32\_t objectIndex, float gain)](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_updateobjectgain) | 更新Audio Vivid信号格式为[OH\_AudioVividSignalFormat](capi-native-audio-vivid-h.md#oh_audiovividsignalformat).OH\_AUDIO\_VIVID\_SIGNAL\_FORMAT\_MIX时的音频对象渲染的线性增益。 |
| [OH\_AVErrCode OH\_AudioVividMetaBuilder\_GetMetaLen(const OH\_AudioVividMetaBuilder \*builder, bool withStaticMeta, int32\_t \*len)](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_getmetalen) | 获取元数据长度。 |
| [OH\_AVErrCode OH\_AudioVividMetaBuilder\_GetMeta(const OH\_AudioVividMetaBuilder \*builder, bool withStaticMeta, uint8\_t \*buffer, int32\_t len)](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_getmeta) | 获取元数据缓冲区。 |
| [OH\_AVErrCode OH\_AudioVividMetaBuilder\_Destroy(OH\_AudioVividMetaBuilder \*builder)](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_destroy) | 销毁Audio Vivid元数据构建器并释放资源。 |
| [OH\_AVErrCode OH\_AudioVividMetaBuilder\_CreateEmptyBuilder(OH\_AudioVividMetaBuilder \*\*builder)](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_createemptybuilder) | 创建一个空的Audio Vivid元数据构建器。该函数用于合并Audio Vivid元数据的场景。在创建一个空的元数据构造器后，用户可以通过调用[OH\_AudioVividMetaBuilder\_UpdateBaseMeta](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_updatebasemeta)接口来增加、修改或者删除音频对象。 |
| [OH\_AVErrCode OH\_AudioVividMetaBuilder\_UpdateBaseMeta(OH\_AudioVividMetaBuilder \*builder, const uint8\_t \*buffer, int32\_t len)](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_updatebasemeta) | 更新Audio Vivid元数据构造器的基础元数据。buffer需要包含完整的Audio Vivid元数据。构造器会将元数据里的音频声床和音频对象信息保留下来。 |
| [OH\_AVErrCode OH\_AudioVividMetaBuilder\_AddObject(OH\_AudioVividMetaBuilder \*builder, int32\_t \*objectIndex)](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_addobject) | Audio Vivid元数据构造器内添加一个音频对象。添加音频对象后，可以通过[OH\_AudioVividMetaBuilder\_UpdateObjectPos](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_updateobjectpos)和[OH\_AudioVividMetaBuilder\_UpdateObjectGain](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_updateobjectgain)接口，更新该对象的位置和对象渲染的线性增益。 |
| [OH\_AVErrCode OH\_AudioVividMetaBuilder\_RemoveObject(OH\_AudioVividMetaBuilder \*builder, int32\_t objectIndex)](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_removeobject) | 从Audio Vivid元数据构造器内删除一个音频对象。只有通过[OH\_AudioVividMetaBuilder\_AddObject](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_addobject)函数新增的音频对象可以被删除。通过[OH\_AudioVividMetaBuilder\_UpdateBaseMeta](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_updatebasemeta)函数新增的音频对象无法删除。删除音频对象后，其他音频对象的索引保持不变。 |

## 枚举类型说明

### OH\_AudioVividSignalFormat

```c
enum OH_AudioVividSignalFormat
```

**描述**

Audio Vivid编码器信号格式枚举。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| OH\_AUDIO\_VIVID\_SIGNAL\_FORMAT\_MONO = 0 | Audio Vivid信号格式为单声道，编码器接收单声道数据，内部标记声道布局为[OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_MONO。 |
| OH\_AUDIO\_VIVID\_SIGNAL\_FORMAT\_STEREO = 1 | Audio Vivid信号格式为立体声，编码器接收双声道数据，内部标记声道布局为[OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_STEREO。 |
| OH\_AUDIO\_VIVID\_SIGNAL\_FORMAT\_MC = 2 | Audio Vivid信号格式为多声道，编码器支持声道布局[OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_5POINT1、[OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_5POINT1POINT2、[OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_5POINT1POINT4、[OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_7POINT1、[OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_7POINT1POINT2、[OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_7POINT1POINT4。 |
| OH\_AUDIO\_VIVID\_SIGNAL\_FORMAT\_MIX = 4 | Audio Vivid信号格式为混合模式，包含声床（Bed）和对象（object）。声床的声道布局支持[OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_STEREO、[OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_5POINT1、[OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_5POINT1POINT2、[OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_5POINT1POINT4、[OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_7POINT1、[OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_7POINT1POINT2、[OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout).CH\_LAYOUT\_7POINT1POINT4。 |

## 函数说明

### OH\_AudioVividMetaBuilder\_Create()

```c
OH_AVErrCode OH_AudioVividMetaBuilder_Create(OH_AudioVividMetaBuilder **builder, const OH_AVFormat *format)
```

**描述**

创建Audio Vivid元数据构建器。

**说明** 

生命周期管理：

* 通过本函数创建的实例不再使用时，必须调用[OH\_AudioVividMetaBuilder\_Destroy](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_destroy)手动释放，以避免内存泄漏。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioVividMetaBuilder](capi-core-oh-audiovividmetabuilderstruct.md) \*\*builder | 输出参数，用于获取OH\_AudioVividMetaBuilder实例指针的指针。 |
| [const OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向包含音频格式信息的OH\_AVFormat指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数builder或format为空指针或无效。  AV\_ERR\_UNSUPPORT：当前设备不支持此功能。  AV\_ERR\_UNKNOWN：创建构建器失败，属于未知错误，请查看日志获取详细信息。 |

### OH\_AudioVividMetaBuilder\_UpdateObjectPos()

```c
OH_AVErrCode OH_AudioVividMetaBuilder_UpdateObjectPos(OH_AudioVividMetaBuilder *builder, int32_t objectIndex, OH_AudioObjectPosition pos)
```

**描述**

更新Audio Vivid信号格式为[OH\_AudioVividSignalFormat](capi-native-audio-vivid-h.md#oh_audiovividsignalformat).OH\_AUDIO\_VIVID\_SIGNAL\_FORMAT\_MIX时的音频对象位置。在此信号格式下，输入编码的PCM（Pulse Code Modulation）数据中，声道排列顺序为：声床声道在前，对象声道在后。

对象声道按顺序与objectIndex对应，从0开始编号。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioVividMetaBuilder](capi-core-oh-audiovividmetabuilderstruct.md) \*builder | 指向OH\_AudioVividMetaBuilder的指针。 |
| int32\_t objectIndex | 要更新的音频对象索引，从0开始，小于在[OH\_AudioVividMetaBuilder\_Create](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_create)创建builder时入参format设置的[OH\_MD\_KEY\_AUDIO\_OBJECT\_NUMBER](capi-codecbase.md#音频专有的键值对)对应的值。 |
| [OH\_AudioObjectPosition](capi-core-oh-audioobjectposition.md) pos | 音频对象声源的新位置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数builder为空指针或无效，objectIndex或pos无效。 |

### OH\_AudioVividMetaBuilder\_UpdateObjectGain()

```c
OH_AVErrCode OH_AudioVividMetaBuilder_UpdateObjectGain(OH_AudioVividMetaBuilder *builder, int32_t objectIndex, float gain)
```

**描述**

更新Audio Vivid信号格式为[OH\_AudioVividSignalFormat](capi-native-audio-vivid-h.md#oh_audiovividsignalformat).OH\_AUDIO\_VIVID\_SIGNAL\_FORMAT\_MIX时的音频对象渲染的线性增益。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioVividMetaBuilder](capi-core-oh-audiovividmetabuilderstruct.md) \*builder | 指向OH\_AudioVividMetaBuilder的指针。 |
| int32\_t objectIndex | 要更新的音频对象索引，从0开始，小于在[OH\_AudioVividMetaBuilder\_Create](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_create)创建builder时入参format设置的[OH\_MD\_KEY\_AUDIO\_OBJECT\_NUMBER](capi-codecbase.md#音频专有的键值对)对应的值。 |
| float gain | 对象渲染时应用的线性增益值，范围为[0.0, 6.0]，线性增益0.0为静音，1.0为不变。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数builder为空指针或无效，objectIndex或gain无效。 |

### OH\_AudioVividMetaBuilder\_GetMetaLen()

```c
OH_AVErrCode OH_AudioVividMetaBuilder_GetMetaLen(const OH_AudioVividMetaBuilder *builder, bool withStaticMeta, int32_t *len)
```

**描述**

获取元数据长度。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AudioVividMetaBuilder](capi-core-oh-audiovividmetabuilderstruct.md) \*builder | 指向OH\_AudioVividMetaBuilder的指针。 |
| bool withStaticMeta | 设置输出的长度是否包含静态元数据。true表示输出长度包含静态元数据；false表示输出长度仅包含动态元数据。 |
| int32\_t \*len | 用于接收元数据长度的指针。单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数builder为空指针或无效，len为空指针。 |

### OH\_AudioVividMetaBuilder\_GetMeta()

```c
OH_AVErrCode OH_AudioVividMetaBuilder_GetMeta(const OH_AudioVividMetaBuilder *builder, bool withStaticMeta, uint8_t *buffer, int32_t len)
```

**描述**

获取元数据缓冲区。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AudioVividMetaBuilder](capi-core-oh-audiovividmetabuilderstruct.md) \*builder | 指向OH\_AudioVividMetaBuilder的指针。 |
| bool withStaticMeta | 设置输出的长度是否包含静态元数据。true表示输出缓冲区包含静态元数据；false表示输出缓冲区仅包含动态元数据。 |
| uint8\_t \*buffer | 用于接收元数据内容的缓冲区指针。 |
| int32\_t len | 缓冲区长度。单位为字节。该值需不小于待获取的元数据长度，可通过[OH\_AudioVividMetaBuilder\_GetMetaLen](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_getmetalen)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：builder为空指针或无效，buffer为空指针或len不足。 |

### OH\_AudioVividMetaBuilder\_Destroy()

```c
OH_AVErrCode OH_AudioVividMetaBuilder_Destroy(OH_AudioVividMetaBuilder *builder)
```

**描述**

销毁Audio Vivid元数据构建器并释放资源。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioVividMetaBuilder](capi-core-oh-audiovividmetabuilderstruct.md) \*builder | 指向待销毁的OH\_AudioVividMetaBuilder的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数builder为空指针。 |

### OH\_AudioVividMetaBuilder\_CreateEmptyBuilder()

```c
OH_AVErrCode OH_AudioVividMetaBuilder_CreateEmptyBuilder(OH_AudioVividMetaBuilder **builder)
```

**描述**

创建一个空的Audio Vivid元数据构建器。该函数用于合并Audio Vivid元数据的场景。在创建一个空的元数据构造器后，用户可以通过调用[OH\_AudioVividMetaBuilder\_UpdateBaseMeta](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_updatebasemeta)接口来增加、修改或者删除音频对象。

**说明** 

生命周期管理：

* 通过本函数创建的实例不再使用时，必须调用[OH\_AudioVividMetaBuilder\_Destroy](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_destroy)手动释放，以避免内存泄漏。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioVividMetaBuilder](capi-core-oh-audiovividmetabuilderstruct.md) \*\*builder | 输出参数，用于获取OH\_AudioVividMetaBuilder实例指针的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | * AV\_ERR\_OK：执行成功。  * AV\_ERR\_INVALID\_VAL：参数builder为空指针或无效。  * AV\_ERR\_UNSUPPORT：当前设备不支持此功能。  * AV\_ERR\_UNKNOWN：创建构建器失败，属于未知错误，请查看日志获取详细信息。 |

### OH\_AudioVividMetaBuilder\_UpdateBaseMeta()

```c
OH_AVErrCode OH_AudioVividMetaBuilder_UpdateBaseMeta(OH_AudioVividMetaBuilder *builder, const uint8_t *buffer, int32_t len)
```

**描述**

更新Audio Vivid元数据构造器的基础元数据。buffer需要包含完整的Audio Vivid元数据。构造器会将元数据里的音频声床和音频对象信息保留下来。

**说明** 

约束条件：

* 基础元数据内音频的声床声道数 + 对象数必须小于等于16个。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioVividMetaBuilder](capi-core-oh-audiovividmetabuilderstruct.md) \*builder | 指向OH\_AudioVividMetaBuilder的指针。 |
| const uint8\_t \*buffer | 指向包含基础元数据的指针。 |
| int32\_t len | 缓冲区长度。单位为字节（Byte）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | * AV\_ERR\_OK：执行成功。  * AV\_ERR\_INVALID\_VAL：参数builder、format为空指针或无效。 |

### OH\_AudioVividMetaBuilder\_AddObject()

```c
OH_AVErrCode OH_AudioVividMetaBuilder_AddObject(OH_AudioVividMetaBuilder *builder, int32_t *objectIndex)
```

**描述**

Audio Vivid元数据构造器内添加一个音频对象。添加音频对象后，可以通过[OH\_AudioVividMetaBuilder\_UpdateObjectPos](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_updateobjectpos)和[OH\_AudioVividMetaBuilder\_UpdateObjectGain](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_updateobjectgain)接口，更新该对象的位置和对象渲染的线性增益。

**说明** 

约束条件：

* 音频的声床声道数 + 对象数必须小于等于16个。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioVividMetaBuilder](capi-core-oh-audiovividmetabuilderstruct.md) \*builder | 指向OH\_AudioVividMetaBuilder的指针。 |
| int32\_t \*objectIndex | 输出参数，用于输出新增对象的索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | * AV\_ERR\_OK：执行成功。  * AV\_ERR\_INVALID\_VAL：参数builder、objectIndex为空指针或无效。  * AV\_ERR\_UNKNOWN：添加对象失败，属于未知错误，请查看日志获取详细信息。 |

### OH\_AudioVividMetaBuilder\_RemoveObject()

```c
OH_AVErrCode OH_AudioVividMetaBuilder_RemoveObject(OH_AudioVividMetaBuilder *builder, int32_t objectIndex)
```

**描述**

从Audio Vivid元数据构造器内删除一个音频对象。只有通过[OH\_AudioVividMetaBuilder\_AddObject](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_addobject)函数新增的音频对象可以被删除。通过[OH\_AudioVividMetaBuilder\_UpdateBaseMeta](capi-native-audio-vivid-h.md#oh_audiovividmetabuilder_updatebasemeta)函数新增的音频对象无法删除。删除音频对象后，其他音频对象的索引保持不变。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioVividMetaBuilder](capi-core-oh-audiovividmetabuilderstruct.md) \*builder | 指向OH\_AudioVividMetaBuilder的指针。 |
| int32\_t objectIndex | 要移除的音频对象的索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | * AV\_ERR\_OK：执行成功。  * AV\_ERR\_INVALID\_VAL：  * 1. 参数builder为空指针或无效；  * 2. 参数objectIndex无效。 |
