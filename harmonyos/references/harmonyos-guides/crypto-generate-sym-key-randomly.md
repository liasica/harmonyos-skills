---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-sym-key-randomly
title: 随机生成对称密钥(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥生成和转换 > 密钥生成和转换开发指导 > 随机生成对称密钥(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fc83555bdd53160b6116b61f828d23a3447584458c9376f8a3e75186a9f8a588
---

以AES和SM4为例，随机生成对称密钥（SymKey），并获得二进制数据。

对称密钥对象可用于后续加解密操作，二进制数据可用于存储或传输。

## 随机生成AES密钥

对应的算法规格请查看[对称密钥生成和转换规格：AES](crypto-sym-key-generation-conversion-spec.md#aes)。

1. 调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)，指定字符串参数'AES256'，创建密钥算法为AES、密钥长度为256位的对称密钥生成器（SymKeyGenerator）。
2. 调用[SymKeyGenerator.generateSymKey](../harmonyos-references/js-apis-cryptoframework.md#generatesymkey-1)，随机生成对称密钥对象（SymKey）。
3. 调用[SymKey.getEncoded](../harmonyos-references/js-apis-cryptoframework.md#getencoded)，获取密钥对象的二进制数据。

* 以使用Promise方式随机生成AES密钥为例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. function testGenerateAesKey() {
  4. // 创建SymKeyGenerator实例
  5. let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES256');
  6. // 使用密钥生成器随机生成对称密钥
  7. let promiseSymKey = symKeyGenerator.generateSymKey();
  8. promiseSymKey.then(key => {
  9. // 获取对称密钥的二进制数据，输出256位密钥。长度为32字节
  10. let encodedKey = key.getEncoded();
  11. console.info('key hex: ' + encodedKey.data);
  12. });
  13. }
  ```

  [Promise.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/RandomlyGenerateSymmetricKeyArkTS/entry/src/main/ets/pages/aes/Promise.ets#L16-L30)
* 同步方法（调用方法[generateSymKeySync](../harmonyos-references/js-apis-cryptoframework.md#generatesymkeysync12)）：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. function testSyncGenerateAesKey() {
  4. // 创建SymKeyGenerator实例
  5. let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES256');
  6. // 使用密钥生成器随机生成对称密钥
  7. let promiseSymKey = symKeyGenerator.generateSymKeySync();
  8. // 获取对称密钥的二进制数据，输出256位密钥。长度为32字节
  9. let encodedKey = promiseSymKey.getEncoded();
  10. console.info('key hex: ' + encodedKey.data);
  11. }
  ```

  [Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/RandomlyGenerateSymmetricKeyArkTS/entry/src/main/ets/pages/aes/Sync.ets#L16-L28)

## 随机生成SM4密钥

对应的算法规格请查看[对称密钥生成和转换规格：SM4](crypto-sym-key-generation-conversion-spec.md#sm4)。

1. 调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)，指定字符串参数'SM4\_128'，创建密钥算法为SM4、密钥长度为128位的对称密钥生成器（SymKeyGenerator）。

   如果开发者需要使用其他算法，请注意修改此处入参的字符串参数。
2. 调用[SymKeyGenerator.generateSymKey](../harmonyos-references/js-apis-cryptoframework.md#generatesymkey-1)，随机生成对称密钥对象（SymKey）。
3. 调用[SymKey.getEncoded](../harmonyos-references/js-apis-cryptoframework.md#getencoded)，获取密钥对象的二进制数据。

* 以使用Promise方式随机生成SM4密钥为例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. function testGenerateSM4Key() {
  4. // 创建SymKeyGenerator实例
  5. let symKeyGenerator = cryptoFramework.createSymKeyGenerator('SM4_128');
  6. // 使用密钥生成器随机生成对称密钥
  7. let promiseSymKey = symKeyGenerator.generateSymKey();
  8. promiseSymKey.then(key => {
  9. // 获取对称密钥的二进制数据，输出128位字节流。长度为16字节
  10. let encodedKey = key.getEncoded();
  11. console.info('key hex: ' + encodedKey.data);
  12. });
  13. }
  ```

  [Promise.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/RandomlyGenerateSymmetricKeyArkTS/entry/src/main/ets/pages/sm4/Promise.ets#L16-L30)
* 同步方法（调用方法[generateSymKeySync](../harmonyos-references/js-apis-cryptoframework.md#generatesymkeysync12)）：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. function testSyncGenerateSm4Key() {
  4. // 创建SymKeyGenerator实例
  5. let symKeyGenerator = cryptoFramework.createSymKeyGenerator('SM4_128');
  6. // 使用密钥生成器随机生成对称密钥
  7. let promiseSymKey = symKeyGenerator.generateSymKeySync();
  8. // 获取对称密钥的二进制数据，输出128位字节流。长度为16字节
  9. let encodedKey = promiseSymKey.getEncoded();
  10. console.info('key hex: ' + encodedKey.data);
  11. }
  ```

  [Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/RandomlyGenerateSymmetricKeyArkTS/entry/src/main/ets/pages/sm4/Sync.ets#L16-L28)
