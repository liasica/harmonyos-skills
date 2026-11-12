---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-tooleventcallback
title: ToolEventCallback (CLI工具事件回调)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > ToolEventCallback (CLI工具事件回调)
category: harmonyos-references
scraped_at: 2026-11-12T09:53:33+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:274b7ff8738986903106cf269fff348855e2c9eb291b5110848f437abc40acca
---

ToolEventCallback用于接收CLI工具进程运行期间产生的会话事件。

**起始版本：** 26.0.1

**说明** 

本模块接口仅可在Stage模型下使用。

## 导入模块

```ts
import { common } from '@kit.AbilityKit';
```

## OnEventFn

type OnEventFn = (event: CliToolEvent) => void

CLI工具会话事件的回调函数类型。

**起始版本：** 26.0.1

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [CliToolEvent](js-apis-inner-application-clitoolevent.md#clitoolevent) | 是 | CLI工具进程运行期间产生的会话事件。 |

## ToolEventCallback

CLI工具会话事件的回调接口。

**起始版本：** 26.0.1

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onEvent | [OnEventFn](js-apis-inner-application-tooleventcallback.md#oneventfn) | 否 | 否 | CLI工具会话事件回调函数。 |

**示例：**

```ts
import { common } from '@kit.AbilityKit';

// 定义CLI工具会话事件的回调对象
let callback: common.ToolEventCallback = {
  onEvent: (event: common.CliToolEvent) => {
    console.info('tool event type: ' + event.toolEventType + ', data: ' + event.data);
  }
};
```
