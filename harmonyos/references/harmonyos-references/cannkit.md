---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit
title: CANN
breadcrumb: API参考 > AI > CANN Kit（CANN异构计算框架服务） > C API > 模块 > CANN
category: harmonyos-references
scraped_at: 2026-04-28T08:18:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:afbcda1d046d4990bacb77fc9c4f4d4c5bca7a9fc0aea200accd280032f306e1
---

## 概述

PhonePC/2in1TabletTV

提供CANN Kit模型推理的相关接口。

**系统能力：** SystemCapability.AI.HiAIFoundation

**起始版本：** 4.1.0(11)

说明

CANN Kit的模型编译、加载、推理等基础功能接口已抽取放在[neural\_network\_core.h](capi-neural-network-core-h.md)中，此处重点描述高阶功能。

## 汇总

PhonePC/2in1TabletTV

### 文件

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [hiai\_aipp\_param.h](cannkit-hiai-aipp-param-8h.md) | 模型推理时动态AIPP对象创建，参数设置和查询的接口。 |
| [hiai\_helper.h](cannkit-hiai-helper-8h.md) | 查询CANN Kit版本以及检查模型支持情况的接口。 |
| [hiai\_options.h](cannkit-hiai-options-8h.md) | 选项参数的接口。 |
| [hiai\_single\_op.h](cannkit-hiai-single-op-8h.md) | 定义CANN Kit单算子接口，用于单算子的创建、计算以及Tensor和Buffer的管理。 |
| [hiai\_tensor.h](cannkit-hiai-tensor-8h.md) | 模型推理时使用的输入输出内存相关的辅助接口。 |

