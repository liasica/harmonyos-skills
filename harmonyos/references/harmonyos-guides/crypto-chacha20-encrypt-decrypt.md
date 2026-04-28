---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-chacha20-encrypt-decrypt
title: 使用ChaCha20对称密钥加解密(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用ChaCha20对称密钥加解密(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:27+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:a42ecc8370aa307f07638fdcfb307b45b24dead93b7d4e6ac1ab42c18a195289
---

从API22开始，算法库支持该算法。

对应的算法规格请查看[对称密钥加解密算法规格：ChaCha20](crypto-sym-encrypt-decrypt-spec.md#chacha20)。

## 开发步骤

**创建对象**

调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)、[SymKeyGenerator.generateSymKey](../harmonyos-references/js-apis-cryptoframework.md#generatesymkey-1)，生成密钥算法为ChaCha20的对称密钥（SymKey）。

如何生成ChaCha20对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：ChaCha20](crypto-sym-key-generation-conversion-spec.md#chacha20)和[随机生成对称密钥](crypto-generate-sym-key-randomly.md)理解。参考文档与示例可能存在入参差异，请注意区分。

**加密**

1. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'ChaCha20'，创建对称密钥的Cipher实例，用于完成加密操作。
2. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为加密（cryptoFramework.CryptoMode.ENCRYPT\_MODE），指定加密密钥（SymKey）和对应的加密参数（IvParamsSpec），初始化加密Cipher实例。
3. 调用[Cipher.update](../harmonyos-references/js-apis-cryptoframework.md#update-1)，更新数据（明文）。
4. 调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，获取加密后的数据。

   说明

   由于已使用update传入数据，此处data传入null。

   doFinal输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。

**解密**

1. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'ChaCha20'，创建对称密钥的Cipher实例，用于完成解密操作。
2. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为解密（cryptoFramework.CryptoMode.DECRYPT\_MODE），指定解密密钥（SymKey）和对应的解密参数（IvParamsSpec），初始化解密Cipher实例。
3. 调用[Cipher.update](../harmonyos-references/js-apis-cryptoframework.md#update-1)，更新数据（密文）。
4. 调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，获取解密后的数据。

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
  18. let ivSpec = genIvParamsSpec();

  20. // 加密消息。
  21. async function encryptMessagePromise(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  22. let cipher = cryptoFramework.createCipher('ChaCha20');
  23. await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, ivSpec);
  24. let encryptData = await cipher.doFinal(plainText);
  25. return encryptData;
  26. }

  28. // 解密消息。
  29. async function decryptMessagePromise(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  30. let decoder = cryptoFramework.createCipher('ChaCha20');
  31. await decoder.init(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, ivSpec);
  32. let decryptData = await decoder.doFinal(cipherText);
  33. return decryptData;
  34. }

  36. async function genSymKeyByData(symKeyData: Uint8Array) {
  37. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  38. let chacha20Generator = cryptoFramework.createSymKeyGenerator('ChaCha20');
  39. let symKey = await chacha20Generator.convertKey(symKeyBlob);
  40. console.info('convertKey result: success.');
  41. return symKey;
  42. }

  44. async function main() {
  45. try {
  46. let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159, 83,
  47. 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  48. let symKey = await genSymKeyByData(keyData);
  49. let message = 'This is a test';
  50. let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  51. let encryptText = await encryptMessagePromise(symKey, plainText);
  52. let decryptText = await decryptMessagePromise(symKey, encryptText);
  53. if (plainText.data.toString() === decryptText.data.toString()) {
  54. console.info('decrypt ok.');
  55. console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
  56. } else {
  57. console.error('decrypt failed.');
  58. }
  59. } catch (error) {
  60. console.error(`decrypt failed: errCode: ${error.code}, message: ${error.message}`);
  61. }
  62. }
  ```

  [ChaCha20EncryptionDecryptionAsync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceChaCha20/entry/src/main/ets/pages/chacha20/ChaCha20EncryptionDecryptionAsync.ets#L16-L78)
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

  19. let ivSpec = genIvParamsSpec();

  21. // 加密消息。
  22. function encryptMessage(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  23. let cipher = cryptoFramework.createCipher('ChaCha20');
  24. cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, ivSpec);
  25. let encryptData = cipher.doFinalSync(plainText);
  26. return encryptData;
  27. }

  29. // 解密消息。
  30. function decryptMessage(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  31. let decoder = cryptoFramework.createCipher('ChaCha20');
  32. decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, ivSpec);
  33. let decryptData = decoder.updateSync(cipherText);
  34. return decryptData;
  35. }

  37. function genSymKeyByData(symKeyData: Uint8Array) {
  38. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  39. let chacha20Generator = cryptoFramework.createSymKeyGenerator('ChaCha20');
  40. let symKey = chacha20Generator.convertKeySync(symKeyBlob);
  41. console.info('convertKeySync result: success.');
  42. return symKey;
  43. }

  45. function main() {
  46. try {
  47. let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159, 83,
  48. 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  49. let symKey = genSymKeyByData(keyData);
  50. let message = 'This is a test';
  51. let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  52. let encryptText = encryptMessage(symKey, plainText);
  53. let decryptText = decryptMessage(symKey, encryptText);
  54. if (plainText.data.toString() === decryptText.data.toString()) {
  55. console.info('decrypt ok.');
  56. console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
  57. } else {
  58. console.error('decrypt failed.');
  59. }
  60. } catch (error) {
  61. console.error(`decrypt failed: errCode: ${error.code}, message: ${error.message}`);
  62. }
  63. }
  ```

  [ChaCha20EncryptionDecryptionSync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceChaCha20/entry/src/main/ets/pages/chacha20/ChaCha20EncryptionDecryptionSync.ets#L16-L82)
