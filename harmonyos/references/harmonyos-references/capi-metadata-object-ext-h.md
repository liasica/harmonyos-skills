---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-metadata-object-ext-h
title: metadata_object_ext.h
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 头文件 > metadata_object_ext.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3adb11a6443d854e12386b44d66d8fe499454844d76e01a478b686c8bbb196d2
---

## 概述

声明元数据对象扩展概念。

**引用文件：** <ohcamera/metadata\_object\_ext.h>

**库：** libohcamera.so

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 26.0.0

**相关模块：** [OH\_Camera](capi-oh-camera.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Camera\_MetadataObjectExt](capi-oh-camera-oh-camera-metadataobjectext.md) | OH\_Camera\_MetadataObjectExt | 元数据对象扩展结构体。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [Camera\_ErrorCode OH\_MetadataObjectExt\_GetMetadataObjectType(const OH\_Camera\_MetadataObjectExt\* metadataObjectExt, Camera\_MetadataObjectType\* type)](capi-metadata-object-ext-h.md#oh_metadataobjectext_getmetadataobjecttype) | 获取元数据对象类型。 |
| [Camera\_ErrorCode OH\_MetadataObjectExt\_GetTimestamp(const OH\_Camera\_MetadataObjectExt\* metadataObjectExt, int64\_t\* timestamp)](capi-metadata-object-ext-h.md#oh_metadataobjectext_gettimestamp) | 获取元数据对象的时间戳。 |
| [Camera\_ErrorCode OH\_MetadataObjectExt\_GetBoundingBox(const OH\_Camera\_MetadataObjectExt\* metadataObjectExt, OH\_Camera\_Rect\_Ext\* boundingBox)](capi-metadata-object-ext-h.md#oh_metadataobjectext_getboundingbox) | 获取元数据对象的边界框。 |
| [Camera\_ErrorCode OH\_MetadataObjectExt\_GetPitchAngle(const OH\_Camera\_MetadataObjectExt\* metadataObjectExt, float\* pitchAngle)](capi-metadata-object-ext-h.md#oh_metadataobjectext_getpitchangle) | 获取元数据对象（如人脸）的俯仰角度。取值范围为[-90, 90]，以向下为正方向。 |
| [Camera\_ErrorCode OH\_MetadataObjectExt\_GetYawAngle(const OH\_Camera\_MetadataObjectExt\* metadataObjectExt, float\* yawAngle)](capi-metadata-object-ext-h.md#oh_metadataobjectext_getyawangle) | 获取元数据对象（如人脸）的左右旋转角度。取值范围为[-90, 90]，以向右为正方向。 |
| [Camera\_ErrorCode OH\_MetadataObjectExt\_GetRollAngle(const OH\_Camera\_MetadataObjectExt\* metadataObjectExt, float\* rollAngle)](capi-metadata-object-ext-h.md#oh_metadataobjectext_getrollangle) | 获取元数据对象（如人脸）的平面内旋转角度。取值范围为[-180, 180]，以顺时针方向为正方向。 |
| [Camera\_ErrorCode OH\_MetadataObjectExt\_GetLeftEyeBoundingBox(const OH\_Camera\_MetadataObjectExt\* metadataObjectExt, OH\_Camera\_Rect\_Ext\* boundingBox)](capi-metadata-object-ext-h.md#oh_metadataobjectext_getlefteyeboundingbox) | 获取元数据对象（如人脸）的左眼边界框。 |
| [Camera\_ErrorCode OH\_MetadataObjectExt\_GetRightEyeBoundingBox(const OH\_Camera\_MetadataObjectExt\* metadataObjectExt, OH\_Camera\_Rect\_Ext\* boundingBox)](capi-metadata-object-ext-h.md#oh_metadataobjectext_getrighteyeboundingbox) | 获取元数据对象（如人脸）的右眼边界框。 |
| [Camera\_ErrorCode OH\_MetadataObjectExt\_GetEmotion(const OH\_Camera\_MetadataObjectExt\* metadataObjectExt, OH\_Camera\_MetadataObjectEmotion\* emotion)](capi-metadata-object-ext-h.md#oh_metadataobjectext_getemotion) | 获取元数据对象（如人脸）的情绪类型。 |
| [void OH\_MetadataObjectExt\_Destroy(OH\_Camera\_MetadataObjectExt\*\* metadataObjectExt, uint32\_t objectCount)](capi-metadata-object-ext-h.md#oh_metadataobjectext_destroy) | 销毁OH\_Camera\_MetadataObjectExt实例数组。 |
| [bool OH\_MetadataObjectExt\_IsLockFocusTracked(const OH\_Camera\_MetadataObjectExt\* metadataObjectExt)](capi-metadata-object-ext-h.md#oh_metadataobjectext_islockfocustracked) | 查询焦点是否已锁定跟踪。 |

## 函数说明

### OH\_MetadataObjectExt\_GetMetadataObjectType()

```c
Camera_ErrorCode OH_MetadataObjectExt_GetMetadataObjectType(const OH_Camera_MetadataObjectExt* metadataObjectExt, Camera_MetadataObjectType* type)
```

**描述**

获取元数据对象类型。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Camera\_MetadataObjectExt](capi-oh-camera-oh-camera-metadataobjectext.md)\* metadataObjectExt | OH\_Camera\_MetadataObjectExt实例的指针。 |
| [Camera\_MetadataObjectType](capi-camera-h.md#camera_metadataobjecttype)\* type | 元数据对象类型的指针，是一个Camera\_MetadataObjectType实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：操作成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或参数类型错误。 |

### OH\_MetadataObjectExt\_GetTimestamp()

```c
Camera_ErrorCode OH_MetadataObjectExt_GetTimestamp(const OH_Camera_MetadataObjectExt* metadataObjectExt, int64_t* timestamp)
```

**描述**

获取元数据对象的时间戳。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Camera\_MetadataObjectExt](capi-oh-camera-oh-camera-metadataobjectext.md)\* metadataObjectExt | OH\_Camera\_MetadataObjectExt实例的指针。 |
| int64\_t\* timestamp | 存储时间戳的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：操作成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或参数类型错误。 |

### OH\_MetadataObjectExt\_GetBoundingBox()

```c
Camera_ErrorCode OH_MetadataObjectExt_GetBoundingBox(const OH_Camera_MetadataObjectExt* metadataObjectExt, OH_Camera_Rect_Ext* boundingBox)
```

**描述**

获取元数据对象的边界框。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Camera\_MetadataObjectExt](capi-oh-camera-oh-camera-metadataobjectext.md)\* metadataObjectExt | OH\_Camera\_MetadataObjectExt实例的指针。 |
| [OH\_Camera\_Rect\_Ext](capi-oh-camera-oh-camera-rect-ext.md)\* boundingBox | 元数据对象边界框的指针，是一个OH\_Camera\_Rect\_Ext实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：操作成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或参数类型错误。 |

### OH\_MetadataObjectExt\_GetPitchAngle()

```c
Camera_ErrorCode OH_MetadataObjectExt_GetPitchAngle(const OH_Camera_MetadataObjectExt* metadataObjectExt, float* pitchAngle)
```

**描述**

获取元数据对象（如人脸）的俯仰角度。取值范围为[-90, 90]，以向下为正方向。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Camera\_MetadataObjectExt](capi-oh-camera-oh-camera-metadataobjectext.md)\* metadataObjectExt | OH\_Camera\_MetadataObjectExt实例的指针。 |
| float\* pitchAngle | 存储俯仰角的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：操作成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或参数类型错误。  CAMERA\_ERROR\_OPTIONAL\_PROPERTY\_NOT\_EXIST：可选属性不存在。 |

### OH\_MetadataObjectExt\_GetYawAngle()

```c
Camera_ErrorCode OH_MetadataObjectExt_GetYawAngle(const OH_Camera_MetadataObjectExt* metadataObjectExt, float* yawAngle)
```

**描述**

获取元数据对象（如人脸）的左右旋转角度。取值范围为[-90, 90]，以向右为正方向。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Camera\_MetadataObjectExt](capi-oh-camera-oh-camera-metadataobjectext.md)\* metadataObjectExt | OH\_Camera\_MetadataObjectExt实例的指针。 |
| float\* yawAngle | 存储左右旋转角度的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：操作成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或参数类型错误。  CAMERA\_ERROR\_OPTIONAL\_PROPERTY\_NOT\_EXIST：可选属性不存在。 |

### OH\_MetadataObjectExt\_GetRollAngle()

```c
Camera_ErrorCode OH_MetadataObjectExt_GetRollAngle(const OH_Camera_MetadataObjectExt* metadataObjectExt, float* rollAngle)
```

**描述**

获取元数据对象（如人脸）的平面内旋转角度。取值范围为[-180, 180]，以顺时针方向为正方向。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Camera\_MetadataObjectExt](capi-oh-camera-oh-camera-metadataobjectext.md)\* metadataObjectExt | OH\_Camera\_MetadataObjectExt实例的指针。 |
| float\* rollAngle | 存储翻滚角的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：操作成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或参数类型错误。  CAMERA\_ERROR\_OPTIONAL\_PROPERTY\_NOT\_EXIST：可选属性不存在。 |

### OH\_MetadataObjectExt\_GetLeftEyeBoundingBox()

```c
Camera_ErrorCode OH_MetadataObjectExt_GetLeftEyeBoundingBox(const OH_Camera_MetadataObjectExt* metadataObjectExt, OH_Camera_Rect_Ext* boundingBox)
```

**描述**

获取元数据对象（如人脸）的左眼边界框。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Camera\_MetadataObjectExt](capi-oh-camera-oh-camera-metadataobjectext.md)\* metadataObjectExt | OH\_Camera\_MetadataObjectExt实例的指针。 |
| [OH\_Camera\_Rect\_Ext](capi-oh-camera-oh-camera-rect-ext.md)\* boundingBox | 元数据对象边界框的指针，是一个OH\_Camera\_Rect\_Ext实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：操作成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或参数类型错误。  CAMERA\_ERROR\_OPTIONAL\_PROPERTY\_NOT\_EXIST：可选属性不存在。 |

### OH\_MetadataObjectExt\_GetRightEyeBoundingBox()

```c
Camera_ErrorCode OH_MetadataObjectExt_GetRightEyeBoundingBox(const OH_Camera_MetadataObjectExt* metadataObjectExt, OH_Camera_Rect_Ext* boundingBox)
```

**描述**

获取元数据对象（如人脸）的右眼边界框。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Camera\_MetadataObjectExt](capi-oh-camera-oh-camera-metadataobjectext.md)\* metadataObjectExt | OH\_Camera\_MetadataObjectExt实例的指针。 |
| [OH\_Camera\_Rect\_Ext](capi-oh-camera-oh-camera-rect-ext.md)\* boundingBox | 元数据对象边界框的指针，是一个OH\_Camera\_Rect\_Ext实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：操作成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或参数类型错误。  CAMERA\_ERROR\_OPTIONAL\_PROPERTY\_NOT\_EXIST：可选属性不存在。 |

### OH\_MetadataObjectExt\_GetEmotion()

```c
Camera_ErrorCode OH_MetadataObjectExt_GetEmotion(const OH_Camera_MetadataObjectExt* metadataObjectExt, OH_Camera_MetadataObjectEmotion* emotion)
```

**描述**

获取元数据对象（如人脸）的情绪类型。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Camera\_MetadataObjectExt](capi-oh-camera-oh-camera-metadataobjectext.md)\* metadataObjectExt | OH\_Camera\_MetadataObjectExt实例的指针。 |
| [OH\_Camera\_MetadataObjectEmotion](capi-camera-h.md#oh_camera_metadataobjectemotion)\* emotion | 存储情绪类型的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：操作成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或参数类型错误。  CAMERA\_ERROR\_OPTIONAL\_PROPERTY\_NOT\_EXIST：可选属性不存在。 |

### OH\_MetadataObjectExt\_Destroy()

```c
void OH_MetadataObjectExt_Destroy(OH_Camera_MetadataObjectExt** metadataObjectExt, uint32_t objectCount)
```

**描述**

销毁OH\_Camera\_MetadataObjectExt实例数组。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Camera\_MetadataObjectExt](capi-oh-camera-oh-camera-metadataobjectext.md)\*\* metadataObjectExt | OH\_Camera\_MetadataObjectExt实例数组的指针。 |
| uint32\_t objectCount | 要销毁的元数据对象数量。 |

### OH\_MetadataObjectExt\_IsLockFocusTracked()

```c
bool OH_MetadataObjectExt_IsLockFocusTracked(const OH_Camera_MetadataObjectExt* metadataObjectExt)
```

**描述**

查询焦点是否已锁定跟踪。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Camera\_MetadataObjectExt](capi-oh-camera-oh-camera-metadataobjectext.md)\* metadataObjectExt | OH\_Camera\_MetadataObjectExt实例指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 焦点是否已锁定跟踪，返回true表示已锁定，返回false表示未锁定。 |
