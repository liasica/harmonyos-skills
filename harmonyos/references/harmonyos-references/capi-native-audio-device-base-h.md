---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-device-base-h
title: native_audio_device_base.h
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 头文件 > native_audio_device_base.h
category: harmonyos-references
scraped_at: 2026-04-28T08:11:48+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b1d3365c87f8f385c58e3a0550c755eb3770a5b3c98c1de228b6aa79fc210d4c
---

## 概述

PhonePC/2in1TabletTVWearable

定义音频设备参数的类型以及获取每个设备参数的接口。

**库：** libohaudio.so

**引用文件：** <ohaudio/native\_audio\_device\_base.h>

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 12

**相关模块：** [OHAudio](capi-ohaudio.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md) | OH\_AudioDeviceDescriptorArray | 声明音频设备描述符数组。 |
| [OH\_AudioDeviceDescriptor](capi-ohaudio-oh-audiodevicedescriptor.md) | OH\_AudioDeviceDescriptor | 声明音频设备描述符。该实例用于获取更多音频设备详细信息属性。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioDevice\_ChangeType](capi-native-audio-device-base-h.md#oh_audiodevice_changetype) | OH\_AudioDevice\_ChangeType | 定义音频设备更改类型。 |
| [OH\_AudioDevice\_Role](capi-native-audio-device-base-h.md#oh_audiodevice_role) | OH\_AudioDevice\_Role | 定义音频设备角色。 |
| [OH\_AudioDevice\_Type](capi-native-audio-device-base-h.md#oh_audiodevice_type) | OH\_AudioDevice\_Type | 定义音频设备类型。 |
| [OH\_AudioDevice\_Flag](capi-native-audio-device-base-h.md#oh_audiodevice_flag) | OH\_AudioDevice\_Flag | 定义音频设备标志。 |
| [OH\_AudioDevice\_Usage](capi-native-audio-device-base-h.md#oh_audiodevice_usage) | OH\_AudioDevice\_Usage | 定义可获取的设备种类。 |
| [OH\_AudioDevice\_BlockStatus](capi-native-audio-device-base-h.md#oh_audiodevice_blockstatus) | OH\_AudioDevice\_BlockStatus | 声明音频设备的堵塞状态。默认情况下，音频设备被视为未堵塞。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceRole(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor, OH\_AudioDevice\_Role \*deviceRole)](capi-native-audio-device-base-h.md#oh_audiodevicedescriptor_getdevicerole) | 查询目标音频设备描述符的设备角色。 |
| [OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceType(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor, OH\_AudioDevice\_Type \*deviceType)](capi-native-audio-device-base-h.md#oh_audiodevicedescriptor_getdevicetype) | 查询目标音频设备描述符的设备类型。 |
| [OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceId(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor, uint32\_t \*id)](capi-native-audio-device-base-h.md#oh_audiodevicedescriptor_getdeviceid) | 查询目标音频设备描述符的设备id。 |
| [OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceName(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor, char \*\*name)](capi-native-audio-device-base-h.md#oh_audiodevicedescriptor_getdevicename) | 查询目标音频设备描述符的设备名称。 |
| [OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceAddress(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor, char \*\*address)](capi-native-audio-device-base-h.md#oh_audiodevicedescriptor_getdeviceaddress) | 查询目标音频设备描述符的设备地址。 |
| [OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceSampleRates(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor, uint32\_t \*\*sampleRates, uint32\_t \*size)](capi-native-audio-device-base-h.md#oh_audiodevicedescriptor_getdevicesamplerates) | 查询目标音频设备描述符的采样率数组。 |
| [OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceChannelCounts(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor, uint32\_t \*\*channelCounts, uint32\_t \*size)](capi-native-audio-device-base-h.md#oh_audiodevicedescriptor_getdevicechannelcounts) | 查询目标音频设备描述符的设备通道计数数组。 |
| [OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceDisplayName(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor, char \*\*displayName)](capi-native-audio-device-base-h.md#oh_audiodevicedescriptor_getdevicedisplayname) | 查询目标音频设备描述符的显示名称。 |
| [OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceEncodingTypes(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor, OH\_AudioStream\_EncodingType \*\*encodingTypes, uint32\_t \*size)](capi-native-audio-device-base-h.md#oh_audiodevicedescriptor_getdeviceencodingtypes) | 查询目标音频设备描述符的编码类型数组。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_AudioDevice\_ChangeType

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioDevice_ChangeType
```

**描述**

定义音频设备更改类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| AUDIO\_DEVICE\_CHANGE\_TYPE\_CONNECT = 0 | 设备连接。 |
| AUDIO\_DEVICE\_CHANGE\_TYPE\_DISCONNECT = 1 | 设备断开。 |

### OH\_AudioDevice\_Role

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioDevice_Role
```

**描述**

定义音频设备角色。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| AUDIO\_DEVICE\_ROLE\_INPUT = 1 | 输入设备。 |
| AUDIO\_DEVICE\_ROLE\_OUTPUT = 2 | 输出设备。 |

### OH\_AudioDevice\_Type

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioDevice_Type
```

**描述**

定义音频设备类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| AUDIO\_DEVICE\_TYPE\_INVALID = 0 | 无效设备。 |
| AUDIO\_DEVICE\_TYPE\_EARPIECE = 1 | 内置听筒。 |
| AUDIO\_DEVICE\_TYPE\_SPEAKER = 2 | 内置扬声器。 |
| AUDIO\_DEVICE\_TYPE\_WIRED\_HEADSET = 3 | 带话筒的耳机。 |
| AUDIO\_DEVICE\_TYPE\_WIRED\_HEADPHONES = 4 | 无话筒的耳机。 |
| AUDIO\_DEVICE\_TYPE\_BLUETOOTH\_SCO = 7 | 使用面向同步连接链路（SCO）的蓝牙设备。 |
| AUDIO\_DEVICE\_TYPE\_BLUETOOTH\_A2DP = 8 | 使用高级音频分布模式（A2DP）的蓝牙设备。 |
| AUDIO\_DEVICE\_TYPE\_MIC = 15 | 内置麦克风。 |
| AUDIO\_DEVICE\_TYPE\_USB\_HEADSET = 22 | USB音频耳机。 |
| AUDIO\_DEVICE\_TYPE\_DISPLAY\_PORT = 23 | 显示端口（DisplayPort）设备。 |
| AUDIO\_DEVICE\_TYPE\_REMOTE\_CAST = 24 | 音频被系统应用投送到其他远程的设备。 |
| AUDIO\_DEVICE\_TYPE\_USB\_DEVICE = 25 | USB设备（不包含USB耳机）。  **起始版本：** 18 |
| AUDIO\_DEVICE\_TYPE\_ACCESSORY = 26 | 附件设备，如遥控器上的麦克风。  **起始版本：** 19 |
| AUDIO\_DEVICE\_TYPE\_HDMI = 27 | HDMI设备（例如HDMI、ARC、eARC等）。  **起始版本：** 19 |
| AUDIO\_DEVICE\_TYPE\_LINE\_DIGITAL = 28 | 有线数字设备（例如S/PDIF等）。  **起始版本：** 19 |
| AUDIO\_DEVICE\_TYPE\_HEARING\_AID = 30 | 助听器设备。  **起始版本：** 20 |
| AUDIO\_DEVICE\_TYPE\_NEARLINK = 31 | 星闪设备。  **起始版本：** 20 |
| AUDIO\_DEVICE\_TYPE\_DEFAULT = 1000 | 默认设备类型。 |

### OH\_AudioDevice\_Flag

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioDevice_Flag
```

**描述**

定义音频设备标志。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| AUDIO\_DEVICE\_FLAG\_NONE = 0 | 无设备。 |
| AUDIO\_DEVICE\_FLAG\_OUTPUT = 1 | 输出设备。 |
| AUDIO\_DEVICE\_FLAG\_INPUT = 2 | 输入设备。 |
| AUDIO\_DEVICE\_FLAG\_ALL = 3 | 所有设备。 |

### OH\_AudioDevice\_Usage

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioDevice_Usage
```

**描述**

定义可获取的设备种类。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| AUDIO\_DEVICE\_USAGE\_MEDIA\_OUTPUT = 1 | 媒体输出设备。 |
| AUDIO\_DEVICE\_USAGE\_MEDIA\_INPUT = 2 | 媒体输入设备。 |
| AUDIO\_DEVICE\_USAGE\_MEDIA\_ALL = 3 | 所有媒体设备。 |
| AUDIO\_DEVICE\_USAGE\_CALL\_OUTPUT = 4 | 通话输出设备。 |
| AUDIO\_DEVICE\_USAGE\_CALL\_INPUT = 8 | 通话输入设备。 |
| AUDIO\_DEVICE\_USAGE\_CALL\_ALL = 12 | 所有通话设备。 |

### OH\_AudioDevice\_BlockStatus

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioDevice_BlockStatus
```

**描述**

声明音频设备的堵塞状态。默认情况下，音频设备被视为未堵塞。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| AUDIO\_DEVICE\_UNBLOCKED = 0 | 音频设备未被堵塞。 |
| AUDIO\_DEVICE\_BLOCKED = 1 | 音频设备被堵塞。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AudioDeviceDescriptor\_GetDeviceRole()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceRole(OH_AudioDeviceDescriptor *audioDeviceDescriptor,OH_AudioDevice_Role *deviceRole)
```

**描述**

查询目标音频设备描述符的设备角色。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDeviceDescriptor](capi-ohaudio-oh-audiodevicedescriptor.md) \*audioDeviceDescriptor | 音频设备描述符。通过 [OH\_AudioRoutingManager\_GetDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_getdevices) 或者[OH\_AudioRoutingManager\_OnDeviceChangedCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ondevicechangedcallback)获取。 |
| [OH\_AudioDevice\_Role](capi-native-audio-device-base-h.md#oh_audiodevice_role) \*deviceRole | 设备角色指针。将设置设备角色值的变量，指向[OH\_AudioDevice\_Role](capi-native-audio-device-base-h.md#oh_audiodevice_role)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS或AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM。 |

### OH\_AudioDeviceDescriptor\_GetDeviceType()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceType(OH_AudioDeviceDescriptor *audioDeviceDescriptor,OH_AudioDevice_Type *deviceType)
```

**描述**

查询目标音频设备描述符的设备类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDeviceDescriptor](capi-ohaudio-oh-audiodevicedescriptor.md) \*audioDeviceDescriptor | 音频设备描述符。通过 [OH\_AudioRoutingManager\_GetDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_getdevices) 或者[OH\_AudioRoutingManager\_OnDeviceChangedCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ondevicechangedcallback)获取。 |
| [OH\_AudioDevice\_Type](capi-native-audio-device-base-h.md#oh_audiodevice_type) \*deviceType | 设备类型指针。将设置设备类型值的变量，指向[OH\_AudioDevice\_Type](capi-native-audio-device-base-h.md#oh_audiodevice_type)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS或AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM。 |

### OH\_AudioDeviceDescriptor\_GetDeviceId()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceId(OH_AudioDeviceDescriptor *audioDeviceDescriptor,uint32_t *id)
```

**描述**

查询目标音频设备描述符的设备id。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDeviceDescriptor](capi-ohaudio-oh-audiodevicedescriptor.md) \*audioDeviceDescriptor | 音频设备描述符。通过 [OH\_AudioRoutingManager\_GetDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_getdevices) 或者[OH\_AudioRoutingManager\_OnDeviceChangedCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ondevicechangedcallback)获取。 |
| uint32\_t \*id | 设备id指针，将设置设备角色值的变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS 或 AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM。 |

### OH\_AudioDeviceDescriptor\_GetDeviceName()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceName(OH_AudioDeviceDescriptor *audioDeviceDescriptor,char **name)
```

**描述**

查询目标音频设备描述符的设备名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDeviceDescriptor](capi-ohaudio-oh-audiodevicedescriptor.md) \*audioDeviceDescriptor | 音频设备描述符。通过 [OH\_AudioRoutingManager\_GetDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_getdevices) 或者[OH\_AudioRoutingManager\_OnDeviceChangedCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ondevicechangedcallback)获取。 |
| char \*\*name | 设备名称指针，将设置设备名称值的变量。  不要单独释放音频设备名称指针，而是调用[OH\_AudioRoutingManager\_ReleaseDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_releasedevices)，以便在不再使用时释放所有DeviceDescriptor数组。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS或AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM。 |

### OH\_AudioDeviceDescriptor\_GetDeviceAddress()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceAddress(OH_AudioDeviceDescriptor *audioDeviceDescriptor,char **address)
```

**描述**

查询目标音频设备描述符的设备地址。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDeviceDescriptor](capi-ohaudio-oh-audiodevicedescriptor.md) \*audioDeviceDescriptor | 音频设备描述符。通过 [OH\_AudioRoutingManager\_GetDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_getdevices) 或者[OH\_AudioRoutingManager\_OnDeviceChangedCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ondevicechangedcallback)获取。 |
| char \*\*address | 设备MAC地址指针，将设置设备MAC地址值的变量。  不要单独释放音频设备MAC地址指针，而是调用[OH\_AudioRoutingManager\_ReleaseDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_releasedevices)，以便在不再使用时释放所有DeviceDescriptor数组。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS或AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM。 |

### OH\_AudioDeviceDescriptor\_GetDeviceSampleRates()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceSampleRates(OH_AudioDeviceDescriptor *audioDeviceDescriptor,uint32_t **sampleRates, uint32_t *size)
```

**描述**

查询目标音频设备描述符的采样率数组。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDeviceDescriptor](capi-ohaudio-oh-audiodevicedescriptor.md) \*audioDeviceDescriptor | 音频设备描述符。通过 [OH\_AudioRoutingManager\_GetDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_getdevices) 或者[OH\_AudioRoutingManager\_OnDeviceChangedCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ondevicechangedcallback)获取。 |
| uint32\_t \*\*sampleRates | 设置采样率数组值的数组指针变量。  不要单独释放音频设备采样率指针，而是调用[OH\_AudioRoutingManager\_ReleaseDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_releasedevices)，以便在不再使用时释放所有DeviceDescriptor数组。 |
| uint32\_t \*size | 设置采样率大小值的指针变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS或AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM。 |

### OH\_AudioDeviceDescriptor\_GetDeviceChannelCounts()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceChannelCounts(OH_AudioDeviceDescriptor *audioDeviceDescriptor,uint32_t **channelCounts, uint32_t *size)
```

**描述**

查询目标音频设备描述符的设备通道计数数组。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDeviceDescriptor](capi-ohaudio-oh-audiodevicedescriptor.md) \*audioDeviceDescriptor | 音频设备描述符。通过 [OH\_AudioRoutingManager\_GetDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_getdevices) 或者[OH\_AudioRoutingManager\_OnDeviceChangedCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ondevicechangedcallback)获取。 |
| uint32\_t \*\*channelCounts | 数组指针变量，该变量将设置通道计数数组值。  不要单独释放音频设备通道数指针，而是调用[OH\_AudioRoutingManager\_ReleaseDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_releasedevices)，以便在不再使用时释放所有DeviceDescriptor数组。 |
| uint32\_t \*size | 设置通道计数大小值的指针变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS或AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM。 |

### OH\_AudioDeviceDescriptor\_GetDeviceDisplayName()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceDisplayName(OH_AudioDeviceDescriptor *audioDeviceDescriptor,char **displayName)
```

**描述**

查询目标音频设备描述符的显示名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDeviceDescriptor](capi-ohaudio-oh-audiodevicedescriptor.md) \*audioDeviceDescriptor | 音频设备描述符。通过 [OH\_AudioRoutingManager\_GetDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_getdevices) 或者[OH\_AudioRoutingManager\_OnDeviceChangedCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ondevicechangedcallback)获取。 |
| char \*\*displayName | 设置显示名称值的指针变量。  不要单独释放音频设备显示名称指针，而是调用[OH\_AudioRoutingManager\_ReleaseDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_releasedevices)，以便在不再使用时释放所有DeviceDescriptor数组。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS或AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM。 |

### OH\_AudioDeviceDescriptor\_GetDeviceEncodingTypes()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceEncodingTypes(OH_AudioDeviceDescriptor *audioDeviceDescriptor,OH_AudioStream_EncodingType **encodingTypes, uint32_t *size)
```

**描述**

查询目标音频设备描述符的编码类型数组。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDeviceDescriptor](capi-ohaudio-oh-audiodevicedescriptor.md) \*audioDeviceDescriptor | 音频设备描述符。通过 [OH\_AudioRoutingManager\_GetDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_getdevices) 或者[OH\_AudioRoutingManager\_OnDeviceChangedCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ondevicechangedcallback)获取。 |
| [OH\_AudioStream\_EncodingType](capi-native-audiostream-base-h.md#oh_audiostream_encodingtype) \*\*encodingTypes | 音频设备编码类型，指向[OH\_AudioStream\_EncodingType](capi-native-audiostream-base-h.md#oh_audiostream_encodingtype)。  不要单独释放音频设备编码类型指针，而是调用[OH\_AudioRoutingManager\_ReleaseDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_releasedevices)，以便在不再使用时释放所有DeviceDescriptor数组。 |
| uint32\_t \*size | 设置编码类型大小值的指针变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS或AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM。 |
