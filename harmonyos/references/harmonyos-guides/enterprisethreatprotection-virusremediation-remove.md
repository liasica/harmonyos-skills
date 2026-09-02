---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisethreatprotection-virusremediation-remove
title: 文件隔离删除
breadcrumb: 指南 > 系统 > 安全 > Enterprise Threat Protection Kit（企业威胁防护服务） > 病毒检测与处置 > 文件隔离删除
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:03+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:d8040382fec87e921bb0a1a0986b787e19380ccdfb60692e8cfcd70b406724a2
---

## 基本概念

**隔离区**：是指系统中临时存放被识别为威胁的文件的区域。

文件隔离删除是指将隔离区的文件永久删除。

## 场景介绍

当隔离区的文件日益增加，磁盘空间占用持续增长时，可通过调用隔离文件删除接口，对已隔离文件进行删除，保证系统资源的高效利用并持续维护防护性能。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisethreatprotection-virusremediation-interface.md#removeisolatedfile)。

| 接口 | 描述 |
| --- | --- |
| removeIsolatedFile(id: string): Promise<void> | 对指定隔离ID的文件进行删除。删除后无法恢复。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { virusRemediation } from '@kit.EnterpriseThreatProtectionKit';
   ```
2. 通过调用接口[removeIsolatedFile](../harmonyos-references/enterprisethreatprotection-virusremediation-interface.md#removeisolatedfile)，实现对指定隔离ID文件的删除。id参数为隔离文件的唯一标识符，可通过调用[queryIsolatedFiles](../harmonyos-references/enterprisethreatprotection-virusremediation-interface.md#queryisolatedfiles)接口获取。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';

   // 对指定隔离文件ID进行删除
   function removeIsolatedFilePromise() {
     // 隔离文件ID，可通过queryIsolatedFiles()接口获取
     let isolatedFileId: string = 'example-id-12345';
     virusRemediation.removeIsolatedFile(isolatedFileId).then(() => {
       console.info('Succeeded in removing isolated file.');
     }).catch((err: BusinessError) => {
     // 根据错误码进行不同的业务处理
       if (err.code === 1023806001) {
         console.error('Database error, please retry or contact support.');
       } else if (err.code === 1023804003) {
         console.error('Invalid isolation ID, please verify the ID exists.');
       } else {
         console.error(`Failed to remove isolated file. Code: ${err.code}, message: ${err.message}.`);
       }
     });
   }
   ```
