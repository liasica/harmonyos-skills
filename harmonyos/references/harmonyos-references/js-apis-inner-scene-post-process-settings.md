---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-post-process-settings
title: ScenePostProcessSettings
breadcrumb: API参考 > 图形 > ArkGraphics 3D（方舟3D图形） > ArkTS API > graphics3d > ScenePostProcessSettings
category: harmonyos-references
scraped_at: 2026-04-28T08:15:38+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:4fbfefcf29902405fca3f5ba9038b777d010c5b86440602fc573c24e0f573b6f
---

本模块提供3D图形中的色调映射等图像后处理方法。

说明

* 本模块首批接口从API version 12开始支持，后续版本的新增接口，采用上角标标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { ToneMappingType, ToneMappingSettings, BloomSettings, PostProcessSettings } from '@kit.ArkGraphics3D';
```

## ToneMappingType

PhonePC/2in1TabletTVWearable

色调映射类型枚举。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACES | 0 | ACES色调映射类型，基于Academy Color Encoding System标准，将高动态范围（HDR）图像映射到低动态范围（LDR），适用于追求电影级色彩还原的场景。 |
| ACES\_2020 | 1 | ACES\_2020色调映射类型，基于ACES 2020标准，提供更广的色域支持，适用于需要高色彩精度的HDR渲染场景。 |
| FILMIC | 2 | FILMIC色调映射类型，模拟胶片曝光响应曲线，高光过渡柔和自然，适用于追求写实风格和电影质感的一般3D场景。 |

## ToneMappingSettings

PhonePC/2in1TabletTVWearable

色调映射设置。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ToneMappingType](js-apis-inner-scene-post-process-settings.md#tonemappingtype) | 否 | 是 | 色调映射类型，默认值为undefined。 |
| exposure | number | 否 | 是 | 曝光度，取值大于0，默认值为undefined。 |

## BloomSettings18+

PhonePC/2in1TabletTVWearable

泛光设置。当[RenderingPipelineType](js-apis-inner-scene-types.md#renderingpipelinetype21)为FORWARD\_LIGHTWEIGHT时，此功能不可用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| thresholdHard | number | 否 | 是 | 硬阈值，取值范围是非负数，默认值为1.0。 |
| thresholdSoft | number | 否 | 是 | 软阈值，取值范围是非负数，默认值为2.0。 |
| scaleFactor | number | 否 | 是 | 缩放因子，取值范围大于0，默认值为1.0。 |
| scatter | number | 否 | 是 | 扩散量，取值范围大于0，默认值为1.0。 |

## VignetteSettings22+

PhonePC/2in1TabletTVWearable

边缘暗角设置。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| roundness | number | 否 | 是 | 暗角的覆盖区域大小，取值范围为[0, 1]，取值为0时覆盖区域收缩至最小，取值为1时覆盖区域为全局，默认值为sqrt(0.5)（约0.707）。 |
| intensity | number | 否 | 是 | 作用强度，取值范围为[0, 1]，取值为0时无暗角效果，取值为1时为最大暗角强度，默认值为0.4。 |

## ColorFringeSettings22+

PhonePC/2in1TabletTVWearable

色晕设置。当[RenderingPipelineType](js-apis-inner-scene-types.md#renderingpipelinetype21)为FORWARD\_LIGHTWEIGHT时，此功能不可用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| intensity | number | 否 | 是 | 作用强度，取值范围为0到1之间，默认值为0.2。 |

## PostProcessSettings

PhonePC/2in1TabletTVWearable

后处理设置，用于配置相机渲染后的图像处理效果，包括色调映射、泛光、边缘暗角和色晕等，作为[Camera](js-apis-inner-scene-nodes.md#camera)的postProcess属性来使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| toneMapping | [ToneMappingSettings](js-apis-inner-scene-post-process-settings.md#tonemappingsettings) | 否 | 是 | 色调映射，默认值为undefined。 |
| bloom18+ | [BloomSettings](js-apis-inner-scene-post-process-settings.md#bloomsettings18) | 否 | 是 | 泛光，默认值为undefined。 |
| vignette22+ | [VignetteSettings](js-apis-inner-scene-post-process-settings.md#vignettesettings22) | 否 | 是 | 边缘暗角，默认值为undefined。 |
| colorFringe22+ | [ColorFringeSettings](js-apis-inner-scene-post-process-settings.md#colorfringesettings22) | 否 | 是 | 色晕，默认值为undefined。 |
