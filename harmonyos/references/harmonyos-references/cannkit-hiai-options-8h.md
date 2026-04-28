---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-hiai-options-8h
title: hiai_options.h
breadcrumb: API参考 > AI > CANN Kit（CANN异构计算框架服务） > C API > 头文件和结构体 > 头文件 > hiai_options.h
category: harmonyos-references
scraped_at: 2026-04-28T08:18:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5707ae18071014e077d89a272901e32d3c50f06e5de1f755cc9dc7524f72f631
---

## 概述

PhonePC/2in1TabletTV

选项参数的接口。

支持设置动态shape、变更模型shape、设置数据排列格式、算子融合策略、量化配置、算子级调优、模型级调优、辅助调优、带宽模式等参数配置。

**引用文件：** <CANNKit/hiai\_options.h>

**库：** libhiai\_foundation.so

**系统能力：** SystemCapability.AI.HiAIFoundation

**起始版本：** 4.1.0(11)

**相关模块：** [CANN](cannkit.md)

## 汇总

PhonePC/2in1TabletTV

### 枚举

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [HiAI\_FormatMode](cannkit.md#hiai_formatmode) {  HIAI\_FORMAT\_MODE\_NCHW = 0,  HIAI\_FORMAT\_MODE\_ORIGIN = 1  } | 模型编译时数据的排列格式。 |
| [HiAI\_DynamicShapeStatus](cannkit.md#hiai_dynamicshapestatus) {  HIAI\_DYNAMIC\_SHAPE\_DISABLED = 0,  HIAI\_DYNAMIC\_SHAPE\_ENABLED = 1  } | 是否使能编译前可变shape。 |
| [HiAI\_DynamicShapeCacheMode](cannkit.md#hiai_dynamicshapecachemode) {  HIAI\_DYNAMIC\_SHAPE\_CACHE\_BUILT\_MODEL = 0,  HIAI\_DYNAMIC\_SHAPE\_CACHE\_LOADED\_MODEL = 1  } | 编译前可变shape支持的模式。 |
| [HiAI\_ExecuteDevice](cannkit.md#hiai_executedevice) {  HIAI\_EXECUTE\_DEVICE\_NPU = 0,  HIAI\_EXECUTE\_DEVICE\_CPU = 1,  HIAI\_EXECUTE\_DEVICE\_GPU = 2  } | 模型运行时支持的设备类型。 |
| [HiAI\_FallbackMode](cannkit.md#hiai_fallbackmode) {  HIAI\_FALLBACK\_ENABLED = 0,  HIAI\_FALLBACK\_DISABLED = 1  } | 指定的硬件设备无法编译模型时，是否允许CANN Kit选择其他硬件设备，例如CPU。 |
| [HiAI\_DeviceMemoryReusePlan](cannkit.md#hiai_devicememoryreuseplan) {  HIAI\_DEVICE\_MEMORY\_REUSE\_PLAN\_UNSET = 0,  HIAI\_DEVICE\_MEMORY\_REUSE\_PLAN\_LOW = 1,  HIAI\_DEVICE\_MEMORY\_REUSE\_PLAN\_HIGH = 2  } | 设备内存复用配置选项。 |
| [HiAI\_TuningStrategy](cannkit.md#hiai_tuningstrategy) {  HIAI\_TUNING\_STRATEGY\_OFF = 0,  HIAI\_TUNING\_STRATEGY\_ON\_DEVICE\_TUNING = 1,  HIAI\_TUNING\_STRATEGY\_ON\_DEVICE\_PREPROCESS\_TUNING = 2,  HIAI\_TUNING\_STRATEGY\_ON\_CLOUD\_TUNING = 3  } | 模型优化策略配置选项。 |
| [HiAI\_TuningMode](cannkit.md#hiai_tuningmode) {  HIAI\_TUNING\_MODE\_UNSET = 0,  HIAI\_TUNING\_MODE\_AUTO = 1,  HIAI\_TUNING\_MODE\_HETER = 2  } | 辅助调优模式。 |
| [HiAI\_BandMode](cannkit.md#hiai_bandmode) {  HIAI\_BANDMODE\_UNSET = 0,  HIAI\_BANDMODE\_LOW = 1,  HIAI\_BANDMODE\_NORMAL = 2,  HIAI\_BANDMODE\_HIGH = 3  } | 定义硬件之间带宽模式。 |
| [HiAI\_OmType](cannkit.md#hiai_omtype) {  HIAI\_OM\_TYPE\_OFF = 0,  HIAI\_OM\_TYPE\_PROFILING = 1,  HIAI\_OM\_TYPE\_DUMP = 2  } | 维测类型定义。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
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
| OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetOmOptions](cannkit.md#hms_hiaioptions_setomoptions)(OH\_NNCompilation \*compilation, [HiAI\_OmType](cannkit.md#hiai_omtype) type, const char \*outputDir) | 设置模型加载时的维测选项信息。 |
