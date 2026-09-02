---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisethreatprotection-virusremediation-terminate
title: 威胁进程终止
breadcrumb: 指南 > 系统 > 安全 > Enterprise Threat Protection Kit（企业威胁防护服务） > 病毒检测与处置 > 威胁进程终止
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:03+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:88259ed1abbf83c6c90674b8706264798c0ddbfb089ff4113b37a61cd67b3cde
---

从26.0.0版本开始，新增提供威胁进程终止接口，为企业安全类应用提供对运行中恶意进程及可疑进程的安全处置能力。

## 基本概念

威胁进程终止是一种主动防御手段，通过对已识别为恶意或存在安全风险的进程执行终止操作，使威胁失去运行载体，从而达到遏制攻击、保护终端安全的目的。该能力主要服务于企业级安全厂商，帮助其安全产品在客户端环境中实现自动化或可控的威胁清除。

## 场景介绍

支持三方杀软对规格范围内的威胁进程执行终止操作。典型应用场景包括：实时防护发现威胁后的即时阻断、违规软件或违规行为的强制终止、以及应急响应事件中的快速威胁遏制。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisethreatprotection-virusremediation-interface.md#terminateprocess)。

| 接口 | 描述 |
| --- | --- |
| terminateProcess(pid: number): Promise<void> | 三方杀软应用调用接口终止威胁进程。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { virusRemediation } from '@kit.EnterpriseThreatProtectionKit';
   ```
2. 调用接口[terminateProcess](../harmonyos-references/enterprisethreatprotection-virusremediation-interface.md#terminateprocess)，实现终止指定PID的威胁进程。

   ```typescript
   function terminateProcessPromise() {
     let pid: number = 0;
     virusRemediation.terminateProcess(pid).then(() => {
       console.info(`Succeeded in terminating process.`);
     }).catch((err: BusinessError) => {
       if (err.code === 1023807001) {
         console.error('Process not found.');
       } else if (err.code === 1023807002) {
         console.error('Access and disposal are denied for this process.');
       } else if (err.code === 1023807003) {
         console.error(`Access to other users' processes is not allowed.`);
       } else {
         console.error(`Failed to terminate process. Code: ${err.code}, message: ${err.message}.`);
       }
     });
   }
   ```
