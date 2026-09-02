---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hmaf-a2a-dev-guide
title: 通过AgentAbilityExtension实现智能体间A2A协议通信
breadcrumb: 指南 > AI > Agent Framework Kit（智能体框架服务） > 通过AgentAbilityExtension实现智能体间A2A协议通信
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:04+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:99438097dfdc1a57ca9605ee36454e4dd1553b82ebf24ed39801f7e50078ff23
---

从API版本26.0.0开始，新增支持通过AgentAbilityExtension实现智能体间A2A协议通信。

A2A（Agent to Agent）协议用于智能体之间的通信。A2A服务端负责接收客户端请求、触发智能体执行任务、更新任务状态和返回执行结果。

通过Agent Framework Kit，开发者可以在ArkTS应用中构建支持A2A协议的Agent服务端，实现以下能力：

* 接收客户端的请求消息
* 触发智能体执行业务逻辑
* 更新任务状态和返回执行结果

## 基本概念

* **Agent Card（智能体卡片）**：一种JSON元数据文档，用于描述智能体的身份、能力、端点地址、技能和认证要求。客户端通过解析智能体卡片来发现智能体并了解如何安全有效地与其交互。
* **Task（任务）**：由智能体发起的具有唯一标识和明确定义生命周期的有状态工作单元。用于跟踪长时间运行的操作和支持多轮交互与协作。
* **Message（消息）**：客户端与智能体之间一次通信的单元，包含内容和角色（"user"或"agent"）。用于传递指令、上下文、问题、答案或状态更新。
* **Part（消息部件）**：消息和产物中使用的基础内容容器。一个部件可以包含以下内容之一：文本内容、文件引用（URL或内联字节）或结构化数据。
* **Artifact（产物）**：智能体在任务处理过程中生成的有形成果或具体结果（如文档、图片或结构化数据）。与通用消息不同，产物是实际的交付物，具有唯一的产物ID和名称。
* **Context（上下文）**：由服务端生成的标识符，用于逻辑上关联多个相关的任务对象，为一系列交互提供上下文。
* **TaskState（任务状态）**：任务可能处于的状态，包括已提交、工作中、需要用户输入、已完成、已取消、已失败、已拒绝、需要认证等。

## 业务功能介绍

A2A协议支持智能体之间的高效通信，其核心业务功能包括：

* **智能体发现**：通过Agent Card元数据文档，客户端可以发现智能体并了解其能力、端点地址和认证要求。
* **任务管理**：支持创建和管理具有明确生命周期的任务，支持长时间运行操作的跟踪和多轮交互。
* **消息传递**：支持客户端与智能体之间的单轮通信，传递指令、上下文、问题、答案或状态更新。
* **产物生成**：智能体在任务处理过程中可以生成有形的交付物（如文档、图片或结构化数据）。
* **状态更新**：支持任务状态的全程跟踪，包括已提交、工作中、需要用户输入、已完成、已取消、已失败、已拒绝、需要认证等状态。

## 业务流程

1. **客户端连接**：客户端通过Agent Card发现智能体后，与A2A Server建立连接。
2. **发送请求**：客户端构造请求消息并发送给服务端，请求触发智能体执行任务。
3. **处理任务**：服务端接收请求后，触发智能体执行业务逻辑，处理任务并生成产物。
4. **返回结果**：服务端更新任务状态和返回执行结果，客户端收到响应后完成本次交互。

## 接口说明

本模块提供A2A协议的服务端API，具体接口说明请参见[A2A Server模块API文档](../harmonyos-references/hmaf-a2a-protocol.md)。

主要接口包括：

