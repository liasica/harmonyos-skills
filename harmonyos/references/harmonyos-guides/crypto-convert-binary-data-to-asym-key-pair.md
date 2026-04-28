---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-convert-binary-data-to-asym-key-pair
title: 指定二进制数据转换非对称密钥对(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥生成和转换 > 密钥生成和转换开发指导 > 指定二进制数据转换非对称密钥对(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3eb55c4f5172dbe72682e184e16dd5454acdbfc52c14c875d98acbf2c2b00452
---

以RSA、ECC、SM2为例，根据指定的非对称密钥二进制数据，生成非对称密钥对（KeyPair），即将外部或存储的二进制数据转换为算法库的密钥对象，该对象可用于后续的加解密等操作。

说明

针对非对称密钥的convertKey操作：

* 公钥需满足：ASN.1语法、X.509规范、DER编码格式。
* 私钥需满足：ASN.1语法、PKCS#8规范、DER编码格式。

## 指定二进制数据转换RSA密钥对

对应的算法规格请查看[非对称密钥生成和转换规格：RSA](crypto-asym-key-generation-conversion-spec.md#rsa)。

1. 获取RSA公钥或私钥二进制数据，封装成[DataBlob](../harmonyos-references/js-apis-cryptoframework.md#datablob)对象。

   公钥和私钥可单独传入，此处示例传入公钥。
2. 调用[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)，指定字符串参数'RSA1024'，创建RSA密钥类型为RSA1024、素数个数为2的非对称密钥生成器（AsyKeyGenerator）。

   生成RSA非对称密钥时，默认素数为2，此处省略了参数PRIMES\_2。
3. 调用[AsyKeyGenerator.convertKey](../harmonyos-references/js-apis-cryptoframework.md#convertkey-3)，传入二进制密钥数据，生成非对称密钥对象（KeyPair）。即将外部或存储的二进制数据转换为算法库的密钥对象，该对象可用于后续的加解密等操作。

* 以使用callback方式生成RSA密钥对为例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. function convertAsyKey() {
  4. let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  5. let pkVal =
  6. new Uint8Array([48, 129, 159, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 3, 129, 141, 0, 48, 129, 137,
  7. 2, 129, 129, 0, 174, 203, 113, 83, 113, 3, 143, 213, 194, 79, 91, 9, 51, 142, 87, 45, 97, 65, 136, 24, 166, 35, 5,
  8. 179, 42, 47, 212, 79, 111, 74, 134, 120, 73, 67, 21, 19, 235, 80, 46, 152, 209, 133, 232, 87, 192, 140, 18, 206,
  9. 27, 106, 106, 169, 106, 46, 135, 111, 118, 32, 129, 27, 89, 255, 183, 116, 247, 38, 12, 7, 238, 77, 151, 167, 6,
  10. 102, 153, 126, 66, 28, 253, 253, 216, 64, 20, 138, 117, 72, 15, 216, 178, 37, 208, 179, 63, 204, 39, 94, 244, 170,
  11. 48, 190, 21, 11, 73, 169, 156, 104, 193, 3, 17, 100, 28, 60, 50, 92, 235, 218, 57, 73, 119, 19, 101, 164, 192,
  12. 161, 197, 106, 105, 73, 2, 3, 1, 0, 1]);
  13. let pkBlob: cryptoFramework.DataBlob = { data: pkVal };
  14. rsaGenerator.convertKey(pkBlob, null, (err, keyPair) => {
  15. if (err) {
  16. console.error(`convertKey failed: errCode: ${err.code}, message: ${err.message}`);
  17. return;
  18. }
  19. console.info('convertKey result: success.');
  20. });
  21. }
  ```

  [Callback.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/BinaryDataConvertAsymmetricKeyPairArkTS/entry/src/main/ets/pages/rsa/Callback.ets#L16-L38)
* 同步返回结果（调用方法[convertKeySync](../harmonyos-references/js-apis-cryptoframework.md#convertkeysync12)）：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. function convertAsyKeySync() {
  4. let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  5. let pkVal =
  6. new Uint8Array([48, 129, 159, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 3, 129, 141, 0, 48, 129, 137,
  7. 2, 129, 129, 0, 174, 203, 113, 83, 113, 3, 143, 213, 194, 79, 91, 9, 51, 142, 87, 45, 97, 65, 136, 24, 166, 35, 5,
  8. 179, 42, 47, 212, 79, 111, 74, 134, 120, 73, 67, 21, 19, 235, 80, 46, 152, 209, 133, 232, 87, 192, 140, 18, 206,
  9. 27, 106, 106, 169, 106, 46, 135, 111, 118, 32, 129, 27, 89, 255, 183, 116, 247, 38, 12, 7, 238, 77, 151, 167, 6,
  10. 102, 153, 126, 66, 28, 253, 253, 216, 64, 20, 138, 117, 72, 15, 216, 178, 37, 208, 179, 63, 204, 39, 94, 244, 170,
  11. 48, 190, 21, 11, 73, 169, 156, 104, 193, 3, 17, 100, 28, 60, 50, 92, 235, 218, 57, 73, 119, 19, 101, 164, 192,
  12. 161, 197, 106, 105, 73, 2, 3, 1, 0, 1]);
  13. let pkBlob: cryptoFramework.DataBlob = { data: pkVal };
  14. try {
  15. let keyPair = rsaGenerator.convertKeySync(pkBlob, null);
  16. if (keyPair != null) {
  17. console.info('convertKeySync result: success.');
  18. }
  19. } catch (e) {
  20. console.error(`get key pair failed: errCode: ${e.code}, message: ${e.message}`);
  21. }
  22. }
  ```

  [Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/BinaryDataConvertAsymmetricKeyPairArkTS/entry/src/main/ets/pages/rsa/Sync.ets#L16-L39)

## 指定二进制数据转换ECC密钥对

查看[非对称密钥生成和转换规格：ECC](crypto-asym-key-generation-conversion-spec.md#ecc)。

1. 获取ECC公钥或私钥二进制数据，封装成[DataBlob](../harmonyos-references/js-apis-cryptoframework.md#datablob)对象。

   公钥和私钥可以只传入其中一个，此处示例以传入公钥和私钥为例。
2. 调用[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)，指定字符串参数'ECC256'，创建密钥算法为ECC、密钥长度为256位的非对称密钥生成器（AsyKeyGenerator）。
3. 调用[AsyKeyGenerator.convertKey](../harmonyos-references/js-apis-cryptoframework.md#convertkey-3)，传入公钥二进制和私钥二进制，生成非对称密钥对象（KeyPair）。

* 使用callback方式生成ECC密钥对：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. function convertEccAsyKey() {
  4. let pubKeyArray =
  5. new Uint8Array([48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7, 3, 66, 0, 4,
  6. 83, 96, 142, 9, 86, 214, 126, 106, 247, 233, 92, 125, 4, 128, 138, 105, 246, 162, 215, 71, 81, 58, 202, 121, 26,
  7. 105, 211, 55, 130, 45, 236, 143, 55, 16, 248, 75, 167, 160, 167, 106, 2, 152, 243, 44, 68, 66, 0, 167, 99, 92,
  8. 235, 215, 159, 239, 28, 106, 124, 171, 34, 145, 124, 174, 57, 92]);
  9. let priKeyArray =
  10. new Uint8Array([48, 49, 2, 1, 1, 4, 32, 115, 56, 137, 35, 207, 0, 60, 191, 90, 61, 136, 105, 210, 16, 27, 4, 171,
  11. 57, 10, 61, 123, 40, 189, 28, 34, 207, 236, 22, 45, 223, 10, 189, 160, 10, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7]);
  12. let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyArray };
  13. let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyArray };
  14. let generator = cryptoFramework.createAsyKeyGenerator('ECC256');
  15. generator.convertKey(pubKeyBlob, priKeyBlob, (error, data) => {
  16. if (error) {
  17. console.error(`convertKey failed: errCode: ${error.code}, message: ${error.message}`);
  18. return;
  19. }
  20. console.info('convertKey result: success.');
  21. });
  22. }
  ```

  [Callback.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/BinaryDataConvertAsymmetricKeyPairArkTS/entry/src/main/ets/pages/ecc/Callback.ets#L16-L39)
* 同步返回结果（调用[convertKeySync](../harmonyos-references/js-apis-cryptoframework.md#convertkeysync12)）：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. function convertECCAsyKeySync() {
  4. let pubKeyArray =
  5. new Uint8Array([48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7, 3, 66, 0, 4,
  6. 83, 96, 142, 9, 86, 214, 126, 106, 247, 233, 92, 125, 4, 128, 138, 105, 246, 162, 215, 71, 81, 58, 202, 121, 26,
  7. 105, 211, 55, 130, 45, 236, 143, 55, 16, 248, 75, 167, 160, 167, 106, 2, 152, 243, 44, 68, 66, 0, 167, 99, 92,
  8. 235, 215, 159, 239, 28, 106, 124, 171, 34, 145, 124, 174, 57, 92]);
  9. let priKeyArray =
  10. new Uint8Array([48, 49, 2, 1, 1, 4, 32, 115, 56, 137, 35, 207, 0, 60, 191, 90, 61, 136, 105, 210, 16, 27, 4, 171,
  11. 57, 10, 61, 123, 40, 189, 28, 34, 207, 236, 22, 45, 223, 10, 189, 160, 10, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7]);
  12. let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyArray };
  13. let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyArray };
  14. let generator = cryptoFramework.createAsyKeyGenerator('ECC256');
  15. try {
  16. let keyPair = generator.convertKeySync(pubKeyBlob, priKeyBlob);
  17. if (keyPair != null) {
  18. console.info('convertKeySync result: success.');
  19. }
  20. } catch (e) {
  21. console.error(`get key pair failed: errCode: ${e.code}, message: ${e.message}`);
  22. }
  23. }
  ```

  [Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/BinaryDataConvertAsymmetricKeyPairArkTS/entry/src/main/ets/pages/ecc/Sync.ets#L16-L40)

## 指定PKCS8二进制数据转换ECC私钥

查看[非对称密钥生成和转换规格：ECC](crypto-asym-key-generation-conversion-spec.md#ecc)。

获取ECC公钥或私钥二进制数据，封装成[DataBlob](../harmonyos-references/js-apis-cryptoframework.md#datablob)对象再转为ECC密钥格式。示例如下：

1. 调用[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)，指定字符串参数'ECC256'，创建密钥算法为ECC、密钥长度为256位的非对称密钥生成器（AsyKeyGenerator）。
2. 调用[PubKey.getEncoded](../harmonyos-references/js-apis-cryptoframework.md#getencoded)获取公钥数据字节流，调用[PriKey.getEncodedDer](../harmonyos-references/js-apis-cryptoframework.md#getencodedder12-1) 并设置参数为'PKCS8'，获取私钥数据的字节流。由此分别获取密钥对象的二进制数据。
3. 调用[AsyKeyGenerator.convertKey](../harmonyos-references/js-apis-cryptoframework.md#convertkey-3)，将生成的二进制密钥数据转为非对称密钥对象（KeyPair）。

```
1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

3. async function main() {
4. // 创建一个AsyKeyGenerator实例
5. let eccGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
6. // 使用密钥生成器随机生成非对称密钥对
7. let keyGenPromise = eccGenerator.generateKeyPair();
8. keyGenPromise.then(keyPair => {
9. let pubKey = keyPair.pubKey;
10. let priKey = keyPair.priKey;
11. // 获取非对称密钥对ECC的二进制数据
12. let pubBlob = pubKey.getEncoded();
13. let skBlob = priKey.getEncodedDer('PKCS8');
14. let generator = cryptoFramework.createAsyKeyGenerator('ECC256');
15. generator.convertKey(pubBlob, skBlob, (error, data) => {
16. if (error) {
17. console.error(`convertKey failed: errCode: ${error.code}, message: ${error.message}`);
18. return;
19. }
20. console.info('convertKey result: success.');
21. });
22. });
23. }
```

[PKCS8ECC.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/BinaryDataConvertAsymmetricKeyPairArkTS/entry/src/main/ets/pages/pkcs8ecc/PKCS8ECC.ets#L16-L40)

## 指定二进制数据转换SM2密钥对

查看[非对称密钥生成和转换规格：SM2](crypto-asym-key-generation-conversion-spec.md#sm2)。

1. 获取SM2公钥或私钥的二进制数据，封装成[DataBlob](../harmonyos-references/js-apis-cryptoframework.md#datablob)对象。

   公钥和私钥可以只传入其中一个，示例以传入公钥和私钥为例。
2. 调用[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)，指定字符串参数'SM2\_256'，创建密钥算法为SM2、密钥长度为256位的非对称密钥生成器（AsyKeyGenerator）。
3. 调用[AsyKeyGenerator.convertKey](../harmonyos-references/js-apis-cryptoframework.md#convertkey-3)，传入公钥和私钥的二进制数据，生成非对称密钥对象（KeyPair）。

* 以使用callback方式生成SM2密钥对为例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. function convertSM2AsyKey() {
  4. let pubKeyArray =
  5. new Uint8Array([48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 129, 28, 207, 85, 1, 130, 45, 3, 66, 0,
  6. 4, 90, 3, 58, 157, 190, 248, 76, 7, 132, 200, 151, 208, 112, 230, 96, 140, 90, 238, 211, 155, 128, 109, 248, 40,
  7. 83, 214, 78, 42, 104, 106, 55, 148, 249, 35, 61, 32, 221, 135, 143, 100, 45, 97, 194, 176, 52, 73, 136, 174, 40,
  8. 70, 70, 34, 103, 103, 161, 99, 27, 187, 13, 187, 109, 244, 13, 7]);
  9. let priKeyArray =
  10. new Uint8Array([48, 49, 2, 1, 1, 4, 32, 54, 41, 239, 240, 63, 188, 134, 113, 31, 102, 149, 203, 245, 89, 15, 15, 47,
  11. 202, 170, 60, 38, 154, 28, 169, 189, 100, 251, 76, 112, 223, 156, 159, 160, 10, 6, 8, 42, 129, 28, 207, 85, 1,
  12. 130, 45]);
  13. let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyArray };
  14. let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyArray };
  15. let generator = cryptoFramework.createAsyKeyGenerator('SM2_256');
  16. generator.convertKey(pubKeyBlob, priKeyBlob, (error, data) => {
  17. if (error) {
  18. console.error(`convertKey failed: errCode: ${error.code}, message: ${error.message}`);
  19. return;
  20. }
  21. console.info('convertKey result: success.');
  22. });
  23. }
  ```

  [Callback.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/BinaryDataConvertAsymmetricKeyPairArkTS/entry/src/main/ets/pages/sm2/Callback.ets#L16-L40)
* 同步返回结果（调用方法[convertKeySync](../harmonyos-references/js-apis-cryptoframework.md#convertkeysync12)）：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. function convertSM2AsyKeySync() {
  4. let pubKeyArray =
  5. new Uint8Array([48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 129, 28, 207, 85, 1, 130, 45, 3, 66, 0,
  6. 4, 90, 3, 58, 157, 190, 248, 76, 7, 132, 200, 151, 208, 112, 230, 96, 140, 90, 238, 211, 155, 128, 109, 248, 40,
  7. 83, 214, 78, 42, 104, 106, 55, 148, 249, 35, 61, 32, 221, 135, 143, 100, 45, 97, 194, 176, 52, 73, 136, 174, 40,
  8. 70, 70, 34, 103, 103, 161, 99, 27, 187, 13, 187, 109, 244, 13, 7]);
  9. let priKeyArray =
  10. new Uint8Array([48, 49, 2, 1, 1, 4, 32, 54, 41, 239, 240, 63, 188, 134, 113, 31, 102, 149, 203, 245, 89, 15, 15, 47,
  11. 202, 170, 60, 38, 154, 28, 169, 189, 100, 251, 76, 112, 223, 156, 159, 160, 10, 6, 8, 42, 129, 28, 207, 85, 1,
  12. 130, 45]);
  13. let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyArray };
  14. let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyArray };
  15. let generator = cryptoFramework.createAsyKeyGenerator('SM2_256');
  16. try {
  17. let keyPair = generator.convertKeySync(pubKeyBlob, priKeyBlob);
  18. if (keyPair != null) {
  19. console.info('convertKeySync result: success.');
  20. }
  21. } catch (e) {
  22. console.error(`get key pair failed: errCode: ${e.code}, message: ${e.message}`);
  23. }
  24. }
  ```

  [Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/BinaryDataConvertAsymmetricKeyPairArkTS/entry/src/main/ets/pages/sm2/Sync.ets#L16-L41)
