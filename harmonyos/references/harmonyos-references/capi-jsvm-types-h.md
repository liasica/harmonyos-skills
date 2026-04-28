---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h
title: jsvm_types.h
breadcrumb: API参考 > 公共基础能力 > C API > 头文件 > jsvm_types.h
category: harmonyos-references
scraped_at: 2026-04-28T08:19:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a5ee98c92c0dd966559ef409ef4fd9837b9789176924dc76985d8f58509911a9
---

## 概述

PhonePC/2in1TabletWearable

提供JSVM-API类型定义。通过API接口为开发者提供独立、标准、完整的JavaScript引擎能力，包括管理引擎生命周期、编译运行JS代码、实现JS/C++跨语言调用、拍摄快照等。

**引用文件：** <ark\_runtime/jsvm\_types.h>

**库：** libjsvm.so

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 11

**相关模块：** [JSVM](capi-jsvm.md)

## 汇总

PhonePC/2in1TabletWearable

### 结构体

PhonePC/2in1TabletWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [JSVM\_CallbackStruct](capi-jsvm-jsvm-callbackstruct.md) | JSVM\_CallbackStruct | 用户提供的native回调函数的指针和数据，这些函数通过JSVM-API接口暴露给JavaScript。 |
| [JSVM\_HeapStatistics](capi-jsvm-jsvm-heapstatistics.md) | JSVM\_HeapStatistics | 用于保存有关JavaScript堆内存使用情况的统计信息。 |
| [JSVM\_InitOptions](capi-jsvm-jsvm-initoptions.md) | JSVM\_InitOptions | 初始化选项，用于初始化JavaScript虚拟机。 |
| [JSVM\_CreateVMOptions](capi-jsvm-jsvm-createvmoptions.md) | JSVM\_CreateVMOptions | 创建JavaScript虚拟机的选项。 |
| [JSVM\_VMInfo](capi-jsvm-jsvm-vminfo.md) | JSVM\_VMInfo | JavaScript虚拟机信息。 |
| [JSVM\_PropertyDescriptor](capi-jsvm-jsvm-propertydescriptor.md) | JSVM\_PropertyDescriptor | 属性描述符。 |
| [JSVM\_ExtendedErrorInfo](capi-jsvm-jsvm-extendederrorinfo.md) | JSVM\_ExtendedErrorInfo | 扩展的异常信息。 |
| [JSVM\_TypeTag](capi-jsvm-jsvm-typetag.md) | JSVM\_TypeTag | 类型标记，存储为两个无符号64位整数的128位值。作为一个UUID，通过它，JavaScript对象可以是"tagged"，以确保它们的类型保持不变。 |
| [JSVM\_PropertyHandlerConfigurationStruct](capi-jsvm-jsvm-propertyhandlerconfigurationstruct.md) | JSVM\_PropertyHandlerConfigurationStruct | 当执行对象的getter、setter、deleter和enumerator操作时，该结构体中对应的函数回调将会触发。 |
| [JSVM\_ScriptOrigin](capi-jsvm-jsvm-scriptorigin.md) | JSVM\_ScriptOrigin | 某段JavaScript代码的原始信息，如sourceMap路径、源文件名、源文件中的起始行/列号等。 |
| [JSVM\_CompileOptions](capi-jsvm-jsvm-compileoptions.md) | JSVM\_CompileOptions | 对应JSVM的编译选项，包含内容和ID。 |
| [JSVM\_CodeCache](capi-jsvm-jsvm-codecache.md) | JSVM\_CodeCache | 对应JSVM代码缓存的地址与大小。 |
| [JSVM\_PropertyHandler](capi-jsvm-jsvm-propertyhandler.md) | JSVM\_PropertyHandler | 包含将class作为函数进行调用时所触发的回调函数的函数指针和访问实例对象属性时触发的回调函数的函数指针集。 |
| [JSVM\_DefineClassOptions](capi-jsvm-jsvm-defineclassoptions.md) | JSVM\_DefineClassOptions | 定义Class的选项。 |
| [JSVM\_VM\_\_\*](capi-jsvm-jsvm-vm--8h.md) | JSVM\_VM | 表示JavaScript虚拟机实例。 |
| [JSVM\_VMScope\_\_\*](capi-jsvm-jsvm-vmscope--8h.md) | JSVM\_VMScope | 表示JavaScript虚拟机作用域。 |
| [JSVM\_EnvScope\_\_\*](capi-jsvm-jsvm-envscope--8h.md) | JSVM\_EnvScope | 表示用于控制附加到当前虚拟机实例的环境。只有当线程通过OH\_JSVM\_OpenEnvScope进入该环境的JSVM\_EnvScope后，该环境才对线程的虚拟机实例可用。 |
| [JSVM\_Script\_\_\*](capi-jsvm-jsvm-script--8h.md) | JSVM\_Script | 表示一段JavaScript代码。 |
| [JSVM\_Env\_\_\*](capi-jsvm-jsvm-env--8h.md) | JSVM\_Env | 表示虚拟机特定状态的上下文环境，需要在调用native函数时作为参数传递，并且传递给后续任何的JSVM-API嵌套调用。 |
| [JSVM\_CpuProfiler\_\_\*](capi-jsvm-jsvm-cpuprofiler--8h.md) | JSVM\_CpuProfiler | 表示一个JavaScript CPU时间性能分析器。 |
| [JSVM\_Value\_\_\*](capi-jsvm-jsvm-value--8h.md) | JSVM\_Value | 表示JavaScript值。 |
| [JSVM\_Data\_\_\*](capi-jsvm-jsvm-data--8h.md) | JSVM\_Data | 表示一个 JavaScript Data。 |
| [JSVM\_Ref\_\_\*](capi-jsvm-jsvm-ref--8h.md) | JSVM\_Ref | 表示JavaScript值的引用。 |
| [JSVM\_HandleScope\_\_\*](capi-jsvm-jsvm-handlescope--8h.md) | JSVM\_HandleScope | 表示JavaScript值的作用域，用于控制和修改在特定范围内创建的对象的生命周期。通常，JSVM-API值是在JSVM\_HandleScope的上下文中创建的。当从JavaScript调用native方法时，将存在默认JSVM\_HandleScope。如果用户没有显式创建新的JSVM\_HandleScope，将在默认JSVM\_HandleScope中创建JSVM-API值。对于native方法执行之外的任何代码调用（例如，在libuv回调调用期间），模块需要在调用任何可能导致创建JavaScript值的函数之前创建一个作用域。JSVM\_HandleScope是使用OH\_JSVM\_OpenHandleScope创建的，并使用OH\_JSVM\_CloseHandleScope销毁的。关闭作用域代表向GC指示在JSVM\_HandleScope作用域的生命周期内创建的所有JSVM\_Value将不再从当前堆的栈帧中引用。 |
| [JSVM\_EscapableHandleScope\_\_\*](capi-jsvm-jsvm-escapablehandlescope--8h.md) | JSVM\_EscapableHandleScope | 表示一种特殊类型的handle scope，用于将在特定handle scope内创建的值返回到父作用域。 |
| [JSVM\_CallbackInfo\_\_\*](capi-jsvm-jsvm-callbackinfo--8h.md) | JSVM\_CallbackInfo | 表示传递给回调函数的不透明数据类型。可用于获取调用该函数的上下文的附加信息。 |
| [JSVM\_Deferred\_\_\*](capi-jsvm-jsvm-deferred--8h.md) | JSVM\_Deferred | 表示Promise延迟对象。 |
| [JSVM\_PropertyHandlerConfigurationStruct\*](api-jsvm-jsvm-propertyhandlerconfigurationstruct8h.md) | JSVM\_PropertyHandlerCfg | 包含属性监听回调的结构的指针类型。 |
| [JSVM\_CallbackStruct\*](capi-jsvm-jsvm-callbackstruct8h.md) | JSVM\_Callback | 用户提供的native函数的函数指针类型，这些函数通过JSVM-API接口暴露给JavaScript。 |
| [JSVM\_CompileProfile](capi-jsvm-jsvm-compileprofile.md) | JSVM\_CompileProfile | 与JSVM\_COMPILE\_COMPILE\_PROFILE一起传递的编译采样文件。 |

