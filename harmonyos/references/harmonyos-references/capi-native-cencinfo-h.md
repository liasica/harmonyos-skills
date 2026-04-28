---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-cencinfo-h
title: native_cencinfo.h
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 头文件 > native_cencinfo.h
category: harmonyos-references
scraped_at: 2026-04-28T08:12:06+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ab72d43628bbaaa88e205b8e78ac5622f4ce2f5537eb186710c161c3ec5d594d
---

## 概述

PhonePC/2in1TabletTVWearable

声明用于设置解密参数的Native API。

**引用文件：** <multimedia/player\_framework/native\_cencinfo.h>

**库：** libnative\_media\_avcencinfo.so

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 12

**相关模块：** [Multimedia\_Drm](capi-multimedia-drm.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [DrmSubsample](capi-multimedia-drm-drmsubsample.md) | DrmSubsample | Subsample结构类型定义。 |
| [OH\_AVBuffer](capi-core-oh-avbuffer.md) | OH\_AVBuffer | AVBuffer结构。 |
| [OH\_AVCencInfo](capi-multimedia-drm-oh-avcencinfo.md) | OH\_AVCencInfo | AVCencInfo结构。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [DrmCencAlgorithm](capi-native-cencinfo-h.md#drmcencalgorithm) | DrmCencAlgorithm | Drm CENC算法类型。 |
| [DrmCencInfoMode](capi-native-cencinfo-h.md#drmcencinfomode) | DrmCencInfoMode | 枚举类型，表示cencInfo中keyId/iv/subsample信息是否设置。 |

### 宏定义

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| DRM\_KEY\_ID\_SIZE 16 | Key id长度为16字节。  **起始版本：** 12 |
| DRM\_KEY\_IV\_SIZE 16 | Iv长度为16字节。  **起始版本：** 12 |
| DRM\_KEY\_MAX\_SUB\_SAMPLE\_NUM 64 | 最大的Subsample数量为64个。  **起始版本：** 12 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_AVCencInfo \*OH\_AVCencInfo\_Create()](capi-native-cencinfo-h.md#oh_avcencinfo_create) | 创建用于设置cencInfo的OH\_AVCencInfo实例。 |
| [OH\_AVErrCode OH\_AVCencInfo\_Destroy(OH\_AVCencInfo \*cencInfo)](capi-native-cencinfo-h.md#oh_avcencinfo_destroy) | 销毁OH\_AVCencInfo实例并释放内部资源。  同一个实例只能销毁一次。在再次创建实例之前，不应使用该实例。建议在实例销毁成功后立即将实例指针设置为nullptr。 |
| [OH\_AVErrCode OH\_AVCencInfo\_SetAlgorithm(OH\_AVCencInfo \*cencInfo, enum DrmCencAlgorithm algo)](capi-native-cencinfo-h.md#oh_avcencinfo_setalgorithm) | 设置cencInfo加密算法。 |
| [OH\_AVErrCode OH\_AVCencInfo\_SetKeyIdAndIv(OH\_AVCencInfo \*cencInfo, uint8\_t \*keyId, uint32\_t keyIdLen, uint8\_t \*iv, uint32\_t ivLen)](capi-native-cencinfo-h.md#oh_avcencinfo_setkeyidandiv) | 设置cencInfo的keyId和iv。 |
| [OH\_AVErrCode OH\_AVCencInfo\_SetSubsampleInfo(OH\_AVCencInfo \*cencInfo, uint32\_t encryptedBlockCount, uint32\_t skippedBlockCount, uint32\_t firstEncryptedOffset, uint32\_t subsampleCount, DrmSubsample \*subsamples)](capi-native-cencinfo-h.md#oh_avcencinfo_setsubsampleinfo) | 设置cencInfo的subsamples信息。 |
| [OH\_AVErrCode OH\_AVCencInfo\_SetMode(OH\_AVCencInfo \*cencInfo, enum DrmCencInfoMode mode)](capi-native-cencinfo-h.md#oh_avcencinfo_setmode) | 设置cencInfo的模式。 |
| [OH\_AVErrCode OH\_AVCencInfo\_SetAVBuffer(OH\_AVCencInfo \*cencInfo, OH\_AVBuffer \*buffer)](capi-native-cencinfo-h.md#oh_avcencinfo_setavbuffer) | 将cencInfo设置到AVBuffer。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### DrmCencAlgorithm

PhonePC/2in1TabletTVWearable

```
1. enum DrmCencAlgorithm
```

**描述**

Drm CENC算法类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| DRM\_ALG\_CENC\_UNENCRYPTED = 0x0 | 不加密算法。 |
| DRM\_ALG\_CENC\_AES\_CTR = 0x1 | AES CTR算法。 |
| DRM\_ALG\_CENC\_AES\_WV = 0x2 | AES WV算法。 |
| DRM\_ALG\_CENC\_AES\_CBC = 0x3 | AES CBC算法。 |
| DRM\_ALG\_CENC\_SM4\_CBC = 0x4 | SM4 CBC算法。 |
| DRM\_ALG\_CENC\_SM4\_CTR = 0x5 | SM4 CTR算法。 |

### DrmCencInfoMode

PhonePC/2in1TabletTVWearable

```
1. enum DrmCencInfoMode
```

**描述**

枚举类型，表示cencInfo中keyId/iv/subsample信息是否设置。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| DRM\_CENC\_INFO\_KEY\_IV\_SUBSAMPLES\_SET = 0x0 | keyId/iv/subsample信息已设置。 |
| DRM\_CENC\_INFO\_KEY\_IV\_SUBSAMPLES\_NOT\_SET = 0x1 | keyId/iv/subsample信息未设置。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AVCencInfo\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_AVCencInfo *OH_AVCencInfo_Create()
```

**描述**

创建用于设置cencInfo的OH\_AVCencInfo实例。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVCencInfo](capi-multimedia-drm-oh-avcencinfo.md) \* | 返回新创建的OH\_AVCencInfo对象。如果返回nullptr，则表示创建对象失败。  可能失败的原因：应用程序地址空间已满，或者对象中的数据初始化失败。 |

### OH\_AVCencInfo\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVCencInfo_Destroy(OH_AVCencInfo *cencInfo)
```

**描述**

销毁OH\_AVCencInfo实例并释放内部资源。

同一个实例只能销毁一次。在再次创建实例之前，不应使用该实例。建议在实例销毁成功后立即将实例指针设置为nullptr。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCencInfo](capi-multimedia-drm-oh-avcencinfo.md) \*cencInfo | 指向OH\_AVCencInfo实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：cencInfo为空。 |

### OH\_AVCencInfo\_SetAlgorithm()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVCencInfo_SetAlgorithm(OH_AVCencInfo *cencInfo, enum DrmCencAlgorithm algo)
```

**描述**

设置cencInfo加密算法。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCencInfo](capi-multimedia-drm-oh-avcencinfo.md) \*cencInfo | 指向OH\_AVCencInfo实例的指针。 |
| [enum DrmCencAlgorithm](capi-native-cencinfo-h.md#drmcencalgorithm) algo | 加密算法模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：cencInfo为空。 |

### OH\_AVCencInfo\_SetKeyIdAndIv()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVCencInfo_SetKeyIdAndIv(OH_AVCencInfo *cencInfo, uint8_t *keyId, uint32_t keyIdLen, uint8_t *iv, uint32_t ivLen)
```

**描述**

设置cencInfo的keyId和iv。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCencInfo](capi-multimedia-drm-oh-avcencinfo.md) \*cencInfo | 指向OH\_AVCencInfo实例的指针。 |
| uint8\_t \*keyId | Key标识。 |
| uint32\_t keyIdLen | Key标识长度。 |
| uint8\_t \*iv | 初始化向量。 |
| uint32\_t ivLen | 初始化向量长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：cencInfo为空、keyId为空、keyIdLen != DRM\_KEY\_ID\_SIZE、iv是空、ivLen != DRM\_KEY\_IV\_SIZE、keyId拷贝失败，或者iv拷贝失败。 |

### OH\_AVCencInfo\_SetSubsampleInfo()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVCencInfo_SetSubsampleInfo(OH_AVCencInfo *cencInfo, uint32_t encryptedBlockCount, uint32_t skippedBlockCount, uint32_t firstEncryptedOffset, uint32_t subsampleCount, DrmSubsample *subsamples)
```

**描述**

设置cencInfo的subsamples信息。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCencInfo](capi-multimedia-drm-oh-avcencinfo.md) \*cencInfo | 指向OH\_AVCencInfo实例的指针。 |
| uint32\_t encryptedBlockCount | 加密块的数量。 |
| uint32\_t skippedBlockCount | 不加密块的数量。 |
| uint32\_t firstEncryptedOffset | 第一个加密有效负载的偏移量。 |
| uint32\_t subsampleCount | Subsample数量。 |
| [DrmSubsample](capi-multimedia-drm-drmsubsample.md) \*subsamples | Subsample内容集。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：cencInfo为空、subsampleCount > DRM\_KEY\_MAX\_SUB\_SAMPLE\_NUM，或者subsamples为空。 |

### OH\_AVCencInfo\_SetMode()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVCencInfo_SetMode(OH_AVCencInfo *cencInfo, enum DrmCencInfoMode mode)
```

**描述**

设置cencInfo的模式。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCencInfo](capi-multimedia-drm-oh-avcencinfo.md) \*cencInfo | 指向OH\_AVCencInfo实例的指针。 |
| [enum DrmCencInfoMode](capi-native-cencinfo-h.md#drmcencinfomode) mode | cencInfo模式，指示是否设置了keyId/iv/subsample。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：cencInfo为空。 |

### OH\_AVCencInfo\_SetAVBuffer()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVCencInfo_SetAVBuffer(OH_AVCencInfo *cencInfo, OH_AVBuffer *buffer)
```

**描述**

将cencInfo设置到AVBuffer。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCencInfo](capi-multimedia-drm-oh-avcencinfo.md) \*cencInfo | 指向OH\_AVCencInfo实例的指针。 |
| [OH\_AVBuffer](capi-core-oh-avbuffer.md) \*buffer | 携带数据的帧buffer。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：cencInfo为空、buffer为空、buffer->buffer\_为空，或者buffer->buffer\_->meta\_为空。 |
