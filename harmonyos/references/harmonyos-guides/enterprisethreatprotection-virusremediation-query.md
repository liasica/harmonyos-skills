---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisethreatprotection-virusremediation-query
title: 隔离查询
breadcrumb: 指南 > 系统 > 安全 > Enterprise Threat Protection Kit（企业威胁防护服务） > 病毒检测与处置 > 隔离查询
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:03+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:84b73dcf7400d791dcdc28785cd7259bc14aa4b2a0b39a968246c0205782c516
---

## 基本概念

隔离查询功能帮助安全防护类应用获取当前用户下由该应用隔离的处于隔离状态的文件信息列表。

## 场景介绍

当安全防护类应用更新或卸载，导致原本存储在应用数据库中的隔离信息丢失时，可通过隔离查询接口，为安全防护类应用提供隔离信息查询的能力，快速获取自身应用已隔离的当前用户的文件信息，保障隔离恢复和隔离删除的可操作性。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisethreatprotection-virusremediation-interface.md#queryisolatedfiles)。

| 接口 | 描述 |
| --- | --- |
| queryIsolatedFiles(callback: [QueryCallback](../harmonyos-references/enterprisethreatprotection-virusremediation-interface.md#querycallback), batchNum?: number): void | 获取已隔离文件的文件信息。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { virusRemediation } from '@kit.EnterpriseThreatProtectionKit';
   ```
2. 通过声明查询结果回调queryCallback，并调用[queryIsolatedFiles](../harmonyos-references/enterprisethreatprotection-virusremediation-interface.md#queryisolatedfiles)接口，获取已隔离文件的文件信息。

   ```typescript
   function startQueryTask() {
     // 查询隔离文件信息回调
     let onQuery: (files: virusRemediation.IsolatedFileInfo[]) => void = (files: virusRemediation.IsolatedFileInfo[]) => {
       files.forEach((value: virusRemediation.IsolatedFileInfo, index: number) => {
         console.info(`Succeeded in getting isolated file, file id: ${value.id}.`);
       })
     };
     // 查询隔离文件信息结束通知
     let onComplete: () => void = () => {
       console.info(`Query completed`);
     };
     // 查询隔离文件信息错误报告
     let onError: (code: number, message: string) => void = (code: number, message: string) => {
       console.error(`Query error, error code: ${code}, message: ${message}`);
     }
     let queryCallback: virusRemediation.QueryCallback = {
       onQuery: onQuery,
       onComplete: onComplete,
       onError: onError
     };
     try {
       virusRemediation.queryIsolatedFiles(queryCallback);
     } catch (error) {
       console.error(`Failed to get isolated file. Error: ${error}`);
     }
   }
   ```
