---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avimage-generator-h
title: avimage_generator.h
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 头文件 > avimage_generator.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:51+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:187744803f4e5b611b81a57cd9e7caa1ca34721efdfa3a6e8d960ae9ae9469ff
---

## 概述

PhonePC/2in1TabletTVWearable

定义AVImageGenerator接口。使用其C API从视频资源中获取指定时间点视频帧。

**引用文件：** <multimedia/player\_framework/avimage\_generator.h>

**库：** libavimage\_generator.so

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 18

**相关模块：** [AVImageGenerator](capi-avimagegenerator.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVImageGenerator](capi-avimagegenerator-oh-avimagegenerator.md) | OH\_AVImageGenerator | 定义OH\_AVImageGenerator类型，用于生成指定时间点视频帧。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_AVImageGenerator\* OH\_AVImageGenerator\_Create(void)](capi-avimage-generator-h.md#oh_avimagegenerator_create) | 创建OH\_AVImageGenerator实例，用于生成指定时间点视频帧。 |
| [OH\_AVErrCode OH\_AVImageGenerator\_SetFDSource(OH\_AVImageGenerator\* generator, int32\_t fd, int64\_t offset, int64\_t size)](capi-avimage-generator-h.md#oh_avimagegenerator_setfdsource) | 通过媒体文件描述符设置数据源。 |
| [OH\_AVErrCode OH\_AVImageGenerator\_FetchFrameByTime(OH\_AVImageGenerator\* generator, int64\_t timeUs, OH\_AVImageGenerator\_QueryOptions options, OH\_PixelmapNative\*\* pixelMap)](capi-avimage-generator-h.md#oh_avimagegenerator_fetchframebytime) | 从视频资源中获取指定时间点视频帧。  此函数必须在[OH\_AVImageGenerator\_SetFDSource](capi-avimage-generator-h.md#oh_avimagegenerator_setfdsource)之后调用。 |
| [OH\_AVErrCode OH\_AVImageGenerator\_Release(OH\_AVImageGenerator\* generator)](capi-avimage-generator-h.md#oh_avimagegenerator_release) | 释放用于OH\_AVImageGenerator的资源以及销毁OH\_AVImageGenerator实例。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AVImageGenerator\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_AVImageGenerator* OH_AVImageGenerator_Create(void)
```

**描述**

创建OH\_AVImageGenerator实例，用于生成指定时间点视频帧。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 18

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVImageGenerator](capi-avimagegenerator-oh-avimagegenerator.md)\* | 创建成功时返回指向OH\_AVImageGenerator实例的指针，否则返回空指针。  可能的失败原因：HstEngineFactory未能创建AVMetadataHelperEngine。 |

### OH\_AVImageGenerator\_SetFDSource()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVImageGenerator_SetFDSource(OH_AVImageGenerator* generator,int32_t fd, int64_t offset, int64_t size)
```

**描述**

通过媒体文件描述符设置数据源。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVImageGenerator](capi-avimagegenerator-oh-avimagegenerator.md)\* generator | 指向OH\_AVImageGenerator实例的指针。 |
| int32\_t fd | 媒体源的文件描述符。 |
| int64\_t offset | 媒体源在文件描述符中的偏移量。 |
| int64\_t size | 媒体源的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入的generator为空指针或参数无效。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作被禁止。  AV\_ERR\_NO\_MEMORY：内部内存分配失败。 |

### OH\_AVImageGenerator\_FetchFrameByTime()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVImageGenerator_FetchFrameByTime(OH_AVImageGenerator* generator,int64_t timeUs, OH_AVImageGenerator_QueryOptions options, OH_PixelmapNative** pixelMap)
```

**描述**

从视频资源中获取指定时间点视频帧。

此函数必须在[OH\_AVImageGenerator\_SetFDSource](capi-avimage-generator-h.md#oh_avimagegenerator_setfdsource)之后调用。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVImageGenerator](capi-avimagegenerator-oh-avimagegenerator.md)\* generator | 指向OH\_AVImageGenerator实例的指针。 |
| int64\_t timeUs | 需要获取的视频帧在视频中的时间点，单位为微秒（μs）。 |
| [OH\_AVImageGenerator\_QueryOptions](capi-avimage-generator-base-h.md#oh_avimagegenerator_queryoptions) options | 关于给定时间Us和视频帧之间关系的时间选项。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)\*\* pixelMap | 获取的视频帧对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入的generator为空指针或参数无效。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作被禁止。  AV\_ERR\_UNSUPPORTED\_FORMAT：格式不支持。  AV\_ERR\_NO\_MEMORY：内部内存分配失败。 |

### OH\_AVImageGenerator\_Release()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVImageGenerator_Release(OH_AVImageGenerator* generator)
```

**描述**

释放用于OH\_AVImageGenerator的资源以及销毁OH\_AVImageGenerator实例。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVImageGenerator](capi-avimagegenerator-oh-avimagegenerator.md)\* generator | 指向OH\_AVImageGenerator实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入的generator为空指针或参数无效。 |
