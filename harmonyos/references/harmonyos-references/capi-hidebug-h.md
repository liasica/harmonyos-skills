---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-h
title: hidebug.h
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 头文件 > hidebug.h
category: harmonyos-references
scraped_at: 2026-04-28T08:11:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2675818bacfd6cf8386faaaecc7484688b5b9b37f76a4c840ef2c84b46dfedc4
---

## 概述

PhonePC/2in1TabletTVWearable

定义HiDebug模块的调试功能。

**引用文件：** <hidebug/hidebug.h>

**库：** libohhidebug.so

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 12

**相关模块：** [HiDebug](capi-hidebug.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [double OH\_HiDebug\_GetSystemCpuUsage()](capi-hidebug-h.md#oh_hidebug_getsystemcpuusage) | - | 获取系统的CPU资源占用情况百分比。注意：由于该接口涉及跨进程通信，耗时较长，建议不要在主线程中直接调用。 |
| [double OH\_HiDebug\_GetAppCpuUsage()](capi-hidebug-h.md#oh_hidebug_getappcpuusage) | - | 获取进程的CPU使用率百分比。注意：由于该接口涉及跨进程通信，耗时较长，建议不要在主线程中直接调用。 |
| [HiDebug\_ThreadCpuUsagePtr OH\_HiDebug\_GetAppThreadCpuUsage()](capi-hidebug-h.md#oh_hidebug_getappthreadcpuusage) | - | 获取应用所有线程CPU使用情况。注意：由于该接口涉及跨进程通信，耗时较长，建议不要在主线程中直接调用。 |
| [void OH\_HiDebug\_FreeThreadCpuUsage(HiDebug\_ThreadCpuUsagePtr \*threadCpuUsage)](capi-hidebug-h.md#oh_hidebug_freethreadcpuusage) | - | 释放线程数据结构。 |
| [void OH\_HiDebug\_GetSystemMemInfo(HiDebug\_SystemMemInfo \*systemMemInfo)](capi-hidebug-h.md#oh_hidebug_getsystemmeminfo) | - | 获取系统内存信息。 |
| [void OH\_HiDebug\_GetAppNativeMemInfo(HiDebug\_NativeMemInfo \*nativeMemInfo)](capi-hidebug-h.md#oh_hidebug_getappnativememinfo) | - | 获取应用程序进程的内存信息。注意：由于该接口需要读取/proc/{pid}/smaps\_rollup节点信息，耗时较长，建议不要在主线程中直接调用。 |
| [void OH\_HiDebug\_GetAppNativeMemInfoWithCache(HiDebug\_NativeMemInfo \*nativeMemInfo, bool forceRefresh)](capi-hidebug-h.md#oh_hidebug_getappnativememinfowithcache) | - | 获取应用程序进程的内存信息，该接口存在缓存机制以提高接口性能。缓存值的有效期为5分钟。注意：由于该接口需要读取/proc/{pid}/smaps\_rollup节点信息，耗时较长，建议不要在主线程中直接调用。 |
| [void OH\_HiDebug\_GetAppMemoryLimit(HiDebug\_MemoryLimit \*memoryLimit)](capi-hidebug-h.md#oh_hidebug_getappmemorylimit) | - | 获取应用程序进程的内存限制。 |
| [HiDebug\_ErrorCode OH\_HiDebug\_StartAppTraceCapture(HiDebug\_TraceFlag flag, uint64\_t tags, uint32\_t limitSize, char\* fileName, uint32\_t length)](capi-hidebug-h.md#oh_hidebug_startapptracecapture) | - | 启动应用trace采集。 |
| [HiDebug\_ErrorCode OH\_HiDebug\_StopAppTraceCapture()](capi-hidebug-h.md#oh_hidebug_stopapptracecapture) | - | 停止采集应用程序trace。 |
| [HiDebug\_ErrorCode OH\_HiDebug\_GetGraphicsMemory(uint32\_t \*value)](capi-hidebug-h.md#oh_hidebug_getgraphicsmemory) | - | 获取应用GPU显存大小。注意：由于该接口涉及多次跨进程通信，其耗时可能超过1秒，建议不要在主线程中直接调用该接口。 |
| [int OH\_HiDebug\_BacktraceFromFp(HiDebug\_Backtrace\_Object object, void\* startFp, void\*\* pcArray, int size)](capi-hidebug-h.md#oh_hidebug_backtracefromfp) | - | 根据给定的fp地址进行栈回溯，该函数异步信号安全。 |
| [typedef void (\*OH\_HiDebug\_SymbolicAddressCallback)(void\* pc, void\* arg, const HiDebug\_StackFrame\* frame)](capi-hidebug-h.md#oh_hidebug_symbolicaddresscallback) | OH\_HiDebug\_SymbolicAddressCallback | 若[OH\_HiDebug\_SymbolicAddress](capi-hidebug-h.md#oh_hidebug_symbolicaddress)接口调用成功，将通过该函数将解析后的栈信息返回给调用者。  **注意：** 由于该接口涉及多次IO操作，耗时较长，建议不要在主线程中直接调用。 |
| [HiDebug\_ErrorCode OH\_HiDebug\_SymbolicAddress(HiDebug\_Backtrace\_Object object, void\* pc, void\* arg, OH\_HiDebug\_SymbolicAddressCallback callback)](capi-hidebug-h.md#oh_hidebug_symbolicaddress) | - | 通过给定的pc地址获取详细的符号信息，该函数非异步信号安全。  **注意：** 由于该接口涉及多次IO操作，耗时较长，建议不要在主线程中直接调用。 |
| [HiDebug\_Backtrace\_Object OH\_HiDebug\_CreateBacktraceObject(void)](capi-hidebug-h.md#oh_hidebug_createbacktraceobject) | - | 创建一个用于栈回溯及栈解析的对象，该函数非异步信号安全。  **注意：** 由于该接口涉及多次IO操作，耗时较长，建议不要在主线程中直接调用。 |
| [void OH\_HiDebug\_DestroyBacktraceObject(HiDebug\_Backtrace\_Object object)](capi-hidebug-h.md#oh_hidebug_destroybacktraceobject) | - | 销毁由[OH\_HiDebug\_CreateBacktraceObject](capi-hidebug-h.md#oh_hidebug_createbacktraceobject)创建的对象，以释放栈回溯及栈解析过程中申请的资源，该函数非异步信号安全。 |
| [HiDebug\_ErrorCode OH\_HiDebug\_SetMallocDispatchTable(struct HiDebug\_MallocDispatch \*dispatchTable)](capi-hidebug-h.md#oh_hidebug_setmallocdispatchtable) | - | 通过设置基础库C库中的MallocDispatch表，将原始内存操作函数（例如：malloc/free/calloc/realloc/mmap/munmap）临时替换为开发者自定义的内存操作函数。MallocDispatch表是基础库C库中封装malloc/calloc/realloc/free等内存操作函数的结构体，HiDebug\_MallocDispatch只是MallocDispatch结构体的一部分。  **注意：** 禁止在自定义内存操作函数中直接调用libc标准库中的malloc/free/calloc/realloc/mmap/munmap等内存操作函数，否则会导致死锁。禁止在自定义malloc方法中使用hilog打印日志，否则会导致死锁。 |
| [HiDebug\_MallocDispatch\* OH\_HiDebug\_GetDefaultMallocDispatchTable(void)](capi-hidebug-h.md#oh_hidebug_getdefaultmallocdispatchtable) | - | 获取基础库C库当前默认MallocDispatch表，调用[OH\_HiDebug\_RestoreMallocDispatchTable](capi-hidebug-h.md#oh_hidebug_restoremallocdispatchtable)可恢复。 |
| [void OH\_HiDebug\_RestoreMallocDispatchTable(void)](capi-hidebug-h.md#oh_hidebug_restoremallocdispatchtable) | - | 恢复基础库C库MallocDispatch表。 |
| [HiDebug\_ErrorCode OH\_HiDebug\_GetGraphicsMemorySummary(uint32\_t interval, HiDebug\_GraphicsMemorySummary \*summary)](capi-hidebug-h.md#oh_hidebug_getgraphicsmemorysummary) | - | 获取应用显存占用的详细数据。 |
| [typedef void (\*OH\_HiDebug\_ThreadLiteSamplingCallback)(const char\* stacks)](capi-hidebug-h.md#oh_hidebug_threadlitesamplingcallback) | OH\_HiDebug\_ThreadLiteSamplingCallback | 轻量级Perf采样栈内容的回调函数定义。注意：采样数据仅在该回调函数执行期间有效，若需在函数外使用，务必对采样栈内容进行深拷贝。 |
| [HiDebug\_ErrorCode OH\_HiDebug\_RequestThreadLiteSampling(HiDebug\_ProcessSamplerConfig\* config, OH\_HiDebug\_ThreadLiteSamplingCallback stacksCallback)](capi-hidebug-h.md#oh_hidebug_requestthreadlitesampling) | - | 对指定的数个线程进行Perf采样，并在调用结束后返回采样栈内容。注意：调用该函数后会阻塞当前线程，直至采样过程完全结束。系统对该接口的调用次数有严格限制，频繁调用超出限额后，将返回[HIDEBUG\_RESOURCE\_UNAVAILABLE](capi-hidebug-type-h.md#hidebug_errorcode)错误码。 |
| [uint64\_t OH\_HiDebug\_SetCrashObj(HiDebug\_CrashObjType type, void\* addr)](capi-hidebug-h.md#oh_hidebug_setcrashobj) | - | 将维测信息添加到崩溃日志中，与[OH\_HiDebug\_ResetCrashObj](capi-hidebug-h.md#oh_hidebug_resetcrashobj)配对使用。若程序在OH\_HiDebug\_SetCrashObj与OH\_HiDebug\_ResetCrashObj之间发生崩溃，会将OH\_HiDebug\_SetCrashObj设置的维测信息添加到记录本次崩溃的日志中。 |
| [void OH\_HiDebug\_ResetCrashObj(uint64\_t crashObj)](capi-hidebug-h.md#oh_hidebug_resetcrashobj) | - | 将维测信息对象还原到使用OH\_HiDebug\_SetCrashObj之前的状态。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_HiDebug\_GetSystemCpuUsage()

PhonePC/2in1TabletTVWearable

```
1. double OH_HiDebug_GetSystemCpuUsage()
```

**描述**

获取系统的CPU资源占用情况百分比。注意：由于该接口涉及跨进程通信，耗时较长，建议不要在主线程中直接调用。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回系统CPU资源占用情况百分比。如果返回结果为0，可能的原因是获取失败。 |

### OH\_HiDebug\_GetAppCpuUsage()

PhonePC/2in1TabletTVWearable

```
1. double OH_HiDebug_GetAppCpuUsage()
```

**描述**

获取进程的CPU使用率百分比。注意：由于该接口涉及跨进程通信，耗时较长，建议不要在主线程中直接调用。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回进程的CPU使用率百分比。如果返回结果为0，可能因当前应用的CPU使用率过低导致。 |

### OH\_HiDebug\_GetAppThreadCpuUsage()

PhonePC/2in1TabletTVWearable

```
1. HiDebug_ThreadCpuUsagePtr OH_HiDebug_GetAppThreadCpuUsage()
```

**描述**

获取应用所有线程CPU使用情况。注意：由于该接口涉及跨进程通信，耗时较长，建议不要在主线程中直接调用。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HiDebug\_ThreadCpuUsagePtr](capi-hidebug-hidebug-threadcpuusage.md) | 返回所有线程CPU使用情况，见[HiDebug\_ThreadCpuUsagePtr](capi-hidebug-hidebug-threadcpuusage.md)。  若返回结果为null，可能因未获取到线程相关数据所致。 |

### OH\_HiDebug\_FreeThreadCpuUsage()

PhonePC/2in1TabletTVWearable

```
1. void OH_HiDebug_FreeThreadCpuUsage(HiDebug_ThreadCpuUsagePtr *threadCpuUsage)
```

**描述**

释放线程数据结构。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiDebug\_ThreadCpuUsagePtr](capi-hidebug-hidebug-threadcpuusage.md) \*threadCpuUsage | 应用的所有线程可用CPU使用缓冲区指针，见[HiDebug\_ThreadCpuUsagePtr](capi-hidebug-hidebug-threadcpuusage.md)。传入的参数是要由OH\_HiDebug\_GetAppThreadCpuUsage()得到的。 |

### OH\_HiDebug\_GetSystemMemInfo()

PhonePC/2in1TabletTVWearable

```
1. void OH_HiDebug_GetSystemMemInfo(HiDebug_SystemMemInfo *systemMemInfo)
```

**描述**

获取系统内存信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiDebug\_SystemMemInfo](capi-hidebug-hidebug-systemmeminfo.md) \*systemMemInfo | 表示指向[HiDebug\_SystemMemInfo](capi-hidebug-hidebug-systemmeminfo.md)。函数调用后，若结构体数据为空，则表明调用失败。 |

### OH\_HiDebug\_GetAppNativeMemInfo()

PhonePC/2in1TabletTVWearable

```
1. void OH_HiDebug_GetAppNativeMemInfo(HiDebug_NativeMemInfo *nativeMemInfo)
```

**描述**

获取应用程序进程的内存信息。注意：由于该接口需要读取/proc/{pid}/smaps\_rollup节点信息，耗时较长，建议不要在主线程中直接调用。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiDebug\_NativeMemInfo](capi-hidebug-hidebug-nativememinfo.md) \*nativeMemInfo | 表示指向[HiDebug\_NativeMemInfo](capi-hidebug-hidebug-nativememinfo.md)。函数调用后，若结构体数据为空，则表明调用失败。 |

### OH\_HiDebug\_GetAppNativeMemInfoWithCache()

PhonePC/2in1TabletTVWearable

```
1. void OH_HiDebug_GetAppNativeMemInfoWithCache(HiDebug_NativeMemInfo *nativeMemInfo, bool forceRefresh)
```

**描述**

获取应用程序进程的内存信息，该接口存在缓存机制以提高接口性能。缓存值的有效期为5分钟。注意：由于该接口需要读取/proc/{pid}/smaps\_rollup节点信息，耗时较长，建议不要在主线程中直接调用。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiDebug\_NativeMemInfo](capi-hidebug-hidebug-nativememinfo.md) \*nativeMemInfo | 表示指向[HiDebug\_NativeMemInfo](capi-hidebug-hidebug-nativememinfo.md)。函数调用后，若结构体数据为空，则表明调用失败。 |
| bool forceRefresh | 是否需要无视缓存有效性，强制更新缓存值。  当为true时，直接获取当前内存数据并更新缓存值；  当为false时，缓存有效时，直接返回缓存值，缓存失效时，获取当前内存数据并更新缓存值。 |

### OH\_HiDebug\_GetAppMemoryLimit()

PhonePC/2in1TabletTVWearable

```
1. void OH_HiDebug_GetAppMemoryLimit(HiDebug_MemoryLimit *memoryLimit)
```

**描述**

获取应用程序进程的内存限制。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiDebug\_MemoryLimit](capi-hidebug-hidebug-memorylimit.md) \*memoryLimit | 表示指向[HiDebug\_MemoryLimit](capi-hidebug-hidebug-memorylimit.md)。函数调用后，若结构体数据为空，则表明调用失败。 |

### OH\_HiDebug\_StartAppTraceCapture()

PhonePC/2in1TabletTVWearable

```
1. HiDebug_ErrorCode OH_HiDebug_StartAppTraceCapture(HiDebug_TraceFlag flag, uint64_t tags, uint32_t limitSize, char* fileName, uint32_t length)
```

**描述**

启动应用trace采集。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiDebug\_TraceFlag](capi-hidebug-type-h.md#hidebug_traceflag) flag | 采集线程trace方式。 |
| uint64\_t tags | 采集trace场景标签。 |
| uint32\_t limitSize | trace文件的最大大小（以字节为单位），最大为 500MB。 |
| char\* fileName | 输出trace文件名缓冲区。 |
| uint32\_t length | 输出trace文件名缓冲区长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HiDebug\_ErrorCode](capi-hidebug-type-h.md#hidebug_errorcode) | 0 - 成功。  [HIDEBUG\_INVALID\_ARGUMENT](capi-hidebug-type-h.md#hidebug_errorcode) 401 - fileName参数为空指针或者传入的length参数过小或者limitSize参数小于等于0。  11400102 - 已经开启了一个trace。  11400103 - 没有权限去开启trace。  11400104 - 系统内部错误。 |

### OH\_HiDebug\_StopAppTraceCapture()

PhonePC/2in1TabletTVWearable

```
1. HiDebug_ErrorCode OH_HiDebug_StopAppTraceCapture()
```

**描述**

停止采集应用程序trace。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HiDebug\_ErrorCode](capi-hidebug-type-h.md#hidebug_errorcode) | 0 - 成功。  11400104 - 系统内部错误。  11400105 - 当前没有trace正在运行 |

### OH\_HiDebug\_GetGraphicsMemory()

PhonePC/2in1TabletTVWearable

```
1. HiDebug_ErrorCode OH_HiDebug_GetGraphicsMemory(uint32_t *value)
```

**描述**

获取应用GPU显存大小。注意：由于该接口涉及多次跨进程通信，其耗时可能超过1秒，建议不要在主线程中直接调用该接口。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t \*value | 指向用来保存接口获取到的应用显存大小（单位KB）的变量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HiDebug\_ErrorCode](capi-hidebug-type-h.md#hidebug_errorcode) | 0 - 接口获取成功。  401 - 无效参数，所传递参数为空指针。  11400104 - 系统内部错误。 |

### OH\_HiDebug\_BacktraceFromFp()

PhonePC/2in1TabletTVWearable

```
1. int OH_HiDebug_BacktraceFromFp(HiDebug_Backtrace_Object object, void* startFp, void** pcArray, int size)
```

**描述**

根据给定的fp地址进行栈回溯，该函数异步信号安全。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiDebug\_Backtrace\_Object](capi-hidebug-hidebug-backtrace-object--8h.md) object | 由[OH\_HiDebug\_CreateBacktraceObject](capi-hidebug-h.md#oh_hidebug_createbacktraceobject)接口获取到的用来栈回溯的对象。 |
| void\* startFp | 栈回溯的起始栈帧地址。 |
| void\*\* pcArray | 保存栈回溯得到的pc地址的数组。 |
| int size | 保存栈回溯得到的pc地址的数组长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功回溯并写入到pcArray中的栈帧数量。如果返回结果为0，原因可能是栈回溯失败。 |

### OH\_HiDebug\_SymbolicAddressCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_HiDebug_SymbolicAddressCallback)(void* pc, void* arg, const HiDebug_StackFrame* frame)
```

**描述**

若[OH\_HiDebug\_SymbolicAddress](capi-hidebug-h.md#oh_hidebug_symbolicaddress)接口调用成功，将通过该函数将解析后的栈信息返回给调用者。注意：由于该接口涉及多次IO操作，耗时较长，建议不要在主线程中直接调用。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| void\* pc | 传入[OH\_HiDebug\_SymbolicAddress](capi-hidebug-h.md#oh_hidebug_symbolicaddress)接口的需要解析的pc地址。 |
| void\* arg | 传入[OH\_HiDebug\_SymbolicAddress](capi-hidebug-h.md#oh_hidebug_symbolicaddress)接口的arg值。 |
| [const HiDebug\_StackFrame](capi-hidebug-hidebug-stackframe.md)\* frame | 由传入[OH\_HiDebug\_SymbolicAddress](capi-hidebug-h.md#oh_hidebug_symbolicaddress)接口的pc地址解析后的得到栈信息[HiDebug\_StackFrame](capi-hidebug-hidebug-stackframe.md)指针，该指针指向内容仅在该函数作用域内有效。 |

### OH\_HiDebug\_SymbolicAddress()

PhonePC/2in1TabletTVWearable

```
1. HiDebug_ErrorCode OH_HiDebug_SymbolicAddress(HiDebug_Backtrace_Object object, void* pc, void* arg, OH_HiDebug_SymbolicAddressCallback callback)
```

**描述**

通过给定的pc地址获取详细的符号信息，该函数非异步信号安全。

注意

由于该接口涉及多次IO操作，耗时较长，建议不要在主线程中直接调用。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiDebug\_Backtrace\_Object](capi-hidebug-hidebug-backtrace-object--8h.md) object | 由[OH\_HiDebug\_CreateBacktraceObject](capi-hidebug-h.md#oh_hidebug_createbacktraceobject)接口创建的对象。 |
| void\* pc | 由[OH\_HiDebug\_BacktraceFromFp](capi-hidebug-h.md#oh_hidebug_backtracefromfp)接口获取到的pc地址。 |
| void\* arg | 保留的自定义参数，符号解析成功后系统内部会将该参数传递给回调函数[OH\_HiDebug\_SymbolicAddressCallback](capi-hidebug-h.md#oh_hidebug_symbolicaddresscallback)。 |
| [OH\_HiDebug\_SymbolicAddressCallback](capi-hidebug-h.md#oh_hidebug_symbolicaddresscallback) callback | 用于返回解析后栈信息的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HiDebug\_ErrorCode](capi-hidebug-type-h.md#hidebug_errorcode) | 返回结果具体可参考[HiDebug\_ErrorCode](capi-hidebug-type-h.md#hidebug_errorcode)：  [HIDEBUG\_SUCCESS](capi-hidebug-type-h.md#hidebug_errorcode) 成功获取到详细的栈信息，且该函数传入的callback被调用。  [HIDEBUG\_INVALID\_ARGUMENT](capi-hidebug-type-h.md#hidebug_errorcode) 无效参数。  [HIDEBUG\_INVALID\_SYMBOLIC\_PC\_ADDRESS](capi-hidebug-type-h.md#hidebug_errorcode) 无法根据传入的pc地址找到对应的符号。 |

### OH\_HiDebug\_CreateBacktraceObject()

PhonePC/2in1TabletTVWearable

```
1. HiDebug_Backtrace_Object OH_HiDebug_CreateBacktraceObject(void)
```

**描述**

创建一个用于栈回溯及栈解析的对象，该函数非异步信号安全。

注意

由于该接口涉及多次IO操作，耗时较长，建议不要在主线程中直接调用。

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HiDebug\_Backtrace\_Object](capi-hidebug-hidebug-backtrace-object--8h.md) | 返回创建的对象的指针，当创建失败时返回NULL。 |

### OH\_HiDebug\_DestroyBacktraceObject()

PhonePC/2in1TabletTVWearable

```
1. void OH_HiDebug_DestroyBacktraceObject(HiDebug_Backtrace_Object object)
```

**描述**

销毁由[OH\_HiDebug\_CreateBacktraceObject](capi-hidebug-h.md#oh_hidebug_createbacktraceobject)创建的对象，以释放栈回溯及栈解析过程中申请的资源，该函数非异步信号安全。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiDebug\_Backtrace\_Object](capi-hidebug-hidebug-backtrace-object--8h.md) object | 需要被销毁的对象。 |

### OH\_HiDebug\_SetMallocDispatchTable()

PhonePC/2in1TabletTVWearable

```
1. HiDebug_ErrorCode OH_HiDebug_SetMallocDispatchTable(struct HiDebug_MallocDispatch *dispatchTable)
```

**描述**

通过设置基础库C库中的MallocDispatch表，将原始内存操作函数（例如：malloc/free/calloc/realloc/mmap/munmap）临时替换为开发者自定义的内存操作函数。MallocDispatch表是基础库C库中封装malloc/calloc/realloc/free等内存操作函数的结构体，HiDebug\_MallocDispatch只是MallocDispatch结构体的一部分。

注意

禁止在自定义内存操作函数中直接调用libc标准库中的malloc/free/calloc/realloc/mmap/munmap等内存操作函数，否则会导致死锁。

禁止在自定义malloc方法中使用hilog打印日志，否则会导致死锁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct HiDebug\_MallocDispatch](capi-hidebug-hidebug-mallocdispatch.md) \*dispatchTable | 指向开发者自定义内存操作函数[HiDebug\_MallocDispatch](capi-hidebug-hidebug-mallocdispatch.md)结构体指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HiDebug\_ErrorCode](capi-hidebug-type-h.md#hidebug_errorcode) | 返回结果具体可参考[HiDebug\_ErrorCode](capi-hidebug-type-h.md#hidebug_errorcode)：  [HIDEBUG\_SUCCESS](capi-hidebug-type-h.md#hidebug_errorcode) 成功设置自定义内存操作函数。  [HIDEBUG\_INVALID\_ARGUMENT](capi-hidebug-type-h.md#hidebug_errorcode) 无效参数。 |

### OH\_HiDebug\_GetDefaultMallocDispatchTable()

PhonePC/2in1TabletTVWearable

```
1. HiDebug_MallocDispatch* OH_HiDebug_GetDefaultMallocDispatchTable(void)
```

**描述**

获取基础库C库当前默认MallocDispatch表，调用[OH\_HiDebug\_RestoreMallocDispatchTable](capi-hidebug-h.md#oh_hidebug_restoremallocdispatchtable)可恢复。

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HiDebug\_MallocDispatch\*](capi-hidebug-hidebug-mallocdispatch.md) | 当前C库默认的[HiDebug\_MallocDispatch](capi-hidebug-hidebug-mallocdispatch.md)结构体指针。 |

### OH\_HiDebug\_RestoreMallocDispatchTable()

PhonePC/2in1TabletTVWearable

```
1. void OH_HiDebug_RestoreMallocDispatchTable(void)
```

**描述**

恢复基础库C库MallocDispatch表。

**起始版本：** 20

### OH\_HiDebug\_GetGraphicsMemorySummary()

PhonePC/2in1TabletTVWearable

```
1. HiDebug_ErrorCode OH_HiDebug_GetGraphicsMemorySummary(uint32_t interval, HiDebug_GraphicsMemorySummary *summary)
```

**描述**

获取应用显存占用的详细数据。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t interval | 当显存数据缓存值存在时间超过设定间隔interval（单位：秒）时，接口会获取最新的显存数据并更新缓存；否则，接口将直接返回缓存值。  interval的取值范围为[2，3600]，若传入的interval超出取值范围时，将使用300作为默认值。 |
| [HiDebug\_GraphicsMemorySummary](capi-hidebug-hidebug-graphicsmemorysummary.md) \*summary | 表示指向[HiDebug\_GraphicsMemorySummary](capi-hidebug-hidebug-graphicsmemorysummary.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HiDebug\_ErrorCode](capi-hidebug-type-h.md#hidebug_errorcode) | 返回结果具体可参考[HiDebug\_ErrorCode](capi-hidebug-type-h.md#hidebug_errorcode)：  HIDEBUG\_SUCCESS 成功获取到应用显存数据。  HIDEBUG\_INVALID\_ARGUMENT 无效参数。  HIDEBUG\_TRACE\_ABNORMAL 系统内部错误。 |

### OH\_HiDebug\_ThreadLiteSamplingCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_HiDebug_ThreadLiteSamplingCallback)(const char* stacks)
```

**描述**

轻量级Perf采样栈内容的回调函数定义。注意：采样数据仅在该回调函数执行期间有效，若需在函数外使用，务必对采样栈内容进行深拷贝。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* stacks | 采样得到的调用栈内容。 |

### OH\_HiDebug\_RequestThreadLiteSampling()

PhonePC/2in1TabletTVWearable

```
1. HiDebug_ErrorCode OH_HiDebug_RequestThreadLiteSampling(HiDebug_ProcessSamplerConfig* config, OH_HiDebug_ThreadLiteSamplingCallback stacksCallback)
```

**描述**

对指定的数个线程进行Perf采样，并在调用结束后返回采样栈内容。注意：调用该函数后会阻塞当前线程，直至采样过程完全结束。系统对该接口的调用次数有严格限制，频繁调用超出限额后，将返回[HIDEBUG\_RESOURCE\_UNAVAILABLE](capi-hidebug-type-h.md#hidebug_errorcode)错误码。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiDebug\_ProcessSamplerConfig](capi-hidebug-hidebug-processsamplerconfig.md)\* config | 指向Perf采样配置结构体[HiDebug\_ProcessSamplerConfig](capi-hidebug-hidebug-processsamplerconfig.md)的指针。 |
| [OH\_HiDebug\_ThreadLiteSamplingCallback](capi-hidebug-h.md#oh_hidebug_threadlitesamplingcallback) stacksCallback | 采样结束时的回调函数，用于返回采样结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HiDebug\_ErrorCode](capi-hidebug-type-h.md#hidebug_errorcode) | 返回结果码：  HIDEBUG\_SUCCESS：采样成功完成。  HIDEBUG\_INVALID\_ARGUMENT：无效参数。  HIDEBUG\_NOT\_SUPPORTED：当前设备不支持Perf采样。  HIDEBUG\_UNDER\_SAMPLING：已有采样任务正在执行中。  HIDEBUG\_RESOURCE\_UNAVAILABLE：采样资源不足或已达调用上限。 |

### OH\_HiDebug\_SetCrashObj()

PhonePC/2in1TabletTVWearable

```
1. uint64_t OH_HiDebug_SetCrashObj(HiDebug_CrashObjType type, void* addr)
```

**描述**

将维测信息添加到崩溃日志中，与[OH\_HiDebug\_ResetCrashObj](capi-hidebug-h.md#oh_hidebug_resetcrashobj)配对使用。若程序在OH\_HiDebug\_SetCrashObj与OH\_HiDebug\_ResetCrashObj之间发生崩溃，会将OH\_HiDebug\_SetCrashObj设置的维测信息添加到记录本次崩溃的日志中。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiDebug\_CrashObjType](capi-hidebug-type-h.md#hidebug_crashobjtype) type | 维测信息的数据类型[HiDebug\_CrashObjType](capi-hidebug-type-h.md#hidebug_crashobjtype)。 |
| void\* addr | 维测信息的地址，崩溃时该地址必须保持有效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint64\_t | 上次设置的维测信息的对象，如果上次没有设置则为0。 |

### OH\_HiDebug\_ResetCrashObj()

PhonePC/2in1TabletTVWearable

```
1. void OH_HiDebug_ResetCrashObj(uint64_t crashObj)
```

**描述**

将维测信息对象还原到使用OH\_HiDebug\_SetCrashObj之前的状态。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint64\_t crashObj | 函数OH\_HiDebug\_SetCrashObj的返回值。 |
