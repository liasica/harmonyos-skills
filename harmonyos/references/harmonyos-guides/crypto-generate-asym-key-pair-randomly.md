---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-randomly
title: 随机生成非对称密钥对(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥生成与转换 > 随机生成非对称密钥对(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:00+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:173d3aea35d75c1febfb610b0c3c7bca75af80a8ab582187aab4b788d0910cfb
---

以RSA和SM2为例，随机生成非对称密钥对（KeyPair），并获得二进制数据。

非对称密钥对可用于后续加解密等操作，二进制数据可用于存储或传输。

## 随机生成RSA密钥对

对应的算法规格请查看[非对称密钥生成和转换规格：RSA](crypto-key-generation-conversion.md#rsa)。

1. 调用[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)，指定字符串参数'RSA1024|PRIMES\_2'，创建RSA密钥类型为RSA1024、素数个数为2的非对称密钥生成器（AsyKeyGenerator）。
2. 调用[AsyKeyGenerator.generateKeyPair](../harmonyos-references/js-apis-cryptoframework.md#generatekeypair-1)，随机生成非对称密钥对象（KeyPair）。

   KeyPair对象中包括公钥PubKey、私钥PriKey。
3. 调用[PubKey.getEncoded](../harmonyos-references/js-apis-cryptoframework.md#getencoded)和[PriKey.getEncoded](../harmonyos-references/js-apis-cryptoframework.md#getencoded)，分别获取密钥对象的二进制数据。

* 以使用Promise方式随机生成RSA密钥对为例：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  function generateAsyKey() {
    // 创建一个AsyKeyGenerator实例
    let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024|PRIMES_2');
    // 使用密钥生成器随机生成非对称密钥对
    let keyGenPromise = rsaGenerator.generateKeyPair();
    keyGenPromise.then(keyPair => {
      let pubKey = keyPair.pubKey;
      let priKey = keyPair.priKey;
      // 获取非对称密钥对的二进制数据
      let pkBlob = pubKey.getEncoded();
      let skBlob = priKey.getEncoded();
      console.info('pk bin data: ' + pkBlob.data);
      console.info('sk bin data: ' + skBlob.data);
    });
  }
  ```
* 同步返回结果（调用方法[generateKeyPairSync](../harmonyos-references/js-apis-cryptoframework.md#generatekeypairsync12)）：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  function generateAsyKeySync() {
    // 创建一个AsyKeyGenerator实例
    let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024|PRIMES_2');
    // 使用密钥生成器随机生成非对称密钥对
    try {
      let keyPair = rsaGenerator.generateKeyPairSync();
      if (keyPair != null) {
        let pubKey = keyPair.pubKey;
        let priKey = keyPair.priKey;
        // 获取非对称密钥对的二进制数据
        let pkBlob = pubKey.getEncoded();
        let skBlob = priKey.getEncoded();
        console.info('pk bin data: ' + pkBlob.data);
        console.info('sk bin data: ' + skBlob.data);
      } else {
        console.error('[Sync]: get key pair result: fail!');
      }
    } catch (e) {
      console.error(`get key pair failed: errCode: ${e.code}, message: ${e.message}`);
    }
  }
  ```

## 随机生成SM2密钥对

对应的算法规格请查看[非对称密钥生成和转换规格：SM2](crypto-key-generation-conversion.md#sm2)。

1. 调用[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)，指定字符串参数'SM2\_256'，创建密钥算法为SM2、密钥长度为256位的非对称密钥生成器（AsyKeyGenerator）。
2. 调用[AsyKeyGenerator.generateKeyPair](../harmonyos-references/js-apis-cryptoframework.md#generatekeypair-1)，随机生成非对称密钥对象（KeyPair）。

   KeyPair对象中包括公钥PubKey、私钥PriKey。
3. 调用[PubKey.getEncoded](../harmonyos-references/js-apis-cryptoframework.md#getencoded)和[PriKey.getEncoded](../harmonyos-references/js-apis-cryptoframework.md#getencoded)，分别获取密钥对象的二进制数据。

* 以使用Promise方式随机生成SM2密钥对为例：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  function generateSM2Key() {
    // 创建一个AsyKeyGenerator实例
    let sm2Generator = cryptoFramework.createAsyKeyGenerator('SM2_256');
    // 使用密钥生成器随机生成非对称密钥对
    let keyGenPromise = sm2Generator.generateKeyPair();
    keyGenPromise.then(keyPair => {
      let pubKey = keyPair.pubKey;
      let priKey = keyPair.priKey;
      // 获取非对称密钥对的二进制数据
      let pkBlob = pubKey.getEncoded();
      let skBlob = priKey.getEncoded();
      console.info('pk bin data: ' + pkBlob.data);
      console.info('sk bin data: ' + skBlob.data);
    });
  }
  ```
* 同步返回结果（调用方法[generateKeyPairSync](../harmonyos-references/js-apis-cryptoframework.md#generatekeypairsync12)）：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  function generateSM2KeySync() {
    // 创建一个AsyKeyGenerator实例
    let sm2Generator = cryptoFramework.createAsyKeyGenerator('SM2_256');
    // 使用密钥生成器随机生成非对称密钥对
    try {
      let keyPair = sm2Generator.generateKeyPairSync();
      if (keyPair != null) {
        let pubKey = keyPair.pubKey;
        let priKey = keyPair.priKey;
        // 获取非对称密钥对的二进制数据
        let pkBlob = pubKey.getEncoded();
        let skBlob = priKey.getEncoded();
        console.info('pk bin data: ' + pkBlob.data);
        console.info('sk bin data: ' + skBlob.data);
      } else {
        console.error('[Sync]: get key pair result: fail!');
      }
    } catch (e) {
      console.error(`get key pair failed: errCode: ${e.code}, message: ${e.message}`);
    }
  }
  ```
