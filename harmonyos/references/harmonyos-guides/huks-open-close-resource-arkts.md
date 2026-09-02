---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-open-close-resource-arkts
title: 打开资源/关闭资源(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > 资源管理 > 打开资源/关闭资源(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:32+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:d43afad85b91243b89820b18a1bc56c00738989ecff60679e687b42dbf7aaf4a
---

从API版本26.0.0开始，huksExternalCrypto提供打开/关闭资源功能的ArkTS接口。

## 打开资源

应用在密钥操作之前（密钥操作、通用操作、PIN码认证等），需要先调用[openResource](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptoopenresource)打开资源。打开资源需要获取resourceId，resourceId可通过[openAuthorizeDialog](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)获取，或通过[getResourceId](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptogetresourceid)获取外部密钥管理扩展的资源ID。

### 开发步骤

1. 通过[openAuthorizeDialog](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)获取keyUri作为resourceId，或通过[getResourceId](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptogetresourceid)获取外部密钥管理扩展的资源ID。
2. 调用[openResource](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptoopenresource)打开资源。

### 开发案例

```ts
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

const resourceId = JSON.stringify({
  providerName: "testProviderName",
  bundleName: "com.example.cryptoapplication",
  abilityName: "CryptoExtension",
  index: {
    key: "testKey"
  } as ESObject
});

const openResourceParams: Array<huksExternalCrypto.HuksExternalCryptoParam> = [];

async function openResource(): Promise<void> {
  try {
    await huksExternalCrypto.openResource(resourceId, openResourceParams)
      .then(() => {
        console.info('promise: openResource success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: openResource failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: openResource input arg invalid.');
  }
}
```

## 关闭资源

生态应用调用证书HAP界面，展示证书列表，用户选择证书，生态应用拿到对应的resourceId，关闭资源依赖于对应的resourceId。具体的场景介绍及规格，请参考[资源管理介绍及规格](huks-resource-management-overview.md)。

### 开发步骤

1. 通过[openAuthorizeDialog](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)获取resourceId，或通过[getResourceId](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptogetresourceid)获取外部密钥管理扩展的资源ID。
2. 调用[closeResource](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptocloseresource)关闭资源。

### 开发案例

```ts
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

const resourceId = JSON.stringify({
  providerName: "testProviderName",
  bundleName: "com.example.cryptoapplication",
  abilityName: "CryptoExtension",
  index: {
    key: "testKey"
  } as ESObject
});

const closeResourceParams: Array<huksExternalCrypto.HuksExternalCryptoParam> = [];

async function closeResource(): Promise<void> {
  try {
    await huksExternalCrypto.closeResource(resourceId, closeResourceParams)
      .then(() => {
        console.info('promise: closeResource success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: closeResource failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: closeResource input arg invalid.');
  }
}
```
