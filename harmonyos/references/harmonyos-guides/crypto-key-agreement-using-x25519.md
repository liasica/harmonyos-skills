---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-using-x25519
title: 使用X25519进行密钥协商(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥协商 > 密钥协商开发指导 > 使用X25519进行密钥协商(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:db60eb601cd2e8ba350f2bee2e7fbff861d2f62070f53afd892118b8c7022bda
---

对应的算法规格请查看[密钥协商算法规格：X25519](crypto-key-agreement-overview.md#x25519)。

## 开发步骤

1. 调用[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)、[AsyKeyGenerator.generateKeyPair](../harmonyos-references/js-apis-cryptoframework.md#generatekeypair-1)、[AsyKeyGenerator.convertKey](../harmonyos-references/js-apis-cryptoframework.md#convertkey-3)生成密钥算法为X25519的非对称密钥（KeyPair）。

   如何生成X25519非对称密钥，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：X25519](crypto-asym-key-generation-conversion-spec.md#x25519)和[随机生成非对称密钥对](crypto-generate-asym-key-pair-randomly.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[cryptoFramework.createKeyAgreement](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatekeyagreement)，指定字符串参数'X25519'，创建密钥算法为X25519的密钥协议生成器（KeyAgreement）。
3. 调用[KeyAgreement.generateSecret](../harmonyos-references/js-apis-cryptoframework.md#generatesecret-1)，基于传入的私钥（KeyPair.priKey）与公钥（KeyPair.pubKey）进行密钥协商，返回共享密钥。

* 异步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. async function x25519Await() {
  4. // 假设此公私钥对数据为外部传入
  5. let pubKeyArray =
  6. new Uint8Array([48, 42, 48, 5, 6, 3, 43, 101, 110, 3, 33, 0, 36, 98, 216, 106, 74, 99, 179, 203, 81, 145, 147, 101,
  7. 139, 57, 74, 225, 119, 196, 207, 0, 50, 232, 93, 147, 188, 21, 225, 228, 54, 251, 230, 52]);
  8. let priKeyArray =
  9. new Uint8Array([48, 46, 2, 1, 0, 48, 5, 6, 3, 43, 101, 110, 4, 34, 4, 32, 112, 65, 156, 73, 65, 89, 183, 39, 119,
  10. 229, 110, 12, 192, 237, 186, 153, 21, 122, 28, 176, 248, 108, 22, 242, 239, 179, 106, 175, 85, 65, 214, 90]);
  11. let keyGen = cryptoFramework.createAsyKeyGenerator('X25519');
  12. // 外部传入的公私钥对A
  13. let keyPairA = await keyGen.convertKey({ data: pubKeyArray }, { data: priKeyArray });
  14. // 内部生成的公私钥对B
  15. let keyPairB = await keyGen.generateKeyPair();
  16. let keyAgreement = cryptoFramework.createKeyAgreement('X25519');
  17. // 使用A的公钥和B的私钥进行密钥协商
  18. let secret1 = await keyAgreement.generateSecret(keyPairB.priKey, keyPairA.pubKey);
  19. // 使用A的私钥和B的公钥进行密钥协商
  20. let secret2 = await keyAgreement.generateSecret(keyPairA.priKey, keyPairB.pubKey);
  21. // 两种协商的结果应当一致
  22. if (secret1.data.toString() === secret2.data.toString()) {
  23. console.info('x25519 result: success.');
  24. console.info('x25519 output: ' + secret1.data);
  25. } else {
  26. console.error('x25519 result is not equal.');
  27. }
  28. }
  ```

  [X25519Async.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyNegotiation/entry/src/main/ets/pages/X25519/X25519Async.ets#L15-L44)
* 同步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. function x25519Await() {
  4. // 假设此公私钥对数据为外部传入
  5. let pubKeyArray =
  6. new Uint8Array([48, 42, 48, 5, 6, 3, 43, 101, 110, 3, 33, 0, 36, 98, 216, 106, 74, 99, 179, 203, 81, 145, 147, 101,
  7. 139, 57, 74, 225, 119, 196, 207, 0, 50, 232, 93, 147, 188, 21, 225, 228, 54, 251, 230, 52]);
  8. let priKeyArray =
  9. new Uint8Array([48, 46, 2, 1, 0, 48, 5, 6, 3, 43, 101, 110, 4, 34, 4, 32, 112, 65, 156, 73, 65, 89, 183, 39, 119,
  10. 229, 110, 12, 192, 237, 186, 153, 21, 122, 28, 176, 248, 108, 22, 242, 239, 179, 106, 175, 85, 65, 214, 90]);
  11. let keyGen = cryptoFramework.createAsyKeyGenerator('X25519');
  12. // 外部传入的公私钥对A
  13. let keyPairA = keyGen.convertKeySync({ data: pubKeyArray }, { data: priKeyArray });
  14. // 内部生成的公私钥对B
  15. let keyPairB = keyGen.generateKeyPairSync();
  16. let keyAgreement = cryptoFramework.createKeyAgreement('X25519');
  17. // 使用A的公钥和B的私钥进行密钥协商
  18. let secret1 = keyAgreement.generateSecretSync(keyPairB.priKey, keyPairA.pubKey);
  19. // 使用A的私钥和B的公钥进行密钥协商
  20. let secret2 = keyAgreement.generateSecretSync(keyPairA.priKey, keyPairB.pubKey);
  21. // 两种协商的结果应当一致
  22. if (secret1.data.toString() === secret2.data.toString()) {
  23. console.info('x25519 result: success.');
  24. console.info('x25519 output: ' + secret1.data);
  25. } else {
  26. console.error('x25519 result is not equal.');
  27. }
  28. }
  ```

  [X25519Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyNegotiation/entry/src/main/ets/pages/X25519/X25519Sync.ets#L15-L44)
