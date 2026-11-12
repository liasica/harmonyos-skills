---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-childprocessrunninginfo
title: ChildProcessInformation
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > ChildProcessInformation
category: harmonyos-references
scraped_at: 2026-11-12T09:53:32+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:cc9366d82d91bc300991358b25f92fe007edf702e1765876620d5ed152e09566
---

ChildProcessInformation定义子进程信息，包括子进程的PID、父进程PID及子进程名称等，可以通过[getChildProcessInfos](js-apis-app-ability-childprocessmanager.md#childprocessmanagergetchildprocessinfos)、[getUIAbilityChildProcessInfos](js-apis-inner-application-applicationcontext.md#applicationcontextgetuiabilitychildprocessinfos)方法获取。

**起始版本**：26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```ts
import { childProcessManager } from '@kit.AbilityKit';
```

## 属性

**起始版本**：26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pid | number | 否 | 否 | 子进程的PID。 |
| parentPid | number | 否 | 否 | 子进程的父进程PID。 |
| processName | string | 否 | 否 | 子进程的进程名。 |
