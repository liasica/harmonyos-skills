---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/hmaf-a2a-protocol
title: A2A (A2A协议)
breadcrumb: API参考 > AI > Agent Framework Kit（智能体框架服务） > ArkTS API > A2A (A2A协议)
category: harmonyos-references
scraped_at: 2026-09-05T06:21:31+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:7c7a07892554192228819d5385c7ced62041ca0873327dc9c591bf4658ca12eb
---

本模块提供A2A（Agent to Agent）协议的服务端实现能力，包括创建A2A Server实例、处理客户端请求、管理任务状态和Artifact（智能体执行任务的产物）等。

A2A协议用于智能体之间的通信，A2A Server端负责接收客户端请求、触发智能体执行任务、更新任务状态和返回执行结果。

**起始版本：** 26.0.0

## 导入模块

```typescript
import { Role, TaskState, Part, Message, Artifact, TaskStatus, Task, OnDataCallback, createA2AServer, ProxySender,
    Server, RequestContext, TaskArtifactParam } from '@kit.AgentFrameworkKit';
```

## createA2AServer

createA2AServer(agentCard: common.AgentCard, onData: OnDataCallback, want?: Want): Server

创建并获取Server实例，用于处理A2A协议通信。调用此方法后，将创建A2A服务端实例并准备启动。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agentCard | [common.AgentCard](js-apis-app-ability-common.md#agentcard24) | 是 | AgentCard信息。 |
| onData | [OnDataCallback](hmaf-a2a-protocol.md#ondatacallback) | 是 | 智能体数据处理回调函数。 |
| want | [Want](js-apis-app-ability-want.md) | 否 | 包含A2A版本信息的Want对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Server](hmaf-a2a-protocol.md#server) | 创建的A2A Server实例。该Server实例可用于调用start()、stop()、onMessage()等方法以控制A2A服务端行为。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-agent-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1022400010 | Invalid parameter |
| 1022420001 | Memory allocation failed |

**示例：**

```typescript
import { Want, AgentExtensionAbility } from '@kit.AbilityKit';
import { createA2AServer, Server, RequestContext, OnDataCallback } from '@kit.AgentFrameworkKit';

export default class MyAgentExtensionAbility extends AgentExtensionAbility {
  private server: Server | null = null;

  private agentOnData: OnDataCallback = (method: string, context: RequestContext) => {
    // 处理来自客户端的智能体操作请求，根据method类型执行相应业务逻辑
  }

  async onCreate(want: Want) {
    try {
      const card = this.context.agentCard;
      this.server = createA2AServer(card, this.agentOnData, want);
    } catch (error) {
      console.error(`Failed to create server: ${error}`);
    }
  }
}
```

## OnDataCallback

type OnDataCallback = (method: string, context: RequestContext) => void

A2A Server收到客户端请求后，触发智能体执行的事件回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| method | string | 是 | 智能体操作类型。包括以下取值：  'Execute'：触发执行操作。小艺发送"对话交互"、"长任务陪伴"、"UI控制陪伴"或"原生控制"等消息时触发，此时客户端使用的方法为"SendMessage"或"SendStreamingMessage"。智能体应从context中读取必要信息，通过updateStatus更新任务状态，并通过addArtifact返回产物。一旦状态更新为非WORKING或非SUBMITTED状态，则认为本次执行完成。  'Cancel'：触发取消操作。当客户端发送"CancelTask"请求时触发。智能体应尝试停止context中指定的任务。  'PerceptionSuggest'：触发感知建议操作。小艺在初始化期间使用此方法获取智能体的感知建议chips。智能体应从context中读取必要信息，通过updateStatus更新任务状态，并通过addArtifact返回产物。一旦状态更新为非WORKING或非SUBMITTED状态，则认为本次执行完成。详见[感知建议chips](../service/agent2agent-chips-0000002660585431.md)。  'GetOpening'：获取应用开场白操作。小艺在初始化期间使用此方法从应用的智能体获取开场白。  其他A2A方法：有关支持的A2A消息指令完整列表，请参见[A2A消息指令定义](../service/agent2agent-message-0000002630186256.md)。 |
| context | [RequestContext](hmaf-a2a-protocol.md#requestcontext) | 是 | 请求上下文对象。 |

## ProxySender

type ProxySender = (data: string) => void

回调函数类型，通过代理将A2A响应数据发送给客户端。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 | 发送给客户端的数据。 |

## Server

服务器实例接口，负责处理智能体通信和任务生命周期管理。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

### start

start(): void

启动A2A服务端实例。

**说明** 

该接口调用后，退出时应使用[stop](hmaf-a2a-protocol.md#stop)方法停止服务器实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

**示例：**

```typescript
// server对象通过createA2AServer接口创建
server.start();
```

### stop

stop(): void

停止服务器实例。

**说明** 

该接口调用前，应先调用[start](hmaf-a2a-protocol.md#start)方法启动A2A服务端实例，否则不会产生实际作用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

**示例：**

```typescript
// server对象通过createA2AServer接口创建
server.stop();
```

### onMessage

onMessage(data: string, sender: ProxySender): void

A2A服务端处理来自A2A客户端的消息请求，并将响应发送回客户端。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 | 客户端请求的JSON字符串。 |
| sender | [ProxySender](hmaf-a2a-protocol.md#proxysender) | 是 | 响应回调函数，用于发送响应给客户端。 |

**示例：**

```typescript
// server对象通过createA2AServer接口创建
// data是通过传输层获取的客户端的请求数据
// proxy提供外部定义的消息发送接口
server.onMessage(data, (response: string) => {
  proxy.sendData(response);
});
```

### onAuth

onAuth(data: string): string

A2A服务端处理来自A2A客户端的密钥协商请求。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 | 客户端的密钥协商请求，包含客户端公钥信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 密钥协商信息，包含服务端公钥。 |

**示例：**

```typescript
// server对象通过createA2AServer接口创建
// data是通过传输层获取的客户端的鉴权数据
const authResp: string = server.onAuth(data);
```

### updateStatus

updateStatus(taskId: string, status: TaskStatus): void

更新任务状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| taskId | string | 是 | 任务唯一标识，必须为UUID格式，格式为xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx。 |
| status | [TaskStatus](hmaf-a2a-protocol.md#taskstatus) | 是 | 新的任务状态。 |

**示例：**

```typescript
// server对象通过createA2AServer接口创建
// taskId是通过RequestContext的getTaskId接口获取的任务ID
server.updateStatus(taskId, {
  state: TaskState.COMPLETED,
  message: {
    messageId: 'msg1',
    role: Role.AGENT,
    parts: [{
      text: 'Task completed'
    }]
  }
});
```

### addArtifact

addArtifact(taskId: string, taskArtifactParam: TaskArtifactParam): void

添加任务智能体产物信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| taskId | string | 是 | 任务唯一标识。 |
| taskArtifactParam | [TaskArtifactParam](hmaf-a2a-protocol.md#taskartifactparam) | 是 | 产物更新参数。 |

**示例：**

```typescript
// server对象通过createA2AServer接口创建
// taskId是通过RequestContext的getTaskId接口获取的任务ID
server.addArtifact(taskId, {
  artifactId: 'result-artifact-id',
  parts: [{
    mediaType: 'application/json',
    data: {'action': 'completed', 'result': 'Task finished successfully'}
  }]
});
```

## RequestContext

提供传入请求的上下文信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

### getAgentId

getAgentId(): string | undefined

获取智能体ID。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | undefined | 智能体ID，若不存在则返回undefined。 |

**示例：**

```typescript
// context对象在实现OnDataCallback接口时，作为参数获取
const agentId: string = context.getAgentId() ?? '';
```

### getUserInput

getUserInput(delimiter?: string): string

获取用户输入内容。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| delimiter | string | 否 | 分隔符，用于分隔多条用户输入。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 用户输入的内容。 |

**示例：**

```typescript
// context对象在实现OnDataCallback接口时，作为参数获取
const userInput: string = context.getUserInput(',');
```

### getMessage

getMessage(): Message | undefined

获取A2A客户端请求中的消息体对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Message](hmaf-a2a-protocol.md#message) | undefined | 消息对象，若不存在则返回undefined。 |

**示例：**

```typescript
// context对象在实现OnDataCallback接口时，作为参数获取
const message = context.getMessage();
```

### getRelatedTasks

getRelatedTasks(): Task[]

获取关联任务列表。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Task](hmaf-a2a-protocol.md#task)[] | 关联任务数组。 |

**示例：**

```typescript
// context对象在实现OnDataCallback接口时，作为参数获取
const relatedTasks: Task[] = context.getRelatedTasks();
```

### getCurrentTask

getCurrentTask(): Task | undefined

获取当前任务。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Task](hmaf-a2a-protocol.md#task) | undefined | 当前任务对象，若不存在则返回undefined。 |

**示例：**

```typescript
// context对象在实现OnDataCallback接口时，作为参数获取
const currentTask = context.getCurrentTask();
```

### getTaskId

getTaskId(): string | undefined

获取任务ID。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | undefined | 任务ID，若不存在则返回undefined。 |

**示例：**

```typescript
// context对象在实现OnDataCallback接口时，作为参数获取
const taskId: string = context.getTaskId() ?? '';
```

### getContextId

getContextId(): string | undefined

获取上下文ID。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | undefined | 上下文ID，若不存在则返回undefined。 |

**示例：**

```typescript
// context对象在实现OnDataCallback接口时，作为参数获取
const contextId: string = context.getContextId() ?? '';
```

### getMetadata

getMetadata(): object

获取客户端请求的元数据，用于附带额外的请求信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| object | 元数据。 |

**示例：**

```typescript
// context对象在实现OnDataCallback接口时，作为参数获取
const metadata: object = context.getMetadata();
```

## TaskArtifactParam

任务产物更新参数接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| parts | [Part](hmaf-a2a-protocol.md#part)[] | 否 | 否 | 产物内容部件数组。 |
| artifactId | string | 否 | 是 | 产物唯一标识。 |
| name | string | 否 | 是 | 产物名称。 |
| metadata | object | 否 | 是 | 产物元数据，需要支持JSON序列化。 |
| append | boolean | 否 | 是 | 是否在任务历史记录中将当前的parts数组追加到有相同ID的产物中。true: 追加到现有的相同ID的产物，false: 在产物列表中新增一项。默认值：false。 |
| lastChunk | boolean | 否 | 是 | 是否为最后一个数据块。true: 是最后一个数据块，false: 不是最后一个数据块。默认值：false。 |
| extensions | string[] | 否 | 是 | 扩展URI列表。 |

## TaskState

任务状态枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUBMITTED | 0 | 任务已提交。 |
| WORKING | 1 | 任务正在处理中。 |
| INPUT\_REQUIRED | 2 | 任务需要用户输入才能继续。 |
| COMPLETED | 3 | 任务已成功完成。 |
| CANCELED | 4 | 任务已取消。 |
| FAILED | 5 | 任务已失败。 |
| REJECTED | 6 | 任务已拒绝。 |
| AUTH\_REQUIRED | 7 | 任务需要认证才能继续。 |
| UNSPECIFIED | 8 | 任务状态未指定。 |

## Role

消息发送者角色枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AGENT | 0 | 智能体角色。 |
| USER | 1 | 用户角色。 |
| UNSPECIFIED | 2 | 未指定角色。 |

## Message

消息接口，表示A2A通信中的消息单元。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| messageId | string | 否 | 否 | 消息唯一标识，UUID格式。 |
| role | [Role](hmaf-a2a-protocol.md#role) | 否 | 否 | 消息发送者角色。 |
| parts | [Part](hmaf-a2a-protocol.md#part)[] | 否 | 否 | 消息内容部件数组。 |
| contextId | string | 否 | 是 | 上下文ID，UUID格式。 |
| extensions | string[] | 否 | 是 | 扩展URI列表。 |
| metadata | object | 否 | 是 | 元数据，需要支持JSON序列化。 |
| referenceTaskIds | string[] | 否 | 是 | 引用的任务ID列表。 |
| taskId | string | 否 | 是 | 任务ID，UUID格式。 |

## Part

消息内容接口，支持文本、原始数据、URL、媒体等类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | string | 否 | 是 | 文本内容。 |
| raw | string | 否 | 是 | 原始数据内容。 |
| url | string | 否 | 是 | 指向文件内容的URL，必须符合标准URL规范，例如'file://'、'https://'、'http://'。 |
| data | object | string | number | boolean | 否 | 是 | 任意支持JSON序列化的对象、字符串、数字、布尔值。 |
| mediaType | string | 否 | 是 | Part内容的媒体类型（MIME类型），例如'text/plain'、'application/json'、'image/png'。 |
| filename | string | 否 | 是 | 文件名，例如'document.pdf'。 |
| metadata | object | 否 | 是 | 元数据，需要支持JSON序列化。 |

## Task

任务接口，表示A2A任务，包含任务状态、产物和历史消息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 任务唯一标识，UUID格式。 |
| contextId | string | 否 | 否 | 上下文ID，UUID格式。 |
| status | [TaskStatus](hmaf-a2a-protocol.md#taskstatus) | 否 | 否 | 任务状态。 |
| artifacts | [Artifact](hmaf-a2a-protocol.md#artifact)[] | 否 | 是 | 任务产物列表。 |
| history | [Message](hmaf-a2a-protocol.md#message)[] | 否 | 是 | 历史消息列表。 |
| metadata | object | 否 | 是 | 元数据，需要支持JSON序列化。 |

## TaskStatus

任务状态接口，表示任务当前状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | [TaskState](hmaf-a2a-protocol.md#taskstate) | 否 | 否 | 任务状态。 |
| timestamp | string | 否 | 是 | 状态记录时间，ISO 8601格式时间戳。 |
| message | [Message](hmaf-a2a-protocol.md#message) | 否 | 是 | 状态更新附加的相关消息，默认为空。 |

## Artifact

智能体产物接口，表示任务产生的资源。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| artifactId | string | 否 | 否 | 智能体产物唯一标识，UUID格式。 |
| parts | [Part](hmaf-a2a-protocol.md#part)[] | 否 | 否 | 智能体产物内容部件数组，至少包含一个部件。 |
| description | string | 否 | 是 | 智能体产物的描述。 |
| extensions | string[] | 否 | 是 | 扩展URI列表。 |
| metadata | object | 否 | 是 | 元数据，需要支持JSON序列化。 |
| name | string | 否 | 是 | 智能体产物的名称。 |
