---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-qos-h
title: qos.h
breadcrumb: API参考 > 系统 > 基础功能 > Kernel Enhance Kit（内核增强能力） > C API > 头文件 > qos.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:11+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:de1ea340b48913fa497d02972cfe27204668bbb680f59d0eacbb1df7bd4e0d6f
---

## 概述

声明QoS（Quality of Service）提供的C接口，用于设置、获取和取消线程QoS等级，帮助系统根据任务重要程度进行差异化调度。本文件同时提供格物服务（Gewu service，端侧AI推理加速服务）相关C接口，用于创建会话、提交推理请求、接收回复、中止请求和销毁会话等操作，适用于需要在本地执行AI模型推理并精细控制资源调度的场景。

**引用文件：** <qos/qos.h>

**系统能力：** SystemCapability.Resourceschedule.QoS.Core

**库：** libqos.so

**起始版本：** 12

**相关模块：** [QoS](capi-qos.md)

## 汇总

### 结构体

| 名称 | 描述 |
| --- | --- |
| [OH\_QoS\_GewuCreateSessionResult](capi-qos-oh-qos-gewucreatesessionresult.md) | 格物服务创建会话的返回结果。 |
| [OH\_QoS\_GewuSubmitRequestResult](capi-qos-oh-qos-gewusubmitrequestresult.md) | 格物服务提交请求的返回结果。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [QoS\_Level](capi-qos-h.md#qos_level) | QoS\_Level | 描述QoS等级。 |
| [OH\_QoS\_GewuErrorCode](capi-qos-h.md#oh_qos_gewuerrorcode) | OH\_QoS\_GewuErrorCode | 格物错误码。 |

### 宏定义

| 名称 | 描述 |
| --- | --- |
| OH\_QOS\_GEWU\_INVALID\_SESSION\_ID ((OH\_QoS\_GewuSession)(0xffffffffU)) | 无效会话句柄，用于错误返回。  **起始版本：** 20 |
| OH\_QOS\_GEWU\_INVALID\_REQUEST\_ID ((OH\_QoS\_GewuRequest)(0xffffffffU)) | 无效请求句柄，用于错误返回。  **起始版本：** 20 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [int OH\_QoS\_SetThreadQoS(QoS\_Level level)](capi-qos-h.md#oh_qos_setthreadqos) | - | 为当前线程设置QoS等级。 |
| [int OH\_QoS\_ResetThreadQoS()](capi-qos-h.md#oh_qos_resetthreadqos) | - | 重置当前线程的QoS等级。 |
| [int OH\_QoS\_GetThreadQoS(QoS\_Level \*level)](capi-qos-h.md#oh_qos_getthreadqos) | - | 获取当前线程的QoS等级。 |
| [typedef void (\*OH\_QoS\_GewuOnResponse)(void\* context, const char\* response)](capi-qos-h.md#oh_qos_gewuonresponse) | OH\_QoS\_GewuOnResponse | 用于接收格物服务回复的回调。格物服务在推理完成后异步调用该回调函数，非流式推理时调用一次，流式推理时根据生成过程多次调用。 |
| [OH\_QoS\_GewuCreateSessionResult OH\_QoS\_GewuCreateSession(const char\* attributes)](capi-qos-h.md#oh_qos_gewucreatesession) | - | 创建格物服务会话，attributes参数为会话属性JSON字符串，示例见函数说明。 |
| [OH\_QoS\_GewuErrorCode OH\_QoS\_GewuDestroySession(OH\_QoS\_GewuSession session)](capi-qos-h.md#oh_qos_gewudestroysession) | - | 销毁格物会话。 |
| [OH\_QoS\_GewuErrorCode OH\_QoS\_GewuAbortRequest(OH\_QoS\_GewuSession session, OH\_QoS\_GewuRequest request)](capi-qos-h.md#oh_qos_gewuabortrequest) | - | 停止指定的请求。 |
| [OH\_QoS\_GewuSubmitRequestResult OH\_QoS\_GewuSubmitRequest(OH\_QoS\_GewuSession session, const char\* request, OH\_QoS\_GewuOnResponse callback, void\* context)](capi-qos-h.md#oh_qos_gewusubmitrequest) | - | 提交请求，request参数为请求JSON字符串，示例见函数说明。 |

### 变量

| 名称 | 描述 |
| --- | --- |
| [OH\_QoS\_GewuSession](capi-qos-h.md#oh_qos_gewusession) | 会话句柄。  **起始版本：** 20 |
| [OH\_QoS\_GewuRequest](capi-qos-h.md#oh_qos_gewurequest) | 请求句柄。  **起始版本：** 20 |

## 变量说明

### OH\_QoS\_GewuSession

```c
typedef unsigned int OH_QoS_GewuSession
```

**描述**

格物会话句柄，用于标识通过OH\_QoS\_GewuCreateSession创建的会话。

**起始版本：** 20

### OH\_QoS\_GewuRequest

```c
typedef unsigned int OH_QoS_GewuRequest
```

**描述**

格物请求句柄，用于标识通过OH\_QoS\_GewuSubmitRequest提交的请求。

**起始版本：** 20

## 枚举类型说明

### QoS\_Level

```c
enum QoS_Level
```

**描述**

描述QoS等级。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| QOS\_BACKGROUND = 0 | 表示QoS等级为用户不可见任务。 |
| QOS\_UTILITY = 1 | 表示QoS等级为后台重要任务。 |
| QOS\_DEFAULT = 2 | 表示QoS等级为默认。 |
| QOS\_USER\_INITIATED = 3 | 表示QoS等级为用户触发任务。 |
| QOS\_DEADLINE\_REQUEST = 4 | 表示QoS等级为限时任务。 |
| QOS\_USER\_INTERACTIVE = 5 | 表示QoS等级为用户交互任务。 |

### OH\_QoS\_GewuErrorCode

```c
enum OH_QoS_GewuErrorCode
```

**描述**

格物错误码。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| OH\_QOS\_GEWU\_OK = 0 | 成功。 |
| OH\_QOS\_GEWU\_NOPERM = 201 | 权限错误。可能原因：调用者缺少所需权限。解决措施：请确认已申请相关权限。 |
| OH\_QOS\_GEWU\_NOMEM = 203 | 内存错误。可能原因：系统内存不足。解决措施：请释放资源后重试。 |
| OH\_QOS\_GEWU\_INVAL = 401 | 参数错误。可能原因：参数类型不正确或参数值无效。解决措施：请检查参数类型和取值范围。 |
| OH\_QOS\_GEWU\_EXIST = 501 | 已存在句柄。可能原因：重复创建已存在的会话或请求。解决措施：请勿重复创建，或先销毁已有句柄。 |
| OH\_QOS\_GEWU\_NOENT = 502 | 找不到句柄。可能原因：传入的会话或请求句柄无效或已被销毁。解决措施：请检查句柄是否有效。 |
| OH\_QOS\_GEWU\_NOSYS = 801 | 找不到子系统。可能原因：目标设备不支持该功能。解决措施：更换为支持该功能的设备。 |
| OH\_QOS\_GEWU\_FAULT = 901 | 其他错误。可能原因：未覆盖的内部系统错误。解决措施：请检查系统日志获取详细错误信息，或联系技术支持。 |

## 函数说明

### OH\_QoS\_SetThreadQoS()

```c
int OH_QoS_SetThreadQoS(QoS_Level level)
```

**描述**

为当前线程设置QoS等级。系统会根据QoS等级调整线程调度优先级和资源分配策略，等级越高的任务通常获得更及时的调度。例如：在执行后台下载或数据同步等用户不可见任务时，可设置QOS\_BACKGROUND以降低资源占用；在处理用户交互或前台渲染等高优先级任务时，可设置QOS\_USER\_INTERACTIVE以获得更快的响应速度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [QoS\_Level](capi-qos-h.md#qos_level) level | 表示设置的QoS等级。设置为不同等级会影响线程的调度优先级和资源分配：QOS\_BACKGROUND适用于降低后台任务资源占用，QOS\_USER\_INTERACTIVE适用于提升交互任务响应速度，QOS\_DEFAULT表示默认调度策略。详见[QoS\_Level](capi-qos-h.md#qos_level)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回0，如果级别超出范围或内部错误失败则返回-1。 |

**参考：**

[QoS\_Level](capi-qos-h.md#qos_level)

### OH\_QoS\_ResetThreadQoS()

```c
int OH_QoS_ResetThreadQoS()
```

**描述**

重置当前线程的QoS等级，线程将恢复为系统默认调度策略。例如：当之前设置的高优先级任务执行完毕后，调用此接口恢复默认等级，避免不必要的资源占用。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回0，如果内部错误失败则返回-1。 |

**参考：**

[QoS\_Level](capi-qos-h.md#qos_level)

### OH\_QoS\_GetThreadQoS()

```c
int OH_QoS_GetThreadQoS(QoS_Level *level)
```

**描述**

获取当前线程的QoS等级。该接口用于读取当前线程已设置的QoS等级，如果当前线程未设置QoS等级或发生内部错误则返回-1。例如：在需要根据线程当前优先级进行条件判断的场景中，可先调用此接口获取QoS等级，再决定后续操作。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [QoS\_Level](capi-qos-h.md#qos_level) \*level | 输出参数，线程的QoS等级会以[QoS\_Level](capi-qos-h.md#qos_level)形式写入该变量。此参数不允许为NULL，传入NULL将导致函数返回-1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回0，如果当前线程未设置QoS等级或内部错误失败则返回-1。 |

**参考：**

[QoS\_Level](capi-qos-h.md#qos_level)

### OH\_QoS\_GewuOnResponse()

```c
typedef void (*OH_QoS_GewuOnResponse)(void* context, const char* response)
```

**描述**

用于接收格物服务回复的回调。格物服务在推理完成后异步调用该回调函数，非流式推理时调用一次，流式推理时根据生成过程多次调用。例如：在使用格物服务进行对话式AI推理时，可通过此回调接收模型生成的回复内容。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| void\* context | 提交请求时指定的用户上下文指针。该指针会在收到回复时原样传递给OH\_QoS\_GewuOnResponse回调函数，用于关联请求和响应数据。 |
| const char\* response | 回复的JSON字符串，包含以下字段：  - message: 对象，包含role和content两个字段。其中role为string类型，表示消息的角色类型，应为"assistant"；content为string类型，表示模型生成返回给用户的消息。  - finish\_reason: string or null，停止原因，可能的值如下：  - null: 表示没有停止。流式推理中会有多次回复，只有最后一次回复有非空的"finish\_reason"。而非流式推理只有一次回复，且"finish\_reason"非空。  - "stop": 正常停止。  - "abort": 用户主动提前中止。  - "length": token数超过限制。 |

### OH\_QoS\_GewuCreateSession()

```c
OH_QoS_GewuCreateSessionResult OH_QoS_GewuCreateSession(const char* attributes)
```

**描述**

创建格物会话。调用此接口前，需确保系统支持格物服务能力并已申请接口所需权限。该函数会根据会话属性加载指定的AI模型并初始化推理环境，为后续推理请求做好准备。会话对象的生命周期从OH\_QoS\_GewuCreateSession函数返回开始，到调用OH\_QoS\_GewuDestroySession为止。在生命周期内，可以创建多个请求；建议在销毁会话前等待所有请求完成或中止，否则这些请求会被自动中止且不再收到回复；销毁后会话句柄无法再使用。会话属性通过JSON字符串传入，该JSON字符串支持以下字段：

- model: string（必选），表示会话使用的模型路径。

attributes JSON字符串例子：

{

"model": "/data/storage/el2/base/files/qwen2/"

}

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* attributes | 输入参数，会话属性的JSON字符串，用于指定会话使用的模型路径。支持的字段包括：model（string，必选，表示会话使用的模型路径，支持应用沙箱可访问的路径）。详见函数说明中的JSON示例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_QoS\_GewuCreateSessionResult](capi-qos-oh-qos-gewucreatesessionresult.md) | 格物创建会话结果。  - 表示创建会话成功，返回值OH\_QoS\_GewuCreateSessionResult里的error为OH\_QOS\_GEWU\_OK，session为会话句柄。  - 表示创建会话失败，返回值OH\_QoS\_GewuCreateSessionResult里的error为错误原因，其中OH\_QOS\_GEWU\_NOMEM表示没有足够的内存创建会话，OH\_QOS\_GEWU\_INVAL表示参数错误，OH\_QOS\_GEWU\_NOPERM表示权限不足，OH\_QOS\_GEWU\_EXIST表示会话已存在，OH\_QOS\_GEWU\_NOSYS表示找不到子系统。 |

### OH\_QoS\_GewuDestroySession()

```c
OH_QoS_GewuErrorCode OH_QoS_GewuDestroySession(OH_QoS_GewuSession session)
```

**描述**

销毁格物会话。该函数会释放会话相关资源并清理内部状态。建议等待至所有请求都已完成或中止后再调用此接口。如果调用时还有正在进行的请求，这些请求将会被中止，且不再收到回复，请求句柄无法再被使用。注意，在调用完该接口后，会话对象无法再被使用。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_QoS\_GewuSession](capi-qos-h.md#oh_qos_gewusession) session | 要销毁的会话句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_QoS\_GewuErrorCode](capi-qos-h.md#oh_qos_gewuerrorcode) | 错误码。  - 表示会话销毁成功，返回值为OH\_QOS\_GEWU\_OK。  - 表示找不到会话，返回OH\_QOS\_GEWU\_NOENT。  - 表示参数无效，返回OH\_QOS\_GEWU\_INVAL。  - 表示找不到子系统，返回OH\_QOS\_GEWU\_NOSYS。  - 表示其他内部错误，返回OH\_QOS\_GEWU\_FAULT。 |

### OH\_QoS\_GewuAbortRequest()

```c
OH_QoS_GewuErrorCode OH_QoS_GewuAbortRequest(OH_QoS_GewuSession session, OH_QoS_GewuRequest request)
```

**描述**

停止指定的请求。该函数会请求格物服务中止正在进行的推理计算，并清理该请求相关状态。调用此接口前，需确保传入的会话句柄有效（未通过OH\_QoS\_GewuDestroySession销毁），且请求句柄有效（已通过OH\_QoS\_GewuSubmitRequest提交）。典型使用场景包括用户主动取消正在进行的推理请求，或应用需要释放资源时提前终止不需要的请求。成功调用该函数后，客户端不会再收到该请求的回复，且该请求句柄无法再被使用。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_QoS\_GewuSession](capi-qos-h.md#oh_qos_gewusession) session | 请求提交到的会话句柄。 |
| [OH\_QoS\_GewuRequest](capi-qos-h.md#oh_qos_gewurequest) request | 请求的句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_QoS\_GewuErrorCode](capi-qos-h.md#oh_qos_gewuerrorcode) | 错误码。  - 表示成功停止请求，返回OH\_QOS\_GEWU\_OK。  - 表示找不到请求，返回OH\_QOS\_GEWU\_NOENT。  - 表示参数无效，返回OH\_QOS\_GEWU\_INVAL。  - 表示找不到子系统，返回OH\_QOS\_GEWU\_NOSYS。 |

### OH\_QoS\_GewuSubmitRequest()

```c
OH_QoS_GewuSubmitRequestResult OH_QoS_GewuSubmitRequest(OH_QoS_GewuSession session, const char* request, OH_QoS_GewuOnResponse callback, void* context)
```

**描述**

提交请求。该函数会将推理请求提交到指定会话，由格物服务调度执行。调用此接口前，需确保传入的会话句柄有效（已通过OH\_QoS\_GewuCreateSession创建且未通过OH\_QoS\_GewuDestroySession销毁）。request参数为请求的JSON字符串，支持以下字段：

- messages: array，必填，表示消息的数组，其中每个元素支持以下字段：

- role: string，消息的角色类型，可选值包括：

- "developer"：开发者或系统提供的指示。

- "user"：用户输入。

- "assistant"：模型生成结果。

- content: string，消息内容。

- stream: boolean or null，可选，是否使能流式推理。传入true启用流式推理，适用于需要逐步接收模型生成内容、降低首字延迟的场景，回调会被多次调用；传入false或null使用非流式推理，适用于需要一次性获取完整结果的场景，回调仅调用一次。不传入时默认为非流式。JSON字符串例子：

{

"messages": [

{

"role": "developer",

"content": "You are a helpful assistant."

},

{

"role": "user",

"content": "What is HarmonyOS"

}

],

"stream": true

}

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_QoS\_GewuSession](capi-qos-h.md#oh_qos_gewusession) session | 会话句柄，请求要提交的会话。 |
| const char\* request | 请求的JSON字符串，支持的字段包括：messages（array，消息数组，每个元素包含role和content字段，其中role可选值为developer、user、assistant）、stream（boolean或null，可选，是否启用流式推理，不传时默认为非流式）。详见函数说明中的JSON示例。 |
| [OH\_QoS\_GewuOnResponse](capi-qos-h.md#oh_qos_gewuonresponse) callback | 接收回复的回调。 |
| void\* context | 要传给回调的用户上下文指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_QoS\_GewuSubmitRequestResult](capi-qos-oh-qos-gewusubmitrequestresult.md) | 格物提交请求结果。error字段为枚举[OH\_QoS\_GewuErrorCode](capi-qos-h.md#oh_qos_gewuerrorcode)，枚举值与数字对应关系详见[OH\_QoS\_GewuErrorCode](capi-qos-h.md#oh_qos_gewuerrorcode)枚举说明。  - 表示提交请求成功，返回值OH\_QoS\_GewuSubmitRequestResult里的error为OH\_QOS\_GEWU\_OK（数值0），request为请求句柄。  - 表示提交请求失败，返回值OH\_QoS\_GewuSubmitRequestResult里的error为错误原因，其中OH\_QOS\_GEWU\_NOMEM（数值203）表示没有足够的内存处理该请求，OH\_QOS\_GEWU\_INVAL（数值401）表示参数错误，OH\_QOS\_GEWU\_NOENT（数值502）表示找不到会话，OH\_QOS\_GEWU\_NOPERM（数值201）表示权限不足，OH\_QOS\_GEWU\_NOSYS（数值801）表示找不到子系统。 |
