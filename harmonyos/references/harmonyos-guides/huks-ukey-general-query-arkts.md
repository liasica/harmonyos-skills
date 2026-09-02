---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-ukey-general-query-arkts
title: 通用查询(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > 通用操作 > 通用查询(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:f9839b5bb88d3402d88a284db070b17c9a248f399325705fbba606590bc2350e
---

从API 22开始，huksExternalCrypto提供通用查询功能接口。该接口可以用于从UKey中获取设备标识、App标识以及其他通用属性信息，完成属性查询操作。具体的场景介绍请参考[获取属性介绍及规格](huks-ukey-general-query-overview.md)。

## 开发步骤

**获取属性**

1. 通过证书管理系统能力提供的[openAuthorizeDialog](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)获取[keyUri](../harmonyos-references/js-apis-certmanagerdialog.md#certreference22)作为resourceId，并[打开资源](huks-open-close-resource-ndk.md#打开资源)。
2. 构造输入参数propertyId和可选输入参数[param](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptoparam)。
3. 调用[getProperty](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptogetproperty)获取属性信息。

## 开发案例

```ts
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function getProperty(): Promise<Array<huksExternalCrypto.HuksExternalCryptoParam>> {
  // 1. 获取resourceId, 假设获取的resourceId如下，并已经打开该资源
  const testResourceId = JSON.stringify({
    providerName: "testProviderName",
    bundleName: "com.example.cryptoapplication",
    abilityName: "CryptoExtension",
    index: {
      key: "testKey"
    } as ESObject
  });

  // 2. 构造输入参数propertyId和可选参数param
  let propertyId = "SKF_EnumDev";
  const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [];

  // 3. 调用getProperty获取属性信息
  console.info('promise: await huksExternalCrypto getProperty.');
  try {
    await huksExternalCrypto.getProperty(testResourceId, propertyId, extProperties)
      .then((data) => {
        console.info(`promise: getProperty success, data: ` + JSON.stringify(data));
      }).catch((error: BusinessError) => {
        console.error(`promise: getProperty failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: getProperty failed, errCode : ${error.code}, errMsg : ${error.message}`);
  }
  return extProperties;
}
```
