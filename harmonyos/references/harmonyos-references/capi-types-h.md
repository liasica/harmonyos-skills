---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-types-h
title: types.h
breadcrumb: API参考 > AI > MindSpore Lite Kit（昇思推理框架服务） > C API > 头文件 > types.h
category: harmonyos-references
scraped_at: 2026-04-28T08:19:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2d518309db54b961ce8b0c33420060f6f85166804c6cb2dd7343627a9b7a9acd
---

## 概述

PhonePC/2in1TabletTVWearable

提供了MindSpore Lite支持的模型文件类型和设备类型。

**引用文件：** <mindspore/types.h>

**库：** libmindspore\_lite\_ndk.so

**系统能力：** SystemCapability.Ai.MindSpore

**起始版本：** 9

**相关模块：** [MindSpore](capi-mindspore.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [NNRTDeviceDesc](capi-mindspore-nnrtdevicedesc.md) | NNRTDeviceDesc | NNRt设备信息描述，包含设备ID，设备名称等信息。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AI\_ModelType](capi-types-h.md#oh_ai_modeltype) | OH\_AI\_ModelType | 模型文件的类型。 |
| [OH\_AI\_DeviceType](capi-types-h.md#oh_ai_devicetype) | OH\_AI\_DeviceType | 设备类型信息，包含了目前支持的设备类型。 |
| [OH\_AI\_NNRTDeviceType](capi-types-h.md#oh_ai_nnrtdevicetype) | OH\_AI\_NNRTDeviceType | NNRt管理的硬件设备类型。 |
| [OH\_AI\_PerformanceMode](capi-types-h.md#oh_ai_performancemode) | OH\_AI\_PerformanceMode | NNRt硬件的工作性能模式。 |
| [OH\_AI\_Priority](capi-types-h.md#oh_ai_priority) | OH\_AI\_Priority | NNRt推理任务优先级。 |
| [OH\_AI\_OptimizationLevel](capi-types-h.md#oh_ai_optimizationlevel) | OH\_AI\_OptimizationLevel | 训练优化等级。 |
| [OH\_AI\_QuantizationType](capi-types-h.md#oh_ai_quantizationtype) | OH\_AI\_QuantizationType | 量化类型信息。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_AI\_ModelType

PhonePC/2in1TabletTVWearable

```
1. enum OH_AI_ModelType
```

**描述**

模型文件的类型。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_AI\_MODELTYPE\_MINDIR = 0 | 模型类型是MindIR，对应的模型文件后缀为.ms。 |
| OH\_AI\_MODELTYPE\_INVALID = 0xFFFFFFFF | 模型类型无效。 |

### OH\_AI\_DeviceType

PhonePC/2in1TabletTVWearable

```
1. enum OH_AI_DeviceType
```

**描述**

设备类型信息，包含了目前支持的设备类型。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_AI\_DEVICETYPE\_CPU = 0 | 设备类型是CPU。 |
| OH\_AI\_DEVICETYPE\_GPU | Device type: GPU。预留选项，暂不支持。 |
| OH\_AI\_DEVICETYPE\_KIRIN\_NPU | 设备类型是麒麟NPU。预留选项，暂不支持。 |
| OH\_AI\_DEVICETYPE\_NNRT = 60 | 设备类型是NNRt。 |
| OH\_AI\_DEVICETYPE\_INVALID = 100 | 设备类型无效。 |

### OH\_AI\_NNRTDeviceType

PhonePC/2in1TabletTVWearable

```
1. enum OH_AI_NNRTDeviceType
```

**描述**

NNRt管理的硬件设备类型。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OH\_AI\_NNRTDEVICE\_OTHERS = 0 | 设备类型不属于以下3种，则属于其它。 |
| OH\_AI\_NNRTDEVICE\_CPU = 1 | CPU设备。 |
| OH\_AI\_NNRTDEVICE\_GPU = 2 | GPU设备。 |
| OH\_AI\_NNRTDEVICE\_ACCELERATOR = 3 | 特定的加速设备。 |

### OH\_AI\_PerformanceMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_AI_PerformanceMode
```

**描述**

NNRt硬件的工作性能模式。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OH\_AI\_PERFORMANCE\_NONE = 0 | 无特殊设置。 |
| OH\_AI\_PERFORMANCE\_LOW = 1 | 低功耗模式。 |
| OH\_AI\_PERFORMANCE\_MEDIUM = 2 | 功耗-性能均衡模式。 |
| OH\_AI\_PERFORMANCE\_HIGH = 3 | 高性能模式。 |
| OH\_AI\_PERFORMANCE\_EXTREME = 4 | 极致性能模式。 |

### OH\_AI\_Priority

PhonePC/2in1TabletTVWearable

```
1. enum OH_AI_Priority
```

**描述**

NNRt推理任务优先级。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OH\_AI\_PRIORITY\_NONE = 0 | 无优先级偏好。 |
| OH\_AI\_PRIORITY\_LOW = 1 | 低优先级任务。 |
| OH\_AI\_PRIORITY\_MEDIUM = 2 | 中优先级任务。 |
| OH\_AI\_PRIORITY\_HIGH = 3 | 高优先级。 |

### OH\_AI\_OptimizationLevel

PhonePC/2in1TabletTVWearable

```
1. enum OH_AI_OptimizationLevel
```

**描述**

训练优化等级。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| OH\_AI\_KO0 = 0 | 无优化等级。 |
| OH\_AI\_KO2 = 2 | 将网络转换为float16，保持批量归一化层和损失函数为float32。 |
| OH\_AI\_KO3 = 3 | 将网络转换为float16，包括批量归一化层。 |
| OH\_AI\_KAUTO = 4 | 根据设备选择优化等级。 |
| OH\_AI\_KOPTIMIZATIONTYPE = 0xFFFFFFFF | 无效优化等级。 |

### OH\_AI\_QuantizationType

PhonePC/2in1TabletTVWearable

```
1. enum OH_AI_QuantizationType
```

**描述**

量化类型信息。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| OH\_AI\_NO\_QUANT = 0 | 不做量化。 |
| OH\_AI\_WEIGHT\_QUANT = 1 | 权重量化。 |
| OH\_AI\_FULL\_QUANT = 2 | 全量化。 |
| OH\_AI\_UNKNOWN\_QUANT\_TYPE = 0xFFFFFFFF | 无效量化类型。 |
