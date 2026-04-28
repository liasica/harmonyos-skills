---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-ccm
title: 使用AES对称密钥（CCM模式）加解密(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用AES对称密钥（CCM模式）加解密(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:23+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:4fe5c995dc0b2320b06297dc24bf285a4a3b9dc866573162ba22be79924b8f2c
---

查看[对称密钥加解密算法规格：AES](crypto-sym-encrypt-decrypt-spec.md#aes)。

**加密**

1. 调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)、[SymKeyGenerator.generateSymKey](../harmonyos-references/js-apis-cryptoframework.md#generatesymkey-1)，生成密钥算法为AES、密钥长度为128位的对称密钥（SymKey）。

   如何生成AES对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：AES](crypto-sym-key-generation-conversion-spec.md#aes)和[随机生成对称密钥](crypto-generate-sym-key-randomly.md)进行理解，参考文档与当前示例可能存在入参差异，请注意区分。
2. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'AES128|CCM'，创建对称密钥为AES128、分组模式为CCM的Cipher实例，用于执行加密操作。
3. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为加密（cryptoFramework.CryptoMode.ENCRYPT\_MODE），指定密钥（SymKey）和CCM模式对应的加密参数（CcmParamsSpec），初始化加密Cipher实例。
4. 调用[Cipher.update](../harmonyos-references/js-apis-cryptoframework.md#update-1)，更新数据（明文）。

   当前单次update没有长度限制，开发者可以根据数据量决定如何调用update。

   说明

   CCM模式不支持分段加解密。
5. 调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)获取加密后的数据。

   * 由于已通过update传入数据，此处传入null。
   * doFinal输出结果可能为null，访问具体数据前，需先判断结果是否为null，以避免异常。
6. 读取[CcmParamsSpec.authTag](../harmonyos-references/js-apis-cryptoframework.md#ccmparamsspec)作为解密的认证信息。

   在CCM模式下，算法库目前仅支持12字节的authTag，用于解密时的初始化认证信息。示例中的authTag为12字节。

**解密**

1. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'AES128|CCM'，创建对称密钥为AES128、分组模式为CCM的Cipher实例，用于完成解密操作。
2. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为解密（cryptoFramework.CryptoMode.DECRYPT\_MODE），指定密钥（SymKey）和CCM模式对应的解密参数（CcmParamsSpec），初始化解密Cipher实例。
3. 调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，获取解密后的数据。

* 异步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. function genCcmParamsSpec() {
  5. let rand: cryptoFramework.Random = cryptoFramework.createRandom();
  6. let ivBlob: cryptoFramework.DataBlob = rand.generateRandomSync(7);
  7. let aadBlob: cryptoFramework.DataBlob = rand.generateRandomSync(8);
  8. let arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; // 12 bytes
  9. let dataTag = new Uint8Array(arr);
  10. let tagBlob: cryptoFramework.DataBlob = {
  11. data: dataTag
  12. };
  13. // CCM的authTag在加密时从doFinal结果中获取，在解密时填入init函数的params参数中
  14. let ccmParamsSpec: cryptoFramework.CcmParamsSpec = {
  15. iv: ivBlob,
  16. aad: aadBlob,
  17. authTag: tagBlob,
  18. algName: 'CcmParamsSpec'
  19. };
  20. return ccmParamsSpec;
  21. }

  23. let ccmParams = genCcmParamsSpec();

  25. // 加密消息
  26. async function encryptMessagePromise(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  27. let cipher = cryptoFramework.createCipher('AES128|CCM');
  28. await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, ccmParams);
  29. let encryptUpdate = await cipher.update(plainText);
  30. // ccm模式加密doFinal时传入空，获得tag数据，并更新至ccmParams对象中。
  31. ccmParams.authTag = await cipher.doFinal(null);
  32. return encryptUpdate;
  33. }

  35. // 解密消息
  36. async function decryptMessagePromise(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  37. let decoder = cryptoFramework.createCipher('AES128|CCM');
  38. await decoder.init(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, ccmParams);
  39. let decryptUpdate = await decoder.doFinal(cipherText);
  40. return decryptUpdate;
  41. }

  43. async function genSymKeyByData(symKeyData: Uint8Array) {
  44. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  45. let aesGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  46. let symKey = await aesGenerator.convertKey(symKeyBlob);
  47. console.info('convertKey result: success.');
  48. return symKey;
  49. }

  51. async function main() {
  52. let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  53. let symKey = await genSymKeyByData(keyData);
  54. let message = 'This is a test';
  55. let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  56. let encryptText = await encryptMessagePromise(symKey, plainText);
  57. let decryptText = await decryptMessagePromise(symKey, encryptText);
  58. if (plainText.data.toString() === decryptText.data.toString()) {
  59. console.info('decrypt ok.');
  60. console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
  61. } else {
  62. console.error('decrypt failed.');
  63. }
  64. }
  ```

  [aes\_ccm\_encryption\_decryption\_asynchronous.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceAesArkTs/entry/src/main/ets/pages/aes_ccm_encryption_decryption/aes_ccm_encryption_decryption_asynchronous.ets#L16-L81)
* 同步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. function genCcmParamsSpec() {
  5. let rand: cryptoFramework.Random = cryptoFramework.createRandom();
  6. let ivBlob: cryptoFramework.DataBlob = rand.generateRandomSync(7);
  7. let aadBlob: cryptoFramework.DataBlob = rand.generateRandomSync(8);
  8. let arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; // 12 bytes
  9. let dataTag = new Uint8Array(arr);
  10. let tagBlob: cryptoFramework.DataBlob = {
  11. data: dataTag
  12. };
  13. // CCM的authTag在加密时从doFinal结果中获取，在解密时填入init函数的params参数中
  14. let ccmParamsSpec: cryptoFramework.CcmParamsSpec = {
  15. iv: ivBlob,
  16. aad: aadBlob,
  17. authTag: tagBlob,
  18. algName: 'CcmParamsSpec'
  19. };
  20. return ccmParamsSpec;
  21. }

  23. let ccmParams = genCcmParamsSpec();

  25. // 加密消息
  26. function encryptMessage(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  27. let cipher = cryptoFramework.createCipher('AES128|CCM');
  28. cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, ccmParams);
  29. let encryptUpdate = cipher.updateSync(plainText);
  30. // ccm模式加密doFinal时传入空，获得tag数据，并更新至ccmParams对象中。
  31. ccmParams.authTag = cipher.doFinalSync(null);
  32. return encryptUpdate;
  33. }

  35. // 解密消息
  36. function decryptMessage(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  37. let decoder = cryptoFramework.createCipher('AES128|CCM');
  38. decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, ccmParams);
  39. let decryptUpdate = decoder.doFinalSync(cipherText);
  40. return decryptUpdate;
  41. }

  43. function genSymKeyByData(symKeyData: Uint8Array) {
  44. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  45. let aesGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  46. let symKey = aesGenerator.convertKeySync(symKeyBlob);
  47. console.info('convertKeySync result: success.');
  48. return symKey;
  49. }

  51. function main() {
  52. let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  53. let symKey = genSymKeyByData(keyData);
  54. let message = 'This is a test';
  55. let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  56. let encryptText = encryptMessage(symKey, plainText);
  57. let decryptText = decryptMessage(symKey, encryptText);
  58. if (plainText.data.toString() === decryptText.data.toString()) {
  59. console.info('decrypt ok.');
  60. console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
  61. } else {
  62. console.error('decrypt failed.');
  63. }
  64. }
  ```

  [aes\_ccm\_encryption\_decryption\_synchronous.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceAesArkTs/entry/src/main/ets/pages/aes_ccm_encryption_decryption/aes_ccm_encryption_decryption_synchronous.ets#L16-L81)
