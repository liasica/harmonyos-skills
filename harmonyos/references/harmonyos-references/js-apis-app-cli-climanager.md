---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-cli-climanager
title: "@ohos.app.cli.cliManager (CLI工具管理)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.cli.cliManager (CLI工具管理)
category: harmonyos-references
scraped_at: 2026-11-12T09:53:30+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:7d4e4376fb5cbde8531a5b9dfc0c8be5c3f2b67d7829f16b49bd9cbdce2d6590
---

本模块提供三方应用与系统命令行工具（CLI）的交互能力，可以执行Shell命令，以及管理会话。会话在调用execCmd接口时创建，用于跟踪命令的执行状态和结果。

**起始版本：** 26.0.1

## 导入模块

```ts
import { cliManager } from '@kit.AbilityKit';
```

## ExecCmdOptions

执行Shell命令的可选参数。可用于指定工作目录、环境变量、是否后台运行、前台执行时长、超时时长、安全策略及事件回调。

**起始版本：** 26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| workDir | string | 否 | 是 | 命令执行的工作目录，如果不传或传空，则为根目录。 |
| env | Record<string, string> | 否 | 是 | 命令执行的环境变量。 |
| background | boolean | 否 | 是 | 表示命令是否后台执行。  true：后台执行，false：前台执行。  默认值：false。 |
| yieldMs | number | 否 | 是 | 命令前台执行时长，单位为毫秒。取值范围：0 ~ 1000 \* timeout，默认值：0。超出取值范围时抛出错误码401。 |
| timeout | number | 否 | 是 | 命令执行超时时长，单位为秒。取值范围：0 ~ 1800。默认值：1800，传0表示不会超时。超出取值范围时抛出错误码401。 |
| policy | string | 否 | 是 | 安全策略，参数格式为JSON字符串。 |
| callback | [ToolEventCallback](js-apis-inner-application-tooleventcallback.md) | 否 | 是 | 事件回调函数，用于接收工具事件。若提供该参数，将自动订阅会话事件。 |

## ExecResult

CLI工具执行的结果。包含CLI工具的退出码、标准输出、标准错误输出、终止信号、是否超时及执行时长。

**起始版本：** 26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| exitCode | number | 否 | 是 | 工具的退出码。默认值：undefined。 |
| outputText | string | 否 | 是 | 工具的标准输出（stdout）。默认值：undefined。 |
| errorText | string | 否 | 是 | 工具的标准错误输出（stderr）。默认值：undefined。 |
| signalNumber | number | 否 | 是 | 工具的终止信号。默认值：undefined。 |
| timeOut | boolean | 否 | 否 | 工具的执行是否超时。true表示超时，false表示未超时。默认值：false。 |
| executionTime | number | 否 | 否 | 工具的执行时长。单位：ms。默认值：0。 |

## SessionStatus

执行CLI工具时，系统会为调用方和CLI工具建立一个会话，此字段描述会话状态。

**起始版本：** 26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RUNNING | 'running' | 会话正在进行中。 |
| COMPLETED | 'completed' | 会话已完成。 |
| FAILED | 'failed' | 会话发生失败。 |

## CliSessionInfo

执行CLI工具时，系统会为调用方和CLI工具建立一个会话，此字段描述会话信息的格式。

