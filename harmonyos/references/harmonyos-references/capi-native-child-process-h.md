---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-child-process-h
title: native_child_process.h
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 头文件 > native_child_process.h
category: harmonyos-references
scraped_at: 2026-04-28T07:58:59+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:db12cd95fe8480142f12d5591be88d9a5f4145358118fbe6887d15b06026d91b
---

## 概述

PhonePC/2in1TabletTVWearable

支持创建Native子进程，并在父子进程间建立IPC通道。

通过此模块和[childProcessManager](js-apis-app-ability-childprocessmanager.md)（非SELF\_FORK模式）可以启动的子进程总数最大为512个。

**引用文件：** <AbilityKit/native\_child\_process.h>

**库：** libchild\_process.so

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**相关模块：** [ChildProcess](capi-childprocess.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [NativeChildProcess\_Fd](capi-nativechildprocess-fd.md) | NativeChildProcess\_Fd | 传递给子进程的文件描述符信息。 |
| [NativeChildProcess\_FdList](capi-nativechildprocess-fdlist.md) | NativeChildProcess\_FdList | 传递给子进程的文件描述符信息列表。文件描述符记录个数不能超过16个。 |
| [NativeChildProcess\_Options](capi-nativechildprocess-options.md) | NativeChildProcess\_Options | 子进程所使用的选项。 |
| [NativeChildProcess\_Args](capi-nativechildprocess-args.md) | NativeChildProcess\_Args | 传递给子进程的参数。 |
| [Ability\_ChildProcessConfigs](capi-ability-childprocessconfigs.md) | Ability\_ChildProcessConfigs | 启动子进程的配置信息，包括子进程的进程名、以及数据沙箱与网络环境的共享模式。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Ability\_NativeChildProcess\_ErrCode](capi-native-child-process-h.md#ability_nativechildprocess_errcode) | Ability\_NativeChildProcess\_ErrCode | 定义Native子进程模块错误码。 |
| [NativeChildProcess\_IsolationMode](capi-native-child-process-h.md#nativechildprocess_isolationmode) | NativeChildProcess\_IsolationMode | 定义Native子进程数据沙箱与网络环境的共享模式。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Ability\_ChildProcessConfigs\* OH\_Ability\_CreateChildProcessConfigs()](capi-native-child-process-h.md#oh_ability_createchildprocessconfigs) | - | 创建一个子进程配置信息对象。创建对象成功后需要通过调用[OH\_Ability\_DestroyChildProcessConfigs](capi-native-child-process-h.md#oh_ability_destroychildprocessconfigs)来销毁对象从而避免内存泄漏。 |
| [Ability\_NativeChildProcess\_ErrCode OH\_Ability\_DestroyChildProcessConfigs(Ability\_ChildProcessConfigs\* configs)](capi-native-child-process-h.md#oh_ability_destroychildprocessconfigs) | - | 销毁一个子进程配置信息对象，并释放其内存，在调用该接口后，要避免继续使用已销毁的configs对象。 |
| [Ability\_NativeChildProcess\_ErrCode OH\_Ability\_ChildProcessConfigs\_SetIsolationMode(Ability\_ChildProcessConfigs\* configs, NativeChildProcess\_IsolationMode isolationMode)](capi-native-child-process-h.md#oh_ability_childprocessconfigs_setisolationmode) | - | 设置子进程配置信息对象的数据沙箱与网络环境的共享模式，详见[NativeChildProcess\_IsolationMode](capi-native-child-process-h.md#nativechildprocess_isolationmode)。该设置仅当调用[OH\_Ability\_StartNativeChildProcessWithConfigs](capi-native-child-process-h.md#oh_ability_startnativechildprocesswithconfigs)、[OH\_Ability\_CreateNativeChildProcessWithConfigs](capi-native-child-process-h.md#oh_ability_createnativechildprocesswithconfigs)接口时生效。 |
| [Ability\_NativeChildProcess\_ErrCode OH\_Ability\_ChildProcessConfigs\_SetProcessName(Ability\_ChildProcessConfigs\* configs,const char\* processName)](capi-native-child-process-h.md#oh_ability_childprocessconfigs_setprocessname) | - | 设置子进程配置信息对象中的进程名称。 |
| [typedef void (\*OH\_Ability\_OnNativeChildProcessStarted)(int errCode, OHIPCRemoteProxy \*remoteProxy)](capi-native-child-process-h.md#oh_ability_onnativechildprocessstarted) | OH\_Ability\_OnNativeChildProcessStarted | 通知子进程启动结果的回调函数。 |
| [int OH\_Ability\_CreateNativeChildProcess(const char\* libName,OH\_Ability\_OnNativeChildProcessStarted onProcessStarted)](capi-native-child-process-h.md#oh_ability_createnativechildprocess) | - | 创建子进程并加载参数中指定的动态链接库文件，进程启动结果通过回调参数异步通知，需注意回调通知为独立线程，回调函数实现需要注意线程同步，且不能执行高耗时操作避免长时间阻塞。参数所指定的动态库必须实现并导出下列函数：  1. OHIPCRemoteStub\* NativeChildProcess\_OnConnect()  2. void NativeChildProcess\_MainProc()  处理逻辑顺序如下列伪代码所示：  主进程：  1. OH\_Ability\_CreateNativeChildProcess(libName, onProcessStartedCallback)  子进程：  2. dlopen(libName)  3. dlsym("NativeChildProcess\_OnConnect")  4. dlsym("NativeChildProcess\_MainProc")  5. ipcRemote = NativeChildProcess\_OnConnect()  6. NativeChildProcess\_MainProc()  主进程：  7. onProcessStartedCallback(ipcRemote, errCode)  子进程：  8. 在NativeChildProcess\_MainProc()函数返回后子进程退出。  **设备行为差异：** 对于API 13及之前版本，该接口在PC/2in1中可正常使用，在其他设备中返回[NCP\_ERR\_NOT\_SUPPORTED](capi-native-child-process-h.md#ability_nativechildprocess_errcode)错误码。对于API 14及之后版本，该接口在PC/2in1、Tablet设备可正常使用，在其他设备中返回[NCP\_ERR\_NOT\_SUPPORTED](capi-native-child-process-h.md#ability_nativechildprocess_errcode)错误码。  **说明：** 对于API 14及之前版本，单个进程只能启动1个Native子进程。从API 15开始，单个进程最多支持启动50个Native子进程。 |
| [Ability\_NativeChildProcess\_ErrCode OH\_Ability\_CreateNativeChildProcessWithConfigs(const char\* libName,Ability\_ChildProcessConfigs\* configs, OH\_Ability\_OnNativeChildProcessStarted onProcessStarted)](capi-native-child-process-h.md#oh_ability_createnativechildprocesswithconfigs) | - | 根据传入的子进程配置信息创建子进程，并加载参数中指定的动态链接库文件。子进程的启动结果通过回调参数异步通知调用方。该回调在独立线程中执行，需要确保线程同步，且不能执行高耗时操作避免长时间阻塞。参数所指定的动态库必须实现并导出下列函数：  1. OHIPCRemoteStub\* NativeChildProcess\_OnConnect()  2. void NativeChildProcess\_MainProc()  处理逻辑顺序如下列伪代码所示：  主进程：  1. OH\_Ability\_CreateNativeChildProcessWithConfigs(libName, configs, onProcessStartedCallback)  子进程：  2. dlopen(libName)  3. dlsym("NativeChildProcess\_OnConnect")  4. dlsym("NativeChildProcess\_MainProc")  5. ipcRemote = NativeChildProcess\_OnConnect()  6. NativeChildProcess\_MainProc()  主进程：  7. onProcessStartedCallback(ipcRemote, errCode)  子进程：  8.  在NativeChildProcess\_MainProc()函数返回后子进程退出。  **设备行为差异：** 该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回[NCP\_ERR\_NOT\_SUPPORTED](capi-native-child-process-h.md#ability_nativechildprocess_errcode)错误码。 |
| [Ability\_NativeChildProcess\_ErrCode OH\_Ability\_StartNativeChildProcess(const char\* entry, NativeChildProcess\_Args args,NativeChildProcess\_Options options, int32\_t \*pid)](capi-native-child-process-h.md#oh_ability_startnativechildprocess) | - | 启动一个子进程，并加载指定的动态链接库文件。指定的动态库必须实现一个以NativeChildProcess\_Args为参数的函数（函数名称可自定义），并导出该函数。示例如下：  1. void Main(NativeChildProcess\_Args args);  处理逻辑顺序如下列伪代码所示：  主进程：  1. OH\_Ability\_StartNativeChildProcess(entryPoint, args, options)  子进程：  2. dlopen(libName)  3. dlsym("Main")  4. Main(args)  5. 子进程将在Main(args)函数返回后退出。  **设备行为差异：** 对于API 13及之前版本，该接口在PC/2in1设备中可正常使用，在其他设备类型中返回[NCP\_ERR\_NOT\_SUPPORTED](capi-native-child-process-h.md#ability_nativechildprocess_errcode)错误码。对于API 14及之后版本，该接口在PC/2in1、Tablet中可正常使用，在其他设备类型中返回[NCP\_ERR\_NOT\_SUPPORTED](capi-native-child-process-h.md#ability_nativechildprocess_errcode)错误码。 |
| [Ability\_NativeChildProcess\_ErrCode OH\_Ability\_StartNativeChildProcessWithConfigs(const char\* entry, NativeChildProcess\_Args args, Ability\_ChildProcessConfigs\* configs, int32\_t \*pid)](capi-native-child-process-h.md#oh_ability_startnativechildprocesswithconfigs) | - | 根据参数中子进程配置信息启动Native子进程，加载参数中指定的动态链接库文件并调用入口函数。支持传参到子进程。指定的动态库必须实现一个以NativeChildProcess\_Args为参数的函数（函数名称可自定义），并导出该函数。示例如下：  1. void Main(NativeChildProcess\_Args args);  处理逻辑顺序如下列伪代码所示：  主进程：  1. OH\_Ability\_StartNativeChildProcessWithConfigs(entryPoint, args, configs, &pid)  子进程：  2. dlopen(libName)  3. dlsym("Main")  4. Main(args)  5. 子进程将在Main(args)函数返回后退出。  **设备行为差异：** 该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回[NCP\_ERR\_NOT\_SUPPORTED](capi-native-child-process-h.md#ability_nativechildprocess_errcode)错误码。 |
| [NativeChildProcess\_Args\* OH\_Ability\_GetCurrentChildProcessArgs()](capi-native-child-process-h.md#oh_ability_getcurrentchildprocessargs) | - | 子进程获取自身的启动参数。 |
| [typedef void (\*OH\_Ability\_OnNativeChildProcessExit)(int32\_t pid, int32\_t signal)](capi-native-child-process-h.md#oh_ability_onnativechildprocessexit) | OH\_Ability\_OnNativeChildProcessExit | 获取子进程退出信息。 |
| [Ability\_NativeChildProcess\_ErrCode OH\_Ability\_RegisterNativeChildProcessExitCallback(OH\_Ability\_OnNativeChildProcessExit onProcessExit)](capi-native-child-process-h.md#oh_ability_registernativechildprocessexitcallback) | - | 注册子进程退出回调。只有[OH\_Ability\_StartNativeChildProcess](capi-native-child-process-h.md#oh_ability_startnativechildprocess)、[OH\_Ability\_StartNativeChildProcessWithConfigs](capi-native-child-process-h.md#oh_ability_startnativechildprocesswithconfigs)和[@ohos.app.ability.childProcessManager的startNativeChildProcess](js-apis-app-ability-childprocessmanager.md#childprocessmanagerstartnativechildprocess13)启动的子进程退出时才会触发所注册的回调函数。重复注册同一个回调函数只会保留一个。 |
| [Ability\_NativeChildProcess\_ErrCode OH\_Ability\_UnregisterNativeChildProcessExitCallback(OH\_Ability\_OnNativeChildProcessExit onProcessExit)](capi-native-child-process-h.md#oh_ability_unregisternativechildprocessexitcallback) | - | 解注册子进程退出回调。 |
| [Ability\_NativeChildProcess\_ErrCode OH\_Ability\_ChildProcessConfigs\_SetIsolationUid(Ability\_ChildProcessConfigs\* configs, bool enableIsolationUid)](capi-native-child-process-h.md#oh_ability_childprocessconfigs_setisolationuid) | - | 设置子进程配置信息对象的uid是否隔离。该设置仅在NativeChildProcess\_IsolationMode为NCP\_ISOLATION\_MODE\_ISOLATED时生效。 |
| [Ability\_NativeChildProcess\_ErrCode OH\_Ability\_KillChildProcess(int32\_t pid)](capi-native-child-process-h.md#oh_ability_killchildprocess) | - | 终止当前进程创建的子进程。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### Ability\_NativeChildProcess\_ErrCode

PhonePC/2in1TabletTVWearable

```
1. enum Ability_NativeChildProcess_ErrCode
```

**描述**

定义Native子进程模块错误码。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| NCP\_NO\_ERROR = 0 | 操作成功。 |
| NCP\_ERR\_INVALID\_PARAM = 401 | 无效参数。 |
| NCP\_ERR\_NOT\_SUPPORTED = 801 | 不支持创建Native子进程。 |
| NCP\_ERR\_INTERNAL = 16000050 | 内部错误。 |
| NCP\_ERR\_BUSY = 16010001 | 在Native子进程的启动过程中不能再次创建新的子进程，可以等待当前子进程启动完成后再次尝试。从API version 15开始被废弃。 |
| NCP\_ERR\_TIMEOUT = 16010002 | 启动Native子进程超时。 |
| NCP\_ERR\_SERVICE\_ERROR = 16010003 | 服务端出错。 |
| NCP\_ERR\_MULTI\_PROCESS\_DISABLED = 16010004 | 多进程模式已关闭，不允许启动子进程。 |
| NCP\_ERR\_ALREADY\_IN\_CHILD = 16010005 | 不允许在子进程中再次创建进程。 |
| NCP\_ERR\_MAX\_CHILD\_PROCESSES\_REACHED = 16010006 | 到达最大Native子进程数量限制，不能再创建子进程。 |
| NCP\_ERR\_LIB\_LOADING\_FAILED = 16010007 | 子进程加载动态库失败，文件不存在或者未实现对应的方法并导出。 |
| NCP\_ERR\_CONNECTION\_FAILED = 16010008 | 子进程调用动态库的OnConnect方法失败，可能返回了无效的IPC对象指针。 |
| NCP\_ERR\_CALLBACK\_NOT\_EXIST = 16010009 | 父进程调用解注册Native子进程退出回调，未找到注册的回调函数。  **起始版本：** 20 |
| NCP\_ERR\_INVALID\_PID = 16010010 | 该进程pid不存在，或并非当前进程的子进程pid，或属于[childProcessManager.startChildProcess](js-apis-app-ability-childprocessmanager.md#childprocessmanagerstartchildprocess)接口在SELF\_FORK模式下启动的子进程。  **起始版本：** 22 |

### NativeChildProcess\_IsolationMode

PhonePC/2in1TabletTVWearable

```
1. enum NativeChildProcess_IsolationMode
```

**描述**

定义Native子进程数据沙箱与网络环境的共享模式。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| NCP\_ISOLATION\_MODE\_NORMAL = 0 | 普通隔离模式下，父进程与子进程共享同一沙箱环境或网络环境。 |
| NCP\_ISOLATION\_MODE\_ISOLATED = 1 | 在隔离模式下，父进程与子进程不共享同一沙箱环境或网络环境。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Ability\_CreateChildProcessConfigs()

PhonePC/2in1TabletTVWearable

```
1. Ability_ChildProcessConfigs* OH_Ability_CreateChildProcessConfigs()
```

**描述**

创建一个子进程配置信息对象。创建对象成功后需要通过调用[OH\_Ability\_DestroyChildProcessConfigs](capi-native-child-process-h.md#oh_ability_destroychildprocessconfigs)来销毁对象从而避免内存泄漏。

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Ability\_ChildProcessConfigs](capi-ability-childprocessconfigs.md)\* | 返回一个指向[Ability\_ChildProcessConfigs](capi-ability-childprocessconfigs.md)对象的指针 - 子进程配置信息对象创建成功。  返回nullptr - 发生内部错误或者内存分配失败。 |

### OH\_Ability\_DestroyChildProcessConfigs()

PhonePC/2in1TabletTVWearable

```
1. Ability_NativeChildProcess_ErrCode OH_Ability_DestroyChildProcessConfigs(Ability_ChildProcessConfigs* configs)
```

**描述**

销毁一个子进程配置信息对象，并释放其内存，在调用该接口后，要避免继续使用已销毁的configs对象。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Ability\_ChildProcessConfigs](capi-ability-childprocessconfigs.md)\* configs | 需要销毁的子进程配置信息对象指针。在调用该接口后，对象指针将失效，避免继续使用该指针。允许传入空指针，空指针不会触发任何操作。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Ability\_NativeChildProcess\_ErrCode](capi-native-child-process-h.md#ability_nativechildprocess_errcode) | NCP\_NO\_ERROR - 操作成功。  NCP\_ERR\_INVALID\_PARAM - 传入参数为nullptr。 |

### OH\_Ability\_ChildProcessConfigs\_SetIsolationMode()

PhonePC/2in1TabletTVWearable

```
1. Ability_NativeChildProcess_ErrCode OH_Ability_ChildProcessConfigs_SetIsolationMode(Ability_ChildProcessConfigs* configs, NativeChildProcess_IsolationMode isolationMode)
```

**描述**

设置子进程配置信息对象的数据沙箱与网络环境的共享模式，详见[NativeChildProcess\_IsolationMode](capi-native-child-process-h.md#nativechildprocess_isolationmode)。该设置仅当调用[OH\_Ability\_StartNativeChildProcessWithConfigs](capi-native-child-process-h.md#oh_ability_startnativechildprocesswithconfigs)、[OH\_Ability\_CreateNativeChildProcessWithConfigs](capi-native-child-process-h.md#oh_ability_createnativechildprocesswithconfigs)接口时生效。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Ability\_ChildProcessConfigs](capi-ability-childprocessconfigs.md)\* configs | 子进程的配置信息对象指针。不可以为空指针。 |
| [NativeChildProcess\_IsolationMode](capi-native-child-process-h.md#nativechildprocess_isolationmode) isolationMode | 要设置的数据沙箱与网络环境的共享模式，详见NativeChildProcess\_IsolationMode。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Ability\_NativeChildProcess\_ErrCode](capi-native-child-process-h.md#ability_nativechildprocess_errcode) | NCP\_NO\_ERROR - 执行成功。  NCP\_ERR\_INVALID\_PARAM - 传入参数configs为nullptr。 |

### OH\_Ability\_ChildProcessConfigs\_SetIsolationUid()

PhonePC/2in1TabletTVWearable

```
1. Ability_NativeChildProcess_ErrCode OH_Ability_ChildProcessConfigs_SetIsolationUid(Ability_ChildProcessConfigs* configs, bool isolationUid)
```

**描述**

设置子进程配置信息对象的uid是否隔离。例如用于浏览器的安全加固场景，设置主进程与子进程的uid隔离。

该设置仅在NativeChildProcess\_IsolationMode为NCP\_ISOLATION\_MODE\_ISOLATED时生效。不调用该接口设置isolationUid时，则默认为false，即子进程与主进程拥有相同uid。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Ability\_ChildProcessConfigs](capi-ability-childprocessconfigs.md)\* configs | 子进程的配置信息对象指针。不可以为空指针。 |
| bool isolationUid | 控制子进程是否使用独立的uid。true表示子进程拥有独立的uid，false表示子进程与主进程拥有相同uid。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Ability\_NativeChildProcess\_ErrCode](capi-native-child-process-h.md#ability_nativechildprocess_errcode) | NCP\_NO\_ERROR - 执行成功。  NCP\_ERR\_INVALID\_PARAM - 传入参数configs为nullptr。 |

### OH\_Ability\_ChildProcessConfigs\_SetProcessName()

PhonePC/2in1TabletTVWearable

```
1. Ability_NativeChildProcess_ErrCode OH_Ability_ChildProcessConfigs_SetProcessName(Ability_ChildProcessConfigs* configs,const char* processName)
```

**描述**

设置子进程配置信息对象中的进程名称。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Ability\_ChildProcessConfigs](capi-ability-childprocessconfigs.md)\* configs | 子进程的配置信息对象指针。不能为空指针。 |
| const char\* processName | 设置的子进程名字符串必须是非空字符串，并且只能由字母、数字和下划线构成。最大长度为64字符。最终的进程名是{bundleName}:{processName}。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Ability\_NativeChildProcess\_ErrCode](capi-native-child-process-h.md#ability_nativechildprocess_errcode) | NCP\_NO\_ERROR - 执行成功。  NCP\_ERR\_INVALID\_PARAM - 传入参数configs为nullptr，或者processName包含除字母、数字、下划线以外的字符。 |

### OH\_Ability\_OnNativeChildProcessStarted()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_Ability_OnNativeChildProcessStarted)(int errCode, OHIPCRemoteProxy *remoteProxy)
```

**描述**

定义通知子进程启动结果的回调函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int errCode | 回调函数返回的错误码，可用的值如下：  [NCP\_NO\_ERROR](capi-native-child-process-h.md#ability_nativechildprocess_errcode) - 创建子进程成功。  [NCP\_ERR\_LIB\_LOADING\_FAILED](capi-native-child-process-h.md#ability_nativechildprocess_errcode) - 加载动态库文件失败或动态库中未实现必要的导出函数。  [NCP\_ERR\_CONNECTION\_FAILED](capi-native-child-process-h.md#ability_nativechildprocess_errcode) - 动态库中实现的OnConnect方法未返回有效的IPC Stub指针。  详见[Ability\_NativeChildProcess\_ErrCode](capi-native-child-process-h.md#ability_nativechildprocess_errcode)定义。 |
| [OHIPCRemoteProxy](capi-ohipcparcel-ohipcremoteproxy.md) \*remoteProxy | 子进程的IPC对象指针，出现异常时可能为nullptr：使用完毕后需要调用[OH\_IPCRemoteProxy\_Destroy](capi-ipc-cremote-object-h.md#oh_ipcremoteproxy_destroy)方法释放。 |

**参考：**

[OH\_IPCRemoteProxy\_Destroy](capi-ipc-cremote-object-h.md#oh_ipcremoteproxy_destroy)

### OH\_Ability\_CreateNativeChildProcess()

PhonePC/2in1TabletTVWearable

```
1. int OH_Ability_CreateNativeChildProcess(const char* libName,OH_Ability_OnNativeChildProcessStarted onProcessStarted)
```

**描述**

创建子进程并加载参数中指定的动态链接库文件，进程启动结果通过回调参数异步通知，需注意回调通知为独立线程，回调函数实现需要注意线程同步，且不能执行高耗时操作避免长时间阻塞。

参数所指定的动态库必须实现并导出下列函数：

1. OHIPCRemoteStub\* NativeChildProcess\_OnConnect()

2. void NativeChildProcess\_MainProc()

处理逻辑顺序如下列伪代码所示：

主进程：

1. OH\_Ability\_CreateNativeChildProcess(libName, onProcessStartedCallback)

子进程：

2. dlopen(libName)

3. dlsym("NativeChildProcess\_OnConnect")

4. dlsym("NativeChildProcess\_MainProc")

5. ipcRemote = NativeChildProcess\_OnConnect()

6. NativeChildProcess\_MainProc()

主进程：

7. onProcessStartedCallback(ipcRemote, errCode)

子进程：

8. 在NativeChildProcess\_MainProc()函数返回后子进程退出。

**设备行为差异：** 对于API version 13及之前版本，该接口在PC/2in1中可正常使用，在其他设备中返回[NCP\_ERR\_NOT\_SUPPORTED](capi-native-child-process-h.md#ability_nativechildprocess_errcode)错误码。对于API version 14及之后版本，该接口在PC/2in1、Tablet设备可正常使用，在其他设备中返回[NCP\_ERR\_NOT\_SUPPORTED](capi-native-child-process-h.md#ability_nativechildprocess_errcode)错误码。

说明

API version 14及之前版本，单个进程只能启动1个Native子进程。从API version 15开始，单个进程最多支持启动50个Native子进程。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* libName | 子进程中加载的动态库文件名称，不能为nullptr。 |
| [OH\_Ability\_OnNativeChildProcessStarted](capi-native-child-process-h.md#oh_ability_onnativechildprocessstarted) onProcessStarted | 通知子进程启动结果的回调函数指针，不能为nullptr。详见[OH\_Ability\_OnNativeChildProcessStarted](capi-native-child-process-h.md#oh_ability_onnativechildprocessstarted)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | [NCP\_NO\_ERROR](capi-native-child-process-h.md#ability_nativechildprocess_errcode) - 调用成功，但子进程的实际启动结果由回调函数通知。  [NCP\_ERR\_INVALID\_PARAM](capi-native-child-process-h.md#ability_nativechildprocess_errcode) - 无效的动态库名称或者回调函数指针。  [NCP\_ERR\_NOT\_SUPPORTED](capi-native-child-process-h.md#ability_nativechildprocess_errcode) - 当前设备不支持创建Native子进程。  [NCP\_ERR\_MULTI\_PROCESS\_DISABLED](capi-native-child-process-h.md#ability_nativechildprocess_errcode) - 当前设备已关闭多进程模式。  [NCP\_ERR\_ALREADY\_IN\_CHILD](capi-native-child-process-h.md#ability_nativechildprocess_errcode) - 不允许在子进程中再次创建子进程。  [NCP\_ERR\_MAX\_CHILD\_PROCESSES\_REACHED](capi-native-child-process-h.md#ability_nativechildprocess_errcode) - 到达最大Native子进程数限制。  详见[Ability\_NativeChildProcess\_ErrCode](capi-native-child-process-h.md#ability_nativechildprocess_errcode)定义。 |

**参考：**

[OH\_Ability\_OnNativeChildProcessStarted](capi-native-child-process-h.md#oh_ability_onnativechildprocessstarted)

### OH\_Ability\_CreateNativeChildProcessWithConfigs()

PhonePC/2in1TabletTVWearable

```
1. Ability_NativeChildProcess_ErrCode OH_Ability_CreateNativeChildProcessWithConfigs(const char* libName,Ability_ChildProcessConfigs* configs, OH_Ability_OnNativeChildProcessStarted onProcessStarted)
```

**描述**

根据传入的子进程配置信息创建子进程，并加载参数中指定的动态链接库文件。子进程的启动结果通过回调参数异步通知调用方。该回调在独立线程中执行，需要确保线程同步，且不能执行高耗时操作避免长时间阻塞。

参数所指定的动态库必须实现并导出下列函数：

1. OHIPCRemoteStub\* NativeChildProcess\_OnConnect()

2. void NativeChildProcess\_MainProc()

处理逻辑顺序如下列伪代码所示：

主进程：

1. OH\_Ability\_CreateNativeChildProcessWithConfigs(libName, configs, onProcessStartedCallback)

子进程：

2. dlopen(libName)

3. dlsym("NativeChildProcess\_OnConnect")

4. dlsym("NativeChildProcess\_MainProc")

5. ipcRemote = NativeChildProcess\_OnConnect()

6. NativeChildProcess\_MainProc()

主进程：

7. onProcessStartedCallback(ipcRemote, errCode)

子进程：

8. 在NativeChildProcess\_MainProc()函数返回后子进程退出。

**设备行为差异：** 该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回[NCP\_ERR\_NOT\_SUPPORTED](capi-native-child-process-h.md#ability_nativechildprocess_errcode)错误码。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* libName | 子进程中加载的动态库文件名称，不能为nullptr。 |
| [Ability\_ChildProcessConfigs](capi-ability-childprocessconfigs.md)\* configs | 子进程的配置信息参数，不能为nullptr。 |
| [OH\_Ability\_OnNativeChildProcessStarted](capi-native-child-process-h.md#oh_ability_onnativechildprocessstarted) onProcessStarted | 通知子进程启动结果的回调函数指针，不能为nullptr，详见OH\_Ability\_OnNativeChildProcessStarted。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Ability\_NativeChildProcess\_ErrCode](capi-native-child-process-h.md#ability_nativechildprocess_errcode) | NCP\_NO\_ERROR - 执行成功。  NCP\_ERR\_INVALID\_PARAM - 传入参数无效。  NCP\_ERR\_NOT\_SUPPORTED - 当前设备不支持创建Native子进程。  NCP\_ERR\_MULTI\_PROCESS\_DISABLED - 当前设备已关闭多进程模式，不允许启动子进程。  NCP\_ERR\_ALREADY\_IN\_CHILD - 不允许在子进程中再次创建子进程。  NCP\_ERR\_MAX\_CHILD\_PROCESSES\_REACHED - 超过最大Native子进程数限制。  详见Ability\_NativeChildProcess\_ErrCode定义。 |

**参考：**

[OH\_Ability\_OnNativeChildProcessStarted](capi-native-child-process-h.md#oh_ability_onnativechildprocessstarted)

### OH\_Ability\_StartNativeChildProcess()

PhonePC/2in1TabletTVWearable

```
1. Ability_NativeChildProcess_ErrCode OH_Ability_StartNativeChildProcess(const char* entry, NativeChildProcess_Args args,NativeChildProcess_Options options, int32_t *pid)
```

**描述**

启动Native子进程，并加载参数中指定的动态链接库文件并调用入口函数。指定的动态库必须实现一个以[NativeChildProcess\_Args](capi-nativechildprocess-args.md)为参数的函数（函数名称可自定义），并导出该函数。支持传参到子进程。子进程中不支持创建ArkTS基础运行时环境。

示例如下：

void Main(NativeChildProcess\_Args args);

处理逻辑顺序如下列伪代码所示：

主进程：

1. OH\_Ability\_StartNativeChildProcess(entryPoint, args, options)

子进程：

2. dlopen(libName)

3. dlsym("Main")

4. Main(args)

5. 子进程将在Main(args)函数返回后退出。

**设备行为差异：** 对于API 13及之前版本，该接口在PC/2in1设备中可正常使用，在其他设备类型中返回[NCP\_ERR\_NOT\_SUPPORTED](capi-native-child-process-h.md#ability_nativechildprocess_errcode)错误码。对于API 14及之后版本，该接口在PC/2in1、Tablet中可正常使用，在其他设备类型中返回[NCP\_ERR\_NOT\_SUPPORTED](capi-native-child-process-h.md#ability_nativechildprocess_errcode)错误码。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* entry | 子进程中加载的动态库及入口函数，例如"libEntry.so:Main"，不能为nullptr。 |
| [NativeChildProcess\_Args](capi-nativechildprocess-args.md) args | 传递给子进程的参数。 |
| [NativeChildProcess\_Options](capi-nativechildprocess-options.md) options | 子进程选项。 |
| int32\_t \*pid | 启动的子进程id。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Ability\_NativeChildProcess\_ErrCode](capi-native-child-process-h.md#ability_nativechildprocess_errcode) | NCP\_NO\_ERROR - 调用成功。  NCP\_ERR\_INVALID\_PARAM - 无效的动态库名称或者回调函数指针。  NCP\_ERR\_NOT\_SUPPORTED - 当前设备不支持创建Native子进程。  NCP\_ERR\_ALREADY\_IN\_CHILD - 当前设备已关闭多进程模式。  NCP\_ERR\_MAX\_CHILD\_PROCESSES\_REACHED - 到达最大Native子进程数限制。  详见Ability\_NativeChildProcess\_ErrCode定义。 |

**参考：**

[OH\_Ability\_OnNativeChildProcessStarted](capi-native-child-process-h.md#oh_ability_onnativechildprocessstarted)

### OH\_Ability\_StartNativeChildProcessWithConfigs()

PhonePC/2in1TabletTVWearable

```
1. Ability_NativeChildProcess_ErrCode OH_Ability_StartNativeChildProcessWithConfigs(const char* entry, NativeChildProcess_Args args, Ability_ChildProcessConfigs* configs, int32_t *pid)
```

**描述**

根据参数中子进程配置信息启动Native子进程，加载参数中指定的动态链接库文件并调用入口函数。支持传参到子进程。指定的动态库必须实现一个以[NativeChildProcess\_Args](capi-nativechildprocess-args.md)为参数的函数（函数名称可自定义），并导出该函数。

示例如下：

void Main(NativeChildProcess\_Args args);

处理逻辑顺序如下列伪代码所示：

主进程：

1. OH\_Ability\_StartNativeChildProcessWithConfigs(entryPoint, args, configs, &pid)

子进程：

2. dlopen(libName)

3. dlsym("Main")

4. Main(args)

5. 子进程将在Main(args)函数返回后退出。

**设备行为差异：** 该接口在PC/2in1、Tablet中可正常调用，在其他设备类型中返回[NCP\_ERR\_NOT\_SUPPORTED](capi-native-child-process-h.md#ability_nativechildprocess_errcode)错误码。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* entry | 子进程中调用动态库的符号和入口函数，中间用“:”隔开（例如“libentry.so:Main”），不能为nullptr。 |
| [NativeChildProcess\_Args](capi-nativechildprocess-args.md) args | 传给子进程的参数。 |
| [Ability\_ChildProcessConfigs](capi-ability-childprocessconfigs.md)\* configs | 子进程的配置信息参数。 |
| int32\_t \*pid | 被启动的子进程号。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Ability\_NativeChildProcess\_ErrCode](capi-native-child-process-h.md#ability_nativechildprocess_errcode) | NCP\_NO\_ERROR - 执行成功。  NCP\_ERR\_INVALID\_PARAM - 传入参数无效。  NCP\_ERR\_NOT\_SUPPORTED - 当前设备不支持创建Native子进程。  NCP\_ERR\_ALREADY\_IN\_CHILD - 不允许在子进程中再次创建子进程。  NCP\_ERR\_MAX\_CHILD\_PROCESSES\_REACHED - 超过最大Native子进程数限制。  详见Ability\_NativeChildProcess\_ErrCode定义。 |

### OH\_Ability\_GetCurrentChildProcessArgs()

PhonePC/2in1TabletTVWearable

```
1. NativeChildProcess_Args* OH_Ability_GetCurrentChildProcessArgs()
```

**描述**

通过[OH\_Ability\_StartNativeChildProcess](capi-native-child-process-h.md#oh_ability_startnativechildprocess)启动子进程后，子进程能够在任意so和任意子线程中获取启动参数[NativeChildProcess\_Args](capi-nativechildprocess-args.md)。

**起始版本：** 17

**返回：**

| 类型 | 说明 |
| --- | --- |
| [NativeChildProcess\_Args](capi-nativechildprocess-args.md)\* | 返回指向当前子进程启动参数的指针。 |

### OH\_Ability\_OnNativeChildProcessExit()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_Ability_OnNativeChildProcessExit)(int32_t pid, int32_t signal)
```

**描述**

感知Native子进程退出的回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t pid | 启动的子进程id。 |
| int32\_t signal | 子进程退出信号。 |

**参见：**

[OH\_Ability\_RegisterNativeChildProcessExitCallback](capi-native-child-process-h.md#oh_ability_registernativechildprocessexitcallback)

[OH\_Ability\_UnregisterNativeChildProcessExitCallback](capi-native-child-process-h.md#oh_ability_unregisternativechildprocessexitcallback)

### OH\_Ability\_RegisterNativeChildProcessExitCallback()

PhonePC/2in1TabletTVWearable

```
1. Ability_NativeChildProcess_ErrCode OH_Ability_RegisterNativeChildProcessExitCallback(OH_Ability_OnNativeChildProcessExit onProcessExit)
```

**描述**

注册Native子进程退出回调函数。只有[OH\_Ability\_StartNativeChildProcess](capi-native-child-process-h.md#oh_ability_startnativechildprocess)、[OH\_Ability\_StartNativeChildProcessWithConfigs](capi-native-child-process-h.md#oh_ability_startnativechildprocesswithconfigs)和[@ohos.app.ability.childProcessManager的startNativeChildProcess](js-apis-app-ability-childprocessmanager.md#childprocessmanagerstartnativechildprocess13)启动的子进程退出时才会触发所注册的回调函数。当重复注册同一个回调函数时，子进程退出时只会执行一次回调函数。

参数必须实现[OH\_Ability\_OnNativeChildProcessExit](capi-native-child-process-h.md#oh_ability_onnativechildprocessexit)入口函数。详见[注册Native子进程退出回调](../harmonyos-guides/capi-nativechildprocess-exit-info.md)。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Ability\_OnNativeChildProcessExit](capi-native-child-process-h.md#oh_ability_onnativechildprocessexit) onProcessExit | 子进程退出的回调函数入口，不能为nullptr。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Ability\_NativeChildProcess\_ErrCode](capi-native-child-process-h.md#ability_nativechildprocess_errcode) | NCP\_NO\_ERROR - 调用成功。  NCP\_ERR\_INVALID\_PARAM - 参数不合法。  NCP\_ERR\_INTERNAL - 内部错误。  详见Ability\_NativeChildProcess\_ErrCode。 |

### OH\_Ability\_UnregisterNativeChildProcessExitCallback()

PhonePC/2in1TabletTVWearable

```
1. Ability_NativeChildProcess_ErrCode OH_Ability_UnregisterNativeChildProcessExitCallback(OH_Ability_OnNativeChildProcessExit onProcessExit)
```

**描述**

解注册子进程退出回调。

参数必须实现[OH\_Ability\_OnNativeChildProcessExit](capi-native-child-process-h.md#oh_ability_onnativechildprocessexit)入口函数。详见[解注册Native子进程退出回调](../harmonyos-guides/capi-nativechildprocess-exit-info.md)。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Ability\_OnNativeChildProcessExit](capi-native-child-process-h.md#oh_ability_onnativechildprocessexit) onProcessExit | 子进程退出的回调函数入口，不能为nullptr。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Ability\_NativeChildProcess\_ErrCode](capi-native-child-process-h.md#ability_nativechildprocess_errcode) | NCP\_NO\_ERROR - 调用成功。  NCP\_ERR\_INVALID\_PARAM - 参数不合法。  NCP\_ERR\_INTERNAL - 内部错误。  NCP\_ERR\_CALLBACK\_NOT\_EXIST - 未找到回调函数。  详见Ability\_NativeChildProcess\_ErrCode。 |

### OH\_Ability\_KillChildProcess()

PhonePC/2in1TabletTVWearable

```
1. Ability_NativeChildProcess_ErrCode OH_Ability_KillChildProcess(int32_t pid)
```

**描述**

终止当前进程创建的子进程。

说明

调用该接口无法终止[childProcessManager.startChildProcess](js-apis-app-ability-childprocessmanager.md#childprocessmanagerstartchildprocess)接口在SELF\_FORK模式下启动的子进程。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t pid | 要终止的子进程pid。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Ability\_NativeChildProcess\_ErrCode](capi-native-child-process-h.md#ability_nativechildprocess_errcode) | NCP\_NO\_ERROR - 调用成功。  NCP\_ERR\_SERVICE\_ERROR - 服务端出错。  NCP\_ERR\_INVALID\_PID - 所传入的子进程pid不合法。  详见Ability\_NativeChildProcess\_ErrCode。 |
