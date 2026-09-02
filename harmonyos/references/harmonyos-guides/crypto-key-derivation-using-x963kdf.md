---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-x963kdf
title: 使用X963KDF进行密钥派生(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥派生介绍及算法规格 > 使用X963KDF进行密钥派生(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0015f18b67a4bd7021eadbe646b07b2c05f2d000d8e425044487a6529c5a88ef
---

从API版本22开始，算法库支持使用该算法进行密钥派生操作。

对应的算法规格请查看[密钥派生算法规格：X963KDF](crypto-key-derivation-overview.md#x963kdf算法)。

## 开发步骤

1. 构造[X963KdfSpec](../harmonyos-references/js-apis-cryptoframework.md#x963kdfspec22)对象，作为密钥派生参数进行密钥派生。

   X963KdfSpec是[KdfSpec](../harmonyos-references/js-apis-cryptoframework.md#kdfspec11)的子类，需要指定：

   * algName：指定算法'X963Kdf'。
   * key：原始密钥材料。

     如果使用string类型，需要直接传入用于密钥派生的数据，而不是HexString、base64等字符串类型。同时需要确保该字符串为utf-8编码，否则派生结果会有差异。
   * info：可选的上下文与应用相关信息，可为空，用于扩展短密钥。
   * keySize：目标密钥的字节长度，需要为正整数。
2. 调用[cryptoFramework.createKdf](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatekdf11)，指定字符串参数'X963KDF|SHA256'，创建密钥派生算法为X963KDF、HMAC函数摘要算法为SHA256的密钥派生函数对象（Kdf）。
3. 输入X963KdfSpec对象，调用[Kdf.generateSecret](../harmonyos-references/js-apis-cryptoframework.md#generatesecret11)进行密钥派生。

   Kdf.generateSecret的多种调用形式如表所示。

   | 接口名 | 返回方式 |
   | --- | --- |
   | generateSecret(params: KdfSpec, callback: AsyncCallback<DataBlob>): void | callback异步生成。 |
   | generateSecret(params: KdfSpec): Promise<DataBlob> | Promise异步生成。 |
   | generateSecretSync(params: KdfSpec): DataBlob | 同步生成。 |

* 通过await返回结果：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { buffer } from '@kit.ArkTS';

  async function kdfAwait() {
    let keyData = new Uint8Array(buffer.from('012345678901234567890123456789', 'utf-8').buffer);
    let infoData = new Uint8Array(buffer.from('infostring', 'utf-8').buffer);
    let spec: cryptoFramework.X963KdfSpec = {
      algName: 'X963KDF',
      key: keyData,
      info: infoData,
      keySize: 32
    };
    let kdf = cryptoFramework.createKdf('X963KDF|SHA256');
    let secret = await kdf.generateSecret(spec);
    console.info('key derivation output: ' + secret.data);
  }
  ```
* 通过Promise返回结果：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { buffer } from '@kit.ArkTS';

  function kdfPromise() {
    let keyData = new Uint8Array(buffer.from('012345678901234567890123456789', 'utf-8').buffer);
    let infoData = new Uint8Array(buffer.from('infostring', 'utf-8').buffer);
    let spec: cryptoFramework.X963KdfSpec = {
      algName: 'X963KDF',
      key: keyData,
      info: infoData,
      keySize: 32
    };
    let kdf = cryptoFramework.createKdf('X963KDF|SHA256');
    let kdfPromise = kdf.generateSecret(spec);
    kdfPromise.then((secret) => {
      console.info('key derivation output: ' + secret.data);
    }).catch((error: BusinessError) => {
      console.error(`key derivation failed: errCode: ${error.code}, message: ${error.message}`);
    });
  }
  ```
* 通过同步方式返回结果：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { buffer } from '@kit.ArkTS';

  function kdfSync() {
    let keyData = new Uint8Array(buffer.from('012345678901234567890123456789', 'utf-8').buffer);
    let infoData = new Uint8Array(buffer.from('infostring', 'utf-8').buffer);
    let spec: cryptoFramework.X963KdfSpec = {
      algName: 'X963KDF',
      key: keyData,
      info: infoData,
      keySize: 32
    };
    let kdf = cryptoFramework.createKdf('X963KDF|SHA256');
    let secret = kdf.generateSecretSync(spec);
    console.info('[Sync]key derivation output: ' + secret.data);
  }
  ```
