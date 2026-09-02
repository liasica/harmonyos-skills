---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-accessory-manager-h
title: native_audio_accessory_manager.h
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 头文件 > native_audio_accessory_manager.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2f3fc1c7f634c1f9b0cafe6284f61bafb491e582c651f19290db02c37d687480
---

## 概述

声明音频配件管理相关的接口。

该文件接口用于管理音频配件的创建、连接、断开和销毁等功能。

**引用文件：** <ohaudio/native\_audio\_accessory\_manager.h>

**库：** libohaudio.so

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 26.0.0

**相关模块：** [OHAudio](capi-ohaudio.md)

## 汇总

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef bool (\*OH\_AudioAccessory\_SetNoiseReductionCallback)(OH\_AudioAccessory \*accessory, OH\_AudioNoiseReductionMode mode)](capi-native-audio-accessory-manager-h.md#oh_audioaccessory_setnoisereductioncallback) | OH\_AudioAccessory\_SetNoiseReductionCallback | 音频配件降噪模式变更回调函数。 |
| [OH\_AudioCommon\_Result OH\_AudioManager\_GetAccessoryManager(OH\_AudioAccessoryManager \*\*outManager)](capi-native-audio-accessory-manager-h.md#oh_audiomanager_getaccessorymanager) | - | 获取音频配件管理器实例。 |
| [OH\_AudioCommon\_Result OH\_AudioAccessoryManager\_CreateInput(OH\_AudioAccessoryManager \*manager, const OH\_AudioAccessoryInfo \*info, const OH\_AudioAccessoryCapabilities \*capabilities, OH\_AudioAccessory\_OpenInputStreamCallback openInputStream, OH\_AudioAccessory \*\*outOwnedAccessory)](capi-native-audio-accessory-manager-h.md#oh_audioaccessorymanager_createinput) | - | 创建音频配件实例，并设置其支持的音频流能力。 |
| [OH\_AudioCommon\_Result OH\_AudioAccessoryManager\_SetAssociatedMacAddresses(OH\_AudioAccessoryManager \*manager, OH\_AudioAccessory \*accessory, const char \*\*macAddresses, uint32\_t count)](capi-native-audio-accessory-manager-h.md#oh_audioaccessorymanager_setassociatedmacaddresses) | - | 设置与主音频配件组合使用的副配件MAC地址列表。 |
| [OH\_AudioCommon\_Result OH\_AudioAccessoryManager\_RegisterNoiseReductionCapability(OH\_AudioAccessoryManager \*manager, OH\_AudioAccessory \*accessory, const OH\_AudioAccessoryNoiseReductionCapability \*capability, OH\_AudioAccessory\_SetNoiseReductionCallback onNoiseReduction)](capi-native-audio-accessory-manager-h.md#oh_audioaccessorymanager_registernoisereductioncapability) | - | 注册音频配件的降噪能力。 |
| [OH\_AudioCommon\_Result OH\_AudioAccessoryManager\_SetNoiseReductionMode(OH\_AudioAccessoryManager \*manager, OH\_AudioAccessory \*accessory, OH\_AudioNoiseReductionMode mode)](capi-native-audio-accessory-manager-h.md#oh_audioaccessorymanager_setnoisereductionmode) | - | 设置音频配件的降噪模式。 |
| [OH\_AudioCommon\_Result OH\_AudioAccessoryManager\_Connected(OH\_AudioAccessoryManager \*manager, OH\_AudioAccessory \*accessory)](capi-native-audio-accessory-manager-h.md#oh_audioaccessorymanager_connected) | - | 将音频配件连接到音频系统。 |
| [OH\_AudioCommon\_Result OH\_AudioAccessoryManager\_Disconnected(OH\_AudioAccessoryManager \*manager, OH\_AudioAccessory \*accessory)](capi-native-audio-accessory-manager-h.md#oh_audioaccessorymanager_disconnected) | - | 断开音频配件连接。 |
| [OH\_AudioCommon\_Result OH\_AudioAccessoryManager\_Destroy(OH\_AudioAccessoryManager \*manager, OH\_AudioAccessory \*accessory)](capi-native-audio-accessory-manager-h.md#oh_audioaccessorymanager_destroy) | - | 销毁音频配件实例。 |

## 函数说明

### OH\_AudioAccessory\_SetNoiseReductionCallback()

```c
typedef bool (*OH_AudioAccessory_SetNoiseReductionCallback)(OH_AudioAccessory *accessory, OH_AudioNoiseReductionMode mode)
```

**描述**

音频配件降噪模式变更回调函数。

触发时机：当配件的降噪模式发生变更时触发，此回调可以在配件连接后的任意时间触发。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) \*accessory | 音频配件。 |
| [OH\_AudioNoiseReductionMode](capi-native-audio-common-h.md#oh_audionoisereductionmode) mode | 配件当前的降噪模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | true：请求的降噪模式处理成功。  false：请求的降噪模式处理失败。 |

### OH\_AudioManager\_GetAccessoryManager()

```c
OH_AudioCommon_Result OH_AudioManager_GetAccessoryManager(OH_AudioAccessoryManager **outManager)
```

**描述**

获取音频配件管理器实例。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioAccessoryManager](capi-ohaudio-oh-audioaccessorymanager.md) \*\*outManager | 指向OH\_AudioAccessoryManager指针的地址。该指针地址由系统管理，调用方不得释放，否则可能导致使用异常。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数outManager为NULL。 |

### OH\_AudioAccessoryManager\_CreateInput()

```c
OH_AudioCommon_Result OH_AudioAccessoryManager_CreateInput(OH_AudioAccessoryManager *manager, const OH_AudioAccessoryInfo *info, const OH_AudioAccessoryCapabilities *capabilities, OH_AudioAccessory_OpenInputStreamCallback openInputStream, OH_AudioAccessory **outOwnedAccessory)
```

**描述**

创建音频配件实例，并设置其支持的音频流能力。

**说明** 

* 此函数仅用于创建音频配件实例，不会创建任何输入流。
* 函数执行成功时，系统通过outOwnedAccessory指针返回创建好的OH\_AudioAccessory句柄。
* 该音频配件实例需在不再使用时调用OH\_AudioAccessoryManager\_Destroy释放。
* 当应用请求从该音频配件采集音频时，系统会触发openInputStream回调函数。
* 在一个音频配件的生命周期内，输入流可能被创建和释放多次。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioAccessoryManager](capi-ohaudio-oh-audioaccessorymanager.md) \*manager | 指向通过OH\_AudioManager\_GetAccessoryManager获取的音频配件管理器实例。 |
| const [OH\_AudioAccessoryInfo](capi-ohaudio-oh-audioaccessoryinfo.md) \*info | 指向配件基本信息的指针，不可为NULL。 |
| const [OH\_AudioAccessoryCapabilities](capi-ohaudio-oh-audioaccessorycapabilities.md) \*capabilities | 指向配件能力的指针，不可为NULL。 |
| OH\_AudioAccessory\_OpenInputStreamCallback openInputStream | 音频配件打开输入流的回调函数，不可为NULL。  此回调仅在应用请求从该音频配件采集音频时调用，而非在调用此函数时调用。 |
| [OH\_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) \*\*outOwnedAccessory | 指向OH\_AudioAccessory指针的地址，用于接收创建好的音频配件实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数无效，包括info为NULL、capabilities为NULL、openInputStream为NULL、outOwnedAccessory为NULL、info信息未全部填写、capabilities信息未全部填写，或outOwnedAccessory已通过OH\_AudioAccessoryManager\_CreateInput创建。  AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE：参数manager未通过OH\_AudioManager\_GetAccessoryManager进行初始化。 |

### OH\_AudioAccessoryManager\_SetAssociatedMacAddresses()

```c
OH_AudioCommon_Result OH_AudioAccessoryManager_SetAssociatedMacAddresses(OH_AudioAccessoryManager *manager, OH_AudioAccessory *accessory, const char **macAddresses, uint32_t count)
```

**描述**

设置与主音频配件组合使用的副配件MAC地址列表。

**说明** 

* 此函数适用于多配件组合场景（如二合一、四合一），支持动态管理配件组合。
* 初始化：配件创建后，调用此函数设置初始副配件列表。
* 动态更新：副配件替换或断开连接时，调用此函数覆盖旧的MAC列表。
* 线程安全：录音期间可安全调用。
* 限制：此函数仅用于更新副配件MAC地址列表，不用于更新主配件MAC地址。主配件断开连接或主配件MAC地址变化时，应先断开并销毁原有配件句柄，再使用新的主配件信息重新创建配件实例。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioAccessoryManager](capi-ohaudio-oh-audioaccessorymanager.md) \*manager | 指向通过OH\_AudioManager\_GetAccessoryManager获取的音频配件管理器实例。 |
| [OH\_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) \*accessory | 指向主配件句柄的指针。 |
| const char \*\*macAddresses | 副配件MAC地址数组。  当count为0时可以为空，表示清除副配件MAC列表，适用于所有副配件断开连接的场景。  每个元素需符合以下规则：  - 格式为以冒号分隔的十六进制表示的NUL终止ASCII字符串。  接受大写和小写十六进制数字（A-F / a-f）。  - 需为非空、非零长度字符串。  - 同一数组中的重复地址将被忽略，仅每个唯一地址的首次出现生效。 |
| uint32\_t count | MAC地址数组中的元素数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数无效，包括manager为NULL、manager未通过OH\_AudioManager\_GetAccessoryManager进行初始化、accessory为NULL，或macAddresses传入的个数与count不一致。  AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE：参数accessory未通过OH\_AudioAccessoryManager\_CreateInput创建。 |

### OH\_AudioAccessoryManager\_RegisterNoiseReductionCapability()

```c
OH_AudioCommon_Result OH_AudioAccessoryManager_RegisterNoiseReductionCapability(OH_AudioAccessoryManager *manager, OH_AudioAccessory *accessory, const OH_AudioAccessoryNoiseReductionCapability *capability, OH_AudioAccessory_SetNoiseReductionCallback onNoiseReduction)
```

**描述**

注册音频配件的降噪能力。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioAccessoryManager](capi-ohaudio-oh-audioaccessorymanager.md) \*manager | 指向通过OH\_AudioManager\_GetAccessoryManager获取的音频配件管理器实例。 |
| [OH\_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) \*accessory | 指向通过OH\_AudioAccessoryManager\_CreateInput获取的音频配件实例。 |
| const [OH\_AudioAccessoryNoiseReductionCapability](capi-ohaudio-oh-audioaccessorynoisereductioncapability.md) \*capability | 指向降噪能力的指针，不可为NULL。 |
| OH\_AudioAccessory\_SetNoiseReductionCallback onNoiseReduction | 音频配件的降噪模式发生变更时调用的回调函数。  如果配件不支持动态模式切换，可以为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数无效，包括manager为NULL、manager未通过OH\_AudioManager\_GetAccessoryManager进行初始化、accessory为NULL、capability为NULL，或capability中的supportedModes为NULL或supportedModeCount为0。  AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE：参数accessory未通过OH\_AudioAccessoryManager\_CreateInput创建。 |

### OH\_AudioAccessoryManager\_SetNoiseReductionMode()

```c
OH_AudioCommon_Result OH_AudioAccessoryManager_SetNoiseReductionMode(OH_AudioAccessoryManager *manager, OH_AudioAccessory *accessory, OH_AudioNoiseReductionMode mode)
```

**描述**

设置音频配件的降噪模式。

**说明** 

* 此函数由配件关联的服务或应用来调用，用于将配件当前降噪模式同步到系统。
* 通常在通过其他方式（如硬件按钮或配套应用）更改降噪模式时使用，以确保系统侧的降噪模式与配件实际降噪模式保持一致。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioAccessoryManager](capi-ohaudio-oh-audioaccessorymanager.md) \*manager | 指向通过OH\_AudioManager\_GetAccessoryManager获取的音频配件管理器实例。 |
| [OH\_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) \*accessory | 指向通过OH\_AudioAccessoryManager\_CreateInput获取的音频配件实例。 |
| [OH\_AudioNoiseReductionMode](capi-native-audio-common-h.md#oh_audionoisereductionmode) mode | 要设置的降噪模式。应为通过RegisterNoiseReductionCapability注册的模式之一。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数accessory为NULL。  AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE：参数accessory未通过OH\_AudioAccessoryManager\_CreateInput创建，或未通过OH\_AudioAccessoryManager\_Connected连接。  AUDIOCOMMON\_RESULT\_ERROR\_UNSUPPORTED：设置的降噪模式未通过OH\_AudioAccessoryManager\_RegisterNoiseReductionCapability注册。 |

### OH\_AudioAccessoryManager\_Connected()

```c
OH_AudioCommon_Result OH_AudioAccessoryManager_Connected(OH_AudioAccessoryManager *manager, OH_AudioAccessory *accessory)
```

**描述**

将音频配件连接到音频系统。

**说明** 

* 调用此函数前，需通过OH\_AudioManager\_GetAccessoryManager获取的音频配件管理器实例，并通过OH\_AudioAccessoryManager\_CreateInput创建accessory实例。
* 建议音频配件管理程序优先接入智慧生活应用，为用户提供设备发现与连接体验的一致性。
* 若以独立音频配件管理应用方式，需要申请ACL权限ohos.permission.MANAGE\_AUDIO\_ACCESSORY。

**需要权限：** ohos.permission.MANAGE\_AUDIO\_ACCESSORY

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioAccessoryManager](capi-ohaudio-oh-audioaccessorymanager.md) \*manager | 指向通过OH\_AudioManager\_GetAccessoryManager获取的音频配件管理器实例。 |
| [OH\_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) \*accessory | 指向通过OH\_AudioAccessoryManager\_CreateInput获取的音频配件实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_PERMISSION\_DENIED：调用方没有ohos.permission.MANAGE\_AUDIO\_ACCESSORY权限。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数无效，包括manager为NULL、manager未通过OH\_AudioManager\_GetAccessoryManager进行初始化，或accessory为NULL。  AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE：参数accessory未通过OH\_AudioAccessoryManager\_CreateInput创建，或accessory已通过OH\_AudioAccessoryManager\_Connected连接。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：音频服务进程死亡。 |

### OH\_AudioAccessoryManager\_Disconnected()

```c
OH_AudioCommon_Result OH_AudioAccessoryManager_Disconnected(OH_AudioAccessoryManager *manager, OH_AudioAccessory *accessory)
```

**描述**

断开音频配件连接。

**需要权限：** ohos.permission.MANAGE\_AUDIO\_ACCESSORY

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioAccessoryManager](capi-ohaudio-oh-audioaccessorymanager.md) \*manager | 指向通过OH\_AudioManager\_GetAccessoryManager获取的音频配件管理器实例。 |
| [OH\_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) \*accessory | 指向通过OH\_AudioAccessoryManager\_CreateInput获取的音频配件实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_PERMISSION\_DENIED：调用方没有ohos.permission.MANAGE\_AUDIO\_ACCESSORY权限。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数accessory为NULL。  AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE：参数accessory未通过OH\_AudioAccessoryManager\_Connected连接。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：音频服务进程死亡。 |

### OH\_AudioAccessoryManager\_Destroy()

```c
OH_AudioCommon_Result OH_AudioAccessoryManager_Destroy(OH_AudioAccessoryManager *manager, OH_AudioAccessory *accessory)
```

**描述**

销毁音频配件实例。

**说明** 

销毁前需先断开配件连接。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioAccessoryManager](capi-ohaudio-oh-audioaccessorymanager.md) \*manager | 指向通过OH\_AudioManager\_GetAccessoryManager获取的音频配件管理器实例。 |
| [OH\_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) \*accessory | 指向通过OH\_AudioAccessoryManager\_CreateInput获取的音频配件实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数无效，包括manager为NULL、manager未通过OH\_AudioManager\_GetAccessoryManager进行初始化，或accessory为NULL。  AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE：参数accessory未通过OH\_AudioAccessoryManager\_Disconnected断开连接。 |
