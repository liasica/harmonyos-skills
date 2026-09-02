---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rc4-sym-encrypt-decrypt
title: 使用RC4对称密钥加解密(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密介绍 > 使用RC4对称密钥加解密(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:00+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:44c2005f22d527f46f105e7ea5ab898bc46c1870f351a880a637b4772309d38a
---

从API版本26.0.0开始，算法库支持RC4对称密钥加解密。

对应的算法规格请参见[对称密钥加解密算法规格：RC4](crypto-encryption-decryption.md#rc4)。

RC4为流密码算法，无需分组模式与填充。

**加密**

1. 调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)、[SymKeyGenerator.generateSymKey](../harmonyos-references/js-apis-cryptoframework.md#generatesymkey-1)或[SymKeyGenerator.convertKey](../harmonyos-references/js-apis-cryptoframework.md#convertkey-1)，生成密钥算法为RC4、密钥长度在8位～4096位范围内（如RC4\_128）的对称密钥（SymKey）。

   如何生成RC4对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：RC4](crypto-key-generation-conversion.md#rc4)和[指定二进制数据转换对称密钥](crypto-convert-binary-data-to-sym-key.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数（如'RC4'），创建对称密钥类型为RC4的Cipher实例，用于完成加密操作。
3. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为加密（cryptoFramework.CryptoMode.ENCRYPT\_MODE），指定加密密钥（SymKey），初始化加密Cipher实例。RC4为流密码，无IV等加解密参数时传入null。
4. 当加密内容长度较短时，可以直接调用 [Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1) 而无需调用update，以获取加密后的数据。

**解密**

1. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数（如'RC4'），创建对称密钥类型为RC4的Cipher实例，用于完成解密操作。
2. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为解密（cryptoFramework.CryptoMode.DECRYPT\_MODE），指定解密密钥（SymKey）初始化解密Cipher实例。无加解密参数时传入null。
3. 当解密内容长度较短时，可以省略调用update，直接调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，获取解密后的数据。

* 异步方法示例：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { buffer } from '@kit.ArkTS';

  // 加密消息
  async function encryptMessagePromise(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
    let cipher = cryptoFramework.createCipher('RC4');
    await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, null);
    let cipherData = await cipher.doFinal(plainText);
    return cipherData;
  }

  // 解密消息
  async function decryptMessagePromise(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
    let decoder = cryptoFramework.createCipher('RC4');
    await decoder.init(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, null);
    let decryptData = await decoder.doFinal(cipherText);
    return decryptData;
  }

  async function genSymKeyByData(symKeyData: Uint8Array) {
    let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
    let rc4Generator = cryptoFramework.createSymKeyGenerator('RC4');
    let symKey = await rc4Generator.convertKey(symKeyBlob);
    console.info('convertKey result: success.');
    return symKey;
  }

  async function rc4EncryptionDecryption() {
    let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
    let symKey = await genSymKeyByData(keyData);
    let message = 'This is a test';
    let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
    let encryptText = await encryptMessagePromise(symKey, plainText);
    let decryptText = await decryptMessagePromise(symKey, encryptText);
    if (plainText.data.toString() === decryptText.data.toString()) {
      console.info('decrypt ok.');
      console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
    } else {
      console.error('decrypt failed.');
    }
  }
  ```
* 同步方法示例：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { buffer } from '@kit.ArkTS';

  // 加密消息
  function encryptMessage(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
    let cipher = cryptoFramework.createCipher('RC4');
    cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, null);
    let cipherData = cipher.doFinalSync(plainText);
    return cipherData;
  }

  // 解密消息
  function decryptMessage(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
    let decoder = cryptoFramework.createCipher('RC4');
    decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, null);
    let decryptData = decoder.doFinalSync(cipherText);
    return decryptData;
  }

  function genSymKeyByData(symKeyData: Uint8Array) {
    let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
    let rc4Generator = cryptoFramework.createSymKeyGenerator('RC4');
    let symKey = rc4Generator.convertKeySync(symKeyBlob);
    console.info('convertKeySync result: success.');
    return symKey;
  }

  function rc4EncryptionDecryption() {
    let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
    let symKey = genSymKeyByData(keyData);
    let message = 'This is a test';
    let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
    let encryptText = encryptMessage(symKey, plainText);
    let decryptText = decryptMessage(symKey, encryptText);
    if (plainText.data.toString() === decryptText.data.toString()) {
      console.info('decrypt ok.');
      console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
    } else {
      console.error('decrypt failed.');
    }
  }
  ```