### 枚举

PhonePC/2in1TabletWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [JSVM\_PropertyAttributes](capi-jsvm-types-h.md#jsvm_propertyattributes) | JSVM\_PropertyAttributes | 用于控制JavaScript对象属性的行为。 |
| [JSVM\_ValueType](capi-jsvm-types-h.md#jsvm_valuetype) | JSVM\_ValueType | 描述JSVM\_Value的类型。 |
| [JSVM\_TypedarrayType](capi-jsvm-types-h.md#jsvm_typedarraytype) | JSVM\_TypedarrayType | 描述TypedArray的类型。 |
| [JSVM\_Status](capi-jsvm-types-h.md#jsvm_status) | JSVM\_Status | 表示JSVM-API调用成功或失败的完整状态码。 |
| [JSVM\_KeyCollectionMode](capi-jsvm-types-h.md#jsvm_keycollectionmode) | JSVM\_KeyCollectionMode | 限制查找属性的范围。 |
| [JSVM\_KeyFilter](capi-jsvm-types-h.md#jsvm_keyfilter) | JSVM\_KeyFilter | 属性过滤器，可以通过使用or来构造一个复合过滤器。 |
| [JSVM\_KeyConversion](capi-jsvm-types-h.md#jsvm_keyconversion) | JSVM\_KeyConversion | 键转换选项。 |
| [JSVM\_MemoryPressureLevel](capi-jsvm-types-h.md#jsvm_memorypressurelevel) | JSVM\_MemoryPressureLevel | 内存压力水平。 |
| [JSVM\_CompileMode](capi-jsvm-types-h.md#jsvm_compilemode) | JSVM\_CompileMode | JSVM编译模式。 |
| [JSVM\_CompileOptionId](capi-jsvm-types-h.md#jsvm_compileoptionid) | JSVM\_CompileOptionId | JSVM编译选项ID。 |
| [JSVM\_RegExpFlags](capi-jsvm-types-h.md#jsvm_regexpflags) | JSVM\_RegExpFlags | 正则表达式标志位。它们可以用来启用一组标志。 |
| [JSVM\_InitializedFlag](capi-jsvm-types-h.md#jsvm_initializedflag) | JSVM\_InitializedFlag | 初始化方式的标志位。 |
| [JSVM\_WasmOptLevel](capi-jsvm-types-h.md#jsvm_wasmoptlevel) | JSVM\_WasmOptLevel | WebAssembly 函数优化等级。 |
| [JSVM\_CacheType](capi-jsvm-types-h.md#jsvm_cachetype) | JSVM\_CacheType | 缓存类型。 |
| [JSVM\_MicrotaskPolicy](capi-jsvm-types-h.md#jsvm_microtaskpolicy) | JSVM\_MicrotaskPolicy | JSVM 微任务执行策略。 |
| [JSVM\_TraceCategory](capi-jsvm-types-h.md#jsvm_tracecategory) | JSVM\_TraceCategory | JSVM 内部 Trace 事件的类别。 |
| [JSVM\_CBTriggerTimeForGC](capi-jsvm-types-h.md#jsvm_cbtriggertimeforgc) | JSVM\_CBTriggerTimeForGC | 触发回调函数的时机。 |
| [JSVM\_GCType](capi-jsvm-types-h.md#jsvm_gctype) | JSVM\_GCType | GC类型。 |
| [JSVM\_GCCallbackFlags](capi-jsvm-types-h.md#jsvm_gccallbackflags) | JSVM\_GCCallbackFlags | GC回调函数标记。 |
| [JSVM\_PromiseRejectEvent](capi-jsvm-types-h.md#jsvm_promiserejectevent) | JSVM\_PromiseRejectEvent | promise-reject事件。 |
| [JSVM\_MessageErrorLevel](capi-jsvm-types-h.md#jsvm_messageerrorlevel) | JSVM\_MessageErrorLevel | message的报错级别。 |
| [JSVM\_DefineClassOptionsId](capi-jsvm-types-h.md#jsvm_defineclassoptionsid) | JSVM\_DefineClassOptionsId | 定义Class的选项ID。 |
| [JSVM\_DebugOption](capi-jsvm-types-h.md#jsvm_debugoption) | JSVM\_DebugOption | 调试选项。 |

### 函数

PhonePC/2in1TabletWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (JSVM\_CDECL\* JSVM\_Finalize)(JSVM\_Env env,void\* finalizeData,void\* finalizeHint)](capi-jsvm-types-h.md#jsvm_finalize) | JSVM\_CDECL\* JSVM\_Finalize | 函数指针类型，当native类型对象或数据与JS对象被关联时，传入该指针。该函数将会在关联的JS对象被GC回收时被调用，用以执行native的清理动作。 |
| [typedef bool (JSVM\_CDECL\* JSVM\_OutputStream)(const char\* data,int size,void\* streamData)](capi-jsvm-types-h.md#jsvm_outputstream) | JSVM\_CDECL\* JSVM\_OutputStream | ASCII输出流回调的函数指针类型。参数data是指输出的数据指针。参数size是指输出的数据大小。空数据指针指示流的结尾。参数streamData是指与回调一起传递给API函数的指针，该API函数向输出流生成数据。 |
| [typedef void (JSVM\_CDECL\* JSVM\_HandlerForGC)(JSVM\_VM vm, JSVM\_GCType gcType, JSVM\_GCCallbackFlags flags, void\* data)](capi-jsvm-types-h.md#jsvm_handlerforgc) | JSVM\_CDECL\* JSVM\_HandlerForGC | GC回调的函数指针类型。 |
| [typedef void (JSVM\_CDECL\* JSVM\_HandlerForOOMError)(const char\* location,const char\* detail,bool isHeapOOM)](capi-jsvm-types-h.md#jsvm_handlerforoomerror) | JSVM\_CDECL\* JSVM\_HandlerForOOMError | OOM-Error回调的函数指针类型。 |
| [typedef void (JSVM\_CDECL\* JSVM\_HandlerForFatalError)(const char\* location,const char\* message)](capi-jsvm-types-h.md#jsvm_handlerforfatalerror) | JSVM\_CDECL\* JSVM\_HandlerForFatalError | Fatal-Error回调的函数指针类型。 |
| [typedef void (JSVM\_CDECL\* JSVM\_HandlerForPromiseReject)(JSVM\_Env env, JSVM\_PromiseRejectEvent rejectEvent, JSVM\_Value rejectInfo)](capi-jsvm-types-h.md#jsvm_handlerforpromisereject) | JSVM\_CDECL\* JSVM\_HandlerForPromiseReject | Promise-Reject回调的函数指针类型。 |

### 变量

PhonePC/2in1TabletWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| uint16\_t | char16\_t | 为uint16\_t创建一个别名——char16\_t。  这段代码的核心目的是确保 char16\_t 这个类型在所有目标编译环境中都可用，即使在一些不支持它的旧环境里。char16\_t 是 C++11 标准中引入的一个新的基本数据类型，专门用于存储16位字符，通常用来表示UTF-16编码的字符。  如果编译器本身不认识char16\_t，手动创建一个底层实现是16位无符号的整数类型。前置生效条件为：当前编译器——非C++编译器编译 || 是微软Visual C++编译器且版本早于Visual Studio 2015（不含）。 |

## 枚举类型说明

PhonePC/2in1TabletWearable

### JSVM\_PropertyAttributes

PhonePC/2in1TabletWearable

```
1. enum JSVM_PropertyAttributes
```

**描述**

用于控制JavaScript对象属性的行为。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_DEFAULT = 0 | 没有在属性上设置显式属性。 |
| JSVM\_WRITABLE = 1 << 0 | 该属性是可写的。 |
| JSVM\_ENUMERABLE = 1 << 1 | 该属性是可枚举的。 |
| JSVM\_CONFIGURABLE = 1 << 2 | 该属性是可配置的。 |
| JSVM\_NO\_RECEIVER\_CHECK = 1 << 3 | 用于标记本地方法的接收器无需进行检查。如果未设置 JSVM\_NO\_RECEIVER\_CHECK，则该方法仅接受定义类的实例作为接收器，否则会向 JSVM 抛出异常“类型错误：非法调用”。 |
| JSVM\_STATIC = 1 << 10 | 该属性将被定义为类的静态属性，而不是默认的实例属性。这仅由OH\_JSVM\_DefineClass使用。 |
| JSVM\_DEFAULT\_METHOD = JSVM\_WRITABLE | JSVM\_CONFIGURABLE | 就像JS类中的方法一样，该属性是可配置和可写的，但不可枚举。 |
| JSVM\_METHOD\_NO\_RECEIVER\_CHECK = JSVM\_DEFAULT\_METHOD | JSVM\_NO\_RECEIVER\_CHECK | 无需检查接收者的类方法。 |
| JSVM\_DEFAULT\_JSPROPERTY = JSVM\_WRITABLE | JSVM\_ENUMERABLE | JSVM\_CONFIGURABLE | 就像JavaScript中通过赋值设置的属性一样，属性是可写、可枚举和可配置的。 |
| JSVM\_JSPROPERTY\_NO\_RECEIVER\_CHECK = JSVM\_DEFAULT\_JSPROPERTY | JSVM\_NO\_RECEIVER\_CHECK | 无需检查接收者的对象属性。 |

### JSVM\_ValueType

PhonePC/2in1TabletWearable

```
1. enum JSVM_ValueType
```

**描述**

描述JSVM\_Value的类型。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_UNDEFINED | 未定义类型。 |
| JSVM\_NULL | Null类型。 |
| JSVM\_BOOLEAN | 布尔类型。 |
| JSVM\_NUMBER | 数字类型。 |
| JSVM\_STRING | 字符串类型。 |
| JSVM\_SYMBOL | 符号类型。 |
| JSVM\_OBJECT | 对象类型。 |
| JSVM\_FUNCTION | 函数类型。 |
| JSVM\_EXTERNAL | 外部类型。 |
| JSVM\_BIGINT | bigint类型。 |

### JSVM\_TypedarrayType

PhonePC/2in1TabletWearable

```
1. enum JSVM_TypedarrayType
```

**描述**

描述TypedArray的类型。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_INT8\_ARRAY | int8类型。 |
| JSVM\_UINT8\_ARRAY | uint8类型。 |
| JSVM\_UINT8\_CLAMPED\_ARRAY | uint8固定类型。 |
| JSVM\_INT16\_ARRAY | int16类型。 |
| JSVM\_UINT16\_ARRAY | uint16类型。 |
| JSVM\_INT32\_ARRAY | int32类型。 |
| JSVM\_UINT32\_ARRAY | uint32类型。 |
| JSVM\_FLOAT32\_ARRAY | float32类型。 |
| JSVM\_FLOAT64\_ARRAY | float64类型。 |
| JSVM\_BIGINT64\_ARRAY | bigint64类型。 |
| JSVM\_BIGUINT64\_ARRAY | biguint64类型。 |

### JSVM\_Status

PhonePC/2in1TabletWearable

```
1. enum JSVM_Status
```

**描述**

表示JSVM-API调用成功或失败的完整状态码。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_OK | 成功状态。 |
| JSVM\_INVALID\_ARG | 无效的状态。 |
| JSVM\_OBJECT\_EXPECTED | 期待传入对象类型。 |
| JSVM\_STRING\_EXPECTED | 期望传入字符串类型。 |
| JSVM\_NAME\_EXPECTED | 期望传入名字类型。 |
| JSVM\_FUNCTION\_EXPECTED | 期待传入函数类型。 |
| JSVM\_NUMBER\_EXPECTED | 期待传入数字类型。 |
| JSVM\_BOOLEAN\_EXPECTED | 期待传入布尔类型。 |
| JSVM\_ARRAY\_EXPECTED | 期待传入数组类型。 |
| JSVM\_GENERIC\_FAILURE | 泛型失败状态。 |
| JSVM\_PENDING\_EXCEPTION | 挂起异常状态。 |
| JSVM\_CANCELLED | 取消状态。 |
| JSVM\_ESCAPE\_CALLED\_TWICE | 转义调用了两次。 |
| JSVM\_HANDLE\_SCOPE\_MISMATCH | 句柄作用域不匹配。 |
| JSVM\_CALLBACK\_SCOPE\_MISMATCH | 回调作用域不匹配。 |
| JSVM\_QUEUE\_FULL | 队列满。 |
| JSVM\_CLOSING | 关闭中。 |
| JSVM\_BIGINT\_EXPECTED | 期望传入Bigint类型。 |
| JSVM\_DATE\_EXPECTED | 期望传入日期类型。 |
| JSVM\_ARRAYBUFFER\_EXPECTED | 期望传入ArrayBuffer类型。 |
| JSVM\_DETACHABLE\_ARRAYBUFFER\_EXPECTED | 可分离的数组缓冲区预期状态。 |
| JSVM\_WOULD\_DEADLOCK | 将死锁状态。 |
| JSVM\_NO\_EXTERNAL\_BUFFERS\_ALLOWED | 不允许外部缓冲区。 |
| JSVM\_CANNOT\_RUN\_JS | 不能执行JS。 |
| JSVM\_INVALID\_TYPE | 传入的参数为非法类型。  **起始版本：** 18 |
| JSVM\_JIT\_MODE\_EXPECTED | 无 JIT 权限。  **起始版本：** 18 |

### JSVM\_KeyCollectionMode

PhonePC/2in1TabletWearable

```
1. enum JSVM_KeyCollectionMode
```

**描述**

限制查找属性的范围。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_KEY\_INCLUDE\_PROTOTYPES | 也包含对象原型链上的属性。 |
| JSVM\_KEY\_OWN\_ONLY | 仅包含对象自身属性。 |

### JSVM\_KeyFilter

PhonePC/2in1TabletWearable

```
1. enum JSVM_KeyFilter
```

**描述**

属性过滤器，可以通过使用or来构造一个复合过滤器。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_KEY\_ALL\_PROPERTIES = 0 | 所有属性的键。 |
| JSVM\_KEY\_WRITABLE = 1 | 可写的键。 |
| JSVM\_KEY\_ENUMERABLE = 1 << 1 | 可枚举的键。 |
| JSVM\_KEY\_CONFIGURABLE = 1 << 2 | 可配置的键。 |
| JSVM\_KEY\_SKIP\_STRINGS = 1 << 3 | 排除字符串类型的键。 |
| JSVM\_KEY\_SKIP\_SYMBOLS = 1 << 4 | 排除符号类型的键。 |

### JSVM\_KeyConversion

PhonePC/2in1TabletWearable

```
1. enum JSVM_KeyConversion
```

**描述**

键转换选项。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_KEY\_KEEP\_NUMBERS | 将返回整数索引的数字。 |
| JSVM\_KEY\_NUMBERS\_TO\_STRINGS | 将整数索引转换为字符串。 |

### JSVM\_MemoryPressureLevel

PhonePC/2in1TabletWearable

```
1. enum JSVM_MemoryPressureLevel
```

**描述**

内存压力水平。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_MEMORY\_PRESSURE\_LEVEL\_NONE | 无压力。 |
| JSVM\_MEMORY\_PRESSURE\_LEVEL\_MODERATE | 中等压力。 |
| JSVM\_MEMORY\_PRESSURE\_LEVEL\_CRITICAL | 临界压力。 |
| JSVM\_MEMORY\_PRESSURE\_LEVEL\_LOW\_MEMORY | 通知系统内存不足。  警告：这对垃圾回收性能有很强的负面影响。  建议：使用其他值来影响垃圾回收计划。  **起始版本：** 22 |

### JSVM\_CompileMode

PhonePC/2in1TabletWearable

```
1. enum JSVM_CompileMode
```

**描述**

当 id 为 JSVM\_COMPILE\_MODE 时，content 类型的每个值代表一种编译模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_COMPILE\_MODE\_DEFAULT | 默认编译模式。 |
| JSVM\_COMPILE\_MODE\_CONSUME\_CODE\_CACHE | 使用代码缓存的模式。 |
| JSVM\_COMPILE\_MODE\_EAGER\_COMPILE | 激进编译模式。 |
| JSVM\_COMPILE\_MODE\_PRODUCE\_COMPILE\_PROFILE | 生成编译依赖的模式。 |
| JSVM\_COMPILE\_MODE\_CONSUME\_COMPILE\_PROFILE | 使用编译依赖的模式。 |

### JSVM\_CompileOptionId

PhonePC/2in1TabletWearable

```
1. enum JSVM_CompileOptionId
```

**描述**

JSVM\_CompileOptions 中的 id 对应类型，每个值有对应的 content 类型。JSVM\_COMPILE\_ENABLE\_SOURCE\_MAP 的类型为 bool，当 JSVM\_ScriptOrigin 中的 sourceMapUrl 不为空时生效。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_COMPILE\_MODE | JSVM编译模式。 |
| JSVM\_COMPILE\_CODE\_CACHE | JSVM代码缓存。 |
| JSVM\_COMPILE\_SCRIPT\_ORIGIN | JSVM脚本来源。 |
| JSVM\_COMPILE\_COMPILE\_PROFILE | JSVM编译依赖。 |
| JSVM\_COMPILE\_ENABLE\_SOURCE\_MAP | JSVM的 Source Map 的使能情况。 |

### JSVM\_RegExpFlags

PhonePC/2in1TabletWearable

```
1. enum JSVM_RegExpFlags
```

**描述**

正则表达式标志位。它们可以用来启用一组标志。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_REGEXP\_NONE = 0 | None模式。 |
| JSVM\_REGEXP\_GLOBAL = 1 << 0 | Global模式。 |
| JSVM\_REGEXP\_IGNORE\_CASE = 1 << 1 | Ignore Case模式。 |
| JSVM\_REGEXP\_MULTILINE = 1 << 2 | Multiline模式。 |
| JSVM\_REGEXP\_STICKY = 1 << 3 | Sticky模式。 |
| JSVM\_REGEXP\_UNICODE = 1 << 4 | Unicode模式。 |
| JSVM\_REGEXP\_DOT\_ALL = 1 << 5 | dotAll模式。 |
| JSVM\_REGEXP\_LINEAR = 1 << 6 | Linear模式。 |
| JSVM\_REGEXP\_HAS\_INDICES = 1 << 7 | Has Indices模式。 |
| JSVM\_REGEXP\_UNICODE\_SETS = 1 << 8 | Unicode Sets模式。 |

### JSVM\_InitializedFlag

PhonePC/2in1TabletWearable

```
1. enum JSVM_InitializedFlag
```

**描述**

初始化方式的标志位。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_ZERO\_INITIALIZED | 初始化为0。 |
| JSVM\_UNINITIALIZED | 不做初始化。 |

### JSVM\_WasmOptLevel

PhonePC/2in1TabletWearable

```
1. enum JSVM_WasmOptLevel
```

**描述**

WebAssembly 函数优化等级。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_WASM\_OPT\_BASELINE = 10 | baseline 优化等级。 |
| JSVM\_WASM\_OPT\_HIGH = 20 | 高优化等级。 |

### JSVM\_CacheType

PhonePC/2in1TabletWearable

```
1. enum JSVM_CacheType
```

**描述**

缓存类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_CACHE\_TYPE\_JS | JS 缓存, 由接口 OH\_JSVM\_CreateCodeCache 生成。 |
| JSVM\_CACHE\_TYPE\_WASM | WebAssembly 缓存, 由接口 OH\_JSVM\_CreateWasmCache 生成。 |

### JSVM\_MicrotaskPolicy

PhonePC/2in1TabletWearable

```
1. enum JSVM_MicrotaskPolicy
```

**描述**

JSVM 微任务执行策略。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_MICROTASK\_EXPLICIT = 0 | 调用 OH\_JSVM\_PerformMicrotaskCheckpoint 方法后微任务执行。 |
| JSVM\_MICROTASK\_AUTO | JS 调用栈为 0 时自动执行微任务。默认模式。 |

### JSVM\_TraceCategory

PhonePC/2in1TabletWearable

```
1. enum JSVM_TraceCategory
```

**描述**

JSVM 内部 Trace 事件的类别。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_TRACE\_VM | 采集 JSVM 主要接口调用, 例如执行 js 脚本。 |
| JSVM\_TRACE\_COMPILE | 采集编译相关的接口调用, 例如后台编译。 |
| JSVM\_TRACE\_EXECUTE | 采集与运行状态相关的接口调用, 例如中断与微任务。 |
| JSVM\_TRACE\_RUNTIME | 采集外部函数调用相关信息。 |
| JSVM\_TRACE\_STACK\_TRACE | 采集 JSVM 中堆栈相关信息。 |
| JSVM\_TRACE\_WASM | 采集主要的 WASM 相关接口调用, 例如编译与实例化 WASM 模块。 |
| JSVM\_TRACE\_WASM\_DETAILED | 采集更多更细节的 WASM 相关接口调用，例如后台编译、跳板编译。 |

### JSVM\_CBTriggerTimeForGC

PhonePC/2in1TabletWearable

```
1. enum JSVM_CBTriggerTimeForGC
```

**描述**

触发回调函数的时机。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_CB\_TRIGGER\_BEFORE\_GC | 在GC之前触发回调函数。 |
| JSVM\_CB\_TRIGGER\_AFTER\_GC | 在GC之后触发回调函数。 |

### JSVM\_GCType

PhonePC/2in1TabletWearable

```
1. enum JSVM_GCType
```

**描述**

GC类型。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_GC\_TYPE\_SCAVENGE = 1 << 0 | GC算法为Scavenge。 |
| JSVM\_GC\_TYPE\_MINOR\_MARK\_COMPACT = 1 << 1 | GC算法为Minor-Mark-Compact。 |
| JSVM\_GC\_TYPE\_MARK\_SWEEP\_COMPACT = 1 << 2 | GC算法为Mark-Sweep-Compact。 |
| JSVM\_GC\_TYPE\_INCREMENTAL\_MARKING = 1 << 3 | GC算法为Incremental-Marking。 |
| JSVM\_GC\_TYPE\_PROCESS\_WEAK\_CALLBACKS = 1 << 4 | GC算法为Weak-Callbacks。 |
| JSVM\_GC\_TYPE\_ALL = JSVM\_GC\_TYPE\_SCAVENGE | JSVM\_GC\_TYPE\_MINOR\_MARK\_COMPACT | JSVM\_GC\_TYPE\_MARK\_SWEEP\_COMPACT | JSVM\_GC\_TYPE\_INCREMENTAL\_MARKING | JSVM\_GC\_TYPE\_PROCESS\_WEAK\_CALLBACKS | 包含所有类型的GC算法。 |

### JSVM\_GCCallbackFlags

PhonePC/2in1TabletWearable

```
1. enum JSVM_GCCallbackFlags
```

**描述**

GC回调函数标记。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_NO\_GC\_CALLBACK\_FLAGS | 无回调函数标记。 |
| JSVM\_GC\_CALLBACK\_CONSTRUCT\_RETAINED\_OBJECT\_INFOS | 垃圾回收回调中将构建保留对象信息。 |
| JSVM\_GC\_CALLBACK\_FORCED | 强制执行垃圾回收回调。 |
| JSVM\_GC\_CALLBACK\_SYNCHRONOUS\_PHANTOM\_CALLBACK\_PROCESSING | 同步处理幽灵对象回调。 |
| JSVM\_GC\_CALLBACK\_COLLECT\_ALL\_AVAILABLE\_GARBAGE | 垃圾回收过程中会收集所有可用的垃圾对象。 |
| JSVM\_GC\_CALLBACK\_COLLECT\_ALL\_EXTERNAL\_MEMORY | 垃圾回收时会收集所有的外部内存。 |
| JSVM\_GC\_CALLBACK\_SCHEDULE\_IDLE\_GARBAGE\_COLLECTION | 在空闲时调度垃圾回收。 |

### JSVM\_PromiseRejectEvent

PhonePC/2in1TabletWearable

```
1. enum JSVM_PromiseRejectEvent
```

**描述**

promise-reject事件。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_PROMISE\_REJECT\_OTHER\_REASONS = 0 | Promise被拒绝，但拒绝的原因未知或不明确。 |
| JSVM\_PROMISE\_REJECT\_WITH\_NO\_HANDLER = 1 | Promise被拒绝但没有处理程序。 |
| JSVM\_PROMISE\_ADD\_HANDLER\_AFTER\_REJECTED = 2 | Promise已被拒绝后，再添加处理程序。 |
| JSVM\_PROMISE\_REJECT\_AFTER\_RESOLVED = 3 | Promise已被解决后，再尝试拒绝该Promise。 |
| JSVM\_PROMISE\_RESOLVE\_AFTER\_RESOLVED = 4 | Promise已被解决后，再尝试解决该Promise。 |

### JSVM\_MessageErrorLevel

PhonePC/2in1TabletWearable

```
1. enum JSVM_MessageErrorLevel
```

**描述**

message的报错级别。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_MESSAGE\_LOG = (1 << 0) | Log级别的信息。 |
| JSVM\_MESSAGE\_DEBUG = (1 << 1) | Debug级别的信息。 |
| JSVM\_MESSAGE\_INFO = (1 << 2) | Info级别的信息。 |
| JSVM\_MESSAGE\_ERROR = (1 << 3) | Error级别的信息。 |
| JSVM\_MESSAGE\_WARNING = (1 << 4) | Warning级别的信息。 |
| JSVM\_MESSAGE\_ALL = JSVM\_MESSAGE\_LOG | JSVM\_MESSAGE\_DEBUG | JSVM\_MESSAGE\_INFO | JSVM\_MESSAGE\_ERROR | JSVM\_MESSAGE\_WARNING | 所有级别的信息。 |

### JSVM\_DefineClassOptionsId

PhonePC/2in1TabletWearable

```
1. enum JSVM_DefineClassOptionsId
```

**描述**

定义Class的选项ID。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_DEFINE\_CLASS\_NORMAL | 在常规模式下定义Class。 |
| JSVM\_DEFINE\_CLASS\_WITH\_COUNT | 为所创建的Class预留指定数量的interfield槽位，在这些槽位中可以存放native-data。 |
| JSVM\_DEFINE\_CLASS\_WITH\_PROPERTY\_HANDLER | 为所创建的Class设置监听拦截属性以及设置作为函数调用时回调函数。 |

### JSVM\_DebugOption

PhonePC/2in1TabletWearable

```
1. enum JSVM_DebugOption
```

**描述**

调试选项。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| JSVM\_SCOPE\_CHECK | scope校验功能。 |

## 函数说明

PhonePC/2in1TabletWearable

### JSVM\_Finalize()

PhonePC/2in1TabletWearable

```
1. typedef void (JSVM_CDECL* JSVM_Finalize)(JSVM_Env env,void* finalizeData,void* finalizeHint)
```

**描述**

函数指针类型，当native类型对象或数据与JS对象被关联时，传入该指针。该函数将会在关联的JS对象被GC回收时被调用，用以执行native的清理动作。

**起始版本：** 11

### JSVM\_OutputStream()

PhonePC/2in1TabletWearable

```
1. typedef bool (JSVM_CDECL* JSVM_OutputStream)(const char* data,int size,void* streamData)
```

**描述**

ASCII输出流回调的函数指针类型。参数data是指输出的数据指针。参数size是指输出的数据大小。空数据指针指示流的结尾。参数streamData是指与回调一起传递给API函数的指针，该API函数向输出流生成数据。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回true表示流可以继续接收数据，返回false将中止流。 |

### JSVM\_HandlerForGC()

PhonePC/2in1TabletWearable

```
1. typedef void (JSVM_CDECL* JSVM_HandlerForGC)(JSVM_VM vm, JSVM_GCType gcType, JSVM_GCCallbackFlags flags, void* data)
```

**描述**

GC回调的函数指针类型。

**起始版本：** 18

### JSVM\_HandlerForOOMError()

PhonePC/2in1TabletWearable

```
1. typedef void (JSVM_CDECL* JSVM_HandlerForOOMError)(const char* location,const char* detail,bool isHeapOOM)
```

**描述**

OOM-Error回调的函数指针类型。

**起始版本：** 18

### JSVM\_HandlerForFatalError()

PhonePC/2in1TabletWearable

```
1. typedef void (JSVM_CDECL* JSVM_HandlerForFatalError)(const char* location,const char* message)
```

**描述**

Fatal-Error回调的函数指针类型。

**起始版本：** 18

### JSVM\_HandlerForPromiseReject()

PhonePC/2in1TabletWearable

```
1. typedef void (JSVM_CDECL* JSVM_HandlerForPromiseReject)(JSVM_Env env, JSVM_PromiseRejectEvent rejectEvent, JSVM_Value rejectInfo)
```

**描述**

Promise-Reject回调的函数指针类型。

**起始版本：** 18
