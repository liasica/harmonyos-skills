---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recoverykey-update
title: 更新企业公钥证书
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 企业恢复密钥 > 更新企业公钥证书
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:fce4335ca20506e1b983ff07a5da2340f508d7905a0212ded719a64eecbde4bb
---

## 场景介绍

为应用提供更新企业公钥证书的能力，用于在证书泄漏、证书失效等场景及时更新企业公钥证书。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-recoverykey.md)。

| 接口名 | 描述 |
| --- | --- |
| [updateEnterpriseCertificate](../harmonyos-references/dataguard-recoverykey.md#recoverykeyupdateenterprisecertificate)(signature: Uint8Array, cert: Uint8Array): Promise<number> | 使用Promise方式更新企业公钥证书。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 先调用接口[getAuthChallenge](../harmonyos-references/dataguard-recoverykey.md#recoverykeygetauthchallenge)，获取挑战值并[签名](recoverykey-signature.md)，传入挑战值的签名和企业公钥证书，再调用接口[updateEnterpriseCertificate](../harmonyos-references/dataguard-recoverykey.md#recoverykeyupdateenterprisecertificate)，更新企业公钥证书。

   ```typescript
   const TAG: string = 'EnterpriseRecoveryKey_Update';
   const DOMAIN: number = 0x0000;

   function testUpdateEnterpriseCertificate() {
     // 在实际应用中，signature 应替换为由企业的公钥、私钥和挑战值生成的签名。
     let signature: Uint8Array = new Uint8Array([0]);
     // 在实际应用中，cert 应替换为企业证书数据。
     let cert: Uint8Array = new Uint8Array([0]);
     recoveryKey.updateEnterpriseCertificate(signature, cert).then((ret: number) => {
       hilog.info(DOMAIN, TAG, `Succeeded in updating certificate. result is: ${ret}`);
     }).catch((error: BusinessError) => {
       hilog.error(DOMAIN, TAG, `Failed to update certificate. Code: ${error.code}, message: ${error.message}`);
     });
   }
   ```
