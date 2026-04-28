---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-buffer-common-h
title: buffer_common.h
category: harmonyos-references
scraped_at: 2026-04-28T08:14:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fad233e78e5128fedf61257cb162ee0809c74ed7b9233a7ea1d3d0fa62e6cc4b
---

## 概述

PhonePC/2in1TabletTVWearable

提供NativeBuffer模块的公共类型定义。

**引用文件：** <native\_buffer/buffer\_common.h>

**库：** libnative\_buffer.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 12

**相关模块：** [OH\_NativeBuffer](capi-oh-nativebuffer.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_NativeBuffer\_ColorXY](capi-oh-nativebuffer-oh-nativebuffer-colorxy.md) | OH\_NativeBuffer\_ColorXY | 表示基色的X和Y坐标。 |
| [OH\_NativeBuffer\_Smpte2086](capi-oh-nativebuffer-oh-nativebuffer-smpte2086.md) | OH\_NativeBuffer\_Smpte2086 | 表示smpte2086静态元数据。 |
| [OH\_NativeBuffer\_Cta861](capi-oh-nativebuffer-oh-nativebuffer-cta861.md) | OH\_NativeBuffer\_Cta861 | 表示CTA-861.3静态元数据。 |
| [OH\_NativeBuffer\_StaticMetadata](api-oh-nativebuffer-oh-nativebuffer-staticmetadata.md) | OH\_NativeBuffer\_StaticMetadata | 表示HDR静态元数据。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_NativeBuffer\_ColorSpace](capi-buffer-common-h.md#oh_nativebuffer_colorspace) | OH\_NativeBuffer\_ColorSpace | OH\_NativeBuffer的颜色空间。 |
| [OH\_NativeBuffer\_MetadataType](capi-buffer-common-h.md#oh_nativebuffer_metadatatype) | OH\_NativeBuffer\_MetadataType | OH\_NativeBuffer的图像标准。 |
| [OH\_NativeBuffer\_MetadataKey](capi-buffer-common-h.md#oh_nativebuffer_metadatakey) | OH\_NativeBuffer\_MetadataKey | 表示OH\_NativeBuffer的描述信息的键值，如HDR元数据，ROI元数据等。 |
| [OH\_NativeBuffer\_Format](capi-buffer-common-h.md#oh_nativebuffer_format) | OH\_NativeBuffer\_Format | OH\_NativeBuffer格式的枚举。 |
| [OH\_NativeBuffer\_TransformType](capi-buffer-common-h.md#oh_nativebuffer_transformtype) | OH\_NativeBuffer\_TransformType | OH\_NativeBuffer转换类型的枚举。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_NativeBuffer\_ColorSpace

PhonePC/2in1TabletTVWearable

```
1. enum OH_NativeBuffer_ColorSpace
```

**描述**

OH\_NativeBuffer的颜色空间。

从API version 12开始，此枚举由native\_buffer.h移动至此头文件。

API version 12之前，使用该枚举请引用native\_buffer.h头文件；从API version 12开始，引用native\_buffer.h或buffer\_common.h均可正常使用该枚举。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| OH\_COLORSPACE\_NONE | 无颜色空间。 |
| OH\_COLORSPACE\_BT601\_EBU\_FULL | 色域范围为BT601\_P，传递函数为BT709，转换矩阵为BT601\_P，数据范围为RANGE\_FULL。 |
| OH\_COLORSPACE\_BT601\_SMPTE\_C\_FULL | 色域范围为BT601\_N，传递函数为BT709，转换矩阵为BT601\_N，数据范围为RANGE\_FULL。 |
| OH\_COLORSPACE\_BT709\_FULL | 色域范围为BT709，传递函数为BT709，转换矩阵为BT709，数据范围为RANGE\_FULL。 |
| OH\_COLORSPACE\_BT2020\_HLG\_FULL | 色域范围为BT2020，传递函数为HLG，转换矩阵为BT2020，数据范围为RANGE\_FULL。 |
| OH\_COLORSPACE\_BT2020\_PQ\_FULL | 色域范围为BT2020，传递函数为PQ，转换矩阵为BT2020，数据范围为RANGE\_FULL。 |
| OH\_COLORSPACE\_BT601\_EBU\_LIMIT | 色域范围为BT601\_P，传递函数为BT709，转换矩阵为BT601\_P，数据范围为RANGE\_LIMITED。 |
| OH\_COLORSPACE\_BT601\_SMPTE\_C\_LIMIT | 色域范围为BT601\_N，传递函数为BT709，转换矩阵为BT601\_N，数据范围为RANGE\_LIMITED。 |
| OH\_COLORSPACE\_BT709\_LIMIT | 色域范围为BT709，传递函数为BT709，转换矩阵为BT709，数据范围为RANGE\_LIMITED。 |
| OH\_COLORSPACE\_BT2020\_HLG\_LIMIT | 色域范围为BT2020，传递函数为HLG，转换矩阵为BT2020，数据范围为RANGE\_LIMITED。 |
| OH\_COLORSPACE\_BT2020\_PQ\_LIMIT | 色域范围为BT2020，传递函数为PQ，转换矩阵为BT2020，数据范围为RANGE\_LIMITED。 |
| OH\_COLORSPACE\_SRGB\_FULL | 色域范围为SRGB，传递函数为SRGB，转换矩阵为BT601\_N，数据范围为RANGE\_FULL。 |
| OH\_COLORSPACE\_P3\_FULL | 色域范围为P3\_D65，传递函数为SRGB，转换矩阵为P3，数据范围为RANGE\_FULL。 |
| OH\_COLORSPACE\_P3\_HLG\_FULL | 色域范围为P3\_D65，传递函数为HLG，转换矩阵为P3，数据范围为RANGE\_FULL。 |
| OH\_COLORSPACE\_P3\_PQ\_FULL | 色域范围为P3\_D65，传递函数为PQ，转换矩阵为P3，数据范围为RANGE\_FULL。 |
| OH\_COLORSPACE\_ADOBERGB\_FULL | 色域范围为ADOBERGB，传递函数为ADOBERGB，转换矩阵为ADOBERGB，数据范围为RANGE\_FULL。 |
| OH\_COLORSPACE\_SRGB\_LIMIT | 色域范围为SRGB，传递函数为SRGB，转换矩阵为BT601\_N，数据范围为RANGE\_LIMITED。 |
| OH\_COLORSPACE\_P3\_LIMIT | 色域范围为P3\_D65，传递函数为SRGB，转换矩阵为P3，数据范围为RANGE\_LIMITED。 |
| OH\_COLORSPACE\_P3\_HLG\_LIMIT | 色域范围为P3\_D65，传递函数为HLG，转换矩阵为P3，数据范围为RANGE\_LIMITED。 |
| OH\_COLORSPACE\_P3\_PQ\_LIMIT | 色域范围为P3\_D65，传递函数为PQ，转换矩阵为P3，数据范围为RANGE\_LIMITED。 |
| OH\_COLORSPACE\_ADOBERGB\_LIMIT | 色域范围为ADOBERGB，传递函数为ADOBERGB，转换矩阵为ADOBERGB，数据范围为RANGE\_LIMITED。 |
| OH\_COLORSPACE\_LINEAR\_SRGB | 色域范围为SRGB，传递函数为LINEAR。 |
| OH\_COLORSPACE\_LINEAR\_BT709 | 等同于 OH\_COLORSPACE\_LINEAR\_SRGB。 |
| OH\_COLORSPACE\_LINEAR\_P3 | 色域范围为P3\_D65，传递函数为LINEAR。 |
| OH\_COLORSPACE\_LINEAR\_BT2020 | 色域范围为BT2020，传递函数为LINEAR。 |
| OH\_COLORSPACE\_DISPLAY\_SRGB | 等同于OH\_COLORSPACE\_SRGB\_FULL。 |
| OH\_COLORSPACE\_DISPLAY\_P3\_SRGB | 等同于OH\_COLORSPACE\_P3\_FULL。 |
| OH\_COLORSPACE\_DISPLAY\_P3\_HLG | 等同于OH\_COLORSPACE\_P3\_HLG\_FULL。 |
| OH\_COLORSPACE\_DISPLAY\_P3\_PQ | 等同于OH\_COLORSPACE\_P3\_PQ\_FULL。 |
| OH\_COLORSPACE\_DISPLAY\_BT2020\_SRGB | 色域范围为BT2020，传递函数为SRGB，转换矩阵为BT2020，数据范围为RANGE\_FULL。 |
| OH\_COLORSPACE\_DISPLAY\_BT2020\_HLG | 等同于 OH\_COLORSPACE\_BT2020\_HLG\_FULL。 |
| OH\_COLORSPACE\_DISPLAY\_BT2020\_PQ | 等同于OH\_COLORSPACE\_BT2020\_PQ\_FULL。 |

### OH\_NativeBuffer\_MetadataType

PhonePC/2in1TabletTVWearable

```
1. enum OH_NativeBuffer_MetadataType
```

**描述**

OH\_NativeBuffer的图像标准。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| OH\_VIDEO\_HDR\_HLG | 视频HLG。 |
| OH\_VIDEO\_HDR\_HDR10 | 视频HDR10。 |
| OH\_VIDEO\_HDR\_VIVID | 视频HDR VIVID。 |
| OH\_IMAGE\_HDR\_VIVID\_DUAL | 图片HDR VIVID DUAL。  **起始版本：** 22 |
| OH\_IMAGE\_HDR\_VIVID\_SINGLE | 图片HDR VIVID SINGLE。  **起始版本：** 22 |
| OH\_IMAGE\_HDR\_ISO\_DUAL | 图片HDR ISO DUAL。  **起始版本：** 23 |
| OH\_IMAGE\_HDR\_ISO\_SINGLE | 图片HDR ISO SINGLE。  **起始版本：** 23 |
| OH\_VIDEO\_NONE = -1 | 无元数据。  **起始版本：** 13 |

### OH\_NativeBuffer\_MetadataKey

PhonePC/2in1TabletTVWearable

```
1. enum OH_NativeBuffer_MetadataKey
```

**描述**

表示OH\_NativeBuffer的描述信息的键值，如HDR元数据，ROI元数据等。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| OH\_HDR\_METADATA\_TYPE | 元数据类型，其值见[OH\_NativeBuffer\_MetadataType](capi-buffer-common-h.md#oh_nativebuffer_metadatatype)，size为OH\_NativeBuffer\_MetadataType大小。 |
| OH\_HDR\_STATIC\_METADATA | 静态元数据，其值见[OH\_NativeBuffer\_StaticMetadata](api-oh-nativebuffer-oh-nativebuffer-staticmetadata.md)，size为OH\_NativeBuffer\_StaticMetadata大小。 |
| OH\_HDR\_DYNAMIC\_METADATA | 动态元数据，其值见视频流中SEI的字节流，size的取值范围为1-3000。 |
| OH\_REGION\_OF\_INTEREST\_METADATA | 视频编解码感兴趣区域（ROI）元数据，配置格式示例：“Top1,Left1-Bottom1,Right1=QpOffset1;Top2,Left2-Bottom2,Right2=QpOffset2;”。  每个ROI框由位置信息（Top,Left-Bottom,Right），编码质量偏移信息（QpOffset）组成，到分号结束。  ROI框的编码质量偏移信息可以缺省，缺省值为-3，缺省时配置示例：“Top1,Left1-Bottom1,Right1;Top2,Left2-Bottom2,Right2;”。  每组ROI元数据最多支持同时配置6个ROI，且其累计面积不超过全图的1/5。  该枚举值仅支持通过[OH\_NativeBuffer\_SetMetadataValue()](capi-native-buffer-h.md#oh_nativebuffer_setmetadatavalue)接口调用。  **起始版本：** 22 |

### OH\_NativeBuffer\_Format

PhonePC/2in1TabletTVWearable

```
1. enum OH_NativeBuffer_Format
```

**描述**

OH\_NativeBuffer格式的枚举。

从API version 22开始，此枚举由native\_buffer.h移动至此头文件。

API version 22之前，使用该枚举请引用native\_buffer.h头文件；从API version 22开始，引用native\_buffer.h或buffer\_common.h均可正常使用该枚举。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| NATIVEBUFFER\_PIXEL\_FMT\_CLUT8 = 0 | CLUT8格式。  **起始版本：** 12 |
| NATIVEBUFFER\_PIXEL\_FMT\_CLUT1 | CLUT1格式。  **起始版本：** 12 |
| NATIVEBUFFER\_PIXEL\_FMT\_CLUT4 | CLUT4格式。  **起始版本：** 12 |
| NATIVEBUFFER\_PIXEL\_FMT\_RGB\_565 = 3 | RGB565格式。 |
| NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_5658 | RGBA5658格式。 |
| NATIVEBUFFER\_PIXEL\_FMT\_RGBX\_4444 | RGBX4444格式。 |
| NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_4444 | RGBA4444格式。 |
| NATIVEBUFFER\_PIXEL\_FMT\_RGB\_444 | RGB444格式。 |
| NATIVEBUFFER\_PIXEL\_FMT\_RGBX\_5551 | RGBX5551格式。 |
| NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_5551 | RGBA5551格式。 |
| NATIVEBUFFER\_PIXEL\_FMT\_RGB\_555 | RGB555格式。 |
| NATIVEBUFFER\_PIXEL\_FMT\_RGBX\_8888 | RGBX8888格式。 |
| NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888 | RGBA8888格式。 |
| NATIVEBUFFER\_PIXEL\_FMT\_RGB\_888 | RGB888格式。 |
| NATIVEBUFFER\_PIXEL\_FMT\_BGR\_565 | BGR565格式。 |
| NATIVEBUFFER\_PIXEL\_FMT\_BGRX\_4444 | BGRX4444格式。 |
| NATIVEBUFFER\_PIXEL\_FMT\_BGRA\_4444 | BGRA4444格式。 |
| NATIVEBUFFER\_PIXEL\_FMT\_BGRX\_5551 | BGRX5551格式。 |
| NATIVEBUFFER\_PIXEL\_FMT\_BGRA\_5551 | BGRA5551格式。 |
| NATIVEBUFFER\_PIXEL\_FMT\_BGRX\_8888 | BGRX8888格式。 |
| NATIVEBUFFER\_PIXEL\_FMT\_BGRA\_8888 | BGRA8888格式。 |
| NATIVEBUFFER\_PIXEL\_FMT\_YUV\_422\_I | YUV422 interleaved 格式。  **起始版本：** 12 |
| NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_422\_SP | YCBCR422 semi-planar 格式。  **起始版本：** 12 |
| NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_422\_SP | YCRCB422 semi-planar 格式。  **起始版本：** 12 |
| NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP | YCBCR420 semi-planar 格式。  **起始版本：** 12 |
| NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP | YCRCB420 semi-planar 格式。  **起始版本：** 12 |
| NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_422\_P | YCBCR422 planar 格式。  **起始版本：** 12 |
| NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_422\_P | YCRCB422 planar 格式。  **起始版本：** 12 |
| NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_P | YCBCR420 planar 格式。  **起始版本：** 12 |
| NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_P | YCRCB420 planar 格式。  **起始版本：** 12 |
| NATIVEBUFFER\_PIXEL\_FMT\_YUYV\_422\_PKG | YUYV422 packed 格式。  **起始版本：** 12 |
| NATIVEBUFFER\_PIXEL\_FMT\_UYVY\_422\_PKG | UYVY422 packed 格式。  **起始版本：** 12 |
| NATIVEBUFFER\_PIXEL\_FMT\_YVYU\_422\_PKG | YVYU422 packed 格式。  **起始版本：** 12 |
| NATIVEBUFFER\_PIXEL\_FMT\_VYUY\_422\_PKG | VYUY422 packed 格式。  **起始版本：** 12 |
| NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 | RGBA\_1010102 packed 格式。  **起始版本：** 12 |
| NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010 | YCBCR420 semi-planar 10bit packed 格式。  **起始版本：** 12 |
| NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010 | YCRCB420 semi-planar 10bit packed 格式。  **起始版本：** 12 |
| NATIVEBUFFER\_PIXEL\_FMT\_RAW10 | Raw 10bit packed 格式。  **起始版本：** 12 |
| NATIVEBUFFER\_PIXEL\_FMT\_BLOB | BLOB格式。  **起始版本：** 15 |
| NATIVEBUFFER\_PIXEL\_FMT\_RGBA16\_FLOAT | RGBA16 float格式。  **起始版本：** 15 |
| NATIVEBUFFER\_PIXEL\_FMT\_Y8 = 40 | Y8格式。  **起始版本：** 20 |
| NATIVEBUFFER\_PIXEL\_FMT\_Y16 = 41 | Y16格式。  **起始版本：** 20 |
| NATIVEBUFFER\_PIXEL\_FMT\_VENDER\_MASK = 0X7FFF0000 | vender mask 格式。  **起始版本：** 12 |
| NATIVEBUFFER\_PIXEL\_FMT\_BUTT = 0X7FFFFFFF | 无效格式。 |

### OH\_NativeBuffer\_TransformType

PhonePC/2in1TabletTVWearable

```
1. enum OH_NativeBuffer_TransformType
```

**描述**

OH\_NativeBuffer转换类型的枚举。

从API version 22开始，此枚举由native\_buffer.h移动至此头文件。

API version 22之前，使用该枚举请引用native\_buffer.h头文件；从API version 22开始，引用native\_buffer.h或buffer\_common.h均可正常使用该枚举。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| NATIVEBUFFER\_ROTATE\_NONE = 0 | 不旋转。 |
| NATIVEBUFFER\_ROTATE\_90 | 旋转90度。 |
| NATIVEBUFFER\_ROTATE\_180 | 旋转180度。 |
| NATIVEBUFFER\_ROTATE\_270 | 旋转270度。 |
| NATIVEBUFFER\_FLIP\_H | 水平翻转。 |
| NATIVEBUFFER\_FLIP\_V | 垂直翻转。 |
| NATIVEBUFFER\_FLIP\_H\_ROT90 | 水平翻转并旋转90度。 |
| NATIVEBUFFER\_FLIP\_V\_ROT90 | 垂直翻转并旋转90度。 |
| NATIVEBUFFER\_FLIP\_H\_ROT180 | 水平翻转并旋转180度。 |
| NATIVEBUFFER\_FLIP\_V\_ROT180 | 垂直翻转并旋转180度。 |
| NATIVEBUFFER\_FLIP\_H\_ROT270 | 水平翻转并旋转270度。 |
| NATIVEBUFFER\_FLIP\_V\_ROT270 | 垂直翻转并旋转270度。 |
