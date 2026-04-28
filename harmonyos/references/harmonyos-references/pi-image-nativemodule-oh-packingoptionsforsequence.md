---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-image-nativemodule-oh-packingoptionsforsequence
title: OH_PackingOptionsForSequence
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_PackingOptionsForSequence
category: harmonyos-references
scraped_at: 2026-04-28T08:13:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e9a9ef7f14a3e2041580927055f3d7989df0532fca372ef2c841070784441aa2
---

```
1. typedef struct OH_PackingOptionsForSequence OH_PackingOptionsForSequence
```

## 概述

PhonePC/2in1TabletTVWearable

OH\_PackingOptionsForSequence是native层封装的图像序列编码选项结构体，不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。

创建OH\_PackingOptionsForSequence结构体的对象使用[OH\_PackingOptionsForSequence\_Create](capi-image-packer-native-h.md#oh_packingoptionsforsequence_create)函数。

释放OH\_PackingOptionsForSequence对象使用[OH\_PackingOptionsForSequence\_Release](capi-image-packer-native-h.md#oh_packingoptionsforsequence_release)函数。

| 字段类型 | 字段名称 | 字段描述 | 操作函数 | 函数描述 |
| --- | --- | --- | --- | --- |
| uint32\_t | frameCount | 帧数 | [OH\_PackingOptionsForSequence\_GetFrameCount](capi-image-packer-native-h.md#oh_packingoptionsforsequence_getframecount) | 获取编码时指定的帧数。 |
| uint32\_t | frameCount | 帧数 | [OH\_PackingOptionsForSequence\_SetFrameCount](capi-image-packer-native-h.md#oh_packingoptionsforsequence_setframecount) | 设置编码时指定的帧数。 |
| int32\_t \* | delayTimeList | 延迟时间数组 | [OH\_PackingOptionsForSequence\_GetDelayTimeList](capi-image-packer-native-h.md#oh_packingoptionsforsequence_getdelaytimelist) | 获取编码时图片的延迟时间数组。 |
| int32\_t \* | delayTimeList | 延迟时间数组 | [OH\_PackingOptionsForSequence\_SetDelayTimeList](capi-image-packer-native-h.md#oh_packingoptionsforsequence_setdelaytimelist) | 设置编码时图片的延迟时间数组。 |
| uint32\_t \* | disposalTypes | 帧数 | [OH\_PackingOptionsForSequence\_GetDisposalTypes](capi-image-packer-native-h.md#oh_packingoptionsforsequence_getdisposaltypes) | 获取编码时图片的过渡帧模式数组。 |
| uint32\_t \* | disposalTypes | 帧数 | [OH\_PackingOptionsForSequence\_SetDisposalTypes](capi-image-packer-native-h.md#oh_packingoptionsforsequence_setdisposaltypes) | 设置编码时图片的过渡帧模式数组。 |
| uint32\_t | loopCount | 帧数 | [OH\_PackingOptionsForSequence\_GetLoopCount](capi-image-packer-native-h.md#oh_packingoptionsforsequence_getloopcount) | 获取编码时图片循环播放次数。 |
| uint32\_t | loopCount | 帧数 | [OH\_PackingOptionsForSequence\_SetLoopCount](capi-image-packer-native-h.md#oh_packingoptionsforsequence_setloopcount) | 设置编码时图片循环播放次数，取值范围为[0，65535]，0表示无限循环；若无此字段，则表示不循环播放。 |

**起始版本：** 18

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [image\_packer\_native.h](capi-image-packer-native-h.md)