**起始版本：** 26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sessionId | string | 否 | 否 | 会话id。 |
| toolName | string | 否 | 否 | 工具名称。 |
| status | [SessionStatus](js-apis-app-cli-climanager.md#sessionstatus) | 否 | 否 | 会话状态。 |
| result | [ExecResult](js-apis-app-cli-climanager.md#execresult) | 否 | 是 | 工具执行结果。默认值：undefined。 |

## cliManager.execCmd

execCmd(cmd: string, execCmdOptions?: ExecCmdOptions): Promise<CliSessionInfo>

执行Shell命令，返回会话信息。使用Promise异步回调。

**起始版本：** 26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**需要权限**：ohos.permission.EXEC\_CLI\_TOOL（仅系统应用可配置）或 ohos.permission.EXEC\_PUBLIC\_CLI\_TOOL

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**设备行为差异**：该接口在PC/2in1中可正常调用，在其他设备类型中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cmd | string | 是 | 要执行的Shell命令。 |
| execCmdOptions | [ExecCmdOptions](js-apis-app-cli-climanager.md#execcmdoptions) | 否 | 执行命令的可选参数。默认值：详见[ExecCmdOptions](js-apis-app-cli-climanager.md#execcmdoptions)的具体属性默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CliSessionInfo](js-apis-app-cli-climanager.md#clisessioninfo)> | Promise对象。返回会话信息。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 35600031 | Maximum number of processes has been reached. |
| 35600050 | System Error. 1. Failed to connect to the system service; 2. The system service failed to communicate with the dependent module. |

**示例：**

```ts
import { cliManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let cmd: string = 'ls -l';
  let options: cliManager.ExecCmdOptions = {
    background: false,
    timeout: 60,
    workDir: '/system/bin',
    callback: {
      onEvent: (event) => {
        hilog.info(0x0000, 'CliManager', 'event type: %{public}s, data: %{public}s', event.toolEventType, event.data);
      }
    }
  };
  cliManager.execCmd(cmd, options).then((sessionInfo) => {
    hilog.info(0x0000, 'CliManager', 'execCmd success, sessionId: %{public}s, status: %{public}s',
      sessionInfo.sessionId, sessionInfo.status);
  }).catch((error: BusinessError) => {
    hilog.error(0x0000, 'CliManager', 'execCmd failed, code: %{public}d, message: %{public}s', error.code, error.message);
  });
} catch (error) {
  hilog.error(0x0000, 'CliManager', 'execCmd failed, error: %{public}s', JSON.stringify(error));
}
```

## cliManager.subscribeSession

subscribeSession(sessionId: string, callback: ToolEventCallback): Promise<void>

订阅指定CLI工具会话的事件。会话运行期间，CLI工具产生的标准输出、标准错误、退出或错误事件通过回调返回。

**说明** 

* 会话仅限创建进程管理：只有调用execCmd创建该会话的进程可以调用本接口。其他进程即使获取到sessionId，调用本接口也会抛出错误码201（Permission denied）。
* 如果在调用[execCmd](js-apis-app-cli-climanager.md#climanagerexeccmd)时已通过[ExecCmdOptions](js-apis-app-cli-climanager.md#execcmdoptions)的callback参数提供了事件回调，则无需再调用本接口。

**起始版本：** 26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**需要权限**：ohos.permission.EXEC\_CLI\_TOOL（系统应用可配置）或 ohos.permission.EXEC\_PUBLIC\_CLI\_TOOL

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | string | 是 | 目标CLI工具进程的会话ID。 |
| callback | [ToolEventCallback](js-apis-inner-application-tooleventcallback.md) | 是 | CLI工具会话事件的回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 35600032 | The specified session does not exist. |
| 35600050 | System Error. 1. Failed to connect to the system service; 2. The system service failed to communicate with the dependent module. |

**示例：**

```ts
import { cliManager, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let sessionId = 'example_session_id';
// 定义CLI工具会话事件回调
let callback: common.ToolEventCallback = {
  onEvent: (event: common.CliToolEvent) => {
    hilog.info(0x0000, 'CliManager', 'subscribeSession event type: %{public}s, data: %{public}s',
      event.toolEventType, event.data);
  }
};

try {
  // 订阅指定会话的事件
  cliManager.subscribeSession(sessionId, callback).then(() => {
    hilog.info(0x0000, 'CliManager', 'subscribeSession success.');
  }).catch((error: BusinessError) => {
    hilog.error(0x0000, 'CliManager', 'subscribeSession failed, code: %{public}d, message: %{public}s',
      error.code, error.message);
  });
} catch (error) {
  hilog.error(0x0000, 'CliManager', 'subscribeSession failed, error: %{public}s', JSON.stringify(error));
}
```

## cliManager.clearSession

clearSession(sessionId: string): Promise<void>

关闭指定CLI工具会话，并强制结束对应的工具进程。

**说明** 

* 会话仅限创建进程管理：只有调用execCmd创建该会话的进程可以调用本接口。其他进程即使获取到sessionId，调用本接口也会抛出错误码201（Permission denied）。

**起始版本：** 26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**需要权限**：ohos.permission.EXEC\_CLI\_TOOL（系统应用可配置）或 ohos.permission.EXEC\_PUBLIC\_CLI\_TOOL

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | string | 是 | 目标CLI工具进程的会话ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 35600032 | The specified session does not exist. |
| 35600050 | System Error. 1. Failed to connect to the system service; 2. The system service failed to communicate with the dependent module. |

**示例：**

```ts
import { cliManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let sessionId = 'example_session_id';
try {
  // 清除指定会话
  cliManager.clearSession(sessionId).then(() => {
    hilog.info(0x0000, 'CliManager', 'clearSession success.');
  }).catch((error: BusinessError) => {
    hilog.error(0x0000, 'CliManager', 'clearSession failed, code: %{public}d, message: %{public}s',
      error.code, error.message);
  });
} catch (error) {
  hilog.error(0x0000, 'CliManager', 'clearSession failed, error: %{public}s', JSON.stringify(error));
}
```

## cliManager.querySession

querySession(sessionId: string): Promise<CliSessionInfo>

查询指定CLI工具会话的状态和执行结果。

**说明** 

* 会话仅限创建进程管理：只有调用execCmd创建该会话的进程可以调用本接口。其他进程即使获取到sessionId，调用本接口也会抛出错误码201（Permission denied）。

**起始版本：** 26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**需要权限**：ohos.permission.EXEC\_CLI\_TOOL（仅系统应用可配置）或ohos.permission.EXEC\_PUBLIC\_CLI\_TOOL

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | string | 是 | 目标CLI工具进程的会话ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CliSessionInfo](js-apis-app-cli-climanager.md#clisessioninfo)> | Promise对象，返回CLI工具会话信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 35600032 | The specified session does not exist. |
| 35600050 | System Error. 1. Failed to connect to the system service; 2. The system service failed to communicate with the dependent module. |

**示例：**

```ts
import { cliManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let sessionId = 'example_session_id';
try {
  // 查询指定会话的状态和执行结果
  cliManager.querySession(sessionId).then((sessionInfo) => {
    hilog.info(0x0000, 'CliManager', 'querySession success, status: %{public}s', sessionInfo.status);
  }).catch((error: BusinessError) => {
    hilog.error(0x0000, 'CliManager', 'querySession failed, code: %{public}d, message: %{public}s',
      error.code, error.message);
  });
} catch (error) {
  hilog.error(0x0000, 'CliManager', 'querySession failed, error: %{public}s', JSON.stringify(error));
}
```

## cliManager.sendMessage

sendMessage(sessionId: string, message: string): Promise<void>

向指定CLI工具会话对应的进程发送消息。

**说明** 

* 会话仅限创建进程管理：只有调用execCmd创建该会话的进程可以调用本接口。其他进程即使获取到sessionId，调用本接口也会抛出错误码201（Permission denied）。

**起始版本：** 26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**需要权限**：ohos.permission.EXEC\_CLI\_TOOL（系统应用可配置）或 ohos.permission.EXEC\_PUBLIC\_CLI\_TOOL

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | string | 是 | 目标CLI工具进程的会话ID。 |
| message | string | 是 | 要发送的消息，最大长度为10240字符。超过最大长度时抛出错误码401。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 35600032 | The specified session does not exist. |
| 35600033 | Failed to write message to the tool process. |
| 35600050 | System Error. 1. Failed to connect to the system service; 2. The system service failed to communicate with the dependent module. |

**示例：**

```ts
import { cliManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let sessionId = 'example_session_id';
let message = 'example message';
try {
  // 向指定会话发送消息
  cliManager.sendMessage(sessionId, message).then(() => {
    hilog.info(0x0000, 'CliManager', 'sendMessage success.');
  }).catch((error: BusinessError) => {
    hilog.error(0x0000, 'CliManager', 'sendMessage failed, code: %{public}d, message: %{public}s',
      error.code, error.message);
  });
} catch (error) {
  hilog.error(0x0000, 'CliManager', 'sendMessage failed, error: %{public}s', JSON.stringify(error));
}
```
