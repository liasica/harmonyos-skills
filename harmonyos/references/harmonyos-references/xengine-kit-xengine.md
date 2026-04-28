---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine
title: XEngine
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 模块 > XEngine
category: harmonyos-references
scraped_at: 2026-04-28T08:15:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:29540a3e8b3ed4e008649160a5d21c269e21125b6747a134674ab46aff5d4291
---

## 概述

PhonePC/2in1TabletTV

提供XEngine图形相关能力接口。

**系统能力：** SystemCapability.Graphic.XEngine

**起始版本：** 5.0.0(12)

## 汇总

PhonePC/2in1TabletTV

### 文件

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [xeg\_extension\_defs.h](xengine-kit-xeg-extension-defs-8h.md) | 提供XEngine扩展特性宏定义信息。 |
| [xeg\_gles\_adaptive\_vrs.h](xengine-kit-xeg-gles-adaptive-vrs-8h.md) | XEngine VRS特性接口。使用此头文件的接口前需要通过[HMS\_XEG\_GetString](xengine-kit-xengine.md#hms_xeg_getstring)接口查询[XEG\_ADAPTIVE\_VRS\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_adaptive_vrs_extension_name)扩展可用。 |
| [xeg\_gles\_extension.h](xengine-kit-xeg-gles-extension-8h.md) | XEngine扩展特性查询接口（OpenGL ES）。 |
| [xeg\_gles\_neural\_upscale.h](xengine-kit-xeg-gles-neural-upscale-8h.md) | XEngine空域AI超分特性OpenGL ES接口，推荐超分倍率为[1.0, 1.5]。使用此头文件中的接口前需要通过[HMS\_XEG\_GetString](xengine-kit-xengine.md#hms_xeg_getstring)接口查询[XEG\_NEURAL\_UPSCALE\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_neural_upscale_extension_name)扩展可用。 |
| [xeg\_gles\_spatial\_upscale.h](xengine-kit-xeg-gles-spatial-upscale-8h.md) | XEngine空域GPU超分特性OpenGL ES接口。使用此头文件的接口前需要通过[HMS\_XEG\_GetString](xengine-kit-xengine.md#hms_xeg_getstring)接口查询[XEG\_SPATIAL\_UPSCALE\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_spatial_upscale_extension_name)扩展可用。 |
| [xeg\_gles\_temporal\_upscale.h](xengine-kit-xeg-gles-temporal-upscale-8h.md) | XEngine时域AI超分特性OpenGL ES接口。推荐超分倍率为[1.25, 2.0]，使用此头文件中的接口前需要通过[HMS\_XEG\_GetString](xengine-kit-xengine.md#hms_xeg_getstring)接口查询[XEG\_TEMPORAL\_UPSCALE\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_temporal_upscale_extension_name)扩展可用。 |
| [xeg\_vulkan\_adaptive\_vrs.h](xengine-kit-xeg-vulkan-adaptive-vrs-8h.md) | XEngine Adaptive VRS特性Vulkan接口。使用此头文件的接口前需要通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询[XEG\_ADAPTIVE\_VRS\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_adaptive_vrs_extension_name)扩展可用。 |
| [xeg\_vulkan\_common.h](xengine-kit-xeg-vulkan-common-8h.md) | 包含XEngine中Vulkan相关的通用类型定义。 |
| [xeg\_vulkan\_extension.h](xengine-kit-xeg-vulkan-extension-8h.md) | XEngine 扩展特性查询接口（Vulkan）。 |
| [xeg\_vulkan\_hps.h](xengine-kit-xeg-vulkan-hps-8h.md) | XEngine 高性能着色器接口。使用此头文件中的接口前需要通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询[XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_hps_radix_sort_extension_name)扩展可用。 |
| [xeg\_vulkan\_rt\_reflection.h](xengine-kit-xeg-vulkan-rt-reflection-8h.md) | XEngine RT Reflection特性接口。使用此头文件中的接口前需要通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询 [XEG\_RT\_REFLECTION\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_rt_reflection_extension_name)扩展可用。 |
| [xeg\_vulkan\_rt\_visible\_mask.h](xengine-kit-xeg-vulkan-rt-visible-mask-8h.md) | XEngine RT VisibleMask特性接口。使用此头文件中的接口前需要通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询[XEG\_RT\_SHADOW\_AO\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_rt_shadow_ao_extension_name)扩展可用。 |
| [xeg\_vulkan\_rtgi.h](xengine-kit-xeg-vulkan-rtgi-8h.md) | XEngine光线追踪全局光照特性Vulkan接口，提供动态漫反射全局光照（DDGI）及神经网络全局光照（NNGI）两种特性。使用此头文件的接口前，需要先调用[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询扩展[XEG\_RTGI\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_rtgi_extension_name)可用。 |
| [xeg\_vulkan\_spatial\_upscale.h](xengine-kit-xeg-vulkan-spatial-upscale-8h.md) | XEngine空域GPU超分特性Vulkan接口。使用此头文件的接口前需要通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询[XEG\_SPATIAL\_UPSCALE\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_spatial_upscale_extension_name)扩展可用。 |
| [xeg\_vulkan\_temporal\_upscale.h](xengine-kit-xeg-vulkan-temporal-upscale-8h.md) | XEngine时域AI超分特性接口，推荐超分倍率为[1.25, 2.0]。使用此头文件中的接口前需要通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询[XEG\_TEMPORAL\_UPSCALE\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_temporal_upscale_extension_name)扩展可用。 |

### 结构体

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| struct [XEG\_AdaptiveVRSCreateInfo](xengine-kit-xeg-adaptivevrscreateinfo.md) | 此结构体描述创建[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象的参数信息，当结构体中的信息变化时，需要创建新的[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象。 |
| struct [XEG\_AdaptiveVRSDescription](xengine-kit-xeg-adaptivevrsdescription.md) | 此结构体描述下发绘制着色率纹理命令需要的参数信息，每一帧都需要进行更新。 |
| struct [XEG\_ExtensionProperties](xengine-kit-xeg-extensionproperties.md) | 此结构体描述通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询到的XEngine扩展特性集合。 |
| struct [XEG\_HPSCreateInfo](xengine-kit-xeg-hpscreateinfo.md) | 此结构体描述创建[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)对象的信息。 |
| struct [XEG\_HPSRadixSort](xengine-kit-xeg-hpsradixsort.md) | 此结构体描述HPS基数排序扩展结构信息。 |
| struct [XEG\_HPSRadixSortDescription](xengine-kit-xeg-hpsradixsortdescription.md) | 此结构体描述使用[XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_hps_radix_sort_extension_name)扩展进行排序时所需的信息。 |
| struct [XEG\_RTReflectionCreateInfo](xengine-kit-xeg-rtreflectioncreateinfo.md) | 此结构体描述创建[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象的信息。当结构体中的信息变化时，需要创建新的[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象。 |
| struct [XEG\_RTReflectionDescription](xengine-kit-xeg-rtreflectiondescription.md) | 此结构体描述下发光线求交命令时的输入信息。 |
| struct [XEG\_RTShadowAOCreateInfo](xengine-kit-xeg-rtshadowaocreateinfo.md) | 此结构体描述创建支持光线追踪阴影和环境光遮蔽效果[XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask)实例的初始化信息。当结构体中的信息变化时，需要创建新的[XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask)对象。 |
| struct [XEG\_RTShadowParameters](xengine-kit-xeg-rtshadowparameters.md) | 光线追踪阴影（Shadow）算法参数。 |
| struct [XEG\_RTAOParameters](xengine-kit-xeg-rtaoparameters.md) | 光线追踪环境光遮蔽（AO）算法参数。 |
| struct [XEG\_RTShadowAODenoiserParameters](xengine-kit-xeg-rtshadowaodenoiserparameters.md) | 光线追踪阴影和环境光遮蔽算法去噪参数。 |
| struct [XEG\_RTShadowAODescription](xengine-kit-xeg-rtshadowaodescription.md) | 此结构体描述光线追踪阴影和环境光遮蔽算法渲染命令的输入信息。 |
| struct [XEG\_DDGIVolumeEntryParameters](xengine-kit-xeg-ddgivolumeentryparameters.md) | 此结构体描述每一个DDGI体积的必要参数。 |
| struct [XEG\_DDGICreateInfo](xengine-kit-xeg-ddgicreateinfo.md) | 此结构体描述创建具有DDGI特性的[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象的信息，当结构体中的信息变化时，需要创建新的[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象。 |
| struct [XEG\_DDGIDescription](xengine-kit-xeg-ddgidescription.md) | 此结构体描述更新DDGI探针辐照度及渲染输出GI图像所需的信息。 |
| struct [XEG\_NNGICreateInfo](xengine-kit-xeg-nngicreateinfo.md) | 此结构体描述创建具有NNGI特性的[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象的信息，当结构体中的信息变化时，需要创建新的[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象。 |
| struct [XEG\_NNGIDescription](xengine-kit-xeg-nngidescription.md) | 此结构体描述更新NNGI用于计算光线追踪全局光照的所需的信息。 |
| struct [XEG\_SpatialUpscaleCreateInfo](xengine-kit-xeg-spatialupscalecreateinfo.md) | 此结构体描述创建[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象的信息，当结构体中的信息变化时，需要创建新的[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象。 |
| struct [XEG\_SpatialUpscaleDescription](xengine-kit-xeg-spatialupscaledescription.md) | 此结构体描述下发空域GPU超分渲染命令时需要的图像信息。 |
| struct [XEG\_TemporalUpscaleCreateInfo](xengine-kit-xeg-temporalupscalecreateinfo.md) | 此结构体描述创建[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象的信息。当结构体中的信息变化时，需要创建新的[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象。 |
| struct [XEG\_TemporalUpscaleDescription](xengine-kit-xeg-temporalupscaledescription.md) | 此结构体描述下发时域AI超分渲染命令时的输入信息。 |

### 宏定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [XEG\_spatial\_upscale](xengine-kit-xengine.md#xeg_spatial_upscale) 1 | XEngine空域GPU超分扩展特性宏定义。 |
| [XEG\_SPATIAL\_UPSCALE\_VERSION](xengine-kit-xengine.md#xeg_spatial_upscale_version) 1 | XEngine空域GPU超分扩展特性版本号。 |
| [XEG\_SPATIAL\_UPSCALE\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_spatial_upscale_extension_name) "XEG\_spatial\_upscale" | XEngine空域GPU超分扩展特性名称。 |
| [XEG\_neural\_upscale](xengine-kit-xengine.md#xeg_neural_upscale) 1 | XEngine空域AI超分扩展特性宏定义。 |
| [XEG\_NEURAL\_UPSCALE\_VERSION](xengine-kit-xengine.md#xeg_neural_upscale_version) 1 | XEngine空域AI超分扩展特性版本号。 |
| [XEG\_NEURAL\_UPSCALE\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_neural_upscale_extension_name) "XEG\_neural\_upscale" | XEngine空域AI超分扩展特性名称。 |
| [XEG\_temporal\_upscale](xengine-kit-xengine.md#xeg_temporal_upscale) 1 | XEngine时域AI超分扩展特性宏定义。 |
| [XEG\_TEMPORAL\_UPSCALE\_VERSION](xengine-kit-xengine.md#xeg_temporal_upscale_version) 1 | XEngine时域AI超分扩展特性版本号。 |
| [XEG\_TEMPORAL\_UPSCALE\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_temporal_upscale_extension_name) "XEG\_temporal\_upscale" | XEngine时域AI超分扩展特性名称。 |
| [XEG\_adaptive\_vrs](xengine-kit-xengine.md#xeg_adaptive_vrs) 1 | XEngine自适应VRS扩展特性宏定义。 |
| [XEG\_ADAPTIVE\_VRS\_VERSION](xengine-kit-xengine.md#xeg_adaptive_vrs_version) 1 | XEngine自适应VRS扩展特性版本号。 |
| [XEG\_ADAPTIVE\_VRS\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_adaptive_vrs_extension_name) "XEG\_adaptive\_vrs" | XEngine自适应VRS扩展特性名称。 |
| [XEG\_RTGI\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_rtgi_extension_name) "XEG\_rtgi" | XEngine光线追踪全局光照扩展特性名称。 |
| [XEG\_RT\_SHADOW\_AO\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_rt_shadow_ao_extension_name) "XEG\_rt\_shadow\_ao" | XEngine光线追踪阴影和环境光遮蔽扩展特性名称。 |
| [XEG\_RT\_REFLECTION\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_rt_reflection_extension_name) "XEG\_rt\_reflection" | XEngine光线追踪反射扩展特性名称。 |
| [XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_hps_radix_sort_extension_name) "XEG\_hps\_radix\_sort" | XEngine 高性能基数排序扩展特性名称。 |
| [XEG\_ADAPTIVE\_VRS\_INPUT\_SIZE](xengine-kit-xengine.md#xeg_adaptive_vrs_input_size) 0x1U | 用于设置[HMS\_XEG\_AdaptiveVRSParameter](xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter)接口的INPUT\_SIZE参数，表示上一帧渲染管线最终渲染的图像宽度和高度。 |
| [XEG\_ADAPTIVE\_VRS\_INPUT\_REGION](xengine-kit-xengine.md#xeg_adaptive_vrs_input_region) 0x2U | 用于设置[HMS\_XEG\_AdaptiveVRSParameter](xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter)接口的INPUT\_REGION参数，表示上一帧渲染管线最终渲染的图像区域。 |
| [XEG\_ADAPTIVE\_VRS\_TEXEL\_SIZE](xengine-kit-xengine.md#xeg_adaptive_vrs_texel_size) 0x3U | 用于设置[HMS\_XEG\_AdaptiveVRSParameter](xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter)接口的TEXEL\_SIZE参数。 |
| [XEG\_ADAPTIVE\_VRS\_ERROR\_SENSITIVITY](xengine-kit-xengine.md#xeg_adaptive_vrs_error_sensitivity) 0x4U | 用于设置[HMS\_XEG\_AdaptiveVRSParameter](xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter)接口的ERROR\_SENSITIVITY参数，表示控制生成着色率图像的阈值。该值越大，平均着色率越小，即性能会越好但画质会劣化。建议取值范围为[0, 1]。 |
| [XEG\_ADAPTIVE\_VRS\_FLIP](xengine-kit-xengine.md#xeg_adaptive_vrs_flip) 0x5U | 用于设置[HMS\_XEG\_AdaptiveVRSParameter](xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter)接口的FLIP参数，该参数用于控制是否执行图像上下翻转。 |
| [XEG\_EXTENSIONS](xengine-kit-xengine.md#xeg_extensions) 0x01U | 作为[HMS\_XEG\_GetString](xengine-kit-xengine.md#hms_xeg_getstring)接口的入参，以获取XEngine支持的OpenGL ES扩展特性。 |
| [XEG\_NEURAL\_UPSCALE\_SCISSOR](xengine-kit-xengine.md#xeg_neural_upscale_scissor) 0x1U | 用于通过[HMS\_XEG\_NeuralUpscaleParameter](xengine-kit-xengine.md#hms_xeg_neuralupscaleparameter)接口设置超分的裁剪窗口参数，裁剪窗口用于确定对输入图像采样的区域。 |
| [XEG\_NEURAL\_UPSCALE\_SHARPNESS](xengine-kit-xengine.md#xeg_neural_upscale_sharpness) 0x2U | 用于通过[HMS\_XEG\_NeuralUpscaleParameter](xengine-kit-xengine.md#hms_xeg_neuralupscaleparameter)接口设置超分的锐化度参数，锐化度的建议取值范围为[0, 1]。 |
| [XEG\_NEURAL\_UPSCALE\_INPUT\_HANDLE](xengine-kit-xengine.md#xeg_neural_upscale_input_handle) 0x4U | 用于通过[HMS\_XEG\_NeuralUpscaleParameter](xengine-kit-xengine.md#hms_xeg_neuralupscaleparameter)接口设置与超分输入纹理关联的OH\_NativeBuffer handle。 |
| [XEG\_SPATIAL\_UPSCALE\_SCISSOR](xengine-kit-xengine.md#xeg_spatial_upscale_scissor) 0x1U | 用于设置[HMS\_XEG\_SpatialUpscaleParameter](xengine-kit-xengine.md#hms_xeg_spatialupscaleparameter)接口的SCISSOR参数。 |
| [XEG\_SPATIAL\_UPSCALE\_SHARPNESS](xengine-kit-xengine.md#xeg_spatial_upscale_sharpness) 0x2U | 用于设置[HMS\_XEG\_SpatialUpscaleParameter](xengine-kit-xengine.md#hms_xeg_spatialupscaleparameter)接口的SHARPNESS参数。 |
| [XEG\_TEMPORAL\_UPSCALE\_INPUT\_SIZE](xengine-kit-xengine.md#xeg_temporal_upscale_input_size) 0x1U | 用于通过[HMS\_XEG\_TemporalUpscaleParameter](xengine-kit-xengine.md#hms_xeg_temporalupscaleparameter)接口设置超分输入纹理的真实宽高。 |
| [XEG\_TEMPORAL\_UPSCALE\_JITTER\_NUM](xengine-kit-xengine.md#xeg_temporal_upscale_jitter_num) 0x2U | 用于通过[HMS\_XEG\_TemporalUpscaleParameter](xengine-kit-xengine.md#hms_xeg_temporalupscaleparameter)接口设置相机抖动的周期数，取值范围为[4, 16]，推荐8。 |
| [XEG\_TEMPORAL\_UPSCALE\_DEPTH\_REVERSED](xengine-kit-xengine.md#xeg_temporal_upscale_depth_reversed) 0x3U | 用于通过[HMS\_XEG\_TemporalUpscaleParameter](xengine-kit-xengine.md#hms_xeg_temporalupscaleparameter)接口设置是否存在深度反转。true表示存在深度反转，false表示不存在深度反转。 |
| [XEG\_TEMPORAL\_UPSCALE\_RESET\_HISTORY](xengine-kit-xengine.md#xeg_temporal_upscale_reset_history) 0x4U | 用于通过[HMS\_XEG\_TemporalUpscaleParameter](xengine-kit-xengine.md#hms_xeg_temporalupscaleparameter)接口设置是否重置历史帧数据，true表示重置，false表示不重置。在历史帧未使用超分，并且当前帧开始使用超分的情况下建议设置为true。 |
| [XEG\_TEMPORAL\_UPSCALE\_STEADY\_LEVEL](xengine-kit-xengine.md#xeg_temporal_upscale_steady_level) 0x5U | 用于通过[HMS\_XEG\_TemporalUpscaleParameter](xengine-kit-xengine.md#hms_xeg_temporalupscaleparameter)接口设置画面偏向当前帧（鬼影少但可能存在闪烁）还是历史帧（鬼影多但是更稳定）的平衡程度。取值范围为[0.0, 1.0]，值越大越偏向历史帧。 |
| [XEG\_MAX\_EXTENSION\_NAME\_SIZE](xengine-kit-xengine.md#xeg_max_extension_name_size) 256 | XEngine扩展特性名称支持的最大长度。 |

### 类型定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_ADAPTIVEVRSPARAMETER](xengine-kit-xengine.md#pfn_hms_xeg_adaptivevrsparameter)) (GLenum pname, GLvoid \*param) | 设置自适应VRS输入参数的函数指针定义。 |
| typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_DISPATCHADAPTIVEVRS](xengine-kit-xengine.md#pfn_hms_xeg_dispatchadaptivevrs)) (GLfloat \*reprojectionMatrix, GLuint inputColorImage, GLuint inputDepthImage, GLuint shadingRateImage) | 计算着色率图像的函数指针定义。 |
| typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_APPLYADAPTIVEVRS](xengine-kit-xengine.md#pfn_hms_xeg_applyadaptivevrs)) (GLuint shadingRateImage) | 将着色率图像应用到渲染目标中的函数指针定义。 |
| typedef const GLubyte \*(GL\_APIENTRYP [PFN\_HMS\_XEG\_GETSTRING](xengine-kit-xengine.md#pfn_hms_xeg_getstring)) (GLenum name) | XEngine OpenGL ES扩展特性查询接口函数指针定义。 |
| typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_NEURALUPSCALEPARAMETER](xengine-kit-xengine.md#pfn_hms_xeg_neuralupscaleparameter)) (GLenum pname, GLvoid \*param) | 设置空域AI超分输入参数的函数指针定义。 |
| typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_RENDERNEURALUPSCALE](xengine-kit-xengine.md#pfn_hms_xeg_renderneuralupscale)) (GLuint inputTexture) | 执行空域AI超分渲染命令的函数指针定义。 |
| typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_SPATIALUPSCALEPARAMETER](xengine-kit-xengine.md#pfn_hms_xeg_spatialupscaleparameter)) (GLenum pname, GLvoid \*param) | 设置空域GPU超分输入参数的函数指针定义。 |
| typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_RENDERSPATIALUPSCALE](xengine-kit-xengine.md#pfn_hms_xeg_renderspatialupscale)) (GLuint inputTexture) | 执行空域GPU超分渲染命令的函数指针定义。 |
| typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_TemporalUpscaleParameter](xengine-kit-xengine.md#pfn_hms_xeg_temporalupscaleparameter)) (GLenum pname, GLvoid \*param) | 设置时域AI超分输入参数的函数指针定义。 |
| typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_RenderTemporalUpscale](xengine-kit-xengine.md#pfn_hms_xeg_rendertemporalupscale)) (GLuint inputTexture, GLuint depthTexture, GLuint motionVectorTexture, GLuint dynamicMaskTexture, GLfloat jitterX, GLfloat jitterY) | 执行时域AI超分渲染命令的函数指针定义。 |
| VK\_DEFINE\_HANDLE([XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)) | [XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)的句柄。 |
| typedef struct [XEG\_AdaptiveVRSCreateInfo](xengine-kit-xeg-adaptivevrscreateinfo.md) [XEG\_AdaptiveVRSCreateInfo](xengine-kit-xengine.md#xeg_adaptivevrscreateinfo) | 此结构体描述创建[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象的参数信息，当结构体中的信息变化时，需要创建新的[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象。 |
| typedef struct [XEG\_AdaptiveVRSDescription](xengine-kit-xeg-adaptivevrsdescription.md) [XEG\_AdaptiveVRSDescription](xengine-kit-xengine.md#xeg_adaptivevrsdescription) | 此结构体描述下发绘制着色率纹理命令需要的参数信息，每一帧都需要进行更新。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CreateAdaptiveVRS](xengine-kit-xengine.md#pfn_hms_xeg_createadaptivevrs)) (VkDevice device, const [XEG\_AdaptiveVRSCreateInfo](xengine-kit-xeg-adaptivevrscreateinfo.md) \*pXegAdaptiveVRSCreateInfo, [XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs) \*pXegAdaptiveVRS) | 创建[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象的函数指针定义。 |
| typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdDispatchAdaptiveVRS](xengine-kit-xengine.md#pfn_hms_xeg_cmddispatchadaptivevrs)) (VkCommandBuffer commandBuffer, [XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs) xegAdaptiveVRS, [XEG\_AdaptiveVRSDescription](xengine-kit-xeg-adaptivevrsdescription.md) \*pXegAdaptiveVRSDescription) | 执行计算自适应可变着色率命令的函数指针定义。 |
| typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_DestroyAdaptiveVRS](xengine-kit-xengine.md#pfn_hms_xeg_destroyadaptivevrs)) ([XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs) xegAdaptiveVRS) | 销毁[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象的函数指针定义。 |
| typedef enum [XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype) XEG\_StructureType | XEngine结构体类型的枚举。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdSetSynchronization](xengine-kit-xengine.md#pfn_hms_xeg_cmdsetsynchronization)) (VkCommandBuffer commandBuffer, const void \*xegHandle) | 设置同步信号，等待渲染结果写入指定图像的函数指针定义。使用RTGI特性时，为等待GI渲染结果到写入指定图像。 |
| typedef struct [XEG\_ExtensionProperties](xengine-kit-xeg-extensionproperties.md) [XEG\_ExtensionProperties](xengine-kit-xengine.md#xeg_extensionproperties) | 此结构体描述通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询到的XEngine扩展特性集合。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#pfn_hms_xeg_enumeratedeviceextensionproperties)) (VkPhysicalDevice physicalDevice, uint32\_t \*pPropertyCount, [XEG\_ExtensionProperties](xengine-kit-xeg-extensionproperties.md) \*pProperties) | XEngine Vulkan扩展特性查询接口函数指针定义。 |
| VK\_DEFINE\_HANDLE([XEG\_HPS](xengine-kit-xengine.md#xeg_hps)) | [XEG\_HPS](xengine-kit-xengine.md#xeg_hps)的句柄。 |
| typedef struct [XEG\_HPSCreateInfo](xengine-kit-xeg-hpscreateinfo.md) [XEG\_HPSCreateInfo](xengine-kit-xengine.md#xeg_hpscreateinfo) | 此结构体描述创建[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)对象的信息。 |
| typedef struct [XEG\_HPSRadixSort](xengine-kit-xeg-hpsradixsort.md) [XEG\_HPSRadixSort](xengine-kit-xengine.md#xeg_hpsradixsort) | 此结构体描述HPS基数排序扩展结构信息。 |
| typedef struct [XEG\_HPSRadixSortDescription](xengine-kit-xeg-hpsradixsortdescription.md) [XEG\_HPSRadixSortDescription](xengine-kit-xengine.md#xeg_hpsradixsortdescription) | 此结构体描述使用[XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_hps_radix_sort_extension_name)扩展进行排序时所需的信息。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CreateHPS](xengine-kit-xengine.md#pfn_hms_xeg_createhps)) (VkDevice device, const [XEG\_HPSCreateInfo](xengine-kit-xeg-hpscreateinfo.md) \*pCreateInfo, [XEG\_HPS](xengine-kit-xengine.md#xeg_hps) \*pHps) | 创建[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)对象的函数指针定义。 |
| typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_DestroyHPS](xengine-kit-xengine.md#pfn_hms_xeg_destroyhps)) ([XEG\_HPS](xengine-kit-xengine.md#xeg_hps) hps) | 销毁[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)对象的函数指针定义。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdRadixSortHPS](xengine-kit-xengine.md#pfn_hms_xeg_cmdradixsorthps)) (VkCommandBuffer commandBuffer, [XEG\_HPS](xengine-kit-xengine.md#xeg_hps) hps, const [XEG\_HPSRadixSortDescription](xengine-kit-xeg-hpsradixsortdescription.md) \*pDescription) | 录制HPS排序命令的函数指针定义，使用此接口前需要通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询是否支持[XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_hps_radix_sort_extension_name)扩展。 |
| VK\_DEFINE\_HANDLE([XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)) | [XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)的句柄。 |
| typedef struct [XEG\_RTReflectionCreateInfo](xengine-kit-xeg-rtreflectioncreateinfo.md) [XEG\_RTReflectionCreateInfo](xengine-kit-xengine.md#xeg_rtreflectioncreateinfo) | 此结构体描述创建[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象的信息。当结构体中的信息变化时，需要创建新的[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象。 |
| typedef struct [XEG\_RTReflectionDescription](xengine-kit-xeg-rtreflectiondescription.md) [XEG\_RTReflectionDescription](xengine-kit-xengine.md#xeg_rtreflectiondescription) | 此结构体描述下发光线求交命令时的输入信息。 |
| typedef VkResult(VKAPI\_ATTR \* [PFN\_HMS\_XEG\_CreateRTReflection](xengine-kit-xengine.md#pfn_hms_xeg_creatertreflection)) (VkDevice device, const void \*pCreateInfo, [XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection) \*pRtReflection) | 创建[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象的函数指针定义。 |
| typedef VkResult VKAPI\_ATTR \* [PFN\_HMS\_XEG\_CmdRenderRTReflection](xengine-kit-xengine.md#pfn_hms_xeg_cmdrenderrtreflection)(VkCommandBuffer commandBuffer, [XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection) rtReflection, const void \*pDescription) | 录制计算RT反射命中信息命令的函数指针定义。 |
| typedef void VKAPI\_ATTR \* [PFN\_HMS\_XEG\_DestroyRTReflection](xengine-kit-xengine.md#pfn_hms_xeg_destroyrtreflection)([XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection) rtReflection) | 销毁[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象的函数指针定义。 |
| VK\_DEFINE\_HANDLE([XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask)) | [XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask)的句柄。表示光线追踪VisibleMask特性实例，支持阴影和环境光遮蔽效果。 |
| typedef enum [XEG\_DenoiseQualityMode](xengine-kit-xengine.md#xeg_denoisequalitymode) XEG\_DenoiseQualityMode | 去噪质量模式枚举。 |
| typedef enum [XEG\_TraversalMode](xengine-kit-xengine.md#xeg_traversalmode) XEG\_TraversalMode | 遍历模式枚举。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CreateRTVisibleMask](xengine-kit-xengine.md#pfn_hms_xeg_creatertvisiblemask)) (VkDevice device, const void \*pCreateInfo, [XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask) \*pRTVisibleMask) | 创建[XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask)对象的函数指针定义。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdRenderRTVisibleMask](xengine-kit-xengine.md#pfn_hms_xeg_cmdrenderrtvisiblemask)) (VkCommandBuffer commandBuffer, [XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask) rtVisibleMask, const void \*pDescription) | 录制光线追踪VisibleMask渲染命令的函数指针定义。 |
| typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_DestroyRTVisibleMask](xengine-kit-xengine.md#pfn_hms_xeg_destroyrtvisiblemask)) ([XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask) rtVisibleMask) | 销毁[XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask)对象的函数指针定义。 |
| VK\_DEFINE\_HANDLE([XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)) | [XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)的句柄。 |
| typedef enum [XEG\_RTGIQualityMode](xengine-kit-xengine.md#xeg_rtgiqualitymode) XEG\_RTGIQualityMode | 输出图像质量模式的枚举。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CreateRTGI](xengine-kit-xengine.md#pfn_hms_xeg_creatertgi)) (VkDevice device, const void \*pCreateInfo, [XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi) \*pRtGI) | 创建[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象的函数指针定义。 |
| typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_DestroyRTGI](xengine-kit-xengine.md#pfn_hms_xeg_destroyrtgi)) ([XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi) rtGI) | 销毁[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象的函数指针定义。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdRenderRTGI](xengine-kit-xengine.md#pfn_hms_xeg_cmdrenderrtgi)) (VkCommandBuffer commandBuffer, [XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi) rtGI, const void \*pDescription) | 执行渲染命令的函数指针定义。 |
| VK\_DEFINE\_HANDLE([XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)) | [XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)的句柄。 |
| typedef struct [XEG\_SpatialUpscaleCreateInfo](xengine-kit-xeg-spatialupscalecreateinfo.md) [XEG\_SpatialUpscaleCreateInfo](xengine-kit-xengine.md#xeg_spatialupscalecreateinfo) | 此结构体描述创建[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象的信息，当结构体中的信息变化时，需要创建新的[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象。 |
| typedef struct [XEG\_SpatialUpscaleDescription](xengine-kit-xeg-spatialupscaledescription.md) [XEG\_SpatialUpscaleDescription](xengine-kit-xengine.md#xeg_spatialupscaledescription) | 此结构体描述下发空域GPU超分渲染命令时需要的图像信息。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CreateSpatialUpscale](xengine-kit-xengine.md#pfn_hms_xeg_createspatialupscale)) (VkDevice device, const [XEG\_SpatialUpscaleCreateInfo](xengine-kit-xeg-spatialupscalecreateinfo.md) \*pXegSpatialUpscaleCreateInfo, [XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale) \*pXegSpatialUpscale) | 创建[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象的函数指针定义。 |
| typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdRenderSpatialUpscale](xengine-kit-xengine.md#pfn_hms_xeg_cmdrenderspatialupscale)) (VkCommandBuffer commandBuffer, [XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale) xegSpatialUpscale, [XEG\_SpatialUpscaleDescription](xengine-kit-xeg-spatialupscaledescription.md) \*pXegSpatialUpscaleDescription) | 执行空域GPU超分渲染命令的函数指针定义。 |
| typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_DestroySpatialUpscale](xengine-kit-xengine.md#pfn_hms_xeg_destroyspatialupscale)) ([XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale) xegSpatialUpscale) | 销毁[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象的函数指针定义。 |
| VK\_DEFINE\_HANDLE([XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)) | [XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)的句柄。 |
| typedef struct [XEG\_TemporalUpscaleCreateInfo](xengine-kit-xeg-temporalupscalecreateinfo.md) [XEG\_TemporalUpscaleCreateInfo](xengine-kit-xengine.md#xeg_temporalupscalecreateinfo) | 此结构体描述创建[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象的信息。当结构体中的信息变化时，需要创建新的[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象。 |
| typedef struct [XEG\_TemporalUpscaleDescription](xengine-kit-xeg-temporalupscaledescription.md) [XEG\_TemporalUpscaleDescription](xengine-kit-xengine.md#xeg_temporalupscaledescription) | 此结构体描述下发时域AI超分渲染命令时的输入信息。 |
| typedef VkResult(VKAPI\_ATTR \* [PFN\_HMS\_XEG\_CreateTemporalUpscale](xengine-kit-xengine.md#pfn_hms_xeg_createtemporalupscale)) (VkDevice device, [XEG\_TemporalUpscaleCreateInfo](xengine-kit-xeg-temporalupscalecreateinfo.md) \*pTemporalUpscaleInfo, [XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale) \*pTemporalUpscale) | 创建[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象的函数指针定义。 |
| typedef void(VKAPI\_ATTR \* [PFN\_HMS\_XEG\_CmdRenderTemporalUpscale](xengine-kit-xengine.md#pfn_hms_xeg_cmdrendertemporalupscale)) (VkCommandBuffer commandBuffer, [XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale) temporalUpscale, [XEG\_TemporalUpscaleDescription](xengine-kit-xeg-temporalupscaledescription.md) \*pDescription) | 录制时域AI超分渲染命令的函数指针定义。 |
| typedef void(VKAPI\_ATTR \* [PFN\_HMS\_XEG\_DestroyTemporalUpscale](xengine-kit-xengine.md#pfn_hms_xeg_destroytemporalupscale)) ([XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale) temporalUpscale) | 销毁[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象的函数指针定义。 |

### 枚举

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype) {  XEG\_STRUCTURE\_TYPE\_RT\_SHADOWAO\_CREATE\_INFO = 0, XEG\_STRUCTURE\_TYPE\_RT\_SHADOWAO\_DESCRIPTION = 1, XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_CREATE\_INFO = 2, XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_DESCRIPTION = 3,  XEG\_STRUCTURE\_TYPE\_NNGI\_CREATE\_INFO = 4, XEG\_STRUCTURE\_TYPE\_NNGI\_DESCRIPTION = 5, XEG\_STRUCTURE\_TYPE\_DDGI\_CREATE\_INFO = 6, XEG\_STRUCTURE\_TYPE\_DDGI\_DESCRIPTION = 7,  XEG\_STRUCTURE\_TYPE\_HPS\_CREATE\_INFO = 1001, XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT = 1002, XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT\_DESCRIPTION = 1003  } | XEngine结构体类型的枚举。 |
| [XEG\_DenoiseQualityMode](xengine-kit-xengine.md#xeg_denoisequalitymode) { XEG\_DENOISE\_QUALITY\_MODE\_NONE = 0, XEG\_DENOISE\_QUALITY\_MODE\_QUALITY = 1, XEG\_DENOISE\_QUALITY\_MODE\_BALANCED = 2, XEG\_DENOISE\_QUALITY\_MODE\_PERFORMANCES = 3 } | 去噪质量模式枚举。 |
| [XEG\_TraversalMode](xengine-kit-xengine.md#xeg_traversalmode) { XEG\_TRAVERSAL\_MODE\_DEFAULT = 0, XEG\_TRAVERSAL\_MODE\_PERFORMANCES = 1 } | 遍历模式枚举。 |
| [XEG\_RTGIQualityMode](xengine-kit-xengine.md#xeg_rtgiqualitymode) { XEG\_RTGI\_QUALITY\_MODE\_QUALITY = 0, XEG\_RTGI\_QUALITY\_MODE\_BALANCED = 1, XEG\_RTGI\_QUALITY\_MODE\_PERFORMANCE = 2 } | 输出图像质量模式的枚举。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_AdaptiveVRSParameter](xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter) (GLenum pname, GLvoid \*param) | 设置自适应VRS的参数。 |
| GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_DispatchAdaptiveVRS](xengine-kit-xengine.md#hms_xeg_dispatchadaptivevrs) (GLfloat \*reprojectionMatrix, GLuint inputColorImage, GLuint inputDepthImage, GLuint shadingRateImage) | 计算着色率图像。 |
| GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_ApplyAdaptiveVRS](xengine-kit-xengine.md#hms_xeg_applyadaptivevrs) (GLuint shadingRateImage) | 将着色率图像应用到渲染目标中。 |
| const GLubyte \* [HMS\_XEG\_GetString](xengine-kit-xengine.md#hms_xeg_getstring) (GLenum name) | XEngine OpenGL ES扩展特性查询接口。 |
| GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_NeuralUpscaleParameter](xengine-kit-xengine.md#hms_xeg_neuralupscaleparameter) (GLenum pname, GLvoid \*param) | 设置空域AI超分输入参数。 |
| GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_RenderNeuralUpscale](xengine-kit-xengine.md#hms_xeg_renderneuralupscale) (GLuint inputTexture) | 执行空域AI超分渲染命令。 |
| GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_SpatialUpscaleParameter](xengine-kit-xengine.md#hms_xeg_spatialupscaleparameter) (GLenum pname, GLvoid \*param) | 设置空域GPU超分输入参数。 |
| GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_RenderSpatialUpscale](xengine-kit-xengine.md#hms_xeg_renderspatialupscale) (GLuint inputTexture) | 执行空域GPU超分渲染命令。 |
| GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_TemporalUpscaleParameter](xengine-kit-xengine.md#hms_xeg_temporalupscaleparameter) (GLenum pname, const GLvoid \*param) | 设置时域AI超分输入参数。 |
| GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_RenderTemporalUpscale](xengine-kit-xengine.md#hms_xeg_rendertemporalupscale) (GLuint inputTexture, GLuint depthTexture, GLuint motionVectorTexture, GLuint dynamicMaskTexture, GLfloat jitterX, GLfloat jitterY) | 执行时域AI超分渲染命令。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateAdaptiveVRS](xengine-kit-xengine.md#hms_xeg_createadaptivevrs) (VkDevice device, [XEG\_AdaptiveVRSCreateInfo](xengine-kit-xeg-adaptivevrscreateinfo.md) \*pXegAdaptiveVRSCreateInfo, [XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs) \*pXegAdaptiveVRS) | 创建[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象。 |
| VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_CmdDispatchAdaptiveVRS](xengine-kit-xengine.md#hms_xeg_cmddispatchadaptivevrs) (VkCommandBuffer commandBuffer, [XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs) xegAdaptiveVRS, [XEG\_AdaptiveVRSDescription](xengine-kit-xeg-adaptivevrsdescription.md) \*pXegAdaptiveVRSDescription) | 执行计算自适应可变着色率命令。 |
| VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyAdaptiveVRS](xengine-kit-xengine.md#hms_xeg_destroyadaptivevrs) ([XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs) xegAdaptiveVRS) | 销毁[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CmdSetSynchronization](xengine-kit-xengine.md#hms_xeg_cmdsetsynchronization) (VkCommandBuffer commandBuffer, const void \*xegHandle) | 设置同步信号，等待渲染结果写入指定图像。使用RTGI特性时，为等待GI渲染结果写入指定图像。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties) (VkPhysicalDevice physicalDevice, uint32\_t \*pPropertyCount, [XEG\_ExtensionProperties](xengine-kit-xeg-extensionproperties.md) \*pProperties) | XEngine Vulkan扩展特性查询接口。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateHPS](xengine-kit-xengine.md#hms_xeg_createhps) (VkDevice device, const [XEG\_HPSCreateInfo](xengine-kit-xeg-hpscreateinfo.md) \*pCreateInfo, [XEG\_HPS](xengine-kit-xengine.md#xeg_hps) \*pHps) | 创建[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)对象。 |
| VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyHPS](xengine-kit-xengine.md#hms_xeg_destroyhps) ([XEG\_HPS](xengine-kit-xengine.md#xeg_hps) hps) | 销毁[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)对象。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CmdRadixSortHPS](xengine-kit-xengine.md#hms_xeg_cmdradixsorthps) (VkCommandBuffer commandBuffer, [XEG\_HPS](xengine-kit-xengine.md#xeg_hps) hps, const [XEG\_HPSRadixSortDescription](xengine-kit-xeg-hpsradixsortdescription.md) \*pDescription) | 录制HPS排序命令，使用此接口前需要通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询是否支持[XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_hps_radix_sort_extension_name)扩展。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateRTReflection](xengine-kit-xengine.md#hms_xeg_creatertreflection) (VkDevice device, const void \*pCreateInfo, [XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection) \*pRtReflection) | 创建[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CmdRenderRTReflection](xengine-kit-xengine.md#hms_xeg_cmdrenderrtreflection) (VkCommandBuffer commandBuffer, [XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection) rtReflection, const void \*pDescription) | 录制计算RT反射命中信息命令。 |
| VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyRTReflection](xengine-kit-xengine.md#hms_xeg_destroyrtreflection) ([XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection) rtReflection) | 销毁[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateRTVisibleMask](xengine-kit-xengine.md#hms_xeg_creatertvisiblemask) (VkDevice device, const void \*pCreateInfo, [XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask) \*pRTVisibleMask) | 创建[XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask)对象。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CmdRenderRTVisibleMask](xengine-kit-xengine.md#hms_xeg_cmdrenderrtvisiblemask) (VkCommandBuffer commandBuffer, [XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask) rtVisibleMask, const void \*pDescription) | 录制光线追踪VisibleMask渲染命令。 |
| VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyRTVisibleMask](xengine-kit-xengine.md#hms_xeg_destroyrtvisiblemask) ([XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask) rtVisibleMask) | 销毁[XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask)对象。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateRTGI](xengine-kit-xengine.md#hms_xeg_creatertgi) (VkDevice device, const void \*pCreateInfo, [XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi) \*pRtGI) | 创建[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象。 |
| VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyRTGI](xengine-kit-xengine.md#hms_xeg_destroyrtgi) ([XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi) rtGI) | 销毁[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CmdRenderRTGI](xengine-kit-xengine.md#hms_xeg_cmdrenderrtgi) (VkCommandBuffer commandBuffer, [XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi) rtGI, const void \*pDescription) | 执行渲染命令。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateSpatialUpscale](xengine-kit-xengine.md#hms_xeg_createspatialupscale) (VkDevice device, const [XEG\_SpatialUpscaleCreateInfo](xengine-kit-xeg-spatialupscalecreateinfo.md) \*pXegSpatialUpscaleCreateInfo, [XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale) \*pXegSpatialUpscale) | 创建[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象。 |
| VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_CmdRenderSpatialUpscale](xengine-kit-xengine.md#hms_xeg_cmdrenderspatialupscale) (VkCommandBuffer commandBuffer, [XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale) xegSpatialUpscale, [XEG\_SpatialUpscaleDescription](xengine-kit-xeg-spatialupscaledescription.md) \*pXegSpatialUpscaleDescription) | 执行空域GPU超分渲染命令。 |
| VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroySpatialUpscale](xengine-kit-xengine.md#hms_xeg_destroyspatialupscale) ([XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale) xegSpatialUpscale) | 销毁[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateTemporalUpscale](xengine-kit-xengine.md#hms_xeg_createtemporalupscale) (VkDevice device, [XEG\_TemporalUpscaleCreateInfo](xengine-kit-xeg-temporalupscalecreateinfo.md) \*pTemporalUpscaleInfo, [XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale) \*pTemporalUpscale) | 创建[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象。 |
| VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_CmdRenderTemporalUpscale](xengine-kit-xengine.md#hms_xeg_cmdrendertemporalupscale) (VkCommandBuffer commandBuffer, [XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale) temporalUpscale, [XEG\_TemporalUpscaleDescription](xengine-kit-xeg-temporalupscaledescription.md) \*pDescription) | 录制时域AI超分渲染命令。 |
| VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyTemporalUpscale](xengine-kit-xengine.md#hms_xeg_destroytemporalupscale) ([XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale) temporalUpscale) | 销毁[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象。 |

## 宏定义说明

PhonePC/2in1TabletTV

### XEG\_adaptive\_vrs

PhonePC/2in1TabletTV

```
1. #define XEG_adaptive_vrs   1
```

**描述**

XEngine自适应VRS扩展特性宏定义。

**起始版本：** 5.0.0(12)

### XEG\_ADAPTIVE\_VRS\_ERROR\_SENSITIVITY

PhonePC/2in1TabletTV

```
1. #define XEG_ADAPTIVE_VRS_ERROR_SENSITIVITY   0x4U
```

**描述**

用于设置[HMS\_XEG\_AdaptiveVRSParameter](xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter)接口的ERROR\_SENSITIVITY参数，表示控制生成着色率图像的阈值。该值越大，平均着色率越小，即性能会越好但画质会劣化。建议取值范围为[0, 1]。

使用此宏定义时通过[HMS\_XEG\_AdaptiveVRSParameter](xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter)接口设置ERROR\_SENSITIVITY参数，向接口传递的param必须是GLfloat指针，否则将产生未定义行为，如渲染效果不正确或者程序崩溃。 可选参数，默认为0.5。

**起始版本：** 5.0.0(12)

### XEG\_ADAPTIVE\_VRS\_EXTENSION\_NAME

PhonePC/2in1TabletTV

```
1. #define XEG_ADAPTIVE_VRS_EXTENSION_NAME   "XEG_adaptive_vrs"
```

**描述**

XEngine自适应VRS扩展特性名称。

**起始版本：** 5.0.0(12)

### XEG\_ADAPTIVE\_VRS\_FLIP

PhonePC/2in1TabletTV

```
1. #define XEG_ADAPTIVE_VRS_FLIP   0x5U
```

**描述**

用于设置[HMS\_XEG\_AdaptiveVRSParameter](xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter)接口的FLIP参数，该参数用于控制是否执行图像上下翻转。

使用此宏定义时通过[HMS\_XEG\_AdaptiveVRSParameter](xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter)接口设置FLIP参数，向接口传递的param必须是GLboolean指针，否则将产生未定义行为，如渲染效果不正确或者程序崩溃。 可选参数，默认为false。true表示执行上下翻转，false表示不执行上下翻转。

**起始版本：** 5.0.0(12)

### XEG\_ADAPTIVE\_VRS\_INPUT\_REGION

PhonePC/2in1TabletTV

```
1. #define XEG_ADAPTIVE_VRS_INPUT_REGION   0x2U
```

**描述**

用于设置[HMS\_XEG\_AdaptiveVRSParameter](xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter)接口的INPUT\_REGION参数，表示上一帧渲染管线最终渲染的图像区域。

使用此宏定义时通过[HMS\_XEG\_AdaptiveVRSParameter](xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter)接口设置INPUT\_REGION参数，向接口传递的param必须是长度为4的GLuint类型数组，依次为渲染图像区域左下角的坐标和渲染图像区域的宽高，否则将产生未定义行为，如渲染效果不正确或者程序崩溃。 可选参数，默认为[0, 0, INPUT\_SIZE[0], INPUT\_SIZE[1]]。

**起始版本：** 5.0.0(12)

### XEG\_ADAPTIVE\_VRS\_INPUT\_SIZE

PhonePC/2in1TabletTV

```
1. #define XEG_ADAPTIVE_VRS_INPUT_SIZE   0x1U
```

**描述**

用于设置[HMS\_XEG\_AdaptiveVRSParameter](xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter)接口的INPUT\_SIZE参数，表示上一帧渲染管线最终渲染的图像宽度和高度。

使用此宏定义时通过[HMS\_XEG\_AdaptiveVRSParameter](xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter)接口设置INPUT\_SIZE参数，向接口传递的param必须是长度为2的GLsizei类型数组，否则将产生未定义行为，如渲染效果不正确或者程序崩溃。 必填参数，且需要保证和[HMS\_XEG\_DispatchAdaptiveVRS](xengine-kit-xengine.md#hms_xeg_dispatchadaptivevrs)的inputColorImage宽高相同。

**起始版本：** 5.0.0(12)

### XEG\_ADAPTIVE\_VRS\_TEXEL\_SIZE

PhonePC/2in1TabletTV

```
1. #define XEG_ADAPTIVE_VRS_TEXEL_SIZE   0x3U
```

**描述**

用于设置[HMS\_XEG\_AdaptiveVRSParameter](xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter)接口的TEXEL\_SIZE参数。

使用此宏定义时通过[HMS\_XEG\_AdaptiveVRSParameter](xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter)接口设置TEXEL\_SIZE参数，向接口传递的param必须是长度为2的GLsizei类型数组，依次为TEXEL\_WIDTH和TEXEL\_HEIGHT，否则将产生未定义行为，如渲染效果不正确或者程序崩溃。 可选参数，默认为[8, 8]，支持[8, 8]和[16, 16]。

**起始版本：** 5.0.0(12)

### XEG\_ADAPTIVE\_VRS\_VERSION

PhonePC/2in1TabletTV

```
1. #define XEG_ADAPTIVE_VRS_VERSION   1
```

**描述**

XEngine自适应VRS扩展特性版本号。

**起始版本：** 5.0.0(12)

### XEG\_EXTENSIONS

PhonePC/2in1TabletTV

```
1. #define XEG_EXTENSIONS   0x01U
```

**描述**

作为[HMS\_XEG\_GetString](xengine-kit-xengine.md#hms_xeg_getstring)接口的入参，以获取XEngine支持的OpenGL ES扩展特性。

**起始版本：** 5.0.0(12)

### XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME

PhonePC/2in1TabletTV

```
1. #define XEG_HPS_RADIX_SORT_EXTENSION_NAME   "XEG_hps_radix_sort"
```

**描述**

XEngine 高性能基数排序扩展特性名称。

**起始版本：** 6.0.0(20)

### XEG\_MAX\_EXTENSION\_NAME\_SIZE

PhonePC/2in1TabletTV

```
1. #define XEG_MAX_EXTENSION_NAME_SIZE   256
```

**描述**

XEngine扩展特性名称支持的最大长度。

**起始版本：** 5.0.0(12)

### XEG\_neural\_upscale

PhonePC/2in1TabletTV

```
1. #define XEG_neural_upscale   1
```

**描述**

XEngine空域AI超分扩展特性宏定义。

**起始版本：** 5.0.0(12)

### XEG\_NEURAL\_UPSCALE\_EXTENSION\_NAME

PhonePC/2in1TabletTV

```
1. #define XEG_NEURAL_UPSCALE_EXTENSION_NAME   "XEG_neural_upscale"
```

**描述**

XEngine空域AI超分扩展特性名称。

**起始版本：** 5.0.0(12)

### XEG\_NEURAL\_UPSCALE\_INPUT\_HANDLE

PhonePC/2in1TabletTV

```
1. #define XEG_NEURAL_UPSCALE_INPUT_HANDLE   0x4U
```

**描述**

用于通过[HMS\_XEG\_NeuralUpscaleParameter](xengine-kit-xengine.md#hms_xeg_neuralupscaleparameter)接口设置与超分输入纹理关联的OH\_NativeBuffer handle。

使用此宏定义设置超分输入参数时，向接口传递的param值必须是与向[HMS\_XEG\_RenderNeuralUpscale](xengine-kit-xengine.md#hms_xeg_renderneuralupscale)接口传递的inputTexture纹理参数对应的合法的OH\_NativeBuffer handle，否则将产生未定义行为，如渲染效果不正确或者程序崩溃。 必选参数。

**起始版本：** 5.0.0(12)

### XEG\_NEURAL\_UPSCALE\_SCISSOR

PhonePC/2in1TabletTV

```
1. #define XEG_NEURAL_UPSCALE_SCISSOR   0x1U
```

**描述**

用于通过[HMS\_XEG\_NeuralUpscaleParameter](xengine-kit-xengine.md#hms_xeg_neuralupscaleparameter)接口设置超分的裁剪窗口参数，裁剪窗口用于确定对输入图像采样的区域。

使用此宏定义设置裁剪窗口参数时，向接口传递的param值必须是长度为4的无符号整数数组，否则将产生未定义行为，如渲染效果不正确或者程序崩溃。数组中的值依次为：x， y， width， height，其中x、y确定裁剪窗口的左下角，width、height分别确定裁剪窗口的宽和高。 可选参数，不设置裁剪窗口参数时的默认值为（0， 0， 输入纹理的宽， 输入纹理的高）。

**起始版本：** 5.0.0(12)

### XEG\_NEURAL\_UPSCALE\_SHARPNESS

PhonePC/2in1TabletTV

```
1. #define XEG_NEURAL_UPSCALE_SHARPNESS   0x2U
```

**描述**

用于通过[HMS\_XEG\_NeuralUpscaleParameter](xengine-kit-xengine.md#hms_xeg_neuralupscaleparameter)接口设置超分的锐化度参数，锐化度的建议取值范围为[0, 1]。

使用此宏定义设置超分的锐化度参数时，向接口传递的param值必须是指向一个float值的合法指针，否则将产生未定义行为，如渲染效果不正确或者程序崩溃。 可选参数，不设置锐化度参数时的默认值为0.2。

**起始版本：** 5.0.0(12)

### XEG\_NEURAL\_UPSCALE\_VERSION

PhonePC/2in1TabletTV

```
1. #define XEG_NEURAL_UPSCALE_VERSION   1
```

**描述**

XEngine空域AI超分扩展特性版本号。

**起始版本：** 5.0.0(12)

### XEG\_RT\_REFLECTION\_EXTENSION\_NAME

PhonePC/2in1TabletTV

```
1. #define XEG_RT_REFLECTION_EXTENSION_NAME   "XEG_rt_reflection"
```

**描述**

XEngine光线追踪反射扩展特性名称。

**起始版本：** 6.0.0(20)

### XEG\_RT\_SHADOW\_AO\_EXTENSION\_NAME

PhonePC/2in1TabletTV

```
1. #define XEG_RT_SHADOW_AO_EXTENSION_NAME   "XEG_rt_shadow_ao"
```

**描述**

XEngine光线追踪阴影和环境光遮蔽扩展特性名称。

**起始版本：** 6.0.0(20)

### XEG\_RTGI\_EXTENSION\_NAME

PhonePC/2in1TabletTV

```
1. #define XEG_RTGI_EXTENSION_NAME   "XEG_rtgi"
```

**描述**

XEngine光线追踪全局光照扩展特性名称。

**起始版本：** 6.0.0(20)

### XEG\_spatial\_upscale

PhonePC/2in1TabletTV

```
1. #define XEG_spatial_upscale   1
```

**描述**

XEngine空域GPU超分扩展特性宏定义。

**起始版本：** 5.0.0(12)

### XEG\_SPATIAL\_UPSCALE\_EXTENSION\_NAME

PhonePC/2in1TabletTV

```
1. #define XEG_SPATIAL_UPSCALE_EXTENSION_NAME   "XEG_spatial_upscale"
```

**描述**

XEngine空域GPU超分扩展特性名称。

**起始版本：** 5.0.0(12)

### XEG\_SPATIAL\_UPSCALE\_SCISSOR

PhonePC/2in1TabletTV

```
1. #define XEG_SPATIAL_UPSCALE_SCISSOR   0x1U
```

**描述**

用于设置[HMS\_XEG\_SpatialUpscaleParameter](xengine-kit-xengine.md#hms_xeg_spatialupscaleparameter)接口的SCISSOR参数。

使用此宏定义时通过[HMS\_XEG\_SpatialUpscaleParameter](xengine-kit-xengine.md#hms_xeg_spatialupscaleparameter)接口设置SCISSOR参数，向接口传递的param值必须是指向长度为4的无符号整数数组的指针，否则将产生未定义行为，如渲染效果不正确或者程序崩溃。 SCISSOR四个值依次为裁剪窗口的左下角点的x与y的值和裁剪窗口的宽高。

**起始版本：** 5.0.0(12)

### XEG\_SPATIAL\_UPSCALE\_SHARPNESS

PhonePC/2in1TabletTV

```
1. #define XEG_SPATIAL_UPSCALE_SHARPNESS   0x2U
```

**描述**

用于设置[HMS\_XEG\_SpatialUpscaleParameter](xengine-kit-xengine.md#hms_xeg_spatialupscaleparameter)接口的SHARPNESS参数。

使用此宏定义时通过[HMS\_XEG\_SpatialUpscaleParameter](xengine-kit-xengine.md#hms_xeg_spatialupscaleparameter)接口设置SHARPNESS参数，向接口传递的param值必须是指向float类型的指针。SHARPNESS参数建议取值范围为[0, 1]，否则将产生未定义行为，如渲染效果不正确或者程序崩溃。 SHARPNESS参数越大锐化效果越强，不同风格图像锐化值需要调整，否则会导致过度锐化现象，如出现大量噪点。

**起始版本：** 5.0.0(12)

### XEG\_SPATIAL\_UPSCALE\_VERSION

PhonePC/2in1TabletTV

```
1. #define XEG_SPATIAL_UPSCALE_VERSION   1
```

**描述**

XEngine空域GPU超分扩展特性版本号。

**起始版本：** 5.0.0(12)

### XEG\_temporal\_upscale

PhonePC/2in1TabletTV

```
1. #define XEG_temporal_upscale   1
```

**描述**

XEngine时域AI超分扩展特性宏定义。

**起始版本：** 5.0.0(12)

### XEG\_TEMPORAL\_UPSCALE\_DEPTH\_REVERSED

PhonePC/2in1TabletTV

```
1. #define XEG_TEMPORAL_UPSCALE_DEPTH_REVERSED   0x3U
```

**描述**

用于通过[HMS\_XEG\_TemporalUpscaleParameter](xengine-kit-xengine.md#hms_xeg_temporalupscaleparameter)接口设置是否存在深度反转。true表示存在深度反转，false表示不存在深度反转。

使用此宏定义设置是否存在深度反转时，向接口传递的param值必须是指向一个GLboolean值的合法指针，否则将产生未定义行为，如渲染效果不正确或者程序崩溃。必选参数。

**起始版本：** 6.0.0(20)

### XEG\_TEMPORAL\_UPSCALE\_EXTENSION\_NAME

PhonePC/2in1TabletTV

```
1. #define XEG_TEMPORAL_UPSCALE_EXTENSION_NAME   "XEG_temporal_upscale"
```

**描述**

XEngine时域AI超分扩展特性名称。

**起始版本：** 5.0.0(12)

### XEG\_TEMPORAL\_UPSCALE\_INPUT\_SIZE

PhonePC/2in1TabletTV

```
1. #define XEG_TEMPORAL_UPSCALE_INPUT_SIZE   0x1U
```

**描述**

用于通过[HMS\_XEG\_TemporalUpscaleParameter](xengine-kit-xengine.md#hms_xeg_temporalupscaleparameter)接口设置超分输入纹理的真实宽高。

使用此宏定义设置输入宽高时，向接口传递的param值必须是长度为2的无符号整数数组，否则将产生未定义行为，如渲染效果不正确或者程序崩溃。数组中的值依次为：width, height。width和height分别确定输入纹理的宽和高。必选参数。

**起始版本：** 6.0.0(20)

### XEG\_TEMPORAL\_UPSCALE\_JITTER\_NUM

PhonePC/2in1TabletTV

```
1. #define XEG_TEMPORAL_UPSCALE_JITTER_NUM   0x2U
```

**描述**

用于通过[HMS\_XEG\_TemporalUpscaleParameter](xengine-kit-xengine.md#hms_xeg_temporalupscaleparameter)接口设置相机抖动的周期数，取值范围为[4, 16]，推荐8。

使用此宏定义设置相机抖动的周期数时，向接口传递的param值必须是指向一个GLuint值的合法指针，否则将产生未定义行为，如渲染效果不正确或者程序崩溃。必选参数。

**起始版本：** 6.0.0(20)

### XEG\_TEMPORAL\_UPSCALE\_RESET\_HISTORY

PhonePC/2in1TabletTV

```
1. #define XEG_TEMPORAL_UPSCALE_RESET_HISTORY   0x4U
```

**描述**

用于通过[HMS\_XEG\_TemporalUpscaleParameter](xengine-kit-xengine.md#hms_xeg_temporalupscaleparameter)接口设置是否重置历史帧数据，true表示重置，false表示不重置。在历史帧未使用超分，并且当前帧开始使用超分的情况下建议设置为true。

使用此宏定义设置是否重置历史帧数据时，向接口传递的param值必须是指向一个GLboolean值的合法指针，否则将产生未定义行为，如渲染效果不正确或者程序崩溃。必选参数。

**起始版本：** 6.0.0(20)

### XEG\_TEMPORAL\_UPSCALE\_STEADY\_LEVEL

PhonePC/2in1TabletTV

```
1. #define XEG_TEMPORAL_UPSCALE_STEADY_LEVEL   0x5U
```

**描述**

用于通过[HMS\_XEG\_TemporalUpscaleParameter](xengine-kit-xengine.md#hms_xeg_temporalupscaleparameter)接口设置画面偏向当前帧（鬼影少但可能存在闪烁）还是历史帧（鬼影多但是更稳定）的平衡程度。取值范围为[0.0, 1.0]，值越大越偏向历史帧。

使用此宏定义设置平衡程度时，向接口传递的param值必须是指向一个GLfloat值的合法指针，否则将产生未定义行为，如渲染效果不正确或者程序崩溃。可选参数，默认值是0.5。

**起始版本：** 6.0.0(20)

### XEG\_TEMPORAL\_UPSCALE\_VERSION

PhonePC/2in1TabletTV

```
1. #define XEG_TEMPORAL_UPSCALE_VERSION   1
```

**描述**

XEngine时域AI超分扩展特性版本号。

**起始版本：** 5.0.0(12)

## 类型定义说明

PhonePC/2in1TabletTV

### PFN\_HMS\_XEG\_ADAPTIVEVRSPARAMETER

PhonePC/2in1TabletTV

```
1. typedef void(GL_APIENTRYP PFN_HMS_XEG_ADAPTIVEVRSPARAMETER) (GLenum pname, GLvoid *param)
```

**描述**

设置自适应VRS输入参数的函数指针定义。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| pname | 输入参数的枚举名，取值范围是[XEG\_ADAPTIVE\_VRS\_INPUT\_SIZE](xengine-kit-xengine.md#xeg_adaptive_vrs_input_size)、[XEG\_ADAPTIVE\_VRS\_INPUT\_REGION](xengine-kit-xengine.md#xeg_adaptive_vrs_input_region)、[XEG\_ADAPTIVE\_VRS\_TEXEL\_SIZE](xengine-kit-xengine.md#xeg_adaptive_vrs_texel_size)、[XEG\_ADAPTIVE\_VRS\_ERROR\_SENSITIVITY](xengine-kit-xengine.md#xeg_adaptive_vrs_error_sensitivity)、[XEG\_ADAPTIVE\_VRS\_FLIP](xengine-kit-xengine.md#xeg_adaptive_vrs_flip)。 |
| param | 输入参数值，取值详见输入参数枚举名的说明。 |

### PFN\_HMS\_XEG\_APPLYADAPTIVEVRS

PhonePC/2in1TabletTV

```
1. typedef void(GL_APIENTRYP PFN_HMS_XEG_APPLYADAPTIVEVRS) (GLuint shadingRateImage)
```

**描述**

将着色率图像应用到渲染目标中的函数指针定义。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| shadingRateImage | 计算得到的着色率图像，传入0表示关闭自适应VRS。 |

### PFN\_HMS\_XEG\_CmdDispatchAdaptiveVRS

PhonePC/2in1TabletTV

```
1. typedef void(VKAPI_PTR * PFN_HMS_XEG_CmdDispatchAdaptiveVRS) (VkCommandBuffer commandBuffer, XEG_AdaptiveVRS xegAdaptiveVRS, XEG_AdaptiveVRSDescription *pXegAdaptiveVRSDescription)
```

**描述**

执行计算自适应可变着色率命令的函数指针定义。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| commandBuffer | 当前记录命令的VkCommandBuffer，此VkCommandBuffer必须被提交到vkQueueSubmit，否则无法执行。 |
| xegAdaptiveVRS | 已创建的[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象。 |
| pXegAdaptiveVRSDescription | 下发命令的参数结构体[XEG\_AdaptiveVRSDescription](xengine-kit-xeg-adaptivevrsdescription.md)的指针，不允许为空。 |

### PFN\_HMS\_XEG\_CmdRadixSortHPS

PhonePC/2in1TabletTV

```
1. typedef VkResult(VKAPI_PTR * PFN_HMS_XEG_CmdRadixSortHPS) (VkCommandBuffer commandBuffer, XEG_HPS hps, const XEG_HPSRadixSortDescription *pDescription)
```

**描述**

录制HPS排序命令的函数指针定义，使用此接口前需要通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询是否支持[XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_hps_radix_sort_extension_name)扩展。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| commandBuffer | Vulkan命令缓冲对象。 |
| hps | 已创建的[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)对象。 |
| pDescription | [XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_hps_radix_sort_extension_name)扩展输入信息结构体[XEG\_HPSRadixSortDescription](xengine-kit-xeg-hpsradixsortdescription.md)的指针，不允许为空。 |

**返回：**

返回一个VkResult类型的错误码，返回值为VK\_SUCCESS表示执行成功。

### PFN\_HMS\_XEG\_CmdRenderRTGI

PhonePC/2in1TabletTV

```
1. typedef VkResult(VKAPI_PTR * PFN_HMS_XEG_CmdRenderRTGI) (VkCommandBuffer commandBuffer, XEG_RTGI rtGI, const void *pDescription)
```

**描述**

执行渲染命令的函数指针定义。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| commandBuffer | 当前记录命令的VkCommandBuffer，此VkCommandBuffer必须被提交到vkQueueSubmit，否则无法执行。 |
| rtGI | 已创建的[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象。 |
| pDescription | 执行渲染命令的信息结构体的指针，若使用DDGI渲染，为结构体[XEG\_DDGIDescription](xengine-kit-xeg-ddgidescription.md)的指针，若使用NNGI渲染，为结构体[XEG\_NNGIDescription](xengine-kit-xeg-nngidescription.md)的指针，不允许为空。 |

**返回：**

返回一个VkResult类型的错误码，返回值为VK\_SUCCESS表示执行成功。

### PFN\_HMS\_XEG\_CmdRenderRTReflection

PhonePC/2in1TabletTV

```
1. typedef VkResult VKAPI_ATTR* PFN_HMS_XEG_CmdRenderRTReflection(VkCommandBuffer commandBuffer, XEG_RTReflection rtReflection, const void *pDescription)
```

**描述**

录制计算RT反射命中信息命令的函数指针定义。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| commandBuffer | Vulkan命令缓冲对象，需要是Primary类型。 |
| rtReflection | 已创建的[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象。 |
| pDescription | 反射渲染输入信息结构体[XEG\_RTReflectionDescription](xengine-kit-xeg-rtreflectiondescription.md)的指针，不允许为空。 |

### PFN\_HMS\_XEG\_CmdRenderRTVisibleMask

PhonePC/2in1TabletTV

```
1. typedef VkResult(VKAPI_PTR * PFN_HMS_XEG_CmdRenderRTVisibleMask) (VkCommandBuffer commandBuffer, XEG_RTVisibleMask rtVisibleMask, const void *pDescription)
```

**描述**

录制光线追踪VisibleMask渲染命令的函数指针定义。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| commandBuffer | Vulkan命令缓冲对象。 |
| rtVisibleMask | 已创建的[XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask)对象。 |
| pDescription | 执行渲染命令的输入参数结构体指针，当前仅支持[XEG\_RTShadowAODescription](xengine-kit-xeg-rtshadowaodescription.md)类型的指针，不允许为空。 |

**返回：**

VkResult类型的错误码，值为VK\_SUCCESS时表示执行成功。

### PFN\_HMS\_XEG\_CmdRenderSpatialUpscale

PhonePC/2in1TabletTV

```
1. typedef void(VKAPI_PTR * PFN_HMS_XEG_CmdRenderSpatialUpscale) (VkCommandBuffer commandBuffer, XEG_SpatialUpscale xegSpatialUpscale, XEG_SpatialUpscaleDescription *pXegSpatialUpscaleDescription)
```

**描述**

执行空域GPU超分渲染命令的函数指针定义。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| commandBuffer | 当前记录命令的VkCommandBuffer，此VkCommandBuffer必须被提交到vkQueueSubmit，否则无法执行超分。 |
| xegSpatialUpscale | 已创建的[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象。 |
| pXegSpatialUpscaleDescription | 渲染命令的参数结构体[XEG\_SpatialUpscaleDescription](xengine-kit-xeg-spatialupscaledescription.md)的指针，不允许为空。 |

### PFN\_HMS\_XEG\_CmdRenderTemporalUpscale

PhonePC/2in1TabletTV

```
1. typedef void(VKAPI_ATTR * PFN_HMS_XEG_CmdRenderTemporalUpscale) (VkCommandBuffer commandBuffer, XEG_TemporalUpscale temporalUpscale, XEG_TemporalUpscaleDescription *pDescription)
```

**描述**

录制时域AI超分渲染命令的函数指针定义。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| commandBuffer | Vulkan命令缓冲对象，需要是Primary类型。 |
| temporalUpscale | 已创建的[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象。 |
| pDescription | 超分渲染输入信息结构体[XEG\_TemporalUpscaleDescription](xengine-kit-xeg-temporalupscaledescription.md)的指针，不允许为空。 |

### PFN\_HMS\_XEG\_CmdSetSynchronization

PhonePC/2in1TabletTV

```
1. typedef VkResult(VKAPI_PTR * PFN_HMS_XEG_CmdSetSynchronization) (VkCommandBuffer commandBuffer, const void *xegHandle)
```

**描述**

设置同步信号，等待渲染结果写入指定图像的函数指针定义。使用RTGI特性时，为等待GI渲染结果到写入指定图像。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| commandBuffer | 当前记录命令的VkCommandBuffer，此VkCommandBuffer必须被提交到vkQueueSubmit，否则无法执行。 |
| xegHandle | 已创建句柄对象。使用RTGI特性时，为已创建的[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象。 |

**返回：**

返回一个VkResult类型的错误码，返回值为VK\_SUCCESS表示执行成功。

### PFN\_HMS\_XEG\_CreateAdaptiveVRS

PhonePC/2in1TabletTV

```
1. typedef VkResult(VKAPI_PTR * PFN_HMS_XEG_CreateAdaptiveVRS) (VkDevice device, const XEG_AdaptiveVRSCreateInfo *pXegAdaptiveVRSCreateInfo, XEG_AdaptiveVRS *pXegAdaptiveVRS)
```

**描述**

创建[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象的函数指针定义。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| device | 必须是当前使用的VkDevice。 |
| pXegAdaptiveVRSCreateInfo | 结构体[XEG\_AdaptiveVRSCreateInfo](xengine-kit-xeg-adaptivevrscreateinfo.md)的指针，不允许为空。 |
| pXegAdaptiveVRS | 指向句柄的指针，创建的[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)在此句柄中返回。 |

**返回：**

返回一个VkResult类型的错误码，返回值为VK\_SUCCESS表示执行成功。

### PFN\_HMS\_XEG\_CreateHPS

PhonePC/2in1TabletTV

```
1. typedef VkResult(VKAPI_PTR * PFN_HMS_XEG_CreateHPS) (VkDevice device, const XEG_HPSCreateInfo *pCreateInfo, XEG_HPS *pHps)
```

**描述**

创建[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)对象的函数指针定义。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| device | 必须是当前使用的VkDevice。 |
| pCreateInfo | [XEG\_HPS](xengine-kit-xengine.md#xeg_hps)实例句柄创建信息结构体的指针。不允许为空。 |
| pHps | 指向HPS实例句柄的指针，创建的[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)在此句柄中返回。 |

**返回：**

返回一个VkResult类型的错误码，返回值为VK\_SUCCESS表示执行成功。

### PFN\_HMS\_XEG\_CreateRTGI

PhonePC/2in1TabletTV

```
1. typedef VkResult(VKAPI_PTR * PFN_HMS_XEG_CreateRTGI) (VkDevice device, const void *pCreateInfo, XEG_RTGI *pRtGI)
```

**描述**

创建[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象的函数指针定义。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| device | 必须是当前使用的VkDevice。 |
| pCreateInfo | 创建[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象的信息结构体的指针，若创建DDGI句柄，为结构体[XEG\_DDGICreateInfo](xengine-kit-xeg-ddgicreateinfo.md)的指针，若创建NNGI句柄，为结构体[XEG\_NNGICreateInfo](xengine-kit-xeg-nngicreateinfo.md)的指针，不允许为空。 |
| pRtGI | 指向句柄的指针，创建的[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)在此句柄中返回。 |

**返回：**

返回一个VkResult类型的错误码，返回值为VK\_SUCCESS表示执行成功。

### PFN\_HMS\_XEG\_CreateRTReflection

PhonePC/2in1TabletTV

```
1. typedef VkResult(VKAPI_ATTR * PFN_HMS_XEG_CreateRTReflection) (VkDevice device, const void *pCreateInfo, XEG_RTReflection *pRtReflection)
```

**描述**

创建[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象的函数指针定义。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| device | 必须是当前使用的VkDevice。 |
| pCreateInfo | 反射实例句柄创建信息结构体的指针，当前仅支持[XEG\_RTReflectionCreateInfo](xengine-kit-xeg-rtreflectioncreateinfo.md)类型的指针，不允许为空。 |
| pRtReflection | 指向反射实例句柄的指针，创建的[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)在此句柄中返回。 |

**返回：**

返回一个VkResult类型的错误码，返回值为VK\_SUCCESS表示执行成功。

### PFN\_HMS\_XEG\_CreateRTVisibleMask

PhonePC/2in1TabletTV

```
1. typedef VkResult(VKAPI_PTR * PFN_HMS_XEG_CreateRTVisibleMask) (VkDevice device, const void *pCreateInfo, XEG_RTVisibleMask *pRTVisibleMask)
```

**描述**

创建[XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask)对象的函数指针定义。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| device | 必须是当前使用的VkDevice。 |
| pCreateInfo | 创建VisibleMask实例句柄所需描述信息的结构体的指针，当前仅支持[XEG\_RTShadowAOCreateInfo](xengine-kit-xeg-rtshadowaocreateinfo.md)类型的指针，不允许为空。 |
| pRTVisibleMask | 指向VisibleMask实例句柄的指针，创建的[XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask)在此句柄中返回。 |

**返回：**

VkResult类型的错误码，值为VK\_SUCCESS时表示创建成功。

### PFN\_HMS\_XEG\_CreateSpatialUpscale

PhonePC/2in1TabletTV

```
1. typedef VkResult(VKAPI_PTR * PFN_HMS_XEG_CreateSpatialUpscale) (VkDevice device, const XEG_SpatialUpscaleCreateInfo *pXegSpatialUpscaleCreateInfo, XEG_SpatialUpscale *pXegSpatialUpscale)
```

**描述**

创建[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象的函数指针定义。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| device | 必须是当前使用的VkDevice。 |
| pXegSpatialUpscaleCreateInfo | 结构体[XEG\_SpatialUpscaleCreateInfo](xengine-kit-xeg-spatialupscalecreateinfo.md)的指针，不允许为空。 |
| pXegSpatialUpscale | 指向句柄的指针，创建的[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)在此句柄中返回。 |

**返回：**

返回一个VkResult类型的错误码，返回值为VK\_SUCCESS表示执行成功。

### PFN\_HMS\_XEG\_CreateTemporalUpscale

PhonePC/2in1TabletTV

```
1. typedef VkResult(VKAPI_ATTR * PFN_HMS_XEG_CreateTemporalUpscale) (VkDevice device, XEG_TemporalUpscaleCreateInfo *pTemporalUpscaleInfo, XEG_TemporalUpscale *pTemporalUpscale)
```

**描述**

创建[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象的函数指针定义。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| device | 必须是当前使用的VkDevice。 |
| pTemporalUpscaleInfo | 超分实例句柄创建信息结构体[XEG\_TemporalUpscaleCreateInfo](xengine-kit-xeg-temporalupscalecreateinfo.md)的指针，不允许为空。 |
| pTemporalUpscale | 指向句柄的指针，创建的[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)在此句柄中返回。 |

**返回：**

返回一个VkResult类型的错误码，返回值为VK\_SUCCESS表示执行成功。

### PFN\_HMS\_XEG\_DestroyAdaptiveVRS

PhonePC/2in1TabletTV

```
1. typedef void(VKAPI_PTR * PFN_HMS_XEG_DestroyAdaptiveVRS) (XEG_AdaptiveVRS xegAdaptiveVRS)
```

**描述**

销毁[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象的函数指针定义。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| xegAdaptiveVRS | 已创建的[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象。 |

### PFN\_HMS\_XEG\_DestroyHPS

PhonePC/2in1TabletTV

```
1. typedef void(VKAPI_PTR * PFN_HMS_XEG_DestroyHPS) (XEG_HPS hps)
```

**描述**

销毁[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)对象的函数指针定义。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| hps | 需要销毁的[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)对象。 |

### PFN\_HMS\_XEG\_DestroyRTGI

PhonePC/2in1TabletTV

```
1. typedef void(VKAPI_PTR * PFN_HMS_XEG_DestroyRTGI) (XEG_RTGI rtGI)
```

**描述**

销毁[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象的函数指针定义。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| rtGI | 已创建的[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象。 |

### PFN\_HMS\_XEG\_DestroyRTReflection

PhonePC/2in1TabletTV

```
1. typedef void VKAPI_ATTR* PFN_HMS_XEG_DestroyRTReflection(XEG_RTReflection rtReflection)
```

**描述**

销毁[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象的函数指针定义。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| rtReflection | 需要销毁的[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象。 |

### PFN\_HMS\_XEG\_DestroyRTVisibleMask

PhonePC/2in1TabletTV

```
1. typedef void(VKAPI_PTR * PFN_HMS_XEG_DestroyRTVisibleMask) (XEG_RTVisibleMask rtVisibleMask)
```

**描述**

销毁[XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask)对象的函数指针定义。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| rtVisibleMask | 需要销毁的[XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask)对象。 |

### PFN\_HMS\_XEG\_DestroySpatialUpscale

PhonePC/2in1TabletTV

```
1. typedef void(VKAPI_PTR * PFN_HMS_XEG_DestroySpatialUpscale) (XEG_SpatialUpscale xegSpatialUpscale)
```

**描述**

销毁[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象的函数指针定义。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| xegSpatialUpscale | 已创建的[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象。 |

### PFN\_HMS\_XEG\_DestroyTemporalUpscale

PhonePC/2in1TabletTV

```
1. typedef void(VKAPI_ATTR * PFN_HMS_XEG_DestroyTemporalUpscale) (XEG_TemporalUpscale temporalUpscale)
```

**描述**

销毁[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象的函数指针定义。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| temporalUpscale | 需要销毁的[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象。 |

### PFN\_HMS\_XEG\_DISPATCHADAPTIVEVRS

PhonePC/2in1TabletTV

```
1. typedef void(GL_APIENTRYP PFN_HMS_XEG_DISPATCHADAPTIVEVRS) (GLfloat *reprojectionMatrix, GLuint inputColorImage, GLuint inputDepthImage, GLuint shadingRateImage)
```

**描述**

计算着色率图像的函数指针定义。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| reprojectionMatrix | 当前帧和上一帧进行计算的结果矩阵的指针，计算公式为：（上一帧投影矩阵\* 上一帧的观察矩阵）\* （（当前帧的投影矩阵\* 当前帧的观察矩阵）的逆矩阵），矩阵必须是4\*4列主序的矩阵。可选参数，非空时画质较优。 |
| inputColorImage | 上一帧渲染管线最终渲染结果颜色附件纹理ID。 |
| inputDepthImage | 当前帧渲染管线最终渲染结果深度附件纹理ID。 |
| shadingRateImage | 用于生成着色率图信息的纹理ID，需用户创建并输入。 |

说明

纹理类型需要是GL\_TEXTURE\_2D且mipLevels为1。

### PFN\_HMS\_XEG\_EnumerateDeviceExtensionProperties

PhonePC/2in1TabletTV

```
1. typedef VkResult(VKAPI_PTR * PFN_HMS_XEG_EnumerateDeviceExtensionProperties) (VkPhysicalDevice physicalDevice, uint32_t *pPropertyCount, XEG_ExtensionProperties *pProperties)
```

**描述**

XEngine Vulkan扩展特性查询接口函数指针定义。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| physicalDevice | 当前使用的Vulkan物理设备。 |
| pPropertyCount | 查询或传入扩展特性的数量，当**pProperties**为nullptr时返回当前支持的XEngine扩展特性数量。 当传入的**propertyCount**大于或等于真实支持的XEngine扩展特性数量时，通过**pProperties**返回查询信息，返回结果为VK\_SUCCESS。 当传入的**propertyCount**小于真实支持的XEngine扩展特性数量时，通过**pProperties**返回查询信息，但返回结果为VK\_INCOMPLETE。 |
| pProperties | 查询到的XEngine扩展特性，通过结构体[XEG\_ExtensionProperties](xengine-kit-xeg-extensionproperties.md)指针返回。 |

**返回：**

返回VkResult类型错误码，查询成功时返回值为VK\_SUCCESS。 当**pProperties**不为nullptr且传入的**propertyCount**小于实际支持的XEngine扩展特性数量时返回值为VK\_INCOMPLETE，表示查询特性不完整。

### PFN\_HMS\_XEG\_GETSTRING

PhonePC/2in1TabletTV

```
1. typedef const GLubyte *(GL_APIENTRYP PFN_HMS_XEG_GETSTRING) (GLenum name)
```

**描述**

XEngine OpenGL ES扩展特性查询接口函数指针定义。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| name | 输入参数的枚举名，取值范围为[XEG\_EXTENSIONS](xengine-kit-xengine.md#xeg_extensions)。 |

**返回：**

当参数为[XEG\_EXTENSIONS](xengine-kit-xengine.md#xeg_extensions)时，返回XEngine支持的空格分隔的扩展列表，注意扩展名不包含空格字符。查询结果异常则返回空。

### PFN\_HMS\_XEG\_NEURALUPSCALEPARAMETER

PhonePC/2in1TabletTV

```
1. typedef void(GL_APIENTRYP PFN_HMS_XEG_NEURALUPSCALEPARAMETER) (GLenum pname, GLvoid *param)
```

**描述**

设置空域AI超分输入参数的函数指针定义。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| pname | 输入参数的枚举名，取值范围为[XEG\_NEURAL\_UPSCALE\_SCISSOR](xengine-kit-xengine.md#xeg_neural_upscale_scissor)、[XEG\_NEURAL\_UPSCALE\_SHARPNESS](xengine-kit-xengine.md#xeg_neural_upscale_sharpness)、[XEG\_NEURAL\_UPSCALE\_INPUT\_HANDLE](xengine-kit-xengine.md#xeg_neural_upscale_input_handle)。 |
| param | 输入参数的值，取值详见输入参数枚举名的说明。 |

### PFN\_HMS\_XEG\_RENDERNEURALUPSCALE

PhonePC/2in1TabletTV

```
1. typedef void(GL_APIENTRYP PFN_HMS_XEG_RENDERNEURALUPSCALE) (GLuint inputTexture)
```

**描述**

执行空域AI超分渲染命令的函数指针定义。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputTexture | 超分输入纹理，输入纹理是GL\_TEXTURE\_2D类型且mipLevels为1，纹理的宽度取值范围是[448, 1728]，否则可能会引起AI推理结果错误。此输入纹理必须是由OH\_NativeBuffer创建的，并需要在调用此接口前将OH\_NativeBuffer对应的handle设置为超分的输入参数，详见接口[HMS\_XEG\_NeuralUpscaleParameter](xengine-kit-xengine.md#hms_xeg_neuralupscaleparameter)。 |

### PFN\_HMS\_XEG\_RENDERSPATIALUPSCALE

PhonePC/2in1TabletTV

```
1. typedef void(GL_APIENTRYP PFN_HMS_XEG_RENDERSPATIALUPSCALE) (GLuint inputTexture)
```

**描述**

执行空域GPU超分渲染命令的函数指针定义。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputTexture | 超分输入纹理，输入纹理是GL\_TEXTURE\_2D类型且mipLevels为1。此纹理必须在调用此接口前创建好，否则会导致渲染失败，如黑屏问题。 |

### PFN\_HMS\_XEG\_RenderTemporalUpscale

PhonePC/2in1TabletTV

```
1. typedef void(GL_APIENTRYP PFN_HMS_XEG_RenderTemporalUpscale) (GLuint inputTexture, GLuint depthTexture, GLuint motionVectorTexture, GLuint dynamicMaskTexture, GLfloat jitterX, GLfloat jitterY)
```

**描述**

执行时域AI超分渲染命令的函数指针定义。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputTexture | 超分输入纹理，输入纹理是GL\_TEXTURE\_2D类型且mipLevels为1，支持的最大尺寸为2048 \* 1024。 |
| depthTexture | 深度纹理。 |
| motionVectorTexture | 运动矢量图像。运动矢量的计算方式为当前渲染像素的NDC坐标的XY值减去上一帧的NDC坐标的XY值。 |
| dynamicMaskTexture | 物体的动态遮罩图像，格式需要是GL\_RED或其兼容格式。R通道的合法值为0.0，0.2或1.0，其中0.0表示静态物体，0.2表示运动物体如人物，1.0表示特效或半透明物体。 |
| jitterX | 相机在X方向上的抖动。 |
| jitterY | 相机在Y方向上的抖动。 |

### PFN\_HMS\_XEG\_SPATIALUPSCALEPARAMETER

PhonePC/2in1TabletTV

```
1. typedef void(GL_APIENTRYP PFN_HMS_XEG_SPATIALUPSCALEPARAMETER) (GLenum pname, GLvoid *param)
```

**描述**

设置空域GPU超分输入参数的函数指针定义。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| pname | 输入参数的枚举名，取值范围为[XEG\_SPATIAL\_UPSCALE\_SCISSOR](xengine-kit-xengine.md#xeg_spatial_upscale_scissor)、[XEG\_SPATIAL\_UPSCALE\_SHARPNESS](xengine-kit-xengine.md#xeg_spatial_upscale_sharpness)。 |
| param | 输入参数值，取值详见输入参数枚举名的说明。 |

### PFN\_HMS\_XEG\_TemporalUpscaleParameter

PhonePC/2in1TabletTV

```
1. typedef void(GL_APIENTRYP PFN_HMS_XEG_TemporalUpscaleParameter) (GLenum pname, GLvoid *param)
```

**描述**

设置时域AI超分输入参数的函数指针定义。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| pname | 输入参数的枚举名，取值范围为 [XEG\_TEMPORAL\_UPSCALE\_INPUT\_SIZE](xengine-kit-xengine.md#xeg_temporal_upscale_input_size)、[XEG\_TEMPORAL\_UPSCALE\_JITTER\_NUM](xengine-kit-xengine.md#xeg_temporal_upscale_jitter_num)、[XEG\_TEMPORAL\_UPSCALE\_DEPTH\_REVERSED](xengine-kit-xengine.md#xeg_temporal_upscale_depth_reversed)、[XEG\_TEMPORAL\_UPSCALE\_RESET\_HISTORY](xengine-kit-xengine.md#xeg_temporal_upscale_reset_history)、[XEG\_TEMPORAL\_UPSCALE\_STEADY\_LEVEL](xengine-kit-xengine.md#xeg_temporal_upscale_steady_level)。 |
| param | 输入参数的值，取值详见输入参数枚举名的说明。 |

### XEG\_AdaptiveVRS

PhonePC/2in1TabletTV

```
1. VK_DEFINE_HANDLE(XEG_AdaptiveVRS)
```

**描述**

[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)的句柄。

**起始版本：** 5.0.0(12)

### XEG\_AdaptiveVRSCreateInfo

PhonePC/2in1TabletTV

```
1. typedef struct XEG_AdaptiveVRSCreateInfo XEG_AdaptiveVRSCreateInfo
```

**描述**

此结构体描述创建[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象的参数信息，当结构体中的信息变化时，需要创建新的[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象。

**起始版本：** 5.0.0(12)

### XEG\_AdaptiveVRSDescription

PhonePC/2in1TabletTV

```
1. typedef struct XEG_AdaptiveVRSDescription XEG_AdaptiveVRSDescription
```

**描述**

此结构体描述下发绘制着色率纹理命令需要的参数信息，每一帧都需要进行更新。

**起始版本：** 5.0.0(12)

### XEG\_DenoiseQualityMode

PhonePC/2in1TabletTV

```
1. typedef enum XEG_DenoiseQualityMode XEG_DenoiseQualityMode
```

**描述**

去噪质量模式枚举。

**起始版本：** 6.0.0(20)

### XEG\_ExtensionProperties

PhonePC/2in1TabletTV

```
1. typedef struct XEG_ExtensionProperties XEG_ExtensionProperties
```

**描述**

此结构体描述通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询到的XEngine扩展特性集合。

**起始版本：** 5.0.0(12)

### XEG\_HPS

PhonePC/2in1TabletTV

```
1. VK_DEFINE_HANDLE(XEG_HPS)
```

**描述**

[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)的句柄。

**起始版本：** 6.0.0(20)

### XEG\_HPSCreateInfo

PhonePC/2in1TabletTV

```
1. typedef struct XEG_HPSCreateInfo XEG_HPSCreateInfo
```

**描述**

此结构体描述创建[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)对象的信息。

**起始版本：** 6.0.0(20)

### XEG\_HPSRadixSort

PhonePC/2in1TabletTV

```
1. typedef struct XEG_HPSRadixSort XEG_HPSRadixSort
```

**描述**

此结构体描述HPS基数排序扩展结构信息。

**起始版本：** 6.0.0(20)

### XEG\_HPSRadixSortDescription

PhonePC/2in1TabletTV

```
1. typedef struct XEG_HPSRadixSortDescription XEG_HPSRadixSortDescription
```

**描述**

此结构体描述使用[XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_hps_radix_sort_extension_name)扩展进行排序时所需的信息。

**起始版本：** 6.0.0(20)

### XEG\_RTGI

PhonePC/2in1TabletTV

```
1. VK_DEFINE_HANDLE(XEG_RTGI)
```

**描述**

[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)的句柄。

**起始版本：** 6.0.0(20)

### XEG\_RTGIQualityMode

PhonePC/2in1TabletTV

```
1. typedef enum XEG_RTGIQualityMode XEG_RTGIQualityMode
```

**描述**

输出图像质量模式的枚举。

**起始版本：** 6.0.0(20)

### XEG\_RTReflection

PhonePC/2in1TabletTV

```
1. VK_DEFINE_HANDLE(XEG_RTReflection)
```

**描述**

[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)的句柄。

**起始版本：** 6.0.0(20)

### XEG\_RTReflectionCreateInfo

PhonePC/2in1TabletTV

```
1. typedef struct XEG_RTReflectionCreateInfo XEG_RTReflectionCreateInfo
```

**描述**

此结构体描述创建[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象的信息。当结构体中的信息变化时，需要创建新的[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象。

**起始版本：** 6.0.0(20)

### XEG\_RTReflectionDescription

PhonePC/2in1TabletTV

```
1. typedef struct XEG_RTReflectionDescription XEG_RTReflectionDescription
```

**描述**

此结构体描述下发光线求交命令时的输入信息。

**起始版本：** 6.0.0(20)

### XEG\_RTVisibleMask

PhonePC/2in1TabletTV

```
1. VK_DEFINE_HANDLE(XEG_RTVisibleMask)
```

**描述**

[XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask)的句柄。表示光线追踪VisibleMask特性实例，支持阴影和环境光遮蔽效果。

**起始版本：** 6.0.0(20)

### XEG\_SpatialUpscale

PhonePC/2in1TabletTV

```
1. VK_DEFINE_HANDLE(XEG_SpatialUpscale)
```

**描述**

[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)的句柄。

**起始版本：** 5.0.0(12)

### XEG\_SpatialUpscaleCreateInfo

PhonePC/2in1TabletTV

```
1. typedef struct XEG_SpatialUpscaleCreateInfo XEG_SpatialUpscaleCreateInfo
```

**描述**

此结构体描述创建[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象的信息，当结构体中的信息变化时，需要创建新的[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象。

**起始版本：** 5.0.0(12)

### XEG\_SpatialUpscaleDescription

PhonePC/2in1TabletTV

```
1. typedef struct XEG_SpatialUpscaleDescription XEG_SpatialUpscaleDescription
```

**描述**

此结构体描述下发空域GPU超分渲染命令时需要的图像信息。

**起始版本：** 5.0.0(12)

### XEG\_StructureType

PhonePC/2in1TabletTV

```
1. typedef enum XEG_StructureType XEG_StructureType
```

**描述**

XEngine结构体类型的枚举。

**起始版本：** 6.0.0(20)

### XEG\_TemporalUpscale

PhonePC/2in1TabletTV

```
1. VK_DEFINE_HANDLE(XEG_TemporalUpscale)
```

**描述**

[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)的句柄。

**起始版本：** 5.0.0(12)

### XEG\_TemporalUpscaleCreateInfo

PhonePC/2in1TabletTV

```
1. typedef struct XEG_TemporalUpscaleCreateInfo XEG_TemporalUpscaleCreateInfo
```

**描述**

此结构体描述创建[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象的信息。当结构体中的信息变化时，需要创建新的[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象。

**起始版本：** 5.0.0(12)

### XEG\_TemporalUpscaleDescription

PhonePC/2in1TabletTV

```
1. typedef struct XEG_TemporalUpscaleDescription XEG_TemporalUpscaleDescription
```

**描述**

此结构体描述下发时域AI超分渲染命令时的输入信息。

**起始版本：** 5.0.0(12)

### XEG\_TraversalMode

PhonePC/2in1TabletTV

```
1. typedef enum XEG_TraversalMode XEG_TraversalMode
```

**描述**

遍历模式枚举。

**起始版本：** 6.0.0(20)

## 枚举类型说明

PhonePC/2in1TabletTV

### XEG\_DenoiseQualityMode

PhonePC/2in1TabletTV

```
1. enum XEG_DenoiseQualityMode
```

**描述**

去噪质量模式枚举。

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| XEG\_DENOISE\_QUALITY\_MODE\_NONE | 不进行去噪。 |
| XEG\_DENOISE\_QUALITY\_MODE\_QUALITY | 生成高质量的无噪声结果，但速度可能较慢。 |
| XEG\_DENOISE\_QUALITY\_MODE\_BALANCED | 生成较高质量的无噪声结果，速度适中。 |
| XEG\_DENOISE\_QUALITY\_MODE\_PERFORMANCES | 高性能地生成无噪声结果。 |

### XEG\_RTGIQualityMode

PhonePC/2in1TabletTV

```
1. enum XEG_RTGIQualityMode
```

**描述**

输出图像质量模式的枚举。

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| XEG\_RTGI\_QUALITY\_MODE\_QUALITY | 质量模式。 |
| XEG\_RTGI\_QUALITY\_MODE\_BALANCED | 平衡模式。 |
| XEG\_RTGI\_QUALITY\_MODE\_PERFORMANCE | 性能模式。 |

### XEG\_StructureType

PhonePC/2in1TabletTV

```
1. enum XEG_StructureType
```

**描述**

XEngine结构体类型的枚举。

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| XEG\_STRUCTURE\_TYPE\_RT\_SHADOWAO\_CREATE\_INFO | 结构体[XEG\_RTShadowAOCreateInfo](xengine-kit-xeg-rtshadowaocreateinfo.md)的类型。 |
| XEG\_STRUCTURE\_TYPE\_RT\_SHADOWAO\_DESCRIPTION | 结构体[XEG\_RTShadowAODescription](xengine-kit-xeg-rtshadowaodescription.md)的类型。 |
| XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_CREATE\_INFO | 结构体[XEG\_RTReflectionCreateInfo](xengine-kit-xeg-rtreflectioncreateinfo.md)的类型。 |
| XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_DESCRIPTION | 结构体[XEG\_RTReflectionDescription](xengine-kit-xeg-rtreflectiondescription.md)的类型。 |
| XEG\_STRUCTURE\_TYPE\_NNGI\_CREATE\_INFO | 结构体[XEG\_NNGICreateInfo](xengine-kit-xeg-nngicreateinfo.md)的类型。 |
| XEG\_STRUCTURE\_TYPE\_NNGI\_DESCRIPTION | 结构体[XEG\_NNGIDescription](xengine-kit-xeg-nngidescription.md)的类型。 |
| XEG\_STRUCTURE\_TYPE\_DDGI\_CREATE\_INFO | 结构体[XEG\_DDGICreateInfo](xengine-kit-xeg-ddgicreateinfo.md)的类型。 |
| XEG\_STRUCTURE\_TYPE\_DDGI\_DESCRIPTION | 结构体[XEG\_DDGIDescription](xengine-kit-xeg-ddgidescription.md)的类型。 |
| XEG\_STRUCTURE\_TYPE\_HPS\_CREATE\_INFO | 结构体[XEG\_HPSCreateInfo](xengine-kit-xeg-hpscreateinfo.md)的类型。 |
| XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT | 结构体[XEG\_HPSRadixSort](xengine-kit-xeg-hpsradixsort.md)的类型。 |
| XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT\_DESCRIPTION | 结构体[XEG\_HPSRadixSortDescription](xengine-kit-xeg-hpsradixsortdescription.md)的类型。 |

### XEG\_TraversalMode

PhonePC/2in1TabletTV

```
1. enum XEG_TraversalMode
```

**描述**

遍历模式枚举。

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| XEG\_TRAVERSAL\_MODE\_DEFAULT | 逐像素进行光线追踪场景遍历。 |
| XEG\_TRAVERSAL\_MODE\_PERFORMANCES | 通过算法进行场景遍历，性能更好，画质可能有细微的差别。 |

## 函数说明

PhonePC/2in1TabletTV

### HMS\_XEG\_AdaptiveVRSParameter()

PhonePC/2in1TabletTV

```
1. GL_APICALL void GL_APIENTRY HMS_XEG_AdaptiveVRSParameter (GLenum pname, GLvoid * param)
```

**描述**

设置自适应VRS的参数。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| pname | 输入参数的枚举名，取值范围是[XEG\_ADAPTIVE\_VRS\_INPUT\_SIZE](xengine-kit-xengine.md#xeg_adaptive_vrs_input_size)、[XEG\_ADAPTIVE\_VRS\_INPUT\_REGION](xengine-kit-xengine.md#xeg_adaptive_vrs_input_region)、[XEG\_ADAPTIVE\_VRS\_TEXEL\_SIZE](xengine-kit-xengine.md#xeg_adaptive_vrs_texel_size)、[XEG\_ADAPTIVE\_VRS\_ERROR\_SENSITIVITY](xengine-kit-xengine.md#xeg_adaptive_vrs_error_sensitivity)、[XEG\_ADAPTIVE\_VRS\_FLIP](xengine-kit-xengine.md#xeg_adaptive_vrs_flip)。 |
| param | 输入参数值，取值详见输入参数枚举名的说明。 |

### HMS\_XEG\_ApplyAdaptiveVRS()

PhonePC/2in1TabletTV

```
1. GL_APICALL void GL_APIENTRY HMS_XEG_ApplyAdaptiveVRS (GLuint shadingRateImage)
```

**描述**

将着色率图像应用到渲染目标中。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| shadingRateImage | 计算得到的着色率图像，传入0表示关闭自适应VRS。 |

### HMS\_XEG\_CmdDispatchAdaptiveVRS()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR void VKAPI_CALL HMS_XEG_CmdDispatchAdaptiveVRS (VkCommandBuffer commandBuffer, XEG_AdaptiveVRS xegAdaptiveVRS, XEG_AdaptiveVRSDescription * pXegAdaptiveVRSDescription)
```

**描述**

执行计算自适应可变着色率命令。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| commandBuffer | 当前记录命令的VkCommandBuffer，此VkCommandBuffer必须被提交到vkQueueSubmit，否则无法执行。 |
| xegAdaptiveVRS | 已创建的[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象。 |
| pXegAdaptiveVRSDescription | 下发命令的参数结构体[XEG\_AdaptiveVRSDescription](xengine-kit-xeg-adaptivevrsdescription.md)的指针，不允许为空。 |

### HMS\_XEG\_CmdRadixSortHPS()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CmdRadixSortHPS (VkCommandBuffer commandBuffer, XEG_HPS hps, const XEG_HPSRadixSortDescription * pDescription)
```

**描述**

录制HPS排序命令，使用此接口前需要通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询是否支持[XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_hps_radix_sort_extension_name)扩展。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| commandBuffer | Vulkan命令缓冲对象。 |
| hps | 已创建的[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)对象。 |
| pDescription | [XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_hps_radix_sort_extension_name)扩展输入信息结构体[XEG\_HPSRadixSortDescription](xengine-kit-xeg-hpsradixsortdescription.md)的指针，不允许为空。 |

**返回：**

返回一个VkResult类型的错误码，返回值为VK\_SUCCESS表示执行成功。

### HMS\_XEG\_CmdRenderRTGI()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CmdRenderRTGI (VkCommandBuffer commandBuffer, XEG_RTGI rtGI, const void * pDescription)
```

**描述**

执行渲染命令。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| commandBuffer | 当前记录命令的VkCommandBuffer，此VkCommandBuffer必须被提交到vkQueueSubmit，否则无法执行。 |
| rtGI | 已创建的[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象。 |
| pDescription | 执行渲染命令的信息结构体的指针，若使用DDGI渲染，为结构体[XEG\_DDGIDescription](xengine-kit-xeg-ddgidescription.md)的指针，若使用NNGI渲染，为结构体[XEG\_NNGIDescription](xengine-kit-xeg-nngidescription.md)的指针，不允许为空。 |

**返回：**

返回一个VkResult类型的错误码，返回值为VK\_SUCCESS表示执行成功。

### HMS\_XEG\_CmdRenderRTReflection()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CmdRenderRTReflection (VkCommandBuffer commandBuffer, XEG_RTReflection rtReflection, const void * pDescription)
```

**描述**

录制计算RT反射命中信息命令。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| commandBuffer | Vulkan命令缓冲对象，需要是Primary类型。 |
| rtReflection | 已创建的[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象。 |
| pDescription | 反射渲染输入信息结构体[XEG\_RTReflectionDescription](xengine-kit-xeg-rtreflectiondescription.md)的指针，不允许为空。 |

### HMS\_XEG\_CmdRenderRTVisibleMask()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CmdRenderRTVisibleMask (VkCommandBuffer commandBuffer, XEG_RTVisibleMask rtVisibleMask, const void * pDescription)
```

**描述**

录制光线追踪VisibleMask渲染命令。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| commandBuffer | Vulkan命令缓冲对象。 |
| rtVisibleMask | 已创建的[XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask)对象。 |
| pDescription | 执行渲染命令的输入参数结构体指针，当前仅支持[XEG\_RTShadowAODescription](xengine-kit-xeg-rtshadowaodescription.md)类型的指针，不允许为空。 |

**返回：**

VkResult类型的错误码，值为VK\_SUCCESS时表示执行成功。

### HMS\_XEG\_CmdRenderSpatialUpscale()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR void VKAPI_CALL HMS_XEG_CmdRenderSpatialUpscale (VkCommandBuffer commandBuffer, XEG_SpatialUpscale xegSpatialUpscale, XEG_SpatialUpscaleDescription * pXegSpatialUpscaleDescription)
```

**描述**

执行空域GPU超分渲染命令。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| commandBuffer | 当前记录命令的VkCommandBuffer，此VkCommandBuffer必须被提交到vkQueueSubmit，否则无法执行超分。 |
| xegSpatialUpscale | 已创建的[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象。 |
| pXegSpatialUpscaleDescription | 渲染命令的参数结构体[XEG\_SpatialUpscaleDescription](xengine-kit-xeg-spatialupscaledescription.md)的指针，不允许为空。 |

### HMS\_XEG\_CmdRenderTemporalUpscale()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR void VKAPI_CALL HMS_XEG_CmdRenderTemporalUpscale (VkCommandBuffer commandBuffer, XEG_TemporalUpscale temporalUpscale, XEG_TemporalUpscaleDescription * pDescription)
```

**描述**

录制时域AI超分渲染命令。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| commandBuffer | Vulkan命令缓冲对象，需要是Primary类型。 |
| temporalUpscale | 已创建的[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象。 |
| pDescription | 超分渲染输入信息结构体[XEG\_TemporalUpscaleDescription](xengine-kit-xeg-temporalupscaledescription.md)的指针，不允许为空。 |

### HMS\_XEG\_CmdSetSynchronization()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CmdSetSynchronization (VkCommandBuffer commandBuffer, const void * xegHandle )
```

**描述**

设置同步信号，等待渲染结果写入指定图像。使用RTGI特性时，为等待GI渲染结果写入指定图像。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| commandBuffer | 当前记录命令的VkCommandBuffer，此VkCommandBuffer必须被提交到vkQueueSubmit，否则无法执行。 |
| xegHandle | 已创建句柄对象。使用RTGI特性时，为已创建的[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象。 |

**返回：**

返回一个VkResult类型的错误码，返回值为VK\_SUCCESS表示执行成功。

### HMS\_XEG\_CreateAdaptiveVRS()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CreateAdaptiveVRS (VkDevice device, XEG_AdaptiveVRSCreateInfo * pXegAdaptiveVRSCreateInfo, XEG_AdaptiveVRS * pXegAdaptiveVRS)
```

**描述**

创建[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| device | 必须是当前使用的VkDevice。 |
| pXegAdaptiveVRSCreateInfo | 结构体[XEG\_AdaptiveVRSCreateInfo](xengine-kit-xeg-adaptivevrscreateinfo.md)的指针，不允许为空。 |
| pXegAdaptiveVRS | 指向句柄的指针，创建的[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)在此句柄中返回。 |

**返回：**

返回一个VkResult类型的错误码，返回值为VK\_SUCCESS表示执行成功。

### HMS\_XEG\_CreateHPS()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CreateHPS (VkDevice device, const XEG_HPSCreateInfo * pCreateInfo, XEG_HPS * pHps )
```

**描述**

创建[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)对象。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| device | 必须是当前使用的VkDevice。 |
| pCreateInfo | [XEG\_HPS](xengine-kit-xengine.md#xeg_hps)实例句柄创建信息结构体的指针。不允许为空。 |
| pHps | 指向HPS实例句柄的指针，创建的[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)在此句柄中返回。 |

**返回：**

返回一个VkResult类型的错误码，返回值为VK\_SUCCESS表示执行成功。

### HMS\_XEG\_CreateRTGI()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CreateRTGI (VkDevice device, const void * pCreateInfo, XEG_RTGI * pRtGI )
```

**描述**

创建[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| device | 必须是当前使用的VkDevice。 |
| pCreateInfo | 创建[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象的信息结构体的指针，若创建DDGI句柄，为结构体[XEG\_DDGICreateInfo](xengine-kit-xeg-ddgicreateinfo.md)的指针，若创建NNGI句柄，为结构体[XEG\_NNGICreateInfo](xengine-kit-xeg-nngicreateinfo.md)的指针，不允许为空。 |
| pRtGI | 指向句柄的指针，创建的[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)在此句柄中返回。 |

**返回：**

返回一个VkResult类型的错误码，返回值为VK\_SUCCESS表示执行成功。

### HMS\_XEG\_CreateRTReflection()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CreateRTReflection (VkDevice device, const void * pCreateInfo, XEG_RTReflection * pRtReflection )
```

**描述**

创建[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| device | 必须是当前使用的VkDevice。 |
| pCreateInfo | 反射实例句柄创建信息结构体的指针，当前仅支持[XEG\_RTReflectionCreateInfo](xengine-kit-xeg-rtreflectioncreateinfo.md)类型的指针，不允许为空。 |
| pRtReflection | 指向反射实例句柄的指针，创建的[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)在此句柄中返回。 |

**返回：**

返回一个VkResult类型的错误码，返回值为VK\_SUCCESS表示执行成功。

### HMS\_XEG\_CreateRTVisibleMask()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CreateRTVisibleMask (VkDevice device, const void * pCreateInfo, XEG_RTVisibleMask * pRTVisibleMask )
```

**描述**

创建[XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask)对象。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| device | 必须是当前使用的VkDevice。 |
| pCreateInfo | 创建VisibleMask实例句柄所需描述信息的结构体的指针，当前仅支持[XEG\_RTShadowAOCreateInfo](xengine-kit-xeg-rtshadowaocreateinfo.md)类型的指针，不允许为空。 |
| pRTVisibleMask | 指向VisibleMask实例句柄的指针，创建的[XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask)在此句柄中返回。 |

**返回：**

VkResult类型的错误码，值为VK\_SUCCESS时表示创建成功。

### HMS\_XEG\_CreateSpatialUpscale()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CreateSpatialUpscale (VkDevice device, const XEG_SpatialUpscaleCreateInfo * pXegSpatialUpscaleCreateInfo, XEG_SpatialUpscale * pXegSpatialUpscale)
```

**描述**

创建[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| device | 必须是当前使用的VkDevice。 |
| pXegSpatialUpscaleCreateInfo | 结构体[XEG\_SpatialUpscaleCreateInfo](xengine-kit-xeg-spatialupscalecreateinfo.md)的指针，不允许为空。 |
| pXegSpatialUpscale | 指向句柄的指针，创建的[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)在此句柄中返回。 |

**返回：**

返回一个VkResult类型的错误码，返回值为VK\_SUCCESS表示执行成功。

### HMS\_XEG\_CreateTemporalUpscale()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CreateTemporalUpscale (VkDevice device, XEG_TemporalUpscaleCreateInfo * pTemporalUpscaleInfo, XEG_TemporalUpscale * pTemporalUpscale)
```

**描述**

创建[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| device | 必须是当前使用的VkDevice。 |
| pTemporalUpscaleInfo | 超分实例句柄创建信息结构体[XEG\_TemporalUpscaleCreateInfo](xengine-kit-xeg-temporalupscalecreateinfo.md)的指针，不允许为空。 |
| pTemporalUpscale | 指向句柄的指针，创建的[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)在此句柄中返回。 |

**返回：**

返回一个VkResult类型的错误码，返回值为VK\_SUCCESS表示执行成功。

### HMS\_XEG\_DestroyAdaptiveVRS()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR void VKAPI_CALL HMS_XEG_DestroyAdaptiveVRS (XEG_AdaptiveVRS xegAdaptiveVRS)
```

**描述**

销毁[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| xegAdaptiveVRS | 已创建的[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象。 |

### HMS\_XEG\_DestroyHPS()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR void VKAPI_CALL HMS_XEG_DestroyHPS (XEG_HPS hps)
```

**描述**

销毁[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)对象。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| hps | 需要销毁的[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)对象。 |

### HMS\_XEG\_DestroyRTGI()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR void VKAPI_CALL HMS_XEG_DestroyRTGI (XEG_RTGI rtGI)
```

**描述**

销毁[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| rtGI | 已创建的[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象。 |

### HMS\_XEG\_DestroyRTReflection()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR void VKAPI_CALL HMS_XEG_DestroyRTReflection (XEG_RTReflection rtReflection)
```

**描述**

销毁[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| rtReflection | 需要销毁的[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象。 |

### HMS\_XEG\_DestroyRTVisibleMask()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR void VKAPI_CALL HMS_XEG_DestroyRTVisibleMask (XEG_RTVisibleMask rtVisibleMask)
```

**描述**

销毁[XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask)对象。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| rtVisibleMask | 需要销毁的[XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask)对象。 |

### HMS\_XEG\_DestroySpatialUpscale()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR void VKAPI_CALL HMS_XEG_DestroySpatialUpscale (XEG_SpatialUpscale xegSpatialUpscale)
```

**描述**

销毁[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| xegSpatialUpscale | 已创建的[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象。 |

### HMS\_XEG\_DestroyTemporalUpscale()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR void VKAPI_CALL HMS_XEG_DestroyTemporalUpscale (XEG_TemporalUpscale temporalUpscale)
```

**描述**

销毁[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| temporalUpscale | 需要销毁的[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象。 |

### HMS\_XEG\_DispatchAdaptiveVRS()

PhonePC/2in1TabletTV

```
1. GL_APICALL void GL_APIENTRY HMS_XEG_DispatchAdaptiveVRS (GLfloat * reprojectionMatrix, GLuint inputColorImage, GLuint inputDepthImage, GLuint shadingRateImage)
```

**描述**

计算着色率图像。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| reprojectionMatrix | 当前帧和上一帧进行计算的结果矩阵的指针，计算公式为：（上一帧投影矩阵\* 上一帧的观察矩阵）\* （（当前帧的投影矩阵\* 当前帧的观察矩阵）的逆矩阵），矩阵必须是4\*4列主序的矩阵。可选参数，非空时画质较优。 |
| inputColorImage | 上一帧渲染管线最终渲染结果颜色附件纹理ID。 |
| inputDepthImage | 当前帧渲染管线最终渲染结果深度附件纹理ID。 |
| shadingRateImage | 用于生成着色率图信息的纹理ID，需用户创建并输入。 |

说明

纹理类型需要是GL\_TEXTURE\_2D且mipLevels为1。

### HMS\_XEG\_EnumerateDeviceExtensionProperties()

PhonePC/2in1TabletTV

```
1. VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_EnumerateDeviceExtensionProperties (VkPhysicalDevice physicalDevice, uint32_t * pPropertyCount, XEG_ExtensionProperties * pProperties)
```

**描述**

XEngine Vulkan扩展特性查询接口。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| physicalDevice | 当前使用的Vulkan物理设备。 |
| pPropertyCount | 查询或传入扩展特性的数量，当**pProperties**为nullptr时返回当前支持的XEngine扩展特性数量。 当传入的**propertyCount**大于或等于真实支持的XEngine扩展特性数量时，通过**pProperties**返回查询信息，返回结果为VK\_SUCCESS。 当传入的**propertyCount**小于真实支持的XEngine扩展特性数量时，通过**pProperties**返回查询信息，但返回结果为VK\_INCOMPLETE。 |
| pProperties | 查询到的XEngine扩展特性，通过结构体[XEG\_ExtensionProperties](xengine-kit-xeg-extensionproperties.md)指针返回。 |

**返回：**

返回VkResult类型错误码，查询成功时返回值为VK\_SUCCESS。 当**pProperties**不为nullptr且传入的**propertyCount**小于实际支持的XEngine扩展特性数量时返回值为VK\_INCOMPLETE，表示查询特性不完整。

### HMS\_XEG\_GetString()

PhonePC/2in1TabletTV

```
1. const GLubyte* HMS_XEG_GetString (GLenum name)
```

**描述**

XEngine OpenGL ES扩展特性查询接口。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| name | 输入参数的枚举名，取值范围为[XEG\_EXTENSIONS](xengine-kit-xengine.md#xeg_extensions)。 |

**返回：**

当参数为[XEG\_EXTENSIONS](xengine-kit-xengine.md#xeg_extensions)时，返回XEngine支持的空格分隔的扩展列表，注意扩展名不包含空格字符。查询结果异常则返回空。

### HMS\_XEG\_NeuralUpscaleParameter()

PhonePC/2in1TabletTV

```
1. GL_APICALL void GL_APIENTRY HMS_XEG_NeuralUpscaleParameter (GLenum pname, GLvoid * param)
```

**描述**

设置空域AI超分输入参数。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| pname | 输入参数的枚举名，取值范围为[XEG\_NEURAL\_UPSCALE\_SCISSOR](xengine-kit-xengine.md#xeg_neural_upscale_scissor)、[XEG\_NEURAL\_UPSCALE\_SHARPNESS](xengine-kit-xengine.md#xeg_neural_upscale_sharpness)、[XEG\_NEURAL\_UPSCALE\_INPUT\_HANDLE](xengine-kit-xengine.md#xeg_neural_upscale_input_handle)。 |
| param | 输入参数值，取值详见输入参数枚举名的说明。 |

### HMS\_XEG\_RenderNeuralUpscale()

PhonePC/2in1TabletTV

```
1. GL_APICALL void GL_APIENTRY HMS_XEG_RenderNeuralUpscale (GLuint inputTexture)
```

**描述**

执行空域AI超分渲染命令。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputTexture | 超分输入纹理，输入纹理是GL\_TEXTURE\_2D类型且mipLevels为1，纹理的宽度取值范围是[448, 1728]，否则可能会引起AI推理结果错误。此输入纹理必须是由OH\_NativeBuffer创建的，并需要在调用此接口前将OH\_NativeBuffer对应的handle设置为超分的输入参数，详见接口[HMS\_XEG\_NeuralUpscaleParameter](xengine-kit-xengine.md#hms_xeg_neuralupscaleparameter)。 |

### HMS\_XEG\_RenderSpatialUpscale()

PhonePC/2in1TabletTV

```
1. GL_APICALL void GL_APIENTRY HMS_XEG_RenderSpatialUpscale (GLuint inputTexture)
```

**描述**

执行空域GPU超分渲染命令。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputTexture | 超分输入纹理，输入纹理是GL\_TEXTURE\_2D类型且mipLevels为1。此纹理必须在调用此接口前创建好，否则会导致渲染失败，如黑屏问题。 |

### HMS\_XEG\_RenderTemporalUpscale()

PhonePC/2in1TabletTV

```
1. GL_APICALL void GL_APIENTRY HMS_XEG_RenderTemporalUpscale (GLuint inputTexture, GLuint depthTexture, GLuint motionVectorTexture, GLuint dynamicMaskTexture, GLfloat jitterX, GLfloat jitterY )
```

**描述**

执行时域AI超分渲染命令。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputTexture | 超分输入纹理，输入纹理是GL\_TEXTURE\_2D类型且mipLevels为1，支持的最大尺寸为2048 \* 1024。 |
| depthTexture | 深度纹理。 |
| motionVectorTexture | 运动矢量图像。运动矢量的计算方式为当前渲染像素的NDC坐标的XY值减去上一帧的NDC坐标的XY值。 |
| dynamicMaskTexture | 物体的动态遮罩图像，格式需要是GL\_RED或其兼容格式。R通道的合法值为0.0，0.2或1.0，其中0.0表示静态物体，0.2表示运动物体如人物，1.0表示特效或半透明物体。 |
| jitterX | 相机在X方向上的抖动。 |
| jitterY | 相机在Y方向上的抖动。 |

### HMS\_XEG\_SpatialUpscaleParameter()

PhonePC/2in1TabletTV

```
1. GL_APICALL void GL_APIENTRY HMS_XEG_SpatialUpscaleParameter (GLenum pname, GLvoid * param)
```

**描述**

设置空域GPU超分输入参数。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| pname | 输入参数的枚举名，取值范围为[XEG\_SPATIAL\_UPSCALE\_SCISSOR](xengine-kit-xengine.md#xeg_spatial_upscale_scissor)、[XEG\_SPATIAL\_UPSCALE\_SHARPNESS](xengine-kit-xengine.md#xeg_spatial_upscale_sharpness)。 |
| param | 输入参数值，取值详见输入参数枚举名的说明。 |

### HMS\_XEG\_TemporalUpscaleParameter()

PhonePC/2in1TabletTV

```
1. GL_APICALL void GL_APIENTRY HMS_XEG_TemporalUpscaleParameter (GLenum pname, const GLvoid * param)
```

**描述**

设置时域AI超分输入参数。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| pname | 输入参数的枚举名，取值范围为[XEG\_TEMPORAL\_UPSCALE\_INPUT\_SIZE](xengine-kit-xengine.md#xeg_temporal_upscale_input_size)、[XEG\_TEMPORAL\_UPSCALE\_JITTER\_NUM](xengine-kit-xengine.md#xeg_temporal_upscale_jitter_num)、[XEG\_TEMPORAL\_UPSCALE\_DEPTH\_REVERSED](xengine-kit-xengine.md#xeg_temporal_upscale_depth_reversed)、[XEG\_TEMPORAL\_UPSCALE\_RESET\_HISTORY](xengine-kit-xengine.md#xeg_temporal_upscale_reset_history)、[XEG\_TEMPORAL\_UPSCALE\_STEADY\_LEVEL](xengine-kit-xengine.md#xeg_temporal_upscale_steady_level)。 |
| param | 输入参数的值，取值详见输入参数枚举名的说明。 |
