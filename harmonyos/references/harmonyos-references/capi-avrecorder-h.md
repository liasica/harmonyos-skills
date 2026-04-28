---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-h
title: avrecorder.h
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 头文件 > avrecorder.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:604fe6f22a4d5f83ab709d22c0990719dbc3e718e50610dca9919baf30bcbc01
---

## 概述

PhonePC/2in1TabletTVWearable

定义AVRecorder接口。应用可使用媒体AVRecorder提供的接口录制媒体数据。

**引用文件：** <multimedia/player\_framework/avrecorder.h>

**库：** libavrecorder.so

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**相关模块：** [AVRecorder](capi-avrecorder.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_AVRecorder \*OH\_AVRecorder\_Create(void)](capi-avrecorder-h.md#oh_avrecorder_create) | 创建AVRecorder实例。调用成功之后进入AVRECORDER\_IDLE状态。 |
| [OH\_AVErrCode OH\_AVRecorder\_Prepare(OH\_AVRecorder \*recorder, OH\_AVRecorder\_Config \*config)](capi-avrecorder-h.md#oh_avrecorder_prepare) | 配置AVRecorder参数，准备录制。必须在[OH\_AVRecorder\_Create](capi-avrecorder-h.md#oh_avrecorder_create)成功触发之后调用，调用成功之后进入AVRECORDER\_PREPARED状态。  若只录制音频，则无需配置视频相关参数；同理，若只录制视频，则无需配置音频相关参数。 |
| [OH\_AVErrCode OH\_AVRecorder\_GetAVRecorderConfig(OH\_AVRecorder \*recorder, OH\_AVRecorder\_Config \*\*config)](capi-avrecorder-h.md#oh_avrecorder_getavrecorderconfig) | 获取当前的录制参数。此接口必须在录制准备完成后调用。传入的\*config必须为nullptr，由框架层统一分配和释放内存，以避免内存管理混乱，防止内存泄漏或重复释放等问题。 |
| [OH\_AVErrCode OH\_AVRecorder\_GetInputSurface(OH\_AVRecorder \*recorder, OHNativeWindow \*\*window)](capi-avrecorder-h.md#oh_avrecorder_getinputsurface) | 获取输入Surface。必须在[OH\_AVRecorder\_Prepare](capi-avrecorder-h.md#oh_avrecorder_prepare)成功触发之后，[OH\_AVRecorder\_Start](capi-avrecorder-h.md#oh_avrecorder_start)之前调用。  此Surface提供给调用者，调用者从此Surface中获取Surface Buffer，填入相应的视频数据。 |
| [OH\_AVErrCode OH\_AVRecorder\_UpdateRotation(OH\_AVRecorder \*recorder, int32\_t rotation)](capi-avrecorder-h.md#oh_avrecorder_updaterotation) | 更新视频旋转角度。必须在[OH\_AVRecorder\_Prepare](capi-avrecorder-h.md#oh_avrecorder_prepare)成功触发之后，[OH\_AVRecorder\_Start](capi-avrecorder-h.md#oh_avrecorder_start)之前调用。 |
| [OH\_AVErrCode OH\_AVRecorder\_Start(OH\_AVRecorder \*recorder)](capi-avrecorder-h.md#oh_avrecorder_start) | 开始录制。必须在[OH\_AVRecorder\_Prepare](capi-avrecorder-h.md#oh_avrecorder_prepare)成功触发之后调用，调用成功之后进入AVRECORDER\_STARTED状态。 |
| [OH\_AVErrCode OH\_AVRecorder\_Pause(OH\_AVRecorder \*recorder)](capi-avrecorder-h.md#oh_avrecorder_pause) | 暂停录制。必须在[OH\_AVRecorder\_Start](capi-avrecorder-h.md#oh_avrecorder_start)成功触发之后，处于AVRECORDER\_STARTED状态时调用，调用成功之后进入AVRECORDER\_PAUSED状态。  之后可以通过调用[OH\_AVRecorder\_Resume](capi-avrecorder-h.md#oh_avrecorder_resume)恢复录制，重新进入AVRECORDER\_STARTED状态。 |
| [OH\_AVErrCode OH\_AVRecorder\_Resume(OH\_AVRecorder \*recorder)](capi-avrecorder-h.md#oh_avrecorder_resume) | 恢复录制。必须在[OH\_AVRecorder\_Pause](capi-avrecorder-h.md#oh_avrecorder_pause)成功触发之后，处于PAUSED状态时调用，调用成功之后重新进入AVRECORDER\_STARTED状态。 |
| [OH\_AVErrCode OH\_AVRecorder\_Stop(OH\_AVRecorder \*recorder)](capi-avrecorder-h.md#oh_avrecorder_stop) | 停止录制。必须在[OH\_AVRecorder\_Start](capi-avrecorder-h.md#oh_avrecorder_start)成功触发之后调用，调用成功之后进入AVRECORDER\_STOPPED状态。  纯音频录制时，需要重新调用[OH\_AVRecorder\_Prepare](capi-avrecorder-h.md#oh_avrecorder_prepare)接口才能重新录制。  纯视频录制、音视频录制时，需要重新调用[OH\_AVRecorder\_Prepare](capi-avrecorder-h.md#oh_avrecorder_prepare)和[OH\_AVRecorder\_GetInputSurface](capi-avrecorder-h.md#oh_avrecorder_getinputsurface)接口才能重新录制。 |
| [OH\_AVErrCode OH\_AVRecorder\_Reset(OH\_AVRecorder \*recorder)](capi-avrecorder-h.md#oh_avrecorder_reset) | 重置录制状态。必须在非AVRECORDER\_RELEASED状态下调用，调用成功之后进入AVRECORDER\_IDLE状态。  纯音频录制时，需要重新调用[OH\_AVRecorder\_Prepare](capi-avrecorder-h.md#oh_avrecorder_prepare)接口才能重新录制。  纯视频录制、音视频录制时，需要重新调用[OH\_AVRecorder\_Prepare](capi-avrecorder-h.md#oh_avrecorder_prepare)和[OH\_AVRecorder\_GetInputSurface](capi-avrecorder-h.md#oh_avrecorder_getinputsurface)接口才能重新录制。 |
| [OH\_AVErrCode OH\_AVRecorder\_Release(OH\_AVRecorder \*recorder)](capi-avrecorder-h.md#oh_avrecorder_release) | 释放录制资源。调用成功之后进入AVRECORDER\_RELEASED状态。  调用此接口释放录制资源后，recorder内存将释放，应用层需要显式地将recorder指针置空，避免访问野指针。释放音视频录制资源之后，该OH\_AVRecorder实例不能再进行任何操作。 |
| [OH\_AVErrCode OH\_AVRecorder\_GetAvailableEncoder(OH\_AVRecorder \*recorder, OH\_AVRecorder\_EncoderInfo \*\*info, int32\_t \*length)](capi-avrecorder-h.md#oh_avrecorder_getavailableencoder) | 获取AVRecorder可用的编码器和编码器信息。  参数\*info必须为nullptr，由框架层统一分配和释放内存，以避免内存管理混乱，防止内存泄漏或重复释放等问题。 |
| [OH\_AVErrCode OH\_AVRecorder\_SetStateCallback(OH\_AVRecorder \*recorder, OH\_AVRecorder\_OnStateChange callback, void \*userData)](capi-avrecorder-h.md#oh_avrecorder_setstatecallback) | 设置状态回调函数，以便应用能够响应AVRecorder生成的状态变化事件。此接口必须在[OH\_AVRecorder\_Start](capi-avrecorder-h.md#oh_avrecorder_start)调用之前调用。 |
| [OH\_AVErrCode OH\_AVRecorder\_SetErrorCallback(OH\_AVRecorder \*recorder, OH\_AVRecorder\_OnError callback, void \*userData)](capi-avrecorder-h.md#oh_avrecorder_seterrorcallback) | 设置错误回调函数，以便应用能够响应AVRecorder生成的错误事件。此接口必须在[OH\_AVRecorder\_Start](capi-avrecorder-h.md#oh_avrecorder_start)调用之前调用。 |
| [OH\_AVErrCode OH\_AVRecorder\_SetUriCallback(OH\_AVRecorder \*recorder, OH\_AVRecorder\_OnUri callback, void \*userData)](capi-avrecorder-h.md#oh_avrecorder_seturicallback) | 设置URI回调函数，以便应用能够响应AVRecorder生成的URI事件。此接口必须在[OH\_AVRecorder\_Start](capi-avrecorder-h.md#oh_avrecorder_start)调用之前调用。 |
| [OH\_AVErrCode OH\_AVRecorder\_SetWillMuteWhenInterrupted(OH\_AVRecorder \*recorder, bool muteWhenInterrupted)](capi-avrecorder-h.md#oh_avrecorder_setwillmutewheninterrupted) | 设置是否开启静音打断模式。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AVRecorder\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_AVRecorder *OH_AVRecorder_Create(void)
```

**描述**

创建AVRecorder实例。调用成功之后进入AVRECORDER\_IDLE状态。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) | 成功时返回指向OH\_AVRecorder实例的指针，失败时返回nullptr。 |

### OH\_AVRecorder\_Prepare()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVRecorder_Prepare(OH_AVRecorder *recorder, OH_AVRecorder_Config *config)
```

**描述**

配置AVRecorder参数，准备录制。必须在[OH\_AVRecorder\_Create](capi-avrecorder-h.md#oh_avrecorder_create)成功触发之后调用，调用成功之后进入AVRECORDER\_PREPARED状态。

若只录制音频，则无需配置视频相关参数；同理，若只录制视频，则无需配置音频相关参数。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) \*recorder | 指向OH\_AVRecorder实例的指针。 |
| [OH\_AVRecorder\_Config](capi-avrecorder-oh-avrecorder-config.md) \*config | 指向OH\_AVRecorder\_Config实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入的recorder为nullptr或者准备失败。 |

### OH\_AVRecorder\_GetAVRecorderConfig()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVRecorder_GetAVRecorderConfig(OH_AVRecorder *recorder, OH_AVRecorder_Config **config)
```

**描述**

获取当前的录制参数。此接口必须在录制准备完成后调用。

传入的\*config必须为nullptr，由框架层统一分配和释放内存，以避免内存管理混乱，防止内存泄漏或重复释放等问题。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) \*recorder | 指向OH\_AVRecorder实例的指针。 |
| [OH\_AVRecorder\_Config](capi-avrecorder-oh-avrecorder-config.md) \*\*config | 指向OH\_AVRecorder\_Config实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入的recorder为nullptr或\*config不为nullptr。  AV\_ERR\_NO\_MEMORY：内存不足，\*config内存分配失败。 |

### OH\_AVRecorder\_GetInputSurface()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVRecorder_GetInputSurface(OH_AVRecorder *recorder, OHNativeWindow **window)
```

**描述**

获取输入Surface。必须在[OH\_AVRecorder\_Prepare](capi-avrecorder-h.md#oh_avrecorder_prepare)成功触发之后，[OH\_AVRecorder\_Start](capi-avrecorder-h.md#oh_avrecorder_start)之前调用。

此Surface提供给调用者，调用者从此Surface中获取Surface Buffer，填入相应的视频数据。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) \*recorder | 指向OH\_AVRecorder实例的指针。 |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*\*window | 指向OHNativeWindow实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入的recorder为nullptr。 |

### OH\_AVRecorder\_UpdateRotation()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVRecorder_UpdateRotation(OH_AVRecorder *recorder, int32_t rotation)
```

**描述**

更新视频旋转角度。必须在[OH\_AVRecorder\_Prepare](capi-avrecorder-h.md#oh_avrecorder_prepare)成功触发之后，[OH\_AVRecorder\_Start](capi-avrecorder-h.md#oh_avrecorder_start)之前调用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) \*recorder | 指向OH\_AVRecorder实例的指针。 |
| int32\_t rotation | 视频旋转角度，必须是整数 [0, 90, 180, 270] 中的一个。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入的recorder为nullptr或输入的rotation不符合要求或更新方向失败。 |

### OH\_AVRecorder\_Start()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVRecorder_Start(OH_AVRecorder *recorder)
```

**描述**

开始录制。必须在[OH\_AVRecorder\_Prepare](capi-avrecorder-h.md#oh_avrecorder_prepare)成功触发之后调用，调用成功之后进入AVRECORDER\_STARTED状态。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) \*recorder | 指向OH\_AVRecorder实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入的recorder为nullptr或启动失败。 |

### OH\_AVRecorder\_Pause()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVRecorder_Pause(OH_AVRecorder *recorder)
```

**描述**

暂停录制。必须在[OH\_AVRecorder\_Start](capi-avrecorder-h.md#oh_avrecorder_start)成功触发之后，处于AVRECORDER\_STARTED状态时调用，调用成功之后进入AVRECORDER\_PAUSED状态。

之后可以通过调用[OH\_AVRecorder\_Resume](capi-avrecorder-h.md#oh_avrecorder_resume)恢复录制，重新进入AVRECORDER\_STARTED状态。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) \*recorder | 指向OH\_AVRecorder实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入的recorder为nullptr或暂停失败。 |

### OH\_AVRecorder\_Resume()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVRecorder_Resume(OH_AVRecorder *recorder)
```

**描述**

恢复录制。必须在[OH\_AVRecorder\_Pause](capi-avrecorder-h.md#oh_avrecorder_pause)成功触发之后，处于PAUSED状态时调用，调用成功之后重新进入AVRECORDER\_STARTED状态。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) \*recorder | 指向OH\_AVRecorder实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入的recorder为nullptr或恢复失败。 |

### OH\_AVRecorder\_Stop()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVRecorder_Stop(OH_AVRecorder *recorder)
```

**描述**

停止录制。必须在[OH\_AVRecorder\_Start](capi-avrecorder-h.md#oh_avrecorder_start)成功触发之后调用，调用成功之后进入AVRECORDER\_STOPPED状态。

纯音频录制时，需要重新调用[OH\_AVRecorder\_Prepare](capi-avrecorder-h.md#oh_avrecorder_prepare)接口才能重新录制。

纯视频录制、音视频录制时，需要重新调用[OH\_AVRecorder\_Prepare](capi-avrecorder-h.md#oh_avrecorder_prepare)和[OH\_AVRecorder\_GetInputSurface](capi-avrecorder-h.md#oh_avrecorder_getinputsurface)接口才能重新录制。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) \*recorder | 指向OH\_AVRecorder实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入的recorder为nullptr或停止失败。 |

### OH\_AVRecorder\_Reset()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVRecorder_Reset(OH_AVRecorder *recorder)
```

**描述**

重置录制状态。必须在非AVRECORDER\_RELEASED状态下调用，调用成功之后进入AVRECORDER\_IDLE状态。

纯音频录制时，需要重新调用[OH\_AVRecorder\_Prepare](capi-avrecorder-h.md#oh_avrecorder_prepare)接口才能重新录制。

纯视频录制、音视频录制时，需要重新调用[OH\_AVRecorder\_Prepare](capi-avrecorder-h.md#oh_avrecorder_prepare)和[OH\_AVRecorder\_GetInputSurface](capi-avrecorder-h.md#oh_avrecorder_getinputsurface)接口才能重新录制。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) \*recorder | 指向OH\_AVRecorder实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入的recorder为nullptr或重置失败。 |

### OH\_AVRecorder\_Release()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVRecorder_Release(OH_AVRecorder *recorder)
```

**描述**

释放录制资源。调用成功之后进入AVRECORDER\_RELEASED状态。

调用此接口释放录制资源后，recorder内存将释放，应用层需要显式地将recorder指针置空，避免访问野指针。释放音视频录制资源之后，该OH\_AVRecorder实例不能再进行任何操作。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) \*recorder | 指向OH\_AVRecorder实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入的recorder为nullptr或释放失败。 |

### OH\_AVRecorder\_GetAvailableEncoder()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVRecorder_GetAvailableEncoder(OH_AVRecorder *recorder, OH_AVRecorder_EncoderInfo **info,int32_t *length)
```

**描述**

获取AVRecorder可用的编码器和编码器信息。

参数\*info必须为nullptr，由框架层统一分配和释放内存，以避免内存管理混乱，防止内存泄漏或重复释放等问题。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) \*recorder | 指向OH\_AVRecorder实例的指针。 |
| [OH\_AVRecorder\_EncoderInfo](capi-avrecorder-oh-avrecorder-encoderinfo.md) \*\*info | 指向OH\_AVRecorder\_EncoderInfo实例的指针。 |
| int32\_t \*length | 可用编码器的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入的 recorder 为nullptr。  AV\_ERR\_NO\_MEMORY：内存不足，\*info内存分配失败。 |

### OH\_AVRecorder\_SetStateCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVRecorder_SetStateCallback(OH_AVRecorder *recorder, OH_AVRecorder_OnStateChange callback, void *userData)
```

**描述**

设置状态回调函数，以便应用能够响应AVRecorder生成的状态变化事件。此接口必须在[OH\_AVRecorder\_Start](capi-avrecorder-h.md#oh_avrecorder_start)调用之前调用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) \*recorder | 指向OH\_AVRecorder实例的指针。 |
| [OH\_AVRecorder\_OnStateChange](capi-avrecorder-base-h.md#oh_avrecorder_onstatechange) callback | 状态回调函数。 |
| void \*userData | 指向用户特定数据的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入的recorder为nullptr或回调函数为nullptr。 |

### OH\_AVRecorder\_SetErrorCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVRecorder_SetErrorCallback(OH_AVRecorder *recorder, OH_AVRecorder_OnError callback, void *userData)
```

**描述**

设置错误回调函数，以便应用能够响应AVRecorder生成的错误事件。此接口必须在[OH\_AVRecorder\_Start](capi-avrecorder-h.md#oh_avrecorder_start)调用之前调用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) \*recorder | 指向OH\_AVRecorder实例的指针。 |
| [OH\_AVRecorder\_OnError](capi-avrecorder-base-h.md#oh_avrecorder_onerror) callback | 错误回调函数。 |
| void \*userData | 指向用户特定数据的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入的recorder为nullptr或回调函数为nullptr。 |

### OH\_AVRecorder\_SetUriCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVRecorder_SetUriCallback(OH_AVRecorder *recorder, OH_AVRecorder_OnUri callback, void *userData)
```

**描述**

设置URI回调函数，以便应用能够响应AVRecorder生成的URI事件。此接口必须在[OH\_AVRecorder\_Start](capi-avrecorder-h.md#oh_avrecorder_start)调用之前调用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) \*recorder | 指向OH\_AVRecorder实例的指针。 |
| [OH\_AVRecorder\_OnUri](capi-avrecorder-base-h.md#oh_avrecorder_onuri) callback | URI回调函数。 |
| void \*userData | 指向用户特定数据的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入的recorder为nullptr或回调函数为nullptr。 |

### OH\_AVRecorder\_SetWillMuteWhenInterrupted()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVRecorder_SetWillMuteWhenInterrupted(OH_AVRecorder *recorder, bool muteWhenInterrupted)
```

**描述**

设置是否开启静音打断模式。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) \*recorder | 指向OH\_AVRecorder实例的指针。 |
| bool muteWhenInterrupted | 设置是否开启静音打断模式。设置成true表示当应用需要录制时保持静音而不是被打断，设置成false表示应用录制打断时停止录音而不是保持静音。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入的recorder为nullptr或回调函数为nullptr。  AV\_ERR\_INVALID\_STATE：函数在无效状态下调用，应先处于准备状态。 |
