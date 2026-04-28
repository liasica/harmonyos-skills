---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-asym-encrypt-decrypt
title: 使用SM2非对称密钥加解密(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用SM2非对称密钥加解密(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:30+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:2f1c90bb0f063f60ff977c0c529ed8ac0f723e1984c1e10bf10ecb16c7722716
---

对应的算法规格请查看[非对称密钥加解密算法规格：SM2](crypto-asym-encrypt-decrypt-spec.md#sm2)。

**加密**

1. 调用[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)、[AsyKeyGenerator.generateKeyPair](../harmonyos-references/js-apis-cryptoframework.md#generatekeypair-1)，生成SM2密钥类型为SM2\_256的非对称密钥对（KeyPair）。KeyPair对象中包括公钥PubKey、私钥PriKey。

   如何生成SM2非对称密钥对，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：SM2](crypto-asym-key-generation-conversion-spec.md#sm2)和[随机生成非对称密钥对](crypto-generate-asym-key-pair-randomly.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'SM2\_256|SM3'，创建非对称密钥类型为SM2\_256、摘要算法为SM3的Cipher实例，用于完成加解密操作。
3. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为加密（cryptoFramework.CryptoMode.ENCRYPT\_MODE），指定加密密钥（KeyPair.PubKey），初始化加密Cipher实例。

   非对称密钥无加密参数，直接传入null。
4. 调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，传入明文，获取加密后的数据。

   doFinal输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。

**解密**

1. 由于SM2算法的Cipher实例不支持重复init操作，需要调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，重新生成Cipher实例。
2. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为解密（cryptoFramework.CryptoMode.DECRYPT\_MODE），指定解密密钥（KeyPair.PriKey）初始化解密Cipher实例。SM2无加密参数，直接传入null。
3. 调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，传入密文，获取解密后的数据。

* 异步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. // 加密消息
  5. async function encryptMessagePromise(publicKey: cryptoFramework.PubKey, plainText: cryptoFramework.DataBlob) {
  6. let cipher = cryptoFramework.createCipher('SM2_256|SM3');
  7. await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, publicKey, null);
  8. let encryptData = await cipher.doFinal(plainText);
  9. return encryptData;
  10. }

  12. // 解密消息
  13. async function decryptMessagePromise(privateKey: cryptoFramework.PriKey, cipherText: cryptoFramework.DataBlob) {
  14. let decoder = cryptoFramework.createCipher('SM2_256|SM3');
  15. await decoder.init(cryptoFramework.CryptoMode.DECRYPT_MODE, privateKey, null);
  16. let decryptData = await decoder.doFinal(cipherText);
  17. return decryptData;
  18. }

  20. // 生成SM2密钥对
  21. async function genKeyPairByData(pubKeyData: Uint8Array, priKeyData: Uint8Array) {
  22. let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyData };
  23. let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyData };
  24. let sm2Generator = cryptoFramework.createAsyKeyGenerator('SM2_256');
  25. let keyPair = await sm2Generator.convertKey(pubKeyBlob, priKeyBlob);
  26. console.info('convertKey result: success.');
  27. return keyPair;
  28. }

  30. async function main() {
  31. let pkData =
  32. new Uint8Array([48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 129, 28, 207, 85, 1, 130, 45, 3, 66, 0,
  33. 4, 90, 3, 58, 157, 190, 248, 76, 7, 132, 200, 151, 208, 112, 230, 96, 140, 90, 238, 211, 155, 128, 109, 248, 40,
  34. 83, 214, 78, 42, 104, 106, 55, 148, 249, 35, 61, 32, 221, 135, 143, 100, 45, 97, 194, 176, 52, 73, 136, 174, 40,
  35. 70, 70, 34, 103, 103, 161, 99, 27, 187, 13, 187, 109, 244, 13, 7]);
  36. let skData =
  37. new Uint8Array([48, 49, 2, 1, 1, 4, 32, 54, 41, 239, 240, 63, 188, 134, 113, 31, 102, 149, 203, 245, 89, 15, 15, 47,
  38. 202, 170, 60, 38, 154, 28, 169, 189, 100, 251, 76, 112, 223, 156, 159, 160, 10, 6, 8, 42, 129, 28, 207, 85, 1,
  39. 130, 45]);
  40. let keyPair = await genKeyPairByData(pkData, skData);
  41. let pubKey = keyPair.pubKey;
  42. let priKey = keyPair.priKey;
  43. let message = 'This is a test';
  44. // 把字符串按utf-8解码为Uint8Array
  45. let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  46. let encryptText = await encryptMessagePromise(pubKey, plainText);
  47. let decryptText = await decryptMessagePromise(priKey, encryptText);
  48. if (plainText.data.toString() === decryptText.data.toString()) {
  49. console.info('decrypt ok.');
  50. // 把Uint8Array按utf-8编码为字符串
  51. let messageDecrypted = buffer.from(decryptText.data).toString('utf-8');
  52. console.info('decrypted result string:' + messageDecrypted);
  53. } else {
  54. console.error('decrypt failed.');
  55. }
  56. }
  ```

  [SM2EncryptionDecryptionAsync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceSM2/entry/src/main/ets/pages/sm2/SM2EncryptionDecryptionAsync.ets#L16-L74)
* 同步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. // 加密消息
  5. function encryptMessage(publicKey: cryptoFramework.PubKey, plainText: cryptoFramework.DataBlob) {
  6. let cipher = cryptoFramework.createCipher('SM2_256|SM3');
  7. cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, publicKey, null);
  8. let encryptData = cipher.doFinalSync(plainText);
  9. return encryptData;
  10. }

  12. // 解密消息
  13. function decryptMessage(privateKey: cryptoFramework.PriKey, cipherText: cryptoFramework.DataBlob) {
  14. let decoder = cryptoFramework.createCipher('SM2_256|SM3');
  15. decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, privateKey, null);
  16. let decryptData = decoder.doFinalSync(cipherText);
  17. return decryptData;
  18. }

  20. // 生成SM2密钥对
  21. function genKeyPairByData(pubKeyData: Uint8Array, priKeyData: Uint8Array) {
  22. let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyData };
  23. let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyData };
  24. let sm2Generator = cryptoFramework.createAsyKeyGenerator('SM2_256');
  25. let keyPair = sm2Generator.convertKeySync(pubKeyBlob, priKeyBlob);
  26. console.info('convertKeySync result: success.');
  27. return keyPair;
  28. }

  30. function main() {
  31. let pkData =
  32. new Uint8Array([48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 129, 28, 207, 85, 1, 130, 45, 3, 66, 0,
  33. 4, 90, 3, 58, 157, 190, 248, 76, 7, 132, 200, 151, 208, 112, 230, 96, 140, 90, 238, 211, 155, 128, 109, 248, 40,
  34. 83, 214, 78, 42, 104, 106, 55, 148, 249, 35, 61, 32, 221, 135, 143, 100, 45, 97, 194, 176, 52, 73, 136, 174, 40,
  35. 70, 70, 34, 103, 103, 161, 99, 27, 187, 13, 187, 109, 244, 13, 7]);
  36. let skData =
  37. new Uint8Array([48, 49, 2, 1, 1, 4, 32, 54, 41, 239, 240, 63, 188, 134, 113, 31, 102, 149, 203, 245, 89, 15, 15, 47,
  38. 202, 170, 60, 38, 154, 28, 169, 189, 100, 251, 76, 112, 223, 156, 159, 160, 10, 6, 8, 42, 129, 28, 207, 85, 1,
  39. 130, 45]);
  40. let keyPair = genKeyPairByData(pkData, skData);
  41. let pubKey = keyPair.pubKey;
  42. let priKey = keyPair.priKey;
  43. let message = 'This is a test';
  44. // 把字符串按utf-8解码为Uint8Array
  45. let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  46. let encryptText = encryptMessage(pubKey, plainText);
  47. let decryptText = decryptMessage(priKey, encryptText);
  48. if (plainText.data.toString() === decryptText.data.toString()) {
  49. console.info('decrypt ok.');
  50. // 把Uint8Array按utf-8编码为字符串
  51. let messageDecrypted = buffer.from(decryptText.data).toString('utf-8');
  52. console.info('decrypted result string:' + messageDecrypted);
  53. } else {
  54. console.error('decrypt failed.');
  55. }
  56. }
  ```

  [SM2EncryptionDecryptionSync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceSM2/entry/src/main/ets/pages/sm2/SM2EncryptionDecryptionSync.ets#L16-L74)
