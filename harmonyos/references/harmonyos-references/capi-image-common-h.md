---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-common-h
title: image_common.h
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 头文件 > image_common.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f243075a5abb6765c322def922ebe84a5fb7149fcd95f32f70dc630a8141bf9c
---

## 概述

PhonePC/2in1TabletTVWearable

声明图像接口使用的公共枚举和结构体。

**引用文件：** <multimedia/image\_framework/image/image\_common.h>

**库：** libimage\_common.so

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Image\_Size](capi-image-nativemodule-image-size.md) | Image\_Size | 图像大小结构体。 |
| [Image\_Region](capi-image-nativemodule-image-region.md) | Image\_Region | 待解码的图像源区域结构体。 |
| [Image\_PositionArea](capi-image-nativemodule-image-positionarea.md) | Image\_PositionArea | 要读取或写入的图像像素区域。 |
| [Image\_Scale](capi-image-nativemodule-image-scale.md) | Image\_Scale | 图像缩放倍数。 |
| [Image\_String](capi-image-nativemodule-image-string.md) | Image\_String/Image\_MimeType | 字符串结构。 |
| [OH\_PictureMetadata](capi-image-nativemodule-oh-picturemetadata.md) | OH\_PictureMetadata | 声明用于Picture的元数据。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | Image\_ErrorCode | 错误码。 |
| [Image\_MetadataType](capi-image-common-h.md#image_metadatatype) | Image\_MetadataType | 定义元数据类型。 |
| [IMAGE\_ALLOCATOR\_MODE](capi-image-common-h.md#image_allocator_mode) | IMAGE\_ALLOCATOR\_MODE | pixelmap内存分配类型。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Image\_ErrorCode OH\_PictureMetadata\_Create(Image\_MetadataType metadataType, OH\_PictureMetadata \*\*metadata)](capi-image-common-h.md#oh_picturemetadata_create) | 创建OH\_PictureMetadata指针。 |
| [Image\_ErrorCode OH\_PictureMetadata\_GetProperty(OH\_PictureMetadata \*metadata, Image\_String \*key, Image\_String \*value)](capi-image-common-h.md#oh_picturemetadata_getproperty) | 根据key获取Metadata的单条属性。该接口获取到的value.data缺少字符串结束符'\0'，请谨慎使用。 |
| [Image\_ErrorCode OH\_PictureMetadata\_SetProperty(OH\_PictureMetadata \*metadata, Image\_String \*key, Image\_String \*value)](capi-image-common-h.md#oh_picturemetadata_setproperty) | 根据key修改Metadata的单条属性。 |
| [Image\_ErrorCode OH\_PictureMetadata\_GetPropertyWithNull(OH\_PictureMetadata \*metadata, Image\_String \*key, Image\_String \*value)](capi-image-common-h.md#oh_picturemetadata_getpropertywithnull) | 获取图片元数据的属性值。输出的value.data以字符串结束符'\0'结尾。 |
| [Image\_ErrorCode OH\_PictureMetadata\_Release(OH\_PictureMetadata \*metadata)](capi-image-common-h.md#oh_picturemetadata_release) | 释放OH\_PictureMetadata指针。 |
| [Image\_ErrorCode OH\_PictureMetadata\_Clone(OH\_PictureMetadata \*oldMetadata, OH\_PictureMetadata \*\*newMetadata)](capi-image-common-h.md#oh_picturemetadata_clone) | 拷贝元数据。 |

### 变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| static const char \* MIME\_TYPE\_BMP = "image/bmp" | bmp图片格式。  **起始版本：** 12 |
| static const char \* MIME\_TYPE\_JPEG = "image/jpeg" | jpeg图片格式。  **起始版本：** 12 |
| static const char \* MIME\_TYPE\_HEIC = "image/heic" | heic图片格式。  **起始版本：** 12 |
| static const char \* MIME\_TYPE\_PNG = "image/png" | png图片格式。  **起始版本：** 12 |
| static const char \* MIME\_TYPE\_WEBP = "image/webp" | webp图片格式。  **起始版本：** 12 |
| static const char \* MIME\_TYPE\_GIF = "image/gif" | gif图片格式。  **起始版本：** 12 |
| static const char \* MIME\_TYPE\_ICON = "image/x-icon" | ico图片格式。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_BITS\_PER\_SAMPLE = "BitsPerSample" | 每个像素比特数。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_ORIENTATION = "Orientation" | 图片方向。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_IMAGE\_LENGTH = "ImageLength" | 图片长度。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_IMAGE\_WIDTH = "ImageWidth" | 图片宽度。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_LATITUDE = "GPSLatitude" | 图片纬度。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_LONGITUDE = "GPSLongitude" | 图片经度。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_LATITUDE\_REF = "GPSLatitudeRef" | 纬度引用，例如N或S。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_LONGITUDE\_REF = "GPSLongitudeRef" | 经度引用，例如W或E。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_DATE\_TIME\_ORIGINAL = "DateTimeOriginal" | 拍摄时间，例如2022:09:06 15:48:00。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_EXPOSURE\_TIME = "ExposureTime" | 曝光时间，例如1/33 sec。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SCENE\_TYPE = "SceneType" | 拍摄场景模式，例如人像、风光、运动、夜景等。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_ISO\_SPEED\_RATINGS = "ISOSpeedRatings" | ISO感光度，例如400。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_F\_NUMBER = "FNumber" | 光圈值，例如f/1.8。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_COMPRESSED\_BITS\_PER\_PIXEL = "CompressedBitsPerPixel" | 用于压缩图像的压缩模式，单位为每像素位数。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_COMPRESSION = "Compression" | 图像压缩方案。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_PHOTOMETRIC\_INTERPRETATION = "PhotometricInterpretation" | 像素构成，例如RGB或YCbCr。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_STRIP\_OFFSETS = "StripOffsets" | 每个strip的字节偏移量。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SAMPLES\_PER\_PIXEL = "SamplesPerPixel" | 每个像素的分量数。由于该标准适用于RGB和YCbCr图像，因此该标签的值设置为3。在JPEG压缩数据中，使用JPEG标记代替该标签。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_ROWS\_PER\_STRIP = "RowsPerStrip" | 每个strip的图像数据行数。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_STRIP\_BYTE\_COUNTS = "StripByteCounts" | 每个图像数据带的总字节数。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_X\_RESOLUTION = "XResolution" | 图像宽度方向的分辨率。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_Y\_RESOLUTION = "YResolution" | 图像高度方向的分辨率。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_PLANAR\_CONFIGURATION = "PlanarConfiguration" | 表示像素组件的记录格式，chunky格式或是planar格式。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_RESOLUTION\_UNIT = "ResolutionUnit" | 用于测量XResolution和YResolution的单位。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_TRANSFER\_FUNCTION = "TransferFunction" | 图像的传递函数，通常用于颜色校正。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SOFTWARE = "Software" | 用于生成图像的软件的名称和版本。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_ARTIST = "Artist" | 创建图像的用户名称。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_WHITE\_POINT = "WhitePoint" | 图像的白点色度。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_PRIMARY\_CHROMATICITIES = "PrimaryChromaticities" | 图像的主要颜色的色度。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_YCBCR\_COEFFICIENTS = "YCbCrCoefficients" | 从RGB到YCbCr图像数据的转换矩阵系数。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_YCBCR\_SUB\_SAMPLING = "YCbCrSubSampling" | 色度分量与亮度分量的采样比率。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_YCBCR\_POSITIONING = "YCbCrPositioning" | 色度分量相对于亮度分量的位置。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_REFERENCE\_BLACK\_WHITE = "ReferenceBlackWhite" | 参考黑点值和参考白点值。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_COPYRIGHT = "Copyright" | 图像的版权信息。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_JPEG\_INTERCHANGE\_FORMAT = "JPEGInterchangeFormat" | JPEG压缩缩略图数据开始字节（SOI）的偏移。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_JPEG\_INTERCHANGE\_FORMAT\_LENGTH = "JPEGInterchangeFormatLength" | JPEG压缩缩略图数据的字节数。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_EXPOSURE\_PROGRAM = "ExposureProgram" | 拍照时相机用来设置曝光的程序的类别。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SPECTRAL\_SENSITIVITY = "SpectralSensitivity" | 表示所用相机的每个通道的光谱灵敏度。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_OECF = "OECF" | 表示ISO 14524中规定的光电转换函数（OECF）。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_EXIF\_VERSION = "ExifVersion" | 支持的Exif标准版本。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_DATE\_TIME\_DIGITIZED = "DateTimeDigitized" | 图像作为数字数据存储的日期和时间，格式为YYYY:MM:DD HH:MM:SS。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_COMPONENTS\_CONFIGURATION = "ComponentsConfiguration" | 压缩数据的特定信息。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SHUTTER\_SPEED\_VALUE = "ShutterSpeedValue" | 快门速度，以APEX（摄影曝光的加法系统）值表示。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_BRIGHTNESS\_VALUE = "BrightnessValue" | 图像的亮度值，以APEX单位表示。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_MAX\_APERTURE\_VALUE = "MaxApertureValue" | 最小F数镜头。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SUBJECT\_DISTANCE = "SubjectDistance" | 测量单位为米的主体距离。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SUBJECT\_AREA = "SubjectArea" | 该标签指示整个场景中主要主体的位置和区域。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_MAKER\_NOTE = "MakerNote" | Exif/DCF制造商使用的标签，用于记录任何所需信息。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SUBSEC\_TIME = "SubsecTime" | 用于为DateTime标签记录秒的分数的标签。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SUBSEC\_TIME\_ORIGINAL = "SubsecTimeOriginal" | 用于为DateTimeOriginal标签记录秒的分数的标签。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SUBSEC\_TIME\_DIGITIZED = "SubsecTimeDigitized" | 用于为DateTimeDigitized标签记录秒的分数的标签。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FLASHPIX\_VERSION = "FlashpixVersion" | 该标签表示FPXR文件支持的Flashpix格式版本，增强了设备兼容性。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_COLOR\_SPACE = "ColorSpace" | 色彩空间信息标签，通常记录为色彩空间指定符。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_RELATED\_SOUND\_FILE = "RelatedSoundFile" | 与图像数据相关的音频文件的名称。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FLASH\_ENERGY = "FlashEnergy" | 图像捕获时的闪光能量，以BCPS表示。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SPATIAL\_FREQUENCY\_RESPONSE = "SpatialFrequencyResponse" | 相机或输入设备的空间频率表。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FOCAL\_PLANE\_X\_RESOLUTION = "FocalPlaneXResolution" | 图像宽度中每FocalPlaneResolutionUnit的像素。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FOCAL\_PLANE\_Y\_RESOLUTION = "FocalPlaneYResolution" | 图像高度中每FocalPlaneResolutionUnit的像素。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FOCAL\_PLANE\_RESOLUTION\_UNIT = "FocalPlaneResolutionUnit" | 测量FocalPlaneXResolution和FocalPlaneYResolution的单位。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SUBJECT\_LOCATION = "SubjectLocation" | 主要对象相对于左边缘的位置。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_EXPOSURE\_INDEX = "ExposureIndex" | 捕获时选定的曝光指数。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SENSING\_METHOD = "SensingMethod" | 相机上的图像传感器类型。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FILE\_SOURCE = "FileSource" | 表明图像来源。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_CFA\_PATTERN = "CFAPattern" | 图像传感器的色彩滤光片（CFA）几何图案。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_CUSTOM\_RENDERED = "CustomRendered" | 指示图像数据上的特殊处理。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_EXPOSURE\_MODE = "ExposureMode" | 拍摄时设置的曝光模式。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_DIGITAL\_ZOOM\_RATIO = "DigitalZoomRatio" | 捕获时的数字变焦比率。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SCENE\_CAPTURE\_TYPE = "SceneCaptureType" | 捕获的场景类型。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GAIN\_CONTROL = "GainControl" | 整体图像增益调整的程度。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_CONTRAST = "Contrast" | 相机应用的对比度处理方向。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SATURATION = "Saturation" | 相机应用的饱和度处理方向。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SHARPNESS = "Sharpness" | 相机应用的锐度处理方向。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_DEVICE\_SETTING\_DESCRIPTION = "DeviceSettingDescription" | 特定相机模型的拍照条件信息。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SUBJECT\_DISTANCE\_RANGE = "SubjectDistanceRange" | 表示主体到相机的距离范围。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_IMAGE\_UNIQUE\_ID = "ImageUniqueID" | 为每张图片唯一分配的标识符。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_VERSION\_ID = "GPSVersionID" | GPSInfoIFD的版本。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_ALTITUDE\_REF = "GPSAltitudeRef" | 用于GPS高度的参照高度。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_ALTITUDE = "GPSAltitude" | 基于GPSAltitudeRef的高度。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_SATELLITES = "GPSSatellites" | 用于测量的GPS卫星。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_STATUS = "GPSStatus" | 录制图像时GPS接收器的状态。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_MEASURE\_MODE = "GPSMeasureMode" | GPS测量模式。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_DOP = "GPSDOP" | GPS DOP（数据精度等级）。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_SPEED\_REF = "GPSSpeedRef" | 用来表示GPS接收器移动速度的单位。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_SPEED = "GPSSpeed" | GPS接收器的移动速度。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_TRACK\_REF = "GPSTrackRef" | GPS接收机移动方向的参照。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_TRACK = "GPSTrack" | GPS接收机的移动方向。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_IMG\_DIRECTION\_REF = "GPSImgDirectionRef" | 图像方向的参照。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_IMG\_DIRECTION = "GPSImgDirection" | 拍摄时图像的方向。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_MAP\_DATUM = "GPSMapDatum" | GPS接收器使用的大地测量数据。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_DEST\_LATITUDE\_REF = "GPSDestLatitudeRef" | 目的地点的纬度参照。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_DEST\_LATITUDE = "GPSDestLatitude" | 目的地点的纬度。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_DEST\_LONGITUDE\_REF = "GPSDestLongitudeRef" | 目的地点的经度参照。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_PROCESSING\_METHOD = "GPSProcessingMethod" | 记录定位方法名的字符串。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_AREA\_INFORMATION = "GPSAreaInformation" | 记录GPS区域名的字符串。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_DIFFERENTIAL = "GPSDifferential" | 此字段表示GPS数据是否应用了差分校正，对于精确的位置准确性至关重要。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_BODY\_SERIAL\_NUMBER = "BodySerialNumber" | 相机机身的序列号。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_CAMERA\_OWNER\_NAME = "CameraOwnerName" | 相机所有者的姓名。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_COMPOSITE\_IMAGE = "CompositeImage" | 表示图像是否为合成图像。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_DNG\_VERSION = "DNGVersion" | DNG版本标签编码了符合DNG规范的四级版本号。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_DEST\_LONGITUDE = "GPSDestLongitude" | 目的地点的经度。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_DEST\_BEARING\_REF = "GPSDestBearingRef" | 指向目的地点的方位参照。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_DEST\_BEARING = "GPSDestBearing" | 目的地方位。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_DEST\_DISTANCE\_REF = "GPSDestDistanceRef" | 目标点距离的测量单位。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_DEST\_DISTANCE = "GPSDestDistance" | 到目的地点的距离。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_DEFAULT\_CROP\_SIZE = "DefaultCropSize" | DefaultCropSize指定了原始坐标中的最终图像大小，考虑了额外的边缘像素。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GAMMA = "Gamma" | 表示系数伽马的值。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_ISO\_SPEED\_LATITUDEYYY = "ISOSpeedLatitudeyyy" | 该标签指示摄像机或输入设备的ISO速度纬度yyy值，该值在ISO 12232中定义。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_ISO\_SPEED\_LATITUDEZZZ = "ISOSpeedLatitudezzz" | 该标签指示摄像机或输入设备的ISO速度纬度zzz值，该值在ISO 12232中定义。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_LENS\_MAKE = "LensMake" | 镜头的制造商。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_LENS\_MODEL = "LensModel" | 镜头的型号名称。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_LENS\_SERIAL\_NUMBER = "LensSerialNumber" | 镜头的序列号。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_LENS\_SPECIFICATION = "LensSpecification" | 使用的镜头规格。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_NEW\_SUBFILE\_TYPE = "NewSubfileType" | 在Exif中，"NewSubfileType"字段用于标识子文件的数据类型，如全分辨率图像、缩略图或多帧图像的一部分。其值是位掩码，0代表全分辨率图像，1代表缩略图，2代表多帧图像的一部分。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_OFFSET\_TIME = "OffsetTime" | 在Exif中，OffsetTime字段表示与UTC（协调世界时）的时间偏移，格式为±HH:MM，用于确定照片拍摄的本地时间。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_OFFSET\_TIME\_DIGITIZED = "OffsetTimeDigitized" | 此标签记录图像数字化时的UTC偏移量，有助于准确调整时间戳。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_OFFSET\_TIME\_ORIGINAL = "OffsetTimeOriginal" | 此标签记录原始图像创建时的UTC偏移量，对于时间敏感的应用至关重要。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SOURCE\_EXPOSURE\_TIMES\_OF\_COMPOSITE\_IMAGE = "SourceExposureTimesOfCompositeImage" | 合成图像的源图像曝光时间。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SOURCE\_IMAGE\_NUMBER\_OF\_COMPOSITE\_IMAGE = "SourceImageNumberOfCompositeImage" | 用于合成图像的源图像数量。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SUBFILE\_TYPE = "SubfileType" | 此标签指示此子文件中的数据类型。标签已弃用，请使用NewSubfileType替代。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_H\_POSITIONING\_ERROR = "GPSHPositioningError" | 此标签指示水平定位误差，单位为米。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_PHOTOGRAPHIC\_SENSITIVITY = "PhotographicSensitivity" | 此标签指示拍摄图像时相机或输入设备的灵敏度。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_BURST\_NUMBER = "HwMnoteBurstNumber" | 连拍次数。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FACE\_CONF = "HwMnoteFaceConf" | 人脸置信度。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FACE\_LEYE\_CENTER = "HwMnoteFaceLeyeCenter" | 左眼中心。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FACE\_MOUTH\_CENTER = "HwMnoteFaceMouthCenter" | 嘴中心。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FACE\_POINTER = "HwMnoteFacePointer" | 脸部指针。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FACE\_RECT = "HwMnoteFaceRect" | 脸部矩形。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FACE\_REYE\_CENTER = "HwMnoteFaceReyeCenter" | 右眼中心。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FACE\_SMILE\_SCORE = "HwMnoteFaceSmileScore" | FaceCount张人脸的笑脸分数。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FACE\_VERSION = "HwMnoteFaceVersion" | 人脸算法版本信息。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FRONT\_CAMERA = "HwMnoteFrontCamera" | 是否是前置相机自拍。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SCENE\_POINTER = "HwMnoteScenePointer" | 场景指针。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SCENE\_VERSION = "HwMnoteSceneVersion" | 场景算法版本信息。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_IS\_XMAGE\_SUPPORTED = "HwMnoteIsXmageSupported" | 是否支持XMAGE。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_XMAGE\_MODE = "HwMnoteXmageMode" | XMAGE水印模式。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_XMAGE\_LEFT = "HwMnoteXmageLeft" | 水印区域X1坐标。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_XMAGE\_TOP = "HwMnoteXmageTop" | 水印区域Y1坐标。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_XMAGE\_RIGHT = "HwMnoteXmageRight" | 水印区域X2坐标  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_XMAGE\_BOTTOM = "HwMnoteXmageBottom" | 水印区域Y2坐标。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_CLOUD\_ENHANCEMENT\_MODE = "HwMnoteCloudEnhancementMode" | 云增强模式。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_WIND\_SNAPSHOT\_MODE = "HwMnoteWindSnapshotMode" | 运动快拍模式。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GIF\_LOOP\_COUNT = "GIFLoopCount" | GIF图片循环次数。  **起始版本：** 12 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_X\_IN\_ORIGINAL = "XInOriginal" | 水印裁剪图左上角在原始图中的X坐标。  **起始版本：** 13 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_Y\_IN\_ORIGINAL = "YInOriginal" | 水印裁剪图左上角在原始图中的Y坐标。  **起始版本：** 13 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FRAGMENT\_WIDTH = "FragmentImageWidth" | 水印裁剪图的宽。  **起始版本：** 13 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FRAGMENT\_HEIGHT = "FragmentImageHeight" | 水印裁剪图的高。  **起始版本：** 13 |
| static const char \* IMAGE\_PROPERTY\_GIF\_DELAY\_TIME = "GifDelayTime" | GIF图片的每帧播放时长（单位为毫秒）。  **起始版本：** 20 |
| static const char \* IMAGE\_PROPERTY\_GIF\_DISPOSAL\_TYPE = "GifDisposalType" | GIF图片每帧的帧过渡模式。  **起始版本：** 20 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### Image\_ErrorCode

PhonePC/2in1TabletTVWearable

```
1. enum Image_ErrorCode
```

**描述**

错误码。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| IMAGE\_SUCCESS = 0 | 操作成功。 |
| IMAGE\_BAD\_PARAMETER = 401 | 无效参数。 |
| IMAGE\_UNSUPPORTED\_MIME\_TYPE = 7600101 | 不支持的MIME类型。 |
| IMAGE\_UNKNOWN\_MIME\_TYPE = 7600102 | 未知的MIME类型。 |
| IMAGE\_TOO\_LARGE = 7600103 | 过大的数据或图片。 |
| IMAGE\_GET\_IMAGE\_DATA\_FAILED = 7600104 | 获取图像数据失败。  **起始版本：** 23 |
| IMAGE\_DMA\_NOT\_EXIST = 7600173 | 内存不是DMA内存。 |
| IMAGE\_DMA\_OPERATION\_FAILED = 7600174 | DMA内存操作失败。 |
| IMAGE\_UNSUPPORTED\_OPERATION = 7600201 | 不支持的操作。 |
| IMAGE\_UNSUPPORTED\_METADATA = 7600202 | 不支持的metadata。 |
| IMAGE\_UNSUPPORTED\_CONVERSION = 7600203 | 不支持的转换。 |
| IMAGE\_INVALID\_REGION = 7600204 | 无效区域。 |
| IMAGE\_UNSUPPORTED\_MEMORY\_FORMAT = 7600205 | 不支持的内存格式。  **起始版本：** 13 |
| IMAGE\_INVALID\_PARAMETER = 7600206 | 无效参数。  **起始版本：** 19 |
| IMAGE\_UNSUPPORTED\_DATA\_FORMAT = 7600207 | 不支持的数据格式。  **起始版本：** 22 |
| IMAGE\_ALLOC\_FAILED = 7600301 | 申请内存失败。 |
| IMAGE\_COPY\_FAILED = 7600302 | 内存拷贝失败。 |
| IMAGE\_LOCK\_UNLOCK\_FAILED = 7600303 | 内存加锁或解锁失败。  **起始版本：** 15 |
| IMAGE\_INIT\_FAILED = 7600304 | 初始化失败。  **起始版本：** 22 |
| IMAGE\_CREATE\_PIXELMAP\_FAILED = 7600305 | 创建PixelMap失败。  **起始版本：** 22 |
| IMAGE\_ALLOCATOR\_MODE\_UNSUPPORTED = 7600501 | 不支持的内存分配器类型。例如，使用共享内存创建hdr图像。  DMA内存支持hdr元数据。  **起始版本：** 20 |
| IMAGE\_UNKNOWN\_ERROR = 7600901 | 未知错误。 |
| IMAGE\_BAD\_SOURCE = 7700101 | 解码数据源异常。 |
| IMAGE\_SOURCE\_UNSUPPORTED\_MIME\_TYPE = 7700102 | 图片解码中不支持的MIME类型。  **起始版本：** 15 |
| IMAGE\_SOURCE\_TOO\_LARGE = 7700103 | 图像过大。  **起始版本：** 15 |
| IMAGE\_SOURCE\_UNSUPPORTED\_ALLOCATOR\_TYPE = 7700201 | 不支持的分配器类型。例如，DMA支持HDR元数据，可以使用共享内存解码HDR图像。  **起始版本：** 15 |
| IMAGE\_SOURCE\_UNSUPPORTED\_METADATA = 7700202 | 不支持的元数据类型。如不支持的属性名或属性值非法。  **起始版本：** 23 |
| IMAGE\_SOURCE\_UNSUPPORTED\_OPTIONS = 7700203 | 不支持的选项。例如，无法将图像转换为所需的像素格式。  **起始版本：** 15 |
| IMAGE\_SOURCE\_INVALID\_PARAMETER = 7700204 | ImageSource的无效参数。  **起始版本：** 19 |
| IMAGE\_DECODE\_FAILED = 7700301 | 解码失败。 |
| IMAGE\_SOURCE\_ALLOC\_FAILED = 7700302 | 内存申请失败。  **起始版本：** 15 |
| IMAGE\_PACKER\_INVALID\_PARAMETER = 7800202 | ImagePacker的无效参数。  **起始版本：** 19 |
| IMAGE\_ENCODE\_FAILED = 7800301 | 编码失败。 |
| IMAGE\_RECEIVER\_INVALID\_PARAMETER = 7900201 | ImageReceiver的无效参数。  **起始版本：** 20 |

### Image\_MetadataType

PhonePC/2in1TabletTVWearable

```
1. enum Image_MetadataType
```

**描述**

定义元数据类型。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| EXIF\_METADATA = 1 | EXIF元数据。 |
| FRAGMENT\_METADATA = 2 | 水印裁剪图元数据。 |
| GIF\_METADATA = 5 | GIF图片元数据。  **起始版本：** 20 |

### IMAGE\_ALLOCATOR\_MODE

PhonePC/2in1TabletTVWearable

```
1. enum IMAGE_ALLOCATOR_MODE
```

**描述**

pixelmap内存分配类型。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| IMAGE\_ALLOCATOR\_MODE\_AUTO = 0 | 系统决定创建pixelmap时分配内存的类型。 |
| IMAGE\_ALLOCATOR\_MODE\_DMA = 1 | 分配DMA类型的内存Buffer。 |
| IMAGE\_ALLOCATOR\_MODE\_SHARED\_MEMORY = 2 | 使用共享内存创建pixelmap。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_PictureMetadata\_Create()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PictureMetadata_Create(Image_MetadataType metadataType, OH_PictureMetadata **metadata)
```

**描述**

创建OH\_PictureMetadata指针。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Image\_MetadataType](capi-image-common-h.md#image_metadatatype) metadataType | 元数据的类型。 |
| [OH\_PictureMetadata](capi-image-nativemodule-oh-picturemetadata.md) \*\*metadata | 被操作的OH\_PictureMetadata指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PictureMetadata\_GetProperty()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PictureMetadata_GetProperty(OH_PictureMetadata *metadata, Image_String *key, Image_String *value)
```

**描述**

根据key获取Metadata的单条属性。该接口获取到的value.data缺少字符串结束符'\0'，请谨慎使用。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PictureMetadata](capi-image-nativemodule-oh-picturemetadata.md) \*metadata | 被操作的OH\_PictureMetadata指针。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*key | 属性的键。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*value | 属性的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_UNSUPPORTED\_METADATA：不支持的元数据类型，或元数据类型与辅助图片类型不匹配。 |

### OH\_PictureMetadata\_SetProperty()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PictureMetadata_SetProperty(OH_PictureMetadata *metadata, Image_String *key, Image_String *value)
```

**描述**

根据key修改Metadata的单条属性。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PictureMetadata](capi-image-nativemodule-oh-picturemetadata.md) \*metadata | 被操作的OH\_PictureMetadata指针。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*key | 属性的键。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*value | 属性的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_UNSUPPORTED\_METADATA：不支持的元数据类型，或元数据类型与辅助图片类型不匹配。 |

### OH\_PictureMetadata\_GetPropertyWithNull()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PictureMetadata_GetPropertyWithNull(OH_PictureMetadata *metadata, Image_String *key, Image_String *value)
```

**描述**

获取图片元数据的属性值。输出的value.data以字符串结束符'\0'结尾。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PictureMetadata](capi-image-nativemodule-oh-picturemetadata.md) \*metadata | 将被操作的PictureMetadata指针。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*key | 属性键指针。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*value | 属性值指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_INVALID\_PARAMETER：metadata、key或value为空。  IMAGE\_UNSUPPORTED\_METADATA：不支持的元数据类型，或元数据类型与辅助图片类型不匹配。 |

### OH\_PictureMetadata\_Release()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PictureMetadata_Release(OH_PictureMetadata *metadata)
```

**描述**

释放OH\_PictureMetadata指针。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PictureMetadata](capi-image-nativemodule-oh-picturemetadata.md) \*metadata | 被操作的OH\_PictureMetadata指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PictureMetadata\_Clone()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PictureMetadata_Clone(OH_PictureMetadata *oldMetadata, OH_PictureMetadata **newMetadata)
```

**描述**

拷贝元数据。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PictureMetadata](capi-image-nativemodule-oh-picturemetadata.md) \*oldMetadata | 被操作的OH\_PictureMetadata指针。 |
| [OH\_PictureMetadata](capi-image-nativemodule-oh-picturemetadata.md) \*\*newMetadata | 拷贝得到的OH\_PictureMetadata指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_ALLOC\_FAILED：内存分配失败。  IMAGE\_COPY\_FAILED：内存拷贝失败。 |
