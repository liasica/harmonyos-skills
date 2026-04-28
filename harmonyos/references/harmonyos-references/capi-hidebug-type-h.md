---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-type-h
title: hidebug_type.h
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 头文件 > hidebug_type.h
category: harmonyos-references
scraped_at: 2026-04-28T08:11:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:129b864425ec96de267f91508963f4b796170b493ba817a29eb166026ca62a74
---

## 概述

PhonePC/2in1TabletTVWearable

HiDebug模块代码结构体定义。

**引用文件：** <hidebug/hidebug\_type.h>

**库：** libohhidebug.so

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 12

**相关模块：** [HiDebug](capi-hidebug.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [HiDebug\_ThreadCpuUsage](capi-hidebug-hidebug-threadcpuusage.md) | HiDebug\_ThreadCpuUsage | 应用程序所有线程的CPU使用率结构体定义。 |
| [HiDebug\_SystemMemInfo](capi-hidebug-hidebug-systemmeminfo.md) | HiDebug\_SystemMemInfo | 系统内存信息结构类型定义。 |
| [HiDebug\_NativeMemInfo](capi-hidebug-hidebug-nativememinfo.md) | HiDebug\_NativeMemInfo | 应用程序进程本机内存信息结构类型定义。 |
| [HiDebug\_MemoryLimit](capi-hidebug-hidebug-memorylimit.md) | HiDebug\_MemoryLimit | 应用程序进程内存限制结构类型定义。 |
| [HiDebug\_JsStackFrame](capi-hidebug-hidebug-jsstackframe.md) | HiDebug\_JsStackFrame | js栈帧内容的定义。 |
| [HiDebug\_NativeStackFrame](capi-hidebug-hidebug-nativestackframe.md) | HiDebug\_NativeStackFrame | native栈帧内容的定义。 |
| [HiDebug\_StackFrame](capi-hidebug-hidebug-stackframe.md) | HiDebug\_StackFrame | 栈帧内容的定义。 |
| [HiDebug\_MallocDispatch](capi-hidebug-hidebug-mallocdispatch.md) | HiDebug\_MallocDispatch | 应用程序进程可替换/恢复的HiDebug\_MallocDispatch表结构类型定义。 |
| [HiDebug\_GraphicsMemorySummary](capi-hidebug-hidebug-graphicsmemorysummary.md) | HiDebug\_GraphicsMemorySummary | 应用图形显存占用详情的结构定义。 |
| [HiDebug\_ProcessSamplerConfig](capi-hidebug-hidebug-processsamplerconfig.md) | HiDebug\_ProcessSamplerConfig | 采样配置的结构定义。 |
| [HiDebug\_Backtrace\_Object\_\_\*](capi-hidebug-hidebug-backtrace-object--8h.md) | HiDebug\_Backtrace\_Object | 用于栈回溯及栈解析的对象。 |
| [HiDebug\_ThreadCpuUsage\*](capi-hidebug-hidebug-threadcpuusage.md) | HiDebug\_ThreadCpuUsagePtr | HiDebug\_ThreadCpuUsage指针定义。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [HiDebug\_ErrorCode](capi-hidebug-type-h.md#hidebug_errorcode) | HiDebug\_ErrorCode | 错误码定义。 |
| [HiDebug\_TraceFlag](capi-hidebug-type-h.md#hidebug_traceflag) | HiDebug\_TraceFlag | 采集trace线程的类型。 |
| [HiDebug\_StackFrameType](capi-hidebug-type-h.md#hidebug_stackframetype) | HiDebug\_StackFrameType | 栈帧类型的枚举值定义。 |
| [HiDebug\_CrashObjType](capi-hidebug-type-h.md#hidebug_crashobjtype) | HiDebug\_CrashObjType | 维测信息数据类型的枚举。 |

### 宏定义

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [HIDEBUG\_TRACE\_TAG\_FFRT](capi-hidebug-type-h.md#hidebug_trace_tag_ffrt) (1ULL << 13) | FFRT任务标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_COMMON\_LIBRARY](capi-hidebug-type-h.md#hidebug_trace_tag_common_library) (1ULL << 16) | 公共库子系统标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_HDF](capi-hidebug-type-h.md#hidebug_trace_tag_hdf) (1ULL << 18) | HDF子系统标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_NET](capi-hidebug-type-h.md#hidebug_trace_tag_net) (1ULL << 23) | 网络标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_NWEB](capi-hidebug-type-h.md#hidebug_trace_tag_nweb) (1ULL << 24) | NWeb标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_AUDIO](capi-hidebug-type-h.md#hidebug_trace_tag_distributed_audio) (1ULL << 27) | 分布式音频标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_FILE\_MANAGEMENT](capi-hidebug-type-h.md#hidebug_trace_tag_file_management) (1ULL << 29) | 文件管理标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_OHOS](capi-hidebug-type-h.md#hidebug_trace_tag_ohos) (1ULL << 30) | OHOS通用标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_ABILITY\_MANAGER](capi-hidebug-type-h.md#hidebug_trace_tag_ability_manager) (1ULL << 31) | Ability Manager标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_CAMERA](capi-hidebug-type-h.md#hidebug_trace_tag_camera) (1ULL << 32) | 相机模块标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_MEDIA](capi-hidebug-type-h.md#hidebug_trace_tag_media) (1ULL << 33) | 媒体模块标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_IMAGE](capi-hidebug-type-h.md#hidebug_trace_tag_image) (1ULL << 34) | 图像模块标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_AUDIO](capi-hidebug-type-h.md#hidebug_trace_tag_audio) (1ULL << 35) | 音频模块标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_DATA](capi-hidebug-type-h.md#hidebug_trace_tag_distributed_data) (1ULL << 36) | 分布式数据管理器模块标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_GRAPHICS](capi-hidebug-type-h.md#hidebug_trace_tag_graphics) (1ULL << 38) | 图形模块标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_ARKUI](capi-hidebug-type-h.md#hidebug_trace_tag_arkui) (1ULL << 39) | ArkUI开发框架标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_NOTIFICATION](capi-hidebug-type-h.md#hidebug_trace_tag_notification) (1ULL << 40) | 通知模块标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_MISC](capi-hidebug-type-h.md#hidebug_trace_tag_misc) (1ULL << 41) | MISC模块标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_MULTIMODAL\_INPUT](capi-hidebug-type-h.md#hidebug_trace_tag_multimodal_input) (1ULL << 42) | 多模态输入模块标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_RPC](capi-hidebug-type-h.md#hidebug_trace_tag_rpc) (1ULL << 46) | RPC标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_ARK](capi-hidebug-type-h.md#hidebug_trace_tag_ark) (1ULL << 47) | JSVM虚拟机标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_WINDOW\_MANAGER](capi-hidebug-type-h.md#hidebug_trace_tag_window_manager) (1ULL << 48) | 窗口管理器标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_SCREEN](capi-hidebug-type-h.md#hidebug_trace_tag_distributed_screen) (1ULL << 50) | 分布式屏幕标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_CAMERA](capi-hidebug-type-h.md#hidebug_trace_tag_distributed_camera) (1ULL << 51) | 分布式相机标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_HARDWARE\_FRAMEWORK](capi-hidebug-type-h.md#hidebug_trace_tag_distributed_hardware_framework) (1ULL << 52) | 分布式硬件框架标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_GLOBAL\_RESOURCE\_MANAGER](capi-hidebug-type-h.md#hidebug_trace_tag_global_resource_manager) (1ULL << 53) | 全局资源管理器标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_HARDWARE\_DEVICE\_MANAGER](capi-hidebug-type-h.md#hidebug_trace_tag_distributed_hardware_device_manager) (1ULL << 54) | 分布式硬件设备管理器标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_SAMGR](capi-hidebug-type-h.md#hidebug_trace_tag_samgr) (1ULL << 55) | SA标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_POWER\_MANAGER](capi-hidebug-type-h.md#hidebug_trace_tag_power_manager) (1ULL << 56) | 电源管理器标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_SCHEDULER](capi-hidebug-type-h.md#hidebug_trace_tag_distributed_scheduler) (1ULL << 57) | 分布式调度程序标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_INPUT](capi-hidebug-type-h.md#hidebug_trace_tag_distributed_input) (1ULL << 59) | 分布式输入标签。  **起始版本：** 12 |
| [HIDEBUG\_TRACE\_TAG\_BLUETOOTH](capi-hidebug-type-h.md#hidebug_trace_tag_bluetooth) (1ULL << 60) | 蓝牙标签。  **起始版本：** 12 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### HiDebug\_ErrorCode

PhonePC/2in1TabletTVWearable

```
1. enum HiDebug_ErrorCode
```

**描述**

错误码定义。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| HIDEBUG\_SUCCESS = 0 | 成功。 |
| HIDEBUG\_INVALID\_ARGUMENT = 401 | 无效参数，可能的原因： 1.参数传值问题；2.参数类型问题。 |
| HIDEBUG\_TRACE\_CAPTURED\_ALREADY = 11400102 | 重复采集。 |
| HIDEBUG\_NO\_PERMISSION = 11400103 | 没有写文件的权限。 |
| HIDEBUG\_TRACE\_ABNORMAL = 11400104 | 系统内部错误。 |
| HIDEBUG\_NO\_TRACE\_RUNNING = 11400105 | 当前没有trace正在运行。 |
| HIDEBUG\_INVALID\_SYMBOLIC\_PC\_ADDRESS = 11400200 | 传入符号解析函数的pc地址是无效的。  **起始版本：** 20。 |
| HIDEBUG\_NOT\_SUPPORTED = 11400300 | 当前设备不支持。  **起始版本：** 22 |
| HIDEBUG\_UNDER\_SAMPLING = 11400301 | 当前进程正在采样。  **起始版本：** 22 |
| HIDEBUG\_RESOURCE\_UNAVAILABLE = 11400302 | 采样资源不可用。  **起始版本：** 22 |

### HiDebug\_TraceFlag

PhonePC/2in1TabletTVWearable

```
1. enum HiDebug_TraceFlag
```

**描述**

采集trace线程的类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| HIDEBUG\_TRACE\_FLAG\_MAIN\_THREAD = 1 | 只采集当前应用主线程。 |
| HIDEBUG\_TRACE\_FLAG\_ALL\_THREADS = 2 | 采集当前应用下所有线程。 |

### HiDebug\_StackFrameType

PhonePC/2in1TabletTVWearable

```
1. enum HiDebug_StackFrameType
```

**描述**

栈帧类型的枚举值定义。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| HIDEBUG\_STACK\_FRAME\_TYPE\_JS = 1 | js类型栈帧。 |
| HIDEBUG\_STACK\_FRAME\_TYPE\_NATIVE = 2 | native类型栈帧。 |

### HiDebug\_CrashObjType

PhonePC/2in1TabletTVWearable

```
1. enum HiDebug_CrashObjType
```

**描述**

维测信息数据类型的枚举。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| HIDEBUG\_CRASHOBJ\_STRING = 0 | 字符串 |
| HIDEBUG\_CRASHOBJ\_MEMORY\_64B = 1 | 64字节内存块 |
| HIDEBUG\_CRASHOBJ\_MEMORY\_256B = 2 | 256字节内存块 |
| HIDEBUG\_CRASHOBJ\_MEMORY\_1024B = 3 | 1024字节内存块 |
| HIDEBUG\_CRASHOBJ\_MEMORY\_2048B = 4 | 2048字节内存块 |
| HIDEBUG\_CRASHOBJ\_MEMORY\_4096B = 5 | 4096字节内存块 |

## 宏定义说明

PhonePC/2in1TabletTVWearable

### HIDEBUG\_TRACE\_TAG\_FFRT

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_FFRT (1ULL << 13)
```

**描述**

FFRT任务标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_COMMON\_LIBRARY

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_COMMON_LIBRARY (1ULL << 16)
```

**描述**

公共库子系统标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_HDF

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_HDF (1ULL << 18)
```

**描述**

HDF子系统标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_NET

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_NET (1ULL << 23)
```

**描述**

网络标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_NWEB

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_NWEB (1ULL << 24)
```

**描述**

NWeb标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_AUDIO

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_DISTRIBUTED_AUDIO (1ULL << 27)
```

**描述**

分布式音频标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_FILE\_MANAGEMENT

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_FILE_MANAGEMENT (1ULL << 29)
```

**描述**

文件管理标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_OHOS

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_OHOS (1ULL << 30)
```

**描述**

OHOS通用标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_ABILITY\_MANAGER

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_ABILITY_MANAGER (1ULL << 31)
```

**描述**

Ability Manager标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_CAMERA

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_CAMERA (1ULL << 32)
```

**描述**

相机模块标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_MEDIA

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_MEDIA (1ULL << 33)
```

**描述**

媒体模块标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_IMAGE

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_IMAGE (1ULL << 34)
```

**描述**

图像模块标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_AUDIO

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_AUDIO (1ULL << 35)
```

**描述**

音频模块标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_DATA

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_DISTRIBUTED_DATA (1ULL << 36)
```

**描述**

分布式数据管理器模块标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_GRAPHICS

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_GRAPHICS (1ULL << 38)
```

**描述**

图形模块标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_ARKUI

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_ARKUI (1ULL << 39)
```

**描述**

ArkUI开发框架标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_NOTIFICATION

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_NOTIFICATION (1ULL << 40)
```

**描述**

通知模块标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_MISC

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_MISC (1ULL << 41)
```

**描述**

MISC模块标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_MULTIMODAL\_INPUT

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_MULTIMODAL_INPUT (1ULL << 42)
```

**描述**

多模态输入模块标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_RPC

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_RPC (1ULL << 46)
```

**描述**

RPC标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_ARK

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_ARK (1ULL << 47)
```

**描述**

JSVM虚拟机标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_WINDOW\_MANAGER

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_WINDOW_MANAGER (1ULL << 48)
```

**描述**

窗口管理器标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_SCREEN

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_DISTRIBUTED_SCREEN (1ULL << 50)
```

**描述**

分布式屏幕标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_CAMERA

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_DISTRIBUTED_CAMERA (1ULL << 51)
```

**描述**

分布式相机标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_HARDWARE\_FRAMEWORK

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_DISTRIBUTED_HARDWARE_FRAMEWORK (1ULL << 52)
```

**描述**

分布式硬件框架标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_GLOBAL\_RESOURCE\_MANAGER

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_GLOBAL_RESOURCE_MANAGER (1ULL << 53)
```

**描述**

全局资源管理器标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_HARDWARE\_DEVICE\_MANAGER

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_DISTRIBUTED_HARDWARE_DEVICE_MANAGER (1ULL << 54)
```

**描述**

分布式硬件设备管理器标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_SAMGR

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_SAMGR (1ULL << 55)
```

**描述**

SA标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_POWER\_MANAGER

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_POWER_MANAGER (1ULL << 56)
```

**描述**

电源管理器标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_SCHEDULER

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_DISTRIBUTED_SCHEDULER (1ULL << 57)
```

**描述**

分布式调度程序标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_INPUT

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_DISTRIBUTED_INPUT (1ULL << 59)
```

**描述**

分布式输入标签。

**起始版本：** 12

### HIDEBUG\_TRACE\_TAG\_BLUETOOTH

PhonePC/2in1TabletTVWearable

```
1. #define HIDEBUG_TRACE_TAG_BLUETOOTH (1ULL << 60)
```

**描述**

蓝牙标签。

**起始版本：** 12
