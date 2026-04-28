---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-cbc
title: 使用AES对称密钥（CBC模式）加解密(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用AES对称密钥（CBC模式）加解密(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:23+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:1a93b12fa2ed3f085d80ce77172a43ec992d51d3560bb61802179436d3cf7d6e
---

对应的算法规格请参见[对称密钥加解密算法规格：AES](crypto-sym-encrypt-decrypt-spec.md#aes)。

**加密**

1. 调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)、[SymKeyGenerator.generateSymKey](../harmonyos-references/js-apis-cryptoframework.md#generatesymkey-1)，生成密钥算法为AES、密钥长度为128位的对称密钥（SymKey）。

   如何生成AES对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：AES](crypto-sym-key-generation-conversion-spec.md#aes)和[随机生成对称密钥](crypto-generate-sym-key-randomly.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'AES128|CBC|PKCS7'，创建对称密钥类型为AES128、分组模式为CBC、填充模式为PKCS7的Cipher实例，用于完成加密操作。
3. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为加密（cryptoFramework.CryptoMode.ENCRYPT\_MODE），指定加密密钥（SymKey）和CBC模式对应的加密参数（IvParamsSpec），初始化加密Cipher实例。
4. 当加密内容长度较短时，可以直接调用 [Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1) 而无需调用update，以获取加密后的数据。

**解密**

1. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'AES128|CBC|PKCS7'，创建对称密钥类型为AES128、分组模式为CBC、填充模式为PKCS7的Cipher实例，用于完成解密操作。
2. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为解密（cryptoFramework.CryptoMode.DECRYPT\_MODE），指定解密密钥（SymKey）和CBC模式对应的解密参数（IvParamsSpec），初始化解密Cipher实例。
3. 当解密内容长度较短时，可以省略调用update，直接调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，获取解密后的数据。

* 异步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. function generateRandom(len: number) {
  5. let rand = cryptoFramework.createRandom();
  6. let generateRandSync = rand.generateRandomSync(len);
  7. return generateRandSync;
  8. }

  10. function genIvParamsSpec() {
  11. let ivBlob = generateRandom(16);
  12. let ivParamsSpec: cryptoFramework.IvParamsSpec = {
  13. algName: 'IvParamsSpec',
  14. iv: ivBlob
  15. };
  16. return ivParamsSpec;
  17. }

  19. let iv = genIvParamsSpec();

  21. // 加密消息
  22. async function encryptMessagePromise(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  23. let cipher = cryptoFramework.createCipher('AES128|CBC|PKCS7');
  24. await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, iv);
  25. let cipherData = await cipher.doFinal(plainText);
  26. return cipherData;
  27. }

  29. // 解密消息
  30. async function decryptMessagePromise(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  31. let decoder = cryptoFramework.createCipher('AES128|CBC|PKCS7');
  32. await decoder.init(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, iv);
  33. let decryptData = await decoder.doFinal(cipherText);
  34. return decryptData;
  35. }

  37. async function genSymKeyByData(symKeyData: Uint8Array) {
  38. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  39. let aesGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  40. let symKey = await aesGenerator.convertKey(symKeyBlob);
  41. console.info('convertKey result: success.');
  42. return symKey;
  43. }

  45. async function aesCBC() {
  46. try {
  47. let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  48. let symKey = await genSymKeyByData(keyData);
  49. let message = 'This is a test';
  50. let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  51. let encryptText = await encryptMessagePromise(symKey, plainText);
  52. let decryptText = await decryptMessagePromise(symKey, encryptText);
  53. if (plainText.data.toString() === decryptText.data.toString()) {
  54. console.info('decrypt ok');
  55. console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
  56. } else {
  57. console.error('decrypt failed');
  58. }
  59. } catch (error) {
  60. console.error(`AES CBC failed: errCode: ${error.code}, message: ${error.message}`);
  61. }
  62. }
  ```

  [aes\_cbc\_encryption\_decryption\_asynchronous.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceAesArkTs/entry/src/main/ets/pages/aes_cbc_encryption_decryption/aes_cbc_encryption_decryption_asynchronous.ets#L16-L79)
* 同步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. function generateRandom(len: number) {
  5. let rand = cryptoFramework.createRandom();
  6. let generateRandSync = rand.generateRandomSync(len);
  7. return generateRandSync;
  8. }

  10. function genIvParamsSpec() {
  11. let ivBlob = generateRandom(16);
  12. let ivParamsSpec: cryptoFramework.IvParamsSpec = {
  13. algName: 'IvParamsSpec',
  14. iv: ivBlob
  15. };
  16. return ivParamsSpec;
  17. }

  19. let iv = genIvParamsSpec();

  21. // 加密消息
  22. function encryptMessage(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  23. let cipher = cryptoFramework.createCipher('AES128|CBC|PKCS7');
  24. cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, iv);
  25. let cipherData = cipher.doFinalSync(plainText);
  26. return cipherData;
  27. }

  29. // 解密消息
  30. function decryptMessage(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  31. let decoder = cryptoFramework.createCipher('AES128|CBC|PKCS7');
  32. decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, iv);
  33. let decryptData = decoder.doFinalSync(cipherText);
  34. return decryptData;
  35. }

  37. function genSymKeyByData(symKeyData: Uint8Array) {
  38. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  39. let aesGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  40. let symKey = aesGenerator.convertKeySync(symKeyBlob);
  41. console.info('convertKeySync result: success.');
  42. return symKey;
  43. }

  45. function main() {
  46. try {
  47. let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  48. let symKey = genSymKeyByData(keyData);
  49. let message = 'This is a test';
  50. let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  51. let encryptText = encryptMessage(symKey, plainText);
  52. let decryptText = decryptMessage(symKey, encryptText);
  53. if (plainText.data.toString() === decryptText.data.toString()) {
  54. console.info('decrypt ok.');
  55. console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
  56. } else {
  57. console.error('decrypt failed.');
  58. }
  59. } catch (error) {
  60. console.error(`AES CBC failed: errCode: ${error.code}, message: ${error.message}`);
  61. }
  62. }
  ```

  [aes\_cbc\_encryption\_decryption\_synchronous.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceAesArkTs/entry/src/main/ets/pages/aes_cbc_encryption_decryption/aes_cbc_encryption_decryption_synchronous.ets#L16-L79)
