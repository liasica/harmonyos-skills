---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-extension-set-property-arkts
title: 属性设置(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > 通用操作 > 属性设置(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:079f56599fac9dd0ec12eb252dd44f777761ab59d3bd9555675adbbac9de39ed
---

从API版本26.0.0开始，huksExternalCrypto提供设置属性的功能接口。应用可通过setProperty接口设置指定资源的属性值，由[CryptoExtensionAbility](../harmonyos-references/js-apis-cryptoextensionability.md)实现方提供，推荐使用GMT 0016-2023中定义的SKF接口名作为属性ID。具体的场景介绍及规格，请参考[通用查询介绍及规格](huks-ukey-general-query-overview.md)。

## 开发步骤

1. 获取资源ID。可通过[openAuthorizeDialog](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)获取keyUri作为resourceId，或通过[getResourceId](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptogetresourceid)获取外部密钥管理扩展的资源ID。
2. 调用[setProperty](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptosetproperty)设置属性值。

## 开发案例

```ts
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function setProperty(resourceId: string, propertyId: string): Promise<void> {
  try {
    await huksExternalCrypto.setProperty(resourceId, propertyId)
      .then(() => {
        console.info('promise: setProperty success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: setProperty failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: setProperty input arg invalid.');
  }
}
```
