---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-encoded-decoded
title: 使用RSA私钥进行编码解码(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥生成与转换 > 使用RSA私钥进行编码解码(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d65e4cdf8d63a7060a9c97d903a5180b4ee3b5b9f7a0a096475839494abfe911
---

**编码**

1. 调用[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)、[AsyKeyGenerator.generateKeyPair](../harmonyos-references/js-apis-cryptoframework.md#generatekeypair-1)，生成RSA密钥类型为RSA1024、素数个数为2的非对称密钥对（KeyPair）。KeyPair对象中包括公钥PubKey、私钥PriKey。

   如何生成RSA非对称密钥对，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：RSA](crypto-key-generation-conversion.md#rsa)和[随机生成非对称密钥对](crypto-generate-asym-key-pair-randomly.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 传入参数[KeyEncodingConfig](../harmonyos-references/js-apis-cryptoframework.md#keyencodingconfig18)，参数PKCS1/PKCS8，调用[prikey.getEncodedPem](../harmonyos-references/js-apis-cryptoframework.md#getencodedpem18)生成编码后的私钥字符串。

**解码**

1. 调用[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)生成RSA非对称密钥生成器asyKeyGenerator。

   如何生成RSA非对称密钥对，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：RSA](crypto-key-generation-conversion.md#rsa)。

   **注意** 

   解码应该与编码传入的算法一致。
2. 调用异步[asyKeyGenerator.convertPemKey](../harmonyos-references/js-apis-cryptoframework.md#convertpemkey18)或者同步方法[asyKeyGenerator.convertPemKeySync](../harmonyos-references/js-apis-cryptoframework.md#convertpemkeysync18)，传入编码后的私钥字符串与编码口令。最后返回密钥对对象（KeyPair），其中包含解码后的私钥。

* 编码示例：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  function prikeyEncoding() {
    let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
    let keyPair = rsaGenerator.generateKeyPairSync();
    let options : cryptoFramework.KeyEncodingConfig = {
        password: '123456',
        cipherName: 'AES-128-CBC'
    }
    let priPemKey = keyPair.priKey;
    let priString = priPemKey.getEncodedPem('PKCS1', options);
    console.info('[sync]TestPriKeyPkcs1Encoded priString output: ' + priString);
  }
  ```
* 解码示例：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  let priKeyPkcs1EncodingStr : string =
  '-----BEGIN RSA PRIVATE KEY-----\n'+
    'Proc-Type: 4,ENCRYPTED\n'+
    'DEK-Info: AES-128-CBC,815A066131BF05CF87CE610A59CC69AE\n\n'+
    '7Jd0vmOmYGFZ2yRY8fqRl3+6rQlFtNcMILvcb5KWHDSrxA0ULmJE7CW0DSRikHoA\n'+
    't0KgafhYXeQXh0dRy9lvVRAFSLHCLJVjchx90V7ZSivBFEq7+iTozVp4AlbgYsJP\n'+
    'vx/1sfZD2WAcyMJ7IDmJyft7xnpVSXsyWGTT4f3eaHJIh1dqjwrso7ucAW0FK6rp\n'+
    '/TONyOoXNfXtRbVtxNyCWBxt4HCSclDZFvS9y8fz9ZwmCUV7jei/YdzyQI2wnE13\n'+
    'W8cKlpzRFL6BWi8XPrUtAw5MWeHBAPUgPWMfcmiaeyi5BJFhQCrHLi+Gj4EEJvp7\n'+
    'mP5cbnQAx6+paV5z9m71SKrI/WSc4ixsYYdVmlL/qwAK9YliFfoPl030YJWW6rFf\n'+
    'T7J9BUlHGUJ0RB2lURNNLakM+UZRkeE9TByzCzgTxuQtyv5Lwsh2mAk3ia5x0kUO\n'+
    'LHg3Eoabhdh+YZA5hHaxnpF7VjspB78E0F9Btq+A41rSJ6zDOdToHey4MJ2nxdey\n'+
    'Z3bi81TZ6Fp4IuROrvZ2B/Xl3uNKR7n+AHRKnaAO87ywzyltvjwSh2y3xhJueiRs\n'+
    'BiYkyL3/fnocD3pexTdN6h3JgQGgO5GV8zw/NrxA85mw8o9im0HreuFObmNj36T9\n'+
    'k5N+R/QIXW83cIQOLaWK1ThYcluytf0tDRiMoKqULiaA6HvDMigExLxuhCtnoF8I\n'+
    'iOLN1cPdEVQjzwDHLqXP2DbWW1z9iRepLZlEm1hLRLEmOrTGKezYupVv306SSa6J\n'+
    'OA55lAeXMbyjFaYCr54HWrpt4NwNBX1efMUURc+1LcHpzFrBTTLbfjIyq6as49pH\n'+
    '-----END RSA PRIVATE KEY-----';

  async function prikeyDecoding() {
    let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
    asyKeyGenerator.convertPemKey(null, priKeyPkcs1EncodingStr, '123456')
      .then(keyPair => {
        let priKey = keyPair.priKey;
        if (priKey) {
          console.info('convertPemKey result: success.');
        }
      }).catch((error: BusinessError) => {
      console.error(`convertPemKey failed: errCode: ${error.code}, message: ${error.message}`);
    });
  }
  ```