| 接口名 | 说明 |
| --- | --- |
| [createA2AServer](../harmonyos-references/hmaf-a2a-protocol.md#createa2aserver) | 创建并获取Server实例，用于处理A2A协议通信。 |
| [Server](../harmonyos-references/hmaf-a2a-protocol.md#server) | 服务器实例接口，负责处理智能体通信和任务生命周期管理。 |
| [RequestContext](../harmonyos-references/hmaf-a2a-protocol.md#requestcontext) | 请求上下文接口，提供传入请求的上下文信息。 |
| [OnDataCallback](../harmonyos-references/hmaf-a2a-protocol.md#ondatacallback) | A2A Server收到客户端请求后，触发智能体执行的事件回调函数类型。 |
| [Message](../harmonyos-references/hmaf-a2a-protocol.md#message) | A2A通信中的消息单元。 |
| [Task](../harmonyos-references/hmaf-a2a-protocol.md#task) | A2A任务，包含任务状态、产物和历史消息。 |

## 开发步骤

### 导入所需模块

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common, Want, AgentExtensionAbility } from '@kit.AbilityKit';
import { RequestContext, createA2AServer, Server, TaskState, Role } from '@kit.AgentFrameworkKit';
```

### 业务功能实现步骤

推荐在服务端继承[AgentExtensionAbility](../harmonyos-references/js-apis-app-agent-agentextensionability.md)，以实现跨App进程通信的能力。AgentExtensionAbility提供了基于IPC的请求处理回调接口。

参考以下步骤，实现每一个AgentExtensionAbility中的方法。

1. 创建OnDataCallback，定义Agent的业务处理逻辑。

   ```typescript
   const TAG = '=====A2AServer===='
   export default class MyAgentExtensionAbility extends AgentExtensionAbility {
     private server: Server | null = null;

     // OnDataCallback函数
     private agentOnData = (method: string, context: RequestContext) => {
       // 从结构化的上下文参数context中，获取AgentID等信息
       const agentId: string = context.getAgentId() ?? '';
       if (!agentId) {
           hilog.error(0x0000, TAG, 'Agent ID not found in request context');
           return;
       }
       const taskId: string = context.getTaskId() ?? '';
       switch (method) {
         case 'Execute':
           // 使用server.updateStatus，更新任务执行状态
           this.server?.updateStatus(taskId, {
               state: TaskState.WORKING,
               message: {
                   messageId: 'msg1',
                   role: Role.AGENT,
                   parts: [{
                       mediaType: 'text/plain',
                       text: 'Starting work on your request...'
                   }]
               }
           });

           // 等待Agent生成产物
           this.server?.addArtifact(taskId, {
               artifactId: 'result-artifact',
               parts: [{
                   mediaType: 'text/plain',
                   text: '{"action": "completed", "result": "Task finished successfully"}'
               }]
           });

           // 通知任务完成
           this.server?.updateStatus(taskId, {
               state: TaskState.COMPLETED,
               message: {
                   messageId: 'msg3',
                   role: Role.AGENT,
                   parts: [{
                       mediaType: 'text/plain',
                       text: 'Task completed successfully!'
                   }]
               }
           });
           break;
         case 'Cancel':
           // 根据AgentId，通知Agent处理取消任务的请求
           hilog.info(0x0000, TAG, 'Cancel called');
           break;
         case 'PerceptionSuggest':
           hilog.info(0x0000, TAG, `Perception suggest called, metadata: ${JSON.stringify(context.getMetadata(), null, 2)}`);
           break;
         default:
           break;
       }
     }
   }
   ```
2. 实现onCreate方法，确保在首次收到请求时调用createA2AServer创建A2A Server对象。

   ```typescript
   async onCreate(want: Want) {
      try {
        const card = this.context.agentCard;
        this.server = createA2AServer(card, this.agentOnData, want=want);
      } catch (error) {
        hilog.error(0x0000, TAG, `Failed to create server: ${error}`);
      }
   }
   ```
3. 实现onConnect，客户端建连时触发，启动服务端。

   ```typescript
   onConnect(want: Want, proxy: common.AgentHostProxy) {
     // 客户端连接时触发的回调
     this.server?.start();
   }
   ```
4. 接收客户端请求时触发onData，需要调用server.onMessage传递请求体。

   ```typescript
   async onData(proxy: common.AgentHostProxy, data: string) {
     // 处理请求的回调函数
     this.server?.onMessage(data, (response: string) => {
        proxy.sendData(response);
     });
   }
   ```
5. 客户端断开连接时，在onDisconnect中关闭服务端。

   ```typescript
   onDisconnect(want: Want, proxy: common.AgentHostProxy) {
     // 客户端断开连接时触发的回调
     this.server?.stop();
   }
   ```
6. 服务对象销毁时触发onDestroy。

   ```typescript
   onDestroy() {
     // 清理资源
     this.server?.stop();
   }
   ```

### 完整示例

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common, Want, AgentExtensionAbility } from '@kit.AbilityKit';
import { RequestContext, createA2AServer, Server, TaskState, Role } from '@kit.AgentFrameworkKit';

const TAG = '=====A2AServer===='
export default class MyAgentExtensionAbility extends AgentExtensionAbility {
  private server: Server | null = null;

  // OnDataCallback函数
  private agentOnData = (method: string, context: RequestContext) => {
    // 从结构化的上下文参数context中，获取AgentID等信息
    const agentId: string = context.getAgentId() ?? '';
    if (!agentId) {
      hilog.error(0x0000, TAG, 'Agent ID not found in request context');
      return;
    }
    const taskId: string = context.getTaskId() ?? '';
    switch (method) {
      case 'Execute':
        // 使用server.updateStatus，更新任务执行状态
        this.server?.updateStatus(taskId, {
          state: TaskState.WORKING,
          message: {
            messageId: 'msg1',
            role: Role.AGENT,
            parts: [{
              mediaType: 'text/plain',
              text: 'Starting work on your request...'
            }]
          }
        });

        // 等待Agent生成产物
        this.server?.addArtifact(taskId, {
          artifactId: 'result-artifact',
          parts: [{
            mediaType: 'text/plain',
            text: '{"action": "completed", "result": "Task finished successfully"}'
          }]
        });

        // 通知任务完成
        this.server?.updateStatus(taskId, {
          state: TaskState.COMPLETED,
          message: {
            messageId: 'msg3',
            role: Role.AGENT,
            parts: [{
              mediaType: 'text/plain',
              text: 'Task completed successfully!'
            }]
          }
        });
        break;
      case 'Cancel':
        // 根据AgentId，通知Agent处理取消任务的请求
        hilog.info(0x0000, TAG, 'Cancel called');
        break;
      case 'PerceptionSuggest':
        hilog.info(0x0000, TAG, `Perception suggest called, metadata: ${JSON.stringify(context.getMetadata(), null, 2)}`);
        this.server?.updateStatus(taskId, {
          state: TaskState.COMPLETED,
          message: {
            messageId: 'onChipsMsg1',
            role: Role.AGENT,
            parts: [{
              mediaType: 'text/plain',
              text: 'On chips task completed successfully!'
            }]
          }
        });
      default:
        break;
    }
  }

  async onCreate(want: Want) {
    try {
      const card = this.context.agentCard;
      this.server = createA2AServer(card, this.agentOnData, want=want);
    } catch (error) {
      hilog.error(0x0000, TAG, `Failed to create server: ${error}`);
    }
  }

  onConnect(want: Want, proxy: common.AgentHostProxy) {
    // 客户端连接时触发的回调
    this.server?.start();
  }

  async onData(proxy: common.AgentHostProxy, data: string) {
    // 处理请求的回调函数
    this.server?.onMessage(data, (response: string) => {
      proxy.sendData(response);
    });
  }

  onDisconnect(want: Want, proxy: common.AgentHostProxy) {
    // 客户端断开连接时触发的回调
    this.server?.stop();
  }

  onDestroy() {
    // 清理资源
    this.server?.stop();
  }
}
```

### A2A智能体发送AgentChips数据示例

AgentChips请求用于小艺应用感知用户当前所在App，向Agent请求推荐内容。本小节提供了一个App端回复小艺AgentChips请求的示例。

参考[小艺AgentChips交互流程](../service/agent2agent-chips-0000002660585431.md)，小艺会向AgentExtensionAbility所在的App发送一个PerceptionSuggest类型的请求。

通过定义OnDataCallback中method为'PerceptionSuggest'的处理流程，Agent即可按照小艺AgentChips交互流程的示例报文格式进行回复。

AgentChips场景下OnDataCallback的实现示例：

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common, Want, AgentExtensionAbility } from '@kit.AbilityKit';
import { RequestContext, createA2AServer, Server, TaskState, Role, OnDataCallback } from '@kit.AgentFrameworkKit';

const TAG = '=====A2AServer===='
export default class MyAgentExtensionAbility extends AgentExtensionAbility {
  private server: Server | null = null;
  // 定义Agent业务处理逻辑
  private agentOnData: OnDataCallback = (method: string, context: RequestContext) => {
    switch (method) {
      // 小艺请求类型为PerceptionSuggest，Agent可以按示例报文格式回复推荐内容
      case 'PerceptionSuggest':
        // 获取任务ID
        const taskId = context.getTaskId();

        // 生成ArtifactID，示例中为固定值
        const artId = 'artifact-1';

        if (!taskId) {
          console.error(TAG, "Task ID not found in request context");
          return;
        }

        // 模拟Agent分析推荐结果，将推荐结果返回给小艺
        this.server?.addArtifact(taskId, {
          artifactId: artId,
          parts: [
            {
              data: {
                suggestionCandidates: [
                  {
                    text: "最新的电视剧",
                    reply: "最新的电视剧"
                  }
                ]
              },
              mediaType: "application/json"
            }
          ],
          append: false,
          lastChunk: true
        });

        // 通知AgentChips任务完成
        this.server?.updateStatus(taskId, {
          state: TaskState.COMPLETED,
          message: {
            messageId: "demo-msg-123",
            role: Role.AGENT,
            parts: [{
              mediaType: "text/plain",
              text: "Task completed successfully!"
            }]
          }
        });

        break;
      default:
        break;
    }
  }

  async onCreate(want: Want) {
    try {
      const card = this.context.agentCard;
      this.server = createA2AServer(card, this.agentOnData, want=want);
    } catch (error) {
      hilog.error(0x0000, TAG, `Failed to create server: ${error}`);
    }
  }

  onConnect(want: Want, proxy: common.AgentHostProxy) {
    // 客户端连接时触发的回调
    this.server?.start();
  }

  async onData(proxy: common.AgentHostProxy, data: string) {
    // 处理请求的回调函数
    this.server?.onMessage(data, (response: string) => {
      proxy.sendData(response);
    });
  }

  onDisconnect(want: Want, proxy: common.AgentHostProxy) {
    // 客户端断开连接时触发的回调
    this.server?.stop();
  }

  onDestroy() {
    // 清理资源
    this.server?.stop();
  }
}
```
