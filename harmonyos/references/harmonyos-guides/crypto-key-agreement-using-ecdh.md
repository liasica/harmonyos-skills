---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-using-ecdh
title: 使用ECDH进行密钥协商(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥协商 > 密钥协商开发指导 > 使用ECDH进行密钥协商(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ce01ebce22c4d4f37430db24c8dbcdc3bd1ca83858af2af8c636ee6bfe2c4bcb
---

对应的算法规格请查看[密钥协商算法规格：ECDH](crypto-key-agreement-overview.md#ecdh)。

## 开发步骤

1. 调用[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)、[AsyKeyGenerator.generateKeyPair](../harmonyos-references/js-apis-cryptoframework.md#generatekeypair-1)、[AsyKeyGenerator.convertKey](../harmonyos-references/js-apis-cryptoframework.md#convertkey-3)生成密钥算法为ECC、密钥长度为256位的非对称密钥（KeyPair）。

   如何生成ECC非对称密钥，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：ECC](crypto-asym-key-generation-conversion-spec.md#ecc)和[随机生成非对称密钥对](crypto-generate-asym-key-pair-randomly.md)理解。参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[cryptoFramework.createKeyAgreement](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatekeyagreement)，指定字符串参数'ECC256'，创建密钥算法为ECC、密钥长度为256位的密钥协议生成器（KeyAgreement）。
3. 调用[KeyAgreement.generateSecret](../harmonyos-references/js-apis-cryptoframework.md#generatesecret-1)，基于传入的私钥（KeyPair.priKey）与公钥（KeyPair.pubKey）进行密钥协商，返回共享密钥。

* 以使用await方式，完成密钥协商为例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. async function ecdhAwait() {
  4. // 假设此公私钥对数据为外部传入
  5. let pubKeyArray =
  6. new Uint8Array([48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7, 3, 66, 0, 4,
  7. 83, 96, 142, 9, 86, 214, 126, 106, 247, 233, 92, 125, 4, 128, 138, 105, 246, 162, 215, 71, 81, 58, 202, 121, 26,
  8. 105, 211, 55, 130, 45, 236, 143, 55, 16, 248, 75, 167, 160, 167, 106, 2, 152, 243, 44, 68, 66, 0, 167, 99, 92,
  9. 235, 215, 159, 239, 28, 106, 124, 171, 34, 145, 124, 174, 57, 92]);
  10. let priKeyArray =
  11. new Uint8Array([48, 49, 2, 1, 1, 4, 32, 115, 56, 137, 35, 207, 0, 60, 191, 90, 61, 136, 105, 210, 16, 27, 4, 171,
  12. 57, 10, 61, 123, 40, 189, 28, 34, 207, 236, 22, 45, 223, 10, 189, 160, 10, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7]);
  13. let eccGen = cryptoFramework.createAsyKeyGenerator('ECC256');
  14. // 外部传入的公私钥对A
  15. let keyPairA = await eccGen.convertKey({ data: pubKeyArray }, { data: priKeyArray });
  16. // 内部生成的公私钥对B
  17. let keyPairB = await eccGen.generateKeyPair();
  18. let eccKeyAgreement = cryptoFramework.createKeyAgreement('ECC256');
  19. // 使用A的公钥和B的私钥进行密钥协商
  20. let secret1 = await eccKeyAgreement.generateSecret(keyPairB.priKey, keyPairA.pubKey);
  21. // 使用A的私钥和B的公钥进行密钥协商
  22. let secret2 = await eccKeyAgreement.generateSecret(keyPairA.priKey, keyPairB.pubKey);
  23. // 两种协商的结果应当一致
  24. if (secret1.data.toString() === secret2.data.toString()) {
  25. console.info('ecdh result: success.');
  26. console.info('ecdh output: ' + secret1.data);
  27. } else {
  28. console.error('ecdh result is not equal.');
  29. }
  30. }
  ```

  [EDCHAsync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyNegotiation/entry/src/main/ets/pages/ECDH/EDCHAsync.ets#L15-L47)
* 同步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. function ecdhAwait() {
  4. // 假设此公私钥对数据为外部传入
  5. let pubKeyArray =
  6. new Uint8Array([48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7, 3, 66, 0, 4,
  7. 83, 96, 142, 9, 86, 214, 126, 106, 247, 233, 92, 125, 4, 128, 138, 105, 246, 162, 215, 71, 81, 58, 202, 121, 26,
  8. 105, 211, 55, 130, 45, 236, 143, 55, 16, 248, 75, 167, 160, 167, 106, 2, 152, 243, 44, 68, 66, 0, 167, 99, 92,
  9. 235, 215, 159, 239, 28, 106, 124, 171, 34, 145, 124, 174, 57, 92]);
  10. let priKeyArray =
  11. new Uint8Array([48, 49, 2, 1, 1, 4, 32, 115, 56, 137, 35, 207, 0, 60, 191, 90, 61, 136, 105, 210, 16, 27, 4, 171,
  12. 57, 10, 61, 123, 40, 189, 28, 34, 207, 236, 22, 45, 223, 10, 189, 160, 10, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7]);
  13. let eccGen = cryptoFramework.createAsyKeyGenerator('ECC256');
  14. // 外部传入的公私钥对A
  15. let keyPairA = eccGen.convertKeySync({ data: pubKeyArray }, { data: priKeyArray });
  16. // 内部生成的公私钥对B
  17. let keyPairB = eccGen.generateKeyPairSync();
  18. let eccKeyAgreement = cryptoFramework.createKeyAgreement('ECC256');
  19. // 使用A的公钥和B的私钥进行密钥协商
  20. let secret1 = eccKeyAgreement.generateSecretSync(keyPairB.priKey, keyPairA.pubKey);
  21. // 使用A的私钥和B的公钥进行密钥协商
  22. let secret2 = eccKeyAgreement.generateSecretSync(keyPairA.priKey, keyPairB.pubKey);
  23. // 两种协商的结果应当一致
  24. if (secret1.data.toString() === secret2.data.toString()) {
  25. console.info('ecdh result: success.');
  26. console.info('ecdh output: ' + secret1.data);
  27. } else {
  28. console.error('ecdh result is not equal.');
  29. }
  30. }
  ```

  [EDCHSync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyNegotiation/entry/src/main/ets/pages/ECDH/EDCHSync.ets#L16-L49)
