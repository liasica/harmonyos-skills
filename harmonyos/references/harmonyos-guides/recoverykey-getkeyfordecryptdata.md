---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recoverykey-getkeyfordecryptdata
title: 获取解密硬盘数据的企业恢复密钥
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 企业恢复密钥 > 获取解密硬盘数据的企业恢复密钥
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:31+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:b7a35d082399e0622599e3ae544769821a6cb64759e94e1b6e088c638b795643
---

## 场景介绍

为应用提供获取企业恢复密钥的能力，在企业公钥证书配置成功后，可直接获取企业恢复密钥，用于解密已加密的硬盘数据。

**说明** 

企业恢复密钥仅可被获取一次，获取到企业恢复密钥后，可在持有企业私钥的设备上解密，并进行相应的存储。如果需要再次获取，需要先调用[删除企业恢复密钥](recoverykey-delete.md)能力，再调用该能力。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-recoverykey.md)。

| 接口名 | 描述 |
| --- | --- |
| [getEnterpriseRecoveryKey](../harmonyos-references/dataguard-recoverykey.md#recoverykeygetenterpriserecoverykey)(userId: number): Promise<[EnterpriseRecoveryKeyInfo](../harmonyos-references/dataguard-recoverykey.md#enterpriserecoverykeyinfo)> | 使用Promise方式获取企业恢复密钥。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { buffer } from '@kit.ArkTS';
   import { osAccount, BusinessError } from '@kit.BasicServicesKit';
   import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 调用接口[getEnterpriseRecoveryKey](../harmonyos-references/dataguard-recoverykey.md#recoverykeygetenterpriserecoverykey)，传入需要获取企业恢复密钥的用户ID，获取企业恢复密钥。

   ```typescript
   const TAG: string = 'EnterpriseRecoveryKey_GetRecoveryKey';
   const DOMAIN: number = 0x0000;

   /**
    * 获取解密硬盘数据的企业恢复密钥。使用Promise异步回调。
    */
   function getEnterpriseRecoveryKey() {
     let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
     accountManager.getOsAccountLocalId().then((userId: number) => {
       hilog.info(DOMAIN, TAG, `getEnterpriseRecoveryKey userId: ${userId}.`);
       recoveryKey.getEnterpriseRecoveryKey(userId).then((info: recoveryKey.EnterpriseRecoveryKeyInfo) => {
         hilog.info(DOMAIN, TAG, `Succeeded in getting enterprise recovery key.`);
         hilog.info(DOMAIN, TAG,
           `EnterpriseRecoveryKeyInfo enterpriseRecoveryKey: ${buffer.from(info.enterpriseRecoveryKey)
             .toString('hex')}`);
         hilog.info(DOMAIN, TAG,
           `EnterpriseRecoveryKeyInfo exportPublicKey: ${buffer.from(info.exportPublicKey).toString('hex')}`);
         hilog.info(DOMAIN, TAG, `EnterpriseRecoveryKeyInfo iv: ${buffer.from(info.iv).toString('hex')}`);
         hilog.info(DOMAIN, TAG, `EnterpriseRecoveryKeyInfo tag: ${buffer.from(info.tag).toString('hex')}`);
       }).catch((error: BusinessError) => {
         hilog.error(DOMAIN, TAG,
           `Failed to get enterprise recovery key. Code: ${error.code}, message: ${error.message}`);
       });
     });
   }
   ```
