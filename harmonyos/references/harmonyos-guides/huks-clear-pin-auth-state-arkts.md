---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-clear-pin-auth-state-arkts
title: 清除UKey PIN码认证状态(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > UKeyPIN码认证管理 > 清除UKey PIN码认证状态(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:86a4f7cb31257178752c5b2882f367d40221fef47b7b11e1e644b9870a6f4047
---

从API版本26.0.0开始，huksExternalCrypto提供清除UKey PIN码认证状态功能接口。应用在密钥操作完成后或需要重置认证状态时，可以调用该接口清除指定资源的PIN码认证状态。具体的场景介绍及规格，请参考[UKey PIN码认证介绍及规格](huks-ukey-pin-authentication-management-overview.md)。

## 开发步骤

1. 获取资源ID。可通过[openAuthorizeDialog](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)获取keyUri作为resourceId，或通过[getResourceId](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptogetresourceid)获取外部密钥管理扩展的资源ID。
2. 调用[clearUkeyPinAuthState](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptoclearukeypinauthstate)清除PIN码认证状态。

## 开发案例

```ts
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 清除PIN码认证状态
async function clearUkeyPinAuthState(resourceId: string): Promise<void> {
  try {
    await huksExternalCrypto.clearUkeyPinAuthState(resourceId)
      .then(() => {
        console.info('promise: clearUkeyPinAuthState success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: clearUkeyPinAuthState failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: clearUkeyPinAuthState input arg invalid.');
  }
}
```
