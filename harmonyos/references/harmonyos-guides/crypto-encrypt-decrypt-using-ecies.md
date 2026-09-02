---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-encrypt-decrypt-using-ecies
title: 使用ECIES混合加解密(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密介绍 > 使用ECIES混合加解密(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1d510643ad8c5dc52272bb3aa0978dc83db288982dd18ae5e6dba31f46a0369b
---

从API版本26.0.0开始，支持ECIES算法，ECIES是一种基于椭圆曲线密码学的加密算法。

**约束条件：**

* 密钥协商算法支持ECC256、ECC384、ECC521。
* 密钥派生算法仅支持X963KDF，摘要算法支持SHA1、SHA256、SHA384、SHA512。
* 对称加密算法支持AES128、AES192、AES256。
* 分组模式仅支持GCM。

## 开发步骤

### 加密

1. 调用[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)和[AsyKeyGenerator.generateKeyPair](../harmonyos-references/js-apis-cryptoframework.md#generatekeypair)，使用ECC算法生成密钥对。
2. 调用[cryptoFramework.createKeyAgreement](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatekeyagreement)和[KeyAgreement.generateSecret](../harmonyos-references/js-apis-cryptoframework.md#generatesecret11)，基于本端的私钥（KeyPair.priKey）与对端的公钥（KeyPair.pubKey）进行密钥协商，返回共享密钥。
3. X963KDF密钥派生，调用[cryptoFramework.createKdf](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatekdf11)和[Kdf.generateSecret](../harmonyos-references/js-apis-cryptoframework.md#generatesecret11)，基于协商的共享密钥（Secret）进行密钥派生，返回派生后的密钥。
4. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'AES128|GCM'，创建对称密钥类型为AES128、分组模式为GCM的Cipher实例，用于完成加密操作。
5. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为加密（cryptoFramework.CryptoMode.ENCRYPT\_MODE），指定加密密钥（SymKey）和GCM模式对应的加密参数（GcmParamsSpec），初始化加密Cipher实例。
6. 调用[Cipher.update](../harmonyos-references/js-apis-cryptoframework.md#update-1)，更新数据（明文）。
7. 调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，获取加密后的数据。
8. 读取[GcmParamsSpec](../harmonyos-references/js-apis-cryptoframework.md#gcmparamsspec).authTag作为解密的认证信息。

### 解密

1. 调用[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)和[AsyKeyGenerator.generateKeyPair](../harmonyos-references/js-apis-cryptoframework.md#generatekeypair)，使用ECC算法生成密钥对。
2. 调用[cryptoFramework.createKeyAgreement](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatekeyagreement)和[KeyAgreement.generateSecret](../harmonyos-references/js-apis-cryptoframework.md#generatesecret11)，基于本端的私钥（KeyPair.priKey）与对端的公钥（KeyPair.pubKey）进行密钥协商，返回共享密钥。
3. X963KDF密钥派生，调用[cryptoFramework.createKdf](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatekdf11)和[Kdf.generateSecret](../harmonyos-references/js-apis-cryptoframework.md#generatesecret11)，基于协商的共享密钥（Secret）进行密钥派生，返回派生后的密钥。
4. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'AES128|GCM'，创建对称密钥类型为AES128、分组模式为GCM的Cipher实例，用于完成解密操作。
5. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为解密（cryptoFramework.CryptoMode.DECRYPT\_MODE），指定解密密钥（SymKey）和GCM模式对应的解密参数（GcmParamsSpec），初始化解密Cipher实例。
6. 调用[Cipher.update](../harmonyos-references/js-apis-cryptoframework.md#update-1)，更新数据（密文）。
7. 调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，获取解密后的数据。

### 示例代码

* 异步方法示例：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { buffer } from '@kit.ArkTS';
  import { BusinessError } from '@kit.BasicServicesKit';

  namespace ECIES {
    function generateGcmParamsSpec(ivData: Uint8Array): cryptoFramework.GcmParamsSpec {
      let ivBlob: cryptoFramework.DataBlob = {
        data: ivData,
      };
      let rand: cryptoFramework.Random = cryptoFramework.createRandom();
      let aadBlob: cryptoFramework.DataBlob = rand.generateRandomSync(8);
      let tagBlob: cryptoFramework.DataBlob = rand.generateRandomSync(16);
      // GCM的authTag在加密时从doFinal结果中获取，在解密时填入init函数的params参数中
      let gcmParams: cryptoFramework.GcmParamsSpec = {
        iv: ivBlob,
        aad: aadBlob,
        authTag: tagBlob,
        algName: 'GcmParamsSpec',
      };
      return gcmParams;
    }

    async function generateSecret(priKey: cryptoFramework.PriKey, pubKey: cryptoFramework.PubKey):
      Promise<cryptoFramework.DataBlob> {
      // EC密钥协商
      let agreement: cryptoFramework.KeyAgreement = cryptoFramework.createKeyAgreement('ECC256');
      let keyData: cryptoFramework.DataBlob = await agreement.generateSecret(priKey, pubKey);

      let infoData: Uint8Array = new Uint8Array(buffer.from('infostring', 'utf-8').buffer);
      let spec: cryptoFramework.X963KdfSpec = {
        algName: 'X963KDF',
        key: keyData.data,
        info: infoData,
        keySize: 32, // 前16字节作为AES128的IV，后16字节作为密钥
      };

      // 使用X963KDF进行密钥派生
      let kdf = cryptoFramework.createKdf('X963KDF|SHA256');
      let secret = await kdf.generateSecret(spec);
      return secret;
    }

    async function generateSymKey(secret: cryptoFramework.DataBlob): Promise<cryptoFramework.SymKey> {
      let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
      let keyData: cryptoFramework.DataBlob = {
        data: secret.data.slice(16),
      };
      let symKey: cryptoFramework.SymKey = await symKeyGenerator.convertKey(keyData);
      return symKey;
    }

    async function encrypt(symKey: cryptoFramework.SymKey, gcmParams: cryptoFramework.GcmParamsSpec,
      plainText: cryptoFramework.DataBlob): Promise<cryptoFramework.DataBlob> {
      // AES-GCM对称加密
      let cipher: cryptoFramework.Cipher = cryptoFramework.createCipher('AES128|GCM');
      await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, gcmParams);
      let cipherText: cryptoFramework.DataBlob = await cipher.update(plainText);
      gcmParams.authTag = await cipher.doFinal(null);
      return cipherText;
    }

    async function decrypt(symKey: cryptoFramework.SymKey, gcmParams: cryptoFramework.GcmParamsSpec,
      cipherText: cryptoFramework.DataBlob): Promise<cryptoFramework.DataBlob> {
      // AES-GCM对称解密
      let cipher: cryptoFramework.Cipher = cryptoFramework.createCipher('AES128|GCM');
      await cipher.init(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, gcmParams);
      let plainText: cryptoFramework.DataBlob = await cipher.doFinal(cipherText);
      return plainText;
    }

    export async function doEciesTest(): Promise<string> {
      try {
        // 生成A端和B端的EC密钥对
        let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
        let keyPairA: cryptoFramework.KeyPair = asyKeyGenerator.generateKeyPairSync();
        let keyPairB: cryptoFramework.KeyPair = asyKeyGenerator.generateKeyPairSync();

        // A端加密：A端的私钥 + B端的公钥
        let secretA: cryptoFramework.DataBlob = await generateSecret(keyPairA.priKey, keyPairB.pubKey);
        let symKeyA: cryptoFramework.SymKey = await generateSymKey(secretA);
        let ivData: Uint8Array = secretA.data.slice(0, 16);
        let gcmParams: cryptoFramework.GcmParamsSpec = generateGcmParamsSpec(ivData);

        let message: string = 'This is a test message!!!';
        let plainText: cryptoFramework.DataBlob = {
          data: new Uint8Array(buffer.from(message, 'utf-8').buffer),
        };
        let cipherData: cryptoFramework.DataBlob = await encrypt(symKeyA, gcmParams, plainText);

        // B端解密：B端的私钥 + A端的公钥
        let secretB: cryptoFramework.DataBlob = await generateSecret(keyPairB.priKey, keyPairA.pubKey);
        let symKeyB: cryptoFramework.SymKey = await generateSymKey(secretB);
        let plainData: cryptoFramework.DataBlob = await decrypt(symKeyB, gcmParams, cipherData);
        console.info('doEciesTest success, message: ' + buffer.from(plainData.data).toString('utf-8'));
        return 'Success';
      } catch (error) {
        let e: BusinessError = error as BusinessError;
        console.error(`doEciesTest failed: errCode: ${e.code}, message: ${e.message}`);
        return 'Failed';
      }
    }
  }
  ```
* 同步方法示例：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { buffer } from '@kit.ArkTS';
  import { BusinessError } from '@kit.BasicServicesKit';

  namespace ECIES {
    function generateGcmParamsSpec(ivData: Uint8Array): cryptoFramework.GcmParamsSpec {
      let ivBlob: cryptoFramework.DataBlob = {
        data: ivData,
      };
      let rand: cryptoFramework.Random = cryptoFramework.createRandom();
      let aadBlob: cryptoFramework.DataBlob = rand.generateRandomSync(8);
      let tagBlob: cryptoFramework.DataBlob = rand.generateRandomSync(16);
      // GCM的authTag在加密时从doFinal结果中获取，在解密时填入init函数的params参数中
      let gcmParams: cryptoFramework.GcmParamsSpec = {
        iv: ivBlob,
        aad: aadBlob,
        authTag: tagBlob,
        algName: 'GcmParamsSpec',
      };
      return gcmParams;
    }

    function generateSecret(priKey: cryptoFramework.PriKey, pubKey: cryptoFramework.PubKey):
      cryptoFramework.DataBlob {
      // EC密钥协商
      let agreement: cryptoFramework.KeyAgreement = cryptoFramework.createKeyAgreement('ECC256');
      let keyData: cryptoFramework.DataBlob = agreement.generateSecretSync(priKey, pubKey);

      let infoData: Uint8Array = new Uint8Array(buffer.from('infostring', 'utf-8').buffer);
      let spec: cryptoFramework.X963KdfSpec = {
        algName: 'X963KDF',
        key: keyData.data,
        info: infoData,
        keySize: 32, // 前16字节作为AES128的IV，后16字节作为密钥
      };

      // 使用X963KDF进行密钥派生
      let kdf = cryptoFramework.createKdf('X963KDF|SHA256');
      let secret = kdf.generateSecretSync(spec);
      return secret;
    }

    function generateSymKey(secret: cryptoFramework.DataBlob): cryptoFramework.SymKey {
      let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
      let keyData: cryptoFramework.DataBlob = {
        data: secret.data.slice(16),
      };
      let symKey: cryptoFramework.SymKey = symKeyGenerator.convertKeySync(keyData);
      return symKey;
    }

    function encrypt(symKey: cryptoFramework.SymKey, gcmParams: cryptoFramework.GcmParamsSpec,
      plainText: cryptoFramework.DataBlob): cryptoFramework.DataBlob {
      // AES-GCM对称加密
      let cipher: cryptoFramework.Cipher = cryptoFramework.createCipher('AES128|GCM');
      cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, gcmParams);
      let cipherText: cryptoFramework.DataBlob = cipher.updateSync(plainText);
      gcmParams.authTag = cipher.doFinalSync(null);
      return cipherText;
    }

    function decrypt(symKey: cryptoFramework.SymKey, gcmParams: cryptoFramework.GcmParamsSpec,
      cipherText: cryptoFramework.DataBlob): cryptoFramework.DataBlob {
      // AES-GCM对称解密
      let cipher: cryptoFramework.Cipher = cryptoFramework.createCipher('AES128|GCM');
      cipher.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, gcmParams);
      let plainText: cryptoFramework.DataBlob = cipher.doFinalSync(cipherText);
      return plainText;
    }

    export function doEciesTest(): string {
      try {
        // 生成A端和B端的EC密钥对
        let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
        let keyPairA: cryptoFramework.KeyPair = asyKeyGenerator.generateKeyPairSync();
        let keyPairB: cryptoFramework.KeyPair = asyKeyGenerator.generateKeyPairSync();

        // A端加密：A端的私钥 + B端的公钥
        let secretA: cryptoFramework.DataBlob = generateSecret(keyPairA.priKey, keyPairB.pubKey);
        let symKeyA: cryptoFramework.SymKey = generateSymKey(secretA);
        let ivData: Uint8Array = secretA.data.slice(0, 16);
        let gcmParams: cryptoFramework.GcmParamsSpec = generateGcmParamsSpec(ivData);

        let message: string = 'This is a test message!!!';
        let plainText: cryptoFramework.DataBlob = {
          data: new Uint8Array(buffer.from(message, 'utf-8').buffer),
        };
        let cipherData: cryptoFramework.DataBlob = encrypt(symKeyA, gcmParams, plainText);

        // B端解密：B端的私钥 + A端的公钥
        let secretB: cryptoFramework.DataBlob = generateSecret(keyPairB.priKey, keyPairA.pubKey);
        let symKeyB: cryptoFramework.SymKey = generateSymKey(secretB);
        let plainData: cryptoFramework.DataBlob = decrypt(symKeyB, gcmParams, cipherData);
        console.info('doEciesTest success, message: ' + buffer.from(plainData.data).toString('utf-8'));
        return 'Success';
      } catch (error) {
        let e: BusinessError = error as BusinessError;
        console.error(`doEciesTest failed: errCode: ${e.code}, message: ${e.message}`);
        return 'Failed';
      }
    }
  }
  ```
