---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisethreatprotection-virusremediation-restore
title: 文件隔离恢复
breadcrumb: 指南 > 系统 > 安全 > Enterprise Threat Protection Kit（企业威胁防护服务） > 病毒检测与处置 > 文件隔离恢复
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:02+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:e5bb9a4c7110b442b1c74a92f1d2c39ce59b708476de344a86495ef3d8dbe0f5
---

## 基本概念

文件隔离恢复是指将指定隔离ID的文件从隔离区还原至其原始存储路径。

## 场景介绍

当安全防护类应用之前扫描过程中将正常文件误判为威胁文件并已隔离时，可通过文件隔离恢复接口将已隔离的文件还原至原路径，从而确保正常业务文件可用，保障用户数据完整性与业务连续性。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisethreatprotection-virusremediation-interface.md#restoreisolatedfile)。

| 接口 | 描述 |
| --- | --- |
| restoreIsolatedFile(id: string): Promise<string> | 对指定隔离ID的文件进行恢复并获得恢复路径。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { virusRemediation } from '@kit.EnterpriseThreatProtectionKit';
   ```
2. 调用接口[restoreIsolatedFile](../harmonyos-references/enterprisethreatprotection-virusremediation-interface.md#restoreisolatedfile)，实现对指定隔离ID的文件恢复并获取恢复路径。id参数为隔离文件的唯一标识符，可通过调用[queryIsolatedFiles](../harmonyos-references/enterprisethreatprotection-virusremediation-interface.md#queryisolatedfiles)接口获取。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';

   // 按指定隔离文件ID进行恢复，打印恢复后的文件路径
   function restoreFilePromise() {
     // 隔离文件ID，可通过queryIsolatedFiles()接口获取
     let isolatedFileId: string = 'example-id-12345';
     // 调用接口恢复指定ID的隔离文件
     virusRemediation.restoreIsolatedFile(isolatedFileId).then((path: string) => {
       console.info(`Succeeded in restoring file. Restore path: ${path}, ID: ${isolatedFileId}.`);
     }).catch((err: BusinessError) => {
       // 根据错误码进行不同的业务处理
       if (err.code === 1023802001) {
         console.error('Target file does not exist, please verify the file path.');
       } else if (err.code === 1023802002) {
         console.error('Path access denied, please check path permissions.');
       } else if (err.code === 1023802003) {
         console.error('File name conflict, please rename or delete the existing file.');
       } else {
         console.error(`Failed to restore file. Code: ${err.code}, message: ${err.message}.`);
       }
     });
   }
   ```
