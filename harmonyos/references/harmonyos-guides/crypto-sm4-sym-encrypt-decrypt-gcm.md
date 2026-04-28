---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm4-sym-encrypt-decrypt-gcm
title: 使用SM4对称密钥（GCM模式）加解密(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用SM4对称密钥（GCM模式）加解密(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:26+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:2cba6e825c1acc8bd1c35de0c0e470659510faab81c8dff60cafde2c8c3e9670
---

对应的算法规格请查看[对称密钥加解密算法规格：SM4](crypto-sym-encrypt-decrypt-spec.md#sm4)。

**加密**

1. 调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)、[SymKeyGenerator.generateSymKey](../harmonyos-references/js-apis-cryptoframework.md#generatesymkey-1)，生成密钥算法为SM4、密钥长度为128位的对称密钥（SymKey）。

   如何生成SM4对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：SM4](crypto-sym-key-generation-conversion-spec.md#sm4)和[随机生成对称密钥](crypto-generate-sym-key-randomly.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'SM4\_128|GCM|PKCS7'，创建对称密钥类型为SM4\_128、分组模式为GCM、填充模式为PKCS7的Cipher实例，用于完成加密操作。
3. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为加密（cryptoFramework.CryptoMode.ENCRYPT\_MODE），指定加密密钥（SymKey）和GCM模式对应的加密参数（GcmParamsSpec），初始化加密Cipher实例。
4. 调用[Cipher.update](../harmonyos-references/js-apis-cryptoframework.md#update-1)，更新数据（明文）。

   当前单次update长度没有限制，开发者可以根据数据量判断如何调用update。

   * 当数据量较小时，可以在init完成后直接调用doFinal。
   * 当数据量较大时，可以多次调用update，即[分段加解密](crypto-sm4-sym-encrypt-decrypt-gcm-by-segment.md)。
5. 调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，获取加密后的数据。

   * 由于已使用update传入数据，此处data传入null。
   * doFinal输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。
6. 读取[GcmParamsSpec](../harmonyos-references/js-apis-cryptoframework.md#gcmparamsspec).authTag作为解密的认证信息。

   在GCM模式下，需要从加密后的数据中取出末尾16字节，作为解密时初始化的认证信息。示例中authTag恰好为16字节。

**解密**

1. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'SM4\_128|GCM|PKCS7'，创建对称密钥类型为SM4\_128、分组模式为GCM、填充模式为PKCS7的Cipher实例，用于完成解密操作。
2. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为解密（cryptoFramework.CryptoMode.DECRYPT\_MODE），指定解密密钥（SymKey）和GCM模式对应的解密参数（GcmParamsSpec），初始化解密Cipher实例。
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

  10. function genGcmParamsSpec() {
  11. let ivBlob = generateRandom(12); // 12 bytes
  12. let arr = [1, 2, 3, 4, 5, 6, 7, 8]; // 8 bytes
  13. let dataAad = new Uint8Array(arr);
  14. let aadBlob: cryptoFramework.DataBlob = { data: dataAad };
  15. arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; // 16 bytes
  16. let dataTag = new Uint8Array(arr);
  17. let tagBlob: cryptoFramework.DataBlob = {
  18. data: dataTag
  19. };
  20. // GCM的authTag在加密时从doFinal结果中获取，在解密时填入init函数的params参数中
  21. let gcmParamsSpec: cryptoFramework.GcmParamsSpec = {
  22. iv: ivBlob,
  23. aad: aadBlob,
  24. authTag: tagBlob,
  25. algName: 'GcmParamsSpec'
  26. };
  27. return gcmParamsSpec;
  28. }

  30. let gcmParams = genGcmParamsSpec();

  32. // 加密消息
  33. async function encryptMessagePromise(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  34. let cipher = cryptoFramework.createCipher('SM4_128|GCM|PKCS7');
  35. await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, gcmParams);
  36. let encryptUpdate = await cipher.update(plainText);
  37. // gcm模式加密doFinal时传入空，获得tag数据，并更新至gcmParams对象中。
  38. gcmParams.authTag = await cipher.doFinal(null);
  39. return encryptUpdate;
  40. }

  42. // 解密消息
  43. async function decryptMessagePromise(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  44. let decoder = cryptoFramework.createCipher('SM4_128|GCM|PKCS7');
  45. await decoder.init(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, gcmParams);
  46. let decryptUpdate = await decoder.update(cipherText);
  47. // gcm模式解密doFinal时传入空，验证init时传入的tag数据，如果验证失败会抛出异常。
  48. let decryptData = await decoder.doFinal(null);
  49. if (decryptData == null) {
  50. console.info('GCM decrypt result: success, decryptData is null.');
  51. }
  52. return decryptUpdate;
  53. }

  55. async function genSymKeyByData(symKeyData: Uint8Array) {
  56. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  57. let sm4Generator = cryptoFramework.createSymKeyGenerator('SM4_128');
  58. let symKey = await sm4Generator.convertKey(symKeyBlob);
  59. console.info('convertKey result: success.');
  60. return symKey;
  61. }

  63. async function main() {
  64. let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  65. let symKey = await genSymKeyByData(keyData);
  66. let message = 'This is a test';
  67. let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  68. let encryptText = await encryptMessagePromise(symKey, plainText);
  69. let decryptText = await decryptMessagePromise(symKey, encryptText);
  70. if (plainText.data.toString() === decryptText.data.toString()) {
  71. console.info('decrypt ok.');
  72. console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
  73. } else {
  74. console.error('decrypt failed.');
  75. }
  76. }
  ```

  [sm4\_gcm\_encryption\_decryption\_asynchronous.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceSM4ArkTs/entry/src/main/ets/pages/sm4_gcm_encryption_decryption/sm4_gcm_encryption_decryption_asynchronous.ets#L16-L93)
* 同步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. function generateRandom(len: number) {
  5. let rand = cryptoFramework.createRandom();
  6. let generateRandSync = rand.generateRandomSync(len);
  7. return generateRandSync;
  8. }

  10. function genGcmParamsSpec() {
  11. let ivBlob = generateRandom(12); // 12 bytes
  12. let arr = [1, 2, 3, 4, 5, 6, 7, 8]; // 8 bytes
  13. let dataAad = new Uint8Array(arr);
  14. let aadBlob: cryptoFramework.DataBlob = { data: dataAad };
  15. arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; // 16 bytes
  16. let dataTag = new Uint8Array(arr);
  17. let tagBlob: cryptoFramework.DataBlob = {
  18. data: dataTag
  19. };
  20. // GCM的authTag在加密时从doFinal结果中获取，在解密时填入init函数的params参数中
  21. let gcmParamsSpec: cryptoFramework.GcmParamsSpec = {
  22. iv: ivBlob,
  23. aad: aadBlob,
  24. authTag: tagBlob,
  25. algName: 'GcmParamsSpec'
  26. };
  27. return gcmParamsSpec;
  28. }

  30. let gcmParams = genGcmParamsSpec();

  32. // 加密消息
  33. function encryptMessage(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  34. let cipher = cryptoFramework.createCipher('SM4_128|GCM|PKCS7');
  35. cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, gcmParams);
  36. let encryptUpdate = cipher.updateSync(plainText);
  37. // gcm模式加密doFinal时传入空，获得tag数据，并更新至gcmParams对象中。
  38. gcmParams.authTag = cipher.doFinalSync(null);
  39. return encryptUpdate;
  40. }

  42. // 解密消息
  43. function decryptMessage(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  44. let decoder = cryptoFramework.createCipher('SM4_128|GCM|PKCS7');
  45. decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, gcmParams);
  46. let decryptUpdate = decoder.updateSync(cipherText);
  47. // gcm模式解密doFinal时传入空，验证init时传入的tag数据，如果验证失败会抛出异常。
  48. let decryptData = decoder.doFinalSync(null);
  49. if (decryptData == null) {
  50. console.info('GCM decrypt result: success, decryptData is null.');
  51. }
  52. return decryptUpdate;
  53. }

  55. function genSymKeyByData(symKeyData: Uint8Array) {
  56. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  57. let sm4Generator = cryptoFramework.createSymKeyGenerator('SM4_128');
  58. let symKey = sm4Generator.convertKeySync(symKeyBlob);
  59. console.info('convertKeySync result: success.');
  60. return symKey;
  61. }

  63. function main() {
  64. let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  65. let symKey = genSymKeyByData(keyData);
  66. let message = 'This is a test';
  67. let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  68. let encryptText = encryptMessage(symKey, plainText);
  69. let decryptText = decryptMessage(symKey, encryptText);
  70. if (plainText.data.toString() === decryptText.data.toString()) {
  71. console.info('decrypt ok.');
  72. console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
  73. } else {
  74. console.error('decrypt failed.');
  75. }
  76. }
  ```

  [sm4\_gcm\_encryption\_decryption\_synchronous.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceSM4ArkTs/entry/src/main/ets/pages/sm4_gcm_encryption_decryption/sm4_gcm_encryption_decryption_synchronous.ets#L16-L93)
