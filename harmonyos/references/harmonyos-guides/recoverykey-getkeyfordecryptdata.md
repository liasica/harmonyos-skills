---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recoverykey-getkeyfordecryptdata
title: 获取解密硬盘数据的企业恢复密钥
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 企业恢复密钥 > 获取解密硬盘数据的企业恢复密钥
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:535c1f899603098527249eda8224d687633ede433ef2ac022ddee1ddc9d14712
---

## 场景介绍

为应用提供获取企业恢复密钥的能力，在企业公钥证书配置成功后，可直接获取企业恢复密钥，用于解密已加密的硬盘数据。

说明

企业恢复密钥仅可被获取一次，获取到企业恢复密钥后，可在持有企业私钥的设备上解密，并进行相应的存储。如果需要再次获取，需要先调用[删除企业恢复密钥](recoverykey-delete.md)能力，再调用该能力。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-recoverykey.md)。

| 接口名 | 描述 |
| --- | --- |
| [getEnterpriseRecoveryKey](../harmonyos-references/dataguard-recoverykey.md#getenterpriserecoverykey)(userId: number): Promise<[EnterpriseRecoveryKeyInfo](../harmonyos-references/dataguard-recoverykey.md#enterpriserecoverykeyinfo)> | 使用Promise方式获取恢复密钥。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
   2. import { BusinessError, osAccount } from '@kit.BasicServicesKit';
   ```
2. 调用接口[getEnterpriseRecoveryKey](../harmonyos-references/dataguard-recoverykey.md#getenterpriserecoverykey)，传入需要获取企业恢复密钥的用户ID，获取企业恢复密钥。

   ```
   1. async function testGetEnterpriseRecoveryKey() {
   2. try {
   3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
   4. let userId: number = await accountManager.getOsAccountLocalId();
   5. recoveryKey.getEnterpriseRecoveryKey(userId).then((info: recoveryKey.EnterpriseRecoveryKeyInfo) => {
   6. console.info(`Succeeded in getting enterprise recovery key.`);
   7. }).catch((error: BusinessError) => {
   8. console.error(`Failed to get enterprise recovery key. Code: ${error.code}, message: ${error.message}`);
   9. });
   10. } catch (e) {
   11. console.error(`Failed to testGetEnterpriseRecoveryKey. Code: ${e.code}, message: ${e.message}`);
   12. }
   13. }
   ```
