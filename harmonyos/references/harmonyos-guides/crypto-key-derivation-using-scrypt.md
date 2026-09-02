---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-scrypt
title: 使用SCRYPT进行密钥派生(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥派生介绍及算法规格 > 使用SCRYPT进行密钥派生(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bd22ac7b65c636516f96df8633de5562c224eca3c1f469e7526e14db4874bb14
---

对应的算法规格请查看[密钥派生算法规格：SCRYPT](crypto-key-derivation-overview.md#scrypt算法)。

## 开发步骤

1. 构造[ScryptSpec](../harmonyos-references/js-apis-cryptoframework.md#scryptspec18)对象，作为密钥派生参数进行密钥派生。

   ScryptSpec是[KdfSpec](../harmonyos-references/js-apis-cryptoframework.md#kdfspec11)的子类，需要指定：

   * algName：指定算法名为'SCRYPT'。
   * passphrase：用于生成派生密钥的原始密码。

     如果使用string类型，需要直接传入用于密钥派生的数据，而不是HexString、base64等字符串类型。同时需要确保该字符串为utf-8编码，否则派生结果会有差异。
   * salt：盐值。
   * n：迭代次数，需要为正整数。
   * p：并行化参数，需要为正整数。
   * r：块大小参数，需要为正整数。
   * maxMemory：最大内存限制参数，需要为正整数。
   * keySize：目标密钥的字节长度，需要为正整数。
2. 调用[cryptoFramework.createKdf](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatekdf11)，指定字符串参数'SCRYPT'，创建密钥派生算法为SCRYPT的密钥派生函数对象（Kdf）。
3. 输入SCRYPT对象，调用[Kdf.generateSecret](../harmonyos-references/js-apis-cryptoframework.md#generatesecret11)进行密钥派生。

   Kdf.generateSecret的多种调用形式如表所示。

   | 接口名 | 返回方式 |
   | --- | --- |
   | generateSecret(params: KdfSpec, callback: AsyncCallback<DataBlob>): void | callback异步生成。 |
   | generateSecret(params: KdfSpec): Promise<DataBlob> | Promise异步生成。 |
   | generateSecretSync(params: KdfSpec): DataBlob | 同步生成。 |

* 通过await返回结果：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { buffer } from '@kit.ArkTS';

  async function scryptAwait() {
    try {
      let spec: cryptoFramework.ScryptSpec = {
        algName: 'SCRYPT',
        salt: new Uint8Array(16),
        passphrase: 'password',
        n:1024,
        p:16,
        r:8,
        maxMemory:1024 * 16 * 8 * 10, //n * p * r * 10
        keySize: 64
      };
      let kdf = cryptoFramework.createKdf('SCRYPT');
      let secret = await kdf.generateSecret(spec);
      console.info('key derivation output: ' + secret.data);
    } catch(error) {
      let e: BusinessError = error as BusinessError;
      console.error('key derivation failed, errCode: ' + e.code + ', errMsg: ' + e.message);
    }
  }
  ```
* 通过Promise返回结果：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { buffer } from '@kit.ArkTS';

  function scryptPromise() {
    let spec: cryptoFramework.ScryptSpec = {
      algName: 'SCRYPT',
      passphrase: '123456',
      salt: new Uint8Array(16),
      n:1024,
      p:16,
      r:8,
      maxMemory:1024 * 16 * 8 * 10, //n * p * r * 10
      keySize: 64
    };
    let kdf = cryptoFramework.createKdf('SCRYPT');
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
  import { BusinessError } from '@kit.BasicServicesKit';
  import { buffer } from '@kit.ArkTS';

  function kdfSync() {
    try {
      let spec: cryptoFramework.ScryptSpec = {
        algName: 'SCRYPT',
        passphrase: '123456',
        salt: new Uint8Array(16),
        n:1024,
        p:16,
        r:8,
        maxMemory:1024 * 16 * 8 * 10, //n * p * r * 10
        keySize: 64
      };
      let kdf = cryptoFramework.createKdf('SCRYPT');
      let secret = kdf.generateSecretSync(spec);
      console.info('[Sync]key derivation output: ' + secret.data);
    } catch(error) {
      let e: BusinessError = error as BusinessError;
      console.error('key derivation failed, errCode: ' + e.code + ', errMsg: ' + e.message);
    }
  }
  ```
