---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-h
title: image.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > image.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:955668a45dc4dcf9b876018658ce5806f3125ec172e94d7999e70bf0106fb585
---

## 概述

为NativeNode API提供Image节点类型定义。

**引用文件：** <arkui/node\_attributes/image.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [NativeTypeSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeType/native_type_sample)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_ImageRepeat](capi-image-h.md#arkui_imagerepeat) | ArkUI\_ImageRepeat | 定义图片重复铺设枚举值。 |
| [ArkUI\_ImageSize](capi-image-h.md#arkui_imagesize) | ArkUI\_ImageSize | 定义图片宽高样式。 |
| [ArkUI\_ObjectFit](capi-image-h.md#arkui_objectfit) | ArkUI\_ObjectFit | 定义[Image](ts-basic-components-image.md)组件的图片填充效果。 |
| [ArkUI\_ImageInterpolation](capi-image-h.md#arkui_imageinterpolation) | ArkUI\_ImageInterpolation | 定义图片插值效果。用于优化图片缩放时的锯齿问题。SVG类型图源不支持该属性。 |
| [ArkUI\_DynamicRangeMode](capi-image-h.md#arkui_dynamicrangemode) | ArkUI\_DynamicRangeMode | 定义图像动态范围模式（例如：SDR/HDR），用于控制图像的明暗与色彩显示范围。 |
| [ArkUI\_ImageRotateOrientation](capi-image-h.md#arkui_imagerotateorientation) | ArkUI\_ImageRotateOrientation | 定义图像旋转方向。 |
| [ArkUI\_ImageRenderMode](capi-image-h.md#arkui_imagerendermode) | ArkUI\_ImageRenderMode | 定义图片渲染模式。 |

## 枚举类型说明

### ArkUI\_ImageRepeat

```c
enum ArkUI_ImageRepeat
```

**描述**

定义图片重复铺设枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_IMAGE\_REPEAT\_NONE = 0 | 不重复铺设图片，图片按原样显示一次。 |
| ARKUI\_IMAGE\_REPEAT\_X = 1 | 在X轴方向重复铺设图片，使图片横向铺满显示区域。 |
| ARKUI\_IMAGE\_REPEAT\_Y = 2 | 在Y轴方向重复铺设图片，使图片纵向铺满显示区域。 |
| ARKUI\_IMAGE\_REPEAT\_XY = 3 | 在X轴和Y轴方向重复铺设图片，使图片铺满整个显示区域。 |

### ArkUI\_ImageSize

```c
enum ArkUI_ImageSize
```

**描述**

定义图片宽高样式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_IMAGE\_SIZE\_AUTO = 0 | 保持原图的比例不变。 |
| ARKUI\_IMAGE\_SIZE\_COVER = 1 | 保持宽高比进行缩小或者放大，使得图片两边都大于或等于显示边界。 |
| ARKUI\_IMAGE\_SIZE\_CONTAIN = 2 | 保持宽高比进行缩小或者放大，使得图片完全显示在显示边界内。 |

### ArkUI\_ObjectFit

```c
enum ArkUI_ObjectFit
```

**描述**

定义[Image](ts-basic-components-image.md)组件的图片填充效果。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_OBJECT\_FIT\_CONTAIN = 0 | 保持宽高比进行缩小或者放大，使得图片完全显示在显示边界内。 |
| ARKUI\_OBJECT\_FIT\_COVER = 1 | 保持宽高比进行缩小或者放大，使得图片的宽度和高度都大于或等于显示边界的宽度和高度（可能超出边界部分被裁剪）。 |
| ARKUI\_OBJECT\_FIT\_AUTO = 2 | 自适应显示，根据图片和容器尺寸自动选择合适的填充方式。 |
| ARKUI\_OBJECT\_FIT\_FILL = 3 | 不保持宽高比进行放大缩小，使得图片充满显示边界。 |
| ARKUI\_OBJECT\_FIT\_SCALE\_DOWN = 4 | 保持宽高比显示，图片缩小或者保持不变。 |
| ARKUI\_OBJECT\_FIT\_NONE = 5 | 图片大小不变。 |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_TOP\_START = 6 | 图片大小不变，在Image组件中顶部起始端对齐。 |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_TOP = 7 | 图片大小不变，在Image组件中顶部横向居中对齐。 |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_TOP\_END = 8 | 图片大小不变，在Image组件中顶部尾端对齐。 |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_START = 9 | 图片大小不变，在Image组件中起始端纵向居中对齐。 |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_CENTER = 10 | 图片大小不变，在Image组件中横向和纵向居中对齐。 |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_END = 11 | 图片大小不变，在Image组件中尾端纵向居中对齐。 |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_BOTTOM\_START = 12 | 图片大小不变，在Image组件中底部起始端对齐。 |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_BOTTOM = 13 | 图片大小不变，在Image组件中底部横向居中对齐。 |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_BOTTOM\_END = 14 | 图片大小不变，在Image组件中底部尾端对齐。 |
| ARKUI\_OBJECT\_FIT\_NONE\_MATRIX = 15 | 不改变图像原始大小，在Image组件中需要配合[ArkUI\_NodeAttributeType](capi-native-node-h.md#arkui_nodeattributetype)中的NODE\_IMAGE\_IMAGE\_MATRIX使用，通过矩阵变换控制图像的显示效果（如缩放、旋转、平移等）。若不配合NODE\_IMAGE\_IMAGE\_MATRIX使用，该枚举值将无法生效。  **起始版本：** 21 |

### ArkUI\_ImageInterpolation

```c
enum ArkUI_ImageInterpolation
```

**描述**

定义图片插值效果。用于优化图片缩放时的锯齿问题。SVG类型图源不支持该属性。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_IMAGE\_INTERPOLATION\_NONE = 0 | 不使用图片插值。 |
| ARKUI\_IMAGE\_INTERPOLATION\_LOW = 1 | 低图片插值。 |
| ARKUI\_IMAGE\_INTERPOLATION\_MEDIUM = 2 | 中图片插值。 |
| ARKUI\_IMAGE\_INTERPOLATION\_HIGH = 3 | 高图片插值，插值质量最高。 |

### ArkUI\_DynamicRangeMode

```c
enum ArkUI_DynamicRangeMode
```

**描述**

定义图像动态范围模式（例如：SDR/HDR），用于控制图像的明暗与色彩显示范围。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_DYNAMIC\_RANGE\_MODE\_HIGH = 0 | 高动态范围（High Dynamic Range，简称HDR），表示图片中显示亮度（brightness）的最小值和最大值的范围，范围越大图像的亮度表达更逼近真实环境，在太亮的环境下不会产生过曝（纯白），太暗的环境下不会产生过暗的效果（纯黑）。 |
| ARKUI\_DYNAMIC\_RANGE\_MODE\_CONSTRAINT = 1 | 受限的高动态范围，包含比SDR更丰富的亮度和色彩，但不是完整的HDR，一般用于需要兼容SDR的情况。 |
| ARKUI\_DYNAMIC\_RANGE\_MODE\_STANDARD = 2 | 标准动态范围（Standard Dynamic Range，简称SDR），表示亮度范围有限，一般在0~100尼特（亮度单位）左右，明暗对比度较小，暗部容易糊成黑，亮部容易过曝。 |

### ArkUI\_ImageRotateOrientation

```c
enum ArkUI_ImageRotateOrientation
```

**描述**

定义图像旋转方向。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ORIENTATION\_AUTO = 0 | 读取图片携带的EXIF元数据作为显示方向，支持旋转和镜像。EXIF（Exchangeable image file format）是专门为数码相机的照片设定的文件格式，可以记录数码照片的属性信息和拍摄数据。 |
| ARKUI\_ORIENTATION\_UP = 1 | 默认按照当前图片的像素数据进行显示，不做任何处理。 |
| ARKUI\_ORIENTATION\_RIGHT = 2 | 将当前图片顺时针旋转90度后显示。 |
| ARKUI\_ORIENTATION\_DOWN = 3 | 将当前图片顺时针旋转180度后显示。 |
| ARKUI\_ORIENTATION\_LEFT = 4 | 将当前图片顺时针旋转270度后显示。 |
| ARKUI\_ORIENTATION\_UP\_MIRRORED = 5 | 将当前图片水平翻转后显示。 |
| ARKUI\_ORIENTATION\_RIGHT\_MIRRORED = 6 | 将当前图片水平翻转再顺时针旋转90度后显示。 |
| ARKUI\_ORIENTATION\_DOWN\_MIRRORED = 7 | 将当前图片垂直翻转后显示。 |
| ARKUI\_ORIENTATION\_LEFT\_MIRRORED = 8 | 将当前图片水平翻转再顺时针旋转270度后显示。 |

### ArkUI\_ImageRenderMode

```c
enum ArkUI_ImageRenderMode
```

**描述**

定义图片渲染模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_IMAGE\_RENDER\_MODE\_ORIGINAL = 0 | 原色渲染模式。 |
| ARKUI\_IMAGE\_RENDER\_MODE\_TEMPLATE = 1 | 黑白渲染模式。 |
