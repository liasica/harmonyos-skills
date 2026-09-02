---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisethreatprotection-virusremediation-isolate
title: 文件隔离
breadcrumb: 指南 > 系统 > 安全 > Enterprise Threat Protection Kit（企业威胁防护服务） > 病毒检测与处置 > 文件隔离
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:02+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:48370902a6e4474ac5a9b5abcffba486881352f50f1fa5da6c99d3ee9978e0c1
---

## 基本概念

文件隔离是指将检测到的威胁文件转移到安全隔离区。

## 场景介绍

在安全防护类应用检测到病毒、木马等恶意文件后可以使用文件隔离接口将恶意文件转移到安全隔离区，实现安全防护类应用对恶意文件的隔离能力。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisethreatprotection-virusremediation-interface.md#isolatethreatfile)。

| 接口 | 描述 |
| --- | --- |
| isolateThreatFile(path: string): Promise<string> | 对指定路径文件进行隔离并获得隔离ID。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { virusRemediation } from '@kit.EnterpriseThreatProtectionKit';
   ```
2. 通过调用接口[isolateThreatFile](../harmonyos-references/enterprisethreatprotection-virusremediation-interface.md#isolatethreatfile)，实现对恶意文件的安全隔离。path参数为目标文件的绝对路径。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';

   // 隔离文件，打印被隔离文件对应的隔离id
   function isolateFilePromise() {
     // 恶意文件路径，此处为示例路径，实际使用时需替换为真实文件路径
     let maliciousFilePath: string = '/data/service/el2/test/test.txt';
     virusRemediation.isolateThreatFile(maliciousFilePath).then((id: string) => {
       console.info(`Succeeded in isolating file. Path: ${maliciousFilePath}, ID: ${id}.`);
     }).catch((err: BusinessError) => {
     // 根据错误码进行不同的业务处理
       if (err.code === 1023804001) {
         console.error('Invalid file type, only single files are supported.');
       } else if (err.code === 1023804002) {
         console.error('Application bundle path detected, please uninstall the app or disable running.');
       } else {
         console.error(`Failed to isolate file. Code: ${err.code}, message: ${err.message}.`);
       }
     });
   }
   ```
