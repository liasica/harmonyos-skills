---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-packingoptionsforsequence
title: OH_PackingOptionsForSequence
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_PackingOptionsForSequence
category: harmonyos-references
scraped_at: 2026-09-02T14:52:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1f4dab7e4bc1353e6a0bfb28e29b93ecfdf46c5cd21ff3c7ae1a47a004c379eb
---

```c
typedef struct OH_PackingOptionsForSequence OH_PackingOptionsForSequence
```

## 概述

OH\_PackingOptionsForSequence是native层封装的GIF序列编码选项结构体，不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。

使用[OH\_PackingOptionsForSequence\_Create](capi-image-packer-native-h.md#oh_packingoptionsforsequence_create)函数创建OH\_PackingOptionsForSequence对象。

使用[OH\_PackingOptionsForSequence\_Release](capi-image-packer-native-h.md#oh_packingoptionsforsequence_release)函数释放OH\_PackingOptionsForSequence对象。

使用约束：OH\_PackingOptionsForSequence用于配置PixelMap序列编码为GIF格式时的编码参数，需传入[OH\_ImagePackerNative\_PackToDataFromPixelmapSequence](capi-image-packer-native-h.md#oh_imagepackernative_packtodatafrompixelmapsequence)或[OH\_ImagePackerNative\_PackToFileFromPixelmapSequence](capi-image-packer-native-h.md#oh_imagepackernative_packtofilefrompixelmapsequence)使用。

资源管理：OH\_PackingOptionsForSequence使用完成后，应调用[OH\_PackingOptionsForSequence\_Release](capi-image-packer-native-h.md#oh_packingoptionsforsequence_release)释放。释放后不应继续传入图像序列编码接口或调用其字段获取和设置接口。通过[OH\_PackingOptionsForSequence\_SetDelayTimeList](capi-image-packer-native-h.md#oh_packingoptionsforsequence_setdelaytimelist)和[OH\_PackingOptionsForSequence\_SetDisposalTypes](capi-image-packer-native-h.md#oh_packingoptionsforsequence_setdisposaltypes)传入的数组不会被拷贝，调用方需保证OH\_PackingOptionsForSequence对象使用期间数组数据有效。释放OH\_PackingOptionsForSequence对象不会释放这些数组。

OH\_PackingOptionsForSequence结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 字段获取函数 | 字段设置函数 |
| --- | --- | --- | --- | --- |
| uint32\_t | frameCount | 编码时指定的帧数，编码时必须大于0。 | [OH\_PackingOptionsForSequence\_GetFrameCount](capi-image-packer-native-h.md#oh_packingoptionsforsequence_getframecount) | [OH\_PackingOptionsForSequence\_SetFrameCount](capi-image-packer-native-h.md#oh_packingoptionsforsequence_setframecount) |
| int32\_t \* | delayTimeList | 编码时图片的延迟时间数组，数组中的每个延迟时间必须大于0且不超过65535，单位为10毫秒（ms）。 | [OH\_PackingOptionsForSequence\_GetDelayTimeList](capi-image-packer-native-h.md#oh_packingoptionsforsequence_getdelaytimelist) | [OH\_PackingOptionsForSequence\_SetDelayTimeList](capi-image-packer-native-h.md#oh_packingoptionsforsequence_setdelaytimelist) |
| uint32\_t \* | disposalTypes | 编码时图片的过渡帧模式数组，数组中的每个取值必须小于等于3，取值含义见[OH\_PackingOptionsForSequence\_SetDisposalTypes](capi-image-packer-native-h.md#oh_packingoptionsforsequence_setdisposaltypes)。 | [OH\_PackingOptionsForSequence\_GetDisposalTypes](capi-image-packer-native-h.md#oh_packingoptionsforsequence_getdisposaltypes) | [OH\_PackingOptionsForSequence\_SetDisposalTypes](capi-image-packer-native-h.md#oh_packingoptionsforsequence_setdisposaltypes) |
| uint32\_t | loopCount | 编码时图片循环播放次数，取值范围为[0, 65535]。 | [OH\_PackingOptionsForSequence\_GetLoopCount](capi-image-packer-native-h.md#oh_packingoptionsforsequence_getloopcount) | [OH\_PackingOptionsForSequence\_SetLoopCount](capi-image-packer-native-h.md#oh_packingoptionsforsequence_setloopcount) |

**起始版本：** 18

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [image\_packer\_native.h](capi-image-packer-native-h.md)
