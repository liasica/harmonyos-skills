---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-chacha20-encrypt-decrypt-poly1305
title: 使用ChaCha20对称密钥（Poly1305模式）加解密(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用ChaCha20对称密钥（Poly1305模式）加解密(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:28+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:bcaf7b237ad8280c2bdc4908f487c4907148a76881810fc5d13d4cc1bfbb2309
---

从API22开始，算法库支持该算法。

对应的算法规格请查看[对称密钥加解密算法规格：ChaCha20](crypto-sym-encrypt-decrypt-spec.md#chacha20)。

## 开发步骤

**创建对象**

调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)、[SymKeyGenerator.generateSymKey](../harmonyos-references/js-apis-cryptoframework.md#generatesymkey-1)，生成密钥算法为ChaCha20的对称密钥（SymKey）。

如何生成ChaCha20对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：ChaCha20](crypto-sym-key-generation-conversion-spec.md#chacha20)和[随机生成对称密钥](crypto-generate-sym-key-randomly.md)理解。参考文档与示例可能存在入参差异，请注意区分。

**加密**

1. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'ChaCha20|Poly1305'，创建对称密钥类型为ChaCha20、模式为Poly1305的Cipher实例，用于完成加密操作。
2. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为加密（cryptoFramework.CryptoMode.ENCRYPT\_MODE），指定加密密钥（SymKey）和Poly1305模式对应的加密参数（Poly1305ParamsSpec），初始化加密Cipher实例。
3. 调用[Cipher.update](../harmonyos-references/js-apis-cryptoframework.md#update-1)，更新数据（明文）。
4. 调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，获取加密后的数据。

   说明

   由于已使用update传入数据，此处data传入null。

   doFinal输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。
5. 读取[Poly1305ParamsSpec](../harmonyos-references/js-apis-cryptoframework.md#poly1305paramsspec22).authTag作为解密的认证信息。

   在Poly1305模式下，需要从加密后的数据中取出末尾16字节，作为解密时初始化的认证信息。

**解密**

1. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'ChaCha20|Poly1305'，创建对称密钥类型为ChaCha20、模式为Poly1305的Cipher实例，用于完成解密操作。
2. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为解密（cryptoFramework.CryptoMode.DECRYPT\_MODE），指定解密密钥（SymKey）和Poly1305模式对应的解密参数（Poly1305ParamsSpec），初始化解密Cipher实例。
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

  10. function genPoly1305ParamsSpec() {
  11. let ivBlob = generateRandom(12); // 12 bytes
  12. let arr = [1, 2, 3, 4, 5, 6, 7, 8]; // 8 bytes
  13. let dataAad = new Uint8Array(arr);
  14. let aadBlob: cryptoFramework.DataBlob = { data: dataAad };
  15. arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; // 16 bytes
  16. let dataTag = new Uint8Array(arr);
  17. let tagBlob: cryptoFramework.DataBlob = {
  18. data: dataTag
  19. };
  20. // Poly1305的authTag在加密时从doFinal结果中获取，在解密时填入init函数的params参数中。
  21. let poly1305ParamsSpec: cryptoFramework.Poly1305ParamsSpec = {
  22. iv: ivBlob,
  23. aad: aadBlob,
  24. authTag: tagBlob,
  25. algName: 'Poly1305ParamsSpec'
  26. };
  27. return poly1305ParamsSpec;
  28. }

  30. let poly1305Params = genPoly1305ParamsSpec();

  32. // 加密消息。
  33. async function encryptMessagePromise(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  34. let cipher = cryptoFramework.createCipher('ChaCha20|Poly1305');
  35. await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, poly1305Params);
  36. let encryptUpdate = await cipher.update(plainText);
  37. // poly1305模式加密doFinal时传入空，获得tag数据，并更新至poly1305Params对象中。
  38. poly1305Params.authTag = await cipher.doFinal(null);
  39. return encryptUpdate;
  40. }
  41. // 解密消息。
  42. async function decryptMessagePromise(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  43. let decoder = cryptoFramework.createCipher('ChaCha20|Poly1305');
  44. await decoder.init(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, poly1305Params);
  45. let decryptData = await decoder.update(cipherText);
  46. // poly1305模式解密doFinal时传入空，验证init时传入的tag数据，如果验证失败会抛出异常。
  47. let decryptData = await decoder.doFinal(null);
  48. if (decryptData === null) {
  49. console.info('poly1305 decrypt result: success, decryptData is null.');
  50. }
  51. return decryptData;
  52. }
  53. async function genSymKeyByData(symKeyData: Uint8Array) {
  54. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  55. let chacha20Generator = cryptoFramework.createSymKeyGenerator('ChaCha20');
  56. let symKey = await chacha20Generator.convertKey(symKeyBlob);
  57. console.info('convertKey result: success.');
  58. return symKey;
  59. }
  60. async function main() {
  61. try {
  62. let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159,
  63. 83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  64. let symKey = await genSymKeyByData(keyData);
  65. let message = 'This is a test';
  66. let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  67. let encryptText = await encryptMessagePromise(symKey, plainText);
  68. let decryptText = await decryptMessagePromise(symKey, encryptText);
  69. if (plainText.data.toString() === decryptText.data.toString()) {
  70. console.info('decrypt ok.');
  71. console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
  72. } else {
  73. console.error('decrypt failed.');
  74. }
  75. } catch (error) {
  76. console.error(`decrypt failed: errCode: ${error.code}, message: ${error.message}`);
  77. }
  78. }
  ```

  [ChaCha20Poly1305EncryptionDecryptionAsync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceChaCha20/entry/src/main/ets/pages/chacha20/ChaCha20Poly1305EncryptionDecryptionAsync.ets#L16-L97)
* 同步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. function generateRandom(len: number) {
  5. let rand = cryptoFramework.createRandom();
  6. let generateRandSync = rand.generateRandomSync(len);
  7. return generateRandSync;
  8. }

  10. function genPoly1305ParamsSpec() {
  11. let ivBlob = generateRandom(12); // 12 bytes
  12. let arr = [1, 2, 3, 4, 5, 6, 7, 8]; // 8 bytes
  13. let dataAad = new Uint8Array(arr);
  14. let aadBlob: cryptoFramework.DataBlob = { data: dataAad };
  15. arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; // 16 bytes
  16. let dataTag = new Uint8Array(arr);
  17. let tagBlob: cryptoFramework.DataBlob = {
  18. data: dataTag
  19. };
  20. // Poly1305的authTag在加密时从doFinal结果中获取，在解密时填入init函数的params参数中。
  21. let poly1305ParamsSpec: cryptoFramework.Poly1305ParamsSpec = {
  22. iv: ivBlob,
  23. aad: aadBlob,
  24. authTag: tagBlob,
  25. algName: 'Poly1305ParamsSpec'
  26. };
  27. return poly1305ParamsSpec;
  28. }

  30. let poly1305Params = genPoly1305ParamsSpec();

  32. // 加密消息。
  33. function encryptMessage(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  34. let cipher = cryptoFramework.createCipher('ChaCha20|Poly1305');
  35. cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, poly1305Params);
  36. let encryptUpdate = cipher.updateSync(plainText);
  37. // poly1305模式加密doFinal时传入空，获得tag数据，并更新至poly1305Params对象中。
  38. poly1305Params.authTag = cipher.doFinalSync(null);
  39. return encryptUpdate;
  40. }
  41. // 解密消息。
  42. function decryptMessage(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  43. let decoder = cryptoFramework.createCipher('ChaCha20|Poly1305');
  44. decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, poly1305Params);
  45. let decryptData = decoder.updateSync(cipherText);
  46. // poly1305模式解密doFinal时传入空，验证init时传入的tag数据，如果验证失败会抛出异常。
  47. let decryptData = decoder.doFinalSync(null);
  48. if (decryptData === null) {
  49. console.info('poly1305 decrypt result: success, decryptData is null.');
  50. }
  51. return decryptData;
  52. }
  53. function genSymKeyByData(symKeyData: Uint8Array) {
  54. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  55. let chacha20Generator = cryptoFramework.createSymKeyGenerator('ChaCha20');
  56. let symKey = chacha20Generator.convertKeySync(symKeyBlob);
  57. console.info('convertKeySync result: success.');
  58. return symKey;
  59. }
  60. function main() {
  61. try {
  62. let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159,
  63. 83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  64. let symKey = genSymKeyByData(keyData);
  65. let message = 'This is a test';
  66. let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  67. let encryptText = encryptMessage(symKey, plainText);
  68. let decryptText = decryptMessage(symKey, encryptText);
  69. if (plainText.data.toString() === decryptText.data.toString()) {
  70. console.info('decrypt ok.');
  71. console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
  72. } else {
  73. console.error('decrypt failed.');
  74. }
  75. } catch (error) {
  76. console.error(`decrypt failed: errCode: ${error.code}, message: ${error.message}`);
  77. }
  78. }
  ```

  [ChaCha20Poly1305EncryptionDecryptionSync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceChaCha20/entry/src/main/ets/pages/chacha20/ChaCha20Poly1305EncryptionDecryptionSync.ets#L16-L97)
