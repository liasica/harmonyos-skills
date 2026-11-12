---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-clitoolevent
title: CliToolEvent (CLI工具会话事件)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > CliToolEvent (CLI工具会话事件)
category: harmonyos-references
scraped_at: 2026-11-12T09:53:33+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:aa3fff348764427aa46e851677e7788238b3a5f9238552cdd2a673e2c41b6f39
---

CliToolEvent用于描述CLI工具进程运行期间产生的会话事件信息。

**起始版本：** 26.0.1

## 导入模块

```ts
import { common } from '@kit.AbilityKit';
```

## CliToolEvent

CLI工具会话事件信息。

**起始版本：** 26.0.1

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| toolEventType | [ToolEventType](js-apis-inner-application-clitoolevent.md#tooleventtype) | 否 | 否 | CLI工具事件类型。 |
| data | string | 否 | 否 | CLI工具事件数据。 |

## ToolEventType

CLI工具会话事件类型。

**起始版本：** 26.0.1

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STDOUT | 'stdout' | 标准输出事件。 |
| STDERR | 'stderr' | 标准错误事件。 |
| EXIT | 'exit' | 进程退出事件。 |
| ERROR | 'error' | 进程错误事件。 |
