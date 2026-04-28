---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocess
title: @ohos.app.ability.ChildProcess (子进程基类)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.ChildProcess (子进程基类)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:dc8ce2816b9e79bafcceeed5ec6ef45eee642591114d1610f99689a9c2e610eb
---

开发者自定义子进程的基类。通过[childProcessManager](js-apis-app-ability-childprocessmanager.md)启动子进程时，需要继承此类并重写入口方法。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { ChildProcess } from '@kit.AbilityKit';
```

## ChildProcess.onStart

PhonePC/2in1TabletTVWearable

onStart(args?: ChildProcessArgs): void

子进程的入口方法，通过[childProcessManager](js-apis-app-ability-childprocessmanager.md)启动子进程后调用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| args12+ | [ChildProcessArgs](js-apis-app-ability-childprocessargs.md) | 否 | 传递到子进程的参数。 |

**示例：**

```
1. import { ChildProcess, ChildProcessArgs } from '@kit.AbilityKit';

3. export default class DemoProcess extends ChildProcess {

5. onStart(args?: ChildProcessArgs) {
6. let entryParams = args?.entryParams;
7. let fd = args?.fds?.key1;
8. // ..
9. }
10. }
```
