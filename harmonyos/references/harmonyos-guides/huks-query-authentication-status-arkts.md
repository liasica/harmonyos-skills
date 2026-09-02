---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-query-authentication-status-arkts
title: 查询认证状态(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > UKeyPIN码认证管理 > 查询认证状态(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:7a4dc46ac3d3d67ec7c24b3e32df0bb46af73e1118438534c683b47549867dd5
---

从API 22开始，huksExternalCrypto提供PIN码认证状态查询功能接口。应用可以通过该接口查询PIN码是否认证通过。具体的场景介绍及规格，请参考[UKey PIN码认证介绍及规格](huks-ukey-pin-authentication-management-overview.md)。

## 开发步骤

1. 通过证书管理系统能力提供的[openAuthorizeDialog](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)获取[keyUri](../harmonyos-references/js-apis-certmanagerdialog.md#certreference22)，并将其作为resourceId。
2. 调用查询认证状态接口[getUkeyPinAuthState](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptogetukeypinauthstate)验证PIN码。

## 开发案例

```ts
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function getUkeyPinAuthState(): Promise<huksExternalCrypto.HuksExternalPinAuthState> {
  let ret: huksExternalCrypto.HuksExternalPinAuthState = huksExternalCrypto.HuksExternalPinAuthState.HUKS_EXT_CRYPTO_PIN_NO_AUTH;
  try {
    /* 1.构造查询PIN码状态参数 */
    const testResourceId = JSON.stringify({
      providerName: "testProviderName",
      bundleName: "com.example.cryptoapplication",
      abilityName: "CryptoExtension",
      index: {
        key: "testKey"
      } as ESObject
    });
    const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [];

    /* 2.调用getUkeyPinAuthState */
    await huksExternalCrypto.getUkeyPinAuthState(testResourceId, extProperties)
      .then((data) => {
        console.info(`promise: getUkeyPinAuthState success , data : ${data}`);
      }).catch((error: BusinessError) => {
        console.error(`promise: getUkeyPinAuthState failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: getUkeyPinAuthState input arg invalid.');
  }
  return ret;
}

async function testGetUkeyPinAuthState() {
  let ret: huksExternalCrypto.HuksExternalPinAuthState = await getUkeyPinAuthState();
  if (ret != huksExternalCrypto.HuksExternalPinAuthState.HUKS_EXT_CRYPTO_PIN_AUTH_SUCCEEDED) {
    console.error('getUkeyPinAuthState failed.');
    return;
  }

  console.info('getUkeyPinAuthState success.');
}
```
