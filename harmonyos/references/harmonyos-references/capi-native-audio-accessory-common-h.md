---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-accessory-common-h
title: native_audio_accessory_common.h
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 头文件 > native_audio_accessory_common.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f3d2c036ddcc2c61e6ebd7e1e87d18e242f1d917f59bfb91de20e4103f987bc1
---

## 概述

声明外部音频配件设备接口的公共数据结构。

定义音频配件接口的公共类型。

**引用文件：** <ohaudio/native\_audio\_accessory\_common.h>

**库：** libohaudio.so

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 26.0.0

**相关模块：** [OHAudio](capi-ohaudio.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioAccessoryManager](capi-ohaudio-oh-audioaccessorymanager.md) | OH\_AudioAccessoryManager | 声明音频配件管理器。 |
| [OH\_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) | OH\_AudioAccessory | 声明音频配件。 |
| [OH\_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) | OH\_AudioAccessoryInputStream | 声明音频配件输入流。 |
| [OH\_AudioAccessoryInfo](capi-ohaudio-oh-audioaccessoryinfo.md) | OH\_AudioAccessoryInfo | 定义音频配件的基本信息。 |
| [OH\_AudioAccessoryNoiseReductionCapability](capi-ohaudio-oh-audioaccessorynoisereductioncapability.md) | OH\_AudioAccessoryNoiseReductionCapability | 定义音频配件的降噪能力。 |
| [OH\_AudioAccessoryCapabilities](capi-ohaudio-oh-audioaccessorycapabilities.md) | OH\_AudioAccessoryCapabilities | 定义音频配件的能力。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioAccessoryType](capi-native-audio-accessory-common-h.md#oh_audioaccessorytype) | OH\_AudioAccessoryType | 枚举音频配件连接类型。 |

## 枚举类型说明

### OH\_AudioAccessoryType

```c
enum OH_AudioAccessoryType
```

**描述**

枚举音频配件连接类型。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| AUDIO\_ACCESSORY\_TYPE\_BT\_SPP = 1 | 蓝牙串行端口配置文件（Serial Port Profile，SPP）连接。 |
