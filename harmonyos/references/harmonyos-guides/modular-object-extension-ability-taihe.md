---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/modular-object-extension-ability-taihe
title: 使用Taihe实现ModularObjectExtensionAbility的IPC通信 (C/C++)
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > 基于ModularObjectExtensionAbility的模块化对象开发指导 (C/C++) > 使用Taihe实现ModularObjectExtensionAbility的IPC通信 (C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:11+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d1458e406f15ca2f06005f8ce5fac145dbf10ef52ae879e35069168159566dee
---

从API版本26.0.0开始，通过[Taihe](ability-terminology.md#taihe)可自动生成ModularObjectExtensionAbility（相关C API定义见[modular\_object\_extension\_ability.h](../harmonyos-references/capi-modular-object-extension-ability-h.md)）所需的Proxy/Stub代码及类型库文件，屏蔽IPC通信底层细节（如参数序列化/反序列化、消息码分发等），使开发者专注于接口设计与业务逻辑，大幅简化ModularObjectExtensionAbility的开发流程。

## 命令行使用

Taihe提供了核心编译器工具[taihec](ability-terminology.md#taihec)，用于解析ohidl文件并将其编译为目标语言代码。本章节介绍如何使用taihec生成ModularObjectExtensionAbility在IPC通信场景下所需的Proxy和Stub代码。请参考[模块化对象模型概述 (C/C++)](modular-object-extension-overview.md)的[基本概念](modular-object-extension-overview.md#基本概念)，了解Proxy与Stub。

**taihec工具获取：**

taihec工具随SDK发布，位于DevEco Studio/sdk/default/openharmony/toolchains/taihe/bin目录下。

**命令基本格式：**

```bash
taihec [taihe_files ...] [options ...]
```

* taihe\_files：一个或多个接口定义文件ohidl，主接口文件和公共类型文件需一并列出。
* options：用于指定代码生成的各种选项。

**命令行参数说明：**

| 参数 | 简写 | 必选/可选 | 说明 |
| --- | --- | --- | --- |
| --output <path> | -O <path> | 必选 | 指定生成的目标文件（.cpp/.h格式）存放目录。 |
| --generate <backend> | -G <backend> | 可选 | 指定代码生成后端。在ModularObjectExtensionAbility的IPC通信场景下，固定使用modobj-ipc。 |
| --codegen <namespace>:<config>[=<value>] | -C <namespace>:<config>[=<value>] | 可选 | 额外的代码生成配置项。ModularObjectExtensionAbility的IPC通信场景下仅支持modobj:ipc-common=common.ohidl，用于引入公共类型文件。 |

**执行代码生成示例：**

当主接口文件需要引用其他文件中的数据类型时，通过-C参数引入公共类型文件（定义结构体、枚举等公共数据类型）。带-C参数的生成命令会将公共数据类型单独生成到ExampleServiceIpcTypes.cpp和ExampleServiceIpcTypes.h文件中。

```bash
taihec -G modobj-ipc -O example/generated/IBasicTypes_ohidl_c -C modobj:ipc-common=example/ExampleServiceIpcTypes.ohidl example/IBasicTypes.ohidl
```

所有类型都定义在主接口文件中，无需引用其他文件。

```bash
taihec -G modobj-ipc -O example/generated example/Easy.ohidl
```

## ohidl文件编写规范

本节介绍ohidl文件中支持的数据类型、注解使用方式以及示例文件，帮助开发者编写ohidl文件。

### 数据类型与注解

**基础数据类型：**

| Taihe | C++类型 | Parcel写入/读取规则 |
| --- | --- | --- |
| bool | bool | OH\_IPCParcel\_WriteInt32/OH\_IPCParcel\_ReadInt32 |
| i8 | int8\_t | OH\_IPCParcel\_WriteInt8/OH\_IPCParcel\_ReadInt8 |
| i16 | int16\_t | OH\_IPCParcel\_WriteInt16/OH\_IPCParcel\_ReadInt16 |
| i32 | int32\_t | OH\_IPCParcel\_WriteInt32/OH\_IPCParcel\_ReadInt32 |
| i64 | int64\_t | OH\_IPCParcel\_WriteInt64/OH\_IPCParcel\_ReadInt64 |
| f32 | float | OH\_IPCParcel\_WriteFloat/OH\_IPCParcel\_ReadFloat |
| f64 | double | OH\_IPCParcel\_WriteDouble/OH\_IPCParcel\_ReadDouble |
| u8 | uint8\_t | OH\_IPCParcel\_WriteUint8\_t/OH\_IPCParcel\_ReadUint8\_t |
| u16 | uint16\_t | OH\_IPCParcel\_WriteUint16\_t/OH\_IPCParcel\_ReadUint16\_t |
| u32 | uint32\_t | OH\_IPCParcel\_WriteUint32\_t/OH\_IPCParcel\_ReadUint32\_t |
| u64 | uint64\_t | OH\_IPCParcel\_WriteUint64\_t/OH\_IPCParcel\_ReadUint64\_t |

**复杂数据类型：**

| Taihe | C++类型 | Parcel写入/读取规则 |
| --- | --- | --- |
| String | std::string | 转为const char\*后OH\_IPCParcel\_WriteString/OH\_IPCParcel\_ReadString。 |
| enum | enum | 按int32\_t序列化。 |
| Vector<T> | std::vector<T> | 先写size，再逐项序列化。 |
| @size(N) Array<T> | std::array<T, N> | 先写size，再逐项序列化。 |
| Set<T> | std::set<T> | 先写size，再逐项序列化。 |
| Map<K,V> | std::map<K, V> | 先写size，再顺序写入key/value。 |
| struct | struct& | 调用生成的Marshalling/Unmarshalling。 |
| interface | interface& | 写入OHIPCRemoteStub或OHIPCRemoteProxy，读取OHIPCRemoteProxy。 |

**注解与使用：**

| 注解 | 作用范围 | 说明 | 示例 |
| --- | --- | --- | --- |
| @main\_service(version="x.y.z") | interface | 有且仅能声明一个主服务接口，生成的Stub作为[OH\_AbilityRuntime\_ModObjExtensionAbility\_OnConnectFunc](../harmonyos-references/capi-modular-object-extension-ability-h.md#oh_abilityruntime_modobjextensionability_onconnectfunc)的返回值。 | @main\_service(version="1.0.0") |
| @callback | 方法 | 用于声明一个回调接口。服务端可持有此接口的实例来调用客户端，相关逻辑会在客户端的线程中执行。典型使用场景：客户端向服务端注册监听器、服务端主动通知客户端事件。完整开发流程参见[示例文件说明](modular-object-extension-ability-taihe.md#示例文件说明)中的ITestEventCallback示例。 | @callback interface ICallback {} |
| @oneway | 方法 | 异步单向IPC调用，仅支持void类型返回值。 | @oneway Notify(...): void; |
| @!namespace("A","B") | ohidl文件 | 设置生成代码所在的命名空间，以及IPC接口描述符字符串前缀。 | @!namespace("OHOS","NativeApp") |
| @size(N) | 参数 | 定长数组的大小，仅供Array类型参数使用。 | @size(4) Array<i32>; |

### 示例文件说明

编写ohidl文件时需要遵循以下约束与限制。

**ohidl文件的约束与限制：**

* 主接口文件定义服务核心接口，使用@main\_service标记。
* 公共类型文件定义结构体、枚举，通过from...use...复用。
* Map<K, V>的键类型仅支持基础数据类型、String和enum。
* 严禁调换interface中已有方法的顺序，否则将导致IpcCode错位而破坏兼容性。建议新增方法时应在interface末尾添加，并做好版本管理记录，以避免误操作破坏兼容性。

  **接口版本升级规范：**

  + 新增方法：只能在接口末尾添加新方法，不得在已有方法前插入。
  + 废弃方法：保留方法声明但标记为废弃，不得删除或移动位置。
  + 参数变更：建议新增方法而非修改已有方法的参数签名，确保老客户端兼容。
* 单次modobj-ipc生成范围内，所有interface、struct和enum名称必须全局唯一，不受命名空间限制。

**文件示例：**

```ohipc
@!namespace("OHOS", "IPC")

interface ICalculator {
    Add(a: i32, b: i32): i32;
}

struct OnProgressResult {
    summary: String;
}

@callback
interface ITestEventCallback {
    OnConnected(clientId: i32, welcome: String): void;
    OnProgress(taskId: i32): OnProgressResult;

    @oneway
    OnDisconnected(reason: String): void;
}

@main_service(version = "1.0.0")
interface ITestCallbackService {
    RegisterCallback(callback: ITestEventCallback): i32;
    GetPrimaryCalculator(userId: i32): ICalculator;
}
```

## 开发步骤

1. 创建example文件夹，并新建Easy.ohidl文件。

   ```ohipc
   @!namespace("OHOS", "IPC")

   @main_service(version = "1.0.0")
   interface ICalculator {
       Add(a: i32, b: i32): i32;
   }
   ```
2. 使用taihec命令生成代码。

   ```bash
   ./taihec -G modobj-ipc -O ./example/generated ./example/Easy.ohidl
   ```
3. 生成的代码文件解析。

   | 文件名 | 说明 |
   | --- | --- |
   | icalculator.h | 接口定义头文件。 |
   | calculator\_proxy.h | 客户端代理类声明。 |
   | calculator\_proxy.cpp | 代理实现，负责参数序列化、发送IPC请求、解析返回值。 |
   | calculator\_stub.h | 服务端Stub类声明。 |
   | calculator\_stub.cpp | Stub实现，负责反序列化请求、调用业务实现、写回响应。 |
   | calculator.typelib.json | 类型库信息文件。 |

   * icalculator.h

     GetDescriptor()返回接口描述符字符串，IpcCode枚举为每个方法分配唯一命令码，从1001开始。

     ```c
     class ICalculator {
     public:
         virtual ~ICalculator() = default;
         static const char* GetDescriptor() { return "OHOS.IPC.ICalculator"; }

         virtual ErrCode WriteRemoteObject(OHIPCParcel* parcel) const = 0;

         enum class IpcCode : uint32_t {
             COMMAND_ADD = 1001,
             COMMAND_GET_TYPE_LIB_INFO = 1,
             COMMAND_GET_VERSION = 2,
             COMMAND_GET_TAIHE_VERSION = 3,
         };

         virtual ErrCode Add(int32_t a, int32_t b, int32_t& result) = 0;
         virtual ErrCode GetTypeLibInfo(int32_t fd) = 0;
         virtual ErrCode GetVersion(std::string& result) = 0;
         virtual ErrCode GetTaiheVersion(std::string& result) = 0;
     };
     ```
   * calculator\_proxy.h

     CalculatorProxy继承ICalculator，并包含了远端代理对象remoteProxy\_。

     ```c
     class CalculatorProxy : public ICalculator {
     public:
         explicit CalculatorProxy(OHIPCRemoteProxy* remote) : remoteProxy_(remote) {}
         ~CalculatorProxy() override = default;
     // ...
         ErrCode WriteRemoteObject(OHIPCParcel* parcel) const override;

         ErrCode Add(int32_t a, int32_t b, int32_t& result) override;
     // ...
     private:
         OHIPCRemoteProxy* remoteProxy_ = nullptr;
     };
     ```
   * calculator\_proxy.cpp

     创建OHIPCParcel请求包和响应包，写入接口描述符和序列化参数。

     调用OH\_IPCRemoteProxy\_SendRequest()发起同步IPC，并读取reply中的错误码与返回值。

     ```
     ErrCode CalculatorProxy::WriteRemoteObject(OHIPCParcel* parcel) const
     {
         if (parcel == nullptr || remoteProxy_ == nullptr) {
             return OH_IPC_CHECK_PARAM_ERROR;
         }
         if (OH_IPCParcel_WriteRemoteProxy(parcel, remoteProxy_) != OH_IPC_SUCCESS) {
             return OH_IPC_PARCEL_WRITE_ERROR;
         }
         return OH_IPC_SUCCESS;
     }

     ErrCode CalculatorProxy::Add(int32_t a, int32_t b, int32_t& result)
     {
     // ...
         std::unique_ptr<OHIPCParcel, ParcelDeleter> parcelData(OH_IPCParcel_Create());
         std::unique_ptr<OHIPCParcel, ParcelDeleter> parcelReply(OH_IPCParcel_Create());
     // ...
         if (OH_IPCParcel_WriteInterfaceToken(parcelData.get(),
             ICalculator::GetDescriptor()) != OH_IPC_SUCCESS) {
             return OH_IPC_PARCEL_WRITE_ERROR;
         }

         if (OH_IPCParcel_WriteInt32(parcelData.get(), a) != OH_IPC_SUCCESS) {
             return OH_IPC_PARCEL_WRITE_ERROR;
         }
         if (OH_IPCParcel_WriteInt32(parcelData.get(), b) != OH_IPC_SUCCESS) {
             return OH_IPC_PARCEL_WRITE_ERROR;
         }
     // ...
         int32_t errCode = OH_IPC_SUCCESS;
         if (OH_IPCParcel_ReadInt32(parcelReply.get(), &errCode) != OH_IPC_SUCCESS) {
             return OH_IPC_PARCEL_READ_ERROR;
         }

         int32_t resultValue = 0;
         if (OH_IPCParcel_ReadInt32(parcelReply.get(), &resultValue) != OH_IPC_SUCCESS) {
             return OH_IPC_PARCEL_READ_ERROR;
         }
         result = resultValue;

         return errCode;
     }
     ```
   * calculator\_stub.h

     CalculatorStub继承ICalculator。

     OnRemoteRequest作为IPC调用入口，OnRemoteRequestInner根据code分发到具体HandleXXX方法。

     ```c
     class CalculatorStub : public ICalculator {
     public:
     // ...
         ErrCode WriteRemoteObject(OHIPCParcel* parcel) const override;

         static int32_t OnRemoteRequest(
             uint32_t code,
             const OHIPCParcel* data,
             OHIPCParcel* reply,
             void* userData);
     // ...
     private:
         int32_t OnRemoteRequestInner(uint32_t code, const OHIPCParcel* data, OHIPCParcel* reply);
         int32_t HandleAdd(const OHIPCParcel* data, OHIPCParcel* reply);
     // ...
     };
     ```
   * calculator\_stub.cpp

     OnRemoteRequestInner方法中先校验接口描述符，再调用HandleAdd从data中读取参数，调用真实Add业务实现，并将errCode和结果写回reply。

     ```
     int32_t CalculatorStub::OnRemoteRequestInner(uint32_t code, const OHIPCParcel* data, OHIPCParcel* reply)
     {
     // ...
         if (OH_IPCParcel_ReadInterfaceToken(data, &remoteDescriptor,
             &remoteDescriptorLen, OhipcReadInterfaceTokenAllocator) != OH_IPC_SUCCESS) {
             return OH_IPC_CHECK_PARAM_ERROR;
         }
     // ...
         switch (static_cast<ICalculator::IpcCode>(code)) {
             case ICalculator::IpcCode::COMMAND_ADD:
                 return HandleAdd(data, reply);
     // ...
             default:
                 return OH_IPC_CHECK_PARAM_ERROR;
         }
     }

     int32_t CalculatorStub::HandleAdd(const OHIPCParcel* data, OHIPCParcel* reply)
     {
         int32_t aValue = 0;
         if (OH_IPCParcel_ReadInt32(data, &aValue) != OH_IPC_SUCCESS) {
             return OH_IPC_PARCEL_READ_ERROR;
         }
         int32_t a = aValue;
     // ...
         int32_t result = 0;
         ErrCode errCode = Add(a, b, result);
         if (OH_IPCParcel_WriteInt32(reply, errCode) != OH_IPC_SUCCESS) {
             return OH_IPC_PARCEL_WRITE_ERROR;
         }

         if (OH_IPCParcel_WriteInt32(reply, result) != OH_IPC_SUCCESS) {
             return OH_IPC_PARCEL_WRITE_ERROR;
         }

         return OH_IPC_SUCCESS;
     }
     ```
   * calculator.typelib.json

     类型库元数据文件用于存储接口定义信息（如接口名称、描述符、方法名、IPC code、参数与返回类型等），供运行时查询方法信息和动态路由调用。该文件内容在编译期嵌入到生成的Stub代码中，开发者无需手动加载或随应用打包此JSON文件。下方示例仅用于展示文件内部结构。

     ```json
     {
       "version": "1.0",
       "taihe_version": "1.0.0",
       "enums": [],
       "structs": [],
       "interfaces": [
         {
           "memberId": 1,
           "name": "ICalculator",
           "descriptor": "OHOS.IPC.ICalculator",
           "interface_type": 1,
           "methods": [
             {
               "memberId": 4,
               "name": "Add",
               "code": 1001,
               "oneway": false,
               "return_type": {
                 "type": "i32"
               },
               "parameters": [
                 {
                   "memberId": 2,
                   "name": "a",
                   "type_info": {
                     "type": "i32"
                   }
                 },
                 {
                   "memberId": 3,
                   "name": "b",
                   "type_info": {
                     "type": "i32"
                   }
                 }
               ]
             }
           ]
         }
       ]
     }
     ```

     除了开发者在ohidl文件中定义的接口方法外，Taihe还会自动生成GetTypeLibInfo、GetVersion、GetTaiheVersion等方法。

     | 方法 | 默认行为 | 常量 |
     | --- | --- | --- |
     | GetTypeLibInfo | 返回类型库信息。 | COMMAND\_GET\_TYPE\_LIB\_INFO = 1 |
     | GetVersion | 返回@main\_service注解中 version 声明的版本号。 | COMMAND\_GET\_VERSION = 2 |
     | GetTaiheVersion | 返回Taihe编译器的版本，供系统调用，开发者无需关注。 | COMMAND\_GET\_TAIHE\_VERSION = 3 |
4. Proxy和Stub源码的使用。

   生成的Proxy和Stub代码可直接用于IPC通信。在客户端侧，通过创建CalculatorProxy实例并传入OHIPCRemoteProxy对象来调用远端方法；在服务端侧，继承CalculatorStub并实现业务逻辑接口。

   详细开发流程请参考[使用ModularObjectExtensionAbility实现模块化对象 (C/C++)](modular-object-extension-development.md)。
