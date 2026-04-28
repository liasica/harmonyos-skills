---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recoverykey-update
title: 更新企业公钥证书
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 企业恢复密钥 > 更新企业公钥证书
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0785ab4f61507df515485c9cb22eb6c5958025cc200962a2a4ac50237a8e37d3
---

## 场景介绍

为应用提供更新企业公钥证书的能力，用于在证书泄漏、证书失效等场景及时更新企业公钥证书。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-recoverykey.md)。

| 接口名 | 描述 |
| --- | --- |
| [updateEnterpriseCertificate](../harmonyos-references/dataguard-recoverykey.md#updateenterprisecertificate)(signature: Uint8Array, cert: Uint8Array): Promise<number> | 使用Promise方式更新证书。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 先调用接口[getAuthChallenge](../harmonyos-references/dataguard-recoverykey.md#getauthchallenge)，获取挑战值并[签名](recoverykey-signature.md)，传入挑战值的签名和企业公钥证书，再调用接口[updateEnterpriseCertificate](../harmonyos-references/dataguard-recoverykey.md#updateenterprisecertificate)，更新企业公钥证书。

   ```
   1. function testUpdateEnterpriseCertificate() {
   2. // 在实际应用中，signature 应替换为由企业的公钥、私钥和挑战值生成的签名。
   3. let signature: Uint8Array = new Uint8Array([0]);
   4. // 在实际应用中，cert 应需替换为企业证书数据。
   5. let cert: Uint8Array = new Uint8Array([0]);
   6. recoveryKey.updateEnterpriseCertificate(signature, cert).then((ret: number) => {
   7. console.info(`Succeeded in updating certificate.`);
   8. }).catch((error: BusinessError) => {
   9. console.error(`Failed to update certificate. Code: ${error.code}, message: ${error.message}`);
   10. });
   11. }
   ```
