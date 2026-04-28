---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-pkcs1
title: 使用RSA非对称密钥（PKCS1模式）加解密(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用RSA非对称密钥（PKCS1模式）加解密(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:29+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:e2998151d25a6c1bb7e2007c750432106019a454cf3af690b66e9a8c27ac2433
---

对应的算法规格请查看[非对称密钥加解密算法规格：RSA](crypto-asym-encrypt-decrypt-spec.md#rsa)。

**加密**

1. 调用[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)、[AsyKeyGenerator.generateKeyPair](../harmonyos-references/js-apis-cryptoframework.md#generatekeypair-1)，生成RSA密钥类型为RSA1024、素数个数为2的非对称密钥对（KeyPair）。KeyPair对象中包括公钥PubKey、私钥PriKey。

   如何生成RSA非对称密钥对，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：RSA](crypto-asym-key-generation-conversion-spec.md#rsa)和[随机生成非对称密钥对](crypto-generate-asym-key-pair-randomly.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'RSA1024|PKCS1'，创建非对称密钥类型为RSA1024、填充模式为PKCS1的Cipher实例，用于完成加解密操作。
3. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为加密（cryptoFramework.CryptoMode.ENCRYPT\_MODE），指定加密密钥（KeyPair.PubKey），初始化加密Cipher实例。

   非对称密钥无加密参数，直接传入null。
4. 调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，传入明文，获取加密后的数据。

   * doFinal输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。
   * 当数据量较大时，可以多次调用doFinal，即[分段加解密](crypto-rsa-asym-encrypt-decrypt-by-segment.md)。

**解密**

1. 由于RSA算法的Cipher实例不支持重复init操作，需要调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，重新生成Cipher实例。
2. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为解密（cryptoFramework.CryptoMode.DECRYPT\_MODE），指定解密密钥（KeyPair.PriKey）初始化解密Cipher实例。PKCS1模式无加密参数，直接传入null。
3. 调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，传入密文，获取解密后的数据。

* 异步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. // 加密消息
  5. async function encryptMessagePromise(publicKey: cryptoFramework.PubKey, plainText: cryptoFramework.DataBlob) {
  6. let cipher = cryptoFramework.createCipher('RSA1024|PKCS1');
  7. await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, publicKey, null);
  8. let encryptData = await cipher.doFinal(plainText);
  9. return encryptData;
  10. }

  12. // 解密消息
  13. async function decryptMessagePromise(privateKey: cryptoFramework.PriKey, cipherText: cryptoFramework.DataBlob) {
  14. let decoder = cryptoFramework.createCipher('RSA1024|PKCS1');
  15. await decoder.init(cryptoFramework.CryptoMode.DECRYPT_MODE, privateKey, null);
  16. let decryptData = await decoder.doFinal(cipherText);
  17. return decryptData;
  18. }

  20. // 生成RSA密钥对
  21. async function genKeyPairByData(pubKeyData: Uint8Array, priKeyData: Uint8Array) {
  22. let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyData };
  23. let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyData };
  24. let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  25. let keyPair = await rsaGenerator.convertKey(pubKeyBlob, priKeyBlob);
  26. console.info('convertKey result: success.');
  27. return keyPair;
  28. }

  30. async function main() {
  31. let pkData =
  32. new Uint8Array([48, 129, 159, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 3, 129, 141, 0, 48, 129, 137,
  33. 2, 129, 129, 0, 197, 64, 10, 198, 14, 110, 65, 92, 206, 35, 28, 123, 153, 24, 134, 255, 145, 74, 42, 173, 40, 215,
  34. 146, 58, 143, 46, 10, 195, 154, 160, 69, 196, 220, 152, 179, 44, 111, 200, 84, 78, 215, 73, 210, 181, 12, 29, 70,
  35. 68, 36, 135, 153, 89, 230, 202, 130, 212, 111, 243, 234, 92, 131, 62, 145, 50, 73, 48, 104, 245, 46, 70, 45, 157,
  36. 147, 143, 140, 162, 156, 216, 220, 49, 121, 142, 194, 33, 223, 201, 0, 16, 163, 210, 240, 118, 92, 147, 121, 220,
  37. 17, 114, 24, 52, 125, 135, 176, 88, 21, 83, 86, 17, 156, 88, 250, 48, 79, 86, 128, 248, 105, 208, 133, 140, 13,
  38. 153, 164, 191, 136, 164, 44, 53, 2, 3, 1, 0, 1]);
  39. let skData =
  40. new Uint8Array([48, 130, 2, 119, 2, 1, 0, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 4, 130, 2, 97, 48,
  41. 130, 2, 93, 2, 1, 0, 2, 129, 129, 0, 197, 64, 10, 198, 14, 110, 65, 92, 206, 35, 28, 123, 153, 24, 134, 255, 145,
  42. 74, 42, 173, 40, 215, 146, 58, 143, 46, 10, 195, 154, 160, 69, 196, 220, 152, 179, 44, 111, 200, 84, 78, 215, 73,
  43. 210, 181, 12, 29, 70, 68, 36, 135, 153, 89, 230, 202, 130, 212, 111, 243, 234, 92, 131, 62, 145, 50, 73, 48, 104,
  44. 245, 46, 70, 45, 157, 147, 143, 140, 162, 156, 216, 220, 49, 121, 142, 194, 33, 223, 201, 0, 16, 163, 210, 240,
  45. 118, 92, 147, 121, 220, 17, 114, 24, 52, 125, 135, 176, 88, 21, 83, 86, 17, 156, 88, 250, 48, 79, 86, 128, 248,
  46. 105, 208, 133, 140, 13, 153, 164, 191, 136, 164, 44, 53, 2, 3, 1, 0, 1, 2, 129, 128, 70, 75, 184, 139, 53, 1, 94,
  47. 17, 240, 244, 218, 101, 193, 253, 215, 190, 164, 204, 197, 192, 200, 89, 107, 39, 171, 119, 65, 38, 204, 168, 105,
  48. 180, 234, 217, 16, 161, 185, 132, 175, 103, 25, 154, 153, 153, 36, 36, 26, 178, 150, 66, 45, 8, 185, 19, 90, 228,
  49. 210, 177, 30, 200, 177, 141, 78, 184, 248, 59, 113, 154, 145, 73, 160, 24, 73, 157, 86, 207, 186, 32, 95, 200,
  50. 106, 252, 107, 69, 170, 193, 216, 196, 181, 142, 74, 203, 15, 18, 89, 228, 152, 19, 239, 21, 233, 98, 121, 214,
  51. 57, 187, 111, 239, 223, 248, 199, 70, 223, 108, 108, 113, 234, 144, 155, 95, 246, 144, 244, 122, 39, 55, 127, 81,
  52. 2, 65, 0, 246, 96, 188, 0, 0, 104, 221, 105, 139, 144, 63, 175, 209, 87, 179, 162, 88, 192, 99, 82, 125, 53, 54,
  53. 48, 70, 245, 239, 37, 15, 242, 247, 84, 115, 187, 196, 95, 156, 40, 165, 60, 64, 102, 13, 229, 243, 2, 149, 0,
  54. 232, 226, 221, 192, 95, 11, 12, 208, 5, 181, 98, 62, 210, 190, 141, 235, 2, 65, 0, 204, 244, 34, 10, 105, 80, 76,
  55. 116, 163, 35, 231, 168, 187, 206, 189, 101, 215, 103, 80, 115, 86, 11, 34, 127, 203, 114, 84, 188, 121, 174, 169,
  56. 31, 142, 2, 182, 27, 140, 225, 157, 227, 71, 98, 15, 203, 187, 213, 5, 190, 20, 121, 8, 30, 193, 100, 232, 101,
  57. 141, 8, 124, 20, 29, 78, 6, 95, 2, 65, 0, 204, 43, 225, 224, 6, 118, 224, 117, 100, 200, 199, 94, 70, 23, 109,
  58. 175, 173, 232, 208, 230, 61, 8, 105, 189, 156, 48, 150, 91, 154, 89, 248, 136, 173, 215, 254, 166, 84, 220, 130,
  59. 1, 234, 68, 40, 100, 84, 251, 224, 202, 254, 51, 115, 28, 198, 38, 124, 25, 175, 129, 94, 199, 61, 17, 216, 189,
  60. 2, 64, 72, 230, 129, 129, 48, 138, 134, 87, 106, 123, 231, 247, 165, 173, 216, 194, 115, 198, 228, 223, 209, 120,
  61. 46, 114, 68, 92, 75, 117, 170, 214, 140, 131, 147, 208, 181, 19, 193, 157, 178, 186, 87, 246, 178, 101, 166, 79,
  62. 20, 54, 211, 51, 101, 199, 2, 197, 48, 192, 134, 84, 193, 69, 170, 82, 201, 131, 2, 65, 0, 213, 165, 55, 166, 131,
  63. 210, 195, 56, 250, 147, 195, 61, 205, 208, 189, 185, 40, 52, 50, 119, 137, 23, 246, 46, 220, 108, 52, 23, 152,
  64. 154, 94, 32, 144, 195, 184, 249, 21, 168, 12, 57, 222, 18, 60, 117, 81, 157, 72, 30, 155, 190, 165, 242, 228, 139,
  65. 240, 184, 145, 170, 103, 210, 160, 161, 135, 13]);
  66. let keyPair = await genKeyPairByData(pkData, skData);
  67. let pubKey = keyPair.pubKey;
  68. let priKey = keyPair.priKey;
  69. let message = 'This is a test';
  70. // 把字符串按utf-8解码为Uint8Array
  71. let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  72. let encryptText = await encryptMessagePromise(pubKey, plainText);
  73. let decryptText = await decryptMessagePromise(priKey, encryptText);
  74. if (plainText.data.toString() === decryptText.data.toString()) {
  75. console.info('decrypt ok.');
  76. // 把Uint8Array按utf-8编码为字符串
  77. let messageDecrypted = buffer.from(decryptText.data).toString('utf-8');
  78. console.info('decrypted result string:' + messageDecrypted);
  79. } else {
  80. console.error('decrypt failed.');
  81. }
  82. }
  ```

  [RSAPKCS1Async.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceRSA/entry/src/main/ets/pages/rsa_pkcs1/RSAPKCS1Async.ets#L16-L100)
* 同步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. // 加密消息
  5. function encryptMessage(publicKey: cryptoFramework.PubKey, plainText: cryptoFramework.DataBlob) {
  6. let cipher = cryptoFramework.createCipher('RSA1024|PKCS1');
  7. cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, publicKey, null);
  8. let encryptData = cipher.doFinalSync(plainText);
  9. return encryptData;
  10. }

  12. // 解密消息
  13. function decryptMessage(privateKey: cryptoFramework.PriKey, cipherText: cryptoFramework.DataBlob) {
  14. let decoder = cryptoFramework.createCipher('RSA1024|PKCS1');
  15. decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, privateKey, null);
  16. let decryptData = decoder.doFinalSync(cipherText);
  17. return decryptData;
  18. }

  20. // 生成RSA密钥对
  21. function genKeyPairByData(pubKeyData: Uint8Array, priKeyData: Uint8Array) {
  22. let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyData };
  23. let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyData };
  24. let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  25. let keyPair = rsaGenerator.convertKeySync(pubKeyBlob, priKeyBlob);
  26. console.info('convertKeySync result: success.');
  27. return keyPair;
  28. }

  30. function main() {
  31. let pkData =
  32. new Uint8Array([48, 129, 159, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 3, 129, 141, 0, 48, 129, 137,
  33. 2, 129, 129, 0, 197, 64, 10, 198, 14, 110, 65, 92, 206, 35, 28, 123, 153, 24, 134, 255, 145, 74, 42, 173, 40, 215,
  34. 146, 58, 143, 46, 10, 195, 154, 160, 69, 196, 220, 152, 179, 44, 111, 200, 84, 78, 215, 73, 210, 181, 12, 29, 70,
  35. 68, 36, 135, 153, 89, 230, 202, 130, 212, 111, 243, 234, 92, 131, 62, 145, 50, 73, 48, 104, 245, 46, 70, 45, 157,
  36. 147, 143, 140, 162, 156, 216, 220, 49, 121, 142, 194, 33, 223, 201, 0, 16, 163, 210, 240, 118, 92, 147, 121, 220,
  37. 17, 114, 24, 52, 125, 135, 176, 88, 21, 83, 86, 17, 156, 88, 250, 48, 79, 86, 128, 248, 105, 208, 133, 140, 13,
  38. 153, 164, 191, 136, 164, 44, 53, 2, 3, 1, 0, 1]);
  39. let skData =
  40. new Uint8Array([48, 130, 2, 119, 2, 1, 0, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 4, 130, 2, 97, 48,
  41. 130, 2, 93, 2, 1, 0, 2, 129, 129, 0, 197, 64, 10, 198, 14, 110, 65, 92, 206, 35, 28, 123, 153, 24, 134, 255, 145,
  42. 74, 42, 173, 40, 215, 146, 58, 143, 46, 10, 195, 154, 160, 69, 196, 220, 152, 179, 44, 111, 200, 84, 78, 215, 73,
  43. 210, 181, 12, 29, 70, 68, 36, 135, 153, 89, 230, 202, 130, 212, 111, 243, 234, 92, 131, 62, 145, 50, 73, 48, 104,
  44. 245, 46, 70, 45, 157, 147, 143, 140, 162, 156, 216, 220, 49, 121, 142, 194, 33, 223, 201, 0, 16, 163, 210, 240,
  45. 118, 92, 147, 121, 220, 17, 114, 24, 52, 125, 135, 176, 88, 21, 83, 86, 17, 156, 88, 250, 48, 79, 86, 128, 248,
  46. 105, 208, 133, 140, 13, 153, 164, 191, 136, 164, 44, 53, 2, 3, 1, 0, 1, 2, 129, 128, 70, 75, 184, 139, 53, 1, 94,
  47. 17, 240, 244, 218, 101, 193, 253, 215, 190, 164, 204, 197, 192, 200, 89, 107, 39, 171, 119, 65, 38, 204, 168, 105,
  48. 180, 234, 217, 16, 161, 185, 132, 175, 103, 25, 154, 153, 153, 36, 36, 26, 178, 150, 66, 45, 8, 185, 19, 90, 228,
  49. 210, 177, 30, 200, 177, 141, 78, 184, 248, 59, 113, 154, 145, 73, 160, 24, 73, 157, 86, 207, 186, 32, 95, 200,
  50. 106, 252, 107, 69, 170, 193, 216, 196, 181, 142, 74, 203, 15, 18, 89, 228, 152, 19, 239, 21, 233, 98, 121, 214,
  51. 57, 187, 111, 239, 223, 248, 199, 70, 223, 108, 108, 113, 234, 144, 155, 95, 246, 144, 244, 122, 39, 55, 127, 81,
  52. 2, 65, 0, 246, 96, 188, 0, 0, 104, 221, 105, 139, 144, 63, 175, 209, 87, 179, 162, 88, 192, 99, 82, 125, 53, 54,
  53. 48, 70, 245, 239, 37, 15, 242, 247, 84, 115, 187, 196, 95, 156, 40, 165, 60, 64, 102, 13, 229, 243, 2, 149, 0,
  54. 232, 226, 221, 192, 95, 11, 12, 208, 5, 181, 98, 62, 210, 190, 141, 235, 2, 65, 0, 204, 244, 34, 10, 105, 80, 76,
  55. 116, 163, 35, 231, 168, 187, 206, 189, 101, 215, 103, 80, 115, 86, 11, 34, 127, 203, 114, 84, 188, 121, 174, 169,
  56. 31, 142, 2, 182, 27, 140, 225, 157, 227, 71, 98, 15, 203, 187, 213, 5, 190, 20, 121, 8, 30, 193, 100, 232, 101,
  57. 141, 8, 124, 20, 29, 78, 6, 95, 2, 65, 0, 204, 43, 225, 224, 6, 118, 224, 117, 100, 200, 199, 94, 70, 23, 109,
  58. 175, 173, 232, 208, 230, 61, 8, 105, 189, 156, 48, 150, 91, 154, 89, 248, 136, 173, 215, 254, 166, 84, 220, 130,
  59. 1, 234, 68, 40, 100, 84, 251, 224, 202, 254, 51, 115, 28, 198, 38, 124, 25, 175, 129, 94, 199, 61, 17, 216, 189,
  60. 2, 64, 72, 230, 129, 129, 48, 138, 134, 87, 106, 123, 231, 247, 165, 173, 216, 194, 115, 198, 228, 223, 209, 120,
  61. 46, 114, 68, 92, 75, 117, 170, 214, 140, 131, 147, 208, 181, 19, 193, 157, 178, 186, 87, 246, 178, 101, 166, 79,
  62. 20, 54, 211, 51, 101, 199, 2, 197, 48, 192, 134, 84, 193, 69, 170, 82, 201, 131, 2, 65, 0, 213, 165, 55, 166, 131,
  63. 210, 195, 56, 250, 147, 195, 61, 205, 208, 189, 185, 40, 52, 50, 119, 137, 23, 246, 46, 220, 108, 52, 23, 152,
  64. 154, 94, 32, 144, 195, 184, 249, 21, 168, 12, 57, 222, 18, 60, 117, 81, 157, 72, 30, 155, 190, 165, 242, 228, 139,
  65. 240, 184, 145, 170, 103, 210, 160, 161, 135, 13]);
  66. let keyPair = genKeyPairByData(pkData, skData);
  67. let pubKey = keyPair.pubKey;
  68. let priKey = keyPair.priKey;
  69. let message = 'This is a test';
  70. // 把字符串按utf-8解码为Uint8Array
  71. let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  72. let encryptText = encryptMessage(pubKey, plainText);
  73. let decryptText = decryptMessage(priKey, encryptText);
  74. if (plainText.data.toString() === decryptText.data.toString()) {
  75. console.info('decrypt ok.');
  76. // 把Uint8Array按utf-8编码为字符串
  77. let messageDecrypted = buffer.from(decryptText.data).toString('utf-8');
  78. console.info('decrypted result string:' + messageDecrypted);
  79. } else {
  80. console.error('decrypt failed.');
  81. }
  82. }
  ```

  [RSAPKCS1Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceRSA/entry/src/main/ets/pages/rsa_pkcs1/RSAPKCS1Sync.ets#L16-L100)
