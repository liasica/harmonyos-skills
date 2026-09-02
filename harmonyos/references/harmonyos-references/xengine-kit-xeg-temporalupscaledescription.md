---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-temporalupscaledescription
title: XEG_TemporalUpscaleDescription
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_TemporalUpscaleDescription
category: harmonyos-references
scraped_at: 2026-09-02T15:02:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6c6e1fc5beb509a2215675ddbb072fa93a4b25786dce49be8956a07379e4b427
---

## 概述

此结构体描述下发时域AI超分渲染命令时的输入信息。

**起始版本：** 5.0.0(12)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_temporal\_upscale.h](xengine-kit-xeg-vulkan-temporal-upscale-8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkImageView [inputImage](xengine-kit-xeg-temporalupscaledescription.md#inputimage) | 输入图像。 |
| VkImageView [depthImage](xengine-kit-xeg-temporalupscaledescription.md#depthimage) | 深度图像。 |
| VkImageView [motionVectorImage](xengine-kit-xeg-temporalupscaledescription.md#motionvectorimage) | 运动矢量图像。运动矢量的计算方式为当前渲染像素的NDC坐标的XY值减去上一帧的NDC坐标的XY值。图像格式需要是VK\_FORMAT\_R16G16\_SFLOAT或更高精度。 |
| VkImageView [dynamicMaskImage](xengine-kit-xeg-temporalupscaledescription.md#dynamicmaskimage) | 物体的动态遮罩图像，格式需要是VK\_FORMAT\_R8\_UNORM或其兼容格式。R通道的合法值为0.0，0.2或1.0，其中0.0表示静态物体，0.2表示运动物体如人物，1.0表示特效或半透明物体。 |
| VkImageView [outputImage](xengine-kit-xeg-temporalupscaledescription.md#outputimage) | 输出图像。 |
| float [jitterX](xengine-kit-xeg-temporalupscaledescription.md#jitterx) | 相机在X方向上的抖动，通常为超分依赖的前序渲染过程中应用的亚像素抖动，包含在相机的投影矩阵中；在ndc坐标系下，其取值范围是 [-1/width, 1/width], width是输入inputTexture纹理的宽度（像素数）。 |
| float [jitterY](xengine-kit-xeg-temporalupscaledescription.md#jittery) | 相机在Y方向上的抖动，通常为超分依赖的前序渲染过程中应用的亚像素抖动，包含在相机的投影矩阵中；在ndc坐标系下，其取值范围是 [-1/height, 1/height], height是输入inputTexture纹理的高度（像素数）。 |
| bool [resetHistory](xengine-kit-xeg-temporalupscaledescription.md#resethistory) | 是否重置历史帧数据，true表示重置，false表示不重置。在历史帧未使用超分，当前帧开始使用超分的情况下建议设置为true。 |
| float [steadyLevel](xengine-kit-xeg-temporalupscaledescription.md#steadylevel) | 画面偏向当前帧（鬼影少但可能存在闪烁）还是历史帧（鬼影多但是更稳定）的平衡程度。取值范围为[0.0, 1.0]，如果该值不在以上范围内，则会发生未定义行为，例如渲染效果不正确或程序崩溃，值越大越偏向历史帧。建议根据实际需求选择合适的值，例如在需要减少鬼影时可设置为较小值，需要减少闪烁可以设置为较大值，推荐值为0.5。 |

## 结构体成员变量说明

### depthImage

```cpp
VkImageView XEG_TemporalUpscaleDescription::depthImage
```

**描述**

深度图像。

### dynamicMaskImage

```cpp
VkImageView XEG_TemporalUpscaleDescription::dynamicMaskImage
```

**描述**

物体的动态遮罩图像，格式需要是VK\_FORMAT\_R8\_UNORM或其兼容格式。R通道的合法值为0.0，0.2或1.0，其中0.0表示静态物体，0.2表示运动物体如人物，1.0表示特效或半透明物体。

### inputImage

```cpp
VkImageView XEG_TemporalUpscaleDescription::inputImage
```

**描述**

输入图像。

### jitterX

```cpp
float XEG_TemporalUpscaleDescription::jitterX
```

**描述**

相机在X方向上的抖动，通常为超分依赖的前序渲染过程中应用的亚像素抖动，包含在相机的投影矩阵中；在ndc坐标系下，其取值范围是 [-1/width, 1/width], width是输入inputTexture纹理的宽度（像素数）。

### jitterY

```cpp
float XEG_TemporalUpscaleDescription::jitterY
```

**描述**

相机在Y方向上的抖动，通常为超分依赖的前序渲染过程中应用的亚像素抖动，包含在相机的投影矩阵中；在ndc坐标系下，其取值范围是 [-1/height, 1/height], height是输入inputTexture纹理的高度（像素数）。

### motionVectorImage

```cpp
VkImageView XEG_TemporalUpscaleDescription::motionVectorImage
```

**描述**

运动矢量图像。运动矢量的计算方式为当前渲染像素的NDC坐标的XY值减去上一帧的NDC坐标的XY值。图像格式需要是VK\_FORMAT\_R16G16\_SFLOAT或更高精度。

### outputImage

```cpp
VkImageView XEG_TemporalUpscaleDescription::outputImage
```

**描述**

输出图像。

### resetHistory

```cpp
bool XEG_TemporalUpscaleDescription::resetHistory
```

**描述**

是否重置历史帧数据，true表示重置，false表示不重置。在历史帧未使用超分，当前帧开始使用超分的情况下建议设置为true。

### steadyLevel

```cpp
float XEG_TemporalUpscaleDescription::steadyLevel
```

**描述**

画面偏向当前帧（鬼影少但可能存在闪烁）还是历史帧（鬼影多但是更稳定）的平衡程度。取值范围为[0.0, 1.0]，如果该值不在以上范围内，则会发生未定义行为，例如渲染效果不正确或程序崩溃，值越大越偏向历史帧。建议根据实际需求选择合适的值，例如在需要减少鬼影时可设置为较小值，需要减少闪烁可以设置为较大值，推荐值为0.5。
