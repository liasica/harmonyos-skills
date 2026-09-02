---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recoverykey-delete
title: 删除企业恢复密钥
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 企业恢复密钥 > 删除企业恢复密钥
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:03+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:fb9f057ad2cefa0302261152e45d8b659080c99d8bf6b2f230cd44d96d286b4a
---

## 场景介绍

为应用提供删除企业恢复密钥的能力，用于在企业恢复密钥发生泄漏、禁用企业恢复密钥时删除相关数据，使之前导出的企业恢复密钥失效。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-recoverykey.md)。

| 接口名 | 描述 |
| --- | --- |
| [deleteEnterpriseRecoveryKey](../harmonyos-references/dataguard-recoverykey.md#recoverykeydeleteenterpriserecoverykey)(userId: number, signature: Uint8Array): Promise<number> | 使用Promise方式删除企业恢复密钥相关数据。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { BusinessError, osAccount } from '@kit.BasicServicesKit';
   import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 先调用接口[getAuthChallenge](../harmonyos-references/dataguard-recoverykey.md#recoverykeygetauthchallenge)，获取挑战值并[签名](recoverykey-signature.md)，传入需要删除企业恢复密钥的用户ID和挑战值的签名，再调用接口[deleteEnterpriseRecoveryKey](../harmonyos-references/dataguard-recoverykey.md#recoverykeydeleteenterpriserecoverykey)，删除企业恢复密钥相关数据。

   ```typescript
   const TAG: string = 'EnterpriseRecoveryKey_Delete';
   const DOMAIN: number = 0x0000;

   async function testDeleteEnterpriseRecoveryKey() {
     try {
       let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
       let userId: number = await accountManager.getOsAccountLocalId();
       // 在实际应用中，signature 应替换为由企业的公钥、私钥和挑战值生成的签名。
       let signature: Uint8Array = new Uint8Array([0]);
       recoveryKey.deleteEnterpriseRecoveryKey(userId, signature).then((ret: number) => {
         hilog.info(DOMAIN, TAG, `Succeeded in deleting enterprise recovery key. result is: ${ret}`);
       }).catch((err: BusinessError) => {
         hilog.error(DOMAIN, TAG, `Failed to delete enterprise recovery key. Code: ${err.code}, message: ${err.message}`);
       });
     } catch (e) {
       hilog.error(DOMAIN, TAG, `Failed to testDeleteEnterpriseRecoveryKey. Code: ${e.code}, message: ${e.message}`);
     }
   }
   ```