### 结构体

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| struct [HiAISingleOpDescriptor\_ConvolutionParam](cannkit-sopdesc-convparam.md) | [HMS\_HiAISingleOpDescriptor\_CreateConvolution](cannkit.md#hms_hiaisingleopdescriptor_createconvolution)输入参数。 |
| struct [HiAI\_SingleOpExecutorConvolutionParam](cannkit-sopexec-convparam.md) | [HMS\_HiAISingleOpExecutor\_CreateConvolution](cannkit.md#hms_hiaisingleopexecutor_createconvolution)输入参数。 |
| struct [HiAI\_SingleOpExecutorFusedConvolutionActivationParam](cannkit-sopexec-fusedconv-actparam.md) | [HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation](cannkit.md#hms_hiaisingleopexecutor_createfusedconvolutionactivation)输入参数。 |

### 类型定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| typedef struct [HiAI\_AippParam](cannkit.md#hiai_aippparam) [HiAI\_AippParam](cannkit.md#hiai_aippparam) | AIPP参数对象。 |
| typedef struct [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) | 单算子Tensor描述的句柄。 |
| typedef struct [HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer) [HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer) | 单算子Buffer句柄。 |
| typedef struct [HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) [HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) | 单算子Tensor句柄。 |
| typedef struct [HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions) [HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions) | 单算子选项句柄。 |
| typedef struct [HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor) [HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor) | 单算子的算子描述句柄。 |
| typedef struct [HiAISingleOpDescriptor\_ConvolutionParam](cannkit-sopdesc-convparam.md) | [HMS\_HiAISingleOpDescriptor\_CreateConvolution](cannkit.md#hms_hiaisingleopdescriptor_createconvolution)输入参数。 |
| typedef struct [HiAI\_SingleOpExecutorConvolutionParam](cannkit-sopexec-convparam.md) | [HMS\_HiAISingleOpExecutor\_CreateConvolution](cannkit.md#hms_hiaisingleopexecutor_createconvolution)输入参数。 |
| typedef struct [HiAI\_SingleOpExecutorFusedConvolutionActivationParam](cannkit-sopexec-fusedconv-actparam.md) | [HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation](cannkit.md#hms_hiaisingleopexecutor_createfusedconvolutionactivation)输入参数。 |
| typedef struct [HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor) [HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor) | 单算子执行器句柄。 |

### 枚举

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [HiAI\_ImageFormat](cannkit.md#hiai_imageformat) {  HIAI\_YUV420SP\_U8 = 0,  HIAI\_XRGB8888\_U8 = 1,  HIAI\_YUV400\_U8 = 2,  HIAI\_ARGB8888\_U8 = 3,  HIAI\_YUYV\_U8 = 4,  HIAI\_YUV422SP\_U8 = 5,  HIAI\_AYUV444\_U8 = 6,  HIAI\_RGB888\_U8 = 7,  HIAI\_BGR888\_U8 = 8,  HIAI\_YUV444SP\_U8 = 9,  HIAI\_YVU444SP\_U8 = 10,  HIAI\_IMAGE\_FORMAT\_INVALID = 255  } | CANN Kit推理支持的输入和输出Tensor的图片格式的枚举。 |
| [HiAI\_ImageColorSpace](cannkit.md#hiai_imagecolorspace) {  HIAI\_JPEG = 0,  HIAI\_BT\_601\_NARROW = 1,  HIAI\_BT\_601\_FULL = 2,  HIAI\_BT\_709\_NARROW = 3,  HIAI\_IMAGE\_COLOR\_SPACE\_INVALID = 4  } | 图像色域空间类型。 |
| [HiAI\_Compatibility](cannkit.md#hiai_compatibility) {  HIAI\_COMPATIBILITY\_COMPATIBLE = 0,  HIAI\_COMPATIBILITY\_INCOMPATIBLE = 1  } | 编译后模型兼容性结果。 |
| [HiAI\_FormatMode](cannkit.md#hiai_formatmode) {  HIAI\_FORMAT\_MODE\_NCHW = 0,  HIAI\_FORMAT\_MODE\_ORIGIN = 1  } | 模型编译时数据的排列格式。 |
| [HiAI\_DynamicShapeStatus](cannkit.md#hiai_dynamicshapestatus) {  HIAI\_DYNAMIC\_SHAPE\_DISABLED = 0,  HIAI\_DYNAMIC\_SHAPE\_ENABLED = 1  } | 是否使能编译前可变shape。 |
| [HiAI\_DynamicShapeCacheMode](cannkit.md#hiai_dynamicshapecachemode) {  HIAI\_DYNAMIC\_SHAPE\_CACHE\_BUILT\_MODEL = 0,  HIAI\_DYNAMIC\_SHAPE\_CACHE\_LOADED\_MODEL = 1  } | 编译前可变shape支持的模式。 |
| [HiAI\_ExecuteDevice](cannkit.md#hiai_executedevice) {  HIAI\_EXECUTE\_DEVICE\_NPU = 0,  HIAI\_EXECUTE\_DEVICE\_CPU = 1,  HIAI\_EXECUTE\_DEVICE\_GPU = 2  } | 模型运行时支持的设备类型。 |
| [HiAI\_FallbackMode](cannkit.md#hiai_fallbackmode) {  HIAI\_FALLBACK\_ENABLED = 0,  HIAI\_FALLBACK\_DISABLED = 1  } | 指定的硬件设备无法编译模型时，是否允许CANN Kit选择其他硬件设备，例如CPU。 |
| [HiAI\_DeviceMemoryReusePlan](cannkit.md#hiai_devicememoryreuseplan) { HIAI\_DEVICE\_MEMORY\_REUSE\_PLAN\_UNSET = 0,  HIAI\_DEVICE\_MEMORY\_REUSE\_PLAN\_LOW = 1,  HIAI\_DEVICE\_MEMORY\_REUSE\_PLAN\_HIGH = 2  } | 设备内存复用配置选项。 |
| [HiAI\_TuningStrategy](cannkit.md#hiai_tuningstrategy) {  HIAI\_TUNING\_STRATEGY\_OFF = 0,  HIAI\_TUNING\_STRATEGY\_ON\_DEVICE\_TUNING = 1,  HIAI\_TUNING\_STRATEGY\_ON\_DEVICE\_PREPROCESS\_TUNING = 2,  HIAI\_TUNING\_STRATEGY\_ON\_CLOUD\_TUNING = 3  } | 模型优化策略配置选项。 |
| [HiAI\_TuningMode](cannkit.md#hiai_tuningmode) {  HIAI\_TUNING\_MODE\_UNSET = 0,  HIAI\_TUNING\_MODE\_AUTO = 1,  HIAI\_TUNING\_MODE\_HETER = 2  } | 辅助调优模式。 |
| [HiAI\_BandMode](cannkit.md#hiai_bandmode) {  HIAI\_BANDMODE\_UNSET = 0,  HIAI\_BANDMODE\_LOW = 1,  HIAI\_BANDMODE\_NORMAL = 2,  HIAI\_BANDMODE\_HIGH = 3  } | 定义硬件之间带宽模式。 |
| [HiAI\_OmType](cannkit.md#hiai_omtype) {  HIAI\_OM\_TYPE\_OFF = 0,  HIAI\_OM\_TYPE\_PROFILING = 1,  HIAI\_OM\_TYPE\_DUMP = 2  } | 维测类型定义。 |
| [HiAI\_SingleOpDataType](cannkit.md#hiai_singleopdatatype) {  HIAI\_SINGLEOP\_DT\_FLOAT = 0,  HIAI\_SINGLEOP\_DT\_FLOAT16 = 1,  HIAI\_SINGLEOP\_DT\_UNDEFINED = 17  } | 单算子张量数据类型枚举。 |
| [HiAI\_SingleOpFormat](cannkit.md#hiai_singleopformat) {  HIAI\_SINGLEOP\_FORMAT\_NCHW = 0,  HIAI\_SINGLEOP\_FORMAT\_NHWC = 1,  HIAI\_SINGLEOP\_FORMAT\_ND = 2,  HIAI\_SINGLEOP\_FORMAT\_NC1HWC0 = 3,  HIAI\_SINGLEOP\_FORMAT\_NC4HW4 = 28,  HIAI\_SINGLEOP\_FORMAT\_NC8HW8 = 31,  HIAI\_SINGLEOP\_FORMAT\_RESERVED = 255  } | 单算子张量排布格式枚举。 |
| [HiAI\_SingleOpConvMode](cannkit.md#hiai_singleopconvmode) {  HIAI\_SINGLEOP\_CONV\_MODE\_COMMON = 0,  HIAI\_SINGLEOP\_CONV\_MODE\_TRANSPOSED = 1,  HIAI\_SINGLEOP\_CONV\_MODE\_DEPTHWISE = 2  } | 单算子卷积模式枚举。 |
| [HiAI\_SingleOpPadMode](cannkit.md#hiai_singleoppadmode) {  HIAI\_SINGLEOP\_PAD\_MODE\_SPECIFIC = 0,  HIAI\_SINGLEOP\_PAD\_MODE\_SAME = 1,  HIAI\_SINGLEOP\_PAD\_MODE\_SAME\_UPPER = 2,  HIAI\_SINGLEOP\_PAD\_MODE\_SAME\_LOWER = 3,  HIAI\_SINGLEOP\_PAD\_MODE\_VALID = 4  } | 单算子填充模式枚举。 |
| [HiAI\_SingleOpActivationType](cannkit.md#hiai_singleopactivationtype) {  HIAI\_SINGLEOP\_ACTIVATION\_TYPE\_RELU = 0,  HIAI\_SINGLEOP\_ACTIVATION\_TYPE\_RELU6 = 1  } | 单算子激活模式枚举。 |
| [HiAI\_SingleOpSupportStatus](cannkit.md#hiai_singleopsupportstatus) {  HIAI\_SINGLEOP\_OPTIMIZED = 0,  HIAI\_SINGLEOP\_COMMON = 1,  HIAI\_SINGLEOP\_UNSUPPORTED = 2  } | 单算子支持状态枚举。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [HiAI\_AippParam](cannkit.md#hiai_aippparam) \* [HMS\_HiAIAippParam\_Create](cannkit.md#hms_hiaiaippparam_create) (uint32\_t batchNum) | 根据batchNum创建动态AippParam对象。 |
| void \* [HMS\_HiAIAippParam\_GetData](cannkit.md#hms_hiaiaippparam_getdata) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam) | 获取AippParam申请的内存地址。 |
| uint32\_t [HMS\_HiAIAippParam\_GetDataSize](cannkit.md#hms_hiaiaippparam_getdatasize) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam) | 获取AippParam申请的内存大小。 |
| int [HMS\_HiAIAippParam\_GetInputIndex](cannkit.md#hms_hiaiaippparam_getinputindex) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam) | 查询AippParam对象所在输入的索引。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetInputIndex](cannkit.md#hms_hiaiaippparam_setinputindex) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, uint32\_t inputIndex) | 设置AippParam在输入上的索引。 |
| int [HMS\_HiAIAippParam\_GetInputAippIndex](cannkit.md#hms_hiaiaippparam_getinputaippindex) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam) | 查询AippParam对象在该输入的多个输出分支上的索引。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetInputAippIndex](cannkit.md#hms_hiaiaippparam_setinputaippindex) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, uint32\_t inputAippIndex) | 设置AippParam对象作用于该输入的多个输出分支上的索引。 |
| void [HMS\_HiAIAippParam\_Destroy](cannkit.md#hms_hiaiaippparam_destroy) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*\*aippParam) | 释放AippParam对象。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetInputFormat](cannkit.md#hms_hiaiaippparam_setinputformat) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, [HiAI\_ImageFormat](cannkit.md#hiai_imageformat) inputFormat) | 设置AippParam对象的输入图像格式。 |
| [HiAI\_ImageFormat](cannkit.md#hiai_imageformat) [HMS\_HiAIAippParam\_GetInputFormat](cannkit.md#hms_hiaiaippparam_getinputformat) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam) | 查询AippParam对象的输入图像格式。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetInputShape](cannkit.md#hms_hiaiaippparam_setinputshape) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, uint32\_t srcImageW, uint32\_t srcImageH) | 设置AippParam对象的输入图像宽高。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetInputShape](cannkit.md#hms_hiaiaippparam_getinputshape) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, uint32\_t \*srcImageW, uint32\_t \*srcImageH) | 查询AippParam对象的输入图像宽高。 |
| uint32\_t [HMS\_HiAIAippParam\_GetBatchCount](cannkit.md#hms_hiaiaippparam_getbatchcount) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam) | 查询AippParam对象的图像数量。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetCscConfig](cannkit.md#hms_hiaiaippparam_setcscconfig) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, [HiAI\_ImageFormat](cannkit.md#hiai_imageformat) inputFormat, [HiAI\_ImageFormat](cannkit.md#hiai_imageformat) outputFormat, [HiAI\_ImageColorSpace](cannkit.md#hiai_imagecolorspace) space) | 设置AippParam对象的CSC色域转换参数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetCscConfig](cannkit.md#hms_hiaiaippparam_getcscconfig) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, [HiAI\_ImageFormat](cannkit.md#hiai_imageformat) \*inputFormat, [HiAI\_ImageFormat](cannkit.md#hiai_imageformat) \*outputFormat, [HiAI\_ImageColorSpace](cannkit.md#hiai_imagecolorspace) \*space) | 查询AippParam对象的CSC色域转换相关参数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetChannelSwapConfig](cannkit.md#hms_hiaiaippparam_setchannelswapconfig) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, bool rbuvSwapSwitch, bool axSwapSwitch) | 设置AippParam对象的ChannelSwap通道交换参数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetChannelSwapConfig](cannkit.md#hms_hiaiaippparam_getchannelswapconfig) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, bool \*rbuvSwapSwitch, bool \*axSwapSwitch) | 查询AippParam对象的ChannelSwap通道交换参数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetSingleBatchMultiCrop](cannkit.md#hms_hiaiaippparam_setsinglebatchmulticrop) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, bool singleBatchMultiCrop) | 设置AippParam对象的SingleBatchMultiCrop标识。 |
| bool [HMS\_HiAIAippParam\_GetSingleBatchMultiCrop](cannkit.md#hms_hiaiaippparam_getsinglebatchmulticrop) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam) | 查询AippParam对象的SingleBatchMultiCrop标识。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetCropConfig](cannkit.md#hms_hiaiaippparam_setcropconfig) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t startPosW, uint32\_t startPosH, uint32\_t croppedW, uint32\_t croppedH) | 设置AippParam对象的裁剪参数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetCropConfig](cannkit.md#hms_hiaiaippparam_getcropconfig) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t \*startPosW, uint32\_t \*startPosH, uint32\_t \*croppedW, uint32\_t \*croppedH) | 查询AippParam对象的裁剪参数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetResizeConfig](cannkit.md#hms_hiaiaippparam_setresizeconfig) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t resizedW, uint32\_t resizedH) | 设置AippParam对象的图像缩放参数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetResizeConfig](cannkit.md#hms_hiaiaippparam_getresizeconfig) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t \*resizedW, uint32\_t \*resizedH) | 查询AippParam对象的图像缩放参数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetPadConfig](cannkit.md#hms_hiaiaippparam_setpadconfig) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t leftPadSize, uint32\_t rightPadSize, uint32\_t topPadSize, uint32\_t bottomPadSize) | 设置AippParam对象的输入图像的填充像素数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetPadConfig](cannkit.md#hms_hiaiaippparam_getpadconfig) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t \*leftPadSize, uint32\_t \*rightPadSize, uint32\_t \*topPadSize, uint32\_t \*bottomPadSize) | 查询AippParam对象的输入图像的填充像素数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetChannelPadding](cannkit.md#hms_hiaiaippparam_setchannelpadding) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t paddingValues[], uint32\_t channelCount) | 设置AippParam对象的通道padding填充值。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetChannelPadding](cannkit.md#hms_hiaiaippparam_getchannelpadding) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t paddingValues[], uint32\_t channelCount) | 查询AippParam对象的通道padding填充值。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetRotationAngle](cannkit.md#hms_hiaiaippparam_setrotationangle) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float rotationAngle) | 设置AippParam对象的旋转角度。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetRotationAngle](cannkit.md#hms_hiaiaippparam_getrotationangle) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float \*rotationAngle) | 查询AippParam对象的图像旋转角度。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetDtcMeanPixel](cannkit.md#hms_hiaiaippparam_setdtcmeanpixel) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t meanPixel[], uint32\_t channelCount) | 设置AippParam对象的数据类型转换通道像素平均值。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetDtcMeanPixel](cannkit.md#hms_hiaiaippparam_getdtcmeanpixel) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t meanPixel[], uint32\_t channelCount) | 查询AippParam对象的数据类型转换通道像素平均值。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetDtcMinPixel](cannkit.md#hms_hiaiaippparam_setdtcminpixel) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float minPixel[], uint32\_t channelCount) | 设置AippParam对象的数据类型转换通道像素最小值。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetDtcMinPixel](cannkit.md#hms_hiaiaippparam_getdtcminpixel) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float minPixel[], uint32\_t channelCount) | 查询AippParam对象的数据类型转换通道像素最小值。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetDtcVarReciPixel](cannkit.md#hms_hiaiaippparam_setdtcvarrecipixel) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float varReciPixel[], uint32\_t channelCount) | 设置AippParam对象的数据类型转换通道像素方差。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetDtcVarReciPixel](cannkit.md#hms_hiaiaippparam_getdtcvarrecipixel) ([HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float varReciPixel[], uint32\_t channelCount) | 查询AippParam对象的数据类型转换通道像素方差。 |
| const char \* [HMS\_HiAI\_GetVersion](cannkit.md#hms_hiai_getversion) (void) | 获取CANN Kit版本号，并通过返回模板hiaiversion A1A2A3.X1X2X3.Y1Y2Y3.Z1Z2Z3指定X1是否为0来区分是否支持NPU。若X1为0，则表示不支持NPU；若X1为非0，则表示支持NPU。 |
| [HiAI\_Compatibility](cannkit.md#hiai_compatibility) [HMS\_HiAICompatibility\_CheckFromFile](cannkit.md#hms_hiaicompatibility_checkfromfile) (const char \*file) | 查询编译后储存在文件中的模型的兼容性。 若发生不兼容情况，建议重新编译模型。 |
| [HiAI\_Compatibility](cannkit.md#hiai_compatibility) [HMS\_HiAICompatibility\_CheckFromBuffer](cannkit.md#hms_hiaicompatibility_checkfrombuffer) (const void \*data, size\_t size) | 查询编译后储存在内存中的模型的兼容性。 若发生不兼容情况，建议重新编译模型。 |
| OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetInputTensorShapes](cannkit.md#hms_hiaioptions_setinputtensorshapes) (OH\_NNCompilation \*compilation, NN\_TensorDesc \*inputTensorDescs[], size\_t shapeCount) | 编译时更新模型输入shape。 |
| size\_t [HMS\_HiAIOptions\_GetInputTensorShapeSize](cannkit.md#hms_hiaioptions_getinputtensorshapesize) (const OH\_NNCompilation \*compilation) | 查询选项参数中shape描述的个数。 |
| NN\_TensorDesc \* [HMS\_HiAIOptions\_GetInputTensorShape](cannkit.md#hms_hiaioptions_getinputtensorshape) (const OH\_NNCompilation \*compilation, size\_t index) | 查询选项参数中指定索引的shape描述。 |
| OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetFormatMode](cannkit.md#hms_hiaioptions_setformatmode) (OH\_NNCompilation \*compilation, [HiAI\_FormatMode](cannkit.md#hiai_formatmode) formatMode) | 设置模型编译时的数据排列格式。 |
| [HiAI\_FormatMode](cannkit.md#hiai_formatmode) [HMS\_HiAIOptions\_GetFormatMode](cannkit.md#hms_hiaioptions_getformatmode) (const OH\_NNCompilation \*compilation) | 查询模型编译参数中的数据排列格式。 |
| OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetDynamicShapeStatus](cannkit.md#hms_hiaioptions_setdynamicshapestatus) (OH\_NNCompilation \*compilation, [HiAI\_DynamicShapeStatus](cannkit.md#hiai_dynamicshapestatus) status) | 设置编译前可变shape配置中的EnableMode参数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetDynamicShapeMaxCache](cannkit.md#hms_hiaioptions_setdynamicshapemaxcache) (OH\_NNCompilation \*compilation, size\_t maxCacheCount) | 设置编译前可变shape配置中的最大缓存编译后模型数量。 |
| OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetDynamicShapeCacheMode](cannkit.md#hms_hiaioptions_setdynamicshapecachemode) (OH\_NNCompilation \*compilation, [HiAI\_DynamicShapeCacheMode](cannkit.md#hiai_dynamicshapecachemode) mode) | 设置编译前可变shape配置中的缓存模式参数。 |
| [HiAI\_DynamicShapeStatus](cannkit.md#hiai_dynamicshapestatus) [HMS\_HiAIOptions\_GetDynamicShapeStatus](cannkit.md#hms_hiaioptions_getdynamicshapestatus) (const OH\_NNCompilation \*compilation) | 查询编译前可变shape配置中的状态参数。 |
| size\_t [HMS\_HiAIOptions\_GetDynamicShapeMaxCache](cannkit.md#hms_hiaioptions_getdynamicshapemaxcache) (const OH\_NNCompilation \*compilation) | 查询编译前可变shape配置中的最大缓存数量。 |
| [HiAI\_DynamicShapeCacheMode](cannkit.md#hiai_dynamicshapecachemode) [HMS\_HiAIOptions\_GetDynamicShapeCacheMode](cannkit.md#hms_hiaioptions_getdynamicshapecachemode) (const OH\_NNCompilation \*compilation) | 查询编译前可变shape配置中的cacheMode参数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetOperatorDeviceOrder](cannkit.md#hms_hiaioptions_setoperatordeviceorder) (OH\_NNCompilation \*compilation, const char \*operatorName, [HiAI\_ExecuteDevice](cannkit.md#hiai_executedevice) \*executeDevices, size\_t deviceCount) | 设置算子级调优配置中算子执行设备列表。 |
| size\_t [HMS\_HiAIOptions\_GetOperatorDeviceCount](cannkit.md#hms_hiaioptions_getoperatordevicecount) (const OH\_NNCompilation \*compilation, const char \*operatorName) | 查询算子级调优配置中指定算子的执行设备个数。 |
| [HiAI\_ExecuteDevice](cannkit.md#hiai_executedevice) \* [HMS\_HiAIOptions\_GetOperatorDeviceOrder](cannkit.md#hms_hiaioptions_getoperatordeviceorder) (const OH\_NNCompilation \*compilation, const char \*operatorName) | 查询算子级调优配置中指定算子的执行设备列表。 |
| OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetModelDeviceOrder](cannkit.md#hms_hiaioptions_setmodeldeviceorder) (OH\_NNCompilation \*compilation, [HiAI\_ExecuteDevice](cannkit.md#hiai_executedevice) \*executeDevices, size\_t deviceCount) | 设置模型级调优配置中模型执行设备列表。 |
| size\_t [HMS\_HiAIOptions\_GetModelDeviceCount](cannkit.md#hms_hiaioptions_getmodeldevicecount) (const OH\_NNCompilation \*compilation) | 查询模型级调优配置中模型的执行设备个数。 |
| [HiAI\_ExecuteDevice](cannkit.md#hiai_executedevice) \* [HMS\_HiAIOptions\_GetModelDeviceOrder](cannkit.md#hms_hiaioptions_getmodeldeviceorder) (const OH\_NNCompilation \*compilation) | 查询模型级调优配置中模型的执行设备列表。 |
| OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetFallbackMode](cannkit.md#hms_hiaioptions_setfallbackmode) (OH\_NNCompilation \*compilation, [HiAI\_FallbackMode](cannkit.md#hiai_fallbackmode) fallbackMode) | 设置调优配置中的回滚模式。 |
| [HiAI\_FallbackMode](cannkit.md#hiai_fallbackmode) [HMS\_HiAIOptions\_GetFallbackMode](cannkit.md#hms_hiaioptions_getfallbackmode) (const OH\_NNCompilation \*compilation) | 查询调优配置中的回滚模式。 |
| OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetDeviceMemoryReusePlan](cannkit.md#hms_hiaioptions_setdevicememoryreuseplan) (OH\_NNCompilation \*compilation, [HiAI\_DeviceMemoryReusePlan](cannkit.md#hiai_devicememoryreuseplan) deviceMemoryReusePlan) | 设置调优配置中的设备内存复用参数。 |
| [HiAI\_DeviceMemoryReusePlan](cannkit.md#hiai_devicememoryreuseplan) [HMS\_HiAIOptions\_GetDeviceMemoryReusePlan](cannkit.md#hms_hiaioptions_getdevicememoryreuseplan) (const OH\_NNCompilation \*compilation) | 查询调优配置中的设备内存复用参数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetTuningStrategy](cannkit.md#hms_hiaioptions_settuningstrategy) (OH\_NNCompilation \*compilation, [HiAI\_TuningStrategy](cannkit.md#hiai_tuningstrategy) tuningStrategy) | 设置模型编译时的模型优化策略。 |
| [HiAI\_TuningStrategy](cannkit.md#hiai_tuningstrategy) [HMS\_HiAIOptions\_GetTuningStrategy](cannkit.md#hms_hiaioptions_gettuningstrategy) (const OH\_NNCompilation \*compilation) | 查询模型优化策略。 |
| OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetQuantConfig](cannkit.md#hms_hiaioptions_setquantconfig) (OH\_NNCompilation \*compilation, void \*data, size\_t size) | 设置模型编译时量化配置。 |
| void \* [HMS\_HiAIOptions\_GetQuantConfigData](cannkit.md#hms_hiaioptions_getquantconfigdata) (const OH\_NNCompilation \*compilation) | 查询量化配置的数据地址。 |
| size\_t [HMS\_HiAIOptions\_GetQuantConfigSize](cannkit.md#hms_hiaioptions_getquantconfigsize) (const OH\_NNCompilation \*compilation) | 查询量化配置的数据大小。 |
| OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetTuningMode](cannkit.md#hms_hiaioptions_settuningmode) (OH\_NNCompilation \*compilation, [HiAI\_TuningMode](cannkit.md#hiai_tuningmode) tuningMode) | 选择辅助调优模式。 |
| OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetTuningCacheDir](cannkit.md#hms_hiaioptions_settuningcachedir) (OH\_NNCompilation \*compilation, const char \*cacheDir) | 设置辅助调优的缓存目录。 |
| [HiAI\_TuningMode](cannkit.md#hiai_tuningmode) [HMS\_HiAIOptions\_GetTuningMode](cannkit.md#hms_hiaioptions_gettuningmode) (const OH\_NNCompilation \*compilation) | 查询辅助调优模式。 |
| const char \* [HMS\_HiAIOptions\_GetTuningCacheDir](cannkit.md#hms_hiaioptions_gettuningcachedir) (const OH\_NNCompilation \*compilation) | 查询辅助调优的缓存目录。 |
| OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetBandMode](cannkit.md#hms_hiaioptions_setbandmode) (OH\_NNCompilation \*compilation, [HiAI\_BandMode](cannkit.md#hiai_bandmode) bandMode) | 设置NPU与周边硬件IO资源的带宽模式。 |
| [HiAI\_BandMode](cannkit.md#hiai_bandmode) [HMS\_HiAIOptions\_GetBandMode](cannkit.md#hms_hiaioptions_getbandmode) (const OH\_NNCompilation \*compilation) | 查询带宽模式。 |
| OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetOmOptions](cannkit.md#hms_hiaioptions_setomoptions) (OH\_NNCompilation \*compilation, [HiAI\_OmType](cannkit.md#hiai_omtype) type, const char \*outputDir) | 设置模型加载时的维测选项信息。 |
| [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \* [HMS\_HiAISingleOpTensorDesc\_Create](cannkit.md#hms_hiaisingleoptensordesc_create) (const int64\_t \*dims, size\_t dimNum, [HiAI\_SingleOpDataType](cannkit.md#hiai_singleopdatatype) dataType, [HiAI\_SingleOpFormat](cannkit.md#hiai_singleopformat) format, bool isVirtual) | 创建[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象。 |
| size\_t [HMS\_HiAISingleOpTensorDesc\_GetDimensionCount](cannkit.md#hms_hiaisingleoptensordesc_getdimensioncount) (const [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \*tensorDesc) | 查询[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)的维度数量。 |
| int64\_t [HMS\_HiAISingleOpTensorDesc\_GetDimension](cannkit.md#hms_hiaisingleoptensordesc_getdimension) (const [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \*tensorDesc, size\_t index) | 查询[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)指定索引的维度长度。 |
| [HiAI\_SingleOpDataType](cannkit.md#hiai_singleopdatatype) [HMS\_HiAISingleOpTensorDesc\_GetDataType](cannkit.md#hms_hiaisingleoptensordesc_getdatatype) (const [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \*tensorDesc) | 查询[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)的数据类型。 |
| [HiAI\_SingleOpFormat](cannkit.md#hiai_singleopformat) [HMS\_HiAISingleOpTensorDesc\_GetFormat](cannkit.md#hms_hiaisingleoptensordesc_getformat) (const [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \*tensorDesc) | 查询[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)的排布格式。 |
| bool [HMS\_HiAISingleOpTensorDesc\_IsVirtual](cannkit.md#hms_hiaisingleoptensordesc_isvirtual) (const [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \*tensorDesc) | 查询[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)是否为虚拟张量。 |
| size\_t [HMS\_HiAISingleOpTensorDesc\_GetByteSize](cannkit.md#hms_hiaisingleoptensordesc_getbytesize) (const [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \*tensorDesc) | 查询基于[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)的维度和数据类型计算的数据占用字节数。 |
| void [HMS\_HiAISingleOpTensorDesc\_Destroy](cannkit.md#hms_hiaisingleoptensordesc_destroy) ([HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \*\*tensorDesc) | 释放[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象。 |
| [HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer) \* [HMS\_HiAISingleOpBuffer\_Create](cannkit.md#hms_hiaisingleopbuffer_create) (size\_t dataSize) | 按照指定的内存大小创建[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)对象。 |
| size\_t [HMS\_HiAISingleOpBuffer\_GetSize](cannkit.md#hms_hiaisingleopbuffer_getsize) (const [HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer) \*buffer) | 查询[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)的字节大小。 |
| void \* [HMS\_HiAISingleOpBuffer\_GetData](cannkit.md#hms_hiaisingleopbuffer_getdata) (const [HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer) \*buffer) | 查询[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)的内存地址。 |
| OH\_NN\_ReturnCode [HMS\_HiAISingleOpBuffer\_Destroy](cannkit.md#hms_hiaisingleopbuffer_destroy) ([HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer) \*\*buffer) | 释放[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)对象。 |
| [HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) \* [HMS\_HiAISingleOpTensor\_CreateFromTensorDesc](cannkit.md#hms_hiaisingleoptensor_createfromtensordesc) (const [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \*desc) | 根据[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)创建[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象。 |
| [HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) \* [HMS\_HiAISingleOpTensor\_CreateFromSingleOpBuffer](cannkit.md#hms_hiaisingleoptensor_createfromsingleopbuffer) (const [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \*desc, void \*data, size\_t dataSize) | 根据[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)、[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)的内存地址和数据大小创建[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象。 |
| [HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) \* [HMS\_HiAISingleOpTensor\_CreateFromConst](cannkit.md#hms_hiaisingleoptensor_createfromconst) (const [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \*desc, void \*data, size\_t dataSize) | 根据[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)、常量数据（如卷积权重、偏置等）的内存地址和数据大小创建[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象。 |
| [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \* [HMS\_HiAISingleOpTensor\_GetTensorDesc](cannkit.md#hms_hiaisingleoptensor_gettensordesc) (const [HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) \*tensor) | 获取[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)的Tensor描述。 |
| [HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer) \* [HMS\_HiAISingleOpTensor\_GetBuffer](cannkit.md#hms_hiaisingleoptensor_getbuffer) (const [HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) \*tensor) | 获取[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)的Buffer。 |
| OH\_NN\_ReturnCode [HMS\_HiAISingleOpTensor\_Destroy](cannkit.md#hms_hiaisingleoptensor_destroy) ([HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) \*\*tensor) | 释放[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象。 |
| [HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions) \* [HMS\_HiAISingleOpOptions\_Create](cannkit.md#hms_hiaisingleopoptions_create) (void) | 创建[HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions)对象。 |
| void [HMS\_HiAISingleOpOptions\_Destroy](cannkit.md#hms_hiaisingleopoptions_destroy) ([HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions) \*\*options) | 释放[HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions)对象。 |
| [HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor) \* [HMS\_HiAISingleOpDescriptor\_CreateConvolution](cannkit.md#hms_hiaisingleopdescriptor_createconvolution) ([HiAISingleOpDescriptor\_ConvolutionParam](cannkit-sopdesc-convparam.md) param) | 创建卷积类（普通卷积、转置卷积、深度卷积）的描述符对象。 |
| [HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor) \* [HMS\_HiAISingleOpDescriptor\_CreateActivation](cannkit.md#hms_hiaisingleopdescriptor_createactivation) ([HiAI\_SingleOpActivationType](cannkit.md#hiai_singleopactivationtype) activationType, float coef) | 创建激活函数类的描述符对象。 |
| void [HMS\_HiAISingleOpDescriptor\_Destroy](cannkit.md#hms_hiaisingleopdescriptor_destroy) ([HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor) \*\*opDesc) | 释放[HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor)对象。 |
| [HiAI\_SingleOpSupportStatus](cannkit.md#hiai_singleopsupportstatus) [HMS\_HiAISingleOpExecutor\_PreCheckConvolution](cannkit.md#hms_hiaisingleopexecutor_precheckconvolution) ([HiAI\_SingleOpExecutorConvolutionParam](cannkit-sopexec-convparam.md) param) | 预查询卷积算子的支持状态。 |
| [HiAI\_SingleOpSupportStatus](cannkit.md#hiai_singleopsupportstatus) [HMS\_HiAISingleOpExecutor\_PreCheckFusedConvolutionActivation](cannkit.md#hms_hiaisingleopexecutor_precheckfusedconvolutionactivation) ([HiAI\_SingleOpExecutorFusedConvolutionActivationParam](cannkit-sopexec-fusedconv-actparam.md) param) | 预查询卷积和激活融合算子的支持状态。 |
| [HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor) \* [HMS\_HiAISingleOpExecutor\_CreateConvolution](cannkit.md#hms_hiaisingleopexecutor_createconvolution) ([HiAI\_SingleOpExecutorConvolutionParam](cannkit-sopexec-convparam.md) param) | 创建卷积类算子对应的[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)对象。 |
| [HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor) \* [HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation](cannkit.md#hms_hiaisingleopexecutor_createfusedconvolutionactivation) ([HiAI\_SingleOpExecutorFusedConvolutionActivationParam](cannkit-sopexec-fusedconv-actparam.md) param) | 创建卷积和激活融合算子对应的[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)对象。 |
| OH\_NN\_ReturnCode [HMS\_HiAISingleOpExecutor\_UpdateOutputTensorDesc](cannkit.md#hms_hiaisingleopexecutor_updateoutputtensordesc) (const [HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor) \*executor, uint32\_t index, [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \*output) | 更新[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)的输出tensor描述。 |
| size\_t [HMS\_HiAISingleOpExecutor\_GetWorkspaceSize](cannkit.md#hms_hiaisingleopexecutor_getworkspacesize) (const [HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor) \*executor) | 查询[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)所需的ION内存工作空间的字节大小。 |
| OH\_NN\_ReturnCode [HMS\_HiAISingleOpExecutor\_Init](cannkit.md#hms_hiaisingleopexecutor_init) ([HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor) \*executor, void \*workspace, size\_t workspaceSize) | 加载[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)。 |
| OH\_NN\_ReturnCode [HMS\_HiAISingleOpExecutor\_Execute](cannkit.md#hms_hiaisingleopexecutor_execute) ([HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor) \*executor, [HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) \*input[], int32\_t inputNum, [HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) \*output[], int32\_t outputNum) | 执行同步运算推理。 |
| OH\_NN\_ReturnCode [HMS\_HiAISingleOpExecutor\_Destroy](cannkit.md#hms_hiaisingleopexecutor_destroy) ([HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor) \*\*executor) | 销毁[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)对象，释放执行器占用的内存。 |
| size\_t [HMS\_HiAITensor\_GetSizeWithImageFormat](cannkit.md#hms_hiaitensor_getsizewithimageformat) (NN\_TensorDesc \*desc, [HiAI\_ImageFormat](cannkit.md#hiai_imageformat) format) | 根据NN\_TensorDesc和HiAI\_ImageFormat计算申请tensor的大小。 |
| OH\_NN\_ReturnCode [HMS\_HiAITensor\_SetAippParams](cannkit.md#hms_hiaitensor_setaippparams) (NN\_Tensor \*tensor, [HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParams[], size\_t aippNum) | 给NN\_Tensor设置AippParams。 |

## 类型定义说明

PhonePC/2in1TabletTV

### HiAI\_AippParam

PhonePC/2in1TabletTV

```
1. typedef struct HiAI_AippParam HiAI_AippParam
```

**描述**

AIPP参数对象。

**起始版本：** 4.1.0(11)

### HiAI\_SingleOpBuffer

PhonePC/2in1TabletTV

```
1. typedef struct HiAI_SingleOpBuffer HiAI_SingleOpBuffer
```

**描述**

单算子Buffer句柄。

**起始版本：** 5.0.0(12)

### HiAI\_SingleOpDescriptor

PhonePC/2in1TabletTV

```
1. typedef struct HiAI_SingleOpDescriptor HiAI_SingleOpDescriptor
```

**描述**

单算子的算子描述句柄。

**起始版本：** 5.0.0(12)

### HiAISingleOpDescriptor\_ConvolutionParam

PhonePC/2in1TabletTV

```
1. typedef struct HiAISingleOpDescriptor_ConvolutionParam
```

**描述**

[HMS\_HiAISingleOpDescriptor\_CreateConvolution](cannkit.md#hms_hiaisingleopdescriptor_createconvolution)输入参数。

**起始版本：** 5.0.0(12)

### HiAI\_SingleOpExecutor

PhonePC/2in1TabletTV

```
1. typedef struct HiAI_SingleOpExecutor HiAI_SingleOpExecutor
```

**描述**

单算子执行器句柄。

**起始版本：** 5.0.0(12)

### HiAI\_SingleOpExecutorConvolutionParam

PhonePC/2in1TabletTV

```
1. typedef struct HiAI_SingleOpExecutorConvolutionParam
```

**描述**

[HMS\_HiAISingleOpExecutor\_CreateConvolution](cannkit.md#hms_hiaisingleopexecutor_createconvolution)输入参数。

**起始版本：** 5.0.0(12)

### HiAI\_SingleOpExecutorFusedConvolutionActivationParam

PhonePC/2in1TabletTV

```
1. typedef struct HiAI_SingleOpExecutorFusedConvolutionActivationParam
```

**描述**

[HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation](cannkit.md#hms_hiaisingleopexecutor_createfusedconvolutionactivation)输入参数。

**起始版本：** 5.0.0(12)

### HiAI\_SingleOpOptions

PhonePC/2in1TabletTV

```
1. typedef struct HiAI_SingleOpOptions HiAI_SingleOpOptions
```

**描述**

单算子选项句柄。

**起始版本：** 5.0.0(12)

### HiAI\_SingleOpTensor

PhonePC/2in1TabletTV

```
1. typedef struct HiAI_SingleOpTensor HiAI_SingleOpTensor
```

**描述**

单算子Tensor句柄。

**起始版本：** 5.0.0(12)

### HiAI\_SingleOpTensorDesc

PhonePC/2in1TabletTV

```
1. typedef struct HiAI_SingleOpTensorDesc HiAI_SingleOpTensorDesc
```

**描述**

单算子Tensor描述的句柄。

**起始版本：** 5.0.0(12)

## 枚举类型说明

PhonePC/2in1TabletTV

### HiAI\_BandMode

PhonePC/2in1TabletTV

```
1. enum HiAI_BandMode
```

**描述**

定义硬件之间带宽模式。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI\_BANDMODE\_UNSET | 不设置，由系统调节。 |
| HIAI\_BANDMODE\_LOW | 低级带宽模式。 |
| HIAI\_BANDMODE\_NORMAL | 中级带宽模式。 |
| HIAI\_BANDMODE\_HIGH | 高级带宽模式。 |

### HiAI\_Compatibility

PhonePC/2in1TabletTV

```
1. enum HiAI_Compatibility
```

**描述**

编译后模型兼容性结果。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI\_COMPATIBILITY\_COMPATIBLE | 模型兼容。 |
| HIAI\_COMPATIBILITY\_INCOMPATIBLE | 模型不兼容。 |

### HiAI\_DeviceMemoryReusePlan

PhonePC/2in1TabletTV

```
1. enum HiAI_DeviceMemoryReusePlan
```

**描述**

设备内存复用配置选项。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI\_DEVICE\_MEMORY\_REUSE\_PLAN\_UNSET | 不使用，默认值。 |
| HIAI\_DEVICE\_MEMORY\_REUSE\_PLAN\_LOW | 低内存复用率，模型申请的内存较多但模型推理性能相对较优。 |
| HIAI\_DEVICE\_MEMORY\_REUSE\_PLAN\_HIGH | 高内存复用率，模型申请的内存较少但模型推理性能相对较差。 |

### HiAI\_DynamicShapeCacheMode

PhonePC/2in1TabletTV

```
1. enum HiAI_DynamicShapeCacheMode
```

**描述**

编译前可变shape支持的模式。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI\_DYNAMIC\_SHAPE\_CACHE\_BUILT\_MODEL | 缓存编译后的模型，内存占用较小，默认值。 |
| HIAI\_DYNAMIC\_SHAPE\_CACHE\_LOADED\_MODEL | 缓存加载后的模型，性能较优。 |

### HiAI\_DynamicShapeStatus

PhonePC/2in1TabletTV

```
1. enum HiAI_DynamicShapeStatus
```

**描述**

是否使能编译前可变shape。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI\_DYNAMIC\_SHAPE\_DISABLED | 不使能编译前可变shape，默认值。 |
| HIAI\_DYNAMIC\_SHAPE\_ENABLED | 使能编译前可变shape。 |

### HiAI\_ExecuteDevice

PhonePC/2in1TabletTV

```
1. enum HiAI_ExecuteDevice
```

**描述**

模型运行时支持的设备类型。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI\_EXECUTE\_DEVICE\_NPU | NPU，默认值。 |
| HIAI\_EXECUTE\_DEVICE\_CPU | CPU。 |
| HIAI\_EXECUTE\_DEVICE\_GPU | GPU。 |

### HiAI\_FallbackMode

PhonePC/2in1TabletTV

```
1. enum HiAI_FallbackMode
```

**描述**

指定的硬件设备无法编译模型时，是否允许CANN Kit选择其他硬件设备，例如CPU。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI\_FALLBACK\_ENABLED | 允许，默认值。 |
| HIAI\_FALLBACK\_DISABLED | 不允许。 |

### HiAI\_FormatMode

PhonePC/2in1TabletTV

```
1. enum HiAI_FormatMode
```

**描述**

模型编译时数据的排列格式。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI\_FORMAT\_MODE\_NCHW | 格式为NCHW，默认值。 |
| HIAI\_FORMAT\_MODE\_ORIGIN | 格式为原始模型格式。 |

### HiAI\_ImageColorSpace

PhonePC/2in1TabletTV

```
1. enum HiAI_ImageColorSpace
```

**描述**

图像色域空间类型。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI\_JPEG | JPEG色域空间类型。 |
| HIAI\_BT\_601\_NARROW | BT.601 video range色域空间类型。 |
| HIAI\_BT\_601\_FULL | BT.601 full range色域空间类型。 |
| HIAI\_BT\_709\_NARROW | BT.709 video range色域空间类型。 |
| HIAI\_IMAGE\_COLOR\_SPACE\_INVALID | 无效图像色域类型。 |

### HiAI\_ImageFormat

PhonePC/2in1TabletTV

```
1. enum HiAI_ImageFormat
```

**描述**

CANN Kit推理支持的输入和输出Tensor的图片格式的枚举。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI\_YUV420SP\_U8 | YUV420SP\_U8格式的图片。 |
| HIAI\_XRGB8888\_U8 | XRGB8888\_U8格式的图片。 |
| HIAI\_YUV400\_U8 | YUV400\_U8格式的图片。 |
| HIAI\_ARGB8888\_U8 | ARGB8888\_U8格式的图片。 |
| HIAI\_YUYV\_U8 | YUYV\_U8格式的图片。 |
| HIAI\_YUV422SP\_U8 | YUV422SP\_U8格式的图片。 |
| HIAI\_AYUV444\_U8 | AYUV444\_U8格式的图片。 |
| HIAI\_RGB888\_U8 | RGB888\_U8格式的图片。 |
| HIAI\_BGR888\_U8 | BGR888\_U8格式的图片。 |
| HIAI\_YUV444SP\_U8 | YUV444SP格式的图片。 |
| HIAI\_YVU444SP\_U8 | YVU444SP格式的图片。 |
| HIAI\_IMAGE\_FORMAT\_INVALID | 不支持的图片格式。 |

### HiAI\_OmType

PhonePC/2in1TabletTV

```
1. enum HiAI_OmType
```

**描述**

维测类型定义。

**起始版本：** 5.1.0(18)

| 枚举值 | 描述 |
| --- | --- |
| HIAI\_OM\_TYPE\_OFF | 关闭维测。 |
| HIAI\_OM\_TYPE\_PROFILING | Profiling维测类型。 |
| HIAI\_OM\_TYPE\_DUMP | Dump维测类型。  **起始版本**：6.0.0(20) |

### HiAI\_SingleOpActivationType

PhonePC/2in1TabletTV

```
1. enum HiAI_SingleOpActivationType
```

**描述**

单算子激活模式枚举。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| HIAI\_SINGLEOP\_ACTIVATION\_TYPE\_RELU | ReLU激活函数。 |
| HIAI\_SINGLEOP\_ACTIVATION\_TYPE\_RELU6 | ReLU6激活函数。 |

### HiAI\_SingleOpConvMode

PhonePC/2in1TabletTV

```
1. enum HiAI_SingleOpConvMode
```

**描述**

单算子卷积模式枚举。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| HIAI\_SINGLEOP\_CONV\_MODE\_COMMON | 普通卷积。 |
| HIAI\_SINGLEOP\_CONV\_MODE\_TRANSPOSED | 转置卷积。 |
| HIAI\_SINGLEOP\_CONV\_MODE\_DEPTHWISE | 深度卷积。 |

### HiAI\_SingleOpDataType

PhonePC/2in1TabletTV

```
1. enum HiAI_SingleOpDataType
```

**描述**

单算子张量数据类型枚举。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| HIAI\_SINGLEOP\_DT\_FLOAT | 张量数据类型为float。 |
| HIAI\_SINGLEOP\_DT\_FLOAT16 | 张量数据类型为float16。 |
| HIAI\_SINGLEOP\_DT\_UNDEFINED | 张量数据类型未定义。 |

### HiAI\_SingleOpFormat

PhonePC/2in1TabletTV

```
1. enum HiAI_SingleOpFormat
```

**描述**

单算子张量排布格式枚举。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| HIAI\_SINGLEOP\_FORMAT\_NCHW | 张量按照NCHW格式排布。 |
| HIAI\_SINGLEOP\_FORMAT\_NHWC | 张量按照NHWC格式排布。 |
| HIAI\_SINGLEOP\_FORMAT\_ND | 张量按照ND格式排布。暂不支持用户使用ND格式排布的单算子Tensor。 |
| HIAI\_SINGLEOP\_FORMAT\_NC1HWC0 | 张量按照NC1HWC0格式排布。 |
| HIAI\_SINGLEOP\_FORMAT\_NC4HW4 | 张量按照NC4HW4格式排布。 |
| HIAI\_SINGLEOP\_FORMAT\_NC8HW8 | 张量按照NC8HW8格式排布。 |
| HIAI\_SINGLEOP\_FORMAT\_RESERVED | 张量排布格式未定义。 |

### HiAI\_SingleOpPadMode

PhonePC/2in1TabletTV

```
1. enum HiAI_SingleOpPadMode
```

**描述**

单算子填充模式枚举。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| HIAI\_SINGLEOP\_PAD\_MODE\_SPECIFIC | 如果填充算法未设置，将根据参数**pads**采用显示填充。 |
| HIAI\_SINGLEOP\_PAD\_MODE\_SAME | 对输入进行填充使输出维度与输入维度相同。输出维度由ceil(输入维度 / 步长)确定。 |
| HIAI\_SINGLEOP\_PAD\_MODE\_SAME\_UPPER | 使用SAME\_UPPER填充模式，当填充长度为奇数时，起始的填充长度小于等于末尾的填充长度。 |
| HIAI\_SINGLEOP\_PAD\_MODE\_SAME\_LOWER | 使用SAME\_LOWER填充模式，当填充长度为奇数时，起始的填充长度大于等于末尾的填充长度。 |
| HIAI\_SINGLEOP\_PAD\_MODE\_VALID | 不填充，输出维度由ceil((输入维度 - 滤波器维度 + 1) / 步长)确定。 |

### HiAI\_SingleOpSupportStatus

PhonePC/2in1TabletTV

```
1. enum HiAI_SingleOpSupportStatus
```

**描述**

单算子支持状态枚举。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| HIAI\_SINGLEOP\_OPTIMIZED | 使用单算子性能已优化。推荐用户使用单算子执行器，执行单算子推理计算。 |
| HIAI\_SINGLEOP\_COMMON | 使用单算子性能普通。支持该算子，但使用单算子可能性能收益小。 |
| HIAI\_SINGLEOP\_UNSUPPORTED | 不支持该单算子。若创建该单算子执行器将会失败。 |

### HiAI\_TuningMode

PhonePC/2in1TabletTV

```
1. enum HiAI_TuningMode
```

**描述**

辅助调优模式。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI\_TUNING\_MODE\_UNSET | 关闭调优模式。 |
| HIAI\_TUNING\_MODE\_AUTO | 自动调优模式，推荐选择的模式，内部算法控制调优。 |
| HIAI\_TUNING\_MODE\_HETER | 异构调优模式。 |

### HiAI\_TuningStrategy

PhonePC/2in1TabletTV

```
1. enum HiAI_TuningStrategy
```

**描述**

模型优化策略配置选项。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI\_TUNING\_STRATEGY\_OFF | 不支持深度融合场景，也不支持编译前可变shape，默认值。 |
| HIAI\_TUNING\_STRATEGY\_ON\_DEVICE\_TUNING | 支持编译前可变shape场景深度融合优化模型。 |
| HIAI\_TUNING\_STRATEGY\_ON\_DEVICE\_PREPROCESS\_TUNING | NPU算子库动态升级场景深度融合优化模型。 |
| HIAI\_TUNING\_STRATEGY\_ON\_CLOUD\_TUNING | 未来场景的预留，目前不使用。 |

## 函数说明

PhonePC/2in1TabletTV

### HMS\_HiAI\_GetVersion()

PhonePC/2in1TabletTV

```
1. const char* HMS_HiAI_GetVersion (void)
```

**描述**

获取CANN Kit版本号，并通过返回模板hiaiversion A1A2A3.X1X2X3.Y1Y2Y3.Z1Z2Z3指定X1是否为0来区分是否支持NPU。若X1为0，则表示不支持NPU；若X1为非0，则表示支持NPU。

**起始版本：** 4.1.0(11)

**返回：**

成功返回CANN Kit版本号，失败返回空指针。

### HMS\_HiAIAippParam\_Create()

PhonePC/2in1TabletTV

```
1. HiAI_AippParam* HMS_HiAIAippParam_Create (uint32_t batchNum)
```

**描述**

根据batchNum创建动态AippParam对象。

本方法用于创建动态AippParam对象，根据传入的batchNum申请相应的内存，用于存储动态AIPP参数。 不需要[HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例时，需要调用[HMS\_HiAIAippParam\_Destroy](cannkit.md#hms_hiaiaippparam_destroy)进行释放，否则会出现内存泄漏。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| batchNum | 模型输入的batch大小，取值范围为(0, 127]。 |

**返回：**

成功时返回[HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，失败返回空指针。

### HMS\_HiAIAippParam\_Destroy()

PhonePC/2in1TabletTV

```
1. void HMS_HiAIAippParam_Destroy (HiAI_AippParam ** aippParam)
```

**描述**

释放AippParam对象。

本方法用于释放通过[HMS\_HiAIAippParam\_Create](cannkit.md#hms_hiaiaippparam_create)创建的[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空。 |

### HMS\_HiAIAippParam\_GetBatchCount()

PhonePC/2in1TabletTV

```
1. uint32_t HMS_HiAIAippParam_GetBatchCount (HiAI_AippParam * aippParam)
```

**描述**

查询AippParam对象的图像数量。

本方法用于动态AIPP推理时，根据[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象查询推理AippParam设置图像数量。 在单batch多crop场景为一张图像多个crop的子图像的数量。在多batch单crop场景为输入的batch值。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空。 |

**返回：**

成功返回图像数量，失败返回0。

### HMS\_HiAIAippParam\_GetChannelPadding()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_GetChannelPadding (HiAI_AippParam * aippParam, uint32_t batchIndex, uint32_t paddingValues[], uint32_t channelCount)
```

**描述**

查询AippParam对象的通道padding填充值。

本方法用于动态AIPP推理时，根据[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象查询对应索引的通道padding的填充值。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| paddingValues[] | 通道填充值数组，填充值范围[-65504, 65504]，默认填充值为0。 |
| channelCount | 通道填充数，当前支持[1, 4]，例如channelCount=3则对应查询通道chn0, chn1, chn2的数据。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_GetChannelSwapConfig()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_GetChannelSwapConfig (HiAI_AippParam * aippParam, bool * rbuvSwapSwitch, bool * axSwapSwitch)
```

**描述**

查询AippParam对象的ChannelSwap通道交换参数。

本方法用于动态AIPP推理时，根据[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象查询通道交换参数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| rbuvSwapSwitch | 返回真为RB/UV通道交换已使能，返回假为RB/UV通道交换未使能。 |
| axSwapSwitch | 返回真为AX通道交换已使能，返回假为AX通道交换未使能。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_GetCropConfig()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_GetCropConfig (HiAI_AippParam * aippParam, uint32_t batchIndex, uint32_t * startPosW, uint32_t * startPosH, uint32_t * croppedW, uint32_t * croppedH)
```

**描述**

查询AippParam对象的裁剪参数。

本方法用于动态AIPP推理时，根据[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象查询对应索引的裁剪参数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应即将crop出来的图像索引。 |
| startPosW | 裁剪起始位置水平方向坐标。 |
| startPosH | 裁剪起始位置垂直方向坐标。 |
| croppedW | 裁剪出的图像宽度，单位为像素。 |
| croppedH | 裁剪出的图像高度，单位为像素。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_GetCscConfig()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_GetCscConfig (HiAI_AippParam * aippParam, HiAI_ImageFormat * inputFormat, HiAI_ImageFormat * outputFormat, HiAI_ImageColorSpace * space)
```

**描述**

查询AippParam对象的CSC色域转换相关参数。

本方法用于动态AIPP推理时，根据[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象查询推理AippParam色域转换参数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| inputFormat | 图像输入格式，可参考[HiAI\_ImageFormat](cannkit.md#hiai_imageformat)。 |
| outputFormat | 图像输出格式，可参考[HiAI\_ImageFormat](cannkit.md#hiai_imageformat)。 |
| space | 图像颜色空间类型，可参考[HiAI\_ImageColorSpace](cannkit.md#hiai_imagecolorspace)。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_GetData()

PhonePC/2in1TabletTV

```
1. void* HMS_HiAIAippParam_GetData (HiAI_AippParam * aippParam)
```

**描述**

获取AippParam申请的内存地址。

本方法用于获取通过[HMS\_HiAIAippParam\_Create](cannkit.md#hms_hiaiaippparam_create)申请的[HiAI\_AippParam](cannkit.md#hiai_aippparam)的data内存地址。 data指向申请的AIPP参数的内存。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返空指针。 |

**返回：**

成功时返回AippParam申请的内存地址，失败返回空指针。

### HMS\_HiAIAippParam\_GetDataSize()

PhonePC/2in1TabletTV

```
1. uint32_t HMS_HiAIAippParam_GetDataSize (HiAI_AippParam * aippParam)
```

**描述**

获取AippParam申请的内存大小。

本方法用于获取通过[HMS\_HiAIAippParam\_Create](cannkit.md#hms_hiaiaippparam_create)申请的[HiAI\_AippParam](cannkit.md#hiai_aippparam)的size大小。 size为申请的AIPP参数的内存大小。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回0。 |

**返回：**

成功时返回AippParam申请的内存大小，失败返回0。

### HMS\_HiAIAippParam\_GetDtcMeanPixel()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_GetDtcMeanPixel (HiAI_AippParam * aippParam, uint32_t batchIndex, uint32_t meanPixel[], uint32_t channelCount)
```

**描述**

查询AippParam对象的数据类型转换通道像素平均值。

该方法用于动态AIPP推理时，根据[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象查询对应索引的数据类型转换像素平均值。 该方法需配合[HMS\_HiAIAippParam\_GetDtcMinPixel](cannkit.md#hms_hiaiaippparam_getdtcminpixel)、[HMS\_HiAIAippParam\_GetDtcVarReciPixel](cannkit.md#hms_hiaiaippparam_getdtcvarrecipixel)共同使用，来获取所有数据类型转换参数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| meanPixel[] | 通道像素平均值数组，数组size为channelCount。 |
| channelCount | 通道数量，取值范围为[1, 4]，对应从chn0开始。例如channelCount等于3则对应查询通道chn0, chn1, chn2的数据。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_GetDtcMinPixel()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_GetDtcMinPixel (HiAI_AippParam * aippParam, uint32_t batchIndex, float minPixel[], uint32_t channelCount)
```

**描述**

查询AippParam对象的数据类型转换通道像素最小值。

该方法用于动态AIPP推理时，根据[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象查询对应索引的数据类型转换像素最小值。 该方法需配合[HMS\_HiAIAippParam\_GetDtcMeanPixel](cannkit.md#hms_hiaiaippparam_getdtcmeanpixel)、[HMS\_HiAIAippParam\_GetDtcVarReciPixel](cannkit.md#hms_hiaiaippparam_getdtcvarrecipixel)共同使用，来获取所有数据类型转换参数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| minPixel[] | 通道像素最小值数组，数组size为channelCount。 |
| channelCount | 通道数量，取值范围为[1, 4]，对应从chn0开始。例如channelCount等于3则对应查询通道chn0, chn1, chn2的数据。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_GetDtcVarReciPixel()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_GetDtcVarReciPixel (HiAI_AippParam * aippParam, uint32_t batchIndex, float varReciPixel[], uint32_t channelCount)
```

**描述**

查询AippParam对象的数据类型转换通道像素方差。

该方法用于动态AIPP推理时，根据[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象查询对应索引的数据类型转换像素方差值。 该方法需配合[HMS\_HiAIAippParam\_GetDtcMeanPixel](cannkit.md#hms_hiaiaippparam_getdtcmeanpixel)、[HMS\_HiAIAippParam\_GetDtcMinPixel](cannkit.md#hms_hiaiaippparam_getdtcminpixel)共同使用，来获取所有数据类型转换参数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| varReciPixel[] | 通道像素方差数组，数组size为channelCount。 |
| channelCount | 通道数量，取值范围为[1, 4]，对应从chn0开始。例如channelCount等于3则对应查询通道chn0, chn1, chn2的数据。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_GetInputAippIndex()

PhonePC/2in1TabletTV

```
1. int HMS_HiAIAippParam_GetInputAippIndex (HiAI_AippParam * aippParam)
```

**描述**

查询AippParam对象在该输入的多个输出分支上的索引。

本方法用于在data节点有多个索引时，查询AippParam对象在data节点上的索引。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回-1。 |

**返回：**

成功时返回该AippParam对象在data节点上的索引，失败返回-1。

### HMS\_HiAIAippParam\_GetInputFormat()

PhonePC/2in1TabletTV

```
1. HiAI_ImageFormat HMS_HiAIAippParam_GetInputFormat (HiAI_AippParam * aippParam)
```

**描述**

查询AippParam对象的输入图像格式。

本方法用于动态AIPP推理时，根据[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象查询输入图像格式。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回HIAI\_IMAGE\_FORMAT\_INVALID。 |

**返回：**

成功返回[HiAI\_ImageFormat](cannkit.md#hiai_imageformat)，失败返回HIAI\_IMAGE\_FORMAT\_INVALID。

### HMS\_HiAIAippParam\_GetInputIndex()

PhonePC/2in1TabletTV

```
1. int HMS_HiAIAippParam_GetInputIndex (HiAI_AippParam * aippParam)
```

**描述**

查询AippParam对象所在输入的索引。

本方法用于在多个输入情况下，查询AippParam对象所在输入的索引。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回-1。 |

**返回：**

成功时返回该AippParam对象所在输入的索引，失败返回-1。

### HMS\_HiAIAippParam\_GetInputShape()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_GetInputShape (HiAI_AippParam * aippParam, uint32_t * srcImageW, uint32_t * srcImageH)
```

**描述**

查询AippParam对象的输入图像宽高。

本方法用于动态AIPP推理时，根据[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象查询输入图像宽高。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| srcImageW | 输入图像的宽度，单位为像素。 |
| srcImageH | 输入图像的高度，单位为像素。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_GetPadConfig()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_GetPadConfig (HiAI_AippParam * aippParam, uint32_t batchIndex, uint32_t * leftPadSize, uint32_t * rightPadSize, uint32_t * topPadSize, uint32_t * bottomPadSize)
```

**描述**

查询AippParam对象的输入图像的填充像素数。

本方法用于动态AIPP推理时，根据[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象查询对应索引的对输入图像的填充像素数。 当需要查询channel上的填充值时，需与[HMS\_HiAIAippParam\_GetChannelPadding](cannkit.md#hms_hiaiaippparam_getchannelpadding)一起使用。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| leftPadSize | 图像左侧Padding像素数。 |
| rightPadSize | 图像右侧Padding像素数。 |
| topPadSize | 图像上侧Padding像素数。 |
| bottomPadSize | 图像下侧Padding像素数。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_GetResizeConfig()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_GetResizeConfig (HiAI_AippParam * aippParam, uint32_t batchIndex, uint32_t * resizedW, uint32_t * resizedH)
```

**描述**

查询AippParam对象的图像缩放参数。

本方法用于动态AIPP推理时，根据[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象查询对应索引的缩放后图像宽高值。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| resizedW | 缩放后图像宽度，单位为像素。 |
| resizedH | 缩放后图像高度，单位为像素。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_GetRotationAngle()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_GetRotationAngle (HiAI_AippParam * aippParam, uint32_t batchIndex, float * rotationAngle)
```

**描述**

查询AippParam对象的图像旋转角度。

本方法用于动态AIPP推理时，根据[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象查询对应索引的图像旋转角度。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| rotationAngle | 旋转角度。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_GetSingleBatchMultiCrop()

PhonePC/2in1TabletTV

```
1. bool HMS_HiAIAippParam_GetSingleBatchMultiCrop (HiAI_AippParam * aippParam)
```

**描述**

查询AippParam对象的SingleBatchMultiCrop标识。

本方法用于动态AIPP推理时，根据[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象查询是否为单batch多crop场景。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空。 |

**返回：**

返回真为单batch多crop场景，返回假为非单batch多crop场景。

### HMS\_HiAIAippParam\_SetChannelPadding()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_SetChannelPadding (HiAI_AippParam * aippParam, uint32_t batchIndex, uint32_t paddingValues[], uint32_t channelCount)
```

**描述**

设置AippParam对象的通道padding填充值。

本方法用于动态AIPP推理时，设置AIPP通道padding的填充值到[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| paddingValues[] | 通道填充值数组，填充值范围[-65504, 65504]，默认填充值为0。 |
| channelCount | 通道填充数，当前支持[1, 4]，例如channelCount=3则对应配置通道chn0, chn1, chn2的数据。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_SetChannelSwapConfig()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_SetChannelSwapConfig (HiAI_AippParam * aippParam, bool rbuvSwapSwitch, bool axSwapSwitch)
```

**描述**

设置AippParam对象的ChannelSwap通道交换参数。

本方法用于动态AIPP推理时，设置AippParam通道交换参数到[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象。 AIPP支持两种类型的通道交换：RB/UV通道交换和AX通道交换。 RB/UV通道交换丰富了输入图像的格式，开启RB/UV通道交换后，AIPP支持的图像输入格式比可配置的输入类型丰富了一倍。

| 配置类型 | 可接受图像类型 |
| --- | --- |
| YUV420SP\_U8 | YUV420SP\_U8，YVU420 + rbuv\_swap\_switch |
| XRGB8888\_U8 | XRGB8888\_U8，XBGR + rbuv\_swap\_switch |
| ARGB8888\_U8 | ARGB8888\_U8，ABGR + rbuv\_swap\_switch |
| RGB888\_U8 | BGR888\_U8 + rbuv\_swap\_switch |
| BGR888\_U8 | RGB888\_U8 + rbuv\_swap\_switch |
| YUYV\_U8 | YUYV\_U8，YVYU\_U8 + rbuv\_swap\_switch |
| YUV422SP\_U8 | YUV422SP\_U8，YVU422\_U8 + rbuv\_swap\_switch |
| AYUV444\_U8 | AYUV444\_U8 + rbuv\_swap\_switch |

YUV400\_U8是灰度图，不支持通道交换。

当配置的图像输入格式为XRGB、ARGB或AYUV时，支持开启AX通道交换。开启后，图像第一个通道的输入被搬移到第四个通道上，即当XRGB、ARGB和AYUV开启AX通道交换后，转变为RGBX、RGBA和YUVA。 当模型训练集为RGB格式的图像，而推理时的图像输入为XRGB或者ARGB时，可以通过使能AX通道交换，将RGB通道前移，实现兼容。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| rbuvSwapSwitch | 参数真为使能RB/UV通道交换，参数假为不使能RB/UV通道交换。 |
| axSwapSwitch | 参数真为使能AX通道交换，参数假为不使能AX通道交换。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_SetCropConfig()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_SetCropConfig (HiAI_AippParam * aippParam, uint32_t batchIndex, uint32_t startPosW, uint32_t startPosH, uint32_t croppedW, uint32_t croppedH)
```

**描述**

设置AippParam对象的裁剪参数。

本方法用于动态AIPP推理时，设置裁剪参数到[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象。 YUV类型的图像受图像自身类型的限制，当输入图像类型为YUV420SP、YUYV、YUV422SP和AYUV444时，裁剪的起始坐标和裁剪的宽高需为是偶数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应即将crop出来的图像索引。 |
| startPosW | 裁剪起始位置水平方向坐标，startPosW小于输入图像的宽度，单位为像素。 |
| startPosH | 裁剪起始位置垂直方向坐标，startPosH小于输入图像的高度，单位为像素。 |
| croppedW | 裁剪出的图像宽度，startPosW与cropSizeW之和小于等于输入图像的宽度，单位为像素。 |
| croppedH | 裁剪出的图像高度，startPosH与cropSizeH之和小于等于输入图像的高度，单位为像素。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_SetCscConfig()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_SetCscConfig (HiAI_AippParam * aippParam, HiAI_ImageFormat inputFormat, HiAI_ImageFormat outputFormat, HiAI_ImageColorSpace space)
```

**描述**

设置AippParam对象的CSC色域转换参数。

本方法用于动态AIPP推理时，设置AippParam色域转换参数到[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象。 色域转换（Color Space Conversion，以下简称CSC），特指在YUV444和RGB888两种图像格式之间进行转换。 输入为YUV格式图像(YUV420/YUYV/YUV422SP/AYUV444)，模型训练集可为RGB,BGR，灰度图（YUV400\_U8）。 输入为RGB格式图像(XRGB8888/ARGB8888)，模型训练集可为YUV444SP，YVU444SP，灰度图（YUV400\_U8）。 不支持从YUV400到RGB或BGR的转换。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| inputFormat | 图像输入格式，可参考[HiAI\_ImageFormat](cannkit.md#hiai_imageformat)。 |
| outputFormat | 图像输出格式，可参考[HiAI\_ImageFormat](cannkit.md#hiai_imageformat)。 |
| space | 图像颜色空间类型，可参考[HiAI\_ImageColorSpace](cannkit.md#hiai_imagecolorspace)。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_SetDtcMeanPixel()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_SetDtcMeanPixel (HiAI_AippParam * aippParam, uint32_t batchIndex, uint32_t meanPixel[], uint32_t channelCount)
```

**描述**

设置AippParam对象的数据类型转换通道像素平均值。

数据类型转换（Data Type Conversion，简称DTC），用于将输入图像中像素值转换为模型训练时的数据类型。设置DTC参数，使得转换之后的数据在一个预期的范围，避免强制转换。 数据类型转化功能，将输入的图像数据类型通过转化公式转换为FP16类型送给后续模块计算，实际为依次执行减均值、减最小值和乘方差操作。

计算公式为：U8->FP16: pixelOutChn(i) = [pixelInChn(i)–meanChn(i)–minChn(i)] \* varReciChn(i), i ∈ [0, 4) 其中：pixelOutChn(i)为DTC模块的每个通道的输出值，pixelInChn(i)为DTC模块的每个通道的输入值，meanChn(i)为用户输入的每个通道的均值， minChn(i)为用户输入的每个通道的最小值， varReciChn(i)为用户输入的每个通道的方差。

该方法用于动态AIPP推理时，设置DTC数据类型转换像素平均值到[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象。 该方法需配合[HMS\_HiAIAippParam\_SetDtcMinPixel](cannkit.md#hms_hiaiaippparam_setdtcminpixel)、[HMS\_HiAIAippParam\_SetDtcVarReciPixel](cannkit.md#hms_hiaiaippparam_setdtcvarrecipixel)共同使用。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| meanPixel[] | 通道像素平均值数组，数组size为channelCount，默认值为0。 |
| channelCount | 通道数量，取值范围为[1, 4]，例如channelCount=3则对应配置通道chn0, chn1, chn2的数据。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_SetDtcMinPixel()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_SetDtcMinPixel (HiAI_AippParam * aippParam, uint32_t batchIndex, float minPixel[], uint32_t channelCount)
```

**描述**

设置AippParam对象的数据类型转换通道像素最小值。

该方法用于动态AIPP推理时，设置DTC数据类型转换像素最小值到[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象。 该方法需配合[HMS\_HiAIAippParam\_SetDtcMeanPixel](cannkit.md#hms_hiaiaippparam_setdtcmeanpixel)、[HMS\_HiAIAippParam\_SetDtcVarReciPixel](cannkit.md#hms_hiaiaippparam_setdtcvarrecipixel)共同使用。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| minPixel[] | 通道像素最小值数组，数组size为channelCount，默认值为0。 |
| channelCount | 通道数量，取值范围为[1, 4]，例如channelCount=3则对应配置通道chn0, chn1, chn2的数据。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_SetDtcVarReciPixel()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_SetDtcVarReciPixel (HiAI_AippParam * aippParam, uint32_t batchIndex, float varReciPixel[], uint32_t channelCount)
```

**描述**

设置AippParam对象的数据类型转换通道像素方差。

该方法用于动态AIPP推理时，设置DTC数据类型转换像素方差到[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象。 该方法需配合[HMS\_HiAIAippParam\_SetDtcMeanPixel](cannkit.md#hms_hiaiaippparam_setdtcmeanpixel)、[HMS\_HiAIAippParam\_SetDtcMinPixel](cannkit.md#hms_hiaiaippparam_setdtcminpixel)共同使用。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| varReciPixel[] | 通道像素方差数组，数组size为channelCount，默认值为1.0。 |
| channelCount | 通道数量，取值范围为[1, 4]，例如channelCount=3则对应配置通道chn0, chn1, chn2的数据。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_SetInputAippIndex()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_SetInputAippIndex (HiAI_AippParam * aippParam, uint32_t inputAippIndex)
```

**描述**

设置AippParam对象作用于该输入的多个输出分支上的索引。

本方法用于在data有多个输出分支时，设置AippParam对象作用域该输入的第几个输出分支。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空。 |
| inputAippIndex | 用于标识AIPP配置参数在输入Data有多个输出分支时作用于第几个分支，从0开始计数。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_SetInputFormat()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_SetInputFormat (HiAI_AippParam * aippParam, HiAI_ImageFormat inputFormat)
```

**描述**

设置AippParam对象的输入图像格式。

本方法用于动态AIPP推理时，设置AIPP的输入图像格式到[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象。 AIPP可配置的图像格式为[HiAI\_ImageFormat](cannkit.md#hiai_imageformat)所支持的范围。 图像像素点为Uint8类型，范围为0到255。当图像的输入为YUV类型时，无论是YUV420还是YUV422或者YUYV，AIPP自动将图像数据补齐为YUV444格式。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| inputFormat | 输入图像的格式[HiAI\_ImageFormat](cannkit.md#hiai_imageformat)。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_SetInputIndex()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_SetInputIndex (HiAI_AippParam * aippParam, uint32_t inputIndex)
```

**描述**

设置AippParam在输入上的索引。

本方法用于在多个输入情况下，设置索引以确定该AippParam对象作用于第几个输入。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空。 |
| inputIndex | 用于标识此AIPP参数作用于模型的第几个输入，从0开始计数。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_SetInputShape()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_SetInputShape (HiAI_AippParam * aippParam, uint32_t srcImageW, uint32_t srcImageH)
```

**描述**

设置AippParam对象的输入图像宽高。

本方法用于动态AIPP推理时，设置输入图像宽高到[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| srcImageW | 输入图像的宽度，单位为像素，取值范围[16, 4096]。 |
| srcImageH | 输入图像的高度，单位为像素，取值范围[16, 4096]。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_SetPadConfig()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_SetPadConfig (HiAI_AippParam * aippParam, uint32_t batchIndex, uint32_t leftPadSize, uint32_t rightPadSize, uint32_t topPadSize, uint32_t bottomPadSize)
```

**描述**

设置AippParam对象的输入图像的填充像素数。

本方法用于动态AIPP推理时，设置对输入图像的填充像素数到[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象。包含图像左右上下侧的Padding像素数。 当需要设置channel上的填充值时，需与[HMS\_HiAIAippParam\_SetChannelPadding](cannkit.md#hms_hiaiaippparam_setchannelpadding)一起使用。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| leftPadSize | 图像左侧Padding像素数，经过padding后的图像宽度，需与原始模型维度中宽度保持一致。 |
| rightPadSize | 图像右侧Padding像素数，经过padding后的图像宽度，需与原始模型维度中宽度保持一致。 |
| topPadSize | 图像上侧Padding像素数，经过padding后的图像高度，需与原始模型维度中高度保持一致。 |
| bottomPadSize | 图像下侧Padding像素数，经过padding后的图像高度，需与原始模型维度中高度保持一致。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_SetResizeConfig()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_SetResizeConfig (HiAI_AippParam * aippParam, uint32_t batchIndex, uint32_t resizedW, uint32_t resizedH)
```

**描述**

设置AippParam对象的图像缩放参数。

本方法用于动态AIPP推理时，设置图像缩放参数到[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象。Resize的类型为双线性插值。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| resizedW | 缩放后图像宽度，单位为像素，取值范围[16, 448]，图像宽度缩放倍数的范围[1/16, 16]。 |
| resizedH | 缩放后图像高度，单位为像素，取值范围[16, 4096]，图像高度缩放倍数的范围[1/16, 16]。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_SetRotationAngle()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_SetRotationAngle (HiAI_AippParam * aippParam, uint32_t batchIndex, float rotationAngle)
```

**描述**

设置AippParam对象的旋转角度。

本方法用于动态AIPP推理时，设置旋转角度到[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| rotationAngle | 旋转角度，仅支持0, 90, 180, 270。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIAippParam\_SetSingleBatchMultiCrop()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIAippParam_SetSingleBatchMultiCrop (HiAI_AippParam * aippParam, bool singleBatchMultiCrop)
```

**描述**

设置AippParam对象的SingleBatchMultiCrop标识。

本方法用于动态AIPP推理时，设置AippParam单batch多crop标识到[HiAI\_AippParam](cannkit.md#hiai_aippparam)对象。 对于单个batch的图像输入的场景，支持一次性传入多组crop等AIPP参数，一次推理即能得到全部人脸等的关键点信息。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | [HiAI\_AippParam](cannkit.md#hiai_aippparam)指针实例，非空，否则返回失败。 |
| singleBatchMultiCrop | 参数真为单batch多crop场景，参数假为非单batch多crop场景。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAICompatibility\_CheckFromBuffer()

PhonePC/2in1TabletTV

```
1. HiAI_Compatibility HMS_HiAICompatibility_CheckFromBuffer (const void * data, size_t size)
```

**描述**

查询编译后储存在内存中的模型的兼容性。 若发生不兼容情况，建议重新编译模型。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| data | 编译后模型数据地址，非空，否则返回不兼容。 |
| size | 编译后模型数据大小，非空，否则返回不兼容。 |

**返回：**

成功返回 [HiAI\_Compatibility](cannkit.md#hiai_compatibility)，失败返回不兼容。

### HMS\_HiAICompatibility\_CheckFromFile()

PhonePC/2in1TabletTV

```
1. HiAI_Compatibility HMS_HiAICompatibility_CheckFromFile (const char * file)
```

**描述**

查询编译后储存在文件中的模型的兼容性。 若发生不兼容情况，建议重新编译模型。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| file | 编译后模型文件路径及名称，要求用户进程对文件有访问权限，非空，否则返回不兼容。 |

**返回：**

成功返回 [HiAI\_Compatibility](cannkit.md#hiai_compatibility)，失败返回不兼容。

### HMS\_HiAIOptions\_GetBandMode()

PhonePC/2in1TabletTV

```
1. HiAI_BandMode HMS_HiAIOptions_GetBandMode (const OH_NNCompilation * compilation)
```

**描述**

查询带宽模式。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回默认值。 |

**返回：**

成功返回带宽模式[HiAI\_BandMode](cannkit.md#hiai_bandmode)，失败返回默认值。

### HMS\_HiAIOptions\_GetDeviceMemoryReusePlan()

PhonePC/2in1TabletTV

```
1. HiAI_DeviceMemoryReusePlan HMS_HiAIOptions_GetDeviceMemoryReusePlan (const OH_NNCompilation * compilation)
```

**描述**

查询调优配置中的设备内存复用参数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回默认值。 |

**返回：**

成功时返回[HiAI\_DeviceMemoryReusePlan](cannkit.md#hiai_devicememoryreuseplan)，失败返回默认值。

### HMS\_HiAIOptions\_GetDynamicShapeCacheMode()

PhonePC/2in1TabletTV

```
1. HiAI_DynamicShapeCacheMode HMS_HiAIOptions_GetDynamicShapeCacheMode (const OH_NNCompilation * compilation)
```

**描述**

查询编译前可变shape配置中的cacheMode参数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回默认值。 |

**返回：**

成功时返回[HiAI\_DynamicShapeCacheMode](cannkit.md#hiai_dynamicshapecachemode)，失败返回默认值。

### HMS\_HiAIOptions\_GetDynamicShapeMaxCache()

PhonePC/2in1TabletTV

```
1. size_t HMS_HiAIOptions_GetDynamicShapeMaxCache (const OH_NNCompilation * compilation)
```

**描述**

查询编译前可变shape配置中的最大缓存数量。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回0。 |

**返回：**

成功时返回最大缓存数量，失败返回0。

### HMS\_HiAIOptions\_GetDynamicShapeStatus()

PhonePC/2in1TabletTV

```
1. HiAI_DynamicShapeStatus HMS_HiAIOptions_GetDynamicShapeStatus (const OH_NNCompilation * compilation)
```

**描述**

查询编译前可变shape配置中的状态参数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回默认值。 |

**返回：**

成功时返回[HiAI\_DynamicShapeStatus](cannkit.md#hiai_dynamicshapestatus)，失败返回默认值。

### HMS\_HiAIOptions\_GetFallbackMode()

PhonePC/2in1TabletTV

```
1. HiAI_FallbackMode HMS_HiAIOptions_GetFallbackMode (const OH_NNCompilation * compilation)
```

**描述**

查询调优配置中的回滚模式。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回默认值。 |

**返回：**

成功时返回[HiAI\_FallbackMode](cannkit.md#hiai_fallbackmode)，失败返回默认值。

### HMS\_HiAIOptions\_GetFormatMode()

PhonePC/2in1TabletTV

```
1. HiAI_FormatMode HMS_HiAIOptions_GetFormatMode (const OH_NNCompilation * compilation)
```

**描述**

查询模型编译参数中的数据排列格式。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回默认值。 |

**返回：**

成功返回[HiAI\_FormatMode](cannkit.md#hiai_formatmode)，失败返回默认值。

### HMS\_HiAIOptions\_GetInputTensorShape()

PhonePC/2in1TabletTV

```
1. NN_TensorDesc* HMS_HiAIOptions_GetInputTensorShape (const OH_NNCompilation * compilation, size_t index)
```

**描述**

查询选项参数中指定索引的shape描述。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回空指针。 |
| index | 输入shape的索引，取值为[0, [HMS\_HiAIOptions\_GetInputTensorShapeSize](cannkit.md#hms_hiaioptions_getinputtensorshapesize))。 |

**返回：**

成功返回选项参数中的shape描述，失败返回空指针。

### HMS\_HiAIOptions\_GetInputTensorShapeSize()

PhonePC/2in1TabletTV

```
1. size_t HMS_HiAIOptions_GetInputTensorShapeSize (const OH_NNCompilation * compilation)
```

**描述**

查询选项参数中shape描述的个数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回0。 |

**返回：**

成功返回选项参数中shape描述的个数，失败返回0。

### HMS\_HiAIOptions\_GetModelDeviceCount()

PhonePC/2in1TabletTV

```
1. size_t HMS_HiAIOptions_GetModelDeviceCount (const OH_NNCompilation * compilation)
```

**描述**

查询模型级调优配置中模型的执行设备个数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回0。 |

**返回：**

成功时返回执行设备的个数，失败返回0。

### HMS\_HiAIOptions\_GetModelDeviceOrder()

PhonePC/2in1TabletTV

```
1. HiAI_ExecuteDevice* HMS_HiAIOptions_GetModelDeviceOrder (const OH_NNCompilation * compilation)
```

**描述**

查询模型级调优配置中模型的执行设备列表。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回空指针。 |

**返回：**

成功时返回[HiAI\_ExecuteDevice](cannkit.md#hiai_executedevice)执行设备列表，失败返回空指针。

### HMS\_HiAIOptions\_GetOperatorDeviceCount()

PhonePC/2in1TabletTV

```
1. size_t HMS_HiAIOptions_GetOperatorDeviceCount (const OH_NNCompilation * compilation, const char * operatorName)
```

**描述**

查询算子级调优配置中指定算子的执行设备个数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回0。 |
| operatorName | 算子名称，非空，否则返回0。 |

**返回：**

成功时返回执行设备的个数，失败返回0。

### HMS\_HiAIOptions\_GetOperatorDeviceOrder()

PhonePC/2in1TabletTV

```
1. HiAI_ExecuteDevice* HMS_HiAIOptions_GetOperatorDeviceOrder (const OH_NNCompilation * compilation, const char * operatorName)
```

**描述**

查询算子级调优配置中指定算子的执行设备列表。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回空指针。 |
| operatorName | 算子名称，非空，否则返回空指针。 |

**返回：**

成功时返回[HiAI\_ExecuteDevice](cannkit.md#hiai_executedevice)执行设备列表，失败返回空指针。

### HMS\_HiAIOptions\_GetQuantConfigData()

PhonePC/2in1TabletTV

```
1. void* HMS_HiAIOptions_GetQuantConfigData (const OH_NNCompilation * compilation)
```

**描述**

查询量化配置的数据地址。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回空指针。 |

**返回：**

成功返回量化配置的数据地址，失败返回空指针。

### HMS\_HiAIOptions\_GetQuantConfigSize()

PhonePC/2in1TabletTV

```
1. size_t HMS_HiAIOptions_GetQuantConfigSize (const OH_NNCompilation * compilation)
```

**描述**

查询量化配置的数据大小。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回0。 |

**返回：**

成功返回量化配置的数据大小，失败返回0。

### HMS\_HiAIOptions\_GetTuningCacheDir()

PhonePC/2in1TabletTV

```
1. const char* HMS_HiAIOptions_GetTuningCacheDir (const OH_NNCompilation * compilation)
```

**描述**

查询辅助调优的缓存目录。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回空指针。 |

**返回：**

成功返回缓存目录，失败返回空指针。

### HMS\_HiAIOptions\_GetTuningMode()

PhonePC/2in1TabletTV

```
1. HiAI_TuningMode HMS_HiAIOptions_GetTuningMode (const OH_NNCompilation * compilation)
```

**描述**

查询辅助调优模式。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回默认值。 |

**返回：**

返回辅助调优模式[HiAI\_TuningMode](cannkit.md#hiai_tuningmode)，失败返回默认值。

### HMS\_HiAIOptions\_GetTuningStrategy()

PhonePC/2in1TabletTV

```
1. HiAI_TuningStrategy HMS_HiAIOptions_GetTuningStrategy (const OH_NNCompilation * compilation)
```

**描述**

查询模型优化策略。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回默认值。 |

**返回：**

成功返回[HiAI\_TuningStrategy](cannkit.md#hiai_tuningstrategy)，失败返回默认值。

### HMS\_HiAIOptions\_SetBandMode()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIOptions_SetBandMode (OH_NNCompilation * compilation, HiAI_BandMode bandMode)
```

**描述**

设置NPU与周边硬件IO资源的带宽模式。

根据需要设置合适的值，带宽与功耗成正比，高带宽也意味着高功耗。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回失败。 |
| bandMode | 带宽模式[HiAI\_BandMode](cannkit.md#hiai_bandmode)。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIOptions\_SetDeviceMemoryReusePlan()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIOptions_SetDeviceMemoryReusePlan (OH_NNCompilation * compilation, HiAI_DeviceMemoryReusePlan deviceMemoryReusePlan)
```

**描述**

设置调优配置中的设备内存复用参数。

本方法仅在模型编译阶段生效。用于在调优时，指定设备内存复用方式。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回失败。 |
| deviceMemoryReusePlan | 设备内存复用[HiAI\_DeviceMemoryReusePlan](cannkit.md#hiai_devicememoryreuseplan)。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIOptions\_SetDynamicShapeCacheMode()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIOptions_SetDynamicShapeCacheMode (OH_NNCompilation * compilation, HiAI_DynamicShapeCacheMode mode)
```

**描述**

设置编译前可变shape配置中的缓存模式参数。

本方法仅在模型编译阶段生效，用于在推理阶段期望变更shape，且模型的shape变化数量不超过10个场景。 本方法需与[HMS\_HiAIOptions\_SetDynamicShapeStatus](cannkit.md#hms_hiaioptions_setdynamicshapestatus)、[HMS\_HiAIOptions\_SetDynamicShapeMaxCache](cannkit.md#hms_hiaioptions_setdynamicshapemaxcache)搭配使用。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回失败。 |
| mode | 编译前可变shape的缓存模式[HiAI\_DynamicShapeCacheMode](cannkit.md#hiai_dynamicshapecachemode)。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIOptions\_SetDynamicShapeMaxCache()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIOptions_SetDynamicShapeMaxCache (OH_NNCompilation * compilation, size_t maxCacheCount)
```

**描述**

设置编译前可变shape配置中的最大缓存编译后模型数量。

本方法仅在模型编译阶段生效，用于在推理阶段期望变更shape，且模型的shape变化数量不超过10个场景。 本方法需与[HMS\_HiAIOptions\_SetDynamicShapeStatus](cannkit.md#hms_hiaioptions_setdynamicshapestatus)、[HMS\_HiAIOptions\_SetDynamicShapeCacheMode](cannkit.md#hms_hiaioptions_setdynamicshapecachemode)搭配使用。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回失败。 |
| maxCacheCount | 最大档位，取值范围[1, 10]。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIOptions\_SetDynamicShapeStatus()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIOptions_SetDynamicShapeStatus (OH_NNCompilation * compilation, HiAI_DynamicShapeStatus status)
```

**描述**

设置编译前可变shape配置中的EnableMode参数。

本方法仅在模型编译阶段生效，用于在推理阶段期望变更shape，且模型的shape变化数量不超过10个场景。 本方法需与[HMS\_HiAIOptions\_SetDynamicShapeMaxCache](cannkit.md#hms_hiaioptions_setdynamicshapemaxcache)、[HMS\_HiAIOptions\_SetDynamicShapeCacheMode](cannkit.md#hms_hiaioptions_setdynamicshapecachemode)搭配使用。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回失败。 |
| status | 是否使能编译前可变shape[HiAI\_DynamicShapeStatus](cannkit.md#hiai_dynamicshapestatus)。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIOptions\_SetFallbackMode()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIOptions_SetFallbackMode (OH_NNCompilation * compilation, HiAI_FallbackMode fallbackMode)
```

**描述**

设置调优配置中的回滚模式。

本方法仅在模型编译阶段生效。用于在模型级或算子级调优时，指定的执行设备列表出现不支持时，是否可回滚到其他硬件执行。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回失败。 |
| fallbackMode | 是否使能回滚模式[HiAI\_FallbackMode](cannkit.md#hiai_fallbackmode)。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIOptions\_SetFormatMode()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIOptions_SetFormatMode (OH_NNCompilation * compilation, HiAI_FormatMode formatMode)
```

**描述**

设置模型编译时的数据排列格式。

本方法仅在模型编译阶段生效，用于模型中的数据排列格式与默认值不匹配时的场景。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空。 |
| formatMode | 数据排列格式[HiAI\_FormatMode](cannkit.md#hiai_formatmode)。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIOptions\_SetInputTensorShapes()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIOptions_SetInputTensorShapes (OH_NNCompilation * compilation, NN_TensorDesc * inputTensorDescs[], size_t shapeCount)
```

**描述**

编译时更新模型输入shape。

本方法仅在模型编译阶段生效，用于模型结构及权重不变，模型输入shape需要变化的场景。数组的大小需要与模型的输入数量保持一致。 模型编译后，模型的输入shape将变更为新设置的shape，推理时输入输出数据需符合新的模型输入输出描述。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空。 |
| inputTensorDescs[] | 模型输入shape列表数组NN\_TensorDesc，非空。 |
| shapeCount | 模型输入shape的个数，需与模型输入个数对应。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIOptions\_SetModelDeviceOrder()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIOptions_SetModelDeviceOrder (OH_NNCompilation * compilation, HiAI_ExecuteDevice * executeDevices, size_t deviceCount)
```

**描述**

设置模型级调优配置中模型执行设备列表。

本方法仅在模型编译阶段生效，不可与其他调优混用。用于指定模型的执行设备列表，按照优先级顺序排列。默认NPU优先。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回失败。 |
| executeDevices | 支持的设备类型列表[HiAI\_ExecuteDevice](cannkit.md#hiai_executedevice)，非空，否则返回失败。 |
| deviceCount | 支持的执行硬件个数。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIOptions\_SetOmOptions()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIOptions_SetOmOptions (OH_NNCompilation * compilation, HiAI_OmType type, const char * outputDir)
```

**描述**

设置模型加载时的维测选项信息。

该方法属于可选接口，在模型加载阶段生效，用于模型的性能调试。

**起始版本：** 5.1.0(18)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回失败。 |
| type | 维测类型[HiAI\_OmType](cannkit.md#hiai_omtype)。 |
| outputDir | 维测输出目录，用于生产profiling相关文件。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIOptions\_SetOperatorDeviceOrder()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIOptions_SetOperatorDeviceOrder (OH_NNCompilation * compilation, const char * operatorName, HiAI_ExecuteDevice * executeDevices, size_t deviceCount)
```

**描述**

设置算子级调优配置中算子执行设备列表。

本方法仅在模型编译阶段生效，不可与其他调优混用。用于指定模型中算子的执行设备列表，按照优先级顺序排列，算子名称不可重复。 模型中的算子可以部分指定，不指定的算子以NPU优先，可以使用开源工具Netron查看模型中的算子名称。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回失败。 |
| operatorName | 算子名称，非空，否则返回失败。 |
| executeDevices | 支持的设备类型列表[HiAI\_ExecuteDevice](cannkit.md#hiai_executedevice)，非空，否则返回失败。 |
| deviceCount | 支持的执行硬件个数。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIOptions\_SetQuantConfig()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIOptions_SetQuantConfig (OH_NNCompilation * compilation, void * data, size_t size)
```

**描述**

设置模型编译时量化配置。

本方法仅在模型编译阶段生效。用于模型编译时进行量化的场景。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回失败。 |
| data | 量化配置的数据地址，非空，否则返回失败。 |
| size | 量化配置的数据大小，大于0，否则返回失败。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIOptions\_SetTuningCacheDir()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIOptions_SetTuningCacheDir (OH_NNCompilation * compilation, const char * cacheDir)
```

**描述**

设置辅助调优的缓存目录。

要求用户进程对缓存目录有读写权限。本方法需与[HMS\_HiAIOptions\_SetTuningMode](cannkit.md#hms_hiaioptions_settuningmode)搭配使用。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回失败。 |
| cacheDir | 缓存目录，非空，否则返回失败。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIOptions\_SetTuningMode()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIOptions_SetTuningMode (OH_NNCompilation * compilation, HiAI_TuningMode tuningMode)
```

**描述**

选择辅助调优模式。

本方法仅在模型编译阶段生效，不可与其他调优混用。用于指定CANN Kit协助进行调优的场景。 本方法需与[HMS\_HiAIOptions\_SetTuningCacheDir](cannkit.md#hms_hiaioptions_settuningcachedir)搭配使用。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回失败。 |
| tuningMode | 辅助调优模式[HiAI\_TuningMode](cannkit.md#hiai_tuningmode)。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAIOptions\_SetTuningStrategy()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAIOptions_SetTuningStrategy (OH_NNCompilation * compilation, HiAI_TuningStrategy tuningStrategy)
```

**描述**

设置模型编译时的模型优化策略。

本方法仅在模型编译阶段生效。用于模型算子深度融合的场景。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH\_NNCompilation指针实例，非空，否则返回失败。 |
| tuningStrategy | 模型优化策略配置[HiAI\_TuningStrategy](cannkit.md#hiai_tuningstrategy)。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAISingleOpBuffer\_Create()

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpBuffer* HMS_HiAISingleOpBuffer_Create (size_t dataSize)
```

**描述**

按照指定的内存大小创建[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)对象。

本方法用于根据指定的**dataSize**申请对应大小的ION内存，并创建[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)对象。当不再使用[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)对象时， 调用[HMS\_HiAISingleOpBuffer\_Destroy](cannkit.md#hms_hiaisingleopbuffer_destroy)销毁，否则会造成内存泄漏。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| dataSize | 要申请的内存字节大小。该值不能为0，否则返回空指针。 |

**返回：**

指向[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)对象的指针，如果创建失败则返回空指针。

### HMS\_HiAISingleOpBuffer\_Destroy()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAISingleOpBuffer_Destroy (HiAI_SingleOpBuffer ** buffer)
```

**描述**

释放[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)对象。

本方法用于释放调用[HMS\_HiAISingleOpBuffer\_Create](cannkit.md#hms_hiaisingleopbuffer_create)创建的[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)对象。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| buffer | 指向[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)对象的二级指针。**buffer**和 **\*buffer**不能是空指针，否则返回错误码。 |

**返回：**

函数执行的结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAISingleOpBuffer\_GetData()

PhonePC/2in1TabletTV

```
1. void* HMS_HiAISingleOpBuffer_GetData (const HiAI_SingleOpBuffer * buffer)
```

**描述**

查询[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)的内存地址。

本方法用于获取指定[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)对象的内存地址。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| buffer | 指向[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)对象的指针。该值不能为空指针，否则返回空指针。 |

**返回：**

Buffer的内存地址。

### HMS\_HiAISingleOpBuffer\_GetSize()

PhonePC/2in1TabletTV

```
1. size_t HMS_HiAISingleOpBuffer_GetSize (const HiAI_SingleOpBuffer * buffer)
```

**描述**

查询[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)的字节大小。

本方法用于获取指定[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)对象的字节大小。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| buffer | 指向[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)对象的指针。该值不能为空指针，否则返回0。 |

**返回：**

Buffer的字节大小。

### HMS\_HiAISingleOpDescriptor\_CreateActivation()

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpDescriptor* HMS_HiAISingleOpDescriptor_CreateActivation (HiAI_SingleOpActivationType activationType, float coef)
```

**描述**

创建激活函数类的描述符对象。

本方法用于根据传入的参数创建激活函数类的[HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor)对象。当不再使用[HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor)对象时，调用[HMS\_HiAISingleOpDescriptor\_Destroy](cannkit.md#hms_hiaisingleopdescriptor_destroy)销毁，否则会造成内存泄漏。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| activationType | 激活模式。 |
| coef | 如果激活模式为带系数的激活类型，该值表示系数。否则，该值不会生效。 |

**返回：**

指向[HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor)对象的指针，如果创建失败则返回空指针。

### HMS\_HiAISingleOpDescriptor\_CreateConvolution()

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpDescriptor* HMS_HiAISingleOpDescriptor_CreateConvolution (HiAISingleOpDescriptor_ConvolutionParam param)
```

**描述**

创建卷积类（普通卷积、转置卷积、深度卷积）的描述符对象。

本方法用于根据传入的参数创建卷积类的[HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor)对象。当不再使用[HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor)对象时，调用[HMS\_HiAISingleOpDescriptor\_Destroy](cannkit.md#hms_hiaisingleopdescriptor_destroy)销毁，否则会造成内存泄漏。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| param | 详细输入参数参见[HiAISingleOpDescriptor\_ConvolutionParam](cannkit-sopdesc-convparam.md)。 |

**返回：**

指向[HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor)对象的指针，如果创建失败则返回空指针。

### HMS\_HiAISingleOpDescriptor\_Destroy()

PhonePC/2in1TabletTV

```
1. void HMS_HiAISingleOpDescriptor_Destroy (HiAI_SingleOpDescriptor ** opDesc)
```

**描述**

释放[HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor)对象。

当不再使用[HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor)对象时，调用该接口销毁，否则会造成内存泄漏。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| opDesc | 指向[HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor)对象的二级指针。**opDesc**和 **\*opDesc**不能是空指针，否则销毁失败。 |

### HMS\_HiAISingleOpExecutor\_CreateConvolution()

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpExecutor* HMS_HiAISingleOpExecutor_CreateConvolution (HiAI_SingleOpExecutorConvolutionParam param)
```

**描述**

创建卷积类算子对应的[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)对象。

当不再使用[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)对象时，调用[HMS\_HiAISingleOpExecutor\_Destroy](cannkit.md#hms_hiaisingleopexecutor_destroy)销毁，否则会造成内存泄漏。

对于输出Tensor描述，其数据类型和排布格式可以同时为HIAI\_SINGLEOP\_DT\_UNDEFINED和HIAI\_SINGLEOP\_FORMAT\_RESERVED。在这种情况下，执行器会将输出的数据类型和排布格式设置为适配硬件的类型。该接口执行成功后，可以调用[HMS\_HiAISingleOpExecutor\_UpdateOutputTensorDesc](cannkit.md#hms_hiaisingleopexecutor_updateoutputtensordesc)更新输出Tensor描述的数据类型和排布格式。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| param | 详细输入参数参见[HiAI\_SingleOpExecutorConvolutionParam](cannkit-sopexec-convparam.md)。 |

**返回：**

指向[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)对象的指针，如果创建失败，则返回空指针。

### HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation()

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpExecutor* HMS_HiAISingleOpExecutor_CreateFusedConvolutionActivation (HiAI_SingleOpExecutorFusedConvolutionActivationParam param)
```

**描述**

创建卷积和激活融合算子对应的[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)对象。

当不再使用[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)对象时，调用[HMS\_HiAISingleOpExecutor\_Destroy](cannkit.md#hms_hiaisingleopexecutor_destroy)销毁，否则会造成内存泄漏。

对于输出Tensor描述，其数据类型和排布格式可以为HIAI\_SINGLEOP\_DT\_UNDEFINED和HIAI\_SINGLEOP\_FORMAT\_RESERVED。在这种情况下，执行器会将输出的数据类型和排布格式设置为适配硬件的类型。该接口执行成功后，可以调用[HMS\_HiAISingleOpExecutor\_UpdateOutputTensorDesc](cannkit.md#hms_hiaisingleopexecutor_updateoutputtensordesc)更新输出Tensor描述的数据类型和排布格式。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| param | 详细输入参数参见[HiAI\_SingleOpExecutorFusedConvolutionActivationParam](cannkit-sopexec-fusedconv-actparam.md)。 |

**返回：**

指向[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)对象的指针，如果创建失败，则返回空指针。

### HMS\_HiAISingleOpExecutor\_Destroy()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAISingleOpExecutor_Destroy (HiAI_SingleOpExecutor ** executor)
```

**描述**

销毁[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)对象，释放执行器占用的内存。

当不再使用[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)对象时，调用该接口销毁，否则会造成内存泄漏。

注意：该接口不会释放传递给[HMS\_HiAISingleOpExecutor\_Init](cannkit.md#hms_hiaisingleopexecutor_init)的工作空间内存，工作空间所属的[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)需要单独释放。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| executor | 指向[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)对象的二级指针。**executor**和 **\*executor**不能是空指针，否则返回错误码。 |

**返回：**

函数执行的结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAISingleOpExecutor\_Execute()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAISingleOpExecutor_Execute (HiAI_SingleOpExecutor * executor, HiAI_SingleOpTensor * input[], int32_t inputNum, HiAI_SingleOpTensor * output[], int32_t outputNum)
```

**描述**

执行同步运算推理。

在调用该接口前，需要先通过[HMS\_HiAISingleOpTensor\_CreateFromTensorDesc](cannkit.md#hms_hiaisingleoptensor_createfromtensordesc)或[HMS\_HiAISingleOpTensor\_CreateFromSingleOpBuffer](cannkit.md#hms_hiaisingleoptensor_createfromsingleopbuffer)接口创建输入和输出Tensor并填充输入Tensor数据。执行器会通过执行推理产生推理结果，并将结果写入输出Tensor中。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| executor | 指向[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)对象的指针。该值不能为空指针，否则返回错误码。 |
| input[] | 输入Tensor的数组。 |
| inputNum | 输入Tensor的数量。 |
| output[] | 输出Tensor的数组。 |
| outputNum | 输出Tensor的数量。 |

**返回：**

函数执行的结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAISingleOpExecutor\_GetWorkspaceSize()

PhonePC/2in1TabletTV

```
1. size_t HMS_HiAISingleOpExecutor_GetWorkspaceSize (const HiAI_SingleOpExecutor * executor)
```

**描述**

查询[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)所需的ION内存工作空间的字节大小。

在成功创建[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)后，调用该接口获取执行器所需的ION内存工作空间的字节大小，然后需要调用[HMS\_HiAISingleOpBuffer\_Create](cannkit.md#hms_hiaisingleopbuffer_create)申请足够的工作空间内存，将分配的工作空间传入[HMS\_HiAISingleOpExecutor\_Init](cannkit.md#hms_hiaisingleopexecutor_init)接口。

注意：同一个执行器的工作空间内存和输入、输出Tensor内存不能复用，不同执行器的工作空间内存可以复用。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| executor | 指向[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)对象的指针。该值不能为空指针，否则返回0。 |

**返回：**

工作空间的字节大小。

### HMS\_HiAISingleOpExecutor\_Init()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAISingleOpExecutor_Init (HiAI_SingleOpExecutor * executor, void * workspace, size_t workspaceSize)
```

**描述**

加载[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)。

在调用该接口之前，需要申请执行器所需的工作空间内存。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| executor | 指向[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)对象的指针。该值不能为空指针，否则返回错误码。 |
| workspace | 工作空间地址。当**workspaceSize**不为0时，该值必须为[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)中的内存地址，否则返回错误码。 |
| workspaceSize | 提供的**workspace**的字节大小。该值必须大于等于[HMS\_HiAISingleOpExecutor\_GetWorkspaceSize](cannkit.md#hms_hiaisingleopexecutor_getworkspacesize)获取的所需工作空间大小， 否则返回错误码。 |

**返回：**

函数执行的结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAISingleOpExecutor\_PreCheckConvolution()

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpSupportStatus HMS_HiAISingleOpExecutor_PreCheckConvolution (HiAI_SingleOpExecutorConvolutionParam param)
```

**描述**

预查询卷积算子的支持状态。

根据该接口的返回值确定是否调用[HMS\_HiAISingleOpExecutor\_CreateConvolution](cannkit.md#hms_hiaisingleopexecutor_createconvolution)来创建卷积执行器，也可以不调用本方法，直接调用创建卷积执行器。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| param | 详细输入参数参见[HiAI\_SingleOpExecutorConvolutionParam](cannkit-sopexec-convparam.md)。 |

**返回：**

支持状态。具体状态请参考[HiAI\_SingleOpSupportStatus](cannkit.md#hiai_singleopsupportstatus)。

### HMS\_HiAISingleOpExecutor\_PreCheckFusedConvolutionActivation()

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpSupportStatus HMS_HiAISingleOpExecutor_PreCheckFusedConvolutionActivation (HiAI_SingleOpExecutorFusedConvolutionActivationParam param)
```

**描述**

预查询卷积和激活融合算子的支持状态。

根据该接口的返回值确定是否调用[HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation](cannkit.md#hms_hiaisingleopexecutor_createfusedconvolutionactivation)来创建卷积激活融合执行器，也可以不调用本方法，直接创建卷积激活融合执行器。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| param | 详细输入参数参见[HiAI\_SingleOpExecutorFusedConvolutionActivationParam](cannkit-sopexec-fusedconv-actparam.md)。 |

**返回：**

支持状态。具体状态请参考[HiAI\_SingleOpSupportStatus](cannkit.md#hiai_singleopsupportstatus)。

### HMS\_HiAISingleOpExecutor\_UpdateOutputTensorDesc()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAISingleOpExecutor_UpdateOutputTensorDesc (const HiAI_SingleOpExecutor * executor, uint32_t index, HiAI_SingleOpTensorDesc * output)
```

**描述**

更新[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)的输出tensor描述。

如果在创建[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)时，输入参数**output**数据类型为HIAI\_SINGLEOP\_DT\_UNDEFINED，且排布格式为HIAI\_SINGLEOP\_FORMAT\_RESERVED，那么在成功创建[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)后，调用该接口将输出Tensor描述更新为硬件适配的数据类型和排布格式。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| executor | 指向[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)对象的指针。该值不能为空指针，否则返回错误码。 |
| index | 输出Tensor描述的索引，与创建executor时的输出顺序一致。索引值从0开始。 |
| output | 需要更新的[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象的指针。 |

**返回：**

函数执行的结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAISingleOpOptions\_Create()

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpOptions* HMS_HiAISingleOpOptions_Create (void)
```

**描述**

创建[HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions)对象。

当不再使用[HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions)对象时，调用[HMS\_HiAISingleOpOptions\_Destroy](cannkit.md#hms_hiaisingleopoptions_destroy)销毁，否则会造成内存泄漏。

**起始版本：** 5.0.0(12)

**返回：**

指向[HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions)对象的指针，如果创建失败则返回空指针。

### HMS\_HiAISingleOpOptions\_Destroy()

PhonePC/2in1TabletTV

```
1. void HMS_HiAISingleOpOptions_Destroy (HiAI_SingleOpOptions ** options)
```

**描述**

释放[HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions)对象。

本方法用于释放调用[HMS\_HiAISingleOpOptions\_Create](cannkit.md#hms_hiaisingleopoptions_create)创建的[HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions)对象。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| options | 指向[HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions)对象的二级指针。**options**和 **\*options**不能是空指针，否则销毁失败。 |

### HMS\_HiAISingleOpTensor\_CreateFromConst()

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpTensor* HMS_HiAISingleOpTensor_CreateFromConst (const HiAI_SingleOpTensorDesc * desc, void * data, size_t dataSize)
```

**描述**

根据[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)、常量数据（如卷积权重、偏置等）的内存地址和数据大小创建[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象。

本方法用于根据[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)和常量数据（如卷积权重、偏置等）的内存地址和数据大小创建[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象。

本方法直接复用**data**和**dataSize**对应的常量数据，不会进行数据的拷贝。因此，在本方法创建的Tensor仍要被使用时，不要释放该Tensor对应的常量数据内存。本方法仅读取**data**和**dataSize**对应的常量数据，不会修改其数据。

注意：该接口会将**desc**拷贝到[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)中。因此，当**desc**不再使用时，请使用[HMS\_HiAISingleOpTensorDesc\_Destroy](cannkit.md#hms_hiaisingleoptensordesc_destroy)销毁**desc**。

当不再使用[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象时，调用[HMS\_HiAISingleOpTensor\_Destroy](cannkit.md#hms_hiaisingleoptensor_destroy)销毁，否则会造成内存泄漏。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| desc | 指向[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象的指针。该值不能为空指针，否则返回空指针。 |
| data | 常量数据地址。该值不能为空指针，否则返回空指针。 |
| dataSize | 常量数据大小。该值不能为0，否则返回空指针。 |

**返回：**

指向[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象的指针，如果创建失败则返回空指针。

### HMS\_HiAISingleOpTensor\_CreateFromSingleOpBuffer()

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpTensor* HMS_HiAISingleOpTensor_CreateFromSingleOpBuffer (const HiAI_SingleOpTensorDesc * desc, void * data, size_t dataSize)
```

**描述**

根据[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)、[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)的内存地址和数据大小创建[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象。

本方法复用[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)的ION内存，所复用的内存地址和大小由**data**和**dataSize**确定。**dataSize**必须等于通过[HMS\_HiAISingleOpTensorDesc\_GetByteSize](cannkit.md#hms_hiaisingleoptensordesc_getbytesize)计算得到的**desc**的字节大小。当调用[HMS\_HiAISingleOpTensor\_Destroy](cannkit.md#hms_hiaisingleoptensor_destroy)接口销毁该接口创建的Tensor时，不会释放该Tensor数据的内存。

注意：该接口会将**desc**拷贝到[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)中。因此，当**desc**不再使用时，请使用[HMS\_HiAISingleOpTensorDesc\_Destroy](cannkit.md#hms_hiaisingleoptensordesc_destroy)销毁**desc**。

当不再使用[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象时，调用[HMS\_HiAISingleOpTensor\_Destroy](cannkit.md#hms_hiaisingleoptensor_destroy)销毁，否则会造成内存泄漏。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| desc | 指向[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象的指针。该值不能为空指针，否则返回空指针。 |
| data | Tensor数据地址。该值必须是[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)中的内存地址，否则返回空指针。 |
| dataSize | Tensor数据大小。该值不能为0，否则返回空指针。 |

**返回：**

指向[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象的指针，如果创建失败则返回空指针。

### HMS\_HiAISingleOpTensor\_CreateFromTensorDesc()

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpTensor* HMS_HiAISingleOpTensor_CreateFromTensorDesc (const HiAI_SingleOpTensorDesc * desc)
```

**描述**

根据[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)创建[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象。

本方法使用[HMS\_HiAISingleOpTensorDesc\_GetByteSize](cannkit.md#hms_hiaisingleoptensordesc_getbytesize)计算Tensor数据的字节数， 并使用[HMS\_HiAISingleOpBuffer\_Create](cannkit.md#hms_hiaisingleopbuffer_create)为Tensor数据分配ION内存。设备驱动将通过“零拷贝”的方式直接获取张量数据。

注意：该接口会将**desc**拷贝到[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)中。因此，当**desc**不再使用时，请使用[HMS\_HiAISingleOpTensorDesc\_Destroy](cannkit.md#hms_hiaisingleoptensordesc_destroy)销毁**desc**。

当不再使用[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象时，调用[HMS\_HiAISingleOpTensor\_Destroy](cannkit.md#hms_hiaisingleoptensor_destroy)销毁，否则会造成内存泄漏。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| desc | 指向[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象的指针。该值不能为空指针，否则返回空指针。 |

**返回：**

指向[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象的指针，如果创建失败则返回空指针。

### HMS\_HiAISingleOpTensor\_Destroy()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAISingleOpTensor_Destroy (HiAI_SingleOpTensor ** tensor)
```

**描述**

释放[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象。

当不再使用[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象时，需要调用该接口销毁该对象，否则会造成内存泄漏。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tensor | 指向[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象的二级指针。**tensor**和 **\*tensor**不能是空指针，否则返回错误码。 |

**返回：**

函数执行的结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。

### HMS\_HiAISingleOpTensor\_GetBuffer()

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpBuffer* HMS_HiAISingleOpTensor_GetBuffer (const HiAI_SingleOpTensor * tensor)
```

**描述**

获取[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)的Buffer。

本方法用于获取指定[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象的[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tensor | 指向[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象的指针。该值不能为空指针，否则返回空指针。 |

**返回：**

指向[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)对象的指针。

### HMS\_HiAISingleOpTensor\_GetTensorDesc()

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpTensorDesc* HMS_HiAISingleOpTensor_GetTensorDesc (const HiAI_SingleOpTensor * tensor)
```

**描述**

获取[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)的Tensor描述。

本方法用于获取指定[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象的[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tensor | 指向[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象的指针。该值不能为空指针，否则返回空指针。 |

**返回：**

指向[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象的指针。

### HMS\_HiAISingleOpTensorDesc\_Create()

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpTensorDesc* HMS_HiAISingleOpTensorDesc_Create (const int64_t * dims, size_t dimNum, HiAI_SingleOpDataType dataType, HiAI_SingleOpFormat format, bool isVirtual)
```

**描述**

创建[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象。

本方法用于根据传入的维度、数据类型、排布格式等参数创建[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象。

可以调用以下接口，基于传入的[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)指针创建[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象： [HMS\_HiAISingleOpTensor\_CreateFromTensorDesc](cannkit.md#hms_hiaisingleoptensor_createfromtensordesc)、[HMS\_HiAISingleOpTensor\_CreateFromSingleOpBuffer](cannkit.md#hms_hiaisingleoptensor_createfromsingleopbuffer)、 [HMS\_HiAISingleOpTensor\_CreateFromConst](cannkit.md#hms_hiaisingleoptensor_createfromconst)。

注意：这些接口会将[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象复制到[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)中。 当[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象不再使用时，调用[HMS\_HiAISingleOpTensorDesc\_Destroy](cannkit.md#hms_hiaisingleoptensordesc_destroy)接口销毁，否则会造成内存泄漏。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| dims | 张量维度列表。该值不能为空指针，否则返回空指针。 |
| dimNum | 张量维度数量。该值不能为0，否则返回空指针。 |
| dataType | 张量数据类型。 |
| format | 张量排布格式。 |
| isVirtual | 表示张量是否是虚拟张量。true表示该张量为虚拟张量，false表示该张量为非虚拟张量。虚拟张量是相连的CANN Kit单算子之间的中间张量，其中的数据仅暂时存在，不经非CANN Kit单算子内存读取或写入。例如， 若CANN Kit单算子A的输出张量T1仅作为CANN Kit单算子B的输入张量，且用户只读取单算子B的输出张量T2，不会读取或写入T1，那么T1需要被设置为虚拟张量，而T2则是非虚拟张量。 |

**返回：**

指向[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象的指针，如果创建失败，则返回空指针。

### HMS\_HiAISingleOpTensorDesc\_Destroy()

PhonePC/2in1TabletTV

```
1. void HMS_HiAISingleOpTensorDesc_Destroy (HiAI_SingleOpTensorDesc ** tensorDesc)
```

**描述**

释放[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象。

本方法用于释放调用[HMS\_HiAISingleOpTensorDesc\_Create](cannkit.md#hms_hiaisingleoptensordesc_create)创建的[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tensorDesc | 指向[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象的二级指针。 **tensorDesc**和 **\*tensorDesc**不能为空指针。 |

### HMS\_HiAISingleOpTensorDesc\_GetByteSize()

PhonePC/2in1TabletTV

```
1. size_t HMS_HiAISingleOpTensorDesc_GetByteSize (const HiAI_SingleOpTensorDesc * tensorDesc)
```

**描述**

查询基于[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)的维度和数据类型计算的数据占用字节数。

本方法用于获取基于[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)的维度和数据类型计算得到的数据占用字节数。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tensorDesc | 指向[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象的指针。该值不能为空指针，否则返回0。 |

**返回：**

张量的数据字节数。

### HMS\_HiAISingleOpTensorDesc\_GetDataType()

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpDataType HMS_HiAISingleOpTensorDesc_GetDataType (const HiAI_SingleOpTensorDesc * tensorDesc)
```

**描述**

查询[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)的数据类型。

本方法用于获取指定[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象的数据类型。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tensorDesc | 指向[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象的指针。该值不能为空指针，否则返回HIAI\_SINGLEOP\_DT\_UNDEFINED。 |

**返回：**

张量的数据类型。

### HMS\_HiAISingleOpTensorDesc\_GetDimension()

PhonePC/2in1TabletTV

```
1. int64_t HMS_HiAISingleOpTensorDesc_GetDimension (const HiAI_SingleOpTensorDesc * tensorDesc, size_t index)
```

**描述**

查询[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)指定索引的维度长度。

本方法用于获取指定[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象的某个维度的长度。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tensorDesc | 指向[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象的指针。该值不能为空指针，否则返回0。 |
| index | 维度的索引值。索引从0开始。 |

**返回：**

张量的索引为**index**的维度的长度，如果执行失败，则返回0。

### HMS\_HiAISingleOpTensorDesc\_GetDimensionCount()

PhonePC/2in1TabletTV

```
1. size_t HMS_HiAISingleOpTensorDesc_GetDimensionCount (const HiAI_SingleOpTensorDesc * tensorDesc)
```

**描述**

查询[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)的维度数量。

本方法用于获取指定[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象的维度数量。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tensorDesc | 指向[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象的指针。该值不能为空指针，否则返回0。 |

**返回：**

张量的维度数量，如果执行失败，则返回0。

### HMS\_HiAISingleOpTensorDesc\_GetFormat()

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpFormat HMS_HiAISingleOpTensorDesc_GetFormat (const HiAI_SingleOpTensorDesc * tensorDesc)
```

**描述**

查询[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)的排布格式。

本方法用于获取指定[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象的排布格式。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tensorDesc | 指向[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象的指针。该值不能为空指针，否则返回HIAI\_SINGLEOP\_FORMAT\_RESERVED。 |

**返回：**

张量的排布格式。

### HMS\_HiAISingleOpTensorDesc\_IsVirtual()

PhonePC/2in1TabletTV

```
1. bool HMS_HiAISingleOpTensorDesc_IsVirtual (const HiAI_SingleOpTensorDesc * tensorDesc)
```

**描述**

查询[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)是否为虚拟张量。

虚拟张量是相连的CANN Kit单算子之间的中间张量，其中的数据仅暂时存在，不经非CANN Kit单算子内存读取或写入。例如，若CANN Kit单算子A的输出张量T1仅作为CANN Kit单算子B的输入张量，且用户只读取单算子B的输出张量T2，不会读取或写入T1， 那么T1需要被设置为虚拟张量，而T2则是非虚拟张量。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tensorDesc | 指向[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象的指针。该值不能为空指针，否则返回false。 |

**返回：**

如果张量是虚拟张量，则返回true，否则返回false。

### HMS\_HiAITensor\_GetSizeWithImageFormat()

PhonePC/2in1TabletTV

```
1. size_t HMS_HiAITensor_GetSizeWithImageFormat (NN_TensorDesc * desc, HiAI_ImageFormat format)
```

**描述**

根据NN\_TensorDesc和HiAI\_ImageFormat计算申请tensor的大小。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| desc | NN\_TensorDesc指针实例，非空，否则返回0。 |
| format | 图像的格式[HiAI\_ImageFormat](cannkit.md#hiai_imageformat)。 |

**返回：**

成功时返回计算后需要申请的tensor的大小，失败返回0。

### HMS\_HiAITensor\_SetAippParams()

PhonePC/2in1TabletTV

```
1. OH_NN_ReturnCode HMS_HiAITensor_SetAippParams (NN_Tensor * tensor, HiAI_AippParam * aippParams[], size_t aippNum)
```

**描述**

给NN\_Tensor设置AippParams。

AIPP参数设置给NN\_Tensor后，其内存在tensor使用完成后，调用[HMS\_HiAIAippParam\_Destroy](cannkit.md#hms_hiaiaippparam_destroy)释放。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tensor | NN\_Tensor指针实例，非空，否则返回空指针。 |
| aippParams[] | AIPP参数数组。 |
| aippNum | AIPP参数数量。 |

**返回：**

函数执行结果状态。执行成功返回OH\_NN\_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH\_NN\_ReturnCode](capi-neural-network-runtime-type-h.md#oh_nn_returncode)。
