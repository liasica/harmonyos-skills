---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-3des-sym-encrypt-decrypt-ecb
title: 使用3DES对称密钥加解密(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用3DES对称密钥加解密(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cf0b6aa6c7c047c28309a00e1240646c724431c02a034430143d1aa8a9b7baaa
---

对应的算法规格请查看[对称密钥加解密算法规格：3DES](crypto-sym-encrypt-decrypt-spec.md#section3des)。

## 开发步骤

**加密**

1. 调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)和[SymKeyGenerator.convertKey](../harmonyos-references/js-apis-cryptoframework.md#convertkey-1)，生成密钥算法为3DES、密钥长度为192位的对称密钥（SymKey）。

   如何生成3DES对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：3DES](crypto-sym-key-generation-conversion-spec.md#section3des)和[指定二进制数据转换对称密钥](crypto-convert-binary-data-to-sym-key.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'3DES192|ECB|PKCS7'，创建对称密钥类型为3DES192、分组模式为ECB、填充模式为PKCS7的Cipher实例，用于完成加密操作。
3. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为加密（CryptoMode.ENCRYPT\_MODE），指定加密密钥（SymKey），初始化加密Cipher实例。

   ECB模式无加密参数，传入null。
4. 调用[Cipher.update](../harmonyos-references/js-apis-cryptoframework.md#update-1)，更新数据（明文）。

   * 当数据量较小时，可以在init完成后直接调用doFinal。
   * 当数据量较大时，可以多次调用update，即分段加解密。
   * 用户可以自行决定数据量大小。例如，数据量大于20字节时使用update。
5. 调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，获取加密后的数据。

   * 已使用update，data传入null。
   * doFinal输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。

**解密**

1. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'3DES192|ECB|PKCS7'，创建对称密钥类型为3DES192、分组模式为ECB、填充模式为PKCS7的Cipher实例，用于完成解密操作。
2. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为解密（CryptoMode.DECRYPT\_MODE），并指定解密密钥（SymKey）初始化解密Cipher实例。ECB模式无加密参数，调用时直接传入null。
3. 调用[Cipher.update](../harmonyos-references/js-apis-cryptoframework.md#update-1)，更新数据（密文）。
4. 调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，获取解密后的数据。

## 开发示例

当前示例以ECB分组模式为例，不需要设置加解密参数IV。

如果使用CBC、CTR、OFB、CFB分组模式，需设置加解密参数IV，请参考[设置加解密参数IV](crypto-3des-sym-encrypt-decrypt-ecb.md#设置加解密参数iv)，并确保在生成和初始化Cipher实例时正确设置相关参数。

* 异步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. // 加密消息
  5. async function encryptMessagePromise(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  6. let cipher = cryptoFramework.createCipher('3DES192|ECB|PKCS7');
  7. await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, null);
  8. let encryptData = await cipher.doFinal(plainText);
  9. return encryptData;
  10. }

  12. // 解密消息
  13. async function decryptMessagePromise(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  14. let decoder = cryptoFramework.createCipher('3DES192|ECB|PKCS7');
  15. await decoder.init(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, null);
  16. let decryptData = await decoder.doFinal(cipherText);
  17. return decryptData;
  18. }

  20. async function genSymKeyByData(symKeyData: Uint8Array) {
  21. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  22. let symGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
  23. let symKey = await symGenerator.convertKey(symKeyBlob);
  24. console.info('convertKey result: success.');
  25. return symKey;
  26. }

  28. async function main() {
  29. let keyData =
  30. new Uint8Array([238, 249, 61, 55, 128, 220, 183, 224, 139, 253, 248, 239, 239, 41, 71, 25, 235, 206, 230, 162, 249,
  31. 27, 234, 114]);
  32. let symKey = await genSymKeyByData(keyData);
  33. let message = 'This is a test';
  34. let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  35. let encryptText = await encryptMessagePromise(symKey, plainText);
  36. let decryptText = await decryptMessagePromise(symKey, encryptText);
  37. if (plainText.data.toString() === decryptText.data.toString()) {
  38. console.info('decrypt ok');
  39. console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
  40. } else {
  41. console.error('decrypt failed');
  42. }
  43. }
  ```

  [3des\_ecb\_encryption\_decryption\_asynchronous.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidance3DES/entry/src/main/ets/pages/3des_ecb_encryption_decryption_asynchronous.ets#L16-L60)
* 同步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. // 加密消息
  5. function encryptMessage(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  6. let cipher = cryptoFramework.createCipher('3DES192|ECB|PKCS7');
  7. cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, null);
  8. let encryptData = cipher.doFinalSync(plainText);
  9. return encryptData;
  10. }

  12. // 解密消息
  13. function decryptMessage(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  14. let decoder = cryptoFramework.createCipher('3DES192|ECB|PKCS7');
  15. decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, null);
  16. let decryptData = decoder.doFinalSync(cipherText);
  17. return decryptData;
  18. }

  20. function genSymKeyByData(symKeyData: Uint8Array) {
  21. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  22. let symGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
  23. let symKey = symGenerator.convertKeySync(symKeyBlob);
  24. console.info('convertKeySync result: success.');
  25. return symKey;
  26. }

  28. function main() {
  29. let keyData =
  30. new Uint8Array([238, 249, 61, 55, 128, 220, 183, 224, 139, 253, 248, 239, 239, 41, 71, 25, 235, 206, 230, 162, 249,
  31. 27, 234, 114]);
  32. let symKey = genSymKeyByData(keyData);
  33. let message = 'This is a test';
  34. let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  35. let encryptText = encryptMessage(symKey, plainText);
  36. let decryptText = decryptMessage(symKey, encryptText);
  37. if (plainText.data.toString() === decryptText.data.toString()) {
  38. console.info('decrypt ok');
  39. console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
  40. } else {
  41. console.error('decrypt failed');
  42. }
  43. }
  ```

  [3des\_ecb\_encryption\_decryption\_synchronous.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidance3DES/entry/src/main/ets/pages/3des_ecb_encryption_decryption_synchronous.ets#L16-L60)

### 设置加解密参数IV

下述示例为CBC分组模式，需要设置加解密参数IV。

如果分组模式为CBC、CTR、OFB、CFB，需要参考如下设置加解密参数IV。ECB不需要设置加解密参数IV。

```
1. function genIvParamsSpec() {
2. let ivBlob = generateRandom(8); //3DES的 CBC、CFB、OFB、CTR的iv长度为8字节。
3. let ivParamsSpec: cryptoFramework.IvParamsSpec = {
4. algName: "IvParamsSpec",
5. iv: ivBlob
6. };
7. return ivParamsSpec;
8. }
9. let iv = genIvParamsSpec();
10. let cipher = cryptoFramework.createCipher('3DES192|CBC|PKCS7');
11. cipher.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, iv);
12. // 本段代码只展示CBC、CTR、OFB、CFB分段模式的不同，其他流程请参考开发示例。
```
