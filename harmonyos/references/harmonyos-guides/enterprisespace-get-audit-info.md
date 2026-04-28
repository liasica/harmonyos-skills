---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-get-audit-info
title: 获取审批信息
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间互传 > 获取审批信息
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9dd6f9e30616f3d63b41fa8cd9a7ed1d652a035d6d6d95285a75cb277ee6f897
---

## 场景介绍

Enterprise Space Kit为应用提供获取审批信息的能力。文件外发需经过审批流程控制，通过调用审批状态同步接口实时获取审批结果，审批完成后允许文件外发至个人空间，若审批被拒绝或撤销则禁止外发。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisespace-spacedatatransfer.md#getauditinfo)。

| 接口名 | 描述 |
| --- | --- |
| [getAuditInfo](../harmonyos-references/enterprisespace-spacedatatransfer.md#getauditinfo)(transactionNum: string): [AuditInfo](../harmonyos-references/enterprisespace-spacedatatransfer.md#auditinfo) | 获取审批信息。 |

## 开发步骤

1. 导入Enterprise Space Kit模块。

   ```
   1. import { fileTransfer } from '@kit.EnterpriseSpaceKit';
   ```
2. 调用[getAuditInfo](../harmonyos-references/enterprisespace-spacedatatransfer.md#getauditinfo)接口，获取审批信息，并且查看打印信息。

   ```
   1. const transactionNum: string = '1111111';
   2. try {
   3. const auditInfo: fileTransfer.AuditInfo = fileTransfer.getAuditInfo(transactionNum);
   4. console.info(`Succeeded in getting audit info:` + JSON.stringify(auditInfo));
   5. } catch (err) {
   6. console.error(`Failed to get audit info. Code: ${err.code}, message: ${err.message}`);
   7. }
   ```
