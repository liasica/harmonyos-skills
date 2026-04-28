---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recoverykey-delete
title: 删除企业恢复密钥
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 企业恢复密钥 > 删除企业恢复密钥
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8aae7179beda1732b1c6f169e901afc8b8680f3f42e0fa48f7c69b3d49e0ea22
---

## 场景介绍

为应用提供删除企业恢复密钥的能力，用于在企业恢复密钥发生泄漏、禁用企业恢复密钥时删除相关数据，使之前导出的企业恢复密钥失效。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-recoverykey.md)。

| 接口名 | 描述 |
| --- | --- |
| [deleteEnterpriseRecoveryKey](../harmonyos-references/dataguard-recoverykey.md#deleteenterpriserecoverykey)(userId: number, signature: Uint8Array): Promise<number> | 使用Promise方式删除企业恢复密钥相关数据。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
   2. import { BusinessError, osAccount } from '@kit.BasicServicesKit';
   ```
2. 先调用接口[getAuthChallenge](../harmonyos-references/dataguard-recoverykey.md#getauthchallenge)，获取挑战值并[签名](recoverykey-signature.md)，传入需要删除企业恢复密钥的用户ID和挑战值的签名，再调用接口[deleteEnterpriseRecoveryKey](../harmonyos-references/dataguard-recoverykey.md#deleteenterpriserecoverykey)，删除企业恢复密钥相关数据。

   ```
   1. async function testDeleteEnterpriseRecoveryKey() {
   2. try {
   3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
   4. let userId: number = await accountManager.getOsAccountLocalId();
   5. // 在实际应用中，signature 应替换为由企业的公钥、私钥和挑战值生成的签名。
   6. let signature: Uint8Array = new Uint8Array([0]);
   7. recoveryKey.deleteEnterpriseRecoveryKey(userId, signature).then((ret: number) => {
   8. console.info(`Succeeded in deleting enterprise recovery key.`);
   9. }).catch((err: BusinessError) => {
   10. console.error(`Failed to delete enterprise recovery key. Code: ${err.code}, message: ${err.message}`);
   11. });
   12. } catch (e) {
   13. console.error(`Failed to testDeleteEnterpriseRecoveryKey. Code: ${e.code}, message: ${e.message}`);
   14. }
   15. }
   ```
