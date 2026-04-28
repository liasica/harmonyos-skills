---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-wrap-encrypt-decrypt
title: 使用AES-WRAP算法对对称密钥加解密(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用AES-WRAP算法对对称密钥加解密(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:29+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:525c95726b5017056c7fc7d57da8909c6a45e77ef7429d9c81877efb5b870e44
---

从API version 22开始，算法库支持使用该算法进行加密和解密操作。

对应的算法规格请参见[AES-WRAP加解密算法规格](crypto-sym-encrypt-decrypt-spec.md#aes-wrap)。

**加密**

1. 调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)、[SymKeyGenerator.generateSymKey](../harmonyos-references/js-apis-cryptoframework.md#generatesymkey-1)，生成密钥算法为AES、密钥长度为128位的对称密钥（SymKey）。

   如何生成AES对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：AES](crypto-sym-key-generation-conversion-spec.md#aes)和[随机生成对称密钥](crypto-generate-sym-key-randomly.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'AES128-WRAP'，创建类型为AES128-WRAP的Cipher实例，用于完成加密操作。
3. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为加密（cryptoFramework.CryptoMode.ENCRYPT\_MODE），指定加密密钥（SymKey）和对应的加密参数（IvParamsSpec），初始化加密Cipher实例。
4. 当加密内容长度较短时，可以直接调用 [Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1) 而无需调用update，以获取加密后的数据。

**解密**

1. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'AES128-WRAP'，创建类型为AES128-WRAP的Cipher实例，用于完成解密操作。
2. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为解密（cryptoFramework.CryptoMode.DECRYPT\_MODE），指定解密密钥（SymKey）和对应的解密参数（IvParamsSpec），初始化解密Cipher实例。
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
  11. let ivBlob = generateRandom(8);
  12. let ivParamsSpec: cryptoFramework.IvParamsSpec = {
  13. algName: 'IvParamsSpec',
  14. iv: ivBlob
  15. };
  16. return ivParamsSpec;
  17. }
  18. let iv = genIvParamsSpec();
  19. // 加密消息。
  20. async function encryptMessagePromise(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  21. let cipher = cryptoFramework.createCipher('AES128-WRAP');
  22. await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, iv);
  23. let cipherData = await cipher.doFinal(plainText);
  24. return cipherData;
  25. }
  26. // 解密消息。
  27. async function decryptMessagePromise(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  28. let decoder = cryptoFramework.createCipher('AES128-WRAP');
  29. await decoder.init(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, iv);
  30. let decryptData = await decoder.doFinal(cipherText);
  31. return decryptData;
  32. }

  34. async function genSymKeyByData(symKeyData: Uint8Array) {
  35. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  36. let aesGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  37. let symKey = await aesGenerator.convertKey(symKeyBlob);
  38. console.info('convertKey result: success.');
  39. return symKey;
  40. }

  42. async function aesWrapTest() {
  43. try {
  44. let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  45. let symKey = await genSymKeyByData(keyData);
  46. let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(keyData)};
  47. let encryptText = await encryptMessagePromise(symKey, plainText);
  48. let decryptText = await decryptMessagePromise(symKey, encryptText);
  49. if (plainText.data.toString() === decryptText.data.toString()) {
  50. console.info('decrypt ok.');
  51. console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
  52. } else {
  53. console.error('decrypt failed.');
  54. }
  55. } catch (error) {
  56. console.error(`AES Wrap failed: errCode: ${error.code}, message: ${error.message}`);
  57. }
  58. }
  ```

  [AesWrapEncryptionDecryptionAsync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceAesWrap/entry/src/main/ets/pages/aeswrap/AesWrapEncryptionDecryptionAsync.ets#L16-L77)
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
  11. let ivBlob = generateRandom(8);
  12. let ivParamsSpec: cryptoFramework.IvParamsSpec = {
  13. algName: 'IvParamsSpec',
  14. iv: ivBlob
  15. };
  16. return ivParamsSpec;
  17. }
  18. let iv = genIvParamsSpec();
  19. // 加密消息。
  20. function encryptMessage(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  21. let cipher = cryptoFramework.createCipher('AES128-WRAP');
  22. cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, iv);
  23. let cipherData = cipher.doFinalSync(plainText);
  24. return cipherData;
  25. }
  26. // 解密消息。
  27. function decryptMessage(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  28. let decoder = cryptoFramework.createCipher('AES128-WRAP');
  29. decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, iv);
  30. let decryptData = decoder.doFinalSync(cipherText);
  31. return decryptData;
  32. }

  34. function genSymKeyByData(symKeyData: Uint8Array) {
  35. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  36. let aesGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  37. let symKey = aesGenerator.convertKeySync(symKeyBlob);
  38. console.info('convertKeySync result: success.');
  39. return symKey;
  40. }

  42. function main() {
  43. try {
  44. let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  45. let symKey = genSymKeyByData(keyData);
  46. let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(keyData)};
  47. let encryptText = encryptMessage(symKey, plainText);
  48. let decryptText = decryptMessage(symKey, encryptText);
  49. if (plainText.data.toString() === decryptText.data.toString()) {
  50. console.info('decrypt ok.');
  51. console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
  52. } else {
  53. console.error('decrypt failed.');
  54. }
  55. } catch (error) {
  56. console.error(`AES Wrap failed: errCode: ${error.code}, message: ${error.message}`);
  57. }
  58. }
  ```

  [AesWrapEncryptionDecryptionSync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceAesWrap/entry/src/main/ets/pages/aeswrap/AesWrapEncryptionDecryptionSync.ets#L16-L77)
