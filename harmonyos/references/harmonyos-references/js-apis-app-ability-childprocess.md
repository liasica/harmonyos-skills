---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocess
title: "@ohos.app.ability.ChildProcess (子进程基类)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.ChildProcess (子进程基类)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:32+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1b0f65963eb6277dd35661eeb19810a72272629513f274888a3c75b01458e604
---

开发者自定义子进程的基类。通过[childProcessManager](js-apis-app-ability-childprocessmanager.md)启动子进程时，需要继承此类并重写入口方法。

**说明** 

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

```ts
import { ChildProcess } from '@kit.AbilityKit';
```

## ChildProcess.onStart

onStart(args?: ChildProcessArgs): void

子进程的入口方法，通过[childProcessManager](js-apis-app-ability-childprocessmanager.md)启动子进程后调用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| args12+ | [ChildProcessArgs](js-apis-app-ability-childprocessargs.md) | 否 | 传递到子进程的参数。参数为可选，不传或传null时使用默认配置启动。 |

**示例：**

```ts
import { ChildProcess, ChildProcessArgs } from '@kit.AbilityKit';

export default class DemoProcess extends ChildProcess {

  onStart(args?: ChildProcessArgs) {
    let entryParams = args?.entryParams;
    let fd = args?.fds?.key1;
    // ...
  }
}
```
