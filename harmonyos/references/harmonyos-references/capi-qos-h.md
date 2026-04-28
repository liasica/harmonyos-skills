---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-qos-h
title: qos.h
breadcrumb: API参考 > 系统 > 基础功能 > Kernel Enhance Kit（内核增强能力） > C API > 头文件 > qos.h
category: harmonyos-references
scraped_at: 2026-04-28T08:10:33+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:6ca9333ff414e59bef2e9e9da332767c5f152a884e89743061d5aea53c34327d
---

## 概述

PhonePC/2in1TabletTVWearable

声明QoS提供的C接口。

**引用文件：** <qos/qos.h>

**系统能力：** SystemCapability.Resourceschedule.QoS.Core

**库：** libqos.so

**起始版本：** 12

**相关模块：** [QoS](capi-qos.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_QoS\_GewuCreateSessionResult](capi-qos-oh-qos-gewucreatesessionresult.md) | 格物创建会话的返回结果 |
| [OH\_QoS\_GewuSubmitRequestResult](capi-qos-oh-qos-gewusubmitrequestresult.md) | 格物提交请求的返回结果 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [QoS\_Level](capi-qos-h.md#qos_level) | QoS\_Level | 描述QoS等级。 |
| [OH\_QoS\_GewuErrorCode](capi-qos-h.md#oh_qos_gewuerrorcode) | OH\_QoS\_GewuErrorCode | 格物错误码。 |

### 宏定义

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| OH\_QOS\_GEWU\_INVALID\_SESSION\_ID (static\_cast<OH\_QoS\_GewuSession>(0xffffffffU)) | 无效会话句柄，用于错误返回。  **起始版本：** 20 |
| OH\_QOS\_GEWU\_INVALID\_REQUEST\_ID (static\_cast<OH\_QoS\_GewuRequest>(0xffffffffU)) | 无效请求句柄，用于错误返回。  **起始版本：** 20 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [int OH\_QoS\_SetThreadQoS(QoS\_Level level)](capi-qos-h.md#oh_qos_setthreadqos) | - | 为当前线程设置QoS等级。 |
| [int OH\_QoS\_ResetThreadQoS()](capi-qos-h.md#oh_qos_resetthreadqos) | - | 取消当前线程的QoS等级。 |
| [int OH\_QoS\_GetThreadQoS(QoS\_Level \*level)](capi-qos-h.md#oh_qos_getthreadqos) | - | 获得当前线程的QoS等级。 |
| [typedef void (\*OH\_QoS\_GewuOnResponse)(void\* context, const char\* response)](capi-qos-h.md#oh_qos_gewuonresponse) | OH\_QoS\_GewuOnResponse | 用于接收回复的回调。 |
| [OH\_QoS\_GewuCreateSessionResult OH\_QoS\_GewuCreateSession(const char\* attributes)](capi-qos-h.md#oh_qos_gewucreatesession) | - | 创建格物会话。会话对象的生命周期从CreateSession函数返回开始，到调用DestroySession为止。会话属性的json字符串。该json字符串支持以下字段：- model: string. 表示会话使用的模型的路径。attributes json字符串例子：  {  "model": "/data/storage/el2/base/files/qwen2/"  } |
| [OH\_QoS\_GewuErrorCode OH\_QoS\_GewuDestroySession(OH\_QoS\_GewuSession session)](capi-qos-h.md#oh_qos_gewudestroysession) | - | 销毁格物会话。建议用户应当等待至所有请求都已完成或中止，然后再调用该接口来销毁会话。如果调用该接口时还有正在进行的请求，那些请求将会被中止，且用户不会再收到回复。注意，在调用完该接口后，会话对象无法再被使用。 |
| [OH\_QoS\_GewuErrorCode OH\_QoS\_GewuAbortRequest(OH\_QoS\_GewuSession session, OH\_QoS\_GewuRequest request)](capi-qos-h.md#oh_qos_gewuabortrequest) | - | 停止指定的请求。成功调用该函数后，client不会再收到该请求的回复，且该请求句柄无法再被使用。 |
| [OH\_QoS\_GewuSubmitRequestResult OH\_QoS\_GewuSubmitRequest(OH\_QoS\_GewuSession session, const char\* request, OH\_QoS\_GewuOnResponse callback, void\* context)](capi-qos-h.md#oh_qos_gewusubmitrequest) | - | 提交请求。请求的json字符串，支持以下字段：- messages: array. 表示消息的数组其中每个元素支持以下字段：- role: string. 消息的角色类型。可以为以下字段：- "developer": 开发者或系统提供的指示。- "user":用户输入。- "assistant": 模型生成结果。- content: string. 消息内容。- stream: boolean or null; 可选。是否使能流式推理，默认为非流式。json字符串例子：  {  "messages": [  {  "role": "developer",  "content": "You are a helpful assistant."  },  {  "role": "user",  "content": "What is HarmonyOS"  }  ],  "stream": true  } |

### 变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| OH\_QoS\_GewuSession | 会话句柄。  **起始版本：** 20 |
| OH\_QoS\_GewuRequest | 请求句柄。  **起始版本：** 20 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### QoS\_Level

PhonePC/2in1TabletTVWearable

```
1. enum QoS_Level
```

**描述**

描述QoS等级。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| QOS\_BACKGROUND = 0 | 表示QoS等级为用户不可见任务。 |
| QOS\_UTILITY | 表示QoS等级为后台重要任务。 |
| QOS\_DEFAULT | 表示QoS等级为默认。 |
| QOS\_USER\_INITIATED | 表示QoS等级为用户触发任务。 |
| QOS\_DEADLINE\_REQUEST | 表示QoS等级为限时任务。 |
| QOS\_USER\_INTERACTIVE | 表示QoS等级为用户交互任务。 |

### OH\_QoS\_GewuErrorCode

PhonePC/2in1TabletTVWearable

```
1. enum OH_QoS_GewuErrorCode
```

**描述**

格物错误码。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| OH\_QOS\_GEWU\_OK = 0 | 成功 |
| OH\_QOS\_GEWU\_NOPERM = 201 | 权限错误 |
| OH\_QOS\_GEWU\_NOMEM = 203 | 内存错误 |
| OH\_QOS\_GEWU\_INVAL = 401 | 参数错误 |
| OH\_QOS\_GEWU\_EXIST = 501 | 已存在句柄 |
| OH\_QOS\_GEWU\_NOENT = 502 | 找不到句柄 |
| OH\_QOS\_GEWU\_NOSYS = 801 | 找不到符号 |
| OH\_QOS\_GEWU\_FAULT = 901 | 其它错误 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_QoS\_SetThreadQoS()

PhonePC/2in1TabletTVWearable

```
1. int OH_QoS_SetThreadQoS(QoS_Level level)
```

**描述**

为当前线程设置QoS等级。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [QoS\_Level](capi-qos-h.md#qos_level) level | 表示设置的QoS等级，详细信息可以查看[QoS\_Level](capi-qos-h.md#qos_level)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回0，如果级别超出范围或内部错误失败则返回-1。 |

**参考：**

[QoS\_Level](capi-qos-h.md#qos_level)

### OH\_QoS\_ResetThreadQoS()

PhonePC/2in1TabletTVWearable

```
1. int OH_QoS_ResetThreadQoS()
```

**描述**

取消当前线程的QoS等级。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回0，如果级别超出范围或内部错误失败则返回-1。 |

**参考：**

[QoS\_Level](capi-qos-h.md#qos_level)

### OH\_QoS\_GetThreadQoS()

PhonePC/2in1TabletTVWearable

```
1. int OH_QoS_GetThreadQoS(QoS_Level *level)
```

**描述**

获得当前线程的QoS等级。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [QoS\_Level](capi-qos-h.md#qos_level) \*level | 参数是输出参数，线程的QoS等级会以[QoS\_Level](capi-qos-h.md#qos_level)形式写入该变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回0，如果级别超出范围或内部错误失败则返回-1。 |

**参考：**

[QoS\_Level](capi-qos-h.md#qos_level)

### OH\_QoS\_GewuOnResponse()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_QoS_GewuOnResponse)(void* context, const char* response)
```

**描述**

用于接收回复的回调。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| void\* context | 提交请求时指定的用户上下文句柄。 |
| const char\* response | 回复的json字符串，包含以下参数：  - message: 包含下列字段的消息。  - role: string. 消息的角色类型，应为"assistant".  - content: string。模型生成返回给用户的消息。  - finish\_reason: string or null. 停止原因，可能的值如下：  - null: 表示没有停止。流式推理中会有多次回复，只有最后一次回复有非空的"finish\_reason"。而非流式推理只有一次回复，且"finish\_reason"非空。  - "stop": 正常停止。  - "abort": 用户主动提前中止。  - "length": token数超过限制。 |

### OH\_QoS\_GewuCreateSession()

PhonePC/2in1TabletTVWearable

```
1. OH_QoS_GewuCreateSessionResult OH_QoS_GewuCreateSession(const char* attributes)
```

**描述**

创建格物会话。会话对象的生命周期从CreateSession函数返回开始，到调用DestroySession为止。会话属性的json字符串。该json字符串支持以下字段：- model: string. 表示会话使用的模型的路径。attributes json字符串例子：

{

"model": "/data/storage/el2/base/files/qwen2/"

}

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* attributes | 会话attributes的json字符串。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_QoS\_GewuCreateSessionResult](capi-qos-oh-qos-gewucreatesessionresult.md) | 创建会话的结果。 |

### OH\_QoS\_GewuDestroySession()

PhonePC/2in1TabletTVWearable

```
1. OH_QoS_GewuErrorCode OH_QoS_GewuDestroySession(OH_QoS_GewuSession session)
```

**描述**

销毁格物会话。建议用户应当等待至所有请求都已完成或中止，然后再调用该接口来销毁会话。如果调用该接口时还有正在进行的请求，那些请求将会被中止，且用户不会再收到回复。注意，在调用完该接口后，会话对象无法再被使用。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_QoS\_GewuSession](capi-qos-h.md#变量) session | 要销毁的会话的句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_QoS\_GewuErrorCode](capi-qos-h.md#oh_qos_gewuerrorcode) | 错误码  - 会话销毁成功，返回值为OH\_QOS\_GEWU\_OK。  - 找不到会话返回OH\_QOS\_GEWU\_NOENT。 |

### OH\_QoS\_GewuAbortRequest()

PhonePC/2in1TabletTVWearable

```
1. OH_QoS_GewuErrorCode OH_QoS_GewuAbortRequest(OH_QoS_GewuSession session, OH_QoS_GewuRequest request)
```

**描述**

停止指定的请求。成功调用该函数后，client不会再收到该请求的回复，且该请求句柄无法再被使用。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_QoS\_GewuSession](capi-qos-h.md#变量) session | 请求提交到的会话句柄。 |
| [OH\_QoS\_GewuRequest](capi-qos-h.md#变量) request | 请求的句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_QoS\_GewuErrorCode](capi-qos-h.md#oh_qos_gewuerrorcode) | 错误码。  - 成功停止请求返回OH\_QOS\_GEWU\_OK。  - 找不到请求返回OH\_QOS\_GEWU\_NOENT。 |

### OH\_QoS\_GewuSubmitRequest()

PhonePC/2in1TabletTVWearable

```
1. OH_QoS_GewuSubmitRequestResult OH_QoS_GewuSubmitRequest(OH_QoS_GewuSession session, const char* request, OH_QoS_GewuOnResponse callback, void* context)
```

**描述**

提交请求。请求的json字符串，支持以下字段：- messages: array. 表示消息的数组其中每个元素支持以下字段：- role: string. 消息的角色类型。- "developer": 开发者或系统提供的指示。- "user":用户输入。- "assistant": 模型生成结果。- content: string. 消息内容。- stream: boolean or null; 可选。是否使能流式推理，默认为非流式。json字符串例子：

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
| [OH\_QoS\_GewuSession](capi-qos-h.md#变量) session | 会话句柄，表示请求要提交到哪个会话。 |
| const char\* request | 请求的json字符串。 |
| [OH\_QoS\_GewuOnResponse](capi-qos-h.md#oh_qos_gewuonresponse) callback | 接受回复的回调。 |
| void\* context | 要传给回调的用户上下文指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_QoS\_GewuSubmitRequestResult](capi-qos-oh-qos-gewusubmitrequestresult.md) | 格物提交请求结果。  - 提交请求成功，返回值OH\_QoS\_GewuSubmitRequestResult里的error为OH\_QOS\_GEWU\_OK，request为请求句柄。  - 提交请求失败，返回值OH\_QoS\_GewuSubmitRequestResult里的error为错误原因，其中OH\_QOS\_GEWU\_NOMEM表示没有足够的内存处理该请求。 |
