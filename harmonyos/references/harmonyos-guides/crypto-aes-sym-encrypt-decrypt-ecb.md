---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-ecb
title: 使用AES对称密钥（ECB模式）加解密(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用AES对称密钥（ECB模式）加解密(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:24+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:9ebd027ac6cbcf7461cf388a3d333e6499d99d81d175ac03172bcf94d95d68c4
---

请查看[对称密钥加解密算法规格：AES](crypto-sym-encrypt-decrypt-spec.md#aes)。

**加密**

1. 调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)、[SymKeyGenerator.generateSymKey](../harmonyos-references/js-apis-cryptoframework.md#generatesymkey-1)，生成密钥算法为AES、密钥长度为128位的对称密钥（SymKey）。

   如何生成AES对称密钥，开发者可以参考以下示例，并结合[对称密钥生成和转换规格：AES](crypto-sym-key-generation-conversion-spec.md#aes)和[随机生成对称密钥](crypto-generate-sym-key-randomly.md)进行理解。参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'AES128|ECB|PKCS7'，创建对称密钥类型为AES128、分组模式为ECB、填充模式为PKCS7的Cipher实例，用于完成加密操作。
3. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为加密（cryptoFramework.CryptoMode.ENCRYPT\_MODE），指定加密密钥（SymKey），ECB模式Params为空，初始化加密Cipher实例。
4. 加密内容较短时，可以不调用update，直接调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，获取加密后的数据。

**解密**

1. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'AES128|ECB|PKCS7'，创建对称密钥类型为AES128、分组模式为ECB、填充模式为PKCS7的Cipher实例，用于完成解密操作。
2. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为解密（cryptoFramework.CryptoMode.DECRYPT\_MODE），指定解密密钥（SymKey），ECB模式Params为空，初始化解密Cipher实例。
3. 解密内容较短时，可以不调用update，直接调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，获取解密后的数据。

* 异步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. // 加密消息
  5. async function encryptMessagePromise(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  6. let cipher = cryptoFramework.createCipher('AES128|ECB|PKCS7');
  7. await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, null);
  8. let cipherData = await cipher.doFinal(plainText);
  9. return cipherData;
  10. }

  12. // 解密消息
  13. async function decryptMessagePromise(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  14. let decoder = cryptoFramework.createCipher('AES128|ECB|PKCS7');
  15. await decoder.init(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, null);
  16. let decryptData = await decoder.doFinal(cipherText);
  17. return decryptData;
  18. }

  20. async function genSymKeyByData(symKeyData: Uint8Array) {
  21. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  22. let aesGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  23. let symKey = await aesGenerator.convertKey(symKeyBlob);
  24. console.info('convertKey result: success.');
  25. return symKey;
  26. }

  28. async function aesECB() {
  29. try {
  30. let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  31. let symKey = await genSymKeyByData(keyData);
  32. let message = 'This is a test';
  33. let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  34. let encryptText = await encryptMessagePromise(symKey, plainText);
  35. let decryptText = await decryptMessagePromise(symKey, encryptText);
  36. if (plainText.data.toString() === decryptText.data.toString()) {
  37. console.info('decrypt ok.');
  38. console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
  39. } else {
  40. console.error('decrypt failed.');
  41. }
  42. } catch (error) {
  43. console.error(`AES ECB failed: errCode: ${error.code}, message: ${error.message}`);
  44. }
  45. }
  ```

  [aes\_ecb\_encryption\_decryption\_asynchronous.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceAesArkTs/entry/src/main/ets/pages/aes_ecb_encryption_decryption/aes_ecb_encryption_decryption_asynchronous.ets#L16-L62)
* 同步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. // 加密消息
  5. function encryptMessage(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  6. let cipher = cryptoFramework.createCipher('AES128|ECB|PKCS7');
  7. cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, null);
  8. let cipherData = cipher.doFinalSync(plainText);
  9. return cipherData;
  10. }

  12. // 解密消息
  13. function decryptMessage(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  14. let decoder = cryptoFramework.createCipher('AES128|ECB|PKCS7');
  15. decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, null);
  16. let decryptData = decoder.doFinalSync(cipherText);
  17. return decryptData;
  18. }

  20. function genSymKeyByData(symKeyData: Uint8Array) {
  21. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  22. let aesGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  23. let symKey = aesGenerator.convertKeySync(symKeyBlob);
  24. console.info('convertKeySync result: success.');
  25. return symKey;
  26. }

  28. function main() {
  29. try {
  30. let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  31. let symKey = genSymKeyByData(keyData);
  32. let message = 'This is a test';
  33. let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  34. let encryptText = encryptMessage(symKey, plainText);
  35. let decryptText = decryptMessage(symKey, encryptText);
  36. if (plainText.data.toString() === decryptText.data.toString()) {
  37. console.info('decrypt ok.');
  38. console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
  39. } else {
  40. console.error('decrypt failed.');
  41. }
  42. } catch (error) {
  43. console.error(`AES ECB failed: errCode: ${error.code}, message: ${error.message}`);
  44. }
  45. }
  ```

  [aes\_ecb\_encryption\_decryption\_synchronous.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceAesArkTs/entry/src/main/ets/pages/aes_ecb_encryption_decryption/aes_ecb_encryption_decryption_synchronous.ets#L16-L62)
