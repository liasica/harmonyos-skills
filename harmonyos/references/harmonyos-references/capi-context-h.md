---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-context-h
title: context.h
breadcrumb: API参考 > AI > MindSpore Lite Kit（昇思推理框架服务） > C API > 头文件 > context.h
category: harmonyos-references
scraped_at: 2026-04-28T08:19:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6666fb7974a763a2637f6565d71d6482a4a8a733c1ab5daa4e2d127aa80f1547
---

## 概述

PhonePC/2in1TabletTVWearable

提供了Context相关的接口，可以配置运行时信息，该接口是非线程安全的。

**引用文件：** <mindspore/context.h>

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
| [OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md) | void\* | MindSpore Lite上下文信息的指针，该指针会指向Context。 |
| [OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md) | void\* | MindSpore Lite运行设备信息的指针。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_AI\_API OH\_AI\_ContextHandle OH\_AI\_ContextCreate()](capi-context-h.md#oh_ai_contextcreate) | 创建一个上下文的对象。注意：此接口需跟OH\_AI\_ContextDestroy配套使用。 |
| [OH\_AI\_API void OH\_AI\_ContextDestroy(OH\_AI\_ContextHandle \*context)](capi-context-h.md#oh_ai_contextdestroy) | 释放上下文对象。 |
| [OH\_AI\_API void OH\_AI\_ContextSetThreadNum(OH\_AI\_ContextHandle context, int32\_t thread\_num)](capi-context-h.md#oh_ai_contextsetthreadnum) | 设置运行时的线程数量。 |
| [OH\_AI\_API int32\_t OH\_AI\_ContextGetThreadNum(const OH\_AI\_ContextHandle context)](capi-context-h.md#oh_ai_contextgetthreadnum) | 获取线程数量。 |
| [OH\_AI\_API void OH\_AI\_ContextSetThreadAffinityMode(OH\_AI\_ContextHandle context, int mode)](capi-context-h.md#oh_ai_contextsetthreadaffinitymode) | 设置运行时线程绑定CPU核心的策略，按照CPU物理核频率分为大、中、小三种类型的核心，并且仅需绑大核或者绑中核，不需要绑小核。 |
| [OH\_AI\_API int OH\_AI\_ContextGetThreadAffinityMode(const OH\_AI\_ContextHandle context)](capi-context-h.md#oh_ai_contextgetthreadaffinitymode) | 获取运行时线程绑定CPU核心的策略。 |
| [OH\_AI\_API void OH\_AI\_ContextSetThreadAffinityCoreList(OH\_AI\_ContextHandle context, const int32\_t \*core\_list,size\_t core\_num)](capi-context-h.md#oh_ai_contextsetthreadaffinitycorelist) | 设置运行时线程绑定CPU核心的列表。  例如：当core\_list=[2,6,8]时，则线程会在CPU的第2，6，8个核心上运行。  如果对于同一个上下文对象，调用了[OH\_AI\_ContextSetThreadAffinityMode](capi-context-h.md#oh_ai_contextsetthreadaffinitymode)和[OH\_AI\_ContextSetThreadAffinityCoreList](capi-context-h.md#oh_ai_contextsetthreadaffinitycorelist)。  这两个函数，则仅[OH\_AI\_ContextSetThreadAffinityCoreList](capi-context-h.md#oh_ai_contextsetthreadaffinitycorelist)的core\_list参数生效，而[OH\_AI\_ContextSetThreadAffinityMode](capi-context-h.md#oh_ai_contextsetthreadaffinitymode)的mode参数不生效。 |
| [OH\_AI\_API const int32\_t \*OH\_AI\_ContextGetThreadAffinityCoreList(const OH\_AI\_ContextHandle context, size\_t \*core\_num)](capi-context-h.md#oh_ai_contextgetthreadaffinitycorelist) | 获取CPU绑核列表。 |
| [OH\_AI\_API void OH\_AI\_ContextSetEnableParallel(OH\_AI\_ContextHandle context, bool is\_parallel)](capi-context-h.md#oh_ai_contextsetenableparallel) | 设置运行时是否支持并行。此接口特性当前未开启，设置无效。 |
| [OH\_AI\_API bool OH\_AI\_ContextGetEnableParallel(const OH\_AI\_ContextHandle context)](capi-context-h.md#oh_ai_contextgetenableparallel) | 获取是否支持算子间并行。 |
| [OH\_AI\_API void OH\_AI\_ContextAddDeviceInfo(OH\_AI\_ContextHandle context, OH\_AI\_DeviceInfoHandle device\_info)](capi-context-h.md#oh_ai_contextadddeviceinfo) | 将一个用户定义的运行设备信息附加到推理上下文中。 |
| [OH\_AI\_API OH\_AI\_DeviceInfoHandle OH\_AI\_DeviceInfoCreate(OH\_AI\_DeviceType device\_type)](capi-context-h.md#oh_ai_deviceinfocreate) | 创建一个设备信息对象。 |
| [OH\_AI\_API void OH\_AI\_DeviceInfoDestroy(OH\_AI\_DeviceInfoHandle \*device\_info)](capi-context-h.md#oh_ai_deviceinfodestroy) | 释放设备信息实例。注意：设备信息实例被添加到context后，无须调用者手动释放。 |
| [OH\_AI\_API void OH\_AI\_DeviceInfoSetProvider(OH\_AI\_DeviceInfoHandle device\_info, const char \*provider)](capi-context-h.md#oh_ai_deviceinfosetprovider) | 设置生产商的名称。 |
| [OH\_AI\_API const char \*OH\_AI\_DeviceInfoGetProvider(const OH\_AI\_DeviceInfoHandle device\_info)](capi-context-h.md#oh_ai_deviceinfogetprovider) | 获取生产商的名称。 |
| [OH\_AI\_API void OH\_AI\_DeviceInfoSetProviderDevice(OH\_AI\_DeviceInfoHandle device\_info, const char \*device)](capi-context-h.md#oh_ai_deviceinfosetproviderdevice) | 设置生产商设备的名称。 |
| [OH\_AI\_API const char \*OH\_AI\_DeviceInfoGetProviderDevice(const OH\_AI\_DeviceInfoHandle device\_info)](capi-context-h.md#oh_ai_deviceinfogetproviderdevice) | 获取生产商设备的名称。 |
| [OH\_AI\_API OH\_AI\_DeviceType OH\_AI\_DeviceInfoGetDeviceType(const OH\_AI\_DeviceInfoHandle device\_info)](capi-context-h.md#oh_ai_deviceinfogetdevicetype) | 获取设备的类型。 |
| [OH\_AI\_API void OH\_AI\_DeviceInfoSetEnableFP16(OH\_AI\_DeviceInfoHandle device\_info, bool is\_fp16)](capi-context-h.md#oh_ai_deviceinfosetenablefp16) | 设置是否开启float16推理模式，仅CPU/GPU设备可用。 |
| [OH\_AI\_API bool OH\_AI\_DeviceInfoGetEnableFP16(const OH\_AI\_DeviceInfoHandle device\_info)](capi-context-h.md#oh_ai_deviceinfogetenablefp16) | 获取是否开启float16推理模式，仅CPU/GPU设备可用。 |
| [OH\_AI\_API void OH\_AI\_DeviceInfoSetFrequency(OH\_AI\_DeviceInfoHandle device\_info, int frequency)](capi-context-h.md#oh_ai_deviceinfosetfrequency) | 设置NPU的频率，仅NPU设备可用。 |
| [OH\_AI\_API int OH\_AI\_DeviceInfoGetFrequency(const OH\_AI\_DeviceInfoHandle device\_info)](capi-context-h.md#oh_ai_deviceinfogetfrequency) | 获取NPU的频率类型，仅NPU设备可用。 |
| [OH\_AI\_API NNRTDeviceDesc \*OH\_AI\_GetAllNNRTDeviceDescs(size\_t \*num)](capi-context-h.md#oh_ai_getallnnrtdevicedescs) | 获取系统中所有NNRt硬件设备的描述信息。 |
| [OH\_AI\_API NNRTDeviceDesc \*OH\_AI\_GetElementOfNNRTDeviceDescs(NNRTDeviceDesc \*descs, size\_t index)](capi-context-h.md#oh_ai_getelementofnnrtdevicedescs) | 获取NNRt设备描述信息数组中的元素指针。 |
| [OH\_AI\_API void OH\_AI\_DestroyAllNNRTDeviceDescs(NNRTDeviceDesc \*\*desc)](capi-context-h.md#oh_ai_destroyallnnrtdevicedescs) | 销毁从[OH\_AI\_GetAllNNRTDeviceDescs](capi-context-h.md#oh_ai_getallnnrtdevicedescs)获取的NNRt描述信息实例数组。 |
| [OH\_AI\_API size\_t OH\_AI\_GetDeviceIdFromNNRTDeviceDesc(const NNRTDeviceDesc \*desc)](capi-context-h.md#oh_ai_getdeviceidfromnnrtdevicedesc) | 从特定的NNRt设备描述信息实例获取NNRt设备ID。注意，此ID只对NNRt有效。 |
| [OH\_AI\_API const char \*OH\_AI\_GetNameFromNNRTDeviceDesc(const NNRTDeviceDesc \*desc)](capi-context-h.md#oh_ai_getnamefromnnrtdevicedesc) | 从特定的NNRt设备描述信息实例获取NNRt设备名称。 |
| [OH\_AI\_API OH\_AI\_NNRTDeviceType OH\_AI\_GetTypeFromNNRTDeviceDesc(const NNRTDeviceDesc \*desc)](capi-context-h.md#oh_ai_gettypefromnnrtdevicedesc) | 从特定的NNRt设备描述信息实例获取NNRt设备类型。 |
| [OH\_AI\_API OH\_AI\_DeviceInfoHandle OH\_AI\_CreateNNRTDeviceInfoByName(const char \*name)](capi-context-h.md#oh_ai_creatennrtdeviceinfobyname) | 查找指定名称的NNRt设备，根据找到的第一个设备信息，创建NNRt设备信息。 |
| [OH\_AI\_API OH\_AI\_DeviceInfoHandle OH\_AI\_CreateNNRTDeviceInfoByType(OH\_AI\_NNRTDeviceType type)](capi-context-h.md#oh_ai_creatennrtdeviceinfobytype) | 查找指定类型的NNRt设备，根据找到的第一个设备信息，创建NNRt设备信息。 |
| [OH\_AI\_API void OH\_AI\_DeviceInfoSetDeviceId(OH\_AI\_DeviceInfoHandle device\_info, size\_t device\_id)](capi-context-h.md#oh_ai_deviceinfosetdeviceid) | 设置NNRt设备ID，仅NNRt设备可用。 |
| [OH\_AI\_API size\_t OH\_AI\_DeviceInfoGetDeviceId(const OH\_AI\_DeviceInfoHandle device\_info)](capi-context-h.md#oh_ai_deviceinfogetdeviceid) | 获取NNRt设备ID，仅NNRt设备可用。 |
| [OH\_AI\_API void OH\_AI\_DeviceInfoSetPerformanceMode(OH\_AI\_DeviceInfoHandle device\_info, OH\_AI\_PerformanceMode mode)](capi-context-h.md#oh_ai_deviceinfosetperformancemode) | 设置NNRt性能模式，仅NNRt设备可用。 |
| [OH\_AI\_API OH\_AI\_PerformanceMode OH\_AI\_DeviceInfoGetPerformanceMode(const OH\_AI\_DeviceInfoHandle device\_info)](capi-context-h.md#oh_ai_deviceinfogetperformancemode) | 获取NNRt性能模式，仅NNRt设备可用。 |
| [OH\_AI\_API void OH\_AI\_DeviceInfoSetPriority(OH\_AI\_DeviceInfoHandle device\_info, OH\_AI\_Priority priority)](capi-context-h.md#oh_ai_deviceinfosetpriority) | 设置NNRt任务优先级，仅NNRt设备可用。 |
| [OH\_AI\_API OH\_AI\_Priority OH\_AI\_DeviceInfoGetPriority(const OH\_AI\_DeviceInfoHandle device\_info)](capi-context-h.md#oh_ai_deviceinfogetpriority) | 获取NNRt任务优先级，仅NNRt设备可用。 |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_DeviceInfoAddExtension(OH\_AI\_DeviceInfoHandle device\_info, const char \*name,const char \*value, size\_t value\_size)](capi-context-h.md#oh_ai_deviceinfoaddextension) | 向设备信息中添加键/值对形式的扩展配置。只对NNRt设备信息有效。  当前仅支持配置以下11种键：{"CachePath": "YourCachePath"}，{"CacheVersion": "YourCacheVersion"}，  {"QuantBuffer": "YourQuantBuffer"}，{"ModelName": "YourModelName"}，  {"isProfiling": "YourProfilingSwitch"}，{"opLayout": "YourOpLayout"}，  {"InputDims": "YourInputDims"}，{"DynamicDims": "YourDynamicDims"}，  {"QuantConfigData": "YourQuantConfigData"}，{"BandMode": "YourBandMode"}，  {"NPU\_FM\_SHARED": "YourNPU\_FM\_SHARED"}，用户可根据使用情况配置各个键对应的值。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AI\_ContextCreate()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_ContextHandle OH_AI_ContextCreate()
```

**描述**

创建一个上下文的对象。注意：此接口需跟OH\_AI\_ContextDestroy配套使用。

**起始版本：** 9

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md) | 指向上下文信息的[OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)。 |

### OH\_AI\_ContextDestroy()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_ContextDestroy(OH_AI_ContextHandle *context)
```

**描述**

释放上下文对象。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md) \*context | 指向[OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)的二级指针，上下文销毁后会对context置为空指针。 |

### OH\_AI\_ContextSetThreadNum()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_ContextSetThreadNum(OH_AI_ContextHandle context, int32_t thread_num)
```

**描述**

设置运行时的线程数量。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md) context | 指向上下文信息实例的[OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)。 |
| int32\_t thread\_num | 运行时的线程数量。长度跟随系统限制。 |

### OH\_AI\_ContextGetThreadNum()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API int32_t OH_AI_ContextGetThreadNum(const OH_AI_ContextHandle context)
```

**描述**

获取线程数量。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md) context | 指向上下文信息实例的[OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API int32\_t | 当前的线程数量。 |

### OH\_AI\_ContextSetThreadAffinityMode()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_ContextSetThreadAffinityMode(OH_AI_ContextHandle context, int mode)
```

**描述**

设置运行时线程绑定CPU核心的策略，按照CPU物理核频率分为大、中、小三种类型的核心，并且仅需绑大核或者绑中核，不需要绑小核。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md) context | 指向上下文信息实例的[OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)。 |
| int mode | 绑核策略。一共有三种策略，0为不绑核，1为大核优先，2为中核优先。 |

### OH\_AI\_ContextGetThreadAffinityMode()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API int OH_AI_ContextGetThreadAffinityMode(const OH_AI_ContextHandle context)
```

**描述**

获取运行时线程绑定CPU核心的策略。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md) context | 指向上下文信息实例的[OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API int | 绑核策略。一共有三种策略，0为不绑核，1为大核优先，2为中核优先。 |

### OH\_AI\_ContextSetThreadAffinityCoreList()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_ContextSetThreadAffinityCoreList(OH_AI_ContextHandle context, const int32_t *core_list,size_t core_num)
```

**描述**

设置运行时线程绑定CPU核心的列表。

例如：当core\_list=[2,6,8]时，则线程会在CPU的第2，6，8个核心上运行。

如果对于同一个上下文对象，调用了[OH\_AI\_ContextSetThreadAffinityMode](capi-context-h.md#oh_ai_contextsetthreadaffinitymode)和[OH\_AI\_ContextSetThreadAffinityCoreList](capi-context-h.md#oh_ai_contextsetthreadaffinitycorelist)。

这两个函数，则仅[OH\_AI\_ContextSetThreadAffinityCoreList](capi-context-h.md#oh_ai_contextsetthreadaffinitycorelist)的core\_list参数生效，而[OH\_AI\_ContextSetThreadAffinityMode](capi-context-h.md#oh_ai_contextsetthreadaffinitymode)的mode参数不生效。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md) context | 指向上下文信息实例的[OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)。 |
| const int32\_t \*core\_list | CPU绑核的列表。 |
| size\_t core\_num | 核的数量，它就代表core\_list的长度。 |

### OH\_AI\_ContextGetThreadAffinityCoreList()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API const int32_t *OH_AI_ContextGetThreadAffinityCoreList(const OH_AI_ContextHandle context, size_t *core_num)
```

**描述**

获取CPU绑核列表。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md) context | 指向上下文信息实例的[OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)。 |
| size\_t \*core\_num | 该参数是输出参数，表示核的数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API const int32\_t \* | CPU绑核列表。此列表对象由[OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)管理，调用者无须手动释放。 |

### OH\_AI\_ContextSetEnableParallel()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_ContextSetEnableParallel(OH_AI_ContextHandle context, bool is_parallel)
```

**描述**

设置运行时是否支持并行。此接口特性当前未开启，设置无效。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md) context | 指向上下文信息实例的[OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)。 |
| bool is\_parallel | 是否支持并行。true为支持并行，false为不支持并行。 |

### OH\_AI\_ContextGetEnableParallel()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API bool OH_AI_ContextGetEnableParallel(const OH_AI_ContextHandle context)
```

**描述**

获取是否支持算子间并行。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md) context | 指向上下文信息实例的[OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API bool | 是否支持并行。true为支持并行，false为不支持并行。 |

### OH\_AI\_ContextAddDeviceInfo()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_ContextAddDeviceInfo(OH_AI_ContextHandle context, OH_AI_DeviceInfoHandle device_info)
```

**描述**

将一个用户定义的运行设备信息附加到推理上下文中。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md) context | 指向上下文信息实例的[OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)。 |
| [OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md) device\_info | 指向设备信息实例的[OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md)。 |

### OH\_AI\_DeviceInfoCreate()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_DeviceInfoHandle OH_AI_DeviceInfoCreate(OH_AI_DeviceType device_type)
```

**描述**

创建一个设备信息对象。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_DeviceType](capi-types-h.md#oh_ai_devicetype) device\_type | 设备类型，具体见[OH\_AI\_DeviceType](capi-types-h.md#oh_ai_devicetype)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md) | 指向设备信息实例的[OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md)。 |

### OH\_AI\_DeviceInfoDestroy()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_DeviceInfoDestroy(OH_AI_DeviceInfoHandle *device_info)
```

**描述**

释放设备信息实例。注意：设备信息实例被添加到context后，无须调用者手动释放。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md) \*device\_info | 指向设备信息实例的[OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md)。 |

### OH\_AI\_DeviceInfoSetProvider()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_DeviceInfoSetProvider(OH_AI_DeviceInfoHandle device_info, const char *provider)
```

**描述**

设置生产商的名称。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md) device\_info | 指向设备信息实例的[OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md)。 |
| const char \*provider | 生产商的名称。字符串长度跟随系统限制。 |

### OH\_AI\_DeviceInfoGetProvider()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API const char *OH_AI_DeviceInfoGetProvider(const OH_AI_DeviceInfoHandle device_info)
```

**描述**

获取生产商的名称。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md) device\_info | 指向设备信息实例的[OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API const char \* | 生产商的名称。 |

### OH\_AI\_DeviceInfoSetProviderDevice()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_DeviceInfoSetProviderDevice(OH_AI_DeviceInfoHandle device_info, const char *device)
```

**描述**

设置生产商设备的名称。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md) device\_info | 指向设备信息实例的[OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md)。 |
| const char \*device | 生产商设备名称。例如: CPU。字符串长度跟随系统限制。 |

### OH\_AI\_DeviceInfoGetProviderDevice()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API const char *OH_AI_DeviceInfoGetProviderDevice(const OH_AI_DeviceInfoHandle device_info)
```

**描述**

获取生产商设备的名称。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md) device\_info | 指向设备信息实例的[OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API const char \* | 生产商设备的名称。 |

### OH\_AI\_DeviceInfoGetDeviceType()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_DeviceType OH_AI_DeviceInfoGetDeviceType(const OH_AI_DeviceInfoHandle device_info)
```

**描述**

获取设备的类型。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md) device\_info | 指向设备信息实例的[OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_DeviceType](capi-types-h.md#oh_ai_devicetype) | 生产商设备类型。 |

### OH\_AI\_DeviceInfoSetEnableFP16()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_DeviceInfoSetEnableFP16(OH_AI_DeviceInfoHandle device_info, bool is_fp16)
```

**描述**

设置是否开启float16推理模式，仅CPU/GPU设备可用。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md) device\_info | 指向设备信息实例的[OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md)。 |
| bool is\_fp16 | 是否开启float16推理模式。true为开启float16推理模式，false为不开启float16推理模式。 |

### OH\_AI\_DeviceInfoGetEnableFP16()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API bool OH_AI_DeviceInfoGetEnableFP16(const OH_AI_DeviceInfoHandle device_info)
```

**描述**

获取是否开启float16推理模式，仅CPU/GPU设备可用。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md) device\_info | 指向设备信息实例的[OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API bool | 是否开启float16推理模式。true为开启float16推理模式，false为不开启float16推理模式。 |

### OH\_AI\_DeviceInfoSetFrequency()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_DeviceInfoSetFrequency(OH_AI_DeviceInfoHandle device_info, int frequency)
```

**描述**

设置NPU的频率，仅NPU设备可用。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md) device\_info | 指向设备信息实例的[OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md)。 |
| int frequency | 频率类型，取值范围为0-4，默认是3。0表示不设置，由系统调节；1表示低功耗；2表示平衡；3表示高性能；4表示超高性能。 |

### OH\_AI\_DeviceInfoGetFrequency()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API int OH_AI_DeviceInfoGetFrequency(const OH_AI_DeviceInfoHandle device_info)
```

**描述**

获取NPU的频率类型，仅NPU设备可用。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md) device\_info | 指向设备信息实例的[OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API int | NPU的频率类型。取值范围为0-4，0表示不设置，由系统调节；1表示低功耗；2表示平衡；3表示高性能；4表示超高性能。 |

### OH\_AI\_GetAllNNRTDeviceDescs()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API NNRTDeviceDesc *OH_AI_GetAllNNRTDeviceDescs(size_t *num)
```

**描述**

获取系统中所有NNRt硬件设备的描述信息。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| size\_t \*num | 输出参数，返回设备数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [NNRTDeviceDesc](capi-mindspore-nnrtdevicedesc.md) \* | 指向NNRt设备描述信息实例数组的指针。当获取失败时，返回NULL。 |

### OH\_AI\_GetElementOfNNRTDeviceDescs()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API NNRTDeviceDesc *OH_AI_GetElementOfNNRTDeviceDescs(NNRTDeviceDesc *descs, size_t index)
```

**描述**

获取NNRt设备描述信息数组中的元素指针。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [NNRTDeviceDesc](capi-mindspore-nnrtdevicedesc.md) \*descs | NNRt设备描述信息数组。 |
| size\_t index | 数组元素索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [NNRTDeviceDesc](capi-mindspore-nnrtdevicedesc.md) \* | NNRt设备描述信息类型指针。 |

### OH\_AI\_DestroyAllNNRTDeviceDescs()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_DestroyAllNNRTDeviceDescs(NNRTDeviceDesc **desc)
```

**描述**

销毁从[OH\_AI\_GetAllNNRTDeviceDescs](capi-context-h.md#oh_ai_getallnnrtdevicedescs)获取的NNRt描述信息实例数组。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [NNRTDeviceDesc](capi-mindspore-nnrtdevicedesc.md) \*\*desc | 指向NNRt设备描述信息实例数组的二重指针。销毁结束，desc指向内容会被置为NULL。 |

### OH\_AI\_GetDeviceIdFromNNRTDeviceDesc()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API size_t OH_AI_GetDeviceIdFromNNRTDeviceDesc(const NNRTDeviceDesc *desc)
```

**描述**

从特定的NNRt设备描述信息实例获取NNRt设备ID。注意，此ID只对NNRt有效。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [NNRTDeviceDesc](capi-mindspore-nnrtdevicedesc.md) \*desc | 指向NNRt设备描述信息实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API size\_t | NNRt设备ID。 |

### OH\_AI\_GetNameFromNNRTDeviceDesc()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API const char *OH_AI_GetNameFromNNRTDeviceDesc(const NNRTDeviceDesc *desc)
```

**描述**

从特定的NNRt设备描述信息实例获取NNRt设备名称。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [NNRTDeviceDesc](capi-mindspore-nnrtdevicedesc.md) \*desc | 指向NNRt设备描述信息实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API const char \* | NNRt设备名称，指向一个常量字符串的指针，该常量字符串由desc持有，调用者无需单独释放此指针。 |

### OH\_AI\_GetTypeFromNNRTDeviceDesc()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_NNRTDeviceType OH_AI_GetTypeFromNNRTDeviceDesc(const NNRTDeviceDesc *desc)
```

**描述**

从特定的NNRt设备描述信息实例获取NNRt设备类型。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [NNRTDeviceDesc](capi-mindspore-nnrtdevicedesc.md) \*desc | 指向NNRt设备描述信息实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_NNRTDeviceType](capi-types-h.md#oh_ai_nnrtdevicetype) | [OH\_AI\_NNRTDeviceType](capi-types-h.md#oh_ai_nnrtdevicetype) NNRt设备类型。 |

### OH\_AI\_CreateNNRTDeviceInfoByName()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_DeviceInfoHandle OH_AI_CreateNNRTDeviceInfoByName(const char *name)
```

**描述**

查找指定名称的NNRt设备，根据找到的第一个设备信息，创建NNRt设备信息。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*name | 目标NNRt设备名。字符串长度跟随系统限制。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md) | 指向设备信息实例的[OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md)。 |

### OH\_AI\_CreateNNRTDeviceInfoByType()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_DeviceInfoHandle OH_AI_CreateNNRTDeviceInfoByType(OH_AI_NNRTDeviceType type)
```

**描述**

查找指定类型的NNRt设备，根据找到的第一个设备信息，创建NNRt设备信息。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_NNRTDeviceType](capi-types-h.md#oh_ai_nnrtdevicetype) type | [OH\_AI\_NNRTDeviceType](capi-types-h.md#oh_ai_nnrtdevicetype) 目标NNRt设备类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md) | 指向设备信息实例的[OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md)。 |

### OH\_AI\_DeviceInfoSetDeviceId()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_DeviceInfoSetDeviceId(OH_AI_DeviceInfoHandle device_info, size_t device_id)
```

**描述**

设置NNRt设备ID，仅NNRt设备可用。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md) device\_info | 指向设备信息实例的[OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md)。 |
| size\_t device\_id | NNRt设备ID。 |

### OH\_AI\_DeviceInfoGetDeviceId()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API size_t OH_AI_DeviceInfoGetDeviceId(const OH_AI_DeviceInfoHandle device_info)
```

**描述**

获取NNRt设备ID，仅NNRt设备可用。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md) device\_info | 指向设备信息实例的[OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API size\_t | NNRt设备ID。 |

### OH\_AI\_DeviceInfoSetPerformanceMode()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_DeviceInfoSetPerformanceMode(OH_AI_DeviceInfoHandle device_info, OH_AI_PerformanceMode mode)
```

**描述**

设置NNRt性能模式，仅NNRt设备可用。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md) device\_info | 指向设备信息实例的[OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md)。 |
| [OH\_AI\_PerformanceMode](capi-types-h.md#oh_ai_performancemode) mode | [OH\_AI\_PerformanceMode](capi-types-h.md#oh_ai_performancemode) NNRt性能模式。 |

### OH\_AI\_DeviceInfoGetPerformanceMode()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_PerformanceMode OH_AI_DeviceInfoGetPerformanceMode(const OH_AI_DeviceInfoHandle device_info)
```

**描述**

获取NNRt性能模式，仅NNRt设备可用。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md) device\_info | 指向设备信息实例的[OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_PerformanceMode](capi-types-h.md#oh_ai_performancemode) | [OH\_AI\_PerformanceMode](capi-types-h.md#oh_ai_performancemode) NNRt性能模式。 |

### OH\_AI\_DeviceInfoSetPriority()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_DeviceInfoSetPriority(OH_AI_DeviceInfoHandle device_info, OH_AI_Priority priority)
```

**描述**

设置NNRt任务优先级，仅NNRt设备可用。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md) device\_info | 指向设备信息实例的[OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md)。 |
| [OH\_AI\_Priority](capi-types-h.md#oh_ai_priority) priority | [OH\_AI\_Priority](capi-types-h.md#oh_ai_priority) NNRt任务优先级。 |

### OH\_AI\_DeviceInfoGetPriority()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_Priority OH_AI_DeviceInfoGetPriority(const OH_AI_DeviceInfoHandle device_info)
```

**描述**

获取NNRt任务优先级，仅NNRt设备可用。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md) device\_info | 指向设备信息实例的[OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_Priority](capi-types-h.md#oh_ai_priority) | [OH\_AI\_Priority](capi-types-h.md#oh_ai_priority) NNRt任务优先级。 |

### OH\_AI\_DeviceInfoAddExtension()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_Status OH_AI_DeviceInfoAddExtension(OH_AI_DeviceInfoHandle device_info, const char *name,const char *value, size_t value_size)
```

**描述**

向设备信息中添加键/值对形式的扩展配置。只对NNRt设备信息有效。

当前仅支持配置以下11种键：{"CachePath": "YourCachePath"}，{"CacheVersion": "YourCacheVersion"}，

{"QuantBuffer": "YourQuantBuffer"}，{"ModelName": "YourModelName"}，

{"isProfiling": "YourProfilingSwitch"}，{"opLayout": "YourOpLayout"}，

{"InputDims": "YourInputDims"}，{"DynamicDims": "YourDynamicDims"}，

{"QuantConfigData": "YourQuantConfigData"}，{"BandMode": "YourBandMode"}，

{"NPU\_FM\_SHARED": "YourNPU\_FM\_SHARED"}，用户可根据使用情况配置各个键对应的值。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md) device\_info | 指向设备信息实例的[OH\_AI\_DeviceInfoHandle](capi-mindspore-oh-ai-deviceinfohandle.md)。 |
| const char \*name | 单个扩展项的键，格式为C字符串。字符串长度限制为128。 |
| const char \*value | 单个扩展项的值内容首地址。字符串长度跟随系统限制。 |
| size\_t value\_size | 单个扩展项的值内容长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_Status](capi-status-h.md#oh_ai_status) | [OH\_AI\_Status](capi-status-h.md#oh_ai_status) 执行状态码，若成功返回OH\_AI\_STATUS\_SUCCESS，失败则返回具体错误码。 |
